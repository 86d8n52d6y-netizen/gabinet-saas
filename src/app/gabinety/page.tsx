import Link from 'next/link';
import ActionForm from '@/components/ActionForm';
import { requireAccess } from '@/lib/access';
import { COLORS, MODELS } from '@/lib/clinics';
import { withUser } from '@/lib/db';
import { fmtC } from '@/lib/nfz/engine';
import { saveClinic, toggleClinic } from '@/lib/praca/actions';
export const metadata = { title: 'Gabinety – Gabinet' };
export const dynamic = 'force-dynamic';

const zl = (gr: number | null) => gr == null ? '' : String(gr / 100).replace('.', ',');
const num = (x: string | null) => x == null ? '' : String(Number(x)).replace('.', ',');

export default async function Gabinety({ searchParams }: { searchParams: Promise<{ id?: string; nowy?: string; ok?: string }> }) {
  const s = await requireAccess();
  const sp = await searchParams;
  const list = await withUser(s.userId, async c => (await c.query(
    `SELECT id, name, short, color, active, model, pct::text, lab_share::text, hourly_gr, daily_gr, min_daily_gr, extra, version
       FROM app.clinics WHERE deleted_at IS NULL ORDER BY active DESC, sort, created_at`)).rows);
  const ed = sp.id ? list.find(x => x.id === sp.id) : null;
  const showForm = !!ed || sp.nowy === '1' || list.length === 0;
  return (
    <main className="wrap">
      <h1>Gabinety</h1>
      {sp.ok && <p className="msg ok" role="status">{sp.ok === 'dodano' ? 'Dodano gabinet.' : 'Zapisano zmiany gabinetu.'}</p>}
      <p className="muted">Gabinety, w których pracujesz. Model rozliczenia wykorzysta Kalendarz (etap 4e); nazwa i kolor – opisy, zarobki i wykresy.</p>
      <section className="card">
        {list.length === 0 ? <p>Nie masz jeszcze gabinetów. Dodaj pierwszy poniżej.</p> : (
          <table>
            <thead><tr><th>Gabinet</th><th>Rozliczenie</th><th></th></tr></thead>
            <tbody>{list.map(c => (
              <tr key={c.id} className={c.active ? '' : 'muted-row'}>
                <td><span className="dot" style={{ ['--cc' as string]: `var(--c${c.color})` }} /> <b>{c.name}</b> {c.short && <span className="muted">({c.short})</span>}
                  {!c.active && <span className="badge">nieaktywny</span>}{c.extra?.address && <div className="hint">{c.extra.address}</div>}</td>
                <td className="muted">{MODELS[c.model as keyof typeof MODELS]}{c.model.startsWith('pct') && ` · ${num(c.pct)}%`}
                  {c.model === 'hourly' && ` · ${fmtC(c.hourly_gr)}/h`}{c.model === 'daily' && ` · ${fmtC(c.daily_gr)}/dzień`}</td>
                <td style={{ textAlign: 'right', whiteSpace: 'nowrap' }}>
                  <Link className="btn ghost" href={`/gabinety?id=${c.id}`}>Edytuj</Link>{' '}
                  <form action={toggleClinic} style={{ display: 'inline' }}><input type="hidden" name="id" value={c.id} />
                    <button className="ghost" type="submit">{c.active ? 'Wyłącz' : 'Włącz'}</button></form>
                </td></tr>))}
            </tbody>
          </table>)}
        {!showForm && <div className="row"><Link className="btn" href="/gabinety?nowy=1">Dodaj gabinet</Link></div>}
      </section>
      {showForm && (
        <section className="card" aria-labelledby="f">
          <h2 id="f" style={{ marginTop: 0 }}>{ed ? `Edycja: ${ed.name}` : 'Nowy gabinet'}</h2>
          <ActionForm action={saveClinic} submit={ed ? 'Zapisz zmiany' : 'Dodaj gabinet'} pending="Zapisuję…">
            {ed && <><input type="hidden" name="id" value={ed.id} /><input type="hidden" name="version" value={ed.version} /></>}
            <div className="grid2">
              <div><label htmlFor="name">Nazwa</label><input id="name" name="name" type="text" required maxLength={80} defaultValue={ed?.name ?? ''} /></div>
              <div><label htmlFor="short">Skrót (do 6 znaków)</label><input id="short" name="short" type="text" maxLength={6} defaultValue={ed?.short ?? ''} /></div>
            </div>
            <label htmlFor="address">Adres (opcjonalnie)</label><input id="address" name="address" type="text" maxLength={200} defaultValue={ed?.extra?.address ?? ''} />
            <fieldset style={{ border: 0, padding: 0, margin: '14px 0 0' }}><legend style={{ fontWeight: 600 }}>Kolor</legend>
              <div className="swatches">{Array.from({ length: COLORS }, (_, i) => i + 1).map(i => (
                <label key={i}><input type="radio" name="color" value={i} defaultChecked={(ed?.color ?? ((list.length % COLORS) + 1)) === i} />
                  <span className="dot" style={{ ['--cc' as string]: `var(--c${i})` }} /><span className="sr-only">kolor {i}</span></label>))}</div></fieldset>
            <label htmlFor="model">Rozliczenie</label>
            <select id="model" name="model" defaultValue={ed?.model ?? 'pct_lab'}>{Object.entries(MODELS).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</select>
            <div className="grid2">
              <div><label htmlFor="pct">Twój % (modele procentowe)</label><input id="pct" name="pct" type="text" inputMode="decimal" defaultValue={ed ? num(ed.pct) : '30'} /></div>
              <div><label htmlFor="lab_share">Twój udział w labie % („lab dzielony”)</label><input id="lab_share" name="lab_share" type="text" inputMode="decimal" defaultValue={ed ? num(ed.lab_share) : '50'} /></div>
              <div><label htmlFor="hourly">Stawka za godzinę (zł)</label><input id="hourly" name="hourly" type="text" inputMode="decimal" defaultValue={zl(ed?.hourly_gr ?? null)} /></div>
              <div><label htmlFor="daily">Stawka za dzień (zł)</label><input id="daily" name="daily" type="text" inputMode="decimal" defaultValue={zl(ed?.daily_gr ?? null)} /></div>
              <div><label htmlFor="min_daily">Minimum za dzień (zł, puste = brak)</label><input id="min_daily" name="min_daily" type="text" inputMode="decimal" defaultValue={zl(ed?.min_daily_gr ?? null)} /></div>
            </div>
          </ActionForm>
          {ed && <p><Link href="/gabinety">Anuluj</Link></p>}
        </section>)}
    </main>
  );
}
