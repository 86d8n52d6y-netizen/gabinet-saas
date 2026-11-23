// Historia wizyt generatora NFZ w chmurze (decyzja 1): data, gabinet, kody, punkty, stawki z dnia zapisu, kwoty, czas.
// NIE przyjmujemy: treści opisu, odpowiedzi z formularza (wiek, zęby, rozpoznania), inicjałów pacjenta.
// Konflikty dwóch urządzeń: wygrywa wpis o nowszym czasie zmiany (client_at); usunięcie to znacznik deleted_at.
import 'server-only';
import { createHash } from 'node:crypto';
import type { PoolClient } from 'pg';
import { visitMoney } from './engine';

export type Meta = {
  id: string; no: number; date: string; created: string; at: string; src: 'gen' | 'man'; codes: string[];
  pts: number; price: number; pct: number; revH: number; revRate: number; ex: { c: number; d: string }[];
  min: number | null; miss: number; gab: string;
};

const ID = /^[A-Za-z0-9_-]{1,40}$/, UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const ISO = (s: unknown) => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$/.test(s) && !isNaN(Date.parse(s)) ? s : null;
const DATE = (s: unknown) => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s + 'T00:00:00Z')) && s >= '2000-01-01' && s <= '2100-12-31';
const num = (v: unknown, lo: number, hi: number) => { const n = Number(v); return Number.isFinite(n) && n >= lo && n <= hi ? n : null; };
const r2 = (x: number) => Math.round(x * 100) / 100;
const clean = (s: unknown, max: number) => String(s ?? '').replace(/[\u0000-\u001f<>]/g, ' ').trim().slice(0, max);

/** Ścisła walidacja wpisu z urządzenia (te same granice co normMeta w generatorze). null = odrzucony. Inicjały są pomijane. */
export function cleanMeta(x: unknown): Meta | null {
  if (!x || typeof x !== 'object') return null;
  const o = x as Record<string, unknown>;
  if (typeof o.id !== 'string' || !ID.test(o.id) || !DATE(o.date)) return null;
  const at = ISO(o.at), created = ISO(o.created) ?? at;
  if (!at || !created) return null;
  const pts = num(o.pts, 0, 1e6), price = num(o.price, 0.0001, 99.9999), pct = num(o.pct, 0, 100);
  const revH = num(o.revH, 0, 24), revRate = num(o.revRate, 0, 1e5);
  if ([pts, price, pct, revH, revRate].includes(null)) return null;
  const ex = Array.isArray(o.ex) ? o.ex.slice(0, 30).map(e => ({ c: Math.round(Number((e as { c?: unknown })?.c)), d: clean((e as { d?: unknown })?.d, 120) }))
    .filter(e => Number.isInteger(e.c) && e.c > 0 && e.c <= 1e10) : [];
  const min = o.min === null || o.min === undefined || o.min === '' ? null : num(o.min, 0, 1440);
  return {
    id: o.id, no: Number.isInteger(o.no) && (o.no as number) > 0 && (o.no as number) < 1e9 ? o.no as number : 1,
    date: o.date as string, created, at, src: o.src === 'man' ? 'man' : 'gen',
    codes: Array.isArray(o.codes) ? o.codes.filter(c => typeof c === 'string' && /^[A-Za-z0-9.]{1,10}$/.test(c)).slice(0, 40) as string[] : [],
    pts: r2(pts!), price: price!, pct: pct!, revH: r2(revH!), revRate: revRate!, ex,
    min: min === null ? null : Math.round(min), miss: Number.isInteger(o.miss) && (o.miss as number) > 0 ? Math.min(o.miss as number, 999) : 0,
    gab: typeof o.gab === 'string' && UUID.test(o.gab) ? o.gab : '',
  };
}

