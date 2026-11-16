-- Gabinet SaaS – schemat bazy, wersja 1 (PROJEKT do akceptacji – FAZA 2)
-- PostgreSQL 16. Zasady:
--  * brak tabel i kolumn na dane pacjentów; opisy zabiegów NIE są przechowywane (decyzja 1, 16.11.2026),
--  * każda tabela z danymi użytkownika ma owner_id i Row Level Security (FORCE – obowiązuje też właściciela tabeli),
--  * aplikacja łączy się rolą bez uprawnień do obejścia RLS; identyfikator użytkownika ustawiany w każdej transakcji:
--      SET LOCAL app.user_id = '<uuid z sesji>';
--  * kwoty w groszach (bigint), procenty numeric(5,2), daty w strefie Europe/Warsaw po stronie aplikacji,
--  * synchronizacja między urządzeniami: kolumna version (optymistyczna kontrola konfliktów) + deleted_at (znaczniki usunięcia).

BEGIN;
CREATE EXTENSION IF NOT EXISTS citext;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ---------- role (hasła nadawane przy wdrożeniu, nie w tym pliku) ----------
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='gabinet_app')     THEN CREATE ROLE gabinet_app     NOLOGIN NOBYPASSRLS; END IF; -- żądania zalogowanego użytkownika
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='gabinet_auth')    THEN CREATE ROLE gabinet_auth    NOLOGIN NOBYPASSRLS; END IF; -- logowanie, sesje, tokeny e-mail
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='gabinet_billing') THEN CREATE ROLE gabinet_billing NOLOGIN NOBYPASSRLS; END IF; -- webhooki płatności, licencje
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='gabinet_admin')   THEN CREATE ROLE gabinet_admin   NOLOGIN NOBYPASSRLS; END IF; -- panel administratora (bez treści użytkowników)
END $$;

CREATE SCHEMA app;
REVOKE ALL ON SCHEMA app FROM PUBLIC;
GRANT USAGE ON SCHEMA app TO gabinet_app, gabinet_auth, gabinet_billing, gabinet_admin;

-- bieżący użytkownik z ustawienia transakcji; brak ustawienia = brak dostępu (NULL nie pasuje do żadnego owner_id)
CREATE FUNCTION app.uid() RETURNS uuid LANGUAGE sql STABLE AS $$ SELECT nullif(current_setting('app.user_id', true), '')::uuid $$;

CREATE FUNCTION app.touch() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN NEW.updated_at := now(); NEW.version := OLD.version + 1; RETURN NEW; END $$;

