# Przenosi generator Opisów NFZ z obecnej aplikacji (repo opisy-nfz) do wersji SaaS.
# Logika i teksty bez zmian; nakładane są tylko poprawki z listy PATCHES (każda opisana). Wynik: generator/nfz.html,
# generator/szablony.js, generator/wspolne.css. Użycie: python3 tests/tools/przenies_generator.py <ścieżka do opisy-nfz>
# Skrypt kończy się błędem, jeśli którakolwiek poprawka nie pasuje dokładnie raz (zmiana w oryginale = świadoma decyzja).
import os, shutil, subprocess, sys

OLD = os.path.abspath(sys.argv[1])
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'generator')
commit = subprocess.run(['git', '-C', OLD, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

PATCHES = [
  ('P1 czcionki lokalnie zamiast Google Fonts (prywatność: brak wysyłania IP do Google; CSP tylko własne zasoby)',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('P2 tytuł strony w aplikacji Gabinet',
   '<title>Generator opisów NFZ</title>', '<title>Opisy NFZ – Gabinet</title>'),
  ('P3 bez manifestu i ikon wersji statycznej (aplikacja SaaS ma własne)',
   '<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n', ''),
  ('P4 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('P5 wspolne.js (sejf lokalny z hasłem) → gabinet-saas.js (konto SaaS: klucz urządzenia, synchronizacja danych bez treści opisów); dane startowe wstawia serwer w miejsce znacznika',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('P6 szablony.js z zasobów chronionych logowaniem',
   '<script src="szablony.js?v=2026-11-15-10"></script>', '<script src="/opisy-nfz/zasoby/szablony.js"></script>'),
  ('P7 identyfikator gabinetu: UUID z bazy (36 znaków) zamiast „c1”…„c24” z Kalendarza',
   "gab:typeof x.gab==='string'&&/^[A-Za-z0-9_-]{1,24}$/.test(x.gab)?x.gab:''};",
   "gab:typeof x.gab==='string'&&/^[A-Za-z0-9_-]{1,40}$/.test(x.gab)?x.gab:''};"),
]

src = open(os.path.join(OLD, 'nfz.html'), encoding='utf-8').read()
for name, old, new in PATCHES:
    n = src.count(old)
    if n != 1: sys.exit(f'Poprawka „{name}” pasuje {n} razy (oczekiwano 1) – sprawdź zmiany w opisy-nfz/nfz.html')
    src = src.replace(old, new)
head = f'<!-- Gabinet SaaS: generator przeniesiony z opisy-nfz@{commit} (nfz.html) przez tests/tools/przenies_generator.py; poprawki: generator/ZMIANY.md -->\n'
open(os.path.join(OUT, 'nfz.html'), 'w', encoding='utf-8').write(head + src)
shutil.copy(os.path.join(OLD, 'szablony.js'), os.path.join(OUT, 'szablony.js'))
shutil.copy(os.path.join(OLD, 'wspolne.css'), os.path.join(OUT, 'wspolne.css'))
with open(os.path.join(OUT, 'ZMIANY.md'), 'w', encoding='utf-8') as f:
    f.write(f'# Generator Opisów NFZ – zmiany względem obecnej aplikacji\n\nŹródło: repo `opisy-nfz`, commit `{commit}` – pliki `nfz.html`, `szablony.js`, `wspolne.css` (logika, pytania, reguły NFZ i teksty bez zmian).\n'
            'Plik `wspolne.js` (sejf z hasłem w przeglądarce) zastąpiony przez `gabinet-saas.js`.\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
print(f'generator przeniesiony z opisy-nfz@{commit}: {len(PATCHES)} poprawek')
