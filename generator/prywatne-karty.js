/* Karty procedur jako procedury do klikania w Opisach prywatnych (etap K1, decyzja Patryka 22.11.2026:
   wszystkie 144 karty zweryfikowane w Opisach prywatnych, blok dokumentacyjny, puste obowiązkowe → [UZUPEŁNIJ]).
   Plik aplikacji SaaS (jak opis-z-karty.js) – nie pochodzi ze starej aplikacji. Dane: window.KARTY_OPISY (generator/karty-opisy.js).
   Dokłada procedury „karta-…” do window.PRYW_KATALOG PRZED startem modułu; własne procedury Patryka (19) zostają bez zmian.
   Tekst: szablon standardowy karty (te same zasady co „Opis z karty”: zdanie bez wartości pomijane, częściowo wypełnione → [UZUPEŁNIJ]),
   + blok dokumentacyjny (rozpoznanie, znieczulenie z dawką, powikłania, informacja i zgoda pacjenta).
   Podstawy bloku: rozporządzenie MZ o dokumentacji medycznej (t.j. Dz.U. 2026 poz. 1391) § 8, § 10 pkt 4, § 38 ust. 4;
   ustawa o prawach pacjenta (t.j. Dz.U. 2024 poz. 581) art. 9, 16–18; ustawa o zawodach lekarza i lekarza dentysty
   (t.j. Dz.U. 2026 poz. 37) art. 31–34. Wszystko na urządzeniu – bez danych pacjenta poza tym, co moduł i tak zapisuje. */
