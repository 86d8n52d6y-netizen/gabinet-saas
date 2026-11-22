// Baza stomatologiczna (docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md): katalog badań i karty procedur ICD-9 z data/ – tylko odczyt,
// bez danych pacjentów. Źródło prawdy: data/badania, data/procedury-icd9, data/baza-stomatologiczna (walidacja: scripts/waliduj_baze.py).
import 'server-only';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

type Rec = Record<string, unknown>;
export type Poz = { tekst: string; podstawa: string; zrodla?: string[]; warunek?: string };
export type Procedura = Rec & { id: string; kod: string; nazwa_oficjalna: string; nazwa_krotka?: string; kategoria: string; status: string; uzasadnienie_statusu?: string; opis?: string; kody_aplikacji?: string[] };
export type Badanie = Rec & { id: string; nazwa: string; nazwa_krotka: string; kategoria: string; status: string };
export type Szablon = { id: string; dotyczy: string; wariant: string; tekst: string; pola: string[]; tekst_aplikacji?: string };
export type ElementChk = { id: string; tekst: string; poziom: string; podstawa: string; zrodla?: string[]; warunek?: string; pole?: string };
export type Baza = {
  wersja: string; badania: Badanie[]; procedury: Procedura[]; szablony: Szablon[];
  pola: Map<string, Rec & { etykieta: string }>; kroki: Map<string, { nazwa: string; opis: string; uwaga?: string; warianty?: string[] }>;
  materialy: Map<string, { nazwa: string; kategoria: string; uwagi?: string }>; zrodla: Map<string, { opis: string; pmid?: string | null; status: string }>;
  checklisty: Map<string, { wspolne: string[]; elementy: ElementChk[] }>; wspolne: Map<string, ElementChk>;
  mapowania: { procedura: string; icd10: string; okolicznosci: string; potwierdzenie: string; w_audycie_nfz?: boolean }[]; icd10: Map<string, string>;
};

let cache: Baza | null = null;
export async function baza(): Promise<Baza> {
  if (cache && process.env.NODE_ENV === 'production') return cache;
  const j = async (...p: string[]) => JSON.parse(await readFile(path.join(process.cwd(), 'data', ...p), 'utf8'));
  const [man, bad, pb, sb, pw, pr, kr, mt, sp, ch, mp, zk, zn, dg] = await Promise.all([
    j('baza-stomatologiczna', 'manifest.json'), j('badania', 'examinations.json'), j('badania', 'examination-fields.json'), j('badania', 'examination-templates.json'),
    j('baza-stomatologiczna', 'pola-wspolne.json'), j('procedury-icd9', 'procedures.json'), j('procedury-icd9', 'procedure-steps.json'), j('procedury-icd9', 'procedure-materials.json'),
    j('procedury-icd9', 'procedure-templates.json'), j('procedury-icd9', 'procedure-checklists.json'), j('procedury-icd9', 'procedure-diagnosis-mappings.json'),
    j('baza-stomatologiczna', 'zrodla-kliniczne.json'), j('nfz', 'sources.json'), j('nfz', 'diagnoses.json')]);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const m = (l: any[]) => new Map<string, any>(l.map(x => [x.id, x]));
  cache = {
    wersja: String(man.wersja), badania: bad.badania, procedury: pr.procedury, szablony: [...sb.szablony, ...sp.szablony],
    pola: m([...pw.pola, ...pb.pola]), kroki: m(kr.kroki), materialy: m(mt.materialy),
    zrodla: new Map([...zn.zrodla.map((s: { id: string; tytul: string; status: string }) => [s.id, { opis: s.tytul, status: s.status }]),
      ...zk.zrodla.map((s: { id: string; opis: string; pmid: string | null; status: string }) => [s.id, { opis: s.opis, pmid: s.pmid, status: s.status }])]),
    checklisty: new Map(ch.checklisty.map((c: { procedura: string; wspolne?: string[]; elementy: ElementChk[] }) => [c.procedura, { wspolne: c.wspolne ?? [], elementy: c.elementy }])),
    wspolne: m(ch.wspolne), mapowania: mp.mapowania, icd10: new Map(dg.diagnozy.map((d: { kod: string; nazwa_pl_robocza: string }) => [d.kod, d.nazwa_pl_robocza])),
  };
  return cache as Baza;
}

export const STATUS: Record<string, string> = { draft: 'wersja robocza – do weryfikacji', requires_expert_review: 'do oceny specjalisty', verified: 'zweryfikowana', not_started: 'nieopracowana', in_progress: 'w opracowaniu' };
export const PODSTAWA: Record<string, string> = { wymaganie_prawne: 'prawne', wymaganie_nfz: 'NFZ', zalecenie_kliniczne: 'zalecenie kliniczne', propozycja_aplikacji: 'propozycja aplikacji' };
export const POZIOM: Record<string, string> = { obowiazkowe: 'obowiązkowe (ostrzeżenie)', zalecane: 'zalecane', sytuacyjne: 'zależne od sytuacji', rozliczeniowe: 'rozliczenie NFZ' };
