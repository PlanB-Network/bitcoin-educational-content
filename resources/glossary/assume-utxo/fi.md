---
term: ASSUME UTXO

---
Johtavan Bitcoin Core -asiakasohjelman konfiguraatioparametri, jonka avulla solmu, joka on juuri alustettu (mutta ei ole vielä käynyt läpi IBD:tä), voi lykätä transaktioiden ja UTXO-asetuksen tarkistamista tiettyyn tilannekuvaan asti. Konsepti perustuu Core:n tarjoaman ja oletettavasti tarkan UTXO-setin (luettelo kaikista tiettynä ajankohtana olemassa olevista UTXO:ista) käyttöön, minkä ansiosta solmu voidaan synkronoida hyvin nopeasti sen ketjun kanssa, jossa on eniten kertynyttä työtä. Koska solmu ohittaa pitkällisen IBD-vaiheen, se on käyttäjänsä käytettävissä hyvin nopeasti. Oletetaan, että UTXO jakaa synkronoinnin (IBD) kahteen osaan:


- Ensin solmu suorittaa Header First Sync -toiminnon (vain otsikoiden tarkistus) ja pitää Ytimen toimittamaa UTXO-joukkoa voimassa olevana;
- Kun solmu on toimintakunnossa, se tarkistaa koko lohkon historian taustalla ja päivittää uuden UTXO-sarjan, jonka se on itse tarkistanut. Jos tämä uusi UTXO-sarja ei vastaa Coren toimittamaa, se antaa virheilmoituksen.

Siksi oletetaan, että UTXO nopeuttaa uuden Bitcoin-solmun valmistelua lykkäämällä transaktioiden verifiointiprosessia ja UTXO-asetusta Core-ohjelmassa olevan päivitetyn tilannekuvan kautta.