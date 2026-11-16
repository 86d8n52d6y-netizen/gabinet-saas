-- Gabinet SaaS – migracja 4: synchronizacja historii wizyt generatora (etap 4b).
-- W chmurze: data, gabinet, kody, punkty, stawki, kwoty, czas – BEZ treści opisu, odpowiedzi, wieku i inicjałów (decyzja 1).
BEGIN;
ALTER TABLE app.saved_descriptions
  ADD COLUMN client_key text CHECK (client_key ~ '^[A-Za-z0-9_-]{1,40}$'),   -- identyfikator wpisu z urządzenia (np. „v…”)
  ADD COLUMN client_at  timestamptz,                                          -- czas ostatniej zmiany na urządzeniu (nowszy wygrywa)
  ADD COLUMN meta jsonb NOT NULL DEFAULT '{}'::jsonb CHECK (jsonb_typeof(meta) = 'object' AND pg_column_size(meta) < 8192);
-- numer wpisu nadaje urządzenie; dwa urządzenia offline mogą nadać ten sam – numer jest tylko etykietą (nie identyfikatorem)
ALTER TABLE app.saved_descriptions DROP CONSTRAINT saved_descriptions_owner_id_module_seq_no_key;
CREATE UNIQUE INDEX saved_descriptions_client_key ON app.saved_descriptions(owner_id, module, client_key);
COMMIT;
