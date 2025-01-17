---
term: (0XAC)

---
Tarkistaa allekirjoituksen pätevyyden tiettyä julkista avainta vastaan. Se ottaa pinosta kaksi ylintä elementtiä: allekirjoituksen ja julkisen avaimen, ja arvioi, onko allekirjoitus oikea tapahtuman hash:lle ja määritetylle julkiselle avaimelle. Jos tarkistus onnistuu, se siirtää pinoon arvon `1` (true), muuten `0` (false). Tätä op-koodia muutettiin Tapscriptissä Schnorr-allekirjoitusten tarkistamiseksi.