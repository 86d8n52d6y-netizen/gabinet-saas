// Kalendarz (etap 4e-1): dokumenty 1:1 z obecnej aplikacji + wspólne gabinety.
// Gabinet = wiersz app.clinics. Pola wspólne (nazwa, skrót, kolor, aktywny, model, %, udział w labie, stawki) – kolumny tabeli;
// pola wyłącznie kalendarzowe (zmiany, dni pracy, termin płatności, oczekiwany obrót…) – clinics.extra->'kal'.
// Kalendarz przechowuje kwoty w zł (liczby), tabela – w groszach.
import 'server-only';
import type { PoolClient } from 'pg';

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const DOC = /^(settings|courses|m[0-9]{4}-[0-9]{2})$/;
const MODELS = ['pct_lab', 'pct_share', 'pct', 'hourly', 'daily', 'manual'];
const BASE = ['id', 'name', 'short', 'color', 'active', 'model', 'pct', 'labShare', 'hourly', 'daily', 'minDaily', 'address'];
const n = (v: unknown) => { const x = typeof v === 'string' ? parseFloat(v.replace(',', '.')) : Number(v); return Number.isFinite(x) ? x : null; };
const gr = (v: unknown) => { const x = n(v); return x === null || x < 0 || x > 1e8 ? null : Math.round(x * 100); };
const zl = (g: unknown) => g === null || g === undefined ? 0 : Number(g) / 100;
const txt = (s: unknown, max: number) => String(s ?? '').replace(/[\u0000-\u001f<>]/g, ' ').trim().slice(0, max);

/** Dokumenty Kalendarza dla strony: 'settings' z gabinetami z tabeli (tabela ma pierwszeństwo dla pól wspólnych) + wersje dokumentów. */
export async function loadDocs(c: PoolClient) {
  const rows = (await c.query(`SELECT doc, data, version FROM app.calendar_docs WHERE doc <> 'sumy'`)).rows;
  const docs: Record<string, Record<string, unknown>> = Object.fromEntries(rows.map(r => [r.doc, r.data]));
  const ver: Record<string, number> = Object.fromEntries(rows.map(r => [r.doc, r.version]));
  const cl = (await c.query(`SELECT id, name, short, color, active, model, pct::float8, lab_share::float8, hourly_gr, daily_gr, min_daily_gr, extra
                               FROM app.clinics WHERE deleted_at IS NULL ORDER BY sort, created_at`)).rows;
  if (cl.length) {
    const s = (docs.settings ??= {}) as { clinics?: Record<string, unknown>[] };
    const old = new Map((Array.isArray(s.clinics) ? s.clinics : []).map(k => [String(k.id), k]));
    s.clinics = cl.map(k => ({
      ...(k.extra?.kal ?? {}), ...(old.get(k.id) ?? {}),
      id: k.id, name: k.name, short: k.short ?? '', color: Math.min(8, k.color), active: k.active, model: k.model,
      pct: k.pct ?? 0, labShare: k.lab_share ?? 0, hourly: zl(k.hourly_gr), daily: zl(k.daily_gr), minDaily: zl(k.min_daily_gr),
      address: k.extra?.address ?? '',
    }));
  }
  return { docs, ver };
}

type Conflict = Record<string, { data: unknown; version: number }>;
/** Zapis dokumentów z urządzenia z kontrolą wersji (base: wersja, od której urządzenie zaczynało; 0 = nowy dokument).
 *  Dokument zmieniony w międzyczasie na innym urządzeniu nie jest nadpisywany – wraca jako konflikt (urządzenie scala zmiany i wysyła ponownie). */
