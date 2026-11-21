// Walidacja zleceń przed zapisem na koncie (E7): tylko pola z listy; nigdy imię i nazwisko, PESEL, adres, zdjęcia.
import { describe, expect, it } from 'vitest';
import { clean } from '../src/lib/zlecenia';

const ok = { id: 'zabc12345', nr: 'ZP-2026-001', typ: 'kor-emax', status: 'wysłane', data: '2026-11-21', at: '2026-11-21T10:00:00Z',
  a: { ini: 'AB', zeby: '11, 21', etapy: ['przymiarka konstrukcji'], schemat: { '11': 'korona', '21': 'korona' }, zUw: { '11': 'abfrakcja' }, fotoDruk: false },
  hist: [{ at: '2026-11-21T10:00:00Z', co: 'utworzono' }] };

describe('zlecenia – walidacja', () => {
  it('przyjmuje poprawne zlecenie bez zmian', () => { expect(clean(ok)).toEqual(ok); });
  it.each(['pesel', 'imie', 'nazwisko', 'adres', 'pacjent', 'zdjecia', 'foto'])('odrzuca pole „%s” w treści', f => {
    expect(() => clean({ ...ok, a: { ...ok.a, [f]: 'x' } })).toThrow(/niedozwolone/);
  });
  it('odrzuca nieznane pole główne (np. zdjęcia obok treści)', () => { expect(() => clean({ ...ok, zdjecia: [] })).toThrow(/niedozwolone/); });
  it('odrzuca schemat z numerem spoza FDI', () => { expect(() => clean({ ...ok, a: { ...ok.a, schemat: { 'xx': 'korona' } } })).toThrow(); });
  it('odrzuca zbyt długi tekst i zły identyfikator', () => {
    expect(() => clean({ ...ok, a: { ...ok.a, uwagi: 'x'.repeat(4001) } })).toThrow();
    expect(() => clean({ ...ok, id: '../x' })).toThrow(/identyfikator/);
  });
  it('odrzuca obce pola w historii', () => { expect(() => clean({ ...ok, hist: [{ at: 'x', co: 'y', pesel: '1' }] })).toThrow(/historia/); });
});
