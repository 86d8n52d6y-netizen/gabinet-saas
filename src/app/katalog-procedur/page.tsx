// Katalog procedur i badań – jeden widok, dwie rozdzielone tabele (prompt Patryka 23.11.2026, pkt 3):
// Tabela 1 – procedury NFZ (zasada rozliczenia punktowego), Tabela 2 – procedury prywatne (cena i wynagrodzenie lekarza z Cennika).
// Dane: data/ (src/lib/baza.ts), rozliczenie NFZ i katalog prywatny: src/lib/katalog.ts. Tylko odczyt.
import { requireAccess } from '@/lib/access';
import { baza, STATUS } from '@/lib/baza';
import { cenaPryw, katalog, type NfzRozl } from '@/lib/katalog';
import { withUser } from '@/lib/db';
import { getBlobs } from '@/lib/pryw/wizyty';
export const metadata = { title: 'Katalog procedur – Gabinet' };
export const dynamic = 'force-dynamic';

const zl = (gr: number | null) => gr == null ? '—' : (gr / 100).toLocaleString('pl-PL', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' zł';
function rozlOpis(r: NfzRozl): [string, string] {
  switch (r.typ) {
    case 'pakiet': return [r.pakiety.map(p => `${p.id} – ${p.pkt} pkt`).join(' / '), 'procedura kierunkowa pakietu (zał. 1c/1d)'];
    case 'skladowa': return [`w pakiecie (0 pkt) – lista ${r.listy.join(', ')}`, (r.wlasny ? `bez pakietu na wizycie: ${r.wlasny.id} – ${r.wlasny.pkt} pkt` : r.jedn ? `bez pakietu: ${r.jedn.pkt} pkt (zał. 1b)${r.jedn.liczone ? '' : ' – do akceptacji'}` : 'tylko jako składowa pakietu')];
    case 'jednostkowe': return [`${r.pkt} pkt (zał. 1b)`, r.liczone ? 'świadczenie jednostkowe – liczone w zakładce NFZ' : 'zał. 1b – do akceptacji, w zakładce NFZ niewliczane do sumy'];
    default: return ['brak wyceny w danych', 'nie liczone'];
  }
}

export default async function KatalogProcedur({ searchParams }: { searchParams: Promise<{ q?: string; g?: string }> }) {
  const s = await requireAccess();
  const { q = '', g = '' } = await searchParams;
  const [b, k] = await Promise.all([baza(), katalog()]);
  const { clinics, cennik } = await withUser(s.userId, async c => ({
    clinics: (await c.query(`SELECT id, name, model, pct FROM app.clinics WHERE deleted_at IS NULL ORDER BY active DESC, sort, created_at`)).rows as { id: string; name: string; model: string; pct: string | null }[],
    cennik: (await getBlobs(c, ['pryw:cennik']))['pryw:cennik'] ?? null }));
  const gab = clinics.find(x => x.id === g) ?? null;
  const kPct = gab && gab.pct != null && /^pct/.test(gab.model) ? Number(gab.pct) : null;
  const fraza = q.trim().toLowerCase();
  const pasuje = (t: string) => !fraza || t.toLowerCase().includes(fraza);
  const nfz = k.nfz.filter(p => pasuje(`${p.kod} ${p.nazwa} ${p.kategoria}`));
  const pryw = k.pryw.filter(p => pasuje(`${p.kod ?? ''} ${p.nazwa}`));
  const specj = [...new Set(nfz.map(p => p.kategoria))].sort((a, b2) => a.localeCompare(b2, 'pl'));
  const bad = b.badania.filter(x => x.status !== 'not_started' && pasuje(`${x.nazwa} ${x.nazwa_krotka}`));
  const pominiete = b.procedury.filter(p => p.status === 'not_started').length;
  return (
    <main className="wrap">
      <h1>Katalog procedur i badań</h1>
      <p className="muted">Dwie osobne tabele: <b>procedury NFZ</b> (rozliczenie punktowe – zakładka „NFZ”) i <b>procedury prywatne</b> (ceny i wynagrodzenie lekarza – Opisy prywatne).
        Karty zweryfikowane przez Patryka: <b>{b.procedury.filter(p => p.status === 'verified').length}</b>. Kody pominięte lub odrzucone Twoimi decyzjami ({pominiete}) – w rejestrze kompletności, nie trafiają do opisów.</p>
      <form className="card" method="get" style={{ display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'end' }} data-testid="kp-filtr">
        <label>Szukaj (kod, nazwa)<br /><input name="q" defaultValue={q} placeholder="np. 23.1502, ekstrakcja" /></label>
        <label>Gabinet (ceny w tabeli prywatnej)<br /><select name="g" defaultValue={g}><option value="">— bez gabinetu —</option>{clinics.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}</select></label>
        <button type="submit" className="btn">Pokaż</button>
      </form>

      <section className="card" aria-labelledby="kp-nfz" data-testid="kp-tab-nfz">
        <h2 id="kp-nfz" style={{ marginTop: 0 }}>Tabela 1 – Procedury NFZ ({nfz.length})</h2>
        <p className="hint">Do opisów w zakładce <a href="/nfz">NFZ</a>. Punkty: zał. 1b (44/2025/DSOZ), zał. 1c i skład pakietów zał. 1d (95/2026/DSOZ). Procedura z listy dodatkowej pakietu obecnego na wizycie jest jego składową (0 pkt). Współczynniki: ×1,5 do 18 r.ż. (bez ST30D–G), ×1,2 ciąża, kolejny pakiet ×0,8. Te karty są też dostępne w Opisach prywatnych dla pacjenta prywatnego – tutaj tylko w tabeli NFZ.</p>
        {specj.map(sp => <div key={sp}><h3>{sp}</h3><div style={{ overflowX: 'auto' }}><table className="num" data-testid="kp-nfz-tab"><thead><tr><th>Kod</th><th>Procedura</th><th>Rozliczenie NFZ</th><th>Uwagi</th></tr></thead><tbody>
          {nfz.filter(p => p.kategoria === sp).map(p => { const [r1, r2] = rozlOpis(p.rozl); return <tr key={p.kod} data-kod={p.kod}><td><a href={`/katalog-procedur/PROC-${p.kod}`}>{p.kod}</a></td><td style={{ textAlign: 'left' }}>{p.nazwa}{p.gwarantowane ? '' : <span className="muted"> · wyceniana w pakiecie</span>}</td><td style={{ textAlign: 'left' }}>{r1}</td><td style={{ textAlign: 'left' }} className="muted">{r2}</td></tr>; })}
        </tbody></table></div></div>)}
        {!nfz.length && <p className="muted">Brak wyników.</p>}
      </section>

      <section className="card" aria-labelledby="kp-pryw" data-testid="kp-tab-pryw">
        <h2 id="kp-pryw" style={{ marginTop: 0 }}>Tabela 2 – Procedury prywatne ({pryw.length})</h2>
        <p className="hint">Do <a href="/opisy-prywatne">Opisów prywatnych</a>: Twoje procedury i karty, których NFZ nie wycenia. Cena i wynagrodzenie lekarza z <a href="/opisy-prywatne">Cennika</a> {gab ? <>gabinetu <b>{gab.name}</b></> : 'bez gabinetu'}; brak % w Cenniku – % gabinetu z <a href="/gabinety">Gabinetów</a>. Wynagrodzenie = cena × % / 100.</p>
        {k.kat.map(kt => { const ps = pryw.filter(p => p.kat === kt.id); return ps.length ? <div key={kt.id}><h3>{kt.name}</h3><div style={{ overflowX: 'auto' }}><table className="num" data-testid="kp-pryw-tab"><thead><tr><th>Procedura</th><th>Źródło</th><th>Cena</th><th>Wynagrodzenie lekarza</th></tr></thead><tbody>
          {ps.map(p => { const c = cenaPryw(cennik, g, p.id, kPct); return <tr key={p.id} data-pid={p.id}><td style={{ textAlign: 'left' }}>{p.kod ? <a href={`/katalog-procedur/PROC-${p.kod}`}>{p.kod}</a> : null} {p.nazwa}</td><td>{p.wlasna ? 'Twój szablon' : 'karta procedury'}</td><td>{zl(c.c)}</td><td>{c.pay == null ? <span className="muted">{c.c == null ? 'brak ceny' : c.opis}</span> : <>{zl(c.pay)} <span className="muted">({c.opis})</span></>}</td></tr>; })}
        </tbody></table></div></div> : null; })}
        {!pryw.length && <p className="muted">Brak wyników.</p>}
      </section>

      {bad.length > 0 && <section className="card" aria-labelledby="kp-bad"><h2 id="kp-bad" style={{ marginTop: 0 }}>Badania ({bad.length})</h2>
        <ul data-testid="kp-badania">{bad.map(x => <li key={x.id}><a href={`/katalog-procedur/${x.id}`}>{x.nazwa}</a> <span className={x.status === 'verified' ? 'badge' : 'badge warn'}>{STATUS[x.status] ?? x.status}</span></li>)}</ul></section>}
      <p className="src">Dane: data/procedury-icd9, data/nfz, data/badania · rozliczenie NFZ: generator/nfz-pakiety-dane.js · rejestr: docs/procedury-icd9/REJESTR_KOMPLETNOSCI.md</p>
    </main>
  );
}
