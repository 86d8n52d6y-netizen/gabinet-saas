// Katalog procedur (etap porządkowania 23.11.2026, prompt Patryka pkt 3): dwie rozdzielone tabele w jednym widoku.
// Tabela 1 – procedury NFZ: karty rozliczane w NFZ (ta sama reguła co zakładka „NFZ”: świadczenie gwarantowane albo wycena
//   w zarządzeniu – pakiet / lista dodatkowa zał. 1d / świadczenie jednostkowe zał. 1b) z zasadą rozliczenia punktowego.
// Tabela 2 – procedury prywatne: własne procedury Opisów prywatnych + karty nierozliczane w NFZ; ceny i wynagrodzenie lekarza z Cennika.
// Dane rozliczenia NFZ: generator/nfz-pakiety-dane.js (te same, z których liczy zakładka NFZ – scripts/nfz_pakiety_przegladarka.py).
import 'server-only';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { baza, type Procedura } from './baza';

type Pak = { pkt: number; kier: string[]; wym: string[]; opc: string[]; kody_opc?: string[] };
export type NfzDane = { pakiety: Record<string, Pak>; listy: Record<string, string[]>; jednostkowe: Record<string, { pkt: number; nazwa: string; znane: boolean }>; zrodlo: string };
export type NfzRozl =
  | { typ: 'pakiet'; pakiety: { id: string; pkt: number }[] }
  | { typ: 'skladowa'; listy: string[]; wlasny?: { id: string; pkt: number }; jedn?: { pkt: number; liczone: boolean } }
  | { typ: 'jednostkowe'; pkt: number; liczone: boolean }
  | { typ: 'brak' };
export type PozNfz = { kod: string; nazwa: string; kategoria: string; gwarantowane: boolean; rozl: NfzRozl };
export type PozPryw = { id: string; nazwa: string; kat: string; kod?: string; wlasna: boolean };

const G = (...p: string[]) => path.join(process.cwd(), 'generator', ...p);
async function wczytajJs<T>(plik: string, nazwa: string, pre: Record<string, unknown> = {}): Promise<T> {
  const ctx: { window: Record<string, unknown> } = { window: { ...pre } };
  vm.runInNewContext(await readFile(G(plik), 'utf8'), ctx, { timeout: 2000 });
  return ctx.window[nazwa] as T;
}
let cache: { nfz: PozNfz[]; pryw: PozPryw[]; kat: { id: string; name: string }[]; dane: NfzDane } | null = null;

/** Zasada rozliczenia NFZ dla kodu ICD-9 karty (bez podwójnego liczenia: składowa pakietu = 0 pkt, gdy pakiet jest na wizycie). */
export function rozliczenieNfz(d: NfzDane, kod: string): NfzRozl {
  const pak = Object.entries(d.pakiety).filter(([, p]) => p.kier.includes(kod)).map(([id, p]) => ({ id, pkt: p.pkt }));
  const listy = Object.keys(d.listy).filter(l => d.listy[l].includes(kod));
  const j = d.jednostkowe[kod];
  const WLASNY: Record<string, string> = { '23.1809': 'ST27', '23.1812': 'ST07', '23.1815': 'ST31', '23.1620': 'ST32' };
  if (listy.length) return { typ: 'skladowa', listy, ...(WLASNY[kod] ? { wlasny: { id: WLASNY[kod], pkt: d.pakiety[WLASNY[kod]].pkt } } : {}), ...(j ? { jedn: { pkt: j.pkt, liczone: j.znane } } : {}) };
  if (pak.length) return { typ: 'pakiet', pakiety: pak };
  if (j) return { typ: 'jednostkowe', pkt: j.pkt, liczone: j.znane };
  return { typ: 'brak' };
}

