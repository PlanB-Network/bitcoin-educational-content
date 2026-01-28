---
term: OP_PUSHDATA4 (0X4E)
definition: Opcode som skjuter in mycket stora mängder data på stacken (används sällan).
---

Gör det möjligt att lägga en mycket stor mängd data på stacken. Den följs av fyra byte (little-endian) som anger längden på de data som ska skjutas (upp till ca 4,3 GB). Denna opcode används för att infoga mycket stora datamängder i skript, även om det är extremt ovanligt på grund av praktiska begränsningar av transaktionsstorleken.