export async function saveDocs(c: PoolClient, owner: string, put: Record<string, unknown>, del: string[], base?: Record<string, unknown>) {
  const ver: Record<string, number> = {}, conflict: Conflict = {};
  const check = (doc: string) => base && Object.prototype.hasOwnProperty.call(base, doc) ? Math.max(0, Math.floor(Number(base[doc]) || 0)) : null;
  for (const [doc, data] of Object.entries(put)) {
    if (!DOC.test(doc) || !data || typeof data !== 'object' || Array.isArray(data)) throw new Error('Nieprawidłowy dokument: ' + doc);
    const b = check(doc);
    const cur = (await c.query('SELECT version FROM app.calendar_docs WHERE doc = $1 FOR UPDATE', [doc])).rows[0]?.version ?? 0;
    if (b !== null && cur !== b) { conflict[doc] = await current(c, doc); continue; }
    if (doc === 'settings') await syncClinics(c, owner, (data as { clinics?: unknown }).clinics);
    ver[doc] = (await c.query(`INSERT INTO app.calendar_docs(owner_id, doc, data) VALUES ($1, $2, $3::jsonb)
                   ON CONFLICT (owner_id, doc) DO UPDATE SET data = EXCLUDED.data RETURNING version`, [owner, doc, JSON.stringify(data)])).rows[0].version;
  }
  for (const doc of del) {
    if (!/^(courses|m[0-9]{4}-[0-9]{2})$/.test(doc)) continue;                   // ustawień (z gabinetami) nie usuwamy – Kalendarz zapisuje nowe
    const b = check(doc);
    const cur = (await c.query('SELECT version FROM app.calendar_docs WHERE doc = $1 FOR UPDATE', [doc])).rows[0]?.version ?? 0;
    if (b !== null && cur && cur !== b) { conflict[doc] = await current(c, doc); continue; }
    await c.query('DELETE FROM app.calendar_docs WHERE doc = $1', [doc]); ver[doc] = 0;
  }
  return { ver, conflict };
}
async function current(c: PoolClient, doc: string) {
  if (doc === 'settings') { const { docs, ver } = await loadDocs(c); return { data: docs.settings ?? null, version: ver.settings ?? 0 }; }
  const r = (await c.query('SELECT data, version FROM app.calendar_docs WHERE doc = $1', [doc])).rows[0];
  return { data: r?.data ?? null, version: r?.version ?? 0 };
}
/** Dokumenty zmienione względem wersji znanych urządzeniu (odświeżenie po powrocie do karty). */
export async function changedDocs(c: PoolClient, known: Record<string, unknown>) {
  const rows = (await c.query(`SELECT doc, version FROM app.calendar_docs WHERE doc <> 'sumy'`)).rows as { doc: string; version: number }[];
  const out: Conflict = {};
  const changed = rows.filter(r => Number(known[r.doc] ?? 0) !== r.version);
  for (const r of changed) out[r.doc] = await current(c, r.doc);
  for (const k of Object.keys(known)) if (Number(known[k]) > 0 && !rows.some(r => r.doc === k)) out[k] = { data: null, version: 0 };
  return out;
}

/** Gabinet w formacie Kalendarza → wiersz app.clinics (UPDATE albo INSERT z identyfikatorem nadanym na urządzeniu). */
async function upsertClinic(c: PoolClient, owner: string, k: Record<string, unknown>, sort: number) {
  const model = MODELS.includes(String(k.model)) ? String(k.model) : 'pct_lab';
  const pct = n(k.pct), ls = n(k.labShare), color = Math.min(8, Math.max(1, Math.round(n(k.color) ?? 1)));
  const kal = Object.fromEntries(Object.entries(k).filter(([key]) => !BASE.includes(key)));
  const vals = [txt(k.name, 80) || 'Gabinet', txt(k.short, 6).toUpperCase().replace(/[^A-Z0-9ĄĆĘŁŃÓŚŹŻ]/g, '') || null, color, k.active !== false, model,
    model.startsWith('pct') && pct !== null && pct >= 0 && pct <= 100 ? pct : null, model === 'pct_share' && ls !== null && ls >= 0 && ls <= 100 ? ls : null,
    gr(k.hourly), gr(k.daily), gr(k.minDaily) || null, JSON.stringify({ address: txt(k.address, 200), kal }), sort];
  const u = await c.query(`UPDATE app.clinics SET name=$2, short=$3, color=$4, active=$5, model=$6, pct=$7, lab_share=$8, hourly_gr=$9, daily_gr=$10,
      min_daily_gr=$11, extra = extra || $12::jsonb, sort=$13, deleted_at=NULL WHERE id=$1`, [k.id, ...vals]);
  if (!u.rowCount) await c.query(`INSERT INTO app.clinics(id, owner_id, name, short, color, active, model, pct, lab_share, hourly_gr, daily_gr, min_daily_gr, extra, sort)
      VALUES ($1,$14,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12::jsonb,$13)`, [k.id, ...vals, owner]);   // cudzy UUID → błąd klucza (RLS ukrywa wiersz) – odrzucone
}

