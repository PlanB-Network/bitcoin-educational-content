---
name: Watch Tower
description: Vartiotornin ymmärtäminen ja käyttäminen
---

## Miten vartiotornit toimivat?

Oleellisena osana Lightning Network -ekosysteemiä, vartiotornit tarjoavat lisäsuojaa käyttäjien salamakanaville. Niiden päävastuu on pitää silmällä kanavien terveyttä ja puuttua tilanteeseen, jos toinen kanavaosapuoli yrittää huijata toista.

Miten vartiotorni voi määrittää, onko kanava vaarantunut? Vartiotorni saa tarvittavat tiedot asiakkaalta, yhdeltä kanavaosapuolilta, jotta se voi asianmukaisesti tunnistaa ja reagoida mahdollisiin rikkomuksiin. Tähän tietoon sisältyy yleensä viimeisimmät tapahtumatiedot, nykyinen kanavan tila ja tarvittavat tiedot rangaistustransaktioiden luomiseksi. Ennen tietojen lähettämistä vartiotornille, asiakas saattaa salata ne yksityisyyden ja salassapidon suojaamiseksi. Tämä estää vartiotornia purkamasta salattuja tietoja, ellei rikkomusta todella ole tapahtunut, vaikka se saisi tiedot. Tämä salausjärjestelmä suojaa asiakkaan yksityisyyttä ja estää vartiotornia pääsemästä käsiksi yksityisiin tietoihin ilman lupaa.

## Kuinka pystytät oman Eye of Satoshi -vartiotornisi ja aloitat panostamisen

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) on ei-huoltaja Lightning vartiotorni, joka on yhteensopiva [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) kanssa. Siinä on kaksi pääkomponenttia:

1. teos: sisältää CLI:n ja tornin palvelinpuolen ydintoiminnot. Tämän paketin rakentaminen tuottaa kaksi binääriä—teosd ja teos-cli.

2. teos-common: Sisältää jaetut palvelin- ja asiakaspuolen toiminnot (hyödyllinen asiakkaan luomisessa).

Jotta torni toimisi onnistuneesti, sinun on käynnistettävä bitcoind ennen tornin käynnistämistä teosd-komennolla. Ennen näiden komentojen suorittamista sinun on määritettävä bitcoin.conf-tiedostosi. Tässä ovat ohjeet, kuinka tämä tehdään:

1. Asenna bitcoin core lähdekoodista tai lataa se. Lataamisen jälkeen sijoita bitcoin.conf-tiedosto Bitcoin core -käyttäjähakemistoon. Tarkista tämä linkki saadaksesi lisätietoja tiedoston sijoituspaikasta, sillä se riippuu käyttämästäsi käyttöjärjestelmästä.

2. Tiedoston luomispaikan tunnistamisen jälkeen, lisää nämä asetukset:

'''
#RPC
server=1
rpcuser=<käyttäjäsi>
rpcpassword=<salasanasi>

#chain
regtest=1
'''

- server: RPC-pyyntöjä varten
- rpcuser ja rpcpassword: RPC-asiakkaat voivat todentaa itsensä palvelimelle
- regtest: Ei pakollinen, mutta hyödyllinen, jos suunnittelet kehitystyötä.

Sinun on valittava rpcuser ja rpcpassword. Ne on kirjoitettava ilman lainausmerkkejä. Esim:

'''
rpcuser=aniketh
rpcpassword=strongpassword
'''

Nyt, jos suoritat bitcoind:n, sen pitäisi alkaa suorittaa solmua.

1. Tornin osalta, sinun on ensin asennettava teos lähdekoodista. Noudata tässä linkissä annettuja ohjeita.

2. Onnistuneesti asennettuasi teos:n järjestelmääsi ja suoritettuasi testit, voit edetä viimeiseen vaiheeseen, joka on teos.toml-tiedoston määrittäminen teos-käyttäjähakemistossa. Tiedosto on sijoitettava kansioon nimeltä .teos (huomaa piste) kotihakemistossasi. Esimerkiksi Linuxissa /home/<käyttäjänimesi>/.teos. Kun olet löytänyt paikan, luo teos.toml-tiedosto ja aseta nämä asetukset vastaamaan muutoksia, joita olemme tehneet bitcoind:ssa.
#bitcoindbtc_network = "regtest"
btc_rpc_user = <käyttäjänimesi>
btc_rpc_password = <salasanasi>
'''

Huomaa, että tässä käyttäjänimen ja salasanan on oltava lainausmerkeissä, eli saman esimerkin mukaisesti:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "vahvasalasana"
'''

Kun olet tehnyt tämän, sinun pitäisi olla valmis käynnistämään torni. Koska käytämme regtestiä, on mahdollista, ettei bitcoin-testiverkossamme ole louhittu yhtään lohkoa ensimmäisellä kerralla, kun torni yhdistää siihen (jos on, jokin on varmasti pielessä). Torni rakentaa sisäisen välimuistin bitcoindin viimeisimmistä 100 lohkosta, joten ensimmäisellä kerralla suorittaessamme saatamme saada seuraavan virheen:

> VIRHE [teosd] Ei tarpeeksi lohkoja tornin käynnistämiseksi (vaadittu: 100). Louhi vähintään 100 lohkoa lisää

Koska käytämme regtestiä, voimme louhia lohkoja antamalla RPC-komennon, ilman että meidän tarvitsee odottaa 10 minuutin keskimääräistä aikaa, jonka yleensä näemme muissa verkoissa (kuten pääverkko tai testiverkko). Tarkista bitcoin-cli:n ohje ja etsi, miten lohkoja louhitaan. Jos tarvitset apua, voit tutustua tähän artikkeliin.

![kuva](assets/2.webp)

Siinä kaikki, olet onnistuneesti käynnistänyt tornin. Onnittelut. 🎉