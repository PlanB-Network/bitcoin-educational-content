---
termi: P2MS
---

P2MS tarkoittaa *Pay to Multisig*, suomeksi "maksa useammalle allekirjoitukselle". Se on standardi skriptimalli, jota käytetään määrittämään kulutusehdot UTXO:lle. Se mahdollistaa bitcoinien lukitsemisen useilla julkisilla avaimilla. Näiden bitcoinien käyttämiseen vaaditaan allekirjoitus, joka on yhdistetty ennalta määrättyyn määrään yksityisiä avaimia. Esimerkiksi `P2MS 2/3` sisältää `3` julkista avainta, joilla on `3` niihin liittyvää salattua yksityistä avainta. Bitcoinien käyttämiseksi, jotka on lukittu tällä P2MS-skriptillä, tarvitaan allekirjoitus vähintään `2`lla `3`sta yksityisestä avaimesta. Tämä on kynnysarvon turvajärjestelmä.

Tämän skriptin keksi Gavin Andresen vuonna 2011, kun hän otti vastuun Bitcoinin pääasiakasohjelman ylläpidosta. Nykyään P2MS:tä käytetään vain marginaalisesti joissakin sovelluksissa. Suurin osa nykyaikaisista moniallekirjoituksista käyttää muita skriptejä, kuten P2SH tai P2WSH. Näihin verrattuna P2MS on äärimmäisen triviaali. Siinä olevat julkiset avaimet paljastetaan vastaanotettaessa transaktio. P2MS:n käyttö on myös kalliimpaa kuin muiden moniallekirjoitusskriptien.

> ► *P2MS:ää kutsutaan usein "bare-multisigiksi", joka voitaisiin kääntää "alaston moniallekirjoitus" tai "raaka moniallekirjoitus". Vuoden 2023 alussa P2MS-skriptit olivat kiistan keskiössä niiden väärinkäytön vuoksi Stamps-protokollassa. Niiden vaikutus UTXO-joukkoon huomautettiin erityisesti.*