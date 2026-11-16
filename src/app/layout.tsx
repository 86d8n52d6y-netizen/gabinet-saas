import type { Metadata, Viewport } from 'next';
import Link from 'next/link';
import './globals.css';
import { getSession } from '@/lib/session';
import { logout } from '@/lib/auth/actions';

export const metadata: Metadata = { title: 'Gabinet', description: 'Opisy zabiegów, procedury, zestawy, zarobki i kalendarz dyżurów' };
export const viewport: Viewport = { width: 'device-width', initialScale: 1, themeColor: '#0b6a70' };

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const s = await getSession().catch(() => null);
  const inside = s?.mfaPassed;
  return (
    <html lang="pl"><body>
      <header className="top">
        <Link href={inside ? '/konto' : '/'} className="brand">Gabi<span>net</span></Link>
        <nav className="nav" aria-label="Menu">
          {inside ? (<>
            <Link href="/katalog-nfz">Katalog NFZ</Link>
            <Link href="/gabinety">Gabinety</Link>
            <Link href="/ustawienia">Ustawienia</Link>
            <Link href="/konto">Konto</Link>
            <form action={logout}><button className="ghost" type="submit">Wyloguj</button></form>
          </>) : (<>
            <Link href="/logowanie">Zaloguj</Link>
            <Link href="/rejestracja" className="btn">Załóż konto</Link>
          </>)}
        </nav>
      </header>
      {children}
    </body></html>
  );
}
