# docs/nfz – audyt świadczeń stomatologicznych NFZ

Stan prawny na **21.11.2026**. Audyt rozpoczęty 21.11.2026.

| Plik | Zawartość |
|---|---|
| `AUDYT_RAPORT.md` | **zacznij tutaj** – wnioski, etapy A–H, porównanie z aplikacją, listy kontrolne, projekt techniczny, plan testów |
| `DECYZJE_I_NIEJASNOSCI.md` | decyzje D1–D7 (A/B/C) i luki N1–N12 |
| `REJESTR_ZRODEL.md` | 26 źródeł ze statusem |
| `REGULY_ROZLICZEN.md` | 47 reguł + macierz łączenia + współczynniki |
| `PROCEDURY_ICD9.md` | 107 kart procedur (25 pól) + tabela pakietów ST |
| `MAPOWANIA_ICD9_ICD10.md` | podpowiedzi ICD-10 (nie wymóg NFZ) + warianty kodów NFZ |

Dane maszynowe: `data/nfz/*.json`, schematy: `data/nfz/schemas/`, walidacja: `python3 scripts/waliduj_nfz.py`.

## Statusy

- Reguła: **POTWIERDZONA**, **CZĘŚCIOWO POTWIERDZONA** albo **WYMAGA WERYFIKACJI**.
- Łączenie: **DOZWOLONE**, **NIEDOZWOLONE**, **WARUNKOWO DOZWOLONE**, **WYMAGA DODATKOWEJ WERYFIKACJI** albo **NIE DOTYCZY**.
- Poziom kontroli: **BLOKADA** (tylko eksport, tylko reguła potwierdzona), **OSTRZEŻENIE** albo **INFORMACJA**.

## Zasady nienaruszalne

1. Niepotwierdzona reguła nie blokuje.
2. Brak zakazu nie oznacza „DOZWOLONE”.
3. Aplikacja nie podpowiada dopisywania czynności ani zmiany daty wstecz.
4. Mapowania ICD-9→ICD-10 to podpowiedzi. Rozpoznanie wybiera lekarz.
5. Dane pacjenta (wiek, ząb, ciąża) są używane wyłącznie na urządzeniu.
