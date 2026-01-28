---
term: OP_PUSHDATA1 (0X4C)

definition: Opcode che inserisce fino a 255 byte di dati sullo stack.
---
Spinge una certa quantità di dati sullo stack. È seguito da un byte che indica la lunghezza dei dati da inserire (fino a 255 byte). Questo opcode viene utilizzato per includere dati di dimensioni variabili negli script.