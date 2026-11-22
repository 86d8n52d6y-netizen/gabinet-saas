# Karty procedur ICD-9 (świadczenia gwarantowane – stomatologia)

> Stan prawny na **21.11.2026**. Dokument generowany z `data/nfz/*.json` (`scripts` w paczce audytu) – nie edytuj ręcznie, popraw dane i wygeneruj ponownie.


Każda karta ma 25 pól. Puste pole jest zabronione – zamiast niego „NIE DOTYCZY” albo „WYMAGA WERYFIKACJI”.

Liczba kart: **107**. Pakiety (ST..) opisane są w tabeli na końcu.


## 23.02 – Badanie żywotności zęba

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.02 |
| 2. Nazwa ICD-9 PL 5.91 | Badanie żywotności zęba |
| 3. Nazwa w rozporządzeniu | Badanie żywotności zęba |
| 4. Załącznik / lp | zał. 1 lp 4, zał. 2 lp 4, zał. 2b lp 4 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST28, ST30 (lista ST4) |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje badanie żywotności zęba z objęciem badaniem 3 zębów sąsiednich lub przeciwstawnych. • [zał. 2] Świadczenie obejmuje badanie żywotności zęba z objęciem badaniem 3 zębów sąsiednich lub przeciwstawnych. • [zał. 2b] Świadczenie obejmuje badanie żywotności zęba z objęciem badaniem 3 zębów sąsiednich lub przeciwstawnych. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Badanie żywotności obejmuje ząb + 3 zęby sąsiednie lub przeciwstawne – dokumentować wyniki. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.1, S02.5 |
| 20. Ryzyka kontrolne | R-ZYW-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.06 – Wizyta adaptacyjna -dotyczy pierwszych wizyt małych dzieci

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.06 |
| 2. Nazwa ICD-9 PL 5.91 | Wizyta adaptacyjna -dotyczy pierwszych wizyt małych dzieci |
| 3. Nazwa w rozporządzeniu | Wizyta adaptacyjna – dotyczy pierwszych wizyt małych dzieci |
| 4. Załącznik / lp | zał. 1 lp 43, zał. 2 lp 36, zał. 2b lp 36 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2306000 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 85 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane bez połączenia z innymi świadczeniami gwarantowanymi. Świadczenie dotyczy pierwszej wizyty małych dzieci (do ukończenia 6. roku życia). • [zał. 2] Świadczenie jest udzielane bez połączenia z innymi świadczeniami gwarantowanymi. Świadczenie dotyczy pierwszej wizyty małych dzieci (do ukończenia 6. roku życia). • [zał. 2b] Świadczenie jest udzielane bez połączenia z innymi świadczeniami gwarantowanymi. Świadczenie dotyczy pierwszej wizyty dzieci do ukończenia 6. roku życia. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | Wizyta adaptacyjna – bez połączenia z innymi świadczeniami; pierwsza wizyta dziecka do ukończenia 6. r.ż. |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z01.2 |
| 20. Ryzyka kontrolne | R-ADAPT-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.17 – Chirurgiczne usunięcie zęba

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.17 |
| 2. Nazwa ICD-9 PL 5.91 | Chirurgiczne usunięcie zęba |
| 3. Nazwa w rozporządzeniu | Chirurgiczne usunięcie zęba |
| 4. Załącznik / lp | zał. 1 lp 30, zał. 2 lp 30, zał. 2b lp 30 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST03 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje usunięcie zęba przez dłutowanie wewnątrzzębodołowe z zastosowaniem wierteł i dźwigni. Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2] Świadczenie obejmuje usunięcie zęba przez dłutowanie wewnątrzzębodołowe z zastosowaniem wierteł i dźwigni. Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2b] Świadczenie obejmuje usunięcie zęba przez dłutowanie wewnątrzzębodołowe z zastosowaniem wierteł i dźwigni. Świadczenie nie obejmuje odpowiedniego znieczulenia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.1, K04.5, K04.7, K02.9, K05.3, K08.3, K01.1, S02.5, K07.3 |
| 20. Ryzyka kontrolne | R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0101 – Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0101 |
| 2. Nazwa ICD-9 PL 5.91 | Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej |
| 3. Nazwa w rozporządzeniu | Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej (kod ICD-9-CM 23.08) |
| 4. Załącznik / lp | zał. 1 lp 1, zał. 2 lp 1, zał. 2b lp 1 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST30D, ST30F, ST33, ST33A |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Badanie lekarskie stomatologiczne – 1 raz w roku kalendarzowym. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane 1 raz w roku kalendarzowym. • [zał. 2] Świadczenie jest udzielane 1 raz w roku kalendarzowym. • [zał. 2b] Świadczenie jest udzielane raz w roku kalendarzowym. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z01.2 |
| 20. Ryzyka kontrolne | R-BAD-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0102 – Badanie lekarskie kontrolne

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0102 |
| 2. Nazwa ICD-9 PL 5.91 | Badanie lekarskie kontrolne |
| 3. Nazwa w rozporządzeniu | Badanie lekarskie kontrolne |
| 4. Załącznik / lp | zał. 1 lp 2, zał. 2 lp 2, zał. 2b lp 2 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST34, ST34A |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Badanie kontrolne – 3 razy w roku kalendarzowym; ciąża/połóg – nie częściej niż 1 raz na kwartał. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane 3 razy w roku kalendarzowym. W przypadku kobiet w ciąży i w okresie połogu świadczenie jest udzielane nie częściej niż 1 raz na kwartał. • [zał. 2] Świadczenie jest udzielane 3 razy w roku kalendarzowym. W przypadku kobiet w ciąży i w okresie połogu świadczenie jest udzielane nie częściej niż 1 raz na kwartał. • [zał. 2b] Świadczenie jest udzielane 3 razy w roku kalendarzowym. W przypadku kobiet w ciąży i w okresie połogu świadczenie jest udzielane nie częściej niż raz na kwartał. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z01.2 |
| 20. Ryzyka kontrolne | R-BAD-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0105 – Konsultacja specjalistyczna

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0105 |
| 2. Nazwa ICD-9 PL 5.91 | Konsultacja specjalistyczna |
| 3. Nazwa w rozporządzeniu | Konsultacja specjalistyczna |
| 4. Załącznik / lp | zał. 1 lp 3, zał. 2 lp 3, zał. 2b lp 3 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST29 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje badanie lekarza specjalisty z krótką pisemną oceną i wskazaniami diagnostyczno- -terapeutycznymi dla lekarza prowadzącego, bez połączenia z innymi świadczeniami gwarantowanymi. • [zał. 2] Świadczenie obejmuje badanie lekarza specjalisty z krótką pisemną oceną i wskazaniami diagnostyczno- -terapeutycznymi dla lekarza prowadzącego, bez połączenia z innymi świadczeniami gwarantowanymi. • [zał. 2b] Świadczenie obejmuje badanie lekarza specjalisty z krótką pisemną oceną i wskazaniami diagnostyczno-terapeutycznymi dla lekarza prowadzącego, bez połączenia z innymi świadczeniami gwarantowanymi. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | Konsultacja specjalistyczna bez połączenia z innymi świadczeniami gwarantowanymi. |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | Konsultacja specjalistyczna bez połączenia z innymi świadczeniami gwarantowanymi. |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z01.2 |
| 20. Ryzyka kontrolne | R-KONS-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0107 – Badanie lekarskie stomatologiczne i kontrolne po urazie zęba

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0107 |
| 2. Nazwa ICD-9 PL 5.91 | Badanie lekarskie stomatologiczne i kontrolne po urazie zęba |
| 3. Nazwa w rozporządzeniu | Badanie lekarskie stomatologiczne i kontrolne po urazie zęba / Badanie lekarskie stomatologiczne i kontrolne po urazie zębów |
| 4. Załącznik / lp | zał. 1 lp 60, zał. 2 lp 53, zał. 2b lp 53 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST28 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. Świadczenie obejmuje jednorazowe badanie lekarskie stomatologiczne po urazie zęba wraz z instruktażem higieny jamy ustnej, w połączeniu ze świadczeniami stomatologicznymi związanymi z udzieleniem pomocy medycznej pourazowej, oraz badanie lekarskie kontrolne związane z urazem zęba, wykonywane do 3 razy w ciągu pierwszych 6 miesięcy od urazu, z wpisaniem opisu do dokumentacji medycznej. 3) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 3 kanałów; 4) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA – inne. 23.13143 23.13149 • [zał. 2] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. Świadczenie obejmuje jednorazowe badanie lekarskie stomatologiczne po urazie zęba wraz z instruktażem higieny jamy ustnej, w połączeniu ze świadczeniami stomatologicznymi związanymi z udzieleniem pomocy medycznej pourazowej, oraz badanie lekarskie kontrolne związane z urazem zęba, wykonywane do 3 razy w ciągu pierwszych 6 miesięcy od urazu, z wpisaniem opisu do dokumentacji medycznej. • [zał. 2b] Świadczenie obejmuje jednorazowe badanie lekarskie stomatologiczne po urazie wraz z instruktażem higieny jamy ustnej, w połączeniu ze świadczeniami stomatologicznymi związanymi z udzieleniem pomocy medycznej pourazowej, oraz badanie lekarskie kontrolne związane z urazem zęba, wykonywane do 3 razy w okresie pierwszych 6 miesięcy od urazu, z wpisaniem opisu do dokumentacji medycznej. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0301 – Rentgenodiagnostyka do 2 zdjęć wewnątrzustnych

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0301 |
| 2. Nazwa ICD-9 PL 5.91 | Rentgenodiagnostyka do 2 zdjęć wewnątrzustnych |
| 3. Nazwa w rozporządzeniu | Rentgenodiagnostyka do 2 zdjęć wewnątrzustnych |
| 4. Załącznik / lp | zał. 1 lp 5, zał. 2 lp 5, zał. 2b lp 5 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2303010 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 20 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie jest udzielane do 2 zdjęć wewnątrzustnych w roku kalendarzowym w połączeniu z innymi świadczeniami gwarantowanymi z wpisaniem opisu do dokumentacji medycznej. • [zał. 2] Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie jest udzielane do 2 zdjęć wewnątrzustnych w roku kalendarzowym w połączeniu z innymi świadczeniami gwarantowanymi z wpisaniem opisu do dokumentacji medycznej. • [zał. 2b] Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie jest udzielane do 2 zdjęć wewnątrzustnych w roku kalendarzowym w połączeniu z innymi świadczeniami gwarantowanymi z wpisaniem opisu do dokumentacji medycznej. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. |
| 13. Warunki z zarządzenia | Przypis: rozliczane także 23.0302 |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Opis zdjęcia musi być wpisany do dokumentacji medycznej. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.1, K04.5, K01.1, K08.3, K07.3 |
| 20. Ryzyka kontrolne | R-RTG-01; R-RTG-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0302 – Rentgenodiagnostyka do 5 zdjęć wewnątrzustnych

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0302 |
| 2. Nazwa ICD-9 PL 5.91 | Rentgenodiagnostyka do 5 zdjęć wewnątrzustnych |
| 3. Nazwa w rozporządzeniu | Rentgenodiagnostyka do 5 zdjęć wewnątrzustnych |
| 4. Załącznik / lp | zał. 1 lp 62, zał. 2 lp 55, zał. 2b lp 55 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie obejmuje wykonanie do 5 zdjęć wewnątrzustnych w roku kalendarzowym wraz z przygotowaniem opisu badań oraz wpisaniem opisu zdjęć w dokumentację medyczną pacjenta. Świadczenie jest realizowane w połączeniu ze świadczeniami gwarantowanymi o kodzie ICD-9 23.01 wraz z rozszerzeniami oraz 23.13 wraz z rozszerzeniami. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania, w tym liczbę zdjęć. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. • [zał. 2] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie obejmuje wykonanie do 5 zdjęć wewnątrzustnych w roku kalendarzowym wraz z przygotowaniem opisu badań oraz wpisaniem opisu zdjęć w dokumentację medyczną pacjenta. Świadczenie jest realizowane w połączeniu ze świadczeniami gwarantowanymi o kodzie ICD-9 23.01 wraz z rozszerzeniami oraz 23.13 wraz z rozszerzeniami. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania, w tym liczbę zdjęć. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. • [zał. 2b] Świadczenie obejmuje wykonanie techniczne zdjęcia. Świadczenie obejmuje wykonanie do 5 zdjęć wewnątrzustnych w roku kalendarzowym wraz z przygotowaniem opisu badań oraz wpisaniem opisu zdjęć do dokumentacji medycznej pacjenta. Świadczenie jest realizowane w połączeniu ze świadczeniami gwarantowanymi o kodzie ICD-9 23.01 wraz z rozszerzeniami oraz 23.13 wraz z rozszerzeniami. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania, w tym liczbę zdjęć. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Opis zdjęcia musi być wpisany do dokumentacji medycznej. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.1, K04.5, K01.1, K08.3, K07.3 |
| 20. Ryzyka kontrolne | R-RTG-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0304 – Rentgenodiagnostyka - zdjęcie pantomograficzne z opisem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0304 |
| 2. Nazwa ICD-9 PL 5.91 | Rentgenodiagnostyka - zdjęcie pantomograficzne z opisem |
| 3. Nazwa w rozporządzeniu | Rentgenodiagnostyka – zdjęcie pantomograficzne z opisem |
| 4. Załącznik / lp | zał. 1 lp 6310), zał. 2 lp 56, zał. 2b lp 56 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2303040 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 74 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Pantomogram: dorośli – na potrzeby leczenia endodontycznego oraz (wszyscy) przed protetyką, 1 raz na 5 lat; dzieci 5–18 lat – w uzasadnionych medycznie przypadkach, 1 raz na 3 lata; zawsze w połączeniu z innymi świadczeniami, z opisem w dokumentacji. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] W przypadku: 1) osób dorosłych świadczenie jest udzielane na potrzeby leczenia endodontycznego oraz w przypadku wszystkich świadczeniobiorców przed rozpoczęciem udzielania świadczeń protetyki stomatologicznej. Świadczenie jest udzielane 1 raz na 5 lat w połączeniu ze świadczeniami gwarantowanymi z zakresu leczenia stomatologicznego; 2) dzieci i młodzieży od 5. do ukończenia 18. roku życia świadczenie jest udzielane w uzasadnionych medycznie przypadkach przy podejrzeniu nieprawidłowości rozwojowych zębów, zmian chorobowych w obrębie kości szczęk lub zapalenia przyzębia lub w diagnostyce ognisk infekcji zębo- i niezębopochodnych. Świadczenie jest udzielane 1 raz na 3 lata w połączeniu ze świadczeniami gwarantowanymi z zakresu leczenia stomatologicznego. Świadczenie obejmuje wykonanie techniczne zdjęcia wraz z przygotowaniem opisu badania oraz wpisaniem opisu zdjęcia w dokumentację medyczną pacjenta. Skierowanie wystawia lekarz dentysta posiadający specjalizację lub lekarz dentysta w trakcie szkolenia specjalizacyjnego. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub dostępie. • [zał. 2] Świadczenie jest udzielane dzieciom i młodzieży od 5. do ukończenia 18. roku życia w uzasadnionych medycznie przypadkach przy podejrzeniu nieprawidłowości rozwojowych zębów, zmian chorobowych w obrębie kości szczęk lub zapalenia przyzębia, diagnostyce ognisk infekcji zębo- i niezębopochodnych. Świadczenie obejmuje wykonanie techniczne zdjęcia wraz z przygotowaniem opisu badania oraz wpisaniem opisu zdjęcia w dokumentację medyczną pacjenta. Świadczenie jest udzielane 1 raz na 3 lata w połączeniu ze świadczeniami gwarantowanymi z zakresu stomatologii. Skierowanie wystawia lekarz dentysta posiadający specjalizację lub lekarz dentysta w trakcie szkolenia specjalizacyjnego. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. • [zał. 2b] Świadczenie jest udzielane dzieciom i młodzieży od 5. do ukończenia 18. roku życia w uzasadnionych medycznie przypadkach przy podejrzeniu nieprawidłowości rozwojowych zębów, zmian chorobowych w obrębie kości szczęk lub zapalenia przyzębia, lub diagnostyce ognisk infekcji zębo- i niezębopochodnych. Świadczenie obejmuje wykonanie techniczne zdjęcia wraz z przygotowaniem opisu badań oraz wpisaniem opisu zdjęcia do dokumentacji medycznej pacjenta. Świadczenie jest udzielane 1 raz na 3 lata w połączeniu ze świadczeniami gwarantowanymi z zakresu stomatologii. Skierowanie wystawia lekarz dentysta posiadający specjalizację lub lekarz dentysta w trakcie szkolenia specjalizacyjnego. Lekarz kierujący na badanie ma obowiązek uzasadnić w treści skierowania konieczność wykonania badania. Wyposażenie niezbędne do realizacji świadczenia: aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Opis zdjęcia musi być wpisany do dokumentacji medycznej. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.1, K04.5, K01.1, K08.3, K07.3 |
| 20. Ryzyka kontrolne | R-RTG-02; R-RTG-03 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0401 – Znieczulenie miejscowe powierzchniowe

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0401 |
| 2. Nazwa ICD-9 PL 5.91 | Znieczulenie miejscowe powierzchniowe |
| 3. Nazwa w rozporządzeniu | Znieczulenie miejscowe powierzchniowe |
| 4. Załącznik / lp | zał. 1 lp 6, zał. 2 lp 6, zał. 2b lp 6 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2304010 |
| 8. Pakiety, w których występuje | ST01 (lista ST1), ST04 (lista ST1), ST19 (lista ST1), ST20 (lista ST1), ST21 (lista ST1), ST22 (lista ST1), ST23 (lista ST1), ST24 (lista ST1), ST25 (lista ST1), ST30 (lista ST1) |
| 9. Punkty (zał. 1b) | 3 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane jako samodzielne znieczulenie w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2] Świadczenie jest udzielane jako samodzielne znieczulenie w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2b] Świadczenie jest udzielane jako samodzielne znieczulenie w połączeniu z innymi świadczeniami gwarantowanymi. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | NIE DOTYCZY |
| 20. Ryzyka kontrolne | R-ZNI-01; R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0402 – Znieczulenie miejscowe nasiękowe

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0402 |
| 2. Nazwa ICD-9 PL 5.91 | Znieczulenie miejscowe nasiękowe |
| 3. Nazwa w rozporządzeniu | Znieczulenie miejscowe nasiękowe |
| 4. Załącznik / lp | zał. 1 lp 7, zał. 2 lp 7, zał. 2b lp 7 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2304020 |
| 8. Pakiety, w których występuje | ST01 (lista ST1), ST04 (lista ST1), ST19 (lista ST1), ST20 (lista ST1), ST21 (lista ST1), ST22 (lista ST1), ST23 (lista ST1), ST24 (lista ST1), ST25 (lista ST1), ST30 (lista ST1) |
| 9. Punkty (zał. 1b) | 12 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2b] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | NIE DOTYCZY |
| 20. Ryzyka kontrolne | R-ZNI-01; R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.0403 – Znieczulenie przewodowe wewnątrzustne

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.0403 |
| 2. Nazwa ICD-9 PL 5.91 | Znieczulenie przewodowe wewnątrzustne |
| 3. Nazwa w rozporządzeniu | Znieczulenie przewodowe wewnątrzustne |
| 4. Załącznik / lp | zał. 1 lp 8, zał. 2 lp 8, zał. 2b lp 8 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2304030 |
| 8. Pakiety, w których występuje | ST01 (lista ST1), ST04 (lista ST1), ST19 (lista ST1), ST20 (lista ST1), ST21 (lista ST1), ST22 (lista ST1), ST23 (lista ST1), ST24 (lista ST1), ST25 (lista ST1), ST30 (lista ST1) |
| 9. Punkty (zał. 1b) | 20 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. • [zał. 2b] Świadczenie jest udzielane w połączeniu z innymi świadczeniami gwarantowanymi. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | NIE DOTYCZY |
| 20. Ryzyka kontrolne | R-ZNI-01; R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1003 – Zabezpieczenie profilaktyczne bruzd lakiem szczelinowym - za każdy ząb

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1003 |
| 2. Nazwa ICD-9 PL 5.91 | Zabezpieczenie profilaktyczne bruzd lakiem szczelinowym - za każdy ząb |
| 3. Nazwa w rozporządzeniu | Zabezpieczenie profilaktyczne bruzd lakiem szczelinowym – za każdy ząb |
| 4. Załącznik / lp | zał. 1 lp 44, zał. 2 lp 37, zał. 2b lp 37 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2310090 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 11 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Lakowanie bruzd: pierwsze trzonowce stałe – 1 raz do ukończenia 8. r.ż.; drugie trzonowce stałe – 1 raz do ukończenia 14. r.ż. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy bruzd pierwszych trzonowców stałych i jest udzielane 1 raz do ukończenia 8. roku życia oraz bruzd drugich trzonowców stałych i jest udzielane 1 raz do ukończenia 14. roku życia. • [zał. 2] Świadczenie dotyczy bruzd pierwszych trzonowców stałych i jest udzielane 1 raz do ukończenia 8. roku życia oraz bruzd drugich trzonowców stałych i jest udzielane 1 raz do ukończenia 14. roku życia. • [zał. 2b] Świadczenie dotyczy bruzd pierwszych trzonowców stałych i jest udzielane 1 raz do ukończenia 8. roku życia oraz bruzd drugich trzonowców stałych i jest udzielane 1 raz do ukończenia 14. roku życia. |
| 13. Warunki z zarządzenia | Kod produktu 2310090 przy ICD-9 23.1003 – odczytany tak w zał. 1b; zweryfikować znak po znaku |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, K02.0, K02.3 |
| 20. Ryzyka kontrolne | R-LAKOW-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1004 – Zabezpieczanie profilaktyczne bruzd innymi materiałami

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1004 |
| 2. Nazwa ICD-9 PL 5.91 | Zabezpieczanie profilaktyczne bruzd innymi materiałami |
| 3. Nazwa w rozporządzeniu | Profilaktyczne zabezpieczenie bruzd innymi materiałami PRR typu 1 |
| 4. Załącznik / lp | zał. 1 lp 6411), zał. 2 lp 5714), zał. 2b lp 5720) |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2310040 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 42 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy bruzd pierwszych i drugich trzonowców stałych. • [zał. 2] Świadczenie dotyczy bruzd pierwszych i drugich trzonowców stałych. • [zał. 2b] Świadczenie dotyczy bruzd pierwszych i drugich trzonowców stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, K02.0, K02.3 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1006 – Lakierowanie zębów 1/4 łuku zębowego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1006 |
| 2. Nazwa ICD-9 PL 5.91 | Lakierowanie zębów 1/4 łuku zębowego |
| 3. Nazwa w rozporządzeniu | Lakierowanie zębów 1/4 łuku zębowego |
| 4. Załącznik / lp | zał. 1 lp 459), zał. 2 lp 3813), zał. 2b lp 3819) |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2310060 |
| 8. Pakiety, w których występuje | ST30D (lista ST5) |
| 9. Punkty (zał. 1b) | 5 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Lakierowanie 23.1006 – tylko dzieci i młodzież do 18. r.ż.; zęby mleczne i stałe; nie częściej niż 1× na kwartał za każdą ¼ łuku. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy wszystkich zębów mlecznych i stałych i jest udzielane nie częściej niż 1 raz na kwartał – za każdą 1/4 łuku zębowego. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie dotyczy wszystkich zębów mlecznych i stałych i jest udzielane nie częściej niż 1 raz na kwartał – za każdą 1/4 łuku zębowego. • [zał. 2b] Świadczenie dotyczy wszystkich zębów mlecznych i stałych i jest udzielane nie częściej niż 1 raz na kwartał – za każdą 1/4 łuku zębowego. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | Pakiety ST30, ST30A, ST30B, ST30C nie sumują się z 23.1006 (lakierowanie) – wycena pakietu obejmuje lakierowanie. |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, K02.0, K02.3 |
| 20. Ryzyka kontrolne | R-ST30-LAKIER; R-LAKIER-01 |
| 21. Komunikaty NFZ / spory | R-ST30-LAKIER: Przed 01.09.2026: korekty wsteczne NFZ na podstawie komunikatów 1292084/819330 – SPORNE (interpelacja 16442). Aplikacja nie ocenia przeszłych rozliczeń. |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-NFZ-KOM-8924`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1008 – Impregnacja zębiny

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1008 |
| 2. Nazwa ICD-9 PL 5.91 | Impregnacja zębiny |
| 3. Nazwa w rozporządzeniu | Impregnacja zębiny |
| 4. Załącznik / lp | zał. 1 lp 46, zał. 2 lp 39, zał. 2b lp 39 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2310080 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 3 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy impregnacji zębiny zębów mlecznych – za każdy ząb. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie dotyczy impregnacji zębiny zębów mlecznych – za każdy ząb. • [zał. 2b] Świadczenie dotyczy impregnacji zębiny zębów mlecznych – za każdy ząb. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, K02.0, K02.3 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1009 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. miesiącu życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1009 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. miesiącu życia |
| 3. Nazwa w rozporządzeniu | 6. miesiąc życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. miesiącu życia |
| 4. Załącznik / lp | zał. 10 lp 1, zał. 10b lp 1 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000001 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 85 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta kontrolna z instruktażem matki w zakresie higieny jamy ustnej. 2. Badanie lekarskie stomatologiczne w zakresie początku ząbkowania i stanu jamy ustnej. • [zał. 10b] 1. Wizyta kontrolna z instruktażem w zakresie higieny jamy ustnej. 2. Badanie lekarskie stomatologiczne w zakresie początku ząbkowania i stanu jamy ustnej. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1010 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 9. miesiącu życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1010 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 9. miesiącu życia |
| 3. Nazwa w rozporządzeniu | 9. miesiąc życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 9. miesiącu życia |
| 4. Załącznik / lp | zał. 10 lp 2, zał. 10b lp 2 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000002 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 115 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia mlecznego z instruktażem matki w zakresie higieny jamy ustnej. 2. Profilaktyka fluorkowa przy braku przeciwwskazań. • [zał. 10b] 1. Ocena stanu uzębienia mlecznego z instruktażem w zakresie higieny jamy ustnej. 2. Profilaktyka fluorkowa przy braku przeciwwskazań. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1011 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 12. miesiącu życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1011 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 12. miesiącu życia |
| 3. Nazwa w rozporządzeniu | 12. miesiąc życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 12. miesiącu życia |
| 4. Załącznik / lp | zał. 10 lp 3, zał. 10b lp 3 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000003 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 115 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta adaptacyjna z oceną stanu uzębienia mlecznego. 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem matki w zakresie higieny jamy ustnej). 3. Profilaktyka fluorkowa przy braku przeciwwskazań. • [zał. 10b] 1. Wizyta adaptacyjna z oceną stanu uzębienia mlecznego. 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem w zakresie higieny jamy ustnej). 3. Profilaktyka fluorkowa przy braku przeciwwskazań. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1012 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 2. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1012 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 2. roku życia |
| 3. Nazwa w rozporządzeniu | 2. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 2. roku życia |
| 4. Załącznik / lp | zał. 10 lp 4, zał. 10b lp 4 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000004 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 144 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta adaptacyjna. 2. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych. 3. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem matki w zakresie higieny jamy ustnej). 4. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie liczby jednoimiennych górnych i dolnych siekaczy po prawej i lewej stronie łuku oraz przebiegu linii pośrodkowej; 2) sposób zwierania się siekaczy; 3) sprawdzenie toru oddychania; 4) sposób układania dziecka do snu; 5) sposób karmienia; 6) sprawdzenie występowania nawyków w postaci ssania smoczków lub palców. 5. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie o dbałości oddychania przez nos, o odpowiednich sposobach układania dziecka do snu, konieczności odzwyczajenia od nawyków. 6. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. • [zał. 10b] 1. Wizyta adaptacyjna. 2. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych. 3. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem w zakresie higieny jamy ustnej). 4. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmująca sprawdzenie: 1) liczby jednoimiennych górnych i dolnych siekaczy po prawej i lewej stronie łuku oraz przebiegu linii pośrodkowej; 2) sposobu zwierania się siekaczy; 3) toru oddychania; 4) sposobu układania dziecka do snu; 5) sposobu karmienia; 6) występowania nawyków w postaci ssania smoczków lub palców. 5. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie o dbałości oddychania przez nos, o odpowiednich sposobach układania dziecka do snu, konieczności odzwyczajenia od nawyków. 6. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1012a – 3. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 3. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1012a |
| 2. Nazwa ICD-9 PL 5.91 | brak w 5.91 – wariant NFZ / rozdz. 87 |
| 3. Nazwa w rozporządzeniu | 3. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 3. roku życia |
| 4. Załącznik / lp | zał. 10 lp 4a34), zał. 10b lp 4a37) |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000014 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 144 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta adaptacyjna przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystano świadczenia wcześniej) albo w przypadku dzieci odczuwających lęk związany z zabiegiem stomatologicznym (co najmniej 2 wizyty adaptacyjne mające na celu zmniejszenie odczuwania lęku przez dzieci oraz ocenę stanu zdrowia uzębienia). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie liczby zębów oraz przebiegu linii pośrodkowej; 2) sprawdzenie sposobu zwierania siekaczy; 3) sprawdzenie toru oddychania; 4) sprawdzenie występowania nawyków w postaci ssania smoczków lub palców. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie dotyczące: 1) dbałości o to, by dziecko oddychało przez nos; 2) wprowadzania pokarmów o stałej konsystencji; 3) oduczania nawyków. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. • [zał. 10b] 1. Wizyta adaptacyjna przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystano świadczenia wcześniej) albo w przypadku dzieci odczuwających lęk związany z zabiegiem stomatologicznym (co najmniej 2 wizyty adaptacyjne mające na celu zmniejszenie odczuwania lęku przez dzieci oraz ocenę stanu zdrowia uzębienia). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie liczby zębów oraz przebiegu linii pośrodkowej; 2) sprawdzenie sposobu zwierania siekaczy; 3) sprawdzenie toru oddychania; 4) sprawdzenie występowania nawyków w postaci ssania smoczków lub palców. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie dotyczące: 1) dbałości o to, by dziecko oddychało przez nos; 2) wprowadzania pokarmów o stałej konsystencji; 3) oduczania nawyków. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. |
| 13. Warunki z zarządzenia | 3. rok życia |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-KOD-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ICD9-PL-591`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Brak kodu w 5.91 – nie eksportować bez potwierdzenia OW NFZ |

