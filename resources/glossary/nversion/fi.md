---
term: NVERSION

---
Bitcoin-tapahtuman `nVersion`-kenttää käytetään osoittamaan käytettävän tapahtumamuodon versio. Sen avulla verkko voi erottaa transaktiomuodon eri kehitysvaiheet ajan mittaan ja soveltaa vastaavia sääntöjä. Tällä kentällä ei ole vaikutusta konsensussääntöihin. Tämä tarkoittaa sitä, että mikä tahansa tälle kentälle annettu arvo ei johda transaktion mitätöintiin. Kentän `nVersion` standardointisäännöt hyväksyvät kuitenkin tällä hetkellä vain arvot `1` ja `2`. Toistaiseksi tämä kenttä on hyödyllinen vain `nSequence`-kentän aktivoinnissa.