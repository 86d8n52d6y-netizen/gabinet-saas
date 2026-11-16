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
