# Raport – baza stomatologiczna (PROMPT 2), stan 22.11.2026

**Status: praca w toku – NIE zakończona** (kryterium 5: 80 procedur ma jeszcze status `not_started` – profilaktyka dzieci wg wieku, fizykoterapia, pomoc doraźna, protetyka). Gałąź: `baza-stomatologiczna` (bez scalania do `main`, bez zmian w aplikacji).

## 1. Etapy promptu

| Etap | Stan |
|---|---|
| 1 Analiza poprzedniego etapu | ✅ audyt NFZ (`data/nfz`, `docs/nfz`), architektura (generator + Next.js + PostgreSQL), istniejące teksty (`generator/szablony.js`) |
| 2 Inwentaryzacja | ✅ rejestr 266 kodów-procedur (260 liści ICD-9 PL 5.91 + 6 kodów nadrzędnych używanych w świadczeniach) |
| 3 Badania | ✅ 17 badań (draft) – pola, 3 warianty opisu |
| 4 Karty procedur | ⏳ 126 kart (85 draft + 41 requires_expert_review) + 3 kody nadrzędne z odesłaniem; 80 not_started; 57 pominiętych decyzją Patryka |
| 5 Powiązania | ⏳ 263 mapowania ICD-10 dla opracowanych kart; badania – warunkowe ICD-9/ICD-10 |
| 6 Zapis i integracja | ✅ JSON + JSON Schema + manifest + `docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md` + `scripts/import_bazy.py` |
| 7 Walidacja | ✅ `scripts/waliduj_baze.py` – WYNIK OK (3 ostrzeżenia – patrz §5) |
| 8 Raport | ⏳ ten dokument (częściowy) |

## 2. Procedury wg grup

| Grupa | draft | requires_expert_review | not_started | pominięte |
|---|---|---|---|---|
| badanie, diagnostyka, RTG, znieczulenie | 12 | – | 4 | – |
| profilaktyka (w tym świadczenia dla dzieci wg wieku) | 4 | – | 19 | – |
| leczenie próchnicy, odbudowa i estetyka, zachowawcza | 21 | 4 | 0 | – |
| endodoncja (miazga, kanały) | 22 | 6 | 0 | – |
| periodontologia i błona śluzowa | 15 | 7 | 2 (kody nadrzędne – odesłanie) | – |
| chirurgia (ekstrakcje, stomatologiczna, wycięcia, zakażenia, urazy) | 11 | 24 | 1 (kod nadrzędny 23.17) | 3 |
| fizykoterapia, pomoc doraźna, dziecko | 0 | – | 10 | – |
| protetyka (korony, mosty, protezy ruchome) | 0 | – | 47 | 10 |
| ortodoncja, złamania szczęk | – | – | – | 44 |
| **razem (266)** | **85** | **41** | **83** (w tym 3 nadrzędne) | **57** |

`requires_expert_review`: zabiegi specjalistyczne chirurgii i periodontologii (31) – treść do weryfikacji przez specjalistę; metody historyczne nadal w wykazie NFZ (dewitalizacja 23.1202, miazga zdewitalizowana 23.1207–23.1210), 23.1310 oraz stare kody „wypełnienie” 23.1109–23.1112 – do decyzji Patryka.

Pełna lista kodów ze statusami: `docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md`.

## 3. Utworzone pliki

`data/baza-stomatologiczna/` (schemas – 10 schematów, `zrodla-kliniczne.json`, `pola-wspolne.json`, `manifest.json`), `data/badania/` (3 pliki), `data/procedury-icd9/` (6 plików), `scripts/waliduj_baze.py`, `scripts/buduj_docs_bazy.py`, `scripts/import_bazy.py`, `docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md`, `docs/badania/*` (README, OPISY_BADAN, STRUKTURA_POL), `docs/procedury-icd9/*` (README, KARTY_PROCEDUR, REJESTR_KOMPLETNOSCI), ten raport.
**Nie zmieniono:** aplikacji (`generator/`, `src/`), `data/nfz/`, `CLAUDE.md`, `HANDOFF.md`, `POSTEP.md`, `docs/AUDYT_SAAS.md`.

## 4. Źródła i weryfikacja

- 21 publikacji sprawdzonych w PubMed (PMID): ESE 2006, ESE S3 2023, ESE 2019 (próchnica głęboka), EFP S3 2020, klasyfikacja 2017 (3), EAPD 2019, ADA 2013 i 2016, AAPD 2017, IADT 2020 (4), DC/TMD 2014, ICDAS 2007, PCR 1972, GI 1963, OPMD 2021, chirurgia endodontyczna 2006.
- Wymagania NFZ – z audytu NFZ (statusy źródeł bez zmian).
- `SRC-PRAKTYKA` (praktyka kliniczna bez publikacji) – wszędzie tam, gdzie nie znalazłem źródła; **do weryfikacji przez Patryka** (m.in. chirurgia, znieczulenia, RTG).
- Żaden rekord nie ma statusu `verified` – weryfikacja należy do Patryka.

## 5. Nierozstrzygnięte kwestie

| # | Kwestia | Propozycja |
|---|---|---|
| 1 | Rozporządzenie o dokumentacji medycznej (Dz.U. 2026 poz. 1391) nieodczytane – elementy „obowiązkowe” oparte na nim mają status „wymaga weryfikacji” | dołączyć tekst aktu albo zaakceptować listę jako zalecenia |
| 2 | Prawo atomowe (uzasadnienie i opis RTG) – akt nieopisany w audycie | jw. |
| 3 | Kody ICD-10 do weryfikacji: K03.8 (nadwrażliwość), K13.7 (odleżyna), K00.4 (MIH) | porównać z wydaniem CeZ (N8 audytu) |
| 4 | Brak stałych powiązań ICD-10 dla 23.0103, 23.1809, 23.1813 (rozpoznanie zależy od przyczyny) | zostawić – lekarz wybiera przy wizycie |
| 5 | Teksty gabinetu (`szablony.js`) mają wyniki prawidłowe wpisane z góry – baza tego nie robi | decyzja przy integracji: zostawić czy przejść na pola |
| 6 | 23.1109–23.1112 (stare kody „wypełnienie na n powierzchniach”) obok 23.1502–23.1506 | sprawdzić, czy NFZ ich jeszcze używa – na razie not_started |

## 6. Rekomendowane kolejne partie

1. ✅ Endodoncja, leczenie próchnicy, estetyka (partia 3).
2. ✅ Periodontologia i chirurgia stomatologiczna (partia 4 – zabiegi specjalistyczne jako requires_expert_review).
3. Profilaktyka dzieci wg wieku (23.1009–23.1023) i fizykoterapia (26).
4. Protetyka (47) – ważne dla przyszłej implantoprotetyki.
5. Po każdej partii: walidator, manifest, dokumentacja, commit na gałąź; na koniec – weryfikacja Patryka (`verified`) i decyzja o integracji.
