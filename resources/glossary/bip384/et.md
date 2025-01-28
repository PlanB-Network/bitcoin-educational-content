---
term: BIP384

---
Võtab kasutusele funktsiooni `combo(KEY)` deskriptorite jaoks. See funktsioon kirjeldab antud avaliku võtme jaoks võimalike väljundskriptide kogumit. Seega hõlmab see korraga mitut tüüpi skripte, sealhulgas P2PK, P2PKH, P2WPKH ja P2SH-P2WPKH. Kui antud võti on tihendatud, testitakse kõiki 4 tüüpi skripte, kui aga mitte, siis testitakse ainult 2 Legacy skriptitüüpi. Eesmärgiks on lihtsustada võtmete esitamist kirjeldustes, pakkudes ühte meetodit sama avaliku võtme alusel erinevate väljundskriptide variantide genereerimiseks. BIP384 rakendati koos kõigi teiste deskriptoritega seotud BIP-dega (välja arvatud BIP386) Bitcoin Core'i versioonis 0.17.