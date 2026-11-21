# Zlecenia protetyczne – specyfikacja (etap E0)

Stan: 21.11.2026 · prompt Patryka „Inteligentne zlecenia protetyczne dla technika dentystycznego” · dokument roboczy (do akceptacji Patryka).

## 1. Decyzje Patryka (21.11.2026)

| Sprawa | Decyzja |
|---|---|
| Dane zlecenia | **na urządzeniu + chmura szyfrowana kluczem użytkownika** (serwer widzi tylko zaszyfrowany blok; zasada nr 1 `CLAUDE.md` bez zmian) |
| Pacjent | **inicjały + numer przypadku** (na urządzeniu); imię i nazwisko opcjonalnie tylko do wydruku (niezapisywane) |
| Komunikacja z technikiem | **poza aplikacją + statusy** (wysłane / przyjęte / do uzupełnienia z listą braków / gotowe) i notatki z rozmów; portal technika – osobny etap po analizie prawnej |
| Załączniki | **zdjęcia na urządzeniu, włączane do wydruku/PDF; skany (STL/PLY/OBJ) wysyłane osobno** – w zleceniu lista plików |
| „TWD” | = zaburzenia czynnościowe stawów skroniowo-żuchwowych (ang. TMD) – potwierdzone przez Patryka |

## 2. Źródła i ich ograniczenia

| Źródło | Stan | Co wnosi |
|---|---|---|
| ACP, *Position statement: dental laboratory and dentist relationship* (prosthodontics.org) | **niepobrane (HTTP 403)** – nie powołujemy się na treść | – |
| deltalabs.pl, *How to prepare a complete laboratory prescription* (27.03.2026; laboratorium – punkt widzenia jednej pracowni) | pobrane | 8 elementów obowiązkowych; najczęstsze braki (kolor kikuta, zdjęcia przy estetyce, przykręcana/cementowana, typ połączenia); niekompletne zlecenie = opóźnienie / ryzyko |
| isdllab.com, *Digital impression: dental lab checklist* (19.07.2026) | pobrane (krótkie) | identyfikator przypadku wspólny dla zlecenia, zdjęć i plików; rejestracja zwarcia; system/platforma/scanbody; akceptacja projektu przed produkcją; wersjonowanie plików |
| Ogólna wiedza protetyczna (bez źródła w tym dokumencie) | – | pozycje oznaczone **[W]** – **do weryfikacji przez Patryka** |

## 3. Pola wspólne (każde zlecenie)

W = wymagane (bez nich zlecenie niekompletne – ostrzeżenie, ale zapis możliwy), Z = zalecane, O = opcjonalne.

| Pole | Status | Źródło |
|---|---|---|
| Numer przypadku (automatyczny, edytowalny) + inicjały pacjenta | W | deltalabs, ISDL |
| Rodzaj pracy (katalog, rozszerzalny, „inna – wpisz”) | W | deltalabs |
| Zęby (FDI 11–48, 51–85) ze schematu | W | deltalabs |
| Materiał (lista zależna od rodzaju pracy + własne) | W | deltalabs |
| Termin odbioru / przymiarki | W | deltalabs |
| Lekarz i kontakt (z konta) | W | deltalabs |
| Laboratorium / technik (lista własna) | Z | [W] |
| Priorytet (zwykły / pilny) | O | prompt |
| Antagoniści i zęby sąsiednie (wycisk/skan dołączony?) | W | deltalabs |
| Etapy (przymiarka konstrukcji, przymiarka zębów, akceptacja projektu przed produkcją) | Z | ISDL |
| Pliki wysłane osobno (skany, rejestracja zwarcia) – nazwy/wersje | Z | ISDL |
| Uwagi ogólne / instrukcje szczególne | O | prompt |

## 4. Kolor

| Pole | Status | Uwagi |
|---|---|---|
| Skala (Vita Classic / Vita 3D-Master / Bleach / inna) | W przy pracach estetycznych | „A2” bez skali jest niejednoznaczne (deltalabs) |
| Kolor główny | W przy pracach estetycznych | |
| Kolor kikuta / podłoża | W przy zębach martwych i przebarwionych, Z pozostałe | deltalabs: „krytyczny” przy zębach martwych |
| Kolor szyjkowy / korony / brzegu siecznego (mapa koloru) | Z (przednie) | [W] |
| Przezierność, opalescencja, fluorescencja, charakteryzacja, przebarwienia, pęknięcia | O | [W] |
| Kolor dziąsła | Z przy pracach pełnołukowych i protezach | [W] |
| Zdjęcia z kolornikiem | Z (przednie estetyczne – praktycznie standard wg deltalabs) | |

