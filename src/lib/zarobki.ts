// Zarobki i statystyki ze wszystkich gabinetów (etap 4d). Jedyne źródło kwot: app.earnings_entries (każda kwota raz),
// wizyty: app.saved_descriptions. Odczyt rolą użytkownika (RLS – wyłącznie własne dane). Definicje jak w obecnej aplikacji
// (index.html, okno „Zarobki – wszystkie gabinety”):
//   zarobek NFZ = wartość punktów (lub udział lekarza – ustawienie „Zarobek z punktów”) + przeglądy + kwoty dodatkowe,
//   zarobek prywatny = wynagrodzenie lekarza (z cennika), wizyta NFZ = wpis z generatora albo z punktami / czasem wizyty.
import 'server-only';
import type { PoolClient } from 'pg';
import { kalPraca } from './kal';

export type Range = { from: string; to: string; label: string; key: string };
const TZ = 'Europe/Warsaw';
const pad = (n: number) => String(n).padStart(2, '0');
const isoD = (d: Date) => `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())}`;
/** Dzisiejsza data w Polsce (YYYY-MM-DD) niezależnie od strefy serwera. */
export function todayPL(now = new Date()): string {
  return new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit' }).format(now);
}
const DATE = /^\d{4}-\d{2}-\d{2}$/;
export const RANGES = { today: 'Dziś', week: 'Ten tydzień', month: 'Ten miesiąc', prev: 'Poprzedni miesiąc', year: 'Ten rok' } as const;

/** Okres jak rangeOf w obecnej aplikacji (tydzień od poniedziałku); 'own' – własny zakres od–do (maks. 3 lata). */
export function rangeOf(key: string, od?: string, doo?: string, now = new Date()): Range {
  const t = todayPL(now), [y, m, d] = t.split('-').map(Number);
  const D = (yy: number, mm: number, dd: number) => isoD(new Date(Date.UTC(yy, mm - 1, dd)));
  if (key === 'own' && od && doo && DATE.test(od) && DATE.test(doo) && od <= doo && !isNaN(Date.parse(od)) && !isNaN(Date.parse(doo))
      && (Date.parse(doo) - Date.parse(od)) <= 3 * 366 * 864e5) return { from: od, to: doo, label: 'Własny zakres', key: 'own' };
  if (key === 'today') return { from: t, to: t, label: RANGES.today, key };
  if (key === 'week') { const dw = (new Date(Date.UTC(y, m - 1, d)).getUTCDay() + 6) % 7; return { from: D(y, m, d - dw), to: D(y, m, d - dw + 6), label: RANGES.week, key }; }
  if (key === 'prev') return { from: D(y, m - 1, 1), to: D(y, m, 0), label: RANGES.prev, key };
  if (key === 'year') return { from: `${y}-01-01`, to: `${y}-12-31`, label: RANGES.year, key };
  return { from: D(y, m, 1), to: D(y, m + 1, 0), label: RANGES.month, key: 'month' };
}

/** Wiersz „Wszystkie gabinety”. vis – odbyte wizyty (wszystkie rodzaje); dr – zarobek lekarza wg zasad gabinetu z odbytych dyżurów (Kalendarz, grosze);
 *  h – godziny pracy z odbytych dyżurów; nv/pv/e1/e2/sum – kwoty z opisów (kafelek „Razem z wizyt”, wykresy, średnie). */
export type ClinicRow = { id: string | null; name: string; color: number | null; nv: number; e1: number; pv: number; e2: number; sum: number; vis: number; dr: number; h: number };
export type Report = {
  basis: 'full' | 'share'; rows: ClinicRow[]; total: Omit<ClinicRow, 'id' | 'name' | 'color'>;
  nfz: { pc: number; sh: number; rv: number; ex: number; pts: number; minutes: number };
  pryw: { val: number; cost: number; pay: number };
  series: { key: string; nfz: number; pryw: number }[]; seriesBy: 'day' | 'month';
  topNfz: { code: string; n: number }[]; topPryw: { name: string; n: number; pay: number }[];
  kind: string; categories: string[];
  weekdays: { dow: number; days: number; nfz: number; pryw: number }[];
  avg: { days: number; perDay: number; perVisit: number; perMonth: number | null };
  prev: Range & { sum: number; nv: number; pv: number };
};

