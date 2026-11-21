# CLAUDE.md – Gabinet (wersja SaaS)

Instrukcja dla Claude Code. Repozytorium **prywatne** (`86d8n52d6y-netizen/gabinet-saas`). Stan projektu, decyzje i plan: **`HANDOFF.md`**. Dziennik etapów: `POSTEP.md`. Audyt i decyzje 1–9: `docs/AUDYT_SAAS.md`. Projekt bazy: `db/SCHEMAT_BAZY.md`.

## 1. Cel aplikacji i dla kogo

Gabinet to aplikacja dla **lekarzy dentystów pracujących w kilku gabinetach** (głównie na kontraktach B2B / JDG). Pomaga:
- pisać opisy wizyt **NFZ** (kody, punkty, reguły NFZ) i **prywatnych** (szablony, cennik),
- planować dyżury w gabinetach i liczyć przychód, ZUS i podatek (**Kalendarz**),
- liczyć zarobki ze wszystkich gabinetów (**Zarobki**, raporty, CSV).

Właściciel: Patryk Barysz (lekarz dentysta). **Patryk nie jest programistą – Claude buduje, testuje i wyjaśnia; Patryk testuje gotowe wersje i podejmuje decyzje.**

Darmowa, starsza wersja (statyczna, bez serwera) jest w **publicznym** repo `opisy-nfz` na GitHub Pages – **z tego repo jej nie zmieniaj**.

## 2. Stack i architektura

| Warstwa | Technologia |
|---|---|
| Aplikacja | Next.js 16 (App Router, server components, server actions, route handlers), React 19, TypeScript (`strict`) |
| Baza | PostgreSQL 16, **FORCE Row Level Security** na każdej tabeli z danymi użytkownika, migracje SQL `db/migrations/NNNN_*.sql` (`scripts/migrate.mjs`) |
| Konta | własny moduł (`src/lib/auth/*`, `session.ts`, `password.ts`): Argon2id, sesje w bazie (ciasteczko HttpOnly), weryfikacja e-mail, reset hasła e-mailem, limity prób, 2FA TOTP (włączanie obecnie wyłączone – `MFA_ENROLL`) |
| Poczta lokalnie | Mailpit (`http://localhost:8025`) – nic nie wychodzi do internetu |
| Uruchomienie | Docker Compose: `db`, `migrate`, `app`, `kopie` (codzienna kopia bazy), `mailpit` |
| Testy | Vitest (`tests/*.test.ts`), testy izolacji SQL (`db/test_izolacja.py`), testy w przeglądarce Python + Playwright (`tests/e2e/t_*.py`) |

### Moduły

| Moduł | Gdzie w kodzie | Uwagi |
|---|---|---|
| **Opisy NFZ** | `generator/nfz.html`, `generator/szablony.js`, trasa `src/app/opisy-nfz`, API `src/app/api/nfz/*`, silnik serwerowy `src/lib/nfz/engine.ts` | generator przeniesiony **1:1** ze starej aplikacji (teksty i reguły bez zmian) |
| **Opisy prywatne** | `generator/prywatne.html`, `generator/prywatne-katalog.js`, `src/app/opisy-prywatne`, API `src/app/api/pryw/wizyty`, `src/app/api/dane` | **cenniki per gabinet** (cena, % lub kwota lekarza, koszty lab.), szablony, zestawy |
| **Kalendarz** | `generator/kalendarz.html`, `src/app/kalendarz`, API `src/app/api/kal/*`, `src/lib/kal.ts`, `src/lib/kal-silnik.ts` | dyżury, rozliczenia gabinetów, ZUS, podatek, terminy, porównanie form; silnik obliczeń uruchamiany też na serwerze (netto w Zarobkach) |
| **Zarobki / raporty** | `src/app/zarobki` (+ `csv`), `src/lib/zarobki.ts`, `src/lib/netto.ts` | okresy, gabinety, brutto/netto, wykres, średnie, dni tygodnia, CSV |
| **Gabinety** | `src/app/gabinety`, `src/lib/clinics.ts` | wspólne dla wszystkich modułów (model rozliczenia, %, kolor) |
| **Katalog NFZ** | `src/app/katalog-nfz`, `src/lib/nfz/catalog.ts`, migracja `0003` | podgląd kodów z punktami i źródłem (zarządzenie DSOZ) |
| Konto, ustawienia, import | `src/app/konto`, `ustawienia`, `import`, `generator/import.html` | import „Kopii całości” ze starej aplikacji |

**Warstwa urządzenia:** `generator/gabinet-saas.js` – zastępuje `wspolne.js` starej aplikacji: klucz urządzenia (AES-GCM, niewyciągalny CryptoKey w IndexedDB), lokalne przechowywanie treści opisów i inicjałów, synchronizacja **tylko metadanych**, kolejka offline, kontrola wersji i scalanie trójstronne (Kalendarz, materiały).

