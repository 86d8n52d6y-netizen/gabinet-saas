# -*- coding: utf-8 -*-
"""Opis z karty procedury (etap I2, decyzja Patryka 22.11.2026): dane dla przeglądarki → generator/karty-opisy.js.

Tylko karty i badania zweryfikowane przez Patryka (status `verified`) – szablony opisów (standardowy / skrócony / rozszerzony),
definicje pól użytych w szablonach i podpowiedzi ICD-10 (wybiera lekarz, nigdy automatycznie). Bez danych pacjentów.
Plik ładowany po zalogowaniu (ASSETS w src/lib/nfz/generator.ts); składanie opisu: generator/opis-z-karty.js.

    python3 scripts/karty_opisy_przegladarka.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'generator' / 'karty-opisy.js'
J = lambda *p: json.loads((ROOT / 'data').joinpath(*p).read_text(encoding='utf-8'))
WARIANTY = ('standardowy', 'skrocony', 'rozszerzony')


def norma(t):
    """Przykład wyniku prawidłowego do przycisku „w normie”: bez dopisków redakcyjnych w nawiasie („(Przykład – wpisuje lekarz.)”),
    a dla badań bez wyniku prawidłowego („Nie dotyczy…”, zestawienie badań składowych) – pusty (przycisk ukryty)."""
    t = re.sub(r'\s*\((Przykład|Wpisuje)[^()]*\)\s*$', '', t.strip())
    return '' if t.startswith(('Nie dotyczy', 'Zestawienie')) else t


def zbuduj():
    proc = J('procedury-icd9', 'procedures.json')['procedury']
    szab = J('procedury-icd9', 'procedure-templates.json')['szablony']
    mapy = J('procedury-icd9', 'procedure-diagnosis-mappings.json')['mapowania']
    pola = {p['id']: p for p in J('baza-stomatologiczna', 'pola-wspolne.json')['pola'] + J('badania', 'examination-fields.json')['pola']}
    icd = {d['kod']: d['nazwa_pl_robocza'] for d in J('nfz', 'diagnoses.json')['diagnozy']}
    man = J('baza-stomatologiczna', 'manifest.json')
    karty, uzyte = [], set()
    for p in proc:
        if p['status'] != 'verified':
            continue
        sz = {s['wariant']: s for s in szab if s['dotyczy'] == p['id']}
        if not all(w in sz for w in WARIANTY):
            continue
        for s in sz.values():
            uzyte.update(s['pola'])
        rozp = [[m['icd10'], icd.get(m['icd10'], ''), m.get('okolicznosci', '')] for m in mapy if m['procedura'] == p['id']]
        karty.append({'id': p['id'], 'kod': p['kod'], 'nazwa': p.get('nazwa_krotka') or p['nazwa_oficjalna'], 'kategoria': p['kategoria'],
                      'nfz': (p.get('nfz') or {}).get('swiadczenie_gwarantowane') == 'tak',
                      'szablony': {w: sz[w]['tekst'] for w in WARIANTY}, 'icd10': rozp})
    # badania (etap D – wybór elementów badania, decyzja Patryka 22.11.2026): zweryfikowane, z szablonami i przykładem wyniku prawidłowego
    sb = J('badania', 'examination-templates.json')['szablony']
    badania = []
    for b in J('badania', 'examinations.json')['badania']:
        if b['status'] != 'verified':
            continue
        sz = {s['wariant']: s for s in sb if s['dotyczy'] == b['id']}
        if not all(w in sz for w in WARIANTY):
            continue
        for s in sz.values():
            uzyte.update(s['pola'])
        badania.append({'id': b['id'], 'nazwa': b['nazwa_krotka'], 'pelna': b['nazwa'], 'szablony': {w: sz[w]['tekst'] for w in WARIANTY},
                        'norma': norma(b.get('wynik_prawidlowy') or '')})
    brak = sorted(f for f in uzyte if f not in pola)
    if brak:
        raise SystemExit(f'Pola użyte w szablonach bez definicji: {brak}')
    defs = {f: {'e': pola[f]['etykieta'], 't': pola[f]['typ'], **({'o': pola[f]['opcje']} if pola[f].get('opcje') else {})} for f in sorted(uzyte)}
    return {'wersja': str(man['wersja']), 'karty': karty, 'badania': badania, 'pola': defs}


def zapisz():
    d = zbuduj()
    OUT.write_text('/* Wygenerowane przez scripts/karty_opisy_przegladarka.py z data/ (baza stomatologiczna ' + d['wersja'] + ') – NIE EDYTUJ RĘCZNIE.\n'
                   '   Tylko karty zweryfikowane przez Patryka; bez danych pacjentów. */\n'
                   'window.KARTY_OPISY=Object.freeze(' + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + ');\n', encoding='utf-8')
    return d


if __name__ == '__main__':
    d = zapisz()
    print(f'karty-opisy.js: wersja {d["wersja"]}, kart {len(d["karty"])}, badań {len(d["badania"])}, pól {len(d["pola"])}, {OUT.stat().st_size // 1024} KB')