/** Poprzedni okres do porównania: poprzedni dzień / tydzień / miesiąc / rok; własny zakres – tyle samo dni bezpośrednio wcześniej. */
export function prevRange(r: Range): Range {
  const d = (s: string) => new Date(s + 'T00:00:00Z'), f = (x: Date) => isoD(x);
  const [y, m] = r.from.split('-').map(Number);
  if (r.key === 'month' || r.key === 'prev') return { from: f(new Date(Date.UTC(y, m - 2, 1))), to: f(new Date(Date.UTC(y, m - 1, 0))), label: 'miesiąc wcześniej', key: 'own' };
  if (r.key === 'year') return { from: `${y - 1}-01-01`, to: `${y - 1}-12-31`, label: 'rok wcześniej', key: 'own' };
  const n = Math.round((d(r.to).getTime() - d(r.from).getTime()) / 864e5) + 1;
  const to = new Date(d(r.from).getTime() - 864e5), from = new Date(to.getTime() - (n - 1) * 864e5);
  return { from: f(from), to: f(to), label: r.key === 'today' ? 'dzień wcześniej' : r.key === 'week' ? 'tydzień wcześniej' : `${n} dni wcześniej`, key: 'own' };
}

/** Filtr rodzaju: '' wszystko, 'nfz', 'pryw', 'kat:<kategoria procedur prywatnych>'. */
function kindSql(kind: string, next: number): { ef: string; vf: string; arg: unknown[]; onlyNfz: boolean; onlyPryw: boolean } {
  if (kind === 'nfz') return { ef: ` AND e.source IN ('nfz_points','nfz_review','nfz_extra')`, vf: ` AND s.module = 'nfz'`, arg: [], onlyNfz: true, onlyPryw: false };
  if (kind === 'pryw') return { ef: ` AND e.source = 'private_procedure'`, vf: ` AND s.module = 'private'`, arg: [], onlyNfz: false, onlyPryw: true };
  if (kind.startsWith('kat:') && kind.length > 4) return { ef: ` AND e.source = 'private_procedure' AND e.category_name = $${next}`,
    vf: ` AND s.module = 'private' AND EXISTS (SELECT 1 FROM app.earnings_entries x WHERE x.description_id = s.id AND x.deleted_at IS NULL AND x.category_name = $${next})`, arg: [kind.slice(4)], onlyNfz: false, onlyPryw: true };
  return { ef: '', vf: '', arg: [], onlyNfz: false, onlyPryw: false };
}

