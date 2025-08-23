---
term: TIMELOCK
---

Een Smart contract primitieve die het mogelijk maakt om een tijdsgebaseerde voorwaarde in te stellen waaraan voldaan moet worden om een transactie aan een blok toe te voegen. Er zijn twee soorten tijdsloten op Bitcoin:


- Het absolute tijdslot, dat een exact moment aangeeft waarvóór de transactie niet kan worden opgenomen in een blok;
- Het relatieve tijdslot, dat een vertraging instelt vanaf de acceptatie van een vorige transactie.

Het tijdslot kan gedefinieerd worden als een datum uitgedrukt in Unix-tijd of als een bloknummer. Tenslotte kan het tijdslot van toepassing zijn op een transactie uitvoer door een specifieke opcode in het locking script te gebruiken (`OP_CHECKLOCKTIMEVERIFY` of `OP_CHECKSEQUENCEVERIFY`), of op een hele transactie door specifieke transactie velden te gebruiken (`nLockTime` of `nSequence`).