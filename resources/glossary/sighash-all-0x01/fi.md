---
termi: SIGHASH_ALL (0X01)
---

SigHash-lipun tyyppi, jota käytetään Bitcoin-siirtojen allekirjoituksissa osoittamaan, että allekirjoitus kattaa kaikki siirron osat. Käyttämällä `SIGHASH_ALL`, allekirjoittaja kattaa kaikki sisääntulot ja kaikki ulostulot. Tämä tarkoittaa, että kumpiakaan sisääntuloja tai ulostuloja ei voida muuttaa allekirjoituksen jälkeen ilman, että se mitätöi sen. Tämä SigHash-lipun tyyppi on yleisin Bitcoin-siirroissa, koska se takaa siirron täydellisen päättäväisyyden ja eheyden.