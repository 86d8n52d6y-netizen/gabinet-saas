# Prompt Patryka 21.11.2026 („Rozwój aplikacji Gabinet”): zmiany w generatorze Opisów NFZ.
# 3.1 pasek dolny bez kwot (zarobki tylko w statystykach), 7.1 przyczyna urazu „nagryzienie na twardy przedmiot”,
# 7.2 opcjonalna informacja o niepewnym rokowaniu w leczeniu zachowawczym (domyślnie nic nie dodaje).
from pomoc import *
t = T(); chk = t.chk
ROK_PELNA = 'Pacjent został poinformowany o niepewnym rokowaniu dotyczącym dalszego utrzymania zęba oraz o możliwych dalszych konsekwencjach leczenia.'
ROK_KROTKA = 'Pacjenta poinformowano o niepewnym rokowaniu leczonego zęba.'

def ready(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def idle(pg): pg.wait_for_function("!state.pendSig&&!ui.busy", timeout=8000); pg.wait_for_timeout(80)
def codes(pg, cs):
    pg.click('#steps button[data-n="1"]'); pg.wait_for_timeout(80)
    pg.fill('#codeIn', cs); pg.click('button[data-act="addcodes"]'); pg.wait_for_timeout(120)
def step(pg, n): pg.click(f'#steps button[data-n="{n}"]'); pg.wait_for_timeout(150)
def seg(pg, key, v): pg.click(f'button[data-act="seg"][data-key="{key}"][data-v="{v}"]'); pg.wait_for_timeout(120)
def txt(pg): return pg.evaluate("genTxt()")
def bar(pg): return pg.inner_text('#bar')

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz P', 'p.7@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/opisy-nfz'); ready(pg)

    # ---- 3.1 pasek dolny bez kwot
    pg.fill('#i_sh_age', '30'); codes(pg, 'ST34')
    chk('pasek (Kody): bez kwoty w zł', 'zł' not in bar(pg), bar(pg))
    step(pg, 2); chk('pasek (Pytania): bez wyceny w zł', 'zł' not in bar(pg) and 'pkt' not in bar(pg), bar(pg))
    step(pg, 3); chk('pasek (Opis): bez wyceny w zł', 'zł' not in bar(pg), bar(pg))
    chk('wycena wizyty zostaje w karcie „Cały opis”', 'Wycena wizyty:' in pg.content())
    step(pg, 5); chk('pasek (Statystyki): bez „Dziś: … zł”', 'zł' not in bar(pg) and 'Dziś' not in bar(pg), bar(pg))
    step(pg, 1); pg.click('#resetBtn') if pg.locator('#resetBtn').count() else None

    # ---- 7.1 badanie po urazie
    pg.evaluate("state.codes=[];render()"); codes(pg, 'ST28'); step(pg, 2)
    chk('ST28: opcja „nagryzienie na twardy przedmiot”', pg.locator('button[data-key="ST28.cause"][data-v="nagryzienie na twardy przedmiot"]').count() == 1)
    chk('ST28: dotychczasowe przyczyny zostają', all(pg.locator(f'button[data-key="ST28.cause"][data-v="{v}"]').count() == 1 for v in ['upadek', 'uderzenie', 'upadek i nagryzienie na twardy przedmiot']))
    seg(pg, 'ST28.cause', 'nagryzienie na twardy przedmiot')
    chk('ST28: przyczyna w opisie badania', '(nagryzienie na twardy przedmiot)' in txt(pg), txt(pg)[:400])

    # ---- 7.2 niepewne rokowanie
    pg.evaluate("state.codes=[];state.a={};render()"); codes(pg, 'ST34'); step(pg, 2)
    chk('rokowanie: brak opcji bez leczenia zachowawczego', pg.locator('button[data-key="sh.rok"]').count() == 0)
    codes(pg, '1105'); step(pg, 2)
    chk('rokowanie: opcja przy leczeniu zachowawczym (3 przyciski)', pg.locator('button[data-key="sh.rok"]').count() == 3)
    base = txt(pg)
    chk('rokowanie: domyślnie nic nie dodaje (opis jak dotąd)', 'rokowani' not in base)
    seg(pg, 'sh.rok', 'pełna informacja'); t1 = txt(pg)
    chk('rokowanie: pełna informacja na końcu opisu zabiegu zachowawczego', t1.rstrip().endswith(ROK_PELNA) and t1.count(ROK_PELNA) == 1, t1[-300:])
    seg(pg, 'sh.rok', 'krótka informacja'); t2 = txt(pg)
    chk('rokowanie: krótka wersja zamiast pełnej', ROK_KROTKA in t2 and ROK_PELNA not in t2)
    seg(pg, 'sh.rok', 'nie dotyczy')
    chk('rokowanie: „nie dotyczy” = opis bez zdania o rokowaniu', txt(pg) == base)
    chk('rokowanie: pole nieobowiązkowe (nie zwiększa „do uzupełnienia”)', pg.evaluate("missCount()") == pg.evaluate("(()=>{const s=state.a['sh.rok'];delete state.a['sh.rok'];const n=missCount();state.a['sh.rok']=s;return n;})()"))
    seg(pg, 'sh.rok', 'pełna informacja'); step(pg, 3)
    chk('rokowanie: zdanie w kopiowanym opisie (krok 3)', ROK_PELNA in pg.evaluate("fullTxt()"))

    # ---- 1.1 lakiery fluorkowe
    pg.goto(URL + '/opisy-nfz'); ready(pg)
    pg.evaluate("state.codes=[];state.a={};render()"); codes(pg, '1101,1006'); step(pg, 2)
    dl = pg.evaluate("[...document.querySelectorAll('datalist option')].map(o=>o.value)")
    chk('1101: lista lakierów (Profluorid, Duraphat, Fluor Protector, Elmex jako żel)', all(x in dl for x in ['VOCO Profluorid Varnish', 'Duraphat (Colgate)', 'Fluor Protector (Ivoclar)', 'Elmex gelée (żel fluorkowy)']), dl)
    b1006 = txt(pg)
    chk('1006: bez wyboru preparatu opis jak dotąd', 'Zastosowany preparat' not in b1006)
    pg.fill('[data-key="1006.prep"]', 'Duraphat (Colgate)'); pg.wait_for_timeout(250)
    chk('1006: wybrany preparat w opisie', 'Zastosowany preparat: Duraphat (Colgate).' in txt(pg), txt(pg)[-300:])
    pg.fill('[data-key="1101.prep"]', 'Mój lakier XYZ'); pg.wait_for_timeout(250)
    chk('1101: własna nazwa lakieru wpisana ręcznie trafia do opisu', '(Mój lakier XYZ)' in txt(pg))

    # ---- 3.2 Statystyki bez kolumn „Z punktów” i „Z przeglądów”
    step(pg, 5); pg.wait_for_timeout(300)
    heads = pg.evaluate("[...document.querySelectorAll('table.stat th')].map(t=>t.textContent)")
    chk('Statystyki: bez kolumn „Z punktów” i „Z przeglądów”', 'Z punktów' not in heads and 'Z przeglądów' not in heads, heads)

    # ---- etap 5: Opisy prywatne – wizyta bez treści na tym urządzeniu nie wisi na „Wczytuję…”
    pg.goto(URL + '/opisy-prywatne'); pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000)
    pg.evaluate("""async () => { const now=new Date().toISOString(), id='bez-tresci-1';
      await G.store('wizyty').put(id,{id,no:1,date:G.today(),gab:'',created:now,at:now,edited:false,ini:'AB',body:true,miss:0,val:40000,pay:16000,cost:0,
        items:[{pid:'zach-kompozyt',name:'Wypełnienie kompozytowe',kat:'Zachowawcze',qty:1,c:40000,m:'pct',p:40,kw:0,cost:0,val:40000,pay:16000}]});
      await G.store('opisy').del(id); }""")
    pg.goto(URL + '/opisy-prywatne'); pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000)
    pg.evaluate("S.tab='hist';render()"); pg.wait_for_timeout(150)
    pg.click('button[data-a="hshow"][data-id="bez-tresci-1"]'); pg.wait_for_timeout(400)
    art = pg.inner_text('#h-bez-tresci-1')
    chk('prywatne: brak treści na urządzeniu → komunikat zamiast „Wczytuję…”', 'Treści tego opisu nie ma na tym urządzeniu' in art and 'Wczytuję' not in art, art)
    pg.click('button[data-a="hcopy"][data-id="bez-tresci-1"]'); pg.wait_for_timeout(200)
    chk('prywatne: „Kopiuj opis” bez treści → konkretny komunikat', 'nie ma na tym urządzeniu' in pg.inner_text('body'))
    chk('prywatne: kwoty i procedury wizyty zostają', '160,00' in art.replace('\xa0', ' ') and 'Wypełnienie kompozytowe' in art, art)

    # ---- 3.3 Kalendarz → Rozliczenia: kwota z rozliczenia gabinetu zasila Zarobki (jak w Kalendarzu: zamiast sumy z dyżurów)
    import datetime, json
    def money(s): return int(round(float(s.replace('\xa0', '').replace(' ', '').replace(' ', '').replace('zł', '').replace(',', '.')) * 100))
    pg.goto(URL + '/gabinety?nowy=1'); fill(pg, name='Rozliczany', pct='40'); submit(pg, 'Dodaj gabinet')
    gid = sql("SELECT id FROM app.clinics WHERE name='Rozliczany'"); uid = sql("SELECT id FROM app.profiles WHERE email='p.7@example.com'")
    first = datetime.date.today().replace(day=1); pm = (first - datetime.timedelta(days=1)).strftime('%Y-%m')
    doc = {'shifts': [{'id': 's1', 'date': pm + '-10', 'clinicId': gid, 'status': 'done', 'start': '08:00', 'end': '14:00', 'turnover': 1000, 'lab': 0},
                      {'id': 's2', 'date': pm + '-11', 'clinicId': gid, 'status': 'done', 'start': '08:00', 'end': '12:00', 'turnover': 500, 'lab': 0}], 'inv': {}}
    def put_doc(d): sql(f"INSERT INTO app.calendar_docs(owner_id, doc, data) VALUES ('{uid}', 'm{pm}', '{json.dumps(d)}'::jsonb) ON CONFLICT (owner_id, doc) DO UPDATE SET data = EXCLUDED.data")
    put_doc(doc)
    pg.goto(URL + f'/zarobki?o=prev&g={gid}')
    chk('Zarobki bez rozliczenia: suma z dyżurów (1500 zł × 40% = 600 zł)', money(pg.inner_text('[data-testid=zarobek]')) == 60000, pg.inner_text('[data-testid=zarobek]'))
    chk('Zarobki bez rozliczenia: bez informacji o kwocie z rozliczenia', pg.locator('[data-testid=wg-rozliczenia]').count() == 0)
    doc['inv'] = {gid: {'statement': '642,50'}}; put_doc(doc)
    pg.goto(URL + f'/zarobki?o=prev&g={gid}')
    chk('Zarobki z rozliczeniem: kwota z Kalendarza → Rozliczenia (642,50 zł) zamiast sumy z dyżurów', money(pg.inner_text('[data-testid=zarobek]')) == 64250, pg.inner_text('[data-testid=zarobek]'))
    chk('Zarobki z rozliczeniem: informacja, skąd kwota', pg.locator('[data-testid=wg-rozliczenia]').count() == 1)
    d1, d2 = pm + '-10', pm + '-10'
    pg.goto(URL + f'/zarobki?o=own&od={d1}&do={d2}&g={gid}')
    chk('niepełny miesiąc (1 dzień): nadal z dyżurów (400 zł) – kwoty miesięcznej nie dzielimy na dni', money(pg.inner_text('[data-testid=zarobek]')) == 40000, pg.inner_text('[data-testid=zarobek]'))
    chk('podwójne liczenie wykluczone: miesiąc = kwota z rozliczenia (nie suma + kwota)', money(pg.inner_text('[data-testid=zarobek]')) != 64250 + 60000)

    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('prompt 21.11: pasek bez kwot, uraz, rokowanie, opisy prywatne')
