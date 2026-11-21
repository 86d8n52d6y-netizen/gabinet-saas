// Konfiguracja serwera ze zmiennych środowiskowych. Sekrety NIGDY nie trafiają do przeglądarki (moduł server-only).
import 'server-only';

function hexKey(name: string): Buffer {
  const v = process.env[name] ?? '';
  if (!/^[0-9a-f]{64}$/i.test(v)) throw new Error(`${name} musi mieć 64 znaki szesnastkowe (32 bajty) – ustaw w pliku .env`);
  return Buffer.from(v, 'hex');
}

let cache: { authSecret: Buffer; encKey: Buffer } | null = null;
export function secrets() {
  if (!cache) cache = { authSecret: hexKey('AUTH_SECRET'), encKey: hexKey('APP_ENC_KEY') };
  return cache;
}

export const appUrl = () => (process.env.APP_URL ?? 'http://localhost:3000').replace(/\/+$/, '');
export const cookieSecure = () => appUrl().startsWith('https://');
export const breachCheckEnabled = () => process.env.PASSWORD_BREACH_CHECK !== '0';
export const statusDetails = () => process.env.STATUS_DETAILS === '1';
/** Włączanie 2FA – wyłączone (decyzja Patryka 21.11.2026). Konta, które już mają 2FA, dalej logują się z kodem i mogą je wyłączyć.
 *  MFA_ENROLL=1 przywraca możliwość włączania (np. w testach albo po zmianie decyzji). */
export const mfaEnrollEnabled = () => process.env.MFA_ENROLL === '1';
