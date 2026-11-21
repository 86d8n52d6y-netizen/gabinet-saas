# Moduły Opisy NFZ, Opisy prywatne i Kalendarz – zmiany względem obecnej aplikacji

Źródło: repo `opisy-nfz`, commit `716689d` – pliki `nfz.html`, `szablony.js`, `prywatne.html`, `prywatne-katalog.js`, `kalendarz.html`, `wspolne.css` (logika, pytania, reguły NFZ, szablony i teksty bez zmian).
Plik `wspolne.js` (sejf z hasłem w przeglądarce) zastąpiony przez `gabinet-saas.js`.

## Opisy NFZ (`nfz.html`)

| # | Poprawka |
|---|---|
| P1 | czcionki lokalnie zamiast Google Fonts (prywatność: brak wysyłania IP do Google; CSP tylko własne zasoby) |
| P2 | tytuł strony w aplikacji Gabinet |
| P3 | bez manifestu i ikon wersji statycznej (aplikacja SaaS ma własne) |
| P4 | wspólne style z zasobów chronionych logowaniem |
| P5 | wspolne.js (sejf lokalny z hasłem) → gabinet-saas.js (konto SaaS: klucz urządzenia, synchronizacja danych bez treści opisów); dane startowe wstawia serwer w miejsce znacznika |
| P6 | szablony.js z zasobów chronionych logowaniem |
| P7 | identyfikator gabinetu: UUID z bazy (36 znaków) zamiast „c1”…„c24” z Kalendarza |

## Opisy prywatne (`prywatne.html`)

| # | Poprawka |
|---|---|
| R1 | bez manifestu i ikon wersji statycznej |
| R2 | czcionki lokalnie zamiast Google Fonts |
| R3 | wspólne style z zasobów chronionych logowaniem |
| R4 | wspolne.js → gabinet-saas.js (konto SaaS, klucz urządzenia, synchronizacja bez treści, pól szablonu, e-ZLA i inicjałów) |
| R5 | katalog procedur z zasobów chronionych logowaniem |
| R6 | historia: wpis z innego urządzenia (z chmury) – komunikat, że treść jest na urządzeniu zapisu (zamiast „usunięta”) |

## Kalendarz (`kalendarz.html`)

| # | Poprawka |
|---|---|
| K1 | bez ikon i manifestu wersji statycznej |
| K2 | czcionki lokalnie zamiast Google Fonts |
| K3 | wspólne style z zasobów chronionych logowaniem |
| K4 | wspolne.js → gabinet-saas.js (konto SaaS: dokumenty Kalendarza na koncie, gabinety wspólne z całą aplikacją, sumy z opisów z serwera) |
| K5 | identyfikator gabinetu domyślnego: UUID (wspólna tabela gabinetów) zamiast „c1”… |
| K6 | identyfikator nowego gabinetu: UUID zamiast „c…” |
| K7 | notatka dyżuru zapisuje się na koncie – przypomnienie, żeby nie wpisywać danych pacjentów |
| K8 | status zapisu w nagłówku: bez „zaszyfrowane, na tym urządzeniu” (dane Kalendarza są na koncie; stan wysyłki pokazuje pasek aplikacji) |
| K9 | opis „Dane” w Ustawieniach: dane Kalendarza są na koncie Gabinet (nie „tylko w tej przeglądarce”) |
| K10 | „Usuń wszystkie dane” usuwa dyżury, kursy i ustawienia Kalendarza, ale nie gabinety (wspólne z Opisami i Zarobkami – usuwa się je w „Gabinety”) |
| K11 | pytanie przed usunięciem danych Kalendarza: gabinety zostają |
| K12 | zmiany z innego urządzenia (scalone na koncie) od razu w otwartym Kalendarzu – bez nadpisywania pola, które właśnie edytujesz |
| K13 | nazwa modelu rozliczenia: „% po odjęciu kosztów własnych” (decyzja Patryka 21.11.2026; logika bez zmian) |
| K14 | domyślne ustawienia bez założeń o użytkowniku (decyzja Patryka 21.11.2026): pusty start JDG, brak formy opodatkowania i okresów ZUS – wybiera użytkownik (kreator K16) |
| K15 | bez ustawionych podatków i ZUS nie pokazujemy „netto ≈” ani „odłóż” (zamiast wyniku liczonego z cudzych założeń); taxReady() = start JDG + forma + okres ZUS |
| K15a | podsumowanie miesiąca bez ustawień podatków: zaproszenie do kreatora zamiast „JDG nieaktywna (start: )” |
| K15b | pasek miesiąca bez ustawień podatków: zaproszenie do kreatora |
| K15c | Podsumowanie bez ustawień podatków: zaproszenie do kreatora |
| K15d | tydzień: „Netto ≈” tylko przy ustawionych podatkach i ZUS |
| K16 | kreator „Ustaw podatki i ZUS” przy pierwszym otwarciu (3 pytania, bez wartości z góry; można pominąć i wrócić) |
| K16a | akcje kreatora i „Ustaw od nowa” (czyści tylko ustawienia podatków i ZUS – po potwierdzeniu; dyżury, gabinety, koszty i kursy zostają) |
| K17 | przycisk „Ustaw od nowa” w Ustawieniach → Działalność i podatek (z potwierdzeniem) |
| K18 | opis pola startu JDG – ogólny (nie tylko wznowienie) |
| K19 | etat: bieżący rok zamiast stałego 2026 (Ustawienia, pomocnik, pierwsze kroki) |
| K19a | pomocnik etatu zapisuje bieżący rok |
| K19b | pierwsze kroki: „Podatki i ZUS” (kreator) zamiast „Kwota ZUS z eZUS”; etat bieżącego roku i opcjonalny |
| K19c | pierwsze kroki: krok „wiz” otwiera kreator |
| K20 | koszty firmowe: opis ogólny zamiast planu jednej osoby (skala do końca 2026) |
| K21 | „+ Dodaj okres” ZUS przy pustej liście: od startu JDG (albo bieżącego miesiąca), wariant do wyboru |
| K22 | przykład (demo) z własnymi, oznaczonymi wartościami podatków – domyślne są puste |
| K23 | domyślnie zero gabinetów (decyzja Patryka 21.11.2026): wcześniej puste konto dostawało 4 przykładowe gabinety z UUID, które przy pierwszym zapisie ustawień trafiały do tabeli gabinetów konta |
| K23a | pusta lista gabinetów zostaje pusta (bez dopełniania przykładowymi) |
| K23b | przykład (demo) tworzy własne 4 gabinety przykładowe |
| K24 | zachęta „Dodaj pierwszy gabinet” (Gabinety w aplikacji) zamiast „Ustaw dni pracy”, gdy konto nie ma gabinetów |
| K25 | bez gabinetu: nowy dyżur prosi o dodanie gabinetu (zamiast błędu) |
| K25a | bez gabinetu: „Dodaj dyżury” prosi o dodanie gabinetu |
| K25b | bez gabinetu: nowy wzór dni pracy prosi o dodanie gabinetu |
| K25c | bez gabinetu: klik w siatkę tygodnia nie odwołuje się do nieistniejącego gabinetu |
