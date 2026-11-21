# Gabinet – instrukcja obsługi (wersja testowa na Maca)

Wersja do 7-dniowego testu. Aplikacja działa **tylko na Twoim Macu** (adres `http://localhost:3000`) – nic nie jest wysyłane do internetu, poza sprawdzeniem, czy hasło nie wyciekło (serwis „Have I Been Pwned”, wysyłany jest tylko 5-znakowy fragment skrótu hasła).

---

## 1. Instalacja (raz) i aktualizacja

**Wymagania:** Mac z Docker Desktop (masz już zainstalowany).
W Docker Desktop: **Settings → General → „Start Docker Desktop when you sign in”** – zaznacz, wtedy Gabinet ruszy sam po włączeniu komputera.

1. Pobierz ZIP z prywatnego repozytorium `gabinet-saas` (**Code → Download ZIP**) i rozpakuj.
2. Otwórz **Terminal**, wpisz `cd ` (ze spacją), przeciągnij rozpakowany folder do okna, Enter.
3. Wpisz `bash zainstaluj-mac.command` i Enter.

Skrypt:

| Krok | Co robi |
|---|---|
| Klucze | Tworzy folder **`~/Gabinet`** z plikiem kluczy `.env`. Przy pierwszym uruchomieniu przenosi tam klucze z obecnego folderu (Twoje dotychczasowe hasło bazy i klucze zostają). **Nie musisz już kopiować `.env` przy aktualizacji.** |
| Kopia przed aktualizacją | Jeśli Gabinet już działał – zapisuje kopię bazy `przed-aktualizacja-….dump` w `~/Gabinet/kopie`. |
| Start | Buduje i uruchamia aplikację (pierwszy raz kilka minut, kolejne 1–2 min). |
| Aplikacja „Gabinet” | Tworzy aplikację **Gabinet** w folderze **Aplikacje w katalogu domowym** (`~/Applications`). Przeciągnij ją do Docka. |

**Aktualizacja do nowej wersji:** pobierz nowy ZIP, rozpakuj i ponownie `bash zainstaluj-mac.command` z nowego folderu. Stary folder możesz potem usunąć – dane są w Dockerze i w `~/Gabinet`.

## 2. Codzienne uruchamianie

| Co | Jak |
|---|---|
| Start | Kliknij **Gabinet** w Docku (sam uruchomi Docker Desktop i otworzy przeglądarkę). |
| Adres | `http://localhost:3000` – możesz dodać zakładkę. |
| Zatrzymanie | Nie trzeba. Gdy chcesz: `bash zatrzymaj-mac.command` w folderze aplikacji albo zamknij Docker Desktop. Dane zostają. |
| Poczta testowa | `http://localhost:8025` – tu przychodzą maile z linkiem potwierdzającym i resetem hasła (nic nie wychodzi na zewnątrz). |

## 3. Pierwsze kroki

1. **Załóż konto** (min. 12 znaków hasła) → potwierdź e-mail w poczcie testowej (`localhost:8025`).
2. (Weryfikacja dwuetapowa 2FA jest w tej wersji wyłączona.)
3. **Gabinety** – dodaj gabinety (nazwa, kolor, model rozliczenia, %). Te same gabinety są w Kalendarzu, Opisach i Zarobkach. Nowe konto nie ma żadnych gabinetów – Kalendarz pokaże „Dodaj pierwszy gabinet”.
4. **Ustawienia** – stawki NFZ (1,84 zł/pkt, 350 zł/h przeglądów, udział 40/35%) i podstawa zarobku z punktów.
5. **Kalendarz → „Ustaw podatki i ZUS”** – kreator otwiera się przy pierwszym wejściu (3 pytania: start działalności, forma opodatkowania, ZUS; nic nie jest wpisane z góry). Możesz kliknąć „Pomiń na razie” i wrócić później. Bez tych ustawień Kalendarz i Zarobki nie liczą netto.
6. **Masz dane w starej aplikacji?** W starej: strona główna → **Kopia całości** → pobierz plik. W nowej: **Konto → „Przenieś dane ze starej aplikacji”** → wskaż plik, wpisz hasło kopii, sprawdź dopasowanie gabinetów → **Przenieś dane**. Ponowne przeniesienie nie dubluje wpisów.

## 4. Moduły

| Moduł | Do czego | Uwagi |
|---|---|---|
| **Kalendarz** | Dyżury, dni pracy, kursy, rozliczenia gabinetów, ZUS i podatek, porównanie form opodatkowania | Jak w obecnej aplikacji. Przy edycji dyżuru – podpowiedź „Wpisz jako obrót” z opisów tego dnia. Notatka dyżuru: **bez danych pacjentów**. Podatki i ZUS: kreator „Ustaw podatki i ZUS”; **Ustawienia → Działalność i podatek → „Ustaw od nowa (wyczyść)”** czyści tylko ustawienia podatków i ZUS (po potwierdzeniu) – dyżury, gabinety, koszty i kursy zostają. |
| **Opisy NFZ** | Generator opisów, kody, punkty, przeglądy, historia, statystyki | Gabinet wybiera się sam według dyżuru w Kalendarzu. |
| **Opisy prywatne** | Procedury, cennik z % lekarza, własne szablony, zestawy, historia | Wynagrodzenie liczone automatycznie (np. 500 zł × 40% = 200 zł). |
| **Zarobki** | Kafelki: „Razem z wizyt”, „Razem punktów”, „Zarobek lekarza (%)”, poprzedni okres; tabela „Wszystkie gabinety”: liczba wizyt, zarobek lekarza, zarobek na godzinę; przełącznik brutto/netto; wykres, średnie, dni tygodnia, filtr, **CSV** | Zarobek lekarza i godziny – z odbytych dyżurów w Kalendarzu wg zasad gabinetu (wpisz obrót przy dyżurze). Netto – wg ustawień podatków i ZUS z Kalendarza (ten sam sposób liczenia co w Kalendarzu); to **szacunek** (podatek rozlicza się rocznie) i dotyczy tylko zarobku lekarza z dyżurów – kwoty z wizyt i CSV są brutto. Bez ustawień w Kalendarzu netto nie jest liczone. |
| **Katalog NFZ** | Kody z punktami i źródłem (zarządzenie DSOZ) | Tylko do podglądu. |
| **Konto** | Imię, hasło, urządzenia (wylogowanie zdalne), dziennik bezpieczeństwa, kopie danych | Wersja testowa – dostęp bez limitu czasu. |

