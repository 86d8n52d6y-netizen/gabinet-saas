import ActionForm from '@/components/ActionForm';
import PasswordFields from '@/components/PasswordFields';
import { resetPassword } from '@/lib/auth/actions';
export const metadata = { title: 'Nowe hasło – Gabinet', referrer: 'no-referrer' };

export default async function NoweHaslo({ searchParams }: { searchParams: Promise<{ t?: string }> }) {
  const { t = '' } = await searchParams;
  return (
    <main className="wrap narrow">
      <h1>Ustaw nowe hasło</h1>
      <section className="card">
        <ActionForm action={resetPassword} submit="Zapisz nowe hasło" pending="Zapisuję…">
          <input type="hidden" name="t" value={t} />
          <PasswordFields label="Nowe hasło" />
          <p className="hint">Po zmianie wylogujemy wszystkie urządzenia.</p>
        </ActionForm>
      </section>
    </main>
  );
}
