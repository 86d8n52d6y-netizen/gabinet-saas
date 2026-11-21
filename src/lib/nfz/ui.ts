// Walidacja ustawień generatora NFZ z urządzenia (ulubione, ukryte, zestawy, własne wersje stałych tekstów) – jak cfgApply.
const CODE = /^[A-Za-z0-9.]{1,10}$/;
const codes = (a: unknown, max: number) => Array.isArray(a) ? [...new Set(a.filter(x => typeof x === 'string' && CODE.test(x)))].slice(0, max) as string[] : [];

export function cleanUi(x: unknown) {
  const c = (x && typeof x === 'object' ? x : {}) as Record<string, unknown>;
  const sets = Array.isArray(c.sets) ? c.sets.filter(z => z && typeof z === 'object').map(z => z as Record<string, unknown>)
    .filter(z => typeof z.id === 'string' && typeof z.name === 'string' && Array.isArray(z.codes))
    .map(z => ({ id: String(z.id).replace(/[^a-z0-9]/gi, '').slice(0, 24), name: String(z.name).replace(/[<>\u0000-\u001f]/g, '').trim().slice(0, 60), codes: codes(z.codes, 30), fav: z.fav === true }))
    .filter(z => z.id && z.name && z.codes.length).slice(0, 60) : [];
  // sum: podsumowanie na początku opisu (prompt Patryka 21.11.2026, pkt 6.1) – domyślnie włączone
  return { fav: codes(c.fav, 60), hid: codes(c.hid, 80), sets, auto: c.auto === true, sum: c.sum !== false };
}
export function cleanSeg(x: unknown) {
  const c = (x && typeof x === 'object' ? x : {}) as { over?: unknown; hist?: unknown };
  const over: Record<string, { txt: string; v?: number; at?: string }> = {};
  if (c.over && typeof c.over === 'object') for (const [k, v] of Object.entries(c.over as Record<string, unknown>).slice(0, 200)) {
    if (!/^[A-Z0-9_]{1,40}$/.test(k) || !v || typeof (v as { txt?: unknown }).txt !== 'string') continue;
    const o = v as { txt: string; v?: unknown; at?: unknown };
    over[k] = { txt: o.txt.slice(0, 20000), ...(Number.isInteger(o.v) ? { v: o.v as number } : {}), ...(typeof o.at === 'string' ? { at: o.at.slice(0, 40) } : {}) };
  }
  const hist: Record<string, unknown[]> = {};
  if (c.hist && typeof c.hist === 'object') for (const [k, v] of Object.entries(c.hist as Record<string, unknown>).slice(0, 200))
    if (/^[A-Z0-9_]{1,40}$/.test(k) && Array.isArray(v)) hist[k] = v.filter(h => h && typeof (h as { txt?: unknown }).txt === 'string').slice(-10)
      .map(h => ({ txt: String((h as { txt: string }).txt).slice(0, 20000), v: Number((h as { v?: unknown }).v) || 0, at: String((h as { at?: unknown }).at ?? '').slice(0, 40) }));
  return { over, hist };
}

