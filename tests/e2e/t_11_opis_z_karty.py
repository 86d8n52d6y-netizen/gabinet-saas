# Etap I2 – opis z karty procedury (decyzja Patryka 22.11.2026): Opisy prywatne + Opisy NFZ (osobny przycisk), domyślnie wariant
# standardowy, formularz z typami pól. Tylko karty zweryfikowane; tekst dopisywany do opisu jako edycja ręczna; nic nie wychodzi na serwer
# poza tym, co moduł i tak zapisuje; generator opisu NFZ bez zmian.
import json, os
from pomoc import *
t = T(); chk = t.chk
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
PROC = json.load(open(os.path.join(ROOT, 'data', 'procedury-icd9', 'procedures.json')))['procedury']
N_VER = sum(p['status'] == 'verified' for p in PROC)
REJ = next(p for p in PROC if p.get('uzasadnienie_statusu', '').startswith('Odrzucone'))

def nfz_ready(pg): pg.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000); pg.wait_for_timeout(200)
def pryw_ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def wybierz_karte(pg, q, kod):
    pg.click('[data-testid="ozk-otworz"]'); pg.wait_for_selector('[data-testid="ozk"]')
    pg.fill('[data-testid="ozk-szukaj"]', q); pg.wait_for_timeout(100)
    pg.click(f'[data-testid="ozk-lista"] button:has-text("{kod}")'); pg.wait_for_selector('[data-testid="ozk-podglad"]')

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz O', 'opis.11@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    sent = []; pg.on('request', lambda r: sent.append((r.url, r.post_data or '')) if r.method in ('POST', 'PUT') else None)

    # ---- czysta funkcja składania (ta sama zasada co w dokumentacji bazy)
    pg.goto(URL + '/opisy-nfz'); nfz_ready(pg)
    chk('Dane kart wczytane: tylko karty zweryfikowane', pg.evaluate("KARTY_OPISY.karty.length") == N_VER, pg.evaluate("KARTY_OPISY.karty.length"))
    chk('Karta odrzucona nie jest dostępna', pg.evaluate(f"!KARTY_OPISY.karty.some(k=>k.kod==='{REJ['kod']}')"))
    z = pg.evaluate("OpisZKarty.zloz('Ząb {{POLE-ZAB}}: zabieg. Kolor: {{POLE-KOLOR}}. Materiał: {{POLE-MATERIAL}}.',{'POLE-ZAB':'36','POLE-MATERIAL':'kompozyt'})")
    chk('Składanie: zdanie bez wartości pominięte w całości', z == 'Ząb 36: zabieg. Materiał: kompozyt.', z)
    z2 = pg.evaluate("OpisZKarty.zloz('Znieczulenie: {{POLE-ZNIECZ-RODZAJ}} {{POLE-ZNIECZ-PREPARAT}}.',{'POLE-ZNIECZ-RODZAJ':'nasiękowe'},{'POLE-ZNIECZ-PREPARAT':'preparat znieczulający'})")
    chk('Składanie: zdanie częściowo wypełnione – zostaje, brak jako [UZUPEŁNIJ: …]', z2 == 'Znieczulenie: nasiękowe [UZUPEŁNIJ: preparat znieczulający].', z2)

    # ---- Opisy NFZ: krok 3 → przycisk → karta 23.1503 → formularz z typami pól
    pg.evaluate("()=>{state.codes=['1503'];state.a={'sh.age':'40'};state.teeth={'1503':{'36':{s:['M','O'],f:{}}}};state.step=3;render()}"); pg.wait_for_timeout(200)
    gen0 = pg.evaluate("genTxt()")
    chk('NFZ krok 3: przycisk „Opis z karty” obok „Edytuj tekst”', pg.locator('[data-testid="ozk-otworz"]').count() == 1)
    wybierz_karte(pg, '23.1503', '23.1503')
    chk('Domyślnie wariant standardowy', pg.locator('[data-testid="ozk-warianty"] button[aria-pressed="true"]').inner_text() == 'standardowy')
    chk('Formularz: powierzchnie jako przyciski, znieczulenie jako lista', pg.locator('[data-pw="POLE-POWIERZCHNIE"]').count() >= 5 and pg.locator('select#ozk-POLE-ZNIECZ-RODZAJ').count() == 1)
    chk('Rozpoznanie z podpowiedziami ICD-10 z karty', pg.locator('#ozk-icd option').count() >= 2)
    pg.fill('#ozk-POLE-ZAB', '36'); pg.click('[data-pw="POLE-POWIERZCHNIE"][data-v="M"]'); pg.click('[data-pw="POLE-POWIERZCHNIE"][data-v="O"]')
    pg.select_option('#ozk-POLE-ZNIECZ-RODZAJ', 'nasiękowe'); pg.fill('#ozk-POLE-MATERIAL', 'kompozyt'); pg.fill('#ozk-POLE-KOLOR', 'A2')
    pv = pg.inner_text('[data-testid="ozk-podglad"]')
    if os.environ.get('ZRZUT'): pg.set_viewport_size({'width': 900, 'height': 1100}); pg.screenshot(path=os.environ['ZRZUT'] + '/ozk_nfz.png', full_page=False)
    chk('Podgląd: wpisane wartości w tekście, puste zdania pominięte, brak preparatu jako [UZUPEŁNIJ]', '36' in pv and 'MO' in pv and 'kompozyt' in pv and 'A2' in pv and 'nasiękowe' in pv and '[UZUPEŁNIJ: preparat' in pv and '{{' not in pv and 'Powikłania' not in pv, pv)
    pg.click('[data-testid="ozk-warianty"] button:has-text("skrócony")'); pv2 = pg.inner_text('[data-testid="ozk-podglad"]')
    chk('Zmiana wariantu na skrócony: krótszy tekst, wartości zachowane', len(pv2) < len(pv) and '36' in pv2, pv2)
    pg.click('[data-testid="ozk-warianty"] button:has-text("standardowy")')
    pg.click('[data-testid="ozk-wstaw"]'); pg.wait_for_timeout(300)
    ed = pg.evaluate("state.ed&&state.ed.txt")
    chk('NFZ: tekst z karty dopisany na końcu opisu (edycja ręczna)', bool(ed) and ed.startswith(gen0) and ed.rstrip().endswith(pv.rstrip()), (ed or '')[-300:])
    chk('NFZ: generator opisu bez zmian (genTxt jak przed wstawieniem)', pg.evaluate("genTxt()") == gen0)
    chk('NFZ: pole edycji pokazuje tekst z karty', pv[:20] in pg.input_value('#edTxt'))
    chk('NFZ: w trybie edycji przycisk „Opis z karty” nadal dostępny', pg.locator('[data-testid="ozk-otworz"]').count() == 1)
    pg.click('[data-testid="ozk-otworz"]'); pg.keyboard.press('Escape'); pg.wait_for_timeout(100)
    chk('Escape zamyka okienko bez zmian', pg.locator('[data-testid="ozk"]').count() == 0 and pg.evaluate("state.ed.txt") == ed)

    # ---- Opisy prywatne
    pg.goto(URL + '/opisy-prywatne'); pryw_ready(pg)
    pg.click('#tabs button[data-tab="wiz"]'); pg.wait_for_timeout(150)
    pg.click('button[data-add="zach-kompozyt"]'); pg.wait_for_timeout(200)
    gen_p = pg.evaluate("visitText()")
    chk('Prywatne: przycisk „Opis z karty”', pg.locator('[data-testid="ozk-otworz"]').count() == 1)
    wybierz_karte(pg, 'wybielanie', '23.1512')
    pg.fill('#ozk-POLE-ZEBY', '13–23'); pv3 = pg.inner_text('[data-testid="ozk-podglad"]')
    if os.environ.get('ZRZUT'): pg.screenshot(path=os.environ['ZRZUT'] + '/ozk_pryw.png')
    pg.click('[data-testid="ozk-wstaw"]'); pg.wait_for_timeout(300)
    txt = pg.evaluate("curText()")
    chk('Prywatne: tekst z karty dopisany do opisu wizyty (edycja ręczna)', pg.evaluate("V.edited") and txt.startswith(gen_p.rstrip()) and txt.rstrip().endswith(pv3.rstrip()), txt[-300:])
    chk('Prywatne: pole edycji z tekstem', pv3[:15] in pg.input_value('#txt_ed'))
    chk('brak błędów JavaScript', not errs, errs)
    chk('Wpisane w okienku wartości nie są wysyłane osobno na serwer (np. „13–23”, „A2” poza zapisem wizyty)', not any('13–23' in d or '"A2"' in d for u, d in sent if '/api/' in u and 'wizyt' not in u), [u for u, d in sent][:10])
    br.close()
t.done('opis z karty procedury – I2 (Opisy prywatne i NFZ)')
