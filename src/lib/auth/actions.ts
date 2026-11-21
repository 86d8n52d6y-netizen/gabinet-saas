'use server';
// Akcje kont wywoływane z formularzy (Next.js Server Actions – Next sprawdza nagłówek Origin, co chroni przed CSRF).
// Zasady: komunikaty nie zdradzają, czy konto istnieje; limity prób; wszystkie zmiany bezpieczeństwa w dzienniku
// security_events; redirect() zawsze PO zakończeniu transakcji.
import { redirect } from 'next/navigation';
import QRCode from 'qrcode';
import { withRole, withUser } from '../db';
import { randomInt } from 'node:crypto';
import { decrypt, encrypt, sha256 } from '../crypto';
import { sendMail } from '../mail';
import { breachCount, hashPassword, passwordProblem, verifyPassword, MAX_LEN } from '../password';
import { clientInfo } from '../request';
import { blocked, clear, hit } from '../ratelimit';
import { mfaEnrollEnabled } from '../env';
import { base32, base32Decode, newTotpSecret, otpauthUri, verifyTotp } from '../totp';
import { clearCookie, createSession, getSession, requireUser, sessionTokenHash } from '../session';
import { mails } from './emails';
import { emailOk, ev, newEmailToken, normEmail, pgUnique, recoveryHash, str, trialKey, useEmailToken, type State } from './core';

const RC = 'abcdefghjkmnpqrstuvwxyz23456789';                       // kody zapasowe: bez znaków mylących (0/o, 1/l/i)
const TOO_MANY = 'Zbyt wiele prób. Odczekaj chwilę (do 15–60 minut) i spróbuj ponownie.';

async function checkNewPassword(pwd: string, pwd2: string, email: string): Promise<string | null> {
  if (pwd !== pwd2) return 'Hasła nie są takie same.';
  const p = passwordProblem(pwd, email);
  if (p) return p;
  const n = await breachCount(pwd);
  if (n && n > 0) return `To hasło pojawiło się w znanych wyciekach danych (${n.toLocaleString('pl-PL')} razy). Wybierz inne.`;
  return null;
}

// ---------------- rejestracja ----------------
export async function register(_: State, fd: FormData): Promise<State> {
  const name = str(fd, 'name', 100).trim(), email = normEmail(str(fd, 'email', 300));
  const pwd = str(fd, 'password', MAX_LEN + 1), pwd2 = str(fd, 'password2', MAX_LEN + 1);
  if (!name || name.length > 80) return { error: 'Podaj imię i nazwisko (do 80 znaków).', field: 'name' };
  if (!emailOk(email)) return { error: 'Podaj poprawny adres e-mail.', field: 'email' };
  if (fd.get('zgoda') !== 'on') return { error: 'Zaznacz potwierdzenie, że nie będziesz wpisywać danych pacjentów.', field: 'zgoda' };
  const { ip, device } = await clientInfo();
  if (await withRole('auth', c => hit(c, 'register:ip', ip))) return { error: TOO_MANY };
  const problem = await checkNewPassword(pwd, pwd2, email);
  if (problem) return { error: problem, field: 'password' };
  const hash = await hashPassword(pwd);

  const out = await withRole('auth', async c => {
    const ex = await c.query('SELECT 1 FROM app.profiles WHERE email = $1', [email]);
    if (ex.rowCount) return { exists: true as const };
    let id: string;
    try {
      id = (await c.query(`INSERT INTO app.profiles(email, password_hash, display_name) VALUES ($1, $2, $3) RETURNING id`, [email, hash, name])).rows[0].id;
    } catch (e) { if (pgUnique(e)) return { exists: true as const }; throw e; }
    await c.query('INSERT INTO app.user_settings(user_id) VALUES ($1)', [id]);
    // Wersja testowa (bez limitu czasu – migracja 0007) dla każdego nowego konta, także przy ponownej rejestracji
    // tym samym e-mailem po usunięciu konta (decyzja Patryka 21.11.2026). Rejestr skrótów HMAC nadal zapisujemy
    // (pierwsza rejestracja), żeby przy powrocie licencji dało się przywrócić zasadę „okres próbny raz na e-mail”.
    const tk = trialKey(email);
    const had = await c.query('SELECT 1 FROM app.trial_registry WHERE email_hmac = $1', [tk]);
    if (!had.rowCount) await c.query('INSERT INTO app.trial_registry(email_hmac) VALUES ($1)', [tk]);
    await c.query(`INSERT INTO app.subscriptions(user_id, plan, status, trial_start, trial_end, updated_by)
                   VALUES ($1, 'trial', 'trial_active', now(), now() + interval '3 months', 'system')`, [id]);
    await ev(c, 'register', id, ip, device, { trial: true, ponowna: !!had.rowCount });
    return { exists: false as const, token: await newEmailToken(c, id, 'verify', '24 hours') };
  });
  const m = out.exists ? mails.alreadyRegistered() : mails.verify(name, out.token);
  await sendMail(email, m.subject, m.text);
  redirect('/rejestracja/sprawdz-poczte');                              // ta sama odpowiedź, gdy konto już istniało
}

