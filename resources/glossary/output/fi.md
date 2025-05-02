---
term: OUTPUT
---

Bitcoin:n yhteydessä tapahtuman tuotos tarkoittaa _Unspent Transaction Outputs_ (UTXOs), jotka luodaan maksun kohdevaroiksi. Tarkemmin sanottuna se on mekanismi, jolla transaktio jakaa varoja. Transaktio ottaa UTXO:t eli bitcoin-bitit "syötteinä" ja luo uusia UTXO:ita "tuotoksina". Näissä tuotoksissa määrätään tietty määrä bitcoineja, jotka usein osoitetaan tietylle Address:lle, sekä ehdot, joiden mukaisesti nämä varat voidaan käyttää myöhemmin.


Bitcoin-transaktion tehtävänä on näin ollen kuluttaa UTXO:ita syötteinä ja luoda uusia UTXO:ita tuotoksina. Näiden kahden erotus vastaa transaktiomaksuja, jotka lohkon voittanut Miner voi periä takaisin. UTXO on pohjimmiltaan edellisen transaktion tuotos, jota ei ole vielä käytetty. Transaktioiden tuotokset ovat siis uusien UTXO:iden luomista, joita puolestaan mahdollisesti käytetään tulevien transaktioiden panoksina.


Laajemmasta näkökulmasta katsottuna termi "tuotos" viittaa tietotekniikassa yleensä funktion, algoritmin tai järjestelmän tuloksena syntyvään dataan. Esimerkiksi kun tietoja johdetaan salausfunktio Hash:n läpi, näitä tietoja kutsutaan "syötteeksi" ja tulosta "tulosteeksi".