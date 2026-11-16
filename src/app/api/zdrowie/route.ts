import { health } from '@/lib/health';
export const dynamic = 'force-dynamic';
export async function GET() {
  const checks = await health();
  const ok = checks.every(c => c.ok);
  return Response.json({ ok, checks: checks.map(({ name, ok }) => ({ name, ok })) }, { status: ok ? 200 : 503, headers: { 'Cache-Control': 'no-store' } });
}
