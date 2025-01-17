---
term: MTP (TEMPO MEDIO PASSATO)

---
Questo concetto è utilizzato nel protocollo Bitcoin per determinare un margine sul timestamp del consenso della rete. L'MTP è definito come la mediana dei timestamp degli ultimi 11 blocchi estratti. L'uso di questo indicatore aiuta a evitare disaccordi tra i nodi sull'ora esatta in caso di discrepanze. L'MTP è stato inizialmente utilizzato per verificare la validità dei timestamp dei blocchi rispetto al passato. Dal BIP113, è stato utilizzato anche come riferimento per il tempo di rete per verificare la validità delle transazioni time-lock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`).