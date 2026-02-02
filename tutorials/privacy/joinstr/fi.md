---
name: Joinstr
description: Hajautetut CoinJoins Nostr-verkon kautta suvereenin Bitcoin-luottamuksellisuuden varmistamiseksi
---

![cover](assets/cover.webp)



Bitcoin-lohkoketjun läpinäkyvyys mahdollistaa transaktiohistorian jäljittämisen. CoinJoins katkaisee nämä yhteydet sekoittamalla useita samanaikaisia transaktioita, mikä palauttaa käteiseen verrattavan luottamuksellisuuden tason.



Perinteiset ratkaisut perustuvat kuitenkin keskitettyyn koordinaattoriin, joka on ainoa vikapiste. Wasabi ja Samourai lopettivat toimintansa vuonna 2024 sääntelyn painostuksesta.



**Joinstr** poistaa tämän heikkouden käyttämällä hajautettua Nostr-verkkoa koordinointiin. Tämä avoimen lähdekoodin sovellus mahdollistaa todella suvereenit CoinJoinsit, joissa mikään keskusviranomainen ei voi sensuroida, valvoa tai keskeyttää palvelua.



## Mikä on Joinstr?



Joinstr on avoimen lähdekoodin työkalu, joka mullistaa CoinJoins-lähestymistavan hyödyntämällä Nostr-protokollaa koordinointi-infrastruktuurina. Toisin kuin keskitetyt ratkaisut, jotka edellyttävät omaa palvelinta, Joinstr luottaa Nostr-relaysien hajautettuun verkkoon, jotta osallistujat voivat koordinoida suoraan vertaistensa välillä.



**Depentralisoitu arkkitehtuuri** : Nostr-verkko korvaa keskuskoordinaattorin. Osallistujat luovat "pooleja" tai liittyvät niihin lähettämällä salattuja ilmoituksia Nostrin releiden kautta. Nämä tiedot (määrät, osallistujat, osoitteet) pysyvät releiden ulottumattomissa, mikä varmistaa, ettei mikään keskusyksikkö voi valvoa, sensuroida tai suodattaa CoinJoineja.



**SIGHASH_ALL|ANYONECANPAY-mekanismi**: Joinstr hyödyntää tätä Bitcoin-allekirjoituslippua, jolloin kukin osallistuja voi allekirjoittaa vain oman syötteensä ja validoida kaikki tuotokset. Kukin käyttäjä luo PSBT:nsä paikallisesti ja jakaa sen sitten Nostrin kautta. Kukin käyttäjä luo PSBT:nsä paikallisesti, allekirjoittaa sen ja jakaa sen sitten Nostrin kautta. Bitcoinisi pysyvät yksinomaisessa hallinnassasi viimeiseen allekirjoitukseen asti.



**Filosofia**: Joinstr noudattaa Bitcoin cypherpunk-etiikkaa, jolla on kolme tavoitetta: **sensuurin vastustaminen** (mikään viranomainen ei voi pysäyttää palvelua), **täydellinen vapaudenriisto** (pidät yksityiset avaimesi) ja **tasa-arvoinen kohtelu** (ketään UTXO:sta ei saa syrjiä).



### Tärkeimmät ominaisuudet



**Joustavat altaat**: Toisin kuin kiinteät nimellisarvot, kuka tahansa käyttäjä voi luoda poolin täsmälleen haluamallaan summalla ja tavoitellulla osallistujamäärällä, mikä optimoi UTXO:n käytön ilman keinotekoista jakamista.



**Transparentit maksut**: Ei koordinointimaksuja. Ainoastaan Bitcoin-tapahtumamaksut jaetaan tasan osallistujien kesken (muutama tuhat satoshia per henkilö).



**Ephemeraliteetti**: Käyttäjätietoja ei säilytetä. Tiedot siirretään salattujen ephemeral Nostr -viestien välityksellä, jotka unohdetaan välittömästi tapahtuman jälkeen.



### Käytettävissä olevat alustat



Tässä oppaassa keskitytään **Android-sovellukseen**, joka on tällä hetkellä ainoa vakaa ja suositeltava ratkaisu. Electrum-lisäosa on olemassa, mutta sen yhteensopivuusongelmat tekevät siitä epävakaan. Verkkokäyttöliittymä on kehitteillä.



