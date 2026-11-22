# -*- coding: utf-8 -*-
"""Baza stomatologiczna → generator/baza-dane.js (window.BAZA_DANE): checklisty kompletności kart dla kodów używanych w Opisach NFZ.
Tylko do odczytu na urządzeniu; nic nie wysyła. Nie edytuj generator/baza-dane.js ręcznie – popraw JSON w data/, uruchom
python3 scripts/waliduj_baze.py, potem python3 tests/tools/przenies_generator.py <opisy-nfz> (wywołuje ten skrypt) albo bezpośrednio ten skrypt."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'generator' / 'baza-dane.js'
J = lambda p: json.loads((ROOT / p).read_text(encoding='utf-8'))
POLA = ('tekst', 'poziom', 'podstawa', 'warunek', 'pole')


def zbuduj():
    man = J('data/baza-stomatologiczna/manifest.json')
    proc = {p['id']: p for p in J('data/procedury-icd9/procedures.json')['procedury']}
    ch = J('data/procedury-icd9/procedure-checklists.json')
    wsp = {e['id']: {k: e[k] for k in POLA if k in e} for e in ch['wspolne']}
    kody = {}
    for c in ch['checklisty']:
        p = proc[c['procedura']]
        for k in p.get('kody_aplikacji') or []:
            if k.startswith('04'):
                continue                                              # znieczulenia – w Opisach NFZ pola „do wyceny”, nie kody wizyty
            kody[k] = {'id': p['id'], 'kod': p['kod'], 'nazwa': p.get('nazwa_krotka') or p['nazwa_oficjalna'], 'status': p['status'],
                       'wspolne': c.get('wspolne', []), 'elementy': [{k2: e[k2] for k2 in POLA if k2 in e} for e in c['elementy']]}
    return {'wersja': man['wersja'], 'wspolne': wsp, 'kody': dict(sorted(kody.items()))}


def zapisz():
    d = zbuduj()
    OUT.write_text('/* Wygenerowane przez scripts/baza_dane_przegladarka.py z data/ (baza stomatologiczna ' + d['wersja'] + ') – NIE EDYTUJ RĘCZNIE. */\n'
                   'window.BAZA_DANE=Object.freeze(' + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + ');\n', encoding='utf-8')
    return d


if __name__ == '__main__':
    d = zapisz()
    print(f'baza-dane.js: wersja {d["wersja"]}, kody Opisów NFZ: {", ".join(d["kody"])}')
