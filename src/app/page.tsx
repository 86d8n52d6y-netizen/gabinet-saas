import { health } from '@/lib/health';
export const dynamic = 'force-dynamic';

export default async function Home() {
  const checks = await health();
  const ok = checks.every(c => c.ok);
  return (
    <main className="wrap">
      <h1>Gabinet</h1>
      <p className="muted">Wersja deweloperska – faza 2: architektura lokalna. Logowanie i moduły pojawią się w kolejnych fazach.</p>
      <section className="card" aria-labelledby="st">
        <h2 id="st" style={{ marginTop: 0 }}>Stan środowiska: <span className={ok ? 'ok' : 'err'}>{ok ? 'wszystko działa' : 'wymaga uwagi'}</span></h2>
        <table><tbody>
          {checks.map(c => (
            <tr key={c.name}><td>{c.name}</td><td className={c.ok ? 'ok' : 'err'}>{c.ok ? 'OK' : 'BŁĄD'}</td><td className="muted">{c.info}</td></tr>
          ))}
        </tbody></table>
      </section>
    </main>
  );
}
