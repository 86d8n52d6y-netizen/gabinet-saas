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
