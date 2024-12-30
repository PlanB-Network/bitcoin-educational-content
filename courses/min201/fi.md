---
name: Johdatus Bitcoin-louhintaan
goal: Ymmärtää louhintateollisuuden toiminta käytännön harjoituksen kautta, jossa kierrätetään ASIC-laitteita.
objectives:
  - Ymmärtää teoria louhinnan takana
  - Ymmärtää louhintateollisuus
  - Muuntaa S9-louhija lämmittimeksi
  - Louhi ensimmäinen satoshisi
---

# Ensiaskeleesi louhinnassa!

Tässä koulutuksessa syvennymme louhintateollisuuteen demystifioimalla tämän monimutkaisen aiheen! Koulutus on kaikille saavutettavissa eikä vaadi alkuperäistä investointia.

Ensimmäinen osio on teoreettinen, jossa Ajelex ja minä käymme läpi syvällistä keskustelua eri aiheista, jotka liittyvät louhintaan. Tämä auttaa meitä ymmärtämään paremmin tätä teollisuudenalaa sekä siihen liittyviä taloudellisia ja geopoliittisia kysymyksiä.
Toisessa osiossa käsittelemme käytännön tapausta. Todellakin, opimme muuntamaan käytetyn S9-louhijan kotilämmitysjärjestelmäksi! Kirjallisten ohjeiden ja videoiden kautta näytämme ja selitämme kaikki askeleet, jotta voit saavuttaa tämän kotona :)

Tämän videon kautta toivomme näyttävämme, että louhintateollisuus on monimutkaisempi kuin miltä se vaikuttaa, ja sen tutkiminen auttaa hienosäätämään ekologista keskustelua, joka on siihen liitetty!
Jos tarvitset apua asennuksessasi, opiskelijoille on luotu Telegram-ryhmä, ja kaikki tarvittavat komponentit löytyvät e-kauppapaikaltamme!

+++

# Johdanto

<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>

## Tervetuloa!

<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>

Tervetuloa MINING 201: johdatus louhintaan. Ajelex, Jim & Rogzy ovat innoissaan saadessaan seurata sinua ensimmäisissä konkreettisissa askeleissasi tässä uudessa teollisuudenalassa. Toivomme, että nautit kurssista ja liityt kotilouhinnan seikkailuun!

### Kurssin Yleiskatsaus

Kurssin ensimmäisessä osiossa keskitymme louhinnan teoriaan Ajelexin kanssa. Käymme läpi syvällisiä keskusteluja eri aiheista, jotka liittyvät louhintaan, mikä auttaa meitä ymmärtämään paremmin tätä teollisuudenalaa sekä siihen liittyviä taloudellisia ja geopoliittisia kysymyksiä.

Toisessa osiossa ryhdymme kiehtovaan käytännön tapaukseen, opimme muuntamaan käytetyn S9-louhijan kotilämmitysjärjestelmäksi. Kirjallisten ohjeiden ja videoiden kautta kaikki tarvittavat askeleet selitetään huolellisesti, varmistaen menestyksesi tässä innovatiivisessa projektissa.

Tämä oppimismatka näyttää sinulle, että louhintateollisuus on monimutkaisempi kuin miltä se näyttää, tarjoten tasapainoisen näkökulman siihen liittyvään ekologiseen keskusteluun. Jatkuva apu on saatavilla opiskelijoille omistetun Telegram-ryhmän kautta, ja kaikki tarvittavat komponentit ovat helposti saatavilla e-kauppapaikaltamme.

### Opetussuunnitelma:

Teoreettinen osio:

- Louhinnan selitys.
- Louhintateollisuus.
- Louhintateollisuuden vivahteet.
- Louhinta Bitcoin-protokollassa.
- Bitcoinin hinta ja hashrate, korrelaatio? Suvereniteetti ja sääntely
- Haastattelu louhintateollisuuden ammattilaisen kanssa

Käytännön osio: Attakai

- Johdatus Attakaihin.
- Ostajan opas.
- Antminer S9:n ohjelmiston muokkaus.
- Tuulettimien vaihto melun vähentämiseksi.
- Poolin konfigurointi.
- Antminer S9:n konfigurointi Braiins OS+:lla.

Valmis sukeltamaan tähän kiehtovaan seikkailuun? Sukelletaan yhdessä kotilouhinnan mielenkiintoiseen maailmaan!

# Kaikki mitä sinun tarvitsee tietää louhinnasta

<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>

## Louhinnan selitys

<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>

### Louhinnan explanation: Palapelitehtävä-analogia

Louhintakonseptin selittämiseksi yksinkertaistetulla tavalla voidaan käyttää osuvaa analogiaa: palapeliä. Aivan kuten palapeli, louhinta on monimutkainen suoritus, mutta helppo todentaa kerran suoritettuna. Bitcoin-louhinnan kontekstissa louhijat pyrkivät nopeasti ratkaisemaan digitaalisen palapelin. Ensimmäinen palapelin ratkaissut louhija esittää ratkaisunsa koko verkolle, joka voi sitten helposti todentaa sen pätevyyden. Tämä onnistunut todentaminen mahdollistaa louhijan uuden lohkon vahvistamisen ja lisäämisen Bitcoin-aikaketjuun. Työstään, joka sisältää merkittäviä kustannuksia, louhija palkitaan tietyn määrän bitcoineja. Tämä palkkio toimii taloudellisena kannustimena louhijoille jatkaa transaktioiden vahvistamista ja Bitcoin-verkon turvaamista.

![kuva](assets/en/01.webp)

Alun perin Bitcoin-verkossa palkinto oli 50 bitcoinia joka kymmenes minuutti, rinnakkain lohkon löytämisen kanssa joka kymmenes minuutti keskimäärin louhijoilta. Tämä palkkio puolittuu joka 210 000 lohkon jälkeen, suunnilleen joka neljäs vuosi. Tämä korvaus toimii voimakkaana kannustimena rohkaista louhijoita osallistumaan louhintaprosessiin huolimatta sen energiakustannuksista. Ilman palkkiota, energiaintensiivinen louhinta hylättäisiin, vaarantaen koko Bitcoin-verkon turvallisuuden ja vakauden.
Nykyinen louhintapalkkio on kaksiosainen. Toisaalta se sisältää uusien bitcoinien luomisen, joka on vähentynyt alun 50 bitcoinista joka kymmenes minuutti nykyiseen 6,25 bitcoiniin (2023). Toisaalta se sisältää transaktiomaksut eli louhintamaksut, transaktioista, jotka louhija valitsee sisällyttääkseen lohkoonsa. Kun bitcoin-transaktio tehdään, maksetaan transaktiomaksuja. Nämä maksut toimivat eräänlaisena huutokauppana, jossa käyttäjät ilmoittavat, kuinka paljon he ovat valmiita maksamaan transaktionsa sisällyttämisestä seuraavaan lohkoon. Maksimoidakseen palkkionsa louhijat, omassa edussaan toimien, valitsevat lohkoonsa sisällytettäviksi tuottoisimmat transaktiot, ottaen huomioon rajallisen saatavilla olevan tilan. Näin ollen louhintapalkkio koostuu sekä uusien bitcoinien luomisesta että transaktiomaksuista, varmistaen jatkuvan kannustimen louhijoille ja turvaten Bitcoin-verkon pitkäikäisyyden ja turvallisuuden.

### Louhijat ja heidän työkalunsa: Louhinta

Louhintaprosessi sisältää kelvollisen hashin löytämisen, joka on hyväksyttävä Bitcoin-verkolle. Kalkuloitu ja löydetty hash on peruuttamaton, samankaltainen kuin perunoiden muuttaminen muusiksi. Se todentaa tietyn toiminnon ilman mahdollisuutta palata takaisin. Louhijat kilpailussa käyttävät koneita näiden hashien laskemiseen. Vaikka teoriassa on mahdollista löytää tämä hash käsin, toiminnon monimutkaisuus tekee tästä vaihtoehdosta epäkäytännöllisen. Tietokoneita, jotka kykenevät suorittamaan nämä laskelmat nopeasti, käytetään siksi, kuluttaen merkittävän määrän sähköä.

Alussa CPU-aikakausi hallitsi, jossa louhijat käyttivät henkilökohtaisia tietokoneitaan Bitcoin-louhintaan. GPUiden (näytönohjaimet) edut tässä tehtävässä löytäminen merkitsi käännekohtaa, merkittävästi lisäten hashratea ja vähentäen energiankulutusta. Edistys ei pysähtynyt tähän, seurasi FPGAiden (field-programmable gate arrays) käyttöönotto. FPGA:t toimivat alustana ASICien (application-specific integrated circuits) kehittämiselle.

![kuva](assets/en/02.webp)
ASICit ovat piirejä, verrattavissa CPU-piiriin, mutta ne on kehitetty suorittamaan vain yhtä tiettyä laskentatyyppiä mahdollisimman tehokkaasti. Toisin sanoen, CPU pystyy suorittamaan monenlaisia laskentoja olematta erityisesti optimoitu mihinkään tiettyyn laskentaan, kun taas ASIC pystyy suorittamaan vain yhtä tyyppistä laskentaa, mutta hyvin tehokkaasti. Bitcoin ASICien tapauksessa ne on suunniteltu SHA256-algoritmin laskentaan. Nykyään kaivostyöläiset käyttävät yksinomaan tähän toimintoon omistettuja ASICeja, jotka on optimoitu testaamaan mahdollisimman monta yhdistelmää mahdollisimman pienellä energiankulutuksella ja mahdollisimman nopeasti. Nämä tietokoneet, jotka eivät pysty suorittamaan muita tehtäviä kuin Bitcoinin louhintaa, ovat konkreettinen todiste Bitcoinin kaivosalan jatkuvasta kehityksestä ja erikoistumisen lisääntymisestä. Tämä jatkuva kehitys heijastaa Bitcoinin sisäistä dynamiikkaa, jossa vaikeustason säätö varmistaa lohkon tuotannon joka kymmenes minuutti huolimatta kaivoskapasiteetin eksponentiaalisesta kasvusta.

Tämän prosessin intensiteetin havainnollistamiseksi, harkitse tyypillistä kaivostyöläistä, joka kykenee saavuttamaan 14 TeraHashia sekunnissa, eli 14 biljoonaa yritystä joka sekunti löytää oikea hash. Bitcoin-verkon mittakaavassa saavutamme nyt noin 300 HexaHashia sekunnissa, mikä korostaa Bitcoinin louhinnassa mobilisoidun kollektiivisen voiman määrää.

### Vaikeustason Säätö:

Vaikeustason säätö on keskeinen mekanismi Bitcoin-verkon toiminnassa, varmistaen, että lohkoja louhitaan keskimäärin joka 10. minuutti. Tämä kesto on keskiarvo, koska louhintaprosessi on itse asiassa todennäköisyyspeli, samanlainen kuin nopan heitto toivossa saada numero, joka on pienempi kuin vaikeustason määrittelemä numero. Joka 2016 lohkon jälkeen, verkko säätää louhintavaikeutta perustuen edellisten lohkojen louhintaan keskimäärin vaadittuun aikaan. Jos keskimääräinen aika on yli 10 minuuttia, vaikeustasoa alennetaan, ja päinvastoin, jos keskimääräinen aika on alempi, vaikeustasoa nostetaan. Tämä säätömekanismi varmistaa, että uusien lohkojen louhinta-aika pysyy vakiona ajan myötä, riippumatta kaivostyöläisten määrästä tai verkon kokonaislaskentatehosta. Tämän vuoksi Bitcoinin lohkoketjua kutsutaan myös Aikaketjuksi.

![image](assets/en/03.webp)

- Esimerkki Kiinasta:
  Kiinan tapaus kuvaa täydellisesti tätä vaikeustason säätömekanismia. Runsaiden ja halpojen energiavarojen ansiosta Kiina oli maailmanlaajuinen keskus Bitcoinin louhinnalle. Vuonna 2021 maa yllättäen kielsi Bitcoinin louhinnan alueellaan, mikä johti globaalin Bitcoin-verkon hashraten massiiviseen laskuun, noin 50%. Tämä nopea louhintatehon lasku olisi voinut vakavasti häiritä Bitcoin-verkkoa lisäämällä keskimääräistä lohkon louhinta-aikaa. Kuitenkin, vaikeustason säätömekanismi aktivoitui, alentaen louhintavaikeutta varmistaakseen, että lohkojen louhintataajuus pysyy keskimäärin 10 minuutissa. Tämä tapaus osoittaa Bitcoinin vaikeustason säätömekanismin tehokkuuden ja joustavuuden, joka takaa verkon vakauden ja ennustettavuuden, jopa äkillisten ja merkittävien muutosten edessä globaalissa louhintamaisemassa.

### Bitcoinin Louhintakoneiden Kehitys

