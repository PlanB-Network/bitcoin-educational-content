---
term: BIP0118
---

Voorstel voor het verbeteren van Bitcoin gericht op het introduceren van twee nieuwe SigHash Flag modifiers: `SIGHASH_ANYPREVOUT` en `SIGHASH_ANYPREVOUTANYSCRIPT`. Deze functies breiden de mogelijkheden van Bitcoin transacties uit, vooral in termen van slimme contracten en overlay oplossingen zoals de Lightning Network. BIP118 zou met name het gebruik van Eltoo mogelijk maken. Het belangrijkste voordeel van `SIGHASH_ANYPREVOUT` is het hergebruik van handtekeningen over meerdere transacties, wat meer flexibiliteit biedt. Specifiek staan deze SigHashes een handtekening toe die geen van de invoer van de transactie dekt.