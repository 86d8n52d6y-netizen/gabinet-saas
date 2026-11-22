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
    # N2 – silnik reguł z danych audytu (na urządzeniu)
    def D(d): return {'sv.date': d}
    r = wiz(pg, ['ST33', 'ST34'], '40', D('2026-11-20'))
    chk('N2: ST33 + ST34 – informacja „wymaga dodatkowej weryfikacji” (para spoza zakazów)', has(r['info'], 'wymaga dodatkowej weryfikacji') and not has(r['err'], 'ST33 i ST34'), r)
    chk('N2: limit badania (1× w roku kalendarzowym) jako informacja (D7=B)', has(r['info'], 'Limit NFZ (ST33)') and has(r['info'], 'roku kalendarzowym') and not has(r['err'], 'Limit'), r)
    r = wiz(pg, ['ST30E'], '12', D('2026-12-15')); chk('N2: przełom roku (grudzień) – ostrzeżenie o roku kalendarzowym (D6=A)', has(r['warn'], 'Przełom roku') and has(r['warn'], 'roku 2026'), r)
    r = wiz(pg, ['ST30E'], '12', D('2027-01-08')); chk('N2: styczeń – wizyta liczy się do roku 2027', has(r['warn'], 'roku 2027'), r)
    r = wiz(pg, ['ST30E'], '12', D('2026-11-20')); chk('N2: listopad – bez ostrzeżenia o przełomie roku', not has(r['warn'], 'Przełom roku') and has(r['info'], 'Limit NFZ (ST30E)'), r)
    r = wiz(pg, ['ST30E'], '12', D('2026-08-20')); chk('N2: reguła oceniana wg daty wizyty – przed 1.09.2026 limit ST30E nie obowiązywał', not has(r['info'], 'Limit NFZ (ST30E)'), r)
    r = wiz(pg, ['ST30', '1006'], '8', D('2026-11-20')); chk('N2: ST30 + 1006 – jeden komunikat (bez duplikatu z danych audytu)', sum('1006' in x and 'razem' in x for x in r['err']) == 1 and not any('ST30 i 1006:' in x for x in r['err']), r['err'])
    wiz(pg, ['ST30E'], '30', D('2026-11-20')); step3 = pg.inner_html('#nfz-box')
    chk('N2: lista „Zasady NFZ dla wybranych kodów” z poziomem, treścią i źródłem', 'Zasady NFZ dla wybranych kodów' in step3 and 'R-ST30DG-WIEK' in step3 and '60/2023/DSOZ' in step3, step3[-600:])
    r = wiz(pg, ['1502'], '30', D('2026-11-20')); chk('N2: wypełnienie bez dodatkowych błędów z danych audytu', r['err'] == [], r)
    pts_a = (wiz(pg, ['ST01', '1502'], '30', D('2026-11-20')), pts(pg))[1]; chk('N2: silnik nie zmienia punktów (ST01 + 1502 = 138 pkt)', pts_a == 138, pts_a)

    # N1 – dane audytu w przeglądarce (generator/nfz-dane.js z data/nfz/)
    import json, os, sys as _s
    _s.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'scripts'))
    import nfz_dane_przegladarka as nd
    wzor = nd.zbuduj(); man = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'nfz', 'manifest.json')))
    nd_js = pg.evaluate("JSON.stringify(window.NFZ_DANE||null)")
    chk('N1: dane NFZ wczytane w Opisach NFZ (wersja z manifestu)', pg.evaluate("window.NFZ_DANE&&NFZ_DANE.wersja") == man['wersja'], pg.evaluate("window.NFZ_DANE&&NFZ_DANE.wersja"))
    chk('N1: plik w przeglądarce = dane z data/nfz (wygenerowany, nie edytowany ręcznie)', json.loads(nd_js) == wzor)
    chk('N1: 47 reguł, każda ze źródłem i datą obowiązywania', pg.evaluate("NFZ_DANE.reguly.length===47&&NFZ_DANE.reguly.every(r=>r.zrodla.length&&r.od)"))
    chk('N1: reguły „WYMAGA WERYFIKACJI” najwyżej jako INFORMACJA (D4=A)', pg.evaluate("NFZ_DANE.reguly.filter(r=>r.status==='WYMAGA WERYFIKACJI').every(r=>r.poziom==='INFORMACJA')"))
    chk('N1: podpowiedzi ICD-10 dla 23.1006 (lekarz wybiera, D3=A)', pg.evaluate("(NFZ_DANE.podpowiedzi_icd10['23.1006']||[]).length>0"))
    chk('N1: dane tylko do odczytu', pg.evaluate("Object.isFrozen(NFZ_DANE)"))
    anon = br.new_context(); pa = anon.new_page()
    r = pa.request.get(URL + '/opisy-nfz/zasoby/nfz-dane.js'); chk('N1: plik danych tylko dla zalogowanych', r.status == 401, r.status); anon.close()
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('audyt NFZ – etapy N3 (ryzyka), N1 (dane) i N2 (silnik reguł)')
