// Migracje bazy: wykonuje pliki db/migrations/NNNN_*.sql po kolei, każdy dokładnie raz (tabela public.schema_migrations).
// Po migracjach tworzy/aktualizuje rolę logowania aplikacji (gabinet_web) – sama nie ma uprawnień do tabel,
// może tylko przełączyć się (SET LOCAL ROLE) na jedną z ról z RLS: gabinet_app / gabinet_auth / gabinet_billing / gabinet_admin.
// Zmienne: DATABASE_ADMIN_URL (właściciel bazy), DB_APP_PASSWORD (hasło roli gabinet_web).
import { readdir, readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import pg from 'pg';

const dir = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'db', 'migrations');
const url = process.env.DATABASE_ADMIN_URL;
const appPwd = process.env.DB_APP_PASSWORD;
if (!url) { console.error('Brak DATABASE_ADMIN_URL'); process.exit(1); }
if (!appPwd || appPwd.length < 16) { console.error('DB_APP_PASSWORD musi mieć co najmniej 16 znaków'); process.exit(1); }

let c;
for (let i = 0; ; i++) {                      // baza w Dockerze może startować kilka sekund – każda próba to nowe połączenie
  c = new pg.Client({ connectionString: url });
  try { await c.connect(); break; } catch (e) {
    await c.end().catch(() => {});
    if (i >= 30) { console.error('Brak połączenia z bazą po 30 próbach:', e.message); process.exit(1); }
    await new Promise(r => setTimeout(r, 1000));
  }
}
try {
  await c.query(`CREATE TABLE IF NOT EXISTS public.schema_migrations (name text PRIMARY KEY, sha256 text NOT NULL, applied_at timestamptz NOT NULL DEFAULT now())`);
  const done = new Map((await c.query('SELECT name, sha256 FROM public.schema_migrations')).rows.map(r => [r.name, r.sha256]));
  const files = (await readdir(dir)).filter(f => /^\d{4}_[a-z0-9_]+\.sql$/.test(f)).sort();
  for (const f of files) {
    const sql = await readFile(path.join(dir, f), 'utf8');
    const sum = createHash('sha256').update(sql).digest('hex');
    if (done.has(f)) {
      if (done.get(f) !== sum) throw new Error(`Migracja ${f} została zmieniona po wykonaniu – utwórz nową migrację zamiast zmieniać starą.`);
      continue;
    }
    console.log('→ migracja', f);
    await c.query(sql);                                        // plik zawiera własne BEGIN/COMMIT
    await c.query('INSERT INTO public.schema_migrations(name, sha256) VALUES ($1, $2)', [f, sum]);
  }
  // rola logowania aplikacji (hasło tylko ze zmiennej środowiskowej, nigdy w repozytorium)
  const exists = (await c.query(`SELECT 1 FROM pg_roles WHERE rolname = 'gabinet_web'`)).rowCount;
  const pw = c.escapeLiteral(appPwd);
  await c.query(exists ? `ALTER ROLE gabinet_web WITH LOGIN NOINHERIT NOBYPASSRLS PASSWORD ${pw}` : `CREATE ROLE gabinet_web WITH LOGIN NOINHERIT NOBYPASSRLS PASSWORD ${pw}`);
  await c.query('GRANT gabinet_app, gabinet_auth, gabinet_billing, gabinet_admin TO gabinet_web');
  await c.query(`REVOKE ALL ON SCHEMA public FROM gabinet_web`);
  console.log(`Baza gotowa: ${files.length} migracji, rola gabinet_web ustawiona.`);
} finally { await c.end(); }
