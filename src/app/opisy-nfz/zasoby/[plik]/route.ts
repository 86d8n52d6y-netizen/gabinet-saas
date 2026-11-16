import { access, asset, ASSETS } from '@/lib/nfz/generator';
export const dynamic = 'force-dynamic';
export async function GET(req: Request, ctx: { params: Promise<{ plik: string }> }) {
  const { plik } = await ctx.params;
  if (!ASSETS.test(plik)) return new Response('Nie znaleziono', { status: 404 });
  const a = await access();
  if ('go' in a) return new Response('Wymagane logowanie', { status: 401 });
  return asset(plik, req.headers.get('if-none-match'));
}
