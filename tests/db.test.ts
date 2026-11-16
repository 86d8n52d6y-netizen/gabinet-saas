// Warstwa dostępu do bazy (src/lib/db.ts) na prawdziwym PostgreSQL: izolacja kont przez withUser, role, brak „wycieku” użytkownika między połączeniami.
// Wymaga DATABASE_URL (rola gabinet_web) i bazy po migracjach.
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { randomUUID } from 'node:crypto';
import { pool, withRole, withUser } from '@/lib/db';

const A = randomUUID(), B = randomUUID();
const H = '$argon2id$v=19$m=65536,t=3,p=4$test';

beforeAll(async () => {
  await withRole('auth', async c => {
    for (const [id, e] of [[A, `a-${A}@test.pl`], [B, `b-${B}@test.pl`]]) {
      await c.query('INSERT INTO app.profiles(id,email,password_hash,display_name) VALUES ($1,$2,$3,$4)', [id, e, H, 'Lekarz']);
      await c.query(`INSERT INTO app.subscriptions(user_id,plan,status,trial_start,trial_end,updated_by) VALUES ($1,'trial','trial_active',now(),now()+interval '3 months','system')`, [id]);
    }
  });
  for (const u of [A, B]) await withUser(u, c => c.query(`INSERT INTO app.procedures(owner_id,kind,name) VALUES ($1,'private',$2)`, [u, 'Procedura ' + u.slice(0, 4)]));
});
afterAll(async () => { await pool().end(); });

describe('izolacja kont w warstwie aplikacji', () => {
  it('użytkownik widzi tylko swoje procedury', async () => {
    const r = await withUser(A, c => c.query('SELECT owner_id FROM app.procedures'));
    expect(r.rows.map(x => x.owner_id)).toEqual([A]);
  });
  it('próba odczytu cudzej procedury po identyfikatorze zwraca 0 wierszy', async () => {
    const idB = (await withUser(B, c => c.query('SELECT id FROM app.procedures'))).rows[0].id;
    const r = await withUser(A, c => c.query('SELECT * FROM app.procedures WHERE id = $1', [idB]));
    expect(r.rowCount).toBe(0);
  });
  it('wstawienie danych z cudzym owner_id jest odrzucane przez bazę', async () => {
    await expect(withUser(A, c => c.query(`INSERT INTO app.procedures(owner_id,kind,name) VALUES ($1,'private','X')`, [B]))).rejects.toThrow(/row-level security/);
  });
  it('nieprawidłowy identyfikator (próba wstrzyknięcia SQL) jest odrzucany przed zapytaniem', async () => {
    await expect(withUser("x'; DROP TABLE app.procedures; --", c => c.query('SELECT 1'))).rejects.toThrow(/identyfikator/);
  });
  it('identyfikator użytkownika nie „przecieka” do kolejnego zapytania na tym samym połączeniu', async () => {
    await withUser(A, c => c.query('SELECT 1'));
    const r = await pool().query(`SELECT coalesce(current_setting('app.user_id', true), '') AS u, current_user AS r`);
    expect(r.rows[0]).toEqual({ u: '', r: 'gabinet_web' });
  });
  it('bez withUser/withRole aplikacja nie odczyta żadnej tabeli', async () => {
    await expect(pool().query('SELECT * FROM app.procedures')).rejects.toThrow(/permission denied/);
  });
  it('użytkownik nie zmieni sobie licencji; serwer sprawdza dostęp', async () => {
    await expect(withUser(A, c => c.query(`UPDATE app.subscriptions SET status='lifetime_active'`))).rejects.toThrow(/permission denied/);
    const r = await withUser(A, c => c.query('SELECT app.has_access() AS ok'));
    expect(r.rows[0].ok).toBe(true);
  });
  it('błąd w transakcji cofa wszystkie zmiany (brak połowicznych zapisów)', async () => {
    await expect(withUser(A, async c => {
      await c.query(`INSERT INTO app.procedures(owner_id,kind,name) VALUES ($1,'private','Częściowa')`, [A]);
      throw new Error('przerwane');
    })).rejects.toThrow('przerwane');
    const r = await withUser(A, c => c.query(`SELECT count(*)::int AS n FROM app.procedures WHERE name='Częściowa'`));
    expect(r.rows[0].n).toBe(0);
  });
  it('administrator nie czyta procedur użytkowników', async () => {
    await expect(withRole('admin', c => c.query('SELECT * FROM app.procedures'))).rejects.toThrow(/permission denied/);
  });
});
