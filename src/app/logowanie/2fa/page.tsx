import { redirect } from 'next/navigation';
import ActionForm from '@/components/ActionForm';
import { loginMfa } from '@/lib/auth/actions';
import { getSession } from '@/lib/session';
export const metadata = { title: 'Kod weryfikacyjny – Gabinet' };

export default async function Mfa() {
  const s = await getSession();
  if (!s) redirect('/logowanie');
  if (s.mfaPassed) redirect('/konto');
  return (
    <main className="wrap narrow">
      <h1>Weryfikacja dwuetapowa</h1>
      <section className="card">
        <ActionForm action={loginMfa} submit="Potwierdź" pending="Sprawdzam…">
          <label htmlFor="code">Kod z aplikacji (6 cyfr)</label>
          <input id="code" name="code" type="text" inputMode="numeric" autoComplete="one-time-code" required maxLength={20} autoFocus />
          <p className="hint">Nie masz telefonu? Wpisz jeden z kodów zapasowych (np. abcde-fghjk).</p>
        </ActionForm>
      </section>
    </main>
  );
}
