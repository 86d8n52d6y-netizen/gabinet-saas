# Katalog B – karty procedur ICD-9

> Plik generowany: `python3 scripts/buduj_docs_bazy.py` z danych w `data/`. Nie edytuj ręcznie – popraw JSON.

Wersja danych: 2026.11.22-1. Kart opracowanych: 21 z 266 (rejestr: `REJESTR_KOMPLETNOSCI.md`). Wymagania NFZ są oddzielone od zaleceń klinicznych; elementy oznaczone podstawą i źródłem.

## 23.1007 – Leczenie nadwrażliwości zębów w obrębie 1/4 łuku zębowego

`PROC-23.1007` · **Leczenie nadwrażliwości zębów (¼ łuku)** · profilaktyka · status: **draft**

Leczenie nadwrażliwości zębów w obrębie ¼ łuku zębowego.

**Na czym polega.** Aplikacja preparatu zamykającego kanaliki zębinowe lub zmniejszającego pobudliwość nerwową na odsłoniętą zębinę. **Cel:** Zmniejszenie bólu zębiny na bodźce.

Wskazania: nadwrażliwość zębiny przy recesjach, abrazji, erozji, po skalingu

**Kwalifikacja** – ocenić: wykluczenie innych przyczyn bólu (próchnica, pęknięcie, nieszczelne wypełnienie, zapalenie miazgi). Wywiad: bodźce wywołujące, dieta (kwasy), technika szczotkowania.

- przeciwwskazanie *wzgledne*: ból z innej przyczyny – leczenie przyczynowe
- rozważ inne postępowanie: pasty odczulające do domu; odbudowa ubytku przy utracie tkanek

**Przygotowanie** – konieczne: oczyszczenie i osuszenie powierzchni; preparat odczulający

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Leczenie nieinwazyjne zmian w szkliwie** – Oczyszczenie powierzchni, osuszenie, aplikacja preparatu remineralizującego / fluorkowego; instruktaż i kontrola aktywności zmiany. *Uwaga: Dotyczy zmian bez ubytku (ICDAS 1–2).* Warianty: infiltracja żywicą (prywatnie).
4. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Wałki ligninowe, ślinociąg (typowe); Preparat do leczenia nadwrażliwości zębiny (konieczne); Preparat fluorkowy (lakier / żel) (alternatywa)

**Kontrola efektu:** reakcja na bodziec (np. dmuchawka) po aplikacji. Dalej: powtórzenie aplikacji; przy braku efektu – inne metody

**Zalecenia pozabiegowe:** Higiena: Miękka szczoteczka, technika bez szorowania; pasta odczulająca.. Ograniczenia: Ograniczyć kwaśne pokarmy i napoje.. Kontrola: Wg lekarza (ocena efektu).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Ćwiartka, zęby i preparat — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **nie**

*Brak w wykazie świadczeń gwarantowanych odczytanym w audycie (zał. 1, 2, 2b, 10, 10b, 10c) – leczenie prywatne albo zakres nieodczytany.*

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K03.8 | Inne określone choroby tkanek twardych zębów | nadwrażliwość zębiny (inne określone choroby tkanek twardych) – do weryfikacji kodu | ocena_kliniczna | nie |
| K03.1 | Abrazja (starcie mechaniczne) zębów | abrazja z nadwrażliwością | ocena_kliniczna | nie |
| K06.0 | Recesja dziąseł | recesja dziąsła z odsłoniętą zębiną | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Zakres (¼ łuku) i preparat — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Leczenie nadwrażliwości zębów: {{POLE-LUK}} – zęby {{POLE-ZEBY}}. Preparat: {{POLE-MATERIAL}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZEBY}}: leczenie nadwrażliwości, {{POLE-MATERIAL}}.

**rozszerzony**