async function syncClinics(c: PoolClient, owner: string, list: unknown) {
  if (!Array.isArray(list) || !list.length) return;
  // usuwamy tylko gabinety, które Kalendarz już znał (były w poprzednio zapisanych ustawieniach) – gabinet dodany w międzyczasie
  // w „Gabinety” na innej karcie/urządzeniu nie zniknie przez zapis starszej wersji ustawień
  const prev = (await c.query(`SELECT coalesce(jsonb_path_query_array(data, '$.clinics[*].id'), '[]'::jsonb) AS ids FROM app.calendar_docs WHERE doc = 'settings'`)).rows[0];
  const known: string[] = (prev?.ids ?? []).filter((x: unknown) => typeof x === 'string' && UUID.test(x));
  const seen: string[] = [];
  let sort = 0;
  for (const raw of list.slice(0, 30)) {
    if (!raw || typeof raw !== 'object') continue;
    const k = raw as Record<string, unknown>;
    if (typeof k.id !== 'string' || !UUID.test(k.id)) continue;           // identyfikatory gabinetów z Kalendarza: UUID (poprawka K5)
    await upsertClinic(c, owner, k, sort++);
    seen.push(k.id);
  }
  // gabinet usunięty w Kalendarzu (możliwe tylko bez dyżurów w historii): ukrywamy; z wizytami w opisach – tylko wyłączamy
  const gone = (await c.query(`SELECT id, EXISTS (SELECT 1 FROM app.saved_descriptions s WHERE s.clinic_id = k.id) AS used
                                 FROM app.clinics k WHERE deleted_at IS NULL AND NOT (id = ANY($1::uuid[])) AND id = ANY($2::uuid[])`, [seen, known])).rows;
  for (const g of gone) await c.query(g.used ? 'UPDATE app.clinics SET active = false WHERE id = $1' : 'UPDATE app.clinics SET deleted_at = now() WHERE id = $1', [g.id]);
}

/** Import kopii ze starej aplikacji: dodanie gabinetów (format Kalendarza, nowe UUID). Istniejących gabinetów nie zmienia ani nie usuwa. */
export async function addClinics(c: PoolClient, owner: string, list: unknown) {
  if (!Array.isArray(list)) return 0;
  const n0 = Number((await c.query('SELECT count(*) AS n FROM app.clinics WHERE deleted_at IS NULL')).rows[0].n);
  if (n0 + list.length > 30) throw new Error('Nieprawidłowy import: za dużo gabinetów (limit 30).');
  let sort = n0, added = 0;
  for (const raw of list) {
    if (!raw || typeof raw !== 'object' || typeof (raw as { id?: unknown }).id !== 'string' || !UUID.test((raw as { id: string }).id)) throw new Error('Nieprawidłowy gabinet w imporcie.');
    if ((await c.query('SELECT 1 FROM app.clinics WHERE id = $1', [(raw as { id: string }).id])).rowCount) continue;
    await upsertClinic(c, owner, raw as Record<string, unknown>, sort++); added++;
  }
  return added;
}

/** Przychód z odbytych dyżurów (wylicza Kalendarz): data → gabinet → {inc} w groszach. */
export async function saveKalSums(c: PoolClient, owner: string, map: unknown) {
  const out: Record<string, Record<string, { inc: number }>> = {};
  if (map && typeof map === 'object') for (const [d, g] of Object.entries(map as Record<string, unknown>).slice(0, 5000)) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d) || !g || typeof g !== 'object') continue;
    for (const [cid, v] of Object.entries(g as Record<string, { inc?: unknown }>)) {
      const inc = Math.round(Number(v?.inc));
      if (UUID.test(cid) && Number.isFinite(inc) && inc > 0 && inc < 1e11) (out[d] ??= {})[cid] = { inc };
    }
  }
  await c.query(`INSERT INTO app.calendar_docs(owner_id, doc, data) VALUES ($1, 'sumy', $2::jsonb) ON CONFLICT (owner_id, doc) DO UPDATE SET data = EXCLUDED.data`,
    [owner, JSON.stringify(out)]);
}

