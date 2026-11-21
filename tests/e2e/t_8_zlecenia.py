# Zlecenia protetyczne (docs/ZLECENIA_PROTETYCZNE.md): moduł na urządzeniu – lista, nowe zlecenie, rodzaje prac, pola zależne,
# kontrola kompletności, statusy, historia zmian, kopiowanie, usuwanie; prywatność (treść nie trafia na serwer).
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(150)
def ch(pg, k, v): pg.click(f'button[data-a="ch"][data-k="{k}"][data-v="{v}"]'); pg.wait_for_timeout(120)
def typ(pg, v):
    if not pg.locator(f'button[data-a="typ"][data-v="{v}"]').is_visible(): pg.click('details[data-sec="typ"] > summary'); pg.wait_for_timeout(100)
    pg.click(f'button[data-a="typ"][data-v="{v}"]'); pg.wait_for_timeout(200)
def wymagane(pg): return pg.evaluate("braki(S.cur).filter(x=>x[0]==='W').map(x=>x[1])")

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz Z', 'zl.8@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    sent = []; pg.on('request', lambda r: sent.append((r.url, r.post_data or '')) if r.method == 'POST' else None)
    r = pg.goto(URL + '/zlecenia'); ready(pg)
    chk('moduł Zlecenia otwiera się (menu: „Zlecenia” aktywne)', r.status == 200 and pg.inner_text('#gbar a.on') == 'Zlecenia')
    chk('pusta lista', 'Nie ma jeszcze zleceń' in pg.inner_text('#main'))

    # ---- nowe zlecenie: korona e.max
    pg.click('button[data-a="nowe"]'); pg.wait_for_timeout(300)
    nr = pg.evaluate("S.cur.nr")
    chk('numer przypadku nadany automatycznie (ZP-RRRR-NNN)', nr.startswith('ZP-') and nr.endswith('-001'), nr)
    chk('bez rodzaju pracy: ostrzeżenie „Wybierz rodzaj pracy”', 'Wybierz rodzaj pracy' in pg.inner_text('#zl-chk'))
    typ(pg, 'kor-emax')
    chk('materiały zależne od rodzaju pracy (korona e.max → e.max)', pg.locator('button[data-a="ch"][data-k="mat"]').count() >= 1 and pg.locator('button[data-k="mat"][data-v="e.max"]').count() == 1)
    chk('kontrola: korona bez materiału → ostrzeżenie', any('Materiał' in x for x in wymagane(pg)))
    pg.fill('#f_ini', 'AB'); pg.fill('#f_zeby', '11, 21'); pg.fill('#f_termin', '2026-12-10'); ch(pg, 'mat', 'e.max'); ch(pg, 'antag', 'skan / wycisk dołączony')
    pg.wait_for_timeout(800)
    chk('kontrola: komplet danych podstawowych → brak wymaganych braków', wymagane(pg) == [], wymagane(pg))
    pg.fill('[data-own="mat"]', 'IPS e.max Press HT'); pg.press('[data-own="mat"]', 'Enter'); pg.wait_for_timeout(200)
    chk('własny materiał wpisany ręcznie (nie blokuje zlecenia)', pg.evaluate("S.cur.a.mat") == 'IPS e.max Press HT')
    ch(pg, 'etapy', 'akceptacja projektu przed produkcją'); ch(pg, 'etapy', 'przymiarka konstrukcji')
    chk('wybór wielu etapów', pg.evaluate("S.cur.a.etapy.length") == 2)
    pg.click('details[data-sec="status"] > summary'); pg.wait_for_timeout(100)
    pg.click('button[data-a="status"][data-v="wysłane"]'); pg.wait_for_timeout(200)
    chk('status „wysłane” + wpis w historii', pg.evaluate("S.cur.status") == 'wysłane' and 'status: wysłane' in pg.inner_text('.zl-hist'))
    pg.click('button[data-a="zapisz"]'); pg.wait_for_timeout(300)

    # ---- zapis na urządzeniu, odczyt po odświeżeniu, prywatność
    pg.goto(URL + '/zlecenia'); ready(pg)
    chk('zlecenie zostaje po odświeżeniu (zapis na urządzeniu)', nr in pg.inner_text('#main') and 'Korona e.max' in pg.inner_text('#main'))
    raw = pg.evaluate("""async()=>{const db=await new Promise((res,rej)=>{const q=indexedDB.open('gabinet-saas@'+G.user.id);q.onsuccess=()=>res(q.result);q.onerror=rej;});
      return await new Promise(res=>{const t=db.transaction(['zlecenia'],'readonly');const r=t.objectStore('zlecenia').getAll();r.onsuccess=()=>res(JSON.stringify(r.result));});}""")
    chk('w bazie przeglądarki treść zaszyfrowana (brak „AB” i „11, 21” jawnym tekstem)', '"AB"' not in raw and '11, 21' not in raw and 'e.max' not in raw)
    leak = [u for u, d in sent if ('AB' in d and 'zeby' in d) or '11, 21' in d or 'IPS e.max' in d]
    chk('na serwer nie trafiła treść zlecenia (inicjały, zęby, materiał)', not leak, leak)
    chk('w bazie serwera brak danych zlecenia', sql("SELECT count(*) FROM app.user_blobs WHERE data::text LIKE '%IPS e.max%'") in ('0', ''))

    # ---- kopiowanie, rodzaje prac, usuwanie
    pg.click(f'.zl-item button[data-a="kopiuj"]'); pg.wait_for_timeout(300)
    chk('kopia zlecenia: nowy numer, te same dane, historia „skopiowano z …”', pg.evaluate("S.cur.nr").endswith('-002') and pg.evaluate("S.cur.a.mat") == 'IPS e.max Press HT'
        and pg.evaluate("S.cur.hist.some(h=>h.co==='skopiowano z '+arguments[0])".replace('arguments[0]', repr(nr))))
    for k, nazwa in [('most-klas', 'Most klasyczny'), ('kor-impl', 'Korona na implancie'), ('aox-4', 'All-on-4'), ('aox-6', 'All-on-6'), ('aox-x', 'All-on-X'),
                     ('rem-calk', 'Proteza całkowita'), ('rem-czesc', 'Proteza częściowa'), ('inne-licowka', 'Licówki'), ('inne-szyna', 'Szyna relaksacyjna / ochronna')]:
        typ(pg, k)
        chk(f'rodzaj pracy: {nazwa} – formularz z materiałami', nazwa in pg.inner_text('h1') and pg.locator('button[data-k="mat"]').count() >= 1)
    # ---- E2: pola zależne od rodzaju pracy + kontrola kompletności (przykłady z promptu, §10)
    def secs(): return pg.evaluate("sekcje(S.cur).map(s=>s.id).join(',')")
    def W(): return ' | '.join(wymagane(pg))
    typ(pg, 'most-klas')
    chk('most: sekcja „filary i przęsła”, bez sekcji implantów', 'most' in secs() and 'impl' not in secs())
    chk('most bez oznaczenia przęseł → ostrzeżenie', 'Przęsła' in W(), W())
    pg.fill('#f_przesla', '15'); pg.fill('#f_filary', '14, 16'); pg.wait_for_timeout(300)
    chk('most z przęsłami i filarami → bez tego ostrzeżenia', 'Przęsła' not in W() and 'filarowe' not in W())
    chk('praca estetyczna bez koloru (i bez skali) → ostrzeżenie', 'Kolor główny' in W() and 'Skala kolorów' in W())
    typ(pg, 'kor-impl')
    chk('korona na implancie bez systemu → ostrzeżenie (system, połączenie, mocowanie)', 'Producent i system implantu' in W() and 'Typ połączenia' in W() and 'Mocowanie' in W(), W())
    typ(pg, 'aox-x')
    chk('All-on-X: sekcja planu + komponenty; brak MUA i pozycji → ostrzeżenie', 'aox' in secs() and 'Multi-unit' in W() and 'Pozycje implantów' in W(), W())
    chk('All-on-X: rejestracja zwarcia wymagana', 'Rejestracja zwarcia' in W())
    typ(pg, 'kor-emax')
    chk('korona: rejestracja zwarcia tylko zalecana (nie wymagana)', 'Rejestracja zwarcia' not in W())
    pg.click('details[data-sec="kolor"] > summary') if not pg.locator('button[data-k="zabStan"]').first.is_visible() else None
    ch(pg, 'zabStan', 'ząb martwy / przebarwiony')
    chk('ząb martwy → kolor kikuta wymagany', 'Kolor kikuta' in W(), W())
    typ(pg, 'rem-czesc'); chk('proteza częściowa: etap i łuk wymagane, klamry zalecane', 'Etap' in W() and 'Łuk' in W() and 'rem' in secs())
    typ(pg, 'inne-szyna'); chk('szyna: łuk i rodzaj wymagane, bez sekcji koloru', 'Rodzaj' in W() and 'kolor' not in secs())
    typ(pg, 'impl-tibase'); chk('Ti-base: bez sekcji koloru, z komponentami implantu', 'kolor' not in secs() and 'impl' in secs())

    pg.click('details[data-sec="typ"] > summary'); pg.wait_for_timeout(100)
    pg.fill('[data-owntyp="1"]', 'Maska dziąsłowa'); pg.press('[data-owntyp="1"]', 'Enter'); pg.wait_for_timeout(300)
    chk('inny rodzaj pracy wpisany ręcznie', 'Maska dziąsłowa' in pg.inner_text('h1'))
    pg.click('button[data-a="usun"]'); pg.click('button[data-a="usun"]'); pg.wait_for_timeout(300)
    chk('usunięcie zlecenia (z potwierdzeniem)', pg.locator('.zl-item').count() == 1)

    # ---- izolacja: inne konto na tym samym komputerze nie widzi zleceń
    c2, p2 = konto(br, 'Lekarz Y', 'zl2.8@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    p2.goto(URL + '/zlecenia'); ready(p2)
    chk('inne konto: nie widzi zleceń pierwszego lekarza', 'Nie ma jeszcze zleceń' in p2.inner_text('#main'))
    c2.close()
    anon = br.new_context(); pa = anon.new_page(); pa.goto(URL + '/zlecenia')
    chk('bez logowania: przekierowanie do logowania', '/logowanie' in pa.url); anon.close()

    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('zlecenia protetyczne: moduł na urządzeniu')
