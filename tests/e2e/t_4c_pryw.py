# Etap 4c: Opisy prywatne w wersji SaaS – działanie, prywatność (w chmurze bez treści, pól szablonu, e-ZLA i inicjałów),
# cennik/szablony/zestawy na koncie, dwa urządzenia, usuwanie, izolacja kont oraz porównanie tekstu ze starą aplikacją (OPISY_DIR).
import json, os, subprocess, time, urllib.request
from pomoc import *
t = T(); chk = t.chk
OPISY = os.environ.get('OPISY_DIR'); OLD = 'http://127.0.0.1:8765'

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def synced(pg, timeout=8000):
    pg.wait_for_function("document.getElementById('gsync')&&document.getElementById('gsync').textContent.includes('zsynchronizowana')", timeout=timeout)
def tab(pg, k): pg.click(f'#tabs button[data-tab="{k}"]'); pg.wait_for_timeout(100)
def fid(pg, i, k): return '#f_' + pg.evaluate(f"V.items[{i}].u") + '_' + k
def login2(br, email, pwd):
    c = br.new_context(bypass_csp=True); p_ = c.new_page()
    p_.goto(URL + '/logowanie'); fill(p_, email=email, password=pwd); submit(p_, 'Zaloguj'); return c, p_
def wizyta(pg, ini='jk', ezla=True):
    """Kompozyt (ząb 36, MO, rozpoznanie, znieczulenie) + skaling; e-ZLA; inicjały."""
    tab(pg, 'wiz'); pg.fill('#p_q', ''); pg.wait_for_timeout(250)
    pg.click('button[data-add="zach-kompozyt"]')
    u = pg.evaluate("V.items[0].u")
    pg.click(f'#it-{u} button[data-a="pick"]'); pg.click('.pw-tb[data-t="36"]')
    for o in ['M', 'O']: pg.check(f'#it-{u} .pw-ms label:has-text("{o}") input')
    pg.fill(fid(pg, 0, 'rozp'), 'próchnica zębiny (K02.1)'); pg.select_option(fid(pg, 0, 'zn'), 'nasiękowe')
    pg.fill(fid(pg, 0, 'znprep'), 'artykaina 4% z adrenaliną 1:100 000'); pg.fill(fid(pg, 0, 'zndawka'), '1,7')
    pg.fill('#p_q', 'skaling'); pg.wait_for_timeout(250); pg.click('button[data-add="hig-skaling"]')
    if ezla:
        pg.check('#ez_on'); pg.fill('#ez_od', '2026-11-16'); pg.fill('#ez_do', '2026-11-18')
    pg.fill('#v_ini', ini); pg.wait_for_timeout(150)
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
    an = br.new_context(); pa = an.new_page(); pa.goto(URL + '/opisy-prywatne')
    chk('bez logowania /opisy-prywatne → logowanie', '/logowanie' in pa.url)
    chk('katalog procedur niedostępny bez logowania', pa.goto(URL + '/opisy-nfz/zasoby/prywatne-katalog.js').status == 401)

    c0, p0 = konto(br, 'Lekarz A', 'a.4c@example.com', 'zielony-kubek-na-biurku')
    for n in ['Gabinet A', 'Gabinet B']:
        p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name=n, pct='30'); submit(p0, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet A'"); B = sql("SELECT id FROM app.clinics WHERE name='Gabinet B'")
    c0.close()
    ctx, pg = login2(br, 'a.4c@example.com', 'zielony-kubek-na-biurku')
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' else None)
    r = pg.goto(URL + '/opisy-prywatne'); ready(pg)
    chk('moduł otwiera się na koncie SaaS (pasek: „Opisy prywatne” aktywne)', r.status == 200 and pg.inner_text('#gbar a.on') == 'Opisy prywatne')
    chk('katalog: 19 procedur własnych + 144 karty procedur (etap K1)', pg.locator('button[data-add]').count() == 163 and pg.locator('button[data-add]:not([data-add^="karta-"])').count() == 19, pg.locator('button[data-add]').count())
    chk('gabinety z konta w module', pg.evaluate(f"S.clinics.map(c=>c.id).join(',')") == f'{A},{B}', pg.evaluate("S.clinics.map(c=>c.name)"))
    chk('przykładowe zestawy przy pierwszym uruchomieniu → zapisane na koncie', pg.wait_for_timeout(600) or 'zx1' in sql("SELECT data::text FROM app.user_blobs WHERE key='pryw:zestawy'"))

    # cennik gabinetu A → konto
    tab(pg, 'cen'); pg.click(f'button[data-cg="{A}"]')
    pg.fill('#c_pct', '40'); pg.press('#c_pct', 'Tab')
    pg.fill('[data-cc="zach-kompozyt"]', '400'); pg.press('[data-cc="zach-kompozyt"]', 'Tab')
    pg.fill('[data-cc="hig-skaling"]', '250'); pg.press('[data-cc="hig-skaling"]', 'Tab'); pg.wait_for_timeout(900)
    cen = json.loads(sql("SELECT data::text FROM app.user_blobs WHERE key='pryw:cennik'") or '{}')
    chk('cennik gabinetu A zapisany na koncie (400 zł, 40%)', cen.get('gab', {}).get(A, {}).get('items', {}).get('zach-kompozyt', {}).get('c') == 40000 and cen['gab'][A]['pct'] == 40, cen)

    # wizyta
    tab(pg, 'wiz'); pg.select_option('#v_gab', A); pg.wait_for_timeout(150)
    wizyta(pg)
    txt = pg.evaluate("curText()")
    pg.click('#b_save'); pg.wait_for_function("V.id&&S.visits.size===1"); pg.wait_for_timeout(300); synced(pg)
    m = pg.evaluate("[...S.visits.values()][0]")
    chk('wizyta zapisana: JK, gabinet A, 2 procedury, wartość 650 zł, lekarz 260 zł', (m['ini'], m['gab'], m['n'], m['val'], m['pay']) == ('JK', A, 2, 65000, 26000), {k: m.get(k) for k in ['ini', 'gab', 'n', 'val', 'pay']})
    dump = sql("SELECT string_agg(t::text,' ') FROM (SELECT row_to_json(s) t FROM app.saved_descriptions s UNION ALL SELECT row_to_json(e) FROM app.earnings_entries e) x")
    chk('w chmurze: 2 procedury z cenami i wynagrodzeniem, gabinet A', sql("SELECT count(*)||'|'||sum(value_gr)||'|'||sum(doctor_pay_gr)||'|'||min(clinic_id::text) FROM app.earnings_entries WHERE source='private_procedure'") == f'2|65000|26000|{A}')
    chk('w chmurze BRAK inicjałów', '"JK"' not in dump and '"ini"' not in dump)
    chk('w chmurze BRAK pól szablonu (ząb, rozpoznanie, znieczulenie)', '"vals"' not in dump and 'K02.1' not in dump and 'artykaina' not in dump and '"def"' not in dump)
    chk('w chmurze BRAK zwolnienia e-ZLA', 'ezla' not in dump and '2026-11-18' not in dump)
    chk('w chmurze BRAK treści opisu', all(line.strip()[:40] not in dump for line in txt.split('\n') if len(line.strip()) > 25))
    loc = pg.evaluate("""async()=>{const db=await new Promise(r=>{const q=indexedDB.open('gabinet-saas@'+G.user.id);q.onsuccess=()=>r(q.result);q.onerror=()=>r(null)});
        return await new Promise(r=>{const t=db.transaction('opisy').objectStore('opisy').getAll();t.onsuccess=()=>r(JSON.stringify(t.result))})}""")
    chk('treść opisu na urządzeniu zaszyfrowana', 'K02.1' not in loc and 'v1:' in loc)

    # drugie urządzenie
    ctx2, p2 = login2(br, 'a.4c@example.com', 'zielony-kubek-na-biurku')
    p2.goto(URL + '/opisy-prywatne'); ready(p2)
    m2 = p2.evaluate("[...S.visits.values()]")
    chk('drugie urządzenie: wizyta w historii (procedury, kwoty, gabinet)', len(m2) == 1 and m2[0]['val'] == 65000 and m2[0]['pay'] == 26000 and m2[0]['gab'] == A and [i['name'] for i in m2[0]['items']] == [i['name'] for i in m['items']], m2)
    chk('drugie urządzenie: bez inicjałów, pól szablonu i e-ZLA', m2[0]['ini'] == '' and not m2[0].get('ezla') and all(not i.get('vals') for i in m2[0]['items']))
    tab(p2, 'hist')
    chk('drugie urządzenie: „treść opisu jest tylko na urządzeniu, na którym zapisano wizytę”', 'tylko na urządzeniu, na którym zapisano' in p2.inner_text('#main'), p2.inner_text('#main')[:300])
    chk('drugie urządzenie: ten sam cennik', p2.evaluate(f"S.cennik.gab['{A}'].items['zach-kompozyt'].c") == 40000)
    pg.evaluate("UK.fav=['zach-kompozyt'];ukSave()"); pg.wait_for_timeout(800)
    p2.goto(URL + '/opisy-prywatne'); ready(p2)
    chk('ulubiona procedura (szablony) zsynchronizowana', p2.evaluate("UK.fav").count('zach-kompozyt') == 1)
    chk('ponowne otwarcie nie usuwa wizyty', len(p2.evaluate("[...S.visits.values()]")) == 1 and sql("SELECT count(*) FROM app.saved_descriptions WHERE deleted_at IS NULL") == '1')

    # usunięcie na drugim urządzeniu → pierwsze
    tab(p2, 'hist'); vid = m['id']
    p2.click(f'button[data-a="hdel"][data-id="{vid}"]'); p2.click(f'button[data-a="hdel"][data-id="{vid}"]'); p2.wait_for_timeout(300); synced(p2)
    chk('usunięcie: znacznik w chmurze, kwoty poza statystykami', sql("SELECT (deleted_at IS NOT NULL)::text||(SELECT count(*) FROM app.earnings_entries WHERE deleted_at IS NULL) FROM app.saved_descriptions") == 'true0')
    pg.goto(URL + '/opisy-prywatne'); ready(pg)
    chk('pierwsze urządzenie: wizyta usunięta także lokalnie', pg.evaluate("S.visits.size") == 0)

    # izolacja i API
    cb, pb = konto(br, 'Lekarz B', 'b.4c@example.com', 'niebieska-lampa-w-oknie')
    st, js = api('/api/pryw/wizyty', {'list': True, 'del': [{'id': vid, 'at': '2099-01-01T00:00:00.000Z'}]}, cookie_of(cb))
    chk('B: lista z chmury pusta (nie widzi wizyt A)', st == 200 and js.get('live') == [], (st, js))
    bad = {'id': 'pX1', 'no': 1, 'date': '2026-11-16', 'gab': A, 'ini': 'ZZ', 'created': '2026-11-16T10:00:00.000Z', 'at': '2026-11-16T10:00:00.000Z',
           'ezla': {'od': '2026-11-16', 'do': '2026-11-20'}, 'items': [{'pid': 'zach-kompozyt', 'name': 'Kompozyt', 'kat': 'Zach', 'qty': 1, 'c': 1000, 'm': 'p', 'p': 40, 'kw': 0, 'cost': 0, 'val': 1000, 'pay': 400,
           'vals': {'zab': '11', 'rozp': 'Jan Kowalski'}}], 'val': 99999999, 'pay': 99999999, 'txt': 'Opis pacjenta Jan Kowalski'}
    st, js = api('/api/pryw/wizyty', {'put': [bad]}, cookie_of(cb))
    rb = sql("SELECT row_to_json(s)::text FROM app.saved_descriptions s WHERE client_key='pX1'")
    chk('API: pola pacjenta odrzucone (inicjały, e-ZLA, pola szablonu, tekst)', st == 200 and all(x not in rb for x in ['ZZ', 'ezla', 'Kowalski', '"vals"']), rb)
    chk('API: gabinet innego konta nie zostaje przypisany', '"clinic_id":null' in rb)
    chk('API: sumy liczone na serwerze z pozycji (nie z deklaracji)', sql("SELECT sum(value_gr)||'|'||sum(doctor_pay_gr) FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id=e.description_id WHERE s.client_key='pX1'") == '1000|400')
    chk('API: dane modułu – tylko klucze z listy', api('/api/dane', {'key': 'pryw:pacjenci', 'data': {}}, cookie_of(cb))[0] == 400)
    chk('API: dane modułu – bez sesji 401, obca domena 403', api('/api/dane', {'key': 'pryw:ust', 'data': {}})[0] == 401 and api('/api/dane', {'key': 'pryw:ust', 'data': {}}, cookie_of(cb), origin='https://zly.example')[0] == 403)
    chk('B nie widzi cennika A', 'zach-kompozyt' not in (sql("SELECT data::text FROM app.user_blobs b JOIN app.profiles p ON p.id=b.owner_id WHERE p.email='b.4c@example.com' AND key='pryw:cennik'") or ''))

    # porównanie tekstu ze starą aplikacją
    if OPISY:
        srv = None
        try: urllib.request.urlopen(OLD + '/prywatne.html', timeout=1)
        except Exception: srv = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=OPISY, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
        oc = br.new_context(); po = oc.new_page(); po.goto(OLD + '/index.html'); po.wait_for_function("window.G&&typeof G.createUser==='function'")
        po.evaluate("async()=>{const r=await G.createUser('Test','haslo-test-1');G.user=r.user;G.key=(await G.session()).key;}")
        po.goto(OLD + '/prywatne.html'); ready(po)
        pg.goto(URL + '/opisy-prywatne'); ready(pg)
        for x in (pg, po): x.evaluate("()=>{Object.assign(V,newVisit());render();}"); x.wait_for_timeout(100)
        wizyta(pg, ini='ab'); wizyta(po, ini='ab')
        pg.evaluate("V.zalUst=false;S.ust.sum=false")   # R11: bez podsumowania; R9 (21.11.2026): zdanie o zaleceniach ustnych wyłączone – reszta tekstu co do znaku jak w starej aplikacji
        a, b = pg.evaluate("curText()"), po.evaluate("curText()")
        chk(f'tekst opisu (kompozyt + skaling + e-ZLA) = stara aplikacja ({len(a)} znaków)', a == b and len(a) > 300, (len(a), len(b)))
        ids = pg.evaluate("KAT.proc.filter(p=>!p.karta).map(p=>p.id)")   # K1: karty procedur nie istnieją w starej aplikacji – porównanie 1:1 dla 19 własnych
        same = 0
        for pid in ids:
            for x in (pg, po):
                x.evaluate("(id)=>{V.items=[];V.ezla={on:false,od:'',do:''};V.zalUst=false;if(S.ust)S.ust.sum=false;V.items.push(newItem(id));render();}", pid); x.wait_for_timeout(40)
            if pg.evaluate("curText()") == po.evaluate("curText()"): same += 1
        chk(f'tekst każdej z {len(ids)} procedur katalogu = stara aplikacja', same == len(ids) == 19, f'{same}/{len(ids)}')
        if srv: srv.terminate()
    else:
        print('UWAGA: pominięto porównanie ze starą aplikacją (brak OPISY_DIR)')
    chk('brak błędów JavaScript', not errs, errs[:5])
    br.close()
t.done('etap 4c: Opisy prywatne')