(function () {
  'use strict';
  const K = window.KARTY_OPISY, P = window.PRYW_KATALOG;
  if (!K || !P || !Array.isArray(K.karty)) return;

  /* kategorie kart → kategorie Opisów prywatnych (dwie nowe: Protetyka, Znieczulenia) */
  const KMAP = { 'badanie i porada': 'diag', diagnostyka: 'diag', radiologia: 'diag', profilaktyka: 'hig', 'periodontologia i błona śluzowa': 'hig',
    'leczenie próchnicy': 'zach', 'odbudowa i estetyka': 'zach', dziecko: 'zach', 'urazy zębów': 'zach',
    'endodoncja – leczenie kanałowe': 'endo', 'endodoncja – leczenie miazgi': 'endo',
    'chirurgia – ekstrakcje': 'chir', 'chirurgia stomatologiczna': 'chir', 'chirurgia – zakażenia': 'chir', znieczulenie: 'znie' };
  const NOWE = [{ id: 'prot', name: 'Protetyka' }, { id: 'znie', name: 'Znieczulenia' }];
  NOWE.forEach(k => { if (!P.kat.some(x => x.id === k.id)) P.kat.push(k); });
  const katOf = k => KMAP[k] || (/^protetyka/.test(k) ? 'prot' : 'diag');

  /* pola kart → pola Opisów prywatnych. Znieczulenie i materiały na kluczach modułu (zn, znprep, zndawka, mat, podklad),
     żeby działały te same podpowiedzi „3 najczęstsze” i dawki ½ / 1 / 2 amp. */
  const KEY = { 'POLE-ZNIECZ-RODZAJ': 'zn', 'POLE-ZNIECZ-PREPARAT': 'znprep', 'POLE-ZNIECZ-DAWKA': 'zndawka', 'POLE-MATERIAL': 'mat', 'POLE-MATERIAL-PODKLAD': 'podklad' };
  const keyOf = id => KEY[id] || 'k_' + id.replace(/^POLE-/, '').toLowerCase().replace(/[^a-z0-9]+/g, '_');
  const BEZ_ZN = { k: 'zn', not: ['nie stosowano'] };
  const ZN_SUG = ['artykaina 4% z adrenaliną 1:100 000', 'artykaina 4% z adrenaliną 1:200 000', 'lidokaina 2% z adrenaliną', 'mepiwakaina 3% bez środka obkurczającego', 'lidokaina w żelu / aerozolu'];
  function pole(id, card) {
    const d = (K.pola || {})[id] || { e: id, t: 'tekst' }, k = keyOf(id), f = { k, l: d.e };
    switch (d.t) {
      case 'zab': f.t = 'tooth'; f.req = 1; break;
      case 'zeby': f.t = 'teeth'; f.req = 1; break;
      case 'powierzchnie': f.t = 'multi'; f.opts = ['M', 'O', 'D', 'B', 'L', 'P', 'I']; f.join = ''; break;
      case 'wybor_wielokrotny': f.t = 'multi'; f.opts = d.o || []; break;
      case 'tekst_dlugi': f.t = 'area'; break;
      case 'liczba': f.t = 'num'; break;
      case 'data': f.t = 'date'; break;
      case 'przelacznik': f.t = 'bool'; break;
      case 'wybor': if (k === 'zn') { f.t = 'select'; f.opts = d.o || []; } else { f.t = 'text'; f.sug = (d.o || []).slice(); } break;   // lista + własna wartość → przyciski i wpisywanie
      default: f.t = 'text';
    }
    if (k === 'znprep' || k === 'zndawka' || k === 'k_znieczulenie_miejsce') f.show = BEZ_ZN;
    if (k === 'zndawka') { f.t = 'num'; f.l = 'Dawka (ml)'; f.unit = 'ml'; }
    if (k === 'znprep') { f.l = 'Środek znieczulający'; f.sug = ZN_SUG.slice(); }   // jak we własnych procedurach; Dentocaine i Mark3 dokłada moduł (QBASE)
    if (k === 'k_rozpoznanie') { f.req = 1; f.l = 'Rozpoznanie / wskazanie (ICD-10)'; f.qloc = 1; f.sug = (card.icd10 || []).map(r => r[0] + ' ' + r[1]); }
    return f;
  }

  const ZT = '{{ZNIECZENIE}}.', ZABIEG = ['zach', 'endo', 'chir', 'hig', 'prot'];
  const PL = /\{\{([A-Za-z0-9_-]+)\}\}/g, NAG = /^[A-ZĄĆĘŁŃÓŚŹŻ0-9 ()–-]{4,}:\s*/;
  function procedura(c) {
    let t = String(c.szablony.standardowy || '');
    const ids = [...new Set([...t.matchAll(PL)].map(m => m[1]))];
    /* znieczulenie – jedno zdanie składane przez blok (rodzaj, preparat, dawka, miejsce) */
    if (!ids.includes('POLE-ROZPOZNANIE')) { const nag = (t.match(NAG) || [''])[0]; t = nag + 'Rozpoznanie: {{POLE-ROZPOZNANIE}}. ' + t.slice(nag.length); }
    const zn = ids.filter(id => /^POLE-ZNIECZ-/.test(id));
    if (zn.length) t = t.split(/(?<=\.)\s+/).map(z => /\{\{POLE-ZNIECZ-/.test(z) ? ZT : z).filter((z, i, a) => z !== ZT || a.indexOf(z) === i).join(' ');
    else if (ZABIEG.includes(katOf(c.kategoria))) {                    // karta zabiegowa bez pól znieczulenia – zdanie po rozpoznaniu (puste = pominięte)
      const m = t.match(/Rozpoznanie: \{\{POLE-ROZPOZNANIE\}\}\.\s*/); t = m ? t.replace(m[0], m[0] + ZT + ' ') : t + ' ' + ZT; }
    if (zn.length || t.includes(ZT)) ['POLE-ZNIECZ-RODZAJ', 'POLE-ZNIECZ-PREPARAT', 'POLE-ZNIECZ-DAWKA'].forEach(id => { if (!zn.includes(id)) zn.push(id); });
    if (!ids.includes('POLE-POWIKLANIA')) t += ' Powikłania: {{POLE-POWIKLANIA}}.';
    const uz = [...new Set([...t.matchAll(PL)].map(m => m[1]).filter(id => id !== 'ZNIECZENIE').concat(zn))];
    const fields = uz.map(id => pole(id, c));
    t = t.replace(PL, (m, id) => id === 'ZNIECZENIE' ? m : '{{' + keyOf(id) + '}}');
    fields.push(
      { k: 'dok_wiek', t: 'select', l: 'Wiek pacjenta (do informacji i zgody)', opts: ['dorosły', '16–17 lat', 'poniżej 16 lat'], def: 'dorosły' },
      { k: 'dok_inf', t: 'select', l: 'Informacja dla pacjenta', opts: ['pełna', 'krótka'], req: 1 },
      { k: 'dok_zg', t: 'select', l: 'Zgoda pacjenta', opts: ['ustna', 'pisemna', 'odmowa'], req: 1 },
      { k: 'dok_odm', t: 'text', l: 'Odmowa – na co', req: 1, show: { k: 'dok_zg', eq: 'odmowa' } });
    return { id: 'karta-' + c.kod.replace(/\./g, '_'), kat: katOf(c.kategoria), name: c.nazwa,
      desc: 'Karta ' + c.kod + (c.nfz ? ' · świadczenie gwarantowane NFZ' : '') + ' – ' + c.kategoria, fields, tpl: '', ktpl: t, karta: c.kod, zab: ZABIEG.includes(katOf(c.kategoria)) };
  }
  const ist = new Set(P.proc.map(p => p.id));
  K.karty.forEach(c => { const p = procedura(c); if (!ist.has(p.id)) { P.proc.push(p); ist.add(p.id); } });   // bez duplikatów kart

  /* ---- składanie tekstu ---- */
  const C1 = 'o stanie zdrowia, rozpoznaniu, proponowanym leczeniu i możliwych metodach alternatywnych, dających się przewidzieć następstwach ich zastosowania albo zaniechania, możliwych powikłaniach oraz rokowaniu';
  const C2 = 'o rozpoznaniu, planowanym leczeniu, metodach alternatywnych, ryzyku powikłań i rokowaniu';
  const BLOK = new Set();
  const u = l => '[UZUPEŁNIJ: ' + l + ']';
  function informacja(w, inf) {
    if (!inf) return u('Informacja dla pacjenta');
    const c = inf === 'pełna' ? C1 : C2, s = inf === 'pełna' ? ' w przystępny sposób ' : ' ';
    if (w === 'poniżej 16 lat') return 'Przedstawiciela ustawowego pacjenta poinformowano' + s + c + '. Pacjentowi udzielono informacji w zakresie i formie potrzebnej do przebiegu leczenia i wysłuchano jego zdania.';
    const kto = w === '16–17 lat' ? 'Pacjenta i jego przedstawiciela ustawowego' : 'Pacjenta';
    return kto + ' poinformowano' + s + c + '.' + (inf === 'pełna' ? ' Pacjent miał możliwość zadania pytań i przedstawienia swojego zdania.' : '');
  }
  function zgoda(w, zg, odm, zab) {
    const na = zab ? 'na zabieg' : 'na świadczenie';
    if (!zg) return u('Zgoda pacjenta');
    if (zg === 'odmowa') {
      const co = String(odm || '').trim() || u('Odmowa – na co');
      return (w === 'poniżej 16 lat' ? 'Przedstawiciel ustawowy pacjenta, poinformowany o następstwach zaniechania leczenia, nie wyraził zgody na: '
        : w === '16–17 lat' ? 'Pacjent i jego przedstawiciel ustawowy, poinformowani o następstwach zaniechania leczenia, nie wyrazili zgody na: '
        : 'Pacjent, poinformowany o następstwach zaniechania leczenia, nie wyraził zgody na: ') + co.replace(/\.$/, '') + '.';
    }
    const f = zg === 'pisemna' ? 'pisemną' : 'ustną', dol = zg === 'pisemna' ? '; oświadczenie o zgodzie dołączono do dokumentacji' : '';
    if (w === 'poniżej 16 lat') return 'Zgodę ' + f + ' ' + na + ' wyraził przedstawiciel ustawowy pacjenta' + dol + '.';
    if (w === '16–17 lat') return 'Zgodę ' + f + ' ' + na + ' wyrazili pacjent i jego przedstawiciel ustawowy' + dol + '.';
    return 'Pacjent wyraził ' + f + ' zgodę ' + na + dol + '.';
  }
  /* p – procedura; val(k) – wartość sformatowana ('' gdy pusta lub pole ukryte); lab(k) – etykieta; req(k) – czy wymagane */
  function tekst(p, val, lab, req, raw) {
    const t = String(p.ktpl || ''), nag = (t.match(NAG) || [''])[0];
    const zd = t.slice(nag.length).split(/(?<=\.)\s+/).map(z => {
      if (z === ZT) {
        const r = val('zn'); if (!r) return '';
        if (r === 'nie stosowano') return 'Znieczulenie: nie stosowano.';
        const pr = val('znprep') || u(lab('znprep')), dz = val('zndawka') ? val('zndawka') + ' ml' : u(lab('zndawka')), mi = val('k_znieczulenie_miejsce');
        return 'Znieczulenie ' + r + (mi ? ' (' + mi + ')' : '') + ': ' + pr + ', ' + dz + '.';
      }
      const ks = [...z.matchAll(PL)].map(m => m[1]);
      if (!ks.length) return z;
      if (!ks.some(k => val(k) !== '') && !ks.some(req)) return '';            // zdanie bez żadnej wartości – pomijane (chyba że pole obowiązkowe)
      return z.replace(PL, (_, k) => val(k) || u(lab(k)));
    }).filter(Boolean);
    const w = raw('dok_wiek') || 'dorosły', b = [informacja(w, raw('dok_inf')), zgoda(w, raw('dok_zg'), raw('dok_odm'), p.zab !== false)];
    b.forEach(x => BLOK.add(x));
    return [(nag + zd.join(' ')).trim()].concat(b).join('\n');
  }
  /* to samo zdanie o informacji / zgodzie przy kilku procedurach jednej wizyty – tylko raz */
  function dedupe(parts) {
    const seen = new Set();
    return parts.map(s => String(s).split('\n').filter(l => { if (!BLOK.has(l)) return true; if (seen.has(l)) return false; seen.add(l); return true; }).join('\n')).filter(Boolean);
  }
  window.KartyPryw = Object.freeze({ tekst, dedupe, liczba: K.karty.length });
})();
