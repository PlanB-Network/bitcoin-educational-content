---
name: Ensimmäisen Bitcoin-solmun perustaminen
goal: Bitcoin-solmun ymmärtäminen, asentaminen, konfigurointi ja käyttö
objectives: 


  - Ymmärtää Bitcoin-solmun rooli ja tarkoitus.
  - Tunnista käytettävissä olevat erilaiset laitteisto- ja ohjelmistoratkaisut.
  - Asenna ja määritä Full node (Bitcoin core).
  - Käytä Interface-sateenvarjoa ja lisää hyödyllisiä sovelluksia.
  - Liitä henkilökohtainen Wallet omaan solmuunsa.
  - Tutustu lisäasetuksiin ja parhaisiin turvallisuuskäytäntöihin.


---
# Ryhdy suvereeniksi bitcoineriksi



Tunnet luultavasti sanonnan "Not your keys, not your coins", joka kannustaa säilyttämään bitcoinisi itse. Omien avainten hallussapito on toki tärkeä ensimmäinen askel, mutta se ei riitä. Todellisen rahapoliittisen itsemääräämisoikeuden saavuttamiseksi sinun on myös asennettava ja käytettävä omaa Bitcoin-solmua. Tämä kurssi on suunniteltu opastamaan sinut tämän perustavanlaatuisen askeleen läpi Bitcoin-matkallasi!



BTC 202 on helppokäyttöinen kurssi, joka on suunniteltu opettamaan sinulle, miten kehräät oman Bitcoin-solmusi, vaikka et olisikaan tekninen asiantuntija. Aloitamme määrittelemällä, mikä Bitcoin-solmu on, mihin sitä käytetään ja miksi on ehdottoman tärkeää kehrätä sellainen itse. Sen jälkeen opastan sinua askel askeleelta laitteiston valinnassa, tarvittavan ohjelmiston asentamisessa, Wallet-solmun kytkemisessä ja ensimmäisten mahdollisten optimointien tekemisessä, jotta voit viedä sitä pidemmälle.



Bitcoin-solmun käyttäminen ei ole vain asiantuntijoiden vaihtoehto, vaan välttämättömyys. Se on resilienssityökalu, joka jokaisen käyttäjän on ymmärrettävä ja otettava käyttöön. Tämä kurssi on lähtökohtasi tulla suvereeniksi bitcoineriksi!




+++




# Johdanto


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Kurssin yleiskatsaus


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Tervetuloa BTC 202:een, jossa opit asentamaan, konfiguroimaan ja käyttämään Bitcoin-solmua helposti ja itsenäisesti. Mutta siinä ei ole vielä kaikki: opit myös lisää solmujen paikasta ja toiminnasta Bitcoin-järjestelmässä. Kurssilla vuorottelevat teoreettiset selitykset ja ohjattu käytännön harjoittelu.



### Osa 1 - Johdanto



Tässä kurssin ensimmäisessä osassa selvitämme peruskäsitteitä ja siirrymme sitten tarkempiin määritelmiin. Mikä on solmu? Mitä eroja on solmun, Wallet:n ja Miner:n välillä? Sen jälkeen opit Bitcoin core:sta ja protokollan toteutuksista. Tavoitteena on puhua samaa kieltä, välttää sekaannuksia ja luoda vankka teoreettinen perusta.



### Osa 2 - Itsenäiseksi bitcoineriksi tuleminen



Tässä toisessa osassa selitän aluksi, miksi on tärkeää käyttää omaa Bitcoin-solmua. Sen jälkeen tarkastelemme erilaisia solmutyyppejä (täydelliset, pruned, SPV...), niiden toimintaa ja teknisiä vaikutuksia.



Sen jälkeen annamme sinulle yleiskatsauksen Bitcoin-solmun käyttämiseen käytettävissä olevista ohjelmistoista sekä niiden eduista ja haitoista. Lopuksi annamme joitakin käytännönläheisiä suosituksia tarpeisiisi ja budjettiisi sopivan laitteiston valitsemiseksi.



Tässä jaksossa kuvataan siis suvereenin bitcoinerin polku: ymmärrä, miksi solmun käyttäminen on välttämätöntä, valitse solmutyyppi, valitse tämän valinnan perusteella ohjelmisto, ja valitusta ohjelmistosta riippuen määritä sopiva laitteisto.



### Osa 3 - Bitcoin-solmun asentaminen helposti



Kun nämä valmistelut on tehty, on aika siirtyä käytäntöön, kun osa 3 on omistettu Umbrelille: kotipilvi-käyttöjärjestelmä, joka yksinkertaistaa itseisännöintiä ja Bitcoin- ja Lightning-solmun asennusta.



Lyhyen Umbrelin esittelyn jälkeen tarjoamme yksityiskohtaisen oppaan, joka opastaa sinut asennus- ja konfigurointiprosessin läpi omassa DIY-koneessasi. Tämän osan tavoite on selvä: saada ensimmäinen täysin toimiva ja synkronoitu Bitcoin-solmusi.



### Osa 4 - Wallet:n liittäminen solmuun



Nyt kun olet perustanut Bitcoin-solmun, on aika käyttää sitä! Tässä osiossa opit, miten voit liittää Wallet-hallintaohjelmiston (kuten Sparrow wallet) omaan Address-indeksoijaasi (Electrs tai Fulcrum) tai suoraan Bitcoin core:een, jotta et ole enää riippuvainen julkisista palvelimista.



Tarkastelemme myös indeksoijien roolia ja eri tapoja muodostaa yhteys solmuun (LAN, Tor, Tailscale jne.). Viimeisessä luvussa käymme lopuksi läpi Umbrelissa saatavilla olevat hyödyllisimmät sovellukset jokapäiväiselle bitcoin-käyttäjälle.



### Osa 5 - Edistyneet käsitteet ja parhaat käytännöt



Tässä BTC 202 -kurssin viimeisessä osassa tavoitteena on syventää tietämystäsi. Ensin tarkastelemme parhaita käytäntöjä, joita kannattaa omaksua uuden Bitcoin-solmun kanssa, ja sitä, miten sitä ylläpidetään pitkällä aikavälillä.



Tämän jälkeen käymme läpi osan aiemmin kurssilla käsitellystä teoriasta, kuten IBD-prosessin ja vertaisverkon löytämisen yksityiskohtaisen ymmärtämisen, solmun anatomian tutkimisen ja lopuksi opettelemme, miten Bitcoin.conf-tiedostoa käytetään asetusten hienosäätöön.



### Osa 6 - Loppuosa



Kuten kaikilla Plan ₿ Network-kursseilla, loppuosassa on loppukoe, jossa testataan tietämystäsi Bitcoin-solmuista.



Oletko valmis käynnistämään ensimmäisen Bitcoin-solmusi? Aseta kurssi kohti suvereniteettia!



## Mikä on Bitcoin-solmu?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Kuten sen luoja Satoshi Nakamoto kuvailee, Bitcoin on vertaisvertainen sähköinen käteisjärjestelmä. Tämä yksinkertainen lause, joka on valkoisen kirjan otsikko, sisältää monia vihjeitä Bitcoin:n luonteesta:




- Ensinnäkin Satoshi kuvaa Bitcoin:tä "järjestelmäksi", toisin sanoen yhtenäiseksi joukoksi laitteisto- ja ohjelmistokomponentteja, jotka ovat vuorovaikutuksessa keskenään tarjotakseen tietyn palvelun tai suorittaakseen tietyn toiminnon;
- Seuraavaksi hän selittää, että tämä järjestelmä mahdollistaa sähköisen käteisen eli eräänlaisen aineettoman valuutan käytön;
- Lopuksi hän huomauttaa, että järjestelmä ei ole riippuvainen mistään keskusyksiköstä: se on "vertaisverkkopohjainen", mikä tarkoittaa, että käyttäjät itse käyttävät järjestelmää.



Koska Bitcoin on järjestelmä, sitä on välttämättä käytettävä tietokoneissa. Ja koska se on luonteeltaan vertaisverkkojärjestelmä, käyttäjät ottavat itse vastuun näiden koneiden käyttämisestä. Kutsumme "Bitcoin-solmuksi" juuri sitä tietokonetta, jolla Bitcoin-protokollaa (kuten Bitcoin core:ää, mutta palaamme siihen myöhemmin) toteuttava ohjelmisto on käynnissä. Tämän ansiosta Bitcoin voi toimia ilman keskusviranomaista: validointi suoritetaan hajautetusti tuhansien käyttäjien tuhansien itsenäisten koneiden toimesta.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Juuri nämä käyttäjät takaavat Bitcoin:n turvallisuuden. Kuten Eric Voskuil selittää kirjassaan *Cryptoeconomics*, Bitcoin:n turvallisuus ei perustu Blockchain:een, hashing-tehoon, validointiin, hajauttamiseen, kryptografiaan, avoimeen lähdekoodiin eikä peliteoriaan. Bitcoin:n turvallisuus riippuu ensisijaisesti henkilöistä, jotka ovat valmiita ottamaan henkilökohtaisen riskin. Hajauttamisen ansiosta tämä riski voidaan jakaa suureen määrään yksilöitä, ja vain heidän kykynsä vastustaa sitä takaa järjestelmän kestävyyden.



Tämä periaate on helppo ymmärtää: jos Bitcoin olisi riippuvainen yhdestä ainoasta solmusta, jonka omistaa yksi henkilö, kyseisen henkilön vangitseminen riittäisi verkon sulkemiseen, koska hän yksin kantaisi kaikki riskit. Kun solmuja on kymmeniä tuhansia ympäri maailmaa, riski leviää: jokainen näistä operaattoreista olisi neutralisoitava Bitcoin:n pysäyttämiseksi.



![Image](assets/fr/048.webp)



Voimme siis erottaa ja nimetä useita käsitteitä, jotta asiat selkiytyisivät tämän kurssin loppua varten:




- Bitcoin-valuutta: tässä järjestelmässä tapahtuvissa liiketoimissa käytettävä laskentayksikkö;
- Bitcoin-verkko: kaikkien toisiinsa liitettyjen solmujen joukko;
- Bitcoin-solmut: koneet, joilla on Bitcoin-toteutus;
- Bitcoin-toteutukset: ohjelmistot, jotka kääntävät protokollan suoritettaviksi ohjeiksi;
- Bitcoin-protokolla: järjestelmän toimintaa ohjaavien sääntöjen kokonaisuus;
- Bitcoin-järjestelmä: kaikkien näiden Elements-järjestelmien johdonmukainen yhdistelmä.



### Bitcoin-solmun rooli



Bitcoin-solmut muodostavat yhdessä niin sanotun Bitcoin-verkon. Niiden avulla koko järjestelmä toimii itsenäisesti ilman keskusviranomaista tai palvelinhierarkiaa.



Bitcoin suunniteltiin alusta alkaen siten, että jokainen käyttäjä voi käyttää henkilökohtaista solmua. Tämä pätee edelleen nykyiseen Bitcoin core-ohjelmistoon, jossa yhdistyvät Wallet:n ja solmun roolit. Nykyään tämä toiminto on kuitenkin usein eriytetty: monet nykyaikaiset Bitcoin-lompakot ovat vain lompakoita, jotka ovat yhteydessä ulkoisiin solmuihin (jotka voivat olla saman henkilön omistamia tai ei).



### Pidä Blockchain



Solmun ensimmäinen tehtävä on ylläpitää paikallista kopiota Blockchain:stä. Double-spending:n estämiseksi Bitcoin:lla ilman keskusviranomaisen osallistumista, jokaisen käyttäjän on tarkistettava, ettei järjestelmässä ole tapahtumaa. Ainoa tapa olla varma tästä on tietää kaikki Bitcoin:ssa tehdyt transaktiot. Tästä syystä kaikki transaktiot leimataan aikaleimalla ja ryhmitellään lohkoihin, ja jokainen solmu tallentaa koko Blockchain:n.



> Ainoa tapa varmistaa, ettei tapahtumaa ole tapahtunut, on olla tietoinen kaikista tapahtumista.

Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer sähköinen käteisrahajärjestelmä*. https://Bitcoin.org/Bitcoin.pdf



Blockchain on siis kehittyvä rekisteri: aina kun Miner julkaisee uuden lohkon, solmu tarkistaa sen kelpoisuuden ennen kuin se lisää sen omaan paikalliseen kopioonsa ketjusta. Tällä hetkellä (heinäkuussa 2025) koko Blockchain:n koko on yli 675 gigatavua, ja tämä koko kasvaa edelleen, sillä uusi lohko lisätään keskimäärin 10 minuutin välein.



![Image](assets/fr/049.webp)



Solmu ylläpitää myös paikallista tietuetta kaikista tiettynä ajankohtana olemassa olevista UTXO:ista, jota kutsutaan nimellä **UTXO set**. Tämä tietokanta sisältää kaikki käyttämättömät Bitcoin-fragmentit. Käymme tätä aihetta yksityiskohtaisesti läpi kurssin viimeisessä osassa.



### Tarkista ja jaa tapahtumat



Solmun toinen tehtävä on varmistaa tapahtumien todentaminen ja siirtäminen. Kun uusi transaktio saapuu solmuun (joko Wallet-ohjelmiston tai toisen solmun kautta), se tarkistaa, että se on sääntöjen mukainen (konsensussäännöt ja välityssäännöt). Esimerkiksi:




- käytettyjä bitcoineja on oltava sen UTXO-sarjassa (tietokannassa, jossa on käyttämättömiä tuotoksia);
- allekirjoituksen on oltava pätevä ja kaikkien menoehtojen on täytyttävä (pätevä käsikirjoitus);
- tuotosten kokonaismäärä ei saa ylittää panosten kokonaismäärää, mikä tarkoittaa, että kustannukset eivät voi olla negatiivisia.



![Image](assets/fr/050.webp)



Vahvistuksen jälkeen tapahtuma tallennetaan solmun Mempool:ään, joka on väliaikainen muistitila, joka on varattu vahvistamattomille tapahtumille, ja välitetään sitten muille verkon vertaisverkoille, joihin solmulla on yhteys. Tämä jakelu- ja validointimekanismi jatkuu solmusta toiseen. Tällä tavoin transaktio leviää Bitcoin-verkon kautta, ja jokainen solmu tallentaa sen Mempool:ään, kunnes Miner sisällyttää sen kelvolliseen lohkoon, joka toimii sen jälkeen sen ensimmäisen vahvistuksen perusteella.



### Tarkista ja jaa lohkot



Solmun kolmas tehtävä on louhittujen lohkojen hallinta. Kun Miner havaitsee uuden lohkon, jolla on voimassa oleva Proof of Work, se lähetetään verkkoon. Solmut vastaanottavat sen, tarkistavat, että se on kaikkien protokollasääntöjen mukainen, ja liittävät sen sitten omaan paikalliseen Blockchain-kopioonsa, jos se on kelvollinen.  Tämä prosessi jatkuu, kunnes kaikki Bitcoin-verkon solmut ovat tietoisia uudesta lohkosta.



![Image](assets/fr/051.webp)



## Mitä eroa on keulan ja Wallet:n välillä?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Bitcoin:ää käytettäessä on tärkeää erottaa toisistaan kaksi eri ohjelmistotyyppiä: solmu ja Wallet.



Kuten edellä mainittiin, Bitcoin-solmu on ohjelmisto, joka osallistuu aktiivisesti vertaisverkkoon. Se suorittaa kolme päätehtävää:




- gW-77:n varmuuskopio,
- tapahtumien validointi ja välittäminen,
- lohkon validointi ja rele.



Bitcoin Wallet puolestaan on ohjelmisto, joka on suunniteltu yksityisten avainten tallentamiseen ja hallintaan. Näiden avainten avulla voit käyttää bitcoinejasi täyttämällä lukitusskriptit (yleensä allekirjoituksen avulla). Wallet voi muodostaa yhteyden solmuun (joko paikalliseen tai etäyhteyteen) saadakseen tietoa Blockchain:n tilasta ja lähettää rakentamiaan transaktioita, mutta se ei ole sellaisenaan verkon osallistuja.



Joissakin tapauksissa nämä kaksi toimintoa ovat rinnakkain samassa ohjelmistossa, kuten Bitcoin core:ssä, joka toimii sekä Full node:na että Wallet:nä. Monet suositut Wallet-ohjelmat (Sparrow, BlueWallet jne.) vaativat kuitenkin yhteyden ulkoiseen solmuun (omaan tai kolmannen osapuolen solmuun), jotta ne voivat lähettää tapahtumia ja määrittää Wallet:n saldon.



![Image](assets/fr/052.webp)



## Mitä eroa on solmun ja Miner:n välillä?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Solmun ja Miner:n käsitteet sekoitetaan usein keskenään. Näillä kahdella Elements:lla on kuitenkin täysin erilaiset tehtävät järjestelmässä.



Kun Satoshi Nakamoto käynnisti Bitcoin:n vuonna 2009, jokaisen käyttäjän odotettiin alun perin osallistuvan koko verkkoon. Alkuperäinen Bitcoin-ohjelmisto yhdisti siis useita toimintoja samanaikaisesti: se toimi Wallet:nä, solmuna, ja myös Miner:na, joka kykeni luomaan uusia lohkoja. Mining:n vaikeusaste oli tuolloin hyvin alhainen. Sinun piti vain ajaa Bitcoin-ohjelmistoa tietokoneellasi löytääksesi lohkoja ja saadaksesi palkkioksi bitcoineja.



Bitcoin:n asteittaisen yleistymisen ja kaivostyöntekijöiden määrän kasvun myötä Mining:n kilpailutilanne on kuitenkin muuttunut radikaalisti. Nykyään Mining:stä on tullut erittäin kilpailtu toiminta, jota hallitsevat erikoistuneilla infrastruktuureilla varustetut teolliset toimijat. Uuden lohkon louhimiseen tarvittava teho on nyt niin suuri, että yksittäisen käyttäjän on käytännössä mahdotonta saavuttaa sitä vain tavanomaisella tietokoneella. Tämän seurauksena Mining:n louhinta tapahtuu nykyään pääasiassa ASIC-koneiden (*Application-Specific Integrated Circuits*) avulla. Nämä piirit on optimoitu yksinomaan suorittamaan kaksinkertaista SHA-256:ta, Mining:ssä käytettyä algoritmia Bitcoin:ssa.



![Image](assets/fr/053.webp)



Tämän kehityksen myötä Bitcoin-solmun ja Miner-solmun tehtävät ovat muuttuneet selvästi erillisiksi. Kuten edellä on esitetty, Bitcoin-solmun rooli on puhtaasti informatiivinen ja validointiin perustuva. Miner:n rooli on erilainen:




- Se valitsee vireillä olevat tapahtumat Mempool:ssä.
- Se muodostaa ehdokaslohkon, joka yhdistää nämä transaktiot.
- Hän etsii kokeilemalla ja erehtymällä kelvollista Proof of Work:aa.
- Jos se löytää kelvollisen todisteen, se lähettää lohkon oman solmunsa kautta muille solmuille.



Miner tarvitsee Bitcoin-solmun ollakseen yhteydessä verkkoon.



Miner:n rooli on myös toisinaan erotettu kopterin roolista. Hakkuri on kone, jonka tehtävänä on Hash mallilohkojen, jotka poolipalvelin toimittaa, hakeminen etsimällä hasheja, jotka täyttävät osuuksille määritellyn vaikeustavoitteen, ei Bitcoin:n. Loput Mining-prosessista, johon kuuluu varsinainen lohkojen rakentaminen, transaktioiden valinta tai Bitcoin:n oman vaikeusasteen mukainen Proof-of-Work-haku sekä jakelu, suoritetaan suoraan poolien toimesta.



![Image](assets/fr/054.webp)



Miner:n ja solmun välillä on myös merkittävä ero taloudellisten kannustimien kannalta. Bitcoin-solmun käyttämisestä ei ole suoraa rahallista hyötyä. Toisaalta Mining:ään osallistuminen tuo palkintoja (tukia ja transaktiomaksuja) jokaisesta löydetystä lohkosta.



Osassa 2 tarkastelemme yksityiskohtaisemmin Bitcoin-solmun asentamisen ja käytön käytännön ja henkilökohtaisia etuja, jotka eivät ole pelkästään taloudellisia.



## Bitcoin core ja protokollatoteutukset


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin-protokolla ei ole ohjelmisto: se on joukko hiljaisia sääntöjä, jotka jaetaan verkon käyttäjien kesken. Se määrittelee transaktioiden voimassaoloehdot, rahanluontimekanismit, lohkomuodon, Proof-of-Work-ehdot ja monia muita eritelmiä. Käyttäjien on käytettävä ohjelmistoja, jotka toteuttavat nämä säännöt, jotta he voivat olla vuorovaikutuksessa protokollan kanssa: tätä kutsutaan Bitcoin:n **toteutukseksi**.



Toteutus on siis solmuohjelmisto: ohjelma, joka kykenee olemaan yhteydessä muihin Bitcoin-verkon koneisiin, lataamaan, tarkistamaan, tallentamaan ja levittämään lohkoja ja transaktioita sekä panemaan paikallisesti täytäntöön konsensus- ja välityssäännöt. Jokainen toteutus on tietyllä ohjelmointikielellä kirjoitettu konkreettinen tulkinta protokollasta, jolla on oma arkkitehtuurinsa, suorituskykynsä ja ergonomiansa. Kullakin toteutuksella on myös oma kehitysorganisaationsa, jolla on oma vastuunjakonsa.



Näistä toteutuksista yksi on ylivoimaisesti hallitseva: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Historiallinen toteutus, josta on tullut vertailuarvo



Bitcoin core on Bitcoin-protokollan viiteohjelmisto. Se on johdettu Satoshi Nakamoton vuosina 2008-2009 kirjoittamasta alkuperäisestä koodista, ja se on sen suora jatko. Se tunnettiin alun perin nimellä "*Bitcoin*", sitten "*Bitcoin QT*" (koska siihen lisättiin graafinen Interface Qt-kirjaston kautta), ja sen nimi muutettiin "*Bitcoin core*" vuonna 2014, jotta ohjelmisto erottuisi selvästi verkosta. Versiosta 0.5 lähtien sitä on jaettu kahdella komponentilla: `Bitcoin-qt` (graafinen Interface) ja `bitcoind` (komentorivin Interface).



Teoriassa Bitcoin core ei edusta Bitcoin-protokollaa, vaan se on vain yksi toteutus monien muiden joukossa. Se erottuu kuitenkin edukseen laajamittaisen hyväksynnän, iän, koodin vankkuuden ja kehitysprosessin tiukkuuden vuoksi. Näin ollen Bitcoin core:n soveltamat säännöt ovat käytännössä käytännössä Bitcoin-protokollan säännöt: käyttäjät, kehittäjät, kaivostoimijat ja ekosysteemipalvelut viittaavat lähes yksinomaan siihen.



### Toteutusten nykyinen jakautuminen



[Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (tunnettu kehittäjä ekosysteemissä) elokuussa 2025 keräämien tietojen mukaan toteutusten jakautuminen verkon julkisten solmujen kesken on seuraava:




- Bitcoin core**: 87.3% solmuista
- Bitcoin Knots**: 12.5
- Muut kumulatiiviset toteutukset**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Toisin sanoen noin yhdeksässä kymmenestä julkisesta solmusta käytetään Bitcoin core:tä. Loput verkosta on riippuvainen marginaalisemmista asiakkaista (vaikka Knotsin osuus on kasvanut jyrkästi viime kuukausina, eikä vähiten OP_RETURN-kokorajasta käytyjen keskustelujen seurauksena). Näitä vaihtoehtoisia toteutuksia ylläpitää usein yksi henkilö tai pieni tiimi.



**Huomautus:** Nämä luvut ovat kuitenkin vielä arvioita, sillä ne perustuvat pääasiassa *kuunteleviin solmuihin*, eli solmuihin, jotka ottavat vastaan saapuvia yhteyksiä (portti 8333 on auki). Muita kuin kuuntelevia solmuja* on paljon monimutkaisempi laskea, koska niihin ei voi ottaa yhteyttä suoraan: on odotettava, että ne tekevät aloitteen lähtevän yhteyden muodossa. Luke Dashjr:n sivusto väittää yrittävänsä laskea myös näitä *ei-kuuntelevia solmuja*, mutta täysin tarkkoja tietoja niistä on edelleen mahdotonta saada, ja näiden tilastojen päivittäminen on väistämättä jäljessä todellisuudesta.



### Bitcoin core:n sisäinen toiminta



Bitcoin core on kirjoitettu C++-kielellä. Se on myös avoimen lähdekoodin hanke, jota ylläpitää kehittäjäyhteisö, joka toimii vapaaehtoisesti tai saa palkkaa eri tahoilta (usein ekosysteemiin kuuluvilta yrityksiltä, jotka ovat kiinnostuneita Coren kehittämisestä). [Koodi on GitHubissa](https://github.com/Bitcoin/Bitcoin), ja kehitys noudattaa tiukkaa:




- Osallistujat** esittävät ehdotuksia _pull request_ (PR) -muodossa. Periaatteessa kuka tahansa voi ehdottaa muutosta, mutta se on testattava, dokumentoitava ja läpäistävä vertaisarviointiprosessi.
- **ylläpitäjillä** on oikeus hyväksyä ja yhdistää PR:t. He takaavat projektin yhtenäisyyden ja vakauden. Heinäkuussa 2025 heitä on viisi: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao ja Ryan Ofsky.
- Helmikuun 2023 jälkeen ei ole ollut **pääylläpitäjää**. Tätä tehtävää hoiti aluksi Satoshi Nakamoto Bitcoin:n käynnistämisen yhteydessä, sitten Gavin Andresen Nakamoton lähdettyä vuoden 2011 alussa ja lopulta Wladimir J. Van Der Laan vuodesta 2014 vuoteen 2023.



![Image](assets/fr/057.webp)



Bitcoin core:n kehitys noudattaa ansiosidonnaista logiikkaa: uusia osallistujia kannustetaan tarkistamaan ja testaamaan koodia ennen kuin he itse ehdottavat muutoksia. Päätökset perustuvat tekniseen yksimielisyyteen, ja suuret muutokset (erityisesti yksimielisyyden piiriin kuuluvilla aloilla) edellyttävät keskusteluja julkisissa kanavissa, kuten postituslistoilla tai PR-arviointikerhoissa.



### Muut Bitcoin-toteutukset



Vaikka muut asiakkaat ovatkin vähäisiä, muita asiakkaita on olemassa. Tärkein niistä on Luke Dashjrin kehittämä Bitcoin Knots, joka on Fork Bitcoin core:stä ja joka sisältää lisävaihtoehtoja ja konservatiivisemman lähestymistavan kehitykseen. Näihin kuuluvat tiukemmat rajoitukset tapahtumamuodoille.



![Image](assets/fr/058.webp)



Voimme myös mainita:




- Libbitcoin**: Amir Taakin kehittämä ja Eric Voskuilin ylläpitämä modulaarinen C++-kirjasto;
- Bcoin**: JavaScript-toteutus, jota ei enää ylläpidetä aktiivisesti;
- BTCD/btcsuit**e: toteutus Go-kielellä.



Nämä hankkeet edistävät ekosysteemin monimuotoisuutta, mutta niiden käyttöönotto on edelleen hyvin vähäistä, mikä vaikeuttaa Bitcoin core:n itsenäistä kehitystä.



### Core-kehittäjien voima



Saatat luulla, että Bitcoin core:n kehittäjät hallitsevat suoraan Bitcoin:ää, mutta näin ei ole. He eivät voi määrätä muutosta protokollaan. Heidän tehtävänään on ehdottaa koodia. Kukin käyttäjä voi solmunsa kautta päättää, käyttääkö hän tätä koodia vai ei.



Tämä tarkoittaa sitä, että jos Bitcoin core:n muutos ei vastaa yksimielisyyttä, solmut voivat jättää sen huomiotta joko jättämällä Bitcoin core:n päivittämättä tai yksinkertaisesti muuttamalla toteutusta. Sitä vastoin, jos käyttäjien toivoma ominaisuus estyy Core-kehitysprosessissa, on aina mahdollista siirtyä toiseen toteutukseen tai Fork hankkeeseen.



Kuten keskustelemme myöhemmin tällä kurssilla, solmut (eli kauppiaat) antavat taloudellisen painoarvonsa mukaan hyötyä protokollan versiolle (ja siten myös vastaavalle valuutalle) hyväksymällä sen sääntöjä noudattavia yksiköitä. Bitcoin:n todellinen hallintavalta on siis näillä kauppiailla, ei kehittäjillä.




# Ryhdy suvereeniksi bitcoineriksi


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Miksi vääntää omaa solmua?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Yleisesti uskotaan, että Bitcoin-solmun käyttäminen on puhtaasti epäitsekäs teko, josta ei ole henkilökohtaista hyötyä ja joka palvelee yksinomaan verkon hajauttamista. Jotkut pitävät sitä eräänlaisena velvollisuutena bitcoin-käyttäjille tukea järjestelmää ja osoittaa kiitollisuuttaan Bitcoin:lle.



Kuten edellisissä luvuissa todettiin, solmun kehräämisestä ei ole suoraa taloudellista hyötyä. Sen vuoksi voisi ajatella, että siihen ei ole mitään henkilökohtaista etua. Oman solmun pyörittäminen tuo kuitenkin monia yksilöllisiä etuja. Voidakseni vakuuttaa sinut tästä, esittelen tässä luvussa kaikki syyt, sekä tekniset että strategiset, miksi sinun pitäisi asentaa ja käyttää omaa Bitcoin-solmua.



### Liiketoimien luottamuksellisempi levittäminen



Kun Wallet-ohjelmisto muodostaa yhteyden ulkoiseen solmuun, se siirtää tapahtumat infrastruktuuriin, joka ei ole hallinnassasi. Tämä aiheuttaa ilmeisen valvontariskin: ulkoisen solmun operaattori voi analysoida tapahtumien yksityiskohtia, mukaan lukien summat ja taajuudet, ja tiettyjä metatietoja (kuten IP-osoitteita, kellonaikoja ja sijainteja) ristiintaulukoimalla yhdistää ne mahdollisesti henkilöllisyyteesi.



Kuten edellisessä luvussa todettiin, lompakot eivät kommunikoi Bitcoin-verkon kanssa taikaiskusta; niiden on otettava yhteys solmuun, jotta ne voivat kysyä saldoja tai lähettää transaktioita. Jos et ole koskaan perustanut omaa solmua, tämä tarkoittaa, että Wallet on riippuvainen kolmannen osapuolen (yleensä ohjelmiston takana olevan yrityksen) infrastruktuurista. Tämä kolmas osapuoli, varsinkin jos se on yritys, voi tarkkailla, hyödyntää tai jopa luovuttaa näitä tietoja: joko kaupallisista syistä, oikeudellisista syistä tai piratismin seurauksena.



![Image](assets/fr/059.webp)



Käyttämällä omaa solmua lähetät transaktiosi suoraan verkkoon, jolloin välittäjät ohitetaan. Jos suojaat solmusi asianmukaisesti (josta puhutaan myöhemmin) tai noudatat tiettyjä standardeja, mitään tietoja ei paljastu: IP-osoitteesi Address tai transaktioiden yksityiskohdat eivät kulje sellaisen tahon kautta, jota et hallitse. Tämä on perusedellytys luottamuksellisuutesi säilyttämiselle Bitcoin:ssä.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Ei-sensuroitavat liiketoimet



Samoista edellä mainituista syistä kolmannen osapuolen solmuun perustuva Wallet-ohjelmisto on altis sensuuririskille: etäsolmun ylläpitäjä voi kieltäytyä välittämästä tiettyjä tapahtumia eri syistä. Se voi pitää niitä epäilyttävinä tai toimintatapojensa vastaisina. Tapahtuma voidaan myös estää, jos se ei ole solmun välityssääntöjen mukainen. Lopuksi operaattori voi kohdistaa IP-osoitteesi Address:een estääkseen transaktioiden lähetyksen.



Käyttämällä omaa solmua varmistat, että transaktiosi leviävät vertaisverkossa. Tämä tarkoittaa, että sinulla on täysi kontrolli tapahtumiesi jakelusta, etkä ole riippuvainen välikäyttäjästä. Kunhan transaktio noudattaa konsensus- ja välityssääntöjä sinun solmuusi liitetyissä solmuissa, se lähetetään verkossa, ja jos se sisältää riittävästi maksuja, Miner integroi sen lohkoon. Oman solmun omistaminen takaa neutraalin, lupavapaan vahvistuksen transaktioillesi.



### Riippumaton tietojen todentaminen



Ilman henkilökohtaista solmua olet edelleen riippuvainen kolmannesta osapuolesta saadaksesi tietoja, kuten Address-saldosi, tapahtuman vahvistustilanteen ja lohkojen voimassaolon. Tämä edellyttää epäsuoraa luottamusta ulkoisen solmun tarkkuuteen ja eheyteen.



![Image](assets/fr/060.webp)



Full node:n käyttäminen tarkoittaa, että voit itse tarkistaa kaikki protokollasäännöt jokaisen transaktion ja jokaisen lohkon osalta. Näin ollen Wallet:n näyttämä saldo ei ole etäpalvelimelta saatua tietoa, vaan tulos, joka on laskettu paikallisesti Blockchain:n täydellisestä kopiosta, joka on validoitu lohko lohkolta. Tämä lähestymistapa antaa täyden merkityksen bitcoin-käyttäjien lausahdukselle:



> Älä luota, tarkista.

### Järjestelmän turvallisuuden parempi jakautuminen



Jokainen verkkoon liitetty solmu vahvistaa Bitcoin:n redundanssia ja joustavuutta. Se helpottaa tiedon levittämistä ja mahdollistaa uusien vertaisverkkojen yhteyden muodostamisen toisiinsa. Ilman solmuja järjestelmä olisi yksinkertaisesti toimimaton.



Kuten olemme nähneet, Bitcoin:n turvallisuus ei perustu hajauttamiseen, Mining:ään tai salaukseen: kuten mikä tahansa järjestelmä, se perustuu yksilöihin. Tarkemmin sanottuna se riippuu solmujen käyttäjien kyvystä vastustaa pakkokeinoja.



Bitcoin:n kaltaisille hajautetuille järjestelmille on ominaista, että riski jakautuu kaikkien niiden toimintaan osallistuvien kesken. Oman Bitcoin-solmun ylläpito tarkoittaa, että hyväksyt osan tästä riskistä varmistamalla oman solmusi turvallisuuden; näin kevennät myös muiden solmujen ylläpitäjien riskitaakkaa.



Kyse ei siis ole suoranaisesta henkilökohtaisesta hyödystä: solmupisteen ylläpito asettaa sinut osittain vastuuseen verkon turvallisuudesta. Se on ennen kaikkea kollektiivinen hyöty, koska osallistumisesi auttaa jakamaan riskiä. Se puolestaan lisää omaa kykyäsi käyttää Bitcoin:tä luotettavasti.



### Syvennä järjestelmää koskevaa ymmärrystäsi



Full node:n asentaminen ei ole mikään yksinkertainen toimenpide. Siihen kuuluu ohjelmiston asentaminen, perustoimintojen ymmärtäminen, synkronoinnin valvonta, lokien tutkiminen ongelmatilanteissa ja jopa päätelaitteen käyttö. Tämä johtaa väistämättä protokollan syvällisempään ymmärtämiseen. Tämä on epäsuora, mutta ei merkityksetön etu.



Tämän tiedon hankkiminen vahvistaa luottamusta työkaluun ja voi vähentää virheriskiä tai huijauksille altistumista. Oman solmun kehrääminen on myös yksi oppimisen muoto.



### Sovellettavien sääntöjen valitseminen



Tärkeä ja usein väärinymmärretty näkökohta on se, että solmun käyttäminen antaa sinulle mahdollisuuden valita paikallisesti sovellettavat säännöt. Sääntöjä on kahta päätyyppiä:





- Konsensussäännöt**:



Nämä ovat Bitcoin-protokollan perussäännöt, joilla varmistetaan järjestelmän eheys ja vahvistetaan kriteerit transaktioiden ja lohkojen validointia varten. Mitään transaktiota, joka ei noudata näitä konsensussääntöjä, ei voida koskaan sisällyttää kelvolliseen lohkoon. Esimerkiksi transaktio, jonka yhdessä merkinnässä on virheellinen allekirjoitus, suljetaan järjestelmällisesti pois.



Näiden sääntöjen muuttaminen vastaa protokollan ja siten valuutan muuttamista (Hard Fork). Vaikka sääntöjä ei yritettäisikään muuttaa, pelkkä olemassa olevien sääntöjen tiukka soveltaminen antaa kuitenkin tietynlaisen vallan: jos lohko rikkoo sääntöjä, solmu hylkää sen välittömästi.





- Relesäännöt**:



Nämä ovat kullekin Bitcoin-solmulle ominaisia sääntöjä, jotka lisätään konsensussääntöihin, jotta voidaan määritellä Mempool:ssa hyväksyttyjen ja vertaisille välitettävien vahvistamattomien transaktioiden rakenne. Kukin solmu konfiguroi ja soveltaa näitä sääntöjä paikallisesti, mikä selittää, miksi ne voivat vaihdella solmusta toiseen. Sääntöjä sovelletaan vain vahvistamattomiin transaktioihin: solmun "epätyypilliseksi" katsoma transaktio hyväksytään vain, jos se esiintyy jo voimassa olevassa lohkossa. Näiden sääntöjen muuttaminen ei poista solmua Bitcoin-järjestelmästä.



Esimerkiksi maksuton transaktio on konsensussääntöjen mukaan täysin pätevä, mutta se hylätään oletusarvoisesti Bitcoin core:n välityskäytännön mukaisesti, koska parametrin `minRelayTxFee` arvoksi on asetettu `0.00001` (BTC/kB). Omassa solmussasi on kuitenkin mahdollista alentaa tätä rajaa, jotta voit välittää pienempiä maksuja sisältäviä transaktioita, tai päinvastoin nostaa rajaa esimerkiksi 2 Sats/vB:hen, jotta vältät pienillä maksuilla toteutettujen transaktioiden välittämisen.



Oman solmun kehrääminen tarkoittaa väittämistä: "Vahvistan sen, mitä päätän vahvistaa, itse hyväksymieni sääntöjen mukaisesti "*. Näin sinusta tulee järjestelmän hallintaan osallistuva toimija, joka voi hylätä kehityksen, jota et voi hyväksyä, tai hyväksyä päivityksen omien kriteeriensä mukaisesti.



Voimme siis nopeasti yrittää ymmärtää, kuinka paljon valtaa sinulla on sääntöihin solmusi ansiosta. Ja tämän vallan laajuus riippuu sääntötyypistä.



#### Relesäännöt



Välityssääntöjen kannalta olennaista on yksinkertaisesti solmun omistaminen riippumatta sen taloudellisesta toiminnasta. Kyse on siitä, suostutko välittämään tietyntyyppisiä liiketoimia vai et.



Jos esimerkiksi uskot, että Bitcoin:n pitäisi hyväksyä transaktiot, joiden maksut ovat alle 1 sat/vB, voit säätää tätä sääntöä solmussasi niin, että se lähettää nämä transaktiot, mikä helpottaa niiden leviämistä verkossa, kunnes Miner lopulta sisällyttää ne kelvolliseen lohkoon. Pohjimmiltaan kyse on siis vallasta transaktioiden levittämisessä: jokaisella solmulla on päätösvalta, koska suostuminen tietyn tyyppisen transaktion välittämiseen on yhtä kuin sen hyväksymisen edistäminen Bitcoin-verkossa. Jos sinulla on useita solmuja, sinulla on suurempi vaikutusvalta välityspolitiikkaan, koska jokaisella solmulla on omat yhteytensä ja vaikutusalueensa verkossa.



Kun yksi tai useampi solmu on konfiguroitu erityisten välityssääntöjen mukaisesti, on määriteltävä, mikä verkon osa hyväksyy tietyn tyyppisen tapahtuman välittämisen. Viestin levittäminen vertaisverkkograafissa, kuten Bitcoin-tapahtumien tapauksessa, noudattaa perkolaatioteorian logiikkaa. Kuvitellaan jokainen solmu sivustoksi, joka voi olla aktiivinen (`p` = se välittää) tai inaktiivinen (`1-p`). Heti kun osuus `p` ylittää kriittisen raja-arvon (`p_c`), syntyy jättiläiskomponentti: transaktio onnistuu kulkemaan verkon läpi ja sillä on kaikki mahdollisuudet saavuttaa Miner. Bitcoin:n kaltaisessa verkossa, jossa kukin solmu ylläpitää keskimäärin 8 lähtevää yhteyttä, `p_c`-kynnysarvo on yleensä vain muutama prosentti, ja se voi olla vieläkin alhaisempi, jos joillakin solmuilla on hyvin paljon yhteyksiä.



![Image](assets/fr/061.webp)



Niin kauan kuin `p` on `p_c`:n alapuolella, transaktio rajoittuu eristettyihin taskuihin eikä saavuta Miner:a. Heti kun tämä kynnysarvo ylittyy, se leviää lähes välittömästi koko verkkoon.



Viime kädessä louhijat päättävät aina, sisällytetäänkö transaktio lohkoon vai ei. Solmut kuitenkin puuttuvat asioihin ennen lohkoa vaikuttamalla transaktioiden jakautumiseen: ne päättävät, ovatko louhijat tietoisia tietystä transaktiosta vai eivät. Jos transaktiota ei välitetä louhijoille, louhijoiden on luonnollisesti mahdotonta sisällyttää sitä lohkoon.



Muutaman solmun lisäämisellä on näin ollen vain marginaalinen vaikutus, jos verkko on jo tietyntyyppisen transaktion perkolaatiovaiheessa, mutta se voi osoittautua ratkaisevaksi, kun perkolaatiokynnys lähestyy. Useiden solmujen omistaminen tai niihin vaikuttaminen, varsinkin jos ne ovat hyvin yhteydessä toisiinsa, voi lisätä tai vähentää p:n arvoa ja siten epäsuorasti ohjata välityssääntöjä, jotka määrittävät, mitkä transaktiot louhijat näkevät ja lopulta hyväksyvät.



#### Konsensussäännöt



Kun on kyse solmusi vaikutuksesta konsensussääntöihin, sen taloudellinen painoarvo on ennen kaikkea ratkaiseva. Tämä on ratkaiseva käsite: minkä tahansa valuutan arvo liittyy suoraan sen kykyyn helpottaa Exchange:ää. Jos kukaan Exchange:ssä ei hyväksy esinettä tavaroiden tai palveluiden vastineeksi, sillä ei teoriassa ole mitään rahallista arvoa. Jos esimerkiksi yksikään kauppias ei hyväksy kiviä maksuvälineeksi, niistä ei ole hyötyä rahana. Hyödyllisyys on tietysti edelleen subjektiivinen käsite yksilöllisessä mittakaavassa, mutta mitä useampi kauppias tietyllä alueella hyväksyy esineen maksuvälineenä Exchange:ssä, sitä todennäköisemmin kyseisellä esineellä on rahallinen hyöty kyseisellä alueella asuville ihmisille.



Otetaan esimerkki kylästä, jossa monet kauppiaat hyväksyvät Exchange-kultaa tavaroista: on todennäköistä, että kullasta on kyläläisille rahallista hyötyä. Tämä osoittaa, että valuutan hyöty riippuu suoraan kauppiaiden päätöksistä hyväksyä tai hylätä se.



Tämä käsite on ratkaisevan tärkeä Bitcoin-järjestelmässä vallitsevan valtadynamiikan ymmärtämiseksi. Satoshi tekee asian selväksi: Bitcoin on sähköinen käteisjärjestelmä; toisin sanoen se tarjoaa palvelun, joka tarjoaa eräänlaista valuuttaa, Bitcoin:ää (tai BTC:tä). Kun protokollan sääntöjä muutetaan tavalla, joka ei ole taaksepäin yhteensopiva (Hard Fork), tämä merkitsee uuden järjestelmän ja siten uuden valuutan luomista. Tämän Fork:n menestys tai epäonnistuminen riippuu sen talouden koosta, joka puolestaan määräytyy sen mukaan, kuinka moni kauppias hyväksyy tämän uuden valuuttamuodon.



![Image](assets/fr/062.webp)



Otetaan esimerkki: oletetaan, että Bitcoin kärsii Hard Fork:sta. Tällöin olisi 2 erilaista valuuttaa: BTC-1 (alkuperäinen, muuttumaton versio) ja BTC-2 (uusi valuutta, jossa on erilaiset konsensussäännöt). Jos kaikki kauppiaat, jotka hyväksyvät BTC-1:n, jatkavat BTC-1:n hyväksymistä, mutta hylkäävät BTC-2:n, jälkimmäisen rahallinen hyöty on teoriassa hyvin rajallinen. Käyttäjänä en olisi kiinnostunut pitämään ja käyttämään BTC-2:ta, koska tiesin, ettei yksikään kauppias haluaisi sitä Exchange:ssä tavaroihin tai palveluihin. Jos taas 50 % kauppiaista päättää hyväksyä ainoastaan BTC-2:n ja loput 50 % vain BTC-1:n, BTC-1:n hyöty on teoriassa puolittunut. Käytän termiä "teoriassa", koska hyöty on yksilötasolla subjektiivinen ja riippuu monista tekijöistä (kuten alueesta ja kulutustottumuksista), joita on vaikea ymmärtää tapauskohtaisesti.



Bitcoin:ssä "kauppiaan" rooliin, jolla tarkoitetaan mitä tahansa yksikköä, jolla on tietty taloudellinen painoarvo, kuuluvat tietenkin yritykset (fyysiset kaupat, verkkomyyntisivustot, palveluntarjoajat jne.), mutta myös Exchange-alustat, koska ne hyväksyvät Bitcoin:n Exchange:ssa muita valuuttoja vastaan, ja louhijat, koska ne hyväksyvät Bitcoin:n Exchange:ssa maksujen kautta palvelusta, joka koskee transaktion sisällyttämistä lohkoon.



Mitä tulee konsensussääntöihin, solmusi antaa sinulle mahdollisuuden suunnata taloudellista toimintaasi yhteen tai toiseen valuuttaan. Jos sinulla on esimerkiksi kotona 10 täyttä solmua, mutta ei merkittävää taloudellista toimintaa, vaikutusmahdollisuutesi Fork:n aikana on lähes olematon. Sitä vastoin yksittäinen solmu, jota käytetään 200 liikkeen ketjun hallintaan ja joka hyväksyy Bitcoin:n, antaa merkittävän taloudellisen painoarvon.



Ratkaisevaa ei siis ole solmujen määrä vaan niiden tukeman taloudellisen toiminnan merkitys. Lisäksi jos taloudellinen toimintasi riippuu solmusta, jota et hallitse, sen omistaja päättää, mitä valuuttaa käytät, niin kauan kuin olet yhteydessä kyseiseen solmuun. Tämän vuoksi oman solmun ylläpitäminen ja käyttäminen on erityisen tärkeää järjestelmän hallinnan kannalta:



> Ei sinun solmusi, ei sinun sääntösi.


## Bitcoin-solmujen eri tyypit


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Bitcoin-solmu on siis kone, jossa on Bitcoin-protokollan toteutus. Tämän solmujen yhteisen määritelmän takana on useita mahdollisia kokoonpanoja, joista kaikki eivät tarjoa samaa autonomian, resurssien kulutuksen ja hyödyllisyyden tasoa verkon kannalta. Tässä luvussa yritämme ymmärtää näitä eroja, jotta voit valita käyttötarkoitukseesi ja laitteistorajoituksiisi sopivan solmuarkkitehtuurin.



### Täydellinen solmu



Full node on yksinkertaisesti Bitcoin-solmu, joka lataa koko Blockchain-lohkon Genesis-lohkosta, validoi jokaisen lohkon itsenäisesti ja tallentaa Blockchain-lohkon historian paikallisesti. Tämä on Bitcoin-solmun "normaali" muoto, sellaisena kuin Satoshi Nakamoto sen kuvitteli.



![Image](assets/fr/063.webp)



Full node:n ei tarvitse luottaa kehenkään, koska se validoi ja tuntee kaikki järjestelmässä olevat tiedot. Se on solmutyyppi, joka antaa sinulle suurimmat takeet: tiedät ilman, että luotat kolmanteen osapuoleen, onko maksu pätevä, onko lohko pätevä, onko uudelleenjärjestely laillinen ja niin edelleen.



Käytännössä Full node vaatii huomattavia resursseja, kuten useita satoja gigatavuja lohkotiedostoja varten, prosessorin, joka pystyy validoimaan skriptejä, RAM-muistia Mempool:lle ja välimuisteille sekä vakaan kaistanleveyden. Ensimmäinen synkronointi (*IBD*) lukee ja tarkistaa koko historian: se on intensiivinen, mutta tapahtuu vain kerran. Full node osallistuu aktiivisesti verkkoon, välittää lohkoja ja transaktioita ja voi ottaa vastaan saapuvia yhteyksiä auttaakseen muita vertaisia.



Tarpeidesi mukaan voit lisätä Full node:ään indeksoijan. Bitcoin core tarjoaa tapahtumien indeksoinnin valinnaisena ominaisuutena (oletusarvoisesti pois käytöstä), joka voi olla hyödyllinen erityistarkoituksiin. Se ei kuitenkaan sisällä Address-indeksoijaa, joka on usein yksittäisten käyttäjien eniten toivoma ominaisuus. Tämän korjaamiseksi voit asentaa solmuun oman ohjelmiston, kuten Electrs tai Fulcrum, nopeuttaaksesi Address-saldon tarkistuskyselyjä siihen liittyviltä UTXOilta. Palaamme indeksoijan rooliin tarkemmin erillisessä luvussa.



### pruned-solmu



pruned-solmu validoi kaiken Full node:n tapaan Genesis-lohkosta ketjun päähän, jossa on eniten työtä, mutta **säilyttää vain lohkotiedostojen viimeisimmän osan**. Kun vanhat lohkot on tarkistettu, se poistaa ne vähitellen, jotta ne pysyvät asetettavan tilarajan alapuolella. Tämä konfiguraatio on ihanteellinen, jos levytilaa on rajoitetusti: säilytät lohkojen validoinnin riippumattomuuden tallentamatta koko Blockchain-historia-arkistoa. Tämä vaihtoehto on erityisen hyödyllinen, jos haluat vain asentaa Bitcoin core:n henkilökohtaiselle tietokoneellesi ilman, että käytät siihen tarkoitettua konetta.



![Image](assets/fr/064.webp)



Tämän vaihtoehdon tekniset vaikutukset ovat melko yksinkertaiset: pruned-solmu pystyy täysin lähettämään transaktiosi, osallistumaan releeseen, vahvistamaan lohkot ja transaktiot sekä seuraamaan ketjua. Toisaalta se ei voi toimia rajojaan laajempana historiatietojen lähteenä muille sovelluksille (esim. täydellisille etsintäohjelmille, indeksoijille, lompakoille). Toiminnot, jotka edellyttävät arkistoa (tai globaalia indeksiä), eivät siis ole käytettävissä.



Käytännössä voit käyttää pruned-solmua Wallet-hallintaohjelmiston, kuten Sparrow wallet:n, liittämiseen. Et kuitenkaan pysty skannaamaan Wallet:ssä tapahtumia, jotka ovat karsimisrajaa vanhempia. Jos esimerkiksi lohkossa 901 458 on rekisteröity tapahtuma, mutta solmusi säilyttää vain lohkoja 905 402:sta ylöspäin (koska vanhimmat lohkot ovat olleet pruned), et voi skannata tätä tapahtumaa. Toisaalta, jos olisit jo skannannut sen, kun solmussasi oli vielä tämä lohkokorkeus, Wallet-hallintaohjelmistosi tallentaa tiedot ja näyttää vastaavien UTXO:iden saldon oikein.



Lyhyesti sanottuna Wallet-seuranta toimii ongelmitta pruned-solmussa, jos luot uuden Wallet:n, kun ohjelmistosi on jo yhdistetty kyseiseen solmuun. Toisaalta saatat kohdata vaikeuksia, jos palautat vanhan Wallet:n, sillä aiempia tapahtumia, joita solmu ei enää säilytä, ei tietenkään voi hakea.



### Valosolmu / SPV



SPV-solmu (*Simplified Payment Verification*) eli kevytsolmu säilyttää vain lohkojen otsikot, ei transaktiotietoja, ja se luottaa siihen, että muut täysimittaiset solmut saavat todisteet siitä, että transaktio on lohkossa (Merkle-todisteet puiden kautta), jonka otsikko sillä on. Yksinkertaistetun maksujen todentamisen käsite ei ole uusi, sillä Satoshi Nakamoto itse ehdotti sitä valkoisen kirjan osassa 8.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Tämäntyyppinen solmu on selvästi paljon kevyempi tallennustilan ja suorittimen käytön kannalta kuin Full node- tai jopa pruned-solmu. SPV-solmu soveltuu siksi hyvin pienemmille laitteille ja ajoittaisille yhteyksille. Itse asiassa se on usein integroitu suoraan Wallet:een, erityisesti mobiilipuolen ohjelmistoon, kuten Blockstream App -sovellukseen.



Kompromissi on luottamus ja luottamuksellisuus: SPV-asiakas ei tarkista itse skriptejä tai validointikäytäntöjä; se olettaa, että ketju, jossa on eniten työtä, on voimassa, ja on riippuvainen yhdestä tai useammasta täydestä solmusta vastausten saamiseksi. Tämäntyyppisen solmun käyttäminen on siis parempi vaihtoehto kuin yhteyden muodostaminen kolmannen osapuolen solmuun; se on kuitenkin edelleen vähemmän edullinen kuin Full node- tai jopa pruned-solmun käyttäminen.



![Image](assets/fr/065.webp)



### Mikä solmu mihin tarpeeseen?





- Mobiili / aloitteleva käyttäjä



Aloittelevalle käyttäjälle, jolla on vain Wallet mobiilisovelluksella, SPV-solmun käyttö on varmasti paras tapa päästä alkuun. Asennus on nopea, vaatii vain vähän resursseja ja käyttökokemus on yksinkertainen ja sujuva. Tämä tarkoittaa, että voit itse tarkistaa tietyt tiedot ja siten luottaa vähemmän kolmansien osapuolten solmuihin ja olla samalla riippumattomampi, kun kyse on transaktioiden lähettämisestä.





- PC / keskitason käyttäjä



Keskitason käyttäjä, jolla on tietokone, voi asentaa pruned-solmun ja hyötyä lähes kaikista Full node:n eduista kuormittamatta konettaan päivittäin: täysi validointi, kohtuullinen levynkäyttö ja yksinkertainen ylläpito. Se on ihanteellinen ratkaisu työpöydän lompakoiden yhdistämiseen ja itsenäisyyden säilyttämiseen transaktioiden jakelussa investoimatta omaan koneeseen tai ylikuormittamatta levytilaa.





- Valtiollinen Bitcoiner / kehittynyt



Full node on edelleen paras ratkaisu, jos haluat olla täysin riippumaton Bitcoin:n käytössä etkä rajoittaa itseäsi myöhemmin edistyneempiin käyttötarkoituksiin, kuten indeksointiin, Lightning-solmuun tai jopa Block explorer:een. Juuri tätä aiomme tutkia tällä kurssilla!



## Katsaus ohjelmistoratkaisuihin


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Ohjelmistopuolella on kaksi päätapaa käyttää Bitcoin-solmua:




- asenna suoraan protokollan toteutus, kuten Bitcoin core (suositeltava) tai Bitcoin Knots,
- tai käyttää avaimet käteen -jakelua (usein "solmu laatikossa"), joka integroi Bitcoin-toteutuksen samalla tavalla, mutta sisältää myös Interface-hallintajärjestelmän, sovelluskaupan ja valmiita työkaluja (Lightning, selaimet, indeksipalvelimet, jopa Bitcoin:n ulkopuoliset sovellukset...).



Molemmat lähestymistavat johtavat samaan tavoitteeseen: oman solmun saamiseen, mutta ne eroavat toisistaan Interface:n asennuksen ja käytön, ylläpidon, laajennettavuuden ja kustannusten osalta. Tätä tarkastelemme tässä luvussa.



### Raaka Bitcoin-solmutoteutukset



Raakatoteutuksen asentaminen tarkoittaa Bitcoin-protokollan toteutuksen (kuten Core) ohjelmiston suoraa käyttöä ilman lisäohjelmistoa Layer. Hallitset itse konfigurointia, päivityksiä ja niihin liittyviä palveluja (indeksointi, API, Lightning, varmuuskopiot jne.) omien tarpeidesi mukaan.



Tämä on kaikkein suvereenein ja joustavin lähestymistapa: tiedät tarkalleen, mikä on käynnissä, missä tiedot ovat ja miten kaikki toimii. Toisaalta se muuttuu monimutkaisemmaksi heti, kun haluat mennä Bitcoin-solmun yksinkertaista toimintaa pidemmälle. Jos tavoitteena on vain solmu, monimutkaisuus on verrattavissa node-in-a-boxin monimutkaisuuteen tai jopa vähemmän monimutkaista, koska kyse on vain ohjelmiston asentamisesta.



#### Bitcoin core (erittäin suuri enemmistöasiakas)



[Bitcoin core on verkon ylivoimainen enemmistöasiakas](https://bitcoincore.org/). Se lataa, validoi ja ylläpitää Blockchain:ää, tarjoaa RPC/REST API:t ja voi integroida Wallet:n. Jos pidät enemmän vakiotyökaluista ja tunnet olosi mukavaksi lisätä palveluja itse (kuten Electrum-palvelin, explorer ja LND), sinun on parempi käyttää Corea sellaisenaan.



**Hyötyjä:** Maksimaalinen vakaus, ennustettava käyttäytyminen, raaka kokemus, helppo asentaa ja konfiguroida.



**Haitat:** Sinun on rakennettava loput pinosta manuaalisesti luodaksesi täydellisen sovellusympäristön Bitcoin-solmun sijaan.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (tärkein vaihtoehtoinen asiakas)



[Bitcoin Knots on Bitcoin core:n Fork](https://bitcoinknots.org/), jota ylläpitää Luke Dashjr. Se on tärkein vaihtoehtoinen asiakasohjelma Core:lle Bitcoin-protokollan toteuttamiseksi. Se on täysin yhteensopiva muun verkon kanssa (se ei missään nimessä ole Hard Fork kuten Bitcoin Cash), mutta tarjoaa kuitenkin lisäominaisuuksia, kuten välityskäytäntövaihtoehtoja, jotka puuttuvat Core:sta tai joita sovelletaan oletusarvoisesti tiukemmin joidenkin mielestä roskapostin rajoittamiseksi.



On kaksi mahdollista syytä valita Knots Coreen nähden:




- Tekniikat**: Määrittämällä, mitkä tapahtumat solmusi hyväksyy ja lähettää.
- Politiikka**: Jotkut haluavat käyttää vaihtoehtoisia asiakkaita, kuten Knotsia, muista kuin teknisistä syistä, erityisesti tukeakseen vaihtoehtoa Core-ohjelmalle ja vähentääkseen siten sen monopolia. Jos Core joskus vaarantuisi, olisi hyödyllistä, että olisi paitsi vankkoja, hyvin ylläpidettyjä vaihtoehtoisia asiakkaita, myös tietoa siitä, miten niitä käytetään tehokkaasti. Toiset käyttävät Knotsia protestitarkoituksessa, koska he ovat menettäneet luottamuksensa Coren kehittäjiin tai eivät hyväksy suurinta osaa asiakkaan hallinnosta.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Suosittelen henkilökohtaisesti valitsemaan Core-version, lähinnä siksi, että voit hyötyä tietoturvakorjauksista nopeammin. Jotkin Knotsissa havaitut haavoittuvuudet korjataan nimittäin viiveellä. Yleisemmin Core-kehitysprosessi on vakaasti jäsennelty ja sitä tukee suuri määrä tekijöitä, kun taas Knotsia ylläpitää yksi henkilö ja sen yhteisö on paljon pienempi. Toisaalta relesäännöt menettävät nykyään usein hyödyllisyytensä, varsinkin kun niitä soveltaa vain pieni osa verkosta (kuten perkolaatioteoriassa).



### Node-in-a-box-jakelut



_node-in-a-box_ yhdistää Bitcoin core:n (tai Knotsin) valmiiksi konfiguroituun käyttöjärjestelmään, Interface Webiin ja App Store -sovelluskauppaan, jossa on itsepalvelupalveluja (Lightning, explorers, Electrum-palvelin, Mempool, BTCPay Server, Nextcloud jne.). Yhdellä napsautuksella voit asentaa, päivittää ja yhdistää nämä eri moduulit toisiinsa.



Se on paljon yksinkertaisempi ratkaisu lukuisten oheissovellusten päivittäiseen käynnistämiseen ja hallintaan. Huonona puolena on se, että ongelman ilmaantuessa (esim. Docker-kuvauskonflikti, virheellinen päivitys, vioittunut tietokanta) vianmäärityksestä voi tulla hyvin monimutkaista, koska olet riippuvainen jakelun omasta integroinnista. Lisäksi yhteisön tai virallinen tuki on usein monimutkaista.



Node-in-a-box on siis erittäin helppokäyttöinen, kunhan kaikki toimii kunnolla, mutta vian sattuessa sinun on oltava valmis suorittamaan pitkiä etsintöjä, odottamaan apua ja likaamaan kätesi.



Useimmat näistä ratkaisuista ovat saatavilla kahdessa muodossa:




- Valmiiksi koottu kone: täydellinen tietokone, johon on jo asennettu käyttöjärjestelmä. Nämä maksulliset koneet on vain kytkettävä verkkovirtaan ja liitettävä Internetiin, jotta ne ovat toiminnassa. Jos budjetti sallii, tämän vaihtoehdon etuna on, että se on hyvin helppo ottaa käyttöön, ja se tarjoaa usein ensisijaista tukea ja osallistuu kehityksen rahoittamiseen, sillä näiden yritysten liiketoimintamalli perustuu yleensä laitteiston myyntiin.
- DIY: asenna jakelu-käyttöjärjestelmä omalle koneellesi (vanha PC, NUC, Raspberry Pi, kotipalvelin...). Tämä on taloudellisin ratkaisu, sillä voit kierrättää vanhan koneen tai valita juuri sinun tarpeitasi ja budjettiasi vastaavan laitteiston. Se on myös joustavin vaihtoehto, ja sen konfigurointi on miellyttävintä. Tutustumme tähän lähestymistapaan kurssin käytännön osuudessa.



Seuraavassa on yleiskatsaus tärkeimpiin saatavilla oleviin node-in-a-box-ratkaisuihin (vuonna 2025):



### Umbrel (umbrelOS & Umbrel Home)



[Nykyään Umbrel on johtava node-in-a-box-ratkaisujen toimittaja (https://umbrel.com/). Sen menestys johtuu suurelta osin sen asennuksen yksinkertaisuudesta (kun se lanseerattiin yksinkertaisella Raspberry Pi -laitteella), sen tyylikkäästä ja intuitiivisesta Interface:stä sekä sovellusten ekosysteemistä, joka on kasvanut nopeasti ja on nyt erittäin laaja.



![Image](assets/fr/067.webp)



Vuonna 2020 yksinkertaisena Bitcoin-solmuna ja muutamana oheissovelluksena markkinoille tuotu Umbrel on vähitellen kehittynyt nykyaikaiseksi ja monipuoliseksi kotipilveksi.



En käsittele tässä yksityiskohtaisemmin, miten se toimii ja mitkä ovat sen erityispiirteet, sillä tarkastelemme niitä tarkemmin seuraavan osan ensimmäisessä luvussa. Olenkin valinnut tämän BTC 202 -kurssin tarkoituksiin UmbrelOS:n, joka on mielestäni paras nykyinen node-in-a-box -ratkaisu aloitteleville ja keskitason käyttäjille.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 tarjoaa StartOS-järjestelmää (https://start9.com/), joka on suunniteltu "suvereeniin tietojenkäsittelyyn": tavoitteena on, että jokainen voi omistaa ja hallita omaa yksityistä palvelinta, jota täydennetään itse isännöityjen sovellusten markkinapaikalla. Voit ostaa Start9-palvelimen (Server One 619 dollaria, Server Pure 899 dollaria) tai koota oman palvelimesi DIY-tilassa omalle koneellesi.



Bitcoin:n puolella StartOS:n avulla voit asentaa Full node:n, Lightning-solmun, BTCPay-palvelimen, Electrs:n ja monia muita palveluja. Start9:n vetovoima ulottuu kuitenkin tätä pidemmälle: se tarjoaa mahdollisuuden löytää, konfiguroida ja paljastaa erilaisia ohjelmistoja (tiedostopilvi, viestinvälitys, seuranta) yhtenäisellä tavalla ja täydellä hallinnalla. Hanke on siis suunnattu käyttäjille, jotka haluavat vankan itsepalvelualustan, eivät pelkkää Bitcoin-solmua. Se on luultavasti Umbrelin jälkeen täydellisin ekosysteemi.



![Image](assets/fr/068.webp)



Suurin ero Umbreliin on Interface:ssä. Umbrel luottaa pitkälle hiottuun käyttöliittymään, kun taas Start9 tarjoaa karkeamman ja toimivamman Interface:n. Start9:n sovellusekosysteemi ei ole yhtä rikas kuin Umbrelin, mutta se kompensoi tämän useilla teknisillä eduilla: pääsy sovellusten lisäasetuksiin on yksinkertaisempaa, kun taas Umbrel muuttuu nopeasti rajoittavaksi, jos haluttua vaihtoehtoa ei ole tarjolla Interface:ssä. Start9 on ylivoimainen myös varmuuskopioiden hallinnassa: Umbrelin LND:n tehokasta ratkaisua lukuun ottamatta ei ole olemassa yhtenäistä mekanismia, toisin kuin Start9:ssä. Lisäksi se tarjoaa helpommin saatavilla olevia valvontatyökaluja ja salatun etäyhteyden (`https`), kun taas paikallinen yhteys Umbreliin toimii `http`:n kautta.



Lyhyesti sanottuna, jos tarvitset vain olennaiset sovellukset Bitcoin:lle, etkä ole erityisen kiinnostunut Umbrelin erittäin rikkaasta ekosysteemistä ja Interface-käyttäjä ei ole ensisijainen, Start9 on parempi vaihtoehto. Muussa tapauksessa Umbrel on parempi valinta.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode on jakelu, joka on keskittynyt yksinomaan Bitcoin:een ja Lightningiin](https://mynodebtc.com/), ja se tarjoaa Interface-verkkopalvelun, sovellusten markkinapaikan ja päivitykset yhdellä napsautuksella. Voit joko ostaa valmiin laitteiston (*Model Two* saatavilla 549 dollarilla) tai asentaa MyNoden ilmaiseksi omalle koneellesi. Projekti tarjoaa myös *Premium*-version ohjelmistosta (94 dollaria), joka sisältää ensisijaisen tuen ja lisäominaisuuksia.



![Image](assets/fr/069.webp)



Käytännössä MyNode kokoaa yhteen kaikki Full node:n käyttämiseen tarvittavat perusrakennuspalikat sekä Bitcoin:n käyttäjille välttämättömät sovellukset. Siksi se on sopiva ratkaisu, jos et tarvitse Bitcoin-ekosysteemin ulkopuolisia sovelluksia, kuten Start9- ja Umbrel-järjestelmistä löytyviä itse isännöityjä sovelluksia.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz on 100% avoimen lähdekoodin projekti](https://docs.raspiblitz.org/) (MIT-lisenssi) Bitcoin-solmun ja Lightning-solmun asentamiseen Raspberry Pi:hen. Lataa kuva, käynnistä se ja seuraa ohjattua ohjelmaa, jotta saat Raspberry Pi:ssäsi toimivan node-in-a-boxin. Myös kolmansilta osapuolilta on saatavana valmiiksi koottuja sarjoja, yleensä 300-400 dollarin hintaan laitteistosta riippuen. RaspiBlitz tarjoaa myös valikoiman helposti asennettavia lisäsovelluksia.



![Image](assets/fr/070.webp)



Jos omistat Raspberry Pi:n, tämä on erinomainen vaihtoehto, sillä Umbrelin kaltaiset täydellisemmät järjestelmät ovat yhä raskaampia tämäntyyppisille mini-PC:ille.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo on yksityisyyden suojaan keskittyvä node-in-a-box](https://wiki.ronindojo.io/en/home), joka automatisoi Samurai Dojon ja Whirlpool:n käyttöönoton, jossa on oma Interface ja lisäosia, jotka on suunniteltu erityisesti Samurai-ekosysteemiä varten.



Periaate on yksinkertainen: jos käytät Ashigaru Wallet:ta (Samurai Wallet:n seuraaja Fork:n kehittäjien pidättämisen jälkeen) tai jos haluat hyötyä kehittyneistä yksityisyydensuojatyökaluista, RoninDojo on sinua varten.



![Image](assets/fr/071.webp)



Hankkeessa tarjottiin aiemmin valmiiksi konfiguroitua konetta nimeltä Tanto, mutta se ei ole tällä hetkellä saatavilla. Se saattaa palata myöhemmin. Sillä välin RoninDojo on mahdollista asentaa helposti Rock5B+- tai Rockpro64-koneeseen tai jopa epäsuorasti Raspberry Pi -koneeseen.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Toinen [node-in-a-box -ratkaisu on Nodl](https://www.nodl.eu/). Kuten edellisissä hankkeissa, voit joko ostaa valmiiksi konfiguroidun laitteiston (599-799 euroa mallista riippuen) tai asentaa sen itse DIY-tilassa.



Ohjelmistopuolella Nodl integroi Bitcoin core:n, LND:n, BTCPay Serverin, Electrs:n, Dojon, Whirlpool:n, Lightning Terminalin, RTL:n sekä BTC RPC Explorerin, kaikki integroidulla päivitysketjulla ja MIT-lisenssin mukaisella avoimen lähdekoodin koodilla.



![Image](assets/fr/072.webp)



Kun olet tutustunut erilaisiin ohjelmistoratkaisuihin, nyt on aika valita kone, joka isännöi solmua!




## Laitteistoratkaisujen yleiskatsaus


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nyt kun olemme tutustuneet kaikkiin ohjelmistomahdollisuuksiin, keskitymme solmun vaatimaan laitteistoon. Annan sinulle konkreettisia neuvoja komponenttien valintaan sekä eri budjeteille räätälöityjä kokoonpanoja. Tämä on tietenkin henkilökohtainen mielipiteeni ja palautteeni: tässä esiteltyjen vaihtoehtojen lisäksi on varmasti muitakin relevantteja vaihtoehtoja. En myöskään käsittele uudelleen node-in-a-box-projektien tarjoamia valmiiksi koottuja koneita, joita käsittelimme jo edellisessä luvussa. Tässä keskitymme yksinomaan DIY-ratkaisuihin.



### Tarvitsetko todella oman koneen?



Viime vuosina bitcoin-asiakkaat ovat tulleet yhä tietoisemmiksi yleisestä harhaluulosta, erityisesti node-in-a-boxin yleistyttyä 2020-luvun alussa: Bitcoin-solmun pitäisi välttämättä toimia koneessa, joka on omistettu yksinomaan tähän tarkoitukseen. Tämä ei kuitenkaan pidä paikkaansa. Bitcoin-solmun käyttämiseen ei välttämättä tarvita omaa tietokonetta: Bitcoin core:ta voi täysin hyvin käyttää jokapäiväisessä tietokoneessa. Jos sinulla on riittävästi levytilaa Blockchain:lle tai otat karsinnan käyttöön, voit vahvistaa ketjun, kytkeä Wallet:n ja jopa sulkea ohjelman, kun olet lopettanut sen käytön. Tämän lähestymistavan etu on huomattava: nolla alkuinvestointia ja minimaalinen monimutkaisuus.



![Image](assets/fr/074.webp)



Erityisen koneen käyttö on kuitenkin usein mukavampaa. Se voi toimia jatkuvasti (24/7), siihen voi olla etäyhteys koko ajan, se ei vie pääkoneesi resursseja ja ennen kaikkea se voi eristää käyttötarkoitukset (hyvä turvallisuuskäytäntö: jos henkilökohtaisessa tietokoneessasi ilmenee ongelma, solmusi jatkaa toimintaansa ja päinvastoin). Kysymys ei siis ole "Tarvitsenko oman koneen?" vaan pikemminkin "Tarvitsenko solmun, joka on jatkuvasti verkossa, johon muut laitteet pääsevät käsiksi ja joka pystyy kehittymään?" (Lightning, indeksoijat, lisäsovellukset...). Jos vastaus on kyllä, erillisen koneen valitseminen tekee asioista paljon yksinkertaisempia.



### 3 hankintamenetelmää: kierrätys, käytetty ja uusi



#### Vanhan tietokoneen kierrätys



Se on taloudellisin ratkaisu. Useimmilla meistä on vanha PC, joka kerää Dust:ää kotona tai ystävien ja perheenjäsenien luona: tämä on täydellinen tilaisuus ottaa se uudelleen käyttöön! Jos haluat mukauttaa sen käytettäväksi Bitcoin-solmuna, lisää yksinkertaisesti 2TB SSD-levy ja tarpeidesi mukaan vaihda tai lisää RAM-palkkeja RAM-muistin lisäämiseksi. Voit odottaa maksavasi 100-200 euroa täysin toimivasta koneesta.



Tarkista ennen laitteiston ostamista käytettävissä olevien levypaikkojen määrä, liitäntätyyppi (M.2 tai SATA), RAM-muistin muoto (SODIMM tai DIMM) ja sukupolvi (DDR4 jne.). Kannattaa myös käyttää tilaisuutta hyväkseen ja puhdistaa kone ja erityisesti tuuletin optimaalisen suorituskyvyn varmistamiseksi.



Ole kuitenkin varovainen, jos käytät kannettavaa tietokonetta: akku voi ajan mittaan muodostua ongelmaksi (tästä lisää myöhemmin tässä luvussa).



#### Kunnostetut tai käytetyt



Markkinat ovat täynnä kunnostettuja yrityskäyttöön tarkoitettuja minitietokoneita, kuten *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* tai *Dell OptiPlex Micro*. Nämä koneet ovat vankkoja, kompakteja, hiljaisia ja energiatehokkaita. Niiden hinta on selvästi alle uuden, ja on helppo löytää 6.-10. sukupolven i5/i7-prosessoreilla ja 8-16 Gt:n RAM-muistilla varustettuja malleja erittäin edulliseen hintaan, joka on yleensä 70-200 euroa kokoonpanosta riippuen. Mielestäni tämä on todennäköisesti paras vaihtoehto, jos etsit Bitcoin-solmulle tarkoitettua konetta.



![Image](assets/fr/075.webp)



On myös mahdollista löytää muutaman vuoden takaisia käytettyjä tietokoneita ja kannettavia tietokoneita, joissa on mielenkiintoisia kokoonpanoja ja erinomainen hinta-laatusuhde.



**Huomautus:** Yritysten laitteissa, kuten *ThinkCentre Tiny*:ssa, on usein vain *DisplayPort* (DP) -portti näyttöä varten, eikä HDMI-ulostuloa. Älä siis unohda ottaa mukaan sovitinta tai DP-HDMI-kaapelia, jos tarvitset sellaista.



#### Uuden ostaminen



Jos budjettisi sallii, voit myös valita uuden koneen. Tämä on hyvä vaihtoehto, jos haluat uusimman laitteiston, jolla on hyvä suorituskyky, varsinkin jos aiot käyttää Umbrelia tai Start9:ää ja Bitcoin-ekosysteemin ulkopuolisia lisäsovelluksia itseisännöintiin.



### Minkä tyyppinen kone minun pitäisi valita?



#### Mini-PC "NUC" / barebone-tietokoneet



Minitietokoneet tarjoavat mielestäni parhaan kompromissin Bitcoin-solmun isännöintiin kotona. Ne säästävät tilaa, mahtuvat helposti hyllyyn, kuluttavat vain vähän virtaa ja niihin on helppo tehdä laitteistomuutoksia, kuten lisätä RAM-muistia tai vaihtaa SSD-levy.



Itse suosin *Lenovo ThinkCentre Tiny*:tä, joka on hyvin yleinen käytetyillä markkinoilla (yritysten kalustossa); ne ovat erityisen vankkoja ja helposti muunneltavia. Muiden valmistajien vastaavia laitteita on tietysti paljon: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Highlights:** Pieni tilantarve, kohtuullinen virrankulutus, alhainen melutaso, skaalautuvuus (mallista riippuen) ja luotettavuus.



**heikkoudet:** hieman kalliimpi kuin Raspberry Pi-tyyppinen SBC, ei sisäänrakennettua näyttöä (etäkäyttö tai ulkoisen näytön kautta), ei akkua (äkillinen sammuminen sähkökatkoksen sattuessa).



#### Oma kannettava tietokone



Se on erinomainen edullinen vaihtoehto mini-PC:lle: nykyään voit löytää edullisesti käytettyjä tai jopa uusia kannettavia tietokoneita, joissa on kunnon prosessorit, lukuisia portteja sekä integroitu näyttö ja näppäimistö (erittäin käytännöllinen ensiasennuksessa). Ennen kaikkea akku toimii luonnollisena UPS:nä: sähkökatkoksen sattuessa solmu ei sammu äkillisesti, vaan se voi pysyä toiminnassa jopa useita tunteja.



![Image](assets/fr/076.webp)



**Highlights:** All-in-one-ratkaisu, akku toimii UPS:nä (ei sähkökatkoksia), yksinkertaistettu asennus integroidun näytön ja näppäimistön ansiosta, integroitu Wi-Fi-kortti ja laaja valikoima käytettyjä ja uusia markkinoita (mikä usein tarkoittaa, että voit neuvotella hinnoista).



**heikkoudet:** hieman suurempi virrankulutus kuin pelkällä Mini-PC:llä, akun asteittainen kuluminen 24/7-käytössä ja kapasiteetin menetys, harvinainen mutta todellinen riski akun turpoamisesta tai lämpökatkosta iän myötä. Lähinnä tämä seikka saa minut pitämään mini-PC:tä parempana vaihtoehtona kuin kannettavaa tietokonetta: akun asteittainen kuluminen ja siihen liittyvät riskit.



Jos valitset tämän ratkaisun, suosittelen tarkkailemaan tarkasti akun kuntoa vaarojen välttämiseksi. Tarkkaile liiallista kuumuutta, epätavallisia hajuja, epävakautta tai muodonmuutoksia kuoressa. Hälytyksen sattuessa sammuta ja irrota tietokone välittömästi pistorasiasta ja hävitä akku sitten siihen erikoistuneessa kierrätyslaitoksessa.



**Vinkki:** Jos BIOS/UEFI tai valmistajan työkalu sallii sen, aseta kuormitusraja (esim. 60 % tai 80 %) akun käyttöiän pidentämiseksi.



#### Vadelma Pi ja muut SBC: väärä ajatus



2020-luvun alussa node-in-a-box-ohjelmistojen yleistymisen myötä myös Raspberry Pi -villitys syntyi keinona käyttää Bitcoin-solmua. Ajatus vaikutti houkuttelevalta: edullinen, kompakti ja helppokäyttöinen.



![Image](assets/fr/073.webp)



Käytännössä, jos tavoitteena on vain Bitcoin-solmun käyttäminen ilman lisäsovelluksia, Raspberry Pi voi olla riittävä. Mutta heti kun haluat käyttää Umbrelia, Start9:ää tai monipuolisempaa ekosysteemiä (Block explorer, Address-indeksoija, Lightning-solmu, itse isännöiviä sovelluksia...), kone saavuttaa nopeasti rajansa.



Raspberry Pi:llä on useita haittoja:




- liian ohuet prosessorit, joiden ARM-arkkitehtuuri on joskus yhteensopimaton tiettyjen ohjelmistojen kanssa tai vaatii enemmän käsittelyä;
- Juotettu RAM-muisti, jota on mahdotonta päivittää ja jonka kokoonpanot ovat rajalliset (usein enintään 8 Gt);
- ulkoiset laatikot SSD-asemille, jotka on liitetty kaapelilla, usein vikojen lähteitä, jotka edellyttävät erityisen kortin ostamista vakaan SSD-aseman saamiseksi;
- taipumus kuumentua nopeasti ja vaikeus varmistaa oikea jäähdytys;
- tarvitse hankkia lisälaitteita (kotelo, tuuletin, SSD-kortti jne.);
- hyvin rajalliset yhteydet.



Raspberry Pi:n kaltaisten SBC-koneiden suuri etu on ollut niiden hinta: muutaman kymmenen euron hintaan sai oman koneen. Nykyään hinnat ovat kuitenkin nousseet jyrkästi, ja kun olet lisännyt kaikki olennaiset lisälaitteistot, kustannukset lähestyvät ensimmäisten käytettyjen tai kunnostettujen x86-minitietokoneiden hintoja, jotka tarjoavat mielestäni paljon enemmän etuja. Tästä syystä en suosittele valitsemaan SBC:tä.



### Komponenttien valitseminen



#### Levytallennus: SSD pakollinen, vähintään 2 TB



Teknisesti on mahdollista käyttää Bitcoin-solmua kiintolevyllä. Ongelmana on, että kaikki hidastuu huomattavasti, erityisesti IBD, josta tulee erittäin pitkä, koska Bitcoin core käyttää levyä intensiivisesti välimuistina (erityisesti UTXO-sarjan osalta). Tämän vuoksi suosittelen vahvasti kiintolevyn käyttöä: se luo todellisen pullonkaulan, rajoittaa huomattavasti tulevaa kehitystä (esim. Lightning-solmua varten) ja saattaa jopa johtaa synkronointivirheeseen Blockchain-pään kanssa. Lisäksi mekaanisen levyn jatkuva rasitus lisää ennenaikaisen kulumisen riskiä.



SSD-levyt muuttavat käyttökokemusta radikaalisti: kaikki muuttuu nopeammaksi ja sujuvammaksi, ja luotettavuus on paljon parempi. SSD-levyn käyttö on siis (lähes) pakollista solmupisteessäsi, etkä tule katumaan sitä, varsinkin kun suurikapasiteettiset mallit ovat nyt suhteellisen edullisia.



![Image](assets/fr/077.webp)



Kapasiteetin osalta 2 Tt on vähitellen vakiinnuttamassa asemaansa uutena kohtuullisena vähimmäistilavuutena. Kesällä 2025 Blockchain lähestyy jo 700 Gt:tä, ja jos siihen lisätään Umbrel, Address-indeksoija ja muutama sovellus, 1 TB:n SSD-levy on nopeasti kyllästynyt. Kun käytössäsi on 2 TB, sinulla on mukava marginaali tuleviksi vuosiksi (karkeasti arvioituna 5 ja 15 vuoden välille). Voit valita myös 4 TB:n, jos aiot käyttää Umbrelissa monia sovelluksia, tallentaa suuria tiedostoja itseisännöinnissä tai jos haluat ennakoida levytilantarpeesi suurelta osin.



![Image](assets/fr/078.webp)



Muoto riippuu koneesi käytettävissä olevista porteista, mutta jos mahdollista, suosittelen käyttämään NVMe M.2 SSD -levyä.



#### Muisti (RAM): rAM-muisti: 8-16 GB



Pelkän Bitcoin core:n (ilman Umbrel-päällystettä) osalta kehittäjien suositusten mukaan RAM-muistia tarvitaan vähintään 256 Mt, kun asetukset on säädetty alimmalle asetukselle, 512 Mt oletusasetuksilla ja 1 Gt normaalikäytössä.



Toisaalta, jos käytät Umbrelin tai Start9:n kaltaista node-in-a-box-järjestelmää, RAM-muistivaatimukset ovat huomattavasti suuremmat. Umbrelin kehittäjät suosittelevat vähintään 4 Gt RAM-muistia. Tämä saattaa riittää pelkän Core-ohjelman käyttämiseen, mutta pian se on rajallinen. Siksi he suosittelevat 8 Gt:tä, jota pidän myös vähimmäismääränä Bitcoin:n ympärillä olevalle peruskokoonpanolle (Core, LND, indeksoija ja muutama sovellus). Kokemukseni mukaan Umbrelin ja muutaman lisäpalvelun kanssa 8 Gt on silti hieman niukka. Jos haluat olla todella mukava ja saada jonkin verran liikkumavaraa, suosittelen 16 GB RAM-muistia.



#### Prosessori (CPU)



Umbrel-solmun vähimmäisvaatimuksena on kaksiytiminen 64-bittinen Intel- tai AMD-prosessori. Jos haluat käyttää Bitcoin core:n lisäksi muutamaa sovellusta, neliytiminen (tai korkeampi) prosessori tekee todellisen eron sujuvuuden kannalta. Esimerkiksi 6.-10. sukupolven i5/i7-prosessorit ovat erinomaisia vaihtoehtoja käytettyjen markkinoilla.



### Esimerkkejä konkreettisista kokoonpanoista



Seuraavassa ehdotan kolmea konkreettista kokoonpanoa, jotka on mukautettu erilaisiin budjetteihin ja tarpeisiin, sekä täsmällisiä malleja niiden tueksi. Nämä valinnat ovat esimerkkejä, jotka havainnollistavat tämän luvun tietoja; sinun ei ole pakko valita juuri näitä malleja. Koska pidän Mini-PC:tä pitkällä aikavälillä parhaana vaihtoehtona, käytän tätä muotoa kolmessa ehdotetussa kokoonpanossa.



*Alla esitetyt hinnat ovat vain suuntaa-antavia, ja ne voivat vaihdella alueittain, myyjittäin ja ajanjaksoittain*



Ennen kaikkea tarvitset SSD-aseman, joka on tarpeeksi suuri Blockchain:lle, mutta jättää silti liikkumavaraa. SSD-levyjen käyttöikä on rajallinen kirjoitussyklien ja kirjoitettujen tietojen kokonaismäärän osalta. Bitcoin-solmu kuormittaa kuitenkin levyä merkittävästi kirjoitettaessa. Siksi en suosittele lähtötason malleja; sen sijaan suosittelen NVMe SSD:tä, joka tarjoaa huomattavasti paremman suorituskyvyn.



Esimerkkinä olen valinnut tämän kurssin tarkoituksiin seuraavan mallin: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, saatavilla noin 120 eurolla Amazonista. Voit valita myös muita tunnettuja merkkejä, kuten Crucial, Western Digital tai Kingston.



![Image](assets/fr/046.webp)



#### Low-budget kokoonpano



Jos budjettisi on hyvin rajallinen (alle 200 euroa), suosittelen tietenkin, ettet investoi erilliseen koneeseen, vaan asennat Bitcoin core:n suoraan jokapäiväiseen tietokoneeseesi (pruned-tilassa, jos levytilaa ei ole riittävästi).



Muuten suosittelen aloittelevalle budjetille *HP EliteDesk 800 G2 Mini -tietokonetta*. Löysin Amazonista 96 euron hintaan kunnostetun mallin, joka on varustettu 6. sukupolven Intel Core i5 -suorittimella ja 8 Gt RAM-muistilla. Tämä on erityisen mielenkiintoinen vaihtoehto aloittelijoille: tämä prosessori ja tämä määrä muistia ovat enemmän kuin riittävät käyttämään Core on Umbrelia sekä useita sovelluksia samanaikaisesti, kuten Electrs-indeksoijaa, Lightning-solmua ja Mempool-instanssia, kunhan Coreen ei varata liikaa välimuistia. Lisäksi tämäntyyppisen mini-PC:n avulla RAM-muistia on helppo lisätä esimerkiksi 16 gigatavuun, jos tarvetta ilmenee (varaudu maksamaan noin 30-40 euroa lisää yhdestä tai kahdesta laadukkaasta muistitikusta).



![Image](assets/fr/045.webp)



Lisää sitten SSD-levy yksinkertaisesti budjettiin. Kun aloitamme Samsungin 2TB:n 120 eurolla, saamme kokonaiskustannuksiksi 216 euroa täydelliselle, toimivalle koneelle.



#### Keskisuuren budjetin kokoonpano



Jos sinulla on keskimäärin noin 300 euron budjetti koneeseen, joka isännöi solmua, suosittelen esimerkiksi *Lenovo ThinkCentre Tiny*:tä, jossa on tehokas prosessori ja riittävästi RAM-muistia. Löysin Amazonista 180 euron hintaan kunnostetun mallin, jossa on 6. sukupolven Intel Core i7 -suoritin ja 16 Gt RAM-muistia. Kun mukaan lisätään 2TB SSD-levy 120 eurolla, kokonaishinnaksi tulee 300 euroa.



![Image](assets/fr/044.webp)



Tämän koneen avulla saat mukavan kokoonpanon: nopean IBD:n ja kyvyn käyttää lukuisia sovelluksia Umbrelissa tai Start9:ssä ilman vaikeuksia. Juuri tätä kokoonpanoa käytän tällä BTC 202 -kurssilla.



#### High-end-kokoonpano



Suuremmalla budjetilla mahdollisuudet ovat huomattavasti laajemmat. Voit valita DIY-kokoonpanon tai jopa valita suoraan node-in-a-box-projektin tarjoaman valmiiksi kootun koneen.



Esimerkiksi *ASUS NUC 14 Pro* on saatavilla uutena Amazonista 540 euron hintaan. Tähän hintaan saat Intel Core Ultra 5 -suorittimen (tuore ja erityisen suorituskykyinen), jonka mukana on 16 Gt DDR5-muistia. Tällaisella kokoonpanolla pystyt suorittamaan IBD:n ennätysajassa ja asentamaan vaativia sovelluksia ongelmitta.



Tämä on erittäin mukava kokoonpano, jopa ylivoimainen, jos alkuperäinen tavoite on vain Bitcoin-solmun käyttäminen. Toisaalta, jos haluat hyödyntää kaikkia Umbrelissa ja Start9:ssä saatavilla olevia itse isännöiviä sovelluksia, tämä tehotaso on juuri sopiva sinulle.



![Image](assets/fr/043.webp)



Käyttötarkoituksesta riippuen voit valita joko 2TB SSD-levyn, kuten muissa kokoonpanoissa, tai suoraan 4TB SSD-levyn 260 eurolla, jos haluat tallentaa myös henkilökohtaisia tiedostoja ja laajentaa itseisännöintiä. 2 Tt:n SSD-levyllä kokoonpanon kokonaiskustannukset ovat 660 euroa, kun taas 4 Tt:n SSD-levyllä ne nousevat 800 euroon.



### Vielä muutama vinkki





- Jos haluat ostaa käytettyjä laitteita ja maksaa bitcoineilla, tule mukaan lähistöllä olevaan tapaamiseen! Keskustelemalla muiden osallistujien kanssa löydät varmasti sopivia laitteita hyvään hintaan ja autat samalla pitämään kiertotalouden Bitcoin:n ympärillä hengissä. Se on myös tilaisuus hyötyä yhteisön hyvistä neuvoista.





- Internet-yhteyttä varten tarvitset tietenkin RJ45 Ethernet-kaapelin, ainakin järjestelmän asennuksen ajaksi.





- Joissakin ympäristöissä, kuten Umbrelissa, voit käyttää Wi-Fi-yhteyttä, mutta suorituskyky on yleensä heikompi (varsinkin jos haluat käyttää Lightning-solmua etänä, sillä tämä voi vaikuttaa). Jos valitset Wi-Fi:n, varmista, että koneessasi on sisäänrakennettu kortti tai lisää yhteensopiva dongle.





- Käytä aina valmistajan alkuperäistä Supply-virtajohtoa koneellesi. Tämä on ratkaisevan tärkeää, jotta laitteesi ei vaurioidu ja jotta vältät tulipalon syttymisvaaran.





- Jos koneessasi ei ole sisäänrakennettua akkua, kannattaa investoida invertteriin äkillisten sammumisten välttämiseksi.





- Laitteiston arvosta ja maantieteellisestä sijainnista riippuen salamasuojausjärjestelmä voi myös olla asianmukainen, joko suoraan jakokeskuksessa tai käytetyssä pistorasiassa.





- Muista lopuksi optimoida koneen jäähdytys: puhdista se säännöllisesti ja asenna se viileään, hyvin tuuletettuun ja siistiin paikkaan, jotta vältetään ylikuumeneminen, joka voi johtaa prosessorin nopeuden vapaaehtoiseen rajoittamiseen.



# Bitcoin-solmun asentaminen helposti


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Sateenvarjo: paljon enemmän kuin Bitcoin-solmu


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel on henkilökohtainen palvelinkäyttöjärjestelmä, joka on suunniteltu tekemään itsehostingista helppokäyttöistä: asennat Umbrelin, avaat selaimen osoitteessa `umbrel.local` ja hallitset kaikkea yksinkertaisen Interface:n kautta.



Hanke teki ensin tunnetuksi ajatuksen yhden napsautuksen Bitcoin- ja Lightning-solmusta ja laajeni sitten todelliseksi "kotipilveksi": tiedostojen ja valokuvien tallennus, multimedian suoratoisto, verkkotyökalut, kotiautomaatio, paikallinen tekoäly ja sadat sovellukset, jotka voidaan asentaa integroidusta App Storesta.



Umbrelissa kukin sovellus toimii Docker-säiliössä (eristäminen, atomiset päivitykset, itsenäinen käynnistys/pysäytys). Interface keskittää pääsyn kaikkiin näihin sovelluksiin ja tarjoaa kertakirjautumisen (valinnaisella 2FA:lla), käyttöjärjestelmän ja sovellusten päivitykset yhdellä napsautuksella, koneen reaaliaikaisen seurannan (suorittimen, RAM-muistin, lämpötilan, tallennustilan), sovellusten välisten käyttöoikeuksien hallinnan ja yleiskatsauksen niiden kulutukseen.



Umbrelin tavoitteena on siis antaa sinulle takaisin tietojesi hallinta ja luottamuksellisuus ilman pilvipalveluja, mikä ei riitä pelkän Bitcoin-solmun käyttämiseen.



### Umbrel Home vs. umbrelOS



Umbrel tarjoaa kaksi erilaista lähestymistapaa:





- [**Umbrel Home**] (https://umbrel.com/umbrel-home): Tämä on käyttövalmis minipalvelin, joka on erityisesti suunniteltu ja optimoitu umbrelOS:lle. Kompakti, hiljainen, Ethernet-yhteydellä varustettu, varustettu NVMe SSD-levyllä (jopa 4TB valinnaisesti), 16GB RAM-muistilla ja neliydinsuorittimella. Tilaat sen, kytket sen ja menet osoitteeseen `umbrel.local`. Saat toimivan Umbrelin käyttöön muutamassa minuutissa. Tämä on plug-and-play-vaihtoehto.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): tämä on käyttöjärjestelmä, jonka voit asentaa itse omalle laitteistollesi (mini-PC, NUC, torni, oma kannettava tietokone...). Käytössäsi on sama Interface ja sama App Store kuin Umbrel Home -käyttöjärjestelmässä.



![Image](assets/fr/080.webp)



Molemmissa tapauksissa käyttäjäkokemus on ohjelmistopuolella identtinen: selainpohjainen hallinta, päivitykset yhdellä napsautuksella, sovellusten asennus tilauksesta... DIY-ratkaisu on usein edullisempi kuin Umbrel Home -ohjelman ostaminen (käytetystä koneesta riippuen). En kuitenkaan välttämättä suosittele, että valitset aina DIY-vaihtoehdon, sillä **Sumbrel Home -järjestelmän ostaminen osallistuu suoraan projektin kehittämisen rahoittamiseen**, koska sen liiketoimintamalli perustuu laitteiston myyntiin. Ja rehellisesti sanottuna, 389 euron hinta 2TB:n tallennustilasta on erittäin kohtuullinen ottaen huomioon tarjolla olevan koneen laadun.



![Image](assets/fr/079.webp)



Seuraavassa luvussa selvitämme, miten umbrelOS DIY asennetaan omalle koneellesi. Voit kuitenkin seurata tätä BTC 202 -kurssia samalla tavalla, jos olet valinnut Umbrel-kodin.



### Käyttötapaus: Bitcoin-solmusta kotipilveen



Umbrel voi pysyä hyvin minimalistisena ja keskittyä pelkästään Bitcoin:een tai kehittyä todelliseksi monitoimiseksi henkilökohtaiseksi palvelimeksi tarpeidesi mukaan. Tässä ovat Umbrelin tärkeimmät käyttökohteet:





- Yksinkertainen Bitcoin-solmu**: tämä on peruskäyttö, johon Umbrel on alusta alkaen luottanut. Voit käyttää Bitcoin core:a (tai Knotsia), liittää lompakot suoraan solmuun, paljastaa Electrum-palvelimen, isännöidä Mempool Block explorer:ta Blockchain:n tarkastelemiseksi ja arvioida maksuja... Näihin käyttötarkoituksiin keskitymme tällä kurssilla.



![Image](assets/fr/082.webp)





- Lightning Network**: Kaksi Lightning Network:n toteutusta, LND tai Core Lightning, voit myös ottaa käyttöön Umbrelin avulla oman Lightning-solmusi hallintaan. Voit avata kanavia, hallita likviditeettiäsi, suorittaa maksuja, automatisoida tasapainotusta, tarjota palveluja, yhdistää etä-Wallet:n tai hyödyntää Interface:n kehittynyttä hallintaa monien käytettävissä olevien sovellusten ansiosta. Tarkastelemme tätä erityistä käyttötapaa seuraavalla LNP 202 -kurssillamme.



![Image](assets/fr/083.webp)





- Yleinen self-hosting**: Nextcloud, Immich, Jellyfin/Plex, DNS:n laajuiset mainosblokkerit (Pi-hole/AdGuard), VPN:t (WireGuard, Tailscale), kotiautomaatio (Home Assistant), varmuuskopiot, muistiinpanojen hallinta, toimistotyökalut, paikallinen tekoäly (Ollama + Open WebUI)... Umbrelista voi tulla henkilökohtainen palvelimesi, jonka avulla voit saada tietosi takaisin hallintaasi. Isännöit itse päivittäin käyttämiäsi palveluita, joiden käyttökokemus muistuttaa pitkälti ulkoisia ratkaisuja, ja säilytät samalla täydellisen hallinnan tietojesi ja yksityisyytesi suhteen.



Kun sovellukset otetaan käyttöön konteissa, voit muokata Umbrelia haluamallasi tavalla: aloita yksinkertaisella Bitcoin-solmulla ja muutamalla sen ekosysteemiin liittyvällä sovelluksella, asenna sitten Lightning-solmu Bitcoin-solmun rinnalle ja täydennä instanssia vähitellen tarvitsemillasi itse isännöivillä sovelluksilla.



### Yhteisö ja keskinäinen apu



Yksi Umbrelin tärkeimmistä eduista kilpailijoihin verrattuna on sen laaja ja erittäin aktiivinen käyttäjäkunta. Voit tavoittaa heidät pääasiassa [heidän Discordissaan](https://discord.gg/efNtFzqtdx) ja [heidän verkkofoorumillaan](https://community.umbrel.com/). Täältä löydät käytännön neuvojen lisäksi ennen kaikkea ratkaisuja ongelmien ratkaisemiseen tai virheiden korjaamiseen. Se on loistava paikka aloittaa, edetä ja lopulta auttaa muita käyttäjiä, jotta et jää yksin Coin:n kanssa.



![Image](assets/fr/084.webp)



### UmbrelOS-lisenssi



Umbrelin koodi on julkisesti saatavilla (voit tarkastella, Fork ja muokata sitä), mutta sillä ei ole todellista avoimen lähdekoodin lisenssiä. Itse asiassa umbrelOS on jaettu [*PolyForm Noncommercial 1.0*]-lisenssin (https://polyformproject.org/licenses/noncommercial/1.0.0/) alla, vaikka jotkin siihen liittyvät kehitystyökalut ovat saatavilla MIT-lisenssin alla.



Käytännössä voit tehdä umbrelOS:llä lähes mitä tahansa, kunhan se on henkilökohtaiseen, ei-kaupalliseen käyttöön: muokkaaminen, jakelu voittoa tavoittelemattomiin tarkoituksiin, johdannaisten luominen itsellesi tai voittoa tavoittelemattomille organisaatioille, kunhan noudatat lakisääteisiä huomautuksia.



On kuitenkin kiellettyä myydä Umbrelia tai sen johdannaisia (esimerkiksi valmiiksi koottuja koneita, joihin on esiasennettu umbrelOS), tarjota Umbreliin liittyviä palveluja kaupallisesti tai integroida sen koodia tuotteeseen voiton tavoittelemiseksi.



Teknisesti tämä lisenssi ei rajoita Umbrelin asentamista, tarkastamista tai mukauttamista henkilökohtaiseen käyttöön. Oikeudellisesti se suojaa projektia luvattomalta jälleenmyynniltä tai kaupalliselta isännöinniltä, erityisesti pilvipalveluntarjoajien toimesta. Umbrel ei siis ole avointa lähdekoodia, vaikka sen koodi onkin julkisesti saatavilla.



Jokaisella Storessa olevalla sovelluksella on kuitenkin oma lisenssinsä, joka on usein avoin lähdekoodi.




## Full node:n asentaminen sateenvarjon kanssa


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nyt kun meillä on kaikki tarvittavat tiedot, on aika syventyä yksityiskohtiin. Tässä oppaassa näytämme, miten täydellinen Bitcoin-solmu asennetaan UmbrelOS:n avulla.



### Tarvittavat materiaalit



Tässä käytämme UmbrelOS x86 -kuvaa (tarkemmin sanottuna x86_64-versiota). Voit seurata tätä opasta millä tahansa valitsemallasi koneella, kunhan siinä ei ole ARM-arkkitehtuurin prosessoria (ei Apple Silicon, Raspberry Pi jne.). Tämä tarkoittaa, että mikä tahansa tietokone, jossa on Intelin tai AMD:n 64-bittinen prosessori, riittää, kunhan se täyttää vähimmäisvaatimukset riippuen siitä, miten aiot käyttää Umbrelia (vähintään kaksiytiminen prosessori on suositeltava).



Jos olet valinnut Raspberry Pi 5:n (vaihtoehtoa en suosittele, kuten edellisessä kappaleessa mainittiin), asennus on hieman erilainen. Voit sitten seurata tätä erityistä opetusohjelmaa ja palata kurssilleni kerran Interface-verkkosivulla `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Kuten edellisessä osiossa mainittiin, päätin suorittaa tämän opetusohjelman pienellä kunnostetulla tietokoneella, jonka löysin edullisesti: *Lenovo ThinkCentre M900 Tiny*, joka on varustettu Intel Core i7 -suorittimella ja 16 Gt RAM-muistilla. Tämä on erittäin mukava kokoonpano Umbrelin käyttämiseen, erityisesti Bitcoin-solmulle. Valitsin kuitenkin tämän kokoonpanon, koska haluan asentaa Lightning-solmun ja muita vaativampia sovelluksia myöhemmin. Olen myös lisännyt ThinkCentreeni 2 Tt:n SSD-levyn säilyttääkseni täyden Blockchain:n ja saadakseni silti mukavan marginaalin. Tällä kokoonpanolla kokonaiskustannukset ovat 270 euroa kaikkine kuluineen.



![Image](assets/fr/001.webp)



Pidän erityisesti Lenovon ThinkCentre Tiny -mallistosta, sillä ne ovat kompakteja, hiljaisia ja erittäin vankkoja koneita. Nämä tietokoneet ovat erittäin suosittuja yritysten keskuudessa, ja siksi niitä on runsaasti käytettyjen koneiden markkinoilla, joista löytyy mielenkiintoisia kokoonpanoja 70-200 euron väliltä.



Jos olet valinnut tietokoneen ilman näyttöä, kuten minä, **sinun täytyy liittää näyttö ja näppäimistö** vain asennuksen ajaksi. Sen jälkeen voit käyttää sitä etäyhteydellä toisesta tietokoneesta samassa verkossa (tai muilla menetelmillä, joita käsittelemme myöhemmissä luvuissa). Tarvitset myös RJ45-Ethernet-kaapelin, jolla voit liittää koneesi lähiverkkoon, ja vähintään 4 gigatavun USB-tietolevyn asennuskuvan tallentamista varten.



Seuraavassa on yhteenveto laitevaatimuksista:




- Tietokone, jossa on x86_64-prosessori (vähintään kaksiytiminen, suositellaan neliytiminen);
- RAM-muisti (vähintään 4 Gt, 8 Gt tai enemmän suositellaan pidempään käyttöön);
- SSD-levy (suositeltava + 2 TB);
- USB-tikku (+ 4 GB) UmbrelOS-kuvan asennusta varten;
- Näyttö ja näppäimistö (hyödyllinen vain ensiasennuksessa, jos tietokoneessa ei ole sellaista);
- RJ45 Ethernet-kaapeli.



### Vaihe 1 - Tietokoneen asentaminen



Riippuen valitsemastasi laitteistosta, ensimmäinen vaihe on tietokoneen eri osien kokoaminen. Esimerkiksi minun tapauksessani alkuperäisen SSD-levyn kapasiteetti oli vain 256 Gt, joten kierrätän sen toiseen käyttöön ja vaihdan sen 2 TB:n SSD-levyyn. Jos haluat vaihtaa myös RAM-moduulit, nyt on aika tehdä se.



### Vaihe 2: Valmistele käynnistettävä USB-levyke



Ennen kuin asennat UmbrelOS:n koneellesi, sinun on luotava käynnistettävä USB-levy, joka sisältää käyttöjärjestelmän. Kaikki vaiheen 2 vaiheet on suoritettava henkilökohtaisella tietokoneellasi (eikä suoraan tietokoneella, josta on tarkoitus tulla solmupisteesi).





- Aloita lataamalla UmbrelOS:n uusin versio USB-muodossa:



Siirry [Umbrelin viralliselle verkkosivustolle lataamaan ISO-kuva](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) USB-aseman kautta tapahtuvaa asennusta varten. Varmista, että valitset x86_64-arkkitehtuurin kanssa yhteensopivan version (tiedosto nimeltä `umbrelos-amd64-usb-installer.iso`). Lataaminen voi kestää jonkin aikaa, koska kuva on melko suuri.



![Image](assets/fr/002.webp)





- Asenna Balena Etcher:



Käynnistettävän USB-tikun luomiseen käytetään yksinkertaista, alustojen välistä työkalua nimeltä [Balena Etcher](https://www.balena.io/etcher/). Lataa ja asenna se tietokoneellesi.



![Image](assets/fr/003.webp)





- Aseta tyhjä, vähintään 4 Gt:n kokoinen USB-muistitikku:



Kytke USB-tikku tietokoneeseen (johon olet juuri ladannut UmbrelOS- ja Balena Etcher -kuvan). **Varoitus: kaikki avaimella olevat tiedot poistetaan**. Varmista, ettei se sisällä tärkeitä tiedostoja.





- Polta ISO-kuva USB-tikulle Balena Etcherillä:



Käynnistä Balena Etcher ja valitse juuri lataamasi `umbrelos-amd64-usb-installer.iso` ISO-tiedosto napsauttamalla "*Flash from file*"-painiketta. Valitse sitten USB-tikku kohdelaitteeksi ja aloita kirjoittaminen napsauttamalla "*Flash!*".



![Image](assets/fr/004.webp)



Kun operaatio on valmis, sinulla on UmbrelOS:n sisältävä käynnistettävä USB-levy, joka on valmis käynnistämään ja asentamaan Umbrelin koneellesi.



![Image](assets/fr/005.webp)



### Vaihe 3: Tietokoneen käynnistäminen USB-muistitikulta



Nyt kun UmbrelOS:n sisältävä käynnistettävä USB-tikkusi on valmis, voit käynnistää tietokoneen siitä ja aloittaa järjestelmän asennuksen. Irrota USB-tikku päätietokoneesta ja aseta se laitteeseen, johon haluat asentaa Umbrelin ja Bitcoin-solmun.



Kuten tämän luvun alussa kerrottiin, asennuksen loppuunsaattamiseksi tarvitset näyttölaitteen ja syöttölaitteen. Kytke näyttö HDMI:n (tai muun portin, riippuen tietokoneestasi) kautta ja näppäimistö USB:n kautta koneeseen. Näitä laitteita tarvitaan vain asennusta varten; et tarvitse niitä sen jälkeen, sillä Umbrelia käytetään etänä toisesta tietokoneesta. Liitä nämä kaksi laitetta tietokoneeseen.



**Vinkki:** Jos sinulla ei ole kotona oheisnäyttöä, voit käyttää televisiota. HDMI- (tai muun) tulon ansiosta sitä voidaan käyttää tilapäisenä näyttönä käyttöjärjestelmän asennuksen ajan.



Umbrel vaatii luonnollisesti Internet-yhteyden. Kytke RJ45 Ethernet-kaapeli laitteesi ja reitittimen välille.



![Image](assets/fr/006.webp)



Kytke koneesi päälle. Useimmissa tapauksissa koneen pitäisi tunnistaa USB-levy automaattisesti ja käynnistyä siitä. Tämän jälkeen näet UmbrelOS Interface:n asennusnäytön.



Jos laite käynnistyy toiseen järjestelmään tai näyttää virheilmoituksen, se tarkoittaa todennäköisesti sitä, että laite ei käynnisty automaattisesti USB-levyltä. Käynnistä laite tässä tapauksessa uudelleen ja siirry BIOS/UEFI-asetuksiin (niihin pääsee yleensä painamalla `DEL`, `F2`, `F12` tai `ESC` tietokoneen valmistajasta riippuen). Muuta sitten käynnistysjärjestystä siten, että USB-levy on etusijalla. Käynnistä laite uudelleen käynnistääksesi UmbrelOS:n.



### Vaihe 4: Asenna UmbrelOS tietokoneellesi



Kun laite on käynnistetty USB-tikulta, Interface UmbrelOS -asennus tulee näkyviin. Tässä vaiheessa järjestelmä asennetaan suoraan koneen sisäiselle Hard-levylle.



Avautuvassa näytössä luetellaan kaikki tietokoneen havaitsemat sisäiset tallennuslaitteet. Jokaisen levyn yhteydessä on numero, nimi ja tallennuskapasiteetti. Etsi levy, jolle haluat asentaa Umbrelin. **Varoitus: kaikki tällä levyllä olevat tiedostot poistetaan pysyvästi.**



![Image](assets/fr/007.webp)



Kun olet tunnistanut oikean levyn (yleensä suurimman kapasiteetin omaavan levyn, johon Blockchain mahtuu), merkitse muistiin sille annettu numero. Jos esimerkiksi valitsemasi levyn numero on `2`, kirjoita `2` ja paina sitten näppäimistön `Enter`-näppäintä.



![Image](assets/fr/008.webp)



Ohjelma alustaa valitun levyn, asentaa UmbrelOS:n ja konfiguroi järjestelmän automaattisesti. Tämä voi kestää muutaman minuutin. Anna prosessin kulkea keskeytyksettä.



![Image](assets/fr/009.webp)



Kun asennus on valmis, sinua pyydetään sammuttamaan laite. Sammuta tietokone painamalla mitä tahansa näppäintä.



![Image](assets/fr/010.webp)



Voit nyt poistaa USB-avaimen, näppäimistön ja näytön, joita Umbrel ei enää tarvitse. Solmusta jää jäljelle vain virtalähde Supply ja RJ45 Ethernet-kaapeli.



![Image](assets/fr/011.webp)



Tarkista seuraavat kaksi kohtaa ennen laitteen uudelleenkäynnistämistä:





- USB-muistitikku on irrotettu**: jos se on edelleen kytkettynä, järjestelmä saattaa käynnistyä uudelleen sisäisen levyn sijasta USB-muistitikulla;
- Ethernet-kaapeli on kytketty**: laitteen on oltava kytkettynä reitittimeen toimiakseen.



Paina virtapainiketta. Järjestelmä käynnistyy automaattisesti sisäiseltä levyltä, jolle UmbrelOS on asennettu. Ensimmäinen käynnistys voi kestää noin **5 minuuttia**. Tänä aikana Umbrel alustaa palvelunsa ja Interface:n.



Avaa verkkoselain (Firefox, Chrome...) toiselta tietokoneelta (tavalliselta tietokoneeltasi), joka on liitetty **samaan lähiverkkoon**, ja siirry osoitteeseen:



```
http://umbrel.local
```



Tätä Address:ää käytetään Umbrel Interface:n graafisen käyttäjän Interface:n etäkäyttöön ja konfiguroinnin aloittamiseen.



Jos Address `http://umbrel.local` ei toimi selaimessasi vähintään 5 minuutin odottelun jälkeen, yritä uudelleen:



```
http://umbrel
```



Jos tämä ei vieläkään toimi, kirjoita Umbrelin paikallinen IP-osoite Address suoraan selaimeen. Esimerkiksi (korvaa `42` sen koneen numerolla, joka isännöi Umbrelia lähiverkossa):



```
http://192.168.1.42
```



Umbrelin IP Address:n tunnistamiseen on useita menetelmiä, yksinkertaisimmista edistyneimpiin:





- Siirry reitittimen hallintatietoihin Interface ja etsi lähiverkossa olevan Umbrel-laitteen IP-osoite Address.





- Käytä verkon skannausohjelmistoa, kuten Angry IP Scanneria, havaitaksesi liitetyt laitteet ja löytääksesi Umbrelin IP Address:n.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Viimeisenä keinona kytke näyttö ja näppäimistö uudelleen laitteeseen, kirjaudu sisään (oletustunnus: `umbrel`, salasana: `umbrel`) ja kirjoita seuraava komento:



```
hostname -I
```



Nyt olet valmis käyttämään Umbrelia!



### Vaihe 5: Umbrelin käytön aloittaminen



Aloita Umbrelin konfigurointi napsauttamalla "*Start*"-painiketta.



![Image](assets/fr/013.webp)



#### Luo tili



Valitse salanimi tai kirjoita nimesi ja aseta sitten vahva salasana. Ole varovainen: tämä salasana on ainoa este, joka suojaa pääsyä Umbreliin verkostasi (ja siten mahdollisesti myös bitcoineihisi, jos käytät Lightning-solmua Umbrelissa). Se suojaa myös etäkäyttöä Torin tai VPN:n kautta, jos nämä palvelut ovat käytössä.



Valitse vahva salasana ja varmista, että sinulla on vähintään yksi varmuuskopio (salasanahallinta on suositeltavaa).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Kun olet syöttänyt salasanasi, napsauta "*Luo*"-painiketta.



![Image](assets/fr/014.webp)



Umbrelin kokoonpano on nyt valmis.



![Image](assets/fr/015.webp)



#### Interface:n löytäminen



Umbrelin Interface on varsin intuitiivinen:





- Etusivulla voit tarkastella asennettuja sovelluksia ja widgettejä.



![Image](assets/fr/016.webp)





- "*App Store*" mahdollistaa uusien sovellusten asentamisen,



![Image](assets/fr/017.webp)





- "*Tiedostot*"-valikossa on keskitetty kaikki Umbreliin tallennetut asiakirjat.



![Image](assets/fr/018.webp)





- "*Asetukset*"-valikossa voit muokata Umbrelin asetuksia ja käyttää sen tietoja, kuten:
    - Päivitä, käynnistä tai pysäytä koneesi;
    - Tarkista käytettävissä oleva tallennustila, RAM-muistin käyttö ja prosessorin lämpötila;
    - Vaihda taustakuva;
    - Hallitse etäkäyttöä Torin, Wi-Fi:n aktivoinnin tai 2FA:n avulla.



![Image](assets/fr/019.webp)



#### Turvallisuus- ja yhteysasetukset



Ensinnäkin suosittelen vahvasti kaksitekijätodennuksen (2FA) käyttöönottoa. Tämä lisää salasanasi turvallisuutta Layer:lla. Se on lähes välttämätön, jos aiot käyttää Umbrelia henkilökohtaisten tiedostojen tallentamiseen, Lightning-solmun käyttämiseen tai muuhun arkaluonteiseen toimintaan.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Voit tehdä tämän napsauttamalla vastaavaa ruutua asetuksissa.



![Image](assets/fr/020.webp)



Skannaa sitten näytetty QR-koodi tunnistautumissovelluksella. Kirjoita sitten 6-numeroinen dynaaminen koodi Umbrelissa olevaan kenttään.



Tästä lähtien jokainen uusi yhteys Umbreliin vaatii sekä salasanan että kaksitekijätodennussovelluksen (2FA) tuottaman kuusinumeroisen koodin.



![Image](assets/fr/021.webp)



Mitä tulee etäyhteyteen Torin kautta, jos et tarvitse sitä, suosittelen jättämään tämän vaihtoehdon pois käytöstä Umbrelin hyökkäyspinnan rajoittamiseksi. Oletusarvoisesti solmua voi käyttää vain samaan lähiverkkoon liitetystä koneesta. Torin kautta tapahtuvan pääsyn ottaminen käyttöön mahdollistaa kuitenkin Umbrelin hallinnan liikkeellä ollessasi.



Jos otat tämän ominaisuuden käyttöön, mikä tahansa kone maailmassa voi teoriassa yrittää muodostaa yhteyden solmuun, kunhan se tuntee Tor Address:n. Salasanasi ja 2FA suojaavat sinua kuitenkin edelleen.



Jos otat tämän vaihtoehdon käyttöön, varmista, että käytössäsi on kahden tekijän todennus (2FA), vahva salasana ja että et koskaan paljasta Tor-yhteyttäsi Address.



Kirjoita tämä Tor Address Tor-selaimeesi, niin pääset Umbrelin Interface:ään mistä tahansa verkosta.



![Image](assets/fr/026.webp)



Tällä asetussivulla voit myös aktivoida Wi-Fi-yhteyden. Jos Umbrelia isännöivässä koneessasi on Wi-Fi-verkkokortti tai Wi-Fi-dongle, voit käyttää Internetiä ilman RJ45-kaapelia. Kokoonpanosta riippuen tämä ratkaisu voi kuitenkin hidastaa yhteyttä, mikä voi vaikuttaa alkusynkronointiin (IBD) ja solmun myöhempään käyttöön (esim. Lightning-transaktioita varten). Henkilökohtaisesti en suosittele tätä vaihtoehtoa, sillä solmua ei ole tarkoitettu mobiilikäyttöön: sitä käytetään aina etänä, joten voit yhtä hyvin jättää sen kytkettynä.



### Vaihe 6: Bitcoin-solmun asentaminen Umbreliin



Nyt kun UmbrelOS on asennettu ja konfiguroitu koneellesi oikein, voit jatkaa Bitcoin-solmun asentamista. Mikään ei voisi olla yksinkertaisempaa: mene App Storeen, avaa "*Bitcoin*"-kategoria ja valitse sitten "*Bitcoin Node*"-sovellus (se on itse asiassa Bitcoin core).



![Image](assets/fr/022.webp)



Napsauta sitten "*Asenna*"-painiketta.



![Image](assets/fr/023.webp)



Kun asennus on valmis, Bitcoin-solmusi käynnistää IBD:n (*Initial Block Download*): se lataa ja validoi kaikki transaktiot ja lohkot siitä lähtien, kun Bitcoin luotiin vuonna 2009.



![Image](assets/fr/024.webp)



Tämä vaihe on erityisen aikaa vievä, sillä sen kesto riippuu useista tekijöistä, kuten solmun välimuistiin varatun RAM-muistin määrästä, levyn nopeudesta, Internet-yhteyden nopeudesta ja prosessorin tehosta. Kestojen vaihteluväli on siis hyvin laaja kokoonpanosta riippuen. Suorituskykyisellä tietokoneella (NVMe SSD, +32 Gt RAM-muistia, tehokas prosessori ja hyvä Internet-yhteys) IBD voidaan suorittaa noin kymmenessä tunnissa. Toisaalta vanha prosessori, vähäinen RAM-muisti tai, mikä vielä pahempaa, mekaaninen Hard-levy (jota ei kannata käyttää) voivat pidentää operaatiota useisiin viikkoihin.



Tavallisella tietokoneella (kunnollinen prosessori, 8-16 Gt RAM-muistia ja SSD-levy) se riittää noin 2-7 päiväksi.



Voit nopeuttaa IBD:tä hieman lisäämällä solmuvälimuistiin varattua RAM-muistia (jota käytetään pääasiassa UTXO-sarjaa varten, johon palaamme myöhemmin kurssilla) parametrilla `dbcache`. Umbrelissa tämä muutos tehdään solmuparametreissa, välilehdellä "*Optimization*".



![Image](assets/fr/025.webp)



Oletusarvoisesti Bitcoin core:n `dbcache`-parametrin arvoksi on asetettu 450 MiB eli noin 472 Mt. Nostamalla tätä arvoa voit hieman nopeuttaa IBD:tä. En kuitenkaan välttämättä suosittele tämän parametrin nostamista liian suureksi: jopa sen asettaminen 4 GiB:iin nopeuttaa synkronointia vain noin 10 prosenttia ja saattaa aiheuttaa ajan menetyksen, jos IBD:n aikana tapahtuu keskeytys.



Ole varovainen, ettet anna liian suurta arvoa koneellesi. Jos UmbrelOS:n käytettävissä oleva RAM-muisti loppuu, solmusi voi pysähtyä äkillisesti, jolloin IBD keskeytyy ja sinun on käynnistettävä se uudelleen manuaalisesti, mikä aiheuttaa huomattavaa ajanhukkaa.



Jos haluat lisätietoja `dbcache`-parametrin vaikutuksesta alkuperäiseen synkronointiin, suosittelen tätä Jameson Loppin analyysia: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Kun solmun IBD on saatu valmiiksi (100-prosenttinen synkronointi), sinulla on nyt täysin toimiva Bitcoin-solmu. Onnittelut, olet nyt kiinteä osa Bitcoin-verkkoa!



![Image](assets/fr/027.webp)



Seuraavassa osassa tarkastelemme uuden solmun käytännön käyttöä: miten kytket Wallet:n siihen ja mitä sovelluksia sinun pitäisi asentaa, jotta sinusta tulisi suvereeni Bitcoin-käyttäjä.





# Wallet:n liittäminen solmuun


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indeksoijat: rooli, toiminta ja ratkaisut


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Jos olet jo tutkinut Bitcoin-solmuja ennen tätä kurssia, olet ehkä törmännyt termiin "indeksoija". Ne ovat työkaluja, kuten Electrs tai Fulcrum, jotka voidaan lisätä Bitcoin core-solmuun. Mutta mikä on niiden tehtävä? Miten ne toimivat käytännössä? Ja pitäisikö sinun asentaa sellainen uuteen Bitcoin-solmuun? Tätä tutkimme tässä luvussa.



### Mikä on indeksoija?



Yleisesti ottaen indeksoija on ohjelma, joka skannaa raakadatan, poimii olennaiset avaimet (kuten sanat, tunnisteet ja osoitteet) ja luo "indeksiksi" kutsutun aputiedoston, jossa kukin avain viittaa datan tarkkaan sijaintiin korpuksessa. Tämä esikäsittelyvaihe käyttää prosessoriaikaa ja vaatii jonkin verran levytilaa, mutta sen ansiosta koko korpusta ei tarvitse käsitellä joka kerta, kun tietokantaan tehdään kysely; indeksin kysyminen tuottaa lähes välittömän vastauksen.



Maallikon kielellä kyseessä on sama periaate kuin kirjan hakemistossa: jos etsit tiettyä tietoa, etsi hakemistosta suoraan sivu, jossa etsimäsi tieto on, etkä lue koko kirjaa uudelleen.



Bitcoin-solmussa, kuten Bitcoin core:ssä, Blockchain-tiedot tallennetaan raa'assa, kronologisessa muodossaan. Kukin lohko sisältää transaktioita, jotka puolestaan sisältävät panoksia ja tuotoksia ilman erityistä luokittelua Address:n, tunnisteen tai Wallet:n mukaan. Tämä lineaarinen organisaatio on optimaalinen lohkojen validointia varten, mutta se ei sovellu kohdennettuihin hakuihin. Jos esimerkiksi haluaisit löytää kaikki tiettyyn Address:een liittyvät tapahtumat indeksoimattomassa solmussa, sinun olisi tarkasteltava manuaalisesti koko Blockchain:ää lohko lohkolta ja tapahtuma tapahtumalta. Juuri tässä kohtaa Bitcoin-solmun indeksoija tulee kuvaan mukaan.



![Image](assets/fr/085.webp)



Indeksoija on erikoistunut ohjelmisto, joka analysoi tämän raakadatamassan (Blockchain-, Mempool- ja UTXO-joukko) ja poimii siitä avaimia, kuten tapahtumatunnukset, osoitteet ja lohkojen korkeudet. Näistä avaimista se muodostaa indeksin, jossa kukin avain yhdistetään tiedon tarkkaan sijaintiin solmun varastossa.



![Image](assets/fr/086.webp)



Indeksoinnin avulla voit etsiä tietoja solmusta nopeasti, tarkasti ja tehokkaasti. Kun esimerkiksi kytket Wallet:n kuten Sparrow:n solmuun, se voi näyttää Address:n saldon lähes välittömästi. Konkreettisesti se kysyy indeksoijalta seuraavanlaisella pyynnöllä: "_Mitkä UTXO:t liittyvät tähän skriptiin-Hash?_" Indeksoija vastaa lähes välittömästi ilman, että koko Blockchain:ta tarvitsee lukea uudelleen, koska nämä tiedot on jo lueteltu sen tietokannassa.



### Onko Bitcoin core:ssä indeksoija?



Ilman lisäohjelmiston tarvetta Bitcoin core ei varsinaisesti tarjoa täydellistä Address indeksointia, joka on verrattavissa Electrs- tai Fulcrum-ohjelmistojen kaltaisiin ohjelmistoihin. Se sisältää kuitenkin useita sisäisiä indeksointimekanismeja sekä valinnaisia vaihtoehtoja sen kyselyominaisuuksien laajentamiseksi. Tilanteen ymmärtämiseksi täysin meidän on tehtävä kiertoajelu projektin historiaan.



Bitcoin core-versioon 0.8.0 asti tapahtumien validointi perustui globaaliin tapahtumaindeksiin, joka tunnetaan nimellä `txindex`. Tämä indeksi viittasi kaikkiin Blockchain-tapahtumiin ja niiden tuloksiin. Kun solmu vastaanotti uuden transaktion, se tarkisti indeksistä, että kulutetut tuotokset (syötteinä) olivat todella olemassa eikä niitä ollut jo käytetty. `txindex` oli siis tuolloin välttämätön tapahtumien validoinnissa.



Tällä lähestymistavalla oli kuitenkin omat rajoituksensa: se oli hidas, kallis tallennuksen kannalta ja tarpeeton tiedon osalta. Tämän korjaamiseksi versiossa 0.8.0 esitellään validointimallin uudistettu versio ***Ultraprune***. Sen sijaan, että Bitcoin core tallentaisi kaiken tapahtumaindeksien muodossa, se ylläpitää yksinkertaista, pelkästään UTXO:ille omistettua tietokantaa nimeltä `chainstate` (arkikielessä tämä tunnetaan nimellä "UTXO set") ja päivittää sen luetteloa sitä mukaa, kun tuotoksia kulutetaan ja luodaan.



Tämä menetelmä on paljon nopeampi ja tallentaa vain rekisterin senhetkisen tilan, jolloin `txindex`-indeksiä ei tarvita. Sen sijaan, että `txindex`-koodi olisi poistettu, kehittäjät ovat kuitenkin päättäneet pitää tämän toiminnallisuuden yksinkertaisen parametrin (`txindex=1`) takana. Kun otat tämän parametrin käyttöön solmussasi, voit kysyä mitä tahansa tapahtumaa sen `txid`:stä.



Toisin kuin yleisesti uskotaan, Bitcoin core ei tarjoa Address-pohjaista indeksointia kuten Electrs tai Fulcrum. Tähän valintaan on useita syitä:





- Bitcoin core:n tehtävänä ei ole tulla täydelliseksi Block explorer:ksi eikä tarjota jokaiseen käyttötarkoitukseen räätälöityä sovellusliittymää. Address-pohjaisen indeksin integroiminen edellyttäisi Commitment pitkäaikaista ylläpitoa, joka ylittää ohjelmiston alkuperäisen soveltamisalan.





- Useimmat käyttötapaukset voidaan jo kattaa muilla tavoin. Esimerkiksi Address:n saldon arvioimiseksi voit käyttää komentoa `scantxoutset`, joka kysyy suoraan UTXO-joukkoa ilman täydellistä indeksiä.





- Kullakin ohjelmistolla on erityisvaatimuksia indeksoitavien tietojen muodon tai tyypin suhteen (Address, Hash-skripti, oma tunniste jne.). On joustavampaa ja loogisempaa antaa näiden ohjelmien rakentaa omat räätälöidyt indeksinsä kuin korjata yleinen ratkaisu Bitcoin core:een.



Bitcoin core:ssa on valinnainen tapahtumaindeksi (`txindex`), joka on jäänne sen historiallisesta toiminnasta, mutta se ei tarjoa Address-indeksiä eikä suoraa Interface:ää monimutkaisia hakuja varten. Joissakin tapauksissa voi siis olla hyödyllistä lisätä ulkoinen indeksoija.



### Pitäisikö solmuun lisätä Address-indeksoija?



Address-indeksointilaitteen, kuten Electrs tai Fulcrum, lisääminen ei ole pakollista; se riippuu erityistarpeistasi.



Jos haluat yksinkertaisesti yhdistää Wallet:n, kuten Sparrow:n, solmuun nähdäksesi saldot ja lähettääksesi tapahtumia, tämä on täysin mahdollista suoraan Bitcoin core:n Interface RPC:n kautta joko paikallisesti tai etänä Torin kautta.



Toisaalta, käyttää kehittyneempiä ohjelmistoja, kuten käynnissä Mempool.Paikallisesti, asennus Address indeksoija tulee välttämätöntä tilaa Block explorer.



Indeksointi vaatii tietyn määrän synkronointiaikaa (vähemmän kuin IBD) ja vie lisää levytilaa. Jos SSD-levylläsi on vielä riittävästi vapaata tilaa Blockchain:n lataamisen jälkeen, voit helposti lisätä indeksoijan.



### Minkä indeksoijan valita?



Tällaisen Address-indeksin rakentamiseen ja sen saataville saattamiseen käytetään yleisesti kahta ohjelmistoa: **Electrs** ja **Fulcrum**. Nämä työkalut indeksoivat Blockchain:n script-Hash:n (osoitteet) mukaan ja ehdottavat sitten standardoitua Interface:ää (Electrum-protokolla), johon lukuisat lompakot, kuten Electrum Wallet, Sparrow tai Phoenix, yhdistyvät.



![Image](assets/fr/087.webp)



Yksinkertaisesti sanottuna Electrs on melko kompakti: se indeksoi Blockchain nopeammin ja vie vähemmän levytilaa, mutta suoriutuu kyselyistä hieman huonommin kuin Fulcrum. Fulcrum sen sijaan kuluttaa enemmän levytilaa ja sen indeksointi kestää kauemmin, mutta sen suorituskyky kyselyissä on parempi.



Yksilölliseen käyttöön suosittelen Electrsia: se kuluttaa vähemmän tilaa, on hyvin ylläpidetty, ja vaikka se on hieman hitaampi tietyissä pyynnöissä kuin Fulcrum, se on silti enemmän kuin riittävä jokapäiväiseen käyttöön. Jos sinulla on aikaa ja levytilaa, voit myös kokeilla Fulcrumia, joka toimii huomattavasti paremmin, erityisesti lompakoissa, joissa on lukuisia tarkistettavia osoitteita.



Konkreettisesti ilmaistuna elokuussa 2025 Electrs tarvitsee noin 56 gigatavua tallennustilaa, kun taas Fulcrumilla se on noin 178 gigatavua. Indeksin valinta riippuu siis myös tallennuskapasiteetista:




- Jos levytilaa on hyvin vähän, sinun on pärjättävä Bitcoin core:llä ilman ulkoista Address-indeksoijaa.
- Jos haluat käyttää indeksoijaa, mutta kapasiteetti rajoittaa sinua, valitse Electrs.
- Jos sinulla on riittävästi levytilaa, Fulcrum voi olla juuri sitä, mitä etsit.



Loppuosassa tätä BTC 202 -kurssia käytän Electrsia, mutta voit helposti seurata Fulcrumin käyttöä: asennusprosessi on identtinen, samoin kuin Interface:n ja Wallet:n välinen yhteys, koska molemmat käyttävät Electrum-palvelinta.



### Miten asennan indeksoijan Umbreliin?



Jos haluat asentaa Electrs (tai Fulcrum) Umbreliin, menettely on yksinkertainen: mene App Storeen, etsi kyseinen sovellus (joka sijaitsee Bitcoin-välilehdellä) ja napsauta sitten "*Asenna*"-painiketta.



![Image](assets/fr/028.webp)



Kun asennus on valmis, Electrs aloittaa synkronointivaiheen (indeksoinnin), joka voi kestää useita tunteja.



![Image](assets/fr/029.webp)



Kun synkronointi on valmis, voit liittää Wallet-ohjelmiston Electrum-palvelimeen, jota ylläpidetään Umbrelissa.



## Miten liitän Wallet:n Bitcoin-solmuun?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nyt kun sinulla on täydellinen Bitcoin-solmu, on aika ottaa se käyttöön! Seuraavassa luvussa tarkastelemme Umbrel-instanssisi muita mahdollisia käyttötarkoituksia. Aloitetaan kuitenkin perusasioista: kytketään Wallet-ohjelmisto käyttämään oman Blockchain:n tietoja ja jakamaan tapahtumia oman solmun kautta.



Kuten edellä mainittiin, on olemassa kaksi pääyhteysliittymää:




- Suora yhteys Bitcoin core:aan RPC:n kautta;
- Tai muodosta yhteys Electrum-palvelimeen (Electrs tai Fulcrum).



Tässä ohjeessa keskitymme yhteyden muodostamiseen solmuun Torin kautta, sillä se on yksinkertainen ja turvallinen ratkaisu aloittelijoille. Suosittelen, että solmun RPC-porttia ei paljasteta avoimesti, sillä vääränlainen konfigurointi on merkittävä riski tietojesi turvallisuudelle ja luottamuksellisuudelle. Torin kautta tapahtuvan viestinnän suurin haittapuoli on sen hitaus. Seuraavassa luvussa tutustumme nopeaan ja turvalliseen vaihtoehtoon Torille solmun etäkäyttöä varten: VPN.



Käytämme tässä luvussa esimerkkinä Sparrow:tä, mutta menettely on sama kaikille muille Wallet-hallintaohjelmistoille, jotka hyväksyvät yhteydet Electrum-palvelimiin. Etsi yksinkertaisesti vastaava asetus sovelluksesi parametreista (yleensä kohdista "*Server*", "*Network*", "*Node*"...).



Avaa Sparrow:ssa välilehti "*File*" ja siirry "Settings"-valikkoon.



![Image](assets/fr/030.webp)



Napsauta sitten "*Palvelin*" päästäksesi yhteysparametreihin.



![Image](assets/fr/031.webp)



Tämän jälkeen näet kolme vaihtoehtoa ohjelmiston liittämiseksi Bitcoin-solmuun:




- Julkinen palvelin* (keltainen): Jos et omista Bitcoin-solmua, tämä vaihtoehto yhdistää sinut oletusarvoisesti julkiseen solmuun, jota et omista (yleensä yrityksen solmuun). Tämä vaihtoehto ei ole tässä yhteydessä merkityksellinen, koska sinulla on oma solmusi Umbrelissa.
- Bitcoin core* (Green): tämä vaihtoehto vastaa yhteyttä Interface RPC:n kautta eli suoraan Bitcoin core:een.
- Private Electrum* (sininen): Tämän vaihtoehdon avulla voit muodostaa yhteyden indeksoijan Interface Electrum-palvelimen (Electrs tai Fulcrum) kautta.



### Yhteys Bitcoin core RPC



Jos Umbrel-solmussasi ei ole indeksoijaa, sinun on valittava tämä vaihtoehto. Napsauta Sparrow:ssä "*Bitcoin core*".



![Image](assets/fr/032.webp)



Tämän jälkeen sinun on annettava useita tietoja, jotta yhteys solmuun voidaan muodostaa. Kaikkiin näihin tietoihin pääsee käsiksi Umbrelin "*Bitcoin Node*"-sovelluksesta napsauttamalla Interface:n oikeassa yläkulmassa olevaa "*Connect*"-painiketta.



![Image](assets/fr/033.webp)



"*RPC Details*"-välilehdellä näytetään kaikki tarvittavat tiedot yhteyden muodostamiseksi. Valitse yhteyden muodostaminen Tor Address:n kautta (tiedostossa `.onion`).



![Image](assets/fr/034.webp)



Syötä nämä tiedot Sparrow wallet:n vastaaviin kenttiin ja napsauta sitten painiketta "*Testaa yhteys*".



![Image](assets/fr/035.webp)



Jos yhteys onnistuu, näyttöön ilmestyy Green:n rasti ja vahvistusviesti.



![Image](assets/fr/036.webp)



Interface Sparrow wallet:n oikeassa alareunassa oleva rasti on nyt Green (mikä osoittaa suoraa yhteyttä Bitcoin core:een).



**Huomaa:** Jotta yhteys onnistuisi, solmun on oltava 100-prosenttisesti synkronoitu. Jos näin ei ole, odota IBD:n loppuun asti.



### Yhdistä sähkölaitteisiin



Jos solmussasi on indeksoija, on parempi muodostaa yhteys siihen kuin käyttää suoraan Bitcoin core:tä, koska kyselyt käsitellään nopeammin.



Siirry Sparrow:ssa välilehdelle "*Private Electrum*".



![Image](assets/fr/037.webp)



Tämän jälkeen sinun on syötettävä useita tietoja, jotta yhteys indeksoijan kanssa voidaan muodostaa. Löydät nämä tiedot Umbrelin "*Electrs*"-sovelluksesta (tai tarvittaessa "*Fulcrum*").



Valitse "*Tor*"-välilehti saadaksesi `.onion`-yhteyden Address. Jos haluat liittää mobiililaitteeseen Wallet-ohjelmiston, voit myös skannata QR-koodin suoraan.



![Image](assets/fr/038.webp)



Kirjoita Electrum-palvelimesi Tor Address -osoite "*URL*"-kenttään ja napsauta sitten "*Test Connection*"-painiketta.



![Image](assets/fr/039.webp)



Jos yhteys onnistuu, näyttöön tulee valintamerkki ja vahvistusviesti.



![Image](assets/fr/040.webp)



Interface Sparrow wallet:n oikeassa alakulmassa oleva rasti muuttuu siniseksi (väri, joka liittyy yhteyden muodostamiseen Electrum-palvelimeen).



**Huomaa:** Jotta yhteys toimisi, indeksoijan on oltava 100-prosenttisesti synkronoitu. Jos näin ei ole, odota, kunnes indeksointiprosessi on valmis.



Nyt tiedät, miten Wallet liitetään Bitcoin-solmuun! Seuraavassa luvussa esittelen sinulle useita Umbrelissa saatavilla olevia lisäsovelluksia, joista olen erityisen ihastunut ja joiden avulla voit tehostaa Bitcoin:n päivittäistä käyttöä solmun kautta.




## Yleiskatsaus käytettävissä olevista sovelluksista


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel tarjoaa laajan sovelluskaupan. Kuten huomaat, siellä on monia Bitcoin:ään liittyviä työkaluja, mutta myös monenlaisia sovelluksia hyvin erilaisilta aloilta: itsepalveluratkaisuja palveluille ja tiedostoille, tuottavuussovelluksia, yleisempiä taloushallinnon työkaluja, median hallintaa, verkkoturvallisuutta ja -hallintaa, kehitystyötä, tekoälyä, sosiaalista verkostoitumista ja jopa kotiautomaatiota.



Tällä BTC 202 -kurssilla keskitymme yksinomaan Bitcoin-sovelluksiin. Tutustu kuitenkin vapaasti muuhun luetteloon etsiessäsi työkaluja, joista voi olla sinulle hyötyä.



On tietenkin mahdotonta luetella kaikkia Bitcoin:n sovelluksia tässä. Tässä luvussa haluan esitellä sinulle keskeiset työkalut, jotka helpottavat ja rikastuttavat Bitcoin:n päivittäistä käyttöäsi.



### Mempool.space



Bitcoin:n päivittäisessä käytössä yksi todella välttämätön työkalu on Block explorer. Se muuntaa Blockchain:n raakadatan jäsennellyksi, selkeäksi ja helposti luettavaan muotoon riippumatta siitä, onko se käytettävissä verkossa vai paikallisesti asennettuna. Siinä on myös hakukone, jonka avulla käyttäjät voivat etsiä nopeasti tietyn lohkon, transaktion tai Address:n.



Konkreettisesti ilmaistuna explorerin avulla voit arvioida maksut, joita tarvitaan, jotta transaktiosi voidaan sisällyttää lohkoon, seurata sen edistymistä: selvittää, sisällytetäänkö se todennäköisesti lähitulevaisuudessa maksumarkkinoista riippuen, ja lopuksi vahvistaa, että se on todellakin sisällytetty lohkoon. Se tarjoaa myös mahdollisuuden analysoida aiempia transaktioitasi ja tutustua niiden historiaan. Lyhyesti sanottuna se on bitcoinerin sveitsiläinen armeijan veitsi.



Kuten aiemmin mainittiin, etsintäohjelma voi sijaita verkossa verkkosivustolla tai toimia paikallisesti koneellasi. Verkkopalveluiden suuri haittapuoli on, että ne voivat vaarantaa yksityisyytesi. Ilman VPN:ää tai Toria exploreria isännöivä palvelin voi yhdistää IP-osoitteesi Address katselemiisi tapahtumiin, mikä voi tarjota ihanteellisen pääsyn ketjuanalyysiin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Lisäksi Internet-palveluntarjoajasi (ISP) saattaa tietää, että katselet tiettyä tapahtumaa Block explorer-sivuston kautta. Tämä herättää myös luottamuskysymyksen: sinun on luotettava siihen, että verkkopalvelu antaa sinulle oikeat tiedot liiketoimistasi, mutta et voi itse tarkistaa niiden todenperäisyyttä.



Siksi on aina parasta käyttää omaa paikallista Block explorer:ää. Näin hakutoimintoihin liittyvät tiedot eivät pääse vuotamaan ulos, koska kaikki kyselyt käsitellään suoraan hallitsemallasi koneella ilman, että ne kulkevat Internetin kautta. Lisäksi paikallinen etsijä luottaa oman Bitcoin-solmusi tietoihin, jotka olet itse validoinut omien sääntöjesi mukaisesti ja joihin voit luottaa.



Umbrel tarjoaa useita lohko-etsintäohjelmia:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Olen erityisen ihastunut Mempool.Spaceen, jonka olen asentanut solmuun. Huomaa: useimpien Umbrelin lohko-etsintäkoneiden käyttämiseen tarvitaan Address-indeksoija. Tarvitset siis Bitcoin Node (tai Bitcoin Knots) -sovelluksen, jossa on 100-prosenttisesti synkronoitu Blockchain, sekä indeksoijan, kuten Electrs tai Fulcrum, joka on myös 100-prosenttisesti synkronoitu.



Kun sovellus on asennettu, voit avata sen ja käyttää omaa etsintäsi.



![Image](assets/fr/041.webp)



Jos haluat lisätietoja Mempool.Space explorerin käytöstä, suosittelen tätä kattavaa opetusohjelmaa:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Salama-solmu



Nyt kun sinulla on oma Bitcoin-solmu, voit myös perustaa oman Lightning-solmun suorittamaan off-chain-transaktioita ilman kolmannen osapuolen infrastruktuuria.



Umbrel tarjoaa useita sovelluksia, joiden avulla saat Lightning-solmun käyttöön. Voit jo nyt valita kahden päätoteutuksen välillä:




- LND, *Lightning Node* -sovelluksen kautta;
- Ydinsalama.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sen jälkeen voit hallita solmua Interface:n pääsivustolta tai, jos haluat vielä enemmän toimintoja ja lisäasetuksia, asentaa *Ride The Lightning*- tai *ThunderHub*-ohjelman. Näiden työkalujen avulla saat solmusi käyttöön paljon kattavamman Interface:n verkkopohjaisen hallintajärjestelmän.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Lopuksi suosittelen *Lightning Network+*-sovellusta, jonka avulla voit löytää vertaisia, joiden kanssa voit avata kanavia, jotka mahdollistavat sekä lähtevät että saapuvat käteistapahtumat.



![Image](assets/fr/089.webp)



Umbrelin ansiosta henkilökohtaisen Lightning-solmun hallinta on yksinkertaistunut huomattavasti, mutta se on silti suhteellisen monimutkaista. Tästä syystä tarkastelemme aihetta tarkemmin tulevalla kurssilla, joka on omistettu kokonaan tälle käyttötarkoitukselle.



### Tailscale



Toinen sovellus, josta pidän Umbrelissa erityisen paljon, on Tailscale. Se on VPN-sovellus, joka on suunniteltu yksinkertaistamaan turvallisten verkkojen luomista useiden laitteiden välille, olivatpa ne missä päin maailmaa tahansa. Toisin kuin perinteiset VPN:t, jotka luottavat keskitettyihin palvelimiin, Tailscale käyttää WireGuard-protokollaa luodakseen päästä päähän salattuja yhteyksiä eri koneiden välille. Tämä tarkoittaa, että voit ottaa käyttöön toimivan VPN:n muutamassa minuutissa ilman monimutkaisia verkkokonfiguraatioita.



Umbrelissa Tailscale-asennus yhdistää Bitcoin-solmun omaan virtuaaliseen yksityisverkkoon. Kun solmusi on konfiguroitu, se saa yksityisen Tailscale-IP:n Address, johon on pääsy vain muista samaan Tailscale-verkkoon liitetyistä laitteista (kuten tietokoneista, älypuhelimista ja tableteista). Tämä yhteys on päästä päähän salattu eikä kulje suojaamattoman julkisen verkon kautta, mikä parantaa turvallisuutta merkittävästi salaamattomaan yhteyteen verrattuna.



![Image](assets/fr/090.webp)



Konkreettisesti sanottuna Tailscale tarjoaa sinulle useita etuja, kun käytät Umbrelia:





- Voit hallinnoida Interface Umbrelia tai käyttää solmuun liitettyjä sovelluksia (kuten Mempool, Ride The Lightning, ThunderHub...) mistä tahansa, ikään kuin olisit samassa lähiverkossa, paljastamatta portteja Internetissä ja kulkematta Torin kautta, joka on hyvin hidas;





- Voit muodostaa yhteyden Electrum-palvelimeen (Electrs tai Fulcrum) tai suoraan Bitcoin core:een VPN:n kautta ohittaen Torin. Tämä tarjoaa turvallisen yhteyden, joka on verrattavissa Torin käyttöön, mutta paljon nopeampi ja viiveettömämpi. Lyhyesti sanottuna säilytät Torin yksityisyyden ja turvallisuuden edut ja nautit samalla Clearnet-yhteyden nopeudesta. On-Chain Wallet:n osalta tämä hyöty saattaa vaikuttaa marginaaliselta, mutta jos aiot perustaa oman Lightning-solmun myöhemmin, ero on huomattava. Maksujen suorittaminen oman solmun kautta liikkeellä Torissa on nimittäin erittäin hidasta vaadittavien lukuisten vaihtojen vuoksi, kun taas Tailscalen kanssa se toimii täydellisesti.





- Sinun ei tarvitse määrittää NAT-sääntöjä, avata portteja tai perustaa perinteistä VPN-palvelinta. Kun sovellus on asennettu Umbreliin ja laitteisiisi, verkko muodostuu automaattisesti.



Tailscale on Umbrel on siis erittäin mielenkiintoinen ratkaisu, jos haluat käyttää solmua mistä päin maailmaa tahansa turvallisella, suorituskykyisellä ja helposti konfiguroitavalla tavalla uhraamatta yksityisyyttä tai turvallisuutta.



Jos haluat asentaa ja määrittää Tailscalen Umbreliin, katso tämän ohjeen osio 4: "*Tailscalen käyttäminen Umbrelissa*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, joka on lyhenne sanoista "*Notes and Other Stuff Transmitted by Relays*", on avoin, hajautettu protokolla, joka on suunniteltu mahdollistamaan viestien julkaiseminen ja vaihtaminen Internetissä ilman riippuvuutta keskitetystä alustasta. Jokaisella käyttäjällä on kryptografinen avainpari: julkinen avain (`npub`), joka toimii tunnisteena, ja yksityinen avain (`nsec`), jota käytetään viestien allekirjoittamiseen ja niiden aitouden takaamiseen.



Viestit välitetään riippumattomien releiden verkon kautta. Tämä hajautettu arkkitehtuuri tekee Nostrista sensuurin kestävän: mikään yksittäinen palvelin ei valvo pääsyä tai jakelua, ja käyttäjä voi muodostaa yhteyden niin moneen releeseen kuin haluaa.



Tämä protokolla on hyvin suosittu Bitcoin-yhteisössä, koska Bitcoin:n tavoin Nostr käsittelee digitaaliseen suvereniteettiin ja tiedonhallintaan liittyviä kysymyksiä. Sen luoja Fiatjaf on kehittäjä, joka on jo tunnustettu ekosysteemissä lukuisista panoksistaan.



Umbrelin avulla voit optimoida Nostrin käytön. Asentamalla ***Nostr Relay*** -sovelluksen voit isännöidä omaa yksityistä relettäsi suoraan koneellasi, jolloin kaikki Nostrissa tekemäsi viestit ja vuorovaikutuksesi tallentuvat paikallisesti, eivätkä julkiset relet voi hävitä niitä poistamalla.



Nostr-asiakkaat ***noStrudel*** tai ***Snort*** ovat myös saatavilla Umbrelissa. Näiden sovellusten ansiosta voit julkaista, lukea, etsiä profiileja ja olla vuorovaikutuksessa Nostr-ekosysteemin kanssa suoraan Umbrelin Interface-verkosta.



Lisäksi Umbrelissa on ***Nostr Wallet Connect*** -sovellus, joka mahdollistaa natiivit Lightning-maksut Nostrissa. Konkreettisesti sanottuna voit yhdistää tulevan Lightning-solmun Nostr-asiakkaisiisi lähettääksesi mikromaksuja, joita kutsutaan nimellä "*zaps*", palkita sisältöä tai olla vuorovaikutuksessa rahanarvoisella tavalla ilman, että sinun tarvitsee mennä kolmannen osapuolen palvelun kautta. Nämä maksut lähetetään suoraan henkilökohtaisesta solmusta kanaviesi kautta.



Jos haluat tietää, miten kaikkia näitä sovelluksia käytetään, suosittelen tutustumaan tähän täydelliseen opetusohjelmaan:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay-palvelin



BTCPay Server on ilmainen, avoimen lähdekoodin maksuprosessori, jonka avulla voit hyväksyä maksuja Bitcoin- ja Lightning Network-maksujen kautta ilman välikäsiä ja säilyttää samalla varojen itsesäilytyksen.



BTCPay Serverin arkkitehtuuri perustuu Bitcoin-solmuun ja Lightningin osalta yhteensopivaan toteutukseen (LND, Core Lightning...), mikä tekee siitä yhden ainoista täysin huoltajattomista PoS-ratkaisuista. Se on myös kattavin seuranta- ja kirjanpito-ohjelmisto.



![Image](assets/fr/091.webp)



Jos omistat yrityksen ja haluat hyväksyä Bitcoin-maksuja suoraan Umbrel-solmun kautta, BTCPay Server -sovellus sopii sinulle. Jos haluat lisätietoja tästä aiheesta, suosittelen tutustumaan seuraaviin lähteisiin:





- BIZ 101 -kurssi Bitcoin:n käytöstä yrityksessäsi:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- POS 305 -kurssi BTCPay Serverin käytöstä:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- BTCPay-palvelimen opetusohjelma:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Edistyneet käsitteet ja parhaat käytännöt


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Sateenvarjosolmun ylläpito


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Aloittaakseni tämän viimeisen osion ja ennen kuin siirrymme edistyneempään teoriaan, haluaisin tarkastella tässä lyhyessä luvussa parhaita käytäntöjä ja konkreettisia toimia, joita voit tehdä, kun Umbrel-solmusi on asennettu, synkronoitu ja oikein konfiguroitu. Miten ylläpidät sitä päivittäin?



### Laitteiden pitäminen terveinä



Luotettava solmu alkaa vakaalla laitteistolla. Varmista, että solmun sisältävä kone on asianmukaisesti tuuletettu, Dust-vapaa ja asennettu kuivaan ympäristöön, poispäin kaikista lämmön ja kosteuden lähteistä. Vältä sen ahtautta ahtaaseen tilaan ja valitse hyvin tuulettuva paikka.



Raspberry Pi -tietokoneissa ja minitietokoneissa Dust tukkii lopulta jäähdytyselementit, mikä nostaa lämpötilaa ja johtaa throttlingiin (resurssien käytön vapaaehtoiseen rajoittamiseen), mikä puolestaan johtaa solmun hyötysuhteen heikkenemiseen. Siksi suosittelen puhdistamaan ilmanottoaukon ja tuulettimen säännöllisesti, mieluiten muutaman kuukauden välein.



Varmista, että käytät laadukasta Supply-verkkolaitetta, sillä epävakaa jännite voi johtaa järjestelmän vioittumiseen ja aiheuttaa jopa tulipalon vaaran. Ihannetapauksessa sinun tulisi käyttää koneen valmistajan toimittamaa alkuperäistä Supply-virtaa. Varo myös Joule-ilmiöstä johtuvaa ylikuumenemista pistorasioissa: noudata aina suurinta sallittua tehoa äläkä koskaan kytke useita pistorasioita kaskadiin.



Suosittelen myös investoimaan UPS:ään. Tämä suojaa solmua äkillisiltä pysäytyksiltä, mahdollistaa Umbrelin puhtaan sammuttamisen katkoksen sattuessa ja varmistaa toiminnan jatkuvuuden mikrokatkosten tai lyhytaikaisten vikojen aikana.



Tallennuspuolella kannattaa pitää silmällä edistymistä: jos levy lähestyy kyllästymistä, harkitse tilan vapauttamista (poista käyttämättömät sovellukset, säädä indeksointiasetuksia) tai siirry suurempaan SSD-levyyn. Täyden Bitcoin-solmun haittapuolena on, että sen tallennustilavaatimukset kasvavat jatkuvasti, koska uusi lohko luodaan 10 minuutin välein eikä vanhoja lohkoja voi poistaa (ellei solmu ole pruned). Siksi suosittelen, että varaat laitteistoa hankkiessasi riittävän suuren kapasiteetin (vähintään 2 TB).



### Päivitys



Solmupäivitykset ovat tärkeitä kolmesta syystä: ensinnäkin tietoturva (haavoittuvuuskorjaukset, verkon koventaminen ja DoS-suojaus), toiseksi yhteensopivuus (relekäytäntöjen muutokset, formaattimuutokset ja protokollan päivitykset) ja kolmanneksi luotettavuus ja suorituskyky (virheiden korjaukset, resurssien kulutus ja muut parannukset). Tarkista siis säännöllisesti, että UmbrelOS ja sovelluksesi ovat ajan tasalla:





- Järjestelmän päivittäminen: Avaa asetusvalikko ja napsauta "*Check for Update*" -painiketta parametrin "*UmbrelOS*" vieressä.



![Image](assets/fr/042.webp)





- Päivittääksesi sovelluksia: Mene App Storeen. Jos jokin sovelluksistasi vaatii päivittämistä, Interface:n oikeaan yläkulmaan ilmestyy painike, jossa on punainen kupla. Napsauta sitä ja päivitä sitten kukin sovellus.



Suorita tämä toimenpide säännöllisesti, jotta käyttöjärjestelmä ja sovellukset pysyvät ajan tasalla.



### Varmuuskopiot



Jos käytät Bitcoin-solmua vain transaktioiden validointiin ja jakeluun, mutta lompakoitasi hallinnoidaan Umbrelin ulkopuolella (esimerkiksi Hardware Wallet:llä ja Sparrow wallet:lla), ei ole mitään syytä varmuuskopioida suoraan Umbreliin. Tässä tapauksessa olennainen varmuuskopio on edelleen ulkoisen Wallet-solmusi palautuslause ja Descriptor, ja tämä pätee riippumatta siitä, käytätkö omaa solmua vai et. Mikään ei siis muutu aiemmasta kokoonpanostasi.



Toisaalta, riippuen Umbrelissa käyttämistäsi lisäsovelluksista, varmuuskopioita voidaan tarvita lisää. Näin on erityisesti silloin, jos käytät Lightning-solmua Umbrelissa. Tässä tapauksessa on ehdottoman tärkeää varmuuskopioida Lightning-solmun asennuksen yhteydessä toimitettu seed. seed:n lisäksi tarvitaan ajantasainen ***Static Channel Backup (SCB)***, jotta Lightning-solmun voi palauttaa ongelmatilanteessa. SCB:n avulla voit palauttaa varasi sulkemalla kanavat väkisin. Jos seed tai SCB puuttuu, Lightning-solmua on mahdotonta palauttaa.



Umbrel tarjoaa myös mahdollisuuden varmuuskopioida SCB:n automaattisesti ja dynaamisesti palvelimilleen Torin kautta, jotta varmistetaan, että ajantasainen tiedosto on aina saatavilla. Tässä tapauksessa solmun palauttamiseen tarvitaan vain seed.



Käymme näitä seikkoja yksityiskohtaisesti läpi seuraavalla LNP202-kurssilla.



### Päivittäinen toimintavarmuus



Käytä Interface Umbreliin pitkää, yksilöllistä ja satunnaista salasanaa ja muista aktivoida kaksitekijätodennus (2FA). Jos sovelluksissa on sekä salasana- että 2FA-suojaus, aktivoi aina molemmat ja vaihda oletussalasanat.



Älä koskaan avaa kojelautaa Internetiin ilman suojattua yhdyskäytävää (kuten VPN, Tor tai vain paikallinen yhteys). Rajoita asentamiesi sovellusten määrää ja poista säännöllisesti ne sovellukset, joita et enää tarvitse, jotta hyökkäyspinta pienenee.



Jos haluat syventää tietämystäsi tietoturvasta yleensä, suosittelen sinua tutustumaan tähän toiseen ilmaiseen kurssiin:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnoosi ja itseapu



Jos Umbrelissasi on vika, käytä ensin generate-diagnostiikkapakettia UmbrelOS:n tai kyseisen sovelluksen vianmääritysosion kautta ja käynnistä sitten sovellus puhtaasti uudelleen. Yritä tarvittaessa myös koko järjestelmän uudelleenkäynnistystä.



Jos ongelma jatkuu, suosittelen, että [liityt Umbrelin käyttäjäyhteisön Discordiin](https://discord.gg/efNtFzqtdx). Aloita tekemällä haku selvittääksesi, onko joku jo kohdannut saman ongelman ja löytänyt ratkaisun. Jos ei, voit lähettää viestin `general-support`-kanavalle. Voit myös käyttää [Umbrelin foorumia](https://community.umbrel.com/).



Näillä alueilla voit paitsi seurata tietoturvailmoituksia ja -päivityksiä myös esittää kysymyksiä ja auttaa muita käyttäjiä. Näissä keskusteluissa löydetään usein parhaita käytäntöjä.



Näiden yksinkertaisten tapojen avulla Umbrel-solmusi pysyy vakaana, turvallisena ja hyödyllisenä sekä sinulle että Bitcoin-verkolle.




## IBD:n ja vertaisryhmän löytämisprosessin ymmärtäminen


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Bitcoin-solmusi käynnistyy ilman ennakkotietoja tapahtumahistoriasta. Aluksi se on vain tietokone, jossa on ohjelmisto (Bitcoin core tai vastaava). Jotta siitä tulisi täysin synkronoitu ja toimiva Bitcoin-solmu, sen on paikallisesti rekonstruoitava Ledger:n tila tarkistamalla kaikki lohkot, jotka on julkaistu Genesis-lohkon (lohko 0, jonka Satoshi Nakamoto julkaisi 3. tammikuuta 2009) jälkeen. Tätä vaihetta kutsutaan **IBD:ksi (_Initial Block Download_)**.



IBD koostuu jokaisen lohkon ja transaktion lataamisesta ja tarkistamisesta erikseen konsensussääntöjä soveltaen, jotta voidaan rakentaa oma versio Blockchain:sta. Tarkoituksena ei ole vain hakea kopio tarkistamattomista tiedoista, vaan päätyä täysin itsenäisesti samaan lopputulokseen kuin verkon rehellinen enemmistö.



![Image](assets/fr/092.webp)



### IBD:n virstanpylväät



Synkronointi alkaa vaiheesta _**headers-first**_. Solmusi pyytää lohko-otsakkeiden sarjan useilta vertaisverkoilta ja tarkistaa kunkin osalta Proof of Work:n, vaikeussäädön, syntaksin sekä Timestamp:n ja versionumeron säännöt. Lyhyesti sanottuna se varmistaa, että jokainen vastaanotettu otsikko on konsensussääntöjen mukainen.



![Image](assets/fr/093.webp)



Muistutuksena mainittakoon, että Bitcoin-lohko koostuu 80 tavun otsikosta ja transaktioluettelosta. Lohkon sormenjälki saadaan soveltamalla kaksinkertaista SHA-256 Hash:tä tähän otsikkoon, joka sisältää kuusi kenttää:




- versio
- Edellisen lohkon Hash
- Merkle Root liiketoimista
- Timestamp (suurempi kuin 11 edellisen lohkon mediaaniaika)
- vaikeustavoite
- Nonce



![Image](assets/fr/094.webp)



Tapahtumat siirretään Merkle Tree:een. Tämä on rakenne, joka tiivistää suuren datajoukon (tässä tapauksessa kaikki lohkon transaktiot) aggregoimalla niiden hasheja asteittain kaksi kerrallaan yhteen "juureen", mikä osoittaa, että elementti kuuluu joukkoon (ja havaitsee mahdolliset muutokset). Tällä tavoin kaikki transaktion muutokset muuttavat myös Merkle Tree:n juurta ja siten lohkon otsikon sormenjälkeä. SegWit on ottanut käyttöön erillisen ylimääräisen Commitment:n evästeitä (allekirjoituksia) varten, joka on sijoitettu kolikkopankkiin.



![Image](assets/fr/095.webp)



Tämän _**otsikot ensin**_ -vaiheen avulla solmu tunnistaa haaran, jossa on eniten työtä (riippumatta sen lohkojen määrästä), ja tämä on haara, johon Bitcoin-solmut synkronoivat. Kun tämä haara on tunnistettu, solmu lataa lohkojen sisällön rinnakkain useista yhteyksistä ja validoi sitten jokaisen transaktion: muoto, skriptien pätevyys (paitsi `assumevalid=1`), määrät ja se, ettei ole kaksinkertaisia menoja. Jokaisen onnistuneen tarkistuksen yhteydessä `chainstate/`-tietokantaan päivitetään kuluttamattomien kolikoiden (UTXO-sarja) tämänhetkinen tila: käytetyt lähdöt poistetaan ja uudet kelvolliset lähdöt lisätään.



Mempool sen sijaan astuu kuvaan vain lähestyttäessä ketjun kärkeä: niin kauan kuin solmu on myöhässä, sillä ei ole vireillä olevia tapahtumia tallennettavaksi.



Kun IBD on valmis, solmu siirtyy normaaliin vaiheeseensa: se validoi uudet lohkot, kun ne julkaistaan, ylläpitää Mempool:nsä vireillä olevia transaktioita välityssääntöjensä mukaisesti, välittää transaktioita ja lohkoja ja hallinnoi ketjun uudelleenjärjestelyjä.



### AssumeValid



Bitcoin core sisältää mekanismin, joka on suunniteltu lyhentämään aikaa, joka kuluu ennen kuin solmu on täysin toimintakykyinen, säilyttäen samalla autonomisen todentamisperiaatteen olennaisen sisällön: AssumeValid.



Parametri `assumevalid` perustuu aiempaan vertailulohkoon, jonka Hash on integroitu jokaiseen ohjelmistoversioon. Jos solmu havaitsee IBD:n aikana, että tämä lohko on todellakin haarassa, jossa on eniten työtä, se voi jättää huomiotta kaikkien tätä edeltävien tapahtumien käsikirjoitusvarmennuksen.



Kaikki muut säännöt (lohkorakenne, Proof of Work, kokorajat, transaktiomäärät, UTXO:t jne.) pysyvät täysin todennettuina. Ainoastaan tätä vertailulohkoa edeltävien skriptien laskenta jätetään huomiotta. Suorituskyky paranee merkittävästi IBD:ssä, koska allekirjoitusten tarkistaminen muodostaa suuren osan suorittimen kuormituksesta. Tämän vertailulohkon jälkeen todentaminen palaa normaaliin tilaansa.



Voit pakottaa kaikkien skriptien täydellisen validoinnin poistamalla tämän mekanismin käytöstä, mutta IBD:n kesto on paljon pidempi, käyttämällä parametria `assumevalid=0` tiedostossa `Bitcoin.conf`.



### OletetaanUTXO



`assumeutxo` on toinen olemassa oleva parametri, mutta toisin kuin `assumevalid`, se ei ole oletusarvoisesti aktivoitu. Tämän mekanismin avulla ohjelmisto voi ladata tilannekuvan UTXO-sarjasta ja sen metatiedoista ja pitää sitä alustavasti viitetilana sen jälkeen, kun on varmistettu, että otsikot johtavat todellakin Blockchain:een, jossa on eniten työtä.



Solmu on siten nopeasti toimintakunnossa yleisiä käyttötarkoituksia varten (RPC, lompakoiden yhdistäminen jne.) ja käynnistää samalla taustalla oman UTXO-sarjansa täydellisen, todennetun rekonstruktion. Kun tämä vaihe on valmis, alkuperäinen tilannekuva korvataan paikallisesti rekonstruoidulla tilalla. Tämä lähestymistapa erottaa solmujen nopean käyttöönoton täydellisestä todentamisesta vaarantamatta jälkimmäistä.



### Vertaisten löytäminen: Miten solmusi löytää Bitcoin-verkon?



Kun solmu käynnistyy ensimmäistä kertaa, se ei vielä tunne yhtään vertaisverkkoa. Sen on kuitenkin löydettävä muita Bitcoin-solmuja Internetistä pyytääkseen otsikoita ja sitten lohkoja, jotta se voi suorittaa IBD:nsä loppuun. Näiden yhteyksien aloittamiseksi Bitcoin core noudattaa priorisoitua logiikkaa.



![Image](assets/fr/096.webp)



Kun solmu käynnistyy uudelleen sen jälkeen, kun sitä on jo käytetty, Core yrittää ensin muodostaa uudelleen yhteyden lähteviin vertaisverkkoihin, jotka on rekisteröity ennen sammuttamista ja joiden tiedot on tallennettu tiedostoon `anchors.dat`. Sen jälkeen se käyttää IP Address -kirjaa **`peers.dat`**, johon on tallennettu luettelo aiemmin kohdatuista vertaisverkoista, saadakseen uudelleen yhteyden niihin. Tämä on yksinkertaisesti paikallinen tiedosto, jota Core päivittää ja pitää yllä. Toisaalta uuden, juuri käynnistetyn solmun kohdalla nämä kaksi tiedostoa ovat tyhjiä, koska se ei ole vielä koskaan ollut yhteydessä muihin Bitcoin-solmuihin.



Tässä tapauksessa ohjelmisto kysyy _**DNS-siemeniä**_. Nämä ovat [tunnustettujen ekosysteemin kehittäjien ylläpitämiä palvelimia](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), jotka palauttavat luettelon oletettujen aktiivisten solmujen IP-osoitteista. Näiden osoitteiden avulla uusi solmu voi aloittaa ensimmäiset yhteydet ja pyytää tarvittavat tiedot IBD:ltä. Tässä on luettelo tähän mennessä aktiivisista *DNS-siemenistä* (elokuu 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: "seed.btc.petertodd.net"
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: gW-568.Mainnet.achownodes.xyz.xyz



Suurimmassa osassa tapauksia *DNS-siemenet* riittää ensimmäisten yhteyksien luomiseen muihin solmuihin. Jos nämä palvelimet eivät poikkeuksellisesti vastaa 60 sekunnin kuluessa, solmu siirtyy toiseen menetelmään: gW-569:n koodiin on sisällytetty [yli 1 000 osoitteen staattinen luettelo](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) _siemensolmuista_, jota päivitetään säännöllisesti. Jos kaksi ensimmäistä IP-osoitteiden hankintamenetelmää epäonnistuvat, tämä viimeisin ratkaisu luo alkuyhteyden, josta solmu voi sitten pyytää uusia IP-osoitteita.



![Image](assets/fr/097.webp)



Viimeisenä keinona voit manuaalisesti Supply IP-osoitteita `peers.dat`-tiedoston kautta pakottaa tietyt yhteydet.



Kun Address:n sisäinen johtaja on käynnistetty, se monipuolistaa lähteitä (erilliset autonomiset verkot, Clearnet ja Tor sekä eri maantieteelliset alueet) vähentääkseen topologisen eristyneisyyden riskiä. Solmu luo nämä lähtevät yhteydet (yhteydet, jotka se valitsee itse ja jotka ovat siksi turvallisempia).



Jos solmusi kuuntelee avointa porttia (oletusarvoisesti 8333), se hyväksyy saapuvat yhteydet. Nämä vahvistavat verkon yleistä häiriönsietokykyä tarjoamalla yhteyspisteen uusille solmuille, mutta eivät tuo mitään erityistä hyötyä omalle IBD:lle. Jos solmusi toimii Torilla, logiikka pysyy samana, mutta käytetyt osoitteet ovat `.onion`-palveluja.




## Bitcoin-solmun anatomia


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Kun solmu on suorittanut alkusynkronoinnin, se tallentaa paikallisesti useita toisiaan täydentäviä tietokokonaisuuksia, joiden avulla se voi validoida lohkoja ja transaktioita, palvella verkon vertaisverkkoja ja käynnistyä uudelleen nopeasti säilyttäen tilansa. solmussa on olennaisia 3 päätiiliä:




- gW-402 **lohkot** tallennettuna levylle,
- avain-arvotietokannassa ylläpidetty **UTXO-sarja**,
- ja **Mempool** tallennetaan RAM-muistiin ja sarjoitetaan määräajoin.



Lisäksi useat aputiedostot (vertaistiedostot, maksuarviot, poissulkemisluettelot, lompakot jne.) täydentävät kuvaa. Tutustutaanpa kaikkien näiden tiedostojen rooliin.



### Missä solmun tiedot itse asiassa sijaitsevat?



Oletusarvoisesti Bitcoin core tallentaa tiedot tiettyyn työhakemistoon. GNU/Linuxissa tämä on yleensä `~/.Bitcoin/`, Windowsissa `%APPDATA%\Bitcoin/` ja macOS:ssä `~/Library/Application Support/Bitcoin/`. Jos käytät pakattua ratkaisua (esim. solmun jakelussa), tämä hakemisto voidaan asentaa muualle, mutta sen rakenne pysyy samana. Alla kuvatut tärkeät alikansiot ja tiedostot sijaitsevat edelleen tässä.



![Image](assets/fr/098.webp)



### Lohkot



Blockchain on siis lohkojen kokoelma. Full node tallentaa nämä lohkot peräkkäisinä tasotiedostoina ja ylläpitää rinnakkaista indeksiä nopeaa hakua varten. Tarvittaessa (uudelleenjärjestely, Wallet uudelleenkatselu, vertaispalvelu) nämä tiedot luetaan uudelleen sellaisenaan.



**Huomautus:** Uudelleenjärjestäytyminen eli resynkronisaatio on ilmiö, jossa Blockchain:n rakenne muuttuu, koska samalla korkeudella on kilpailevia lohkoja. Tämä tapahtuu, kun osa Blockchain:stä korvataan toisella ketjulla, jossa on enemmän kertynyttä työtä. Nämä uudelleensynkronoinnit ovat luonnollinen osa Bitcoin:n toimintaa, jossa eri louhijat voivat löytää uusia lohkoja lähes samanaikaisesti, jolloin Bitcoin-verkko jakautuu kahtia. Tällaisissa tapauksissa verkko voi väliaikaisesti jakautua kilpaileviin ketjuihin. Lopulta, kun yhteen näistä ketjuista kertyy enemmän työtä, solmut hylkäävät muut ketjut, ja niiden lohkoista tulee "vanhentuneita lohkoja" tai "orpoja lohkoja" Tätä prosessia, jossa yksi ketju korvataan toisella, kutsutaan uudelleensynkronoinniksi.



#### Blk*.dat-tiedostot (raakalohkotiedot)



Vastaanotetut ja validoidut lohkot kirjoitetaan peräkkäisiin säiliöihin nimeltä `blkNNNNNNN.dat`, jotka on tallennettu `blocks/`-kansioon. Kukin tiedosto täytetään peräkkäin, kunnes sen enimmäiskoko on 128 MiB, jolloin Core avaa seuraavan tiedoston. Sisällä jokainen lohko on sarjoitettu verkkomuodossa, ja sitä edeltää maaginen tunniste ja pituus. Tämä organisointi mahdollistaa nopean kirjoittamisen levylle ja helpottaa lohkopalvelua vertaisten synkronoimiseksi.



![Image](assets/fr/099.webp)



pruned-tilassa solmu säilyttää vain viimeisimmän ikkunan näistä tiedostoista, jotta levyn jalanjälkeä voidaan rajoittaa. Se poistaa vanhimmat `blk*.dat`-säiliöt heti, kun määritetty tilatavoite on saavutettu, mutta säilyttää samalla riittävästi historiaa, jotta se pysyy johdonmukaisena parhaiten tunnetun ketjun kanssa. Indeksi ja UTXO-sarja pysyvät normaaleina, jolloin seuraavat transaktiot ja lohkot voidaan validoida.



#### Rev*.dat-tiedostot (peruutustiedot)



Jotta uudelleenjärjestelyn aikana voidaan palata ajassa taaksepäin, Core tallentaa jokaisen `blk`-tiedoston kanssa samanaikaisesti `revNNNNNNN.dat`-tiedoston osoitteeseen `blocks/`. Tämä tiedosto sisältää tiedot, joita tarvitaan lohkon vaikutuksen peruuttamiseksi UTXO-joukkoon: jokaisen lohkon kuluttaman tuotoksen osalta tallennetaan vastaavan UTXO:n edellinen tila (määrä, käsikirjoitus, korkeus...). Jos lohko keskeytyy, solmu voi nopeasti palauttaa edellisen tilan ilman, että koko ketjua tarvitsee skannata uudelleen.



![Image](assets/fr/100.webp)



#### Lohkoindeksi (lohkot/indeksi)



Lohkon etsiminen suoraan tasotiedostoista olisi liian aikaa vievää. Core ylläpitää sen vuoksi LevelDB-tietokantaa osoitteessa `blocks/index/`, jossa luetellaan jokaisen tunnetun lohkon metatiedot, kuten Hash, korkeus, validointitilanne, `blk`-tiedosto ja offset, jossa lohko sijaitsee. Kun vertaisohjelma pyytää lohkoa tai kun sisäisen komponentin on päästävä tiettyyn lohkoon käsiksi, tämä indeksi tarjoaa nopean pääsyn. Ilman tätä indeksiä tarvittaisiin liian monta operaatiota.



![Image](assets/fr/101.webp)



#### Valinnaiset indeksit (indexes/)



Jotkin indeksit ovat valinnaisia ja oletusarvoisesti poissa käytöstä, koska ne lisäävät levyn jalanjälkeä:




- `indexes/txindex/`, jonka olemme jo maininneet, tarjoaa transaktio → sijainti -kartoitustaulukon, jonka avulla on mahdollista hakea mikä tahansa vahvistettu transaktio tietämättä sitä sisältävää lohkoa. Tämä on hyödyllistä Wallet `getrawtransaction` -tyyppisissä RPC-kyselyissä, mutta se on melko kallista.
- indexes/blockfilter/`, joka voi sisältää kompakteja lohkosuodattimia (BIP157/158) ohuille asiakkaille. Nämä rakenteet nopeuttavat asiakaspuolen tarkistusta indeksointisolmun lisätallennustilan kustannuksella.



### UTXO-sarja (ketjutila)



UTXO-malli (*Käyttämättä jääneet tapahtumatuotokset*) on Bitcoin:n kirjanpidollinen esitys: jokainen käyttämättä jäänyt tuotos on käytettävissä oleva "Coin", jota voidaan käyttää tulevan tapahtuman syötteenä.



![Image](assets/fr/102.webp)



Kaikkien näiden osien kokonaisuus tietyllä hetkellä T muodostaa UTXO-sarjan: laajan luettelon kaikista nyt saatavilla olevista osista. Tätä tilaa solmu käyttää päättäessään, käytetäänkö transaktiossa laillisia yksiköitä, joita ei ole jo käytetty edellisessä transaktiossa (Double-spending:n välttämiseksi).



![Image](assets/fr/103.webp)



UTXO-sarja on tallennettu `chainstate/`-kansioon kompaktina LevelDB-tietokantana. Jokainen osa yhdistää avaimen, joka on johdettu transaktion Hash:sta, ja lähtöindeksin arvoon, joka sisältää: summan, `scriptPubKey`-lukituksen, luomislohkon korkeuden ja coinbase-indikaattorin.



![Image](assets/fr/104.webp)



Solmu ylläpitää LevelDB:n yläpuolella olevaa muistin välimuistia, joka kestää usein toistuvat luku- ja kirjoitusoperaatiot. Parametrilla `dbcache` voidaan muuttaa tämän välimuistin kokoa: mitä suurempi se on, sitä enemmän muistin käyttömahdollisuuksia IBD ja nykyinen validointi hyötyvät, mutta RAM-muistin kulutus kasvaa. Kun Miner löytää uuden lohkon, solmu poistaa UTXO-joukosta lohkoon sisältyvien transaktioiden kuluttamat (tai kuluttamat) tuotokset ja lisää uudet tuotokset.



Teoriassa voisimme validoida transaktion tarkistamalla lohkohistorian uudelleen ja tarkistamalla, että lähtöä ei ole koskaan käytetty. Käytännössä tämä olisi kuitenkin aivan liian aikaa vievää, koska koko Blockchain olisi skannattava jokaisen uuden tapahtuman kohdalla. UTXO-sarja tarjoaa näin ollen vähimmäisnäkymän, jota tarvitaan Double-spending:n puuttumisen osoittamiseksi paikallisesti ja kohtuullisessa ajassa.



Huomaa, että UTXO-joukko on usein Bitcoin:n hajauttamista koskevien huolenaiheiden ytimessä, koska sen koko kasvaa luonnollisesti nopeasti. Tämä johtuu osittain Bitcoin:n hinnan noususta, joka kannustaa osien pirstaloitumiseen, ja osittain järjestelmän kasvavasta käyttöönotosta: mitä enemmän käyttäjiä on, sitä suurempi on UTXO:iden kysyntä.



![Image](assets/fr/105.webp)



UTXO-sarjan kasvu johtuu myös Bitcoin:n yksinkertaisten maksutapahtumien rakenteesta. Kun maksat maksun, kulutat yhden UTXO:n syötteenä ja luot kaksi uutta UTXO:ta tuotoksena (toinen maksua ja toinen Exchange:aa varten). Ketjuanalyysin heuristiikka, nimeltään CIOH (*Common Input Ownership Heuristic*), tarjoaa lisäkannustimen välttää Coin:n konsolidointia.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Koska osa siitä on pidettävä RAM-muistissa, jotta tapahtumat voidaan tarkistaa kohtuullisessa ajassa, UTXO-sarja voi vähitellen tehdä Full node:n käytöstä liian kallista. Tämän ongelman ratkaisemiseksi on jo olemassa muutamia ehdotuksia, erityisesti [Utreexo](https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool on paikallinen joukko kelvollisia tapahtumia, jotka on vastaanotettu mutta joita ei ole vielä vahvistettu. Muistutettakoon, että "vahvistettu tapahtuma" on sellainen, joka on sisällytetty kelvolliseen lohkoon. Kukin solmu ylläpitää omaa Mempool:a, joka voi poiketa verkon muiden solmujen Mempool:sta riippuen seuraavista tekijöistä:




- gW-614:lle parametrin `maxmempool` kautta varattu koko: solmuun, jolla on suurempi Mempool, mahtuu enemmän tapahtumia kuin solmuun, jolla on pienempi Mempool (ellei jälkimmäinen tyhjene);
- gW-433-säännöt: Nämä ovat osajoukko solmun välityssääntöjä, ja niissä määritellään ominaisuudet, jotka vahvistamattoman tapahtuman on täytettävä, jotta se voidaan hyväksyä Mempool:ssä;
- transaktioiden perkolaatio: eri tekijöistä johtuen tietty transaktio on saattanut levitä yhteen verkon osaan, mutta ei ole vielä saavuttanut toista osaa.



On tärkeää huomata, että solmujen mempoolilla ei ole konsensusarvoa. Bitcoin toimii täydellisesti, vaikka jokaisella solmulla olisi eri Mempool. Viime kädessä arvovaltaiset lohkot ovat aina Blockchain:ään lisätyt lohkot. Vaikka solmu esimerkiksi aluksi hylkäisi tietyn transaktion Mempool:ssä (joka on konsensussääntöjen mukaan pätevä), sen on pakko hyväksyä se, jos se lopulta sisällytetään lohkoon, jolla on pätevä Proof of Work. Jos se ei tee näin ja hylkää kyseisen lohkon, vaikka se noudattaisi konsensussääntöjä, se aiheuttaisi Hard Fork:n eli uuden, erillisen Bitcoin:n luomisen, jossa se olisi yksin.



#### Muistipolitiikka ja -hallinta



Kun maksutapahtuma vastaanotetaan, Core suorittaa sarjan tarkistuksia konsensussääntöjen (syntaksi, kelvolliset skriptit, ei tuplakäyttöä jne.) ja Mempool-sääntöjen perusteella, jotka ovat paikallinen käytäntö (RBF, vähimmäismaksukynnykset, datarajoitus OP_RETURN:ssä jne.). Jos tapahtuma noudattaa näitä sääntöjä, se tallennetaan muistiin.



Mempool:n kokoa rajoittaa parametri `maxmempool` tiedostossa `Bitcoin.conf` (lisää tästä seuraavassa luvussa). Oletusarvoisesti rajoitus on 300 Mt. Kun se on täynnä, solmu nostaa dynaamisesti minimiveloituskynnystä ja poistaa ensin vähiten kannattavat tapahtumat (eli se säilyttää tapahtumat, jotka pitäisi louhia ensin). Liian vanhat transaktiot voivat myös vanhentua määritetyn viiveen jälkeen.



#### Mempool pysyvyys levyllä



Uudelleenkäynnistysten nopeuttamiseksi Core serialisoi Mempool:n tilan säännöllisesti tiedostoon `Mempool.dat`, kun solmu sammutetaan. Muistiin jäävän varsinaisen Mempool:n lisäksi Core tallentaa tämän `Mempool.dat`-tiedoston levylle. Kun solmu käynnistetään seuraavan kerran, se lataa tämän tilannekuvan uudelleen ja poistaa kaiken sen, mikä ei ole enää voimassa nykyisen Blockchain:n osalta.



### Aputiedostot ja tietokannat



Useat muut tiedostot, jotka ovat samalla tasolla kuin `blocks/`, `chainstate/` ja `indexes/`, osallistuvat järjestelmän asianmukaiseen toimintaan:




- `peers.dat` pitää yllä IP Address -luetteloa mahdollisista vertaisverkoista, joita syötetään alkuperäisen DNS-tiedonhaun, verkkovaihdon ja manuaalisten lisäysten avulla. Kun solmu käynnistyy, se voi käyttää tätä tiedostoa luodakseen lähteviä yhteyksiä.
- Kun solmu kytketään pois päältä, `anchors.dat` tallentaa lähtevien vertaisverkkojen osoitteet, jotta voit yrittää ottaa niihin yhteyttä nopeasti uudelleen, kun käynnistät järjestelmän seuraavan kerran.
- `banlist.json` sisältää operaattorin tai solmun päättämiä paikallisia kieltoja (toistuva virheellinen käyttäytyminen), joilla estetään solmua muodostamasta uudelleen yhteyksiä tai hyväksymästä yhteyksiä kyseisiltä vertaisverkoilta.
- maksuestimaattorit.dat tallentaa havaittujen vahvistusten aikahorisonttitilastot, joita maksuestimaattori käyttää ehdottaessaan maksuja, jotka ovat yhdenmukaisia tapahtuman luomisen yhteydessä valittujen viivetavoitteiden kanssa.
- gW-446.conf` sisältää solmun konfigurointiparametrit. Täällä voit säätää välityssääntöjä. Kerron tästä lisää seuraavassa luvussa.
- `settings.json` sisältää lisäparametreja tiedostoon `Bitcoin.conf`.
- `debug.log` on diagnostinen tekstiloki, jota voidaan käyttää solmun toiminnan ymmärtämiseen vian sattuessa.
- gW-448.pid` tallentaa prosessin tunnisteen ajon aikana, jolloin muut sovellukset tai skriptit voivat helposti tunnistaa bitcoind:n (*Bitcoin daemon*) ja olla sen kanssa vuorovaikutuksessa tarvittaessa. Se luodaan solmun käynnistyksen yhteydessä ja poistetaan sen sammutuksen yhteydessä.
- `ip_asn.map` on IP → ASN-kartoitustaulukko (itsenäinen järjestelmä), jota käytetään bucketingiin ja vertaisverkon hajauttamiseen (`-asmap`-vaihtoehto).
- `onion_v3_private_key` tallentaa Tor v3 -palvelun yksityisen avaimen, kun `-listenonion`-vaihtoehto on käytössä, jotta onion Address pysyy vakaana uudelleenkäynnistysten välillä.
- `i2p_private_key` tallentaa I2P:n yksityisen avaimen, kun käytetään `-i2psam=`, jotta voidaan muodostaa lähteviä ja mahdollisesti saapuvia yhteyksiä I2P:llä.
- `.cookie` sisältää hetkellisen RPC-todennuksen token (luodaan käynnistettäessä ja poistetaan sammutettaessa), kun evästetodennusta käytetään. Tätä voidaan käyttää esimerkiksi Wallet-ohjelmiston yhdistämiseen.
- `.lock` on datahakemiston lukitus, joka estää useita instansseja kirjoittamasta samaan datahakemistoon samanaikaisesti.
- `guisettings.ini.bak` on GUI-asetusten (*Bitcoin Qt*) automaattinen tallennus, kun `-resetguisettings`-vaihtoehtoa käytetään.



Kuten näimme tämän BTC 202 -kurssin ensimmäisissä osissa, Bitcoin core on sekä Bitcoin-solmuohjelmisto että Wallet. Se ei kuitenkaan välttämättä ole ratkaisu, jota suosittelisin lompakoiden hallintaan, sillä sen Interface on edelleen perusluonteinen ja sen toiminnot ovat rajalliset verrattuna nykyaikaisiin ohjelmistoihin, kuten Sparrow tai Liana. Core sisältää myös tiedostoja lompakoiden hallintaa varten:





- `wallets/` on oletushakemisto, jossa on yksi tai useampi;
- `wallets/<nimi>/Wallet.dat` on Wallet:n SQLite-tietokanta (avaimet, kuvaajat, tapahtumien metatiedot jne.);
- wallets/<name>/Wallet.dat-journal` on SQLiten rollback-loki.



Yhteenvetona Bitcoin core:n tiedostorakenne on seuraava:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Uuden lohkon validointipolku



Saatuaan uuden lohkon solmusi tarkistaa Proof of Work:n ja yleisemmin konsensussääntöjen noudattamisen. Jos kaikki on kunnossa, se soveltaa muutoksia transaktio transaktio kerrallaan UTXO -joukkoonsa: se tarkistaa, että jokainen merkintä kuluttaa olemassa olevia UTXO:ita voimassa olevalla käsikirjoituksella, poistaa nämä UTXO:t ja lisää uudet ulostulot. Jos kaikki on kelvollista, muutokset siirretään `chainstate/`:iin.



Samanaikaisesti peruutustiedot kirjoitetaan tiedostoon `rev*.dat` ja metatiedot indeksiin `blocks/index/`. Lohko sarjallistetaan sitten oikeaan `blk*.dat`-tiedostoon. Uudelleenjärjestelyn yhteydessä solmu lukee `rev*.dat`-tiedostoa käänteisesti irrottaakseen hylättyjä lohkoja, palauttaakseen UTXO-sarjan ja liittääkseen sitten uuden parhaan ketjun lohkot.





## Bitcoin.conf-tiedoston ymmärtäminen


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Bitcoin.conf-tiedosto on Bitcoin core:n Interface:n pääkonfiguraatiotiedosto. Sen avulla voit säätää solmun käyttäytymistä ja parametreja ilman, että sinun tarvitsee kääntää sen lähdekoodia uudelleen tai tehdä komentorivimuutoksia. Konkreettisesti se on tavallinen tekstitiedosto, joka on jäsennelty avain-arvopareilla, mikä tarkoittaa, että tiedoston jokainen rivi viittaa tiettyyn parametriin (avain) ja siihen liittyvään arvoon, jota voidaan muuttaa kyseisen parametrin säätämiseksi.



Verkko-, tapahtumien välitys-, suorituskyky-, indeksointi-, lokitus- ja RPC-käyttömahdollisuusparametrit voidaan määritellä Bitcoin.conf-tiedostossa. Tämä konfigurointitiedosto ei kuitenkaan koskaan muuta protokollan konsensussääntöjä: se määrittää ainoastaan solmun paikallisen politiikan (välityssäännöt), tavan, jolla se muodostaa yhteyksiä, indeksoi ja paljastaa palveluja.



### Sijainti ja prioriteetti



Oletusarvoisesti `Bitcoin.conf` sijaitsee Bitcoin core:n datahakemistossa. Tämä on se kuuluisa hakemisto, jonka mainitsimme edellisessä luvussa. Bitcoin core ei kuitenkaan luo tätä tiedostoa automaattisesti, paitsi tietyissä ympäristöissä, kuten Umbrelissa. Jos sitä ei ole vielä olemassa, sinun on generate luotava se itse luomalla tiedosto nimeltä `Bitcoin.conf` ja avaamalla se tekstieditorilla muutosten tekemistä varten.



Bitcoin.conf-tiedostossa määritellyt parametrit voidaan ohittaa kahdella tasolla:




- `settings.json` (kirjoitettu dynaamisesti Interface-grafiikan tai jonkin RPC:n toimesta),
- ja komentorivien kautta muutetut vaihtoehdot.



Huomaa, että kaikki muutokset tiedostoon `Bitcoin.conf` vaativat solmun uudelleenkäynnistyksen tullakseen voimaan.



### Muoto ja rakenne



Bitcoin.conf-tiedoston muoto on siis hyvin yksinkertainen: yksi rivi optiota kohti muodossa `option=value`. Tarpeettomat välilyönnit ja tyhjät rivit jätetään huomiotta, ja koodikommentit alkavat `#`:llä.



Lähes kaikki Boolen vaihtoehdot voidaan poistaa käytöstä etuliitteellä `no`. Esimerkiksi `listen=0` ja `nolisten=1` vastaavat toisiaan versiosta riippuen.



Voit segmentoida kokoonpanon verkon mukaan käyttämällä osioita: (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Vaihtoehtoisesti voit liittää vaihtoehdon nimen eteen sanan `regtest.maxmempool=100`.



### Mitä Bitcoin.conf voi tehdä ja mitä ei voi tehdä?



Kuten edellä on selitetty, konsensussääntöjä ei tietenkään voi määrittää Bitcoin.conf-tiedostossa, koska se voisi luoda Hard Fork:n. Toisaalta monet muut seikat ovat konfiguroitavissa. On 3 hyödyllistä luokkaa, jotka kannattaa pitää mielessä:




- Puhtaasti paikalliset parametrit. Nämä vaikuttavat vain omaan solmuun: välimuistin koko (`dbcache`), pruned-tila (`prune`), valinnaiset indeksit... Ne vaikuttavat koneesi suorituskykyyn, mutta eivät verkkoon.
- Relay- ja Mempool-käytännöt. Nämä päättävät, mitä solmusi hyväksyy, säilyttää ja välittää ennen vahvistusta: vähimmäismaksukynnys (`minrelaytxfee`), Mempool-koko ja säilytysaika (`maxmempool`, `mempoolexpiry`), tapahtumien korvaaminen (RBF)... Nämä säännöt eivät ole osa konsensusta, joten kahdella eri solmulla voi olla erilaiset säännöt ja ne voivat silti olla täysin yhteensopivia. Toisaalta nämä parametrit vaikuttavat Bitcoin-verkkoon (kuten ensimmäisessä osassa selitettiin, erityisesti perkolaatioteorian avulla).
- Verkkoyhteys. Nämä vaihtoehdot määrittävät, miten solmusi löytää vertaisverkkoja, kuuntelee, ylittää NAT:n, käyttää Toria tai välityspalvelinta tai rajoittaa kaistanleveyttä. Ne muokkaavat topologiaasi, mutta eivät muuta tapahtumien välittämistä.



Tämän erottelun ymmärtäminen on tärkeää: jos transaktio ei noudata konsensussääntöjä, solmusi hylkää sen joka tapauksessa. Tiukempi paikallinen käytäntö voi kuitenkin kieltäytyä välittämästä konsensussääntöjen mukaista transaktiota.



### Verkko ja topologia



Ensinnäkin on tärkeää erottaa selvästi toisistaan ne kaksi yhteystyyppiä, joita Bitcoin-solmulla voi olla:




- Lähtevät yhteydet, jotka solmumme aloittaa toiseen solmuun;



![Image](assets/fr/106.webp)





- Saapuvat yhteydet, jotka toinen solmu on käynnistänyt omaan solmuun.



![Image](assets/fr/107.webp)



Nämä kaksi yhteystyyppiä pystyvät täydellisesti vaihtamaan samoja tietoja molempiin suuntiin; kyse ei ole virtaussuunnan rajoittamisesta, vaan ainoastaan yhteyden aloittajan erosta. Solmun näkökulmasta lähteviä yhteyksiä pidetään yleensä turvallisempina, koska aloitamme ne ja valitsemme tarkkaan, mihin solmuun otamme yhteyden, jolloin on epätodennäköistä, että yhteys on haitallinen. Oletusarvoisesti Bitcoin core ylläpitää 10 lähtevää yhteyttä (8 "*full-relay*" + 2 "*block-relay-only*").



Full node lisää verkon arvoa hyväksymällä saapuvia yhteyksiä. Parametri `listen=1` mahdollistaa kuuntelun kyseisen verkon oletusportissa 8333, jolloin nämä saapuvat yhteydet voidaan vastaanottaa clearnetissä. Jotta tämä toimisi, tämän portin on oltava auki myös reitittimessäsi. Jos se ei ole, solmusi toimii edelleen vain lähtevillä yhteyksillä, mikä ei vaikuta Bitcoin:n henkilökohtaiseen käyttöön. Voit itse päättää, sallitko saapuvat yhteydet; mitään "parasta vaihtoehtoa" ei ole olemassa



Jos et halua avata porttia reitittimessäsi, mutta haluat silti hyväksyä saapuvat yhteydet, voit aktivoida parametrin `listenonion=1`. Näin saavutetaan sama tulos, mutta vain Tor-verkon eikä clearnetin kautta.



Verkkotasolla meillä on myös:




- `addnode`: lisää ystävällisen vertaissolmun, johon voi ottaa yhteyttä tavanomaisen löytämisen lisäksi (voidaan määrittää useita kertoja).
- connect`: rajoittaa yhteydet tiukasti tarjottuun Address:een (voidaan määrittää useita kertoja). Core ei muodosta yhteyttä mihinkään muuhun solmuun.
- `seednode`: käytetään vain book-Address:n täyttämiseen, kun yhteys solmuun muodostetaan ja yhteys katkaistaan.
- `maxconnections`: Määrittää saapuvien + lähtevien yhteyksien globaalin enimmäismäärän. Oletusarvoisesti tämä parametri on 125, mikä tarkoittaa, että solmusi ei koskaan hyväksy yli 125 yhteyttä.
- maxuploadtarget`: rajoittaa latauksia kaistanleveyden rajoittamiseksi 24 tunnin liukuvan ikkunan aikana. Tämä yläraja ei uhraa olennaisen tärkeän viimeaikaisen Elements:n etenemistä.
- `onlynet`: rajoittaa lähtevät yhteydet vain valittuihin verkkoihin (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Jos esimerkiksi haluat, että solmusi muodostaa yhteyden Bitcoin-verkkoon vain Torin kautta, voit ottaa parametrin `onlynet=onion` käyttöön ja poistaa saapuvat yhteydet käytöstä (tai sallia yhteydet vain Torin kautta).
- `dnsseed`: sallii tai estää _DNS-siemeniä_ pyytämästä vertaisverkkoja, kun paikallinen Address-varasto on vähissä (oletus: `1`, ellei `-connect` tai `-maxconnections=0`).
- `forcednsseed`: pakottaa pyytämään _DNS-siemeniä_ käynnistyksen yhteydessä, vaikka sinulla olisi jo osoitteita varastossa (oletus: `0`).
- `fixedseeds`: (kovakoodattu Address-luettelo), jos _DNS-siemenet_ epäonnistuvat tai ovat pois käytöstä (oletus: `1`).
- `dns`: Valtuuttaa DNS-resoluutiot yleisesti (esim. `-addnode`/`-seednode`/`-connect`).



Oletusarvoisesti solmusi kommunikoi clearnetin, Torin ja I2P:n kautta. Tämä tarkoittaa, että vertaisverkot, joihin se on yhteydessä clearnetissä, näkevät julkisen IP-osoitteesi Address, ja Internet-palveluntarjoajasi pystyy todennäköisesti havaitsemaan, että käytät Bitcoin-solmua (vaikkakin P2P Transport V2 vaikeuttaa Internet-palveluntarjoajan salakuuntelua). Tämä ei välttämättä ole ongelma, mutta jos haluat välttää näiden tietojen vuotamisen, voit liittää solmusi yksinomaan Tor-verkon kautta.



Jotta Tor olisi täysin käytössä, sinun on pakotettava Bitcoin core käyttämään vain tätä verkkoa ja luotava piilotettu palvelu saapuvia yhteyksiä varten (jos haluat ottaa ne käyttöön). Bitcoin.conf-tiedostoon on lisättävä tämä asetus:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Kaikki P2P-yhteydet kulkevat Torin kautta. Solmusi vastaanottaa saapuvia yhteyksiä varten `.onion` Address:n, joten reitittimessä ei tarvitse avata portteja. Internet-palveluntarjoajasi näkee vain Tor-liikennettä, eivätkä vertaisesi tiedä todellista julkista IP-osoitettasi Address.



Jos haluat välttää DNS-resoluution tyhjentämisen, voit lisätä asetuksiin `dnsseed=0` ja `dns=0`. Sinun on sitten annettava manuaalisesti `.onion`-vertaisverkkosolmuja `seednode=` tai `addnode=` kautta, koska uusien solmujen löytäminen on muuten vaikeaa.



Jos olet aloittelija, suosittelen tietysti jättämään kaikki nämä verkkoasetukset toistaiseksi rauhaan. Oletusasetukset ovat usein riittäviä.



### Mempool ja relepolitiikka



#### Perusparametrit



Tässä ovat perusparametrit, joita voit muuttaa Bitcoin.conf-tiedostossasi Mempool:n hallintaa ja vahvistamattomien tapahtumien välittämistä varten:





- `maxmempool=<n>`: Rajoittaa paikallisen Mempool:n maksimikoon `<n>` megatavuun (oletus: `300`). Kun raja saavutetaan, solmusi nostaa dynaamisesti tehokasta maksukynnystä ja priorisoi vähiten kannattavat tapahtumat (maksuprosentin, ei absoluuttisen arvon perusteella) pysyäkseen rajan alapuolella. Voit jättää tämän asetuksen oletusasetukseksi. Sen nostaminen voi olla hyödyllistä, jos olet Mining yksin tai jos haluat saada tarkemman kuvan Mempool ruuhkautumisesta ja parantaa maksuarviota. Sitä vastoin sen pienentäminen säästää RAM-muistia ja vähäisemmässä määrin muita järjestelmäresursseja.





- `mempoolexpiry=<n>`: Vahvistamattomien tapahtumien enimmäissäilytysaika Mempool:ssä (tunteina, oletusarvo: `336`). Tämän ajan jälkeen tapahtumat poistetaan, vaikka tilaa olisi edelleen käytettävissä.





- `persistmempool=1`: Tallentaa tilannekuvan Mempool:sta pysähdystilanteessa ja lataa sen uudelleen uudelleenkäynnistyksen yhteydessä (oletus: `1`). Tämä nopeuttaa uudelleenkäynnistyksen jälkeistä palautumista, jolloin tilaa ei tarvitse opetella uudelleen verkon kautta.





- `maxorphantx=<n>`: Säilytettävien orpojen transaktioiden enimmäismäärä (UTXO:iden riippuvaiset syötteet, joita ei ole vielä nähty UTXO-sarjassa, oletusarvo: `100`). Tämän raja-arvon ylittyessä vanhimmat tapahtumat poistetaan välimuistin hallitsemattoman kasvun välttämiseksi.





- blocksonly=1`: Estää vertaisilta vastaanotettujen vahvistamattomien transaktioiden hyväksymisen ja uudelleenlähettämisen (ellei erityisoikeuksia ole myönnetty). Solmu lataa ja mainostaa nyt vain lohkoja. Paikallisesti luodut transaktiot voidaan edelleen lähettää (käyttääksesi solmua Wallet-ohjelmiston kanssa). Tämä vähentää huomattavasti kaistanleveys- ja RAM-vaatimuksia, vaikkakin sillä hinnalla, että välittäjän hyöty vähenee ja Mempool:n käyttö on täysin tuntematonta.





- `minrelaytxfee=<n>`: Maksun vähimmäismäärä (BTC/kvB), jota pienempiä transaktioita ei hyväksytä solmun Mempool:ssa eikä välitetä vertaisille (oletusarvo: `0.00001` = 1 sat/vB). Mitä korkeampi tämä arvo on, sitä aggressiivisemmin solmusi suodattaa edulliset transaktiot.





- `mempoolfullrbf=1`: RBF-tapahtumien hyväksyminen, vaikka korvatussa tapahtumassa ei olisi nimenomaista RBF-merkintää. Tällä "*full-RBF*"-käytännöllä korkeampaa maksua tarjoava transaktio voi korvata toisen Mempool-transaktion, jos muut korvausehdot täyttyvät.



Muistutettakoon, että RBF on transaktiomekanismi, jonka avulla lähettäjä voi korvata transaktion korkeampien maksujen sisältävällä transaktiolla vahvistuksen nopeuttamiseksi. Jos liian alhaisen maksun sisältävä transaktio jää estetyksi, lähettäjä voi käyttää *Replace-by-fee*:a korottaakseen maksua ja priorisoidakseen korvaavan transaktionsa mempoolissa ja louhijoilla.



#### Lisä- ja erityisasetukset



Tässä ovat Mempool:n ja välityskäytännön lisäasetukset. Jos olet aloittelija, sinun ei tarvitse muuttaa näitä asetuksia:





- datacarrier=1`: Sallii muiden kuin rahoitustietoja sisältävien tapahtumien välittämisen ja (jos Mining solmun kautta) sisällyttämisen OP_RETURN-lähtöön (oletus: `1`). Tämän parametrin poistaminen käytöstä pienentää hieman muiden kuin rahoitustietojen roskapostin pinta-alaa, mutta vähentää yhteensopivuutta tiettyjen käyttötarkoitusten kanssa. Kaikissa tapauksissa sinun on hyväksyttävä louhittu `OP_RETURN`.





- `datacarriersize=<n>`: Solmun välittämän `OP_RETURN`:n enimmäiskoko (tavuina) (oletus: `83`). Tämän arvon pienentäminen rajoittaa `OP_RETURN`:n kautta siirrettäviä hyötykuormia. Huomaa, että tämä rajoitus poistetaan oletusarvoisesti Bitcoin core:n tulevassa versiossa.





- `bytespersigop=<n>`: Parametri, joka muuntaa allekirjoitustapahtumat vastaaviksi tavuiksi relerajojen arviointia varten (oletusarvo: `20`). Tämä vaikuttaa `sigops`-rikkaiden transaktioiden hyväksymiseen paikallisten politiikkasääntöjen mukaisesti.





- `permitbaremultisig=1`: Sallii *bare-Multisig* P2MS-tapahtumien välittämisen (oletus: `1`). Tämä on vanhin skriptimalli UTXO:n monisignatuuriehtojen luomiseen (Gavin Andresen keksi sen vuonna 2011).





- `whitelistrelay=1`: (oletus: `1`). 





- `whitelistforcerelay=1`:  Tämän jälkeen solmu välittää niiden tapahtumat, vaikka ne olisivat jo Mempool:ssa, jolloin se ohittaa redundanssinestomekanismit.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Sitoo Interface- tai Address-alueen ja määrittää hienojakoiset käyttöoikeudet vastaaville vertaisverkoille: `Relay`, `forcerelay`, `Mempool` (Mempool-sisältöpyyntö), `noban`, `download`, `addr`, `bloomfilter`. Tämä voi olla hyödyllistä, kun luotetuille vertaisverkoille (kuten yhdyskäytäville, lähiverkoille ja sisäisille palveluille) myönnetään etuoikeutettu kohtelu.





- peerbloomfilters=1`: Suodatettujen lohkojen/transaktioiden tarjoamiseksi ohuille asiakkaille (oletus: `0`). Varoitus: tämä lisää resurssien kuormitusta.





- peerblockfilters=1`: Tarjoaa BIP157 (*Neutrino*) kompaktisuodattimet vertaisverkoille (oletus: `0`).





- `blockreconstructionextratxn=<n>`: Muistissa säilytettävien transaktioiden lisämäärä kompaktien lohkojen uudelleenrakentamista varten (oletus: `100`). Parantaa jälleenrakentamisen onnistumista kompaktien synkronointien aikana, mutta se vie hieman muistia.



Muistutuksena mainittakoon, että kaikki nämä välityssäännöt eivät vaikuta kelvolliseen lohkoon sisältyvien transaktioiden pätevyyteen. Niiden tarkoituksena on mukauttaa panostasi releeseen, suojella resurssejasi ja tehdä solmusta ennustettava rajoitetuissa ympäristöissä, mutta ne eivät koskaan anna sinulle mahdollisuutta kieltäytyä lohkoista, jotka noudattavat konsensussääntöjä.



### Lompakot



Voit myös säätää tapaa, jolla lompakoitasi hallitaan Bitcoin.conf-tiedostossa. Jos et käytä Wallet:aa suoraan Core-ohjelmassa, vaan ulkoista hallintaohjelmistoa, kuten Sparrow:ää tai Liana:ää, näillä parametreilla ei ole suurta merkitystä:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Määrittää Wallet:n tuottamien osoitteiden muodon vastaanottoa varten.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Pakottaa Exchange Address-muodon (tulon loppuosa yhdellä maksulla).





- `Wallet=<polku>`: Lataa olemassa olevan Wallet:n käynnistyksen yhteydessä (voidaan toistaa useamman lompakon lataamiseksi).





- `walletdir=<dir>`: Hakemisto, joka sisältää lompakot (oletus: `<datadir>/wallets`, jos se on olemassa, muuten `<datadir>`). Tämä voi olla hyödyllistä, jos haluat tallentaa lompakot omaan tai salattuun tietovälineeseen.





- `walletbroadcast=1`: (oletus: `1`). Aseta arvoksi `0`, jos haluat hallita lähetyksiä toisen kanavan kautta.





- `walletrbf=1`: RBF-opt-in, joka antaa RBF-signaalin kaikissa tapahtumissa (oletus: `1`). Mahdollistaa maksujen korottamisen myöhemmin, jos transaktio estyy.





- `txconfirmtarget=<n>`: Transaktion vahvistuskohde (lohkojen lukumääränä, oletus: `6`). Wallet asettaa automaattisesti maksun tapahtumalle, joka on vahvistettava tämän lukumäärän sisällä.





- `paytxfee=<amt>`: Wallet-tapahtumiin sovellettava kiinteä maksu (BTC/kvB). Vältä yleisesti: käytä mukautuvaa estimointia `txconfirmtarget`:n avulla.





- fallbackfee=<amt>`: Fallback rate (BTC/kvB), jota käytetään, jos estimaattorilta loppuu data (oletus: `0.00`). Asettamalla sen arvoksi 0 se poistaa fallbackin kokonaan käytöstä.





- `mintxfee=<amt>`: Vähimmäiskynnys (BTC/kvB), jolla Wallet luo transaktioita (oletusarvo: `0.00001`). Wallet kieltäytyy luomasta transaktiota, jos tämä kynnysarvo alittuu.





- `maxtxfee=<amt>`: Wallet-tapahtuman kokonaismaksujen absoluuttinen yläraja (oletusarvo: `0.10` BTC). Suojaa epätavallisen korkeilta maksuilta, jotka tuhoaisivat tarpeettomasti bitcoineja.





- `avoidpartialspends=1`: Valitsee UTXO:t Address-klustereiden mukaan osittaisten menojen välttämiseksi.





- `spendzeroconfchange=1`: UTXO Exchange voidaan käyttää uudelleen uuden tapahtuman merkintänä (oletus: `1`).





- `consolidatefeerate=<amt>`: Enimmäisnopeus (BTC/kvB), jonka ylittyessä Wallet välttää lisäämästä enemmän syötteitä kuin on tarpeen konsolidointiin. Tämä mahdollistaa opportunistisen konsolidoinnin alhaisilla hinnoilla ja vähentää kustannuksia, kun kustannukset ovat korkeat.





- `maxapsfee=<n>`: Lisämaksujen budjetti (BTC, absoluuttinen arvo), jonka Wallet suostuu maksamaan aktivoidakseen vaihtoehdon "*välttää osittaiset kulutukset*".





- `discardfee=<amt>`: (BTC/kvB), joka osoittaa, että olet valmis heittämään Exchange:n pois lisäämällä sen maksuun. Tuotokset, jotka maksaisivat yli kolmanneksen arvostaan tällä hinnalla, hylätään.





- `keypool=<n>`: Ennalta luodun Address poolin koko (oletus: `1000`). Liian pienet arvot lisäävät epätäydellisten palautusten riskiä.





- `disablewallet=1`: Käynnistää Bitcoin core:n ilman Wallet-alijärjestelmää ja poistaa siihen liittyvät RPC:t käytöstä. Vähentää hyökkäyspintaa ja jalanjälkeä, jos solmua käytetään vain validointiin/julkaisuun.



### Tallennus, indeksointi ja suorituskyky



Määritystiedoston avulla voit myös säätää koneeseesi liittyviä parametreja. Tämä voi olla erityisen tärkeää, jos sinulla on rajalliset resurssit tai päinvastoin suuri määrä käytettävissä olevaa kapasiteettia:





- `datadir=<dir>`: Asettaa Bitcoin core:n päätietohakemiston.





- `blocksdir=<dir>`: Irrottaa lohkotiedostojen (`blocks/blk*.dat` ja `blocks/rev*.dat`) sijainnin `datadir`:sta. Tämä voi olla hyödyllistä, kun lohkoarkisto sijoitetaan eri tietovälineelle, mutta tilapohja (`chainstate/`) pidetään esimerkiksi nopeammalla tietovälineellä.





- `dbcache=<n>`: Varaa `<n>` MiB tietokannan välimuistiin (*LevelDB*), jota lohkoindeksi ja `chainstate` käyttävät (oletus: `450`). Mitä suurempi arvo, sitä nopeampi IBD ja nykyinen validointi, mutta sen kustannuksella, että RAM-muistia kuluu enemmän.





- `prune=<n>`: Ottaa käyttöön lohkotiedostojen karsinnan ja asettaa levytilatavoitteen MiB:nä (oletusarvo: `0` = ei käytössä; `1` = manuaalinen karsinta RPC:n kautta; `>=550` = automaattinen karsinta alle tavoitteen). Yhteensopimaton `txindex=1`:n kanssa. Solmu pysyy täysin validoivana solmuna, mutta ei voi enää tarjota vanhaa historiaa. Tämä vaihtoehto on erityisen hyödyllinen, jos levytilaa on rajoitetusti, esimerkiksi kun asennat solmun kotikoneellesi.





- txindex=1`: Rakentaa ja ylläpitää vahvistettujen tapahtumien globaalia indeksiä. Välttämätön tietyissä kyselyissä (`getrawtransaction`, ei-Wallet) ja etsintätarkoituksissa, mutta kasvattaa merkittävästi levytilaa. Ei yhteensopiva pruned-tilan kanssa.





- `assumevalid=<hex>`: Voit ohittaa sen esivanhempien skriptitarkistukset (aseta `0`, jos haluat tarkistaa kaiken). Katso lisätietoja edellisestä luvusta.





- `reindex=1`: Rekonstruoi lohkoindeksit ja tilan (`chainstate`) levyllä olevista `blk*.dat`-tiedostoista. Rakentaa uudelleen myös valinnaiset aktiiviset indeksit. Tämä on aikaa vievä toimenpide, jota käytetään korruptoituneen tietokannan korjaamiseen tai raskaiden indeksien siistiin aktivointiin/deaktivointiin.





- `reindex-chainstate=1`: Chainstate` nykyisestä lohkoindeksistä. Suositeltava, kun lohkotiedostot ovat terveitä.





- `blockfilterindex=<tyyppi>`: Ylläpitää ohuiden asiakkaiden (BIP157/158) ja joidenkin RPC:iden käyttämien kompaktien lohkosuodattimien (esim. `basic`) indeksejä. Oletusarvoisesti pois käytöstä (`0`). Kuluttaa lisää levytilaa ja indeksointiaikaa.





- `coinstatsindex=1`: Ylläpitää UTXO-sarjan tilastoindeksiä, jota käytetään `gettxoutsetinfo`-kutsulla. Hyödyllinen auditointeja ja mittareita varten, koska se poistaa kalliin uudelleenlaskennan tarpeen. Oletusarvoisesti poissa käytöstä.





- `loadblock=<tiedosto>`: Blk*.dat`-tiedostosta. Käytetään esilataamaan historiaa offline-lähteestä (paikallinen kopio, ulkoinen media) alustuksen nopeuttamiseksi.





- `par=<n>`: Asettaa komentosarjan tarkistussäikeiden määrän (välillä `-10` ja `15`, `0` = auto, `<0` = jättää tämän määrän ytimiä vapaaksi). Mahdollistaa suorittimen rinnakkaisuuden säätämisen vahvistuksen aikana. Automaattinen tila on sopiva useimmissa tapauksissa.





- `debuglogfile=<file>`: Log-tiedosto: Määrittää `debug.log`-lokin sijainnin.





- `shrinkdebugfile=1`: Käynnistyksen yhteydessä (oletus: `1`, kun `-debug` ei ole aktiivinen).





- `settings=<tiedosto>`: `settings.json`: Polku dynaamiseen asetustiedostoon `settings.json`.



### RPC pääsy ja toimintavarmuus



Bitcoin.conf-tiedoston avulla voit myös määrittää solmun käyttöparametrit. Ole varovainen näiden asetusten kanssa, varsinkin jos olet vasta aloittamassa: vältä niiden muuttamista ilman perusteellista ymmärrystä niiden vaikutuksista, sillä se voi aiheuttaa haavoittuvuuksia.





- `server=1`: Aktivoi JSON-RPC-palvelimen. Välttämätön, jos käytät `bitcoind`:tä `bitcoin-cli`:n tai kolmannen osapuolen sovelluksen kautta. Poista käytöstä (`0`) puhtaasti validoivassa solmussa, joka ei tarjoa mitään API:ta tai käyttää jo Electrum-palvelinta.





- `rpcbind=<addr>[:port]`: RPC palvelin kuuntelee Address/port. Oletuksena kuuntelu tapahtuu vain paikallisesti (`127.0.0.0.1` ja `::1`). Tätä parametria ei oteta huomioon, jos `rpcallowip` ei ole myös määritelty. Käytä sitä rajoittaaksesi Interface:n käyttöä nimenomaisesti.





- `rpcport=<port>`: RPC portti (oletus: `8332` Mainnet:ssa, `18332` Testnet:ssä, `38332` kirjanmerkissä, `18443` regtestissä).





- `rpcallowip=<ip|cidr>`: Sallii RPC-asiakkaat tietystä IP-osoitteesta tai aliverkosta (voidaan toistaa). Käytä yhdessä `rpcbind`:n kanssa, jos haluat avata API:n vain luotetulle segmentille (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Suositeltu RPC todennusmenetelmä (hashed password). Mahdollistaa useita merkintöjä ja välttää salaisuuden tallentamisen selvänä tekstinä.





- `rpccookiefile=<polku>`: (oletus: `.cookie`-tiedosto osoitteessa `datadir/`). Tätä käytetään saman käyttäjän paikalliseen käyttöön ilman pysyvien salasanojen hallintaa. Voit esimerkiksi käyttää sitä Liana Wallet:n liittämiseen Bitcoin core:een samalla koneella.





- `rpccuser=<user>` / `rpcpassword=<pw>`: Klassinen RPC-todennus tavallisella salasanalla. Vältä tämän käyttöä `rpcauth`:n tai evästeen hyväksi.





- `rpcthreads=<n>`: RPC-kutsuja palvelevien säikeiden määrä (oletus: `4`). Lisää sitä, jos sinulla on suuria kutsupiikkejä seurannan/ulkoisen työkalun puolella.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Hyväksyttyjen API:iden valittujen tiedostojen luettelo. Vähentää hyökkäyspintaa rajoittamalla käytettävissä olevia menetelmiä.





- `rpcwhitelistdefault=1|0`: Jos valkoluettelo on käytössä ja valkoluetteloa käytetään, luetteloimattomat puhelut hylätään. Tämä voi myös pakottaa oletusarvoisen tyhjän joukon (puheluita ei sallita), kunhan mitään ei ole nimenomaisesti listattu.





- `rest=1`: Ota julkinen REST API käyttöön (oletusarvoisesti pois käytöstä). Paljastetaan vain luotettavassa verkossa (sama varovaisuus kuin JSON-RPC:n kanssa).





- `conf=<tiedosto>`: Määrittää, vain komentorivillä, vain lukukäyttöön tarkoitetun konfiguraatiotiedoston. Hyödyllinen suoritusprofiilin jäädyttämiseen (muuttumaton) ops-puolella.





- `includeconf=<tiedosto>`: Lataa ylimääräisen konfiguraatiotiedoston (polku suhteessa `datadir/`). Mahdollistaa roolien erottamisen: yhteinen perusta + herkkä paikallinen ylikuormitus.





- `daemon=1` / `daemonwait=1`: Käynnistää `bitcoind` taustalla ja odottaa `daemonwait`:n kanssa, että alustaminen on päättynyt, ennen kuin luovuttaa. Tämä helpottaa integroitumista valvojien (systemd, runit) kanssa.





- `pid=<tiedosto>`: PID-tiedoston sijainti.





- `sandbox=<log-and-abort|abort>`: Ottaa käyttöön kokeellisen syscalls sandboxing: vain odotetut syscalls sallitaan.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Suorittaa komennon käynnistyksen tai sammutuksen yhteydessä.





- `alertnotify=<cmd>`: Käynnistää komennon hälytyksen saatuaan.





- `blocknotify=<cmd>`: Suorittaa komennon jokaiselle uudelle lohkolle.





- `debug=<kategoria>|1` / `debugexclude=<kategoria>`: Ottaa käyttöön tai poistaa käytöstä yksityiskohtaiset lokiluokat (esim. `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: IP-osoitteet.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Lisää lokien lähdepaikat, säikeiden nimet ja tarkat aikaleimat.





- `printtoconsole=1`: Lähettää jäljet/virheet konsoliin (*stdout*).





- `help-debug=1`: Näyttää debug-vaihtoehdon ohjeen ja lopettaa.





- `uacomment=<cmt>`: P2P.



Olemme nyt saaneet lueteltua suurimman osan konfigurointiparametreista. Tämä Bitcoin.conf-tiedosto on siis solmusi todellinen kojelauta: siinä määritellään verkon konfigurointi, Mempool:n hallinta, levyn ja muistin käyttö, indeksointi ja yleinen hallinta. Jos haluat oppia lisää tästä tiedostosta ja luoda sen tarpeisiisi sopivaksi, suosittelen käyttämään [Jameson Loppin generaattoria](https://jlopp.github.io/Bitcoin-core-config-generator/).



Olemme päässeet päätökseen tällä BTC 202 -kurssilla, jonka avulla olet ymmärtänyt solmujen toiminnan ja vuorovaikutuksen perusteet ja pystynyt myös perustamaan oman solmusi. Olet nyt suvereeni bitcoinilainen, jolla on oma itsesäilytettävä Wallet ja joka lähettää transaktiosi oman solmusi kautta. Onnittelut!



Voit nyt siirtyä kurssin viimeiseen osaan, jossa voit arvioida BTC 202:n ja tehdä tutkintotodistuksen, jolla voit tarkistaa, että olet oppinut kaikki käsitellyt käsitteet.



Sinulla on nyt useita vaihtoehtoja. Seuraava looginen askel on perustaa oma Lightning-solmusi, jolloin voit olla täysin riippumaton off-chain-tapahtumissasi. Tämä on aiheena tulevassa kurssissa, joka julkaistaan syksyllä 2025 Plan ₿ Network:sta.



Sillä välin kutsun sinut tutustumaan BTC 204 -koulutukseen, jonka avulla voit ymmärtää ja hallita yksityisyyden suojan periaatteet Bitcoin:n käytössäsi:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Viimeinen osa


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Arvostelut & arvostelut


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Loppukoe


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Päätelmä


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>