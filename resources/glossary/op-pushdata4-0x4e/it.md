---
term: OP_PUSHDATA4 (0X4E)

---
Consente di inserire nello stack una quantità di dati molto elevata. È seguito da quattro byte (little-endian) che indicano la lunghezza dei dati da inserire (fino a circa 4,3 GB). Questo opcode viene utilizzato per inserire dati molto grandi negli script, anche se il suo uso è estremamente raro a causa delle limitazioni pratiche sulla dimensione delle transazioni.