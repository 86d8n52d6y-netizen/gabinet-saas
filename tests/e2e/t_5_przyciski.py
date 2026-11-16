# Przegląd przycisków (wymaganie „bez atrap i niedziałających przycisków”): w każdym module i na każdej zakładce klika
# kolejno widoczne przyciski akcji (bez usuwających) i sprawdza, że nie ma błędów JavaScript ani błędów serwera (5xx).
# Strony konta: każdy link menu otwiera się (200) bez błędów.
from pomoc import *
t = T(); chk = t.chk
SKIP = ('del', 'reset', 'clear', 'crash', 'rm', 'hold', 'demo-on', 'modal-bg', 'tdefault', 'detach')

def login2(br, email, pwd):
    c = br.new_context(bypass_csp=True, accept_downloads=True); p_ = c.new_page()
    p_.goto(URL + '/logowanie'); fill(p_, email=email, password=pwd); submit(p_, 'Zaloguj'); return c, p_

def sweep(pg, sel_attr, tabs_sel, label):
    errs = []; bad = []
    pg.on('pageerror', lambda e: errs.append(str(e)[:160]))
    pg.on('response', lambda r: bad.append(f'{r.status} {r.url}') if r.status >= 500 else None)
    clicked = 0
    tabs = pg.locator(tabs_sel).count() if tabs_sel else 1
    for ti in range(max(tabs, 1)):
        if tabs_sel and tabs:
            try: pg.locator(tabs_sel).nth(ti).click(timeout=2000); pg.wait_for_timeout(250)
            except Exception: continue
        seen = set()
        for _ in range(60):
            els = pg.locator(f'[{sel_attr}]:visible')
            n = els.count(); target = None
            for i in range(n):
                e = els.nth(i)
                try: a = e.get_attribute(sel_attr) or ''; key = a + '|' + (e.inner_text(timeout=300) or '')[:30]
                except Exception: continue
                if key in seen or any(s in a for s in SKIP) or a in ('tab', 'step'): continue
                seen.add(key); target = e; break
            if target is None: break
            try:
                with pg.expect_download(timeout=600) as _d: target.click(timeout=1500)
            except Exception: pass
            clicked += 1; pg.wait_for_timeout(120)
            if pg.url.split('#')[0].split('?')[0] != URL + label: pg.go_back(); pg.wait_for_timeout(400)
            try: pg.keyboard.press('Escape')
            except Exception: pass
    return clicked, errs, bad

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    c0, p0 = konto(br, 'Lekarz P', 'p.5@example.com', 'zielony-kubek-na-biurku')
    p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name='Gabinet A', pct='30'); submit(p0, 'Dodaj gabinet'); c0.close()
    ctx, pg = login2(br, 'p.5@example.com', 'zielony-kubek-na-biurku')
    pg.on('dialog', lambda d: d.dismiss())
    for path in ['/konto', '/konto/bezpieczenstwo', '/zarobki', '/katalog-nfz', '/gabinety', '/ustawienia', '/import']:
        r = pg.goto(URL + path); chk(f'strona {path} otwiera się (200)', r.status == 200, r.status)
    pg.goto(URL + '/kalendarz'); pg.wait_for_function("window.Kal&&Kal.UI.loaded", timeout=20000)
    n, e, b = sweep(pg, 'data-a', '#tabs [data-a="tab"], #tabs button', '/kalendarz')
    chk(f'Kalendarz: {n} przycisków kliknięte – bez błędów JS i 5xx', n > 30 and not e and not b, (n, e[:3], b[:3]))
    pg.goto(URL + '/opisy-nfz'); pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000)
    pg.locator('[data-act="code"]').first.click(); pg.wait_for_timeout(200)
    n, e, b = sweep(pg, 'data-act', '#steps button', '/opisy-nfz')
    chk(f'Opisy NFZ: {n} przycisków kliknięte – bez błędów JS i 5xx', n > 15 and not e and not b, (n, e[:3], b[:3]))
    pg.goto(URL + '/opisy-prywatne'); pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000)
    n, e, b = sweep(pg, 'data-a', '#tabs button', '/opisy-prywatne')
    chk(f'Opisy prywatne: {n} przycisków kliknięte – bez błędów JS i 5xx', n > 15 and not e and not b, (n, e[:3], b[:3]))
    br.close()
t.done('przegląd przycisków')
