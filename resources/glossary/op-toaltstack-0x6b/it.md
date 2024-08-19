---
termine: OP_TOALTSTACK (0X6B)
---

Prende il vertice dello stack principale (*main stack*) e lo sposta nello stack alternativo (*alt stack*). Questo opcode viene utilizzato per memorizzare temporaneamente dati da parte per un utilizzo successivo nello script. L'elemento spostato viene quindi rimosso dallo stack principale. `OP_FROMALTSTACK` verrà poi utilizzato per rimetterlo in cima allo stack principale.