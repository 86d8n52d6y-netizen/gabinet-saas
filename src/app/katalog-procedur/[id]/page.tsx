// Karta procedury ICD-9 albo badania z bazy stomatologicznej – tylko odczyt (src/lib/baza.ts).
import { notFound } from 'next/navigation';
import { requireAccess } from '@/lib/access';
import { baza, PODSTAWA, POZIOM, STATUS, type Poz } from '@/lib/baza';
export const dynamic = 'force-dynamic';

type R = Record<string, unknown>;
const L = (x: unknown) => (Array.isArray(x) ? x as string[] : []);
const Lista = ({ t, x }: { t: string; x: unknown }) => L(x).length ? <p><b>{t}:</b> {L(x).join('; ')}</p> : null;

export default async function Karta({ params }: { params: Promise<{ id: string }> }) {
  await requireAccess();
  const { id } = await params;
  const b = await baza();
  const zr = (l?: string[]) => (l ?? []).map(z => { const s = b.zrodla.get(z); return s ? `${s.opis.split(' – ')[0]}${s.pmid ? ` (PMID ${s.pmid})` : ''}` : z; }).join('; ');
  const Pozycje = ({ l }: { l: Poz[] }) => <ul>{l.map((p, i) => <li key={i}>{p.tekst} <span className="muted">— {PODSTAWA[p.podstawa] ?? p.podstawa}{p.warunek ? `, ${p.warunek}` : ''}{p.zrodla?.length ? ` (${zr(p.zrodla)})` : ''}</span></li>)}</ul>;
  const Szablony = ({ dot }: { dot: string }) => <section className="card"><h2 style={{ marginTop: 0 }}>Szablony opisu</h2>
    {b.szablony.filter(s => s.dotyczy === dot).map(s => <div key={s.id}><h3>{s.wariant}</h3><p style={{ whiteSpace: 'pre-wrap' }} data-testid={`szablon-${s.wariant}`}>{s.tekst.replace(/\{\{(POLE-[A-Z0-9-]+)\}\}/g, (_, p) => `[${b.pola.get(p)?.etykieta ?? p}]`)}</p></div>)}
    <p className="src">[pole] – wartość wpisuje lekarz; pusty fragment jest pomijany; tekst zawsze edytowalny przed zapisem.</p></section>;

  if (id.startsWith('BAD-')) {
    const x = b.badania.find(e => e.id === id) as R | undefined;
    if (!x) notFound();
    const cel = x.cel as R, wsk = x.wskazania as R, dok = x.dokumentacja as Record<string, Poz[]>, pw = x.powiazania as R;
    return (
      <main className="wrap"><p><a href="/katalog-procedur">← Katalog procedur i badań</a></p>
        <h1>{String(x.nazwa)}</h1><p><span className="badge warn" data-testid="kp-status">{STATUS[String(x.status)]}</span> <span className="muted">{String(x.id)} · {String(x.kategoria)}</span></p>
        <section className="card"><p><b>Cel:</b> {String(cel.oceniane)}</p><Lista t="Informacje" x={cel.informacje} /><Lista t="Wykrywa" x={cel.wykrywa} /><Lista t="Wskazania" x={wsk.kiedy} /><Lista t="Szczególnie" x={wsk.szczegolnie} /></section>
        <section className="card"><h2 style={{ marginTop: 0 }}>Przebieg</h2><ol>{(x.przebieg as { krok: string; opis: string }[]).map((k, i) => <li key={i}><b>{k.krok}</b> – {k.opis}</li>)}</ol>
          <h3>Elementy oceny</h3><ul>{(x.elementy_oceny as { element: string; co: string; pole?: string }[]).map((e, i) => <li key={i}>{e.element} – {e.co}{e.pole ? <span className="muted"> (pole: {b.pola.get(e.pole)?.etykieta})</span> : null}</li>)}</ul>
          <p><b>Przykład wyniku prawidłowego</b> (nigdy nie zaznaczany za lekarza): {String(x.wynik_prawidlowy)}</p><Lista t="Przykłady nieprawidłowości" x={x.nieprawidlowosci} /></section>
        <section className="card"><h2 style={{ marginTop: 0 }}>Dokumentacja</h2><h3>Niezbędne</h3><Pozycje l={dok.niezbedne} /><h3>Zalecane</h3><Pozycje l={dok.zalecane} />{dok.sytuacyjne.length > 0 && <><h3>Zależne od sytuacji</h3><Pozycje l={dok.sytuacyjne} /></>}
          <p><b>ICD-9:</b> {(pw.icd9 as { kod: string; kiedy: string }[]).map(i => `${i.kod} (${i.kiedy})`).join('; ') || '—'}</p>
          <p><b>ICD-10 (tylko przy stwierdzeniu):</b> {(pw.icd10 as { kod: string; kiedy: string }[]).map(i => `${i.kod} ${b.icd10.get(i.kod) ?? ''} (${i.kiedy})`).join('; ') || '—'}</p></section>
        <Szablony dot={id} /><p className="src">Źródła: {zr(x.zrodla as string[])}</p>
      </main>);
  }

  const p = b.procedury.find(e => e.id === id) as (R & { status: string; kod: string; nazwa_oficjalna: string }) | undefined;
  if (!p) notFound();
  const nag = <><p><a href="/katalog-procedur">← Katalog procedur i badań</a></p><h1>{p.kod} – {p.nazwa_oficjalna}</h1>
    <p><span className="badge warn" data-testid="kp-status">{STATUS[p.status]}</span> <span className="muted">{String(p.kategoria)}{L(p.kody_aplikacji).length ? ` · Opisy NFZ: ${L(p.kody_aplikacji).join(', ')}` : ''}</span></p>
    {p.uzasadnienie_statusu ? <p className="muted">{String(p.uzasadnienie_statusu)}</p> : null}</>;
  if (p.status === 'not_started') return <main className="wrap">{nag}<p>Karta nie jest opracowana.</p></main>;
  const cel = p.cel as R, kw = p.kwalifikacja as R, prz = p.przygotowanie as R, ke = p.kontrola_efektu as R, za = p.zalecenia as R, nfz = p.nfz as R;
  const chk = b.checklisty.get(id);
  const mapy = b.mapowania.filter(m => m.procedura === id);
  return (
    <main className="wrap">{nag}
      <section className="card"><p>{String(p.opis ?? '')}</p><p><b>Na czym polega:</b> {String(cel.na_czym_polega)}</p><p><b>Cel:</b> {String(cel.cel_kliniczny)}</p><Lista t="Wskazania" x={cel.wskazania} /></section>
      <section className="card"><h2 style={{ marginTop: 0 }}>Kwalifikacja i przygotowanie</h2><Lista t="Ocenić przed" x={kw.ocena_przed} /><Lista t="Wywiad" x={kw.wywiad} />
        <ul>{(kw.przeciwwskazania as { tekst: string; rodzaj: string }[]).map((c, i) => <li key={i}><i>{c.rodzaj === 'bezwzgledne' ? 'bezwzględne' : c.rodzaj === 'wzgledne' ? 'względne' : 'ograniczenie'}:</i> {c.tekst}</li>)}</ul>
        <Lista t="Dodatkowa diagnostyka" x={kw.dodatkowa_diagnostyka} /><Lista t="Rozważ inne postępowanie" x={kw.inne_postepowanie} />
        <Lista t="Konieczne" x={prz.konieczne} /><Lista t="Opcjonalne" x={prz.opcjonalne} /><Lista t="Zależne od sytuacji" x={prz.sytuacyjne} />{prz.znieczulenie ? <p><b>Znieczulenie:</b> {String(prz.znieczulenie)}</p> : null}</section>
      <section className="card"><h2 style={{ marginTop: 0 }}>Przebieg krok po kroku</h2><ol data-testid="kp-kroki">{(p.kroki as { krok: string; uwaga?: string }[]).map((s, i) => { const k = b.kroki.get(s.krok);
        return <li key={i}><b>{k?.nazwa}</b> – {k?.opis}{k?.uwaga ? <i> Uwaga: {k.uwaga}</i> : null}{s.uwaga ? <b> W tej procedurze: {s.uwaga}</b> : null}{k?.warianty?.length ? <span className="muted"> Warianty: {k.warianty.join('; ')}.</span> : null}</li>; })}</ol>
        <p><b>Materiały i narzędzia:</b> {(p.materialy as { mat: string; rola?: string }[]).map(m => `${b.materialy.get(m.mat)?.nazwa} (${m.rola ?? ''})`).join('; ')}</p></section>
      <section className="card"><h2 style={{ marginTop: 0 }}>Kontrola efektu i zalecenia</h2><Lista t="Sprawdzić" x={ke.sprawdzic} /><Lista t="Nieprawidłowości" x={ke.nieprawidlowosci} /><Lista t="Dalej" x={ke.dalsze_postepowanie} />
        <Lista t="Dla pacjenta" x={za.dla_pacjenta} /><Lista t="Higiena" x={za.higiena} /><Lista t="Ograniczenia" x={za.ograniczenia} /><Lista t="Kontakt z gabinetem, gdy" x={za.kontakt_gdy} />{za.kontrola ? <p><b>Kontrola:</b> {String(za.kontrola)}</p> : null}</section>
      <section className="card"><h2 style={{ marginTop: 0 }}>Dokumentacja i kompletność</h2><Pozycje l={(p.dokumentacja as { elementy: Poz[] }).elementy} />
        {chk && <><h3>Checklista</h3><ul data-testid="kp-checklista">{[...chk.wspolne.map(w => b.wspolne.get(w)!), ...chk.elementy].filter(Boolean).map(e =>
          <li key={e.id}>[{POZIOM[e.poziom] ?? e.poziom}] {e.tekst} <span className="muted">— {PODSTAWA[e.podstawa]}{e.warunek ? `, ${e.warunek}` : ''}</span></li>)}</ul>
          <p className="src">„Obowiązkowe” – przy zapisie tylko ostrzeżenie, bez blokady (decyzja Patryka 22.11.2026; rozporządzenie o dokumentacji do odczytania).</p></>}</section>
      <section className="card"><h2 style={{ marginTop: 0 }}>NFZ</h2><p>Świadczenie gwarantowane: <b>{String(nfz.swiadczenie_gwarantowane)}</b>{L(nfz.produkty).length ? ` · ${L(nfz.produkty).join('; ')}` : ''}</p>
        <ul>{L(nfz.warunki).map((w, i) => <li key={i}>{w}</li>)}</ul>{L(nfz.reguly).length ? <p>Reguły: {L(nfz.reguly).join(', ')} (Katalog NFZ → Zasady rozliczeń)</p> : null}
        {nfz.uwagi ? <p className="muted">{String(nfz.uwagi)}</p> : null}</section>
      {mapy.length > 0 && <section className="card"><h2 style={{ marginTop: 0 }}>Podpowiedzi ICD-10 (wybiera lekarz)</h2><ul data-testid="kp-icd10">{mapy.map(m => <li key={m.icd10}><b>{m.icd10}</b> {b.icd10.get(m.icd10)} – {m.okolicznosci}</li>)}</ul>
        <p className="src">Nazwy robocze – do porównania z wydaniem CeZ. NFZ nie narzuca pary procedura–rozpoznanie.</p></section>}
      <Szablony dot={id} /><p className="src">Źródła: {zr(p.zrodla as string[])}</p>
    </main>);
}
