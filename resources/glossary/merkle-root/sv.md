---
term: Merkle-rot
definition: Unik hash som sammanfattar alla transaktioner i ett block, inkluderad i blockhuvudet.
---

Digest eller "topp Hash" i en Merkle Tree, som utgör en sammanfattning av all information som finns i trädet. En Merkle Tree är en kryptografisk ackumulatorstruktur, som ibland också kallas ett "Hash-träd". I samband med Bitcoin används Merkle-träd för att organisera transaktioner inom ett block och för att underlätta en snabb verifiering av att en viss transaktion ingår. I Bitcoin-block erhålls således Merkle Root genom att successivt hasha transaktioner i par tills endast en Hash återstår (Merkle Root). Denna inkluderas sedan i rubriken för motsvarande block. Detta Hash-träd finns också i UTREEXO, en struktur som gör det möjligt att kondensera UTXO-noduppsättningen, och i MAST Taproot.