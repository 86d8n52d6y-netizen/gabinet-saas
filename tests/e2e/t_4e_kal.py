# Etap 4e-1: Kalendarz w wersji SaaS – gabinety wspólne z całą aplikacją (w obie strony), dyżury na koncie i na drugim urządzeniu,
# zapis po utracie połączenia, podpowiedź „Wpisz jako obrót” z opisów, kolumna „Dyżury wg Kalendarza” w Zarobkach, kafelek na koncie,
# izolacja kont oraz porównanie Podsumowania / Rozliczeń / Terminów / Porównania form ze starą aplikacją (OPISY_DIR).
import json, os, subprocess, time, urllib.request, uuid, datetime
from pomoc import *
t = T(); chk = t.chk
OPISY = os.environ.get('OPISY_DIR'); OLD = 'http://127.0.0.1:8765'
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat()   # strefa jak w Kalendarzu (testy w listopadzie: CET)
MK = TODAY[:7]

def ready(pg): pg.wait_for_function("window.Kal&&Kal.UI.loaded===true&&Kal.Store.mode==='local'", timeout=20000); pg.wait_for_timeout(300)
PRE = "const clinic=id=>S().clinics.find(c=>c.id===id),clinics=()=>S().clinics;"
def K(pg, body, arg=None):
    """Kod w zasięgu uchwytu testowego Kalendarza (window.Kal: UI, Store, S, M, saveSettings, saveMonth, E, openEditor, render)."""
    return pg.evaluate("(a)=>{with(Kal){" + PRE + body + "}}", arg)
def synced(pg, timeout=8000):
    pg.wait_for_function("document.getElementById('gsync')&&document.getElementById('gsync').textContent.includes('zsynchronizowany')", timeout=timeout)
def login2(br, email, pwd):
    c = br.new_context(bypass_csp=True); p_ = c.new_page()
    p_.goto(URL + '/logowanie'); fill(p_, email=email, password=pwd); submit(p_, 'Zaloguj'); return c, p_
def api(path, body, cookie=None, origin=URL):
    h = {'Content-Type': 'application/json'}
    if origin: h['Origin'] = origin
    if cookie: h['Cookie'] = cookie
    rq = urllib.request.Request(URL + path, data=json.dumps(body).encode(), headers=h, method='POST')
    try:
        with urllib.request.urlopen(rq) as r: return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read() or b'{}')
