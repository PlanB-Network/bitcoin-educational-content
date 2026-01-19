---
name: Ensimmäisen Lightning-solmun perustaminen
goal: Lightning-solmun ymmärtäminen, asentaminen, konfigurointi ja käyttö
objectives: 


  - Ymmärrä Lightning-solmun rooli ja tarkoitus.
  - Tunnista käytettävissä olevat erilaiset ohjelmistoratkaisut.
  - Asenna ja määritä Lightning-solmu (LND).
  - Yhdistä kulujen tili.
  - Tunne salamasolmun käytön riskit.


---

# Ensimmäinen askel kohti itsenäisyyttä Lightningin avulla



Olet jo hankkinut ensimmäisen sats:n, varmistanut itsesäilytysvarasi ja ottanut käyttöön Bitcoin-solmun, joka on suvereeni on-chain-käytössäsi. Seuraava askel on saavuttaa sama autonomia Lightningissa: juuri se on tämän kurssin tatete.



LNP202 on suunnattu keskitason käyttäjille, ja se opastaa sinua askel askeleelta ensimmäisen Lightning-solmun käyttöönotossa ilman teknisiä taitoja.



Opit asentamaan LND:n Umbrel:een, avaamaan ja hallitsemaan kanavia, valvomaan solmua ja yhdistämään mobiilin wallet:n, jotta tet nauttia kokemuksesta, joka on verrattavissa huoltajana toimivan wallet:n kokemukseen, mutta samalla tet hallita varojasi täysin.



+++


# Johdanto


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Kurssin yleiskatsaus


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 on käytännönläheinen kurssi, jonka tarkoituksena on tehdä sinusta Lightningin itsenäinen käyttäjä käyttämällä omaa solmua. Tatete on yksinkertainen: aloita jo käytössä olevasta Bitcoin-solmusta, ota LND käyttöön Umbrel:ssä, suojaa se kunnolla, avaa ja hallitse ensimmäiset kanavasi ja käytä solmua päivittäin liikkuvasta wallet:stä käsin. Tällä kurssilla oletetaan, että olet jo käynyt BTC 202 -kurssin, koska oletan, että Umbrel:ssä oleva Bitcoin-solmusi on käytössä ja synkronoitu. Emme käy tässä läpi Bitcoin-solmun perustamista.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Jos haluat ymmärtää paremmin Lightningin sisäistä mekaniikkaa, LNP 201 -kurssi on myös erittäin suositeltava, vaikka se ei olekaan tämän kurssin ennakkoedellytys:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Tämän LNP202-kurssin ensimmäisessä osassa tarkastelemme, mikä Lightning-solmu oikeastaan on, miten se eroaa yksinkertaisesta wallet:stä ja miksi henkilökohtaisen solmun käyttäminen on ainoa tapa käyttää Lightningia delegoimatta sats:ttä luotettavalle kolmannelle osapuolelle. Tämän jakson lopuksi tehdään strateginen valinta: mikä ratkaisu sopii sinulle, yksinkertaisimmista lähestymistatesta klassiseen Lightning-solmuun, jonka toteutamme tällä kurssilla.



Kurssin toisessa osassa asennat LND:n Umbrel:aan ja otat sitten käyttöön elementit, jotka estävät kalleimmat virheet: realistinen varmuuskopiointistrategia ja suojautuminen huijaukselta vahtitornin avulla. Kun nämä perusasiat ovat kunnossa, avaat ensimmäisen kanavasi, jotta tet aloittaa maksamisen Lightningille omalla infrastruktuurillasi.



Näet siis: tällä LNP202-kurssilla perustamme Lightning-solmun plug-and-play-tilassa Umbrel:n kautta, emmekä käytä klassista komentorivin lähestymistapaa, jotta se soveltuisi myös keskitason käyttäjille. Jos haluat mieluummin komentoriviasennuksen, suosittelen seuraamaan alla olevaa ohjetta. Valmisteilla on myös muita, edistyneempiä, komentoriville suunnattuja Lightning-kursseja.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Osa 3 vie sinut sitten toimivasta solmusta solmuun, jota osaat hallita. Aloitat määrittelemällä Lightning-solmun operaattoriprofiilin (kuluttaja, kauppias tai reititin) ja tutustut sitten täydelliseen hallintaohjelmistopakettiin, jotta tet seurata kanavia ja toimia siististi topologiassasi. Lopuksi käsittelet erittäin tärkeää Lightning-kohtaa: miten hankit maksullisen tai yhteistyöhön perustuvan maksuvalmiuden, olipa kyse sitten maksullisista tai yhteistyöhön perustuvista ratkaisuista.



Osassa 4 keskitytään jokapäiväiseen käyttöön. Luodaan yhteys solmupisteesi ja mobiiliasiakkaan välille, jotta tet maksaa ja noutaa maksun yksinkertaisesti älypuhelimellasi luopumatta omahuolenpidosta. Tarkastelemme ensin verkkomenetelmää *Tailscale*:n kautta ja sitten protokollan lähestymistapaa *Nostr Wallet Connect*:n kautta sekä niiden etuja ja haittoja. Kurssi päättyy loppulukuun, joka antaa sinulle oikeat tavat ylläpitää itsehallintaa sekä toiminnallisesti että pedagogisesti.



Jos seuraat tätä LNP202-kurssia oikeassa järjestyksessä, sen lopussa sinulla on Lightning-solmun täydellinen konfigurointi, joka toimii jokapäiväisessä käytössä ja on ennen kaikkea hallinnassa.




## Lightning-solmujen ymmärtäminen


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Ennen kuin käynnistät oman solmun, tässä luvussa käydään lyhyesti läpi Lightning Network:n perustana oleva teoria. On todellakin tärkeää ymmärtää asiaan liittyvät mekanismit, sillä sen avulla tet tunnistaa riskit ja ottaa käyttöön hyviä käytäntöjä niiden rajoittamiseksi. En kuitenkaan mene tässä yksityiskohtiin, koska se ei ole tämän kurssin päätatete. Jos haluat syventyä aiheeseen syvällisemmin, suosittelen lämpimästi tutustumaan Fanis Michalakisin LNP 201 -kurssiin, joka on alan referenssi:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Mikä on Lightning-solmu?



Palataanpa perusasioihin: ennen kuin määritellään, mikä solmu on, on ymmärrettävä, mikä Lightning Network on. Se on ylimmän tason protokolla, joka on rakennettu Bitcoin:n päälle ja joka on suunniteltu mahdollistamaan ketjun ulkopuoliset BTC-tapahtumat, jotka ovat nopeita (lähes välittömästi lopullisia) ja yleensä edullisia. "Offchain" tarkoittaa, että Lightningilla toteutettujen transaktioiden ei ole tarkoitus näkyä Bitcoin-lohkoketjussa. Lightning on myös osittainen vastaus Bitcoin:n lisääntyvään käyttöön ja ketjun sisäiseen ruuhkautumiseen, joka herättää huolta järjestelmän skaalautuvuudesta.



Lightningin toiminta perustuu osallistujien välisten maksukanavien avaamiseen, joissa transaktiot tedaan suorittaa lähes välittömästi ja usein minimaalisilla maksuilla ilman, että niitä tarvitsee rekisteröidä yksi kerrallaan Bitcoin-lohkoketjuun. Nämä kanavat tevat pysyä auki hyvin pitkään, ja ne vaativat ketjussa tapahtuvia transaktioita vain silloin, kun niitä avataan ja suljetaan.



Lightning-solmu on Lightning-verkon osallistuja, joka avaa kanavia ja suorittaa maksuja muiden solmujen kanssa. Konkreettisesti Lightning-solmu on tietokoneella toimiva ohjelmisto, joka toteuttaa Lightning Network-protokollaa. Esimerkkejä ovat LND, Core Lightning tai Eclair. Tämän ohjelmiston päätehtävänä on:




- muodostaa yhteyden Bitcoin-solmuun saadakseen tietoja päälohkoketjusta;
- luoda ja hallita kaksisuuntaisia maksukanavia muiden solmujen kanssa;
- vaihtaa viestejä koko Lightning-verkon kanssa.



![Image](assets/fr/001.webp)



### Solmu vs. Lightning Wallet: tärkeä ero



Bitcoin:ssa (onchain) "*wallet*" viittaa ohjelmistoon, joka hallinnoi yksityisiä avaimiasi, laskee saldosi UTXO:n avulla ja muodostaa transaktiosi. Tämä wallet te perustua omaan Bitcoin-solmuun tai jonkun muun solmuun, mutta nykyään solmun ja ketjussa toimivan wallet:n rooli on selvästi erilainen.



Lightningissa on vaikeampaa käyttää tällaista sanastoa uudelleen aiheuttamatta sekaannusta. Termi "*Lightning wallet*" on melko epämääräinen, koska todellisuudessa ei ole olemassa todella itsestään toimivaa Lightning wallet:ää, ellei se perustu solmuun. Näin ollen vain kaksi tilannetta on mahdollista:



- Jos sinulla on todellinen Lightning-solmu (eli ei-hallinnollinen): käyttämäsi ohjelmisto (esim. mobiilisovellus kuten Phoenix tai LND-instanssi Umbrel:ssa) todella pyörittää solmua, ja sinulla on avaimet, joilla tet noutaa bitcoinisi. Tässä tapauksessa "*Lightning wallet*" on oikeastaan vain käyttöliittymä Lightning-solmun päällä, olipa se sitten sulautettu tai etäyhteys.



- Säilytyspalvelun käyttö: käytät sovellusta, joka näyttää saldon sats:ssa Lightningissa, mutta taustalla varat ovat palveluntarjoajan solmussa (esim. Wallet of Satoshi). Sinulla ei ole avaimia eikä kanavien hallintaa. Saldosi on vain kirjanpitomerkintä yrityksen tietokannassa. Se on verrattavissa siihen, että jättäisit bitcoinisi pörssialustalle kaikkine siihen liittyvine riskeineen. Tässä tapauksessa "*Lightning wallet*" on vain pääsy tilille, jota hallinnoi operaattori, joka puolestaan pyörittää todellista Lightning-solmua.



Lightningissa ei siis ole välivaihetta: joko sinulla on solmu (jopa sulautettu solmu), joten olet itse hallinnassa, tai sitten sinulla ei ole, joten yritys omistaa sats:n. Mutta kuten seuraavissa luvuissa nähdään, näitä kahta käyttötarkoitusta te joskus olla vaikea erottaa toisistaan. Esimerkiksi Phoenix on mobiilisovellus, johon on upotettu todellinen Lightning-solmu, mutta käyttäjä ei välttämättä ole siitä tietoinen, koska sen toiminnan koko monimutkaisuus on lähes täysin piilossa.



### Muistutus Lightning Network:n toiminnasta



Tässä osiossa annan sinulle lyhyen muistutuksen siitä, miten Lightning toimii. Vielä kerran, jos haluat syvällisemmän esityksen teoreettisista käsitteistä, pyydän sinua tutustumaan LNP 201 -kurssille.



#### Maksukanavat: avaa, päivitä ja sulje



Lightning-verkon ydin perustuu kaksisuuntaisiin maksukanaviin. Kanava tedaan avata (eli luoda), päivittää Lightning-transaktioiden tapahtuessa ja lopuksi sulkea. Onchain-näkökulmasta katsottuna kanava ei ole muuta kuin 2/2-monimerkkinen lähtö.



![Image](assets/fr/002.webp)



Lightningin näkökulmasta kyseessä on maksukanava, jossa likviditeetti on jaettu kahden osallistujan kesken.



![Image](assets/fr/003.webp)





- Kanavan avaaminen:**



Kaksi solmua päättää avata kanavan. Toinen niistä sitoo bitcoineja ketjussa tapahtuvassa transaktiossa nimeltä *rahoitustransaktio*. Tämä transaktio luo tulosteen, joka perustuu 2-of-2 multisignature-skriptiin, mikä tarkoittaa, että näiden varojen käyttäminen Bitcoin:ssä edellyttää kanavan molempien solmujen allekirjoitusta. Ennen tämän transaktion toteuttamista varoja tarjoava osapuoli pyytää toista osapuolta allekirjoittamaan *nostotransaktion*, jota ei toteuteta ketjussa, mutta jonka avulla se te saada varansa takaisin ongelmatilanteessa.



![Image](assets/fr/004.webp)





- Commitment-tapahtumat:**



Kanavan tilaa (eli sats:n jakautumista A:n ja B:n välillä) edustaa *commitment transaction*, joka on molempien solmujen tiedossa mutta jota ei lähetetä välittömästi lohkoketjuun. Tämä transaktio kuvaa, miten kanavan varat jaetaan uudelleen ketjussa Lightningissa tehtyjen maksujen mukaisesti.



Jokaisen Lightning-maksun yhteydessä molemmat solmut allekirjoittavat uuden tilan, joka korvaa edellisen. Vanha tila peruutetaan peruutusavainmekanismin ansiosta: jos toinen osallistujista yrittää lähettää vanhan tilan, toinen te saada takaisin koko rahamäärän rangaistuksena.



Tärkeä ajatus tässä on, että solmut säilyttävät aina allekirjoitetun Bitcoin-tapahtuman, jota ei lähetetä ketjussa ja joka mahdollistaa toistensa sats:n uudelleen jakamisen Lightning Network:ssä suoritettujen maksujen mukaisesti.



![Image](assets/fr/005.webp)





- Kanavan sulkeminen:**



Kanava tedaan sulkea puhtaasti yhteistoiminnallisella sulkemisella, kun molemmat osapuolet sopivat kanavan lopullisesta tilasta, tai yksipuolisesti (pakotettu sulkeminen), jos toinen osallistujista lakkaa tekemästä yhteistyötä tai tulee tatettamattomaksi. Kaikissa tapauksissa sulkeminen tapahtuu ketjussa tapahtuvana transaktiona, joka käyttää 2/2-tuloksen ja jakaa varat osallistujien kesken kanavan viimeisen temassa olevan tilan mukaisesti.



![Image](assets/fr/006.webp)



Lightning toimii näin ollen toissijaisena kerroksena, joka on ankkuroitu Bitcoin:aan: vain tietyt tapahtumat (kanavien avaaminen ja sulkeminen) näkyvät päälohkoketjussa. Välimaksut jäävät lohkoketjun ulkopuolelle.



Ennen kuin menemme pidemmälle, tässä on kaksi olennaista käsitettä Lightning-kanavan hallinnan ymmärtämiseksi:




- Liquidity*: kanavan toisella puolella käytettävissä oleva sats:n määrä;
- *Kapasiteetti*: se on 2/2-multisignaalin ulostuloon lukittu kokonaismäärä eli likviditeetin summa kanavan molemmilla puolilla.



#### Kanavien ja likviditeetin verkosto



Kanava ei ole vain kahden solmupisteen välistä maksua varten: se on osa toisiinsa kytkettyjen kanavien maailmanlaajuista verkkoa. Solmusi te ohjata maksuja muille käyttäjille omien kanaviensa kautta, ja tet lähettää sats:n Lightning-solmuun, jonka kanssa sinulla ei ole suoraa kanavaa, kunhan solmujenne välillä on kelvollinen reitti.



Kukin solmu tietää juoruprotokollan kautta kartan tästä verkosta: mitkä kanavat ovat olemassa, mitkä solmut ovat yhteydessä toisiinsa kaksisuuntaisella kanavalla ja mitkä kapasiteetit on julkaistu. Jos haluat lähettää maksun vastaanottajalle, jolla ei ole suoraa kanavaa, solmusi laskee reitin, joka koostuu useista hyppäyksistä: oma solmusi → solmu X → solmu Y → vastaanottajasolmu. Jokaisella hyppysuoralla maksu kulkee kanavan kautta, jolla on oltava riittävästi likviditeettiä maksun suuntaan.



