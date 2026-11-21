# Zmiany 21.11.2026 (prompt Patryka): 2FA – włączanie wyłączone bez osłabienia logowania; Zarobki – przełącznik brutto/netto
# netto z ustawień Kalendarza (wariant A, ten sam silnik); Katalog NFZ bez „Własnych kodów” i „Sprawdź wycenę”; nowa nazwa modelu „% po odjęciu kosztów własnych”.
import re, datetime, time
from pomoc import *
t = T(); chk = t.chk
def money(s): return int(round(float(s.replace('\xa0', '').replace('\u202f', '').replace(' ', '').replace('zł', '').replace(',', '.')) * 100)) if s.strip() not in ('—', '') else 0

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

    # ---- brutto / netto (wariant A: netto z ustawień Kalendarza – ten sam silnik co Kalendarz)
    pg.goto(URL + '/zarobki')
    chk('Zarobki: przełącznik Brutto (domyślnie) / Netto', pg.locator('nav[aria-label="Kwoty brutto lub netto"] a.on').inner_text() == 'Brutto'
        and 'wymaga konfiguracji' not in pg.locator('nav[aria-label="Kwoty brutto lub netto"]').inner_text())
    pg.click('nav[aria-label="Kwoty brutto lub netto"] >> text=Netto'); pg.wait_for_url('**kw=netto**')
    chk('Netto bez ustawień Kalendarza: informacja, kwoty brutto (nic nie zgadujemy)', 'nie są jeszcze ustawione' in pg.inner_text('[data-testid=netto-info]')
        and 'kw=netto' in pg.url and '(netto)' not in pg.inner_text('main'))
    chk('Netto: wybór zostaje przy zmianie filtrów', pg.locator('form.filters input[name=kw][value=netto]').count() == 1)

    pg.goto(URL + '/gabinety?nowy=1'); fill(pg, name='Gabinet N', pct='30'); submit(pg, 'Dodaj gabinet')
    A = sql("SELECT id FROM app.clinics WHERE name='Gabinet N'")
    TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat(); MK = TODAY[:7]
    kc = br.new_context(bypass_csp=True); kp = kc.new_page()
    kp.goto(URL + '/logowanie'); fill(kp, email='z.6@example.com', password='zielony-kubek-na-biurku'); submit(kp, 'Zaloguj')
    kp.goto(URL + '/kalendarz')
    kp.wait_for_function("window.Kal&&Kal.UI.loaded===true&&Kal.Store.mode==='local'", timeout=20000); kp.wait_for_timeout(300)
    KK = lambda body: kp.evaluate("()=>{with(Kal){" + body + "}}")
    def kal_saved(cond, n=40):
        for _ in range(n):
            if sql(f"SELECT ({cond}) FROM app.calendar_docs WHERE doc='settings'") == 't': return True
            time.sleep(0.25)
        return False
    chk('Kalendarz (nowe konto): domyślnie bez startu JDG, formy i ZUS – nic nie zakładamy',
        KK("return S().jdgStart===''&&Object.keys(S().regimes).length===0&&S().zus.length===0") is True, KK("return [S().jdgStart,S().regimes,S().zus]"))
    chk('Kalendarz: kreator „Ustaw podatki i ZUS” przy pierwszym otwarciu, pola bez wyboru z góry', kp.locator('#wiz').count() == 1
        and kp.input_value('#wiz-start') == '' and kp.input_value('#wiz-reg') == '' and kp.input_value('#wiz-zus') == '')
    KK(f"M('{MK}',true).shifts.push({{id:'n1',date:'{TODAY}',clinicId:'{A}',start:'08:00',end:'14:00',status:'done',turnover:10000,lab:0}});saveMonth('{MK}');UI.sel='{TODAY}';UI.sheet=true;render();")
    kp.wait_for_timeout(200)
    note = [x for x in kp.locator('.note.tn').all_inner_texts() if 'Dzień: przychód' in x]
    chk('bez ustawień podatków: Kalendarz nie pokazuje „netto ≈” (zamiast wyniku z cudzych założeń)', note and 'netto' not in note[0], note)
    for _ in range(40):
        if 'n1' in (sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'") or ''): break
        time.sleep(0.25)
    chk('dyżur z Kalendarza zapisany na koncie', 'n1' in (sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'") or ''))
    pg.goto(URL + '/zarobki?kw=netto')
    chk('Zarobki → Netto bez ustawień podatków: informacja, kwoty brutto', 'nie są jeszcze ustawione' in pg.inner_text('[data-testid=netto-info]')
        and money(pg.inner_text('[data-testid=zarobek]')) == 300000)
    # kreator: walidacja i zapis
    kp.click('[data-a=wiz-save]'); kp.wait_for_timeout(150)
    chk('kreator: bez odpowiedzi nic nie zapisuje', KK("return S().jdgStart") == '' and 'startu JDG' in kp.inner_text('#toast'))
    kp.fill('#wiz-start', MK); kp.select_option('#wiz-reg', 'skala'); kp.select_option('#wiz-zus', 'custom')
    kp.click('[data-a=wiz-save]'); kp.wait_for_timeout(150)
    chk('kreator: „kwota z eZUS” wymaga kwoty', KK("return S().zus.length") == 0)
    kp.fill('#wiz-amt', '800'); kp.click('[data-a=wiz-save]'); kp.wait_for_timeout(200)
    st = KK("return {j:S().jdgStart,r:S().regimes,z:S().zus.map(z=>[z.from,z.variant,z.amount,z.chor]),ok:!!S().setup.zus}")
    chk('kreator zapisał wybór użytkownika (start, forma, ZUS)', st['j'] == MK and st['r'].get(TODAY[:4]) == 'skala' and st['z'] == [[MK, 'custom', 800, False]] and st['ok'], st)
    chk('kreator znika po zapisie', kp.locator('#wiz').count() == 0)
    kp.evaluate("()=>{Kal.UI.sel=" + repr(TODAY) + ";Kal.UI.sheet=true;Kal.render();}")
    note = [x for x in kp.locator('.note.tn').all_inner_texts() if 'Dzień: przychód' in x]
    kal_net = money(re.search(r'netto ≈ ([^\n·]+)', note[0]).group(1)) if note and 'netto ≈' in note[0] else None
    chk('ustawienia na koncie', kal_saved("data->>'jdgStart'='" + MK + "' AND jsonb_array_length(data->'zus')=1"))

    pg.goto(URL + '/zarobki?kw=netto')
    info = pg.inner_text('[data-testid=netto-info]')
    chk('Netto: opis zasad z Kalendarza (forma na rok) i że to szacunek', 'skala 12% / 32%' in info and 'szacunek' in info, info)
    chk('Netto: kwota ZUS potwierdzona w kreatorze – bez ostrzeżenia', pg.locator('[data-testid=netto-zus]').count() == 0)
    zn = money(pg.inner_text('[data-testid=zarobek]'))
    pg.goto(URL + '/zarobki'); zb = money(pg.inner_text('[data-testid=zarobek]'))
    chk('Brutto bez zmian: 30% z 10 000 zł = 3 000 zł', zb == 300000, zb)
    chk('Netto mniejsze od brutto (ZUS, zdrowotna, podatek)', 0 < zn < zb, (zn, zb))
    chk('Netto w Zarobkach = „netto ≈” dnia w Kalendarzu (do złotówki)', kal_net is not None and abs(round(zn / 100) * 100 - kal_net) <= 100, (zn, kal_net, note))
    pg.goto(URL + '/zarobki?kw=netto')
    chk('Netto: tabela i nagłówki oznaczone „(netto)”, kwoty z wizyt opisane jako brutto', 'Zarobek lekarza (netto)' in pg.inner_text('[data-testid=tabela]')
        and 'Kwoty z wizyt' in pg.inner_text('[data-testid=netto-info]'))
    KK("S().setup.zus=false;saveSettings();"); kal_saved("coalesce(data->'setup'->>'zus','false')='false'")
    pg.reload(); chk('Netto: ostrzeżenie, gdy kwota ZUS niepotwierdzona', pg.locator('[data-testid=netto-zus]').count() == 1)
    pg.goto(URL + '/zarobki?kw=netto&k=nfz')
    chk('Netto z filtrem rodzaju: informacja, bez kwot netto', 'niedostępny przy filtrze' in pg.inner_text('[data-testid=netto-info]'))

    # „Ustaw od nowa”: czyści tylko ustawienia podatków i ZUS (po potwierdzeniu), dyżury zostają
    KK("UI.tab='set';render();"); kp.wait_for_timeout(150)
    kp.click('[data-a=tax-reset-ask]'); chk('Ustaw od nowa: najpierw pytanie o potwierdzenie', kp.locator('[data-tax-reset]').count() == 1 and KK("return S().jdgStart") == MK)
    kp.click('[data-a=tax-reset-no]'); chk('„Nie” – nic nie zmienia', KK("return S().jdgStart") == MK and kp.locator('[data-tax-reset]').count() == 0)
    kp.click('[data-a=tax-reset-ask]'); kp.click('[data-a=tax-reset-do]'); kp.wait_for_timeout(200)
    chk('„Tak, wyczyść”: start, forma i ZUS puste, otwiera się kreator', KK("return S().jdgStart===''&&!Object.keys(S().regimes).length&&!S().zus.length") is True and kp.locator('#wiz').count() == 1)
    chk('…na koncie: ustawienia podatków wyczyszczone, dyżur i gabinet zostają', kal_saved("data->>'jdgStart'='' AND data->'zus'='[]'::jsonb AND data->'regimes'='{}'::jsonb")
        and 'n1' in (sql(f"SELECT data::text FROM app.calendar_docs WHERE doc='m{MK}'") or '') and KK(f"return S().clinics.some(c=>c.id==='{A}')") is True)
    pg.goto(URL + '/zarobki?kw=netto')
    chk('Zarobki po wyczyszczeniu: netto nieliczone (informacja)', 'nie są jeszcze ustawione' in pg.inner_text('[data-testid=netto-info]'))
    kp.click('[data-a=wiz-skip]'); kp.wait_for_timeout(150)
    chk('„Pomiń na razie”: kreator chowa się, zostaje przycisk „Ustaw podatki i ZUS”', kp.locator('#wiz').count() == 0 and kp.locator('button.nudge[data-a=wiz-open]').count() == 1)
    kc.close()

    # ---- katalog i nazwa modelu
    pg.goto(URL + '/katalog-nfz')
    chk('Katalog NFZ: bez „Własne kody” i „Sprawdź wycenę”', 'Własne kody' not in pg.content() and 'Sprawdź wycenę' not in pg.content())
    pg.goto(URL + '/gabinety?nowy=1')
    chk('Gabinety: „% po odjęciu kosztów własnych”, bez starej nazwy', '% po odjęciu kosztów własnych' in pg.content() and 'labu/implantów' not in pg.content())
    chk('brak błędów JavaScript', not errs, errs)
    br.close()
t.done('zmiany 21.11.2026: 2FA, brutto/netto, katalog, nazwa modelu')
