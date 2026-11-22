# Baza stomatologiczna – instrukcja przyszłej integracji z aplikacją Gabinet

Stan: 22.11.2026 · gałąź `baza-stomatologiczna` · prompt Patryka „PROMPT 2 – badania stomatologiczne i karty procedur ICD-9”.
**Stan integracji:** etap I1 (22.11.2026) – „Katalog procedur i badań” (`/katalog-procedur`, link w Katalogu NFZ; `src/lib/baza.ts`) oraz kontrola kompletności dokumentacji w Opisach NFZ (krok 3, `generator/baza-dane.js` ze `scripts/baza_dane_przegladarka.py`, poprawki P41–P42a) – ostrzeżenie bez blokady; treść opisów i wycena bez zmian. Pozostałe funkcje (§8) – na Twoje polecenie.

## 1. Gdzie są dane

| Katalog | Zawartość | Rekordy (stan na dziś) |
|---|---|---|
| `data/badania/` | `examinations.json` (katalog A), `examination-fields.json` (pola badań), `examination-templates.json` (opisy: standardowy / skrócony / rozszerzony) | 17 badań, 104 pola, 51 szablonów |
| `data/procedury-icd9/` | `procedures.json` (rejestr + karty), `procedure-steps.json`, `procedure-materials.json`, `procedure-templates.json`, `procedure-checklists.json`, `procedure-diagnosis-mappings.json` | 266 kodów w rejestrze (206 kart: 144 `draft`, 62 `requires_expert_review`; 3 nadrzędne; 57 pominiętych), 114 kroków, 70 materiałów, 618 szablonów procedur, 206 checklist, 401 mapowań ICD-10 |
| `data/baza-stomatologiczna/` | `pola-wspolne.json`, `zrodla-kliniczne.json`, `manifest.json` (wersja, sumy SHA-256, liczniki), `schemas/` (JSON Schema 2020-12) | 31 pól wspólnych, 21 źródeł z PubMed + 2 pomocnicze |
| `data/nfz/` | **audyt NFZ** – słownik ICD-9 PL 5.91, ICD-10, reguły, produkty, źródła prawne (podstawa; baza z niego korzysta, nie kopiuje go) | – |
| `docs/badania/`, `docs/procedury-icd9/` | dokumentacja **generowana z JSON** (`scripts/buduj_docs_bazy.py`) | – |

## 2. Dlaczego taki format (zgodność z architekturą)

Aplikacja ma dwie warstwy (CLAUDE.md §2): generator w przeglądarce (`generator/*.html`, dane na urządzeniu) i serwer Next.js z PostgreSQL (metadane, RLS).
Wiedza stomatologiczna (opisy, kroki, pola, reguły) **nie jest danymi pacjenta ani użytkownika** – to statyczny słownik, jak dane audytu NFZ. Dlatego:

- format = JSON + JSON Schema + walidator w Pythonie – **ten sam mechanizm co `data/nfz/`** (audyt NFZ, etapy N1–N6), bez nowej technologii,
- **bez tabel w bazie i bez migracji** (nic do RLS, nic na serwerze o pacjencie),
- do przeglądarki dane trafiają jak `generator/nfz-dane.js` (skrypt generujący plik JS, dostęp tylko po zalogowaniu – lista `ASSETS` w `src/lib/nfz/generator.ts`),
- na serwer (np. strona „Katalog procedur”) – jak `src/lib/nfz/audyt.ts` (odczyt JSON z `data/`, `outputFileTracingIncludes` w `next.config.ts`).

## 3. Identyfikatory i relacje

| Rekord | Id | Odwołania |
|---|---|---|
| badanie | `BAD-…` | pola (`POLE-…`), szablony (`SZAB-BAD-…-STD/SKR/ROZ`), ICD-9 (`23.…`), ICD-10, reguły NFZ (`R-…`), źródła (`SRC-…`) |
| procedura | `PROC-23.…` (= kod ICD-9 PL 5.91) | kroki (`KROK-…` + uwaga dla tej procedury), materiały (`MAT-…` + rola), szablony (`SZAB-PROC-…`), checklista (po `procedura`), mapowania ICD-10, reguły NFZ, źródła |
| pole | `POLE-…` | wspólne (`pola-wspolne.json`) albo badania (`pole.badanie`) |
| element checklisty | `CHK-W-…` (wspólny) / `CHK-<kod>-n` | pole formularza, źródło, poziom, podstawa |
| mapowanie | `procedura + icd10` | `w_audycie_nfz` – czy para jest w podpowiedziach audytu (liczone automatycznie) |

Relacje wyłącznie po identyfikatorach – walidator sprawdza każde odwołanie. Nazwy tekstowe nie są kluczami.

## 4. Jak czytać dane (przykłady dla przyszłej implementacji)

**Opis procedury (przeglądarka, Opisy NFZ / prywatne)** – składanie szablonu:

