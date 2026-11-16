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

/** Dokumenty Kalendarza dla strony: 'settings' z gabinetami z tabeli (tabela ma pierwszeństwo dla pól wspólnych). */
export async function loadDocs(c: PoolClient) {
  const rows = (await c.query(`SELECT doc, data FROM app.calendar_docs WHERE doc <> 'sumy'`)).rows;
  const docs: Record<string, Record<string, unknown>> = Object.fromEntries(rows.map(r => [r.doc, r.data]));
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
  return docs;
}

/** Zapis dokumentów z urządzenia. Ustawienia: gabinety → tabela clinics (nowe z UUID nadanym w Kalendarzu, zmienione, usunięte). */
export async function saveDocs(c: PoolClient, owner: string, put: Record<string, unknown>, del: string[]) {
  for (const [doc, data] of Object.entries(put)) {
    if (!DOC.test(doc) || !data || typeof data !== 'object' || Array.isArray(data)) throw new Error('Nieprawidłowy dokument: ' + doc);
    if (doc === 'settings') await syncClinics(c, owner, (data as { clinics?: unknown }).clinics);
    await c.query(`INSERT INTO app.calendar_docs(owner_id, doc, data) VALUES ($1, $2, $3::jsonb)
                   ON CONFLICT (owner_id, doc) DO UPDATE SET data = EXCLUDED.data`, [owner, doc, JSON.stringify(data)]);
  }
  for (const doc of del) if (/^(courses|m[0-9]{4}-[0-9]{2})$/.test(doc))   // ustawień (z gabinetami) nie usuwamy – Kalendarz zapisuje nowe
      await c.query('DELETE FROM app.calendar_docs WHERE doc = $1', [doc]);
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
    const model = MODELS.includes(String(k.model)) ? String(k.model) : 'pct_lab';
    const pct = n(k.pct), ls = n(k.labShare), color = Math.min(8, Math.max(1, Math.round(n(k.color) ?? 1)));
    const kal = Object.fromEntries(Object.entries(k).filter(([key]) => !BASE.includes(key)));
    const vals = [txt(k.name, 80) || 'Gabinet', txt(k.short, 6).toUpperCase().replace(/[^A-Z0-9ĄĆĘŁŃÓŚŹŻ]/g, '') || null, color, k.active !== false, model,
      model.startsWith('pct') && pct !== null && pct >= 0 && pct <= 100 ? pct : null, model === 'pct_share' && ls !== null && ls >= 0 && ls <= 100 ? ls : null,
      gr(k.hourly), gr(k.daily), gr(k.minDaily) || null, JSON.stringify({ address: txt(k.address, 200), kal }), sort++];
    const u = await c.query(`UPDATE app.clinics SET name=$2, short=$3, color=$4, active=$5, model=$6, pct=$7, lab_share=$8, hourly_gr=$9, daily_gr=$10,
        min_daily_gr=$11, extra = extra || $12::jsonb, sort=$13, deleted_at=NULL WHERE id=$1`, [k.id, ...vals]);
    if (!u.rowCount) await c.query(`INSERT INTO app.clinics(id, owner_id, name, short, color, active, model, pct, lab_share, hourly_gr, daily_gr, min_daily_gr, extra, sort)
        VALUES ($1,$14,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12::jsonb,$13)`, [k.id, ...vals, owner]);   // cudzy UUID → błąd klucza (RLS ukrywa wiersz) – odrzucone
    seen.push(k.id);
  }
  // gabinet usunięty w Kalendarzu (możliwe tylko bez dyżurów w historii): ukrywamy; z wizytami w opisach – tylko wyłączamy
  const gone = (await c.query(`SELECT id, EXISTS (SELECT 1 FROM app.saved_descriptions s WHERE s.clinic_id = k.id) AS used
                                 FROM app.clinics k WHERE deleted_at IS NULL AND NOT (id = ANY($1::uuid[])) AND id = ANY($2::uuid[])`, [seen, known])).rows;
  for (const g of gone) await c.query(g.used ? 'UPDATE app.clinics SET active = false WHERE id = $1' : 'UPDATE app.clinics SET deleted_at = now() WHERE id = $1', [g.id]);
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
