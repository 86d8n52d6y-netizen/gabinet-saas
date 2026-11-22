# Raport końcowy – baza stomatologiczna (PROMPT 2), 22.11.2026

**Status: opracowanie zakończone, dane NIE są zweryfikowane i NIE są zintegrowane z aplikacją.** Każdy kod-procedura z ICD-9 PL 5.91 ma kartę albo jawny status z uzasadnieniem; żaden rekord nie ma statusu `verified` (weryfikacja należy do Patryka). Gałąź: `baza-stomatologiczna` – bez scalania do `main`, bez zmian w `generator/`, `src/`, `data/nfz/`, `CLAUDE.md`, `HANDOFF.md`, `POSTEP.md`, `docs/AUDYT_SAAS.md`.

## 1. Kryteria zakończenia (sekcja 12 promptu)

| # | Kryterium | Stan |
|---|---|---|
| 1–4 | Katalog badań, opisy wg standardu, 3 warianty tekstów, pola formularzy | ✅ 17 badań, 135 pól (31 wspólnych), szablony 3 × badanie |
| 5 | Każda procedura ICD-9 – karta lub jawny status | ✅ 206 kart + 3 kody nadrzędne z odesłaniem + 57 pominiętych z uzasadnieniem; 0 bez statusu |
| 6–7 | Przebieg krok po kroku, schemat opisu | ✅ 114 kroków w bibliotece (karta = kroki + uwagi dla procedury), 669 szablonów |
| 8 | Powiązania ICD-9 ↔ ICD-10 uzasadnione | ✅ 401 podpowiedzi z okolicznościami (146 obecnych też w audycie NFZ); wszystkie „ocena kliniczna”, nigdy automatyczne |
| 9 | Wymagania NFZ oddzielone od zaleceń | ✅ sekcja `nfz` z danych audytu; elementy dokumentacji i checklist z podstawą (prawna / NFZ / kliniczna / aplikacja) |
| 10–11 | Dane w repozytorium, walidacja | ✅ JSON + 10 schematów; `scripts/waliduj_baze.py` – WYNIK OK |
| 12 | Źródła i status weryfikacji | ✅ 21 publikacji z PubMed (PMID) + źródła prawne audytu; `SRC-PRAKTYKA` jawnie „wymaga weryfikacji” |
| 13 | Rejestr kompletności | ✅ `docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md` |
| 14–15 | Instrukcja integracji, zgodność z architekturą | ✅ `docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md` (format jak audyt NFZ, bez tabel i migracji) |
| 16 | Raport końcowy | ✅ ten dokument |

## 2. Procedury wg grup

| Grupa | draft | requires_expert_review | not_started | kody nadrzędne | pominięte |
|---|---|---|---|---|---|
| badanie, diagnostyka, RTG, znieczulenie | 15 | 1 | – | – | – |
| profilaktyka (w tym świadczenia dla dzieci wg wieku) | 23 | 1 | – | – | – |
| leczenie próchnicy, odbudowa i estetyka, zachowawcza | 21 | 4 | – | – | – |
| endodoncja (miazga, kanały) | 22 | 6 | – | – | – |
| periodontologia i błona śluzowa | 15 | 7 | – | 2 | – |
| chirurgia (ekstrakcje, stomatologiczna, wycięcia, zakażenia, urazy) | 11 | 24 | – | 1 | 3 |
| fizykoterapia, pomoc doraźna | 1 | 8 | – | – | – |
| protetyka (korony, mosty, protezy ruchome) | 36 | 11 | – | – | 10 |
| ortodoncja, złamania szczęk | – | – | – | – | 44 |
| **razem (266)** | **144** | **62** | **0** | **3** | **57** |

