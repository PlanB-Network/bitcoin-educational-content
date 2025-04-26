---
term: RAAKAKAUPPA

---
Bitcoin-tapahtuma, joka on rakennettu ja allekirjoitettu ja joka on olemassa binäärimuodossaan. Raaka transaktio (*raw TX*) on transaktion lopullinen esitys juuri ennen sen lähettämistä verkkoon. Tämä transaktio sisältää kaikki tarvittavat tiedot sen sisällyttämiseksi lohkoon:


- Versio;
- Lippu;
- Syötteet;
- Tuotokset;
- Lukitusaika;
- Todistaja.

Niin sanottu "*raakatransaktio*" edustaa raakadataa, joka ohjataan kahdesti SHA256-hajautusfunktion läpi transaktion TXID-tunnuksen luomiseksi. Näitä tietoja käytetään sitten lohkon Merkle-puussa transaktion integroimiseksi lohkoketjuun.

> ► *Tätä käsitettä kutsutaan joskus myös nimellä "Serialized Transaction". Ranskaksi nämä termit voitaisiin kääntää vastaavasti "transaction brute" ja "transaction sérialisée".*