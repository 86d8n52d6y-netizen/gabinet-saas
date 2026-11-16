# Faza 3 – konta i logowanie: test w prawdziwej przeglądarce (Chrome, Playwright).
# Uruchamiany przez tests/e2e/uruchom.sh (świeża baza, serwer produkcyjny, poczta zapisywana do plików).
import base64, glob, hashlib, hmac, json, os, re, struct, subprocess, sys, time
from playwright.sync_api import sync_playwright

URL = os.environ['E2E_URL']; MAILS = os.environ['E2E_MAILS']; DB = os.environ['E2E_DB']
CHROME = '/usr/bin/google-chrome'
UA2 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1'
ok = bad = 0
def chk(name, cond, info=''):
    global ok, bad
    print(('OK   ' if cond else 'BŁĄD ') + name + ('' if cond else f'  | {info}')); ok += bool(cond); bad += (not cond)
def sql(q):
    r = subprocess.run(['psql', '-X', '-At', '-d', DB, '-c', q], capture_output=True, text=True)
    return r.stdout.strip()
def mails(to, subj=''):
    out = []
    for f in sorted(glob.glob(MAILS + '/*.json')):
        m = json.load(open(f))
        if m['to'] == to and subj in m['subject']: out.append(m)
    return out
def link(m, path):
    return re.search(re.escape(path) + r'\?t=([A-Za-z0-9_-]{43})', m['text']).group(0)
