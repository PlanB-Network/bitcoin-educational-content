---
termi: STAMPS
---

Protokolla, joka mahdollistaa muotoillun kuvadatan suoran integroinnin Bitcoin-lohkoketjuun käyttäen raakoja moniallekirjoitustapahtumia (P2MS). Stamps koodaa kuvan binäärisisällön base 64 -muotoon ja lisää sen 1/3 P2MS:n avaimiin. Yksi avain on aito ja sitä käytetään varojen käyttämiseen, kun taas kaksi muuta ovat valeavaimia (joiden yhdistetty yksityisavain on tuntematon), jotka varastoivat dataa. Koodaamalla data suoraan julkisiksi avaimiksi sen sijaan, että käytettäisiin `OP_RETURN`-tulosteita, Stamps-protokollalla tallennetut kuvat ovat erityisen työläitä solmuille. Tämä menetelmä luo huomattavasti useita UTXO:ja, mikä kasvattaa UTXO-joukon kokoa ja aiheuttaa ongelmia täysille solmuille.