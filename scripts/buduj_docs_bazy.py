# -*- coding: utf-8 -*-
"""Dokumentacja bazy stomatologicznej generowana z danych JSON (nie edytuj plików .md ręcznie):
docs/badania/OPISY_BADAN.md, docs/badania/STRUKTURA_POL.md, docs/procedury-icd9/KARTY_PROCEDUR.md, docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md.
Uruchom:  python3 scripts/buduj_docs_bazy.py   (po python3 scripts/waliduj_baze.py)"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = lambda p: json.loads((ROOT / p).read_text(encoding='utf-8'))
NAG = '> Plik generowany: `python3 scripts/buduj_docs_bazy.py` z danych w `data/`. Nie edytuj ręcznie – popraw JSON.\n\n'
man = J('data/baza-stomatologiczna/manifest.json')
zr = {s['id']: s for s in J('data/nfz/sources.json')['zrodla']} | {s['id']: s for s in J('data/baza-stomatologiczna/zrodla-kliniczne.json')['zrodla']}
pola = {p['id']: p for p in J('data/baza-stomatologiczna/pola-wspolne.json')['pola'] + J('data/badania/examination-fields.json')['pola']}
kroki = {k['id']: k for k in J('data/procedury-icd9/procedure-steps.json')['kroki']}
mat = {m['id']: m for m in J('data/procedury-icd9/procedure-materials.json')['materialy']}
szab = J('data/badania/examination-templates.json')['szablony'] + J('data/procedury-icd9/procedure-templates.json')['szablony']
chk = J('data/procedury-icd9/procedure-checklists.json'); wsp = {e['id']: e for e in chk['wspolne']}
chk_dla = {c['procedura']: c for c in chk['checklisty']}
mapy = J('data/procedury-icd9/procedure-diagnosis-mappings.json')['mapowania']
diag = {d['kod']: d['nazwa_pl_robocza'] for d in J('data/nfz/diagnoses.json')['diagnozy']}
PODST = {'wymaganie_prawne': 'prawne', 'wymaganie_nfz': 'NFZ', 'zalecenie_kliniczne': 'zalecenie kliniczne', 'propozycja_aplikacji': 'propozycja aplikacji'}

def zrodla(lst): return '; '.join(f'`{z}`' + (f' (PMID {zr[z]["pmid"]})' if zr.get(z, {}).get('pmid') else '') for z in lst or [])
def poz(lst): return '\n'.join(f'- {p["tekst"]} — *{PODST[p["podstawa"]]}*' + (f', warunek: {p["warunek"]}' if p.get('warunek') else '') + (f' ({zrodla(p.get("zrodla"))})' if p.get('zrodla') else '') for p in lst) or '- —'
def tpl(dot): return '\n'.join(f'**{s["wariant"]}**\n\n> {s["tekst"]}\n' for s in szab if s['dotyczy'] == dot)

# ---- badania
bad = J('data/badania/examinations.json')['badania']
o = [f'# Katalog A – badania stomatologiczne\n\n{NAG}Wersja danych: {man["wersja"]}. Badań: {len(bad)}. Status każdego badania – w nagłówku. Wynik prawidłowy to **przykład opisu**, nigdy nie jest zaznaczany za lekarza.\n']
for b in bad:
    o.append(f'\n## {b["nazwa"]} (`{b["id"]}`)\n\nKrótko: **{b["nazwa_krotka"]}** · kategoria: {b["kategoria"]} · status: **{b["status"]}**\n')
    o.append(f'\n**Cel.** {b["cel"]["oceniane"]}\n\n- Informacje: ' + '; '.join(b['cel']['informacje']) + '\n- Wykrywa: ' + '; '.join(b['cel']['wykrywa']))
    o.append('\n\n**Wskazania** (' + ', '.join(b['wskazania']['charakter']) + '): ' + '; '.join(b['wskazania']['kiedy']) + ('. Szczególnie: ' + '; '.join(b['wskazania']['szczegolnie']) if b['wskazania'].get('szczegolnie') else ''))
    o.append('\n\n**Przebieg**\n\n' + '\n'.join(f'{i+1}. **{k["krok"]}** – {k["opis"]}' for i, k in enumerate(b['przebieg'])))
    o.append('\n\n**Elementy oceny**\n\n| Element | Co oceniamy | Pole |\n|---|---|---|\n' + '\n'.join(f'| {e["element"]} | {e["co"]} | {("`" + e["pole"] + "`") if e.get("pole") else "—"} |' for e in b['elementy_oceny']))
    o.append(f'\n\n**Przykład wyniku prawidłowego:** {b["wynik_prawidlowy"]}\n\n**Przykłady nieprawidłowości:** ' + '; '.join(b['nieprawidlowosci']))
    d = b['dokumentacja']
    o.append(f'\n\n**Dokumentacja – niezbędne**\n\n{poz(d["niezbedne"])}\n\n**Zalecane**\n\n{poz(d["zalecane"])}\n\n**Zależne od sytuacji**\n\n{poz(d["sytuacyjne"])}')
    p = b['powiazania']
    o.append('\n\n**Powiązania** – ICD-9: ' + ('; '.join(f'{x["kod"]} ({x["kiedy"]})' for x in p['icd9']) or '—') + ' · ICD-10: ' + ('; '.join(f'{x["kod"]} ({x["kiedy"]})' for x in p['icd10']) or '—') + (f' · reguły NFZ: {", ".join(p["reguly_nfz"])}' if p.get('reguly_nfz') else '') + (f'\n\n*{p["uwaga"]}*' if p.get('uwaga') else ''))
    o.append(f'\n\n**Szablony opisu**\n\n{tpl(b["id"])}\n**Źródła:** {zrodla(b["zrodla"])}' + (f'\n\n*Uwagi: {b["uwagi"]}*' if b.get('uwagi') else '') + '\n')
(ROOT / 'docs/badania/OPISY_BADAN.md').write_text(''.join(o), encoding='utf-8')

o = [f'# Pola formularzy (badania i procedury)\n\n{NAG}Typy: tekst, tekst_dlugi, wybor, wybor_wielokrotny (z możliwością własnej wartości), przelacznik, liczba, data, zab/zeby/powierzchnie (diagram FDI). Żadne pole nie jest wymagane do zapisu i żadne nie ma domyślnego wyniku.\n\n| Pole | Etykieta | Typ | Opcje | Badanie |\n|---|---|---|---|---|\n']
for p in pola.values():
    o.append(f'| `{p["id"]}` | {p["etykieta"]} | {p["typ"]}{" (" + p["jednostka"] + ")" if p.get("jednostka") else ""} | {"; ".join(p.get("opcje", [])) or "—"}{" + własna" if p.get("wlasna_wartosc") else ""} | {p.get("badanie", "wspólne")} |\n')
(ROOT / 'docs/badania/STRUKTURA_POL.md').write_text(''.join(o), encoding='utf-8')

# ---- procedury
proc = J('data/procedury-icd9/procedures.json')['procedury']
gotowe = [p for p in proc if p['status'] != 'not_started']
o = [f'# Katalog B – karty procedur ICD-9\n\n{NAG}Wersja danych: {man["wersja"]}. Kart opracowanych: {len(gotowe)} z {len(proc)} (rejestr: `REJESTR_KOMPLETNOSCI.md`). Wymagania NFZ są oddzielone od zaleceń klinicznych; elementy oznaczone podstawą i źródłem.\n']
for p in gotowe:
    o.append(f'\n## {p["kod"]} – {p["nazwa_oficjalna"]}\n\n`{p["id"]}` · **{p.get("nazwa_krotka", "")}** · {p["kategoria"]} · status: **{p["status"]}**' + (f' · kody w Opisach NFZ: {", ".join(p["kody_aplikacji"])}' if p.get('kody_aplikacji') else '') + f'\n\n{p.get("opis", "")}\n')
    c = p['cel']; o.append(f'\n**Na czym polega.** {c["na_czym_polega"]} **Cel:** {c["cel_kliniczny"]}' + (f' {c["kiedy"]}' if c.get('kiedy') else '') + '\n\nWskazania: ' + '; '.join(c['wskazania']))
    k = p['kwalifikacja']; o.append('\n\n**Kwalifikacja** – ocenić: ' + '; '.join(k['ocena_przed']) + '. Wywiad: ' + '; '.join(k['wywiad']) + '.\n\n' + '\n'.join(f'- przeciwwskazanie *{x["rodzaj"]}*: {x["tekst"]}' for x in k['przeciwwskazania']) + ('\n- dodatkowa diagnostyka: ' + '; '.join(k['dodatkowa_diagnostyka']) if k.get('dodatkowa_diagnostyka') else '') + ('\n- rozważ inne postępowanie: ' + '; '.join(k['inne_postepowanie']) if k.get('inne_postepowanie') else ''))
    pr = p['przygotowanie']; o.append('\n\n**Przygotowanie** – konieczne: ' + '; '.join(pr['konieczne']) + ('; opcjonalne: ' + '; '.join(pr['opcjonalne']) if pr.get('opcjonalne') else '') + ('; zależne od sytuacji: ' + '; '.join(pr['sytuacyjne']) if pr.get('sytuacyjne') else '') + (f'. Znieczulenie: {pr["znieczulenie"]}' if pr.get('znieczulenie') else ''))
    o.append('\n\n**Przebieg krok po kroku**\n\n' + '\n'.join(f'{i+1}. **{kroki[s["krok"]]["nazwa"]}** – {kroki[s["krok"]]["opis"]}' + (f' *Uwaga: {kroki[s["krok"]]["uwaga"]}*' if kroki[s['krok']].get('uwaga') else '') + (f' **W tej procedurze:** {s["uwaga"]}' if s.get('uwaga') else '') + (' Warianty: ' + '; '.join(kroki[s['krok']]['warianty']) + '.' if kroki[s['krok']].get('warianty') else '') for i, s in enumerate(p['kroki'])))
    o.append('\n\n**Materiały i narzędzia:** ' + '; '.join(f'{mat[m["mat"]]["nazwa"]} ({m.get("rola", "")})' for m in p['materialy']))
    ke = p['kontrola_efektu']; o.append('\n\n**Kontrola efektu:** ' + '; '.join(ke['sprawdzic']) + ('. Nieprawidłowości: ' + '; '.join(ke['nieprawidlowosci']) if ke.get('nieprawidlowosci') else '') + ('. Dalej: ' + '; '.join(ke['dalsze_postepowanie']) if ke.get('dalsze_postepowanie') else ''))
    z = p['zalecenia']; o.append('\n\n**Zalecenia pozabiegowe:** ' + ' '.join(f'{lab}: ' + '; '.join(z[key]) + '.' for key, lab in (('dla_pacjenta', 'Pacjent'), ('higiena', 'Higiena'), ('ograniczenia', 'Ograniczenia'), ('kontakt_gdy', 'Kontakt z gabinetem, gdy')) if z.get(key)) + (f' Kontrola: {z["kontrola"]}' if z.get('kontrola') else ''))
    o.append(f'\n\n**Dokumentacja**\n\n{poz(p["dokumentacja"]["elementy"])}')
    n = p['nfz']; o.append(f'\n\n**NFZ** – świadczenie gwarantowane: **{n["swiadczenie_gwarantowane"]}**' + ('; produkty: ' + '; '.join(n['produkty']) if n.get('produkty') else '') + ('\n\n' + '\n'.join('- ' + w for w in n['warunki']) if n.get('warunki') else '') + (f'\n\nReguły: {", ".join(n["reguly"])}' if n.get('reguly') else '') + (f'\n\n*{n["uwagi"]}*' if n.get('uwagi') else '') + (f'\n\nŹródła NFZ: {zrodla(n.get("zrodla"))}' if n.get('zrodla') else ''))
    m = [x for x in mapy if x['procedura'] == p['id']]
    if m: o.append('\n\n**ICD-10 (podpowiedzi, wybiera lekarz)**\n\n| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |\n|---|---|---|---|---|\n' + '\n'.join(f'| {x["icd10"]} | {diag.get(x["icd10"], "")} | {x["okolicznosci"]} | {x["potwierdzenie"]} | {"tak" if x.get("w_audycie_nfz") else "nie"} |' for x in m))
    c = chk_dla.get(p['id'])
    if c: o.append('\n\n**Checklista kompletności**\n\n' + '\n'.join(f'- [{wsp[w]["poziom"]}] {wsp[w]["tekst"]} — *{PODST[wsp[w]["podstawa"]]}*' for w in c.get('wspolne', [])) + ('\n' if c['elementy'] else '') + '\n'.join(f'- [{e["poziom"]}] {e["tekst"]} — *{PODST[e["podstawa"]]}*' + (f', {e["warunek"]}' if e.get('warunek') else '') for e in c['elementy']))
    o.append(f'\n\n**Szablony opisu**\n\n{tpl(p["id"])}\n**Źródła kliniczne:** {zrodla(p.get("zrodla"))}\n')
(ROOT / 'docs/procedury-icd9/KARTY_PROCEDUR.md').write_text(''.join(o), encoding='utf-8')

st = {}
for p in proc: st[p['status']] = st.get(p['status'], 0) + 1
o = [f'# Rejestr kompletności – procedury ICD-9 i badania\n\n{NAG}Wersja danych: {man["wersja"]}.\n\n## Podsumowanie\n\n| Status | Procedury |\n|---|---|\n' + '\n'.join(f'| {k} | {v} |' for k, v in sorted(st.items())) + f'\n| **razem** | **{len(proc)}** |\n\nBadania: {len(bad)} (' + ', '.join(f'{b["id"]}: {b["status"]}' for b in bad) + ').\n\n`draft` = opracowane, niezweryfikowane przez Patryka; `verified` – wyłącznie po weryfikacji (pole zweryfikowal).\n\n## Wszystkie kody\n\n| Kod | Nazwa (ICD-9 PL 5.91) | Kategoria | Status | Uwagi |\n|---|---|---|---|---|\n']
for p in proc: o.append(f'| {p["kod"]} | {p["nazwa_oficjalna"]} | {p["kategoria"]} | {p["status"]} | {p.get("uzasadnienie_statusu", "")} |\n')
(ROOT / 'docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md').write_text(''.join(o), encoding='utf-8')
print('docs: OPISY_BADAN.md, STRUKTURA_POL.md, KARTY_PROCEDUR.md, REJESTR_KOMPLETNOSCI.md')
