# Wspólne narzędzia testów przeglądarkowych (Chrome + Playwright).
import glob, json, os, re, subprocess, sys
from playwright.sync_api import sync_playwright  # noqa: F401
URL = os.environ['E2E_URL']; MAILS = os.environ['E2E_MAILS']; DB = os.environ['E2E_DB']
CHROME = '/usr/bin/google-chrome'
class T:
    def __init__(self): self.ok = 0; self.bad = 0
    def chk(self, name, cond, info=''):
        print(('OK   ' if cond else 'BŁĄD ') + name + ('' if cond else f'  | {info}')); self.ok += bool(cond); self.bad += (not cond)
    def done(self, title):
        print(f'--- {title}: {self.ok} OK, {self.bad} błędów'); sys.exit(1 if self.bad else 0)
def sql(q):
    return subprocess.run(['psql', '-X', '-At', '-d', DB, '-c', q], capture_output=True, text=True).stdout.strip()
def mails(to, subj=''):
    out = []
    for f in sorted(glob.glob(MAILS + '/*.json')):
        m = json.load(open(f))
        if m['to'] == to and subj in m['subject']: out.append(m)
    return out
def fill(pg, **kw):
    for k, v in kw.items(): pg.fill(f'[name="{k}"]', v)
def submit(pg, text=None, scope=None):
    before = pg.url
    root = scope or pg
    (root.get_by_role('button', name=text, exact=True) if text else root.locator('button[type=submit]').last).click()
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
def konto(br, name, email, pwd, ua=None):
    """Nowe konto (rejestracja przez formularz) i zalogowany kontekst przeglądarki."""
    ctx = br.new_context(user_agent=ua) if ua else br.new_context(); pg = ctx.new_page()
    pg.goto(URL + '/rejestracja'); fill(pg, name=name, email=email, password=pwd, password2=pwd); pg.check('[name="zgoda"]')
    submit(pg, 'Załóż konto')
    pg.goto(URL + '/logowanie'); fill(pg, email=email, password=pwd); submit(pg, 'Zaloguj')
    return ctx, pg
