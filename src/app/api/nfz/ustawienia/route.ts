// Ustawienia generatora NFZ z urządzenia: stawki, ulubione/ukryte kody, zestawy, własne wersje stałych tekstów.
// Bez danych pacjentów (kody i teksty szablonów gabinetu). Walidacja jak cfgApply w generatorze.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { cleanNfz } from '@/lib/settings';
import { cleanSeg, cleanUi } from '@/lib/nfz/ui';

export async function POST(req: Request) {
  const a = await apiAuth(req, 1_500_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { cfg?: Record<string, unknown>; seg?: unknown };
  const sets: [string, unknown][] = [];
  if (b.cfg) { sets.push(['nfz', cleanNfz(b.cfg)]); sets.push(['nfzUi', cleanUi(b.cfg)]); }
  if (b.seg) sets.push(['nfzSeg', cleanSeg(b.seg)]);
  if (!sets.length) return json({ ok: true });
  try {
    await withUser(a.s.userId, async c => {
      for (const [k, v] of sets) await c.query(`UPDATE app.user_settings SET settings = jsonb_set(settings, $2, $3::jsonb) WHERE user_id = $1`, [a.s.userId, `{${k}}`, JSON.stringify(v)]);
    });
  } catch (e) {
    if ((e as { code?: string }).code === '23514') return json({ error: 'Za dużo własnych tekstów – ustawienia przekraczają limit 64 KB.' }, 413);
    throw e;
  }
  return json({ ok: true });
}
