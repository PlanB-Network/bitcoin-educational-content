---
termi: RAHAKAUPPA
---

Bitcoin-siirto, joka on rakennettu ja allekirjoitettu, olemassa sen binäärimuodossa. Raaka siirto (*raw TX*) on siirron lopullinen esitysmuoto juuri ennen sen lähettämistä verkossa. Tämä siirto sisältää kaikki tarvittavat tiedot sen sisällyttämiseksi lohkoon:
* Versio;
* Lippu;
* Syötteet;
* Tulosteet;
* Lukkoaika;
* Todistaja.

Mitä tarkoitetaan "*raaka siirrolla*" edustaa raakadataa, joka läpäisee SHA256-hajautusfunktion kahdesti siirron TXID:n luomiseksi. Nämä tiedot käytetään sitten lohkon Merkle-puussa integroimaan siirto lohkoketjuun.

> ► *Tätä konseptia kutsutaan joskus myös "Sarjallistetuksi Siirroksi". Ranskaksi nämä termit voidaan vastaavasti kääntää "transaction brute" ja "transaction sérialisée".*