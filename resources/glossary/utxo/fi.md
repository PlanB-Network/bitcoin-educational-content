---
termi: UTXO
---

Lyhenne sanoista *Käyttämätön Transaktio-Output*. UTXO on transaktion output, jota ei ole vielä käytetty, mikä tarkoittaa, että sitä ei ole käytetty uuden transaktion syötteenä. UTXO:t edustavat bitcoineja, jotka käyttäjä omistaa ja jotka ovat tällä hetkellä käytettävissä. Jokaiseen UTXO:on liittyy tietty output-skripti (`scriptPubKey`), joka määrittelee tarvittavat ehdot bitcoinien käyttämiseksi. Bitcoin-transaktiot kuluttavat näitä UTXO:ja syötteinä ja luovat uusia UTXO:ja outputteina. UTXO-malli on olennainen osa Bitcoinia, sillä se mahdollistaa transaktioiden helpon varmistamisen siinä mielessä, ettei yritetä käyttää bitcoineja, joita ei ole olemassa tai jotka on jo käytetty.