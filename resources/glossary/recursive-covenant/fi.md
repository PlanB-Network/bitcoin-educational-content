---
termi: REKURSIIVINEN (SOPIMUS)
---

Bitcoinissa rekursiivinen sopimus on älykkään sopimuksen tyyppi, joka asettaa ehtoja ei vain nykyiselle transaktiolle, mutta myös tuleville transaktioille, jotka käyttävät tämän transaktion tuotoksia. Tämä mahdollistaa transaktioketjujen luomisen, joissa jokaisen on noudatettava tiettyjä sääntöjä, jotka määrittelee ketjun ensimmäinen transaktio. Rekursiivisuus luo transaktiosekvenssin, jossa jokainen perii rajoitukset vanhemmalta transaktioltaan. Tämä mahdollistaisi monimutkaisten ja pitkäaikaisten kontrollimekanismien luomisen sille, miten bitcoineja voidaan käyttää, mutta se toisi mukanaan myös riskejä liittyen käyttövapauden ja vaihdettavuuden suhteen.

Yhteenvetona, ei-rekursiivinen sopimus rajoittaisi itsensä vain välittömästi seuraavaan transaktioon, joka perustaa säännöt. Toisaalta rekursiivinen sopimus kykenee asettamaan tiettyjä ehtoja bitcoinille määrittelemättömän ajan. Transaktiot voivat seurata toisiaan, mutta kyseessä oleva bitcoin säilyttää aina siihen liitetyt alkuperäiset ehdot. Teknisesti ei-rekursiivisen sopimuksen perustaminen tapahtuu, kun UTXO:n `scriptPubKey` määrittelee rajoituksia transaktion tuotosten `scriptPubKey`lle, joka käyttää kyseistä UTXO:a. Toisaalta rekursiivisen sopimuksen perustaminen tapahtuu, kun UTXO:n `scriptPubKey` määrittelee rajoituksia transaktion tuotosten `scriptPubKey`lle, joka käyttää kyseistä UTXO:a, ja kaikille `scriptPubKey`lle, jotka seuraavat tämän UTXO:n käyttöä.

Yleisemmin tietotekniikassa "rekursiivisuus" tarkoittaa funktion kykyä kutsua itseään, luoden eräänlaisen silmukan.