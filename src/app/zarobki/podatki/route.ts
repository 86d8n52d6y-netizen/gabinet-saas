// Zarobki → Podatki i ZUS: widok przeniesiony z Kalendarza (decyzja Patryka 21.11.2026, poprawka K41) –
// ten sam kod i obliczenia Kalendarza (generator/kalendarz.html), dane z tych samych dokumentów konta.
import { access, page } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request) {
  const a = await access();
  if ('go' in a) return Response.redirect(new URL(a.go, req.url), 303);
  return page(a.uid, a.name, 'kalendarz', 'podatki');
}
