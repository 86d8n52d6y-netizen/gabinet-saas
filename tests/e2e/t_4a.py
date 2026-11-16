# Etap 4a: gabinety, ustawienia rozliczeń NFZ, katalog NFZ, własne kody, wycena – w przeglądarce.
import json, os, random
from pomoc import *
t = T(); chk = t.chk
FX = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'nfz_stara_wersja.json')))

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    errs = []
    ctx, pg = konto(br, 'Lekarz A', 'a.4a@example.com', 'zielony-kubek-na-biurku')
    pg.on('pageerror', lambda e: errs.append(str(e)))
    chk('menu: Katalog NFZ, Gabinety, Ustawienia', all(pg.get_by_role('link', name=n).count() for n in ['Katalog NFZ', 'Gabinety', 'Ustawienia']))

    # ---- gabinety
    pg.goto(URL + '/gabinety')
    chk('brak gabinetów → formularz od razu', 'Nie masz jeszcze gabinetów' in pg.content() and pg.locator('#name').count() == 1)
    submit(pg, 'Dodaj gabinet'); chk('walidacja: nazwa wymagana', 'nazwę gabinetu' in msg(pg) or pg.locator('#name:invalid').count() == 1)
    fill(pg, name='Happy Smile', short='hs', address='Gdańsk, ul. Testowa 1', pct='30')
    pg.select_option('#model', 'hourly'); submit(pg, 'Dodaj gabinet')
    chk('błąd walidacji nie czyści wpisanych pól', 'stawkę za godzinę' in msg(pg) and pg.input_value('#name') == 'Happy Smile' and pg.input_value('#address') == 'Gdańsk, ul. Testowa 1', (msg(pg), pg.input_value('#name')))
    pg.select_option('#model', 'pct_lab'); submit(pg, 'Dodaj gabinet'); chk('dodano gabinet', 'Dodano gabinet' in msg(pg) and 'ok=dodano' in pg.url, msg(pg))
    pg.goto(URL + '/gabinety?nowy=1'); fill(pg, name='Klinika B', pct='')
    pg.select_option('#model', 'hourly'); submit(pg, 'Dodaj gabinet')
    chk('stawka godzinowa wymagana dla modelu godzinowego', 'stawkę za godzinę' in msg(pg), msg(pg))
    fill(pg, hourly='150,50'); submit(pg, 'Dodaj gabinet'); chk('dodano gabinet godzinowy', 'Dodano gabinet' in msg(pg), msg(pg))
    row = sql("SELECT short||'|'||color||'|'||model||'|'||pct||'|'||coalesce(lab_share::text,'-')||'|'||(extra->>'address') FROM app.clinics WHERE name='Happy Smile'")
    chk('zapis gabinetu: skrót wielkimi literami, kolor, model, %, adres', row == 'HS|1|pct_lab|30.00|-|Gdańsk, ul. Testowa 1', row)
    chk('kwota w groszach (150,50 zł → 15050)', sql("SELECT hourly_gr FROM app.clinics WHERE name='Klinika B'") == '15050')
    pg.goto(URL + '/gabinety'); chk('lista: 2 gabinety z modelem rozliczenia', pg.locator('tbody tr').count() == 2 and '150,50 zł/h' in pg.content().replace('\xa0', ' '))
    cid = sql("SELECT id FROM app.clinics WHERE name='Happy Smile'")
    # konflikt: ta sama edycja w dwóch kartach
    p1 = ctx.new_page(); p1.goto(URL + f'/gabinety?id={cid}'); p2 = ctx.new_page(); p2.goto(URL + f'/gabinety?id={cid}')
    p1.fill('#pct', '35'); submit(p1, 'Zapisz zmiany'); chk('edycja zapisana (karta 1)', 'Zapisano zmiany' in msg(p1) and 'ok=zmieniono' in p1.url, msg(p1))
    p2.fill('#pct', '25'); submit(p2, 'Zapisz zmiany'); chk('konflikt: karta 2 na starej wersji nie nadpisuje', 'innym urządzeniu' in msg(p2), msg(p2))
    chk('w bazie wartość z karty 1 (35%), wersja 2', sql(f"SELECT pct||'|'||version FROM app.clinics WHERE id='{cid}'") == '35.00|2')
    p1.close(); p2.close()
    pg.goto(URL + '/gabinety'); pg.locator('tr', has_text='Klinika B').get_by_role('button', name='Wyłącz').click(); pg.wait_for_load_state('networkidle')
    chk('wyłączenie gabinetu (zostaje na liście jako nieaktywny)', 'nieaktywny' in pg.content() and sql("SELECT active FROM app.clinics WHERE name='Klinika B'") == 'f')

    # ---- izolacja: B nie zmieni gabinetu A (podmiana id)
    ctxb, pb = konto(br, 'Lekarz B', 'b.4a@example.com', 'niebieska-lampa-w-oknie')
    pb.goto(URL + '/gabinety'); chk('B nie widzi gabinetów A', 'Happy Smile' not in pb.content())
    pb.evaluate(f"""()=>{{const f=document.querySelector('form'); for (const [n,v] of [['id','{cid}'],['version','2']]) {{const i=document.createElement('input'); i.type='hidden'; i.name=n; i.value=v; f.appendChild(i);}}}}""")
    fill(pb, name='Przejęty', pct='99'); submit(pb, 'Dodaj gabinet')
    chk('B nie zmieni gabinetu A po podmianie identyfikatora (RLS)', sql(f"SELECT name||'|'||pct FROM app.clinics WHERE id='{cid}'") == 'Happy Smile|35.00', sql(f"SELECT name FROM app.clinics WHERE id='{cid}'"))
    pb.goto(URL + f'/gabinety?id={cid}'); chk('B nie otworzy edycji gabinetu A', 'Happy Smile' not in pb.content())

    # ---- ustawienia
    pg.goto(URL + '/ustawienia')
    chk('ustawienia domyślne: 1,84 zł / 350 zł / 40% / pełna wartość', pg.input_value('#price') == '1,84' and pg.input_value('#rev') == '350' and pg.input_value('#pct') == '40' and pg.input_value('#basis') == 'full')
    chk('przykład: 100 pkt = 184,00 zł', '184,00 zł' in pg.content().replace('\xa0', ' '))
    fill(pg, price='abc'); submit(pg, 'Zapisz ustawienia'); chk('błędna stawka odrzucona', 'Stawka za punkt' in msg(pg), msg(pg))
    pg.goto(URL + '/ustawienia'); fill(pg, price='1,9', rev='400'); pg.select_option('#pct', '35'); pg.select_option('#basis', 'share')
    submit(pg, 'Zapisz ustawienia'); chk('ustawienia zapisane', 'Zapisano' in msg(pg), msg(pg))
    chk('w bazie: 1.9 / 400 / 35 / share', sql("SELECT settings->'nfz' FROM app.user_settings u JOIN app.profiles p ON p.id=u.user_id WHERE p.email='a.4a@example.com'").replace(' ', '') == '{"pct":35,"rev":400,"basis":"share","price":1.9}')
    pa = ctx.new_page(); pa.goto(URL + '/ustawienia'); pb2 = ctx.new_page(); pb2.goto(URL + '/ustawienia')
    pa.fill('#price', '1,84'); submit(pa, 'Zapisz ustawienia'); pb2.fill('#price', '2'); submit(pb2, 'Zapisz ustawienia')
    chk('ustawienia: konflikt dwóch kart wykryty', 'Zapisano' in msg(pa) and 'innym urządzeniu' in msg(pb2), (msg(pa), msg(pb2)))
    pa.close(); pb2.close()

    # ---- katalog
    pg.goto(URL + '/katalog-nfz')
    kat = pg.locator('section', has_text='Kody z zarządzeń').locator('tbody tr')
    chk('katalog: 23 pozycje', kat.count() == 23, kat.count())
    chk('źródła: 95/2026/DSOZ i 44/2025/DSOZ', '95/2026/DSOZ' in pg.content() and '44/2025/DSOZ' in pg.content())
    chk('ST30E: bez ×1,5, bez ×0,8, min. 5 min', 'bez ×1,5 · bez ×0,8 · min. 5 min' in kat.filter(has_text='ST30E').inner_text())
    fill(pg, code='ST01', name='Moja ekstrakcja', points='10'); submit(pg, 'Dodaj własny kod')
    chk('własny kod: oficjalny kod odrzucony', 'oficjalnym katalogu' in msg(pg), msg(pg))
    fill(pg, code='x 99', name='Świadczenie testowe', points='12,5'); submit(pg, 'Dodaj własny kod')
    chk('własny kod dodany (X99, 12,5 pkt)', 'Dodano własny kod X99' in msg(pg), msg(pg))
    pg.goto(URL + '/katalog-nfz'); fill(pg, code='X99', name='Duplikat', points='1'); submit(pg, 'Dodaj własny kod')
    chk('własny kod: duplikat odrzucony', 'Masz już własny kod X99' in msg(pg), msg(pg))
    chk('oznaczenie „niesprawdzane przez zasady NFZ”', 'niesprawdzane przez zasady NFZ' in pg.content())
    chk('B nie widzi własnych kodów A', (pb.goto(URL + '/katalog-nfz') or True) and 'X99' not in pb.content())

    # ---- wycena = stara aplikacja (przypadki ze wzorca) – przez interfejs
    pg.goto(URL + '/katalog-nfz')
    random.seed(7); probki = random.sample([k for k in FX['punkty'] if k['age'] is not None], 6)
    for i, k in enumerate(probki):
        pg.goto(URL + '/katalog-nfz')
        pg.fill('[aria-label="Wiek pacjenta"]', str(k['age']))
        if k['preg']: pg.check('text=ciąża / połóg')
        for c in k['codes']:
            pg.check(f'[aria-label="Kod {c}"]'); pg.fill(f'[aria-label="Ilość {c}"]', str(k['qty'][c]))
        for a, n in k['an'].items():
            if n: pg.fill(f'[aria-label="Liczba {a}"]', str(n))
        shown = pg.locator('[data-testid=wycena]').inner_text() if pg.locator('[data-testid=wycena]').count() else ''
        exp = (('%.2f' % k['old']['total']).rstrip('0').rstrip('.')).replace('.', ',') + ' pkt'
        chk(f'wycena w interfejsie = stara aplikacja (przypadek {i+1}: {"+".join(k["codes"])}, wiek {k["age"]})', shown.startswith(exp), (shown, exp))
    pg.goto(URL + '/katalog-nfz'); pg.check('[aria-label="Kod ST01"]'); pg.fill('[aria-label="Ilość X99"]', '2')
    w = pg.locator('[data-testid=wycena]').inner_text().replace('\xa0', ' ')
    # ST01 93 pkt + X99 2×12,5 = 118 pkt; stawka 1,84 zł (zmieniona w karcie 1) → 217,12 zł; udział 35% → 75,99 zł
    chk('wycena z własnym kodem i stawkami użytkownika: 118 pkt · 217,12 zł · 35%: 75,99 zł', w == '118 pkt · 217,12 zł · lekarz 35%: 75,99 zł', w)
    pg.locator('section[aria-labelledby=wl]').locator('tr', has_text='Świadczenie testowe').get_by_role('button', name='Usuń').click()
    pg.locator('section[aria-labelledby=wl]').locator('tr', has_text='Świadczenie testowe').wait_for(state='detached', timeout=5000)
    chk('usunięcie własnego kodu (miękkie – zostaje w bazie)', sql("SELECT deleted_at IS NOT NULL FROM app.procedures WHERE nfz_code='X99'") == 't')

    # ---- licencja: bez dostępu moduły zablokowane
    sql("DELETE FROM app.subscriptions WHERE user_id=(SELECT id FROM app.profiles WHERE email='b.4a@example.com')")
    for path in ['/gabinety', '/ustawienia', '/katalog-nfz']:
        pb.goto(URL + path); chk(f'bez licencji {path} → informacja na koncie', 'dostep=brak' in pb.url and 'wymaga aktywnej licencji' in pb.content(), pb.url)
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('etap 4a: gabinety, ustawienia, katalog NFZ')
