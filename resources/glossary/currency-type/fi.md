---
termi: VALUUTTATYYPPI
---

Determinististen ja hierarkkisten (HD) lompakoiden kontekstissa valuuttatyyppi (*coin type* englanniksi) on johdannaisuuden taso, joka mahdollistaa lompakon haarojen erottelun käytettyjen eri kryptovaluuttojen perusteella. Tämä johdannaisuuden kerros, joka on määritelty BIP 44:ssä, sijaitsee johdannaisrakenteen syvyydessä 2, seuraten pääavainta ja tarkoitusta. Esimerkiksi Bitcoinille määritetty indeksi on `0x80000000`, merkittynä johdannaispolussa muodossa `/0'/`. Tämä tarkoittaa, että kaikki tästä polusta johdetut osoitteet ja tilit liittyvät Bitcoiniin. Tämä johdannaisuuden kerros mahdollistaa eri varojen selkeän erottelun monivaluuttalompakossa. Tässä on indeksejä eri kryptovaluutoille:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)