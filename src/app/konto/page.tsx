import Link from 'next/link';
import ActionForm from '@/components/ActionForm';
import { resendVerification, updateName } from '@/lib/auth/actions';
import { withUser } from '@/lib/db';
import { requireUser } from '@/lib/session';
export const metadata = { title: 'Konto – Gabinet' };
export const dynamic = 'force-dynamic';

const fmt = (d: Date | null) => d ? new Date(d).toLocaleDateString('pl-PL', { timeZone: 'Europe/Warsaw', day: 'numeric', month: 'long', year: 'numeric' }) : '';
const STATUS: Record<string, string> = {
  trial_active: 'Okres próbny', annual_active: 'Licencja roczna', lifetime_active: 'Licencja dożywotnia', expired: 'Licencja wygasła',
  suspended: 'Zawieszona', payment_pending: 'Oczekuje na płatność', payment_failed: 'Płatność nieudana',
};

export default async function Konto({ searchParams }: { searchParams: Promise<{ potwierdzono?: string }> }) {
  const s = await requireUser();
  const sp = await searchParams;
  // dane konta odczytywane rolą użytkownika – RLS zwraca wyłącznie jego własne wiersze
  const { sub, access } = await withUser(s.userId, async c => ({
    sub: (await c.query('SELECT status, trial_end, period_end FROM app.subscriptions')).rows[0] ?? null,
    access: (await c.query('SELECT app.has_access() AS a')).rows[0].a as boolean,
  }));
  return (
    <main className="wrap">
      <h1>Dzień dobry, {s.displayName}</h1>
      {sp.potwierdzono && <p className="msg ok" role="status">Adres e-mail potwierdzony.</p>}
      {!s.emailVerified && (
        <section className="card" aria-labelledby="ver">
          <h2 id="ver" style={{ marginTop: 0 }}>Potwierdź adres e-mail</h2>
          <p>Wysłaliśmy link na <strong>{s.email}</strong>. Bez potwierdzenia nie odzyskasz konta, gdy zapomnisz hasła.</p>
          <ActionForm action={resendVerification} submit="Wyślij link ponownie" pending="Wysyłam…" ghost />
        </section>
      )}
      <section className="card" aria-labelledby="lic">
        <h2 id="lic" style={{ marginTop: 0 }}>Dostęp</h2>
        {sub ? (<p><span className="badge">{STATUS[sub.status] ?? sub.status}</span>{' '}
          {sub.status === 'trial_active' && <>do <strong>{fmt(sub.trial_end)}</strong></>}
          {sub.status === 'annual_active' && <>do <strong>{fmt(sub.period_end)}</strong></>}</p>)
          : <p>Brak aktywnej licencji – okres próbny dla tego adresu e-mail został już wykorzystany.</p>}
        <p className="muted">{access ? 'Masz pełny dostęp.' : 'Zakup licencji będzie dostępny w kolejnej wersji (faza 5).'}</p>
      </section>
      <section className="card" aria-labelledby="dane">
        <h2 id="dane" style={{ marginTop: 0 }}>Twoje dane</h2>
        <p>E-mail: <strong>{s.email}</strong> {s.emailVerified ? <span className="badge">potwierdzony</span> : <span className="badge">niepotwierdzony</span>}</p>
        <ActionForm action={updateName} submit="Zapisz" pending="Zapisuję…" ghost>
          <label htmlFor="name">Imię i nazwisko</label>
          <input id="name" name="name" type="text" defaultValue={s.displayName} required maxLength={80} />
        </ActionForm>
      </section>
      <p><Link href="/konto/bezpieczenstwo">Bezpieczeństwo: hasło, weryfikacja dwuetapowa, urządzenia →</Link></p>
    </main>
  );
}
