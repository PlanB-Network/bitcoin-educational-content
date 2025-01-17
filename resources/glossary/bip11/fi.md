---
term: BIP11

---
Gavin Andresenin maaliskuussa 2012 esittelemä BIP, jossa ehdotetaan standardimenetelmää moniäänisten Bitcoin-tapahtumien luomiseen. Ehdotuksen tarkoituksena on parantaa bitcoinien turvallisuutta vaatimalla useita allekirjoituksia tapahtuman vahvistamiseksi. BIP11 esittelee uudenlaisen käsikirjoitustyypin, joka on nimeltään "M-of-N multisig", jossa `M` edustaa allekirjoitusten vähimmäismäärää, joka vaaditaan `N` potentiaalisen julkisen avaimen joukosta. Tässä standardissa hyödynnetään op-koodia `OP_CHECKMULTISIG`, joka on jo olemassa Bitcoinissa, mutta joka ei aiemmin ollut solmujen standardointisääntöjen mukainen. Vaikka tämäntyyppistä skriptiä ei enää yleisesti käytetä varsinaisissa multisig-lompakoissa, vaan suositaan P2SH- tai P2WSH-lompakoita, sen käyttö on edelleen mahdollista. Sitä käytetään erityisesti metaprotokollissa, kuten Stampsissa. Solmut voivat kuitenkin päättää olla välittämättä näitä P2MS-tapahtumia parametrilla `permitbaremultisig=0`.

> ► *Nykyisin tämä standardi tunnetaan nimellä "bare-multisig" tai "P2MS".*