## 5. Zgryz (moduł rozwijany)

Klasa Angle'a (I / II/1 / II/2 / III), overjet i overbite (mm), zgryz głęboki / otwarty / krzyżowy / przewieszony, linia pośrodkowa (zgodna / przesunięta – mm, strona), płaszczyzna zgryzowa, VDO (zachować / zmienić o … mm), rejestracja zwarcia (zgryz w MIC / CR, rejestrat, skan bocznego zwarcia), kontakty zwarciowe (na schemacie), prowadzenie (kłowe / grupowe / przednie), bruksizm i parafunkcje (tak/nie + szyna), zaburzenia SSSŻ (TMD) – uwagi. Wszystko Z/O, z wyjątkiem: **rejestracja zwarcia – W przy mostach i pracach pełnołukowych** [W].

## 6. Katalog rodzajów prac (rozszerzalny) i pola zależne

| Grupa | Rodzaje | Materiały (podpowiedzi) | Dodatkowe pola (W/Z) |
|---|---|---|---|
| A Korony | pełnoceramiczna, cyrkon monolityczny, cyrkon warstwowy, metaloceramika, e.max, tymczasowa, na implancie | cyrkon, e.max, ceramika, metaloceramika (CoCr), PMMA, kompozyt | kolor + kikut (W), granica preparacji/stopień (Z), kontakty styczne (Z) |
| B Mosty | klasyczny, adhezyjny, na implantach, pełnołukowy, tymczasowy | j.w. | **filary i przęsła na schemacie (W)**, kształt przęsła (siodłowe/owalne/higieniczne) (Z), łączniki (Z) |
| C Implantoprotetyka | korona/most na implancie, łącznik indywidualny, Ti-base, przykręcana/cementowana | cyrkon, tytan, CoCr, PMMA | **producent i system (W)**, platforma, połączenie (W wg deltalabs), scanbody (Z), MUA (Z), średnica/długość (O), kąt (O), profil wyłaniania (Z), otwór śruby (Z), tkanki miękkie (O) |
| D Pełnołukowe | All-on-4, All-on-6, All-on-X, tymczasowe, ostateczne, hybrydowe | PMMA, kompozyt, tytan/CoCr + akryl/kompozyt, cyrkon | liczba i pozycje implantów (W), system/MUA (W), rejestracja zwarcia + VDO (W), linia pośrodkowa, płaszczyzna zgryzowa, podparcie wargi, ekspozycja zębów, fonetyka, kształt i ustawienie, kolor zębów i dziąsła (Z), materiał konstrukcji (W), etap: tymczasowa / ostateczna (W), oczekiwane przymiarki (Z) |
| E Ruchome | całkowita, częściowa, szkieletowa, akrylowa, elastyczna, naprawa, podścielenie | akryl, CoCr, nylon (elastyczna) | brakujące zęby i klamry na schemacie (W), etap (łyżka indywidualna / wzorniki / ustawienie / gotowa), kolor zębów (W) i dziąsła (Z), rodzaj/nr zębów sztucznych (O) |
| F Pozostałe | licówki, inlay, onlay, overlay, endokorona, szyna relaksacyjna/ochronna, inna | e.max, kompozyt, cyrkon, PMMA, akryl (szyny) | kolor (W przy estetycznych), grubość szyny (Z), łuk (W przy szynach) |

## 7. Kontrola kompletności (przykłady z promptu)

Korona bez materiału · praca estetyczna bez koloru (lub bez skali) · most bez przęseł · implant bez systemu · All-on-X bez komponentów → **ostrzeżenie**, zapis i wydruk możliwe (z listą braków na wydruku). Status „do uzupełnienia” z listą braków (zgłoszonych przez technika telefonicznie/mailowo – wpisuje lekarz).

## 8. Do weryfikacji przez Patryka

Wszystkie pozycje **[W]** (pochodzą z ogólnej wiedzy, nie ze źródła powyżej) – szczególnie: listy materiałów dla rodzajów prac, pola All-on-X, etapy protez ruchomych.
