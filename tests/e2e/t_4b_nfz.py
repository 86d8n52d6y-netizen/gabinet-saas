# Etap 4b: generator Opisów NFZ w wersji SaaS – działanie, prywatność (bez treści i inicjałów w chmurze), synchronizacja
# między urządzeniami, izolacja kont, bezpieczeństwo API oraz porównanie tekstu opisu ze starą aplikacją (OPISY_DIR).
import json, os, subprocess, time, urllib.request
from pomoc import *
t = T(); chk = t.chk
OPISY = os.environ.get('OPISY_DIR')            # repo opisy-nfz (stara aplikacja) – porównanie tekstów
OLD = 'http://127.0.0.1:8765'

def ready(pg):
    pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def idle(pg):
    pg.wait_for_function("!state.pendSig&&!ui.busy", timeout=8000); pg.wait_for_timeout(80)
def synced(pg, timeout=8000):
    pg.wait_for_function("document.getElementById('gsync')&&document.getElementById('gsync').textContent.includes('zsynchronizowana')", timeout=timeout)
def gen(pg, age='9', plan='I', ini='jk'):
    pg.fill('#i_sv_ini', ini); pg.fill('#i_sh_age', age)
    grp = 'u5' if int(age) < 5 else 'o5'
    pg.click(f'button.plan-btn[data-p="{grp}"][data-w="{plan}"]'); pg.click('#bar button.btn:not(.ghost)')
    for c in ['ST30', 'ST30E']:
        if pg.locator(f'#card-{c}').count(): pg.click(f'#card-{c} button[data-act="quadset"][data-q="1,2"]')
    pg.click('#bar button.btn:not(.ghost)'); idle(pg)
def fresh(pg):
    if pg.evaluate("state.codes.length"):
        if pg.evaluate("state.step") != 3: pg.click('#steps button[data-n="3"]'); pg.wait_for_timeout(100)
        pg.click('#resetBtn'); pg.wait_for_timeout(150)
        if pg.evaluate("state.codes.length"): pg.click('#resetBtn'); pg.wait_for_timeout(150)
def visits(pg): return pg.evaluate("dbList().map(m=>Object.assign({},m,{k:calc(m)}))")
def api(path, body, cookie=None, origin=URL):
    h = {'Content-Type': 'application/json'}
    if origin: h['Origin'] = origin
    if cookie: h['Cookie'] = cookie
    rq = urllib.request.Request(URL + path, data=json.dumps(body).encode(), headers=h, method='POST')
    try:
        with urllib.request.urlopen(rq) as r: return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read() or b'{}')
