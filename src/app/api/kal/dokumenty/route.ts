// Kalendarz: zapis dokumentów (ustawienia z gabinetami, miesiące z dyżurami). Bez danych pacjentów.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { saveDocs } from '@/lib/kal';

export async function POST(req: Request) {
  const a = await apiAuth(req, 3_000_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { put?: unknown; del?: unknown };
  const put = b.put && typeof b.put === 'object' && !Array.isArray(b.put) ? b.put as Record<string, unknown> : {};
  const del = Array.isArray(b.del) ? b.del.filter((x): x is string => typeof x === 'string').slice(0, 500) : [];
  if (Object.keys(put).length > 400) return json({ error: 'Za dużo dokumentów naraz.' }, 413);
  try { await withUser(a.s.userId, c => saveDocs(c, a.s.userId, put, del)); }
  catch (e) {
    const code = (e as { code?: string }).code;
    if (code === '23505' || code === '42501') return json({ error: 'Nieprawidłowy identyfikator gabinetu.' }, 400);
    if (code === '23514') return json({ error: 'Za dużo danych w jednym miesiącu (limit 1 MB).' }, 413);
    if (e instanceof Error && e.message.startsWith('Nieprawidłowy')) return json({ error: e.message }, 400);
    throw e;
  }
  return json({ ok: true });
}