## Bitcoin Ydinkokoonpano



Joinstr Android vaatii yhteyden Bitcoin-solmuun RPC:n kautta. Sinun on ensin määritettävä tietokoneen Bitcoin Core niin, että se hyväksyy yhteydet puhelimesta.



**Huomautus**: Lisätietoja Bitcoin Core -ohjelman täydellisestä konfiguroinnista on erillisissä opetusohjelmissamme :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Verkkovaatimukset



#### Paikanna paikallinen IP-osoite



Android-puhelimen on voitava tavoittaa Bitcoin-solmun paikallisverkossa. Etsi tietokoneesi IP-osoite:



**MacOS:ssä** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Yksinkertainen vaihtoehto:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Linuxissa** :



```bash
hostname -I | awk '{print $1}'
```



**Windowsissa** :



```cmd
ipconfig
```



Etsi IPv4-osoite (muodossa `192.168.x.x.x` tai `10.0.x.x.x`)



### RPC kokoonpano



#### Muokkaa bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Etsi bitcoin.conf -tiedosto:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Avaa tiedosto suosikkitekstieditorillasi ja lisää tämä määritys RPC-palvelimen aktivoimiseksi.



**Suositeltu kokoonpano aloitusta varten (kirjanmerkki)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet**-konfiguraatio (tuotantokäyttöön) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Tärkeää** :




- Signet on erittäin suositeltava** ensimmäisiä testejä varten: sovellus on vielä kehitteillä (beta), ja virheitä voi vielä esiintyä. Signetin avulla voit testata ilmaiseksi, ilman että joudut riskeeraamaan todellisia varoja
- Korvaa `192.168.1.0/24` verkon aliverkolla (esim. jos IP-osoitteesi on `192.168.68.57`, käytä `192.168.68.0/24`)



**Turvallisuus**: Luo vahva salasana :



```bash
openssl rand -base64 32
```



### Alustaminen



#### Käynnistä uudelleen ja tarkista



1. Sammuta Bitcoin Core kokonaan


2. Käynnistä se uudelleen, jotta konfiguraatio otetaan käyttöön




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Kun Bitcoin Core käynnistyy ensimmäisen kerran, se lataa ja synkronoi kirjanmerkin lohkoketjun. Tämä toimenpide on paljon nopeampi kuin mainnet:ssä (vain muutama minuutti). Odota, kunnes synkronointi on valmis, ennen kuin jatkat.



![CRÉATION DE WALLET](assets/fr/04.webp)



Kun olet synkronoinut, luo uusi salkku napsauttamalla "Create a new wallet". Anna sille selkeä nimi, kuten `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet on nyt luotu ja valmis vastaanottamaan kirjanmerkittyjä bitcoineja testausta varten.



#### Hanki kirjanmerkittyjä bitcoineja (testi)



Testata Joinstr kirjanmerkki, tarvitset ilmainen testi bitcoins :



![SIGNET FAUCET](assets/fr/06.webp)



Käytä julkista kirjanmerkkiä, kuten :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Bitcoin Core -ohjelmassa generate:ssä uusi vastaanotto-osoite (välilehti "Receive"), kopioi se ja liitä se hanan lomakkeeseen. Ratkaise captcha tarvittaessa. Saat ilmaisia kirjanmerkittyjä bitcoineja muutamassa sekunnissa.



## Android-sovellus



### Asennus



![APPLICATION ANDROID](assets/fr/07.webp)



Siirry osoitteeseen [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) ladataksesi uusimman APK-version. Lataa tiedosto Android-selaimellasi ja avaa se käynnistääksesi asennuksen. Sinun on tarvittaessa sallittava asennus tuntemattomista lähteistä puhelimesi suojausasetuksissa.



### Sovelluksen konfigurointi



![PERMISSIONS VPN](assets/fr/08.webp)



Ensimmäisellä käynnistyskerralla Joinstr-sovellus kysyy oikeuksia sisäänrakennetun VPN:n hallintaan. Hyväksy molemmat lupapyynnöt: OpenVPN-ohjaus ja VPN-yhteys. Näitä oikeuksia tarvitaan VPN-integrointiin, joka suojaa verkkosi yksityisyyttä.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr-sovellus on järjestetty kolmeen päävälilehteen:




- Koti**: Aloitusnäyttö
- Uima-altaat**: CoinJoin-altaiden luominen ja hallinta
- Asetukset**: Sovelluksen konfigurointi



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Määritä asetukset "Asetukset"-välilehdellä:



**1. Nostorele**: Nostr relay-osoite poolin koordinointia varten




- Esimerkki: `wss://relay.damus.io`
- Muut suositellut releet: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Tärkeää**: Kaikkien osallistujien on käytettävä **samaa Nostr-releetä**, jotta he näkevät samat altaat ja voivat liittyä niihin. Jos käytät eri relettä, et näe muilla relelähtöillä luotuja pooleja



