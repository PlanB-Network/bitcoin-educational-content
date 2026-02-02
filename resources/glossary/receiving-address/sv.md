---
term: Mottagaradress
definition: Information som gör det möjligt att ta emot bitcoins, vanligtvis konstruerad från en hashad offentlig nyckel.
---

Information som används för att ta emot bitcoins. En Address konstrueras vanligtvis genom att hasha en offentlig nyckel med hjälp av `SHA256` och `RIMPEMD160` och lägga till metadata till denna sammanställning. De publika nycklar som används för att konstruera en mottagande Address är en del av användarens Wallet och härleds därför från deras seed. SegWit-adresser består t.ex. av följande information:


- En HRP för att beteckna "Bitcoin": `bc`;
- En separator: `1`;
- Den version av SegWit som användes: `q` eller `p`;
- Nyttolasten: sammanställningen av den offentliga nyckeln (eller direkt den offentliga nyckeln i fallet Taproot);
- Kontrollsumman: en BCH-kod.


En mottagande Address kan dock också representera något annat beroende på vilken skriptmodell som används. Till exempel konstrueras P2SH-adresser med hjälp av skriptets Hash. Taproot-adresser, å andra sidan, innehåller den tweakade publika nyckeln direkt utan att hasha den.


En mottagande Address kan representeras i form av en alfanumerisk sträng eller som en QR-kod. Varje Address kan användas flera gånger, men detta är något som starkt avråds från. För att upprätthålla en viss nivå av integritet rekommenderas att varje Bitcoin Address endast används en gång. En ny Address bör genereras för varje inkommande betalning till ens Wallet. En Address är kodad i `Bech32` för SegWit V0-adresser, i `Bech32m` för SegWit V1-adresser och i `Base58check` för Legacy-adresser. Ur teknisk synvinkel innebär mottagande av Bitcoin att man innehar den privata nyckeln som är associerad med en offentlig nyckel (och därmed en Address). När någon tar emot bitcoins uppdaterar avsändaren den befintliga begränsningen av deras utgifter så att endast mottagaren nu kan ha denna befogenhet.


