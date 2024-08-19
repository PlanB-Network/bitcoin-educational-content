---
termine: OP_NUMEQUALVERIFY (0X9D)
---

Combina le operazioni `OP_NUMEQUAL` e `OP_VERIFY`. Confronta numericamente i due elementi in cima allo stack. Se i valori sono uguali, `OP_NUMEQUALVERIFY` rimuove il risultato vero dallo stack e continua l'esecuzione dello script. Se i valori non sono uguali, il risultato è falso e lo script fallisce immediatamente.