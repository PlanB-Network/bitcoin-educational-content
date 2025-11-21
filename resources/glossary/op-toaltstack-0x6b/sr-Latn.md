---
term: OP_TOALTSTACK (0X6B)
---

Uzima vrh glavne steka (*main stack*) i premešta ga na alternativni stek (*alt stack*). Ovaj opcode se koristi za privremeno skladištenje podataka za kasniju upotrebu u skripti. Premještena stavka se na taj način uklanja iz glavne steka. `OP_FROMALTSTACK` će se zatim koristiti da je vrati na vrh glavne steka.