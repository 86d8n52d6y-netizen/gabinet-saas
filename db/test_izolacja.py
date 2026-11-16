# Testy izolacji i uprawnień schematu 0001_init.sql (PostgreSQL 16).
# Uruchomienie: python3 test_izolacja.py  (serwer: PGHOST/PGPORT/PGUSER – superużytkownik testowy)
# Za każdym razem tworzy od zera osobną bazę gabinet_test_izolacja, więc wynik nie zależy od wcześniejszych danych.
import os, subprocess, sys
TESTDB = 'gabinet_test_izolacja'
MDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'migrations')
MIGR = sorted(os.path.join(MDIR, f) for f in os.listdir(MDIR) if f.endswith('.sql'))   # wszystkie migracje po kolei
ENV = dict(os.environ, PGHOST=os.environ.get('PGHOST', '/tmp/pgtest'), PGPORT=os.environ.get('PGPORT', '55432'),
           PGUSER=os.environ.get('PGUSER', 'migrator'), PGDATABASE=TESTDB)
def _psql(args, db):
    r = subprocess.run(['psql', '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-d', db] + args, capture_output=True, text=True, env=ENV)
    if r.returncode: sys.exit('Nie udało się przygotować bazy testowej: ' + r.stderr.strip())
_psql(['-c', f'DROP DATABASE IF EXISTS {TESTDB} WITH (FORCE)', '-c', f'CREATE DATABASE {TESTDB}'], 'postgres')
for _m in MIGR: _psql(['-f', _m], TESTDB)
ok = bad = 0
def sql(q):
    r = subprocess.run(['psql', '-X', '-At', '-q', '-v', 'ON_ERROR_STOP=1', '-c', q], capture_output=True, text=True, env=ENV)
    return r.returncode == 0, (r.stdout.strip() if r.returncode == 0 else r.stderr.strip())
def as_(role, uid, q):  # jedna transakcja jako rola aplikacji z ustawionym użytkownikiem
    pre = f"BEGIN; SET LOCAL ROLE {role}; " + (f"SET LOCAL app.user_id = '{uid}'; " if uid else '')
    return sql(pre + q + '; COMMIT;')
def chk(name, cond, info=''):
    global ok, bad
    print(('OK   ' if cond else 'BŁĄD ') + name + ('' if cond else f' | {info}')); ok += cond; bad += (not cond)
def denied(res): return (not res[0]) and ('permission denied' in res[1] or 'row-level security' in res[1] or 'violates' in res[1])

A = '11111111-1111-1111-1111-111111111111'; B = '22222222-2222-2222-2222-222222222222'
H = "'$argon2id$v=19$m=65536,t=3,p=4$test'"
# ---- przygotowanie: dwa konta przez moduł logowania ----
for u, e in [(A, 'a@test.pl'), (B, 'b@test.pl')]:
    r = as_('gabinet_auth', None, f"INSERT INTO app.profiles(id,email,password_hash,display_name) VALUES ('{u}','{e}',{H},'Lekarz'); INSERT INTO app.user_settings(user_id) VALUES ('{u}'); INSERT INTO app.subscriptions(user_id,plan,status,trial_start,trial_end,updated_by) VALUES ('{u}','trial','trial_active',now(),now()+interval '3 months','system')")
    chk(f'rejestracja {e} (moduł logowania: profil, ustawienia, trial)', r[0], r[1])
cA = 'aaaaaaaa-0000-0000-0000-00000000000a'; cB = 'bbbbbbbb-0000-0000-0000-00000000000b'
pA = 'aaaaaaaa-0000-0000-0000-0000000000a1'; pB = 'bbbbbbbb-0000-0000-0000-0000000000b1'
for u, c, pr in [(A, cA, pA), (B, cB, pB)]:
    r = as_('gabinet_app', u, f"INSERT INTO app.clinics(id,owner_id,name) VALUES ('{c}','{u}','Gabinet'); INSERT INTO app.procedures(id,owner_id,kind,name) VALUES ('{pr}','{u}','private','Skaling'); INSERT INTO app.earnings_entries(owner_id,entry_date,source,value_gr,doctor_pay_gr) VALUES ('{u}',current_date,'manual',10000,4000)")
    chk('użytkownik zapisuje własne dane (gabinet, procedura, kwota)', r[0], r[1])

