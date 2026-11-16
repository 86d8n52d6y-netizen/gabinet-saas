import Link from 'next/link';
import ActionForm from '@/components/ActionForm';
import { resendVerification, updateName } from '@/lib/auth/actions';
import { withUser } from '@/lib/db';
import { fmtC } from '@/lib/nfz/engine';
import { rangeOf, report, todayPL } from '@/lib/zarobki';
import { todayShifts } from '@/lib/kal';
import { requireUser } from '@/lib/session';
export const metadata = { title: 'Konto – Gabinet' };
export const dynamic = 'force-dynamic';

const fmt = (d: Date | null) => d ? new Date(d).toLocaleDateString('pl-PL', { timeZone: 'Europe/Warsaw', day: 'numeric', month: 'long', year: 'numeric' }) : '';
const STATUS: Record<string, string> = {
  trial_active: 'Okres próbny', annual_active: 'Licencja roczna', lifetime_active: 'Licencja dożywotnia', expired: 'Licencja wygasła',
  suspended: 'Zawieszona', payment_pending: 'Oczekuje na płatność', payment_failed: 'Płatność nieudana',
};

export default async function Konto({ searchParams }: { searchParams: Promise<{ potwierdzono?: string; dostep?: string }> }) {
  const s = await requireUser();
  const sp = await searchParams;
  // dane konta odczytywane rolą użytkownika – RLS zwraca wyłącznie jego własne wiersze
  const { sub, access, dzis, dyz } = await withUser(s.userId, async c => {
    const access = (await c.query('SELECT app.has_access() AS a')).rows[0].a as boolean;
    return { sub: (await c.query('SELECT status, trial_end, period_end FROM app.subscriptions')).rows[0] ?? null, access,
      dzis: access ? (await report(c, rangeOf('today'), null)).total : null, dyz: access ? await todayShifts(c, todayPL()) : [] };
  });
  const wiz = (n: number) => n + ' ' + (n === 1 ? 'wizyta' : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 12 || n % 100 > 14)) ? 'wizyty' : 'wizyt');
  return (
    <main className="wrap">
      <h1>Dzień dobry, {s.displayName}</h1>
      {sp.potwierdzono && <p className="msg ok" role="status">Adres e-mail potwierdzony.</p>}
      {sp.dostep === 'brak' && <p className="msg err" role="alert">Ta część aplikacji wymaga aktywnej licencji lub okresu próbnego.</p>}
      {dzis && (
        <nav className="g-tiles" aria-label="Moduły">
          <a className="tile" href="/kalendarz"><b>Kalendarz</b><span className="muted">{dyz.length ? `Dziś: ${dyz.join(', ')}` : 'Dziś bez dyżuru'}</span></a>
          <a className="tile" href="/opisy-nfz"><b>Opisy NFZ</b><span className="muted">{dzis.nv ? `Dziś: ${wiz(dzis.nv)} · ${fmtC(dzis.e1)}` : 'Dziś brak zapisanych wizyt'}</span></a>
          <a className="tile" href="/opisy-prywatne"><b>Opisy prywatne</b><span className="muted">{dzis.pv ? `Dziś: ${wiz(dzis.pv)} · ${fmtC(dzis.e2)}` : 'Dziś brak zapisanych wizyt'}</span></a>
          <Link className="tile" href="/zarobki"><b>Zarobki</b><span className="muted">{dzis.sum ? `Dziś razem: ${fmtC(dzis.sum)}` : 'Wszystkie gabinety, okresy, CSV'}</span></Link>
        </nav>)}
      {dzis && <p className="hint">Masz dane w starej aplikacji? <a href="/import">Przenieś dane ze starej aplikacji</a> (plik „Kopia całości”).</p>}
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
        <p className="muted">{access ? 'Masz pełny dostęp.' : 'Wersja testowa: okres próbny trwa 3 miesiące. Zakup licencji zostanie dodany po zakończeniu testów.'}</p>
      </section>
      <section className="card" aria-labelledby="dane">
        <h2 id="dane" style={{ marginTop: 0 }}>Twoje dane</h2>
        <p>E-mail: <strong>{s.email}</strong> {s.emailVerified ? <span className="badge">potwierdzony</span> : <span className="badge">niepotwierdzony</span>}</p>
        <ActionForm action={updateName} submit="Zapisz" pending="Zapisuję…" ghost>
          <label htmlFor="name">Imię i nazwisko</label>
          <input id="name" name="name" type="text" defaultValue={s.displayName} required maxLength={80} />
        </ActionForm>
      </section>
      {access && <section className="card"><h2 style={{ marginTop: 0 }}>Na początek</h2>
        <p>1. <Link href="/gabinety">Dodaj gabinety</Link>, w których pracujesz. 2. Sprawdź <Link href="/ustawienia">stawki rozliczeń</Link>. 3. Wpisuj dyżury w <a href="/kalendarz">Kalendarzu</a>, pracuj w <a href="/opisy-nfz">Opisach NFZ</a> i <a href="/opisy-prywatne">Opisach prywatnych</a> – zarobki zbierają się w <Link href="/zarobki">Zarobkach</Link>.</p>
        <p className="muted">Kalendarz dyżurów i przeniesienie danych z obecnej aplikacji – w kolejnym etapie.</p></section>}
      <p><Link href="/konto/bezpieczenstwo">Bezpieczeństwo: hasło, weryfikacja dwuetapowa, urządzenia →</Link></p>
    </main>
  );
}
