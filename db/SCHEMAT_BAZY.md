# Gabinet SaaS – projekt bazy danych (FAZA 2, do akceptacji)

Plik SQL: `0001_init.sql` · testy: `test_izolacja.py` (38 sprawdzeń, wynik 38 OK na PostgreSQL 16 – baza testowa, tymczasowa).
Decyzje: brak treści opisów i danych pacjentów (1), szyfrowanie po stronie serwera (2), Kalendarz od razu (3).

## 1. Tabele i relacje

```
profiles ─┬─ sessions (urządzenia)          ─ email_tokens         ─ security_events
          ├─ user_settings (stawki, ustawienia Kalendarza)
          ├─ subscriptions (licencja) ─ payments ─ payment_events (webhooki)
          ├─ clinics ─┬─ procedure_prices ── procedures ─┬─ procedure_versions
          │           ├─ saved_descriptions ── earnings_entries
          │           ├─ shifts, clinic_invoices          └─ procedure_categories
          ├─ procedure_sets ── procedure_set_items ── procedures | nfz_catalog
          ├─ days_off, business_costs, courses
          └─ audit_logs (dopisywanie)          nfz_catalog (wspólny, tylko odczyt)   trial_registry
```

| Tabela | Zawiera | Najważniejsze ograniczenia |
|---|---|---|
| `profiles` | e-mail, skrót hasła (Argon2id), nazwa, inicjały **lekarza**, rola, status, MFA | e-mail unikalny; skrót tylko Argon2id; rola `user`/`admin` |
| `sessions` | urządzenia: skrót tokenu, opis urządzenia, skrócony IP, ważność | bez limitu urządzeń; token w bazie tylko jako SHA-256 |
| `email_tokens` | weryfikacja e-mail, reset hasła | jednorazowe, z datą ważności |
| `security_events` | logowania, nieudane próby, nowe urządzenie, reset | typy zdarzeń z listy |
| `user_settings` | stawki (1,84 zł/pkt, 350 zł/h…), ustawienia Kalendarza (ZUS, podatki) | JSON, limit rozmiaru |
| `clinics` | gabinety: model rozliczenia, %, stawki, domyślny % lekarza | % 0–100, kwoty ≥ 0 |
| `nfz_catalog` | kody NFZ, punkty, **źródło (nr zarządzenia DSOZ)**, daty ważności, data weryfikacji | bez źródła wpis niemożliwy; aplikacja nie zmienia |
| `procedure_categories`, `procedures` | własne procedury: pola formularza, szablon tekstu, ulubiona, ukryta; `nfz_custom` = własna procedura NFZ (oznaczona „niesprawdzana”) | kategoria tylko własna |
| `procedure_versions` | historia wersji szablonów, przywracanie | wersja unikalna dla procedury |
| `procedure_prices` | cennik: gabinet × procedura: cena, wynagrodzenie (domyślny %, własny %, kwota) | jeden wiersz na gabinet i procedurę |
| `procedure_sets`, `procedure_set_items` | zestawy NFZ i prywatne, kolejność | element = procedura **albo** kod NFZ; kolejność unikalna |
| `saved_descriptions` | **zapisana wizyta bez treści**: data, gabinet, numer kolejny, kody, minuty, stawki z dnia zapisu, „edytowany” | brak pola na tekst i na pacjenta; `client_id` z urządzenia chroni przed dublem po utracie połączenia |
| `earnings_entries` | **jedyne źródło kwot w statystykach**: wartość, koszty, wynagrodzenie, ilość, punkty | każda kwota w jednym wierszu → brak podwójnego liczenia |
| `shifts`, `days_off`, `clinic_invoices`, `business_costs`, `courses` | Kalendarz | przychód z dyżurów liczony osobno, **nie** dodawany do `earnings_entries` |
| `subscriptions` | licencja: plan, 7 statusów z promptu, daty | trial dokładnie 3 miesiące (sprawdza baza) |
| `trial_registry` | HMAC e-maila – drugi trial na ten sam e-mail niemożliwy | patrz RODO niżej |
| `payments`, `payment_events` | transakcje (bez danych kart), zdarzenia webhooków | to samo zdarzenie przetworzone tylko raz |
| `audit_logs` | każda operacja administratora i zmiana licencji | **nie da się zmienić ani usunąć** (wyzwalacz) |

