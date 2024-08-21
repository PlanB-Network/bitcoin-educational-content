---
termi: OP_CHECKSIG (0XAC)
---

Vahvistaa allekirjoituksen pätevyyden annettua julkista avainta vasten. Se ottaa pinon kaksi päällimmäistä elementtiä: allekirjoituksen ja julkisen avaimen, ja arvioi, onko allekirjoitus oikea transaktiohashille ja määritetylle julkiselle avaimelle. Jos vahvistus onnistuu, se työntää pinolle arvon `1` (tosi), muussa tapauksessa `0` (epätosi). Tämä operaatiokoodi muutettiin Tapscriptissä Schnorr-allekirjoitusten vahvistamiseen.