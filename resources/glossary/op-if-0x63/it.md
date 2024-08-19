---
termine: OP_IF (0X63)
---

Esegue la porzione successiva dello script se il valore in cima allo stack è non-zero (vero). Se il valore è zero (falso), queste operazioni vengono saltate, passando direttamente a quelle dopo `OP_ELSE`, se presente. `OP_IF` consente l'avvio di una struttura di controllo condizionale all'interno di uno script. Determina il flusso di controllo in uno script basato su una condizione fornita al momento dell'esecuzione della transazione. `OP_IF` viene utilizzato con `OP_ELSE` e `OP_ENDIF` nel seguente modo:

```text
<condizione>
OP_IF
<operazioni se la condizione è vera>
OP_ELSE
<operazioni se la condizione è falsa>
OP_ENDIF
```