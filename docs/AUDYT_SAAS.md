# Gabinet SaaS – FAZA 1: audyt obecnego projektu i plan przebudowy

Data: 16.11.2026 · gałąź `saas` · podstawa: `main` @ `716689d` (połączona aplikacja na żywo)

Statusy jak w Twoim prompcie: **WDROŻONE** · **WYMAGA MOJEGO DZIAŁANIA** · **WYMAGA KONFIGURACJI ZEWNĘTRZNEJ** · **NIE WDROŻONO**.

---

## 1. Co jest dziś (fakty z kodu)

### 1.1 Struktura i uruchamianie
| Element | Stan |
|---|---|
| Typ aplikacji | statyczna strona (HTML + JavaScript, bez serwera, bez kroku build), GitHub Pages |
| Pliki | `index.html` (logowanie, strona główna), `nfz.html`, `prywatne.html`, `kalendarz.html`, `wspolne.js/css`, `szablony.js`, `prywatne-katalog.js` – razem ok. 7 800 wierszy |
| Zależności | brak bibliotek; jedyne zewnętrzne źródło: czcionki Google |
| Baza danych | **w przeglądarce** (IndexedDB), osobno na każdym urządzeniu |
| Konta | lokalne: hasło, kod odzyskiwania, blokada po bezczynności; bez e-maila, bez serwera |
| Szyfrowanie | AES-GCM 256 w przeglądarce (klucz z hasła, PBKDF2 600 000) – end-to-end |
| Synchronizacja | brak – tylko ręczna „kopia całości” (plik) |
| Testy | 17 plików, 439 sprawdzeń w prawdziwej przeglądarce (Chrome bez okna) |

### 1.2 Funkcje (zachowujemy wszystkie, chyba że zdecydujesz inaczej)
| Moduł | Funkcje |
|---|---|
| **Opisy NFZ** | 22 kody (Zarządzenie 95/2026/DSOZ), pytania i diagram zębów, plany wizyt I–IV, reguły NFZ (łączenie, limity, minimalny czas), wycena punktowa (1,84 zł/pkt, 350 zł/h przeglądów, +10 min), edycja tekstu, ulubione/ukryte kody, zestawy kodów, stałe teksty z wersjami, historia, statystyki z wykresami, kopia zapasowa |
| **Opisy prywatne** | 19 szablonów, edytor szablonów z wersjami, własne procedury, cennik dla każdego gabinetu (cena, % lub kwota, koszty lab.), zestawy, ulubione, szybka wizyta, historia, zarobki (okresy, gabinety, rodzaje), CSV, druk |
| **Kalendarz** (dawny Grafik) | dyżury w gabinetach, rozliczenia (% obrotu po lab., stawka godzinowa/dzienna), podsumowanie, terminy ZUS/podatków, porównanie form opodatkowania, eksport |
| **Wspólne** | strona główna z oknem „Zarobki – wszystkie gabinety”, podpowiedź obrotu w dyżurze, kopia całości |

### 1.3 Co jest wartościowe do przeniesienia
| Element | Dlaczego ważny | Jak przenieść |
|---|---|---|
| Silnik NFZ (`D`, `PTS`, reguły, kalkulacje) | sprawdzony testami regresji, źródła DSOZ | wydzielić do modułu TypeScript bez zmiany logiki; testy porównawcze stara ↔ nowa wersja |
| Silnik szablonów prywatnych (`{pole}`, `{?pole}…{/pole}`) | prosty, przetestowany | moduł TypeScript, ten sam format szablonów |
| `szablony.js` (teksty gabinetu) | Twoje treści | dane startowe katalogu |
| Obliczenia kwot (grosze, zaokrąglenia) | wyrocznia Decimal w testach | 1:1 + te same testy |
| Kalendarz (rozliczenia, ZUS, podatki) | duża logika, działa | etap późniejszy (decyzja 3) |
| Testy (scenariusze) | opisują oczekiwane zachowanie | przepisać na Playwright w TypeScript |

---

## 2. Rozbieżności między obecnym projektem a nowymi wymaganiami

