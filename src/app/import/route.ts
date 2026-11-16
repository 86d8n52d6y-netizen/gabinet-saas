// Przeniesienie danych ze starej aplikacji (plik „Kopia całości”). Odszyfrowanie i zapis treści opisów – tylko w przeglądarce;
// na konto trafiają gabinety, Kalendarz, materiały i historia bez danych pacjentów (jak przy zwykłej pracy w modułach).
import { access, page } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request) {
  const a = await access();
  if ('go' in a) return Response.redirect(new URL(a.go, req.url), 303);
  return page(a.uid, a.name, 'import');
}
