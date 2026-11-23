# -*- coding: utf-8 -*-
"""Zakładka „NFZ” (etap E4): dane pakietów i świadczeń jednostkowych dla przeglądarki → generator/nfz-pakiety-dane.js.

Źródło: data/nfz/products.json (zał. 1b – Zarządzenie 44/2025/DSOZ; zał. 1c i skład pakietów z zał. 1d – Zarządzenie
95/2026/DSOZ, zał. 2, zatwierdzony przez Patryka 22.11.2026). Bez danych pacjentów.
Świadczenia jednostkowe „znane” = te, które Patryk rozlicza w Opisach NFZ (obiekt PTS i PTS_AN w generator/nfz.html) –
liczone do sumy; pozostałe z zał. 1b pokazywane z punktami, ale NIE wliczane do sumy do czasu weryfikacji przez Patryka.

    python3 scripts/nfz_pakiety_przegladarka.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'generator' / 'nfz-pakiety-dane.js'
ZNANE = ['23.1101', '23.1006', '23.1105', '23.1108', '23.1206', '23.1502', '23.1503', '23.1504', '23.1505', '23.0401', '23.0402', '23.0403']
# Listy dodatkowe wszystkich pakietów przepisane z zał. 1d (zał. 2 do 95/2026/DSOZ – plik od Patryka, skład zatwierdzony 22.11.2026):
# (wymagane, opcjonalne). products.json ma część list – skrypt sprawdza zgodność (dane ⊆ tabela) i używa tabeli.
L1D = {'ST01': ('ST1', 'ST2'), 'ST02': ('ST1', 'ST2'), 'ST03': ('ST1', 'ST2'), 'ST04': ('ST1', 'ST2 ST3'), 'ST05': ('ST1', 'ST2 ST3'),
       'ST06': ('ST1', 'ST2'), 'ST07': ('ST1', ''), 'ST08': ('ST1', 'ST2'), 'ST09': ('ST1', 'ST2'), 'ST10': ('ST1', 'ST2'), 'ST11': ('ST1', 'ST2'),
       'ST12': ('ST1', 'ST2'), 'ST13': ('ST1', 'ST2'), 'ST14': ('ST1', 'ST2'), 'ST15': ('ST1', 'ST2'), 'ST16': ('ST1', 'ST2'), 'ST17': ('ST1', 'ST2'),
       'ST18': ('ST1', 'ST2'), 'ST19': ('ST1', ''), 'ST20': ('ST1', ''), 'ST21': ('ST1', 'ST2'), 'ST22': ('ST1', ''), 'ST23': ('', 'ST1'),
       'ST24': ('', 'ST1'), 'ST25': ('', 'ST1'), 'ST26': ('', ''), 'ST27': ('', 'ST1'), 'ST28': ('', ''), 'ST29': ('', ''),
       'ST30': ('', 'ST1 ST4'), 'ST30A': ('', 'ST1 ST4'), 'ST30B': ('', 'ST1 ST4'), 'ST30C': ('', 'ST1 ST4'), 'ST30D': ('', 'ST5'), 'ST30E': ('', 'ST5'),
       'ST30F': ('', 'ST5'), 'ST30G': ('', 'ST5'), 'ST31': ('', 'ST1 ST4'), 'ST32': ('', 'ST1 ST4'), 'ST33': ('', ''), 'ST33A': ('', ''),
       'ST34': ('', ''), 'ST34A': ('', '')}
KODY_OPC = {'ST27': ['23.1815']}   # zał. 1d: do ST27 możliwe ST1 oraz 23.1815 (nie cała lista ST2)
BEZ15 = ['ST30D', 'ST30E', 'ST30F', 'ST30G']      # § 12 ust. 2a zarz. 60/2023/DSOZ (95/2026/DSOZ) – jak PTS_NO15 w Opisach NFZ
BEZ08 = ['ST30E', 'ST30G']                        # § 13 ust. 1 pkt 5a – jak PTS_NO08 w Opisach NFZ


def zbuduj():
    d = json.loads((ROOT / 'data' / 'nfz' / 'products.json').read_text(encoding='utf-8'))
    if set(L1D) != {p['id'] for p in d['pakiety_zal_1c_1d']}:
        raise SystemExit('tabela L1D nie obejmuje wszystkich pakietów')
    pak = {}
    for p in d['pakiety_zal_1c_1d']:
        s = p.get('sklad') or {}
        wym, opc = (L1D[p['id']][0].split(), L1D[p['id']][1].split())
        if not set(s.get('wymagane_listy') or []) <= set(wym) or not set(s.get('opcjonalne_listy') or []) <= set(opc):
            raise SystemExit(f"{p['id']}: listy w products.json niezgodne z zał. 1d")
        pak[p['id']] = {'pkt': p['punkty'], 'kier': s.get('kierunkowa') or [], 'jednaz': s.get('tryb') == 'jedna z',
                        'wym': wym, 'opc': opc, 'kody_opc': KODY_OPC.get(p['id'], []), 'nie': s.get('nie_sumuje_z') or [], 'tylko': s.get('tylko_sumuje_z') or [],
                        'limit': s.get('limit') or '', 'min': s.get('czas_min'), 'wiek_max': s.get('wiek_max_wylacznie')}
    jedn = {}
    for j in d['jednostkowe_zal_1b']:
        k = j.get('kod_icd9')
        if k and k not in jedn:
            jedn[k] = {'pkt': j['punkty'], 'nazwa': j['nazwa'], 'znane': k in ZNANE}
    brak = [k for k in ZNANE if k not in jedn]
    if brak:
        raise SystemExit('brak świadczeń jednostkowych w danych: ' + ', '.join(brak))
    return {'stan_na': d.get('stan_na'), 'zrodlo': 'Zał. 1b – Zarządzenie 44/2025/DSOZ; zał. 1c i 1d – Zarządzenie 95/2026/DSOZ (skład 1d zatwierdzony przez Patryka 22.11.2026)',
            'pakiety': pak, 'listy': d['listy_pomocnicze_zal_1d'], 'jednostkowe': jedn, 'bez15': BEZ15, 'bez08': BEZ08}


def zapisz():
    t = ('/* Wygenerowane przez scripts/nfz_pakiety_przegladarka.py z data/nfz/products.json – NIE EDYTUJ RĘCZNIE. Bez danych pacjentów. */\n'
         'window.NFZ_PAKIETY_DANE=Object.freeze(' + json.dumps(zbuduj(), ensure_ascii=False, separators=(',', ':')) + ');\n')
    OUT.write_text(t, encoding='utf-8')
    return OUT


if __name__ == '__main__':
    print('zapisano', zapisz().relative_to(ROOT))
