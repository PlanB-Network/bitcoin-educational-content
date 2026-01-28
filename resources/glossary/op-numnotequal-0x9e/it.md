---
term: OP_NUMNOTEQUAL (0X9E)

definition: Opcode che verifica se i due elementi in cima allo stack sono numericamente diversi.
---
Confronta i due elementi più alti della pila per verificare se sono numericamente disuguali. Se i valori non sono uguali, spinge `1` (vero) sulla pila, altrimenti spinge `0` (falso). È l'opposto di `OP_NUMEQUAL`.