**Pliki `generator/*` nie edytuje się ręcznie.** Powstają skryptem `python3 tests/tools/przenies_generator.py <ścieżka do repo opisy-nfz>` z oryginału + listy opisanych poprawek (P*, K* …). Każda poprawka musi pasować **dokładnie raz**; opis trafia do `generator/ZMIANY.md`. Nowa zmiana w module = nowa poprawka w skrypcie, potem ponowne wygenerowanie.

## 3. Uruchomienie lokalne – Docker Desktop, MacBook Air M1

Dla Patryka (bez terminala na co dzień) – szczegóły w `INSTRUKCJA_OBSLUGI.md`:
1. Docker Desktop (Apple Silicon) uruchomiony, „Engine running”.
2. Terminal → `cd ` + przeciągnięty folder projektu → `bash zainstaluj-mac.command`.
   Skrypt trzyma klucze w `~/Gabinet/.env`, robi kopię bazy przed aktualizacją, buduje obraz, uruchamia usługi i tworzy aplikację „Gabinet” w `~/Applications`.
3. Aplikacja: `http://localhost:3000`, poczta testowa: `http://localhost:8025`.
4. Inne skrypty: `kopia-teraz-mac.command`, `przywroc-mac.command`, `zatrzymaj-mac.command`. Gatekeeper blokuje dwuklik `.command` z internetu – uruchamiaj przez `bash …`.

Dla dewelopera (ręcznie): `cp .env.example .env` i wpisać losowe wartości (`openssl rand -hex 32` dla `AUTH_SECRET` i `APP_ENC_KEY`), potem `docker compose up --build`.

### Testy (obowiązkowe przed każdym commitem)
```bash
npm run typecheck
DATABASE_URL=postgresql://gabinet_web:…@…/baza_po_migracjach npm test     # bez DATABASE_URL testy bazy (db.test.ts, nfz-zgodnosc.test.ts) się nie uruchomią
python3 db/test_izolacja.py                                               # izolacja SQL, tworzy własną świeżą bazę
npx next build && OPISY_DIR=<ścieżka do opisy-nfz> bash tests/e2e/uruchom.sh   # bez OPISY_DIR pomijane są porównania ze starą aplikacją
npm audit --omit=dev
```
**Uwaga:** `tests/pg-start.sh` i `tests/e2e/pomoc.py` zakładają Linuksa (`/usr/lib/postgresql/16/bin`, `su postgres`, `/usr/bin/google-chrome`). W Claude Code w chmurze (Linux) działają; na macOS trzeba je dostosować (np. Postgres z Homebrew/Dockera, ścieżka Chrome). Lint nie jest skonfigurowany.

## 4. STAŁE ZASADY (nie zmieniaj bez wyraźnej decyzji Patryka)