Bitcoinin louhintakoneiden kehityksestä puhuttaessa on tärkeää huomata, että konteksti on enemmän suunnattu perinteiseen liiketoimintamalliin. Kaivostyöläiset ansaitsevat tulonsa lohkojen validoinnista, tehtävästä, jonka onnistumisen todennäköisyys on suhteellisen pieni. Nykyisin käytössä oleva malli, Antminer S9, vaikka vanhempi malli, joka lanseerattiin noin vuonna 2016, on edelleen kierrossa käytettynä markkinoilla, kaupan noin 100–200 eurolla. Kuitenkin louhintakoneiden hinta vaihtelee Bitcoinin arvon mukaan, ja uudempi malli, Antminer S19, arvioidaan tällä hetkellä noin 3000 euroksi.
Jatkuvien teknologisten edistysaskelten edessä kaivosalalla ammattilaiset joutuvat strategisesti asemoimaan itsensä. Kaivosala on jatkuvan innovaation kohteena, kuten äskettäin julkaistu S19:n J-versio ja odotettu S19 XP:n julkaisu osoittavat, tarjoten huomattavasti paremmat kaivoskyvyt. Lisäksi parannukset eivät liity pelkästään koneiden raakatehoon. Esimerkiksi uusi S19 XP -malli käyttää nestemäistä jäähdytysjärjestelmää, tekninen muutos, joka mahdollistaa merkittävän parannuksen energiatehokkuudessa. Vaikka innovaatio on jatkuvaa, tulevaisuuden tehokkuuden kasvut tulevat todennäköisesti olemaan pienempiä verrattuna tähän mennessä havaittuihin, johtuen tietyn teknologisen innovaation kynnyksen saavuttamisesta.

![kuva](assets/en/04.webp)

Yhteenvetona voidaan todeta, että Bitcoinin kaivosala jatkaa sopeutumista ja kehittymistä, ja alan toimijoiden on ennakoitava tulevaisuudessa pieneneviä tehokkuuden kasvuja ja mukautettava strategioitaan sen mukaisesti. Tulevaisuuden teknologiset edistysaskeleet, vaikka yhä läsnä, todennäköisesti tapahtuvat pienemmässä mittakaavassa, heijastaen alan kasvavaa kypsyyttä.

## Kaivosala

<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>

### Kaivosaltaat

Nykyään Bitcoinin louhinta on kehittynyt vakavaksi ja merkittäväksi alaksi, jossa monet toimijat ovat nyt julkisesti tunnettuja ja merkittävien louhijoiden määrä kasvaa. Tämä kehitys on tehnyt louhinnasta lähes saavuttamattoman pienille toimijoille korkeiden uusien louhintakoneiden hankintakustannusten vuoksi. Tämä herättää kysymyksen hashraten jakautumisesta eri markkinatoimijoiden kesken. Tilanne on monimutkainen, koska on tärkeää tarkastella hashraten jakautumista sekä eri yritysten että eri kaivosaltaiden kesken.

![kuva](assets/en/05.webp)

Kaivosallas on louhijoiden ryhmä, joka yhdistää laskentatehonsa lisätäkseen mahdollisuuksiaan louhia. Tämä yhteistyö on tarpeellista, koska erillään oleva pieni louhintakone kilpailee teollisuuden jättiläisiä vastaan, vähentäen sen menestymismahdollisuuksia merkityksettömälle tasolle. Louhinta toimii lotto-periaatteella, ja mahdollisuudet voittaa lohko (ja siten Bitcoin-palkkio) joka kymmenes minuutti ovat erittäin pienet yksittäiselle pienelle louhijalle. Yhdistämällä voimansa louhijat voivat yhdistää laskentatehonsa, löytää lohkoja useammin ja sitten jakaa palkkiot suhteellisesti kunkin louhijan panokseen altaassa.

Esimerkiksi, jos allas löytää lohkon ja voittaa 6,25 bitcoinia, louhija, joka on antanut 1% altaan kokonaislaskentatehosta, saisi 1% 6,25 bitcoinista. On kuitenkin huomattava, että kaivosaltaat yleensä ottavat pienen komission (yleensä noin 2%) kattaakseen osuuskunnan toimintakustannukset.

### Alan käyttämä ohjelmisto

Bitcoinin louhinnan yhteydessä ohjelmiston rooli on yhtä kriittinen kuin laitteiston. Tämän havainnollistaa Bitmainin rooli, tuottelias valmistaja, joka kehitti Antminer S9:n. Louhintalaitteiston lisäksi ala nojaa voimakkaasti yhteistyöhön perustuviin kaivosaltaihin, kuten Brainspool, joka hallitsee noin 5% Bitcoin-verkon globaalista hashratesta.
Alan toimijat pyrkivät jatkuvasti lisäämään tehokkuutta laitteiston ja ohjelmiston avulla. Esimerkiksi tässä yhteydessä suosittu ohjelmisto on BrainsOS Plus. Tämä ohjelmisto korvaa louhintakoneen alkuperäisen käyttöjärjestelmän, mahdollistaen samojen toimintojen suorittamisen tehokkaammin. Tällaisen ohjelmiston avulla louhija voi lisätä koneensa tehokkuutta 25%. Tämä tarkoittaa, että samalla sähkön määrällä kone voi tuottaa 25% lisää hashratea, mikä lisää louhijan saamia palkkioita. Tämä ohjelmiston optimointi on olennainen kilpailukyvyn elementti Bitcoinin louhinnassa, osoittaen integroidun lähestymistavan tärkeyden, joka yhdistää sekä laitteiston että ohjelmiston parannukset tehokkuuden ja tuottojen maksimoimiseksi.

### Säätely ja sähkön hinnat

Kuten Kiinassa ja muualla on havaittu, säätelyllä on merkittävä vaikutus louhintaan. Vaikka Ranskassa ei ole merkittäviä louhijoita, säätely ja korkeat sähkön hinnat Euroopassa ovat suuria esteitä. Louhijat etsivät jatkuvasti edullista sähköä maksimoidakseen voittonsa. Siksi korkea sähkön hinta Euroopassa ja Ranskassa ei houkuttele louhijoita näille alueille.

Louhijat suuntaavat alueille, joilla on matalat sähkön hinnat, usein kehittyvissä maissa tai maissa, joilla on energiaa ylijäämässä. Esimerkiksi suuri osa maailman hashratesta sijaitsee Texasissa, Yhdysvalloissa. Texasilla on itsenäinen sähköverkko, joka ei jaa energiavarojaan muiden osavaltioiden kanssa. Tämä erityispiirre johtaa usein siihen, että Texas tuottaa enemmän sähköä kuin tarpeellista välttääkseen puutteet, luoden ylijäämän. Bitcoin-louhijat hyödyntävät tätä ylituotantoa perustamalla toimintansa Texasiin, missä he voivat louhia bitcoineja erittäin matalilla sähkön hinnoilla energian ylijäämän aikana. Tämä tilanne osoittaa säätelyn ja sähkön hintojen merkittävän vaikutuksen Bitcoin-louhintaan, korostaen näiden tekijöiden tärkeyttä louhijoiden päätöksenteossa louhintatoimintojensa sijainnin suhteen.

### Minne louhijat menevät ja energianhallinta?

Korostamalla Bitcoin-louhijoiden vaikutusta energian maailmassa, suunta on selvä: nämä toimijat etsivät jatkuvasti halvan sähkön lähteitä, usein niitä, jotka ovat hukkaan meneviä tai hyödyntämättömiä. Tämä ilmiö on ilmeinen alueilla, joilla on uutta sähköinfrastruktuuria, kuten alueilla, joilla on äskettäin rakennettuja vesivoimaloita.

Otetaan esimerkki. Maassa, joka on rakentamassa patoa, sähköntuotanto alkaa usein ennen kuin jakeluverkot ovat täysin toiminnassa. Tämä aikaväli voi aiheuttaa merkittäviä kustannuksia ja estää investointeja tällaisiin infrastruktuurihankkeisiin. Bitcoin-louhijat voivat kuitenkin toimia joustavana kysynnän lähteenä, valmiina kuluttamaan tätä "orpoa" sähköä, auttaen siten kattamaan infrastruktuurikustannuksia. Tästä seuraa, että uudet asennukset voivat olla välittömästi kannattavia, edistäen uusien sähkön lähteiden luomista. Tämä periaate pätee myös pienemmissä mittakaavoissa. Olipa kyseessä yksilö, joka käyttää vesivoimageneraattoria pienellä joella, tai kotitalous, joka on varustettu aurinkopaneeleilla, tuotettu ylimääräinen sähkö voidaan käyttää Bitcoin-louhintatoimintoihin.

Ranskassa esimerkiksi aurinkopaneeleista ylijäävä sähkö injektoidaan takaisin verkkoon ja tuottajat saavat kulutuskrediittiä EDF:ltä. Samoin voi kuvitella louhijan toimivan tällä ylijäämäsähköllä, pysäyttäen toimintansa, kun paikallinen kysyntä vastaa tarjontaa. Vaikka tämä saattaa vaikuttaa itsekkäältä, bitcoin-tuotannon asettaminen paikallisen sähköverkon tukemisen edelle, se tarjoaa toisen näkökulman: sähköverkon vakauttaminen. Ylijäämäsähkön monimutkainen hallinta, joskus jopa siihen liittyvät hävittämiskustannukset, voidaan suuresti yksinkertaistaa. Bitcoin-louhijat voivat absorboida nämä ylijäämät toimien joustavana puskurina, säätäen kysyntää ennemmin kuin tarjontaa. Maailmassa, jossa uusiutuvien (ei-ohjattavien) energialähteiden sähköntuotanto on jatkuvasti kasvussa, louhijat voivat näytellä keskeistä roolia sähköverkkojemme tasapainon varmistamisessa, hyötyen samalla halvasta tai ylijäämäsähköstä louhintatoimintoihinsa.

### Louhinnan keskittäminen

Louhinnan keskittymistä käsitellään merkittävänä haasteena. Suuret toimijat, kuten Foundry, hallitsevat markkinoita, mikä voi mahdollisesti johtaa transaktioiden sensurointiin. Tämä keskittäminen voi myös tehdä verkosta haavoittuvan hyökkäyksille, mukaan lukien 51% hyökkäys, jossa toimija tai ryhmä hallitsee yli 50% verkon hashratesta, mahdollistaen heidän hallita ja manipuloida verkkoa.

Säätelyriskiä korostetaan, että jos maa kuten Yhdysvallat päättäisi säädellä tai kieltää tiettyjä Bitcoin-transaktioita, sillä voisi olla merkittävä vaikutus verkkoon, erityisesti jos suuri osa hashratesta on keskittynyt kyseiseen maahan.

![kuva](assets/en/06.webp)

Tämän keskittymisen torjumiseksi keskustellaan erilaisista strategioista:

- Kotilouhinta: Kotilouhinnan idea perustuu louhintatoiminnan hajauttamiseen. Se kannustaa yksilöitä osallistumaan louhintaan kotoaan käsin, jakaen siten hashraten laajemmin.
- Stratum V2: Stratum V2 -protokolla tarjoaa toisen lähestymistavan. Toisin kuin edeltäjänsä, Stratum V2 sallii louhijoiden valita, mitkä transaktiot sisällyttävät heidän louhimiinsa lohkoihin. Tämä kyky vahvistaa sensuurin vastustusta ja vähentää suurten louhintapoolien kykyä hallita verkkoa. Antamalla enemmän valtaa yksittäisille louhijoille, Stratum V2 -protokolla voi näytellä ratkaisevaa roolia taistelussa hashraten keskittymistä vastaan.
  Avointen lähdekoodien louhintaohjelmisto
- Louhintaohjelmiston avaaminen lähdekoodina: Tämä on toinen mahdollisesti tehokas strategia. Tekemällä louhintaohjelmiston kaikkien saataville, pienillä louhijoilla olisi samat mahdollisuudet kuin suurilla louhintayhtiöillä osallistua ja edistää lohkoketjuverkon toimintaa. Tämä lähestymistapa kannustaisi hashraten laajempaan jakautumiseen, edistäen siten verkon hajauttamista.
- Toimijoiden ja maantieteellisen sijainnin monipuolistaminen: Kryptovaluutan louhintaan osallistuvien moninaisten toimijoiden kannustaminen eri maantieteellisiltä alueilta voi myös osoittautua tehokkaaksi. Hajauttamalla hashrate maantieteellisesti, yksittäisen toimijan tai maan on vaikeampi harjoittaa kohtuutonta kontrollia tai vaikutusvaltaa verkossa. Tämä lähestymistapa voi auttaa suojelemaan verkkoa mahdollisia hyökkäyksiä vastaan ja vahvistamaan sen hajauttamista.

Yleinen johtopäätös on, että hajauttaminen on ratkaisevan tärkeää Bitcoin-verkon turvallisuuden ja joustavuuden kannalta. Vaikka keskittäminen voi tarjota tehokkuusetuja, se altistaa verkon merkittäville riskeille, mukaan lukien sensuuri ja 51% hyökkäykset. Aloitteet kuten Takai ja uusien protokollien, kuten Stratum V2, käyttöönotto ovat tärkeitä askelia kohti hajauttamista ja Bitcoin-verkon suojelemista näitä uhkia vastaan.

## Louhintateollisuuden vivahteet

<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>

### Attakain periaate

Nykyisessä kontekstissa Bitcoinin louhinta S9-mallilla saattaa tuntua monimutkaiselta, mutta syvempi analyysi avaa ovet innovatiivisille vaihtoehdoille. Attakai-periaate perustuu ajatukseen louhintalaitteiden hyödyntämisestä erilaisissa rakennuksissa, kuten kouluissa tai sairaaloissa. Pääajatuksena on sijoittaa muutamia louhintakoneita eri paikkoihin, jolloin koneista vapautuva lämpö voidaan käyttää rakennusten lämmittämiseen. Valitsemalla tehokkaampia malleja, kuten S19, olisi mahdollista jakaa louhintatoiminta, mikä parantaisi kokonaistehokkuutta ja samalla hyödyttäisi yhteiskuntaa. Tämän aloitteen tarkoituksena on kilpailla suurten keskitettyjen louhintalaitosten kanssa hyödyntämällä louhintakoneiden tuottamaa lämpöä tuottavalla ja tehokkaalla tavalla.

