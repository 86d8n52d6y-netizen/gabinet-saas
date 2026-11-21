// Brutto / netto w Zarobkach (decyzja Patryka 21.11.2026).
// Kwoty w aplikacji są BRUTTO (przed podatkiem, składkami i innymi potrąceniami). Zasady wyliczania netto Patryk przekaże później,
// dlatego nie ma tu żadnych stawek, składek ani przykładowych wartości: dopóki konfiguracji nie ma, netto jest nieaktywne
// i aplikacja pokazuje informację „wymaga konfiguracji” zamiast wymyślonego wyniku.
import type { PoolClient } from 'pg';

/** Konfiguracja netto – struktura zarezerwowana; zostanie zdefiniowana po przekazaniu zasad rozliczenia przez Patryka. */
export type NettoConfig = { version: 1; rules: unknown };

export type KwotyTryb = 'brutto' | 'netto';
export const trybKwot = (v: string | undefined): KwotyTryb => (v === 'netto' ? 'netto' : 'brutto');

/** Wczytuje konfigurację netto z ustawień konta (user_settings.settings.netto). Dziś zawsze null – brak skonfigurowanych zasad. */
export async function loadNetto(c: PoolClient): Promise<NettoConfig | null> {
  const n = (await c.query('SELECT settings->\'netto\' AS n FROM app.user_settings')).rows[0]?.n;
  return n && typeof n === 'object' && n.version === 1 && n.rules ? (n as NettoConfig) : null;
}

/** Przeliczenie kwoty brutto (grosze) na netto. Bez konfiguracji – null (nie zgadujemy). Reguły zostaną dodane po decyzji Patryka. */
export function naNetto(bruttoGr: number, cfg: NettoConfig | null): number | null {
  if (!cfg) return null;
  return null;   // zasady netto nie są jeszcze zdefiniowane – celowo brak obliczeń
}
