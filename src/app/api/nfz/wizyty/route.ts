// Synchronizacja historii wizyt generatora NFZ (bez treści opisów i bez inicjałów – patrz lib/nfz/wizyty.ts).
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { cleanMeta, deleteVisit, listVisits, upsertVisit } from '@/lib/nfz/wizyty';

export async function POST(req: Request) {
  const a = await apiAuth(req);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { put?: unknown[]; del?: { id?: unknown; at?: unknown }[]; list?: boolean };
  const put = Array.isArray(b.put) ? b.put.slice(0, 500) : [], del = Array.isArray(b.del) ? b.del.slice(0, 500) : [];
  let saved = 0, rejected = 0;
  const out = await withUser(a.s.userId, async c => {
    for (const x of put) { const m = cleanMeta(x); if (!m) { rejected++; continue; } if (await upsertVisit(c, a.s.userId, m)) saved++; }
    for (const d of del) {
      if (typeof d?.id === 'string' && /^[A-Za-z0-9_-]{1,40}$/.test(d.id) && typeof d.at === 'string' && !isNaN(Date.parse(d.at)))
        await deleteVisit(c, d.id, new Date(d.at).toISOString());
    }
    return b.list ? listVisits(c) : null;
  });
  return json({ ok: true, saved, rejected, ...(out ?? {}) });
}
