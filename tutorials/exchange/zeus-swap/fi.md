---
name: Zeus Swap
description: Exchange-palvelu, joka ei ole huoltajapalvelu On-Chain:n ja Lightning Network:n välillä bitcoineja
---

![cover](assets/cover.webp)



Bitcoin-ekosysteemi on kaksijakoinen: pääverkko (On-Chain) tarjoaa maksimaalisen turvallisuuden, kun taas Lightning Network mahdollistaa välittömät maksutapahtumat. Tämä kahden Layer:n arkkitehtuuri luo käytännön haasteen: miten varoja voidaan siirtää tehokkaasti näiden kahden kerroksen välillä ilman keskitettyjä välikäsiä?



Ongelma on konkreettinen: saat Lightning-maksun, mutta haluat pitää sen Cold-varastossa, tai päinvastoin, sinulla on On-Chain-bittikolikoita, mutta tarvitset Lightning-likviditeettiä. Perinteisiin ratkaisuihin kuuluu Lightning-kanavien manuaalinen avaaminen/sulkeminen (kallista ja teknistä) tai keskitetyt alustat, jotka vaativat KYC:n.



Zeus Swap ratkaisee tämän ongelman automatisoidulla, huoltajuuteen perustumattomalla Exchange-palvelulla. Zeus LSP:n kehittämässä palvelussa voit muuntaa On-Chain-bittikolikoita Lightning-satosheiksi kaksisuuntaisesti ilman, että uskot varojasi välittäjälle. Prosessissa käytetään atomisia sopimuksia (HTLC), jotka takaavat, että Exchange joko toteutuu tai peruuntuu.



Innovaatio perustuu sen yksinkertaisuuteen: vain muutamalla napsautuksella saat Exchange:n, joka säilyttää taloudellisen itsemääräämisoikeutesi, eikä rekisteröintiä tai KYC-tunnuksia tarvita.



## Mikä on Zeus Swap?



Zeus Swap on Zeus LSP:n kehittämä Exchange:n likviditeettipalvelu, joka mahdollistaa atomiset vaihdot Bitcoin-pääverkon ja Lightning Network:n välillä. Kyseessä on tekninen infrastruktuuri, joka käyttää submarine swap- ja reverse swap-operaatioita helpottaakseen On-Chain BTC:n ja Lightning-satoshien välistä kaksisuuntaista muuntamista säilyttäen samalla operaation säilytysmahdollisuudet.



### Tekninen arkkitehtuuri



Zeus Swap käyttää Boltzin avoimen lähdekoodin Bitcoin/Lightning-atomivaihtoteknologiaa. Protokolla käyttää Hash Time Locked Contracts (HTLC) -sopimuksia: sopimuksia, jotka lukitsevat varoja kahdella vapautusehdolla (salakirjoitussalaisuuden paljastuminen tai ajan umpeutuminen).



Sukellusvenevaihdossa (On-Chain → Lightning) käyttäjä lähettää bitcoineja Address:een, joka sisältää Lightning Invoice:n Hash:n. Zeus LSP avaa nämä varat vain maksamalla vastaavalle Invoice:lle, jolloin paljastuu esikuva, joka avaa bitcoinit automaattisesti. Tämä mekanismi takaa atomisuuden.



Käänteistä vaihtoa (Lightning → On-Chain) varten käyttäjä maksaa Zeus LSP:ltä Lightning Invoice -maksun, joka paljastaa ennakkokuvan, joka mahdollistaa valmistellun Bitcoin-tapahtuman vapauttamisen kohde-Address:een.



Jos haluat lisätietoja Lightning Network:n toiminnasta, tutustu omaan kurssiimme :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Liiketoimintamalli



Zeus LSP toimii markkinatakaajana, joka ylläpitää On-Chain- ja Lightning-likviditeettiä swap-sopimusten täyttämiseksi. Zeus perii swapeista vaihtelevan maksun (tyypillisesti 0,1-0,5 % suunnasta ja ehdoista riippuen) sekä Bitcoin:n Mining-maksun, joka näytetään avoimesti ennen validointia.



Lightning-palveluntarjoajana Zeus optimoi kustannuksia, koska se on erikoistunut tilauskanavien avaamiseen, tehokkaaseen reititykseen ja räätälöityihin likviditeettiratkaisuihin.



### Integrointi



Zeus Wallet integroi palvelun natiivisti, mikä mahdollistaa vaihdot poistumatta Interface Bitcoin/Lightningista. Tämä poistaa sovellusten välisen kopioinnin ja liittämisen aiheuttaman kitkan.



