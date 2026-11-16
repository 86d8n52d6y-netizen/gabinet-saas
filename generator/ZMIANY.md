# Moduły Opisy NFZ i Opisy prywatne – zmiany względem obecnej aplikacji

Źródło: repo `opisy-nfz`, commit `716689d` – pliki `nfz.html`, `szablony.js`, `prywatne.html`, `prywatne-katalog.js`, `wspolne.css` (logika, pytania, reguły NFZ, szablony i teksty bez zmian).
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
