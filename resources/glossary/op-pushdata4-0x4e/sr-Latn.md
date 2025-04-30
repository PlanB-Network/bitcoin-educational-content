---
term: OP_PUSHDATA4 (0X4E)
---

Omogućava guranje veoma velike količine podataka na stek. Sledi ga četiri bajta (mali endian) koji označavaju dužinu podataka za guranje (do oko 4.3 GB). Ovaj opcode se koristi za umetanje veoma velikih podataka u skripte, iako je njegova upotreba izuzetno retka zbog praktičnih ograničenja veličine transakcije.