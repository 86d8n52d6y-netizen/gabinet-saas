import Link from 'next/link';
import ActionForm from '@/components/ActionForm';
import PasswordFields from '@/components/PasswordFields';
import { register } from '@/lib/auth/actions';
export const metadata = { title: 'Załóż konto – Gabinet' };

export default function Rejestracja() {
  return (
    <main className="wrap narrow">
      <h1>Załóż konto</h1>
      <p className="muted">3 miesiące bezpłatnie, bez podawania karty.</p>
      <section className="card">
        <ActionForm action={register} submit="Załóż konto" pending="Zakładam konto…">
          <label htmlFor="name">Imię i nazwisko</label>
          <input id="name" name="name" type="text" autoComplete="name" required maxLength={80} />
          <label htmlFor="email">E-mail</label>
          <input id="email" name="email" type="email" autoComplete="email" required maxLength={254} />
          <PasswordFields />
          <label className="check"><input type="checkbox" name="zgoda" required />
            <span>Rozumiem, że w Gabinecie <strong>nie wpisuję danych pacjentów</strong> (imion, nazwisk, inicjałów, PESEL, adresów).</span></label>
        </ActionForm>
      </section>
      <p>Masz już konto? <Link href="/logowanie">Zaloguj się</Link></p>
    </main>
  );
}
