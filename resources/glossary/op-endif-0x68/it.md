---
termine: OP_ENDIF (0X68)
---

Segna la fine di una struttura di controllo condizionale iniziata da un `OP_IF` o un `OP_NOTIF`, solitamente seguita da uno o più `OP_ELSE`. Indica che l'esecuzione dello script dovrebbe continuare oltre la struttura condizionale, indipendentemente dal ramo che è stato eseguito. In altre parole, `OP_ENDIF` serve a delimitare la fine dei blocchi condizionali negli script.