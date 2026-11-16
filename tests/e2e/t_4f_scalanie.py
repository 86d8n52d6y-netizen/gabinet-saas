# Synchronizacja między urządzeniami (specyfikacja 5.5): materiały (cennik) zmieniane na dwóch urządzeniach jednocześnie – scalanie
# bez utraty zmian, kontrola wersji w API, informacja „Zmiany z innego urządzenia – odśwież”; gabinet z dyżuru w Opisach (G.dayClinic).
import json, datetime, time, urllib.request
from pomoc import *
t = T(); chk = t.chk
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat()

def login2(br, email, pwd):
    c = br.new_context(bypass_csp=True); p_ = c.new_page()
    p_.goto(URL + '/logowanie'); fill(p_, email=email, password=pwd); submit(p_, 'Zaloguj'); return c, p_
def api(path, body, cookie):
    rq = urllib.request.Request(URL + path, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json', 'Origin': URL, 'Cookie': cookie}, method='POST')
    try:
        with urllib.request.urlopen(rq) as r: return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read() or b'{}')
def cookie_of(ctx): return '; '.join(f"{c['name']}={c['value']}" for c in ctx.cookies() if c['name'].startswith('gabinet_sesja'))
def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(300)
def cen(): return json.loads(sql("SELECT data::text FROM app.user_blobs WHERE key='pryw:cennik'") or '{}')

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    c0, p0 = konto(br, 'Lekarz S', 's.4f@example.com', 'zielony-kubek-na-biurku')
    for n in ['Gabinet A', 'Gabinet B']:
        p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name=n, pct='30'); submit(p0, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet A'"); B = sql("SELECT id FROM app.clinics WHERE name='Gabinet B'")
    c0.close()
    c1, p1 = login2(br, 's.4f@example.com', 'zielony-kubek-na-biurku'); c2, p2 = login2(br, 's.4f@example.com', 'zielony-kubek-na-biurku')
    errs = []
    for x in (p1, p2): x.on('pageerror', lambda e: errs.append(str(e)))
    ck = cookie_of(c1)

    # API: kontrola wersji materiałów
    st, j = api('/api/dane', {'key': 'pryw:cennik', 'data': {'gab': {}}, 'base': 0}, ck)
    chk('API materiałów: pierwszy zapis od wersji 0 → wersja 1', st == 200 and j.get('version') == 1, (st, j))
    st, j = api('/api/dane', {'key': 'pryw:cennik', 'data': {'gab': {'x': 1}}, 'base': 0}, ck)
    chk('API materiałów: zapis od nieaktualnej wersji → 409 z aktualnymi danymi (nic nie nadpisane)', st == 409 and j['conflict']['version'] == 1 and cen() == {'gab': {}}, (st, j))

    # dwa urządzenia otwierają Opisy prywatne z tym samym cennikiem; każde zmienia inną procedurę
    for x in (p1, p2): x.goto(URL + '/opisy-prywatne'); ready(x)
    p1.evaluate(f"async()=>{{const c=await G.store('kv').get('pryw:cennik')||{{gab:{{}}}};c.gab['{A}']={{pct:40,items:{{'zach-kompozyt':{{c:40000}}}}}};await G.store('kv').put('pryw:cennik',c);}}")
    p1.wait_for_timeout(1200)
    p2.evaluate(f"async()=>{{const c=await G.store('kv').get('pryw:cennik')||{{gab:{{}}}};c.gab['{B}']={{pct:35,items:{{'hig-skaling':{{c:25000}}}}}};await G.store('kv').put('pryw:cennik',c);}}")
    p2.wait_for_timeout(2000)
    g = cen().get('gab', {})
    chk('cennik zmieniony na dwóch urządzeniach: na koncie oba gabinety (A 400 zł/40%, B 250 zł/35%)',
        g.get(A, {}).get('items', {}).get('zach-kompozyt', {}).get('c') == 40000 and g.get(B, {}).get('items', {}).get('hig-skaling', {}).get('c') == 25000, g)
    loc = p2.evaluate("G.store('kv').get('pryw:cennik')")
    chk('urządzenie 2 ma na miejscu scaloną wersję', A in loc.get('gab', {}) and B in loc.get('gab', {}), loc)
    chk('urządzenie 2: „Zmiany z innego urządzenia – odśwież”', 'odśwież' in p2.inner_text('#gsync'), p2.inner_text('#gsync'))
    p1.evaluate("document.dispatchEvent(new Event('visibilitychange'))"); p1.wait_for_timeout(1000)
    chk('urządzenie 1 po powrocie do karty: informacja o zmianach z innego urządzenia', 'odśwież' in p1.inner_text('#gsync'), p1.inner_text('#gsync'))
    p1.click('#greload'); ready(p1)
    loc = p1.evaluate("G.store('kv').get('pryw:cennik')")
    chk('po odświeżeniu urządzenie 1 ma cennik z obu urządzeń', A in loc.get('gab', {}) and B in loc.get('gab', {}), loc)

    # gabinet z dyżuru w Kalendarzu → Opisy (automatyczny wybór gabinetu, jak w obecnej aplikacji)
    st, j = api('/api/kal/dokumenty', {'put': {f'm{TODAY[:7]}': {'shifts': [{'id': 'd1', 'date': TODAY, 'clinicId': B, 'start': '00:00', 'end': '23:59', 'status': 'planned'}], 'off': {}, 'inv': {}, 'costs': []}}}, ck)
    chk('dyżur dziś w gabinecie B zapisany', st == 200, (st, j))
    p1.goto(URL + '/opisy-prywatne'); ready(p1)
    chk('Opisy prywatne: gabinet z dyżuru = B', p1.evaluate(f"G.dayClinic('{TODAY}','')") == B and p1.evaluate("S.gabAuto") == B, p1.evaluate("S.gabAuto"))
    p1.goto(URL + '/opisy-nfz'); p1.wait_for_function("typeof state!=='undefined'&&state.clinics", timeout=20000); p1.wait_for_timeout(500)
    chk('Opisy NFZ: gabinet z dyżuru = B', p1.evaluate("state.gabAuto") == B, p1.evaluate("state.gabAuto"))
    chk('brak błędów JavaScript', not errs, errs[:5])
    br.close()
t.done('synchronizacja i gabinet z dyżuru')