![Image](assets/fr/007.webp)



Kanavan likviditeetti ei siis ole symmetrinen: toinen puoli te olla raskaasti kuormitettu, kun taas toinen puoli on lähes tyhjä. Tämän likviditeetin hallinta, eli se, että tiedetään, missä sats on ja mihin suuntaan se te virrata, on yksi tärkeimmistä Lightning-solmun toiminnan osa-alueista. Tarkastelemme sitä tarkemmin tulevissa käytännön luvuissa.



#### HTLC: maksujen kuljettaminen ilman ryöstöä



Jotta maksut tevat kulkea välisolmujen kautta ilman luottamusta, Lightning käyttää älykkäitä sopimuksia nimeltä *HTLC* (*Hashed Time-Locked Contracts*). Yksinkertaisesti sanottuna HTLC-sopimuksessa varojen siirto riippuu salaisuuden paljastumisesta, ja siihen sisältyy aikarajoitus, joka suojaa lähettäjää tapahtuman epäonnistumisen varalta. Jokaisen maksun edellytyksenä on siis ennakkokuvan esittäminen (salaisuus, jonka hash vastaa sovittua arvoa). Jos lopullinen vastaanottaja esittää tämän ennakkokuvan, hän te vaatia varat, jolloin kukin välittäjäsolmu te periä omat varansa takaisin.



![Image](assets/fr/008.webp)



Säästän sinut HTLC:n toiminnan teknisiltä yksityiskohdilta, sillä ne eivät ole oleellisia tämän kurssin kannalta. Löydät perusteellisen selityksen LNP 201 -teoriakurssilta. Muista vain, että HTLC:t mahdollistavat atomiset vaihdot: joko siirto onnistuu eikä reitityksessä vahingoiteta ketään tai se epäonnistuu ja jokainen osallistuja saa takaisin alkuperäiset varansa. Välitilannetta ei ole olemassa.



### Tärkeimmät Lightning-solmujen toteutukset



Kuten Bitcoin:n tapauksessa, myös Lightning-protokollasta on useita toteutuksia. Useat riippumattomat tiimit kehittävät omia versioitaan, jotka ovat kaikki yhteentoimivia, koska ne noudattavat samoja eritelmiä (BOLTit). Seuraavassa ovat tärkeimmät nykyisin käytössä olevat toteutukset.



#### LND (*Lightning Network Daemon*)



LND on Lightning Labsin kehittämä, Go-kielellä kirjoitettu Lightning-protokollan täydellinen toteutus.



![Image](assets/fr/009.webp)



#### Ydinsalama (*CLN*)



Core Lightning (aiemmin *C-Lightning*) on Blockstreamin kehittämä toteutus. Se on kirjoitettu C-kielellä, ja jotkin osat ovat Rust-kielellä.



![Image](assets/fr/010.webp)



#### Eclair



Eclair on Scala-kielellä kirjoitettu toteutus, jonka ranskalainen ACINQ-yritys on kehittänyt. ACINQ käyttää Eclairilla yhtä Lightning-verkon tärkeimmistä reitityssolmuista ja käyttää tätä toteutusta omien tuotteidensa, kuten Phoenix-sovelluksen, ohjelmistoperustana.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) on Rust-kehityspaketti, jota ylläpitää Spiral (Block, ex-Square). Se ei ole valmis daemon kuten LND tai CLN, vaan kirjasto kehittäjille, jotka haluavat integroida Lightningin suoraan sovelluksiinsa.



![Image](assets/fr/012.webp)



Tällä LNP202-kurssilla keskitymme pääasiassa LND:een: toteutukseen, jota käytetään yleisimmin yksityisasiakkaille suunnatuissa avaimet käteen -ratkaisuissa, kuten Umbrel:ssä.



Se tästä lyhyestä muistutuksesta siitä, miten Salama toimii. Vielä kerran, jos jokin käsite on jäänyt ymmärtämättä tai jos haluat syventyä hieman, ennen kuin otat sen käyttöön, Fanis Michalakisin kurssi on olennainen referenssi aiheesta:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Miksi ylläpitää omaa Lightning-solmua?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Kysymykseen vastaaminen on melko yksinkertaista, koska se on retorinen: ilman omaa solmua et enää oikeasti käytä Lightningia, vaan ainoastaan illuusio Lightningista yrityksen infrastruktuurissa.



Lightning custodial wallet:n käyttäminen tarkoittaa, että bitcoinit kuuluvat teknisesti solmua ylläpitävälle yritykselle. Sinulla ei ole hallussasi yksityisiä avaimia, etkä hallitse kanavia. wallet-saldosi on vain rivi palveluntarjoajan tietokannassa. Tämä tilanne on varmasti erittäin kätevä aloittelijoille, ja käyttökokemus on usein sujuva, mutta peruskysymys on: mitä hyötyä Bitcoin:n ja Lightningin käytöstä on, jos lopulta luovutaan juuri niistä seikoista, jotka erottavat ne perinteisistä valuutoista ja pankeista?



Bitcoin:n kaksi tärkeintä arvolupausta ovat rahapoliittinen suvereniteetti (rahan liikkeeseenlasku ja hallussapito eivät ole enää riippuvaisia keskusviranomaisesta) ja sensuurin vastustaminen (kolmas osapuoli ei te estää tai suodattaa maksuja). Lightningin säilytysjärjestelmä on vastoin molempia näitä tatetteita: et te tarkistaa alustan sisäistä rahan määrää, ja määritelmän mukaan operaattori, jolla on hallussaan kaikki varat ja kaikki kanavat, te sensuroida, viivästyttää, priorisoida tai estää maksusi. Näissä olosuhteissa temme oikeutetusti kysyä itseltämme, **mitä järkeä on käyttää bitcoinia Lightningin kautta, jos se toistaa samat luottamuksen ja riippuvuuden mallit kuin perinteisissä valtiollisissa valuuttajärjestelmissä**.



> Tarvitaan sähköinen maksujärjestelmä, joka perustuu luottamuksen sijasta kryptografisiin todisteisiin ja jonka avulla kaksi halukasta osapuolta te tehdä liiketoimia suoraan toistensa kanssa ilman luotettavaa kolmatta osapuolta.
*Satoshi Nakamoto, Bitcoin Valkoinen kirja


Filosofian ohella konkreettisempia haittoja sinulle ovat seuraavat. Ensinnäkin sinulla ei ole mitään mahdollisuutta varmistaa, että yrityksellä todella on hallussaan näytettyjä saldoja vastaavat bitcoinit. Yritys te toimia murto-osavarannolla, joutua hakkeroiduksi, mennä konkurssiin tai yksinkertaisesti kadota. Tällöin olet vain yksi velkoja, jolla ei ole mitään todellista takuuta siitä, että saat rahasi takaisin.



Toiseksi yhtiöön kohdistuu sääntelyyn liittyviä riskejä: kieltotuomioita, varojen jäädyttämistä, käyttäjien tai liiketoimien estämistä koskevia pyyntöjä, tehostettua valvontaa tai jopa toiminnan suoranaista kieltämistä tietyillä lainkäyttöalueilla. Jokainen palveluntarjoajaa rasittava rajoitus heijastuu mekaanisesti sinuun.



Luottamuksellisuuden osalta tilanne ei ole parempi. Säilytyspalvelun tarjoaja näkee kaikki rahavirtasi: summat, taajuudet, vastaanottajat, saldot ja kulutustottumukset. Yhdistettynä sovelluksen antamiin tietoihin ja mahdollisesti Bitcoin:n taustalla olevaan ketjuanalyysiin nämä tiedot tevat antaa erittäin tarkan profiilin taloudellisesta toiminnastasi. Jälleen kerran, se on kaukana Bitcoin:n tatetteesta vähentää talousseurantaa.



Hyvä uutinen on, että oman Lightning-solmun käyttäminen ei ole enää teknisten asiantuntijoiden tehtävä, kuten se saattoi olla 2010-luvun lopulla. Kotikäyttäjille on tarjolla suhteellisen yksinkertaisia ratkaisuja, joista kerromme tarkemmin seuraavassa luvussa.




## Oikean ratkaisun valitseminen työhön


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Nykyään on mahdollista saada käyttökokemus, joka on hyvin lähellä Lightning custodial wallet:n käyttökokemusta, vaikka se olisi edelleen omavalvonnassa. Tämän luvun tatetteena on auttaa sinua valitsemaan profiiliisi parhaiten sopiva polku.



### Vaihtoehto 1: Älä käytä Lightningia suoraan



Ensimmäinen ratkaisu on yksinkertaisesti olla käyttämättä Lightningia natiivisti, mutta käyttää Bitcoin:tä tai Liquid:ta wallet:a, johon on upotettu atomiset swapit. Esimerkiksi Aqua- tai Bull Bitcoin Wallet-sovellukset käyttävät tätä menetelmää mahdollistamalla Lightning-laskujen maksamisen käyttämättä itse Lightning-solmua ja pysyen samalla omavalvonnassa.



Periaate on yksinkertainen: varasi pysyvät Bitcoin:ssa, joko on-chain:ssä tai Liquid:ssä, ja pääset niihin käsiksi wallet:n kautta, jossa sinulla on avaimet perinteiseen tapaan. Kun skannaat Lightning-laskun, wallet käynnistää transaktion (on-chain tai Liquid) atomivaihtopalveluun. Tämä palvelu hoitaa sitten Lightning-maksun oman solmunsa kautta käyttäen on-chain:n tai Liquid:n kautta antamiasi bitcoineja. Näin ollen sinun ei tarvitse itse käsitellä Lightning-kanavia, mutta tet silti maksaa Lightning-laskuja saumattomasti.



![Image](assets/fr/013.webp)



Tämän lähestymistavan suurimpana etuna tavanomaiseen Lightning custodial wallet:een verrattuna on se, että sinulla on koko ajan 100-prosenttinen määräysvalta varoistasi. Bitcoinit ovat omassa onchain- tai Liquid wallet-ketjussasi, jossa on oma muistisääntösi. Jopa vaihdon aikana pysyt varojen hallussasi, koska vaihto on atomaattinen. Se perustuu salausmekanismiin, joka varmistaa, että on vain kaksi mahdollista lopputulosta: joko vaihto onnistuu täysin tai se epäonnistuu, jolloin palvelu ei te ottaa varojasi haltuunsa.



