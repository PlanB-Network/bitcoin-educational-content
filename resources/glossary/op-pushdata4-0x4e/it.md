---
termine: OP_PUSHDATA4 (0X4E)
---

Consente di inserire una quantità molto grande di dati nello stack. È seguito da quattro byte (little-endian) che indicano la lunghezza dei dati da inserire (fino a circa 4,3 GB). Questo opcode viene utilizzato per inserire dati molto grandi negli script, sebbene il suo utilizzo sia estremamente raro a causa delle limitazioni pratiche sulla dimensione delle transazioni.