Attakai-aloite sai alkunsa kahden ystävän kotiin tekemästä louhintakokeilusta, kun he halusivat osallistua aktiivisesti Bitcoin-verkkoon. He kohtasivat suuria esteitä, kuten louhintalaitteiden korkean melutason, joka oli suunniteltu teolliseen, ei kotikäyttöön. Ongelman ratkaisemiseksi louhintakoneisiin tehtiin laitteistomuutoksia. Alkuperäiset laitteet korvattiin tehokkaammilla ja hiljaisemmilla tuulettimilla, mikä teki kotilouhinnasta helpommin saavutettavaa ja vähemmän häiritsevää. Lisäksi Wi-Fi-sovitin lisättiin, mikä poisti tarpeen Ethernet-kaapeliyhteydelle, yksinkertaistaen kotilouhintaprosessia entisestään. Talvella näitä muutettuja louhintakoneita käytettiin lämmönlähteenä, jolloin haitasta tuli hyöty.

Esiteltyään projektinsa Bitcoin-yhteisölle ja saatuun kiinnostukseen nähden Attakai-keksijät päättivät julkaista yksityiskohtaisia ohjeita Découvre Bitcoin -alustalla, jotta kuka tahansa voi toistaa heidän kotiin tekemänsä louhintakokemuksen. He suunnittelevat nyt laajentavansa konseptia kodin ulkopuolelle. Tavoitteena on osoittaa, miten muutettu louhintakone voidaan muuttaa hiljaiseksi lisälämmittimeksi, jota voidaan käyttää talvella, tarjoten pehmeän siirtymän toiseen koulutusosaan, joka keskittyy näiden muutosten käytännön toteutukseen ja opastaviin videoihin. Kysymys kuuluu kuitenkin, voidaanko tätä aloitetta laajentaa suuremmassa mittakaavassa, tarjoten realistinen ja kestävä vaihtoehto nykyisille keskitettyihin louhintarakenteisiin perustuvalle toiminnalle.

![image](assets/en/07.webp)

### Tämän hajauttamisen raja?

Vaikka ajatus louhinnan hajauttamisesta tuotetun lämmön hyödyllisellä käytöllä vaikuttaa lupaavalta, sillä on tiettyjä rajoituksia ja kysymyksiä pysyy avoimina. Energiaintensiiviset laitokset, kuten saunat ja uima-altaat, voisivat hyötyä tästä konseptista käyttämällä louhijoiden tuottamaa lämpöä veden lämmittämiseen tiloissaan. Tätä käytäntöä on jo toteuttanut joitakin Bitcoin-yhteisön jäseniä, jotka tutkivat erilaisia menetelmiä louhintalaitteiden tuottaman lämmön tehokkaaseen hyödyntämiseen. Esimerkiksi juhlasali voitaisiin teoriassa lämmittää kolmella tai neljällä S19-louhijalla, jotka kukin kuluttavat 3000 wattia ja tuottavat vastaavan määrän lämpöä.

On kuitenkin huomattava, että energiankulutus ja lämmöntuotanto ovat yhtä suuria, olipa energia käytössä sähkölämmittimessä tai louhijassa. Jokaisesta käytetystä kilowatista tuotettu lämpömäärä on sama molemmissa tapauksissa. Ero on siinä, että louhija tarjoaa paitsi lämpöä myös bitcoin-palkkion, tarjoten siten taloudellisen kannustimen käyttää louhijaa yksinkertaisen sähkölämmittimen sijaan. Tämä lisäpalkkio voisi auttaa lieventämään huolia louhijoiden korkeasta energiankulutuksesta.

Bitcoin-louhijoiden käytön pitkän aikavälin tehokkuuden ja toteutettavuuden lämmityksessä kysymys pysyy avoimena. Jatkuvat innovaatiot louhintalaitteistossa ja lämmitysteknologioissa voivat mahdollisesti avata uusia väyliä louhinnasta syntyvän lämmön tehokkaammalle hyödyntämiselle, edistäen näin tämän lähestymistavan elinkelpoisuutta tulevaisuudessa.

### Miksi BTC-palkkiot?

Bitcoinin palkitsemiskysymys toisessa valuutassa kuin bitcoinissa on olennainen osa Satoshi Nakamoton visioimaa järjestelmää. Bitcoinin luominen on määritelty kiinteällä enimmäismäärällä, 21 miljoonaa yksikköä. Tavoitteena oli löytää oikeudenmukainen tapa jakaa nämä vasta luodut yksiköt. Louhijat tarjoamalla laskentatehoaan verkon turvaamiseen ja mahdollisen hyökkäyksen kustannusten kasvattamiseen suojelevat tehokkaasti Bitcoin-verkkoa. Vastineeksi tästä kriittisestä panoksesta heitä palkitaan vasta luoduilla bitcoineilla, mikä helpottaa kolikoiden jakelua ekosysteemissä.
Kyseessä on win-win-järjestelmä. Louhijat palkitaan sekä verkon turvaamisesta että tapahtumien hyväksymisestä. Vasta luodut bitcoinit annetaan kannustimena turvallisuuden vahvistamiseen, ja tapahtumamaksut ovat lisätuloa tapahtumien hyväksymisestä. Nämä kaksi elementtiä yhdessä muodostavat louhinnan kokonaispalkkion. Louhinnan tulevaisuutta koskeva kysymys nousee esiin ohjelmoidun louhintapalkkioiden vähentämisen vuoksi, joka puolittuu joka neljäs vuosi, tapahtumaa kutsutaan "halvingiksi". Vuoteen 2032 mennessä lohkopalkkio on alle yhden bitcoinin, ja vuoteen 2140 mennessä uusia bitcoineja ei luoda enää lainkaan. Tässä vaiheessa louhijat luottavat ainoastaan tapahtumamaksuihin korvauksenaan. Bitcoin-verkon on tuettava suurta määrää tapahtumia, riittävän korkeilla maksuilla, varmistaakseen louhinnan kannattavuuden.

Lightning Networkin, joka mahdollistaa nopeat ja edulliset tapahtumat Bitcoinin pääketjun ulkopuolella, nousu herättää kysymyksiä louhinnan tulevaisuudesta. Lightning Networkilla on potentiaali vähentää merkittävästi tapahtumamaksuja, vaikuttaen näin louhijoiden tuloihin. Tämä riippuu kuitenkin Lightning Networkin omaksumisesta ja käytöstä verrattuna pääasialliseen Bitcoin-verkkoon. Pessimistisessä skenaariossa louhijat saattavat pitää louhintaa kannattavana jopa tappiolla, jos he ovat poistaneet kustannuksensa ja heillä on pääsy halpaan sähköön. Optimistisemmassa skenaariossa pääasiallisen Bitcoin-verkon tapahtumamaksut voivat pysyä tarpeeksi korkeina ylläpitääkseen louhinnan kannattavuutta.

### Mitä Bitcoin-lohkoon tulisi sisältyä?

Kysymykseen siitä, mitä Bitcoin-lohkoon tulisi sisältyä, on tärkeää harkita Bitcoin-verkon eri kerrosten täydentävää luonnetta. Vaikka Lightning Network voi mahdollistaa nopeammat ja halvemmat tapahtumat, se silti nojaa Bitcoinin peruskerrokseen, jota usein kutsutaan "asettelukerrokseksi", maksukanavien avaamiseen ja sulkemiseen.

Lightning Networkin odotetun kasvun ja kanavien avaamisten ja sulkemisten seurauksena tila Bitcoin-lohkoissa muuttuu yhä arvokkaammaksi. Bitcoin-yhteisö arvostaa jo tämän tilan säilyttämistä, tunnustaen sen sisäisen rajallisuuden. Tämä tietoisuus on johtanut keskusteluihin lohkon tilan legitiimistä käytöstä, huolien ollessa "spämmistä" lohkoketjussa, jota pidetään ei-olennaisena tapahtumana.

![image](assets/en/08.webp)

Spekulaatiot lohkon tilan tulevasta käytöstä ovat yleisiä, mutta yleisesti hyväksytään, että se on niukka resurssi, jota tulisi käyttää viisaasti. Vaikka on halu täyttää se, on olennaista säilyttää se varmistaakseen Bitcoin-verkon pitkäaikaisen elinkelpoisuuden, odottaen tulevaa kysynnän kasvua lohkotilalle. Kuten missä tahansa vapaassa markkinassa, tarjonta ja kysyntä säätelevät lohkotilan käyttöä. Rajallisella tarjonnalla sidosryhmien on tehtävä tietoisia valintoja tämän arvokkaan tilan käytöstä varmistaakseen Bitcoin-verkon pitkäaikaisen tehokkuuden ja turvallisuuden.

## Bitcoinin louhinta Bitcoin-protokollassa

<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>

