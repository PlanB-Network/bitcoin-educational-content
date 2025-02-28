---
term: OP_EQUALVERIFY (0X88)

---
Combina le funzioni di `OP_EQUAL` e `OP_VERIFY`. Verifica innanzitutto l'uguaglianza dei primi due valori in pila, quindi richiede che il risultato sia non nullo, altrimenti la transazione non è valida. `OP_EQUALVERIFY` è particolarmente usato negli script di verifica degli indirizzi.