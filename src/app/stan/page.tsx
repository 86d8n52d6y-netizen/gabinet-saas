import { notFound } from 'next/navigation';
import { health } from '@/lib/health';
import { statusDetails } from '@/lib/env';
export const dynamic = 'force-dynamic';

// Szczegóły środowiska tylko lokalnie (STATUS_DETAILS=1); w produkcji strona nie istnieje.
export default async function Stan() {
  if (!statusDetails()) notFound();
  const checks = await health();
  const ok = checks.every(c => c.ok);
  return (
    <main className="wrap">
      <section className="card" aria-labelledby="st">
        <h2 id="st" style={{ marginTop: 0 }}>Stan środowiska: <span className={ok ? 'ok' : 'err'}>{ok ? 'wszystko działa' : 'wymaga uwagi'}</span></h2>
        <table><tbody>
          {checks.map(c => (<tr key={c.name}><td>{c.name}</td><td className={c.ok ? 'ok' : 'err'}>{c.ok ? 'OK' : 'BŁĄD'}</td><td className="muted">{c.info}</td></tr>))}
        </tbody></table>
      </section>
    </main>
  );
}