export async function report(c: PoolClient, r: Range, clinic: string | null, kind = ''): Promise<Report> {
  const basis = (await c.query(`SELECT settings->'nfz'->>'basis' AS b FROM app.user_settings`)).rows[0]?.b === 'share' ? 'share' : 'full';
  const categories = (await c.query(`SELECT DISTINCT category_name AS k FROM app.earnings_entries WHERE source = 'private_procedure' AND deleted_at IS NULL AND coalesce(category_name,'') <> '' ORDER BY 1`)).rows.map(x => x.k as string);
  if (kind.startsWith('kat:') && !categories.includes(kind.slice(4))) kind = '';
  if (!['', 'nfz', 'pryw'].includes(kind) && !kind.startsWith('kat:')) kind = '';
  const K = kindSql(kind, clinic ? 4 : 3);
  const cf = (clinic ? ' AND s.clinic_id = $3' : '') + K.vf, ef = K.ef;
  const args: unknown[] = [r.from, r.to, ...(clinic ? [clinic] : []), ...K.arg];
  const nfzE = basis === 'share'
    ? `sum(CASE e.source WHEN 'nfz_points' THEN e.doctor_pay_gr WHEN 'nfz_review' THEN e.value_gr WHEN 'nfz_extra' THEN e.value_gr ELSE 0 END)`
    : `sum(CASE WHEN e.source IN ('nfz_points','nfz_review','nfz_extra') THEN e.value_gr ELSE 0 END)`;
  const per = (await c.query(
    `WITH v AS (SELECT s.clinic_id,
                  count(*) FILTER (WHERE s.module = 'nfz' AND (s.meta->>'src' = 'gen' OR (s.rates->>'pts')::numeric > 0 OR s.minutes > 0)) AS nv,
                  count(*) FILTER (WHERE s.module = 'private') AS pv
                FROM app.saved_descriptions s WHERE s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf} GROUP BY s.clinic_id),
          k AS (SELECT s.clinic_id, ${nfzE} AS e1, sum(CASE WHEN e.source = 'private_procedure' THEN e.doctor_pay_gr ELSE 0 END) AS e2
                FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
                WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef} GROUP BY s.clinic_id)
     SELECT coalesce(v.clinic_id, k.clinic_id) AS id, coalesce(v.nv,0)::int AS nv, coalesce(v.pv,0)::int AS pv, coalesce(k.e1,0)::bigint AS e1, coalesce(k.e2,0)::bigint AS e2
       FROM v FULL JOIN k ON coalesce(v.clinic_id, '00000000-0000-0000-0000-000000000000'::uuid) = coalesce(k.clinic_id, '00000000-0000-0000-0000-000000000000'::uuid)`, args)).rows;
  const clinics = (await c.query(`SELECT id, name, color, active FROM app.clinics WHERE deleted_at IS NULL ORDER BY sort, created_at`)).rows;
  const byId = new Map(per.map(x => [x.id ?? '', x]));
  // Zarobek lekarza i czas pracy: odbyte dyżury w Kalendarzu wg zasad rozliczenia gabinetu (decyzja Patryka 21.11.2026, opcja A).
  // Kalendarz nie dzieli dyżuru na NFZ i prywatne – przy filtrze rodzaju (NFZ / prywatne / kategoria) tych wartości nie pokazujemy.
  const praca = kind ? new Map<string, { gr: number; h: number; n: number }>() : await kalPraca(c, r.from, r.to);
  const kal = new Map([...praca].filter(([id]) => !clinic || id === clinic));
  const known = new Set(clinics.map(k => k.id as string));
  const ids = [...clinics.filter(k => (!clinic || k.id === clinic) && (k.active || byId.has(k.id) || kal.has(k.id))).map(k => k.id as string),
    ...[...new Set([...byId.keys(), ...kal.keys()])].filter(id => id && !known.has(id)),   // gabinet usunięty, a wizyty/dyżury zostały
    ...(byId.has('') && !clinic ? [''] : [])];
  const rows: ClinicRow[] = ids.map(id => {
    const x = byId.get(id), k = clinics.find(z => z.id === id);
    const e1 = Number(x?.e1 ?? 0), e2 = Number(x?.e2 ?? 0);
    const nv = x?.nv ?? 0, pv = x?.pv ?? 0, w = kal.get(id);
    return { id: id || null, name: k ? k.name : id ? 'Gabinet usunięty' : 'Bez gabinetu', color: k?.color ?? null, nv, e1, pv, e2, sum: e1 + e2, vis: nv + pv, dr: w?.gr ?? 0, h: w?.h ?? 0 };
  });
  const total = rows.reduce((s, x) => ({ nv: s.nv + x.nv, e1: s.e1 + x.e1, pv: s.pv + x.pv, e2: s.e2 + x.e2, sum: s.sum + x.sum, vis: s.vis + x.vis, dr: s.dr + x.dr, h: s.h + x.h }),
    { nv: 0, e1: 0, pv: 0, e2: 0, sum: 0, vis: 0, dr: 0, h: 0 });

  const det = (await c.query(
    `SELECT coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_points'),0)::bigint AS pc, coalesce(sum(e.doctor_pay_gr) FILTER (WHERE e.source='nfz_points'),0)::bigint AS sh,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_review'),0)::bigint AS rv, coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_extra'),0)::bigint AS ex,
            coalesce(sum(e.points) FILTER (WHERE e.source='nfz_points'),0)::float8 AS pts,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS val, coalesce(sum(e.cost_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS cost,
            coalesce(sum(e.doctor_pay_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS pay
       FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef}`, args)).rows[0];
  const minutes = Number((await c.query(`SELECT coalesce(sum(minutes),0)::int AS m FROM app.saved_descriptions s
      WHERE s.module='nfz' AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}`, args)).rows[0].m);

  const days = (Date.parse(r.to) - Date.parse(r.from)) / 864e5 + 1;
  const seriesBy: 'day' | 'month' = days <= 62 ? 'day' : 'month';
  const bucket = seriesBy === 'day' ? `s.visit_date::text` : `to_char(s.visit_date, 'YYYY-MM')`;
  const ser = (await c.query(
    `SELECT ${bucket} AS k, ${nfzE}::bigint AS nfz, sum(CASE WHEN e.source='private_procedure' THEN e.doctor_pay_gr ELSE 0 END)::bigint AS pryw
       FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef} GROUP BY 1 ORDER BY 1`, args)).rows;
  const map = new Map(ser.map(x => [x.k, { nfz: Number(x.nfz), pryw: Number(x.pryw) }]));
  const series: Report['series'] = [];
  if (seriesBy === 'day') for (let t = Date.parse(r.from); t <= Date.parse(r.to); t += 864e5) { const k = isoD(new Date(t)); series.push({ key: k, ...(map.get(k) ?? { nfz: 0, pryw: 0 }) }); }
  else { const [y0, m0] = r.from.split('-').map(Number), [y1, m1] = r.to.split('-').map(Number);
    for (let y = y0, m = m0; y < y1 || (y === y1 && m <= m1); m === 12 ? (y++, m = 1) : m++) { const k = `${y}-${pad(m)}`; series.push({ key: k, ...(map.get(k) ?? { nfz: 0, pryw: 0 }) }); } }

  const topNfz = (await c.query(`SELECT code, count(*)::int AS n FROM app.saved_descriptions s, unnest(s.codes) AS code
      WHERE s.module='nfz' AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf} GROUP BY code ORDER BY n DESC, code LIMIT 10`, args)).rows;
  const topPryw = (await c.query(`SELECT e.label AS name, sum(e.qty)::int AS n, sum(e.doctor_pay_gr)::bigint AS pay FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.source='private_procedure' AND e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf} GROUP BY e.label ORDER BY n DESC, e.label LIMIT 10`, args)).rows
    .map(x => ({ name: x.name, n: x.n, pay: Number(x.pay) }));
  // dni tygodnia (pon.–niedz.): suma zarobków i liczba dni pracy (dni z zapisanymi kwotami)
  const wd = (await c.query(
    `SELECT extract(isodow FROM s.visit_date)::int AS dow, count(DISTINCT s.visit_date)::int AS days, ${nfzE}::bigint AS nfz,
            sum(CASE WHEN e.source='private_procedure' THEN e.doctor_pay_gr ELSE 0 END)::bigint AS pryw
       FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef} GROUP BY 1`, args)).rows;
  const weekdays = [1, 2, 3, 4, 5, 6, 7].map(dow => { const x = wd.find(w => w.dow === dow); return { dow, days: x?.days ?? 0, nfz: Number(x?.nfz ?? 0), pryw: Number(x?.pryw ?? 0) }; });
  const workDays = Number((await c.query(`SELECT count(DISTINCT s.visit_date)::int AS n FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef}`, args)).rows[0].n);
  const curMonth = todayPL().slice(0, 7), months = seriesBy === 'month' ? series.filter(x => x.key <= curMonth).length : 0;
  const visits = total.nv + total.pv;
  const avg = { days: workDays, perDay: workDays ? Math.round(total.sum / workDays) : 0, perVisit: visits ? Math.round(total.sum / visits) : 0,
    perMonth: months >= 2 ? Math.round(total.sum / months) : null };
  // porównanie z poprzednim okresem (te same filtry)
  const pr = prevRange(r), pargs = [pr.from, pr.to, ...args.slice(2)];
  const pt = (await c.query(
    `SELECT coalesce(${nfzE},0)::bigint AS e1, coalesce(sum(CASE WHEN e.source='private_procedure' THEN e.doctor_pay_gr ELSE 0 END),0)::bigint AS e2
       FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}${ef}`, pargs)).rows[0];
  const pv = (await c.query(`SELECT count(*) FILTER (WHERE s.module = 'nfz' AND (s.meta->>'src' = 'gen' OR (s.rates->>'pts')::numeric > 0 OR s.minutes > 0))::int AS nv,
      count(*) FILTER (WHERE s.module = 'private')::int AS pv FROM app.saved_descriptions s WHERE s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}`, pargs)).rows[0];
  const prev = { ...pr, sum: Number(pt.e1) + Number(pt.e2), nv: pv.nv, pv: pv.pv };
  return {
    kind, categories, weekdays, avg, prev,
    basis, rows, total,
    nfz: { pc: Number(det.pc), sh: Number(det.sh), rv: Number(det.rv), ex: Number(det.ex), pts: Math.round(Number(det.pts) * 100) / 100, minutes },
    pryw: { val: Number(det.val), cost: Number(det.cost), pay: Number(det.pay) }, series, seriesBy, topNfz, topPryw,
  };
}

/** Wiersze do pliku CSV (jedna kwota = jeden wiersz). Bez danych pacjentów – są tylko pozycje i kwoty. */
export async function csvRows(c: PoolClient, r: Range, clinic: string | null, kind = '') {
  if (!['', 'nfz', 'pryw'].includes(kind) && !kind.startsWith('kat:')) kind = '';
  const K = kindSql(kind, clinic ? 4 : 3);
  const cf = (clinic ? ' AND s.clinic_id = $3' : '') + K.vf + K.ef;
  return (await c.query(
    `SELECT s.visit_date::text AS data, coalesce(k.name,'Bez gabinetu') AS gabinet, s.module, s.seq_no, e.source, e.label, e.category_name, e.qty,
            e.points::float8 AS points, e.value_gr, e.cost_gr, e.doctor_pay_gr, array_to_string(s.codes, ' ') AS codes
       FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id = e.description_id LEFT JOIN app.clinics k ON k.id = s.clinic_id
      WHERE e.deleted_at IS NULL AND s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2${cf}
      ORDER BY s.visit_date, s.module, s.seq_no, e.line_no`, [r.from, r.to, ...(clinic ? [clinic] : []), ...K.arg])).rows;
}
