# -*- coding: utf-8 -*-
"""Walidacja danych NFZ (data/nfz/*.json).
Uruchom z katalogu głównego repo:  python3 scripts/waliduj_nfz.py
Wymaga: pip install jsonschema  (gdy brak – pomija walidację schematów, robi resztę testów)."""
import json, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'data' / 'nfz'
bledy, ostrz = [], []
def L(p): return json.loads((D / p).read_text(encoding='utf-8'))

PLIKI = ['sources', 'procedures', 'products', 'diagnoses', 'procedure-diagnosis-mappings', 'billing-rules', 'limits-and-combinations', 'materials', 'manifest']
dane = {p: L(p + '.json') for p in PLIKI}

# 1. Schematy JSON
try:
    import jsonschema
    for p in PLIKI:
        sch = json.loads((D / 'schemas' / f'{p}.schema.json').read_text(encoding='utf-8'))
        for e in jsonschema.Draft202012Validator(sch).iter_errors(dane[p]):
            bledy.append(f'[schemat {p}] {"/".join(map(str, e.absolute_path))}: {e.message[:160]}')
except ImportError:
    ostrz.append('Brak modułu jsonschema – pominięto walidację schematów (pip install jsonschema).')

src = {s['id'] for s in dane['sources']['zrodla']}
icd9 = {x['kod'] for x in dane['procedures']['slownik_icd9_591']}
warianty = {w['kod_nfz'] for w in dane['procedures']['warianty_nfz_vs_icd9']}
koszyk_kody = {k['kod_icd9'] for k in dane['procedures']['swiadczenia_gwarantowane'] if k['kod_icd9']}
icd10 = {d['kod'] for d in dane['diagnoses']['diagnozy']}
reguly = {r['id']: r for r in dane['billing-rules']['reguly']}
pakiety = {p['id'] for p in dane['products']['pakiety_zal_1c_1d']}
POZA_ROZDZ = {'87.121'}  # pantomogram – rozdz. 87, poza słownikiem 23–24

# 2. Reguły
if len(reguly) != len(dane['billing-rules']['reguly']): bledy.append('Zduplikowane id reguł')
for r in reguly.values():
    for s in r['zrodla']:
        if s not in src: bledy.append(f'{r["id"]}: nieznane źródło {s}')
    if r['poziom'] == 'BLOKADA' and r['status'] != 'POTWIERDZONA':
        bledy.append(f'{r["id"]}: BLOKADA przy statusie {r["status"]} (niedozwolone – niepotwierdzona reguła nie może blokować)')
    if r['status'] == 'WYMAGA WERYFIKACJI' and r['poziom'] != 'INFORMACJA':
        bledy.append(f'{r["id"]}: reguła WYMAGA WERYFIKACJI powinna mieć poziom INFORMACJA')
    for k in r['dotyczy']:
        if k in ('ST1', 'ST2', 'ST3', 'ST4', 'ST5'): continue
        if k not in icd9 and k not in pakiety and k not in warianty and k not in POZA_ROZDZ and r['id'] != 'R-DOK-05':
            bledy.append(f'{r["id"]}: „dotyczy” zawiera nieznany kod {k}')
    for pole in ('wyzwalacz', 'tresc', 'obowiazuje_od'):
        if not str(r.get(pole, '')).strip(): bledy.append(f'{r["id"]}: puste pole {pole}')

# 3. Mapowania – kody muszą istnieć, nigdy nie są wymagane/blokujące
for m in dane['procedure-diagnosis-mappings']['mapowania']:
    if m['icd9'] not in icd9 and m['icd9'] not in warianty and m['icd9'] not in POZA_ROZDZ:
        bledy.append(f'mapowanie: ICD-9 {m["icd9"]} spoza słownika 5.91 i wariantów NFZ')
    if m['icd10'] != 'NIE DOTYCZY' and m['icd10'] not in icd10:
        bledy.append(f'mapowanie: ICD-10 {m["icd10"]} spoza diagnoses.json')
    if m['wymagane_przez_nfz'] or m['poziom_kontroli'] != 'INFORMACJA':
        bledy.append(f'mapowanie {m["icd9"]}->{m["icd10"]}: nie może być wymagane ani blokujące')

# 4. Łączenie
for c in dane['limits-and-combinations']['laczenie']:
    if c['regula'] not in reguly: bledy.append(f'łączenie {c["a"]}+{c["b"]}: brak reguły {c["regula"]}')
    if c['status'].startswith('NIEDOZWOLONE') and reguly.get(c['regula'], {}).get('status') != 'POTWIERDZONA':
        ostrz.append(f'łączenie {c["a"]}+{c["b"]} NIEDOZWOLONE oparte na regule niepotwierdzonej {c["regula"]}')

# 5. Produkty
for p in dane['products']['jednostkowe_zal_1b']:
    if p['kod_icd9'] not in icd9 and p['kod_icd9'] not in warianty and p['kod_icd9'] not in POZA_ROZDZ:
        bledy.append(f'1b {p["id"]}: kod {p["kod_icd9"]} spoza 5.91 i wariantów')
    if p['kod_produktu'] is None: ostrz.append(f'1b {p["id"]} ({p["kod_icd9"]}): brak kodu produktu NFZ')
kp = [p['kod_produktu'] for p in dane['products']['pakiety_zal_1c_1d']]
if len(kp) != len(set(kp)): bledy.append('pakiety: zduplikowane kody produktów')

# 6. Koszyk vs słownik
for k in koszyk_kody:
    if k not in icd9 and k not in warianty and k not in POZA_ROZDZ: bledy.append(f'koszyk: kod {k} spoza 5.91 i wariantów')
if '23.1513' in icd9: bledy.append('23.1513 pojawił się w słowniku – sprawdzić wersję ICD-9')

# 7. Manifest – sumy kontrolne
for f in dane['manifest']['pliki']:
    b = (D / f['plik']).read_bytes()
    if hashlib.sha256(b).hexdigest() != f['sha256']: bledy.append(f'manifest: zła suma SHA-256 dla {f["plik"]}')

print(f'Reguły: {len(reguly)} | Mapowania: {len(dane["procedure-diagnosis-mappings"]["mapowania"])} | ICD-9: {len(icd9)} | ICD-10: {len(icd10)}')
for o in ostrz: print('OSTRZEŻENIE:', o)
for b in bledy: print('BŁĄD:', b)
print('WYNIK:', 'OK' if not bledy else f'{len(bledy)} błędów')
sys.exit(1 if bledy else 0)
