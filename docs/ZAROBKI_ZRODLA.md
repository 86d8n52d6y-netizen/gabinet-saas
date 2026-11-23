# Centralny system zarobków – źródła przychodu i wynagrodzenie lekarza

Stan: 23.11.2026 (prompt Patryka „Uporządkowanie katalogu procedur, opisów, kalendarza i centralnego systemu zarobków”).
Kod: `src/lib/zarobki-zrodla.ts` (jedyne miejsce liczenia), użycie: `src/lib/zarobki.ts` (raport), `src/lib/netto.ts` (netto), strona `/zarobki`.

## Trzy źródła – jeden mechanizm

| Źródło | Skąd | Przychód | Wynagrodzenie lekarza |
|---|---|---|---|
| Opisy NFZ (Opisy NFZ i zakładka NFZ) | `app.earnings_entries` (`nfz_points`, `nfz_review`, `nfz_extra`) | punkty × stawka + przeglądy + kwoty dodatkowe | udział wg Ustawień NFZ (% z dnia zapisu) + przeglądy + kwoty dodatkowe – **bez zmian zasad NFZ** |
| Opisy prywatne | `app.earnings_entries` (`private_procedure`) | cena × ilość | % lub kwota z Cennika; brak % w Cenniku → % gabinetu z „Gabinety” (model procentowy); % zapisany w pozycji z dniem zapisu |
| Obrót z Kalendarza | dokument miesiąca Kalendarza (`app.calendar_docs`, dyżur `status: done`, `turnover`) | obrót | wg zasad gabinetu (`kalIncome`: %, lab, stawka godzinowa / dzienna, korekta „kwota dla mnie”) |

Każdy dzień pracy (data × gabinet) ma jawnie określone źródła – bez porównywania kwot i bez heurystyk.

## Rozróżnienie obrotu – brak podwójnego naliczania

Dyżur z obrotem ma pole `obrotTyp` (ustawia lekarz w Kalendarzu, przy polu „Obrót”):

| `obrotTyp` | Znaczenie | Przychód dnia | Wynagrodzenie dnia |
|---|---|---|---|
| `opisy` (**domyślnie**, także wszystkie dotychczasowe wpisy) | obrót obejmuje opisy z tego dnia | obrót | z dyżuru wg zasad gabinetu; opisy tego dnia **nie są doliczane** (pokazane szare jako rozbicie) |
| `dodatkowy` | obrót = usługi spoza opisów | opisy + obrót | z opisów + z obrotu wg zasad gabinetu (minimum za dzień – na cały dzień) |

Dzień bez obrotu: gabinet procentowy – wynagrodzenie z opisów (z minimum za dzień, gdy był dyżur); gabinet godzinowy / dzienny / „kwota dla Ciebie” – wynagrodzenie z dyżuru (opisy dają przychód). Dzień bez dyżuru – z opisów.
Kwota z rozliczenia gabinetu (Zarobki → Rozliczenia) zastępuje wynagrodzenie gabinetu za pełny miesiąc w okresie (jak dotąd).

## Decyzje techniczne

1. **Bez migracji bazy.** `obrotTyp` to nowe pole w JSON dokumentu Kalendarza (serwer zapisuje dokument w całości). Brak pola = `opisy`, więc kwoty dla dotychczasowych danych się nie zmieniają (testy t_4d, t_4e, t_6, t_7 bez zmian oczekiwań).
2. **Zmiana względem decyzji z 21.11.2026 („opcja A” – zarobek lekarza tylko z dyżurów):** dzień z opisami bez wpisanego obrotu daje teraz wynagrodzenie z opisów (wcześniej 0 zł). Wynika z promptu z 23.11.2026 (pkt 5–7).
3. **Wynagrodzenie prywatne – % zapisywany w pozycji** w chwili zapisu wizyty: zmiana % gabinetu działa dla nowych wizyt, nie przelicza historii.
4. **Dane historyczne:** zachowane. Pozycje prywatne zapisane wcześniej bez % (wynagrodzenie 0 zł) są wykazywane w Zarobkach z liczbą i wskazówką „otwórz i zapisz ponownie” – nie przeliczamy historii bez decyzji lekarza.
5. **Netto** liczone z tych samych kwot brutto (miesiąc × gabinet), z tym samym silnikiem podatkowym Kalendarza.
6. Ustawienia rozliczenia gabinetu tylko w „Gabinety” (`app.clinics` – źródło prawdy, Kalendarz je wczytuje); pola „Spodziewany przychód” i „Termin płatności” zostają w danych (nie ma ich już w interfejsie).
