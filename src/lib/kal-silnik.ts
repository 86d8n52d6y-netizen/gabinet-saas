// Netto w Zarobkach wg ustawień Kalendarza (decyzja Patryka 21.11.2026: wariant A).
// Nie ma tu własnych stawek ani przepisów: na serwerze uruchamiany jest TEN SAM silnik obliczeń co w Kalendarzu
// (blok <script id="engine"> z generator/kalendarz.html – czyste funkcje, bez DOM), więc netto w Zarobkach i w Kalendarzu
// liczy się identycznie: forma opodatkowania na rok, okresy ZUS, zdrowotna, parametry roczne, etat, wakacje składkowe.
// Netto dyżuru = zarobek z dyżuru × (1 − udział „odłóż na ZUS i podatek” w danym miesiącu) – tak samo jak widok tygodnia Kalendarza.
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';

type Eng = Record<string, (...a: unknown[]) => unknown>;
type Doc = Record<string, unknown>;
type Month = { shifts: Doc[]; off: Doc; inv: Doc; costs: Doc[] };

let ENG: Promise<Eng> | null = null;

/** Silnik Kalendarza z pliku generatora (raz na proces). */
export function silnik(): Promise<Eng> {
  return (ENG ??= (async () => {
    const html = await readFile(path.join(process.cwd(), 'generator', 'kalendarz.html'), 'utf8');
    const m = html.match(/<script id="engine">([\s\S]*?)<\/script>/);
    if (!m) throw new Error('Brak silnika obliczeń w generator/kalendarz.html');
    const ctx = vm.createContext({ TextEncoder });
    return vm.runInContext(m[1] + '\n;E', ctx, { filename: 'kalendarz-engine.js', timeout: 2000 }) as Eng;
  })().catch(e => { ENG = null; throw e; }));
}

/* Domyślne wartości pól używanych przez silnik – jak normalizeSettings()/defaultSettings() w kalendarz.html (po K14:
   bez założeń o użytkowniku – pusty start JDG, brak formy opodatkowania i okresów ZUS). */
const DEF: Doc = { jdgStart: '', regimes: {}, ryczaltRate: 14, uop: {}, kwotaJDG: true, zus: [], wakacje: {}, healthMode: 'auto',
  annualOverride: {}, params: {}, setup: {} };
/** Jak taxReady() w Kalendarzu (K15): start JDG + forma opodatkowania + co najmniej jeden okres ZUS. */
export const taxReady = (s: Doc) => /^\d{4}-\d{2}$/.test(String(s.jdgStart ?? '')) && Object.keys((s.regimes as Doc) ?? {}).length > 0
  && Array.isArray(s.zus) && s.zus.length > 0;
const OBJ = ['regimes', 'uop', 'wakacje', 'annualOverride', 'params', 'setup'];

function settingsOf(raw: Doc): Doc {
  const s: Doc = structuredClone(raw);
  for (const [k, v] of Object.entries(DEF)) if (s[k] === undefined) s[k] = structuredClone(v);
  for (const k of OBJ) if (!s[k] || typeof s[k] !== 'object') s[k] = structuredClone(DEF[k]);
  if (!Array.isArray(s.zus)) s.zus = structuredClone(DEF.zus);
  if (!Array.isArray(s.clinics)) s.clinics = [];
  return s;
}
function monthOf(raw: unknown): Month {
  const d = (raw && typeof raw === 'object' ? raw : {}) as Doc;
  return { shifts: Array.isArray(d.shifts) ? d.shifts as Doc[] : [], off: d.off && typeof d.off === 'object' ? d.off as Doc : {},
    inv: d.inv && typeof d.inv === 'object' ? d.inv as Doc : {}, costs: Array.isArray(d.costs) ? d.costs as Doc[] : [] };
}

