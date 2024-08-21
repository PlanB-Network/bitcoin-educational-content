---
termi: JULKINEN AVAIN
---

Julkisen avaimen on elementti, jota käytetään asymmetrisessa kryptografiassa. Se luodaan yksityisestä avaimesta käyttäen peruuttamatonta matemaattista funktiota. Bitcoinissa julkiset avaimet johdetaan niihin liittyvästä yksityisestä avaimesta digitaalisen allekirjoituksen algoritmien, kuten elliptisen käyrän ECDSA:n tai Schnorrin, kautta. Toisin kuin yksityinen avain, julkinen avain voidaan jakaa vapaasti ilman, että varojen turvallisuus vaarantuu. Bitcoin-protokollassa julkinen avain toimii perustana Bitcoin-osoitteen luomiselle, jota sitten käytetään kulutusehtojen luomiseen UTXO:ssa käyttäen `scriptPubKey`-skriptiä. Julkisia avaimia sekoitetaan usein pääavaimen tai laajennettujen avainten (xpub...) kanssa. Kuitenkin nämä elementit ovat hyvin erilaisia.

> ► *Englanniksi julkinen avain kutsutaan "public key." Tätä termiä lyhennetään joskus muotoon "pubkey" tai "PK."*