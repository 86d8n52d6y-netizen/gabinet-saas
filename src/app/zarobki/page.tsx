import Link from 'next/link';
import { requireAccess } from '@/lib/access';
import { withUser } from '@/lib/db';
import { fmtC, fmtP } from '@/lib/nfz/engine';
import { RANGES, rangeOf, report, type Report } from '@/lib/zarobki';
import { kalNetto, trybKwot } from '@/lib/netto';
export const metadata = { title: 'Zarobki – Gabinet' };
export const dynamic = 'force-dynamic';

type SP = { o?: string; od?: string; do?: string; g?: string; k?: string; kw?: string };
const z = (c: number) => (c ? fmtC(c) : '—');
const fmtH = (h: number) => { const m = Math.round(h * 60); return `${Math.floor(m / 60)} h${m % 60 ? ` ${m % 60} min` : ''}`; };
// zarobek na godzinę = zarobek ÷ godziny pracy (dla podsumowania: łączny zarobek ÷ łączne godziny, nie średnia z gabinetów)
const perHour = (gr: number, h: number) => h > 0
  ? <>{fmtC(Math.round(gr / h))}<span className="hint" style={{ display: 'block' }}>{fmtH(h)}</span></>
  : <span className="muted" data-testid="brak-h">brak danych o czasie pracy</span>;
const dd = (s: string) => s.split('-').reverse().join('.');
const DOW = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'];
const MON = ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paź', 'lis', 'gru'];
const qs = (sp: SP, over: Partial<SP>) => { const o = { ...sp, ...over }; return '?' + Object.entries(o).filter(([, v]) => v).map(([k, v]) => `${k}=${encodeURIComponent(v!)}`).join('&'); };

function Chart({ r }: { r: Report }) {
  const s = r.series, W = 720, H = 200, top = 12, bottom = 26, left = 6;
  const max = Math.max(1, ...s.map(x => x.nfz + x.pryw));
  const bw = (W - left) / Math.max(1, s.length), bar = Math.max(2, Math.min(26, bw * 0.7));
  const y = (v: number) => (H - bottom) - (v / max) * (H - bottom - top);
  const label = (k: string, i: number) => r.seriesBy === 'month' ? MON[Number(k.slice(5, 7)) - 1] : (s.length <= 16 || i % Math.ceil(s.length / 16) === 0 ? String(Number(k.slice(8))) : '');
  return (
    <figure style={{ margin: 0 }}>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={`Wykres zarobków ${r.seriesBy === 'day' ? 'dziennych' : 'miesięcznych'}: NFZ i prywatne`} style={{ width: '100%', height: 'auto' }}>
        <line x1={left} x2={W} y1={H - bottom} y2={H - bottom} stroke="var(--line)" />
        {s.map((x, i) => { const cx = left + i * bw + (bw - bar) / 2; return (
          <g key={x.key}><title>{`${r.seriesBy === 'day' ? dd(x.key) : x.key}: NFZ ${fmtC(x.nfz)}, prywatne ${fmtC(x.pryw)}`}</title>
            {x.nfz > 0 && <rect x={cx} y={y(x.nfz)} width={bar} height={(H - bottom) - y(x.nfz)} fill="var(--c1)" rx="2" />}
            {x.pryw > 0 && <rect x={cx} y={y(x.nfz + x.pryw)} width={bar} height={y(x.nfz) - y(x.nfz + x.pryw)} fill="var(--c3)" rx="2" />}
            <text x={cx + bar / 2} y={H - 8} textAnchor="middle" fontSize="11" fill="var(--muted)">{label(x.key, i)}</text></g>); })}
      </svg>
      <figcaption className="hint"><span className="dot" style={{ ['--cc' as string]: 'var(--c1)' }} /> NFZ &nbsp; <span className="dot" style={{ ['--cc' as string]: 'var(--c3)' }} /> prywatne · {s.some(x => x.nfz + x.pryw > 0) ? `najwyższy ${r.seriesBy === 'day' ? 'dzień' : 'miesiąc'}: ${fmtC(max)}` : 'brak zarobków w tym okresie'}</figcaption>
    </figure>
  );
}

