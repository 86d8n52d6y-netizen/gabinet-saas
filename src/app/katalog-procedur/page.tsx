// Katalog procedur i badań (baza stomatologiczna) – tylko odczyt. Dane: data/ (src/lib/baza.ts). Treść: wersja robocza do weryfikacji Patryka.
import { requireAccess } from '@/lib/access';
import { baza, STATUS } from '@/lib/baza';
export const metadata = { title: 'Katalog procedur – Gabinet' };
export const dynamic = 'force-dynamic';

export default async function KatalogProcedur({ searchParams }: { searchParams: Promise<{ q?: string; status?: string }> }) {
  await requireAccess();
  const { q = '', status = '' } = await searchParams;
  const b = await baza();
  const fraza = q.trim().toLowerCase();
  const pasuje = (t: string) => !fraza || t.toLowerCase().includes(fraza);
  const opracowane = b.procedury.filter(p => p.status !== 'not_started');
  const proc = opracowane.filter(p => (!status || p.status === status) && pasuje(`${p.kod} ${p.nazwa_oficjalna} ${p.nazwa_krotka ?? ''} ${(p.kody_aplikacji ?? []).join(' ')}`));
  const grupy = [...new Set(proc.map(p => p.kategoria))];
  const bad = b.badania.filter(x => pasuje(`${x.nazwa} ${x.nazwa_krotka}`));
  const pominiete = b.procedury.filter(p => p.status === 'not_started').length;
  return (
    <main className="wrap">
      <h1>Katalog procedur i badań</h1>
      <p className="muted">Baza wiedzy (wersja danych {b.wersja}): {b.badania.length} badań, {opracowane.length} kart procedur ICD-9. Zweryfikowane przez Patryka: <b>{b.procedury.filter(p => p.status === 'verified').length}</b>; pozostałe to <b>wersja robocza do weryfikacji</b> – nie zastępują oceny klinicznej; wymagania NFZ z audytu NFZ.
        {' '}Kody pominięte, odrzucone lub nadrzędne ({pominiete}) – w rejestrze kompletności.</p>
      <form className="card" method="get" style={{ display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'end' }} data-testid="kp-filtr">
        <label>Szukaj (kod, nazwa, kod z Opisów NFZ)<br /><input name="q" defaultValue={q} placeholder="np. 23.1502, ekstrakcja, ST30" /></label>
        <label>Status<br /><select name="status" defaultValue={status}>
          <option value="">wszystkie</option><option value="draft">{STATUS.draft}</option><option value="requires_expert_review">{STATUS.requires_expert_review}</option><option value="verified">{STATUS.verified}</option>
        </select></label>
        <button type="submit" className="btn">Pokaż</button>
      </form>
      {bad.length > 0 && <section className="card" aria-labelledby="kp-bad"><h2 id="kp-bad" style={{ marginTop: 0 }}>Badania ({bad.length})</h2>
        <ul data-testid="kp-badania">{bad.map(x => <li key={x.id}><a href={`/katalog-procedur/${x.id}`}>{x.nazwa}</a> <span className={x.status === 'verified' ? 'badge' : 'badge warn'}>{STATUS[x.status] ?? x.status}</span></li>)}</ul></section>}
      <section className="card" aria-labelledby="kp-proc"><h2 id="kp-proc" style={{ marginTop: 0 }}>Procedury ICD-9 ({proc.length})</h2>
        {grupy.length === 0 && <p className="muted">Brak wyników.</p>}
        {grupy.map(g => <div key={g}><h3>{g}</h3><ul data-testid="kp-procedury">{proc.filter(p => p.kategoria === g).map(p =>
          <li key={p.id}><a href={`/katalog-procedur/${p.id}`}><b>{p.kod}</b> {p.nazwa_krotka ?? p.nazwa_oficjalna}</a>
            {p.kody_aplikacji?.length ? <span className="muted"> · Opisy NFZ: {p.kody_aplikacji.join(', ')}</span> : null} <span className={p.status === 'verified' ? 'badge' : 'badge warn'}>{STATUS[p.status] ?? p.status}</span></li>)}</ul></div>)}
      </section>
      <p className="src">Dane: data/badania, data/procedury-icd9 · instrukcja: docs/IMPLEMENTACJA_BAZY_STOMATOLOGICZNEJ.md · rejestr: docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md</p>
    </main>
  );
}
