// Historia wizyt prywatnych w chmurze: data, gabinet, procedury (nazwa, kategoria, ilość), ceny, koszty, wynagrodzenie.
// NIE przyjmujemy: treści opisu, wartości pól szablonu (vals – np. zęby, materiały), zwolnienia e-ZLA, inicjałów pacjenta.
import 'server-only';
import { createHash } from 'node:crypto';
import type { PoolClient } from 'pg';

const ID = /^[A-Za-z0-9_-]{1,40}$/, UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const ISO = (s: unknown) => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$/.test(s) && !isNaN(Date.parse(s)) ? s : null;
const DATE = (s: unknown) => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s + 'T00:00:00Z')) && s >= '2000-01-01' && s <= '2100-12-31';
const gr = (v: unknown) => { const n = Number(v); return Number.isInteger(n) && n >= 0 && n <= 1e10 ? n : null; };
const clean = (s: unknown, max: number) => String(s ?? '').replace(/[\u0000-\u001f<>]/g, ' ').trim().slice(0, max);

export type Item = { pid: string; name: string; kat: string; qty: number; c: number; m: string; p: number | null; kw: number; cost: number; val: number; pay: number };
export type PMeta = { id: string; no: number; date: string; gab: string; created: string; at: string; edited: boolean; items: Item[]; val: number; pay: number; cost: number };

export function cleanPryw(x: unknown): PMeta | null {
  if (!x || typeof x !== 'object') return null;
  const o = x as Record<string, unknown>;
  if (typeof o.id !== 'string' || !ID.test(o.id) || !DATE(o.date)) return null;
  const at = ISO(o.at), created = ISO(o.created) ?? at;
  if (!at || !created || !Array.isArray(o.items)) return null;
  const items: Item[] = [];
  for (const raw of o.items.slice(0, 60)) {
    if (!raw || typeof raw !== 'object') return null;
    const i = raw as Record<string, unknown>;
    const qty = Number(i.qty), val = gr(i.val), pay = gr(i.pay ?? 0), cost = gr(i.cost ?? 0), c = gr(i.c ?? 0), kw = gr(i.kw ?? 0);
    if (!(Number.isInteger(qty) && qty >= 1 && qty <= 99) || [val, pay, cost, c, kw].includes(null)) return null;
    const p = i.p === null || i.p === undefined ? null : Number(i.p);
    items.push({ pid: clean(i.pid, 60).replace(/[^A-Za-z0-9_-]/g, ''), name: clean(i.name, 120), kat: clean(i.kat, 60), qty, c: c!, m: i.m === 'kw' ? 'kw' : i.m === 'p' ? 'p' : String(i.m ?? '').slice(0, 8).replace(/[^a-z]/g, ''),
      p: p === null || !(p >= 0 && p <= 100) ? null : p, kw: kw!, cost: cost!, val: val!, pay: pay! });
  }
  const sum = (k: 'val' | 'pay' | 'cost') => items.reduce((s, i) => s + i[k], 0);
  return { id: o.id, no: Number.isInteger(o.no) && (o.no as number) > 0 && (o.no as number) < 1e9 ? o.no as number : 1, date: o.date as string,
    gab: typeof o.gab === 'string' && UUID.test(o.gab) ? o.gab : '', created, at, edited: o.edited === true, items,
    val: sum('val'), pay: sum('pay'), cost: sum('cost') };      // sumy liczone na serwerze z pozycji (nie z deklaracji urządzenia)
}

