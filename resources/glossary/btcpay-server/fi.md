---
term: BTCPay Server

definition: Avoimen lähdekoodin maksunvälittäjä, joka mahdollistas bitcoin-maksujen vastaanottamisen ilman välikäsiä.
---

⚠️ **Kriittinen tietoturvavaroitus (7. elokuuta 2026):** BTCPay Serveriä koskevaa kriittistä haavoittuvuutta hyödynnetään parhaillaan aktiivisesti, ja se voi johtaa varojen menetykseen. Päivitä instanssisi välittömästi **versioon 2.4.2** polun `Admin Dashboard > Server > Maintenance > Update` kautta ja tarkista sen jälkeen, että alatunnisteessa lukee `2.4.2`. Jos et pysty päivittämään heti, sammuta BTCPay Server. Päivityksen jälkeen sinun on myös uusittava kokonaan macaroons-tunnisteesi ja `macaroons.db`-tiedostosi, uusittava kokonaan kaikkien muiden Lightning-taustajärjestelmien tunnistautumismerkkijonot sekä, mikäli olet luonut kuuman on-chain-lompakon BTCPay Serverin sisällä, siirrettävä kyseiset varat ja luotava lompakko uudelleen. Integraattoreiden tulee lisäksi päivittää NBXplorer versioon 2.6.10. Lähde: [BTCPay Server 2.4.2 -julkaisutiedot](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server on avoimen lähdekoodin maksuprosessori, jonka avulla kauppiaat ja käyttäjät voivat hyväksyä Bitcoin-maksuja turvautumatta kolmannen osapuolen suorittamaan tapahtumien käsittelyyn. Vuonna 2017 lanseerattu BTCPay Server tarjoaa Bitcoin-maksujen integrointiratkaisun verkkokauppasivustoille, ja siinä on kehittyneitä ominaisuuksia, kuten tuki laitteistolompakoille, laskutus- ja kirjanpitotyökalut sekä yhteensopivuus Lightning-verkon kanssa. Sen kehittämisen aloitti Nicolas Dorier vastauksena Bitpayn toimintaan, joka hänen mukaansa oli johtanut käyttäjiään harhaan työntämällä heitä SegWit2x:n käyttöönottoon, jota yritys piti virheellisesti "oikeana" Bitcoinina. Tämä vastustus kiteytyi Nicolas Dorierin nyt kuuluisaksi tulleeseen twiittiin elokuussa 2017:

> "_Tämä on valhetta, luottamukseni sinuun on murtunut, teen sinusta tarpeettoman_".
