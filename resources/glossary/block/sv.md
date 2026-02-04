---
term: Block
definition: Datastruktur som innehåller validerade transaktioner och metadata, länkad till andra block genom hashning.
---

Datastruktur i Bitcoin-systemet. Ett block innehåller en uppsättning giltiga transaktioner och metadata som finns i dess rubrik. Varje block är länkat till nästa genom Hash i dess rubrik, vilket bildar Blockchain. Blockchain fungerar som en tidsstämplingsserver som gör det möjligt för varje användare att känna till alla tidigare transaktioner, för att verifiera att en transaktion inte existerar och förhindra dubbla utgifter. Transaktionerna är organiserade i en Merkle Tree. Denna kryptografiska ackumulator gör det möjligt att producera en sammanställning av alla transaktioner i ett block, kallat "Merkle Root" Rubriken för ett block innehåller 6 Elements:


- Versionen av blocket;
- Avtrycket från det föregående blocket;
- Roten till Merkle Tree av transaktioner;
- Timestamp i kvarteret;
- Svårighetsmålet;
- Nonce.


För att ett block ska vara giltigt måste det ha ett huvud som, när det har hashats med `SHA256d`, ger ett sammandrag som är mindre än eller lika med svårighetsmålet.