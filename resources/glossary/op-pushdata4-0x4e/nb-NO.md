---
term: OP_PUSHDATA4 (0X4E)

definition: Opcode som skyver svært store mengder data på stakken (brukes sjelden).
---
Gjør det mulig å skyve svært store datamengder inn i stakken. Den etterfølges av fire byte (little-endian) som angir lengden på dataene som skal skyves inn (opp til ca. 4,3 GB). Denne opkoden brukes til å sette inn svært store datamengder i skript, selv om den brukes svært sjelden på grunn av praktiske begrensninger på transaksjonsstørrelsen.