---
termine: OP_HASH256 (0XAA)
---

Prende l'elemento in cima allo stack e lo sostituisce con il suo hash, utilizzando la funzione `SHA256` due volte. L'input viene hashato una prima volta con `SHA256`, e poi il digest viene hashato una seconda volta con `SHA256`. Questo processo a due fasi genera un'impronta digitale di 256 bit.