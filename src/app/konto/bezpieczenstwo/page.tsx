import ActionForm from '@/components/ActionForm';
import MfaSetup from '@/components/MfaSetup';
import PasswordFields from '@/components/PasswordFields';
import { changePassword, logoutAll, mfaDisable, revokeSession } from '@/lib/auth/actions';
import { mfaEnrollEnabled } from '@/lib/env';
import { withUser } from '@/lib/db';
import { requireUser } from '@/lib/session';
export const metadata = { title: 'Bezpieczeństwo – Gabinet' };
export const dynamic = 'force-dynamic';

const dt = (d: Date) => new Date(d).toLocaleString('pl-PL', { timeZone: 'Europe/Warsaw', dateStyle: 'short', timeStyle: 'short' });
const EV: Record<string, string> = {
  login_ok: 'Logowanie', login_fail: 'Nieudane logowanie', logout: 'Wylogowanie', logout_all: 'Wylogowanie ze wszystkich urządzeń',
  new_device: 'Nowe urządzenie', password_reset: 'Reset hasła', password_change: 'Zmiana hasła', mfa_on: 'Włączono 2FA', mfa_off: 'Wyłączono 2FA',
  email_verified: 'Potwierdzono e-mail', blocked: 'Próba logowania na zablokowane konto', rate_limited: 'Zbyt wiele prób', register: 'Założenie konta',
  reset_requested: 'Prośba o reset hasła', mfa_fail: 'Błędny kod 2FA', recovery_code_used: 'Użyto kodu zapasowego', suspicious: 'Podejrzana aktywność',
};

export default async function Bezpieczenstwo({ searchParams }: { searchParams: Promise<{ mfa?: string }> }) {
  const s = await requireUser();
  const sp = await searchParams;
  const { sessions, events } = await withUser(s.userId, async c => ({
    sessions: (await c.query(`SELECT id, device_label, created_at, last_seen_at FROM app.sessions
                               WHERE revoked_at IS NULL AND expires_at > now() ORDER BY last_seen_at DESC`)).rows,
    events: (await c.query(`SELECT type, device_label, created_at FROM app.security_events ORDER BY created_at DESC LIMIT 15`)).rows,
  }));
  return (
    <main className="wrap">
      <h1>Bezpieczeństwo</h1>
      {sp.mfa === 'wylaczone' && <p className="msg ok" role="status">Weryfikacja dwuetapowa wyłączona.</p>}

      <section className="card" aria-labelledby="dev">
        <h2 id="dev" style={{ marginTop: 0 }}>Zalogowane urządzenia</h2>
        <table>
          <thead><tr><th>Urządzenie</th><th>Ostatnio</th><th></th></tr></thead>
          <tbody>{sessions.map(x => (
            <tr key={x.id}>
              <td>{x.device_label} {x.id === s.id && <span className="badge">to urządzenie</span>}</td>
              <td className="muted">{dt(x.last_seen_at)}</td>
              <td style={{ textAlign: 'right' }}><form action={revokeSession}><input type="hidden" name="id" value={x.id} /><button className="ghost" type="submit">Wyloguj</button></form></td>
            </tr>))}
          </tbody>
        </table>
        <form action={logoutAll}><div className="row"><button className="danger" type="submit">Wyloguj ze wszystkich urządzeń</button></div></form>
      </section>

      {/* 2FA: włączanie wyłączone (decyzja 21.11.2026, env MFA_ENROLL); konto, które już ma 2FA, widzi tylko jego wyłączenie */}
      {(s.mfaOn || mfaEnrollEnabled()) && <section className="card" aria-labelledby="mfa">
        <h2 id="mfa" style={{ marginTop: 0 }}>Weryfikacja dwuetapowa {s.mfaOn && <span className="badge">włączona</span>}</h2>
        {s.mfaOn ? (
          <ActionForm action={mfaDisable} submit="Wyłącz weryfikację dwuetapową" pending="Wyłączam…" danger>
            <p className="muted">Aby wyłączyć, podaj hasło i aktualny kod z aplikacji (albo kod zapasowy).</p>
            <label htmlFor="d-cur">Obecne hasło</label>
            <input id="d-cur" name="current" type="password" autoComplete="current-password" required maxLength={128} />
            <label htmlFor="d-code">Kod</label>
            <input id="d-code" name="code" type="text" inputMode="numeric" autoComplete="one-time-code" required maxLength={20} />
          </ActionForm>
        ) : <MfaSetup />}
      </section>}

      <section className="card" aria-labelledby="pwd">
        <h2 id="pwd" style={{ marginTop: 0 }}>Zmiana hasła</h2>
        <ActionForm action={changePassword} submit="Zmień hasło" pending="Zmieniam…">
          <label htmlFor="current">Obecne hasło</label>
          <input id="current" name="current" type="password" autoComplete="current-password" required maxLength={128} />
          <PasswordFields label="Nowe hasło" />
        </ActionForm>
      </section>

      <section className="card" aria-labelledby="hist">
        <h2 id="hist" style={{ marginTop: 0 }}>Ostatnie zdarzenia</h2>
        <table><tbody>{events.map((e, i) => (
          <tr key={i}><td>{EV[e.type] ?? e.type}</td><td className="muted">{e.device_label}</td><td className="muted">{dt(e.created_at)}</td></tr>))}
        </tbody></table>
        <p className="hint">Przechowujemy tylko skrócony adres sieci (bez pełnego IP), usuwany po 90 dniach.</p>
      </section>
    </main>
  );
}
