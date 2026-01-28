---
term: Merkle-träd
definition: Hierarkisk datastruktur som möjliggör snabb verifiering av inkludering av en transaktion i ett block.
---

En Merkle Tree är en kryptografisk ackumulator. Det är en metod för att bevisa att en viss del av informationen ingår i en större uppsättning. Det är en datastruktur som underlättar verifiering av information i ett kompakt format. I Bitcoin-systemet används Merkle Trees för att gruppera och kondensera transaktionerna i ett block till en enda Hash, kallad Merkle Root (eller "*Root Hash*"). Varje transaktion hashas, sedan hashas de intilliggande hasharna hierarkiskt tills Merkle Root erhålls.





Denna struktur gör det möjligt att snabbt verifiera om en viss transaktion ingår i ett visst block utan att behöva analysera alla transaktioner. Om jag till exempel bara har Merkle Root och vill verifiera att `TX 7` verkligen är en del av trädet, skulle jag bara behöva följande bevis:


- `TX 7`;
- `Hash 8`;
- `Hash 5-6`;
- "Hash 1-2-3-4".

Med hjälp av dessa uppgifter kan jag beräkna de mellanliggande noderna fram till Merkle Root.





Merkle Trees används framför allt för lätta noder (s.k. "SPV") som endast behåller blockhuvudena, men inte transaktionerna. Den här strukturen finns också i UTREEXO-protokollet, ett protokoll som gör det möjligt att kondensera UTXO-uppsättningen av noder, och i MAST Taproot.