## 23.1013 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 4. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1013 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 4. roku życia |
| 3. Nazwa w rozporządzeniu | 4. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 4. roku życia |
| 4. Załącznik / lp | zał. 10 lp 5, zał. 10b lp 5 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000005 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 144 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta adaptacyjna – przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystało świadczenia wcześniej). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie liczby zębów oraz przebiegu linii pośrodkowej; 2) sposób zwierania siekaczy; 3) sprawdzenie toru oddychania; 4) sprawdzenie występowania nawyków. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie o dbałości oddychania przez nos, o wprowadzaniu pokarmów o stałej konsystencji, odzwyczajaniu od nawyków. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. • [zał. 10b] 1. Wizyta adaptacyjna – przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystało świadczenia wcześniej). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmująca sprawdzenie: 1) liczby zębów oraz przebiegu linii pośrodkowej; 2) sposobu zwierania siekaczy; 3) toru oddychania; 4) występowania nawyków. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Pouczenie o dbałości oddychania przez nos, o wprowadzaniu pokarmów o stałej konsystencji, odzwyczajaniu od nawyków. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1014 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 5. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1014 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 5. roku życia |
| 3. Nazwa w rozporządzeniu | 5. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 5. roku życia |
| 4. Załącznik / lp | zał. 10 lp 6, zał. 10b lp 6 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000006 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 144 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Wizyta adaptacyjna – przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystało świadczenia wcześniej). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie liczby zębów; 2) sposób zwierania się siekaczy oraz przebieg linii pośrodkowej i linii za tylnymi powierzchniami drugich zębów trzonowych mlecznych; 3) występowanie nawyków; 4) starcie powierzchni żujących mlecznych trzonowców; 5) sposób kontaktu kłów. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Nauczenie sposobów działań prowadzących do eliminacji nawyków ssania smoczków i oddychania z otwartymi ustami. Zalecenie podawania pokarmów o stałej konsystencji. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Wizyta adaptacyjna – przysługuje w przypadku pierwszej wizyty dziecka (jeżeli nie wykorzystało świadczenia wcześniej). 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej i oceną stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmująca sprawdzenie: 1) liczby zębów; 2) sposobu zwierania się siekaczy oraz przebiegu linii pośrodkowej i linii za tylnymi powierzchniami drugich zębów trzonowych mlecznych; 3) występowania nawyków; 4) starcia powierzchni żujących mlecznych trzonowców; 5) sposobu kontaktu kłów. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Nauczenie sposobów działań prowadzących do eliminacji nawyków ssania smoczków i oddychania z otwartymi ustami. Zalecenie podawania pokarmów o stałej konsystencji. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1015 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1015 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. roku życia |
| 3. Nazwa w rozporządzeniu | 6. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 6. roku życia |
| 4. Załącznik / lp | zał. 10 lp 7, zał. 10b lp 7 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000007 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 144 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych i PUW* dla zębów stałych. 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmuje: 1) sprawdzenie typu wyrzynania zębów stałych (siekaczowy lub trzonowcowy); 2) sposób zwierania się pierwszych stałych zębów trzonowych według zasad Angle'a; 3) występowanie nawyków ustnych; 4) starcie powierzchni żujących zębów mlecznych. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Nauczenie sposobów działań prowadzących do eliminacji nawyków ssania smoczków i oddychania z otwartymi ustami. Zalecenie podawania pokarmów o stałej konsystencji. W uzasadnianych przypadkach opiłowanie niestartych powierzchni mlecznych kłów prowadzących dolny łuk zębowy nadmiernie ku tyłowi. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych i PUW* dla zębów stałych. 2. Kontrola higieny jamy ustnej (badanie kontrolne wraz z instruktażem higieny jamy ustnej). 3. Ocena stanu morfologicznego i funkcji żucia oraz wyrzynania zębów obejmująca sprawdzenie: 1) typu wyrzynania zębów stałych (siekaczowy lub trzonowcowy); 2) sposobu zwierania się pierwszych stałych zębów trzonowych według zasad Angle'a; 3) występowania nawyków ustnych; 4) starcia powierzchni żujących zębów mlecznych. 4. Zastosowanie działań zapobiegających wadom zgryzu – profilaktyka ortodontyczna. Nauczenie sposobów działań prowadzących do eliminacji nawyków ssania smoczków i oddychania z otwartymi ustami. Zalecenie podawania pokarmów o stałej konsystencji. W uzasadnianych przypadkach opiłowanie niestartych powierzchni mlecznych kłów prowadzących dolny łuk zębowy nadmiernie ku tyłowi. 5. Profilaktyka profesjonalna próchnicy, w tym profilaktyka fluorkowa przy braku przeciwwskazań. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1016 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 7. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1016 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 7. roku życia |
| 3. Nazwa w rozporządzeniu | 7. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 7. roku życia |
| 4. Załącznik / lp | zał. 10 lp 8, zał. 10b lp 8 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000008 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych i PUW* dla zębów stałych. 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych i wskaźnika puw* dla zębów mlecznych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy puw* dla zębów mlecznych i PUW* dla zębów stałych. 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych i wskaźnika puw* dla zębów mlecznych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1017 – Profilaktyczne świadczenie stomatologiczne dla dziecka w 10. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1017 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla dziecka w 10. roku życia |
| 3. Nazwa w rozporządzeniu | 10. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 10. roku życia |
| 4. Załącznik / lp | zał. 10 lp 9, zał. 10b lp 9 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000009 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i puw* dla zębów mlecznych oraz ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych i wskaźnika puw* dla zębów mlecznych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i puw* dla zębów mlecznych oraz ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych i wskaźnika puw* dla zębów mlecznych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1018 – Profilaktyczne świadczenie stomatologiczne dla młodzieży w 12. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1018 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 12. roku życia |
| 3. Nazwa w rozporządzeniu | 12. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 12. roku życia |
| 4. Załącznik / lp | zał. 10 lp 10, zał. 10b lp 10 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000010 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1019 – Profilaktyczne świadczenie stomatologiczne dla młodzieży w 13. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1019 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 13. roku życia |
| 3. Nazwa w rozporządzeniu | 13. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 13. roku życia |
| 4. Załącznik / lp | zał. 10 lp 11, zał. 10b lp 11 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000011 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1020 – Profilaktyczne świadczenie stomatologiczne dla młodzieży w 16. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1020 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 16. roku życia |
| 3. Nazwa w rozporządzeniu | 16. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 16. roku życia |
| 4. Załącznik / lp | zał. 10 lp 12, zał. 10b lp 12 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.0000012 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych i ocena stanu tkanek przyzębia przez oznaczenie głębokości kieszonek dziąsłowych (PD), utraty przyczepu łącznotkankowego (CAL) oraz wskaźnika krwawienia (BOP). 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Kwalifikacja do szczególnej opieki stomatologicznej w zakresie podstawowego leczenia stomatologicznego lub specjalistycznego leczenia stomatologicznego. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. 5. Profesjonalna profilaktyka fluorkowa. Dotyczy zębów mlecznych i stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1021 – Profilaktyczne świadczenie stomatologiczne dla młodzieży w 19. roku życia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1021 |
| 2. Nazwa ICD-9 PL 5.91 | Profilaktyczne świadczenie stomatologiczne dla młodzieży w 19. roku życia |
| 3. Nazwa w rozporządzeniu | 19. rok życia Profilaktyczne świadczenie stomatologiczne dla dziecka w 19. roku życia |
| 4. Załącznik / lp | zał. 10 lp 13, zał. 10b lp 13 |
| 5. Grupa wiekowa | <19, <19 (szkoła) |
| 6. Zakres(y) umowy | ['07.0000.218.02'] |
| 7. Kod produktu NFZ | 5.13.00.0000013 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 131 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 10] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych. 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW*. 3. Ocena stanu zdrowia jamy ustnej z uwzględnieniem stanu uzębienia, przyzębia i błony śluzowej jamy ustnej. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. • [zał. 10b] 1. Ocena stanu uzębienia za pomocą wskaźnika intensywności próchnicy PUW* dla zębów stałych. 2. Oddzielne podanie poszczególnych składowych wskaźnika PUW* dla zębów stałych. 3. Ocena stanu zdrowia jamy ustnej z uwzględnieniem stanu uzębienia, przyzębia i błony śluzowej jamy ustnej. 4. Wykrywanie nieprawidłowości (wad) zgryzu według wskaźnika IOTN**: 1) wyraźnego zniekształcenia lub 2) wyraźnego ograniczenia funkcji żucia lub gryzienia oraz wyrzynania zębów. |
| 13. Warunki z zarządzenia | Tylko zakres 07.0000.218.02 |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła) – WYŁĄCZONE dla tego kodu; 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z29.8, Z01.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1101 – Leczenie próchnicy powierzchniowej - za każdy ząb

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1101 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie próchnicy powierzchniowej - za każdy ząb |
| 3. Nazwa w rozporządzeniu | Leczenie próchnicy powierzchniowej – za każdy ząb |
| 4. Załącznik / lp | zał. 1 lp 9, zał. 2 lp 9, zał. 2b lp 9 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2311010 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 6 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje również leczenie próchnicy początkowej. • [zał. 2] Świadczenie obejmuje również leczenie próchnicy początkowej. • [zał. 2b] Świadczenie obejmuje również leczenie próchnicy początkowej. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1105 – Postępowanie przy obnażeniu i skaleczeniu miazgi - bezpośrednie pokrycie miazgi

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1105 |
| 2. Nazwa ICD-9 PL 5.91 | Postępowanie przy obnażeniu i skaleczeniu miazgi - bezpośrednie pokrycie miazgi |
| 3. Nazwa w rozporządzeniu | Postępowanie przy obnażeniu i skaleczeniu miazgi – bezpośrednie pokrycie miazgi |
| 4. Załącznik / lp | zał. 1 lp 10, zał. 2 lp 10, zał. 2b lp 10 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2311050 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 40 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1106 – Opatrunek leczniczy w zębie stałym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1106 |
| 2. Nazwa ICD-9 PL 5.91 | Opatrunek leczniczy w zębie stałym |
| 3. Nazwa w rozporządzeniu | Opatrunek leczniczy w zębie stałym |
| 4. Załącznik / lp | zał. 1 lp 11, zał. 2 lp 11, zał. 2b lp 11 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2311060 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 11 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1107 – Opatrunek leczniczy w zębie mlecznym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1107 |
| 2. Nazwa ICD-9 PL 5.91 | Opatrunek leczniczy w zębie mlecznym |
| 3. Nazwa w rozporządzeniu | Opatrunek leczniczy w zębie mlecznym |
| 4. Załącznik / lp | zał. 1 lp 47, zał. 2 lp 43, zał. 2b lp 43 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2311070 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 14 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1108 – Wypełnienie ubytku korony zęba mlecznego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1108 |
| 2. Nazwa ICD-9 PL 5.91 | Wypełnienie ubytku korony zęba mlecznego |
| 3. Nazwa w rozporządzeniu | Wypełnienie ubytku korony zęba mlecznego |
| 4. Załącznik / lp | zał. 1 lp 53, zał. 2 lp 40, zał. 2b lp 40 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2311080 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 52 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje także opracowanie ubytku zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie obejmuje także opracowanie ubytku zęba. • [zał. 2b] Świadczenie obejmuje także opracowanie ubytku zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-AMALG-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1201 – Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1201 |
| 2. Nazwa ICD-9 PL 5.91 | Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem |
| 3. Nazwa w rozporządzeniu | Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem |
| 4. Załącznik / lp | zał. 1 lp 16, zał. 2 lp 16, zał. 2b lp 16 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2312010 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 30 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1202 – Dewitalizacja miazgi zęba z zaopatrzeniem ubytku opatrunkiem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1202 |
| 2. Nazwa ICD-9 PL 5.91 | Dewitalizacja miazgi zęba z zaopatrzeniem ubytku opatrunkiem |
| 3. Nazwa w rozporządzeniu | Dewitalizacja miazgi zęba z zaopatrzeniem ubytku opatrunkiem |
| 4. Załącznik / lp | zał. 1 lp 17, zał. 2 lp 17, zał. 2b lp 17 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2312020 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 36 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1203 – Amputacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1203 |
| 2. Nazwa ICD-9 PL 5.91 | Amputacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem |
| 3. Nazwa w rozporządzeniu | Amputacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem |
| 4. Załącznik / lp | zał. 1 lp 48, zał. 2 lp 44, zał. 2b lp 44 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 50 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1204 – Amputacja przyżyciowa miazgi

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1204 |
| 2. Nazwa ICD-9 PL 5.91 | Amputacja przyżyciowa miazgi |
| 3. Nazwa w rozporządzeniu | Amputacja przyżyciowa miazgi |
| 4. Załącznik / lp | zał. 1 lp 49, zał. 2 lp 45, zał. 2b lp 45 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 50 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane w udokumentowanych przypadkach. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie jest udzielane w udokumentowanych przypadkach. • [zał. 2b] Świadczenie jest udzielane w udokumentowanych przypadkach. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Świadczenie „w udokumentowanych przypadkach” – wymagany opis uzasadnienia. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-1204-DOK |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1205 – Ekstyrpacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1205 |
| 2. Nazwa ICD-9 PL 5.91 | Ekstyrpacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem |
| 3. Nazwa w rozporządzeniu | Ekstyrpacja przyżyciowa miazgi w zębie z nieuformowanym korzeniem |
| 4. Załącznik / lp | zał. 1 lp 50, zał. 2 lp 46, zał. 2b lp 46 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 80 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1206 – Ekstyrpacja przyżyciowa miazgi

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1206 |
| 2. Nazwa ICD-9 PL 5.91 | Ekstyrpacja przyżyciowa miazgi |
| 3. Nazwa w rozporządzeniu | Ekstyrpacja przyżyciowa miazgi |
| 4. Załącznik / lp | zał. 1 lp 18, zał. 2 lp 18, zał. 2b lp 18 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2312060 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 70 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1208 – Ekstyrpacja zdewitalizowanej miazgi zęba z nieuformowanym korzeniem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1208 |
| 2. Nazwa ICD-9 PL 5.91 | Ekstyrpacja zdewitalizowanej miazgi zęba z nieuformowanym korzeniem |
| 3. Nazwa w rozporządzeniu | Ekstyrpacja zdewitalizowanej miazgi zęba z nieuformowanym korzeniem |
| 4. Załącznik / lp | zał. 1 lp 51, zał. 2 lp 47, zał. 2b lp 47 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 60 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1209 – Ekstyrpacja zdewitalizowanej miazgi zęba

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1209 |
| 2. Nazwa ICD-9 PL 5.91 | Ekstyrpacja zdewitalizowanej miazgi zęba |
| 3. Nazwa w rozporządzeniu | Ekstyrpacja zdewitalizowanej miazgi zęba |
| 4. Załącznik / lp | zał. 1 lp 19, zał. 2 lp 19, zał. 2b lp 19 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2312090 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 40 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1210 – Amputacja zdewitalizowanej miazgi zęba mlecznego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1210 |
| 2. Nazwa ICD-9 PL 5.91 | Amputacja zdewitalizowanej miazgi zęba mlecznego |
| 3. Nazwa w rozporządzeniu | Amputacja zdewitalizowanej miazgi zęba mlecznego |
| 4. Załącznik / lp | zał. 1 lp 52, zał. 2 lp 48, zał. 2b lp 48 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 40 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje amputację mortalną zęba mlecznego. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie obejmuje amputację mortalną zęba mlecznego. • [zał. 2b] Świadczenie obejmuje amputację mortalną zęba mlecznego. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1306 – Czasowe wypełnienie kanału

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1306 |
| 2. Nazwa ICD-9 PL 5.91 | Czasowe wypełnienie kanału |
| 3. Nazwa w rozporządzeniu | Czasowe wypełnienie kanału |
| 4. Załącznik / lp | zał. 1 lp 20, zał. 2 lp 20, zał. 2b lp 20 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313060 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 30 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1307 – Wypełnienie kanału

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1307 |
| 2. Nazwa ICD-9 PL 5.91 | Wypełnienie kanału |
| 3. Nazwa w rozporządzeniu | Wypełnienie kanału |
| 4. Załącznik / lp | zał. 1 lp 21, zał. 2 lp 21, zał. 2b lp 21 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313070 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 60 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. • [zał. 2] Świadczenie – za każdy kanał. • [zał. 2b] Świadczenie – za każdy kanał. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1308 – Leczenie endodontyczne z wypełnieniem 2 kanałów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1308 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne z wypełnieniem 2 kanałów |
| 3. Nazwa w rozporządzeniu | Leczenie endodontyczne z wypełnieniem 2 kanałów |
| 4. Załącznik / lp | zał. 1 lp 56, zał. 2 lp 49, zał. 2b lp 49 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 200 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia oraz kobietom w ciąży i w okresie połogu. • [zał. 2] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. • [zał. 2b] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1309 – Leczenie endodontyczne z wypełnieniem 3 kanałów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1309 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne z wypełnieniem 3 kanałów |
| 3. Nazwa w rozporządzeniu | Leczenie endodontyczne z wypełnieniem 3 kanałów |
| 4. Załącznik / lp | zał. 1 lp 57, zał. 2 lp 50, zał. 2b lp 50 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 250 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia oraz kobietom w ciąży i w okresie połogu. • [zał. 2] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. • [zał. 2b] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1311 – Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1311 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi |
| 3. Nazwa w rozporządzeniu | Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi / Leczenie endodontyczne zęba z wypełnieniem kanału ze zgorzelą miazgi |
| 4. Załącznik / lp | zał. 1 lp 22, zał. 2 lp 22, zał. 2b lp 22 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313110 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 200 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. • [zał. 2] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. • [zał. 2b] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1312 – Leczenie endodontyczne zęba z wypełnieniem 2 kanałów ze zgorzelą miazgi

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1312 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z wypełnieniem 2 kanałów ze zgorzelą miazgi |
| 3. Nazwa w rozporządzeniu | Leczenie endodontyczne zęba z wypełnieniem 2 kanałów ze zgorzelą miazgi |
| 4. Załącznik / lp | zał. 1 lp 58, zał. 2 lp 51, zał. 2b lp 51 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 240 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia oraz kobietom w ciąży i w okresie połogu. • [zał. 2] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. • [zał. 2b] Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Część świadczeń endodontycznych liczona per kanał (23.1206, 23.1209, 23.1306, 23.1307, 23.1205, 23.1208); 23.1311/1308/1309/1312 nie obejmują opracowania i odbudowy korony. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.4, K04.5, K04.6, K04.7 |
| 20. Ryzyka kontrolne | R-ENDO-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1314 – Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1314 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA |
| 3. Nazwa w rozporządzeniu | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA: |
| 4. Załącznik / lp | zał. 2b lp 54 |
| 5. Grupa wiekowa | <18 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 2b] Świadczenie jest udzielane przez lekarza dentystę specjalistę w dziedzinie stomatologii dziecięcej lub lekarza specjalistę w dziedzinie stomatologii zachowawczej z endodoncją, lub lekarza |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1502 – Całkowite opracowanie i odbudowa ubytku zęba na 1 powierzchni

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1502 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite opracowanie i odbudowa ubytku zęba na 1 powierzchni |
| 3. Nazwa w rozporządzeniu | Całkowite opracowanie i odbudowa ubytku zęba na 1 powierzchni |
| 4. Załącznik / lp | zał. 1 lp 12, zał. 2 lp 12, zał. 2b lp 12 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315020 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 45 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-AMALG-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1503 – Całkowite opracowanie i odbudowa ubytku na 2 powierzchniach

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1503 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite opracowanie i odbudowa ubytku na 2 powierzchniach |
| 3. Nazwa w rozporządzeniu | Całkowite opracowanie i odbudowa ubytku na 2 powierzchniach |
| 4. Załącznik / lp | zał. 1 lp 13, zał. 2 lp 13, zał. 2b lp 13 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315030 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 54 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-AMALG-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1504 – Całkowite opracowanie i odbudowa rozległego ubytku na 2 powierzchniach

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1504 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite opracowanie i odbudowa rozległego ubytku na 2 powierzchniach |
| 3. Nazwa w rozporządzeniu | Całkowite opracowanie i odbudowa rozległego ubytku na 2 powierzchniach |
| 4. Załącznik / lp | zał. 1 lp 14, zał. 2 lp 14, zał. 2b lp 14 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315040 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 71 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-AMALG-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1505 – Całkowite opracowanie i odbudowa rozległego ubytku na 3 powierzchniach

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1505 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite opracowanie i odbudowa rozległego ubytku na 3 powierzchniach |
| 3. Nazwa w rozporządzeniu | Całkowite opracowanie i odbudowa rozległego ubytku na 3 powierzchniach |
| 4. Załącznik / lp | zał. 1 lp 15, zał. 2 lp 15, zał. 2b lp 15 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315050 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 74 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-AMALG-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1507 – Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1507 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych |
| 3. Nazwa w rozporządzeniu | Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych |
| 4. Załącznik / lp | zał. 1 lp 54, zał. 2 lp 41, zał. 2b lp 41 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315070 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 70 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba. • [zał. 2b] Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1508 – Kosmetyczne pokrycie niedorozwoju szkliwa

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1508 |
| 2. Nazwa ICD-9 PL 5.91 | Kosmetyczne pokrycie niedorozwoju szkliwa |
| 3. Nazwa w rozporządzeniu | Kosmetyczne pokrycie niedorozwoju szkliwa |
| 4. Załącznik / lp | zał. 1 lp 55, zał. 2 lp 42, zał. 2b lp 42 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2315080 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 30 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie dotyczy zębów stałych. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia. • [zał. 2] Świadczenie dotyczy zębów stałych. • [zał. 2b] Świadczenie dotyczy zębów stałych. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K02.0, K02.1, K02.2, K02.3, K02.8, K02.9, K03.0, K03.1, K03.2, S02.5 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1601 – Usunięcie złogów nazębnych z 1/2 łuku zębowego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1601 |
| 2. Nazwa ICD-9 PL 5.91 | Usunięcie złogów nazębnych z 1/2 łuku zębowego |
| 3. Nazwa w rozporządzeniu | Usunięcie złogów nazębnych z 1/2 łuku zębowego |
| 4. Załącznik / lp | zał. 1 lp 23, zał. 2 lp 23, zał. 2b lp 23 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Usunięcie złogów (½ łuku) – 1 raz w roku kalendarzowym w obrębie całego uzębienia (zał. 1 i 2). |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane 1 raz w roku kalendarzowym w obrębie całego uzębienia. • [zał. 2] Świadczenie jest udzielane 1 raz w roku kalendarzowym w obrębie całego uzębienia. • [zał. 2b] Świadczenie jest udzielane raz w roku kalendarzowym w obrębie całego uzębienia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K03.6, K05.1, K05.3 |
| 20. Ryzyka kontrolne | R-ZLOG-01; R-KOD-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ICD9-PL-591`, `SRC-NFZ-KOM-9017`, `SRC-ZARZ-60-2023-TJ`, `SRC-ZARZ-95-2026` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1602 – Usunięcie złogów nazębnych ze wszystkich zębów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1602 |
| 2. Nazwa ICD-9 PL 5.91 | Usunięcie złogów nazębnych ze wszystkich zębów |
| 3. Nazwa w rozporządzeniu | Usunięcie złogów nazębnych ze wszystkich zębów |
| 4. Załącznik / lp | zał. 1 lp 59, zał. 2 lp 52, zał. 2b lp 52 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Usunięcie złogów ze wszystkich zębów – nie częściej niż 1 raz na 6 miesięcy (zał. 2). |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane kobietom w ciąży i w okresie połogu, nie częściej niż 1 raz na 6 miesięcy, w obrębie całego uzębienia. • [zał. 2] Świadczenie jest udzielane nie częściej niż 1 raz na 6 miesięcy w obrębie całego uzębienia. • [zał. 2b] Świadczenie jest udzielane nie częściej niż raz na 6 miesięcy w obrębie całego uzębienia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K03.6, K05.1, K05.3 |
| 20. Ryzyka kontrolne | R-ZLOG-02; R-KOD-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ICD9-PL-591`, `SRC-NFZ-KOM-9017`, `SRC-ZARZ-60-2023-TJ`, `SRC-ZARZ-95-2026` |
| 24. Obowiązuje od / do | 2025-05-13, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1604 – Płukanie kieszonki dziąsłowej i aplikacja leku

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1604 |
| 2. Nazwa ICD-9 PL 5.91 | Płukanie kieszonki dziąsłowej i aplikacja leku |
| 3. Nazwa w rozporządzeniu | Płukanie kieszonki dziąsłowej i aplikacja leku |
| 4. Załącznik / lp | zał. 1 lp 24, zał. 2 lp 24, zał. 2b lp 24 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST04 (lista ST3), ST30 (lista ST4) |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje każdą wizytę. • [zał. 2] Świadczenie obejmuje każdą wizytę. • [zał. 2b] Świadczenie obejmuje każdą wizytę. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1605 – Leczenie zmian na błonie śluzowej jamy ustnej

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1605 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie zmian na błonie śluzowej jamy ustnej |
| 3. Nazwa w rozporządzeniu | Leczenie zmian na błonie śluzowej jamy ustnej |
| 4. Załącznik / lp | zał. 1 lp 25, zał. 2 lp 25, zał. 2b lp 25 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST26 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje każdą wizytę. • [zał. 2] Świadczenie obejmuje każdą wizytę. • [zał. 2b] Świadczenie obejmuje każdą wizytę. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1607 – Kiretaż zwykły w obrębie 1/4 uzębienia

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1607 |
| 2. Nazwa ICD-9 PL 5.91 | Kiretaż zwykły w obrębie 1/4 uzębienia |
| 3. Nazwa w rozporządzeniu | Kiretaż zwykły (zamknięty) w obrębie 1/4 uzębienia |
| 4. Załącznik / lp | zał. 1 lp 26, zał. 2 lp 26, zał. 2b lp 26 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST04 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje odpowiedniego znieczulenia i opatrunku. • [zał. 2] Świadczenie nie obejmuje odpowiedniego znieczulenia i opatrunku. • [zał. 2b] Świadczenie nie obejmuje odpowiedniego znieczulenia i opatrunku. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K05.3, K05.2 |
| 20. Ryzyka kontrolne | R-ZNI-02; R-KIR-DZ |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-NFZ-KOM-KIRETAZ-DZ`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2026-07-22, 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1615 – Unieruchomienie zębów ligaturą drucianą

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1615 |
| 2. Nazwa ICD-9 PL 5.91 | Unieruchomienie zębów ligaturą drucianą |
| 3. Nazwa w rozporządzeniu | Unieruchomienie zębów ligaturą drucianą |
| 4. Załącznik / lp | zał. 1 lp 27, zał. 2 lp 27, zał. 2b lp 27 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1701 – Usunięcie zęba jednokorzeniowego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1701 |
| 2. Nazwa ICD-9 PL 5.91 | Usunięcie zęba jednokorzeniowego |
| 3. Nazwa w rozporządzeniu | Usunięcie zęba jednokorzeniowego |
| 4. Załącznik / lp | zał. 1 lp 28, zał. 2 lp 28, zał. 2b lp 28 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST01 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2b] Świadczenie nie obejmuje odpowiedniego znieczulenia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.1, K04.5, K04.7, K02.9, K05.3, K08.3, K01.1, S02.5, K07.3 |
| 20. Ryzyka kontrolne | R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1702 – Usunięcie zęba wielokorzeniowego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1702 |
| 2. Nazwa ICD-9 PL 5.91 | Usunięcie zęba wielokorzeniowego |
| 3. Nazwa w rozporządzeniu | Usunięcie zęba wielokorzeniowego |
| 4. Załącznik / lp | zał. 1 lp 29, zał. 2 lp 29, zał. 2b lp 29 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST02 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2b] Świadczenie nie obejmuje odpowiedniego znieczulenia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.1, K04.5, K04.7, K02.9, K05.3, K08.3, K01.1, S02.5, K07.3 |
| 20. Ryzyka kontrolne | R-ZNI-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2026-09-01 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1809 – Chirurgiczne zaopatrzenie małej rany obejmującej do 3 zębodołów włącznie ze szwem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1809 |
| 2. Nazwa ICD-9 PL 5.91 | Chirurgiczne zaopatrzenie małej rany obejmującej do 3 zębodołów włącznie ze szwem |
| 3. Nazwa w rozporządzeniu | Chirurgiczne zaopatrzenie małej rany obejmującej do 3 zębodołów włącznie ze szwem |
| 4. Załącznik / lp | zał. 1 lp 31, zał. 2 lp 31, zał. 2b lp 31 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST01 (lista ST2), ST04 (lista ST2), ST27 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.1815 – Założenie opatrunku chirurgicznego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.1815 |
| 2. Nazwa ICD-9 PL 5.91 | Założenie opatrunku chirurgicznego |
| 3. Nazwa w rozporządzeniu | Założenie opatrunku chirurgicznego |
| 4. Załącznik / lp | zał. 1 lp 32, zał. 2 lp 32, zał. 2b lp 32 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | ST01 (lista ST2), ST04 (lista ST2), ST26, ST31 |
| 9. Punkty (zał. 1b) | NIE DOTYCZY (rozliczenie w pakiecie) |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2001 – Nacięcie powierzchniowo, podśluzówkowo lub podskórnie leżącego ropnia włącznie z drenażem i opatrunkiem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2001 |
| 2. Nazwa ICD-9 PL 5.91 | Nacięcie powierzchniowo, podśluzówkowo lub podskórnie leżącego ropnia włącznie z drenażem i opatrunkiem |
| 3. Nazwa w rozporządzeniu | Nacięcie powierzchniowo, podśluzówkowo lub podskórnie leżącego ropnia włącznie z drenażem i opatrunkiem / Nacięcie powierzchniowo, podśluzówkowo lub podskórnie leżącego ropnia, włącznie z drenażem i opatrunkiem |
| 4. Załącznik / lp | zał. 1 lp 33, zał. 2 lp 33, zał. 2b lp 33 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2] Świadczenie nie obejmuje odpowiedniego znieczulenia. • [zał. 2b] Świadczenie nie obejmuje odpowiedniego znieczulenia. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2101 – Repozycja i unieruchomienie zwichniętego zęba lub grupy zębów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2101 |
| 2. Nazwa ICD-9 PL 5.91 | Repozycja i unieruchomienie zwichniętego zęba lub grupy zębów |
| 3. Nazwa w rozporządzeniu | Repozycja i unieruchomienie zwichniętego zęba lub grupy zębów – włącznie z prostym umocowaniem do zębów sąsiednich |
| 4. Załącznik / lp | zał. 1 lp 6511), zał. 2 lp 5814), zał. 2b lp 5820) |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2205 – Tymczasowe zaopatrzenie złamanej szczęki lub szczęk

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2205 |
| 2. Nazwa ICD-9 PL 5.91 | Tymczasowe zaopatrzenie złamanej szczęki lub szczęk |
| 3. Nazwa w rozporządzeniu | Tymczasowe zaopatrzenie złamanej szczęki lub szczęk |
| 4. Załącznik / lp | zał. 1 lp 34, zał. 2 lp 34, zał. 2b lp 34 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje tymczasowe zaopatrzenie złamanej szczęki lub żuchwy. • [zał. 2] Świadczenie obejmuje tymczasowe zaopatrzenie złamanej szczęki lub żuchwy. • [zał. 2b] Świadczenie obejmuje tymczasowe zaopatrzenie złamanej szczęki lub żuchwy. |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2209 – Zdjęcie jednej szyny przy wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2209 |
| 2. Nazwa ICD-9 PL 5.91 | Zdjęcie jednej szyny przy wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk |
| 3. Nazwa w rozporządzeniu | 5920) Zdjęcie jednej szyny przy wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk / Zdjęcie jednej szyny przy wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk |
| 4. Załącznik / lp | zał. 1 lp 6611), zał. 2 lp 5914), zał. 2b lp 5920) Zdjęcie jednej szyny przy 23.2209 wymianie unieruchomienia lub zakończeniu leczenia zachowawczego złamania szczęk Tabela nr 2 Warunki realizacji świadczeń ogólnostomatologicznych dla dzieci i młodzieży do ukończenia 18. roku życia udzielanych w gabinecie dentystycznym zlokalizowanym w szkole 1 Personel Lekarz dentysta lub lekarz dentysta w trakcie specjalizacji w dziedzinie stomatologii dziecięcej, lub lekarz dentysta specjalista 1.1 w dziedzinie stomatologii dziecięcej 2 Miejsce udzielania świadczeń 2.1 Gabinet dentystyczny zlokalizowany w szkole 3 Sprzęt i wyposażenie Stanowisko stomatologiczne (fotel, przystawka turbinowa, mikrosilnik, lampa bezcieniowa) lub unit stomatologiczny – w miejscu 3.1 udzielania świadczeń 3.2 Lampa polimeryzacyjna – w miejscu udzielania świadczeń 3.3 Skaler – w miejscu udzielania świadczeń 3.421) Wstrząsarka do materiałów kapsułkowanych stosowanych do wypełniania ubytków § w miejscu udzielania świadczeń 21) |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2210 – Repozycja i unieruchomienie zwichnięcia żuchwy

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2210 |
| 2. Nazwa ICD-9 PL 5.91 | Repozycja i unieruchomienie zwichnięcia żuchwy |
| 3. Nazwa w rozporządzeniu | Repozycja i unieruchomienie zwichnięcia żuchwy |
| 4. Załącznik / lp | zał. 1 lp 35, zał. 2 lp 35, zał. 2b lp 35 |
| 5. Grupa wiekowa | <18, <18 (szkoła), wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w zał. 1b (rozliczane w pakiecie lub w innym zakresie) – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | WYMAGA WERYFIKACJI |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | WYMAGA WERYFIKACJI |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | WYMAGA WERYFIKACJI |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2302 – Wycisk jednej szczęki dla diagnozy, planowania i kontroli

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2302 |
| 2. Nazwa ICD-9 PL 5.91 | Wycisk jednej szczęki dla diagnozy, planowania i kontroli |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 18 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2306 – Analiza telerentgenogramu

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2306 |
| 2. Nazwa ICD-9 PL 5.91 | Analiza telerentgenogramu |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 30 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2307 – Wykonanie zgryzu konstrukcyjnego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2307 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie zgryzu konstrukcyjnego |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 33 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2308 – Korekcyjne szlifowanie zębów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2308 |
| 2. Nazwa ICD-9 PL 5.91 | Korekcyjne szlifowanie zębów |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 30 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2310 – Utrzymywacz przestrzeni jako samodzielne postępowanie

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2310 |
| 2. Nazwa ICD-9 PL 5.91 | Utrzymywacz przestrzeni jako samodzielne postępowanie |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 110 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2312 – Środki do wprowadzenia pojedynczego przemieszczonego zęba do łuku, po chirurgicznym jego odsłonięciu

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2312 |
| 2. Nazwa ICD-9 PL 5.91 | Środki do wprowadzenia pojedynczego przemieszczonego zęba do łuku, po chirurgicznym jego odsłonięciu |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 50 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2401 – Leczenie aparatem ortodontycznym ruchomym, jednoszczękowym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2401 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie aparatem ortodontycznym ruchomym, jednoszczękowym |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 450 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2402 – Leczenie aparatem ortodontycznym ruchomym, dwuszczękowym nieelastycznym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2402 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie aparatem ortodontycznym ruchomym, dwuszczękowym nieelastycznym |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 600 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2406 – Kontrola przebiegu leczenia z aparatem ruchomym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2406 |
| 2. Nazwa ICD-9 PL 5.91 | Kontrola przebiegu leczenia z aparatem ruchomym |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 22 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2502 – Naprawa aparatu z wyciskiem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2502 |
| 2. Nazwa ICD-9 PL 5.91 | Naprawa aparatu z wyciskiem |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 60 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2503 – Rekonstrukcja aparatu ruchomego przy pacjencie w niewielkim zakresie

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2503 |
| 2. Nazwa ICD-9 PL 5.91 | Rekonstrukcja aparatu ruchomego przy pacjencie w niewielkim zakresie |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2325040 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 33 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | Kod produktu 2325040 przy ICD-9 23.2503 – zweryfikować |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2611 – Proteza dziecięca częściowa

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2611 |
| 2. Nazwa ICD-9 PL 5.91 | Proteza dziecięca częściowa |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 420 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.2612 – Proteza dziecięca całkowita

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.2612 |
| 2. Nazwa ICD-9 PL 5.91 | Proteza dziecięca całkowita |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 536 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.0, K07.1, K07.2, K07.3, K07.4, Z46.4 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3102 – Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie 5-8 brakujących zębów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3102 |
| 2. Nazwa ICD-9 PL 5.91 | Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie 5-8 brakujących zębów |
| 3. Nazwa w rozporządzeniu | Uzupełnienie braków zębowych za pomocą protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie 5–8 brakujących zębów |
| 4. Załącznik / lp | zał. 1 lp 36 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2331020 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 470 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje uzupełnienie za pomocą ruchomej protezy akrylowej częściowej z zastosowaniem elementów doginanych utrzymujących lub podpierających w liczbie według wskazań indywidualnych 1 raz na 5 lat w zakresie 5–8 brakujących zębów w 1 łuku zębowym (ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki). |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-03 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3103 – Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie więcej niż 8 zębów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3103 |
| 2. Nazwa ICD-9 PL 5.91 | Uzupełnienie braków zębowych przy pomocy protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie więcej niż 8 zębów |
| 3. Nazwa w rozporządzeniu | Uzupełnienie braków zębowych za pomocą protezy częściowej włącznie z prostymi doginanymi klamrami w zakresie więcej niż 8 zębów |
| 4. Załącznik / lp | zał. 1 lp 37 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2331030 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 470 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje uzupełnienie za pomocą ruchomej protezy akrylowej częściowej z zastosowaniem elementów doginanych utrzymujących lub podpierających w liczbie według wskazań indywidualnych 1 raz na 5 lat w zakresie większym niż 8 brakujących zębów w 1 łuku zębowym (ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki). |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-03 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3104 – Zaopatrzenie bezzębnej szczęki protezą całkowitą w szczęce

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3104 |
| 2. Nazwa ICD-9 PL 5.91 | Zaopatrzenie bezzębnej szczęki protezą całkowitą w szczęce |
| 3. Nazwa w rozporządzeniu | Zaopatrzenie bezzębnej szczęki protezą całkowitą w szczęce |
| 4. Załącznik / lp | zał. 1 lp 38 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 536 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | 1 raz na 5 lat (nie dotyczy pacjentów po leczeniu onkologicznym). |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje zaopatrzenie za pomocą protezy akrylowej całkowitej w szczęce łącznie z pobraniem wycisku czynnościowego na łyżce indywidualnej 1 raz na 5 lat (ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki). |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-01; R-PROT-03 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06, 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3104a – Proteza całkowita górna o charakterze overdenture oparta na zabezpieczonych korzeniach

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3104a |
| 2. Nazwa ICD-9 PL 5.91 | brak w 5.91 – wariant NFZ / rozdz. 87 |
| 3. Nazwa w rozporządzeniu | Proteza całkowita górna o charakterze overdenture oparta na zabezpieczonych korzeniach |
| 4. Załącznik / lp | zał. 1 lp 6711) |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2331041 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 1036 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje zaopatrzenie za pomocą protezy akrylowej całkowitej w szczęce 1 raz na 5 lat na zabezpieczonych korzeniach zębów uprzednio prawidłowo przeleczonych endodontycznie (procedura 23.1502), które nie wymagają usunięcia i mogą służyć jako podparcie dla protezy. Ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki. |
| 13. Warunki z zarządzenia | Overdenture |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-03; R-PROT-04; R-KOD-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ICD9-PL-591`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06 / do odwołania |
| 25. Uwagi dla aplikacji | Brak kodu w 5.91 – nie eksportować bez potwierdzenia OW NFZ |

