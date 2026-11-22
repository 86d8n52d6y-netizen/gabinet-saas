# Moduły Opisy NFZ, Opisy prywatne i Kalendarz – zmiany względem obecnej aplikacji

Źródło: repo `opisy-nfz`, commit `716689d` – pliki `nfz.html`, `szablony.js`, `prywatne.html`, `prywatne-katalog.js`, `kalendarz.html`, `wspolne.css` (logika, pytania, reguły NFZ, szablony i teksty bez zmian).
Plik `wspolne.js` (sejf z hasłem w przeglądarce) zastąpiony przez `gabinet-saas.js`.

## Opisy NFZ (`nfz.html`)

| # | Poprawka |
|---|---|
| P1 | czcionki lokalnie zamiast Google Fonts (prywatność: brak wysyłania IP do Google; CSP tylko własne zasoby) |
| P2 | tytuł strony w aplikacji Gabinet |
| P3 | bez manifestu i ikon wersji statycznej (aplikacja SaaS ma własne) |
| P4 | wspólne style z zasobów chronionych logowaniem |
| P5 | wspolne.js (sejf lokalny z hasłem) → gabinet-saas.js (konto SaaS: klucz urządzenia, synchronizacja danych bez treści opisów); dane startowe wstawia serwer w miejsce znacznika |
| P6 | szablony.js z zasobów chronionych logowaniem |
| P7 | identyfikator gabinetu: UUID z bazy (36 znaków) zamiast „c1”…„c24” z Kalendarza |
| P8 | pasek dolny (Historia, Statystyki, Ustawienia): bez kwoty „Dziś: … zł” – zarobki tylko w statystykach (prompt Patryka 21.11.2026, pkt 3.1; obliczenia bez zmian) |
| P9 | pasek dolny (Kody): bez kwoty „Dziś: … zł” (pkt 3.1) |
| P10 | pasek dolny (Pytania, Opis): bez wyceny wizyty w zł – wycena zostaje w karcie „Cały opis” i „Rozliczenie wizyty” (pkt 3.1) |
| P11 | badanie po urazie (ST28): przyczyna „nagryzienie na twardy przedmiot” jako osobna opcja (pkt 7.1; trafia do opisu jak pozostałe przyczyny) |
| P12 | leczenie zachowawcze: opcjonalna informacja o niepewnym rokowaniu (pkt 7.2) – domyślnie nic nie dodaje; wybór użytkownika, tekst edytowalny w kroku 3 |
| P13 | niepewne rokowanie: zdanie na końcu opisu ostatniego zabiegu zachowawczego (tylko po wyborze w P12) |
| P14 | Statystyki – dni: bez kolumn „Z punktów” i „Z przeglądów” (prompt Patryka 21.11.2026, pkt 3.2; „Razem”, punkty i godziny przeglądów zostają) |
| P15 | Statystyki – dni: wiersze bez kwot „z punktów” i „z przeglądów” |
| P16 | Statystyki – tygodnie: bez kolumn „Z punktów” i „Z przeglądów” (pkt 3.2) |
| P17 | Statystyki – tygodnie: wiersze bez tych kwot |
| P18 | Statystyki – miesiące: bez kolumn „Z punktów” i „Z przeglądów” (pkt 3.2) |
| P19 | Statystyki – miesiące: wiersze bez tych kwot |
| P20 | lakiery fluorkowe (1101): lista podpowiedzi rozszerzona – Duraphat, Fluor Protector (decyzja Patryka 21.11.2026, pkt 1.1); własna nazwa nadal wpisywana ręcznie |
| P21 | lakierowanie zębów (1006): opcjonalny wybór preparatu – dopisywany do opisu tylko po wybraniu (pkt 1.1); Elmex jako żel (nie lakier) |
| P22 | lista preparatów fluorkowych (wspólna dla 1101 i 1006) |
| P23 | nazwa kompozytu: podpowiedzi z „Moich materiałów” (Ustawienia; prompt Patryka 21.11.2026, pkt 1.2) – nadal można wpisać dowolną nazwę |
| P24 | materiał podkładowy (głęboka próchnica): pole przy leczeniu zachowawczym i urazie – domyślnie Ionosit (tekst bez zmian), podpowiedzi z „Moich materiałów” (pkt 1.2) |
| P25 | materiał podkładowy w opisie: wybrana nazwa zamiast „Ionosit” (puste pole = Ionosit, jak dotąd) |
| P26 | wędzidełka: domyślnie „Typ I – śluzówkowy” (decyzja Patryka 21.11.2026, pkt 2.1); zmiana tylko, gdy jest inaczej |
| P27 | wywiad: opcjonalne pole „aktualnie przyjmowane leki” (pkt 2.1; tylko w treści opisu na urządzeniu) |
| P28 | opis badania: wędzidełka domyślnie Typ I (P26) |
| P28a | opis badania: wędzidełko dolne domyślnie Typ I (P26) |
| P29 | opis badania: linia „Aktualnie przyjmowane leki – …” tylko, gdy wpisano (P27) |
| P30 | przycisk „Wywiad bez obciążeń” – jednym kliknięciem brak alergii, chorób i leków; nie nadpisuje wpisanych (pkt 2.1) |
| P30a | obsługa przycisku „Wywiad bez obciążeń”: uzupełnia tylko puste pola |
| P31 | znieczulenie przy wypełnieniach, endo i ST30 (decyzja Patryka 21.11.2026, pkt 6.3): przyciski Dentocaine / Mark3 / bez znieczulenia + własny preparat; rodzaj i dawka (domyślnie 1 amp., do zmiany); nic nie wybrane = opis bez zmian |
| P32 | znieczulenie w opisie: zdanie zaraz po tytule pierwszego zabiegu z listy (P31); ekstrakcje ST01/ST02 bez zmian (mają własne znieczulenie) |
| P33 | stałe znieczuleń (P31–P32) |
| P34 | zalecenia: przełącznik „ustnie / ustnie i pisemnie” przy każdej wizycie, domyślnie „ustnie” (decyzja Patryka 21.11.2026, pkt 6.5) |
| P35 | zalecenia w opisie: przy „ustnie” fraza „ustnie i pisemnie” ze stałych tekstów zamieniona na „ustnie” (stałe teksty w Ustawieniach bez zmian) |
| P36 | stałe zaleceń (P34–P35) |
| P37 | trzy szybkie opcje (decyzja Patryka 21.11.2026, pkt 6.4): kolor wypełnienia, nazwa kompozytu, lakier fluorkowy – 3 najczęściej używane (licznik na tym urządzeniu, bez danych pacjentów; na start: A1/A2/A3 i początek listy); nadal można wpisać własną wartość |
| P38 | funkcje szybkich opcji NFZ (P37) |
| P39 | obsługa szybkich opcji i nauka „najczęściej używanych” przy kopiowaniu opisu |
| P39a | zapamiętanie użytych wartości (kolor, kompozyt, lakier) przy kopiowaniu opisu |
| P39b | wygląd zaznaczonej szybkiej opcji |
| P40 | podsumowanie na początku opisu (decyzja Patryka 21.11.2026, pkt 6.1): „Wykonano: …” z nazw zaznaczonych zabiegów, zębów i powierzchni; domyślnie włączone, wyłącznik w Ustawieniach; kopiowane razem z opisem |
| P40a | podsumowanie także w podglądzie „Cały opis” |
| P40b | wyłącznik podsumowania w Ustawieniach modułu |
| P40c | obsługa wyłącznika podsumowania |
| P30 | audyt NFZ R-ST30DG-WIEK (decyzja Patryka D1=B, 22.11.2026): ST30E/ST30G u pacjenta ≥ 18 lat – ostrzeżenie zamiast błędu; bez wpisanego wieku – przypomnienie (źródło: Zarządzenie 60/2023/DSOZ t.j. od 1.09.2026, 95/2026/DSOZ) |
| P31 | audyt NFZ R-LAKIER-01: lakierowanie 1006 u pacjenta ≥ 18 lat – ostrzeżenie; bez wieku – przypomnienie (źródło: rozporządzenie koszykowe, t.j. Dz.U. 2025 poz. 615) |
| P32 | audyt NFZ R-KIR-DZ (decyzja D4=A): kiretaż ST04 u dziecka – INFORMACJA „wymaga weryfikacji” (komunikat NFZ z 22.07.2026, stan prawny nieustalony) |
| P33 | audyt NFZ R-ZNI-02 (decyzja Patryka 22.11.2026 – ostrzeżenie): znieczulenie wpisane osobno przy ekstrakcji (ST01/ST02) lub kiretażu (ST04) – jest wliczone w pakiet; osobno tylko do wypełnienia, 1105 lub 1206 (źródło: Zarządzenie 60/2023/DSOZ t.j., zał. 1c/1d – lista ST1) |
| P34 | komunikaty NFZ: INFORMACJA (reguły „wymaga weryfikacji”) wyświetlana jako notatka, nie ostrzeżenie (D4=A) |
| P35 | audyt NFZ N1: dane audytu (generator/nfz-dane.js z data/nfz/, scripts/nfz_dane_przegladarka.py) ładowane razem z szablonami – tylko do odczytu na urządzeniu |
| P36 | audyt NFZ N2: silnik reguł z danych audytu (łączenie spoza tabeli „nie sumuje się”, limity jako informacja – D7=B, przełom roku – D6=A, ocena wg daty wizyty) – tylko na urządzeniu (D2=A) |
| P36a | audyt NFZ N2: funkcje silnika reguł (przed nfzIssues) |
| P37 | audyt NFZ N2: rozwijana lista „Zasady NFZ dla wybranych kodów” (treść, poziom, status, źródło) pod komunikatami NFZ |
| P37a | lista zasad NFZ widoczna także bez błędów i ostrzeżeń |
| P37b | lista zasad NFZ na końcu okienka komunikatów |
| P38 | audyt NFZ N5 (D3=A): rozpoznanie ICD-10 wybrane przez lekarza z podpowiedzi pokazywane przy kodzie i w tabeli (domyślnie jak dotąd) |
| P39 | audyt NFZ N5: podpowiedzi ICD-10 z mapowań audytu w karcie każdej procedury (pakiet → procedury kierunkowe; brak podkodu → kod nadrzędny) |
| P40 | audyt NFZ N5: wybór / odznaczenie podpowiedzi ICD-10 |
| P41 | baza stomatologiczna (I1): dane checklist (generator/baza-dane.js z data/, scripts/baza_dane_przegladarka.py) ładowane w Opisach NFZ – tylko do odczytu |
| P42 | baza stomatologiczna (I1): funkcje kontroli kompletności dokumentacji (ostrzeżenie bez blokady – decyzja Patryka 22.11.2026) |
| P42a | kontrola kompletności w kroku 3 (Opis) – przed opisem; treść opisu i wycena bez zmian |

