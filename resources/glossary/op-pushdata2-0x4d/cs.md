---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode vkládající až 65 KB dat na zásobník.
---
Umožňuje vložit na zásobník velké množství dat. Následují dva bajty (little-endian), které určují délku vkládaných dat (až 65 KB). Používá se pro vkládání větších dat do skriptů.