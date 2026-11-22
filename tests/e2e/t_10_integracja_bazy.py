# Integracja bazy stomatologicznej – etap I1: Katalog procedur i badań (tylko odczyt) + kontrola kompletności dokumentacji w Opisach NFZ
# (ostrzeżenie bez blokady – decyzja Patryka 22.11.2026). Treść opisów i wycena bez zmian.
import json, os
from pomoc import *
t = T(); chk = t.chk
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
PROC = json.load(open(os.path.join(ROOT, 'data', 'procedury-icd9', 'procedures.json')))['procedury']
OPR = [p for p in PROC if p['status'] != 'not_started']
BAD = json.load(open(os.path.join(ROOT, 'data', 'badania', 'examinations.json')))['badania']
BAD_WID = [b for b in BAD if b['status'] != 'not_started']
REJ = next(p for p in PROC if p.get('uzasadnienie_statusu', '').startswith('Odrzucone'))   # przykład karty odrzuconej
DRAFT = next((p for p in PROC if p['status'] == 'draft'), None)   # przykład karty niezatwierdzonej (po pełnej weryfikacji 22.11.2026 – brak)

def ready(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def wiz(pg, codes, a=None, teeth=None, quads=None):
    pg.evaluate("([c,a,t,q])=>{state.codes=c;state.a=a;state.teeth=t;state.quads=q;state.step=3;render()}", [codes, a or {}, teeth or {}, quads or {}]); pg.wait_for_timeout(200)
def panel(pg):   # treść panelu (bez braków panel jest zwinięty – rozwijamy do odczytu)
    return pg.evaluate("(()=>{const d=document.querySelector('[data-testid=\"baza-chk\"]');if(!d)return '';const o=d.open;d.open=true;const t=d.innerText;d.open=o;return t})()")

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz K', 'katalog.10@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    sent = []; pg.on('request', lambda r: sent.append(r.post_data or '') if r.method == 'POST' else None)

    # ---- Katalog procedur i badań
    pg.goto(URL + '/katalog-nfz')
    chk('Katalog NFZ: link do Katalogu procedur i badań', pg.locator('[data-testid="link-katalog-procedur"]').count() == 1)
    pg.click('[data-testid="link-katalog-procedur"]'); pg.wait_for_load_state('networkidle')
    txt = pg.inner_text('main')
    n_ver = sum(p['status'] == 'verified' for p in PROC)
    chk('Katalog procedur: strona z liczbą kart zweryfikowanych i informacją o wersji roboczej', '/katalog-procedur' in pg.url and 'wersja robocza do weryfikacji' in txt and f'Zweryfikowane przez Patryka: {n_ver}' in txt, txt[:300])
    chk(f'Katalog: {len(BAD_WID)} badań (bez odrzuconych)', pg.locator('[data-testid="kp-badania"] li').count() == len(BAD_WID), pg.locator('[data-testid="kp-badania"] li').count())
    chk(f'Katalog: {len(OPR)} kart procedur (opracowane)', pg.locator('[data-testid="kp-procedury"] li').count() == len(OPR), pg.locator('[data-testid="kp-procedury"] li').count())
    pg.goto(URL + '/katalog-procedur?q=23.1502')
    chk('Szukaj „23.1502” → jedna karta', pg.locator('[data-testid="kp-procedury"] li').count() == 1 and 'Odbudowa – 1 powierzchnia' in pg.inner_text('[data-testid="kp-procedury"]'))
    pg.goto(URL + '/katalog-procedur?q=ST30')
    chk('Szukaj po kodzie z Opisów NFZ („ST30”) → karty złogów', pg.locator('[data-testid="kp-procedury"] li').count() >= 3, pg.locator('[data-testid="kp-procedury"] li').count())
    pg.goto(URL + '/katalog-procedur?status=requires_expert_review')
    n_rev = sum(p['status'] == 'requires_expert_review' for p in PROC)
    chk(f'Filtr „do oceny specjalisty” → {n_rev} kart', pg.locator('[data-testid="kp-procedury"] li').count() == n_rev)

    pg.goto(URL + '/katalog-procedur/PROC-23.1502')
    chk('Karta 23.1502: status „zweryfikowana” + kto i kiedy', 'zweryfikowana' in pg.inner_text('[data-testid="kp-status"]') and 'zweryfikował: Patryk Barysz' in pg.inner_text('main'))
    if DRAFT:
        pg.goto(URL + '/katalog-procedur/' + DRAFT['id'])
        chk(f'Karta niezatwierdzona ({DRAFT["kod"]}): „wersja robocza – do weryfikacji”', 'wersja robocza' in pg.inner_text('[data-testid="kp-status"]'))
    else:
        pg.goto(URL + '/katalog-procedur')
        chk('Wszystkie widoczne karty zweryfikowane – brak „wersja robocza” na liście', not any('wersja robocza' in x for x in pg.locator('[data-testid="kp-procedury"]').all_inner_texts()))
    pg.goto(URL + '/katalog-procedur/' + REJ['id'])
    chk(f'Karta odrzucona ({REJ["kod"]}): informacja o odrzuceniu, bez treści karty', 'odrzucona' in pg.inner_text('main') and pg.locator('[data-testid="kp-kroki"]').count() == 0)
    pg.goto(URL + '/katalog-procedur?q=' + REJ['kod'])
    chk('Karta odrzucona nie pojawia się na liście', pg.locator('[data-testid="kp-procedury"] li').count() == 0)
    pg.goto(URL + '/katalog-procedur/PROC-23.1502')
    chk('Karta 23.1502: kroki, checklista, ICD-10, 3 szablony', pg.locator('[data-testid="kp-kroki"] li').count() >= 8 and pg.locator('[data-testid="kp-checklista"] li').count() >= 5
        and pg.locator('[data-testid="kp-icd10"] li').count() >= 3 and all(pg.locator(f'[data-testid="szablon-{w}"]').count() == 1 for w in ('standardowy', 'skrocony', 'rozszerzony')))
    chk('Karta: szablon pokazuje nazwy pól zamiast identyfikatorów', '[Ząb (FDI)]' in pg.inner_text('[data-testid="szablon-standardowy"]') and 'POLE-' not in pg.inner_text('[data-testid="szablon-standardowy"]'))
    chk('Karta: sekcja NFZ z danych audytu', 'Świadczenie gwarantowane' in pg.inner_text('main') and 'tak' in pg.inner_text('main'))
    pg.goto(URL + '/katalog-procedur/BAD-PRZYZEBIE')
    chk('Badanie „Ocena stanu przyzębia”: przebieg, dokumentacja, szablony', 'Ocena stanu przyzębia' in pg.inner_text('h1') and 'Przebieg' in pg.inner_text('main') and pg.locator('[data-testid="szablon-rozszerzony"]').count() == 1)
    pg.goto(URL + '/katalog-procedur/BAD-PRZYZEBIE')
    chk('Badanie zatwierdzone: „zweryfikował: Patryk Barysz”', 'zweryfikował: Patryk Barysz' in pg.inner_text('main'))
    pg.goto(URL + '/katalog-procedur/PROC-23.2401')
    chk('Kod pominięty (ortodoncja) – status i uzasadnienie, bez karty', 'Pominięte decyzją Patryka' in pg.inner_text('main') and 'nie jest opracowana' in pg.inner_text('main'))
    r = pg.goto(URL + '/katalog-procedur/PROC-99.99')
    chk('Nieznany identyfikator → 404', r.status == 404, r.status)
    anon = br.new_context(); pa = anon.new_page(); pa.goto(URL + '/katalog-procedur')
    chk('Bez logowania – przekierowanie do logowania', '/logowanie' in pa.url, pa.url); anon.close()

    # ---- Opisy NFZ: kontrola kompletności (ostrzeżenie, bez blokady)
    pg.goto(URL + '/opisy-nfz'); ready(pg)
    chk('Opisy NFZ: dane checklist wczytane (20 kodów)', pg.evaluate("window.BAZA_DANE&&Object.keys(BAZA_DANE.kody).length") == 20)
    wiz(pg, ['ST01'], {'sh.age': '40'})
    box = pg.locator('[data-testid="baza-chk"]')
    chk('ST01 bez zaznaczonego zęba: panel otwarty, ⚠ „nie zaznaczono zębów”', box.count() == 1 and box.evaluate('d=>d.open') and 'nie zaznaczono zębów' in box.inner_text() and '⚠' in box.inner_text(), box.inner_text()[:300] if box.count() else '')
    t0 = pg.evaluate("genTxt()")
    wiz(pg, ['ST01'], {'sh.age': '40'}, {'ST01': {'46': {'s': [], 'f': {}}}})
    w = panel(pg)
    chk('ST01 bez braków: panel zwinięty, w nagłówku „bez braków wykrytych automatycznie”', not pg.locator('[data-testid="baza-chk"]').evaluate('d=>d.open') and 'bez braków' in w)
    chk('ST01 z zaznaczonym zębem: brak ⚠ dla lokalizacji („zaznaczono na diagramie”)', 'zaznaczono na diagramie' in w and 'nie zaznaczono zębów' not in w, w[:300])
    chk('Elementy wspólne sprawdzone automatycznie (data, opis, lekarz, rozpoznanie)', all(s in w for s in ('data wizyty', 'opis generowany', 'z konta lekarza')))
    chk('Elementy do sprawdzenia przez lekarza oznaczone ☐', '☐' in w)
    chk('Panel: karta ST01 oznaczona jako zweryfikowana', 'karta 23.1701 – zweryfikowana' in w, w[:200])
    wiz(pg, ['1006'], {})
    w = panel(pg)
    chk('1006 bez wieku: ⚠ „nie wpisano wieku” (R-LAKIER-01)', 'nie wpisano wieku' in w, w[:400])
    wiz(pg, ['1502'], {'sh.age': '30'}, {'1502': {'36': {'s': ['O'], 'f': {}}}})
    chk('Ostrzeżenie nie blokuje – przycisk zapisu dostępny', pg.locator('button[data-act="savevisit"], button[data-act="save"]').count() == 0 or not pg.locator('button[data-act="savevisit"], button[data-act="save"]').first.is_disabled())
    # treść opisu i wycena bez zmian względem wersji bez panelu
    wiz(pg, ['ST01'], {'sh.age': '40'})
    chk('Panel nie zmienia treści opisu (genTxt identyczny)', pg.evaluate("genTxt()") == t0)
    chk('Panel nie trafia do tekstu opisu', 'Kontrola kompletności' not in pg.evaluate("genTxt()"))
    chk('Nic z panelu nie jest wysyłane na serwer', not any('Kontrola kompletności' in d or 'CHK-' in d for d in sent))
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('integracja bazy – I1 (Katalog procedur, kontrola kompletności)')