**Typy:** identyfikatory `uuid`; kwoty w groszach `bigint` (bez błędów zaokrągleń); procenty `numeric(5,2)`; daty `date`/`timestamptz`; elastyczne części (pola szablonu, ustawienia) `jsonb` z limitem rozmiaru.
**Indeksy:** po `(owner_id, data)` dla historii i statystyk, `(owner_id, gabinet, data)`, wyszukiwanie procedur po nazwie (trigramy), sesje aktywne użytkownika, dziennik po koncie i dacie.

## 2. Izolacja i dostęp

| Rola bazy | Kto | Może | Nie może |
|---|---|---|---|
| `gabinet_app` | żądania zalogowanego użytkownika | swoje wiersze (RLS: `owner_id = app.uid()`), swoją licencję **tylko czytać** | cudze dane, zmiana roli/statusu/hasła, zmiana licencji |
| `gabinet_auth` | logowanie i rejestracja | profile, sesje, tokeny, start triala | procedury, kwoty, Kalendarz, licencje płatne |
| `gabinet_billing` | webhooki płatności | licencje, płatności, zdarzenia | dane użytkowników |
| `gabinet_admin` | panel administratora | konta, licencje, płatności, logi, statystyki (same liczby) | procedury, kwoty, Kalendarz, skróty haseł |

RLS jest **wymuszony** (`FORCE`) – działa także dla właściciela tabel. Identyfikator użytkownika ustawia serwer z sesji w każdej transakcji; brak sesji = 0 wierszy. Klucze złożone `(owner_id, id)` blokują podpięcie własnego rekordu pod cudzy gabinet czy procedurę – nawet przy błędzie w kodzie aplikacji.

## 3. Co sprawdziły testy (38/38 OK)

| Obszar | Przykłady prób, które baza odrzuciła |
|---|---|
| Izolacja | odczyt procedury B po identyfikatorze, zmiana/usunięcie cudzych danych, wstawienie danych na konto B, przepisanie własnego rekordu na B, dyżur w gabinecie B, cena dla procedury B, odczyt bez sesji |
| Konto | odczyt skrótu hasła, nadanie sobie roli admina |
| Licencje | zmiana własnej licencji na lifetime, trial dłuższy niż 3 mies., lifetime z modułu logowania; wygasła licencja → brak dostępu (sprawdzenie na serwerze) |
| Płatności | drugie przetworzenie tego samego zdarzenia webhooka |
| Administrator | odczyt procedur, kwot, Kalendarza, skrótów haseł; zmiana lub usunięcie dziennika audytowego |
| Synchronizacja | zapis ze starszej wersji (drugie urządzenie) nie nadpisuje nowszej |
| Dane pacjentów | brak kolumn typu PESEL/pacjent/adres/telefon; brak pola na treść opisu |

Błąd znaleziony przez testy i poprawiony: unikalność „wizyta + numer pozycji” pozwalała na jedną ręczną kwotę w całej bazie (dla wszystkich użytkowników).

## 4. Do Twojej decyzji / wiedzy

| Sprawa | Propozycja |
|---|---|
| `trial_registry` przechowuje HMAC e-maila także po usunięciu konta (żeby nie dało się powtarzać triala) | to dana spseudonimizowana; okres przechowywania np. 3 lata i zapis w polityce prywatności – do potwierdzenia z prawnikiem |
| Adres IP | zapisywany skrócony (/24), tylko w sesjach i zdarzeniach bezpieczeństwa; usuwanie po 90 dniach |
| Notatka przy dyżurze (500 znaków) | jedyne pole wolnego tekstu poza nazwami – w interfejsie ostrzeżenie „bez danych pacjentów” |
| Inicjały | tylko lekarza/użytkownika (statystyki), nigdy pacjenta |
