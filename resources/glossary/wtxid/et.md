---
term: WTXID

---
Traditsioonilise TXID laiendus, mis sisaldab SegWitiga kasutusele võetud tunnistajate andmeid. Kui TXID on tehinguandmete, välja arvatud tunnistaja, hash, siis WTXID on kogu tehinguandmete, sealhulgas tunnistaja, "SHA256d". WTXID-d salvestatakse eraldi Merkle-puus, mille juur asub coinbase'i tehingus. Selline eraldamine võimaldab TXID-i tehingu muutlikkuse eemaldamist.