---
term: UTREEXO

---
Tadge Dryjan suunnittelema protokolla Bitcoin-solmujen UTXO-joukon tiivistämiseksi käyttämällä Merkle-puihin perustuvaa akkumulaattoria. Toisin kuin klassinen UTXO-joukko, joka vaatii huomattavaa tallennustilaa, Utreexo vähentää huomattavasti muistin tarvetta tallentamalla vain Merkle-puiden juuret. Näin solmu voi tarkistaa tapahtumien syötteissä käytettyjen UTXO:iden olemassaolon ilman, että sen tarvitsee säilyttää koko UTXO-joukkoa. Utreexoa käyttämällä kukin solmu säilyttää vain kryptografisen sormenjäljen, jota kutsutaan Merkle-juureksi. Kun transaktio tehdään, käyttäjä toimittaa UTXO:iden ja niitä vastaavien Merkle-polkujen omistustodistukset. Näin solmu voi todentaa transaktiot tallentamatta koko UTXO-joukkoa. Otetaanpa esimerkki kaavion avulla tämän mekanismin ymmärtämiseksi:

![](../../dictionnaire/assets/15.webp)

Tässä esimerkissä supistin UTXO-joukon tarkoituksella neljään UTXO:hon ymmärtämisen helpottamiseksi. Todellisuudessa on tärkeää kuvitella, että näitä rivejä kirjoitettaessa Bitcoinissa on lähes 140 miljoonaa UTXOa. Tässä kaaviossa Utreexo-solmun tarvitsisi pitää RAM-muistissa vain Merkle-juurta. Jos se vastaanottaa transaktion, joka kuluttaa UTXO nro 3 (mustalla), todiste koostuisi seuraavista elementeistä:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Näiden tapahtuman lähettäjän toimittamien tietojen perusteella Utreexo-solmu suorittaa seuraavat tarkistukset:


- Se laskee UTXO 3:n jäljen, joka antaa sille HASH 3:n;
- Se yhdistää HASH 3 ja HASH 4;
- Se laskee niiden jäljen, joka antaa sille HASH 3-4;
- Se yhdistää HASH 3-4 ja HASH 1-2;
- Se laskee niiden jäljen, joka antaa sille Merkle-juuren.

Jos sen prosessin kautta saama Merkle-käytäntö on sama kuin sen RAM-muistiin tallentama Merkle-käytäntö, se on vakuuttunut siitä, että UTXO nro 3 on todellakin osa UTXO-joukkoa.

Tämä menetelmä vähentää koko solmun operaattoreiden RAM-muistivaatimuksia. Utreexolla on kuitenkin rajoituksia, kuten lohkokoon kasvu lisätodisteiden vuoksi ja Utreexon solmujen mahdollinen riippuvuus Bridge Nodeista puuttuvien todisteiden saamiseksi. Siltasolmut ovat perinteisiä täydellisiä solmuja, jotka toimittavat tarvittavat todisteet Utreexo-solmuille ja mahdollistavat näin täydellisen todentamisen. Tämä lähestymistapa tarjoaa kompromissin tehokkuuden ja hajauttamisen välillä, jolloin transaktioiden validointi on helpommin saatavilla käyttäjille, joilla on rajalliset resurssit.