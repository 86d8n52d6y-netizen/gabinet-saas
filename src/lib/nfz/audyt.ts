// Audyt NFZ (docs/nfz/, etap N6): reguły rozliczeń z data/nfz/ do wyświetlenia w Katalogu NFZ – tylko odczyt, bez danych pacjentów.
// Źródło prawdy: data/nfz/*.json (walidacja: scripts/waliduj_nfz.py). Reguły „WYMAGA WERYFIKACJI” pokazywane jako INFORMACJA (D4=A).
import 'server-only';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

export type RegulaNfz = { id: string; obszar: string; poziom: string; status: string; od: string; tresc: string; zrodla: string[] };
type Raw = { id: string; obszar: string; poziom: string; status: string; obowiazuje_od: string; tresc: string; zrodla: string[] };

let cache: { wersja: string; stan: string; reguly: RegulaNfz[] } | null = null;
export async function regulyNfz() {
  if (cache && process.env.NODE_ENV === 'production') return cache;
  const dir = path.join(process.cwd(), 'data', 'nfz');
  const j = async (f: string) => JSON.parse(await readFile(path.join(dir, f), 'utf8'));
  const [man, src, br] = await Promise.all([j('manifest.json'), j('sources.json'), j('billing-rules.json')]);
  const zr = new Map<string, string>((src.zrodla as { id: string; tytul: string }[]).map(s => [s.id, s.tytul]));
  const reguly = (br.reguly as Raw[]).map(r => ({ id: r.id, obszar: r.obszar, status: r.status, od: r.obowiazuje_od, tresc: r.tresc,
    poziom: r.status === 'WYMAGA WERYFIKACJI' ? 'INFORMACJA' : r.poziom, zrodla: r.zrodla.map(z => zr.get(z) ?? z) }));
  cache = { wersja: String(man.wersja), stan: String(man.stan_prawny_na), reguly };
  return cache;
}
