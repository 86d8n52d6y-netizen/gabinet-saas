'use client';
// Górny pasek stron aplikacji – ten sam wygląd i układ co pasek modułów (generator/gabinet-saas.js, G.bar):
// ikona i nazwa „Gabinet”, moduły jako „pigułki” (aktywny w kolorze morskim). Prompt Patryka 21.11.2026, pkt 4.2.
import { usePathname } from 'next/navigation';
import { logout } from '@/lib/auth/actions';

const NAV: [string, string][] = [['/kalendarz', 'Kalendarz'], ['/opisy-nfz', 'Opisy NFZ'], ['/opisy-prywatne', 'Opisy prywatne'], ['/zarobki', 'Zarobki'],
  ['/katalog-nfz', 'Katalog NFZ'], ['/gabinety', 'Gabinety'], ['/ustawienia', 'Ustawienia'], ['/konto', 'Konto']];

export default function GBar() {
  const path = usePathname() ?? '';
  return (
    <header className="gbar" id="gbar" role="banner"><div className="gbar-in">
      <a className="gbar-home" href="/konto" aria-label="Gabinet – konto">
        <svg viewBox="0 0 32 32" width="22" height="22" aria-hidden="true"><path d="M16 4c-3 0-4.4 1.6-7 1.6C5.8 5.6 4 8 4 11.6c0 5.6 2.3 15.4 5.6 15.4 2.3 0 2.2-6.6 6.4-6.6s4.1 6.6 6.4 6.6c3.3 0 5.6-9.8 5.6-15.4C28 8 26.2 5.6 23 5.6 20.4 5.6 19 4 16 4z" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinejoin="round" /></svg>
        <span>Gabinet</span></a>
      <nav className="gbar-nav" aria-label="Moduły">
        {NAV.map(([href, name]) => {
          const on = path === href || path.startsWith(href + '/');
          return <a key={href} href={href} className={on ? 'on' : undefined} aria-current={on ? 'page' : undefined}>{name}</a>;
        })}
      </nav>
      <form action={logout} className="gbar-out"><button type="submit">Wyloguj</button></form>
    </div></header>
  );
}
