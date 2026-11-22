# Audyt świadczeń stomatologicznych NFZ – dorośli i dzieci, ICD-9, ICD-10, ograniczenia, łączenie, dokumentacja

| | |
|---|---|
| Rozpoczęcie audytu | **21.11.2026** (składanie paczki od 17:28 CET) |
| Stan prawny na | **21.11.2026** |
| Wykonawca | Claude (czat) – do zatwierdzenia przez Patryka |
| Charakter | audyt źródeł + baza reguł; **bez implementacji w aplikacji** |
| Pliki danych | `data/nfz/*.json` (+ `schemas/`, `manifest.json`), walidacja `scripts/waliduj_nfz.py` → **OK** |

> Ten raport opisuje przepisy i interpretacje. Nie jest opinią prawną. Tam, gdzie źródło jest interpretacją płatnika (komunikat NFZ) albo opinią, jest to wprost napisane.

---

## 0. Najważniejsze wnioski (TL;DR)

| # | Wniosek | Status | Wpływ na aplikację |
|---|---|---|---|
| 1 | Obowiązuje **Dz.U. 2025 poz. 615** (t.j. rozporządzenia koszykowego) – brak późniejszych zmian w ELI na 21.11.2026 | POTWIERDZONA | podstawa reguł |
| 2 | Zarządzenie **60/2023/DSOZ** – tekst ujednolicony od **01.09.2026** (zm. 95/2026): nowe pakiety **ST30D–ST30G** (higienizacja **tylko < 18 lat**), rozdzielenie złogów miękkie/twarde (23.16011/12/21/22) | POTWIERDZONA | **RYZYKO**: w aplikacji ST30E/ST30G bez ograniczenia wieku |
| 3 | ST30–ST30C = **wyłącznie złogi twarde** i **nie sumują się z 23.1006** (lakierowanie) | POTWIERDZONA (od 01.09.2026 w zał. 1d); historycznie SPORNA | blokada eksportu pary ST30*+23.1006 |
| 4 | **23.1006 lakierowanie – tylko < 18 lat** (zał. 1 i 2) | POTWIERDZONA | sprawdzić, czy aplikacja nie podpowiada go dorosłym |
| 5 | **23.1513 nie istnieje** w ICD-9 PL 5.91 (podrozdział 23.15 kończy się na 23.1512) | POTWIERDZONA | zrzut FAQ z kodem 23.1513 – błędny lub nieaktualny |
| 6 | NFZ używa **wariantów z literą „a”** (23.1012a, 23.3104a, 23.3105a), których nie ma w ICD-9 PL 5.91 (tam: 23.1023, 23.31041, 23.31051) | WYMAGA WERYFIKACJI (sposób sprawozdania) | nie eksportować bez potwierdzenia OW NFZ |
| 7 | **Brak obowiązkowych par ICD-9 ↔ ICD-10** w przeczytanych przepisach | CZĘŚCIOWO POTWIERDZONA | mapowania = podpowiedzi (INFORMACJA), nigdy blokada |
| 8 | Znieczulenie przy ekstrakcji (ST01) i kiretażu (ST04) jest **wliczone w pakiet** – nie rozlicza się go osobno. Zapis „nie obejmuje znieczulenia” w rozporządzeniu dotyczy definicji świadczenia, nie rozliczenia NFZ | POTWIERDZONA (zarządzenie + praktyka lekarza) | BLOKADA osobnego produktu znieczulenia obok ST01/ST04 |
| 9 | Kiretaż u dzieci – komunikat NFZ 22.07.2026 kontra protest NIL | WYMAGA WERYFIKACJI | tylko INFORMACJA |
| 10 | Plik rozporządzenia od Patryka to **57/118 stron** – brak zał. 2a, 3–9, 10a (chirurgia, perio, ortodoncja, protetyka, znieczulenie ogólne, pomoc doraźna, dentobus) | luka | reguły z tych obszarów oznaczone WYMAGA WERYFIKACJI |

---

## Etap A – Akty prawne i źródła

