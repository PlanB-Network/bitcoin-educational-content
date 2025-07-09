---
name: Bitcoin:n kehitysfilosofia
goal: Bitcoin:n suunnitteluperiaatteiden syvällinen filosofinen ymmärtäminen.
objectives: 

  - Analysoidaan Bitcoin:n perustavanlaatuisia puolustukseen liittyviä kompromisseja ja arkkitehtuuripäätöksiä
  - Opi arvioimaan Bitcoin-protokollaan ehdotettuja muutoksia ja innovaatioita
  - Kooste yli kymmenen vuoden ajalta Bitcoin:n kehityshistoriasta ja yhteisön keskusteluista
  - Soveltaa kriittisen ajattelun kehyksiä arvioidessaan uusia rajatarkastusohjelmia


---

# Syväsukellus Bitcoin-kehityksen filosofiaan



Bitcoin-kehitysfilosofia on kurssi Bitcoin-kehittäjille, jotka jo ymmärtävät Proof-of-Work:n, lohkojen rakentamisen ja transaktioiden elinkaaren kaltaisten käsitteiden ja prosessien perusteet ja jotka haluavat nousta tasolleen ymmärtämällä syvällisemmin Bitcoin:n suunnittelun kompromisseja ja filosofiaa.

Sen pitäisi auttaa uusia kehittäjiä omaksumaan tärkeimmät opetukset yli kymmenen vuoden Bitcoin-kehitystyöstä ja julkisesta keskustelusta, ja samalla se tarjoaa heille hyödyllisen kontekstin uusien ideoiden (hyvien ja huonojen!) arvioimiseksi.


### Mitä odottaa?


Kuten edellä todettiin, tämä on käytännön opas Bitcoin-kehittäjille. Bitcoin on kuitenkin laaja ja monimutkainen aihe, emmekä voi mitenkään käsitellä tässä kaikkia sen näkökohtia. Tällä kurssilla toivomme, että käsittelemme tarvittavat ominaisuudet, jotta saat kehitystoimintasi käyntiin, ja että voit tutustua siihen tarkemmin omatoimisesti.


Bitcoin:n parissa työskentelee paljon ihmisiä; koska joillakin heistä on vastakkaisia mielipiteitä, täältä voit löytää resursseja, jotka ilmaisevat ristiriitaisia ajatuksia. Pyrimme kuitenkin aina pysymään faktojen alueella, jossa mielipiteillä ei ole väliä.


### Kuka tämän kirjoitti?


Tämä kurssi on mukautettu samannimisestä kirjasta, jonka pääkirjoittaja on Kalle Rosenbaum, ja Linnéa Rosenbaum osallistui siihen toisena kirjoittajana.

