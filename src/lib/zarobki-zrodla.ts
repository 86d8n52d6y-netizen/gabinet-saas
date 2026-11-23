// Centralny mechanizm zarobków (prompt Patryka 23.11.2026, pkt 5 i 7): JEDNO miejsce, w którym przychód i wynagrodzenie lekarza
// powstają z trzech źródeł – opisy NFZ, opisy prywatne (app.earnings_entries) i obrót ręczny z dyżuru w Kalendarzu.
//
// Zasada (bez heurystyk, bez porównywania kwot): każdy dzień pracy (data × gabinet) ma jasno określone źródła.
//  • Dyżur z obrotem ręcznym ma znacznik „obrotTyp”, który ustawia lekarz w Kalendarzu:
//      'opisy'     – obrót obejmuje opisy z tego dnia (domyślnie – tak działały dotąd wszystkie wpisy): przychód dnia = obrót,
//                    wynagrodzenie = wg zasad gabinetu z dyżuru; opisy tego dnia NIE są doliczane (są rozbiciem tego samego przychodu);
//      'dodatkowy' – obrót to usługi spoza opisów: przychód = opisy + obrót, wynagrodzenie = z opisów + z obrotu wg zasad gabinetu.
//  • Dyżur bez obrotu: gabinet godzinowy / dzienny / „kwota dla Ciebie” – wynagrodzenie z dyżuru (opisy dają tylko przychód);
//    gabinet procentowy – wynagrodzenie z opisów (NFZ: udział wg ustawień NFZ; prywatne: % / kwota z Cennika albo % gabinetu).
//  • Dzień bez dyżuru: przychód i wynagrodzenie z opisów.
//  • Minimum za dzień (Gabinety) dotyczy dnia z dyżurem; kwota z rozliczenia gabinetu (Zarobki → Rozliczenia) zastępuje
//    wynagrodzenie gabinetu za pełny miesiąc w okresie – jak dotąd (Prompt 21.11.2026, pkt 3.3).
// Kwoty w groszach. Opisy NFZ: przychód = punkty × stawka; wynagrodzenie = udział lekarza + przeglądy + kwoty dodatkowe (jak dotąd).
import 'server-only';
import type { PoolClient } from 'pg';
import { kalHours, kalIncome, loadDocs } from './kal';

export type Dzien = {
  date: string; gab: string;
  nfzVal: number; nfzPay: number; prVal: number; prPay: number; prBezPct: number; nv: number; pv: number;
  obrot: number | null; obrotTyp: 'opisy' | 'dodatkowy' | null; dyzur: boolean; model: string;
  przychod: number; pay: number; zrodla: ('NFZ' | 'prywatne' | 'obrót ręczny')[]; h: number;
};
const num = (v: unknown): number | null => { if (v === null || v === undefined || v === '') return null; const n = Number(String(v).replace(',', '.')); return Number.isFinite(n) ? n : null; };
const gr = (zl: number) => Math.round(zl * 100);
const monthEnd = (mk: string) => { const [y, m] = mk.split('-').map(Number); return new Date(Date.UTC(y, m, 0)).toISOString().slice(0, 10); };

