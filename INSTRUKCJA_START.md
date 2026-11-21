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

## 3. Uruchom / zaktualizuj

Pełna instrukcja obsługi: **`INSTRUKCJA_OBSLUGI.md`**.

**macOS:** Terminal → `cd ` (ze spacją) → przeciągnij folder → Enter → `bash zainstaluj-mac.command`.
Skrypt przenosi klucze do `~/Gabinet/.env` (przy kolejnych wersjach nie trzeba kopiować `.env`), robi kopię bazy przed aktualizacją,
uruchamia aplikację i tworzy aplikację **Gabinet** w `~/Applications` (start jednym kliknięciem).

**Windows:** kliknij dwa razy `uruchom-windows.bat` (przy „System Windows ochronił komputer”: **Więcej informacji → Uruchom mimo to**).

## 4. Co sprawdzić (etap 4e-1 – Kalendarz)

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Menu → **Kalendarz** | Kalendarz jak w obecnej aplikacji; na liście gabinetów są gabinety z zakładki **Gabinety** |
| 2 | Dodaj dyżur dziś (status „Odbyty”, obrót, lab) | przychód wyliczony jak w obecnej aplikacji; **Konto** → kafelek „Kalendarz: Dziś: …” |
| 3 | Zapisz wizytę w Opisach NFZ / prywatnych w tym gabinecie dziś, potem otwórz edycję dyżuru | podpowiedź „Z opisów tego dnia…” i przycisk **Wpisz jako obrót** |
| 4 | **Zarobki** → Dziś | kafelek i kolumna „Dyżury wg Kalendarza” (nie doliczane do „Razem”) |
| 5 | Zmień w Kalendarzu nazwę lub % gabinetu → **Gabinety** | zmiana widoczna; i odwrotnie: zmiana w Gabinetach → odśwież Kalendarz |
| 6 | Druga przeglądarka (np. Safari) → zaloguj się → Kalendarz | te same dyżury, kursy i ustawienia |
| 7 | Kalendarz → Ustawienia → **Usuń wszystkie dane** | dyżury i ustawienia Kalendarza znikają, **gabinety zostają** |

**Nowe konto bez gabinetów:** przy pierwszym zapisie w Kalendarzu powstaną 4 gabinety przykładowe „Gabinet 1–4” (jak w obecnej aplikacji) – zmienisz je w Kalendarzu albo w „Gabinety”.
**Notatki dyżurów, opisy kosztów i kursy zapisują się na koncie** – pole notatki ma dopisek „bez danych pacjentów”.

## Etap 4d – Zarobki

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Zapisz kilka wizyt NFZ i prywatnych w różnych gabinetach | — |
| 2 | **Konto** | kafelki „Dziś: N wizyt · kwota” dla NFZ i prywatnych |
| 3 | Menu → **Zarobki** → Dziś / Ten tydzień / Ten miesiąc / Poprzedni miesiąc / Ten rok | tabela gabinetów jak w oknie „Zarobki – wszystkie gabinety” obecnej aplikacji, wykres, szczegóły NFZ i prywatne |
| 4 | Własny zakres dat i filtr gabinetu → **Pokaż** | tylko wybrany okres / gabinet |
| 5 | **Pobierz CSV** → otwórz w Excelu / Numbers | polskie kolumny, kwoty z przecinkiem, każda kwota w osobnym wierszu |
| 6 | Ustawienia → „Zarobek z punktów: udział lekarza” | Zarobek NFZ liczony od udziału lekarza |

## Etap 4c – Opisy prywatne

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Menu → **Opisy prywatne** | ten sam moduł co w obecnej aplikacji (19 procedur, cenniki, szablony, zestawy, zarobki) |
| 2 | **Cennik** → wybierz gabinet → ceny i % | ceny pojawiają się przy dodawaniu procedur w tym gabinecie |
| 3 | Zrób wizytę (procedury, pola, opcjonalnie e-ZLA) → **Zapisz** | **identyczny tekst** jak w obecnej aplikacji; u góry „Historia zsynchronizowana” |
| 4 | Druga przeglądarka → Opisy prywatne → **Historia** | wizyta (procedury, kwoty, gabinet), komunikat „treść opisu jest tylko na urządzeniu, na którym zapisano wizytę”; ten sam cennik |
| 5 | **Szablony** → zmień szablon albo dodaj ulubioną procedurę | to samo w drugiej przeglądarce po odświeżeniu |

Przeniesienie historii prywatnej i Kalendarza ze starej aplikacji („Kopia całości”) – etap 4e.

## Etap 4b – Opisy NFZ

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Menu → **Opisy NFZ** | ten sam generator co w obecnej aplikacji; u góry pasek Gabinetu i napis „Historia zsynchronizowana” |
| 2 | Zrób wizytę jak zwykle (kody → pytania → opis) | **identyczny tekst** jak w obecnej aplikacji przy tych samych odpowiedziach |
| 3 | Zakładka **Historia** | wizyta z inicjałami (inicjały i treść zostają tylko na tym komputerze) |
| 4 | Zaloguj się w **drugiej przeglądarce** → Opisy NFZ → Historia | ta sama wizyta jako „Anonim” – data, kody, kwoty; **bez treści i bez inicjałów** |
| 5 | **Przeniesienie historii**: w generatorze zakładka **Ustawienia → Wczytaj kopię** – wybierz plik `.json` pobrany z obecnej aplikacji | wizyty z treścią na tym komputerze; w chmurze tylko kody i kwoty |
| 6 | Wyłącz Wi-Fi, zapisz wizytę, włącz Wi-Fi | najpierw „zapisano na tym urządzeniu, wyślę później”, potem „zsynchronizowana” |

Uwaga do kroku 5: wizyty z kopii nie mają przypisanego gabinetu (stara aplikacja ma inne identyfikatory gabinetów) – dopasowanie gabinetów zrobię przy imporcie Kalendarza (etap 4e).

## Etap 4a – gabinety, ustawienia, katalog NFZ

| Krok | Co zrobić | Czego oczekiwać |
|---|---|---|
| 1 | Zaloguj się; w menu: **Katalog NFZ · Gabinety · Ustawienia** | strony otwierają się (wymagają okresu próbnego / licencji) |
| 2 | **Gabinety** → dodaj swoje gabinety (nazwa, skrót, kolor, sposób rozliczenia, %) | lista z kolorami i modelem rozliczenia |
| 3 | Wpisz błędne dane (np. model „Stawka godzinowa” bez stawki) | komunikat, **wpisane pola zostają** |
| 4 | Otwórz edycję tego samego gabinetu w **dwóch kartach**, zapisz w obu | druga karta: „zmieniono w międzyczasie na innym urządzeniu” |
| 5 | **Ustawienia** → stawki NFZ | domyślnie 1,84 zł/pkt, 350 zł/h, 40% |
| 6 | **Katalog NFZ** → tabela kodów | 23 pozycje ze źródłem (95/2026/DSOZ, 44/2025/DSOZ) |
| 7 | (etap historyczny – „Sprawdź wycenę” usunięta 21.11.2026) | – |
| 8 | Dodaj **własny kod** (np. 2301, nazwa, punkty) | oznaczenie „niesprawdzane przez zasady NFZ”; kod z katalogu (np. ST01) odrzucony |

## Wcześniejsza faza 3 – konta i logowanie

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
