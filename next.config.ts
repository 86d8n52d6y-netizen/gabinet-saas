import type { NextConfig } from 'next';

// Nagłówki bezpieczeństwa dla wszystkich stron. CSP: tylko własne zasoby; 'unsafe-inline' dla skryptów wymaga Next.js
// bez nonce (zaostrzenie nonce'ami – faza 7). W trybie deweloperskim Next potrzebuje też 'unsafe-eval'.
const dev = process.env.NODE_ENV !== 'production';
const csp = [
  "default-src 'self'", `script-src 'self' 'unsafe-inline'${dev ? " 'unsafe-eval'" : ''}`, "style-src 'self' 'unsafe-inline'",
  "img-src 'self' data:", "font-src 'self'", "connect-src 'self'", "frame-ancestors 'none'", "form-action 'self'",
  "base-uri 'self'", "object-src 'none'",
].join('; ');
const security = [
  { key: 'Content-Security-Policy', value: csp },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), payment=()' },
  { key: 'Cross-Origin-Opener-Policy', value: 'same-origin' },
];

const config: NextConfig = {
  output: 'standalone',
  // generator Opisów NFZ czytany z dysku w trasach /opisy-nfz – dołączany do wersji produkcyjnej
  outputFileTracingIncludes: { '/opisy-nfz': ['./generator/**/*'], '/opisy-prywatne': ['./generator/**/*'], '/opisy-nfz/zasoby/[plik]': ['./generator/**/*'] },
  poweredByHeader: false,
  reactStrictMode: true,
  async headers() { return [{ source: '/:path*', headers: security }]; },
};
export default config;
