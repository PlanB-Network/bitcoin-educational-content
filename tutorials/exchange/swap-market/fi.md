---
name: SwapMarket
description: Bitcoin ja Lightning swap-palvelujen aggregaattori
---

![cover](assets/cover.webp)



Varojen siirtäminen Bitcoin on-chain:n ja Lightning Network:n välillä edellyttää yleensä joko Lightning-kanavien avaamista manuaalisesti (mikä on teknistä ja kallista) tai keskitettyjen swap-alustojen käyttöä KYC:n kanssa. SwapMarket tarjoaa vaihtoehdon: luotettavat atomiset swapit kilpailukykyisten palveluntarjoajien kautta ilman KYC:tä.



Innovaatio: Vaikka palveluntarjoajat ovat välittäjiä, HTLC (*Hash Time Locked Contracts*) takaa matemaattisesti, että varasi pysyvät sinun hallinnassasi. Useiden palveluntarjoajien (Boltz, ZEUS Swaps, Eldamar, Middle Way) yhdistäminen luo hintakilpailua. Interface-verkkosivusto avoimen lähdekoodin itsehostettavissa.



## Mikä on SwapMarket?



SwapMarket on vuonna 2024 käynnistetty avoimen lähdekoodin aggregaattori, joka toimii Bitcoin/Lightning-swap-palveluntarjoajien vertailukohtana. Käyttäjä vertailee välittömästi ehtoja (maksut, likviditeetti, limiitit) ja valitsee optimaalisen palveluntarjoajan.



### Tekninen arkkitehtuuri



**Frontend-asiakaspuoli**: 100 % asiakaspuolen sovellus (fork Boltz Web App), joka sijaitsee GitHub-sivuilla. Koodi toimii selaimessa ilman backend-palvelinta. Historia tallennetaan paikallisesti (evästeet/ välimuisti). Julkinen ja tarkastettavissa oleva lähdekoodi.



**Palveluntarjoajan löytäminen** : Kovakoodattu lista tiedostossa `src/configs/mainnet.ts`. Uusia palveluntarjoajia lisätään Pull Requestilla tai sähköpostilla.



**Riippumattomat taustajärjestelmät**: Kullakin palveluntarjoajalla on oma Boltz-backend. Käyttöliittymä tekee reaaliaikaisia API-kyselyjä ja vertailee tarjouksia välittömästi.



**HTLC Atomic Swaps**: Hash Aikalukitut sopimukset takaavat atomisuuden: joko swap toteutuu tai kumpikin osapuoli saa varansa takaisin. Vastapuoliriski matemaattisesti eliminoitu.



### Filosofia



SwapMarket vähentää keskittämistä luomalla kilpailua palveluntarjoajien välille maksuista ja likviditeetistä. Ei KYC:tä, avoimen lähdekoodin itsehostattava koodi, riippumattomien operaattoreiden moninkertaistaminen yksittäisten vikapisteiden välttämiseksi.



## Tärkeimmät ominaisuudet



### Palveluntarjoajan markkinapaikka



Käyttöliittymässä näkyvät kaikki aktiiviset palveluntarjoajat: palveluntarjoajan nimi, sovellettavat maksut (prosentuaaliset ja/tai kiinteät), käytettävissä olevat vähimmäis- ja enimmäismäärät sekä tuetut swap-tyypit. Sovellus kysyy suoraan kunkin määritystiedostossa mainitun palveluntarjoajan API:ta saadakseen tarjoukset reaaliajassa. Palveluntarjoajien välinen kilpailu takaa optimaaliset hinnat, jotka ovat yleensä noin 0,5 % vakioswapeissa.



### Kaksisuuntaiset vaihdot



**Swap-in (on-chain → Lightning)**: Muunna on-chain BTC:t Lightning-satoseiksi. Käyttötarkoitus: wallet Lightningin käyttö, solmun saapuvan kapasiteetin hankkiminen tai välitön likviditeetti.



