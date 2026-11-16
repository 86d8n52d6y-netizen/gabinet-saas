// Materiały gabinetowe modułów (cennik, ustawienia, własne szablony, zestawy) – bez danych pacjentów; tylko klucze z listy.
import { apiAuth, json } from '@/lib/api';
import { withUser } from '@/lib/db';
import { BLOB_KEYS } from '@/lib/pryw/wizyty';

export async function POST(req: Request) {
  const a = await apiAuth(req, 1_000_000);
  if (a instanceof Response) return a;
  const b = (a.body ?? {}) as { key?: unknown; data?: unknown };
  if (typeof b.key !== 'string' || !(BLOB_KEYS as readonly string[]).includes(b.key)) return json({ error: 'Nieznany klucz.' }, 400);
  if (b.data === null || typeof b.data !== 'object') return json({ error: 'Oczekiwano obiektu.' }, 400);
  try {
    await withUser(a.s.userId, c => c.query(`INSERT INTO app.user_blobs(owner_id, key, data) VALUES ($1, $2, $3::jsonb)
      ON CONFLICT (owner_id, key) DO UPDATE SET data = EXCLUDED.data`, [a.s.userId, b.key, JSON.stringify(b.data)]));
  } catch (e) {
    if ((e as { code?: string }).code === '23514') return json({ error: 'Za dużo danych (limit 1 MB).' }, 413);
    throw e;
  }
  return json({ ok: true });
}
