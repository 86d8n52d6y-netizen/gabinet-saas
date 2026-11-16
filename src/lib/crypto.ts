// Kryptografia serwera: losowe tokeny, skróty, HMAC (z rozdzieleniem celów), szyfrowanie AES-256-GCM.
import 'server-only';
import { createCipheriv, createDecipheriv, createHash, createHmac, randomBytes, timingSafeEqual } from 'node:crypto';
import { secrets } from './env';

export const randomToken = (bytes = 32) => randomBytes(bytes).toString('base64url');
export const sha256 = (s: string | Buffer) => createHash('sha256').update(s).digest();
/** HMAC-SHA256 z sekretem serwera; `purpose` oddziela zastosowania (ten sam e-mail daje różne skróty w różnych tabelach). */
export const hmac = (purpose: string, data: string) => createHmac('sha256', secrets().authSecret).update(purpose + '\0' + data).digest();
export const safeEqual = (a: Buffer, b: Buffer) => a.length === b.length && timingSafeEqual(a, b);

/** Szyfrowanie (np. sekretu 2FA): iv(12) | tag(16) | szyfrogram; `aad` wiąże szyfrogram z kontem. */
export function encrypt(plain: Buffer, aad: string): Buffer {
  const iv = randomBytes(12);
  const c = createCipheriv('aes-256-gcm', secrets().encKey, iv);
  c.setAAD(Buffer.from(aad));
  const ct = Buffer.concat([c.update(plain), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), ct]);
}
export function decrypt(box: Buffer, aad: string): Buffer {
  const d = createDecipheriv('aes-256-gcm', secrets().encKey, box.subarray(0, 12));
  d.setAAD(Buffer.from(aad));
  d.setAuthTag(box.subarray(12, 28));
  return Buffer.concat([d.update(box.subarray(28)), d.final()]);
}
