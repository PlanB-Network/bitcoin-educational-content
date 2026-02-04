---
term: OP_FROMALTSTACK (0X6C)
definition: Opcode koji prebacuje element sa alternativnog stack-a na glavni stack.
---

Uklanja gornju stavku sa alternativnog steka (*alt stack*) i postavlja je na vrh glavnog steka (*main stack*). Ovaj opcode se koristi za preuzimanje podataka privremeno smeštenih na alternativnom steku. Jednostavno rečeno, to je obrnuta operacija od `OP_TOALTSTACK`.