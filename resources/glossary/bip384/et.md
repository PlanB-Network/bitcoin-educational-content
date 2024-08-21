---
term: BIP384
---

Tutvustab `combo(KEY)` funktsiooni kirjeldajate jaoks. See funktsioon kirjeldab võimalike väljundskriptide kogumit antud avaliku võtme jaoks. Seega hõlmab see korraga mitut tüüpi skripte, sealhulgas P2PK, P2PKH, P2WPKH ja P2SH-P2WPKH. Kui antud võti on kompresseeritud, testitakse kõiki 4 tüüpi skripte, ja kui see ei ole, testitakse ainult 2 Legacy skripti tüüpi. Eesmärk on lihtsustada võtmete esitamist kirjeldajates, pakkudes ühtset meetodit erinevate väljundskriptide variantide genereerimiseks sama avaliku võtme põhjal. BIP384 implementeeriti koos kõigi teiste kirjeldajatega seotud BIP-dega (välja arvatud BIP386) Bitcoin Core versioonis 0.17.