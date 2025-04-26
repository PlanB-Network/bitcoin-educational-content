---
term: RECOVERY PHRASE

---
Palautuslause, jota kutsutaan joskus myös mnemoniseksi, siemenlauseeksi tai salaiseksi lauseeksi, on yleensä 12 tai 24 sanasta koostuva sekvenssi, joka luodaan pseudosattumanvaraisesti entropialähteestä. Pseudosattumanvaraista sekvenssiä täydennetään aina tarkistussummalla. Muistilauseen ja valinnaisen tunnuslauseen avulla johdetaan deterministisesti kaikki HD-lompakkoon (Hierarchical Deterministic) liittyvät avaimet. Tämä tarkoittaa, että tästä lauseesta on mahdollista luoda ja luoda uudelleen deterministisesti kaikki Bitcoin-lompakon yksityiset ja julkiset avaimet ja näin ollen päästä käsiksi siihen liittyviin varoihin. Palautuslauseen tarkoituksena on tarjota keino bitcoinien varmuuskopiointiin ja palautukseen, joka on sekä turvallinen että helppokäyttöinen.

On tärkeää säilyttää tämä lauseke turvallisessa ja varmassa paikassa, sillä kuka tahansa, jolla on muistisana hallussaan, pääsee käsiksi vastaavan lompakon varoihin. Jos sitä käytetään perinteisen lompakon yhteydessä ja ilman valinnaista salasanaa, se muodostaa usein SPOF:n (Single Point Of Failure). Palautuslauseke on siis pseudosattuman ja tarkistussumman koodaus arkipäiväisiksi sanoiksi, jotta sen merkitseminen ja luettavuus olisi helpompaa ihmisille. Se rakennetaan BIP39-standardin mukaisesti, jossa määritellään ja määrätään 2048 sanan luettelo, jota käytetään tähän koodaukseen.

> ► *BIP39:n 2048 sanan luettelo on saatavilla useilla kielillä, mutta on suositeltavaa käyttää vain englanninkielistä versiota, koska se on lompakko-ohjelmiston laajimmin tukema versio.*