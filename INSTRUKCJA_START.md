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

**macOS (zalecane – przez Terminal, omija blokadę „Apple nie może zweryfikować…”):**

1. Otwórz **Terminal** (Cmd + Spacja → „Terminal”).
2. Wpisz `cd ` (ze spacją), przeciągnij rozpakowany folder do okna Terminala, Enter.
3. Wpisz `bash uruchom-mac.command` i Enter.

**Windows:** kliknij dwa razy `uruchom-windows.bat` (przy „System Windows ochronił komputer”: **Więcej informacji → Uruchom mimo to**).

Skrypt sam:
1. sprawdzi, czy Docker działa,
2. utworzy albo uzupełni plik `.env` losowymi hasłami i kluczami (tylko na Twoim komputerze; istniejących wartości nie zmienia),
3. zbuduje aplikację i zaktualizuje bazę (pierwszy raz 3–10 minut, kolejne zwykle 1–2 minuty),
4. otworzy przeglądarkę na **http://localhost:3000**.

**Aktualizacja do nowej wersji:** pobierz nowy ZIP, rozpakuj, **skopiuj plik `.env` ze starego folderu do nowego**
(na Macu ukryte pliki pokazuje Cmd + Shift + kropka), uruchom skrypt. Dane testowe w bazie zostają.

## 4. Co sprawdzić (faza 3 – konta i logowanie)

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | **Załóż konto** (http://localhost:3000 → „Załóż konto”) | strona „Sprawdź skrzynkę e-mail” |
| 2 | Otwórz **testową pocztę** http://localhost:8025 | wiadomość „potwierdź adres e-mail” |
| 3 | Kliknij link w wiadomości → „Potwierdzam adres e-mail” | „Adres e-mail potwierdzony” |
| 4 | Zaloguj się | strona „Konto”: okres próbny do daty za 3 miesiące |
| 5 | Zaloguj się w **drugiej przeglądarce** na tym komputerze (np. Safari i Chrome). Telefon nie połączy się z wersją lokalną – działa ona tylko na tym komputerze | w „Bezpieczeństwo” dwa urządzenia; e-mail „logowanie z nowego urządzenia” |
| 6 | „Bezpieczeństwo” → wyloguj drugie urządzenie | w drugiej przeglądarce po odświeżeniu – strona logowania |
| 7 | **Weryfikacja dwuetapowa**: włącz, zeskanuj kod QR telefonem (Google/Microsoft Authenticator), wpisz kod | 10 kodów zapasowych |
| 8 | Wyloguj i zaloguj ponownie | pytanie o kod z telefonu |
| 9 | „Nie pamiętam hasła” → link z Mailpit → nowe hasło | logowanie nowym hasłem; stare nie działa |
| 10 | 6 razy złe hasło | „Zbyt wiele prób” (blokada 15 minut) |

Stan techniczny środowiska (tylko lokalnie): http://localhost:3000/stan

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
