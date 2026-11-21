-- PROJEKT (nie wykonany) – do akceptacji Patryka przed przeniesieniem do db/migrations/0008_zlecenia.sql (zasada 12).
-- Gabinet SaaS – migracja 8: Zlecenia protetyczne w chmurze (etap E7, decyzja 17 w docs/AUDYT_SAAS.md).
-- Na serwerze: treść zlecenia (numer przypadku, inicjały, rodzaj pracy, zęby/schemat FDI, materiał, kolor, zgryz, implanty,
-- terminy, statusy, historia zmian). NIGDY: imię i nazwisko, PESEL, adres, zdjęcia (zdjęcia zostają na urządzeniu).
-- API przyjmuje tylko pola z listy (odrzuca resztę) – kontrola w src/lib/zlecenia.ts, tu dodatkowe zabezpieczenia w bazie.
BEGIN;
CREATE TABLE app.prosthetic_orders (
  owner_id   uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  id         text NOT NULL CHECK (id ~ '^z[a-z0-9]{6,24}$'),
  data       jsonb NOT NULL CHECK (jsonb_typeof(data) = 'object' AND pg_column_size(data) < 262144
                                   AND NOT (data ? 'imie') AND NOT (data ? 'nazwisko') AND NOT (data ? 'pesel')
                                   AND NOT (data ? 'adres') AND NOT (data ? 'zdjecia')),
  deleted    boolean NOT NULL DEFAULT false,          -- usunięcie = znacznik (inne urządzenia też usuwają u siebie), treść czyszczona
  version    int NOT NULL DEFAULT 1,                  -- kontrola wersji jak w Kalendarzu (konflikt → scalenie / pytanie)
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (owner_id, id),
  CHECK (NOT deleted OR data = '{}'::jsonb)
);
CREATE INDEX prosthetic_orders_upd ON app.prosthetic_orders (owner_id, updated_at);
CREATE TRIGGER touch BEFORE UPDATE ON app.prosthetic_orders FOR EACH ROW EXECUTE FUNCTION app.touch();
ALTER TABLE app.prosthetic_orders ENABLE ROW LEVEL SECURITY; ALTER TABLE app.prosthetic_orders FORCE ROW LEVEL SECURITY;
CREATE POLICY own ON app.prosthetic_orders FOR ALL TO gabinet_app USING (owner_id = app.uid()) WITH CHECK (owner_id = app.uid());
GRANT SELECT, INSERT, UPDATE, DELETE ON app.prosthetic_orders TO gabinet_app;
COMMIT;
