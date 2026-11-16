import Link from 'next/link';
export default function SprawdzPoczte() {
  return (
    <main className="wrap narrow">
      <h1>Sprawdź skrzynkę e-mail</h1>
      <section className="card">
        <p>Wysłaliśmy wiadomość z linkiem do potwierdzenia adresu (ważny 24 godziny). Kliknij go, a potem zaloguj się.</p>
        <p className="muted">Nie widzisz wiadomości? Sprawdź folder spam. W wersji testowej poczta trafia do <a href="http://localhost:8025" target="_blank" rel="noreferrer">Mailpit (localhost:8025)</a>.</p>
        <div className="row"><Link className="btn" href="/logowanie">Przejdź do logowania</Link></div>
      </section>
    </main>
  );
}
