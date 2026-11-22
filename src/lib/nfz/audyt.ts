// Audyt NFZ (docs/nfz/, etap N6): reguły rozliczeń z data/nfz/ do wyświetlenia w Katalogu NFZ – tylko odczyt, bez danych pacjentów.
// Poziom w aplikacji wg decyzji Patryka z data/decyzje-nfz.json (ta sama logika co scripts/nfz_dane_przegladarka.py; test t_9 porównuje oba).
import 'server-only';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

export type RegulaNfz = { id: string; obszar: string; poziom: string; poziomAudyt: string; decyzja: string; status: string; od: string; tresc: string; zrodla: string[] };
type Raw = { id: string; obszar: string; poziom: string; status: string; obowiazuje_od: string; tresc: string; zrodla: string[] };
type Dec = { poziom: string; decyzja: string };

let cache: { wersja: string; stan: string; reguly: RegulaNfz[] } | null = null;
export async function regulyNfz() {
  if (cache && process.env.NODE_ENV === 'production') return cache;
  const j = async (...f: string[]) => JSON.parse(await readFile(path.join(process.cwd(), 'data', ...f), 'utf8'));
  const [man, src, br, lim, dec] = await Promise.all([j('nfz', 'manifest.json'), j('nfz', 'sources.json'), j('nfz', 'billing-rules.json'),
    j('nfz', 'limits-and-combinations.json'), j('decyzje-nfz.json')]);
  const zr = new Map<string, string>((src.zrodla as { id: string; tytul: string }[]).map(s => [s.id, s.tytul.split(' – ')[0]]));
  const limity = new Set((lim.limity as { regula: string }[]).map(l => l.regula));
  const ogolne = dec.zasady_ogolne as Record<string, Dec>, wyj = dec.reguly as Record<string, Dec>;
  const reguly = (br.reguly as Raw[]).map(r => {
    const d: Dec | null = r.status === 'WYMAGA WERYFIKACJI' ? ogolne.wymaga_weryfikacji : wyj[r.id] ?? (limity.has(r.id) ? ogolne.limity_z_historii : null);
    return { id: r.id, obszar: r.obszar, status: r.status, od: r.obowiazuje_od, tresc: r.tresc, poziomAudyt: r.poziom,
      poziom: d ? d.poziom : r.poziom, decyzja: d && d.poziom !== r.poziom ? d.decyzja : '', zrodla: r.zrodla.map(z => zr.get(z) ?? z) };
  });
  cache = { wersja: String(man.wersja), stan: String(man.stan_prawny_na), reguly };
  return cache;
}