Useimmat tämäntyyppisiä toimintoja tarjoavat salkut käyttävät [Boltz](https://boltz.exchange/) -palvelua swapin teknisessä osassa.



Tämä ratkaisu tarjoaa myös mielenkiintoisia etuja luottamuksellisuuden kannalta, erityisesti kun se yhdistetään Liquid:een. Aloittelijalle se on myös erittäin helppo asentaa ja tallentaa: klassinen muistisääntö, ei kanavia, ei tasapainotettavaa likviditeettiä...



Toisaalta tällä lähestymistavalla on rajoituksensa. Ensinnäkin se ei ole mitattavissa: olet riippuvainen vaihtopalvelun saatavuudesta ja hyvästä tahdosta. Jos se ei enää halua käsitellä tiliäsi tai lopettaa toimintansa, et te enää maksaa salamalaskuja sen kautta. Sitten on vielä huomattavat maksut: maksat sekä onchain- tai Liquid-transaktiomaksut että swap-palvelun provision. Jos onchain-maksut nousevat jyrkästi, Lightningin käytöstä te tulla erittäin kallista.



Satunnaiseen käyttöön se on siis vielä hyväksyttävä, mutta erittäin aktiivisen Lightning-käyttäjän on parempi käyttää oikeaa Lightning-solmua.



### Vaihtoehto 2: Sisäänrakennetut Lightning-solmut



Toinen ratkaisujen luokka perustuu suoraan mobiilisovellukseen upotettuihin salamasolmuihin. Phoenix Wallet oli tämän mallin edelläkävijä, ja se on edelleen vertailukohde. Nykyään muut hankkeet tarjoavat vastaavia lähestymistapoja, kuten Zeus (sulautetussa tilassa) tai BitKit.



Idea on yksinkertainen: sovellus itse asiassa käyttää Lightning-solmua, mutta kaikki monimutkaiset toiminnot hoidetaan automaattisesti taustalla. Sinulla on "*Lightning wallet*" -käyttöliittymä, jossa on muistisana varmuuskopiointia varten, näet saldon ja maksat laskut, mutta et hallitse kanavia, likviditeettiä tai useimpia parametreja.



![Image](assets/fr/014.webp)



Nämä ratkaisut ovat aina itsehuoltajia. Varoja ohjaavat avaimet ovat generated, ja ne on tallennettu puhelimeesi, ja varmuuskopiointi tapahtuu seed:n tai vastaavan mekanismin avulla. Sinulla ei ole vain tiliä palveluntarjoajalla, vaan omistat itse asiassa bitcoineja, jotka on lukittu kanaviin, jotka kuuluvat sinulle ja joita ei te varastaa.



LN:n ajoneuvosolmujen edut ovat lukuisat:




- erittäin helppo asentaa ja käyttää;
- käyttäjäkokemus, joka on lähellä Lightning wallet -laitteen käyttökokemusta, mutta jossa on oma säilytys;
- ei manuaalista kanavien tai likviditeetin hallintaa;
- suhteellisen yksinkertainen varmuuskopiointi.



Näillä sulautetuilla wallet:lla on kuitenkin myös merkittäviä rajoituksia. Ensinnäkin luottamuksellisuuden osalta palveluoperaattorilla (esim. ACINQ Phoenix:n tapauksessa) on melko yksityiskohtainen kuva solmun kautta kulkevista virroista: määrät, taajuudet, vastaanottajat, vaikka tämä on varmasti paranemassa erityisesti *Trampoliinisolmujen* asteittaisen käyttöönoton myötä. Toiseksi olet erittäin riippuvainen tästä operaattorista tärkeimpänä Lightning-vertaisoperaattorina. Jos ACINQ-solmu ei ole käytettävissä (Phoenix:n tapauksessa), jos yhtiöön kohdistuu sääntelypaineita tai jos se muuttaa liiketoimintamalliaan, käyttökokemuksesi te heikentyä huomattavasti tai jopa vaarantua.



Yksinkertaisuudella on kuitenkin hintansa. Sulautetut LN-solmupalvelut veloittavat yleensä erityisiä maksuja talletuksista, nostoista tai tietyistä kanavanhallintatoimista. Mielestäni tämä malli on järkevä tarjotun palvelun kannalta, mutta intensiivisessä käytössä se te olla paljon kalliimpi kuin hyvin hoidettu perinteinen Lightning-solmu.



### Vaihtoehto 3: klassinen Lightning-solmu



Kolmas ratkaisu, jota tarkastelemme tarkemmin tällä LNP202-kurssilla, on käyttää perinteistä Lightning-solmua erillisellä palvelimella tai laitteella.



"Klassisella" tarkoitan sitä, että asennat ja konfiguroit Lightning-toteutuksen (esim. LND) itse oman Bitcoin-solmusi päälle. Sinä valitset vertaisverkkosi, avaat kanavasi, hallinnoit saapuvaa ja lähtevää likviditeettiäsi ja määrität reititysmaksukäytäntösi.



Itsemääräämisoikeuden kannalta se on paras ratkaisu.  Jos palvelu katoaa, sats:si pysyy hallitsemissasi kanavissa, ja tet palauttaa ne ketjussa. Voit myös optimoida pitkän aikavälin kustannuksiasi: kun kanavasi on oikein mitoitettu ja hallinnoitu, maksujen kokonaiskustannuksista te tulla hyvin alhaiset.



Luottamuksellisuuden osalta Lightningin oman mallin rajoitukset ovat tietenkin temassa, mutta et luovuta koko liiketoimintaasi yhdelle toimijalle.



Sen sijaan klassisen Lightning-solmun perustaminen on selvästi monimutkaisempaa: sinun on asennettava, konfiguroitava, ylläpidettävä, seurattava päivityksiä, ymmärrettävä kanavien ja veloituskäytäntöjen logiikka, hallittava kanavia ja kassavirtaa ja niin edelleen. Väärä konfigurointi, huolimaton varmuuskopiointi tai huolimaton hallinta tevat johtaa helpommin sats:n menetykseen. Solmun on myös toimittava jatkuvasti.



Juuri tätä polkua ehdotan sinulle tällä kurssilla, ja autan sinua joka askeleella rajoittamaan riskejä ja jäsentämään lähestymistapaa.



### Mikä ratkaisu millekin käyttäjäprofiilille?



Jotta tet valita Lightning-käyttäjäprofiilillesi sopivan ratkaisun, sinun on otettava huomioon kaksi tekijää: kuinka usein käytät Lightningia ja kuinka paljon haluat teknistä hallintaa.



Jos et tee satunnaisesti monia salamamaksuja, mutta haluat silti pystyä maksamaan LN-laskuja puhelimestasi silloin tällöin luopumatta omahallinnosta: Bitcoin tai Liquid wallet, jossa on swap-toiminto, on luultavasti paras vaihtoehto. Säilytät omistusoikeuden varoihisi, et hallinnoi solmuja ja hyväksyt hieman korkeammat maksut yksinkertaisuuden vastineeksi.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Jos käytät Lightningia melko säännöllisesti ja haluat oikean solmun edut, mutta et halua käyttää aikaa kanavien, maksujen tai infrastruktuurin hallintaan, mobiili sulautettu Lightning-solmu on hyvä ratkaisu. Säilytät varojesi hallinnan, käyttöliittymä pysyy hyvin helppokäyttöisenä, ja kaikki monimutkaisuus on piilotettu, mutta hintana on huomattava riippuvuus operaattorista.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Jos olet keskitason tai edistynyt käyttäjä, joka on valmis investoimaan aikaa infrastruktuurin ymmärtämiseen ja hallintaan ja joka haluaa hallita kanavia, likviditeettiä ja kustannuksia mahdollisimman hyvin: klassinen palvelinpohjainen Lightning-solmu on oikea ratkaisu. Se on vaativin ratkaisu, mutta myös parhaiten sopusoinnussa Bitcoin:n ajatuksen suvereniteetista kanssa.




# Ensimmäisen Lightning-solmun luominen


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## LND:n asentaminen Umbrel:n kanssa


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nyt kun olemme käyneet läpi Lightningin perusteet ja saatavilla olevat ratkaisut, on aika siirtyä asiaan. Tämän kurssin suorittamiseen tarvitset Bitcoin-solmun, joka on synkronoitu Umbrel:ään. Tämä LNP202-kurssi on jatkoa BTC 202:lle; jos sinulla ei vielä ole Bitcoin-solmua, pyydän sinua käymään tämän toisen kurssin ennen kuin palaat tänne, kun solmusi on synkronoitu. Suosittelen vahvasti, että tutustut siihen, sillä en aio mennä yksityiskohtaisesti sen toimintaan, konfigurointiin ja turvatoimiin.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Tässä ensimmäisessä luvussa tarkastelemme LND:n asentamista Umbrel-laitteeseen. Umbrel:n toimintatapa tekee tästä vaiheesta hyvin yksinkertaisen, sillä sinun tarvitsee vain asentaa sovellus.



Avaa etusivulta käyttöliittymän alareunassa oleva sovelluskauppa.



![Image](assets/fr/015.webp)



Kirjoita hakupalkkiin `Lightning Node` ja napsauta sitten sovellusta.



![Image](assets/fr/016.webp)



Käynnistä asennus napsauttamalla `Install`-painiketta.



![Image](assets/fr/017.webp)



Avaa sovellus etusivulta napsauttamalla sitä ja valitse sitten "Aseta uusi solmu".



![Image](assets/fr/018.webp)



Sinulle annetaan 24-sanainen muistisääntö. Pidä se turvallisessa paikassa. Tarkastelemme seuraavassa luvussa tarkemmin, miten Lightning-solmun käyttöoikeus palautetaan (tämä on paljon monimutkaisempi prosessi kuin yksinkertaisen Bitcoin wallet:n tapauksessa), mutta muista toistaiseksi, että tällä lauseella on ratkaiseva merkitys ja että se on säilytettävä erittäin huolellisesti.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tallenna tämä lause samalla tavalla kuin tavanomainen muistisääntö: fyysiselle välineelle (paperille tai metallille), joka on tallennettu turvalliseen paikkaan, ja napsauta sitten `NEXT`-painiketta.



![Image](assets/fr/019.webp)



Kirjoita sitten lauseen sanat ja tarkista, että olet kirjoittanut ne oikein.



![Image](assets/fr/020.webp)



Varoitusviesti muistuttaa sinua siitä, että sovellus on beta-versiossa ja että Lightning Network on edelleen kokeellinen teknologia. Älä tietenkään koskaan sitoudu Lightning-solmuun määriä, joita et ole valmis menettämään.



Tämän jälkeen pääset Lightning-solmun pääkäyttöliittymään. Vasemmalla näet solmussasi isännöidyn Bitcoin-ketjun wallet:n. Tämä on se generated 24-sanaisesta lauseesta, jonka olet juuri tallentanut.



Keskellä on Lightning wallet. Se edustaa itse asiassa lähtevää käteistäsi eli bitcoineja, joita omistat Lightning-kanavissasi.



Oikealla näet useita tärkeitä tietoja solmusta:




- Yhteyksien ja atemien kanavien määrä;
- Lähtevän kassavirtasi kokonaismäärä eli se, mitä tet teoriassa käyttää Lightningiin;
- Saapuva likviditeettisi yhteensä eli se, mitä tet teoreettisesti saada Lightningilla.



![Image](assets/fr/021.webp)



Aloitetaan mukauttamalla solmua. Napsauta kolmea pientä pistettä käyttöliittymän oikeassa yläkulmassa ja valitse sitten "Lisäasetukset". Henkilökohtaistaminen -alavalikossa tet määrittää solmulle julkisen nimen (vältä oikean nimesi käyttöä) ja valita sen värin.



![Image](assets/fr/046.webp)



Napsauta sitten vihreää `SAVE AND RESTART`-painiketta käynnistääksesi solmun uudelleen ja soveltaaksesi muutoksia.



Lightning-solmusi on nyt valmis avaamaan ensimmäiset maksukanavansa. Katsotaan kuitenkin ensin, miten sats:ää te suojata!



## Lightning-solmun tallentaminen


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Ennen kuin lähetät ensimmäisen sats:n solmuun, on tärkeää ymmärtää, miten sen varmuuskopiointi toimii ja mitkä ovat siihen liittyvät riskit. Toisin kuin yksinkertainen Bitcoin onchain-salkku, Lightning-solmun varmuuskopiointi on melko monimutkaista: väärä strategia te johtaa varojen pysyvään menetykseen. Tässä luvussa tarkastelemme, mitä varmuuskopiointia todella tarvitaan ja miten Umbrel hoitaa tämän prosessin LND:n avulla.



Tällä kurssilla käytämme LND (*Lightning Network Daemon*) -toteutusta. Vaikka periaatteet ovat samankaltaisia muissa toteutuksissa, palautustiedostot ja menettelyt, joista aion puhua, ovat LND:n erityispiirteitä.



### Mitä minun pitäisi säästää Lightning-solmuun?



Lightning-solmun kohdalla ei riitä, että seed tallennetaan ja toivotaan, että kaikki palaa ennalleen. Useilla elementeillä on eri roolit, joten on tärkeää erottaa ne toisistaan.



#### seed (*aezeed*)



Kun alustat LND:n, saat 24-sanaisen seed:n. Tämä on LND:lle ominainen muoto nimeltään "*aezeed*". Se ei ole klassinen seed BIP39, vaikka se näyttääkin siltä. Tästä seed:stä LND saa Lightning-solmuun liittyvän ketjussa olevan wallet:n yksityiset avaimet, eli osoitteet, joihin tet vastaanottaa tai joihin tet palauttaa bitcoineja kanavan sulkemisen jälkeen.



![Image](assets/fr/019.webp)



Tätä seed:a tedaan siis käyttää solmuun liittyvän ketjussa olevan wallet:n uudelleenluomiseen ja jo ketjuun palautettujen varojen hakemiseen (esim. kanavan sulkemisen jälkeen). Toisaalta pelkkä seed ei riitä palauttamaan vielä atenna olevia Lightning-kanavia, sillä se ei sisällä tarvittavia tietoja kanavien tilasta.



#### Kanavatietokanta (`channel.db`)



LND tallentaa kanavien yksityiskohtaisen tilan tietokantaan nimeltä `channel.db`. Tämä tietokanta sisältää:




- atemien kanavien luettelo;
- vertaisesi ja heidän tunnisteensa;
- kunkin kanavan viimeiset commitment transaction:t (peräkkäiset tilat, jotka määrittelevät, kuka omistaa mitäkin kanavassa, ja mahdollistavat ketjussa olevien varojen palauttamisen ongelmatilanteessa);
- tiedot, joita tarvitaan rangaistakseen vertaista, joka yrittää lähettää vanhan raportin.



Ongelmana tässä tietokannassa on se, että se muuttuu jatkuvasti: jokainen maksu, jokainen reititys, jokainen kanavan avaaminen tai sulkeminen muuttaa sen sisältöä. Tämän vuoksi perinteinen varmuuskopiointi (esim. säännöllinen kopio `channel.db`:stä) on vaarallista. Jos palautat liian vanhan version `channel.db`:stä ja kokoat solmun uudelleen tämän vanhentuneen tilan kanssa, vertaisesi tevat katsoa, että lähetät vanhaa kanavan tilaa. Tässä tapauksessa protokollaan sisältyy rangaistus: vertaisesi te periä takaisin koko kanavan varat, aivan kuin olisit yrittänyt huijata.



Käytännössä `channel.db` ei siis ole varsinainen varmuuskopiointiväline. Se on solmusi elävä tila. Ainoa tilanne, jossa on järkevää käyttää sitä solmun palauttamiseen, on se, että palautat tämän tietokannan suoraan koneelta, joka on juuri vikaantunut (esim. levyltä, joka on vielä luettavissa). Tässä tapauksessa palautat uusimman tilan ja tet käynnistää LND:n uudelleen toisella koneella tämän tietokannan perusteella varmana siitä, että tämä tila on mahdollisimman ajantasainen, koska vanha kone ei ole enää käynnissä. Toinen tilanne, jossa tämä menetelmä te toimia asianmukaisena varmuuskopiona, on kahden levyn kokoonpano, jossa on dynaaminen, pysyvä kopio toisesta toiselle levylle. Tällainen kokoonpano on kuitenkin monimutkaisempi toteuttaa.



Mutta ajoittaisten kopioiden tekeminen tiedostosta `channel.db` ja niiden tallentaminen varmuuskopioiksi, jotka tedaan palauttaa myöhemmin, on erittäin huono ajatus: sinä päivänä, kun käytät niitä, on vaarana, että rankaiset itseäsi ja menetät koko sats:n.



#### Staattinen kanavan varmuuskopiointi (SCB)



LND on ottanut käyttöön *Static Channel Backup* (SCB) -mekanismin, joka mahdollistaa katastrofista palautumisen. Kyseessä on erityinen tiedosto, jota kutsutaan usein nimellä `channel.backup` ja joka sisältää staattisia tietoja kanavistasi: ketkä ovat vertaisesi, miten heihin te ottaa yhteyttä ja mitkä ovat kanavasi.



Tämä tiedosto ei sisällä yksityiskohtaista kanavan tilaa tai päivityshistoriaa. Sen avulla et te avata kanavia uudelleen täsmälleen samassa tilassa, jossa ne olivat, etkä te jatkaa tämän Lightning-solmun käyttöä.  Toisin kuin `channel.db`-tiedostoa, jota muutetaan jokaisen maksun tai reitityksen yhteydessä, SCB-tiedostoa päivitetään siis vain, kun kanava avataan tai suljetaan.



Kun palautus tapahtuu SCB:n kautta, prosessi on seuraava:




- Palautat seed:n (*aezeed*), joka luo uudelleen Lightning-solmuun liittyvän ketjussa olevan wallet:n;
- Toimitat LND:lle viimeisimmän SCB:n;
- LND käyttää SCB:tä löytääkseen luettelon vertaisverkoistasi ja kanavista, joita sinulla on heidän kanssaan;
- Se ottaa yhteyttä kuhunkin vertaiskumppaniin, kertoo heille, että olet menettänyt tietoja, ja pyytää heitä sulkemaan kanavasi heidän kanssaan, jotta tet palauttaa onchain-osuutesi.



Ajatuksena on, että kun kollegasi huomaavat, että ilmoitat tietojen katoamisesta, he lähettävät viimeisen commitment transaction-lähetyksensä ja sulkevat temakanavan. Kun nämä transaktiot on vahvistettu, varasi ilmestyvät jälleen ketjussa olevaan salkkuusi (joka on linkitetty seed:een).



Tämä palautusmekanismi ei kuitenkaan ole täydellinen. Ensinnäkin se ei itse asiassa palauta Lightning-solmua, koska kaikki kanavat suljetaan. Tämän jälkeen sinun on rakennettava uusi Lightning-solmu tyhjästä. Toiseksi se ei takaa 100-prosenttista palautumista, vaikka se lisääkin huomattavasti mahdollisuuksia palauttaa ketjussa olevat saldosi ongelmatilanteessa. Tämä palautusprotokolla riippuu nimittäin vertaisverkostojesi yhteistyöstä ja saatavuudesta: jos yksi niistä on offline-tilassa, on menettänyt omat tietonsa tai kieltäytyy yhteistyöstä, varasi tevat jäädä estyneiksi tai jopa kadota pysyvästi.  



Yhteenvetona tedaan todeta, että LND:n hyvä salamavarmuusstrategia perustuu kolmeen pilariin:




- seed (*aezeed*), onchain-kerrosta varten;
- Luotettava automaattinen SCB-varmuuskopiointi;
- Hyvä kanavanhallinta valitsemalla luotettavia vertaisverkkopalveluja ja sulkemalla ennaltaehkäisevästi ne, jotka ovat usein tatettamattomissa.



### Miten Umbrel hallitsee LND-solmun varmuuskopiointia?



Umbrel tarjoaa LND-solmulle yksinkertaistetun varamekanismin, joka perustuu nimenomaan SCB:hen. Tarkoituksena on säästää sinut tämän tiedoston omalta käsittelyltä, tehdä siitä varmuuskopio ja automatisoida prosessi mahdollisimman pitkälle.



Kun luot solmun Umbrel:lle, saat seed:n, jolla on kaksi tehtävää:




- se johtaa Bitcoin-ketjun wallet:n, joka liittyy Lightning-solmuun;
- sitä käytetään varmuuskopion tunnisteen ja salausavaimen määrittämiseen, joita käytetään SCB:n etävarmistuksissa.



Tämän mekanismin ansiosta Umbrel tekee automaattisesti salatun varmuuskopion SCB:stäsi ja tallentaa sen palvelimilleen Torin kautta. SCB tallennetaan salattuna seed:stä saadun avaimen avulla. Tietojen katoamisen sattuessa sinun tarvitsee siis vain luoda Bitcoin ja Lightning-solmu uudelleen Umbrel:lla, samalla tai toisella koneella, ja syöttää sitten seed:ääsi. Sen jälkeen tet hakea viimeisimmän SCB:n tilan Umbrel-palvelimilta, purkaa sen salauksen ja aloittaa varojen palauttamisprosessin.



Solmusi salaa nämä varmuuskopiot paikallisesti ennen niiden lähettämistä, mikä takaa tietojesi luottamuksellisuuden: Umbrel ei te lukea SCB:n sisältöä. Lähetys tapahtuu Torin kautta, mikä estää IP-osoitteesi vuotamisen. Lisäksi Umbrel lisää liikenteeseen kohinaa (satunnainen pehmuste ja epäsäännöllisin väliajoin lähetetyt väärät varmuuskopiot), jotta palvelin ei pysty päättelemään, milloin juuri sinä avaat tai suljet kanavan.



Tämän menetelmän tärkein etu on se, että se yksinkertaistaa huomattavasti Lightning-solmun varmuuskopiointia: sinun tarvitsee varmuuskopioida seed vain kerran solmun alustuksen aikana. Tähän liittyy jonkin verran riskejä, koska kyseessä on vain SCB:n varmuuskopiointi, mutta kohtuullisille määrille se on hyväksyttävä kompromissi.



### Parhaat käytännöt tappioriskin rajoittamiseksi



Vaikka Umbrel olisi varmuuskopioitu, muutamalla yksinkertaisella hyvällä käytännöllä tedaan huomattavasti vähentää sats:n menettämisen riskiä:





- Seuraa vertaistesi saatavuutta:



Jos tärkeään kanavaan liittyy usein tatettamaton tai epävakaa vertaisverkkopalvelin, on turvallisempaa sulkea se puhtaasti, kun solmusi vielä toimii. Ennaltaehkäisevä yhteistoiminnallinen tai pakotettu sulkeminen poistaa mahdollisen ongelmanlähteen SCB:n toipumisen yhteydessä.





- Vältä keskittämästä liikaa likviditeettiä tuntemattomiin vertaisiin:



Mitä suurempi kanava vertaisvertaisella on sinuun, sitä tärkeämpää on olla luotettava. Valitse vakavasti otettavat, hyvät yhteydet omaavat ja aktiiviset solmut, jotta kaikki SCB:n kautta tapahtuva tuleva palautus te sujua ongelmitta.





- Täydennä Umbrel:ää paikallisilla varmuuskopioilla:



Umbrel:n automaattisen varmuuskopioinnin lisäksi tet myös säilyttää salatun kopion SCB-tiedostostasi (`channel.backup`) ulkoisella tietovälineellä ja päivittää sen säännöllisesti. Ihannetapauksessa sinun tulisi uudistaa se aina, kun avaat tai suljet kanavan. Näin saat varmuuskopiointiratkaisun, jos Umbrel:n automaattinen varmuuskopiointipalvelu ei jostain syystä ole käytettävissä.





- seed:n hallinta oikein



seed Umbrel ei ainoastaan palauta ketjussa olevaa wallet:ääsi, vaan myös johtaa salausavaimen varmuuskopioita varten. Hyökkääjä, jolla on pääsy siihen, tesi siis käynnistää palautuksen ja siirtää varojasi omaan wallet:äänsä ilman, että hänellä olisi edes fyysistä pääsyä solmuun.



Jos sinun on siis palautettava solmusi, mutta sinulla ei ole enää seed:tä, et te palauttaa mitään: kaikki sats:si menetetään. On siis erittäin tärkeää, että tallennat seed:n erittäin huolellisesti, vain fyysiselle tietovälineelle (paperille tai metallille) ja säilytät sen turvallisessa paikassa. Lisätietoja seed:n hallinnoinnista saat tästä ohjeesta:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Miten tallennan Lightning-solmuni Umbrel:een?



Nyt kun olet ymmärtänyt, miten teoria toimii, mennäänpäs nyt asiaan. Napsauta Lightning Node -sovelluksestasi (joka on itse asiassa LND) kolmea pientä pistettä oikeassa yläkulmassa.



![Image](assets/fr/022.webp)



Varmistuksen kannalta tässä on kolme kiinnostavaa tekijää:




- Tarkista, että `Automaattiset varmuuskopiot` -vaihtoehto on käytössä. Tämä lähettää salatun SCB:n automaattisesti Umbrel:n palvelimille.
- Voit sitten valita, lähetätkö Torin vai clearnetin kautta, käyttämällä `Backup over Tor` -vaihtoehtoa. Kuten edellisissä kappaleissa selitettiin, suosittelen vahvasti Torin käyttöä luottamuksellisuuden säilyttämiseksi.
- Lopuksi on painike "Lataa kanavan varmuuskopiotiedosto", jonka avulla tet ladata tietokoneellesi kanavan varmuuskopiotiedoston eli salatun tilannekuvan SCB:stäsi. Näin tet tehdä ajoittain lisää paikallisia varmuuskopioita niiden lisäksi, jotka lähetetään automaattisesti Umbrel-palvelimille.



Nyt tiedät, miten tet suojata Lightning-solmun sats:n tietojen häviämiseltä. Seuraavassa luvussa tarkastelemme, miten tet suojata solmun huijausyrityksiltä.




## Watchtower: rooli ja asetukset


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



Lightningissa kukin kanava perustuu peräkkäisten tilojen sarjaan, jota edustavat julkaisemattomat commitment transaction:t. Jokaisen Lightning-maksun tai -reitityksen yhteydessä kanavan kaksi osallistujaa muodostavat uuden commitment transaction-parin, joka kuvastaa varojen senhetkistä jakautumista kanavassa. Vanhat commitment transaction:t vanhentuvat.



Jos jompikumpi osapuoli julkaisee vanhentuneen tilan, toisella osapuolella on oikeus määrätä seuraamuksia ja periä takaisin kanavan varat kokonaisuudessaan. Tässä luvussa tarkastelemme lyhyesti, miten tämä mekanismi toimii, ja selitämme sitten, miten perustetaan ***watchtower***: järjestelmä, joka suojaa Lightning-solmua mahdollisilta huijausyrityksiltä.



### Vartiotornien toiminnan ymmärtäminen


Kullakin kanavan osapuolella on milloin tahansa commitment transaction, jonka julkaiseminen mahdollistaisi kanavan sulkemisen ja oman osuutensa varojen takaisin saamisen. Tätä prosessia kutsutaan *pakotetuksi sulkemiseksi*. Mutta jos he yrittäisivät julkaista vanhemman commitment transaction:n, joka vastaa kanavan aiempaa tilaa, jossa sillä oli enemmän sats:ta, tätä tapahtumaa pidettäisiin huijausyrityksenä. Tässä tapauksessa vastapuoli te käyttää tähän vanhempaan tilaan liittyvää peruutusavainta saadakseen takaisin koko kanavan varojen määrän, kun taas huijari on tilapäisesti estetty aikalukolla.


Tämä järjestelmä tarkoittaa, että vanhan tilan julkaiseminen eli huijausyritys on hyvin riskialtista: jos toinen osapuoli näkee tämän transaktion mempoolissa tai lohkoketjussa ennen aikalukon päättymistä, se te käyttää peruutusavainta ja saada kaikki varat takaisin. **Siten Lightning-kanavasi turvallisuus riippuu kyvystäsi havaita huijausyritys timelockin asettamassa aikaikkunassa**.



#### Miksi vartiotorneja tarvitaan?



Rangaistusmekanismi toimii vain, jos vahingon kärsinyt osapuoli pystyy siihen:




- seurata jokaista uutta Bitcoin-lohkoa nähdäkseen, onko kanava commitment transaction julkaistu;
- määritetään, vastaako tämä tapahtuma viimeistä temassa olevaa vai peruutettua tilaa;
- peruutustilanteessa lähettää laillinen transaktio ajoissa ja käyttää peruutusavainta kaikkien varojen takaisin saamiseksi ennen aikalukon päättymistä.



![Image](assets/fr/023.webp)



Ihanteellisessa tilanteessa Lightning-solmusi on verkossa 24/7, se on synkronoitu ja seuraa jatkuvasti lohkoketjua. Tästä syystä se te yksin havaita huijausyrityksen ja reagoida siihen. Käytännössä henkilökohtainen Lightning-solmu te kuitenkin sammua, etenkin jos sähköt katkeavat pitkäksi aikaa tai internet-yhteys katkeaa.



 Menetät osan tai kaikki varasi kanavassa.



Watchtower:t otettiin käyttöön tämän riskin vähentämiseksi. Vartiotorni on ulkoinen palvelu, joka valvoo lohkoketjua puolestasi, etsii mahdollisen vanhan tilan julkaisun jossakin kanavassasi ja lähettää tarvittaessa automaattisesti rangaistustapahtuman puolestasi. Joten vaikka Lightning-solmusi pysyisi offline-tilassa pidemmän aikaa, niin kauan kuin käyttämäsi vartiotorni on toiminnassa, se pystyy suojaamaan varojasi seuraamalla mahdollisia huijausyrityksiä ja soveltamalla vastaavaa rangaistusta heti, kun se havaitsee sellaisen.



#### Miten vartiotorni toimii



Vartiotorni on suunniteltu siten, että se saa mahdollisimman vähän tietoa kanavistasi, mutta samalla se pystyy toimimaan ongelman sattuessa:




- Solmusi valmistelee etukäteen mahdollisen rangaistustapahtuman jokaista uutta kanavatilannetta varten. Jos vertainen huijaa, tet tämän tapahtuman avulla saada takaisin kaikki kanavan varat;
- Tämän jälkeen solmusi salaa tämän rangaistustapahtuman käyttämällä vastaavan commitment transaction:n TXID-tunnusta (jota käytettäisiin, jos huijari yrittäisi petosta). Niin kauan kuin sulkeutumista ei tapahdu, vartiotorni ei te purkaa tätä transaktiota, koska se ei täysin tiedä huijaustransaktion TXID-tunnusta;
- Solmusi lähettää valvontatornille paketin, joka sisältää salatun rangaistustapahtuman ja puolet mahdollisen huijaustapahtuman TXID-tunnuksesta.



Koska vartiotornille lähetetty TXID on epätäydellinen, se ei te purkaa oikeustapahtuman salausta. Se te kuitenkin seurata lohkoketjua TXID:n löytämiseksi, joka vastaa sen omistamaa osaa. Jos se havaitsee tällaisen transaktion, se yrittää käyttää kyseisen transaktion täydellistä TXID:tä rangaistustransaktiosi salauksen purkamiseen. Jos salauksen purkaminen onnistuu, se tietää, että kyseessä on huijausyritys, ja julkaisee rangaistustransaktion välittömästi puolestasi.



![Image](assets/fr/024.webp)



Vartiotornilla ei siis ole näkyvyyttä kanaviesi yksityiskohtiin: ei vertaistesi henkilöllisyyteen, saldoihin eikä transaktioiden rakenteeseen. Se näkee vain salatut paketit. Ainoa tieto, jonka se te päätellä, on kanaviesi päivitysnopeus, sillä se saa paketin jokaisesta uudesta tilasta, mutta ei te tietää sen sisältöä. Huijauksen sattuessa se saa varmasti selville kanavatiedot purkamalla rangaistustapahtuman salauksen, mutta ainakin sats:si pelastuu.



Tämä mekanismi perustuu kompromissiin: delegoit kyvyn julkaista ennalta allekirjoitettu rangaistustapahtuma valvontatornille, mutta tämä tapahtuma pysyy täysin läpinäkymättömänä valvontatornille, kunnes jokin huijaus tapahtuu. Vartiotorni ei te muuttaa vastaanottajia eikä siirtää varoja, koska sillä on vain jo allekirjoitettu transaktio, jonka tuotot on jäädytetty sinun eduksesi. Se ei myöskään te tietää kanavan yksityiskohtia laillisessa pakkosulkemisessa tai yhteistyösulkemisessa, koska TXID-tunnukset eivät täsmää. Toisaalta Watchtower on edelleen minimaalinen luotettu kolmas osapuoli: sinun on luotettava siihen, että se on verkossa ja lähettää oikeustransaktiosi asianmukaisesti, kun tarvitset sitä.



#### Vartiotorniksi tuleminen



Teoriassa mikä tahansa Lightning-solmu te toimia muiden solmujen vartiotornina (jos ne käyttävät samaa toteutusta, esim. LND), ja samalla sitä itseään suojaavat muut solmut, jotka hoitavat tätä tehtävää sen puolesta. Seuraavissa käytännön osioissa näytän, miten tämä yksinkertainen mekanismi otetaan käyttöön LND:ssä Umbrel:n alaisuudessa.


Tämän vuoksi mielenkiintoinen strategia tesi olla sopia luotettavien bitcoiner-ystävien kanssa, että he toimivat toistensa vartijoina. Sinä valvot heidän kanaviaan, ja he valvovat sinun kanaviasi.



### Etsi altruistinen vartiotorni



Jos et tunne lähistölläsi ketään, joka tesi tarjota vartiotornipalvelua, on olemassa useita epäitsekkäitä julkisia vartiotorneja, joihin tet liittyä. Esimerkiksi tällä LNP202-kurssilla ehdotan, että otat yhteyden LN+:n ja Voltagen yhdessä tarjoamaan vartiotornipalveluun, joka on LND:n vartiotorni.


Täältä löydät kirjautumistiedot:



- Torin kautta:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Clearnetin kautta:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Kiittääksesi heitä tämän ilmaisen vartiotornipalvelun tarjoamisesta, [tet tehdä lahjoituksen Salaman kautta](https://lightningnetwork.plus/donation).


Nyt kun käytämme altruistista vartiotornipalvelua, katsotaan, miten se määritetään LND-solmussamme Umbrel:n alla.


### Vartiotornin pystyttäminen


Napsauta "Lightning Node" -sovelluksessa kolmea pistettä käyttöliittymän oikeassa yläkulmassa ja valitse sitten "Lisäasetukset".


![Image](assets/fr/025.webp)


Siirry sitten valikkoon `Watchtower`.


![Image](assets/fr/026.webp)



Aktite "Watchtower Client" -vaihtoehto ja napsauta sitten "SAVE AND RESTART NODE" -painiketta. Odota, että LND käynnistyy uudelleen.


![Image](assets/fr/027.webp)


Kun uudelleenkäynnistys on valmis, palaa samaan valikkoon ja syötä valitsemasi altruistisen vartiotornin tunnus sille varattuun kenttään. Vahvista sitten klikkaamalla `ADD`-painiketta. Voit myös säätää parametria `Watchtower Client Sweep Fee Rate` (Watchtower-asiakkaan pyyhkäisymaksu): tämä on maksu, jonka olet valmis maksamaan mahdollisesta oikeustapahtumasta, jonka vartiotorni lähettää. Liian korkeaa maksua ei tarvitse valita, mutta liian alhaista maksua kannattaa myös välttää, sillä muuten oikeustapahtumaa ei vahvisteta ajoissa.


Käynnistä solmu uudelleen käyttämällä `SAVE AND RESTART NODE` -painiketta, jotta muutokset tulevat temaan.


![Image](assets/fr/028.webp)



Jos palaat samaan valikkoon, näet, että Lightning-solmua suojaa nyt juuri lisäämäsi vartiotorni.



![Image](assets/fr/029.webp)



Altruistinen vartiotorni on yleensä riittävä, varsinkin jos et sijoita suuria rahamääriä Salamasolmuun ja jos hoidat solmua hyvin (älä jätä sitä pois käytöstä liian pitkäksi aikaa). Jos haluat vielä suuremman turvallisuuden, tet myös lisätä useita toistamalla saman prosessin.



## Avaa ensimmäinen Lightning-kanava


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Jos olet päässyt tähän asti, tiedät jo, että Lightning-solmu ilman kanavaa on kuin tyhjä wallet: se on olemassa, mutta se on hyödytön. Jotta tet lähettää tai vastaanottaa maksuja, solmusi on oltava yhteydessä vähintään yhteen muuhun Lightning-verkon solmuun kanavan kautta. Tulevaisuudessa suosittelemme vahvasti useiden kanavien avaamista häiriönsietokyvyn ja reitityksen tehokkuuden vuoksi. Seuraavissa luvuissa tarkastelemme myös sitä, miten tet hallita likvidejä varoja, optimoida kanavatopologian ja käyttää Umbrel:n LND-perusliittymää kehittyneempiä työkaluja.



Tässä johdantoluvussa tarkoituksena on kuitenkin vain ymmärtää, miten valita hyvä Lightning-vertaisverkko, mistä löytää vertaisverkkojen valintaan tarvittavat tiedot ja miten avata ensimmäinen kanava LND:n perusliittymän kautta.



### Miten valita hyvä Lightning-vertainen?



Kun avaat kanavan, sinun on valittava vertainen: toinen Lightning-solmu, johon solmusi on suoraan yhteydessä kanavan kautta. Vertaisverkon valinta on tärkeä, sillä se vaikuttaa suoraan:




- maksut löytävät helposti tiensä;
- kanaviesi luotettavuus ajan mittaan;
- reitityskustannukset.



Kaikille ei ole olemassa täydellistä kumppania, mutta on olemassa useita luotettavia kriteerejä, joiden perusteella hyvät ehdokkaat tedaan tunnistaa.



#### 1. Solmujen liitettävyys



Hyvä vertaisverkko on solmu, jolla on hyvät yhteydet Lightning-verkkoon. Tämä ei tarkoita pelkästään sitä, että sillä on suuri määrä kanavia (vaikka se te olla indikaattori), vaan ennen kaikkea sitä, että se on yhteydessä muihin luotettaviin solmuihin ja että se on riittävän keskeisellä paikalla verkon kuvaajassa.



Hyvin yhdistetty solmu lisää mahdollisuuksiasi löytää tehokas reitti useimpiin maksukohteisiin. Se vähentää myös tarvittavien välityssolmujen määrää, mikä pitää kustannukset alhaisina.



Sitä vastoin ensimmäisen kanavan avaaminen eristettyyn tai heikosti verkottuneeseen solmuun te rajoittaa mahdollisuuksiasi: tet maksaa tälle vertaisverkkoon kuuluvalle osapuolelle, mutta on paljon vaikeampaa maksaa muulle verkolle.



#### 2. Pääomitus ja kanavakapasiteetti



Hyvä vertainen on myös riittävän pääomitettu solmu. Tämä ilmenee sen kokonaiskanavakapasiteetista (kaikkiin sen kanaviin sitoutuneiden sats:n summa) ja sen keskimääräisestä kanavakapasiteetista (usein on parempi, että on vain muutama hyvin pääomitettu kanava kuin monta pientä).



Solmu, jonka kapasiteetti on naurettava tai jonka kaikki kanavat ovat pieniä, ei pysty reitittämään suuria maksuja, jolloin reititys epäonnistuu.



#### 3. Kulupolitiikka



Kukin solmu asettaa omat reititysmaksunsa (perusmaksu ja maksuprosentti). Hyvä vertaisverkko ei peri kohtuuttomia maksuja strategisista kanavista. Ensimmäiselle kanavalle kannattaa valita solmu, jonka maksut ovat melko maltillisia, jotta et haittaa omia maksujasi.



Muista, että myös omat reititysmaksusi vaikuttavat siihen, miten muut pitävät sinua vertaisverkkona: solmua, joka muuttaa jatkuvasti maksujaan tai asettaa järjettömiä kustannuksia, arvostetaan harten.



#### 4. Vakaus ja virkaikä



Vertaisryhmän vakaus on erittäin tärkeä kriteeri. Hyvällä solmulla on korkea käyttöaika (se on hyvin harten offline-tilassa), se pitää kanavansa auki pitkään eikä se avaa/sulje kanavia jatkuvasti ilman syytä.







Toisaalta vertainen, joka on usein offline-tilassa tai sulkee kanavat nopeasti, te aiheuttaa sinulle ongelmia ja lisäkustannuksia uusien kanavien avaamisesta.



Näiden kriteerienkään avulla et tee täydellistä valintaa ensimmäisellä kerralla. Se on normaalia: vertaislaitteen todellinen laatu paljastuu sen käytössä. Siksi on tärkeää:




- seurata kanavan toimintaa (reititetyt määrät, saatavuus jne.);
- sulkea kanavat, jotka eivät palvele mitään tarkoitusta tai joiden vertaiset ovat liian usein offline-tilassa;
- kohdentaa pääomasi ajan mittaan uudelleen parempiin vertaisyhtiöihin.



Ajatuksena ei ole avata ja sulkea kanavia joka päivä (mikä olisi kallista ketjukustannuksina), vaan kehittää topologia vähitellen niin, että se lähentyy luotettavien ja hyvien yhteyksien päässä olevien vertaisverkkojen joukkoa, joka vastaa tarpeitasi.



### Miten löydän vertaiseni?



Näiden kriteerien soveltamiseen tarvitaan työkaluja, jotka tarjoavat näkyvyyttä Lightning-verkkoon. Tähän tarkoitukseen on saatavilla useita etsintäohjelmia ja palveluja. Tunnetuimpia Lightning-etsintäohjelmia ovat [1ML](https://1ml.com/) ja [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Suosittelen kuitenkin käyttämään [Lightning Labsin Lightning Terminal -työkalua](https://terminal.lightning.engineering/), joka tarjoaa (tosin osittain subjektiivisiin kriteereihin perustuvan) luokituksen Lightning-solmuista, joita pidetään tärkeimpinä kanavan avaamisen kannalta.



![Image](assets/fr/030.webp)



Ongelma tämän rankingin kärjessä olevien erittäin suurten salamasolmujen kanssa on se, että useimmat niistä eivät hyväksy kanavien avauksia alle hyvin suuria summia. Monet soveltavat myös tiukkoja vertaishallintakäytäntöjä, mikä te johtaa kanavasi sulkemiseen. Toisaalta näillä solmuilla ei yleensä ole tarvetta saapuvalle likviditeetille, kun otetaan huomioon niiden yhteyksien määrä.



Siksi suosittelen, että etenet rankingissa alaspäin ja etsit solmun, jolla on hyvät yhteydet, joka on luotettava ja joka on riittävän keskeisellä sijalla verkon kuvaajassa ilman, että se on liian suuri. Esimerkiksi tässä tapauksessa olen tunnistanut Lightning-solmun osoitteessa stacker.news, joka on hyvin yhteydessä, jolla on suuri kapasiteetti ja joka on keskeisellä paikalla verkon kuvaajassa.



![Image](assets/fr/031.webp)



Toinen mielenkiintoinen lähestymistapa on avata kanava solmuun, joka tarvitsee likviditeettiä, kuten tuttuun kauppiaaseen, yhdistykseen tai yhteisöön. Tällä strategialla on kolme etua:




- Koska valittu taho tarvitsee likviditeettiä, sillä on loogisesti vähemmän kannustimia sulkea kanavasi ilman syytä;
- Sen taloudellinen toiminta lisää mahdollisuuksia reitittää tietoja tätä kanavaa pitkin ja siten kerätä joitakin maksuja;
- Teet ekosysteemille palveluksen ja annat arvokkaan panoksen muille bitcoin-käyttäjille.



Kun olet tunnistanut asiaankuuluvan solmun, tet hakea sen solmutunnuksen. Se on yksinkertaisesti solmun julkisen avaimen, `@`-erottimen, sen IP- tai Tor-osoitteen ja käytetyn portin yhdistelmä. Tunnus on helposti saatavilla solmun profiilista missä tahansa Lightning-selaimessa.



### Avaa ensimmäinen kanava LND:n kautta



Nyt kun olemme tunnistaneet solmun, jolla avaamme ensimmäisen kanavamme, meidän on lukittava sats siihen. Tätä varten sinun on syötettävä Bitcoin onchain wallet:een, joka liittyy LND:ään.



Etsi LND:n pääkäyttöliittymästä Bitcoin Wallet ja napsauta sitten Talletus-painiketta. Ketjussa oleva vastaanottava osoite on tällöin generated: lähetä sats siihen. Siirrettävä määrä riippuu kapasiteetista, jonka haluat osoittaa ensimmäiselle kanavallesi, mutta muista, että sinun on lähetettävä hieman enemmän kuin tateteltu kapasiteetti. Jos esimerkiksi haluat avata 500 000 sats-kanavan, älä lähetä täsmälleen 500 000 sats, vaan suuremman määrän.



![Image](assets/fr/032.webp)



Kun tapahtuma on lähetetty, se näkyy käyttöliittymässä. Odota vahvistusta ennen kanavan avaamista. Kun se on vahvistettu, sen vieressä näkyy vihreä nuoli.



![Image](assets/fr/033.webp)



Vieritä alaspäin pääkäyttöliittymään ja napsauta sitten `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Syötä sen solmun `Node ID`, jonka kanssa haluat avata kanavan, ilmoita summa, jonka haluat lukita, ja säädä sitten avaustapahtumamaksu ketjun maksumarkkinoiden tilan mukaan. Varmista tietysti etukäteen, että sinulla on riittävästi varoja LND onchain-salkussasi.



Kun kaikki parametrit on asetettu, napsauta `OPEN CHANNEL`-painiketta.



![Image](assets/fr/035.webp)



Odota, että avaustapahtuma vahvistetaan ketjussa. Ensimmäinen kanavasi on nyt virallisesti toiminnassa: onnittelut!



Näet, että tällä hetkellä 100 % kanavan likviditeetistä on minun puolellani: se on normaalia, koska minä olen se, joka avasi kanavan. Maksujen ja reitityksen kehittyessä tämä jakauma muuttuu, mutta kanavan kokonaiskapasiteetti pysyy aina samana.



![Image](assets/fr/036.webp)



Nyt kun sinulla on kanava, tet suorittaa ensimmäiset Lightning-maksut, kunhan valittu solmu on liitetty asianmukaisesti verkkoon. Myöhemmissä luvuissa tarkastelemme tietysti, miten tet määrittää kätevämmän tavan maksaa Lightning-laskuja matkapuhelimesta. Mutta nyt kokeillaan tehdä ensimmäinen maksu suoraan LND:stä Umbrel:ään.



Napsauta tätä varten kohdassa `Lightning Wallet` painiketta `SEND` ja liitä sitten asetettava lasku.



![Image](assets/fr/037.webp)



Laskun summa näytetään. Vahvista maksu klikkaamalla `SEND`-painiketta.



![Image](assets/fr/038.webp)



Jos kelvollinen reitti löytyy, ensimmäisen Lightning-maksun pitäisi onnistua.



![Image](assets/fr/039.webp)



Jos tarkastelemme sitten likviditeetin jakautumista kanavassa, huomaamme, että vertaisvertaisellani on nyt 5 002 sats omalla puolellaan. Tämä vastaa äsken suorittamani maksun 5 000 sats:ää, jonka hän ohjasi vastaanottajan solmuun. Ylimääräiset 2 sats edustavat maksamiani reititysmaksuja, koska vastaanottaja sai täsmälleen 5 000 sats.



![Image](assets/fr/040.webp)



Maksujen luotettavuuden parantamiseksi on luonnollisesti avattava muita kanavia. Tatetteistamme riippuen meidän on myös löydettävä keino, jolla saamme saataville saapuvaa likviditeettiä, jotta temme vastaanottaa maksuja Lightningilla. Tämä on seuraavan jakson aiheena.



# Lightning-solmun hallinta


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Määritä solmun operaattorin profiili


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nyt kun Lightning-solmusi on toiminnassa, seuraava vaihe on määritellä kauppiasprofiilisi. Tämä on tärkeä valinta, sillä se määrittää kanavan avausstrategian, suosimasi vertaisryhmätyypin ja tavan, jolla hallitset likviditeettiä.



Lightningin kohdalla tarvitaan likviditeettiä oikeaan suuntaan, jotta tämä toimisi. Lähtevä likviditeetti vastaa maksukykyäsi (sats käytettävissäsi kanavapuolellasi). Saapuva likviditeetti vastaa vastaanottokykyäsi (sats käytettävissä vertaisverkon puolella). Toisin sanoen profiilisi tiivistyy yksinkertaiseen kysymykseen: lähtevätkö sats:t suurimman osan ajasta solmusta vai tulevatko ne sinne?



### Kuluttaja



Tämä on käyttäjien suuren enemmistön profiili. Käytät solmua Lightning-maksujen tekemiseen: tavaroiden ja palveluiden ostamiseen, laskujen maksamiseen, tippien lähettämiseen - lyhyesti sanottuna Lightningin käyttämiseen nopeana maksuvälineenä. Toisaalta saat Lightningista vähän tai vain marginaalisesti, esimerkiksi muutamia lahjoituksia, ystävien välisiä palautuksia tai muutamia mikromaksuja.



Tätä profiilia on helpoin hallita, koska tärkein tarpeesi on pystyä maksamaan. Käytännössä tämä tarkoittaa, että tarvitset lähtevää maksuvalmiutta. Kun olet avannut yhden tai useamman oikein mitoitetun kanavan vakaisiin, hyvin verkottuneisiin solmuihin, lähtevät maksut siirtävät likviditeettiä mekaanisesti kanavien toiselle puolelle. Juuri tämä liike luo luonnollisesti kohtuullisen määrän tulevaa likviditeettiä. Näin ollen, vaikka et haluaisikaan vastaanottaa säännöllisesti, tet silti vastaanottaa aika ajoin ilman monimutkaisen strategian toteuttamista. Sinun ei siis tarvitse huolehtia saapuvasta likviditeetistäsi.



Tällä LNP202-kurssilla keskitymme tähän "kuluttaja"-solmun operaattoriprofiiliin, sillä se vastaa lähes kaikkia Lightningin Bitcoin-käyttäjiä.



### Jälleenmyyjä



Kauppias on tavallaan kuluttajan vastakohta. Tässä tapauksessa päätatetteena ei ole maksaminen vaan periminen. Yritys, palveluntarjoaja, verkkokauppa tai myyntipiste, joka hyväksyy Lightningin, vastaanottaa paljon saapuvia maksuja ja suorittaa suhteellisen vähän lähteviä maksuja tästä solmusta.



Tämä profiili on vaativampi, sillä salamamaksun epääminen saattaa merkitä menetettyä myyntiä. Ensisijainen tatete on siis saapuva likviditeetti. Jos solmussasi ei ole tarpeeksi saapuvaa likviditeettiä, asiakkaasi näkevät maksunsa epäonnistuvan, vaikka heillä olisi varoja, yksinkertaisesti siksi, ettei likviditeettiä saada sinne oikeaan suuntaan.



Suurin haaste kauppiaalle tulee myös kanavien luonnollisesta kehityksestä. Jos teet vain vastaanottamista, kanavasi täyttyvät vähitellen sinun puoleltasi. Tarvitset siis mekanismeja, joilla ylläpidät ja uudistat saapuvaa likviditeettiäsi.



On kuitenkin olemassa yksinkertaisempi tapaus: sekamuotoinen kuluttaja- ja kauppiasprofiili. Jos keräät varoja Lightningin kautta, mutta myös kulutat Lightningin kautta (liiketoimintakulut, maksut tavarantoimittajille tai jopa henkilökohtaiset kulut), lähtevät maksut luovat luonnollisesti uudelleen saapuvat maksut. Hallinnoinnista tulee sujuvampaa, koska virrat kompensoivat toisiaan, ja sinun ei tarvitse turvautua keinotekoisiin mekanismeihin, jotka on suunniteltu pelkästään saapuvan maksuvalmiuden palauttamiseksi.



### Reititin



Reititin on tietty profiili. Se ei käytä omaa Lightning-solmua maksamiseen tai keräämiseen, vaan muiden maksujen reitittämiseen ja maksujen keräämiseen. Tatetteena on olla hyödyllinen, luotettava ja taloudellisesti kilpailukykyinen reititin Lightning-gráfin sisällä.



Rehellisesti sanottuna Lightningin reitittimenä toimiminen on monimutkaisempaa kuin miltä se näyttää, ja kannattavuutta on vaikea saavuttaa. Ensinnäkin kanavien avaaminen ja sulkeminen on kallista onchain-kustannuksina. Jotta tet reitittää tehokkaasti, sinun on usein mukautettava topologiaasi, testattava, suljettava heikosti toimivia kanavia, avattava uusia ja tasapainotettava likviditeettiäsi säännöllisesti. Toiseksi kilpailu on kovaa: suuret, vakiintuneet solmut kaappaavat luonnollisesti suuren osan liikenteestä, ja on vaikea saada jalansijaa sitomatta merkittävää pääomaa hyvin suuriin kanaviin.



Myös toiminnalliset vaatimukset ovat korkeat. Reitityssolmun on oltava erittäin vakaa, sitä on valvottava, siitä on tehtävä asianmukaiset varmuuskopiot ja sitä on hallinnoitava tiukasti. Sinun on seurattava kanavan suorituskykyä, mukautettava maksupolitiikkaa, ylläpidettävä tasapainoista likviditeettiä, hallittava vertaisia ja ratkaistava nopeasti tekniset ongelmat. Tämäntasoinen osallistuminen te olla kiinnostavaa teknisenä harrastuksena tai panoksena infrastruktuuriin, mutta jos tatetteenasi on yksinkertaisesti käyttää Lightningia suvereenisti, reititykseen ryhtyminen rahan ansaitsemiseksi on harten relevanttia. Siksi tämä LNP202-kurssi ei käsittele tätä profiilia perusteellisesti.



### Aseta itsesi selkeästi asemaan ennen kuin menet pidemmälle



Jos sovit kuluttajan profiiliin, etusijalla on luotettava maksaminen ja yksinkertainen hallinnointi. Jos olet kauppias, etusijalla on epäonnistumattoman maksun saaminen, mikä edellyttää sisäänpäin suuntautuvaa likviditeetin hankintastrategiaa. Jos harkitset reititystä, sinun on lähestyttävä sitä vaativana, taloudellisesti epävarmana ja aikaa vievänä toimintana.



Tämän profiilin määrittäminen nyt auttaa sinua välttämään klassisen sudenkuopan: sovellat kauppiaalle tai reitittimelle suunniteltua kanavastrategiaa, vaikka olet vain käyttäjä, joka haluaa maksaa.



## Lightning-solmujen hallinnan käyttäminen


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Tämän LNP202-koulutuskurssin edellisessä osassa käytimme Umbrel:n `Lightning Node` -sovelluksen perusliittymää. Tämä käyttöliittymä riittää olennaisiin toimintoihin (saldojen tarkistaminen, käteisvarojen jakelun tarkastelu, kanavien avaaminen ja sulkeminen), mutta se on tarkoituksellisesti hyvin yksinkertaistettu. Tämä yksinkertaisuus rajoittaa käytettävissä olevia vaihtoehtoja eikä anna pääsyä moniin LND-solmun kehittyneisiin ominaisuuksiin. Tästä syystä käytämme nyt toista, kattavampaa Lightning-solmun hallintaohjelmistoa.



Tämä lisäohjelmisto on vain täydentävä hallintaliittymä solmulle. Tämä tarkoittaa, että tet jatkaa `Lightning Node` -käyttöliittymän käyttöä rinnakkain ja halutessasi jopa käyttää useita eri käyttöliittymiä. Nämä ovat yksinkertaisesti eri tapoja toimia vuorovaikutuksessa saman Lightning-solmun kanssa.



Tunnetuimpia ohjelmistoja ovat mm:




- [Alby Hub] (https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub] (https://thunderhub.io/).



Kaikki kolme ovat hyviä ratkaisuja. Voit halutessasi testata kaikkia kolmea solmun kanssa, ennen kuin valitset niistä sinulle parhaiten sopivan. Itse käytän ThunderHub:a tottumuksesta ja siksi, että se vaikuttaa täydellisemmältä kuin muut. Esittelen tämän työkalun tällä kurssilla, mutta tet myös valita jommankumman kahdesta muusta vaihtoehdosta. Kummallekin ohjelmalle on oma opetusohjelma Plan ₿ Academy:ssä.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Asenna ThunderHub



Nämä ohjelmat tedaan asentaa helposti Umbrel App Storesta. Kuten sanoin, käytämme tässä ThunderHub:tä, mutta jos haluat myöhemmin testata toista ohjelmaa, menettely on samanlainen.



![Image](assets/fr/041.webp)



Umbrel antaa sinulle oletussalasanan ThunderHub:n käyttöä varten. Kopioi se: tarvitset sitä heti. Muista myös tallentaa se salasanahallintaasi, sillä sitä kysytään aina, kun avaat ohjelmiston.



![Image](assets/fr/042.webp)



Napsauta `Login` ja liitä sitten Umbrel:n antama salasana kirjautuaksesi sisään.



![Image](assets/fr/043.webp)



Tämän jälkeen siirryt ThunderHub:n etusivulle, jossa näkyvät Lightning-solmun tärkeimmät tiedot.



![Image](assets/fr/044.webp)



Aluksi suosittelen, että otat käyttöön kaksitekijätodennuksen (2FA). Napsauta asetuksissa yksinkertaisesti `Enable` (Ota käyttöön) -kohtaa `Enable 2FA` (Ota 2FA käyttöön) ja noudata sitten tavanomaista prosessia.



![Image](assets/fr/045.webp)



### Käytä ThunderHub



ThunderHub on suhteellisen helppo oppia. Kaikkiin valikoihin pääsee käyttöliittymän vasemmasta sarakkeesta. Yhteenvetona kerrotaan, mitä kukin valikko tekee:




- kotisivu: solmun yleiskatsaus, saldot ja pikatoiminnot;
- kojelauta: mukautettava kojelauta, jossa on widgettejä ja mittareita;
- peers: tarkastella ja hallita yhteyksiä muihin Lightning-solmuihin;
- kanavat": kanavien täydellinen hallinta (likviditeetti, maksut, sulkeminen jne.);
- rebalance": väline kanavien tasapainottamiseen kiertomaksujen avulla;
- maksutapahtumat: lähetettyjen ja vastaanotettujen Lightning-maksujen historia;
- eteenpäin`: reititystilastot ja kustannukset generated solmun mukaan;
- `Chain`: Bitcoin onchain-salkku (UTXO:t ja transaktiot);
- gW-201-integraatio valvontaa ja varmuuskopiointia varten;
- `Tools`: kehittyneet työkalut (varmuuskopiot, raportit, makaronit, allekirjoitukset jne.);
- vaihtoa: Boltz:n kautta;
- `Stats`: Lightning-solmun yleiset tilastot ja suorituskyky.



Näiden toimintojen avulla sinulla on kaikki tarvittavat työkalut Lightning-solmun tehokkaaseen hallintaan. Kaikkia vaihtoehtoja ei ole välttämätöntä hallita yksityiskohtaisesti heti: tutustumme niihin vähitellen tämän kurssin aikana. Jos kuitenkin haluat tutustua ohjelmistoon syvällisemmin, tutustu ThunderHub-oppaaseen:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Valikko, josta olemme eniten kiinnostuneita, on `Kanavat`. Se tarjoaa yksityiskohtaisen näkymän kaikista solmusi kanavista ja niiden likviditeettijakaumasta. Näet erityisesti, mitkä kanavat ovat atenna kohdassa `Open`, mitkä odottavat avaamista tai sulkemista kohdassa `Pending` ja mitkä ovat jo suljettu kohdassa `Closed`.



![Image](assets/fr/047.webp)



Tietyn kanavan osalta tet napsauttaa vertaisverkon nimeä tai kanavatunnusta avataksesi sen Amboss-sivun ja saadaksesi lisätietoja. Voit myös napsauttaa kynäkuvaketta muuttaaksesi kanavan parametreja, mukaan lukien kyseiseen kanavaan sovellettava maksukäytäntö, jos solmusi reitittää maksut vertaisverkon solmuun.



![Image](assets/fr/048.webp)



Jos käytät Lightning-solmua pääasiassa "kuluttajana", sinun ei tarvitse muuttaa näitä maksuja: tet säilyttää oletusarvot. Toisaalta, jos haluat ymmärtää paremmin, miten reititysmaksut toimivat Lightningissa, suosittelen LNP 201 -koulutusta ja erityisesti lukua 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Voit käynnistää kanavan sulkemisen napsauttamalla pientä ristiä vertaisohjelman vieressä. Jos huomaat esimerkiksi, että vertaisohjelma on säännöllisesti toimimaton, te olla aiheellista sulkea tämä kanava, jotta tet kohdentaa pääomasi uudelleen luotettavampaan vertaisohjelmaan.



Sitten sinulla on kaksi vaihtoehtoa. Ensimmäinen ja aina suositeltavin vaihtoehto on yhteistyöhön perustuva päättäminen. Vahvistamalla tämän toimenpiteen solmusi pyytää vertaisvertaistasi sulkemaan kanavan yhdessä. Jos hän hyväksyy sen, tet lähettää ketjun sulkemistapahtuman ja saada takaisin osuutesi varoista. Tämän menetelmän etuina on, että valitset tapahtuman onchain-maksut, jolloin vältyt turhilta kustannuksilta, ja että varat saadaan takaisin nopeammin, ilman aikalukkoa.



![Image](assets/fr/049.webp)



Toinen vaihtoehto on pakkosulkeminen. Tässä tapauksessa et pyydä vertaisen suostumusta, vaan lähetät suoraan viimeisen hallussasi olevan commitment transaction:n. En suosittele tätä menetelmää, ellei se ole viimeinen keino, esimerkiksi jos vastapuoli kieltäytyy järjestelmällisesti yhteistyöhön perustuvasta sulkemisesta tai ei enää vastaa. Pakkosulkemisessa on kaksi suurta haittaa: maksut ovat usein hyvin korkeita, koska ne on asetettu etukäteen ketjumaksuissa tapahtuvan nousun ennakoimiseksi, ja varojen takaisin saaminen viivästyy, koska ne on estetty aikalukolla. 



![Image](assets/fr/050.webp)



Jos haluat lopuksi avata uuden kanavan, siirry `Home`-valikkoon ja napsauta `Open a Channel` (Avaa kanava) kohdassa `Liquidity`. Tämän jälkeen tet syöttää valitun solmun ID:n, kanavan kapasiteetin, halutun Lightning-reititysmaksun ja avaustapahtuman onchain-maksun.



![Image](assets/fr/051.webp)



Nämä ovat tärkeimmät toimenpiteet, jotka sinun on tehtävä ThunderHub:lle. Tutustumme muihin ominaisuuksiin tämän LNP202-kurssin edetessä.



## Saapuvan likviditeetin hankkiminen


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Kuten huomaat, maksuvalmiuden hankkiminen Lightning-maksujen suorittamiseen ei ole erityisen monimutkaista. Avaa vain omasta aloitteestasi kanavia muihin solmuihin ja aloita sats:n lähettäminen. Toisaalta saapuvan likviditeetin hankkiminen maksujen vastaanottamiseksi Lightningissa on monimutkaisempaa, sillä sinun on joko avattava kanavia muille solmuille tai siirrettävä likviditeettiä itse tekemällä maksuja.



Jos omaksut "kuluttaja"-profiilin, sinun ei yleensä tarvitse olla huolissasi tulevasta likviditeetistä. Lightning-solmun käyttösi on pääasiassa maksamiseen keskittyvää, ei niinkään käteisrahan vastaanottamiseen. Kun teet vain muutaman Lightning-maksun, luot luonnollisesti ajan mittaan tulevaa likviditeettiä.



Toisaalta, jos sinulla on "kauppias"-profiili, tilanne on päinvastainen: keräät pääasiassa maksuja ja teet vain vähän maksuja. Et siis te luottaa pelkästään omien maksujesi varaan saapuvan maksuvalmiuden suhteen. Sen vuoksi muiden Lightning-solmujen on avattava kanavia sinun maksukanavillesi. Mutta miten tämä tedaan toteuttaa? Miten saat muut toimijat sitomaan pääomaa puolestasi? Juuri sitä tutkimme tässä luvussa.



### Sisäänpäin suuntautuvan likviditeetin ostaminen



Kuten arvata saattaa, tehokkain tapa saada joku toimimaan on maksaa hänelle. Lightning-solmuun tulevan likviditeetin osalta periaate on täsmälleen sama. Yksinkertaisin tapa saada kanavia solmuun on maksaa palvelusta ja siihen liittyvästä pääoman sitomisesta.



Jos olet yritys tai vähittäismyyjä, tämä lähestymistapa tarkoittaa, että saat nopeasti luotettavia kanavia, joiden kautta tet kerätä maksuja asiakkailtasi ilman kitkaa.



Sisäänpäin suuntautuvan likviditeetin ostamiseen on monia tapoja. Itse käytän ja suosittelen Amboss:n [Magma](https://magma.amboss.tech/) -alustaa. Se on erittäin helppokäyttöinen, kanavan avaaminen on nopeaa ja hinnat ovat yleensä kohtuullisia. Magma toimii kuin markkinapaikka, jossa on tekijöitä ja ottajia, mutta versio 2 on yksinkertaistanut kokemusta huomattavasti: luo vain pyyntö, maksa hinta Lightningin kautta, ja Magma vastaa automaattisesti parhaaseen saatavilla olevaan tarjoukseen. Kuuden onchain-vahvistuksen jälkeen kanavasi saapuvan likviditeetin kanssa on toiminnassa. Näin se toimii:



Mene [Magman verkkosivuille] (https://magma.amboss.tech/buy), osioon "Osta kanavia".



![Image](assets/fr/052.webp)



Voit halutessasi luoda tilin, jolla tet seurata ostoksiasi, mutta se ei ole pakollista. Jos et luo tiliä, Magma antaa sinulle vain istuntotunnuksen, jonka avulla tet hakea ostoksesi myöhemmin.



Kun olet sivustolla, täytä likviditeetin ostamiseen tarvittavat tiedot. Valitse `One Time`, jos haluat tehdä kertaluonteisen oston, ja anna sitten summa, jonka olet valmis maksamaan saapuvasta likviditeetistä. Mitä korkeampi summa maksetaan, sitä suurempi on solmullesi avatun kanavan kapasiteetti. Alla näkyy arvio kanavan kapasiteetista: tämä on likimääräinen arvio, sillä lopullinen summa riippuu Magman löytämästä parhaasta tarjouksesta, joka on joskus korkeampi ja joskus matalampi.



![Image](assets/fr/053.webp)



Syötä sitten solmun tunnus. Löydät sen esimerkiksi Umbrel:n "Lightning Node" -sovelluksen valikosta "Node ID".



![Image](assets/fr/054.webp)



Kun kaikki tiedot on täytetty, napsauta `Review & open order` -painiketta.



![Image](assets/fr/055.webp)



Jos et ole luonut tiliä, Magma antaa sinulle istuntoavaimen ja varmuuskopiotiedoston. Säilytä nämä kaksi tietoa turvallisessa paikassa, sillä niiden avulla tet hakea tilauksen myöhemmin tai seurata sen tilaa ongelmatilanteessa. Kun olet tallentanut tiedoston, napsauta `Pay with Lightning`-painiketta.



![Image](assets/fr/056.webp)



Magma lähettää sitten generates Lightning-laskun valitsemastasi summasta. Sinun on maksettava se. Jos sinulla on jo kanavia Lightning-solmussasi, tet maksaa suoraan siitä tai käyttää toista ulkoista Lightning wallet -palvelua.



![Image](assets/fr/057.webp)



Kun maksu on suoritettu, maksutapahtuma näkyy Magma-käyttöliittymässä käsitellyksi.



![Image](assets/fr/058.webp)



Muutaman minuutin kuluttua pyyntö käsitellään: kanava sats:llä avataan Lightning-solmuun. Kun avaustapahtuma on vahvistettu ketjussa, saat käyttöösi vastaavan saapuvan likviditeetin.



![Image](assets/fr/059.webp)



Magma on myös integroitu suoraan ThunderHub:een. Vieritä `Home`-välilehdellä alaspäin `Liquidity`-osioon ja napsauta `Buy Inbound Liquidity`. Sinun tarvitsee vain syöttää haluamasi määrä ja vahvistaa. Sinun ei tarvitse maksaa laskuja manuaalisesti, sillä ThunderHub huolehtii automaattisesti maksusta solmusta.



![Image](assets/fr/060.webp)



Jos olet kauppias, tämäntyyppinen palvelu on erityisen sopiva, sillä sen avulla tet saada nopeasti suuren määrän maksuvalmiutta luotettavista solmuista, mikä takaa, että asiakkaasi pystyvät maksamaan sinulle ongelmitta. Toisaalta, jos olet yksityishenkilö tai jos et halua maksaa saapuvasta likviditeetistä, tarjolla on myös ilmaisia ratkaisuja. Katsotaanpa.



### Yhteistyössä tuleva likviditeetti



Jos et ole kauppias, mutta tarvitset silti jonkin verran tulevaa likviditeettiä (esimerkiksi solmun käynnistysvaiheessa, kun odotat maksuja), sinun ei välttämättä tarvitse maksaa siitä. Yksi suosikkiratkaisuistani on tehdä yhteistyötä muiden solmujen ylläpitäjien kanssa, jotka myös tarvitsevat tulevaa likviditeettiä, ja avata Lightning-kanavia toisilleen. Tällä taten kanavan avaaminen tuo sinulle lähtevää likviditeettiä ja tarjoaa samalla sinulle saapuvaa likviditeettiä ilmaiseksi (modulo onchain-maksut avaamisesta).



Voit tietysti sopia tästä suoraan muiden bitcoin-asiakkaiden kanssa. On kuitenkin olemassa foorumi, joka on omistettu tämäntyyppiselle ympäripyöreälle avautumiselle: [Lightning Network +](https://lightningnetwork.plus/). Periaatteena ei ole avata kahta kanavaa samojen ihmisten välillä, vaan järjestää ympäripyöreitä avauksia, joissa on vähintään kolme osallistujaa tai jopa enemmän.



Otetaan esimerkki, jotta ymmärretään, miten Lightning Network+ toimii:




- Solmun operaattori nimeltä "A" julkaisee ilmoituksen, jossa hän ilmoittaa haluavansa avata 1 miljoonan sats-kanavan kahden muun henkilön kanssa;
- Ilmoitus pysyy aktiivisena, kunnes uusia osallistujia lisätään;
- Myöhemmin kaksi operaattoria, `B` ja `C`, liittyvät solmun `A` ilmoitukseen. Kolmio on nyt valmis, ja avautumisvaihe te alkaa.
- Solmu `A` avaa kanavan solmuun `B`;
- Solmu "B" avaa kanavan solmuun "C";
- Solmu C avaa kanavan solmuun A.



Operaation lopussa kullakin solmulla on 1 miljoona sats lähtevää likviditeettiä ja 1 miljoona sats tulevaa likviditeettiä. Tätä järjestelmää tedaan laajentaa neljään tai viiteen osallistujaan.



Mikään tekninen mekanismi ei tietenkään takaa, että osallistuja todella avaa kanavan, jonka hän on sitoutunut luomaan. Siksi foorumi on perustanut mainejärjestelmän, joka perustuu positiivisiin arvosteluihin, kun toimijat täyttävät sitoumuksensa. Ja pahimmassa tapauksessa, jos törmäät henkilöön, joka ei tee yhteistyötä, et ole menettänyt rahaa: olet vain menettänyt mahdollisuuden tulevaan likviditeettiin.



Tämä ratkaisu sopii erityisen hyvin "kuluttaja"-profiiliin, sillä sen avulla tet saada maksutta tulevaa likviditeettiä ja yhdistää solmusi muihin pieniin operaattoreihin. Toisaalta jos olet kauppias, tämä lähestymistapa ei yleensä ole relevantti: jokainen saapuvan likviditeetin satsi edellyttää lähtevän likviditeetin satsipaikan estämistä, ja suuret saapuvan likviditeetin tarpeesi merkitsisivät silloin liian suuren pääoman sitomista.



Lightning Network+:n käyttämiseksi sinulla on kaksi vaihtoehtoa: tet joko käyttää Umbrel:een integroitua sovellusta tai käyttää perinteistä verkkosivustoa ja luoda tilin kirjautumalla sisään solmusta. Suosittelen jälkimmäistä vaihtoehtoa, sillä integroitu sovellus ei tarjoa kaikkia käytettävissä olevia toimintoja.



Mene [Lightning Network +](https://lightningnetwork.plus/) -sivustolle ja napsauta käyttöliittymän oikeassa yläkulmassa olevaa `Login`-painiketta.



![Image](assets/fr/061.webp)



Jotta tet todentaa itsesi, sinun on allekirjoitettava toimitettu viesti Lightning-solmun yksityisellä avaimella. ThunderHub:n avulla tämä toimenpide on hyvin yksinkertainen. Aloita kopioimalla LN+:n näyttämä viesti.



![Image](assets/fr/062.webp)



Siirry ThunderHub:ssa välilehdelle `Tools` ja napsauta sitten `Sign`-painiketta `Messages`-osiossa.



![Image](assets/fr/063.webp)



Liitä LN+:n antama todennusviesti ja napsauta sitten "Allekirjoita".



![Image](assets/fr/064.webp)



ThunderHub allekirjoittaa tämän viestin solmun yksityisellä avaimella. Kopioi generated:n allekirjoitus.



![Image](assets/fr/065.webp)



Liitä tämä allekirjoitus LN+-sivuston vastaavaan kenttään ja napsauta sitten "Kirjaudu sisään".



![Image](assets/fr/066.webp)



Olet nyt yhteydessä LN+:aan Lightning-solmun kanssa. Tämän prosessin avulla LN+ te varmistaa, että olet sen solmun laillinen omistaja, jonka olet lunastanut heidän alustalleen.



![Image](assets/fr/067.webp)



Voit halutessasi muokata LN+-profiiliasi, esimerkiksi lisäämällä lyhyen elämäkerran.



Osallistuaksesi ensimmäiseen kiertävän kanavan avaamiseen, siirry käyttöliittymän yläosassa olevaan `Swaps`-valikkoon. Täältä löydät kaikki tällä hetkellä käytettävissä olevat swapit solmusi ominaisuuksista riippuen.



![Image](assets/fr/068.webp)



Jos haluat liittyä olemassa olevaan vaihtotarjoukseen, klikkaa sitä ja rekisteröidy. LN+:ssa swap-tarjouksen tekijä te kuitenkin asettaa osallistujille tiettyjä ehtoja, kuten kanavien vähimmäismäärän tai solmujen kokonaiskapasiteetin vähimmäismäärän. Siksi on mahdollista, että varsinkin alkuvaiheessa solmusi on käytettävissä vain vähän tarjouksia. Minun tapauksessani solmuni ei ollut saatavilla yhtään tarjousta, vaikka muutama kanava oli jo atenna. Niinpä loin oman swapin, ja tet tehdä samoin, jos olet samassa tilanteessa.



Napsauta `Start Liquidity Swap` ja syötä sitten tarjousparametrit:




- Valitse osallistujien kokonaismäärä (3, 4 tai 5);
- Ilmoita avattavien kanavien määrä (varmista, että sinulla on vähintään tämä määrä onchain wallet:ssä);
- Määritä kanavan aukioloaika. Tämä on ajanjakso, jonka aikana osallistujat sopivat, etteivät sulje niitä;
- Oikealla puolella tet asettaa rajoituksia osallistujille: kanavien vähimmäismäärä, kokonaiskapasiteetin vähimmäismäärä ja hyväksytyn yhteyden tyyppi.



Kun kaikki parametrit on asetettu, napsauta painiketta "Start Liquidity Swap".



![Image](assets/fr/069.webp)



Vaihtotarjouksesi on nyt luotu. Nyt sinun tarvitsee vain odottaa, että muut solmujen ylläpitäjät ilmoittautuvat. Jos ehtosi eivät ole liian rajoittavat, tämän ei pitäisi kestää liian kauan. Muista seurata vaihtosi tilaa seuraavien tuntien tai päivien aikana.



![Image](assets/fr/070.webp)



Kaikki vaihtopaikat on varattu: nyt siirrytään kanavien avausvaiheeseen. Kukin osallistuja näkee LN+ -käyttöliittymästä, mihin solmuun hänen on avattava salamakanava.



![Image](assets/fr/084.webp)



Avaa kanava omalla puolellasi LN+:n antaman solmutunnuksen avulla ja ilmoitettua määrää noudattaen. Kuten olemme nähneet aiemmissa luvuissa, tet tehdä tämän joko ThunderHub:n kautta, toisen Lightning-solmunhallinnan avulla tai suoraan Lightning-solmun perussovellusliittymästä.



![Image](assets/fr/085.webp)



Kun avaus on käynnistetty, näet sen odottavat kanavat -osiossa. Minun tapauksessani se on kanava, jossa on solmu `Plebian_fr`.



![Image](assets/fr/086.webp)



Tämän jälkeen tet palata LN+:aan vahvistaaksesi, että olet aloittanut kanavan avaamisen. Napsauta vain `Kanavan avaaminen aloitettu`-painiketta.



![Image](assets/fr/087.webp)



Kun kaikki muutkin osallistujat ovat avanneet kanavan, johon he ovat sitoutuneet, muista jättää heille positiivinen arvostelu.



![Image](assets/fr/088.webp)



Vaikeuksien tai viivästysten ilmetessä tet ottaa yhteyttä vertaisarvioijiin suoraan sivun alareunassa olevan kommenttiosion kautta.



![Image](assets/fr/089.webp)



Jotkut osallistujat saattavat haluta tasapainottaa kiertokanavia alusta alkaen maksamalla itselleen maksun. Näin varmistetaan käteisvarojen tasapainoinen jakautuminen kussakin kanavassa. Jos olet "kuluttaja"-profiilissa, tämä ei ole välttämätöntä, mutta tet halutessasi joko tehdä tämän tasapainottamisen itse tai asettaa kanavamaksusi väliaikaisesti nollaan, jotta se olisi helpompaa vertaisosaajalle, joka haluaa tehdä sen. Joskus kukaan ei halua tehdä sitä.



![Image](assets/fr/090.webp)




# Lightning-solmun potentiaalin vapauttaminen käyttöön


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Liitä wallet mobiililaitteeseen Tailscale:n kautta


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Siinä kaikki, sinulla on nyt hyvin yhdistetty Lightning-solmu, jossa on sekä saapuvaa että lähtevää likviditeettiä. Olet siis valmis käyttämään Lightning-solmua tosielämässä. Tähän asti olemme aina käyttäneet rajapintoja suoraan Umbrel:ssä, joko `Lightning Node`-sovellusta tai `ThunderHub`-rajapintaa. Nämä työkalut toimivat maksujen lähettämiseen ja vastaanottamiseen, mutta niitä ei selvästikään ole optimoitu jokapäiväisiin Lightning-maksuihin. Käyttöliittymä on suunniteltu käytettäväksi tietokoneella, mikä on epäkäytännöllistä älypuhelimessa, ja se vaatii myös yhteyden samaan verkkoon toimiakseen kunnolla (vaikka teknisesti on mahdollista muodostaa yhteys etänä Torin kautta).



Käytännössä bitcoin-käyttäjinä etsimme klassista Lightning wallet -käyttöliittymää älypuhelimessa: mahdollisuutta skannata laskuja QR-koodin avulla ja yksinkertaista käyttöliittymää sats -maksujen maksamiseen ja lunastamiseen. Juuri tämän toteutamme tässä ja seuraavassa luvussa. Yleisenä ajatuksena on, että älypuhelimessa on mobiili Lightning wallet -sovellus, jota te käyttää mistä tahansa (ei vain lähiverkosta), mutta joka tukeutuu taustalla omaan Lightning-solmuun maksujen lähettämiseksi ja vastaanottamiseksi.



### Millaisia ratkaisuja on olemassa mobiilin asiakkaan yhdistämiseen?



Nykyään on olemassa useita tapoja tehdä tämä sekä mobiilisovelluksen että solmun ja sovelluksen välisen yhteyden tyypin osalta. Kolme tärkeintä yhteystapaa ovat:




- ***Tor***:n kautta;
- vPN:n kautta ***Tailscale***;
- ***Nostr Wallet Connect*** kautta.



Muutama vuosi sitten käytin ***Tor***-yhteyttä, mutta lopetin sen nopeasti: epäonnistumisten määrä ja tiedonsiirtoviiveet olivat aivan liian suuria. Teoriassa se toimii, mutta käytännössä käyttökokemus oli katastrofaalinen. Neutesin siksi olemaan käyttämättä tätä lähestymistapaa.



Vaihtoehto, jonka valitsin, oli käyttää ***Tailscale*** VPN:ää, jolla varmistettiin mobiilisovelluksen ja solmun välinen viestintä. Tämä ratkaisu toimii erittäin hyvin: jopa matkaviestinverkoissa, joissa on alhainen läpäisykyky, maksuni menevät aina läpi ongelmitta. Esittelen tämän menetelmän ensimmäisenä tässä luvussa Zeus-sovelluksen avulla.



Seuraavassa luvussa tarkastelemme toista, uudempaa ratkaisua, joka toimii myös erittäin hyvin: ***Nostr Wallet Connect***. Tällä kertaa käytämme Alby Go-sovellusta esitellessämme sinulle vaihtoehdon, vaikka Zeus on halutessasi yhteensopiva myös NWC:n kanssa.



### Tailscale:n asentaminen ja konfigurointi



Tätä ensimmäistä menetelmää varten tarvitsemme Tailscale:n. Kyseessä on WireGuard:een perustuva VPN-ratkaisu, jonka avulla tet yhdistää turvallisesti eri puolilla Internetiä olevia laitteita ja hallita automaattisesti salausta, todennusta ja NAT-tunnistusta. Yksinkertaisesti sanottuna se on kuin kaikki laitteesi olisivat yhteydessä samaan lähiverkkoon reitittimesi kanssa, vaikka ne tesivat olla missä tahansa Internetissä.



Jos haluat käyttää sitä, luo ensin tili. Siirry Tailscale-sivustolle ja napsauta sitten `Get Started`-painiketta.



![Image](assets/fr/071.webp)



Valitse sitten identiteetin tarjoaja Tailscale-tiliäsi varten. Itse käytin kirjautumiseen yhtä GitHub-tiliäni.



![Image](assets/fr/072.webp)



Kun olet kirjautunut sisään, sinulta kysytään muutamia kysymyksiä käytöstäsi. Vastaa niihin lyhyesti jatkaaksesi.



![Image](assets/fr/073.webp)



Tailscale ehdottaa sitten asiakkaan asentamista koneellesi. Tällä hetkellä emme ole kiinnostuneita tästä: siirry suoraan Umbrel:een ja asenna Tailscale-sovellus App Storesta.



![Image](assets/fr/074.webp)



Kun sovellus avautuu, napsauta "Kirjaudu sisään" ja noudata sitten todennusprosessia samalla menetelmällä kuin tiliä luodessasi.



![Image](assets/fr/075.webp)



Vahvista napsauttamalla `Connect`. Umbrel on nyt yhdistetty VPN-verkkoon.



![Image](assets/fr/076.webp)



Lataa sitten Tailscale-sovellus älypuhelimeesi ja kirjaudu sisään samalla tilillä. Huomaa: Androidissa ei ole mahdollista käyttää kahta VPN:ää samanaikaisesti. Jotta Tailscale toimisi, sinun on poistettava kaikki muut aktiiviset VPN:t käytöstä. Lisäksi aina kun haluat käyttää Lightning-solmua Zeuksen kautta, sinun on aktitetava Tailscale VPN, muuten yhteys ei muodostu.



![Image](assets/fr/077.webp)



Kun Tailscale-sivustossa on nyt vähintään kaksi asiakasta liitetty, tet käyttää hallintakonsolia, jossa on luettelo kaikista verkkoon liitetyistä laitteista ja niiden Tailscale:n IP-osoitteista.



![Image](assets/fr/078.webp)



### Yhdistä Zeus



Asenna Zeus-sovellus puhelimeesi. Kun se avautuu, valitse `Advanced Setup` ja sitten `Create or connect a wallet`.



![Image](assets/fr/079.webp)



Valitse "Wallet-liitäntä"-osiosta "LND (REST)". Kirjoita sitten Umbrel:n Tailscale-osoite, jonka löydät Tailscale-kojelaudalta tai suoraan Umbrel:n Tailscale-sovelluksesta. Kirjoita portiksi `8080`.



![Image](assets/fr/080.webp)



Sitten Zeus pyytää sinua toimittamaan makaroonin. Tämä on valtuutus token, jonka avulla tet määritellä tarkasti sovellukselle (tässä tapauksessa Zeukselle) myönnetyt oikeudet olla vuorovaikutuksessa Lightning-solmusi kanssa. On mahdollista generate makaroonin ThunderHub, `Työkalut`-valikosta, `Leivonta`-alavalikosta, mutta tätä tarkoitusta varten helpoin tapa on hakea se suoraan `Lightning Node`-sovelluksesta.



Napsauta kolmea pientä pistettä käyttöliittymän oikeassa yläkulmassa ja valitse sitten `Connect Wallet`. Valitse `REST (Lähiverkko)`. Tämän jälkeen tet kopioida makaroonin asianmukaisilla oikeuksilla.



![Image](assets/fr/081.webp)



Liitä se Zeuksen vastaavaan kenttään ja napsauta sitten `SAVE WALLET CONFIG`-painiketta.



![Image](assets/fr/082.webp)



Voit nyt käyttää Lightning-solmua Zeus-sovelluksesta. Tämä tarkoittaa, että tet generate-laskuja vastaanottaa maksuja suoraan Lightning-solmussasi älypuhelimestasi ja myös maksaa Lightning-laskuja missä tahansa oletkin.



![Image](assets/fr/083.webp)



Vihje: Tailscale ei rajoitu Lightning-solmun etäkäyttöön. Sen avulla tet käyttää kaikkia Umbrel:n työkaluja muista ohjelmistoista, jopa etänä. Voit esimerkiksi käyttää Umbrel:n Tailscale IP-osoitetta Bitcoin-solmun (Electrs:n tai Fulcrumin kautta) yhdistämiseen Sparrow Wallet:een ilman Torin kautta kulkemista. Näin vältät jälleen kerran Torin hitauden. Asenna vain Tailscale-asiakasohjelma tietokoneellesi ja liitä se verkkoon.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Seuraavassa luvussa tarkastelemme toista, yhtä tehokasta tapaa yhdistää mobiiliasiakas Lightning-solmuun: Nostr Wallet Connect. Käytämme eri sovellusta kuin Zeus (vaikka Zeus on myös yhteensopiva NWC:n kanssa), nimittäin Alby Go:tä.



## Liitä mobiili wallet NWC:n kautta


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Jos Tailscale-yhteys ei vakuuta sinua tai jos kahden VPN:n hallinta tuntuu liian vaivalloiselta, tässä luvussa ehdotetaan toista tapaa käyttää etäyhteyttä käyttävää mobiiliasiakasta sats:n maksamiseen ja vastaanottamiseen Lightning-solmun kautta: ***Nostr Wallet Connect***.



Tässä esimerkissä käytämme Alby Go-mobiilisovellusta, joka on erittäin hyvin suunniteltu ja erityisen helppo oppia. Voit kuitenkin käyttää myös Zeusta tai mitä tahansa muuta NWC-yhteensopivaa mobiilisovellusta. Löydät luettelon yhteensopivista sovelluksista [the `awesome-nwc` GitHub repository](https://github.com/getAlby/awesome-nwc).



### Miten Nostr Wallet Connect toimii?



Nostr Wallet Connect on standardoitu protokolla, jonka avulla sovellus tai verkkosivusto te käynnistää toimintoja etäällä sijaitsevassa Lightning-solmussa ilman suoraa verkkoyhteyttä kyseiseen solmuun (ei API LND paljastettua, ei VPN:ää, ei .onion-palvelua...). NWC määrittelee, miten sovellus muotoilee aikomuksen (esim. `pay_intece`) ja vastaanottaa tuloksen.



Se toimii melko yksinkertaisesti. Aloitat istunnon skannaamalla QR-koodin tai syvälinkin `nostr+walletconnect:` kautta. Tämä merkkijono sisältää istunnon parametrit ja valtuutussalaisuuden. Kun sovellus haluaa maksaa, se sarjallistaa pyynnön, salaa sen ja julkaisee sen tapahtumana Nostr-releessä. Solmu lukee tapahtuman releessä, purkaa sen salauksen, tarkistaa, että tekijä on valtuutettu tähän istuntoon, suorittaa maksun ja palauttaa sitten salatun vastauksen (onnistunut esikuva tai virhe). Relay toimii vain kuljetuksen välittäjänä: se ei te lukea sisältöä, mutta se te tarkkailla pyyntöjen ajoitusta ja tiheyttä.



Tailscale:n tai Torin kautta muodostettavaan yhteyteen verrattuna NWC:n tärkein etu on se, että solmusi ei ole suoraan saavutettavissa ulkopuolelta. Tämä yksinkertaistaa huomattavasti mobiilikäyttöä: solmusi ei tarvitse hyväksyä saapuvia yhteyksiä, sen on vain pystyttävä kommunikoimaan releen kanssa. Toisaalta otat käyttöön toiminnallisen riippuvuuden Nostr-välittäjistä: jos ne eivät ole käytettävissä, käyttökokemus heikkenee. Lisäksi, vaikka viestit on salattu, rele te havaita tietyn tason toiminnan metatietoja.



Turvallisuusmallien ero on myös tärkeä. Tailscale:n tai Torin avulla saat suoran pääsyn solmuun (API:n tai LND:n kautta), joka on suojattu erittäin arkaluonteisilla salaisuuksilla. Tämä on tehokasta, koska tet hallita kaikkea, mutta se on myös alemman tason hyökkäyspinta. NWC:n avulla pääsy on sovelluksellisempi: delegoit istunnon token, joka valtuuttaa vain tietyt toiminnot.



### Asenna Alby Hub Lightning-solmuun



Umbrel App Storessa oli aiemmin sovellus, joka oli tarkoitettu erityisesti NWC-yhteyksiä varten, mutta valitettavasti sitä ei enää ole saatavilla. Sinun on nyt käytettävä Alby Hub:ää tämäntyyppisten yhteyksien muodostamiseen. Aloita asentamalla Alby Hub-sovellus suoraan kaupasta.



![Image](assets/fr/091.webp)



Kun avaat ohjelman, ohita aloitusnäytöt ja napsauta sitten `Get Started (LND)`-painiketta. On tärkeää tarkistaa, että suluissa lukee `LND` eikä `LDK`. Jos `LND` ilmestyy näkyviin, tämä tarkoittaa, että Alby Hub on tunnistanut olemassa olevan Lightning-solmusi oikein ja konfiguroi itsensä sen käyttöliittymäksi. Jos taas `LDK` näkyy, se tarkoittaa, että Alby Hub ei ole havainnut solmua ja aikoo luoda uuden solmun, mikä ei ole tarkoitus.



![Image](assets/fr/092.webp)



Tämän jälkeen sinua pyydetään perustamaan Alby-tili. NWC:hen rajoittuvassa käytössä tämä ei ole välttämätöntä, mutta saatat haluta tehdä niin, jos haluat hyödyntää Alby:n erityispalveluja. Jos et tee sitä, jatka klikkaamalla `Mahdollisesti myöhemmin`.



![Image](assets/fr/093.webp)



Valitse sitten vahva, yksilöllinen salasana. Tämä suojaa pääsyn Alby Hub:ään solmussasi. Muista tallentaa se salasanahallintaasi.



![Image](assets/fr/094.webp)



Näin pääset Alby Hub:n käyttöliittymään. Sinun ei tarvitse käydä läpi koko konfigurointiprosessia, ellet halua käyttää sitä Lightning-solmun päähallintajärjestelmänä. Kuten aiemmin näimme, Alby Hub te itse asiassa korvata ThunderHub:n käytön solmun hallinnassa. Jos haluat lisätietoja Alby Hub:n mahdollisuuksista, tutustu omaan opetusohjelmaamme:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Siirry `Connections`-valikkoon.



![Image](assets/fr/095.webp)



Tässä näet kaikki sovellukset, jotka tevat muodostaa yhteyden Lightning-solmuun NWC:n kautta. Näihin kuuluu myös edellisessä luvussa jo mainittu Zeus. Tässä käytämme Alby Go:ta. Napsauta Alby Go:ta ja sitten `Connect to Alby Go`-painiketta käynnistääksesi yhteysprosessin.



![Image](assets/fr/096.webp)



### Alby Go:n asentaminen ja liittäminen



Asenna Alby Go-sovellus älypuhelimeesi:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Määritä Alby Hub:ssä ne oikeudet, jotka haluat myöntää Lightning-solmun Alby Go-sovellukselle. Voit esimerkiksi asettaa jaksokohtaiset käyttörajat, NWC-linkin temassaolon päättymispäivän tai jättää täydellisen hallinnan. Kun olet asettanut parametrit, napsauta `Next`-painiketta.



![Image](assets/fr/097.webp)



Alby Hub lähettää sitten generate:lle QR-koodin, jolla luodaan NWC-yhteys Lightning-solmun ja Alby Go:n välille.



![Image](assets/fr/098.webp)



Kun Alby Go-sovellus avataan ensimmäisen kerran, napsauta "Yhdistä Wallet" ja skannaa sitten Alby Hub:n toimittama QR-koodi.



![Image](assets/fr/099.webp)



Valitse nimi tämän wallet:n tunnistamiseksi. Sinulla on nyt etäkäyttöoikeus Lightning-solmuun Alby Go:n kautta. Voit generate laskuja vastaanottaa sats solmussasi tai asettaa Lightning-laskuja suoraan sen kanssa.



![Image](assets/fr/100.webp)



Esimerkiksi lähetin 1543 sats Alby Go-liittymästä.



![Image](assets/fr/101.webp)



Jos siirryn Umbrel:n Lightning-solmuni perusliittymään, näen, että solmuni on todellakin suorittanut tämän maksun.



![Image](assets/fr/102.webp)



Nyt tiedät, miten Lightning-solmua te käyttää helposti mistä tahansa.



## Pitkäkestoinen autonomia Lightningilla


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Olemme nyt tulleet tämän LNP202 käytännön kurssin loppuun. Sinulla on nyt perusteet, joita tarvitset Lightning Network:n suvereeniin käyttöön: ymmärrät solmun todellisen roolin, eri lähestymistapojen kompromissit ja olet perustanut LND-instanssin Umbrel:een johdonmukaisen varmuuskopiointi- ja suojausstrategian avulla. Olet myös avannut ensimmäiset kanavasi, oppinut hallitsemaan likviditeettiä ja tekemään maksuista luotettavia päivittäin.



Toiminnan kannalta solmun pitäisi nyt siirtyä ylläpitorytmiin. Tärkeintä on valvoa sitä (käytettävyys, synkronointi, kanavien tila, maksuhäiriöt jne.), soveltaa Umbrel:n tarjoamia päivityksiä, kun vakaita versioita on saatavilla, ja tarkistaa säännöllisesti, että varmuuskopiot ja vartiotornin konfiguraatio ovat edelleen aktiivisia.



Kanavien suhteen kannattaa omaksua pragmaattinen lähestymistapa: pidä ne, jotka ovat sinulle hyödyllisiä, sulje ne, jotka ovat pysyvästi toimimattomia tai jotka liittyvät epävakaisiin vertaisverkkoihin, ja kohdista pääomasi vähitellen uudelleen kohti kestävämpää topologiaa.



**Yksi yleisimmistä sudenkuopista tässä vaiheessa on se, että Lightning-solmulle osoitetaan liikaa pääomaa. Muista, että Lightning-solmusi on paljon vähemmän turvallinen kuin laitteistoon perustuva wallet, ja että kanavillesi sidottujen varojen saatavuus riippuu varamekanismeista, jotka ovat edelleen epätäydellisiä. Siksi on erittäin tärkeää, että pidät kiinni kohtuullisista summista, joita sinulla on varaa menettää ongelmatilanteissa, ja pidät aina suurimman osan sats:sta ketjussa olevassa laitteisto- wallet:ssä.



Työkalujen osalta suosittelen, että pysyt uteliaana ja tarkkaavaisena uuden kehityksen suhteen. Tässä koulutustilaisuudessa löysimme useita niistä, olipa kyse sitten solmun hallinnoinnista, sen liitettävyydestä tai etäkäytöstä maksujen suorittamiseen. Lightning on kuitenkin erityisen dynaaminen ala. Joka vuosi syntyy uusia ja merkityksellisiä työkaluja, ja myös Umbrel:ään ilmestyy monia uusia sovelluksia. Kun pysyt ajan tasalla näistä uusista kehityskuluista, saatat löytää tehokkaampia tai käytännöllisempiä ratkaisuja kuin tällä kurssilla esitellyt.



Koulutusrintamalla, jos et ole vielä tehnyt sitä, suosittelen lämpimästi osallistumaan Fanis Michalakisin LNP 201 -teoriakurssille, joka on omistettu Lightning Network:n toiminnalle. Se auttaa sinua ymmärtämään paremmin tällä LNP202-kurssilla suoritettavia manipulaatioita ja antaa sinulle enemmän varmuutta solmun päivittäisessä hallinnassa.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Suosittelen myös Ludovic Larsin erinomaista kurssia Bitcoin:n syntyhistoriasta, joka on eri asia, mutta yhtä tärkeä bitcoin-matkallesi.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Mutta ennen kuin siirryt eteenpäin, tet kirjoittaa arvostelun tästä LNP202-kurssista ja tietenkin ottaa tutkintotodistuksen vahvistaaksesi, että olet ymmärtänyt kaiken sen sisällön.



# Viimeinen osa


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Arvostelut & arvostelut


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Loppukoe


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Päätelmä


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>