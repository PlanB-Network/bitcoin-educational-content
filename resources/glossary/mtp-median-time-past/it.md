---
termine: MTP (MEDIAN TIME PAST)
---

Questo concetto è utilizzato nel protocollo Bitcoin per determinare un margine sul timestamp di consenso della rete. MTP è definito come la mediana dei timestamp degli ultimi 11 blocchi estratti. L'uso di questo indicatore aiuta a evitare disaccordi tra i nodi riguardo l'orario esatto in caso di discrepanze. MTP è stato inizialmente utilizzato per verificare la validità dei timestamp dei blocchi rispetto al passato. Dal BIP113, è stato anche utilizzato come riferimento per l'orario della rete per verificare la validità delle transazioni con blocco temporale (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`).