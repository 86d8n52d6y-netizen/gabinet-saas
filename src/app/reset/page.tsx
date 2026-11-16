import Link from 'next/link';
import ActionForm from '@/components/ActionForm';
import { requestReset } from '@/lib/auth/actions';
export const metadata = { title: 'Nie pamiętam hasła – Gabinet' };

export default function Reset() {
  return (
    <main className="wrap narrow">
      <h1>Nie pamiętam hasła</h1>
      <section className="card">
        <ActionForm action={requestReset} submit="Wyślij link" pending="Wysyłam…">
          <label htmlFor="email">E-mail konta</label>
          <input id="email" name="email" type="email" autoComplete="email" required maxLength={254} />
        </ActionForm>
      </section>
      <p><Link href="/logowanie">Wróć do logowania</Link></p>
    </main>
  );
}
