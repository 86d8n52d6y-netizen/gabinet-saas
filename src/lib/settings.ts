// Ustawienia rozliczeń NFZ użytkownika (tabela user_settings, kolumna settings → klucz "nfz").
// Domyślne wartości jak w obecnej aplikacji: 1,84 zł/pkt, udział lekarza 40% (lub 35%), 350 zł/h przeglądów, podstawa: pełna wartość.
// Stawek domyślnych nie zmieniamy bez decyzji Patryka (CLAUDE.md).
import type { Basis } from './nfz/engine';

export const PRICE_DEF = 1.84, REV_DEF = 350, PCT_OPTS = [40, 35] as const;
export type NfzSettings = { price: number; pct: number; rev: number; basis: Basis };
export const NFZ_DEFAULTS: NfzSettings = { price: PRICE_DEF, pct: 40, rev: REV_DEF, basis: 'full' };

/** Te same zasady poprawności co cfgApply w nfz.html. */
export function cleanNfz(x: unknown): NfzSettings {
  const c = (x && typeof x === 'object' ? x : {}) as Record<string, unknown>;
  const d = { ...NFZ_DEFAULTS };
  const price = Number(c.price), pct = Number(c.pct), rev = Number(c.rev);
  if (price > 0 && price < 100) d.price = price;
  if ((PCT_OPTS as readonly number[]).includes(pct)) d.pct = pct;
  if (rev > 0 && rev < 100000) d.rev = rev;
  d.basis = c.basis === 'share' ? 'share' : 'full';
  return d;
}
/** Liczba z polskim przecinkiem; NaN gdy niepoprawna. */
export function parseNum(v: string): number {
  const s = String(v ?? '').trim().replace(/[\s ]/g, '').replace(/zł$/i, '').replace(',', '.');
  return /^\d+(\.\d+)?$/.test(s) ? parseFloat(s) : NaN;
}
