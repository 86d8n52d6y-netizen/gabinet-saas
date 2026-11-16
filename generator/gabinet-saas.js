/* Gabinet SaaS – warstwa pod generatorem Opisów NFZ (zamiast wspolne.js z wersji statycznej).
   Interfejs G jak w wspolne.js (ready, store, wrapBE, draft, sums, clinics, dayClinic, bar, onLock), ale:
   - konto i sesja: logowanie na serwerze (ciasteczko HttpOnly); dane startowe wstawia serwer (window.__GABINET),
   - dane na urządzeniu (treść opisów, odpowiedzi, szkice) szyfrowane AES-GCM 256 kluczem urządzenia: niewyciągalny CryptoKey
     w IndexedDB, osobny dla każdego konta; serwer nigdy go nie widzi,
   - do chmury trafia tylko historia bez treści: data, gabinet, kody, punkty, stawki, kwoty, czas – bez inicjałów i opisu (decyzja 1),
   - konflikty między urządzeniami: wygrywa wpis o nowszym czasie zmiany; usunięcia jako znaczniki czasu. */
(function () {
  'use strict';
  const C = window.__GABINET;
  if (!C || !C.uid) { location.replace('/logowanie'); return; }
  const TE = new TextEncoder(), TD = new TextDecoder();
  const rnd = n => crypto.getRandomValues(new Uint8Array(n));
  function b64(u8) { let s = ''; for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode.apply(null, u8.subarray(i, i + 0x8000)); return btoa(s); }
  function unb64(s) { const b = atob(s), u = new Uint8Array(b.length); for (let i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; }
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MOD = C.mod === 'prywatne' || C.mod === 'kalendarz' ? C.mod : 'nfz';
  const G = window.G = { user: { id: C.uid, name: C.name }, key: null, mod: null, esc };
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
  function run(db, stores, mode, fn) {
    return new Promise((res, rej) => {
      let t; try { t = db.transaction(stores, mode); } catch (e) { rej(e); return; }
      let r; t.oncomplete = () => res(r && typeof r === 'object' && 'readyState' in r ? r.result : r);
      t.onabort = t.onerror = () => rej(t.error || new Error('zapis przerwany'));
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
      const pend = pendingBlobs();
      for (const [k, v] of Object.entries(C.blobs || {})) {                                 // cennik, ustawienia, szablony, zestawy – z konta
        if (pend.includes(k)) { const loc = await G.store('kv').get(k).catch(() => undefined); if (loc !== undefined) { postBlob(k, loc); continue; } }
        await kvPutLocal(k, v);
      }
      pend.filter(k => !(k in (C.blobs || {}))).forEach(k => G.store('kv').get(k).then(v => v !== undefined && postBlob(k, v), () => { }));
      try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(() => { }); } catch (e) { }
      return G.user;
    })();
    return G._ready;
  };

  /* ---------- pasek aplikacji ---------- */
  const LOGO = '<svg viewBox="0 0 32 32" width="22" height="22" aria-hidden="true"><path d="M16 4c-3 0-4.4 1.6-7 1.6C5.8 5.6 4 8 4 11.6c0 5.6 2.3 15.4 5.6 15.4 2.3 0 2.2-6.6 6.4-6.6s4.1 6.6 6.4 6.6c3.3 0 5.6-9.8 5.6-15.4C28 8 26.2 5.6 23 5.6 20.4 5.6 19 4 16 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>';
  const NAV = [['/kalendarz', 'Kalendarz', 'kalendarz'], ['/opisy-nfz', 'Opisy NFZ', 'nfz'], ['/opisy-prywatne', 'Opisy prywatne', 'prywatne'], ['/zarobki', 'Zarobki'], ['/katalog-nfz', 'Katalog NFZ'], ['/gabinety', 'Gabinety'], ['/ustawienia', 'Ustawienia'], ['/konto', 'Konto']];
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
    const n = pendingDel().length + dirty.size + (kalBusy ? 1 : 0);
    s.textContent = syncErr ? '⚠ ' + syncErr : n ? 'Zapisuję w chmurze…' : MOD === 'kalendarz' ? 'Kalendarz zsynchronizowany' : 'Historia zsynchronizowana';
    s.className = 'gbar-sync' + (syncErr ? ' err' : '');
  }

  /* ---------- magazyn konta na urządzeniu (kv: ustawienia tekstów, sumy; szkice) ---------- */
  const STORES = ['kv', 'szkice', 'wizyty', 'opisy'];                                   // wizyty/opisy – Opisy prywatne (wersja 2 bazy)
  let udb = null;
  async function userDb() { if (!udb) udb = await idbOpen('gabinet-saas@' + C.uid, STORES, 2); return udb; }
  const BLOBS = ['pryw:cennik', 'pryw:ust', 'pryw:katalog', 'pryw:zestawy'];
  const PB_KEY = 'gabinet-saas.bloby@' + C.uid;
  const pendingBlobs = () => { try { const a = JSON.parse(localStorage.getItem(PB_KEY) || '[]'); return Array.isArray(a) ? a : []; } catch (e) { return []; } };
  const setPendingBlobs = a => { try { localStorage.setItem(PB_KEY, JSON.stringify([...new Set(a)])); } catch (e) { } };
  function postBlob(k, v) {
    setPendingBlobs(pendingBlobs().concat(k));
    post('/api/dane', { key: k, data: v }).then(() => { setPendingBlobs(pendingBlobs().filter(x => x !== k)); syncErr = ''; syncStatus(); }, fail);
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
        if (name === 'kv' && k === 'grafik' && MOD === 'kalendarz') kalPush(v);
      },
      async del(k) {
        const db = await userDb(); await run(db, [name], 'readwrite', t => { t.objectStore(name).delete(k); });
        if (name === 'wizyty' && MOD === 'prywatne') queue([], [{ id: k, at: new Date().toISOString() }]);
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

  /* ---------- Kalendarz: dokumenty (ustawienia, miesiące, kursy) ↔ konto ---------- */
  const KP_KEY = 'gabinet-saas.kalendarz.niewyslane@' + C.uid;
  let kalSent = {}, kalBusy = false, kalNext = null;
  const kalPend = () => { try { const x = JSON.parse(localStorage.getItem(KP_KEY) || '[]'); return Array.isArray(x) ? x : []; } catch (e) { return []; } };
  const kalPendSet = l => { try { l.length ? localStorage.setItem(KP_KEY, JSON.stringify(l)) : localStorage.removeItem(KP_KEY); } catch (e) { } };
  async function kalSeed() {                                                             // konto = źródło prawdy; niewysłane dokumenty z tego urządzenia mają pierwszeństwo
    const docs = Object.assign({}, C.docs || {}), pend = kalPend();
    Object.keys(docs).forEach(k => { kalSent[k] = JSON.stringify(docs[k]); });
    if (pend.length) {
      const loc = (await G.store('kv').get('grafik').catch(() => undefined)) || {};
      pend.forEach(k => { if (loc[k]) docs[k] = loc[k]; else delete docs[k]; });
    }
    await kvPutLocal('grafik', docs);
    if (pend.length) kalPush(docs);
  }
  function kalPush(docs) {
    if (!docs || typeof docs !== 'object') return;
    if (kalBusy) { kalNext = docs; return; }
    const put = {}, del = [];
    Object.keys(docs).forEach(k => { if (!/^(settings|courses|m\d{4}-\d{2})$/.test(k) || !docs[k]) return; const j = JSON.stringify(docs[k]); if (kalSent[k] !== j) put[k] = docs[k]; });
    Object.keys(kalSent).forEach(k => { if (!(k in docs) || !docs[k]) del.push(k); });
    if (!Object.keys(put).length && !del.length) return;
    kalBusy = true; syncStatus();
    kalPendSet([...new Set([...kalPend(), ...Object.keys(put), ...del])]);
    post('/api/kal/dokumenty', { put, del }).then(() => {
      Object.keys(put).forEach(k => { kalSent[k] = JSON.stringify(put[k]); }); del.forEach(k => { delete kalSent[k]; });
      const done = new Set([...Object.keys(put), ...del]); kalPendSet(kalPend().filter(k => !done.has(k) || (k in docs ? JSON.stringify(docs[k]) !== kalSent[k] : false)));
      syncErr = '';
    }, e => { fail(e); setTimeout(() => kalPush(docs), 30000); }).finally(() => {
      kalBusy = false; syncStatus(); if (kalNext) { const n = kalNext; kalNext = null; kalPush(n); }
    });
  }
  const prywLocal = {                                                                   // zapis lokalny wizyt prywatnych bez wysyłania (scalanie)
    async write(ops) { const db = await userDb(); const e2 = await Promise.all(ops.map(o => o.del ? o : enc(o.val, 'g:' + o.s + ':' + o.key).then(x => ({ s: o.s, key: o.key, val: x }))));
      await run(db, [...new Set(e2.map(o => o.s))], 'readwrite', t => { e2.forEach(o => { const st = t.objectStore(o.s); if (o.del) st.delete(o.key); else st.put(o.val, o.key); }); }); }
  };
  G.clinics = async (all) => (C.clinics || []).filter(c => all || c.active !== false).map(c => ({ id: c.id, name: c.name, short: c.short, color: c.color, active: c.active !== false }));
  G.dayClinic = async () => '';                                                        // gabinet z dyżuru – po przeniesieniu Kalendarza (etap 4e)

  /* ---------- ustawienia generatora → konto ---------- */
  const CFG_KEY = 'opisyNFZ@' + C.uid + '.cfg';
  try {                                                                                // stawki, ulubione, zestawy z konta zanim generator wystartuje
    const loc = JSON.parse(localStorage.getItem(CFG_KEY) || 'null') || { v: 2 };
    localStorage.setItem(CFG_KEY, JSON.stringify(Object.assign(loc, C.cfg || {})));
  } catch (e) { }
  let lastCfg = JSON.stringify(C.cfg || {}), cfgT = null;
  function pickCfg() { /* global cfg */ const c = typeof cfg !== 'undefined' ? cfg : null; return c && { price: c.price, pct: c.pct, rev: c.rev, basis: c.basis, auto: c.auto, fav: c.fav, hid: c.hid, sets: c.sets }; }
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
    if (!r.ok) { const e = new Error(j.error || ('błąd serwera ' + r.status)); e.login = !!j.login; throw e; }
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
  addEventListener('online', () => flush());
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
