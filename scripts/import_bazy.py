# -*- coding: utf-8 -*-
"""Bezpieczny import bazy stomatologicznej – PRZYGOTOWANIE (etap 7.6). Nie zmienia danych aplikacji ani bazy PostgreSQL.

  python3 scripts/import_bazy.py                     # walidacja + raport: co jest gotowe do importu
  python3 scripts/import_bazy.py --porownaj <ref>    # różnice względem wersji z gita (np. main, HEAD~1, tag): nowe / zmienione / usunięte rekordy
  python3 scripts/import_bazy.py --pakiet <plik>     # zapisuje pakiet importu (JSON) tylko z rekordów draft/verified – do przyszłej integracji

Zasady (do przyszłej integracji z aplikacją):
- rekordy identyfikowane wyłącznie po stałych id (BAD-…, PROC-23.…, POLE-…, KROK-…, MAT-…, SZAB-…, CHK-…; mapowanie = procedura+icd10),
- import = upsert po id; rekordy nieobecne w nowej wersji NIE są usuwane automatycznie (raport „usunięte” do decyzji),
- poprzedni stan odtwarzalny z gita (każda wersja danych = commit + manifest z sumami SHA-256),
- import wstrzymany, gdy walidator zgłasza błędy."""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZBIORY = [  # plik, klucz listy, funkcja id
    ('data/badania/examinations.json', 'badania', lambda r: r['id']), ('data/badania/examination-fields.json', 'pola', lambda r: r['id']),
    ('data/badania/examination-templates.json', 'szablony', lambda r: r['id']), ('data/baza-stomatologiczna/pola-wspolne.json', 'pola', lambda r: r['id']),
    ('data/baza-stomatologiczna/zrodla-kliniczne.json', 'zrodla', lambda r: r['id']), ('data/procedury-icd9/procedures.json', 'procedury', lambda r: r['id']),
    ('data/procedury-icd9/procedure-steps.json', 'kroki', lambda r: r['id']), ('data/procedury-icd9/procedure-materials.json', 'materialy', lambda r: r['id']),
    ('data/procedury-icd9/procedure-templates.json', 'szablony', lambda r: r['id']), ('data/procedury-icd9/procedure-checklists.json', 'checklisty', lambda r: r['procedura']),
    ('data/procedury-icd9/procedure-diagnosis-mappings.json', 'mapowania', lambda r: r['procedura'] + '→' + r['icd10'])]

def wczytaj(plik, ref=None):
    if ref:
        r = subprocess.run(['git', 'show', f'{ref}:{plik}'], cwd=ROOT, capture_output=True, text=True)
        return json.loads(r.stdout) if r.returncode == 0 else None
    return json.loads((ROOT / plik).read_text(encoding='utf-8'))

def main():
    w = subprocess.run([sys.executable, '-I', str(ROOT / 'scripts' / 'waliduj_baze.py')], capture_output=True, text=True)
    ok = w.returncode == 0
    print('Walidacja:', w.stdout.strip().splitlines()[-1] if w.stdout else 'brak wyniku')
    if not ok:
        print(w.stdout); print('IMPORT WSTRZYMANY – popraw błędy walidacji.'); sys.exit(1)
    if '--porownaj' in sys.argv:
        ref = sys.argv[sys.argv.index('--porownaj') + 1]
        print(f'\nRóżnice względem {ref}:')
        for plik, k, fid in ZBIORY:
            nowy = {fid(r): r for r in wczytaj(plik)[k]}
            st = wczytaj(plik, ref); stary = {fid(r): r for r in st[k]} if st else {}
            dod = sorted(set(nowy) - set(stary)); usu = sorted(set(stary) - set(nowy)); zm = sorted(i for i in set(nowy) & set(stary) if nowy[i] != stary[i])
            if dod or usu or zm:
                print(f'- {plik}: nowe {len(dod)}, zmienione {len(zm)}, usunięte {len(usu)}' + (f' (usunięte – DO DECYZJI, import ich nie kasuje: {", ".join(usu[:10])})' if usu else ''))
    proc = wczytaj('data/procedury-icd9/procedures.json')['procedury']
    gotowe = [p['id'] for p in proc if p['status'] in ('draft', 'verified')]
    print(f'\nGotowe do importu (draft + verified): {len(gotowe)} kart procedur; verified: {sum(p["status"] == "verified" for p in proc)}; badania: {len(wczytaj("data/badania/examinations.json")["badania"])}.')
    print('Uwaga: draft = niezweryfikowane przez Patryka – w aplikacji oznaczyć jako „do weryfikacji”.')
    if '--pakiet' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--pakiet') + 1])
        man = wczytaj('data/baza-stomatologiczna/manifest.json')
        pak = {'wersja': man['wersja'], 'manifest': man, 'dane': {plik: wczytaj(plik) for plik, _, _ in ZBIORY}}
        pak['dane']['data/procedury-icd9/procedures.json'] = {**pak['dane']['data/procedury-icd9/procedures.json'], 'procedury': [p for p in proc if p['status'] in ('draft', 'verified')]}
        out.write_text(json.dumps(pak, ensure_ascii=False), encoding='utf-8')
        print(f'Pakiet importu zapisany: {out} (bez kart not_started).')

main()