// ---------------- logowanie ----------------
async function newDeviceMail(c: import('pg').PoolClient, userId: string, device: string) {
  const r = await c.query(`SELECT count(*)::int AS all, count(*) FILTER (WHERE device_label = $2)::int AS same
                             FROM app.sessions WHERE user_id = $1 AND mfa_passed`, [userId, device]);
  return r.rows[0].all > 0 && r.rows[0].same === 0;
}

export async function login(_: State, fd: FormData): Promise<State> {
  const email = normEmail(str(fd, 'email', 300)), pwd = str(fd, 'password', MAX_LEN + 1);
  if (!emailOk(email) || !pwd) return { error: 'Podaj e-mail i hasło.' };
  const { ip, device } = await clientInfo();
  const res = await withRole('auth', async c => {
    if (await blocked(c, 'login:email', email) || await hit(c, 'login:ip', ip)) {
      await ev(c, 'rate_limited', null, ip, device, { what: 'login' });
      return { error: TOO_MANY };
    }
    const r = await c.query(`SELECT id, password_hash, status, mfa_secret_enc IS NOT NULL AS mfa FROM app.profiles WHERE email = $1 AND status <> 'deleted'`, [email]);
    const u = r.rows[0];
    if (!(await verifyPassword(u?.password_hash ?? null, pwd))) {
      await hit(c, 'login:email', email);
      await ev(c, 'login_fail', u?.id ?? null, ip, device);
      return { error: 'Nieprawidłowy e-mail lub hasło.' };
    }
    if (u.status !== 'active') { await ev(c, 'blocked', u.id, ip, device); return { error: 'To konto jest zablokowane. Skontaktuj się z obsługą Gabinetu.' }; }
    await clear(c, 'login:email', email);
    const notify = !u.mfa && await newDeviceMail(c, u.id, device);
    await createSession(c, u.id, { mfaPassed: !u.mfa, ip, device });
    if (!u.mfa) await ev(c, 'login_ok', u.id, ip, device);
    if (notify) await ev(c, 'new_device', u.id, ip, device);
    if (Math.random() < 0.05) await c.query('SELECT app.auth_cleanup()');          // sprzątanie (tokeny, sesje, IP > 90 dni)
    return { mfa: u.mfa as boolean, notify };
  });
  if ('error' in res) return res;
  if (res.notify) { const m = mails.newDevice(device); await sendMail(email, m.subject, m.text); }
  redirect(res.mfa ? '/logowanie/2fa' : '/konto');
}