## Opisy prywatne (`prywatne.html`)

| # | Poprawka |
|---|---|
| R1 | bez manifestu i ikon wersji statycznej |
| R2 | czcionki lokalnie zamiast Google Fonts |
| R3 | wspólne style z zasobów chronionych logowaniem |
| R4 | wspolne.js → gabinet-saas.js (konto SaaS, klucz urządzenia, synchronizacja bez treści, pól szablonu, e-ZLA i inicjałów) |
| R5 | katalog procedur z zasobów chronionych logowaniem |
| R6 | historia: wpis z innego urządzenia (z chmury) – komunikat, że treść jest na urządzeniu zapisu (zamiast „usunięta”) |
| R7 | historia: brak treści opisu na tym urządzeniu – czytelny komunikat zamiast „Wczytuję…” bez końca (prompt Patryka 21.11.2026, etap 5: „opisy nie zawsze się wyświetlają”) |
| R7a | odczyt treści: zapamiętanie, że treści nie ma (zamiast ponownego „Wczytuję…”) |
| R7b | „Pokaż opis”: komunikat o braku treści na tym urządzeniu |
| R7c | „Kopiuj opis” bez treści na urządzeniu: konkretny komunikat zamiast „Nie udało się skopiować” |
| R8 | podpowiedzi materiałów w szablonach: lista wbudowana + „Moje materiały” z konta (prompt Patryka 21.11.2026, pkt 1.2); pola: materiał wypełnienia, podkład, materiał w zębodole |
| R8a | pole „Materiał w zębodole” też z podpowiedziami „Moich materiałów” |
| R9 | zalecenia ustne (decyzja Patryka 21.11.2026, pkt 6.5): „Zalecenia przekazano pacjentowi w formie ustnej.” na końcu opisu wizyty – domyślnie tak, do wyłączenia przy wizycie |
| R9a | pole wyboru przy wizycie (obok e-ZLA) |
| R9b | obsługa pola „zalecenia ustne” |
| R10 | szybkie opcje (pkt 6.2–6.4): 3 najczęściej używane wartości z historii jako przyciski (materiały, środek znieczulający); 5 dolegliwości do klikania przy wywiadzie (zachowawcze, endo, diagnostyka); dawka znieczulenia ½ / 1 / 2 amp. (domyślnie 1 amp. = 1,7 ml); zawsze można wpisać własną wartość |
| R10a | funkcje szybkich opcji i podpowiedzi (wspólne dla datalist i przycisków) |
| R10b | obsługa przycisków szybkich opcji |
| R10c | wygląd przycisków szybkich opcji |
| R11 | podsumowanie na początku opisu (decyzja Patryka 21.11.2026, pkt 6.1): „Wykonano: …” z procedur wizyty i zębów; domyślnie włączone, wyłącznik w Ustawieniach |
| R11a | wyłącznik podsumowania w Ustawieniach (obok podpisu) |
| R11b | obsługa wyłącznika podsumowania |
| R12 | bezpiecznik startu (zgłoszenie Patryka 21.11.2026: „czasem zostaje Wczytuję…”, zwłaszcza po przejściu z Opisów NFZ): po 8 s bez gotowości – informacja i „Odśwież”; za pierwszym razem samo odświeżenie (najwyżej raz na minutę) |