**2. Solmun URL-osoite**: Bitcoin-solmun IP-osoite (ilman porttia)




- Formaatti: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC Käyttäjätunnus** : Käyttäjänimi, joka on määritetty bitcoin.conf:n `rpcuser=`-kohdassa




- Esimerkki: `satoshi



**4. RPC Salasana** : bitcoin.conf:n kohdassa `rpcpassword=` asetettu salasana



**5. RPC-portti** : RPC-portti verkon mukaan




- Mainnet** : `8332`
- Kirjanmerkki**: `38332`



**6. Wallet**: Valitse Bitcoin Core portfolio, joka sisältää sekoitettavat UTXO:t




- Esimerkki: `tuto_joinstr_signet`



**7. VPN-yhdyskäytävä**: Valitse Riseup VPN-palvelin




- Esimerkki: `(Paris) vpn07-par.riseup.net`
- Muut saatavilla: Amsterdam, Seattle jne.
- ⚠️ **Tärkeää**: Kaikkien samaan pooliin kuuluvien osallistujien on käytettävä **samaa VPN-yhdyskäytävää** osallistuakseen CoinJoin:een. Sekoituskierroksen aikana kaikkien osallistujien on käytettävä samaa poistumis-IP-osoitetta, jotta verkkoanalyysi ei voi korreloida osallistujia



Joinstr-sovellus **integroi natiivisti** Riseup VPN:n, mikä yksinkertaistaa osallistujien välistä koordinointia.



**Tärkeää** :




- Varmista, että puhelin ja tietokone ovat samassa paikallisessa WiFi-verkossa
- VPN-yhteys aktivoituu automaattisesti, kun osallistut pooliin
- Napsauta **"Tallenna "**, kun olet asettanut kaikki parametrit



## Käytännön käyttö



### Luo pooli tai liity siihen



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Sinulla on kaksi vaihtoehtoa osallistua CoinJoin:ään:



**Vaihtoehto 1: Luo uusi allas**



Napsauta "Create New Pool" (Luo uusi allas) "Pools" -välilehdellä. Määritä nimellisarvo BTC:nä (esim. 0,002 BTC) ja haluttu osallistujien määrä (vähintään 2, suositellaan 3-5 osallistujaa anonymiteetin lisäämiseksi). Tämän jälkeen sovellus odottaa, että muut käyttäjät liittyvät pooliin. Kun vaadittu määrä on saavutettu, lähtörekisteröintiprosessi alkaa automaattisesti, ja sinun on valittava UTXO sekoitettavaksi ja napsautettava "Rekisteröidy".



**⏱️ Tärkeää**: Poolit vanhentuvat **10 minuutin** käyttämättömyyden jälkeen. Jos vaadittua osallistujamäärää ei saavuteta, pooli suljetaan automaattisesti.



**Vaihtoehto 2: Liity olemassa olevaan altaaseen**



Näytä muut altaat -välilehdellä voit selata muiden käyttäjien luomia käytettävissä olevia altaita. Valitse määrääsi vastaava allas ja liity siihen. Varmista, että olet määrittänyt saman Nostr relayn ja VPN-yhdyskäytävän kuin muut osallistujat (katso kohta Määritys).



**UTXO-valintasääntö**: UTXO:n on oltava hieman suurempi kuin poolin nimellisarvo (+500 ja +5000 sats:n välillä).



**Esimerkki**: Käytä 0,002 BTC:n (200 000 sats) poolille UTXO:a, joka on välillä 200 500 ja 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Prosessi on sen jälkeen **täysin automaattinen**: kun syötteesi on rekisteröity, sovellus odottaa, että kaikki osallistujat rekisteröivät syötteensä. Kun kaikki syötteet on rekisteröity, PSBT luodaan, allekirjoitetaan automaattisesti sinun avaimillasi ja yhdistetään sitten muiden osallistujien allekirjoituksiin. Lopuksi koko tapahtuma lähetetään Bitcoin-verkkoon. Saat TXID-tunnisteen (transaktion tunniste), kun lähetys on valmis. PSBT:n manuaalista käsittelyä ei tarvita Androidissa.



### on-chain-tarkastus



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Kun transaktio on lähetetty, saat TXID-tunnisteen (transaktion tunniste). Tarkastele sitä [mempool.space](https://mempool.space) tai suosikkiselaimellasi. Jos haluat testata kirjanmerkillä, käytä [mempool.space/signet](https://mempool.space/signet).



Voit tarkkailla :





- N merkintää**: Yksi osallistujaa kohti (esimerkissämme 2 osallistumista)
- N identtistä ulostuloa**: täsmällinen nimellisarvo (tässä 2 ulostuloa, joista kukin on 0,00199800 BTC)
- Virtauskaavio**: mempool.space näyttää visuaalisesti tulojen ja lähtöjen yhdistelmän
- Ominaisuudet** : Tapahtuma voidaan tunnistaa SegWit, Taproot, RBF jne.



Koska kaikilla pääulostuloilla on sama määrä, on **mahdotonta määrittää, mikä kuuluu kenellekin**. Tämä on CoinJoin:n perusperiaate: tuotosten erottamattomuus.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Huomaa**: Jos UTXO:t olivat suurempia kuin poolin nimellisarvo, sinulla on valuuttatuloja (ylijäämiä). Nämä UTXO:t ovat edelleen jäljitettävissä, ja niitä on hallinnoitava erillään nimettömistä tuotoistasi. Älä koskaan yhdistä niitä sekatuotoksiisi.



## CoinJoin laatu- ja anonymiteettipaketit



CoinJoin:n tehokkuutta mitataan sen **anonsetillä**: transaktion tuottamien samanarvoisten tuotosten lukumäärällä. Mitä suurempi tämä luku on, sitä vaikeampaa on määrittää, mikä panos vastaa mitä tuotosta.



Joinstr tuottaa tällä hetkellä keskimäärin **2-5 osallistujan** poolit. Nämä luvut ovat pienempiä kuin perinteisillä keskitetyillä koordinaattoreilla, kuten Wasabilla (50-100 osallistujaa) tai Whirlpool:llä (5-10 osallistujaa), mutta se on hajauttamisen hinta.



💡 **Jos haluat ymmärtää anonymiteettijoukkoja ja niiden laskentaa yksityiskohtaisesti**, katso koko kurssi: [Anonymiteettijoukot](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. muut CoinJoinsit




| Aspekti | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Osallistujat poolissa** | 50-100 | 5-10 | Muuttuva (P2P) | **2-5** |
| **Koordinaattori** | Keskitetty (suljettu 2024) | Keskitetty (aktiivinen) | P2P maker/taker | **Ei mitään (Nostr)** |
| **Sensuuri-vastustus** | Heikko | Keskitaso | Hyvin korkea | **Hyvin korkea** |
| **Koordinaatiomaksut** | Prosentti | Sisäänpääsymaksu | Maksettu tekijöille | **Ei mitään** |
| **UTXO-syrjintä** | Kyllä (mustat listat) | Ei | Ei | **Ei** |

💡 **Muut aktiiviset CoinJoin-liuokset** :




- Ashigaru**: Whirlpool-protokollan avoimen lähdekoodin toteutus, jossa on keskitetty koordinaattori, mutta joka voidaan ottaa käyttöön hajautetusti. Jatkaa toimintaansa Samourain Wallet:n haltuunoton jälkeen vuonna 2024.
- JoinMarket**: Hajautettu P2P-ratkaisu, jossa ei ole keskitettyä koordinaattoria ja joka perustuu maker/taker-liiketoimintamalliin, jossa "makerit" tarjoavat likviditeettiä ja "ottajat" maksavat siitä korvauksen.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Perusteellinen kompromissi**: Joinstr ja JoinMarket ovat ainoat kaksi ratkaisua, joissa ei ole keskuskoordinaattoria. JoinMarket käyttää P2P-liiketoimintamallia, johon liittyy taloudellisia kannustimia, kun taas Joinstr käyttää Nostria kustannuksettomaan koordinointiin. Joinstr uhraa välittömän laajamittaisen anonymiteetin yksinkertaisuuden (ei tekijöiden ja vastaanottajien hallintaa) ja koordinointimaksujen täydellisen puuttumisen hyväksi.



**Käytännön suositus**: Kompensoidaksesi pienemmät poolimäärät, suorita useita peräkkäisiä CoinJoin-kierroksia eri osallistujien kanssa. Vaihda kierrokset ajallisesti ja vaihda Nostr-releet jokaisen kierroksen välillä, jotta voit maksimoida luottamuksellisuuden.



Voit vapaasti tutustua täydelliseen kurssimme Bitcoinin yksityisyyden suojasta saadaksesi lisätietoja tästä aiheesta:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Edut ja rajoitukset



### Kohokohdat



**Lisätty yksityisyys**: Nostr-viestinnän salauksen, osallistujien välisen jaetun VPN:n ja suositellun Torin käytön yhdistelmä luo monikerroksisen suojan, jota on vaikea ohittaa.



**Yksinkertaiset, minimaaliset kustannukset**: Ei koordinointikustannuksia, ainoastaan mining-kustannukset jaetaan tasapuolisesti osallistujien kesken. Yksikään operaattori ei peri prosenttiosuutta.



### Huomioon otettavat rajoitukset





- Muuttuva likviditeetti**: Pienemmät poolit, voivat odottaa osallistujien kokoontumista yhteen
- Käynnissä oleva hanke**: Sovellus on beta-versiossa, virheet mahdollisia. Testaa ensin pienillä määrillä kirjanmerkkiä
- Sybil hyökkää**: Mahdollisuus, että yksi vastustaja hallitsee useita poolin osallistujia



## Parhaat käytännöt



**UTXO eristys**: Älä koskaan yhdistä sekoitettua UTXO:ää sekoittamattomaan UTXO:ään. Käytä erillistä salkkua anonymisoituja tuotoksia varten.



**Moninkertaiset kierrokset välttämättömiä**: Suorita vähintään 3 peräkkäistä kierrosta eri osallistujien kanssa. Vaihtele määriä ja ajoituksia mallien välttämiseksi. Kierrosten väli on useita tunteja.



**Verkon suojaus**: Käytä järjestelmällisesti Toria sisäänrakennetun VPN:n lisäksi. Luo lyhytaikaisia Nostr-avaimia jokaista tärkeää istuntoa varten.



**Varovainen edistyminen**: Aloita kirjanmerkkien lisääminen pienillä määrillä.



## Päätelmä



Joinstr edustaa aidosti hajautettua Bitcoin-yksityisyysratkaisua. Käyttämällä Nostria koordinointiin se poistaa riippuvuuden keskuskoordinaattoreista ja säilyttää samalla käyttäjien itsemääräämisoikeuden.



**Käyttäjille, jotka arvostavat sensuurin vastustamista ja ovat valmiita suorittamaan useita CoinJoin-kierroksia kompensoidakseen pienempiä altaita.



Taloudellisen valvonnan lisääntyessä hajautetuista työkaluista yksityisyyden suojaamiseksi on tulossa välttämättömiä.



## Resurssit



### Viralliset asiakirjat




- [Joinstrin virallinen verkkosivusto](https://joinstr.xyz)
- [Käyttäjän asiakirjat](https://docs.joinstr.xyz/users/using-joinstr)
- [Tekninen dokumentaatio](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLabin lähdekoodi](https://gitlab.com/invincible-privacy/joinstr)
- [Android-sovellus](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Oppaat




- [Electrum plugin opetusohjelma](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Täydellinen opas Sensuroimaton tekniikan avulla



### Yhteisö ja tuki




- [Telegram Joinstr Group](https://t.me/joinstr) - Yhteisön tuki ja kirjanmerkkikulmat
- [Tekninen keskustelu DelvingBitcoinista](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Lisätyökalut




- [Kirjanmerkki Faucet](https://signetfaucet.com) - Ilmainen testi Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet vaihtoehtoinen vaihtoehto
- [Mempool.space](https://mempool.space) - Block explorer ja yksityisyyden suojaa koskeva analyysi