Zapis jest automatyczny. Status w prawym górnym rogu modułu: „zsynchronizowana” = zapisane na koncie; „brak połączenia – zapisano na tym urządzeniu” = wyśle się samo.

## 5. Gdzie są Twoje dane

| Dane | Gdzie | Zabezpieczenie |
|---|---|---|
| Konto, gabinety, ustawienia, Kalendarz, cenniki, szablony, zestawy, historia wizyt **bez danych pacjentów** (data, gabinet, kody, procedury, kwoty) | Baza na Twoim Macu (Docker, wolumen `gabinet_dane_bazy`) | Automatyczna kopia codziennie do `~/Gabinet/kopie` (30 ostatnich) + kopia przed każdą aktualizacją |
| **Treść opisów i inicjały pacjentów** | Tylko w przeglądarce, w której je zapisano (zaszyfrowane kluczem tego urządzenia) | **Twoja kopia:** Konto → „Kopia danych z tego urządzenia” → plik `.json` z hasłem |
| Klucze aplikacji (`.env`) | `~/Gabinet/.env` | Nie usuwaj i nie zmieniaj. Zrób kopię (np. na pendrive). Bez nich przestaną działać m.in. kody zabezpieczeń. |

**Czego nie robić:** nie czyść danych witryny `localhost` w przeglądarce (usuwa treść opisów z tego urządzenia), nie używaj „Reset to factory defaults” / „Clean / Purge data” w Docker Desktop (usuwa bazę), nie usuwaj folderu `~/Gabinet`.

## 6. Kopie zapasowe i przywracanie

| Co | Jak |
|---|---|
| Kopia bazy – automatycznie | Codziennie, pliki `gabinet-RRRR-MM-DD_GGMM.dump` w `~/Gabinet/kopie` |
| Kopia bazy – teraz | `bash kopia-teraz-mac.command` (plik `reczna-….dump`) |
| Przywrócenie bazy | `bash przywroc-mac.command` → wybierz numer kopii → wpisz `TAK`. Przed przywróceniem bieżący stan zapisuje się jako `przed-przywroceniem-….dump`. |
| Kopia treści opisów | Konto → **Kopia danych z tego urządzenia** → hasło (min. 10 znaków) → plik `gabinet-kopia-….json`. **Rób ją np. co 2–3 dni** i trzymaj poza Makiem. |
| Wczytanie kopii treści | Konto → **Wczytaj kopię** → plik + hasło. Nic nie kasuje, dopisuje brakujące. |

Zalecenie na 7 dni testu: raz dziennie pobierz „Kopię danych z tego urządzenia”, a co kilka dni skopiuj folder `~/Gabinet` na dysk zewnętrzny lub do iCloud.

## 7. Zgłaszanie błędów

Napisz w czacie, najlepiej w tej formie:

| Pole | Przykład |
|---|---|
| Moduł / strona | Opisy prywatne → Cennik |
| Co zrobiłeś (kroki) | 1. … 2. … 3. … |
| Co się stało | Kwota się nie zapisała |
| Czego oczekiwałeś | Kwota 400 zł zostaje po odświeżeniu |
| Zrzut ekranu | Cmd + Shift + 4 |
| Przeglądarka | Safari / Chrome |

**Bez danych pacjentów na zrzutach** (zasłoń inicjały i treść opisu).

## 8. Ograniczenia wersji testowej

| Element | Stan |
|---|---|
| Dostęp z telefonu / innego komputera | Niedostępny – aplikacja działa tylko na tym Macu (hosting tylko po Twojej zgodzie – etapy 5–6) |
| Płatności, licencje, panel administratora | Odłożone (dostęp bez limitu czasu) |
| E-maile | Tylko do poczty testowej `localhost:8025` |
| Treść opisów na innych urządzeniach | Tylko przez plik kopii (decyzja: treść nie trafia do chmury) |

## 9. Gdy coś nie działa

| Objaw | Co zrobić |
|---|---|
| Gabinet się nie otwiera | Otwórz Docker Desktop, poczekaj aż wieloryb przestanie migać, kliknij Gabinet ponownie |
| „Aplikacja nie odpowiada” | W folderze aplikacji: `bash zainstaluj-mac.command` (nic nie kasuje) i prześlij mi komunikat |
| „brak połączenia – zapisano na tym urządzeniu” | Aplikacja wyśle zmiany sama; jeśli trwa to długo – sprawdź, czy Gabinet działa |
| „Zmiany z innego urządzenia – odśwież” | Kliknij „odśwież” (np. edytowałeś w dwóch kartach) |
| Brak treści opisu w historii | Wizyta zapisana w innej przeglądarce – treść jest tylko tam (albo wczytaj kopię z tamtego urządzenia) |
| Zapomniane hasło | Logowanie → „Nie pamiętam hasła” → link w poczcie testowej `localhost:8025` |
