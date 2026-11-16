# Etap 4e-2: przeniesienie danych ze starej aplikacji – plik „Kopia całości” utworzony w obecnej aplikacji (OPISY_DIR, http.server 8765)
# → /import w SaaS: dopasowanie gabinetów (ta sama nazwa → istniejący, inne → nowy), Kalendarz, cennik, wizyty NFZ i prywatne
# (treść i inicjały tylko na urządzeniu, na koncie bez danych pacjentów), ponowny import bez duplikatów, złe hasło.
import json, os, subprocess, time, urllib.request, datetime
from pomoc import *
t = T(); chk = t.chk
OPISY = os.environ.get('OPISY_DIR'); OLD = 'http://127.0.0.1:8765'
TODAY = datetime.date.today().isoformat(); MK = TODAY[:7]
PWD_OLD = 'haslo-starej-aplikacji-1'

def idle(pg): pg.wait_for_function("!state.pendSig&&!ui.busy", timeout=8000); pg.wait_for_timeout(80)
def fresh(pg):
    if pg.evaluate("state.codes.length"):
        if pg.evaluate("state.step") != 3: pg.click('#steps button[data-n="3"]'); pg.wait_for_timeout(100)
        pg.click('#resetBtn'); pg.wait_for_timeout(150)
        if pg.evaluate("state.codes.length"): pg.click('#resetBtn'); pg.wait_for_timeout(150)
def nfz(pg, gab, date, plan='II', ini='ab'):
    fresh(pg); pg.click('#steps button[data-n="1"]'); pg.wait_for_timeout(80)
    pg.fill('#i_sv_ini', ini); pg.fill('#i_sh_age', '30')
    pg.click(f'button.plan-btn[data-p="o5"][data-w="{plan}"]'); pg.click('#bar button.btn:not(.ghost)')
    if pg.locator('#card-ST30').count(): pg.click('#card-ST30 button[data-act="quadset"][data-q="1,2"]')
    pg.click('#bar button.btn:not(.ghost)'); idle(pg)
    pg.select_option('#i_sv_gab', gab or '-'); pg.fill('#i_sv_date', date); pg.press('#i_sv_date', 'Tab'); pg.wait_for_timeout(300); idle(pg)
