// Silnik wyceny NFZ – przeniesiony 1:1 z obecnej aplikacji (nfz.html: nfzPoints, ptsCoef, centsPts, centsPct, centsHours, calc).
// Czysty moduł (bez bazy i bez DOM): ten sam kod liczy w przeglądarce i na serwerze. Zgodność ze starą wersją
// sprawdza test porównawczy (tests/e2e/t_silnik_nfz.py – tysiące losowych przypadków w obu wersjach).
//
// Zasady (źródło: komentarze i stałe w nfz.html; zarządzenia DSOZ podane w katalogu):
//   § 12 ust. 2  – ×1,5 dzieci i młodzież do ukończenia 18 r.ż.;  § 12 ust. 2a – ×1,5 nie dotyczy ST30D–ST30G (no15),
//   § 12 ust. 3  – ×1,2 kobieta w ciąży lub połogu (gdy nie stosuje się ×1,5),
//   § 13 ust. 1 pkt 5 – kilka pakietów na wizycie: najwyżej wyceniony ×1,0, kolejne ×0,8;  pkt 5a – nie dotyczy ST30E i ST30G (no08).
//   Świadczenia jednostkowe (kody liczbowe, znieczulenia) nie podlegają ×0,8.

export type CatalogEntry = {
  code: string; name: string; points: number;
  kind: 'pkg' | 'unit' | 'anest'; unit: string | null; no15: boolean; no08: boolean; minPerPkg: number | null;
};
export type Catalog = Record<string, CatalogEntry>;

/** Własna procedura NFZ użytkownika – „niesprawdzana przez zasady NFZ”: punkty × ilość, bez współczynników i bez ×0,8. */
export type CustomCode = { code: string; name: string; points: number };

export type PointsInput = {
  items: { code: string; qty: number }[];   // kody z katalogu (ilość: zęby / ćwiartki / kanały / pakiety)
  anest?: Record<string, number>;           // znieczulenia: kod → liczba
  custom?: { item: CustomCode; qty: number }[];
  age: number | null;                       // wiek pacjenta (bez danych osobowych – tylko liczba lat)
  pregnant: boolean;
};
export type PointsRow = {
  code: string; name: string; qty: number; base: number; k: number; kNote: string;
  pkg: boolean; n10: number; n08: number; pts: number; custom?: boolean;
};

export function coefficient(e: Pick<CatalogEntry, 'no15'>, age: number | null, pregnant: boolean): [number, string] {
  if (age !== null && age < 18) return e.no15 ? [1, 'bez ×1,5'] : [1.5, '×1,5'];
  if (age !== null && pregnant) return [1.2, '×1,2'];
  return [1, ''];
}

export function nfzPoints(cat: Catalog, inp: PointsInput): { rows: PointsRow[]; total: number } {
  const rows: PointsRow[] = [];
  const inst: { r: PointsRow; v: number }[] = [];
  for (const { code, qty } of inp.items) {
    const e = cat[code];
    if (!e || e.kind === 'anest') continue;
    const [k, kNote] = coefficient(e, inp.age, inp.pregnant);
    const r: PointsRow = { code, name: e.name, qty, base: e.points, k, kNote, pkg: e.kind === 'pkg', n10: qty, n08: 0, pts: 0 };
    rows.push(r);
    if (r.pkg && !e.no08) for (let i = 0; i < qty; i++) inst.push({ r, v: r.base * r.k });
  }
  if (inst.length > 1) {
    const top = inst.reduce((m, x) => (x.v > m.v ? x : m), inst[0]);
    for (const r of rows) if (r.pkg && !cat[r.code].no08) { r.n10 = 0; r.n08 = r.qty; }
    top.r.n10 = 1; top.r.n08 -= 1;
  }
  for (const [code, n] of Object.entries(inp.anest ?? {})) {
    const e = cat[code];
    if (!e || e.kind !== 'anest' || !(n > 0)) continue;
    const [k, kNote] = coefficient(e, inp.age, inp.pregnant);
    rows.push({ code: '23.' + code, name: e.name, qty: n, base: e.points, k, kNote, pkg: false, n10: n, n08: 0, pts: 0 });
  }
  for (const r of rows) r.pts = r.base * r.k * (r.n10 + 0.8 * r.n08);
  for (const { item, qty } of inp.custom ?? []) {
    if (!(qty > 0)) continue;
    rows.push({ code: item.code, name: item.name, qty, base: item.points, k: 1, kNote: 'niesprawdzane', pkg: false, n10: qty, n08: 0, pts: item.points * qty, custom: true });
  }
  return { rows, total: Math.round(rows.reduce((t, r) => t + r.pts, 0) * 100) / 100 };
}

// ---- kwoty w groszach (liczby całkowite; zaokrąglenia jak w obecnej aplikacji) ----
export const centsPts = (pts: number, price: number) => Math.round(Math.round((+pts || 0) * 100) * Math.round((+price || 0) * 10000) / 10000);
export const centsPct = (c: number, pct: number) => Math.round(c * (+pct || 0) / 100);
export const centsHours = (h: number, rate: number) => Math.round(Math.round((+h || 0) * 100) * Math.round((+rate || 0) * 100) / 100);

export type Basis = 'full' | 'share';
/** Kwoty wpisu: pc – wartość punktów, sh – udział lekarza, rv – przeglądy, ex – kwoty dodatkowe, pe – punkty wg podstawy, total. */
export function visitMoney(m: { pts: number; price: number; pct: number; revH: number; revRate: number; ex?: { c: number }[] }, basis: Basis) {
  const pc = centsPts(m.pts, m.price), sh = centsPct(pc, m.pct), rv = centsHours(m.revH, m.revRate);
  const ex = (m.ex ?? []).reduce((s, e) => s + e.c, 0);
  const pe = basis === 'share' ? sh : pc;
  return { pc, sh, rv, ex, pe, total: pe + rv + ex };
}

// ---- formatowanie (jak w obecnej aplikacji) ----
export const fmtP = (x: number) => (Math.round(x * 100) / 100).toFixed(2).replace(/\.?0+$/, '').replace('.', ',');
export const fmtC = (gr: number) => (gr / 100).toLocaleString('pl-PL', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' zł';
export function packageNote(r: PointsRow, cat: Catalog): string {
  if (r.custom) return 'własny kod';
  if (!r.pkg) return 'jednostkowe';
  if (cat[r.code]?.no08) return '×1,0 (bez ×0,8)';
  if (!r.qty) return '—';
  if (!r.n08) return r.qty > 1 ? r.qty + '×1,0' : '×1,0';
  if (r.n10) return '1×1,0 + ' + r.n08 + '×0,8';
  return r.qty > 1 ? r.n08 + '×0,8' : '×0,8';
}
