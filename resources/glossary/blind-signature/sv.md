---
term: Blind signatur
definition: Digital signatur där utfärdaren inte känner till det signerade innehållet, används i Chaumian CoinJoins och ecash.
---

Chaums blinda signaturer är en form av digital signatur där den som utfärdar signaturen inte känner till innehållet i det meddelande som signeras. Signaturen kan dock senare verifieras med det ursprungliga meddelandet. Denna teknik utvecklades av kryptografen David Chaum 1983.


Tänk på ett företag som vill autentisera ett konfidentiellt dokument, t.ex. en Contract, utan att avslöja dess innehåll. Företaget tillämpar en maskeringsprocess som kryptografiskt omvandlar originaldokumentet på ett reversibelt sätt. Det modifierade dokumentet skickas till en certifikatutfärdare som använder en blind signatur utan att känna till det underliggande innehållet. Efter att ha mottagit det maskerade signerade dokumentet avmaskerar företaget signaturen. Resultatet är ett originaldokument som autentiserats med myndighetens signatur, utan att myndigheten någonsin har sett originalinnehållet.


Chaums blinda signaturer gör det möjligt att certifiera ett dokuments äkthet utan att känna till dess innehåll, vilket garanterar både konfidentialiteten för användarens data och integriteten för det signerade dokumentet.


I Bitcoin används detta protokoll i system med chaumianska banker som en överlagring (Cashu, Fedimint etc.), men särskilt i chaumianska CoinJoin-protokoll, för att säkerställa att samordnaren inte kan koppla en inmatning till en utmatning.