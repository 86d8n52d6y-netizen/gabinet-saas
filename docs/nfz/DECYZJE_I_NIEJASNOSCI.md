# Decyzje i niejasności – do rozstrzygnięcia przez Patryka

> Stan na 21.11.2026. Każda pozycja ma proponowaną odpowiedź (A/B/C). Bez decyzji nic z tej listy nie trafia do kodu.

## Decyzje (D)

| ID | Pytanie | A (rekomendacja) | B | C |
|---|---|---|---|---|
| D1 | ST30E/ST30G w aplikacji pokazywane dorosłym | dodać ograniczenie < 18 (ostrzeżenie + blokada eksportu) | tylko ostrzeżenie | bez zmian |
| D2 | Gdzie liczyć reguły wymagające wieku / zęba / ciąży | tylko na urządzeniu (zgodnie z zasadą „zero danych pacjentów w chmurze”) | wiek w przedziałach na serwerze (np. „< 18”) – wymaga osobnej analizy | – |
| D3 | Rozpoznania ICD-10 | podpowiedzi przy procedurze, wybór lekarza | lista bez podpowiedzi | pominąć ICD-10 |
| D4 | Reguły ze statusem WYMAGA WERYFIKACJI | pokazywać jako INFORMACJA z adnotacją | ukryć do czasu weryfikacji | – |
| D5 | Kody NFZ z literą „a” (23.1012a, 23.3104a/3105a) | do potwierdzenia w OW NFZ, do tego czasu bez eksportu | eksportować kod ICD-9 (23.1023 / 23.31041 / 23.31051) | eksportować kod „a” |
| D6 | „Rok” w limitach ST30D/F/G | kalendarzowy + ostrzeżenie w okolicy przełomu roku | 12 miesięcy kroczących | – |
| D7 | Limity bazujące na historii (protezy 5 lat, lakowanie) | BLOKADA tylko przy zapisie na tym koncie, w innych przypadkach INFORMACJA | zawsze INFORMACJA | – |

## Niejasności (N) – wymagają źródła

| ID | Niejasność | Co trzeba zrobić |
|---|---|---|
| N1 | Zał. 2a, 3–9, 10a rozporządzenia nie zostały przeczytane (plik 57/118 stron) | Patryk dołącza pełny PDF: `https://api.sejm.gov.pl/eli/acts/DU/2025/615/text.pdf` |
| N2 | Zakresy (maska 12 zakresów) dla wierszy zał. 1b | ponowny odczyt akt.xml (BAW 44022) |
| N3 | Brak kodów produktów dla części 1b (protetyka, ortodoncja, część endo) | j.w. |
| N4 | Kody produktów 2310090 (23.1003), 2314142 (23.13142), 2325040 (23.2503) wyglądają nietypowo | sprawdzić znak po znaku |
| N5 | Skład pakietów ST06–ST13, ST15–ST17, ST19–ST25, ST31, ST32 niepełny | odczyt zał. 1d |
| N6 | Kiretaż u dzieci (komunikat 22.07.2026) | przeczytać komunikat i ewentualną odpowiedź NFZ na protest NIL |
| N7 | Q&A z komunikatów 9017 i 9054 (ST30D a ST33, ST30 a ST30F) | przenieść odpowiedzi dosłownie |
| N8 | Polskie urzędowe nazwy ICD-10; obecność K02.5 i K12.3 w wydaniu PL | porównać z Tomem I CeZ |
| N9 | OWU – wysokość kar umownych, przesłanki zwrotu | odczyt t.j. Dz.U. 2026 poz. 712 |
| N10 | Rozporządzenie o dokumentacji – wymagane elementy wpisu | odczyt t.j. Dz.U. 2026 poz. 1391 |
| N11 | Wyrok SN III CSK 296/16 – treść | pobrać z sn.pl i przeczytać |
| N12 | Odpowiedź MZ na interpelację 16442 | sprawdzić na sejm.gov.pl |

## Odmowy dostępu w tej sesji (dla jasności)

| Próba | Wynik | Co zrobiono |
|---|---|---|
| Dostęp do folderu „Pobrane” na Macu (po pełny PDF) | odrzucony przez system uprawnień | nie obchodzono – prośba o załączenie pliku |
| Załadowanie pdf.js z CDN w przeglądarce (odczyt PDF z ELI) | odrzucone | nie obchodzono |
