---
term: MEMPOOL

---
Termien "memory" ja "pool" lyhenne. Tämä viittaa virtuaaliseen tilaan, jossa lohkoon sisällyttämistä odottavat Bitcoin-tapahtumat on ryhmitelty yhteen. Kun transaktio luodaan ja lähetetään Bitcoin-verkossa, verkon solmut tarkistavat sen ensin. Jos se katsotaan kelvolliseksi, se sijoitetaan kunkin solmun Mempool-varastoon, jossa se pysyy, kunnes louhija valitsee sen sisällytettäväksi lohkoon.

On tärkeää huomata, että Bitcoin-verkon jokainen solmu ylläpitää omaa Mempool-varastoa, joten Mempoolin sisältö voi vaihdella eri solmujen välillä milloin tahansa. Kunkin solmun `bitcoin.conf`-tiedostossa olevan parametrin `maxmempool` avulla operaattorit voivat hallita RAM-muistin (satunnaiskäyttömuisti) määrää, jota heidän solmunsa käyttää tallentaakseen vireillä olevia transaktioita Mempooliin. Rajoittamalla Mempoolin kokoa solmujen operaattorit voivat estää sitä kuluttamasta liikaa järjestelmän resursseja. Tämä parametri ilmoitetaan megatavuina (MB). Bitcoin Coren oletusarvo tähän mennessä on 300 MB.

Mempoolissa olevat tapahtumat ovat väliaikaisia. Niitä ei pitäisi pitää muuttumattomina ennen kuin ne on sisällytetty lohkoon ja tietyn määrän vahvistuksia jälkeen. Ne voidaan usein korvata tai tyhjentää.