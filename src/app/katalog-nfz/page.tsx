import { requireAccess } from '@/lib/access';
import { loadCatalog } from '@/lib/nfz/catalog';
import { regulyNfz } from '@/lib/nfz/audyt';
export const metadata = { title: 'Katalog NFZ – Gabinet' };
export const dynamic = 'force-dynamic';

const d = (x: string | null) => x ? new Date(x).toLocaleDateString('pl-PL') : '—';

// „Własne kody” i „Sprawdź wycenę” usunięte z interfejsu (decyzja Patryka 21.11.2026). Zapisane wcześniej własne kody zostają w bazie,
// a silnik wyceny (src/lib/nfz/engine.ts) dalej liczy kwoty wizyt w Opisach NFZ.
export default async function KatalogNfz() {
  const s = await requireAccess();
  const { rows } = await loadCatalog(s.userId);
  const sources = [...new Set(rows.map(r => r.source))];
  const audyt = await regulyNfz();
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

      <section className="card" aria-labelledby="zas" data-testid="zasady-nfz">
        <h2 id="zas" style={{ marginTop: 0 }}>Zasady rozliczeń NFZ ({audyt.reguly.length})</h2>
        <p className="muted" style={{ marginTop: 0 }}>Z audytu NFZ (wersja {audyt.wersja}, stan prawny na {d(audyt.stan)}). Opisy NFZ sprawdzają je na Twoim urządzeniu według daty wizyty.
          Reguły „wymaga weryfikacji” są tylko informacją. Limity zależne od historii pacjenta – zawsze informacja (aplikacja nie zna wizyt z innych gabinetów).</p>
        <div style={{ overflowX: 'auto' }}><table>
          <thead><tr><th>Reguła</th><th>Treść</th><th>W aplikacji</th><th>Status</th><th>Od</th><th>Źródło</th></tr></thead>
          <tbody>{audyt.reguly.map(r => (
            <tr key={r.id}><td><b>{r.id}</b><br /><span className="muted">{r.obszar}</span></td><td>{r.tresc}</td><td>{r.poziom.toLowerCase()}{r.decyzja ? <span className="muted"><br />audyt: {r.poziomAudyt.toLowerCase()} – {r.decyzja}</span> : null}</td>
              <td className="muted">{r.status.toLowerCase()}</td><td className="muted">{/^\d{4}-/.test(r.od) ? d(r.od) : r.od.toLowerCase()}</td>
              <td className="muted">{r.zrodla.join('; ')}</td></tr>))}
          </tbody></table></div>
        <p className="src">„W aplikacji” – poziom po decyzjach z 22.11.2026 (D1=B, D4=A, D7=B, znieczulenie przy ekstrakcji i kiretażu – ostrzeżenie; data/decyzje-nfz.json). Źródła i pełny raport: docs/nfz/ (AUDYT_RAPORT.md, REGULY_ROZLICZEN.md, REJESTR_ZRODEL.md). Do sprawdzenia przy nowym zarządzeniu NFZ.</p>
      </section>
    </main>
  );
}
