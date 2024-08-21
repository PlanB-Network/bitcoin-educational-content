---
termi: KONSOLIDAATIO
---

Erityinen tapahtuma, jossa useita pieniä UTXO:ita yhdistetään yhdeksi syötteeksi muodostamaan yksittäinen, suurempi UTXO tulosteena. Tämä toimenpide on tapahtuma, joka tehdään omaan lompakkoon. Konsolidaation tavoitteena on hyödyntää ajanjaksoja, jolloin Bitcoin-verkon maksut ovat matalia yhdistämällä useita pieniä UTXO:ita yhdeksi arvoltaan suuremmaksi. Näin se ennakoi pakollisia kuluja maksujen mahdollisesti noustessa, mahdollistaen säästöt tulevissa siirtomaksuissa.

Todellakin, tapahtumat, joissa on monta syötettä, ovat raskaampia ja siten kalliimpia. Siirtomaksujen säästämisen lisäksi konsolidaatio on myös pitkän aikavälin suunnittelun muoto. Jos lompakkosi sisältää hyvin pieniä UTXO:ita, nämä voivat muuttua käyttökelvottomiksi, jos Bitcoin-verkko on pitkään korkeiden maksujen ajanjaksossa. Esimerkiksi, jos sinun tarvitsee käyttää 10 000 satoshin UTXO:a, mutta minimilouhintamaksut ovat 15 000 satoshia, kulut ylittäisivät UTXO:n arvon. Nämä pienet UTXO:t muuttuvat taloudellisesti järjettömiksi käyttää ja pysyvät käyttökelvottomina niin kauan kuin maksut eivät laske. Näitä UTXO:ita kutsutaan yleisesti "pölyksi". Säännöllisesti konsolidoimalla pienet UTXO:si vähennät tätä maksujen nousuun liittyvää riskiä.

On kuitenkin tärkeää huomata, että konsolidaatiotapahtumat ovat tunnistettavissa ketjuanalyysissä. Tällainen tapahtuma osoittaa Common Input Ownership Heuristic (CIOH) -periaatteen, mikä tarkoittaa, että konsolidaatiotapahtuman syötteet kuuluvat yhdelle entiteetille. Tällä voi olla yksityisyyteen liittyviä seurauksia käyttäjälle.

![](../../dictionnaire/assets/7.png)