def cookie_of(ctx): return '; '.join(f"{c['name']}={c['value']}" for c in ctx.cookies() if c['name'].startswith('gabinet_sesja'))
def month(): return json.loads(sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'") or '{}')
def wait_sql(q, want, n=40):
    for _ in range(n):
        v = sql(q)
        if v == want: return v
        time.sleep(0.25)
    return sql(q)

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    an = br.new_context(); pa = an.new_page(); pa.goto(URL + '/kalendarz')
    chk('bez logowania /kalendarz → logowanie', '/logowanie' in pa.url)
    chk('API Kalendarza bez logowania → 401', api('/api/kal/dokumenty', {'put': {}})[0] == 401)

    c0, p0 = konto(br, 'Lekarz A', 'a.4e@example.com', 'zielony-kubek-na-biurku')
    for n in ['Gabinet A', 'Gabinet B']:
        p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name=n, pct='30'); submit(p0, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet A'"); B = sql("SELECT id FROM app.clinics WHERE name='Gabinet B'")
    c0.close()

    ctx, pg = login2(br, 'a.4e@example.com', 'zielony-kubek-na-biurku')
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' and 'net::ERR' not in m.text and 'Failed to fetch' not in m.text else None)
    r = pg.goto(URL + '/kalendarz'); ready(pg)
    chk('Kalendarz otwiera się na koncie SaaS (pasek: „Kalendarz” aktywny)', r.status == 200 and pg.inner_text('#gbar a.on') == 'Kalendarz')
    chk('gabinety z konta w Kalendarzu (te same identyfikatory)', K(pg, "return clinics().map(c=>c.id).join(',')") == f'{A},{B}', K(pg, "return clinics().map(c=>c.id+' '+c.name)"))
    chk('model i procent z konta (% po labie, 30%)', K(pg, f"return (c=>c.model+'|'+c.pct)(clinic('{A}'))") == 'pct_lab|30', K(pg, f"return clinic('{A}')"))

    # dyżur odbyty dziś w gabinecie A
    K(pg, f"""M('{MK}',true).shifts.push({{id:'t1',date:'{TODAY}',clinicId:'{A}',start:'08:00',end:'15:00',status:'done',turnover:5000,lab:1000,note:''}});saveMonth('{MK}');render();""")
    pg.wait_for_timeout(1500); synced(pg)
    sh = [x for x in month().get('shifts', []) if x.get('id') == 't1']
    chk('dyżur zapisany na koncie (miesiąc w calendar_docs)', len(sh) == 1 and sh[0]['clinicId'] == A and sh[0]['turnover'] == 5000, month())
    inc = K(pg, f"return Math.round(E.shiftIncome(M('{MK}').shifts.find(s=>s.id==='t1'),clinic('{A}'))*100)")
    chk('przychód z dyżuru = 30% z (5000 − 1000) = 1200 zł', inc == 120000, inc)
    got = wait_sql(f"SELECT data->'{TODAY}'->'{A}'->>'inc' FROM app.calendar_docs WHERE doc='sumy'", str(inc))
    chk('przychód z dyżurów zapisany dla Zarobków (sumy)', got == str(inc), got)

    # Zarobki: kolumna „Dyżury wg Kalendarza” (poza „Razem”)
    pg.goto(URL + '/zarobki?o=today')
    chk('Zarobki: kafelek „Dyżury wg Kalendarza” 1 200,00 zł', '1200,00' in pg.inner_text('[data-testid=kal]').replace('\xa0', '').replace(' ', ''), pg.inner_text('[data-testid=kal]'))
    chk('Zarobki: kolumna w tabeli gabinetów', 'Dyżury wg Kalendarza' in pg.inner_text('[data-testid=tabela]'))
    chk('Zarobki: „Razem z wizyt” bez dyżurów (0 zł)', pg.inner_text('[data-testid=razem]').replace('\xa0', ' ').startswith('0,00'), pg.inner_text('[data-testid=razem]'))
    pg.goto(URL + '/konto')
    chk('kafelek Kalendarza na koncie: „Dziś: A 8:00–15:00”', 'Dziś:' in pg.inner_text('.g-tiles') and '8:00–15:00' in pg.inner_text('.g-tiles'), pg.inner_text('.g-tiles'))

    # drugie urządzenie: ten sam dyżur; zmiana gabinetu w Kalendarzu → tabela gabinetów
    c2, p2 = login2(br, 'a.4e@example.com', 'zielony-kubek-na-biurku')
    p2.goto(URL + '/kalendarz'); ready(p2)
    chk('drugie urządzenie: dyżur widoczny', K(p2, f"return M('{MK}').shifts.some(s=>s.id==='t1'&&s.turnover===5000)"))
    K(p2, f"const c=clinic('{A}');c.name='Gabinet A2';c.pct=35;c.presets.push({{id:'p9',name:'Popołudnie',start:'14:00',end:'20:00'}});saveSettings();render();")
    got = wait_sql(f"SELECT name||'|'||pct::float8 FROM app.clinics WHERE id='{A}'", 'Gabinet A2|35')
    chk('zmiana gabinetu w Kalendarzu → wspólna tabela gabinetów (nazwa, %)', got == 'Gabinet A2|35', got)
    chk('pola tylko Kalendarza (zmiany) zapisane przy gabinecie', 'Popołudnie' in sql(f"SELECT extra::text FROM app.clinics WHERE id='{A}'"))
    p2.goto(URL + '/gabinety'); chk('zmiana widoczna w „Gabinety”', 'Gabinet A2' in p2.inner_text('main'))
    nid = str(uuid.uuid4())
    p2.goto(URL + '/kalendarz'); ready(p2)
    chk('po odświeżeniu Kalendarz ma zmianę „Popołudnie”', K(p2, f"return clinic('{A}').presets.some(x=>x.name==='Popołudnie')"))
    K(p2, f"const c=JSON.parse(JSON.stringify(clinic('{B}')));Object.assign(c,{{id:'{nid}',name:'Gabinet K',short:'K',color:4,week:{{slots:[],freq:'weekly'}}}});clinics().push(c);saveSettings();render();")
    got = wait_sql(f"SELECT name||'|'||color FROM app.clinics WHERE id='{nid}'", 'Gabinet K|4')
    chk('nowy gabinet dodany w Kalendarzu → pojawia się w tabeli gabinetów', got == 'Gabinet K|4', got)

    # zmiana w „Gabinety” → Kalendarz po odświeżeniu
    p2.goto(URL + f'/gabinety?id={B}'); fill(p2, name='Gabinet B2'); submit(p2, 'Zapisz zmiany')
    pg.goto(URL + '/kalendarz'); ready(pg)
    chk('zmiana nazwy w „Gabinety” widoczna w Kalendarzu', K(pg, f"return clinic('{B}').name") == 'Gabinet B2', K(pg, f"return clinic('{B}').name"))
    chk('Kalendarz pierwszego urządzenia ma gabinet K i zmianę A2', K(pg, f"return !!clinic('{nid}')&&clinic('{A}').name==='Gabinet A2'"))

    # podpowiedź „Wpisz jako obrót” z opisów prywatnych tego dnia (sumy liczone na serwerze)
    ck = cookie_of(ctx)
    item = {'pid': 'zach-kompozyt', 'name': 'Wypełnienie kompozytowe', 'kat': 'Zachowawcze', 'qty': 1, 'c': 40000, 'm': 'p', 'p': 40, 'kw': 0, 'cost': 0, 'val': 40000, 'pay': 16000}
    st, j = api('/api/pryw/wizyty', {'put': [{'id': 'pk1', 'no': 1, 'date': TODAY, 'gab': A, 'created': '2026-11-16T08:00:00Z', 'at': '2026-11-16T08:00:00Z', 'items': [item]}]}, ck)
    chk('wizyta prywatna (400 zł) w gabinecie A zapisana', st == 200 and j.get('saved') == 1, (st, j))
    pg.goto(URL + '/kalendarz'); ready(pg)
    K(pg, "openEditor('t1')"); pg.wait_for_timeout(300)
    hint = pg.inner_text('#sumHint') if pg.locator('#sumHint').count() else ''
    chk('podpowiedź z opisów w edycji dyżuru: 1 wizyta prywatna, 400 zł, „Wpisz jako obrót”', 'Opisy prywatne: 1 wizyta' in hint and '400,00' in hint.replace('\xa0', ' ') and 'Wpisz jako obrót' in hint, hint)
    K(pg, "UI.edit=null;render();")

    # brak połączenia: zmiana zostaje na urządzeniu i wysyła się po powrocie
    pg.route('**/api/kal/dokumenty', lambda r: r.abort())
    K(pg, f"""M('{MK}',true).shifts.push({{id:'t2',date:'{TODAY}',clinicId:'{B}',start:'16:00',end:'19:00',status:'planned'}});saveMonth('{MK}');render();""")
    pg.wait_for_timeout(1500)
    chk('offline: dyżur t2 nie dotarł na konto', not any(x.get('id') == 't2' for x in month().get('shifts', [])))
    chk('offline: komunikat o zapisie na urządzeniu', 'brak połączenia' in pg.inner_text('#gsync'), pg.inner_text('#gsync'))
    pg.unroute('**/api/kal/dokumenty')
    pg.goto(URL + '/kalendarz'); ready(pg); pg.wait_for_timeout(1500)
    chk('po powrocie połączenia niewysłany dyżur trafia na konto', any(x.get('id') == 't2' for x in month().get('shifts', [])), month())
    chk('…a dyżur z konta nie zginął', any(x.get('id') == 't1' for x in month().get('shifts', [])))

    # usunięcie gabinetu w Kalendarzu: bez wizyt → ukryty; z wizytami → tylko wyłączony
    K(pg, f"S().clinics=clinics().filter(c=>c.id!=='{nid}'&&c.id!=='{A}');saveSettings();")
    got = wait_sql(f"SELECT (deleted_at IS NOT NULL)::text FROM app.clinics WHERE id='{nid}'", 'true')
    chk('gabinet bez wizyt usunięty w Kalendarzu → ukryty w tabeli', got == 'true', got)
    chk('gabinet z wizytami (A) tylko wyłączony, historia zostaje', sql(f"SELECT active::text||'|'||(deleted_at IS NULL)::text FROM app.clinics WHERE id='{A}'") == 'false|true')

    # izolacja i walidacja
    cb, pb = konto(br, 'Lekarz B', 'b.4e@example.com', 'czerwony-rower-pod-domem'); cb.close()
    cb, pb = login2(br, 'b.4e@example.com', 'czerwony-rower-pod-domem')
    pb.goto(URL + '/kalendarz'); ready(pb)
    chk('konto B: brak dyżurów i gabinetów konta A', not K(pb, f"return M('{MK}').shifts.length") and A not in K(pb, "return clinics().map(c=>c.id).join(',')"))
    kb = cookie_of(cb)
    st, j = api('/api/kal/dokumenty', {'put': {'settings': {'clinics': [{'id': A, 'name': 'Przejęty', 'model': 'pct', 'pct': 50}]}}}, kb)
    chk('konto B nie przejmie gabinetu A (cudzy identyfikator) → 400', st == 400 and sql(f"SELECT name FROM app.clinics WHERE id='{A}'") == 'Gabinet A2', (st, j))
    chk('nieznany dokument odrzucony → 400', api('/api/kal/dokumenty', {'put': {'pacjenci': {'x': 1}}}, kb)[0] == 400)
    chk('zapis z obcej strony (Origin) odrzucony', api('/api/kal/dokumenty', {'put': {}}, kb, origin='https://zla-strona.example')[0] == 403)
    chk('konto B: w jego dokumentach nic z konta A (dyżury, gabinety)', sql(f"SELECT count(*) FROM app.calendar_docs WHERE owner_id=(SELECT id FROM app.profiles WHERE email='b.4e@example.com') AND (data::text LIKE '%\"t1\"%' OR data::text LIKE '%Gabinet A2%')") == '0')

    # porównanie ze starą aplikacją: te same dokumenty → ten sam tekst Podsumowania, Rozliczeń, Terminów i Porównania form
    if OPISY:
        srv = None
        try: urllib.request.urlopen(OLD + '/kalendarz.html', timeout=1)
        except Exception: srv = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=OPISY, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
        pg.goto(URL + '/kalendarz'); ready(pg)
        K(pg, f"""const m=M('{MK}',true);m.costs.push({{id:'k1',date:'{TODAY}',amount:300,desc:'Materiały',kup:true}});
          m.shifts.push({{id:'t3',date:'{MK}-02',clinicId:'{B}',start:'08:00',end:'14:00',status:'done',turnover:3000,lab:0}});saveMonth('{MK}');render();""")
        pg.wait_for_timeout(1200)
        docs = K(pg, "return JSON.parse(JSON.stringify(Store.docs))")
        oc = br.new_context(); po = oc.new_page(); po.goto(OLD + '/index.html'); po.wait_for_function("window.G&&typeof G.createUser==='function'")
        po.evaluate("async()=>{const r=await G.createUser('Test','haslo-test-1');G.user=r.user;G.key=(await G.session()).key;}")
        po.evaluate("async(d)=>{await G.store('kv').put('grafik',d);}", docs)
        po.goto(OLD + '/kalendarz.html'); ready(po)
        same = []
        for tb in ['sum', 'inv', 'dl', 'cmp']:
            for x in (pg, po): K(x, f"UI.tab='{tb}';UI.edit=null;render();"); x.wait_for_timeout(150)
            a, b = pg.inner_text('#main'), po.inner_text('#main')
            chk(f'zakładka „{tb}”: tekst = stara aplikacja ({len(a)} znaków)', a == b and len(a) > 100, (len(a), len(b), [l for l in a.split('\n') if l not in b.split('\n')][:3]))
        oc.close()
        if srv: srv.terminate()
    else:
        print('UWAGA: pominięto porównanie ze starą aplikacją (brak OPISY_DIR)')
    # „Usuń wszystkie dane” w Kalendarzu: dyżury i ustawienia Kalendarza znikają, gabinety (wspólne) zostają
    pg.goto(URL + '/kalendarz'); ready(pg)
    K(pg, "UI.tab='set';UI.ask='reset';render();"); pg.click('[data-a="reset-do"]'); pg.wait_for_timeout(1500); synced(pg)
    chk('reset Kalendarza: miesiące usunięte z konta', sql("SELECT count(*) FROM app.calendar_docs WHERE doc LIKE 'm%'") == '0', sql("SELECT string_agg(doc,',') FROM app.calendar_docs"))
    chk('reset Kalendarza: gabinety zostają w tabeli i w ustawieniach Kalendarza', sql(f"SELECT (deleted_at IS NULL)::text FROM app.clinics WHERE id='{B}'") == 'true'
        and B in sql("SELECT data::text FROM app.calendar_docs WHERE doc='settings'") and sql("SELECT count(*) FROM app.clinics WHERE name LIKE 'Gabinet _' AND deleted_at IS NULL") == '0')
    chk('opis „Dane”: zapis na koncie, bez „nie trafiają na żaden serwer”', 'na Twoim koncie Gabinet' in pg.inner_text('#main') and 'żaden serwer' not in pg.inner_text('#main'))
    chk('brak błędów JavaScript', not errs, errs[:5])
    br.close()
t.done('etap 4e-1 Kalendarz')
