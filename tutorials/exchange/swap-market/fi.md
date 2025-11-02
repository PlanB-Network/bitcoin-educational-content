---
name: SwapMarket
description: Bitcoin ja Lightning swap-palvelujen aggregaattori
---

![cover](assets/cover.webp)



Varojen siirtäminen Bitcoin On-Chain:n ja Lightning Network:n välillä edellyttää yleensä joko Lightning-kanavien avaamista manuaalisesti (mikä on teknistä ja kallista) tai keskitettyjen swap-alustojen käyttöä KYC:n kanssa. SwapMarket tarjoaa vaihtoehdon: Trustless:n atomiset swapit kilpailukykyisten palveluntarjoajien kautta ilman KYC:tä.



Innovaatio: Vaikka palveluntarjoajat ovat välittäjiä, HTLC (*Hash Time Locked Contracts*) takaa matemaattisesti, että varasi pysyvät sinun hallinnassasi. Useiden palveluntarjoajien (Boltz, ZEUS Swaps, Eldamar, Middle Way) yhdistäminen luo hintakilpailua. Interface-verkkosivusto avoimen lähdekoodin itsehostettavissa.



## Mikä on SwapMarket?



SwapMarket on vuonna 2024 käynnistetty avoimen lähdekoodin aggregaattori, joka toimii Bitcoin/Lightning-swap-palveluntarjoajien vertailujärjestelmänä. Käyttäjä vertailee välittömästi ehtoja (maksut, likviditeetti, limiitit) ja valitsee optimaalisen palveluntarjoajan.



### Tekninen arkkitehtuuri



**Frontend-asiakaspuoli**: 100 % asiakaspuolen sovellus (Fork Boltz Web App), joka sijaitsee GitHub-sivuilla. Koodi toimii selaimessa ilman backend-palvelinta. Historia tallennetaan paikallisesti (evästeet/ välimuisti). Julkinen ja tarkastettavissa oleva lähdekoodi.



**Palveluntarjoajan löytäminen** : Hard-koodattu lista tiedostossa `src/configs/Mainnet.ts`. Uusia palveluntarjoajia lisätään Pull Requestilla tai sähköpostilla.



**Riippumattomat taustajärjestelmät**: Kullakin palveluntarjoajalla on oma Boltz-backend. Interface tekee reaaliaikaisia API-kyselyjä vertaillakseen tarjouksia välittömästi.



**HTLC Atomic Swaps**: Hash Aikalukitut sopimukset takaavat atomisuuden: joko swap toteutuu tai kumpikin osapuoli saa varansa takaisin. Vastapuoliriski matemaattisesti eliminoitu.



### Filosofia



SwapMarket vähentää keskittämistä luomalla kilpailua palveluntarjoajien välille maksuista ja likviditeetistä. Ei KYC:tä, avoimen lähdekoodin itsehostattava koodi, riippumattomien operaattoreiden moninkertaistaminen yksittäisten vikapisteiden välttämiseksi.



## Tärkeimmät ominaisuudet



### Palveluntarjoajan markkinapaikka



Interface näyttää kaikki aktiiviset palveluntarjoajat: palveluntarjoajan nimi, sovellettavat maksut (prosentteina ja/tai kiinteinä), käytettävissä olevat vähimmäis- ja enimmäismäärät sekä tuetut swap-tyypit. Sovellus kysyy suoraan kunkin konfiguraatiotiedostossa mainitun palveluntarjoajan API:lta reaaliaikaisten tarjousten hakemista varten. Palveluntarjoajien välinen kilpailu takaa optimaaliset hinnat, jotka ovat yleensä noin 0,5 % vakioswapeissa.



### Kaksisuuntaiset vaihdot



**Swap-in (On-Chain → Lightning)**: Muunna On-Chain BTC:t Lightning-satoseiksi. Käyttötarkoitus: Wallet Lightningin käyttö, solmun saapuvan kapasiteetin hankkiminen tai välitön likviditeetti.



**Vaihtaminen (Lightning → On-Chain)**: Muunna Lightning-satoshi On-Chain BTC:ksi. Käyttötapaus: Wallet Lightningin siirtäminen Cold-varastoon tai likviditeetin tasapainottaminen kerrosten välillä.



### Turvallisuus ja elpyminen



