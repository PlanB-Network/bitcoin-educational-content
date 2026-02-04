---
term: OP_PUSHDATA2 (0X4D)
definition: Opcode koji postavlja do 65 KB podataka na stack.
---

Omogućava ubacivanje velike količine podataka na stek. Sledi ga dva bajta (mali endian) koja određuju dužinu podataka koji će biti ubačeni (do oko 65 KB). Koristi se za umetanje većih podataka u skripte.