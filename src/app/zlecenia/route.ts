// Zlecenia protetyczne (docs/ZLECENIA_PROTETYCZNE.md). Treść zleceń tylko na urządzeniu (zaszyfrowana kluczem urządzenia) –
// na serwer trafia wyłącznie strona modułu i dane startowe konta (gabinety, „Moje materiały”), bez danych pacjentów.
import { access, page } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request) {
  const a = await access();
  if ('go' in a) return Response.redirect(new URL(a.go, req.url), 303);
  return page(a.uid, a.name, 'zlecenia');
}
