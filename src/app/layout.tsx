import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = { title: 'Gabinet', description: 'Opisy zabiegów, procedury, zestawy, zarobki i kalendarz dyżurów' };
export const viewport: Viewport = { width: 'device-width', initialScale: 1, themeColor: '#0b6a70' };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="pl"><body>{children}</body></html>;
}
