# Prompt Patryka 23.11.2026 (pkt 4–7): centralne Zarobki z trzech źródeł (opisy NFZ, opisy prywatne, obrót z Kalendarza),
# rozróżnienie obrotu „obejmuje opisy” / „dodatkowy” (bez podwójnego naliczania), naprawa „0 zł lekarza” w Opisach prywatnych,
# warianty leczenia zachowawczego (1, 2, 3 powierzchnie, nakład). Każdy scenariusz – osobny dzień poprzedniego miesiąca.
import datetime, json
from pomoc import *
t = T(); chk = t.chk
WYNIKI = []                                                                  # do raportu: scenariusz, wejście, źródło, %, wynagrodzenie, Zarobki

def money(s): return int(round(float(s.replace('\xa0', '').replace(' ', '').replace(' ', '').replace('zł', '').replace(',', '.')) * 100))
def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def zarobki(pg, d, gid):
    pg.goto(URL + f'/zarobki?o=own&od={d}&do={d}&g={gid}')
    return {k: money(pg.inner_text(f'[data-testid={k}]')) for k in ['zr-przychod', 'zr-nfz', 'zr-pryw', 'zr-reczny', 'zr-pay', 'zarobek']}

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz Z', 'zr.16@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/gabinety?nowy=1'); fill(pg, name='Gabinet A', pct='40'); pg.select_option('#model', 'pct'); submit(pg, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet A'"); uid = sql("SELECT id FROM app.profiles WHERE email='zr.16@example.com'")
    chk('Gabinet A: model „% od całego obrotu”, 40%', sql(f"SELECT model||'|'||pct::float8 FROM app.clinics WHERE id='{A}'") == 'pct|40')
    first = datetime.date.today().replace(day=1); pm = (first - datetime.timedelta(days=1)).strftime('%Y-%m')
    D = {i: f'{pm}-{i:02d}' for i in range(1, 11)}
    shifts = []
    def put_doc():
        sql(f"INSERT INTO app.calendar_docs(owner_id, doc, data) VALUES ('{uid}', 'm{pm}', '{json.dumps({'shifts': shifts, 'inv': {}})}'::jsonb) ON CONFLICT (owner_id, doc) DO UPDATE SET data = EXCLUDED.data")
    def dyzur(i, d, **kw): shifts.append(dict({'id': f's{i}', 'date': d, 'clinicId': A, 'status': 'done', 'start': '08:00', 'end': '14:00'}, **kw))
    def maG():
        if not pg.evaluate("typeof G!=='undefined'"): pg.goto(URL + '/opisy-prywatne'); ready(pg)
    def pryw(id_, d, items):
        maG()
        its = [{'pid': pid, 'name': n, 'kat': 'zach', 'qty': 1, 'c': c, 'm': 'pct', 'p': 40, 'kw': 0, 'cost': 0, 'val': c, 'pay': c * 40 // 100} for pid, n, c in items]
        pg.evaluate("(m)=>G._post('/api/pryw/wizyty',{put:[m]})", {'id': id_, 'v': 1, 'no': 1, 'date': d, 'created': d + 'T10:00:00.000Z', 'at': d + 'T10:00:00.000Z', 'gab': A,
                    'items': its, 'n': len(its), 'val': sum(x['val'] for x in its), 'pay': sum(x['pay'] for x in its), 'cost': 0, 'edited': False})
    pg.goto(URL + '/opisy-prywatne'); ready(pg)

    # ---- Scenariusz 1: tylko obrót ręczny 1500 zł, 40%
    dyzur(1, D[1], turnover=1500, lab=0); put_doc()
    z = zarobki(pg, D[1], A)
    chk('S1 tylko obrót ręczny 1500 zł → przychód 1500 zł, lekarz 600 zł', (z['zr-przychod'], z['zr-reczny'], z['zr-pay'], z['zarobek']) == (150000, 150000, 60000, 60000), z)
    WYNIKI.append(('S1 tylko obrót ręczny', '1500 zł', 'obrót z Kalendarza', '40%', z['zr-pay'], z['zr-przychod']))
    # zmiana i usunięcie kwoty obrotu
    shifts[0]['turnover'] = 2000; put_doc(); z = zarobki(pg, D[1], A)
    chk('S1 zmiana obrotu na 2000 zł → przychód 2000 zł, lekarz 800 zł', (z['zr-przychod'], z['zr-pay']) == (200000, 80000), z)
    WYNIKI.append(('S1a zmiana obrotu', '2000 zł', 'obrót z Kalendarza', '40%', z['zr-pay'], z['zr-przychod']))
    del shifts[0]['turnover']; put_doc(); z = zarobki(pg, D[1], A)
    chk('S1 usunięcie obrotu → przychód 0 zł, lekarz 0 zł', (z['zr-przychod'], z['zr-pay']) == (0, 0), z)
    WYNIKI.append(('S1b usunięcie obrotu', '—', 'brak', '40%', z['zr-pay'], z['zr-przychod']))

    # ---- Scenariusz 2: tylko opisy prywatne 1000 zł (2 procedury), 40%
    pryw('s2pryw', D[2], [('zach-1pow', 'Wypełnienie – 1 powierzchnia', 60000), ('zach-2pow', 'Wypełnienie – 2 powierzchnie', 40000)])
    z = zarobki(pg, D[2], A)
    chk('S2 tylko opisy prywatne 1000 zł → przychód 1000 zł, lekarz 400 zł (bez dyżuru w Kalendarzu)', (z['zr-przychod'], z['zr-pryw'], z['zr-pay'], z['zarobek']) == (100000, 100000, 40000, 40000), z)
    WYNIKI.append(('S2 tylko opisy prywatne', '600 + 400 zł', 'opisy prywatne', '40%', z['zr-pay'], z['zr-przychod']))

    # ---- Scenariusz 3: tylko opis NFZ 1000 pkt × 1,84 zł = 1840 zł, udział lekarza 40% (ustawienia NFZ)
    maG(); pg.evaluate("(d)=>G._post('/api/nfz/wizyty',{put:[{id:'s3nfz',v:2,no:1,date:d,created:d+'T10:00:00.000Z',at:d+'T10:00:00.000Z',src:'gen',codes:['ST01'],pts:1000,price:1.84,pct:40,revH:0,revRate:350,ex:[],min:null,miss:0,gab:'" + A + "'}]})", D[3])
    z = zarobki(pg, D[3], A)
    chk('S3 tylko NFZ 1000 pkt → przychód 1840 zł, lekarz 736 zł (udział NFZ 40% wg Ustawień – nie % z Cennika)', (z['zr-przychod'], z['zr-nfz'], z['zr-pay']) == (184000, 184000, 73600), z)
    WYNIKI.append(('S3 tylko opis NFZ', '1000 pkt × 1,84 zł', 'opis NFZ', '40% (NFZ)', z['zr-pay'], z['zr-przychod']))

    # ---- Scenariusz 4: opisy prywatne 1000 zł + obrót DODATKOWY 500 zł
    pryw('s4pryw', D[4], [('zach-3pow', 'Wypełnienie – 3 powierzchnie', 100000)]); dyzur(4, D[4], turnover=500, lab=0, obrotTyp='dodatkowy'); put_doc()
    z = zarobki(pg, D[4], A)
    chk('S4 opisy 1000 zł + obrót dodatkowy 500 zł → przychód 1500 zł, lekarz 400 + 200 = 600 zł', (z['zr-przychod'], z['zr-pryw'], z['zr-reczny'], z['zr-pay']) == (150000, 100000, 50000, 60000), z)
    WYNIKI.append(('S4 opisy + obrót dodatkowy', '1000 zł + 500 zł', 'opisy prywatne + obrót (dodatkowy)', '40%', z['zr-pay'], z['zr-przychod']))

    # ---- Scenariusz 5: opisy prywatne 1000 zł + obrót 1000 zł OBEJMUJĄCY opisy (domyślnie)
    pryw('s5pryw', D[5], [('zach-naklad', 'Nakład (inlay / onlay / overlay)', 100000)]); dyzur(5, D[5], turnover=1000, lab=0); put_doc()
    z = zarobki(pg, D[5], A)
    chk('S5 opisy 1000 zł + obrót 1000 zł „obejmuje opisy” → przychód 1000 zł (nie 2000), lekarz 400 zł', (z['zr-przychod'], z['zr-pay']) == (100000, 40000), z)
    WYNIKI.append(('S5 obrót obejmuje opisy', '1000 zł opisy, 1000 zł obrót', 'obrót z Kalendarza (opisy w nim)', '40%', z['zr-pay'], z['zr-przychod']))
    pg.goto(URL + f'/zarobki?o=own&od={D[5]}&do={D[5]}&g={A}')
    chk('S5 dzień po dniu: obrót oznaczony „obejmuje opisy z tego dnia”', 'obejmuje opisy z tego dnia' in pg.inner_text('[data-testid=zr-dni]'))

    # ---- Cały okres: suma bez podwójnego liczenia
    z = zarobki(pg, D[1], A); pg.goto(URL + f'/zarobki?o=own&od={D[1]}&do={D[10]}&g={A}')
    tot = {k: money(pg.inner_text(f'[data-testid={k}]')) for k in ['zr-przychod', 'zr-pay']}
    chk('Okres (S1–S5): przychód 1000 + 1840 + 1500 + 1000 = 5340 zł, lekarz 400 + 736 + 600 + 400 = 2136 zł', (tot['zr-przychod'], tot['zr-pay']) == (534000, 213600), tot)
    WYNIKI.append(('Okres S1–S5', '—', 'wszystkie', '—', tot['zr-pay'], tot['zr-przychod']))
    pg.goto(URL + f'/zarobki?o=own&od={D[1]}&do={D[10]}&g={A}&kw=netto')
    chk('Netto: liczy się z tych samych kwot (bez błędu strony)', pg.locator('[data-testid=zr-pay]').count() == 1)

    # ---- Opisy prywatne w interfejsie: 0 zł lekarza naprawione (% z Gabinetów), warianty 1/2/3/nakład
    pg.goto(URL + '/opisy-prywatne'); ready(pg)
    pg.select_option('#v_gab', A); pg.wait_for_timeout(150)
    for q, pid in [('1 powierzchnia', 'zach-1pow'), ('2 powierzchnie', 'zach-2pow'), ('3 powierzchnie', 'zach-3pow'), ('Nakład', 'zach-naklad')]:
        pg.fill('#p_q', q); pg.wait_for_timeout(120); pg.click(f'button[data-add="{pid}"]'); pg.wait_for_timeout(150)
    for i, c in enumerate(['200', '300', '400', '1500']):
        pg.fill(f'[data-pr="c"][data-i="{i}"]', c); pg.press(f'[data-pr="c"][data-i="{i}"]', 'Tab'); pg.wait_for_timeout(60)
    pays = pg.evaluate("V.items.map(it=>payOf(it).pay)")
    chk('Wynagrodzenie bez % w Cenniku: 40% z „Gabinety” – 200→80, 300→120, 400→160, 1500→600 zł', pays == [8000, 12000, 16000, 60000], pays)
    chk('Procent zapisany w pozycji (p = 40) – późniejsza zmiana % nie przelicza historii', pg.evaluate("V.items.every(it=>it.p===40)"))
    chk('Brak ostrzeżenia „Brak % wynagrodzenia”', 'Brak % wynagrodzenia' not in pg.inner_text('#main'))
    pg.fill('[data-i="0"][data-k="zab"]', '36'); pg.check('[data-i="0"][data-k="pows"][data-o="1"]'); pg.wait_for_timeout(80)
    pg.fill('[data-i="2"][data-k="zab"]', '26'); [pg.check(f'[data-i="2"][data-k="pows"][data-o="{o}"]') for o in (0, 1, 2)]
    pg.fill('[data-i="3"][data-k="zab"]', '46'); pg.select_option('[data-i="3"][data-k="rodzaj"]', 'onlay'); pg.select_option('[data-i="3"][data-k="etap"]', 'osadzenie nakładu'); pg.wait_for_timeout(150)
    txt = pg.evaluate("visitText()")
    chk('Opis: „wypełnienie jednej powierzchni – powierzchnie O”', 'Ząb 36: wypełnienie jednej powierzchni – powierzchnie O.' in txt, txt[:400])
    chk('Opis: „wypełnienie trzech powierzchni – powierzchnie MOD”', 'Ząb 26: wypełnienie trzech powierzchni – powierzchnie MOD.' in txt, txt[:600])
    chk('Opis: nakład typu onlay – osadzenie', 'Ząb 46: nakład typu onlay – osadzenie nakładu.' in txt, txt)
    chk('„Wykonano: …” z wariantami', 'wypełnienie – 2 powierzchnie' in txt.split('\n')[0] and 'nakład (inlay / onlay / overlay)' in txt.split('\n')[0], txt.split('\n')[0])
    pg.click('#b_save'); pg.wait_for_function("V.id&&S.visits.size>=1"); pg.wait_for_timeout(1200)
    vid = pg.evaluate("V.id")
    got = sql(f"SELECT sum(e.value_gr)||'|'||sum(e.doctor_pay_gr) FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id=e.description_id WHERE s.client_key='{vid}'")
    chk('W bazie: wartość 2400 zł, wynagrodzenie 960 zł (= suma pozycji, zgodne z ekranem)', got == '240000|96000', got)
    WYNIKI.append(('UI: 4 procedury prywatne (1/2/3 pow., nakład)', '200 + 300 + 400 + 1500 zł', 'opis prywatny', '40% (z Gabinetów)', 96000, 240000))
    # zmiana % gabinetu → nowa wizyta 50%, zapisana zostaje 40%
    sql(f"UPDATE app.clinics SET pct = 50 WHERE id = '{A}'")
    pg.goto(URL + '/opisy-prywatne'); ready(pg); pg.evaluate("Object.assign(V,newVisit());render()"); pg.select_option('#v_gab', A); pg.wait_for_timeout(100)
    pg.fill('#p_q', '1 powierzchnia'); pg.wait_for_timeout(100); pg.click('button[data-add="zach-1pow"]'); pg.wait_for_timeout(100)
    pg.fill('[data-pr="c"][data-i="0"]', '200'); pg.press('[data-pr="c"][data-i="0"]', 'Tab')
    chk('Zmiana % gabinetu na 50%: nowa procedura 200 zł → 100 zł', pg.evaluate("payOf(V.items[0]).pay") == 10000)
    chk('…a zapisana wcześniej wizyta bez zmian (960 zł)', sql(f"SELECT sum(e.doctor_pay_gr) FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id=e.description_id WHERE s.client_key='{vid}'") == '96000')
    pg.evaluate("Object.assign(V,newVisit());render()"); pg.select_option('#v_gab', '-'); pg.wait_for_timeout(150)
    pg.fill('#p_q', '1 powierzchnia'); pg.wait_for_timeout(100); pg.click('button[data-add="zach-1pow"]'); pg.wait_for_timeout(100)
    pg.fill('[data-pr="c"][data-i="0"]', '200'); pg.press('[data-pr="c"][data-i="0"]', 'Tab'); pg.wait_for_timeout(150)
    chk('Bez gabinetu i bez % w Cenniku: wyraźne ostrzeżenie (nie ciche 0 zł)', 'Brak % wynagrodzenia' in pg.inner_text('#main') and pg.evaluate("payOf(V.items[0]).pay") is None)

    # ---- Kalendarz: przełącznik „obrót a opisy” w formularzu dyżuru
    pg.goto(URL + '/kalendarz'); pg.wait_for_function("window.Kal&&Kal.UI.loaded===true", timeout=20000); pg.wait_for_timeout(500)
    pg.evaluate("Kal.openEditor('s5')"); pg.wait_for_timeout(300)
    chk('Kalendarz: przy obrocie wybór „Obejmuje opisy” / „Dodatkowy” (domyślnie obejmuje)', pg.locator('[data-testid=obrot-typ] button').count() == 2 and pg.get_attribute('[data-a=f-otyp][data-v=opisy]', 'aria-pressed') == 'true')
    pg.click('[data-a=f-otyp][data-v=dodatkowy]'); pg.wait_for_timeout(150)
    chk('Kalendarz: przełączenie na „Dodatkowy” zmienia opis skutku', 'opisy + ten obrót' in pg.inner_text('#shiftForm'))
    pg.evaluate("Kal.UI.edit=null;Kal.UI.tab='set';Kal.render()"); pg.wait_for_timeout(300)
    chk('Kalendarz: ustawienia gabinetu bez pól rozliczeń (są w Gabinety)', pg.locator('[data-testid=rozl-w-gabinetach]').count() >= 1 and pg.locator('[data-bind$=".minDaily"]').count() == 0 and pg.locator('[data-bind$=".payDays"]').count() == 0 and pg.locator('[data-bind$=".expected"]').count() == 0 and pg.locator('[data-bind$=".pct"]').count() == 0)
    chk('Menu: bez zakładki „Konto” (konto pod logo „Gabinet”)', pg.locator('#gbar nav a[href="/konto"]').count() == 0 and pg.locator('#gbar a.gbar-home[href="/konto"]').count() == 1)
    chk('Brak błędów JavaScript', not errs, errs[:3])
    br.close()
print('WYNIKI_FIN=' + json.dumps(WYNIKI, ensure_ascii=False))
t.done('centralne Zarobki – źródła, bez podwójnego liczenia, 0 zł lekarza, warianty (23.11.2026)')
