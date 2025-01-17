---
term: MERKLE ROOT

---
Merkle-puun pääte tai "top hash", joka edustaa yhteenvetoa kaikesta puun sisältämästä tiedosta. Merkle-puu on kryptografinen akkumulaattorirakenne, jota kutsutaan joskus myös "hash-puuksi". Bitcoinin yhteydessä Merkle-puita käytetään järjestämään transaktioita lohkon sisällä ja helpottamaan tietyn transaktion sisältymisen nopeaa tarkistamista. Bitcoin-lohkoissa Merkle-juureen päädytään siten siten, että transaktiot hakataan pareittain peräkkäin, kunnes jäljelle jää vain yksi hash (Merkle-juureen). Tämä sisällytetään sitten vastaavan lohkon otsikkoon. Tämä hash-puu löytyy myös UTREEXO-rakenteesta, joka mahdollistaa UTXO-solmujen joukon tiivistämisen, ja MAST Taproot -rakenteesta.