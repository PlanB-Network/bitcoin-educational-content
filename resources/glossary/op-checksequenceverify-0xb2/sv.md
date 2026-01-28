---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
definition: Opcode som inför ett relativt tidsvillkor för att spendera en UTXO.
---

Gör transaktionen ogiltig om någon av dessa egenskaper observeras:


- Stapeln är tom;
- Värdet högst upp i stacken är mindre än `0`;
- Inaktiveringsflaggan för värdet högst upp i stacken är odefinierad och; Transaktionsversionen är mindre än `2` eller; Inaktiveringsflaggan för fältet `nSequence` i inmatningen är inställd eller; Tidslocktypen är inte densamma mellan fältet `nSequence` och värdet högst upp i stacken (realtid eller antal block) eller; Värdet högst upp i stacken är större än värdet i fältet `nSequence` i inmatningen.


Om en eller flera av dessa egenskaper observeras kan skriptet som innehåller `OP_CHECKSEQUENCEVERIFY` inte uppfyllas. Om alla villkor är giltiga fungerar `OP_CHECKSEQUENCEVERIFY` som en `OP_NOP`, vilket innebär att den inte utför någon åtgärd i skriptet. Det är som om den försvinner. `OP_CHECKSEQUENCEVERIFY` sätter alltså en relativ tidsbegränsning på användningen av UTXO som är säkrad med skriptet som innehåller den. Den kan göra detta antingen i form av realtid eller som ett antal block. För att göra detta begränsar den de möjliga värdena för fältet `nSequence` i inmatningen som spenderar den, och detta fält `nSequence` begränsar i sig när transaktionen som innehåller denna inmatning kan inkluderas i ett block.


> ► *Den här opkoden är en ersättning för `OP_NOP`. Den placerades på `OP_NOP3`. Den refereras ofta till med sin akronym "CSV". Observera att `OP_CSV` inte ska förväxlas med fältet `nSequence` i en transaktion. Det förra använder det senare, men deras natur och åtgärder är olika.*