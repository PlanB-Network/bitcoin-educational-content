---
term: OP_FROMALTSTACK (0X6C)
definition: Opcode som flyttar ett element från den alternativa stacken till huvudstacken.
---

Tar bort det översta objektet från den alternativa stacken (*alt stack*) och placerar det överst på huvudstacken (*main stack*). Denna opcode används för att hämta data som tillfälligt lagrats på den alternativa stacken. Enkelt uttryckt är det den omvända operationen av `OP_TOALTSTACK`.