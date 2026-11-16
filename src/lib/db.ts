// Dostęp do bazy. Każde zapytanie biegnie w transakcji z jawnie wybraną rolą (RLS):
//   withUser(userId, fn)  – dane zalogowanego użytkownika (gabinet_app, app.user_id = userId)
//   withRole('auth' | 'billing' | 'admin', fn) – logowanie, płatności, panel administratora
// Rola logowania (gabinet_web) sama nie ma dostępu do tabel – bez withUser/withRole nic nie odczyta.
import 'server-only';
import { Pool, type PoolClient } from 'pg';

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const ROLES = { app: 'gabinet_app', auth: 'gabinet_auth', billing: 'gabinet_billing', admin: 'gabinet_admin' } as const;
export type Role = keyof typeof ROLES;

const g = globalThis as unknown as { __gabinetPool?: Pool };
export function pool(): Pool {
  if (!g.__gabinetPool) {
    const url = process.env.DATABASE_URL;
    if (!url) throw new Error('Brak DATABASE_URL');
    g.__gabinetPool = new Pool({ connectionString: url, max: 10, idleTimeoutMillis: 30_000, statement_timeout: 10_000 });
  }
  return g.__gabinetPool;
}

async function tx<T>(role: Role, userId: string | null, fn: (c: PoolClient) => Promise<T>): Promise<T> {
  if (userId !== null && !UUID.test(userId)) throw new Error('Nieprawidłowy identyfikator użytkownika');
  const c = await pool().connect();
  try {
    await c.query('BEGIN');
    await c.query(`SET LOCAL ROLE ${ROLES[role]}`);                       // nazwa roli ze stałej listy – nie z danych wejściowych
    if (userId) await c.query(`SELECT set_config('app.user_id', $1, true)`, [userId]);
    const out = await fn(c);
    await c.query('COMMIT');
    return out;
  } catch (e) {
    await c.query('ROLLBACK').catch(() => {});
    throw e;
  } finally { c.release(); }
}

export const withUser = <T>(userId: string, fn: (c: PoolClient) => Promise<T>) => tx('app', userId, fn);
export const withRole = <T>(role: Exclude<Role, 'app'>, fn: (c: PoolClient) => Promise<T>) => tx(role, null, fn);
