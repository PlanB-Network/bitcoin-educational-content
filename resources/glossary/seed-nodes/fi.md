---
termi: SEED-NODET
---

Staattinen lista julkisista Bitcoin-nodesta, jotka on integroitu suoraan Bitcoin Coren lähdekoodiin (`bitcoin/src/chainparamsseeds.h`). Tämä lista toimii yhteyspisteinä uusille Bitcoin-nodeille liittyessään verkkoon, mutta sitä käytetään vain, jos DNS-seedien ei anna vastausta 60 sekunnin kuluessa niiden pyynnöstä. Tässä tapauksessa uusi Bitcoin-node yhdistää näihin seed-nodeihin muodostaakseen ensimmäisen yhteyden verkkoon ja pyytääkseen muiden nodien IP-osoitteita. Lopullisena tavoitteena on hankkia tarvittavat tiedot suorittamaan Alkuperäinen Lohkon Lataus (IBD) ja synkronoitumaan ketjun kanssa, jolla on kertynyt eniten työtä. Seed-nodien lista sisältää lähes 1000 nodeta, jotka on tunnistettu BIP155-standardin mukaisesti. Näin ollen seed-nodet edustavat kolmatta menetelmää yhteyden muodostamiseksi verkkoon Bitcoin-nodelle, mahdollisen `peers.dat` tiedoston käytön jälkeen, jonka node itse luo, ja DNS-seedien pyytämisen jälkeen.

> ► *Huomaa, seed-nodeja ei tule sekoittaa "DNS-seedeihin", jotka ovat toinen menetelmä yhteyksien muodostamiseksi.*