**Vaihtaminen (Lightning → on-chain)**: Muunna Lightning-satoshi on-chain BTC:ksi. Käyttötapaus: wallet Lightningin tyhjentäminen kylmävarastoon tai likviditeetin tasapainottaminen kerrosten välillä.



### Turvallisuus ja elpyminen



**Trustless atomivaihdot**: HTLC:t takaavat, että joko vaihto suoritetaan kokonaisuudessaan tai että kumpikin osapuoli saa panoksensa takaisin. Vastapuoliriski on matemaattisesti eliminoitu.



**Maksumekanismi**: Jokaisessa swapissa on aikalukko. Jos swap ei onnistu, varat palautetaan automaattisesti takaisin swapin päättymisen jälkeen. Käyttäjällä on aina mahdollisuus saada bitcoininsa takaisin.



**Palautusavaimet**: SwapMarketin avulla voit viedä palautusavaimia meneillään oleville vaihdoille. Ongelmatilanteessa näillä avaimilla voit viimeistellä tai peruuttaa vaihdon mistä tahansa laitteesta.



## Asennus ja pääsy



### Interface web



SwapMarket ei vaadi asennusta. Pääsy tapahtuu selaimen kautta osoitteessa https://swapmarket.github.io. Käytä mahdollisimman suurta luottamuksellisuutta varten Bravea, Firefoxia, jossa on jäljittämisen estävät laajennukset, tai LibreWolfia. Tor-selainta suositellaan verkon anonymiteetin säilyttämiseksi.



Rekisteröintiä, sähköpostia tai henkilöllisyyden tarkistamista ei tarvita.



### Itse isännöinti (valinnainen)



Tekniset käyttäjät, jotka haluavat poistaa riippuvuuden virallisesta GitHub Pages -verkkotunnuksesta, voivat käyttää SwapMarketia paikallisesti:



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Dockerin kautta** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Hakemus on saatavilla osoitteessa "http://localhost:3000". Itsehallinnointi takaa käyttöliittymän täydellisen hallinnan, poistaa virallisen verkkotunnuksen sensuurin riskin ja mahdollistaa lähdekoodin tarkastamisen ennen suorittamista.



### Alkuperäinen konfigurointi



**Wallet Lightning**: wallet Lightning (Phoenix, Zeus, BlueWallet jne.). Vaihtoa varten tarvitset generate Lightning-laskun. Vaihtoja varten maksat Lightning-laskun.



**Wallet on-chain**: wallet Bitcoin on-chain varojen lähettämiseen. Vaihtoja varten valmistele Bitcoin-vastaanotto-osoite.



**Vaihtoehtoinen kokoonpano**: SwapMarket tallentaa vaihtohistorian ja asetukset selaimen evästeisiin. Tiliä ei tarvitse luoda.



## Pääsy asetuksiin ja Rescue Key -avain



Ennen kuin teet ensimmäiset vaihdot, suosittelemme, että lataat **Pelastusavaimen**. Tämän hätäavaimen avulla voit palauttaa varasi, jos laitteeseen tulee tekninen ongelma tai jos et pääse käsiksi laitteeseesi.



### Pääsyparametrit



Napsauta SwapMarketin pääsivulla käyttöliittymän oikeassa yläkulmassa olevaa hammasratas-kuvaketta (⚙️) swap-lomakkeen vieressä.



![Accès aux paramètres](assets/fr/01.webp)



### Sivun asetukset



Asetukset-sivu avautuu ja näyttää useita asetusvaihtoehtoja:





- Nimellisarvo**: BTC tai sats
- Desimaalierotin**: Desimaalierotin (, tai .)
- Ääni-/selainilmoitukset**: Ääni- ja selainilmoitukset
- Pelastusavain** : Lataa palautusavain
- Lokit**: Tarkastele, lataa tai poista lokit



![Page Settings](assets/fr/02.webp)



### Lataa Rescue Key



Napsauta "Rescue Key" -kohdan vieressä olevaa **Lataa**-painiketta.



**Tärkeitä kohtia** :




