import ActionForm from '@/components/ActionForm';
import Wycena from '@/components/Wycena';
import { requireAccess } from '@/lib/access';
import { withUser } from '@/lib/db';
import { loadCatalog } from '@/lib/nfz/catalog';
import { deleteCustomNfz, saveCustomNfz } from '@/lib/praca/actions';
import { cleanNfz } from '@/lib/settings';
export const metadata = { title: 'Katalog NFZ – Gabinet' };
export const dynamic = 'force-dynamic';

const d = (x: string | null) => x ? new Date(x).toLocaleDateString('pl-PL') : '—';

export default async function KatalogNfz({ searchParams }: { searchParams: Promise<{ id?: string }> }) {
  const s = await requireAccess();
  const sp = await searchParams;
  const { catalog, rows } = await loadCatalog(s.userId);
  const { custom, settings } = await withUser(s.userId, async c => ({
    custom: (await c.query(`SELECT id, nfz_code AS code, name, nfz_points::float8 AS points, version FROM app.procedures
                            WHERE kind='nfz_custom' AND deleted_at IS NULL ORDER BY nfz_code`)).rows,
    settings: cleanNfz((await c.query('SELECT settings FROM app.user_settings')).rows[0]?.settings?.nfz),
  }));
  const ed = sp.id ? custom.find(x => x.id === sp.id) : null;
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

      <section className="card" aria-labelledby="wl">
        <h2 id="wl" style={{ marginTop: 0 }}>Własne kody <span className="badge warn">niesprawdzane przez zasady NFZ</span></h2>
        <p className="muted">Kody spoza katalogu (np. nowe świadczenie, zanim pojawi się w aplikacji). Punkty wpisujesz sam; aplikacja liczy punkty × ilość – bez współczynników ×1,5 / ×1,2 / ×0,8 i bez sprawdzania zasad łączenia i limitów NFZ.</p>
        {custom.length > 0 && <table><tbody>{custom.map(c => (
          <tr key={c.id}><td><b>{c.code}</b></td><td>{c.name}</td><td>{String(c.points).replace('.', ',')} pkt</td>
            <td style={{ textAlign: 'right', whiteSpace: 'nowrap' }}><a className="btn ghost" href={`/katalog-nfz?id=${c.id}`}>Edytuj</a>{' '}
              <form action={deleteCustomNfz} style={{ display: 'inline' }}><input type="hidden" name="id" value={c.id} /><button className="danger" type="submit">Usuń</button></form></td></tr>))}
        </tbody></table>}
        <ActionForm action={saveCustomNfz} submit={ed ? 'Zapisz zmiany' : 'Dodaj własny kod'} pending="Zapisuję…" ghost={!ed}>
          {ed && <><input type="hidden" name="id" value={ed.id} /><input type="hidden" name="version" value={ed.version} /></>}
          <div className="grid2">
            <div><label htmlFor="code">Kod</label><input id="code" name="code" type="text" maxLength={12} required defaultValue={ed?.code ?? ''} /></div>
            <div><label htmlFor="cname">Nazwa</label><input id="cname" name="name" type="text" maxLength={120} required defaultValue={ed?.name ?? ''} /></div>
            <div><label htmlFor="points">Punkty</label><input id="points" name="points" type="text" inputMode="decimal" required defaultValue={ed ? String(ed.points).replace('.', ',') : ''} /></div>
          </div>
        </ActionForm>
      </section>

      <section className="card" aria-labelledby="wyc">
        <h2 id="wyc" style={{ marginTop: 0 }}>Sprawdź wycenę</h2>
        <p className="muted">Ten sam silnik, którego użyje generator opisów. Możesz porównać wynik ze starą aplikacją.</p>
        <Wycena catalog={catalog} settings={settings} custom={custom.map(c => ({ code: c.code, name: c.name, points: c.points }))} />
      </section>
    </main>
  );
}
