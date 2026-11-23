// Brutto / netto w Zarobkach. Decyzja Patryka 21.11.2026: netto wg ustawień Kalendarza (wariant A) – forma opodatkowania,
// okresy ZUS, zdrowotna i parametry roczne wpisuje się w Kalendarzu (Ustawienia), tu ich nie dublujemy ani nie wymyślamy.
// Obliczenia: src/lib/kal-silnik.ts (ten sam silnik co Kalendarz). Netto dotyczy wynagrodzenia lekarza z centralnego mechanizmu
// (src/lib/zarobki-zrodla.ts – opisy + obrót ręczny); „Razem z wizyt” pozostaje brutto.
import type { PoolClient } from 'pg';
import { loadDocs } from './kal';
import { kalNettoZ, type NettoWynik } from './kal-silnik';
import { todayPL } from './zarobki';
import { zrodla } from './zarobki-zrodla';

export type KwotyTryb = 'brutto' | 'netto';
export const trybKwot = (v: string | undefined): KwotyTryb => (v === 'netto' ? 'netto' : 'brutto');

/** Netto per gabinet (grosze) dla okresu – z dokumentów Kalendarza tego użytkownika (połączenie w withUser). */
export async function kalNetto(c: PoolClient, from: string, to: string, today = todayPL()): Promise<NettoWynik> {
  const { docs } = await loadDocs(c);
  const { perMies } = await zrodla(c, from, to);                                          // brutto z centralnego mechanizmu (23.11.2026) – netto z tych samych kwot
  return kalNettoZ(docs, from, to, today, perMies);
}
