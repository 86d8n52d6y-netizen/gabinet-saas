-- Gabinet SaaS – migracja 5: dane modułów bez danych pacjentów (etap 4c).
-- user_blobs: cennik prywatny, ustawienia modułu, szablony (własne wersje), zestawy – materiały gabinetowe użytkownika.
BEGIN;
CREATE TABLE app.user_blobs (
  owner_id   uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  key        text NOT NULL CHECK (key ~ '^[a-z]{2,12}:[a-z]{2,12}$'),
  data       jsonb NOT NULL CHECK (pg_column_size(data) < 1048576),
  version    int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (owner_id, key)
);
CREATE TRIGGER touch BEFORE UPDATE ON app.user_blobs FOR EACH ROW EXECUTE FUNCTION app.touch();
ALTER TABLE app.user_blobs ENABLE ROW LEVEL SECURITY; ALTER TABLE app.user_blobs FORCE ROW LEVEL SECURITY;
CREATE POLICY own ON app.user_blobs FOR ALL TO gabinet_app USING (owner_id = app.uid()) WITH CHECK (owner_id = app.uid());
GRANT SELECT, INSERT, UPDATE, DELETE ON app.user_blobs TO gabinet_app;
COMMIT;
