# Zrzuty ekranu stron (kontrola wyglądu): python3 zrzuty.py przez uruchom.sh tests/e2e/zrzuty.py
import os
from pomoc import *
OUT = os.environ.get('ZRZUTY', '/tmp/zrzuty'); os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz', 'z@example.com', 'zielony-kubek-na-biurku')
    pg.goto(URL + '/gabinety'); fill(pg, name='Happy Smile', short='HS', pct='30'); submit(pg, 'Dodaj gabinet')
    for w, n in [(1280, 'desktop'), (390, 'telefon')]:
        pg.set_viewport_size({'width': w, 'height': 900})
        for path in ['ustawienia', 'gabinety?nowy=1', 'katalog-nfz']:
            pg.goto(URL + '/' + path); pg.screenshot(path=f"{OUT}/{path.split('?')[0]}-{n}.png", full_page=True)
    br.close()
print('zrzuty w', OUT)
