// Zakładka „NFZ” (etap E4): opis i wycena punktowa z kart procedur zweryfikowanych – osobny moduł; Opisy NFZ (/opisy-nfz) bez zmian.
// Na serwer trafia tylko strona modułu i dane startowe konta (gabinety, ustawienia stawek, „Moje materiały”) – bez danych pacjentów.
import { access, page } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request) {
  const a = await access();
  if ('go' in a) return Response.redirect(new URL(a.go, req.url), 303);
  return page(a.uid, a.name, 'nfzk');
}