/** Sumy dnia z opisów dla podpowiedzi „Wpisz jako obrót” (format jak G.sums w obecnej aplikacji). */
export async function descSums(c: PoolClient, from: string) {
  const r = (await c.query(
    `SELECT s.visit_date::text AS d, coalesce(s.clinic_id::text, '') AS g, s.module,
            count(DISTINCT s.id) FILTER (WHERE s.module='private' OR s.meta->>'src'='gen' OR (s.rates->>'pts')::numeric > 0 OR s.minutes > 0)::int AS n,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_points'),0)::bigint AS pc, coalesce(sum(e.doctor_pay_gr) FILTER (WHERE e.source='nfz_points'),0)::bigint AS sh,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_review'),0)::bigint AS rv, coalesce(sum(e.value_gr) FILTER (WHERE e.source='nfz_extra'),0)::bigint AS ex,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS val, coalesce(sum(e.cost_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS cost,
            coalesce(sum(e.doctor_pay_gr) FILTER (WHERE e.source='private_procedure'),0)::bigint AS pay
       FROM app.saved_descriptions s LEFT JOIN app.earnings_entries e ON e.description_id = s.id AND e.deleted_at IS NULL
      WHERE s.deleted_at IS NULL AND s.visit_date >= $1 GROUP BY 1, 2, 3`, [from])).rows;
  const nfz: Record<string, Record<string, object>> = {}, pryw: Record<string, Record<string, object>> = {};
  for (const x of r) {
    if (x.module === 'nfz') (nfz[x.d] ??= {})[x.g] = { n: x.n, pc: Number(x.pc), sh: Number(x.sh), rv: Number(x.rv), ex: Number(x.ex) };
    else (pryw[x.d] ??= {})[x.g] = { n: x.n, val: Number(x.val), pay: Number(x.pay), cost: Number(x.cost) };
  }
  return { nfz, pryw };
}

/** Dyżury na dziś (kafelek na stronie konta): „SKRÓT 8:00–15:00”, bez odwołanych. */
export async function todayShifts(c: PoolClient, today: string) {
  const m = (await c.query(`SELECT data FROM app.calendar_docs WHERE doc = $1`, ['m' + today.slice(0, 7)])).rows[0]?.data as { shifts?: Record<string, unknown>[] } | undefined;
  const list = (Array.isArray(m?.shifts) ? m!.shifts : []).filter(x => x && x.date === today && x.status !== 'cancelled');
  if (!list.length) return [];
  const cl = new Map((await c.query(`SELECT id::text, coalesce(nullif(short,''), name) AS s FROM app.clinics`)).rows.map(r => [r.id, r.s]));
  return list.sort((a, b) => String(a.start).localeCompare(String(b.start)))
    .map(x => `${cl.get(String(x.clinicId)) ?? 'Gabinet'} ${String(x.start ?? '').replace(/^0/, '')}–${String(x.end ?? '').replace(/^0/, '')}`);
}

/** Dyżury (bez odwołanych) w oknie dat – do automatycznego wyboru gabinetu w Opisach („gabinet z dyżuru”): data → [[gabinet, od, do]]. */
export async function shiftsByDay(c: PoolClient, from: string, to: string) {
  const rows = (await c.query(`SELECT data FROM app.calendar_docs WHERE doc ~ '^m[0-9]{4}-[0-9]{2}$' AND doc BETWEEN $1 AND $2`, ['m' + from.slice(0, 7), 'm' + to.slice(0, 7)])).rows;
  const out: Record<string, [string, string, string][]> = {};
  for (const r of rows) for (const x of (Array.isArray(r.data?.shifts) ? r.data.shifts : []) as Record<string, unknown>[]) {
    const d = String(x?.date ?? '');
    if (x?.status === 'cancelled' || d < from || d > to || typeof x.clinicId !== 'string') continue;
    (out[d] ??= []).push([x.clinicId, String(x.start ?? ''), String(x.end ?? '')]);
  }
  return out;
}