> Leczenie nadwrażliwości zębiny: {{POLE-LUK}} – zęby {{POLE-ZEBY}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Przebieg: {{POLE-PRZEBIEG}}. Preparat: {{POLE-MATERIAL}}. Efekt: {{POLE-WYNIK}}. Zalecenia: {{POLE-ZALECENIA}}.

**Źródła kliniczne:** `SRC-PRAKTYKA`

## 23.1101 – Leczenie próchnicy powierzchniowej - za każdy ząb

`PROC-23.1101` · **Leczenie próchnicy powierzchniowej** · leczenie próchnicy · status: **draft** · kody w Opisach NFZ: 1101

Leczenie próchnicy powierzchniowej (bez opracowania ubytku) – za każdy ząb.

**Na czym polega.** Nieinwazyjne leczenie zmian próchnicowych ograniczonych do szkliwa (bez ubytku): oczyszczenie, aplikacja preparatu remineralizującego / fluorkowego; ewentualne wygładzenie. **Cel:** Zatrzymanie i remineralizacja zmian początkowych.

Wskazania: aktywne zmiany próchnicowe w szkliwie bez ubytku (ICDAS 1–2); demineralizacje (np. po leczeniu ortodontycznym)

**Kwalifikacja** – ocenić: aktywność zmiany; brak ubytku w zębinie (klinicznie / RTG przy zmianach stycznych). Wywiad: dieta, higiena, fluorki.

- przeciwwskazanie *wzgledne*: ubytek w zębinie – wskazana odbudowa
- rozważ inne postępowanie: lakowanie / lakierowanie; kontrola i instruktaż

**Przygotowanie** – konieczne: oczyszczenie powierzchni; preparat remineralizujący / fluorkowy; opcjonalne: izolacja względna

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Leczenie nieinwazyjne zmian w szkliwie** – Oczyszczenie powierzchni, osuszenie, aplikacja preparatu remineralizującego / fluorkowego; instruktaż i kontrola aktywności zmiany. *Uwaga: Dotyczy zmian bez ubytku (ICDAS 1–2).* Warianty: infiltracja żywicą (prywatnie).
4. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Preparat fluorkowy (lakier / żel) (konieczne); Wałki ligninowe, ślinociąg (typowe); Gumki, krążki, pasty polerskie, paski (sytuacyjne)

**Kontrola efektu:** pokrycie zmian preparatem; instruktaż. Dalej: kontrola aktywności zmian na kolejnej wizycie; przy progresji – odbudowa

**Zalecenia pozabiegowe:** Pacjent: Nie jeść i nie pić ok. 30 min po aplikacji (lub wg preparatu).. Higiena: Pasta z fluorem, ograniczenie cukrów między posiłkami.. Kontrola: Wg ryzyka próchnicy (zwykle 3–6 mies.).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Zęby i powierzchnie objęte leczeniem, użyty preparat — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2311010 – 6 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie obejmuje również leczenie próchnicy początkowej.
- zał. 2 (<18): Świadczenie obejmuje również leczenie próchnicy początkowej.
- zał. 2b (<18 (szkoła)): Świadczenie obejmuje również leczenie próchnicy początkowej.

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa | ocena_kliniczna | tak |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – kontrola, leczenie wg aktywności | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [rozliczeniowe] Zęby objęte leczeniem (każdy ząb = świadczenie) — *NFZ*

**Szablony opisu**

**standardowy**

> Leczenie próchnicy powierzchniowej: zęby {{POLE-ZEBY}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Preparat: {{POLE-MATERIAL}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZEBY}}: leczenie próchnicy powierzchniowej, {{POLE-MATERIAL}}.

**rozszerzony**

> Leczenie próchnicy powierzchniowej (bez opracowania ubytku): zęby {{POLE-ZEBY}}, powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Przebieg: {{POLE-PRZEBIEG}}. Preparat: {{POLE-MATERIAL}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-KLIN-EAPD-F-2019` (PMID 31631242); `SRC-KLIN-ADA-F-2013` (PMID 24177407)

## 23.1104 – Postępowanie przy próchnicy głębokiej - pośrednie pokrycie miazgi

`PROC-23.1104` · **Pośrednie pokrycie miazgi** · leczenie próchnicy · status: **draft**

Postępowanie przy próchnicy głębokiej – pośrednie pokrycie miazgi.

**Na czym polega.** Pozostawienie cienkiej warstwy zębiny nad miazgą (selektywne usunięcie próchnicy) i pokrycie jej materiałem biologicznym przed odbudową. **Cel:** Zachowanie żywej miazgi w zębie z głęboką próchnicą.

Wskazania: głęboka próchnica w zębie żywym bez objawów nieodwracalnego zapalenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *bezwzgledne*: objawy nieodwracalnego zapalenia lub martwica miazgi
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
5. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* **W tej procedurze:** selektywne usunięcie próchnicy w okolicy miazgi Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
6. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
7. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
8. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
9. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
10. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: kontrola żywotności i RTG wg decyzji lekarza (np. po 6 i 12 miesiącach)

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Głębokość ubytku, materiał pokrycia, stan miazgi przed i po — *zalecenie kliniczne* (`SRC-KLIN-ESE-VPT-2019` (PMID 30664240))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **nie**

*Brak w wykazie świadczeń gwarantowanych odczytanym w audycie (zał. 1, 2, 2b, 10, 10b, 10c) – leczenie prywatne albo zakres nieodczytany.*

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny – głęboka | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, zawsze przy tej procedurze

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: próchnica głęboka – pośrednie pokrycie miazgi. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}. Izolacja: {{POLE-IZOLACJA}}. Pokrycie: {{POLE-MATERIAL-PODKLAD}}. Odbudowa: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Kontrola: {{POLE-KONTROLA}}.

**skrocony**

> {{POLE-ZAB}}: pośrednie pokrycie miazgi {{POLE-MATERIAL-PODKLAD}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Żywotność przed zabiegiem: {{POLE-ZY-ZIMNO}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Przebieg (selektywne usunięcie próchnicy): {{POLE-PRZEBIEG}}. Pokrycie pośrednie: {{POLE-MATERIAL-PODKLAD}}. Odbudowa: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia: {{POLE-ZALECENIA}}. Kontrola żywotności: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1105 – Postępowanie przy obnażeniu i skaleczeniu miazgi - bezpośrednie pokrycie miazgi

`PROC-23.1105` · **Bezpośrednie pokrycie miazgi** · leczenie próchnicy · status: **draft** · kody w Opisach NFZ: 1105

Postępowanie przy obnażeniu i skaleczeniu miazgi – bezpośrednie pokrycie.

**Na czym polega.** Pokrycie niewielkiego obnażenia żywej miazgi materiałem biologicznym w warunkach izolacji, po uzyskaniu hemostazy. **Cel:** Zachowanie żywej miazgi.

Wskazania: przypadkowe obnażenie zdrowej miazgi; obnażenie w trakcie usuwania próchnicy w zębie bez objawów nieodwracalnego zapalenia; świeże złamanie korony z niewielkim obnażeniem

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *bezwzgledne*: objawy nieodwracalnego zapalenia / martwica
- przeciwwskazanie *wzgledne*: brak kontroli krwawienia
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: izolacja (koferdam zalecany); materiał krzemianowo-wapniowy lub wodorotlenek wapnia; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
3. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
4. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
5. **Bezpośrednie pokrycie miazgi** – Przy niewielkim obnażeniu żywej miazgi w warunkach izolacji: hemostaza (np. podchloryn sodu), pokrycie materiałem krzemianowo-wapniowym (MTA / bioceramika) lub wodorotlenkiem wapnia, szczelne zamknięcie. *Uwaga: Rokowanie zależy od kontroli krwawienia i szczelności; konieczna kontrola żywotności.* Warianty: przy braku kontroli krwawienia – rozważ pulpotomię częściową.
6. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
7. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
8. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
9. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne); Podchloryn sodu (płyn do płukania kanałów) (typowe)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: kontrola żywotności i RTG (np. po 6 i 12 miesiącach); przy objawach nieodwracalnego zapalenia – leczenie endodontyczne

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Wielkość obnażenia, hemostaza, materiał pokrycia — *zalecenie kliniczne* (`SRC-KLIN-ESE-VPT-2019` (PMID 30664240))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2311050 – 40 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny z przypadkowym obnażeniem | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony z obnażeniem miazgi (uraz) | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Materiał pokrycia miazgi — *zalecenie kliniczne*
- [zalecane] Plan kontroli żywotności — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: bezpośrednie pokrycie miazgi. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}. Izolacja: {{POLE-IZOLACJA}}. Materiał pokrycia: {{POLE-MATERIAL-PODKLAD}}. Odbudowa: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Kontrola: {{POLE-KONTROLA}}.

**skrocony**

> {{POLE-ZAB}}: bezpośrednie pokrycie miazgi {{POLE-MATERIAL-PODKLAD}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Przebieg (wielkość obnażenia, hemostaza): {{POLE-PRZEBIEG}}. Pokrycie: {{POLE-MATERIAL-PODKLAD}}. Odbudowa / opatrunek: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia: {{POLE-ZALECENIA}}. Kontrola żywotności: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1106 – Opatrunek leczniczy w zębie stałym

`PROC-23.1106` · **Opatrunek leczniczy – ząb stały** · leczenie próchnicy · status: **draft**

Założenie opatrunku leczniczego w zębie stałym.

**Na czym polega.** Czasowe zamknięcie ubytku materiałem o działaniu leczniczym / ochronnym na okres obserwacji lub między etapami leczenia. **Cel:** Ochrona miazgi, obserwacja objawów, etapowe usuwanie próchnicy.

Wskazania: etapowe usuwanie głębokiej próchnicy; niejednoznaczny stan miazgi – obserwacja; brak czasu na odbudowę ostateczną

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
5. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
6. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
7. **Opatrunek czasowy** – Szczelne zamknięcie ubytku materiałem tymczasowym (np. cement tlenkowo-cynkowy, glasjonomer) do kolejnej wizyty.
8. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wodorotlenek wapnia (pasta / podkład) (typowe); Materiał krzemianowo-wapniowy (MTA / bioceramika) (alternatywa); Materiał do opatrunku tymczasowego (konieczne); Cement glasjonomerowy (alternatywa)

**Kontrola efektu:** szczelność opatrunku; zwarcie. Dalej: ocena objawów na kolejnej wizycie; odbudowa ostateczna lub leczenie miazgi

**Zalecenia pozabiegowe:** Pacjent: Opatrunek jest czasowy – nie gryźć twardych pokarmów stroną leczoną.. Kontakt z gabinetem, gdy: ból samoistny; wypadnięcie opatrunku. Kontrola: Wg planu lekarza (kolejny etap leczenia).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Rodzaj opatrunku i plan kolejnego etapu — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2311060 – 11 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny – głęboka, leczenie etapowe | ocena_kliniczna | tak |
| K04.0 | Zapalenie miazgi | odwracalne zapalenie miazgi – obserwacja (wybór lekarza) | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Plan kolejnego etapu leczenia — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: opatrunek leczniczy. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Materiał: {{POLE-MATERIAL}}. Plan: {{POLE-DECYZJA}}.

**skrocony**

> {{POLE-ZAB}}: opatrunek leczniczy {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}. Przebieg: {{POLE-PRZEBIEG}}. Opatrunek leczniczy: {{POLE-MATERIAL-PODKLAD}}, zamknięcie: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia: {{POLE-ZALECENIA}}. Kolejny etap: {{POLE-DECYZJA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-PRAKTYKA`

## 23.1107 – Opatrunek leczniczy w zębie mlecznym

`PROC-23.1107` · **Opatrunek leczniczy – ząb mleczny** · leczenie próchnicy · status: **draft**

Założenie opatrunku leczniczego w zębie mlecznym.

**Na czym polega.** Czasowe zamknięcie ubytku materiałem o działaniu leczniczym / ochronnym na okres obserwacji lub między etapami leczenia. **Cel:** Ochrona miazgi, obserwacja objawów, etapowe usuwanie próchnicy.

Wskazania: etapowe usuwanie głębokiej próchnicy; niejednoznaczny stan miazgi – obserwacja; brak czasu na odbudowę ostateczną

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
5. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
6. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
7. **Opatrunek czasowy** – Szczelne zamknięcie ubytku materiałem tymczasowym (np. cement tlenkowo-cynkowy, glasjonomer) do kolejnej wizyty.
8. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wodorotlenek wapnia (pasta / podkład) (typowe); Materiał krzemianowo-wapniowy (MTA / bioceramika) (alternatywa); Materiał do opatrunku tymczasowego (konieczne); Cement glasjonomerowy (alternatywa)

**Kontrola efektu:** szczelność opatrunku; zwarcie. Dalej: ocena objawów na kolejnej wizycie; odbudowa ostateczna lub leczenie miazgi

**Zalecenia pozabiegowe:** Pacjent: Opatrunek jest czasowy – nie gryźć twardych pokarmów stroną leczoną.. Kontakt z gabinetem, gdy: ból samoistny; wypadnięcie opatrunku. Kontrola: Wg planu lekarza (kolejny etap leczenia).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Rodzaj opatrunku i plan kolejnego etapu — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2311070 – 14 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia.
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny – głęboka, leczenie etapowe | ocena_kliniczna | tak |
| K04.0 | Zapalenie miazgi | odwracalne zapalenie miazgi – obserwacja (wybór lekarza) | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Plan kolejnego etapu leczenia — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: opatrunek leczniczy. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Materiał: {{POLE-MATERIAL}}. Plan: {{POLE-DECYZJA}}.

**skrocony**

> {{POLE-ZAB}}: opatrunek leczniczy {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}. Przebieg: {{POLE-PRZEBIEG}}. Opatrunek leczniczy: {{POLE-MATERIAL-PODKLAD}}, zamknięcie: {{POLE-MATERIAL}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia: {{POLE-ZALECENIA}}. Kolejny etap: {{POLE-DECYZJA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-PRAKTYKA`; `SRC-KLIN-AAPD-VPT-2017` (PMID 29179355)

## 23.1108 – Wypełnienie ubytku korony zęba mlecznego

`PROC-23.1108` · **Wypełnienie zęba mlecznego** · leczenie próchnicy · status: **draft** · kody w Opisach NFZ: 1108

Wypełnienie ubytku korony zęba mlecznego.

**Na czym polega.** Opracowanie ubytku w zębie mlecznym i wypełnienie (glasjonomer, kompomer, kompozyt). **Cel:** Zatrzymanie próchnicy i utrzymanie zęba mlecznego do fizjologicznej wymiany.

Wskazania: próchnica zębiny w zębie mlecznym; nieszczelne wypełnienie w zębie mlecznym

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: współpraca dziecka (skala Frankla); dolegliwości bólowe, obrzęk, przetoka; czas do fizjologicznej wymiany zęba.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: techniki minimalnie inwazyjne (np. bez wiercenia – tylko przy kontrolowanym ryzyku); leczenie miazgi przy jej zajęciu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: techniki adaptacyjne (pokaż–powiedz–zrób); znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Opiekun pilnuje, by dziecko nie przygryzało znieczulonej wargi / policzka.. Higiena: Szczotkowanie przez opiekuna pastą z fluorem w ilości odpowiedniej do wieku.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Współpraca dziecka — *zalecenie kliniczne* (`SRC-KLIN-EAPD-F-2019` (PMID 31631242))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2311080 – 52 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie obejmuje także opracowanie ubytku zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia.
- zał. 2 (<18): Świadczenie obejmuje także opracowanie ubytku zęba.
- zał. 2b (<18 (szkoła)): Świadczenie obejmuje także opracowanie ubytku zęba.

Reguły: R-AMALG-01

*Świadczenie dla zębów mlecznych.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny w zębie mlecznym | ocena_kliniczna | tak |
| K02.8 | Inna próchnica zębów | próchnica wtórna | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: wypełnienie ubytku zęba mlecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: wypełnienie ubytku zęba mlecznego, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. wypełnienie ubytku zęba mlecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-EAPD-F-2019` (PMID 31631242); `SRC-PRAKTYKA`

## 23.1201 – Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem

`PROC-23.1201` · **Trepanacja martwego zęba** · endodoncja – leczenie miazgi · status: **draft**

Trepanacja martwego zęba z zaopatrzeniem ubytku opatrunkiem.

**Na czym polega.** Otwarcie komory martwego zęba (odbarczenie), wstępne oczyszczenie i zamknięcie opatrunkiem. **Cel:** Odbarczenie i rozpoczęcie leczenia zęba z martwicą miazgi / zapaleniem okołowierzchołkowym.

Wskazania: martwica miazgi z dolegliwościami; ostre zapalenie tkanek okołowierzchołkowych – leczenie doraźne

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
4. **Dostęp do komory** – Usunięcie próchnicy i nieszczelnych wypełnień, otwarcie komory z usunięciem stropu, lokalizacja ujść kanałów. *Uwaga: Przed rozpoczęciem – ocena możliwości szczelnej odbudowy.*
5. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
6. **Wkładka do kanałów i zamknięcie czasowe** – Wodorotlenek wapnia w kanałach między wizytami; szczelny opatrunek czasowy.
7. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Narzędzia endodontyczne ręczne i maszynowe (konieczne); Endometr (typowe); Podchloryn sodu (płyn do płukania kanałów) (konieczne); Roztwór EDTA (typowe); Sączki papierowe (konieczne); Aparat RTG / czujnik, pozycjoner (konieczne); Wodorotlenek wapnia (pasta / podkład) (typowe); Materiał do opatrunku tymczasowego (konieczne)

**Kontrola efektu:** szczelny opatrunek. Dalej: kontynuacja leczenia kanałowego; przy ropniu – nacięcie / drenaż wg wskazań

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Stan po otwarciu (wysięk, krwawienie) — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2312010 – 30 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.1 | Martwica miazgi | martwica miazgi | ocena_kliniczna | tak |
| K04.4 | Ostre zapalenie tkanek okołowierzchołkowych pochodzenia miazgowego | ostre zapalenie tkanek okołowierzchołkowych | ocena_kliniczna | nie |
| K04.7 | Ropień okołowierzchołkowy bez przetoki | ropień okołowierzchołkowy bez przetoki | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: trepanacja martwego zęba z opatrunkiem. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: trepanacja martwego zęba z opatrunkiem; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. trepanacja martwego zęba z opatrunkiem. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-S3-2023` (PMID 37772327); `SRC-KLIN-ESE-2006` (PMID 17180780)

## 23.1204 – Amputacja przyżyciowa miazgi

`PROC-23.1204` · **Amputacja przyżyciowa miazgi (pulpotomia)** · endodoncja – leczenie miazgi · status: **draft**

Amputacja przyżyciowa miazgi w zębie z uformowanym korzeniem.

**Na czym polega.** Usunięcie miazgi koronowej (pulpotomia częściowa lub całkowita) i pokrycie miazgi korzeniowej materiałem krzemianowo-wapniowym. **Cel:** Zachowanie żywej miazgi korzeniowej.

Wskazania: obnażenie miazgi z możliwością kontroli krwawienia; wybrane przypadki zapalenia miazgi zęba stałego (ESE S3: pulpotomia jako opcja)

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *bezwzgledne*: martwica miazgi / zmiana okołowierzchołkowa
- przeciwwskazanie *wzgledne*: brak kontroli krwawienia po amputacji
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
5. **Dostęp do komory** – Usunięcie próchnicy i nieszczelnych wypełnień, otwarcie komory z usunięciem stropu, lokalizacja ujść kanałów. *Uwaga: Przed rozpoczęciem – ocena możliwości szczelnej odbudowy.*
6. **Amputacja miazgi (pulpotomia)** – Usunięcie miazgi koronowej (częściowe lub całkowite), hemostaza, ocena miazgi korzeniowej, pokrycie materiałem krzemianowo-wapniowym, szczelne zamknięcie. *Uwaga: Brak kontroli krwawienia w kilka minut – wskazanie do ekstyrpacji.*
7. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
8. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
9. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
10. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (konieczne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Podchloryn sodu (płyn do płukania kanałów) (typowe); Materiał krzemianowo-wapniowy (MTA / bioceramika) (konieczne); Wodorotlenek wapnia (pasta / podkład) (alternatywa); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa)

**Kontrola efektu:** hemostaza i szczelne zamknięcie. Dalej: kontrola żywotności / objawów i RTG (np. 6 i 12 miesięcy); przy niepowodzeniu – leczenie kanałowe

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Zakres amputacji, czas hemostazy, materiał — *zalecenie kliniczne* (`SRC-KLIN-ESE-S3-2023` (PMID 37772327))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**

- zał. 1 (wszyscy): Świadczenie jest udzielane w udokumentowanych przypadkach. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia.
- zał. 2 (<18): Świadczenie jest udzielane w udokumentowanych przypadkach.
- zał. 2b (<18 (szkoła)): Świadczenie jest udzielane w udokumentowanych przypadkach.

Reguły: R-1204-DOK

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.0 | Zapalenie miazgi | zapalenie miazgi z możliwością zachowania miazgi korzeniowej | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony z obnażeniem miazgi | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: amputacja przyżyciowa miazgi. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: amputacja przyżyciowa miazgi; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. amputacja przyżyciowa miazgi. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-S3-2023` (PMID 37772327); `SRC-KLIN-ESE-VPT-2019` (PMID 30664240)

## 23.1206 – Ekstyrpacja przyżyciowa miazgi

`PROC-23.1206` · **Ekstyrpacja przyżyciowa miazgi** · endodoncja – leczenie miazgi · status: **draft** · kody w Opisach NFZ: 1206

Usunięcie żywej miazgi z komory i kanałów (świadczenie za każdy kanał).

**Na czym polega.** Usunięcie żywej, nieodwracalnie zmienionej miazgi z komory i kanałów w znieczuleniu, opracowanie i dezynfekcja kanałów. **Cel:** Usunięcie źródła bólu i zapobieganie zakażeniu tkanek okołowierzchołkowych.

Wskazania: nieodwracalne zapalenie miazgi; wskazania protetyczne (wkład koronowo-korzeniowy); obnażenie miazgi z niekorzystnym rokowaniem dla jej zachowania

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
5. **Dostęp do komory** – Usunięcie próchnicy i nieszczelnych wypełnień, otwarcie komory z usunięciem stropu, lokalizacja ujść kanałów. *Uwaga: Przed rozpoczęciem – ocena możliwości szczelnej odbudowy.*
6. **Usunięcie miazgi z kanałów** – Usunięcie miazgi z komory i kanałów narzędziami ręcznymi / maszynowymi przy płukaniu.
7. **Ustalenie długości roboczej** – Endometr i/lub RTG z narzędziem w kanale; zapis długości i punktu odniesienia dla każdego kanału. *Uwaga: Opracowanie i wypełnienie zwykle kończy się 0,5–2 mm od wierzchołka radiologicznego.*
8. **Opracowanie chemomechaniczne kanału** – Udrożnienie, opracowanie kanału do ustalonej długości i rozmiaru z obfitym płukaniem. *Uwaga: Zachowanie przebiegu kanału; kontrola drożności.*
9. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
10. **Wkładka do kanałów i zamknięcie czasowe** – Wodorotlenek wapnia w kanałach między wizytami; szczelny opatrunek czasowy. **W tej procedurze:** gdy wypełnienie kanałów planowane na kolejnej wizycie
11. **Wypełnienie kanałów** – Osuszenie, wypełnienie gutaperką z uszczelniaczem (technika zależna od przypadku) do długości roboczej; usunięcie nadmiaru z komory. *Uwaga: Wypełnienie szczelne, bez pustek, na pełnej długości.* **W tej procedurze:** jeśli kanały wypełniane na tej samej wizycie – rozliczyć także wypełnienie kanału
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Narzędzia endodontyczne ręczne i maszynowe (konieczne); Endometr (typowe); Podchloryn sodu (płyn do płukania kanałów) (konieczne); Roztwór EDTA (typowe); Sączki papierowe (konieczne); Aparat RTG / czujnik, pozycjoner (konieczne); Wodorotlenek wapnia (pasta / podkład) (sytuacyjne); Materiał do opatrunku tymczasowego (typowe)

**Kontrola efektu:** RTG końcowe: długość (0,5–2 mm od wierzchołka radiologicznego), szczelność, brak pustek; szczelność zamknięcia korony. Nieprawidłowości: wypełnienie za krótkie / przepchnięte; pustki; perforacja; złamane narzędzie. Dalej: kontrola kliniczna i RTG po co najmniej 1 roku (do 4 lat przy niepełnym gojeniu); przy powikłaniach – skierowanie do endodonty

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Kanały, długości robocze, płyny płuczące — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2312060 – 70 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych.
- zał. 2 (<18): Świadczenie – za każdy kanał.
- zał. 2b (<18 (szkoła)): Świadczenie – za każdy kanał.

Reguły: R-ENDO-DZ

*Moduł Opisy NFZ: II wizyta nie rozlicza 1206 (rozlicza się wypełnienie); znieczulenie rozliczane osobno.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.0 | Zapalenie miazgi | nieodwracalne zapalenie miazgi – rozpoznanie lekarza | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Kanały: nazwa, długość robocza i punkt odniesienia — *zalecenie kliniczne*
- [rozliczeniowe] Liczba kanałów (świadczenie za każdy kanał) — *NFZ*, rozliczenie NFZ
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: ekstyrpacja przyżyciowa miazgi. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: ekstyrpacja przyżyciowa miazgi; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. ekstyrpacja przyżyciowa miazgi. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1301 – Całkowite opracowanie i dezynfekcja kanału

`PROC-23.1301` · **Opracowanie i dezynfekcja kanału** · endodoncja – leczenie kanałowe · status: **draft**

Całkowite opracowanie i dezynfekcja kanału.

**Na czym polega.** Mechaniczne opracowanie kanału do długości roboczej z płukaniem środkami dezynfekcyjnymi. **Cel:** Usunięcie zakażonej tkanki i bakterii z systemu kanałowego.

Wskazania: martwica miazgi; zapalenie okołowierzchołkowe; etap leczenia kanałowego

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
2. **Dostęp do komory** – Usunięcie próchnicy i nieszczelnych wypełnień, otwarcie komory z usunięciem stropu, lokalizacja ujść kanałów. *Uwaga: Przed rozpoczęciem – ocena możliwości szczelnej odbudowy.*
3. **Ustalenie długości roboczej** – Endometr i/lub RTG z narzędziem w kanale; zapis długości i punktu odniesienia dla każdego kanału. *Uwaga: Opracowanie i wypełnienie zwykle kończy się 0,5–2 mm od wierzchołka radiologicznego.*
4. **Opracowanie chemomechaniczne kanału** – Udrożnienie, opracowanie kanału do ustalonej długości i rozmiaru z obfitym płukaniem. *Uwaga: Zachowanie przebiegu kanału; kontrola drożności.*
5. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
6. **Wkładka do kanałów i zamknięcie czasowe** – Wodorotlenek wapnia w kanałach między wizytami; szczelny opatrunek czasowy.
7. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Narzędzia endodontyczne ręczne i maszynowe (konieczne); Endometr (typowe); Podchloryn sodu (płyn do płukania kanałów) (konieczne); Roztwór EDTA (typowe); Sączki papierowe (konieczne); Aparat RTG / czujnik, pozycjoner (konieczne); Wodorotlenek wapnia (pasta / podkład) (typowe); Materiał do opatrunku tymczasowego (typowe)

**Kontrola efektu:** RTG końcowe: długość (0,5–2 mm od wierzchołka radiologicznego), szczelność, brak pustek; szczelność zamknięcia korony. Nieprawidłowości: wypełnienie za krótkie / przepchnięte; pustki; perforacja; złamane narzędzie. Dalej: kontrola kliniczna i RTG po co najmniej 1 roku (do 4 lat przy niepełnym gojeniu); przy powikłaniach – skierowanie do endodonty

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Kanały, długości robocze, płyny — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **nie**

*Brak w wykazie świadczeń gwarantowanych odczytanym w audycie (zał. 1, 2, 2b, 10, 10b, 10c) – leczenie prywatne albo zakres nieodczytany.*

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.1 | Martwica miazgi | martwica miazgi | ocena_kliniczna | nie |
| K04.5 | Przewlekłe zapalenie tkanek okołowierzchołkowych | przewlekłe zapalenie okołowierzchołkowe | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Kanały: nazwa, długość robocza i punkt odniesienia — *zalecenie kliniczne*
- [rozliczeniowe] Liczba kanałów (świadczenie za każdy kanał) — *NFZ*, rozliczenie NFZ
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: opracowanie i dezynfekcja kanałów. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: opracowanie i dezynfekcja kanałów; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. opracowanie i dezynfekcja kanałów. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1306 – Czasowe wypełnienie kanału

`PROC-23.1306` · **Czasowe wypełnienie kanału** · endodoncja – leczenie kanałowe · status: **draft**

Czasowe wypełnienie kanału (wkładka lecznicza).

**Na czym polega.** Wprowadzenie wkładki leczniczej (zwykle wodorotlenek wapnia) do opracowanego kanału i szczelne zamknięcie. **Cel:** Dezynfekcja kanału między wizytami.

Wskazania: leczenie wielowizytowe; wysięk z kanału; ząb z martwicą i zmianą okołowierzchołkową

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
2. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
3. **Wkładka do kanałów i zamknięcie czasowe** – Wodorotlenek wapnia w kanałach między wizytami; szczelny opatrunek czasowy.
4. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Koferdam (płachta, klamry, ramka) (konieczne); Podchloryn sodu (płyn do płukania kanałów) (typowe); Sączki papierowe (konieczne); Wodorotlenek wapnia (pasta / podkład) (konieczne); Materiał do opatrunku tymczasowego (konieczne)

**Kontrola efektu:** szczelne zamknięcie korony. Dalej: wypełnienie ostateczne na kolejnej wizycie (zwykle po 1–2 tygodniach)

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Kanały i rodzaj wkładki — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2313060 – 30 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych.
- zał. 2 (<18): Świadczenie – za każdy kanał.
- zał. 2b (<18 (szkoła)): Świadczenie – za każdy kanał.

Reguły: R-ENDO-DZ

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.1 | Martwica miazgi | martwica miazgi | ocena_kliniczna | tak |
| K04.5 | Przewlekłe zapalenie tkanek okołowierzchołkowych | przewlekłe zapalenie okołowierzchołkowe | ocena_kliniczna | tak |
| K04.6 | Ropień okołowierzchołkowy z przetoką | ropień okołowierzchołkowy z przetoką | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Kanały: nazwa, długość robocza i punkt odniesienia — *zalecenie kliniczne*
- [rozliczeniowe] Liczba kanałów (świadczenie za każdy kanał) — *NFZ*, rozliczenie NFZ

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: czasowe wypełnienie kanałów. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: czasowe wypełnienie kanałów; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. czasowe wypełnienie kanałów. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-2006` (PMID 17180780)

## 23.1307 – Wypełnienie kanału

`PROC-23.1307` · **Wypełnienie kanału** · endodoncja – leczenie kanałowe · status: **draft**

Ostateczne wypełnienie kanału (świadczenie za każdy kanał).

**Na czym polega.** Szczelne wypełnienie opracowanego i zdezynfekowanego kanału gutaperką z uszczelniaczem do długości roboczej. **Cel:** Zapobieganie reinfekcji systemu kanałowego.

Wskazania: kanał opracowany, suchy, bez wysięku, ząb bez ostrych objawów

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
2. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
3. **Wypełnienie kanałów** – Osuszenie, wypełnienie gutaperką z uszczelniaczem (technika zależna od przypadku) do długości roboczej; usunięcie nadmiaru z komory. *Uwaga: Wypełnienie szczelne, bez pustek, na pełnej długości.*
4. **RTG kontrolne** – Zdjęcie po wypełnieniu kanałów – ocena długości, szczelności i kształtu wypełnienia.
5. **Szczelna odbudowa po leczeniu kanałowym** – Jak najszybciej szczelna odbudowa korony (ostatecznie albo trwałe zamknięcie i plan protetyczny – korona przy rozległej utracie tkanek).
6. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Narzędzia endodontyczne ręczne i maszynowe (konieczne); Endometr (typowe); Podchloryn sodu (płyn do płukania kanałów) (konieczne); Roztwór EDTA (typowe); Sączki papierowe (konieczne); Aparat RTG / czujnik, pozycjoner (konieczne); Gutaperka (ćwieki) (konieczne); Uszczelniacz kanałowy (konieczne)

**Kontrola efektu:** RTG końcowe: długość (0,5–2 mm od wierzchołka radiologicznego), szczelność, brak pustek; szczelność zamknięcia korony. Nieprawidłowości: wypełnienie za krótkie / przepchnięte; pustki; perforacja; złamane narzędzie. Dalej: kontrola kliniczna i RTG po co najmniej 1 roku (do 4 lat przy niepełnym gojeniu); przy powikłaniach – skierowanie do endodonty

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Materiał i technika wypełnienia, RTG kontrolne — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2313070 – 60 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie (za każdy kanał) u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych.
- zał. 2 (<18): Świadczenie – za każdy kanał.
- zał. 2b (<18 (szkoła)): Świadczenie – za każdy kanał.

Reguły: R-ENDO-DZ

*Świadczenie za każdy kanał (zał. 1 i 2).*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.0 | Zapalenie miazgi | nieodwracalne zapalenie miazgi – rozpoznanie lekarza | ocena_kliniczna | tak |
| K04.1 | Martwica miazgi | martwica miazgi | ocena_kliniczna | tak |
| K04.4 | Ostre zapalenie tkanek okołowierzchołkowych pochodzenia miazgowego | ostre zapalenie tkanek okołowierzchołkowych | ocena_kliniczna | tak |
| K04.5 | Przewlekłe zapalenie tkanek okołowierzchołkowych | przewlekłe zapalenie okołowierzchołkowe | ocena_kliniczna | tak |
| K04.6 | Ropień okołowierzchołkowy z przetoką | ropień okołowierzchołkowy z przetoką | ocena_kliniczna | tak |
| K04.7 | Ropień okołowierzchołkowy bez przetoki | ropień okołowierzchołkowy bez przetoki | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Kanały: nazwa, długość robocza i punkt odniesienia — *zalecenie kliniczne*
- [rozliczeniowe] Liczba kanałów (świadczenie za każdy kanał) — *NFZ*, rozliczenie NFZ
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: wypełnienie kanałów. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: wypełnienie kanałów; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. wypełnienie kanałów. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1311 – Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi

`PROC-23.1311` · **Leczenie endodontyczne – 1 kanał, zgorzel** · endodoncja – leczenie kanałowe · status: **draft**

Leczenie endodontyczne zęba z wypełnieniem 1 kanału ze zgorzelą miazgi.

**Na czym polega.** Kompletne leczenie kanałowe zęba jednokanałowego z martwicą / zgorzelą miazgi: opracowanie, dezynfekcja (wkładka), wypełnienie. **Cel:** Wyleczenie lub zapobieganie zapaleniu tkanek okołowierzchołkowych.

Wskazania: zgorzel / martwica miazgi; przewlekłe zapalenie okołowierzchołkowe

**Kwalifikacja** – ocenić: rozpoznanie stanu miazgi i tkanek okołowierzchołkowych; RTG przedzabiegowe; możliwość szczelnej odbudowy i rokowanie zęba (przyzębie, pęknięcia). Wywiad: ból, obrzęk, przetoka; choroby ogólne (np. leczenie antyresorpcyjne), alergie.

- przeciwwskazanie *wzgledne*: ząb niemożliwy do odbudowy lub z pionowym złamaniem korzenia
- przeciwwskazanie *wzgledne*: zaawansowana choroba przyzębia zęba – rokowanie złe
- dodatkowa diagnostyka: CBCT – przy złożonej anatomii lub niejasnym obrazie (poza gabinetem)
- rozważ inne postępowanie: ekstrakcja przy złym rokowaniu; skierowanie do endodonty przy przypadkach trudnych

**Przygotowanie** – konieczne: RTG przedzabiegowe; koferdam; zestaw endodontyczny, płyny płuczące; zależne od sytuacji: endometr; powiększenie (lupy / mikroskop). Znieczulenie: Przy żywej miazdze – znieczulenie przewodowe lub nasiękowe; przy martwicy – zwykle niekonieczne lub w mniejszej dawce.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
4. **Dostęp do komory** – Usunięcie próchnicy i nieszczelnych wypełnień, otwarcie komory z usunięciem stropu, lokalizacja ujść kanałów. *Uwaga: Przed rozpoczęciem – ocena możliwości szczelnej odbudowy.*
5. **Ustalenie długości roboczej** – Endometr i/lub RTG z narzędziem w kanale; zapis długości i punktu odniesienia dla każdego kanału. *Uwaga: Opracowanie i wypełnienie zwykle kończy się 0,5–2 mm od wierzchołka radiologicznego.*
6. **Opracowanie chemomechaniczne kanału** – Udrożnienie, opracowanie kanału do ustalonej długości i rozmiaru z obfitym płukaniem. *Uwaga: Zachowanie przebiegu kanału; kontrola drożności.*
7. **Płukanie kanałów** – Podchloryn sodu w trakcie opracowania; na końcu usunięcie warstwy mazistej (np. EDTA) i płukanie końcowe; aktywacja płynu – opcjonalnie. *Uwaga: Unikaj wtłoczenia podchlorynu poza otwór wierzchołkowy.*
8. **Wkładka do kanałów i zamknięcie czasowe** – Wodorotlenek wapnia w kanałach między wizytami; szczelny opatrunek czasowy.
9. **Wypełnienie kanałów** – Osuszenie, wypełnienie gutaperką z uszczelniaczem (technika zależna od przypadku) do długości roboczej; usunięcie nadmiaru z komory. *Uwaga: Wypełnienie szczelne, bez pustek, na pełnej długości.*
10. **RTG kontrolne** – Zdjęcie po wypełnieniu kanałów – ocena długości, szczelności i kształtu wypełnienia.
11. **Szczelna odbudowa po leczeniu kanałowym** – Jak najszybciej szczelna odbudowa korony (ostatecznie albo trwałe zamknięcie i plan protetyczny – korona przy rozległej utracie tkanek).
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Koferdam (płachta, klamry, ramka) (konieczne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Narzędzia endodontyczne ręczne i maszynowe (konieczne); Endometr (typowe); Podchloryn sodu (płyn do płukania kanałów) (konieczne); Roztwór EDTA (typowe); Sączki papierowe (konieczne); Aparat RTG / czujnik, pozycjoner (konieczne); Wodorotlenek wapnia (pasta / podkład) (typowe); Gutaperka (ćwieki) (konieczne); Uszczelniacz kanałowy (konieczne); Materiał do opatrunku tymczasowego (typowe)

**Kontrola efektu:** RTG końcowe: długość (0,5–2 mm od wierzchołka radiologicznego), szczelność, brak pustek; szczelność zamknięcia korony. Nieprawidłowości: wypełnienie za krótkie / przepchnięte; pustki; perforacja; złamane narzędzie. Dalej: kontrola kliniczna i RTG po co najmniej 1 roku (do 4 lat przy niepełnym gojeniu); przy powikłaniach – skierowanie do endodonty

**Zalecenia pozabiegowe:** Pacjent: Dolegliwości przy nagryzaniu przez kilka dni są możliwe; leki przeciwbólowe wg zaleceń.; Nie gryźć twardych pokarmów do czasu ostatecznej odbudowy.. Kontakt z gabinetem, gdy: narastający ból, obrzęk, gorączka; wypadnięcie opatrunku. Kontrola: Odbudowa ostateczna możliwie szybko; kontrola RTG po co najmniej roku (ESE).

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Przebieg leczenia na kolejnych wizytach — *zalecenie kliniczne* (`SRC-KLIN-ESE-2006` (PMID 17180780))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2313110 – 200 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie u dzieci i młodzieży do ukończenia 18. roku życia oraz kobiet w ciąży i w okresie połogu jest udzielane w całym uzębieniu. Świadczenie u osób powyżej 18. roku życia jest udzielane z wyłączeniem zębów przedtrzonowych i trzonowych. Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba.
- zał. 2 (<18): Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba.
- zał. 2b (<18 (szkoła)): Świadczenie nie obejmuje opracowania i odbudowy ubytku korony zęba.

Reguły: R-ENDO-DZ

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K04.1 | Martwica miazgi | martwica miazgi | ocena_kliniczna | tak |
| K04.5 | Przewlekłe zapalenie tkanek okołowierzchołkowych | przewlekłe zapalenie okołowierzchołkowe | ocena_kliniczna | tak |
| K04.6 | Ropień okołowierzchołkowy z przetoką | ropień okołowierzchołkowy z przetoką | ocena_kliniczna | tak |
| K04.7 | Ropień okołowierzchołkowy bez przetoki | ropień okołowierzchołkowy bez przetoki | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Kanały: nazwa, długość robocza i punkt odniesienia — *zalecenie kliniczne*
- [rozliczeniowe] Liczba kanałów (świadczenie za każdy kanał) — *NFZ*, rozliczenie NFZ
- [zalecane] Izolacja koferdamem lub uzasadnienie braku — *zalecenie kliniczne*
- [zalecane] RTG (przed / kontrolne) — *zalecenie kliniczne*

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: leczenie kanałowe zęba ze zgorzelą miazgi. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Kanały i długości robocze: {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Wypełnienie / wkładka: {{POLE-MATERIAL}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}}: leczenie kanałowe zęba ze zgorzelą miazgi; kanały {{POLE-ENDO-KANALY}}; {{POLE-MATERIAL}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}. Izolacja: {{POLE-IZOLACJA}}. leczenie kanałowe zęba ze zgorzelą miazgi. Przebieg: {{POLE-PRZEBIEG}}. Kanały (nazwa, długość robocza, punkt odniesienia, rozmiar): {{POLE-ENDO-KANALY}}. Płukanie: {{POLE-ENDO-PLUKANIE}}. Materiał: {{POLE-MATERIAL}}. Zamknięcie korony: {{POLE-MATERIAL-PODKLAD}}. RTG: {{POLE-RTG}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-2006` (PMID 17180780); `SRC-KLIN-ESE-S3-2023` (PMID 37772327)

## 23.1501 – Odbudowa zniszczonego, złamanego kąta w zębach siecznych

`PROC-23.1501` · **Odbudowa złamanego kąta w zębach siecznych** · odbudowa i estetyka · status: **draft**

Odbudowa zniszczonego lub złamanego kąta korony zęba siecznego.

**Na czym polega.** Odtworzenie kąta siecznego materiałem złożonym (często z kluczem silikonowym). **Cel:** Przywrócenie kształtu, funkcji i estetyki zęba przedniego.

Wskazania: złamanie kąta korony po urazie (bez obnażenia miazgi); zniszczenie kąta przez próchnicę

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: po urazie – badanie BAD-PO-URAZIE, testy żywotności i RTG; ewentualny fragment zęba do przyklejenia
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Przyczyna utraty (uraz / próchnica); przy urazie – plan kontroli żywotności — *zalecenie kliniczne*, warunek: uraz (`SRC-KLIN-IADT-ZLAM-2020` (PMID 32475015))
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **nie**

*Brak w wykazie świadczeń gwarantowanych odczytanym w audycie (zał. 1, 2, 2b, 10, 10b, 10c) – leczenie prywatne albo zakres nieodczytany.*

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| S02.5 | Złamanie zęba | złamanie korony po urazie | ocena_kliniczna | nie |
| K02.1 | Próchnica zębiny | próchnica zębiny niszcząca kąt | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa kąta siecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa kąta siecznego, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa kąta siecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`; `SRC-KLIN-IADT-ZLAM-2020` (PMID 32475015)

## 23.1502 – Całkowite opracowanie i odbudowa ubytku zęba na 1 powierzchni

`PROC-23.1502` · **Odbudowa – 1 powierzchnia** · odbudowa i estetyka · status: **draft** · kody w Opisach NFZ: 1502

Opracowanie ubytku i odbudowa korony zęba stałego na jednej powierzchni.

**Na czym polega.** Usunięcie zmian próchnicowych lub nieszczelnego wypełnienia i odtworzenie jednej powierzchni korony materiałem adhezyjnym lub glasjonomerem. **Cel:** Zatrzymanie procesu próchnicowego, odtworzenie kształtu, funkcji i estetyki zęba, ochrona miazgi. Ubytek próchnicowy w zębinie, wtórna próchnica, nieszczelne lub uszkodzone wypełnienie, ubytek niepróchnicowy lub urazowy wymagający odbudowy.

Wskazania: próchnica zębiny (ICDAS 4–6); próchnica wtórna; nieszczelne / złamane wypełnienie; ubytek niepróchnicowy z dolegliwościami lub zagrożeniem dla zęba; złamanie korony bez obnażenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Powierzchnie odbudowy i materiał — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2315020 – 45 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Reguły: R-AMALG-01

*Rozliczenie wg liczby powierzchni; współczynnik ×1,5 u dzieci do 18 r.ż. (§ 12 ust. 2 zarz. 60/2023/DSOZ) – liczy moduł Opisy NFZ.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa z ubytkiem wymagającym odbudowy – rzadko; zwykle leczenie nieinwazyjne | ocena_kliniczna | tak |
| K02.1 | Próchnica zębiny | próchnica zębiny – typowe wskazanie do opracowania i odbudowy | ocena_kliniczna | tak |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – odbudowa tylko przy ubytku funkcjonalnym / estetycznym | ocena_kliniczna | tak |
| K02.8 | Inna próchnica zębów | inna określona próchnica (np. wtórna przy wypełnieniu) | ocena_kliniczna | tak |
| K03.1 | Abrazja (starcie mechaniczne) zębów | ścieranie mechaniczne (abrazja) – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.2 | Erozja zębów | erozja – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.0 | Nadmierne ścieranie zębów | nadmierne starcie – odbudowa | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony zęba (uraz) – odbudowa | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa jednej powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa jednej powierzchni, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa jednej powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`

## 23.1503 – Całkowite opracowanie i odbudowa ubytku na 2 powierzchniach

`PROC-23.1503` · **Odbudowa – 2 powierzchnie** · odbudowa i estetyka · status: **draft** · kody w Opisach NFZ: 1503

Opracowanie ubytku i odbudowa korony zęba na dwóch powierzchniach.

**Na czym polega.** Usunięcie zmian próchnicowych lub nieszczelnego wypełnienia i odtworzenie dwóch powierzchni korony materiałem adhezyjnym lub glasjonomerem. **Cel:** Zatrzymanie procesu próchnicowego, odtworzenie kształtu, funkcji i estetyki zęba, ochrona miazgi. Ubytek próchnicowy w zębinie, wtórna próchnica, nieszczelne lub uszkodzone wypełnienie, ubytek niepróchnicowy lub urazowy wymagający odbudowy.

Wskazania: próchnica zębiny (ICDAS 4–6); próchnica wtórna; nieszczelne / złamane wypełnienie; ubytek niepróchnicowy z dolegliwościami lub zagrożeniem dla zęba; złamanie korony bez obnażenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Powierzchnie odbudowy i materiał — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2315030 – 54 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Reguły: R-AMALG-01

*Rozliczenie wg liczby powierzchni; współczynnik ×1,5 u dzieci do 18 r.ż. (§ 12 ust. 2 zarz. 60/2023/DSOZ) – liczy moduł Opisy NFZ.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa z ubytkiem wymagającym odbudowy – rzadko; zwykle leczenie nieinwazyjne | ocena_kliniczna | tak |
| K02.1 | Próchnica zębiny | próchnica zębiny – typowe wskazanie do opracowania i odbudowy | ocena_kliniczna | tak |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – odbudowa tylko przy ubytku funkcjonalnym / estetycznym | ocena_kliniczna | tak |
| K02.8 | Inna próchnica zębów | inna określona próchnica (np. wtórna przy wypełnieniu) | ocena_kliniczna | tak |
| K03.1 | Abrazja (starcie mechaniczne) zębów | ścieranie mechaniczne (abrazja) – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.2 | Erozja zębów | erozja – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.0 | Nadmierne ścieranie zębów | nadmierne starcie – odbudowa | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony zęba (uraz) – odbudowa | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa dwóch powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa dwóch powierzchni, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa dwóch powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`

## 23.1504 – Całkowite opracowanie i odbudowa rozległego ubytku na 2 powierzchniach

`PROC-23.1504` · **Odbudowa rozległa – 2 powierzchnie** · odbudowa i estetyka · status: **draft** · kody w Opisach NFZ: 1504

Opracowanie i odbudowa rozległego ubytku obejmującego dwie powierzchnie (znaczna utrata tkanek).

**Na czym polega.** Usunięcie zmian próchnicowych lub nieszczelnego wypełnienia i odtworzenie dwóch powierzchni – ubytek rozległy korony materiałem adhezyjnym lub glasjonomerem. **Cel:** Zatrzymanie procesu próchnicowego, odtworzenie kształtu, funkcji i estetyki zęba, ochrona miazgi. Ubytek próchnicowy w zębinie, wtórna próchnica, nieszczelne lub uszkodzone wypełnienie, ubytek niepróchnicowy lub urazowy wymagający odbudowy.

Wskazania: próchnica zębiny (ICDAS 4–6); próchnica wtórna; nieszczelne / złamane wypełnienie; ubytek niepróchnicowy z dolegliwościami lub zagrożeniem dla zęba; złamanie korony bez obnażenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Powierzchnie odbudowy i materiał — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2315040 – 71 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Reguły: R-AMALG-01

*Rozliczenie wg liczby powierzchni; współczynnik ×1,5 u dzieci do 18 r.ż. (§ 12 ust. 2 zarz. 60/2023/DSOZ) – liczy moduł Opisy NFZ.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa z ubytkiem wymagającym odbudowy – rzadko; zwykle leczenie nieinwazyjne | ocena_kliniczna | tak |
| K02.1 | Próchnica zębiny | próchnica zębiny – typowe wskazanie do opracowania i odbudowy | ocena_kliniczna | tak |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – odbudowa tylko przy ubytku funkcjonalnym / estetycznym | ocena_kliniczna | tak |
| K02.8 | Inna próchnica zębów | inna określona próchnica (np. wtórna przy wypełnieniu) | ocena_kliniczna | tak |
| K03.1 | Abrazja (starcie mechaniczne) zębów | ścieranie mechaniczne (abrazja) – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.2 | Erozja zębów | erozja – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.0 | Nadmierne ścieranie zębów | nadmierne starcie – odbudowa | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony zęba (uraz) – odbudowa | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa dwóch powierzchni – ubytek rozległy – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa dwóch powierzchni – ubytek rozległy, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa dwóch powierzchni – ubytek rozległy – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`

## 23.1505 – Całkowite opracowanie i odbudowa rozległego ubytku na 3 powierzchniach

`PROC-23.1505` · **Odbudowa rozległa – 3 powierzchnie** · odbudowa i estetyka · status: **draft** · kody w Opisach NFZ: 1505

Opracowanie i odbudowa rozległego ubytku na trzech powierzchniach.

**Na czym polega.** Usunięcie zmian próchnicowych lub nieszczelnego wypełnienia i odtworzenie trzech powierzchni – ubytek rozległy korony materiałem adhezyjnym lub glasjonomerem. **Cel:** Zatrzymanie procesu próchnicowego, odtworzenie kształtu, funkcji i estetyki zęba, ochrona miazgi. Ubytek próchnicowy w zębinie, wtórna próchnica, nieszczelne lub uszkodzone wypełnienie, ubytek niepróchnicowy lub urazowy wymagający odbudowy.

Wskazania: próchnica zębiny (ICDAS 4–6); próchnica wtórna; nieszczelne / złamane wypełnienie; ubytek niepróchnicowy z dolegliwościami lub zagrożeniem dla zęba; złamanie korony bez obnażenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Powierzchnie odbudowy i materiał — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2315050 – 74 pkt (zał. 1b)

- zał. 1 (wszyscy)
- zał. 2 (<18)
- zał. 2b (<18 (szkoła))

Reguły: R-AMALG-01

*Rozliczenie wg liczby powierzchni; współczynnik ×1,5 u dzieci do 18 r.ż. (§ 12 ust. 2 zarz. 60/2023/DSOZ) – liczy moduł Opisy NFZ.*

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa z ubytkiem wymagającym odbudowy – rzadko; zwykle leczenie nieinwazyjne | ocena_kliniczna | tak |
| K02.1 | Próchnica zębiny | próchnica zębiny – typowe wskazanie do opracowania i odbudowy | ocena_kliniczna | tak |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – odbudowa tylko przy ubytku funkcjonalnym / estetycznym | ocena_kliniczna | tak |
| K02.8 | Inna próchnica zębów | inna określona próchnica (np. wtórna przy wypełnieniu) | ocena_kliniczna | tak |
| K03.1 | Abrazja (starcie mechaniczne) zębów | ścieranie mechaniczne (abrazja) – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.2 | Erozja zębów | erozja – odbudowa ubytku niepróchnicowego | ocena_kliniczna | tak |
| K03.0 | Nadmierne ścieranie zębów | nadmierne starcie – odbudowa | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie korony zęba (uraz) – odbudowa | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa trzech powierzchni – ubytek rozległy – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa trzech powierzchni – ubytek rozległy, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa trzech powierzchni – ubytek rozległy – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`

## 23.1506 – Całkowite opracowanie i odbudowa rozległego ubytku na więcej niż 3 powierzchniach

`PROC-23.1506` · **Odbudowa rozległa – > 3 powierzchnie** · odbudowa i estetyka · status: **draft**

Opracowanie i odbudowa rozległego ubytku na więcej niż trzech powierzchniach (odbudowa guzków).

**Na czym polega.** Usunięcie zmian próchnicowych lub nieszczelnego wypełnienia i odtworzenie więcej niż trzech powierzchni korony materiałem adhezyjnym lub glasjonomerem. **Cel:** Zatrzymanie procesu próchnicowego, odtworzenie kształtu, funkcji i estetyki zęba, ochrona miazgi. Ubytek próchnicowy w zębinie, wtórna próchnica, nieszczelne lub uszkodzone wypełnienie, ubytek niepróchnicowy lub urazowy wymagający odbudowy.

Wskazania: próchnica zębiny (ICDAS 4–6); próchnica wtórna; nieszczelne / złamane wypełnienie; ubytek niepróchnicowy z dolegliwościami lub zagrożeniem dla zęba; złamanie korony bez obnażenia miazgi

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Powierzchnie odbudowy i materiał — *zalecenie kliniczne* (`SRC-PRAKTYKA`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **nie**

*Rozliczenie wg liczby powierzchni; współczynnik ×1,5 u dzieci do 18 r.ż. (§ 12 ust. 2 zarz. 60/2023/DSOZ) – liczy moduł Opisy NFZ. Brak w wykazie świadczeń gwarantowanych odczytanym w audycie (zał. 1, 2, 2b, 10, 10b, 10c) – leczenie prywatne albo zakres nieodczytany.*

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.0 | Próchnica ograniczona do szkliwa | próchnica ograniczona do szkliwa z ubytkiem wymagającym odbudowy – rzadko; zwykle leczenie nieinwazyjne | ocena_kliniczna | nie |
| K02.1 | Próchnica zębiny | próchnica zębiny – typowe wskazanie do opracowania i odbudowy | ocena_kliniczna | nie |
| K02.3 | Zatrzymana próchnica zębów | próchnica zatrzymana – odbudowa tylko przy ubytku funkcjonalnym / estetycznym | ocena_kliniczna | nie |
| K02.8 | Inna próchnica zębów | inna określona próchnica (np. wtórna przy wypełnieniu) | ocena_kliniczna | nie |
| K03.1 | Abrazja (starcie mechaniczne) zębów | ścieranie mechaniczne (abrazja) – odbudowa ubytku niepróchnicowego | ocena_kliniczna | nie |
| K03.2 | Erozja zębów | erozja – odbudowa ubytku niepróchnicowego | ocena_kliniczna | nie |
| K03.0 | Nadmierne ścieranie zębów | nadmierne starcie – odbudowa | ocena_kliniczna | nie |
| S02.5 | Złamanie zęba | złamanie korony zęba (uraz) – odbudowa | ocena_kliniczna | nie |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa więcej niż trzech powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa więcej niż trzech powierzchni, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa więcej niż trzech powierzchni – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`

## 23.1507 – Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych

`PROC-23.1507` · **Opracowanie i odbudowa zniszczonego kąta (sieczne)** · odbudowa i estetyka · status: **draft**

Całkowite opracowanie i odbudowa zniszczonego kąta w zębach siecznych.

**Na czym polega.** Opracowanie ubytku obejmującego kąt sieczny i odbudowa materiałem złożonym. **Cel:** Zatrzymanie próchnicy / odtworzenie utraconych tkanek kąta z zachowaniem estetyki.

Wskazania: próchnica lub nieszczelne wypełnienie obejmujące kąt sieczny; złamanie kąta

**Kwalifikacja** – ocenić: żywotność miazgi i objawy (odwracalne / nieodwracalne zapalenie); głębokość ubytku (klinicznie / RTG); możliwość izolacji. Wywiad: ból samoistny / prowokowany; alergie na materiały; leki, choroby ogólne.

- przeciwwskazanie *wzgledne*: objawy nieodwracalnego zapalenia lub martwicy miazgi – wskazane leczenie endodontyczne zamiast samego wypełnienia
- przeciwwskazanie *ograniczenie*: alergia na składnik materiału – dobór innego materiału
- dodatkowa diagnostyka: RTG zgryzowo-skrzydłowe przy podejrzeniu zmian stycznych lub głębokiej próchnicy
- rozważ inne postępowanie: leczenie nieinwazyjne przy zmianach ograniczonych do szkliwa; leczenie endodontyczne przy nieodwracalnym zapaleniu

**Przygotowanie** – konieczne: diagnostyka zęba i zgoda; zestaw podstawowy, wiertła, materiał do odbudowy; opcjonalne: znieczulenie powierzchniowe; zależne od sytuacji: koferdam / izolacja względna; formówka i klin przy ubytkach stycznych. Znieczulenie: Zwykle nasiękowe lub przewodowe – zależnie od zęba i głębokości ubytku; bez znieczulenia, jeśli zabieg nie jest bolesny.

**Przebieg krok po kroku**

1. **Aktualizacja wywiadu, informacja i zgoda** – Sprawdź aktualny wywiad (leki, alergie, ciąża), przedstaw rozpoznanie, plan, alternatywy i ryzyka; uzyskaj zgodę pacjenta. *Uwaga: Szczegóły: badanie BAD-PRZED-LECZENIEM.*
2. **Diagnostyka zęba** – Badanie kliniczne zęba, testy żywotności, opukiwanie; RTG wg wskazań (zgryzowo-skrzydłowe / okołowierzchołkowe). *Uwaga: Szczegóły: BAD-ZYWOTNOSC, BAD-RTG.*
3. **Znieczulenie miejscowe** – Dobierz metodę (nasiękowe / przewodowe / śródwięzadłowe) do zęba i zabiegu; znieczulenie powierzchniowe miejsca wkłucia (opcjonalnie); aspiracja przed podaniem; podawaj powoli; odnotuj preparat, dawkę i miejsce. *Uwaga: Sprawdź maksymalną dawkę dla masy ciała i choroby ogólne (środek obkurczający naczynia).* Warianty: bez znieczulenia – przy zabiegach nieinwazyjnych lub na życzenie pacjenta, jeśli nie powoduje bólu.
4. **Dobór koloru** – Dobór koloru materiału przed izolacją, przy nawilżonych zębach, w świetle dziennym / lampie z dobrym odwzorowaniem barw.
5. **Izolacja pola zabiegowego** – Koferdam (izolacja bezwzględna) albo izolacja względna (wałki ligninowe, ślinociąg) – zależnie od zabiegu. *Uwaga: W leczeniu endodontycznym koferdam jest standardem (ESE).* Warianty: izolacja względna, gdy założenie koferdamu nie jest możliwe – uzasadnij w dokumentacji.
6. **Opracowanie ubytku i usunięcie próchnicy** – Dostęp do zmiany, usunięcie zdemineralizowanej zębiny do twardej przy granicy szkliwno-zębinowej; w ubytkach głębokich (ząb żywy, bez objawów nieodwracalnego zapalenia) – selektywne usunięcie próchnicy przy miazdze. *Uwaga: Unikaj obnażenia miazgi; oceń grubość zębiny nad miazgą.* Warianty: usunięcie etapowe (stepwise) – w bardzo głębokich zmianach.
7. **Ochrona miazgi / podkład** – W ubytkach głębokich – podkład lub pokrycie pośrednie (np. materiał krzemianowo-wapniowy, glasjonomer) zgodnie z głębokością ubytku i stosowanym systemem adhezyjnym. *Uwaga: Dobór materiału zależy od przypadku.*
8. **Formówka i klin** – Odtworzenie ściany stycznej: formówka (sekcyjna / okrężna) i klin; kontrola dopasowania do brzegu przydziąsłowego.
9. **Przygotowanie powierzchni i system wiążący** – Wytrawianie (total-etch / selektywne szkliwa / self-etch – zgodnie z instrukcją systemu), aplikacja systemu wiążącego, polimeryzacja. *Uwaga: Przestrzegaj instrukcji producenta materiału.*
10. **Odbudowa materiałem złożonym** – Nakładanie kompozytu warstwami (zwykle ≤ 2 mm) z polimeryzacją; odtworzenie anatomii i punktu stycznego. *Uwaga: Technika zależy od materiału (np. bulk-fill wg instrukcji).* Warianty: glasjonomer / kompomer – np. zęby mleczne, ograniczona izolacja.
11. **Kontrola zwarcia, wykończenie i polerowanie** – Usunięcie nadmiarów, kontrola zwarcia i ruchów (kalka), kontrola punktu stycznego (nić), polerowanie.
12. **Przekazanie zaleceń** – Przekaż zalecenia pozabiegowe (ustnie lub ustnie i pisemnie) i ustal termin kontroli.

**Materiały i narzędzia:** Lusterko, zgłębnik, pęseta, sonda periodontologiczna (konieczne); Strzykawka, igła, środek znieczulający miejscowo (sytuacyjne); Wiertła i końcówki (turbina, kątnica), ekskawator (konieczne); Wałki ligninowe, ślinociąg (typowe); Koferdam (płachta, klamry, ramka) (alternatywa); Formówki, kliny, pierścienie (sytuacyjne); Wytrawiacz (kwas ortofosforowy) (typowe); System wiążący (typowe); Materiał złożony (kompozyt) (typowe); Cement glasjonomerowy (alternatywa); Materiał krzemianowo-wapniowy (MTA / bioceramika) (sytuacyjne); Lampa polimeryzacyjna (typowe); Gumki, krążki, pasty polerskie, paski (typowe); Kalka zgryzowa, nić dentystyczna (konieczne)

**Kontrola efektu:** szczelność brzeżna i brak nawisów (zgłębnik, RTG przy wątpliwości); punkt styczny (nić); zwarcie i ruchy żuchwy (kalka); kształt anatomiczny i kolor. Nieprawidłowości: nawis przydziąsłowy; brak punktu stycznego; kontakt przedwczesny; nadwrażliwość pozabiegowa. Dalej: korekta nawisu / zwarcia; przy dolegliwościach miazgowych – ponowna diagnostyka żywotności

**Zalecenia pozabiegowe:** Pacjent: Nie jeść do ustąpienia znieczulenia (ryzyko przygryzienia).; Przejściowa wrażliwość na zimno może wystąpić przez kilka dni.. Higiena: Szczotkowanie 2× dziennie pastą z fluorem, oczyszczanie przestrzeni międzyzębowych.. Kontakt z gabinetem, gdy: ból samoistny lub nocny; ból przy nagryzaniu utrzymujący się > kilka dni; wypadnięcie / pęknięcie wypełnienia. Kontrola: Na najbliższym badaniu kontrolnym; przy głębokim ubytku – kontrola żywotności wg decyzji lekarza.

**Dokumentacja**

- Rozpoznanie / wskazanie i ząb (FDI) — *prawne* (`SRC-DU-2026-1391`)
- Zakres wykonanej procedury (powierzchnie, kanały) — *prawne* (`SRC-DU-2026-1391`)
- Znieczulenie: rodzaj, preparat, dawka — *zalecenie kliniczne*, warunek: gdy zastosowano (`SRC-PRAKTYKA`)
- Powikłania i zalecenia — *zalecenie kliniczne* (`SRC-PRAKTYKA`)

**NFZ** – świadczenie gwarantowane: **tak**; produkty: 5.13.00.2315070 – 70 pkt (zał. 1b)

- zał. 1 (wszyscy): Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba. Świadczenie jest udzielane dzieciom i młodzieży do ukończenia 18. roku życia.
- zał. 2 (<18): Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba.
- zał. 2b (<18 (szkoła)): Świadczenie dotyczy zębów stałych i obejmuje złamany, zniszczony kąt sieczny zęba.

Źródła NFZ: `SRC-DU-2025-615`; `SRC-ZARZ-60-2023-TJ`

**ICD-10 (podpowiedzi, wybiera lekarz)**

| Kod | Nazwa robocza | Kiedy | Potwierdzenie | W audycie NFZ |
|---|---|---|---|---|
| K02.1 | Próchnica zębiny | próchnica zębiny obejmująca kąt | ocena_kliniczna | tak |
| S02.5 | Złamanie zęba | złamanie kąta (uraz) | ocena_kliniczna | tak |

**Checklista kompletności**

- [obowiazkowe] Data udzielenia świadczenia — *prawne*
- [obowiazkowe] Opis udzielonego świadczenia (co wykonano, gdzie) — *prawne*
- [obowiazkowe] Rozpoznanie (ICD-10) lub wskazanie do świadczenia — *prawne*
- [obowiazkowe] Oznaczenie lekarza udzielającego świadczenia — *prawne*
- [rozliczeniowe] Świadczenie przekazane do rozliczenia zgodne z dokumentacją — *NFZ*
- [rozliczeniowe] Lokalizacja zęba wg PN-EN ISO 3950 (FDI) — *NFZ*
- [sytuacyjne] Znieczulenie: rodzaj, preparat, dawka, miejsce — *zalecenie kliniczne*
- [zalecane] Zalecenia przekazane pacjentowi (i forma) — *zalecenie kliniczne*
- [zalecane] Powikłania – odnotowane albo zaznaczony ich brak przez lekarza — *zalecenie kliniczne*
- [rozliczeniowe] Powierzchnie odbudowy (oznaczenie) — *NFZ*, produkt zależy od liczby powierzchni
- [zalecane] Materiał odbudowy — *zalecenie kliniczne*
- [sytuacyjne] Ochrona miazgi / podkład przy ubytku głębokim — *zalecenie kliniczne*, ubytek głęboki

**Szablony opisu**

**standardowy**

> Ząb {{POLE-ZAB}}: odbudowa zniszczonego kąta siecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}. Izolacja: {{POLE-IZOLACJA}}. Podkład: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Kontrola zwarcia i punktu stycznego: {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}}. Zalecenia przekazano {{POLE-ZALECENIA-FORMA}}.

**skrocony**

> {{POLE-ZAB}} {{POLE-POWIERZCHNIE}}: odbudowa zniszczonego kąta siecznego, {{POLE-MATERIAL}}; znieczulenie {{POLE-ZNIECZ-RODZAJ}}.

**rozszerzony**

> Ząb {{POLE-ZAB}}. Rozpoznanie: {{POLE-ROZPOZNANIE}}. Wskazanie: {{POLE-WSKAZANIE}}. Znieczulenie: {{POLE-ZNIECZ-RODZAJ}}, {{POLE-ZNIECZ-PREPARAT}} {{POLE-ZNIECZ-DAWKA}}, miejsce: {{POLE-ZNIECZ-MIEJSCE}}. Izolacja: {{POLE-IZOLACJA}}. odbudowa zniszczonego kąta siecznego – powierzchnie {{POLE-POWIERZCHNIE}}. Przebieg: {{POLE-PRZEBIEG}}. Ochrona miazgi: {{POLE-MATERIAL-PODKLAD}}. Materiał: {{POLE-MATERIAL}}, kolor {{POLE-KOLOR}}. Wynik (szczelność, punkt styczny, zwarcie): {{POLE-WYNIK}}. Powikłania: {{POLE-POWIKLANIA}} {{POLE-POWIKLANIA-OPIS}}. Zalecenia ({{POLE-ZALECENIA-FORMA}}): {{POLE-ZALECENIA}}. Kontrola: {{POLE-KONTROLA}}.

**Źródła kliniczne:** `SRC-KLIN-ESE-VPT-2019` (PMID 30664240); `SRC-KLIN-ICDAS-2007` (PMID 17518963); `SRC-PRAKTYKA`