![Kuka pitää vallan? Bitcoin, energia ja valmistajat](https://www.youtube.com/watch?v=4wywK6BfDw8)
Louhijoiden rooli Bitcoin-verkossa on ollut kiivaiden keskustelujen kohteena lohkokoon sodissa. Vaikka louhijat ovat olennaisen tärkeitä verkon turvallisuuden ja toiminnallisuuden kannalta, he eivät välttämättä pidä lopullista valtaa Bitcoin-ekosysteemissä. Louhijoiden, solmujen ja loppukäyttäjien välinen tasapaino varmistaa verkon eheyden ja jakelun.

### Lohkokoon sodat

Lohkokoon sodissa monet louhijat vastustivat tiettyjä kehityksiä verkossa, mikä korosti jännitettä ekosysteemin eri toimijoiden välillä. Kysymys siitä, miten valtaa tulisi tasapainottaa louhijoiden, solmujen ja käyttäjien kesken Bitcoinin pitkäaikaisen turvallisuuden varmistamiseksi, pysyy avoimena.

![kuva](assets/en/09.webp)

Bitcoinin turvallisuusdilemma perustuu hauraaseen tasapainoon. Vaikka louhijat ovat keskeisessä roolissa lohkojen vahvistamisessa ja luomisessa, solmut ylläpitävät eheyttä vahvistamalla ja validoidessa transaktioita ja lohkoja. Virheellinen tai petollinen lohko hylätään solmujen toimesta, näin sensuroiden louhijaa ja säilyttäen verkon turvallisuuden. Valtaa pitävät myös Bitcoin-verkon solmut ja käyttäjät. Solmuilla on vahvistamisen ja validoinnin valta, kun taas käyttäjillä on valta valita, mitä lohkoketjua käyttää. Tämän vallanjaon avulla varmistetaan Bitcoin-verkon jakelu ja eheys.

Lohkokoon sodat paljastivat epävarmuuden ja jännitteen, joka on luontainen Bitcoin-verkon hallinnassa. Vaikka Bitcoin Core on tällä hetkellä hallitseva ketju, hallinnon ja verkonhallinnan yli käytävä keskustelu jatkuu.

Lopulta vastuu jakautuu kaikkien Bitcoin-verkon toimijoiden kesken. Käyttäjien, solmujen tai louhijoiden määrän väheneminen voisi heikentää verkkoa, lisäten keskittymisen riskiä ja haavoittuvuutta hyökkäyksille. Jokainen toimija edistää verkon vahvuutta ja turvallisuutta, korostaen vallan ja vastuun tasapainon ylläpidon tärkeyttä.

### Louhijoiden valta

Satoshi Nakamoton elegantti peliteoria loi tilanteen, jossa jokainen Bitcoin-verkon toimija on kannustettu toimimaan oikein suojellakseen sekä omia etujaan että muiden osallistujien etuja. Tämä luo tasapainon, jossa huonoa käytöstä voidaan rangaista, parantaen koko järjestelmän turvallisuutta ja vakautta. Tästä huolimatta valtiot pysyvät potentiaalisena uhkana. Kuten Surfing Bitcoin 2022 -esityksessä mainittiin, valtiot voivat yrittää hyökätä louhintateollisuutta vastaan, altistaen Bitcoin-verkon keskittymisen ja hyökkäyksen riskeille. Hypoteettiset skenaariot, kuten sotilaallinen hyökkäys louhintalaitteiden tuotantolaitoksia vastaan, korostavat maantieteellisen ja teollisen monipuolistamisen tärkeyttä Bitcoin-verkon joustavuudelle.

![kuva](assets/en/10.webp)

Louhintalaitteiden tuotannon keskittäminen Kiinaan aiheuttaa toisen riskin. Kieltäytyminen louhintakoneiden viennistä tai hashraten kasaaminen mahdollista 51% hyökkäystä varten Kiinassa korostaa louhintalaitteiden tuotannon monipuolistamisen tarvetta. Näihin riskeihin vastauksena Bitcoin-yhteisö tutkii aktiivisesti ratkaisuja. Yritykset, kuten Intel, harkitsevat louhintalaitteiden tuottamista Yhdysvalloissa, edistäen tuotannon jakautumista. Muut aloitteet, kuten Blockin avoimen lähdekoodin Mining Development Kit (MDK), pyrkivät vähentämään louhintalaitteiden suunnittelun ja tuotannon monopolia, mahdollistaen hashraten laajemman jakautumisen. Näiden keskustelujen ytimessä on Bitcoinin perustehtävä: olla sensuurinkestävä arvonvaihdon verkosto. Bitcoin-yhteisö pyrkii jatkuvasti vahvistamaan jakautumista, sensuurinkestävyyttä ja verkon anti-haurautta, hyläten ehdotukset, kuten siirtyminen proof of stake -malliin, jotka eivät ole linjassa näiden periaatteiden kanssa.

### Proof of Work vs Proof of Stake fyysinen linkki

Proof of Work (PoW) on olennainen, koska se edustaa fyysistä linkkiä todellisen maailman ja Bitcoinin välillä. Vaikka bitcoinit ovat aineettomia, niiden tuottaminen vaatii konkreettista energiaa, luoden suoran yhteyden fyysiseen ja todelliseen maailmaan. Tämä yhteys varmistaa, että bitcoinien ja lohkojen tuotanto ja validointi aiheuttavat todellisia energiakustannuksia, ankkuroiden Bitcoin-verkon fyysiseen todellisuuteen ja estäen sen täydellisen hallinnan voimakkaiden toimijoiden toimesta. PoW toimii keskittymisen vastavoimana, varmistaen, että verkostoon osallistuminen ja transaktioiden validointi vaativat investointeja konkreettisiin resursseihin. Tämä estää verkon monopolisoitumisen toimijoiden toimesta, jotka muuten voisivat ottaa hallinnan ilman merkittäviä esteitä, varmistaen näin voiman ja vaikutusvallan tasaisemman jakautumisen Bitcoin-verkossa.

![image](assets/en/11.webp)

### Proof of Staken rajoitukset

Toisaalta, Proof of Stake (PoS), vaikka se mahdollistaakin pienimuotoisen osallistumisen, ei takaa vastaavaa suojaa keskittymistä vastaan. PoS-verkossa ne, jotka jo omistavat suuren määrän valuuttaa, hallitsevat suhteettoman suurta valtaa, heijastaen olemassa olevia valtaepätasapainoja yhteiskunnassa laajemmin. Tämä dynamiikka voisi mahdollisesti perpetuoida keskittymistä ja vallan keskittymistä harvojen käsiin, mikä on vastoin Bitcoin-verkon perustavanlaatuisia jakautumistavoitteita. Väite, että jokainen voi osallistua PoS:ään, jopa pienimuotoisesti, liittymällä pooliin, ei välttämättä ole kovin vahva. PoW-verkossa jopa pieni panostaja, vaatimattomalla laitteistolla, voi aktiivisesti osallistua ja edistää verkon turvallisuutta ja jakautumista.

### Yhteenveto

Yhteenvetona voidaan todeta, että louhijat vahvistavat Bitcoin-verkon sensuurinkestävyyttä käyttämällä sähköä Bitcoinin proof of workin laskemiseen, ja heitä palkitaan uusilla bitcoineilla ja transaktiomaksuilla. Teollisuuden ammattimaistuessa erilaiset toimijat tulevat esiin, näytellen eri rooleja sirujen luomisesta louhintatilojen hallintaan. Lisäksi rahoitus myös vaikuttaa, päättämällä kuka selviää eri markkinavaiheissa. Keskittymisen ongelma pysyy, rikkaimpien toimijoiden mahdollisesti hallitessa markkinoita. Kuitenkin vaihtoehtoja kehitetään sekä laitteisto- että ohjelmistotasolla. Jokaisen yksilön on toimittava ja osallistuttava verkon jakautumiseen. Bitcoin edustaa poikkeuksellista mahdollisuutta paitsi vapauden myös energiariippumattomuuden näkökulmasta. Huolimatta kiistoista sen sähkönkulutuksen ympärillä, Bitcoin tarjoaa taloudellisen kannustimen siirtymiselle kohti järkevämpää ja runsaampaa energian käyttöä, toteuttaen aiemmin ekologisen ihanteen.

## Bitcoinin hinta ja hashrate, korrelaatio?

<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>

![Kuinka saada puhdas ja koskematon bitcoin?](https://youtu.be/A5MTtn4mm44?si=D1Yi0dVwkyafeHv-)

### Hashrate, hinta ja kannattavuus

Nykyinen hashrate, huolimatta siitä, että Bitcoinin hinta on $30,000 verrattuna aiempaan huippuunsa $69,000, korostaa konkreettista linkkiä louhinnan ja todellisen maailman välillä. Härkämarkkinakaudet johtavat korkeaan kysyntään Bitcoin-louhintaan ja lisääntyneisiin koneiden tilauksiin valmistajilta, kuten Avalon ja Bitmain. Tuotanto ja toimitus eivät kuitenkaan ole välittömiä, luoden epäsuhtaa lisääntyneen kysynnän ja myöhäisemmän saatavuuden välille. Tämä voi johtaa siihen, että härkämarkkinoiden aikana tilatut koneet toimitetaan karhumarkkinoilla, korostaen merkittävää epäsymmetriaa matalan hinnan ja korkean hashraten välillä.
Tämä tilanne myös havainnollistaa Bitcoinin sietokykyä, jota usein arvioidaan sen hinnan perusteella. Kuitenkin syvällisempi analyysi Bitcoinin terveydestä vaatii sen hash-nopeuden tutkimista, joka mittaa sekunnissa Bitcoin-verkossa suoritettavien laskentojen määrää. Vaikka Bitcoinin hinta vaihtelee, sen kustannus, joka on yhteydessä louhintaan tarvittavan sähkön määrään, on olennainen ymmärtääkseen markkinadynamiikkaa. Keskittymällä kustannukseen hinnan sijaan saadaan johdonmukaisempi näkökulma Bitcoinin vakaudelle ja pitkän aikavälin elinkelpoisuudelle. Yleisesti ottaen Bitcoinin kustannus on suhteessa sen hintaan, tarjoten paremman ymmärryksen hintavaihteluista ja tulevaisuuden näkymistä.

![kuva](assets/en/12.webp)

### Hash-nopeus ja palkkio

Louhinta asettaa Bitcoinille lattiahinnan, jonka alapuolella louhijat myisivät tappiolla. Louhinnan kustannus vaikuttaa merkittävästi hintaan, kuten Kiinassa louhinnan kiellon yhteydessä nähtiin, kun hash-nopeus ja hinta laskivat merkittävästi mutta palautuivat nopeasti. Pelkästään hinnan tarkastelu voi olla harhaanjohtavaa. Kustannusten tutkiminen, esimerkiksi kannattavuuslaskureiden kautta, tarjoaa tasapainoisemman näkökulman. Markkinat voivat kuitenkin käyttäytyä epärationaalisesti, ja louhijat voivat joutua myymään tappiolla, mahdollisesti laskien hintaa alle louhintakustannusten. Bitcoinin terveyden ja sen hajauttamisen arvioimiseksi voitaisiin kehittää yhtälö, joka sisältää erilaisia tekijöitä, kuten solmujen määrän ja hinnan. Tämä lähestymistapa voisi tarjota syvällisemmän analyysin Bitcoinista verrattuna keskusteluihin, jotka perustuvat pelkästään hintaan.

### Louhinta voiton vai verkon vuoksi?

Kysymys on syvällinen ja kattaa useita Bitcoinin louhinnan ulottuvuuksia. Tasapainon löytäminen voiton tavoittelun ja Bitcoin-verkon turvallisuuden sekä hajauttamisen edistämisen välillä on jatkuva dilemma louhijoille. Keskustelu jatkuu Bitcoin-yhteisössä, vahvojen argumenttien kera kummaltakin puolelta.

- Louhinta voiton vuoksi:

* Puolesta: Louhijat houkutellaan luonnollisesti Bitcoin-louhinnan potentiaalisilla tuloilla. Kalliisiin louhintalaitteisiin sijoittaminen voidaan kattaa louhintapalkkioilla ja transaktiomaksuilla, erityisesti kun Bitcoinin hinta on korkea.
* Vastaan: Voiton tavoittelu voi johtaa laskentatehon keskittymiseen, jos vain muutamat suuret yritykset pystyvät sijoittamaan huippuluokan louhintalaitteisiin. Lisäksi, voiton tavoittelu voi aiheuttaa merkittävän ympäristövaikutuksen.

- Louhinta verkon vuoksi:

* Puolesta: Louhinta Bitcoin-verkon turvallisuuden ja hajauttamisen edistämiseksi on jalotavoitteinen aloite. Se auttaa vahvistamaan verkon sietokykyä ja vastustamaan sensuuria sekä hyökkäyksiä.
* Vastaan: Ilman riittävää taloudellista kannustinta louhijoiden voi olla vaikea jatkaa verkon tukemista, erityisesti jos he toimivat tappiolla.
  Attakai-aloite korostaa verkostoon panostamisen tärkeyttä tarjoten samalla ratkaisuja, jotka tekevät louhinnasta helpommin saavutettavaa ja vähemmän haitallista. Mahdollisuus louhia kotona, edullisemmilla laitteilla ja ratkaisuilla melusaasteen vähentämiseksi, voi auttaa demokratisoimaan Bitcoin-louhintaa. Se kannustaa Bitcoinista kiinnostuneita ei ainoastaan investoimaan ja pitämään bitcoineja, vaan myös aktiivisesti osallistumaan verkon turvaamiseen. Testatun laitteiston ja kokoamis- sekä asennusoppaiden tarjoamisen myötä Attakai tekee Bitcoin-louhinnan maailmaan astumisen helpommaksi. Se myös kannustaa innovaatioihin ja jatkuviin parannuksiin, kutsuen yhteisön jakamaan ideoitaan ja kokemuksiaan kotilouhinnan parantamiseksi. Attakai-malli on vastaus kysymykseen louhimisesta voiton vai verkon hyväksi. Kyse ei ole vain voittojen tekemisestä, vaan myös Bitcoin-verkon jakelun ja turvallisuuden vahvistamisesta, samalla mahdollistaen useammille ihmisille osallistumisen louhintaan, oppimisen ja tämän keskeisen alan ymmärtämisen. Mahdollisen louhintakiellon haaste Euroopassa pysyy avoimena kysymyksenä. Tämä herättää huolia Bitcoin-louhinnan tulevaisuudesta alueella ja tasapainoisen sääntelyn tarpeesta, joka tunnistaa louhinnan tärkeyden Bitcoin-verkon turvallisuudelle ja elinkelpoisuudelle samalla käsitellen ympäristökysymyksiä. Attakai ja muut vastaavat aloitteet voivat näytellä keskeistä roolia tässä keskustelussa, osoittaen, että on mahdollista louhia kestävämmällä ja vastuullisemmalla tavalla, samalla positiivisesti edistäen Bitcoin-verkkoa.

## Suvereniteetti ja Sääntely

<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>

### Suvereniteetti Ennen Voittoa?

Louhinnasta saatavan vaurauden keskeisen kysymyksen käsittelyssä on tärkeää harkita erilaisia näkökulmia ja lähestymistapoja. Louhinnan kannattavuutta koskevat kysymykset ovat yleisiä, ja niissä pohditaan esimerkiksi osakkeiden ostamista yrityksistä kuten Riot tai louhintakoneiden vuokraamista maissa, joissa on alhaiset energiakustannukset, kuten Islanti tai Venäjä. Ennen louhintaan ryhtymistä keskeinen harkinta olisi verrata louhinnan kannattavuutta Bitcoinin suoraan ostamiseen. Jos Bitcoinin louhimisen kustannus ylittää sen suoran ostohinnan, on yleensä viisaampaa ostaa Bitcoin suoraan. Tämä välttää monia louhintaprosessiin liittyviä haasteita ja kustannuksia.

Louhinta tarjoaa kuitenkin ainutlaatuisia tapoja osallistua Bitcoin-ekosysteemiin. Esimerkiksi Bitcoinin louhiminen talvella voi olla ovela tapa lämmittää kotiasi samalla kun tuotat Bitcoin-tuloja. Toinen vaihtoehto on sijoittaa yrityksiin, jotka myyvät louhintalaitteistoa ja säilyttävät ja hallinnoivat koneita alhaisen energiakustannuksen paikoissa, tarjoten pääsyn edullisiin sähköhintoihin ilman laitteiston hallinnan vaivaa.

Näistä vaihtoehdoista huolimatta louhinta esittää merkittäviä haasteita. Kryptovaluuttojen maailmassa tunnettu sanonta "Ei sinun avaimiasi, ei sinun bitcoinejasi" löytää vastaavan kaikun louhintamaailmassa: "Ei sinun hashrateasi, ei sinun palkkioitasi." Pettymysten ja katkaistujen koneiden tarinat ovat yleisiä, monien toimijoiden luvatessa poikkeuksellisia tuloksia, mutta epäonnistuessa toimittamaan. Sähköntoimituksen ongelmat ja koneiden rikkoutumiset voivat jättää sijoittajat voimattomiksi, kalliiden laitteiden kanssa, joita he eivät hallitse. Tässä kontekstissa varovaisuus ja syvällinen ymmärrys louhintasektorista ovat ratkaisevan tärkeitä ennen siihen ryhtymistä. Vaikka voiton mahdollisuuksia on olemassa, riskit ovat merkittävät, ja tietoinen ja harkittu lähestymistapa on välttämätön tässä monimutkaisessa ja usein arvaamattomassa kentässä. On siis elintärkeää suorittaa perusteellinen tutkimus ja huolellisesti punnita hyvät ja huonot puolet ennen Bitcoin-louhintaan osallistumista.

![kuva](assets/en/13.webp)

### Neitsyt Bitcoinit

Oman hashrate-omistuksen tavoittelu näyttäytyy lupaavana polkuna louhinnan maailmassa. Tämän monimutkaisen ekosysteemin navigointi vaatii kuitenkin varovaista lähestymistapaa. Pilvilouhinnan ala on täynnä huijauksia, joita ruokkii monien sijoittajien louhinnasta ymmärtämisen puute. Houkuttelevat tarjoukset, jotka on paketoitu monin eri tavoin, voivat helposti johtaa harhaan niitä, jotka eivät ole riittävän hyvin informoituja. Toisaalta oman louhintalaitteiston omistaminen tarjoaa huomattavia etuja. Henkilökohtaisen tyytyväisyyden lisäksi, joka tulee aktiivisesta osallistumisesta Bitcoin-verkon turvallisuuteen ja palkkioiden näkemisestä suoraan lompakossasi, on houkutteleva näkökulma "neitseellisistä bitcoineista". Nämä ovat vasta louhittuja bitcoineja, joita ei ole koskaan käytetty ja joihin ei liity mitään historiaa. Näitä bitcoineja pidetään usein arvokkaampina, koska ne eivät ole "tahrattuja", tarjoten tietynlaista takuuta hylkäämisen vastaisesti sääntelijöiden tai suurten vaihtoalustojen toimesta.

Mahdollisuus louhia neitseellisiä bitcoineja välttäen samalla Know Your Customer (KYC) -menettelyjä on toinen lisäarvo. Monet louhintapoolit eivät vaadi louhijoiden henkilöllisyyden todentamista, mahdollistaen siten bitcoinien hankkimisen ilman aikaa vieviä henkilöllisyystarkastuksia. Neitseellisiä bitcoineja pidetään "puhtaina", ilman menneisyyttä tai yhdistyksiä. Ne ovat erityisen haluttuja suurten institutionaalisten toimijoiden keskuudessa, jotka voivat taata digitaalisten omaisuuseriensa laillisuuden sääntelyviranomaisten edessä. Kuitenkin, huolimatta näistä eduista, on tärkeää tunnistaa, että louhintateollisuus on äärimmäisen kilpailtu ja volatiili, ja ennakoimattomat tapahtumat voivat häiritä louhintatoimintaa.

Tässä kontekstissa itsenäisen ja sivistyneen lähestymistavan valitseminen louhintaan vaikuttaa viisaalta. Oman hashrate-omistuksen hankkiminen ja henkilökohtaiseen louhintalaitteistoon investoiminen, samalla riskeistä ja haasteista tietoisena, voi mahdollisesti tarjota turvallisemman ja tyydyttävämmän polun neitseellisten bitcoinien hankkimiseen, parantaen samalla yksilön taloudellista itsenäisyyttä ja tukien Bitcoin-ekosysteemiä kokonaisuudessaan.

### Onko louhinta kielletty Euroopassa?

Louhinnan mahdollisen kiellon myötä Euroopassa keskustelut sääntelystä ovat yhä merkityksellisempiä. Vaihteleva sääntelymaisema voi todellakin merkittävästi vaikuttaa Bitcoin-louhintateollisuuteen. Louhinnan kielto Euroopassa on kuviteltavissa oleva skenaario, erityisesti ottaen huomioon Kiinan ennakkotapaukset. Vaikka louhintatoiminnot jatkuvat Kiinassa kiellosta huolimatta, Eurooppa saattaisi seurata samankaltaista polkua. Hashrate-omistuksen laajempi jakautuminen eri alueille voisi auttaa vahvistamaan louhintayhteisöä Euroopassa, mahdollistaen heidän tehokkaan vastustamisen väärinkäsityksiä ja väärinkäsityksiä louhinnasta, sen ympäristövaikutuksista ja sähköverkon jalanjäljestä.

![image](assets/en/14.webp)

Kampanjoiden, kuten Greenpeacen ja joidenkin tutkimusten usein harhaanjohtavien lukujen, edessä paras ase on totuudenmukainen tieto. On olennaista informoida yleisöä ja päätöksentekijöitä louhinnan todellisuudesta, sen monimutkaisuudesta ja vivahteista, sen sijaan että annettaisiin heidän nojautua stereotypioihin ja epätarkkaan tietoon. Mitä enemmän ihmiset ovat informoituja ja tietoisia siitä, mitä louhinta todella on, sitä paremmin teollisuus voi puolustautua mahdollisia rajoittavia sääntelyjä vastaan.

Yhteenvetona, huolimatta sääntelyriskistä ja louhinnan kiellon mahdollisuudesta Euroopassa, tehokkain ase on koulutus ja informaatio. Selkeä ja tarkka ymmärrys louhinnasta, sen toiminnasta ja vaikutuksesta voi auttaa demystifioimaan teollisuutta ja taistelemaan väärää tietoa vastaan, tarjoten siten paremman vastustuksen mahdollisesti vahingollisia sääntelyjä vastaan. Aloite kouluttaa ja informoida ihmisiä louhinnasta, kuten tämä keskustelu tekee, on askel oikeaan suuntaan varmistaakseen louhinnan kestävyyden ja kasvun Euroopassa ja koko maailmassa. Jatkuvat ponnistelut kouluttaa ja informoida ovat olennaisia varmistamaan turvallisen ja menestyksekkään tulevaisuuden Bitcoin-louhintateollisuudelle.

## Haastattelu louhintateollisuuden ammattilaisen kanssa

<chapterId>4d613261-d1a8-5ffe-a50c-047a3d77d6c5</chapterId>

### Kulissien takana teollisessa louhinnassa - Sebastien Gouspillou

![Teollisen kaivostoiminnan kulissien takana - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Kotikaivostoiminta ja lämmön uudelleenkäyttö

<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>

## Attakai - mahdollistaa kotikaivostoiminnan ja tekee siitä saavutettavaa!

<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>

Attakai, joka japaniksi tarkoittaa "ihannetta lämpötilaa", on nimenä aloitteelle, jonka tavoitteena on tutustuttaa ihmisiä bitcoinien louhintaan lämmön uudelleenkäytön kautta, jonka ovat käynnistäneet @ajelexBTC ja @jimzap21 yhdessä Découvre Bitcoinin kanssa.
Tämä ASIC-muunnosopas toimii perustana oppimiselle lisää louhinnasta, sen toiminnasta ja taustalla olevasta taloudesta osoittamalla mahdollisuuden mukauttaa Bitcoin-louhintalaite toimimaan lämpöpattereina kodeissa. Tämä tarjoaa lisää mukavuutta ja säästöjä, mahdollistaen osallistujille saada ei-KYC BTC käteispalautusta sähkölämmityslaskustaan.

Bitcoin säätää automaattisesti louhintavaikeutta ja palkitsee louhijoita heidän osallistumisestaan. Kuitenkin hashraten keskittyminen voi aiheuttaa riskejä verkon neutraaliudelle. Bitcoinin laskentatehon käyttäminen lämmitysratkaisuihin hyödyttää suoraan verkkoa itseään lisäämällä laskentatehon jakautumista.

### Miksi uudelleenkäyttää ASIC:sta saatavaa lämpöä?

On tärkeää ymmärtää suhde energian ja lämmöntuotannon välillä sähköjärjestelmässä.

1 kW:n sähköenergian investoinnilla sähköpatteri tuottaa 1 kW lämpöä, ei enempää eikä vähempää. Uudet patterit eivät ole tehokkaampia kuin perinteiset patterit. Niiden etu on kyvyssä jakaa lämpöä jatkuvasti ja tasaisesti huoneessa, tarjoten enemmän mukavuutta verrattuna perinteisiin pattereihin, jotka vaihtelevat korkean lämmitystehon ja lämmityksen puuttumisen välillä, aiheuttaen säännöllisiä lämpötilan vaihteluita ja epämukavuutta.

Tietokone, tai laajemmin elektroninen kortti, ei kuluta energiaa laskelmien suorittamiseen, vaan tarvitsee vain energiaa komponenttiensa läpi virtaamiseen toimiakseen. Energiankulutus johtuu komponenttien sähköisestä vastuksesta, mikä tuottaa häviöitä ja tuottaa lämpöä, tunnetaan Joulen vaikutuksena.

Jotkut yritykset ovat keksineet idean yhdistää laskentatehon tarpeet lämmitystarpeisiin lämpöpatteri/palvelimien kautta. Idea on jakaa yrityksen palvelimet pieniin yksiköihin, jotka voitaisiin sijoittaa koteihin tai toimistoihin. Tämä idea kohtaa kuitenkin useita ongelmia. Palvelimien tarve ei liity lämmitystarpeeseen, ja yritykset eivät voi käyttää palvelimiensa laskentakykyä joustavasti. Myös yksilöiden käytettävissä olevalla kaistanleveydellä on rajoituksia. Kaikki nämä rajoitukset estävät yritystä tekemästä näistä kalliista asennuksista kannattavia tai tarjoamasta vakaa online-palvelintarjonta ilman datakeskuksia, jotka voivat ottaa vastuun, kun lämmitystä ei tarvita.

> Lämpö, jonka tietokoneesi tuottaa, ei ole hukkaa, jos tarvitset lämmittää kotiasi. Jos käytät sähkölämmitystä asuinpaikassasi, silloin tietokoneesi tuottama lämpö ei ole hukkaa. Se maksaa saman verran tuottaa tämä lämpö tietokoneellasi. Jos sinulla on halvempi lämmitysjärjestelmä kuin sähkölämmitys, silloin hukka on vain kustannuserossa. Jos on kesä ja käytät ilmastointia, silloin se on kaksinkertainen hukka. Bitcoinien louhinnan tulisi tapahtua siellä, missä se on halvempaa. Ehkä se on paikassa, missä ilmasto on kylmä ja missä lämmitys on sähköistä, missä louhinta muuttuu ilmaiseksi."
> Satoshi Nakamoto - 8. elokuuta 2010

Bitcoin ja sen proof of work -mekanismi erottuvat, koska ne säätävät automaattisesti louhinnan vaikeustasoa koko verkon suorittaman laskentatehon määrän perusteella. Tätä määrää kutsutaan hashrateksi ja se ilmoitetaan hasheina sekunnissa. Nykyään sen arvioidaan olevan 380 eksahashia sekunnissa, mikä on 380 miljardia miljardia hashea sekunnissa. Tämä hashrate edustaa työtä ja siten käytettyä energiamäärää. Mitä korkeampi hashrate, sitä korkeampi vaikeustaso, ja päinvastoin. Näin ollen Bitcoin-louhija voidaan aktivoida tai deaktivoida milloin tahansa ilman, että se vaikuttaa verkkoon, toisin kuin lämpöpatterit/palvelimet, jotka on pidettävä vakaina palvelunsa tarjoamiseksi. Louhija palkitaan osallistumisestaan suhteessa muihin, riippumatta siitä, kuinka pieni se saattaa olla.
Yhteenvetona voidaan todeta, että sekä sähkölämmitin että Bitcoin-louhija tuottavat 1 kW lämpöä 1 kW sähköä kuluttaen. Louhija saa kuitenkin palkkioksi bitcoineja. Riippumatta sähkön hinnasta, bitcoinin hinnasta tai kilpailusta Bitcoin-louhinnassa verkossa, taloudellisesti on edullisempaa lämmittää louhijalla kuin sähköpatterilla.

### Bitcoinin lisäarvo

On tärkeää ymmärtää, miten louhinta edistää Bitcoinin hajauttamista.
Useita olemassa olevia teknologioita on yhdistetty nerokkaasti tuomaan Nakamoton konsensus eloon. Tämä konsensus taloudellisesti palkitsee rehelliset osallistujat heidän panoksestaan Bitcoin-verkon toimintaan, samalla kun se discourages epärehellisiä osallistujia. Tämä on yksi avainkohdista, joka mahdollistaa verkon kestävän olemassaolon.
Rehelliset toimijat, ne jotka louhivat sääntöjen mukaan, kilpailevat keskenään saadakseen mahdollisimman suuren osan palkkiosta uusien lohkojen tuottamisesta. Tämä taloudellinen kannustin johtaa luonnollisesti tietynlaiseen keskittymiseen, kun yritykset päättävät erikoistua tähän tuottoisaan toimintaan vähentämällä kustannuksiaan mittakaavaetujen kautta. Nämä teolliset toimijat ovat edullisessa asemassa koneiden hankinnassa ja ylläpidossa sekä tukkumyynnin sähköhintojen neuvottelussa.

> Aluksi useimmat käyttäjät pyörittäisivät verkkosolmuja, mutta kun verkko kasvaa tietyn pisteen yli, se jäisi yhä enemmän erikoistuneiden palvelinfarmien tehtäväksi, joissa on erikoistunutta laitteistoa. Palvelinfarmi tarvitsisi vain yhden solmun verkossa ja loput LAN yhdistäisivät siihen solmuun.
>
> Satoshi Nakamoto - 2. marraskuuta 2008

Tietyt toimijat hallitsevat merkittävää prosenttiosuutta koko hashratesta suurissa louhintafarmeissa. Voimme havaita äskettäisen kylmän aallon Yhdysvalloissa, jossa merkittävä osa hashratesta otettiin pois käytöstä ohjaamaan energiaa kotitalouksiin, joilla oli poikkeuksellinen tarve sähkölle. Usean päivän ajan louhijat olivat taloudellisesti kannustettuja sammuttamaan farmejaan, ja tämä poikkeuksellinen sää näkyy Bitcoinin hashrate-käyrässä.

Tämä kysymys voisi muodostua ongelmalliseksi ja aiheuttaa merkittävän riskin verkon puolueettomuudelle. Toimija, jolla on yli 51% hashratesta, voisi helpommin sensuroida transaktioita, jos niin haluaisi. Siksi on tärkeää jakaa hashrate useiden toimijoiden kesken pikemminkin kuin keskitettyjen toimijoiden, jotka hallitus voisi esimerkiksi helpommin takavarikoida.

**Jos louhijat jakautuvat tuhansiin, jopa miljooniin, kotitalouksiin ympäri maailmaa, valtion on hyvin vaikea ottaa niitä hallintaansa.**

Tehtaasta tullessaan louhija ei sovellu käytettäväksi lämmittimenä kotona kahdesta pääongelmasta johtuen: liiallinen melu ja säädettävyyden puute. Nämä ongelmat voidaan kuitenkin helposti ratkaista laitteisto- ja ohjelmistomuutoksilla, mahdollistaen paljon hiljaisemman louhijan, joka voidaan konfiguroida ja automatisoida kuten modernit sähkölämmittimet.

**Attakaï on koulutusaloite, joka opettaa sinulle, miten voit muuttaa Antminer S9:n kustannustehokkaasti.**
Tämä on erinomainen tilaisuus oppia käytännön kautta samalla, kun saat palkkion osallistumisestasi KYC-vapaina satosheina.

## Ostajan opas käytetyn ASIC:n hankintaan

<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>

Tässä osiossa käsittelemme parhaita käytäntöjä käytetyn Bitmain Antminer S9:n ostamiseen, joka on tämän jäähdytysmuutoksen opetusohjelman perustana. Tämä opas pätee myös muihin ASIC-malleihin, sillä se on yleinen opas käytetyn louhintalaitteiston ostamiseen.

Antminer S9 on laite, jonka Bitmain on tarjonnut toukokuusta 2016 lähtien. Se kuluttaa 1400W sähköä ja tuottaa 13,5 TH/s. Vaikka sitä pidetään vanhana, se on edelleen erinomainen vaihtoehto louhinnan aloittamiseen. Koska sitä on valmistettu suurina määrinä, varaosia on helppo löytää runsaasti monilta alueilta ympäri maailmaa. Yleensä sen voi hankkia vertaisverkossa sivustoilta kuten eBay tai LeBonCoin, sillä ammattimaiset jälleenmyyjät eivät enää tarjoa sitä sen alhaisemman kilpailukyvyn vuoksi verrattuna uudempiin koneisiin. Se on vähemmän tehokas kuin ASIC:t, kuten Antminer S19, jota on tarjottu maaliskuusta 2020 lähtien, mutta tämä tekee siitä edullisen käytetyn laitteiston ja sopivamman tekemiimme muutoksiin.

Antminer S9 tulee useissa variaatioissa (i, j), jotka tekevät pieniä muutoksia ensimmäisen sukupolven laitteistoon. Emme usko, että tämän pitäisi vaikuttaa ostopäätökseesi, ja tämä opas toimii kaikille näille variaatioille.

ASIC:ien hinta vaihtelee monien tekijöiden mukaan, kuten bitcoinin hinnan, verkon vaikeusasteen, koneen tehokkuuden ja sähkön hinnan mukaan. Siksi on vaikea antaa tarkkaa arviota käytetyn koneen ostosta. Helmikuussa 2023 Ranskassa odotettu hinta yleensä vaihtelee 100 €:sta 200 €:oon, mutta nämä hinnat voivat muuttua nopeasti.

![kuva](assets/en/15.webp)

Antminer S9 koostuu seuraavista osista:

- 3 hashboardia, jotka sisältävät sirut, jotka tuottavat louhintatehon.

![kuva](assets/en/16.webp)

- Ohjauskortti, joka sisältää paikan SD-kortille, Ethernet-portin ja liittimet hashboardeille ja tuulettimille. Tämä on ASIC:isi aivot.

![kuva](assets/en/17.webp)

- 3 datakaapelia, jotka yhdistävät hashboardit ohjauskorttiin.

![kuva](assets/en/18.webp)

- Virtalähde, joka toimii 220V:lla ja voidaan kytkeä kuten tavallinen kotitalouslaite.

![kuva](assets/en/19.webp)

- 2 120mm tuuletinta.

![kuva](assets/en/20.webp)

- Uros C13-kaapeli.

![kuva](assets/en/21.webp)

Käytettyä konetta ostaessa on tärkeää tarkistaa, että kaikki osat ovat mukana ja toimivat. Vaihdon aikana sinun tulisi pyytää myyjää käynnistämään kone tarkistaaksesi sen toimivuuden. On tärkeää varmistaa, että laite käynnistyy oikein, ja sitten tarkistaa internet-yhteys kytkemällä Ethernet-kaapeli ja pääsemällä Bitmainin kirjautumisliittymään verkkoselaimen kautta samassa paikallisverkossa. Tämän IP-osoitteen löydät yhdistämällä internet-reitittimesi liittymään ja etsimällä yhdistettyjä laitteita. Tämän osoitteen tulisi olla seuraavassa muodossa: 192.168.x.x

![kuva](assets/en/22.webp)
Tarkista myös, että oletusarvoiset tunnukset toimivat (käyttäjäname: root, salasana: root). Jos oletusarvoiset tunnukset eivät toimi, sinun tarvitsee nollata laite.
![kuva](assets/en/23.webp)

Kun olet yhdistänyt, sinun pitäisi pystyä näkemään kunkin hashboardin tila hallintapaneelissa. Jos louhija on yhdistetty pooliin, sinun pitäisi nähdä kaikkien hashboardien toimivan. On tärkeää huomata, että louhijat pitävät paljon melua, mikä on normaalia. Varmista myös, että tuulettimet toimivat kunnolla.

Voit sen jälkeen poistaa edellisen omistajan louhintapoolin asettaaksesi myöhemmin oman. Halutessasi voit myös tarkastella hashboardeja purkamalla laitteen. Tämä vaihe on kuitenkin monimutkaisempi ja vaatii enemmän aikaa sekä joitakin työkaluja. Jos haluat jatkaa tämän purkamisen kanssa, voit viitata seuraavaan osaan tässä oppaassa, jossa kerrotaan, miten se tehdään. On tärkeää huomata, että louhijat keräävät paljon pölyä ja vaativat säännöllistä huoltoa. Voit havaita tämän pölyn kertymisen ja huollon laadun purkamalla laitteen.
Kaikkien näiden seikkojen tarkastelun jälkeen voit ostaa laitteesi suurella luottamuksella. Jos epäröit, konsultoi yhteisöä.

Tiivistääkseni tämän oppaan yhteen lauseeseen: **"Älä luota, varmista."**

[Voit myös kääntyä ammattilaisten puoleen, jotka ovat erikoistuneet louhintalaitteiden kunnostukseen, kuten kumppanimme 21energy. He tarjoavat testattuja S9-laitteita, jotka on puhdistettu ja joissa on jo asennettuna BraiiinOS+ -ohjelmisto. Affiliate-koodilla "decouvre" saat 10 % alennuksen S9:n ostosta samalla tukien Attakai-projektia.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Opas S9:n laitteistomuutosten hankintaan

<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>

Antminer S9:n omistajana tiedät todennäköisesti, kuinka äänekäs ja kömpelö tämä laitteisto voi olla. On kuitenkin mahdollista muuttaa se hiljaiseksi ja yhdistetyksi lämmittimeksi noudattamalla muutamia yksinkertaisia vaiheita. Tässä osiossa esittelemme tarvittavat laitteet muutosten tekemiseen.

Jos olet taitava nikkaroi ja haluat muuttaa louhijan lämmittimeksi, tämä opas on sinulle. Haluamme varoittaa, että sähkölaitteen muutokset voivat aiheuttaa sähköriskejä. On siis olennaisen tärkeää ryhtyä kaikkiin tarvittaviin varotoimiin vahinkojen tai loukkaantumisten välttämiseksi.

1. Vaihda tuulettimet

Antminer S9:n alkuperäiset tuulettimet ovat liian äänekkäitä käyttääksesi Antmineriasi lämmittimenä. Ratkaisu on vaihtaa ne hiljaisempiin tuulettimiin. Tiimimme on testannut useita malleja Noctua-merkiltä ja on valinnut Noctua NF-A14 iPPC-2000 PWM:n parhaaksi kompromissiksi. Varmista, että valitset tuulettimien 12V version. Tämä 140mm tuuletin voi tuottaa jopa 1200W lämpöä ylläpitäen teoreettisen melutason 31 dB. Asentaaksesi nämä 140mm tuulettimet, tarvitset 140mm - 120mm sovittimen, jonka löydät DécouvreBitcoin-kaupasta. Lisäämme myös 140mm suojaverkot.

![kuva](assets/en/24.webp)
![kuva](assets/en/25.webp)
![kuva](assets/en/26.webp)
Virtalähteen tuuletin on myös melko äänekäs ja se täytyy vaihtaa. Suosittelemme Noctua NF-A6x25 PWM -mallia. Huomaa, että Noctuan tuulettimien liittimet eivät ole samanlaisia kuin alkuperäisissä, joten tarvitset liitinsovittimen niiden kytkemiseen. Kaksi riittää. Varmista jälleen, että valitset tuulettimen 12V version.
![kuva](assets/en/27.webp)
![kuva](assets/en/28.webp)

2. Lisää WIFI/Ethernet-silta

Ethernet-kaapelin sijaan voit yhdistää Antminerisi WIFIin lisäämällä WIFI/Ethernet-sillan. Olemme valinneet vonets vap11g-300 -mallin, koska se mahdollistaa helposti WIFI-signaalin vastaanottamisen Internet-laitteestasi ja lähettämisen Antminerillesi Ethernetin kautta luomatta aliverkkoa. Jos sinulla on sähkötekniikan taitoja, voit kytkeä sen suoraan Antminerisi virtalähteeseen ilman USB-laturin lisäämistä. Tätä varten tarvitset naaraspuolisen 5.5mmx2.1mm jakin.

![kuva](assets/en/29.webp)
![kuva](assets/en/30.webp)

3. Vaihtoehtoinen: lisää älypistoke
   Jos haluat kytkeä Antminerisi päälle/pois päältä älypuhelimestasi ja seurata sen energiankulutusta, voit lisätä älypistokkeen. Testasimme ANTELA-pistoketta 16A versiossa, joka on yhteensopiva smartlife-sovelluksen kanssa. Tämä älypistoke mahdollistaa päivittäisen ja kuukausittaisen energiankulutuksen tarkastelun ja yhdistää suoraan internet-reitittimeesi WiFi-yhteyden kautta.

![kuva](assets/en/31.webp)

Laitteiden ja linkkien luettelo

- 2X 3D-sovitinkappale 140mm to 120mm

- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

- [2X 140mm tuuletinsuojat](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
- [Sähköasentajan sokeri 2.5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Valinnainen ANTELA älypistoke](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - Antminer S9 -ohjelmiston muokkaus

<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>

## Vonet WIFI/Ethernet-sillan asennus

<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>

ASIC:n yhdistämiseksi WIFI-verkkoon tarvitset laitteen, jota kutsutaan sillaksi. Tämä laite mahdollistaa WIFI-signaalin vastaanottamisen reitittimeltäsi ja sen lähettämisen toiselle laitteelle Ethernetin kautta.

Monet laitteet voivat suorittaa tämän toiminnon, mutta suosittelemme VONETS WiFi-siltaa/toistinta sen kätevyyden vuoksi.

Virran saamiseksi sillalle, yhdistä se USB:n kautta.

Tietokoneeltasi, yhdistä VONETS\_**\*\*** WIFI-verkkoon salasanalla 12345678.

![kuva](assets/en/32.webp)

Kirjaudu sisään käyttäjänimellä "admin" ja salasanalla "admin".

![kuva](assets/en/33.webp)

Valitse Wizard.

![kuva](assets/en/34.webp)

Valitse WIFI-verkko, johon haluat yhdistää louhintalaitteesi, ja klikkaa Seuraava.

HUOM: Vonet-silta toimii vain 2.4GHz taajuudella. Nykyään reitittimet tarjoavat yleensä kaksi WIFI-verkkoa, yhden 2.4GHz ja toisen 5GHz taajuudella.

![kuva](assets/en/35.webp)

Anna WIFI-verkkosi salasana "Lähde-WIFI-hotspotin salasana" -kenttään. Jos et halua käyttää Vonet-siltaasi laajentaaksesi WIFI-verkkoasi, valitse "Poista hotspot käytöstä" -ruutu. Muussa tapauksessa jätä se valitsematta.

Voit sen jälkeen klikata Käytä.

Lopuksi, klikkaa uudelleenkäynnistä restartataksesi sillan. Uudelleenkäynnistyminen kestää muutaman minuutin.

Silta pitäisi yhdistää reitittimeesi ja näkyä nimellä "[VONETS.COM](http://vonets.com/)". Jos se ei vieläkään yhdistä muutaman minuutin jälkeen, saatat joutua irrottamaan/liittämään sillan uudelleen.
Kun silta on yhdistetty, kytke Ethernet-kaapeli sillasta ASIC-laitteeseesi ja kytke sitten ASIC virtalähteeseen. Tämän jälkeen voit käyttää ASIC-laitteen käyttöliittymää samalla tavalla kuin jos se olisi suoraan yhdistetty reitittimeesi Ethernetin kautta.

## Antminer S9:n nollaaminen

<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>

Ennen BraiinOS+:n asentamista voi olla tarpeen nollata S9 tehdasasetuksiinsa.
Tämä menetelmä voidaan soveltaa 2 minuutista 10 minuuttiin louhijan käynnistämisen jälkeen.
2 minuuttia louhijan käynnistämisen jälkeen, paina "Reset"-nappia 5 sekunnin ajan ja vapauta se sitten. Louhija palautuu tehdasasetuksiin 4 minuutin kuluessa ja käynnistyy uudelleen automaattisesti (sitä ei tarvitse sammuttaa).

![kuva](assets/en/36.webp)

## BraiinsOS+:n asentaminen Antminer S9:ään

<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>

Antminerin louhintakoneisiin asennettu alkuperäinen ohjelmisto on rajallinen toiminnallisuudeltaan. Siksi tässä oppaassa asennamme toisen ohjelmiston nimeltä BraiinsOS+. Se on kolmannen osapuolen kehittämä ohjelmisto, joka on peräisin ensimmäisestä Bitcoin-louhintapoolista ja tarjoaa enemmän ominaisuuksia, mahdollistaen esimerkiksi koneen tehon muokkaamisen.

ASIC-laitteeseen on useita tapoja asentaa Braiins OS+. Voit viitata tähän oppaaseen sekä [viralliseen Braiins-dokumentaatioon](https://academy.braiins.com/en/braiins-os/about/).

Tässä näemme, miten Braiins OS+ voidaan helposti asentaa suoraan Antminerisi muistiin käyttäen BOS toolbox -ohjelmistoa, korvaten alkuperäisen käyttöjärjestelmän, alla olevien yksityiskohtaisten vaiheiden kautta.

1. Kytke Antminerisi päälle ja yhdistä se internet-laatikkoosi.
2. Lataa BOS toolbox Windowsille / Linuxille.
3. Pura ladattu tiedosto ja avaa bos-toolbox.bat-tiedosto. Valitse kieli, ja muutaman hetken kuluttua näet tämän ikkunan:

![kuva](assets/en/37.webp)

4. Bos toolbox mahdollistaa Antminerisi IP-osoitteen helposti löytämisen ja BraiinsOS+:n asentamisen. Jos tiedät jo koneesi IP-osoitteen, voit siirtyä suoraan vaiheeseen 8. Muussa tapauksessa siirry skannaus-välilehdelle.

![kuva](assets/en/38.webp)

5. Yleensä kotiverkoissa IP-osoitealue on välillä 192.168.1.1 ja 192.168.1.255, joten syötä "192.168.1.0/24" IP-aluekenttään. Jos verkkosi on erilainen, muuta näitä osoitteita vastaavasti. Klikkaa sitten "Aloita".

6. Huomio, jos Antminerissa on salasana, havaitseminen ei toimi. Jos näin on, yksinkertaisin ratkaisu on suorittaa nollaus.

7. Sinun pitäisi nähdä kaikki verkkosi Antminerit tässä, ja IP-osoite on 192.168.1.37.

![kuva](assets/en/39.webp)

8. Klikkaa "Takaisin" ja sitten "Asenna"-välilehteä, syötä aiemmin löydetty IP-osoite ja klikkaa "Aloita".

> Jos asennus ei toimi, voi olla tarpeen suorittaa nollaus ja yrittää uudelleen (katso edellinen osio).
> ![kuva](assets/en/40.webp) 9. Hetken kuluttua Antminerisi käynnistyy uudelleen, ja pääset käsiksi Braiins OS+ -käyttöliittymään määritetyssä IP-osoitteessa, tässä tapauksessa 192.168.1.37, suoraan selaimen osoiteriviltä. Oletuskäyttäjänimi on "root" eikä oletussalasanaa ole.

## BraiinsOS+:n konfigurointi

<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>

Sinun täytyy yhdistää ASIC-laitteeseesi käyttäen laitteesi paikallista IP-osoitetta verkossasi selaimen kautta.

Voit löytää koneesi IP-osoitteen käyttämällä BOS toolbox -työkalua tai suoraan reitittimesi verkkosivulta.

Oletustunnukset ovat samat kuin alkuperäisessä käyttöjärjestelmässä.

- käyttäjäname: root
- salasana: (ei ole)

Tämän jälkeen sinut toivottaa tervetulleeksi Braiins OS+ -hallintapaneeli.

### Hallintapaneeli

![kuva](assets/en/41.webp)

Tällä ensimmäisellä sivulla voit tarkkailla koneesi reaaliaikaista suorituskykyä.

- Kolme reaaliaikaista graafia, jotka näyttävät koneesi lämpötilan, hashraten ja yleisen tilan.
- Oikealla, todellinen hashrate, piirien keskimääräinen lämpötila, arvioitu tehokkuus W/THs:ssa ja virrankulutus.
- Alla, tuulettimen nopeus prosentteina maksiminopeudesta ja kierrosten määrä minuutissa.

![kuva](assets/en/42.webp)

- Alempana löydät yksityiskohtaisen näkymän kustakin hashboardista. Lautan keskimääräinen lämpötila ja sen sisältämien piirien lämpötila sekä jännite ja taajuus.
- Tiedot aktiivisista louhintapoolista Pools-osiossa.
- Autotunauksen tila Tuner Status -osiossa.
- Oikealla, tiedot poolille lähetetystä datasta.

### Konfiguraatio

![kuva](assets/en/43.webp)

### Järjestelmä

![kuva](assets/en/44.webp)

### Pikatoiminnot

![kuva](assets/en/45.webp)

# Attakai - Tuulettimen muokkaus

<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>

## Virtalähteen tuulettimen vaihto

<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>

> VAROITUS: On välttämätöntä, että olet aiemmin asentanut Braiins OS+:n tai jonkin muun ohjelmiston, joka voi vähentää koneesi suorituskykyä. Tämä toimenpide on kriittinen, koska melun vähentämiseksi asennamme vähemmän tehokkaita tuulettimia, jotka voivat hajottaa vähemmän lämpöä.

![kuva](assets/en/46.webp)

### Tarvittavat materiaalit

- 1 Noctua NF-A6x25 PWM -tuuletin
- 2,5mm2 sähköasentajan sokeri

> VAROITUS: Ennen aloittamista, varmista, että olet irrottanut louhijan virtalähteestä välttääksesi sähköiskun vaaran.

![kuva](assets/en/47.webp)

Ensimmäiseksi, poista 6 ruuvia kotelon sivulta, jotka pitävät sen kiinni. Kun ruuvit on poistettu, avaa kotelo varovasti poistaaksesi muovisuojan, joka peittää komponentit.

![kuva](assets/en/48.webp)
![kuva](assets/en/49.webp)

Seuraavaksi on aika poistaa alkuperäinen tuuletin varoen, ettei vahingoita muita komponentteja. Tee tämä poistamalla ruuvit, jotka pitävät sitä paikallaan ja varovasti irrottamalla valkoinen liima liittimen ympäriltä. On tärkeää edetä varoen välttääkseen johtojen tai liittimien vahingoittamisen.
![kuva](assets/en/50.webp)
Kun alkuperäinen tuuletin on poistettu, huomaat, että uuden Noctua-tuulettimen liittimet eivät vastaa alkuperäisen tuulettimen liittimiä. Uudessa tuulettimessa on nimittäin 3 johtoa, mukaan lukien keltainen johto, joka mahdollistaa nopeudensäädön. Tätä johtoa ei kuitenkaan käytetä tässä tapauksessa. Uuden tuulettimen liittämiseksi suositellaan siis erityisen sovittimen käyttöä. On kuitenkin tärkeää huomata, että tämän sovittimen löytäminen voi joskus olla vaikeaa.

![kuva](assets/en/51.webp)

Jos sinulla ei ole tätä sovitinta, voit silti jatkaa uuden tuulettimen liittämistä käyttämällä sähköasentajan sokeripalaa. Tätä varten sinun on leikattava vanhan ja uuden tuulettimen kaapelit.

![kuva](assets/en/52.webp)
![kuva](assets/en/53.webp)

Uudessa tuulettimessa käytä leikkuria ja leikkaa varovasti pääsuojan ääriviivat 1cm:n kohdalta leikkaamatta alla olevien johtojen suojia.

![kuva](assets/en/54.webp)

Vedä sitten pääsuoja alaspäin ja leikkaa punaisen ja mustan kaapelin suojat samalla tavalla kuin aiemmin. Ja leikkaa keltainen kaapeli tasaiseksi.

![kuva](assets/en/55.webp)

Vanhan tuulettimen kohdalla on hankalampaa leikata pääsuoja vahingoittamatta punaisen ja mustan johdon suojia. Tätä varten käytimme neulaa, jonka liu'utimme pääsuojan ja punaisen sekä mustan johdon väliin.

![kuva](assets/en/56.webp)
![kuva](assets/en/57.webp)

Kun punaisen ja mustan johdon suojat ovat paljaana, leikkaa suojat varovasti välttääksesi sähköjohtojen vahingoittamisen.

![kuva](assets/en/58.webp)

Yhdistä sitten johdot sokeripalalla, musta johto mustaan ja punainen johto punaiseen. Voit myös lisätä sähköteippiä.

![kuva](assets/en/59.webp)
![kuva](assets/en/60.webp)

Kun liitäntä on tehty, on aika asentaa uusi Noctua-tuuletin ritilän ja vanhojen ruuvien kanssa. Paketissa olevat uudet ruuvit käytetään myöhemmin uudelleen. Varmista, että asennat sen oikeaan suuntaan. Huomaat tuulettimen toisella puolella nuolen, joka osoittaa ilmavirran suunnan. On tärkeää asettaa tuuletin siten, että tämä nuoli osoittaa kotelon sisäpuolelle. Kytke sitten tuuletin uudelleen.

![kuva](assets/en/61.webp)
![kuva](assets/en/62.webp)

> Vaihtoehtoisesti: Jos sinulla on sähkötekniikan tietämystä, voit suoraan lisätä naaras 5,5mm jakkiliittimen 12V virtalähteeseen, joka virtalähtee suoraan Vonet Wi-Fi -sillan. Jos kuitenkin epäilet sähkötekniikan taitojasi, on turvallisempaa käyttää USB-liitintä älypuhelintyypin laturin kanssa välttääksesi oikosulun tai sähkövahingon riskin.

![kuva](assets/en/63.webp)

Kun liitännät on tehty, aseta muovikansi kotelon muovin päälle eikä sisään.

![kuva](assets/en/64.webp)

Lopuksi, aseta kotelon kansi takaisin paikalleen ja kiristä sivuilla olevat 6 ruuvia pitämään kaikki paikoillaan. Ja siinä se on, virtalähteesi kotelossa on nyt uusi tuuletin.

## Päätuulettimien vaihtaminen

<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>

> VAROITUS: On välttämätöntä, että olet asentanut Braiins OS+:n tai muun ohjelmiston, joka kykenee alentamaan koneesi suorituskykyä, louhijaasi ennen tätä toimenpidettä. Tämä toimenpide on kriittisen tärkeä, sillä melun vähentämiseksi asennamme vähemmän tehokkaita tuulettimia, jotka hajottavat vähemmän lämpöä.
> ![kuva](assets/en/46.webp)

### Tarvittavat Materiaalit

- 2 kpl 3D-sovitinta 140mm - 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM -tuuletinta
- 2 kpl 140mm tuuletinsuojaa

> VAROITUS: Ennen aloittamista, varmista että olet irrottanut louhijan virtalähteestä välttääksesi sähköiskun vaaran.

1. Irrota ensin tuulettimet ja ruuvaa ne irti.

![kuva](assets/en/65.webp)

2. Uusien Noctua-tuulettimien liittimet eivät vastaa alkuperäisiä, mutta älä huoli! Ota veitsesi esiin ja leikkaa varovasti pienet muoviset välilehdet pois, jotta liittimet sopivat täydellisesti louhijaasi.

![kuva](assets/en/66.webp)
![kuva](assets/en/67.webp) 3. On aika asentaa 3D-osat!
Kiinnitä ne louhijan molemmille puolille käyttäen tuulettimista irrottamiasi ruuveja. Ruuvaa ne sisään, kunnes ruuvin pää on tasainen 3D-osan kanssa ja se on varmasti paikoillaan. Ole varovainen, ettet kiristä liikaa, sillä saatat vahingoittaa osaa ja yksi ruuveista saattaa koskettaa kondensaattoria!

![kuva](assets/en/68.webp)

4. Nyt siirrytään tuulettimiin.

Kiinnitä ne 3D-osiin mukana tulleilla ruuveilla. Kiinnitä huomiota ilmavirran suuntaan, tuulettimien sivuilla olevat nuolet osoittavat suunnan. Mene Ethernet-portin puolelta toiselle puolelle. Katso alla oleva kuva.

![kuva](assets/en/69.webp)
![kuva](assets/en/70.webp)
![kuva](assets/en/71.webp)

5. Viimeinen vaihe: yhdistä tuulettimet ja kiinnitä suojukset päälle käyttäen ruuveja, joita ei käytetty virtalähteen tuulettimen laatikossa. Sinulla on niitä vain 4, mutta 2 per suojus vastakkaisissa kulmissa riittää. Tarvittaessa voit etsiä samankaltaisia ruuveja rautakaupasta.

![kuva](assets/en/72.webp)
![kuva](assets/en/73.webp)

Odottaessasi, että voimme tarjota tyylikkäämmän kotelon uudelle lämmittimellesi, voit kiinnittää kotelon ja virtalähteen sähköasentajan nippusiteillä.

![kuva](assets/en/74.webp)

Ja viimeisenä silauksena, yhdistä Vonet-silta Ethernet-porttiin ja sen virtalähteeseen.

![kuva](assets/en/75.webp)

Ja siinä se, onneksi olkoon! Olet juuri vaihtanut louhijasi koko mekaanisen osan. Nyt sinun pitäisi kuulla huomattavasti vähemmän melua.

# Attakai - Kokoonpano

<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>

## Liittyminen louhintapooliin

<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>

Voit ajatella louhintapoolia maatalousosuuskuntana. Maanviljelijät kokoavat tuotantonsa yhteen vähentääkseen tarjonnan ja kysynnän vaihtelua ja saadakseen siten vakautetumpia tuloja toiminnalleen. Louhintapooli toimii samalla tavalla, jaettuna resurssina ovat hashit. Todellakin, yhden kelvollisen hashin löytäminen mahdollistaa lohkon luomisen ja coinbase-palkinnon tai -palkkion voittamisen, joka on tällä hetkellä 6,25 BTC plus lohkoon sisältyvät siirtomaksut.
Jos louhit yksin, saat palkkion vain, kun löydät lohkon. Kilpaillessasi kaikkia muita maailman louhijoita vastaan, sinulla olisi hyvin vähän mahdollisuuksia voittaa tämä arpajainen, ja sinun täytyisi silti maksaa louhijasi käyttöön liittyvät maksut ilman menestyksen takeita. Louhintapoolit ratkaisevat tämän ongelman yhdistämällä useiden (tuhansien) louhijoiden laskentatehon ja jakamalla palkinnot osallistumisprosentin mukaan poolin hashratesta, kun lohko löydetään. Visualisoidaksesi mahdollisuutesi louhia lohko yksin, voit käyttää tätä työkalua. Syöttämällä tiedot Antminer S9:stä, voimme nähdä, että mahdollisuudet löytää hash, joka mahdollistaa lohkon luomisen, ovat 1 24 777 849:stä jokaista lohkoa kohden tai 1 172 068:ssa päivässä. Keskimäärin (jatkuvalla hashratella ja vaikeudella) kestäisi 471 vuotta löytää lohko.

Kuitenkin, koska kaikki Bitcoinissa perustuu todennäköisyyteen, joskus käy niin, että yksin louhivat saavat palkkion tämän riskin ottamisesta: Yksinäinen Bitcoin-louhija ratkaisee lohkon vain 10 TH/s:n hashratella, voittaen erittäin epätodennäköiset mahdollisuudet – Decrypt

Jos pidät uhkapelaamisesta, voit kokeilla, mutta oppaamme ei keskity siihen suuntaan. Sen sijaan keskitymme louhintapooliin, joka parhaiten vastaa tarpeitamme luoda lämmitysjärjestelmä.

Louhintapoolia valittaessa huomioon otettavia seikkoja ovat poolin palkkioiden toiminta, joka voi vaihdella, sekä vähimmäismäärä ennen kuin palkkioita voidaan nostaa osoitteeseen. Esimerkiksi Braiins, joka tarjoaa tässä keskustelemamme ohjelmiston, tarjoaa myös poolin. Tällä poolilla on palkkiojärjestelmä nimeltä "Score", joka kannustaa louhijoita louhimaan pitkiä aikoja. Osallistuminen sisältää käyttöajan tekijän, joka ilmaistaan "scoring hashratena". Tapauksessamme, kun haluamme lämmitysjärjestelmän, joka voidaan kytkeä päälle vain muutamaksi minuutiksi, tämä ei ole ihanteellinen palkkiojärjestelmä. Suosimme palkkiojärjestelmää, joka antaa meille saman palkkion jokaisesta osallistumisesta. Lisäksi Braiins Poolin vähimmäisnostomäärä on 100 000 satsia ja On-Chain. Joten menetämme joitakin satseja siirtomaksuissa ja osa palkkiostamme voi jäädä lukkoon, jos emme louhi tarpeeksi talven aikana.

Meitä kiinnostava palkkiomalli on PPS, joka tarkoittaa "pay-per-share" eli maksa per osuus. Tämä tarkoittaa, että louhija saa palkkion jokaisesta kelvollisesta osuudesta. Tästä järjestelmästä on myös variantti, FPPS (Full Pay Per Share), joka jakaa paitsi coinbase-palkkion myös lohkoon sisältyvät siirtomaksut. Louhintapoolit, joita suosittelemme yhdistämään louhinta-/lämmitysjärjestelmääsi, ovat Linecoin Pool (FPPS) ja Nicehash (PPS).

- Nicehash: Nicehashin etuna on, että nostot voidaan tehdä Lightningin kautta minimaalisin maksuin. Lisäksi vähimmäisnostomäärä on 2000 satsia. Haittapuolena on, että Nicehash käyttää hashrateaan tuottoisimpaan lohkoketjuun antamatta todellista kontrollia käyttäjälle, joten se ei välttämättä edistä Bitcoinin hashratea.
- Linecoin: Linecoinin etuna on tarjottavien ominaisuuksien määrä, kuten yksityiskohtainen hallintapaneeli, mahdollisuus tehdä nostoja Paynymilla (BIP 47) paremman yksityisyydensuojan saavuttamiseksi, sekä Telegram-botin integrointi ja suoraan mobiilisovelluksessa konfiguroitavat automaatiot. Tämä allas louhii ainoastaan Bitcoin-lohkoja, mutta nostojen vähimmäismäärä pysyy korkeana, 100 000 satoshissa. Tarkastelemme yhden näistä altaista käyttöliittymää tarkemmin tulevassa artikkelissa.
  Braiins OS+:n avulla altaan konfiguroimiseksi sinun on luotava tili valitsemassasi altaassa. Tässä otamme esimerkiksi Linecoinin:

![kuva](assets/en/76.webp)

Kun tilisi on luotu, klikkaa Yhdistä Altaaseen

Kopioi sitten Stratum-osoite ja käyttäjänimesi:

![kuva](assets/en/77.webp)

Voit nyt palata Braiins OS+ -käyttöliittymään syöttääksesi nämä tunnistetiedot. Salasanakentän voit jättää tyhjäksi.

![kuva](assets/en/78.webp)

## Antminer S9:n suorituskyvyn optimointi

<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>

Sekä ylikellotus että automaattinen säätö sisältävät hash-lautojen taajuuksien säätämisen ASIC:n suorituskyvyn parantamiseksi. Erot näiden kahden välillä liittyvät taajuusasetusten monimutkaisuuteen.

Ylikellotus on yksinkertainen säätö, joka sisältää hash-lautojen taajuuden nostamisen koneen hash-nopeuden kasvattamiseksi. Alakellotus puolestaan tarkoittaa integroidun piirin kellotaajuuden alentamista sen nimellistaajuuden alapuolelle. ASIC:n kellotaajuuden alentamisen myötä laitteiston tuottama lämpö vähenee. Tämä mahdollistaa ASIC:n jäähdyttämiseen tarvittavien tuulettimien nopeuden vähentämisen, koska niiden ei tarvitse työskennellä yhtä kovasti sopivan lämpötilan ylläpitämiseksi. Tuulettimien nopeuden vähentäminen vähentää myös ASIC:n tuottamaa melua. Tämä voi olla erityisen hyödyllistä käyttäjille, jotka käyttävät ASIC-laitteita kotona ja haluavat minimoida louhintalaitteiston aiheuttamat meluhäiriöt.

Braiins OS+ tukee ASIC-laitteiden ylikellotusta, alakellotusta ja automaattista säätöä. Se mahdollistaa käyttäjien säätää laitteistonsa kellotaajuutta joustavasti maksimoidakseen suorituskyvyn tai säästääkseen energiaa heidän mieltymystensä mukaan.

### Antminer S9:n suorituskyvyn optimointi automaattisella säädöllä

Ennen vuotta 2018 louhijat saivat etua toiminnassaan kahdella tavalla: löytämällä sähkön kohtuulliseen hintaan ja ostamalla tehokkaampaa laitteistoa. Kuitenkin vuonna 2018 löydettiin uusi edistysaskel louhintalaitteiston ohjelmisto- ja laiteohjelmistosektorilla, nimeltään AsicBoost. Tämä tekniikka mahdollistaa louhijoiden vähentää kustannuksiaan noin 13% muokkaamalla laitteissaan toimivaa laiteohjelmistoa.

Nykyään on olemassa uusi edistysaskel ohjelmisto- ja laiteohjelmistosektorilla louhinnassa, nimeltään automaattinen säätö, joka tarjoaa vielä suuremman edun kuin AsicBoost. ASICit koostuvat monista pienistä tietokonepiireistä, jotka suorittavat hashauksen. Nämä piirit on valmistettu piistä, samaa alkuainetta, jota käytetään laajalti puolijohteissa ja muissa mikroelektronisissa komponenteissa. Keskeinen ymmärrys tässä on, että kaikki pii-piirit eivät ole identtisiä, vaan jokainen voi vaihdella hieman sähköisissä ominaisuuksissaan. Laitteistovalmistajat ovat tietoisia tästä ja julkaisevat louhintakoneidensa suorituskykyspesifikaatiot perustuen niiden toleranssien alarajaan. Toisin sanoen, valmistajat tietävät taajuuden, joka toimii parhaiten keskimääräisille piireille, ja he käyttävät tätä taajuutta yhtenäisesti kaikissa koneen piireissä.
Tämä asettaa ylärajan koneen hash-nopeudelle. Autotuning on prosessi, jossa algoritmit arvioivat optimaaliset taajuudet sirukohtaiselle hashaukselle, sen sijaan että koko konetta kohdeltaisiin yhtenä yksikkönä. Tämä tarkoittaa, että korkealaatuisempi siru, joka pystyy suorittamaan enemmän hasheja sekunnissa, saa korkeamman taajuuden, ja alhaisemman laadun siru, joka pystyy suorittamaan suhteellisesti vähemmän hasheja, saa alhaisemman taajuuden. Sirutason autotuning on käytännössä tapa optimoida ASIC:n suorituskykyä sen päällä toimivan ohjelmiston ja firmwaren avulla.

Lopputuloksena on korkeampi hash-nopeus wattia kohden, mikä tarkoittaa suurempia voittomarginaaleja louhijoille. Syy siihen, miksi koneita ei jaeta tämän tyyppisen ohjelmiston kanssa, on se, että koneiden vaihtelu on epätoivottavaa, koska asiakkaat haluavat tietää tarkalleen, mitä he saavat, joten valmistajille on huono idea myydä tuotetta, jolla ei ole johdonmukaista ja ennustettavaa suorituskykyä koneesta toiseen. Lisäksi sirutason autotuning vaatii huomattavia kehitysresursseja, sillä sen toteuttaminen on monimutkaista. Valmistajat käyttävät jo paljon resursseja kehittäessään omia firmwarejaan. On olemassa ohjelmistoratkaisuja, jotka mahdollistavat autotuningin, kuten Braiins OS+. Lisäksi ASIC-suorituskyvyn parantaminen jopa 20%:lla.

# Yhteenveto

<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>

## Arvioi tämä kurssi

<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>
<isCourseReview>true</isCourseReview>

## Loppukoe

<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>
<isCourseExam>true</isCourseExam>

## Yhteenveto

<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>
Onnittelut kurssin suorittamisesta!

Olemme iloisia, että olet saavuttanut tämän tärkeän virstanpylvään oppimismatkallasi.

Omistautumisesi ja sitoutumisesi ansiosta olet saanut arvokasta tietoa ja taitoja, jotka palvelevat sinua ammatillisessa kehityksessäsi.

Jatkaaksesi Bitcoin-maailman syvällistä tutkimista, kutsumme sinut tutustumaan kaikkiin muihin Plan ₿ Networkissa saatavilla oleviin kursseihin:

#### Tutustu Bitcoiniin ja sen perusteisiin kurssilla

https://planb.network/courses/btc101

#### Tutustu Lightning Networkiin kurssilla

https://planb.network/courses/lnp201

#### Hallitse Bitcoinin yksityisyyden periaatteet

https://planb.network/courses/btc204

#### Tutustu Bitcoinin alkuperän historiaan kurssilla

https://planb.network/courses/his201

#### Ymmärrä, miten Bitcoin-lompakko toimii, kurssilla

https://planb.network/courses/cyp201
