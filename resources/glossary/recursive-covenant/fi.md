---
term: REKURSIIVINEN (LIITTO)

---
Bitcoinin rekursiivinen sopimus on eräänlainen älykäs sopimus, joka asettaa ehtoja nykyisen transaktion lisäksi myös tuleville transaktioille, jotka käyttävät tämän transaktion tuotoksia. Näin voidaan luoda transaktioketjuja, joissa jokaisen on noudatettava tiettyjä sääntöjä, jotka ketjun ensimmäinen osapuoli on määritellyt. Rekursiivisuus luo transaktioiden sarjan, jossa kukin perii vanhemman transaktionsa rajoitukset. Tämä mahdollistaisi monimutkaisen ja pitkäaikaisen kontrollin siitä, miten bitcoineja voidaan käyttää, mutta se toisi myös riskejä, jotka liittyvät kulutusvapauteen ja korvattavuuteen.

Yhteenvetona voidaan todeta, että ei-rekursiivinen kovenantti rajoittaisi itsensä vain siihen transaktioon, joka seuraa välittömästi sääntöä vahvistavaa transaktiota. Sitä vastoin rekursiivinen sopimus voi asettaa bitcoinille tiettyjä ehtoja loputtomiin. Transaktiot voivat seurata toisiaan, mutta kyseinen bitcoin säilyttää aina siihen alun perin liitetyt ehdot. Teknisesti ottaen ei-rekursiivinen sopimus syntyy, kun UTXO:n `scriptPubKey` määrittelee rajoituksia UTXO:ta käyttävän transaktion tuotosten `scriptPubKey`:lle. Toisaalta rekursiivinen sopimus syntyy, kun UTXO:n `scriptPubKey` määrittelee rajoituksia kyseisen UTXO:n käyttävän transaktion tuotosten `scriptPubKey`:lle ja kaikille UTXO:n käyttämistä seuraaville `scriptPubKey`:ille.

Yleisemmin tietojenkäsittelyssä "rekursiivisuudella" tarkoitetaan funktion kykyä kutsua itseään, jolloin syntyy eräänlainen silmukka.