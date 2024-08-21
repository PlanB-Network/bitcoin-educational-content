---
termi: INITIAL BLOCK DOWNLOAD (IBD)
---

Viittaa prosessiin, jonka aikana solmu lataa ja varmentaa lohkoketjun Genesis-lohkosta lähtien ja synkronoituu Bitcoin-verkon muiden solmujen kanssa. IBD on suoritettava uuden täyssolmun käynnistäessä. Tämän alkusynkronoinnin alussa solmulla ei ole tietoa aiemmista transaktioista. Se lataa siis jokaisen lohkon verkon muista solmuista, varmistaa sen pätevyyden ja lisää sen sitten paikalliseen versioonsa lohkoketjusta. On huomionarvoista, että IBD voi olla pitkäkestoinen ja resurssi-intensiivinen johtuen lohkoketjun ja UTXO-joukon kasvavasta koosta. Sen suoritusnopeus riippuu isäntäkoneen laskentakyvystä, RAM-muistin kapasiteetista, tallennuslaitteen nopeudesta ja kaistanleveydestä. Antaaksesi sinulle käsityksen, jos sinulla on tehokas internet-yhteys ja solmu isännöidään viimeisimmällä MacBookilla, jossa on runsaasti RAM-muistia, IBD kestää vain muutaman tunnin. Päinvastoin, jos käytät mikrotietokonetta, kuten Raspberry Pi:tä, IBD voi kestää viikon tai enemmän.

> ► *Ranskaksi on yleisesti hyväksytty viitata suoraan IBD:hen. Joskus käytetty käännös on "synchronisation initiale" tai "téléchargement initial des blocs".*