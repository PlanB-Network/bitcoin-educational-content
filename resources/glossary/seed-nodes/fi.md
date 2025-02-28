---
term: SEED NODES

---
Staattinen luettelo julkisista Bitcoin-solmuista, joka on integroitu suoraan Bitcoin Coren lähdekoodiin (`bitcoin/src/chainparamsseeds.h`). Tämä luettelo toimii yhteyspisteinä uusille Bitcoin-solmuille, jotka liittyvät verkkoon, mutta sitä käytetään vain, jos DNS-siemenet eivät anna vastausta 60 sekunnin kuluessa pyynnöstä. Tällöin uusi Bitcoin-solmu muodostaa yhteyden näihin siemensolmuihin luodakseen ensimmäisen yhteyden verkkoon ja pyytäessään muiden solmujen IP-osoitteita. Perimmäisenä tavoitteena on hankkia tarvittavat tiedot, jotta voidaan suorittaa alustava lohkolataus (Initial Block Download, IBD) ja synkronoitua ketjuun, jossa on kertynyt eniten työtä. Siemensolmujen luettelossa on lähes 1000 solmua, jotka on yksilöity BIP155:ssä vahvistetun standardin mukaisesti. Näin ollen siemensolmut edustavat Bitcoin-solmun kolmatta tapaa muodostaa yhteys verkkoon solmun itsensä luoman `peers.dat`-tiedoston mahdollisen käytön ja DNS-siementen pyytämisen jälkeen.

> ► * Huomaa, että siemensolmuja ei pidä sekoittaa DNS-siemeniin, jotka ovat toinen tapa luoda yhteyksiä.*