/** Sprawdza kod 2FA albo kod zapasowy; zwraca true, jeśli poprawny (i zużywa go). */
async function checkSecondFactor(c: import('pg').PoolClient, userId: string, code: string): Promise<'totp' | 'recovery' | null> {
  const p = (await c.query('SELECT mfa_secret_enc, mfa_last_step FROM app.profiles WHERE id = $1', [userId])).rows[0];
  if (!p?.mfa_secret_enc) return null;
  const clean = code.trim();
  if (/^\d{3}\s?\d{3}$/.test(clean)) {
    const secret = decrypt(p.mfa_secret_enc, 'mfa:' + userId);
    const step = verifyTotp(secret, clean, p.mfa_last_step === null ? null : Number(p.mfa_last_step));
    if (step === null) return null;
    await c.query('UPDATE app.profiles SET mfa_last_step = $2 WHERE id = $1', [userId, step]);
    return 'totp';
  }
  const r = await c.query('UPDATE app.mfa_recovery_codes SET used_at = now() WHERE user_id = $1 AND code_hash = $2 AND used_at IS NULL RETURNING 1',
    [userId, recoveryHash(userId, clean)]);
  return r.rowCount ? 'recovery' : null;
}

export async function loginMfa(_: State, fd: FormData): Promise<State> {
  const s = await getSession();
  if (!s) redirect('/logowanie');
  if (s.mfaPassed) redirect('/konto');
  const code = str(fd, 'code', 40);
  const { ip, device } = await clientInfo();
  const res = await withRole('auth', async c => {
    if (await blocked(c, 'mfa:user', s.userId)) {
      await c.query('UPDATE app.sessions SET revoked_at = now() WHERE id = $1', [s.id]);
      return { error: TOO_MANY + ' Zaloguj się ponownie.', out: true };
    }
    const kind = await checkSecondFactor(c, s.userId, code);
    if (!kind) { await hit(c, 'mfa:user', s.userId); await ev(c, 'mfa_fail', s.userId, ip, device); return { error: 'Nieprawidłowy kod.' }; }
    await clear(c, 'mfa:user', s.userId);
    if (kind === 'recovery') await ev(c, 'recovery_code_used', s.userId, ip, device);
    const notify = await newDeviceMail(c, s.userId, device);
    await c.query('UPDATE app.sessions SET revoked_at = now() WHERE id = $1', [s.id]);          // nowa sesja po 2FA (nowy token)
    await createSession(c, s.userId, { mfaPassed: true, ip, device });
    await ev(c, 'login_ok', s.userId, ip, device, { mfa: kind });
    if (notify) await ev(c, 'new_device', s.userId, ip, device);
    return { notify };
  });
  if ('error' in res) { if (res.out) await clearCookie(); return { error: res.error }; }
  if (res.notify) { const m = mails.newDevice(device); await sendMail(s.email, m.subject, m.text); }
  redirect('/konto');
}

// ---------------- wylogowanie i urządzenia ----------------
export async function logout(): Promise<void> {
  const th = await sessionTokenHash();
  const { ip, device } = await clientInfo();
  if (th) await withRole('auth', async c => {
    const r = await c.query('UPDATE app.sessions SET revoked_at = now() WHERE token_hash = $1 AND revoked_at IS NULL RETURNING user_id', [th]);
    if (r.rows[0]) await ev(c, 'logout', r.rows[0].user_id, ip, device);
  });
  await clearCookie();
  redirect('/logowanie?wylogowano=1');
}

export async function logoutAll(): Promise<void> {
  const s = await requireUser();
  const { ip, device } = await clientInfo();
  await withRole('auth', async c => {
    await c.query('UPDATE app.sessions SET revoked_at = now() WHERE user_id = $1 AND revoked_at IS NULL', [s.userId]);
    await ev(c, 'logout_all', s.userId, ip, device);
  });
  await clearCookie();
  redirect('/logowanie?wylogowano=wszedzie');
}