| # | Wymaganie z promptu | Stan obecny | Skutek |
|---|---|---|---|
| R1 | **Brak danych pacjentów** | wizyty mają **inicjały pacjenta**, wiek, numery zębów, rozpoznania i pełną treść opisu z datą i gabinetem | w chmurze: inicjały **usuwamy**; treść opisu z datą + gabinetem + lekarzem może pozwolić zidentyfikować pacjenta (dana o zdrowiu, art. 9 RODO) → **decyzja 1** |
| R2 | Centralna baza, synchronizacja, reset hasła e-mailem, panel admina | szyfrowanie end-to-end: serwer nie mógłby czytać danych; reset e-mailem = utrata danych | trzeba wybrać model szyfrowania → **decyzja 2** |
| R3 | Prompt nie wymienia Kalendarza | Kalendarz jest częścią aplikacji (przychody, ZUS, podatki) | nie usuwam bez zgody → **decyzja 3** |
| R4 | Next.js, TypeScript, PostgreSQL, Docker | czysty HTML/JS bez serwera | przebudowa techniczna; logikę przenosimy, nie piszemy od nowa |
| R5 | „Dodawanie własnych procedur” także NFZ | celowo nie zrobione (ominęłyby reguły NFZ) | robię z oznaczeniem „niesprawdzane przez zasady NFZ”, punkty wpisuje użytkownik |
| R6 | „Zestawienia według inicjałów lekarza lub użytkownika” | dziś każdy użytkownik widzi tylko siebie | rozumiem jako statystyki **w ramach konta** (np. kilku lekarzy w jednym koncie = osobna funkcja „zespół”, nie w tej wersji) – do potwierdzenia |
| R7 | Środowisko lokalne „na moim komputerze” | Ty nie pracujesz w terminalu | buduję i testuję u siebie; Ty uruchamiasz wersję próbną jednym programem → **decyzja 4** |
| R8 | Aplikacja wspiera dokumentację medyczną | generator proponuje treść wpisu | do sprawdzenia prawnego: czy oprogramowanie nie jest wyrobem medycznym (MDR) – moim zdaniem nie (nie diagnozuje, nie leczy), ale przed sprzedażą komercyjną potrzebna opinia prawnika |

---

## 3. Proponowana architektura (Etap A – lokalnie)

| Warstwa | Wybór | Uzasadnienie |
|---|---|---|
| Aplikacja | **Next.js (App Router) + TypeScript** | Twój wybór; jeden projekt dla interfejsu i API |
| Baza | **PostgreSQL 16** z **Row Level Security** | izolacja użytkowników po stronie bazy, nie tylko w kodzie |
| Dostęp do bazy | Drizzle ORM + zapytania parametryzowane | ochrona przed SQL injection, migracje w Git |
| Konta | własny moduł: hasła Argon2id, sesje w bazie (ciasteczko HttpOnly, Secure, SameSite), lista urządzeń, wylogowanie wszystkich, weryfikacja e-mail, reset hasła, TOTP (MFA) opcjonalnie | pełna kontrola, brak zewnętrznej usługi kont |
| E-mail (lokalnie) | Mailpit (podgląd e-maili w przeglądarce) | testy bez wysyłania prawdziwych wiadomości |
| Płatności | Stripe w trybie testowym (webhooki z podpisem, idempotencja) | sprawdzę aktualną obsługę BLIK/Przelewy24 przed fazą 5 |
| Interfejs | obecny wygląd (IBM Plex, kolory teal) przeniesiony do komponentów; PWA | zachowujemy to, co znasz |
| Uruchamianie | **Docker Compose**: aplikacja + PostgreSQL + Mailpit + Caddy | lokalnie to samo co później na Hetznerze |
| Testy | Vitest (logika, NFZ, kwoty) + Playwright (przeglądarka) + testy izolacji kont (próby odczytu cudzych danych przez API i URL) | przenosimy dzisiejsze scenariusze |

### 3.1 Baza danych – szkic (szczegóły z relacjami, typami, indeksami i politykami RLS przedstawię przed utworzeniem – FAZA 2)
`profiles`, `sessions`, `email_tokens`, `procedure_categories`, `procedures` (+ `procedure_versions`), `procedure_sets`, `procedure_set_items`, `clinics`, `price_lists`, `saved_descriptions` (wg decyzji 1), `earnings_entries`, `user_settings`, `subscriptions`, `payments`, `payment_events` (idempotencja webhooków), `audit_logs`, `security_events`; dla Kalendarza (decyzja 3): `shifts`, `tax_settings`.
Każda tabela danych użytkownika: `owner_id` + polityka RLS `owner_id = current_user_id`. Brak tabel pacjentów.

