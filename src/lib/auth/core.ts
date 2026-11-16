// Wspólne elementy logiki kont (bez 'use server' – nie są wywoływane z przeglądarki).
import 'server-only';
import type { PoolClient } from 'pg';
import { hmac, randomToken, sha256 } from '../crypto';

export type State = { error?: string; ok?: string; secret?: string; qr?: string; codes?: string[]; field?: string };

export const str = (fd: FormData, k: string, max = 256) => {
  const v = fd.get(k);
  return typeof v === 'string' ? v.slice(0, max) : '';
};
export const normEmail = (e: string) => e.trim().toLowerCase();
export const emailOk = (e: string) => e.length <= 254 && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e);

export async function ev(c: PoolClient, type: string, userId: string | null, ip: string | null, device: string | null, details: object = {}) {
  await c.query('INSERT INTO app.security_events(user_id, type, ip_prefix, device_label, details) VALUES ($1, $2, $3, $4, $5)',
    [userId, type, ip, device, JSON.stringify(details)]);
}

/** Jednorazowy token e-mail; zwraca token do linku (w bazie tylko skrót). Poprzednie niewykorzystane tokeny tego typu są unieważniane. */
export async function newEmailToken(c: PoolClient, userId: string, purpose: 'verify' | 'reset', ttl: string) {
  await c.query(`UPDATE app.email_tokens SET used_at = now() WHERE user_id = $1 AND purpose = $2 AND used_at IS NULL`, [userId, purpose]);
  const token = randomToken();
  await c.query(`INSERT INTO app.email_tokens(user_id, purpose, token_hash, expires_at) VALUES ($1, $2, $3, now() + $4::interval)`,
    [userId, purpose, sha256(token), ttl]);
  return token;
}
/** Zużywa token (jeden raz). Zwraca user_id albo null. */
export async function useEmailToken(c: PoolClient, token: string, purpose: 'verify' | 'reset'): Promise<string | null> {
  if (!/^[A-Za-z0-9_-]{43}$/.test(token)) return null;
  const r = await c.query(`UPDATE app.email_tokens SET used_at = now()
     WHERE token_hash = $1 AND purpose = $2 AND used_at IS NULL AND expires_at > now() RETURNING user_id`, [sha256(token), purpose]);
  return r.rows[0]?.user_id ?? null;
}

export const recoveryHash = (userId: string, code: string) => hmac('mfa-recovery:' + userId, code.toLowerCase().replace(/[^a-z0-9]/g, ''));
export const trialKey = (email: string) => hmac('trial', normEmail(email));
export const pgUnique = (e: unknown) => (e as { code?: string })?.code === '23505';
