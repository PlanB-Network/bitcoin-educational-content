---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode che inserisce fino a 65 KB di dati sullo stack.
---
Consente di inserire una grande quantità di dati nello stack. È seguito da due byte (little-endian) che specificano la lunghezza dei dati da inserire (fino a circa 65 KB). Viene utilizzato per inserire dati più grandi negli script.