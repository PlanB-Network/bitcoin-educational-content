---
name: Johdanto Bitcoin mining
goal: Bitcoin mining:n ja proof-of-work:n ymmärtäminen alusta alkaen
objectives: 


  - Ymmärtää proof-of-work:n ja sen roolin Bitcoin:ssa.
  - Analysoi vaikeussäätömekanismi.
  - Tiedä, mitä mining:ään liittyvät tekniset termit todella tarkoittavat.
  - Kuvaa Bitcoin-lohkon ja sen komponenttien rakentamiseen liittyvät vaiheet.
  - Tunnistetaan mining-teollisuuden tärkeimmät kehityssuuntaukset.


---

# Tutustu Bitcoin mining:n perusteisiin



proof of work:n ymmärtäminen tarkoittaa Bitcoin:n toiminnan ymmärtämistä. Ilman tätä keksintöä ja sen nerokasta käyttöä Bitcoin:ta ei yksinkertaisesti olisi voinut olla olemassa. Tämä kurssi tarjoaa sinulle kaiken mining:n teorian, jota tarvitset bitcoin-matkallasi.



MIN 101 on suunnattu ensisijaisesti aloittelijoille, sillä siinä selitetään kaikki käsitteet tarkasti alusta alkaen. Jos sinulla on kuitenkin jo keskitason tiedot, voit tällä kurssilla vahvistaa ymmärrystäsi, korjata joitakin likimääräisiä intuitioita ja tutkia yksityiskohtia, jotka usein puuttuvat valtavirran selityksistä.



Tämän kurssin lopussa osaat selittää proof-of-work:n toiminnan yksinkertaisesti ja täsmällisesti. MIN 101 on myös ihanteellinen johdanto kaikkiin muihin Bitcoin mining Plan ₿ Academy:lle omistettuihin edistyneempiin kursseihin, olivatpa ne sitten teoreettisia tai käytännön kursseja.



+++


# Johdanto


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Kurssin yleiskatsaus


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Tervetuloa MIN 101 -kurssille, jossa tutustut mining:n ja Proof-of-Work:n teoreettisiin peruskäsitteisiin Bitcoin-järjestelmässä. Tämä kurssi on ensimmäinen askel bitcoinerin matkallasi ymmärtääksesi, miten mining toimii. Kun olet suorittanut sen, voit siirtyä edistyneemmille teoriakursseille tai päästä käytännön työhön ja ryhtyä itse bitcoin-louhijaksi!



Tällä MIN 101 -kurssilla emme käy läpi Bitcoin:n peruskäsitteitä, vaan menemme suoraan asian ytimeen: mining:EEN. Jos et ole koskaan kuullut Bitcoin:sta tai jos sen perusteet ovat sinulle vielä hieman epäselviä, suosittelen lämpimästi, että aloitat BTC:n peruskurssilla. Kun olet oppinut nämä perusteet, voit käsitellä MIN 101 -kurssia luottavaisin mielin:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Osa 1 - Johdanto



Aloitamme tämän kurssin valinnaisella ensimmäisellä luvulla, jossa tarjoan hyvin yksinkertaistetun selityksen mining:stä, jotta saat selkeän mielikuvan ennen teknisten mekanismien käsittelyä.



Tarkoituksena ei ole antaa sinulle kaikkia teknisiä yksityiskohtia (ne tulevat myöhemmin kurssilla), vaan antaa sinulle suuntaa-antava säie. Kun tämä kehys on kunnossa, jokainen kehittyneempi käsite, joka esitellään myöhemmin, sopii luontevasti tähän rakenteeseen.



### Osa 2 - Miten proof of work toimii



Johdannon jälkeen osa 2 on koulutusohjelman tekninen perusta. Sen tavoitteena on selittää vaihe vaiheelta, miten Bitcoin tuottaa kelvollisia lohkoja. Aloitamme tutustumalla lohkon rakenteeseen, ennen kuin käymme läpi proof-of-work:n mekanismin: kohteen, nonceen ja hash-funktion roolin. Lopuksi käymme läpi, miten Bitcoin onnistuu säilyttämään vakaan lohkojen tuotantonopeuden hash-tehon vaihteluista huolimatta vaikeuden säätömekanismin ansiosta. Tämän jakson lopussa sinulla on täydellinen käsitys Bitcoin:n proof-of-work:n perusperiaatteista.



### Osa 3 - Bitcoin mining -kannustinjärjestelmä



Kolmannessa osassa tarkastelemme, miksi kaivostyöläisiä kannustetaan osallistumaan rehellisesti mining:een. Kerromme yksityiskohtaisesti lohkopalkkion periaatteesta, sen koostumuksesta ja laskentamenetelmästä, sen kehittymisestä ajan mittaan halvingien kautta sekä coinbase-transaktion erityisroolista.



### Osa 4 - Bitcoin mining -teollisuus



Neljännessä osassa mining palautetaan takaisin toiminnalliseen todellisuuteen. Siinä seurataan mining-koneiden kehitystä Bitcoin:n alusta nykyaikaiseen ASIC:een, jotta voidaan ymmärtää nykyisiä laitteistorajoituksia. Tarkastelemme myös mining-poolien perusteita, jotta ymmärtäisimme, miten louhijat onnistuvat vähentämään tulojensa vaihtelua.



### Osa 5 - Loppuosa



Kurssin loppuosassa voit testata mining:n osaamistasi suorittamalla tutkintotodistuksen.



Tämän MIN 101 -kurssin tavoitteena on siis antaa sinulle selkeä, jäsennelty ja kestävä käsitys Bitcoin mining:stä sekä teknisesti että taloudellisesti.



Oletko valmis löytämään Bitcoin mining? Aloitetaan!




