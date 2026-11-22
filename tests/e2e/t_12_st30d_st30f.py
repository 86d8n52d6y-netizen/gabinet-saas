# ST30D i ST30F w Opisach NFZ (decyzja Patryka 22.11.2026: 1A, 2A) – zał. 1c/1d Zarządzenia 95/2026/DSOZ,
# komunikaty Centrali NFZ z 23.09.2026 i 9.11.2026. ST30G zgodnie z nazwą – bez instruktażu.
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def wiz(pg, codes, age='10', quads=None):
    pg.evaluate("([c,a,q])=>{state.codes=c;state.a=Object.assign({},state.a,{'sh.age':a});state.quads=q;state.teeth={};state.step=3;render()}", [codes, age, quads or {}]); pg.wait_for_timeout(150)
    return pg.evaluate("(()=>{const r=nfzIssues();return {err:r.err.map(e=>e.msg),warn:r.warn.filter(w=>!w.info&&!w.soft).map(w=>w.msg),info:r.warn.filter(w=>w.info).map(w=>w.msg),soft:r.warn.filter(w=>w.soft).map(w=>w.msg)}})()")
has = lambda L, s: any(s in x for x in L)

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz H', 'higiena.12@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/opisy-nfz'); ready(pg)

    chk('Lista kodów: ST30D i ST30F w „Profilaktyka i higienizacja”', pg.evaluate("GROUPS.find(g=>g[0]==='Profilaktyka i higienizacja')[1].includes('ST30D')&&GROUPS.find(g=>g[0]==='Profilaktyka i higienizacja')[1].includes('ST30F')") if pg.evaluate("typeof GROUPS!=='undefined'") else pg.evaluate("!!D.ST30D&&!!D.ST30F"))
    chk('Punkty: ST30D 66, ST30F 138 (zał. 1c, 95/2026/DSOZ)', pg.evaluate("PTS.ST30D===66&&PTS.ST30F===138"))
    chk('Bez ×1,5 dla ST30D i ST30F u dziecka', pg.evaluate("PTS_NO15.includes('ST30D')&&PTS_NO15.includes('ST30F')"))

    # ST30D – tekst z badaniem i instruktażem, 1 ćwiartka
    r = wiz(pg, ['ST30D'], '10', {'ST30D': ['1']})
    txt = pg.evaluate("genTxt()")
    chk('ST30D: tytuł „Z INSTRUKTAŻEM … ½ ŁUKU (ST30D)” i sekcja instruktażu', '(ST30D)' in txt and 'Z INSTRUKTAŻEM HIGIENY ½ ŁUKU' in txt and 'INSTRUKTAŻ HIGIENY JAMY USTNEJ' in txt, txt[:300])
    chk('ST30D: badanie lekarskie z instruktażem w opisie', 'Badanie lekarskie stomatologiczne, które obejmuje również instruktaż' in txt)
    chk('ST30D: brak błędów przy samym ST30D', not r['err'], r)
    chk('ST30D: limit 1× w roku – informacja o ST33 / ST30F', has(r['soft'], 'ST33 lub ST30F'), r['soft'])

    # 1× ST30D + ST30E na pozostałych ćwiartkach – NFZ zapłaci
    r = wiz(pg, ['ST30D', 'ST30E'], '10', {'ST30D': ['1'], 'ST30E': ['2', '3']})
    chk('ST30D + 2× ST30E: bez błędów (zalecenie NFZ)', not r['err'], r['err'])
    pkt = pg.evaluate("(()=>{const x=ptsRows?ptsRows():null;return x})()") if pg.evaluate("typeof ptsRows==='function'") else None
    r = wiz(pg, ['ST30D', 'ST30E'], '10', {'ST30D': ['1'], 'ST30E': ['2', '3', '4', '1']})
    chk('ST30D + 4× ST30E: ostrzeżenie „maks. 3 × ST30E”', has(r['warn'], 'maks. za 3 × ST30E'), r['warn'])
    r = wiz(pg, ['ST30D'], '10', {'ST30D': ['1', '2']})
    chk('ST30D na 2 ćwiartkach: ostrzeżenie „pozostałe ćwiartki w ST30E”', has(r['warn'], 'pozostałe ćwiartki zaznacz w ST30E'), r['warn'])

    # dosumować wyłącznie
    r = wiz(pg, ['ST30D', 'ST33'], '10', {'ST30D': ['1']})
    chk('ST30D + ST33: błąd – NFZ nie zapłaci', has(r['err'], 'ST33'), r['err'])
    r = wiz(pg, ['ST30D', 'ST01'], '10', {'ST30D': ['1']})
    chk('ST30D + ST01: błąd „dosumować wyłącznie ST30E i 1101”', has(r['err'], 'dosumować wyłącznie ST30E i 1101'), r['err'])
    r = wiz(pg, ['ST30D', '1101'], '10', {'ST30D': ['1']})
    chk('ST30D + 1101: bez błędów', not r['err'], r['err'])
    r = wiz(pg, ['ST30F', 'ST30E'], '10', {'ST30E': ['1']})
    chk('ST30F + ST30E: błąd (ST30F tylko z 1101)', bool(r['err']), r)
    r = wiz(pg, ['ST30F', '1101'], '10')
    chk('ST30F + 1101: bez błędów', not r['err'], r['err'])
    txt = pg.evaluate("genTxt()")
    chk('ST30F: tytuł „Z INSTRUKTAŻEM … CAŁE UZĘBIENIE (ST30F)” i sekcja instruktażu', '(ST30F)' in txt and 'CAŁE UZĘBIENIE' in txt and 'INSTRUKTAŻ HIGIENY JAMY USTNEJ' in txt)

    # wiek
    r = wiz(pg, ['ST30D'], '18', {'ST30D': ['1']})
    chk('ST30D u 18-latka: ostrzeżenie – tylko do 18 r.ż.', has(r['warn'], 'przeznaczone dla dzieci'), r['warn'])
    r = wiz(pg, ['ST30F'], '17')
    chk('ST30F u 17-latka: bez ostrzeżenia o wieku', not has(r['warn'], 'przeznaczone dla dzieci'), r['warn'])

    # ST30G bez instruktażu + podpowiedź ST30F; ST30E bez ST30D – podpowiedź
    r = wiz(pg, ['ST30G'], '10')
    txt = pg.evaluate("genTxt()")
    chk('ST30G: opis BEZ sekcji instruktażu (zgodnie z nazwą)', 'BEZ INSTRUKTAŻU' in txt and 'INSTRUKTAŻ HIGIENY JAMY USTNEJ' not in txt, txt[-300:])
    chk('ST30G: informacja „z instruktażem rozlicz ST30F”', has(r['info'], 'rozlicz ST30F'), r['info'])
    r = wiz(pg, ['ST30E'], '10', {'ST30E': ['1', '2']})
    chk('ST30E bez ST30D: podpowiedź „1× ST30D + pozostałe ST30E”', has(r['info'], '1× ST30D'), r['info'])

    # wycena: ST30D + 2× ST30E u dziecka = 66 + 48 (bez ×1,5, ST30E bez ×0,8)
    wiz(pg, ['ST30D', 'ST30E'], '10', {'ST30D': ['1'], 'ST30E': ['2', '3']})
    tot = pg.evaluate("(()=>{const t=document.querySelector('#pts-total, [data-testid=\"pts-total\"]');return t?t.textContent:document.body.innerText})()")
    chk('Wycena ST30D + 2× ST30E = 114 pkt', '114' in tot, tot[:200] if len(tot) < 400 else 'brak 114 w stronie')
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('ST30D i ST30F – higienizacja z instruktażem (Opisy NFZ)')
