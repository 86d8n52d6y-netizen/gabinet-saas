# Etap K1 (decyzja Patryka 22.11.2026): 144 karty procedur zweryfikowane jako procedury do klikania w Opisach prywatnych,
# blok dokumentacyjny (rozpoznanie, znieczulenie z dawką, powikłania, informacja i zgoda – rozp. MZ Dz.U. 2026 poz. 1391,
# ustawa o prawach pacjenta art. 9, 16–18, ustawa o zawodach lekarza art. 31–34), puste obowiązkowe → [UZUPEŁNIJ],
# podpowiedzi „3 najczęstsze”. Własne procedury (19) bez zmian; w chmurze nadal bez treści i pól szablonu.
import json
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(200)
def synced(pg, timeout=8000):
    pg.wait_for_function("document.getElementById('gsync')&&document.getElementById('gsync').textContent.includes('zsynchronizowana')", timeout=timeout)
def dodaj(pg, q, pid):
    pg.fill('#p_q', q); pg.wait_for_timeout(150); pg.click(f'button[data-add="{pid}"]'); pg.wait_for_timeout(200)
def pole(pg, i, k): return f'[data-i="{i}"][data-k="{k}"]'

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz K', 'karty.13@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/opisy-prywatne'); ready(pg)

    n = pg.evaluate("({all:KAT.proc.length,karty:KAT.proc.filter(p=>p.karta).length,wlasne:KAT.proc.filter(p=>!p.karta).length,uniq:new Set(KAT.proc.map(p=>p.id)).size})")
    chk('Katalog: 19 własnych procedur + 144 karty zweryfikowane, bez duplikatów', n == {'all': 163, 'karty': 144, 'wlasne': 19, 'uniq': 163}, n)
    chk('Własne procedury bez zmian (np. „Opracowanie ubytku + odbudowa kompozytowa”)', pg.evaluate("PROC.get('zach-kompozyt').name") == 'Opracowanie ubytku + odbudowa kompozytowa')
    chk('Nowe kategorie: Protetyka i Znieczulenia', pg.evaluate("KAT.kat.map(k=>k.name).includes('Protetyka')&&KAT.kat.map(k=>k.name).includes('Znieczulenia')"))
    chk('Karty NFZ i prywatne – obie grupy dostępne (decyzja: wszystkie 144 w prywatnych)', pg.evaluate("KAT.proc.filter(p=>p.karta&&/gwarantowane NFZ/.test(p.desc)).length") == 73)

    # ---- wypełnienie 1 powierzchni (23.1502)
    dodaj(pg, '23.1502', 'karta-23_1502')
    chk('Wyszukiwanie po kodzie karty (23.1502) i dodanie do wizyty', pg.evaluate("V.items.length===1&&V.items[0].pid==='karta-23_1502'"))
    t0 = pg.evaluate("visitText()")
    chk('Puste: ząb, rozpoznanie, informacja i zgoda → [UZUPEŁNIJ]', all(s in t0 for s in ['[UZUPEŁNIJ: Ząb (FDI)]', '[UZUPEŁNIJ: Rozpoznanie / wskazanie (ICD-10)]', '[UZUPEŁNIJ: Informacja dla pacjenta]', '[UZUPEŁNIJ: Zgoda pacjenta]']), t0)
    chk('Puste zalecane (powikłania, materiał, znieczulenie) – pominięte', 'Powikłania' not in t0 and 'Materiał' not in t0 and 'Znieczulenie' not in t0, t0)
    pg.fill(pole(pg, 0, 'k_zab'), '36'); pg.press(pole(pg, 0, 'k_zab'), 'Tab')
    pg.check('[data-i="0"][data-k="k_powierzchnie"][data-o="1"]')
    sug = pg.evaluate("[...document.querySelectorAll('.pw-qb[data-k=\"k_rozpoznanie\"]')].map(b=>b.dataset.v)")
    chk('Rozpoznanie: podpowiedzi ICD-10 z karty jako przyciski (maks. 3)', 0 < len(sug) <= 3 and all(s[:1] == 'K' for s in sug), sug)
    pg.click(f'.pw-qb[data-k="k_rozpoznanie"][data-v="{sug[0]}"]')
    pg.select_option(pole(pg, 0, 'zn'), 'nasiękowe'); pg.wait_for_timeout(150)
    prep = pg.evaluate("[...document.querySelectorAll('.pw-qb[data-k=\"znprep\"]')].map(b=>b.dataset.v)")
    chk('Środek znieczulający: Dentocaine wpisane samo (decyzja Patryka) i pierwsze w podpowiedziach', pg.evaluate("V.items[0].vals.znprep").startswith('Dentocaine') and 'Dentocaine' in prep[0] and pg.input_value(pole(pg, 0, 'znprep')).startswith('Dentocaine'), prep)
    chk('Znieczulenie w formularzu zaraz pod rozpoznaniem', pg.evaluate("(()=>{const k=PROC.get('karta-23_1502').fields.map(f=>f.k);return k.indexOf('zn')===k.indexOf('k_rozpoznanie')+1&&k.indexOf('znprep')===k.indexOf('zn')+1})()"))
    chk('Dawka: przyciski ½ / 1 / 2 amp., domyślnie 1,7 ml', pg.locator('.pw-qb[data-k="zndawka"]').count() == 3 and pg.evaluate("V.items[0].vals.zndawka") == '1,7')
    pg.click(f'.pw-qb[data-k="znprep"][data-v="{prep[0]}"]')
    pg.fill(pole(pg, 0, 'mat'), 'Mój kompozyt X'); pg.press(pole(pg, 0, 'mat'), 'Tab')
    chk('Własna wartość wpisana ręcznie mimo podpowiedzi', pg.evaluate("V.items[0].vals.mat") == 'Mój kompozyt X')
    pg.click('.pw-qb[data-k="k_powiklania"][data-v="nie wystąpiły"]')
    pg.select_option(pole(pg, 0, 'dok_inf'), 'krótka'); pg.select_option(pole(pg, 0, 'dok_zg'), 'ustna'); pg.wait_for_timeout(150)
    t1 = pg.evaluate("visitText()")
    for s_ in ['Ząb 36: odbudowa jednej powierzchni – powierzchnie O.', 'Rozpoznanie: ' + sug[0] + '.', 'Znieczulenie nasiękowe: ' + prep[0] + ', 1,7 ml.',
               'Materiał: Mój kompozyt X', 'Powikłania: nie wystąpiły.', 'Pacjenta poinformowano o rozpoznaniu, planowanym leczeniu, metodach alternatywnych, ryzyku powikłań i rokowaniu.',
               'Pacjent wyraził ustną zgodę na zabieg.']:
        chk('Opis w zdaniach: „' + s_[:60] + '”', s_ in t1, t1)
    chk('Brak [UZUPEŁNIJ] po wypełnieniu obowiązkowych (kolor częściowo – podany materiał bez koloru → znacznik)', t1.count('[UZUPEŁNIJ') == 1 and '[UZUPEŁNIJ: Kolor' in t1, t1)

    # ---- dziecko < 16 lat: warianty A3 / B3
    pg.select_option(pole(pg, 0, 'dok_wiek'), 'poniżej 16 lat'); pg.select_option(pole(pg, 0, 'dok_zg'), 'pisemna'); pg.wait_for_timeout(150)
    t2 = pg.evaluate("visitText()")
    chk('< 16 lat: informacja dla przedstawiciela ustawowego + wysłuchanie zdania (art. 31 ust. 6–7 u.z.l.)', 'Przedstawiciela ustawowego pacjenta poinformowano' in t2 and 'wysłuchano jego zdania' in t2, t2)
    chk('< 16 lat, pisemna: zgoda przedstawiciela, oświadczenie w dokumentacji', 'Zgodę pisemną na zabieg wyraził przedstawiciel ustawowy pacjenta; oświadczenie o zgodzie dołączono do dokumentacji.' in t2, t2)
    pg.select_option(pole(pg, 0, 'dok_wiek'), 'dorosły'); pg.select_option(pole(pg, 0, 'dok_zg'), 'ustna'); pg.wait_for_timeout(100)

    # ---- druga procedura z karty: ekstrakcja (23.1701) – zgoda/informacja tylko raz, rozpoznania z tej karty
    dodaj(pg, 'usunięcie', 'karta-23_1701')
    sug2 = pg.evaluate("[...document.querySelectorAll('.pw-qb[data-i=\"1\"][data-k=\"k_rozpoznanie\"]')].map(b=>b.dataset.v)")
    chk('Ekstrakcja: podpowiedzi rozpoznań z karty ekstrakcji (nie z wypełnienia)', sug2 != sug and not any(x == sug[0] for x in sug2) or sug2 == [], {'wyp': sug, 'eks': sug2})
    chk('Karta zabiegowa bez pól znieczulenia w szablonie – pole znieczulenia dodane', pg.locator(pole(pg, 1, 'zn')).count() == 1)
    pg.fill(pole(pg, 1, 'k_zab'), '48'); pg.press(pole(pg, 1, 'k_zab'), 'Tab')
    pg.fill(pole(pg, 1, 'k_rozpoznanie'), 'K01.1 Zęby zatrzymane'); pg.press(pole(pg, 1, 'k_rozpoznanie'), 'Tab')
    pg.select_option(pole(pg, 1, 'dok_inf'), 'krótka'); pg.select_option(pole(pg, 1, 'dok_zg'), 'ustna'); pg.wait_for_timeout(150)
    t3 = pg.evaluate("visitText()")
    chk('Dwie procedury z tą samą informacją i zgodą – zdania w opisie tylko raz', t3.count('Pacjent wyraził ustną zgodę na zabieg.') == 1 and t3.count('Pacjenta poinformowano') == 1, t3)
    chk('„Wykonano: …” z obu procedur i zębów', 'ząb 36' in t3.split('\n')[0] and 'ząb 48' in t3.split('\n')[0], t3.split('\n')[0])
    pg.select_option(pole(pg, 1, 'dok_zg'), 'odmowa'); pg.wait_for_timeout(100)
    chk('Odmowa → pole „na co” wymagane', '[UZUPEŁNIJ: Odmowa – na co]' in pg.evaluate("visitText()"))
    pg.fill(pole(pg, 1, 'dok_odm'), 'usunięcie zęba 48'); pg.press(pole(pg, 1, 'dok_odm'), 'Tab')
    chk('Odmowa: zdanie zgodne z art. 16 u.p.p.', 'Pacjent, poinformowany o następstwach zaniechania leczenia, nie wyraził zgody na: usunięcie zęba 48.' in pg.evaluate("visitText()"))
    pg.select_option(pole(pg, 1, 'dok_zg'), 'ustna'); pg.wait_for_timeout(100)

    # ---- cena, zapis, chmura bez treści, ponowne otwarcie z historii
    pg.fill('[data-pr="c"][data-i="0"]', '300'); pg.press('[data-pr="c"][data-i="0"]', 'Tab'); pg.fill('[data-pr="p"][data-i="0"]', '40'); pg.press('[data-pr="p"][data-i="0"]', 'Tab')
    txt = pg.evaluate("curText()")
    pg.click('#b_save'); pg.wait_for_function("V.id&&S.visits.size===1"); pg.wait_for_timeout(300); synced(pg)
    chk('Zarobki: procedura z karty w chmurze (300 zł, lekarz 120 zł)', sql("SELECT label||'|'||value_gr||'|'||doctor_pay_gr FROM app.earnings_entries WHERE source='private_procedure' AND value_gr>0") == pg.evaluate("PROC.get('karta-23_1502').name") + '|30000|12000')
    dump = sql("SELECT string_agg(t::text,' ') FROM (SELECT row_to_json(s) t FROM app.saved_descriptions s UNION ALL SELECT row_to_json(e) FROM app.earnings_entries e) x")
    chk('W chmurze BRAK treści, pól i bloku (zgoda, rozpoznanie, preparat)', 'zgod' not in dump and 'K01.1' not in dump and 'Mój kompozyt' not in dump and '"vals"' not in dump and 'ktpl' not in dump, dump[:300])
    vid = pg.evaluate("V.id")
    pg.reload(); ready(pg)
    pg.click('#tabs button[data-tab="hist"]'); pg.wait_for_timeout(200)
    pg.click(f'button[data-a="hopen"][data-id="{vid}"]'); pg.wait_for_function(f"V.id==='{vid}'"); pg.wait_for_timeout(300)
    chk('Wizyta otwarta z historii – ten sam tekst (wersja szablonu karty zapisana)', pg.evaluate("curText()") == txt)

    # ---- Szablony: karty bez edycji, własne z edycją
    pg.click('#tabs button[data-tab="tpl"]'); pg.wait_for_timeout(200)
    chk('Szablony: karta bez „Edytuj” (tekst z bazy kart), własna procedura z „Edytuj”',
        pg.locator('#t-karta-23_1502 [data-a="tedit"]').count() == 0 and pg.locator('#t-karta-23_1502 .pw-tag', has_text='karta 23.1502').count() == 1 and pg.locator('#t-zach-kompozyt [data-a="tedit"]').count() == 1)
    chk('Brak błędów JavaScript', not errs, errs)
    br.close()
t.done('karty procedur do klikania w Opisach prywatnych – K1')