Riippumaton Interface-verkko on edelleen kaikkien lompakoiden käytettävissä, mikä takaa maksimaalisen käyttöjoustavuuden.



## Tärkeimmät ominaisuudet



### Kaksisuuntaiset vaihdot



Zeus Swap tarjoaa kahdenlaista Exchange:ta:



**Submarine swaps (On-Chain → Lightning)**: lisää Lightning-rahoitusta Bitcoin:n varannoista, mikä on hyödyllistä liikkuvan Wallet:n tai Lightning-solmun ruokkimiseen ilman manuaalista kanavien avaamista.



**Käänteisvaihto (Lightning → On-Chain)**: muuntaa Lightning-satosheja On-Chain-bitcoineiksi pitkäaikaista varastointia varten, jolloin vältetään kalliit kanavien sulkemiset.



### Käyttöliittymät



**Interface web** (swaps.zeuslsp.com): yksinkertaistettu kokemus ilman rekisteröitymistä, opastettu prosessi, jossa maksut ja tila näkyvät reaaliaikaisesti.



**Zeus Wallet -integraatio**: suora vaihtaminen sovelluksesta, laskujen ja osoitteiden automaattinen hallinta, käsittelyvirheiden poistaminen.



### Turvallisuus ja elpyminen



Jokainen vaihto tuottaa ainutlaatuisen Contract:n, jonka parametrit ovat muuttumattomia: Hash Salama, aikakatkaisu, palautus Address. Vian sattuessa automaattinen palautus Address:n kautta Zeus LSP:stä riippumatta.



**Zeus vaihtaa pelastusavaimen**: On-Chain → Lightning-vaihdon aikana Zeus luo automaattisesti universaalin pelastusavaimen, joka korvaa vanhat yksittäiset palautustiedostot. Tämä ainutlaatuinen avain toimii millä tahansa laitteella ja kaikissa sillä luoduissa swapeissa. On erittäin tärkeää ladata ja tallentaa tämä avain turvalliseen paikkaan, jotta voit palauttaa rahavarasi swapin epäonnistumisen yhteydessä.



### Verkon optimointi



Zeus Swap säätää automaattisesti vanhenemisaikoja ja Mining-maksuja verkko-olosuhteiden mukaan. Zeuksen käyttäjät hyötyvät kehittyneistä vaihtoehdoista: LSP:n valinta, räätälöidyt viiveet, yhteensopivuus muiden palvelujen kanssa (Boltz).



## Asennus ja käyttö



### Pääsymenetelmät



**Interface web** (swaps.zeuslsp.com): universaali ratkaisu, joka on yhteensopiva kaikkien lompakoiden kanssa, ei vaadi asennusta, ihanteellinen satunnaiseen käyttöön.



**Zeus-sovellus** (iOS/Android): integroitu kokemus, jossa yhdistyvät Wallet ja swaps, sopii tavallisille käyttäjille.



Katso Zeus-opas saadaksesi lisätietoja tästä täydellisestä Wallet:stä:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Web-konfigurointi



**On-Chain → Salama**: Interface web Zeus Swap: Prosessi aloitetaan konfiguroimalla swap Interface:ssä. Käyttäjä voi käyttää On-Chain- ja Lightning-kenttien välissä olevaa nuolta swapin suunnan kääntämiseen.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: summan valinta (Sats 50,000 → Sats 49,648 maksujen jälkeen) ja verkkomaksujen (Sats 302) ja Zeus-palvelun (Sats 50) läpinäkyvä näyttö*



Prosessin aikana Zeus tarjoaa sinulle mahdollisuuden ladata universaalin palautusavaimen :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Lataa Zeus Swaps Rescue Key -yleisavain, joka korvaa vanhat yksittäiset korvaustiedostot*



Jos sinulla on jo avain, Zeus antaa sinun tarkistaa sen:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface tarkistaa olemassa olevan Zeus Swaps Rescue Key -avaimen voimassaolon*



Kun Zeus on määritetty, se luo Bitcoin-varaston Address ja näyttää ohjeet :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Vaihdon valmistumissivu: Address 50 000 Satssin lähettämiseen, muistutuksella 24 tunnin päättymispäivästä*



Vaihto odottaa sitten Bitcoin:n vahvistusta:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transaction in Mempool" - odottaa Bitcoin:n vahvistusta vaihdon viimeistelyä varten*



Vahvistuksen jälkeen vaihto suoritetaan automaattisesti:



![Swap réussi](assets/fr/06.webp)



*Vahvistus onnistumisesta: 49,648 Sats saatu Lightningilla verkko- ja palvelumaksujen vähentämisen jälkeen*



