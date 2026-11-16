import Link from 'next/link';
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/session';
export const dynamic = 'force-dynamic';

export default async function Home() {
  const s = await getSession();
  if (s?.mfaPassed) redirect('/konto');
  return (
    <main className="wrap">
      <h1>Gabinet</h1>
      <p className="muted">Opisy zabiegów NFZ i prywatnych, procedury, zestawy, zarobki i kalendarz dyżurów – na każdym urządzeniu.</p>
      <section className="card">
        <p><strong>Wersja testowa (faza 3: konta i logowanie).</strong> Moduły pracy pojawią się w fazie 4.</p>
        <p className="muted">Gabinet nie przechowuje danych pacjentów. Treść opisów zostaje na Twoim urządzeniu.</p>
        <div className="row"><Link className="btn" href="/rejestracja">Załóż konto – 3 miesiące za darmo</Link><Link className="btn ghost" href="/logowanie">Zaloguj się</Link></div>
      </section>
    </main>
  );
}
