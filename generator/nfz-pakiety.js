/* Zakładka „NFZ” (etap E4a) – rozpoznawanie pakietów i wycena punktowa wizyty z wybranych kart procedur (kody ICD-9).
   Plik aplikacji SaaS – nie pochodzi ze starej aplikacji; Opisy NFZ (generator/nfz.html) z niego NIE korzystają.
   Dane: window.NFZ_PAKIETY_DANE (generator/nfz-pakiety-dane.js, scripts/nfz_pakiety_przegladarka.py).

   Zasady (te same co w Opisach NFZ – nfzPoints() w generator/nfz.html; zarz. 60/2023/DSOZ z późn. zm.):
   – pakiet = procedura kierunkowa + listy dodatkowe ST1–ST5 z zał. 1d (95/2026/DSOZ, zał. 2); procedura z listy pakietu
     obecnego na wizycie jest jego składową: 0 pkt („w pakiecie STxx”), bez osobnego rozliczenia;
   – lista wymagana (np. ST1 – znieczulenie) bez procedury z tej listy → błąd: NFZ nie zapłaci za pakiet;
   – § 12 ust. 2 i 2a: ×1,5 do ukończenia 18 r.ż. (nie dotyczy ST30D–ST30G); § 12 ust. 3: ×1,2 ciąża / połóg;
   – § 13 ust. 1 pkt 5 i 5a: kilka pakietów na wizycie – najwyżej wyceniony ×1,0, kolejne ×0,8 (1 pakiet = 1 ząb / ćwiartka /
     ½ łuku); ST30E i ST30G zawsze ×1,0;
   – „nie sumuje się z” / „można dosumować wyłącznie” – z zał. 1d → błąd;
   – świadczenia jednostkowe (zał. 1b): liczone tylko te, które Patryk rozlicza w Opisach NFZ; pozostałe – punkty widoczne,
     nie wliczane do sumy do czasu weryfikacji.
   Wejście: poz = [{ kod: '23.1702', n: 2, wariant: 'ST30B'?, zn: '23.0403'? }], opcje { wiek: liczba|null, ciaza: bool }. */
