---
term: ALUSTAVA LOHKOLATAUS (IBD)

---
Tarkoittaa prosessia, jossa solmu lataa ja tarkistaa lohkoketjun Genesis-lohkosta ja synkronoi sen Bitcoin-verkon muiden solmujen kanssa. IBD on suoritettava, kun käynnistetään uusi täysi solmu. Tämän ensimmäisen synkronoinnin alussa solmulla ei ole tietoa aiemmista transaktioista. Siksi se lataa jokaisen lohkon muilta verkon solmuilta, tarkistaa sen pätevyyden ja lisää sen sitten lohkoketjun paikalliseen versioonsa. On syytä huomata, että IBD voi olla pitkäaikainen ja resurssi-intensiivinen lohkoketjun ja UTXO-joukon koon kasvun vuoksi. Sen suorituksen nopeus riippuu solmua isännöivän tietokoneen laskentakyvystä, sen RAM-kapasiteetista, tallennuslaitteen nopeudesta ja kaistanleveydestä. Esimerkkinä mainittakoon, että jos sinulla on tehokas internetyhteys ja solmu on isännöity uusimmassa MacBookissa, jossa on runsaasti RAM-muistia, IBD kestää vain muutaman tunnin. Jos taas käytät mikrotietokonetta, kuten Raspberry Pi -tietokonetta, IBD voi kestää viikon tai enemmänkin.

> ► *Ranskaksi on yleisesti hyväksytty viittaus suoraan IBD:hen. Joskus käytetty käännös on "synchronisation initiale" tai "téléchargement initial des blocs".*