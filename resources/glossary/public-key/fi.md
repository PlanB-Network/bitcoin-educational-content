---
term: PUBLIC KEY

---
Julkinen avain on epäsymmetrisessä salauksessa käytettävä elementti. Se luodaan yksityisestä avaimesta käyttämällä peruuttamatonta matemaattista funktiota. Bitcoinissa julkiset avaimet johdetaan niihin liittyvästä yksityisestä avaimesta elliptisen käyrän ECDSA- tai Schnorr-algoritmin digitaalisen allekirjoituksen avulla. Toisin kuin yksityistä avainta, julkista avainta voidaan jakaa vapaasti vaarantamatta varojen turvallisuutta. Bitcoin-protokollassa julkinen avain toimii perustana Bitcoin-osoitteen luomiselle, jota käytetään sitten UTXO:n käyttöehtojen luomiseen "scriptPubKey"-avaimen avulla. Julkiset avaimet sekoitetaan usein pääavaimeen tai laajennettuihin avaimiin (xpub...). Nämä elementit ovat kuitenkin aivan erilaisia.

> ► *Englanniksi julkinen avain on nimeltään "public key" Tämä termi lyhennetään toisinaan "pubkey" tai "PK"