def totp(b32, at=None):
    key = base64.b32decode(b32.replace(' ', '') + '=' * (-len(b32.replace(' ', '')) % 8))
    step = int((at or time.time()) // 30)
    h = hmac.new(key, struct.pack('>Q', step), 'sha1').digest(); o = h[-1] & 15
    return '%06d' % ((struct.unpack('>I', h[o:o+4])[0] & 0x7fffffff) % 1000000)
def fresh_code(b32):
    # nowy kod (inne okno 30 s niż poprzednio użyte) – czekamy na zmianę okna, jeśli trzeba
    s = int(time.time() // 30)
    while int(time.time() // 30) == s: time.sleep(0.5)
    return totp(b32)

def fill(pg, **kw):
    for k, v in kw.items(): pg.fill(f'[name="{k}"]', v)
def submit(pg, text=None):
    before = pg.url
    (pg.get_by_role('button', name=text) if text else pg.locator('form button[type=submit]').last).click()
    # czekamy aż akcja się zakończy: przycisk znów aktywny, a przy przekierowaniu – nowy adres
    for _ in range(100):
        pg.wait_for_timeout(100)
        if pg.locator('button[disabled]').count() == 0: break
    pg.wait_for_load_state('networkidle')
    for _ in range(20):
        if pg.url != before or pg.locator('.msg').count(): break
        pg.wait_for_timeout(100)
def msg(pg):
    pg.wait_for_timeout(150)
    return ' '.join(pg.locator('.msg').all_inner_texts())
def register(pg, name, email, p1, p2=None, zgoda=True):
    pg.goto(URL + '/rejestracja')
    fill(pg, name=name, email=email, password=p1, password2=p2 or p1)
    if zgoda: pg.check('[name="zgoda"]')
    else: pg.evaluate("document.querySelector('[name=zgoda]').required=false")
    pg.evaluate("document.querySelectorAll('input').forEach(i=>{i.removeAttribute('minlength');i.removeAttribute('required')})")
    submit(pg, 'Załóż konto')
def login(pg, email, pwd):
    pg.goto(URL + '/logowanie'); fill(pg, email=email, password=pwd); submit(pg, 'Zaloguj')

A, B = 'anna.test@example.com', 'bartek.test@example.com'
PA, PB = 'zielony-kubek-na-biurku', 'niebieska-lampa-w-oknie'

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx = br.new_context(); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))

    # --- nagłówki i strony publiczne
    r = pg.goto(URL + '/')
    h = r.headers
    chk('strona główna działa', r.status == 200 and 'Gabinet' in pg.content())
    chk('nagłówek CSP z frame-ancestors none', "frame-ancestors 'none'" in h.get('content-security-policy', ''), h.get('content-security-policy'))
    chk('nagłówki nosniff i X-Frame-Options', h.get('x-content-type-options') == 'nosniff' and h.get('x-frame-options') == 'DENY')
    chk('/stan niedostępny bez STATUS_DETAILS (produkcja)', pg.goto(URL + '/stan').status == 404)
    z = pg.goto(URL + '/api/zdrowie').json()
    chk('/api/zdrowie bez szczegółów (wersja bazy ukryta)', z.get('ok') is True and all('info' not in c for c in z.get('checks', [])), z)
    pg.goto(URL + '/konto'); chk('/konto bez logowania → przekierowanie do logowania', '/logowanie' in pg.url)

    # --- rejestracja: walidacja po stronie serwera
    register(pg, 'Anna Test', A, 'krotkie'); chk('za krótkie hasło odrzucone', 'co najmniej 12' in msg(pg), msg(pg))
    register(pg, 'Anna Test', A, 'qwerty123456'); chk('popularne hasło odrzucone', 'popularne' in msg(pg), msg(pg))
    register(pg, 'Anna Test', A, 'anna.test-haslo-1'); chk('hasło z adresem e-mail odrzucone', 'adresu e-mail' in msg(pg), msg(pg))
    register(pg, 'Anna Test', A, PA, PA + 'x'); chk('różne hasła odrzucone', 'nie są takie same' in msg(pg), msg(pg))
    register(pg, 'Anna Test', A, PA, zgoda=False); chk('bez potwierdzenia „bez danych pacjentów” odrzucone', 'danych pacjentów' in msg(pg), msg(pg))
    chk('po błędach konto nie powstało', sql(f"SELECT count(*) FROM app.profiles WHERE email='{A}'") == '0')
    register(pg, 'Anna Test', A, PA)
    chk('rejestracja → strona „sprawdź skrzynkę”', '/rejestracja/sprawdz-poczte' in pg.url, pg.url)
    mv = mails(A, 'potwierdź adres')
    chk('e-mail weryfikacyjny wysłany', len(mv) == 1, mv)
    chk('hasło zapisane jako Argon2id (nie jawnie)', sql(f"SELECT password_hash LIKE '$argon2id$v=19$m=65536,t=3,p=1$%' AND position('{PA}' in password_hash)=0 FROM app.profiles WHERE email='{A}'") == 't')
    chk('okres próbny 3 miesiące utworzony', sql(f"SELECT s.status||':'||(s.trial_end = s.trial_start + interval '3 months') FROM app.subscriptions s JOIN app.profiles p ON p.id=s.user_id WHERE p.email='{A}'") == 'trial_active:true')
    chk('token e-mail zapisany jako skrót (nie jawnie)', sql("SELECT count(*) FROM app.email_tokens WHERE purpose='verify'") == '1' and link(mv[0], '/weryfikacja').split('t=')[1] not in sql("SELECT encode(token_hash,'escape') FROM app.email_tokens"))
    register(pg, 'Ktoś Inny', A, 'inne-dlugie-haslo-xyz')
    chk('ponowna rejestracja tego samego e-maila: ta sama odpowiedź (nie zdradza konta)', '/rejestracja/sprawdz-poczte' in pg.url)
    chk('… i e-mail „próba założenia konta” zamiast drugiego konta', len(mails(A, 'próba założenia')) == 1 and sql(f"SELECT count(*) FROM app.profiles WHERE email='{A}'") == '1')

    # --- logowanie przed potwierdzeniem, weryfikacja e-mail
    login(pg, A, 'zle-haslo-123456'); chk('złe hasło: ogólny komunikat', 'Nieprawidłowy e-mail lub hasło' in msg(pg), msg(pg))
    login(pg, 'nie.ma@example.com', PA); chk('nieistniejące konto: ten sam komunikat', 'Nieprawidłowy e-mail lub hasło' in msg(pg))
    login(pg, A, PA); chk('logowanie → /konto', pg.url.endswith('/konto'), pg.url)
    chk('baner „potwierdź adres e-mail”', 'Potwierdź adres e-mail' in pg.content())
    chk('status: okres próbny z datą', 'Okres próbny' in pg.content() and 'Masz pełny dostęp' in pg.content())
    ck = [c for c in ctx.cookies() if c['name'].startswith('gabinet_sesja')]
    chk('ciasteczko sesji: HttpOnly, SameSite=Lax', len(ck) == 1 and ck[0]['httpOnly'] and ck[0]['sameSite'] == 'Lax', ck)
    chk('w bazie tylko skrót tokenu sesji', ck and sql("SELECT count(*) FROM app.sessions WHERE revoked_at IS NULL") == '1' and ck[0]['value'] not in sql("SELECT encode(token_hash,'hex') FROM app.sessions"))
    pg.goto(URL + link(mv[0], '/weryfikacja'))
    chk('link weryfikacyjny nie potwierdza samym otwarciem (ochrona przed skanerami poczty)', sql(f"SELECT email_verified_at IS NULL FROM app.profiles WHERE email='{A}'") == 't')
    submit(pg, 'Potwierdzam adres e-mail')
    chk('potwierdzenie → /konto, adres potwierdzony', 'potwierdzono=1' in pg.url and 'potwierdzony' in pg.content(), pg.url)
    pg.goto(URL + link(mv[0], '/weryfikacja')); submit(pg, 'Potwierdzam adres e-mail')
    chk('ponowne użycie linku odrzucone', 'wygasł albo został już użyty' in msg(pg), msg(pg))
    pg.goto(URL + '/konto'); pg.fill('[name=name]', 'Anna Testowa'); submit(pg, 'Zapisz')
    chk('zmiana imienia (zapis rolą użytkownika z RLS)', 'Zapisano' in msg(pg) and sql(f"SELECT display_name FROM app.profiles WHERE email='{A}'") == 'Anna Testowa')

    # --- drugie urządzenie, lista urządzeń, wylogowanie zdalne
    ctx2 = br.new_context(user_agent=UA2); pg2 = ctx2.new_page()
    login(pg2, A, PA)
    chk('logowanie z drugiego urządzenia', pg2.url.endswith('/konto'))
    chk('e-mail „nowe urządzenie” (Safari, iPhone)', any('Safari, iPhone' in m['text'] for m in mails(A, 'nowego urządzenia')))
    pg.goto(URL + '/konto/bezpieczenstwo')
    rows = pg.locator('tbody tr').filter(has=pg.locator('button', has_text='Wyloguj'))
    chk('lista urządzeń: 2 sesje, „to urządzenie” oznaczone', rows.count() == 2 and 'to urządzenie' in pg.content() and 'Safari, iPhone' in pg.content(), rows.count())
    pg.locator('tr', has_text='Safari, iPhone').get_by_role('button', name='Wyloguj').click(); pg.wait_for_load_state('networkidle')
    pg2.goto(URL + '/konto'); chk('zdalne wylogowanie drugiego urządzenia działa', '/logowanie' in pg2.url, pg2.url)

    # --- izolacja: konto B nie wyloguje sesji A (podmiana identyfikatora w formularzu)
    ctxb = br.new_context(); pgb = ctxb.new_page()
    register(pgb, 'Bartek Test', B, PB); login(pgb, B, PB)
    a_sid = sql(f"SELECT s.id FROM app.sessions s JOIN app.profiles p ON p.id=s.user_id WHERE p.email='{A}' AND s.revoked_at IS NULL LIMIT 1")
    pgb.goto(URL + '/konto/bezpieczenstwo')
    pgb.evaluate(f"document.querySelector('input[name=id]').value='{a_sid}'")
    pgb.locator('tbody form button').first.click(); pgb.wait_for_load_state('networkidle')
    chk('B nie może wylogować sesji A (RLS)', sql(f"SELECT revoked_at IS NULL FROM app.sessions WHERE id='{a_sid}'") == 't')
    pg.goto(URL + '/konto'); chk('… A nadal zalogowana', pg.url.endswith('/konto'))
    chk('B widzi tylko swoje urządzenia', 'Safari, iPhone' not in pgb.content())

    # --- zmiana hasła
    login(pg2, A, PA)
    pg.goto(URL + '/konto/bezpieczenstwo')
    f = pg.locator('form', has=pg.get_by_role('button', name='Zmień hasło'))
    f.locator('[name=current]').fill('zle-obecne-haslo'); f.locator('[name=password]').fill('nowe-haslo-do-gabinetu'); f.locator('[name=password2]').fill('nowe-haslo-do-gabinetu')
    submit(pg, 'Zmień hasło'); chk('zmiana hasła: złe obecne hasło odrzucone', 'Obecne hasło jest nieprawidłowe' in msg(pg))
    f = pg.locator('form', has=pg.get_by_role('button', name='Zmień hasło'))
    f.locator('[name=current]').fill(PA); f.locator('[name=password]').fill('nowe-haslo-do-gabinetu'); f.locator('[name=password2]').fill('nowe-haslo-do-gabinetu')
    submit(pg, 'Zmień hasło'); chk('hasło zmienione', 'Hasło zmienione' in msg(pg), msg(pg))
    pg2.goto(URL + '/konto'); chk('… inne urządzenia wylogowane', '/logowanie' in pg2.url)
    pg.goto(URL + '/konto'); chk('… bieżące urządzenie zostaje zalogowane', pg.url.endswith('/konto'))
    chk('… e-mail o zmianie hasła', len(mails(A, 'hasło zostało zmienione')) == 1)
    PA = 'nowe-haslo-do-gabinetu'

    # --- weryfikacja dwuetapowa
    pg.goto(URL + '/konto/bezpieczenstwo')
    pg.fill('#mfa-cur', PA); submit(pg, 'Włącz weryfikację dwuetapową')
    chk('2FA: kod QR i klucz pokazane', pg.locator('img.qr').count() == 1 and pg.locator('.mono').count() == 1)
    secret = pg.locator('.mono').inner_text()
    chk('sekret 2FA w bazie zaszyfrowany (nie jawnie)', secret.replace(' ', '') not in sql(f"SELECT encode(mfa_pending_enc,'escape') FROM app.profiles WHERE email='{A}'"))
    pg.fill('#mfa-code', '000000'); submit(pg, 'Potwierdź i włącz'); chk('2FA: zły kod odrzucony', 'Nieprawidłowy kod' in msg(pg), msg(pg))
    pg.fill('#mfa-code', totp(secret)); submit(pg, 'Potwierdź i włącz')
    pg.wait_for_selector('.codes span', timeout=5000)
    codes = pg.locator('.codes span').all_inner_texts()
    chk('2FA włączone, 10 kodów zapasowych', len(codes) == 10 and all(re.fullmatch(r'[a-z2-9]{5}-[a-z2-9]{5}', c) for c in codes), codes)
    chk('kody zapasowe w bazie tylko jako skróty', sql(f"SELECT count(*) FROM app.mfa_recovery_codes") == '10' and codes[0] not in sql("SELECT encode(code_hash,'escape') FROM app.mfa_recovery_codes"))
    pg.get_by_role('link', name='Zapisałem kody').click(); pg.wait_for_load_state('networkidle')
    pg.get_by_role('button', name='Wyloguj').first.click(); pg.wait_for_load_state('networkidle')
    login(pg, A, PA); chk('logowanie z 2FA → strona kodu', '/logowanie/2fa' in pg.url, pg.url)
    pg.goto(URL + '/konto'); chk('bez kodu 2FA /konto niedostępne', '/logowanie/2fa' in pg.url, pg.url)
    pg.fill('[name=code]', '123456'); submit(pg, 'Potwierdź'); chk('zły kod przy logowaniu odrzucony', 'Nieprawidłowy kod' in msg(pg))
    c1 = fresh_code(secret)
    pg.fill('[name=code]', c1); submit(pg, 'Potwierdź'); chk('poprawny kod → /konto', pg.url.endswith('/konto'), pg.url)
    pg.get_by_role('button', name='Wyloguj').first.click(); pg.wait_for_load_state('networkidle')
    login(pg, A, PA); pg.fill('[name=code]', c1); submit(pg, 'Potwierdź')
    chk('ten sam kod 2FA nie działa drugi raz', 'Nieprawidłowy kod' in msg(pg), msg(pg))
    pg.fill('[name=code]', codes[0]); submit(pg, 'Potwierdź'); chk('kod zapasowy działa', pg.url.endswith('/konto'), pg.url)
    pg.get_by_role('button', name='Wyloguj').first.click(); pg.wait_for_load_state('networkidle')
    login(pg, A, PA); pg.fill('[name=code]', codes[0]); submit(pg, 'Potwierdź')
    chk('kod zapasowy jest jednorazowy', 'Nieprawidłowy kod' in msg(pg))
    pg.fill('[name=code]', fresh_code(secret)); submit(pg, 'Potwierdź')
    pg.goto(URL + '/konto/bezpieczenstwo')
    pg.fill('#d-cur', PA); pg.fill('#d-code', fresh_code(secret)); submit(pg, 'Wyłącz weryfikację dwuetapową')
    chk('po wyłączeniu strona od razu pokazuje stan „wyłączona”', pg.locator('#mfa .badge').count() == 0 and pg.locator('#mfa-cur').count() == 1)
    chk('2FA wyłączone (hasło + kod)', 'mfa=wylaczone' in pg.url and sql(f"SELECT mfa_secret_enc IS NULL FROM app.profiles WHERE email='{A}'") == 't', pg.url)
    chk('e-maile o włączeniu i wyłączeniu 2FA', len(mails(A, 'włączono weryfikację')) == 1 and len(mails(A, 'wyłączono weryfikację')) == 1)

    # --- reset hasła
    ctxr = br.new_context(); pr = ctxr.new_page()
    pr.goto(URL + '/reset'); pr.fill('[name=email]', 'nie.ma@example.com'); submit(pr, 'Wyślij link')
    m_unknown = msg(pr)
    pr.goto(URL + '/reset'); pr.fill('[name=email]', A); submit(pr, 'Wyślij link')
    chk('reset: ta sama odpowiedź dla istniejącego i nieistniejącego konta', m_unknown == msg(pr) and 'Jeśli konto' in m_unknown, (m_unknown, msg(pr)))
    chk('reset: e-mail tylko do istniejącego konta', len(mails(A, 'ustaw nowe hasło')) == 1 and len(mails('nie.ma@example.com')) == 0)
    rl = link(mails(A, 'ustaw nowe hasło')[0], '/reset/nowe')
    pr.goto(URL + rl); fill(pr, password='krotkie', password2='krotkie')
    pr.evaluate("document.querySelectorAll('input').forEach(i=>i.removeAttribute('minlength'))"); submit(pr, 'Zapisz nowe hasło')
    chk('reset: słabe hasło odrzucone, link nadal ważny', 'co najmniej 12' in msg(pr))
    fill(pr, password='trzecie-haslo-gabinetu', password2='trzecie-haslo-gabinetu'); submit(pr, 'Zapisz nowe hasło')
    chk('reset: nowe hasło zapisane → logowanie', 'haslo=zmienione' in pr.url, pr.url)
    pg.goto(URL + '/konto'); chk('reset: wszystkie sesje wylogowane', '/logowanie' in pg.url)
    pr.goto(URL + rl); fill(pr, password='czwarte-haslo-gabinetu', password2='czwarte-haslo-gabinetu'); submit(pr, 'Zapisz nowe hasło')
    chk('reset: link jednorazowy', 'wygasł albo został już użyty' in msg(pr))
    login(pr, A, 'nowe-haslo-do-gabinetu'); chk('stare hasło nie działa', 'Nieprawidłowy' in msg(pr))
    login(pr, A, 'trzecie-haslo-gabinetu'); chk('nowe hasło działa', pr.url.endswith('/konto'))

    # --- limit prób logowania
    ctxl = br.new_context(); pl = ctxl.new_page()
    for i in range(5): login(pl, B, f'zle-haslo-{i}-xxxxxx')
    login(pl, B, PB); chk('po 5 nieudanych próbach nawet poprawne hasło jest blokowane', 'Zbyt wiele prób' in msg(pl), msg(pl))
    chk('w tabeli limitów brak jawnych e-maili', B not in sql("SELECT string_agg(encode(key_hash,'escape'),'') FROM app.rate_limits"))
    sql("DELETE FROM app.rate_limits WHERE bucket='login:email'")
    login(pl, B, PB); chk('po upływie blokady logowanie działa', pl.url.endswith('/konto'))

    # --- dziennik bezpieczeństwa
    types = sql(f"SELECT string_agg(DISTINCT type, ',') FROM app.security_events e JOIN app.profiles p ON p.id=e.user_id WHERE p.email='{A}'").split(',')
    need = {'register','login_ok','login_fail','email_verified','new_device','password_change','mfa_on','mfa_off','mfa_fail','recovery_code_used','reset_requested','password_reset','logout'}
    chk('dziennik bezpieczeństwa: wszystkie typy zdarzeń', need <= set(types), need - set(types))
    chk('dziennik: IP tylko skrócone (/24)', all(x.endswith('/24') for x in sql("SELECT DISTINCT ip_prefix FROM app.security_events WHERE ip_prefix IS NOT NULL").split()) )
    pg.goto(URL + '/logowanie'); fill(pg, email=A, password='trzecie-haslo-gabinetu'); submit(pg, 'Zaloguj')
    pg.goto(URL + '/konto/bezpieczenstwo'); chk('historia zdarzeń widoczna na stronie (15 najnowszych)', 'Reset hasła' in pg.content() and 'Wyłączono 2FA' in pg.content() and pg.locator('#hist ~ table tr').count() == 15, pg.locator('#hist ~ table tr').count())
    chk('brak błędów JavaScript w przeglądarce', not errs, errs)
    br.close()

print(f'--- konta i logowanie: {ok} OK, {bad} błędów')
sys.exit(1 if bad else 0)
