---
term: BIP0141

definition: SegWitin (Segregated Witness) esittely, joka erottaa allekirjoitukset muusta tapahtumasta muokattavuuden (malleability) ratkaisemiseksi.
---
Esitteli SegWit (Segregated Witness) -konseptin, joka antoi nimensä SegWit soft forkille. BIP141 esittelee merkittävän muutoksen Bitcoin-protokollaan, jonka tarkoituksena on ratkaista transaktioiden väärennettävyysongelma. SegWit erottaa todistajan (allekirjoitustiedot) muusta transaktiotiedosta. Tämä erottelu saavutetaan lisäämällä todistajat erilliseen tietorakenteeseen, joka on sitoutunut uuteen Merkle-puuhun, johon itse viitataan lohkossa coinbase-transaktion kautta, mikä tekee SegWitistä yhteensopivan protokollan vanhempien versioiden kanssa.