def cookie_of(ctx): return '; '.join(f"{c['name']}={c['value']}" for c in ctx.cookies() if c['name'].startswith('gabinet_sesja'))

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    # bez logowania
    anon = br.new_context(); pa = anon.new_page()
    pa.goto(URL + '/opisy-nfz'); chk('bez logowania /opisy-nfz → logowanie', '/logowanie' in pa.url, pa.url)
    r = pa.goto(URL + '/opisy-nfz/zasoby/szablony.js'); chk('kod generatora niedostępny bez logowania (401)', r.status == 401, r.status)
    r = pa.goto(URL + '/opisy-nfz/zasoby/../package.json'); chk('zasoby: tylko pliki z listy (bez wyjścia poza katalog)', r.status in (401, 404), r.status)

    ctx, pg = konto(br, 'Lekarz A', 'a.4b@example.com', 'zielony-kubek-na-biurku')
    pg.goto(URL + '/gabinety'); fill(pg, name='Happy Smile', short='HS', pct='30'); submit(pg, 'Dodaj gabinet')
    gab = sql("SELECT id FROM app.clinics WHERE name='Happy Smile'")
    ctx.close()
    # kontekst z pominięciem CSP tylko dla narzędzia testowego (wait_for_function); nagłówek CSP sprawdzany osobno
    ctx = br.new_context(bypass_csp=True); pg = ctx.new_page()
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' and 'favicon' not in m.text else None)
    pg.goto(URL + '/logowanie'); fill(pg, email='a.4b@example.com', password='zielony-kubek-na-biurku'); submit(pg, 'Zaloguj')
    resp = pg.goto(URL + '/opisy-nfz'); ready(pg)
    chk('generator otwiera się na koncie SaaS', resp.status == 200 and pg.locator('#steps').count() == 1)
    chk('CSP także na stronie generatora', "default-src 'self'" in (resp.headers.get('content-security-policy') or ''))
    chk('pasek: Kalendarz, Opisy NFZ (aktywne), Opisy prywatne, Zlecenia, Zarobki, Katalog NFZ, Gabinety, Ustawienia, Konto', pg.locator('#gbar a.on').inner_text() == 'Opisy NFZ' and pg.locator('#gbar nav a').count() == 9)
    chk('czcionki lokalnie (bez Google Fonts)', 'fonts.googleapis.com' not in pg.content())
    chk('stawki z konta (1,84 zł / 40% / 350 zł)', pg.evaluate("[cfg.price,cfg.pct,cfg.rev].join('|')") == '1.84|40|350')
    chk('gabinet z konta na liście generatora', pg.evaluate(f"state.clinics.some(c=>c.id==='{gab}')"))
    synced(pg); chk('stan: „Historia zsynchronizowana”', 'zsynchronizowana' in pg.inner_text('#gsync'))

    # zapis wizyty → chmura bez treści i inicjałów
    gen(pg, age='9', plan='I', ini='jk')
    v = visits(pg)
    chk('wizyta zapisana na urządzeniu (z inicjałami i treścią lokalnie)', len(v) == 1 and v[0]['ini'] == 'JK' and v[0]['body'] is True, v[:1])
    synced(pg)
    row = sql("SELECT row_to_json(s)::text FROM app.saved_descriptions s")
    chk('wizyta w chmurze: data, kody, punkty, stawki', row and json.loads(row)['codes'] == v[0]['codes'] and json.loads(row)['rates']['pts'] == v[0]['pts'], row)
    txt = pg.evaluate("genTxt()")
    dump = sql("SELECT string_agg(t::text, ' ') FROM (SELECT row_to_json(s) t FROM app.saved_descriptions s UNION ALL SELECT row_to_json(e) FROM app.earnings_entries e) x")
    chk('w chmurze BRAK inicjałów pacjenta', 'JK' not in dump and '"ini"' not in dump)
    chk('w chmurze BRAK treści opisu (żadnego zdania z opisu)', all(line.strip()[:40] not in dump for line in txt.split('\n') if len(line.strip()) > 25))
    chk('w chmurze BRAK wieku i odpowiedzi z formularza', '"age"' not in dump and 'sh.age' not in dump and '"a"' not in dump)
    k = v[0]['k']
    chk('kwoty do statystyk = kwoty generatora (grosze)', sql(f"SELECT value_gr||'|'||doctor_pay_gr FROM app.earnings_entries WHERE source='nfz_points'") == f"{k['pc']}|{k['sh']}", (sql("SELECT value_gr, doctor_pay_gr FROM app.earnings_entries"), k))
    loc = pg.evaluate("""async()=>{const db=await new Promise(r=>{const q=indexedDB.open('opisyNFZ@'+UID,1);q.onsuccess=()=>r(q.result)});
       return await new Promise(r=>{const t=db.transaction('bodies').objectStore('bodies').getAll();t.onsuccess=()=>r(JSON.stringify(t.result))})}""")
    chk('treść opisu na urządzeniu zaszyfrowana (nie da się jej odczytać z bazy przeglądarki)', 'BADANIE' not in loc and 'v1:' in loc)

    # drugie urządzenie: historia bez treści
    ctx2 = br.new_context(bypass_csp=True); p2 = ctx2.new_page()
    p2.goto(URL + '/logowanie'); fill(p2, email='a.4b@example.com', password='zielony-kubek-na-biurku'); submit(p2, 'Zaloguj')
    p2.goto(URL + '/opisy-nfz'); ready(p2)
    v2 = visits(p2)
    chk('drugie urządzenie: wizyta w historii (data, kody, kwoty)', len(v2) == 1 and v2[0]['codes'] == v[0]['codes'] and v2[0]['k']['total'] == k['total'], v2)
    chk('drugie urządzenie: bez inicjałów i bez treści (tylko na urządzeniu zapisu)', v2[0]['ini'] == '' and v2[0]['body'] is False)
    p2.click('#steps button[data-n="4"]'); p2.wait_for_timeout(200)
    chk('drugie urządzenie: historia pokazuje wpis „Anonim”, bez przycisku otwarcia opisu', 'Anonim' in p2.inner_text('#main') and p2.locator('button[data-act="hdel"]').count() == 1 and p2.locator('button[data-act="hopen"]').count() == 0, p2.inner_text('#main')[:600])

    # ustawienia generatora → konto → drugie urządzenie
    pg.click('#steps button[data-n="1"]'); pg.wait_for_timeout(100); fresh(pg)
    pg.click('#custBtn'); pg.click('#cr-ST33 button[data-act="cfav"]'); pg.click('#custBtn'); pg.wait_for_timeout(900)
    chk('ulubiony kod zapisany na koncie', 'ST33' in sql("SELECT settings->'nfzUi'->>'fav' FROM app.user_settings u JOIN app.profiles p ON p.id=u.user_id WHERE p.email='a.4b@example.com'"))
    p2.goto(URL + '/opisy-nfz'); ready(p2); chk('drugie urządzenie: ten sam ulubiony kod', p2.evaluate("cfg.fav").count('ST33') == 1 if isinstance(p2.evaluate("cfg.fav"), list) else False)
    pg.click('#steps button[data-n="6"]'); pg.click('#sg-INSTR_HEAD button[data-act="segedit"]')
    pg.fill('#segTxt', 'INSTRUKTAŻ HIGIENY – WERSJA GABINETU TESTOWA'); pg.click('#segSave'); pg.wait_for_timeout(900)
    chk('własna wersja stałego tekstu zapisana na koncie', 'WERSJA GABINETU TESTOWA' in sql("SELECT settings->'nfzSeg'::text FROM app.user_settings u JOIN app.profiles p ON p.id=u.user_id WHERE p.email='a.4b@example.com'"))
    p2.goto(URL + '/opisy-nfz'); ready(p2); chk('drugie urządzenie: ta sama wersja tekstu', p2.evaluate("SEG.INSTR_HEAD") == 'INSTRUKTAŻ HIGIENY – WERSJA GABINETU TESTOWA')

    # usunięcie na drugim urządzeniu → znika na pierwszym
    p2.click('#steps button[data-n="4"]'); p2.wait_for_timeout(150)
    vid = v[0]['id']
    p2.click(f'button[data-act="hdel"][data-id="{vid}"]'); p2.click(f'button[data-act="hdel"][data-id="{vid}"]'); p2.wait_for_timeout(200); synced(p2)
    chk('usunięcie: w chmurze znacznik usunięcia, kwoty poza statystykami', sql("SELECT (deleted_at IS NOT NULL)::text||(SELECT count(*) FROM app.earnings_entries WHERE deleted_at IS NULL) FROM app.saved_descriptions") == 'true0')
    pg.goto(URL + '/opisy-nfz'); ready(pg)
    chk('pierwsze urządzenie: wizyta usunięta także lokalnie (z treścią)', len(visits(pg)) == 0 and pg.evaluate("dbBody('" + vid + "').then(b=>!!b)") is False)

    # praca bez połączenia
    gen(pg, age='30', plan='III', ini='ab'); pg.wait_for_timeout(300); synced(pg)
    ctx.set_offline(True)
    fresh(pg); gen(pg, age='40', plan='II', ini='cd'); pg.wait_for_timeout(800)
    chk('bez internetu: wizyta zapisana na urządzeniu, komunikat o wysłaniu później', len(visits(pg)) == 2 and 'później' in pg.inner_text('#gsync'), pg.inner_text('#gsync'))
    ctx.set_offline(False); pg.evaluate("dispatchEvent(new Event('online'))"); synced(pg, 15000)
    chk('po powrocie internetu wizyta trafia do chmury', sql("SELECT count(*) FROM app.saved_descriptions WHERE deleted_at IS NULL") == '2')

    # izolacja i bezpieczeństwo API
    ctxb, pb = konto(br, 'Lekarz B', 'b.4b@example.com', 'niebieska-lampa-w-oknie')
    keyA = sql("SELECT client_key FROM app.saved_descriptions WHERE deleted_at IS NULL LIMIT 1")
    st, js = api('/api/nfz/wizyty', {'del': [{'id': keyA, 'at': '2099-01-01T00:00:00.000Z'}], 'list': True}, cookie_of(ctxb))
    chk('B: lista z chmury pusta (nie widzi wizyt A)', st == 200 and js.get('live') == [], (st, js))
    chk('B nie usunie wizyty A (ten sam identyfikator, RLS)', sql(f"SELECT deleted_at IS NULL FROM app.saved_descriptions WHERE client_key='{keyA}'") == 't')
    bad = {'id': 'vtest1', 'no': 1, 'ini': 'XYZ', 'date': '2026-11-16', 'created': '2026-11-16T10:00:00.000Z', 'at': '2026-11-16T10:00:00.000Z', 'src': 'gen',
           'codes': ['ST33'], 'pts': 56, 'price': 1.84, 'pct': 40, 'revH': 0, 'revRate': 350, 'ex': [], 'min': 30, 'miss': 0, 'gab': gab,
           'txt': 'Pacjent Jan Kowalski PESEL 90010112345', 'a': {'sh.age': '33'}}
    st, js = api('/api/nfz/wizyty', {'put': [bad]}, cookie_of(ctxb))
    rowb = sql("SELECT row_to_json(s)::text FROM app.saved_descriptions s WHERE client_key='vtest1'")
    chk('API: dodatkowe pola (tekst, odpowiedzi, inicjały) odrzucone przy zapisie', st == 200 and 'XYZ' not in rowb and 'Kowalski' not in rowb and '90010112345' not in rowb and 'sh.age' not in rowb, rowb)
    chk('API: gabinet innego konta nie zostaje przypisany', '"clinic_id":null' in rowb, rowb)
    chk('API bez nagłówka Origin → 403', api('/api/nfz/wizyty', {'put': []}, cookie_of(ctxb), origin=None)[0] == 403)
    chk('API z obcej domeny → 403', api('/api/nfz/wizyty', {'put': []}, cookie_of(ctxb), origin='https://zly.example')[0] == 403)
    chk('API bez sesji → 401', api('/api/nfz/wizyty', {'put': []})[0] == 401)
    st, _ = api('/api/nfz/wizyty', {'put': [dict(bad, id='x' * 50), dict(bad, id='v2', date='2026-13-45'), dict(bad, id='v3', pts=-5)]}, cookie_of(ctxb))
    chk('API: niepoprawne wpisy odrzucone (id, data, punkty)', sql("SELECT count(*) FROM app.saved_descriptions WHERE client_key IN ('v2','v3')") == '0')

    # porównanie tekstu opisu ze starą aplikacją (te same odpowiedzi → identyczny tekst)
    if OPISY:
        srv = None
        try: urllib.request.urlopen(OLD + '/nfz.html', timeout=1)
        except Exception: srv = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=OPISY, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
        oc = br.new_context(); po = oc.new_page(); po.goto(OLD + '/index.html'); po.wait_for_function("window.G&&typeof G.createUser==='function'")
        po.evaluate("async()=>{const r=await G.createUser('Test','haslo-test-1');G.user=r.user;G.key=(await G.session()).key;}")
        po.goto(OLD + '/nfz.html'); ready(po)
        # przywrócenie domyślnego stałego tekstu zmienionego wcześniej w teście synchronizacji
        fresh(pg); pg.click('#steps button[data-n="6"]'); pg.click('#sg-INSTR_HEAD button[data-act="segedit"]'); pg.click('#segDef'); pg.click('#segDef'); pg.wait_for_timeout(400)
        chk('stały tekst przywrócony do domyślnego', pg.evaluate("SEG.INSTR_HEAD===SEG0.INSTR_HEAD"))
        pg.click('#steps button[data-n="1"]'); pg.wait_for_timeout(100)
        n = 0
        for age in ['3', '9', '30', '67']:
            for plan in ['I', 'II', 'III', 'IV']:
                if int(age) < 5 and plan in ('III', 'IV'): continue
                fresh(pg); fresh(po)
                gen(pg, age=age, plan=plan, ini='ab'); gen(po, age=age, plan=plan, ini='ab')
                # 21.11.2026 (P26): wędzidełka w SaaS domyślnie „Typ I” – w starej aplikacji ustawiamy to samo, reszta tekstu co do znaku
                po.evaluate("['sh.wg','sh.wd'].forEach(k=>{if(state.a[k]===undefined)state.a[k]=WEDZ[0];})")
                pg.evaluate("state.a['sh.zal']='ustnie i pisemnie'")   # P34: porównanie przy wariancie jak w starej aplikacji
                pg.evaluate("cfg.sum=false")   # P40: podsumowanie wyłączone – reszta tekstu co do znaku jak w starej aplikacji
                a, b = pg.evaluate("genTxt()"), po.evaluate("genTxt()")
                ka, kb = pg.evaluate("JSON.stringify(nfzPoints())"), po.evaluate("JSON.stringify(nfzPoints())")
                chk(f'tekst opisu = stara aplikacja (wiek {age}, plan {plan}, {len(a)} znaków)', a == b and len(a) > 200, (len(a), len(b)))
                chk(f'wycena = stara aplikacja (wiek {age}, plan {plan})', ka == kb); n += 1
        # import kopii zapasowej ze starej aplikacji → nowe konto (inicjały zostają tylko na urządzeniu)
        for age, plan, ini in [('30', 'II', 'kw'), ('9', 'IV', 'mn')]: fresh(po); gen(po, age=age, plan=plan, ini=ini)
        kop = po.evaluate("""async()=>{const bodies={};(await DB.be.all('bodies')).forEach(([k,v])=>{if(DB.visits.has(k)&&v&&typeof v.txt==='string')bodies[k]=v;});
            const segs={};DB.segs.forEach((v,k)=>{segs[k]=v;});
            return JSON.stringify({app:'opisy-nfz',schema:2,exported:new Date().toISOString(),cfg:{price:cfg.price,pct:cfg.pct,rev:cfg.rev,basis:cfg.basis,auto:cfg.auto},visits:dbList().slice().reverse(),bodies,segs});}""")
        nOld = len(json.loads(kop)['visits'])
        cc, pc = konto(br, 'Lekarz C', 'c.4b@example.com', 'czerwony-dzbanek-w-kuchni'); cc.close()
        cc = br.new_context(bypass_csp=True); pc = cc.new_page()
        pc.goto(URL + '/logowanie'); fill(pc, email='c.4b@example.com', password='czerwony-dzbanek-w-kuchni'); submit(pc, 'Zaloguj')
        pc.goto(URL + '/opisy-nfz'); ready(pc)
        pc.evaluate("(j)=>backupImport(new File([j],'kopia.json',{type:'application/json'}))", kop); pc.wait_for_timeout(500); synced(pc)
        chk(f'import kopii ze starej aplikacji: {nOld} wpisów na urządzeniu, z treścią', len(visits(pc)) == nOld and all(x['body'] for x in visits(pc)), len(visits(pc)))
        cnt = sql("SELECT count(*) FROM app.saved_descriptions s JOIN app.profiles p ON p.id=s.owner_id WHERE p.email='c.4b@example.com' AND s.deleted_at IS NULL")
        dumpc = sql("SELECT string_agg(row_to_json(s)::text,' ') FROM app.saved_descriptions s JOIN app.profiles p ON p.id=s.owner_id WHERE p.email='c.4b@example.com'")
        chk(f'import → chmura: {nOld} wpisów, bez inicjałów (KW, MN, AB)', cnt == str(nOld) and all(x not in dumpc for x in ['"KW"', '"MN"', '"AB"', '"ini"']), (cnt, dumpc[:200]))
        chk('import: treść opisów nie trafiła do chmury', 'BADANIE' not in dumpc and 'Ząb' not in dumpc)
        if srv: srv.terminate()
    else:
        print('UWAGA: pominięto porównanie ze starą aplikacją (brak OPISY_DIR)')
    errs = [e for e in errs if 'ERR_INTERNET_DISCONNECTED' not in e]          # celowo symulowany brak internetu
    chk('brak błędów JavaScript w generatorze', not errs, errs[:5])
    br.close()
t.done('etap 4b: generator Opisów NFZ')
