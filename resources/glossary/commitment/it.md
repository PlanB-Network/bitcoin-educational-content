---
term: Commitment
---

Un Commitment (in senso crittografico) è un oggetto matematico, indicato con $C$, derivato deterministicamente da un'operazione su dati strutturati $m$ (il messaggio) e da un valore casuale $r$. Scriviamo :


$$
C = \text{commit}(m, r)
$$


Questo meccanismo comprende due operazioni principali:




- Commit: applichiamo una funzione crittografica a un messaggio $m$ e a un $r$ casuale per produrre $C$ ;
- Verifica: utilizza $C$, il messaggio $m$ e il valore $r$ per verificare che questo Commitment sia corretto. La funzione restituisce `Vero` o `Falso`.


Un Commitment deve rispettare due proprietà:




- Legame: deve essere impossibile trovare due messaggi diversi che producano lo stesso $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Come ad esempio :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Occultamento: la conoscenza di $C$ non deve rivelare il contenuto di $m$.


Nel caso del protocollo RGB, un Commitment è incluso in una transazione Bitcoin per dimostrare l'esistenza di una certa informazione in un determinato momento, senza rivelare l'informazione stessa.