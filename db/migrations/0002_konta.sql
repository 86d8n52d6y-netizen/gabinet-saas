-- Gabinet SaaS – migracja 2: konta i logowanie (FAZA 3)
--  * 2FA (TOTP): sekret w trakcie konfiguracji, ochrona przed ponownym użyciem tego samego kodu, kody zapasowe (tylko skróty),
--  * limity prób (logowanie, rejestracja, reset hasła, kody 2FA) – klucze jako HMAC, bez jawnych adresów IP i e-maili,
--  * sprzątanie: wygasłe tokeny, stare sesje i limity; skrócone IP w dzienniku bezpieczeństwa usuwane po 90 dniach
--    (zasada zaakceptowana 16.11.2026).
BEGIN;

ALTER TABLE app.profiles
  ADD COLUMN mfa_pending_enc bytea,                 -- sekret TOTP podczas konfiguracji (przed potwierdzeniem kodem)
  ADD COLUMN mfa_last_step   bigint,                -- numer ostatnio użytego okna 30 s – ten sam kod nie zadziała drugi raz
  ADD COLUMN password_changed_at timestamptz NOT NULL DEFAULT now();

CREATE TABLE app.mfa_recovery_codes (
  user_id    uuid NOT NULL REFERENCES app.profiles(id) ON DELETE CASCADE,
  code_hash  bytea NOT NULL CHECK (length(code_hash) = 32),       -- HMAC-SHA256 kodu; samego kodu nie przechowujemy
  used_at    timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, code_hash)
);

CREATE TABLE app.rate_limits (
  bucket       text NOT NULL CHECK (bucket ~ '^[a-z_:]{1,40}$'),  -- np. login:email, login:ip, register:ip
  key_hash     bytea NOT NULL CHECK (length(key_hash) = 32),       -- HMAC klucza (e-mail / skrócone IP)
  window_start timestamptz NOT NULL DEFAULT now(),
  hits         int NOT NULL DEFAULT 0 CHECK (hits >= 0),
  PRIMARY KEY (bucket, key_hash)
);

ALTER TABLE app.mfa_recovery_codes ENABLE ROW LEVEL SECURITY; ALTER TABLE app.mfa_recovery_codes FORCE ROW LEVEL SECURITY;
ALTER TABLE app.rate_limits        ENABLE ROW LEVEL SECURITY; ALTER TABLE app.rate_limits        FORCE ROW LEVEL SECURITY;
CREATE POLICY auth_all ON app.mfa_recovery_codes FOR ALL TO gabinet_auth USING (true) WITH CHECK (true);
CREATE POLICY auth_all ON app.rate_limits        FOR ALL TO gabinet_auth USING (true) WITH CHECK (true);
GRANT SELECT, INSERT, UPDATE, DELETE ON app.mfa_recovery_codes, app.rate_limits TO gabinet_auth;
GRANT DELETE ON app.email_tokens TO gabinet_auth;

-- zdarzenia bezpieczeństwa: rejestracja i prośba o reset (bez zmiany istniejących typów)
ALTER TABLE app.security_events DROP CONSTRAINT security_events_type_check;
ALTER TABLE app.security_events ADD CONSTRAINT security_events_type_check CHECK (type IN (
  'login_ok','login_fail','logout','logout_all','new_device','password_reset','password_change','mfa_on','mfa_off',
  'email_verified','blocked','rate_limited','suspicious','register','reset_requested','mfa_fail','recovery_code_used'));

-- licznik prób w oknie czasowym; zwraca liczbę prób w bieżącym oknie (po doliczeniu tej próby)
CREATE FUNCTION app.rate_hit(p_bucket text, p_key bytea, p_window interval) RETURNS int
LANGUAGE sql SECURITY INVOKER SET search_path = app, pg_temp AS $$
  INSERT INTO app.rate_limits AS r (bucket, key_hash, window_start, hits) VALUES (p_bucket, p_key, now(), 1)
  ON CONFLICT (bucket, key_hash) DO UPDATE SET
    hits = CASE WHEN r.window_start < now() - p_window THEN 1 ELSE r.hits + 1 END,
    window_start = CASE WHEN r.window_start < now() - p_window THEN now() ELSE r.window_start END
  RETURNING hits
$$;
REVOKE ALL ON FUNCTION app.rate_hit(text, bytea, interval) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION app.rate_hit(text, bytea, interval) TO gabinet_auth;

-- sprzątanie (wywoływane przez serwer co jakiś czas); SECURITY DEFINER, bo dziennik bezpieczeństwa jest tylko do dopisywania
CREATE FUNCTION app.auth_cleanup() RETURNS void LANGUAGE sql SECURITY DEFINER SET search_path = app, pg_temp AS $$
  DELETE FROM app.email_tokens WHERE expires_at < now() - interval '1 day';
  DELETE FROM app.sessions     WHERE (revoked_at IS NOT NULL OR expires_at < now()) AND last_seen_at < now() - interval '30 days';
  DELETE FROM app.rate_limits  WHERE window_start < now() - interval '1 day';
  UPDATE app.security_events SET ip_prefix = NULL WHERE ip_prefix IS NOT NULL AND created_at < now() - interval '90 days';
  UPDATE app.sessions        SET ip_prefix = NULL WHERE ip_prefix IS NOT NULL AND created_at < now() - interval '90 days';
$$;
REVOKE ALL ON FUNCTION app.auth_cleanup() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION app.auth_cleanup() TO gabinet_auth;

COMMIT;