## Bitcoin mining helpoksi tehty


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Ennen kuin siirrymme yksityiskohtaiseen ja teknisempään selitykseen Bitcoin [mining](https://planb.academy/resources/glossary/mining):stä, haluaisin antaa sinulle yleiskatsauksen periaatteesta, joka on tarkoituksella yksinkertainen ja kaavamainen. Jos sinulla on jo jonkin verran perustietoja, voit siirtyä suoraan asian ytimeen seuraavassa luvussa, kun olet vastannut tietokilpailun kysymyksiin. Tämä luku on suunnattu ensisijaisesti aloittelijoille, jotta saatte varovaisen alun.



Kuvittele Bitcoin suureksi julkiseksi muistikirjaksi, jonka kaikki jakavat ja johon kirjataan, kuka on lähettänyt bitcoineja kenellekin. Tätä muistikirjaa kutsutaan [lohkoketjuksi](https://planb.academy/resources/glossary/blockchain). Se ei voi olla vain yhden henkilön hallussa, koska muuten siihen pitäisi luottaa. Sen sijaan Bitcoin toimii kollektiivisesti: tuhannet tietokoneet varmistavat ja ylläpitävät samaa versiota tästä muistikirjasta.



![Image](assets/fr/049.webp)



Kun teet maksun Bitcoin:ssä, luot [tapahtuman](https://planb.academy/resources/glossary/transaction-tx). Tätä tapahtumaa ei lisätä välittömästi muistikirjaan. Se lähetetään ensin verkkoon ja odottaa sitten, että se liitetään seuraavaan tapahtumapakettiin. Tätä pakettia kutsutaan [lohkoksi](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Lohko on yksinkertaisesti joukko transaktioita, jotka on ryhmitelty yhteen. Kun lohko on valmis, ei riitä, että se julkaistaan. Sinun on todistettava verkolle, että lohko on sen arvoinen, että se lisätään pooliin. Tässä kohtaa mining astuu kuvaan.



Mining on lohkon validointityö, joka kuluttaa energiaa. [Louhijoiksi](https://planb.academy/resources/glossary/miner) kutsutut toimijat käyttävät erikoistuneita tietokoneita. Nämä koneet kuluttavat sähköä suorittaakseen hyvin suuren määrän testejä silmukassa, kunnes ne löytävät todisteen, jonka verkko hyväksyy. Kun louhija löytää tämän todisteen, hänen lohkonsa katsotaan kelvolliseksi.



Kun lohko on validoitu, se lähetetään verkkoon. Muut [solmut](https://planb.academy/resources/glossary/node) tarkistavat nopeasti, että se on sääntöjen mukainen, ja lisäävät sen sitten aiempien lohkojen sarjaan. Tämän vuoksi sitä kutsutaan "lohkoketjuksi": jokainen uusi lohko tulee peräkkäisessä järjestyksessä muiden jälkeen, ja tämä ketju kasvaa pikkuhiljaa.



![Image](assets/fr/051.webp)



Yhteenvetona voidaan todeta, että tapahtumat luodaan ensin. Sitten ne ryhmitellään lohkoksi. Sitten louhija validoi lohkon kuluttamalla sähköä. Lopuksi lohko lisätään lohkoketjuun, ja sen sisältämät transaktiot [vahvistetaan](https://planb.academy/resources/glossary/confirmation).



Jos kaivostyöläiset kuluttavat sähköä, se ei johdu siitä, että he ovat vapaaehtoisia. He tekevät sen, koska siitä saa palkkion. Kun louhija validoi lohkon, hän saa kahdenlaisia tuloja. Yhtäältä hän saa uusia bitcoineja. Toisaalta hän kerää käyttäjien maksamat [maksut](https://planb.academy/resources/glossary/transaction-fees) lohkoon sisältyvistä transaktioista. Toisin sanoen louhija saa korvauksen sekä ohjelmoidun rahan liikkeeseenlaskusta että markkinoiden määrittelemistä transaktiomaksuista.



Tässä vaiheessa sinulle annetaan tarkoituksella hyvin yksinkertainen kuva mining:stä. Siinä ei vielä selitetä, miten lohko on rakennettu yksityiskohtaisesti, tai miten tarkalleen ottaen kaivostyöläisten etsimä todiste toimii, tai miten Bitcoin pitää tasaista tahtia, tai miten palkkio lasketaan tarkasti, tai miten sitä lunastetaan. Ei se mitään, muuta emme näe tämän MIN 101 -kurssin loppuosassa!



Tämän luvun tavoitteena oli yksinkertaisesti antaa sinulle selkeä henkinen rakenne: transaktiot → lohkot → mining → lohkoketju → palkkio. Pidä tämä ajatusketju mielessäsi. Kurssin loppupuolella jokainen luku lisää kerros teknisiä yksityiskohtia johonkin näistä elementeistä, kunnes ymmärrät paitsi, mitä tapahtuu, myös sen, miten ja miksi se toimii luotettavasti, laajassa mittakaavassa, ilman pomoa ja ilman, että tarvitset luottamusta.



# Miten proof of work toimii


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Bitcoin-tapahtumapolku


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Jotta ymmärtäisimme, mistä Bitcoin mining:ssa on kyse, meidän on ensin seurattava tyypillisen Bitcoin-tapahtuman kulkua. Näin näet tarkalleen, missä lohko on mukana ja miksi se on järjestelmän ydin. Tämän haluan sinun löytävän tässä ensimmäisessä luvussa.



Bitcoin:ssä transaktio on tietorakenne, joka siirtää bitcoinien omistusoikeuden käyttäjältä toiselle. Konkreettisesti sanottuna se kuluttaa aiempien transaktioiden (niin sanottujen [UTXO](https://planb.academy/resources/glossary/utxo):ien) "[tuotoksia](https://planb.academy/resources/glossary/output)", joihin viitataan "[syötteinä](https://planb.academy/resources/glossary/input)", ja luo sitten uusia "tuotoksia", jotka määrittelevät, kenelle nämä bitcoinit nyt kuuluvat ja millä edellytyksillä niitä voidaan käyttää myöhemmin.



![Image](assets/fr/001.webp)



Tärkeä seikka Bitcoin:ssä on valtuutus käyttää varoja. Bitcoin:t eivät ole tilillä, kuten pankissa olevat rahasi, vaan ne on lukittu käyttöehdoilla. Kun [wallet](https://planb.academy/resources/glossary/wallet) haluaa käyttää UTXO:ta panoksena, sen on toimitettava kryptografinen todiste siitä, että sillä on oikeus avata lukitus. Tämä todiste on usein [digitaalinen allekirjoitus](https://planb.academy/resources/glossary/digital-signature) generated [yksityisestä avaimesta](https://planb.academy/resources/glossary/private-key). Tämän vuoksi bitcoin-käyttäjät vaativat yksityisten avainten suojaamista: ne avaavat pääsyn bitcoineihisi ja mahdollistavat näin ollen niiden käyttämisen.



![Image](assets/fr/002.webp)



Bitcoin:n digitaalisella allekirjoituksella on kaksi tärkeää tehtävää:




- Menojen hyväksyminen: tämä todistaa, että käyttäjällä on UTXO-menoehdon edellyttämä yksityinen avain;
- Eheyden suojaus: yhdistää valtuutuksen tapahtuman tarkkoihin yksityiskohtiin (vastaanottajat, määrät, maksut jne.). Jos joku muuttaa tapahtumaa jälkikäteen, allekirjoitus ei ole enää voimassa.



Kun käyttäjän Bitcoin wallet on muodostanut ja allekirjoittanut tapahtuman oikein, se on lähetettävä Bitcoin-verkossa.



### Bitcoin-solmun rooli jakelussa



Bitcoin on [vertaisverkko](https://planb.academy/resources/glossary/peertopeer-p2p): ei ole keskitettyä palvelinta, joka vastaanottaa ja käsittelee kaikki tapahtumat. Solmut hoitavat tämän tehtävän kollektiivisesti. Bitcoin-solmu on ohjelmisto (esim. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)), joka on yhteydessä muihin Bitcoin-verkon solmuihin ja jonka päätehtävänä on tarkistaa, tallentaa ja välittää transaktioita ja lohkoja.



Kun lähetät tapahtuman wallet:stä, wallet välittää sen solmuun (omaan tai palvelun solmuun). Tämä solmu tarkistaa ensin, että tapahtuma on erilaisten sääntöjen mukainen, kuten:




- allekirjoitukset ovat voimassa;
- syötteet viittaavat olemassa oleviin UTXO:iin (eli olemassa oleviin bitcoineihin);
- näitä UTXO-varoja ei ole jo käytetty muualla;
- tuotosten määrä on pienempi tai yhtä suuri kuin panosten määrä (bitcoineja ei luoda tyhjästä);
- jne.



Jos tapahtuma läpäisee kaikki nämä tarkistukset, solmu välittää sen muille verkon solmuille, joihin se on yhteydessä. Ne puolestaan tarkistavat sen ja välittävät sen eteenpäin ja niin edelleen. Muutamassa sekunnissa tapahtuma on levinnyt ja tullut koko Bitcoin-verkon tai ainakin suuren osan siitä tietoon.



![Image](assets/fr/003.webp)



### Mempool: transaktioiden odotushuone



Transaktion lähetyshetken ja sen lohkossa vahvistamisen välillä sen on odotettava. Tätä odotusaluetta kutsutaan nimellä **[mempool](https://planb.academy/resources/glossary/mempool)** (lyhenne sanoista `memory` ja `pool`). Mempool on siis väliaikainen säilytyspaikka kelvollisille, mutta vielä vahvistamattomille transaktioille.



Tärkeä seikka: ei ole olemassa yhtä ainoaa mempoolia, vaan ainoastaan mempoolit. Jokainen solmu ylläpitää omaa mempooliaan, jolla on omat paikalliset rajoituksensa. Tämä tarkoittaa, että millä tahansa hetkellä kahdella solmulla voi olla hieman erilainen mempoolin sisältö (riippuen siitä, mitä ne ovat saaneet, mitä ne ovat hylänneet tai mitä ne ovat puhdistaneet).



![Image](assets/fr/004.webp)



Tässä vaiheessa verkko tietää transaktiosta, on vahvistanut sen ja pitää sitä muistissa, kunnes se vahvistetaan. Transaktio vahvistetaan kuitenkin vasta, kun louhija lisää sen lohkoon ja verkko hyväksyy lohkon.



### Blockchain: julkinen aikaleimarekisteri



Koska bitcoin on aineeton valuutta, sen on ratkaistava yksi ongelma: estettävä [kaksinkertainen rahankäyttö](https://planb.academy/resources/glossary/double-spending-attack) ilman keskusviranomaista. Jos kaksi transaktiota yrittää käyttää saman UTXO:n, kaikkien on pystyttävä lähentymään yhteen, yhtenäiseen tilaan. Satoshi Nakamoto kiteyttää tämän ongelman tähän kuuluisaan lauseeseen:



> Ainoa tapa varmistaa, ettei tapahtumaa ole tapahtunut, on olla tietoinen kaikista tapahtumista.

Toisin sanoen, jos haluat tietää, että bitcoinia ei ole jo käytetty, tarvitset yhteiset tiedot aiemmista käyttökerroista.



Tämä on lohkoketjun rooli: julkinen rekisteri, joka sisältää transaktioiden historian. Sen sijaan, että Bitcoin kirjoittaisi jokaisen transaktion sitä mukaa kuin se tapahtuu, se ryhmittelee ne lohkoiksi. Kukin lohko toimii historiasivuna, ja järjestelmä toimii siten kuin aikaleimapalvelin: se järjestää transaktiot ajan mittaan todennettavalla tavalla.



Tätä rekisteriä ei voi kirjoittaa uudelleen yksinkertaisen periaatteen ansiosta: jokainen lohko sisältää edellisen lohkon kryptografisen sormenjäljen ([hash](https://planb.academy/resources/glossary/hash-function)). Lohkot ovat siis yhteydessä toisiinsa: jos aiempaa lohkoa muutetaan, sen hash muuttuu, mikä katkaisee yhteyden seuraavaan lohkoon, mikä katkaisee yhteyden sitä seuraavaan lohkoon ja niin edelleen. Tämä riippuvuusketju antaa "*lohkoketjulle*" sen nimen.



![Image](assets/fr/005.webp)



Kun olemme ymmärtäneet nämä Bitcoin:n perusperiaatteet, voimme kuvata louhijan tavoitteen konkreettisemmin: rakentaa uusi lohko, joka laajentaa olemassa olevaa ketjua merkitsemällä siihen vireillä olevia transaktioita, ja yrittää sitten saada sen kelvolliseksi (tämä on se kuuluisa "[proof of work](https://planb.academy/resources/glossary/proof-of-work)", jota tutkimme myöhemmässä luvussa). Mutta ensin selvitetään yhdessä seuraavassa luvussa, miten ehdokaslohko rakennetaan.



## Bitcoin-lohkon rakentaminen


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Olet nyt ymmärtänyt, miten Bitcoin-transaktio toimii ja mikä on lohkoketjun rooli. Ennen kuin tarkastelemme tarkemmin proof-of-work:n toimintaa, on kuitenkin vielä yksi olennainen vaihe, joka louhijan on suoritettava: [ehdokaslohkon](https://planb.academy/resources/glossary/candidate-block) rakentaminen. Selvitetään yhdessä, mikä ehdokaslohko on ja miten louhija rakentaa sen, ennen kuin lähdetään etsimään pätevää todistusta.



### Ehdokaslohko



Miner:n on itse rakennettava lohkojaan ennen kuin se yrittää louhia niitä. Kukin louhija puolestaan rakentaa niin sanotun ehdokaslohkon omassa mempoolissaan vireillä olevista transaktioista. Ehdokaslohkon rakentaminen koostuu siis seuraavista vaiheista:




- valita mukaan otettavat tapahtumat;
- järjestää nämä liiketoimet tavalla, joka on yhteensopiva Bitcoin-sääntöjen kanssa;
- tuottaa lohkon metatiedot, jotka on tallennettu lohkon [otsikkoon](https://planb.academy/resources/glossary/block-header).



Transaktioiden valinta noudattaa yksinkertaista taloudellista logiikkaa: lohkolla on Bitcoin-protokollan rajoittama kapasiteetti, joten louhija pyrkii maksimoimaan sen, mitä hän ansaitsee tästä tilasta. Hän valitsee ensisijaisesti transaktiot, jotka tarjoavat korkeimmat maksut suhteessa niiden lohkossa varaamaan tilaan (tätä kutsutaan "maksuprosentiksi", joka ilmaistaan sats/vB:nä). Maksujen yksityiskohtia käsitellään myöhemmin; muistakaa vain ajatus lajittelusta tilatehokkuuden mukaan.



Bitcoin-lohko koostuu siis kahdesta pääosasta:




- luettelo tapahtumista;
- lohkon otsikko, joka toimii tavallaan lohkon henkilökorttina.



![Image](assets/fr/006.webp)



Otsikko on olennainen, koska sitä käytetään proof-of-work:n perustana: Bitcoin:ssa ei louhita suoraan koko lohkoa, vaan ainoastaan lohkon otsikko, jossa on yhteenveto tiedoista, joita tarvitaan lohkon liittämiseksi ketjuun ja sen sisällön sitomiseksi. Jotta otsikko edustaisi kaikkia transaktioita, Bitcoin käyttää kryptografista työkalua: [Merkle-puuta](https://planb.academy/resources/glossary/merkle-tree).



### Merkle-puu: yhteenveto suuresta joukosta tapahtumia



Kaikkien tapahtumien luettelointi otsikkoon olisi mahdotonta: lohko voi sisältää tuhansia tapahtumia, kun taas otsikolla on kiinteä koko (80 tavua). Ratkaisu on siis laskea yksilöllinen hash, joka riippuu kaikista lohkon transaktioista: tämä on [Merkle-juuresta](https://planb.academy/resources/glossary/merkle-root).



Periaate on seuraava:




- lasketaan kunkin tapahtuman kryptografinen sormenjälki (hash);
- nämä hashit paritetaan, yhdistetään, ja sitten hashataan uudelleen, jolloin muodostuu uusi hashikerros;
- tämä prosessi toistetaan, kunnes saadaan yksi lopullinen hash: Merkle-juureen.



![Image](assets/fr/007.webp)



Jos siis yksittäinen tapahtuma muuttuu, vaikka vain yhden bitin verran, seurauksena on sen sormenjäljen muutos, joka leviää Merkle-juureen. Tämä juuri sisältyy lohkon otsikkoon. Aikaisemman tapahtuman muuttaminen tarkoittaa siis sen lohko-otsikon muuttamista, johon se sisältyy, ja näin ollen lohkon jalanjäljen muuttamista ja sen jälkeen linkin muuttamista seuraaviin lohkoihin.



[SegWit](https://planb.academy/resources/glossary/segwit):n jälkeen olemme erottaneet allekirjoitukset muista. Todellisuudessa jokaisessa lohkossa on siis kaksi Merkle-puuta. Tämä erottelu vaikuttaa tapaan, jolla laskemme lohkon koon, ja tiettyihin kryptografisiin sitoumuksiin, mutta perusajatus pysyy samana: otsikon on sitouduttava tiiviisti lohkon koko sisältöön.



### Lohkon otsikko



Lohkon otsikko on 80 tavua pitkä ja sisältää tasan 6 kenttää. Nämä kuusi kenttää hashataan, kun etsitään proof of work:tä (katso seuraava luku):





- Versio (`version`): Tämä osoittaa, mitä sääntöjä tai päivityssignaaleja lohko noudattaa. Se toimii mekanismina protokollan yhteensopivuuden ja kehityksen ylläpitämiseksi.




- Edellisen lohkon hash (`previousblockhash`): Tämä on edellisen lohkon otsikon hash. Tämä yhdistää lohkot toisiinsa. Ilman tätä kenttää meillä olisi itsenäisiä lohkoja. Sisällyttämällä edellisen lohkon otsikon hash, saadaan ketju, jossa jokainen uusi lohko rakentuu edellisen lohkon päälle.





- Merkle-juuri (`merkleroot`): Tämä on kaikkien lohkon transaktioiden sormenjälki (Merkle-puun kautta). Se yhdistää otsikon ja sisällön: jos louhija muuttaa transaktioiden valintaa tai järjestystä, juuri muuttuu.





- [Aikaleima](https://planb.academy/resources/glossary/timestamp): Tämä on louhijan valitsema aikaleima (Unix-aika) (voimassaoloaikarajoituksin), jonka on osoitettava, milloin lohko louhittiin. Sen ei tarvitse olla täysin sekunnin tarkkuudella, mutta sen on täytettävä tietyt ehdot, jotta verkko voi hyväksyä sen.





- Koodattu vaikeuskohde (`nbits`): Tämä kenttä koodaa nykyisen [vaikeustavoitteen](https://planb.academy/resources/glossary/difficulty-target). Käymme tarkemmin läpi vaikeuksia käsittelevässä luvussa, mutta muista, että tämä parametri on osa otsikkoa.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Tämä on arvo, jota louhija voi vapaasti muuttaa. Se toimii säädettävänä muuttujana proof-of-work:n aikana. Selitän sen roolia tarkemmin seuraavassa luvussa, mutta on tärkeää ymmärtää, että nonce on osa lohko-otsikkoa ja että se on suunniteltu mahdollistamaan peräkkäiset yritykset.



Jotta tätä olisi helpompi havainnollistaa, tässä on esimerkki lohkon otsikosta heksadesimaalimuodossa (80 tavua):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Seuraavassa on kenttäkohtainen erittely:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Tämä louhijan rakentama ehdokaslohkon otsikko muodostaa heidän työnsä perustan. Kun etsitään kelvollista proof-of-work:aa, koko transaktioluetteloa ei suoraan hashata silmukassa, vaan tämä 80 tavun lohko sisältää kaiken, mitä tarvitaan lohkon linkittämiseen menneisyyteen ja sen sisällön sitomiseen, ja se sisältää myös parametrit, joita tarvitaan mining-mekanismia varten, jota tarkastellaan seuraavassa luvussa.



## Hash, kohde ja nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Edellisissä luvuissa seurasit Bitcoin-tapahtuman kulkua: wallet luo ja allekirjoittaa sen, solmut välittävät sen eteenpäin, se tallennetaan mempooliin ja vahvistetaan, kun louhija sisällyttää sen verkon hyväksymään lohkoon. Mutta emme ole vielä nähneet, miten louhija voi lisätä lohkonsa lohkoketjuun. Mikä on prosessi mining:n takana?



mining-prosessin ymmärtäminen on melko yksinkertaista. Se koostuu kolmesta käsitteestä, jotka kulkevat käsi kädessä: hash-funktio, tavoitearvo ja muuttuja, jota louhija voi muokata. Katsotaanpa, miten se kaikki toimii.



### Hash-funktio



Hash-funktio on työkalu, joka ottaa syötteenä viestin ja tuottaa kiinteän kokoisen tulosteen, jota kutsutaan nimellä "*fingerprint*" tai "*hash*".



![Image](assets/fr/010.webp)



Hash-funktio on mielenkiintoinen tietokonejärjestelmissä, koska sillä on tiettyjä ominaisuuksia:





- Jos muutat yhdenkin bitin syötteessä, tuloksena saatava hash muuttuu täysin ja ennalta arvaamattomasti;



![Image](assets/fr/011.webp)





- On mahdotonta siirtyä ulostulosta sisääntuloon: funktio on peruuttamaton;



![Image](assets/fr/012.webp)





- On mahdotonta löytää kahta erilaista viestiä, jotka antavat täsmälleen saman hashin.



![Image](assets/fr/013.webp)



Bitcoin:ssä mining:ssa käytetty hash-funktio on "[SHA256](https://planb.academy/resources/glossary/sha256)", jota käytetään kahdesti peräkkäin. Tämä tunnetaan nimellä kaksinkertainen SHA256 eli SHA256d. Lohkon sormenjälki saadaan aikaan juuri tällä kaksinkertaisella hashilla.



```text
hash = SHA256(SHA256(message))
```



Meidän tapauksessamme `message` vastaa itse asiassa lohko-otsikkoa, jonka näit edellisessä luvussa. Muistutuksena mainittakoon, että otsikko on pieni rakenne, joka tiivistää kaiken lohkossa olevan.



![Image](assets/fr/014.webp)



### Työn todistus: tavoitetta pienemmän hash-arvon löytäminen



Proof-of-Work:ta kuvataan usein monimutkaisen ongelman ratkaisuksi. Todellisuudessa kyse ei ole niinkään ongelmasta vaan pikemminkin kokeilemalla ja erehdyksellä tehtävästä etsinnästä: louhijan on löydettävä otsikon versio, jonka hash-arvo (SHA256d-hash-funktion läpikäymisen jälkeen) täyttää yksinkertaisen ehdon: sen on oltava tiettyä tavoitetta pienempi.



Tämä ehto muotoillaan seuraavasti:




- lohkootsikon hash lasketaan hash-funktion avulla;
- tulkitsemme tämän hashin numeroksi;
- jotta lohko olisi voimassa, tämän luvun on oltava pienempi tai yhtä suuri kuin arvo nimeltä "*vaikeustavoite*".



Toisin sanoen lohko on voimassa, jos:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Kohde on 256-bittinen luku. Koska `SHA256d`:n tuottama hash on myös 256-bittinen, niitä voidaan verrata kahtena lukuna. Mitä alhaisempi tavoite on, sitä vaikeampi ehto on, koska tämän rajan alapuolella on vähemmän mahdollisia tuloksia. Mitä korkeampi tavoite on, sitä helpompi ehto on täyttää ja sitä helpompi on louhia lohko. Tarkastelemme tarkemmin, miten tämä tavoite määritetään myöhemmissä luvuissa.



Tässä järjestelmässä hash-funktio on mielenkiintoinen. Muista, että on helppoa laskea tuloste syötteestä, mutta mahdotonta löytää syötettä tuntemalla vain funktion tuloste. mining:ssä louhijoita ei pyydetä löytämään tarkkaa hashia, vaan pikemminkin löytämään tavoitearvon alittava hash. Ainoa tapa saavuttaa tämä tavoite on tehdä hyvin monta yritystä, kunnes heidän ehdokaslohkonsa tietty otsikko tuottaa hash-arvon, joka on pienempi kuin tavoitearvo.



Kun tavoite on riittävän alhainen, tämä prosessi tulee kalliiksi. Louhija laskee hakkerin ehdokkaan lohkon otsikon, tarkistaa tuloksen ja jos ehto ei täyty, muuttaa otsikkoa ja toistaa laskennan. Tätä silmukkaa toistetaan, kunnes kelvollinen otsikko löytyy. Kun otsikon hash lopulta täyttää ehdon, proof of work on perustettu, lohko katsotaan kelvolliseksi ja se voidaan lähettää Bitcoin-verkkoon, jotta solmut voivat lisätä sen lohkoketjuunsa. Voittanut louhija saa sitten siihen liittyvän palkkion (sen koostumuksesta kerrotaan tarkemmin myöhemmin), kun taas kaikki louhijat lähtevät välittömästi etsimään uutta, kelvollista otsikkoa seuraavaa lohkoa varten.



Tämän mekanismin perustavanlaatuinen etu on sen epäsymmetrisyys. proof of work:n tuottaminen on kallista louhijoille, koska se vaatii suuren määrän hash-laskentoja. Toisaalta verifioijille eli verkon solmuille verifiointi on äärimmäisen yksinkertaista: niiden tarvitsee vain hassata louhijan toimittama lohkootsikko ja tarkistaa, että tuloksena saatu hash-arvo on todellakin tavoitetta pienempi. Todisteen löytäminen vaatii siis paljon työtä ja resursseja, kun taas sen paikkansapitävyyden todentaminen on nopeaa ja edullista. Juuri tämä ominaisuus määrittelee tehokkaan proof-of-work-järjestelmän.



### Nonce



Jäljelle jää käytännön kysymys: jos louhijan rakentama ehdokaslohkon otsikko ei anna kelvollista hashia, miten louhija voi yrittää uudelleen? Hänen on muutettava jotakin otsakkeessa saadakseen toisen hashin. Juuri tämä on nonceen tehtävä.



Muista hash-funktion ensimmäinen ominaisuus: yhden bitin muuttaminen syötteessä riittää tuottamaan täysin erilaisen ja arvaamattoman hash-tuloksen. Jokainen hash-laskenta on siis kuin satunnaisarvonta.



![Image](assets/fr/016.webp)



Kokeillakseen onneaan uudelleen louhijan ei tarvitse muuttaa koko lohkonsa otsikkoa: hänen on muutettava vain pieni osa siitä, sillä jo yksi eri bitti johtaa täysin uuteen hashiin, joka voi olla kelvollinen, jos se on pienempi kuin tavoite.



Juuri tämän vuoksi lohko-otsikko sisältää nonce-tiedon. Nonce on 32-bittinen arvo, jota käytetään kerran ja joka sitten korvataan. Käytännössä louhija voi testata samalle lohkoehdokkaalle noin 4,29 miljardia mahdollista arvoa (0:sta 2^32 - 1:een). Jokainen nonce-arvon muunnos muuttaa lohkon otsikkoa ja näin ollen täysin SHA256d-hash-funktion soveltamisen jälkeen tuotettua hash-arvoa.



mining-prosessi on hyvin yksinkertainen:




- louhija muodostaa ehdokaslohkon (transaktiot + otsikko);
- laskee sen jälkeen `SHA256d(header)`:n hashin;
- jos tulos on suurempi kuin tavoite, se vaihtaa noncea;
- alkaa uudelleen;
- jne.



![Image](assets/fr/017.webp)



Itse asiassa nonce ei ole ainoa kenttä, jota voidaan muuttaa. Mikä tahansa lohkon transaktioissa tapahtuva muutos johtaa Merkle-puun juuren muuttumiseen ja siten kyseisen lohkon otsikon muuttumiseen. Nykyaikaisella laskentateholla 4,29 miljardin mahdollisen nonce-arvon läpikäyminen voidaan tehdä suhteellisen nopeasti. Tämän vuoksi on olemassa toinen kenttä, jota kutsutaan yleensä nimellä "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", joka moninkertaistaa otsikon vaihtelumahdollisuudet entisestään. Palaamme tähän mekanismiin tarkemmin myöhemmässä luvussa.



### Mikä on proof of work:n tarkoitus?



Kutsumme sitä "todisteeksi", koska tulos on välittömästi todennettavissa: kun lohko on tuotettu, mikä tahansa solmu voi sekunnin murto-osassa tarkistaa, että sen otsikon kryptografinen hash-arvo on todellakin alle vaaditun tavoitteen. Kutsumme sitä "työksi", koska tämän hash-arvon saavuttaminen vaatii lukuisia yrityksiä ja siten todellisia laskenta- ja energiakustannuksia.



Bitcoin:n [valkoisessa kirjassa](https://planb.academy/resources/glossary/white-paper) Satoshi Nakamoto esittää kaksi etua proof-of-work-järjestelmän käytöstä Bitcoin:ssa:





- Taloushistorian Seal:**



Kun laskentakuorma on käytetty, lohko lukitaan: sen muuttaminen edellyttäisi kyseisen lohkon proof of work:n uudelleen tekemistä. Ja koska lohkot on ketjutettu toisiinsa, vanhan lohkon muuttaminen tarkoittaisi myös kaikkien seuraavien lohkojen uudelleenlaskemista, ja sen jälkeen rehellisen ketjun käynnissä olevan työn saavuttamista ja ylittämistä.



Toisin sanoen proof-of-work toimii aikaleimausjärjestelmän selkärankana, jolloin menneisyyden väärentäminen on yhä kalliimpaa, kun lohkoja kertyy. Kun uusi lohko louhitaan, proof of work:n tarjoamaa suojausta sovelletaan samanaikaisesti ja yhdenmukaisesti kaikkiin olemassa oleviin UTXO-lohkoihin. Jokaisen lisätyn lohkon myötä jokainen UTXO kerää näin ollen lisää Proof-of-Work:n antamaa turvaa.





- Määrittele enemmistösääntö ([konsensus](https://planb.academy/resources/glossary/consensus)) ja neutraloi Sybil:**



Proof-of-Work mahdollistaa myös sen, että Bitcoin pääsee yhteisymmärrykseen ilman "yksi tunnus = yksi ääni" -äänestyssääntöä, jota voidaan helposti väärentää luomalla massiivisesti identiteettejä (IP-osoitteita, solmuja, avaimia jne.).



Bitcoin:ssä "enemmistö*" ei ole suurin määrä osallistujia, vaan **ketju, joka kerää eniten työtä**. Satoshi:n mukaan tämä on "yksi prosessori = yksi ääni" -periaate, eli ääni painotetaan kelvollisten lohkojen tuottamiseen käytetyn todellisen laskentatehon mukaan. Tuhansien solmujen käyttöönotto ei siis sinänsä tuo mitään etua Bitcoin:een verrattuna. Ilman ylimääräistä laskentatehoa ei kerry lisää todisteita, ja [Sybil-hyökkäyksestä](https://planb.academy/resources/glossary/sybil-attack) tulee hyödytön, kun taas päätössääntö pysyy objektiivisena eikä vaadi osallistujien tunnistamista.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer sähköinen käteisrahajärjestelmä.*](https://bitcoin.org/bitcoin.pdf)



Alaikäisten hyödyllisyyteen ja valtuuksiin liittyvät periaatteet ovat erittäin monimutkainen aihe, jota en käsittele tarkemmin tällä kurssilla. Palaamme kuitenkin tähän aiheeseen perusteellisesti tulevilla MIN 201 -koulutuskursseilla.



Tällä hetkellä voit tiivistää mining:n toiminnan seuraavasti: louhijat rakentavat ehdokaslohkon mempoolissa vireillä olevien transaktioiden avulla ja etsivät sitten sen otsikon hashia (SHA256d:n avulla), joka on pienempi tai yhtä suuri kuin tavoite. He saavuttavat tämän testaamalla epäsisältöjä kokeilemalla ja erehtymällä.



Seuraavassa luvussa teemme lyhyen historiallisen ekskursion proof-of-work-periaatteeseen ymmärtääkseen sen taustan ja tarkastelemme sitten, miten järjestelmä määrittää vaikeuskohteen.



## proof of work:n historia


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work-tekniikkaa ei keksitty Bitcoin:a varten. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi):ssa käytettiin ja yhdistettiin useita vanhempia ideoita, joita oli jo tutkittu eri yhteyksissä.



### Hashcash



Sähköpostin roskapostiongelmasta tuli merkittävä 1990-luvun lopulla. Jos sähköpostin lähettäminen ei maksa juuri mitään, roskapostittaja voi lähettää miljoonia. Mutta jos jokainen viesti vaatii vain pienen laskennallisen panostuksen, yhden laillisen viestin lähettäminen on tavalliselle käyttäjälle helppoa, kun taas miljoonien viestien lähettäminen tulee hyvin kalliiksi.



Tämä on [Hashcashin](https://planb.academy/resources/glossary/hashcash) tavoite, jota Adam Back ehdotti vuonna 1997 ja jota pidetään proof-of-work-periaatteen keksintönä. Hashcashin periaate on hyvin samankaltainen kuin mining:n: tuotetaan hash, joka noudattaa tiettyä ehtoa (tietty määrä nollia hashin alussa). Todiste on sitten viestin mukana, ja vastaanottaja voi tarkistaa sen hyvin nopeasti. Jos vastaanotetaan sähköpostiviesti, joka ei sisällä tätä todistetta, sitä voidaan pitää välittömästi roskapostina ja suodattaa. Roskapostittajat joutuvat tällöin käyttämään huomattavan paljon energiaa miljoonien viestien lähettämiseen, mikä vähentää huomattavasti (tai jopa mitätöi kokonaan) tämäntyyppisen toiminnan kannattavuutta, olipa kyse sitten markkinoinnista tai vilpillisestä toiminnasta.



Nykyään Hashcashia ei käytetä sähköpostiin. Roskapostin suodatus perustuu nykyään suurelta osin keskitettyihin järjestelmiin. Hashcashin etu nykyisiin ratkaisuihin verrattuna on se, että se ei vaadi keskitettyä suodatusta: kuka tahansa voi säätää parametreja omien kriteeriensä mukaan. Se ei myöskään vaadi tunnistamista, sillä hash-haku voidaan suorittaa nimettömänä. Ennen kaikkea se ei perustu mainejärjestelmään, jolla on taipumus ottaa käyttöön subjektiivisia suodatuksen muotoja.



Hashcashissa ei ollut kyse rahan luomisesta. Sillä pyrittiin asettamaan marginaalikustannuksia helposti automatisoitavissa olevalle digitaaliselle toiminnalle.



![Image](assets/fr/008.webp)



### Bitti kultaa



1990-luvun lopulla ja 2000-luvun alussa Nick Szabo tutki proof of work:een perustuvaa ajatusta digitaalisesta niukkuudesta. Hänen Bit Gold -nimisessä käsitteellisessä hankkeessaan arvoyksiköitä luodaan ratkaisemalla kallis proof of work-ongelma ja tallentamalla nämä todisteet rekisteriin eräänlaisen omistusoikeuden luomiseksi.



Bit Gold ei johtanut Bitcoin:n kaltaiseen käyttöönotettuun järjestelmään, mutta se sisältää useita tärkeitä oivalluksia: ajatuksen siitä, että laskenta voi tuottaa niukkuutta, ja ajatuksen elementtien ajoituksesta ajan mittaan, jotta voidaan luoda historia, jota on vaikea kirjoittaa uudelleen.



### RPOW



Vuonna 2004 Hal Finney ehdotti RPOW:ta (*Reusable Proofs of Work*). Ajatuksena oli tuottaa työtodistuksia, joita voitaisiin sitten vaihtaa sen sijaan, että ne vain kulutettaisiin. RPOW:n tavoitteena oli luoda proof of work:n pohjalta digitaalisia token-todistuksia ja järjestelmä näiden token-todistusten todentamiseksi ja siirtämiseksi ilman niiden kopiointia. RPOW ei myöskään ratkaissut täysin hajautetun rekisterin ongelmaa tyydyttävästi, kuten Bitcoin myöhemmin teki, mutta se on edelleen yksi Bitcoin:n suurista edeltäjistä.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold ja RPOW käyttävät proof-of-work:ää kustannusten asettamiseen ja niukkuuden luomiseen. Bitcoin jatkaa tätä mekanismia, mutta antaa sille keskeisen ja kollektiivisen roolin: proof-of-work:ää ei käytetä vain jonkin luomiseen, vaan sitä käytetään myös päättämään, kenellä on oikeus kirjoittaa rekisterin seuraava sivu (seuraava lohko), ja tekemään rekisterin väärentämisestä kallista.



## Vaikeustavoitteen säätäminen


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Edellisissä luvuissa näit proof-of-work:n ytimen: louhijat hakkeroivat lohkonsa otsikon "SHA256d"-merkillä, ja lohko katsotaan kelvolliseksi vain, jos tuloksena saatu hakkerointi on numeerisesti pienempi tai yhtä suuri kuin viitearvo, jota kutsutaan tavoitearvoksi. Kysymys kuuluukin: mistä tämä tavoitearvo tulee ja miten järjestelmä varmistaa, että se pysyy ajan mittaan johdonmukaisena?



Bitcoin:n tavoitteena on, että keskimäärin yksi lohko löydetään 10 minuutin välein. Tätä tahtia ei tietenkään voida taata sekunnin tarkkuudella. Käytännössä jotkut lohkot löytyvät muutaman sekunnin kuluttua edellisestä, kun taas toiset löytyvät yli tunnin kuluttua. Tärkeintä on keskiarvo riittävän pitkältä ajanjaksolta.



![Image](assets/fr/019.webp)



Tämä vaihtelu johtuu mining:n todennäköisyysluonteesta: jokainen hash on itsenäinen yritys, jonka tuloksen jääminen tavoitteen alapuolelle on vakiotodennäköistä (olettaen, että tavoite pysyy muuttumattomana). Sitä voidaan siis verrata arpajaisiin, joissa on jatkuva arvonta: mitä enemmän hasheja louhijat tekevät sekunnissa, sitä lyhyempi on odotettavissa oleva viive ennen kelvollisen lohkon ilmestymistä, mutta satunnaisuutta ei kuitenkaan koskaan poisteta arvonnasta toiseen.



### Miksi pyrkiä 10 minuuttiin harkkojen välillä?



Vaikka tästä ei ole todisteita, Satoshi Nakamoto valitsi varmasti 10 minuuttia käytännölliseksi kompromissiksi tehokkuuden ja turvallisuuden välillä. Lyhyempi aikaväli antaisi tiheämpiä vahvistuksia, mutta aiheuttaisi enemmän väliaikaisia verkon hajoamisia. Tämän asian ymmärtämiseksi on palattava takaisin lohkon etenemistapaan.



Kun louhija löytää kelvollisen lohkon, hän jakaa sen välittömästi vertaisilleen. Sitä vastaanottavat solmut tarkistavat sen pätevyyden (transaktiot, proof of work, konsensussäännöt jne.) ja välittävät sen sitten vuorollaan eteenpäin. Tämä leviäminen vie tietyn ajan, jota rajoittaa internetin viive, kaistanleveys ja kunkin solmun kyky tarkistaa lohko.



![Image](assets/fr/020.webp)



Jos tämän diffuusioviiveen aikana toinen louhija löytää myös kelvollisen lohkon samalla korkeudella, verkko voi jakautua väliaikaisesti: yksi osa solmuista ja louhijoista luottaa lohkoon A, kun taas toinen osa luottaa lohkoon B. Tämä on verkon väliaikainen jako.



![Image](assets/fr/021.webp)



Nämä erot eivät ole katastrofaalisia. Nakamoto-konsensus ennustaa, että pitkällä aikavälillä vain yksi haara voittaa: se, joka kerää eniten työtä. Heti kun uusi lohko louhitaan esimerkiksi lohkon A päälle, koko verkko synkronoituu uudelleen tähän haaraan ja hylkää lohkon B, josta tulee "*[stale-lohko](https://planb.academy/resources/glossary/stale-block)*", jota arkikielessä kutsutaan joskus virheellisesti "*orphan-lohkoksi*".



![Image](assets/fr/022.webp)



Toisaalta niillä on hintansa: muutaman minuutin ajan murto-osa kaivostyöläisistä työskentelee oksalla, joka hylätään. Tämä työ on sitten hukkaan heitettyä yleisen turvallisuuden kannalta, koska se ei ole edistänyt lopullisen ketjun muodostumista. Mitä nopeampi on lohkojen välinen aika, sitä suurempi on tällaisten jakojen todennäköisyys, koska etenemisajan osuus lohkojen välisestä ajasta on suurempi.



Kymmenen minuutin aikaväli antaa yleensä voittaneelle lohkolle riittävästi aikaa levitä laajalle ennen kuin samalle korkeudelle löydetään kilpaileva lohko. Tämä on kompromissi, joka rajoittaa jakoja, vähentää laskentatehon tuhlausta ja auttaa verkkoa pysymään synkronoituna maailmanlaajuisessa mittakaavassa.



### hashrate:n ymmärtäminen



*'[Hashrate](https://planb.academy/resources/glossary/hashrate)*' tarkoittaa sekunnissa tuotetun hash-laskennan määrää, olipa kyseessä sitten yksittäinen louhija, louhijaryhmä tai kaikki Bitcoin:n louhijat. Se ilmaistaan muodossa "H/s" (hasheja sekunnissa) ja sen kertoimina "TH/s" (terahashia sekunnissa) tai "EH/s" (exahashia sekunnissa). Tämä tarkoittaa sitä, kuinka monta yritystä louhijat voivat tehdä sekunnissa yrittäessään saada tavoitetta alhaisemman hash-arvon.



Jos kohde pysyy kiinteänä, niin:




- jokaisella yrityksellä on kiinteä onnistumisen todennäköisyys;
- useamman yrityksen tekeminen sekunnissa lisää todennäköisyyttä, että voittoyritys ilmestyy nopeasti


Toisin sanoen, jos huomenna Bitcoin-verkko kaksinkertaistaa laskentatehonsa liittämällä yhteen kaksi kertaa enemmän mining-koneita, lohkot löytyisivät ilman korjausmekanismia keskimäärin kaksi kertaa nopeammin. Tavoitetta on siis mukautettava hashrate-vaihteluiden kompensoimiseksi.



### Vaikeustavoitteen säätäminen



Bitcoin ratkaisee tämän ongelman ajoittaisella kohteen säätömekanismilla, joka säätää mining:n [vaikeusastetta](https://planb.academy/resources/glossary/difficulty-adjustment). Periaate on seuraava: vuoden 2016 lohkojen välein (noin kahden viikon välein) kukin solmu laskee vaikeustavoitteen uudelleen tarkkailemalla, kuinka paljon aikaa näiden vuoden 2016 lohkojen tuottamiseen todella kului.



Tämän mekanismin tavoitteena on lyhentää lohkon keskimääräistä tuotantoaikaa noin 10 minuuttiin, kun verkon hashrate-verkko muuttuu jatkuvasti, koska koneita poistetaan käytöstä tai päinvastoin uusia koneita lisätään.



![Image](assets/fr/023.webp)



Laskelma perustuu kuluneen ajanjakson havaittuun aikaan:




- jos vuoden 2016 viimeiset lohkot löydettiin liian nopeasti, tämä tarkoittaa, että hashrate kasvoi tällä kaudella; Bitcoin vaikeuttaa tilannetta alentamalla seuraavan kauden tavoitetta;
- jos vuoden 2016 lohkot löydettiin liian hitaasti, tämä tarkoittaa, että hashrate on vähentynyt; Bitcoin helpottaa tilannetta lisäämällä tavoitetta.



Kaava on seuraava:



```txt
Tn = To * (Ta / Tt)
```



Kanssa:




- `tn`: uusi kohde
- `to`: vanha kohde
- `Ta`: kulunut reaaliaika viimeisten 2016 lohkon osalta
- `Tt`: tavoiteaika (sekunteina)



Tavoiteaika on kaksi viikkoa eli `Tt = 1 209 600` sekuntia:



```txt
Tn = To * (Ta / 1 209 600)
```



Jotta ymmärtäisit, miten Bitcoin mining:n vaikeusastetta voidaan säätää, tässä on esimerkki kuvitteellisista arvoista:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Kanssa:



- `**To = 18,045,755,102**`: Vanha tavoite eli viitearvo ennen oikaisua.
- `**ta = 1 000 000 sekuntia**`: Viimeisen 2016 lohkon tuottamiseen käytetty aika. Koska tämä aika on pienempi kuin tavoiteaika, verkko on louhinut liian nopeasti.
- `**1,209,600 sekuntia**`: Tavoiteaika, joka vastaa 10 minuuttia lohkoa kohti vuoden 2016 lohkoissa ja jota käytetään vertailukohtana säätöä varten.
- `**tn = 14,918,779,020**`: Uusi tavoite on laskettu vaikeusasteen mukautuksen jälkeen.



Tässä tapauksessa uusi tavoite on alhaisempi kuin vanha, mikä tarkoittaa, että mining:stä tulee kovempi, jotta lohkotuotantoa voidaan hidastaa seuraavalla kaudella.


*Tämän esimerkin tavoitearvot on yksinkertaistettu ja skaalattu opetustarkoituksiin; Bitcoin:ssa käytetty todellinen tavoite on 256-bittinen kokonaisluku, joka on aivan eri suuruusluokkaa.*



Kukin solmu suorittaa tämän laskennan paikallisesti lohkoihin syötettyjen aikaleimojen perusteella. Koska kaikki solmut soveltavat samoja sääntöjä, ne päätyvät samaan tulokseen, ja uudesta tavoitteesta tulee yhteinen viite seuraaville vuoden 2016 lohkoille.



Tähän säätöön liittyy yksi tärkeä yksityiskohta: **Se on rajoitettu**. Bitcoin rajoittaa vaikeusasteen vaihtelua jaksoittain, jotta vältettäisiin liian äkilliset muutokset, jotka voisivat estää sen. Itse asiassa huomioon otettava todellinen aika on rajoitettu pysymään alueella, joka vastaa 4-kerrointa (vähintään neljännes vanhasta tavoitteesta, enintään nelinkertainen vanhaan tavoitteeseen verrattuna). Näin estetään äärimmäinen uudelleenkohdennus, jos aikaleimat ovat hyvin epätyypillisiä tai niitä on manipuloitu.



Huomattakoon myös, että todellisuudessa Bitcoinin vaikeustason säätö ei ole täysin tarkka. Olemme nähneet, että vaikeustaso on tarkoitus laskea uudelleen joka 2016. lohkon kohdalla vertaamalla todellista kulunutta aikaa 14 päivän tavoiteaikaan (2016 × 10 minuuttia). Satoshin alkuperäinen koodi sisältää kuitenkin niin kutsutun "*off-by-one*"-virheen: sen sijaan, että se mittaisi kunkin jakson viimeisten lohkojen välisen ajan (eli 2016 aikaväliä), se mittaa ensimmäisen ja viimeisen lohkon välisen ajan, mikä on vain 2015 aikaväliä. Käytännössä vaikeustaso lasketaan ikään kuin jakso sisältäisi vain 2015 lohkoa 2016:n sijaan. Seurauksena on, että vaikeustaso on järjestelmällisesti hieman yliarvioitu, mikä tarkoittaa, että lohkoja louhitaan keskimäärin hieman hitaammin kuin tavoitellut 10 minuuttia (noin 0,05 % hitaammin). Tämä bugi on tunnettu, mutta sitä ei ole koskaan korjattu, koska sen muuttaminen vaatisi kovan haarautumisen (hard fork) ja sen vaikutus on käytännössä merkityksetön, lukuun ottamatta teoreettista "*time warp*" -hyökkäystä.

### Tavoiteedustus



Kohde ei näy lohko-otsakkeessa täydessä 256-bittisessä muodossaan, koska se veisi liikaa tilaa. Sen sijaan 32-bittinen `nBits`-kenttä koodaa kohteen kompaktissa muodossa, joka on verrattavissa tieteelliseen merkintätapaan 256: eksponentti (1 tavu) ja kerroin (3 tavua). Täydellinen kohde rekonstruoidaan sitten näistä kahdesta arvosta. Emme mene tässä yksityiskohtiin, koska aihe on suhteellisen monimutkainen eikä se lisää mining:n ymmärtämistä. Muistakaa vain, että kohdetta ei tallenneta raakamuodossa lohko-otsikkoon, vaan kompaktissa muodossa.



Tässä ensimmäisen osan viimeisessä luvussa olemme käyneet läpi, miten proof-of-work toimii Bitcoin:ssä: louhija rakentaa ehdokaslohkon valitsemalla transaktioita mempoolistaan, laskee ehdokaslohkon otsikon, hashaa sen, vertaa tuloksena saatua hashia jaksotavoitteeseen ja aloittaa sitten alusta muuttamalla noncea, kunnes saadaan pätevä hash. Lopuksi verkko laskee 2016 lohkon välein uuden tavoitteen uudelleen, jotta keskimääräinen aika lohkoa kohden pysyy noin 10 minuutissa hashrate:n jatkuvista vaihteluista huolimatta.




# Bitcoin mining kannustinjärjestelmä


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Kuten voitte kuvitella, Bitcoin mining ei ole epäitsekästä toimintaa. Miner:llä on todellisia kustannuksia: sähköä mining-tietokoneidensa käyttämiseen, erikoislaitteiden hankkimista, huoltopalkkoja, joskus tiloja ja jäähdytysjärjestelmiä. Jotta Bitcoin-järjestelmä toimisi, louhijoiden yksityisten etujen on oltava linjassa verkon kollektiivisten etujen kanssa. Juuri tämä on mining-palkkion tehtävä. Se kannustaa louhijoita investoimaan proof of work:een, sisällyttämään siihen päteviä transaktioita ja noudattamaan protokollan sääntöjä sen sijaan, että he yrittäisivät korruptoida sitä.



Tämä logiikka perustuu peliteoriaan: protokolla tekee rehellisyydestä järkevää. Louhija ansaitsee rahaa, kun hän tuottaa kelvollisen lohkon, jonka solmut hyväksyvät. Jos hän sitä vastoin yrittää huijata, solmut hylkäävät hänen lohkonsa, eikä hän saa mitään. Koska lohkon tuottaminen maksaa, hylätty lohko on suora tappio. Kilpailuympäristössä, jossa tuhannet pelaajat etsivät samanaikaisesti kelvollisia lohkoja, kannattavin strategia on useimmiten noudattaa sääntöjä tarkasti ja maksimoida tulot rehellisesti.



Tämän saavuttamiseksi Bitcoin-protokollassa määrätään, että louhija, joka löytää kelvollisen lohkon, voittaa oikeuden sisällyttää siihen tietyn transaktion, jolloin louhija saa tietyn summan BTC. Tämä tunnetaan nimellä **[lohkopalkkio](https://planb.academy/resources/glossary/block-reward)**. Tämän osion ensimmäisessä luvussa pyritään ymmärtämään, mistä se koostuu ja miten se määräytyy. Myöhemmin näemme, miten rahanluontiosuus kehittyy ajan myötä (halvingien avulla) ja miten se itse asiassa kerätään teknisesti (coinbase-tapahtuman kautta).



### Mistä korttelipalkkio koostuu?



Edellisissä luvuissa näimme, miten louhijat onnistuvat löytämään kelvollisen lohkon. Kun louhija on löytänyt otsikon, jonka hash on pienempi kuin tavoite, hänen lohkoehdokkaansa katsotaan kelvolliseksi. Sen jälkeen hän voi jakaa sen koko Bitcoin-verkkoon. Lohko lisätään muuhun lohkoketjuun, jolloin sen sisältämät transaktiot vahvistetaan.



Juuri tämä tapahtuma (lohkon varsinainen lisääminen lohkoketjuun) käynnistää palkkion antamisen voittaneelle louhijalle. Tämä palkkio koostuu kahdesta eri elementistä, jotka lasketaan yhteen:




- [lohkotuki](https://planb.academy/resources/glossary/block-subsidy)**;
- transaktiomaksut**.



![Image](assets/fr/024.webp)



Katsotaanpa, mitä nämä kaksi palkkion osaa vastaavat.



### Ryhmätuki



Lohkotuki vastaa palkkion rahallista luomisosuutta. Kun louhija tuottaa kelvollisen lohkon, protokolla valtuuttaa hänet luomaan tietyn määrän uusia bitcoineja ja jakamaan ne itselleen palkkiona. Nämä bitcoinit luodaan ex nihilo. Niitä ei ollut olemassa aiemmin.



Uusien bitcoinien määrä ei kuitenkaan ole mitenkään sattumanvarainen. Se on tiukasti määritelty Bitcoin-protokollan säännöissä, ja se on sama kaikille louhijoille. Tarkastelemme tätä mekanismia tarkemmin seuraavassa luvussa, sillä tuki ei ole loputtomiin kiinteä arvo: se jaetaan määräajoin tarkan aikataulun mukaan. Muista toistaiseksi vain tämä:




- ryhmäavustus on toinen ryhmäpalkkion kahdesta osasta;
- se on rajattu, ja sen määrittää protokolla, ei louhija (vaikka louhija voi teknisesti pyytää maksimimäärää pienempää määrää);
- se luo bitcoineja tyhjästä.



Tällä tuella on kaksi päätehtävää Bitcoin-pöytäkirjassa. Ensimmäinen tehtävä on kannustaa pelaajia osallistumaan mining:een. Bitcoin:n alkuvuosina (ja joskus vielä nykyäänkin) transaktiomaksut olivat hyvin alhaiset. Tuki on siis taannut riittävän korvauksen, joka houkuttelee louhijoita ja ylläpitää järjestelmän turvallisuustasoa.



Toinen rooli liittyy valuutan jakeluun. Mikä tahansa uusi valuutta joutuu miettimään, miten rahayksiköt jaetaan oikeudenmukaisesti väestölle. Lohkoavustus tarjoaa ratkaisun tähän ongelmaan. Luomalla bitcoineja mining:n avulla se mahdollistaa niiden alustavan jakelun avoimella ja neutraalilla tavalla: kuka tahansa voi saada niitä, kunhan hän osallistuu mining:een, ilman ennakkolupaa tai tunnistamista.



Toisaalta, koska bitcoinit luodaan tyhjästä, niiden arvo ei ole vailla perustaa. Lisäämällä liikkeessä olevan rahan määrää tuki laimentaa mekaanisesti olemassa olevien bitcoinien arvoa. Näin ollen se johtaa eräänlaiseen rahan inflaatioon. Näemme kuitenkin seuraavassa luvussa, että tämän tuen on määrä kadota vähitellen ja että inflaatio loppuu lopulta.



![Image](assets/fr/025.webp)



### Transaktiomaksut



Lohkopalkkion toinen osa liittyy järjestelmän käyttöön: kun käyttäjä lähettää tapahtuman, hän haluaa, että se vahvistetaan. Lohkotilaa on kuitenkin rajoitetusti, ja lohkoja ilmestyy keskimäärin vain noin 10 minuutin välein. Lohkotila on siis niukka resurssi. Kun kysyntä ylittää tarjonnan, hinta nousee: tämä on transaktiopalkkiomarkkina. Jokainen louhija, joka onnistuu tuottamaan kelvollisen lohkon, saa oikeuden kerätä omaan lukuunsa kaikki transaktiomaksut, jotka liittyvät kaikkiin hänen lohkoonsa sisältämiinsä transaktioihin.



Voit ajatella sitä huutokauppajärjestelmänä: jokainen transaktio ehdottaa maksun määrää, ja kaivostyöläiset priorisoivat ne, jotka maksimoivat heidän tulonsa tilan rajoitteiden puitteissa. Tämä mekanismi sovittaa edut luonnollisesti yhteen:




- kiireiset käyttäjät maksavat enemmän saadakseen sen mukaan nopeasti;
- louhijoita kannustetaan sisällyttämään mukaan transaktioita, jotka maksavat korkeimmat maksut lohkotilasta.
- verkko välttää roskapostia, koska tapahtuman julkaiseminen maksaa.



#### Miten transaktiomaksut lasketaan?



Toisin kuin yleisesti luullaan, maksut eivät ole Bitcoin-tapahtuman tuotos. Itse asiassa transaktio kuluttaa panoksia ja luo tuotoksia. Panokset edustavat käytettyjen bitcoinien lähdettä, kun taas tuotokset edustavat maksujen määränpäätä. Transaktiomaksut ovat yksinkertaisesti **kokonaispanosten ja kokonaistuotosten välinen erotus**.



Toisin sanoen käyttäjän bitcoin-panokset, jotka kuuluvat hänelle, luovat tuotoksia vastaanottajille, mutta eivät tuota koko summaa, jonka panokset kuluttavat. Näiden kahden erotus edustaa transaktiopalkkioita, jotka louhija voi kerätä.



Otetaanpa esimerkki. Transaktio kuluttaa kaksi panosta, joista toinen on 100 000 sats ja toinen 150 000 sats, ja tuottaa kolme tuotosta, jotka ovat 35 000 sats, 42 000 sats ja 170 000 sats.



![Image](assets/fr/027.webp)



Panosten summa on siis 250 000 sats ja tuotosten summa 247 000 sats. Tämä tarkoittaa, että 3 000 sats` on kulutettu panoksina ilman, että niitä on luotu uudelleen tuotoksina: tämä määrä vastaa tässä liiketoimessa ehdotettuja maksuja.



![Image](assets/fr/028.webp)



Jos louhija sisällyttää tämän transaktion kelvolliseen lohkoon, hänellä on oikeus saada takaisin nämä 3000 sats` kaikkien muiden lohkoon sisältyvien transaktioiden palkkioiden lisäksi. Maksun maksavan transaktion ja louhijan tosiasiallisesti keräämän sats:n välillä ei kuitenkaan ole suoraa yhteyttä. Teknisesti ottaen 3000 sats`:n suuruiset palkkiot tuhotaan, ja vastineeksi louhija saa oikeuden luoda saman summan uudelleen itselleen.



#### Maksusuhde



Lohkoa ei rajoita transaktioiden määrä, vaan sen kokonaiskapasiteetti (nykyään käytännössä lohkon paino). Jotkin transaktiot vievät enemmän tilaa kuin toiset: transaktio, jossa on monia tuloja ja lähtöjä, on suurempi kuin yksinkertainen transaktio, jossa on yksi tulo ja kaksi lähtöä. Myös käytetyt skriptit vaikuttavat kokoon.



![Image](assets/fr/026.webp)



Kaksi transaktiota voi siis maksaa absoluuttisesti saman verran maksuja, mutta ne eivät ole taloudellisesti samanarvoisia louhijan näkökulmasta. Jos toinen on kaksi kertaa suurempi, se maksaa kaksi kertaa enemmän tilaa lohkossa. Tilaa on niukasti, joten louhija pyrkii maksimoimaan tulonsa tilayksikköä kohden.



Tämän vuoksi käytännössä transaktion kilpailukyky ilmaistaan maksujen suhteella, joka on yleensä sats/vB ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) per virtuaalinen tavu). Tämän suhdeluvun laskeminen on yksinkertaista:



```text
fee rate = fee / weight (in vB)
```



Jos esimerkiksi transaktio painaa 141 vB ja siihen kohdistuu 1 974 sats maksua, sen maksuprosentti on 14 sats/vB.



```text
1 974 / 141 ≈ 14 sats/vB
```



Tämä suhde selittää louhijoiden tekemät taloudelliset valinnat: kiinteällä kapasiteetilla korkeahintaisten transaktioiden sisällyttäminen maksimoi lohkon kokonaispalkkiot ja siten louhijan korvauksen. Se selittää myös sen, miksi edulliset transaktiot pysyvät jonossa mempoolissa pitkiä aikoja: ne kilpailevat muiden transaktioiden kanssa, jotka maksavat enemmän tilaa kohden.



### Verkon suojaus roskapostia vastaan



Maksuilla on myös toiminnallinen turvallisuustarkoitus: ne lisäävät kustannuksia tapahtumien moninkertaistamiseen. Jos transaktion julkaiseminen olisi ilmaista, verkko olisi helppo täyttää turhilla transaktioilla ja mempoolit täyttyisivät, mikä lisäisi solmujen kuormitusta.



Käytännössä solmut soveltavat paikallisia välityskäytäntöjä (mempool-sääntöjä) ja asettavat usein vähimmäismaksukynnyksen, jonka alittuessa ne eivät välitä tapahtumaa (oletusarvo on `0.1 sat/vB` Bitcoin Core:ssa `minRelayTxFee`:n kautta). Transaktio voi olla konsensussääntöjen tiukassa mielessä pätevä, mutta useimmat solmut eivät välitä sitä, jos sen maksut ovat liian alhaiset. Tämän seurauksena se ei kierrä, ei saavuta louhijoita ja sillä on hyvin pienet mahdollisuudet tulla vahvistetuksi.



Tässä vaiheessa olet ymmärtänyt lohkopalkkion ytimen: se vastaa voittaneelle louhijalle maksettavaa korvausta, ja se koostuu kahdesta eri elementistä. Yhtäältä protokollan sääntöjen määrittelemästä lohkotuesta, joka luo uusia bitcoineja ex nihilo. Toisaalta louhittuun lohkoon sisältyvien transaktioiden maksut.



Seuraavassa luvussa keskitymme tarkemmin lohkotukeen, jotta ymmärtäisimme tarkkaan, miten se lasketaan ja miten se kehittyy ajan mittaan Bitcoin-pöytäkirjan sääntöjen mukaisesti.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Edellisessä luvussa näimme, että louhijat, jotka tuottavat kelvollisen lohkon, saavat palkkion, joka koostuu lohkoon sisältyvien transaktioiden maksuista sekä lohkotuesta. Emme kuitenkaan ole vielä selittäneet, miten tämän tuen määrä määräytyy. Mekanismi, joka määrittää ja kehittää tätä arvoa, tunnetaan nimellä ***[halving](https://planb.academy/resources/glossary/halving)***.



### Mitä on puolitus?



Halving on Bitcoin-protokollaan ohjelmoitu tapahtuma, joka puolittaa lohkotuen eli uusien bitcoinien enimmäismäärän, jonka voittava louhija saa luoda jokaisella lohkolla. Se ei vaikuta transaktiomaksuihin: maksut ovat olemassa itsenäisesti ja määräytyvät edelleen käyttäjien aktiivisuuden ja lohkotilasta käytävän kilpailun perusteella.



Kun Bitcoin käynnistettiin vuonna 2009, lohkotuki oli 50 BTC kutakin louhittua lohkoa kohti. Sen jälkeen tämä tuki on puolitettu useita kertoja jokaista puolitusta kohden.



![Image](assets/fr/029.webp)



Halving ei käynnisty päivämäärän vaan lohkon korkeuden perusteella. Se suoritetaan **joka 210 000 lohkon välein**. Koska Bitcoin:n tavoitteena on noin 10 minuutin keskimääräinen aikaväli lohkoa kohti, 210 000 lohkoa vastaa noin neljää vuotta.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Näin ollen, jos huomioidaan, että `n` on jo toteutuneiden puolikkaiden lukumäärä, lohkotuki BTC:ssä voidaan laskea seuraavasti:



```text
subsidy(n) = 50 / 2^n
```



### Aiemmat puolikkaat



Seuraavassa on yhteenvetotaulukko jo tapahtuneista puolittamisista, niiden lohkokorkeudesta, päivämäärästä ja tapahtuman jälkeen sovellettavasta uudesta lohkotuesta:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Milloin ja miten tuki päättyy?



Halving toistetaan niin kauan kuin tuki voidaan ilmaista järjestelmän vähimmäisyksikkönä: satoshi.



```text
1 BTC = 100 000 000 sats
```



Kun tuki puolitetaan, saavutamme lopulta niin pieniä bitcoinin murto-osia, että niistä tulee alle 1 satoshi. Tässä vaiheessa ei ole enää mahdollista luoda puolta satoshi-yksikköä. Rahan luominen lohkotuen avulla loppuu, ja louhijoille maksetaan korvaus ainoastaan transaktiomaksujen perusteella. Tästä lähtien kaikki bitcoinit ovat liikkeessä, eikä uusia yksiköitä ole enää mahdollista tuottaa.



Lohkotukien lopullinen päättyminen tapahtuu lohkotasolla 6,930,000 eli 33. ja viimeisellä puolittamiskerralla. Tämän tapahtuman odotetaan tapahtuvan vuoden 2140 tienoilla, vaikka tarkkaa päivämäärää on mahdotonta sanoa, koska se riippuu siitä, kuinka nopeasti lohkoja todella löytyy tähän mennessä.



Koska lohkotuki noudattaa geometrista jaksoa, jonka suhde on 1/2 jokaisella puolittumisella, rahanluonti oli Bitcoin:n alkuaikoina erittäin suurta ja väheni sitten hyvin nopeasti. Seitsemänteen puolitukseen mennessä yli 99 prosenttia bitcoineista on jo laitettu kiertoon. 99 prosentin rajan odotetaan ylittyvän vuosien 2032 ja 2036 välillä. Tämä tarkoittaa, että viimeisen 1 prosentin bitcoinien louhimiseen kuluu yli 100 vuotta. Vaikka rahan inflaatio oli Bitcoin:n lanseerauksen aikaan hyvin korkea, jotta valuutan levittäminen olisi mahdollista, se on nyt hyvin alhainen ja laskee edelleen, kunnes se saavuttaa todellisen kovan valuutan tason, jonka kiertävä tarjonta ei voi enää kasvaa.



![Image](assets/fr/030.webp)



### Miksi BTC:ää ei koskaan valmisteta 21 miljoonaa kappaletta?



Bitcoin:n rahamääräinen enimmäistarjonta esitetään usein 21 miljoonana BTC:na. Tämä on hyvä likiarvo sen rahapolitiikan ymmärtämiseksi, mutta puhtaasti teknisestä näkökulmasta katsottuna kokonaistarjonta ei koskaan saavuta täsmälleen 21 000 000 bitcoinia.



Tärkein syy on mekaaninen. Peräkkäisten puolikkaiden kautta lohkotuki putoaa lopulta alle 1 prosentin vähimmäisarvon, jolloin liikkeeseenlasku päättyy ennen kuin se saavuttaa tarkan teoreettisen kokonaismäärän. Tämän vähimmäisrakeisuuden ja pyöristyssääntöjen vuoksi tukien avulla luotujen bitcoinien kokonaismäärä on hieman alle 21 miljoonaa.



Lisäksi vähäiset protokollaan liittyvät poikkeamat voivat myös lisätä tätä. Esimerkiksi harvinaisissa tapauksissa jotkut louhijat eivät ehkä ole hakeneet täyttä tukeaan, mikä vähentää lopullisesti todellisuudessa liikkeeseen laskettujen bitcoinien määrää. Voimme myös mainita Satoshi:n 3. tammikuuta 2009 tuottaman [genesis-lohkon](https://planb.academy/resources/glossary/genesis-block), jonka luomat bitcoinit eivät kuulu [UTXO set](https://planb.academy/resources/glossary/utxo-set):ään, sekä tietyt vikoihin liittyvät historialliset tapahtumat, kuten päällekkäiset coinbase-transaktiotunnukset.



Lopuksi on otettava huomioon myös kaikki bitcoinit, jotka on tuhottu tai estetty:




- bitcoineja lukittuna ratkaisemattomiin skripteihin;
- gW-219-skriptien tarkoituksellisesti tuhoamat;
- tai yksityisten avainten katoaminen sovellustasolla.



Teoriassa Bitcoin:n tarjonta on siis rajoitettu 21 miljoonaan. Käytännössä liikkeessä ei kuitenkaan koskaan ole 21 miljoonaa bitcoinia.



## Coinbase-tapahtuma


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Edellisissä luvuissa esitimme kaksi tärkeää seikkaa. Ensinnäkin louhija, joka onnistuu tuottamaan ja jakamaan kelvollisen lohkon, saa palkkion. Toisaalta näimme, että tämä palkkio koostuu kahdesta eri elementistä:




- lohkotuki (ex nihilo luotuja bitcoineja, joiden enimmäismäärä on protokollan asettama ja vähitellen pienenevä puolittamalla);
- kaikki transaktiomaksut, jotka ovat maksaneet käyttäjät, joiden transaktiot on sisällytetty lohkoon.



Yksi kysymys on kuitenkin vielä avoinna: millä mekanismilla kaivosmies kerää tämän palkkion Bitcoin:ssä? Juuri tämä on tietyn "coinbase"-nimisen transaktion rooli.



### Miten coinbase-transaktio toimii



Kuten kurssin ensimmäisessä osassa nähtiin, jokainen Bitcoin-lohko sisältää luettelon vireillä olevista transaktioista, jotka se vahvistaa. Näistä ensimmäinen on aina [coinbase-tapahtuma](https://planb.academy/resources/glossary/coinbase-transaction). Sen avulla voittava louhija voi saada palkkionsa.



![Image](assets/fr/031.webp)



Ensi silmäyksellä se näyttää klassiselta Bitcoin-transaktiolta: sillä on [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), lähdöt ja se sisältyy lohkon Merkle-puuhun. Se eroaa kuitenkin yhdestä tärkeästä seikasta: se ei käytä mitään olemassa olevaa UTXO-tapahtumaa.



Klassisessa Bitcoin-tapahtumassa "syötteet" viittaavat aiempiin käyttämättömiin tuotoksiin (UTXO:t), joista saadaan syöttöarvo. Tämän jälkeen tuotokset jakavat tämän arvon uudelleen uusille UTXO:ille, joilla on uudet käyttöehdot. Toisin sanoen, jotta voit lähettää bitcoineja, sinun on jo omistettava ne. Coinbase-tapahtuma ei sen sijaan kuluta bitcoineja panoksena: se luo bitcoineja tuotoksena suoraan tyhjästä.



Juuri tämä mekanismi mahdollistaa uusien bitcoinien tuomisen liikkeeseen lohkotuen avulla ja hyvittää louhijalle lohkoon sisältyviin transaktioihin liittyvät maksut. Coinbase-transaktio ei voi viitata todelliseen olemassa olevaan UTXO:ään (itse asiassa se viittaa kuvitteelliseen UTXO:ään), koska sen tehtävänä on nimenomaan luoda osa arvosta (tuki) ja periä toinen osa (maksut) takaisin ilman, että se saa niitä aiemmasta transaktiosta. Jotta koko järjestelmä pysyisi johdonmukaisena, maksuja vastaavan osuuden on täsmälleen vastattava niiden bitcoinien summaa, jotka on kulutettu panoksina mutta joita ei ole luotu uudelleen tuotoksina lohkon muissa transaktioissa.



![Image](assets/fr/032.webp)



Tämä tapahtuma ei ole vapaaehtoinen. Lohko, joka ei sisällä coinbase-transaktiota, on virheellinen, ja verkon solmut hylkäävät sen järjestelmällisesti.



⚠️ Huomaa: termi "*coinbase*" ei liity mitenkään samannimiseen vaihtopalveluun. Bitcoin:ssa "*coinbase*" viittaa historiallisesti transaktioon, joka luo lohkopalkkion. Yritys on yksinkertaisesti ottanut tämän termin käyttöönsä nimenä.



Coinbase-transaktiolla on itse asiassa useita tehtäviä samanaikaisesti:




- Ensimmäinen on se, jota juuri käsittelimme yksityiskohtaisesti: se osoittaa louhijalle palkkion, johon hän on oikeutettu kelvollisen lohkon tuottamisesta.
- Sen toinen, teknisempi tehtävä on ankkuroida kryptografinen sitoumus lohkoon sisältyvien SegWit-tapahtumien todistajiin (allekirjoituksiin).
- Kolmas rooli, joka ei tällä kertaa liity suoraan protokollaan mutta liittyy mining:n nykyaikaiseen teollistumiseen, on se, että kolikkopohjaa käytetään nykyään usein mielivaltaisten teknisten tietojen ankkuroimiseen. Nämä tiedot liittyvät yleensä mining-poolien toimintaan ja niiden sisäiseen organisaatioon.



Jotta ymmärtäisit nämä eri käyttötarkoitukset, tarkastelemme nyt tarkemmin coinbase-tapahtuman rakennetta.



### Coinbase-tapahtuman perusrakenne



Coinbase-tapahtuman on sisällettävä täsmälleen yksi panos. Yksinkertaisuuden vuoksi sanomme joskus, että sillä ei ole panosta, koska tämä panos ei kuluta todellista UTXO. Todellisuudessa panos, jolla on viitattu lähde, on olemassa, mutta se osoittaa tarkoituksella olemattomaan UTXO:een.



Kuten olemme jo nähneet, jokaisen Bitcoin-tapahtuman on käytettävä UTXO:aa syötteenä luodakseen kelvollisia tuotoksia. Bitcoin-transaktiossa tämä kulutus tapahtuu viittaamalla olemassa olevaan UTXO:een syötteenä. Viittaus tapahtuu yksinkertaisesti ilmoittamalla edellisen tapahtuman (jossa UTXO luotiin) tunniste sekä sen indeksi tämän tapahtuman tuotosten joukossa. Konkreettisesti UTXO määritellään hash-tunnisteella (edellinen TXID) ja indeksillä.



Mutta coinbase-tapahtuman tapauksessa sen sijaan, että viitattaisiin todelliseen olemassa olevaan UTXO:ään, syötteen on välttämättä osoitettava tähän väärennettyyn UTXO:ään, jonka TXID-tunnus on täynnä nollia ja joka ei vastaa mitään todellista TXID-tunnusta:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Suoraan sen jälkeen väärä indeksi:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Satoshi Nakamoto:ssä kuvatussa Bitcoin:n perusprotokollassa tämä väärä syöttö on ainoa rajoitus, joka asetetaan coinbase-tapahtumalle.



Kuten mihin tahansa UTXO:aan, johon viitataan tapahtuman syötteessä, se liittyy `scriptSig`-kenttään. Tavanomaisessa transaktiossa tämä `scriptSig`-kenttä sisältää elementit, joita tarvitaan `scriptPubKey`:n täyttämiseksi ja siten käytetyn UTXO:n lukituksen avaamiseksi. Mutta coinbasen tapauksessa, koska UTXO, johon viitataan, on tarkoituksellisesti kuvitteellinen, `scriptSig`-kenttä on täysin vapaa. Miner:n käyttäjät voivat siis syöttää haluamansa tiedot. Katsomme myöhemmin, miten tätä vapautta käytetään.


Tämän väärän syötteen lisäksi on yksi tai useampi täysin tavanomainen lähtö, jonka avulla louhija voi kerätä bitcoineja palkkiosta yhteen Bitcoin-osoitteistaan. Nämä tuotokset ovat UTXO-osoitteita, jotka on lukittu `scriptPubKey`:llä (esim. skripti, joka osoittaa louhijan tai poolin hallitsemaan osoitteeseen). Ainoa erityispiirre tässä on niiden arvon laskentasääntö: kolikkopohjan tuotosten kokonaissumma ei saa koskaan ylittää suurinta sallittua tukea, johon lisätään lohkomaksut.



Historiallisesti coinbase-transaktio on siis tiivistetty tähän yksinkertaiseen järjestelmään: väärennetty tulo, joka viittaa olemattomaan UTXO:een, ja yksi tai useampi lähtö, jonka tarkoituksena on jakaa lohkopalkkio voittavalle louhijalle. Nykyään coinbase ei kuitenkaan enää rajoitu tähän jakotehtävään. Sen erityinen asema lohkossa ja sen rakenteen suuri joustavuus ovat johtaneet uusiin käyttötapoihin sekä itse protokollassa että mining-poolin hallintamekanismeissa.



### Muut coinbase-käyttötarkoitukset



Ajan myötä coinbase-transaktiosta on tullut erityisen kätevä lisäyspiste, johon voidaan integroida erilaisia mining:n ja itse lohkorakenteen kannalta hyödyllisiä tietoja. Tutustutaanpa niihin, jotta ymmärtäisimme paremmin koko coinbase-organisaatiota.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) on fork-softa, joka otettiin käyttöön maaliskuussa 2013 alkaen lohkosta 227,930, jossa esiteltiin versio 2 Bitcoin-lohkoista. Tämä uusi versio edellyttää, että jokainen lohko sisältää coinbase-tapahtuman `scriptSigissä` luotavan lohkon korkeuden.



Toisaalta tämä kehitys selventää tapaa, jolla verkko suostuu kehittämään lohkorakennetta ja konsensussääntöjä. Toisaalta se varmistaa jokaisen lohkon ja coinbase-transaktion ainutlaatuisuuden.



Näin ollen coinbasen `scriptSig` ei ole täysin ilmainen. BIP-34:n aktivoinnista lähtien se on yksinkertaisesti rajoitettu aloittamaan sen lohkon korkeudella, johon tämä coinbase-tapahtuma sisältyy.



![Image](assets/fr/035.webp)



#### Extra-nonce



Kuten näimme tämän kurssin ensimmäisissä luvuissa, louhijalla on lohkon otsikossa 32-bittinen nonce-kenttä, jota hän muokkaa kokeilemalla ja erehtymällä löytääkseen hash-arvon, joka on pienempi tai yhtä suuri kuin tavoite. Tämä 32-bittinen alue mahdollistaa jo hyvin suuren määrän yhdistelmiä, mutta kun mining:n vaikeusaste on korkea, tämä alue voidaan käyttää kokonaan loppuun suhteellisen lyhyessä ajassa, eikä näin ollen välttämättä löydy yhtään yhdistelmää, joka tuottaisi kelvollisen hashin. Jos kaikki `nonce`:n mahdolliset arvot on testattu tuloksetta, louhijan on muutettava toista elementtiä lohkon otsikon muuttamiseksi ja aloitettava uusi sarja yrityksiä.



Koska coinbase-transaktio tarjoaa vapaan kentän sen syötteen "scriptSig"-kentän kautta, nonce-avaruuden laajentamiseen käytetään ratkaisua, jossa hyödynnetään osaa tästä "scriptSig"-kentästä. Tätä kutsutaan yleisesti ylimääräiseksi nonseksi. Muokkaamalla extra-noncea louhija muuttaa coinbasen `scriptSig`:iä eli transaktion tunnusta, sitten lohkon Merkle-juurta ja lopuksi itse lohkon otsikkoa. Näin he saavat uuden hakuavaruuden tutkittavaksi ilman, että heidän tarvitsee muuttaa lohkoehdokkaidensa muita osia.



![Image](assets/fr/036.webp)



#### Poolien ja louhijoiden tunnistaminen



Nykyään hyvin suuri osa maailman hashrate:stä on järjestetty mining-altaissa. Nämä rakenteet kokoavat yhteen yksittäisiä kaivostyöläisiä yhdistääkseen työnsä ja vähentääkseen tulojensa vaihtelua.



Toiminnallisista syistä mining-altaat käyttävät myös coinbase-syötteen `scriptSig`-kentän vapaata kenttää erilaisten tietojen lisäämiseen. Nämä tiedot vaihtelevat pooleittain ja verkkoprotokollasta toiseen, mutta yleensä niihin sisältyy kullekin louhijalle annettu yksilöllinen tunniste (usein ylimääräinen nonce, joka koostuu useista alaosista), jotta vältetään päällekkäinen työ poolin sisällä. Yleensä lisätään poolin tunniste, jota käytetään löydettyjen lohkojen julkiseen tunnistamiseen, mining-tilastoihin ja muihin seurantatarkoituksiin.



![Image](assets/fr/037.webp)



#### SegWit:n sitoutuminen



Siitä lähtien, kun SegWit soft fork otettiin käyttöön vuonna 2017, todistajatiedot (eli yleensä allekirjoitukset) on erotettu tapahtumien päätiedoista, erityisesti [Bitcoin-tapahtumien muokattavuusongelman](https://planb.academy/resources/glossary/malleability-transaction) korjaamiseksi. Tämä erottelu tuo siis lohkoon uuden elementin, joka on sidottava lohkoon.



Tätä varten todistajat ryhmitellään yhteen toiseen erityiseen Merkle-puuhun, jonka juuret siirretään sitten coinbase-transaktioon "OP_RETURN"-ulostulon kautta.



![Image](assets/fr/038.webp)



En käsittele tätä mekanismia tarkemmin tällä kurssilla, koska se ei kuulu tämän artikkelin piiriin, mutta muista, että SegWit:n käyttöönotosta lähtien coinbase-transaktio toimii välineenä, jonka avulla lohkoon ankkuroidaan sormenjälki, jossa on yhteenveto kaikista SegWit-todistajista. Todistajat sijoitetaan itsenäiseen Merkle-puuhun, tämän puun juuri kirjoitetaan coinbase-transaktion tulosteeseen, ja tämä coinbase-transaktio sisällytetään itse pää-Merkle-puuhun yhdessä kaikkien muiden transaktioiden kanssa, joiden juuri näkyy lohkon otsikossa. Näin todistajat, jotka on tallennettu erillään päätransaktiotiedoista, sitoutuvat edelleen lohkon otsikkoon.



![Image](assets/fr/039.webp)



#### Mielivaltaiset viestit



Koska `scriptSig` sallii kaivostyöläisen vapaasti lisätä haluamiaan tietoja, jotkut ovat käyttäneet tilaisuutta hyväkseen ja lisänneet teknisten viestien sijasta henkilökohtaisempia viestejä. Tunnetuin tapaus on tietysti Satoshi Nakamoto, jonka viesti on nykyään ikoninen:



> The Times 03/Jan/2009 Liittokansleri toisen pankkien pelastuspaketin partaalla

Tämä Genesis-lohkossa (Bitcoin:n ensimmäinen lohko) oleva viesti on itse asiassa koodattu heksadesimaalisessa muodossa coinbase-transaktion `scriptSig` -lohkossa:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Erääntymisaika


Kun lohko on louhittu ja jaettu, coinbase-tapahtuma näkyy lohkoketjussa kuten mikä tahansa muu tapahtuma. Se luo UTXO:t voittavalle louhijalle, jolloin hän voi noutaa palkkionsa. Nämä UTXO:t eivät kuitenkaan ole välittömästi käytettävissä: niihin sovelletaan [eräpäivää](https://planb.academy/resources/glossary/maturity-period). Tämä maturiteetti on asetettu 100 lohkoa kolikkopohjan sisältävän lohkon jälkeen. Konkreettisesti sanottuna coinbase-tapahtuman on siis saatava 101 vahvistusta, jotta voittanut louhija voi käyttää sen tuotokset.


![Image](assets/fr/040.webp)


Säännön tavoitteena on rajoittaa ketjujen uudelleenjärjestelyjen vaikutusta talouteen. Kuten aiemmissa luvuissa on todettu, voi käydä niin, että eri louhijat löytävät samalta korkeudelta lähes samanaikaisesti kaksi erilaista kelvollista lohkoa. Verkko voi hetkeksi jakautua: jotkin solmut saavat ensin lohkon A, kun taas toiset näkevät lohkon B ensin. Seuraavien lohkojen aikana jompikumpi haaroista kerää enemmän työtä ja siitä tulee referenssihaara. Toinen haara hylätään ja sen lohkot vanhentuvat. Sen sisältämät transaktiot voivat sitten teoriassa palata mempooleihin odottamaan vahvistusta.



Käytännössä näin tapahtuu harvoin, koska maksumarkkinoiden vuoksi lähes samat liiketoimet esiintyvät usein kahdessa kilpailevassa lohkossa samalla korkeudella. Tämä on yksi syy siihen, miksi Bitcoin-tapahtuman katsotaan yleisesti muuttumattomaksi kuuden vahvistuksen jälkeen: yli kuuden lohkon uudelleenjärjestelyt ovat niin epätodennäköisiä, että niitä voidaan kohtuudella pitää mahdottomina.



![Image](assets/fr/041.webp)



Näiden uudelleenjärjestelyjen ongelma coinbase-kaupan tapauksessa on se, että kyseessä ei ole tavallinen kauppa. Se tuo liikkeeseen aivan uusia bitcoineja. Jos lohkopalkkio voitaisiin käyttää välittömästi, voisi syntyä ongelmallinen kaskaditilanne:




- louhija käyttää bitcoineja kolikkopankista,
- nämä bitcoinit kiertävät taloudessa,
- sitten alkuperäinen kortteli lopulta hylättiin uudelleenjärjestelyn yhteydessä.



Silloin liikkeessä olevia bitcoineja ei olisi koskaan ollut olemassa lopullisessa ketjussa, ja sarja transaktioita, jotka olivat voimassa liikkeeseenlaskuhetkellä, muuttuisi jälkikäteen pätemättömiksi.



Erääntymisaika on niin pitkä, että tämä skenaario on epärealistinen. 101 lohkon uudelleenjärjestelyä pidetään käytännössä mahdottomana (vaikka sen todennäköisyys onkin äärettömän pieni). Emme tiedä tarkalleen, miksi Satoshi valitsi näin korkean arvon maturiteetille, mutta on todennäköistä, että se valittiin, jotta mekanismi pysyisi toimintakykyisenä myös suurten verkkohäiriöiden sattuessa.



Tämä sääntö estää äskettäin luotua lohkopalkkiorahaa alkamasta kiertää ennen kuin lohko, joka generated se on turvallisesti haudattu suuren määrän kertyneen työn alle.



---

Olemme nyt päässeet loppuun selityksessämme siitä, miten Bitcoin mining toimii. Sinulla pitäisi nyt olla selkeä kuva asiaan liittyvistä perusmekanismeista.



Kurssin viimeisessä osassa palaamme konkreettisempiin näkökohtiin ja näytämme, miten Bitcoin mining toteutuu todellisessa maailmassa: sen teollistaminen, käytetyt koneet, pelaajien ryhmittely ja niin edelleen. Tavoitteena on antaa sinulle kokonaiskuva Bitcoin mining:stä sekä juuri näkemästämme teoreettisesta ja protokollanäkökulmasta että sen käytännön ja toiminnallisesta puolesta.



# Bitcoin mining teollisuus


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## mining-koneiden kehitys


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Bitcoin:n alkuaikoina mining ei ollut teollista toimintaa. Se oli osa Bitcoin-ohjelmistoa, joka käynnistettiin henkilökohtaisella tietokoneella usein uteliaisuudesta, joskus verkon tukemiseksi ja toissijaisesti bitcoinien hankkimiseksi, joilla ei tuolloin ollut käytännössä mitään markkina-arvoa.



Vuosien mittaan tämä toiminta on muuttunut: koneet ovat muuttuneet, vaikeusaste on kasvanut räjähdysmäisesti, ja mining:sta on tullut oma teollisuudenalansa. Tarkastellaanpa Bitcoin mining:n toiminnallisia näkökohtia.



### Aloittaminen: mining suorittimen kanssa



Vuonna 2009 ja alkuvuosina mining:n käyttö suoritettiin pääasiassa tavanomaisen tietokoneen suorittimella. Bitcoin oli tuolloin vain yksinkertainen ohjelmisto, joka toimi wallet:nä, solmuna ja louhijana. Pelkkä Satoshi Nakamoto:n ohjelmiston käynnistäminen henkilökohtaisella tietokoneella riitti mining-prosessiin osallistumiseen ja monissa tapauksissa lohkojen löytämiseen.



Suoritin voi tehdä kaikkea, mutta sitä ei ole optimoitu mihinkään. Se suorittaa hyvin yleisiä ohjeita, joissa on monimutkainen logiikka. Lohkojen otsikoiden toistuvan hashingin kaltaiseen tehtävään se ei ole ihanteellinen työkalu, mutta verkon käynnistyksen yhteydessä vaikeusaste on niin alhainen, että se on enemmän kuin riittävä lohkojen löytämiseen.



Tämä ajanjakso on tärkeä, koska se muistuttaa meitä tärkeästä asiasta: proof of work ei ole riippuvainen tietystä laiteluokasta. Ratkaisevaa on kyky laskea hasheja nopeammin kuin muut tietyllä hinnalla. Heti kun tekninen etu ilmenee, se muuttuu automaattisesti taloudelliseksi eduksi. Absoluuttisesti tarkasteltuna on kuitenkin vielä nykyäänkin mahdollista yrittää löytää Bitcoin-lohkoja tavanomaisella suorittimella. Tähän lähestymistapaan on päätynyt esimerkiksi NerdMiner-projekti. Mahdollisuudet lohkon löytämiseen ovat käytännössä olemattomat, mutta todennäköisyys on silti äärettömän pieni.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Siirtyminen näytönohjaimiin



Pian louhijat ymmärsivät, että pullonkaulana ei ollut teho vaan kyky suorittaa valtava määrä samanlaisia operaatioita rinnakkain. Grafiikkasuorittimet (GPU) pystyivät juuri tähän. Alun perin näytönohjain oli suunniteltu suorittamaan samoja operaatioita suurilla tietomäärillä. Tämä arkkitehtuuri soveltui täydellisesti toistuvan hashhauksen kaltaiseen tehtävään: muutaman erittäin monipuolisen ytimen sijasta käytössä oli satoja ja jopa tuhansia yksiköitä, jotka pystyivät suorittamaan samoja ohjeita samanaikaisesti.



Vertailukelpoisella virrankulutuksella näytönohjain voi tuottaa paljon enemmän hasheja sekunnissa kuin suoritin. Samaan aikaan bitcoinilla oli vaihtokurssi dollariin nähden, sen arvo nousi ja vaihtofoorumeita ilmestyi. Siitä lähtien mining:n luonne alkoi muuttua. Kyse ei ollut enää vain osallistumisesta, vaan rahan ansaitsemisesta. Erikoiskokoonpanoja ilmestyi: useiden näytönohjainten ympärille rakennettuja koneita, joskus ilman näyttöä, joissa oli minimaalinen järjestelmä ja erikoistuneita ohjelmistoja, joiden ainoa tarkoitus oli louhia.



Tässä vaiheessa mining:n vaikeudet alkoivat räjähtää käsiin. Vuoden 2010 puolivälistä vuoden 2011 puoliväliin se kasvoi jopa tuhatkertaiseksi. Mekaanisesti erikoistuminen alkaa, aivan kuten teollistumisen alkuvaiheessa, ja tavallisilla käyttäjillä - jotka tyytyvät käyttämään Bitcoin-ohjelmistoa henkilökohtaisilla tietokoneillaan - on nyt vain hyvin pieni mahdollisuus löytää kelvollinen lohko.



![Image](assets/fr/044.webp)



*Lähde: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



GPU-aikakauden ja nykyaikaisen [ASIC](https://planb.academy/resources/glossary/asic)-aikakauden välissä oli välivaihe: FPGA:iden käyttö. FPGA on uudelleenohjelmoitava komponentti: se voidaan konfiguroida toteuttamaan suoraan tiettyyn laskentaan, tässä tapauksessa SHA256d:hen, tarkoitettu logiikkapiiri. Ajatuksena oli siirtyä vielä kauemmas yleiskäyttöisestä laitteistosta (CPU/GPU) energiatehokkuuden parantamiseksi. Pian FPGA-piireissä virtuaalisesti tehtyjä parannuksia sovellettaisiin kuitenkin fyysisesti itse siruihin: ASIC on tulossa.



### ASIC:n saapuminen



Viimeinen vaihe mining-laitteiston erikoistumisessa oli ASIC-piirien (*sovelluskohtaiset integroidut piirit*) ilmestyminen. ASIC on piirisiru, joka on suunniteltu yhtä tehtävää varten. Bitcoin mining:n tapauksessa tämä tehtävä on nimenomaan SHA256d:n suorittaminen suurimmalla mahdollisella nopeudella ja mahdollisimman energiatehokkaasti. Toisin kuin näytönohjainta, ASIC-piiriä ei käytetä pelien, 3D-renderöinnin tai tekoälyn suorittamiseen. Se on tarkoitettu vain hashing-laskentaan.



![Image](assets/fr/045.webp)



*Bitmainin valmistama ASIC S21 XP*



Tällä erikoistumisella on kaksi merkittävää seurausta:




- Ensimmäinen on suorituskyvyn ja tehokkuuden harppaus. Vertailukelpoisen sukupolven laitteissa ASIC tuottaa paljon enemmän hasheja sekunnissa kuin näytönohjain ja kuluttaa samalla vähemmän virtaa. Mining:sta ja näytönohjaimesta tuli nopeasti kilpailukyvytön: vaikka se toimi teknisesti, sähkökustannukset ylittivät useimmissa yhteyksissä odotettavissa olevat tuotot;
- Toinen on mallin muutos: investoinnit ovat siirtyneet pääasiassa teollisen luokan laitteistoihin. Mining:ssa on nyt kyse tähän tarkoitukseen suunniteltujen koneiden ostamisesta, niiden jatkuvasta virransyötöstä, jäähdytyksestä, huollosta ja vanhentumisesta. ASIC ei nimittäin ole taloudellisesti ikuinen: kun markkinoille tulee uusi, tehokkaampi sukupolvi, vanhoista koneista tulee yhä kannattamattomampia, vaikka ne pysyisivätkin toiminnassa.



Siitä lähtien emme enää puhu vain harrastuksesta. Kyse on alasta, jonka kilpailukyky riippuu yhtälöstä:




- sähkön hinta;
- laitekustannukset ja poistot;
- kyky jäähdyttää ja toimia laajassa mittakaavassa;
- koneen käytettävyys ja luotettavuus;
- viestinnän nopeus;
- jne.



### Mining maatilat



Yksittäinen kone voi louhia, mutta ryhmittelemällä satoja ja jopa tuhansia ASIC:n laitteita yhteen paikkaan jaamme kiinteät kustannukset, optimoimme logistiikan ja siirrymme lähemmäs erikoistunutta datakeskusmallia.



Yksinkertaisimmillaan [mining-farmi](https://planb.academy/resources/glossary/mining-farm) on rakennus (tai joukko kontteja), joka on täynnä ASIC-laitteita, jotka toimivat 24/7. Haasteena on nyt vakaiden toimintaolosuhteiden ylläpitäminen:




- tuottaa suuria määriä edullista ja vakaata sähköenergiaa;
- hallita lämpöä kuristumisen välttämiseksi, koska energiatiheys on huomattava;
- suodattaa pölyä, säätää kosteutta, puhdistaa;
- koneen suorituskyvyn reaaliaikainen seuranta (lämpötilat, laitteistovirheet, hashrate-pudotukset jne.).



![Image](assets/fr/043.webp)



*Yksi seitsemästä rakennuksesta, jotka on omistettu Bitcoin mining:lle Riot Platformsin Rockdalen tehtaalla lähellä Austinia, Texasissa. Tämä on omistettu erityisesti immersiolle mining*



Mining:n toimintaa ohjaavat nyt teolliset toimijat, joista osa on listattu pörssiin ja jotka rakentavat ja ylläpitävät erittäin suuria maatiloja. Näihin kuuluvat MARA Holdings (Nasdaq: `MARA`) ja Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Vaikka emme perehtyisikään kannattavuusmallien yksityiskohtiin, on tärkeää ymmärtää, miksi mining on saanut tämän muodon. Proof-of-work on kilpailumekanismi: todennäköisyys löytää lohko ja siten ansaita rahaa on verrannollinen siihen, kuinka suuren osan hashrate:stä otat käyttöön. Tämän seurauksena on jatkuvia paineita lisätä laskentatehoa, alentaa kustannuksia laskentayksikköä kohti ja rajoittaa tappioita. Tämän seurauksena ympäristöistä, joissa on halvempaa sähköä, jäähdytystä suosiva ilmasto tai runsas energiainfrastruktuuri, tulee luonnollisesti houkuttelevampia.



Mining Bitcoin on näin ollen kehittynyt alkuaikojen kenen tahansa ulottuvilla olleesta toiminnasta erikoislaitteiden ja ammattilaisten harjoittaman toiminnan hallitsemaksi toiminnaksi. Tämä ei kuitenkaan muuta pöytäkirjan sääntöjä. Teoriassa kuka tahansa voi louhia millä tahansa koneella. Käytännössä ASIC:n vaikeustaso ja tehokkuus ovat kuitenkin tehneet kotimaisesta mining:stä useimmiten kilpailukyvyttömän.



Tietenkin on edelleen tilanteita, joissa koti mining voi olla kiinnostava, esimerkiksi jos hyödyt erittäin halvasta sähköstä tai jos käytät kaivostyöläisesi generated-lämpöä kotisi lämmittämiseen talvella. Joka tapauksessa sinun on kuitenkin ostettava kone, jossa on ASIC-siru. Lisäksi, koska mining-tehosi pysyy erittäin pienenä suhteessa Bitcoin-verkkoon, sinun on keksittävä keino vähentää tulojesi vaihtelua: juuri tämä on mining-altaiden tehtävä, jota käsittelemme seuraavassa luvussa.



Jos haluat tutustua mining-kotiratkaisuihin lämmön talteenotolla, meillä on oppaita erilaisista työkaluista, sekä valmiista että itse tehdyistä:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Ryhmittely mining-altaisiin


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin aiheuttaa jatkuvia ja väistämättömiä kustannuksia, joista tärkein on koneen virrankulutus. Nämä kustannukset syntyvät tuloksista riippumatta, vaikka mining:stä saatavat tulot ovat luonteeltaan harvinaisia ja satunnaisia. Lohkon löytyminen riippuu yksinomaan louhijan osuudesta hashrate:sta, mikä tekee tuloista sitä arvaamattomampia, mitä pienempi tämä osuus on. Juuri tämä käytännön ongelma johti nopeasti [mining-poolien](https://planb.academy/resources/glossary/pool-mining) yleistymiseen. Tässä MIN 101 -kurssin viimeisessä luvussa esittelen mining-poolien periaatteet ja toiminnan Bitcoin:ssa.



### Mikä on mining-allas?



mining-pooli on organisaatio (usein verkkopalvelu), joka yhdistää monien itsenäisten louhijoiden laskentatehon, jotta ryhmä löytäisi lohkoja entistä useammin. Kun pooli löytää lohkon, lohkopalkkio jaetaan uudelleen osallistujien kesken poolin sisäisten sääntöjen mukaisesti (jotka käsitellään MIN 201 -kurssilla, koska ne ovat liian monimutkaisia MIN 101 -kurssille).



mining-poolin osallistujia kutsutaan tällöin usein "[hasheriksi](https://planb.academy/resources/glossary/hasher)" eikä "louhijoiksi", koska he eivät enää suorita kaikkea mining-työtä, vaan ainoastaan hakkeroivat poolin heille lähettämät tiedot.



Varo sekoittamasta mining-poolia mining-farmiin. Ne ovat kaksi eri käsitettä. Kuten edellisessä luvussa todettiin, farmi on fyysinen paikka, jossa yksi yksikkö käyttää useita mining-koneita. Pool taas on ennen kaikkea virtuaalinen ryhmittymä: tuhannet, usein maantieteellisesti hajallaan olevat koneet toimivat yhteisen koordinoinnin alaisina. Farmi voi kuitenkin osallistua ja usein osallistuukin pooliin.



![Image](assets/fr/048.webp)



### Tuloerojen pienentäminen



Miksi siis liittyä altaaseen? Yksinkertaisesti siksi, että mining-toiminnan tulos on todennäköinen: jokaisella hash-yrityksellä on hyvin pieni mahdollisuus, että se täyttää vaikeustavoitteen ja tuottaa siten kelvollisen lohkon.



Hyvin pitkällä aikavälillä keskimääräisen ansiosi pitäisi olla suhteessa osuuteesi hashrate:stä. Tämä periaate seuraa suoraan todennäköisyyden laeista: jokainen hash-laskenta on itsenäinen satunnaisarvonta, ja suurten lukujen lain mukaan lohkojen löytämisen tiheys lähenee matemaattisesti osuuttasi verkon koko hashrate:stä. Lyhyellä ja keskipitkällä aikavälillä todelliset tulosi voivat kuitenkin olla erittäin epäsäännöllisiä. Tätä teoreettisen keskiarvon ja satunnaisen todellisuuden välistä eroa kutsutaan matematiikassa **varianssiksi**.



Seuraavassa on yksinkertainen esimerkki periaatteen havainnollistamiseksi:




- Bitcoin-verkko tuottaa keskimäärin 144 lohkoa päivässä (noin yksi lohko 10 minuutin välein);
- Jos sinulla on `0,0001 %` koko hashrate:sta, odotuksesi on `144 × 0,000001` eli `0,000144` lohkoa päivässä;
- Toisin sanoen lohkoa pitäisi löytyä keskimäärin joka `1 / 0,000144` päivä, eli 6 944 päivän välein eli noin 19 vuoden välein.



Tämä arvo vastaa kuitenkin vain matemaattista odotusta: löytöaikojen jakauma noudattaa satunnaislakia, joten käytännössä on täysin mahdollista, ettei koskaan löydetä yhtään lohkoa edes hyvin pitkän ajanjakson aikana. Voit olla epäonninen etkä löydä mitään hyvin pitkään aikaan, ja samalla voit maksaa toistuvia kustannuksia (sähkö, huolto, laitteiden poistot...).



mining-allas muuttaa tämän ongelman luonteen: yhdistämällä hashrate:iä allas löytää lohkoja useammin. Kukin osallistuja suostuu tällöin saamaan vain murto-osan jokaisesta löydetystä lohkosta, mutta paljon useammin. Kyseessä on muutos erittäin epävakaasta, laajalle hajautetusta tulosta säännöllisempään tuloon, mutta sillä kustannuksella, että palkkiot jaetaan ja palvelumaksuja maksetaan.



### Miksi varianssi laskee, kun ryhmittyvät yhteen?



Mitä suurempi on laskentatehosi, sitä suurempi on löydettyjen lohkojen odotettu esiintymistiheys. Mitä tärkeämpää on, että mitä useammin tapahtumia on, sitä lähempänä havaitut tulokset ovat tietyn ajanjakson tilastollista keskiarvoa.



Yksittäinen pienimuotoinen louhija voi olla vuosia ilman yhtään lohkoa, sitten hän saa jonain päivänä suuren voiton ja sitten ei mitään. Poolissa sama todennäköisyystodellisuus pätee edelleen, mutta sitä tasoitetaan kollektiivisessa mittakaavassa: pool löytää lohkoja useammin, ja uudelleenjako muuttaa nämä tapahtumat säännöllisemmiksi maksuiksi jokaiselle osallistujalle. **mining-pooli myy siis ennustettavuutta mining-toimintaan**.



### Historialliset maamerkit



Kuten edellisessä luvussa todettiin, mining:n saattoi aivan alussa tehdä yksin tavallisella tietokoneella, koska sen vaikeusaste oli hyvin alhainen. Mutta kun maailmanlaajuinen hashrate räjähti käsiin (GPU, sitten ASIC), soolotehtävästä mining tuli useimmille osallistujille hyvin aikaa vievä uhkapeli.



Ensimmäiset altaat luotiin juuri tämän uuden todellisuuden vuoksi. Braiins Pool (entinen Slush Pool / Bitcoin.cz) on ensimmäinen Bitcoin mining-allas: se louhi ensimmäisen lohkonsa 16. joulukuuta 2010. Tämän ensimmäisen mining-poolin menestys oli nopeaa, sillä vain muutamassa päivässä se kaappasi lähes 3,5 prosenttia maailmanlaajuisesta hashrate:stä.



![Image](assets/fr/047.webp)



Teknisesti poolit rakennettiin poolin ja louhijoiden välisten erityisten viestintäprotokollien (esim. [Stratum](https://planb.academy/resources/glossary/stratum), sitten Stratum V2) ympärille, jotta hajautettua työtä voitaisiin organisoida tehokkaasti. Tarkastelemme näitä käsitteitä tarkemmin MIN 201 -koulutuskurssillamme.



### Nykytilanne



Tätä kirjoitettaessa (vuoden 2026 alussa) maailmanlaajuinen Bitcoin hashrate on suuruusluokkaa zetta-hash sekunnissa (= 1 000 EH/s = 1 000 000 000 000 000 000 000 000 000 hashia sekunnissa), ja lähes kaikki löydetyt lohkot ovat peräisin mining-altaista.



Seuraavassa on tähän mennessä laadittu luettelo tärkeimmistä mining-rahastoista ja niiden osuudesta hashrate:stä. Tämä järjestys muuttuu todennäköisesti siihen mennessä, kun luet tätä kurssia. Ajantasaiset tiedot löydät osoitteesta [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Lähde [mempool.space](https://mempool.space/graphs/mining/pools), yhden kuukauden tiedot, 16.12.2025 - 16.1.2025.*



Edistyneemmällä kurssilla menemme syvemmälle poolien sisäiseen toimintaan (osakkeet, verkkoprotokollat, maksutavat...), sillä juuri tässä vaiheessa tulevat esiin yksityiskohdat, jotka määrittävät sekä louhijan kannattavuuden että mahdolliset vaikutukset Bitcoin:een.



---

Olemme nyt tulleet MIN 101:n loppuun. Kiitos, että seurasit sitä loppuun asti. Jos haluat arvioida kurssin aikana hankkimiasi taitoja, loppukoe odottaa sinua seuraavassa osiossa.



Juuri hankkimiesi perustietojen avulla voit nyt suorittaa mining:n Plan ₿ Academy:n edistyneempiä kursseja, joko teoriassa, kuten tämä, tai käytännön kursseja, jotta sinäkin voit alkaa osallistua Bitcoin mining:een!



# Viimeinen osa


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Arvostelut & arvostelut


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Loppukoe


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Päätelmä


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>