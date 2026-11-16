// Import kopii ze starej aplikacji: nowe gabinety (identyfikatory nadane w przeglądarce). Istniejące gabinety bez zmian.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { addClinics } from '@/lib/kal';

export async function POST(req: Request) {
  const a = await apiAuth(req, 200_000);
  if (a instanceof Response) return a;
  try {
    const added = await withUser(a.s.userId, c => addClinics(c, a.s.userId, (a.body as { clinics?: unknown })?.clinics));
    return json({ ok: true, added });
  } catch (e) {
    const code = (e as { code?: string }).code;
    if (code === '23505' || code === '42501') return json({ error: 'Nieprawidłowy identyfikator gabinetu.' }, 400);
    if (e instanceof Error && e.message.startsWith('Nieprawidłowy')) return json({ error: e.message }, 400);
    throw e;
  }
}
