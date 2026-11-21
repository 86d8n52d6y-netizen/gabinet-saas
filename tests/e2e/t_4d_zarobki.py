# Etap 4d: Zarobki i statystyki ze wszystkich gabinetów – kwoty zgodne z wyliczeniami modułów (grosze), okresy, gabinety,
# podstawa „pełna wartość / udział lekarza”, CSV (format, ochrona przed formułami), izolacja kont.
import urllib.parse, csv, datetime, io, json, urllib.request
from pomoc import *
t = T(); chk = t.chk

def ready_nfz(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def ready_pr(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def synced(pg): pg.wait_for_function("document.getElementById('gsync').textContent.includes('zsynchronizowana')", timeout=10000)
def idle(pg): pg.wait_for_function("!state.pendSig&&!ui.busy", timeout=8000); pg.wait_for_timeout(80)
def fresh(pg):
    if pg.evaluate("state.codes.length"):
        if pg.evaluate("state.step") != 3: pg.click('#steps button[data-n="3"]'); pg.wait_for_timeout(100)
        pg.click('#resetBtn'); pg.wait_for_timeout(150)
        if pg.evaluate("state.codes.length"): pg.click('#resetBtn'); pg.wait_for_timeout(150)
def nfz(pg, gab, date, age='30', plan='II', ini='ab'):
    fresh(pg); pg.click('#steps button[data-n="1"]'); pg.wait_for_timeout(80)
    pg.fill('#i_sv_ini', ini); pg.fill('#i_sh_age', age)
    pg.click(f'button.plan-btn[data-p="o5"][data-w="{plan}"]'); pg.click('#bar button.btn:not(.ghost)')
    if pg.locator('#card-ST30').count(): pg.click('#card-ST30 button[data-act="quadset"][data-q="1,2"]')
    pg.click('#bar button.btn:not(.ghost)'); idle(pg)
    pg.select_option('#i_sv_gab', gab or '-'); pg.fill('#i_sv_date', date); pg.press('#i_sv_date', 'Tab'); pg.wait_for_timeout(300); idle(pg)
def pryw(pg, gab, date, pids):
    pg.evaluate("(a)=>{Object.assign(V,newVisit());V.date=a.d;V.gab=a.g;a.p.forEach(id=>V.items.push(newItem(id)));render();}", {'d': date, 'g': gab, 'p': pids})
    pg.wait_for_timeout(150); pg.click('#b_save'); pg.wait_for_timeout(400)
def money(s): return int(round(float(s.replace('\xa0', '').replace(' ', '').replace('zł', '').replace(',', '.')) * 100)) if s.strip() not in ('—', '') else 0
def table(pg):
    out = {}
    for tr in pg.locator('[data-testid=tabela] tbody tr').all():
        c = [x.inner_text().strip() for x in tr.locator('td').all()]
        out[c[0]] = int(c[1]) if c[1] != '—' else 0      # tabela 21.11.2026: Gabinet | Liczba wizyt | Zarobek lekarza | Zarobek na godzinę
    return out
def razem(pg, url):
    pg.goto(URL + url); return money(pg.inner_text('[data-testid=razem]'))

today = datetime.date.today()
prev = (today.replace(day=1) - datetime.timedelta(days=1)).replace(day=10).isoformat()
T0 = today.isoformat()
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    c0, p0 = konto(br, 'Lekarz A', 'a.4d@example.com', 'zielony-kubek-na-biurku')
    for n in ['Gabinet A', 'Gabinet B']:
        p0.goto(URL + '/gabinety?nowy=1'); fill(p0, name=n, pct='30'); submit(p0, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet A'"); B = sql("SELECT id FROM app.clinics WHERE name='Gabinet B'")
    p0.goto(URL + '/konto'); chk('Konto: kafelki „Dziś” (brak wizyt)', 'Dziś brak zapisanych wizyt' in p0.content() and p0.locator('a.tile').count() == 4 and 'Dziś bez dyżuru' in p0.content())
    c0.close()
    ctx = br.new_context(bypass_csp=True, accept_downloads=True); pg = ctx.new_page()
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/logowanie'); fill(pg, email='a.4d@example.com', password='zielony-kubek-na-biurku'); submit(pg, 'Zaloguj')

    # ---- dane: NFZ (2× A dziś, 1× bez gabinetu dziś, 1× A poprzedni miesiąc) i prywatne (A, B dziś)
    pg.goto(URL + '/opisy-nfz'); ready_nfz(pg)
    nfz(pg, A, T0, plan='II'); nfz(pg, A, T0, plan='III', ini='cd'); nfz(pg, '', T0, plan='IV', ini='ef'); nfz(pg, A, prev, plan='II', ini='gh')
    synced(pg)
    V = pg.evaluate("dbList().map(m=>({gab:m.gab,date:m.date,k:calc(m),vis:isVisit(m)}))")
    chk('NFZ: 4 wizyty zapisane (3 dziś, 1 w poprzednim miesiącu)', len(V) == 4 and sum(1 for v in V if v['date'] == T0) == 3, [(v['gab'][:4], v['date']) for v in V])
    pg.goto(URL + '/opisy-prywatne'); ready_pr(pg)
    tab = lambda k: pg.click(f'#tabs button[data-tab="{k}"]')
    tab('cen'); pg.click(f'button[data-cg="{A}"]'); pg.fill('#c_pct', '40'); pg.press('#c_pct', 'Tab')
    pg.fill('[data-cc="zach-kompozyt"]', '400'); pg.press('[data-cc="zach-kompozyt"]', 'Tab'); pg.fill('[data-cc="hig-skaling"]', '250'); pg.press('[data-cc="hig-skaling"]', 'Tab')
    pg.click(f'button[data-cg="{B}"]'); pg.fill('#c_pct', '35'); pg.press('#c_pct', 'Tab'); pg.fill('[data-cc="zach-kompozyt"]', '350'); pg.press('[data-cc="zach-kompozyt"]', 'Tab'); pg.wait_for_timeout(500)
    tab('wiz'); pryw(pg, A, T0, ['zach-kompozyt', 'hig-skaling']); pryw(pg, B, T0, ['zach-kompozyt']); synced(pg)
    P = pg.evaluate("[...S.visits.values()].map(m=>({gab:m.gab,pay:m.pay,val:m.val,cost:m.cost}))")
    chk('prywatne: 2 wizyty (A: 650 zł → 260 zł; B: 350 zł → 122,50 zł)', sorted([(x['val'], x['pay']) for x in P]) == [(35000, 12250), (65000, 26000)], P)

    # ---- oczekiwane (z wyliczeń modułów)
    def exp(basis, frm, to):
        rows = {}
        for v in V:
            if not (frm <= v['date'] <= to): continue
            k = v['k']; e = (k['sh'] if basis == 'share' else k['pc']) + k['rv'] + k['ex']
            r = rows.setdefault(v['gab'] or '', {'nv': 0, 'e1': 0, 'pv': 0, 'e2': 0}); r['nv'] += 1 if v['vis'] else 0; r['e1'] += e
        for x in P:
            r = rows.setdefault(x['gab'] or '', {'nv': 0, 'e1': 0, 'pv': 0, 'e2': 0}); r['pv'] += 1; r['e2'] += x['pay']
        for r in rows.values(): r['sum'] = r['e1'] + r['e2']
        return rows
    names = {A: 'Gabinet A', B: 'Gabinet B', '': 'Bez gabinetu'}
    vis = lambda rows: {names[k]: v['nv'] + v['pv'] for k, v in rows.items()}
    pg.goto(URL + '/zarobki?o=today'); got = table(pg)
    E = exp('full', T0, T0); e = vis(E)
    chk('Dziś: liczba wizyt w gabinetach = wizyty z modułów (NFZ + prywatne razem)', got == e, (got, e))
    tot = sum(v['sum'] for v in E.values())
    chk('Dziś: „Razem z wizyt” = suma wyliczeń modułów (grosze)', razem(pg, '/zarobki?o=today') == tot)
    for k in (A, B):
        chk(f'Dziś, filtr {names[k]}: „Razem z wizyt” = wyliczenia modułów dla gabinetu (grosze)', razem(pg, f'/zarobki?o=today&g={k}') == E[k]['sum'], (razem(pg, f'/zarobki?o=today&g={k}'), E[k]['sum']))
    pg.goto(URL + '/zarobki?o=prev'); got = table(pg)
    chk('Poprzedni miesiąc: tylko wizyta NFZ z tamtego okresu', got.get('Gabinet A') == 1 and all(v == 0 for k, v in got.items() if k != 'Gabinet A'), got)
    pg.goto(URL + f'/zarobki?o=own&od={prev}&do={T0}'); got = table(pg)
    chk('Własny zakres (poprzedni + bieżący): wizyty = moduły', got == vis(exp('full', prev, T0)), (got, vis(exp('full', prev, T0))))
    pg.goto(URL + f'/zarobki?o=today&g={B}'); got = table(pg)
    chk('Filtr gabinetu: tylko Gabinet B', list(got) == ['Gabinet B'] and got['Gabinet B'] == e['Gabinet B'], got)
    pg.goto(URL + '/zarobki?o=year'); chk('Rok: wykres miesięczny (12 słupków-miesięcy)', 'Miesiąc po miesiącu' in pg.content() and pg.locator('svg[role=img] text').count() == 12)
    pg.goto(URL + '/zarobki?o=month'); chk('Miesiąc: wykres dzienny', 'Dzień po dniu' in pg.content())
    chk('Najczęstsze kody NFZ i procedury prywatne', 'Najczęstsze kody' in pg.content() and 'Najczęstsze procedury' in pg.content())

    # ---- 5.6: porównanie okresów, średnie, dni tygodnia, filtr rodzaju/kategorii
    pg.goto(URL + '/zarobki?o=month')
    exp_prev = sum(v['k']['pc'] + v['k']['rv'] + v['k']['ex'] for v in V if v['date'][:7] == prev[:7])
    chk('Porównanie: „Poprzedni okres” (miesiąc wcześniej) = zarobki z poprzedniego miesiąca', money(pg.inner_text('[data-testid=poprz]')) == exp_prev and exp_prev > 0, (pg.inner_text('[data-testid=poprz]'), exp_prev))
    chk('Porównanie: różnica kwotowa i procentowa', '%' in pg.inner_text('[data-testid=zmiana]'), pg.inner_text('[data-testid=zmiana]'))
    pg.goto(URL + '/zarobki?o=today'); rz = money(pg.inner_text('[data-testid=razem]'))
    dni = pg.locator('[data-testid=dni] tbody tr').all_inner_texts()
    import datetime as _dt
    dow = _dt.date.fromisoformat(T0).isoweekday()
    chk('Dni tygodnia: 7 wierszy, dzisiejszy dzień = „Razem”, 1 dzień pracy', len(dni) == 7 and money(dni[dow - 1].split('\t')[2]) == rz and dni[dow - 1].split('\t')[1] == '1', dni)
    sr = pg.locator('[data-testid=srednie] tr').all_inner_texts()
    chk('Średnie: 1 dzień pracy, średnio na dzień = „Razem”, na wizytę = Razem / 5 wizyt', sr[0].endswith('1') and money(sr[1].split('\t')[1]) == rz and money(sr[2].split('\t')[1]) == round(rz / 5), sr)
    pg.goto(URL + '/zarobki?o=today&k=nfz'); got = table(pg)
    chk('Filtr „NFZ”: tylko wizyty NFZ i kwoty NFZ', {k: v for k, v in got.items() if v} == {names[k]: v['nv'] for k, v in E.items() if v['nv']} and money(pg.inner_text('[data-testid=razem]')) == sum(v['e1'] for v in E.values()), got)
    chk('Filtr rodzaju: zarobek lekarza (Kalendarz) niedostępny – „—”', pg.inner_text('[data-testid=zarobek]').strip() == '—')
    kat = sql("SELECT category_name FROM app.earnings_entries WHERE label ILIKE '%kompozyt%' LIMIT 1")
    pg.goto(URL + '/zarobki?o=today&k=' + urllib.parse.quote('kat:' + kat)); got = table(pg)
    chk(f'Filtr kategorii „{kat}”: tylko wypełnienia (A 160 zł + B 122,50 zł), bez NFZ', money(pg.inner_text('[data-testid=razem]')) == 28250 and got.get('Gabinet A') == 1 and got.get('Gabinet B') == 1 and sum(got.values()) == 2, got)
    chk('Filtr widoczny i do wyłączenia', 'pokaż wszystko' in pg.content())

    # ---- podstawa: udział lekarza
    pg.goto(URL + '/ustawienia'); pg.select_option('#basis', 'share'); submit(pg, 'Zapisz ustawienia')
    E2 = exp('share', T0, T0)
    chk('Podstawa „udział lekarza”: „Razem z wizyt” = udział + przeglądy + dodatkowe + prywatne', razem(pg, '/zarobki?o=today') == sum(v['sum'] for v in E2.values()))
    chk('Podstawa „udział lekarza”: także dla gabinetu A', razem(pg, f'/zarobki?o=today&g={A}') == E2[A]['sum'])
    pg.goto(URL + '/zarobki?o=today')

    # ---- CSV
    with pg.expect_download() as d: pg.click('a:has-text("Pobierz CSV")')
    raw = open(d.value.path(), 'rb').read()
    txt = raw.decode('utf-8-sig'); rows = list(csv.reader(io.StringIO(txt), delimiter=';'))
    chk('CSV: UTF-8 z BOM, średnik, nagłówek po polsku', raw[:3] == b'\xef\xbb\xbf' and rows[0][:3] == ['Data', 'Gabinet', 'Moduł'], rows[0])
    s_pay = sum(int(round(float(r[12].replace(',', '.')) * 100)) for r in rows[1:])
    chk('CSV: suma „Dla lekarza” = suma wszystkich kwot w okresie (grosze)', s_pay == sum(x['pay'] for x in P) + sum(v['k']['sh'] + v['k']['rv'] + v['k']['ex'] for v in V if v['date'] >= T0[:8] + '01'), s_pay)
    chk('CSV: brak inicjałów pacjentów', all(x not in txt for x in ['AB', 'CD', 'EF', 'GH']))
    ck = '; '.join(f"{c['name']}={c['value']}" for c in ctx.cookies() if c['name'].startswith('gabinet_sesja'))
    bad = {'id': 'vcsv1', 'no': 9, 'date': T0, 'created': T0 + 'T10:00:00.000Z', 'at': T0 + 'T10:00:00.000Z', 'src': 'man', 'codes': [], 'pts': 0, 'price': 1.84, 'pct': 40,
           'revH': 0, 'revRate': 350, 'ex': [{'c': 100, 'd': '=HYPERLINK("http://zly.example")'}], 'min': None, 'miss': 0, 'gab': ''}
    rq = urllib.request.Request(URL + '/api/nfz/wizyty', data=json.dumps({'put': [bad]}).encode(), headers={'Content-Type': 'application/json', 'Origin': URL, 'Cookie': ck}, method='POST')
    urllib.request.urlopen(rq).read()
    with pg.expect_download() as d: pg.goto(URL + '/zarobki'); pg.click('a:has-text("Pobierz CSV")')
    txt2 = open(d.value.path(), 'rb').read().decode('utf-8-sig')
    chk('CSV: ochrona przed formułami (=… zapisane jako tekst)', "'=HYPERLINK" in txt2 and ';=HYPERLINK' not in txt2)

    # ---- Konto: kafelki „Dziś”
    pg.goto(URL + '/konto'); tiles = pg.locator('a.tile').all_inner_texts()
    chk('Konto: kafelki „Dziś” z liczbą wizyt i kwotą (wpis z samą kwotą dodatkową nie jest wizytą – jak w obecnej aplikacji)', 'Dziś bez dyżuru' in tiles[0] and 'Dziś: 3 wizyty' in tiles[1] and 'Dziś: 2 wizyty' in tiles[2] and 'Dziś razem' in tiles[3], tiles)

    # ---- izolacja
    cb, pb = konto(br, 'Lekarz B', 'b.4d@example.com', 'niebieska-lampa-w-oknie')
    pb.goto(URL + '/zarobki?o=year'); chk('B: zero zarobków i brak gabinetów A', money(pb.inner_text('[data-testid=razem]')) == 0 and 'Gabinet A' not in pb.content())
    r = cb.request.get(URL + f'/zarobki/csv?od=2000-01-01&do=2100-12-31&g={A}')
    chk('B: CSV z filtrem gabinetu A – tylko nagłówek', r.status == 200 and len(r.text().strip().splitlines()) == 1, r.text()[:200])
    r = br.new_context().request.get(URL + '/zarobki/csv?od=2026-01-01&do=2026-12-31')
    chk('CSV bez logowania → 401', r.status == 401)
    chk('brak błędów JavaScript', not errs, errs[:3])
    br.close()
t.done('etap 4d: zarobki i statystyki')
