---
termi: UTREEXO
---

Protokolla, jonka Tadge Dryja on suunnitellut Bitcoin-noodien UTXO-joukon tiivistämiseen käyttäen akkumulaattoria, joka perustuu Merkle-puihin. Toisin kuin klassinen UTXO-joukko, joka vaatii merkittävästi tallennustilaa, Utreexo vähentää radikaalisti tarvittavaa muistia säilyttämällä vain Merkle-puiden juuria. Tämä mahdollistaa noodin varmistaa UTXO:iden olemassaolon, joita käytetään transaktioiden syötteissä, ilman, että sen tarvitsee säilyttää koko UTXO-joukkoa. Utreexoa käyttämällä jokainen noodi säilyttää vain kryptografisen sormenjäljen, jota kutsutaan Merkle-juureksi. Kun transaktio tehdään, käyttäjä toimittaa omistuksen todisteet UTXO:ista ja vastaavat Merkle-polut. Näin noodi voi varmistaa transaktiot säilyttämättä koko UTXO-joukkoa. Otetaan esimerkki diagrammin avulla ymmärtääksemme tämän mekanismin:

![](../../dictionnaire/assets/15.png)

Tässä esimerkissä vähensin tarkoituksella UTXO-joukon 4 UTXO:oon ymmärtämisen helpottamiseksi. Todellisuudessa on tärkeää kuvitella, että Bitcoinissa on lähes 140 miljoonaa UTXO:a kirjoitushetkellä. Tässä diagrammissa Utreexo-noodin tarvitsisi säilyttää vain Merkle-juuri RAM-muistissa. Jos se vastaanottaa transaktion, joka käyttää UTXO:a numero 3 (mustana), todistus koostuisi seuraavista elementeistä:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Tämän transaktion lähettäjän välittämän tiedon avulla Utreexo-noodi suorittaa seuraavat tarkistukset:
* Se laskee UTXO 3:n jäljen, mikä antaa sille HASH 3:n;
* Se yhdistää HASH 3:n HASH 4:ään;
* Se laskee niiden jäljen, mikä antaa sille HASH 3-4:n;
* Se yhdistää HASH 3-4:n HASH 1-2:een;
* Se laskee niiden jäljen, mikä antaa sille Merkle-juuren.

Jos Merkle-juuri, jonka se saa prosessinsa kautta, on sama kuin se Merkle-juuri, jonka se on säilyttänyt RAM-muistissaan, se on vakuuttunut siitä, että UTXO numero 3 on todellakin osa UTXO-joukkoa.
Tämä menetelmä vähentää täysnoodien RAM-vaatimuksia. Utreexolla on kuitenkin rajoituksia, mukaan lukien lohkon koon kasvu lisätodisteiden vuoksi ja Utreexo-noodien mahdollinen riippuvuus Bridge Nodeista puuttuvien todisteiden saamiseksi. Bridge Nodet ovat perinteisiä täysnoodeja, jotka tarjoavat tarvittavat todisteet Utreexo-noodeille, mahdollistaen täyden varmennuksen. Tämä lähestymistapa tarjoaa kompromissin tehokkuuden ja hajautuksen välillä, tehden transaktioiden vahvistamisen helpommin saavutettavaksi käyttäjille, joilla on rajalliset resurssit.