// TOTP (RFC 6238, SHA-1, 6 cyfr, 30 s) – zgodne z Google Authenticator, Microsoft Authenticator, 1Password itp.
import { createHmac, randomBytes } from 'node:crypto';

const B32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
export function base32(buf: Buffer): string {
  let bits = 0, val = 0, out = '';
  for (const b of buf) { val = (val << 8) | b; bits += 8; while (bits >= 5) { out += B32[(val >>> (bits - 5)) & 31]; bits -= 5; } }
  if (bits > 0) out += B32[(val << (5 - bits)) & 31];
  return out;
}
export function base32Decode(s: string): Buffer {
  const clean = s.toUpperCase().replace(/[^A-Z2-7]/g, '');
  let bits = 0, val = 0; const out: number[] = [];
  for (const ch of clean) { val = (val << 5) | B32.indexOf(ch); bits += 5; if (bits >= 8) { out.push((val >>> (bits - 8)) & 255); bits -= 8; } }
  return Buffer.from(out);
}

export const newTotpSecret = () => randomBytes(20);                     // 160 bitów (zalecane w RFC 4226)
export const currentStep = (now = Date.now()) => Math.floor(now / 1000 / 30);

export function totpAt(secret: Buffer, step: number): string {
  const msg = Buffer.alloc(8); msg.writeBigUInt64BE(BigInt(step));
  const h = createHmac('sha1', secret).update(msg).digest();
  const o = h[h.length - 1] & 15;
  const n = ((h[o] & 127) << 24) | (h[o + 1] << 16) | (h[o + 2] << 8) | h[o + 3];
  return String(n % 1_000_000).padStart(6, '0');
}

/** Sprawdza kod w oknie ±1 (±30 s). Zwraca numer okna albo null. Okna ≤ lastStep są odrzucane (kod nie zadziała dwa razy). */
export function verifyTotp(secret: Buffer, code: string, lastStep: number | null, now = Date.now()): number | null {
  const c = code.replace(/\s/g, '');
  if (!/^\d{6}$/.test(c)) return null;
  const s = currentStep(now);
  for (const st of [s - 1, s, s + 1]) {
    if (lastStep !== null && st <= lastStep) continue;
    if (totpAt(secret, st) === c) return st;
  }
  return null;
}

export const otpauthUri = (secretB32: string, account: string) =>
  `otpauth://totp/${encodeURIComponent('Gabinet:' + account)}?secret=${secretB32}&issuer=Gabinet&algorithm=SHA1&digits=6&period=30`;
