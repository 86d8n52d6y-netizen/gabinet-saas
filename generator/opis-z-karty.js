/* Opis z karty procedury (etap I2 – decyzja Patryka 22.11.2026: Opisy prywatne + Opisy NFZ, domyślnie wariant standardowy,
   formularz z typami pól; etap D: zakładka „Badanie” – wybór elementów badania, zestaw zapamiętany na urządzeniu, „w normie” tylko po kliknięciu).
   Plik aplikacji SaaS (jak gabinet-saas.js) – nie pochodzi ze starej aplikacji.
   Dane: window.KARTY_OPISY (generator/karty-opisy.js ze scripts/karty_opisy_przegladarka.py) – tylko karty zweryfikowane przez Patryka.
   Składanie: nagłówek szablonu zostaje; zdanie bez żadnej wartości jest pomijane; w zdaniu wypełnionym częściowo brak = [UZUPEŁNIJ: pole]\n   (ten sam znacznik co w modułach – liczony jako „do uzupełnienia”).
   Wszystko dzieje się na urządzeniu: wpisane wartości nie są nigdzie wysyłane; gotowy tekst trafia do pola opisu modułu (edycja ręczna)
   i dalej podlega tym samym zasadom co ręcznie poprawiony opis. Generator opisu NFZ (1:1 ze starej aplikacji) pozostaje bez zmian. */
