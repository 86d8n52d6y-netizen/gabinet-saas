// Netto w Zarobkach = silnik Kalendarza (generator/kalendarz.html) uruchomiony na serwerze. Wynik policzony ręcznie wg zasad
// opisanych w Kalendarzu („Jak liczę”), parametry 2027 z PARAMS w kalendarz.html.
import { describe, expect, it } from 'vitest';
import { kalNettoZ, silnik } from '../src/lib/kal-silnik';

const clinic = { id: 'g1', name: 'A', model: 'daily', daily: 10000, pct: 0 };
const base = (extra: Record<string, unknown> = {}) => ({
  settings: { clinics: [clinic], jdgStart: '2026-10', regimes: { 2026: 'skala', 2027: 'ryczalt' }, ryczaltRate: 14,
    zus: [{ id: 'z1', from: '2026-10', variant: 'custom', amount: 800, chor: true }], setup: { zus: true }, ...extra },
  'm2027-01': { shifts: [{ id: 's1', date: '2027-01-10', clinicId: 'g1', status: 'done', start: '08:00', end: '15:00' }] },
});

describe('netto z ustawień Kalendarza', () => {
  it('silnik Kalendarza wczytuje się z generatora', async () => {
    const E = await silnik();
    expect(typeof E.computeYear).toBe('function');
    expect(E.shiftIncome({ status: 'done' }, clinic)).toBe(10000);
  });

  it('ryczałt 14%: ZUS 800, zdrowotna wg prognozowanego progu, podatek od przychodu', async () => {
    // zdrowotna płacona (próg 1): r2(r2(9828,50×60%)×9%) = 530,74; ryczałt: round(10000 − 800 − 265,37) × 14% = 8935 × 0,14 → 1251
    // prognoza roku: 10 000 + 11 × 10 000 (średnia) − 12 × 800 = 110 400 > 60 000 → realny próg 2: 9828,50 × 9% = 884,57
    // odłóż = 800 + 884,57 + 1251 = 2935,57 → netto = 10 000 × (1 − 2935,57/10 000) = 7064,43 zł
    const { info, perClinic } = await kalNettoZ(base(), '2027-01-01', '2027-01-31', '2027-01-20');
    expect(info.ok).toBe(true);
    expect(info.zasady).toEqual(['2027: ryczałt 14%']);
    expect(info.szacunek).toBe(true);                  // parametry 2027 oznaczone w Kalendarzu jako szacunek
    expect(perClinic.get('g1')).toBe(706443);
  });

  it('miesiąc przed założeniem JDG: bez ZUS i podatku, netto = brutto (jak w Kalendarzu)', async () => {
    const { perClinic } = await kalNettoZ(base({ jdgStart: '2027-06' }), '2027-01-01', '2027-01-31', '2027-01-20');
    expect(perClinic.get('g1')).toBe(1000000);
  });

  it('bez ustawień Kalendarza netto nie jest liczone; niepotwierdzony ZUS jest zgłaszany', async () => {
    const none = await kalNettoZ({}, '2027-01-01', '2027-01-31', '2027-01-20');
    expect(none.info.ok).toBe(false);
    expect(none.perClinic.size).toBe(0);
    // dokument Kalendarza bez wybranych podatków (nowe domyślne, K14) → netto nieliczone, niczego nie zakładamy
    for (const brak of [{ jdgStart: '' }, { regimes: {} }, { zus: [] }, { jdgStart: undefined, regimes: undefined, zus: undefined }]) {
      const r = await kalNettoZ({ ...base(), settings: { ...base().settings, ...brak } }, '2027-01-01', '2027-01-31', '2027-01-20');
      expect(r.info.ok, JSON.stringify(brak)).toBe(false);
      expect(r.perClinic.size).toBe(0);
    }
    const unconf = await kalNettoZ(base({ setup: {} }), '2027-01-01', '2027-01-31', '2027-01-20');
    expect(unconf.info.zusNiepotwierdzony).toBe(true);
  });

  it('dyżury poza okresem i nieodbyte nie wchodzą', async () => {
    const d = base();
    (d['m2027-01'].shifts as Record<string, unknown>[]).push({ id: 's2', date: '2027-01-11', clinicId: 'g1', status: 'planned' });
    const { perClinic } = await kalNettoZ(d, '2027-01-11', '2027-01-31', '2027-01-20');
    expect(perClinic.get('g1')).toBeUndefined();
  });
});
