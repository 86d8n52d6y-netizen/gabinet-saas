# Katalog A – badania stomatologiczne

> Plik generowany: `python3 scripts/buduj_docs_bazy.py` z danych w `data/`. Nie edytuj ręcznie – popraw JSON.

Wersja danych: 2026.11.22-1. Badań: 17. Status każdego badania – w nagłówku. Wynik prawidłowy to **przykład opisu**, nigdy nie jest zaznaczany za lekarza.

## Badanie podmiotowe (wywiad lekarski stomatologiczny) (`BAD-WYWIAD`)

Krótko: **Wywiad** · kategoria: podmiotowe · status: **draft**

**Cel.** Stan zdrowia ogólnego i jamy ustnej z perspektywy pacjenta, czynniki ryzyka i przeciwwskazania do leczenia.

- Informacje: powód zgłoszenia i dolegliwości; choroby ogólne, leki, alergie; ciąża / karmienie; używki i parafunkcje; przebieg wcześniejszego leczenia stomatologicznego; nawyki higieniczne i dietetyczne
- Wykrywa: przeciwwskazania lub ograniczenia do zabiegów (np. leczenie przeciwkrzepliwe, leki antyresorpcyjne, radioterapia); ryzyko powikłań po znieczuleniu; czynniki ryzyka próchnicy i chorób przyzębia; objawy sugerujące choroby ogólne

**Wskazania** (rutynowe): pierwsza wizyta; każda wizyta – aktualizacja (leki, choroby, ciąża); przed każdym zabiegiem chirurgicznym i znieczuleniem. Szczególnie: pacjenci z chorobami przewlekłymi i wielolekowością; kobiety w ciąży; dzieci (wywiad od opiekuna)

**Przebieg**

1. **Powód zgłoszenia** – Zapytaj o powód wizyty i dolegliwości; zanotuj słowami pacjenta.
2. **Wywiad w kierunku dolegliwości** – Lokalizacja, charakter bólu (samoistny / prowokowany), czas trwania, czynniki nasilające i łagodzące, ból nocny, obrzęk, gorączka.
3. **Wywiad ogólnomedyczny** – Choroby przewlekłe, hospitalizacje, leki (szczególnie przeciwkrzepliwe, antyagregacyjne, antyresorpcyjne, sterydy), alergie, ciąża / karmienie; u dzieci – od opiekuna.
4. **Wywiad stomatologiczny** – Dotychczasowe leczenie, reakcje na znieczulenie, powikłania po ekstrakcjach, ostatnia wizyta kontrolna, ortodoncja, protezy.
5. **Czynniki ryzyka** – Higiena, dieta (częstość cukrów), fluorki, palenie, parafunkcje, suchość w jamie ustnej.
6. **Potwierdzenie i podpis** – Odczytaj kluczowe informacje pacjentowi; przy ankiecie pisemnej – zweryfikuj ją ustnie.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| powód zgłoszenia | dolegliwość główna | `POLE-WYW-POWOD` |
| choroby ogólne | choroby wpływające na leczenie | `POLE-WYW-CHOROBY` |
| leki | leki modyfikujące krzepnięcie, gojenie i metabolizm kości | `POLE-WYW-LEKI` |
| alergie | reakcje uczuleniowe | `POLE-WYW-ALERGIE` |
| ciąża | ciąża / karmienie | `POLE-WYW-CIAZA` |
| używki | palenie, alkohol | `POLE-WYW-NALOGI` |
| parafunkcje | bruksizm i nawyki | `POLE-WYW-PARAFUNKCJE` |

**Przykład wyniku prawidłowego:** Pacjent bez dolegliwości, zgłasza się na wizytę kontrolną. Wg pacjenta nie choruje przewlekle, nie przyjmuje leków na stałe, alergii nie zgłasza. Nie pali tytoniu. Zęby szczotkuje 2× dziennie pastą z fluorem. (Przykład – wpisują się wyłącznie informacje podane przez pacjenta.)

**Przykłady nieprawidłowości:** ból samoistny, nocny lub pulsujący; przyjmowanie leków przeciwkrzepliwych (np. acenokumarol, rywaroksaban, apiksaban, dabigatran); leki antyresorpcyjne (bisfosfoniany, denosumab) – ryzyko martwicy kości szczęk; radioterapia okolicy głowy i szyi; alergia na środki znieczulające lub lateks; ciąża; niekontrolowana cukrzyca; palenie tytoniu

**Dokumentacja – niezbędne**