---

## 4. Plan przebudowy (fazy z Twojego promptu)

| Faza | Zakres | Wynik do sprawdzenia przez Ciebie |
|---|---|---|
| 1 | **Audyt i plan** (ten dokument) | Twoje decyzje 1–4 |
| 2 | Projekt Next.js, Docker, schemat bazy z RLS (najpierw przedstawię tabele) | akceptacja schematu |
| 3 | Rejestracja, e-mail, logowanie, sesje, urządzenia, reset hasła, MFA, testy izolacji | konto testowe w wersji próbnej |
| 4 | Generator NFZ i prywatny, procedury, zestawy, cenniki, autozapis z synchronizacją i konfliktami, historia, statystyki z wykresami; import danych z obecnej aplikacji (bez inicjałów) | porównanie z obecną aplikacją |
| 5 | Licencje (trial 3 mies., roczna, lifetime, statusy po stronie serwera), Stripe test, panel administratora z dziennikiem audytu | test zakupu w trybie testowym |
| 6 | Testy funkcjonalne, bezpieczeństwa (próby obejścia uprawnień), synchronizacji, wydajności (20 równoczesnych użytkowników) | raport testów |
| 7 | Konfiguracja produkcyjna, kopie zapasowe, odtwarzanie, monitoring – **bez uruchamiania** | plan wdrożenia |
| 8 | Aktualne ceny Hetznera/domeny/Stripe/e-maila, plan, ryzyka → **pytanie o zgodę** | Twoja decyzja |
| 9 | Wdrożenie – tylko po zgodzie | – |

Obecna aplikacja na GitHub Pages działa dalej bez zmian przez cały Etap A.

---

## 5. Statusy po FAZIE 1

| Pozycja | Status |
|---|---|
| Audyt obecnego projektu | **WDROŻONE** (ten dokument) |
| Plan przebudowy | **WDROŻONE** – czeka na decyzje |
| Decyzje 1–4 (dane, szyfrowanie, Kalendarz, środowisko) | **WYMAGA MOJEGO DZIAŁANIA** (Twojego) |
| Opinia prawna: RODO (dokumenty), status wyrobu medycznego, regulamin sprzedaży | **WYMAGA KONFIGURACJI ZEWNĘTRZNEJ** (prawnik) – przed sprzedażą, nie przed budową |
| Konto Stripe (tryb testowy), konto Hetzner, domena | **WYMAGA MOJEGO DZIAŁANIA** – dopiero w fazach 5 i 8 |
| Wszystko z faz 2–9 | **NIE WDROŻONO** |

---

## 6. Decyzje Patryka (16.11.2026)

| # | Decyzja |
|---|---|
| 1 | W chmurze **bez treści opisów**: procedury, kody, kwoty, data, gabinet. Inicjały pacjentów usunięte. |
| 2 | Szyfrowanie **po stronie serwera** (baza, transmisja, RLS); reset hasła e-mailem. |
| 3 | **Kalendarz od razu** – w fazie 4 razem z resztą. |
| 4 | Buduję i testuję u siebie; Patryk testuje gotowe wersje (Docker Desktop + jedna komenda). |

Projekt bazy: `saas/db/SCHEMAT_BAZY.md` (czeka na akceptację przed utworzeniem bazy aplikacji).

### Decyzje Patryka przed fazą 4 (16.11.2026)
| # | Decyzja |
|---|---|
| 5 | Faza 4 w etapach 4a–4e (4a: gabinety, ustawienia, katalog i silnik NFZ; 4b: Opisy NFZ; 4c: Opisy prywatne; 4d: zarobki, statystyki, synchronizacja; 4e: Kalendarz i import), test po każdym. |
| 6 | R6: zestawienia **w ramach jednego konta** (konto = jeden lekarz; podział wg gabinetu, okresu, rodzaju zabiegu). Funkcja „zespół” – nie w tej wersji. |
| 7 | R5: własne procedury NFZ **tak**, z widocznym oznaczeniem „niesprawdzane przez zasady NFZ”; punkty wpisuje użytkownik; reguły łączenia i limitów NFZ ich nie obejmują. |

