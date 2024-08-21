---
termi: BIP11
---

BIP, jonka Gavin Andresen esitteli maaliskuussa 2012, ehdottaa standardimenetelmää multisignatuurisiin (moniallekirjoitus) transaktioihin Bitcoinissa. Tämän ehdotuksen tavoitteena on parantaa bitcoinien turvallisuutta vaatimalla useita allekirjoituksia transaktion vahvistamiseksi. BIP11 esittelee uuden tyyppisen skriptin, nimeltään "M-of-N multisig", missä `M` edustaa vähimmäismäärää vaadittavia allekirjoituksia `N` mahdollisesta julkisesta avaimesta. Tämä standardi hyödyntää `OP_CHECKMULTISIG`-operaatiokoodia, joka on jo olemassa Bitcoinissa, mutta joka ei aiemmin ollut yhteensopiva solmujen standardisointisääntöjen kanssa. Vaikka tätä skriptityyppiä ei enää yleisesti käytetä varsinaisissa multisig-lompakoissa, suosien P2SH tai P2WSH:ta, sen käyttö on edelleen mahdollista. Sitä käytetään erityisesti meta-protokollissa, kuten Stamps. Solmut voivat kuitenkin valita olla välittämättä näitä P2MS-transaktioita parametrilla `permitbaremultisig=0`.

> ► *Nykyään tätä standardia kutsutaan "bare-multisigiksi" tai "P2MS":ksi.*