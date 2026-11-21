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

PATCHES_PRYW = [
  ('R1 bez manifestu i ikon wersji statycznej',
   '<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n', ''),
  ('R2 czcionki lokalnie zamiast Google Fonts',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('R3 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('R4 wspolne.js → gabinet-saas.js (konto SaaS, klucz urządzenia, synchronizacja bez treści, pól szablonu, e-ZLA i inicjałów)',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('R5 katalog procedur z zasobów chronionych logowaniem',
   '<script src="prywatne-katalog.js?v=1"></script>', '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>'),
  ('R6 historia: wpis z innego urządzenia (z chmury) – komunikat, że treść jest na urządzeniu zapisu (zamiast „usunięta”)',
   "'<span class=\"pw-note\">treść opisu usunięta (ustawienie prywatności)</span>'",
   "'<span class=\"pw-note\">' + (m.cloud ? 'treść opisu jest tylko na urządzeniu, na którym zapisano wizytę' : 'treść opisu usunięta (ustawienie prywatności)') + '</span>'"),
]

PATCHES_KAL = [
  ('K1 bez ikon i manifestu wersji statycznej',
   '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n', ''),
  ('K2 czcionki lokalnie zamiast Google Fonts',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('K3 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('K4 wspolne.js → gabinet-saas.js (konto SaaS: dokumenty Kalendarza na koncie, gabinety wspólne z całą aplikacją, sumy z opisów z serwera)',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('K5 identyfikator gabinetu domyślnego: UUID (wspólna tabela gabinetów) zamiast „c1”…',
   "return { id: 'c' + (i + 1), name: 'Gabinet ' + (i + 1),", "return { id: crypto.randomUUID(), name: 'Gabinet ' + (i + 1),"),
  ('K6 identyfikator nowego gabinetu: UUID zamiast „c…”',
   "var c = defClinic(cs.length); c.id = 'c' + uid(); c.color = color;", "var c = defClinic(cs.length); c.id = crypto.randomUUID(); c.color = color;"),
  ('K7 notatka dyżuru zapisuje się na koncie – przypomnienie, żeby nie wpisywać danych pacjentów',
   '<label class="f">Notatka<input type="text" id="f-note"', '<label class="f">Notatka (bez danych pacjentów)<input type="text" id="f-note"'),
  ('K8 status zapisu w nagłówku: bez „zaszyfrowane, na tym urządzeniu” (dane Kalendarza są na koncie; stan wysyłki pokazuje pasek aplikacji)',
   "saved: 'Zapisano (zaszyfrowane)', local: 'Zaszyfrowane, na tym urządzeniu' }", "saved: 'Zapisano', local: 'Zapisano' }"),
  ('K9 opis „Dane” w Ustawieniach: dane Kalendarza są na koncie Gabinet (nie „tylko w tej przeglądarce”)',
   "'Dane są zapisane tylko w tej przeglądarce, na tym urządzeniu – nikt inny ich nie widzi i nie trafiają na żaden serwer. Rób co jakiś czas kopię (.json): Safari na iPhonie usuwa dane stron nieotwieranych przez 7 dni używania przeglądarki; po dodaniu aplikacji do ekranu początkowego („Udostępnij” → „Do ekranu początk.”) ten limit jej nie dotyczy.'",
   "'Dane Kalendarza (dyżury, kwoty, koszty, kursy, ustawienia) są zapisane na Twoim koncie Gabinet – widzisz je tylko Ty, na każdym urządzeniu po zalogowaniu. Gabinety są wspólne z całą aplikacją (zakładka „Gabinety”). Nie wpisuj tu danych pacjentów.'"),
  ('K10 „Usuń wszystkie dane” usuwa dyżury, kursy i ustawienia Kalendarza, ale nie gabinety (wspólne z Opisami i Zarobkami – usuwa się je w „Gabinety”)',
   "'reset-do': function () { Object.keys(Store.docs).forEach(function (k) { Store.remove(k); }); UI.ask = null;",
   "'reset-do': function () { var keep = S().clinics; Object.keys(Store.docs).forEach(function (k) { Store.remove(k); }); var ns = defaultSettings(); ns.clinics = keep; Store.docs.settings = normalizeSettings(ns); Store.touch('settings'); UI.ask = null;"),
  ('K11 pytanie przed usunięciem danych Kalendarza: gabinety zostają',
   "'<span class=\"confirm\">Usunąć wszystkie dyżury i ustawienia? ", "'<span class=\"confirm\">Usunąć wszystkie dyżury, kursy i ustawienia Kalendarza? Gabinety zostają. "),
  ('K12 zmiany z innego urządzenia (scalone na koncie) od razu w otwartym Kalendarzu – bez nadpisywania pola, które właśnie edytujesz',
   'function setSync(s) { Store.sync = s; renderHeader(); }',
   'function setSync(s) { Store.sync = s; renderHeader(); }\nwindow.addEventListener(\'gabinet:grafik\', function (e) {\n  var d = e.detail || {};\n  Object.keys(d).forEach(function (k) { if (Store.isDirty(k)) return; if (d[k]) Store.docs[k] = d[k]; else delete Store.docs[k]; });\n  if (Store.docs.settings) normalizeSettings(Store.docs.settings);\n  invalidate(); renderWhenIdle();\n});'),
  ('K13 nazwa modelu rozliczenia: „% po odjęciu kosztów własnych” (decyzja Patryka 21.11.2026; logika bez zmian)',
   "pct_lab: '% po odjęciu labu/implantów'", "pct_lab: '% po odjęciu kosztów własnych'"),
]

def przenies(plik, patches):
    src = open(os.path.join(OLD, plik), encoding='utf-8').read()
    for name, old, new in patches:
        n = src.count(old)
        if n != 1: sys.exit(f'Poprawka „{name}” pasuje {n} razy (oczekiwano 1) – sprawdź zmiany w opisy-nfz/{plik}')
        src = src.replace(old, new)
    head = f'<!-- Gabinet SaaS: przeniesione z opisy-nfz@{commit} ({plik}) przez tests/tools/przenies_generator.py; poprawki: generator/ZMIANY.md -->\n'
    open(os.path.join(OUT, plik), 'w', encoding='utf-8').write(head + src)

przenies('nfz.html', PATCHES)
przenies('prywatne.html', PATCHES_PRYW)
przenies('kalendarz.html', PATCHES_KAL)
shutil.copy(os.path.join(OLD, 'prywatne-katalog.js'), os.path.join(OUT, 'prywatne-katalog.js'))
shutil.copy(os.path.join(OLD, 'szablony.js'), os.path.join(OUT, 'szablony.js'))
shutil.copy(os.path.join(OLD, 'wspolne.css'), os.path.join(OUT, 'wspolne.css'))
with open(os.path.join(OUT, 'ZMIANY.md'), 'w', encoding='utf-8') as f:
    f.write(f'# Moduły Opisy NFZ, Opisy prywatne i Kalendarz – zmiany względem obecnej aplikacji\n\nŹródło: repo `opisy-nfz`, commit `{commit}` – pliki `nfz.html`, `szablony.js`, `prywatne.html`, `prywatne-katalog.js`, `kalendarz.html`, `wspolne.css` (logika, pytania, reguły NFZ, szablony i teksty bez zmian).\n'
            'Plik `wspolne.js` (sejf z hasłem w przeglądarce) zastąpiony przez `gabinet-saas.js`.\n\n## Opisy NFZ (`nfz.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
    f.write('\n## Opisy prywatne (`prywatne.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES_PRYW: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
    f.write('\n## Kalendarz (`kalendarz.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES_KAL: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
print(f'przeniesiono z opisy-nfz@{commit}: nfz.html ({len(PATCHES)}), prywatne.html ({len(PATCHES_PRYW)}), kalendarz.html ({len(PATCHES_KAL)} poprawek)')
