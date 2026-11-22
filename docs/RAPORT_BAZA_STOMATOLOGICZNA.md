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
| 1 | Rozporządzenie o dokumentacji medycznej (Dz.U. 2026 poz. 1391) nieodczytane – 4 elementy „obowiązkowe” opierają się na nim | **Decyzja Patryka 22.11.2026: przy integracji – ostrzeżenie przed zapisem, bez blokady** (do czasu odczytania aktu) |
| 2 | Prawo atomowe (uzasadnienie i opis RTG) – akt nieopisany w audycie | jw. |
| 3 | Kody ICD-10 oznaczone „do weryfikacji kodu” (np. K03.8, K13.7, K00.4, K08.8, S02.6) | porównać z wydaniem CeZ (N8 audytu) |
| 4 | Brak stałych powiązań ICD-10 dla porady, zaopatrzenia ran, krwawień (rozpoznanie zależy od przyczyny) | zostawić – wybiera lekarz |
| 5 | Teksty gabinetu (`szablony.js`) mają wyniki prawidłowe wpisane z góry; baza – nie | decyzja przy integracji |
| 6 | 23.1109–23.1112 obok 23.1502–23.1506 | czy NFZ jeszcze ich używa |
| 7 | Zał. 6 (protetyka) nieczytany – warunki NFZ protetyki tylko z danych odczytanych | przy rozliczaniu protez NFZ – dołączyć zał. 6 |
| 8 | Treść kart oparta w dużej części na `SRC-PRAKTYKA` (chirurgia, protetyka, znieczulenia, RTG) | weryfikacja Patryka; dla kluczowych obszarów – dodatkowe wytyczne (np. postępowanie przy lekach przeciwkrzepliwych) |

## 6. Rekomendowane kolejne kroki

1. **Weryfikacja Patryka** – zacznij od kart z kodami używanymi w Opisach NFZ (ST33, ST34, ST28, ST26, ST30*, ST04, ST01, ST02, ST19, 1101, 1105, 1108, 1206, 1502–1505, 1006, 0401–0403); zatwierdzone → `verified`.
2. Decyzje do kwestii 5 i 6 (kwestia 1 – rozstrzygnięta: ostrzeżenie).
3. Integracja (na zlecenie): `generator/baza-dane.js` jak `nfz-dane.js` → katalog procedur, podpowiedzi przebiegu, checklisty przed zapisem, generowanie opisów z szablonów (przykład w instrukcji, sprawdzony na danych).

## 7. Weryfikacja i decyzje Patryka (22.11.2026)

| Decyzja | Karty | Stan |
|---|---|---|
| Zatwierdzone (`verified`) | wszystkie kody wizyty z Opisów NFZ: 23.0101, 23.0102, 23.0107, 23.0401–23.0403, 23.1006, 23.1101, 23.1105, 23.1108, 23.1206, 23.1502–23.1505, 23.16011, 23.16012, 23.16021, 23.1605, 23.1607, 23.1701, 23.1702, 23.2001 | 23 |
| Odrzucone – nie umieszczać w aplikacji | metody historyczne i rzadkie (fizykoterapia, dewitalizacja i miazga zdewitalizowana, 23.1310, stare kody „wypełnienie” 23.1109–23.1112, impregnacja, znieczulenie zewnątrzustne, 23.07), chirurgia specjalistyczna (24), periodontologia specjalistyczna (7) | 51 – status `not_started` z uzasadnieniem „Odrzucone decyzją Patryka”; treść zachowana, przywracalna |
| Zostają „do oceny specjalisty” | protetyka specjalistyczna (teleskopy, overdenture, uzupełnienia złożone, metalowa podstawa, odlewane elementy, odtworzenie zwarcia, 23.2901) – przyda się przy implantoprotetyce | 11 |

Stan po decyzjach: 23 verified, 121 draft, 11 requires_expert_review, 51 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja protetyki (22.11.2026)

