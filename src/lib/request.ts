// Informacje o żądaniu: skrócony adres IP (minimalizacja danych) i opis urządzenia z nagłówka User-Agent.
import 'server-only';
import { headers } from 'next/headers';
import { isIP } from 'node:net';

/** Adres skrócony do /24 (IPv4) lub /48 (IPv6) – wystarcza do limitów i rozpoznania sieci, nie wskazuje urządzenia. */
export function ipPrefix(ip: string | null): string | null {
  if (!ip) return null;
  let a = ip.trim();
  if (a.startsWith('::ffff:') && isIP(a.slice(7)) === 4) a = a.slice(7);
  if (isIP(a) === 4) return a.split('.').slice(0, 3).join('.') + '.0/24';
  if (isIP(a) === 6) {
    const full = expand6(a);
    return full.slice(0, 3).join(':') + '::/48';
  }
  return null;
}
function expand6(a: string): string[] {
  const [h, t] = a.split('::');
  const head = h ? h.split(':') : [], tail = t !== undefined && t ? t.split(':') : [];
  const mid = a.includes('::') ? Array(8 - head.length - tail.length).fill('0') : [];
  return [...head, ...mid, ...tail].map(x => x || '0');
}

export function deviceLabel(ua: string | null): string {
  if (!ua) return 'Nieznane urządzenie';
  const b = /Edg\//.test(ua) ? 'Edge' : /Firefox\//.test(ua) ? 'Firefox' : /Chrome\//.test(ua) ? 'Chrome' : /Safari\//.test(ua) ? 'Safari' : 'Przeglądarka';
  const o = /iPhone/.test(ua) ? 'iPhone' : /iPad/.test(ua) ? 'iPad' : /Android/.test(ua) ? 'Android'
    : /Mac OS X|Macintosh/.test(ua) ? 'Mac' : /Windows/.test(ua) ? 'Windows' : /Linux/.test(ua) ? 'Linux' : 'inny system';
  return `${b}, ${o}`;
}

export async function clientInfo() {
  const h = await headers();
  // Za odwrotnym proxy (Caddy) pierwszy adres z X-Forwarded-For; aplikacja nie jest dostępna z pominięciem proxy.
  const ip = h.get('x-forwarded-for')?.split(',')[0] ?? h.get('x-real-ip');
  return { ip: ipPrefix(ip), device: deviceLabel(h.get('user-agent')) };
}
