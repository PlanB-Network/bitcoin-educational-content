---
term: LOMPAKON JALANJÄLKI

---
Joukko erityispiirteitä, jotka ovat havaittavissa saman Bitcoin-lompakon tekemissä transaktioissa. Näihin ominaisuuksiin voi kuulua samankaltaisuuksia skriptityyppien käytössä, osoitteiden uudelleenkäytössä, UTXO:iden järjestyksessä, muutostulosten sijoittelussa, RBF:n (*Replace-by-Fee*) signaloinnissa, versionumerossa, `nSequence`-kentässä ja `nLockTime`-kentässä.

Analyytikot käyttävät lompakkojälkiä jäljittääkseen tietyn yksikön toimintaa lohkoketjussa tunnistamalla sen transaktioissa toistuvia malleja. Esimerkiksi käyttäjä, joka järjestelmällisesti lähettää vaihtorahansa P2TR-osoitteisiin (`bc1p...`), luo tunnusomaisen jalanjäljen, jonka avulla voidaan seurata hänen tulevia tapahtumiaan.

Kuten LaurentMT selittää Space Kek #19:ssä (ranskankielinen podcast), lompakkojalanjäljen hyödyllisyys ketjuanalyysissä kasvaa merkittävästi ajan myötä. Skriptityyppien kasvava määrä ja lompakko-ohjelmistojen yhä asteittaisempi uusien ominaisuuksien käyttöönotto korostavat nimittäin eroja. On jopa mahdollista tunnistaa tarkasti jäljitetyn yksikön käyttämä ohjelmisto. Siksi on tärkeää ymmärtää, että lompakon jalanjäljen tutkiminen on erityisen merkityksellistä viimeaikaisten transaktioiden osalta, enemmän kuin 2010-luvun alussa aloitettujen transaktioiden osalta.