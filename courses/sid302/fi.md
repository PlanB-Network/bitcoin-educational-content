---
name: Liquid Bootcamp Essentials
goal: Saat kattavan käsityksen Liquid Network- ja Elements-hankkeista ja opit, miten luottamuksellisia transaktioita, tokenisointia ja hajautettua verkkoarkkitehtuuria koskevia edistyksellisiä ratkaisuja voidaan toteuttaa.
objectives: 

  - Ymmärtää Liquid-arkkitehtuurin perusteet ja sen suhde Bitcoin:een.
  - Opi konfiguroimaan ja käyttämään Liquid-solmuja Elements-ohjelmiston avulla.
  - Tutkitaan luottamuksellisten liiketoimien ja varojen liikkeeseenlaskun käyttöä Liquid Network:ssä.
  - Liquid:n liiketoiminnallisten ja teknisten näkökohtien ymmärtäminen pääomamarkkinasovelluksia varten.

---

# Liquid-verkon esittely


Lähde koulutusmatkalle, jonka tarkoituksena on antaa syvällinen käsitys Liquid Network- ja Elements-hankkeista. Tässä bootcampissa yhdistetään teoriaa ja käytäntöä, jotta opit tekniset, arkkitehtoniset ja liiketoiminnalliset perusteet, joita tarvitaan Liquid:n ominaisuuksien toteuttamiseen ja hyödyntämiseen. Tämä kurssi sopii luottamuksellisista liiketoimista ekosysteemin suunnitteluun niille, jotka haluavat laajentaa tietämystään Bitcoin-ekosysteemin kehittyneistä työkaluista.


Kurssilla käsitellään alan asiantuntijoiden esitysten avulla muun muassa Liquid-arkkitehtuuria, tokenisointisovelluksia, Elements:n teknisiä käsitteitä ja innovatiivisia käyttötapauksia, kuten Breez SDK:ta. Kurssi on suunniteltu aloittelijoille ja keskitason käyttäjille, mutta se tarjoaa arvoa myös kokeneille kehittäjille, jotka haluavat hallita Liquid:tä alustana projektiensa optimoimiseksi.

+++

# Johdanto


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Kurssin yleiskatsaus


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Tervetuloa Liquid Bootcampiin, kattavaan koulutukseen, joka on suunniteltu antamaan sinulle tiedot ja taidot, joiden avulla voit hyödyntää tehokkaasti Liquid Network- ja Elements-hankkeita. Tällä kurssilla tutustutaan kattavasti Liquid:n erityispiirteisiin, kuten Confidential Transactions:ään, omaisuuserien liikkeeseenlaskuun ja sen yhdistettyyn verkkoarkkitehtuuriin, ja samalla esitellään Elements:n, Liquid:n taustalla olevan ohjelmiston, peruskäsitteet.


Koko boot campin ajan tutustut Liquid Network:n käytännön sovelluksiin, solmujen perustamisesta ja toiminnasta sen käytön ymmärtämiseen Bitcoin:n pääomamarkkinoilla ja tokenisoinnissa. Alan asiantuntijoiden esitysten avulla saat myös tietoa edistyneistä aiheista, kuten HTLC:stä, Breez SDK:sta ja Blockstream AMP -projektista.


Tämä bootcamp toteutettiin alun perin henkilökohtaisena tapahtumana, jossa noudatettiin livenä pidettäviä istuntoja varten suunniteltua aikataulua (kuten kuvassa). Tämän kurssin mukauttamista varten sisältö on kuitenkin järjestetty uudelleen, jotta se sopisi paremmin verkkomuotoon ja helpottaisi opiskelijoiden ymmärtämistä. Uusi järjestys takaa loogisen etenemisen peruskäsitteistä edistyneempiin ja teknisempiin aiheisiin, mikä maksimoi oppimiskokemuksen.


Matka on suunniteltu siten, että se sopii eritasoisille osallistujille, ja se tarjoaa sekoituksen teoreettista tietoa ja käytännön kokemusta. Tämän boot campin lopussa sinulla on vankka käsitys Liquid:n arkkitehtuurista, sen integroinnista Bitcoin:n kanssa ja siitä, miten sen innovatiivisia ominaisuuksia voidaan hyödyntää rahoitusratkaisujen rakentamisessa ja optimoinnissa.


Sukella Liquid-sivuketjun maailmaan ja vapauta sen koko potentiaali juuri nyt!

# Perusteet


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid arkkitehtuuri


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network-arkkitehtuuri ja konsensusmalli


