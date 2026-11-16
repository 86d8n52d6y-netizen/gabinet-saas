// Dostęp do modułów pracy: zalogowany (z 2FA, jeśli włączone) + aktywna licencja sprawdzona w bazie (app.has_access()).
import 'server-only';
import { redirect } from 'next/navigation';
import { withUser } from './db';
import { requireUser, type Session } from './session';

export async function requireAccess(): Promise<Session> {
  const s = await requireUser();
  const ok = await withUser(s.userId, async c => (await c.query('SELECT app.has_access() AS a')).rows[0].a as boolean);
  if (!ok) redirect('/konto?dostep=brak');
  return s;
}
