// Hasła: Argon2id (parametry powyżej minimum OWASP), zasady siły, sprawdzenie w bazie wycieków (k-anonimowość).
import 'server-only';
import { hash, verify } from '@node-rs/argon2';
import { createHash } from 'node:crypto';
import { breachCheckEnabled } from './env';

// Argon2id: 64 MiB pamięci, 3 przebiegi, 1 wątek (OWASP Password Storage Cheat Sheet: min. 19 MiB / 2 przebiegi)
const OPTS = { algorithm: 2 as const, memoryCost: 65536, timeCost: 3, parallelism: 1 };
export const MIN_LEN = 12, MAX_LEN = 128;

export const hashPassword = (pwd: string) => hash(pwd.normalize('NFKC'), OPTS);

let dummy: Promise<string> | null = null;
/** Weryfikacja; dla nieistniejącego konta liczymy skrót „na próżno”, żeby czas odpowiedzi nie zdradzał, czy konto istnieje. */
export async function verifyPassword(stored: string | null, pwd: string): Promise<boolean> {
  if (!stored) { dummy ??= hashPassword('nieistniejace-konto-' + Math.random()); await verify(await dummy, pwd).catch(() => false); return false; }
  try { return await verify(stored, pwd.normalize('NFKC')); } catch { return false; }
}

// najczęstsze hasła (≥ 12 znaków), także polskie – odrzucane niezależnie od sprawdzenia wycieków
const COMMON = new Set(['123456789012', '1234567890123', 'qwertyuiop12', 'qwerty123456', 'password1234', 'password123!', 'haslo1234567',
  'haslohaslo12', 'zaq12wsxcde3', '1q2w3e4r5t6y', 'qwertyuiopas', 'aaaaaaaaaaaa', 'iloveyou1234', 'administrator', 'admin1234567',
  'polska123456', 'gabinet12345', 'dentysta1234', 'stomatologia', 'zaq1@wsxcde3', '1qaz2wsx3edc', 'abcdefghijkl', 'kochamcie123']);

/** Zwraca opis problemu albo null, gdy hasło jest dopuszczalne. */
export function passwordProblem(pwd: string, email: string): string | null {
  if (pwd.length < MIN_LEN) return `Hasło musi mieć co najmniej ${MIN_LEN} znaków.`;
  if (pwd.length > MAX_LEN) return `Hasło może mieć najwyżej ${MAX_LEN} znaków.`;
  const low = pwd.toLowerCase();
  if (COMMON.has(low) || /^(.)\1+$/.test(pwd)) return 'To hasło jest zbyt popularne. Wybierz inne.';
  const local = email.split('@')[0]?.toLowerCase() ?? '';
  if (local.length >= 4 && low.includes(local)) return 'Hasło nie może zawierać adresu e-mail.';
  return null;
}

/** Ile razy hasło wystąpiło w znanych wyciekach (Have I Been Pwned, model k-anonimowości: wysyłane jest tylko
 *  5 pierwszych znaków skrótu SHA-1, nigdy hasło). Przy braku połączenia zwraca null (nie blokuje rejestracji). */
export async function breachCount(pwd: string): Promise<number | null> {
  if (!breachCheckEnabled()) return null;
  const h = createHash('sha1').update(pwd).digest('hex').toUpperCase();
  try {
    const r = await fetch(`https://api.pwnedpasswords.com/range/${h.slice(0, 5)}`, { headers: { 'Add-Padding': 'true' }, signal: AbortSignal.timeout(2500) });
    if (!r.ok) return null;
    for (const line of (await r.text()).split('\n')) {
      const [suf, n] = line.trim().split(':');
      if (suf === h.slice(5)) return Number(n) || 0;
    }
    return 0;
  } catch { return null; }
}