-- ================= KONTA =================
CREATE TABLE app.profiles (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email           citext NOT NULL UNIQUE CHECK (length(email) <= 254 AND email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  email_verified_at timestamptz,
  password_hash   text NOT NULL CHECK (password_hash LIKE '$argon2id$%'),
  display_name    text NOT NULL CHECK (length(display_name) BETWEEN 1 AND 80),
  initials        varchar(6) CHECK (initials ~ '^[A-ZĄĆĘŁŃÓŚŹŻ]{1,6}$'),          -- inicjały LEKARZA (statystyki), nie pacjenta
  role            text NOT NULL DEFAULT 'user' CHECK (role IN ('user','admin')),
  status          text NOT NULL DEFAULT 'active' CHECK (status IN ('active','blocked','deleted')),
  mfa_secret_enc  bytea,                                                              -- TOTP, zaszyfrowany kluczem aplikacji
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now(),
  deleted_at      timestamptz
);

CREATE TABLE app.sessions (                                -- jedna sesja = jedno urządzenie; bez limitu liczby urządzeń
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  token_hash    bytea NOT NULL UNIQUE CHECK (length(token_hash) = 32),             -- SHA-256 losowego tokenu z ciasteczka HttpOnly
  device_label  text CHECK (length(device_label) <= 120),                          -- np. „Safari, iPhone”
  ip_prefix     inet,                                                              -- adres skrócony (/24, /48) – minimalizacja danych
  created_at    timestamptz NOT NULL DEFAULT now(),
  last_seen_at  timestamptz NOT NULL DEFAULT now(),
  expires_at    timestamptz NOT NULL,
  mfa_passed    boolean NOT NULL DEFAULT false,
  revoked_at    timestamptz
);
CREATE INDEX sessions_user ON app.sessions(user_id) WHERE revoked_at IS NULL;

CREATE TABLE app.email_tokens (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  purpose     text NOT NULL CHECK (purpose IN ('verify','reset','email_change')),
  token_hash  bytea NOT NULL UNIQUE CHECK (length(token_hash) = 32),
  new_email   citext,
  expires_at  timestamptz NOT NULL,
  used_at     timestamptz,
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE app.security_events (                         -- logowania, nieudane próby, nowe urządzenie, reset hasła
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id     uuid REFERENCES app.profiles(id) ON DELETE SET NULL,
  type        text NOT NULL CHECK (type IN ('login_ok','login_fail','logout','logout_all','new_device','password_reset','password_change','mfa_on','mfa_off','email_verified','blocked','rate_limited','suspicious')),
  ip_prefix   inet,
  device_label text,
  details     jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at  timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX security_events_user ON app.security_events(user_id, created_at DESC);

CREATE TABLE app.user_settings (                           -- stawki (1,84 zł/pkt, 350 zł/h…), wygląd, ustawienia podatkowe Kalendarza
  user_id     uuid PRIMARY KEY REFERENCES app.profiles(id) ON DELETE CASCADE,
  settings    jsonb NOT NULL DEFAULT '{}'::jsonb CHECK (jsonb_typeof(settings) = 'object' AND pg_column_size(settings) < 65536),
  calendar    jsonb NOT NULL DEFAULT '{}'::jsonb CHECK (jsonb_typeof(calendar) = 'object' AND pg_column_size(calendar) < 131072),
  version     int NOT NULL DEFAULT 1,
  updated_at  timestamptz NOT NULL DEFAULT now()
);

-- ================= GABINETY =================
CREATE TABLE app.clinics (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  name        text NOT NULL CHECK (length(name) BETWEEN 1 AND 80),
  short       varchar(6),
  color       smallint NOT NULL DEFAULT 1 CHECK (color BETWEEN 1 AND 12),
  active      boolean NOT NULL DEFAULT true,
  model       text NOT NULL DEFAULT 'pct_lab' CHECK (model IN ('pct_lab','pct_share','pct','hourly','daily','manual')),
  pct         numeric(5,2) CHECK (pct BETWEEN 0 AND 100),
  lab_share   numeric(5,2) CHECK (lab_share BETWEEN 0 AND 100),
  hourly_gr   bigint CHECK (hourly_gr >= 0),
  daily_gr    bigint CHECK (daily_gr >= 0),
  min_daily_gr bigint CHECK (min_daily_gr >= 0),
  default_doctor_pct numeric(5,2) CHECK (default_doctor_pct BETWEEN 0 AND 100),     -- domyślny % w cenniku prywatnym
  sort        int NOT NULL DEFAULT 0,
  extra       jsonb NOT NULL DEFAULT '{}'::jsonb,                                    -- adres, godziny – ustawienia Kalendarza
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  UNIQUE (owner_id, id)
);
CREATE INDEX clinics_owner ON app.clinics(owner_id) WHERE deleted_at IS NULL;

-- ================= KATALOG NFZ (wspólny, tylko do odczytu) =================
CREATE TABLE app.nfz_catalog (
  code        text PRIMARY KEY CHECK (code ~ '^[A-Z0-9]{3,8}$'),
  name        text NOT NULL,
  points      numeric(8,2) CHECK (points >= 0),
  source      text NOT NULL,                     -- np. „Zarządzenie Prezesa NFZ nr 95/2026/DSOZ, zał. 2” – bez źródła nie ma wpisu
  valid_from  date NOT NULL,
  valid_to    date,
  verified_at date NOT NULL,                     -- kiedy ostatnio sprawdzono z aktualnym zarządzeniem
  definition  jsonb NOT NULL                     -- pytania, reguły, szablon (przeniesione z obecnego silnika)
);

-- ================= PROCEDURY UŻYTKOWNIKA =================
CREATE TABLE app.procedure_categories (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  name        text NOT NULL CHECK (length(name) BETWEEN 1 AND 60),
  sort        int NOT NULL DEFAULT 0,
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  UNIQUE (owner_id, id)
);
CREATE UNIQUE INDEX procedure_categories_name ON app.procedure_categories(owner_id, lower(name)) WHERE deleted_at IS NULL;

CREATE TABLE app.procedures (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  category_id uuid,
  kind        text NOT NULL CHECK (kind IN ('private','nfz_custom')),       -- nfz_custom: własna procedura NFZ, oznaczona „niesprawdzana przez zasady NFZ”
  nfz_code    text CHECK (nfz_code IS NULL OR nfz_code ~ '^[A-Z0-9.]{2,12}$'),
  nfz_points  numeric(8,2) CHECK (nfz_points >= 0),
  name        text NOT NULL CHECK (length(name) BETWEEN 1 AND 120),
  description text CHECK (length(description) <= 300),
  fields      jsonb NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(fields) = 'array' AND pg_column_size(fields) < 65536),
  template    text NOT NULL DEFAULT '' CHECK (length(template) <= 20000),
  builtin_key text,                                                       -- np. „zach-staly” – kopia szablonu domyślnego
  is_favorite boolean NOT NULL DEFAULT false,
  is_hidden   boolean NOT NULL DEFAULT false,
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  UNIQUE (owner_id, id),
  FOREIGN KEY (owner_id, category_id) REFERENCES app.procedure_categories(owner_id, id),   -- kategoria tylko własna
  CHECK (kind = 'nfz_custom' OR (nfz_code IS NULL AND nfz_points IS NULL))
);
CREATE INDEX procedures_owner ON app.procedures(owner_id, category_id) WHERE deleted_at IS NULL;
CREATE INDEX procedures_search ON app.procedures USING gin (name gin_trgm_ops);

CREATE TABLE app.procedure_versions (                      -- historia wersji szablonu, przywracanie
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id     uuid NOT NULL,
  procedure_id uuid NOT NULL,
  version      int NOT NULL,
  snapshot     jsonb NOT NULL,
  created_at   timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (owner_id, procedure_id) REFERENCES app.procedures(owner_id, id) ON DELETE CASCADE,
  UNIQUE (procedure_id, version)
);

CREATE TABLE app.procedure_prices (                        -- cennik: osobno dla każdego gabinetu (clinic_id NULL = „bez gabinetu”)
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL,
  clinic_id   uuid,
  procedure_id uuid NOT NULL,
  price_gr    bigint CHECK (price_gr >= 0),
  pay_mode    text NOT NULL DEFAULT 'default_pct' CHECK (pay_mode IN ('default_pct','pct','amount')),
  pay_pct     numeric(5,2) CHECK (pay_pct BETWEEN 0 AND 100),
  pay_amount_gr bigint CHECK (pay_amount_gr >= 0),
  version     int NOT NULL DEFAULT 1,
  updated_at  timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (owner_id, procedure_id) REFERENCES app.procedures(owner_id, id) ON DELETE CASCADE,
  FOREIGN KEY (owner_id, clinic_id) REFERENCES app.clinics(owner_id, id) ON DELETE CASCADE,
  UNIQUE NULLS NOT DISTINCT (owner_id, clinic_id, procedure_id),
  CHECK ((pay_mode = 'pct') = (pay_pct IS NOT NULL)),
  CHECK ((pay_mode = 'amount') = (pay_amount_gr IS NOT NULL))
);

-- ================= ZESTAWY =================
CREATE TABLE app.procedure_sets (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  module      text NOT NULL CHECK (module IN ('nfz','private')),
  name        text NOT NULL CHECK (length(name) BETWEEN 1 AND 80),
  category    text CHECK (length(category) <= 60),
  is_favorite boolean NOT NULL DEFAULT false,
  sort        int NOT NULL DEFAULT 0,
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  UNIQUE (owner_id, id)
);

CREATE TABLE app.procedure_set_items (
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id     uuid NOT NULL,
  set_id       uuid NOT NULL,
  position     int NOT NULL CHECK (position >= 0),
  procedure_id uuid,
  nfz_code     text REFERENCES app.nfz_catalog(code),
  FOREIGN KEY (owner_id, set_id) REFERENCES app.procedure_sets(owner_id, id) ON DELETE CASCADE,
  FOREIGN KEY (owner_id, procedure_id) REFERENCES app.procedures(owner_id, id) ON DELETE CASCADE,
  CHECK ((procedure_id IS NULL) <> (nfz_code IS NULL)),
  UNIQUE (set_id, position) DEFERRABLE INITIALLY DEFERRED                 -- zmiana kolejności w jednej transakcji
);

-- ================= ZAPISANE WIZYTY (BEZ TREŚCI OPISU I BEZ DANYCH PACJENTA) =================
CREATE TABLE app.saved_descriptions (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  client_id   uuid NOT NULL,                                 -- nadany na urządzeniu: ponowne wysłanie po utracie połączenia nie tworzy dubla
  module      text NOT NULL CHECK (module IN ('nfz','private')),
  visit_date  date NOT NULL,
  clinic_id   uuid,
  seq_no      int NOT NULL CHECK (seq_no > 0),               -- numer kolejny wpisu użytkownika (zamiast inicjałów pacjenta)
  minutes     int CHECK (minutes BETWEEN 0 AND 1440),
  review_hours numeric(5,2) CHECK (review_hours BETWEEN 0 AND 24),
  rates       jsonb NOT NULL DEFAULT '{}'::jsonb,            -- stawki z chwili zapisu (pkt, %, zł/h) – późniejsza zmiana stawek nie zmienia wpisu
  codes       text[] NOT NULL DEFAULT '{}' CHECK (cardinality(codes) <= 40),
  edited      boolean NOT NULL DEFAULT false,                -- czy tekst był poprawiany ręcznie (sam tekst nie jest przechowywany)
  status      text NOT NULL DEFAULT 'active' CHECK (status IN ('active','corrected','deleted')),
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  UNIQUE (owner_id, id),
  UNIQUE (owner_id, client_id),
  UNIQUE (owner_id, module, seq_no),
  FOREIGN KEY (owner_id, clinic_id) REFERENCES app.clinics(owner_id, id)
);
CREATE INDEX saved_descriptions_date ON app.saved_descriptions(owner_id, visit_date DESC) WHERE deleted_at IS NULL;

-- jedyne źródło kwot w statystykach – każda kwota ma dokładnie jeden wiersz (brak podwójnego liczenia)
CREATE TABLE app.earnings_entries (
  id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id       uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  description_id uuid,
  line_no        smallint NOT NULL DEFAULT 0 CHECK (line_no >= 0),
  entry_date     date NOT NULL,
  clinic_id      uuid,
  source         text NOT NULL CHECK (source IN ('nfz_points','nfz_review','nfz_extra','private_procedure','manual')),
  procedure_id   uuid,
  nfz_code       text,
  category_name  text CHECK (length(category_name) <= 60),      -- kategoria z chwili zapisu (filtrowanie)
  label          text CHECK (length(label) <= 120),             -- nazwa procedury lub opis kwoty (bez danych pacjenta)
  qty            int NOT NULL DEFAULT 1 CHECK (qty BETWEEN 1 AND 99),
  points         numeric(10,2) CHECK (points >= 0),
  value_gr       bigint NOT NULL CHECK (value_gr >= 0),
  cost_gr        bigint NOT NULL DEFAULT 0 CHECK (cost_gr >= 0),
  doctor_pay_gr  bigint NOT NULL CHECK (doctor_pay_gr >= 0),
  version        int NOT NULL DEFAULT 1,
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now(),
  deleted_at     timestamptz,
  FOREIGN KEY (owner_id, description_id) REFERENCES app.saved_descriptions(owner_id, id) ON DELETE CASCADE,
  FOREIGN KEY (owner_id, clinic_id) REFERENCES app.clinics(owner_id, id),
  UNIQUE (description_id, line_no)                              -- kwoty ręczne (description_id NULL) mogą być wielokrotne
);
CREATE INDEX earnings_date ON app.earnings_entries(owner_id, entry_date) WHERE deleted_at IS NULL;
CREATE INDEX earnings_clinic ON app.earnings_entries(owner_id, clinic_id, entry_date) WHERE deleted_at IS NULL;

-- ================= KALENDARZ =================
CREATE TABLE app.shifts (                                   -- dyżury; przychód z dyżurów NIE jest dodawany do earnings_entries (te same wizyty)
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  clinic_id   uuid NOT NULL,
  shift_date  date NOT NULL,
  start_time  time NOT NULL,
  end_time    time NOT NULL,
  status      text NOT NULL DEFAULT 'planned' CHECK (status IN ('planned','done','cancelled')),
  turnover_gr bigint CHECK (turnover_gr >= 0),
  lab_gr      bigint CHECK (lab_gr >= 0),
  amount_gr   bigint CHECK (amount_gr >= 0),
  override_gr bigint CHECK (override_gr >= 0),
  note        text CHECK (length(note) <= 500),
  version     int NOT NULL DEFAULT 1,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  FOREIGN KEY (owner_id, clinic_id) REFERENCES app.clinics(owner_id, id)
);
CREATE INDEX shifts_date ON app.shifts(owner_id, shift_date) WHERE deleted_at IS NULL;

CREATE TABLE app.days_off (
  owner_id  uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  day       date NOT NULL,
  kind      text NOT NULL CHECK (kind IN ('urlop','l4','wolne')),
  version   int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (owner_id, day)
);

CREATE TABLE app.clinic_invoices (                          -- faktura dla gabinetu za miesiąc: wystawiona / opłacona
  owner_id  uuid NOT NULL,
  clinic_id uuid NOT NULL,
  month     date NOT NULL CHECK (extract(day FROM month) = 1),
  issued_on date,
  paid_on   date,
  amount_gr bigint CHECK (amount_gr >= 0),
  version   int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (owner_id, clinic_id, month),
  FOREIGN KEY (owner_id, clinic_id) REFERENCES app.clinics(owner_id, id) ON DELETE CASCADE
);

CREATE TABLE app.business_costs (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id   uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  cost_date  date NOT NULL,
  amount_gr  bigint NOT NULL CHECK (amount_gr >= 0),
  label      text NOT NULL CHECK (length(label) BETWEEN 1 AND 200),
  is_kup     boolean NOT NULL DEFAULT true,              -- koszt uzyskania przychodu
  course_id  uuid,
  version    int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  deleted_at timestamptz
);
CREATE INDEX business_costs_date ON app.business_costs(owner_id, cost_date) WHERE deleted_at IS NULL;

CREATE TABLE app.courses (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_id   uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  name       text NOT NULL CHECK (length(name) BETWEEN 1 AND 200),
  days       jsonb NOT NULL DEFAULT '[]'::jsonb,           -- dni i godziny kursu
  cme_points numeric(6,1) CHECK (cme_points >= 0),
  blocks_shifts boolean NOT NULL DEFAULT true,
  version    int NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  deleted_at timestamptz
);

-- ================= LICENCJE I PŁATNOŚCI =================
CREATE TABLE app.subscriptions (                            -- jedna bieżąca licencja na konto; zmienia ją tylko serwer (rola billing/admin)
  user_id      uuid PRIMARY KEY REFERENCES app.profiles(id) ON DELETE CASCADE,
  plan         text NOT NULL CHECK (plan IN ('trial','annual','lifetime')),
  status       text NOT NULL CHECK (status IN ('trial_active','annual_active','lifetime_active','expired','suspended','payment_pending','payment_failed')),
  trial_start  timestamptz,
  trial_end    timestamptz,
  period_start timestamptz,
  period_end   timestamptz,
  lifetime_since timestamptz,
  provider_customer_id text,
  updated_at   timestamptz NOT NULL DEFAULT now(),
  updated_by   text NOT NULL,                               -- 'system' | 'webhook:<event>' | 'admin:<uuid>'
  CHECK (plan <> 'trial' OR (trial_start IS NOT NULL AND trial_end = trial_start + interval '3 months')),
  CHECK (plan <> 'lifetime' OR lifetime_since IS NOT NULL)
);

CREATE TABLE app.trial_registry (                           -- blokada ponownego triala po usunięciu konta / zmianie danych
  email_hmac  bytea PRIMARY KEY CHECK (length(email_hmac) = 32), -- HMAC-SHA256 znormalizowanego e-maila z sekretem serwera
  first_trial_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE app.payments (                                 -- bez danych kart: tylko identyfikatory operatora
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      uuid REFERENCES app.profiles(id) ON DELETE SET NULL,
  provider     text NOT NULL DEFAULT 'stripe',
  provider_ref text NOT NULL,
  product      text NOT NULL CHECK (product IN ('annual','lifetime')),
  amount_gr    bigint NOT NULL CHECK (amount_gr >= 0),
  currency     char(3) NOT NULL DEFAULT 'PLN',
  status       text NOT NULL CHECK (status IN ('pending','succeeded','failed','refunded')),
  created_at   timestamptz NOT NULL DEFAULT now(),
  updated_at   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (provider, provider_ref)
);

CREATE TABLE app.payment_events (                           -- idempotencja webhooków: każde zdarzenie przetwarzane raz
  provider     text NOT NULL,
  event_id     text NOT NULL,
  type         text NOT NULL,
  received_at  timestamptz NOT NULL DEFAULT now(),
  processed_at timestamptz,
  payload_sha256 bytea NOT NULL,
  PRIMARY KEY (provider, event_id)
);

-- ================= DZIENNIK AUDYTOWY (tylko dopisywanie) =================
CREATE TABLE app.audit_logs (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  actor_id    uuid,
  actor_role  text NOT NULL CHECK (actor_role IN ('user','admin','system','webhook')),
  action      text NOT NULL,
  target_user uuid,
  target      text,
  before      jsonb,
  after       jsonb,
  ip_prefix   inet,
  created_at  timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX audit_logs_target ON app.audit_logs(target_user, created_at DESC);
CREATE FUNCTION app.audit_immutable() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN RAISE EXCEPTION 'audit_logs: wpisów nie można zmieniać ani usuwać'; END $$;
CREATE TRIGGER audit_no_change BEFORE UPDATE OR DELETE ON app.audit_logs FOR EACH ROW EXECUTE FUNCTION app.audit_immutable();

-- ================= WERSJE (synchronizacja) =================
DO $$ DECLARE t text; BEGIN
  FOREACH t IN ARRAY ARRAY['clinics','procedure_categories','procedures','procedure_prices','procedure_sets','saved_descriptions','earnings_entries','shifts','days_off','clinic_invoices','business_costs','courses','user_settings'] LOOP
    EXECUTE format('CREATE TRIGGER touch BEFORE UPDATE ON app.%I FOR EACH ROW EXECUTE FUNCTION app.touch()', t);
  END LOOP;
END $$;

-- ================= ROW LEVEL SECURITY =================
DO $$ DECLARE t text; BEGIN
  -- dane użytkownika: tylko właściciel (rola gabinet_app); pełne CRUD
  FOREACH t IN ARRAY ARRAY['clinics','procedure_categories','procedures','procedure_versions','procedure_prices','procedure_sets','procedure_set_items','saved_descriptions','earnings_entries','shifts','days_off','clinic_invoices','business_costs','courses'] LOOP
    EXECUTE format('ALTER TABLE app.%I ENABLE ROW LEVEL SECURITY', t);
    EXECUTE format('ALTER TABLE app.%I FORCE ROW LEVEL SECURITY', t);
    EXECUTE format('CREATE POLICY own ON app.%I FOR ALL TO gabinet_app USING (owner_id = app.uid()) WITH CHECK (owner_id = app.uid())', t);
    EXECUTE format('GRANT SELECT, INSERT, UPDATE, DELETE ON app.%I TO gabinet_app', t);
  END LOOP;
END $$;

ALTER TABLE app.user_settings ENABLE ROW LEVEL SECURITY; ALTER TABLE app.user_settings FORCE ROW LEVEL SECURITY;
CREATE POLICY own ON app.user_settings FOR ALL TO gabinet_app USING (user_id = app.uid()) WITH CHECK (user_id = app.uid());
GRANT SELECT, INSERT, UPDATE ON app.user_settings TO gabinet_app;

-- profil: użytkownik czyta i zmienia tylko swoje nazwy (nie rolę, status ani hasło – kolumnowe uprawnienia)
ALTER TABLE app.profiles ENABLE ROW LEVEL SECURITY; ALTER TABLE app.profiles FORCE ROW LEVEL SECURITY;
CREATE POLICY self_read ON app.profiles FOR SELECT TO gabinet_app USING (id = app.uid());
CREATE POLICY self_upd ON app.profiles FOR UPDATE TO gabinet_app USING (id = app.uid()) WITH CHECK (id = app.uid());
GRANT SELECT (id, email, email_verified_at, display_name, initials, role, status, created_at) ON app.profiles TO gabinet_app;
GRANT UPDATE (display_name, initials, updated_at) ON app.profiles TO gabinet_app;
-- moduł logowania: profile, sesje, tokeny (bez dostępu do treści użytkownika)
CREATE POLICY auth_all ON app.profiles FOR ALL TO gabinet_auth USING (true) WITH CHECK (true);
GRANT SELECT, INSERT, UPDATE ON app.profiles TO gabinet_auth;
GRANT SELECT, INSERT, UPDATE, DELETE ON app.sessions, app.email_tokens TO gabinet_auth;
GRANT INSERT ON app.security_events TO gabinet_auth, gabinet_app;
GRANT INSERT ON app.user_settings, app.subscriptions, app.trial_registry TO gabinet_auth;   -- rejestracja: ustawienia startowe + trial
CREATE POLICY auth_init ON app.user_settings FOR INSERT TO gabinet_auth WITH CHECK (true);
GRANT SELECT ON app.trial_registry TO gabinet_auth;
-- sesje i zdarzenia bezpieczeństwa: użytkownik widzi swoje (lista urządzeń), może odwołać swoje
ALTER TABLE app.sessions ENABLE ROW LEVEL SECURITY; ALTER TABLE app.sessions FORCE ROW LEVEL SECURITY;
CREATE POLICY own ON app.sessions FOR ALL TO gabinet_app USING (user_id = app.uid()) WITH CHECK (user_id = app.uid());
CREATE POLICY auth_all ON app.sessions FOR ALL TO gabinet_auth USING (true) WITH CHECK (true);
GRANT SELECT (id, device_label, ip_prefix, created_at, last_seen_at, expires_at, revoked_at) ON app.sessions TO gabinet_app;
GRANT UPDATE (revoked_at) ON app.sessions TO gabinet_app;
ALTER TABLE app.security_events ENABLE ROW LEVEL SECURITY; ALTER TABLE app.security_events FORCE ROW LEVEL SECURITY;
CREATE POLICY own_read ON app.security_events FOR SELECT TO gabinet_app USING (user_id = app.uid());
CREATE POLICY own_ins ON app.security_events FOR INSERT TO gabinet_app WITH CHECK (user_id = app.uid());
CREATE POLICY auth_ins ON app.security_events FOR INSERT TO gabinet_auth WITH CHECK (true);
GRANT SELECT ON app.security_events TO gabinet_app;

-- licencje: użytkownik tylko CZYTA swoją; zmienia wyłącznie billing (webhook) i admin
ALTER TABLE app.subscriptions ENABLE ROW LEVEL SECURITY; ALTER TABLE app.subscriptions FORCE ROW LEVEL SECURITY;
CREATE POLICY own_read ON app.subscriptions FOR SELECT TO gabinet_app USING (user_id = app.uid());
CREATE POLICY billing_all ON app.subscriptions FOR ALL TO gabinet_billing, gabinet_admin USING (true) WITH CHECK (true);
CREATE POLICY auth_trial ON app.subscriptions FOR INSERT TO gabinet_auth WITH CHECK (plan = 'trial' AND status = 'trial_active');
GRANT SELECT ON app.subscriptions TO gabinet_app;
GRANT SELECT, INSERT, UPDATE ON app.subscriptions TO gabinet_billing, gabinet_admin;
ALTER TABLE app.payments ENABLE ROW LEVEL SECURITY; ALTER TABLE app.payments FORCE ROW LEVEL SECURITY;
CREATE POLICY own_read ON app.payments FOR SELECT TO gabinet_app USING (user_id = app.uid());
CREATE POLICY billing_all ON app.payments FOR ALL TO gabinet_billing USING (true) WITH CHECK (true);
CREATE POLICY admin_read ON app.payments FOR SELECT TO gabinet_admin USING (true);
GRANT SELECT ON app.payments TO gabinet_app, gabinet_admin;
GRANT SELECT, INSERT, UPDATE ON app.payments TO gabinet_billing;
GRANT SELECT, INSERT, UPDATE ON app.payment_events TO gabinet_billing;

-- katalog NFZ: wszyscy czytają, nikt z aplikacji nie zmienia (aktualizacje tylko migracją ze źródłem DSOZ)
GRANT SELECT ON app.nfz_catalog TO gabinet_app, gabinet_admin;

-- administrator: konta, licencje, płatności, logi; BEZ dostępu do procedur, wizyt, kwot i Kalendarza użytkowników
CREATE POLICY admin_read ON app.profiles FOR SELECT TO gabinet_admin USING (true);
CREATE POLICY admin_upd ON app.profiles FOR UPDATE TO gabinet_admin USING (true) WITH CHECK (true);
GRANT SELECT (id, email, email_verified_at, display_name, role, status, created_at, deleted_at) ON app.profiles TO gabinet_admin;
GRANT UPDATE (status, role, updated_at) ON app.profiles TO gabinet_admin;
CREATE POLICY admin_read ON app.security_events FOR SELECT TO gabinet_admin USING (true);
GRANT SELECT ON app.security_events TO gabinet_admin;
CREATE POLICY admin_read ON app.sessions FOR SELECT TO gabinet_admin USING (true);
CREATE POLICY admin_revoke ON app.sessions FOR UPDATE TO gabinet_admin USING (true) WITH CHECK (true);
GRANT SELECT (id, user_id, device_label, created_at, last_seen_at, revoked_at) ON app.sessions TO gabinet_admin;
GRANT UPDATE (revoked_at) ON app.sessions TO gabinet_admin;

-- dziennik audytowy: wszyscy dopisują, tylko admin czyta
GRANT INSERT ON app.audit_logs TO gabinet_app, gabinet_auth, gabinet_billing, gabinet_admin;
GRANT SELECT ON app.audit_logs TO gabinet_admin;

-- statystyki korzystania dla admina: tylko liczby, bez treści (funkcja z prawami właściciela schematu)
CREATE FUNCTION app.usage_stats() RETURNS TABLE(users bigint, active_7d bigint, visits_30d bigint, trial bigint, annual bigint, lifetime bigint)
LANGUAGE sql SECURITY DEFINER SET search_path = app, pg_temp AS $$
  SELECT (SELECT count(*) FROM app.profiles WHERE status <> 'deleted'),
         (SELECT count(DISTINCT user_id) FROM app.sessions WHERE last_seen_at > now() - interval '7 days'),
         (SELECT count(*) FROM app.saved_descriptions WHERE created_at > now() - interval '30 days' AND deleted_at IS NULL),
         (SELECT count(*) FROM app.subscriptions WHERE status = 'trial_active'),
         (SELECT count(*) FROM app.subscriptions WHERE status = 'annual_active'),
         (SELECT count(*) FROM app.subscriptions WHERE status = 'lifetime_active')
$$;
REVOKE ALL ON FUNCTION app.usage_stats() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION app.usage_stats() TO gabinet_admin;

-- licencja sprawdzana na serwerze: czy zalogowane konto ma teraz dostęp do funkcji płatnych
CREATE FUNCTION app.has_access() RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER SET search_path = app, pg_temp AS $$
  SELECT EXISTS (SELECT 1 FROM app.subscriptions s JOIN app.profiles p ON p.id = s.user_id
    WHERE s.user_id = app.uid() AND p.status = 'active' AND (
      (s.status = 'trial_active'   AND now() < s.trial_end) OR
      (s.status = 'annual_active'  AND now() < s.period_end) OR
      (s.status = 'lifetime_active')))
$$;
REVOKE ALL ON FUNCTION app.has_access() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION app.has_access() TO gabinet_app;                  -- tylko własne konto (app.uid()), bez parametru

COMMIT;
