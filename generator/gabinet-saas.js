/* Gabinet SaaS – warstwa pod generatorem Opisów NFZ (zamiast wspolne.js z wersji statycznej).
   Interfejs G jak w wspolne.js (ready, store, wrapBE, draft, sums, clinics, dayClinic, bar, onLock), ale:
   - konto i sesja: logowanie na serwerze (ciasteczko HttpOnly); dane startowe wstawia serwer (window.__GABINET),
   - dane na urządzeniu (treść opisów, odpowiedzi, szkice) szyfrowane AES-GCM 256 kluczem urządzenia: niewyciągalny CryptoKey
     w IndexedDB, osobny dla każdego konta; serwer nigdy go nie widzi,
   - do chmury trafia tylko historia bez treści: data, gabinet, kody, punkty, stawki, kwoty, czas – bez inicjałów i opisu (decyzja 1),
   - konflikty między urządzeniami: wizyty – wygrywa wpis o nowszym czasie zmiany, usunięcia jako znaczniki czasu;
     dokumenty Kalendarza i materiały (cennik, szablony, zestawy) – kontrola wersji na serwerze i scalanie trójstronne
     (zmiany z obu urządzeń zostają; ta sama wartość zmieniona w obu miejscach – wygrywa to urządzenie). */
(function () {
  'use strict';
  const C = window.__GABINET;
  if (!C || !C.uid) { location.replace('/logowanie'); return; }
  const TE = new TextEncoder(), TD = new TextDecoder();
  const rnd = n => crypto.getRandomValues(new Uint8Array(n));
  function b64(u8) { let s = ''; for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode.apply(null, u8.subarray(i, i + 0x8000)); return btoa(s); }
  function unb64(s) { const b = atob(s), u = new Uint8Array(b.length); for (let i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; }
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MOD = C.mod === 'prywatne' || C.mod === 'kalendarz' || C.mod === 'import' || C.mod === 'zlecenia' ? C.mod : 'nfz';
  const G = window.G = { user: { id: C.uid, name: C.name }, key: null, mod: null, esc };
  // Własne materiały z konta (Ustawienia → Moje materiały; pkt 1.2): podpowiedzi = lista wbudowana + własne, bez powtórzeń.
  G.mat = (kinds, base) => { const out = [], seen = new Set();
    for (const n of (base || []).concat(...[].concat(kinds).map(k => ((C.mat || {})[k] || []))))
      if (typeof n === 'string' && n && !seen.has(n.toLowerCase())) { seen.add(n.toLowerCase()); out.push(n); }
    return out; };
  G.zl = c => (Math.round(c) / 100).toLocaleString('pl-PL', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' zł';
  G.today = () => { const d = new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };

  /* ---------- IndexedDB ---------- */
  function idbOpen(name, stores, ver) {
    return new Promise((res, rej) => {
      let rq; try { rq = indexedDB.open(name, ver || 1); } catch (e) { rej(e); return; }
      const to = setTimeout(() => rej(new Error('baza danych przeglądarki nie odpowiada')), 6000);
      rq.onupgradeneeded = () => { const db = rq.result; stores.forEach(s => { if (!db.objectStoreNames.contains(s)) db.createObjectStore(s); }); };
      rq.onsuccess = () => { clearTimeout(to); const db = rq.result; db.onversionchange = () => { try { db.close(); } catch (e) { } }; res(db); };
      rq.onerror = () => { clearTimeout(to); rej(rq.error || new Error('baza niedostępna')); };
      rq.onblocked = () => { clearTimeout(to); rej(new Error('baza zablokowana przez inną kartę')); };
    });
  }
  // Limit czasu operacji na bazie przeglądarki (Safari potrafi zawiesić transakcję po przejściu między stronami):
  // zamiast „Wczytuję…” bez końca – błąd z komunikatem (moduł pokazuje informację i „Odśwież”).
  const TX_MS = 20000;
  function run(db, stores, mode, fn) {
    return new Promise((res, rej) => {
      let t; try { t = db.transaction(stores, mode); } catch (e) { rej(e); return; }
      const to = setTimeout(() => { try { t.abort(); } catch (_) { } rej(new Error('baza danych przeglądarki nie odpowiada – odśwież stronę')); }, TX_MS);
      let r; t.oncomplete = () => { clearTimeout(to); res(r && typeof r === 'object' && 'readyState' in r ? r.result : r); };
      t.onabort = t.onerror = () => { clearTimeout(to); rej(t.error || new Error('zapis przerwany')); };
      try { r = fn(t); } catch (e) { try { t.abort(); } catch (_) { } rej(e); }
    });
  }
  async function readAll(db, store) {
    if (!db.objectStoreNames.contains(store)) return [];
    let ks = [], vs = [];
    await run(db, [store], 'readonly', t => { const o = t.objectStore(store), a = o.getAllKeys(), b = o.getAll(); a.onsuccess = () => { ks = a.result; }; b.onsuccess = () => { vs = b.result; }; });
    return ks.map((k, i) => [k, vs[i]]);
  }

  /* ---------- klucz urządzenia (niewyciągalny) i szyfrowanie ---------- */
  async function deviceKey() {
    const db = await idbOpen('gabinet-saas-urzadzenie', ['klucze']);
    let k = await run(db, ['klucze'], 'readonly', t => t.objectStore('klucze').get(C.uid));
    if (k) return k;
    const nk = await crypto.subtle.generateKey({ name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
    try { await run(db, ['klucze'], 'readwrite', t => { t.objectStore('klucze').add(nk, C.uid); }); return nk; }
    catch (e) { return run(db, ['klucze'], 'readonly', t => t.objectStore('klucze').get(C.uid)); }   // inna karta była szybsza – jej klucz
  }
  async function enc(obj, aad) {
    const iv = rnd(12);
    const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv, additionalData: TE.encode(aad) }, G.key, TE.encode(JSON.stringify(obj === undefined ? null : obj)));
    return 'v1:' + b64(iv) + ':' + b64(new Uint8Array(ct));
  }
  async function dec(s, aad) {
    if (typeof s !== 'string' || s.slice(0, 3) !== 'v1:') throw new Error('nieznany zapis');
    const p = s.split(':');
    return JSON.parse(TD.decode(await crypto.subtle.decrypt({ name: 'AES-GCM', iv: unb64(p[1]), additionalData: TE.encode(aad) }, G.key, unb64(p[2]))));
  }
  G.enc = enc; G.dec = dec;

  /* ---------- konto i sesja ---------- */
  G.hint = () => C.uid;
  G.goLogin = () => location.replace('/logowanie');
  const lockHooks = [];
  G.onLock = fn => lockHooks.push(fn);
  addEventListener('pagehide', () => lockHooks.forEach(f => { try { f(); } catch (e) { } }));
  G.ready = function (mod) {
    if (G._ready) return G._ready;
    G.mod = mod;
    G._ready = (async () => {
      G.key = await deviceKey();
      if (C.seg && typeof C.seg === 'object') await kvPutLocal('nfz:seg', C.seg);          // własne wersje tekstów – z konta
      if (MOD === 'kalendarz') await kalSeed();
      if (MOD === 'zlecenia') await zlSeed();
      await blobSeed();
      try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => { }); } catch (e) { }
      return G.user;
    })();
    return G._ready;
  };

  /* ---------- pasek aplikacji ---------- */
  const LOGO = '<svg viewBox="0 0 32 32" width="22" height="22" aria-hidden="true"><path d="M16 4c-3 0-4.4 1.6-7 1.6C5.8 5.6 4 8 4 11.6c0 5.6 2.3 15.4 5.6 15.4 2.3 0 2.2-6.6 6.4-6.6s4.1 6.6 6.4 6.6c3.3 0 5.6-9.8 5.6-15.4C28 8 26.2 5.6 23 5.6 20.4 5.6 19 4 16 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>';
  const NAV = [['/kalendarz', 'Kalendarz', 'kalendarz'], ['/opisy-nfz', 'Opisy NFZ', 'nfz'], ['/opisy-prywatne', 'Opisy prywatne', 'prywatne'], ['/zlecenia', 'Zlecenia', 'zlecenia'], ['/zarobki', 'Zarobki', 'zarobki'], ['/katalog-nfz', 'Katalog NFZ'], ['/gabinety', 'Gabinety'], ['/ustawienia', 'Ustawienia'], ['/konto', 'Konto']];
  G.bar = function (mod) {
    let el = document.getElementById('gbar');
    if (!el) { el = document.createElement('header'); el.id = 'gbar'; document.body.insertBefore(el, document.body.firstChild); }
    el.className = 'gbar'; el.setAttribute('role', 'banner');
    el.innerHTML = '<div class="gbar-in"><a class="gbar-home" href="/konto" aria-label="Gabinet – konto">' + LOGO + '<span>Gabinet</span></a>' +
      '<nav class="gbar-nav" aria-label="Moduły">' + NAV.map(m => '<a href="' + m[0] + '"' + (m[2] === mod ? ' class="on" aria-current="page"' : '') + '>' + m[1] + '</a>').join('') + '</nav>' +
      '<span class="gbar-sync" id="gsync" role="status" aria-live="polite"></span></div>';
    syncStatus();
  };
  let syncErr = '';
  function syncStatus() {
    const s = document.getElementById('gsync'); if (!s) return;
    const n = pendingDel().length + dirty.size + (kalBusy ? 1 : 0) + (MOD === 'zlecenia' ? Object.keys(zPend()).length : 0) + Object.values(bBusy).filter(Boolean).length;
    if (stale && !syncErr && !n) {                                                         // materiały zmienione na innym urządzeniu (scalone na koncie)
      s.innerHTML = 'Zmiany z innego urządzenia – <a href="" id="greload">odśwież</a>'; s.className = 'gbar-sync';
      const a = document.getElementById('greload'); if (a) a.onclick = ev => { ev.preventDefault(); location.reload(); };
      return;
    }
    s.textContent = syncErr ? '⚠ ' + syncErr : n ? 'Zapisuję w chmurze…' : MOD === 'kalendarz' ? 'Kalendarz zsynchronizowany' : MOD === 'zlecenia' ? 'Zlecenia zsynchronizowane' : 'Historia zsynchronizowana';
    s.className = 'gbar-sync' + (syncErr ? ' err' : '');
  }

  /* ---------- magazyn konta na urządzeniu (kv: ustawienia tekstów, sumy; szkice) ---------- */
  const STORES = ['kv', 'szkice', 'wizyty', 'opisy', 'zlecenia', 'zdjecia'];             // zlecenia/zdjecia – Zlecenia protetyczne (wersja 3 bazy; zlecenia też w chmurze od E7, zdjęcia tylko na urządzeniu)                                   // wizyty/opisy – Opisy prywatne (wersja 2 bazy)
  let udb = null;
  async function userDb() { if (!udb) udb = await idbOpen('gabinet-saas@' + C.uid, STORES, 3); return udb; }
  // Safari zachowuje poprzednią stronę w pamięci „wstecz/naprzód” razem z otwartym połączeniem do bazy, co potrafi
  // zablokować bazę na następnej stronie (np. Opisy NFZ → Opisy prywatne). Przy wyjściu zamykamy połączenie (po zapisach
  // z pagehide), a stronę przywróconą z tej pamięci przeładowujemy na świeżo. Zgłoszenie Patryka 21.11.2026.
  addEventListener('pagehide', e => { if (e.persisted) setTimeout(() => { try { if (udb) udb.close(); } catch (_) { } udb = null; }, 0); });
  addEventListener('pageshow', e => { if (e.persisted) location.reload(); });
  const BLOBS = ['pryw:cennik', 'pryw:ust', 'pryw:katalog', 'pryw:zestawy'];
  const PB_KEY = 'gabinet-saas.bloby@' + C.uid;
  const pendingBlobs = () => { try { const a = JSON.parse(localStorage.getItem(PB_KEY) || '[]'); return Array.isArray(a) ? a : []; } catch (e) { return []; } };
  const setPendingBlobs = a => { try { localStorage.setItem(PB_KEY, JSON.stringify([...new Set(a)])); } catch (e) { } };
  /* scalanie trójstronne: baza (ostatnia wersja z konta znana urządzeniu), zmiany tutaj, zmiany na koncie */
  const J = x => x === undefined ? undefined : JSON.stringify(x);
  const clone = x => x === undefined ? undefined : JSON.parse(JSON.stringify(x));      // kopia: strona modułu modyfikuje swoje obiekty w miejscu
  const isObj = x => !!x && typeof x === 'object' && !Array.isArray(x);
  const idArr = a => Array.isArray(a) && a.every(x => isObj(x) && (typeof x.id === 'string' || typeof x.id === 'number'));
  function merge3(b, l, s) {
    const jl = J(l), js = J(s), jb = J(b);
    if (jl === js) return l;
    if (jl === jb) return s;                                                              // zmiana tylko na koncie
    if (js === jb) return l;                                                              // zmiana tylko tutaj
    if (l === undefined || l === null) return s;                                          // usunięte tutaj, zmienione gdzie indziej → zostaje
    if (s === undefined || s === null) return l;
    if (isObj(l) && isObj(s)) {
      const bb = isObj(b) ? b : {}, out = {};
      new Set([...Object.keys(s), ...Object.keys(l)]).forEach(k => { const m = merge3(bb[k], l[k], s[k]); if (m !== undefined) out[k] = m; });
      return out;
    }
    if (idArr(l) && idArr(s)) {                                                           // listy z identyfikatorami (dyżury, koszty, gabinety, zestawy…)
      const bm = new Map((idArr(b) ? b : []).map(x => [x.id, x])), lm = new Map(l.map(x => [x.id, x])), sm = new Map(s.map(x => [x.id, x]));
      const ids = [...l.map(x => x.id), ...s.map(x => x.id).filter(id => !lm.has(id))], out = [];
      ids.forEach(id => { const m = merge3(bm.get(id), lm.get(id), sm.get(id)); if (m !== undefined) out.push(m); });
      return out;
    }
    return l;
  }
  G._merge3 = merge3;
  G._kal = () => ({ base: Object.fromEntries(Object.entries(kBase).map(([k, v]) => [k, v.ver])), pend: kalPend() });
  async function kvGetLocal(k) { const db = await userDb(); const v = await run(db, ['kv'], 'readonly', t => t.objectStore('kv').get(k)); return v === undefined ? undefined : dec(v, 'g:kv:' + k); }

  /* materiały (cennik, ustawienia, szablony, zestawy) ↔ konto z kontrolą wersji */
  const bBase = {}, bBusy = {}, bNext = {};
  let stale = false;
  async function blobSeed() {
    const pend = pendingBlobs(), srv = C.blobs || {}, ver = C.blobVer || {};
    for (const k of BLOBS) {
      const sv = { ver: ver[k] || 0, data: clone(srv[k]) };
      const loc = pend.includes(k) ? await kvGetLocal(k).catch(() => undefined) : undefined;
      if (loc !== undefined) {                                                            // zmiana z tego urządzenia jeszcze niewysłana
        bBase[k] = (await kvGetLocal('base:' + k).catch(() => undefined)) || sv;
        postBlob(k, loc);
      } else if (k in srv) { await kvPutLocal(k, srv[k]); bBase[k] = sv; kvPutLocal('base:' + k, sv).catch(() => { }); }
      else bBase[k] = sv;
    }
  }
  function postBlob(k, v) {
    if (bBusy[k]) { bNext[k] = v; return; }
    bBusy[k] = true;
    setPendingBlobs(pendingBlobs().concat(k));
    const b = bBase[k] || { ver: 0 };
    post('/api/dane', { key: k, data: v, base: b.ver }).then(j => {
      bBase[k] = { ver: j.version, data: clone(v) }; kvPutLocal('base:' + k, bBase[k]).catch(() => { });
      if (!bNext[k]) setPendingBlobs(pendingBlobs().filter(x => x !== k));
      syncErr = '';
    }, async e => {
      if (e.status === 409 && e.data && e.data.conflict) {                                 // zmienione na innym urządzeniu – scal i wyślij ponownie
        const c = e.data.conflict, m = merge3(b.data, bNext[k] !== undefined ? bNext[k] : v, c.data);
        bBase[k] = { ver: c.version, data: clone(c.data) }; kvPutLocal('base:' + k, bBase[k]).catch(() => { });
        await kvPutLocal(k, m).catch(() => { });
        bNext[k] = m; stale = true;
      } else { fail(e); setTimeout(() => { if (!bBusy[k]) postBlob(k, v); }, 30000); }
    }).finally(() => {
      bBusy[k] = false; syncStatus();
      if (bNext[k] !== undefined) { const n = bNext[k]; delete bNext[k]; postBlob(k, n); }
    });
  }
  async function blobRefresh() {                                                         // po powrocie do karty: czy materiały zmieniły się gdzie indziej
    if (MOD !== 'prywatne' || document.hidden) return;
    const since = {}; BLOBS.forEach(k => { since[k] = (bBase[k] || {}).ver || 0; });
    try { const j = await post('/api/dane', { since }); if (Object.keys(j.changed || {}).length) { stale = true; syncStatus(); } } catch (e) { }
  }
  let prywMerged = false;
  async function kvPutLocal(k, v) { const s = await enc(v, 'g:kv:' + k); const db = await userDb(); await run(db, ['kv'], 'readwrite', t => { t.objectStore('kv').put(s, k); }); }
  G.store = function (name) {
    const aad = k => 'g:' + name + ':' + k;
    return {
      async get(k) { const db = await userDb(); const v = await run(db, [name], 'readonly', t => t.objectStore(name).get(k)); return v === undefined ? undefined : dec(v, aad(k)); },
      async put(k, v) {
        const s = await enc(v, aad(k)); const db = await userDb(); await run(db, [name], 'readwrite', t => { t.objectStore(name).put(s, k); });
        if (name === 'kv' && k === 'nfz:seg') postSettings({ seg: v });           // własne wersje stałych tekstów → konto (bez danych pacjentów)
        if (name === 'kv' && BLOBS.includes(k)) postBlob(k, v);                   // cennik, ustawienia, szablony, zestawy → konto
        if (name === 'wizyty' && MOD === 'prywatne' && v && v.id === k) queue([v], []);
        if (name === 'kv' && k === 'grafik' && MOD === 'kalendarz') kalPush();
        if (name === 'zlecenia' && MOD === 'zlecenia') zMark(k, 'put');
      },
      async del(k) {
        const db = await userDb(); await run(db, [name], 'readwrite', t => { t.objectStore(name).delete(k); });
        if (name === 'wizyty' && MOD === 'prywatne') queue([], [{ id: k, at: new Date().toISOString() }]);
        if (name === 'zlecenia' && MOD === 'zlecenia') zMark(k, 'del');
      },
      async all() {
        const rows = await readAll(await userDb(), name);
        const out = (await Promise.all(rows.map(([k, v]) => dec(v, aad(k)).then(x => [k, x], () => null)))).filter(Boolean);
        if (name === 'wizyty' && MOD === 'prywatne' && !prywMerged) { prywMerged = true; return reconcile(prywLocal, out); }
        return out;
      }
    };
  };
  G.draft = {
    save: (mod, v) => G.store('szkice').put(mod, Object.assign({ at: new Date().toISOString() }, v)).catch(() => { }),
    load: mod => G.store('szkice').get(mod).catch(() => undefined),
    clear: mod => G.store('szkice').del(mod).catch(() => { })
  };
  G.sums = {                                                                           // sumy z opisów liczy serwer; przychód z dyżurów – Kalendarz
    put: (kind, map) => kind === 'kal' ? post('/api/kal/sumy', { map }).then(() => { }, () => { }) : Promise.resolve(),
    get: kind => Promise.resolve(C.sums && C.sums[kind] ? C.sums[kind] : undefined)
  };

  /* ---------- Kalendarz: dokumenty (ustawienia, miesiące, kursy) ↔ konto, z kontrolą wersji ---------- */
  const KP_KEY = 'gabinet-saas.kalendarz.niewyslane@' + C.uid;
  const KDOC = /^(settings|courses|m\d{4}-\d{2})$/;
  let kBase = {}, kalBusy = false, kalAgain = false;                                       // kBase: dokument → {ver, data} ostatnio uzgodniony z kontem
  const kalPend = () => { try { const x = JSON.parse(localStorage.getItem(KP_KEY) || '[]'); return Array.isArray(x) ? x : []; } catch (e) { return []; } };
  const kalPendSet = l => { try { l.length ? localStorage.setItem(KP_KEY, JSON.stringify([...new Set(l)])) : localStorage.removeItem(KP_KEY); } catch (e) { } };
  const saveBase = () => kvPutLocal('base:grafik', kBase).catch(() => { });
  const kalShow = changed => { try { window.dispatchEvent(new CustomEvent('gabinet:grafik', { detail: changed })); } catch (e) { } };
  async function kalSeed() {                                                             // konto = źródło prawdy; niewysłane dokumenty z tego urządzenia mają pierwszeństwo
    const docs = Object.assign({}, C.docs || {}), ver = C.ver || {}, pend = kalPend();
    const old = pend.length ? ((await kvGetLocal('base:grafik').catch(() => undefined)) || {}) : {};
    const loc = pend.length ? ((await kvGetLocal('grafik').catch(() => undefined)) || {}) : {};
    Object.keys(docs).forEach(k => { kBase[k] = { ver: ver[k] || 0, data: clone(docs[k]) }; });
    pend.forEach(k => { if (old[k]) kBase[k] = old[k]; if (loc[k]) docs[k] = loc[k]; else delete docs[k]; });
    await kvPutLocal('grafik', docs); saveBase();
    if (pend.length) kalPush();
    document.addEventListener('visibilitychange', kalRefresh);
  }
  async function kalPush() {
    if (kalBusy) { kalAgain = true; return; }
    const docs = (await kvGetLocal('grafik').catch(() => undefined)) || {};
    const put = {}, del = [], base = {};
    Object.keys(docs).forEach(k => { if (KDOC.test(k) && docs[k] && J(docs[k]) !== J((kBase[k] || {}).data)) { put[k] = docs[k]; base[k] = (kBase[k] || {}).ver || 0; } });
    Object.keys(kBase).forEach(k => { if (kBase[k].ver && !docs[k] && KDOC.test(k)) { del.push(k); base[k] = kBase[k].ver; } });
    if (!Object.keys(put).length && !del.length) { kalPendSet([]); return; }
    kalBusy = true; syncStatus();
    kalPendSet(kalPend().concat(Object.keys(put), del));
    try {
      const j = await post('/api/kal/dokumenty', { put, del, base });
      Object.entries(j.ver || {}).forEach(([k, v]) => { if (v) kBase[k] = { ver: v, data: clone(put[k]) }; else delete kBase[k]; });
      const cf = j.conflict || {};
      if (Object.keys(cf).length) {                                                       // zmienione na innym urządzeniu: scal i wyślij ponownie
        const cur = (await kvGetLocal('grafik').catch(() => undefined)) || {}, shown = {};
        Object.entries(cf).forEach(([k, c]) => {
          const m = merge3((kBase[k] || {}).data, cur[k], c.data === null ? undefined : c.data);
          if (c.version) kBase[k] = { ver: c.version, data: clone(c.data) }; else delete kBase[k];
          if (m === undefined || m === null) delete cur[k]; else cur[k] = m;
          shown[k] = clone(cur[k]) || null;
        });
        await kvPutLocal('grafik', cur); kalShow(shown); kalAgain = true;
      } else kalPendSet([]);
      saveBase(); syncErr = '';
    } catch (e) { fail(e); setTimeout(kalPush, 30000); }
    finally { kalBusy = false; syncStatus(); if (kalAgain) { kalAgain = false; kalPush(); } }
  }
  async function kalRefresh() {                                                          // po powrocie do karty: zmiany z innych urządzeń
    if (document.hidden || kalBusy || kalPend().length) return;
    const since = {}; Object.keys(kBase).forEach(k => { since[k] = kBase[k].ver; });
    let j; try { j = await post('/api/kal/dokumenty', { since }); } catch (e) { return; }
    const ch = j.changed || {}; if (!Object.keys(ch).length || kalBusy || kalPend().length) return;
    const cur = (await kvGetLocal('grafik').catch(() => undefined)) || {}, shown = {};
    Object.entries(ch).forEach(([k, c]) => {
      if (c.version) { kBase[k] = { ver: c.version, data: clone(c.data) }; cur[k] = c.data; } else { delete kBase[k]; delete cur[k]; }
      shown[k] = clone(cur[k]) || null;
    });
    await kvPutLocal('grafik', cur); saveBase(); kalShow(shown);
  }
  /* ---------- Zlecenia protetyczne ↔ konto (E7, decyzja 17): treść zlecenia z kontrolą wersji; zdjęcia NIGDY (tylko urządzenie) ---------- */
  const ZP_KEY = 'gabinet-saas.zlecenia.niewyslane@' + C.uid;                            // id → [rodzaj, znacznik] (bez treści)
  let zVer = {}, zBusy = false, zAgain = false, zT = null;
  const zPend = () => { try { const x = JSON.parse(localStorage.getItem(ZP_KEY) || '{}'); return x && typeof x === 'object' && !Array.isArray(x) ? x : {}; } catch (e) { return {}; } };
  const zPendSet = o => { try { Object.keys(o).length ? localStorage.setItem(ZP_KEY, JSON.stringify(o)) : localStorage.removeItem(ZP_KEY); } catch (e) { } };
  const zSaveVer = () => kvPutLocal('zl:ver', zVer).catch(() => { });
  const zShow = ids => { try { window.dispatchEvent(new CustomEvent('gabinet:zlecenia', { detail: ids })); } catch (e) { } };
  function zMark(id, co) { const p = zPend(); p[id] = [co, Date.now() + Math.random()]; zPendSet(p); syncStatus(); clearTimeout(zT); zT = setTimeout(zlPush, 700); }
  async function zLocalDel(id) {                                                         // zlecenie usunięte na innym urządzeniu: też jego zdjęcia z tego urządzenia
    const keys = (await readAll(await userDb(), 'zdjecia')).map(([k]) => k).filter(k => String(k).startsWith(id + ':'));
    await prywLocal.write([{ s: 'zlecenia', key: id, del: true }].concat(keys.map(k => ({ s: 'zdjecia', key: k, del: true }))));
  }
  async function zlSeed() {
    zVer = (await kvGetLocal('zl:ver').catch(() => undefined)) || {};
    const had = Object.keys(zVer).length;
    await zlPull(true);
    if (!had) {                                                                          // pierwsze połączenie: zlecenia zapisane wcześniej tylko na tym urządzeniu → do chmury
      const p = zPend(); for (const [k] of await readAll(await userDb(), 'zlecenia')) if (!zVer[k] && !p[k]) p[k] = ['put', Date.now()];
      zPendSet(p);
    }
    if (Object.keys(zPend()).length) zlPush();
    document.addEventListener('visibilitychange', () => { if (!document.hidden) zlPull(); });
  }
  async function zlPull(start) {
    if (zBusy) return;
    let j; try { j = await post('/api/zlecenia', { known: zVer }); } catch (e) { if (!start) return; fail(e); return; }
    const ch = j.changed || {}, pend = zPend(), shown = [];
    for (const [id, c] of Object.entries(ch)) {
      if (pend[id]) continue;                                                            // niewysłana zmiana z tego urządzenia – rozstrzygnie zapis (konflikt wersji)
      if (c.deleted || !c.version) { await zLocalDel(id); delete zVer[id]; }
      else { await prywLocal.write([{ s: 'zlecenia', key: id, val: c.data }]); zVer[id] = c.version; }
      shown.push(id);
    }
    if (shown.length) { await zSaveVer(); if (!start) zShow(shown); }
  }
  async function zlPush() {
    if (zBusy) { zAgain = true; return; }
    const pend = zPend(), ids = Object.keys(pend).slice(0, 100); if (!ids.length) { syncStatus(); return; }
    zBusy = true; syncStatus();
    try {
      const put = [], del = [];
      for (const id of ids) {
        const o = pend[id][0] === 'del' ? undefined : await G.store('zlecenia').get(id).catch(() => undefined);
        if (o) put.push({ o, base: zVer[id] || 0 }); else del.push({ id, base: zVer[id] || 0 });
      }
      const j = await post('/api/zlecenia', { put, del });
      Object.entries(j.ver || {}).forEach(([id, v]) => { if (v) zVer[id] = v; else delete zVer[id]; });
      const shown = [], keep = new Set(), cf = j.conflict || {};
      for (const [id, c] of Object.entries(cf)) {                                         // zmienione na innym urządzeniu
        const loc = put.find(p => p.o.id === id);
        if (!loc && c.deleted) { delete zVer[id]; continue; }                                 // usuwane tu i tam – gotowe
        zVer[id] = c.version || 0;
        if (!loc) { keep.add(id); continue; }                              // usunięcie wygrywa – ponów z nową wersją
        if (c.deleted || !c.data || String(loc.o.at || '') >= String(c.data.at || '')) { keep.add(id); continue; }   // nowsza wersja z tego urządzenia – ponów
        await prywLocal.write([{ s: 'zlecenia', key: id, val: c.data }]); shown.push(id);   // nowsza wersja z innego urządzenia – przyjęta
      }
      const now = zPend();
      ids.forEach(id => { if (!keep.has(id) && now[id] && now[id][1] === pend[id][1]) delete now[id]; });   // zmienione w trakcie wysyłania – zostaje w kolejce
      zPendSet(now); await zSaveVer(); syncErr = '';
      if (shown.length) zShow(shown);
      if (Object.keys(now).length) zAgain = true;
    } catch (e) {
      if (e.status === 400) { syncErr = 'zlecenie odrzucone przez serwer: ' + e.message; const p = zPend(); ids.forEach(id => { delete p[id]; }); zPendSet(p); }
      else { fail(e); setTimeout(zlPush, 30000); }
    } finally { zBusy = false; syncStatus(); if (zAgain) { zAgain = false; setTimeout(zlPush, 50); } }
  }
  const prywLocal = {                                                                   // zapis lokalny wizyt prywatnych bez wysyłania (scalanie)
    async write(ops) { const db = await userDb(); const e2 = await Promise.all(ops.map(o => o.del ? o : enc(o.val, 'g:' + o.s + ':' + o.key).then(x => ({ s: o.s, key: o.key, val: x }))));
      await run(db, [...new Set(e2.map(o => o.s))], 'readwrite', t => { e2.forEach(o => { const st = t.objectStore(o.s); if (o.del) st.delete(o.key); else st.put(o.val, o.key); }); }); }
  };
  G.clinics = async (all) => (C.clinics || []).filter(c => all || c.active !== false).map(c => ({ id: c.id, name: c.name, short: c.short, color: c.color, active: c.active !== false }));
  G.dayClinic = async (date, hhmm) => {                                                 // gabinet z dyżuru w Kalendarzu (jak w obecnej aplikacji)
    const sh = ((C.shifts || {})[date] || []).map(x => ({ c: x[0], s: x[1], e: x[2] }));
    if (!sh.length) return '';
    if (hhmm) { const hit = sh.find(x => x.s <= hhmm && hhmm < x.e); if (hit) return hit.c; }
    return sh.slice().sort((a, b) => String(a.s).localeCompare(String(b.s)))[0].c;
  };

  /* ---------- ustawienia generatora → konto ---------- */
  const CFG_KEY = 'opisyNFZ@' + C.uid + '.cfg';
  try {                                                                                // stawki, ulubione, zestawy z konta zanim generator wystartuje
    const loc = JSON.parse(localStorage.getItem(CFG_KEY) || 'null') || { v: 2 };
    localStorage.setItem(CFG_KEY, JSON.stringify(Object.assign(loc, C.cfg || {})));
  } catch (e) { }
  let lastCfg = JSON.stringify(C.cfg || {}), cfgT = null;
  function pickCfg() { /* global cfg */ const c = typeof cfg !== 'undefined' ? cfg : null; return c && { price: c.price, pct: c.pct, rev: c.rev, basis: c.basis, auto: c.auto, fav: c.fav, hid: c.hid, sets: c.sets, sum: c.sum }; }
  addEventListener('DOMContentLoaded', () => {
    const orig = window.cfgSave;
    if (typeof orig !== 'function') return;
    window.cfgSave = function () {
      const r = orig.apply(this, arguments);
      clearTimeout(cfgT); cfgT = setTimeout(() => { const p = pickCfg(); const s = JSON.stringify(p); if (p && s !== lastCfg) { lastCfg = s; postSettings({ cfg: p }); } }, 400);
      return r;
    };
  });

  /* ---------- komunikacja z serwerem ---------- */
  async function post(url, body) {
    const data = JSON.stringify(body);                                                   // keepalive: zapis dokończy się przy przejściu do innej strony (limit 64 KB)
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, credentials: 'same-origin', body: data, keepalive: data.length < 60000 });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) { const e = new Error(j.error || ('błąd serwera ' + r.status)); e.login = !!j.login; e.status = r.status; e.data = j; throw e; }
    return j;
  }
  function fail(e) { syncErr = e && e.login ? 'sesja wygasła – zaloguj się ponownie (dane są zapisane na tym urządzeniu)' : 'brak połączenia – zapisano na tym urządzeniu, wyślę później'; syncStatus(); }
  function postSettings(b) { post('/api/nfz/ustawienia', b).then(() => { syncErr = ''; syncStatus(); }, fail); }

  /* ---------- historia wizyt: urządzenie ↔ chmura ---------- */
  const DEL_KEY = 'gabinet-saas.' + MOD + '.usuniete@' + C.uid;
  const pendingDel = () => { try { const a = JSON.parse(localStorage.getItem(DEL_KEY) || '[]'); return Array.isArray(a) ? a : []; } catch (e) { return []; } };
  const setPendingDel = a => { try { localStorage.setItem(DEL_KEY, JSON.stringify(a.slice(-2000))); } catch (e) { } };
  const API = MOD === 'prywatne' ? '/api/pryw/wizyty' : '/api/nfz/wizyty';
  const cloudMeta = m => {                                                              // do chmury: bez inicjałów, treści, pól szablonu, e-ZLA
    const o = Object.assign({}, m); delete o.ini; delete o.body; delete o.cloud; delete o.ezla;
    if (Array.isArray(o.items)) o.items = o.items.map(i => { const x = Object.assign({}, i); delete x.vals; delete x.def; delete x.snap; return x; });
    return o;
  };
  G._cloudMeta = cloudMeta; G._post = post; G._idbOpen = idbOpen; G._run = run; G._readAll = readAll;   // dla przeniesienia danych ze starej aplikacji (import.html)
  const dirty = new Map();                                                               // id → wpis do wysłania
  let flushT = null, flushing = false;
  function queue(puts, dels) {
    puts.forEach(m => dirty.set(m.id, m));
    if (dels.length) { const p = pendingDel().filter(d => !dels.some(x => x.id === d.id)); setPendingDel(p.concat(dels)); dels.forEach(d => dirty.delete(d.id)); }
    syncStatus(); clearTimeout(flushT); flushT = setTimeout(flush, 250);
  }
  async function flush() {
    if (flushing) { flushT = setTimeout(flush, 300); return; }
    const put = [...dirty.values()], del = pendingDel();
    if (!put.length && !del.length) { syncStatus(); return; }
    flushing = true;
    try {
      for (let i = 0; i < put.length || (i === 0 && del.length); i += 400) {
        await post(API, { put: put.slice(i, i + 400).map(cloudMeta), del: i === 0 ? del : [] });
      }
      put.forEach(m => { if (dirty.get(m.id) === m) dirty.delete(m.id); });
      setPendingDel(pendingDel().filter(d => !del.some(x => x.id === d.id && x.at === d.at)));
      syncErr = '';
    } catch (e) { fail(e); setTimeout(flush, 30000); }
    finally { flushing = false; syncStatus(); }
  }
  addEventListener('online', () => { flush(); if (MOD === 'kalendarz') kalPush(); if (MOD === 'zlecenia') zlPush(); BLOBS.forEach(k => { if (pendingBlobs().includes(k) && !bBusy[k]) kvGetLocal(k).then(v => v !== undefined && postBlob(k, v), () => { }); }); });
  document.addEventListener('visibilitychange', blobRefresh);
  addEventListener('pagehide', () => {                                                   // ostatnie zmiany przy zamknięciu karty
    const put = [...dirty.values()].map(cloudMeta), del = pendingDel();
    if ((put.length || del.length) && navigator.sendBeacon) navigator.sendBeacon(API, new Blob([JSON.stringify({ put: put.slice(0, 200), del })], { type: 'application/json' }));
  });

  /* scalenie przy starcie: chmura (stan z chwili otwarcia strony) + urządzenie; nowszy czas zmiany wygrywa */
  const VST = MOD === 'prywatne' ? 'wizyty' : 'visits', BST = MOD === 'prywatne' ? 'opisy' : 'bodies';   // nazwy sekcji magazynu modułu
  async function reconcile(be, rows) {
    const loc = new Map(rows.map(([k, v]) => [k, v]));
    const live = (C.visits && C.visits.live) || [], gone = new Map(((C.visits && C.visits.gone) || []).map(g => [g.id, g.at]));
    const myDel = new Map(pendingDel().map(d => [d.id, d.at]));
    const ops = [], push = [];
    for (const m of live) {
      if (myDel.has(m.id) && myDel.get(m.id) >= m.at) continue;                           // usunięte tu, czeka na wysłanie
      const L = loc.get(m.id);
      if (!L) { ops.push({ s: VST, key: m.id, val: m }); loc.set(m.id, m); }           // wpis z innego urządzenia (bez treści)
      else if (m.at > L.at) {
        const v = Object.assign({}, m, { ini: L.ini || '', body: L.body }, L.ezla !== undefined ? { ezla: L.ezla } : {});
        if (Array.isArray(v.items) && Array.isArray(L.items)) v.items = v.items.map((it, i) => { const li = L.items[i]; return li && li.pid === it.pid ? Object.assign({}, it, { vals: li.vals || {}, def: li.def }) : it; });
        ops.push({ s: VST, key: m.id, val: v }); loc.set(m.id, v);
      }
      else if (L.at > m.at) push.push(L);
    }
    const liveIds = new Set(live.map(m => m.id));
    for (const [id, L] of [...loc]) {
      if (liveIds.has(id)) continue;
      if (gone.has(id) && gone.get(id) >= L.at) { ops.push({ s: VST, key: id, del: true }, { s: BST, key: id, del: true }); loc.delete(id); }
      else push.push(L);                                                                   // zapisane offline albo przed założeniem chmury
    }
    if (ops.length) await be.write(ops);
    if (push.length || myDel.size) queue(push, []);
    return [...loc];
  }

  /* warstwa szyfrująca dla magazynu Opisów NFZ (DB.be: all / get / write / clear) + synchronizacja historii.
     Synchronizuje WYŁĄCZNIE pierwszy (główny) magazyn generatora. Magazyny pomocnicze – np. zapasowy localStorage,
     który generator przy starcie przepisuje do IndexedDB i czyści – nie wysyłają nic do chmury (ich czyszczenie ≠ usunięcie wizyt). */
  let mainBE = null;
  G.wrapBE = function (be, ns) {
    const aad = (s, k) => ns + ':' + s + ':' + k;
    const isMain = !mainBE;
    let merged = !isMain;
    const W = {
      kind: be.kind, enc: true,
      async all(store) {
        const rows = await be.all(store);
        const out = (await Promise.all(rows.map(([k, v]) => dec(v, aad(store, k)).then(x => [k, x], () => null)))).filter(Boolean);
        G.undecrypted = (G.undecrypted || 0) + (rows.length - out.length);
        if (store === 'visits' && !merged) { merged = true; return reconcile(raw, out); }
        return out;
      },
      async get(store, key) { const v = await be.get(store, key); if (v === undefined || v === null) return undefined; try { return await dec(v, aad(store, key)); } catch (e) { return undefined; } },
      async write(ops) {
        await raw.write(ops);
        const now = new Date().toISOString();
        const puts = ops.filter(o => o.s === 'visits' && !o.del && o.val).map(o => o.val), dels = ops.filter(o => o.s === 'visits' && o.del).map(o => ({ id: o.key, at: now }));
        if (isMain && (puts.length || dels.length)) queue(puts, dels);
      },
      async clear(stores) {
        if (isMain && stores.includes('visits')) { const ids = (await be.all('visits')).map(([k]) => k), now = new Date().toISOString(); queue([], ids.map(id => ({ id, at: now }))); }
        return be.clear(stores);
      }
    };
    const raw = {                                                                          // zapis lokalny bez wysyłania (scalanie)
      async write(ops) { const o2 = await Promise.all(ops.map(o => o.del ? o : enc(o.val, aad(o.s, o.key)).then(s => ({ s: o.s, key: o.key, val: s })))); return be.write(o2); }
    };
    if (isMain) mainBE = W;
    return W;
  };
})();
