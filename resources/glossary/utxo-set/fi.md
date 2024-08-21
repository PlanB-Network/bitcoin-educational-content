---
termi: UTXO JOUKKO
---

Viittaa kaikkien olemassa olevien UTXO:iden kokoelmaan tietyllä hetkellä. Toisin sanoen, se on suuri lista kaikista eri bitcoinien palasista, jotka odottavat käytettäväksi. Jos lasket yhteen kaikkien UTXO-joukon UTXO:iden määrät, saat kokonaissumman bitcoineja, jotka ovat kierrossa. Jokainen solmu Bitcoin-verkossa ylläpitää omaa UTXO-joukkoaan reaaliajassa. Se päivittää sitä aina, kun uudet validit lohkot vahvistetaan sisältäen transaktioita, jotka kuluttavat joitakin UTXO:ja UTXO-joukosta ja luovat uusia tilalle.

Jokainen solmu pitää yllä tätä UTXO-joukkoa nopeuttaakseen transaktioissa käytettyjen UTXO:jen legitiimiyden tarkistusta. Tämä mahdollistaa heidän havaita ja hylätä kaksinkertaisen kulutuksen yritykset. UTXO-joukko on usein Bitcoinin hajauttamisen ytimessä, koska sen koko luonnollisesti kasvaa erittäin nopeasti. Koska osa siitä on pidettävä RAM-muistissa transaktioiden tarkistamiseksi kohtuullisessa ajassa, UTXO-joukko voisi ajan myötä tehdä täyden solmun ylläpidon liian kalliiksi. UTXO-joukolla on myös merkittävä vaikutus IBD:hen (*Alkuperäinen Lohkon Lataus*). Mitä enemmän UTXO-joukkoa voidaan sijoittaa RAM-muistiin, sitä nopeampi IBD on. Bitcoin Core:ssa UTXO-joukko säilytetään kansiossa nimeltä `/chainstate`.

> ► *Englanniksi "UTXO set" voidaan kääntää suomeksi "UTXO joukko".*