/** Wylogowanie jednego urządzenia – przez rolę użytkownika (RLS: tylko własne sesje). */
export async function revokeSession(fd: FormData): Promise<void> {
  const s = await requireUser();
  const id = str(fd, 'id', 40);
  if (!/^[0-9a-f-]{36}$/i.test(id)) return;
  await withUser(s.userId, c => c.query('UPDATE app.sessions SET revoked_at = now() WHERE id = $1 AND revoked_at IS NULL', [id]));
  if (id === s.id) { await clearCookie(); redirect('/logowanie?wylogowano=1'); }
  redirect('/konto/bezpieczenstwo');
}

// ---------------- weryfikacja e-mail ----------------
export async function verifyEmail(_: State, fd: FormData): Promise<State> {
  const token = str(fd, 't', 100);
  const { ip, device } = await clientInfo();
  const ok = await withRole('auth', async c => {
    const uid = await useEmailToken(c, token, 'verify');
    if (!uid) return false;
    await c.query('UPDATE app.profiles SET email_verified_at = coalesce(email_verified_at, now()), updated_at = now() WHERE id = $1', [uid]);
    await ev(c, 'email_verified', uid, ip, device);
    return true;
  });
  if (!ok) return { error: 'Link jest nieprawidłowy, wygasł albo został już użyty. Zaloguj się i wyślij nowy link.' };
  redirect((await getSession()) ? '/konto?potwierdzono=1' : '/logowanie?potwierdzono=1');
}

export async function resendVerification(_: State): Promise<State> {
  const s = await requireUser();
  if (s.emailVerified) return { ok: 'Adres e-mail jest już potwierdzony.' };
  const token = await withRole('auth', async c => (await hit(c, 'verify:user', s.userId)) ? null : newEmailToken(c, s.userId, 'verify', '24 hours'));
  if (!token) return { error: TOO_MANY };
  const m = mails.verify(s.displayName, token);
  await sendMail(s.email, m.subject, m.text);
  return { ok: 'Wysłaliśmy nowy link. Sprawdź skrzynkę (także folder spam).' };
}

// ---------------- reset hasła ----------------
export async function requestReset(_: State, fd: FormData): Promise<State> {
  const email = normEmail(str(fd, 'email', 300));
  if (!emailOk(email)) return { error: 'Podaj poprawny adres e-mail.' };
  const { ip, device } = await clientInfo();
  const OK = { ok: 'Jeśli konto z tym adresem istnieje, wysłaliśmy link do ustawienia nowego hasła (ważny 30 minut). Sprawdź skrzynkę.' };
  const token = await withRole('auth', async c => {
    if (await hit(c, 'reset:ip', ip) || await hit(c, 'reset:email', email)) return 'limit' as const;
    const u = (await c.query(`SELECT id FROM app.profiles WHERE email = $1 AND status = 'active'`, [email])).rows[0];
    if (!u) return null;
    await ev(c, 'reset_requested', u.id, ip, device);
    return newEmailToken(c, u.id, 'reset', '30 minutes');
  });
  if (token === 'limit') return { error: TOO_MANY };
  if (token) { const m = mails.reset(token); await sendMail(email, m.subject, m.text); }
  return OK;
}

