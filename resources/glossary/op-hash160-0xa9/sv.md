---
term: OP_HASH160 (0XA9)
definition: Opcode som hashar det översta elementet med SHA256 och sedan RIPEMD160.
---

Tar det översta elementet från stacken och ersätter det med dess Hash, med hjälp av funktionerna `SHA256` och `RIPEMD160` samtidigt. Denna tvåstegsprocess genererar ett 160-bitars fingeravtryck.