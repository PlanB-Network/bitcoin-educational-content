---
term: POSTIMERKIT

---
Protokolla, joka mahdollistaa muotoillun kuvatiedon integroinnin suoraan Bitcoin-lohkoketjuun raakojen moniäänisten allekirjoitustapahtumien (P2MS) avulla. Stamps koodaa kuvan binäärisisällön 64-alkuisena ja lisää sen 1/3 P2MS:n avaimiin. Yksi avain on todellinen ja sitä käytetään varojen käyttämiseen, kun taas kaksi muuta ovat valeavaimia (niihin liittyvä yksityinen avain on tuntematon), jotka tallentavat tiedot. Koska tiedot koodataan suoraan julkisiksi avaimiksi sen sijaan, että käytettäisiin `OP_RETURN`-ulostuloja, Stamps-protokollalla tallennetut kuvat ovat erityisen työläitä solmuille. Tällä menetelmällä luodaan erityisesti useita UTXO:ita, mikä kasvattaa UTXO-joukon kokoa ja aiheuttaa ongelmia täysille solmuille.