/** Stały UUID wpisu z identyfikatora urządzenia (ponowne wysłanie = ten sam wiersz). */
export const clientUuid = (key: string) => {
  const h = createHash('sha256').update('gabinet-nfz:' + key).digest('hex');
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-4${h.slice(13, 16)}-8${h.slice(17, 20)}-${h.slice(20, 32)}`;
};

/** Zapis (wstawienie lub zmiana, jeśli wpis z urządzenia jest nowszy). Zwraca true, gdy zapisano. */
export async function upsertVisit(c: PoolClient, owner: string, m: Meta): Promise<boolean> {
  let gab: string | null = m.gab || null;
  if (gab && !(await c.query('SELECT 1 FROM app.clinics WHERE id = $1', [gab])).rowCount) gab = null;   // nieznany / cudzy gabinet (RLS) → bez gabinetu
  const r = await c.query(
    `INSERT INTO app.saved_descriptions AS s (owner_id, client_id, client_key, client_at, module, visit_date, clinic_id, seq_no, minutes, review_hours, rates, codes, meta)
     VALUES ($1, $2, $3, $4, 'nfz', $5, $6, $7, $8, $9, $10::jsonb, $11, $12::jsonb)
     ON CONFLICT (owner_id, client_id) DO UPDATE SET client_at = EXCLUDED.client_at, visit_date = EXCLUDED.visit_date, clinic_id = EXCLUDED.clinic_id,
       seq_no = EXCLUDED.seq_no, minutes = EXCLUDED.minutes, review_hours = EXCLUDED.review_hours, rates = EXCLUDED.rates, codes = EXCLUDED.codes,
       meta = EXCLUDED.meta, deleted_at = NULL, status = 'active'
     WHERE s.client_at IS NULL OR s.client_at < EXCLUDED.client_at
     RETURNING id`,
    [owner, clientUuid(m.id), m.id, m.at, m.date, gab, m.no, m.min, m.revH,
      JSON.stringify({ pts: m.pts, price: m.price, pct: m.pct, revRate: m.revRate }), m.codes,
      JSON.stringify({ src: m.src, created: m.created, miss: m.miss, ex: m.ex })]);
  const id = r.rows[0]?.id;
  if (!id) return false;
  // kwoty do statystyk – jedyne źródło sum; te same zaokrąglenia co w generatorze
  const k = visitMoney(m, 'full');
  await c.query('DELETE FROM app.earnings_entries WHERE description_id = $1', [id]);
  const rows: [number, string, string | null, number | null, number, number][] = [];
  if (m.pts > 0 || m.codes.length) rows.push([0, 'nfz_points', 'Punkty NFZ', m.pts, k.pc, k.sh]);
  if (k.rv > 0) rows.push([1, 'nfz_review', 'Przeglądy', null, k.rv, k.rv]);
  m.ex.forEach((e, i) => rows.push([2 + i, 'nfz_extra', e.d || 'Kwota dodatkowa', null, e.c, e.c]));
  for (const [line, src, label, points, value, pay] of rows)
    await c.query(`INSERT INTO app.earnings_entries(owner_id, description_id, line_no, entry_date, clinic_id, source, label, points, value_gr, doctor_pay_gr)
                   VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10)`, [owner, id, line, m.date, gab, src, label, points, value, pay]);
  return true;
}

/** Usunięcie (znacznik czasu; kwoty znikają ze statystyk). Starsze usunięcie nie kasuje nowszej zmiany z innego urządzenia. */
export async function deleteVisit(c: PoolClient, key: string, at: string): Promise<void> {
  const r = await c.query(`UPDATE app.saved_descriptions SET deleted_at = $2, status = 'deleted', client_at = $2
                           WHERE client_key = $1 AND module = 'nfz' AND deleted_at IS NULL AND (client_at IS NULL OR client_at <= $2) RETURNING id`, [key, at]);
  if (r.rows[0]) await c.query('UPDATE app.earnings_entries SET deleted_at = $2 WHERE description_id = $1', [r.rows[0].id, at]);
}

/** Lista z chmury (do scalenia na urządzeniu): wpisy i znaczniki usunięć. */
/** Wizyty z zakładki „NFZ” (karty procedur, etap E4) mają identyfikator z przedrostkiem „k-”: ta sama tabela i Zarobki,
 *  ale osobne listy – Opisy NFZ dostają tylko swoje wpisy (ich historia i scalanie bez zmian), zakładka „NFZ” – tylko swoje. */
export const KARTY_PREFIX = 'k-';
export async function listVisits(c: PoolClient, zrodlo: 'opisy' | 'karty' = 'opisy') {
  const r = await c.query(`SELECT client_key, client_at, deleted_at, visit_date::text, clinic_id, seq_no, minutes, review_hours::float8, rates, codes, meta
                             FROM app.saved_descriptions WHERE module = 'nfz' AND client_key IS NOT NULL AND (left(client_key, 2) = $1) = $2 ORDER BY visit_date DESC`,
    [KARTY_PREFIX, zrodlo === 'karty']);
  const live: Record<string, unknown>[] = [], gone: { id: string; at: string }[] = [];
  for (const x of r.rows) {
    if (x.deleted_at) { gone.push({ id: x.client_key, at: new Date(x.deleted_at).toISOString() }); continue; }
    live.push({ id: x.client_key, v: 2, no: x.seq_no, ini: '', date: x.visit_date, created: x.meta.created, at: new Date(x.client_at).toISOString(),
      src: x.meta.src, codes: x.codes, pts: Number(x.rates.pts), price: Number(x.rates.price), pct: Number(x.rates.pct), revH: x.review_hours ?? 0,
      revRate: Number(x.rates.revRate), ex: x.meta.ex ?? [], min: x.minutes, miss: x.meta.miss ?? 0, body: false, gab: x.clinic_id ?? '', cloud: true });
  }
  return { live, gone };
}