```js
// BAZA = window.BAZA_STOM (przyszły generator/baza-dane.js, wzór: scripts/nfz_dane_przegladarka.py)
// Sprawdzone 22.11.2026 na danych z data/ (node): puste pola → całe zdanie pomijane, nagłówek wielkimi literami zostaje.
function opis(BAZA, id, wariant, wartosci) {                     // wartosci: {'POLE-ZAB': '36', ...} – wpisane przez lekarza
  const s = BAZA.szablony.find(t => t.dotyczy === id && t.wariant === wariant);
  const pelne = z => [...z.matchAll(/\{\{(POLE-[A-Z0-9-]+)\}\}/g)].every(m => (wartosci[m[1]] ?? '') !== '');
  const nag = (s.tekst.match(/^[A-ZĄĆĘŁŃÓŚŹŻ0-9 ()–-]{4,}:\s*/) || [''])[0];  // nagłówek zostaje zawsze
  const zdania = s.tekst.slice(nag.length).split(/(?<=\.)\s+/)       // zdania szablonu (kropka + spacja)
    .filter(pelne)                                                    // zdanie z pustym polem – pomijane w całości
    .map(z => z.replace(/\{\{(POLE-[A-Z0-9-]+)\}\}/g, (_, p) => wartosci[p]));
  return (nag + zdania.join(' ')).trim();                             // wynik trafia do edytowalnego pola przed zapisem
}
// opis(BAZA, 'PROC-23.1502', 'standardowy', {'POLE-ZAB':'36','POLE-POWIERZCHNIE':'O','POLE-ROZPOZNANIE':'K02.1','POLE-MATERIAL':'kompozyt','POLE-KOLOR':'A2', ...})
// → „Ząb 36: odbudowa jednej powierzchni – powierzchnie O. Rozpoznanie: K02.1. … Materiał: kompozyt, kolor A2.”
```

**Kontrola kompletności** – checklista: `obowiazkowe` → ostrzeżenie przed zapisem, **bez blokady** (decyzja Patryka 22.11.2026 – do czasu odczytania rozporządzenia o dokumentacji, `SRC-DU-2026-1391`), `zalecane` / `sytuacyjne` → podpowiedź, `rozliczeniowe` → tylko przy rozliczeniu NFZ.

**Podpowiedzi ICD-10** – `procedure-diagnosis-mappings.json` + nazwy z `data/nfz/diagnoses.json` (robocze); to samo zachowanie co etap N5 audytu: wybiera lekarz, nigdy automatycznie.

**Katalog na serwerze** – wzór `src/lib/nfz/audyt.ts`: odczyt JSON, cache w produkcji, tylko do odczytu.

## 5. Walidacja, import, wersje

```bash
python3 scripts/waliduj_nfz.py            # najpierw dane audytu NFZ (zależność)
python3 scripts/waliduj_baze.py           # schematy, odwołania, ICD-9/ICD-10, checklisty, szablony, manifest
python3 scripts/waliduj_baze.py --manifest  # po zmianie danych: przelicza sumy SHA-256 i liczniki
python3 scripts/buduj_docs_bazy.py        # dokumentacja .md z JSON
python3 scripts/import_bazy.py --porownaj main   # raport: nowe / zmienione / usunięte rekordy względem main
python3 scripts/import_bazy.py --pakiet /tmp/pakiet.json   # pakiet importu (tylko draft + verified)
```

Zasady importu: upsert po id; rekordy usunięte z JSON **nie są kasowane automatycznie** (raport do decyzji); poprzednia wersja = commit w gicie + manifest; błąd walidacji wstrzymuje import.

## 6. Dodawanie i aktualizacja

- **Nowa karta procedury:** w `procedures.json` uzupełnij rekord `PROC-…` (status `draft`), dodaj 3 szablony, checklistę, mapowania ICD-10; kroki i materiały – najpierw z bibliotek, nowe tylko gdy brak. Sekcję `nfz` wypełnij z danych audytu (nie przepisuj ręcznie warunków – wzór w narzędziu autorskim: świadczenia gwarantowane, produkty 1b, pakiety, reguły).
- **Nowe badanie:** rekord `BAD-…`, pola z `badanie`, 3 szablony.
- **Weryfikacja przez Patryka:** `status: "verified"`, `zweryfikowal: "Patryk Barysz"`, data – walidator wymaga obu.
- **Nowe zarządzenie NFZ:** najpierw `data/nfz/` (audyt), potem `waliduj_baze.py` pokaże niespójności (np. nieistniejące reguły).
- Po każdej zmianie: walidator → `--manifest` → dokumentacja → commit.

## 7. Co jest zweryfikowane, a co nie

| Element | Status |
|---|---|
| Kody i nazwy ICD-9 | zgodne z ICD-9 PL 5.91 (walidator porównuje nazwę z plikiem Patryka) |
| Warunki NFZ w kartach | wyliczone z audytu NFZ (statusy źródeł jak w audycie) |
| Źródła kliniczne | 21 publikacji sprawdzonych w PubMed (PMID; DOI gdy zwrócony) |
| Treść kart i badań | **draft – wymaga weryfikacji Patryka** (żadna karta nie jest `verified`) |
| Wymagania prawne dokumentacji | oparte na `SRC-DU-2026-1391` – **akt nieodczytany w audycie (wymaga weryfikacji)** |
| Nazwy ICD-10 | robocze (audyt, N8) – do porównania z wydaniem CeZ |

## 8. Elementy aplikacji, które mogą korzystać z bazy

Katalog badań i procedur (strona), dynamiczne formularze w Opisach NFZ / prywatnych, generowanie opisów z szablonów, podpowiedzi przebiegu (kroki), checklisty kompletności przed zapisem, podpowiedzi ICD-10, moduł kontroli rozliczeń NFZ (reguły z audytu). Zaimplementowane w I1: katalog (strona) i checklisty kompletności (Opisy NFZ). Pozostałe – wymagają Twojego zlecenia.
