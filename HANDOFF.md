# HANDOFF – Gabinet SaaS (stan na 21.11.2026)

Przekazanie projektu z czatu Claude do Claude Code. Źródło prawdy: **kod w repozytorium** (ostatni commit `97165c3`), `POSTEP.md`, `docs/AUDYT_SAAS.md`. Ten plik streszcza stan; przy rozbieżności rozstrzyga kod i `POSTEP.md`.

## 0. Najpierw przeczytaj

| Sprawa | Stan |
|---|---|
| Ostatni commit kodu | `97165c3` (Kalendarz bez przykładowych gabinetów) – **wysłany na GitHub 21.11.2026**; następny commit dodaje tylko `CLAUDE.md` i `HANDOFF.md`. ZIP przekazany w czacie zawiera ten sam stan kodu. |
| Kompletność | ZIP = wszystkie pliki śledzone przez git w `97165c3` (pełny kod, nie fragmenty) + ten plik + nowy `CLAUDE.md`. Pominięte: `node_modules/`, `.next/`, `.env` (sekrety), `tsconfig.tsbuildinfo`, `next-env.d.ts` (generowane), `tests/e2e/__pycache__/*.pyc` (śmieć śledzony w repo). |
| `CLAUDE.md` | **Zastępuje** dotychczasowy `CLAUDE.md` z repo (wszystkie jego zasady przeniesione + nowe sekcje). |
| Testy w chwili pakowania | wszystkie zielone (szczegóły w sekcji 2). **Na Macu Patryka nie sprawdzone są zmiany z 21.11.** |
| Nieaktualne dokumenty | `INSTRUKCJA_OBSLUGI.md` (Zarobki: „Netto – po skonfigurowaniu Twoich zasad rozliczenia” – od 21.11 netto liczy się z ustawień Kalendarza; brak opisu kreatora podatków i „Ustaw od nowa”); `INSTRUKCJA_START.md` sekcja 4 (lista kontrolna z etapu 4e-1); `README.md` („z licencjami” – licencje odłożone). **Zaktualizowane 21.11.2026** (odpowiedź na pytanie 7, sekcja 7). |

## 1. Numeracja etapów (dwie równoległe – nie mieszać)

Używaliśmy **dwóch numeracji**; przy rozmowie podawaj obie.

**A. Fazy z pierwotnego planu (`docs/AUDYT_SAAS.md` §4):**

| Faza | Zakres | Stan |
|---|---|---|
| 1 | Audyt i plan | ✅ zakończona, decyzje 1–4 |
| 2 | Projekt Next.js, Docker, schemat bazy z RLS | ✅ zakończona, **potwierdzona przez Patryka** (Docker Desktop, Mac M1) |
| 3 | Konta: rejestracja, e-mail, sesje, urządzenia, reset hasła, 2FA, izolacja | ✅ zakończona, **potwierdzona** (10/10 kroków) |
| 4a | Gabinety, ustawienia, katalog i silnik NFZ | ✅ **potwierdzona** |
| 4b | Opisy NFZ | ✅ **potwierdzona** |
| 4c | Opisy prywatne | ✅ **potwierdzona** |
| 4d | Zarobki, statystyki, CSV | ✅ **potwierdzona** |
| 4e-1 | Kalendarz | ✅ zbudowana i przetestowana automatycznie; osobnego potwierdzenia Patryka w `POSTEP.md` brak (używany w teście 7-dniowym) |
| 4e-2 | Import „Kopii całości” ze starej aplikacji | ✅ zbudowana, testy automatyczne |
| „Sekcja 5” specyfikacji (5.1–5.7) | funkcje aplikacji | ✅ zrealizowana (przegląd w `AUDYT_SAAS.md`) |
| 5 | Licencje, Stripe test, panel admina | ⏸ **odłożona bez terminu (decyzja 9)** |
| 6 | Testy funkcjonalne, bezpieczeństwa, wydajności | ⏳ częściowo (testy automatyczne są; testy bezpieczeństwa/wydajności – w etapie „zabezpieczenie”) |
| 7 | Konfiguracja produkcyjna bez uruchamiania | ⏳ nie rozpoczęta |
| 8 | Ceny, plan, ryzyka → pytanie o zgodę | ⏳ nie rozpoczęta |
| 9 | Wdrożenie (hosting) – tylko po zgodzie | ⏳ nie rozpoczęta |