Zatwierdzone (`verified`): 36 kart – przygotowanie i korony (23.2701–23.2706, 23.2801–23.2806, 23.2903, 23.3125), mosty i szyna (23.3001–23.3003, 23.3005, 23.3009–23.3011, 23.2902), protezy ruchome (23.3101–23.3105, 23.3107, 23.3108, 23.3111–23.3117).
Odrzucone – nie umieszczać: 11 kart protetyki specjalistycznej (23.2901, 23.3004, 23.3006–23.3008, 23.31041, 23.31051, 23.3106, 23.3109, 23.3110, 23.3126) – decyzja po przeglądzie pojedynczych kart.

Stan: 59 verified, 85 draft, 0 requires_expert_review, 62 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja profilaktyki (22.11.2026)

Zatwierdzone (`verified`): 16 kart – bilanse NFZ dla dzieci 23.1009–23.1021 (13, każdy zatwierdzony pojedynczo), lakowanie 23.1003 i 23.1004, leczenie nadwrażliwości 23.1007.
Odrzucone – nie umieszczać: 23.08 (instruktaż), 23.1001 (fluoryzacja indywidualna), 23.1002 (fluoryzacja zbiorowa), 23.1022 (profilaktyka wad zgryzu), 23.1023 (profilaktyka 3. r.ż. – brak w wykazie NFZ wg audytu).
Uwagi pozostawione bez zmian (decyzja: zatwierdzone bez poprawek): szablony 23.1009–23.1011 i 23.1021 zawierają zdania puw/PUW lub „Fluorki” nieobowiązkowe w danym wieku – puste pole usuwa całe zdanie. Kod produktu przy 23.1003 (`5.13.00.2310090`) nadal „WYMAGA WERYFIKACJI” w audycie NFZ.

Stan: 75 verified, 64 draft, 0 requires_expert_review, 67 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja endodoncji (22.11.2026)

Zatwierdzone (`verified`), każda karta pojedynczo: 21 kart – 23.1201, 23.1203–23.1205, 23.1301–23.1309, 23.1311–23.1314, 23.13141, 23.13142, 23.13143, 23.13149.
Poprawka na polecenie Patryka: szablony 23.1203 i 23.1204 (amputacja przyżyciowa) – usunięte pola „Kanały” i „Płukanie” (przy pulpotomii zbędne).
23.1314 (kod nadrzędny MTA) – karta zatwierdzona decyzją Patryka (rozlicza się podkody 23.13141–23.13149).
**Uwagi do audytu NFZ (nie zmienione w tym etapie):** 23.1313 (3 kanały ze zgorzelą) – brak w wykazie zał. 1b odczytanym w audycie, choć 23.1312 jest – sprawdzić w zarządzeniu; kod produktu 23.13142 `5.13.00.2314142` – „WYMAGA WERYFIKACJI”; kody produktów 23.1203–23.1205, 23.1308, 23.1309, 23.1312 – nieodczytane.

Stan: 96 verified, 43 draft, 67 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja periodontologii, odbudowy i chirurgii (22.11.2026)

Zatwierdzone pojedynczo (14): perio 23.16022, 23.1604, 23.1609, 23.1611, 23.1615; odbudowa 23.1501, 23.1506, 23.1507, 23.1511, 23.1512; chirurgia 23.1703, 23.1704, 23.1806, 23.1815.
Odrzucone – nie umieszczać (11): 23.1603, 23.1612, 23.1616, 23.1617, 23.1620, 23.1508, 23.1509, 23.1510, 23.1809, 23.1810, 23.1813.
Uwagi: 23.1501 i 23.1507 opisują podobny zabieg (w NFZ rozliczana 23.1507) – obie zatwierdzone decyzją Patryka; 23.1615 – świadczenie gwarantowane bez odczytanego kodu produktu (audyt NFZ).

Stan: 110 verified, 18 draft, 78 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja ostatnich kart (22.11.2026) – koniec weryfikacji kart procedur