const clientUuid = (key: string) => { const h = createHash('sha256').update('gabinet-pryw:' + key).digest('hex');
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-4${h.slice(13, 16)}-8${h.slice(17, 20)}-${h.slice(20, 32)}`; };

export async function upsertPryw(c: PoolClient, owner: string, m: PMeta): Promise<boolean> {
  let gab: string | null = m.gab || null;
  if (gab && !(await c.query('SELECT 1 FROM app.clinics WHERE id = $1', [gab])).rowCount) gab = null;
  const r = await c.query(
    `INSERT INTO app.saved_descriptions AS s (owner_id, client_id, client_key, client_at, module, visit_date, clinic_id, seq_no, edited, meta)
     VALUES ($1, $2, $3, $4, 'private', $5, $6, $7, $8, $9::jsonb)
     ON CONFLICT (owner_id, client_id) DO UPDATE SET client_at = EXCLUDED.client_at, visit_date = EXCLUDED.visit_date, clinic_id = EXCLUDED.clinic_id,
       seq_no = EXCLUDED.seq_no, edited = EXCLUDED.edited, meta = EXCLUDED.meta, deleted_at = NULL, status = 'active'
     WHERE s.client_at IS NULL OR s.client_at < EXCLUDED.client_at
     RETURNING id`,
    [owner, clientUuid(m.id), m.id, m.at, m.date, gab, m.no, m.edited, JSON.stringify({ created: m.created, items: m.items })]);
  const id = r.rows[0]?.id;
  if (!id) return false;
  await c.query('DELETE FROM app.earnings_entries WHERE description_id = $1', [id]);
  let line = 0;
  for (const i of m.items)
    await c.query(`INSERT INTO app.earnings_entries(owner_id, description_id, line_no, entry_date, clinic_id, source, label, category_name, qty, value_gr, cost_gr, doctor_pay_gr)
                   VALUES ($1,$2,$3,$4,$5,'private_procedure',$6,$7,$8,$9,$10,$11)`, [owner, id, line++, m.date, gab, i.name || 'Procedura', i.kat || null, i.qty, i.val, i.cost, i.pay]);
  return true;
}

export async function deletePryw(c: PoolClient, key: string, at: string) {
  const r = await c.query(`UPDATE app.saved_descriptions SET deleted_at = $2, status = 'deleted', client_at = $2
     WHERE client_key = $1 AND module = 'private' AND deleted_at IS NULL AND (client_at IS NULL OR client_at <= $2) RETURNING id`, [key, at]);
  if (r.rows[0]) await c.query('UPDATE app.earnings_entries SET deleted_at = $2 WHERE description_id = $1', [r.rows[0].id, at]);
}

export async function listPryw(c: PoolClient) {
  const r = await c.query(`SELECT client_key, client_at, deleted_at, visit_date::text, clinic_id, seq_no, edited, meta FROM app.saved_descriptions
                            WHERE module = 'private' AND client_key IS NOT NULL ORDER BY visit_date DESC`);
  const live: Record<string, unknown>[] = [], gone: { id: string; at: string }[] = [];
  for (const x of r.rows) {
    if (x.deleted_at) { gone.push({ id: x.client_key, at: new Date(x.deleted_at).toISOString() }); continue; }
    const items = (x.meta.items ?? []) as Item[];
    live.push({ id: x.client_key, v: 1, no: x.seq_no, date: x.visit_date, gab: x.clinic_id ?? '', ini: '', created: x.meta.created, at: new Date(x.client_at).toISOString(),
      items: items.map(i => ({ ...i, vals: {} })), n: items.length, val: items.reduce((s, i) => s + i.val, 0), pay: items.reduce((s, i) => s + i.pay, 0),
      cost: items.reduce((s, i) => s + i.cost, 0), ezla: null, edited: x.edited, body: false, cloud: true });
  }
  return { live, gone };
}

// ---- materiały gabinetowe (bez danych pacjentów) ----
export const BLOB_KEYS = ['pryw:cennik', 'pryw:ust', 'pryw:katalog', 'pryw:zestawy'] as const;
export async function getBlobs(c: PoolClient, keys: readonly string[]) {
  const r = await c.query('SELECT key, data FROM app.user_blobs WHERE key = ANY($1)', [keys]);
  return Object.fromEntries(r.rows.map(x => [x.key, x.data]));
}
