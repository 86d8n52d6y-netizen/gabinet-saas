// Etap E4a – silnik pakietów zakładki „NFZ” (generator/nfz-pakiety.js). Punkty i współczynniki jak w Opisach NFZ (nfzPoints w generator/nfz.html).
import { describe, expect, it } from 'vitest';
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const ctx: { window: { NFZ_PAKIETY_DANE?: unknown } } = { window: {} };
vm.runInNewContext(readFileSync(path.join(ROOT, 'generator/nfz-pakiety-dane.js'), 'utf8'), ctx);
const D = ctx.window.NFZ_PAKIETY_DANE as never;
const E = createRequire(import.meta.url)(path.join(ROOT, 'generator/nfz-pakiety.js')) as { licz: (d: never, p: unknown[], o?: unknown) => Wynik };
type Wiersz = { kod: string; pts: number; n10: number; n08: number; q: number };
type Wynik = { wiersze: Wiersz[]; skladowe: { kod: string; pakiet: string }[]; nieliczone: { kod: string }[]; bledy: string[]; ostrz: string[]; suma: number };
const licz = (p: unknown[], o: unknown = { wiek: 40 }) => E.licz(D, p, o);
const kody = (w: Wynik) => w.wiersze.map(r => r.kod);

describe('pakiety – rozpoznanie i brak podwójnych punktów', () => {
  it('ekstrakcja wielokorzeniowa + znieczulenie przewodowe w karcie → ST02 104 pkt, znieczulenie 0 pkt w pakiecie', () => {
    const w = licz([{ kod: '23.1702', n: 1, zn: '23.0403' }]);
    expect(kody(w)).toEqual(['ST02']); expect(w.suma).toBe(104); expect(w.bledy).toEqual([]);
    expect(w.skladowe).toEqual([{ i: 0, kod: '23.0403', pakiet: 'ST02', zn: true }]);
  });
  it('ta sama ekstrakcja ze znieczuleniem jako osobna karta → też składowa (bez 20 pkt za 23.0403)', () => {
    const w = licz([{ kod: '23.1702' }, { kod: '23.0403' }]);
    expect(w.suma).toBe(104); expect(w.skladowe.map(s => s.pakiet)).toEqual(['ST02']);
  });
  it('znieczulenie z karty wypełnienia NIE wpada do pakietu ekstrakcji: ST02 104 + 1502 45 + 23.0402 12 = 161', () => {
    const w = licz([{ kod: '23.1702', zn: '23.0403' }, { kod: '23.1502', zn: '23.0402' }]);
    expect(w.suma).toBe(161); expect(w.skladowe.map(s => s.kod)).toEqual(['23.0403']); expect(kody(w)).toEqual(['ST02', '23.1502', '23.0402']);
  });
  it('ekstrakcja bez znieczulenia z listy ST1 → błąd: NFZ nie zapłaci', () => {
    const w = licz([{ kod: '23.1701' }]);
    expect(w.bledy.some(b => b.startsWith('ST01 wymaga procedury z listy ST1'))).toBe(true);
  });
  it('ekstrakcja + szycie małej rany (23.1809) → szycie w pakiecie (ST2), nie osobny ST27', () => {
    const w = licz([{ kod: '23.1701', zn: '23.0402' }, { kod: '23.1809' }]);
    expect(kody(w)).toEqual(['ST01']); expect(w.skladowe.map(s => s.kod).sort()).toEqual(['23.0402', '23.1809']);
  });
  it('samo szycie małej rany → własny pakiet ST27 (95 pkt)', () => {
    const w = licz([{ kod: '23.1809' }]); expect(kody(w)).toEqual(['ST27']); expect(w.suma).toBe(95);
  });
  it('ST27: szycie + opatrunek chirurgiczny (23.1815) w pakiecie; szycie + duża rana (23.1812) → osobny ST07 (zał. 1d)', () => {
    expect(kody(licz([{ kod: '23.1809' }, { kod: '23.1815' }]))).toEqual(['ST27']);
    expect(kody(licz([{ kod: '23.1809' }, { kod: '23.1812', zn: '23.0402' }])).sort()).toEqual(['ST07', 'ST27']);
  });
  it('kiretaż + opatrunek parodontologiczny → ST04 ze składową ST3, nie ST32', () => {
    const w = licz([{ kod: '23.1607', n: 2, zn: '23.0402' }, { kod: '23.1620' }]);
    expect(kody(w)).toEqual(['ST04']); expect(w.skladowe.some(s => s.kod === '23.1620' && s.pakiet === 'ST04')).toBe(true);
  });
  it('samo 23.1620 → ST32', () => { expect(kody(licz([{ kod: '23.1620' }]))).toEqual(['ST32']); });
  it('ST28: 23.0107 + 23.02 → jeden pakiet 96 pkt; bez 23.02 → błąd', () => {
    expect(licz([{ kod: '23.02' }, { kod: '23.0107' }]).suma).toBe(96);
    expect(licz([{ kod: '23.0107' }]).bledy.some(b => b.startsWith('ST28 wymaga'))).toBe(true);
  });
});