- Wywiad: choroby, leki, alergie – informacje podane przez pacjenta — *prawne* (`SRC-DU-2026-1391`)
- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Wywiad stomatologiczny i czynniki ryzyka (higiena, dieta, palenie) — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- Uzgodnienie z lekarzem prowadzącym (np. modyfikacja leczenia przeciwkrzepliwego) – tylko przez lekarza prowadzącego — *zalecenie kliniczne*, warunek: leki przeciwkrzepliwe przed zabiegiem chirurgicznym (`SRC-PRAKTYKA`)
- Tydzień ciąży — *zalecenie kliniczne*, warunek: ciąża (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: — · ICD-10: —

*Wywiad jest częścią każdego badania (23.0101, 23.0102, 23.0105, 23.0107) – nie jest osobnym świadczeniem ICD-9.*

**Szablony opisu**

**standardowy**

> WYWIAD: Powód zgłoszenia: {{POLE-WYW-POWOD}}. Dolegliwości: {{POLE-WYW-DOLEGLIWOSCI}}. Choroby ogólne: {{POLE-WYW-CHOROBY}}. Leki: {{POLE-WYW-LEKI}}. Alergie: {{POLE-WYW-ALERGIE}}. Ciąża / karmienie: {{POLE-WYW-CIAZA}}. Używki: {{POLE-WYW-NALOGI}}.

**skrocony**

> Wywiad: {{POLE-WYW-POWOD}}; choroby: {{POLE-WYW-CHOROBY}}; leki: {{POLE-WYW-LEKI}}; alergie: {{POLE-WYW-ALERGIE}}.

**rozszerzony**

> WYWIAD: Powód zgłoszenia: {{POLE-WYW-POWOD}}. Dolegliwości: {{POLE-WYW-DOLEGLIWOSCI}}. Choroby ogólne: {{POLE-WYW-CHOROBY}}. Leki przyjmowane stale: {{POLE-WYW-LEKI}}. Alergie: {{POLE-WYW-ALERGIE}}. Ciąża / karmienie: {{POLE-WYW-CIAZA}}. Używki: {{POLE-WYW-NALOGI}}. Wywiad stomatologiczny: {{POLE-WYW-STOMAT}}. Higiena i dieta: {{POLE-WYW-HIGIENA}}. Parafunkcje: {{POLE-WYW-PARAFUNKCJE}}. Uwagi: {{POLE-UWAGI}}.

**Źródła:** `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Badanie przedmiotowe zewnątrzustne (`BAD-ZEWNATRZUSTNE`)

Krótko: **Zewnątrzustne** · kategoria: przedmiotowe · status: **draft**

**Cel.** Twarz, skóra, wargi, węzły chłonne, stawy skroniowo-żuchwowe i mięśnie żucia.

- Informacje: symetria i obrzęki; zmiany skórne i na czerwieni wargowej; stan węzłów chłonnych; przesiewowo – SSŻ i mięśnie
- Wykrywa: obrzęki zapalne (zębopochodne); powiększone węzły chłonne (zapalne, nowotworowe); zmiany skórne i czerwieni wargowej (opryszczka, zajady, zmiany przedrakowe); objawy dysfunkcji SSŻ

**Wskazania** (rutynowe, diagnostyczne): badanie pierwszorazowe (23.0101); obrzęk, ból, uraz. Szczególnie: podejrzenie zakażenia zębopochodnego; palacze – czujność onkologiczna

**Przebieg**

1. **Oglądanie** – Oceń symetrię twarzy z przodu i z boku, zabarwienie skóry, obrzęki, przetoki skórne, czerwień wargową i kąciki ust.
2. **Palpacja węzłów chłonnych** – Obustronnie, przy lekko pochylonej głowie: podbródkowe, podżuchwowe, szyjne; oceń wielkość, bolesność, spoistość, przesuwalność.
3. **Przesiewowa ocena SSŻ i mięśni** – Palpacja okolicy stawów przy otwieraniu/zamykaniu, osłuchanie trzasków, palpacja mięśni żwaczy i skroniowych; przy objawach – osobne badanie SSŻ.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| twarz | symetria, obrzęki | `POLE-ZEW-TWARZ` |
| skóra | zmiany, przetoki | `POLE-ZEW-SKORA` |
| wargi | czerwień, kąciki | `POLE-ZEW-WARGI` |
| węzły chłonne | wielkość, bolesność, ruchomość | `POLE-ZEW-WEZLY` |
| SSŻ | przesiewowo | `POLE-ZEW-SSZ` |
| mięśnie żucia | bolesność | `POLE-ZEW-MIESNIE` |

**Przykład wyniku prawidłowego:** Twarz symetryczna, bez obrzęków. Skóra twarzy i czerwień wargowa bez zmian chorobowych. Węzły chłonne podżuchwowe i szyjne niewyczuwalne. Stawy skroniowo-żuchwowe i mięśnie żucia bez objawów w badaniu przesiewowym. (Przykład wyniku – wpisywany tylko po stwierdzeniu przez lekarza.)

**Przykłady nieprawidłowości:** obrzęk okolicy podżuchwowej / policzka; przetoka skórna; powiększony, bolesny węzeł chłonny podżuchwowy; twardy, nieprzesuwalny węzeł – wskazanie do dalszej diagnostyki; zmiana na czerwieni wargowej (np. rogowacenie, owrzodzenie); trzaski w SSŻ, bolesność mięśni

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Opis każdej oglądanej struktury (także bez odchyleń) — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- Wielkość, bolesność i przesuwalność powiększonego węzła chłonnego; skierowanie — *zalecenie kliniczne*, warunek: powiększony węzeł chłonny (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.0101 (element badania lekarskiego stomatologicznego) · ICD-10: —

*Samo badanie nie uzasadnia rozpoznania.*

**Szablony opisu**

**standardowy**

> BADANIE ZEWNĄTRZUSTNE: Twarz: {{POLE-ZEW-TWARZ}}. Skóra: {{POLE-ZEW-SKORA}}. Czerwień wargowa: {{POLE-ZEW-WARGI}}. Węzły chłonne: {{POLE-ZEW-WEZLY}}. SSŻ: {{POLE-ZEW-SSZ}}. Mięśnie żucia: {{POLE-ZEW-MIESNIE}}.

**skrocony**

> Zewnątrzustnie: twarz {{POLE-ZEW-TWARZ}}, węzły chłonne {{POLE-ZEW-WEZLY}}, SSŻ {{POLE-ZEW-SSZ}}.

**rozszerzony**

> BADANIE ZEWNĄTRZUSTNE: Twarz: {{POLE-ZEW-TWARZ}}. Skóra: {{POLE-ZEW-SKORA}}. Czerwień wargowa i kąciki ust: {{POLE-ZEW-WARGI}}. Węzły chłonne: {{POLE-ZEW-WEZLY}}. SSŻ: {{POLE-ZEW-SSZ}}. Mięśnie żucia: {{POLE-ZEW-MIESNIE}}. Opis odchyleń: {{POLE-ZEW-OPIS}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Badanie przedmiotowe wewnątrzustne (tkanki miękkie) (`BAD-WEWNATRZUSTNE`)

Krótko: **Wewnątrzustne** · kategoria: przedmiotowe · status: **draft**

**Cel.** Błona śluzowa przedsionka, policzków, języka, dna jamy ustnej, podniebienia, cieśni gardła; ślinianki i wędzidełka.

- Informacje: stan błony śluzowej; wydzielanie śliny; przyczepy wędzidełek
- Wykrywa: zmiany błony śluzowej (zapalne, urazowe, potencjalnie złośliwe); suchość jamy ustnej; nieprawidłowe przyczepy wędzidełek; przetoki dziąsłowe

**Wskazania** (rutynowe, diagnostyczne): każde badanie pierwszorazowe i kontrolne; dolegliwości ze strony błony śluzowej. Szczególnie: palacze, alkohol – czujność onkologiczna; protezy ruchome

**Przebieg**

1. **Systematyczne oglądanie** – Przy dobrym oświetleniu, z lusterkiem: wargi i przedsionek, policzki, język (grzbiet, brzegi, spód – z wysunięciem języka), dno jamy ustnej, podniebienie, cieśń gardła.
2. **Palpacja** – Palpacja dwuręczna dna jamy ustnej i policzków; ocena konsystencji zmian.
3. **Ślinianki i wędzidełka** – Ocena wypływu śliny z ujść, wilgotności błony śluzowej; przyczepy wędzidełek (test napięcia wargi).
4. **Zmiana na błonie śluzowej** – Przy stwierdzeniu zmiany – opis szczegółowy wg badania „Ocena zmiany na błonie śluzowej”.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| przedsionek, wargi, policzki | barwa, ciągłość, zmiany | `POLE-WEW-PRZEDSIONEK` |
| język | brzegi i spód – miejsca predylekcji raka | `POLE-WEW-JEZYK` |
| dno jamy ustnej | zmiany, konsystencja | `POLE-WEW-DNO` |
| podniebienie | zmiany, ubytki | `POLE-WEW-PODNIEBIENIE` |
| gardło | migdałki | `POLE-WEW-GARDLO` |
| ślinianki | wypływ śliny, suchość | `POLE-WEW-SLINIANKI` |
| wędzidełka | przyczep | `POLE-WEW-WEDZIDELKA` |

**Przykład wyniku prawidłowego:** Błona śluzowa przedsionka, policzków, języka, dna jamy ustnej i podniebienia różowa, wilgotna, bez zmian chorobowych. Ujścia ślinianek bez zmian, ślina przejrzysta. Wędzidełka bez zaburzeń przyczepu. (Przykład – tylko po stwierdzeniu przez lekarza.)

**Przykłady nieprawidłowości:** biała lub czerwona plama niedająca się zetrzeć (leukoplakia / erytroplakia – wymaga dalszej diagnostyki); owrzodzenie utrzymujące się > 2 tygodnie; nadżerki, pęcherze; odleżyna protetyczna; suchość jamy ustnej; wysoki przyczep wędzidełka wargi

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Opis każdej zmiany: lokalizacja, wielkość, barwa, powierzchnia, konsystencja, bolesność — *zalecenie kliniczne* (`SRC-KLIN-OPMD-2021` (PMID 33128420))

**Zależne od sytuacji**

- Skierowanie (chirurgia stomatologiczna, periodontologia, onkologia) i termin kontroli zmiany — *zalecenie kliniczne*, warunek: zmiana podejrzana lub utrzymująca się > 2 tygodnie (`SRC-KLIN-OPMD-2021` (PMID 33128420))

**Powiązania** – ICD-9: 23.0101 (element badania lekarskiego stomatologicznego) · ICD-10: K13.2 (tylko gdy lekarz rozpozna leukoplakię / zmiany nabłonka); K12.0 (nawracające afty – rozpoznanie lekarza)

*Rozpoznanie wyłącznie przy stwierdzonej zmianie.*

**Szablony opisu**

**standardowy**

> BADANIE WEWNĄTRZUSTNE: Przedsionek, wargi, policzki: {{POLE-WEW-PRZEDSIONEK}}. Język: {{POLE-WEW-JEZYK}}. Dno jamy ustnej: {{POLE-WEW-DNO}}. Podniebienie: {{POLE-WEW-PODNIEBIENIE}}. Gardło: {{POLE-WEW-GARDLO}}. Ślinianki: {{POLE-WEW-SLINIANKI}}. Wędzidełka: {{POLE-WEW-WEDZIDELKA}}.

**skrocony**

> Wewnątrzustnie: błona śluzowa {{POLE-WEW-PRZEDSIONEK}}, język {{POLE-WEW-JEZYK}}, wędzidełka {{POLE-WEW-WEDZIDELKA}}.

**rozszerzony**

> BADANIE WEWNĄTRZUSTNE: Przedsionek, wargi, policzki: {{POLE-WEW-PRZEDSIONEK}}. Język: {{POLE-WEW-JEZYK}}. Dno jamy ustnej: {{POLE-WEW-DNO}}. Podniebienie: {{POLE-WEW-PODNIEBIENIE}}. Gardło: {{POLE-WEW-GARDLO}}. Ślinianki: {{POLE-WEW-SLINIANKI}}. Wędzidełka: {{POLE-WEW-WEDZIDELKA}}. Opis zmian: {{POLE-WEW-OPIS}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-OPMD-2021` (PMID 33128420); `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Ocena zmiany na błonie śluzowej jamy ustnej (`BAD-BLONA`)

Krótko: **Błona śluzowa – zmiana** · kategoria: specjalistyczne · status: **draft**

**Cel.** Opis morfologiczny stwierdzonej zmiany i ocena jej charakteru.

- Informacje: morfologia wykwitu; czas trwania i czynnik miejscowy; cechy niepokojące
- Wykrywa: zmiany potencjalnie złośliwe (leukoplakia, erytroplakia, liszaj płaski); zmiany urazowe i protetyczne; zmiany zapalne i infekcyjne (kandydoza, opryszczka, afty)

**Wskazania** (diagnostyczne): stwierdzenie zmiany w badaniu wewnątrzustnym; dolegliwości ze strony błony śluzowej. Szczególnie: zmiana > 2 tygodnie mimo usunięcia czynnika; palacze, alkohol, HPV; twardy naciek, owrzodzenie bez bólu

**Przebieg**

1. **Wywiad dotyczący zmiany** – Czas trwania, nawroty, ból, czynniki (proteza, urazy, leki, palenie).
2. **Opis morfologiczny** – Lokalizacja, wielkość (mm), rodzaj wykwitu, barwa, powierzchnia, granice; próba starcia nalotu.
3. **Palpacja** – Konsystencja, naciek podstawy, bolesność; węzły chłonne regionalne.
4. **Dokumentacja fotograficzna** – Zdjęcie zmiany (jeśli możliwe) – na urządzeniu; zdjęcia nie trafiają na serwer (zasada nr 1).
5. **Decyzja** – Usunięcie czynnika miejscowego i kontrola za ok. 2 tygodnie albo skierowanie; przy cechach niepokojących – bez zwłoki.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| lokalizacja i wielkość | miejsce, mm | `POLE-BL-LOK` |
| wykwit | rodzaj | `POLE-BL-WYKWIT` |
| powierzchnia | gładka / nierówna, ścieralność nalotu | `POLE-BL-POW` |
| konsystencja | naciek | `POLE-BL-KONS` |
| bolesność | ból | `POLE-BL-BOL` |
| czas trwania | tygodnie | `POLE-BL-CZAS` |

**Przykład wyniku prawidłowego:** Nie dotyczy – badanie wykonuje się przy stwierdzonej zmianie.

**Przykłady nieprawidłowości:** plama biała niedająca się zetrzeć, niezwiązana z czynnikiem miejscowym; plama czerwona o aksamitnej powierzchni; owrzodzenie z twardym naciekiem podstawy; zmiana utrzymująca się > 2 tygodnie po usunięciu czynnika

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Pełny opis morfologiczny zmiany i decyzja — *zalecenie kliniczne* (`SRC-KLIN-OPMD-2021` (PMID 33128420))

**Zależne od sytuacji**

- Skierowanie i termin kontroli — *zalecenie kliniczne*, warunek: zmiana niepokojąca (`SRC-KLIN-OPMD-2021` (PMID 33128420))

**Powiązania** – ICD-9: 23.1605 (gdy po ocenie wykonano leczenie zmian na błonie śluzowej) · ICD-10: K13.2 (leukoplakia i inne zaburzenia nabłonka – rozpoznanie lekarza); K12.0 (afty nawracające); K12.1 (inne postacie zapalenia jamy ustnej); K13.0 (choroby warg); K14.0 (zapalenie języka)

*Rozpoznanie histopatologiczne zmian podejrzanych – poza gabinetem; w aplikacji tylko opis i decyzja.*

**Szablony opisu**

**standardowy**

> Zmiana na błonie śluzowej: lokalizacja {{POLE-BL-LOK}}, wymiar {{POLE-BL-WYM}} mm, {{POLE-BL-WYKWIT}}, powierzchnia {{POLE-BL-POW}}, konsystencja {{POLE-BL-KONS}}, {{POLE-BL-BOL}}. Czas trwania: {{POLE-BL-CZAS}}. Postępowanie: {{POLE-BL-DECYZJA}}.

**skrocony**

> Zmiana: {{POLE-BL-LOK}}, {{POLE-BL-WYKWIT}}, {{POLE-BL-WYM}} mm. Postępowanie: {{POLE-BL-DECYZJA}}.

**rozszerzony**

> OCENA ZMIANY NA BŁONIE ŚLUZOWEJ: Lokalizacja: {{POLE-BL-LOK}}. Wymiar: {{POLE-BL-WYM}} mm. Wykwit: {{POLE-BL-WYKWIT}}. Powierzchnia: {{POLE-BL-POW}}. Konsystencja: {{POLE-BL-KONS}}. Bolesność: {{POLE-BL-BOL}}. Czas trwania: {{POLE-BL-CZAS}}. Czynnik miejscowy: {{POLE-BL-CZYNNIK}}. Węzły chłonne: {{POLE-ZEW-WEZLY}}. Postępowanie: {{POLE-BL-DECYZJA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła:** `SRC-KLIN-OPMD-2021` (PMID 33128420); `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Badanie uzębienia (stan zębów stałych i mlecznych) (`BAD-UZEBIENIE`)

Krótko: **Uzębienie** · kategoria: przedmiotowe · status: **draft**

**Cel.** Każdy ząb: obecność, próchnica (aktywność, głębokość), wypełnienia i ich szczelność, uzupełnienia protetyczne, leczenie kanałowe, zmiany niepróchnicowe.

- Informacje: diagram zębów; wskaźnik DMFT/dmft; ryzyko próchnicy
- Wykrywa: próchnica pierwotna i wtórna; nieszczelne wypełnienia; zmiany niepróchnicowe (erozje, abfrakcje, starcie, MIH); braki zębowe; zęby wymagające diagnostyki endodontycznej

**Wskazania** (rutynowe, kontrolne): badanie pierwszorazowe i kontrolne; przed planem leczenia. Szczególnie: wysokie ryzyko próchnicy; dzieci w okresie uzębienia mieszanego

**Przebieg**

1. **Przygotowanie** – Usunięcie płytki z powierzchni (jeśli konieczne), osuszenie zębów, dobre oświetlenie, lusterko, zgłębnik z kulką (WHO) – bez nacisku na zdemineralizowane szkliwo.
2. **Ocena systematyczna** – Ząb po zębie w ustalonej kolejności (od 18 do 48 / od 55 do 85); powierzchnie żujące, styczne, gładkie.
3. **Klasyfikacja zmian** – Próchnica wg ICDAS (kod 0–6) lub opisowo; aktywność zmian; wypełnienia (szczelność, próchnica wtórna).
4. **Uzupełnienie diagnostyki** – Przy podejrzeniu zmian stycznych lub głębokich – RTG zgryzowo-skrzydłowe; przy objawach miazgowych – testy żywotności.
5. **Ocena ryzyka i plan** – Ocena ryzyka próchnicy (dieta, higiena, fluorki, ślina, aktywne zmiany) i propozycja planu leczenia.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| diagram | stan każdego zęba | `POLE-UZ-DIAGRAM` |
| próchnica | kryteria ICDAS / opisowe | `POLE-UZ-SYSTEM` |
| DMFT | liczba zębów D/M/F | `POLE-UZ-DMFT` |
| zmiany niepróchnicowe | starcie, erozje, MIH | `POLE-UZ-NIEPROCH` |
| ryzyko próchnicy | ocena lekarza | `POLE-UZ-RYZYKO` |

**Przykład wyniku prawidłowego:** Uzębienie stałe pełne, bez ognisk próchnicy i zmian niepróchnicowych; wypełnienia szczelne. DMFT = 0. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** próchnica w obrębie szkliwa (ICDAS 1–2) – leczenie nieinwazyjne; ubytek próchnicowy w zębinie (ICDAS 5–6); próchnica wtórna przy wypełnieniu; MIH pierwszych trzonowców; starcie patologiczne (bruksizm); erozje (dieta, refluks)

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Stan uzębienia (diagram) z oznaczeniem zębów wg FDI — *NFZ*, warunek: rozliczenie NFZ – lokalizacja zębów (`SRC-NFZ-KOM-6113`)

**Zalecane**

- Kryteria oceny próchnicy i aktywność zmian — *zalecenie kliniczne* (`SRC-KLIN-ICDAS-2007` (PMID 17518963))
- Ocena ryzyka próchnicy i plan profilaktyki — *zalecenie kliniczne* (`SRC-KLIN-EAPD-F-2019` (PMID 31631242))

**Zależne od sytuacji**

- Zlecenie RTG z uzasadnieniem — *zalecenie kliniczne*, warunek: podejrzenie zmian niewidocznych klinicznie (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.0101 (w ramach badania lekarskiego); 23.0102 (w ramach badania kontrolnego) · ICD-10: K02.0 (próchnica ograniczona do szkliwa – rozpoznanie lekarza); K02.1 (próchnica zębiny); K03.0 (nadmierne starcie); K03.2 (erozja); K00.4 (zaburzenia rozwoju zębów (np. MIH – do weryfikacji kodu)); K08.1 (utrata zębów (wypadek, ekstrakcja, choroba przyzębia))

*Rozpoznanie dotyczy konkretnego zęba i tylko przy stwierdzonej zmianie.*

**Szablony opisu**

**standardowy**

> UZĘBIENIE ({{POLE-UZ-TYP}}): {{POLE-UZ-DIAGRAM}}. Ocena próchnicy: {{POLE-UZ-SYSTEM}}. DMFT/dmft: {{POLE-UZ-DMFT}}. Zmiany niepróchnicowe: {{POLE-UZ-NIEPROCH}}.

**skrocony**

> Uzębienie: {{POLE-UZ-DIAGRAM}}.

**rozszerzony**

> UZĘBIENIE ({{POLE-UZ-TYP}}): {{POLE-UZ-DIAGRAM}}. Kryteria: {{POLE-UZ-SYSTEM}}. DMFT/dmft: {{POLE-UZ-DMFT}}. Zmiany niepróchnicowe: {{POLE-UZ-NIEPROCH}}. Ryzyko próchnicy: {{POLE-UZ-RYZYKO}}. Opis: {{POLE-UZ-OPIS}}. RTG: {{POLE-RTG}}. Plan: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-KLIN-EAPD-F-2019` (PMID 31631242); `SRC-NFZ-KOM-6113`; `SRC-DU-2026-1391`

## Ocena stanu przyzębia (`BAD-PRZYZEBIE`)

Krótko: **Przyzębie** · kategoria: przedmiotowe · status: **draft**

**Cel.** Dziąsło i tkanki przyzębia: krwawienie, kieszonki, utrata przyczepu, recesje, ruchomość, furkacje.

- Informacje: wynik badania przesiewowego; BOP %; PPD i CAL; stadium i stopień zapalenia przyzębia
- Wykrywa: zapalenie dziąseł; zapalenie przyzębia i jego zaawansowanie; recesje dziąsłowe; zmiany w furkacjach; ruchomość patologiczną

**Wskazania** (rutynowe, diagnostyczne, kontrolne): każde badanie pierwszorazowe (przesiewowo); krwawienie dziąseł, ruchomość zębów; przed leczeniem protetycznym i implantologicznym. Szczególnie: cukrzyca, palenie; BPE 3–4 – pełne badanie periodontologiczne

**Przebieg**

1. **Badanie przesiewowe** – Sonda WHO/BPE, 6 sekstantów, najwyższy wynik w sekstancie (0–4, * przy furkacji).
2. **Pełne badanie (przy BPE 3–4 lub objawach)** – Sonda periodontologiczna, 6 punktów na ząb: PPD, recesja (CAL = PPD + recesja), BOP; ruchomość (Miller), furkacje (Hamp).
3. **RTG** – Ocena utraty kości (pantomogram / zdjęcia wewnątrzustne) – wg wskazań.
4. **Klasyfikacja** – Rozpoznanie wg klasyfikacji 2017: zdrowie / zapalenie dziąseł / zapalenie przyzębia – stadium (I–IV) i stopień (A–C).

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| BPE/PSR | sekstanty | `POLE-PZ-BPE` |
| BOP | % miejsc | `POLE-PZ-BOP` |
| PPD | kieszonki ≥ 4 mm | `POLE-PZ-PPD` |
| CAL / recesje | utrata przyczepu | `POLE-PZ-CAL` |
| ruchomość | stopień | `POLE-PZ-RUCH` |
| furkacje | stopień | `POLE-PZ-FURK` |

**Przykład wyniku prawidłowego:** BPE 0 we wszystkich sekstantach; BOP < 10%, brak kieszonek > 3 mm, brak utraty przyczepu i ruchomości – przyzębie zdrowe (klasyfikacja 2017). (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** BOP ≥ 10% bez utraty przyczepu – zapalenie dziąseł; kieszonki ≥ 4 mm z utratą przyczepu – zapalenie przyzębia (stadium/stopień); recesje dziąsłowe; zajęcie furkacji II–III stopnia; ruchomość II–III stopnia

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Wyniki BPE/PSR lub karta periodontologiczna (PPD, CAL, BOP) — *zalecenie kliniczne* (`SRC-KLIN-EFP-S3-2020` (PMID 32383274))
- Rozpoznanie wg klasyfikacji 2017 (stadium, stopień) — *zalecenie kliniczne* (`SRC-KLIN-PERIO-2018` (PMID 29926490))

**Zależne od sytuacji**

- Plan leczenia periodontologicznego (etapy wg EFP) — *zalecenie kliniczne*, warunek: zapalenie przyzębia (`SRC-KLIN-EFP-S3-2020` (PMID 32383274))

**Powiązania** – ICD-9: 23.0101 (w ramach badania lekarskiego) · ICD-10: K05.1 (przewlekłe zapalenie dziąseł – rozpoznanie lekarza); K05.3 (przewlekłe zapalenie przyzębia); K05.2 (ostre zapalenie przyzębia / ropień przyzębny); K06.0 (recesja dziąsła)

*Odpowiedniość klasyfikacji 2017 ↔ ICD-10 jest przybliżona – wybór kodu należy do lekarza.*

**Szablony opisu**

**standardowy**

> PRZYZĘBIE: BPE/PSR: {{POLE-PZ-BPE}}. BOP: {{POLE-PZ-BOP}}%. Kieszonki ≥ 4 mm: {{POLE-PZ-PPD}}. Ocena: {{POLE-PZ-ROZPOZNANIE}}.

**skrocony**

> Przyzębie: BPE {{POLE-PZ-BPE}}, BOP {{POLE-PZ-BOP}}%; {{POLE-PZ-ROZPOZNANIE}}.

**rozszerzony**

> BADANIE PERIODONTOLOGICZNE: BPE/PSR: {{POLE-PZ-BPE}}. BOP: {{POLE-PZ-BOP}}%. PPD (≥ 4 mm): {{POLE-PZ-PPD}}. CAL / recesje: {{POLE-PZ-CAL}}. Ruchomość: {{POLE-PZ-RUCH}}. Furkacje: {{POLE-PZ-FURK}}. RTG: {{POLE-RTG}}. Rozpoznanie: {{POLE-PZ-ROZPOZNANIE}}, stadium {{POLE-PZ-STADIUM}}, stopień {{POLE-PZ-STOPIEN}}. Plan: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-EFP-S3-2020` (PMID 32383274); `SRC-KLIN-PERIO-2018` (PMID 29926490); `SRC-KLIN-GING-2018` (PMID 29926499); `SRC-KLIN-KLASYF-2018` (PMID 29926489); `SRC-DU-2026-1391`

## Ocena higieny jamy ustnej (wskaźniki płytki i stanu dziąseł) (`BAD-HIGIENA`)

Krótko: **Higiena** · kategoria: przedmiotowe · status: **draft**

**Cel.** Ilość i rozmieszczenie płytki nazębnej, złogi, stan zapalny dziąseł.

- Informacje: wskaźnik płytki (API/PCR); wskaźnik dziąsłowy; rodzaj złogów
- Wykrywa: niewystarczającą higienę; miejsca zaniedbane (powierzchnie styczne); zapalenie dziąseł związane z płytką

**Wskazania** (rutynowe, kontrolne): badanie pierwszorazowe (23.0101 obejmuje instruktaż); przed i po higienizacji; kontrola motywacji. Szczególnie: leczenie ortodontyczne; zapalenie przyzębia; wysokie ryzyko próchnicy

**Przebieg**

1. **Wybarwienie płytki (opcjonalnie)** – Płyn / tabletka wybarwiająca; płukanie wodą.
2. **Wskaźnik płytki** – API: obecność płytki na powierzchniach stycznych (zgłębnik) w kwadrantach; PCR: 4 powierzchnie każdego zęba, wynik w %.
3. **Wskaźnik dziąsłowy** – GI (0–3) lub krwawienie z brodawek (SBI).
4. **Instruktaż** – Pokaż technikę szczotkowania i oczyszczania przestrzeni międzyzębowych dostosowaną do pacjenta; zalecenia dot. fluorków.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| płytka | wskaźnik i wartość | `POLE-HG-WARTOSC` |
| dziąsła | GI / SBI | `POLE-HG-GI` |
| złogi | rodzaj i lokalizacja | `POLE-HG-ZLOGI` |

**Przykład wyniku prawidłowego:** API 15%, płytka pojedynczo na powierzchniach stycznych, brak kamienia; GI 0 – higiena dobra. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** API > 40% – higiena niedostateczna; kamień naddziąsłowy na powierzchniach językowych siekaczy dolnych; krwawienie z brodawek; przebarwienia (palenie, kawa, chlorheksydyna)

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Instruktaż higieny jamy ustnej – fakt przeprowadzenia (część świadczenia 23.0101) — *NFZ*, warunek: rozliczenie 23.0101 / ST33 (`SRC-DU-2025-615`)

**Zalecane**

- Wartość wskaźnika płytki i dziąsłowego — *zalecenie kliniczne* (`SRC-KLIN-PCR-1972` (PMID 4500182); `SRC-KLIN-GI-1963` (PMID 14121956))

**Zależne od sytuacji**

- Zakres instruktażu dla pacjenta z aparatem / protezą — *zalecenie kliniczne*, warunek: aparat ortodontyczny, uzupełnienia protetyczne (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.08 (instruktaż higieny jako samodzielna czynność); 23.0101 (badanie lekarskie obejmuje instruktaż higieny) · ICD-10: K03.6 (złogi nazębne – rozpoznanie lekarza); K05.1 (przewlekłe zapalenie dziąseł) · reguły NFZ: R-BAD-01

**Szablony opisu**

**standardowy**

> HIGIENA JAMY USTNEJ: {{POLE-HG-WSKAZNIK}} {{POLE-HG-WARTOSC}}%, GI/SBI {{POLE-HG-GI}}. Złogi: {{POLE-HG-ZLOGI}}. Ocena: {{POLE-HG-OCENA}}. Instruktaż higieny: {{POLE-HG-INSTRUKTAZ}}.

**skrocony**

> Higiena: {{POLE-HG-WSKAZNIK}} {{POLE-HG-WARTOSC}}%, złogi {{POLE-HG-ZLOGI}}; instruktaż: {{POLE-HG-INSTRUKTAZ}}.

**rozszerzony**

> HIGIENA JAMY USTNEJ: {{POLE-HG-WSKAZNIK}} {{POLE-HG-WARTOSC}}%, GI/SBI {{POLE-HG-GI}}. Złogi: {{POLE-HG-ZLOGI}}. Ocena: {{POLE-HG-OCENA}}. Instruktaż: {{POLE-HG-INSTRUKTAZ}} – {{POLE-HG-INSTR-OPIS}}. Zalecenia: {{POLE-ZALECENIA}}.

**Źródła:** `SRC-KLIN-PCR-1972` (PMID 4500182); `SRC-KLIN-GI-1963` (PMID 14121956); `SRC-KLIN-GING-2018` (PMID 29926499); `SRC-DU-2025-615`; `SRC-DU-2026-1391`

## Badanie zgryzu i warunków zwarciowych (`BAD-ZGRYZ`)

Krótko: **Zgryz** · kategoria: przedmiotowe · status: **draft**

**Cel.** Relacje łuków zębowych w zwarciu i ruchach żuchwy.

- Informacje: klasa Angle’a; nagryz pionowy i poziomy; linia pośrodkowa; prowadzenie; wady zgryzu
- Wykrywa: wady zgryzu wymagające konsultacji ortodontycznej; kontakty przedwczesne; urazy zgryzowe

**Wskazania** (rutynowe, diagnostyczne): badanie pierwszorazowe; przed leczeniem protetycznym i rozległymi odbudowami; dzieci – okres uzębienia mieszanego. Szczególnie: starcie, bruksizm; dolegliwości SSŻ

**Przebieg**

1. **Zwarcie centralne** – Oceń klasę Angle’a (pierwsze trzonowce i kły), overjet, overbite, linię pośrodkową.
2. **Ruchy żuchwy** – Protruzja i ruchy boczne – prowadzenie kłowe / grupowe, kontakty po stronie nieżującej (kalka zgryzowa).
3. **Wady i decyzja** – Odnotuj wady; u dzieci – rozważ skierowanie do ortodonty.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| klasa Angle’a | relacja trzonowcowa | `POLE-ZG-ANGLE` |
| overjet | mm | `POLE-ZG-OJ` |
| overbite | mm | `POLE-ZG-OB` |
| wady | rodzaj | `POLE-ZG-WADY` |
| prowadzenie | kłowe / grupowe | `POLE-ZG-PROWADZENIE` |

**Przykład wyniku prawidłowego:** Klasa I Angle’a obustronnie, overjet 2 mm, overbite 2 mm, linia pośrodkowa zgodna, prowadzenie kłowe. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** klasa II/III Angle’a; zgryz krzyżowy boczny; zgryz otwarty przedni; kontakty przedwczesne; przesunięcie linii pośrodkowej

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Klasa Angle’a, overjet, overbite, wady — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- Skierowanie do ortodonty — *zalecenie kliniczne*, warunek: wada zgryzu u dziecka (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.0101 (w ramach badania lekarskiego); 23.1022 (profilaktyczne świadczenie zapobiegające wadom zgryzu (warunki NFZ – zał. 1)) · ICD-10: K07.2 (anomalie relacji łuków – rozpoznanie lekarza); K07.3 (anomalie położenia zębów)

**Szablony opisu**

**standardowy**

> ZGRYZ: klasa Angle’a {{POLE-ZG-ANGLE}}, overjet {{POLE-ZG-OJ}} mm, overbite {{POLE-ZG-OB}} mm, linia pośrodkowa {{POLE-ZG-LINIA}}. Wady: {{POLE-ZG-WADY}}.

**skrocony**

> Zgryz: kl. {{POLE-ZG-ANGLE}}, wady: {{POLE-ZG-WADY}}.

**rozszerzony**

> ZGRYZ: klasa Angle’a {{POLE-ZG-ANGLE}}, overjet {{POLE-ZG-OJ}} mm, overbite {{POLE-ZG-OB}} mm, linia pośrodkowa {{POLE-ZG-LINIA}}. Prowadzenie: {{POLE-ZG-PROWADZENIE}}. Wady: {{POLE-ZG-WADY}}. Opis: {{POLE-ZG-OPIS}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Badanie stawów skroniowo-żuchwowych i mięśni żucia (`BAD-SSZ`)

Krótko: **SSŻ** · kategoria: specjalistyczne · status: **draft**

**Cel.** Funkcja i dolegliwości stawów skroniowo-żuchwowych oraz mięśni żucia.

- Informacje: ból (lokalizacja, „ból znany”); zakres i tor odwodzenia; odgłosy stawowe; zablokowania
- Wykrywa: ból mięśniowo-powięziowy; artralgię; przemieszczenia krążka; ograniczenie otwierania

**Wskazania** (diagnostyczne): dolegliwości bólowe twarzy, uszu, skroni; trzaski, zablokowania; przed leczeniem protetycznym / ortodontycznym. Szczególnie: bruksizm; bóle głowy

**Przebieg**

1. **Wywiad** – Ból w ostatnich 30 dniach, wpływ ruchów żuchwy, zablokowania, bóle głowy (DC/TMD oś I – skrócone).
2. **Pomiar odwodzenia** – Linijką między brzegami siecznymi: bez bólu, maksymalne czynne, z pomocą; tor ruchu.
3. **Odgłosy** – Palpacja / osłuchanie stawu podczas otwierania, zamykania, ruchów bocznych.
4. **Palpacja** – Żwacze, mięśnie skroniowe, boczne bieguny stawów (ok. 1 kg nacisku); czy ból jest „znany” pacjentowi.
5. **Wstępna ocena** – Opis objawów; rozpoznanie wg DC/TMD lub skierowanie (protetyk / specjalista zaburzeń czynnościowych).

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| ból | lokalizacja, ból znany | `POLE-SSZ-BOL` |
| odwodzenie | mm | `POLE-SSZ-ODWODZENIE` |
| tor | zbaczanie | `POLE-SSZ-TOR` |
| odgłosy | trzaski, trzeszczenia | `POLE-SSZ-ODGLOSY` |
| palpacja | mięśnie i staw | `POLE-SSZ-PALPACJA` |

**Przykład wyniku prawidłowego:** Pacjent nie zgłasza bólu; odwodzenie 45 mm bez bólu, tor prosty, bez odgłosów stawowych; palpacja mięśni i stawów niebolesna. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** odwodzenie < 40 mm; zbaczanie toru; trzask wzajemny (otwieranie i zamykanie); ból znany przy palpacji żwacza; zablokowanie otwierania

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Odwodzenie w mm, tor, odgłosy, wynik palpacji — *zalecenie kliniczne* (`SRC-KLIN-DCTMD-2014` (PMID 24482784))

**Zależne od sytuacji**

- Skierowanie / plan (szyna, fizjoterapia) — *zalecenie kliniczne*, warunek: objawy TMD (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.0105 (konsultacja specjalistyczna – jeśli dotyczy); 23.2902 (szyna zgryzowa (płytka relaksacyjna) – leczenie po rozpoznaniu) · ICD-10: K07.6 (zaburzenia stawu skroniowo-żuchwowego – rozpoznanie lekarza)

**Szablony opisu**

**standardowy**

> SSŻ: ból {{POLE-SSZ-BOL}}; odwodzenie {{POLE-SSZ-ODWODZENIE}} mm, tor {{POLE-SSZ-TOR}}; odgłosy {{POLE-SSZ-ODGLOSY}}; palpacja: {{POLE-SSZ-PALPACJA}}.

**skrocony**

> SSŻ: ból {{POLE-SSZ-BOL}}, odwodzenie {{POLE-SSZ-ODWODZENIE}} mm, odgłosy {{POLE-SSZ-ODGLOSY}}.

**rozszerzony**

> BADANIE SSŻ (wg DC/TMD – skrócone): ból {{POLE-SSZ-BOL}}; odwodzenie {{POLE-SSZ-ODWODZENIE}} mm, tor {{POLE-SSZ-TOR}}; odgłosy {{POLE-SSZ-ODGLOSY}}; zablokowanie {{POLE-SSZ-ZABLOK}}; palpacja: {{POLE-SSZ-PALPACJA}}. Ocena: {{POLE-SSZ-OPIS}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-DCTMD-2014` (PMID 24482784); `SRC-DU-2026-1391`

## Badanie żywotności zęba (testy miazgowe i okołowierzchołkowe) (`BAD-ZYWOTNOSC`)

Krótko: **Żywotność zęba** · kategoria: specjalistyczne · status: **draft**

**Cel.** Reakcja miazgi na bodźce i stan tkanek okołowierzchołkowych.

- Informacje: wynik testu na zimno / EPT; opukiwanie i palpacja; porównanie z zębem kontrolnym
- Wykrywa: odwracalne i nieodwracalne zapalenie miazgi; martwicę miazgi; zapalenie tkanek okołowierzchołkowych

**Wskazania** (diagnostyczne, kontrolne): ból zęba; przed leczeniem głębokiej próchnicy, protetycznym (filary); po urazie (kontrole wg IADT). Szczególnie: zęby po urazie – pierwszy wynik może być fałszywie ujemny; zęby z rozległymi wypełnieniami / koronami

**Przebieg**

1. **Wybór zęba kontrolnego** – Ząb jednoimienny lub sąsiedni, zdrowy – badany najpierw.
2. **Test na zimno** – Osuszony ząb, wacik z czynnikiem chłodzącym na powierzchnię wargową/policzkową; oceń reakcję i czas jej trwania.
3. **EPT (opcjonalnie)** – Przy niejednoznacznym teście termicznym; elektroda na osuszonym szkliwie z żelem przewodzącym.
4. **Opukiwanie i palpacja** – Opukiwanie pionowe i poziome, palpacja okolicy wierzchołka; test nagryzania przy podejrzeniu pęknięcia.
5. **Ocena** – Zestawienie z wywiadem i RTG; ocena stanu miazgi.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| zimno | reakcja i czas | `POLE-ZY-ZIMNO` |
| EPT | wynik | `POLE-ZY-EPT` |
| opukiwanie | ból | `POLE-ZY-OPUK` |
| palpacja | okolica wierzchołka | `POLE-ZY-PALP` |
| ząb kontrolny | porównanie | `POLE-ZY-KONTROLA` |

**Przykład wyniku prawidłowego:** Ząb 36: test na zimno dodatni, reakcja krótkotrwała, porównywalna z zębem 46; opukiwanie i palpacja niebolesne. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** reakcja przedłużona po ustaniu bodźca – nieodwracalne zapalenie miazgi; brak reakcji na zimno i EPT – podejrzenie martwicy (potwierdzić RTG / klinicznie); bolesne opukiwanie pionowe – zapalenie tkanek okołowierzchołkowych; ból przy nagryzaniu – podejrzenie pęknięcia

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Ząb badany (FDI) i wynik każdego testu — *NFZ*, warunek: rozliczenie 23.02 (`SRC-DU-2025-615`)

**Zalecane**

- Ząb kontrolny i jego wynik — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))

**Zależne od sytuacji**

- Plan kolejnych testów (np. po urazie: 4 tyg., 3 mies. …) — *zalecenie kliniczne*, warunek: uraz zęba (`SRC-KLIN-IADT-ZLAM-2020` (PMID 32475015))

**Powiązania** – ICD-9: 23.02 (badanie żywotności zęba – świadczenie) · ICD-10: K04.0 (zapalenie miazgi – rozpoznanie lekarza); K04.1 (martwica miazgi); K04.4 (ostre zapalenie tkanek okołowierzchołkowych); K04.5 (przewlekłe zapalenie okołowierzchołkowe (ziarniniak))

**Szablony opisu**

**standardowy**

> BADANIE ŻYWOTNOŚCI zęba {{POLE-ZAB}}: test na zimno {{POLE-ZY-ZIMNO}}; opukiwanie {{POLE-ZY-OPUK}}; palpacja {{POLE-ZY-PALP}}. Ząb kontrolny: {{POLE-ZY-KONTROLA}}. Ocena: {{POLE-ZY-OCENA}}.

**skrocony**

> Żywotność {{POLE-ZAB}}: zimno {{POLE-ZY-ZIMNO}}, opukiwanie {{POLE-ZY-OPUK}}.

**rozszerzony**

> BADANIE ŻYWOTNOŚCI zęba {{POLE-ZAB}}: test na zimno {{POLE-ZY-ZIMNO}}; EPT {{POLE-ZY-EPT}}; opukiwanie {{POLE-ZY-OPUK}}; palpacja {{POLE-ZY-PALP}}; test nagryzania {{POLE-ZY-NAGRYZ}}. Ząb kontrolny: {{POLE-ZY-KONTROLA}}. RTG: {{POLE-RTG}}. Ocena: {{POLE-ZY-OCENA}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-ESE-S3-2023` (PMID 37772327); `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-IADT-ZLAM-2020` (PMID 32475015); `SRC-DU-2025-615`; `SRC-DU-2026-1391`

## Ocena radiologiczna (opis zdjęcia RTG) (`BAD-RTG`)

Krótko: **Opis RTG** · kategoria: specjalistyczne · status: **draft**

**Cel.** Struktury niewidoczne klinicznie: przestrzenie styczne, korzenie, ozębna, kość wyrostka, zęby zatrzymane.

- Informacje: rodzaj zdjęcia i wskazanie; opis zmian
- Wykrywa: próchnicę styczną i wtórną; zmiany okołowierzchołkowe; utratę kości; zęby zatrzymane, torbiele; jakość wypełnienia kanałowego

**Wskazania** (diagnostyczne, kontrolne): wg wskazań klinicznych (nie rutynowo); leczenie endodontyczne (przed, w trakcie, po); przed ekstrakcją chirurgiczną; diagnostyka próchnicy stycznej. Szczególnie: ciąża – tylko przy pilnym wskazaniu, z ochroną

**Przebieg**

1. **Uzasadnienie** – Ustal wskazanie (zasada uzasadnienia); u kobiet w wieku rozrodczym – wywiad w kierunku ciąży.
2. **Wykonanie** – Zgodnie z procedurami pracowni RTG gabinetu; osłony wg obowiązujących procedur.
3. **Opis** – Systematycznie: jakość zdjęcia, zęby (korony, korzenie, kanały, wypełnienia), ozębna i blaszka zbita, kość wyrostka, inne struktury.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| wskazanie | uzasadnienie | `POLE-RTG-WSKAZANIE` |
| opis | wynik | `POLE-RTG-OPIS` |

**Przykład wyniku prawidłowego:** Zdjęcie zgryzowo-skrzydłowe strony prawej: bez cech próchnicy stycznej, wyrostek bez cech utraty kości. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** przejaśnienie okołowierzchołkowe; poszerzenie szpary ozębnej; próchnica styczna w zębinie; niedopełnione wypełnienie kanałowe; ząb zatrzymany

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis zdjęcia w dokumentacji (warunek rozliczenia RTG) — *NFZ*, warunek: rozliczenie 23.0301–23.0304 (`SRC-DU-2025-615`)
- Uzasadnienie wykonania — *prawne*, warunek: każde zdjęcie (prawo atomowe – do weryfikacji aktu) (`SRC-PRAKTYKA`)

**Zalecane**

- Rodzaj zdjęcia i data — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- —

**Powiązania** – ICD-9: 23.0301 (do 2 zdjęć wewnątrzustnych); 23.0302 (do 5 zdjęć); 23.0303 (do 8 zdjęć); 23.0304 (pantomogram z opisem) · ICD-10: — · reguły NFZ: R-RTG-01, R-RTG-02, R-RTG-03

*Rozpoznanie wynika z całości badania, nie z samego zdjęcia.*

**Szablony opisu**

**standardowy**

> RTG ({{POLE-RTG-RODZAJ}}), wskazanie: {{POLE-RTG-WSKAZANIE}}. Opis: {{POLE-RTG-OPIS}}.

**skrocony**

> RTG {{POLE-RTG-RODZAJ}}: {{POLE-RTG-OPIS}}.

**rozszerzony**

> OCENA RADIOLOGICZNA – {{POLE-RTG-RODZAJ}} z dnia {{POLE-DATA}}. Wskazanie: {{POLE-RTG-WSKAZANIE}}. Opis: {{POLE-RTG-OPIS}}. Wnioski / decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-DU-2025-615`; `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

*Uwagi: Wymagania prawa atomowego (uzasadnienie, ochrona radiologiczna) – akt nieopisany w audycie; oznaczone do weryfikacji.*

## Badanie stomatologiczne i kontrolne po urazie zęba (`BAD-PO-URAZIE`)

Krótko: **Po urazie** · kategoria: specjalistyczne · status: **draft**

**Cel.** Rodzaj i zakres urazu zębów i tkanek przyzębia, stan miazgi, tkanki miękkie.

- Informacje: okoliczności; klasyfikacja urazu; testy żywotności (wyjściowe); RTG; plan kontroli
- Wykrywa: złamania korony i korzenia; zwichnięcia; urazy tkanek miękkich; urazy wymagające pilnego leczenia (awulsja, obnażenie miazgi)

**Wskazania** (diagnostyczne, kontrolne): uraz zęba – badanie pierwsze; kontrole po urazie (świadczenie kontrolne). Szczególnie: awulsja – postępowanie natychmiastowe; dzieci – zęby mleczne i zawiązki zębów stałych

**Przebieg**

1. **Wywiad** – Kiedy, gdzie, jak; utrata przytomności, wymioty, ból głowy (wskazanie do pilnej konsultacji lekarskiej); szczepienie p/tężcowi.
2. **Badanie zewnątrz- i wewnątrzustne** – Rany, obrzęki, fragmenty zębów w tkankach, zgryz.
3. **Badanie zębów** – Złamania, ruchomość, przemieszczenie, opukiwanie (dźwięk metaliczny – wtłoczenie), testy żywotności (wyjściowe).
4. **RTG** – Zdjęcia wewnątrzustne (różne kąty) zależnie od urazu; RTG tkanek miękkich przy podejrzeniu fragmentów.
5. **Klasyfikacja i plan** – Rozpoznanie wg IADT, leczenie doraźne, plan kontroli (np. 4 tyg., 6–8 tyg., 4 mies., 6 mies., 1 rok – zależnie od urazu).

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| okoliczności | wywiad | `POLE-UR-OKOLICZNOSCI` |
| rodzaj urazu | klasyfikacja IADT | `POLE-UR-RODZAJ` |
| ruchomość | przemieszczenie | `POLE-UR-RUCH` |
| tkanki miękkie | rany | `POLE-UR-TKANKI` |

**Przykład wyniku prawidłowego:** Nie dotyczy – badanie po urazie; wyniki wpisuje lekarz.

**Przykłady nieprawidłowości:** złamanie korony z obnażeniem miazgi; wtłoczenie zęba; awulsja; złamanie korzenia na RTG; brak reakcji na testy (po urazie możliwy przejściowo)

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Okoliczności urazu, zęby objęte urazem (FDI), rodzaj urazu — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Testy żywotności i RTG wyjściowe; plan kontroli — *zalecenie kliniczne* (`SRC-KLIN-IADT-OG-2020` (PMID 32472740))

**Zależne od sytuacji**

- Szczepienie p/tężcowi – weryfikacja — *zalecenie kliniczne*, warunek: rana zanieczyszczona / awulsja (`SRC-KLIN-IADT-AWUL-2020` (PMID 32460393))
- Dokumentacja fotograficzna (na urządzeniu) — *zalecenie kliniczne* (`SRC-KLIN-IADT-OG-2020` (PMID 32472740))

**Powiązania** – ICD-9: 23.0107 (badanie i kontrola po urazie zęba (ST28)); 23.02 (testy żywotności); 23.2101 (repozycja i unieruchomienie zwichniętego zęba) · ICD-10: S02.5 (złamanie zęba – rozpoznanie lekarza); S03.2 (zwichnięcie zęba)

**Szablony opisu**

**standardowy**

> BADANIE PO URAZIE: okoliczności: {{POLE-UR-OKOLICZNOSCI}}. Zęby: {{POLE-ZEBY}}. Rodzaj urazu: {{POLE-UR-RODZAJ}}. Ruchomość / przemieszczenie: {{POLE-UR-RUCH}}. Tkanki miękkie: {{POLE-UR-TKANKI}}. Plan kontroli: {{POLE-UR-PLAN}}.

**skrocony**

> Uraz {{POLE-ZEBY}}: {{POLE-UR-RODZAJ}}; kontrola: {{POLE-UR-PLAN}}.

**rozszerzony**

> BADANIE PO URAZIE: okoliczności: {{POLE-UR-OKOLICZNOSCI}}. Zęby: {{POLE-ZEBY}}. Rodzaj urazu (IADT): {{POLE-UR-RODZAJ}}. Ruchomość / przemieszczenie: {{POLE-UR-RUCH}}. Tkanki miękkie: {{POLE-UR-TKANKI}}. Żywotność: {{POLE-ZY-ZIMNO}}. RTG: {{POLE-RTG}}. Tężec: {{POLE-UR-SZCZEPIENIE}}. Leczenie doraźne: {{POLE-PRZEBIEG}}. Plan kontroli: {{POLE-UR-PLAN}}. Zalecenia: {{POLE-ZALECENIA}}.

**Źródła:** `SRC-KLIN-IADT-OG-2020` (PMID 32472740); `SRC-KLIN-IADT-ZLAM-2020` (PMID 32475015); `SRC-KLIN-IADT-AWUL-2020` (PMID 32460393); `SRC-KLIN-IADT-MLECZ-2020` (PMID 32458553); `SRC-DU-2026-1391`

## Badanie stomatologiczne dziecka (`BAD-DZIECKO`)

Krótko: **Badanie dziecka** · kategoria: dziecko · status: **draft**

**Cel.** Uzębienie mleczne / mieszane, rozwój zgryzu, ryzyko próchnicy, nawyki, współpraca.

- Informacje: stan uzębienia (dmft/DMFT); rozwój i wyrzynanie; nawyki dietetyczne i higieniczne; ekspozycja na fluorki; współpraca
- Wykrywa: próchnicę wczesnego dzieciństwa; zaburzenia wyrzynania i rozwoju; szkodliwe nawyki; wady zgryzu do konsultacji ortodontycznej

**Wskazania** (rutynowe, kontrolne): pierwsza wizyta (najpóźniej po wyrznięciu pierwszego zęba / ok. 1. r.ż.); profilaktyczne świadczenia wg wieku (23.1009–23.1023); kontrole wg ryzyka próchnicy. Szczególnie: wysokie ryzyko próchnicy; dzieci z niepełnosprawnością

**Przebieg**

1. **Wywiad z opiekunem** – Dieta, karmienie nocne, higiena (kto szczotkuje), fluorki, nawyki, choroby, leki.
2. **Badanie** – U małych dzieci – pozycja „kolano do kolana”; uzębienie, błona śluzowa, wędzidełka, zgryz.
3. **Ocena ryzyka** – Ryzyko próchnicy (aktywne zmiany, dieta, higiena, fluorki).
4. **Instruktaż i profilaktyka** – Instruktaż opiekuna; ilość pasty i stężenie fluoru wg wieku (EAPD); lakier fluorkowy wg ryzyka.
5. **Plan** – Termin kontroli wg ryzyka; ewentualne skierowanie do ortodonty.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| uzębienie | dmft/DMFT | `POLE-UZ-DMFT` |
| rozwój | wyrzynanie | `POLE-DZ-ROZWOJ` |
| nawyki | dieta, ssanie | `POLE-DZ-NAWYKI` |
| fluorki | ekspozycja | `POLE-DZ-FLUOR` |
| współpraca | Frankl | `POLE-DZ-WSPOLPRACA` |

**Przykład wyniku prawidłowego:** Uzębienie mleczne pełne, bez próchnicy (dmft = 0), wyrzynanie zgodne z wiekiem; higiena prowadzona przez opiekuna, pasta z fluorem. Współpraca 4 (Frankl). (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** próchnica wczesnego dzieciństwa (powierzchnie wargowe siekaczy górnych); nocne karmienie butelką ze słodkim płynem; pasta bez fluoru; ssanie smoczka po 3. r.ż.; opóźnione wyrzynanie

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Informacje przekazane opiekunowi (instruktaż, zalecenia) — *prawne*, warunek: pacjent małoletni (`SRC-PRAWA-PACJENTA`)

**Zalecane**

- Ocena ryzyka próchnicy i zalecenia fluorkowe — *zalecenie kliniczne* (`SRC-KLIN-EAPD-F-2019` (PMID 31631242))

**Zależne od sytuacji**

- Skierowanie do ortodonty — *zalecenie kliniczne*, warunek: wada zgryzu / nawyki (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.06 (wizyta adaptacyjna małego dziecka); 23.1009 (profilaktyka – 6. miesiąc życia); 23.1011 (profilaktyka – 12. miesiąc); 23.1023 (profilaktyka – 3. rok życia (wariant NFZ 23.1012a – D5=B)); 23.0101 (badanie lekarskie) · ICD-10: Z01.2 (badanie stomatologiczne bez rozpoznania choroby); K02.1 (próchnica zębiny – rozpoznanie lekarza) · reguły NFZ: R-BAD-01

**Szablony opisu**

**standardowy**

> BADANIE DZIECKA ({{POLE-DZ-WIEK}} l.): uzębienie {{POLE-UZ-TYP}}, dmft/DMFT {{POLE-UZ-DMFT}}; rozwój: {{POLE-DZ-ROZWOJ}}. Nawyki: {{POLE-DZ-NAWYKI}}. Fluorki: {{POLE-DZ-FLUOR}}. Współpraca: {{POLE-DZ-WSPOLPRACA}}.

**skrocony**

> Dziecko {{POLE-DZ-WIEK}} l.: dmft {{POLE-UZ-DMFT}}, ryzyko próchnicy {{POLE-UZ-RYZYKO}}; zalecenia przekazano opiekunowi: {{POLE-DZ-OPIEKUN}}.

**rozszerzony**

> BADANIE DZIECKA ({{POLE-DZ-WIEK}} l.): uzębienie {{POLE-UZ-TYP}}: {{POLE-UZ-DIAGRAM}}; dmft/DMFT {{POLE-UZ-DMFT}}. Rozwój: {{POLE-DZ-ROZWOJ}}. Zgryz: {{POLE-ZG-WADY}}. Nawyki: {{POLE-DZ-NAWYKI}}. Fluorki: {{POLE-DZ-FLUOR}}. Ryzyko próchnicy: {{POLE-UZ-RYZYKO}}. Współpraca: {{POLE-DZ-WSPOLPRACA}}. Zalecenia: {{POLE-ZALECENIA}} – przekazano opiekunowi: {{POLE-DZ-OPIEKUN}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła:** `SRC-KLIN-EAPD-F-2019` (PMID 31631242); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAWA-PACJENTA`; `SRC-DU-2026-1391`

## Badanie lekarskie stomatologiczne z instruktażem higieny jamy ustnej (23.0101) (`BAD-STOMATOLOGICZNE`)

Krótko: **Badanie stomatologiczne** · kategoria: kontrolne · status: **draft**

**Cel.** Pełna ocena stanu jamy ustnej: wywiad, badanie zewnątrz- i wewnątrzustne, uzębienie, przyzębie, higiena, zgryz; plan leczenia; instruktaż higieny.

- Informacje: wyniki badań składowych; plan leczenia; instruktaż higieny
- Wykrywa: wszystkie odchylenia wykrywane w badaniach składowych

**Wskazania** (rutynowe): pierwsza wizyta pacjenta; raz w roku kalendarzowym (NFZ). Szczególnie: planowanie kompleksowego leczenia

**Przebieg**

1. **Wywiad** – Badanie BAD-WYWIAD.
2. **Badanie zewnątrzustne** – BAD-ZEWNATRZUSTNE.
3. **Badanie wewnątrzustne** – BAD-WEWNATRZUSTNE (przy zmianie – BAD-BLONA).
4. **Uzębienie, przyzębie, higiena, zgryz** – BAD-UZEBIENIE, BAD-PRZYZEBIE (przesiewowo), BAD-HIGIENA, BAD-ZGRYZ.
5. **Instruktaż higieny** – Instruktaż higieny jamy ustnej – składnik świadczenia 23.0101.
6. **Plan leczenia** – Omówienie wyników i planu z pacjentem; termin kolejnej wizyty.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| badania składowe | wyniki z formularzy badań składowych | — |

**Przykład wyniku prawidłowego:** Zestawienie wyników badań składowych – bez odchyleń (tylko jeśli lekarz tak ocenił każde z nich).

**Przykłady nieprawidłowości:** dowolne odchylenia z badań składowych

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Instruktaż higieny jamy ustnej przeprowadzony — *NFZ*, warunek: rozliczenie 23.0101 / ST33 (`SRC-DU-2025-615`)

**Zalecane**

- Plan leczenia przekazany pacjentowi — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- —

**Powiązania** – ICD-9: 23.0101 (świadczenie badania lekarskiego (ST33)) · ICD-10: Z01.2 (badanie bez rozpoznania choroby) · reguły NFZ: R-BAD-01

*Przy rozpoznaniu choroby – kod choroby zamiast Z01.2 (podpowiedź audytu).*

**Szablony opisu**

**standardowy**

> BADANIE LEKARSKIE STOMATOLOGICZNE. {{POLE-PRZEBIEG}} Instruktaż higieny jamy ustnej: {{POLE-HG-INSTRUKTAZ}}. Plan leczenia: {{POLE-DECYZJA}}.

**skrocony**

> Badanie stomatologiczne: {{POLE-PRZEBIEG}} Instruktaż: {{POLE-HG-INSTRUKTAZ}}.

**rozszerzony**

> BADANIE LEKARSKIE STOMATOLOGICZNE. {{POLE-PRZEBIEG}} RTG: {{POLE-RTG}}. Instruktaż higieny: {{POLE-HG-INSTRUKTAZ}} – {{POLE-HG-INSTR-OPIS}}. Plan leczenia: {{POLE-DECYZJA}}. Zalecenia: {{POLE-ZALECENIA}}. Kolejna wizyta: {{POLE-KONTROLA}}.

**Źródła:** `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`; `SRC-DU-2026-1391`

*Uwagi: Badanie złożone – nie powiela pól; opis składa się z szablonów badań składowych.*

## Badanie lekarskie kontrolne (23.0102) (`BAD-KONTROLNE`)

Krótko: **Badanie kontrolne** · kategoria: kontrolne · status: **draft**

**Cel.** Zmiany od ostatniego badania, efekty leczenia, nowe ogniska chorobowe.

- Informacje: aktualizacja wywiadu; nowe zmiany; ocena wcześniejszego leczenia
- Wykrywa: nowe ogniska próchnicy; niepowodzenia leczenia; progresję chorób przyzębia

**Wskazania** (kontrolne): kontrola w trakcie / po leczeniu; odstęp zależny od ryzyka (NFZ: limit 3× w roku, ciąża – 1× na kwartał). Szczególnie: wysokie ryzyko próchnicy / chorób przyzębia

**Przebieg**

1. **Aktualizacja wywiadu** – Nowe dolegliwości, choroby, leki, ciąża.
2. **Badanie ukierunkowane** – Uzębienie, przyzębie, błona śluzowa – z porównaniem do poprzedniego badania.
3. **Ocena i plan** – Ocena leczenia, dalszy plan, termin kolejnej kontroli.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| zmiany od ostatniej wizyty | wywiad | `POLE-KO-ZMIANY` |
| ocena | stan jamy ustnej | `POLE-KO-OCENA` |

**Przykład wyniku prawidłowego:** Bez nowych dolegliwości; bez nowych ognisk próchnicy; wypełnienia szczelne. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** nowe ognisko próchnicy; nieszczelne wypełnienie; nasilenie krwawienia dziąseł

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Porównanie z poprzednim badaniem — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**Zależne od sytuacji**

- —

**Powiązania** – ICD-9: 23.0102 (badanie lekarskie kontrolne (ST34)) · ICD-10: Z01.2 (bez rozpoznania choroby) · reguły NFZ: R-BAD-02

**Szablony opisu**

**standardowy**

> BADANIE KONTROLNE: Zmiany od ostatniej wizyty: {{POLE-KO-ZMIANY}}. Ocena: {{POLE-KO-OCENA}}. Plan: {{POLE-DECYZJA}}.

**skrocony**

> Kontrola: {{POLE-KO-OCENA}}.

**rozszerzony**

> BADANIE KONTROLNE: Zmiany od ostatniej wizyty: {{POLE-KO-ZMIANY}}. Uzębienie: {{POLE-UZ-DIAGRAM}}. Przyzębie: {{POLE-PZ-ROZPOZNANIE}}. Higiena: {{POLE-HG-OCENA}}. Ocena: {{POLE-KO-OCENA}}. Plan: {{POLE-DECYZJA}}. Kolejna kontrola: {{POLE-KONTROLA}}.

**Źródła:** `SRC-DU-2025-615`; `SRC-DU-2026-1391`

## Kwalifikacja do leczenia (badanie przed zabiegiem) (`BAD-PRZED-LECZENIEM`)

Krótko: **Przed leczeniem** · kategoria: kwalifikacja · status: **draft**

**Cel.** Wskazania, przeciwwskazania i ryzyko planowanego leczenia; świadoma zgoda.

- Informacje: aktualny wywiad; wyniki badań dodatkowych; omówione alternatywy i ryzyka; zgoda
- Wykrywa: przeciwwskazania lub potrzebę modyfikacji leczenia; potrzebę konsultacji lekarskiej

**Wskazania** (diagnostyczne): przed zabiegiem chirurgicznym, endodontycznym, protetycznym; przed leczeniem w znieczuleniu. Szczególnie: pacjenci z chorobami ogólnymi i lekami modyfikującymi krzepnięcie

**Przebieg**

1. **Aktualizacja wywiadu** – Leki (w tym przeciwkrzepliwe – data ostatniej dawki, INR jeśli dotyczy), choroby, alergie, ciąża.
2. **Ocena miejscowa** – Badanie okolicy zabiegu, RTG.
3. **Decyzja i informacja** – Przedstaw rozpoznanie, proponowane leczenie, alternatywy, ryzyka i rokowanie.
4. **Zgoda** – Uzyskaj zgodę (pisemną przy zabiegach o podwyższonym ryzyku).

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| zabieg | plan | `POLE-PL-ZABIEG` |
| czynniki ryzyka | wywiad | `POLE-PL-RYZYKA` |
| badania dodatkowe | wyniki | `POLE-PL-BADANIA` |
| zgoda | odnotowanie | `POLE-ZGODA` |

**Przykład wyniku prawidłowego:** Brak przeciwwskazań do planowanego zabiegu wg wywiadu i badania; pacjent poinformowany, wyraził zgodę. (Wpisuje lekarz.)

**Przykłady nieprawidłowości:** INR powyżej zakresu bezpiecznego dla zabiegu – odroczenie / konsultacja; leczenie antyresorpcyjne – ryzyko martwicy kości szczęk; niekontrolowane nadciśnienie

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)
- Zgoda pacjenta na zabieg (pisemna przy zabiegu o podwyższonym ryzyku) — *prawne*, warunek: zabiegi chirurgiczne i o podwyższonym ryzyku (`SRC-PRAWA-PACJENTA`)

**Zalecane**

- Omówione alternatywy i ryzyka — *zalecenie kliniczne* (`SRC-PRAWA-PACJENTA`)

**Zależne od sytuacji**

- Konsultacja z lekarzem prowadzącym — *zalecenie kliniczne*, warunek: choroby ogólne wymagające modyfikacji leczenia (`SRC-PRAKTYKA`)

**Powiązania** – ICD-9: 23.0103 (porada lekarska – jeśli dotyczy) · ICD-10: —

*Kwalifikacja jest częścią leczenia; nie jest osobnym świadczeniem rozliczanym.*

**Szablony opisu**

**standardowy**

> KWALIFIKACJA: planowany zabieg: {{POLE-PL-ZABIEG}}. Czynniki ryzyka: {{POLE-PL-RYZYKA}}. Omówiono alternatywy i ryzyka: {{POLE-PL-ALTERNATYWY}}. Zgoda pacjenta: {{POLE-ZGODA}}.

**skrocony**

> Kwalifikacja do {{POLE-PL-ZABIEG}}: ryzyka {{POLE-PL-RYZYKA}}; zgoda {{POLE-ZGODA}}.

**rozszerzony**

> KWALIFIKACJA DO LECZENIA: planowany zabieg: {{POLE-PL-ZABIEG}}. Wskazanie: {{POLE-WSKAZANIE}}. Czynniki ryzyka: {{POLE-PL-RYZYKA}}. Badania dodatkowe: {{POLE-PL-BADANIA}}. Alternatywy i ryzyka: {{POLE-PL-ALTERNATYWY}}. Zgoda pacjenta: {{POLE-ZGODA}}. Decyzja: {{POLE-DECYZJA}}.

**Źródła:** `SRC-PRAWA-PACJENTA`; `SRC-PRAKTYKA`; `SRC-DU-2026-1391`

## Badanie po zakończonym leczeniu (ocena wyniku) (`BAD-PO-LECZENIU`)

Krótko: **Po leczeniu** · kategoria: kontrolne · status: **draft**

**Cel.** Wynik zakończonego leczenia: objawy, funkcja, gojenie, obraz RTG.

- Informacje: rodzaj leczenia; ocena kliniczna i RTG; wynik
- Wykrywa: niepowodzenia (np. zmiana okołowierzchołkowa po leczeniu kanałowym); powikłania gojenia; nieszczelność odbudowy

**Wskazania** (kontrolne): kontrola po leczeniu kanałowym (ESE: co najmniej po roku, dalej do 4 lat przy niepełnym gojeniu); kontrola po ekstrakcji / zabiegu chirurgicznym; kontrola po leczeniu periodontologicznym

**Przebieg**

1. **Wywiad** – Dolegliwości od zakończenia leczenia.
2. **Badanie kliniczne** – Opukiwanie, palpacja, przetoki, szczelność odbudowy, kieszonki.
3. **RTG (wg wskazań)** – Porównanie z RTG końcowym.
4. **Ocena** – Powodzenie / niepewny / niepowodzenie; plan.

**Elementy oceny**

| Element | Co oceniamy | Pole |
|---|---|---|
| leczenie | rodzaj, zęby | `POLE-PO-LECZENIE` |
| ocena | klinicznie / RTG | `POLE-PO-OCENA` |
| wynik | kategoria | `POLE-PO-WYNIK` |

**Przykład wyniku prawidłowego:** Ząb 46 rok po leczeniu kanałowym: bez dolegliwości, opukiwanie niebolesne, na RTG prawidłowa szpara ozębnej – powodzenie leczenia. (Przykład – wpisuje lekarz.)

**Przykłady nieprawidłowości:** nowa lub powiększona zmiana okołowierzchołkowa; przetoka; nieszczelna odbudowa

**Dokumentacja – niezbędne**

- Data i oznaczenie lekarza — *prawne* (`SRC-DU-2026-1391`)
- Opis wykonanego badania i stwierdzonych odchyleń (lub informacja lekarza o braku odchyleń w badanych strukturach) — *prawne* (`SRC-DU-2026-1391`)

**Zalecane**

- Kryteria oceny wyniku (kliniczne i RTG) — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))

**Zależne od sytuacji**

- Plan przy niepowodzeniu — *zalecenie kliniczne*, warunek: niepowodzenie leczenia (`SRC-KLIN-ESE-S3-2023` (PMID 37772327))

**Powiązania** – ICD-9: 23.0102 (w ramach badania kontrolnego) · ICD-10: K04.5 (przewlekłe zapalenie okołowierzchołkowe – przy niepowodzeniu, rozpoznanie lekarza)

**Szablony opisu**

**standardowy**

> KONTROLA PO LECZENIU: {{POLE-PO-LECZENIE}}. Ocena: {{POLE-PO-OCENA}}. Wynik: {{POLE-PO-WYNIK}}.

**skrocony**

> Po leczeniu {{POLE-PO-LECZENIE}}: {{POLE-PO-WYNIK}}.

**rozszerzony**

> KONTROLA PO LECZENIU: {{POLE-PO-LECZENIE}}. Dolegliwości: {{POLE-KO-ZMIANY}}. Ocena kliniczna i RTG: {{POLE-PO-OCENA}}. RTG: {{POLE-RTG}}. Wynik: {{POLE-PO-WYNIK}}. Plan: {{POLE-DECYZJA}}.

**Źródła:** `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-ESE-S3-2023` (PMID 37772327); `SRC-DU-2026-1391`
