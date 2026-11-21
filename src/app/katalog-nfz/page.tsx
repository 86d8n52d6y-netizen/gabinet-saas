import { requireAccess } from '@/lib/access';
import { loadCatalog } from '@/lib/nfz/catalog';
export const metadata = { title: 'Katalog NFZ – Gabinet' };
export const dynamic = 'force-dynamic';

const d = (x: string | null) => x ? new Date(x).toLocaleDateString('pl-PL') : '—';

// „Własne kody” i „Sprawdź wycenę” usunięte z interfejsu (decyzja Patryka 21.11.2026). Zapisane wcześniej własne kody zostają w bazie,
// a silnik wyceny (src/lib/nfz/engine.ts) dalej liczy kwoty wizyt w Opisach NFZ.
export default async function KatalogNfz() {
  const s = await requireAccess();
  const { rows } = await loadCatalog(s.userId);
  const sources = [...new Set(rows.map(r => r.source))];
  return (
    <main className="wrap">
      <h1>Katalog NFZ</h1>
      <section className="card" aria-labelledby="kat">
        <h2 id="kat" style={{ marginTop: 0 }}>Kody z zarządzeń DSOZ ({rows.length})</h2>
        <div style={{ overflowX: 'auto' }}><table>
          <thead><tr><th>Kod</th><th>Świadczenie</th><th>Punkty</th><th>Uwagi</th><th>Obowiązuje od</th></tr></thead>
          <tbody>{rows.map(r => (
            <tr key={r.code}><td><b>{r.kind === 'anest' ? '23.' : ''}{r.code}</b></td><td>{r.name}</td>
              <td>{String(r.points).replace('.', ',')}{r.unit ? ` / ${r.unit}` : ''}</td>
              <td className="muted">{r.kind === 'pkg' ? 'pakiet' : r.kind === 'anest' ? 'znieczulenie' : 'jednostkowe'}{r.no15 ? ' · bez ×1,5' : ''}{r.no08 ? ' · bez ×0,8' : ''}{r.minPerPkg ? ` · min. ${r.minPerPkg} min / pakiet` : ''}</td>
              <td className="muted">{d(r.validFrom)}</td></tr>))}
          </tbody></table></div>
        {sources.map(x => <p key={x} className="src">Źródło: {x}</p>)}
        <p className="src">Dane przeniesione 1:1 z obecnej aplikacji (stan na {d(rows[0]?.verifiedAt)}). „—” = data obowiązywania do uzupełnienia przy weryfikacji z treścią zarządzenia.</p>
      </section>

    </main>
  );
}