describe('współczynniki – jak w Opisach NFZ', () => {
  it('ST01 + wypełnienie 1 powierzchni (1502) = 138 pkt (jak t_9)', () => {
    expect(licz([{ kod: '23.1701', zn: '23.0402' }, { kod: '23.1502' }]).suma).toBe(138);
  });
  it('dziecko 10 lat: ×1,5 dla pakietu i świadczenia jednostkowego → 207 pkt', () => {
    expect(licz([{ kod: '23.1701', zn: '23.0402' }, { kod: '23.1502' }], { wiek: 10 }).suma).toBe(207);
  });
  it('kilka pakietów: najwyżej wyceniony ×1,0, kolejny ×0,8 (ST04 130 + ST01 93×0,8 = 204,4)', () => {
    const w = licz([{ kod: '23.1701', zn: '23.0402' }, { kod: '23.1607' }]);
    expect(w.suma).toBe(204.4); expect(w.wiersze.find(r => r.kod === 'ST01')).toMatchObject({ n10: 0, n08: 1 });
  });
  it('2 ekstrakcje = 2 pakiety: 104 + 104×0,8', () => { expect(licz([{ kod: '23.1702', n: 2, zn: '23.0403' }]).suma).toBe(187.2); });
  it('ciąża: ×1,2', () => { expect(licz([{ kod: '23.1502' }], { wiek: 30, ciaza: true }).suma).toBe(54); });
});

describe('higienizacja < 18 (ST30D–ST30G, 95/2026/DSOZ)', () => {
  it('badanie z instruktażem + 3 × ½ łuku miękkie → 1× ST30D + 2× ST30E, bez ×1,5 i bez ×0,8 dla ST30E = 114 pkt', () => {
    const w = licz([{ kod: '23.0101' }, { kod: '23.16011', n: 3 }], { wiek: 10 });
    expect(kody(w)).toEqual(['ST30D', 'ST30E']); expect(w.suma).toBe(114); expect(w.bledy).toEqual([]);
    expect(w.skladowe).toEqual([{ i: 0, kod: '23.0101', pakiet: 'ST30D', zn: false }]);
  });
  it('kolejność kart bez znaczenia (higienizacja przed badaniem)', () => {
    expect(licz([{ kod: '23.16011', n: 3 }, { kod: '23.0101' }], { wiek: 10 }).suma).toBe(114);
  });
  it('całe uzębienie miękkie: z badaniem → ST30F (138), bez → ST30G (96)', () => {
    expect(licz([{ kod: '23.16021' }, { kod: '23.0101' }], { wiek: 12 }).suma).toBe(138);
    expect(licz([{ kod: '23.16021' }], { wiek: 12 }).suma).toBe(96);
  });
  it('ST30D + lakierowanie (ST5) → lakierowanie w pakiecie; ST30F + 1101 → bez błędów', () => {
    expect(licz([{ kod: '23.0101' }, { kod: '23.16011' }, { kod: '23.1006' }], { wiek: 10 }).skladowe.some(s => s.kod === '23.1006')).toBe(true);
    expect(licz([{ kod: '23.0101' }, { kod: '23.16021' }, { kod: '23.1101' }], { wiek: 10 }).bledy).toEqual([]);
  });
  it('ST30F + wypełnienie → błąd „dosumować wyłącznie 23.1101”', () => {
    expect(licz([{ kod: '23.0101' }, { kod: '23.16021' }, { kod: '23.1502' }], { wiek: 10 }).bledy.some(b => b.startsWith('Do ST30F można dosumować wyłącznie'))).toBe(true);
  });
  it('ST30 (złogi twarde) + lakierowanie → błąd „nie sumują się”', () => {
    expect(licz([{ kod: '23.16012' }, { kod: '23.1006' }]).bledy.some(b => b.includes('nie sumują się'))).toBe(true);
  });
  it('ST30D u 18-latka → ostrzeżenie o wieku', () => {
    expect(licz([{ kod: '23.0101' }, { kod: '23.16011' }], { wiek: 18 }).ostrz.some(o => o.startsWith('ST30D – świadczenie dla dzieci'))).toBe(true);
  });
  it('ST30D + 4× ST30E → ostrzeżenie „maks. za 3 × ST30E”', () => {
    expect(licz([{ kod: '23.0101' }, { kod: '23.16011', n: 5 }], { wiek: 10 }).ostrz.some(o => o.includes('maks. za 3 × ST30E'))).toBe(true);
  });
});

describe('świadczenia jednostkowe', () => {
  it('znane (rozliczane w Opisach NFZ) liczone; RTG z zał. 1b – punkty widoczne, nie wliczone', () => {
    const w = licz([{ kod: '23.1503' }, { kod: '23.0301' }]);
    expect(w.suma).toBe(54); expect(w.nieliczone.map(x => x.kod)).toEqual(['23.0301']);
  });
  it('samo znieczulenie przy wypełnieniu – liczone osobno jak w Opisach NFZ (23.0402 = 12 pkt)', () => {
    expect(licz([{ kod: '23.1502', zn: '23.0402' }]).suma).toBe(57);
  });
});
