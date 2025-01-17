---
term: UTXO

---
Lyhenne sanoista *Unspent Transaction Output*. UTXO on transaktiotulos, jota ei ole vielä käytetty, eli sitä ei ole käytetty uuden transaktion syötteenä. UTXO:t edustavat sitä osaa bitcoineista, jonka käyttäjä omistaa ja joka on tällä hetkellä käytettävissä käytettäväksi. Kukin UTXO liittyy tiettyyn tulostusskriptiin (`scriptPubKey`), joka määrittelee bitcoinien käyttämiseen tarvittavat ehdot. Bitcoinin transaktiot kuluttavat näitä UTXO:ita syötteinä ja luovat uusia UTXO:ita tuotoksina. UTXO-malli on olennainen Bitcoinissa, sillä sen avulla voidaan helposti varmistaa, että transaktioilla ei yritetä käyttää bitcoineja, joita ei ole olemassa tai jotka on jo käytetty.