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
  ('K14 domyślne ustawienia bez założeń o użytkowniku (decyzja Patryka 21.11.2026): pusty start JDG, brak formy opodatkowania i okresów ZUS – wybiera użytkownik (kreator K16)',
   "jdgStart: '2026-10', regimes: { 2026: 'skala', 2027: 'ryczalt' }, ryczaltRate: 14,\n    uop: {}, kwotaJDG: true, zus: [{ id: 'z1', from: '2026-10', variant: 'custom', amount: 800, base: 0, chor: true }],",
   "jdgStart: '', regimes: {}, ryczaltRate: 14,\n    uop: {}, kwotaJDG: true, zus: [],"),
  ('K15 bez ustawionych podatków i ZUS nie pokazujemy „netto ≈” ani „odłóż” (zamiast wyniku liczonego z cudzych założeń); taxReady() = start JDG + forma + okres ZUS',
   "function reserveRatio(mk) {\n  var o = monthRes(mk, 'fcst');",
   "function curYear() { return +todayStr().slice(0, 4); }\nfunction taxReady() { var s = S(); return /^\\d{4}-\\d{2}$/.test(s.jdgStart || '') && Object.keys(s.regimes || {}).length > 0 && Array.isArray(s.zus) && s.zus.length > 0; }\nfunction taxNote(tag) { return '<' + (tag || 'div') + ' class=\"note\" data-tax-todo>Ustaw <b>podatki i ZUS</b> – wtedy policzę netto i kwoty do odłożenia. <button class=\"btn sm\" data-a=\"wiz-open\">Ustaw teraz</button></' + (tag || 'div') + '>'; }\nfunction reserveRatio(mk) {\n  if (!taxReady()) return null;\n  var o = monthRes(mk, 'fcst');"),
  ('K15a podsumowanie miesiąca bez ustawień podatków: zaproszenie do kreatora zamiast „JDG nieaktywna (start: )”',
   "  if (!a.active) return '<div class=\"note\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ').</div>';",
   "  if (!a.active) return taxReady() ? '<div class=\"note\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ').</div>' : taxNote();"),
  ('K15b pasek miesiąca bez ustawień podatków: zaproszenie do kreatora',
   "  if (!a.active) return '<span class=\"muted\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ')</span>';",
   "  if (!a.active) return taxReady() ? '<span class=\"muted\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ')</span>' : '<span class=\"muted\">Ustaw podatki i ZUS, żeby liczyć netto</span>';"),
  ('K15c Podsumowanie bez ustawień podatków: zaproszenie do kreatora',
   "  if (!a.active) h += '<div class=\"note\">W tym miesiącu JDG nie była aktywna (start: ' + esc(S().jdgStart) + '). Datę zmienisz w Ustawieniach → Podatek.</div>';",
   "  if (!a.active) h += taxReady() ? '<div class=\"note\">W tym miesiącu JDG nie była aktywna (start: ' + esc(S().jdgStart) + '). Datę zmienisz w Ustawieniach → Podatek.</div>' : taxNote();"),
  ('K15d tydzień: „Netto ≈” tylko przy ustawionych podatkach i ZUS',
   "['Netto ≈', zl0(n.net), '']",
   "['Netto ≈', taxReady() ? zl0(n.net) : '—', taxReady() ? '' : 'ustaw podatki i ZUS']"),
  ('K16 kreator „Ustaw podatki i ZUS” przy pierwszym otwarciu (3 pytania, bez wartości z góry; można pominąć i wrócić)',
   "function nudges() {\n  if (!UI.loaded) return '<div class=\"note\">Wczytuję Twoje dane…</div>';\n  var out = [], todo = todoShifts();",
   "function wizard() {\n  var cy = curYear(), opt = function (o) { return Object.keys(o).map(function (k) { return '<option value=\"' + k + '\">' + o[k] + '</option>'; }).join(''); };\n  return '<div class=\"card\" id=\"wiz\" style=\"margin-bottom:12px\"><h3 style=\"margin-top:0\">Ustaw podatki i ZUS</h3><p class=\"small muted\">Z tego policzę netto, kwoty do odłożenia i terminy. Niczego nie zakładam z góry – zmienisz to w każdej chwili w Ustawieniach.</p><div class=\"frow\">' +\n    '<label class=\"f\">1. Od kiedy prowadzisz JDG<input type=\"month\" id=\"wiz-start\"><span class=\"hint\">miesiąc rozpoczęcia lub wznowienia</span></label>' +\n    '<label class=\"f\">2. Forma opodatkowania w ' + cy + '<select id=\"wiz-reg\"><option value=\"\">— wybierz —</option>' + opt(REGIMES) + '</select></label>' +\n    '<label class=\"f\">Od ' + (cy + 1) + ' (opcjonalnie)<select id=\"wiz-reg2\"><option value=\"\">bez zmiany</option>' + opt(REGIMES) + '</select></label>' +\n    '<label class=\"f\">3. Składki społeczne ZUS<select id=\"wiz-zus\"><option value=\"\">— wybierz —</option>' + opt(ZUSV) + '</select></label>' +\n    '<label class=\"f\">Kwota (zł)<input type=\"text\" inputmode=\"decimal\" id=\"wiz-amt\"><span class=\"hint\">„z eZUS”: miesięczne społeczne · „własna podstawa”: podstawa wymiaru</span></label>' +\n    '<label class=\"chk\" style=\"align-self:end\"><input type=\"checkbox\" id=\"wiz-chor\"> chorobowe (dobrowolne)</label></div>' +\n    '<div class=\"row\"><button class=\"btn primary\" data-a=\"wiz-save\">Zapisz</button><button class=\"btn ghost\" data-a=\"wiz-skip\">Pomiń na razie</button></div></div>';\n}\nfunction nudges() {\n  if (!UI.loaded) return '<div class=\"note\">Wczytuję Twoje dane…</div>';\n  var out = [], todo = todoShifts();\n  if (Store.mode !== 'demo' && (UI.wiz || (!taxReady() && !S().setup.wizSkip))) out.push(wizard());\n  else if (Store.mode !== 'demo' && !taxReady()) out.push('<button class=\"nudge accent\" data-a=\"wiz-open\"><b>Ustaw podatki i ZUS</b> – wtedy policzę netto i kwoty do odłożenia</button>');"),
  ('K16a akcje kreatora i „Ustaw od nowa” (czyści tylko ustawienia podatków i ZUS – po potwierdzeniu; dyżury, gabinety, koszty i kursy zostają)',
   "  'uop-calc': function () {",
   "  'wiz-open': function () { UI.wiz = true; UI.tab = 'cal'; UI.edit = null; render(); window.scrollTo(0, 0); },\n  'wiz-skip': function () { S().setup.wizSkip = true; UI.wiz = false; saveSettings(); render(); },\n  'wiz-save': function () {\n    var v = function (id) { return (document.getElementById(id) || {}).value || ''; };\n    var st = v('wiz-start'), r = v('wiz-reg'), r2 = v('wiz-reg2'), zv = v('wiz-zus'), amt = num(v('wiz-amt'));\n    if (!/^\\d{4}-\\d{2}$/.test(st)) return toast('Podaj miesiąc startu JDG');\n    if (!REGIMES[r]) return toast('Wybierz formę opodatkowania');\n    if (!ZUSV[zv]) return toast('Wybierz wariant składek ZUS');\n    if ((zv === 'custom' || zv === 'base') && !(amt > 0)) return toast(zv === 'custom' ? 'Wpisz miesięczną kwotę społecznych z eZUS' : 'Wpisz podstawę wymiaru');\n    var s = S(), cy = curYear(), y0 = +st.slice(0, 4), b = Math.max(y0, cy);\n    s.jdgStart = st; s.regimes = {}; s.regimes[y0] = r; s.regimes[b] = r; if (r2 && r2 !== r) s.regimes[b + 1] = r2;\n    s.zus = [{ id: uid(), from: st, variant: zv, amount: zv === 'custom' ? amt : 0, base: zv === 'base' ? amt : 0, chor: !!(document.getElementById('wiz-chor') || {}).checked }];\n    s.setup.zus = true; s.setup.wizSkip = false; UI.wiz = false; saveSettings(); render(); toast('Zapisano – netto liczę wg Twoich ustawień');\n  },\n  'tax-reset-ask': function () { UI.taxReset = true; render(); },\n  'tax-reset-no': function () { UI.taxReset = false; render(); },\n  'tax-reset-do': function () {\n    var s = S(); s.jdgStart = ''; s.regimes = {}; s.zus = []; s.uop = {}; s.wakacje = {}; s.annualOverride = {}; s.params = {}; s.healthMode = 'auto'; s.ryczaltRate = 14; s.kwotaJDG = true;\n    s.setup.zus = false; s.setup.uop = false; s.setup.wizSkip = false; UI.taxReset = false; saveSettings(); ACT['wiz-open'](); toast('Wyczyszczono ustawienia podatków i ZUS – ustaw je od nowa');\n  },\n  'uop-calc': function () {"),
  ('K17 przycisk „Ustaw od nowa” w Ustawieniach → Działalność i podatek (z potwierdzeniem)',
   "'<section class=\"set-sec\" id=\"sec-tax\"><h2>Działalność i podatek</h2><div class=\"card\"><div class=\"frow\">' +",
   "'<section class=\"set-sec\" id=\"sec-tax\"><h2>Działalność i podatek</h2>' + (UI.taxReset ? '<div class=\"confirm\" data-tax-reset>Wyczyścić ustawienia podatków i ZUS (start JDG, formę opodatkowania, okresy ZUS, wakacje składkowe, dochód z etatu, parametry lat, prognozę przychodu)? Dyżury, gabinety, koszty i kursy zostają. <button class=\"btn sm danger\" data-a=\"tax-reset-do\">Tak, wyczyść</button><button class=\"btn sm\" data-a=\"tax-reset-no\">Nie</button></div>' : '<div class=\"row\" style=\"margin-bottom:10px\"><button class=\"btn ghost\" data-a=\"wiz-open\">Kreator: ustaw podatki i ZUS</button><button class=\"btn ghost danger\" data-a=\"tax-reset-ask\">Ustaw od nowa (wyczyść)</button></div>') + '<div class=\"card\"><div class=\"frow\">' +"),
  ('K18 opis pola startu JDG – ogólny (nie tylko wznowienie)',
   "Start JDG (wznowienie)", "Start JDG (lub wznowienie)"),
  ('K19 etat: bieżący rok zamiast stałego 2026 (Ustawienia, pomocnik, pierwsze kroki)',
   "'<div class=\"card\"><h3>Etat w 2026 (skala)</h3><div class=\"frow\">' + fld('Dochód z etatu 2026 (zł)', 'uop-2026', 'uop.2026', (s.uop || {})[2026], { num: 1, hint: 'przychód − koszty − Twoje składki społeczne (PIT-11)' }) +\n    '<label class=\"f\">Pomocnik: brutto z etatu w 2026<input",
   "'<div class=\"card\"><h3>Etat w ' + curYear() + ' (skala, jeśli masz)</h3><div class=\"frow\">' + fld('Dochód z etatu ' + curYear() + ' (zł)', 'uop-' + curYear(), 'uop.' + curYear(), (s.uop || {})[curYear()], { num: 1, hint: 'przychód − koszty − Twoje składki społeczne (PIT-11)' }) +\n    '<label class=\"f\">Pomocnik: brutto z etatu w ' + curYear() + '<input"),
  ('K19a pomocnik etatu zapisuje bieżący rok',
   "s.uop = s.uop || {}; s.uop[2026] = v;", "s.uop = s.uop || {}; s.uop[curYear()] = v;"),
  ('K19b pierwsze kroki: „Podatki i ZUS” (kreator) zamiast „Kwota ZUS z eZUS”; etat bieżącego roku i opcjonalny',
   "['Kwota ZUS z eZUS', 'set', 'sec-zus', !!s.setup.zus],\n    ['Dochód z etatu 2026', 'set', 'sec-tax', !!s.setup.uop || (num((s.uop || {})[2026]) || 0) > 0],",
   "['Podatki i ZUS', 'wiz', '', taxReady() && !!s.setup.zus],\n    ['Dochód z etatu (jeśli masz)', 'set', 'sec-tax', !!s.setup.uop || (num((s.uop || {})[curYear()]) || 0) > 0],"),
  ('K19c pierwsze kroki: krok „wiz” otwiera kreator',
   "var act = x[1] === 'tpl' ? 'data-a=\"tpl-open\"' :", "var act = x[1] === 'tpl' ? 'data-a=\"tpl-open\"' : x[1] === 'wiz' ? 'data-a=\"wiz-open\"' :"),
  ('K20 koszty firmowe: opis ogólny zamiast planu jednej osoby (skala do końca 2026)',
   "<p>Na skali (do końca 2026) koszty obniżają podatek i zdrowotną. Na ryczałcie zmniejszają tylko Twoje netto – dlatego większe zakupy warto rozważyć jeszcze w 2026 (potwierdź z księgową).</p>",
   "<p>Na skali i podatku liniowym koszty obniżają podatek i zdrowotną. Na ryczałcie nie obniżają podatku – zmniejszają tylko Twoje netto (szczegóły potwierdź z księgową).</p>"),
  ('K21 „+ Dodaj okres” ZUS przy pustej liście: od startu JDG (albo bieżącego miesiąca), wariant do wyboru',
   "var s = S(), last = s.zus[s.zus.length - 1]; s.zus.push({ id: uid(), from: mkAdd(last && last.from ? last.from : s.jdgStart, 12), variant: 'full',",
   "var s = S(), last = s.zus[s.zus.length - 1]; s.zus.push({ id: uid(), from: last && last.from ? mkAdd(last.from, 12) : (s.jdgStart || mkOf(todayStr())), variant: last ? 'full' : 'custom',"),
  ('K22 przykład (demo) z własnymi, oznaczonymi wartościami podatków – domyślne są puste',
   "s.setup = { clinics: true, zus: true, uop: true, grid: true }; s.uop = { 2026: 85000 };",
   "s.setup = { clinics: true, zus: true, uop: true, grid: true }; s.uop = {}; s.uop[curYear()] = 85000;\n  s.jdgStart = (curYear() - 1) + '-01'; s.regimes = {}; s.regimes[curYear() - 1] = 'skala'; s.zus = [{ id: 'z1', from: s.jdgStart, variant: 'custom', amount: 1600, base: 0, chor: true }];"),
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