| Akt / źródło | Rola | Stan |
|---|---|---|
| Ustawa o świadczeniach (t.j. Dz.U. 2025 poz. 1461) | podstawa systemu, art. 50 eWUŚ | obowiązuje |
| **Rozporządzenie koszykowe – t.j. Dz.U. 2025 poz. 615** | wykaz świadczeń gwarantowanych + warunki | obowiązuje; sprawdzone w ELI API |
| § 4 ust. 1a (od 01.01.2026) | nowe kryteria znieczulenia ogólnego u dzieci < 18 | obowiązuje |
| **Zarządzenie 60/2023/DSOZ** (t. ujednolicony od 01.09.2026) | produkty, punkty, pakiety, współczynniki, łączenie | obowiązuje; zmiany: 105/2023, 119/2023, 38/2025, 44/2025, **95/2026** |
| ICD-9 PL **5.91** (plik Patryka) | słownik procedur | najnowsza znana (5.89 od 01.09.2026, 5.90 z 25.09.2026) |
| ICD-10 – wydanie polskie (CeZ) | rozpoznania | obowiązuje; **ICD-11 nie wdrożono** |
| Rozporządzenie o dokumentacji medycznej (t.j. Dz.U. 2026 poz. 1391) | dokumentacja | obowiązuje – **paragrafy do odczytu** |
| OWU (t.j. Dz.U. 2026 poz. 712 + zm.) | kary umowne, zwroty | obowiązuje – **paragrafy do odczytu** |
| Komunikaty NFZ: 8924, 9017, 9054, 8386, 6113, webinaria | interpretacje płatnika | – |

Pełny rejestr: `REJESTR_ZRODEL.md` / `data/nfz/sources.json`.

### Weryfikacja plików Patryka

| Plik | Ocena |
|---|---|
| `icd-9_pl_cm_v_5.91.xlsx` | ✅ aktualny. **Uwaga:** mój pierwszy wyciąg (CSV) gubił kody nadrzędne – przebudowano z xlsx (290 kodów, wszystkie poziomy). |
| `Dz.U.2025.615.pdf` | ✅ właściwy akt, ⚠️ **niepełny** (57/118 stron) |
| `prezentacja_stomatologia__11.05.pdf` | ⚠️ **nieaktualna** – sprzed zarządzenia 95/2026; tylko tło |
| zrzut FAQ NFZ (kody zębów/powierzchni) | ⚠️ kod **23.1513 nie istnieje** w 5.91; **23.1501** w 5.91 to „Odbudowa zniszczonego, złamanego kąta w zębach siecznych” |

---

## Etap B – Wykaz ICD-9 / ICD-10

- **ICD-9 PL 5.91, rozdz. 23–24:** 290 kodów → `procedures.json › slownik_icd9_591` (z poziomem i informacją o podkodach).
- **Świadczenia gwarantowane z rozporządzenia:** 217 wierszy z zał. 1, 2, 2b, 10, 10b, 10c (strona PDF, lp, kod, nazwa, pełny tekst warunków).
- **Produkty NFZ:** 84 jednostkowe (zał. 1b) + 43 pakiety (zał. 1c/1d) → `products.json`.
- **ICD-10:** 131 kodów (K00–K14 pełne na poziomie 4 znaków + S02.5, S02.6, S03.2, Z01.2, Z29.8, Z46.3, Z46.4) → `diagnoses.json`.

Krytycznie:
- Polskie nazwy ICD-10 w paczce to **nazwy robocze**. Przed użyciem w interfejsie trzeba je porównać 1:1 z Tomem I CeZ.
- **K02.5** (próchnica z obnażeniem miazgi) i **K12.3** to kody z aktualizacji WHO po 2008. Mogą **nie istnieć w wydaniu polskim**, więc mają status WYMAGA WERYFIKACJI.

---

## Etap C – Mapowanie ICD-9 → ICD-10

- 429 par, **wszystkie**: `typ = sugestia kliniczna`, `wymagane_przez_nfz = false`, `poziom = INFORMACJA`, `status = WYMAGA WERYFIKACJI`.
- Nie znalazłem w przepisach obowiązkowych par. NFZ wymaga ICD-10 w sprawozdaniu, ale nie narzuca pary z procedurą. Mapa potrzeb (wielkopolskie) wskazuje, że raportowane ICD-10 często nie odzwierciedla realnych rozpoznań.
- Aplikacja **nie może** sama wpisywać rozpoznania. Może tylko podpowiadać, a lekarz wybiera.

Szczegóły: `MAPOWANIA_ICD9_ICD10.md`.

---

## Etap D – Limity i łączenie

Kluczowe reguły (pełna lista – `REGULY_ROZLICZEN.md`, 47 reguł):