**B. Aktualna kolejność (decyzja 9, 20.11.2026) – obowiązuje:**

| # | Etap | Stan |
|---|---|---|
| 0 | **Test 7 dni** na Macu Patryka (wersja testowa: instalator + aplikacja „Gabinet”) | **w toku** – instalator działa; 21.11 Patryk zgłosił pierwsze zmiany (zrealizowane, sekcja 4) |
| 1 | Podsumowanie testów (błędy, poprawki, co zostało, gotowość) | czeka na koniec testu |
| 2 | Dyktowanie: okno „Notatka” + parser w przeglądarce (notatka nie trafia na serwer) | nie rozpoczęte; wybór silnika (MacWhisper / Claude / Ollama) – osobna decyzja i koszty |
| 3 | Kompleksowe zabezpieczenie: ochrona kodu, autorstwa i IP, backend/API, logowanie, dane, ataki, kopie **+ audyt i testy bezpieczeństwa** (hardening) | nie rozpoczęte |
| 4 | Konfiguracja produkcyjna **bez uruchomienia** (serwer, domena, certyfikaty, kopie, monitoring) | nie rozpoczęte |
| 5 | Koszty i zgoda (≤ 30 USD/mies., plan migracji, pytanie o zgodę – dokładne brzmienie w `CLAUDE.md`) | nie rozpoczęte |
| 6 | Hosting (planowany Hetzner) – **tylko po wyraźnej zgodzie** | nie rozpoczęte |

> Prośba Patryka mówiła o „planie etapów 5–9”. W numeracji A fazy 5–9 to: licencje (odłożone), testy, konfiguracja produkcyjna, koszty/zgoda, wdrożenie. W numeracji B to samo odpowiada etapom 3–6 (plus dyktowanie jako 2). **Nie mam pewności, którą numerację Patryk chce dalej stosować → pytanie otwarte nr 10.**

## 2. Co działa (sprawdzone testami 21.11.2026, przy `97165c3`)

| Test | Wynik |
|---|---|
| `npm run typecheck`, `npx next build`, `npm audit --omit=dev` | bez błędów, 0 podatności |
| Vitest (`tests/*.test.ts`) | 39/39 (z bazą; netto policzone ręcznie i zgodne co do grosza) |
| Izolacja SQL (`db/test_izolacja.py`) | 73/73 |
| Przeglądarka (`tests/e2e`, z porównaniem ze starą aplikacją `OPISY_DIR`) | konta 72, 4a 33, 4b 69, 4c 32, 4d 32, 4e 50, 4f 11, 4g 30, przyciski 10, zmiany 41 – 0 błędów |

Funkcje: konta i bezpieczeństwo, Gabinety, Ustawienia NFZ, Katalog NFZ, Opisy NFZ (tekst = stara aplikacja), Opisy prywatne (cenniki per gabinet), Kalendarz (rozliczenia, ZUS, podatek, terminy, porównanie form = stara aplikacja), Zarobki (brutto/netto, zarobek lekarza i na godzinę z Kalendarza, wykres, średnie, dni tygodnia, poprzedni okres, filtry, CSV), import ze starej aplikacji, synchronizacja między urządzeniami z pracą offline, kopie bazy na Macu.

**Nie sprawdzone przez Claude:** budowa obrazu i uruchomienie w Docker Desktop (Docker Hub zablokowany w środowisku czatu) – to sprawdza Patryk na Macu. Zmiany z 21.11 nie były jeszcze uruchomione na Macu.

## 3. Niedokończone, znane błędy i obejścia

