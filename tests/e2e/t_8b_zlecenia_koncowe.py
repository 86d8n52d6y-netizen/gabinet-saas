# Zlecenia protetyczne – testy końcowe (etap E8, HANDOFF §10): dla każdego rodzaju pracy z promptu pełne zlecenie
# (wszystkie pola wymagane wypełnione przez formularz) → brak braków, wydruk zawiera dane, synchronizacja z kontem, widok telefonu.
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(150)
def synced(pg): pg.wait_for_function("!localStorage.getItem('gabinet-saas.zlecenia.niewyslane@'+G.user.id)", timeout=15000); pg.wait_for_timeout(100)
def typ(pg, v):
    if not pg.locator(f'button[data-a="typ"][data-v="{v}"]').is_visible(): pg.click('details[data-sec="typ"] > summary'); pg.wait_for_timeout(100)
    pg.click(f'button[data-a="typ"][data-v="{v}"]'); pg.wait_for_timeout(200)
def wymagane(pg): return pg.evaluate("braki(S.cur).filter(x=>x[0]==='W').map(x=>x[1])")
PRZYKLAD = {'nr': None, 'ini': 'KW', 'termin': '2026-12-15', 'implSys': 'Straumann BLT RC', 'aoxMua': '15: 30° 3 mm; 12: 0° 2 mm; 22: 0° 2 mm; 25: 30° 3 mm',
            'kikut': 'ND3', 'kolor': 'A2', 'zeby': '11', 'filary': '14, 16', 'przesla': '15', 'aoxPoz': '15, 12, 22, 25'}

def wypelnij(pg):
    """Wypełnia przez formularz każde pole wymagane (chips: pierwsza opcja, tekst: przykład) – aż do braku braków."""
    for _ in range(4):
        pola = pg.evaluate("""(()=>{const out=[];for(const s of sekcje(S.cur))for(const f of s.pola){if(f.st!=='W')continue;const v=val(S.cur,f.k);
            if(v===undefined||v===''||(Array.isArray(v)&&!v.length))out.push({k:f.k,t:f.t,o:(f.opts||[])[0]||'',sec:s.id})}return out})()""")
        if not pola: return
        for f in pola:
            det = f'details[data-sec="{f["sec"]}"]'
            if pg.locator(det).count() and not pg.locator(det).first.evaluate('d=>d.open'): pg.click(det + ' > summary'); pg.wait_for_timeout(80)
            if f['t'] in ('chips1', 'chipsN'):
                pg.click(f'button[data-a="ch"][data-k="{f["k"]}"][data-v="{f["o"]}"]')
            else:
                pg.fill(f'#f_{f["k"]}', PRZYKLAD.get(f['k'], 'test ' + f['k']))
            pg.wait_for_timeout(120)