| Obszar | Reguła | Poziom |
|---|---|---|
| Badanie 23.0101 / ST33 | 1×/rok kalendarzowy | BLOKADA |
| Kontrola 23.0102 / ST34 | 3×/rok; ciąża/połóg ≤ 1×/kwartał | OSTRZEŻENIE |
| Konsultacja 23.0105 | bez łączenia z innymi | BLOKADA |
| Znieczulenie 23.0401–0403 | tylko z innym świadczeniem | BLOKADA |
| RTG 23.0301 | ≤ 2 zdjęcia/rok, opis w dokumentacji | OSTRZEŻENIE |
| Pantomogram 23.0304 | dorośli: endo / przed protetyką, 1×/5 lat; dzieci 5–18: 1×/3 lata, uzasadnienie | OSTRZEŻENIE |
| Złogi 23.1601 / ST30 | 1×/rok kalendarzowy, całe uzębienie | OSTRZEŻENIE |
| ST30–ST30C | tylko złogi twarde; nie z 23.1006 | BLOKADA (para) |
| ST30–ST30G | wzajemnie się wykluczają (wyjątki: ST30D+ST30E, ST30D/F+23.1101) | BLOKADA |
| ST30D–G | tylko < 18; limity 1×/rok (ST30E 4×, 3× z ST30D) | BLOKADA |
| Minimalne czasy ST30* | 10/40/10/10/15/5/30/20 min | OSTRZEŻENIE (dokumentacja) |
| Lakowanie 23.1003 | 6-ki do 8 r.ż., 7-ki do 14 r.ż., 1× | BLOKADA* |
| Lakierowanie 23.1006 | < 18, ≤ 1×/kwartał na ¼ łuku | OSTRZEŻENIE |
| Wizyta adaptacyjna 23.06 | do 6 r.ż., bez łączenia | BLOKADA |
| Protezy całkowite | 1×/5 lat | BLOKADA* |
| Naprawa z wyciskiem, podścielenie | 1×/2 lata | OSTRZEŻENIE |
| Kilka pakietów na wizycie | 1,0 + 0,8 (WKR), nie dla ST30E/ST30G | INFORMACJA |

\* BLOKADA tylko na podstawie zapisów z tego samego konta. Aplikacja nie zna świadczeń z innych gabinetów, więc w pozostałych przypadkach daje INFORMACJĘ.

**Zasada domyślna macierzy łączenia:** para, której nie ma na liście, ma status **WYMAGA DODATKOWEJ WERYFIKACJI**, a nie DOZWOLONE.

---

## Etap E – Dzieci i zmiany 2026

| Zmiana | Od | Źródło |
|---|---|---|
| Znieczulenie ogólne u dzieci < 18: nowe kryteria (§ 4 ust. 1a) – m.in. < 3 lat z ≥ 8 ogniskami próchnicy lub ≥ 4 zębami do leczenia, brak współpracy, alergia, choroby ogólne z opinią specjalisty, ostry stan zapalny | 01.01.2026 | rozporządzenie |
| Pakiety higienizacyjne ST30D–ST30G dla < 18 (minimalne czasy, limity roczne) | 01.09.2026 | zarządzenie 95/2026 |
| Rozdzielenie 23.1601/23.1602 na miękkie/twarde | 01.09.2026 (ICD-9 5.89) | zarządzenie + ICD-9 |
| Współczynnik 1,5 **nie** dla ST30D–G | 01.09.2026 | zarządzenie |
| Kiretaż u dzieci – komunikat NFZ + protest NIL | 22.07.2026 | sporne |

---

## Etap F – Kontrole NFZ i typowe błędy

| Błąd | Skutek | Kontrola w aplikacji |
|---|---|---|
| Świadczenie w sprawozdaniu, a brak w dokumentacji (lub inna data) | zwrot + kara umowna; w skrajnym przypadku sprawa karna | R-DOK-01: eksport tylko z zapisanym opisem z tej samej daty |
| „Rozpisywanie” jednej wizyty na kilka terminów, wpisy na zapas | art. 286 § 1 k.k. (II Ka 168/24) | R-DOK-04: brak zmiany daty wstecz bez jawnego śladu |
| Poprawki bez autoryzacji, podpisy bez dat | dowód przeciw świadczeniodawcy | historia zmian (kto, kiedy) |
| Lakierowanie + złogi na 1 wizycie | korekty finansowe (wsteczne) | R-ST30-LAKIER |
| Zły kod rozliczeniowy | spór o kwalifikację; ciężar dowodu po stronie NFZ (II C 992/22 – laryngologia, analogia) | walidacja kodów + słownik 5.91 |
| Brak opisu RTG, brak czasu przy ST30* | negatywna weryfikacja | ostrzeżenia dokumentacyjne |
| Braki formalne | kara (przykład z kontroli NFZ 15.7320.168.2017: 732,24 zł) | listy kontrolne |

