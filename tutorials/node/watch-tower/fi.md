---
name: Lightning Watchtower
description: Watchtower:n ymmärtäminen ja käyttö Lightning-solmussa
---
![cover](assets/cover.webp)



## Miten vartiotornit toimivat?



Lightning Network:n ekosysteemin olennainen osa, _Watchtowers_ tarjoaa ylimääräistä suojaa käyttäjien Lightning-kanaville. Niiden päätehtävänä on valvoa kanavan tilaa ja puuttua asiaan, jos kanavan toinen osapuoli yrittää huijata toista.



Miten Watchtower voi määrittää, onko kanava vaarantunut? Se saa asiakkaalta (yhdeltä kanavan osapuolelta) tiedot, joita tarvitaan mahdollisen loukkauksen asianmukaiseen tunnistamiseen ja käsittelyyn. Näihin tietoihin kuuluvat tiedot viimeisimmästä tapahtumasta, kanavan nykytilasta ja rangaistustapahtumien luomiseen tarvittavasta Elements:stä. Ennen näiden tietojen lähettämistä Watchtower:lle asiakas voi salata ne luottamuksellisuuden säilyttämiseksi. Vaikka Watchtower vastaanottaa tiedot, se ei voi purkaa niitä ennen kuin rikkomus on todella tapahtunut. Tämä salausmekanismi suojaa asiakkaan yksityisyyttä ja estää Watchtower:a saamasta luvatonta pääsyä arkaluonteisiin tietoihin.



Tässä ohjeessa tarkastelemme 3 tapaa käyttää **Watchtower** :




- ensinnäkin klassinen raaka menetelmä LND:n kautta,
- sitten toinen lähestymistapa Eye of Satoshi:n kanssa,
- ja lopuksi Watchtower:n yksinkertaistettu konfigurointi Lightning-solmussasi, jota isännöi Umbrel.



## 1 - Watchtower:n tai LND:n kautta toimivan asiakkaan määrittäminen



