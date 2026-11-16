// Wysyłka e-maili. Lokalnie: Mailpit (przechwytuje wszystko, nic nie wychodzi do internetu).
// MAIL_DIR (tylko testy): zapis wiadomości do plików zamiast SMTP.
import 'server-only';
import nodemailer, { type Transporter } from 'nodemailer';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

let t: Transporter | null = null;
function transport() {
  t ??= nodemailer.createTransport({
    host: process.env.SMTP_HOST ?? 'localhost', port: Number(process.env.SMTP_PORT ?? 1025),
    secure: process.env.SMTP_SECURE === '1',
    auth: process.env.SMTP_USER ? { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS ?? '' } : undefined,
  });
  return t;
}

export async function sendMail(to: string, subject: string, text: string) {
  const from = process.env.MAIL_FROM ?? 'Gabinet <no-reply@gabinet.local>';
  if (process.env.MAIL_DIR) {
    await mkdir(process.env.MAIL_DIR, { recursive: true });
    const f = path.join(process.env.MAIL_DIR, `${Date.now()}-${Math.random().toString(36).slice(2, 8)}.json`);
    await writeFile(f, JSON.stringify({ from, to, subject, text }));
    return;
  }
  await transport().sendMail({ from, to, subject, text });
}
