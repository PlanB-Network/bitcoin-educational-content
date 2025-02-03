---
term: VALUUTTATYYPPI

---
Determinististen ja hierarkkisten (HD) lompakoiden yhteydessä valuuttatyyppi (englanniksi *coin type*) on johdannaiserittelyn taso, jonka avulla lompakon haarat voidaan erottaa toisistaan käytettyjen kryptovaluuttojen perusteella. Tämä BIP 44:n määrittelemä johdannaiskerros sijaitsee johdannaisrakenteen syvyydessä 2, pääavaimen ja tarkoituksen jälkeen. Esimerkiksi Bitcoinille annettu indeksi on `0x80000000`, joka on merkitty `/0'/` derivointipolkuun. Tämä tarkoittaa, että kaikki tästä polusta johdetut osoitteet ja tilit liittyvät Bitcoiniin. Tämä johdannaiskerros mahdollistaa eri omaisuuserien selkeän erottelun usean valuutan lompakossa. Seuraavassa on eri kryptovaluuttojen indeksit:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)