## Kalendarz (`kalendarz.html`)

| # | Poprawka |
|---|---|
| K1 | bez ikon i manifestu wersji statycznej |
| K2 | czcionki lokalnie zamiast Google Fonts |
| K3 | wspólne style z zasobów chronionych logowaniem |
| K4 | wspolne.js → gabinet-saas.js (konto SaaS: dokumenty Kalendarza na koncie, gabinety wspólne z całą aplikacją, sumy z opisów z serwera) |
| K5 | identyfikator gabinetu domyślnego: UUID (wspólna tabela gabinetów) zamiast „c1”… |
| K6 | identyfikator nowego gabinetu: UUID zamiast „c…” |
| K7 | notatka dyżuru zapisuje się na koncie – przypomnienie, żeby nie wpisywać danych pacjentów |
| K8 | status zapisu w nagłówku: bez „zaszyfrowane, na tym urządzeniu” (dane Kalendarza są na koncie; stan wysyłki pokazuje pasek aplikacji) |
| K9 | opis „Dane” w Ustawieniach: dane Kalendarza są na koncie Gabinet (nie „tylko w tej przeglądarce”) |
| K10 | „Usuń wszystkie dane” usuwa dyżury, kursy i ustawienia Kalendarza, ale nie gabinety (wspólne z Opisami i Zarobkami – usuwa się je w „Gabinety”) |
| K11 | pytanie przed usunięciem danych Kalendarza: gabinety zostają |
| K12 | zmiany z innego urządzenia (scalone na koncie) od razu w otwartym Kalendarzu – bez nadpisywania pola, które właśnie edytujesz |
| K13 | nazwa modelu rozliczenia: „% po odjęciu kosztów własnych” (decyzja Patryka 21.11.2026; logika bez zmian) |
| K14 | domyślne ustawienia bez założeń o użytkowniku (decyzja Patryka 21.11.2026): pusty start JDG, brak formy opodatkowania i okresów ZUS – wybiera użytkownik (kreator K16) |
| K15 | bez ustawionych podatków i ZUS nie pokazujemy „netto ≈” ani „odłóż” (zamiast wyniku liczonego z cudzych założeń); taxReady() = start JDG + forma + okres ZUS |
| K15a | podsumowanie miesiąca bez ustawień podatków: zaproszenie do kreatora zamiast „JDG nieaktywna (start: )” |
| K15b | pasek miesiąca bez ustawień podatków: zaproszenie do kreatora |
| K15c | Podsumowanie bez ustawień podatków: zaproszenie do kreatora |
| K15d | tydzień: „Netto ≈” tylko przy ustawionych podatkach i ZUS |
| K16 | kreator „Ustaw podatki i ZUS” przy pierwszym otwarciu (3 pytania, bez wartości z góry; można pominąć i wrócić) |
| K16a | akcje kreatora i „Ustaw od nowa” (czyści tylko ustawienia podatków i ZUS – po potwierdzeniu; dyżury, gabinety, koszty i kursy zostają) |
| K17 | przycisk „Ustaw od nowa” w Ustawieniach → Działalność i podatek (z potwierdzeniem) |
| K18 | opis pola startu JDG – ogólny (nie tylko wznowienie) |
| K19 | etat: bieżący rok zamiast stałego 2026 (Ustawienia, pomocnik, pierwsze kroki) |
| K19a | pomocnik etatu zapisuje bieżący rok |
| K19b | pierwsze kroki: „Podatki i ZUS” (kreator) zamiast „Kwota ZUS z eZUS”; etat bieżącego roku i opcjonalny |
| K19c | pierwsze kroki: krok „wiz” otwiera kreator |
| K20 | koszty firmowe: opis ogólny zamiast planu jednej osoby (skala do końca 2026) |
| K21 | „+ Dodaj okres” ZUS przy pustej liście: od startu JDG (albo bieżącego miesiąca), wariant do wyboru |
| K22 | przykład (demo) z własnymi, oznaczonymi wartościami podatków – domyślne są puste |
| K23 | domyślnie zero gabinetów (decyzja Patryka 21.11.2026): wcześniej puste konto dostawało 4 przykładowe gabinety z UUID, które przy pierwszym zapisie ustawień trafiały do tabeli gabinetów konta |
| K23a | pusta lista gabinetów zostaje pusta (bez dopełniania przykładowymi) |
| K23b | przykład (demo) tworzy własne 4 gabinety przykładowe |
| K24 | zachęta „Dodaj pierwszy gabinet” (Gabinety w aplikacji) zamiast „Ustaw dni pracy”, gdy konto nie ma gabinetów |
| K25 | bez gabinetu: nowy dyżur prosi o dodanie gabinetu (zamiast błędu) |
| K25a | bez gabinetu: „Dodaj dyżury” prosi o dodanie gabinetu |
| K25b | bez gabinetu: nowy wzór dni pracy prosi o dodanie gabinetu |
| K25c | bez gabinetu: klik w siatkę tygodnia nie odwołuje się do nieistniejącego gabinetu |
| K39 | wygląd jak reszta aplikacji (prompt Patryka 21.11.2026, pkt 4.1; wzorzec: Opisy NFZ): czcionka IBM Plex, paleta Gabinetu, wyróżnienia (przyciski główne, aktywna zakładka, dziś, podpowiedzi) w kolorze morskim zamiast czarnego, zakładki jako „pigułki”; logika bez zmian; kolory gabinetów bez zmian |
| K40 | strona nie przeskakuje po wejściu do Kalendarza (zgłoszenie Patryka 21.11.2026: „ucina zakładki u góry”): gdy strona jest na samej górze, przerysowanie (np. podpowiedzi po wczytaniu danych) nie przewija jej w dół |
| K40a | utrzymanie miejsca na ekranie tylko, gdy strona była przewinięta |
| K41 | Rozliczenia i Podsumowanie przeniesione do Zarobków (decyzja Patryka 21.11.2026): ten sam kod i obliczenia, otwierane pod /zarobki/rozliczenia i /zarobki/podatki (widok z danych startowych); w menu aktywne „Zarobki” |
| K41a | zakładki: w Kalendarzu bez „Podsumowanie” i „Rozliczenia”; w widoku Zarobków tylko wybrany widok |
| K41b | w widoku Zarobków zamiast zakładek Kalendarza – nawigacja Zarobki · Rozliczenia · Podatki i ZUS |
| K41c | start: w widoku Zarobków właściwa zakładka; stare adresy #podsumowanie / #rozliczenia prowadzą do Zarobków |
| K41d | przejścia do zakładek z innych miejsc (podpowiedzi, terminy): Podsumowanie/Rozliczenia → Zarobki; z widoku Zarobków do pozostałych → Kalendarz |
| K41e | Rozliczenia: kolumna „Zarobek lekarza (z dyżurów)” – ta sama nazwa i kwota co w Zarobkach |
