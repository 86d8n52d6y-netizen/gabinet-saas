import type { Metadata, Viewport } from 'next';
import Link from 'next/link';
import './globals.css';
import { getSession } from '@/lib/session';
import GBar from '@/components/GBar';

export const metadata: Metadata = { title: 'Gabinet', description: 'Opisy zabiegów, procedury, zestawy, zarobki i kalendarz dyżurów' };
export const viewport: Viewport = { width: 'device-width', initialScale: 1, themeColor: '#0b6a70' };

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const s = await getSession().catch(() => null);
  const inside = s?.mfaPassed;
  return (
    <html lang="pl">{inside && <head><link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css" /></head>}<body>
      {inside ? <GBar /> : (
        <header className="top">
          <Link href="/" className="brand">Gabi<span>net</span></Link>
          <nav className="nav" aria-label="Menu">
            <Link href="/logowanie">Zaloguj</Link>
            <Link href="/rejestracja" className="btn">Załóż konto</Link>
          </nav>
        </header>)}
      {children}
    </body></html>
  );
}
