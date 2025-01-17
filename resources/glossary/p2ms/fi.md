---
term: P2MS

---
P2MS on lyhenne sanoista *Pay to Multisig*, joka tarkoittaa "maksa useista allekirjoituksista". Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. Se mahdollistaa bitcoinien lukitsemisen useilla julkisilla avaimilla. Näiden bitcoinien käyttäminen edellyttää allekirjoitusta, johon liittyy ennalta määritelty määrä yksityisiä avaimia. Esimerkiksi `P2MS 2/3` sisältää `3` julkista avainta ja `3` siihen liittyvää salaista yksityistä avainta. Tämän P2MS-skriptin avulla lukittujen bitcoinien käyttämiseen tarvitaan allekirjoitus, jossa on vähintään `2` yksityisistä avaimista `3`. Tämä on kynnysturvajärjestelmä.

Tämän skriptin keksi Gavin Andresen vuonna 2011, kun hän otti hoitaakseen Bitcoinin pääasiakasohjelman ylläpidon. Nykyään P2MS:ää käytetään vain marginaalisesti joissakin sovelluksissa. Valtaosa nykyaikaisista multisignatureista käyttää muita skriptejä, kuten P2SH:ta tai P2WSH:ta. Näihin verrattuna P2MS on äärimmäisen triviaali. Sen muodostamat julkiset avaimet paljastetaan transaktion vastaanottamisen yhteydessä. P2MS:n käyttäminen on myös kalliimpaa kuin muiden monialakirjoitusskriptien.

> ► *P2MS:ää kutsutaan usein nimellä "bare-multisig", joka voidaan kääntää "naked multisignature" tai "raw multisignature". Vuoden 2023 alussa P2MS-skriptit olivat kiistan keskipisteessä, koska niitä käytettiin väärin Stamps-protokollassa. Niiden vaikutus UTXO-joukkoon tuotiin erityisesti esiin.*