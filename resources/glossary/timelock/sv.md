---
term: Timelock
definition: Smart kontrakt-primitiv som definierar ett tidsvillkor innan en transaktion kan inkluderas i ett block.
---

En Smart contract-primitiv som gör det möjligt att ställa in ett tidsbaserat villkor som måste uppfyllas för att en transaktion ska läggas till i ett block. Det finns två typer av tidslås på Bitcoin:


- Den absoluta tidslåsningen, som anger en exakt tidpunkt före vilken transaktionen inte kan inkluderas i ett block;
- Den relativa tidslåsningen, som anger en fördröjning från godkännandet av en tidigare transaktion.

Tidsspärren kan definieras antingen som ett datum uttryckt i Unix-tid eller som ett blocknummer. Slutligen kan tidslåsningen gälla för en transaktionsutgång genom att använda en specifik opcode i låsningsskriptet (`OP_CHECKLOCKTIMEVERIFY` eller `OP_CHECKSEQUENCEVERIFY`), eller för en hel transaktion genom att använda specifika transaktionsfält (`nLockTime` eller `nSequence`).