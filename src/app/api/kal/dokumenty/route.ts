// Kalendarz: zapis dokumentów (ustawienia z gabinetami, miesiące z dyżurami, kursy) z kontrolą wersji. Bez danych pacjentów.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { changedDocs, saveDocs } from '@/lib/kal';

export async function POST(req: Request) {
  const a = await apiAuth(req, 3_000_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { put?: unknown; del?: unknown; base?: unknown; since?: unknown };
  const obj = (x: unknown) => x && typeof x === 'object' && !Array.isArray(x) ? x as Record<string, unknown> : null;
  if (obj(b.since)) return json({ ok: true, changed: await withUser(a.s.userId, c => changedDocs(c, obj(b.since)!)) });
  const put = obj(b.put) ?? {};
  const del = Array.isArray(b.del) ? b.del.filter((x): x is string => typeof x === 'string').slice(0, 500) : [];
  if (Object.keys(put).length > 400) return json({ error: 'Za dużo dokumentów naraz.' }, 413);
  try {
    const r = await withUser(a.s.userId, c => saveDocs(c, a.s.userId, put, del, obj(b.base) ?? undefined));
    return json({ ok: true, ...r });
  } catch (e) {
    const code = (e as { code?: string }).code;
    if (code === '23505' || code === '42501') return json({ error: 'Nieprawidłowy identyfikator gabinetu.' }, 400);
    if (code === '23514') return json({ error: 'Za dużo danych w jednym miesiącu (limit 1 MB).' }, 413);
    if (e instanceof Error && e.message.startsWith('Nieprawidłowy')) return json({ error: e.message }, 400);
    throw e;
  }
}
