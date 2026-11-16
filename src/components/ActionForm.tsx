'use client';
// Formularz akcji serwera z komunikatem błędu/sukcesu i blokadą przycisku podczas wysyłania (działa też bez JavaScriptu).
import { useActionState } from 'react';
import type { State } from '@/lib/auth/core';

type Props = {
  action: (s: State, fd: FormData) => Promise<State>;
  submit: string; pending?: string; children?: React.ReactNode; danger?: boolean; ghost?: boolean;
  after?: (s: State) => React.ReactNode;
};
export default function ActionForm({ action, submit, pending = 'Proszę czekać…', children, danger, ghost, after }: Props) {
  const [state, run, busy] = useActionState(action, {} as State);
  return (
    <form action={run} noValidate={false}>
      {children}
      {state.error && <p className="msg err" role="alert">{state.error}</p>}
      {state.ok && <p className="msg ok" role="status">{state.ok}</p>}
      {after?.(state)}
      <div className="row"><button type="submit" disabled={busy} className={danger ? 'danger' : ghost ? 'ghost' : undefined}>{busy ? pending : submit}</button></div>
    </form>
  );
}
