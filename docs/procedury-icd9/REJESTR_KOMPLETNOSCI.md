# Rejestr kompletności – procedury ICD-9 i badania

> Plik generowany: `python3 scripts/buduj_docs_bazy.py` z danych w `data/`. Nie edytuj ręcznie – popraw JSON.

Wersja danych: 2026.11.22-1.

## Podsumowanie

| Status | Procedury |
|---|---|
| draft | 144 |
| not_started | 60 |
| requires_expert_review | 62 |
| **razem** | **266** |

Badania: 17 (BAD-WYWIAD: draft, BAD-ZEWNATRZUSTNE: draft, BAD-WEWNATRZUSTNE: draft, BAD-BLONA: draft, BAD-UZEBIENIE: draft, BAD-PRZYZEBIE: draft, BAD-HIGIENA: draft, BAD-ZGRYZ: draft, BAD-SSZ: draft, BAD-ZYWOTNOSC: draft, BAD-RTG: draft, BAD-PO-URAZIE: draft, BAD-DZIECKO: draft, BAD-STOMATOLOGICZNE: draft, BAD-KONTROLNE: draft, BAD-PRZED-LECZENIEM: draft, BAD-PO-LECZENIU: draft).

`draft` = opracowane, niezweryfikowane przez Patryka; `verified` – wyłącznie po weryfikacji (pole zweryfikowal).

## Wszystkie kody