## 23.3105 – Zaopatrzenie bezzębnej szczęki protezą całkowitą w żuchwie

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3105 |
| 2. Nazwa ICD-9 PL 5.91 | Zaopatrzenie bezzębnej szczęki protezą całkowitą w żuchwie |
| 3. Nazwa w rozporządzeniu | Zaopatrzenie bezzębnej szczęki protezą całkowitą w żuchwie |
| 4. Załącznik / lp | zał. 1 lp 39 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 536 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | 1 raz na 5 lat (nie dotyczy pacjentów po leczeniu onkologicznym). |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje zaopatrzenie za pomocą protezy akrylowej całkowitej w żuchwie łącznie z pobraniem wycisku czynnościowego na łyżce indywidualnej 1 raz na 5 lat (ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki). |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-01; R-PROT-03 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06, 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3105a – Proteza całkowita dolna o charakterze overdenture oparta na zabezpieczonych korzeniach

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3105a |
| 2. Nazwa ICD-9 PL 5.91 | brak w 5.91 – wariant NFZ / rozdz. 87 |
| 3. Nazwa w rozporządzeniu | Proteza całkowita dolna o charakterze overdenture oparta na zabezpieczonych korzeniach |
| 4. Załącznik / lp | zał. 1 lp 6811) |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2331051 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 1036 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje zaopatrzenie za pomocą protezy akrylowej całkowitej w żuchwie 1 raz na 5 lat na zabezpieczonych korzeniach zębów uprzednio prawidłowo przeleczonych endodontycznie (procedura 23.1502), które nie wymagają usunięcia i mogą służyć jako wsparcie dla protezy. Ograniczenie nie dotyczy osób po operacyjnym usunięciu nowotworów w obrębie twarzoczaszki. |
| 13. Warunki z zarządzenia | Overdenture |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Pisemne oświadczenie pacjenta o uprawnieniu dołączone do dokumentacji; odbiór protezy potwierdzony podpisem pacjenta na zleceniu (zał. 3 zarządzenia). |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-03; R-PROT-04; R-KOD-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ICD9-PL-591`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2023-04-06 / do odwołania |
| 25. Uwagi dla aplikacji | Brak kodu w 5.91 – nie eksportować bez potwierdzenia OW NFZ |

## 23.3112 – Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) w większym zakresie z wyciskiem

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3112 |
| 2. Nazwa ICD-9 PL 5.91 | Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) w większym zakresie z wyciskiem |
| 3. Nazwa w rozporządzeniu | Czynności dla odtworzenia funkcji lub poszerzenia zakresu ruchomej protezy (naprawy) w większym zakresie z wyciskiem |
| 4. Załącznik / lp | zał. 1 lp 40 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 172 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Naprawa z wyciskiem – 1×/2 lata; podścielenie – 1×/2 lata. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie obejmuje odtworzenie funkcji żucia przez naprawę protez ruchomych w większym zakresie z wyciskiem, 1 raz na 2 lata. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | patrz pole 12 („Świadczenie obejmuje…”) |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3116 – Całkowite podścielenie jednej protezy w sposób pośredni, włącznie z ukształtowaniem obrzeża - dla szczęki

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3116 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite podścielenie jednej protezy w sposób pośredni, włącznie z ukształtowaniem obrzeża - dla szczęki |
| 3. Nazwa w rozporządzeniu | Całkowite podścielenie jednej protezy w sposób pośredni, włącznie z ukształtowaniem obrzeża – dla szczęki |
| 4. Załącznik / lp | zał. 1 lp 41 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 240 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Naprawa z wyciskiem – 1×/2 lata; podścielenie – 1×/2 lata. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane 1 raz na 2 lata. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3117 – Całkowite podścielenie jednej protezy w sposób pośredni włącznie z czynnościowym ukształtowaniem obrzeża -dla żuchwy

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3117 |
| 2. Nazwa ICD-9 PL 5.91 | Całkowite podścielenie jednej protezy w sposób pośredni włącznie z czynnościowym ukształtowaniem obrzeża -dla żuchwy |
| 3. Nazwa w rozporządzeniu | Całkowite podścielenie jednej protezy w sposób pośredni, włącznie z czynnościowym ukształtowaniem obrzeża – dla żuchwy |
| 4. Załącznik / lp | zał. 1 lp 42 |
| 5. Grupa wiekowa | wszyscy |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 240 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | Naprawa z wyciskiem – 1×/2 lata; podścielenie – 1×/2 lata. |
| 12. Warunki z rozporządzenia (tekst) | [zał. 1] Świadczenie jest udzielane 1 raz na 2 lata. |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-PROT-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | CZĘŚCIOWO POTWIERDZONA |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3118 – Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównanie lub zamknięcie defektów w obrębie szczęki przy istniejącym uzębieniu resztkowym

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3118 |
| 2. Nazwa ICD-9 PL 5.91 | Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównanie lub zamknięcie defektów w obrębie szczęki przy istniejącym uzębieniu resztkowym |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 200 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3119 – Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównania lub zamknięcia defektów w obrębie bezzębnej szczęki

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3119 |
| 2. Nazwa ICD-9 PL 5.91 | Czynności dla uzupełnienia brakujących tkanek miękkich, wyrównania lub zamknięcia defektów w obrębie bezzębnej szczęki |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 200 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3120 – Wykonanie obturatora dla zamknięcia podniebienia miękkiego

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3120 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie obturatora dla zamknięcia podniebienia miękkiego |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 450 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3121 – Wykonanie tymczasowej protezy poresekcyjnej wypełniającej ubytki po resekcji lub uzupełniającej duże defekty szczęki

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3121 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie tymczasowej protezy poresekcyjnej wypełniającej ubytki po resekcji lub uzupełniającej duże defekty szczęki |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 400 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3122 – Wykonanie protezy poresekcyjnej ostatecznej

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3122 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie protezy poresekcyjnej ostatecznej |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 624 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3123 – Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy w mniejszym zakresie

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3123 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy w mniejszym zakresie |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 624 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.3124 – Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy o większym zakresie

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.3124 |
| 2. Nazwa ICD-9 PL 5.91 | Wykonanie protezy lub epitezy dla uzupełnienia zewnątrzustrojowych defektów części miękkich lub dla uzupełnienia brakujących części twarzy o większym zakresie |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | brak w odczycie zał. 1b – WYMAGA WERYFIKACJI |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 960 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | Z46.3, K08.1, K08.2 |
| 20. Ryzyka kontrolne | R-DOK-01 (zgodność z dokumentacją) |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.13141 – Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 1 kanału

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.13141 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 1 kanału |
| 3. Nazwa w rozporządzeniu | 1) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 1 kanału; |
| 4. Załącznik / lp | zał. 2b lp  |
| 5. Grupa wiekowa | <18 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313141 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 200 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | [zał. 2b] dentystę w trakcie specjalizacji w dziedzinie stomatologii dziecięcej lub stomatologii zachowawczej z endodoncją. Wyposażenie niezbędne do realizacji świadczenia: 1) endometr w miejscu udzielania świadczeń; 2) aparat RTG do zdjęć zębowych lub radiowizjografia w lokalizacji lub w dostępie. |
| 13. Warunki z zarządzenia | Wiersz z przesuniętą komórką w XML – punkty odczytane ręcznie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.5, K02.5 |
| 20. Ryzyka kontrolne | R-MTA-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.13142 – Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 2 kanałów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.13142 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 2 kanałów |
| 3. Nazwa w rozporządzeniu | 2) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 2 kanałów; |
| 4. Załącznik / lp | zał. 2b lp  |
| 5. Grupa wiekowa | <18 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2314142 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 400 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | Kod produktu 2314142 (nie 2313142?) – zweryfikować; wiersz z przesuniętą komórką |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.5, K02.5 |
| 20. Ryzyka kontrolne | R-MTA-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.13143 – Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 3 kanałów

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.13143 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 3 kanałów |
| 3. Nazwa w rozporządzeniu | 3) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA 3 kanałów, |
| 4. Załącznik / lp | zał. 2b lp  |
| 5. Grupa wiekowa | <18 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313143 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 600 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | Wiersz z przesuniętą komórką |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.5, K02.5 |
| 20. Ryzyka kontrolne | R-MTA-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 23.13149 – Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA - inne

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 23.13149 |
| 2. Nazwa ICD-9 PL 5.91 | Leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA - inne |
| 3. Nazwa w rozporządzeniu | 4) leczenie endodontyczne zęba z nieuformowanym korzeniem z zastosowaniem materiału typu MTA – inne. |
| 4. Załącznik / lp | zał. 2b lp  |
| 5. Grupa wiekowa | <18 (szkoła) |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.2313149 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 700 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | WYMAGA WERYFIKACJI |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | WYMAGA WERYFIKACJI |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K04.0, K04.1, K04.5, K02.5 |
| 20. Ryzyka kontrolne | R-MTA-01 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 (t.j. rozporządzenia) / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

## 87.121 – 

| Pole | Wartość |
|---|---|
| 1. Kod ICD-9 | 87.121 |
| 2. Nazwa ICD-9 PL 5.91 | brak w 5.91 – wariant NFZ / rozdz. 87 |
| 3. Nazwa w rozporządzeniu | WYMAGA WERYFIKACJI |
| 4. Załącznik / lp | brak w przeczytanych załącznikach (zał. 2a/3–9/10a nieprzeczytane) |
| 5. Grupa wiekowa | WYMAGA WERYFIKACJI |
| 6. Zakres(y) umowy | WYMAGA WERYFIKACJI |
| 7. Kod produktu NFZ | 5.13.00.8712100 |
| 8. Pakiety, w których występuje | NIE DOTYCZY |
| 9. Punkty (zał. 1b) | 85 |
| 10. Jednostka / lokalizacja | ząb wg ISO 3950 / ½ łuku / łuk – WYMAGA WERYFIKACJI |
| 11. Limit częstotliwości | NIE DOTYCZY |
| 12. Warunki z rozporządzenia (tekst) | WYMAGA WERYFIKACJI |
| 13. Warunki z zarządzenia | brak szczególnych w odczycie |
| 14. Co obejmuje (wliczone) | WYMAGA WERYFIKACJI |
| 15. Z czym nie łączyć | WYMAGA WERYFIKACJI |
| 16. Współczynniki | 1,5 dzieci <18 (zakresy 218/221/dentobus/szkoła); 1,2 ciąża/połóg (218) |
| 17. Wymagane uprawnienia / specjalizacja | WYMAGA WERYFIKACJI |
| 18. Wymagana dokumentacja | Opis zdjęcia musi być wpisany do dokumentacji medycznej. |
| 19. Sugerowane ICD-10 (kliniczne, nie wymóg NFZ) | K07.3, K01.1, K08.3, K04.5, K07.6 |
| 20. Ryzyka kontrolne | R-RTG-02 |
| 21. Komunikaty NFZ / spory | brak znanych sporów |
| 22. Status weryfikacji | WYMAGA WERYFIKACJI |
| 23. Źródła | `SRC-DU-2025-615`, `SRC-ZARZ-60-2023-TJ` |
| 24. Obowiązuje od / do | 2025-05-13 / do odwołania |
| 25. Uwagi dla aplikacji | Reguły z poziomem BLOKADA blokują tylko eksport; opis kliniczny zawsze możliwy |

# Pakiety (zał. 1c / 1d)

| Pakiet | Kod produktu | Pkt | Procedura kierunkowa | Listy | Nie sumuje się z | Limit | Min. czas | Zakresy | Status kodu |
|---|---|---|---|---|---|---|---|---|---|
| ST01 | 5.13.00.7000001 | 93 | 23.1701 | ST1, ST2 (opcj.) | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST02 | 5.13.00.7000002 | 104 | 23.1702 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST03 | 5.13.00.7000003 | 166 | 23.17 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST04 | 5.13.00.7000004 | 130 | 23.1607 | ST1, ST2 (opcj.), ST3 (opcj.) | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST05 | 5.13.00.7000005 | 260 | 23.1608 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST06 | 5.13.00.7000006 | 162 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST07 | 5.13.00.7000007 | 177 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST08 | 5.13.00.7000008 | 138 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST09 | 5.13.00.7000009 | 162 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST10 | 5.13.00.7000010 | 298 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST11 | 5.13.00.7000011 | 269 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST12 | 5.13.00.7000012 | 266 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST13 | 5.13.00.7000013 | 223 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST14 | 5.13.00.7000014 | 266 | 23.1705, 23.1707 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST15 | 5.13.00.7000015 | 220 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST16 | 5.13.00.7000016 | 269 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST17 | 5.13.00.7000017 | 222 | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST18 | 5.13.00.7000018 | 222 | 23.1613, 23.1614 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | ['07.0000.219.02', '07.0000.223.02', '07.0000.220.02'] | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST19 | 5.13.00.7000019 | 86 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST20 | 5.13.00.7000020 | 202 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST21 | 5.13.00.7000021 | 251 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST22 | 5.13.00.7000022 | 91 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST23 | 5.13.00.7000023 | 171 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST24 | 5.13.00.7000024 | 104 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST25 | 5.13.00.7000025 | 218 | WYMAGA WERYFIKACJI | ST1 | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST26 | 5.13.00.7000026 | 51 | 23.1605, 23.1815 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST27 | 5.13.00.7000027 | 95 | 23.1809 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST28 | 5.13.00.7000028 | 96 | 23.0107, 23.02 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST29 | 5.13.00.7000029 | 73 | 23.0105 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST30 | 5.13.00.7000030 | 44 | 23.16012 | ST1 (opcj.), ST4 (opcj.) | 23.1006, ST30A, ST30B, ST30C, ST30D, ST30E, ST30F, ST30G | WYMAGA WERYFIKACJI | 10 min | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST30A | 5.13.00.7000130 | 75 | 23.16022 | NIE DOTYCZY | 23.1006, ST30, ST30B, ST30C, ST30D, ST30E, ST30F, ST30G | WYMAGA WERYFIKACJI | 40 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30B | 5.13.00.7000230 | 44 | 23.16012 | NIE DOTYCZY | 23.1006, ST30, ST30A, ST30C, ST30D, ST30E, ST30F, ST30G | WYMAGA WERYFIKACJI | 10 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30C | 5.13.00.7000330 | 88 | 23.16012 | NIE DOTYCZY | 23.1006, ST30, ST30A, ST30B, ST30D, ST30E, ST30F, ST30G | WYMAGA WERYFIKACJI | 10 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30D | 5.13.00.7000430 | 66 | 23.16011, 23.0101 | ST5 (opcj.) | tylko z: ST30E, 23.1101 | 1×/rok | 15 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30E | 5.13.00.7000530 | 24 | 23.16011 | NIE DOTYCZY | 23.1006, ST30, ST30A, ST30B, ST30C, ST30F, ST30G, ST33, ST33A, ST34, ST34A | 4×/rok (3×/rok gdy w roku wykonano ST30D) | 5 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30F | 5.13.00.7000630 | 138 | 23.16021, 23.0101 | NIE DOTYCZY | tylko z: 23.1101 | 1×/rok | 30 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST30G | 5.13.00.7000730 | 96 | 23.16021 | NIE DOTYCZY | 23.1006, ST30, ST30A, ST30B, ST30C, ST30D, ST30E, ST30F, ST33, ST33A, ST34, ST34A | 1×/rok | 20 min | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST31 | 5.13.00.7000031 | 92 | 23.1815 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST32 | 5.13.00.7000032 | 117 | 23.1620 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST33 | 5.13.00.7000033 | 56 | 23.0101 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST33A | 5.13.00.7000133 | 75 | 23.0101 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | POTWIERDZONA |
| ST34 | 5.13.00.7000034 | 47 | 23.0102 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | CZĘŚCIOWO POTWIERDZONA (wzorzec 5.13.00.70000NN z zał. 1c – sprawdzić znak po znaku) |
| ST34A | 5.13.00.7000134 | 63 | 23.0102 | NIE DOTYCZY | WYMAGA WERYFIKACJI | WYMAGA WERYFIKACJI | NIE DOTYCZY | WYMAGA WERYFIKACJI | POTWIERDZONA |