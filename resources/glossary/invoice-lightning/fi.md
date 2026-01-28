---
term: Invoice lightning
definition: Lightning-maksupyyntö, joka sisältää kaikki rahansiirron suorittamiseen tarvittavat tiedot.
---

Vastaanottajan luoma salamamaksupyyntö, joka sisältää kaikki maksutapahtuman suorittamiseen tarvittavat tiedot.


Invoice Lightning sisältää maksun määränpään vastaanottavan solmun julkisen avaimen muodossa, mutta myös `LN`-etuliitteen, summan, voimassaoloajan, HTLC:ssä käytettävän salaisuuden Hash:n ja muita metatietoja, joista osa on valinnaisia, kuten reititysasetukset. Nämä laskut määritellään BOLT11-standardissa. Kun Invoice Lightning on maksettu, sitä ei voi käyttää uudelleen.


