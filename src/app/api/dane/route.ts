// Materiały gabinetowe modułów (cennik, ustawienia, własne szablony, zestawy) – bez danych pacjentów; tylko klucze z listy.
// Kontrola wersji: zapis od nieaktualnej wersji (zmiana na innym urządzeniu) → 409 z aktualnymi danymi; urządzenie scala i wysyła ponownie.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { BLOB_KEYS, getBlobVers } from '@/lib/pryw/wizyty';

export async function POST(req: Request) {
  const a = await apiAuth(req, 1_000_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { key?: unknown; data?: unknown; base?: unknown; since?: unknown };
  if (b.since && typeof b.since === 'object') {                                        // odświeżenie: materiały zmienione na innym urządzeniu
    const known = b.since as Record<string, unknown>;
    const out = await withUser(a.s.userId, async c => {
      const v = await getBlobVers(c, BLOB_KEYS);
      const ch = BLOB_KEYS.filter(k => v[k] && Number(known[k] ?? 0) !== v[k]);
      const rows = ch.length ? (await c.query('SELECT key, data, version FROM app.user_blobs WHERE key = ANY($1)', [ch])).rows : [];
      return Object.fromEntries(rows.map(r => [r.key, { data: r.data, version: r.version }]));
    });
    return json({ ok: true, changed: out });
  }
  if (typeof b.key !== 'string' || !(BLOB_KEYS as readonly string[]).includes(b.key)) return json({ error: 'Nieznany klucz.' }, 400);
  if (b.data === null || typeof b.data !== 'object') return json({ error: 'Oczekiwano obiektu.' }, 400);
  const base = b.base === undefined ? null : Math.max(0, Math.floor(Number(b.base) || 0));
  try {
    const r = await withUser(a.s.userId, async c => {
      const cur = (await c.query('SELECT data, version FROM app.user_blobs WHERE key = $1 FOR UPDATE', [b.key])).rows[0];
      if (base !== null && (cur?.version ?? 0) !== base) return { conflict: { data: cur?.data ?? null, version: cur?.version ?? 0 } };
      const v = (await c.query(`INSERT INTO app.user_blobs(owner_id, key, data) VALUES ($1, $2, $3::jsonb)
        ON CONFLICT (owner_id, key) DO UPDATE SET data = EXCLUDED.data RETURNING version`, [a.s.userId, b.key, JSON.stringify(b.data)])).rows[0].version;
      return { version: v as number };
    });
    if ('conflict' in r) return json({ error: 'Zmienione na innym urządzeniu.', conflict: r.conflict }, 409);
    return json({ ok: true, version: r.version });
  } catch (e) {
    if ((e as { code?: string }).code === '23514') return json({ error: 'Za dużo danych (limit 1 MB).' }, 413);
    throw e;
  }
}
