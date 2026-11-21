'use server';
// Akcje modułów pracy (etap 4a): ustawienia rozliczeń NFZ, gabinety. (Własne kody NFZ usunięte z interfejsu 21.11.2026 – dane zostają w bazie.)
// Każdy zapis: requireAccess() (sesja + licencja), rola użytkownika z RLS (withUser) i kontrola wersji –
// gdy rekord zmieniono w międzyczasie na innym urządzeniu, zapis jest odrzucany z komunikatem (bez cichego nadpisania).
import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';
import { requireAccess } from '../access';
import { withUser } from '../db';
import { str, type State } from '../auth/core';
import { cleanNfz, parseNum, PCT_OPTS } from '../settings';
import { COLORS, MODELS, type Model } from '../clinics';
import { cleanMat, linesOf, MAT_KINDS } from '../materialy';

const CONFLICT = 'Te dane zmieniono w międzyczasie na innym urządzeniu. Odśwież stronę i wprowadź zmianę ponownie.';
const ver = (fd: FormData) => { const v = Number(str(fd, 'version', 12)); return Number.isInteger(v) && v > 0 ? v : 0; };
const uuid = (s: string) => /^[0-9a-f-]{36}$/i.test(s) ? s : '';

// ---------------- ustawienia NFZ ----------------
export async function saveNfzSettings(_: State, fd: FormData): Promise<State> {
  const s = await requireAccess();
  const price = parseNum(str(fd, 'price', 20)), rev = parseNum(str(fd, 'rev', 20)), pct = Number(str(fd, 'pct', 5));
  if (!(price > 0 && price < 100)) return { error: 'Stawka za punkt: podaj liczbę większą od 0 (np. 1,84).' };
  if (!(rev > 0 && rev < 100000)) return { error: 'Stawka za godzinę przeglądów: podaj liczbę większą od 0 (np. 350).' };
  if (!(PCT_OPTS as readonly number[]).includes(pct)) return { error: 'Udział lekarza: wybierz 40% albo 35%.' };
  const nfz = cleanNfz({ price, rev, pct, basis: str(fd, 'basis', 10) });
  const r = await withUser(s.userId, c => c.query(
    `UPDATE app.user_settings SET settings = jsonb_set(settings, '{nfz}', $2::jsonb) WHERE user_id = $1 AND version = $3`,
    [s.userId, JSON.stringify(nfz), ver(fd)]));
  if (!r.rowCount) return { error: CONFLICT };
  revalidatePath('/ustawienia');
  return { ok: 'Zapisano. Nowe stawki dotyczą nowych wizyt – zapisane wizyty pamiętają stawki z dnia zapisu.' };
}

// ---------------- własne materiały (prompt 21.11.2026, pkt 1.2) ----------------
export async function saveMaterials(_: State, fd: FormData): Promise<State> {
  const s = await requireAccess();
  const mat = cleanMat(Object.fromEntries(Object.keys(MAT_KINDS).map(k => [k, linesOf(str(fd, 'mat_' + k, 20000))])));
  const r = await withUser(s.userId, c => c.query(
    `UPDATE app.user_settings SET settings = jsonb_set(settings, '{mat}', $2::jsonb) WHERE user_id = $1 AND version = $3`,
    [s.userId, JSON.stringify(mat), ver(fd)]));
  if (!r.rowCount) return { error: CONFLICT };
  revalidatePath('/ustawienia');
  const n = Object.values(mat).reduce((a, l) => a + l.length, 0);
  return { ok: `Zapisano ${n} ${n === 1 ? 'materiał' : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 'materiały' : 'materiałów'}. Pojawią się jako podpowiedzi w Opisach NFZ i prywatnych.` };
}

