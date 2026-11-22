# Reguły rozliczeń i kontroli – baza reguł

> Stan prawny na **21.11.2026**. Dokument generowany z `data/nfz/*.json` (`scripts` w paczce audytu) – nie edytuj ręcznie, popraw dane i wygeneruj ponownie.


## Poziomy kontroli

| Poziom | Znaczenie | Warunek |
|---|---|---|
| **BLOKADA** | blokuje wyłącznie eksport / rozliczenie; zapis kliniczny zawsze możliwy | tylko reguła POTWIERDZONA |
| **OSTRZEŻENIE** | komunikat + możliwość kontynuacji z zapisem świadomej decyzji | reguła POTWIERDZONA lub CZĘŚCIOWO |
| **INFORMACJA** | podpowiedź | każda, obowiązkowo dla WYMAGA WERYFIKACJI |

## Trzy niezależne warstwy kontroli

- **medyczna** – czy świadczenie ma sens kliniczny (nigdy nie blokuje lekarza),
- **dokumentacyjna** – czy dokumentacja zawiera wymagane elementy (opis RTG, czas, oświadczenia),
- **rozliczeniowa** – limity, łączenie, współczynniki, kody.

## Reguły

| ID | Obszar | Warstwa | Wyzwalacz | Treść | Poziom | Status | Od | Źródła |
|---|---|---|---|---|---|---|---|---|
| `R-BAD-01` | badanie | rozliczeniowa | dodanie 23.0101 / ST33 / ST33A | Badanie lekarskie stomatologiczne – 1 raz w roku kalendarzowym. | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| `R-BAD-02` | badanie | rozliczeniowa | dodanie 23.0102 / ST34 / ST34A | Badanie kontrolne – 3 razy w roku kalendarzowym; ciąża/połóg – nie częściej niż 1 raz na kwartał. _Uwaga: Brzmienie dla ciąży („nie częściej niż 1×/kwartał”) – zinterpretować łącznie z limitem rocznym; dlatego OSTRZEŻENIE._ | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-KONS-01` | konsultacja | rozliczeniowa | 23.0105 + inne świadczenie tego dnia | Konsultacja specjalistyczna bez połączenia z innymi świadczeniami gwarantowanymi. | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ZYW-01` | diagnostyka | dokumentacyjna | dodanie 23.02 | Badanie żywotności obejmuje ząb + 3 zęby sąsiednie lub przeciwstawne – dokumentować wyniki. | **INFORMACJA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-RTG-01` | RTG | rozliczeniowa | dodanie 23.0301 (wszyscy) | Do 2 zdjęć wewnątrzustnych w roku kalendarzowym, w połączeniu z innymi świadczeniami, z opisem w dokumentacji. _Uwaga: Limit dla dzieci różny (23.0302 – do 5 zdjęć) – sprawdzić, który limit dotyczy danego zakresu._ | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-RTG-02` | RTG | dokumentacyjna | RTG bez opisu | Opis zdjęcia musi być wpisany do dokumentacji medycznej. | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-RTG-03` | RTG | rozliczeniowa | 23.0304 u dziecka | Pantomogram: dorośli – na potrzeby leczenia endodontycznego oraz (wszyscy) przed protetyką, 1 raz na 5 lat; dzieci 5–18 lat – w uzasadnionych medycznie przypadkach, 1 raz na 3 lata; zawsze w połączeniu z innymi świadczeniami, z opisem w dokumentacji. | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ZNI-01` | znieczulenie | rozliczeniowa | znieczulenie jako jedyne świadczenie wizyty | Znieczulenie (23.0401/0402/0403) – tylko w połączeniu z innymi świadczeniami. | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ZNI-02` | znieczulenie | rozliczeniowa | znieczulenie przy ekstrakcji (ST01) lub kiretażu (ST04) | Znieczulenie jest wliczone w pakiet ST01/ST04 (lista ST1 = składnik pakietu). Nie rozlicza się go jako osobnego produktu jednostkowego (5.13.00.2304010/020/030). Kod ICD-9 znieczulenia podaje się tylko jako element pakietu. _Uwaga: Rozporządzenie (koszyk) pisze przy 23.1607 i 23.2001 „nie obejmuje odpowiedniego znieczulenia” – to dotyczy definicji świadczenia gwarantowanego, a NIE rozliczenia: w zarządzeniu NFZ znieczulenie jest w wycenie pakietu. Potwierdzone praktyką rozliczeniową lekarza (Patryk, 21.11.2026). Czy ST1 jest w pakiecie obowiązkowy czy opcjonalny – sprawdzić w zał. 1d._ | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-DU-2025-615` |
| `R-ST1-ZO` | znieczulenie | rozliczeniowa | lista ST1 w zakresie 07.0000.219.02 | Lista ST1 (znieczulenia miejscowe) nie ma zastosowania w znieczuleniu ogólnym. | **OSTRZEŻENIE** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-ZLOG-01` | złogi | rozliczeniowa | 23.1601 / ST30–ST30C | Usunięcie złogów (½ łuku) – 1 raz w roku kalendarzowym w obrębie całego uzębienia (zał. 1 i 2). | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ZLOG-02` | złogi | rozliczeniowa | 23.1602 u dziecka (zał. 2) | Usunięcie złogów ze wszystkich zębów – nie częściej niż 1 raz na 6 miesięcy (zał. 2). | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ST30-TWARDE` | złogi | medyczna+rozliczeniowa | ST30/ST30A/ST30B/ST30C | Pakiety ST30–ST30C dotyczą wyłącznie złogów twardych (23.16012 / 23.16022). Złogi miękkie u dorosłych nie są osobno rozliczanym świadczeniem. _Uwaga: Spór środowiska (LIL, NRL, Lewiatan) – stan przepisów jednoznaczny od 01.09.2026, interpretacja historyczna (przed 01.09.2026) SPORNA._ | **OSTRZEŻENIE** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-NFZ-KOM-8924` |
| `R-ST30-LAKIER` | złogi | rozliczeniowa | ST30–ST30C + 23.1006 tego dnia | Pakiety ST30, ST30A, ST30B, ST30C nie sumują się z 23.1006 (lakierowanie) – wycena pakietu obejmuje lakierowanie. _Uwaga: Przed 01.09.2026: korekty wsteczne NFZ na podstawie komunikatów 1292084/819330 – SPORNE (interpelacja 16442). Aplikacja nie ocenia przeszłych rozliczeń._ | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-NFZ-KOM-8924` |
| `R-ST30-WZAJEM` | złogi | rozliczeniowa | dwa pakiety z grupy ST30–ST30G tego dnia | Pakiety ST30–ST30G wzajemnie się wykluczają (wg listy „nie sumuje się” w zał. 1d); ST30D może być z ST30E i 23.1101; ST30F tylko z 23.1101. | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-ST30-CZAS` | złogi | dokumentacyjna | zapis pakietu ST30–ST30G | Minimalny czas: ST30 10, ST30A 40, ST30B 10, ST30C 10, ST30D 15, ST30E 5, ST30F 30, ST30G 20 minut – czas trzeba móc wykazać w dokumentacji. _Uwaga: Sposób dokumentowania czasu (godzina rozpoczęcia/zakończenia?) – WYMAGA WERYFIKACJI._ | **OSTRZEŻENIE** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-ST30DG-WIEK` | higienizacja | rozliczeniowa | ST30D/E/F/G u pacjenta ≥ 18 lat | Pakiety ST30D–ST30G – profesjonalna higienizacja wyłącznie u dzieci i młodzieży do 18. r.ż. _Uwaga: RYZYKO W APLIKACJI: obecne etykiety ST30E/ST30G nie pokazują ograniczenia wieku._ | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-ZARZ-95-2026` |
| `R-ST30E-LIMIT` | higienizacja | rozliczeniowa | kolejny ST30E w roku | ST30E – maks. 4× w roku; 3×, jeśli w roku wykonano ST30D. | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-ST30DFG-LIMIT` | higienizacja | rozliczeniowa | kolejny ST30D/ST30F/ST30G w roku | ST30D, ST30F, ST30G – 1× w roku. _Uwaga: „rok” – kalendarzowy czy 12 miesięcy? WYMAGA WERYFIKACJI; do czasu wyjaśnienia liczyć kalendarzowo i oznaczać OSTRZEŻENIE dla granicznych przypadków._ | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-ST30BC-WYK` | higienizacja | rozliczeniowa | ST30B/ST30C, ST33A/ST34A | ST30B (i ST30C wg przypisu) wykonuje periodontolog; ST33A/ST34A – specjaliści w zakresach periodontologia / chirurgia i periodontologia. | **OSTRZEŻENIE** | CZĘŚCIOWO POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-LAKIER-01` | profilaktyka | rozliczeniowa | 23.1006 u dziecka | Lakierowanie 23.1006 – tylko dzieci i młodzież do 18. r.ż.; zęby mleczne i stałe; nie częściej niż 1× na kwartał za każdą ¼ łuku. | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-LAKOW-01` | profilaktyka | rozliczeniowa | 23.1003 | Lakowanie bruzd: pierwsze trzonowce stałe – 1 raz do ukończenia 8. r.ż.; drugie trzonowce stałe – 1 raz do ukończenia 14. r.ż. _Uwaga: BLOKADA tylko gdy na tym koncie jest już zapis lakowania tego zęba; inaczej INFORMACJA._ | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ADAPT-01` | wizyta adaptacyjna | rozliczeniowa | 23.06 + inne świadczenie | Wizyta adaptacyjna – bez połączenia z innymi świadczeniami; pierwsza wizyta dziecka do ukończenia 6. r.ż. | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ENDO-DZ` | endodoncja | dokumentacyjna | endodoncja u dziecka | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. | **INFORMACJA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-1204-DOK` | endodoncja | dokumentacyjna | 23.1204 | Świadczenie „w udokumentowanych przypadkach” – wymagany opis uzasadnienia. | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-PROT-01` | protetyka | rozliczeniowa | protezy całkowite 23.3104/23.3105 | 1 raz na 5 lat (nie dotyczy pacjentów po leczeniu onkologicznym). _Uwaga: Aplikacja nie zna protez z innych gabinetów – BLOKADA tylko na podstawie danych z własnego konta, w pozostałych przypadkach INFORMACJA._ | **BLOKADA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-PROT-02` | protetyka | rozliczeniowa | naprawa z wyciskiem 23.3112; podścielenie 23.3116/23.3117 | Naprawa z wyciskiem – 1×/2 lata; podścielenie – 1×/2 lata. | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-PROT-03` | protetyka | dokumentacyjna | dowolna proteza NFZ | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). | **OSTRZEŻENIE** | POTWIERDZONA | 2023-04-06 | `SRC-ZARZ-60-2023-TJ` |
| `R-PROT-04` | protetyka | rozliczeniowa | 23.3104a/23.3105a | Proteza overdenture – warunki z zał. 6 rozporządzenia NIE ZOSTAŁY PRZECZYTANE. | **INFORMACJA** | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| `R-WSP-15` | współczynniki | rozliczeniowa | pacjent < 18 w zakresie 218/221/dentobus/szkoła | Współczynnik 1,5 – poza wizytą adaptacyjną, pantomogramem, profilaktyką i ST30D–G. | **INFORMACJA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ` |
| `R-WSP-12` | współczynniki | rozliczeniowa | ciąża/połóg, zakres 218 | Współczynnik 1,2 (kod WKC); ciąża potwierdzona kartą przebiegu ciąży (§ 5 rozporządzenia). | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-ZARZ-60-2023-TJ`, `SRC-DU-2025-615`, `SRC-NFZ-KOM-8386` |
| `R-WSP-08` | współczynniki | rozliczeniowa | ≥ 2 pakiety na wizycie | Najwyżej wyceniony pakiet 1,0, kolejne 0,8 (kod WKR); nie stosuje się do ST30E i ST30G. | **INFORMACJA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-NFZ-WEBINAR`, `SRC-NFZ-KOM-8386` |
| `R-ZO-01` | znieczulenie ogólne | medyczna | zakres 07.0000.219.02 u dziecka | Kryteria § 4 ust. 1a (od 1.01.2026): alergia; choroby ogólne z opinią specjalisty; < 3 lat, brak współpracy i ≥ 8 ognisk próchnicy lub ≥ 4 zęby do leczenia; < 18, brak współpracy i ≥ 4 zęby lub zabieg chirurgiczny; ostry stan zapalny. Dodatkowo § 4 ust. 1 i 2 (niepełnosprawność). _Uwaga: Szczegółowe brzmienie każdego punktu – w pełnym tekście; aplikacja tylko przypomina o udokumentowaniu kryterium._ | **OSTRZEŻENIE** | POTWIERDZONA | 2026-01-01 | `SRC-DU-2025-615-P4-1A` |
| `R-BOL-01` | organizacja | dokumentacyjna | wizyta bólowa | Pacjent z bólem – udzielenie świadczenia w dniu zgłoszenia (§ 6). | **INFORMACJA** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-DOK-01` | dokumentacja | dokumentacyjna | eksport/rozliczenie | Świadczenia przedstawiane do rozliczenia muszą być zgodne z indywidualną dokumentacją medyczną. _Uwaga: BLOKADA = aplikacja nie pozwala wyeksportować świadczenia bez zapisanego opisu wizyty z tą samą datą._ | **BLOKADA** | POTWIERDZONA | 2023-04-06 | `SRC-ZARZ-60-2023-TJ`, `SRC-WYR-SO-SIEDLCE-IIKa168-24` |
| `R-DOK-02` | dokumentacja | dokumentacyjna | świadczenie na zębie | Lokalizacja zęba wg PN-EN ISO 3950; ząb dodatkowy – „ZD”. _Uwaga: Uwaga: numer zęba to dana pacjenta? W SaaS – tylko na urządzeniu (zasada „zero danych pacjentów w chmurze”)._ | **OSTRZEŻENIE** | CZĘŚCIOWO POTWIERDZONA | NIE DOTYCZY | `SRC-NFZ-KOM-6113` |
| `R-DOK-03` | dokumentacja | rozliczeniowa | pakiet na zębie | Jeden pakiet = jeden ząb / jedna lokalizacja (½ łuku przy złogach – także przy niepełnym łuku). | **INFORMACJA** | CZĘŚCIOWO POTWIERDZONA | NIE DOTYCZY | `SRC-NFZ-WEBINAR` |
| `R-DOK-04` | dokumentacja | dokumentacyjna | zmiana daty / dopisanie świadczenia po fakcie | Aplikacja nie podpowiada dopisywania czynności ani zmiany daty wstecz; każda zmiana po zapisaniu jest jawnie oznaczona (kto, kiedy). _Uwaga: Zasada projektowa wynikająca z wymogów audytu i orzecznictwa._ | **BLOKADA** | POTWIERDZONA | NIE DOTYCZY | `SRC-WYR-SO-SIEDLCE-IIKa168-24` |
| `R-DOK-05` | dokumentacja | rozliczeniowa | kod ICD-9 spoza słownika | Kod ICD-9 nieobecny w ICD-9 PL 5.91 (np. 23.1513) nie może trafić do rozliczenia. | **BLOKADA** | POTWIERDZONA | NIE DOTYCZY | `SRC-ICD9-PL-591` |
| `R-KOD-01` | kody | rozliczeniowa | 23.1601 / 23.1602 bez podkodu (data ≥ 2026-09-01) | Od 01.09.2026 wykazuje się podkody: 23.16011/23.16012 (½ łuku miękkie/twarde), 23.16021/23.16022 (wszystkie zęby). | **BLOKADA** | POTWIERDZONA | 2026-09-01 | `SRC-ZARZ-60-2023-TJ`, `SRC-ZARZ-95-2026`, `SRC-NFZ-KOM-9017`, `SRC-ICD9-PL-591` |
| `R-KOD-02` | kody | rozliczeniowa | 23.1012a / 23.3104a / 23.3105a | Kody NFZ z literą „a” nie występują w ICD-9 PL 5.91 (odpowiedniki: 23.1023, 23.31041, 23.31051). Sposób wykazania w SWIAD do potwierdzenia. | **INFORMACJA** | WYMAGA WERYFIKACJI | NIE DOTYCZY | `SRC-ZARZ-60-2023-TJ`, `SRC-ICD9-PL-591` |
| `R-AMALG-01` | materiały | rozliczeniowa | usunięcie wypełnienia amalgamatowego | Tylko przy 23.1108, 23.1502–23.1505; stanowisko z separatorem amalgamatu (zał. 10c). _Uwaga: Kod ICD-9 / produkt NFZ dla tego świadczenia – WYMAGA WERYFIKACJI._ | **OSTRZEŻENIE** | POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615` |
| `R-ICD10-01` | rozpoznania | rozliczeniowa | świadczenie bez ICD-10 | Sprawozdanie wymaga ICD-10; brak obowiązkowych par ICD-9↔ICD-10 – podpowiedź, nie blokada. | **INFORMACJA** | CZĘŚCIOWO POTWIERDZONA | NIE DOTYCZY | `SRC-NFZ-KOM-8386` |
| `R-KIR-DZ` | periodontologia | rozliczeniowa | ST04 / 23.1607 u dziecka < 15 r.ż. | Komunikat Prezesa NFZ nr 627276 (22.07.2026): od świadczeń z 1.01.2026 odrzucenie w weryfikacji; wyjątek – wniosek do OW NFZ. NRL (31.07.2026) kwestionuje. Stan sporny (aktualizacja 22.11.2026 wg Gazety Lekarskiej 9/2026). | **INFORMACJA** | WYMAGA WERYFIKACJI | 2026-01-01 | `SRC-NFZ-KOM-KIRETAZ-DZ`, `SRC-GL-2026-09-KIRETAZ`, `SRC-DU-2025-615` |
| `R-UPR-01` | uprawnienia | rozliczeniowa | każda wizyta NFZ | Potwierdzenie prawa do świadczeń (eWUŚ / art. 50 ustawy) – dokument potwierdzający w razie braku potwierdzenia elektronicznego. | **INFORMACJA** | CZĘŚCIOWO POTWIERDZONA | NIE DOTYCZY | `SRC-USTAWA-SWIADCZENIA`, `SRC-ZARZ-60-2023-TJ` |
| `R-MTA-01` | endodoncja | rozliczeniowa | 23.13141–23.13149 | Wskazania i ograniczenia MTA – nie przeniesione z zarządzenia. | **INFORMACJA** | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | `SRC-ZARZ-60-2023-TJ` |
| `R-PROF-01` | profilaktyka | rozliczeniowa | 23.1009–23.1021, 23.1012a | Profilaktyczne świadczenia wiekowe (zał. 10/10b); 23.1012a – 3. rok życia; 23.1021 – tylko zakres 218 (19. r.ż.). Warunki wieku dla każdego kodu – patrz warunki_tekst. | **OSTRZEŻENIE** | CZĘŚCIOWO POTWIERDZONA | 2025-05-13 | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |

## Macierz łączenia

Para spoza listy = WYMAGA DODATKOWEJ WERYFIKACJI (nie DOZWOLONE). Brak znalezionego zakazu nie oznacza zgody.

| A | B | Status | Reguła | Uwagi |
|---|---|---|---|---|
| ST30 | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30 | ST30A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30B | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30C | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30D | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30 | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30A | ST30 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30B | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30C | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30D | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30A | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30B | ST30 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30C | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30D | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30B | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30C | ST30 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30B | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30D | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30C | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30E | ST30 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST30A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST30B | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST30C | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST33 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST33A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST34 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30E | ST34A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | 23.1006 | **NIEDOZWOLONE** | `R-ST30-LAKIER` |  |
| ST30G | ST30 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30B | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30C | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30D | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST30F | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST33 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST33A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST34 | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30G | ST34A | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST30D | ST30E | **WARUNKOWO DOZWOLONE** | `R-ST30E-LIMIT` | ST30E maks. 3× w roku z ST30D |
| ST30D | 23.1101 | **DOZWOLONE** | `R-ST30-WZAJEM` | wprost dopuszczone w zał. 1d |
| ST30F | 23.1101 | **DOZWOLONE** | `R-ST30-WZAJEM` | wprost dopuszczone w zał. 1d |
| ST30D | 23.1006 | **DOZWOLONE** | `R-ST30-WZAJEM` | 23.1006 jest składnikiem (lista ST5) pakietu ST30D – nie rozliczać osobno |
| ST30 | ST1 | **WARUNKOWO DOZWOLONE** | `R-ST30-WZAJEM` | ST1 opcjonalnie w składzie pakietu ST30 |
| ST30 | 23.02 | **WARUNKOWO DOZWOLONE** | `R-ST30-WZAJEM` | lista ST4 – składnik opcjonalny |
| 23.0401 | (brak innego świadczenia) | **NIEDOZWOLONE** | `R-ZNI-01` |  |
| 23.0402 | (brak innego świadczenia) | **NIEDOZWOLONE** | `R-ZNI-01` |  |
| 23.0403 | (brak innego świadczenia) | **NIEDOZWOLONE** | `R-ZNI-01` |  |
| 23.0105 | (dowolne inne świadczenie) | **NIEDOZWOLONE** | `R-KONS-01` |  |
| 23.06 | (dowolne inne świadczenie) | **NIEDOZWOLONE** | `R-ADAPT-01` |  |
| ST04 | produkt jednostkowy znieczulenia (23.0401/0402/0403) | **NIEDOZWOLONE** | `R-ZNI-02` | znieczulenie wliczone w pakiet ST04 – tylko jako składnik, bez osobnych punktów |
| ST01 | produkt jednostkowy znieczulenia (23.0401/0402/0403) | **NIEDOZWOLONE** | `R-ZNI-02` | znieczulenie wliczone w pakiet ST01 – tylko jako składnik, bez osobnych punktów |
| ST01 | ST1 | **DOZWOLONE** | `R-ZNI-02` | ST1 wymagane w ST01 |
| ST04 | ST1 | **DOZWOLONE** | `R-ZNI-02` | ST1 wymagane w ST04 |
| ST04 | (pacjent < 18) | **WYMAGA DODATKOWEJ WERYFIKACJI** | `R-KIR-DZ` |  |
| ST33 | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST34 | ST30E | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST33 | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST34 | ST30G | **NIEDOZWOLONE** | `R-ST30-WZAJEM` |  |
| ST33 | ST34 | **WYMAGA DODATKOWEJ WERYFIKACJI** | `R-BAD-02` | badanie i kontrola tego samego dnia – brak wyraźnej reguły w przeczytanych źródłach |
| ST30D | ST33 | **WYMAGA DODATKOWEJ WERYFIKACJI** | `R-ST30-WZAJEM` | ST30D zawiera 23.0101; pytanie z komunikatu 9017 – odpowiedź do przeniesienia |

## Współczynniki

| ID | Wartość | Dotyczy | Wyłączenia |
|---|---|---|---|
| WSP-1.5 | 1.5 | dzieci < 18 w zakresach 218, 221, dentobus, gabinet szkolny | 23.06 wizyta adaptacyjna, 23.0304 pantomogram, profilaktyka § 3 ust. 1 pkt 10, ST30D, ST30E, ST30F, ST30G |
| WSP-1.2 | 1.2 | kobiety w ciąży i połogu, zakres 218 |  |
| WSP-0.8 | 0.8 | kolejny pakiet na tej samej wizycie (najwyżej wyceniony 1,0) | ST30E, ST30G |