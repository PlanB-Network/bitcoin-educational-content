---
term: OP_EVAL
definition: Opcode som föreslogs 2011 och övergavs, slutligen ersatt av P2SH.
---

Opcode som föreslogs av Gavin Andresen 2011. Den tar det skript som ligger högst upp i stacken, kör det som om det vore en del av `scriptPubKey` och placerar resultatet på stacken. `OP_EVAL` övergavs på grund av problem relaterade till komplexiteten i denna opcode, som så småningom skulle ersättas av P2SH.