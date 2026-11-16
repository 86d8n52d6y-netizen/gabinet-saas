import ActionForm from '@/components/ActionForm';
import { requireAccess } from '@/lib/access';
import { withUser } from '@/lib/db';
import { centsHours, centsPts, fmtC } from '@/lib/nfz/engine';
import { saveNfzSettings } from '@/lib/praca/actions';
import { cleanNfz, PCT_OPTS } from '@/lib/settings';
export const metadata = { title: 'Ustawienia – Gabinet' };
export const dynamic = 'force-dynamic';

const num = (x: number) => String(x).replace('.', ',');

export default async function Ustawienia() {
  const s = await requireAccess();
  const row = await withUser(s.userId, async c => (await c.query('SELECT settings, version FROM app.user_settings')).rows[0]);
  const n = cleanNfz(row?.settings?.nfz);
  return (
    <main className="wrap">
      <h1>Ustawienia</h1>
      <section className="card" aria-labelledby="nfz">
        <h2 id="nfz" style={{ marginTop: 0 }}>Rozliczenie NFZ</h2>
        <ActionForm action={saveNfzSettings} submit="Zapisz ustawienia" pending="Zapisuję…">
          <input type="hidden" name="version" value={row?.version ?? 0} />
          <div className="grid2">
            <div><label htmlFor="price">Stawka za punkt (zł)</label>
              <input id="price" name="price" type="text" inputMode="decimal" defaultValue={num(n.price)} required />
              <p className="hint">np. 100 pkt = {fmtC(centsPts(100, n.price))}</p></div>
            <div><label htmlFor="rev">Przeglądy – stawka za godzinę (zł)</label>
              <input id="rev" name="rev" type="text" inputMode="decimal" defaultValue={num(n.rev)} required />
              <p className="hint">np. 1,5 h = {fmtC(centsHours(1.5, n.rev))}</p></div>
            <div><label htmlFor="pct">Udział lekarza</label>
              <select id="pct" name="pct" defaultValue={n.pct}>{PCT_OPTS.map(p => <option key={p} value={p}>{p}%</option>)}</select>
              <p className="hint">procent wartości punktów dla lekarza</p></div>
            <div><label htmlFor="basis">Zarobek z punktów</label>
              <select id="basis" name="basis" defaultValue={n.basis}>
                <option value="full">pełna wartość punktów</option><option value="share">udział lekarza (%)</option></select>
              <p className="hint">jak liczyć zarobek w statystykach</p></div>
          </div>
          <p className="hint">Domyślnie: 1,84 zł/pkt, 40%, 350 zł/h. Pakiet higienizacyjny z ekstrakcją lub leczeniem zachowawczym: +10 min do czasu wizyty (zasada bez zmian).</p>
        </ActionForm>
      </section>
    </main>
  );
}