**requires_expert_review (62)** – treść gotowa, ale wymaga oceny eksperta lub Twojej decyzji: zabiegi specjalistyczne chirurgii i periodontologii (31), protetyka specjalistyczna (teleskopy, uzupełnienia złożone, overdenture, odlewane elementy, metalowa podstawa, odtworzenie zwarcia, likwidacja dużych zaburzeń zgryzowych), metody historyczne nadal w wykazie NFZ (dewitalizacja 23.1202, miazga zdewitalizowana 23.1207–23.1210, 23.1310), stare kody „wypełnienie” 23.1109–23.1112, fizykoterapia, impregnacja zębiny, pomoc poza godzinami, znieczulenie zewnątrzustne.

## 3. Checklisty kompletności

10 elementów wspólnych + elementy procedur: zalecane, rozliczeniowe (NFZ, z warunkiem), sytuacyjne. **Żaden element procedury nie jest „obowiązkowy”**; obowiązkowe są tylko 4 elementy wspólne z rozporządzenia o dokumentacji (data, opis, rozpoznanie, lekarz), a to źródło ma status „wymaga weryfikacji” – do czasu weryfikacji aplikacja powinna je pokazywać jako ostrzeżenie, nie blokadę. Świadczenia profilaktyczne dla dzieci (23.1009–23.1023): checklista = punkty z zał. 10 rozporządzenia (wyciągnięte z danych audytu, nie przepisane ręcznie).

## 4. Utworzone pliki

`data/baza-stomatologiczna/` (10 schematów, `zrodla-kliniczne.json`, `pola-wspolne.json`, `manifest.json`), `data/badania/` (3), `data/procedury-icd9/` (6), `scripts/waliduj_baze.py`, `scripts/buduj_docs_bazy.py`, `scripts/import_bazy.py`, `docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md`, `docs/badania/` (README, OPISY_BADAN, STRUKTURA_POL), `docs/procedury-icd9/` (README, KARTY_PROCEDUR, REJESTR_KOMPLETNOSCI), ten raport.

## 5. Nierozstrzygnięte kwestie

| # | Kwestia | Propozycja |
|---|---|---|
| 1 | Rozporządzenie o dokumentacji medycznej (Dz.U. 2026 poz. 1391) nieodczytane – 4 elementy „obowiązkowe” opierają się na nim | dołączyć tekst aktu albo uznać je za zalecenia |
| 2 | Prawo atomowe (uzasadnienie i opis RTG) – akt nieopisany w audycie | jw. |
| 3 | Kody ICD-10 oznaczone „do weryfikacji kodu” (np. K03.8, K13.7, K00.4, K08.8, S02.6) | porównać z wydaniem CeZ (N8 audytu) |
| 4 | Brak stałych powiązań ICD-10 dla porady, zaopatrzenia ran, krwawień (rozpoznanie zależy od przyczyny) | zostawić – wybiera lekarz |
| 5 | Teksty gabinetu (`szablony.js`) mają wyniki prawidłowe wpisane z góry; baza – nie | decyzja przy integracji |
| 6 | 23.1109–23.1112 obok 23.1502–23.1506 | czy NFZ jeszcze ich używa |
| 7 | Zał. 6 (protetyka) nieczytany – warunki NFZ protetyki tylko z danych odczytanych | przy rozliczaniu protez NFZ – dołączyć zał. 6 |
| 8 | Treść kart oparta w dużej części na `SRC-PRAKTYKA` (chirurgia, protetyka, znieczulenia, RTG) | weryfikacja Patryka; dla kluczowych obszarów – dodatkowe wytyczne (np. postępowanie przy lekach przeciwkrzepliwych) |

## 6. Rekomendowane kolejne kroki

1. **Weryfikacja Patryka** – zacznij od kart z kodami używanymi w Opisach NFZ (ST33, ST34, ST28, ST26, ST30*, ST04, ST01, ST02, ST19, 1101, 1105, 1108, 1206, 1502–1505, 1006, 0401–0403); zatwierdzone → `verified`.
2. Decyzje do kwestii 1, 5 i 6.
3. Integracja (na zlecenie): `generator/baza-dane.js` jak `nfz-dane.js` → katalog procedur, podpowiedzi przebiegu, checklisty przed zapisem, generowanie opisów z szablonów (przykład w instrukcji, sprawdzony na danych).
