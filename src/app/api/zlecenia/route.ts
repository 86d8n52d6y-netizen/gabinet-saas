// Zlecenia protetyczne ↔ konto (etap E7): zapis z kontrolą wersji i pobieranie zmian. Bez zdjęć, imienia i nazwiska, PESEL, adresu.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { Bledne, changedOrders, saveOrders } from '@/lib/zlecenia';

export async function POST(req: Request) {
  const a = await apiAuth(req, 3_000_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { put?: unknown; del?: unknown; known?: unknown };
  if (b.known && typeof b.known === 'object' && !Array.isArray(b.known)) {
    if (Object.keys(b.known).length > 20000) return json({ error: 'Za dużo zleceń naraz.' }, 413);
    return json({ ok: true, changed: await withUser(a.s.userId, c => changedOrders(c, b.known as Record<string, unknown>)) });
  }
  const put = Array.isArray(b.put) ? b.put as { o: unknown; base: unknown }[] : [];
  const del = Array.isArray(b.del) ? b.del as { id: unknown; base: unknown }[] : [];
  if (put.length + del.length > 200) return json({ error: 'Za dużo zleceń naraz.' }, 413);
  if (put.some(p => !p || typeof p !== 'object') || del.some(d => !d || typeof d !== 'object')) return json({ error: 'Nieprawidłowe zlecenie: format' }, 400);
  try {
    return json({ ok: true, ...(await withUser(a.s.userId, c => saveOrders(c, a.s.userId, put, del))) });
  } catch (e) {
    if (e instanceof Bledne) return json({ error: e.message }, 400);
    const code = (e as { code?: string }).code;
    if (code === '23514') return json({ error: 'Nieprawidłowe zlecenie albo za dużo danych (limit 256 KB na zlecenie).' }, 400);
    if (code === '23505' || code === '42501') return json({ error: 'Nieprawidłowy identyfikator zlecenia.' }, 400);
    throw e;
  }
}