export async function zrodla(c: PoolClient, from: string, to: string) {
  const op = (await c.query(
    `SELECT s.visit_date::text AS d, coalesce(s.clinic_id::text, '') AS g,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source IN ('nfz_points','nfz_review','nfz_extra')),0)::bigint AS nv_gr,
            coalesce(sum(CASE e.source WHEN 'nfz_points' THEN e.doctor_pay_gr WHEN 'nfz_review' THEN e.value_gr WHEN 'nfz_extra' THEN e.value_gr ELSE 0 END),0)::bigint AS np_gr,
            coalesce(sum(e.value_gr) FILTER (WHERE e.source = 'private_procedure'),0)::bigint AS pv_gr,
            coalesce(sum(e.doctor_pay_gr) FILTER (WHERE e.source = 'private_procedure'),0)::bigint AS pp_gr,
            count(DISTINCT s.id) FILTER (WHERE s.module = 'nfz' AND (s.meta->>'src' = 'gen' OR (s.rates->>'pts')::numeric > 0 OR s.minutes > 0))::int AS nv,
            count(DISTINCT s.id) FILTER (WHERE s.module = 'private')::int AS pv
       FROM app.saved_descriptions s LEFT JOIN app.earnings_entries e ON e.description_id = s.id AND e.deleted_at IS NULL
      WHERE s.deleted_at IS NULL AND s.visit_date BETWEEN $1 AND $2 GROUP BY 1, 2`, [from, to])).rows;
  // pozycje prywatne bez ustalonego % (zapisane przed poprawką z 23.11.2026 – wynagrodzenie 0 zł); tylko do informacji
  const bez = (await c.query(
    `SELECT s.visit_date::text AS d, coalesce(s.clinic_id::text, '') AS g, count(*)::int AS n FROM app.saved_descriptions s,
            jsonb_array_elements(coalesce(s.meta->'items', '[]'::jsonb)) i
      WHERE s.deleted_at IS NULL AND s.module = 'private' AND s.visit_date BETWEEN $1 AND $2 AND coalesce(i->>'m','') <> 'kw'
        AND (i->>'p') IS NULL AND coalesce((i->>'val')::numeric, 0) > 0 GROUP BY 1, 2`, [from, to]).catch(() => ({ rows: [] }))).rows;
  const { docs } = await loadDocs(c);
  const clinics = new Map(((docs.settings as { clinics?: Record<string, unknown>[] } | undefined)?.clinics ?? []).map(k => [String(k.id), k]));
  const dni = new Map<string, Dzien>();
  const day = (d: string, g: string): Dzien => {
    const k = d + '|' + g; let x = dni.get(k);
    if (!x) { x = { date: d, gab: g, nfzVal: 0, nfzPay: 0, prVal: 0, prPay: 0, prBezPct: 0, nv: 0, pv: 0, obrot: null, obrotTyp: null, dyzur: false, model: String(clinics.get(g)?.model ?? ''), przychod: 0, pay: 0, zrodla: [], h: 0 }; dni.set(k, x); }
    return x;
  };
  for (const o of op) Object.assign(day(o.d, o.g), { nfzVal: Number(o.nv_gr), nfzPay: Number(o.np_gr), prVal: Number(o.pv_gr), prPay: Number(o.pp_gr), nv: o.nv, pv: o.pv });
  for (const b of bez) day(b.d, b.g).prBezPct = b.n;
  // dyżury odbyte w okresie (wynagrodzenie z dyżuru wg zasad gabinetu – kalIncome, jak w Kalendarzu)
  const zDyzuru = new Map<string, { inc: number; raw: Record<string, unknown> }>();
  const statements = new Map<string, number>();                                          // mk|gabinet → kwota z rozliczenia (grosze)
  for (const [doc, data] of Object.entries(docs)) {
    if (!/^m[0-9]{4}-[0-9]{2}$/.test(doc) || doc.slice(1) < from.slice(0, 7) || doc.slice(1) > to.slice(0, 7)) continue;
    const mk = doc.slice(1);
    for (const sh of (Array.isArray((data as { shifts?: unknown }).shifts) ? (data as { shifts: Record<string, unknown>[] }).shifts : [])) {
      const d = String(sh?.date ?? '');
      if (!sh || sh.status !== 'done' || d < from || d > to || typeof sh.clinicId !== 'string') continue;
      const x = day(d, sh.clinicId); x.dyzur = true; x.h += kalHours(sh);
      const t = num(sh.turnover); if (t !== null) { x.obrot = (x.obrot ?? 0) + gr(t); x.obrotTyp = sh.obrotTyp === 'dodatkowy' ? 'dodatkowy' : x.obrotTyp ?? 'opisy'; }
      const z = zDyzuru.get(d + '|' + sh.clinicId) ?? { inc: 0, raw: sh }; z.inc += gr(kalIncome(sh, clinics.get(sh.clinicId))); zDyzuru.set(d + '|' + sh.clinicId, z);
    }
    if (from <= `${mk}-01` && to >= monthEnd(mk)) {
      const inv = ((data as { inv?: unknown }).inv ?? {}) as Record<string, { statement?: unknown } | undefined>;
      for (const id of Object.keys(inv)) { const st = num(inv[id]?.statement); if (st !== null && clinics.has(id)) statements.set(mk + '|' + id, gr(st)); }
    }
  }
  for (const x of dni.values()) {
    const opisyVal = x.nfzVal + x.prVal, opisyPay = x.nfzPay + x.prPay, k = clinics.get(x.gab), z = zDyzuru.get(x.date + '|' + x.gab);
    const procent = /^pct/.test(x.model), minD = gr(num(k?.minDaily) ?? 0);
    if (x.nfzVal) x.zrodla.push('NFZ'); if (x.prVal) x.zrodla.push('prywatne');
    if (x.obrot !== null) x.zrodla.push('obrót ręczny');
    if (x.dyzur && num(z?.raw.override) !== null) { x.przychod = x.obrot !== null && x.obrotTyp === 'opisy' ? x.obrot : opisyVal + (x.obrot ?? 0); x.pay = z!.inc; }      // „kwota dla mnie” – nadpisuje wyliczenie dnia
    else if (x.obrot !== null && x.obrotTyp === 'opisy') { x.przychod = x.obrot; x.pay = z?.inc ?? 0; }
    else if (x.obrot !== null) {                                                          // obrót dodatkowy: opisy + obrót (wynagrodzenie z obrotu bez minimum, minimum na cały dzień)
      const zObrotu = procent ? gr(kalIncome({ ...z!.raw, override: null }, { ...k, minDaily: 0 })) : 0;
      x.przychod = opisyVal + x.obrot; x.pay = Math.max(opisyPay + zObrotu, minD);
    }
    else if (x.dyzur && !procent) { x.przychod = opisyVal; x.pay = z?.inc ?? 0; }        // godzinowy / dzienny / kwota ręczna
    else { x.przychod = opisyVal; x.pay = x.dyzur ? Math.max(opisyPay, minD) : opisyPay; }
  }
  // kwota z rozliczenia gabinetu za pełny miesiąc zastępuje sumę dni tego gabinetu (jak dotąd)
  const perGab = new Map<string, { gr: number; h: number; n: number; st: number; przychod: number; nfz: number; pryw: number; reczny: number; nfzPay: number; prPay: number; recznyPay: number }>();
  const perMies = new Map<string, Map<string, number>>();                               // mk → gabinet → wynagrodzenie (grosze) – do netto
  const G = (g: string) => { let o = perGab.get(g); if (!o) { o = { gr: 0, h: 0, n: 0, st: 0, przychod: 0, nfz: 0, pryw: 0, reczny: 0, nfzPay: 0, prPay: 0, recznyPay: 0 }; perGab.set(g, o); } return o; };
  const M = (mk: string) => { let m = perMies.get(mk); if (!m) { m = new Map(); perMies.set(mk, m); } return m; };
  for (const x of dni.values()) {
    const o = G(x.gab), mk = x.date.slice(0, 7);
    o.h += x.h; if (x.dyzur) o.n++; o.przychod += x.przychod;
    const wObrocie = x.obrot !== null && x.obrotTyp === 'opisy';
    o.nfz += wObrocie ? 0 : x.nfzVal; o.pryw += wObrocie ? 0 : x.prVal; o.reczny += x.obrot ?? 0;
    if (!statements.has(mk + '|' + x.gab)) { o.gr += x.pay; M(mk).set(x.gab, (M(mk).get(x.gab) ?? 0) + x.pay); }
  }
  for (const [key, st] of statements) { const [mk, g] = key.split('|'); const o = G(g); o.gr += st; o.st++; M(mk).set(g, (M(mk).get(g) ?? 0) + st); }
  return { dni: [...dni.values()].sort((a, b) => a.date.localeCompare(b.date) || a.gab.localeCompare(b.gab)), perGab, perMies, rozliczenia: statements.size };
}
