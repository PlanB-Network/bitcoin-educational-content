---
term: OP_ENDIF (0X68)

---
Segna la fine di una struttura di controllo condizionale iniziata da un `OP_IF` o un `OP_NOTIF`, di solito seguito da uno o più `OP_ELSE`. Indica che l'esecuzione dello script deve continuare oltre la struttura condizionale, indipendentemente dal ramo eseguito. In altre parole, `OP_ENDIF` serve a delineare la fine dei blocchi condizionali negli script.