| # | Sprawa | Obejście / co zrobić |
|---|---|---|
| 1 | ~~Commit `97165c3` niewysłany na GitHub~~ | załatwione: wysłany 21.11.2026 |
| 2 | Konta, które zapisały ustawienia Kalendarza **przed** poprawką K23, mogą mieć fikcyjne gabinety „Gabinet 1–4” (30% po kosztach) | ręcznie usunąć w „Gabinety”; automatycznie nie usuwamy (usuwanie danych – tylko za zgodą) |
| 3 | Konto Patryka na Macu ma stare ustawienia podatków (JDG od 10.2026, ZUS 800 zł, skala 2026 → ryczałt 2027) | Patryk wybrał „wyczyścić”: po aktualizacji Kalendarz → Ustawienia → „Ustaw od nowa (wyczyść)” → kreator |
| 4 | Ponowna rejestracja z tym samym e-mailem (po usunięciu konta) → konto **bez dostępu** (rejestr triali HMAC: trial raz na e-mail, brak subskrypcji) | do decyzji – pytanie 2 |
| 5 | Treść opisów i inicjały tylko w przeglądarce – wyczyszczenie danych witryny / utrata urządzenia = utrata treści (kwoty i kody zostają) | Konto → „Kopia danych z tego urządzenia” (.json z hasłem) |
| 6 | Netto to **szacunek** (podatek i progi rozlicza się rocznie); dotyczy tylko zarobku lekarza z Kalendarza; kwoty z wizyt i CSV są brutto | opisane w aplikacji |
| 7 | Parametry 2027 w Kalendarzu (przeciętne wynagrodzenie, prognoza) to szacunki | zaktualizować po komunikatach GUS/ZUS (oznaczone „szacunek”) |
| 8 | Testy wymagają Linuksa (ścieżki Postgresa i Chrome), `OPISY_DIR` (klon `opisy-nfz`) i `DATABASE_URL` dla vitest | patrz `CLAUDE.md` §3 |
| 9 | Lint nie skonfigurowany | opcjonalnie później |
| 10 | Gatekeeper macOS blokuje dwuklik `.command` | `bash zainstaluj-mac.command` w Terminalu |
| 11 | Skrypty Windows (`uruchom-windows.bat`, `zatrzymaj-windows.bat`) – z fazy 2, nieaktualizowane przy wersji „tylko Mac” | nie używać do testu; ewentualnie usunąć za zgodą |
| 12 | `tests/e2e/__pycache__/*.pyc` śledzony w git | usunąć z repo i dodać do `.gitignore` (za zgodą) |
| 13 | `mailpit` w `docker-compose.yml` z tagiem `:latest` | przypiąć wersję w etapie zabezpieczenia |
| 14 | 2FA: włączanie wyłączone (`MFA_ENROLL`), konta z 2FA nadal logują się kodem | przywrócić przed produkcją? – w etapie zabezpieczenia |
| 15 | Opinia prawna (RODO, status wyrobu medycznego MDR, regulamin) | przed sprzedażą, nie przed budową |

## 4. Decyzje projektowe (i dlaczego)

