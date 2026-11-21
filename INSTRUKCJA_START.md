# Gabinet (wersja SaaS) – uruchomienie na własnym komputerze

To jest **wersja testowa, lokalna**. Działa tylko na Twoim komputerze, nic nie trafia do internetu i nic nie kosztuje.
Obecna strona na GitHub Pages działa dalej bez zmian.

## 1. Jednorazowo: zainstaluj Docker Desktop

Wejdź na https://www.docker.com/products/docker-desktop/ → „Download for Mac” (wybierz *Apple Silicon* dla M1/M2/M3/M4 albo *Intel*). Otwórz pobrany plik `.dmg` i przeciągnij Docker do Aplikacji.

Uruchom aplikację **Docker Desktop** i poczekaj, aż napisze „Engine running” (ikona wieloryba przestaje migać).
Docker Desktop jest darmowy do użytku prywatnego i w małych firmach (do 250 osób i 10 mln USD przychodu).

## 2. Pobierz projekt

1. Zaloguj się na GitHub (konto właściciela) i otwórz https://github.com/86d8n52d6y-netizen/gabinet-saas – repozytorium jest **prywatne**, inni go nie widzą.
2. Zielony przycisk **Code → Download ZIP**.
3. Rozpakuj ZIP i wejdź do rozpakowanego folderu (tam są pliki `uruchom-…`).

## 3. Uruchom / zaktualizuj

Pełna instrukcja obsługi: **`INSTRUKCJA_OBSLUGI.md`**.

**macOS:** Terminal → `cd ` (ze spacją) → przeciągnij folder → Enter → `bash zainstaluj-mac.command`.
Skrypt przenosi klucze do `~/Gabinet/.env` (przy kolejnych wersjach nie trzeba kopiować `.env`), robi kopię bazy przed aktualizacją,
uruchamia aplikację i tworzy aplikację **Gabinet** w `~/Applications` (start jednym kliknięciem).

Wersja testowa działa tylko na Macu (skrypty dla Windows usunięte 21.11.2026).

## 4. Co sprawdzić po aktualizacji (zmiany z 21.11.2026)

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Zaktualizuj: `bash zainstaluj-mac.command` z nowego folderu | aplikacja startuje, dane zostają (kopia bazy w `~/Gabinet/kopie`) |
| 2 | **Kalendarz → Ustawienia → Działalność i podatek → „Ustaw od nowa (wyczyść)”** → potwierdź | otwiera się kreator „Ustaw podatki i ZUS”; dyżury, gabinety, koszty i kursy zostają |
| 3 | Przejdź kreator (start działalności, forma, ZUS) | Kalendarz pokazuje „netto ≈” i „odłóż” |
| 4 | **Zarobki** → przełącznik **Netto** | zarobek lekarza netto wg ustawień Kalendarza; kwoty z wizyt i CSV brutto |
| 5 | **Gabinety** | jeśli są fikcyjne „Gabinet 1–4” (powstały przed poprawką 21.11) – usuń je ręcznie |
| 6 | Nowe konto testowe (inny e-mail) → Kalendarz | brak przykładowych gabinetów, zachęta „Dodaj pierwszy gabinet” |

Pełny opis modułów: **`INSTRUKCJA_OBSLUGI.md`**. Listy kontrolne wcześniejszych etapów (4a–4e, konta) są w historii repozytorium.

## 5. Zatrzymanie i usunięcie

| Cel | Jak |
|---|---|
| Zatrzymać (dane zostają) | `bash zatrzymaj-mac.command` |
| Usunąć wszystko łącznie z testową bazą | w Docker Desktop → Containers → `gabinet` → kosz, oraz Volumes → `gabinet_dane_bazy` → kosz |

## Gdy coś nie działa

| Objaw | Rozwiązanie |
|---|---|
| „Docker Desktop nie jest uruchomiony” | otwórz Docker Desktop i poczekaj na „Engine running” |
| „port is already allocated” (3000 lub 8025) | inny program używa portu – zamknij go albo napisz, zmienię port |
| Po zmianie haseł w `.env` baza nie startuje | hasła ustawia się raz przy pierwszym starcie bazy; usuń wolumen `gabinet_dane_bazy` (to tylko dane testowe) |
| Cokolwiek innego | skopiuj tekst z okna terminala i prześlij |
