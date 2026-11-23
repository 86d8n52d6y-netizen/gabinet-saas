# Etap E4b: zakładka „NFZ” (/nfz) – opis z kart procedur NFZ (bez szablonów Opisów NFZ) i wycena pakietów (nfz-pakiety.js).
# Decyzje Patryka 22.11.2026: osobna pozycja w menu, opis wyłącznie z kart, Opisy NFZ nietknięte.
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(150)
def dodaj(pg, q, pid):
    pg.fill('#p_q', q); pg.wait_for_timeout(120); pg.click(f'button[data-add="{pid}"]'); pg.wait_for_timeout(150)
def pole(i, k): return f'[data-i="{i}"][data-k="{k}"]'
W = lambda pg: pg.evaluate("wycena()")

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    an = br.new_context(); pa = an.new_page(); pa.goto(URL + '/nfz')
    chk('bez logowania /nfz → logowanie', '/logowanie' in pa.url)
    chk('silnik pakietów niedostępny bez logowania', pa.goto(URL + '/opisy-nfz/zasoby/nfz-pakiety.js').status == 401)
    ctx, pg = konto(br, 'Lekarz N', 'nfz.14@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    r = pg.goto(URL + '/nfz'); ready(pg)
    chk('strona /nfz otwiera się, w menu aktywne „NFZ” obok „Opisy NFZ”', r.status == 200 and pg.inner_text('#gbar a.on') == 'NFZ' and pg.locator('#gbar a[href="/opisy-nfz"]').count() == 1)
    chk('katalog: 83 karty rozliczane w NFZ (73 gwarantowane + 10 wycenianych w pakietach, m.in. 23.16011–23.16022) – tylko karty, bez szablonów Opisów NFZ',
        pg.evaluate("PROCS.length") == 83 and pg.evaluate("['23.16011','23.16012','23.16021','23.16022'].every(k=>PROCS.some(p=>p.karta===k))") and pg.evaluate("typeof state==='undefined'"))

    # ekstrakcja wielokorzeniowa 46 + znieczulenie przewodowe w karcie
    dodaj(pg, '23.1702', 'karta-23_1702')
    pg.fill(pole(0, 'k_zab'), '46'); pg.press(pole(0, 'k_zab'), 'Tab')
    pg.select_option(pole(0, 'zn'), 'przewodowe wewnątrzustne'); pg.wait_for_timeout(150)
    w = W(pg)
    chk('ekstrakcja + znieczulenie przewodowe → ST02 104 pkt; znieczulenie w pakiecie (0 pkt)', [x['kod'] for x in w['wiersze']] == ['ST02'] and w['suma'] == 104 and w['skladowe'][0]['kod'] == '23.0403', w)
    chk('tabela wyceny i „W pakiecie” na ekranie', 'ST02' in pg.inner_text('[data-testid="nk-tab"]') and '23.0403' in pg.inner_text('[data-testid="nk-sklad"]'))
    chk('Dentocaine i 1,7 ml wpisane samo – widoczne w polach od razu', pg.evaluate("S.items[0].vals.znprep").startswith('Dentocaine') and pg.input_value(pole(0, 'znprep')).startswith('Dentocaine') and pg.input_value(pole(0, 'zndawka')) == '1,7')
    chk('kwota: 104 pkt × 1,84 zł = 191,36 zł', '191,36' in pg.inner_text('[data-testid="nk-zl"]'), pg.inner_text('[data-testid="nk-zl"]'))

    # wypełnienie 1 powierzchni 36
    dodaj(pg, '23.1502', 'karta-23_1502')
    pg.fill(pole(1, 'k_zab'), '36'); pg.press(pole(1, 'k_zab'), 'Tab')
    chk('ST02 + 23.1502 = 104 + 45 = 149 pkt', W(pg)['suma'] == 149, W(pg))
    pg.select_option(pole(1, 'zn'), 'nasiękowe'); pg.wait_for_timeout(120)
    chk('znieczulenie z karty wypełnienia rozliczone osobno (12 pkt), nie w pakiecie ekstrakcji: 161 pkt', W(pg)['suma'] == 161 and [s_['kod'] for s_ in W(pg)['skladowe']] == ['23.0403'], W(pg))
    chk('wiek tylko w nagłówku – bez pola „Wiek pacjenta” w karcie', pg.locator('[data-k="dok_wiek"]').count() == 0)
    pg.select_option(pole(1, 'zn'), 'nie stosowano'); pg.wait_for_timeout(120)
    pg.fill('#v_wiek', '10'); pg.dispatch_event('#v_wiek', 'change'); ready(pg)
    chk('wiek 10 lat → ×1,5: 223,5 pkt', W(pg)['suma'] == 223.5, W(pg))
    chk('wiek ustawia wariant informacji i zgody (poniżej 16 lat)', pg.evaluate("S.items.every(it=>it.vals.dok_wiek==='poniżej 16 lat')"))
    pg.fill('#v_wiek', '40'); pg.dispatch_event('#v_wiek', 'change'); ready(pg)

    # RTG – zał. 1b, niezweryfikowane: widoczne, nie wliczone
    dodaj(pg, '23.0301', 'karta-23_0301')
    w = W(pg)
    chk('RTG (zał. 1b, zakres do potwierdzenia) – nie wliczone do sumy, widoczne na liście', w['suma'] == 149 and any(n['kod'] == '23.0301' for n in w['nieliczone']) and '23.0301' in pg.inner_text('[data-testid="nk-nie"]'))
    pg.click('button[data-a="rm"][data-i="2"]'); pg.wait_for_timeout(150)

    # opis w zdaniach z kart + blok dokumentacyjny
    for i in (0, 1):
        pg.select_option(pole(i, 'dok_inf'), 'krótka'); pg.select_option(pole(i, 'dok_zg'), 'pisemna' if i == 0 else 'ustna'); pg.wait_for_timeout(80)
    txt = pg.evaluate("visitText()")
    chk('Opis: „Wykonano: …” z obu kart i zębów', txt.startswith('Wykonano: ') and 'ząb 46' in txt.split('\n')[0] and 'ząb 36' in txt.split('\n')[0], txt[:200])
    chk('Opis z kart: ekstrakcja i znieczulenie z dawką w zdaniach', 'Ząb 46' in txt and 'Znieczulenie przewodowe wewnątrzustne: Dentocaine' in txt and '1,7 ml' in txt, txt)
    chk('Opis: zgoda pisemna (ekstrakcja) i ustna (wypełnienie), informacja raz', 'pisemną zgodę na zabieg' in txt and 'ustną zgodę na zabieg' in txt and txt.count('Pacjenta poinformowano') == 1, txt)
    chk('Opis kończy się listą świadczeń NFZ do rozliczenia', txt.rstrip().endswith('Świadczenia NFZ: ST02; 23.1502.'), txt[-80:])
    chk('Opis bez tekstów szablonów Opisów NFZ (np. „INSTRUKTAŻ”, „PROTOKÓŁ”)', 'INSTRUKTAŻ' not in txt and 'PROTOKÓŁ' not in txt)

    # błąd: pakiet bez znieczulenia z listy ST1
    pg.select_option(pole(0, 'zn'), 'nie stosowano'); pg.wait_for_timeout(150)
    chk('ekstrakcja bez znieczulenia z ST1 → błąd „NFZ nie zapłaci”', any('ST02 wymaga procedury z listy ST1' in e for e in W(pg)['bledy']) and pg.locator('[data-testid="nk-err"]').count() >= 1)

    # higienizacja < 18: badanie + 3 × ½ łuku
    pg.click('button[data-a="new"]'); pg.click('button[data-a="new"]'); pg.wait_for_timeout(100)
    pg.fill('#v_wiek', '12'); pg.dispatch_event('#v_wiek', 'change'); ready(pg)
    dodaj(pg, '23.0101', 'karta-23_0101'); dodaj(pg, '23.16011', 'karta-23_16011')
    pg.fill('[data-n="1"]', '3'); pg.dispatch_event('[data-n="1"]', 'input'); pg.wait_for_timeout(100)
    w = W(pg)
    chk('badanie + 3 × ½ łuku (12 lat) → 1× ST30D + 2× ST30E = 114 pkt, bez ×1,5', [x['kod'] for x in w['wiersze']] == ['ST30D', 'ST30E'] and w['suma'] == 114, w)
    chk('karta wieloznaczna: wybór pakietu (badanie: ST33 / ST33A)', pg.locator('[data-war="0"]').count() == 1)

    # podpowiedzi: 3 najczęstsze z możliwością własnej wartości
    pg.goto(URL + '/nfz'); ready(pg); dodaj(pg, '23.1502', 'karta-23_1502')
    q = pg.evaluate("[...document.querySelectorAll('[data-a=\"qset\"][data-k=\"k_rozpoznanie\"]')].map(b=>b.dataset.v)")
    chk('rozpoznanie: do 3 podpowiedzi ICD-10 z karty', 0 < len(q) <= 3, q)
    pg.fill(pole(0, 'mat'), 'Mój materiał'); pg.dispatch_event(pole(0, 'mat'), 'input')
    chk('własna wartość wpisana ręcznie', pg.evaluate("S.items[0].vals.mat") == 'Mój materiał')

    # ---- E4c: zapis, Zarobki, historia, rozdzielenie od Opisów NFZ, duplikat, usunięcie
    pg.goto(URL + '/nfz'); ready(pg)
    pg.fill('#v_wiek', '40'); pg.dispatch_event('#v_wiek', 'change'); ready(pg)
    dodaj(pg, '23.1702', 'karta-23_1702'); pg.fill(pole(0, 'k_zab'), '46'); pg.press(pole(0, 'k_zab'), 'Tab')
    pg.select_option(pole(0, 'zn'), 'przewodowe wewnątrzustne'); pg.fill(pole(0, 'k_rozpoznanie'), 'K04.1'); pg.press(pole(0, 'k_rozpoznanie'), 'Tab')
    pg.select_option(pole(0, 'dok_inf'), 'krótka'); pg.select_option(pole(0, 'dok_zg'), 'pisemna'); pg.wait_for_timeout(100)
    txt = pg.evaluate("visitText()")
    pg.click('#b_save'); pg.wait_for_function("S.id&&H.size===1"); pg.wait_for_timeout(600)
    vid = pg.evaluate("S.id")
    chk('zapis: identyfikator z przedrostkiem „k-”, przycisk „Zapisano ✓”', vid.startswith('k-') and 'Zapisano' in pg.inner_text('#b_save'))
    chk('Zarobki: 104 pkt → 191,36 zł (lekarz 40%: 76,54 zł) w chmurze', sql(f"SELECT e.points||'|'||e.value_gr||'|'||e.doctor_pay_gr FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id=e.description_id WHERE s.client_key='{vid}' AND e.source='nfz_points'") == '104.00|19136|7654')
    dump = sql(f"SELECT row_to_json(s)::text FROM app.saved_descriptions s WHERE client_key='{vid}'")
    chk('w chmurze BRAK treści, rozpoznania, zgody i wieku', dump and 'K04.1' not in dump and 'zgod' not in dump and 'Dentocaine' not in dump and '"wiek"' not in dump and '"body"' not in dump, dump[:200])
    r3 = pg.goto(URL + '/opisy-nfz'); pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000)
    chk('Opisy NFZ NIE widzą wizyty z zakładki NFZ (osobne listy)', vid not in pg.evaluate("JSON.stringify(window.__GABINET.visits)"))
    pg.goto(URL + '/nfz'); ready(pg)
    chk('historia po ponownym otwarciu strony: wizyta na liście', pg.locator(f'[data-hid="{vid}"]').count() == 1)
    pg.click(f'button[data-a="hopen"][data-id="{vid}"]'); pg.wait_for_timeout(300)
    chk('otwarcie z historii odtwarza opis co do znaku', pg.evaluate("visitText()") == txt)
    # wizyta w Opisach NFZ tego samego dnia z ST02 → ostrzeżenie o duplikacie
    pg.evaluate("(d)=>G._post('/api/nfz/wizyty',{put:[{id:'stara1',v:2,no:1,date:d,created:new Date().toISOString(),at:new Date().toISOString(),src:'gen',codes:['ST02'],pts:104,price:1.84,pct:40,revH:0,revRate:350,ex:[],min:null,miss:0,gab:''}]})", pg.evaluate("S.date"))
    pg.goto(URL + '/nfz'); ready(pg); dodaj(pg, '23.1702', 'karta-23_1702'); pg.wait_for_timeout(150)
    chk('ostrzeżenie: ta sama wizyta w Opisach NFZ (Zarobki policzyłyby obie)', pg.locator('[data-testid="nk-dup"]').count() == 1)
    chk('lista Opisów NFZ nadal z ich wizytą „stara1” (bez zmian)', sql("SELECT count(*) FROM app.saved_descriptions WHERE client_key='stara1' AND deleted_at IS NULL") == '1')
    pg.click(f'button[data-a="hdel"][data-id="{vid}"]'); pg.click(f'button[data-a="hdel"][data-id="{vid}"]'); pg.wait_for_timeout(600)
    chk('usunięcie: znika z historii i z Zarobków', pg.locator(f'[data-hid="{vid}"]').count() == 0 and sql(f"SELECT count(*) FROM app.earnings_entries e JOIN app.saved_descriptions s ON s.id=e.description_id WHERE s.client_key='{vid}' AND e.deleted_at IS NULL") == '0')

    # Opisy NFZ – nadal działają (stary generator)
    r2 = pg.goto(URL + '/opisy-nfz'); pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000)
    chk('Opisy NFZ otwierają się jak dotąd (generator bez zmian)', r2.status == 200 and pg.evaluate("typeof genTxt==='function'&&PTS.ST01===93"))
    chk('Brak błędów JavaScript', not errs, errs)
    br.close()
t.done('zakładka NFZ – opis i wycena z kart (E4b)')