- Rescue Key on **yhden luukun hätäavain**, joka toimii kaikissa tulevissa vaihdoissa
- Säilytä tämä avain **turvallisessa ja pysyvässä** paikassa (salasanahallinta, digitaalinen kassakaappi)
- Swap-ongelman sattuessa (aikakatkaisu, tekninen vika) voit palauttaa rahasi tämän avaimen avulla



## Swapin luominen vaihe vaiheelta



### Vaihda pois: Bitcoin



Tämä ensimmäinen esimerkki osoittaa, miten Lightning-satoshi muunnetaan on-chain-bittikolikoiksi.



**Vaihe 1: Vaihda kokoonpano



Valitse pääsivulta vaihtolomake :




- LIGHTNING** (ylempi kenttä): Syötä määrä, jonka haluat lähettää sats Lightningina (esimerkki: 30,000 sats)
- BITCOIN** (alempi kenttä): Summa, jonka saat, näytetään automaattisesti sen jälkeen, kun maksut on vähennetty (esimerkki: 29,320 sats)



Liitä alimpaan kenttään **vastaanottavan Bitcoin:n osoite**, johon haluat vastaanottaa varat. Tarkista tämä osoite huolellisesti.



Oletusarvoinen palveluntarjoaja on yleensä Boltz Exchange. Verkkomaksut ja palveluntarjoajan maksut näkyvät selvästi.



![Configuration swap-out](assets/fr/03.webp)



**Vaihe 2: Palveluntarjoajan valinta**



Napsauta palveluntarjoaja-pudotusvalikkoa (oletus: "Boltz Exchange") näyttääksesi kaikki käytettävissä olevat likviditeetin tarjoajat.



Avautuu modaalinen ikkuna, jossa näkyy vertailutaulukko:




