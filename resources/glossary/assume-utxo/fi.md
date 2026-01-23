---
term: Assume utxo

definition: Bitcoin Core-parametri, joka mahdollistaa uuden solmun nopean synkronoinnin käyttämällä UTXO-joukon hetkenäistä, jonka oletetaan olevan pätevä, ennen historian tarkistamista taustalla.
---
Konfigurointiparametri Bitcoin Core -enemmistöasiakasohjelmassa, jonka avulla juuri alustettu solmu (joka ei ole vielä suorittanut IBD:tä) voi lykätä transaktioiden ja UTXO-joukon tarkistamista ennen tiettyä snapshotia. Konsepti perustuu Coren tarjoaman ja tarkkana pidetyn UTXO-joukon (luettelo kaikista tietyllä hetkellä olemassa olevista UTXO:ista) käyttöön, mikä mahdollistaa solmun synkronoinnin erittäin nopeasti ketjuun, jossa on eniten kertynyttä työtä. Koska solmu ohittaa pitkän IBD-vaiheen, se on erittäin nopeasti käyttäjän käytettävissä.

Assume UTXO jakaa synkronoinnin (IBD) kahteen osaan: Ensin solmu suorittaa Header First Syncin (vain otsikoiden tarkistus) ja pitää Coren sille tarjoamaa UTXO-joukkoa voimassa olevana; Sitten, kun se on toiminnassa, solmu tarkistaa koko lohkohistorian taustalla päivittäen uuden UTXO-joukon, jonka se on itse tarkistanut. Jos jälkimmäinen ei vastaa Coren tarjoamaa UTXO-joukkoa, se antaa virheilmoituksen.

Assume UTXO mahdollistaa siten uuden Bitcoin-solmun valmistelun nopeuttamisen lykkäämällä transaktioiden ja UTXO-joukon tarkistusprosessia Coressa tarjotun päivitetyn snapshotin ansiosta.





