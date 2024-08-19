---
termine: OP_EQUALVERIFY (0X88)
---

Combina le funzioni di `OP_EQUAL` e `OP_VERIFY`. Verifica prima l'uguaglianza dei due valori in cima allo stack, poi richiede che il risultato sia non-zero; in caso contrario, la transazione è invalida. `OP_EQUALVERIFY` è notevolmente utilizzato negli script di verifica degli indirizzi.