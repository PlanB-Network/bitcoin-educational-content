---
term: WTXID

---
Perinteisen TXID-tunnuksen laajennus, joka sisältää SegWitin myötä käyttöön otetut todistajatiedot. TXID on transaktiodatan hash-tunnus ilman todistajaa, kun taas WTXID on koko transaktiodatan, todistaja mukaan lukien, `SHA256d`. WTXID-tunnukset tallennetaan erilliseen Merkle-puuhun, jonka juuri sijaitsee coinbase-transaktiossa. Tämä erottelu mahdollistaa TXID:n transaktion muokattavuuden poistamisen.