import 'server-only';
import { pool, withRole } from './db';

export type Check = { name: string; ok: boolean; info: string };

// Stan środowiska: połączenie z bazą, migracje, RLS włączony na tabelach użytkowników, rola aplikacji bez obejścia RLS.
export async function health(): Promise<Check[]> {
  const out: Check[] = [];
  try {
    const r = await pool().query('SELECT current_user AS u, version() AS v');
    out.push({ name: 'Połączenie z bazą PostgreSQL', ok: true, info: String(r.rows[0].v).split(',')[0] });
    out.push({ name: 'Aplikacja łączy się jako rola bez uprawnień do tabel', ok: r.rows[0].u === 'gabinet_web', info: r.rows[0].u });
  } catch (e) {
    out.push({ name: 'Połączenie z bazą PostgreSQL', ok: false, info: e instanceof Error ? e.message : String(e) });
    return out;
  }
  try {
    const t = await pool().query(`SELECT count(*)::int AS n, count(*) FILTER (WHERE relrowsecurity AND relforcerowsecurity)::int AS rls
      FROM pg_class c JOIN pg_namespace s ON s.oid = c.relnamespace WHERE s.nspname = 'app' AND c.relkind = 'r'`);
    const { n, rls } = t.rows[0];
    out.push({ name: 'Tabele schematu (migracje)', ok: n >= 25, info: `${n} tabel` });
    out.push({ name: 'Wymuszona izolacja wierszy (RLS)', ok: rls >= 19, info: `${rls} tabel z FORCE RLS` });
  } catch (e) { out.push({ name: 'Tabele schematu (migracje)', ok: false, info: e instanceof Error ? e.message : String(e) }); }
  try {
    await pool().query('SELECT 1 FROM app.procedures LIMIT 1');
    out.push({ name: 'Bez wybranej roli odczyt tabel zablokowany', ok: false, info: 'odczyt się udał – błąd konfiguracji uprawnień' });
  } catch { out.push({ name: 'Bez wybranej roli odczyt tabel zablokowany', ok: true, info: 'permission denied' }); }
  try {
    const n = await withRole('admin', c => c.query('SELECT users FROM app.usage_stats()'));
    out.push({ name: 'Rola administratora: tylko statystyki liczbowe', ok: true, info: `kont: ${n.rows[0].users}` });
  } catch (e) { out.push({ name: 'Rola administratora: tylko statystyki liczbowe', ok: false, info: e instanceof Error ? e.message : String(e) }); }
  return out;
}
