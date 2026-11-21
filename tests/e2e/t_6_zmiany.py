# Zmiany 21.11.2026 (prompt Patryka): 2FA – włączanie wyłączone bez osłabienia logowania; Zarobki – przełącznik brutto/netto
# bez wymyślonych zasad netto; Katalog NFZ bez „Własnych kodów” i „Sprawdź wycenę”; nowa nazwa modelu „% po odjęciu kosztów własnych”.
from pomoc import *
t = T(); chk = t.chk

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    ctx, pg = konto(br, 'Lekarz Z', 'z.6@example.com', 'zielony-kubek-na-biurku')
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))

    # ---- 2FA
    pg.goto(URL + '/konto/bezpieczenstwo')
    body = pg.inner_text('main')
    chk('Bezpieczeństwo: brak włączania 2FA (sekcja ukryta)', 'Weryfikacja dwuetapowa' not in body and pg.locator('#mfa-cur').count() == 0, body[:300])
    chk('Bezpieczeństwo: zmiana hasła, urządzenia i historia zostają', 'Zmiana hasła' in body and 'Wyloguj ze wszystkich urządzeń' in body)
    pg.goto(URL + '/konto'); chk('Konto: link bez wzmianki o 2FA', 'weryfikacja dwuetapowa' not in pg.inner_text('main').lower())
    ctx.clear_cookies()
    pg.goto(URL + '/logowanie'); fill(pg, email='z.6@example.com', password='zła-hasło-12345'); submit(pg, 'Zaloguj')
    chk('logowanie: złe hasło odrzucone', '/logowanie' in pg.url and '/konto' not in pg.url)
    fill(pg, email='z.6@example.com', password='zielony-kubek-na-biurku'); submit(pg, 'Zaloguj')
    chk('logowanie hasłem działa (bez kroku 2FA)', '/konto' in pg.url and '/logowanie/2fa' not in pg.url, pg.url)
    chk('w bazie: brak sekretu 2FA, polityka haseł bez zmian', sql("SELECT mfa_secret_enc IS NULL AND mfa_pending_enc IS NULL FROM app.profiles WHERE email='z.6@example.com'") == 't')

    # ---- brutto / netto
    pg.goto(URL + '/zarobki')
    chk('Zarobki: przełącznik Brutto (domyślnie) / Netto', pg.locator('nav[aria-label="Kwoty brutto lub netto"] a.on').inner_text() == 'Brutto'
        and 'wymaga konfiguracji' in pg.locator('nav[aria-label="Kwoty brutto lub netto"]').inner_text())
    pg.click('text=Netto (wymaga konfiguracji)'); pg.wait_for_url('**kw=netto**')
    chk('Netto bez konfiguracji: informacja, brak wymyślonych kwot', pg.locator('[data-testid=netto-info]').count() == 1 and 'kw=netto' in pg.url)
    chk('Netto: wybór zostaje przy zmianie filtrów', pg.locator('form.filters input[name=kw][value=netto]').count() == 1)

    # ---- katalog i nazwa modelu
    pg.goto(URL + '/katalog-nfz')
    chk('Katalog NFZ: bez „Własne kody” i „Sprawdź wycenę”', 'Własne kody' not in pg.content() and 'Sprawdź wycenę' not in pg.content())
    pg.goto(URL + '/gabinety?nowy=1')
    chk('Gabinety: „% po odjęciu kosztów własnych”, bez starej nazwy', '% po odjęciu kosztów własnych' in pg.content() and 'labu/implantów' not in pg.content())
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('zmiany 21.11.2026: 2FA, brutto/netto, katalog, nazwa modelu')
