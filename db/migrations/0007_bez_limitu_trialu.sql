-- 0007: okres próbny bez daty końca (decyzja Patryka 21.11.2026: „wyłącz opcję okresu próbnego”; licencje i płatności odłożone – decyzja 9).
-- Zmiana tylko funkcji app.has_access(): konto aktywne ze statusem trial_active ma dostęp bez względu na trial_end.
-- Bez zmian: konta zablokowane/usunięte (profiles.status <> 'active') nie mają dostępu; licencja roczna – do period_end; dożywotnia – bez limitu;
-- rekordy subskrypcji (trial_start, trial_end) zostają nietknięte. Cofnięcie: nowa migracja przywracająca warunek now() < s.trial_end.
BEGIN;
CREATE OR REPLACE FUNCTION app.has_access() RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER SET search_path = app, pg_temp AS $$
  SELECT EXISTS (SELECT 1 FROM app.subscriptions s JOIN app.profiles p ON p.id = s.user_id
    WHERE s.user_id = app.uid() AND p.status = 'active' AND (
      (s.status = 'trial_active') OR
      (s.status = 'annual_active'  AND now() < s.period_end) OR
      (s.status = 'lifetime_active')))
$$;
REVOKE ALL ON FUNCTION app.has_access() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION app.has_access() TO gabinet_app;
COMMIT;
