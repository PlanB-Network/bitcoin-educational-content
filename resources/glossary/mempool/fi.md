---
termi: MEMPOOL
---

Lyhenne sanoista "memory" ja "pool". Tämä viittaa virtuaaliseen tilaan, jossa Bitcoin-siirrot, jotka odottavat sisällyttämistä lohkoon, ryhmitellään yhteen. Kun siirto luodaan ja lähetetään Bitcoin-verkkoon, sen vahvistavat ensin verkon solmut. Jos siirto katsotaan päteväksi, se sijoitetaan kunkin solmun Mempooliin, jossa se pysyy kunnes kaivosmies valitsee sen sisällytettäväksi lohkoon.

On tärkeää huomata, että jokainen Bitcoin-verkon solmu ylläpitää omaa Mempooliaan, ja siksi Mempoolin sisältö voi vaihdella eri solmujen välillä milloin tahansa. Erityisesti `maxmempool`-parametri kunkin solmun `bitcoin.conf`-tiedostossa mahdollistaa operaattoreiden hallita RAM-muistin (satunnaiskäyttömuisti) määrää, jota heidän solmunsa käyttää odottavien siirtojen tallentamiseen Mempooliin. Mempoolin koon rajoittamisella solmuoperaattorit voivat estää sen kuluttamasta liikaa resursseja järjestelmässään. Tämä parametri ilmoitetaan megatavuina (MB). Bitcoin Coren oletusarvo tähän mennessä on 300 MB.

Mempoolissa olevat siirrot ovat alustavia. Niitä ei tulisi pitää muuttumattomina ennen kuin ne on sisällytetty lohkoon ja saaneet tietyn määrän vahvistuksia. Näitä voidaan usein korvata tai poistaa.