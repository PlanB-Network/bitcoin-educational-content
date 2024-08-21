---
termi: PSBT
---

Lyhenne sanoista "Partially Signed Bitcoin Transaction" (osittain allekirjoitettu Bitcoin-siirto). Kyseessä on BIP174:n myötä esitelty määrittely, jonka tarkoituksena on standardisoida tapa, jolla keskeneräiset siirrot rakennetaan Bitcoiniin liittyvässä ohjelmistossa, kuten lompakko-ohjelmistossa. PSBT kapseloi siirron, jonka syötteet eivät välttämättä ole täysin allekirjoitettuja. Se sisältää kaikki tarvittavat tiedot osallistujan siirron allekirjoittamiseksi ilman lisätietojen tarvetta. Näin ollen PSBT voi saada kolme erilaista muotoa:
* Täysin rakennettu siirto, mutta ei vielä allekirjoitettu;
* Osittain allekirjoitettu siirto, jossa jotkut syötteet on allekirjoitettu, kun taas toiset eivät vielä ole;
* Tai täysin allekirjoitettu Bitcoin-siirto, joka voidaan muuntaa lähetykseen valmiiksi verkossa.

PSBT-muoto helpottaa eri lompakko-ohjelmistojen ja allekirjoituslaitteiden (hardware wallet) välistä yhteentoimivuutta. Tällä hetkellä käytössä on PSBT:n versio 0, kuten BIP174:ssä määritellään, mutta versiota 2 ehdotetaan BIP370:n kautta.

> ► *PSBT:n versiota 1 ei ole olemassa. Koska versio 0 oli ensimmäinen versio, toista versiota alettiin epävirallisesti kutsua versioksi 2. Ava Chow, joka kirjoitti BIP370:n, päätti näin ollen antaa tälle uudelle versiolle numeron 2 välttääkseen sekaannuksia.*