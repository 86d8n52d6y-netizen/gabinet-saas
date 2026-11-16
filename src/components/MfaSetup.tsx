'use client';
// Włączanie weryfikacji dwuetapowej: 1) hasło → kod QR, 2) kod z aplikacji → kody zapasowe (pokazywane jeden raz).
import { useActionState } from 'react';
import { mfaConfirm, mfaStart } from '@/lib/auth/actions';
import type { State } from '@/lib/auth/core';

export default function MfaSetup() {
  const [a, start, busyA] = useActionState(mfaStart, {} as State);
  const [b, confirm, busyB] = useActionState(mfaConfirm, {} as State);
  if (b.codes) return (
    <div>
      <p className="msg ok" role="status">{b.ok}</p>
      <p><strong>Zapisz kody zapasowe</strong> (np. wydrukuj albo zapisz w menedżerze haseł). Każdy działa jeden raz – gdy nie masz telefonu.
        Nie pokażemy ich ponownie.</p>
      <div className="codes" aria-label="Kody zapasowe">{b.codes.map(c => <span key={c}>{c}</span>)}</div>
      <div className="row"><a className="btn" href="/konto/bezpieczenstwo">Zapisałem kody</a></div>
    </div>
  );
  if (!a.qr) return (
    <form action={start}>
      <p className="muted">Po włączeniu przy logowaniu podasz też 6-cyfrowy kod z aplikacji w telefonie (Google Authenticator, Microsoft Authenticator, 1Password, Bitwarden…).</p>
      <label htmlFor="mfa-cur">Obecne hasło</label>
      <input id="mfa-cur" name="current" type="password" autoComplete="current-password" required maxLength={128} />
      {a.error && <p className="msg err" role="alert">{a.error}</p>}
      <div className="row"><button type="submit" disabled={busyA}>{busyA ? 'Proszę czekać…' : 'Włącz weryfikację dwuetapową'}</button></div>
    </form>
  );
  return (
    <form action={confirm}>
      <p>1. Zeskanuj kod aplikacją w telefonie:</p>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="qr" src={a.qr} alt="Kod QR do aplikacji uwierzytelniającej" />
      <p className="hint">Albo wpisz klucz ręcznie: <span className="mono">{a.secret}</span></p>
      <label htmlFor="mfa-code">2. Wpisz 6-cyfrowy kod z aplikacji</label>
      <input id="mfa-code" name="code" type="text" inputMode="numeric" autoComplete="one-time-code" required maxLength={7} />
      {b.error && <p className="msg err" role="alert">{b.error}</p>}
      <div className="row"><button type="submit" disabled={busyB}>{busyB ? 'Sprawdzam…' : 'Potwierdź i włącz'}</button></div>
    </form>
  );
}
