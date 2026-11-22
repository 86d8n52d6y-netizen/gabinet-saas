# Pola formularzy (badania i procedury)

> Plik generowany: `python3 scripts/buduj_docs_bazy.py` z danych w `data/`. Nie edytuj ręcznie – popraw JSON.

Typy: tekst, tekst_dlugi, wybor, wybor_wielokrotny (z możliwością własnej wartości), przelacznik, liczba, data, zab/zeby/powierzchnie (diagram FDI). Żadne pole nie jest wymagane do zapisu i żadne nie ma domyślnego wyniku.

| Pole | Etykieta | Typ | Opcje | Badanie |
|---|---|---|---|---|
| `POLE-ZAB` | Ząb (FDI) | zab | — | wspólne |
| `POLE-ZEBY` | Zęby / okolica (FDI) | zeby | — | wspólne |
| `POLE-POWIERZCHNIE` | Powierzchnie | powierzchnie | — | wspólne |
| `POLE-LOKALIZACJA` | Lokalizacja (tekstem) | tekst | — | wspólne |
| `POLE-LUK` | Zakres łuku | wybor | ¼ łuku (ćwiartka); ½ łuku; cały łuk; całe uzębienie + własna | wspólne |
| `POLE-ROZPOZNANIE` | Rozpoznanie (ICD-10) | tekst | — | wspólne |
| `POLE-WSKAZANIE` | Wskazanie kliniczne | tekst_dlugi | — | wspólne |
| `POLE-ZNIECZ-RODZAJ` | Znieczulenie | wybor | nie stosowano; powierzchniowe; nasiękowe; przewodowe wewnątrzustne; przewodowe zewnątrzustne; śródwięzadłowe + własna | wspólne |
| `POLE-ZNIECZ-PREPARAT` | Preparat znieczulający | tekst | — | wspólne |
| `POLE-ZNIECZ-DAWKA` | Dawka (ml / ampułki) | tekst | — | wspólne |
| `POLE-ZNIECZ-MIEJSCE` | Miejsce podania | tekst | — | wspólne |
| `POLE-IZOLACJA` | Izolacja pola zabiegowego | wybor | koferdam; wałki ligninowe i ślinociąg; OptraGate / rozwieracz; bez izolacji (uzasadnij) + własna | wspólne |
| `POLE-MATERIAL` | Materiał | tekst | — | wspólne |
| `POLE-MATERIAL-PODKLAD` | Materiał podkładowy / ochrona miazgi | tekst | — | wspólne |
| `POLE-KOLOR` | Kolor (skala) | tekst | — | wspólne |
| `POLE-PRZEBIEG` | Przebieg (opis czynności) | tekst_dlugi | — | wspólne |
| `POLE-WYNIK` | Wynik / ocena efektu | tekst_dlugi | — | wspólne |
| `POLE-POWIKLANIA` | Powikłania w trakcie / bezpośrednio po | wybor | nie wystąpiły; wystąpiły – opis poniżej + własna | wspólne |
| `POLE-POWIKLANIA-OPIS` | Opis powikłań i postępowania | tekst_dlugi | — | wspólne |
| `POLE-ZALECENIA-FORMA` | Forma przekazania zaleceń | wybor | ustnie; ustnie i pisemnie + własna | wspólne |
| `POLE-ZALECENIA` | Zalecenia dla pacjenta | tekst_dlugi | — | wspólne |
| `POLE-KONTROLA` | Termin / warunki kontroli | tekst | — | wspólne |
| `POLE-DECYZJA` | Decyzja lekarza / plan dalszego postępowania | tekst_dlugi | — | wspólne |
| `POLE-UWAGI` | Uwagi | tekst_dlugi | — | wspólne |
| `POLE-ZGODA` | Zgoda pacjenta (świadoma) – odnotowana | przelacznik | — | wspólne |
| `POLE-RTG` | Zdjęcie RTG – numer / data / opis | tekst | — | wspólne |
| `POLE-CZAS` | Czas zabiegu | liczba (min) | — | wspólne |
| `POLE-WIEK` | Wiek pacjenta | liczba (lata) | — | wspólne |
| `POLE-DATA` | Data | data | — | wspólne |
| `POLE-ENDO-KANALY` | Kanały: nazwa – długość robocza – punkt odniesienia – rozmiar | tekst_dlugi | — | wspólne |
| `POLE-ENDO-PLUKANIE` | Płukanie kanałów (preparaty) | wybor_wielokrotny | podchloryn sodu; EDTA; chlorheksydyna; sól fizjologiczna; aktywacja płynu + własna | wspólne |
| `POLE-WYW-POWOD` | Powód zgłoszenia (słowami pacjenta) | tekst | — | BAD-WYWIAD |
| `POLE-WYW-DOLEGLIWOSCI` | Dolegliwości – charakter, czas trwania, czynniki wywołujące | tekst_dlugi | — | BAD-WYWIAD |
| `POLE-WYW-CHOROBY` | Choroby ogólne | wybor_wielokrotny | brak – wg pacjenta; choroby układu krążenia; cukrzyca; choroby krwi / skazy krwotoczne; padaczka; astma / POChP; choroby tarczycy; choroba nowotworowa (leczenie onkologiczne, radioterapia głowy i szyi); osteoporoza (leki antyresorpcyjne); choroby zakaźne (HBV, HCV, HIV); zaburzenia psychiczne + własna | BAD-WYWIAD |
| `POLE-WYW-LEKI` | Leki przyjmowane stale (w tym przeciwkrzepliwe, antyresorpcyjne) | tekst_dlugi | — | BAD-WYWIAD |
| `POLE-WYW-ALERGIE` | Alergie (leki, lateks, materiały, środki znieczulające) | tekst | — | BAD-WYWIAD |
| `POLE-WYW-CIAZA` | Ciąża / karmienie piersią | wybor | nie dotyczy; nie; ciąża – tydzień:; karmienie piersią + własna | BAD-WYWIAD |
| `POLE-WYW-NALOGI` | Używki | wybor_wielokrotny | nie pali; palenie tytoniu; e-papierosy; alkohol; inne + własna | BAD-WYWIAD |
| `POLE-WYW-STOMAT` | Wywiad stomatologiczny (dotychczasowe leczenie, powikłania po znieczuleniu / ekstrakcji, częstość wizyt) | tekst_dlugi | — | BAD-WYWIAD |
| `POLE-WYW-HIGIENA` | Nawyki higieniczne i dietetyczne (szczotkowanie, nici, fluor, cukry) | tekst_dlugi | — | BAD-WYWIAD |
| `POLE-WYW-PARAFUNKCJE` | Parafunkcje | wybor_wielokrotny | nie zgłasza; zaciskanie / zgrzytanie zębami; obgryzanie paznokci / przedmiotów; ssanie palca / smoczka; oddychanie przez usta + własna | BAD-WYWIAD |
| `POLE-ZEW-TWARZ` | Symetria i obrys twarzy | wybor | symetryczna; asymetria – opis; obrzęk – lokalizacja + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-SKORA` | Skóra twarzy | wybor | bez zmian chorobowych; zmiana – opis + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-WARGI` | Czerwień wargowa i kąciki ust | wybor | bez zmian chorobowych; zajady; opryszczka; zmiana – opis + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-WEZLY` | Węzły chłonne (podżuchwowe, podbródkowe, szyjne) | wybor | niewyczuwalne; powiększone – opis (wielkość, bolesność, ruchomość) + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-SSZ` | Stawy skroniowo-żuchwowe (przesiewowo) | wybor | bez objawów; objawy – patrz badanie SSŻ + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-MIESNIE` | Mięśnie żucia (palpacja przesiewowa) | wybor | niebolesne; bolesność – lokalizacja + własna | BAD-ZEWNATRZUSTNE |
| `POLE-ZEW-OPIS` | Opis stwierdzonych odchyleń | tekst_dlugi | — | BAD-ZEWNATRZUSTNE |
| `POLE-WEW-PRZEDSIONEK` | Przedsionek, wargi i policzki (strona śluzówkowa) | wybor | bez zmian chorobowych; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-JEZYK` | Język | wybor | bez zmian chorobowych; nalot; język geograficzny; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-DNO` | Dno jamy ustnej | wybor | bez zmian chorobowych; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-PODNIEBIENIE` | Podniebienie twarde i miękkie | wybor | bez zmian chorobowych; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-GARDLO` | Cieśń gardła / migdałki | wybor | bez zmian chorobowych; przerost migdałków; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-SLINIANKI` | Ujścia ślinianek, ślina | wybor | ślina wypływa, przejrzysta; suchość błony śluzowej; zmiana – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-WEDZIDELKA` | Wędzidełka warg i języka | wybor | przyczep bez zaburzeń; przyczep wysoki / skrócone – opis + własna | BAD-WEWNATRZUSTNE |
| `POLE-WEW-OPIS` | Opis stwierdzonych zmian | tekst_dlugi | — | BAD-WEWNATRZUSTNE |
| `POLE-BL-LOK` | Lokalizacja zmiany | tekst | — | BAD-BLONA |
| `POLE-BL-WYM` | Największy wymiar zmiany | liczba (mm) | — | BAD-BLONA |
| `POLE-BL-WYKWIT` | Rodzaj wykwitu | wybor_wielokrotny | plama biała; plama czerwona; nadżerka; owrzodzenie; pęcherz / pęcherzyk; grudka / guzek; rogowacenie siateczkowate + własna | BAD-BLONA |
| `POLE-BL-POW` | Powierzchnia | wybor | gładka; nierówna / brodawkowata; pokryta nalotem dającym się zetrzeć; pokryta nalotem niedającym się zetrzeć + własna | BAD-BLONA |
| `POLE-BL-KONS` | Konsystencja (palpacja) | wybor | miękka; elastyczna; twarda / naciek + własna | BAD-BLONA |
| `POLE-BL-BOL` | Bolesność | wybor | niebolesna; bolesna + własna | BAD-BLONA |
| `POLE-BL-CZAS` | Czas trwania (wg pacjenta) | tekst | — | BAD-BLONA |
| `POLE-BL-CZYNNIK` | Prawdopodobny czynnik miejscowy (np. ostra krawędź, proteza) | tekst | — | BAD-BLONA |
| `POLE-BL-DECYZJA` | Postępowanie | wybor | usunięcie czynnika i kontrola za 2 tygodnie; leczenie miejscowe; skierowanie do chirurga stomatologa / specjalisty chorób błony śluzowej; pilne skierowanie onkologiczne + własna | BAD-BLONA |
| `POLE-UZ-TYP` | Uzębienie | wybor | stałe; mieszane; mleczne + własna | BAD-UZEBIENIE |
| `POLE-UZ-DIAGRAM` | Stan zębów – diagram (próchnica, wypełnienia, braki, korony, leczenie kanałowe) | tekst_dlugi | — | BAD-UZEBIENIE |
| `POLE-UZ-SYSTEM` | Kryteria oceny próchnicy | wybor | ICDAS II; opisowo (powierzchniowa / średnia / głęboka) + własna | BAD-UZEBIENIE |
| `POLE-UZ-DMFT` | DMFT / dmft | liczba | — | BAD-UZEBIENIE |
| `POLE-UZ-NIEPROCH` | Zmiany niepróchnicowe | wybor_wielokrotny | starcie; abfrakcje; erozje; hipomineralizacja (MIH); pęknięcia; przebarwienia + własna | BAD-UZEBIENIE |
| `POLE-UZ-RYZYKO` | Ryzyko próchnicy (ocena lekarza) | wybor | niskie; umiarkowane; wysokie + własna | BAD-UZEBIENIE |
| `POLE-UZ-OPIS` | Opis odchyleń | tekst_dlugi | — | BAD-UZEBIENIE |
| `POLE-PZ-SKRINING` | Badanie przesiewowe (BPE / PSR) | wybor | wykonano – wyniki sekstantów; nie wykonano + własna | BAD-PRZYZEBIE |
| `POLE-PZ-BPE` | Wyniki BPE/PSR (sekstanty, 0–4, *) | tekst | — | BAD-PRZYZEBIE |
| `POLE-PZ-BOP` | Krwawienie przy zgłębnikowaniu (BOP) | liczba (%) | — | BAD-PRZYZEBIE |
| `POLE-PZ-PPD` | Głębokość kieszonek (PPD) – miejsca ≥ 4 mm | tekst_dlugi | — | BAD-PRZYZEBIE |
| `POLE-PZ-CAL` | Utrata przyczepu (CAL) / recesje | tekst_dlugi | — | BAD-PRZYZEBIE |
| `POLE-PZ-RUCH` | Ruchomość zębów (stopień, zęby) | tekst | — | BAD-PRZYZEBIE |
| `POLE-PZ-FURK` | Zajęcie furkacji (stopień, zęby) | tekst | — | BAD-PRZYZEBIE |
| `POLE-PZ-ROZPOZNANIE` | Ocena stanu przyzębia (klasyfikacja 2017) | wybor | zdrowe przyzębie; zapalenie dziąseł wywołane płytką; zapalenie przyzębia – stadium/stopień:; inne – opis + własna | BAD-PRZYZEBIE |
| `POLE-PZ-STADIUM` | Stadium zapalenia przyzębia | wybor | I; II; III; IV + własna | BAD-PRZYZEBIE |
| `POLE-PZ-STOPIEN` | Stopień (tempo progresji) | wybor | A; B; C + własna | BAD-PRZYZEBIE |
| `POLE-HG-WSKAZNIK` | Wskaźnik płytki | wybor | API (Lange); PCR (O’Leary); OHI-S; opisowo + własna | BAD-HIGIENA |
| `POLE-HG-WARTOSC` | Wartość wskaźnika płytki | liczba (%) | — | BAD-HIGIENA |
| `POLE-HG-GI` | GI (Löe–Silness) / SBI | liczba | — | BAD-HIGIENA |
| `POLE-HG-ZLOGI` | Złogi | wybor_wielokrotny | brak; płytka (złogi miękkie); kamień naddziąsłowy; kamień poddziąsłowy; przebarwienia + własna | BAD-HIGIENA |
| `POLE-HG-OCENA` | Ocena higieny (lekarz) | wybor | dobra; dostateczna; zła + własna | BAD-HIGIENA |
| `POLE-HG-INSTRUKTAZ` | Przeprowadzono instruktaż higieny | przelacznik | — | BAD-HIGIENA |
| `POLE-HG-INSTR-OPIS` | Zakres instruktażu (technika, przybory, fluorki) | tekst_dlugi | — | BAD-HIGIENA |
| `POLE-ZG-ANGLE` | Klasa Angle’a (trzonowce) | wybor | I; II; III; nie do oceny + własna | BAD-ZGRYZ |
| `POLE-ZG-OJ` | Nagryz poziomy (overjet) | liczba (mm) | — | BAD-ZGRYZ |
| `POLE-ZG-OB` | Nagryz pionowy (overbite) | liczba (mm) | — | BAD-ZGRYZ |
| `POLE-ZG-WADY` | Wady zgryzu | wybor_wielokrotny | brak; zgryz krzyżowy; zgryz otwarty; zgryz głęboki; przodozgryz; stłoczenia; diastema + własna | BAD-ZGRYZ |
| `POLE-ZG-LINIA` | Linia pośrodkowa | wybor | zgodna; przesunięta – mm i strona + własna | BAD-ZGRYZ |
| `POLE-ZG-PROWADZENIE` | Prowadzenie | wybor | kłowe; grupowe; przednie; zaburzone – kontakty przedwczesne + własna | BAD-ZGRYZ |
| `POLE-ZG-OPIS` | Opis | tekst_dlugi | — | BAD-ZGRYZ |
| `POLE-SSZ-BOL` | Ból w okolicy SSŻ / mięśni (ostatnie 30 dni) | wybor | nie; tak – lokalizacja + własna | BAD-SSZ |
| `POLE-SSZ-ODWODZENIE` | Maksymalne odwodzenie bez bólu / z pomocą | liczba (mm) | — | BAD-SSZ |
| `POLE-SSZ-TOR` | Tor odwodzenia | wybor | prosty; zbaczanie (deviation); zbaczanie z powrotem (deflection) + własna | BAD-SSZ |
| `POLE-SSZ-ODGLOSY` | Odgłosy stawowe | wybor_wielokrotny | brak; trzask przy otwieraniu; trzask przy zamykaniu; trzeszczenia + własna | BAD-SSZ |
| `POLE-SSZ-PALPACJA` | Palpacja (żwacze, skroniowe, staw) – ból znany pacjentowi | tekst | — | BAD-SSZ |
| `POLE-SSZ-ZABLOK` | Zablokowanie / ograniczenie otwierania | wybor | nie; tak – opis + własna | BAD-SSZ |
| `POLE-SSZ-OPIS` | Opis i wstępna ocena | tekst_dlugi | — | BAD-SSZ |
| `POLE-ZY-ZIMNO` | Test na zimno | wybor | dodatni – reakcja krótkotrwała; dodatni – reakcja przedłużona (> 10 s); ujemny; niejednoznaczny + własna | BAD-ZYWOTNOSC |
| `POLE-ZY-EPT` | Elektryczny test żywotności (wartość / wynik) | tekst | — | BAD-ZYWOTNOSC |
| `POLE-ZY-OPUK` | Opukiwanie | wybor | niebolesne; bolesne pionowo; bolesne poziomo + własna | BAD-ZYWOTNOSC |
| `POLE-ZY-PALP` | Palpacja okolicy wierzchołka | wybor | niebolesna; bolesna; obrzęk / przetoka + własna | BAD-ZYWOTNOSC |
| `POLE-ZY-NAGRYZ` | Test nagryzania | wybor | niebolesny; bolesny + własna | BAD-ZYWOTNOSC |
| `POLE-ZY-KONTROLA` | Ząb kontrolny (porównawczy) i jego wynik | tekst | — | BAD-ZYWOTNOSC |
| `POLE-ZY-OCENA` | Ocena stanu miazgi / tkanek okołowierzchołkowych | wybor | miazga żywa – bez objawów; odwracalne zapalenie miazgi; nieodwracalne zapalenie miazgi; martwica miazgi; ząb leczony kanałowo; zmiana okołowierzchołkowa + własna | BAD-ZYWOTNOSC |
| `POLE-RTG-RODZAJ` | Rodzaj zdjęcia | wybor | zdjęcie wewnątrzustne okołowierzchołkowe; zdjęcie zgryzowo-skrzydłowe; pantomogram; CBCT (poza gabinetem) + własna | BAD-RTG |
| `POLE-RTG-WSKAZANIE` | Uzasadnienie wykonania (wskazanie) | tekst | — | BAD-RTG |
| `POLE-RTG-OPIS` | Opis zdjęcia (zęby, ozębna, kość, zmiany) | tekst_dlugi | — | BAD-RTG |
| `POLE-RTG-OPIS-OBOW` | Opis zdjęcia wpisany do dokumentacji | przelacznik | — | BAD-RTG |
| `POLE-UR-OKOLICZNOSCI` | Okoliczności urazu (kiedy, gdzie, jak) | tekst_dlugi | — | BAD-PO-URAZIE |
| `POLE-UR-RODZAJ` | Rodzaj urazu (IADT) | wybor | infrakcja szkliwa; złamanie korony bez obnażenia miazgi; złamanie korony z obnażeniem miazgi; złamanie korzenia; wstrząs; nadwichnięcie; zwichnięcie boczne; wtłoczenie; wysunięcie; zwichnięcie całkowite (awulsja) + własna | BAD-PO-URAZIE |
| `POLE-UR-TKANKI` | Tkanki miękkie (rany, fragmenty w wardze) | tekst | — | BAD-PO-URAZIE |
| `POLE-UR-RUCH` | Ruchomość / przemieszczenie | wybor | brak; ruchomość – stopień; przemieszczenie – kierunek + własna | BAD-PO-URAZIE |
| `POLE-UR-SZCZEPIENIE` | Zweryfikowano szczepienie przeciw tężcowi (przy ranach / awulsji) | przelacznik | — | BAD-PO-URAZIE |
| `POLE-UR-PLAN` | Plan kontroli (terminy wg IADT) | tekst | — | BAD-PO-URAZIE |
| `POLE-DZ-WIEK` | Wiek dziecka | liczba (lata) | — | BAD-DZIECKO |
| `POLE-DZ-WSPOLPRACA` | Współpraca (skala Franklla) | wybor | 1 – zdecydowanie negatywna; 2 – negatywna; 3 – pozytywna; 4 – zdecydowanie pozytywna + własna | BAD-DZIECKO |
| `POLE-DZ-FLUOR` | Ekspozycja na fluorki | wybor | pasta z fluorem odpowiednia do wieku; pasta bez fluoru; lakier fluorkowy w gabinecie; nie ustalono + własna | BAD-DZIECKO |
| `POLE-DZ-NAWYKI` | Nawyki | wybor_wielokrotny | butelka / karmienie nocne; częste słodkie przekąski / napoje; ssanie smoczka / palca; oddychanie przez usta + własna | BAD-DZIECKO |
| `POLE-DZ-ROZWOJ` | Wyrzynanie i rozwój uzębienia (zgodność z wiekiem) | tekst | — | BAD-DZIECKO |
| `POLE-DZ-OPIEKUN` | Informacje przekazano opiekunowi | wybor | tak; nie dotyczy (pacjent pełnoletni) + własna | BAD-DZIECKO |
| `POLE-KO-ZMIANY` | Zmiany od ostatniej wizyty (wywiad, nowe dolegliwości, leki) | tekst_dlugi | — | BAD-KONTROLNE |
| `POLE-KO-OCENA` | Ocena leczenia / stanu jamy ustnej na kontroli | tekst_dlugi | — | BAD-KONTROLNE |
| `POLE-PL-ZABIEG` | Planowany zabieg | tekst | — | BAD-PRZED-LECZENIEM |
| `POLE-PL-RYZYKA` | Czynniki ryzyka zabiegu | wybor_wielokrotny | brak – wg wywiadu; leki przeciwkrzepliwe / antyagregacyjne; leki antyresorpcyjne; radioterapia głowy i szyi; cukrzyca niewyrównana; ciąża; alergia na środki znieczulające; choroby serca – profilaktyka antybiotykowa do rozważenia + własna | BAD-PRZED-LECZENIEM |
| `POLE-PL-BADANIA` | Wyniki badań dodatkowych (INR, RTG, konsultacje) | tekst_dlugi | — | BAD-PRZED-LECZENIEM |
| `POLE-PL-ALTERNATYWY` | Omówione alternatywy i ryzyka | tekst_dlugi | — | BAD-PRZED-LECZENIEM |
| `POLE-PO-LECZENIE` | Leczenie zakończone (rodzaj, zęby, data) | tekst | — | BAD-PO-LECZENIU |
| `POLE-PO-OCENA` | Ocena wyniku leczenia (klinicznie / RTG) | tekst_dlugi | — | BAD-PO-LECZENIU |
| `POLE-PO-WYNIK` | Wynik | wybor | powodzenie; niepewny – dalsza obserwacja; niepowodzenie – plan + własna | BAD-PO-LECZENIU |
