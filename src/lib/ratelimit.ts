// Limity prób (ochrona przed zgadywaniem haseł i nadużyciami). Klucze to HMAC – w bazie nie ma jawnych e-maili ani IP.
import 'server-only';
import type { PoolClient } from 'pg';
import { hmac } from './crypto';

export const LIMITS = {
  'login:email':   { max: 5,  windowMin: 15 },   // nieudane logowania na konto
  'login:ip':      { max: 30, windowMin: 15 },   // wszystkie próby logowania z sieci
  'register:ip':   { max: 10, windowMin: 60 },
  'reset:email':   { max: 3,  windowMin: 60 },
  'reset:ip':      { max: 10, windowMin: 60 },
  'verify:user':   { max: 5,  windowMin: 60 },   // ponowne wysłanie linku weryfikacyjnego
  'mfa:user':      { max: 5,  windowMin: 15 },   // nieudane kody 2FA
} as const;
export type Bucket = keyof typeof LIMITS;

const key = (b: Bucket, k: string) => hmac('rate:' + b, k.toLowerCase());

/** Dolicza próbę; zwraca true, gdy limit został przekroczony. */
export async function hit(c: PoolClient, b: Bucket, k: string | null): Promise<boolean> {
  if (!k) return false;
  const { max, windowMin } = LIMITS[b];
  const r = await c.query<{ n: number }>('SELECT app.rate_hit($1, $2, make_interval(mins => $3)) AS n', [b, key(b, k), windowMin]);
  return r.rows[0].n > max;
}
/** Sprawdza bez doliczania. */
export async function blocked(c: PoolClient, b: Bucket, k: string | null): Promise<boolean> {
  if (!k) return false;
  const { max, windowMin } = LIMITS[b];
  const r = await c.query('SELECT 1 FROM app.rate_limits WHERE bucket = $1 AND key_hash = $2 AND hits >= $3 AND window_start > now() - make_interval(mins => $4)',
    [b, key(b, k), max, windowMin]);
  return (r.rowCount ?? 0) > 0;
}
export async function clear(c: PoolClient, b: Bucket, k: string) {
  await c.query('DELETE FROM app.rate_limits WHERE bucket = $1 AND key_hash = $2', [b, key(b, k)]);
}
