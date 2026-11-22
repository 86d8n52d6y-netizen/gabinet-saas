# Audyt NFZ (paczka 21.11.2026, docs/nfz/) – etap N3: ryzyka z INSTRUKCJA_DLA_CLAUDE_CODE.md wg decyzji Patryka.
# P30 R-ST30DG-WIEK (D1=B: ostrzeżenie, nie błąd), P31 R-LAKIER-01, P32 R-KIR-DZ (D4=A: informacja), P33 R-ZNI-02 (ostrzeżenie),
# P34 informacja jako notatka. Punkty i stawki bez zmian. Reguły liczone tylko na urządzeniu (D2=A).
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def wiz(pg, codes, age=None, a=None):
    st = {'sh.age': age} if age is not None else {}
    st.update(a or {})
    pg.evaluate("([c,a])=>{state.codes=c;state.a=a;render()}", [codes, st]); pg.wait_for_timeout(150)
    return pg.evaluate("(()=>{const r=nfzIssues();return {err:r.err.map(e=>e.msg),warn:r.warn.filter(w=>!w.soft&&!w.info).map(w=>w.msg),info:r.warn.filter(w=>w.info).map(w=>w.msg)}})()")
def has(lst, s): return any(s in x for x in lst)
def pts(pg): return pg.evaluate("nfzPoints().total")

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz A', 'audyt.9@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    sent = []; pg.on('request', lambda r: sent.append(r.post_data or '') if r.method == 'POST' else None)
    pg.goto(URL + '/opisy-nfz'); ready(pg)

    # P30 – ST30E / ST30G
    for c in ('ST30E', 'ST30G'):
        r = wiz(pg, [c], '30')
        chk(f'{c}, dorosły (30 l.): ostrzeżenie, nie błąd (D1=B)', has(r['warn'], 'są przeznaczone dla dzieci') and not has(r['err'], 'profesjonalnej higienizacji'), r)
        chk(f'{c}, dorosły: ostrzeżenie podaje źródło (zarządzenie DSOZ)', has(r['warn'], '60/2023/DSOZ'))
        r = wiz(pg, [c], '12'); chk(f'{c}, dziecko (12 l.): bez ostrzeżenia o wieku', not has(r['warn'], 'są przeznaczone dla dzieci') and not has(r['warn'], 'wpisz wiek'), r)
        r = wiz(pg, [c]); chk(f'{c}, bez wieku: przypomnienie „wpisz wiek”', has(r['warn'], 'wpisz wiek'), r)
    wiz(pg, ['ST30E'], '30'); pg.wait_for_timeout(100)
    box = pg.inner_html('#nfz-box')
    chk('ST30E u dorosłego: w okienku żółte ostrzeżenie, nie „Błąd NFZ”', 'class="warn"' in box and 'Błąd NFZ' not in box, box[:300])

    # P31 – 1006 (lakierowanie)
    r = wiz(pg, ['1006'], '40'); chk('1006, dorosły: ostrzeżenie „tylko do 18 r.ż.” ze źródłem', has(r['warn'], 'lakierowanie zębów jest świadczeniem gwarantowanym tylko') and has(r['warn'], 'Dz.U. 2025 poz. 615'), r)
    r = wiz(pg, ['1006'], '8'); chk('1006, dziecko: bez ostrzeżenia o wieku', not has(r['warn'], 'lakierowanie zębów jest'), r)
    r = wiz(pg, ['1006']); chk('1006, bez wieku: przypomnienie', has(r['warn'], '1006: wpisz wiek'), r)
    r = wiz(pg, ['ST30', '1006'], '8'); chk('ST30 + 1006: nadal błąd „nie sumuje się” (R-ST30-LAKIER, bez zmian)', has(r['err'], 'nie mogą być rozliczone razem'), r)

    # P32 – kiretaż u dzieci (INFORMACJA)
    r = wiz(pg, ['ST04'], '15'); chk('ST04, dziecko: informacja „wymaga weryfikacji” (D4=A), nie błąd ani ostrzeżenie', has(r['info'], 'wymaga weryfikacji') and not has(r['err'], 'kiretaż') and not has(r['warn'], 'kiretaż u dzieci'), r)
    box = pg.inner_html('#nfz-box'); chk('informacja wyświetlana jako notatka (P34)', 'class="note"' in box and 'kiretaż u dzieci' in box, box[:400])
    r = wiz(pg, ['ST04'], '45'); chk('ST04, dorosły: bez informacji o dzieciach', not has(r['info'], 'kiretaż'), r)

    # P33 – znieczulenie osobno przy ekstrakcji / kiretażu
    r = wiz(pg, ['ST01', '1502'], '40', {'pt.an0402': '1'})
    chk('ST01 + wypełnienie + znieczulenie osobno: ostrzeżenie (R-ZNI-02), punkty liczone jak wpisano', has(r['warn'], 'wliczone w pakiet') and pts(pg) == 93 + 45 + 12, (r, pts(pg)))
    r = wiz(pg, ['ST04', '1105'], '40', {'pt.an0403': '2'}); chk('ST04 + znieczulenie osobno: ostrzeżenie', has(r['warn'], 'wliczone w pakiet'), r)
    r = wiz(pg, ['1502'], '40', {'pt.an0402': '1'}); chk('samo wypełnienie + znieczulenie: bez ostrzeżenia', not has(r['warn'], 'wliczone w pakiet'), r)
    r = wiz(pg, ['ST01', '1502'], '40'); chk('ST01 bez znieczulenia osobno: bez ostrzeżenia', not has(r['warn'], 'wliczone w pakiet'), r)

    # stawki i punkty bez zmian
    wiz(pg, ['ST30E'], '30'); chk('punkty ST30E bez zmian (24 pkt / ćwiartka)', pg.evaluate("PTS.ST30E") == 24 and pg.evaluate("PTS.ST30G") == 96 and pg.evaluate("PTS['1006']") == 5)
    chk('stawka domyślna bez zmian (1,84 zł/pkt, 350 zł/h)', pg.evaluate("cfg.price") == 1.84 and pg.evaluate("cfg.rev") == 350, pg.evaluate("[cfg.price,cfg.rev]"))
    chk('wiek nie trafia na serwer (D2=A)', not any('sh.age' in d or '"age"' in d for d in sent))
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('audyt NFZ – etap N3 (ryzyka)')
