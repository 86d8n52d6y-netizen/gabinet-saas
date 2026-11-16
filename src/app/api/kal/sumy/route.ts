// Kalendarz: przychód z odbytych dyżurów (dzień → gabinet) – kolumna „Dyżury wg Kalendarza” w Zarobkach.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { saveKalSums } from '@/lib/kal';

export async function POST(req: Request) {
  const a = await apiAuth(req, 2_000_000);
  if (a instanceof Response) return a;
  await withUser(a.s.userId, c => saveKalSums(c, a.s.userId, (a.body as { map?: unknown })?.map));
  return json({ ok: true });
}