**Trustless Atomivaihdot: HTLC takaa, että joko Exchange toteutetaan kokonaisuudessaan tai että kumpikin osapuoli saa panoksensa takaisin. Vastapuoliriski on matemaattisesti eliminoitu.



**Lunastusmekanismi**: Kullakin swapilla on päättymispäivä (TIMELOCK). Jos swap ei onnistu, varat palautetaan automaattisesti vanhentumisen jälkeen. Käyttäjällä on aina mahdollisuus saada bitcoininsa takaisin.



**Palautusavaimet**: SwapMarketin avulla voit viedä palautusavaimia käynnissä oleville vaihdoille. Ongelmatilanteessa näillä avaimilla voit viimeistellä tai peruuttaa vaihdon mistä tahansa laitteesta.



## Asennus ja pääsy



### Interface web



SwapMarket ei vaadi asennusta. Pääsy tapahtuu selaimen kautta osoitteessa https://swapmarket.github.io. Käytä mahdollisimman suurta luottamuksellisuutta varten Bravea, Firefoxia, jossa on jäljittämisen estävät laajennukset, tai LibreWolfia. Tor-selainta suositellaan verkon anonymiteetin säilyttämiseksi.



Rekisteröitymistä, sähköpostia tai henkilöllisyyden tarkistamista ei tarvita.



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



Hakemus on saatavilla osoitteessa "http://localhost:3000". Itsehostaminen takaa Interface:n täydellisen valvonnan, poistaa virallisen verkkotunnuksen sensuurin riskin ja mahdollistaa lähdekoodin tarkastamisen ennen suorittamista.



### Alkuperäinen konfigurointi



**Wallet Lightning**: Wallet Lightning (Phoenix, Zeus, BlueWallet jne.). Vaihtoa varten sinulla on generate Lightning Invoice. Vaihtoja varten maksat Lightning Invoice:n.



**Wallet On-Chain**: Wallet Bitcoin On-Chain: Vaihtoa varten tarvitset Wallet Bitcoin On-Chain:n varojen lähettämistä varten. Vaihtoja varten valmistele Bitcoin, joka vastaanottaa Address:n.



**Vaihtoehtoinen kokoonpano**: SwapMarket tallentaa vaihtohistorian ja asetukset selaimen evästeisiin. Tiliä ei tarvitse luoda.



## Pääsy asetuksiin ja Rescue Key -avain



Ennen kuin teet ensimmäiset vaihdot, suosittelemme, että lataat **Pelastusavaimen**. Tämän hätäavaimen avulla voit palauttaa varasi, jos laitteeseen tulee tekninen ongelma tai jos et pääse käsiksi laitteeseesi.



### Pääsyparametrit



Napsauta SwapMarketin pääsivulla Interface:n oikeassa yläkulmassa olevaa hammasratas-kuvaketta (⚙️) swap-lomakkeen vieressä.



![Accès aux paramètres](assets/fr/01.webp)



### Sivun asetukset



Asetukset-sivu avautuu ja näyttää useita asetusvaihtoehtoja:





- Nimellisarvo**: BTC tai Sats
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



Tämä ensimmäinen esimerkki osoittaa, miten Lightning-satoshi muunnetaan On-Chain-bittikolikoiksi.



**Vaihe 1: Vaihda kokoonpano



Valitse pääsivulta vaihtolomake :




- LIGHTNING** (ylempi kenttä): Syötä määrä, jonka haluat lähettää Sats Lightningina (esimerkki: 30,000 Sats)
- Bitcoin** (alin kenttä): Saamasi summa näkyy automaattisesti sen jälkeen, kun maksut on vähennetty (esimerkki: Sats 29,320)



Liitä alimmaiseen kenttään **vastaanottava Bitcoin Address**, johon haluat vastaanottaa varat. Tarkista tämä Address huolellisesti.



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



**Huomaa**: Interface ei näytä kunkin palveluntarjoajan **minimimääriä**. Nämä tiedot näkyvät vasta swap creation Interface:ssa, kun palveluntarjoaja on valittu. Minimi- ja maksimimäärät voivat vaihdella palveluntarjoajakohtaisesti ja muuttua ajan myötä. **Katso nämä rajat aina swappia tehtäessäsi**: jos summa, jonka haluat vaihtaa, on palveluntarjoajan rajojen ulkopuolella, voit valita toisen palveluntarjoajan, joka soveltuu paremmin transaktioosi.