Kirjan tilasi ja rahoitti [Chaincode Labs] (https://learning.chaincode.com/), kehityskeskus, joka järjestää koulutusohjelmia Bitcoin-kehityksestä kiinnostuneille kehittäjille.


+++



# Johdanto

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Kurssin yleiskatsaus

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Tervetuloa kurssille PHI 301 Bitcoin kehitysfilosofiasta.


Bitcoin on enemmän kuin pelkkä kryptovaluutta, se ilmentää filosofista näkemystä hajauttamisesta, yksityisyydestä, luotettavuudesta ja kestävyydestä. Tämä kurssi on suunniteltu erityisesti Bitcoin:n tekniset perusteet jo tunteville kehittäjille, jotka haluavat nyt syventää ymmärrystään Bitcoin:n suunnittelun ja hallinnon perustana olevista periaatteista.


Tämän kurssin aikana saat selvyyttä olennaisiin arvoihin ja strategioihin, jotka ovat ohjanneet Bitcoin:n kehitystä yli kymmenen vuoden ajan. Tutustumalla näihin teemoihin syvällisesti kehität kriittisen näkökulman, jota tarvitset arvioidaksesi ja osallistuaksesi tulevaan kehitykseen luottavaisin mielin.


### Bitcoin:n keskeiset arvot


Mikä tekee Bitcoin:sta ainutlaatuisen? Tässä osiossa paljastetaan Bitcoin:n suunnittelun ytimessä olevat perusarvot. Tutustut **desentralisaatioon**, joka on kulmakivi, jolla varmistetaan, ettei mikään yksittäinen taho hallitse verkkoa; **luottamuksettomuuteen**, joka on avain kolmannen osapuolen riippuvuuden poistamiseen; **yksityisyyden suojaan**, joka on olennainen sekä yksilön vapaudelle että järjestelmän eheydelle; ja **loppuiseen Supply:ään**, joka on Bitcoin:n taloudellista identiteettiä muovaava koodattu niukkuuden tae. Näiden käsitteiden hallitseminen antaa sinulle mahdollisuuden ymmärtää täysin Bitcoin:n vahvuudet ja haavoittuvuudet.


### Bitcoin Hallinto


Bitcoin:n monimutkaisessa hallintomaailmassa liikkuminen vaatii muutakin kuin teknistä asiantuntemusta, se edellyttää Bitcoin:n ainutlaatuisen lähestymistavan ymmärtämistä konsensukseen ja päätöksentekoon. Tässä osiossa perehdytään mekanismeihin ja filosofioihin, jotka ovat kriittisten prosessien, kuten protokollapäivitysten, taustalla, vastakkainasettelun välttämättömyyteen, avoimen lähdekoodin yhteistyön vahvuuteen, skaalaamisen jatkuviin haasteisiin ja vivahteikkaisiin strategioihin, joita tarvitaan, kun asiat väistämättä menevät pieleen. Näillä tiedoilla varustautuneena olet valmis paitsi osallistumaan myös muokkaamaan Bitcoin:n tulevaisuutta tehokkaasti ja vastuullisesti.


Oletko valmis ottamaan seuraavan askeleen Bitcoin-matkallasi? Aloitetaan!


***N.B.**: Jos törmäät kurssin aikana Bitcoin:een liittyviin tuntemattomiin termeihin, katso määritelmiä [sanastosta] (https://planb.network/resources/glossary).*




# Bitcoin Keskeiset arvot

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Hajauttaminen

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Tässä analysoidaan, mitä hajauttaminen on ja miksi se on välttämätöntä Bitcoin:n toiminnalle. Erottelemme toisistaan

kaivostyöläisten hajauttaminen ja kokonaisten solmujen hajauttaminen, ja keskustella siitä, mitä ne tuovat mukanaan sensuurin vastustamiseen, joka on yksi Bitcoin:n keskeisimmistä ominaisuuksista.


Tämän jälkeen keskustelu siirtyy neutraaliuden ymmärtämiseen - eli käyttäjien, louhijoiden ja kehittäjien lupavapauteen - joka on kaikkien hajautettujen järjestelmien välttämätön ominaisuus. Lopuksi käsittelemme sitä, miten Hard:n kaltaista hajautettua järjestelmää voi olla vaikea ymmärtää, ja esittelemme joitakin mentaalimalleja, jotka voivat auttaa sinua ymmärtämään sen.


Järjestelmää, jossa ei ole keskitettyä ohjauspistettä, kutsutaan *hajautetuksi*. Bitcoin on suunniteltu välttämään keskitettyä valvontapistettä, tai tarkemmin sanottuna *sensuurin keskitettyä pistettä*.


Hajauttaminen on keino saavuttaa *sensuurin vastustaminen*.


Bitcoin:n hajauttamiseen liittyy kaksi tärkeää näkökohtaa: Miner:n hajauttaminen ja Full node:n hajauttaminen.


Miner:n hajauttamisella tarkoitetaan sitä, että mikään keskusyksikkö ei suorita eikä koordinoi transaktioiden käsittelyä. Full node hajauttamisella tarkoitetaan sitä, että lohkojen eli louhijoiden tuottamien tietojen validointi tehdään verkon reunalla, viime kädessä sen käyttäjien toimesta, eikä muutamien luotettavien viranomaisten toimesta.


![](assets/decentralization-banner.webp)


### Miner hajauttaminen



Digitaalisia valuuttoja oli yritetty luoda jo ennen Bitcoin:ää, mutta useimmat niistä epäonnistuivat hallinnon hajauttamisen ja sensuurin vastustamisen puutteeseen.


Miner:n hajauttaminen Bitcoin:ssä tarkoittaa sitä, että *tapahtumien tilaamista* ei suorita mikään yksittäinen taho tai kiinteä joukko tahoja. Sen suorittavat kollektiivisesti kaikki toimijat, jotka haluavat osallistua siihen; tämä louhijoiden kollektiivi on dynaaminen joukko käyttäjiä. Kuka tahansa voi liittyä tai poistua halutessaan. Tämä ominaisuus tekee Bitcoin:stä sensuurille vastustuskykyisen.


Jos Bitcoin olisi keskitetty, se olisi altis niille, jotka haluaisivat sensuroida sitä, kuten hallituksille. Se kokisi saman kohtalon kuin aiemmat yritykset luoda digitaalista rahaa. [Paperin] (https://www.blockstream.com/sidechains.pdf) "Enabling Blockchain Innovations with Pegged Sidechains" johdannossa kirjoittajat selittävät, miten digitaalisen rahan varhaisversiot eivät olleet varustettuja vastakkainasetteluympäristöön (ks. myös seuraavassa osassa oleva luku Adversarial Thinking).


David Chaum esitteli digitaalisen käteisrahan tutkimuskohteena vuonna 1983 tilanteessa, jossa on keskuspalvelin, johon luotetaan Double-spending:n estämiseksi. Vähentääkseen yksilöiden yksityisyysriskiä, joka aiheutuu tästä luotetusta keskushallinnosta, ja varmistaakseen vaihdettavuuden Chaum otti käyttöön sokean allekirjoituksen, jonka avulla hän tarjosi kryptografisen keinon estää keskuspalvelimen allekirjoitusten (jotka edustavat kolikoita) yhdistäminen ja sallii keskuspalvelimen silti estää kaksinkertaisen rahan käytön.

Keskuspalvelinta koskevasta vaatimuksesta tuli digitaalisen käteisen Akilleen kantapää[Gri99]. Vaikka tätä yksittäistä vikapistettä on mahdollista lieventää korvaamalla keskuspalvelimen allekirjoitus useiden allekirjoittajien kynnysarvoisella allekirjoituksella, tarkastettavuuden kannalta on tärkeää, että allekirjoittajat ovat erillisiä ja tunnistettavissa. Tämä jättää järjestelmän silti alttiiksi epäonnistumiselle, koska jokainen allekirjoittaja voi epäonnistua tai hänet voidaan saada epäonnistumaan yksi kerrallaan.


Kävi selväksi, että keskitetyn palvelimen käyttäminen tapahtumien tilaamiseen ei ollut toimiva vaihtoehto sensuurin suuren riskin vuoksi. Vaikka keskuspalvelin korvattaisiinkin n palvelimen muodostamalla liitto, jossa on kiinteä joukko n palvelinta, joista vähintään m:n on hyväksyttävä tilaus, vaikeuksia olisi silti. Ongelma muuttuisi siten, että käyttäjien olisi sovittava tästä n palvelimen joukosta sekä siitä, miten haitalliset palvelimet korvataan hyvillä palvelimilla ilman, että turvaudutaan keskusviranomaiseen.


Mietitäänpä, mitä voisi tapahtua, jos Bitcoin olisi sensuroitavissa. Sensori voisi painostaa käyttäjiä tunnistamaan itsensä, ilmoittamaan, mistä heidän rahansa ovat peräisin tai mitä he ostavat niillä, ennen kuin heidän liiketoimiensa sallitaan siirtyä Blockchain:ään.


Lisäksi sensuurin vastustuksen puute antaisi sensuurille mahdollisuuden pakottaa käyttäjät hyväksymään järjestelmän uudet säännöt. He voisivat esimerkiksi määrätä muutoksen, joka antaisi heille mahdollisuuden paisuttaa Supply:n rahamäärää ja siten rikastua. Tällaisessa tapauksessa lohkoja tarkistavalla käyttäjällä olisi kolme vaihtoehtoa käsitellä uusia sääntöjä:



- Hyväksy: Hyväksyy muutokset ja sisällyttää ne Full node:eensa.
- Hylkää: Kieltäydy hyväksymästä muutoksia; tällöin käyttäjälle jää järjestelmä, joka ei enää käsittele transaktioita, koska käyttäjän Full node pitää sensorin estoja nyt pätemättöminä.
- Siirto: Nimetään uusi keskusvalvontakeskus; kaikkien käyttäjien on selvitettävä, miten koordinoidaan ja sovittava sitten uudesta keskusvalvontakeskuksesta.


Jos he onnistuvat, samat ongelmat tulevat todennäköisesti esiin uudelleen jossain vaiheessa tulevaisuudessa, kun otetaan huomioon, että järjestelmä on edelleen yhtä sensuroitavissa kuin ennenkin.


Mikään näistä vaihtoehdoista ei hyödytä käyttäjää.


Sensuurin vastustaminen hajauttamisen avulla erottaa Bitcoin:n muista rahajärjestelmistä, mutta se ei ole helppoa toteuttaa *Double-spending-ongelman* vuoksi. Tämä on ongelma, joka liittyy sen varmistamiseen, ettei kukaan voi käyttää samaa kolikkoa kahteen kertaan, ongelma, jota monet pitivät mahdottomana ratkaista hajautetusti. Satoshi Nakamoto kirjoittaa [Bitcoin whitepaperissaan] (https://planb.network/Bitcoin.pdf) siitä, miten Double-spending-ongelma ratkaistaan:


> Tässä asiakirjassa ehdotamme ratkaisua Double-spending-ongelmaan käyttämällä Timestamp-palvelinta, joka on hajautettu vertaisverkkopalvelin generate-laskentatodisteena tapahtumien kronologisesta järjestyksestä.


Tässä hän käyttää omituiselta kuulostavaa ilmaisua "peer-to-peer distributed Timestamp server". Avainsana tässä on *hajautettu*, mikä tässä yhteydessä tarkoittaa, että keskusvalvontapistettä ei ole. Nakamoto jatkaa sitten selittämällä, miten Proof-of-Work on ratkaisu.

Kukaan ei kuitenkaan selitä sitä paremmin kuin

[Gregory Maxwell Redditissä](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), jossa hän vastaa henkilölle, joka ehdottaa kaivostyöläisten Hash-tehon rajoittamista mahdollisten 51 prosentin hyökkäysten välttämiseksi:


> Bitcoin:n kaltaisessa hajautetussa järjestelmässä käytetään julkisia vaaleja. Hajautetussa järjestelmässä ei kuitenkaan voi äänestää vain "ihmisiä", koska se edellyttäisi, että keskitetty taho antaisi ihmisille luvan äänestää. Sen sijaan Bitcoin:ssä käytetään laskentatehon äänestystä, koska laskentateho on mahdollista todentaa ilman keskitettyä apua
kolmas osapuoli.


Postauksessa selitetään, miten hajautettu Bitcoin-verkko voi päästä sopimukseen transaktioiden tilaamisesta Proof-of-Work:n avulla.


Sitten hän toteaa lopuksi, että 51 prosentin hyökkäys ei ole erityisen huolestuttavaa verrattuna siihen, että ihmiset eivät välitä tai ymmärrä Bitcoin:n hajautusominaisuuksia:


> Bitcoin:n kannalta paljon suurempi riski on se, että sitä käyttävä yleisö ei ymmärrä, ei välitä eikä suojele niitä hajautettuja ominaisuuksia, jotka tekevät siitä arvokkaamman kuin keskitetyistä vaihtoehdoista alun perin.

Johtopäätös on tärkeä. Jos ihmiset eivät suojele Bitcoin:n hajautusta, joka on sen sensuurin vastustamisen korvike, Bitcoin saattaa joutua keskittämisvaltojen uhriksi, kunnes se on niin keskitetty, että sensuurista tulee asia. Silloin suurin osa, ellei jopa kaikki, sen arvolupauksesta on mennyttä. Tästä pääsemmekin seuraavaan Full node:n hajauttamista käsittelevään osioon.


### Full node hajauttaminen



Edellä olevissa kappaleissa olemme puhuneet lähinnä Miner:n hajauttamisesta ja siitä, miten kaivostoiminnan keskittäminen voi mahdollistaa sensuurin. Mutta hajauttamiseen liittyy myös toinenkin näkökohta, nimittäin *Full node:n hajauttaminen*.


Full node:n hajauttamisen merkitys liittyy luottamuksen puutteeseen. Oletetaan, että käyttäjä lopettaa oman Full node:nsä käytön esimerkiksi käyttökustannusten kohtuuttoman nousun vuoksi. Tällöin hänen on oltava vuorovaikutuksessa Full node-verkon kanssa jollakin muulla tavalla, mahdollisesti käyttämällä verkkolompakoita tai kevyitä lompakoita, mikä edellyttää tiettyä luottamusta näiden palvelujen tarjoajiin.


Käyttäjä siirtyy verkon konsensussääntöjen suorasta noudattamisesta luottamaan siihen, että joku muu noudattaa niitä. Oletetaan nyt, että useimmat käyttäjät siirtävät konsensussääntöjen noudattamisen valvonnan luotettavalle taholle. Tällöin verkko voi nopeasti ajautua keskittämiseen, ja verkoston sääntöjä voivat muuttaa salaliittoutuneet pahansuovat toimijat.


Vuonna [a

Bitcoin Magazine -artikkelissa](https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446) Aaron van Wirdum haastattelee Bitcoin-kehittäjiä heidän näkemyksistään hajauttamisesta ja Bitcoin:n maksimilohkokoon kasvattamiseen liittyvistä riskeistä. Tämä keskustelu oli Hot:n aiheena vuosien 2014-2017 aikana, jolloin monet kiistelivät lohkokokorajan kasvattamisesta, jotta transaktioiden läpimenoa voitaisiin lisätä.


Lohkokoon kasvattamista vastaan puhuu vahvasti se, että se lisää todentamiskustannuksia Jos todentamiskustannukset nousevat, se saa jotkut käyttäjät lopettamaan täydet solmut. Tämä puolestaan johtaa siihen, että yhä useammat ihmiset eivät pysty käyttämään järjestelmää Trustless:n tavalla.


Artikkelissa siteerataan Pieter Wuillea, joka selittää Full node:n keskittämisen riskejä:


> Jos monet yritykset käyttävät Full node:tä, ne on saatava vakuuttuneiksi siitä, että ne kaikki ottavat käyttöön erilaiset säännöt. Toisin sanoen: lohkojen validoinnin hajauttaminen antaa konsensussäännöille niiden painoarvon.
> Mutta jos Full node:n määrä putoaisi hyvin pieneksi esimerkiksi siksi, että kaikki käyttävät samoja verkkolompakoita, pörssejä ja SPV- tai mobiililompakoita, sääntelystä voisi tulla todellisuutta. Ja jos viranomaiset voivat säännellä konsensussääntöjä, se tarkoittaa, että he voivat muuttaa kaikkea, mikä tekee Bitcoin:sta Bitcoin:n. Jopa 21 miljoonan Bitcoin:n rajan.

No niin. Bitcoin-käyttäjien pitäisi käyttää omia täydellisiä solmujaan, jotta sääntelyviranomaiset ja suuret yritykset eivät yrittäisi muuttaa konsensussääntöjä.


### Neutraalius



Bitcoin on neutraali, tai luvaton, kuten ihmiset haluavat sitä kutsua. Tämä tarkoittaa, että Bitcoin ei välitä siitä, kuka olet tai mihin käytät sitä.


Bitcoin on neutraali, mikä on hyvä asia ja ainoa tapa, jolla se voi toimia. Jos se olisi jonkin organisaation hallinnassa, se olisi vain yksi virtuaalinen objektityyppi, ja se ei kiinnostaisi minua lainkaan


Kunhan noudatat sääntöjä, voit käyttää sitä vapaasti ja kyselemättä keneltäkään lupaa. Tämä sisältää *Mining:n*, *transaktiot* ja *protokollien ja palveluiden rakentamisen* Bitcoin:n päälle:



- Jos *Mining* olisi luvanvarainen prosessi, tarvitsisimme keskusviranomaisen valitsemaan, kuka saa louhia. Tämä johtaisi todennäköisesti siihen, että kaivostyöntekijät joutuisivat allekirjoittamaan laillisia sopimuksia, joissa he suostuisivat siihen, että

sensuroida liiketoimia keskusviranomaisen mielijohteiden mukaan, mikä on Mining:n tarkoituksen vastaista.



- Jos Bitcoin:ssä *transaktioita tekevien* ihmisten pitäisi antaa henkilökohtaisia tietoja, ilmoittaa, mitä varten he tekevät transaktioita, tai muulla tavoin todistaa, että he ovat transaktioiden arvoisia, tarvitsisimme myös keskusviranomaisen, joka hyväksyisi käyttäjät tai transaktiot. Tämäkin johtaisi sensuuriin ja poissulkemiseen.



- Jos kehittäjien olisi pyydettävä lupaa *rakentaa pöytäkirjoja* Bitcoin:n päälle, vain keskitetyn kehittäjien lupakomitean sallimat pöytäkirjat saataisiin kehitettyä. Tämä sulkisi hallituksen väliintulon vuoksi väistämättä pois kaikki yksityisyyttä suojaavat protokollat ja kaikki yritykset parantaa hajautusta.


Kaikilla tasoilla rajoitusten asettaminen sille, kuka saa käyttää Bitcoin:a mihin, vahingoittaa Bitcoin:a siinä määrin, että se ei enää vastaa arvolupaustaan.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518 [vastaa kysymykseen Stack Exchange:sta] siitä, miten Blockchain liittyy tavallisiin tietokantoihin. Hän selittää, miten luvattomuus voidaan saavuttaa käyttämällä Proof-of-Work:ää yhdessä taloudellisten kannustimien kanssa.


Hän toteaa lopuksi:


> Käyttämällä Trustless konsensusalgoritmeja kuten PoW lisää jotain, mitä mikään muu rakenne ei anna sinulle (luvaton osallistuminen, mikä tarkoittaa, että ei ole olemassa tiettyä osallistujaryhmää, joka voi sensuroida muutoksesi), Käyttämällä Trustless konsensusalgoritmeja kuten PoW lisää jotakin, mutta sillä on korkeat kustannukset, ja sen taloudelliset olettamukset tekevät siitä hyödyllisen vain järjestelmille, jotka määrittelevät oman kryptovaluutan.
> Maailmassa on luultavasti ainoa paikka yhdelle tai muutamalle todella käytetylle tällaiselle.

Hän selittää, että lupavapauden saavuttamiseksi järjestelmä tarvitsee todennäköisesti oman valuutan, mikä "rajoittaa käyttötapaukset käytännössä vain kryptovaluuttoihin". Tämä johtuu siitä, että lupavapaa osallistuminen eli Mining edellyttää taloudellisia kannustimia, jotka on rakennettu itse järjestelmään.


### Hajauttamisen ymmärtäminen



Bitcoin:n kiehtova piirre on se, miten Hard:n on ymmärrettävä, ettei kukaan hallitse sitä. Bitcoin:ssä ei ole komiteoita tai johtajia. Gregory Maxwell, jälleen [Bitcoin:n subredditissä] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), vertaa tätä englannin kieleen kiehtovalla tavalla:


> Monilla ihmisillä on Hard aikaa ymmärtää itsenäisiä järjestelmiä, heidän elämässään on monia asioita, kuten englannin kieli, mutta ihmiset pitävät niitä itsestäänselvyyksinä eivätkä edes ajattele niitä järjestelminä. He ovat juuttuneet keskitettyyn ajattelutapaan, jossa kaikella, mitä he ajattelevat "asiaksi", on auktoriteetti, joka hallitsee sitä.
>

> Bitcoin ei keskity mihinkään. Useat Bitcoin:n käyttöön ottaneet ihmiset ovat omasta vapaasta tahdostaan päättäneet edistää sitä, ja se, miten he sen tekevät, on heidän oma asiansa. Auktoriteettikiinnittyneet ihmiset saattavat nähdä nämä toimet ja uskoa, että ne ovat Bitcoin:n auktoriteetin toimintaa, mutta sellaista auktoriteettia ei ole olemassa.


Bitcoin:n tapa toimia hajautetusti muistuttaa poikkeuksellista kollektiivista älykkyyttä, jota esiintyy monien luonnon lajien keskuudessa. Tietojenkäsittelytieteilijä Radhika Nagpal puhuu [Ted-puheessa] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) kalaparvien kollektiivisesta käyttäytymisestä ja siitä, miten tutkijat yrittävät jäljitellä sitä robottien avulla.


> Toiseksi, ja se, mikä on minusta edelleen kaikkein ihmeellisintä, on se, että tiedämme, ettei tätä kalaparvea valvo mikään johtaja. Sen sijaan tämä uskomaton kollektiivinen käyttäytyminen syntyy puhtaasti kalojen keskinäisestä vuorovaikutuksesta.
> Jotenkin naapurikalojen välillä on vuorovaikutussuhteita tai toimintasääntöjä, jotka saavat kaiken toimimaan.

Hän huomauttaa, että monet järjestelmät, niin luonnolliset kuin keinotekoisetkin, voivat toimia ja toimivat ilman johtajia, ja ne ovat voimakkaita ja kestäviä. Kukin yksilö on vuorovaikutuksessa vain lähiympäristönsä kanssa, mutta yhdessä ne muodostavat jotain valtavaa.


![](assets/fishschool.webp)

*Kalakannoilla ei ole johtajia*


Oli Bitcoin:stä mitä mieltä tahansa, sen hajautettu luonne vaikeuttaa sen hallintaa. Bitcoin on olemassa, eikä sille voi tehdä mitään. Sitä pitää tutkia, ei keskustella siitä.


### Johtopäätös hajauttamisesta


Erotamme Full node:n hajauttamisen Mining:n hajauttamisesta. Mining:n hajauttaminen on keino saavuttaa sensuurin vastustaminen, kun taas Full node:n hajauttaminen pitää verkon konsensussäännöt Hard:n muuttumattomina ilman laajaa tukea käyttäjien keskuudessa.


Bitcoin:n hajautettu luonne mahdollistaa neutraaliuden kehittäjiä, käyttäjiä ja louhijoita kohtaan. Kuka tahansa voi vapaasti osallistua kyselemättä lupaa.


Hajautettuja järjestelmiä voi olla vaikea ymmärtää, mutta on olemassa mentaalisia malleja, jotka voivat auttaa, esimerkiksi englannin kieli tai kalakoulut.


## Luottamuksettomuus

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Tässä luvussa analysoidaan epäluotettavuuden käsitettä, mitä se tarkoittaa tietotekniikan näkökulmasta ja miksi Bitcoin:n on oltava Trustless säilyttääkseen arvolupauksensa.

Sitten puhumme siitä, mitä tarkoittaa Bitcoin:n käyttö Trustless:n tavoin ja millaisia takuita Full node voi antaa ja millaisia ei voi antaa.

Viimeisessä jaksossa tarkastelemme Bitcoin:n ja todellisten ohjelmistojen tai käyttäjien välistä vuorovaikutusta todellisessa maailmassa ja tarvetta tehdä kompromisseja mukavuuden ja epäluotettavuuden välillä, jotta saisimme ylipäätään mitään aikaan.


Ihmiset sanovat usein, että "Bitcoin on loistava, koska se on Trustless".


Mitä he tarkoittavat Trustless:llä? Pieter Wuille selittää tämän yleisesti käytetyn termin [Stack Exchange](https://Bitcoin.stackexchange.com/a/45674/69518):


> Trustless:ssa tarkoitettu luottamus on abstrakti tekninen termi. Hajautettua järjestelmää kutsutaan Trustless:ksi, kun se ei tarvitse luotettavia osapuolia toimiakseen oikein.

Lyhyesti sanalla *Trustless* viitataan Bitcoin-protokollan ominaisuuteen, jonka mukaan se voi loogisesti toimia ilman "luotettavia osapuolia". Tämä on eri asia kuin luottamus, joka sinun on väistämättä luotettava käyttämääsi ohjelmistoon tai laitteistoon. Luottamuksen jälkimmäisestä näkökohdasta puhutaan lisää myöhemmin tässä luvussa.


Keskitetyissä järjestelmissä luotamme keskitetyn toimijan maineeseen varmistaaksemme, että se huolehtii turvallisuudesta tai vetäytyy takaisin ongelmien ilmetessä, sekä oikeusjärjestelmään, joka rankaisee mahdollisista rikkomuksista. Nämä luottamusvaatimukset ovat ongelmallisia pseudonyymisissä hajautetuissa järjestelmissä - ei ole mitään mahdollisuutta turvautua oikeussuojakeinoihin, joten luottamusta ei todellakaan voi olla. Satoshi Nakamoto kuvaa tätä ongelmaa [Bitcoin whitepaperin] (https://Bitcoin.org/Bitcoin.pdf) johdannossa:


> Internetissä tapahtuva kaupankäynti on lähes yksinomaan riippuvainen rahoituslaitoksista, jotka toimivat luotettavina kolmansina osapuolina sähköisten maksujen käsittelyssä.
> Vaikka järjestelmä toimii riittävän hyvin useimmissa liiketoimissa, se kärsii silti luottamukseen perustuvan mallin luontaisista heikkouksista.  Täysin peruuttamattomat transaktiot eivät oikeastaan ole mahdollisia, koska rahoituslaitokset eivät voi välttää riitojen välittämistä. Sovittelukustannukset lisäävät transaktiokustannuksia, mikä rajoittaa transaktioiden käytännön vähimmäiskokoa ja poistaa mahdollisuuden pieniin satunnaisiin transaktioihin, ja laajempana kustannuksena on se, että menetetään mahdollisuus suorittaa peruuttamattomia maksuja peruuttamattomista palveluista.
> Luottamuksen tarve leviää, kun on olemassa peruuttamismahdollisuus. Kauppiaiden on oltava varovaisia asiakkaitaan kohtaan ja pyydettävä heiltä enemmän tietoja kuin he muuten tarvitsisivat.  Tietty prosenttiosuus petoksista hyväksytään väistämättömänä. Nämä kustannukset ja maksamiseen liittyvät epävarmuustekijät voidaan välttää henkilökohtaisesti käyttämällä fyysistä valuuttaa, mutta ei ole olemassa mitään mekanismia, jolla maksut voitaisiin suorittaa viestintäkanavan kautta ilman luotettavaa osapuolta

Vaikuttaa siltä, että meillä ei voi olla luottamukseen perustuvaa hajautettua järjestelmää, ja siksi luottamuksen puute on tärkeää Bitcoin:ssä.


Jos haluat käyttää Bitcoin:tä Trustless:n tavoin, sinun on käytettävä täysin validoivaa Bitcoin-solmua. Vain siten voit varmistaa, että muilta saamasi lohkot noudattavat konsensussääntöjä; esimerkiksi että kolikoiden liikkeeseenlaskuaikataulua noudatetaan ja että Blockchain:ssa ei tapahdu kaksinkertaisia kuluja. Jos et käytä Full node:ää, ulkoistat Bitcoin-lohkojen varmentamisen jollekin toiselle ja luotat siihen, että tämä kertoo sinulle totuuden, mikä tarkoittaa, ettet käytä Bitcoin:tä luotettavasti.


David Harding on kirjoittanut [artikkelin Bitcoin.org-sivustolle](https://Bitcoin.org/en/Bitcoin-core/features/validation), jossa hän selittää, miten Full node:n käyttäminen - tai Bitcoin:n käyttäminen ilman luottamusta - todella auttaa sinua:


> Bitcoin-valuutta toimii vain silloin, kun ihmiset hyväksyvät bitcoineja Exchange:ssä muita arvokkaita asioita vastaan. Tämä tarkoittaa, että ihmiset, jotka hyväksyvät bitcoineja, antavat sille arvon ja päättävät, miten Bitcoin:n pitäisi toimia.
>

> Kun hyväksyt bitcoineja, sinulla on valtuudet valvoa Bitcoin:n sääntöjä, kuten estää kenen tahansa henkilön bitcoinien takavarikointi ilman pääsyä kyseisen henkilön yksityisiin avaimiin.
>

> Valitettavasti monet käyttäjät ulkoistavat täytäntöönpanovaltansa. Tämä jättää Bitcoin:n hajautuksen heikentyneeseen tilaan, jossa kourallinen kaivostyöläisiä voi yhdessä kourallisen pankkien ja ilmaispalvelujen kanssa muuttaa Bitcoin:n sääntöjä kaikkien niiden käyttäjien osalta, jotka eivät ole tarkistaneet valtaa, mutta jotka ovat ulkoistaneet sen.
>

> Toisin kuin muut lompakot, Bitcoin Core noudattaa sääntöjä - jos kaivostyöläiset ja pankit muuttavat sääntöjä niiden käyttäjien osalta, jotka eivät ole vahvistavia käyttäjiä, nämä käyttäjät eivät pysty maksamaan täyden validoinnin Bitcoin Core -käyttäjille, kuten sinulle.


Hän sanoo, että Full node:n suorittaminen auttaa sinua tarkistamaan kaikki Blockchain:n osatekijät luottamatta kehenkään muuhun, jotta voit varmistaa, että muilta saamasi kolikot ovat aitoja. Tämä on hienoa, mutta on yksi tärkeä asia, jossa Full node ei voi auttaa: se ei voi estää ketjun uudelleenkirjoittamisen kautta tapahtuvaa kaksinkertaista kuluttamista:


> Huomaa, että vaikka kaikki ohjelmat - myös Bitcoin Core - ovat alttiita ketjun uudelleenkirjoittamiselle, Bitcoin tarjoaa puolustusmekanismin: mitä enemmän vahvistuksia transaktioillasi on, sitä turvallisempi olet. Tätä parempaa hajautettua puolustusta ei tunneta.

Vaikka ohjelmistosi olisi kuinka kehittynyt tahansa, sinun on silti luotettava siihen, että kolikkojasi sisältäviä lohkoja ei kirjoiteta uudelleen. Kuten Harding huomautti, voit kuitenkin odottaa useita vahvistuksia, minkä jälkeen pidät ketjun uudelleenkirjoittamisen todennäköisyyttä riittävän pienenä, jotta se on hyväksyttävää.


Kannustimet Bitcoin:n käyttämiseksi Trustless:n tavalla vastaavat järjestelmän tarvetta Full node:n hajauttamiseen. Mitä enemmän ihmisiä käyttää omia täysiä solmujaan, sitä enemmän Full node hajautetaan ja sitä vahvempi Bitcoin on protokollaan tehtäviä ilkivaltaisia muutoksia vastaan. Mutta valitettavasti, kuten Full node:n hajauttamista käsittelevässä osassa selitettiin, käyttäjät valitsevat usein luotettavat palvelut, mikä on seurausta väistämättömästä kompromissista epäluotettavuuden ja mukavuuden välillä.


Bitcoin:n luotettavuus on ehdottoman tärkeää järjestelmän kannalta. Vuonna 2018 Matt Corallo [puhui luotettavuudesta](https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) Baltic Honeybadger -konferenssissa Riiassa.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


Puheenvuoron ydin on se, että Trustless-järjestelmiä ei voi rakentaa luotettavan järjestelmän päälle, mutta luotettavia järjestelmiä - esimerkiksi Wallet-huoltajuusjärjestelmä - voi rakentaa Trustless-järjestelmän päälle.



![width=50%](assets/trust.webp)


Trustless-perus Layer mahdollistaa erilaisia kompromisseja korkeammilla tasoilla


Tämän turvallisuusmallin avulla järjestelmän suunnittelija voi valita kompromissit

jotka ovat heidän kannaltaan järkeviä, pakottamatta muita tekemään kompromisseja.


### Älä luota, tarkista



Bitcoin toimii luotettavasti, mutta sinun on silti luotettava ohjelmistoosi ja laitteistoosi jossain määrin. Tämä johtuu siitä, että ohjelmistosi tai laitteistosi ei välttämättä ole ohjelmoitu tekemään sitä, mitä laatikossa lukee. Esim:



- Suoritin saatetaan suunnitella pahantahtoisesti havaitsemaan yksityisen avaimen salausoperaatiot ja vuotamaan yksityisen avaimen tiedot.
- Käyttöjärjestelmän satunnaislukugeneraattori ei välttämättä ole niin satunnainen kuin se väittää.
- Bitcoin Core on saattanut sisällyttää koodin, joka lähettää yksityiset avaimesi jollekin pahantekijälle.


Sen lisäksi, että käytät Full node:ta, sinun on myös varmistettava, että käytät sitä, mitä aiot käyttää. Reddit-käyttäjä brianddk [kirjoitti artikkelin](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) eri luotettavuustasoista, joista voit valita, kun tarkistat ohjelmistosi. Kohdassa "Trusting the builders" hän puhuu toistettavista buildeista:


> Toistettavat asennukset ovat tapa suunnitella ohjelmisto niin, että monet yhteisön kehittäjät voivat kukin rakentaa ohjelmiston ja varmistaa, että lopullinen asennettava ohjelma on identtinen muiden kehittäjien tuottaman ohjelmiston kanssa. Bitcoin:n kaltaisessa hyvin julkisessa, monistettavassa projektissa ei tarvitse luottaa täysin yksittäiseen kehittäjään. Useat kehittäjät voivat kaikki suorittaa rakentamisen ja todistaa, että he ovat tuottaneet saman tiedoston kuin se, jonka alkuperäinen rakentaja on digitaalisesti allekirjoittanut.

Artikkelissa määritellään viisi luottamuksen tasoa: luottamus sivustoon, rakentajiin, kääntäjään, ytimeen ja laitteistoon.


Syventääkseen edelleen toistettavien rakennusten aihetta Carl Dong [piti esityksen Guixista](https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/), jossa hän selitti, miksi luottamus käyttöjärjestelmään, kirjastoihin ja kääntäjiin voi olla ongelmallista ja miten tämä voidaan korjata Guix-nimisellä järjestelmällä, jota Bitcoin Core käyttää nykyään.


> Mitä voimme siis tehdä sille, että työkaluketjussamme voi olla joukko luotettavia binääripaketteja, jotka voivat olla toistettavasti haitallisia? Meidän on oltava enemmän kuin toistettavissa. Meidän on oltava käynnistettävissä. Meillä ei voi olla niin paljon binäärityökaluja, jotka meidän on ladattava ja joihin meidän on luotettava muiden organisaatioiden valvomilta ulkoisilta palvelimilta.
>

> Meidän pitäisi tietää, miten nämä työkalut on rakennettu ja miten voimme rakentaa ne uudelleen, mieluiten paljon pienemmästä joukosta luotettavia binääripaketteja. Meidän on minimoitava luotettavien binääriohjelmien joukko mahdollisimman pieneksi, ja meillä on oltava helposti tarkastettavissa oleva polku näistä työkaluketjuista siihen, mitä käytämme Bitcoin:n rakentamiseen. Näin voimme maksimoida todentamisen ja minimoida luottamuksen.

Sitten hän selittää, miten Guixin avulla voimme luottaa vain minimaaliseen, 357 tavun binääritiedostoon, joka voidaan todentaa ja ymmärtää täysin, jos osaat tulkita ohjeita. Tämä on melko huomattavaa: tarkistetaan, että 357 tavun binääri tekee mitä sen pitäisi, sitten käytetään sitä koko build-järjestelmän rakentamiseen lähdekoodista, ja lopputuloksena on Bitcoin Core -binääri, jonka pitäisi olla tarkka kopio kenenkään muun buildista.


Monet bitcoin-asiakkaat noudattavat erästä mantraa, joka kuvaa hyvin suurta osaa edellä esitetystä:


> Älä luota, tarkista.

Tämä viittaa lauseeseen "[trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify)", jota Yhdysvaltain entinen presidentti Ronald Reagan käytti ydinaseriisunnan yhteydessä. [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) vaihtoi sen ympäri korostaakseen luottamuksen hylkäämistä ja Full node:n suorittamisen tärkeyttä.


Käyttäjät voivat itse päättää, missä määrin he haluavat tarkistaa käyttämänsä ohjelmiston ja vastaanottamansa Blockchain-tiedot. Kuten monissa muissakin Bitcoin:n asioissa, myös tässä on kyse mukavuuden ja luotettavuuden välisestä kompromissista. On lähes aina kätevämpää käyttää huollettavaa Wallet:tä kuin käyttää Bitcoin Corea omalla laitteistolla. Bitcoin-ohjelmiston kypsyessä ja käyttöliittymien parantuessa sen pitäisi kuitenkin ajan mittaan tukea paremmin käyttäjiä, jotka ovat halukkaita työskentelemään kohti luotettavuutta. Kun käyttäjät saavat ajan mittaan lisää tietoa, heidän pitäisi pystyä vähitellen poistamaan luottamus yhtälöstä.


Jotkut käyttäjät ajattelevat vastakkaisesti ja tarkistavat useimmat käyttämiensä ohjelmistojen osat. Tämän seurauksena he vähentävät luottamuksen tarpeen minimiin, sillä heidän on luotettava vain tietokonelaitteistoonsa ja käyttöjärjestelmäänsä. Näin he auttavat myös niitä, jotka eivät tarkista laitteistoaan yhtä perusteellisesti, nostamalla äänensä julkisesti esiin varoittaakseen mahdollisista ongelmista. Yksi hyvä esimerkki tästä on [vuonna 2018 sattunut tapahtuma](https://bitcoincore.org/en/2018/09/20/notice/), kun joku löysi bugin, jonka avulla louhijat saattoivat käyttää tuoton kahdesti samassa transaktiossa:


> CVE-2018-17144, jonka korjaus julkaistiin 18. syyskuuta Bitcoin Core -versioissa 0.16.3 ja 0.17.0rc4, sisältää sekä palvelunestokomponentin että kriittisen inflaatiohaavoittuvuuden. Se ilmoitettiin alun perin useille Bitcoin Corea työstäville kehittäjille sekä muita kryptovaluuttoja tukeville projekteille, kuten ABC:lle ja Unlimitedille, 17. syyskuuta vain palvelunesto-ongelmana, mutta totesimme kuitenkin nopeasti, että ongelma oli myös inflaatio-haavoittuvuus, jolla oli sama perussyy ja korjaus.

Tässä tapauksessa nimettömänä esiintynyt henkilö ilmoitti asiasta, joka osoittautui paljon pahemmaksi kuin toimittaja tajusi. Tämä korostaa sitä, että ihmiset, jotka tarkistavat koodin, raportoivat usein tietoturva-aukoista sen sijaan, että käyttäisivät niitä hyväkseen. Tästä on hyötyä niille, jotka eivät pysty itse tarkistamaan kaikkea.


Käyttäjien ei kuitenkaan pitäisi luottaa siihen, että muut pitävät heidät turvassa, vaan heidän pitäisi pikemminkin varmistaa asia itse aina ja kaikin mahdollisin tavoin; näin ihminen pysyy mahdollisimman suvereenina ja Bitcoin menestyy. Mitä useampi silmä tarkkailee ohjelmistoa, sitä epätodennäköisempää on, että haittakoodi ja tietoturva-aukot pääsevät livahtamaan läpi.


### Johtopäätös epäluotettavuudesta



Bitcoin-protokolla on Trustless-protokolla, koska sen avulla käyttäjät voivat olla vuorovaikutuksessa sen kanssa luottamatta kolmanteen osapuoleen. Käytännössä useimmat ihmiset eivät kuitenkaan pysty tarkistamaan koko ohjelmisto- ja laitteistopinoa, jolla he käyttävät Bitcoin:tä. Ammattitaitoiset henkilöt, jotka tarkistavat ohjelmistoja tai laitteistoja, pystyvät varoittamaan muita, vähemmän ammattitaitoisia henkilöitä, kun he löytävät haitallista koodia tai vikoja.


Ilman luottamuksen puutetta ei voi olla hajauttamista, koska luottamukseen liittyy väistämättä jokin keskeinen auktoriteettipiste. Trustless-järjestelmän päälle voi rakentaa luotettavan järjestelmän, mutta Trustless-järjestelmää ei voi rakentaa luotettavan järjestelmän päälle.


## Yksityisyys

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Tässä luvussa käsitellään sitä, miten voit pitää yksityiset taloudelliset tietosi omana tietonasi. Siinä selitetään, mitä yksityisyys tarkoittaa Bitcoin:n yhteydessä, miksi se on tärkeää ja mitä tarkoittaa, että Bitcoin on pseudonyymi. Siinä tarkastellaan myös sitä, miten yksityiset tiedot voivat vuotaa, sekä On-Chain että off-chain.


Sitten siinä puhutaan siitä, että bitcoinien pitäisi olla vaihdettavissa, eli vaihdettavissa muihin bitcoineihin, ja siitä, miten vaihdettavuus ja yksityisyys kulkevat käsi kädessä. Lopuksi luvussa esitellään joitakin toimenpiteitä, joilla voit parantaa omaa ja muiden yksityisyyttä.


Bitcoin voidaan kuvata pseudonyymijärjestelmäksi, jossa käyttäjillä on useita pseudonyymejä julkisten avainten muodossa. Ensisilmäyksellä tämä näyttää melko hyvältä tavalta suojata käyttäjiä tunnistamiselta, mutta todellisuudessa yksityisiä taloudellisia tietoja on todella helppo vuotaa tahattomasti.


### Mitä yksityisyys tarkoittaa?



Yksityisyys voi tarkoittaa eri asioita eri yhteyksissä. Bitcoin:ssä se tarkoittaa yleensä sitä, että käyttäjien ei tarvitse paljastaa taloudellisia tietojaan muille, elleivät he tee sitä vapaaehtoisesti.


Voit vuotaa yksityisiä tietojasi muille monin tavoin, joko tietämättäsi tai tietämättäsi. Tietoja voi vuotaa joko julkisesta Blockchain:sta tai muulla tavoin, esimerkiksi kun pahansuovat toimijat sieppaavat Internet-viestintäsi.


### Miksi yksityisyys on tärkeää?


Saattaa tuntua itsestään selvältä, miksi yksityisyys on tärkeää Bitcoin:ssa, mutta siihen liittyy joitakin näkökohtia, joita ei ehkä heti tule ajatelleeksi. [Bitcoin Talk -foorumilla] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908) Gregory Maxwell esittelee meille monia hyviä syitä, miksi yksityisyys on hänen mielestään tärkeää. Niitä ovat muun muassa vapaat markkinat, turvallisuus ja ihmisarvo:


> Taloudellinen yksityisyys on olennainen edellytys vapaiden markkinoiden tehokkaalle toiminnalle: jos johdat yritystä, et voi asettaa hintoja tehokkaasti, jos toimittajasi ja asiakkaasi näkevät kaikki liiketoimesi vastoin tahtoasi.
> Et voi kilpailla tehokkaasti, jos kilpailijasi seuraa myyntiäsi.  Yksilöllinen informaatiovoimasi häviää yksityisissä asioissasi, jos sinulla ei ole yksityisyyden suojaa tileistäsi: jos maksat vuokranantajallesi Bitcoin:ssä ilman riittävää yksityisyyden suojaa, vuokranantajasi näkee, milloin olet saanut palkankorotuksen, ja voi pyytää sinulta lisää vuokraa.
>

> Taloudellinen yksityisyys on olennaisen tärkeää henkilökohtaisen turvallisuuden kannalta: jos varkaat näkevät rahankäyttösi, tulosi ja omaisuutesi, he voivat käyttää näitä tietoja kohdehenkilöinäsi ja käyttää sinua hyväkseen. Ilman yksityisyyttä pahansuovilla tahoilla on paremmat mahdollisuudet varastaa henkilöllisyytesi, siepata suuret ostoksesi kotioveltasi tai esiintyä sinua kohtaan yrityksinä, joiden kanssa asioit... he tietävät tarkalleen, kuinka paljon he voivat yrittää huijata sinua.
>

> Taloudellinen yksityisyys on ihmisarvon kannalta olennaisen tärkeää: kukaan ei halua, että kahvilan räkänokkainen barista tai uteliaat naapurit kommentoivat hänen tulojaan tai kulutustottumuksiaan. Kukaan ei halua vauvahullujen appivanhempiensa kyselevän, miksi he ostavat ehkäisyä (tai seksileluja). Työnantajallasi ei ole mitään asiaa tietää, mihin kirkkoon lahjoitat. Vain täydellisen valistuneessa, syrjinnästä vapaassa maailmassa, jossa kenelläkään ei ole kohtuutonta valtaa toisiin nähden, voisimme säilyttää ihmisarvomme ja tehdä lailliset liiketoimemme vapaasti ilman itsesensuuria, jos meillä ei ole yksityisyyttä.

Maxwell käsittelee myös korvattavuutta, jota käsitellään myöhemmin tässä luvussa, sekä sitä, miten yksityisyys ja lainvalvonta eivät ole ristiriidassa keskenään.


### Pseudonymiteetti


Edellä mainittiin, että Bitcoin on pseudonyymi ja että pseudonyymit ovat julkisia avaimia. Tiedotusvälineissä kuulee usein, että Bitcoin on anonyymi, mikä ei pidä paikkaansa. Anonymiteetin ja pseudonymiteetin välillä on ero.


Andrew Poelstra [selittää Bitcoin Stack Exchange -postauksessa](https://Bitcoin.stackexchange.com/a/29473/69518), miltä anonymiteetti näyttäisi liiketoimissa:


> Täydellinen anonymiteetti eli se, että kun käytät rahaa, ei ole mitään jälkiä siitä, mistä raha on peräisin tai minne se on menossa, on teoreettisesti mahdollista käyttämällä kryptografista tekniikkaa, joka perustuu nollatietotodistuksiin.

Ero näyttää olevan siinä, että pseudonyymisessä rahamuodossa voi jäljittää maksuja pseudonyymien välillä, kun taas anonyymissä rahamuodossa ei voi. Koska Bitcoin:n maksut ovat jäljitettävissä salanimien välillä, kyseessä ei ole anonyymi järjestelmä.


Olemme myös sanoneet, että salanimet ovat julkisia avaimia, mutta itse asiassa kyse on julkisista avaimista johdetuista osoitteista. Miksi käytämme pseudonyymeinä osoitteita emmekä jotakin muuta, esimerkiksi joitakin kuvaavia nimiä, kuten "watchme1984"? Tämän on [selittänyt hyvin](https://Bitcoin.stackexchange.com/a/25175/69518) käyttäjä Tim S., myös Bitcoin Stack Exchange:ssä:


> Jotta Bitcoin:n idea toimisi, tarvitaan kolikoita, joita voi käyttää vain tietyn yksityisen avaimen omistaja. Tämä tarkoittaa sitä, että kaikki, mihin lähetät kolikoita, on sidottava jollakin tavalla julkiseen avaimeen.
>

> Mielivaltaisten salanimien (esim. käyttäjänimien) käyttäminen tarkoittaisi, että salanimi pitäisi jotenkin yhdistää julkiseen avaimeen, jotta julkisen ja yksityisen avaimen salaus olisi mahdollista. Tämä poistaisi mahdollisuuden luoda turvallisesti osoitteita/salanimiä offline-tilassa (esim. ennen kuin joku voisi lähettää rahaa käyttäjänimelle "tdumidu", sinun pitäisi ilmoittaa Blockchain:ssa, että "tdumidu" kuuluu julkiselle avaimelle "a1c...", ja sisällyttää siihen maksu, jotta muilla olisi syy ilmoittaa siitä), vähentäisi anonymiteettiä (koska se kannustaisi käyttämään pseudonyymejä uudestaan) ja kasvattaisi tarpeettomasti Blockchain:n kokoa. Se loisi myös vääränlaisen turvallisuuden tunteen siitä, että lähetät rahaa sille, jolle luulet olevasi (jos otan nimen "Linus Torvalds" ennen häntä, se on minun, ja ihmiset saattavat lähettää rahaa luullen maksavansa Linuxin luojalle, eivät minulle).

Käyttämällä osoitteita tai julkisia avaimia saavutamme tärkeitä tavoitteita, kuten sen, ettei salanimeä tarvitse rekisteröidä jotenkin etukäteen, että salanimen uudelleenkäyttöä kannustetaan vähemmän, että vältetään Blockchain:n paisuttaminen ja että muiden ihmisten esittäminen toisena henkilönä on vaikeampaa.


### Blockchain yksityisyys



Blockchain:n yksityisyys tarkoittaa tietoja, jotka paljastat tehdessäsi liiketoimia Blockchain:ssä. Se koskee kaikkia tapahtumia, sekä lähettämiäsi että vastaanottamiasi.


Satoshi Nakamoto pohtii On-Chain:n yksityisyyttä [Bitcoin whitepaperin] (https://Bitcoin.org/Bitcoin.pdf) kohdassa 7:


> Lisäpalomuurina jokaiselle tapahtumalle olisi käytettävä uutta avainparia, jotta niitä ei voida yhdistää yhteiseen omistajaan. Joitakin linkityksiä ei silti voida välttää usean syötteen tapahtumissa, jotka välttämättä paljastavat, että niiden syötteet olivat saman omistajan omistuksessa. Riskinä on, että jos avaimen omistaja paljastuu, linkittäminen voi paljastaa muita samalle omistajalle kuuluvia tapahtumia.

Asiakirjassa esitetään yhteenveto Blockchain yksityisyyden suojan tärkeimmistä ongelmista, nimittäin Address uudelleenkäytöstä ja Address klusteroinnista. Ensimmäinen on itsestään selvä, jälkimmäisellä tarkoitetaan kykyä päättää tietyllä varmuudella, että joukko eri osoitteita kuuluu samalle käyttäjälle.


![](assets/address-reuse-clustering.webp)


Tyypillisiä Blockchain:n yksityisyysvuotoja


Chris Belcher [kirjoitti hyvin yksityiskohtaisesti](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) erilaisista yksityisyydensuojan vuodoista, joita voi tapahtua Bitcoin Blockchain:ssa. Suosittelemme, että luet ainakin ensimmäiset alaluvut kohdasta "Blockchain:n hyökkäykset yksityisyyttä vastaan"


Lopputulos on, että Bitcoin:n yksityisyys ei ole täydellinen. Yksityinen kaupankäynti vaatii huomattavan paljon työtä. Useimmat ihmiset eivät ole valmiita menemään niin pitkälle yksityisyyden vuoksi. Yksityisyyden ja käytettävyyden välillä näyttää olevan selkeä kompromissi.


Toinen tärkeä yksityisyyden suojaan liittyvä näkökohta on se, että toimenpiteet, joihin ryhdyt oman yksityisyytesi suojaamiseksi, vaikuttavat myös muihin käyttäjiin. Jos olet huolimaton oman yksityisyytesi suhteen, muutkin ihmiset saattavat kokea yksityisyyden suojan heikentyneen. Gregory Maxwell selittää tämän hyvin selkeästi samassa Bitcoin Talk -keskustelussa [johon linkitimme edellä] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252) ja esittää lopuksi esimerkin:


> Tämä toimii myös käytännössä... Eräs mukava whitehat-hakkeri IRC:ssä leikki brainwalletin murtamista ja löysi lauseen, jossa oli ~250 BTC.  Pystyimme tunnistamaan omistajan pelkän Address:n perusteella, koska hänelle oli maksanut Bitcoin-palvelu, joka käytti osoitteita uudelleen, ja hän pystyi puhumaan hänet luovuttamaan käyttäjien yhteystiedot. Hän sai käyttäjän itse asiassa puhelimeen, ja hän oli järkyttynyt ja hämmentynyt, mutta kiitollinen siitä, ettei hän menettänyt kolikkoaan.  Siinä oli onnellinen loppu. (Tämä ei ole läheskään ainoa esimerkki siitä, mutta se on yksi hauskimmista).

Tässä tapauksessa kaikki sujui hyvin hyväntekeväisyysmielisen hakkerin ansiosta, mutta älä luota siihen ensi kerralla.


### Muu kuin Blockchain-yksityisyys


Vaikka Blockchain osoittautuukin pahamaineiseksi yksityisyysvuotojen lähteeksi, on paljon muitakin vuotoja, joissa ei käytetä Blockchain:ää, jotkut niistä ovat salakavalampia kuin toiset. Ne vaihtelevat näppäinlokituksista verkkoliikenteen analysointiin. Jos haluat tutustua joihinkin näistä menetelmistä, lue uudelleen [Chris Belcherin artikkeli] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), erityisesti kohta "Non-Blockchain attacks on privacy".


Belcher mainitsee lukuisten hyökkäysten joukossa mahdollisuuden, että joku, esimerkiksi Internet-palveluntarjoajasi, voi urkkia internet-yhteyttäsi:


> Jos vastustaja näkee solmusta lähtevän transaktion tai lohkon, jota ei ole aiemmin tullut solmuun, se voi tietää lähes varmasti, että transaktio on sinun tekemäsi tai lohko on sinun louhimasi. Koska kyse on internet-yhteyksistä, vastustaja pystyy yhdistämään IP Address:n ja löydetyn Bitcoin:n tiedot.

Ilmeisimpiä yksityisyyden suojan vuotoja ovat kuitenkin vaihdot. Pörssit ja niihin liittyvät yritykset joutuvat usein keräämään käyttäjiensä henkilötietoja ja perustamaan suuria tietokantoja siitä, ketkä käyttäjät omistavat mitäkin bitcoineja, koska niiden toiminta-alueilla on voimassa lakeja, joihin yleensä viitataan nimillä KYC (Know Your Customer) ja AML (Anti-Money Laundering). Nämä tietokannat ovat loistavia hunajaputkia pahoille hallituksille ja rikollisille, jotka etsivät aina uusia uhreja. Tällaisille tiedoille on olemassa todelliset markkinat, joilla hakkerit

myydä tietoja eniten tarjoavalle.


Kaiken kukkuraksi näitä tietokantoja hallinnoivilla yrityksillä on usein vain vähän kokemusta taloustietojen suojaamisesta, ja monet niistä ovat itse asiassa nuoria start-up-yrityksiä, ja tiedämme varmasti, että useita vuotoja on jo tapahtunut. Muutamia esimerkkejä ovat

[intialainen MobiQwik](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) ja [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Tietojen suojaaminen näin monenlaisilta hyökkäyksiltä on Hard, ja on todennäköistä, että et pysty siihen täysin. Sinun on valittava sinulle parhaiten sopiva kompromissi mukavuuden ja yksityisyyden välillä.


### Sienestettävyys


Rahojen osalta korvattavuus tarkoittaa, että yksi kolikko on vaihdettavissa mihin tahansa saman valuutan kolikkoon. Tämä hassu

sanaa käsiteltiin lyhyesti aiemmin tässä luvussa.


Kyseisessä artikkelissa Gregory Maxwell [totesi](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Taloudellinen yksityisyys on Bitcoin:ssä olennainen osa korvattavuutta: jos kolikon voi erottaa toisistaan, sen korvattavuus on heikko. Jos fungibiliteettimme on käytännössä liian heikko, emme voi olla hajautettuja: jos joku tärkeä taho ilmoittaa luettelon varastetuista kolikoista, joista johdettuja kolikoita ei hyväksytä, sinun on tarkistettava hyväksymäsi kolikot huolellisesti luettelosta ja palautettava ne, jotka eivät ole hyväksyttyjä.  Kaikki joutuvat tarkistamaan eri viranomaisten laatimia mustia listoja, koska siinä maailmassa emme kaikki haluaisi jäädä kiinni huonoihin kolikoihin. Tämä lisää kitkaa ja transaktiokustannuksia ja vähentää Bitcoin:n arvoa rahana.

Tässä hän puhuu vaaroista, jotka johtuvat vaihdettavuuden puutteesta. Oletetaan, että sinulla on UTXO. Tuon UTXO:n historia voidaan yleensä jäljittää useiden hyppyjen päähän, ja se ulottuu moniin aiempiin tuotoksiin. Jos jokin näistä ulostuloista on ollut osallisena laittomassa, ei-toivotussa tai epäilyttävässä toiminnassa, jotkut kolikkosi mahdolliset vastaanottajat saattavat hylätä sen. Jos uskot, että maksunsaajat tarkistavat kolikkosi jonkin keskitetyn valkoisen tai mustan listan palvelun avulla, voit varmuuden vuoksi alkaa tarkistaa myös vastaanottamasi kolikot. Tuloksena on, että huono fungibiliteetti vahvistaa vielä huonompaa fungibiliteettiä.


Adam Back ja Matt Corallo [pitivät esityksen siedettävyydestä] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) Scaling Bitcoin -tapahtumassa Milanossa vuonna 2016. He ajattelivat samoilla linjoilla:


> Bitcoin:n toiminnan edellytyksenä on, että se on vaihdettavissa. Jos saat kolikoita etkä voi käyttää niitä, alat epäillä, voitko käyttää niitä. Jos saatte kolikoista epäilyksiä, ihmiset menevät taint-palveluihin ja tarkistavat, ovatko nämä kolikot siunattuja, ja sitten ihmiset kieltäytyvät kaupankäynnistä. Tämä tarkoittaa, että Bitcoin siirtyy hajautetusta luvattomasta järjestelmästä keskitettyyn luvalliseen järjestelmään, jossa sinulla on "velkakirja" mustan listan tarjoajilta.

Näyttää siltä, että yksityisyys ja vaihdettavuus kulkevat käsi kädessä. Sienestettävyys heikkenee, jos yksityisyyden suoja on heikko, sillä esimerkiksi ei-toivottujen ihmisten kolikot voivat joutua mustalle listalle. Samoin yksityisyys heikkenee, jos siedettävyys on heikko: jos on olemassa musta lista, sinun on kysyttävä mustan listan tarjoajilta, mitä kolikoita haluat hyväksyä, jolloin saatat mahdollisesti paljastaa IP-osoitteesi Address, sähköpostiosoitteesi Address ja muita arkaluonteisia tietoja. Nämä kaksi ominaisuutta ovat niin toisiinsa kietoutuneita, että on Hard puhua kummastakaan niistä erikseen.


### Yksityisyyden suojaa koskevat toimenpiteet



Useita tekniikoita on kehitetty auttamaan ihmisiä suojautumaan yksityisyyden suojan vuotamiselta. Ilmeisimpiä niistä on, kuten Nakamoto aiemmin totesi, yksilöllisten ja ainutlaatuisten

osoitteita jokaista tapahtumaa varten, mutta on olemassa useita muitakin. Emme aio opettaa sinulle, miten sinusta tulee yksityisyyden ninja. Bitcoin Q+A:ssa on kuitenkin [nopea yhteenveto yksityisyyttä parantavista tekniikoista](https://bitcoiner.guide/privacytips/), jotka on järjestetty hieman sen mukaan, miten Hard ne on toteutettava. Kun luet sen, huomaat, että Bitcoin:n yksityisyyden suoja liittyy usein Bitcoin:n ulkopuolisiin asioihin. Sinun ei esimerkiksi pitäisi kehuskella bitcoineillasi, ja sinun pitäisi käyttää Tor- ja VPN-verkkoja.


Postissa luetellaan myös joitakin toimenpiteitä, jotka liittyvät suoraan Bitcoin:een:


- Full node: Jos et käytä omaa Full node:ääsi, vuodat paljon tietoja Wallet:stäsi internetin palvelimille. Full node:n käyttäminen on hyvä ensimmäinen askel.
- Lightning Network: Bitcoin:n päälle on olemassa useita protokollia, esimerkiksi Lightning Network ja Blockstreamin Liquid Sidechain.
- CoinJoin: Tapa, jolla useat ihmiset voivat yhdistää tapahtumansa yhdeksi, mikä vaikeuttaa ketjuanalyysin tekemistä.


Breaking Bitcoin -konferenssissa pitämässään puheessa (https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) Chris Belcher antoi mielenkiintoisen käytännön esimerkin siitä, miten yksityisyyttä on parannettu:


> Ne olivat Bitcoin-kasino. Nettipelaaminen ei ole sallittua Yhdysvalloissa. Kaikkien Coinbasen asiakkaiden, jotka tallettivat suoraan Bustabitiin, tilit suljettaisiin, koska Coinbase valvoi tätä. Bustabit teki muutamia asioita. He tekivät jotain, jota kutsutaan vaihtorahojen välttämiseksi, jossa käydään läpi ja katsotaan, voidaanko rakentaa transaktio, joka ei tuota vaihtorahoja. Tämä säästää Miner-maksuja ja vaikeuttaa myös analysointia.
>

> Lisäksi he toivat joinmarketiin paljon käytetyt, uudelleen käytetyt talletusosoitteet. Tässä vaiheessa coinbase.com-asiakkaita ei koskaan kielletty. Näyttää siltä, että Coinbasen valvontapalvelu ei pystynyt tekemään analyysiä tämän jälkeen, joten näiden algoritmien rikkominen on mahdollista.

Hän mainitsi tämän esimerkin myös Bitcoin-wikin [Privacy page](https://en.Bitcoin.it/Privacy) -sivulla.


Huomaa, että parempi yksityisyys voidaan saavuttaa rakentamalla järjestelmiä Bitcoin:n päälle, kuten Lightning Network:n tapauksessa:


![image](assets/privacy.webp)


Bitcoin:n päällä olevat kerrokset voivat lisätä yksityisyyttä


Edellisessä lehdessä todettiin, että luottamuksen tarve voi kasvaa vain kerroksittain, mutta tämä ei näytä koskevan yksityisyyttä, jota voidaan parantaa tai huonontaa mielivaltaisesti kerroksittain. Miksi näin on? Minkä tahansa Layer:n, joka on Bitcoin:n päällä, kuten kerroksittaista skaalausta koskevassa kappaleessa tulevassa luvussa Skaalaus selitetään, on käytettävä On-Chain-tapahtumia satunnaisesti, muuten se ei olisi "Bitcoin:n päällä". Yksityisyyttä lisäävät kerrokset pyrkivät yleensä käyttämään perus-Layer:ta mahdollisimman vähän, jotta paljastuvan tiedon määrä olisi mahdollisimman pieni.


Edellä mainitut ovat jokseenkin teknisiä tapoja parantaa yksityisyyttäsi. Mutta on muitakin tapoja. Tämän luvun alussa sanoimme, että Bitcoin on pseudonyymijärjestelmä. Tämä tarkoittaa sitä, että Bitcoin:n käyttäjiä ei tunneta oikeilla nimillään tai muilla henkilötiedoillaan, vaan heidän julkisilla avaimillaan. Julkinen avain on käyttäjän salanimi, ja käyttäjällä voi olla useita salanimiä. Ihanteellisessa maailmassa henkilökohtainen henkilöllisyytesi on erotettu Bitcoin-pseudonyymeistäsi. Valitettavasti tässä luvussa kuvattujen yksityisyyden suojaan liittyvien ongelmien vuoksi tämä erottaminen heikkenee yleensä ajan myötä.


Henkilötietojesi paljastumisen riskejä voi vähentää antamalla niitä alun perin luovuttamatta tai antamalla niitä keskitetyille palveluille, jotka rakentavat suuria tietokantoja, jotka voivat vuotaa. Bitcoin Q+A:n artikkelissa [selitetään KYC] (https://bitcoiner.guide/nokyconly/) ja siitä johtuvat vaarat. Siinä ehdotetaan myös joitakin toimia, joilla voit parantaa tilannetta:


> Onneksi on olemassa joitakin vaihtoehtoja ostaa Bitcoin ilman KYC-lähteitä. Nämä ovat kaikki P2P (peer to peer) -vaihtoja, joissa käydään kauppaa suoraan toisen henkilön kanssa eikä keskitetyn kolmannen osapuolen kanssa. Valitettavasti jotkut myyvät Bitcoin:n lisäksi myös muita kolikoita, joten kehotamme sinua olemaan varovainen.

Artikkelissa ehdotetaan, että vältät KYC/AML-vaatimuksia sisältäviä pörssejä ja käytät sen sijaan yksityisiä tai hajautettuja pörssejä, kuten [bisq](https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Jos haluat lukea syvällisemmin vastatoimista, katso aiemmin mainittu [wikiartikkeli yksityisyydestä](https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), alkaen kohdasta "Methods for improving privacy (non-Blockchain)".


### Yksityisyyden suojaa koskevat päätelmät



Yksityisyys on erittäin tärkeää, mutta Hard:n saavuttaminen on vaikeaa. Yksityisyyden suojaa ei ole olemassa.


Saadaksesi kunnollisen yksityisyyden Bitcoin:ssa sinun on ryhdyttävä aktiivisiin toimenpiteisiin, joista osa on kalliita ja aikaa vieviä.


## Lopullinen Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Tässä luvussa tarkastellaan Bitcoin Supply-rajaa, joka on 21 miljoonaa BTC:tä, vai kuinka paljon se todellisuudessa on? Puhumme siitä, miten tätä rajaa valvotaan ja mitä voi tehdä varmistaakseen, että sitä noudatetaan. Lisäksi kurkistamme kristallipalloon ja keskustelemme dynamiikasta, joka astuu kuvaan, kun Block reward siirtyy tukipohjaisesta maksupohjaiseksi.


Bitcoin:n perusominaisuutena pidetään tunnettua 21 miljoonan BTC:n äärellistä Supply:ää. Mutta onko se todella kiveen hakattu?


Aloitetaan tarkastelemalla, mitä nykyiset konsensussäännöt sanovat Bitcoin:n Supply:stä ja kuinka suuri osa siitä on todella käyttökelpoista. Pieter Wuille kirjoitti tästä [Stack Exchange:stä](https://Bitcoin.stackexchange.com/a/38998/69518), jossa hän laski, kuinka monta bitcoinia on jäljellä, kun kaikki kolikot on louhittu:


> Jos lasket kaikki nämä luvut yhteen, saat 20999999.9769 BTC.

Tätä ylärajaa ei kuitenkaan koskaan saavuteta useista syistä, kuten kolikkopankkitransaktioiden alkuvaiheen ongelmista, kaivostyöläisistä, jotka vahingossa vaativat vähemmän kuin on sallittua, ja yksityisten avainten katoamisesta, johtuen. Wuille päättelee:


> Jäljelle jää 20999817.31308491 BTC (kun otetaan huomioon kaikki lohkoon 528333 asti)

Useita lompakoita on kuitenkin kadonnut tai varastettu, tapahtumia on lähetetty väärään Address:aan ja ihmiset ovat unohtaneet omistavansa Bitcoin:n. Näiden summa voi hyvinkin olla miljoonia. Ihmiset ovat yrittäneet laskea tiedossa olevia tappioita yhteen [täällä](https://bitcointalk.org/index.php?topic=7253.0).


Jäljelle jäävät: ??? BTC.


Voimme siis olla varmoja, että Bitcoin Supply on enintään 20999817.31308491 BTC. Kaikki kadonneet tai todistamattomasti poltetut kolikot pienentävät tätä lukua, mutta emme tiedä kuinka paljon. Mielenkiintoista on se, että sillä ei ole oikeastaan mitään väliä, tai paremminkin sillä on merkitystä positiivisella tavalla Bitcoin:n haltijoille,

[kuten Satoshi Nakamoto selitti] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647):


> Kadonneet kolikot tekevät muiden kolikoista vain hieman arvokkaampia.  Ajattele sitä lahjoituksena kaikille.

Rajallinen Supply supistuu, ja tämän pitäisi ainakin teoriassa aiheuttaa hintojen deflaatiota.


Liikkeessä olevien kolikoiden tarkkaa lukumäärää tärkeämpää on tapa, jolla Supply-rajaa valvotaan ilman keskusviranomaista. Alias chytrik ilmaisee asian hyvin [Stack Exchange](https://Bitcoin.stackexchange.com/a/106830/69518):


> Vastaus on siis se, että sinun ei tarvitse luottaa siihen, että joku ei lisää Supply:ää. Sinun on vain ajettava jokin koodi, joka todentaa, että he eivät ole lisänneet.

Vaikka jotkut täydet solmut kääntyisivät pimeälle puolelle ja päättäisivät hyväksyä lohkoja, joissa on arvokkaampia coinbase-transaktioita, kaikki loput täydet solmut yksinkertaisesti laiminlyövät ne ja jatkavat liiketoimintaa tavalliseen tapaan. Jotkin täydet solmut saattavat tahallaan tai tahattomasti käyttää pahoja ohjelmistoja, mutta kollektiivi turvaa Blockchain:n vankasti. Yhteenvetona voidaan todeta, että voit luottaa järjestelmään ilman, että sinun tarvitsee luottaa kehenkään.


### Ryhmätuki ja transaktiomaksut



Block reward koostuu lohkotuesta ja transaktiomaksuista. Block reward:n on katettava Bitcoin:n turvakustannukset. Voimme sanoa varmasti, että nykyisissä olosuhteissa, jotka koskevat lohkotukea, transaktiomaksuja, Bitcoin:n hintaa, Mempool:n kokoa, Hash:n tehoa, hajauttamisastetta jne., jokaisen pelaajan kannustimet pelata sääntöjen mukaan ovat riittävän suuret turvallisen rahajärjestelmän säilyttämiseksi.


Mitä tapahtuu, kun lohkotuki lähestyy nollaa? Yksinkertaisuuden vuoksi oletetaan, että se on nolla. Tässä vaiheessa järjestelmän turvallisuuskustannukset katetaan ainoastaan transaktiomaksuilla. Emme voi tietää, mitä tulevaisuus tuo tullessaan. Epävarmuustekijöitä on lukuisia, ja jäämme arvailujen varaan. Esimerkiksi Paul Sztorcin panos aiheeseen [Truthcoin-blogissaan](https://www.truthcoin.info/blog/security-budget/) on enimmäkseen spekulaatioita, mutta hänellä on ainakin yksi vankka pointti (huomaa, että Sztorcin mainitsema M2 on fiat-rahan Supply-mittaus):


> Vaikka nämä kaksi yhdistetään samaan "turvallisuusbudjettiin", lohkotuki ja txn-maksut ovat täysin ja täysin erilaisia. Ne eroavat toisistaan yhtä paljon kuin "VISA:n kokonaisvoitto vuonna 2017" eroaa "M2:n kokonaiskasvusta vuonna 2017".

Nykyään arvopaperin haltijat maksavat arvopapereista (rahan inflaation kautta). Huomenna on tuhlaajien vuoro jotenkin kantaa tämä taakka, kuten alla on esitetty.


![image](assets/finitesupply.webp)


Ajan myötä turvakustannusten kantaminen siirtyy haltijoilta kulujen maksajille


Kun transaktiomaksut ovat Mining:n tärkein motiivi, kannustimet muuttuvat. Jos Miner:n Mempool ei sisällä riittävästi transaktiomaksuja, Miner:lle voi olla kannattavampaa kirjoittaa Bitcoin:n historia uudelleen kuin laajentaa sitä. Bitcoin Optechissa on erityinen [tätä käyttäytymistä käsittelevä osio](https://bitcoinops.org/en/topics/fee-sniping/), nimeltään *fee sniping*, jonka on kirjoittanut David Harding:


> Palkkioiden nappaaminen on ongelma, joka voi ilmetä, kun Bitcoin:n tuki vähenee edelleen ja transaktiomaksut alkavat hallita Bitcoin:n lohkopalkkioita. Jos transaktiopalkkiot ovat kaikki, millä on merkitystä, niin Miner:llä, jolla on `x` prosenttia Hash:n määrästä, on `x` prosentin mahdollisuus saada Mining seuraavassa lohkossa, joten rehellisen Mining:n odotusarvo heille on `x` prosenttia [parhaasta feerate-joukosta transaktioita](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) heidän Mempool:ssä.
>

> Vaihtoehtoisesti Miner voisi epärehellisesti yrittää louhia uudelleen edellisen lohkon ja kokonaan uuden lohkon ketjun laajentamiseksi. Tällaista käyttäytymistä kutsutaan "fee snipingiksi", ja epärehellisen Miner:n mahdollisuus onnistua siinä, jos kaikki muut Miner:t ovat rehellisiä, on `(x/(1-x))^2`. Vaikka fee snipingin todennäköisyys onnistua on kaiken kaikkiaan pienempi kuin rehellisen Mining:n, epärehellisen Mining:n yrittäminen voi olla kannattavampi vaihtoehto, jos edellisen lohkon transaktiot maksoivat huomattavasti korkeampia feerateja kuin tällä hetkellä Mempool:ssa olevat transaktiot - pieni mahdollisuus suureen summaan voi olla arvokkaampi kuin suuri mahdollisuus pieneen summaan.

Tulevaisuuden toiveitamme heikentää se, että jos kaivostyöläiset alkavat harjoittaa palkkioiden salametsästystä, se kannustaa muita tekemään samoin, jolloin rehellisiä kaivostyöläisiä jää vielä vähemmän. Tämä voi heikentää Bitcoin:n yleistä turvallisuutta vakavasti. Harding luettelee vielä muutamia mahdollisia vastatoimia, kuten transaktioiden aikalukkojen käyttäminen rajoittaakseen sitä, missä kohtaa Blockchain:ta transaktio voi esiintyä.


Kun siis otetaan huomioon, että yksimielisyys rajallisesta Supply:stä säilyy, lohkotuki nollautuu vuoden 2140 tienoilla, kiitos [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki), jossa korjattiin hyvin pitkäaikainen inflaatiovika. Riittävätkö transaktiomaksut sen jälkeen turvaamaan verkon?


Sitä on mahdotonta sanoa, mutta tiedämme muutamia asioita:


- Vuosisata on Bitcoin:n näkökulmasta *pitkä* aika. Jos se on yhä olemassa, se on todennäköisesti kehittynyt valtavasti.
- Jos ylivoimainen taloudellinen enemmistö katsoo tarpeelliseksi muuttaa sääntöjä ja ottaa käyttöön esimerkiksi ikuisen 0,1 tai 1 prosentin vuotuisen rahan inflaation, Supply Bitcoin:n Supply ei ole enää rajallinen.
- Kun korttelituki on nolla ja Mempool on tyhjä tai lähes tyhjä, tilanne voi muuttua epävakaaksi maksullisuuden vuoksi.


Koska siirtyminen vain maksulliseen Block reward:ään on niin kaukana tulevaisuudessa, voisi olla viisasta olla tekemättä hätiköityjä johtopäätöksiä ja yrittää korjata mahdolliset ongelmat, kun vielä voimme. Esimerkiksi Peter Todd uskoo, että on olemassa todellinen riski, että Bitcoin:n turvabudjetti ei riitä tulevaisuudessa, ja näin ollen hän kannattaa pientä jatkuvaa inflaatiota Bitcoin:ssä. Hän on kuitenkin myös sitä mieltä, ettei ole hyvä idea keskustella tällaisesta asiasta tällä hetkellä, kuten [hän sanoi What Bitcoin Did -podcastissa] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Mutta se on riski, joka on 10-20 vuoden päässä tulevaisuudessa. Se on hyvin pitkä aika. Ja kuka helvetti tietää, mitä riskejä siihen mennessä on olemassa?

Ehkä voisimme ajatella Bitcoin:n olevan jotain orgaanista. Kuvitelkaa pieni, hitaasti kasvava tammikasvi. Kuvittele myös, ettet ole koskaan elämäsi aikana nähnyt täysikasvuista puuta. Eikö silloin olisi viisasta hillitä valvontakysymyksiänne sen sijaan, että asetatte etukäteen kaikki säännöt sille, miten tämän kasvin pitäisi antaa kehittyä ja kasvaa?


### Johtopäätös äärellisestä Supply:stä



Sitä, kasvaako Bitcoin Supply yli 21 miljoonan, emme voi sanoa tänään, eikä se luultavasti ole niin huono asia. Sen varmistaminen, että turvallisuusbudjetti pysyy riittävän suurena, on ratkaisevan tärkeää mutta ei kiireellistä. Käydään tämä keskustelu 10-50 vuoden kuluttua, kun tiedämme enemmän. Jos se on vielä ajankohtaista.


# Bitcoin Gouvernance

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Päivittäminen

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Bitcoin:n päivittäminen turvallisella tavalla voi olla erittäin vaikeaa. Joidenkin muutosten käyttöönotto kestää useita vuosia. Tässä luvussa tutustumme Bitcoin:n päivittämiseen liittyvään yleiseen sanastoon ja tutkimme joitakin esimerkkejä sen protokollan historiallisista päivityksistä sekä niistä saatuja oivalluksia. Lopuksi puhumme ketjujen jakamisesta ja niihin liittyvistä riskeistä ja kustannuksista.


Jotta pääsisit virittäytymään tähän lukuun, sinun kannattaa lukea [David Hardingin kappale harmoniasta ja epäsointuisuudesta] (https://bitcointalk.org/dec/p1.html):


> Bitcoin Asiantuntijat puhuvat usein konsensuksesta, jonka merkitys on abstrakti ja Hard vaikeasti määriteltävissä. Mutta sana konsensus on kehittynyt latinan sanasta concentus, "yhdessä laulava harmonia", joten ei puhuta Bitcoin konsensuksesta vaan Bitcoin harmoniasta.
>

> Bitcoin toimii harmonian ansiosta. Tuhannet täydet solmut työskentelevät kukin itsenäisesti varmistaakseen, että niiden vastaanottamat transaktiot ovat päteviä, mikä tuottaa harmonisen sopimuksen Bitcoin Ledger:n tilasta ilman, että yhdenkään solmun operaattorin tarvitsee luottaa keneenkään muuhun. Se muistuttaa kuoroa, jossa jokainen jäsen laulaa samaa laulua samaan aikaan tuottaakseen jotain paljon kauniimpaa kuin kukaan heistä voisi yksinään tuottaa.
>

> Bitcoin:n harmonian tuloksena syntyy järjestelmä, jossa bitcoinit ovat turvassa paitsi pikkuvarkailta (edellyttäen, että pidät avaimesi turvassa) myös loputtomalta inflaatiolta, massakonfiskaatiolta tai kohdennetulta takavarikolta tai yksinkertaisesti byrokraattiselta suolta, joka on perinteinen rahoitusjärjestelmä.

Tässä luvussa käsitellään sitä, miten Bitcoin:ää voidaan päivittää aiheuttamatta epäsopua. Yhdenmukaisuuden säilyttäminen eli konsensuksen ylläpitäminen on todellakin yksi Bitcoin:n kehittämisen suurimmista haasteista. Päivitysmekanismeihin liittyy paljon vivahteita, joita voi ymmärtää parhaiten tutkimalla aiempien päivitysten todellisia tapauksia. Tästä syystä luvussa keskitytään paljon historiallisiin esimerkkeihin, ja se alkaa alustamalla hyödyllisellä sanastolla.


### Sanasto



Wikipedian mukaan [eteenpäin yhteensopivuus] (https://en.wikipedia.org/wiki/Forward_compatibility) tarkoittaa tilaa, jossa vanha ohjelmisto voi käsitellä uudempien ohjelmistojen luomia tietoja ja jättää huomiotta ne osat, joita se ei ymmärrä:


Standardi tukee yhteensopivuutta eteenpäin, jos aiempien versioiden mukainen tuote voi käsitellä standardin myöhempiä versioita varten suunniteltuja syötteitä ja jättää huomiotta uudet osat, joita se ei ymmärrä.


Päinvastoin, [taaksepäin yhteensopivuus] (https://en.wikipedia.org/wiki/Backward_compatibility) tarkoittaa sitä, että vanhan ohjelmiston tietoja voidaan käyttää uudemmissa ohjelmistoissa. Muutoksen sanotaan olevan täysin yhteensopiva, jos se on sekä eteenpäin että taaksepäin yhteensopiva.


Bitcoin-konsensussääntöjen muutoksen sanotaan olevan *Soft Fork*, jos se on täysin yhteensopiva. Tämä on yleisin tapa päivittää Bitcoin useista syistä, joita käsittelemme myöhemmin tässä luvussa. Jos Bitcoin-konsensussääntöjen muutos on taaksepäin yhteensopiva mutta ei eteenpäin yhteensopiva, sitä kutsutaan *Hard Fork*:ksi.


Tekninen yleiskatsaus Soft-haaroista ja Hard-haaroista on luettavissa [Grokking Bitcoin -kirjan 11. luvussa](https://rosenbaum.se/book/grokking-Bitcoin-11.html). Siinä selitetään nämä termit ja syvennytään myös päivitysmekanismeihin. On suositeltavaa, vaikkakaan ei ehdottoman välttämätöntä, perehtyä tähän ennen kuin jatkat lukemista.


### Historialliset parannukset



Bitcoin ei ole nykyään sama kuin lohkon Genesis perustamisen aikaan. Vuosien varrella on tehty useita parannuksia. Vuonna 2018 Eric Lombrozo [puhui Breaking Bitcoin -konferenssissa](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) Bitcoin:n eri päivitysmekanismeista ja huomautti, kuinka paljon ne ovat kehittyneet ajan myötä. Hän jopa selitti, miten Satoshi Nakamoto päivitti Bitcoin:n kerran Hard Fork:n kautta:


> Bitcoin:ssa oli itse asiassa Hard-Fork, jonka Satoshi toteutti, emmekä ikinä tekisi sitä tällä tavalla - se on aika huono tapa tehdä se. Jos katsot git-toimituksen kuvausta täällä [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], hän sanoo jotain palautetusta makefile.unix wx-configin versiosta 0.3.6. Aivan. Siinä lukee vain se. Siinä ei ole mitään viitteitä siitä, että siinä on rikkova muutos. Hän periaatteessa piilotti sen sinne. Hän myös [kirjoitti bitcointalkiin](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) ja sanoi, että päivitä 0.3.6:een ASAP. Korjasimme toteutusvirheen, jonka vuoksi on mahdollista, että väärät transaktiot voidaan näyttää hyväksytyiksi. Älä hyväksy Bitcoin-maksuja ennen kuin päivität 0.3.6:een. Jos et voi päivittää heti, olisi parasta sulkea Bitcoin-solmusi siihen asti. Ja sitten kaiken lisäksi, en tiedä miksi hän päätti tehdä tämänkin, hän päätti lisätä joitakin optimointeja samaan koodiin. Korjaa bugi ja lisää joitakin optimointeja.

Hän huomauttaa, että oli se tahallista tai ei, tämä Hard Fork loi mahdollisuuksia tuleville Soft-haaroille, nimittäin skriptioperaattoreille (opkoodeille) OP_NOP1-OP_NOP10. Tarkastelemme tätä koodimuutosta tarkemmin artikkelissa cve-2010-5141. Näitä op-koodeja on käytetty tähän mennessä kahdessa Soft-haarassa:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo antaa myös yleiskatsauksen siitä, miten päivitysmekanismit ovat kehittyneet vuosien varrella vuoteen 2017 asti. Sen jälkeen on otettu käyttöön vain yksi toinen suuri päivitys, Taproot. Pitkä ja jokseenkin kaoottinen prosessi, joka johti sen aktivointiin, on auttanut meitä saamaan lisää tietoa Bitcoin:n päivitysmekanismeista.


#### SegWit päivitys



Kaikki SegWit:a edeltäneet päivitykset olivat olleet enemmän tai vähemmän kivuttomia, mutta tämä oli erilainen. Kun SegWit:n aktivointikoodi julkaistiin lokakuussa 2016, Bitcoin-käyttäjät näyttivät saavan sille valtaisan tuen, mutta jostain syystä kaivostyöntekijät eivät ilmoittaneet tukevansa tätä päivitystä, mikä pysäytti aktivoinnin, eikä ratkaisua ollut näkyvissä.


Aaron van Wirdum kuvaa tätä mutkaista tietä Bitcoin Magazine -lehden artikkelissaan [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Hän aloittaa selittämällä, mikä SegWit on ja miten se liittyy lohkokokokeskusteluun. Sitten van Wirdum kuvaa tapahtumien kulkua, joka johti sen lopulliseen aktivointiin. Prosessin keskiössä oli päivitysmekanismi nimeltä *käyttäjän aktivoima Soft Fork*, tai lyhyesti UASF, jota ehdotti käyttäjä Shaolinfry:


> Shaolinfry ehdotti vaihtoehtoa: käyttäjän aktivoima Soft Fork (UASF). Hash-virran aktivoinnin sijaan käyttäjän aktivoimassa Soft Fork:ssa olisi "'lippupäivän aktivointi', jossa solmut aloittavat täytäntöönpanon ennalta määritettynä ajankohtana tulevaisuudessa" Niin kauan kuin tällainen UASF pannaan täytäntöön taloudellisen enemmistön toimesta, tämän pitäisi pakottaa enemmistö kaivostyöläisistä noudattamaan (tai aktivoimaan) Soft Fork.

Hän mainitsee muun muassa Shaolinfryn sähköpostin Bitcoin-dev-postituslistalle. Siinä Shaolinfry [vastusti Miner:n aktivoituja Soft-haaroja](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html) ja luetteli useita niiden ongelmia:


> Ensinnäkin se edellyttää, että Hash:n teho vahvistetaan aktivoinnin jälkeen.  BIP66 Soft Fork oli tapaus, jossa 95 prosenttia Hashrate:stä ilmoitti valmiudesta, mutta todellisuudessa noin puolet ei todellisuudessa validoinut päivitettyjä sääntöjä ja louhi vahingossa virheellisen lohkon.
>

> Toiseksi Miner-signaalinannossa on luonnollinen veto-oikeus, joka antaa pienelle osalle Hashrate:sta mahdollisuuden kieltää päivityksen aktivoimisen kaikkien solmupisteissä. Tähän mennessä Soft-haarat ovat käyttäneet hyväkseen suhteellisen keskitettyä Mining-maisemaa, jossa on suhteellisen vähän Mining-pooleja, jotka rakentavat kelvollisia lohkoja; kun siirrymme kohti Hashrate:n hajauttamista, on todennäköistä, että kärsitään yhä enemmän "päivitysinertiasta", joka estää useimmat päivitykset.

Shaolinfry kiinnitti huomiota myös Miner-signaalin yleiseen väärintulkintaan: ihmiset luulivat yleensä, että se oli keino, jolla kaivostyöläiset voivat päättää protokollan päivityksistä, eikä niinkään toiminto, joka auttoi päivitysten koordinoinnissa. Tämän väärinkäsityksen vuoksi kaivostyöläiset saattoivat myös tuntea velvollisuudekseen julistaa julkisesti mielipiteensä tietystä Soft Fork:sta, ikään kuin se antaisi ehdotukselle painoarvoa.


Ammattikorkeakoulun ehdotus on lyhyesti sanottuna "liputuspäivä", jolloin solmut alkavat panna täytäntöön tiettyjä uusia sääntöjä. Näin louhijoiden ei tarvitse tehdä kollektiivista työtä päivityksen koordinoimiseksi, vaan ne *voivat* käynnistää aktivoinnin aiemmin kuin liputuspäivänä, jos tarpeeksi monta lohkoa ilmoittaa tukevansa sitä:


> Ehdotan, että saat molempien maailmojen parhaat puolet. Koska käyttäjän aktivoima Soft Fork tarvitsee suhteellisen pitkän läpimenoajan ennen aktivointia, voimme yhdistää sen BIP9:n kanssa ja antaa mahdollisuuden nopeampaan Hash-virran koordinoituun aktivointiin tai aktivointiin lippupäivänä, riippuen siitä, kumpi tapahtuu aikaisemmin.
> Molemmissa tapauksissa voimme hyödyntää BIP9:n varoitusjärjestelmiä. Muutos on suhteellisen yksinkertainen: lisätään aktivointiaikaparametri, joka siirtää BIP9-tilan LOCKED_IN-tilaan ennen BIP9:n käyttöönottoaikakatkaisun päättymistä.

Tämä ajatus herätti paljon kiinnostusta, mutta se ei näyttänyt saavan lähes yksimielistä kannatusta, mikä aiheutti huolta mahdollisesta ketjun hajoamisesta. Aaron van Wirdumin artikkelissa kerrotaan, miten asia lopulta ratkaistiin James Hilliardin kirjoittaman [BIP91](https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki) ansiosta:


> Hilliard ehdotti hieman monimutkaista mutta nokkelaa ratkaisua, jolla kaikki olisi yhteensopivaa: Bitcoin Core -kehitystiimin ehdottama erillisen todistajan aktivointi, BIP148-ammattikorkeakoulun ammattikorkeakoulun toimintajärjestelmä ja New Yorkin sopimuksen aktivointimekanismi. Hänen BIP91:nsä voisi pitää Bitcoin:n ehjänä - ainakin SegWit:n aktivoinnin ajan.

Tässä rajatarkastusasemassa oli otettava huomioon joitakin monimutkaisempia tekijöitä (esim. niin sanottu New Yorkin sopimus). Kannustamme teitä lukemaan Van Wirdumin artikkelin kokonaisuudessaan, jotta voitte tutustua tarinan moniin mielenkiintoisiin yksityiskohtiin.


#### SegWit:n jälkeinen keskustelu


SegWit:n käyttöönoton jälkeen syntyi keskustelu käyttöönottomekanismeista. Kuten Eric Lombrozo [Breaking Bitcoin -konferenssissa pitämässään puheessa] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) ja Shaolinfry totesivat, Miner:n aktivoima Soft Fork ei ole ihanteellinen päivitysmekanismi:


> Jossain vaiheessa haluamme todennäköisesti lisätä Bitcoin-protokollaan lisää ominaisuuksia. Tämä on suuri filosofinen kysymys, jonka kysymme itseltämme. Teemmekö UASF:n seuraavaa versiota varten? Entäpä hybridi lähestymistapa? Miner:n aktivointi yksinään on suljettu pois. bip9:ää emme aio käyttää enää.

Tammikuussa 2020 Matt Corallo [lähetti sähköpostin](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) Bitcoin-dev-postituslistalle, joka käynnisti keskustelun Soft Fork:n tulevista käyttöönottomekanismeista. Hän luetteli viisi tavoitetta, jotka hänen mielestään olivat olennaisia päivityksessä. David Harding [tiivistää ne Bitcoin Optechin uutiskirjeessä](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) seuraavasti:


> Mahdollisuus keskeyttää, jos ehdotettuja konsensussääntöjä koskevia muutoksia vastustetaan vakavasti . Varataan riittävästi aikaa päivitetyn ohjelmiston julkaisemisen jälkeen, jotta voidaan varmistaa, että suurin osa taloussolmuista päivitetään kyseisten sääntöjen noudattamista varten. Odotetaan, että verkon Hash -nopeus on suunnilleen sama ennen muutosta ja sen jälkeen sekä siirtymäkauden aikana . Estetään mahdollisuuksien mukaan sellaisten lohkojen luominen, jotka eivät ole uusien sääntöjen mukaan päteviä, mikä voisi johtaa vääriin vahvistuksiin päivittämättömissä solmuissa ja SPV-asiakkaissa . Varmuus siitä, että suruttajat tai partisaanit eivät voi käyttää keskeytysmekanismeja väärin estääkseen laajalti toivottua päivitystä, johon ei liity tunnettuja ongelmia

Corallo ehdottaa yhdistelmää, jossa Miner aktivoi Soft Fork:n ja käyttäjä aktivoi Soft Fork:n:


> Hieman konkreettisempana aktivointimenetelmä, joka luo oikean ennakkotapauksen ja ottaa asianmukaisesti huomioon edellä mainitut tavoitteet, olisi mielestäni seuraava:
>

> 1) tavanomainen BIP 9:n käyttöönotto, jossa on yhden vuoden aikahorisontti
aktivointi 95 prosentin Miner-valmiudella, +

> 2) jos aktivointia ei tapahdu vuoden kuluessa, kuuden kuukauden mittainen
rauhoittumisjakso, jonka aikana yhteisö voi analysoida ja keskustella

syyt, joiden vuoksi toimintaa ei ole käynnistetty, ja +

> 3) jos se on järkevää, yksinkertainen komentorivin/Bitcoin.conf-parametri, jota on tuettu alkuperäisestä käyttöönottojulkaisusta lähtien, antaisi käyttäjille mahdollisuuden valita BIP 8 -käyttöönoton, jossa lippupäivän aktivoinnin aikahorisontti on 24 kuukautta (samoin kuin uusi Bitcoin Core -julkaisu, jossa lippu otetaan käyttöön yleisesti).
>

> Tämä tarjoaa hyvin pitkän aikajänteen tavanomaisemmalle aktivoinnille ja varmistaa samalla, että 5. kohdan tavoitteet saavutetaan, vaikka näissä tapauksissa aikajännettä on pidennettävä huomattavasti 3. kohdan tavoitteiden saavuttamiseksi. Bitcoin:n kehittäminen ei ole kilpailu. Jos meidän on pakko, 42 kuukauden odottaminen varmistaa, ettemme luo negatiivista ennakkotapausta, jota voimme katua Bitcoin:n kasvun jatkuessa.

#### Taproot-päivitys - Nopea oikeudenkäynti



Kun Taproot oli valmis käyttöönotettavaksi lokakuussa 2020, mikä tarkoitti sitä, että kaikki sen konsensussääntöihin liittyvät tekniset yksityiskohdat oli toteutettu ja ne olivat saaneet yhteisön laajan hyväksynnän, alkoivat keskustelut siitä, miten se todella otettaisiin käyttöön, kiihtyä. Nämä keskustelut olivat olleet siihen asti melko hiljaisia.


Monet ehdotukset aktivointimekanismeiksi alkoivat liikkua, ja David Harding

[tiivistelmä Bitcoin Wikissä](https://en.Bitcoin.it/wiki/Taproot_activation_proposals). Artikkelissaan hän selitti joitakin BIP8:n ominaisuuksia, ja siihen oli tuolloin tehty joitakin muutoksia sen joustavuuden lisäämiseksi.


> Tätä asiakirjaa kirjoitettaessa [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) on laadittu vuonna 2017 saatujen kokemusten perusteella. Yksi merkittävä muutos BIP:ien 9+148 jälkeen on se, että pakotettu aktivointi perustuu nyt lohkon korkeuteen eikä menneen ajan mediaaniin; toinen merkittävä muutos on se, että pakotettu aktivointi on boolean-parametri, joka valitaan, kun Soft Fork:n aktivointiparametrit asetetaan joko ensimmäistä käyttöönottoa varten tai päivitetään myöhemmässä käyttöönotossa.

BIP8 ilman pakotettua aktivointia on hyvin samankaltainen kuin [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) versio bittien kanssa, jossa on aikakatkaisu ja viive, ainoana merkittävänä erona on BIP8:n käyttämä lohkon korkeus verrattuna BIP9:n käyttämään mediaaniajan menneisyyteen. Tämä asetus sallii yrityksen epäonnistumisen (mutta sitä voidaan yrittää myöhemmin uudelleen).


Pakkoaktivoinnin sisältävä BIP8 päättyy pakolliseen signalointijaksoon, jonka aikana kaikkien sen sääntöjen mukaisesti tuotettujen lohkojen on ilmoitettava Soft Fork:n valmiudesta tavalla, joka käynnistää aktivoinnin saman Soft Fork:n aikaisemmassa käyttöönotossa, jossa ei ole pakollista aktivointia. Toisin sanoen, jos solmuversio x julkaistaan ilman pakollista aktivointia ja myöhemmin julkaistaan versio y, joka onnistuneesti pakottaa louhijat aloittamaan valmiuden ilmoittamisen saman ajanjakson kuluessa, molemmat versiot alkavat soveltaa uusia konsensussääntöjä samanaikaisesti.


Tarkistetun BIP8-ehdotuksen joustavuus mahdollistaa joidenkin muiden ajatusten ilmaisemisen sen suhteen, miltä ne näyttäisivät BIP8:n avulla. Näin saadaan yhteinen tekijä, jota voidaan käyttää monien eri ehdotusten luokittelussa.


Tästä eteenpäin keskustelut kiihtyivät erityisesti siitä, pitäisikö `lockinontimeout` olla `true` (kuten käyttäjän aktivoimassa Soft Fork:ssä, johon Harding viittasi nimellä "BIP8 with forced activation") vai `false` (kuten Miner:ssa aktivoidussa Soft Fork:ssä, johon Harding viittasi nimellä "BIP8 without forced activation").


Yksi luetelluista ehdotuksista oli otsikoitu "Katsotaan, mitä tapahtuu". Jostain syystä tämä ehdotus ei saanut juurikaan vetoapua ennen kuin vasta seitsemän kuukautta myöhemmin.


Seitsemän kuukauden aikana keskustelu jatkui, eikä tuntunut siltä, että olisi päästy laajaan yhteisymmärrykseen siitä, mitä käyttöönottomekanismia olisi käytettävä. Oli lähinnä kaksi leiriä: toinen piti parempana `lockinontimeout=true` (ammattikorkeakoulun väki) ja toinen piti parempana `lockinontimeout=false` ("kokeile ja jos se epäonnistuu, mieti uudelleen" -väki). Koska mikään näistä vaihtoehdoista ei saanut ylivoimaista kannatusta, keskustelu kulki ympyrää, eikä näyttäisi olleen mitään tietä eteenpäin. Osa näistä keskusteluista käytiin IRC:ssä kanavalla nimeltä ##Taproot-activation, mutta [5. maaliskuuta 2021](https://gnusha.org/Taproot-activation/2021-03-05.log) jokin muuttui:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


"Katsotaan, mitä tapahtuu" -lähestymistapa näytti vihdoin napsahtavan ihmisten mieliin. Tätä prosessia kutsuttiin myöhemmin "Speedy Trialiksi" sen lyhyen merkkipaalun vuoksi. David Harding selittää tätä ajatusta laajemmalle yhteisölle artikkelissa

[sähköposti Bitcoin-dev-postituslistalle](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> Tämän ehdotuksen aiempi versio dokumentoitiin yli 200 päivää sitten, ja Taproot:n taustalla oleva koodi sulautettiin Bitcoin Coreen yli 140 päivää sitten.Jos olisimme aloittaneet Speedy Trial -kokeilun Taproot:n sulauttamisen aikaan (mikä on hieman epärealistista), olisimme joko alle kahden kuukauden päässä Taproot:stä tai olisimme siirtyneet seuraavaan aktivointiyritykseen yli kuukausi sitten.
>

> Sen sijaan olemme keskustelleet pitkään, emmekä näytä olevan yhtään lähempänä mielestäni yleisesti hyväksyttävää ratkaisua kuin silloin, kun postituslistalla alettiin keskustella SegWit:n jälkeisistä aktivointijärjestelmistä yli vuosi sitten.Mielestäni Speedy Trial on keino generate:n nopeaan edistymiseen, joka joko lopettaa keskustelun (toistaiseksi, jos aktivointi onnistuu) tai antaa meille todellista tietoa, jonka pohjalta voimme tehdä tulevia Taproot:n aktivointiehdotuksia.

Tätä käyttöönottomekanismia hiottiin kahden kuukauden ajan, minkä jälkeen se julkaistiin [Bitcoin Core versiona 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Louhijat alkoivat nopeasti signaloida tämän päivityksen siirtämällä käyttöönottotilan tilaan `LOCKED_IN`, ja armonaika-ajan jälkeen Taproot-säännöt aktivoitiin marraskuun 2021 puolivälissä lohkossa [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Tulevat käyttöönottomekanismit


Kun otetaan huomioon viimeisimpien Soft-haarojen, SegWit:n ja Taproot:n, ongelmat, ei ole selvää, miten seuraava päivitys otetaan käyttöön. Speedy Trialia käytettiin Taproot:n käyttöönotossa, mutta sitä käytettiin ammattikorkeakoulun ja MASF:n väkijoukkojen välisen kuilun kuromiseksi umpeen, ei siksi, että se olisi osoittautunut parhaaksi tunnetuksi käyttöönottomekanismiksi.


### Riskit


Minkä tahansa Fork:n aktivoinnin aikana, olipa kyseessä sitten Hard tai Soft, Miner aktivoitu tai käyttäjän aktivoima, on olemassa riski pitkäaikaisesta ketjun halkeamisesta. Yli muutaman korttelin kestävä halkeama voi aiheuttaa vakavaa vahinkoa Bitcoin:n ympärillä vallitsevalle tunnetilalle ja sen hinnalle. Mutta ennen kaikkea se aiheuttaisi suurta hämmennystä siitä, mikä Bitcoin on. Onko Bitcoin tämä ketju vai tuo ketju?


Käyttäjän aktivoiman Soft Fork:n riskinä on, että uudet säännöt aktivoituvat, vaikka suurin osa Hash:n voimasta ei niitä tukisi. Tämä skenaario johtaisi pitkäkestoiseen ketjun jakautumiseen, joka jatkuisi, kunnes valtaosa Hash-valtakunnasta ottaa uudet säännöt käyttöön. Erityisesti Hard voisi kannustaa louhijoita siirtymään uuteen ketjuun, jos he olivat jo louhineet lohkoja jakautumisen jälkeen vanhassa ketjussa, koska vaihtamalla haaraa he luopuisivat omista lohkopalkkioistaan. On kuitenkin syytä mainita eräs merkittävä episodi: maaliskuussa 2013 pitkäkestoinen split, tapahtui tahattoman Hard Fork:n vuoksi, ja vastoin tätä kannustinta kaksi suurta Mining-poolia teki päätöksen luopua haarasta splitissä konsensuksen palauttamiseksi.


Toisaalta Miner:n aktivoiman Soft:n Fork:n riski johtuu siitä, että kaivostyöläiset voivat harjoittaa väärää signalointia, mikä tarkoittaa, että muutosta tukevan Hash:n tehon todellinen osuus voi olla pienempi kuin miltä se näyttää. Jos todellinen kannatus ei käsitä enemmistöä Hash-voimasta, näkisimme todennäköisesti edellisessä kappaleessa kuvatun kaltaisen pitkäkestoisen ketjun jakautumisen. Tämä tai ainakin vastaava ongelma on tapahtunut todellisuudessa, kun BIP66 otettiin käyttöön, mutta se saatiin ratkaistua noin 6 lohkon kuluessa.


#### Jakautumisen kustannukset



Jimmy Song [puhui Hard-haarukoihin liittyvistä kustannuksista](https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) Breaking Bitcoin -tapahtumassa Pariisissa, mutta suuri osa siitä, mitä hän sanoi, pätee myös ketjun hajoamiseen epäonnistuneen Soft Fork:n vuoksi. Hän puhui *negatiivisista ulkoisvaikutuksista* ja määritteli ne hinnaksi, jonka joku muu joutuu maksamaan omista toimistasi:


> Klassinen esimerkki negatiivisesta ulkoisvaikutuksesta on tehdas. Ehkä se tuottaa - ehkä se on öljynjalostamo - ja se tuottaa tavaraa, joka on hyväksi taloudelle, mutta se tuottaa myös jotakin, joka on negatiivinen ulkoisvaikutus, kuten saasteita. Se ei ole vain jotakin, josta kaikkien on maksettava, jota on puhdistettava tai josta kaikkien on kärsittävä. Kyse on myös 2. ja 3. asteen vaikutuksista, kuten lisääntyneestä liikenteestä, joka kulkee kohti tehdasta, koska sinne on saatava lisää työntekijöitä. Voi myös olla, että vaarannetaan joitakin luonnonvaraisia eläimiä. Kaikkien ei tarvitse maksaa negatiivisista ulkoisvaikutuksista, vaan ne voivat kohdistua tiettyihin ihmisiin, kuten ihmisiin, jotka aiemmin käyttivät kyseistä tietä, tai eläimiin, jotka olivat tehtaan lähellä, ja he maksavat myös tehtaan aiheuttamista kustannuksista.

Bitcoin:n yhteydessä hän havainnollistaa negatiivisia ulkoisvaikutuksia käyttämällä Bitcoin Cashia (bcash), joka on Hard Fork Bitcoin:n Bitcoin:stä, joka luotiin juuri ennen kyseistä konferenssia vuonna 2017. Hän luokittelee Hard Fork:n negatiiviset ulkoisvaikutukset kertaluonteisiin kustannuksiin ja pysyviin kustannuksiin.


Monista kertaluonteisista kustannuksista hän mainitsee esimerkkinä vaihtojen aiheuttamat kustannukset:


> Meillä on siis joukko vaihtokeskuksia, ja niiden oli maksettava paljon kertaluonteisia kustannuksia. Ensimmäiseksi talletukset ja nostot oli keskeytettävä pariksi päiväksi tai kahdeksi näiden vaihtojen osalta, koska he eivät tienneet, mitä tapahtuisi. Monet näistä pörsseistä joutuivat käyttämään Cold:n varastoja, koska niiden käyttäjät vaativat bcashia. Se on osa niiden fidicuiary velvollisuutta, heidän on tehtävä se. Uusi ohjelmisto on myös tarkastettava. Tämä on jotain, mitä meidän oli tehtävä itbitissä. Haluamme käyttää käteistä - miten teemme sen? Pitääkö meidän ladata electron cash? Onko siinä haittaohjelmia? Meidän on mentävä tarkastamaan se. Meillä oli noin 10 päivää aikaa selvittää, oliko tämä ok vai ei. Ja sitten on päätettävä, sallimmeko vain kertaluonteisen noston vai listaammeko tämän uuden kolikon? Exchange:lle uuden kolikon listaaminen ei ole helppoa - Cold:n säilytykseen, allekirjoittamiseen, talletuksiin ja nostoihin liittyy kaikenlaisia uusia menettelyjä. Tai sitten voisit vain järjestää tämän kertaluonteisen tapahtuman, jossa annat heille heidän käteisrahansa jossain vaiheessa, etkä enää koskaan ajattele sitä. Mutta siinäkin on omat ongelmansa. Ja lopuksi, olipa tapa mikä tahansa, nostot tai listaus - tarvitset uuden infrastruktuurin, joka toimii jollain tavalla token:n kanssa, vaikka kyseessä olisi vain kertaluonteinen nosto. Tarvitset jonkinlaisen tavan antaa nämä tunnukset käyttäjillesi. Jälleen kerran, lyhyellä varoitusajalla. Eikö niin? Tähän ei ole aikaa, se on tehtävä nopeasti.

Hän luettelee myös kauppiaille, maksuprosessoreille, lompakoille, louhijoille ja käyttäjille aiheutuvat kertaluonteiset kustannukset sekä joitakin pysyviä kustannuksia, kuten yksityisyyden suojan menettäminen ja korkeampi reorgien riski.


Kun jako tapahtuu ja ketju, jossa on yleisimmät säännöt, tulee vahvemmaksi kuin ketju, jossa on tiukemmat säännöt, tapahtuu uudelleenjärjestely. Tällä on vakava vaikutus kaikkiin transaktioihin, jotka suoritetaan hävinneessä haarassa. Näistä syistä on todella tärkeää pyrkiä aina välttämään ketjujen jakautumista.


### Johtopäätös päivittämisestä


Bitcoin kasvaa ja kehittyy ajan myötä. Vuosien varrella on käytetty erilaisia päivitysmekanismeja, ja oppimiskäyrä on jyrkkä. Yhä kehittyneempiä ja kestävämpiä menetelmiä keksitään jatkuvasti, kun opimme lisää siitä, miten verkko reagoi.


Bitcoin:n pitämiseksi sopusoinnussa Soft:n haarautuminen on osoittautunut oikeaksi tavaksi edetä, mutta suureen kysymykseen ei ole vieläkään saatu täyttä vastausta: miten otamme Soft:n haarautumisen turvallisesti käyttöön aiheuttamatta eripuraa?


## Vastakkainasettelu

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Tässä luvussa käsitellään *vastapuoliajattelua*, ajattelutapaa, jossa keskitytään siihen, mikä voi mennä pieleen ja miten vastapuoli saattaa toimia. Aloitamme käsittelemällä Bitcoin:n turvallisuusoletuksia ja turvallisuusmallia, minkä jälkeen selitämme, miten tavalliset käyttäjät voivat parantaa itsemääräämisoikeuttaan ja Bitcoin:n Full node:n hajauttamista ajattelemalla vastakkainasettelua. Sen jälkeen tarkastelemme joitakin Bitcoin:ään kohdistuvia todellisia uhkia sekä vastustajan ajatuksia. Lopuksi puhumme *vastarinnan akselista*, joka voi auttaa ymmärtämään, miksi ihmiset ylipäätään työskentelevät Bitcoin:n parissa.


Kun keskustellaan eri järjestelmien turvallisuudesta, on tärkeää ymmärtää, mitkä ovat turvallisuusoletukset. Tyypillinen Bitcoin:n turvallisuusoletus on "diskreetti logaritmiongelma on Hard ratkaistavissa", mikä yksinkertaisesti sanottuna tarkoittaa, että on käytännössä mahdotonta löytää yksityistä avainta, joka vastaa tiettyä julkista avainta. Toinen melko vahva turvallisuusoletus on, että suurin osa verkon hashpowerista on rehellisiä, eli he pelaavat sääntöjen mukaan. Jos nämä oletukset osoittautuvat vääriksi, Bitcoin on vaikeuksissa.


Vuonna 2015 Andrew Poelstra [puhui](https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) Hongkongissa järjestetyssä Scaling Bitcoin -konferenssissa, jossa hän analysoi Bitcoin:n turvallisuusoletuksia. Hän aloittaa huomioimalla, että monet järjestelmät jättävät vastustajat jossain määrin huomiotta; esimerkiksi on todella Hard:n mukaista suojata rakennus kaikentyyppisiltä vastustajilta. Sen sijaan hyväksymme yleensä sen mahdollisuuden, että joku voi polttaa rakennuksen, ja jossain määrin estämme tämän ja muunlaisen vastustajan käyttäytymisen lainvalvonnan jne. avulla.


Katso Greg Maxwellin analogia rakennuksesta:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Mutta verkossa asiat ovat toisin:


> Verkossa meillä ei kuitenkaan ole tätä mahdollisuutta. Meillä on pseudonyymi ja anonyymi käyttäytyminen, kuka tahansa voi ottaa yhteyttä kaikkiin ja vahingoittaa järjestelmää. Jos on mahdollista vahingoittaa järjestelmää, he tekevät sen. Emme voi olettaa, että he ovat näkyvissä ja että he jäävät kiinni.

Tästä seuraa, että kaikki Bitcoin:n tunnetut heikkoudet on jotenkin korjattava, muuten niitä käytetään hyväksi. Loppujen lopuksi Bitcoin on maailman suurin hunajapata.


Poelstra jatkaa mainitsemalla, että Bitcoin on uudenlainen järjestelmä; se on epämääräisempi kuin esimerkiksi allekirjoitusprotokolla, jolla on hyvin selkeät turvallisuusoletukset.


Henkilökohtaisessa blogissaan ohjelmistoinsinööri Jameson Lopp [syventyy tähän](https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> Todellisuudessa Bitcoin-protokollaa rakennettiin ja rakennetaan ilman virallisesti määriteltyä eritelmää tai turvallisuusmallia. Parasta, mitä voimme tehdä, on tutkia järjestelmän toimijoiden kannustimia ja käyttäytymistä, jotta voimme ymmärtää ja yrittää kuvata sitä paremmin.

Meillä on siis järjestelmä, joka näyttää toimivan käytännössä, mutta jonka turvallisuutta emme voi muodollisesti todistaa. Todistaminen ei todennäköisesti ole mahdollista seuraavista syistä

järjestelmän monimutkaisuus.


### Ei vain Bitcoin-asiantuntijoille



Vastakkainasetteluajattelun merkitys ulottuu jossain määrin myös Bitcoin:n jokapäiväisiin käyttäjiin, ei vain Bitcoin:n hardcore-kehittäjiin ja asiantuntijoihin. Ragnar Lifthasir mainitsee [twiittimyrskyssä](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking), kuinka yksinkertaistetut kertomukset Bitcoin:n ympärillä - esimerkiksi "vain HODL" - voivat olla Bitcoin:n itsensä kannalta halventavia, ja toteaa lopuksi seuraavaa


> Jotta voimme tehdä Bitcoin:stä ja itsestämme vahvempia, meidän on ajateltava kuten Bitcoin:een osallistuvat ohjelmistosuunnittelijat. He tekevät vertaisarviointeja ja etsivät armottomasti virheitä. Tekniikkatapahtumissaan he puhuvat kaikista mahdollisista tavoista, joilla ehdotus voi epäonnistua. He ajattelevat vastakkain. He ovat konservatiivisia

Hän kutsuu näitä yksinkertaistettuja kertomuksia monomanioiksi. Tämän määritelmän avulla hän sanoo, että keskittymällä yhteen asiaan - esimerkiksi "vain HODL:aan" - on vaarana jättää huomiotta kiistatta tärkeämmät asiat, kuten Bitcoin:n pitäminen turvassa tai Bitcoin:n käyttäminen Trustless:lla tavalla.


### Uhkat



Bitcoin:ssä on paljon tunnettuja heikkouksia, ja monia niistä käytetään aktiivisesti hyväksi. Jos haluat saada siitä käsityksen, katso [Heikkoudet-sivua] (https://en.Bitcoin.it/wiki/Weaknesses) Bitcoin-wikissä. Siellä mainitaan monenlaisia ongelmia, kuten seuraavat

Wallet varkaus ja palvelunestohyökkäykset:


> Jos hyökkääjä yrittää täyttää verkon hallitsemillaan asiakkailla, on hyvin todennäköistä, että muodostat yhteyden vain hyökkääjän solmuihin. Vaikka Bitcoin ei koskaan käytä solmujen lukumäärää mihinkään, solmun täydellinen eristäminen rehellisestä verkosta voi olla hyödyllistä muiden hyökkäysten suorittamisessa.

Tällaista hyökkäystä kutsutaan *Sybil-hyökkäykseksi*, ja se tapahtuu aina, kun yksi taho hallitsee useita solmuja verkossa ja käyttää niitä esiintyäkseen useina tahoina.


Kuten lainauksessa mainitaan, Sybil-hyökkäys ei ole tehokas Bitcoin-verkossa, koska äänestäminen ei tapahdu solmujen tai muiden numeroitavien yksiköiden, vaan laskentatehon kautta. Tämä tasainen rakenne tekee järjestelmästä kuitenkin alttiin muille hyökkäyksille. Bitcoin:n wiki-sivulla hahmotellaan myös muita mahdollisia hyökkäyksiä, kuten tiedon piilottamista (usein *eclipse-hyökkäys*), ja tapaa, jolla Bitcoin Core toteuttaa joitakin heuristisia vastatoimia tällaisia hyökkäyksiä vastaan.


Edellä mainitut ovat esimerkkejä todellisista uhkista, joista on huolehdittava.


### Yksinkertainen sabotaasikenttä


![](assets/sabotage-manual.webp)


Ote Yksinkertaisen sabotaasin kenttäoppaasta


Vastustajan mielen ymmärtämiseksi paremmin voisi olla hyödyllistä saada käsitys siitä, miten hän toimii. Toisen maailmansodan aikana toiminut Yhdysvaltain hallituksen elin nimeltä Office of Strategic Services, jonka tehtäviin kuului muun muassa vakoilu, sabotaasi ja propagandan levittäminen, laati henkilöstölleen [käsikirjan] (https://www.gutenberg.org/ebooks/26184) siitä, miten vihollisen sabotointia harjoitetaan asianmukaisesti. Sen nimi oli "Simple Sabotage Field Manual" (Yksinkertainen sabotaasikäsikirja), ja se sisälsi konkreettisia vinkkejä vihollisen soluttautumiseen, jotta sen elämästä tulisi Hard. Vinkit vaihtelivat varastojen polttamisesta harjoitusten kulumisen aiheuttamiseen vihollisen vähentämiseksi

tehokkuus.


Siinä on esimerkiksi osio siitä, miten soluttautuja voi häiritä organisaatioita. Ei ole Hard nähdä, miten tällaista taktiikkaa voitaisiin käyttää kohdistamaan Bitcoin kehitysprosessia, johon kuka tahansa voi osallistua. Asialleen omistautunut hyökkääjä voi jatkuvasti jarruttaa edistymistä loputtomilla huolenaiheilla epäolennaisista asioista, tinkiä tarkoista sanamuodoista ja yrittää toistaa keskusteluja, jotka on jo käsitelty kattavasti. Hyökkääjä voi myös palkata trolliarmeijan moninkertaistaakseen oman tehokkuutensa; tätä voidaan kutsua sosiaaliseksi Sybil-hyökkäykseksi. Käyttämällä sosiaalista Sybil-hyökkäystä he voivat saada sen näyttämään siltä, että ehdotettua muutosta vastustetaan enemmän kuin todellisuudessa on.


Tämä osoittaa, miten päättäväinen valtio voi tehdä ja tekee kaikkensa tuhotakseen vihollisen, myös hajottaakseen sen sisältäpäin. Koska Bitcoin on rahamuoto, joka kilpailee vakiintuneiden fiat-valuuttojen kanssa, on todennäköistä, että valtiot pitävät Bitcoin:ta vihollisena.


### Vastarinnan aksonomi


Eric Voskuil [kirjoittaa Cryptoeconomics wiki-sivullaan](https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) siitä, mitä hän kutsuu "vastarinnan aksioomaksi":


> Toisin sanoen oletetaan, että järjestelmän on mahdollista vastustaa valtiollista valvontaa. Tätä ei hyväksytä tosiseikaksi, vaan sitä pidetään kohtuullisena oletuksena, joka perustuu empiiriseen tutkimukseen samankaltaisten järjestelmien käyttäytymisestä ja johon järjestelmä voidaan perustaa.
>

> Se, joka ei hyväksy vastarinnan aksioomaa, harkitsee täysin erilaista järjestelmää kuin Bitcoin. Jos oletetaan, että järjestelmän ei ole mahdollista vastustaa valtion valvontaa, johtopäätöksissä ei ole järkeä Bitcoin:n yhteydessä - aivan kuten pallogeometrian johtopäätökset ovat ristiriidassa euklidisen geometrian kanssa. Miten Bitcoin voi olla luvaton tai sensuurin kestävä ilman aksioomaa? Ristiriita johtaa tekemään ilmeisiä virheitä yrittäessään järkeistää ristiriitaa.


Hän tarkoittaa lähinnä sitä, että vasta kun oletetaan, että on mahdollista luoda järjestelmä, jota valtiot eivät voi hallita, on mielekästä yrittää.


Tämä tarkoittaa sitä, että Bitcoin:n parissa työskentelevän on hyväksyttävä vastarinnan aksiooma, muuten hänen on parempi käyttää aikansa muihin projekteihin. Tämän aksiooman tunnustaminen auttaa sinua keskittymään kehitystyössäsi todellisiin ongelmiin: valtion tason vastustajien koodaamiseen. Toisin sanoen, ajattele vastarintaisesti.


### Vastakkainasettelua koskeva päätelmä



Hajautetussa järjestelmässä ei voi olla vastuuvelvollisuutta järjestelmän itsensä ulkopuolella, joten Bitcoin:n on estettävä haitallinen käyttäytyminen tiukemmin kuin perinteisten järjestelmien. Vastapuolinen ajattelu on välttämätöntä tällaisessa järjestelmässä.


Jotta Bitcoin pysyisi turvassa, sinun on tunnettava sen viholliset ja niiden kannustimet. Suurin osa uhkista näyttää olevan kansallisvaltioita, joilla on valtavasti taloudellista valtaa verotuksen ja rahan painamisen avulla. Ne eivät luultavasti luovu rahan painamisen etuoikeuksistaan helposti.


## Avoin lähdekoodi

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin on rakennettu käyttäen avoimen lähdekoodin ohjelmistoja. Tässä luvussa analysoidaan, mitä tämä tarkoittaa, miten ohjelmiston ylläpito toimii ja miten Bitcoin:n avoimen lähdekoodin ohjelmistot mahdollistavat luvattoman kehityksen. Tutustumme *valintakryptografiaan*, joka käsittelee kirjastojen valintaa ja käyttöä kryptografisissa järjestelmissä. Luvussa on jakso Bitcoin:n tarkistusprosessista, jonka jälkeen on toinen jakso siitä, miten Bitcoin:n kehittäjät saavat rahoitusta. Viimeisessä jaksossa puhutaan siitä, miten Bitcoin:n avoimen lähdekoodin kulttuuri voi näyttää ulkopuolelta todella oudolta ja miksi tämä koettu outous on oikeastaan merkki hyvästä terveydestä.


Useimmat Bitcoin-ohjelmistot, erityisesti Bitcoin Core, ovat avoimen lähdekoodin ohjelmistoja. Tämä tarkoittaa sitä, että ohjelmiston lähdekoodi on yleisön saatavilla, jotta sitä voidaan tutkia, muokata, muokata ja jakaa edelleen. Avoimen lähdekoodin määritelmä osoitteessa [](https://opensource.org/osd) sisältää muun muassa seuraavat tärkeät kohdat:


> Vapaa jakelu: Lisenssi ei saa rajoittaa ketään osapuolta myymästä tai luovuttamasta ohjelmistoa osana ohjelmistokokonaisjakelua, joka sisältää ohjelmia useista eri lähteistä. Lisenssi ei saa vaatia rojaltia tai muuta maksua tällaisesta myynnistä.
>

> Lähdekoodi: Ohjelman on sisällettävä lähdekoodi, ja sen jakelun on oltava mahdollista sekä lähdekoodina että käännettynä. Jos jotakin tuotteen muotoa ei jaeta lähdekoodin kanssa, on oltava hyvin julkistettu keino saada lähdekoodi enintään kohtuullisin kopiointikustannuksin, mieluiten lataamalla se Internetin kautta maksutta. Lähdekoodin on oltava ensisijainen muoto, jossa ohjelmoija muuttaisi ohjelmaa. Tarkoituksellisesti peitetty lähdekoodi ei ole sallittua. Välimuotoja, kuten esikäsittelijän tai kääntäjän tulosta, ei sallita.
>

> Johdetut teokset: Lisenssin on sallittava muutokset ja johdetut teokset, ja niitä on voitava levittää samoin ehdoin kuin alkuperäisen ohjelmiston lisenssiä.

Bitcoin Core noudattaa tätä määritelmää jakelemalla sitä [MIT-lisenssin] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING) mukaisesti:


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Kuten luvussa "Älä luota, tarkista" todettiin, käyttäjien on tärkeää pystyä tarkistamaan, että heidän käyttämänsä Bitcoin-ohjelmisto "toimii kuten mainostetaan". Tätä varten heillä on oltava rajoittamaton pääsy sen ohjelmiston lähdekoodiin, jonka he haluavat tarkistaa.


Seuraavissa osioissa tarkastelemme Bitcoin:n avoimen lähdekoodin ohjelmistojen muita mielenkiintoisia näkökohtia.


### Ohjelmistojen ylläpito



Bitcoin Coren lähdekoodia ylläpidetään Git-tietokannassa, joka sijaitsee osoitteessa [GitHub](https://github.com/Bitcoin/Bitcoin). Kuka tahansa voi kloonata juuri tuon arkiston kysymättä lupaa ja sitten tarkastaa, rakentaa tai tehdä muutoksia siihen paikallisesti. Tämä tarkoittaa, että arkistosta on tuhansia kopioita ympäri maailmaa. Nämä kaikki ovat kopioita samasta arkistosta, joten mikä tekee tästä tietystä GitHub Bitcoin Core -arkistosta niin erityisen? Teknisesti se ei ole lainkaan erityinen, mutta sosiaalisesti siitä on tullut Bitcoin-kehityksen keskipiste.


Bitcoin- ja tietoturva-asiantuntija Jameson Lopp selittää tämän hyvin [blogikirjoituksessaan](https://blog.lopp.net/who-controls-Bitcoin-core-/) "Who Controls Bitcoin Core?":


> Bitcoin Core on pikemminkin Bitcoin-protokollan kehittämisen keskipiste kuin ohjaus- ja valvontapiste. Jos se lakkaisi jostain syystä olemasta, syntyisi uusi keskipiste - tekninen viestintäalusta, johon se perustuu (tällä hetkellä GitHub-tietovarasto), on pikemminkin mukavuuskysymys kuin määrittelyn/projektin eheyden kysymys. Itse asiassa olemme jo nähneet Bitcoin:n kehittämisen painopisteen vaihtavan alustoja ja jopa nimiä!

Hän jatkaa selittämällä, miten Bitcoin Core -ohjelmistoa ylläpidetään ja suojataan haitallisilta koodimuutoksilta. Tämän koko artikkelin yleistajuinen anti on tiivistetty aivan sen lopussa:


> Kukaan ei valvo Bitcoin:tä.
>

> Kukaan ei hallitse Bitcoin:n kehittämisen painopistettä.

Bitcoin-ytimen kehittäjä Eric Lombrozo kertoo lisää kehitysprosessista [Medium-postauksessaan](https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) otsikolla "The Bitcoin Core Merge Process":


> Kuka tahansa voi Fork koodipohjan arkistoon ja tehdä mielivaltaisia muutoksia omaan arkistoonsa. He voivat halutessaan rakentaa asiakkaan omasta arkistostaan ja käyttää sitä sen sijaan. He voivat myös tehdä binäärikokoonpanoja, joita muut voivat ajaa.
>

> Jos joku haluaa yhdistää omassa arkistossaan tekemänsä muutoksen Bitcoin Coreen, hän voi lähettää vetopyynnön. Kun pyyntö on lähetetty, kuka tahansa voi tarkastella muutoksia ja kommentoida niitä riippumatta siitä, onko hänellä commit-oikeudet itse Bitcoin Coreen vai ei.

On syytä huomata, että julkaisupyyntöjen yhdistäminen arkistoon voi kestää hyvin kauan, ennen kuin ylläpitäjät yhdistävät ne, ja se johtuu yleensä tarkistuksen puutteesta, joka usein johtuu *katsojien* puutteesta.


Lombrozo puhuu myös prosessista, joka ympäröi konsensusmuutoksia, mutta se ei kuulu tämän luvun piiriin. Katso aiemmasta luvusta "Päivitykset" lisätietoja siitä, miten Bitcoin-protokollaa päivitetään.


### Luvaton kehittäminen



Olemme todenneet, että kuka tahansa voi kirjoittaa koodia Bitcoin Coreen kysymättä lupaa, mutta ei välttämättä saada sitä yhdistettyä Git-päätietovarastoon. Tämä vaikuttaa kaikkiin muutoksiin, graafisen käyttäjän Interface värimaailman muuttamisesta siihen, miten vertaisverkkoviestit muotoillaan, ja jopa konsensussääntöihin eli sääntöjoukkoon, joka määrittelee kelvollisen Blockchain:n. Tämä vaikuttaa kaikkiin muutoksiin, kuten Interface:n värimaailman muuttamiseen, vertaisverkkoviestien muotoiluun ja jopa konsensussääntöihin.


Todennäköisesti yhtä tärkeää on, että käyttäjät voivat vapaasti kehittää järjestelmiä Bitcoin:n päälle kysymättä lupaa. Olemme nähneet lukemattomia menestyksekkäitä ohjelmistoprojekteja, jotka on rakennettu Bitcoin:n päälle, kuten esimerkiksi seuraavat:



- Lightning Network: Maksuverkko, joka mahdollistaa hyvin pienten summien nopean maksamisen. Se vaatii hyvin vähän On-Chain Bitcoin maksutapahtumia. Erilaisia yhteentoimivia toteutuksia on olemassa, kuten [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) ja [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Useat osapuolet yhdistävät maksunsa yhdeksi tapahtumaksi, jotta Address klusterointi olisi vaikeampaa. Erilaisia toteutuksia on olemassa.
- Sivuketjut: Tämä järjestelmä voi lukita kolikon Bitcoin:n Blockchain:ssa avatakseen sen jossakin toisessa Blockchain:ssa. Näin bitcoinit voidaan siirtää johonkin toiseen Blockchain:een eli Sidechain:ään, jotta voidaan käyttää kyseisen Sidechain:n ominaisuuksia. Esimerkkejä ovat [Blockstreamin Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: Sen avulla voit [Timestamp asiakirjan](https://opentimestamps.org/) Bitcoin:n Blockchain:ssä yksityisesti. Sen jälkeen voit käyttää tätä Timestamp todistamaan, että asiakirjan on täytynyt olla olemassa ennen tiettyä aikaa.


Monet näistä hankkeista eivät olisi olleet mahdollisia ilman luvanvaraista kehittämistä. Kuten puolueettomuutta käsittelevässä luvussa todettiin, jos kehittäjien olisi pitänyt pyytää lupaa rakentaa protokollia Bitcoin:n päälle, kehitettäisiin vain sellaisia protokollia, jotka keskitetty kehittäjien lupakomitea olisi sallinut.


On tavallista, että edellä lueteltujen kaltaiset järjestelmät on lisensoitu avoimen lähdekoodin ohjelmistoiksi, mikä puolestaan antaa ihmisille mahdollisuuden osallistua niiden koodin käyttöön, uudelleenkäyttöön tai tarkistamiseen pyytämättä lupaa. Avoimesta lähdekoodista on tullut Bitcoin-ohjelmistojen lisensoinnin kultainen standardi.


### Pseudonyymin kehitys



Se, että Bitcoin-ohjelmiston kehittämiseen ei tarvitse pyytää lupaa, tuo pöytään mielenkiintoisen ja tärkeän vaihtoehdon: voit kirjoittaa ja julkaista koodia Bitcoin Coreen tai mihin tahansa muuhun avoimen lähdekoodin projektiin paljastamatta henkilöllisyyttäsi.


Monet kehittäjät valitsevat tämän vaihtoehdon toimimalla salanimellä ja yrittäen pitää sen erillään todellisesta henkilöllisyydestään. Syyt tähän voivat vaihdella kehittäjittäin. Yksi salanimellä toimiva käyttäjä on ZmnSCPxj. Hän osallistuu muiden hankkeiden ohella Bitcoin Coreen ja Core Lightningiin, joka on yksi useista Lightning Network:n toteutuksista. [Hän kirjoittaa](https://zmnscpxj.github.io/about.html) verkkosivullaan:


> Olen ZmnSCPxj, satunnaisesti luotu Internet-henkilö. Pronominini ovat he/him/his.
>

> Ymmärrän, että ihmiset haluavat vaistomaisesti tietää identiteettini. Mielestäni identiteettini on kuitenkin suurelta osin epäolennainen, ja haluan, että minua arvioidaan mieluummin työni perusteella.
>

> Jos mietit, lahjoittaisitko vai et, ja ihmettelet, mitkä ovat elinkustannukseni tai tuloni, ymmärräthän, että oikein puhuen sinun pitäisi lahjoittaa minulle sen perusteella, mikä on mielestäsi hyödyllisyys minun
artikkelit ja työni Bitcoin:n ja Lightning Network:n parissa.


Hänen tapauksessaan salanimen käytön syytä on arvioitava hänen ansioidensa perusteella eikä sen perusteella, kuka tai ketkä ovat salanimen takana. Mielenkiintoista on, että hän paljasti [CoinDeskin artikkelissa] (https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/), että salanimi luotiin eri syystä.


> Alkuperäinen syyni [salanimen käyttöön] oli yksinkertaisesti se, että olin huolissani [siitä], että tekisin suuren virheen; siksi ZmnSCPxj oli alun perin tarkoitettu kertakäyttöiseksi salanimeksi, josta voitaisiin luopua tällaisessa tapauksessa. Se näyttää kuitenkin saaneen enimmäkseen myönteistä mainetta, joten olen säilyttänyt sen

Salanimellä voit todellakin puhua vapaammin vaarantamatta henkilökohtaista mainettasi, jos sanot jotain tyhmää tai teet suuren virheen. Kuten kävi ilmi, hänen salanimensä sai erittäin hyvän maineen ja vuonna 2019 [hän sai jopa kehitysapurahan](https://twitter.com/spiralbtc/status/1204815615678177280), mikä on jo itsessään osoitus Bitcoin:n luvattomasta luonteesta.


Bitcoin:n tunnetuin salanimi on Satoshi Nakamoto. On epäselvää, miksi hän valitsi salanimen, mutta jälkikäteen ajateltuna se oli luultavasti hyvä päätös useista syistä:


- Koska monet ihmiset arvelevat, että Nakamoto omistaa paljon Bitcoin:ää, hänen taloudellisen ja henkilökohtaisen turvallisuutensa kannalta on välttämätöntä pitää henkilöllisyytensä tuntemattomana.
- Koska hänen henkilöllisyyttään ei tiedetä, ketään ei voida asettaa syytteeseen, mikä antaa eri viranomaisille Hard-aikaa.
- Ei ole arvovaltaista henkilöä, jota voisi ihailla, mikä tekee Bitcoin:sta meritokraattisemman ja vastustuskykyisemmän kiristystä vastaan.


Huomaa, että nämä seikat eivät koske vain Satoshi Nakamotoa, vaan kaikkia, jotka työskentelevät Bitcoin:n parissa tai joilla on hallussaan merkittäviä määriä valuuttaa, vaihtelevassa määrin.


### Valinnan salaus


Avoimen lähdekoodin kehittäjät käyttävät usein muiden kehittämiä avoimen lähdekoodin kirjastoja. Tämä on luonnollinen ja mahtava osa mitä tahansa tervettä ekosysteemiä. Bitcoin-ohjelmistoissa on kuitenkin kyse oikeasta rahasta, ja tämän vuoksi kehittäjien on oltava erityisen varovaisia valitessaan, mistä kolmansien osapuolten kirjastoista ne ovat riippuvaisia.


Filosofisessa [kryptografiaa käsittelevässä puheessa] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/) Gregory Maxwell haluaa määritellä uudelleen termin "kryptografia", joka on hänen mielestään liian suppea. Hän selittää, että pohjimmiltaan *tieto haluaa olla vapaata*, ja määrittelee kryptografian määritelmän sen perusteella:


> Kryptografia on taidetta ja tiedettä, jota käytämme taistellaksemme tiedon perusluonnetta vastaan, taivuttaaksemme sitä poliittisen ja moraalisen tahtomme mukaan ja ohjataksemme sitä inhimillisiin päämääriin vastoin kaikkia mahdollisuuksia ja pyrkimyksiä vastustaa sitä.

Sitten hän esittelee termin *valintakryptografia*, jota kutsutaan kryptografisten työkalujen valinnan taidoksi, ja selittää, miksi se on tärkeä osa kryptografiaa. Se pyörii sen ympärillä, miten valita kryptografisia kirjastoja, työkaluja ja käytäntöjä, tai kuten hän sanoo "kryptosysteemien valinnan kryptosysteemi".


Konkreettisten esimerkkien avulla hän osoittaa, miten valintakryptografia voi helposti mennä pahasti pieleen, ja ehdottaa myös luetteloa kysymyksistä, joita voit kysyä itseltäsi, kun harjoitat sitä. Alla on tiivistetty versio tästä luettelosta:


- Onko ohjelmisto tarkoitettu käyttötarkoituksiisi?
- Otetaanko kryptografiset näkökohdat vakavasti?
- Mikä on tarkistusprosessi? Onko sellainen olemassa?
- Mikä on kirjoittajien kokemus?
- Onko ohjelmisto dokumentoitu?
- Onko ohjelmisto siirrettävissä?
- Onko ohjelmisto testattu?
- Otetaanko ohjelmistossa käyttöön parhaat käytännöt?


Vaikka tämä ei olekaan lopullinen opas menestykseen, voi olla erittäin hyödyllistä käydä nämä kohdat läpi, kun teet valintasalausta.


Maxwellin edellä mainitsemien ongelmien vuoksi Bitcoin Core pyrkii todella Hard [minimoimaan altistumisensa kolmansien osapuolten kirjastoille] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Kaikkia ulkoisia riippuvuuksia ei tietenkään voi poistaa, koska muuten kaikki olisi kirjoitettava itse, fonttien renderöinnistä järjestelmäkutsujen toteutukseen.


### Arvostelu



Tämä osio on nimetty "Review" eikä "Code review", koska Bitcoin:n tietoturva perustuu vahvasti monitasoiseen tarkasteluun, ei vain lähdekoodin tarkasteluun. Lisäksi erilaiset ideat vaativat tarkistusta eri tasoilla: konsensussäännön muutos vaatisi perusteellisemman tarkistuksen useammalla tasolla verrattuna värimaailman muutokseen tai kirjoitusvirheen korjaukseen.


Matkalla lopulliseen hyväksymiseen idea käy yleensä läpi useita keskustelu- ja tarkasteluvaiheita. Seuraavassa luetellaan joitakin näistä vaiheista:



- Idea on lähetetty Bitcoin-dev-postituslistalle
- Ajatus on virallistettu Bitcoin:n parannusehdotukseksi (BIP)
- Rajatarkastus on toteutettu vetopyynnössä (PR) Bitcoin Coreen
- Käyttöönottomekanismeista keskustellaan
- Joitakin kilpailevia käyttöönottomekanismeja on toteutettu Bitcoin Core -ohjelman vetopyynnöissä
- Pull-pyynnöt yhdistetään master-haaraan
- Käyttäjät valitsevat, käyttävätkö he ohjelmistoa vai eivät


Jokaisessa vaiheessa eri näkökulmista ja taustoista tulevat henkilöt tarkastelevat saatavilla olevaa tietoa, olipa kyseessä sitten lähdekoodi, BIP tai vain väljästi kuvattu idea. Vaiheita ei yleensä suoriteta tiukasti ylhäältä alaspäin, vaan useita vaiheita voi tapahtua samanaikaisesti, ja joskus niiden välillä siirrytään edestakaisin. Eri henkilöt voivat myös antaa palautetta eri vaiheiden aikana.


Yksi Bitcoin Coren tuotteliaimmista koodin tarkistajista on Jon Atack. Hän kirjoitti [blogikirjoituksen](https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) siitä, miten Bitcoin Coreen voi tarkistaa vetoomuksia. Hän korostaa, että hyvä koodin tarkastaja keskittyy siihen, miten hän voi parhaiten lisätä arvoa.


> Uutena tulokkaana tavoitteena on pyrkiä tuomaan lisäarvoa ystävällisesti ja nöyrästi ja samalla oppia mahdollisimman paljon.
>

> Hyvä lähestymistapa on, että et keskity itseesi, vaan kysyt pikemminkin: "Miten voin palvella parhaiten?"

Hän korostaa, että tarkastelu on todella rajoittava tekijä Bitcoin Core -ohjelmassa. Monet hyvät ideat jäävät jumiin limboon, jossa niitä ei tarkisteta, odottamaan. Huomaa, että tarkistaminen ei ole vain hyödyllistä Bitcoin:lle, vaan se on myös loistava tapa oppia ohjelmistosta ja samalla tuottaa sille lisäarvoa. Atackin nyrkkisääntö on tarkistaa 5-15 PR:ää, ennen kuin tekee oman PR:n. Tässäkin tapauksessa sinun tulisi keskittyä siihen, miten voit parhaiten palvella yhteisöä, ei siihen, miten saat oman koodisi yhdistettyä. Tämän lisäksi hän painottaa, että on tärkeää tehdä tarkastelu oikealla tasolla: onko nyt aika tarkastella pikkujuttuja ja kirjoitusvirheitä vai tarvitseeko kehittäjä enemmän käsitteellistä tarkastelua? Jon Attack lisää:


> Hyödyllinen ensimmäinen kysymys tarkastelun alussa voi olla: "Mitä tässä tarvitaan eniten tällä hetkellä?" Tähän kysymykseen vastaaminen edellyttää kokemusta ja kertynyttä kontekstia, mutta se on hyödyllinen kysymys, kun päätetään, miten voidaan tuottaa eniten lisäarvoa vähimmällä ajalla.

Postauksen toinen puoli koostuu hyödyllisistä käytännön teknisistä ohjeista, jotka koskevat tarkistuksen tekemistä, ja sisältää linkkejä tärkeisiin dokumentteihin, joista voit lukea lisää.


Bitcoin Core -kehittäjä ja koodin tarkastaja Gloria Zhao on kirjoittanut [artikkelin] (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md), joka sisältää kysymyksiä, joita hän yleensä esittää itselleen tarkistuksen aikana. Hän kertoo myös, mitä hän pitää hyvänä arvosteluna:


> Minusta hyvä arvostelu on sellainen, jossa olen esittänyt itselleni paljon kärkeviä kysymyksiä PR:stä ja ollut tyytyväinen vastauksiin
heille. [...] Aloitan luonnollisesti käsitteellisillä kysymyksillä, sitten lähestymistapaan liittyvillä kysymyksillä ja sitten täytäntöönpanokysymyksillä. Yleisesti ottaen olen itse sitä mieltä, että on hyödytöntä jättää C++-syntaksiin liittyviä kommentteja PR-luonnokseen, ja minusta tuntuisi epäkohteliäältä palata kysymykseen "onko tässä järkeä" sen jälkeen, kun kirjoittaja on käsitellyt yli 20 ehdotustani koodin organisointiin.


Hänen ajatuksensa siitä, että hyvässä arvioinnissa olisi keskityttävä siihen, mitä tarvitaan eniten tiettynä ajankohtana, vastaa hyvin Jon Atackin neuvoja. Hän

ehdottaa luetteloa kysymyksistä, joita voitte esittää itsellenne arviointiprosessin eri vaiheissa, mutta korostaa, että luettelo ei ole mitenkään tyhjentävä eikä suoraviivainen resepti. Luetteloa havainnollistetaan tosielämän esimerkeillä GitHubista.


### Rahoitus



Monet ihmiset työskentelevät Bitcoin:n avoimen lähdekoodin kehittämisen parissa, joko Bitcoin Core -ohjelmiston tai muiden projektien parissa. Monet tekevät sitä vapaa-ajallaan saamatta mitään korvausta, mutta jotkut kehittäjät saavat siitä myös palkkaa.


Yritykset, yksityishenkilöt ja organisaatiot, jotka ovat kiinnostuneita Bitcoin:n jatkuvasta menestyksestä, voivat lahjoittaa varoja kehittäjille joko suoraan tai organisaatioiden kautta, jotka puolestaan jakavat varat yksittäisille kehittäjille. On myös useita Bitcoin:een keskittyviä yrityksiä, jotka palkkaavat ammattitaitoisia kehittäjiä ja antavat heidän työskennellä kokopäiväisesti Bitcoin:n parissa.


### Kulttuurishokki



Ihmiset saavat joskus sen käsityksen, että Bitcoin:n kehittäjät käyvät paljon sisäisiä taisteluita ja loputtomia kiivaita keskusteluja ja että he ovat kyvyttömiä tekemään päätöksiä.


Esimerkiksi Taproot:n käyttöönottomekanismista keskusteltiin pitkään, ja sen aikana muodostui kaksi "leiriä". Toinen halusi "epäonnistua" päivityksessä, jos kaivostyöläiset eivät olisi äänestäneet ylivoimaisesti uusien sääntöjen puolesta tietyn hetken jälkeen, kun taas toinen halusi panna säännöt täytäntöön tuon hetken jälkeen kaikesta huolimatta. Michael Folkson tiivistää näiden kahden leirin argumentit Bitcoin-dev-postituslistalle lähettämässään [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) kirjeessä.


Keskustelu jatkui näennäisesti ikuisuuden, ja oli todella Hard, eikä asiasta ollut odotettavissa yhteisymmärrystä lähiaikoina. Tämä sai ihmiset turhautumaan, ja sen seurauksena kuumuus kiihtyi. Gregory Maxwell (käyttäjänä nullc) pelkäsi [Redditissä](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3), että pitkät keskustelut tekisivät päivityksestä vähemmän turvallisen:


> Tässä vaiheessa ylimääräinen odottelu ei lisää tarkastelua ja varmuutta. Sen sijaan lisäviiveet heikentävät inertiaa ja mahdollisesti lisäävät riskiä jonkin verran, kun ihmiset alkavat unohtaa yksityiskohtia, lykkäävät jatkokäyttöön liittyviä töitä (kuten Wallet-tukea) ja eivät investoi niin paljon ylimääräistä tarkistustyötä kuin he investoisivat, jos he olisivat varmoja aktivointiaikataulusta.

Lopulta tämä kiista saatiin ratkaistua David Hardingin ja Russel O'Connorin uuden ehdotuksen nimeltä Speedy Trial ansiosta, joka sisälsi verrattain lyhyemmän signaalin antamisen kaivosmiehille lukita Taproot:n aktivointi tai epäonnistua nopeasti. Jos he aktivoivat sen tuon ajanjakson aikana, Taproot otettaisiin käyttöön noin 6 kuukautta myöhemmin.


Joku, joka ei ole tottunut Bitcoin:n kehitysprosessiin, luultavasti ajattelisi, että nämä kiihkeät keskustelut näyttävät hirvittävän huonoilta ja jopa myrkyllisiltä. On ainakin kaksi tekijää, jotka saavat ne joidenkin mielestä näyttämään pahalta:



- Suljetun lähdekoodin yrityksiin verrattuna kaikki keskustelut käydään avoimesti, muokkaamattomina. Googlen kaltainen ohjelmistoyritys ei koskaan antaisi työntekijöidensä keskustella avoimesti ehdotetuista ominaisuuksista, vaan se julkaisisi korkeintaan lausunnon yrityksen kannasta asiaan. Tämä saa yritykset näyttämään harmonisemmilta Bitcoin:een verrattuna.
- Koska Bitcoin on luvaton, kuka tahansa saa ilmaista mielipiteensä. Tämä eroaa olennaisesti suljetun lähdekoodin yrityksistä, joissa on kourallinen ihmisiä, joilla on mielipide, yleensä samanhenkisiä ihmisiä. Bitcoin:ssa ilmaistujen mielipiteiden paljous on yksinkertaisesti huikea verrattuna esimerkiksi PayPaliin.


Useimmat Bitcoin-kehittäjät väittävät, että tämä avoimuus luo hyvän ja terveen ympäristön ja että se on jopa välttämätöntä parhaan lopputuloksen saavuttamiseksi.


Kuten luvussa Uhka vihjattiin, toinen edellä oleva kohta voi olla erittäin hyödyllinen, mutta sillä on myös haittapuolensa. Hyökkääjä voi käyttää viivytystaktiikoita, kuten [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184) -julkaisussa esitettyjä, vääristääkseen päätöksenteko- ja kehitysprosessia.


Toinen mainitsemisen arvoinen asia on se, että koska Bitcoin on rahaa ja Bitcoin Core turvaa käsittämättömiä rahamääriä, turvallisuuteen ei tässä yhteydessä suhtauduta kevyesti. Siksi kokenut Bitcoin Core

kehittäjät saattavat vaikuttaa hyvin Hard-päiseviltä, mikä asenne on yleensä perusteltu. Ominaisuutta, jolla on heikko perustelu, ei hyväksytä. Sama tapahtuisi, jos se rikkoisi

jäljitettävissä olevia rakennuksia, lisätty uusia riippuvuuksia tai jos koodi ei noudattanut Bitcoin:n [parhaita käytäntöjä] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Tämä voi turhauttaa uusia (ja vanhoja) kehittäjiä. Mutta kuten avoimen lähdekoodin ohjelmistoissa on tapana, voit aina käyttää Fork-tietovarastoa, yhdistää haluamasi omaan Fork:ään ja rakentaa ja ajaa oman binäärisi.


### Johtopäätös avoimesta lähdekoodista


Bitcoin Core ja useimmat muut Bitcoin-ohjelmistot ovat avoimen lähdekoodin ohjelmistoja, mikä tarkoittaa, että kuka tahansa voi vapaasti levittää, muokata ja käyttää ohjelmistoa haluamallaan tavalla. Bitcoin Core -tietovarasto GitHubissa on tällä hetkellä Bitcoin:n kehityksen keskipiste, mutta tämä asema voi muuttua, jos ihmiset alkavat epäillä sen ylläpitäjiä tai sivustoa itseään.


Avoimen lähdekoodin ansiosta Bitcoin:n sisällä ja sen päällä voidaan kehittää ilman lupia. Kirjoititpa sitten koodia, tarkistit koodia tai pöytäkirjoja; avoin lähdekoodi mahdollistaa sen, että voit tehdä sen, pseudonomisesti tai ei.


Bitcoin:n kehitysprosessi on radikaalisti avoin, mikä voi saada Bitcoin:n näyttämään myrkylliseltä ja tehottomalta paikalta, mutta juuri se pitää Bitcoin:n joustavana pahansuovia toimijoita vastaan.


## Skaalaus

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



Tässä luvussa selvitetään, miten Bitcoin skaalautuu ja miten ei. Aloitamme tarkastelemalla, miten ihmiset ovat aiemmin pohtineet skaalautumista. Sitten suurin osa tästä luvusta selittää erilaisia lähestymistapoja Bitcoin:n skaalaamiseen, erityisesti vertikaalista, horisontaalista, sisäänpäin suuntautuvaa ja kerroksittaista skaalaamista. Kunkin kuvauksen jälkeen pohditaan, onko lähestymistapa ristiriidassa Bitcoin:n arvolupauksen kanssa.


Bitcoin-alueella eri ihmiset määrittelevät sanan "asteikko" eri tavoin. Jotkut käsittävät sen Blockchain:n transaktiokapasiteetin kasvattamisena, toiset uskovat sen tarkoittavan Blockchain:n tehokkaampaa käyttöä ja toiset taas Bitcoin:n päälle kehitettävien järjestelmien kehittämistä.


Bitcoin:n yhteydessä ja tämän kirjan tarkoituksia varten määrittelemme skaalautumisen * Bitcoin:n käyttökapasiteetin kasvattamiseksi vaarantamatta sen sensuurinsietokykyä*. Tämä määritelmä kattaa useita

esimerkiksi erilaisia muutoksia:


- Transaktiosyötteiden käyttäminen vähemmän tavuja
- Allekirjoitusten tarkastuksen suorituskyvyn parantaminen
- Vertaisverkon käyttö pienentää kaistanleveyttä
- Tapahtumien eräajot
- Kerroksellinen arkkitehtuuri


Tutustumme pian erilaisiin lähestymistapoihin skaalautumiseen, mutta aloitetaan lyhyellä katsauksella Bitcoin:n historiaan skaalautumisen yhteydessä.


### Skaalautumisen historia



Skaalaus on ollut keskeinen keskustelunaihe Bitcoin:n Genesis:stä lähtien. Aivan ensimmäinen lause [aivan ensimmäisessä sähköpostiviestissä](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) vastauksena Satoshi:n ilmoitukseen Bitcoin:n whitepaperista Cryptography-postituslistalla koski todellakin skaalautumista:


> Satoshi Nakamoto kirjoitti:
>

> "Olen työskennellyt uuden sähköisen käteisrahajärjestelmän parissa, joka on täysin vertaisverkkopohjainen, ilman luotettavaa kolmatta osapuolta.  Julkaisu on saatavilla osoitteessa http://www.Bitcoin.org/Bitcoin.pdf"
>

> Tarvitsemme erittäin, erittäin paljon tällaista järjestelmää, mutta ymmärtääkseni ehdotuksenne ei näytä skaalautuvan tarvittavaan kokoon.

Keskustelu sinänsä ei ehkä ole kovin mielenkiintoinen eikä tarkka, mutta se osoittaa, että skaalautuminen on ollut huolenaiheena alusta alkaen.


Skaalauskeskustelut saavuttivat suurimman kiinnostuksensa vuosien 2015-2017 tienoilla, jolloin oli liikkeellä monia erilaisia ideoita siitä, pitäisikö lohkokoon enimmäisrajaa kasvattaa ja miten. Kyseessä oli melko epäkiinnostava keskustelu lähdekoodin parametrin muuttamisesta, muutos, joka ei pohjimmiltaan ratkaissut mitään, mutta siirsi skaalautumisongelmaa pidemmälle tulevaisuuteen ja kasvatti teknistä velkaa.


Vuonna 2015 Montrealissa järjestettiin konferenssi nimeltä [Scaling Bitcoin] (https://scalingbitcoin.org/), jonka seurantakonferenssi pidettiin kuusi kuukautta myöhemmin Hongkongissa ja sen jälkeen useissa muissa paikoissa ympäri maailmaa. Konferenssissa keskityttiin nimenomaan Address:n skaalaamiseen. Monet Bitcoin:n kehittäjät ja muut harrastajat kokoontuivat näihin konferensseihin keskustelemaan erilaisista skaalauskysymyksistä ja -ehdotuksista. Useimmat näistä keskusteluista eivät pyörineet lohkokoon kasvattamisen ympärillä vaan pitkän aikavälin ratkaisujen ympärillä.


Hongkongin konferenssin jälkeen joulukuussa 2015 Gregory Maxwell [tiivisti näkemyksensä](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) monista keskustelunaiheista ja aloitti yleisestä skaalausfilosofiasta:


> Käytettävissä olevalla teknologialla on perustavanlaatuisia kompromisseja mittakaavan ja hajauttamisen välillä. Jos järjestelmä on liian kallis, ihmisten on pakko luottaa kolmansiin osapuoliin sen sijaan, että he panisivat itsenäisesti täytäntöön järjestelmän säännöt. Jos Bitcoin Blockchain:n resurssien käyttö suhteessa käytettävissä olevaan tekniikkaan on liian suurta, Bitcoin menettää kilpailuetujaan vanhoihin järjestelmiin verrattuna, koska validointi on liian kallista (hinnoittelemalla monet käyttäjät pois), mikä pakottaa luottamuksen takaisin järjestelmään.  Jos kapasiteetti on liian pieni ja transaktiomenetelmämme liian tehottomia, ketjun käyttö riidanratkaisua varten on liian kallista, mikä taas pakottaa luottamuksen takaisin järjestelmään.

Hän puhuu läpimenon ja hajauttamisen välisestä kompromissista. Jos sallitaan isommat lohkot, jotkut ihmiset joutuvat poistumaan verkosta, koska heillä ei ole enää resursseja lohkojen validointiin. Mutta toisaalta, jos lohkotilan käyttö kallistuu, yhä harvemmilla on varaa käyttää sitä riitojenratkaisumekanismina. Kummassakin tapauksessa käyttäjiä työnnetään kohti luotettavia palveluita.


Hän jatkaa tekemällä yhteenvedon konferenssissa esitellyistä monista skaalautumiseen liittyvistä lähestymistavoista. Niitä ovat muun muassa laskennallisesti tehokkaammat allekirjoitusten todentamiset, *segregoitu todistaja*, mukaan lukien lohkokokorajojen muutos, tilatehokkaampi lohkojen etenemismekanismi ja protokollien rakentaminen Bitcoin:n päälle kerroksittain. Monet näistä

lähestymistapoja on sittemmin toteutettu.


### Skaalauslähestymistavat



Kuten edellä vihjattiin, Bitcoin:n skaalaamisen ei välttämättä tarvitse tarkoittaa lohkokokorajoituksen tai muiden rajoitusten lisäämistä. Käymme nyt läpi joitakin yleisiä lähestymistapoja skaalautumiseen, joista osa ei kärsi edellisessä jaksossa mainitusta läpäisykyvyn ja hajautuksen välisestä kompromissista.


#### Pystysuora skaalaus



Vertikaalinen skaalautuminen tarkoittaa tietojenkäsittelykoneiden laskentaresurssien lisäämistä. Bitcoin:n yhteydessä nämä jälkimmäiset ovat täydellisiä solmuja eli koneita, jotka validoivat Blockchain:n käyttäjiensä puolesta.


Bitcoin:ssä yleisimmin käsitelty vertikaalisen skaalauksen tekniikka on lohkokokorajoituksen kasvattaminen. Tämä edellyttäisi, että joidenkin solmujen olisi päivitettävä laitteistonsa, jotta ne pysyisivät kasvavien laskentavaatimusten tasalla. Huonona puolena on, että se tapahtuu keskittämisen kustannuksella.


Full node:n hajauttamiseen kohdistuvien kielteisten vaikutusten lisäksi vertikaalinen skaalautuminen saattaa vaikuttaa kielteisesti Bitcoin:n Mining hajauttamiseen ja turvallisuuteen myös vähemmän ilmeisillä tavoilla. Katsotaanpa, miten louhijoiden "pitäisi" toimia. Sanotaan, että Miner louhii lohkon korkeudella 7 ja julkaisee kyseisen lohkon Bitcoin-verkossa. Kestää jonkin aikaa, ennen kuin tämä lohko saavuttaa laajan hyväksynnän, mikä johtuu pääasiassa kahdesta tekijästä:


- Lohkon siirtäminen vertaisverkon välillä vie aikaa kaistanleveysrajoitusten vuoksi.
- Lohkon validointi vie aikaa.


Kun lohko 7 leviää verkossa, monet louhijat ovat edelleen Mining lohkon 6 päällä, koska he eivät ole vielä saaneet ja vahvistaneet lohkoa 7. Tänä aikana, jos joku näistä louhijoista löytää uuden lohkon korkeudella 7, kyseisellä korkeudella on kaksi kilpailevaa lohkoa. Korkeudella 7 (tai millä tahansa muulla korkeudella) voi olla vain yksi lohko, mikä tarkoittaa, että jommankumman ehdokkaista on vanhentunut.


Lyhyesti sanottuna vanhentuneita lohkoja syntyy, koska jokaisen lohkon eteneminen vie aikaa, ja mitä kauemmin eteneminen kestää, sitä suurempi on vanhentuneiden lohkojen todennäköisyys.


Oletetaan, että lohkokokorajoitus poistetaan ja että keskimääräinen lohkokoko kasvaa huomattavasti. Tällöin lohkojen eteneminen verkossa hidastuisi kaistanleveysrajoitusten ja verifiointiajan vuoksi. Levitysajan piteneminen lisää myös vanhentuneiden lohkojen todennäköisyyttä.


Louhijat eivät pidä siitä, että heidän lohkonsa pysähtyvät, koska he menettävät Block reward:nsa, joten he tekevät kaikkensa välttääkseen tämän

skenaario. Toimenpiteisiin, joihin ne voivat ryhtyä, kuuluvat:



- Saapuvan lohkon validoinnin lykkääminen, joka tunnetaan myös nimellä *validoiva Mining*. Louhijat voivat vain tarkistaa lohkon otsikon Proof-of-Work:n ja louhia sen perusteella, kun he sillä välin lataavat koko lohkon ja validoivat sen.
- Yhdistäminen Mining pool:ään, jolla on suurempi kaistanleveys ja yhteydet.


Validoimaton Mining heikentää entisestään Full node:n hajauttamista, koska Miner luottaa saapuviin lohkoihin ainakin väliaikaisesti. Se haittaa myös jossain määrin turvallisuutta, koska osa verkon laskentatehosta rakentaa mahdollisesti virheellisen Blockchain:n varaan sen sijaan, että se rakentaisi vahvimman ja pätevän ketjun varaan.


Toisella luetelmakohdalla on kielteinen vaikutus Miner:n hajauttamiseen, sillä yleensä poolit, joilla on parhaat verkkoyhteydet ja kaistanleveys, ovat myös suurimpia, mikä saa kaivostyöntekijät suuntautumaan muutamiin suuriin pooleihin.


#### Vaakasuora skaalaus



Horisontaalisella skaalauksella tarkoitetaan tekniikoita, joilla työmäärä jaetaan useille koneille. Vaikka tämä on yleinen skaalausmenetelmä suosituilla verkkosivustoilla ja tietokannoissa, sitä ei ole helppo toteuttaa Bitcoin:ssä.


Monet kutsuvat tätä Bitcoin-skaalausmenetelmää *shardingiksi*. Periaatteessa siinä annetaan kunkin Full node:n tarkistaa vain osa Blockchain:sta. Peter Todd on miettinyt paljon sharding-käsitettä. Hän kirjoitti [blogikirjoituksen] (https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard), jossa hän selittää shardausta yleisesti ja esittelee myös oman ideansa nimeltä *treechains*. Artikkeli on vaikealukuinen, mutta Todd esittää joitakin kohtia, jotka ovat varsin sulavia:


> Varjostetuissa järjestelmissä "Full node-puolustus" ei toimi, ainakaan suoraan. Kyse on siitä, että kaikilla ei ole kaikkia tietoja, joten on päätettävä, mitä tapahtuu, kun niitä ei ole saatavilla.

Sitten hän esittelee erilaisia ideoita siitä, miten shardaus eli horisontaalinen skaalautuminen voidaan toteuttaa. Postauksen loppupuolella hän toteaa:


> On kuitenkin suuri ongelma: pyhä !@#$ on edellä mainittu kompleksi verrattuna Bitcoin:een! Jopa shardauksen "lapsiversio" - minun linearisointisuunnitelmani zk-SNARKSin sijasta - on luultavasti yhden tai kaksi kertaluokkaa monimutkaisempi kuin Bitcoin-protokollan käyttäminen tällä hetkellä, mutta silti tällä hetkellä valtava osa tämän alan yrityksistä näyttää nostaneen kätensä pystyyn ja käyttävän sen sijaan keskitettyjä API-palveluntarjoajia. Edellä esitetyn toteuttaminen ja sen saaminen loppukäyttäjien käyttöön ei ole helppoa.
>

> Toisaalta hajauttaminen ei ole halpaa: PayPalin käyttäminen on suuruusluokkaa yksinkertaisempaa kuin Bitcoin-protokollan käyttäminen.

Hänen johtopäätöksensä on, että jakaminen *voi* olla teknisesti mahdollista, mutta se olisi valtavan monimutkaista. Kun otetaan huomioon, että monet käyttäjät pitävät Bitcoin jo nyt liian monimutkaisena ja käyttävät sen sijaan mieluummin keskitettyjä palveluita, on Hard:n tehtävä vakuuttaa heidät käyttämään jotain vielä monimutkaisempaa.


#### Sisäinen skaalautuminen



Vaikka horisontaalinen ja vertikaalinen skaalautuminen on historiallisesti toiminut hyvin keskitetyissä järjestelmissä, kuten tietokannoissa ja verkkopalvelimissa, ne eivät näytä soveltuvan Bitcoin:n kaltaiseen hajautettuun verkkoon niiden keskittämisvaikutusten vuoksi.


Aivan liian vähän arvostusta saa lähestymistapa, jota voidaan kutsua *sisäiseksi skaalautumiseksi*, mikä tarkoittaa "tee enemmän vähemmällä". Se viittaa siihen jatkuvaan työhön, jota monet kehittäjät tekevät jatkuvasti optimoidakseen jo käytössä olevia algoritmeja, jotta voimme tehdä enemmän järjestelmän nykyisissä rajoissa.


Sisäisen skaalauksen avulla saavutetut parannukset ovat vähintäänkin vaikuttavia. Jotta saisit yleiskuvan vuosien varrella tapahtuneista parannuksista, Jameson Lopp [on suorittanut Blockchain:n synkronointia koskevia vertailuarvotestejä](https://blog.lopp.net/Bitcoin-core-performance-evolution/), joissa verrataan Bitcoin Coren monia eri versioita aina versiosta 0.8 asti.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Bitcoin Core -ydinjärjestelmän eri versioiden alustava lohkolataussuoritus. Y-akselilla on synkronoidun lohkon korkeus ja X-akselilla aika, joka kului synkronointiin kyseiseen korkeuteen


Eri rivit edustavat Bitcoin Core -ohjelman eri versioita. Vasemmanpuoleisin rivi on uusin eli versio 0.22, joka julkaistiin syyskuussa 2021 ja jonka täydellinen synkronointi kesti 396 minuuttia. Oikeanpuoleisin on marraskuussa 2013 julkaistu versio 0.8, joka kesti 3452 minuuttia. Kaikki tämä noin 10-kertainen parannus johtuu sisäänpäin skaalautumisesta.


Parannukset voidaan luokitella joko tilan (RAM-muisti, levy, kaistanleveys jne.) tai laskentatehon säästämiseen. Molemmat luokat vaikuttavat osaltaan yllä olevassa kaaviossa esitettyihin parannuksiin.


Hyvä esimerkki laskennallisesta parannuksesta on [libsecp256k1](https://github.com/Bitcoin-core/secp256k1) -kirjasto, joka muun muassa toteuttaa digitaalisten allekirjoitusten laatimiseen ja tarkistamiseen tarvittavat kryptografiset alkeet. Pieter Wuille on yksi tämän kirjaston tekijöistä, ja hän kirjoitti [Twitter-ketjun](https://twitter.com/pwuille/status/1450471673321381896), jossa esitellään eri pull request -pyynnöillä saavutettuja suorituskyvyn parannuksia.


![](assets/libsecp256k1speedups.webp)


Allekirjoitusten tarkastuksen suorituskyky ajan mittaan, ja aikajanalle on merkitty merkittävät vetopyynnöt


Kaaviossa esitetään suuntaus kahdella eri 64-bittisellä suorittimella, jotka ovat ARM ja x86. Suorituskykyero johtuu siitä, että x86-arkkitehtuurissa on enemmän erikoistuneita käskyjä kuin ARM-arkkitehtuurissa, jossa on vähemmän ja yleisempiä käskyjä. Yleinen suuntaus on kuitenkin sama molemmilla arkkitehtuureilla. Huomaa, että Y-akseli on logaritminen, mikä saa parannukset näyttämään vähemmän vaikuttavilta kuin ne todellisuudessa ovat.


On myös useita hyviä esimerkkejä tilaa säästävistä parannuksista, jotka ovat osaltaan parantaneet suorituskykyä. Eräässä

[Medium-blogikirjoitus](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) Taproot:n osuudesta tilan säästämiseen, käyttäjä Murch vertaa, kuinka paljon lohkotilaa 2:3-kynnysarvoinen allekirjoitus vaatisi käyttämällä Taproot:aa eri tavoin ja ilman sitä lainkaan.


![](assets/murch-taproot.webp)


Tilansäästö eri menotyypeille, Taproot ja vanhoille versioille.


2-of-3 Multisig, jossa käytetään natiivia SegWit:ää, vaatisi yhteensä 104,5+43 vB = 147,5 vB, kun taas tilaa säästävin Taproot:n käyttö vaatisi vain 57,5+43 vB = 100,5 vB vakiokäyttötilanteessa. Pahimmillaan ja harvinaisissa tapauksissa, kuten silloin, kun vakiomuotoinen allekirjoittaja ei jostain syystä ole käytettävissä, Taproot käyttäisi 107,5+43 vB = 150,5 vB. Sinun ei tarvitse ymmärtää kaikkia yksityiskohtia, mutta tämän pitäisi antaa sinulle käsitys siitä, miten kehittäjät ajattelevat tilan säästämisestä - jokainen pieni tavu on tärkeä.


Bitcoin-ohjelmiston sisäisen skaalautumisen lisäksi on joitakin tapoja, joilla käyttäjät voivat myös edistää sisäistä skaalautumista. He voivat tehdä liiketoimensa älykkäämmin säästääkseen transaktiomaksuissa ja samalla pienentää Full node-vaatimuksiin liittyvää jalanjälkeään. Kaksi yleisesti käytettyä tekniikkaa, joilla pyritään saavuttamaan tällainen tavoite, ovat transaktioiden yhdistäminen (transaction batching) ja tuotosten yhdistäminen (output consolidation).


Tapahtumien yhdistämisen ideana on yhdistää useita maksuja yhdeksi tapahtumaksi sen sijaan, että tehtäisiin yksi tapahtuma per maksu. Näin voit säästää paljon maksuja ja samalla vähentää lohkotilan kuormitusta.


![](assets/tx-batching.webp)


Maksutapahtumien yhdistäminen yhdistää useita maksuja yhdeksi maksutapahtumaksi ja säästää siten maksuja.


Tuotosten yhdistämisellä tarkoitetaan lohkotilan vähäisen kysynnän kausien hyödyntämistä useiden tuotosten yhdistämiseksi yhdeksi tuotokseksi. Tämä voi vähentää maksukustannuksiasi myöhemmin, kun sinun on suoritettava maksu lohkotilan kysynnän ollessa korkealla.


![](assets/utxo-consolidation.webp)


Lähtöjen konsolidointi: Sulata kolikkosi yhdeksi isoksi kolikoksi, kun maksut ovat alhaiset, jotta säästät myöhemmin maksuja.


Ei ehkä ole ilmeistä, miten tuotannon vakauttaminen edistää sisäistä skaalautumista. Loppujen lopuksi Blockchain-tietojen kokonaismäärä kasvaa jopa hieman tällä menetelmällä. Siitä huolimatta UTXO-joukko eli tietokanta, joka pitää kirjaa siitä, kuka omistaa mitäkin kolikoita, kutistuu, koska kulutat enemmän UTXO:ita kuin luot. Tämä keventää täysien solmujen taakkaa UTXO-sarjojensa ylläpitämisessä.


Valitettavasti nämä kaksi *UTXO-hallintatekniikkaa* voivat kuitenkin olla haitaksi omalle tai maksunsaajien yksityisyydelle. Kun kyseessä on eräajotapahtuma, jokainen maksunsaaja tietää, että kaikki eräajotapahtumat ovat sinulta muille maksunsaajille (paitsi mahdollisesti muutos). UTXO:n konsolidointitapauksessa paljastat, että konsolidoimasi tuotokset kuuluvat samaan Wallet:een. Sinun on siis ehkä tehtävä kompromissi kustannustehokkuuden ja yksityisyyden suojan välillä.


#### Kerroksellinen skaalaus



Vaikuttavin lähestymistapa skaalaamiseen on luultavasti kerrostaminen. Yleinen ajatus kerrostamisen takana on, että protokolla voi suorittaa käyttäjien välisiä maksuja lisäämättä tapahtumia Blockchain:ään.


Kerrosprotokolla alkaa siitä, että kaksi tai useampi henkilö sopii Blockchain:een laitettavasta aloitustapahtumasta, kuten alla olevassa kuvassa on esitetty.


![](assets/scaling-layer.webp)

Tyypillinen Layer 2 -protokolla Bitcoin:n ja Layer 1:n päälle.


Alkutapahtuman luontitapa vaihtelee eri protokollien välillä, mutta yhteistä on, että osallistujat luovat allekirjoittamattoman alkutapahtuman ja joukon esisignoituja rangaistustapahtumia, jotka käyttävät alkutapahtuman tuotoksen eri tavoin. Tämän jälkeen aloitustapahtuma allekirjoitetaan ja julkaistaan Blockchain:lle, ja rangaistustapahtumat voidaan allekirjoittaa ja julkaista väärin käyttäytyvän osapuolen rankaisemiseksi. Tämä kannustaa osallistujia pitämään lupauksensa, jotta protokolla voi toimia Trustless tavalla.


Kun käynnistystapahtuma on käynnistetty Blockchain:ssä, protokolla voi tehdä sen, mitä sen on tarkoitus tehdä. Se voi esimerkiksi suorittaa erittäin nopeita maksuja osallistujien välillä, toteuttaa joitakin yksityisyyden suojaa parantavia tekniikoita tai tehdä kehittyneempiä skriptejä, joita Bitcoin Blockchain ei tue.


Emme kerro yksityiskohtaisesti, miten tietyt protokollat toimivat, mutta kuten edellisestä kuvasta näkyy, Blockchain:ta käytetään harvoin protokollan elinkaaren aikana. Kaikki mehukas toiminta tapahtuu *off-chain*. Olemme nähneet, miten tämä voi olla etu yksityisyyden suojan kannalta, jos se tehdään oikein, mutta se voi olla myös etu skaalautuvuuden kannalta.


Reddit-postauksessa](https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) otsikolla "Matka kuuhun vaatii raketin, jossa on useita vaiheita, tai muuten rakettiyhtälö syö lounaan... Kaikkien pakkaaminen pelleauton tyyliin trebuchetiin ja toivominen onnistumisesta on aivan out." Gregory Maxwell selittää, miksi kerrostaminen on paras mahdollisuutemme saada Bitcoin skaalautumaan suuruusluokkien verran.


Hän korostaa aluksi, että on virheellistä pitää Visaa tai Mastercardia Bitcoin:n tärkeimpinä kilpailijoina, ja korostaa, että lohkojen enimmäiskoon kasvattaminen on huono tapa vastata kyseiseen kilpailuun. Sitten hän puhuu siitä, miten kerroksia käyttämällä voidaan saada aikaan todellista eroa:


> Tarkoittaako tämä, että Bitcoin ei voi olla suuri voittaja maksuteknologiana? Ei, mutta jotta voimme saavuttaa sellaisen kapasiteetin, jota tarvitaan maailman maksutarpeiden tyydyttämiseksi, meidän on työskenneltävä älykkäämmin.
>

> Bitcoin oli alusta alkaen suunniteltu sisällyttämään kerroksia turvallisella tavalla älykkään sopimuksenteko-ominaisuuden avulla (luuletko, että se lisättiin sinne vain siksi, että ihmiset voisivat filosofoida merkityksettömistä "DAO:ista"?). Käytännössä käytämme Bitcoin-järjestelmää erittäin helppokäyttöisenä ja täydellisen luotettavana robottituomarina ja hoidamme suurimman osan asioistamme oikeussalin ulkopuolella - mutta teemme liiketoimia siten, että jos jokin menee pieleen, meillä on kaikki todisteet ja tehdyt sopimukset, joten voimme luottaa siihen, että robottituomioistuin korjaa asian. (Nörttisivupalkki: Jos tämä tuntuu mahdottomalta, lue tämä vanha postaus transaktioiden läpileikkauksesta)
>

> Tämä on mahdollista juuri Bitcoin:n ydinominaisuuksien vuoksi. Sensuroitava tai palautuva perusjärjestelmä ei sovellu kovin hyvin tehokkaan ylemmän Layer:n transaktiokäsittelyn rakentamiseen sen päälle... ja jos taustalla oleva omaisuuserä ei ole kunnossa, ei ole juurikaan järkeä tehdä transaktioita sen kanssa lainkaan.

Vertaus tuomariin on varsin havainnollinen siitä, miten kerrostaminen toimii: tämän tuomarin on oltava lahjomaton eikä hänen mielensä saa koskaan muuttua, muuten Bitcoin:n pohjan Layer:n yläpuolella olevat kerrokset eivät toimi luotettavasti.


Hän jatkaa esittämällä huomautuksen keskitetyistä palveluista. Yleensä ei ole mitään ongelmaa luottaa siihen, että keskitetty palvelin, jolla on vähäpätöinen määrä Bitcoin:ta, saa asiat hoidettua: sekin on kerroksittaista skaalautumista.


Monta vuotta on kulunut siitä, kun Maxwell kirjoitti yllä olevan kappaleen, ja hänen sanansa pitävät edelleen paikkansa. Lightning Network:n menestys osoittaa, että kerrostaminen on todellakin keino lisätä Bitcoin:n hyötyjä.



### Johtopäätös skaalautumisesta



Olemme keskustelleet eri tavoista, joilla Bitcoin:tä voidaan skaalata ja Bitcoin:n käyttökapasiteettia lisätä. Skaalautuminen on ollut huolenaihe Bitcoin:ssä sen alkuvaiheista lähtien.


Nykyään tiedämme, että Bitcoin ei skaalaudu hyvin vertikaalisesti ("osta isompaa laitteistoa") tai horisontaalisesti ("tarkista vain osa tiedoista"), vaan pikemminkin sisäänpäin ("tee enemmän vähemmällä") ja kerroksittain ("rakenna protokollia Bitcoin:n päälle").


## Kun paska osuu tuulettimeen

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin on ihmisten rakentama. Ihmiset kirjoittavat ohjelmiston, ja ihmiset sitten käyttävät tätä ohjelmistoa. Kun tietoturva-aukko tai vakava vika löydetään - onko näiden kahden välillä todella eroa? - sen löytävät aina ihmiset, lihaa ja verta. Tässä luvussa pohditaan, mitä ihmiset tekevät, mitä heidän pitäisi tehdä ja mitä heidän ei pitäisi tehdä, kun paska osuu tuulettimeen. Ensimmäisessä luvussa selitetään termi *vastuullinen paljastaminen*, jolla tarkoitetaan sitä, miten haavoittuvuuden löytäjä voi toimia vastuullisesti ja auttaa minimoimaan haavoittuvuudesta aiheutuvat vahingot. Luvun loppuosassa käydään läpi joitakin vuosien varrella löydetyistä vakavimmista haavoittuvuuksista ja sitä, miten kehittäjät, louhijat ja käyttäjät ovat niitä käsitelleet. Bitcoin:n varhaislapsuudessa asiat eivät olleet yhtä tiukkoja kuin nykyään.


### Vastuullinen tiedonanto



Kuvittele, että löydät Bitcoin Core -ohjelmassa virheen, jonka avulla kuka tahansa voi sammuttaa Bitcoin Core -solmun etänä käyttämällä erityisesti muokattuja verkkoviestejä. Kuvittele, että et ole myöskään pahansuopa ja haluat, että tätä ongelmaa ei käytetä hyväksi. Mitä teet? Jos vaikenet asiasta, joku muu todennäköisesti löytää ongelman, etkä voi olla varma, ettei hän ole pahansuopa.


Kun tietoturvaongelma havaitaan, sen löytäjän tulisi käyttää termiä _responsible disclosure_, jota Bitcoin-kehittäjät käyttävät usein. Termi on [selitetty Wikipediassa](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Laitteistojen ja ohjelmistojen kehittäjät tarvitsevat usein aikaa ja resursseja virheidensä korjaamiseen. Usein juuri eettiset hakkerit löytävät näitä
haavoittuvuudet. Hakkerit ja tietoturvatutkijat ovat sitä mieltä, että heidän yhteiskunnallinen velvollisuutensa on tehdä haavoittuvuudet tunnetuksi. Ongelmien piilottelu voisi aiheuttaa väärän turvallisuuden tunteen. Tämän välttämiseksi osapuolet koordinoivat ja neuvottelevat kohtuullisen ajan haavoittuvuuden korjaamiselle. Riippuen haavoittuvuuden mahdollisesta vaikutuksesta, hätäkorjauksen tai kiertotien kehittämiseen ja soveltamiseen tarvittavasta arvioidusta ajasta ja muista tekijöistä tämä aika voi vaihdella muutamasta päivästä useisiin kuukausiin.


Tämä tarkoittaa, että jos havaitset tietoturvaongelman, sinun on ilmoitettava siitä järjestelmästä vastaavalle tiimille. Mutta mitä tämä tarkoittaa Bitcoin:n yhteydessä? Kukaan ei hallitse Bitcoin:tä, mutta tällä hetkellä Bitcoin:n kehitykselle on olemassa keskipiste, nimittäin [Bitcoin Core Github repository](https://github.com/Bitcoin/Bitcoin). Kyseisen arkiston ylläpitäjät ovat vastuussa siinä olevasta koodista, mutta he eivät ole vastuussa koko järjestelmästä - kukaan ei ole. Yleinen paras käytäntö on kuitenkin lähettää sähköpostia osoitteeseen security@bitcoincore.org.


Anthony Towns yritti vuonna 2017 julkaistussa [sähköpostiketjussa](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) otsikolla "Responsible disclosure of bugs" (vikojen vastuullinen julkistaminen) tehdä yhteenvedon siitä, mitä hän piti nykyisin parhaina käytäntöinä. Hän oli kerännyt syötteitä useista lähteistä ja eri ihmisiltä saadakseen tietoa näkemyksestään aiheesta.




- Haavoittuvuudet tulee ilmoittaa osoitteessa security at bitcoincore.org
- Kriittinen ongelma (jota voidaan hyödyntää välittömästi tai jota jo hyödynnetään ja joka aiheuttaa suurta vahinkoa) käsitellään seuraavasti:
  - julkaistu korjaus ASAP
  - laaja ilmoitus päivitystarpeesta (tai järjestelmien poistamisesta käytöstä)
  - todellisen ongelman mahdollisimman vähäinen paljastaminen hyökkäysten viivyttämiseksi
- Ei-kriittinen haavoittuvuus (koska sen hyödyntäminen on vaikeaa tai kallista) käsitellään seuraavasti:
  - tavanomaisen kehitystyön yhteydessä suoritettu korjaus ja uudelleentarkastelu
  - korjauksen tai kiertoratkaisun backportti master-versiosta nykyiseen julkaistuun versioon
- Kehittäjät pyrkivät varmistamaan, että korjauksen julkaiseminen ei paljasta haavoittuvuuden luonnetta tarjoamalla ehdotetun korjauksen kokeneille kehittäjille, jotka eivät ole saaneet tietoa haavoittuvuudesta, kertomalla heille, että se korjaa haavoittuvuuden, ja pyytämällä heitä tunnistamaan haavoittuvuuden.
- Kehittäjät voivat suositella, että muut Bitcoin-toteutukset ottavat käyttöön haavoittuvuuskorjaukset ennen korjauksen julkaisemista ja laajamittaista käyttöönottoa, jos he voivat tehdä sen paljastamatta haavoittuvuutta; esimerkiksi jos korjauksella on merkittäviä suorituskykyetuja, jotka oikeuttavat sen sisällyttämisen.
- Ennen kuin haavoittuvuus tulee julkiseksi, kehittäjät yleensä suosittelevat ystävällisille Altcoin:n kehittäjille, että he korjaavat sen. Tämä tapahtuu kuitenkin vasta sen jälkeen, kun korjaukset on otettu laajasti käyttöön Bitcoin-verkossa.
- Kehittäjät eivät yleensä ilmoita Altcoin:n kehittäjille, jotka ovat käyttäytyneet vihamielisesti (esim. käyttäneet haavoittuvuuksia hyökätäkseen toisten kimppuun tai rikkoneet kauppasaartoja).
- Bitcoin:n kehittäjät eivät paljasta haavoittuvuuden yksityiskohtia ennen kuin >80 % Bitcoin-solmuista on ottanut korjaukset käyttöön. Haavoittuvuuksien paljastajia kannustetaan ja pyydetään noudattamaan samaa käytäntöä. [1] [6]


Tämä luettelo osoittaa, kuinka varovainen on oltava Bitcoin:n korjauksia julkaistessaan, sillä korjaus itsessään saattaa paljastaa haavoittuvuuden. Neljäs kohta on erityisen mielenkiintoinen, sillä siinä kerrotaan, miten testataan, onko korjaustiedosto naamioitu tarpeeksi hyvin. Jos muutamat todella kokeneet kehittäjät eivät nimittäin huomaa haavoittuvuutta, vaikka tietävät, että paikkaus korjaa sen, muiden on luultavasti todella Hard vaikea löytää sitä.


Tähän sähköpostiviestiin johtaneessa viestiketjussa keskusteltiin siitä, pitäisikö altcoinien ja muiden Bitcoin:n toteutusten haavoittuvuudet paljastaa, milloin ja miten. Tähän ei ole selkeää vastausta. "Hyvien auttaminen" vaikuttaa järkevältä, mutta kuka päättää, keitä he ovat, ja missä kulkee raja? Bryan Bishop [väitti](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html), että altcoinien ja jopa huijauskolikoiden auttaminen puolustautumaan tietoturva-aukkoja vastaan on moraalinen velvollisuus:


> Ei riitä, että Bitcoin:aa ja sen käyttäjiä puolustetaan aktiivisilta uhilta, vaan yleisemminkin on vastuu puolustaa kaikenlaisia käyttäjiä ja erilaisia ohjelmistoja monenlaisilta uhilta kaikissa muodoissaan, vaikka ihmiset käyttäisivätkin typeriä ja turvattomia ohjelmistoja, joita et itse ylläpidä tai joiden kehittämiseen et osallistu tai joita et kannata. Haavoittuvuustiedon käsittely on arkaluonteinen asia, ja saatat saada tietoa, jolla on vakavampia suoria tai epäsuoria vaikutuksia kuin alun perin kuvattiin.

Townin edellä mainittua sähköpostia edelsi myös Gregory Maxwellin [postaus](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html), jossa hän väitti, että tietoturva-aukot voivat olla vakavampia kuin miltä ne näyttävät:


> Olen useaan kertaan nähnyt Hard hyödyntää ongelma osoittautuu vähäpätöiseksi, kun löydät oikean temppu, tai pieni dos ongelma kääntyä meidän paljon vakavampi.
>

> Yksinkertaisia suorituskykyvirheitä, jotka on otettu asiantuntevasti käyttöön, voidaan mahdollisesti käyttää verkon pilkkomiseen - Miner A ja Exchange B menevät yhteen osioon, kaikki muut toiseen... ja kaksinkertaistavat kulutuksen.
>

> Ja niin edelleen.  Vaikka olenkin täysin samaa mieltä siitä, että eri asioita pitäisi ja voidaan käsitellä eri tavoin, asia ei ole aina niin yksiselitteinen. On järkevää käsitellä asioita vakavampina kuin mitä tiedätte niiden olevan.

Vaikka haavoittuvuus vaikuttaisi Hard:ltä hyödynnettävältä, on ehkä parasta olettaa, että se on helposti hyödynnettävissä, mutta et vain ole vielä keksinyt, miten.


Hän mainitsee myös, että "on jokseenkin virheellistä kutsua tätä säiettä joksikin julkistamisesta kertovaksi, tässä säikeessä ei ole kyse julkistamisesta". Julkistaminen on sitä, kun kerrot myyjälle.  Tässä viestiketjussa on kyse julkaisemisesta, ja sillä on aivan eri seuraukset. Julkaiseminen on sitä, kun olet varma, että olet kertonut mahdollisille hyökkääjille". Tämä viimeinen huomio, joka koskee julkistamisen ja julkaisemisen välistä eroa, on tärkeä. Helppo osa on vastuullinen paljastaminen; Hard:n osa on järkevä julkaiseminen.


### Bitcoin:n traumaattinen lapsuus



Bitcoin alkoi yhden miehen projektina (ainakin sen luojan salanimi viittaa siihen), ja Bitcoin:lla ei aluksi ollut juuri mitään arvoa. Sen vuoksi haavoittuvuuksia ja virheiden korjauksia ei käsitelty yhtä tarkasti kuin nykyään.


Bitcoin:n wikissä on [luettelo yhteisistä haavoittuvuuksista ja altistumisista](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE), jotka Bitcoin on käynyt läpi. Tämä osio on pieni katsaus joihinkin Bitcoin:n alkuvuosien tietoturvaongelmiin ja vaaratilanteisiin. Emme käsittele niitä kaikkia, mutta olemme valinneet niistä muutaman, jotka ovat mielestämme erityisen mielenkiintoisia.


#### 2010-07-28: Kenen tahansa kolikoiden tuhlaaminen (CVE-2010-5141)



28. heinäkuuta 2010 ArtForz-niminen henkilö löysi version 0.3.4 bugin, jonka avulla kuka tahansa saattoi ottaa kolikoita keneltä tahansa muulta. ArtForz *vastuullisesti* ilmoitti tästä Satoshi Nakamotolle ja toiselle Bitcoin-kehittäjälle nimeltä Gavin Andresen.


Ongelmana oli, että skriptioperaattori `OP_RETURN` yksinkertaisesti lopettaisi ohjelman suorituksen, joten jos scriptPubKey oli `<pubkey> OP_CHECKSIG` ja scriptSig oli `OP_1 OP_RETURN`, scriptPubKey:ssä olevaa ohjelman osaa ei koskaan suoritettaisi. Ainoa asia, joka tapahtuisi, olisi, että `1` tulisi pinoon ja sitten `OP_RETURN` aiheuttaisi ohjelman poistumisen. Mikä tahansa nollasta poikkeava arvo pinon päällä ohjelman suorittamisen jälkeen tarkoittaa, että menoehto täyttyy. Koska pinon ylin elementti `1` on nollasta poikkeava, meno on OK.


Tämä oli koodi, jolla käsiteltiin "OP_RETURN":


```
case OP_RETURN:
{
pc = pend;
}
break;
```

`pc = pend;` vaikutti siihen, että ohjelman loppuosa ohitettiin, mikä tarkoitti, että scriptPubKey:n lukitusskriptit jätettiin huomiotta. Korjaus koostui `OP_RETURN`:n merkityksen muuttamisesta niin, että se epäonnistui välittömästi.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi teki tämän muutoksen paikallisesti ja rakensi siitä version 0.3.5 sisältävän suoritettavan binäärin. Sitten hän kirjoitti Bitcointalk-foorumilla `\\\*** ALERT \*** Upgrade to 0.3.5 ASAP`, kehottaen käyttäjiä asentamaan tämän binääriversionsa, esittämättä sen lähdekoodia:


> Päivitä 0.3.5:een ASAP!  Korjasimme toteutusvirheen, jonka vuoksi oli mahdollista, että väärät transaktiot voitiin hyväksyä.  Älä hyväksy Bitcoin-tapahtumia maksuksi ennen kuin päivität versioon 0.3.5!

Alkuperäistä viestiä on myöhemmin muokattu, eikä se ole enää saatavilla täydessä muodossaan. Yllä oleva katkelma on [lainausvastauksesta](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Jotkut käyttäjät kokeilivat Satoshi:n binääriversiota, mutta törmäsivät ongelmiin sen kanssa. Pian tämän jälkeen [Satoshi kirjoitti](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> En ole vielä ehtinyt päivittää SVN:ää.  Odota 0.3.6:sta, rakennan sitä parhaillaan.  Voit sammuttaa solmusi sillä välin.

Ja 35 minuuttia myöhemmin [hän kirjoitti](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN on päivitetty versioon 0.3.6.
>

> Lataan 0.3.6:n Windows-version Sourceforgeen nyt, sitten rakennan linuxin uudelleen.

Tässä vaiheessa hän näytti myös päivittäneen alkuperäistä viestiä mainitsemalla 0.3.6:n 0.3.5:n sijaan:


> Päivitä 0.3.6:een ASAP!  Korjasimme toteutusvirheen, jonka vuoksi oli mahdollista, että väärät tapahtumat näytettiin hyväksyttyinä.  Älä hyväksy Bitcoin-tapahtumia maksuksi ennen kuin päivität versioon 0.3.6!
>

> Jos et voi päivittää 0.3.6:een heti, on parasta sammuttaa Bitcoin-solmusi siihen asti.
>

> Myös 0.3.6, nopeampi hashing:
> - midstate-välimuistin optimointi tcatm:n ansiosta
> - Crypto++ ASM SHA-256 kiitos BlackEye:n
> Kokonaisnopeus on 2,4x nopeampi.
>

> Lataa:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Windows- ja Linux-käyttäjät: jos sinulla on 0.3.5, sinun on silti päivitettävä 0.3.6:een.

Huomaa, että ongelman luonnehdinta eroaa ensimmäisestä viestistä: "voitaisiin näyttää hyväksyttynä" vs. "voitaisiin hyväksyä". Ehkä Satoshi vähätteli viestinnässään vian vakavuutta, jotta varsinaiseen ongelmaan ei kiinnitettäisi liikaa huomiota. Joka tapauksessa ihmiset päivittivät version 0.3.6:een ja se toimi odotetusti. Tämä erityinen ongelma ratkaistiin hämmästyttävästi ilman Bitcoin:n tappioita.


Satoshi:n viestissä kuvattiin myös joitakin Mining:n suorituskyvyn optimointeja. On epäselvää, miksi se sisällytettiin kriittiseen tietoturvakorjaukseen, ja on mahdollista, että tarkoituksena oli hämärtää todellinen ongelma. Vaikuttaa kuitenkin todennäköisemmältä, että hän vain julkaisi sen, mikä oli Subversion-arkiston kehityshaaran päässä, ja siihen oli lisätty tietoturvakorjaus.


Tuolloin käyttäjiä ei ollut läheskään niin paljon kuin nykyään, ja Bitcoin:n arvo oli lähellä nollaa. Jos tämä vikavaste toteutettaisiin nykyään, sitä pidettäisiin täydellisenä paskashow'na monesta syystä:



- Satoshi teki korjauksen sisältävän version 0.3.5, joka sisältää vain binääriversion. Korjausta tai koodia ei toimitettu, ehkä toimenpiteenä ongelman hämärtämiseksi.
- 0.3.5 [ei edes toiminut](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- 0.3.6:n korjaus oli itse asiassa Hard Fork.


Toinen kiistanalainen asia on se, onko hyvä vai huono asia, että käyttäjiä pyydettiin sulkemaan solmunsa. Tämä ei olisi mahdollista nykyään, mutta tuohon aikaan monet käyttäjät seurasivat aktiivisesti foorumeilla päivityksiä ja olivat yleensä ajan tasalla. Koska tämä oli mahdollista, se olisi voinut olla järkevää.


#### 2010-08-15 Yhdistetty ulostulon ylivuoto (CVE-2010-5139)



Elokuun 2010 puolivälissä Bitcointalk-foorumin käyttäjä jgarzik, alias Jeff Garzik,

[havaitsi, että](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) tietyssä transaktiossa lohkon 74638 korkeudella oli kaksi epätavallisen suurta tulosta:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> Tässä lohkossa #74638 oleva "arvo pois" on varsin outo:
>

> 92233720368.54277039 BTC?  Onkohan se UINT64_MAX?

Oletettavasti oli virhe, joka aiheutti kahden int64 (ei uint64, kuten Garzik oletti) tulosteen summan ylivuodon negatiiviseen arvoon -0,00997538 BTC. Riippumatta siitä, mikä oli syötteiden summa, tulosteiden "summa" oli pienempi, joten tapahtuma oli tuolloin käytössä olleen koodin mukaan OK.


Tässä tapauksessa vika oli paljastettu ja julkaistu todellisen hyväksikäytön kautta. Valitettava seuraus tästä oli, että oli luotu noin 2x92 miljardia Bitcoin-kolikkoa, mikä laimensi vakavasti tuolloin olemassa olleen noin 3,7 miljoonan Supply-kolikon rahamäärää.


Aiheeseen liittyvässä viestiketjussa [Satoshi kirjoitti](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531), että hän arvostaisi sitä, jos ihmiset lopettaisivat Mining:n (tai *luomisen*, kuten sitä silloin kutsuttiin):


> Auttaisi, jos ihmiset lopettaisivat tuottamisen.  Meidän on luultavasti tehtävä uusi haara nykyisen haaran ympärille, ja mitä vähemmän generate:aa, sitä nopeammin se onnistuu.
>

> Ensimmäinen korjaus on SVN rev 132:ssa.  Sitä ei ole vielä ladattu.  Työnnän ensin pois tieltä joitakin muita muutoksia, ja sitten lataan tämän korjauksen.

Hänen suunnitelmansa oli tehdä Soft Fork, jotta tässä käsitellyn kaltaiset transaktiot olisivat pätemättömiä, mikä tekisi pätemättömiksi lohkot (erityisesti lohko 74638), jotka sisälsivät tällaisia transaktioita. Alle tunti myöhemmin hän teki [korjauksen Subversion-tietokannan versioon 132](https://sourceforge.net/p/Bitcoin/code/132/) ja [kirjoitti foorumille](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) kuvaten, mitä hänen mielestään käyttäjien pitäisi tehdä:


> Korjaus on ladattu SVN rev 132:een!
>

> Toistaiseksi suositellut vaiheet:
> 1) Sammuta.
> 2) Lataa knightmb:n blk-tiedostot.  (korvaa blk0001.dat- ja blkindex.dat-tiedostot)
> 3) Päivitys.
> 4) Sen pitäisi aloittaa alle 74000 lohkolla. Anna sen ladata loput uudelleen.
>

> Jos et halua käyttää knightmb:n tiedostoja, voit vain poistaa blk*.dat-tiedostot, mutta se kuormittaa verkkoa paljon, jos kaikki lataavat koko lohkoindeksin kerralla.
>

> Rakennan julkaisut lähiaikoina.

Hän halusi, että ihmiset voisivat ladata lohkotietoja tietystä käyttäjästä, nimittäin knightmb:stä, joka oli julkaissut Blockchain:nsä sellaisena kuin se oli hänen levykkeellään, tiedostot blkXXXXXX.dat ja blkindex.dat. Syy Blockchain:n datan lataamiseen tällä tavalla, toisin kuin synkronoimalla se alusta alkaen, oli vähentää verkon kaistanleveyden pullonkauloja.


Tähän liittyi suuri varoitus: käyttäjät latasivat tietoja knightmb:stä [Bitcoin-ohjelmisto ei vahvistanut niitä](https://Bitcoin.stackexchange.com/a/113682/69518) käynnistyksen yhteydessä. Tiedosto blkindex.dat sisälsi UTXO:n joukon, ja ohjelmisto hyväksyisi kaikki siinä olevat tiedot ikään kuin se olisi jo tarkistanut ne. knightmb olisi voinut manipuloida tietoja antaakseen itselleen tai kenelle tahansa muulle bitcoineja.


Jälleen kerran ihmiset näyttivät olevan samaa mieltä, ja invalidilohkon ja sen seuraajien kumoaminen onnistui. Louhijat alkoivat työstää lohkon [74637] (https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) uutta seuraajaa, ja lohkon Timestamp:n mukaan lohkon seuraaja ilmestyi kello 23:53 UTC eli noin kuusi tuntia ongelman havaitsemisen jälkeen. Seuraavana päivänä, 16. elokuuta, klo 08:10 lohkon 74689 ympärillä uusi ketju oli ohittanut vanhan ketjun, joten kaikki päivittämättömät solmut liittyivät uudelleen seuraamaan uutta ketjua. Tämä on syvin reorg - 52 lohkoa - Bitcoin:n historiassa.


OP_RETURN-ongelmaan verrattuna tämä ongelma käsiteltiin hieman siistimmin:


- Ei binary-only-korjausjulkaisua
- Julkaistu ohjelmisto toimi tarkoitetulla tavalla
- Ei Hard Fork


Käyttäjiä pyydettiin pysäyttämään Mining myös tämän ongelman aikana. Voimme keskustella siitä, onko tämä hyvä ajatus vai ei, mutta kuvittele, että olet Miner ja olet vakuuttunut siitä, että kaikki huonon lohkon päällä olevat lohkot pyyhkiytyvät lopulta pois syvässä reorgissa: miksi tuhlaisit resursseja Mining:n tuomittuihin lohkoihin?


Saatat myös ajatella, että on hieman epäilyttävää tehdä kuten Nakamoto ehdotti ja ladata Blockchain, mukaan lukien UTXO-sarja, satunnaisen kaverin Hard-asemalta. Jos näin on, olet oikeassa: se on epäilyttävää. Mutta olosuhteisiin nähden tämä hätätilanne oli järkevä ratkaisu.


Tämä tapaus eroaa merkittävästi aiemmasta OP_RETURN-tapauksesta: tätä ongelmaa käytettiin hyväksi luonnossa, joten korjaaminen oli helpompaa. OP_RETURN-tapauksessa korjausta piti hämätä ja antaa julkisia lausuntoja, jotka eivät suoraan paljastaneet, mikä ongelma oli kyseessä.


#### 2013-03-11 DB-lukitusongelma 0.7.2 - 0.8.0 (CVE-2013-3220)



Maaliskuussa 2013 nousi esiin erittäin mielenkiintoinen ja kasvatuksellisesti arvokas asia. Näytti siltä, että Blockchain oli jakautunut (vaikka alla olevassa lainauksessa käytetäänkin sanaa "Fork") lohkon 225429 jälkeen. Tapahtuman yksityiskohdat ilmoitettiin [BIP50:ssä] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). Yhteenvedossa sanotaan:


> Lohko, jossa oli enemmän transaktiosyöttöjä kuin aiemmin oli nähty, louhittiin ja lähetettiin. Bitcoin 0.8:n solmut pystyivät käsittelemään tämän, mutta jotkut ennen 0.8:aa olevat Bitcoin:n solmut hylkäsivät sen, mikä aiheutti odottamattoman Fork:n Blockchain:n. Ennen 0.8-ketjua yhteensopivalla ketjulla (tästä eteenpäin 0.8-ketju) oli tuossa vaiheessa noin 60 % Mining Hash -tehosta, mikä varmisti, ettei jako purkautunut automaattisesti (kuten olisi tapahtunut, jos ennen 0.8-ketjua oleva ketju olisi ylittänyt 0.8-ketjun kokonaistyömäärän, mikä olisi pakottanut 0.8-ketjun solmuja järjestäytymään uudelleen ennen 0.8-ketjua olevaan ketjuun).
>

> Palauttaakseen kanonisen ketjun mahdollisimman pian, BTCGuild ja Slush alensivat Bitcoin 0.8 -solmunsa 0.7:ään, jotta myös niiden poolit hylkäisivät suuremman lohkon. Tämä siirsi enemmistön hashpowerin ketjuun, jossa ei ollut suurempaa lohkoa, mikä lopulta sai 0.8-solmut järjestäytymään uudelleen 0.8:aa edeltävään ketjuun.

Mining-altaiden, BTCGuildin ja Slushin nopea toiminta oli välttämätöntä tässä hätätilanteessa. Ne pystyivät siirtämään suurimman osan Hash:n vallasta ennen 0,8:aa olleeseen jakohaaraan ja siten auttamaan konsensuksen palauttamisessa. Tämä antoi kehittäjille aikaa keksiä kestävä korjaus.


Erittäin mielenkiintoista on myös se, että versio 0.7.2 oli yhteensopimaton itsensä kanssa, kuten aiemmatkin versiot. Tämä on selitetty [BIP50:n juurisyytä koskevassa osassa] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause):


> Koska BDB-lukitus oli liian suuri, siitä oli epäsuorasti tullut lohkon kelpoisuutta määrittävä verkkokonsensussääntö (vaikkakin se on
epäjohdonmukainen ja vaarallinen sääntö, koska lukon käyttö voi vaihdella solmusta toiseen).


Lyhyesti sanottuna ongelma on se, että tietokannan lukitusten määrä, jonka Bitcoin Core -ohjelmisto tarvitsee lohkon tarkistamiseen, ei ole deterministinen. Yksi solmu saattaa tarvita X lukitusta, kun taas toinen solmu saattaa tarvita X+1 lukitusta. Solmuilla on myös rajoitus sille, kuinka monta lukitusta Bitcoin voi ottaa. Jos tarvittavien lukkojen määrä ylittää rajan, lohko katsotaan virheelliseksi. Jos siis X+1 ylittää rajan mutta ei X, kaksi solmua jakaa Blockchain:n ja ovat eri mieltä siitä, kumpi haara on pätevä.


Ratkaisuksi valittiin kahden poolin välittömien toimien lisäksi konsensuksen palauttamiseksi seuraavat toimet



- rajoittaa lohkojen kokoa ja tarvittavia lukituksia versiossa 0.8.1
- korjaa vanhat versiot (0.7.2 ja jotkut vanhemmat) samoilla uusilla säännöillä ja lisää globaalia lukitusrajaa.


Lukuun ottamatta toisessa luetelmakohdassa mainittua korotettua globaalia lukitusrajaa, nämä säännöt otettiin käyttöön väliaikaisesti ennalta määritellyksi ajaksi. Nämä rajoitukset oli tarkoitus poistaa, kun suurin osa solmuista oli päivittynyt.


Tämä Soft Fork vähensi merkittävästi konsensuksen epäonnistumisen riskiä, ja muutamaa kuukautta myöhemmin, 15. toukokuuta, väliaikaiset säännöt poistettiin käytöstä yhdessä koko verkossa. Huomattakoon, että tämä deaktivointi oli käytännössä Hard Fork, mutta se ei ollut kiistanalainen. Lisäksi se julkaistiin yhdessä sitä edeltävän Soft Fork:n kanssa, joten Soft-haarukoitua ohjelmistoa käyttävät ihmiset olivat hyvin tietoisia siitä, että Hard Fork seuraisi sitä. Näin ollen suurin osa solmuista pysyi yhteisymmärryksessä, kun Hard Fork aktivoitui. Valitettavasti muutama solmu, jotka eivät päivittäneet, kuitenkin hävisi prosessissa.


Voisi miettiä, olisiko tämä mahdollista nykyään. Mining toimintaympäristö on nykyään monimutkaisempi, ja riippuen Hash vallan määrästä jaon kummallakin puolella, voi olla Hard vaikeaa ottaa BIP50:n kaltainen korjaus käyttöön riittävän nopeasti. Olisi luultavasti Hard vakuuttaa "väärän" haaran kaivostyöläiset luopumaan lohkopalkkioistaan.


#### BIP66



BIP66 on mielenkiintoinen, koska siinä korostetaan:



- hyvä valinta kryptografia
- vastuullinen tiedonanto
- käyttöönotto paljastamatta haavoittuvuutta
- Mining todennettujen lohkojen päällä


BIP66 oli ehdotus Bitcoin-skriptin allekirjoituskoodauksia koskevien sääntöjen tiukentamiseksi. Motivaatio](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) oli se, että allekirjoituksia voitaisiin analysoida muilla ohjelmistoilla tai kirjastoilla kuin OpenSSL:llä ja jopa OpenSSL:n uusimmilla versioilla. OpenSSL on yleiskäyttöön tarkoitettu salauskirjasto, jota Bitcoin Core käytti tuolloin.


Rajatarkastusasema aktivoitui 4. heinäkuuta 2015. Vaikka edellä mainittu pitää paikkansa, BIP66:lla korjataan myös paljon vakavampi ongelma, jota ei mainita BIP:ssä.


##### Haavoittuvuus



Pieter Wuille julkaisi 28. heinäkuuta 2015 Pieter Wuillen 28. heinäkuuta 2015 julkaisemassa artikkelissa

[sähköposti Bitcoin-dev-postituslistalle](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Hei kaikille,
>

> Haluaisin paljastaa syyskuussa 2014 löytämäni haavoittuvuuden, jota ei voitu hyödyntää, kun BIP66:n 95 prosentin kynnysarvo saavutettiin aiemmin tässä kuussa.
>

> Lyhyt kuvaus:
>

> Erikoisvalmisteinen transaktio olisi voinut haarukoida Blockchain:n solmujen välillä:
>

> - openSSL:n käyttö 32-bittisissä järjestelmissä ja 64-bittisissä Windows-järjestelmissä
> - openSSL:n käyttö muissa kuin Windows 64-bittisissä järjestelmissä (Linux, OSX, ...)
> - joidenkin muiden kuin OpenSSL-koodipohjien käyttäminen allekirjoitusten jäsentämiseen

Sähköpostissa kerrotaan tarkemmin, miten ongelma havaittiin ja mikä sen aiheutti. Lopussa hän esittää tapahtumien aikajanan, ja toistamme tässä joitakin tärkeimpiä tapahtumia. Osa niistä on jo kuvattu, kuten yllä olevasta kuvasta käy ilmi.


![](assets/bip66-timeline-1.webp)


BIP66:een liittyvien tapahtumien aikajana. Mustalla merkityt kohdat on selitetty edellä.


##### Ennen löytämistä



Ilman, että kukaan olisi tiennyt asiasta, se olisi voitu ratkaista nykyään leveydeltään poistetulla BIP62:lla, joka oli ehdotus transaktioiden muokattavuuden mahdollisuuksien vähentämiseksi. BIP62:ssa ehdotettujen muutosten joukossa oli allekirjoitusten koodausta koskevien konsensussääntöjen tiukentaminen eli "tiukka DER-koodaus". Pieter Wuille ehdotti heinäkuussa 2014 joitakin parannuksia BIP:hen, jotka olisivat ratkaisseet ongelman:


> 2014-Jul-18: Muutin BIP62-ehdotusta siten, että sen tiukka DER-allekirjoituksia koskeva vaatimus koskee myös version 1 tapahtumia, jotta Bitcoin:n allekirjoitusten koodaussäännöt eivät riippuisi OpenSSL:n erityisestä jäsentimestä. Lohkoihin ei tuolloin enää louhittu muita kuin DER-allekirjoituksia, joten oletettiin, että tällä ei ole vaikutusta. Katso https://github.com/Bitcoin/bips/pull/90 ja http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Ei tiedossa tuolloin, mutta jos tämä olisi otettu käyttöön, haavoittuvuus olisi ratkaistu.

Koska tämä rajapintarajapinta oli laaja ja kattoi huomattavasti muutakin kuin vain "tiukan DER-koodauksen", sitä muutettiin jatkuvasti, eikä se koskaan päässyt lähellekään käyttöönottoa. BIP poistettiin myöhemmin, koska Segregated Witness, BIP141, ratkaisi transaktioiden muokattavuuden eri ja kattavammalla tavalla.


##### Löydön jälkeen



OpenSSL julkaisi uusia ohjelmistoversioita, joissa oli korjauksia, jotka olisivat ratkaisseet ongelman, jos niitä olisi käytetty Bitcoin:ssä alusta alkaen. OpenSSL:n uusien versioiden käyttäminen vain Bitcoin Core -ohjelman uudessa versiossa pahentaisi tilannetta. Gregory Maxwell selittää tämän toisessa [email thread](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) tammikuussa 2015:


> Vaikka useimmissa sovelluksissa on yleisesti hyväksyttävää hylätä innokkaasti joitakin allekirjoituksia, Bitcoin on konsensusjärjestelmä, jossa kaikkien osallistujien on yleensä oltava samaa mieltä syötettyjen tietojen täsmällisestä pätevyydestä tai virheellisyydestä.  Tavallaan johdonmukaisuus on tärkeämpää kuin "oikeellisuus".
> [...]
> Edellä mainitut korjaukset korjaavat kuitenkin vain yhden oireen yleisestä ongelmasta: konsensuskäyttöön soveltumattomien ohjelmistojen (erityisesti OpenSSL:n) käyttäminen konsensuksen normatiivisen käyttäytymisen varmistamiseksi.  Siksi ehdotan asteittaisena parannuksena kohdennettua Soft-Fork:ää, jolla varmistetaan pian tiukka DER-vaatimustenmukaisuus ja jossa käytetään BIP62:n osajoukkoa.

Hän huomauttaa, että sellaisen koodin käyttö, jota ei ole tarkoitettu käytettäväksi konsensusjärjestelmissä, aiheuttaa vakavia riskejä, ja ehdottaa, että Bitcoin:ssä otetaan käyttöön tiukka DER-koodaus. Tämä on hyvin selkeä esimerkki hyvän valintasalauksen tärkeydestä.


Näistä tapahtumista voi saada sen vaikutelman, että Gregory Maxwell tiesi Pieter Wuillen myöhemmin julkaisemasta haavoittuvuudesta, mutta halusi auttaa korjauksen hiipimisessä varotoimenpiteeksi naamioituna kiinnittämättä liikaa huomiota varsinaiseen ongelmaan. Näin saattaa olla, mutta se on pelkkää spekulaatiota.


Maxwellin ehdotuksen mukaisesti BIP66 luotiin BIP62:n osajoukkona, jossa määritettiin vain tiukka DER-koodaus. Tämä BIP ilmeisesti hyväksyttiin laajalti ja otettiin käyttöön heinäkuussa, vaikka kaksi Blockchain:n jakoa ironisesti johtui *validoimattomasta Mining:sta*. Näitä jakoja käsitellään seuraavassa jaksossa.


![](assets/bip66-timeline-2.webp)


Keskeinen johtopäätös tästä on, että rajapintojen tulisi olla enemmän tai vähemmän *atomisia*, eli niiden tulisi olla riittävän kattavia tarjotakseen jotain hyödyllistä tai ratkaistakseen tietyn ongelman, mutta riittävän pieniä, jotta ne saavat laajan tuen käyttäjien keskuudessa. Mitä enemmän sisältöä BIP:hen laitetaan, sitä pienempi on sen hyväksymisen mahdollisuus.


##### Validoimattomasta Mining:stä johtuvat hajaantumiset



Valitettavasti BIP66:n tarina ei päättynyt tähän. Kun BIP66 aktivoitiin, se osoittautui melko sotkuiseksi, koska jotkut louhijat eivät vahvistaneet lohkoja, joita he yrittivät laajentaa. Tätä kutsutaan validoimattomaksi Mining:ksi eli SPV-Mining:ksi (kuten Simplified Payment Verification). Bitcoin-solmuille lähetettiin hälytysviesti, jossa oli linkki [verkkosivulle, jossa kuvataan ongelmaa](https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> Aikaisin aamulla 4. heinäkuuta 2015 saavutettiin 950/1000 (95 %) kynnysarvo. Pian tämän jälkeen pieni Miner (osa päivittämättömästä 5 prosentin ryhmästä) louhi virheellisen lohkon - mikä oli odotettavissa. Valitettavasti kävi ilmi, että noin puolet verkon Hash-asteesta oli Mining, joka ei validoinut lohkoja täysin (nimeltään SPV Mining), ja rakensi uusia lohkoja tuon virheellisen lohkon päälle.

Hälytyssivulla kehotettiin odottamaan 30 lisävahvistusta enemmän kuin normaalisti, jos he käyttivät Bitcoin Core -ohjelman vanhempia versioita.


Edellä mainittu jako tapahtui 2015-07-04 klo 02:10 UTC lohkon korkeuden [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e) jälkeen. Tämä ongelma ratkaistiin samana päivänä klo 03:50, kun 6 virheellistä lohkoa oli louhittu. Valitettavasti sama ongelma toistui seuraavana päivänä eli 2015-07-05 klo 21:50, mutta tällä kertaa invalidihaaran kesto oli vain 3 lohkoa.


![](assets/bip66-timeline-3.webp)

Tapahtumat, jotka johtivat BIP66:een, sen käyttöönottoon ja jälkiseurauksiin, ovat erittäin hyvä tapaustutkimus siitä, kuinka varovaisia Bitcoin:n kehittäjien on oltava. Muutamia keskeisiä asioita BIP66:sta:



- Tasapaino avoimuuden ja haavoittuvuuden julkaisematta jättämisen välillä on herkkä.
- Julkaisemattomien haavoittuvuuksien korjausten käyttöönotto on hankalaa.
- Säilyttävä yksimielisyys on Hard.
- Ohjelmistot, joita ei ole tarkoitettu konsensusjärjestelmiin, ovat yleensä riskialttiita.
- Rajatarkastusohjelmien pitäisi olla jokseenkin atomisia.


### Johtopäätös aiheesta Kun paska osuu tuulettimeen



Bitcoin:ssä on virheitä. Virheitä löytäviä henkilöitä kannustetaan ilmoittamaan niistä vastuullisesti Bitcoin:n kehittäjille, jotta he voivat korjata virheen paljastamatta sitä julkisesti. Ihannetapauksessa vikakorjaus voidaan naamioida suorituskyvyn parannukseksi tai joksikin muuksi savuverhoksi.


Olemme tarkastelleet joitakin vuosien varrella esiin tulleita vakavampia ongelmia ja sitä, miten niitä on käsitelty. Jotkut löydettiin julkisesti hyväksikäyttöjen kautta, kun taas toiset paljastettiin vastuullisesti ja voitiin korjata ennen kuin pahansuovat toimijat ehtivät hyödyntää niitä.


## Keskustelukysymykset

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Nämä keskustelukysymykset eivät ole vain yhteenveto "Bitcoin-kehitysfilosofian" sisällöstä, vaan niiden tarkoituksena on kannustaa sinua tutkimaan lisää, joten varmista, että lähdet tutkimaan asiaa.


Voit testata ymmärryksesi syvyyttä kirjoittamalla 100-300 sanan [mini-esseen] (https://www.youtube.com/watch?v=N4YjXJVzoZY) valitsemalla aiheen tästä kysymyssarjasta. Jos haluat palautetta työstäsi, voit lähettää sen osoitteeseen mini-essay@planb.network, tarkistamme sen mielellämme.


#### Hajauttaminen



- Hajauttaminen on Hard. Miksi teemme kaiken tämän vaivan saadaksemme sen toimimaan? Voisimmeko valita hybridilähestymistavan, jossa jotkin osat ovat keskitettyjä ja toiset eivät?
- Aiheuttaako hajauttaminen kaksinkertaisten menojen ongelman vai edellyttääkö kaksinkertaisten menojen ongelma hajauttamista? Miten Satoshi ratkaisi kaksinkertaisten menojen ongelman?
- Missä asioissa Bitcoin on edelleen alttiimpana sensuurille, ja miksi sensuuri on niin huono asia? Onko sensuuria puoltavia argumentteja?
- Bitcoin:n todetaan olevan luvaton. Onko olemassa muita maksutapoja, joita voisitte pitää luvattomina?



#### Luottamuksettomuus




- Luottamuksettomuus on usein spektri, ei kaksitahoinen. Mitkä Bitcoin:n näkökohdat ovat pikemminkin Trustless:tä ja mitkä tyypillisesti edellyttävät suurempaa luottamusta? Voidaanko niitä lieventää?
- Haluat käyttää Full node:ta, jotta kaikki tapahtumat voidaan validoida. Lataa Bitcoin Core osoitteesta https://Bitcoin.org/en/download. Mihin luotit ja missä olet täysin Trustless?
- Voiko Trustless-järjestelmän rakentaa luotetun järjestelmän päälle?



#### Yksityisyys




- Mitkä ovat tärkeitä etuja, joita käyttäjä saa, kun hän säilyttää hyvän yksityisyyden suojan Bitcoin:n kanssa toimiessaan? Mitä epäitsekkäitä hyötyjä verkko saa?
- Miten osoitteiden uudelleenkäyttö vaikuttaa yksityisyyteesi?
- Bitcoin käyttää UTXO-mallia, kun taas jotkut vaihtoehtoiset kryptovaluutat käyttävät tilimallia. Mitä vaikutuksia tällä valinnalla on yksityisyyteen?



#### Lopullinen Supply




- Mikä on Bitcoin:n rajallisen Supply:n ja sen Coinbase Transaction:n kautta tapahtuvan kolikkojen liikkeeseenlaskun välinen suhde? Mikä on kolikoiden liikkeeseenlaskun ja arvopaperibudjetin välinen suhde, ja miten ne ovat ristiriidassa keskenään?
- Mitä parametreja Satoshi olisi voinut säätää Bitcoin:n Supply-korkin muuttamiseksi? Mikä muuttuisi, jos hän olisi päättänyt asettaa Supply:n ylärajan 1 miljoonaan? Entä 1 biljoona?
- Miksi jotkut kannattavat Bitcoin Supply:n korottamista? Uskotteko, että näin tapahtuu?


#### Päivittäminen



- Mikä on Speedy Trial ja miksi Taproot:n aktivointi oli tarpeen?
- Miksi tarvitsemme niin suuren prosenttiosuuden kaivostyöläisiä päivittääksemme softforkissa? Miksi kynnysarvo ei ole vain 51 prosenttia?



#### Vastakkainasettelu




- Mikä on sybil-hyökkäys ja mikä tekee hajautetusta verkosta niin alttiin sille?
- Miksi on tärkeää, että kaikki Bitcoin-verkoston toimijat - eivätkä vain kehittäjät - ajattelevat vastakkain?



#### Avoin lähdekoodi




- Vain muutamalla ylläpitäjällä on tarvittavat GitHub-oikeudet koodin yhdistämiseen [Bitcoin Core](https://github.com/Bitcoin/Bitcoin) -arkistoon. Eikö tämä ole ristiriidassa luvattoman verkon kanssa?
- Onko avoimen lähdekoodin kehitysprosessi altis sybil-hyökkäyksille? Jos on, miten torjuisitte sen?
- Mitkä ovat kolmannen osapuolen avoimen lähdekoodin kirjastojen käytön edut ja haitat, ja mikä on Bitcoin Core -ohjelmiston lähestymistapa?
- Millä tavoin tarvitsemme muutakin tarkastelua kuin pelkkää koodin tarkastelua? Miten määritetään, kuinka paljon tarkastelua on tarpeeksi?
- Miten varmistamme, että Bitcoin:n parissa työskentelee aina riittävästi asiantuntevia henkilöitä? Mitä tapahtuu, jos heitä ei ole, ja miten arvioimme heidän rehellisyyttään ja aikomuksiaan?



#### Skaalaus




- On väitetty, että jakaminen tarjoaa skaalautumisen etuja monimutkaisuuden kustannuksella. Miksi meidän pitäisi tai ei pitäisi ottaa käyttöön teknologisia parannuksia, koska niitä on vaikea ymmärtää, vaikka ne vaikuttavat teknisesti järkeviltä?
- Mitkä ovat esimerkkejä Bitcoin:ssa käyttöön otetuista sisäänpäin skaalautumismenetelmistä?
- Miksi vertikaalinen skaalautuminen on paljon vaikeampaa hajautetussa järjestelmässä? Entä horisontaalinen skaalautuminen?
- Emme näytä pääsevän lähellekään yksimielisyyttä siitä, miten voisimme ottaa koko maailman mukaan Bitcoin:ään. Eikö Satoshi:n olisi pitänyt ainakin miettiä, miten sinne päästään, ennen kuin Mining:n ensimmäinen lohko vuonna 2009?
- Miten luokittelisit (pystysuora, vaakasuora, sisäänpäin suuntautuva vai ei skaalautumistekniikka) kunkin seuraavista: sharding, lohkokoon kasvattaminen, SegWit, SPV-solmut, keskitetyt pörssit, Lightning Network, lohkovälin pienentäminen, Taproot, sivuketjut



# Viimeinen jakso


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Arvostelut & arvostelut


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Päätelmä


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>