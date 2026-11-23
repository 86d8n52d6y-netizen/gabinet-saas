# Prompt Patryka 23.11.2026, pkt 9: niezawodne wejście do Opisów prywatnych – wielokrotne przechodzenie z innych zakładek,
# wstecz / naprzód, odświeżenie, dwie karty naraz (inny moduł otwarty w drugiej karcie), ponowne logowanie. Chromium
# (Safari / WebKit niedostępny w środowisku testowym – diagnostyka etapów startu w komunikacie i konsoli).
import time
from pomoc import *
t = T(); chk = t.chk
GOT = "typeof S!=='undefined'&&S.ready===true"

def wejdz(pg, skad=None, limit=12000):
    if skad: pg.goto(URL + skad); pg.wait_for_timeout(250)
    t0 = time.time(); pg.goto(URL + '/opisy-prywatne'); pg.wait_for_function(GOT, timeout=limit); return round(time.time() - t0, 2)

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz D', 'dostep.17@example.com', 'zielony-kubek-na-biurku', bypass_csp=True)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    czasy, bad = [], []
    for i in range(12):
        skad = ['/opisy-nfz', '/nfz', '/kalendarz', '/zlecenia', '/zarobki', '/konto'][i % 6]
        try: czasy.append(wejdz(pg, skad))
        except Exception as e: bad.append((skad, str(e)[:80]))
    chk('12 wejść do Opisów prywatnych z różnych zakładek – każde gotowe', not bad and len(czasy) == 12, bad)
    chk('Czas startu: każdy < 8 s (bez przeładowania przez bezpiecznik)', max(czasy) < 8, czasy)
    chk('Etapy startu zapisane (diagnostyka): ostatni etap „gotowe”', pg.evaluate("G.etapNow") == 'gotowe' and len(pg.evaluate("G.etapy")) >= 5, pg.evaluate("G.etapy"))
    # wstecz / naprzód
    pg.goto(URL + '/opisy-nfz'); pg.wait_for_timeout(400); pg.go_back(); pg.wait_for_function(GOT, timeout=12000); pg.go_forward(); pg.wait_for_timeout(400); pg.go_back(); pg.wait_for_function(GOT, timeout=12000)
    chk('Wstecz / naprzód: Opisy prywatne gotowe', pg.evaluate(GOT))
    # odświeżenie
    for _ in range(3): pg.reload(); pg.wait_for_function(GOT, timeout=12000)
    chk('3× odświeżenie: Opisy prywatne gotowe', pg.evaluate(GOT))
    # dwie karty: Opisy NFZ i NFZ otwarte w drugiej karcie, potem wejście do prywatnych w pierwszej
    p2 = ctx.new_page(); p2.goto(URL + '/opisy-nfz'); p2.wait_for_function("typeof DB!=='undefined'&&DB.ready===true", timeout=20000)
    p3 = ctx.new_page(); p3.goto(URL + '/opisy-prywatne'); p3.wait_for_function(GOT, timeout=12000)
    ok2 = True
    try: wejdz(pg, '/nfz')
    except Exception: ok2 = False
    chk('Trzy karty naraz (Opisy NFZ, Opisy prywatne, NFZ → prywatne): wszystkie gotowe', ok2 and p3.evaluate(GOT))
    p2.close(); p3.close()
    # zapis wizyty i ponowne wejście (dane zostają)
    pg.fill('#p_q', 'skaling'); pg.wait_for_timeout(100); pg.click('button[data-add="hig-skaling"]'); pg.wait_for_timeout(150); pg.click('#b_save'); pg.wait_for_function("S.visits.size===1"); pg.wait_for_timeout(600)
    # ponowne logowanie
    ctx.clear_cookies(); pg.goto(URL + '/opisy-prywatne'); chk('Po wylogowaniu: przekierowanie do logowania', '/logowanie' in pg.url)
    pg.goto(URL + '/logowanie'); fill(pg, email='dostep.17@example.com', password='zielony-kubek-na-biurku'); submit(pg, 'Zaloguj')   # ten sam adres co testy (przekierowanie wskazuje localhost)
    wejdz(pg); chk('Po ponownym zalogowaniu: Opisy prywatne gotowe, zapisana wizyta jest', pg.evaluate("S.visits.size") == 1)
    chk('Brak błędów JavaScript', not errs, errs[:3])
    br.close()
t.done('dostęp do Opisów prywatnych (23.11.2026)')
