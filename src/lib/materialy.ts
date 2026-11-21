// Własne materiały użytkownika (prompt Patryka 21.11.2026, pkt 1.2): nazwy preparatów do ponownego użycia w Opisach NFZ
// i prywatnych. To NIE są dane pacjentów – tylko nazwy handlowe. Zapis: user_settings.settings → klucz "mat" (bez migracji).
export const MAT_KINDS = {
  kompozyt: 'Kompozyty i materiały wypełnień',
  lakier: 'Lakiery fluorkowe',
  podklad: 'Materiały podkładowe',
  inne: 'Inne materiały',
  kolor: 'Kolory (zlecenia protetyczne)',
  lab: 'Laboratoria / technicy',
  implant: 'Systemy implantów',
  praca: 'Własne rodzaje prac protetycznych',
} as const;
export type MatKind = keyof typeof MAT_KINDS;
export type Mat = Record<MatKind, string[]>;

const MAX_ITEMS = 60, MAX_LEN = 80;
const cleanName = (s: unknown) => String(s ?? '').replace(/[\u0000-\u001f<>]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, MAX_LEN);

/** Walidacja po stronie serwera: tylko znane rodzaje, krótkie nazwy bez znaków HTML, bez duplikatów (wielkość liter bez znaczenia). */
export function cleanMat(x: unknown): Mat {
  const o = (x && typeof x === 'object' ? x : {}) as Record<string, unknown>;
  const out = {} as Mat;
  for (const k of Object.keys(MAT_KINDS) as MatKind[]) {
    const seen = new Set<string>(), list: string[] = [];
    for (const raw of Array.isArray(o[k]) ? (o[k] as unknown[]) : []) {
      const n = cleanName(raw);
      if (!n || seen.has(n.toLowerCase())) continue;
      seen.add(n.toLowerCase()); list.push(n);
      if (list.length >= MAX_ITEMS) break;
    }
    out[k] = list;
  }
  return out;
}
/** Pole tekstowe „jedna nazwa w linii” → lista. */
export const linesOf = (s: string) => s.split(/\r?\n/);
