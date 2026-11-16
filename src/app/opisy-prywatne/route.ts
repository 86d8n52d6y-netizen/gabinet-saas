// Opisy prywatne (etap 4c). Szczegóły: src/lib/nfz/generator.ts, src/lib/pryw/wizyty.ts, generator/ZMIANY.md.
import { access, page } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request) {
  const a = await access();
  if ('go' in a) return Response.redirect(new URL(a.go, req.url), 303);
  return page(a.uid, a.name, 'prywatne');
}
