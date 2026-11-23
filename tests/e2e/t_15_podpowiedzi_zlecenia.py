# Pkt 5 zadania (22.11.2026): podpowiedzi „3 najczęstsze” w Zleceniach protetycznych (laboratorium, system implantu, kolor) –
# z historii zleceń na urządzeniu, potem „Moje materiały” i lista wbudowana; własny wpis nadal możliwy.
from pomoc import *
t = T(); chk = t.chk

def ready(pg): pg.wait_for_function("typeof S!=='undefined'&&S.ready===true", timeout=20000); pg.wait_for_timeout(150)
def typ(pg, v):
    if not pg.locator(f'button[data-a="typ"][data-v="{v}"]').is_visible(): pg.click('details[data-sec="typ"] > summary'); pg.wait_for_timeout(100)
    pg.click(f'button[data-a="typ"][data-v="{v}"]'); pg.wait_for_timeout(200)
podp = lambda pg, k: pg.evaluate(f"[...document.querySelectorAll('[data-testid=\"podp-{k}\"] button')].map(b=>b.dataset.v)")

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz Z', 'zl.15@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '/zlecenia'); ready(pg)
    pg.click('button[data-a="nowe"]'); pg.wait_for_timeout(300); typ(pg, 'kor-emax')
    pg.click('button[data-a="ch"][data-k="skala"][data-v="Vita Classic"]'); pg.wait_for_timeout(150)
    k = podp(pg, 'kolor')
    chk('kolor: 3 podpowiedzi z wybranej skali (bez historii)', len(k) == 3 and all(x in ['A1', 'A2', 'A3', 'A3,5', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D2', 'D3', 'D4'] for x in k), k)
    pg.click(f'[data-testid="podp-kolor"] button[data-v="{k[1]}"]'); pg.wait_for_timeout(150)
    chk('klik w podpowiedź ustawia wartość pola', pg.evaluate("S.cur.a.kolor") == k[1] and pg.input_value('#f_kolor') == k[1])
    pg.fill('#f_lab', 'Laboratorium Kowalczyk'); pg.dispatch_event('#f_lab', 'input'); pg.wait_for_timeout(100)
    chk('własna wartość wpisana ręcznie', pg.evaluate("S.cur.a.lab") == 'Laboratorium Kowalczyk')
    pg.click('button[data-a="zapisz"]'); pg.wait_for_timeout(500)
    for kol in ['B2', 'B2']:
        pg.click('button[data-a="lista"]') if pg.locator('button[data-a="lista"]').count() else None; pg.wait_for_timeout(150)
        pg.click('button[data-a="nowe"]'); pg.wait_for_timeout(300); typ(pg, 'kor-emax')
        pg.click('button[data-a="ch"][data-k="skala"][data-v="Vita Classic"]'); pg.wait_for_timeout(100)
        pg.fill('#f_kolor', kol); pg.dispatch_event('#f_kolor', 'input'); pg.click('button[data-a="zapisz"]'); pg.wait_for_timeout(500)
    pg.goto(URL + '/zlecenia'); ready(pg); pg.click('button[data-a="nowe"]'); pg.wait_for_timeout(300); typ(pg, 'kor-emax')
    pg.click('button[data-a="ch"][data-k="skala"][data-v="Vita Classic"]'); pg.wait_for_timeout(150)
    chk('kolor: najczęściej używany (B2 ×2) pierwszy', podp(pg, 'kolor')[0] == 'B2', podp(pg, 'kolor'))
    chk('laboratorium: wpisane wcześniej podpowiada się', 'Laboratorium Kowalczyk' in podp(pg, 'lab'), podp(pg, 'lab'))
    chk('Brak błędów JavaScript', not errs, errs)
    br.close()
t.done('podpowiedzi w Zleceniach protetycznych (pkt 5)')