export async function resetPassword(_: State, fd: FormData): Promise<State> {
  const token = str(fd, 't', 100), pwd = str(fd, 'password', MAX_LEN + 1), pwd2 = str(fd, 'password2', MAX_LEN + 1);
  if (!/^[A-Za-z0-9_-]{43}$/.test(token)) return { error: 'Link jest nieprawidłowy. Poproś o nowy.' };
  // e-mail potrzebny do zasad hasła – odczyt bez zużywania tokenu
  const email = await withRole('auth', async c => (await c.query(
    `SELECT p.email FROM app.email_tokens t JOIN app.profiles p ON p.id = t.user_id
      WHERE t.token_hash = $1 AND t.purpose = 'reset' AND t.used_at IS NULL AND t.expires_at > now() AND p.status = 'active'`,
    [sha256(token)])).rows[0]?.email as string | undefined);
  if (!email) return { error: 'Link wygasł albo został już użyty. Poproś o nowy.' };
  const problem = await checkNewPassword(pwd, pwd2, email);
  if (problem) return { error: problem };
  const hash = await hashPassword(pwd);
  const { ip, device } = await clientInfo();
  const ok = await withRole('auth', async c => {
    const uid = await useEmailToken(c, token, 'reset');
    if (!uid) return false;
    await c.query(`UPDATE app.profiles SET password_hash = $2, password_changed_at = now(), updated_at = now(),
                   email_verified_at = coalesce(email_verified_at, now()) WHERE id = $1`, [uid, hash]);
    await c.query('UPDATE app.sessions SET revoked_at = now() WHERE user_id = $1 AND revoked_at IS NULL', [uid]);
    await clear(c, 'login:email', email);
    await ev(c, 'password_reset', uid, ip, device);
    return true;
  });
  if (!ok) return { error: 'Link wygasł albo został już użyty. Poproś o nowy.' };
  const m = mails.passwordChanged(); await sendMail(email, m.subject, m.text);
  await clearCookie();
  redirect('/logowanie?haslo=zmienione');
}

// ---------------- konto: hasło, nazwa ----------------
async function checkCurrentPassword(userId: string, pwd: string) {
  const h = await withRole('auth', async c => (await c.query('SELECT password_hash FROM app.profiles WHERE id = $1', [userId])).rows[0]?.password_hash);
  return verifyPassword(h ?? null, pwd);
}

export async function changePassword(_: State, fd: FormData): Promise<State> {
  const s = await requireUser();
  const cur = str(fd, 'current', MAX_LEN + 1), pwd = str(fd, 'password', MAX_LEN + 1), pwd2 = str(fd, 'password2', MAX_LEN + 1);
  if (!(await checkCurrentPassword(s.userId, cur))) return { error: 'Obecne hasło jest nieprawidłowe.' };
  if (cur === pwd) return { error: 'Nowe hasło musi się różnić od obecnego.' };
  const problem = await checkNewPassword(pwd, pwd2, s.email);
  if (problem) return { error: problem };
  const hash = await hashPassword(pwd);
  const { ip, device } = await clientInfo();
  await withRole('auth', async c => {
    await c.query('UPDATE app.profiles SET password_hash = $2, password_changed_at = now(), updated_at = now() WHERE id = $1', [s.userId, hash]);
    await c.query('UPDATE app.sessions SET revoked_at = now() WHERE user_id = $1 AND id <> $2 AND revoked_at IS NULL', [s.userId, s.id]);
    await ev(c, 'password_change', s.userId, ip, device);
  });
  const m = mails.passwordChanged(); await sendMail(s.email, m.subject, m.text);
  return { ok: 'Hasło zmienione. Pozostałe urządzenia zostały wylogowane.' };
}

export async function updateName(_: State, fd: FormData): Promise<State> {
  const s = await requireUser();
  const name = str(fd, 'name', 100).trim();
  if (!name || name.length > 80) return { error: 'Podaj imię i nazwisko (do 80 znaków).' };
  await withUser(s.userId, c => c.query('UPDATE app.profiles SET display_name = $2, updated_at = now() WHERE id = $1', [s.userId, name]));
  return { ok: 'Zapisano.' };
}