- Tila**: Green-ilmaisin, jos palveluntarjoaja on aktiivinen
- Alias**: Palveluntarjoajan nimi (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Maksu**: Palveluntarjoajan perimät maksut (yleensä 0,49-0,5 %)
- Maksimivaihto**: Swapissa hyväksytty enimmäismäärä



Vertaile maksuja ja enimmäismääriä ja valitse sitten haluamasi palveluntarjoaja.



**Huomaa**: Palveluntarjoajan valintaliittymä ei näytä **minimimääriä** kullekin palveluntarjoajalle. Nämä tiedot näkyvät vasta swapin luomisliittymässä, kun palveluntarjoaja on valittu. Minimi- ja maksimimäärät voivat vaihdella palveluntarjoajakohtaisesti ja muuttua ajan myötä. **Tarkista nämä rajat aina swapin tekohetkellä**: jos summa, jonka haluat vaihtaa, on palveluntarjoajan rajojen ulkopuolella, voit valita toisen palveluntarjoajan, joka soveltuu paremmin transaktioosi.



![Sélection du provider](assets/fr/04.webp)



**Vaihe 3: Swapin luominen ja Lightning**-maksu



Napsauta keltaista **"CREATE ATOMIC SWAP "** -painiketta. SwapMarket lähettää generate **Lightning-laskun** (BOLT11), jonka voit maksaa wallet Lightningilla.



Sivu näyttää :




- Vaihtotunnus**: Yksilöllinen swap-tunniste (esimerkki: J4ymFIMVR6Hm)
- Tila**: "swap.created" (swap luotu, odottaa maksua)
- QR-koodi**: Skannaa se wallet Lightningilla
- Invoice Lightning**: (esimerkki: lnbc300u1p50whiv...gn5dk2szgqkvfkzc): Merkkijono, joka alkaa kirjaimella "lnbc" (esimerkki: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Maksa tämä lasku wallet Lightningilla (Phoenix, Zeus, BlueWallet jne.). Tarkka maksettava summa näytetään (esimerkki: 30 000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Vaihe 4: Vahvistus ja hyväksyntä**



Kun Lightning-maksu on vahvistettu, SwapMarket vastaanottaa maksun välittömästi ja palveluntarjoaja lähettää Bitcoin-tapahtuman osoitteeseesi.



Tilaksi muuttuu **"invoice.settled "** (lasku maksettu), ja näyttöön tulee vahvistusviesti.



on-chain-bittikolikkosi ovat käytettävissäsi heti, kun maksutapahtuma on vahvistettu (yleensä muutamasta minuutista muutamaan tuntiin, riippuen palveluntarjoajan valitsemista mining-maksuista).



![Confirmation swap-out](assets/fr/06.webp)



Voit napsauttaa **"OPEN CLAIM TRANSACTION "** nähdäksesi Bitcoin-transaktion lohkoketju-selaimella.



### Vaihda sisään: Bitcoin → Salama



Tämä toinen esimerkki osoittaa, miten on-chain-bittikolikot muunnetaan Lightning-satosheiksi.



**Vaihe 1: Vaihda kokoonpano



Valitse pääsivulta vaihtolomake :




- BITCOIN** (ylempi kenttä): Kirjoita summa, jonka haluat lähettää sats Bitcoin:nä (esimerkki: 63 400 sats)
- LIGHTNING** (alempi kenttä): Saamasi summa näkyy automaattisesti maksujen vähentämisen jälkeen (esimerkki: 62 884 sats)



Liitä alimmaiseen kenttään wallet Lightning -ohjelmalla luotu Lightning**-lasku (BOLT11) tai käytä LNURL-osoitetta, jos wallet tukee sitä.



![Configuration swap-in](assets/fr/07.webp)



**Vaihe 2: Pelastusavaimen tarkistus**



Kun olet napsauttanut **"CREATE ATOMIC SWAP "**, näyttöön tulee modaalinen ikkuna, jossa sinua pyydetään vahvistamaan Rescue Key -avaimesi.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Napsauta **"VERIFY EXISTING KEY "** -painiketta tuodaksesi tallentamasi avaimen.



Valitse aiemmin ladattu Rescue Key -tiedosto. Kun vahvistus on onnistunut, käyttöliittymä siirtyy automaattisesti seuraavaan vaiheeseen.



**Vaihe 3: Bitcoin** talletusosoite



SwapMarket luo nyt **yksilöllisen Bitcoin-osoitteen**, joka sisältää Lightning-laskuusi liitetyn HTLC-sopimuksen.



Sivu näyttää :




- Vaihtotunnus**: Yksilöllinen tunniste (esimerkki: 1kGmB6JyGqU4)
- Tila**: "invoice.set" (lasku asetettu, odottaa maksua Bitcoin): "invoice.set" (lasku asetettu, odottaa maksua Bitcoin)
- QR-koodi**: Bitcoin varikon osoite
- Bitcoin** osoite: ..." (esimerkki: bc1p5mvtwxapjkds...9d4n9f)
- Varoitus keltaisella** : "Varmista, että transaktiosi vahvistetaan ~24 tunnin kuluessa tämän swapin luomisesta!"



Tämä ~24 tunnin ajanjakso on HTLC-sopimuksen **aikakatko**. Jos Bitcoin-tapahtumaasi ei vahvisteta tämän ajan kuluessa, vaihto epäonnistuu, ja sinun on käytettävä Rescue Key -avainta varojen palauttamiseksi.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Voit kopioida osoitteen napsauttamalla **"ADRESS "**-painiketta tai skannata QR-koodin suoraan wallet on-chain:llä.



**Vaihe 4: Bitcoinien lähettäminen**



Lähettäkää wallet Bitcoin on-chain:sta **tarkasti** ilmoitettu määrä (esim. 63 400 sats) muodostettuun osoitteeseen.



**Tärkeää**: Käytä asianmukaisia mining-maksuja nopean vahvistuksen takaamiseksi. Jos maksu on liian alhainen ja transaktio jää mempooliin aikakatkaisun (~24h) jälkeen, vaihto epäonnistuu.



Kun transaktio on lähetetty, SwapMarket havaitsee, että se on mempoolissa ja näyttää :




- Tila** : "transaction.mempool
- Viesti**: "Transaktio on mempoolissa - Odottaa vahvistusta swapin loppuun saattamiseksi"



![Transaction en mempool](assets/fr/10.webp)



**Vaihe 5: Vahvistus ja salama** vastaanotto



Heti kun Bitcoin-tapahtuma saa ensimmäisen vahvistuksen, palveluntarjoaja maksaa Lightning-laskusi automaattisesti. Saat satoshit välittömästi wallet Lightning -laskuusi.



Tilaksi muuttuu **"transaction.claim.pending "**, minkä jälkeen näyttöön tulee vahvistusviesti:



![Confirmation swap-in](assets/fr/11.webp)



Lightning-satosi ovat välittömästi käytettävissä wallet:ssäsi.



## Edut ja rajoitukset



### Edut



**Kilpailu**: Palveluntarjoajien yhdistäminen luo luonnollista kilpailua, joka laskee maksuja (0,49 % - 0,5 %).



**Salaisuuden suojaaminen**: Ei KYC, 100% asiakaspuolen käyttöliittymä (ei henkilötietojen siirtoa), Tor Browser -yhteensopiva.



**Ei huoltajuutta**: HTLC takaa matemaattisesti varojen yksinomaisen hallinnan. Joko vaihto onnistuu tai saat bitcoinisi takaisin.



**Open-source self-hostable**: auditoitava julkinen koodi, joka voidaan ottaa käyttöön paikallisesti, jotta se kestää mahdollisimman hyvin sensuuria.



### Rajoitukset



**Rajoitettu likviditeetti**: Rajoitettu määrä aktiivisia palveluntarjoajia (Boltz, Eldamar, MiddleWay riippuen ajanjaksosta). Enimmäismäärät voivat olla rajoitettuja.



**Virkamääräajan päättymisajankohta**: 24h - 48h. Jos on-chain-tapahtumaa ei vahvisteta ennen voimassaolon päättymistä, tarvitaan manuaalinen palautus.



**Interface:n keskittäminen**: Vaikka virallinen käyttöliittymä on itse isännöitavissa, se on isännöity GitHub-sivuilla. Jos GitHub sensuroi repon, pääsy swapmarket.github.io:n kautta estetään (ratkaisu: itsehostaus).



**on-chain Traces**: HTLC-skriptit ovat mahdollisesti tunnistettavissa kehittyneellä lohkoketjuanalyysillä.



## Parhaat käytännöt



### Turvallinen konfigurointi



**Lataa pelastusavain**: Lataa Rescue Key -avain Asetuksista ennen ensimmäisiä vaihtoja (ks. edellä oleva oma osio). Tämä yksilöllinen avain toimii kaikissa tulevissa swapeissasi, ja sen avulla voit palauttaa rahasi ongelman sattuessa.



**Käytä Tor-selainta**: Käytä Tor-selainta: Maksimaalisen luottamuksellisuuden saavuttamiseksi käytä SwapMarketia Tor-selaimen kautta IP-osoitteesi piilottamiseksi.



**Harkitse itse isännöintiä**: Teknisille käyttäjille oman SwapMarket-instanssin käyttäminen poistaa riippuvuuden virallisesta GitHub Pages -verkkotunnuksesta.



### Vaihdon optimointi



**Pitäkää silmällä mempoolia**: Tarkista mempool.space ennen vaihtoa. Valitse vähäisen aktiivisuuden ajankohdat mining-kustannusten minimoimiseksi.



**Tarkista osoitteet**: Tarkista tarkkaan vastaanotto-osoitteesi, jos haluat vaihtaa osoitteesi. Käytä kopioi ja liitä -toimintoa ja tarkista 5 ensimmäistä ja 5 viimeistä merkkiä.



**Kokeile pienillä määrillä**: Aloita pienimmällä sallitulla määrällä (25 000-50 000 sats). Suurenna asteittain, kun hallitset prosessin.



**Dokumentoi vaihtosi**: Merkitse muistiin jokaisen swapin tunnus, lunastusosoite ja viimeinen voimassaolopäivä. Nämä tiedot helpottavat seurantaa ja palautusta teknisen ongelman sattuessa.



### Käyttöstrategia



**Tasapainota kassavirtaasi**: Käytä SwapMarketia säätääksesi jakoa on-chain:n (säästöt, pitkäaikainen turva) ja Lightningin (päivittäiset kulut, pikamaksut) välillä todellisten tarpeidesi mukaan.



**Lasketaan kannattavuus**: Vertaa toistuvien swap-sopimusten kumulatiivisia kustannuksia verrattuna Lightning-kanavan avaamiseen suoraan. SwapMarket soveltuu erinomaisesti kertaluonteisiin säätöihin, ei välttämättä suuriin säännöllisiin virtoihin.



## SwapMarket vs Boltz: Mikä on ero?



### Boltz: Boltz: Teknologia vs. palvelu



**Boltz on avoimen lähdekoodin teknologia** (`boltz-backend` GitHubissa), joka toteuttaa HTLC:n kautta atomiset vaihdot Bitcoin:n, Lightningin ja Liquid:n välillä.



**Kriittinen kohta**: Kaikki SwapMarket-palveluntarjoajat (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) käyttävät omaa Boltz-backendiä. Taustalla oleva teknologia on siis identtinen. Boltzin backendissä oleva haavoittuvuus voisi vaikuttaa kaikkiin palveluntarjoajiin, mutta järjestelmän avoimen lähdekoodin luonne mahdollistaa yhteisön suorittaman tarkastuksen.



**Boltz Exchange** on Boltzin tiimin ylläpitämä yksittäinen palvelu, kun taas **SwapMarket** yhdistää useita Boltzin teknologiaa käyttäviä palveluntarjoajia, mikä luo kilpailukykyisen hinnoitteluympäristön.



Katso lisätietoja Boltzin ja Zeuksen vaihto-oppaista:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Keskeiset erot



| Ominaisuus   | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Luonne        | Ainutlaatuinen palvelu | Monitoimittaja-aggregaattori       |
| Tarjoajat     | Vain Boltz           | Boltz, ZEUS, Eldamar, Middle Way     |
| Kilpailu      | Kiinteät hinnat       | Vapaa kilpailu                       |
| Käyttöliittymä| boltz.exchange       | swapmarket.github.io (itse isännöitävä) |
| Turvallisuus  | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**SwapMarketin edut**: Hintakilpailu, backend-instanssien monipuolistaminen, reaaliaikainen vertailu.



**Tekniset vaihtoehdot** (ei SwapMarket-yhteensopiva): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Nämä ratkaisut käyttävät omia toteutuksiaan vedenalaisista swapeista.



**Suositus**: Käytä Boltz Exchange:tä yksinkertaisuuden vuoksi tai SwapMarketia kustannusten optimoimiseksi kilpailun avulla. Molemmat ovat turvallisuudeltaan vastaavia (HTLC ei ole vartiointiliike).



## Päätelmä



SwapMarket helpottaa Bitcoin/Lightning-vaihtoja yhdistämällä useita palveluntarjoajia yhteen käyttöliittymään. HTLC-arkkitehtuuri takaa, että swapit eivät ole luonteeltaan säilytysoikeudellisia, KYC:n puuttuminen säilyttää luottamuksellisuuden, ja itse ylläpidettävä avoimen lähdekoodin koodi vahvistaa sensuurin vastustuskykyä.



Palveluntarjoajien välinen kilpailu parantaa korkoja ja moninkertaistaa likviditeetin lähteet. SwapMarket on käytännöllinen väline, jolla voidaan optimoida kaksitasoinen hallinnointi (on-chain-säästöt, Lightning-kustannukset) ja säilyttää taloudellinen riippumattomuus ja luottamuksellisuus.



## Resurssit



### Viralliset asiakirjat




- [SwapMarket - Web-sovellus](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tekninen dokumentaatio](https://docs.boltz.exchange/)
- [Opas itseisännöintiin](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Aiheeseen liittyvät hankkeet




- [Boltz Exchange](https://boltz.exchange) - Alkuperäinen atominvaihtopalvelu
- [ZEUS Swaps](https://zeusln.com) - Salamavaihtojen tarjoaja