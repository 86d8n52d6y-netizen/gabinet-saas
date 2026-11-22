# Katalog B – karty procedur ICD-9

| Plik | Co zawiera |
|---|---|
| `KARTY_PROCEDUR.md` | karty opracowanych procedur (generowane z `data/procedury-icd9/`) |
| `REJESTR_KOMPLETNOSCI.md` | wszystkie 266 kodów-procedur ICD-9 PL 5.91 ze statusem (not_started / in_progress / draft / verified / requires_expert_review) |

Pominięte decyzją Patryka (22.11.2026): ortodoncja (23.23–23.26), złamania szczęk (23.22), epitezy / obturatory / protezy poresekcyjne, zabiegi szpitalne – z uzasadnieniem w rejestrze.
Wymagania NFZ w kartach są wyliczane z danych audytu (`data/nfz/`) i oddzielone od zaleceń klinicznych. Każdy element dokumentacji i checklisty ma podstawę (prawna / NFZ / zalecenie kliniczne / propozycja aplikacji) i źródło.
Pliki `.md` są generowane (`python3 scripts/buduj_docs_bazy.py`) – nie edytuj ich ręcznie.