### Zeus-sovelluksen käyttäminen



**Lightning → On-Chain**: Zeus-sovellus tarjoaa integroidun kokemuksen käänteisvaihtoja varten (Lightning-Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeuksen päänäyttö, jossa näkyy Lightningin (69,851 Sats) ja On-Chain:n (38,018 Sats) saldot, vaihtoihin pääsee käsiksi sivuvalikon kautta*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface:n käänteisen vaihdon luominen: gW-69, jossa verkkomaksut (530 Sats) ja palvelu (250 Sats) näkyvät selvästi. Käyttäjät voivat joko syöttää manuaalisesti Bitcoin:n vastaanottavan Address:n tai generate:n automaattisesti Wallet Zeuksesta "generate On-Chain Address" -painikkeen avulla.*



![Finalisation du swap mobile](assets/fr/09.webp)



*Viimeistelynäytöt: Vahvistus onnistuneesta Lightning-maksusta 9,96 sekunnissa ja saldolaskelma, jossa 49 162 Sats odottaa vahvistusta*



### Valvonta ja turvallisuus



Jokaisella swapilla on yksilöllinen tunniste, jota voidaan seurata reaaliaikaisesti. Täydellinen edistymisnäyttö, automaattiset hälytykset päättymispäivistä. Automaattiset lataussuositukset verkko-olosuhteiden mukaan.



## Edut ja rajoitukset



### Edut





- Yksinkertaisuus**: Vaihtaminen muutamalla klikkauksella verrattuna manuaaliseen kanavan manipulointiin
- Ei-huoltajuus**: ei KYC:tä, ei tiliä, varoja ei koskaan luovuteta kolmannelle osapuolelle
- Läpinäkyvyys**: maksut näkyvät selkeästi ennen validointia (0,1-0,5 % + minimimaksu käyttäjätestien mukaan - tarkista kulloinkin voimassa olevat maksut jokaisessa swapissa)
- Mobiiliintegraatio**: natiivikokemus Zeus Wallet:ssä



### Rajoitukset





- Viimeiset voimassaoloajat**: 24-48h, epäonnistuminen, jos Bitcoin ei vahvisteta ajoissa
- Määrärajat**: vähintään 25 000 Sats, Zeus LSP -likviditeetti vaihtelee ehtojen mukaan
- Jäljet On-Chain**: HTLC-skriptit, jotka voidaan mahdollisesti tunnistaa Blockchain-analyysin avulla
- Vahvistus vaaditaan**: vähintään 10 minuuttia Bitcoin:n validointia varten



## Parhaat käytännöt



### Ajoitus ja kustannukset





- Tarkkaile Mempool.space-verkkosivustoa vähäisen ruuhkautumisen aikoina
- Suosivat viikonloppuja ja ruuhka-aikojen ulkopuolisia aikoja Mining-kustannusten vähentämiseksi
- Kannattavuuden laskeminen: pienet määrät vs. suora kanavan avaaminen



### Turvallisuus





- Tarkista Bitcoin-osoitteet huolellisesti (suositellaan copy-paste)
- Varmuuskopioi Zeus Swaps Rescue Key**: lataa ja säilytä palautusavain turvallisessa paikassa
- Asiakirja: Contract ID, tuki Address, viimeinen voimassaolopäivä
- Käytä asianmukaisia Mining-maksuja oikea-aikaisen vahvistuksen saamiseksi



### Käyttöstrategia





- Tasapainota On-Chain/Lightning-likviditeetti tarpeisiisi sopivaksi
- Zeus Swap kertaluonteisiin säätöihin, suorat kanavat pysyviin tarpeisiin



## Vertailu muihin swap-palveluihin



### Zeus Swap vs Boltz Exchange



Zeus Swap käyttää Boltzin backend-teknologiaa, mutta siinä on joitakin ratkaisevia parannuksia:



**Zeus Swapin edut** :




- Interface yhtenäistetty**: natiivi integrointi Zeukseen Wallet vs. Interface web-tekniikka Boltz
- WebSocket API**: reaaliaikaiset päivitykset verrattuna manuaaliseen kyselyyn
- Automaattinen hallinta**: automaattinen laskutus ja Address-hallinta
- Mobiilituki**: vain optimointi älypuhelimille vs. työpöydälle
- Swagger-dokumentaatio**: täydellinen REST API kehittäjille



**Boltz on edelleen edullinen**, koska se on täysin riippumaton ja sitä voidaan käyttää minkä tahansa Bitcoin/Lightning-asennuksen kanssa.



Zeus Swap muuntaa hyväksi havaitun Boltz-teknologian valtavirran käyttökokemukseksi, joka on verrattavissa raakaprotokollan ja käyttäjäystävällisen sovelluksen väliseen eroon.



### Zeus Swap vs Phoenix/Breez (integroitu vaihto)



Phoenix ja Breez integroivat läpinäkyviä vaihtotoimintoja, jotka piilottavat teknisen monimutkaisuuden loppukäyttäjältä. Phoenix käyttää automaattista swap-in/swap-out-järjestelmää, jossa käyttäjä ei tee nimenomaista eroa Bitcoin-kerrosten välillä: hän "lähettää Bitcoin Address:een" ja sovellus hoitaa swapin taustalla.



Tämä erittäin yksinkertaistettu lähestymistapa sopii täydellisesti aloittelijoille, mutta rajoittaa toimintojen ymmärtämistä ja hallintaa. Zeus Swap noudattaa opettavaisempaa filosofiaa: käyttäjät ymmärtävät, että he vaihtavat kahden eri kerroksen välillä, ja kehittävät vähitellen ymmärrystään kahden Layer Bitcoin ekosysteemistä.



## Yksityiskohtainen maksujen ja rajojen vertailu (2024)



⚠️ **Varoitus**: Maksut voivat vaihdella ajan mittaan markkinaolosuhteiden ja palvelupäivitysten mukaan. Tarkista aina Interface:ssa näkyvät maksut ennen swapin vahvistamista.




| Palvelu | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Minimimäärä |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + louhintamaksut | 0.5% + louhintamaksut | 25 000 sats |
| **Boltz** | 0.2% + louhintamaksut | 0.5% + louhintamaksut | 50 000 sats |
| **Phoenix** | Vain louhintamaksut | 0.4% kiinteä | 10 000 sats |
| **Breez** | 0.25% + verkkomaksut | 0.5% + louhintamaksut | 50 000 sats |

Zeus Swap tarjoaa tasapainon helppokäyttöisyyden ja teknisen hallinnan välillä: se on helpommin lähestyttävä kuin Boltz, joustavampi kuin Phoenix/Breez ja sen lähestymistapa on tiukka, mutta ei säilytysvelvollisuutta.



## Päätelmä



Zeus Swap on merkittävä innovaatio Bitcoin-ekosysteemissä, sillä se ratkaisee tyylikkäästi pääverkon ja Lightning Network:n välisen yhteentoimivuuden haasteen. Yhdistämällä atomisoidun swapin kryptografisen kestävyyden helppokäyttöiseen käyttäjäkokemukseen tämä palvelu demokratisoi Bitcoin:n ja Layer:n kaksoisswapin hallinnan tinkimättä taloudellisen riippumattomuuden periaatteista.



Zeus Swapin ei-hallinnollinen arkkitehtuuri, joka on periytynyt hyväksi havaitusta Boltz-teknologiasta, varmistaa, että varasi pysyvät yksinomaisessa hallinnassasi koko swap-prosessin ajan. Tämä lähestymistapa kunnioittaa Bitcoin:n henkeä ja tarjoaa samalla käyttömukavuutta, jota valtavirran käyttöönotto edellyttää. Hinnoittelun avoimuus ja KYC-prosessien puuttuminen vahvistavat tätä ainutlaatuista arvolupausta.



Nykyaikaiselle Bitcoin-käyttäjälle Zeus Swap on strateginen työkalu, jolla voidaan optimoida likviditeetin jakaminen tarpeiden mukaan: On-Chain turvallinen säilytys pitkäaikaisia säästöjä varten, Lightning-saatavuus päivittäisiä menoja ja mikrotransaktioita varten. Tämä joustavuus muuttaa Bitcoin:n hallinnan teknisestä rajoitteesta kilpailueduksi.



Kokeneen Zeus LSP -tiimin ja avoimen lähdekoodin Boltz-yhteisön tukemana Zeus Swapin tuleva kehitys lupaa jatkuvia parannuksia kustannuksiin, käsittelyaikoihin ja käyttäjäkokemukseen. Tämä palvelu on osa laajempaa Bitcoin-infrastruktuurin kypsymisen suuntausta, jossa tekninen kehittyneisyys tulee loppukäyttäjälle läpinäkyväksi.



## Resurssit



### Viralliset asiakirjat




- [Zeus Swap - Verkkoportaali](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobiilisovellus](https://zeusln.app)
- [Blog Zeus - Ilmoitukset ja opetusohjelmat](https://blog.zeusln.com)
- [Zeuksen tekninen dokumentaatio](https://docs.zeusln.app)



### Yhteisö ja tuki




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [sähke Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)