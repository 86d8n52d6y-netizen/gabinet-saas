# -*- coding: utf-8 -*-
"""Audyt NFZ, etap N1: dane z data/nfz/*.json → generator/nfz-dane.js (window.NFZ_DANE) dla Opisów NFZ w przeglądarce.
Reguły z wiekiem, zębem i ciążą liczy wyłącznie urządzenie (decyzja Patryka D2=A) – ten plik niczego nie wysyła.
Nie edytuj generator/nfz-dane.js ręcznie: popraw JSON w data/nfz/, uruchom scripts/waliduj_nfz.py, potem
python3 tests/tools/przenies_generator.py <opisy-nfz> (wywołuje ten skrypt) albo bezpośrednio:  python3 scripts/nfz_dane_przegladarka.py"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'data' / 'nfz'
OUT = ROOT / 'generator' / 'nfz-dane.js'


def zbuduj():
    L = lambda p: json.loads((D / p).read_text(encoding='utf-8'))
    man, src, rules = L('manifest.json'), L('sources.json'), L('billing-rules.json')
    lim, mp, dg = L('limits-and-combinations.json'), L('procedure-diagnosis-mappings.json'), L('diagnoses.json')
    for f in man['pliki']:                                                     # dane muszą być tymi, które przeszły walidację
        if hashlib.sha256((D / f['plik']).read_bytes()).hexdigest() != f['sha256']:
            sys.exit(f'nfz-dane: zła suma SHA-256 dla {f["plik"]} – uruchom scripts/waliduj_nfz.py')
    zr = {s['id']: s['tytul'] for s in src['zrodla']}
    icd10 = {d['kod']: {'n': d['nazwa_pl_robocza'], 'robocza': True, 'status': d['status']} for d in dg['diagnozy']}
    sug = {}
    for m in mp['mapowania']:                                                  # tylko podpowiedzi (D3=A) – nigdy wymagane ani blokujące
        if m['icd10'] == 'NIE DOTYCZY' or m['wymagane_przez_nfz'] or m['poziom_kontroli'] != 'INFORMACJA': continue
        sug.setdefault(m['icd9'], []).append({'k': m['icd10'], 'u': m.get('uwagi', '')})
    reguly = []
    for r in rules['reguly']:
        poziom = r['poziom']
        if r['status'] == 'WYMAGA WERYFIKACJI': poziom = 'INFORMACJA'           # D4=A: nigdy powyżej informacji
        reguly.append({'id': r['id'], 'obszar': r['obszar'], 'poziom': poziom, 'status': r['status'], 'od': r['obowiazuje_od'],
                       'do': r.get('obowiazuje_do'), 'dotyczy': r['dotyczy'], 'wyzwalacz': r['wyzwalacz'], 'tresc': r['tresc'],
                       'zrodla': [zr.get(z, z) for z in r['zrodla']]})
    return {'wersja': man['wersja'], 'stan_prawny_na': man['stan_prawny_na'],
            'uwaga': 'Dane audytu NFZ (docs/nfz/). Nazwy ICD-10 robocze – do porównania z Tomem I CeZ. Mapowania ICD-9→ICD-10 to podpowiedzi, wybiera lekarz.',
            'reguly': reguly, 'limity': lim['limity'], 'laczenie': lim['laczenie'], 'zasada_laczenia': lim['zasada_domyslna'],
            'icd10': icd10, 'podpowiedzi_icd10': sug}


def zapisz():
    dane = zbuduj()
    js = ('/* Wygenerowane przez scripts/nfz_dane_przegladarka.py z data/nfz/ (wersja ' + dane['wersja'] + ') – NIE EDYTUJ RĘCZNIE.\n'
          '   Kody aplikacji: pakiety „ST…” jak w zarządzeniu, świadczenia jednostkowe bez prefiksu „23.” (np. 1006 = ICD-9 23.1006). */\n'
          'window.NFZ_DANE=Object.freeze(' + json.dumps(dane, ensure_ascii=False, separators=(',', ':')) + ');\n')
    OUT.write_text(js, encoding='utf-8')
    return dane


if __name__ == '__main__':
    d = zapisz()
    print(f'nfz-dane.js: wersja {d["wersja"]}, reguł {len(d["reguly"])}, ICD-10 {len(d["icd10"])}, procedur z podpowiedziami {len(d["podpowiedzi_icd10"])}')
