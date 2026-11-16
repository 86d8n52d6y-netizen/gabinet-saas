'use client';
// „Sprawdź wycenę” – kalkulator punktów i kwot NFZ (ten sam silnik co generator). Do porównania ze starą aplikacją.
import { useMemo, useState } from 'react';
import { nfzPoints, visitMoney, fmtP, fmtC, packageNote, type Catalog, type CustomCode } from '@/lib/nfz/engine';
import type { NfzSettings } from '@/lib/settings';

export default function Wycena({ catalog, custom, settings }: { catalog: Catalog; custom: CustomCode[]; settings: NfzSettings }) {
  const codes = Object.values(catalog).filter(e => e.kind !== 'anest');
  const anest = Object.values(catalog).filter(e => e.kind === 'anest');
  const [qty, setQty] = useState<Record<string, number>>({});
  const [an, setAn] = useState<Record<string, number>>({});
  const [cq, setCq] = useState<Record<string, number>>({});
  const [age, setAge] = useState(''); const [preg, setPreg] = useState(false);
  const ageN = /^\d{1,3}$/.test(age) ? Number(age) : null;
  const P = useMemo(() => nfzPoints(catalog, {
    items: Object.entries(qty).filter(([, q]) => q >= 0).map(([code, q]) => ({ code, qty: q })),
    anest: an, custom: custom.filter(c => cq[c.code] > 0).map(c => ({ item: c, qty: cq[c.code] })), age: ageN, pregnant: preg,
  }), [catalog, custom, qty, an, cq, ageN, preg]);
  const k = visitMoney({ pts: P.total, price: settings.price, pct: settings.pct, revH: 0, revRate: settings.rev }, settings.basis);
  const num = (v: string) => Math.max(0, Math.min(32, parseInt(v, 10) || 0));
  return (
    <div>
      <div className="row" style={{ marginTop: 0 }}>
        <label style={{ margin: 0 }}>Wiek pacjenta (lata) <input type="text" inputMode="numeric" value={age} onChange={e => setAge(e.target.value)} style={{ width: 90 }} aria-label="Wiek pacjenta" /></label>
        <label className="check" style={{ margin: 0 }}><input type="checkbox" checked={preg} onChange={e => setPreg(e.target.checked)} /> ciąża / połóg</label>
      </div>
      <p className="hint">Wiek wpływa tylko na współczynnik (×1,5 do 18 r.ż.). Nic z tego formularza nie jest zapisywane.</p>
      <table className="pick">
        <thead><tr><th>Kod</th><th>Świadczenie</th><th>Ilość</th></tr></thead>
        <tbody>
          {codes.map(e => (
            <tr key={e.code}>
              <td><label className="check" style={{ margin: 0 }}><input type="checkbox" checked={e.code in qty} aria-label={'Kod ' + e.code}
                onChange={x => setQty(q => { const n = { ...q }; if (x.target.checked) n[e.code] = 1; else delete n[e.code]; return n; })} /> <b>{e.code}</b></label></td>
              <td>{e.name} <span className="muted">· {e.points} pkt{e.unit ? ' / ' + e.unit : ''}</span></td>
              <td>{e.code in qty && <input type="number" min={0} max={32} value={qty[e.code]} aria-label={'Ilość ' + e.code} style={{ width: 70 }}
                onChange={x => setQty(q => ({ ...q, [e.code]: num(x.target.value) }))} />}</td>
            </tr>))}
          {anest.map(e => (
            <tr key={e.code}><td><b>23.{e.code}</b></td><td>{e.name} <span className="muted">· {e.points} pkt</span></td>
              <td><input type="number" min={0} max={32} value={an[e.code] ?? 0} aria-label={'Liczba ' + e.code} style={{ width: 70 }}
                onChange={x => setAn(a => ({ ...a, [e.code]: num(x.target.value) }))} /></td></tr>))}
          {custom.map(c => (
            <tr key={'c' + c.code}><td><b>{c.code}</b> <span className="badge warn">własny</span></td><td>{c.name} <span className="muted">· {c.points} pkt</span></td>
              <td><input type="number" min={0} max={32} value={cq[c.code] ?? 0} aria-label={'Ilość ' + c.code} style={{ width: 70 }}
                onChange={x => setCq(a => ({ ...a, [c.code]: num(x.target.value) }))} /></td></tr>))}
        </tbody>
      </table>
      {P.rows.length > 0 && (
        <div className="card" style={{ background: 'var(--bg)' }} aria-live="polite">
          <table>
            <thead><tr><th>Kod</th><th>Ilość</th><th>Pkt</th><th>Wiek / ciąża</th><th>Pakiety (§ 13)</th><th>Punkty</th></tr></thead>
            <tbody>{P.rows.map(r => (
              <tr key={r.code}><td>{r.code}</td><td>{r.qty}</td><td>{fmtP(r.base)}</td><td>{r.kNote || '—'}</td><td>{packageNote(r, catalog)}</td><td><b>{fmtP(r.pts)}</b></td></tr>))}
            </tbody>
          </table>
          <p className="wyc" data-testid="wycena"><b>{fmtP(P.total)} pkt</b> · {fmtC(k.pc)} · lekarz {fmtP(settings.pct)}%: {fmtC(k.sh)}</p>
          {P.rows.some(r => r.custom) && <p className="hint">Własne kody: punkty × ilość, bez współczynników ×1,5 / ×1,2 / ×0,8 – niesprawdzane przez zasady NFZ.</p>}
        </div>)}
    </div>
  );
}