// ---------------- weryfikacja dwuetapowa (TOTP) ----------------
const MFA_OFF = 'Weryfikacja dwuetapowa jest wyłączona w tej wersji aplikacji.';
export async function mfaStart(_: State, fd: FormData): Promise<State> {
  const s = await requireUser();
  if (!mfaEnrollEnabled()) return { error: MFA_OFF };
  if (s.mfaOn) return { error: 'Weryfikacja dwuetapowa jest już włączona.' };
  if (!(await checkCurrentPassword(s.userId, str(fd, 'current', MAX_LEN + 1)))) return { error: 'Hasło jest nieprawidłowe.' };
  const secret = newTotpSecret();
  await withRole('auth', c => c.query('UPDATE app.profiles SET mfa_pending_enc = $2 WHERE id = $1', [s.userId, encrypt(secret, 'mfa:' + s.userId)]));
  const b32 = base32(secret);
  const svg = await QRCode.toString(otpauthUri(b32, s.email), { type: 'svg', margin: 1, errorCorrectionLevel: 'M' });
  return { secret: b32.replace(/(.{4})/g, '$1 ').trim(), qr: 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64') };
}

export async function mfaConfirm(_: State, fd: FormData): Promise<State> {
  const s = await requireUser();
  if (!mfaEnrollEnabled()) return { error: MFA_OFF };
  const code = str(fd, 'code', 20);
  const { ip, device } = await clientInfo();
  const codes = await withRole('auth', async c => {
    if (await blocked(c, 'mfa:user', s.userId)) return 'limit' as const;
    const p = (await c.query('SELECT mfa_pending_enc FROM app.profiles WHERE id = $1', [s.userId])).rows[0];
    if (!p?.mfa_pending_enc) return 'none' as const;
    const step = verifyTotp(decrypt(p.mfa_pending_enc, 'mfa:' + s.userId), code, null);
    if (step === null) { await hit(c, 'mfa:user', s.userId); return 'bad' as const; }
    await c.query(`UPDATE app.profiles SET mfa_secret_enc = mfa_pending_enc, mfa_pending_enc = NULL, mfa_last_step = $2, updated_at = now() WHERE id = $1`, [s.userId, step]);
    await c.query('DELETE FROM app.mfa_recovery_codes WHERE user_id = $1', [s.userId]);
    const list: string[] = [];
    for (let i = 0; i < 10; i++) {
      const raw = Array.from({ length: 10 }, () => RC[randomInt(RC.length)]).join('');   // ~50 bitów losowości
      const code = raw.slice(0, 5) + '-' + raw.slice(5);
      list.push(code);
      await c.query('INSERT INTO app.mfa_recovery_codes(user_id, code_hash) VALUES ($1, $2) ON CONFLICT DO NOTHING', [s.userId, recoveryHash(s.userId, code)]);
    }
    await ev(c, 'mfa_on', s.userId, ip, device);
    return list;
  });
  if (codes === 'limit') return { error: TOO_MANY };
  if (codes === 'none') return { error: 'Najpierw rozpocznij konfigurację (podaj hasło).' };
  if (codes === 'bad') return { error: 'Nieprawidłowy kod. Sprawdź, czy godzina w telefonie jest ustawiona automatycznie.' };
  const m = mails.mfaChanged(true); await sendMail(s.email, m.subject, m.text);
  return { ok: 'Weryfikacja dwuetapowa włączona.', codes };
}

export async function mfaDisable(_: State, fd: FormData): Promise<State> {
  const s = await requireUser();
  if (!(await checkCurrentPassword(s.userId, str(fd, 'current', MAX_LEN + 1)))) return { error: 'Hasło jest nieprawidłowe.' };
  const { ip, device } = await clientInfo();
  const res = await withRole('auth', async c => {
    if (await blocked(c, 'mfa:user', s.userId)) return 'limit';
    if (!(await checkSecondFactor(c, s.userId, str(fd, 'code', 40)))) { await hit(c, 'mfa:user', s.userId); return 'bad'; }
    await c.query('UPDATE app.profiles SET mfa_secret_enc = NULL, mfa_pending_enc = NULL, mfa_last_step = NULL, updated_at = now() WHERE id = $1', [s.userId]);
    await c.query('DELETE FROM app.mfa_recovery_codes WHERE user_id = $1', [s.userId]);
    await ev(c, 'mfa_off', s.userId, ip, device);
    return 'ok';
  });
  if (res === 'limit') return { error: TOO_MANY };
  if (res === 'bad') return { error: 'Nieprawidłowy kod.' };
  const m = mails.mfaChanged(false); await sendMail(s.email, m.subject, m.text);
  redirect('/konto/bezpieczenstwo?mfa=wylaczone');
}