| Kod | Nazwa (ICD-9 PL 5.91) | Kategoria | Status | Uwagi |
|---|---|---|---|---|
| 23.0101 | Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej | badanie i porada | draft |  |
| 23.0102 | Badanie lekarskie kontrolne | badanie i porada | draft |  |
| 23.0103 | Porada lekarska | badanie i porada | draft |  |
| 23.0104 | Wydanie orzeczenia lekarskiego | badanie i porada | draft |  |
| 23.0105 | Konsultacja specjalistyczna | badanie i porada | draft |  |
| 23.0106 | Wydanie krótkiego zaświadczenia lub świadectwa | badanie i porada | draft |  |
| 23.0107 | Badanie lekarskie stomatologiczne i kontrolne po urazie zęba | badanie i porada | draft |  |
| 23.02 | Badanie żywotności zęba | diagnostyka | draft |  |
| 23.0301 | Rentgenodiagnostyka do 2 zdjęć wewnątrzustnych | radiologia | draft |  |
| 23.0302 | Rentgenodiagnostyka do 5 zdjęć wewnątrzustnych | radiologia | draft |  |
| 23.0303 | Rentgenodiagnostyka do 8 zdjęć wewnątrzustnych | radiologia | draft |  |
| 23.0304 | Rentgenodiagnostyka - zdjęcie pantomograficzne z opisem | radiologia | draft |  |
| 23.0401 | Znieczulenie miejscowe powierzchniowe | znieczulenie | draft |  |
| 23.0402 | Znieczulenie miejscowe nasiękowe | znieczulenie | draft |  |
| 23.0403 | Znieczulenie przewodowe wewnątrzustne | znieczulenie | draft |  |
| 23.0404 | Znieczulenie przewodowe zewnątrzustne | znieczulenie | requires_expert_review | Technika specjalistyczna – do weryfikacji eksperckiej. |
| 23.05 | Postępowanie w nagłych przypadkach | pomoc doraźna | draft |  |
| 23.06 | Wizyta adaptacyjna -dotyczy pierwszych wizyt małych dzieci | dziecko | draft |  |
| 23.07 | Pilne zabiegi poza godzinami pracy w dni świąteczne lub w domu pacjenta | pomoc doraźna | requires_expert_review | Zasady organizacyjne i rozliczeniowe (pomoc doraźna – zał. nieodczytany w audycie) do weryfikacji. |
| 23.08 | Instruktaż higieny jamy ustnej | profilaktyka | draft |  |
| 23.0901 | Balneoterapia lub hydroterapia | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0902 | Naświetlanie Sollux | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0903 | Jonoforeza nadziąsłowa | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0904 | Jonoforeza lub elektrosterylizacja kanału korzeniowego | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0905 | Diadynamik 1/2 łuku zębowego | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0906 | Hydroterapia | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.0907 | Laseroterapia biostymulacyjna | fizykoterapia | requires_expert_review | Fizykoterapia w stomatologii – ograniczone współczesne dowody skuteczności; karta do weryfikacji eksperckiej. |
| 23.1001 | Indywidualna fluoryzacja metodą kontaktową - za każdy zabieg | profilaktyka | draft |  |
| 23.1002 | Fluoryzacja kontaktowa zbiorowa, 1 zabieg u każdego dziecka | profilaktyka | draft |  |
| 23.1003 | Zabezpieczenie profilaktyczne bruzd lakiem szczelinowym - za każdy ząb | profilaktyka | draft |  |
| 23.1004 | Zabezpieczanie profilaktyczne bruzd innymi materiałami | profilaktyka | draft |  |
| 23.1006 | Lakierowanie zębów 1/4 łuku zębowego | profilaktyka | draft |  |
| 23.1007 | Leczenie nadwrażliwości zębów w obrębie 1/4 łuku zębowego | profilaktyka | draft |  |
| 23.1008 | Impregnacja zębiny | profilaktyka | requires_expert_review | Preparat i wskazania do weryfikacji (np. fluorek diaminy srebra – przebarwienia, zgoda). |
| 23.1009 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. miesiącu życia | profilaktyka | draft |  |
| 23.1010 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 9. miesiącu życia | profilaktyka | draft |  |
| 23.1011 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 12. miesiącu życia | profilaktyka | draft |  |
| 23.1012 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 2. roku życia | profilaktyka | draft |  |
| 23.1013 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 4. roku życia | profilaktyka | draft |  |
| 23.1014 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 5. roku życia | profilaktyka | draft |  |
| 23.1015 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. roku życia | profilaktyka | draft |  |
| 23.1016 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 7. roku życia | profilaktyka | draft |  |
| 23.1017 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 10. roku życia | profilaktyka | draft |  |
| 23.1018 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 12. roku życia | profilaktyka | draft |  |
| 23.1019 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 13. roku życia | profilaktyka | draft |  |
| 23.1020 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 16. roku życia | profilaktyka | draft |  |
| 23.1021 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 19. roku życia | profilaktyka | draft |  |
| 23.1022 | Profilaktyczne świadczenie stomatologiczne zapobiegające wadom zgryzu | profilaktyka | draft |  |
| 23.1023 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 3. roku życia | profilaktyka | draft |  |
| 23.1101 | Leczenie próchnicy powierzchniowej - za każdy ząb | leczenie próchnicy | draft |  |
| 23.1102 | Całkowite opracowanie ubytku próchnicowego z założeniem podkładu | leczenie próchnicy | draft |  |
| 23.1103 | Całkowite opracowanie rozległego ubytku próchnicowego z założeniem podwójnego podkładu | leczenie próchnicy | draft |  |
| 23.1104 | Postępowanie przy próchnicy głębokiej - pośrednie pokrycie miazgi | leczenie próchnicy | draft |  |
| 23.1105 | Postępowanie przy obnażeniu i skaleczeniu miazgi - bezpośrednie pokrycie miazgi | leczenie próchnicy | draft |  |
| 23.1106 | Opatrunek leczniczy w zębie stałym | leczenie próchnicy | draft |  |
| 23.1107 | Opatrunek leczniczy w zębie mlecznym | leczenie próchnicy | draft |  |
| 23.1108 | Wypełnienie ubytku korony zęba mlecznego | leczenie próchnicy | draft |  |
| 23.1109 | Wypełnienie ubytku korony zęba na 1 powierzchni | leczenie próchnicy | requires_expert_review | Kod obecny w ICD-9 PL 5.91 obok 23.1502–23.1506 – Patryk: czy jest jeszcze używany (raport, kwestia 6). |
| 23.1110 | Wypełnienie ubytku korony zęba na 2 powierzchniach | leczenie próchnicy | requires_expert_review | Kod obecny w ICD-9 PL 5.91 obok 23.1502–23.1506 – Patryk: czy jest jeszcze używany (raport, kwestia 6). |
| 23.1111 | Wypełnienie ubytku korony zęba na 3 powierzchniach | leczenie próchnicy | requires_expert_review | Kod obecny w ICD-9 PL 5.91 obok 23.1502–23.1506 – Patryk: czy jest jeszcze używany (raport, kwestia 6). |
| 23.1112 | Wypełnienie ubytku korony zęba na więcej niż 3 powierzchniach | leczenie próchnicy | requires_expert_review | Kod obecny w ICD-9 PL 5.91 obok 23.1502–23.1506 – Patryk: czy jest jeszcze używany (raport, kwestia 6). |
| 23.1201 | Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem | endodoncja – leczenie miazgi | draft |  |
| 23.1202 | Dewitalizacja miazgi zęba z zaopatrzeniem ubytku opatrunkiem | endodoncja – leczenie miazgi | requires_expert_review | Metoda z użyciem preparatu dewitalizującego – nadal w wykazie świadczeń gwarantowanych, ale współczesne wytyczne (ESE) preferują leczenie w znieczuleniu; do oceny Patryka, jak ją przedstawiać w aplikacji. |
| 23.1203 | Amputacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem | endodoncja – leczenie miazgi | draft |  |
| 23.1204 | Amputacja przyżyciowa miazgi | endodoncja – leczenie miazgi | draft |  |
| 23.1205 | Ekstyrpacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem | endodoncja – leczenie miazgi | draft |  |
| 23.1206 | Ekstyrpacja przyżyciowa miazgi | endodoncja – leczenie miazgi | draft |  |
| 23.1207 | Amputacja zdewitalizowanej miazgi zęba | endodoncja – leczenie miazgi | requires_expert_review | Metoda z użyciem preparatu dewitalizującego – nadal w wykazie świadczeń gwarantowanych, ale współczesne wytyczne (ESE) preferują leczenie w znieczuleniu; do oceny Patryka, jak ją przedstawiać w aplikacji. |
| 23.1208 | Ekstyrpacja zdewitalizowanej miazgi zęba z nieuformowanym korzeniem | endodoncja – leczenie miazgi | requires_expert_review | Metoda z użyciem preparatu dewitalizującego – nadal w wykazie świadczeń gwarantowanych, ale współczesne wytyczne (ESE) preferują leczenie w znieczuleniu; do oceny Patryka, jak ją przedstawiać w aplikacji. |
| 23.1209 | Ekstyrpacja zdewitalizowanej miazgi zęba | endodoncja – leczenie miazgi | requires_expert_review | Metoda z użyciem preparatu dewitalizującego – nadal w wykazie świadczeń gwarantowanych, ale współczesne wytyczne (ESE) preferują leczenie w znieczuleniu; do oceny Patryka, jak ją przedstawiać w aplikacji. |
| 23.1210 | Amputacja zdewitalizowanej miazgi zęba mlecznego | endodoncja – leczenie miazgi | requires_expert_review | Metoda z użyciem preparatu dewitalizującego – nadal w wykazie świadczeń gwarantowanych, ale współczesne wytyczne (ESE) preferują leczenie w znieczuleniu; do oceny Patryka, jak ją przedstawiać w aplikacji. |
| 23.1301 | Całkowite opracowanie i dezynfekcja kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.1302 | Leczenie zgorzeli | endodoncja – leczenie kanałowe | draft |  |
| 23.1303 | Leczenie zgorzeli całkowitej niepowikłanej zęba z nieuformowanym korzeniem | endodoncja – leczenie kanałowe | draft |  |
| 23.1304 | Dodatkowe fizykochemiczne metody udrażniania i opracowywania kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.1305 | Ponowne udrożnienie wypełnionego kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.1306 | Czasowe wypełnienie kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.1307 | Wypełnienie kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.1308 | Leczenie endodontyczne z wypełnieniem 2 kanałów | endodoncja – leczenie kanałowe | draft |  |
| 23.1309 | Leczenie endodontyczne z wypełnieniem 3 kanałów | endodoncja – leczenie kanałowe | draft |  |
| 23.1310 | Leczenie endodontyczne metodą amputacyjno-ekstyrpacyjną | endodoncja – leczenie kanałowe | requires_expert_review | Metoda historyczna (brak w wykazie świadczeń gwarantowanych wg audytu) – do oceny Patryka. |
| 23.1311 | Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi | endodoncja – leczenie kanałowe | draft |  |
| 23.1312 | Leczenie endodontyczne zęba z wypełnieniem 2 kanałów ze zgorzelą miazgi | endodoncja – leczenie kanałowe | draft |  |
| 23.1313 | Leczenie endodontyczne zęba z wypełnieniem 3 kanałów ze zgorzelą miazgi | endodoncja – leczenie kanałowe | draft |  |
| 23.1314 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA | endodoncja – leczenie kanałowe | draft |  |
| 23.13141 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 1 kanału | endodoncja – leczenie kanałowe | draft |  |
| 23.13142 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 2 kanałów | endodoncja – leczenie kanałowe | draft |  |
| 23.13143 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 3 kanałów | endodoncja – leczenie kanałowe | draft |  |
| 23.13149 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA - inne | endodoncja – leczenie kanałowe | draft |  |
| 23.14 | Szczególne trudności w preparowaniu/ wypełnianiu zębów - usunięcie przerośniętej brodawki międzyzębowej, zatamowanie krwawienia z brodawki, separowanie zębów itp. | stomatologia zachowawcza | draft |  |
| 23.1501 | Odbudowa zniszczonego, złamanego kąta w zębach siecznych | odbudowa i estetyka | draft |  |
| 23.1502 | Całkowite opracowanie i odbudowa ubytku zęba na 1 powierzchni | odbudowa i estetyka | draft |  |
| 23.1503 | Całkowite opracowanie i odbudowa ubytku na 2 powierzchniach | odbudowa i estetyka | draft |  |
| 23.1504 | Całkowite opracowanie i odbudowa rozległego ubytku na 2 powierzchniach | odbudowa i estetyka | draft |  |
| 23.1505 | Całkowite opracowanie i odbudowa rozległego ubytku na 3 powierzchniach | odbudowa i estetyka | draft |  |
| 23.1506 | Całkowite opracowanie i odbudowa rozległego ubytku na więcej niż 3 powierzchniach | odbudowa i estetyka | draft |  |
| 23.1507 | Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych | odbudowa i estetyka | draft |  |
| 23.1508 | Kosmetyczne pokrycie niedorozwoju szkliwa | odbudowa i estetyka | draft |  |
| 23.1509 | Kosmetyczna korekta przebarwienia zębiny w zębach przednich | odbudowa i estetyka | draft |  |
| 23.1510 | Likwidacja diastemy | odbudowa i estetyka | draft |  |
| 23.1511 | Wybielanie zęba metodą wewnętrzną | odbudowa i estetyka | draft |  |
| 23.1512 | Wybielanie grupy zębów metodą zewnętrzną | odbudowa i estetyka | draft |  |
| 23.1601 | Usunięcie złogów nazębnych z 1/2 łuku zębowego | periodontologia i błona śluzowa | not_started | Kod nadrzędny – od 01.09.2026 do rozliczenia wykazuje się podkody (R-KOD-01): 23.16011 / 23.16012; karty w podkodach. |
| 23.16011 | Usunięcie złogów nazębnych miękkich z 1/2 łuku zębowego | periodontologia i błona śluzowa | draft |  |
| 23.16012 | Usunięcie złogów nazębnych twardych z 1/2 łuku zębowego | periodontologia i błona śluzowa | draft |  |
| 23.1602 | Usunięcie złogów nazębnych ze wszystkich zębów | periodontologia i błona śluzowa | not_started | Kod nadrzędny – od 01.09.2026 do rozliczenia wykazuje się podkody (R-KOD-01): 23.16021 / 23.16022; karty w podkodach. |
| 23.16021 | Usunięcie złogów nazębnych miękkich ze wszystkich zębów | periodontologia i błona śluzowa | draft |  |
| 23.16022 | Usunięcie złogów nazębnych twardych ze wszystkich zębów | periodontologia i błona śluzowa | draft |  |
| 23.1603 | Polerowanie zębów | periodontologia i błona śluzowa | draft |  |
| 23.1604 | Płukanie kieszonki dziąsłowej i aplikacja leku | periodontologia i błona śluzowa | draft |  |
| 23.1605 | Leczenie zmian na błonie śluzowej jamy ustnej | periodontologia i błona śluzowa | draft |  |
| 23.1606 | Korekta zgryzu | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1607 | Kiretaż zwykły w obrębie 1/4 uzębienia | periodontologia i błona śluzowa | draft |  |
| 23.1608 | Kiretaż otwarty w obrębie 1/4 uzębienia | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1609 | Gingwoplastyka | periodontologia i błona śluzowa | draft |  |
| 23.1610 | Gingwoosteoplastyka | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1611 | Podcięcie wędzidełka, wargi, języka, policzka | periodontologia i błona śluzowa | draft |  |
| 23.1612 | Plastyka wędzidełka ,wargi ,policzka | periodontologia i błona śluzowa | draft |  |
| 23.1613 | Plastyka przedsionka jamy ustnej met. Clarka, Kazanjana | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1614 | Plastyka przedsionka jamy ustnej met. Nabersa | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1615 | Unieruchomienie zębów ligaturą drucianą | periodontologia i błona śluzowa | draft |  |
| 23.1616 | Unieruchomienie zębów materiałem złożonym (kompozytowym) | periodontologia i błona śluzowa | draft |  |
| 23.1617 | Unieruchomienie zębów szyną z materiału złożonego z dodatkowymi wzmocnieniami | periodontologia i błona śluzowa | draft |  |
| 23.1618 | Zabieg wszczepiania hydroksyapatytu, bioglassu lub tp. | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1619 | Zabieg pokrycia obnażonych korzeni zębów metodą bocznie przesuniętego płata | periodontologia i błona śluzowa | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1620 | Założenie opatrunku parodontologicznego | periodontologia i błona śluzowa | draft |  |
| 23.17 | Chirurgiczne usunięcie zęba | chirurgia – ekstrakcje | not_started | Kod nadrzędny używany w składzie pakietów NFZ – karty w podkodach: 23.1701–23.1708. |
| 23.1701 | Usunięcie zęba jednokorzeniowego | chirurgia – ekstrakcje | draft |  |
| 23.1702 | Usunięcie zęba wielokorzeniowego | chirurgia – ekstrakcje | draft |  |
| 23.1703 | Usunięcie głęboko złamanego zęba poprzez dłutowanie wewnątrzzębodołowe przy zastosowaniu wierteł, dźwigni | chirurgia – ekstrakcje | draft |  |
| 23.1704 | Usunięcie zęba przez dłutowanie zewnątrzzębodołowe z wytworzeniem płata śluzówkowo-okostnowego | chirurgia – ekstrakcje | draft |  |
| 23.1705 | Operacyjne usunięcie zęba zatrzymanego | chirurgia – ekstrakcje | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1706 | Operacyjne odsłonięcie zatrzymanego zęba z założeniem pętli drucianej dla celów ortodontycznych | chirurgia – ekstrakcje | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1707 | Operacyjne usunięcie zawiązków zębów ze wskazań ortodontycznych | chirurgia – ekstrakcje | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1708 | Usunięcie zębów w znieczuleniu ogólnym u pacjentów z niedorozwojem umysłowym | chirurgia – ekstrakcje | not_started | Pominięte decyzją Patryka (22.11.2026): usuwanie zębów w znieczuleniu ogólnym – warunki szpitalne/anestezjologiczne. |
| 23.1801 | Zamknięcie zatoki otwartej w przebiegu chirurgicznego usuwania zęba | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1802 | Resekcja wierzchołka korzenia zęba przedniego | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1803 | Resekcja wierzchołka korzenia zęba bocznego | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1804 | Resekcja wierzchołka korzenia zęba każdego następnego zęba podczas tego samego zabiegu i dotyczy zębów | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1805 | Hemisekcja zęba | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1806 | Reimplantacja zęba | chirurgia stomatologiczna | draft |  |
| 23.1807 | Wyłuszczenie torbieli zębopochodnej | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1808 | Wyłuszczenie kamienia z przewodu ślinianki | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1809 | Chirurgiczne zaopatrzenie małej rany obejmującej do 3 zębodołów włącznie ze szwem | chirurgia stomatologiczna | draft |  |
| 23.1810 | Chirurgiczne zaopatrzenie małej rany obejmującej do 2-3 zębodołów włącznie z opracowaniem i szwami | chirurgia stomatologiczna | draft |  |
| 23.1811 | Chirurgiczne zaopatrzenie dużej rany w obrębie połowy szczęki włącznie ze szwami | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1812 | Chirurgiczne zaopatrzenie dużej, albo znacznie zanieczyszczonej rany w obrębie połowy szczęki włącznie z opracowaniem i szwami | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1813 | Zatamowanie krwawienia w obrębie jamy ustnej - nie zaliczane w bezpośrednim połączeniu z zabiegiem chirurgicznym, chyba że zajmuje niewspółmiernie dużo czasu | chirurgia stomatologiczna | draft |  |
| 23.1814 | Zatamowanie masywnego krwawienia w obrębie jamy ustnej przez podwiązanie, pokłucie naczyń bądź zatkanie kością | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1815 | Założenie opatrunku chirurgicznego | chirurgia stomatologiczna | draft |  |
| 23.1816 | Ograniczone, miejscowe wycięcie wargi, języka | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1817 | Krioterapia niewielkich zmian w obrębie tkanek miękkich jamy ustnej | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1819 | Ograniczone wycięcie, zniszczenie zmiany podniebienia twardego | chirurgia stomatologiczna | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1901 | Wycięcie małego guzka lub zmiany guzopodobnej, włókniaka | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1902 | Wycięcie przerostu błony śluzowej (guzy łagodne, zmiany guzopodobnej, nadziąślaki) w obrębie połowy szczęki | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1903 | Plastyka wyrostka zębodołowego w obrębie połowy szczęki | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1904 | Plastyka wyrostka zębodołowego szczęki lub części zębodołowej żuchwy z użyciem przeszczepu lub wszczepu | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1905 | Plastyka guza szczęki | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.1906 | Plastyka połączenia lub przetoki ustno-zatokowej - jako samodzielne postępowanie lub jako następstwo ekstrakcji | chirurgia – wycięcia i plastyki | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.2001 | Nacięcie powierzchniowo, podśluzówkowo lub podskórnie leżącego ropnia włącznie z drenażem i opatrunkiem | chirurgia – zakażenia | draft |  |
| 23.2002 | Nacięcie z dojścia wewnątrz lub zewnątrzustnego głęboko leżącego ropnia włącznie z drenażem i opatrunkiem | chirurgia – zakażenia | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.2003 | Nacięcie ropowicy | chirurgia – zakażenia | not_started | Pominięte decyzją Patryka (22.11.2026): nacięcie ropowicy – chirurgia szczękowo-twarzowa (szpital). |
| 23.2101 | Repozycja i unieruchomienie zwichniętego zęba lub grupy zębów | urazy zębów | draft |  |
| 23.2102 | Repozycja i unieruchomienie złamanego fragmentu wyrostka zębodołowego z zębem lub zębami | urazy zębów | requires_expert_review | Zabieg specjalistyczny – treść karty do weryfikacji przez chirurga stomatologa / periodontologa. |
| 23.2103 | Repozycja i unieruchomienie pośredniego, trudnego do repozycji lub wklinowanego fragmentu złamanego wyrostka zębodołowego | urazy zębów | not_started | Pominięte decyzją Patryka (22.11.2026): repozycja trudnego, wklinowanego fragmentu złamania – chirurgia szczękowo-twarzowa. |
| 23.2201 | Repozycja i unieruchomienie pojedynczego złamania żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2202 | Repozycja i unieruchomienie wielokrotnego, z odłamami pośrednimi złamania żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2203 | Repozycja i unieruchomienie poprzecznego lub strzałkowego złamania szczęki | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2204 | Repozycja i unieruchomienie złamania szczęki z przemieszczaniem odłamów ze złamaniami innych kości twarzy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2205 | Tymczasowe zaopatrzenie złamanej szczęki lub szczęk | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2206 | Założenie szyny drucianej (nazębnej) przy zwichnięciach, reimplantacjach lub transplantacjach zębów, również założenie szyny przy zapaleniu kości, operacjachplastycznych lub resekcjach oraz szynowanie nieuszkodzonej, przeciwstawnej szczęki lub żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2207 | Założenie szyny z pelotą lub płytą nagryzową przy złamaniach z przemieszczeniem szczęki lub dna oczodołu lub wyrostka kłykciowego żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2208 | Badanie kontrolne w trakcie unieruchomienia złamanych szczęk | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2209 | Zdjęcie jednej szyny przy wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2210 | Repozycja i unieruchomienie zwichnięcia żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2211 | Repozycja i unieruchomienie zastarzałego zwichnięcia żuchwy | chirurgia szczękowo-twarzowa – złamania | not_started | Pominięte decyzją Patryka (22.11.2026): złamania szczęk – chirurgia szczękowo-twarzowa – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2301 | Opracowanie na piśmie, na zlecenie lub życzenie, planu leczenia ortodontycznego, włącznie z oceną modeli i kosztów | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2302 | Wycisk jednej szczęki dla diagnozy, planowania i kontroli | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2303 | Postępowanie przygotowujące do wykonania aparatu, wyciski , ustalenie zwarcia | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2304 | Fotografia (profilu i en face) z oceną (każdego zdjęcia) | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2305 | Zastosowanie dodatkowych metod diagnostycznych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2306 | Analiza telerentgenogramu | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2307 | Wykonanie zgryzu konstrukcyjnego | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2308 | Korekcyjne szlifowanie zębów | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2309 | Środki do usunięcia szkodliwych przyzwyczajeń i dysfunkcji, również porady i pouczenia, jeżeli są związane z praktycznymi wskazaniami lub ćwiczeniami (każda wizyta) | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2310 | Utrzymywacz przestrzeni jako samodzielne postępowanie | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2312 | Środki do wprowadzenia pojedynczego przemieszczonego zęba do łuku, po chirurgicznym jego odsłonięciu | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2401 | Leczenie aparatem ortodontycznym ruchomym, jednoszczękowym | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2402 | Leczenie aparatem ortodontycznym ruchomym, dwuszczękowym nieelastycznym | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2403 | Leczenie wady zgryzu aparatem ruchomym ponadstandardowym | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2404 | Oddanie nowego aparatu ruchomego połączone z instruktażem właściwego postępowania | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2405 | Kontrola przebiegu leczenia bez aparatu | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2406 | Kontrola przebiegu leczenia z aparatem ruchomym | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2501 | Naprawa aparatu bez wycisku | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2502 | Naprawa aparatu z wyciskiem | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2503 | Rekonstrukcja aparatu ruchomego przy pacjencie w niewielkim zakresie | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2504 | Rekonstrukcja aparatu ruchomego obejmującego całą górną lub dolną część aparatu | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2601 | Środki dla przebudowy szczęki, łącznie z retencją w przypadkach prostych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2602 | Środki dla przebudowy szczęki, łącznie z retencją w przypadkach średniotrudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2603 | Środki dla przebudowy szczęki, łącznie z retencją w przypadkach trudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2604 | Środki dla przebudowy szczęki, łącznie z retencją w przypadkach bardzo trudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2605 | Środki dla ustawienia żuchwy w prawidłowym zgryzie w kierunku strzałkowym i bocznym, włącznie z retencją w przypadkach prostych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2606 | Środki dla ustawienia żuchwy w prawidłowym zgryzie w kierunku strzałkowym i bocznym, włącznie z retencją w przypadkach średniotrudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2607 | Środki dla ustawienia żuchwy w prawidłowym zgryzie w kierunku strzałkowym i bocznym, włącznie z retencją w przypadkach trudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2608 | Środki dla ustawienia żuchwy w prawidłowym zgryzie w kierunku strzałkowym i bocznym, włącznie z retencją w przypadkach bardzo trudnych | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2609 | Osadzenie zamka ortodontycznego na zębie | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2610 | Kontrola leczenia aparatem stałym | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2611 | Proteza dziecięca częściowa | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2612 | Proteza dziecięca całkowita | ortodoncja | not_started | Pominięte decyzją Patryka (22.11.2026): ortodoncja – poza zakresem gabinetu ogólnostomatologicznego. |
| 23.2701 | Opracowanie na piśmie na zlecenie lub życzenie planu leczenia i kosztów zaopatrzenia protetycznego włącznie z oceną modeli | protetyka | draft |  |
| 23.2702 | Wycisk szczęki dla celów wykonania modelu sytuacyjnego, również wycisk częściowy lub wycisk zgryzowy dla celów diagnostycznych lub planowania | protetyka | draft |  |
| 23.2703 | Zabiegi przygotowujące (pobieranie wycisków, proste ustalenie zgryzu lub tp. dla wykonania modelu obu szczęk celem oceny diagnostycznej i planowania łącznie z wyceną) | protetyka | draft |  |
| 23.2704 | Przygotowanie uszkodzonego zęba do osadzenia korony poprzez odbudowę kikuta zęba wkładem koronowo-korzeniowym lanym lub śrubowym | protetyka | draft |  |
| 23.2705 | Ochrona oszlifowanego zęba kształka, formówka | protetyka | draft |  |
| 23.2706 | Ochrona oszlifowanego zęba i zabezpieczenie funkcji prowizoryczną koroną lub zastąpienia brakującego zęba elementem prowizorycznego mostu, za koronę lub element mostu | protetyka | draft |  |
| 23.2715 | Wykonanie i zaopatrzenie w protezę twarzy | protetyka | not_started | Pominięte decyzją Patryka (22.11.2026): proteza twarzy – leczenie szpitalne / specjalistyczne. |
| 23.2718 | Wykonanie i zaopatrzenie w protezę gałki ocznej, wargi i nosa | protetyka | not_started | Pominięte decyzją Patryka (22.11.2026): proteza gałki ocznej, wargi i nosa – leczenie specjalistyczne. |
| 23.2801 | Odbudowa pojedynczego zęba przy zastosowaniu korony lanej | protetyka – korony | draft |  |
| 23.2802 | Odbudowa pojedynczego zęba przy zastosowaniu korony licowanej | protetyka – korony | draft |  |
| 23.2803 | Odbudowa pojedynczego zęba przy zastosowaniu korony pochewkowej lub częściowej (szlifowanie zęba ze stopniem okrężnym) | protetyka – korony | draft |  |
| 23.2804 | Czynności związane z odtworzeniem funkcji koron i prowizorycznych mostów - ponowne osadzenie korony, zęba ćwiekowego, licówki również zdjęcie korony żywiczej | protetyka – korony | draft |  |
| 23.2805 | Czynności związane z odtworzeniem funkcji koron i prowizorycznych mostów - odnowienie licówki, licowania korony itp. | protetyka – korony | draft |  |
| 23.2806 | Czynności związane z odtworzeniem funkcji koron i prowizorycznych mostów - zdjęcie i powtórne umocowanie prowizorycznej korony | protetyka – korony | draft |  |
| 23.2901 | Likwidacja dużych zaburzeń artykulacyjnych i zgryzowych przed uzupełnieniem braków zębowych protezami lub mostami | protetyka | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.2902 | Zmiana położenia szczęki za pomocą płytki zgryzowej (prowadzącej , ustalającej zwarcie, relaksacyjnej) | protetyka | draft |  |
| 23.2903 | Wycisk czynnościowy za pomocą łyżki indywidualnej | protetyka | draft |  |
| 23.3001 | Uzupełnienie braków zębowych mostem - za każdy ząb filarowy odbudowany koroną laną | protetyka – mosty | draft |  |
| 23.3002 | Uzupełnienie braków zębowych mostem - za każdy ząb filarowy odbudowany koroną licowaną | protetyka – mosty | draft |  |
| 23.3003 | Uzupełnienie braków zębowych mostem - za każdy ząb filarowy odbudowany koroną pochewkową lub częściową | protetyka – mosty | draft |  |
| 23.3004 | Uzupełnienie braków zębowych mostem - za każdy ząb filarowy odbudowany koroną teleskopową | protetyka – mosty | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3005 | Dalsze czynności przy uzupełnianiu braków zębowych za pomocą na stałe mocowanych mostów za każdy element (punkt) przęsła; liczy się również element jednobrzeżny | protetyka – mosty | draft |  |
| 23.3006 | Uzupełnienie braków zębowych za pomocą złożonych na stałe umocowanych lub ruchomych mostów i/lub złożonych stałych/ruchomych uzupełnień - dodatkowo przy zastosowaniu przęsła, włącznie z elementem łączącym każde przęsło | protetyka – mosty | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3007 | Uzupełnienie braków zębowych za pomocą złożonych na stałe umocowanych lub ruchomych mostów i/lub złożonych stałych /ruchomych uzupełnień - dodatkowo przy zastosowaniu śrub, sztyftów sprężynowych lub tp. - za każdy element łączący | protetyka – mosty | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3008 | Uzupełnienie braków zębowych za pomocą złożonych na stałe umocowanych lub ruchomych mostów i/lub złożonych stałych /ruchomych uzupełnień - dodatkowo przy zastosowaniu zatrzasków, zawiasów, zasuw lub zakotwiczeń - za każdy element (matrycę i stempel należy traktować jako całość) | protetyka – mosty | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3009 | Czynności dla odtworzenia funkcji mostów lub mocowanych na stałe szyn -powtórne osadzenie mostu lub stałej szyny z dwoma zakotwiczeniami | protetyka – mosty | draft |  |
| 23.3010 | Czynności dla odtworzenia funkcji mostów lub mocowanych na stałe szyn- powtórne osadzenie mostu lub stałej szyny z więcej niż dwoma zakotwiczeniami | protetyka – mosty | draft |  |
| 23.3011 | Czynności dla odtworzenia funkcji mostu - odnowienie licówki, licowania korony filarowej | protetyka – mosty | draft |  |
| 23.3101 | Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie 1-4 brakujących zębów | protetyka – protezy ruchome | draft |  |
| 23.3102 | Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie 5-8 brakujących zębów | protetyka – protezy ruchome | draft |  |
| 23.3103 | Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie więcej niż 8 zębów | protetyka – protezy ruchome | draft |  |
| 23.3104 | Zaopatrzenie bezzębnej szczęki protezą całkowitą w szczęce | protetyka – protezy ruchome | draft |  |
| 23.31041 | Proteza całkowita górna o charakterze overdenture oparta na zabezpieczonych korzeniach | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3105 | Zaopatrzenie bezzębnej szczęki protezą całkowitą w żuchwie | protetyka – protezy ruchome | draft |  |
| 23.31051 | Proteza całkowita dolna o charakterze overdenture oparta na zabezpieczonych korzeniach | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3106 | Zastosowanie metalowej podstawy przy bezzębnej szczęce | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3107 | Zastosowanie prostych dwuramiennych elementów utrzymujących lub podpierających lub wieloramiennych elementów doginanych o podobnym działaniu dodatkowo do każdej protezy- przy prowizorycznych protezach jedynie w szczególnych przypadkach, za element | protetyka – protezy ruchome | draft |  |
| 23.3108 | Zastosowanie płyty metalowej z elementami utrzymującymi i podporami | protetyka – protezy ruchome | draft |  |
| 23.3109 | Zastosowanie odlewanych skomplikowanych elementów utrzymujących i podpierających przy zastosowaniu jednego elementu utrzymującego i podpierającego - nie przy protezach prowizorycznych | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3110 | Zastosowanie odlewanych skomplikowanych elementów utrzymujących i podpierających przy zastosowaniu przynajmniej dwóch elementów utrzymujących i podpierającychnie przy protezach prowizorycznych | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3111 | Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) w małym zakresie bez wycisku | protetyka – protezy ruchome | draft |  |
| 23.3112 | Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) w większym zakresie z wyciskiem | protetyka – protezy ruchome | draft |  |
| 23.3113 | Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) - częściowe podścielenie jednej protezy | protetyka – protezy ruchome | draft |  |
| 23.3114 | Całkowite bezpośrednie podścielenie jednej protezy | protetyka – protezy ruchome | draft |  |
| 23.3115 | Całkowite podścielenie jednej protezy w sposób pośredni | protetyka – protezy ruchome | draft |  |
| 23.3116 | Całkowite podścielenie jednej protezy w sposób pośredni, włącznie z ukształtowaniem obrzeża - dla szczęki | protetyka – protezy ruchome | draft |  |
| 23.3117 | Całkowite podścielenie jednej protezy w sposób pośredni włącznie z czynnościowym ukształtowaniem obrzeża -dla żuchwy | protetyka – protezy ruchome | draft |  |
| 23.3118 | Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównanie lub zamknięcie defektów w obrębie szczęki przy istniejącym uzębieniu resztkowym | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3119 | Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównania lub zamknięcia defektów w obrębie bezzębnej szczęki | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3120 | Wykonanie obturatora dla zamknięcia podniebienia miękkiego | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3121 | Wykonanie tymczasowej protezy poresekcyjnej wypełniającej ubytki po resekcji lub uzupełniającej duże defekty szczęki | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3122 | Wykonanie protezy poresekcyjnej ostatecznej | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3123 | Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy w mniejszym zakresie | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3124 | Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy o większym zakresie | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): obturatory, protezy poresekcyjne, epitezy – protetyka szczękowo-twarzowa (specjalistyczna). |
| 23.3125 | Czynności związane z odtwarzaniem funkcji koron i mostów - zdjęcie korony lanej | protetyka – protezy ruchome | draft |  |
| 23.3126 | Czynności odtwarzające wysokość zwarcia poprzez zastosowanie elementów nakładowych w protezie | protetyka – protezy ruchome | requires_expert_review | Rozwiązanie protetyczne specjalistyczne – treść do weryfikacji (Patryk / protetyk). |
| 23.3127 | Zastosowanie szyny lanej do repozycji i unieruchomienia złamania szczęk lub repozycji i unieruchomienia szczęk po zabiegach korygujących wady zgryzu - za każde 2 zęby kolejne objęte szyną | protetyka – protezy ruchome | not_started | Pominięte decyzją Patryka (22.11.2026): szyna lana do złamań szczęk – chirurgia szczękowo-twarzowa. |