/* ---------- Zarobek lekarza i czas pracy z Kalendarza (Zarobki → „Wszystkie gabinety”, decyzja Patryka 21.11.2026: opcja A) ----------
   Port 1:1 funkcji Kalendarza: num, r2, hoursOf, shiftIncome (generator/kalendarz.html) – te same zasady gabinetu
   (% po odjęciu kosztów własnych, % od obrotu z udziałem w labie, % od obrotu, stawka godzinowa, dzienna, kwota ręczna, minimum dzienne).
   Liczone tylko dyżury „odbyte” (status done), jak w Kalendarzu i w „Wpisz jako obrót”. Liczone na serwerze z aktualnych danych,
   więc nie zależą od tego, czy Kalendarz był ostatnio otwarty. */
const kNum = (v: unknown): number | null => {
  if (v === null || v === undefined || v === '') return null;
  if (typeof v === 'number') return Number.isFinite(v) ? v : null;
  const x = parseFloat(String(v).replace(/\s| /g, '').replace(',', '.'));
  return Number.isFinite(x) ? x : null;
};
const kR2 = (x: number) => Math.round((x + (x >= 0 ? 1 : -1) * 1e-9) * 100) / 100;
const kMin = (t: unknown) => { const s = String(t ?? ''); if (!s.includes(':')) return null; const [h, m] = s.split(':').map(Number); return h * 60 + m; };
export function kalHours(sh: Record<string, unknown>) {
  const a = kMin(sh.start), b = kMin(sh.end);
  if (a === null || b === null || !Number.isFinite(a) || !Number.isFinite(b)) return 0;
  let d = b - a; if (d < 0) d += 1440;
  return d / 60;
}
export function kalIncome(sh: Record<string, unknown>, c: Record<string, unknown> | undefined) {
  if (!c || sh.status === 'cancelled') return 0;
  const ov = kNum(sh.override);
  if (ov !== null) return kR2(ov);
  const t = kNum(sh.turnover) ?? 0, lab = kNum(sh.lab) ?? 0, pct = (kNum(c.pct) ?? 0) / 100;
  let inc = 0;
  switch (c.model) {
    case 'pct_lab': inc = Math.max(0, t - lab) * pct; break;
    case 'pct_share': inc = t * pct - lab * ((kNum(c.labShare) ?? 0) / 100); break;
    case 'pct': inc = t * pct; break;
    case 'hourly': inc = kalHours(sh) * (kNum(c.hourly) ?? 0); break;
    case 'daily': inc = kNum(c.daily) ?? 0; break;
    default: inc = kNum(sh.amount) ?? 0;
  }
  const min = kNum(c.minDaily) ?? 0;
  if (min > 0) inc = Math.max(inc, min);
  return kR2(inc);
}

/** Odbyte dyżury w okresie: gabinet → { zarobek lekarza (grosze), godziny pracy, liczba dyżurów }. */
export async function kalPraca(c: PoolClient, from: string, to: string) {
  const { docs } = await loadDocs(c);
  const clinics = new Map(((docs.settings as { clinics?: Record<string, unknown>[] } | undefined)?.clinics ?? []).map(k => [String(k.id), k]));
  const out = new Map<string, { gr: number; h: number; n: number }>();
  for (const [doc, data] of Object.entries(docs)) {
    if (!/^m[0-9]{4}-[0-9]{2}$/.test(doc) || doc.slice(1) < from.slice(0, 7) || doc.slice(1) > to.slice(0, 7)) continue;
    for (const sh of (Array.isArray((data as { shifts?: unknown }).shifts) ? (data as { shifts: Record<string, unknown>[] }).shifts : [])) {
      const d = String(sh?.date ?? '');
      if (!sh || sh.status !== 'done' || d < from || d > to || typeof sh.clinicId !== 'string') continue;
      const k = clinics.get(sh.clinicId);
      const o = out.get(sh.clinicId) ?? { gr: 0, h: 0, n: 0 };
      o.gr += Math.round(kalIncome(sh, k) * 100); o.h += kalHours(sh); o.n++;
      out.set(sh.clinicId, o);
    }
  }
  return out;
}
