# -*- coding: utf-8 -*-
"""Walidacja bazy stomatologicznej (katalog badań + karty procedur ICD-9).
Uruchom z katalogu głównego repo:  python3 scripts/waliduj_baze.py  [--manifest  – przelicza sumy SHA-256 w manifeście]
Zależy od danych audytu NFZ (data/nfz/) – najpierw python3 scripts/waliduj_nfz.py.
Błąd = dane nie nadają się do importu. Ostrzeżenie = do uzupełnienia, import możliwy."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B, BAD, PR, NFZ = ROOT / 'data' / 'baza-stomatologiczna', ROOT / 'data' / 'badania', ROOT / 'data' / 'procedury-icd9', ROOT / 'data' / 'nfz'
bledy, ostrz = [], []
J = lambda p: json.loads(p.read_text(encoding='utf-8'))

PLIKI = [  # plik, schemat, klucz listy
    (B / 'zrodla-kliniczne.json', 'zrodla-kliniczne', 'zrodla'), (B / 'pola-wspolne.json', 'pola', 'pola'),
    (BAD / 'examinations.json', 'examinations', 'badania'), (BAD / 'examination-fields.json', 'pola', 'pola'),
    (BAD / 'examination-templates.json', 'szablony', 'szablony'),
    (PR / 'procedures.json', 'procedures', 'procedury'), (PR / 'procedure-steps.json', 'procedure-steps', 'kroki'),
    (PR / 'procedure-materials.json', 'procedure-materials', 'materialy'), (PR / 'procedure-templates.json', 'szablony', 'szablony'),
    (PR / 'procedure-checklists.json', 'procedure-checklists', 'checklisty'), (PR / 'procedure-diagnosis-mappings.json', 'procedure-diagnosis-mappings', 'mapowania')]
D = {}
for p, sch, k in PLIKI:
    try: D[p.name] = J(p)
    except Exception as e: bledy.append(f'{p.relative_to(ROOT)}: nie da się odczytać JSON ({e})'); D[p.name] = {k: []}

# 1. Schematy
try:
    import jsonschema
    for p, sch, k in PLIKI:
        s = J(B / 'schemas' / f'{sch}.schema.json')
        for e in jsonschema.Draft202012Validator(s, format_checker=jsonschema.FormatChecker()).iter_errors(D[p.name]):
            bledy.append(f'[schemat {p.name}] {"/".join(map(str, e.absolute_path))}: {e.message[:180]}')
except ImportError:
    ostrz.append('Brak modułu jsonschema – pominięto walidację schematów (pip install jsonschema).')

L = lambda n, k: D[n].get(k, [])
def ids(lista, nazwa):
    seen = set()
    for r in lista:
        if r['id'] in seen: bledy.append(f'{nazwa}: zduplikowany identyfikator {r["id"]}')
        seen.add(r['id'])
    return seen

# 2. Słowniki i źródła
nfz_src = {s['id']: s for s in J(NFZ / 'sources.json')['zrodla']}
klin = {s['id']: s for s in L('zrodla-kliniczne.json', 'zrodla')}; ids(L('zrodla-kliniczne.json', 'zrodla'), 'źródła kliniczne')
ZR = {**nfz_src, **klin}
slownik = {x['kod']: x for x in J(NFZ / 'procedures.json')['slownik_icd9_591']}
icd10 = {d['kod'] for d in J(NFZ / 'diagnoses.json')['diagnozy']}
reguly = {r['id'] for r in J(NFZ / 'billing-rules.json')['reguly']}
pary_audytu = {(m['icd9'], m['icd10']) for m in J(NFZ / 'procedure-diagnosis-mappings.json')['mapowania']}
pola = {}
for n in ('pola-wspolne.json', 'examination-fields.json'):
    for f in L(n, 'pola'):
        if f['id'] in pola: bledy.append(f'pola: zduplikowany identyfikator {f["id"]}')
        pola[f['id']] = f
kroki = ids(L('procedure-steps.json', 'kroki'), 'kroki'); mat = ids(L('procedure-materials.json', 'materialy'), 'materiały')
badania = {b['id']: b for b in L('examinations.json', 'badania')}; ids(L('examinations.json', 'badania'), 'badania')
procs = {p['id']: p for p in L('procedures.json', 'procedury')}; ids(L('procedures.json', 'procedury'), 'procedury')

def src_ok(lst, gdzie):
    for z in lst or []:
        if z not in ZR: bledy.append(f'{gdzie}: nieznane źródło {z}')
def poz_ok(lst, gdzie):
    for p in lst or []:
        src_ok(p.get('zrodla'), gdzie)
        if p['podstawa'] in ('wymaganie_prawne', 'wymaganie_nfz') and not p.get('zrodla'):
            bledy.append(f'{gdzie}: „{p["tekst"][:50]}” – wymaganie prawne/NFZ bez źródła')

# 3. Rejestr procedur – każdy kod-procedura ze słownika ma rekord
prod = J(NFZ / 'products.json'); gw = J(NFZ / 'procedures.json')['swiadczenia_gwarantowane']
uzywane = {x['kod_icd9'] for x in gw if x['kod_icd9']} | {x['kod_icd9'] for x in prod['jednostkowe_zal_1b']}
for x in prod['pakiety_zal_1c_1d']: uzywane |= set((x.get('sklad') or {}).get('kierunkowa') or [])
for k, x in slownik.items():
    if (not x.get('ma_podkody') or k in uzywane) and 'PROC-' + k not in procs: bledy.append(f'rejestr: brak rekordu dla procedury {k} ({x["nazwa"][:50]})')
SEKCJE = ['nazwa_krotka', 'opis', 'cel', 'kwalifikacja', 'przygotowanie', 'kroki', 'materialy', 'kontrola_efektu', 'zalecenia', 'dokumentacja', 'nfz', 'zrodla']
szab = L('procedure-templates.json', 'szablony') + L('examination-templates.json', 'szablony')
szab_dla = {}
for s in szab: szab_dla.setdefault(s['dotyczy'], set()).add(s['wariant'])
chk_dla = {c['procedura'] for c in L('procedure-checklists.json', 'checklisty')}
wspolne_chk = {e['id']: e for e in D['procedure-checklists.json'].get('wspolne', [])}
for p in procs.values():
    g = p['id']
    if p['kod'] not in slownik: bledy.append(f'{g}: kodu nie ma w ICD-9 PL 5.91')
    elif p['nazwa_oficjalna'] != slownik[p['kod']]['nazwa']: bledy.append(f'{g}: nazwa oficjalna różni się od słownika ICD-9 PL 5.91')
    src_ok(p.get('zrodla'), g); src_ok(p.get('zrodla_kodu'), g)
    if p['status'] in ('draft', 'verified', 'requires_expert_review'):
        for s in SEKCJE:
            if s not in p: bledy.append(f'{g}: status {p["status"]}, a brak sekcji „{s}”')
        brak = {'standardowy', 'skrocony', 'rozszerzony'} - szab_dla.get(g, set())
        if brak: bledy.append(f'{g}: brak szablonów opisu: {", ".join(sorted(brak))}')
        if g not in chk_dla: bledy.append(f'{g}: brak checklisty kompletności')
        if not any(m['procedura'] == g for m in L('procedure-diagnosis-mappings.json', 'mapowania')) and p['kategoria'] not in ('znieczulenie', 'radiologia'):
            ostrz.append(f'{g}: brak powiązań z ICD-10')
    if p['status'] == 'verified' and (not p.get('zweryfikowal') or not p.get('zweryfikowano') or not p.get('zrodla')): bledy.append(f'{g}: verified bez osoby weryfikującej, daty lub źródeł')
    if p['status'] == 'not_started' and not p.get('uzasadnienie_statusu'): bledy.append(f'{g}: not_started bez uzasadnienia')
    for k in p.get('kroki', []):
        if k['krok'] not in kroki: bledy.append(f'{g}: nieznany krok {k["krok"]}')
    for m in p.get('materialy', []):
        if m['mat'] not in mat: bledy.append(f'{g}: nieznany materiał {m["mat"]}')
    if 'dokumentacja' in p: poz_ok(p['dokumentacja']['elementy'], g + ' dokumentacja')
    n = p.get('nfz') or {}
    src_ok(n.get('zrodla'), g + ' NFZ')
    for r in n.get('reguly', []):
        if r not in reguly: bledy.append(f'{g}: nieznana reguła NFZ {r}')
    if n.get('swiadczenie_gwarantowane') == 'tak' and not n.get('zrodla'): bledy.append(f'{g}: „świadczenie gwarantowane” bez źródła')

# 4. Badania
for b in badania.values():
    g = b['id']; src_ok(b['zrodla'], g)
    if b['status'] == 'verified' and (not b.get('zweryfikowal') or not b.get('zweryfikowano')): bledy.append(f'{g}: verified bez osoby weryfikującej lub daty')
    for s in ('niezbedne', 'zalecane', 'sytuacyjne'): poz_ok(b['dokumentacja'][s], g + ' dokumentacja')
    for e in b['elementy_oceny']:
        if e.get('pole') and e['pole'] not in pola: bledy.append(f'{g}: nieznane pole {e["pole"]}')
    for x in b['powiazania']['icd9']:
        if x['kod'] not in slownik: bledy.append(f'{g}: ICD-9 {x["kod"]} spoza słownika')
    for x in b['powiazania']['icd10']:
        if x['kod'] not in icd10: bledy.append(f'{g}: ICD-10 {x["kod"]} spoza diagnoses.json')
    for r in b['powiazania'].get('reguly_nfz', []):
        if r not in reguly: bledy.append(f'{g}: nieznana reguła NFZ {r}')
    brak = {'standardowy', 'skrocony', 'rozszerzony'} - szab_dla.get(g, set())
    if brak and b['status'] != 'not_started': bledy.append(f'{g}: brak szablonów opisu: {", ".join(sorted(brak))}')
for f in pola.values():
    if f.get('badanie') and f['badanie'] not in badania: bledy.append(f'pole {f["id"]}: nieznane badanie {f["badanie"]}')
    src_ok(f.get('zrodla'), f['id'])

# 5. Szablony – pola w tekście = lista pól; bez wpisanych z góry wyników
ids(szab, 'szablony')
for s in szab:
    w = set(re.findall(r'\{\{(POLE-[A-Z0-9-]+)\}\}', s['tekst']))
    if w != set(s['pola']): bledy.append(f'{s["id"]}: pola w tekście ≠ lista pól ({sorted(w ^ set(s["pola"]))})')
    for f in w:
        if f not in pola: bledy.append(f'{s["id"]}: nieznane pole {f}')
    if s['dotyczy'] not in procs and s['dotyczy'] not in badania: bledy.append(f'{s["id"]}: dotyczy nieznanego rekordu {s["dotyczy"]}')
    bez_pol = re.sub(r'\{\{POLE-[A-Z0-9-]+\}\}', '', s['tekst']).lower()
    for fr in ('bez zmian patologicznych', 'bez powikłań', 'prawidłow', 'nie stwierdzono'):
        if fr in bez_pol: ostrz.append(f'{s["id"]}: tekst zawiera stały wynik „{fr}” – wynik powinien pochodzić z pola wypełnianego przez lekarza')

# 6. Checklisty – obowiązkowe tylko z podstawą prawną/NFZ i źródłem
for e in wspolne_chk.values():
    poz_ok([e], e['id'])
    if e['poziom'] == 'obowiazkowe' and e['podstawa'] not in ('wymaganie_prawne', 'wymaganie_nfz'): bledy.append(f'{e["id"]}: obowiązkowe bez podstawy prawnej/NFZ')
seen = set()
for c in L('procedure-checklists.json', 'checklisty'):
    if c['procedura'] not in procs: bledy.append(f'checklista: nieznana procedura {c["procedura"]}')
    for w in c.get('wspolne', []):
        if w not in wspolne_chk: bledy.append(f'checklista {c["procedura"]}: nieznany element wspólny {w}')
    for e in c['elementy']:
        if e['id'] in seen or e['id'] in wspolne_chk: bledy.append(f'checklista: zduplikowany element {e["id"]}')
        seen.add(e['id']); poz_ok([e], e['id'])
        if e['poziom'] == 'obowiazkowe' and e['podstawa'] not in ('wymaganie_prawne', 'wymaganie_nfz'):
            bledy.append(f'{e["id"]}: element obowiązkowy bez podstawy prawnej/NFZ (nieuzasadnione wymaganie)')
        if e.get('pole') and e['pole'] not in pola: bledy.append(f'{e["id"]}: nieznane pole {e["pole"]}')
        for z in e.get('zrodla', []):
            if e['poziom'] == 'obowiazkowe' and ZR.get(z, {}).get('status', '').startswith('WYMAGA'):
                ostrz.append(f'{e["id"]}: element obowiązkowy oparty na źródle „wymaga weryfikacji” ({z})')

# 7. Mapowania ICD-9 → ICD-10
para = set()
for m in L('procedure-diagnosis-mappings.json', 'mapowania'):
    g = f'mapowanie {m["procedura"]}→{m["icd10"]}'
    if (m['procedura'], m['icd10']) in para: bledy.append(f'{g}: duplikat')
    para.add((m['procedura'], m['icd10']))
    if m['procedura'] not in procs: bledy.append(f'{g}: nieznana procedura')
    if m['icd10'] not in icd10: bledy.append(f'{g}: ICD-10 spoza diagnoses.json')
    src_ok(m.get('zrodla'), g)
    if m['potwierdzenie'] == 'zrodlo' and not m.get('zrodla'): bledy.append(f'{g}: „potwierdzone źródłem” bez źródła')
    kod = m['procedura'][5:]
    w = (kod, m['icd10']) in pary_audytu
    if m.get('w_audycie_nfz') is not None and m['w_audycie_nfz'] != w: bledy.append(f'{g}: w_audycie_nfz={m["w_audycie_nfz"]}, a w audycie {w}')

# 8. Manifest – sumy kontrolne
man_p = B / 'manifest.json'
if '--manifest' in sys.argv and not bledy:
    man = J(man_p) if man_p.exists() else {'nazwa': 'baza-stomatologiczna', 'wersja': '2026.11.22-1', 'zalezy_od': 'data/nfz (audyt NFZ)'}
    man['pliki'] = [{'plik': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'schemat': f'data/baza-stomatologiczna/schemas/{s}.schema.json', 'rekordy': len(D[p.name].get(k, []))} for p, s, k in PLIKI]
    st = {}
    for p in procs.values(): st[p['status']] = st.get(p['status'], 0) + 1
    man['liczniki'] = {'badania': len(badania), 'procedury': len(procs), 'procedury_wg_statusu': st, 'szablony': len(szab), 'pola': len(pola), 'kroki': len(kroki), 'materialy': len(mat), 'mapowania_icd10': len(para)}
    man_p.write_text(json.dumps(man, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('manifest zaktualizowany')
elif man_p.exists():
    for f in J(man_p)['pliki']:
        if hashlib.sha256((ROOT / f['plik']).read_bytes()).hexdigest() != f['sha256']: bledy.append(f'manifest: zła suma SHA-256 dla {f["plik"]} (uruchom z --manifest po zmianach)')
else: ostrz.append('brak manifestu – uruchom z --manifest')

st = {}
for p in procs.values(): st[p['status']] = st.get(p['status'], 0) + 1
print(f'Badania: {len(badania)} | Procedury: {len(procs)} {st} | Szablony: {len(szab)} | Pola: {len(pola)} | Kroki: {len(kroki)} | Materiały: {len(mat)} | Mapowania ICD-10: {len(para)}')
for o in ostrz: print('OSTRZEŻENIE:', o)
for b in bledy: print('BŁĄD:', b)
print('WYNIK:', 'OK' if not bledy else f'{len(bledy)} błędów')
sys.exit(1 if bledy else 0)
