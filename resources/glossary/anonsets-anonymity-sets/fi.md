---
term: ANONSETS (NIMETTÖMYYSJOUKOT)

---
Anonyymit toimivat indikaattoreina, joiden avulla voidaan arvioida tietyn UTXO:n yksityisyystasoa. Tarkemmin sanottuna ne mittaavat erottamattomien UTXO:iden lukumäärää joukossa, joka sisältää tutkittavan kolikon. Koska tarvitaan joukko identtisiä UTXO:ita, anonsetit lasketaan yleensä kolikkojen yhdistämissyklin aikana. Niiden avulla voidaan tarvittaessa arvioida kolikoiden yhdistämisen laatua. Suuri anonset merkitsee suurempaa anonymiteettitasoa, koska tiettyä UTXO:ta on vaikea erottaa joukosta. On olemassa kahdenlaisia anonsetteja:


- Tuleva nimettömyysjoukko;
- Retrospektiivinen anonymiteettisarja.

Ensimmäinen osoittaa sen ryhmän koon, johon tutkittu UTXO on piilotettu, kun tiedetään, että UTXO on tulossa. Tämän indikaattorin avulla voidaan mitata kolikon yksityisyyden vastustuskykyä analyysia vastaan menneisyydestä nykyhetkeen (tulosta lähtöön). Englanniksi tämän indikaattorin nimi on "*forward anonset*" tai "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Toinen osoittaa tietyn kolikon mahdollisten lähteiden lukumäärän, kun tiedetään UTXO:n olevan ulostulossa. Tämän indikaattorin avulla voidaan mitata kolikon yksityisyyden vastustuskykyä analyysia vastaan nykyhetkestä menneisyyteen (ulostulosta tuloon). Englanniksi tämän indikaattorin nimi on "*backward anonset*" tai "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> ► *Ranskaksi on yleisesti hyväksytty termi "anonset" Se voitaisiin kuitenkin kääntää "ensemble d'anonymat" tai "potentiel d'anonymat" Sekä englanniksi että ranskaksi käytetään toisinaan myös termiä "score" viittaamaan anonsetiin (prospektiivinen score ja retrospektiivinen score).*