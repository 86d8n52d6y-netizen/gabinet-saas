// Testy jednostkowe modułów kont: TOTP (wektory RFC 6238), szyfrowanie, hasła, skracanie IP, sprawdzanie wycieków, SMTP.
import { afterEach, beforeAll, describe, expect, it, vi } from 'vitest';
import { SMTPServer } from 'smtp-server';

beforeAll(() => {
  process.env.AUTH_SECRET = 'a'.repeat(64);
  process.env.APP_ENC_KEY = 'b'.repeat(64);
});

describe('TOTP (RFC 6238, SHA-1)', async () => {
  const { totpAt, verifyTotp, base32, base32Decode, otpauthUri } = await import('@/lib/totp');
  const secret = Buffer.from('12345678901234567890');
  it.each([[59, '287082'], [1111111109, '081804'], [1234567890, '005924'], [2000000000, '279037']])(
    'wektor RFC 6238 dla T=%i → %s', (t, code) => expect(totpAt(secret, Math.floor(t / 30))).toBe(code));
  it('base32 w obie strony', () => expect(base32Decode(base32(secret)).equals(secret)).toBe(true));
  it('akceptuje kod z sąsiedniego okna (±30 s), odrzuca starszy', () => {
    const now = 1234567890_000, step = Math.floor(now / 30000);
    expect(verifyTotp(secret, totpAt(secret, step - 1), null, now)).toBe(step - 1);
    expect(verifyTotp(secret, totpAt(secret, step - 2), null, now)).toBeNull();
  });
  it('ten sam kod nie działa drugi raz (ostatnie okno zapamiętane)', () => {
    const now = 1234567890_000, step = Math.floor(now / 30000), c = totpAt(secret, step);
    expect(verifyTotp(secret, c, null, now)).toBe(step);
    expect(verifyTotp(secret, c, step, now)).toBeNull();
  });
  it('odrzuca kody w złym formacie', () => {
    for (const c of ['', '12345', '1234567', 'abcdef']) expect(verifyTotp(secret, c, null)).toBeNull();
  });
  it('adres otpauth zawiera wydawcę Gabinet', () => expect(otpauthUri('ABC', 'a@b.pl')).toMatch(/^otpauth:\/\/totp\/Gabinet%3Aa%40b\.pl\?secret=ABC&issuer=Gabinet/));
});

describe('szyfrowanie AES-256-GCM i HMAC', async () => {
  const { encrypt, decrypt, hmac } = await import('@/lib/crypto');
  it('szyfruje i odszyfrowuje', () => expect(decrypt(encrypt(Buffer.from('tajne'), 'mfa:1'), 'mfa:1').toString()).toBe('tajne'));
  it('każde szyfrowanie daje inny wynik (losowy IV)', () => expect(encrypt(Buffer.from('x'), 'a').equals(encrypt(Buffer.from('x'), 'a'))).toBe(false));
  it('szyfrogram innego konta (inne AAD) nie da się odszyfrować', () => expect(() => decrypt(encrypt(Buffer.from('x'), 'mfa:1'), 'mfa:2')).toThrow());
  it('zmieniony szyfrogram jest wykrywany', () => {
    const box = encrypt(Buffer.from('tajne'), 'a'); box[box.length - 1] ^= 1;
    expect(() => decrypt(box, 'a')).toThrow();
  });
  it('HMAC rozdziela zastosowania', () => expect(hmac('trial', 'a@b.pl').equals(hmac('rate', 'a@b.pl'))).toBe(false));
});

