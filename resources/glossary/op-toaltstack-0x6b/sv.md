---
term: OP_TOALTSTACK (0X6B)
definition: Opcode som flyttar toppen av huvudstacken till den alternativa stacken.
---

Tar toppen av huvudstacken (*main stack*) och flyttar den till den alternativa stacken (*alt stack*). Denna opcode används för att temporärt lagra data för senare användning i skriptet. Det flyttade objektet tas därmed bort från huvudstacken. `OP_FROMALTSTACK` kommer sedan att användas för att lägga tillbaka det ovanpå huvudstacken.