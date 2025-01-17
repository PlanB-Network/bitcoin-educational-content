---
term: (0X01)

---
SigHash-tyyppi Merkki, jota käytetään Bitcoin-tapahtuman allekirjoituksissa osoittamaan, että allekirjoitus koskee kaikkia tapahtuman osia. Käyttämällä `SIGHASH_ALL` allekirjoittaja kattaa kaikki tulot ja kaikki lähdöt. Tämä tarkoittaa, että syötteitä tai tuotoksia ei voi muuttaa allekirjoituksen jälkeen mitätöimättä sitä. Tämäntyyppinen SigHash Flag on yleisin Bitcoin-tapahtumissa, koska se varmistaa tapahtuman täydellisen lopullisuuden ja eheyden.