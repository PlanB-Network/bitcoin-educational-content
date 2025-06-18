---
name: Zeus Embedded - Edistyneet
description: Usean solmun itsesäätelyjärjestelmä Wallet
---

![Zeus](assets/cover.webp)


## ZEUS Wallet:n esittely


ZEUS on Bitcoin Wallet- ja solmujen hallintasovellus, jossa on Bitcoin Lightning Wallet:n täydet toiminnot ja joka tekee Bitcoin-maksuista yksinkertaisia, antaa käyttäjille täydellisen hallinnan taloudestaan ja antaa edistyneemmille käyttäjille mahdollisuuden hallita Lightning-solmujaan kämmeneltä käsin.


### Kenelle ZEUS on tarkoitettu?

Tällä hetkellä ZEUS on tarkoitettu ihmisille, jotka käyttävät omia [Lightning Network Daemon (LND)](https://lightning.engineering/) tai [Core Lightning Lightning (CLN)](https://blockstream.com/lightning/) koti-/yrityssolmujaan ja hallinnoivat niitä Zeuksen kautta etänä.


Kauppiaat, jotka käyttävät [BTCPay](https://btcpayserver.org/) tai [LNBits](https://lnbits.com/) tai [Alby](https://getalby.com/) (tai mitä tahansa muuta LNDhub-tiliä), voivat myös muodostaa yhteyden solmuihinsa / tileihinsä, käyttää niitä ja hallita niitä ZEUSista.


[Alkaen v0.8:sta](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS alkaa palvella tavallisia käyttäjiä, jotka haluavat vain yksinkertaisen tavan tehdä nopeita ja halpoja Bitcoin-maksuja mobiililaitteestaan, sillä ZEUSissa on [sisäänrakennettu mobiili Lightning-solmu](https://docs.zeusln.app/category/embedded-node), jossa on integroitu [Lightning-palveluntarjoaja (Lightning Service Provider, LSP)](https://docs.zeusln.app/lsp/intro).


### Tärkeitä Zeus-resursseja:


- Zeuksen virallinen verkkosivusto - [https://zeusln.app/](https://zeusln.app/)
- Zeus Documentation - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github arkisto](https://github.com/ZeusLN/zeus)
- [Zeus Telegram -tukiryhmä](https://t.me/ZeusLN)
- [Zeus on NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus Blogin ilmoitukset](https://blog.zeusln.com)


### Zeuksen ominaisuudet

#### Yleiset ominaisuudet:


- Omahuoltajuus, vain Bitcoin ja Lightning Wallet
- Ei käsittelymaksuja, ei KYC
- Täysin avoin lähdekoodi (APGLv3)
- Tuettu useita solmuja / tilejä (voit hallita omaa kotisolmua (-solmuja), käyttää sulautettua LND-solmua, muodostaa yhteyden useisiin LNDhub-tileihin)
- Helppokäyttöinen toimintovalikko
- PIN- tai passphrase-salaus, yksityisyydensuojatila - piilota arkaluonteiset tietosi
- Yhteystietokirja, multi teema, multi kieli


#### Tekniset ominaisuudet


- Yhdistä Torin kautta
- Täysi LNURL-tuki (maksu, nosto, hyväksyntä, kanava), lähetä Lightning-osoitteisiin
- Yksityiskohtainen valaistuskanavien hallinta, MPP/AMP-tuki, Keysend, reititysmaksujen hallinta
- Replace-by-fee (RBF) ja Lapsi maksaa vanhemmasta (CPFP) -tuki
- NFC-maksut ja -pyynnöt, allekirjoitus ja viestien vahvistaminen
- SegWit- ja Taproot-tuki
- Yksinkertaiset Taproot-kanavat
- Omahuoltajan salamaosoitteet (@zeuspay.com)
- Point of Sale by Square (pian avoin PoS)


### Oppaat ja video-oppaat

Jotta voisit käyttää Zeusta ja hallita Lightning-kanavia, likviditeettiä, maksuja jne., on parempi lukea ensin joitakin tärkeitä oppaita Lightning Network:stä.


#### Oppaat:


- [LND - Lightning Network Daemon Documentation](https://docs.lightning.engineering/)
- [CLN - Core Lightning Documentation](https://lightning.readthedocs.io/index.html)
- [Aloittelijoiden salamaopas](https://bitcoiner.guide/lightning/) - Bitcoin Q&A mukaan
- [Lightning Node Management](https://www.lightningnode.info/) - by openoms
- [Lightning Network ja lentoaseman analogia](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Salamasolmun likviditeetin hallinta](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Salamasolmun ylläpito](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### BTC Sessionsin video-opastus


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Kävelyopas Zeus LN:n sulautetun solmun käytön aloittamisesta mobiililaitteessa


![Image](assets/en/01.webp)


Omistan tämän oppaan kaikille niille uusille Lightning Network (LN) -käyttäjille, jotka haluavat aloittaa uuden suvereenin matkan käyttämällä Wallet-solmua mobiililaitteissaan.


Oletetaan, että olet jo käynyt läpi kaiken tuon huoltajien LN-lompakoiden runsauden, mutta et ole vielä valmis aloittamaan PUBLIC-routing LN-solmun käyttöä, vaan haluat vain pinota enemmän Sats:ta LN:n päälle enemmän itse huoltajina ja suorittaa säännölliset maksut LN:n kautta.


Täältä tulee Zeus, alkaen [versio v0.8.0 ilmoitti blogissaan](https://blog.zeusln.com/new-release-zeus-v0-8-0/), tarjoaa nyt upotettu LND solmun sovellukseen. Tähän asti Zeus oli noodien etähallintasovellus + LNDhub-tilit. Mutta nyt... solmu on puhelimessa!


![Image](assets/en/02.webp)


### Nopea yhteenveto Zeus Noden tärkeimmistä ominaisuuksista:



- Yksityinen LND-solmu** - Tämä tarkoittaa, että tämä solmu EI reititä muiden maksuja julkisesti solmusi kautta. Solmu ja kanavat ovat ilmoittamattomia (yksityisiä, eivät näy julkisessa LN-grafiikassa). Maksujen vastaanottaminen ja suorittaminen tapahtuu perusteellisesti yhdistettyjen LSP-vertaisvertaisvertaistesi kautta. MUISTUTUS: Zeus Embedded Node EI tee julkista reititystä!
- Pysyvä LND-palvelu** - käyttäjä voi aktivoida tämän ominaisuuden ja pitää LND-palvelun jatkuvasti aktiivisena kuten minkä tahansa tavallisen LN-solmun. Sovelluksen ei tarvitse olla avoinna, vaan jatkuva palvelu pitää kaiken viestinnän verkossa.
- Neutrino-lohkosuodattimet** - lohkosynkronointi tapahtuu [lohkosuodattimien ja Neutrino-protokollan](https://bitcoinops.org/en/topics/compact-block-filters/) avulla (kun ei ole tietoa käyttäjien On-Chain-varoista). Muistutus: korkean viiveen / hitaiden internetyhteyksien osalta tämä neutriinoon perustuva lohkosynkronointi voi joskus epäonnistua. Vaihtaminen lähellä olevaan neutriinopalvelimeen voi auttaa synkronoinnin palauttamisessa. Ilman tätä synkronointia LND-solmusi ei voi käynnistyä!
- Yksinkertaiset Taproot-kanavat** - Kun nämä kanavat suljetaan, käyttäjille aiheutuu vähemmän maksuja ja he saavat enemmän yksityisyyttä, koska ne näyttävät On-Chain-jalanjälkeä tarkasteltaessa samalta kuin muutkin Taproot-kanavat.
- Integroitu LSP** - Olympus on Zeuksen uusi LSP-solmu. Käyttäjät voivat vastaanottaa Sats:ää LN:n kautta välittömästi ilman, että LN-kanavia on aiemmin määritetty. Heidän on vain luotava LN Invoice ja maksettava mistä tahansa muusta LN Wallet:sta Zeuksen 0-conf-kanavapalvelun avulla. Lue lisää Zeus LSP:stä täältä. LSP tarjoaa myös lisää yksityisyyttä käyttäjillemme tarjoamalla heille käärittyjä laskuja, jotka salaavat solmujensa julkiset avaimet maksajilta.
- Yhteystietokirja** - voit tallentaa yhteystietoja manuaalisesti tai tuoda niitä NOSTR:stä, jotta voit helposti lähettää maksuja tavallisiin kohteisiisi.
- Täysi tuki LNURL:lle, LN Address:n lähettämiselle ja vastaanottamiselle** - nyt voit perustaa oman LN Address:n itsesäätöjärjestelmän @zeuspay.com:n avulla. Muistutus: Voit käyttää Zeusta myös LN-authiin sivustoilla, joihin voit kirjautua LN-tunnistautumisella. On erittäin kätevää.
- Myyntipiste** - Nyt kauppiaiden käyttäjät voivat asettaa omia tuotetuotteita ja myydä suoraan Zeuksesta, integroituna myyntipisteeseen. Tällä hetkellä se sisältää perustarpeet, mutta tulevaisuudessa se sisältää laajennettuja ominaisuuksia.
- LND-lokit** - käyttäjä voi lukea reaaliaikaisesti LND-palvelun lokitietoja ja käyttää niitä mahdollisten ongelmien (lähinnä huonojen yhteyksien) korjaamiseen
- Automaattiset varmuuskopiot** - LN-solmun kanavat varmuuskopioidaan automaattisesti Olympus-palvelimelle. Tämä automaattinen varmuuskopiointi on salattu solmun Wallet seed kanssa (ilman seed on täysin hyödytön). Käyttäjä voi myös viedä manuaalisesti SCB:n (staattinen kanavien varmuuskopio) katastrofipalautusta varten.


### Kuinka päästä alukselle Zeus LN Node (LND sulautettu) kanssa


Tässä oppaassa puhun vain sulautetusta LND-solmusta, enkä muista tavoista käyttää tätä upeaa sovellusta (solmujen etähallinta ja LNDhub-tilit). Muista yhteystyypeistä voit lukea [Zeus Docs -sivulta](https://docs.zeusln.app/category/getting-started), joka on selitetty erittäin hyvin, eikä erillistä opasta tarvitse kirjoittaa.


#### VAIHE 1 - ALKUASENNUS


Koska Zeus on täysi LND-solmu, minulla on joitakin alustavia suosituksia:



- Älä käytä vanhaa laitetta, sillä se voi vaikuttaa tämän tehokkaan sovelluksen käyttöön. Erityisesti synkronoinnin aikana sovellus voi käyttää intensiivisesti suorittimen ja RAM-muistia. Näiden puute voi jopa tehdä Zeus-sovelluksen käytön mahdottomaksi.
- Käytä mobiilikäyttöjärjestelmänä vähintään Android 11:tä ja päivitä sitä niin paljon kuin mahdollista. IOS:lle sama, yritä käyttää paljon korkeampaa käyttöjärjestelmäversiota.
- Tarvitset vähintään 1 Gt levytilaa tietojen tallentamista varten. Ajan mittaan voi kasvaa enemmän, mutta on olemassa toiminto, jolla tietokanta voidaan tiivistää MB:n tasolle.
- Zeusta ei tarvitse käyttää Tor- tai Orbot-palvelun kanssa. Älkää mutkistako asioita enempää kuin on tarpeen. Tor ei tässä tapauksessa tarjoa sinulle lisää yksityisyyttä, vaan vain huonontaa asioita alkuperäisen synkronoinnin osalta. Ole myös varovainen sen kanssa mitä VPN:ää käytät ja tarkista yhteyden latenssi neutrino-palvelimille päin. Pidä mielessä, että Neutrino-estosuodatin ei vuoda tai jäljitä laitteesi identiteettiä, se vain palvelee estoja. LN:n liikenne on myös LSP:n takana yksityisillä kanavilla, joten hyvin vähän tietoa tulee ulos, ei ole mitään syytä pelätä yksityisyyttä.
- Kärsivällisyyttä synkronoinnin alkuvaiheessa, se voi kestää useita minuutteja. Yritä olla yhteydessä laajakaistayhteyteen, jossa on hyvä viive. Jos sinulla on oma Bitcoin-solmu, [voit aktivoida neutriinopalvelun](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) ja liittää Zeuksen omaan solmuun, vaikka sisäisen lähiverkon kautta, jolloin saat maksiminopeuden.


Kun olet määrittänyt yhteystyypin "Sulautettu solmu", sovellus alkaa synkronoida jonkin aikaa. Odota kärsivällisesti tämän osan loppuun ja siirry sitten pääasetussivulle.


![Image](assets/en/03.webp)


Tutustutaan lyhyesti kuhunkin Asetukset-osioon ja selvitetään joitakin tärkeimpiä ominaisuuksia, ennen kuin alat käyttää Zeusta:


**A - ASETUKSET**


Tämä on osio, jossa on koko sovelluksen yleiset asetukset


**1 - Salamapalveluntarjoaja (LSP)**


Tässä esitellään kaksi LSP-palvelua:



- _Just in time -kanavat_ - kun sinulla ei ole yhtään kanavaa avoinna tai saapuvaa likviditeettiä käytettävissä, jos palvelu on aktivoitu, se avaa sinulle kanavan lennossa. Tämän vaihtoehdon voi poistaa käytöstä, jos et halua avata lisää tämäntyyppisiä kanavia.
- _Kanavien tilaaminen etukäteen_ - voit ostaa saapuvia kanavia Olympus LSP:ltä suoraan sovelluksesta useilla eri vaihtoehdoilla ja määrillä (saapuvia ja lähteviä kanavia varten).


LSP auttaa yhdistämään käyttäjät Lightning Network:ään avaamalla maksukanavat niiden solmukohtiin. [Lue lisää LSP:stä täältä](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUSiin on integroitu uusi LSP nimeltään [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), joka on kaikkien uutta sulautettua solmua käyttävien käyttäjien käytettävissä.


Tässä osiossa on oletuksena Olympus LSP (https://0conf.lnolymp.us), mutta pian voit myös asettaa toisen 0conf LSP:n, joka tukee tätä protokollaa.


_Keep in mind:_

_Kun avaat kanavan Olympus LSP:n kanssa käyttämällä käärittyjä LN-laskuja, saat myös 100k saapuvaa likviditeettiä ! Tämä on todella hyvä vaihtoehto, jos tarvitset heti lisää Sats:ta. _

esimerkki: talletat 400k Sats avataksesi LSP-kanavan, jolloin LSP avaa 500k Sats kapasiteettikanavan Zeus-solmuun ja työntää tallettamasi 400k Sats omalle puolellesi._

_"Sisäänpäin suuntautuva likviditeetti" = enemmän "tilaa" kanavassasi vastaanottaa._


Tulevaisuudessa toivomme, että meillä voisi olla monia muita LSP:tä, jotka voitaisiin integroida Zeukseen ja käyttää vaihtoehtoisesti kutakin. On vain ajan kysymys, kunnes uudet LSP:t ottavat käyttöön avoimen standardin tällaisille 0conf-kanaville.


Jos et halua avata uusia kanavia "lennossa", voit poistaa tämän vaihtoehdon käytöstä.


Tässä samassa osiossa voit myös valita vaihtoehdon "Pyydä yksinkertaisia Taproot-kanavia", kun LSP avaa kanavan Zeus-solmua kohti. Nämä yksinkertaiset Taproot-kanavat tarjoavat paremman On-Chain-salaisuuden ja pienemmät maksut kanavan sulkemisen yhteydessä. On vain kaksi syytä, miksi et halua käyttää niitä:



- Ne ovat uusia, ja LND:ssä voi vielä olla virheitä, kun niitä käytetään.
- Vastapuolesi ei tue niitä. Jopa LND-solmujen on toistaiseksi nimenomaisesti valittava ne.


**2 - Maksuasetukset**


Tämä ominaisuus tarjoaa sinulle mahdollisuuden asettaa omat haluamasi maksut LN:n kautta tai ketjussa tapahtuville maksuille. Voit myös lisätä tai vähentää laskujen aikakatkaisuaikaa.


Jos osa LN-maksuistasi epäonnistuu, voit korottaa maksua paremman reitin löytämiseksi. Myös jos teet onchain-tx:iä, voit asettaa tietyn maksun, jotta tx:si ei jäisi jumiin Mempool:ään pitkäksi aikaa, jos maksujen määrä on korkea.


**3 - Laskujen asetukset**


Tässä osiossa on joitain vaihtoehtoja generate-laskuille:



- Aseta vakiomuistio näytettäväksi Invoice:ssa generate:ssä
- Vanhentumisaika sekunteina, jos haluat tietyn ajan, pidemmän tai lyhyemmän Invoice:n maksettavaksi
- Sisällytä reittivihjeitä - anna tietoa mainostamattomien tai yksityisten kanavien löytämiseksi. Tämä mahdollistaa maksujen reitittämisen solmuihin, jotka eivät ole julkisesti näkyvissä verkossa. Reittivihje tarjoaa osittaisen reitin vastaanottajan yksityisen solmun ja julkisen solmun välillä. Tämä reititysvihje sisällytetään sitten vastaanottajan tuottamaan Invoice:ään, joka toimitetaan maksajalle. Suosittelen, että se on oletusarvoisesti käytössä, sillä muuten saapuvat maksut voivat epäonnistua (reittiä ei löydy).
- AMP Invoice - Atomic Multi-path Payments on LND:lla toteutettu uudentyyppinen salamamaksutyyppi, jonka avulla Sats:n voi vastaanottaa ilman tiettyä Invoice:tä [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). On käytännössä staattinen maksukoodi. [Lue lisää täältä](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Näytä mukautettu esikuvakenttä - käytä tätä vaihtoehtoa vain hyvin erityisissä tapauksissa, kun haluat todella käyttää mukautettuja kenttiä esikuvassa. [Lue lisää täältä](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Toinen vaihtoehto tässä osiossa on se, miten voit määrittää haluamasi onchain Address -tyypin: SegWit, SegWit, Taproot.


![Image](assets/en/04.webp)


Napsauta ylintä pyöräpainiketta, jolloin avautuu ponnahdusikkuna, josta voit valita haluamasi Address-tyypin. Kun olet asettanut sen, kun seuraavan kerran painat vastaanottopainiketta onchainia varten, se generate valitsee valitun Address-tyypin. Voit muuttaa sitä milloin tahansa.


**4 - Kanavien asetukset**


Tässä osiossa voit esiasettaa joitakin avauskanavien ominaisuuksia, kuten:



- vahvistusten määrä
- Ilmoita kanava (oletusarvoisesti on pois päältä), mikä tarkoittaa, että se on ilmoittamaton kanavat
- Yksinkertaiset Taproot-kanavat
- Näytä kanavan ostopainike


**5 - Yksityisyysasetukset**


Täältä löydät joitakin perusasetuksia, joilla voit lisätä yksityisyyttä Zeus-sovelluksen avulla:



- Block explorer avaa tx-tiedot (Mempool.space, blockstream.info tai mukautettu henkilökohtainen)
- Lue leikepöytä - päälle/pois -vaihtoehto, jos haluat Zeuksen lukevan laitteesi leikepöydän
- Lurker-tila - päälle/pois-vaihtoehto, jos haluat piilottaa tiettyjä arkaluonteisia tietoja Zeus-sovelluksestasi. On hyvä vaihtoehto, kun teet demoja tai kuvakaappauksia.
- Mempool-maksuehdotus - aktivoi tämä vaihtoehto, jos haluat käyttää [Mempool.space](https://Mempool.space/) suositeltuja maksutasoja


**6 - Turvallisuus**


Tässä osiossa on vain kaksi vaihtoehtoa sovelluksen suojaamiseksi avaamisen yhteydessä: salasanan tai PIN-koodin asettaminen.


Kun olet asettanut PIN-koodin sovelluksen avaamista varten, voit myös asettaa "pakkokoodin". Tätä salaista ylimääräistä PIN-koodia käytetään AINOASTAAN pakkotilanteessa, jos sinua uhataan. Jos laitat tämän PIN-koodin, kaikki asetukset pyyhitään pois. Joten sinun on parasta pitää varmuuskopiot ajan tasalla. Automaattiset varmuuskopiot ovat oletusarvoisesti päällä, mutta on hyvä, että sinulla on myös omat varmuuskopiot laitteesta.


**7 - Valuutta**


Ota käyttöön tai poista käytöstä mahdollisuus näyttää fiat-valuutan muuntaminen Zeus-sovelluksen käytössä. Tällä hetkellä se tukee yli 30 maailmanlaajuista fiat-valuuttaa.


**8 - Kieli**


Voit vaihtaa useiden käännöskielten välillä, jotka Zeus-yhteisö on tarkistanut äidinkielisten puhujien kanssa.


**9 - Näyttö**


Tässä osiossa voit muokata Zeuksen näyttöä valitsemalla erilaisia väriteemoja, oletusnäytön (näppäimistö tai tasapaino), näyttää solmun aliaksen, aktivoida isot näppäimistöpainikkeet, näyttää enemmän desimaalipaikkoja.


**10 - Myyntipiste**


Tämä on erikoisominaisuus, jolla voit ottaa käyttöön tai poistaa käytöstä Zeukseen integroidun PoS-järjestelmän. Voit käyttää itsenäistä PoS-järjestelmää tai yhdistää sen Square PoS-järjestelmään. Tällä hetkellä se tukee perustoimintoja PoS:nä, mutta se riittää hyvään alkuun ja voisi auttaa pieniä kauppiaita (baareja/ravintoloita, ruokakauppoja) aloittamaan BTC:n hyväksymisen natiivilla tavalla.


Näissä asetuksissa on useita vaihtoehtoja, joilla voit määrittää PoS:n:



- Vahvistusmaksun tyyppi: Vain LN, 0-conf, 1-conf
- Ota vinkit käyttöön / poista ne käytöstä kassalla työskentelevälle työntekijälle
- Näytä / piilota näppäimistö
- Lippuun sovellettava veroprosentti
- Luo tuotteita ja tuoteryhmiä
- Yksinkertainen luettelo kaikesta myynnistä


Tässä on live-demovideo Zeus PoS:n käytöstä:


**B - Wallet:n varmuuskopio**


ZEUSin sulautettu solmu perustuu LND:een ja käyttää [aezeed seed -formaattia] (https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Tämä on erilainen kuin tyypillinen [BIP39-muoto](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki), joka esiintyy useimmissa Bitcoin-lompakoissa, vaikka se saattaa vaikuttaa samankaltaiselta. Aezeed sisältää joitain lisätietoja, kuten Wallet:n syntymäpäivän, jotka auttavat palauttamisen aikana tehtäviä uudelleenkuvauksia tehostamaan.


Aezeed-avaimen muodon pitäisi olla yhteensopiva seuraavien mobiililompakoiden kanssa: Blixt, BlueWallet ja Breez. Huomaa, että pelkkä seed ei riitä palauttamaan kaikkia saldojasi, jos sinulla on avoimia tai vireillä olevia sulkemiskanavia !


Lisätietoja varmuuskopiointi- ja palautusprosessista on [Zeus Docs -sivulla](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


VALTAKUNNALLINEN NEUVONTA: Kun tallennat seed:n, tallenna myös solmun julkistusavain! Joskus on hyvä pitää se käsillä yhdessä seed:n ja SCB:n (Static Channels Backup) kanssa siltä varalta, että sinun on tarkistettava palautus.


SCB on tarpeen vain, jos LN-kanavat ovat auki. Jos sinulla on vain onchain varoja, ei ole tarpeen.


Jos huomaat, että pitkän ajan jälkeen ei vieläkään näy vanhaa historiaa txs, mene Embedded node - Peers ja poistaa vaihtoehto käyttää luetteloa valittujen vertaisryhmien (oletuksena on btcd.lnolymp.us). Tämä käynnistää uudelleen ja muodostaa yhteyden ensimmäiseen käytettävissä olevaan neutriinosolmuun, jolla on parempi aikavaste. Tai käytä alla mainittuja muita tunnettuja neutriinon vertaisvertaisverkkoja.


Jos haluat nähdä lisää palautusvaihtoehtoja LND-solmulle, [lue edellinen oppaani](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), jossa kerrotaan, miten tuodaan tyhjennetty seed Sparrow Wallet:een tai muilla menetelmillä.


**C - Sulautettu solmu**


Tässä osassa on joitakin perustyökaluja integroidun solmun hallintaan:



- _Disaster Recovery_ - LN-kanavien automaattiset ja manuaaliset varmuuskopiot. Lue lisää tämän ominaisuuden käytöstä Zeus Docs -sivulta.
- _Express Graph Sync_ - Zeus-sovellus lataa LN-juorutietojen kuvaajan omalta palvelimelta nopeampaa ja parempaa synkronointia varten ja tarjoaa parhaat maksupolut. Voit myös valita, että aiemmat kuvaajatiedot tyhjennetään käynnistyksen yhteydessä.
- _Peers_ - osio neutriino- ja 0-conf-vertaisryhmien hallintaa varten. Jos sinulla on ongelmia alkuperäisen synkronoinnin kanssa, kanavat eivät tule verkkoon, se johtuu siitä, että laitteellasi on suuri viive konfiguroidun neutriinopiirin kanssa.  Tunnettuja neutriinopalvelimia ovat:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - Yhdysvaltain aluetta varten
 - sg.lnolymp.us - Aasian alueelle
 - btcd-Mainnet.lightning.computer - Yhdysvaltain alueelle
 - uswest.blixtwallet.com (Seattle) - Yhdysvaltain alueeseen
 - europe.blixtwallet.com (Saksa) - EU:n alueella
 - asia.blixtwallet.com - Aasian alueeseen
 - node.eldamar.icu - Yhdysvaltain alueella
 - noad.sathoarder.com - Yhdysvaltain alueelle
 - bb1.breez.technology | bb2.breez.technology - Yhdysvaltain alueelle
 - neutrino.shock.network - Yhdysvaltain alue



- _LND-lokit_ - erittäin hyödyllinen työkalu LN-solmun ongelmien vianmääritykseen ja teknisen tason ongelmien syvälliseen valvontaan.
- _Advanced settings_ - lisää työkaluja LND-solmun käytön hallintaan:



 - _Pathfinding mode_ - bimodaalinen tai apriori, tapoja löytää parempi reitti LN-maksuille ja myös edellisen reittitiedon nollaaminen. Lue nämä erittäin hyvät oppaat polunhakutoiminnoista: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - kirjoittanut Docs Lightning Engineering ja [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - kirjoittanut Voltage
 - _Pysyvä LND_ - aktivoi tämä tila, jos haluat LND-palvelun toimivan jatkuvasti taustalla ja pitävän solmun verkossa 24/7. Tämä on erittäin hyödyllistä, jos käytät Zeusta PoS:nä pienessä kaupassa tai jos saat paljon LN-vihjeitä LN Address:n kautta.
 - _Tarkista lompakko_ - tämä vaihtoehto käynnistää uudelleenkäynnistyksen yhteydessä Wallet:n kaikkien ketjussa olevien tx:ien täydellisen tarkistuksen. Aktivoi se vain siinä tapauksessa, että Wallet:sta puuttuu joitakin tx:iä. Uudelleentarkistus vie aikaa, useita minuutteja, joten ole kärsivällinen ja tarkista aina lokitiedot nähdäksesi tarkemmat tiedot edistymisestä.
 - _Compact Database_ - tämä vaihtoehto on erittäin hyödyllinen, jos Zeus-sovelluksesi vie paljon tilaa laitteelta (katso sovelluksen tiedot laitteen asetuksista). Jos Zeuksen käyttö on vilkasta, suosittelen tekemään tämän tiivistämisen useammin. Kun näet, että Zeus-sovelluksen tiedot ovat yli 1-1,5 Gt, tee tiivistäminen. Se käynnistyy uudelleen ja kestää jonkin aikaa, joten ole kärsivällinen.
 - _Delete Neutrino files_ - tämä vaihtoehto poistaa neutriinotiedostot (uudelleenkäynnistyksen yhteydessä) vähentää huomattavasti tietojen tallennuskäyttöä. Datan käytön vähentämisellä on myös suuri vaikutus akun käyttöön, mikä vähentää akun käyttöä, varsinkin jos käytät Zeusta pysyvällä tilalla.


**D - Solmun tiedot**


Tässä osiossa löydät lisätietoja Zeus-solmusi tilasta seuraavasti:



- Alias - lyhyt solmun tunnus
- Julkinen avain - solmusi täydellinen julkinen avain, jota muut solmut tarvitsevat löytääkseen polun kohti solmua. Muista, että tämä julkinen avain EI näy tavallisissa LN Explorereissa (Mempool, Amboss, 1ML jne.). Tämä julkinen avain on saavutettavissa AINOASTAAN yhdistettyjen LN-vertaisverkkojen ja -kanavien kautta.
- LN-toteutuksen versio
- Zeus-sovelluksen versio
- Synkronoitu ketjuun ja Synkronoitu graafin tilaan - erittäin tärkeitä, sillä ne näyttävät solmun oikean tilan. Jos nämä kaksi eivät näytä "true", se tarkoittaa, että solmusi synkronointi on vielä kesken tai että synkronoinnissa on ongelmia. On siis suositeltavaa tutkia LND-lokeja tai odottaa vielä vähän aikaa.
- Lohkon korkeus ja Hash - näyttää viimeisimmän lohkon ja Hash:n, jonka solmusi näki ja synkronoi.


**E - Verkkotiedot**


Tässä osiossa näytetään lisätietoja Lightning Network:n yleisestä tilasta, jotka on poimittu graafin synkronointitiedoista: käytettävissä olevien julkisten kanavien määrä, solmujen määrä, zombie-kanavien määrä (offline tai kuollut), graafin läpimitta, keskimääräinen ja maksimiaste graafissa.


Nämä tiedot voivat olla hyödyllisiä vianmäärityksessä tai niitä voidaan käyttää vain tilastoihin.


**F - Salama Address**


Tässä osiossa käyttäjä voi perustaa oman LN Address @zeuspay.com -palvelun.


ZEUS PAY hyödyntää käyttäjien luomia esikuva-hasheja, HODL-laskuja ja Zaplocker Nostr -todennusjärjestelmää, jotta käyttäjät, jotka eivät välttämättä ole verkossa 24/7, voivat vastaanottaa maksuja staattiseen Address-salamaan. Käyttäjien on vain kirjauduttava sisään ZEUS-lompakkoihinsa 24 tunnin kuluessa lunastaakseen maksut, muuten ne palautetaan lähettäjälle.


Jos aktivoit "pysyvän tilan", kaikki maksut LN Address:een vastaanotetaan välittömästi.


Lue lisää siitä, miten [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) maksut toimivat ja lisää [ZeusPayn maksuista täällä](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain-osoitteet**


Tässä osiossa voit kuulla luotuja onchain-osoitteita parempaa kolikon hallintaa varten


**H - Yhteystiedot**


Zeus v 0.8.0:ssa esiteltiin uusi yhteystietokirja, jonka avulla voit lähettää nopeasti maksuja ystävillesi ja perheellesi, ja voit myös tuoda yhteystietosi Nostrista.


Syötä vain Nostr npub tai ihmisluettavissa oleva NIP-05 Address, ja ZEUS kysyy Nostrista kaikki yhteystietosi. Sieltä voit lähettää pikamaksun yhteystiedolle tai tuoda kaikki tai valitut yhteystiedot paikalliseen yhteystietokirjaasi./<<


Tässä on lyhyt video Zeus-yhteystietojen määrittämisestä ja käytöstä:


**I - Työkalut**


Täällä on useita alaosioita, joissa on lisää työkaluja:



- _Tilit_ - tästä voit tuoda ulkoisia tilejä / lompakoita, Cold-lompakoita, Hot-lompakoita, hallita tai käyttää ulkoisena rahoituslähteenä Zeus-solmun kanaville. Tämä ominaisuus on vielä kokeellinen.
- _Tapahtuman nopeuttaminen_ - Tämä ominaisuus voi olla hyödyllinen, kun lähetys Mempool:een on jumissa ja haluat nostaa maksun. Sinun on annettava tx-tuloste tx-tiedoista ja valittava haluamasi uusi maksu, jota haluat käyttää. Sen on oltava korkeampi kuin edellisen, ja se edellyttää, että sinulla on enemmän varoja käytettävissäsi onchain Wallet:ssä.


![Image](assets/en/05.webp)


Sinun on mentävä vireillä olevaan tx:ään ja kopioitava txid-ulostulopiste. Tule sitten tähän osioon ja liitä se, valitse sitten uusi maksu, jota haluat käyttää bumpiin. Se avaa uuden näytön, jossa on suositellut maksut sillä hetkellä, tai voit asettaa mukautetun maksun. Muista, että sen PITÄÄ olla korkeampi kuin edellisen.


On aina parempi pitää UTXO, jolla on enintään 100k Sats Zeus onchain Wallet:ssä, jotta sitä voidaan käyttää maksujen nostamiseen tarvittaessa.



- _Signoi tai vahvista_ - Tämän toiminnon avulla voit allekirjoittaa tietyn viestin Wallet-avaimillasi. Sitä voidaan käyttää myös viestin todentamiseen sen osoittamiseksi, että se on peräisin tietyistä Wallet-avaimista.
- _Currency converter_ - yksinkertainen työkalu BTC:n ja muiden fiat-valuuttojen välisen muuntokurssin laskemiseen.


**J - Tavarat ja tuki**


Täältä löydät lisätietoja ja linkkejä Zeuksesta, verkkokaupasta, sponsoreista ja sosiaalisesta mediasta.


**K - Apua**


Tästä viimeisestä osiosta löydät linkit Zeuksen dokumentointisivulle, Github-kysymyksiin (jos haluat lähettää bugin tai pyynnön suoraan sovelluskehittäjille) ja sähköpostitukeen.



### VAIHE 2 - ALOITA ZEUS-SOLMUN KÄYTTÖ



Muista, että Zeus on tarkoitettu käytettäväksi pääasiassa LN Wallet:n kanssa, jotta maksujen suorittaminen LN:n kautta olisi helppoa ja nopeaa. Toki se sisältää myös onchain Wallet:n, mutta sitä tulisi käyttää yksinomaan LN-kanavien avaamiseen/sulkemiseen eikä kahvin säännöllisiin maksuihin.


Lue toinen oppaani [kuinka olla oma pankkisi Stash:n kolmen tason avulla] (https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Tällä hetkellä käyttäjällä on kaksi tapaa aloittaa Zeuksen käyttö:



- Suoraan LN:n kautta Olympus LSP:n 0-conf-kanavaa käyttäen
- Talleta ensin onchain Wallet:ään ja avaa sitten normaali LN-kanava haluamallesi vertaisversiolle.


#### Menetelmä A - Olympus LSP:n käyttö


Tämä on erittäin helppo ja suoraviivainen tapa ottaa uusi LN-käyttäjä käyttöön Zeuksen kanssa. Kyseessä voi olla täysin uusi Bitcoin-käyttäjä, jolla ei ole lainkaan Sats:tä, jonka ystävä on ottanut mukaan tai uusi kauppias, joka aloittaa ensimmäisen LN-maksunsa.


Oletusarvoisesti Zeus käyttää omaa LSP:tä, Olympusta. Myöhemmin voit kuitenkin vaihtaa kanavien avaamiseen myös muita LSP:itä, jotka tukevat tätä 0-conf-protokollaa.


Luomalla yksinkertaisesti Invoice:n Zeuksellesi (laita summa ja napsauta "Pyydä"-painiketta), voit saada nämä Sats:t heti.


Invoice:n generate:lle tehdään [kääre](https://docs.zeusln.app/lsp/wrapped-invoices), ja sinulle esitetään palveluun liittyvät maksut, jos ne on maksettu. Tämä kääritty Invoice sisältää reittivihjeitä Zeus-solmusi suuntaan, joten LSP voi löytää uuden solmusi ja avata kanavan tallettamillesi uusille varoille.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Saadaksesi LSP:ltä LN-kanavan, jossa on varat, jotka haluat vastaanottaa 1. kerran, tämä Invoice on maksettava toisesta LN Wallet:stä ja odotettava hetki, kunnes LSP avaa kanavan Zeus-solmuun, vähentää maksun ja työntää jäljellä olevan maksun omalle puolellesi kanavaa.


Sinun tarvitsee vain maksaa sinulle ZEUSissa luotu Invoice toisella salamayhteydellä Wallet, ja kanavasi avautuu välittömästi. [Tutustu Zeuksen LSP-maksuihin](https://docs.zeusln.app/lsp/fees).


Toinen kanavasta maksamisen etu on maksuttomuus. Tämä tarkoittaa, että kun maksuja reititetään, ensimmäinen siirto OLYMPUS by ZEUSin kautta ei aiheuta reititysmaksuja. Huomaa, että OLYMPUS by ZEUSin jälkeisistä siirtymisistä veloitetaan silti.


Kun kanava on valmis, napsauta oikeaa painiketta näytön alareunassa, joka näyttää Zeus-kanavat.


![Image](assets/en/08.webp)


Näet tällaisen kanavan, jossa näkyy sinun puolesi kanavan tasapainosta:


![Image](assets/en/09.webp)


Mitä enemmän käytät tästä kanavasta, sitä enemmän sinulla on saapuvaa likviditeettiä. Mitä enemmän Sats:tä saat tähän kanavaan, sitä vähemmän sinulla on saapuvaa likviditeettitilaa.


Tässä on hieno yksinkertainen visuaalinen esittely (Rene Pickhardt) siitä, miten LN-kanavat toimivat:


Tällä hetkellä, kun kanavien esittelynäyttöä tarkastellaan, napsauta kanavan nimeä, niin näet lisätietoja kanavasta.


Sinulla on Olympuksen kanssa yksi kanava, jonka kokonaiskapasiteetti on 490 000 Sats, ja sinun puolellasi on 378 000 Sats ja Olympuksen puolella 88 000 Sats. Tämä tarkoittaa, että voit vastaanottaa enintään 88k Sats lisää samalla kanavalla.


Jos haluat vastaanottaa enemmän kuin 88k Sats (tässä tapauksessa käytettävissä oleva saapuva likviditeetti), esimerkiksi 500k Sats, luomalla yksinkertaisesti uuden LN Invoice:n kyseisellä määrällä, käynnistät uuden kanavapyynnön Olympus LSP:lle. Saat siis toisen kanavan.


Siksi, jotta vältyttäisiin useiden kanavien avaamisesta aiheutuvilta lisämaksuilta, on suositeltavaa avata ensin suurempi kanava, esimerkiksi 1-2M Sats. Kun se on avattu, voit vaihtaa osan näistä Sats:stä, vaikkapa 50 %, ketjussa olevaan ketjuun käyttämällä mitä tahansa tässä oppaassa kuvattua ulkoista vaihtopalvelua.


Kun olet vaihtanut tuosta kanavasta vaikkapa 50 % ja saanut Sats:n takaisin omaan Zeus onchain Wallet:aan, olet valmis siirtymään seuraavaan menetelmään uuden kanavan avaamiseksi - onchain-tasapainosta.


#### Menetelmä B - Onchain-saldon käyttäminen


Tällä menetelmällä voit avata kanavia mihin tahansa toiseen LN-solmuun, myös samaan Olympus LSP:hen. Mutta jos sinulla on jo kanava Olympuksen kanssa, on suositeltavaa, että sinulla on kanava myös toisen solmun kanssa, koska se lisää luotettavuutta ja voit myös käyttää MPP:tä (multi-part payment).


![Image](assets/en/10.webp)


Yllä on esimerkki LN Invoice:n maksamisesta MPP:n avulla. Kuten näet, näytön alareunassa on "asetukset", ja se avaa avattavan sivun, jossa on lisätietoja maksusta, jonka aiot suorittaa. Jos sinulla on vähintään kaksi kanavaa auki, MPP-ominaisuus on oletusarvoisesti päällä. Voit myös aktivoida AMP:n (atomic multi-path) ja asettaa tietyt haluamasi osat. Tämä on tehokas ominaisuus!


Zeuksen kaltaiselle yksityiselle solmulle suosittelen 2-3 hyvää kanavaa (enintään 4-5), joilla on hyvät LSP:t ja hyvä likviditeetti, jotta ne kattavat kaikki tarpeesi maksaa tai vastaanottaa Sats LN:n kautta. [Katso lisää LN-solmun likviditeettineuvoja tästä oppaasta](/nodes/managing-lightning-node-liquidity-en.html). Myös tässä toinen [yleinen opas LN-likviditeetistä](https://Bitcoin.design/guide/how-it-works/liquidity/) Bitcoin-suunnittelutiimiltä.


Tiedän, että oikeiden vertaisryhmien valitseminen ei ole helppo tehtävä edes kokeneille käyttäjille. (https://github.com/ZeusLN/zeus/discussions/2265), nämä ovat vertaisverkkosolmuja, joita testasin itse Zeuksen avulla (yritin muodostaa yhteyden vain LND-solmuihin, jotta vältyttäisiin yhteensopimattomuusongelmilta)


Täällä on myös luettelo Zeuksen varmennetuista solmupisteiden vertaisvertaisverkoista. Jos tiedät hyviä, voit lisätä ne tähän luetteloon.


Voit avata kanavan Zeuksessa siirtymällä Kanavat-näkymään napsauttamalla kanavakuvaketta päänäkymän oikeassa alakulmassa ja painamalla sitten +-kuvaketta oikeassa yläkulmassa.


![Image](assets/en/11.webp)


Jos haluat avata kanavan tietyn solmun kanssa, napsauta (A) yläkulmaa skannataksesi solmun QR-nodeID:n (Mempool, Amboss, 1ML:llä saat tämän QR:n), ja kaikki vertaisverkon tiedot täytetään.


MUISTUTUS:


- Zeus sulautettu solmu ei käytä Tor-palvelua ! Joten älkää yrittäkö avata kanavia solmujen kanssa, jotka ovat Torin alla! Teet enemmän vahinkoa itsellesi kuin lisäät yksityisyyttä. Tor for LN se ei tarjoa lisää yksityisyyttä vaan lisää ongelmia.
- valitse viisaasti vertaisesi, parempi olla hyviä LSP:tä, hyviä reitityssolmuja, ei satunnaisia pleb-solmuja, jotka voivat sulkea kanavasi eivätkä voi tarjota hyvää likviditeettiä. [Täällä kirjoitin oman oppaan](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) likviditeetistä ja esimerkkejä solmuista.


Jos napsautat suoraan painiketta "Open Channel to Olympus" (Avaa kanava Olympukselle), täytät tarvittavat kentät kanavan avaamiseksi [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Toisin kuin maksulliset LSP-kanavat, kanavasi vaatii On-Chain-vahvistuksen, jossa käytetään ketjussa olevia varoja (voit valita UTXO-varojesi joukosta avoimen kanavan näkymässä); se ei avaudu heti. Tutustu ensin todellisiin Mempool-maksuihin ja säädä ne vastaavasti sen mukaan, kuinka nopeasti haluat avata kyseisen kanavan.


Ennen kuin painat kanavan avauspainiketta, siirrä lisäasetukset alaspäin:


![Image](assets/en/12.webp)


Sinun on myös varmistettava, että kanava on ilmoittamaton (yksityinen). Oletusarvoisesti vaihtoehto on pois päältä ilmoitetuille kanaville. Tätä vaihtoehtoa ei suositella aktivoitavaksi Zeuksen sulautetulle solmulle, se on hyödyllinen vain silloin, kun käytät Zeusta etäsolmun kanssa julkisena reitityssolmuna.


Toisin kuin maksulliset LSP-kanavat, et hyödy nollamaksullisesta reitityksestä avaamalla kanavia tällä menetelmällä.


Ja valmis, klikkaa vain painiketta "Open Channel", odota, että kaivostyöläiset vahvistavat tx:n. Kun kanava on avattu, voit tehdä haluamasi liiketoimet Sats:n kanssa kanavistasi.


Muista, että näillä kanavilla on kaikki tasapaino SINUN puolellasi, joten sinulla ei ole sisäänpäin suuntautuvaa likviditeettiä. Kuten sanoin aiemmin, vaihda tai käytä Sats:a ostamalla tavaraa LN:n yli, jotta saat "lisää tilaa" vastaanottamista varten.


Ajattele LN-kanavia vesilasina. Kaadat vettä (Sats) tyhjään lasiin (kanavasi), kunnes se täyttyy. Et voi kaataa lisää vettä, ennen kuin juot vähän (kulutat/vaihdat). Kun lasi on melkein tyhjä, kaada siihen lisää vettä (Sats) käyttämällä swap-in. [Lue lisää ulkoisista vaihtopalveluista täältä](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


On myös muita LSP-palveluja, jotka myyvät sinulle saapuvia kanavia: LNBig tai Bitrefill. Luulen, että on muitakin tällaisia palveluja, mutta en muista niitä juuri nyt.


Jos siis tarvitset käytännössä tyhjän LN-kanavan (saldo on alusta alkaen 100 % vertaispuolella), jotta voit vastaanottaa enemmän maksuja kuin pystyt käsittelemään olemassa olevilla, täynnä olevilla kanavillasi, tämä voi olla erittäin hyvä vaihtoehto. Maksat tietyn maksun näiden kanavien avaamisesta ja saat runsaasti saapuvaa tilaa.



## VINKKEJÄ JA NIKSEJÄ


### Saapuvan varannon rajoitukset


Juuri nyt joidenkin LN-koodin rajoitusten vuoksi ei ole mahdollista vastaanottaa täsmälleen sitä, kuinka paljon "Inbound"-kohdassa näkyy. Pidä aina mielessä, että sinun tulisi tehdä laskut hieman pienemmällä summalla, vastaavasti "Channel Local Reserve" -määrällä.


![Image](assets/en/13.webp)


Kuten näet yllä olevasta kuvasta, "saapuva" se näyttää, että voin edelleen vastaanottaa 5101 Sats, mutta itse asiassa tällä hetkellä on mahdotonta vastaanottaa enemmän. Ja voit havaita, että se on sama määrä kuin "Paikallinen varaus".


Muista siis, että kun teet laskuja vastaanotettavaksi, vilkaise myös kanaviesi likviditeettiä ja vähennä siitä paikallinen varaus, jos haluat viedä saatavien määrän äärirajoille.


### Nopea neuvo uusille käyttäjille, jotka aloittavat Zeus-solmun käytön:



- Tartu oikein uusiin kanaviin.


Jos esimerkiksi tiedät, että saat viikossa vaikkapa 1M Sats, avaa 2M Sats-kanava ja vaihda onchain Wallet:een tai toiseen (väliaikaiseen) LN-tiliin 50-60% lähtevästä likviditeetistäsi. Varaudu aina lisäämään likviditeettiä. Kun tarvitset lisää likviditeettiä takaisin Zeus-kanaviin, voit siirtää sitä takaisin säilytystileiltä.


Jos tiedät, että lähetät vaikkapa 500k Sats/viikko, avaa 1M Sats-kanava. Tällä tavoin sinulla on edelleen reserviä, kunnes täytät sen uudelleen.



- Jos olet kauppias ja saat aina enemmän kuin käytät säännöllisesti, osta oma saapuvan viestinnän kanava. Se on halvin tapa. Maksat minimaalisen maksun ja saat "tyhjän" kanavan.



- Älä avaa pieniä merkityksettömiä 50-100-300-500k Sats-kanavia. Täytät ne muutamassa päivässä, vaikka käyttäisitkin niitä vain zap-kanaviin. Avaa isompia ja erilaisia kanavia, ÄLÄ vain yhtä kanavaa.


Kun avaat isomman kanavan, voit aina käyttää ulkoisia sukellusvenevaihtoja Sats:n siirtämiseksi onchain-lompakoihin (myös takaisin Zeus onchainiin). Tasapainon säilyttäminen sisään- ja ulospäin suuntautuvan likviditeetin välillä on hyvä asia, ja lisäksi voit halutessasi "käyttää" näitä Sats:tä uudelleen avataksesi lisää kanavia.


### Kääritty Invoice


Jos haluat lisätä yksityisyyttä vastaanotossa, voit käyttää "kääritty Invoice" -menetelmää. Muistutus: jotta voit tehdä tämän, tarvitset kanavan, jossa on Olympus LSP. Kääritty lasku "piilottaa" lopullisen määränpään (Zeus-solmusi) ja näyttää LSP-solmusi määränpäänä maksajalle.


Saadaksesi käärityn Invoice:n mene näppäimistön päänäyttöön, laita summa ja paina request. Näyttää tavallisen QR-koodin Invoice:lle. Napsauta nyt oikeaa yläreunan "X"-painiketta, ja sinut ohjataan Invoice:n lisävaihtoehtoihin.


![Image](assets/en/14.webp)


Nyt sinun on aktivoitava yläreunassa oleva vaihtoehto "Enable LSP" ja painettava "Create Invoice" -painiketta. Tuo vaihtoehto luo käärityn Invoice:n ja muistaa, että se veloittaa pienen maksun.


### Laskut, joissa on reittivihjeitä


Tämä on erittäin hyödyllinen ominaisuus, jos haluat hallita useita saapuvien kanavien likviditeettiä. Käytännössä voit ilmoittaa, mihin saapuvaan kanavaan haluat vastaanottaa Sats:n Invoice:stä.


Tätä ominaisuutta voidaan käyttää myös ympyränmuotoiseen tasapainottamiseen, kun haluat siirtää likviditeettiä yhdestä täytetystä kanavasta toiseen tyhjentyneeseen kanavaan.


Miten luodaan Invoice reittivihjeiden avulla?



- Liu'uta päänäytössä LN-laatikkoa oikealle ja napsauta "Vastaanota"
- Siirry Invoice-asetuksissa alaosaan ja aktivoi painike "Insert route hints" (Lisää reittivihjeitä) ja valitse sitten "Custom" (Mukautettu) -välilehti. Se avaa näytön, jossa on kaikki käytettävissä olevat kanavat. Valitse se, jonka haluat vastaanottaa.
- Täytä kaikki muut Invoice:n tiedot, summa, muistio jne. ja napsauta "create Invoice".
- Jos maksat kyseisen Invoice:n, Sats tulee ilmoitetulle kanavalle.


Jos haluat maksaa itsellesi tuon Invoice:n (ympyränmuotoinen uudelleentasapainotus), kun maksat sen samasta Zeus-solmusta, valitse maksunäytössä lähtevä kanava (jossa on enemmän likviditeettiä), jota haluat käyttää maksun lähettämiseen.


### Maksa Keysendillä


Keysend on hyvin aliarvostettu LN:n ominaisuus, ja käyttäjien pitäisi käyttää sitä useammin.


[Keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) antaa Lightning Network:n käyttäjille mahdollisuuden lähettää maksuja muille suoraan heidän julkiseen avaimeensa, kunhan heidän solmullaan on julkiset kanavat ja keysend on käytössä. Keysend ei edellytä, että maksunsaaja antaa Invoice:n.


Miten se onnistuu Zeuksen kanssa?


Skannaa tai kopioi kohteen nodeID (tai käytä Zeuksen yhteystietoja tallentaaksesi tavalliset kohdesolmut yhteystietoina) ja napsauta sitten Zeuksen päänäytöltä "Lähetä"-painiketta. Liitä nodeID-numero kyseiseen näyttöön tai valitse se yhteystiedoistasi.


Laita Sats:n määrä, tarvittaessa viesti (kyllä, voit käyttää sitä myös salaisena keskusteluna LN:n kautta) ja napsauta "Lähetä"-painiketta. Valmis!


![Image](assets/en/15.webp)


Jos sinulla on suora kanava kohdekumppanin kanssa, maksuja ei peritä.


Jos sinulla ei ole suoraa kanavaa määränpään vertaisverkon kanssa, avaintenlähetysmaksu maksaa maksut tavallisena LN Invoice-maksuna, joka reititetään säännöllistä polkua pitkin kuten mikä tahansa muu maksu. Muista vain, että siitä ei jää mitään jälkiä LN Invoice:nä.


## Conlusion


Suosittelen lukemaan jatko-oppaan [Advanced usage of Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html), jossa on lisää ohjeita ja käyttötapauksia.


Ja... siinä se! Tästä lähtien voit käyttää Zeus Nodea tavallisena BTC/LN Wallet:nä kännykässäsi. Käyttöliittymä on melko suoraviivainen ja helppokäyttöinen, intuitiivinen kaikenlaisille käyttäjille, en usko, että minun tarvitsee syöttää lisää yksityiskohtia siitä, miten tehdä ja vastaanottaa maksuja.


Lopuksi tässä on yksityisyyden suojan vertailutaulukko :


![Image](assets/en/16.webp)