| # | Data | Decyzja | Dlaczego |
|---|---|---|---|
| 1 | 16.11 | W chmurze **bez treści opisów**: procedury, kody, kwoty, data, gabinet; inicjały usunięte | treść + data + gabinet mogłyby zidentyfikować pacjenta (dane o zdrowiu, art. 9 RODO) |
| 2 | 16.11 | Szyfrowanie po stronie serwera (baza, transmisja, RLS) + reset hasła e-mailem | szyfrowanie end-to-end uniemożliwiłoby reset hasła bez utraty danych |
| 3 | 16.11 | Kalendarz od razu w fazie 4 | to część aplikacji (przychody, ZUS, podatki); nie usuwamy funkcji bez zgody |
| 4 | 16.11 | Claude buduje i testuje, Patryk testuje gotowe wersje (Docker Desktop + jedna komenda) | Patryk nie pracuje w terminalu |
| 5 | 16.11 | Faza 4 w etapach 4a–4e, test po każdym | mniejsze ryzyko, łatwiejsze sprawdzanie |
| 6 | 16.11 | Zestawienia w ramach jednego konta (1 konto = 1 lekarz); „zespół” nie w tej wersji | prostota, izolacja |
| 7 | 16.11 | Własne kody NFZ – tak, z oznaczeniem „niesprawdzane przez zasady NFZ” | ominęłyby reguły NFZ |
| 8 | 16.11 | Kolejność: sekcja 5 → wersja na 7 dni na Macu → testy → zabezpieczenia → (hosting po zgodzie) | najpierw użyteczność i test w praktyce |
| 9 | 20.11 | Licencje, płatności (Stripe) i panel admina **odłożone bez terminu**; kolejność test → podsumowanie → dyktowanie → zabezpieczenie → konfiguracja → koszty i zgoda → hosting | teraz niepotrzebne |
| – | 16.11 | Generatory (NFZ, prywatne, Kalendarz) przeniesione **1:1** przez skrypt z opisanymi poprawkami, nie pisane od nowa | przepisanie groziłoby różnicami w opisach i obliczeniach; zgodność sprawdzana testami ze starą aplikacją |
| – | 16.11 | Treść opisów na urządzeniu, zaszyfrowana kluczem urządzenia; serwer odrzuca dodatkowe pola | realizacja decyzji 1 |
| – | 16.11 | Konflikty: wizyty – nowszy czas zmiany wygrywa + znaczniki usunięcia; Kalendarz i materiały – kontrola wersji + scalanie trójstronne | praca na kilku urządzeniach i offline |
| – | 16.11 | Kod generatorów poza katalogiem publicznym – tylko dla zalogowanych | ochrona pracy autorskiej |
| – | 21.11 | Zarobek lekarza w Zarobkach = z **odbytych dyżurów w Kalendarzu** wg zasad gabinetu (wariant A); zarobek na godzinę = zarobek ÷ godziny dyżurów | jedno źródło zasad rozliczenia |
| – | 21.11 | Usunięte z interfejsu: „Sprawdź wycenę”, „Własne kody” (dane w bazie zostają) | uproszczenie (prompt Patryka) |
| – | 21.11 | 2FA: włączanie wyłączone; migracja 0007: wersja testowa bez limitu czasu | uproszczenie testu |
| – | 21.11 | Nazwa modelu „% po odjęciu kosztów własnych” (K13) | czytelność |
| – | 21.11 | **Netto wg ustawień Kalendarza** (wariant A) – ten sam silnik co Kalendarz uruchamiany na serwerze | spójność; brak wymyślonych stawek |
| – | 21.11 | Kalendarz **bez założeń o użytkowniku**: domyślnie pusty start JDG, brak formy i ZUS, zero gabinetów; kreator „Ustaw podatki i ZUS”; „Ustaw od nowa” z potwierdzeniem | wcześniejsze domyślne były ustawione pod Patryka |

**Niespójność w dokumentach:** `docs/AUDYT_SAAS.md` (decyzja 9) mówi, że okres próbny 3 mies. „zostaje bez zmian”; migracja **0007 (21.11, nowsza)** usunęła limit czasu na prośbę Patryka. **Aktualne jest 0007.**

## 5. Odłożone na później

| Temat | Stan i warunki |
|---|---|
| Licencje / płatności (Stripe) / panel admina | odłożone bez terminu (decyzja 9); dziś tylko okres próbny bez limitu (0007) |
| Treść opisów w chmurze | osobna analiza i zgoda; opcje: (A) kopia zaszyfrowana kluczem znanym tylko użytkownikowi (reset hasła = utrata kopii), (B) treść na serwerze (art. 9 RODO: umowa powierzenia, rejestr czynności, ocena skutków, opinia prawnika) |
| Dyktowanie głosowe (Whisper) | etap 2: okno „Notatka” + parser w przeglądarce; silnik: MacWhisper (lokalnie) / Claude / Ollama – decyzja i koszty przed wdrożeniem; notatka nie trafia na serwer |
| Hosting Hetzner | etapy 4–6; ≤ 30 USD/mies.; tylko po zgodzie (dokładne pytanie w `CLAUDE.md`) |
| Audyt bezpieczeństwa / hardening | etap 3 (ochrona kodu i IP, API, logowanie, dane, ataki, kopie, testy bezpieczeństwa) |
| Funkcja „zespół” (kilku lekarzy w koncie) | poza tą wersją (decyzja 6) |
| Netto dla kwot z wizyt i w CSV | nie robione (Kalendarz nie liczy netto od wizyt) |