Zatwierdzone pojedynczo (9): RTG 23.0301, 23.0302, 23.0303, 23.0304; 23.1104 pośrednie pokrycie miazgi; 23.1106 i 23.1107 opatrunek leczniczy; 23.06 wizyta adaptacyjna; 23.2101 repozycja zwichniętego zęba.
Odrzucone (9): 23.0103, 23.0104, 23.0105, 23.0106, 23.02 (badanie/porada/diagnostyka – grupowo), 23.1102, 23.1103, 23.05, 23.14.
Uwagi: karty RTG nie mają mapowań ICD-10; 23.0302 i 23.2101 – świadczenia gwarantowane bez odczytanego kodu produktu (audyt NFZ).

**Stan końcowy kart procedur:** 119 verified, 0 draft, 87 odrzucone (ukryte, treść zachowana), 57 pominięte, 3 nadrzędne (razem 266). Badania (17) – nadal draft.

### Przegląd kart odrzuconych (22.11.2026)

Patryk przejrzał pojedynczo wszystkie 87 odrzuconych kart (przywrócić / pozostawić).
Przywrócone i zatwierdzone (25): 23.0103, 23.0104, 23.0106, 23.02, 23.0404, 23.1008, 23.1109–23.1112, 23.1202, 23.1208, 23.1209, 23.1610, 23.1612, 23.1613, 23.1618, 23.1619, 23.1705, 23.1707, 23.1801, 23.2002, 23.3004, 23.31041, 23.31051.
Pozostają odrzucone: 62. Pominięte kody (57: ortodoncja, chirurgia szczękowo-twarzowa, znieczulenie ogólne, epitezy) – bez zmian, decyzja: nie opracowywać.

**Stan:** 144 verified, 0 draft, 62 odrzucone, 57 pominięte, 3 nadrzędne (razem 266).

### Weryfikacja badań (22.11.2026)

Patryk zatwierdził wszystkie 17 badań (`verified`, z osobą i datą – schemat badań rozszerzony o `zweryfikowal`, `zweryfikowano`, `uzasadnienie_statusu`; walidator wymaga osoby i daty przy `verified`). Dodany mechanizm odrzucania badań (status `not_started` + „Odrzucone…” → ukryte w katalogu, jak karty procedur) – obecnie nieużywany.
**Prośba Patryka – nowa funkcja (do zaplanowania):** w aplikacji wybór, które części badania mają się pojawić w opisie (np. bez wywiadu i bez oceny zmian na błonie, ale z badaniem wewnątrz- i zewnątrzustnym).

### Uwagi do audytu NFZ – sprawdzenie (22.11.2026)

| Uwaga | Wynik | Źródło |
|---|---|---|
| 23.1313 (3 kanały ze zgorzelą) brak w NFZ | **Potwierdzone – nie jest świadczeniem gwarantowanym.** Rozporządzenie wymienia 23.1308, 23.1309, 23.1311, 23.1312, 23.1314 (MTA), a 23.1313 nie występuje w żadnym załączniku (1, 2, 2a, 2b, 3, 4). Karta zostaje z oznaczeniem „poza NFZ”. | Dz.U. 2025 poz. 615 (t.j. rozporządzenia MZ), pobrany z api.sejm.gov.pl 22.11.2026; zmian rozporządzenia po t.j. nie sprawdzano |
| 23.1308 / 23.1309 / 23.1312 – warunki | Zgodne z kartami: tylko dzieci i młodzież do 18 r.ż. oraz kobiety w ciąży i połogu; bez opracowania i odbudowy korony | jw. |
| Kody produktów 23.13142 (`2314142`?), 23.1003 (`2310090`?) i nieodczytane (23.1203–23.1205, 23.1308, 23.1309, 23.1312 i in.) | **Nie sprawdzone** – strona baw.nfz.gov.pl blokuje pobieranie automatyczne; potrzebny zał. 1b do zarządzenia 60/2023/DSOZ (t.j.) od Patryka (PDF/XLSX) albo odczyt w portalu NFZ | SRC-ZARZ-60-2023-TJ |