![Sélection du provider](assets/fr/04.webp)



**Vaihe 3: Swapin luominen ja Lightning**-maksu



Napsauta keltaista **"CREATE ATOMIC SWAP "** -painiketta. SwapMarket lähettää sinulle generate:n **Lightning Invoice** (BOLT11), jonka voit maksaa Wallet Lightningilla.



Sivu näyttää :




- Vaihtotunnus**: Yksilöllinen swap-tunniste (esimerkki: J4ymFIMVR6Hm)
- Tila**: "swap.created" (swap luotu, odottaa maksua)
- QR-koodi**: Skannaa se Wallet Lightningilla
- Invoice Salama**: (esimerkki: lnbc300u1p50whiv...gn5dk2szgqkvfkzc): Merkkijono, joka alkaa kirjaimella "lnbc" (esimerkki: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Maksa tämä Invoice omasta Wallet Lightningista (Phoenix, Zeus, BlueWallet jne.). Tarkka maksettava summa näytetään (esimerkki: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Vaihe 4: Vahvistus ja hyväksyntä**



Kun Lightning-maksu on vahvistettu, SwapMarket vastaanottaa maksun välittömästi ja palveluntarjoaja lähettää Bitcoin-tapahtuman Address:aan.



Tilaksi muuttuu **"Invoice.settled "** (Invoice maksettu), ja näyttöön tulee vahvistusviesti.



On-Chain-bittikolikkosi ovat käytettävissäsi heti, kun maksutapahtuma on vahvistettu (yleensä muutamasta minuutista muutamaan tuntiin, riippuen palveluntarjoajan valitsemista Mining-maksuista).



![Confirmation swap-out](assets/fr/06.webp)



Voit napsauttaa **"OPEN CLAIM TRANSACTION "** nähdäksesi Bitcoin-tapahtuman Blockchain-selaimessa.



### Vaihda sisään: Bitcoin → Salama



Tämä toinen esimerkki osoittaa, miten On-Chain-bittikolikot muunnetaan Lightning-satosheiksi.



**Vaihe 1: Vaihda kokoonpano



Valitse pääsivulta vaihtolomake :




- Bitcoin** (ylempi kenttä): Kirjoita määrä, jonka haluat lähettää Sats Bitcoin (esimerkki: 63 400 Sats)
- LIGHTNING** (alempi kenttä): Saamasi summa näkyy automaattisesti maksujen vähentämisen jälkeen (esimerkki: 62 884 Sats)



Liitä alimmaiseen kenttään Lightning** Invoice (BOLT11), joka on luotu Wallet Lightningista, tai käytä LNURL Address:tä, jos Wallet tukee sitä.



![Configuration swap-in](assets/fr/07.webp)



**Vaihe 2: Pelastusavaimen tarkistus**



Kun olet napsauttanut **"CREATE ATOMIC SWAP "**, näyttöön tulee modaalinen ikkuna, jossa sinua pyydetään vahvistamaan Rescue Key -avaimesi.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Napsauta **"VERIFY EXISTING KEY "** -painiketta tuodaksesi tallentamasi avaimen.



Valitse aiemmin ladattu Rescue Key -tiedosto. Kun vahvistus on onnistunut, Interface siirtyy automaattisesti seuraavaan vaiheeseen.



**Vaihe 3: Bitcoin** talletus Address



SwapMarket luo nyt **yksilöllisen Bitcoin Address**:n, joka sisältää HTLC Contract:n, joka on yhdistetty Lightning Invoice:ään.



Sivu näyttää :




- Vaihtotunnus**: Yksilöllinen tunniste (esimerkki: 1kGmB6JyGqU4)
- Tila** : "Invoice.set" (Invoice asetettu, odottaa maksua Bitcoin)
- QR-koodi**: Bitcoin varikko Address
- Bitcoin** Address: Alkaa yleensä sanoilla "bc1p..." (esimerkki: bc1p5mvtwxapjkds...9d4n9f)
- Varoitus keltaisella** : "Varmista, että transaktiosi vahvistetaan ~24 tunnin kuluessa tämän swapin luomisesta!"



Tämä ~24 tunnin jakso on HTLC Contract:n **timeout**. Jos Bitcoin-tapahtumaasi ei vahvisteta tämän ajan kuluessa, vaihto epäonnistuu ja sinun on käytettävä Rescue Key -avainta varojen palauttamiseksi.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Voit kopioida Address:n napsauttamalla **"Address"**-painiketta tai skannata QR-koodin suoraan Wallet On-Chain:stä.



**Vaihe 4: Bitcoinien lähettäminen**



Lähetä Wallet Bitcoin On-Chain:sta **tarkasti** ilmoitettu määrä (esim. 63 400 Sats) Address:ään.



**Tärkeää**: Käytä asianmukaisia Mining-maksuja nopean vahvistuksen takaamiseksi. Jos maksu on liian alhainen ja transaktio pysyy Mempool:ssa yli aikakatkaisun (~24 tuntia), vaihto epäonnistuu.



Kun transaktio on lähetetty, SwapMarket havaitsee, että se on Mempool:ssa ja näyttää :




- Tila** : "transaction.Mempool"
- Viesti**: "Transaktio on Mempool:ssa - Odotetaan vahvistusta swapin loppuunsaattamiseksi."



![Transaction en mempool](assets/fr/10.webp)



**Vaihe 5: Vahvistus ja salama** vastaanotto



Heti kun Bitcoin-tapahtuma saa ensimmäisen vahvistuksen, palveluntarjoaja maksaa automaattisesti Lightning Invoice -maksun. Saat satoshit välittömästi Wallet Lightningisi.



Tilaksi muuttuu **"transaction.claim.pending "**, minkä jälkeen näyttöön tulee vahvistusviesti:



![Confirmation swap-in](assets/fr/11.webp)



Lightning-satosi ovat välittömästi käytettävissä Wallet:ssa.



## Edut ja rajoitukset



### Edut



**Kilpailu**: Palveluntarjoajien yhdistäminen luo luonnollista kilpailua, joka laskee maksuja (0,49 % - 0,5 %).



**Salaisuuden suojaaminen**: Interface 100% asiakaspuolella (ei henkilötietojen siirtoa), Tor Browser -yhteensopiva.



**Ei huoltajuutta**: HTLC takaa matemaattisesti varojen yksinomaisen hallinnan. Joko vaihto onnistuu tai saat bitcoinisi takaisin.



**Open-source self-hostable**: auditoitava julkinen koodi, joka voidaan ottaa käyttöön paikallisesti, jotta se kestää mahdollisimman hyvin sensuuria.



### Rajoitukset



**Rajoitettu likviditeetti**: Rajoitettu määrä aktiivisia palveluntarjoajia (Boltz, Eldamar, MiddleWay riippuen ajanjaksosta). Enimmäismäärät voivat olla rajoitettuja.



**Virkamääräajan päättymisajankohta**: 24h - 48h. Jos On-Chain-tapahtumaa ei vahvisteta ennen voimassaolon päättymistä, tarvitaan manuaalinen palautus.



**Interface keskittäminen**: Interface:n virallinen versio on GitHub-sivuilla, vaikka se onkin itse isännöitavissa. Jos GitHub sensuroi repon, pääsy swapmarket.github.io:n kautta estetään (ratkaisu: itsehostaus).



**On-Chain jäljet**: HTLC-skriptit ovat mahdollisesti tunnistettavissa kehittyneellä Blockchain-analyysillä.



## Parhaat käytännöt



### Turvallinen konfigurointi



**Lataa pelastusavain**: Lataa Rescue Key -avain Asetuksista ennen ensimmäisiä vaihtoja (ks. edellä oleva oma osio). Tämä yksilöllinen avain toimii kaikissa tulevissa swapeissasi, ja sen avulla voit palauttaa rahasi ongelman sattuessa.



**Käytä Tor-selainta**: Address.



**Harkitse itse isännöintiä**: Teknisille käyttäjille oman SwapMarket-instanssin käyttäminen poistaa riippuvuuden virallisesta GitHub Pages -verkkotunnuksesta.



### Vaihdon optimointi



**Keep an eye on Mempool**: Tarkista Mempool.space ennen vaihtoa. Valitse ajankohdat, jolloin toiminta on vähäistä, jotta Mining-kustannukset ovat mahdollisimman pienet.



**Tarkista osoitteet**: Tarkista huolellisesti vastaanottamasi Address. Käytä kopioi ja liitä -toimintoa ja tarkista 5 ensimmäistä ja 5 viimeistä merkkiä.



**Kokeile pienillä määrillä**: Aloita pienimmällä sallitulla määrällä (25 000-50 000 Sats). Lisää vähitellen, kun hallitset prosessin.



**Dokumentoi vaihtosi**: Merkitse muistiin jokaisen swapin tunnus, lunastus Address ja viimeinen voimassaolopäivä. Nämä tiedot helpottavat seurantaa ja palautusta teknisen ongelman sattuessa.



### Käyttöstrategia



**Tasapainota kassavirtaasi**: Käytä SwapMarketia säätääksesi jakoa On-Chain (säästöt, pitkäaikainen turva) ja Lightning (päivittäiset kulut, pikamaksut) välillä todellisten tarpeidesi mukaan.



**Lasketaan kannattavuus**: Vertaa toistuvien swap-sopimusten kumulatiivisia kustannuksia verrattuna Lightning-kanavan avaamiseen suoraan. SwapMarket soveltuu erinomaisesti kertaluonteisiin säätöihin, ei välttämättä suuriin säännöllisiin virtoihin.



## SwapMarket vs Boltz: Mikä on ero?



### Boltz: Boltz: Teknologia vs. palvelu



**Boltz on avoimen lähdekoodin teknologia** (`boltz-backend` GitHubissa), joka toteuttaa HTLC:n kautta atomiset vaihdot Bitcoin:n, Lightningin ja Liquid:n välillä.



**Kriittinen kohta**: Kaikki SwapMarket-palveluntarjoajat (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) käyttävät omaa Boltz-backendiä. Taustalla oleva teknologia on siis identtinen. Boltzin backendissä oleva haavoittuvuus voisi vaikuttaa kaikkiin palveluntarjoajiin, mutta järjestelmän avoimen lähdekoodin luonne mahdollistaa yhteisön suorittaman tarkastuksen.



**Boltz Exchange** on Boltzin tiimin ylläpitämä yksittäinen palvelu, kun taas **SwapMarket** yhdistää useita Boltzin teknologiaa käyttäviä palveluntarjoajia, mikä luo kilpailukykyisen hinnoitteluympäristön.



Katso lisätietoja Boltzin ja Zeuksen vaihto-oppaista:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Keskeiset erot



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarketin edut**: Hintakilpailu, backend-instanssien monipuolistaminen, reaaliaikainen vertailu.



**Tekniset vaihtoehdot** (ei SwapMarket-yhteensopiva): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Nämä ratkaisut käyttävät omia toteutuksiaan vedenalaisista swapeista.



**Suositus**: Käytä Boltz Exchange:ää yksinkertaisuuden vuoksi tai SwapMarketia kustannusten optimoimiseksi kilpailun avulla. Molemmat ovat turvallisuudeltaan vastaavia (HTLC ei ole huoltajapainotteinen).



## Päätelmä



SwapMarket helpottaa Bitcoin/Lightning-vaihtoja yhdistämällä useita palveluntarjoajia yhdeksi Interface:ksi. HTLC-arkkitehtuuri takaa, että swapit eivät ole luonteeltaan säilytysvelvollisia, KYC:n puuttuminen säilyttää luottamuksellisuuden, ja avoimen lähdekoodin itse ylläpidettävä koodi vahvistaa sensuurin vastustuskykyä.



Palveluntarjoajien välinen kilpailu parantaa korkoja ja moninkertaistaa likviditeetin lähteet. SwapMarket on käytännöllinen väline, jolla voidaan optimoida kahden Layer:n hallintaa (On-Chain-säästöt, Lightning-kulut) ja joka säilyttää taloudellisen itsemääräämisoikeuden ja luottamuksellisuuden.



## Resurssit



### Viralliset asiakirjat




- [SwapMarket - Web-sovellus](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tekninen dokumentaatio](https://docs.boltz.Exchange/)
- [Opas itseisännöintiin](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Aiheeseen liittyvät hankkeet




- [Boltz Exchange](https://boltz.Exchange) - Alkuperäinen atominvaihtopalvelu
- [ZEUS Swaps](https://zeusln.com) - Salamanvaihtosopimusten tarjoaja