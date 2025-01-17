---
term: OP_IF (0X63)

---
Esegue la seguente parte dello script se il valore in cima alla pila è diverso da zero (true). Se il valore è zero (falso), queste operazioni vengono saltate, passando direttamente a quelle dopo `OP_ELSE`, se presente. `OP_IF` consente di lanciare una struttura di controllo condizionale all'interno di uno script. Determina il flusso di controllo in uno script in base a una condizione fornita al momento dell'esecuzione della transazione. `OP_IF` viene utilizzato con `OP_ELSE` e `OP_ENDIF` nel modo seguente:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```