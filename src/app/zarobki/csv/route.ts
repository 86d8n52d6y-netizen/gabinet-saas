// Zarobki – plik CSV (Excel/Numbers): średnik, przecinek dziesiętny, UTF-8 z BOM. Jedna kwota = jeden wiersz; bez danych pacjentów.
import { withUser } from '@/lib/db';
import { getSession } from '@/lib/session';
import { csvRows, rangeOf } from '@/lib/zarobki';
export const dynamic = 'force-dynamic';

const ZRODLO: Record<string, string> = { nfz_points: 'NFZ – punkty', nfz_review: 'NFZ – przeglądy', nfz_extra: 'NFZ – kwota dodatkowa', private_procedure: 'Prywatne – procedura', manual: 'Ręcznie' };
const q = (v: unknown) => { const s = String(v ?? ''); return /[;"\n\r]/.test(s) || /^[=+\-@]/.test(s) ? '"' + s.replace(/^([=+\-@])/, "'$1").replace(/"/g, '""') + '"' : s; };
const zl = (gr: number) => (Number(gr) / 100).toFixed(2).replace('.', ',');

export async function GET(req: Request) {
  const s = await getSession();
  if (!s || !s.mfaPassed) return new Response('Wymagane logowanie', { status: 401 });
  const u = new URL(req.url);
  const r = rangeOf('own', u.searchParams.get('od') ?? '', u.searchParams.get('do') ?? '');
  const g = u.searchParams.get('g');
  const rows = await withUser(s.userId, async c => {
    if (!(await c.query('SELECT app.has_access() AS a')).rows[0].a) return null;
    const gid = g && /^[0-9a-f-]{36}$/i.test(g) && (await c.query('SELECT 1 FROM app.clinics WHERE id = $1', [g])).rowCount ? g : null;
    return csvRows(c, r, gid);
  });
  if (!rows) return new Response('Brak aktywnej licencji', { status: 403 });
  const head = ['Data', 'Gabinet', 'Moduł', 'Nr wpisu', 'Rodzaj', 'Pozycja', 'Kategoria', 'Ilość', 'Punkty', 'Kody NFZ', 'Wartość (zł)', 'Koszty (zł)', 'Dla lekarza (zł)'];
  const lines = rows.map(x => [x.data, x.gabinet, x.module === 'nfz' ? 'NFZ' : 'Prywatne', x.seq_no, ZRODLO[x.source] ?? x.source, x.label ?? '', x.category_name ?? '', x.qty,
    x.points == null ? '' : String(x.points).replace('.', ','), x.codes ?? '', zl(x.value_gr), zl(x.cost_gr), zl(x.doctor_pay_gr)].map(q).join(';'));
  const body = '﻿' + [head.join(';'), ...lines].join('\r\n') + '\r\n';
  return new Response(body, { headers: { 'Content-Type': 'text/csv; charset=utf-8', 'Content-Disposition': `attachment; filename="zarobki-${r.from}-${r.to}.csv"`, 'Cache-Control': 'no-store' } });
}