1. **Zero danych pacjentów w chmurze.** Na serwerze tylko: procedury, kody, kwoty, data, gabinet (klinika) – **bez tekstu opisów**, bez inicjałów, PESEL, adresów, zdjęć, wieku, numerów zębów, rozpoznań. Treść opisów i inicjały są **tylko na urządzeniu** (zaszyfrowane kluczem urządzenia); API odrzuca dodatkowe pola. Funkcji wymagających danych pacjentów nie dodawaj bez osobnej analizy i zgody Patryka.
2. **1 konto = 1 lekarz.** Zestawienia w ramach jednego konta; funkcji „zespół” nie ma (decyzja 6).
3. **Własne kody NFZ** zawsze z widocznym oznaczeniem **„niesprawdzane przez zasady NFZ”**; punkty wpisuje użytkownik, reguły łączenia/limitów NFZ ich nie obejmują (decyzja 7). *Stan 21.11.2026: zakładka „Własne kody” jest ukryta w interfejsie (dane w bazie zostają) – patrz HANDOFF.md, pytania otwarte.*
4. **Szyfrowanie po stronie serwera + reset hasła e-mailem** (decyzja 2): bezpieczeństwo przez bazę, transmisję i RLS; sekret 2FA szyfrowany `APP_ENC_KEY`. Treść opisów – osobno, na urządzeniu.
5. **Żadnego płatnego hostingu, usług ani zakupów bez wyraźnej zgody Patryka i planu kosztów.** Przed hostingiem zadaj dokładnie pytanie: „Czy wyrażasz zgodę na rozpoczęcie konfiguracji i uruchomienia produkcyjnego hostingu Gabinetu, zgodnie z przedstawionym planem i kosztami?”. Budżet ≤ 30 USD/mies. Wcześniejsza akceptacja architektury ≠ zgoda na zakup.
6. **Patryk nie jest programistą – Claude buduje, Patryk testuje.** Wyjaśniaj prosto, po polsku; pytania z wyborem odpowiedzi (A/B/C); przy niejasności pytaj, nie zgaduj.
7. **Nie deklaruj wykonania czegoś, czego nie zrobiłeś; nie twierdź, że działa, jeśli nie sprawdzone.** Nie deklaruj zgodności z RODO bez weryfikacji prawnej.
8. **Kodów NFZ i stawek nie wymyślaj** – źródło (numer zarządzenia DSOZ) przy każdej zmianie. Stawki: **1,84 zł/pkt, 350 zł/h przeglądów, +10 min** przy pakiecie higienizacyjnym z ekstrakcją lub leczeniem zachowawczym – bez zmian bez decyzji Patryka. Nie wymyślaj stawek podatkowych, składek ani potrąceń.
9. **Bez zgody Patryka:** nie usuwaj funkcji ani danych, nie rób commitów/pushy, nie zmieniaj `CLAUDE.md`, `HANDOFF.md`, `POSTEP.md`, `docs/AUDYT_SAAS.md`, nie zaczynaj kolejnego etapu, nie rób operacji destrukcyjnych w git.
10. **Sekrety tylko w `.env`** (nigdy w repo ani we frontendzie). `AUTH_SECRET` i `APP_ENC_KEY` **nie zmieniać po uruchomieniu** (2FA i rejestr triali przestaną działać); w produkcji kopia w bezpiecznym miejscu. Brak uniwersalnych haseł i ukrytych kont.
11. **Izolacja:** aplikacja łączy się jako `gabinet_web` i dostaje rolę wyłącznie przez `withUser` / `withRole` z `src/lib/db.ts`. Nie dodawaj dostępu do bazy z pominięciem tych funkcji. Każda nowa tabela z danymi użytkownika: `owner_id` + FORCE RLS + test w `db/test_izolacja.py`.
12. **Schemat bazy tylko nową migracją** `db/migrations/NNNN_*.sql`; wykonanych migracji nigdy nie edytuj. Migrację najpierw przedstaw Patrykowi.
13. Licencje (gdy wrócą) weryfikowane wyłącznie na serwerze; Stripe lokalnie tylko w trybie testowym.

## 5. Sposób pracy
- Etapami. Po etapie: testy (pkt 3) → raport ze statusami **WDROŻONE / WYMAGA MOJEGO DZIAŁANIA / WYMAGA KONFIGURACJI ZEWNĘTRZNEJ / NIE WDROŻONO** → za zgodą Patryka commit, push i jeden wiersz w `POSTEP.md`.
- Po przerwie: najpierw `HANDOFF.md`, `POSTEP.md`, `git log --oneline -10`.
- Odpowiedzi przejrzyste: tabele, krótkie bloki, źródła. Błędy przyznawaj wprost.

## 6. Konwencje kodu i nazewnictwa
- **Język:** nazwy tras, plików domenowych, komunikatów i testów po polsku (`/zarobki`, `/opisy-nfz`, `kal-silnik.ts`, `t_4e_kal.py`); kod pomocniczy i typy mogą być po angielsku (`withUser`, `ClinicRow`). Teksty interfejsu wyłącznie po polsku.
- **Kwoty:** na serwerze w **groszach** (liczby całkowite); formatowanie `fmtC` (`src/lib/nfz/engine.ts`). Daty `RRRR-MM-DD`, strefa `Europe/Warsaw` (`todayPL()` w `src/lib/zarobki.ts`).
- **Dostęp:** strony – `requireAccess()` (`src/lib/access.ts`); API – sesja + licencja + sprawdzenie `Origin` + walidacja (`src/lib/api.ts`); moduły serwerowe z `server-only`.
- **Silniki 1:1:** logika ze starej aplikacji przenoszona bez zmian i porównywana testami ze starą wersją (NFZ: 3000 losowych wizyt; teksty opisów co do znaku; Kalendarz: ten sam kod uruchamiany na serwerze przez `node:vm`).
- **Testy w przeglądarce:** `tests/e2e/t_<etap>_<temat>.py`, sprawdzenia `chk('opis po polsku', warunek, szczegóły)`, selektory `data-testid`, świeża baza na plik (`uruchom.sh`).
- **Zależności:** wersje przypięte w `package.json`; nowych bibliotek nie dodawaj bez potrzeby (obecnie tylko Next, React, pg, Argon2, nodemailer, qrcode).
- **Commity:** po polsku, opis co i dlaczego, na końcu linie współautorstwa wskazane przez środowisko.
