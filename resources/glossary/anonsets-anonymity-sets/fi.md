---
termi: ANONSETS (ANONYYMISET JOUKOT)
---

Anonsetit toimivat indikaattoreina arvioitaessa tietyn UTXO:n yksityisyyden tasoa. Tarkemmin sanottuna ne mittaavat erottamattomien UTXO:iden määrää joukossa, joka sisältää tutkittavan kolikon. Koska identtisten UTXO:iden ryhmä vaaditaan, anonsetit lasketaan yleensä kolikoiden yhdistämisen (coinjoin) syklin aikana. Ne mahdollistavat tarvittaessa kolikoiden yhdistämisen laadun arvioinnin. Suuri anonset tarkoittaa lisääntynyttä anonymiteetin tasoa, koska tietyn UTXO:n erottaminen joukosta muuttuu vaikeaksi. Anonseteja on kahta tyyppiä:
* Tuleva anonymiteettijoukko;
* Takautuva anonymiteettijoukko.

Ensimmäinen ilmaisee ryhmän koon, jonka seassa tutkittu UTXO piilotetaan, tietäen UTXO:n syötteenä. Tämä indikaattori mahdollistaa kolikon yksityisyyden vastustuskyvyn mittaamisen analyysissä menneisyydestä nykyhetkeen (syöte lähtöön). Englanniksi tämän indikaattorin nimi on “*forward anonset*,” tai “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

Toinen ilmaisee mahdollisten lähteiden määrän tietylle kolikolle, tietäen UTXO:n lähteenä. Tämä indikaattori mahdollistaa kolikon yksityisyyden vastustuskyvyn mittaamisen analyysissä nykyhetkestä menneisyyteen (lähtö syötteeseen). Englanniksi tämän indikaattorin nimi on “*backward anonset*,” tai “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *Ranskaksi yleisesti hyväksytään termi “anonset.” Sitä voitaisiin kuitenkin kääntää “ensemble d'anonymat” tai “potentiel d'anonymat.” Sekä englanniksi että ranskaksi termiä “score” käytetään joskus viittaamaan anonsetteihin (tuleva score ja takautuva score).*