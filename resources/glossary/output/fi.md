---
term: OUTPUT

---
Bitcoinin yhteydessä transaktion tuotos tarkoittaa UTXO:ta (*Unspent Transaction Outputs*), joka luodaan maksun kohdevaroiksi. Tarkemmin sanottuna se on mekanismi, jolla transaktio jakaa varoja.

Transaktio ottaa UTXO:t eli bitcoinit syötteinä ja luo uusia UTXO:ita tuotoksina. Näissä tuotoksissa määritetään tietty määrä bitcoineja, jotka usein osoitetaan tiettyyn osoitteeseen, sekä ehdot, joilla nämä varat voidaan käyttää myöhemmin. Bitcoin-tapahtuman tehtävänä on siis kuluttaa UTXO:ita panoksina ja luoda uusia UTXO:ita tuotoksina. Näiden kahden erotus vastaa transaktiomaksuja, jotka lohkon voittanut louhija voi kerätä. UTXO on pohjimmiltaan edellisen transaktion tuotos, jota ei ole vielä käytetty. Transaktioiden tuotokset ovat siis uusien UTXO:iden luomista, joita puolestaan voidaan mahdollisesti käyttää tulevien transaktioiden panoksina.

Laajemmasta näkökulmasta laskentatoimessa termi "tuotos" viittaa yleensä funktiosta, algoritmista tai järjestelmästä saataviin tietoihin. Esimerkiksi kun tiedot ohjataan kryptografisen hash-funktion läpi, tätä tietoa kutsutaan "syötteeksi" ja tulosta "tulosteeksi"