---
term: OP_HASH256 (0XAA)
---

Tar det översta objektet från stacken och ersätter det med dess Hash genom att använda funktionen `SHA256` två gånger. Inmatningen hashas en gång med `SHA256` och sedan hashas sammanställningen en andra gång med `SHA256`. Denna tvåstegsprocess genererar ett 256-bitars fingeravtryck.