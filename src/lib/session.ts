// Sesje: losowy token w ciasteczku HttpOnly; w bazie tylko jego skrót SHA-256. Jedna sesja = jedno urządzenie.
import 'server-only';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import type { PoolClient } from 'pg';
import { withRole } from './db';
import { randomToken, sha256 } from './crypto';
import { cookieSecure } from './env';

export const SESSION_DAYS = 30;          // wygasa po 30 dniach bez używania
export const SESSION_MAX_DAYS = 180;     // i najpóźniej po 180 dniach od zalogowania
export const MFA_PENDING_MIN = 10;       // na wpisanie kodu 2FA po haśle
const cookieName = () => (cookieSecure() ? '__Host-gabinet_sesja' : 'gabinet_sesja');

export type Session = {
  id: string; userId: string; email: string; displayName: string; role: 'user' | 'admin';
  emailVerified: boolean; mfaOn: boolean; mfaPassed: boolean;
};

/** Tworzy sesję (w ramach transakcji roli auth) i ustawia ciasteczko. */
export async function createSession(c: PoolClient, userId: string, opts: { mfaPassed: boolean; ip: string | null; device: string }) {
  const token = randomToken();
  const ttl = opts.mfaPassed ? `${SESSION_DAYS} days` : `${MFA_PENDING_MIN} minutes`;
  await c.query(
    `INSERT INTO app.sessions(user_id, token_hash, device_label, ip_prefix, expires_at, mfa_passed)
     VALUES ($1, $2, $3, $4, now() + $5::interval, $6)`, [userId, sha256(token), opts.device, opts.ip, ttl, opts.mfaPassed]);
  (await cookies()).set(cookieName(), token, {
    httpOnly: true, secure: cookieSecure(), sameSite: 'lax', path: '/',
    maxAge: opts.mfaPassed ? SESSION_DAYS * 86400 : MFA_PENDING_MIN * 60,
  });
}

export async function clearCookie() { (await cookies()).delete(cookieName()); }
export async function sessionTokenHash(): Promise<Buffer | null> {
  const t = (await cookies()).get(cookieName())?.value;
  return t && /^[A-Za-z0-9_-]{43}$/.test(t) ? sha256(t) : null;
}

/** Bieżąca sesja. Bez zapamiętywania w obrębie żądania: po akcji (np. 2FA) strona docelowa musi widzieć nowy stan.
 *  Przedłuża ważność najwyżej raz na godzinę. */
export async function getSession(): Promise<Session | null> {
  const th = await sessionTokenHash();
  if (!th) return null;
  return withRole('auth', async c => {
    const r = await c.query(
      `SELECT s.id, s.user_id, s.mfa_passed, s.last_seen_at, p.email, p.display_name, p.role,
              p.email_verified_at IS NOT NULL AS verified, p.mfa_secret_enc IS NOT NULL AS mfa_on
         FROM app.sessions s JOIN app.profiles p ON p.id = s.user_id
        WHERE s.token_hash = $1 AND s.revoked_at IS NULL AND s.expires_at > now() AND p.status = 'active'
          AND s.created_at > now() - make_interval(days => $2)`, [th, SESSION_MAX_DAYS]);
    const s = r.rows[0];
    if (!s) return null;
    if (s.mfa_passed && Date.now() - new Date(s.last_seen_at).getTime() > 3600_000)
      await c.query(`UPDATE app.sessions SET last_seen_at = now(), expires_at = now() + make_interval(days => $2) WHERE id = $1`, [s.id, SESSION_DAYS]);
    return { id: s.id, userId: s.user_id, email: s.email, displayName: s.display_name, role: s.role,
      emailVerified: s.verified, mfaOn: s.mfa_on, mfaPassed: s.mfa_passed };
  });
}

/** Strona wymagająca zalogowania (z ukończonym 2FA, jeśli włączone). */
export async function requireUser(): Promise<Session> {
  const s = await getSession();
  if (!s) redirect('/logowanie');
  if (!s.mfaPassed) redirect('/logowanie/2fa');
  return s;
}