export async function katalog() {
  if (cache && process.env.NODE_ENV === 'production') return cache;
  const [b, dane, karty, pk] = await Promise.all([baza(), wczytajJs<NfzDane>('nfz-pakiety-dane.js', 'NFZ_PAKIETY_DANE'),
    wczytajJs<{ karty: { kod: string; nfz: boolean }[] }>('karty-opisy.js', 'KARTY_OPISY'),
    wczytajJs<{ kat: { id: string; name: string }[]; proc: { id: string; kat: string; name: string }[] }>('prywatne-katalog.js', 'PRYW_KATALOG')]);
  const wycena = new Set([...Object.values(dane.pakiety).flatMap(p => p.kier), ...Object.values(dane.listy).flat(), ...Object.keys(dane.jednostkowe)]);
  const proc = new Map(b.procedury.map(p => [p.kod, p] as [string, Procedura]));
  const nazwa = (p?: Procedura) => p ? (p.nazwa_krotka ?? p.nazwa_oficjalna) : '';
  const nfz: PozNfz[] = [], pryw: PozPryw[] = pk.proc.map(p => ({ id: p.id, nazwa: p.name, kat: p.kat, wlasna: true }));
  // kategorie kart → kategorie Opisów prywatnych (jak generator/prywatne-karty.js)
  const KMAP: Record<string, string> = { 'badanie i porada': 'diag', diagnostyka: 'diag', radiologia: 'diag', profilaktyka: 'hig', 'periodontologia i błona śluzowa': 'hig',
    'leczenie próchnicy': 'zach', 'odbudowa i estetyka': 'zach', dziecko: 'zach', 'urazy zębów': 'zach', 'endodoncja – leczenie kanałowe': 'endo', 'endodoncja – leczenie miazgi': 'endo',
    'chirurgia – ekstrakcje': 'chir', 'chirurgia stomatologiczna': 'chir', 'chirurgia – zakażenia': 'chir', znieczulenie: 'znie' };
  for (const k of karty.karty) {
    const p = proc.get(k.kod);
    if (k.nfz || wycena.has(k.kod)) nfz.push({ kod: k.kod, nazwa: nazwa(p), kategoria: p?.kategoria ?? '', gwarantowane: k.nfz, rozl: rozliczenieNfz(dane, k.kod) });
    else pryw.push({ id: 'karta-' + k.kod.replace(/\./g, '_'), nazwa: nazwa(p), kat: KMAP[p?.kategoria ?? ''] ?? (/^protetyka/.test(p?.kategoria ?? '') ? 'prot' : 'diag'), kod: k.kod, wlasna: false });
  }
  const kat = [...pk.kat, { id: 'prot', name: 'Protetyka' }, { id: 'znie', name: 'Znieczulenia' }];
  cache = { nfz, pryw, kat, dane };
  return cache;
}

/** Cena i wynagrodzenie lekarza z Cennika gabinetu (pryw:cennik; kwoty w groszach) – ta sama kolejność co priceFor() w Opisach prywatnych,
 *  z uzupełnieniem: brak % w Cenniku → % gabinetu z „Gabinety” (modele procentowe). */
export function cenaPryw(cennik: unknown, gab: string, pid: string, klinikaPct: number | null) {
  const g = ((cennik as { gab?: Record<string, { pct?: number | null; items?: Record<string, { c?: number | null; m?: string; p?: number | null; kw?: number | null }> }> } | null)?.gab ?? {})[gab || '-'] ?? {};
  const e = (g.items ?? {})[pid] ?? {};
  const c = typeof e.c === 'number' ? e.c : null;
  if (e.m === 'kw') return { c, opis: 'kwota ' + ((e.kw ?? 0) / 100).toFixed(2).replace('.', ',') + ' zł', pay: e.kw ?? 0 };
  const pct = typeof e.p === 'number' ? e.p : typeof g.pct === 'number' ? g.pct : klinikaPct;
  return { c, opis: pct == null ? 'brak %' : String(pct).replace('.', ',') + '%' + (typeof e.p === 'number' ? '' : typeof g.pct === 'number' ? ' (domyślny w Cenniku)' : ' (z Gabinetów)'), pay: c != null && pct != null ? Math.round(c * pct / 100) : null };
}
