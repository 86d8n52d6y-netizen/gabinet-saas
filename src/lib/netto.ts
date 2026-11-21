// Brutto / netto w Zarobkach. Decyzja Patryka 21.11.2026: netto wg ustawień Kalendarza (wariant A) – forma opodatkowania,
// okresy ZUS, zdrowotna i parametry roczne wpisuje się w Kalendarzu (Ustawienia), tu ich nie dublujemy ani nie wymyślamy.
// Obliczenia: src/lib/kal-silnik.ts (ten sam silnik co Kalendarz). Netto dotyczy zarobku lekarza z odbytych dyżurów;
// kwoty z wizyt (Opisy NFZ / prywatne) pozostają brutto.
import type { PoolClient } from 'pg';
import { loadDocs } from './kal';
import { kalNettoZ, type NettoWynik } from './kal-silnik';
import { todayPL } from './zarobki';

export type KwotyTryb = 'brutto' | 'netto';
export const trybKwot = (v: string | undefined): KwotyTryb => (v === 'netto' ? 'netto' : 'brutto');

/** Netto per gabinet (grosze) dla okresu – z dokumentów Kalendarza tego użytkownika (połączenie w withUser). */
export async function kalNetto(c: PoolClient, from: string, to: string, today = todayPL()): Promise<NettoWynik> {
  const { docs } = await loadDocs(c);
  return kalNettoZ(docs, from, to, today);
}