# ---- izolacja ----
r = as_('gabinet_app', A, "SELECT count(*) FROM app.procedures"); chk('A widzi tylko swoje procedury (1)', r == (True, '1'), r)
r = as_('gabinet_app', A, f"SELECT count(*) FROM app.procedures WHERE id = '{pB}'"); chk('A nie odczyta procedury B nawet po identyfikatorze (zmiana adresu / API)', r == (True, '0'), r)
r = as_('gabinet_app', A, "SELECT coalesce(sum(value_gr),0) FROM app.earnings_entries"); chk('sumy zarobków A nie zawierają kwot B', r == (True, '10000'), r)
r = as_('gabinet_app', A, f"UPDATE app.procedures SET name='X' WHERE id='{pB}' RETURNING id"); chk('A nie zmieni procedury B (0 wierszy)', r[0] and r[1] == '', r)
r = as_('gabinet_app', A, f"DELETE FROM app.clinics WHERE id='{cB}' RETURNING id"); chk('A nie usunie gabinetu B (0 wierszy)', r[0] and r[1] == '', r)
r = as_('gabinet_app', A, f"INSERT INTO app.procedures(owner_id,kind,name) VALUES ('{B}','private','Podrzucona')"); chk('A nie wstawi danych na konto B', denied(r), r)
r = as_('gabinet_app', A, f"UPDATE app.procedures SET owner_id='{B}' WHERE id='{pA}'"); chk('A nie przepisze swojej procedury na B', denied(r), r)
r = as_('gabinet_app', A, f"INSERT INTO app.shifts(owner_id,clinic_id,shift_date,start_time,end_time) VALUES ('{A}','{cB}',current_date,'08:00','14:00')"); chk('A nie podepnie dyżuru pod gabinet B (klucz złożony owner_id + id)', denied(r), r)
r = as_('gabinet_app', A, f"INSERT INTO app.procedure_prices(owner_id,clinic_id,procedure_id,price_gr) VALUES ('{A}',NULL,'{pB}',100)"); chk('A nie ustawi ceny dla procedury B', denied(r), r)
r = as_('gabinet_app', None, "SELECT count(*) FROM app.procedures"); chk('bez zalogowanego użytkownika: 0 wierszy', r == (True, '0'), r)
r = as_('gabinet_app', A, "SELECT count(*) FROM app.profiles"); chk('A widzi tylko swój profil', r == (True, '1'), r)
r = as_('gabinet_app', A, "SELECT password_hash FROM app.profiles"); chk('A nie odczyta skrótu hasła (nawet swojego)', denied(r), r)
r = as_('gabinet_app', A, f"UPDATE app.profiles SET role='admin' WHERE id='{A}'"); chk('A nie nada sobie roli administratora', denied(r), r)
r = as_('gabinet_app', A, f"UPDATE app.profiles SET display_name='Dr A' WHERE id='{A}' RETURNING display_name"); chk('A zmienia swoją nazwę', r == (True, 'Dr A'), r)
r = as_('gabinet_app', A, "SELECT count(*) FROM app.sessions"); chk('A widzi tylko swoje sesje (urządzenia)', r[0], r)
# ---- licencje ----
r = as_('gabinet_app', A, f"UPDATE app.subscriptions SET status='lifetime_active', plan='lifetime', lifetime_since=now() WHERE user_id='{A}'"); chk('A nie zmieni sobie licencji (np. na lifetime)', denied(r), r)
r = as_('gabinet_app', A, "SELECT status FROM app.subscriptions"); chk('A widzi tylko swoją licencję', r == (True, 'trial_active'), r)
r = as_('gabinet_app', A, "SELECT app.has_access()"); chk('trial aktywny → dostęp (sprawdzenie na serwerze)', r == (True, 't'), r)
r = as_('gabinet_billing', None, f"UPDATE app.subscriptions SET status='expired', updated_by='system' WHERE user_id='{A}'")
r2 = as_('gabinet_app', A, "SELECT app.has_access()"); chk('licencja wygasła (zmiana przez serwer) → brak dostępu', r[0] and r2 == (True, 'f'), (r, r2))
r = as_('gabinet_auth', None, f"INSERT INTO app.subscriptions(user_id,plan,status,lifetime_since,updated_by) VALUES ('{A}','lifetime','lifetime_active',now(),'x')"); chk('moduł logowania nie przyzna licencji lifetime', denied(r), r)
r = sql(f"INSERT INTO app.subscriptions(user_id,plan,status,trial_start,trial_end,updated_by) VALUES (gen_random_uuid(),'trial','trial_active',now(),now()+interval '1 year','x')"); chk('trial dłuższy niż 3 miesiące odrzucony przez bazę', not r[0], r)
r = as_('gabinet_billing', None, "INSERT INTO app.payment_events(provider,event_id,type,payload_sha256) VALUES ('stripe','evt_1','checkout.session.completed','\\x00')")
r2 = as_('gabinet_billing', None, "INSERT INTO app.payment_events(provider,event_id,type,payload_sha256) VALUES ('stripe','evt_1','checkout.session.completed','\\x00')")
chk('webhook: to samo zdarzenie drugi raz odrzucone (idempotencja)', r[0] and not r2[0], (r, r2))
# ---- administrator ----
r = as_('gabinet_admin', None, "SELECT count(*) FROM app.procedures"); chk('administrator nie czyta procedur użytkowników', denied(r), r)
r = as_('gabinet_admin', None, "SELECT count(*) FROM app.earnings_entries"); chk('administrator nie czyta kwot użytkowników', denied(r), r)
r = as_('gabinet_admin', None, "SELECT count(*) FROM app.shifts"); chk('administrator nie czyta Kalendarza użytkowników', denied(r), r)
r = as_('gabinet_admin', None, "SELECT count(*) FROM app.profiles"); chk('administrator widzi listę kont', r == (True, '2'), r)
r = as_('gabinet_admin', None, "SELECT password_hash FROM app.profiles"); chk('administrator nie widzi skrótów haseł', denied(r), r)
r = as_('gabinet_admin', None, "SELECT users, trial FROM app.usage_stats()"); chk('administrator: statystyki korzystania (same liczby)', r == (True, '2|1'), r)
r = as_('gabinet_admin', None, f"INSERT INTO app.audit_logs(actor_id,actor_role,action,target_user) VALUES ('{A}','admin','extend_license','{B}')"); chk('wpis do dziennika audytowego', r[0], r)
r = sql("UPDATE app.audit_logs SET action='x'"); chk('dziennika audytowego nie da się zmienić (nawet właścicielowi bazy)', not r[0] and 'nie można' in r[1], r)
r = sql("DELETE FROM app.audit_logs"); chk('dziennika audytowego nie da się wyczyścić', not r[0], r)
# ---- konflikty i dane pacjentów ----
r = as_('gabinet_app', A, f"UPDATE app.procedures SET name='v2' WHERE id='{pA}' AND version=1 RETURNING version")
r2 = as_('gabinet_app', A, f"UPDATE app.procedures SET name='stare urządzenie' WHERE id='{pA}' AND version=1 RETURNING version")
chk('konflikt dwóch urządzeń: druga zmiana na starej wersji nie nadpisuje (0 wierszy → komunikat w aplikacji)', r == (True, '2') and r2 == (True, ''), (r, r2))
r = sql("SELECT string_agg(table_name||'.'||column_name, ', ') FROM information_schema.columns WHERE table_schema='app' AND column_name ~* '(pesel|patient|pacjent|address|adres|birth|phone|telefon)'")
chk('w schemacie nie ma kolumn na dane pacjentów (PESEL, pacjent, adres, telefon, data urodzenia)', r == (True, ''), r)
r = sql("SELECT string_agg(table_name||'.'||column_name, ', ') FROM information_schema.columns WHERE table_schema='app' AND table_name='saved_descriptions' AND data_type='text' AND column_name NOT IN ('module','status','client_key')")
chk('zapisana wizyta nie ma pola na treść opisu (decyzja 1)', r == (True, ''), r)
# ---- konta (migracja 0002) ----
r = as_('gabinet_app', A, "SELECT count(*) FROM app.rate_limits"); chk('użytkownik nie czyta tabeli limitów prób', denied(r), r)
r = as_('gabinet_app', A, "SELECT count(*) FROM app.mfa_recovery_codes"); chk('użytkownik nie czyta kodów zapasowych 2FA (nawet skrótów)', denied(r), r)
r = as_('gabinet_admin', None, "SELECT count(*) FROM app.mfa_recovery_codes"); chk('administrator nie czyta kodów zapasowych 2FA', denied(r), r)
r = as_('gabinet_app', A, "SELECT password_hash FROM app.profiles"); chk('użytkownik nie odczyta nawet własnego skrótu hasła', denied(r), r)
r = as_('gabinet_app', A, "SELECT mfa_secret_enc FROM app.profiles"); chk('użytkownik nie odczyta zaszyfrowanego sekretu 2FA', denied(r), r)
r = as_('gabinet_app', A, "UPDATE app.profiles SET email_verified_at = now()"); chk('użytkownik nie potwierdzi sam adresu e-mail', denied(r), r)
r = as_('gabinet_app', A, "UPDATE app.profiles SET role = 'admin'"); chk('użytkownik nie nada sobie roli administratora', denied(r), r)
r = as_('gabinet_app', A, "SELECT token_hash FROM app.sessions"); chk('użytkownik nie odczyta skrótów tokenów sesji', denied(r), r)
r = as_('gabinet_app', A, "SELECT app.rate_hit('login:ip', '\\x" + '00'*32 + "', interval '1 minute')"); chk('użytkownik nie wywoła licznika limitów', denied(r), r)
r = as_('gabinet_app', A, "SELECT app.auth_cleanup()"); chk('użytkownik nie wywoła sprzątania', denied(r), r)
k = "'\\x" + 'ab'*32 + "'"
r = [as_('gabinet_auth', None, f"SELECT app.rate_hit('login:email', {k}, interval '15 minutes')")[1] for _ in range(3)]
chk('licznik prób rośnie w oknie czasowym', r == ['1', '2', '3'], r)
sql(f"UPDATE app.rate_limits SET window_start = now() - interval '16 minutes' WHERE key_hash = {k}")
r = as_('gabinet_auth', None, f"SELECT app.rate_hit('login:email', {k}, interval '15 minutes')"); chk('po upływie okna licznik startuje od 1', r == (True, '1'), r)
sql(f"INSERT INTO app.security_events(user_id,type,ip_prefix,created_at) VALUES ('{A}','login_ok','83.21.140.0/24', now() - interval '91 days'), ('{A}','login_ok','83.21.141.0/24', now() - interval '10 days')")
r = as_('gabinet_auth', None, "SELECT app.auth_cleanup()")
r2 = sql(f"SELECT string_agg(coalesce(host(ip_prefix),'-'), ',' ORDER BY created_at) FROM app.security_events WHERE user_id='{A}' AND type='login_ok'")
chk('sprzątanie: skrócone IP usuwane po 90 dniach, nowsze zostają', r[0] and r2 == (True, '-,83.21.141.0'), (r, r2))
r = as_('gabinet_auth', None, f"INSERT INTO app.security_events(user_id,type) VALUES ('{A}','nieznany_typ')"); chk('nieznany typ zdarzenia odrzucony', not r[0], r)
# ---- katalog NFZ (migracja 0003) ----
r = as_('gabinet_app', A, "SELECT count(*) FROM app.nfz_catalog"); chk('katalog NFZ: 23 kody widoczne dla użytkownika', r == (True, '23'), r)
r = as_('gabinet_app', A, "UPDATE app.nfz_catalog SET points = 999 WHERE code = 'ST01'"); chk('użytkownik nie zmieni punktów w katalogu NFZ', denied(r), r)
r = as_('gabinet_app', A, "INSERT INTO app.nfz_catalog(code,name,points,source,verified_at,definition) VALUES ('ZZ99','x',1,'x',current_date,'{}')"); chk('użytkownik nie doda kodu do katalogu NFZ', denied(r), r)
r = as_('gabinet_admin', None, "UPDATE app.nfz_catalog SET points = 1 WHERE code = 'ST01'"); chk('administrator też nie zmieni katalogu z aplikacji', denied(r), r)
r = sql("SELECT count(*) FROM app.nfz_catalog WHERE source !~ 'Zarządzenie Prezesa NFZ nr (95/2026|44/2025)/DSOZ'"); chk('każdy kod ma źródło (zarządzenie DSOZ)', r == (True, '0'), r)
r = sql("INSERT INTO app.nfz_catalog(code,name,points,verified_at,definition) VALUES ('ZZ98','x',1,current_date,'{}')"); chk('kod bez źródła odrzucony przez bazę', not r[0], r)
# ---- historia wizyt (migracja 0004): identyfikator z urządzenia nie pomieści tekstu ----
r = as_('gabinet_app', A, f"INSERT INTO app.saved_descriptions(owner_id,client_id,client_key,module,visit_date,seq_no) VALUES ('{A}',gen_random_uuid(),'Pacjent Jan Kowalski ząb 16','nfz',current_date,1)")
chk('client_key: tylko identyfikator (litery, cyfry, - _ ; bez spacji i polskich znaków)', not r[0] and 'check' in r[1].lower(), r)
r = as_('gabinet_app', A, f"INSERT INTO app.saved_descriptions(owner_id,client_id,client_key,module,visit_date,seq_no,meta) VALUES ('{A}',gen_random_uuid(),'v1','nfz',current_date,1,jsonb_build_object('x',repeat('a',9000)))")
chk('meta wpisu: limit 8 KB (nie zmieści treści opisu)', not r[0], r)
print(f'--- izolacja i uprawnienia: {ok} OK, {bad} błędów'); sys.exit(1 if bad else 0)