Liquid Network on Elements:n koodipohjaan rakennettu federoitu sivuketju, joka on suunniteltu laajentamaan Bitcoin:n ominaisuuksia ja samalla tukeutumaan sen perusturvallisuuteen. Toisin kuin Bitcoin:n [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work), Liquid toimii Federated [Consensus](https://planb.academy/resources/glossary/consensus) -mallilla. Verkkoa ylläpitää maailmanlaajuisesti hajautettu jäsenryhmä, johon kuuluu pörssejä, kaupankäyntipisteitä ja infrastruktuurin tarjoajia. Tästä jäsenkunnasta valitaan viisitoista "toiminnantekijää" toimimaan [lohkojen](https://planb.academy/resources/glossary/block) allekirjoittajina.


Nämä toimihenkilöt tuottavat lohkoja deterministisesti round-robin-muodossa, ja uusi lohko luodaan joka minuutti. Tämä tarkka ajoitus on vastakohta Bitcoin:n todennäköisille kymmenen minuutin väleille. Jotta lohko olisi pätevä, sen on oltava vähintään 11:n allekirjoittajan allekirjoittama 15:stä (kaksi kolmasosaa plus yksi). Tämä mekanismi antaa Liquid:lle "kahden lohkon lopullisuuden", mikä tarkoittaa, että kun [transaktio](https://planb.academy/resources/glossary/transaction-tx) on vahvistettu kahdesti (noin kahden minuutin kuluessa), ketjua on matemaattisesti mahdotonta järjestää uudelleen. Tämä nopeus ja varmuus ovat ratkaisevan tärkeitä arbitraasin, automaattisen kaupankäynnin ja nopean pörssien välisen selvityksen kannalta.


Liitto on dynaaminen. Dynafed-protokollan (Dynamic Federation) avulla verkko voi vaihtaa toimihenkilöitä tai päivittää parametreja ilman, että tarvitaan kovaa [fork](https://planb.academy/resources/glossary/fork):ta. Tämän ansiosta järjestelmä voi kehittyä ja vaihtaa laitteistoa tai jäseniä saumattomasti ja samalla ylläpitää jatkuvaa toimintaa.


### Confidential Transactions ja omaisuuden hallinta


Liquid:n erityispiirre on sen natiivituki Confidential Transactions:lle (CT) ja useille omaisuuserille. Bitcoin-pääketjussa kaikki transaktiotiedot - lähettäjä, vastaanottaja ja summa - ovat julkisia. Liquid:ssä CT käyttää kryptografisia sitoumuksia piilottaakseen omaisuuserän tyypin ja summan julkiselta pääkirjalta, mutta antaa verkon silti tarkistaa, että transaktio on pätevä (eli [inflaatiota](https://planb.academy/resources/glossary/inflation) ei ole tapahtunut). Ainoastaan osallistujat, joilla on sulkemisavaimet, voivat nähdä tietyt arvot, mikä tarjoaa kaupallisen yksityisyyden tason, joka on välttämätön suuria positioita siirtäville laitoksille.


Liquid käsittelee kaikkia omaisuuseriä [lohkoketjun](https://planb.academy/resources/glossary/blockchain) "alkuperäisinä" kansalaisina. Tämä sisältää Liquid Bitcoin (LBTC), vakaat kolikot, kuten USDT, ja turvamerkit. Omaisuuserän liikkeeseenlasku ei vaadi monimutkaisia älykkäitä sopimuksia, vaan se on protokollan perustoiminto.


#### Säännellyt varat ja AMP

Liquid käyttää Blockstream Asset Management Platformia (AMP) vaatimustenmukaisuutta vaativiin omaisuuseriin, kuten arvopaperimerkkeihin. Tämä ottaa käyttöön luvanvaraisen kerroksen, jossa tapahtumat vaativat toisen allekirjoituksen valtuutuspalvelimelta. Näin liikkeeseenlaskijat voivat valvoa sääntöjä - kuten Whitelisting- tai KYC-vaatimuksia - rakeisella tasolla, jolloin lohkoketjun tehokkuus yhdistyy perinteisen rahoituksen sääntelyvalvontaan.


### Kaksisuuntainen peg ja turvallisuusinfrastruktuuri


Yhteys Liquid:n ja Bitcoin:n välillä säilyy kaksisuuntaisen tapin kautta. Käyttäjä lähettää Bitcoin:n mainchain:ssä luotuun osoitteeseen. Nämä varat on lukittu 102 vahvistuksen ajaksi (noin 17 tuntia) uudelleenjärjestelyriskien eliminoimiseksi. Kun ne on vahvistettu, vastaava määrä LBTC:tä lyödään Liquid:n sivuketjussa.


"Peg-out"-prosessin avulla käyttäjät voivat lunastaa LBTC:n Bitcoin:ksi. Tämä edellyttää LBTC:n polttamista ja federaation kryptografista valtuutusta. Varkauksien estämiseksi peg-out-menetelmää valvotaan tiukasti federaation jäsenten hallussa olevilla Peg-out Authorization Keys (PAK) -avaimilla. Lisäksi varoja voidaan vaihtaa välittömästi kolmansien osapuolten, kuten SideSwapin, kautta, jolloin selvitysviive ohitetaan ja likviditeetti nopeutuu.


#### Laitteiston turvamoduulit (HSM)

Tietoturva varmistetaan tiukasti laitteiston avulla. Toimijat eivät pidä [yksityisiä avaimia](https://planb.academy/resources/glossary/private-key) tavallisilla palvelimilla, vaan käyttävät laitteiston turvamoduuleja (Hardware Security Modules, HSM). Nämä laitteet on erotettu isäntäpalvelimen logiikasta, ja ne on ohjelmoitu tiukkojen sääntöjen mukaisesti. HSM esimerkiksi kieltäytyy allekirjoittamasta lohkoa, jos sen korkeus ei ole suurempi kuin edellisen lohkon korkeus, mikä estää historian uudelleenkirjoittamisen. Tässä "vastarinnan" suojausmallissa oletetaan, että isäntäpalvelin voidaan vaarantaa, jolloin varmistetaan, että avaimet pysyvät turvassa, vaikka fyysinen sijainti murrettaisiinkin.


## Elements:n perusteet


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Liquid:n perusta


Elements on avoimen lähdekoodin lohkoketjualusta, joka perustuu Bitcoin Core -koodipohjaan. Se laajentaa Bitcoin:n toiminnallisuutta mahdollistamalla sivuketjuista riippumattomat lohkoketjut, jotka voivat siirtää varoja Bitcoin:een ja Bitcoin:sta. Bitcoin Core käyttää Bitcoin-verkkoa, mutta Elements on Liquid Network:n ja muiden mukautettujen sivuketjujen taustalla oleva ohjelmistomoottori.


Suhde on suoraviivainen: Liquid on Elements-sivuketjun erityinen "instanssi", joka on konfiguroitu tuotantokäyttöön federoitua konsensusmallia varten. Bitcoin:n tuntevat kehittäjät pitävät Elements:tä intuitiivisena, koska siinä on sama RPC:n (Remote Procedure Call) käyttöliittymä ja komentorivirakenne (`elements-cli`, `elements-d`, `elements-qt`). Keskeinen ero on konfiguroinnissa: asetus `chain=liquidv1` yhdistää [solmun](https://planb.academy/resources/glossary/node) Liquid-pääverkkoon, kun taas `chain=elementsregtest` käynnistää paikallisen regressiotestausympäristön, jossa kehittäjät voivat generate-lohkoja välittömästi ja testata ilman ulkoisia riippuvuuksia.


#### Omaisuuserien liikkeeseenlasku

Elements:n erikoisominaisuus on omaisuuserien liikkeeseenlasku. Toisin kuin Ethereumissa, jossa tokenit ovat monimutkaisia älykkäitä sopimuksia, Elements:ssä omaisuuserät ovat ensimmäisen luokan kansalaisia, jotka luodaan yksinkertaisella RPC-komennolla (issueasset).


- Yksilölliset tunnisteet:** Jokainen omaisuuserä saa yksilöllisen 64-merkkisen heksadesimaalisen tunnisteen.
- Reissuance Tokens:** Liikkeeseenlaskijat voivat valinnaisesti luoda reissuance-tunnuksia, jotka antavat haltijalleen oikeuden lyödä myöhemmin lisää omaisuuseriä (hyödyllinen stablecoineille tai arvopaperitunnuksille).
- Vararekisteri:** Koska heksatunnukset eivät ole ihmiselle luettavissa, Blockstream-vararekisteri muuntaa nämä tunnukset nimiksi ja tickereiksi (esim. "USDT"), kuten DNS-varat.


### Yksityisyys Confidential Transactions:n kautta


Elements puuttuu yhteen julkisten lohkoketjujen tärkeimmistä rajoituksista: kaupallisen yksityisyyden puuttumiseen. Bitcoin:ssa jokainen transaktiomäärä näkyy koko maailmalle. Elements:ssä otetaan käyttöön **Confidential Transactions (CT)**, joka kryptografisesti peittää summan ja omaisuuserätyypin, mutta sallii silti verkon tarkistaa transaktion oikeellisuuden.


Tämä saavutetaan käyttämällä **Pedersen-sitoumuksia** ja **Range Proofs**.


- Pedersen-sitoumukset** korvaavat näkyvän määrän kryptografisella sitoumuksella. Homomorfisen salauksen ansiosta validoijat voivat tarkistaa, että *Input Commitments = Output Commitments + Fees* näkevät todelliset arvot näkemättä niitä koskaan.
- Alueen todistukset** estävät käyttäjää luomasta rahaa tyhjästä (esim. käyttämällä negatiivisia lukuja) todistamalla matemaattisesti, että piilotettu arvo on positiivinen kokonaisluku kelvollisella alueella.


Ulkopuoliselle tarkkailijalle luottamuksellinen transaktio näyttää oikeat tulot ja lähdöt, mutta se peittää *mitä* lähetetään ja *paljon*. Ainoastaan lähettäjä ja vastaanottaja (joilla on sokeuttavat avaimet) voivat nähdä selvätekstitiedot.


### Kehitys ja RPC-työnkulku


Vuorovaikutus Elements-solmun kanssa tapahtuu pääasiassa sen JSON-RPC-rajapinnan kautta. Näin Pythonilla, JavaScriptillä tai Go-kielellä kirjoitetut sovellukset voivat kommunikoida lohkoketjun kanssa.



- Asennus:** Kehittäjä aloittaa tyypillisesti `regtest`-tilassa. Tämä mahdollistaa lohkojen välittömän luomisen (`generateblock`), jotta transaktiot voidaan vahvistaa välittömästi, jolloin ohitetaan live-verkon 1 minuutin lohkoaika.
- Komennot:** Bitcoin:n vakiokomennot, kuten `getblockchaininfo`, ovat käytettävissä, samoin kuin Elements-kohtaiset komennot, kuten `dumpblindingkey` (CT:iden auditointiin) tai `pegin` (BTC:n siirtämiseen sivuketjuun).
- Aliakset:** Useiden solmujen hallitsemiseksi (esim. "lähettäjä" ja "vastaanottaja" testausta varten) kehittäjät käyttävät usein komentotulkin aliaksia, kuten `e1-cli` ja `e2-cli`, jotka osoittavat eri datahakemistoihin, simuloiden [vertaisverkkoa](https://planb.academy/resources/glossary/peertopeer-p2p) yhdellä koneella.


Tämän arkkitehtuurin avulla kehittäjät voivat rakentaa kehittyneitä rahoitussovelluksia, kuten arvopaperialustoja tai yksityisiä maksuportaita, Bitcoin-ekosysteemin vankkojen ja tuttujen työkalujen avulla.


## Bitcoin-kerrosten yhdistäminen


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Layer:n rajat ylittävä infrastruktuuri ja HTLC:t


Bitcoin-ekosysteemi on kehittynyt monikerroksiseksi arkkitehtuuriksi, jossa Mainchain tarjoaa selvityksen, Lightning nopeuden ja Liquid kehittyneet omaisuuseräominaisuudet. Arvon siirtäminen näiden kerrosten välillä ilman keskitettyjä välikäsiä edellyttää luotettavaa kryptografista primitiiviä: [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


HTLC luo ehdollisen [maksukanavan](https://planb.academy/resources/glossary/payment-channel), joka yhdistää itsenäiset järjestelmät atomisesti. Se toimii kahden ensisijaisen rajoituksen avulla: **hash-lukko** ja **aikalukko**.


- Hash-lukko:** Varat voidaan käyttää välittömästi, jos vastaanottaja paljastaa salaisen "esikuvan", joka vastaa tiettyä kryptografista hash-määritystä.
- Aikalukko:** Jos vastaanottaja ei paljasta salaisuutta tietyn ajan kuluessa (lohkon korkeus), alkuperäinen lähettäjä voi vaatia varat takaisin.


Tämä kaksitie rakenne takaa turvallisuuden. Ristikkäisessä vaihdossa samaa hash-lukkoa käytetään molemmissa verkoissa. Kun vastaanottaja paljastaa salaisuuden lunastaakseen varoja yhdessä kerroksessa (esim. Liquid), salaisuus tulee näkyviin lähettäjälle, joka voi käyttää sitä lunastaakseen vastavuoroisesti varoja toisessa kerroksessa (esim. Lightning). Tämä kryptografinen sitoumus takaa, että vaihto joko onnistuu molempien osapuolten osalta tai epäonnistuu molempien osalta, mikä poistaa riskin siitä, että toinen osapuoli menettää varoja, kun toinen saa niitä.


### Taproot ja MuSig2 päivitys


Vanhat HTLC:t ([SegWit](https://planb.academy/resources/glossary/segwit) v0) toimivat hyvin, mutta kärsivät yksityisyyden suojaan ja tehokkuuteen liittyvistä puutteista. Ne edellyttivät koko käsikirjoituslogiikan on-chain:n julkaisemista, mikä teki vaihtotapahtumista helposti tunnistettavia lohkoketjuanalyytikoille ja kalliimpia niiden datakoon vuoksi. [Taproot](https://planb.academy/resources/glossary/taproot):n (SegWit v1) ja MuSig2-protokollan käyttöönotto mullisti tämän arkkitehtuurin.


Taproot sallii **avainten yhdistämisen** MuSig2:n kautta. Sen sijaan, että paljastettaisiin monimutkainen [käsikirjoitus](https://planb.academy/resources/glossary/script), jossa on useita [julkisia avaimia](https://planb.academy/resources/glossary/public-key), MuSig2:n avulla vaihtoon osallistujat voivat yhdistää avaimensa yhdeksi yhdistetyksi julkiseksi avaimeksi.


- Yhteistyöhön perustuva "avainpolku":** Jos molemmat osapuolet hyväksyvät swapin ("onnellinen polku"), he allekirjoittavat transaktion. Verkon silmissä tämä näyttää samanlaiselta kuin tavallinen, yhden allekirjoituksen maksu. Se kuluttaa minimaalisen vähän lohkotilaa eikä paljasta mitään tietoa swap-ehdoista.
- Vastapuolen "käsikirjoituspolku":** Jos toinen osapuoli ei vastaa tai on pahansuopa, taustalla oleva käsikirjoitus (joka sisältää hash-/aikalukot) paljastuu vasta silloin. Tämä on järjestetty [Merkle-puuksi](https://planb.academy/resources/glossary/merkle-tree), jolloin rehellinen osapuoli voi paljastaa vain sen haaran, jota tarvitaan varojen takaisin saamiseksi, ja pitää muun sopimuslogiikan piilossa.


### Käytännön toteutus: Liquid-Lightning Swaps


Käytännössä nämä protokollat mahdollistavat saumattoman vuorovaikutuksen Bitcoin:n kerrosten välillä. Tyypillinen Liquid:stä Lightningiin tapahtuva vaihto alkaa siten, että asiakas pyytää vaihtoa palveluntarjoajalta. Asiakas toimittaa [Lightning-laskun](https://planb.academy/resources/glossary/invoice-lightning), ja palveluntarjoaja lukitsee vastaavan Liquid Bitcoin:n (L-BTC) Taproot-käytössä olevaan HTLC-osoitteeseen.


Atomisuus toteutuu, kun maksu suoritetaan. L-BTC:n lunastamiseksi palveluntarjoajalla on oltava esikuva. Se saa tämän preimagen vain, kun se maksaa asiakkaan Lightning-laskun onnistuneesti. Kun Lightning-maksu on suoritettu, preimage paljastuu, jolloin palveluntarjoaja voi vapauttaa Liquid-varat.


#### Wallet Abstraktio ja UTXO Hallinta

Loppukäyttäjille tämä monimutkaisuus on täysin abstraktia. Nykyaikaiset lompakot, kuten Aqua, hoitavat avainten luomisen, laskujen laatimisen ja allekirjoittamisen taustalla. Käyttäjä yksinkertaisesti "maksaa" Lightning-laskun Liquid-saldollaan. Kulissien takana palvelu hallinnoi [UTXO](https://planb.academy/resources/glossary/utxo):n konsolidointia, pyyhkäisee säännöllisesti pienet, lunastamattomat tai palautetut tuotot, jotta [wallet](https://planb.academy/resources/glossary/wallet):n tehokkuus säilyy ja maksuvaikutukset minimoituvat vilkkaina kausina.


## Liquid Network Yleiskatsaus


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arkkitehtuuri ja konsensus


Liquid Network toimii yhdistettynä sivuketjuna, joka perustuu **Elements**-koodipohjaan. Elements - fork Bitcoin Core - tarjoaa ohjelmistoperustan, mutta Liquid on tuotantoverkon toteutus. Toisin kuin Bitcoin:n Proof-of-Work, joka perustuu kilpailevaan [mining](https://planb.academy/resources/glossary/mining):ään, Liquid käyttää **Federated Consensus** -mallia.


Verkostoa ylläpitää viisitoista maailmanlaajuisesti hajautettua "toimihenkilöä" Nämä yksiköt käyttävät erikoistuneita palvelimia, joilla on kaksi kriittistä tehtävää:

1.  **Lohkotuotanto:** Toimihenkilöt luovat vuorotellen lohkoja deterministisessä round-robin-aikataulussa, jolloin uusi lohko syntyy täsmälleen joka minuutti.

2.  **Lohkon allekirjoittaminen:** Jotta lohko olisi pätevä, sen on oltava vähintään 11:n allekirjoittajan allekirjoittama 15:stä.


Tämä 11:stä 15:een -kynnys varmistaa, että verkko kestää jopa neljän solmun vian pysähtymättä. Tämän kompromissin ensisijainen etu on **deterministinen lopullisuus**. Bitcoin:ssä käytetään todennäköisyyksiä, kun taas Liquid:ssä saavutetaan ratkaisuvarmuus kahden lohkon (noin kahden minuutin) jälkeen. Kun lohkon päälle on saatu yksi vahvistus, ketjua ei voida järjestää uudelleen, joten se on erittäin tehokas arbitraasiin ja nopeaan selvitykseen.


### Confidential Transactions ja alkuperäiskansojen omaisuuserät


Liquid:n ominaispiirre on **Confidential Transactions (CT)**:n oletuskäyttö. Bitcoin mainchain:ssa lähettäjä, vastaanottaja ja määrä ovat julkisia. Liquid parantaa tätä salaamalla summan ja omaisuuserätyypin, mutta jättää lähettäjän ja vastaanottajan osoitteet näkyviin tarkistusta varten.


Liquid käyttää **Pedersen-sitoumuksia** ja **Range Proofs** sen varmistamiseksi, että käyttäjä ei voi tulostaa rahaa (esim. lähettämällä negatiivisia summia). Näiden salausmenetelmien avulla verkko voi todentaa, että *Syötteet = Tuotokset + Maksut* ja että kaikki arvot ovat positiivisia kokonaislukuja, paljastamatta koskaan tiettyjä lukuja julkiseen pääkirjaan. Ainoastaan osallistujat, joilla on salausavaimet, voivat nähdä puretut tiedot.


#### Omaisuuserien liikkeeseenlasku

Liquid käsittelee kaikkia omaisuuseriä "alkuperäisinä" Olipa kyseessä Liquid Bitcoin (L-BTC), vakaa kolikko, kuten USDT, tai arvopaperi token, niillä kaikilla on sama arkkitehtuuri. Omaisuuserän liikkeeseenlasku ei vaadi älykkäitä sopimuksia, vaan ainoastaan yksinkertaisen RPC-kutsun.


- Sääntelemättömät omaisuuserät:** Kuka tahansa voi myöntää niitä ilman lupaa.
- Säännellyt omaisuuserät:** Blockstream Asset Management Platformin (AMP) avulla liikkeeseenlaskijat voivat valvoa sääntöjen noudattamista (kuten KYC/AML) vaatimalla toisen allekirjoituksen valtuutuspalvelimelta ennen kuin omaisuuserä voidaan siirtää.


### Kahdensuuntainen kiinnitys ja dynaaminen liitto


Bitcoin:n ja Liquid:n välinen silta on **kaksisuuntainen tappi**. Sen avulla käyttäjät voivat siirtää BTC:tä sivuketjuun (Peg-in) ja takaisin mainchain:een (Peg-out).


**Hyllyttämisprosessi:**

Tämä on luvatonta. Käyttäjä lähettää BTC:tä federaation valvomaan osoitteeseen. Bitcoin-lohkoketjun uudelleenjärjestelyiltä suojautuakseen näiden varojen on odotettava **102 vahvistusta** (noin 17 tuntia) ennen kuin vastaava L-BTC lyödään sivuketjussa.


**Peg-out-prosessi:**

Bitcoin:een palaamiseksi L-BTC poltetaan. Bitcoin-varantojen varastamisen estämiseksi peg-out ei kuitenkaan ole täysin automatisoitu. Ne edellyttävät valtuutusta jäseneltä, jolla on **Peg-Out Authorization Key (PAK)**. Itse Bitcoin-varat on suojattu 11:sta 15:een wallet:n moniäänisellä allekirjoituksella, jonka avaimia säilytetään HSM-moduuleissa (Hardware Security Modules), jotka ovat ilmakaapeleissa toiminnonharjoittajien pääpalvelimista.


**Dynaaminen liitto (Dynafed):**

Pitkäikäisyyden varmistamiseksi Liquid käyttää Dynafed-protokollaa, jonka avulla verkko voi vaihtaa toimihenkilöitä tai päivittää parametreja ilman kovaa fork. Jos toimihenkilö on vaihdettava, verkko lähettää siirtymätapahtuman. Kahden viikon päällekkäisjakson jälkeen uusi konfiguraatio astuu tilalle, jolloin liitto voi kehittyä saumattomasti ja ylläpitää jatkuvaa käyttöaikaa.


## Ekosysteemi ja pääomamarkkinat


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Liiketoimintastrategia ja ekosysteemi


Liquid on enemmän kuin tekninen sivuketju; se on liiketoimintaan keskittyvä infrastruktuurikerros, joka on suunniteltu käsittelemään pääomamarkkinoiden monimutkaisia vaatimuksia, joita Bitcoin mainchain ei pysty tehokkaasti tukemaan. [Lightning Network](https://planb.academy/resources/glossary/lightning-network) on optimoitu suurtaajuusmaksuja ja vähäarvoisia maksuja varten, kun taas Liquid on suunnattu suurten arvojen siirtoihin, omaisuuserien liikkeeseenlaskuun ja pörssien väliseen selvitykseen.


Ekosysteemiä vetää **Liquid Federation**, joka on noin 73 yrityksen yhteenliittymä, johon kuuluu pörssejä, kaupankäyntipisteitä ja infrastruktuurin tarjoajia. Tämä yhteistoimintamalli vastaa perinteisiä rahoitusalan selvityskeskuksia, mutta se toimii avoimemmin ja huomattavasti lyhyemmällä toimitusajalla (2 minuuttia verrattuna T+2 päivään).


### Reaalimaailman omaisuuden (RWA) tokenisointi


Liquid:n keskeinen liiketoiminta-ajatus on "tokenisointi" - reaalimaailman arvon (osakkeet, joukkovelkakirjat, mining-sopimukset) esittäminen digitaalisena tokenina lohkoketjussa. Tämä tarjoaa kolme ensisijaista etua:

1.  **24/7 Global Markets:** Pankkiaikojen ja maantieteellisten rajoitusten poistaminen.

2.  **Toiminnallinen tehokkuus:** Yhteisen, muuttumattoman pääkirjan avulla eliminoidaan täsmäytysvirheet.

3.  **Atomic Settlement:** Vähentää vastapuoliriskiä varmistamalla, että toimitus tapahtuu samanaikaisesti maksun kanssa.


#### Säännellyt varat ja AMP

Useimmat institutionaaliset varat eivät voi käydä kauppaa luvattomasti oikeudellisten vaatimusten vuoksi. **Asset Management Platform (AMP)** on tekninen standardi, jolla nämä säännöt pannaan täytäntöön.


- Whitelisting:** Liikkeeseenlaskijat voivat rajoittaa hallussapidon ja kaupankäynnin KYC-varmennettuihin osoitteisiin.
- Multisig-valvonta:** Vaatimustenmukaisuuteen liittyviä toimia (kuten varastettujen varojen jäädyttämistä tai kadonneiden tunnisteiden palauttamista) hallitaan usean allekirjoituksen valtuutuksen avulla, jolloin varmistetaan, ettei yksikään työntekijä voi toimia yksipuolisesti.


Tämä infrastruktuuri on käytössä tänään. Alustat, kuten **Stalker**, tarjoavat päästä päähän - tokenisaatiopalveluja Euroopassa, kun taas **Sideswap** toimii hajautettuna pörssinä ja wallet:n ei-säilytysjärjestelmänä, joka mahdollistaa vertaiskaupankäynnin omaisuuserillä, kuten **Blockstream Mining -setelillä (BMN)** ja tokenisoiduilla MicroStrategy-osakkeilla (CMSTR).


### Todellisen maailman menestys: Mayfellin tapaustutkimus


Vakuuttavin todiste Liquid:n hyödyllisyydestä on peräisin Meksikossa sijaitsevasta **Mayfellistä**. Markkinoilla, joilla perinteinen rahoitus perustuu paperisiin velkakirjoihin, jotka ovat alttiita katoamiselle, petoksille ja hitaalle käsittelylle, Mayfell siirsi koko infrastruktuurin Liquid:een.



- Mittakaava:** Yli 25 000 annettua velkakirjaa, joiden arvo on yli 1,5 miljardia dollaria**.
- Tietosuoja:** Liquid:n Confidential Transactions:n avulla lainasummat näkyvät vain lainanantajalle ja lainanottajalle, mikä säilyttää kaupallisen yksityisyyden ja antaa tilintarkastajille mahdollisuuden tarkistaa pääkirjan eheyden.
- Vaikutus:** Yhdistämällä pankkien ulkopuoliset lainanantajat globaaleille pääomamarkkinoille lohkoketjun avulla Mayfell vähensi kustannuksia ja laajensi meksikolaisten pk-yritysten luotonsaantia, mikä osoittaa, että Liquid:n arvolupaus ulottuu pitkälle spekulatiivisen kaupankäynnin ulkopuolelle.


### Strateginen asemointi verrattuna muihin ketjuihin


Liquid kilpailee tokenisointialustojen (Ethereum, Solana jne.) ruuhkaisilla markkinoilla, mutta sillä on selviä strategisia etuja:


- Sääntelyn selkeys:** Liquid käyttää Bitcoin:tä (L-BTC) alkuperäisenä omaisuuseränään. Sillä ei ole valmiiksi louhittua token:ää eikä ICO:ta, joten se välttää "rekisteröimättömän arvopaperin" riskit, jotka vaivaavat muita L1-lohkoketjuja.
- Vakaus:** Toisin kuin Ethereumin tilimallissa, jossa epäonnistuneet transaktiot polttavat edelleen kaasumaksuja, Liquid:n UTXO-malli on deterministinen ja luotettava kriittisille rahoitustiedoille.
- Tietosuoja:** Useimmat rahoituslaitokset vaativat oletusarvoista luottamuksellisuutta, ja Liquid tarjoaa ominaisuuden, jota julkisten ketjujen on vaikea toteuttaa ilman monimutkaisia lisäosia.


Kehittäjille tämä ekosysteemi tarjoaa selkeän mahdollisuuden: sellaisten työkalujen (kojelautojen, lompakoiden, vaatimustenmukaisuusintegraatioiden) rakentaminen, jotka yhdistävät perinteisen rahoituksen ja Bitcoin:n turvallisen selvityskerroksen.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Liquid:n luvanvarainen omaisuudenvalvonta


Blockstream AMP (Asset Management Platform) toimii Liquid Network:n kriittisenä infrastruktuurikerroksena, joka on suunniteltu erityisesti säänneltyjen digitaalisten arvopapereiden ja stabiilien kolikoiden liikkeeseenlaskijoille. Vaikka Liquid tarjoaa luvanvaraisen pohjakerroksen, jossa on natiivien omaisuuserien liikkeeseenlasku, säännellyt yksiköt vaativat usein tiukkaa valvontaa ja vaatimustenmukaisuusominaisuuksia. AMP kuroo tämän kuilun umpeen ottamalla käyttöön luvanvaraisen valvontakerroksen tietyille omaisuuserille tinkimättä Liquid:n Confidential Transactions:n yksityisyyseduista.


Alustan keskeinen arvolupaus perustuu kahteen ensisijaiseen ominaisuuteen: kattavaan liikkeeseenlaskijanäkyvyyteen ja tapahtumien valtuuttamiseen. Toisin kuin tavanomaisissa Liquid-varoissa, joissa määrät ja tyypit ovat blinded kaikille muille paitsi osallistujille, AMP-varat antavat liikkeeseenlaskijalle mahdollisuuden ylläpitää täysin unblinded-tarkistusketjua. Tämä läpinäkyvyys on olennaisen tärkeää viranomaisraportoinnin ja sisäisten tarkastusten kannalta. Lisäksi AMP:ssä noudatetaan tiukkaa valtuutusmallia yhteisalennusmekanismin avulla. Jokainen AMP-varojen siirto edellyttää AMP-palvelimen allekirjoitusta. Tämän ansiosta liikkeeseenlaskijat voivat panna täytäntöön monimutkaisia off-chain-sääntöjä, kuten tilien jäädyttämistä, akkreditoitujen sijoittajien valkoisen listan laatimista tai siirtorajojen asettamista, ja toimia tehokkaasti keskitettynä portinvartijana hajautetussa verkossa.


#### Operatiiviset kompromissit

Tämä arkkitehtuuri tuo mukanaan erityisiä kompromisseja. Järjestelmä on riippuvainen AMP-palvelimen käytettävyydestä; jos palvelin toimii toisena allekirjoittajana ja menee offline-tilaan, varojen likviditeetti pysähtyy. Lisäksi vaikka käyttäjien välinen yksityisyys säilyy, sijoittajien on hyväksyttävä, että liikkeeseenlaskijalla on täysi näkyvyys heidän omistuksiinsa. Tämä malli on ihanteellinen sääntöjen mukaisille arvopaperilähteille, mutta ei sovellu sensuurin kestäviin [kryptovaluuttoihin](https://planb.academy/resources/glossary/cryptocurrency).


### Arkkitehtuurin kehitys ja integraatiopolut


AMP-ekosysteemi on parhaillaan siirtymässä ensimmäisestä versiostaan joustavampaan ja yhteentoimivampaan "versio 2" -arkkitehtuuriin. Vanhassa järjestelmässä liikkeeseenlaskijoiden oli ylläpidettävä täysin synkronoituja Elements-solmuja, ja kehittäjien oli pakko luottaa pitkälti monoliittiseen Green SDK:hon. Vaikka järjestelmä oli toimiva, se loi suuria teknisiä esteitä markkinoille pääsylle ja rajoitti wallet-valintoja.


Seuraavan sukupolven arkkitehtuuri yksinkertaistaa näitä vaatimuksia siirtämällä monimutkaisuutta palvelimelle. Tässä uudessa mallissa AMP-palvelin huolehtii transaktioiden rakentamisen, UTXO:n valinnan ja maksujen laskennan raskaista tehtävistä. Se esittää liikkeeseenlaskijalle osittain allekirjoitetun Elements-transaktion (PSET), joka tarvitsee vain allekirjoituksen. Tämä "älykäs palvelin, tyhmä wallet" -lähestymistapa poistaa liikkeeseenlaskijoilta tarpeen käyttää kokonaisia solmuja ja mahdollistaa laitteistolompakoiden ja vakiomuotoisten moniallekirjoituskokoonpanojen käytön kassanhallinnassa.


Kehittäjien kannalta tämä kehitys tarkoittaa siirtymistä pois omista SDK:ista kohti standardoituja kuvaajia ja PSET-työnkulkuja. Lompakot voivat nyt rekisteröidä AMP-palvelimelle monisignatuuriset kuvaajat valtuutusoikeuksien määrittämiseksi. Tämä yhdenmukaistaa AMP-kehityksen laajempien Bitcoin wallet-standardien kanssa, mikä mahdollistaa integroinnin mihin tahansa sovellukseen, joka pystyy käsittelemään PSBT/PSET-muotoja. Tämänhetkisiä kehittäjiä kannustetaan käyttämään Liquid Wallet Kitin (LWK) kaltaisia työkaluja, jotka tukevat näitä nykyaikaisia, kuvaajiin perustuvia arkkitehtuureja ja varmistavat, että heidän sovelluksensa ovat tulevaisuudenkestäviä uusia AMP-standardeja varten.


### Liquid Wallet -ekosysteemi ja luottamuksellisuus


Sovellusten rakentaminen Liquid:lle vaatii monimutkaisemman pinoamisen kuin tavallinen Bitcoin-kehitys, koska se sisältää natiivien ominaisuuksien ja Confidential Transactions:n kaltaisia ominaisuuksia. Ekosysteemiä tukee kerroksellinen arkkitehtuuri: matalan tason kirjastot, kuten `secp256k1-zkp`, käsittelevät salausalgoritmeja, kun taas korkeamman tason työkalupaketit hallitsevat wallet-logiikkaa.


Aikaisemmin Green Development Kit (GDK) tarjosi kattavan mutta jäykän ratkaisun. Nykyaikainen vaihtoehto on Liquid Wallet Kit (LWK), joka tarjoaa modulaarisen lähestymistavan. LWK jakaa huolenaiheet erillisiin laatikoihin, jotka käsittelevät kuvaajia, allekirjoitusta ja laitteistokommunikaatiota itsenäisesti, mikä antaa kehittäjille joustavuutta rakentaa mukautettuja ratkaisuja ilman monoliittisen kirjaston aiheuttamia yleiskustannuksia.


#### Confidential Transactions:n käsittely

Tämän ekosysteemin suurin haaste on sokeuden elinkaaren hallinta. Liquid:ssä transaktiotulosteet salataan käyttämällä Elliptic Curve Diffie-Hellman (ECDH) -avaintenvaihtoa. Lähettäjä käyttää vastaanottajan julkista avainta salatakseen omaisuuserien määrät ja tyypit, jolloin syntyy todiste, joka todentaa tapahtuman pätevyyden paljastamatta arvoja.


Jotta wallet toimisi, sen on onnistuttava kääntämään tämä prosessi. Kun wallet havaitsee saapuvan tapahtuman, se yrittää poistaa lähdön sokkoutuksen yksityisen sokkoutusavaimensa avulla. Jos jaettu salaisuus täsmää, wallet voi purkaa arvon ja lisätä sen käyttäjän saldoon. Tämä prosessi on laskennallisesti intensiivinen ja vaatii sokaistuskertoimien tarkkaa hallintaa, jotta voidaan varmistaa, että transaktiot ovat matemaattisesti tasapainossa, ja LWK:n kaltaiset työkalut pyrkivät poistamaan tämän monimutkaisuuden kehittäjältä.


# Tekninen


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Breez Liquid SDK:n käyttöönotto


Breez Liquid SDK on avoimen lähdekoodin työkalupakki, joka on suunniteltu kuromaan umpeen kuilu Liquid Network:n ja laajemman Bitcoin-ekosysteemin välillä. Sen ensisijaisena tehtävänä on abstrahoida Lightning Network-solmujen hallinnan ja atomivaihtojen monimutkaisuus, jotta kehittäjät voivat rakentaa kitkattomia rahoitussovelluksia.


Ydinlogiikka on kirjoitettu Rust-kielellä suorituskyvyn ja turvallisuuden vuoksi, mutta se hyödyntää UniFFI:tä (Unified Foreign Function Interface) tarjotakseen natiivisidoksia Kotlinille, Swiftille, Pythonille, C#:lle, Dartille ja Flutterille. Näin varmistetaan, että kehittäjät voivat integroida Bitcoin-toiminnot haluamaansa ympäristöön ilman matalan tason salausoperaatioiden hallintaa.


**Tuetut tapahtumatyypit:**

SDK toimii Liquid:n kanssa "kotipesänä" Se on erinomainen kolmessa erityisessä toiminnassa:

1.  **Liquid-Liquid:** Suorat on-chain-siirrot.

2.  **Liquid-to-Lightning:** Lightning-laskujen maksaminen Liquid-varoilla.

3.  **Liquid-Bitcoin:** Varojen vaihtaminen suoraan Bitcoin mainchain:een.


*Huomautus: SDK ei tue suoria Lightning-to-Lightning- tai Bitcoin-Bitcoin-tapahtumia. Se on puhtaasti Liquid-keskeinen työkalu.*


### Maksuarkkitehtuurit: Submarine Swaps


Liquid:n, Lightningin ja Bitcoin:n välisen yhteentoimivuuden saavuttamiseksi ilman keskitettyjä säilyttäjiä Breez käyttää **Submarine Swap -järjestelmää**. Nämä ovat atomisia operaatioita, joissa transaktio joko suoritetaan onnistuneesti molemmissa verkoissa tai epäonnistuu molemmissa verkoissa, jolloin varmistetaan, että varoja ei koskaan menetetä kuljetuksen aikana.


#### Lightning Send (Sukellusveneen vaihto)

Kun käyttäjä maksaa Lightning-laskun, SDK lähettää Liquid Network:een "lock-up"-tapahtuman. Näin varat siirretään käytännössä tileille. Swap-palveluntarjoaja (Boltz) havaitsee tämän, maksaa Lightning-laskun ja käyttää sitten maksun esikuvaa (kryptografista kuittia) lunastaakseen lukitut Liquid-varat.


#### Lightning Receive (Käänteinen sukellusveneen vaihto)

Salaman vastaanottaminen on käänteinen prosessi. Käyttäjä luo laskun, ja swap-palveluntarjoaja lukitsee varat Lightning Network:ään. SDK valvoo tätä prosessia WebSocketsin kautta. Kun lukitus on vahvistettu, SDK suorittaa automaattisesti saantotapahtuman, jolla vastaavat varat siirretään käyttäjän Liquid wallet:een.


#### Ristiketju Bitcoin

Liquid:n ja Bitcoin:n välisissä siirroissa arkkitehtuuri käyttää "dual-swap"-mekanismia. Lukitustapahtumat tapahtuvat molemmissa ketjuissa samanaikaisesti. Lähettäjä hakee varoja Bitcoin:stä ja vastaanottaja Liquid:stä. Tämä mahdollistaa luotettavan siltaamisen ilman federated peg-ulkoistuksia tai keskitettyjä vaihtoja.


### Kehittäjä Interface ja automatisoitu hallinta


Breez SDK yksinkertaistaa kehittäjäkokemusta tiivistämällä monimutkaiset rahoitusvirrat standardoituun kolmivaiheiseen prosessiin: **Connect, Prepare ja Execute**.


1.  **Connect:** Alustaa wallet:n, synkronoi lohkoketjun kanssa Liquid Wallet Kitin (LWK) avulla ja luo WebSocket-yhteydet reaaliaikaista seurantaa varten.

2.  **Prepare:** Ennen varojen sitomista tämä vaihe laskee ja palauttaa kaikki verkkomaksut ja swap-kustannukset, jolloin käyttöliittymä esittää käyttäjälle selkeän loppusumman.

3.  **Toteutus:** Tässä vaiheessa rakennetaan transaktio, lähetetään se ja käynnistetään vaihto.


#### Automaattiset turvamekanismit

Yksi SDK:n tärkeimmistä ominaisuuksista on **automaattinen palautusten hallinta**. Verkkovian tai yhteistyöhaluttoman vastapuolen tapauksessa varat voivat teoriassa juuttua aikarajoitettuun sopimukseen. SDK abstrahoi palautuslogiikan kokonaan. Se valvoo jokaisen swap-sopimuksen tilaa; jos swap-sopimus epäonnistuu tai sen voimassaoloaika päättyy, SDK rakentaa ja lähettää automaattisesti palautustapahtuman, jolla varat palautetaan käyttäjän wallet:een.


Lisäksi SDK käsittelee **Metatietojen resoluution**. Se yhdistää off-chain:n swap-tiedot (jotka Boltz:n swap-operaattori toimittaa) on-chain:n tapahtumahistoriaan. Näin varmistetaan, että käyttäjän tapahtumahistoria on ihmisen luettavissa ja näyttää laskun yksityiskohdat ja maksukontekstin eikä pelkkiä raakoja heksadesimaalisia tapahtumahashhejä.


# Viimeinen jakso


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Arvostelut & arvostelut


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Loppukoe


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Päätelmä


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>