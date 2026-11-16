import Link from 'next/link';
import { redirect } from 'next/navigation';
import ActionForm from '@/components/ActionForm';
import { login } from '@/lib/auth/actions';
import { getSession } from '@/lib/session';
export const metadata = { title: 'Logowanie – Gabinet' };

const INFO: Record<string, string> = {
  'wylogowano=1': 'Wylogowano.', 'wylogowano=wszedzie': 'Wylogowano ze wszystkich urządzeń.',
  'potwierdzono=1': 'Adres e-mail potwierdzony. Możesz się zalogować.', 'haslo=zmienione': 'Hasło zmienione. Zaloguj się nowym hasłem.',
};

export default async function Logowanie({ searchParams }: { searchParams: Promise<Record<string, string>> }) {
  const s = await getSession();
  if (s?.mfaPassed) redirect('/konto');
  const sp = await searchParams;
  const info = Object.entries(sp).map(([k, v]) => INFO[`${k}=${v}`]).find(Boolean);
  return (
    <main className="wrap narrow">
      <h1>Logowanie</h1>
      {info && <p className="msg ok" role="status">{info}</p>}
      <section className="card">
        <ActionForm action={login} submit="Zaloguj" pending="Loguję…">
          <label htmlFor="email">E-mail</label>
          <input id="email" name="email" type="email" autoComplete="username" required maxLength={254} />
          <label htmlFor="password">Hasło</label>
          <input id="password" name="password" type="password" autoComplete="current-password" required maxLength={128} />
        </ActionForm>
      </section>
      <p><Link href="/reset">Nie pamiętam hasła</Link> · <Link href="/rejestracja">Załóż konto</Link></p>
    </main>
  );
}