## 6. Plan kolejnych kroków
1. Zaktualizować wersję na Macu (`bash zainstaluj-mac.command` z najnowszego kodu z GitHuba).
2. Patryk: Kalendarz → „Ustaw od nowa” → kreator; dokończyć **test 7-dniowy** i zgłaszać uwagi.
3. Podsumowanie testu (etap 1): lista błędów, poprawki, gotowość.
4. Dyktowanie (etap 2) – po decyzji o silniku i kosztach.
5. **Hardening i audyt bezpieczeństwa** (etap 3), m.in.: przypięcie obrazów Dockera, decyzja o 2FA, nagłówki/CSP, limity, kopie i odtwarzanie, testy prób obejścia uprawnień, wydajność (20 równoczesnych użytkowników), aktualizacja instrukcji.
6. Konfiguracja produkcyjna bez uruchomienia (etap 4) → koszty i pytanie o zgodę (etap 5) → hosting tylko po zgodzie (etap 6).

## 7. Pytania otwarte do Patryka
1. ~~Przeniesienie: push czy ZIP?~~ – rozstrzygnięte: push (21.11.2026); `CLAUDE.md` i `HANDOFF.md` dodane do repo.
2. Ponowna rejestracja tym samym e-mailem daje konto bez dostępu – zostawić (ochrona przed wielokrotnym trialem) czy dawać dostęp, skoro wersja testowa jest bez limitu?
3. Fikcyjne „Gabinet 1–4” na kontach sprzed K23 – usuwać automatycznie (migracja, za zgodą) czy ręcznie?
4. **Własne kody NFZ:** w `CLAUDE.md` jest zasada „oznaczane jako niesprawdzane” (decyzja 7), ale 21.11 zakładka została ukryta. Przywrócić (z oznaczeniem) czy zostawić ukrytą?
5. Dyktowanie: który silnik (MacWhisper lokalnie / Claude / Ollama) i jaki budżet?
6. Docelowy model licencji (trial, roczna, dożywotnia) – kiedy wracamy do tematu?
7. Zgoda na aktualizację nieaktualnych instrukcji (`INSTRUKCJA_OBSLUGI.md`, `INSTRUKCJA_START.md`, `README.md`) i usunięcie `__pycache__` / skryptów Windows?
8. 2FA: przywrócić włączanie przed produkcją?
9. Wyniki testu 7-dniowego – lista uwag do podsumowania.
10. Którą numerację etapów stosować dalej: fazy 1–9 (audyt) czy etapy 0–6 (decyzja 9)?

### Odpowiedzi Patryka (21.11.2026, Claude Code)

| # | Odpowiedź | Stan |
|---|---|---|
| 2 | **Dawać dostęp** przy ponownej rejestracji | zrobione: każde nowe konto dostaje wersję testową; rejestr HMAC nadal zapisywany (na ewentualny powrót licencji). Konta zarejestrowane ponownie przed poprawką nadal nie mają subskrypcji. |
| 3 | Fikcyjne „Gabinet 1–4” – **ręcznie** | Patryk usuwa w „Gabinety” |
| 4 | Własne kody NFZ – **zostają ukryte** | bez zmian |
| 5 | Dyktowanie – **odłożone** | przed etapem 2 porównanie (koszt, jakość PL, prywatność) |
| 6 | Licencje – **bez terminu** | jak decyzja 9 |
| 7 | Porządki – **wszystko** | zrobione: 3 instrukcje zaktualizowane, `__pycache__` usunięty z repo i w `.gitignore`, skrypty Windows usunięte |
| 8 | 2FA – **zostaje wyłączone** | przypomnieć przed hostingiem |
| 9 | Test 7-dniowy – **w toku** | czekamy na uwagi |
| 10 | Numeracja – **etapy 0–6** (decyzja 9) | obowiązuje |
| 11 | Test `t_6_zmiany.py` przerywał się po 36/41 (konto bez `bypass_csp`) | naprawiony (`9f107e8`) |

## 8. Narzędzia dla Claude Code (ustalone z Patrykiem 21.11.2026)

