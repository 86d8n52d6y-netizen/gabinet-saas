# Świadczenia jednostkowe (zał. 1b) w zakładce „NFZ” – do akceptacji Patryka

Stan: 22.11.2026 (etap E4). Źródło punktów: `data/nfz/products.json` → `jednostkowe_zal_1b` (Zarządzenie 44/2025/DSOZ, zał. 1; bez zmian w 95/2026/DSOZ).

**Dziś w zakładce „NFZ”:** te świadczenia są widoczne z punktami, ale **NIE są wliczane do sumy** („zakres umowy do potwierdzenia”).
Liczone są tylko świadczenia jednostkowe, które rozliczasz w Opisach NFZ: 23.1101, 23.1006, 23.1105, 23.1108, 23.1206, 23.1502–23.1505, 23.0401–23.0403.

Jak zatwierdzać (jak przy kartach): po grupie – „Zatwierdzam grupę X” albo numery wyjątków. Zatwierdzone = dopisanie do listy `ZNANE` w `scripts/nfz_pakiety_przegladarka.py` + test.

## Uwagi przed zatwierdzeniem (krytycznie)

1. **Współczynnik ×1,5 ma wyłączenia** (`wspolczynniki` w products.json, WSP-1.5): 23.06 wizyta adaptacyjna, 23.0304 pantomogram, profilaktyka z § 3 ust. 1 pkt 10 (grupa B). Silnik zakładki **nie ma jeszcze tych wyłączeń** – trzeba je dodać razem z zatwierdzeniem grup A i B, inaczej u dziecka NFZ zapłaci mniej, niż pokaże aplikacja (np. pantomogram u 10-latka: NFZ – 74 pkt, a bez wyłączenia aplikacja pokazałaby 111).
2. **Grupa D (protezy)** to osobny zakres umowy (protetyka) – zwykle rozliczana poza zakresem ogólnostomatologicznym; dobrze, żeby trafiała do osobnej pozycji, a nie do sumy wizyty ogólnostomatologicznej.
3. **Zakresy umowy** (`zakresy`) mają w danych status „WYMAGA WERYFIKACJI” – NFZ płaci za świadczenie tylko w zakresie, który masz w umowie gabinetu.

## Grupa A – diagnostyka i profilaktyka (6)
| Kod | Pkt | Nazwa |
|---|---|---|
| 23.0301 | 20 | Rentgenodiagnostyka do 2 zdjęć wewnątrzustnych |
| 23.0304 | 74 | Zdjęcie pantomograficzne z opisem (bez ×1,5) |
| 23.06 | 85 | Wizyta adaptacyjna – pierwsze wizyty małych dzieci (bez ×1,5) |
| 23.1003 | 11 | Lakowanie bruzd – za każdy ząb |
| 23.1004 | 42 | Zabezpieczenie bruzd innymi materiałami |
| 23.1008 | 3 | Impregnacja zębiny |

## Grupa B – profilaktyczne świadczenia dla dzieci i młodzieży (13, § 3 ust. 1 pkt 10 – bez ×1,5)
| Kod | Pkt | Wiek |
|---|---|---|
| 23.1009 | 85 | 6. miesiąc życia |
| 23.1010 | 115 | 9. miesiąc |
| 23.1011 | 115 | 12. miesiąc |
| 23.1012 | 144 | 2. rok życia |
| 23.1013 | 144 | 4. rok |
| 23.1014 | 144 | 5. rok |
| 23.1015 | 144 | 6. rok |
| 23.1016 | 131 | 7. rok |
| 23.1017 | 131 | 10. rok |
| 23.1018 | 131 | 12. rok |
| 23.1019 | 131 | 13. rok |
| 23.1020 | 131 | 16. rok |
| 23.1021 | 131 | 19. rok |

## Grupa C – leczenie miazgi i kanałowe, odbudowa kąta (20)
| Kod | Pkt | Nazwa |
|---|---|---|
| 23.1106 | 11 | Opatrunek leczniczy w zębie stałym |
| 23.1107 | 14 | Opatrunek leczniczy w zębie mlecznym |
| 23.1201 | 30 | Trepanacja martwego zęba z opatrunkiem |
| 23.1202 | 36 | Dewitalizacja miazgi z opatrunkiem |
| 23.1203 | 50 | Amputacja przyżyciowa – ząb z nieuformowanym korzeniem |
| 23.1204 | 50 | Amputacja przyżyciowa miazgi |
| 23.1205 | 80 | Ekstyrpacja przyżyciowa – ząb z nieuformowanym korzeniem |
| 23.1208 | 60 | Ekstyrpacja zdewitalizowanej miazgi – nieuformowany korzeń |
| 23.1209 | 40 | Ekstyrpacja zdewitalizowanej miazgi |
| 23.1306 | 30 | Czasowe wypełnienie kanału |
| 23.1307 | 60 | Wypełnienie kanału |
| 23.1308 | 200 | Leczenie endodontyczne – 2 kanały |
| 23.1309 | 250 | Leczenie endodontyczne – 3 kanały |
| 23.1311 | 200 | Leczenie endodontyczne – 1 kanał, zgorzel |
| 23.1312 | 240 | Leczenie endodontyczne – 2 kanały, zgorzel |
| 23.13141 | 200 | Nieuformowany korzeń z MTA – etap 1 |
| 23.13142 | 400 | Nieuformowany korzeń z MTA – etap 2 |
| 23.13143 | 600 | Nieuformowany korzeń z MTA – etap 3 |
| 23.13149 | 700 | Nieuformowany korzeń z MTA – całość |
| 23.1507 | 70 | Odbudowa zniszczonego kąta w zębach siecznych |

## Grupa D – protetyka (7, osobny zakres umowy)
| Kod | Pkt | Nazwa |
|---|---|---|
| 23.3102 | 470 | Proteza częściowa (szczęka) |
| 23.3103 | 470 | Proteza częściowa (żuchwa) |
| 23.3104 | 536 | Proteza całkowita – szczęka |
| 23.3105 | 536 | Proteza całkowita – żuchwa |
| 23.3112 | 172 | Odtworzenie funkcji / poszerzenie protezy |
| 23.3116 | 240 | Podścielenie protezy (pośrednie) |
| 23.3117 | 240 | Podścielenie protezy (pośrednie, z czynnościami) |

Bez wyceny w danych (nie liczone): 23.0302 (RTG do 5 zdjęć), 23.1314 (kod nadrzędny MTA – rozliczane podkody 23.13141–23.13149).