### Zmiana kolejności prac (Patryk, 16.11.2026, decyzja 8)
| Etap | Zakres | Stan |
|---|---|---|
| 1 | Dokończenie sekcji 5 specyfikacji (FUNKCJE APLIKACJI 5.1–5.7). Licencje i płatności (sekcje 8–9), panel administratora (10) – **odłożone bez terminu (decyzja 9)**. | zrealizowane (przegląd niżej) |
| 2 | Wersja do 7 dni pracy **tylko na Macu Patryka**: Docker + aplikacja „Gabinet”, automatyczne kopie bazy, kopia treści z urządzenia, instrukcja obsługi | zrealizowane |
| 3 | 7 dni testów Patryka, poprawki zgłoszeń, podsumowanie | czeka na Patryka |
| 4 | Kompleksowe zabezpieczenie (kod, autorstwo, backend/API, uwierzytelnianie, dane, ataki, kopie) + audyt i testy bezpieczeństwa | po etapie 3 |
| 5 | Hosting i publikacja – **tylko po wyraźnej zgodzie**, z wcześniejszą specyfikacją, kosztami i planem migracji | odłożony |

#### Decyzja 9 (Patryk, 20.11.2026): kolejność dalszych prac, licencje i płatności odłożone
| # | Etap | Zakres |
|---|---|---|
| 0 | Test 7 dni | praca Patryka, poprawki zgłoszeń |
| 1 | Podsumowanie testów | błędy, poprawki, co zostało, gotowość |
| 2 | Dyktowanie | okno „Notatka” + parser w przeglądarce (notatka nie trafia na serwer); MacWhisper / Claude / Ollama – osobna decyzja (decyzja 1, koszty) |
| 3 | Kompleksowe zabezpieczenie | ochrona kodu, autorstwa i IP, backend/API, logowanie, dane, ataki, kopie + audyt i testy bezpieczeństwa |
| 4 | Konfiguracja produkcyjna (bez uruchomienia) | serwer, domena, certyfikaty, kopie, monitoring – przygotowane, nie włączone |
| 5 | Koszty i zgoda | specyfikacja, koszt (≤ 30 USD/mies.), plan migracji, pytanie o zgodę |
| 6 | Hosting | tylko po wyraźnej zgodzie |

**Licencje, płatności (Stripe) i panel administratora – odłożone bez terminu** (Patryk doda je w osobnym kroku). Nic z tego nie było zbudowane poza istniejącym okresem próbnym (3 miesiące od rejestracji, sprawdzany na serwerze) – ten mechanizm zostaje bez zmian, dopóki Patryk nie zdecyduje inaczej (bez zgody nie usuwamy funkcji).

#### Decyzje Patryka 21.11.2026 (pytania otwarte z HANDOFF.md §7)
| # | Decyzja |
|---|---|
| 10 | Ponowna rejestracja tym samym e-mailem daje dostęp (wersja testowa); rejestr HMAC zostaje na ewentualny powrót zasady „okres próbny raz na e-mail”. |
| 11 | Fikcyjne „Gabinet 1–4” sprzed K23 – usuwane ręcznie, bez migracji. |
| 12 | Własne kody NFZ – zakładka zostaje ukryta (dane w bazie zostają). |
| 13 | Dyktowanie – wybór silnika odłożony; przed etapem 2 porównanie opcji. |
| 14 | Licencje – bez terminu (podtrzymanie decyzji 9). Okres próbny jest bez limitu czasu (migracja 0007, nowsza niż zapis przy decyzji 9). |
| 15 | 2FA – włączanie zostaje wyłączone. |
| 16 | Numeracja: obowiązują etapy 0–6 z decyzji 9. |

