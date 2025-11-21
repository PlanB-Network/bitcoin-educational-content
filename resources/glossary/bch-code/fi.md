---
term: BCH-KOODI
---

Virheenkorjauskoodien luokka, jota käytetään havaitsemaan ja korjaamaan virheitä datasekvenssissä. Toisin sanoen BCH-virheenkorjauskoodeja käytetään löytämään ja korjaamaan satunnaisia virheitä lähetetyssä tiedossa, jotta varmistetaan, että tieto saapuu ehjänä perille. Lyhenne "BCH" on näiden koodien keksijöiden nimien alkukirjaimet: Bose, Ray-Chaudhuri ja Hocquenghem.


Tätä työkalua käytetään monilla tietotekniikan aloilla, kuten SSD-levyillä, DVD-levyillä ja QR-koodeilla. Esimerkiksi näiden virheenkorjauskoodien ansiosta QR-koodin sisältämä tieto voidaan hakea, vaikka se olisi osittain peittynyt.


Bitcoin:n osana BCH-koodeja käytetään tarkistussummana Bech32- ja Bech32m (SegWit:n jälkeisissä) Address-formaateissa. Ne ovat parempi kompromissi tarkistussumman koon ja virheentunnistuskyvyn välillä kuin aiemmin Legacy-osoitteissa käytetyt yksinkertaiset Hash-toiminnot. Bitcoin:n yhteydessä BCH-koodeja käytetään vain virheiden havaitsemiseen, ei virheenkorjaukseen. Näin ollen Bitcoin-salkkuohjelmisto tunnistaa ja ilmoittaa käyttäjälle kaikki vastaanottavassa Address:ssa olevat virheet, mutta ei vaihda virheellistä Address:ta automaattisesti. Tämä valinta perustuu siihen, että virheenkorjauksen integrointi vaikuttaa väistämättä algoritmin virheentunnistusvalmiuksiin.