export type NettoInfo = {
  /** czy w Kalendarzu ustawiono podatki i ZUS (bez nich nie liczymy netto) */
  ok: boolean;
  /** opis zasad użytych w okresie, np. „2026: skala 12% / 32%” */
  zasady: string[];
  /** kwota ZUS nie została potwierdzona w Kalendarzu (krok „Kwota ZUS z eZUS”) */
  zusNiepotwierdzony: boolean;
  /** część parametrów roku to szacunki (np. 2027) */
  szacunek: boolean;
};
export type NettoWynik = { info: NettoInfo; perClinic: Map<string, number> };

const REG: Record<string, string> = { skala: 'skala 12% / 32%', liniowy: 'liniowy 19%' };

/**
 * Netto (grosze) odbytych dyżurów w okresie, per gabinet, z ustawień Kalendarza.
 * docs – dokumenty Kalendarza (settings z gabinetami z tabeli + miesiące mRRRR-MM), today – dziś (RRRR-MM-DD, Europe/Warsaw).
 */
export async function kalNettoZ(docs: Record<string, unknown>, from: string, to: string, today: string): Promise<NettoWynik> {
  const perClinic = new Map<string, number>();
  if (!docs.settings || typeof docs.settings !== 'object') return { info: { ok: false, zasady: [], zusNiepotwierdzony: false, szacunek: false }, perClinic };
  const E = await silnik();
  const settings = settingsOf(docs.settings as Doc);
  if (!taxReady(settings)) return { info: { ok: false, zasady: [], zusNiepotwierdzony: false, szacunek: false }, perClinic };
  const months = new Map<string, Month>();
  for (const [k, v] of Object.entries(docs)) if (/^m\d{4}-\d{2}$/.test(k) && v) months.set(k.slice(1), monthOf(v));
  const EMPTY = monthOf(null);
  const ctx = {
    settings,
    month: (mk: string) => months.get(mk) ?? EMPTY,
    allMonths: () => [...months.keys()].sort().map(mk => [mk, months.get(mk)!]),
  };
  const nowMk = today.slice(0, 7);
  const rates = E.clinicRates(ctx), avg = E.recentAvg(ctx, rates, nowMk);
  const years = new Map<number, { regime: string; rate: number; fcst: { months: { active: boolean; rev: number; reserve: number }[] } }>();
  const year = (y: number) => {
    if (!years.has(y)) years.set(y, E.computeYear(ctx, y, rates, nowMk, avg) as never);
    return years.get(y)!;
  };
  // jak reserveRatio() w Kalendarzu: udział z prognozy miesiąca, ograniczony do 0–95%; brak przychodu → 0
  const ratio = (mk: string) => {
    const o = year(+mk.slice(0, 4)).fcst.months[+mk.slice(5) - 1];
    if (!o || !o.active || !(o.rev > 0)) return 0;
    return Math.min(0.95, Math.max(0, o.reserve / o.rev));
  };
  const clinics = new Map((settings.clinics as Doc[]).map(k => [String(k.id), k]));
  for (const [mk, md] of months) {
    if (mk < from.slice(0, 7) || mk > to.slice(0, 7)) continue;
    const r = ratio(mk);
    for (const sh of md.shifts) {
      const d = String(sh?.date ?? '');
      if (!sh || sh.status !== 'done' || d < from || d > to || typeof sh.clinicId !== 'string') continue;
      const inc = E.shiftIncome(sh, clinics.get(sh.clinicId)) as number;
      perClinic.set(sh.clinicId, (perClinic.get(sh.clinicId) ?? 0) + Math.round(inc * (1 - r) * 100));
    }
  }
  const est = E.ESTIMATED as unknown as Record<string, unknown>;
  const ys: number[] = [];
  for (let y = +from.slice(0, 4); y <= +to.slice(0, 4); y++) ys.push(y);
  const zasady = ys.map(y => {
    const Y = year(y);
    return `${y}: ${Y.regime === 'ryczalt' ? `ryczałt ${Math.round(Y.rate * 100)}%` : REG[Y.regime] ?? Y.regime}`;
  });
  return { info: { ok: true, zasady, zusNiepotwierdzony: !(settings.setup as Doc).zus, szacunek: ys.some(y => !!est[y]) }, perClinic };
}
