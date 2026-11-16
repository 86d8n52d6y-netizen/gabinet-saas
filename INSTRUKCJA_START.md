# Gabinet (wersja SaaS) – uruchomienie na własnym komputerze

To jest **wersja testowa, lokalna**. Działa tylko na Twoim komputerze, nic nie trafia do internetu i nic nie kosztuje.
Obecna strona na GitHub Pages działa dalej bez zmian.

## 1. Jednorazowo: zainstaluj Docker Desktop

| System | Co zrobić |
|---|---|
| macOS | Wejdź na https://www.docker.com/products/docker-desktop/ → „Download for Mac” (wybierz *Apple Silicon* dla M1/M2/M3/M4 albo *Intel*). Otwórz pobrany plik `.dmg` i przeciągnij Docker do Aplikacji. |
| Windows 10/11 | Ta sama strona → „Download for Windows”. Zainstaluj z domyślnymi opcjami (WSL 2). Po instalacji może być potrzebny restart. |

Uruchom aplikację **Docker Desktop** i poczekaj, aż napisze „Engine running” (ikona wieloryba przestaje migać).
Docker Desktop jest darmowy do użytku prywatnego i w małych firmach (do 250 osób i 10 mln USD przychodu).

## 2. Pobierz projekt

1. Zaloguj się na GitHub (konto właściciela) i otwórz https://github.com/86d8n52d6y-netizen/gabinet-saas – repozytorium jest **prywatne**, inni go nie widzą.
2. Zielony przycisk **Code → Download ZIP**.
3. Rozpakuj ZIP i wejdź do rozpakowanego folderu (tam są pliki `uruchom-…`).

## 3. Uruchom

| System | Plik do kliknięcia (2×) |
|---|---|
| macOS | `uruchom-mac.command` (za pierwszym razem: prawy klik → **Otwórz** → **Otwórz**, bo macOS blokuje pliki z internetu) |
| Windows | `uruchom-windows.bat` (jeśli pojawi się „System Windows ochronił komputer”: **Więcej informacji → Uruchom mimo to**) |

Skrypt sam:
1. sprawdzi, czy Docker działa,
2. utworzy plik `.env` z **losowymi** hasłami do bazy (tylko na Twoim komputerze),
3. zbuduje aplikację (pierwszy raz 3–10 minut, kolejne kilka sekund),
4. otworzy przeglądarkę na **http://localhost:3000**.

## 4. Co powinieneś zobaczyć

Stronę „Gabinet” z tabelą **Stan środowiska: wszystko działa** i sześcioma wierszami „OK”:

| Sprawdzenie | Co oznacza |
|---|---|
| Połączenie z bazą PostgreSQL | baza działa |
| Aplikacja łączy się jako rola bez uprawnień do tabel | aplikacja nie ma „klucza do wszystkiego” |
| Tabele schematu (migracje) | baza została utworzona |
| Wymuszona izolacja wierszy (RLS) | każdy użytkownik widzi tylko swoje dane |
| Bez wybranej roli odczyt tabel zablokowany | dodatkowa blokada |
| Rola administratora: tylko statystyki liczbowe | admin nie widzi treści użytkowników |

Testowa skrzynka pocztowa (przyda się od fazy 3): **http://localhost:8025**. Wszystkie maile aplikacji trafiają tylko tam.

**Proszę o zrzut ekranu tej strony** albo informację, który wiersz nie ma „OK”.

## 5. Zatrzymanie i usunięcie

| Cel | Jak |
|---|---|
| Zatrzymać (dane zostają) | `zatrzymaj-mac.command` / `zatrzymaj-windows.bat` |
| Usunąć wszystko łącznie z testową bazą | w Docker Desktop → Containers → `gabinet` → kosz, oraz Volumes → `gabinet_dane_bazy` → kosz |

## Gdy coś nie działa

| Objaw | Rozwiązanie |
|---|---|
| „Docker Desktop nie jest uruchomiony” | otwórz Docker Desktop i poczekaj na „Engine running” |
| „port is already allocated” (3000 lub 8025) | inny program używa portu – zamknij go albo napisz, zmienię port |
| Po zmianie haseł w `.env` baza nie startuje | hasła ustawia się raz przy pierwszym starcie bazy; usuń wolumen `gabinet_dane_bazy` (to tylko dane testowe) |
| Cokolwiek innego | skopiuj tekst z okna terminala i prześlij |
