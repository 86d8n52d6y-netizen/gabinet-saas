// Zlecenia protetyczne w chmurze (etap E7, decyzja 17): treść zlecenia (numer, inicjały, rodzaj pracy, zęby, kolor, zgryz, implanty,
// statusy, historia) z kontrolą wersji. NIGDY: imię i nazwisko, PESEL, adres, zdjęcia – pola spoza listy są odrzucane (zasada nr 1).
import 'server-only';
import type { PoolClient } from 'pg';

export const ID = /^z[a-z0-9]{6,24}$/;
const TOP = new Set(['id', 'nr', 'typ', 'status', 'data', 'a', 'hist', 'at']);
const TOP_LEN: Record<string, number> = { id: 26, nr: 40, typ: 120, status: 40, data: 10, at: 40 };
const KEY = /^[A-Za-z]{1,30}$/;
const ZAKAZ = /^(imie|nazwisko|pacjent|pesel|adres|telefon|email|zdjecia|zdjecie|foto|fotos|photo|photos)$/i;   // dane identyfikujące i zdjęcia – nigdy na serwer
const FDI = /^[1-8][0-9]$/;

export class Bledne extends Error {}
const bad = (m: string): never => { throw new Bledne('Nieprawidłowe zlecenie: ' + m); };
const str = (v: unknown, max: number, co: string) => typeof v === 'string' && v.length <= max ? v : bad(co);

/** Tylko pola z listy, w znanych kształtach. Zwraca kopię gotową do zapisu albo rzuca Bledne. */
export function clean(o: unknown): Record<string, unknown> {
  if (!o || typeof o !== 'object' || Array.isArray(o)) bad('format');
  const src = o as Record<string, unknown>, out: Record<string, unknown> = {};
  for (const [k, v] of Object.entries(src)) {
    if (!TOP.has(k)) bad('niedozwolone pole „' + k.slice(0, 30) + '”');
    if (k === 'a') {
      if (!v || typeof v !== 'object' || Array.isArray(v)) bad('pola zlecenia');
      const a: Record<string, unknown> = {};
      const ent = Object.entries(v as Record<string, unknown>); if (ent.length > 150) bad('za dużo pól');
      for (const [f, x] of ent) {
        if (!KEY.test(f) || ZAKAZ.test(f)) bad('niedozwolone pole „' + f.slice(0, 30) + '”');
        if (typeof x === 'string') a[f] = str(x, 4000, f);
        else if (typeof x === 'boolean' || x === null) a[f] = x;
        else if (typeof x === 'number' && Number.isFinite(x)) a[f] = x;
        else if (Array.isArray(x)) { if (x.length > 60) bad(f); a[f] = x.map(y => str(y, 300, f)); }
        else if (typeof x === 'object') {                                                 // schemat zębów / uwagi do zębów: numer FDI → tekst
          const e2 = Object.entries(x as Record<string, unknown>); if (e2.length > 60) bad(f);
          a[f] = Object.fromEntries(e2.map(([z, y]) => [FDI.test(z) ? z : bad(f), str(y, 500, f)]));
        } else bad(f);
      }
      out.a = a;
    } else if (k === 'hist') {
      if (!Array.isArray(v) || v.length > 100) bad('historia');
      out.hist = (v as unknown[]).map(h => { const x = h as Record<string, unknown>;
        if (!x || typeof x !== 'object' || Object.keys(x).some(q => q !== 'at' && q !== 'co')) bad('historia');
        return { at: str(x.at, 40, 'historia'), co: str(x.co, 300, 'historia') }; });
    } else out[k] = str(v, TOP_LEN[k], k);
  }
  if (typeof out.id !== 'string' || !ID.test(out.id)) bad('identyfikator');
  return out;
}

type Cur = { data: Record<string, unknown> | null; version: number; deleted: boolean };
async function current(c: PoolClient, id: string): Promise<Cur> {
  const r = (await c.query('SELECT data, version, deleted FROM app.prosthetic_orders WHERE id = $1', [id])).rows[0];
  return r ? { data: r.deleted ? null : r.data, version: r.version, deleted: r.deleted } : { data: null, version: 0, deleted: true };   // usunięte: prawdziwa wersja (ponowny zapis z tą bazą przywraca zlecenie)
}

/** Zapis z kontrolą wersji: base = wersja znana urządzeniu; inna niż w bazie → konflikt (urządzenie scala i wysyła ponownie). */
export async function saveOrders(c: PoolClient, owner: string, put: { o: unknown; base: unknown }[], del: { id: unknown; base: unknown }[]) {
  const ver: Record<string, number> = {}, conflict: Record<string, Cur> = {};
  const baseOf = (b: unknown) => Math.max(0, Math.floor(Number(b) || 0));
  for (const p of put) {
    const o = clean(p.o), id = o.id as string;
    const cur = (await c.query('SELECT version FROM app.prosthetic_orders WHERE id = $1 FOR UPDATE', [id])).rows[0]?.version ?? 0;
    if (cur !== baseOf(p.base)) { conflict[id] = await current(c, id); continue; }
    ver[id] = (await c.query(`INSERT INTO app.prosthetic_orders(owner_id, id, data) VALUES ($1, $2, $3::jsonb)
        ON CONFLICT (owner_id, id) DO UPDATE SET data = EXCLUDED.data, deleted = false RETURNING version`, [owner, id, JSON.stringify(o)])).rows[0].version;
  }
  for (const d of del) {
    const id = typeof d.id === 'string' && ID.test(d.id) ? d.id : bad('identyfikator');
    const cur = (await c.query('SELECT version, deleted FROM app.prosthetic_orders WHERE id = $1 FOR UPDATE', [id])).rows[0];
    if (!cur || cur.deleted) { ver[id] = 0; continue; }
    if (cur.version !== baseOf(d.base)) { conflict[id] = await current(c, id); continue; }
    await c.query(`UPDATE app.prosthetic_orders SET deleted = true, data = '{}'::jsonb WHERE id = $1`, [id]); ver[id] = 0;
  }
  return { ver, conflict };
}

/** Zlecenia zmienione względem wersji znanych urządzeniu (nowe, zmienione, usunięte). */
export async function changedOrders(c: PoolClient, known: Record<string, unknown>) {
  const rows = (await c.query('SELECT id, version, deleted, data FROM app.prosthetic_orders')).rows as { id: string; version: number; deleted: boolean; data: Record<string, unknown> }[];
  const out: Record<string, Cur> = {}, ids = new Set(rows.map(r => r.id));
  for (const r of rows) {
    const k = Math.floor(Number(known[r.id]) || 0);
    if (r.deleted ? k > 0 : k !== r.version) out[r.id] = { data: r.deleted ? null : r.data, version: r.deleted ? 0 : r.version, deleted: r.deleted };
  }
  for (const k of Object.keys(known)) if (Number(known[k]) > 0 && !ids.has(k) && ID.test(k)) out[k] = { data: null, version: 0, deleted: true };
  return out;
}