---

## Etap G – Orzecznictwo (tylko sprawdzone sygnatury)

| Sygnatura | Sąd, data | Dziedzina | Teza dla aplikacji | Status |
|---|---|---|---|---|
| **II Ka 168/24** | SO Siedlce, 31.01.2025 | **ortodoncja NFZ** | fikcyjne daty, wpisy niewykonanych świadczeń, nieautoryzowane poprawki → oszustwo, 5-letni zakaz | POTWIERDZONA (SAOS 523200) |
| **II C 992/22** | SR Białystok, 01.03.2024 | laryngologia (**nie stomatologia**) | spór o kod; NFZ musi udowodnić; niejasności zarządzenia obciążają autora | POTWIERDZONA (SAOS 544836) |
| III CSK 296/16 | SN, 24.11.2017 | zwrot nienależnych środków, kara za dokumentację | **treści nie pobrano** – nie cytować | WYMAGA WERYFIKACJI |

Nie znalazłem żadnej sygnatury dotyczącej wprost ST30 ani lakierowania. Nic nie zostało wymyślone.

---

## Etap H – Praktyka, fora, stanowiska środowiska

- **Spór o ST30 i lakierowanie** (marzec–maj 2026):
  - komunikaty NFZ 1292084 (25.03), 819330 (24.03) i 8924 (13.04) uznały, że wycena ST30–ST30C obejmuje lakierowanie;
  - po nich przyszły wsteczne korekty finansowe;
  - Lubelska Izba Lekarska, Prezydium NRL (30/26/P-IX, 39/26/P-IX) i Konfederacja Lewiatan (19.05.2026) zakwestionowały zmianę zakresu świadczenia komunikatem;
  - interpelacja 16442 przywołuje opinię konsultanta krajowego ds. periodontologii: brak wskazań do obowiązkowej fluoryzacji.
- **Od 01.09.2026** wyłączenie 23.1006 przy ST30–ST30C jest już **wprost w zał. 1d zarządzenia**. Dla nowych rozliczeń sprawa jest więc jednoznaczna, a sporne pozostają rozliczenia sprzed tej daty.
- **Pytania praktyków z komunikatów 9017 i 9054**: ST30D a ST33; ST30 a ST30F w tym samym roku; limity czasowe a pacjenci bólowi. Odpowiedzi trzeba przenieść dosłownie. **Do zrobienia: ponowny odczyt komunikatów** (tu przeczytane tylko fragmenty).
- Forów typu Reddit i grup lekarzy na FB nie dało się zweryfikować. Żadnej „wiedzy z forów” nie wpisano do reguł.

---

## Porównanie z aplikacją Gabinet (stan repo, tylko odczyt)

| Element | W aplikacji | Wynik audytu | Działanie (decyzja Patryka) |
|---|---|---|---|
| Punkty ST01, ST02, ST04, ST19, ST26, ST28, ST30, ST30E, ST30G, ST33, ST34 | zgodne z zał. 1c | ✅ | – |
| ST30E / ST30G | „Profesjonalna higienizacja” bez ograniczenia wieku | ⚠️ tylko < 18 | dodać ograniczenie wieku / ostrzeżenie |
| 23.1006 | dostępne | ⚠️ tylko < 18; nie z ST30–ST30C | ostrzeżenie |
| ST04 kiretaż u dzieci | dostępny | ❓ sporne | INFORMACJA |
| 23.1601 / 23.1602 | ? | od 01.09.2026 podkody | sprawdzić eksport |
| Kody „…a” | ? | brak w 5.91 | nie eksportować bez potwierdzenia |

**Ograniczenie z zasady SaaS:** numer zęba, wiek pacjenta i ciąża to dane pacjenta. Zgodnie z CLAUDE.md (zasada 1) reguły, które ich potrzebują, muszą działać **lokalnie na urządzeniu**, a serwer nie może tych danych dostać. To decyzja projektowa do zatwierdzenia.

