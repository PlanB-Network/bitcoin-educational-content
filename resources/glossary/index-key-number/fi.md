---
term: INDEX (AVAINNUMERO)
---

HD-lompakon kontekstissa se viittaa peräkkäiseen numeroon, joka on määritetty lapsiavaimelle, joka on luotu vanhemmasta avaimesta. Tätä indeksiä käytetään yhdessä vanhemman avaimen ja vanhemman ketjukoodin kanssa deterministisesti johdettujen uniikkien lapsiavainten luomiseen. Se mahdollistaa rakenteellisen järjestämisen ja useiden sisaruslapsiavainparien toistettavan tuottamisen samasta vanhemmasta avaimesta. Se on 32-bittinen kokonaisluku, jota käytetään `HMAC-SHA512` johdannaisfunktiossa. Tämä numero siis erottaa sisaruslapsiavaimet toisistaan HD-lompakossa.