#### Przegląd sekcji 5 specyfikacji (stan 16.11.2026)
| Punkt | Wymaganie | Realizacja |
|---|---|---|
| 5.1 | Generator NFZ i prywatny, wybór i łączenie procedur, własne procedury, edycja, kopiowanie | Moduły 1:1 z obecnej aplikacji (testy: tekst = stara aplikacja); własne kody NFZ z oznaczeniem |
| 5.2 | Własna baza procedur: dodawanie, edycja, usuwanie, kategorie, wyszukiwanie, ulubione, kwoty, własne opisy | Opisy prywatne (katalog, kategorie, szukaj, ulubione, cennik, szablony) + Katalog NFZ; dane tylko w koncie (RLS) |
| 5.3 | Zestawy: zapis, nazwa, edycja, usuwanie, kolejność, kopiowanie, wstawianie | Opisy prywatne (zestawy: zup/zdown, zdup, zuse) i Opisy NFZ (zestawy kodów: setmv, setdup, setapply) |
| 5.4 | Cena, kwota lekarza, %, parametry; automatyczne wyliczenie | Cennik z % per gabinet, kwoty stałe, koszty; NFZ: punkty × stawka, udział 40/35%, przeglądy 350 zł/h |
| 5.5 | Autozapis, synchronizacja, odporność na odświeżenie, status, błędy połączenia, ochrona przed utratą, konflikty | Wizyty: nowszy czas zmiany wygrywa + znaczniki usunięcia; Kalendarz i materiały: **kontrola wersji + scalanie trójstronne** (dodane), kolejka offline, keepalive, status w pasku |
| 5.6 | Dzień/tydzień/miesiąc/rok, dni tygodnia, zestawienia wg lekarza, porównanie okresów, średnie, filtr dat i kategorii, wykresy, bez podwójnego liczenia | /zarobki: okresy, własny zakres, **dni tygodnia, średnie, poprzedni okres, filtr NFZ/prywatne/kategoria** (dodane), wykres, CSV; jedno źródło kwot (earnings_entries). „Wg lekarza” = konto (decyzja 6) |
| 5.7 | Historia: wyszukiwanie, filtr, przegląd, ponowne użycie, edycja, korekta, bez danych pacjentów | Historia w modułach (szukaj, filtry, otwórz/edytuj, użyj ponownie); na koncie bez inicjałów i treści |
| – | Import danych ze starej aplikacji (4e-2) | /import: „Kopia całości” + kopia z urządzenia (ten sam format) |
| – | Atrapy | „gabinet z dyżuru” (G.dayClinic) zwracał zawsze pusty wynik – naprawione; nieaktualne napisy „faza/etap” usunięte; test klikający wszystkie przyciski modułów (t_5_przyciski.py) |


### Etap 4b – rozwiązanie techniczne generatora NFZ (16.11.2026)
| Kwestia | Rozwiązanie |
|---|---|
| Przeniesienie generatora | Ten sam kod (`nfz.html`, `szablony.js`) z 7 opisanymi poprawkami (`generator/ZMIANY.md`, skrypt `tests/tools/przenies_generator.py`) – teksty i reguły bez zmian; zgodność sprawdzana testem (14 kombinacji wieku i planu: tekst identyczny co do znaku). Przepisanie na nowo groziłoby różnicami w opisach. |
| Treść opisu, odpowiedzi, wiek, inicjały | **Tylko na urządzeniu**, zaszyfrowane AES-GCM kluczem urządzenia (niewyciągalny CryptoKey w IndexedDB, osobny dla konta). Serwer ich nie otrzymuje – API odrzuca dodatkowe pola. |
| Chmura (decyzja 1) | Data, gabinet, kody, punkty, stawki z dnia zapisu, kwoty (do statystyk), czas wizyty, numer wpisu. |
| Inne urządzenie | Historia bez treści („Anonim #n”, kody, kwoty, „Edytuj kwoty”, „usuń”). |
| Konflikty | Nowszy czas zmiany wygrywa; usunięcie = znacznik czasu (starsze usunięcie nie kasuje nowszej zmiany). Praca bez internetu – wysyłka po powrocie połączenia. |
| Kod generatora | Poza katalogiem publicznym: strona i pliki tylko dla zalogowanych z licencją (ochrona pracy autorskiej). |
| Ograniczenie | Utrata urządzenia / wyczyszczenie danych przeglądarki = utrata treści opisów z tego urządzenia (kwoty i kody zostają w chmurze). Kopia zapasowa `.json` z generatora nadal działa. |

### Otwarta sprawa na później: treść opisów w chmurze (zgłoszona przez Patryka 16.11.2026)
Patryk chce w przyszłości przenieść treść opisów z przeglądarki do chmury (po uruchomieniu hostingu) – **osobny krok, nie teraz**.
Przed realizacją: osobna analiza i wyraźna zgoda (prompt: „nie dodawaj funkcji wymagających danych pacjentów bez osobnej analizy”).
Do porównania wtedy: (A) kopia treści zaszyfrowana na urządzeniu kluczem znanym tylko użytkownikowi (serwer nie odczyta; reset hasła = utrata kopii),
(B) przechowywanie treści na serwerze (dane o zdrowiu – art. 9 RODO: umowa powierzenia z hostingiem, rejestr czynności, ocena skutków, opinia prawnika).
