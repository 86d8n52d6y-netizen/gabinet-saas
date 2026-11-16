import ActionForm from '@/components/ActionForm';
import { verifyEmail } from '@/lib/auth/actions';
export const metadata = { title: 'Potwierdzenie adresu – Gabinet', referrer: 'no-referrer' };

// Potwierdzenie przyciskiem (POST), a nie samym otwarciem linku – skanery poczty nie zużyją tokenu.
export default async function Weryfikacja({ searchParams }: { searchParams: Promise<{ t?: string }> }) {
  const { t = '' } = await searchParams;
  return (
    <main className="wrap narrow">
      <h1>Potwierdź adres e-mail</h1>
      <section className="card">
        <ActionForm action={verifyEmail} submit="Potwierdzam adres e-mail" pending="Potwierdzam…">
          <input type="hidden" name="t" value={t} />
        </ActionForm>
      </section>
    </main>
  );
}
