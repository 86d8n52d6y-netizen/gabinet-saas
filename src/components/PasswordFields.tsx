export default function PasswordFields({ label = 'Hasło' }: { label?: string }) {
  return (<>
    <label htmlFor="password">{label}</label>
    <input id="password" name="password" type="password" autoComplete="new-password" required minLength={12} maxLength={128} />
    <p className="hint">Co najmniej 12 znaków. Najlepiej kilka słów, np. „zielony-kubek-na-biurku”.</p>
    <label htmlFor="password2">Powtórz hasło</label>
    <input id="password2" name="password2" type="password" autoComplete="new-password" required minLength={12} maxLength={128} />
  </>);
}
