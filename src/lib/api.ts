// Wspólne zabezpieczenia API wywoływanego z generatora (fetch z tej samej domeny):
// sesja + licencja, nagłówek Origin zgodny z domeną (ochrona przed CSRF, obok ciasteczka SameSite=Lax), limit rozmiaru.
import 'server-only';
import { withUser } from './db';
import { getSession, type Session } from './session';
import { appUrl } from './env';

export const json = (data: unknown, status = 200) => Response.json(data, { status, headers: { 'Cache-Control': 'no-store' } });

export async function apiAuth(req: Request, maxBytes = 2_000_000): Promise<{ s: Session; body: unknown } | Response> {
  const origin = req.headers.get('origin');
  const host = req.headers.get('x-forwarded-host') ?? req.headers.get('host');
  const allowed = new Set([appUrl(), host ? `http://${host}` : '', host ? `https://${host}` : ''].filter(Boolean));
  if (!origin || !allowed.has(origin)) return json({ error: 'Niedozwolone źródło żądania.' }, 403);
  if (!(req.headers.get('content-type') ?? '').startsWith('application/json')) return json({ error: 'Oczekiwano JSON.' }, 415);
  const len = Number(req.headers.get('content-length') ?? 0);
  if (len > maxBytes) return json({ error: 'Za duże żądanie.' }, 413);
  const s = await getSession();
  if (!s || !s.mfaPassed) return json({ error: 'Sesja wygasła – zaloguj się ponownie.', login: true }, 401);
  const ok = await withUser(s.userId, async c => (await c.query('SELECT app.has_access() AS a')).rows[0].a as boolean);
  if (!ok) return json({ error: 'Brak aktywnej licencji.' }, 403);
  const text = await req.text();
  if (text.length > maxBytes) return json({ error: 'Za duże żądanie.' }, 413);
  try { return { s, body: JSON.parse(text) }; } catch { return json({ error: 'Niepoprawny JSON.' }, 400); }
}
