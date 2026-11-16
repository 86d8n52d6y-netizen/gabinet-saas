-- Gabinet SaaS – migracja 6: Kalendarz (etap 4e-1). Dokumenty Kalendarza 1:1 z obecnej aplikacji:
-- 'settings' (ustawienia, gabinety z polami kalendarza, ZUS, podatki), 'courses' (kursy, punkty edukacyjne), 'mRRRR-MM' (dyżury miesiąca), 'sumy' (przychód z dyżurów
-- dzień → gabinet – do okna Zarobki). Bez danych pacjentów. Gabinety: wspólna tabela app.clinics (pola kalendarza w extra->'kal').
BEGIN;
CREATE TABLE app.calendar_docs (
  owner_id   uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  doc        text NOT NULL CHECK (doc ~ '^(settings|courses|sumy|m[0-9]{4}-[0-9]{2})$'),
  data       jsonb NOT NULL CHECK (jsonb_typeof(data) = 'object' AND pg_column_size(data) < 1048576),
  version    int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (owner_id, doc)
);
CREATE TRIGGER touch BEFORE UPDATE ON app.calendar_docs FOR EACH ROW EXECUTE FUNCTION app.touch();
ALTER TABLE app.calendar_docs ENABLE ROW LEVEL SECURITY; ALTER TABLE app.calendar_docs FORCE ROW LEVEL SECURITY;
CREATE POLICY own ON app.calendar_docs FOR ALL TO gabinet_app USING (owner_id = app.uid()) WITH CHECK (owner_id = app.uid());
GRANT SELECT, INSERT, UPDATE, DELETE ON app.calendar_docs TO gabinet_app;
COMMIT;