export default async function Zarobki({ searchParams }: { searchParams: Promise<SP> }) {
  const s = await requireAccess();
  const sp = await searchParams;
  const range = rangeOf(sp.o ?? 'month', sp.od, sp.do);
  const tryb = trybKwot(sp.kw);
  const { r, clinics, netto } = await withUser(s.userId, async c => {
    const clinics = (await c.query(`SELECT id, name FROM app.clinics WHERE deleted_at IS NULL ORDER BY sort, created_at`)).rows as { id: string; name: string }[];
    const g = sp.g && clinics.some(k => k.id === sp.g) ? sp.g : null;
    const r = await report(c, range, g, (sp.k ?? '').slice(0, 130));
    // netto tylko na żądanie i bez filtra rodzaju (zarobek lekarza z Kalendarza jest wtedy niedostępny)
    const netto = tryb === 'netto' && !r.kind ? await kalNetto(c, range.from, range.to) : null;
    return { r, clinics, g, netto };
  });
  const T = r.total;
  const N = netto?.info.ok ? netto : null;              // netto policzone z ustawień Kalendarza
  const dr = (id: string | null, brutto: number) => (N ? (id ? N.perClinic.get(id) ?? 0 : 0) : brutto);
  const drT = N ? r.rows.reduce((a, x) => a + dr(x.id, x.dr), 0) : T.dr;
  const nt = N ? ' (netto)' : '';
  return (
    <main className="wrap wide">
      <h1>Zarobki</h1>
      <nav className="tabs-row" aria-label="Okres">
        {Object.entries(RANGES).map(([k, v]) => <Link key={k} href={qs(sp, { o: k, od: '', do: '' })} className={'chip' + (range.key === k ? ' on' : '')} aria-current={range.key === k ? 'page' : undefined}>{v}</Link>)}
      </nav>
      <nav className="tabs-row" aria-label="Kwoty brutto lub netto">
        <Link href={qs(sp, { kw: '' })} className={'chip' + (tryb === 'brutto' ? ' on' : '')} aria-current={tryb === 'brutto' ? 'true' : undefined}>Brutto</Link>
        <Link href={qs(sp, { kw: 'netto' })} className={'chip' + (tryb === 'netto' ? ' on' : '')} aria-current={tryb === 'netto' ? 'true' : undefined}>Netto</Link>
      </nav>
      {tryb === 'netto' && r.kind && <p className="msg" role="status" data-testid="netto-info">Netto liczy się dla zarobku lekarza, który jest niedostępny przy filtrze rodzaju – poniżej kwoty <b>brutto</b>.</p>}
      {tryb === 'netto' && netto && !N && <p className="msg" role="status" data-testid="netto-info">Netto liczy się z Twoich ustawień w <a href="/kalendarz">Kalendarzu</a> (start JDG, forma opodatkowania, ZUS) – nie są jeszcze ustawione. Otwórz Kalendarz i wybierz je w „Ustaw podatki i ZUS”; do tego czasu poniżej są kwoty <b>brutto</b>.</p>}
      {N && <p className="msg" role="status" data-testid="netto-info">Zarobek lekarza <b>netto</b> – po odjęciu ZUS, składki zdrowotnej i podatku wg ustawień <a href="/kalendarz">Kalendarza</a> ({N.info.zasady.join(' · ')}). To szacunek: podatek i progi rozlicza się rocznie, tak samo jak „Netto ≈” w Kalendarzu. Kwoty z wizyt (Razem z wizyt, wykres, średnie, szczegóły) są brutto.
        {N.info.zusNiepotwierdzony && <> <b data-testid="netto-zus">Kwota ZUS nie jest potwierdzona w Kalendarzu</b> (Ustawienia → „Kwota się zgadza”) – netto może być niedokładne.</>}
        {N.info.szacunek && <> Część parametrów roku to szacunki (oznaczone w Ustawieniach Kalendarza).</>}</p>}
      <form className="row filters" method="get">
        {tryb === 'netto' && <input type="hidden" name="kw" value="netto" />}
        <input type="hidden" name="o" value="own" />
        <label>od <input type="date" name="od" defaultValue={range.from} required /></label>
        <label>do <input type="date" name="do" defaultValue={range.to} required /></label>
        <label>gabinet <select name="g" defaultValue={sp.g ?? ''}><option value="">wszystkie</option>{clinics.map(k => <option key={k.id} value={k.id}>{k.name}</option>)}</select></label>
        <label>rodzaj <select name="k" defaultValue={r.kind}><option value="">wszystko</option><option value="nfz">NFZ</option><option value="pryw">prywatne</option>
          {r.categories.map(k => <option key={k} value={'kat:' + k}>prywatne: {k}</option>)}</select></label>
        <button type="submit" className="ghost">Pokaż</button>
        <a className="btn ghost" href={`/zarobki/csv${qs({}, { od: range.from, do: range.to, g: sp.g, k: r.kind })}`} download>Pobierz CSV</a>
      </form>
      <p className="muted" data-testid="okres">{range.label}: {dd(range.from)} – {dd(range.to)}</p>

      {r.kind && <p className="msg" role="status">Filtr: {r.kind === 'nfz' ? 'tylko NFZ' : r.kind === 'pryw' ? 'tylko prywatne' : 'prywatne – kategoria „' + r.kind.slice(4) + '”'} · <Link href={qs(sp, { k: '' })}>pokaż wszystko</Link></p>}
      <section className="card tiles" aria-label="Podsumowanie">
        <div><span className="muted">Razem z wizyt</span><b data-testid="razem">{fmtC(T.sum)}</b><span className="hint">{T.nv + T.pv} wizyt</span></div>
        <div><span className="muted">Razem punktów</span><b data-testid="punkty">{fmtP(r.nfz.pts)} pkt</b><span className="hint">punkty NFZ z opisów</span></div>
        <div><span className="muted">Zarobek lekarza (%){nt}</span><b data-testid="zarobek">{r.kind ? '—' : fmtC(drT)}</b>
          <span className="hint">{r.kind ? 'niedostępny przy filtrze rodzaju' : 'wg zasad rozliczenia gabinetów'}</span></div>
        <div><span className="muted">Poprzedni okres ({r.prev.label})</span><b data-testid="poprz">{fmtC(r.prev.sum)}</b>
          <span className="hint" data-testid="zmiana">{r.prev.sum ? `${T.sum >= r.prev.sum ? '+' : '−'}${fmtC(Math.abs(T.sum - r.prev.sum))} (${T.sum >= r.prev.sum ? '+' : '−'}${Math.abs(Math.round((T.sum - r.prev.sum) / r.prev.sum * 1000) / 10).toLocaleString('pl-PL')}%)` : 'brak zarobków w poprzednim okresie'} · {dd(r.prev.from)} – {dd(r.prev.to)}</span></div>
      </section>

      <section className="card" aria-labelledby="gab">
        <h2 id="gab" style={{ marginTop: 0 }}>Wszystkie gabinety</h2>
        {r.rows.length ? (
          <div style={{ overflowX: 'auto' }}><table className="num" data-testid="tabela">
            <thead><tr><th>Gabinet</th><th>Liczba wizyt</th><th>Zarobek lekarza{nt}</th><th>Zarobek na godzinę{nt}</th></tr></thead>
            <tbody>{r.rows.map(x => (
              <tr key={x.id ?? '-'}><td>{x.color && <span className="dot" style={{ ['--cc' as string]: `var(--c${x.color})` }} />} {x.name}</td>
                <td>{x.vis || '—'}</td><td><b>{r.kind ? '—' : z(dr(x.id, x.dr))}</b></td><td>{r.kind ? '—' : perHour(dr(x.id, x.dr), x.h)}</td></tr>))}
            </tbody>
            <tfoot><tr><td>Razem</td><td>{T.vis || '—'}</td><td>{r.kind ? '—' : z(drT)}</td><td>{r.kind ? '—' : perHour(drT, T.h)}</td></tr></tfoot>
          </table></div>) : <p className="muted">Brak gabinetów i wizyt w tym okresie.</p>}
        <p className="hint">Liczba wizyt: wszystkie zapisane (odbyte) wizyty z Opisów NFZ i prywatnych. Zarobek lekarza: kwota należna z danego gabinetu wg jego zasad rozliczenia (<Link href="/gabinety">Gabinety</Link>), z odbytych dyżurów w <a href="/kalendarz">Kalendarzu</a> – obrót wpisujesz przy dyżurze (np. „Wpisz jako obrót”). Zarobek na godzinę: zarobek lekarza ÷ godziny odbytych dyżurów; w podsumowaniu – łączny zarobek ÷ łączne godziny.</p>
      </section>

      <section className="card" aria-labelledby="wyk">
        <h2 id="wyk" style={{ marginTop: 0 }}>{r.seriesBy === 'day' ? 'Dzień po dniu' : 'Miesiąc po miesiącu'}</h2>
        <Chart r={r} />
      </section>

      <div className="grid2 plain">
        <section className="card" aria-labelledby="sre">
          <h2 id="sre" style={{ marginTop: 0 }}>Średnie</h2>
          <table className="num" data-testid="srednie"><tbody>
            <tr><td>Dni pracy (z zapisanymi kwotami)</td><td>{r.avg.days}</td></tr>
            <tr><td>Średnio na dzień pracy</td><td>{z(r.avg.perDay)}</td></tr>
            <tr><td>Średnio na wizytę</td><td>{z(r.avg.perVisit)}</td></tr>
            {r.avg.perMonth !== null && <tr><td>Średnio na miesiąc</td><td>{z(r.avg.perMonth)}</td></tr>}
          </tbody></table>
        </section>
        <section className="card" aria-labelledby="sdt">
          <h2 id="sdt" style={{ marginTop: 0 }}>Dni tygodnia</h2>
          <table className="num" data-testid="dni"><thead><tr><th>Dzień</th><th>Dni pracy</th><th>Zarobek</th><th>Średnio na dzień</th></tr></thead><tbody>
            {r.weekdays.map(w => { const t = w.nfz + w.pryw; return <tr key={w.dow}><td>{DOW[w.dow - 1]}</td><td>{w.days || '—'}</td><td>{z(t)}</td><td>{w.days ? z(Math.round(t / w.days)) : '—'}</td></tr>; })}
          </tbody></table>
        </section>
      </div>

      <div className="grid2 plain">
        <section className="card" aria-labelledby="snfz">
          <h2 id="snfz" style={{ marginTop: 0 }}>NFZ – szczegóły</h2>
          <table className="num"><tbody>
            <tr><td>Wartość punktów ({fmtP(r.nfz.pts)} pkt)</td><td>{fmtC(r.nfz.pc)}</td></tr>
            <tr><td>Udział lekarza w punktach</td><td>{fmtC(r.nfz.sh)}</td></tr>
            <tr><td>Przeglądy</td><td>{fmtC(r.nfz.rv)}</td></tr>
            <tr><td>Kwoty dodatkowe</td><td>{fmtC(r.nfz.ex)}</td></tr>
            <tr><td>Czas wizyt</td><td>{Math.floor(r.nfz.minutes / 60)} h {r.nfz.minutes % 60} min</td></tr>
          </tbody></table>
          {r.topNfz.length > 0 && <><h3>Najczęstsze kody</h3><p>{r.topNfz.map(x => `${x.code} (${x.n})`).join(' · ')}</p></>}
        </section>
        <section className="card" aria-labelledby="spr">
          <h2 id="spr" style={{ marginTop: 0 }}>Prywatne – szczegóły</h2>
          <table className="num"><tbody>
            <tr><td>Wartość zabiegów</td><td>{fmtC(r.pryw.val)}</td></tr>
            <tr><td>Koszty (lab, materiały)</td><td>{fmtC(r.pryw.cost)}</td></tr>
            <tr><td>Wynagrodzenie lekarza</td><td>{fmtC(r.pryw.pay)}</td></tr>
          </tbody></table>
          {r.topPryw.length > 0 && <><h3>Najczęstsze procedury</h3><table className="num"><tbody>{r.topPryw.map(x => <tr key={x.name}><td>{x.name} ×{x.n}</td><td>{fmtC(x.pay)}</td></tr>)}</tbody></table></>}
        </section>
      </div>
    </main>
  );
}