Zasada: narzędzia uruchamiane **lokalnie, bez wysyłania danych na zewnątrz**; instalowane poza repo (bez dopisywania do `package.json`) – stałe dodanie do repo tylko za zgodą. Przy konflikcie instrukcji wtyczki z `CLAUDE.md` wygrywa `CLAUDE.md`.

| Narzędzie | Do czego | Etap (numeracja 0–6) |
|---|---|---|
| Context7 | aktualna dokumentacja Next.js 16 / React 19 zamiast pisania z pamięci | każdy |
| `/code-review` (wbudowany) + wtyczka `code-review` | przegląd zmian przed PR | każdy |
| wtyczka `playwright` | ręczne „przeklikanie” aplikacji, odtwarzanie zgłoszeń Patryka, zrzuty | 0–1 |
| `engineering:debug` | szukanie przyczyny przy zgłoszeniach | 0–1 |
| `engineering:architecture` | decyzja o silniku dyktowania (porównanie opcji) | 2 |
| `security-review`, `engineering:testing-strategy`, shellcheck, gitleaks, ESLint, semgrep/osv-scanner, axe-core + Lighthouse, autocannon/k6 | audyt i testy bezpieczeństwa, dostępności, obciążenia (20 użytkowników) | 3 |
| `engineering:deploy-checklist`, `operations:runbook`, hadolint | konfiguracja produkcyjna, kopie i odtwarzanie, `Dockerfile` | 4 |
| `operations:risk-assessment` | ryzyka przed pytaniem o zgodę | 5 |
| wtyczka `frontend-design` | tylko nowe ekrany (np. okno „Notatka”); istniejący wygląd i moduły 1:1 bez zmian | 2+ |

**Nie używać w Gabinecie:** `product-tracking-skills` (analityka wysyła dane na zewnątrz), `brightdata` (zewnętrzna usługa). Wyłączone: `superpowers` (wymusza skille przy każdej odpowiedzi), `github` z marketplace (wymaga tokena; wystarcza wbudowany dostęp do GitHuba). Wtyczki instalowane w sesji znikają z kontenerem – na stałe tylko w ustawieniach konta.

**Ograniczenia środowiska w chmurze:** pobieranie gotowych programów z GitHub Releases (np. gitleaks) zablokowane przez kontrolę uprawnień; Docker Hub zablokowany (ZAP, Trivy, budowa obrazu – tylko na Macu).

### Pierwszy raport (21.11.2026, `main` @ `dd29862`, tylko odczyt)

| Sprawdzenie | Wynik |
|---|---|
| shellcheck 0.9.0 (8 skryptów `.sh`/`.command`) | **0 błędów**, 6 ostrzeżeń, 11 uwag stylu. Ostrzeżenia: `tests/e2e/uruchom.sh` (`cd` bez `|| exit`, brak cudzysłowów przy `$(cat $PIDF)`, nieużyta zmienna pętli); `zainstaluj-mac.command:24` (`ls … </dev/null` – celowe, poprawka `f37b14a`; fałszywy alarm), `:90` (nieużyta zmienna pętli). Nic krytycznego – do ewentualnej poprawki w etapie 3. |
| Sekrety w historii git (28 commitów; zamiast gitleaks – wyszukiwanie wzorców: klucze prywatne, tokeny GitHub/Stripe/AWS, 64-znakowe klucze hex przypisane do `AUTH_SECRET`/`APP_ENC_KEY`/haseł) | **nic nie znaleziono**; w historii tylko `.env.example` z tekstami zastępczymi. Drobiazg: komentarz w `.env.example` wspomina „skrypty uruchom-*” (dziś `zainstaluj-mac.command`). |

## 9. Prompt „Rozwój aplikacji Gabinet” (21.11.2026) – stan i decyzje Patryka

Treść promptu: 7 etapów (materiały, automatyzacja formularzy, zarobki i rozliczenia, wygląd, opisy prywatne, generowanie opisów, badanie). Zasady promptu: etapami, testy po każdym, bez zmian architektury bez zgody, `POSTEP.md` / `CLAUDE.md` / `docs/AUDYT_SAAS.md` tylko za zgodą.