---

## Listy kontrolne

### Przed rozliczeniem wizyty (lekarz)
- [ ] Prawo do świadczeń potwierdzone (eWUŚ lub dokument)
- [ ] Opis wizyty zapisany **z tą samą datą**, co rozliczenie
- [ ] Każde świadczenie ma ząb lub lokalizację (ISO 3950, „ZD” dla zęba dodatkowego)
- [ ] RTG ma opis w dokumentacji
- [ ] Przy ST30*: rodzaj złogów (twarde/miękkie) i czas zabiegu
- [ ] Przy znieczuleniu ogólnym: udokumentowane kryterium z § 4
- [ ] Ciąża: karta przebiegu ciąży (dla 1,2 / WKC)
- [ ] Protezy: oświadczenie o uprawnieniu, podpis przy odbiorze
- [ ] Rozpoznanie ICD-10 wybrane przez lekarza (nie automatycznie)

### Przed wdrożeniem reguł (Claude Code)
- [ ] `python3 scripts/waliduj_nfz.py` → OK
- [ ] Żadna reguła WYMAGA WERYFIKACJI nie ma poziomu wyższego niż INFORMACJA
- [ ] BLOKADA działa tylko na eksport, nie na zapis opisu
- [ ] Testy dla każdej reguły BLOKADA (pozytywny i negatywny)
- [ ] Reguły z danymi pacjenta liczone tylko na urządzeniu

---

## Projekt techniczny (propozycja – bez implementacji)

```
data/nfz/*.json  ──(build/test)──►  silnik reguł (czysta funkcja, TS)
                                     ├─ warstwa medyczna      → INFORMACJA/OSTRZEŻENIE
                                     ├─ warstwa dokumentacyjna→ OSTRZEŻENIE/BLOKADA eksportu
                                     └─ warstwa rozliczeniowa → limity, łączenie, współczynniki
wejście: wizyta {data, zakres, świadczenia[], wiek*, ciąża*, ząb*}   (* tylko na urządzeniu)
wyjście: [{regula_id, poziom, komunikat, zrodla[]}]
```

- Reguły to dane (JSON), a nie `if` w kodzie. Każdy komunikat w interfejsie pokazuje `id` reguły i źródło.
- Wersjonowanie: `manifest.json` (wersja + SHA-256). Reguły mają `obowiazuje_od`/`obowiazuje_do`, a silnik ocenia wizytę według **daty wizyty**, nie daty dzisiejszej.
- Decyzja lekarza przy OSTRZEŻENIU zapisuje się lokalnie (kto, kiedy, którą regułę pominięto).
- Zmiana w danych NFZ to nowa wersja manifestu plus ponowne uruchomienie testów. Wykonanych migracji bazy nie edytuje się (zasada 12).

## Plan testów

| Grupa | Przykłady przypadków |
|---|---|
| Walidacja danych | schematy, odwołania do źródeł, SHA-256, BLOKADA ⇒ POTWIERDZONA |
| Limity | 2× 23.0101 w roku → BLOKADA; 4× 23.0102 → OSTRZEŻENIE; ST30E 5× → BLOKADA; ST30E 4× + ST30D → BLOKADA |
| Łączenie | ST30 + 23.1006 → BLOKADA; ST30D + ST30E → OK; 23.0105 + 23.1101 → BLOKADA; 23.0401 samo → BLOKADA |
| Wiek | ST30E u 18-latka → BLOKADA; 23.1006 u dorosłego → OSTRZEŻENIE; 23.1003 na 6-ce u 9-latka → BLOKADA |
| Daty | ST30D z datą 31.08.2026 → reguła nieaktywna; 23.1601 bez podkodu po 01.09.2026 → BLOKADA |
| Kody | 23.1513 → BLOKADA; 23.1012a → INFORMACJA |
| Współczynniki | dziecko + 23.06 → bez 1,5; 2 pakiety → 1,0 + 0,8; ST30E w parze → bez 0,8 |
| Bezpieczeństwo | wiek/ząb/ciąża nie trafiają do API (test sieci jak w `tests/e2e`) |
| Nieblokowanie | każdy przypadek BLOKADA: opis kliniczny da się zapisać, blokowany jest tylko eksport |
