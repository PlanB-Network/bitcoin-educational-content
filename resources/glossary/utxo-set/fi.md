---
term: UTXO SET

---
Tarkoittaa kaikkien tiettynä hetkenä olemassa olevien UTXO:iden kokoelmaa. Toisin sanoen se on suuri luettelo kaikista bitcoinien eri paloista, jotka odottavat käyttämistä. Jos lasket yhteen UTXO-joukon kaikkien UTXO-erien määrät, saadaan liikkeessä olevien bitcoinien rahamääräinen kokonaismassa. Bitcoin-verkon jokainen solmu ylläpitää omaa UTXO-joukkoaan reaaliaikaisesti. Se päivittää sitä sitä mukaa, kun uusia kelvollisia lohkoja vahvistetaan, ja niiden sisältämiä transaktioita, jotka kuluttavat UTXO-joukon UTXO-yksiköitä ja luovat uusia UTXO-yksiköitä vastineeksi.

Kukin solmu säilyttää tätä UTXO-joukkoa, jotta se voi nopeasti tarkistaa, ovatko transaktioihin käytetyt UTXO:t todella laillisia. Näin ne voivat havaita ja torjua kaksinkertaisen kuluttamisen yritykset. UTXO-joukko on usein Bitcoinin hajauttamiseen liittyvien huolenaiheiden ytimessä, sillä sen koko kasvaa luonnollisesti hyvin nopeasti. Koska osa siitä on pidettävä RAM-muistissa, jotta transaktiot voidaan todentaa kohtuullisessa ajassa, UTXO-joukko voi vähitellen tehdä kokonaisen solmun käyttämisestä liian kallista. UTXO-joukolla on myös merkittävä vaikutus IBD:hen (*Initial Block Download*). Mitä enemmän UTXO-joukkoa voidaan sijoittaa RAM-muistiin, sitä nopeampi IBD on. Bitcoin Coressa UTXO-setti tallennetaan kansioon nimeltä `/chainstate`.

> ► *Englanniksi "UTXO set" voitaisiin kääntää "UTXO set".*