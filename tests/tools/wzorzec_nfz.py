# Generuje wzorzec zgodności silnika NFZ: losowe przypadki liczone w STAREJ aplikacji (opisy-nfz/nfz.html, prawdziwa przeglądarka).
# Użycie: python3 tests/tools/wzorzec_nfz.py <ścieżka do repo opisy-nfz> [liczba przypadków]
# Wynik: tests/fixtures/nfz_stara_wersja.json (test tests/nfz-zgodnosc.test.ts porównuje z nim nowy silnik).
import json, os, random, subprocess, sys, time
OLD = os.path.abspath(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
sys.path.insert(0, os.path.join(OLD, 'testy'))
os.environ.setdefault('OPISY_URL', 'http://127.0.0.1:8765/nfz.html')
from h import sync_playwright, launch, open_page, BASE  # noqa: E402
commit = subprocess.run(['git', '-C', OLD, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
random.seed(20261116)
QTY = {'ST30': 4, 'ST30E': 4, '1006': 4, 'ST04': 4, '1206': 4, 'ST01': 4, 'ST02': 4, 'ST19': 1, '1101': 4, '1105': 3, '1108': 4, '1502': 4, '1503': 4, '1504': 3, '1505': 3}
cases = []
with sync_playwright() as p:
    b = launch(p); ctx = b.new_context(); pg = open_page(ctx, BASE)
    pg.wait_for_function("typeof D==='object' && typeof nfzPoints==='function'")
    codes = pg.evaluate("Object.keys(D)")
    for i in range(N):
        cs = random.sample(codes, random.randint(1, 6))
        qty = {c: (random.randint(0 if c == '1206' else 1, QTY[c]) if c in QTY else 1) for c in cs}
        age = random.choice([None, 2, 4, 10, 15, 17, 18, 25, 40, 70])
        preg = random.random() < 0.3
        an = {k: random.choice([0, 0, 1, 2, 3]) for k in ['0401', '0402', '0403']}
        cases.append({'codes': cs, 'qty': qty, 'age': age, 'preg': preg, 'an': an})
    res = pg.evaluate("""(cases)=>cases.map(k=>{
        state.codes=k.codes.slice(); state.a=Object.assign({}, state.a, {'sh.preg': k.preg?'tak':''});
        ['0401','0402','0403'].forEach(x=>state.a['pt.an'+x]=k.an[x]?String(k.an[x]):'');
        window.ptsQty=c=>[k.qty[c],'']; window.AGE=()=>k.age;
        const P=nfzPoints(); return {total:P.total, rows:P.rows.map(r=>[r.c,r.q,r.k,r.n10,r.n08,Math.round(r.pts*10000)/10000])};})""", cases)
    money = []
    for i in range(N):
        money.append({'pts': round(random.uniform(0, 900), random.choice([0, 1, 2])), 'price': random.choice([1.84, 1.81, 1.7, 2.05, 1.8399]),
                      'pct': random.choice([40, 35, 0, 100, 33.33]), 'revH': round(random.uniform(0, 8), random.choice([0, 1, 2])),
                      'revRate': random.choice([350, 300, 0, 412.5]), 'ex': [{'c': random.randint(1, 50000)} for _ in range(random.randint(0, 3))],
                      'basis': random.choice(['full', 'share'])})
    mres = pg.evaluate("""(ms)=>ms.map(m=>{cfg.basis=m.basis; const k=calc(m); return [k.pc,k.sh,k.rv,k.ex,k.pe,k.total];})""", money)
    b.close()
for c, r in zip(cases, res): c['old'] = r
for m, r in zip(money, mres): m['old'] = r
out = {'zrodlo': f'opisy-nfz@{commit} nfz.html (nfzPoints, calc) – przeglądarka Chrome', 'wygenerowano': time.strftime('%Y-%m-%d'), 'punkty': cases, 'kwoty': money}
json.dump(out, open(os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'nfz_stara_wersja.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(f'zapisano {len(cases)} przypadków punktów i {len(money)} kwot (źródło {out["zrodlo"]})')
