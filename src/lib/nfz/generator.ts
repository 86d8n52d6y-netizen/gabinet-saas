// Strony modułów Opisy NFZ i Opisy prywatne: pliki z katalogu generator/ (poza public/ – kod widoczny tylko dla zalogowanych z licencją).
import 'server-only';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { withUser } from '../db';
import { getSession } from '../session';
import { cleanNfz } from '../settings';
import { cleanUi } from './ui';
import { listVisits } from './wizyty';
import { BLOB_KEYS, getBlobs, listPryw } from '../pryw/wizyty';

const DIR = path.join(process.cwd(), 'generator');
const TYPES: Record<string, string> = { js: 'text/javascript; charset=utf-8', css: 'text/css; charset=utf-8', woff2: 'font/woff2', html: 'text/html; charset=utf-8' };
export const ASSETS = /^(gabinet-saas\.js|szablony\.js|prywatne-katalog\.js|wspolne\.css|fonts\.css|ibm-plex-(sans|mono)-latin(-ext)?-[4-7]00-normal\.woff2)$/;

const cache = new Map<string, { buf: Buffer; etag: string }>();
async function file(name: string) {
  let f = cache.get(name);
  if (!f || process.env.NODE_ENV !== 'production') {
    const buf = await readFile(path.join(DIR, name.endsWith('.woff2') ? 'fonts' : '', name));
    f = { buf, etag: '"' + createHash('sha1').update(buf).digest('hex').slice(0, 16) + '"' };
    cache.set(name, f);
  }
  return f;
}

/** Dostęp: zalogowany z ukończonym 2FA i aktywną licencją. Zwraca id użytkownika albo adres przekierowania. */
export async function access(): Promise<{ uid: string; name: string } | { go: string }> {
  const s = await getSession();
  if (!s) return { go: '/logowanie' };
  if (!s.mfaPassed) return { go: '/logowanie/2fa' };
  const ok = await withUser(s.userId, async c => (await c.query('SELECT app.has_access() AS a')).rows[0].a as boolean);
  return ok ? { uid: s.userId, name: s.displayName } : { go: '/konto?dostep=brak' };
}

export async function asset(name: string, ifNoneMatch: string | null): Promise<Response> {
  const f = await file(name);
  const h = { 'Content-Type': TYPES[name.split('.').pop()!], 'Cache-Control': 'private, no-cache', ETag: f.etag, 'X-Content-Type-Options': 'nosniff' };
  if (ifNoneMatch === f.etag) return new Response(null, { status: 304, headers: h });
  return new Response(new Uint8Array(f.buf), { headers: h });
}

/** Strona modułu z danymi startowymi konta (bez treści opisów – tych w chmurze nie ma). */
export async function page(uid: string, name: string, mod: 'nfz' | 'prywatne' = 'nfz'): Promise<Response> {
  const data = await withUser(uid, async c => {
    const st = (await c.query('SELECT settings FROM app.user_settings')).rows[0]?.settings ?? {};
    const clinics = (await c.query(`SELECT id, name, short, color, active FROM app.clinics WHERE deleted_at IS NULL ORDER BY active DESC, sort, created_at`)).rows;
    if (mod === 'prywatne') return { uid, name, mod, clinics, blobs: await getBlobs(c, BLOB_KEYS), visits: await listPryw(c) };
    return { uid, name, mod, clinics, cfg: { ...cleanNfz(st.nfz), ...cleanUi(st.nfzUi) }, seg: st.nfzSeg ?? null, visits: await listVisits(c) };
  });
  const json = JSON.stringify(data).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
  const html = (await file(mod === 'prywatne' ? 'prywatne.html' : 'nfz.html')).buf.toString('utf8').replace('<!--GABINET_DANE-->', `<script>window.__GABINET=${json};</script>`);
  return new Response(html, { headers: { 'Content-Type': TYPES.html, 'Cache-Control': 'no-store', 'Referrer-Policy': 'same-origin' } });
}
