---
term: Betalkanal
definition: Dubbelriktad anslutning mellan två Lightning-noder för bitcoin-utbyten utanför kedjan.
---

Inom ramen för Lightning Network är en betalningskanal en dubbelriktad anslutning mellan två Lightning-noder som möjliggör off-chain Bitcoin-utbyten. On-Chain, en betalningskanal representeras av en 2/2 multisignatur Address som innehas av båda deltagarna. Betalningskanalen kräver en On-Chain-transaktion för att öppnas och en annan för att stängas. Mellan dessa två händelser kan kanalanvändare utföra ett mycket stort antal off-chain Bitcoin-utbyten på Lightning Network, utan att On-Chain-aktivitet krävs. På Lightning är det möjligt att dirigera en betalning genom flera kanaler och noder, för att skicka bitcoins utan att nödvändigtvis öppna en direktkanal med mottagaren.