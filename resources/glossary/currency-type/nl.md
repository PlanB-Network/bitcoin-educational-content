---
term: VALUTAAT TYPE
---

In de context van deterministische en hiërarchische (HD) wallets is het valutatype (*Coin type* in het Engels) een afleidingsniveau dat het mogelijk maakt om de vertakkingen van de Wallet te differentiëren op basis van de verschillende gebruikte cryptocurrencies. Deze Layer van afleiding, gedefinieerd door BIP 44, bevindt zich op diepte 2 van de afleidingsstructuur, na de hoofdsleutel en het doel. Bijvoorbeeld, voor Bitcoin is de toegewezen index `0x80000000`, genoteerd als `/0'/` in het derivatiepad. Dit betekent dat alle adressen en accounts die van dit pad zijn afgeleid, geassocieerd zijn met Bitcoin. Deze Layer afleiding maakt een duidelijke scheiding mogelijk van verschillende activa in een Wallet met meerdere valuta. Hier zijn de indexen die gebruikt worden voor verschillende cryptocurrencies:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...


![](../../dictionnaire/assets/21.webp)