*Tämä ohje on otettu [virallisesta LND-dokumentaatiosta](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Alkuperäiseen versioon on saatettu tehdä joitakin muutoksia



Versiosta 0.7.0 lähtien `LND` tukee yksityisen altruistisen Watchtower:n suorittamista täysin integroituna `LND`:n alijärjestelmänä. Watchtowerit tarjoavat toisen puolustuslinjan ilkivaltaisia tai vahingossa tapahtuvia murtautumisskenaarioita vastaan, kun asiakassolmu on offline tai ei pysty vastaamaan murtautumishetkellä, mikä lisää kanavarahastojen turvallisuutta.



Toisin kuin _palkkiovartiotorni_, joka vaatii vastineeksi palvelustaan osuuden kanavan varoista, _altruistinen vartiotorni_ palauttaa kaikki uhrin varat (miinus On-Chain-palkkiot) perimättä palkkiota. Palkitsemisvartiotornit aktivoidaan myöhemmässä versiossa; ne ovat vielä testaus- ja parannusvaiheessa.



Lisäksi LND voidaan nyt konfiguroida toimimaan _vartiotornin asiakkaana_, joka tallentaa salattuja rikkomusten korjaustapahtumia (niin sanottuja "oikeustapahtumia") muilta epäitsekkäiltä vartiotorneilta. Watchtower tallentaa kiinteän kokoisia salattuja blobeja ja voi purkaa salauksen ja julkaista oikeudenmukaisuustransaktion vasta sen jälkeen, kun rikkomuksen tekijä on lähettänyt peruutetun Commitment-tilan. Asiakas ↔ Watchtower -viestintä salataan ja todennetaan ephemeral-avainpareilla, mikä rajoittaa Watchtower:n kykyä jäljittää asiakkaitaan pitkäaikaisten tunnistetietojen avulla.



Huomaa, että olemme päättäneet ottaa tässä versiossa käyttöön rajoitetun joukon ominaisuuksia, jotka jo tarjoavat merkittävää turvallisuutta LND-käyttäjille. Monet muut Watchtower:ään liittyvät ominaisuudet ovat joko lähellä valmistumista tai jo pitkällä; jatkamme niiden toimittamista sitä mukaa kuin testaamme niitä ja heti kun ne katsotaan turvallisiksi.



huom: toistaiseksi vartiotornit tallentavat vain peruttujen sitoumusten `to_local`- ja `to_remote`-tulosteet; HTLC-tulosteen tallentaminen otetaan käyttöön tulevassa versiossa, kun protokollaa voidaan laajentaa lisäämään allekirjoitustietoja salattuihin blobseihin._



### Watchtower:n määrittäminen



Watchtower:n asentamiseksi komentorivin käyttäjien on käännettävä valinnainen `watchtowerrpc`-alipalvelin, joka mahdollistaa vuorovaikutuksen Watchtower:n kanssa gRPC:n tai `lncli`:n kautta. Julkaistut binäärit sisältävät oletusarvoisesti `watchtowerrpc`-alipalvelimen.



Watchtower:n aktivoiminen edellyttää vähintään asetusta `Watchtower.active=1`.



Voit hakea Watchtower:n kokoonpanotiedot komennolla `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Kaikki Watchtower:n konfigurointivaihtoehdot ovat käytettävissä komennolla `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Kuunteluliitännät



Oletusarvoisesti Watchtower kuuntelee osoitteessa `:9911`, joka vastaa porttia `9911` kaikissa käytettävissä olevissa liitännöissä. Käyttäjät voivat määritellä omat kuuntelurajapintansa vaihtoehdolla `--Watchtower.listen=`. Voit tarkistaa asetuksesi `lncli tower info`:n `"listeners"-kentästä. Jos sinulla on ongelmia yhteyden muodostamisessa Watchtower:aan, varmista, että `<port>` on auki tai että välityspalvelimesi on konfiguroitu oikein aktiiviseen Interface:ään.



#### Ulkoiset IP-osoitteet



Käyttäjät voivat myös määrittää Watchtower:n ulkoisen IP-osoitteen Address(e) komennolla `Watchtower.externalip=`, joka paljastaa Watchtower:n täydellisen URI:n (pubkey@host:port) RPC:n tai `lncli tower info`:n kautta:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI:t voidaan ilmoittaa asiakkaille yhteyden muodostamista ja käyttöä varten seuraavalla komennolla:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Jos Watchtower:n asiakkaiden on päästävä siihen käsiksi etänä, varmista, että :




- Avaa portti 9911 (tai portti, joka on määritelty `Watchtower.listen`:n kautta).
- Käytä välityspalvelinta liikenteen ohjaamiseen avoimesta portista Watchtower:n kuuntelevaan Address:ään.



#### Tor piilotetut palvelut



Watchtowers tukee Torin piilotettuja palveluita ja voi automaattisesti generate:n käynnistyksen yhteydessä seuraavilla asetuksilla:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Tämän jälkeen .onion Address ilmestyy `"uris"-kenttään `lncli tower info` -kyselyssä:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



huomautus: Watchtower:n julkinen avain eroaa LND-solmun julkisesta avaimesta. Toistaiseksi se toimii "Soft:n valkoluettelona", sillä asiakkaiden on tiedettävä Watchtower:n julkinen avain, jotta he voivat käyttää sitä varmuuskopiona, kunnes kehittyneemmät valkoluettelomekanismit tulevat käyttöön. Suosittelemme, ettet paljasta tätä julkista avainta avoimesti, ellet ole valmis paljastamaan Watchtower:ääsi koko Internetille._



#### Watchtower-tietokannan hakemisto



Watchtower-tietokanta voidaan siirtää käyttämällä vaihtoehtoa `Watchtower.towerdir=`. Huomaa, että valittuun polkuun lisätään `/Bitcoin/Mainnet/Watchtower.db` -liite, jotta tietokannat voidaan eristää merkkijonon mukaan. Näin ollen asetus `Watchtower.towerdir=/path/to/towerdir` tuottaa tietokannan osoitteeseen `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Esimerkiksi Linuxissa Watchtower:n oletustietokanta sijaitsee osoitteessa :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Watchtower-asiakkaan määrittäminen



Watchtower-asiakkaan määrittäminen edellyttää kahta asiaa:





- Aktivoi Watchtower-asiakasohjelma vaihtoehdolla `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- Aktiivisen Watchtower:n URI.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Voit määrittää useita vartiotorneja tällä tavalla.



#### Oikeudellisista toimista perittävät maksut



Käyttäjät voivat valinnaisesti asettaa oikeudenmukaisuustapahtumien maksun hinnan valitsemalla `wtclient.sweep-fee-rate` -vaihtoehdon, joka hyväksyy arvot sat/byte. Oletusarvo on 10 sat/byte, mutta on mahdollista pyrkiä korkeampaan maksuun, jotta maksuhuippujen aikana saavutetaan korkeampi prioriteetti. `sweep-fee-rate`:n muuttaminen koskee kaikkia uusia päivityksiä daemon:n uudelleenkäynnistyksen jälkeen.



#### Valvonta



Käyttäjät voivat nyt komennolla `lncli wtclient` olla suoraan vuorovaikutuksessa Watchtower-asiakkaan kanssa saadakseen tai muuttaakseen tietoja kaikista rekisteröidyistä vartiotorneista.



Esimerkiksi komennolla `lncli wtclient tower` saat selville edellä lisätyn Watchtower:n kanssa parhaillaan neuvoteltujen istuntojen määrän ja voit määrittää, käytetäänkö sitä varmuuskopiointiin kentän `active_session_candidate` ansiosta.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Jos haluat saada tietoja Watchtower-istunnoista, käytä `--include_sessions`-vaihtoehtoa.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Kaikki Watchtower-asiakkaan asetukset ovat käytettävissä komennolla `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Satoshi:n oman Eye of Satoshi:n asentaminen



*Tämä opetusohjelma on osittain poimittu [Summer of Bitcoin -blogin] (https://blog.summerofbitcoin.org/) artikkelista. Alkuperäiseen versioon on tehty muutoksia*



Satoshi:n silmä ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) on [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) mukainen Watchtower Salama, joka ei ole talletettu. Se koostuu kahdesta pääkomponentista:





- teos**: sisältää komentorivin Interface (CLI) ja Watchtower:n keskeiset palvelinominaisuudet. Kaksi binääritiedostoa - **teosd** ja **teos-CLI** - tuotetaan, kun tämä _crate_ käännetään.





- teos-common**: sisältää jaetun palvelin- ja asiakaspuolen toiminnallisuuden (hyödyllinen asiakkaan luomisessa).



Jotta Watchtower toimisi oikein, sinun on suoritettava **bitcoind** ennen Watchtower:n käynnistämistä komennolla **teosd**. Ennen näiden kahden komennon suorittamista sinun on määritettävä **Bitcoin.conf**-tiedosto. Näin se tehdään:





- Asenna Bitcoin core lähdekoodista tai lataa se. Kun olet ladannut sen, aseta **Bitcoin.conf**-tiedosto Bitcoin core:n käyttäjähakemistoon. Katso tästä linkistä lisätietoja tiedoston sijoittamisesta, sillä se riippuu käytettävästä käyttöjärjestelmästä.





- Kun sijainti on määritetty, lisää seuraavat vaihtoehdot:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- palvelin**: RPC-pyyntöjä varten





- rpcuser** ja **rpcpassword**: RPC-asiakkaiden todennus palvelimelle





- regtest**: ei pakollinen, mutta hyödyllinen, jos suunnittelet kehitystä.



**rpccuser**- ja **rpcpassword**-arvot on valittava itse. Ne on kirjoitettava ilman lainausmerkkejä. Esimerkiksi:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Jos nyt suoritat **bitcoind**, solmun pitäisi käynnistyä.





- Watchtower-osaa varten sinun on ensin asennettava **teos** lähdekoodista. Seuraa tässä linkissä annettuja ohjeita.





- Kun olet onnistuneesti asentanut **teos**:n järjestelmääsi ja suorittanut testit, voit siirtyä viimeiseen vaiheeseen: **teos.toml**-tiedoston määrittämiseen teos-käyttäjähakemistoon. Tiedosto on sijoitettava kansioon nimeltä **.teos** (huomaa piste) kotihakemistosi alle. Esimerkiksi **/home//.teos** Linuxissa. Kun sijainti on löydetty, luo **teos.toml**-tiedosto ja aseta nämä asetukset **bitcoind**:ssä** tehtyjen muutosten mukaisesti:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Huomaa, että käyttäjätunnus ja salasana on kirjoitettava **lainausmerkkien sisään**. Edellisen esimerkin avulla :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Kun tämä on tehty, sinun pitäisi olla valmis käynnistämään Watchtower. Koska käytämme **regtest**-verkkoa, on todennäköistä, että Bitcoin-testiverkossamme ei louhittu lohkoja, kun Watchtower kytkeytyi ensimmäisen kerran (jos näin tapahtui, jokin on vialla). Watchtower luo sisäisen välimuistin **bitcoind**:n viimeisistä sadasta lohkosta, joten ensimmäisellä käynnistyskerralla saatat saada seuraavan virheilmoituksen:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Koska käytämme **regtest**-ohjelmaa, voimme käyttää Miner-lohkoja antamalla RPC-komennon ilman, että meidän tarvitsee odottaa muissa verkoissa (kuten Mainnet tai Testnet) havaittua 10 minuutin mediaaniviivettä. Katso **bitcoin-cli**-ohjeesta lisätietoja Miner-lohkojen käytöstä.



![Image](assets/fr/01.webp)



Siinä kaikki: olet suorittanut Watchtower:n onnistuneesti. Onnittelut. 🎉




## 3 - Watchtower:n konfigurointi Umbrelissa



Umbrelissa yhteyden muodostaminen Watchtower:een Lightning-solmun suojaamiseksi on erittäin yksinkertaista, sillä kaikki tapahtuu graafisen Interface:n kautta. Kun olet muodostanut etäyhteyden solmuun, avaa "**Lightning Node**" -sovellus.



![Image](assets/fr/02.webp)



Napsauta kolmea pientä pistettä Interface:n oikeassa yläkulmassa ja valitse sitten "**Lisäasetukset**".



![Image](assets/fr/03.webp)



Valikossa "**Watchtower**" on kaksi vaihtoehtoa:





- Watchtower-palvelu**: Tämän vaihtoehdon avulla voit käyttää Watchtower:tä eli palvelua, joka valvoo muiden solmujen kanavia havaitakseen mahdolliset petosyritykset. Jos petos tapahtuu, Watchtower julkaisee tapahtuman Blockchain:ssä, jolloin käyttäjät voivat saada lukitut varansa takaisin. Aktivoinnin jälkeen Watchtower:n URI ilmestyy näkyviin, ja se voidaan välittää muille solmuille, jotta ne voivat lisätä sen Watchtower-asiakkaaseen;





- Watchtower Client**: Tämän vaihtoehdon avulla voit muodostaa yhteyden ulkoisiin vahtitorniin omien kanavien suojaamiseksi. Kun olet aktivoinut sen, voit lisätä Watchtower-palveluja, joihin solmusi lähettää tarvittavat tiedot kanavistaan. Nämä vartiotornit valvovat sitten niiden tilaa ja puuttuvat asiaan, jos kanavia yritetään huijata.



Ensisijaisesti sinun on tietenkin aktivoitava *Watchtower Client* solmusi suojaamiseksi, mutta suosittelen myös *Watchtower Service*:n aktivoimista, jotta voit vastineeksi edistää muiden käyttäjien turvallisuutta.



![Image](assets/fr/04.webp)



Napsauta sitten Green:n "**Tallenna ja käynnistä solmu uudelleen**"-painiketta. LND käynnistyy uudelleen.



Samasta valikosta löydät myös Watchtower-palvelun URI:n, jos olet aktivoinut sen. Voit myös lisätä ulkoisen Watchtower:n URI:n kanavien suojaamiseksi. Vahvista klikkaamalla "**ADD**".



![Image](assets/fr/05.webp)



Verkossa on saatavilla useita Vartiotorneja. Esimerkiksi [LN+ ja Voltage tarjoavat altruistisen Watchtower:n](https://lightningnetwork.plus/Watchtower), johon voit muodostaa yhteyden:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Toinen vaihtoehto on Exchange Watchtower URI:n käyttäminen yhdessä muiden bitcoin-käyttäjien kanssa, jotta kumpikin suojelee toistensa solmua.



Suosittelen myös, että perustat useita vartiotorneja, jotta voit vähentää riskejä siinä tapauksessa, että yksi niistä ei ole käytettävissä.



Lopuksi voit säätää parametria "**Watchtower Client Sweep Fee Rate**". Tämä määrittää maksimipalkkion, jonka olet valmis maksamaan lohkoon sisällytettävästä Watchtower-lähetysrangaistustapahtumasta. Varmista, että asetat riittävän korkean arvon, joka on mukautettu kanavissasi lukittuihin määriin.