describe('hasła', async () => {
  const { passwordProblem, hashPassword, verifyPassword, breachCount } = await import('@/lib/password');
  afterEach(() => vi.unstubAllGlobals());
  it('zasady: długość, popularne, e-mail', () => {
    expect(passwordProblem('krotkie', 'a@b.pl')).toMatch(/12 znaków/);
    expect(passwordProblem('x'.repeat(129), 'a@b.pl')).toMatch(/najwyżej/);
    expect(passwordProblem('qwerty123456', 'a@b.pl')).toMatch(/popularne/);
    expect(passwordProblem('bbbbbbbbbbbbbb', 'a@b.pl')).toMatch(/popularne/);
    expect(passwordProblem('jan.kowalski-2026', 'jan.kowalski@x.pl')).toMatch(/e-mail/);
    expect(passwordProblem('zielony-kubek-na-biurku', 'jan@x.pl')).toBeNull();
  });
  it('Argon2id: poprawne hasło tak, złe nie; brak konta → false', async () => {
    const h = await hashPassword('zielony-kubek-na-biurku');
    expect(h).toMatch(/^\$argon2id\$v=19\$m=65536,t=3,p=1\$/);
    expect(await verifyPassword(h, 'zielony-kubek-na-biurku')).toBe(true);
    expect(await verifyPassword(h, 'zielony-kubek-na-biurkU')).toBe(false);
    expect(await verifyPassword(null, 'cokolwiek')).toBe(false);
    expect(await verifyPassword('uszkodzony', 'x')).toBe(false);
  });
  it('wycieki: wysyłane tylko 5 znaków skrótu SHA-1; wynik z odpowiedzi', async () => {
    // SHA-1('password') = 5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8
    const f = vi.fn(async (url: string) => new Response('1E4C9B93F3F0682250B6CF8331B7EE68FD8:9659365\r\nAAAA:1'));
    vi.stubGlobal('fetch', f);
    expect(await breachCount('password')).toBe(9659365);
    expect(f.mock.calls[0][0]).toBe('https://api.pwnedpasswords.com/range/5BAA6');
  });
  it('wycieki: brak połączenia nie blokuje (null)', async () => {
    vi.stubGlobal('fetch', vi.fn(async () => { throw new Error('offline'); }));
    expect(await breachCount('cokolwiek-dlugiego')).toBeNull();
  });
});

describe('dane żądania (minimalizacja)', async () => {
  const { ipPrefix, deviceLabel } = await import('@/lib/request');
  it('IPv4 → /24, IPv6 → /48, IPv4 w IPv6, śmieci → null', () => {
    expect(ipPrefix('83.21.140.77')).toBe('83.21.140.0/24');
    expect(ipPrefix('2a01:110f:4407:1a00:1:2:3:4')).toBe('2a01:110f:4407::/48');
    expect(ipPrefix('2a01:db8::1')).toBe('2a01:db8:0::/48');
    expect(ipPrefix('::ffff:10.1.2.3')).toBe('10.1.2.0/24');
    expect(ipPrefix('nie-ip')).toBeNull();
    expect(ipPrefix(null)).toBeNull();
  });
  it('opis urządzenia', () => {
    expect(deviceLabel('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15')).toBe('Safari, Mac');
    expect(deviceLabel('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0')).toBe('Edge, Windows');
    expect(deviceLabel('Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Mobile Safari/537.36')).toBe('Chrome, Android');
    expect(deviceLabel(null)).toBe('Nieznane urządzenie');
  });
});

describe('wysyłka e-mail przez SMTP (jak Mailpit)', () => {
  it('wiadomość dociera do serwera SMTP z poprawnym nadawcą i treścią', async () => {
    const got: string[] = [];
    const srv = new SMTPServer({ authOptional: true, disabledCommands: ['STARTTLS'], onData(stream, _s, cb) {
      let d = ''; stream.on('data', x => (d += x)); stream.on('end', () => { got.push(d); cb(); });
    } });
    await new Promise<void>(r => srv.listen(0, '127.0.0.1', () => r()));
    const port = (srv.server.address() as { port: number }).port;
    process.env.SMTP_HOST = '127.0.0.1'; process.env.SMTP_PORT = String(port); delete process.env.MAIL_DIR;
    const { sendMail } = await import('@/lib/mail');
    await sendMail('lekarz@example.com', 'Gabinet – test', 'Treść testowa ąęłńóśźż');
    await new Promise<void>(r => srv.close(() => r()));
    expect(got).toHaveLength(1);
    expect(got[0]).toMatch(/From: Gabinet <no-reply@gabinet\.local>/);
    expect(got[0]).toMatch(/To: lekarz@example\.com/);
  });
});
