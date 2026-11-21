// Gabinety użytkownika (tabela app.clinics, RLS: tylko własne). Modele rozliczeń jak w Kalendarzu obecnej aplikacji.
export const MODELS = {
  pct_lab: '% po odjęciu kosztów własnych', pct_share: '% od obrotu, lab dzielony', pct: '% od całego obrotu',
  hourly: 'Stawka godzinowa', daily: 'Stawka za dzień', manual: 'Kwota wpisywana ręcznie',
} as const;
export type Model = keyof typeof MODELS;
export const COLORS = 8;   // paleta Kalendarza (--c1 … --c8)

export type Clinic = {
  id: string; name: string; short: string | null; color: number; active: boolean; model: Model;
  pct: number | null; labShare: number | null; hourlyGr: number | null; dailyGr: number | null; minDailyGr: number | null;
  address: string; version: number; deleted: boolean;
};
