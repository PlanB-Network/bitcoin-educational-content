---
term: Utreexo
definition: Protokoll som komprimerar UTXO-setet för Bitcoin-noder via en ackumulator baserad på Merkle-träd.
---

Protokoll utformat av Tadge Dryja för att komprimera Bitcoin-nodernas UTXO-uppsättning med hjälp av en ackumulator baserad på Merkle-träd. Till skillnad från den klassiska UTXO-uppsättningen som kräver betydande lagringsutrymme, minskar Utreexo drastiskt det minne som behövs genom att endast lagra Merkle Tree-rötterna. Detta gör att noden kan verifiera förekomsten av UTXO:er som används i transaktionsinmatningar utan att behöva behålla hela uppsättningen UTXO:er. Genom att använda Utreexo behåller varje nod endast ett kryptografiskt fingeravtryck som kallas Merkle Root. När en transaktion görs tillhandahåller användaren bevisen på Ownership för UTXO:erna och motsvarande Merkle-vägar. På så sätt kan noden verifiera transaktioner utan att lagra hela UTXO-uppsättningen. Låt oss ta ett exempel med ett diagram för att förstå denna mekanism:





I det här exemplet har jag avsiktligt reducerat UTXO-uppsättningen till 4 UTXO:er för att underlätta förståelsen. I verkligheten är det viktigt att föreställa sig att det finns nästan 140 miljoner UTXO:er på Bitcoin när dessa rader skrivs. I det här diagrammet skulle Utreexo-noden bara behöva hålla Merkle Root i RAM-minnet. Om den tar emot en transaktion som spenderar UTXO nr 3 (i svart), skulle beviset bestå av följande Elements:


- UTXO 3;
- Hash 4;
- Hash 1-2.


Med denna information som sänds av transaktionens avsändare utför Utreexo-noden följande kontroller:


- Den beräknar avtrycket av UTXO 3, vilket ger den Hash 3;
- Den sammanfogar Hash 3 med Hash 4;
- Den beräknar deras avtryck, vilket ger den Hash 3-4;
- Den sammanfogar Hash 3-4 med Hash 1-2;
- Den beräknar deras avtryck, vilket ger den Merkle Root.


Om den Merkle Root som erhålls genom processen är densamma som den Merkle Root som lagrats i RAM-minnet, är den övertygad om att UTXO nr 3 verkligen är en del av UTXO-uppsättningen.

Denna metod minskar RAM-kraven för Full node-operatörer. Utreexo har dock begränsningar, bland annat en ökning av blockstorleken på grund av ytterligare bevis och Utreexo-nodernas potentiella beroende av Bridge Nodes för att erhålla saknade bevis. Bridge Nodes är traditionella fulla noder som tillhandahåller de nödvändiga bevisen till Utreexo-noderna, vilket möjliggör fullständig verifiering. Detta tillvägagångssätt erbjuder en kompromiss mellan effektivitet och decentralisering, vilket gör transaktionsvalidering mer tillgänglig för användare med begränsade resurser.