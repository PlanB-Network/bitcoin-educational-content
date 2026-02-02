---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
definition: Opcode som inför ett absolut tidsvillkor för att spendera en UTXO.
---

Gör transaktionen ogiltig om inte alla dessa villkor är uppfyllda:


- Stapeln är inte tom;
- Värdet högst upp i stacken är större än eller lika med `0`;
- Typen av tidslås är densamma mellan fältet `nLockTime` och värdet högst upp i stacken (realtid eller blocknummer);
- Fältet `nSequence` i inmatningen är inte lika med `0xffffffff`;
- Värdet högst upp i stacken är större än eller lika med värdet i fältet `nLockTime` i transaktionen.


Om något av dessa villkor inte är uppfyllt kan skriptet som innehåller `OP_CHECKLOCKTIMEVERIFY` inte uppfyllas. Om alla dessa villkor är giltiga fungerar `OP_CHECKLOCKTIMEVERIFY` som en `OP_NOP`, vilket innebär att den inte utför någon åtgärd på skriptet. Det är som om det försvinner. `OP_CHECKLOCKTIMEVERIFY` inför således en tidsbegränsning för användningen av UTXO som är säkrad med skriptet som innehåller den. Den kan göra detta antingen i form av ett Unix-tidsdatum eller som ett blocknummer. För att göra detta begränsar den de möjliga värdena för fältet `nLockTime` i den transaktion som spenderar den, och detta fält `nLockTime` begränsar i sig när transaktionen kan inkluderas i ett block.


> ► *Den här opkoden är en ersättning för `OP_NOP`. Den placerades på `OP_NOP2`. Den refereras ofta till med sin akronym "CLTV". Observera att `OP_CLTV` inte ska förväxlas med fältet `nLockTime` i en transaktion. Den förra använder den senare, men deras natur och åtgärder är olika.*