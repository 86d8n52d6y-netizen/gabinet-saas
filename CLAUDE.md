# Zasady pracy w tym repo (Gabinet – wersja SaaS)

- Komunikacja po polsku. Repozytorium **prywatne** – kodu SaaS nie publikuj w publicznych repozytoriach.
- Pracuj fazami (plan: `docs/AUDYT_SAAS.md`). Po każdej fazie: testy → commit → push → wpis w `POSTEP.md` → raport ze statusami WDROŻONE / WYMAGA MOJEGO DZIAŁANIA / WYMAGA KONFIGURACJI ZEWNĘTRZNEJ / NIE WDROŻONO. Nie zaczynaj kolejnej fazy bez potwierdzenia poprzedniej.
- Po przerwie zacznij od `POSTEP.md` i `git log --oneline -10`.
- Testy przed commitem: `npm run typecheck`, `npm test` (vitest), `python3 db/test_izolacja.py` (izolacja SQL, tworzy własną świeżą bazę).
- Prywatność (decyzje Patryka): w chmurze NIE przechowujemy danych pacjentów ani treści opisów – tylko procedury, kody, kwoty, datę i gabinet. Bez inicjałów, PESEL, adresów, zdjęć.
- Izolacja: każda tabela z danymi użytkownika ma FORCE RLS; aplikacja łączy się jako `gabinet_web` i przełącza rolę przez `withUser` / `withRole` z `src/lib/db.ts`. Nie dodawaj dostępu z pominięciem tych funkcji.
- Zmiany schematu tylko nową migracją `db/migrations/NNNN_*.sql` – nigdy nie edytuj wykonanej migracji.
- Sekrety tylko w `.env` (nie w repo, nie we frontendzie). Brak uniwersalnych haseł i ukrytych kont.
- Licencje weryfikowane wyłącznie na serwerze; Stripe lokalnie tylko w trybie testowym.
- Bez zgody Patryka: żadnych płatnych usług, hostingu produkcyjnego, usuwania danych ani funkcji.
- Kodów NFZ i stawek nie wymyślaj – podawaj źródło (zarządzenie DSOZ). Stawki: 1,84 zł/pkt, 350 zł/h przeglądów, +10 min – nie zmieniaj bez decyzji Patryka.
- Darmowa wersja (statyczna) jest w publicznym repo `opisy-nfz` i działa na GitHub Pages – nie zmieniaj jej z tego repo.
