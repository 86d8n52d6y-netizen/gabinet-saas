// Treści e-maili (zwykły tekst – czytelne w każdym programie pocztowym, bez śledzących obrazków).
import 'server-only';
import { appUrl } from '../env';

const foot = '\n\n—\nGabinet\nTa wiadomość została wysłana automatycznie. Nie odpowiadaj na nią.';
const when = () => new Date().toLocaleString('pl-PL', { timeZone: 'Europe/Warsaw' });

export const mails = {
  verify: (name: string, token: string) => ({
    subject: 'Gabinet – potwierdź adres e-mail',
    text: `Dzień dobry ${name},\n\naby potwierdzić adres e-mail i aktywować konto, otwórz link (ważny 24 godziny):\n${appUrl()}/weryfikacja?t=${token}\n\nJeśli to nie Ty zakładałeś konto, zignoruj tę wiadomość.` + foot,
  }),
  alreadyRegistered: () => ({
    subject: 'Gabinet – próba założenia konta',
    text: `Dzień dobry,\n\nktoś (może Ty) próbował założyć konto w Gabinecie na ten adres e-mail, ale konto już istnieje.\nJeśli nie pamiętasz hasła, ustaw nowe: ${appUrl()}/reset\n\nJeśli to nie Ty – nic nie musisz robić, Twoje konto jest bezpieczne.` + foot,
  }),
  reset: (token: string) => ({
    subject: 'Gabinet – ustaw nowe hasło',
    text: `Dzień dobry,\n\notrzymaliśmy prośbę o zmianę hasła. Aby ustawić nowe hasło, otwórz link (ważny 30 minut, działa jeden raz):\n${appUrl()}/reset/nowe?t=${token}\n\nJeśli to nie Ty – zignoruj wiadomość; hasło pozostanie bez zmian.` + foot,
  }),
  passwordChanged: () => ({
    subject: 'Gabinet – hasło zostało zmienione',
    text: `Dzień dobry,\n\nhasło do Twojego konta zostało zmienione (${when()}). Wylogowaliśmy pozostałe urządzenia.\n\nJeśli to nie Ty – natychmiast ustaw nowe hasło: ${appUrl()}/reset` + foot,
  }),
  newDevice: (device: string) => ({
    subject: 'Gabinet – logowanie z nowego urządzenia',
    text: `Dzień dobry,\n\nzalogowano się do Twojego konta z nowego urządzenia: ${device} (${when()}).\n\nJeśli to nie Ty – zmień hasło i wyloguj wszystkie urządzenia: ${appUrl()}/konto/bezpieczenstwo` + foot,
  }),
  mfaChanged: (on: boolean) => ({
    subject: on ? 'Gabinet – włączono weryfikację dwuetapową' : 'Gabinet – wyłączono weryfikację dwuetapową',
    text: `Dzień dobry,\n\nna Twoim koncie ${on ? 'włączono' : 'wyłączono'} weryfikację dwuetapową (${when()}).\n\nJeśli to nie Ty – zmień hasło: ${appUrl()}/reset` + foot,
  }),
};
