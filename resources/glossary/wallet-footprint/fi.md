---
termi: LOMPAKON JÄLKI
---

Joukko erottuvia ominaisuuksia, jotka ovat havaittavissa saman Bitcoin-lompakon tekemissä transaktioissa. Näihin ominaisuuksiin voi kuulua yhtäläisyyksiä skriptityyppien käytössä, osoitteiden uudelleenkäytössä, UTXOjen järjestyksessä, vaihtorahojen sijoittelussa, RBF:n (*Replace-by-Fee*, korvaa maksulla) merkinnässä, versionumerossa, `nSequence`-kentässä ja `nLockTime`-kentässä.

Lompakon jälkiä käytetään analyytikkojen toimesta seuraamaan tietyn entiteetin toimintaa lohkoketjussa tunnistamalla toistuvia kaavoja sen transaktioissa. Esimerkiksi käyttäjä, joka järjestelmällisesti lähettää vaihtorahansa P2TR-osoitteisiin (`bc1p…`), luo erottuvan jäljen, jota voidaan käyttää hänen tulevien transaktioidensa seuraamiseen.

Kuten LaurentMT selittää Space Kek #19:ssä (ranskankielinen podcast), lompakon jälkien hyödyllisyys ketjuanalyysissä kasvaa merkittävästi ajan myötä. Todellakin, skriptityyppien kasvava määrä ja näiden uusien ominaisuuksien asteittainen käyttöönotto lompakko-ohjelmistojen toimesta korostaa eroja. On jopa mahdollista tarkasti tunnistaa jäljitettävän entiteetin käyttämä ohjelmisto. Siksi on tärkeää ymmärtää, että lompakon jäljen tutkiminen on erityisen relevanttia viimeaikaisten transaktioiden osalta, vielä enemmän kuin niiden, jotka on aloitettu 2010-luvun alussa.