# Katalog A – badania stomatologiczne

| Plik | Co zawiera |
|---|---|
| `OPISY_BADAN.md` | pełne opisy badań (generowane z `data/badania/examinations.json`) |
| `STRUKTURA_POL.md` | wszystkie pola formularzy (wspólne i badań) |

Dane źródłowe: `data/badania/` · schematy: `data/baza-stomatologiczna/schemas/` · instrukcja integracji: `docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md`.
Zasady: wynik prawidłowy to przykład opisu – nigdy nie jest zaznaczany za lekarza; żadne pole nie jest wymagane do zapisu; tekst zawsze edytowalny.
Pliki `.md` są generowane (`python3 scripts/buduj_docs_bazy.py`) – nie edytuj ich ręcznie.