### Zrobione (PR #4, `main` @ `d8b9426`)
| Pkt | Zmiana |
|---|---|
| 1.1 | lakiery: Duraphat (Colgate), Fluor Protector (Ivoclar), Elmex gelée (żel fluorkowy – to nie lakier) obok VOCO Profluorid; 1006 – opcjonalny preparat w opisie (P20–P22) |
| 3.1 | Opisy NFZ: dolny pasek bez kwot (P8–P10) |
| 3.2 | Statystyki NFZ: bez kolumn „Z punktów” i „Z przeglądów” (P14–P19) |
| 3.3 | Zarobki: kwota z rozliczenia gabinetu (Kalendarz → Rozliczenia) zamiast sumy z dyżurów – jak `monthCalc` w Kalendarzu, tylko pełne miesiące, brutto i netto (`kal.ts`, `kal-silnik.ts`) |
| 3.4 | sprawdzone: gabinety już są jednym rekordem (UUID) – bez zmian |
| 4.1/4.2 | jeden wygląd: `GBar` na stronach aplikacji, Kalendarz K39 (tylko CSS) |
| 5 | Opisy prywatne: brak treści na urządzeniu → komunikat zamiast „Wczytuję…” (R7–R7c); pomiar startu: 1500 wizyt < 0,3 s |
| 7.1 / 7.2 | uraz: „nagryzienie na twardy przedmiot” (P11); niepewne rokowanie – opcja pełna/krótka, domyślnie nic (P12–P13) |

### Do zrobienia – decyzje Patryka (pytania do klikania, 21.11.2026)
| Pkt | Decyzja |
|---|---|
| 1.2 materiały | lista „wybierz albo wpisz własny”, zapisana **na koncie**, w polach: nazwa kompozytu (NFZ), lakier fluorkowy (NFZ), materiał podkładowy (zamiast stałego „Ionosit”), materiały w Opisach prywatnych; zarządzanie: sekcja „Moje materiały” na stronie **Ustawienia**; zmiana API: nowy klucz ustawień z walidacją, **bez migracji** |
| 2.1 wędzidełka | oba domyślnie „Typ I – śluzówkowy” |
| 2.1 wywiad | przycisk „wywiad bez obciążeń” (brak alergii, chorób, leków naraz; nie nadpisuje wpisanych) + wyraźne pole „aktualne leki”; dane tylko w treści opisu na urządzeniu |
| 6.1 podsumowanie | na górze opisu, **domyślnie włączone**, wyłącznik w Ustawieniach; forma: „Wykonano: badanie kontrolne, usunięcie złogów (½ łuku), wypełnienie zęba 36 (MO).” (NFZ i prywatne) |
| 6.2 dolegliwości | 5 przycisków: ból samoistny · ból na zimno/ciepło · ból przy nagryzaniu · nadwrażliwość · ukruszenie/złamanie zęba (lub wypełnienia); kilka naraz + własny wpis; Opisy prywatne: procedury zachowawcze, endo, konsultacje |
| 6.3 znieczulenie | przyciski: Dentocaine (artykaina), Mark3 20% benzokaina, bez znieczulenia, własny preparat; dawka domyślnie **1 amp. (1,7 ml)**, przyciski ½ / 2 amp. + własna; NFZ: wypełnienia (1105, 1108, 15xx), endo (1206), ST30; ekstrakcje ST01/ST02 bez zmian; prywatne: procedury zabiegowe |
| 6.4 trzy szybkie opcje | kolor, nazwa kompozytu, lakier, pola w prywatnych; „najczęstsze” liczone z historii na urządzeniu (na start – pierwsze z listy) |
| 6.5 zalecenia | przycisk „ustnie / ustnie i pisemnie”, **domyślnie „ustnie”**; prywatne: „Zalecenia przekazano pacjentowi w formie ustnej.” we wszystkich, z wyłączeniem przy wizycie |

**Skutek:** domyślny tekst opisów NFZ zmieni się (6.1, 6.5, 2.1) – testy porównawcze ze starą aplikacją dostosować: porównanie przy wyłączonych nowościach + osobne sprawdzenie nowych fragmentów.
**Kolejność:** 1.2 → 2.1 → 6.3 → 6.2 → 6.5 → 6.4 → 6.1; po każdym etapie testy; commit + PR po całości (Patryk scala).