// ---------------- gabinety ----------------
function grosze(v: string): number | null | 'bad' {
  if (!v.trim()) return null;
  const n = parseNum(v);
  return isNaN(n) || n > 1e7 ? 'bad' : Math.round(n * 100);
}
export async function saveClinic(_: State, fd: FormData): Promise<State> {
  const s = await requireAccess();
  const id = uuid(str(fd, 'id', 40));
  const name = str(fd, 'name', 100).trim().replace(/[\u0000-\u001f<>]/g, '');
  const short = str(fd, 'short', 10).trim().toUpperCase().replace(/[^A-Z0-9ĄĆĘŁŃÓŚŹŻ]/g, '').slice(0, 6) || null;
  const color = Number(str(fd, 'color', 3));
  const model = str(fd, 'model', 20) as Model;
  const address = str(fd, 'address', 200).trim().replace(/[\u0000-\u001f<>]/g, '');
  if (!name || name.length > 80) return { error: 'Podaj nazwę gabinetu (do 80 znaków).' };
  if (!(model in MODELS)) return { error: 'Wybierz sposób rozliczenia.' };
  if (!(Number.isInteger(color) && color >= 1 && color <= COLORS)) return { error: 'Wybierz kolor.' };
  const pctS = str(fd, 'pct', 10), lsS = str(fd, 'lab_share', 10);
  const pct = pctS.trim() ? parseNum(pctS) : null, labShare = lsS.trim() ? parseNum(lsS) : null;
  if (model.startsWith('pct') && !(pct !== null && pct >= 0 && pct <= 100)) return { error: 'Podaj Twój procent (0–100).' };
  if (labShare !== null && !(labShare >= 0 && labShare <= 100)) return { error: 'Udział w kosztach labu: 0–100%.' };
  const hourly = grosze(str(fd, 'hourly', 20)), daily = grosze(str(fd, 'daily', 20)), minDaily = grosze(str(fd, 'min_daily', 20));
  if ([hourly, daily, minDaily].includes('bad')) return { error: 'Kwoty wpisz jako liczby, np. 150 albo 150,50.' };
  if (model === 'hourly' && !hourly) return { error: 'Podaj stawkę za godzinę.' };
  if (model === 'daily' && !daily) return { error: 'Podaj stawkę za dzień.' };
  const vals = [name, short, color, model, model.startsWith('pct') ? pct : null, model === 'pct_share' ? labShare : null,
    hourly, daily, minDaily, JSON.stringify({ address })];
  const r = await withUser(s.userId, async c => {
    if (!id) {
      const n = (await c.query('SELECT count(*)::int AS n FROM app.clinics WHERE deleted_at IS NULL')).rows[0].n;
      if (n >= 30) return 'limit';
      await c.query(`INSERT INTO app.clinics(owner_id, name, short, color, model, pct, lab_share, hourly_gr, daily_gr, min_daily_gr, extra, sort)
                     VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11::jsonb,$12)`, [s.userId, ...vals, n]);
      return 'ok';
    }
    const u = await c.query(`UPDATE app.clinics SET name=$2, short=$3, color=$4, model=$5, pct=$6, lab_share=$7, hourly_gr=$8, daily_gr=$9,
        min_daily_gr=$10, extra = extra || $11::jsonb WHERE id=$1 AND version=$12 AND deleted_at IS NULL`, [id, ...vals, ver(fd)]);
    return u.rowCount ? 'ok' : 'conflict';
  });
  if (r === 'limit') return { error: 'Można mieć najwyżej 30 gabinetów.' };
  if (r === 'conflict') return { error: CONFLICT };
  revalidatePath('/gabinety');
  redirect(`/gabinety?ok=${id ? 'zmieniono' : 'dodano'}`);
}

/** Aktywny / nieaktywny (gabinet, w którym już nie pracujesz – zostaje w historii i statystykach). */
export async function toggleClinic(fd: FormData): Promise<void> {
  const s = await requireAccess();
  const id = uuid(str(fd, 'id', 40));
  if (id) await withUser(s.userId, c => c.query('UPDATE app.clinics SET active = NOT active WHERE id = $1 AND deleted_at IS NULL', [id]));
  revalidatePath('/gabinety');
}