(function (root, f) { const api = f(); if (typeof module === 'object' && module.exports) module.exports = api; else root.NfzPakiety = api; })(this, function () {
  'use strict';
  const SPECJ = ['ST33A', 'ST34A', 'ST30B', 'ST30C'];
  const WLASNY = { '23.1809': 'ST27', '23.1812': 'ST07', '23.1815': 'ST31', '23.1620': 'ST32' };   // własny pakiet, gdy nie jest składową innego
  const r2 = x => Math.round(x * 100) / 100;
  const fmt = x => String(r2(x)).replace('.', ',');

  function licz(D, poz, o) {
    o = o || {}; const wiek = typeof o.wiek === 'number' && isFinite(o.wiek) ? o.wiek : null;
    const P = D.pakiety, L = D.listy, J = D.jednostkowe;
    const listOf = c => Object.keys(L).filter(k => L[k].includes(c));
    /* 1. pozycje: karta + znieczulenie wybrane w karcie (jako osobna procedura ICD-9) */
    const e = [];
    (poz || []).forEach((p, i) => {
      if (!p || !p.kod) return; const n = Math.max(1, Math.floor(Number(p.n) || 1));
      e.push({ i, kod: p.kod, n, w: p.wariant || '', st: null });
      if (p.zn) e.push({ i, kod: p.zn, n: 1, w: '', st: null, zn: true });
    });
    const has = c => e.some(x => x.kod === c);
    const free = c => e.find(x => x.kod === c && !x.st);
    const inst = [];                                         // pakiety: { id, q, z: [i] }
    const addPkg = (id, q, x) => { let r = inst.find(t => t.id === id); if (!r) { r = { id, q: 0, z: [] }; inst.push(r); } r.q += q; if (!r.z.includes(x.i)) r.z.push(x.i); };
    const sklad = (x, id) => { x.st = { typ: 'sklad', pak: id }; };
    const bledy = [], ostrz = [], info = [];
    /* 2a. pakiety z procedur kierunkowych – najpierw higienizacja i uraz (zabierają 23.0101 / 23.02 niezależnie od kolejności kart) */
    const PIERW = ['23.16011', '23.16021', '23.0107'];
    e.filter(x => PIERW.includes(x.kod)).concat(e.filter(x => !PIERW.includes(x.kod))).forEach(x => {
      if (x.st) return; const c = x.kod;
      if (c === '23.16011') {
        const b = free('23.0101');
        if (b) { addPkg('ST30D', 1, x); sklad(b, 'ST30D'); if (x.n > 1) addPkg('ST30E', x.n - 1, x); }
        else addPkg('ST30E', x.n, x);
        x.st = { typ: 'pak' }; return;
      }
      if (c === '23.16021') { const b = free('23.0101'); if (b) { addPkg('ST30F', x.n, x); sklad(b, 'ST30F'); } else addPkg('ST30G', x.n, x); x.st = { typ: 'pak' }; return; }
      if (c === '23.16012') { addPkg(['ST30', 'ST30B', 'ST30C'].includes(x.w) ? x.w : 'ST30', x.n, x); x.st = { typ: 'pak' }; return; }
      if (c === '23.0107') { const b = free('23.02'); addPkg('ST28', x.n, x); x.st = { typ: 'pak' };
        if (b) sklad(b, 'ST28'); else bledy.push('ST28 wymaga też 23.02 (badanie żywotności zęba) – bez niego NFZ nie zapłaci za ST28.'); return; }
      if (WLASNY[c] || listOf(c).length) return;                  // decyzja w kroku 2b (składowa albo własny pakiet / jednostkowe)
      if (c === '23.1605') { addPkg('ST26', x.n, x); x.st = { typ: 'pak' }; return; }
      const ids = Object.keys(P).filter(id => P[id].kier.includes(c) && !['ST30D', 'ST30F', 'ST33', 'ST33A', 'ST34', 'ST34A'].includes(id));
      if (c === '23.0101' || c === '23.0102') { const id = c === '23.0101' ? (x.w === 'ST33A' ? 'ST33A' : 'ST33') : (x.w === 'ST34A' ? 'ST34A' : 'ST34'); addPkg(id, x.n, x); x.st = { typ: 'pak' }; return; }
      if (ids.length === 1) { addPkg(ids[0], x.n, x); x.st = { typ: 'pak' }; }
    });
    /* 2b. procedury z list dodatkowych: składowa pakietu obecnego na wizycie, inaczej własny pakiet lub świadczenie jednostkowe */
    const pakList = id => P[id].wym.concat(P[id].opc);
    e.forEach(x => {
      if (x.st) return; const ls = listOf(x.kod);
      /* znieczulenie wybrane w karcie należy do TEJ procedury: składowa tylko jej pakietu; przy świadczeniu jednostkowym
         (np. wypełnienie) – rozliczane osobno jak w Opisach NFZ (nie „wpada” do pakietu innej procedury wizyty) */
      const host = inst.find(t => (!x.zn || t.z.includes(x.i)) && (pakList(t.id).some(l => ls.includes(l)) || (P[t.id].kody_opc || []).includes(x.kod)));
      if (host) { sklad(x, host.id); return; }
      if (x.zn) return;
      if (x.kod === '23.1815' && x.w === 'ST26') { addPkg('ST26', x.n, x); x.st = { typ: 'pak' }; return; }
      if (WLASNY[x.kod]) { addPkg(WLASNY[x.kod], x.n, x); x.st = { typ: 'pak' }; }
    });
    /* składowe ST2 itp. zgłoszone po utworzeniu pakietu z 2b (np. 23.1815 przy ST27) */
    e.forEach(x => { if (x.st || x.zn) return; const ls = listOf(x.kod); const host = inst.find(t => pakList(t.id).some(l => ls.includes(l)) || (P[t.id].kody_opc || []).includes(x.kod)); if (host) sklad(x, host.id); });
    /* 2c. świadczenia jednostkowe */
    const jed = [], nie = [];
    e.forEach(x => {
      if (x.st) return; const j = J[x.kod];
      if (j && j.znane) { let r = jed.find(t => t.kod === x.kod); if (!r) { r = { kod: x.kod, q: 0, z: [] }; jed.push(r); } r.q += x.n; if (!r.z.includes(x.i)) r.z.push(x.i); x.st = { typ: 'jed' }; }
      else { nie.push({ i: x.i, kod: x.kod, pkt: j ? j.pkt : null, nazwa: j ? j.nazwa : '',
        powod: j ? 'zał. 1b: ' + j.pkt + ' pkt – zakres umowy do potwierdzenia; nie wliczone do sumy' : 'brak wyceny NFZ w danych – nie wliczone' }); x.st = { typ: 'nie' }; }
    });
    /* 3. zasady łączenia */
    const ids = inst.map(t => t.id), billed = ids.concat(jed.map(t => t.kod));
    const obecne = c => ids.includes(c) || jed.some(t => t.kod === c) || has(c);
    inst.forEach(t => {
      const p = P[t.id];
      p.wym.forEach(l => { if (!e.some(x => L[l].includes(x.kod))) bledy.push(t.id + ' wymaga procedury z listy ' + l + ' (' + L[l].join(', ') + ') – bez niej NFZ nie zapłaci za ' + t.id + (l === 'ST1' ? ' (wymóg nie dotyczy znieczulenia ogólnego).' : '.')); });
      p.nie.forEach(c => { if (c !== t.id && obecne(c) && !(c === '23.1006' && !ids.includes(t.id))) {
        const k = [t.id, c].sort().join(' + '); if (!bledy.some(b => b.startsWith(k))) bledy.push(k + ': nie sumują się (zał. 1d) – NFZ nie zapłaci za oba; usuń jedno.'); } });
      if (p.tylko.length) { const inne = billed.filter(c => c !== t.id && !p.tylko.includes(c)); if (inne.length) bledy.push('Do ' + t.id + ' można dosumować wyłącznie ' + p.tylko.join(' i ') + ' (zał. 1d) – NFZ nie zapłaci za: ' + inne.join(', ') + '.'); }
      if (p.wiek_max && wiek !== null && wiek >= p.wiek_max) ostrz.push(t.id + ' – świadczenie dla dzieci i młodzieży do ukończenia ' + p.wiek_max + ' r.ż. (wiek ' + wiek + ' lat).');
      if (SPECJ.includes(t.id)) info.push(t.id + ' – tylko w zakresach specjalistycznych (periodontologia / chirurgia i periodontologia).');
      if (p.limit) info.push(t.id + ' – limit: ' + p.limit + '.');
    });
    const e3 = inst.find(t => t.id === 'ST30E');
    if (e3) { const max = ids.includes('ST30D') ? 3 : 4; if (e3.q > max) ostrz.push('ST30E: maks. za ' + max + ' × ST30E' + (max === 3 ? ' przy ST30D' : '') + ' (zał. 1d) – NFZ nie zapłaci za nadmiar.'); }
    if (wiek === null) ostrz.push('Nie wpisano wieku – wycena bez współczynnika ×1,5 dla dzieci i młodzieży do 18 r.ż.');
    /* 4. punkty – jak nfzPoints() w Opisach NFZ */
    const coef = c => { if (wiek !== null && wiek < 18) return D.bez15.includes(c) ? [1, 'bez ×1,5'] : [1.5, '×1,5']; if (wiek !== null && o.ciaza) return [1.2, '×1,2']; return [1, '']; };
    const wiersze = [], li = [];
    inst.forEach(t => { const [k, kn] = coef(t.id); const r = { kod: t.id, pkg: true, q: t.q, base: P[t.id].pkt, k, kn, n10: t.q, n08: 0, z: t.z }; wiersze.push(r);
      if (!D.bez08.includes(t.id)) for (let i = 0; i < t.q; i++) li.push({ r, v: r.base * r.k }); });
    if (li.length > 1) { const top = li.reduce((m, x) => x.v > m.v ? x : m, li[0]);
      wiersze.forEach(r => { if (r.pkg && !D.bez08.includes(r.kod)) { r.n10 = 0; r.n08 = r.q; } }); top.r.n10 = 1; top.r.n08 -= 1; }
    jed.forEach(t => { const [k, kn] = coef(t.kod); wiersze.push({ kod: t.kod, pkg: false, q: t.q, base: J[t.kod].pkt, k, kn, n10: t.q, n08: 0, z: t.z, nazwa: J[t.kod].nazwa }); });
    wiersze.forEach(r => { r.pts = r2(r.base * r.k * (r.n10 + 0.8 * r.n08)); });
    const skladowe = e.filter(x => x.st && x.st.typ === 'sklad').map(x => ({ i: x.i, kod: x.kod, pakiet: x.st.pak, zn: !!x.zn }));
    return { wiersze, skladowe, nieliczone: nie, bledy, ostrz, info: [...new Set(info)], suma: r2(wiersze.reduce((s, r) => s + r.pts, 0)) };
  }
  function opisWiersza(r) { if (!r.pkg) return 'jednostkowe'; if (r.n08 === 0) return r.q > 1 ? r.q + '×1,0' : '×1,0'; if (r.n10) return '1×1,0 + ' + r.n08 + '×0,8'; return r.q > 1 ? r.n08 + '×0,8' : '×0,8'; }
  return Object.freeze({ licz, opisWiersza, fmt });
});