def ready_nfz(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def ready_pr(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def login2(br, email, pwd):
    c = br.new_context(bypass_csp=True); p_ = c.new_page()
    p_.goto(URL + '/logowanie'); fill(p_, email=email, password=pwd); submit(p_, 'Zaloguj'); return c, p_

if not OPISY:
    print('UWAGA: pominięto test importu (brak OPISY_DIR – potrzebna obecna aplikacja do utworzenia pliku kopii)'); t.done('import kopii')

srv = None
try: urllib.request.urlopen(OLD + '/index.html', timeout=1)
except Exception: srv = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=OPISY, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    # ---- obecna aplikacja: konto, Kalendarz (2 gabinety), wizyty NFZ i prywatne, cennik → kopia całości
    oc = br.new_context(); po = oc.new_page(); po.goto(OLD + '/index.html'); po.wait_for_function("window.G&&typeof G.createUser==='function'")
    po.evaluate("async(p)=>{const r=await G.createUser('Lekarz',p);G.user=r.user;G.key=(await G.session()).key;}", PWD_OLD)
    po.evaluate(f"""async()=>{{await G.store('kv').put('grafik',{{settings:{{v:1,clinics:[
        {{id:'c1',name:'Gabinet Alfa',short:'ALF',color:2,active:true,model:'pct_lab',pct:30,labShare:0,hourly:0,daily:0,minDaily:0,presets:[{{id:'p1',name:'Rano',start:'08:00',end:'14:00'}}],week:{{slots:[{{day:1,pid:'p1'}}],freq:'weekly'}}}},
        {{id:'c2',name:'Gabinet Beta',short:'BET',color:5,active:true,model:'pct',pct:40,labShare:0,hourly:0,daily:0,minDaily:0,presets:[],week:{{slots:[],freq:'weekly'}}}}],
        jdgStart:'2026-10',zus:[{{id:'z1',from:'2026-10',variant:'custom',amount:900,base:0,chor:true}}]}},
      'm{MK}':{{shifts:[{{id:'s1',date:'{TODAY}',clinicId:'c1',start:'08:00',end:'14:00',status:'done',turnover:6000,lab:1000}},
                       {{id:'s2',date:'{MK}-02',clinicId:'c2',start:'09:00',end:'15:00',status:'done',turnover:3000,lab:0}}],off:{{}},inv:{{'c2':{{issued:true}}}},costs:[]}}}});}}""")
    po.goto(OLD + '/nfz.html'); ready_nfz(po)
    nfz(po, 'c1', TODAY, plan='II', ini='kw'); nfz(po, 'c2', TODAY, plan='III', ini='mn')
    old_nfz = po.evaluate("dbList().map(m=>({id:m.id,gab:m.gab,k:calc(m)}))")
    chk('obecna aplikacja: 2 wizyty NFZ', len(old_nfz) == 2, old_nfz)
    po.goto(OLD + '/prywatne.html'); ready_pr(po)
    po.click('#tabs button[data-tab="cen"]'); po.click('button[data-cg="c1"]'); po.fill('#c_pct', '40'); po.press('#c_pct', 'Tab')
    po.fill('[data-cc="zach-kompozyt"]', '500'); po.press('[data-cc="zach-kompozyt"]', 'Tab'); po.wait_for_timeout(500)
    po.click('#tabs button[data-tab="wiz"]')
    po.evaluate(f"()=>{{Object.assign(V,newVisit());V.date='{TODAY}';V.gab='c1';V.ini='PR';V.items.push(newItem('zach-kompozyt'));render();}}")
    po.wait_for_timeout(150); po.click('#b_save'); po.wait_for_timeout(600)
    old_pr = po.evaluate("[...S.visits.values()].map(m=>({id:m.id,gab:m.gab,pay:m.pay,ini:m.ini}))")
    chk('obecna aplikacja: wizyta prywatna 500 zł → lekarz 200 zł', len(old_pr) == 1 and old_pr[0]['pay'] == 20000, old_pr)
    po.goto(OLD + '/index.html'); po.wait_for_function("window.G&&G.backup")
    po.evaluate("async()=>{G.user=G.user||(await G.session()).user;}")
    kopia = po.evaluate("async(p)=>{const r=await G.backup.export(p);return await r.blob.text();}", PWD_OLD)
    chk('plik „Kopia całości” utworzony w obecnej aplikacji (zaszyfrowany)', json.loads(kopia).get('app') == 'gabinet-kopia' and 'Gabinet Alfa' not in kopia)
    path = '/tmp/gabinet-kopia-test.json'; open(path, 'w').write(kopia)
    oc.close()

    # ---- SaaS: konto z gabinetem „Gabinet Alfa” (dopasowanie po nazwie)
    c0, p0 = konto(br, 'Lekarz', 'imp@example.com', 'zielony-kubek-na-biurku')
    p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name='Gabinet Alfa', pct='25'); submit(p0, 'Dodaj gabinet'); c0.close()
    ALFA = sql("SELECT id FROM app.clinics WHERE name='Gabinet Alfa'")
    ctx, pg = login2(br, 'imp@example.com', 'zielony-kubek-na-biurku')
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/konto'); chk('Konto: link „Przenieś dane ze starej aplikacji”', pg.locator('a[href="/import"]').count() >= 1)
    pg.goto(URL + '/import')
    pg.set_input_files('#plik', path); pg.fill('#haslo', 'zle-haslo-123'); pg.click('#b1'); pg.wait_for_timeout(4000)
    chk('złe hasło → komunikat, nic nie przeniesione', 'Nieprawidłowe hasło' in pg.inner_text('#m1') and pg.locator('#krok2').is_hidden(), pg.inner_text('#m1'))
    pg.fill('#haslo', PWD_OLD); pg.click('#b1'); pg.wait_for_selector('#krok2:not([hidden])', timeout=20000)
    s = pg.inner_text('#podsum')
    chk('podsumowanie kopii: 2 wizyty NFZ, 1 prywatna, 1 miesiąc, 2 dyżury', '2 wizyty' in s and '1 wizyta' in s and '2 dyżurów' in s, s)
    sel = pg.locator('#mapa select')
    chk('gabinety: Alfa → istniejący (ta sama nazwa), Beta → nowy', sel.count() == 2 and sel.nth(0).input_value() == ALFA and sel.nth(1).input_value() == 'new', [sel.nth(i).input_value() for i in range(sel.count())])
    pg.click('#b2'); pg.wait_for_function("document.getElementById('h3').textContent.startsWith('Gotowe')||document.getElementById('h3').textContent.includes('błęd')||document.getElementById('h3').textContent.startsWith('Nie')", timeout=30000)
    logt = pg.inner_text('#log'); print(logt)
    chk('import zakończony bez błędów', pg.inner_text('#h3').startswith('Gotowe'), logt)
    BETA = sql("SELECT id FROM app.clinics WHERE name='Gabinet Beta'")
    chk('gabinety na koncie: Alfa (istniejący, 25%) + nowy Beta (model % od obrotu, 40%)', sql("SELECT count(*) FROM app.clinics WHERE deleted_at IS NULL") == '2'
        and sql(f"SELECT model||'|'||pct::float8 FROM app.clinics WHERE id='{BETA}'") == 'pct|40' and sql(f"SELECT pct::float8 FROM app.clinics WHERE id='{ALFA}'") == '25')
    m = json.loads(sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'") or '{}')
    chk('Kalendarz: dyżury z identyfikatorami gabinetów z konta (c1→Alfa, c2→Beta), rozliczenie Beta', sorted(x['clinicId'] for x in m.get('shifts', [])) == sorted([ALFA, BETA]) and BETA in m.get('inv', {}), m)
    st = json.loads(sql("SELECT data::text FROM app.calendar_docs WHERE doc='settings'") or '{}')
    chk('Kalendarz: ustawienia (ZUS 900 zł, dni pracy Alfa „Rano” w poniedziałki)', st.get('zus', [{}])[0].get('amount') == 900 and any(c['id'] == ALFA and c.get('week', {}).get('slots') for c in st.get('clinics', [])), st.get('clinics'))
    chk('w danych na koncie nie ma starych identyfikatorów c1/c2', '"c1"' not in sql("SELECT string_agg(data::text,' ') FROM app.calendar_docs") + sql("SELECT string_agg(data::text,' ') FROM app.user_blobs"))
    cen = json.loads(sql("SELECT data::text FROM app.user_blobs WHERE key='pryw:cennik'") or '{}')
    chk('cennik: 500 zł / 40% przy gabinecie Alfa', cen.get('gab', {}).get(ALFA, {}).get('items', {}).get('zach-kompozyt', {}).get('c') == 50000, cen)
    chk('historia na koncie: 2 wizyty NFZ + 1 prywatna (gabinety z konta)', sql("SELECT count(*) FILTER (WHERE module='nfz')||'|'||count(*) FILTER (WHERE module='private') FROM app.saved_descriptions WHERE deleted_at IS NULL") == '2|1'
        and sql(f"SELECT clinic_id FROM app.saved_descriptions WHERE module='private'") == ALFA)
    dump = sql("SELECT string_agg(t::text,' ') FROM (SELECT row_to_json(s) t FROM app.saved_descriptions s UNION ALL SELECT row_to_json(e) FROM app.earnings_entries e) x")
    chk('na koncie BRAK inicjałów (KW, MN, PR) i treści opisów', all(x not in dump for x in ['"KW"', '"MN"', '"PR"', '"ini"']) and 'Rozpoznanie' not in dump)
    chk('kwoty prywatne = stara aplikacja (200 zł dla lekarza)', sql("SELECT sum(doctor_pay_gr) FROM app.earnings_entries WHERE source='private_procedure'") == '20000')
    exp_pc = sum(v['k']['pc'] for v in old_nfz)
    chk('kwoty NFZ (wartość punktów) = stara aplikacja', sql("SELECT sum(value_gr) FROM app.earnings_entries WHERE source='nfz_points'") == str(exp_pc), (sql("SELECT sum(value_gr) FROM app.earnings_entries WHERE source='nfz_points'"), exp_pc))

    # moduły na tym urządzeniu: treść opisów i inicjały dostępne
    pg.goto(URL + '/opisy-nfz'); ready_nfz(pg)
    L = pg.evaluate("dbList().map(m=>({gab:m.gab,ini:m.ini,body:!!m.id}))")
    chk('Opisy NFZ na tym urządzeniu: 2 wizyty z inicjałami, gabinety z konta', len(L) == 2 and sorted(x['ini'] for x in L) == ['KW', 'MN'] and {x['gab'] for x in L} == {ALFA, BETA}, L)
    pg.goto(URL + '/opisy-prywatne'); ready_pr(pg)
    P = pg.evaluate("[...S.visits.values()].map(m=>({gab:m.gab,ini:m.ini,pay:m.pay}))")
    chk('Opisy prywatne na tym urządzeniu: wizyta „PR” w Alfa, 200 zł', P == [{'gab': ALFA, 'ini': 'PR', 'pay': 20000}], P)
    pg.goto(URL + '/kalendarz'); pg.wait_for_function("window.Kal&&Kal.UI.loaded===true", timeout=20000); pg.wait_for_timeout(1500)
    chk('Kalendarz otwiera się z przeniesionymi dyżurami (s1, s2; dni pracy dopisują kolejne jak w obecnej aplikacji)', pg.evaluate(f"['s1','s2'].every(id=>Kal.M('{MK}').shifts.some(s=>s.id===id))"))

    # ponowny import: bez duplikatów
    pg.goto(URL + '/import'); pg.set_input_files('#plik', path); pg.fill('#haslo', PWD_OLD); pg.click('#b1'); pg.wait_for_selector('#krok2:not([hidden])', timeout=20000)
    chk('ponownie: oba gabinety dopasowane do istniejących', [pg.locator('#mapa select').nth(i).input_value() for i in range(2)] == [ALFA, BETA])
    pg.click('#b2'); pg.wait_for_function("document.getElementById('h3').textContent.startsWith('Gotowe')", timeout=30000)
    chk('ponowny import: bez duplikatów (2 gabinety, 2+1 wizyty, dyżur s1 raz)', sql("SELECT count(*) FROM app.clinics WHERE deleted_at IS NULL") == '2'
        and sql("SELECT count(*) FROM app.saved_descriptions WHERE deleted_at IS NULL") == '3'
        and [x['id'] for x in json.loads(sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'"))['shifts']].count('s1') == 1, pg.inner_text('#log'))

    # kopia z tego urządzenia → nowe urządzenie (pusta przeglądarka) → wczytanie: treść opisów i inicjały wracają
    ctx.set_default_timeout(30000)
    pg.goto(URL + '/import'); pg.fill('#h1', 'haslo-kopii-urzadzenia'); pg.fill('#h2', 'haslo-kopii-urzadzenia')
    with pg.expect_download() as d: pg.click('#b9')
    kop2 = open(d.value.path()).read()
    chk('kopia z urządzenia: plik zaszyfrowany (bez inicjałów i nazw)', json.loads(kop2).get('app') == 'gabinet-kopia' and set(json.loads(kop2)) == {'app', 'v', 'at', 'kdf', 'iv', 'ct'} and 'Gabinet Alfa' not in kop2)
    chk('kopia z urządzenia: komunikat z liczbą wizyt i data ostatniej kopii', '2 wizyty' in pg.inner_text('#m0') and 'Ostatnia kopia' in pg.inner_text('#ost'), pg.inner_text('#m0'))
    path2 = '/tmp/gabinet-kopia-saas.json'; open(path2, 'w').write(kop2)
    c3 = br.new_context(bypass_csp=True); p3 = c3.new_page(); p3.goto(URL + '/logowanie'); fill(p3, email='imp@example.com', password='zielony-kubek-na-biurku'); submit(p3, 'Zaloguj')
    p3.goto(URL + '/opisy-nfz'); ready_nfz(p3)
    chk('nowe urządzenie przed wczytaniem: wizyty z konta bez inicjałów', sorted((x or '') for x in p3.evaluate("dbList().map(m=>m.ini||'')")) == ['', ''])
    p3.goto(URL + '/import'); p3.set_input_files('#plik', path2); p3.fill('#haslo', 'haslo-kopii-urzadzenia'); p3.click('#b1'); p3.wait_for_selector('#krok2:not([hidden])', timeout=30000)
    chk('własna kopia: gabinety dopasowane do tych samych (identyfikator)', sorted(p3.locator('#mapa select').nth(i).input_value() for i in range(p3.locator('#mapa select').count())) == sorted([ALFA, BETA]))
    p3.click('#b2'); p3.wait_for_function("document.getElementById('h3').textContent.startsWith('Gotowe')", timeout=30000)
    p3.goto(URL + '/opisy-nfz'); ready_nfz(p3)
    chk('nowe urządzenie po wczytaniu: inicjały KW, MN wróciły', sorted(p3.evaluate("dbList().map(m=>m.ini)")) == ['KW', 'MN'])
    p3.goto(URL + '/opisy-prywatne'); ready_pr(p3)
    chk('nowe urządzenie: wizyta prywatna „PR”', [m['ini'] for m in p3.evaluate("[...S.visits.values()]")] == ['PR'])
    chk('konto bez zmian po wczytaniu własnej kopii (2 gabinety, 3 wizyty)', sql("SELECT count(*) FROM app.clinics WHERE deleted_at IS NULL") == '2' and sql("SELECT count(*) FROM app.saved_descriptions WHERE deleted_at IS NULL") == '3')
    chk('brak błędów JavaScript', not errs, errs[:5])
    br.close()
if srv: srv.terminate()
t.done('import kopii ze starej aplikacji')