(function () {
  'use strict';
  const D = () => window.KARTY_OPISY || { karty: [], pola: {} };
  const WAR = [['standardowy', 'standardowy'], ['skrocony', 'skrócony'], ['rozszerzony', 'rozszerzony']];
  const POW = ['M', 'O', 'D', 'B', 'L', 'P', 'I'];
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const PL = /\{\{(POLE-[A-Z0-9-]+)\}\}/g;
  let host = null, st = null;
  const KLUCZ = 'gabinet:opis-badania:elementy';                       // ustawienie (bez danych pacjenta) – ostatnio użyty zestaw elementów badania
  const START = ['BAD-WYWIAD', 'BAD-ZEWNATRZUSTNE', 'BAD-WEWNATRZUSTNE', 'BAD-UZEBIENIE', 'BAD-PRZYZEBIE', 'BAD-HIGIENA'];   // pierwsze użycie: zestaw badania 23.0101
  const zestaw = () => { try { const v = JSON.parse(localStorage.getItem(KLUCZ) || 'null'); if (Array.isArray(v)) return v; } catch (_) { } return START.slice(); };
  const zapiszZestaw = a => { try { localStorage.setItem(KLUCZ, JSON.stringify(a)); } catch (_) { } };
  const NAG = /^[A-ZĄĆĘŁŃÓŚŹŻ0-9 ()–-]{4,}:\s*/;

  /* ---- składanie opisu (czysta funkcja – testowana) ---- */
  function zloz(tekst, w, etyk) {
    const val = p => String(w[p] ?? '').trim();
    const cos = z => [...z.matchAll(PL)].some(m => val(m[1]) !== '');          // zdanie bez żadnej wartości – pomijane w całości
    const nag = (tekst.match(NAG) || [''])[0];
    const zd = tekst.slice(nag.length).split(/(?<=\.)\s+/).filter(z => !z.includes('{{POLE-') || cos(z))
      .map(z => z.replace(PL, (_, p) => val(p) || '[UZUPEŁNIJ: ' + ((etyk && etyk[p]) || p) + ']'));   // częściowo wypełnione – znacznik jak w module
    return (nag + zd.join(' ')).trim();
  }
  function polaKarty(k, war) { return [...new Set([...k.szablony[war].matchAll(PL)].map(m => m[1]))]; }

  /* ---- style (własne klasy ozk-*, zmienne kolorów modułu z wartościami zapasowymi) ---- */
  function css() {
    if (document.getElementById('ozk-css')) return;
    const s = document.createElement('style'); s.id = 'ozk-css';
    s.textContent = '.ozk-bg{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:9999;display:flex;align-items:flex-start;justify-content:center;overflow:auto;padding:16px}' +
      '.ozk{background:var(--g-surface,var(--card,#fff));color:var(--g-ink,var(--ink,#1d2433));border-radius:12px;max-width:720px;width:100%;padding:16px;box-shadow:0 10px 40px rgba(0,0,0,.3);font:inherit}' +
      '.ozk h2{margin:0 0 4px;font-size:18px;display:flex;justify-content:space-between;gap:8px}.ozk .ozk-n{font-size:13px;opacity:.75;margin:0 0 10px}' +
      '.ozk label{display:block;font-size:13px;opacity:.85;margin:10px 0 4px}.ozk input,.ozk select,.ozk textarea{width:100%;box-sizing:border-box;padding:8px 10px;border:1px solid var(--g-line,var(--line,#ccd));border-radius:8px;background:inherit;color:inherit;font:inherit}' +
      '.ozk textarea{min-height:56px;resize:vertical}.ozk .ozk-g{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}@media(max-width:560px){.ozk .ozk-g{grid-template-columns:1fr}}' +
      '.ozk .ozk-seg{display:flex;flex-wrap:wrap;gap:6px}.ozk .ozk-seg button{border:1px solid var(--g-line,var(--line,#ccd));background:inherit;color:inherit;border-radius:999px;padding:5px 12px;font:inherit;font-size:13px;cursor:pointer}' +
      '.ozk .ozk-seg button[aria-pressed=true]{background:var(--g-accent,var(--acc,#2f6fed));border-color:var(--g-accent,var(--acc,#2f6fed));color:#fff}' +
      '.ozk .ozk-lst{max-height:220px;overflow:auto;border:1px solid var(--g-line,var(--line,#ccd));border-radius:8px;margin-top:6px}.ozk .ozk-lst button{display:block;width:100%;text-align:left;border:0;border-bottom:1px solid var(--g-line,var(--line,#eee));background:inherit;color:inherit;padding:7px 10px;font:inherit;cursor:pointer}' +
      '.ozk .ozk-lst button:hover,.ozk .ozk-lst button:focus{background:rgba(47,111,237,.1)}.ozk .ozk-pv{white-space:pre-wrap;background:rgba(47,111,237,.08);border-radius:8px;padding:10px 12px;margin-top:4px;min-height:40px}' +
      '.ozk .ozk-b{display:flex;gap:8px;justify-content:flex-end;margin-top:12px;flex-wrap:wrap}.ozk .ozk-b button{padding:9px 16px;border-radius:8px;font:inherit;font-weight:600;cursor:pointer;border:1px solid var(--g-accent,var(--acc,#2f6fed))}' +
      '.ozk .ozk-ok{background:var(--g-accent,var(--acc,#2f6fed));color:#fff}.ozk .ozk-no{background:inherit;color:inherit}.ozk .ozk-chk{display:flex;gap:10px;flex-wrap:wrap}.ozk .ozk-chk label{display:flex;gap:4px;align-items:center;margin:0;font-size:14px;opacity:1}.ozk .ozk-chk input{width:auto}';
    document.head.appendChild(s);
  }

  /* ---- pola formularza wg typu ---- */
  function poleHTML(f, k) {
    const d = D().pola[f] || { e: f, t: 'tekst' }, v = st.w[f] ?? '', id = 'ozk-' + f;
    const lab = '<label for="' + id + '">' + esc(d.e) + '</label>';
    if (f === 'POLE-ROZPOZNANIE' && k.icd10.length)
      return lab + '<input id="' + id + '" data-f="' + f + '" list="ozk-icd" value="' + esc(v) + '" placeholder="wybierz z podpowiedzi albo wpisz">' +
        '<datalist id="ozk-icd">' + k.icd10.map(r => '<option value="' + esc(r[0] + (r[1] ? ' ' + r[1] : '')) + '">' + esc(r[2] || '') + '</option>').join('') + '</datalist>';
    switch (d.t) {
      case 'wybor': return lab + '<select id="' + id + '" data-f="' + f + '"><option value="">— (pomiń zdanie)</option>' + (d.o || []).map(o => '<option' + (o === v ? ' selected' : '') + '>' + esc(o) + '</option>').join('') + '</select>';
      case 'wybor_wielokrotny': { const sel = String(v).split(', ').filter(Boolean);
        return '<label>' + esc(d.e) + '</label><div class="ozk-chk">' + (d.o || []).map((o, i) => '<label><input type="checkbox" data-fm="' + f + '" value="' + esc(o) + '"' + (sel.includes(o) ? ' checked' : '') + ' id="' + id + '-' + i + '">' + esc(o) + '</label>').join('') + '</div>'; }
      case 'powierzchnie': { const sel = String(v);
        return '<label>' + esc(d.e) + '</label><div class="ozk-seg" role="group" aria-label="' + esc(d.e) + '">' + POW.map(p => '<button type="button" data-pw="' + f + '" data-v="' + p + '" aria-pressed="' + sel.includes(p) + '">' + p + '</button>').join('') + '</div>'; }
      case 'przelacznik': return '<label class="ozk-chk"><input type="checkbox" data-fp="' + f + '" id="' + id + '"' + (v ? ' checked' : '') + '> ' + esc(d.e) + '</label>';
      case 'tekst_dlugi': return lab + '<textarea id="' + id + '" data-f="' + f + '">' + esc(v) + '</textarea>';
      case 'liczba': return lab + '<input id="' + id + '" data-f="' + f + '" inputmode="decimal" value="' + esc(v) + '">';
      case 'data': return lab + '<input id="' + id + '" data-f="' + f + '" type="date" value="' + esc(v) + '">';
      case 'zab': return lab + '<input id="' + id + '" data-f="' + f + '" inputmode="numeric" placeholder="np. 36" value="' + esc(v) + '">';
      default: return lab + '<input id="' + id + '" data-f="' + f + '" value="' + esc(v) + '">';
    }
  }

  const etyk = () => { const P = D().pola; return Object.fromEntries(Object.keys(P).map(f => [f, P[f].e.toLowerCase()])); };
  function badanieTekst(b, war, w, norma, et) {                         // jeden element badania; pusty, gdy nic nie wpisano
    const tpl = b.szablony[war], nag = (tpl.match(NAG) || [''])[0];
    if (norma) return ((nag || b.nazwa + ': ') + b.norma).trim();
    const t = zloz(tpl, w, et);
    return [...tpl.matchAll(PL)].some(m => String(w[m[1]] ?? '').trim() !== '') ? t : '';
  }
  function tekst() {
    if (st.tab === 'badanie') { const et = etyk(); return D().badania.filter(b => st.bsel.includes(b.id)).map(b => badanieTekst(b, st.war, st.w, st.norma.includes(b.id), et)).filter(Boolean).join('\n'); }
    const k = st.k; return k ? zloz(k.szablony[st.war], st.w, etyk()) : '';
  }
  function rysuj() {
    const box = document.getElementById('ozk-box'); if (!box) return;
    const k = st.k;
    let h = '<h2><span>Opis z karty procedury</span><button type="button" class="ozk-no" data-ozk-x aria-label="Zamknij" style="border:0;background:none;font-size:20px;cursor:pointer;color:inherit">×</button></h2>' +
      '<p class="ozk-n">Tylko karty zatwierdzone przez Ciebie. Zdanie bez wartości jest pomijane; brak w częściowo wypełnionym zdaniu = [UZUPEŁNIJ]. Tekst trafi do opisu – możesz go poprawić przed zapisem.</p>';
    h += '<div class="ozk-seg" role="tablist" aria-label="Rodzaj opisu" style="margin-bottom:8px">' + [['karta', 'Karta procedury'], ['badanie', 'Badanie']].map(([t, n]) => '<button type="button" role="tab" data-ozk-tab="' + t + '" data-testid="ozk-tab-' + t + '" aria-pressed="' + (st.tab === t) + '" aria-selected="' + (st.tab === t) + '">' + n + '</button>').join('') + '</div>';
    if (st.tab === 'badanie') {
      const B = D().badania, wyb = B.filter(b => st.bsel.includes(b.id));
      h += '<label>Elementy badania – zaznacz, co ma trafić do opisu <span style="opacity:.7">(wybór zapamiętany na tym urządzeniu)</span></label>' +
        '<div class="ozk-chk" data-testid="ozk-elementy">' + B.map(b => '<label><input type="checkbox" data-bsel="' + b.id + '"' + (st.bsel.includes(b.id) ? ' checked' : '') + '>' + esc(b.nazwa) + '</label>').join('') + '</div>' +
        '<label>Wariant opisu</label><div class="ozk-seg" role="group" aria-label="Wariant opisu" data-testid="ozk-warianty">' + WAR.map(([w, n]) => '<button type="button" data-war="' + w + '" aria-pressed="' + (w === st.war) + '">' + n + '</button>').join('') + '</div>' +
        wyb.map(b => { const n = st.norma.includes(b.id), P = [...new Set([...b.szablony[st.war].matchAll(PL)].map(m => m[1]))];
          return '<section style="border-top:1px solid var(--g-line,var(--line,#ddd));margin-top:12px;padding-top:8px" data-testid="ozk-el-' + b.id + '"><h3 style="margin:0;font-size:15px;display:flex;justify-content:space-between;align-items:center;gap:8px">' + esc(b.pelna) +
            '<span class="ozk-seg"><button type="button" data-norma="' + b.id + '" aria-pressed="' + n + '" title="Wstawia przykład wyniku prawidłowego z karty badania">w normie' + (n ? ' ✓' : '') + '</button></span></h3>' +
            (n ? '<p style="margin:6px 0 0;opacity:.85">' + esc(b.norma) + '</p>' : '<div class="ozk-g">' + P.map(f => '<div>' + poleHTML(f, { icd10: [] }) + '</div>').join('') + '</div>') + '</section>'; }).join('') +
        (wyb.length ? '' : '<p style="opacity:.75">Zaznacz co najmniej jeden element badania.</p>') +
        '<label>Podgląd</label><div class="ozk-pv" data-testid="ozk-podglad" id="ozk-pv">' + esc(tekst()) + '</div>' +
        '<div class="ozk-b"><button type="button" class="ozk-no" data-ozk-x>Anuluj</button><button type="button" class="ozk-ok" data-ozk-wstaw data-testid="ozk-wstaw">Wstaw do opisu</button></div>';
    } else if (!k) {
      const q = st.q.trim().toLowerCase(), L = D().karty.filter(x => !q || (x.kod + ' ' + x.nazwa + ' ' + x.kategoria).toLowerCase().includes(q)).slice(0, 60);
      h += '<label for="ozk-q">Szukaj karty (kod ICD-9 albo nazwa)</label><input id="ozk-q" data-testid="ozk-szukaj" value="' + esc(st.q) + '" placeholder="np. 23.1503 albo odbudowa" autocomplete="off">' +
        '<div class="ozk-lst" data-testid="ozk-lista">' + (L.length ? L.map(x => '<button type="button" data-k="' + esc(x.id) + '"><b>' + esc(x.kod) + '</b> ' + esc(x.nazwa) + ' <span style="opacity:.6;font-size:12px">' + esc(x.kategoria) + (x.nfz ? ' · NFZ' : '') + '</span></button>').join('') : '<p style="padding:8px 10px;margin:0">Brak kart dla „' + esc(st.q) + '”.</p>') + '</div>' +
        '<div class="ozk-b"><button type="button" class="ozk-no" data-ozk-x>Anuluj</button></div>';
    } else {
      const P = polaKarty(k, st.war);
      h += '<p style="margin:4px 0"><b>' + esc(k.kod) + '</b> ' + esc(k.nazwa) + ' <button type="button" class="ozk-no" data-ozk-zm style="border:0;background:none;color:inherit;text-decoration:underline;cursor:pointer">zmień kartę</button></p>' +
        '<label>Wariant opisu</label><div class="ozk-seg" role="group" aria-label="Wariant opisu" data-testid="ozk-warianty">' + WAR.map(([w, n]) => '<button type="button" data-war="' + w + '" aria-pressed="' + (w === st.war) + '">' + n + '</button>').join('') + '</div>' +
        '<div class="ozk-g">' + P.map(f => '<div>' + poleHTML(f, k) + '</div>').join('') + '</div>' +
        '<label>Podgląd</label><div class="ozk-pv" data-testid="ozk-podglad" id="ozk-pv">' + esc(tekst()) + '</div>' +
        '<div class="ozk-b"><button type="button" class="ozk-no" data-ozk-x>Anuluj</button><button type="button" class="ozk-ok" data-ozk-wstaw data-testid="ozk-wstaw">Wstaw do opisu</button></div>';
    }
    box.innerHTML = h;
  }
  const odswiezPodglad = () => { const pv = document.getElementById('ozk-pv'); if (pv) pv.textContent = tekst(); };
  function zamknij() { const bg = document.getElementById('ozk-bg'); if (bg) bg.remove(); document.removeEventListener('keydown', klaw); if (st && st.focus) try { st.focus.focus(); } catch (_) { } st = null; }
  function klaw(e) { if (e.key === 'Escape') zamknij(); }

  function otworz() {
    if (!host) return;
    const ok = host.moze ? host.moze() : true;
    if (ok !== true) { alert(typeof ok === 'string' ? ok : 'Nie można teraz wstawić opisu.'); return; }
    css(); st = { tab: 'karta', k: null, war: 'standardowy', w: {}, q: '', bsel: zestaw(), norma: [], focus: document.activeElement };
    const bg = document.createElement('div'); bg.className = 'ozk-bg'; bg.id = 'ozk-bg';
    bg.innerHTML = '<div class="ozk" id="ozk-box" role="dialog" aria-modal="true" aria-label="Opis z karty procedury" data-testid="ozk"></div>';
    document.body.appendChild(bg); rysuj(); document.addEventListener('keydown', klaw);
    const q = document.getElementById('ozk-q'); if (q) q.focus();
    bg.addEventListener('click', e => {
      const t = e.target;
      if (t === bg || t.closest('[data-ozk-x]')) return zamknij();
      const kb = t.closest('[data-k]'); if (kb) { st.k = D().karty.find(x => x.id === kb.dataset.k) || null; st.w = {}; rysuj(); return; }
      if (t.closest('[data-ozk-zm]')) { st.k = null; rysuj(); const q2 = document.getElementById('ozk-q'); if (q2) q2.focus(); return; }
      const tb = t.closest('[data-ozk-tab]'); if (tb) { st.tab = tb.dataset.ozkTab; rysuj(); return; }
      const nb = t.closest('[data-norma]'); if (nb) { const id = nb.dataset.norma; st.norma = st.norma.includes(id) ? st.norma.filter(x => x !== id) : st.norma.concat(id); rysuj(); return; }
      const wb = t.closest('[data-war]'); if (wb) { st.war = wb.dataset.war; rysuj(); return; }
      const pb = t.closest('[data-pw]'); if (pb) { const f = pb.dataset.pw, cur = String(st.w[f] || ''), p = pb.dataset.v;
        st.w[f] = POW.filter(x => x === p ? !cur.includes(p) : cur.includes(x)).join(''); pb.setAttribute('aria-pressed', String(st.w[f].includes(p))); odswiezPodglad(); return; }
      if (t.closest('[data-ozk-wstaw]')) { const tx = tekst(); if (!tx) return; if (st.tab === 'badanie') zapiszZestaw(st.bsel); const h = host; zamknij(); h.wstaw(tx); }
    });
    bg.addEventListener('input', e => {
      const t = e.target;
      if (t.id === 'ozk-q') { st.q = t.value; const pos = t.selectionStart; rysuj(); const q2 = document.getElementById('ozk-q'); if (q2) { q2.focus(); q2.setSelectionRange(pos, pos); } return; }
      if (t.dataset.f) { st.w[t.dataset.f] = t.value; odswiezPodglad(); return; }
    });
    bg.addEventListener('change', e => {
      const t = e.target;
      if (t.dataset.f) { st.w[t.dataset.f] = t.value; odswiezPodglad(); }
      if (t.dataset.fm) { const f = t.dataset.fm; st.w[f] = [...document.querySelectorAll('[data-fm="' + f + '"]:checked')].map(x => x.value).join(', '); odswiezPodglad(); }
      if (t.dataset.fp) { st.w[t.dataset.fp] = t.checked ? 'tak' : ''; odswiezPodglad(); }
      if (t.dataset.bsel) { const id = t.dataset.bsel, B = D().badania.map(b => b.id); st.bsel = B.filter(x => x === id ? t.checked : st.bsel.includes(x)); zapiszZestaw(st.bsel); rysuj(); }
    });
  }

  document.addEventListener('click', e => { if (e.target.closest && e.target.closest('[data-ozk-otworz]')) { e.preventDefault(); otworz(); } });

  window.OpisZKarty = Object.freeze({
    /* host: { wstaw(tekst) – dopisuje tekst do opisu modułu, moze() – true albo komunikat, gdy wstawienie niemożliwe } */
    podlacz: h => { host = h; },
    przycisk: (klasa) => '<button type="button" class="' + (klasa || '') + '" data-ozk-otworz data-testid="ozk-otworz">Opis z karty / badanie</button>',
    zloz, otworz, badanieTekst
  });
})();
