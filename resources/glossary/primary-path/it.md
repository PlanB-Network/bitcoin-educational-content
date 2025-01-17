---
term: PERCORSO PRIMARIO

---
In un software di portafoglio che utilizza Miniscript, come ad esempio Liana, il percorso primario si riferisce all'insieme di chiavi che consentono di spendere immediatamente i fondi, senza alcuna condizione temporale. Questo percorso è sempre accessibile e viene utilizzato per la gestione quotidiana dei bitcoin, senza richiedere un'attesa (timelock) a differenza dei percorsi di recupero. Prendiamo l'esempio di uno script che incorpora 2 chiavi distinte: la chiave A, che autorizza la spesa immediata dei bitcoin, e la chiave B, che permette di spenderli dopo un ritardo definito da un timelock di 52.560 blocchi. In questo esempio, la chiave A proviene dal percorso primario, mentre la chiave B proviene dal percorso di recupero.