PRACE = [('kor-emax', 'Korona e.max', 'A'), ('kor-cyrk-mono', 'Korona cyrkonowa monolityczna', 'A'), ('most-klas', 'Most klasyczny', 'B'),
         ('kor-impl', 'Korona na implancie', 'A'), ('most-impl', 'Most na implantach', 'B'), ('aox-4', 'All-on-4', 'D'), ('aox-6', 'All-on-6', 'D'),
         ('aox-x', 'All-on-X', 'D'), ('rem-calk', 'Proteza całkowita', 'E'), ('rem-czesc', 'Proteza częściowa', 'E'), ('rem-szkiel', 'Proteza szkieletowa', 'E'),
         ('inne-licowka', 'Licówki', 'F'), ('inne-szyna', 'Szyna relaksacyjna / ochronna', 'F')]

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz E8', 'zl.8b@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/zlecenia'); ready(pg)
    pg.evaluate("window.print=()=>{window.__druk=document.querySelector('#druk').innerHTML}")
    ids = {}
    for k, nazwa, grp in PRACE:
        pg.click('button[data-a="nowe"]') if pg.locator('button[data-a="nowe"]').count() else (pg.click('button[data-a="lista"]'), pg.wait_for_timeout(200), pg.click('button[data-a="nowe"]'))
        pg.wait_for_timeout(250); typ(pg, k)
        # zęby ze schematu: role zależne od rodzaju pracy
        roles = {'B': [('filar', 14), ('filar', 16), ('przęsło', 15)], 'D': [('implant', 15), ('implant', 12), ('implant', 22), ('implant', 25)],
                 'E': [('brak', 46), ('brak', 36)]}.get(grp, [('korona', 11)])
        if k == 'most-impl': roles = [('implant', 14), ('implant', 16), ('przęsło', 15)]
        for r, n in roles:
            pg.click(f'button[data-a="rola"][data-v="{r}"]'); pg.click(f'[data-testid="zab-{n}"]'); pg.wait_for_timeout(100)
        wypelnij(pg); pg.wait_for_timeout(300)
        w = wymagane(pg)
        chk(f'{nazwa}: komplet wymaganych pól przez formularz', w == [], w)
        chk(f'{nazwa}: komunikat „Wszystkie wymagane informacje są uzupełnione”', 'Wszystkie wymagane' in pg.inner_text('#zl-chk'))
        pg.click('[data-testid="drukuj"]'); pg.wait_for_timeout(300)
        d = pg.evaluate("window.__druk||''"); a = pg.evaluate("S.cur.a")
        brak = [v for kk, v in a.items() if isinstance(v, str) and v and kk not in ('fotoDruk',) and v not in d.replace('&amp;', '&')]
        chk(f'{nazwa}: wydruk zawiera rodzaj pracy, schemat i wszystkie wpisane wartości, bez listy braków', nazwa in d and 'Schemat zębów' in d and not brak and 'niekompletne' not in d, brak)
        ids[k] = pg.evaluate("S.cur.id")
        pg.click('button[data-a="zapisz"]'); pg.wait_for_timeout(200)
    synced(pg)
    chk('wszystkie zlecenia zapisane na koncie', sql("SELECT count(*) FROM app.prosthetic_orders WHERE NOT deleted") == str(len(PRACE)))
    chk('na koncie zęby ze schematu (most: 14 i 16 filary, 15 przęsło)', sql(f"SELECT data->'a'->>'filary' || '|' || (data->'a'->>'przesla') FROM app.prosthetic_orders WHERE id='{ids['most-klas']}'") == '14, 16|15')

    # responsywność: telefon i tablet – bez przewijania strony w poziomie, przyciski zębów klikalne
    for wdt, nazwa in [(390, 'telefon'), (768, 'tablet')]:
        pg.set_viewport_size({'width': wdt, 'height': 900}); pg.click('button[data-a="lista"]'); pg.wait_for_timeout(200)
        chk(f'{nazwa} ({wdt} px): lista bez przewijania w poziomie', pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
        pg.click(f'button[data-a="otworz"][data-id="{ids["aox-x"]}"]'); pg.wait_for_timeout(300)
        chk(f'{nazwa} ({wdt} px): zlecenie bez przewijania w poziomie', pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"), pg.evaluate("document.documentElement.scrollWidth"))
        pg.click('[data-testid="zab-48"]', trial=True)
        chk(f'{nazwa} ({wdt} px): skrajny ząb (48) da się kliknąć', True)
    pg.set_viewport_size({'width': 1280, 'height': 900})

    # druk na A4: tylko wydruk, bez menu
    pg.click('[data-testid="drukuj"]'); pg.wait_for_timeout(300)
    pg.emulate_media(media='print'); pg.evaluate("document.querySelector('#druk').innerHTML=window.__druk")
    pdf = pg.pdf(format='A4')
    chk('PDF (A4) powstaje i ma treść', len(pdf) > 5000, len(pdf))
    chk('w druku nie ma menu ani formularza', not pg.is_visible('#gbar') and not pg.is_visible('#main'))
    pg.emulate_media(media='screen')

    # izolacja: inne konto nie widzi zleceń ani na urządzeniu, ani przez API
    c2, p2 = konto(br, 'Lekarz Q', 'zl.8c@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    p2.goto(URL + '/zlecenia'); ready(p2)
    chk('inne konto: pusta lista zleceń', 'Nie ma jeszcze zleceń' in p2.inner_text('#main'))
    ch = p2.evaluate("""async()=>{const r=await fetch('/api/zlecenia',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({known:{}})});return (await r.json()).changed}""")
    chk('inne konto: API nie zwraca cudzych zleceń', ch == {}, ch)
    k1 = list(ids.values())[0]
    r = p2.evaluate(f"""async()=>{{const r=await fetch('/api/zlecenia',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{put:[],del:[{{id:'{k1}',base:1}}]}})}});return r.status}}""")
    chk('inne konto: próba usunięcia cudzego zlecenia nic nie zmienia', sql(f"SELECT deleted::text FROM app.prosthetic_orders WHERE id='{k1}'") == 'false', r)
    c2.close()
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('zlecenia protetyczne – testy końcowe (E8)')
