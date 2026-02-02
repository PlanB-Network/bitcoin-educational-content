---
term: BIP0118
definition: ANYPREVOUT-förslag som introducerar nya SigHash Flags som gör det möjligt att återanvända signaturer mellan transaktioner, användbart för Eltoo.
---

Förslag till förbättring av Bitcoin som syftar till att införa två nya SigHash Flag-modifierare: `SIGHASH_ANYPREVOUT` och `SIGHASH_ANYPREVOUTANYSCRIPT`. Dessa funktioner utökar kapaciteten för Bitcoin-transaktioner, särskilt när det gäller smarta kontrakt och överlagringslösningar som Lightning Network. BIP118 skulle särskilt möjliggöra användning av Eltoo. Den största fördelen med `SIGHASH_ANYPREVOUT` är att tillåta återanvändning av signaturer över flera transaktioner, vilket ger mer flexibilitet. Specifikt tillåter dessa SigHashes en signatur som inte täcker någon av transaktionens ingångar.