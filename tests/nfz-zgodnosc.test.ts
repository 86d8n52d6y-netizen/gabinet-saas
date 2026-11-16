// Zgodność nowego silnika NFZ ze starą aplikacją: 3000 losowych wizyt i 3000 wyliczeń kwot policzonych w nfz.html
// (wzorzec: tests/fixtures/nfz_stara_wersja.json, generator: tests/tools/wzorzec_nfz.py). Katalog – z bazy (migracja 0003).
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { randomUUID } from 'node:crypto';
import { pool, withRole } from '@/lib/db';
import { loadCatalog } from '@/lib/nfz/catalog';
import { nfzPoints, visitMoney, type Catalog } from '@/lib/nfz/engine';

type Case = { codes: string[]; qty: Record<string, number>; age: number | null; preg: boolean; an: Record<string, number>;
  old: { total: number; rows: [string, number, number, number, number, number][] } };
type Money = { pts: number; price: number; pct: number; revH: number; revRate: number; ex: { c: number }[]; basis: 'full' | 'share'; old: number[] };
const fx = JSON.parse(readFileSync(new URL('./fixtures/nfz_stara_wersja.json', import.meta.url), 'utf8')) as { zrodlo: string; punkty: Case[]; kwoty: Money[] };

let cat: Catalog;
const U = randomUUID();
beforeAll(async () => {
  await withRole('auth', c => c.query(`INSERT INTO app.profiles(id,email,password_hash,display_name) VALUES ($1,$2,'$argon2id$x','T')`, [U, `nfz-${U}@test.pl`]));
  cat = (await loadCatalog(U)).catalog;
});
afterAll(async () => { await pool().end(); });

describe(`silnik NFZ = stara aplikacja (${fx.zrodlo})`, () => {
  it('katalog: 20 kodów + 3 znieczulenia, każdy ze źródłem', () => {
    expect(Object.keys(cat)).toHaveLength(23);
    expect(Object.values(cat).filter(e => e.kind === 'anest').map(e => e.code).sort()).toEqual(['0401', '0402', '0403']);
  });
  it(`punkty: ${fx.punkty.length} losowych wizyt – suma i każdy wiersz identyczne`, () => {
    const diff: string[] = [];
    for (const k of fx.punkty) {
      const P = nfzPoints(cat, { items: k.codes.map(c => ({ code: c, qty: k.qty[c] })), anest: k.an, age: k.age, pregnant: k.preg });
      const rows = P.rows.map(r => [r.code, r.qty, r.k, r.n10, r.n08, Math.round(r.pts * 10000) / 10000]);
      if (P.total !== k.old.total || JSON.stringify(rows) !== JSON.stringify(k.old.rows)) diff.push(JSON.stringify({ k, nowe: { total: P.total, rows } }));
    }
    expect(diff.slice(0, 3)).toEqual([]);
  });
  it(`kwoty: ${fx.kwoty.length} wyliczeń (grosze) identyczne`, () => {
    const diff = fx.kwoty.filter(m => { const k = visitMoney(m, m.basis); return JSON.stringify([k.pc, k.sh, k.rv, k.ex, k.pe, k.total]) !== JSON.stringify(m.old); });
    expect(diff.slice(0, 3)).toEqual([]);
  });
  it('własny kod NFZ: punkty × ilość, bez współczynników i bez ×0,8', () => {
    const P = nfzPoints(cat, { items: [{ code: 'ST01', qty: 2 }], custom: [{ item: { code: 'X99', name: 'Własny', points: 10 }, qty: 3 }], age: 10, pregnant: false });
    const x = P.rows.find(r => r.custom)!;
    expect([x.k, x.pts]).toEqual([1, 30]);
    expect(P.total).toBe(93 * 1.5 * (1 + 0.8) + 30);
  });
});
