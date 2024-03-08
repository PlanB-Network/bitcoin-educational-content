---
name: Johdanto Bitcoin-louhintaan
goal: Ymmärrä louhintateollisuuden toiminta käytännön harjoituksen kautta, jossa kierrätetään ASICeja.
objectives:
  - Ymmärrä louhinnan taustalla oleva teoria
  - Ymmärrä louhintateollisuus
  - Muunna S9-louhija lämmittimeksi
  - Louhi ensimmäinen satoshisi
---

# Ensiaskeleesi louhinnassa!

Tässä koulutuksessa sukellamme louhintateollisuuteen demystifioidaksemme tämän monimutkaisen aiheen! Koulutus on kaikille avoin eikä vaadi alkuinvestointia.

Ensimmäinen osio on teoreettinen, jossa Ajelex ja minä käymme syvällistä keskustelua louhintaan liittyvistä eri aiheista. Tämä auttaa meitä ymmärtämään paremmin tätä teollisuudenalaa sekä siihen liittyviä taloudellisia ja geopoliittisia kysymyksiä.
Toisessa osiossa käsittelemme käytännön tapausta. Opimme nimittäin muuntamaan käytetyn S9-louhijan kotilämmitysjärjestelmäksi! Kirjallisten ohjeiden ja videoiden avulla näytämme ja selitämme kaikki tarvittavat vaiheet tämän toteuttamiseksi kotona :)

Tämän videon kautta toivomme näyttävämme, että louhintateollisuus on monimutkaisempi kuin miltä se vaikuttaa, ja sen tutkiminen auttaa hienosäätämään siihen liittyvää ekologista keskustelua!
Jos tarvitset apua asennuksessasi, opiskelijoille on luotu Telegram-ryhmä, ja kaikki tarvittavat komponentit löytyvät e-kauppapaikaltamme!

+++

# Johdanto

## Tervetuloa!

Tervetuloa MINING 201: johdatus louhintaan. Ajelex, Jim & Rogzy ovat innoissaan saadessaan seurata sinua ensimmäisillä konkreettisilla askeleillasi tässä uudessa teollisuudenalassa. Toivomme, että nautit kurssista ja liityt kotilouhinnan seikkailuun!

### Kurssin Yleiskatsaus

Tässä kurssissa ensimmäinen osio keskittyy louhinnan teoriaan Ajelexin kanssa. Käymme syvällisiä keskusteluja louhintaan liittyvistä eri aiheista, mikä auttaa meitä ymmärtämään paremmin tätä teollisuudenalaa sekä siihen liittyviä taloudellisia ja geopoliittisia kysymyksiä.

Toisessa osiossa ryhdymme kiehtovaan käytännön tapaukseen, opimme muuntamaan käytetyn S9-louhijan kotilämmitysjärjestelmäksi. Kirjallisten ohjeiden ja videoiden avulla kaikki tarvittavat vaiheet selitetään huolellisesti, varmistaen menestyksesi tässä innovatiivisessa projektissa.

Tämä oppimismatka näyttää sinulle, että louhintateollisuus on monimutkaisempi kuin miltä se näyttää, tarjoten tasapainoisen näkökulman siihen liittyvään ekologiseen keskusteluun. Jatkuva apu on saatavilla opiskelijoille omistetun Telegram-ryhmän kautta, ja kaikki tarvittavat komponentit ovat helposti saatavilla e-kauppapaikaltamme.

### Opetussuunnitelma:

Teoreettinen osio:
* Louhinnan selitys.
* Louhintateollisuus.
* Louhintateollisuuden vivahteet.
* Louhinta Bitcoin-protokollassa.
* Bitcoinin hinta ja hashrate, korrelaatio? Suvereniteetti ja sääntely
* Haastattelu louhintateollisuuden ammattilaisen kanssa

Käytännön osio: Attakai
* Johdanto Attakaihin.
* Osto-opas.
* Antminer S9:n ohjelmiston muokkaus.
* Tuulettimien vaihto melun vähentämiseksi.
* Poolin konfigurointi.
* Antminer S9:n konfigurointi Braiins OS+:lla.

Valmis sukeltamaan tähän kiehtovaan seikkailuun? Sukelletaan yhdessä kotilouhinnan mielenkiintoiseen maailmaan!

# Kaikki mitä sinun tarvitsee tietää louhinnasta

## Louhinnan selitys

![Mikä on Bitcoin-louhinta?](https://www.youtube.com/watch?v=neEQzEQzmPQ)

### Louhinnan selitys: Palapeli-analogia
Selittääkseni kaivostoiminnan konseptia yksinkertaistetulla tavalla, voidaan käyttää osuvaa analogiaa: palapeliä. Aivan kuten palapeli, kaivostoiminta on monimutkainen tehtävä suorittaa, mutta helppo varmistaa kerran valmistuttuaan. Bitcoinin kaivostoiminnan kontekstissa kaivostyöläiset pyrkivät nopeasti ratkaisemaan digitaalisen palapelin. Ensimmäinen kaivostyöläinen, joka ratkaisee palapelin, esittää ratkaisunsa koko verkolle, joka voi sitten helposti varmistaa sen pätevyyden. Tämä onnistunut varmistus mahdollistaa kaivostyöläisen uuden lohkon vahvistamisen ja lisäämisen Bitcoinin aikaketjuun. Työnsä tunnustuksena, joka sisältää merkittäviä kustannuksia, kaivostyöläinen palkitaan tietyn määrän bitcoineja. Tämä palkkio toimii taloudellisena kannustimena kaivostyöläisille jatkaa transaktioiden vahvistamista ja Bitcoin-verkon turvaamista.
![kuva](assets/overview/puzzle.png)

Alun perin Bitcoin-verkossa palkinto oli 50 bitcoinia joka kymmenes minuutti, rinnakkain lohkon löytämisen kanssa joka kymmenes minuutti keskimäärin kaivostyöläisten toimesta. Tämä palkkio puolittuu joka 210 000 lohkon jälkeen, suunnilleen joka neljäs vuosi. Tämä korvaus toimii voimakkaana kannustimena rohkaista kaivostyöläisiä osallistumaan kaivostoimintaan huolimatta sen energiakustannuksista. Ilman palkkiota energiavaltaisesta kaivostoiminnasta luovuttaisiin, vaarantaen koko Bitcoin-verkon turvallisuuden ja vakauden.
Nykyinen kaivospalkkio on kaksiosainen. Toisaalta se sisältää uusien bitcoinien luomisen, joka on vähentynyt 50 bitcoinista joka kymmenes minuutti alun perin 6,25 bitcoiniin tänään (2023). Toisaalta se sisältää transaktiomaksut eli kaivosmaksut transaktioista, jotka kaivostyöläinen valitsee sisällyttää lohkoonsa. Kun bitcoin-transaktio tehdään, maksetaan transaktiomaksut. Nämä maksut toimivat eräänlaisena huutokauppana, jossa käyttäjät ilmoittavat, kuinka paljon he ovat valmiita maksamaan transaktionsa sisällyttämisestä seuraavaan lohkoon. Maksimoidakseen palkkionsa, kaivostyöläiset, omien etujensa mukaisesti, valitsevat tuottoisimmat transaktiot sisällytettäväksi lohkoon, ottaen huomioon rajallisen käytettävissä olevan tilan. Näin ollen kaivospalkkio koostuu sekä uusien bitcoinien luomisesta että transaktiomaksuista, varmistaen jatkuvan kannustimen kaivostyöläisille ja takaen Bitcoin-verkon pitkäikäisyyden ja turvallisuuden.

### Kaivostyöläiset ja heidän työkalunsa: Kaivostoiminta

Kaivostoimintaprosessi sisältää kelvollisen hashin löytämisen, joka on hyväksyttävä Bitcoin-verkolle. Kertaalleen laskettuna ja löydettynä, tämä hash on peruuttamaton, samankaltainen kuin perunoiden muuttaminen perunamuusiksi. Se varmistaa tietyn toiminnon ilman mahdollisuutta palata takaisin. Kaivostyöläiset kilpailevat käyttäen koneita näiden hashien laskemiseen. Vaikka teoriassa on mahdollista löytää tämä hash käsin, toiminnan monimutkaisuus tekee tästä vaihtoehdosta epäkäytännöllisen. Tietokoneita, jotka pystyvät suorittamaan nämä laskelmat nopeasti, käytetään siksi, kuluttaen merkittävän määrän sähköä.

Alussa CPU-aikakausi dominoi, jolloin kaivostyöläiset käyttivät henkilökohtaisia tietokoneitaan Bitcoinin kaivamiseen. GPUiden (näytönohjaimet) etujen löytäminen tähän tehtävään merkitsi käännekohtaa, merkittävästi lisäten hashratea ja vähentäen energiankulutusta. Edistys ei pysähtynyt tähän, seurasi FPGAiden (field-programmable gate arrays) käyttöönotto. FPGA:t toimivat alustana ASICien (application-specific integrated circuits) kehittämiselle.

![kuva](assets/overview/chip.png)

ASICit ovat piirejä, verrattavissa CPU-piiriin, kuitenkin, ne on kehitetty suorittamaan vain yhtä tiettyä laskentatyyppiä mahdollisimman tehokkaasti. Toisin sanoen, CPU pystyy suorittamaan monenlaisia erilaisia laskelmia olematta erityisen optimoitu mihinkään tiettyyn laskentatyyppiin, kun taas ASIC pystyy suorittamaan vain yhtä tyyppiä laskentaa, mutta erittäin tehokkaasti. Bitcoin ASICien tapauksessa ne on suunniteltu SHA256-algoritmin laskentaan.
Nykyään louhijat käyttävät yksinomaan ASIC-laitteita, jotka on omistettu tähän toimintaan ja optimoitu testaamaan mahdollisimman suuren määrän yhdistelmiä mahdollisimman pienellä energiankulutuksella ja mahdollisimman nopeasti. Nämä tietokoneet, jotka eivät kykene suorittamaan muita tehtäviä kuin Bitcoin-louhintaa, ovat konkreettinen todiste Bitcoin-louhinta-alan jatkuvasta kehityksestä ja kasvavasta erikoistumisesta. Tämä jatkuva kehitys heijastaa Bitcoinin sisäistä dynamiikkaa, jossa vaikeustason säätö varmistaa lohkon tuotannon joka kymmenes minuutti huolimatta louhintakapasiteetin eksponentiaalisesta kasvusta.
Kuvataksemme tämän prosessin intensiteettiä, harkitse tyypillistä louhijaa, joka kykenee saavuttamaan 14 TeraHashia sekunnissa, eli 14 biljoonaa yritystä joka sekunti löytääkseen oikean hashin. Bitcoin-verkon mittakaavassa saavutamme nyt noin 300 HexaHashia sekunnissa, mikä korostaa Bitcoin-louhinnassa mobilisoidun kollektiivisen voiman määrää.

### Vaikeustason Säätö:

Vaikeustason säätö on keskeinen mekanismi Bitcoin-verkon toiminnassa, varmistaen, että lohkot louhitaan keskimäärin joka 10. minuutti. Tämä kesto on keskiarvo, koska louhintaprosessi on itse asiassa todennäköisyyspeli, samanlainen kuin nopan heittäminen toivossa saada numero, joka on pienempi kuin vaikeustason määrittelemä numero. Joka 2016 lohkon jälkeen verkko säätää louhintavaikeutta perustuen edellisten lohkojen louhintaan keskimäärin vaadittuun aikaan. Jos keskimääräinen aika on yli 10 minuuttia, vaikeustasoa alennetaan, ja päinvastoin, jos keskimääräinen aika on alle, vaikeustasoa nostetaan. Tämä säätömekanismi varmistaa, että uusien lohkojen louhinta-aika pysyy vakiona ajan myötä, riippumatta louhijoiden määrästä tai verkon kokonaislaskentatehosta. Tämän vuoksi Bitcoin Blockchainia kutsutaan myös Timechainiksi.

![kuva](assets/overview/chinaban.png)

* Esimerkki Kiinasta:
Kiinan tapaus kuvaa täydellisesti tätä vaikeustason säätömekanismia. Runsaiden ja halpojen energiavarojen ansiosta Kiina oli maailmanlaajuinen keskus Bitcoin-louhinnalle. Vuonna 2021 maa kielsi yllättäen Bitcoin-louhinnan alueellaan, mikä johti maailmanlaajuisen Bitcoin-verkon hashraten massiiviseen laskuun, noin 50%. Tämä nopea louhintatehon lasku olisi voinut vakavasti häiritä Bitcoin-verkkoa lisäämällä keskimääräistä lohkon louhinta-aikaa. Kuitenkin, vaikeustason säätömekanismi aktivoitui, alentaen louhintavaikeutta varmistaakseen, että lohkon louhintataajuus pysyy keskimäärin 10 minuutissa. Tämä tapaus osoittaa Bitcoinin vaikeustason säätömekanismin tehokkuuden ja joustavuuden, joka varmistaa verkon vakauden ja ennustettavuuden, jopa äkillisten ja merkittävien muutosten edessä globaalissa louhintamaisemassa.

### Bitcoin-louhintakoneiden Kehitys

Bitcoin-louhintakoneiden kehityksestä puhuttaessa on tärkeää huomata, että konteksti on enemmän suunnattu perinteiseen liiketoimintamalliin. Louhijat ansaitsevat tulonsa lohkojen validoinnista, tehtävästä, jonka onnistumisen todennäköisyys on suhteellisen pieni. Nykyisin käytössä oleva malli, Antminer S9, vaikka onkin vanhempi malli, joka lanseerattiin noin vuonna 2016, on edelleen kierrossa käytettyjen markkinoiden kautta, kaupan noin 100–200 eurolla. Kuitenkin louhintakoneiden hinta vaihtelee Bitcoinin arvon mukaan, ja uudempi malli, Antminer S19, arvioidaan tällä hetkellä noin 3000 euroksi.

Jatkuvien teknologisten edistysaskelten edessä louhinta-alalla ammattilaiset joutuvat strategisesti asemoitumaan. Louhintateollisuus on jatkuvien innovaatioiden kohteena, kuten äskettäin julkaistu S19:n J-versio ja odotettu S19 XP:n julkaisu, jotka tarjoavat huomattavasti korkeammat louhintakyvyt, osoittavat. Lisäksi parannukset eivät liity pelkästään koneiden raakatehoon. Esimerkiksi uusi S19 XP -malli käyttää nesteen jäähdytysjärjestelmää, tekninen muutos, joka mahdollistaa merkittävän parannuksen energiatehokkuudessa. Vaikka innovaatio on jatkuvaa, tulevaisuuden tehokkuusvoitot todennäköisesti pienenevät verrattuna tähän mennessä havaittuihin, koska tietty teknologisen innovaation kynnys on saavutettu.
![kuva](assets/overview/chipevolution.png)Yhteenvetona voidaan todeta, että Bitcoin-louhinta-ala jatkaa mukautumista ja kehittymistä, ja alan toimijoiden on ennakoitava tulevaisuudessa väheneviä tehokkuusvoittoja ja mukautettava strategioitaan sen mukaisesti. Vaikka tulevaisuuden teknologiset edistysaskeleet ovat edelleen mahdollisia, ne todennäköisesti tapahtuvat pienemmässä mittakaavassa, mikä heijastaa alan kasvavaa kypsyyttä.
## Louhinta-ala

![Onko Bitcoin-louhinta liian keskitettyä? Riskit ja ratkaisut](https://www.youtube.com/watch?v=xkiY8DgkcLQ)

### Louhintapoolit

Tällä hetkellä Bitcoin-louhinta on kehittynyt vakavaksi ja merkittäväksi alaksi, jossa monet toimijat ovat nyt julkisesti tunnettuja ja merkittävien louhijoiden määrä kasvaa. Tämä kehitys on tehnyt louhinnasta lähes saavuttamattoman pienille toimijoille uusien louhintakoneiden hankinnan korkeiden kustannusten vuoksi. Tämä herättää kysymyksen hashraten jakautumisesta eri markkinatoimijoiden kesken. Tilanne on monimutkainen, koska on tärkeää tarkastella hashraten jakautumista sekä eri yritysten että eri louhintapoolien kesken.

![kuva](assets/overview/pool.png)

Louhintapooli on ryhmä louhijoita, jotka yhdistävät laskentatehonsa lisätäkseen mahdollisuuksiaan louhia. Tämä yhteistyö on tarpeellista, koska yksittäinen pieni louhintakone kilpailee teollisuuden jättiläisiä vastaan, mikä vähentää sen menestymismahdollisuuksia merkityksettömälle tasolle. Louhinta toimii lotto-periaatteella, ja mahdollisuudet voittaa lohko (ja siten Bitcoin-palkkio) joka kymmenes minuutti ovat erittäin pienet yksittäiselle pienelle louhijalle. Yhdistämällä voimansa louhijat voivat yhdistää laskentatehonsa, löytää lohkoja useammin ja sitten jakaa palkkiot suhteessa kunkin louhijan panokseen poolissa.

Esimerkiksi, jos pooli löytää lohkon ja voittaa 6,25 bitcoinia, louhija, joka on antanut 1% poolin kokonaislaskentatehosta, saisi 1% 6,25 bitcoinista. On kuitenkin huomattava, että louhintapoolit yleensä ottavat pienen komission (yleensä noin 2%) kattaakseen yhteistyön käyttökustannukset.

### Alan käyttämä ohjelmisto

Bitcoin-louhinnan yhteydessä ohjelmiston rooli on yhtä tärkeä kuin laitteiston. Tämän osoittaa esimerkiksi Bitmainin rooli, joka on tuottelias valmistaja ja kehitti Antminer S9:n. Louhintalaitteiston lisäksi ala nojaa voimakkaasti yhteistyöhön perustuviin louhintapooleihin, kuten Brainspool, joka hallitsee noin 5% Bitcoin-verkon globaalista hashratesta.
Alan toimijat pyrkivät jatkuvasti lisäämään tehokkuutta laitteiston ja ohjelmiston avulla. Esimerkiksi tässä yhteydessä suosittu ohjelmisto on BrainsOS Plus. Tämä ohjelmisto korvaa louhintakoneen alkuperäisen käyttöjärjestelmän, mahdollistaen samojen toimintojen suorittamisen tehokkaammin. Tällaisen ohjelmiston avulla louhija voi lisätä koneensa tehokkuutta 25%. Tämä tarkoittaa, että samalla sähkön määrällä kone voi tuottaa 25% lisää hashratea, mikä lisää louhijan saamia palkkioita. Tämä ohjelmistooptimointi on olennainen kilpailukyvyn elementti Bitcoin-louhinnassa, mikä osoittaa integroidun lähestymistavan tärkeyden, joka yhdistää sekä laitteiston että ohjelmiston parannukset maksimoidakseen tehokkuuden ja tuotot.

### Säätely ja sähkön hinnat

Kuten Kiinassa ja muualla on havaittu, säätelyllä on merkittävä vaikutus louhintaan. Vaikka Ranskassa ei ole merkittäviä louhijoita, säätely ja korkeat sähkön hinnat Euroopassa ovat suuria esteitä. Louhijat etsivät jatkuvasti edullista sähköä maksimoidakseen voittonsa. Siksi Euroopan ja Ranskan korkeat sähkön hinnat eivät houkuttele louhijoita näille alueille.
Louhijat hakeutuvat usein alueille, joilla on matalat sähköntariffit, usein kehittyvissä maissa tai maissa, joilla on energian ylijäämää. Esimerkiksi suuri osa maailman hashratesta sijaitsee Texasissa, Yhdysvalloissa. Texasilla on itsenäinen sähköverkko, joka ei jaa energiavarojaan muiden osavaltioiden kanssa. Tämä ainutlaatuisuus johtaa usein siihen, että Texas tuottaa enemmän sähköä kuin on tarpeen välttääkseen puutteita, luoden ylijäämän. Bitcoin-louhijat hyödyntävät tätä ylituotantoa perustamalla toimintansa Texasiin, missä he voivat louhia bitcoineja erittäin matalilla sähköntariffeilla energian ylijäämän aikana. Tämä tilanne osoittaa sääntelyjen ja sähköntariffien merkittävän vaikutuksen Bitcoin-louhintaan, korostaen näiden tekijöiden tärkeyttä louhijoiden päätöksenteossa louhintatoimintojensa sijainnin suhteen.

### Minne louhijat menevät ja energianhallinta?

Korostamalla Bitcoin-louhijoiden vaikutusta energian maailmassa, polku on selvä: nämä toimijat etsivät jatkuvasti halvan sähkön lähteitä, usein niitä, jotka ovat hukkaan meneviä tai hyödyntämättömiä. Tämä ilmiö on ilmeinen alueilla, joilla on uusi sähköinfrastruktuuri, kuten ne, jotka on varustettu uusilla vesivoimalaitoksilla.
Otetaan esimerkki. Maassa, joka on rakentamassa patoa, sähköntuotanto usein alkaa ennen kuin jakeluverkot ovat täysin toiminnassa. Tämä aikaväli voi aiheuttaa merkittäviä kustannuksia ja estää investoinnit tällaisiin infrastruktuurihankkeisiin. Bitcoin-louhijat voivat kuitenkin toimia joustavana kysynnän lähteenä, valmiina kuluttamaan tätä "orpoa" sähköä, auttaen näin kattamaan infrastruktuurikustannuksia. Tässä on vihjattu, että uudet asennukset voivat olla välittömästi kannattavia, edistäen uusien sähkön lähteiden luomista. Tämä periaate pätee myös pienemmissä mittakaavoissa. Olipa kyseessä yksilö, joka käyttää vesivoimageneraattoria pienellä joella, tai kotitalous, joka on varustettu aurinkopaneeleilla, tuotettu ylimääräinen sähkö voidaan käyttää Bitcoin-louhintatoimintoihin.

Ranskassa esimerkiksi aurinkopaneeleista ylijäämäinen sähkö injektoidaan takaisin verkkoon ja tuottajat saavat kulutuskrediittiä EDF:ltä. Samoin voi kuvitella louhijan toimivan tällä ylijäämäsähköllä, sammuttaen toimintansa, kun paikallinen kysyntä vastaa tarjontaa. Vaikka tämä saattaa vaikuttaa itsekkäältä, Bitcoin-tuotannon asettaminen paikallisen sähköverkon tukemisen edelle, se tarjoaa toisen näkökulman: sähköverkon vakauttaminen. Ylijäämäsähkön monimutkainen hallinta, joskus jopa siihen liittyvät hävittämiskustannukset, voidaan suuresti yksinkertaistaa. Bitcoin-louhijat voivat absorboida nämä ylijäämät, toimien joustavana puskurina, säätäen kysyntää ennemmin kuin tarjontaa. Maailmassa, jossa uusiutuvan (ei-ohjattavan) sähköntuotannon määrä kasvaa jatkuvasti, louhijat voivat näytellä keskeistä roolia sähköverkkojemme tasapainon varmistamisessa, hyötyen samalla halvasta tai ylijäämäsähköstä louhintatoimintoihinsa.

### Louhinnan keskittäminen

Louhinnan keskittymistä käsitellään merkittävänä haasteena. Suuret toimijat, kuten Foundry, hallitsevat markkinoita, mikä voi mahdollisesti johtaa transaktioiden sensurointiin. Tämä keskittäminen voi myös tehdä verkosta haavoittuvan hyökkäyksille, mukaan lukien 51% hyökkäys, jossa toimija tai ryhmä hallitsee yli 50% verkon hashratesta, mahdollistaen heidän hallita ja manipuloida verkkoa.
Sääntelyn riskiä korostetaan, että jos maa kuten Yhdysvallat päättäisi säädellä tai kieltää tiettyjä Bitcoin-transaktioita, sillä voisi olla merkittävä vaikutus verkkoon, erityisesti jos suuri osa hashratesta on keskittynyt kyseiseen maahan.

![kuva](assets/overview/foundry.png)

Tämän keskittymisen torjumiseksi keskustellaan erilaisista strategioista:
* Kotilouhinta: Kotilouhinnan idea perustuu louhintatoiminnan hajauttamiseen. Se kannustaa yksilöitä osallistumaan louhintaan kodeistaan, jakamalla hashratea laajemmin.
* Stratum V2: Stratum V2 -protokolla tarjoaa toisenlaisen lähestymistavan. Toisin kuin edeltäjänsä, Stratum V2 mahdollistaa louhijoiden valita, mitkä transaktiot sisällytetään heidän louhimiinsa lohkoihin. Tämä kyky vahvistaa sensuurin vastustuskykyä ja vähentää suurten louhintapoolien mahdollisuutta hallita verkkoa. Antamalla enemmän valtaa yksittäisille louhijoille, Stratum V2 -protokolla voi näytellä ratkaisevaa roolia taistelussa hashrate-keskittymistä vastaan.
* Avointen lähdekoodien louhintaohjelmisto: Tämä on toinen mahdollisesti tehokas strategia. Tekemällä louhintaohjelmiston kaikkien saataville, pienillä louhijoilla olisi samat mahdollisuudet kuin suurilla louhintayhtiöillä osallistua ja edistää lohkoketjuverkon toimintaa. Tämä lähestymistapa kannustaisi hashraten laajempaan jakautumiseen, edistäen näin verkon hajauttamista.
* Toimijoiden ja maantieteellisen alueen monipuolistaminen: Kryptovaluutan louhinnan monipuolistaminen eri maantieteellisiltä alueilta tulevien toimijoiden osallistumisen kannustaminen voi myös osoittautua tehokkaaksi. Hajauttamalla hashrate maantieteellisesti, yksittäisen toimijan tai maan on vaikeampi harjoittaa suhteetonta kontrollia tai vaikutusvaltaa verkossa. Tämä lähestymistapa voi auttaa suojelemaan verkkoa mahdollisilta hyökkäyksiltä ja vahvistamaan sen hajauttamista.

Yleinen johtopäätös on, että hajauttaminen on ratkaisevan tärkeää Bitcoin-verkon turvallisuuden ja joustavuuden kannalta. Vaikka keskittäminen voi tarjota tehokkuusetuja, se altistaa verkon merkittäville riskeille, mukaan lukien sensuuri ja 51% hyökkäykset. Aloitteet kuten Takai ja uusien protokollien, kuten Stratum V2, omaksuminen ovat tärkeitä askeleita kohti hajauttamista ja Bitcoin-verkon suojelemista näiltä uhkilta.

## Louhintateollisuuden vivahteet

![Kotisi lämmittäminen bitcoineja louhimalla?](https://www.youtube.com/watch?v=SQaK4_8M0kA)

### Attakai-periaate
Tämän hajauttamisen raja?
Vaikka ajatus louhinnan hajauttamisesta tuottavasti tuotetun lämmön avulla vaikuttaa lupaavalta, siinä on tiettyjä rajoituksia ja kysymyksiä pysyy avoimina. Energiaintensiiviset laitokset, kuten saunat ja uima-altaat, voisivat hyötyä tästä konseptista käyttämällä louhijoiden tuottamaa lämpöä veden lämmittämiseen tiloissaan. Tätä käytäntöä on jo toteuttanut joitakin Bitcoin-yhteisön jäseniä, jotka tutkivat erilaisia menetelmiä louhintalaitteiden tuottaman lämmön tehokkaaseen hyödyntämiseen. Esimerkiksi juhlasali voitaisiin teoriassa lämmittää kolmella tai neljällä S19-louhijalla, jotka kukin kuluttavat 3000 wattia ja tuottavat vastaavan määrän lämpöä.

On kuitenkin huomattava, että energiankulutus ja lämmöntuotanto ovat yhtä suuret, käytettiinpä energiaa sitten sähkölämmittimeen tai louhijaan. Jokaisesta käytetystä kilowatista tuotettu lämpömäärä on molemmissa tapauksissa sama. Ero on siinä, että louhija tarjoaa paitsi lämpöä myös bitcoin-palkkion, tarjoten taloudellisen kannustimen käyttää louhijaa yksinkertaisen sähkölämmittimen sijaan. Tämä lisäpalkkio voisi auttaa lieventämään huolia louhijoiden korkeasta energiankulutuksesta.

Bitcoin-louhijoiden käytön pitkän aikavälin tehokkuuden ja toteutettavuuden kysymys lämmityksessä pysyy avoimena. Jatkuvat innovaatiot louhintalaitteistossa ja lämmitysteknologioissa saattavat mahdollisesti avata uusia väyliä louhinnasta syntyvän lämmön tehokkaammalle hyödyntämiselle, edistäen näin tämän lähestymistavan elinkelpoisuutta tulevaisuudessa.

### Miksi BTC-palkkiot?

Kysymys bitcoinilla palkitsemisesta toisen valuutan sijaan on olennainen Satoshi Nakamoton visioimassa järjestelmässä. Bitcoinin luominen on luonnehdittu 21 miljoonan yksikön kiinteällä katolla. Tavoitteena oli löytää oikeudenmukainen tapa jakaa nämä vasta luodut yksiköt. Louhijat, tarjoamalla laskentatehonsa verkon turvaamiseen ja tehdäkseen hyökkäykset yhä kalliimmiksi, suojelevat tehokkaasti Bitcoin-verkkoa. Tästä ratkaisevasta panoksesta heitä palkitaan vasta luoduilla bitcoineilla, helpottaen kolikoiden jakelua ekosysteemissä.
Se on win-win-järjestelmä. Louhijat palkitaan sekä verkon turvaamisesta että transaktioiden hyväksymisestä. Uudet bitcoinit annetaan kannustimena turvallisuuden vahvistamiseen, ja transaktiomaksut ovat lisätuloa transaktioiden hyväksymisestä. Nämä kaksi elementtiä yhdessä muodostavat kokonaispalkkion louhinnasta. Louhinnan tulevaisuutta koskeva kysymys nousee esiin ohjelmoidun louhintapalkkioiden vähentämisen vuoksi, joka puolittuu joka neljäs vuosi, tapahtumaa kutsutaan "halvingiksi". Vuoteen 2032 mennessä lohkopalkkio on alle yhden bitcoinin, ja vuoteen 2140 mennessä uusia bittejä ei luoda. Tässä vaiheessa louhijat luottavat ainoastaan transaktiomaksuihin korvauksena. Bitcoin-verkon on tuettava suurta määrää transaktioita, riittävän korkeilla maksuilla, varmistaakseen louhinnan kannattavuuden. Lightning Networkin nousu, joka mahdollistaa nopeat ja edulliset transaktiot Bitcoinin pääketjun ulkopuolella, herättää kysymyksiä louhinnan tulevaisuudesta. Lightning Networkilla on potentiaali merkittävästi vähentää transaktiomaksuja, vaikuttaen siten louhijoiden tuloihin. Tämä riippuu kuitenkin Lightning Networkin omaksumisesta ja käytöstä verrattuna pääasialliseen Bitcoin-verkkoon. Pessimistisessä skenaariossa louhijat saattavat pitää louhintaa kannattavana jopa tappiolla, jos he ovat poistaneet kustannuksensa ja heillä on pääsy halpaan sähköön. Optimistisemmassa skenaariossa transaktiomaksut pääasiallisessa Bitcoin-verkossa voivat pysyä tarpeeksi korkeina ylläpitääkseen louhinnan kannattavuutta.

### Mitä Bitcoin-lohkoon tulisi sisältyä?

Bitcoin-lohkon sisältöä koskevassa kysymyksessä on tärkeää harkita Bitcoin-verkon eri kerrosten täydentävää luonnetta. Vaikka Lightning Network voi mahdollistaa nopeammat ja halvemmat transaktiot, se silti nojaa Bitcoinin peruskerrokseen, jota usein kutsutaan "asettelukerrokseksi", maksukanavien avaamiseen ja sulkemiseen.

Lightning Networkin odotetun kasvun ja kanavien avaamisen ja sulkemisen lisääntymisen myötä tila Bitcoin-lohkoissa muuttuu yhä arvokkaammaksi. Bitcoin-yhteisö arvostaa jo tämän tilan säilyttämistä, tunnustaen sen sisäisen rajallisuuden. Tämä tietoisuus on johtanut keskusteluihin lohkon tilan legitiimistä käytöstä, huolien ollessa "spämmistä" lohkoketjussa, jota pidetään ei-olennaisena transaktioina.

![kuva](assets/overview/block.png)
Spekulaatioita lohkon tilan tulevasta käytöstä on, mutta yleisesti hyväksytään, että se on niukka resurssi, jota tulisi käyttää viisaasti. Vaikka on halu täyttää se, on olennaista säilyttää se varmistaakseen Bitcoin-verkon pitkän aikavälin elinkelpoisuuden, odottaen tulevaa kysynnän kasvua lohkotilalle. Kuten missä tahansa vapaassa markkinassa, tarjonta ja kysyntä säätelevät lohkotilan käyttöä. Rajallisella tarjonnalla sidosryhmien on tehtävä tietoisia valintoja tämän arvokkaan tilan käytöstä varmistaakseen Bitcoin-verkon pitkän aikavälin tehokkuuden ja turvallisuuden.

## Louhinta Bitcoin-protokollassa

![Kuka hallitsee? Bitcoin, energia ja valmistajat](https://www.youtube.com/watch?v=4wywK6BfDw8)

Louhijoiden rooli Bitcoin-verkossa on ollut kiivas keskustelun aihe lohkosotien aikana. Vaikka ne ovat olennaisia verkon turvallisuuden ja toiminnallisuuden kannalta, louhijat eivät välttämättä pidä lopullista valtaa Bitcoin-ekosysteemissä. Tasapaino louhijoiden, solmujen ja loppukäyttäjien välillä varmistaa verkon eheyden ja jakelun.

### Lohkosodat

Lohkosotien aikana monet louhijat vastustivat tiettyjä verkon kehityksiä, korostaen jännitettä ekosysteemin eri toimijoiden välillä. Kysymys siitä, miten valtaa tulisi tasapainottaa louhijoiden, solmujen ja käyttäjien välillä Bitcoinin pitkäaikaisen turvallisuuden varmistamiseksi, pysyy.

Turvallisuus ja vallan tasapaino

![kuva](assets/overview/blocksize-wars--BTC-vs-BCH-.webp)
Bitcoinin turvallisuusdilemma perustuu hauraaseen tasapainoon. Vaikka louhijat ovat keskeisessä roolissa lohkojen vahvistamisessa ja luomisessa, solmut ylläpitävät eheyttä vahvistamalla ja validoidessa transaktioita ja lohkoja. Virheellinen tai petollinen lohko hylätään solmujen toimesta, mikä sensuroi louhijaa ja säilyttää verkon turvallisuuden. Valtaa pitävät myös Bitcoin-verkon solmut ja käyttäjät. Solmuilla on vahvistamisen ja validoinnin valta, kun taas käyttäjillä on valta valita, mitä lohkoketjua käyttää. Tämän vallanjaon avulla varmistetaan Bitcoin-verkon hajautus ja eheys.
Lohkosodat paljastivat Bitcoin-verkon hallinnan sisäisen epävarmuuden ja jännitteen. Vaikka Bitcoin Core on tällä hetkellä hallitseva ketju, hallinnointia ja verkon hallintaa koskeva keskustelu jatkuu.
Lopulta vastuu jaetaan kaikkien Bitcoin-verkon toimijoiden kesken. Käyttäjien, solmujen tai louhijoiden määrän väheneminen voisi heikentää verkkoa, lisäten keskittymisen riskiä ja haavoittuvuutta hyökkäyksille. Jokainen toimija edistää verkon vahvuutta ja turvallisuutta, korostaen vallan ja vastuun tasapainon ylläpidon tärkeyttä.
### Louhijoiden valta

Satoshi Nakamoton elegantti peliteoria loi tilanteen, jossa jokainen Bitcoin-verkon toimija on kannustettu toimimaan oikein suojellakseen sekä omia etujaan että muiden osallistujien etuja. Tämä luo tasapainon, jossa huonoa käytöstä voidaan rangaista, vahvistaen koko järjestelmän turvallisuutta ja vakautta. Huolimatta tästä tasapainosta, valtiot pysyvät potentiaalisena uhkana. Kuten Surfing Bitcoin 2022 -esityksessä mainittiin, valtiot saattavat yrittää hyökätä louhintateollisuutta vastaan, altistaen Bitcoin-verkon keskittymisen ja hyökkäyksen riskeille. Hypoteettiset skenaariot, kuten sotilaallinen hyökkäys louhintalaitteiden tuotantolaitoksia vastaan, korostavat maantieteellisen ja teollisen hajauttamisen tärkeyttä Bitcoin-verkon joustavuudelle.

![image](assets/overview/miner.png)

Louhintalaitteiden tuotannon keskittäminen Kiinaan muodostaa toisen riskin. Kieltäytyminen louhintakoneiden viennistä tai hashraten kasaaminen mahdollista 51% hyökkäystä varten Kiinassa korostaa tarvetta louhintalaitteiden tuotannon monipuolistamiseen. Näiden riskien edessä Bitcoin-yhteisö tutkii aktiivisesti ratkaisuja. Yritykset, kuten Intel, harkitsevat louhintalaitteiden tuottamista Yhdysvalloissa, edistäen tuotannon jakautumista. Muut aloitteet, kuten Blockin avoimen lähdekoodin Mining Development Kit (MDK), pyrkivät vähentämään louhintalaitteiden suunnittelun ja tuotannon monopolia, mahdollistaen hashraten laajemman jakautumisen. Näiden keskustelujen ytimessä on Bitcoinin perustehtävä: olla sensuuria vastustava arvonvaihdon verkosto. Bitcoin-yhteisö pyrkii jatkuvasti vahvistamaan jakautumista, sensuurin vastustusta ja verkon anti-haurautta, hyläten ehdotukset, kuten siirtyminen proof of stake -malliin, jotka eivät ole linjassa näiden periaatteiden kanssa.

### Proof of Work vs. Proof of Stake fyysinen linkki
Proof of Work (PoW) on olennainen, koska se edustaa fyysistä linkkiä todellisen maailman ja Bitcoinin välillä. Vaikka bitcoinit ovat aineettomia, niiden tuotanto vaatii konkreettista energiaa, luoden suoran yhteyden fyysiseen ja todelliseen maailmaan. Tämä yhteys varmistaa, että bitcoinien ja lohkojen tuotanto ja validointi ovat todellisia energiakustannuksia, ankkuroi Bitcoin-verkon fyysiseen todellisuuteen ja estää sen täydellisen hallinnan voimakkaiden toimijoiden toimesta. PoW toimii keskittymisen esteenä, varmistaen, että verkkoon osallistuminen ja transaktioiden validointi vaativat investointeja konkreettisiin resursseihin. Tämä estää verkon monopolisoitumisen toimijoiden toimesta, jotka muuten voisivat ottaa hallinnan ilman merkittäviä esteitä, varmistaen näin oikeudenmukaisemman vallan ja vaikutusvallan jakautumisen Bitcoin-verkossa.
![image](assets/overview/POWPOS.png)

### Proof of Staken rajat
Toisaalta, Proof of Stake (PoS) mahdollistaa pienimuotoisen osallistumisen, mutta ei takaa vastaavaa suojaa keskittymistä vastaan. PoS-verkossa ne, jotka jo omistavat suuren määrän valuuttaa, saavat suhteettoman paljon valtaa, mikä heijastaa yleisiä yhteiskunnallisia valtaepätasapainoja. Tämä dynamiikka voi mahdollisesti jatkaa keskittymistä ja vallan keskittymistä harvojen käsiin, mikä on vastoin Bitcoin-verkon perustavoitteita. Väite, että kuka tahansa voi osallistua PoS:ään, jopa pienimuotoisesti, liittymällä pooliin, ei välttämättä ole vahva. PoW-verkossa jopa pieni osallistuja, vaatimattomalla laitteistolla, voi aktiivisesti osallistua ja edistää verkon turvallisuutta ja jakautumista.

### Yhteenveto

Yhteenvetona voidaan todeta, että louhijat vahvistavat Bitcoin-verkkoa sensuuria vastaan käyttämällä sähköä Bitcoinin proof of work -todistuksen laskemiseen, ja heitä palkitaan uusilla bitcoineilla ja siirtomaksuilla. Teollisuuden ammattimaistuessa erilaiset toimijat tulevat esiin, suorittaen erilaisia rooleja piirien luomisesta louhintatilojen hallintaan. Lisäksi rahoitusala puuttuu peliin, kontrolloimalla sitä, kuka selviää eri markkinavaiheissa. Keskittymisen ongelma pysyy, rikkaimpien tahojen mahdollisesti hallitessa markkinoita. Kuitenkin vaihtoehtoja kehitetään sekä laitteisto- että ohjelmistotasolla. Jokaisen yksilön on toimittava ja osallistuttava verkon jakautumiseen. Bitcoin edustaa ennennäkemätöntä mahdollisuutta ei ainoastaan vapauden, vaan myös energiariippumattomuuden suhteen. Huolimatta kiistoista sen sähkönkulutuksen ympärillä, Bitcoin tarjoaa taloudellisen kannustimen siirtymiselle järkevämpään ja runsaampaan energian käyttöön, materialisoiden aiemmin ekologisen ihanteen.

## Bitcoinin hinta ja hashrate, korrelaatioko?
Louhinta voiton vai verkon vuoksi?

Nykyinen hashrate, vaikka Bitcoinin hinta on $30,000 verrattuna aiempaan huippuunsa $69,000, korostaa konkreettista yhteyttä louhinnan ja todellisen maailman välillä. Hinnannousukaudet (härkämarkkinat) johtavat korkeaan kysyntään Bitcoinin louhinnalle ja koneiden tilauksiin valmistajilta, kuten Avalon ja Bitmain. Tuotanto ja toimitus eivät kuitenkaan ole välittömiä, mikä luo epäsuhtaa lisääntyneen kysynnän ja myöhäisemmän saatavuuden välille. Tämä voi johtaa siihen, että härkämarkkinoiden aikana tilatut koneet toimitetaan laskevalla markkinalla, korostaen merkittävää epäsymmetriaa alhaisen hinnan ja korkean hashraten välillä.

Tilanne kuvastaa myös Bitcoinin joustavuutta, jota usein arvioidaan sen hinnan perusteella. Kuitenkin Bitcoinin terveyden syvällisempi analyysi vaatii sen hashraten tarkastelua, joka mittaa sekunnissa tehtyjä laskelmia Bitcoin-verkossa. Vaikka Bitcoinin hinta vaihtelee, sen kustannus, joka liittyy louhintakoneiden käyttämiseen tarvittavaan sähköön, on olennainen markkinadynamiikan ymmärtämiseksi. Keskittymällä kustannuksiin hinnan sijaan saadaan johdonmukaisempi näkökulma Bitcoinin vakaudelle ja pitkän aikavälin elinkelpoisuudelle. Yleisesti ottaen Bitcoinin kustannus on suhteessa sen hintaan, tarjoten paremman ymmärryksen hintavaihteluista ja tulevaisuuden näkymistä.

Hashrate ja palkkio

Louhinta määrittää Bitcoinille lattiapalkkion, jonka alapuolella louhijat myisivät tappiolla. Louhinnan kustannus vaikuttaa merkittävästi hintaan, kuten Kiinassa louhinnan kieltämisen jälkeen nähtiin, kun hashrate ja hinta laskivat merkittävästi, mutta palautuivat nopeasti. Pelkästään hinnan tarkastelu voi olla harhaanjohtavaa. Kustannusten tutkiminen, esimerkiksi kannattavuuslaskureiden kautta, tarjoaa tasapainoisemman näkökulman. Markkinat voivat kuitenkin käyttäytyä irrationaalisesti, pakottaen louhijat myymään tappiolla, mahdollisesti laskien hinnan alle louhintakustannusten. Bitcoinin terveyden ja sen hajauttamisen arvioimiseksi voitaisiin kehittää yhtälö, joka sisältää erilaisia tekijöitä, kuten solmujen määrän ja hinnan. Tämä lähestymistapa voisi tarjota syvällisemmän analyysin Bitcoinista verrattuna keskusteluihin, jotka perustuvat pelkästään hintaan.

Louhinta voiton vai verkon vuoksi?
Kysymys on syvällinen ja kattaa useita Bitcoin-louhinnan ulottuvuuksia. Tasapainon etsiminen voiton tavoittelun ja Bitcoin-verkon turvallisuuden ja jakelun edistämisen välillä on jatkuva dilemma louhijoille. Keskustelu jatkuu Bitcoin-yhteisössä, ja molemmilla puolilla on vahvat argumentit.

* Louhinta voiton vuoksi:
  - Puolesta: Louhijat houkuttelee luonnostaan Bitcoin-louhinnan tarjoama voiton mahdollisuus. Investointi kalliiseen louhintalaitteistoon voi olla kannattavaa louhintapalkkioiden ja transaktiomaksujen kautta, erityisesti kun Bitcoinin hinta on korkea.
  - Vastaan: Voiton tavoittelu voi johtaa laskentatehon keskittymiseen, jos vain muutamat suuret yritykset pystyvät investoimaan huippuluokan louhintalaitteistoon. Lisäksi voiton tavoittelun energiankulutuksella voi olla merkittävä ympäristövaikutus.

* Louhinta verkoston hyväksi:
  - Puolesta: Louhinta Bitcoin-verkon turvallisuuden ja hajautuksen edistämiseksi on jalomielinen aloite. Se auttaa vahvistamaan verkon vastustuskykyä sensuurille ja hyökkäyksille.
  - Vastaan: Ilman riittävää taloudellista kannustinta louhijoiden voi olla vaikea jatkaa verkon tukemista, erityisesti jos he toimivat tappiolla.

Attakai-aloite korostaa verkon tukemisen tärkeyttä tarjoten ratkaisuja, jotka tekevät louhinnasta helpommin saavutettavaa ja vähemmän haitallista. Mahdollisuus louhia kotona, edullisemmalla laitteistolla ja ratkaisuilla melusaasteen vähentämiseksi, voi auttaa demokratisoimaan Bitcoin-louhintaa. Se kannustaa Bitcoinista kiinnostuneita ei vain sijoittamaan ja pitämään bitcoineja, vaan myös aktiivisesti osallistumaan verkon turvaamiseen. Testatun laitteiston ja kokoamis- ja asennusoppaiden tarjoamisen kautta Attakai helpottaa pääsyä Bitcoin-louhinnan maailmaan. Se myös kannustaa innovaatioihin ja jatkuviin parannuksiin, kutsuen yhteisön osallistumaan ja jakamaan ideoitaan ja kokemuksiaan kotilouhinnan parantamiseksi. Attakai-malli on vastaus kysymykseen louhinnasta voiton tai verkon hyväksi. Kyse ei ole vain voittojen tekemisestä, vaan myös Bitcoin-verkon jakelun ja turvallisuuden vahvistamisesta samalla mahdollistaen useammille ihmisille osallistumisen louhintaan, oppimisen ja tämän keskeisen alan ymmärtämisen. Mahdollisen louhintakiellon haaste Euroopassa pysyy avoimena kysymyksenä. Tämä herättää huolia Bitcoin-louhinnan tulevaisuudesta alueella ja tasapainoisen sääntelyn tarpeesta, joka tunnistaa louhinnan tärkeyden Bitcoin-verkon turvallisuudelle ja elinkelpoisuudelle samalla käsitellen ympäristökysymyksiä. Attakai ja muut vastaavat aloitteet voivat näytellä keskeistä roolia tässä keskustelussa, osoittaen, että on mahdollista louhia kestävämmällä ja vastuullisemmalla tavalla samalla positiivisesti edistäen Bitcoin-verkkoa.

## Suvereniteetti ja sääntely
### Suvereniteetti ennen voittoa?
Rikkauden käsittelyn tärkeän kysymyksen osalta on tärkeää harkita erilaisia näkökulmia ja lähestymistapoja. Louhinnan kannattavuutta koskevat kysymykset ovat yleisiä, ja huolia herättää esimerkiksi osakkeiden ostaminen yrityksistä kuten Riot tai louhintakoneiden vuokraaminen alhaisen energian hintamaissa kuten Islanti tai Venäjä. Ennen louhintaan ryhtymistä olennainen harkinta olisi verrata louhinnan kannattavuutta Bitcoinin suoraan ostamiseen. Jos yhden Bitcoinin louhimisen kustannukset ylittävät suoran ostohinnan, on yleensä viisaampaa ostaa Bitcoin suoraan. Tämä välttää monia louhintaprosessiin liittyviä haasteita ja kustannuksia.

Louhinta tarjoaa kuitenkin ainutlaatuisia tapoja osallistua Bitcoin-ekosysteemiin. Esimerkiksi Bitcoinin louhinta talvella voi olla nokkela tapa lämmittää kotiasi samalla kun generoit tuloja Bitcoinissa. Toinen vaihtoehto on investoida yrityksiin, jotka myyvät louhintalaitteistoa ja säilyttävät ja hallinnoivat koneita alhaisen energian hintapaikoissa, tarjoten näin pääsyn edullisiin sähköhintoihin ilman laitteiston hallinnan vaivaa.
Vaikka nämä vaihtoehdot ovat olemassa, louhintaan liittyy merkittäviä haasteita. Kryptovaluuttojen maailmassa tunnettu sanonta "Ei sinun avaimiasi, ei sinun Bitcoinejasi" kaikuu samankaltaisena louhintamaailmassa: "Ei sinun hashrateasi, ei sinun palkkioitasi." Pettymysten ja katkenneiden koneiden tarinat ovat yleisiä, monien toimijoiden luvatessa poikkeuksellisia tuloksia, mutta eivät toimita niitä. Sähkönsyöttöongelmat ja konevikat voivat jättää sijoittajat voimattomiksi, kalliiden laitteiden kanssa, joita he eivät hallitse. Tässä kontekstissa varovaisuus ja syvällinen ymmärrys louhintasektorista ovat ratkaisevan tärkeitä ennen siihen ryhtymistä. Vaikka voitonmahdollisuuksia on olemassa, riskit ovat merkittävät, ja tietoinen ja harkittu lähestymistapa on välttämätön tässä monimutkaisessa ja usein arvaamattomassa kentässä. Siksi perusteellinen tutkimus ja huolellinen etujen ja haittojen harkinta ovat elintärkeitä ennen Bitcoin-louhintaan osallistumista.
![kuva](assets/overview/self.png)

### Neitsyt Bitcoinit
Louhinta Kielletty Euroopassa?

Käännös:
Oman hashraten omistamisen tavoittelu esittäytyy lupaavana polkuna louhintamaailmassa. Tämän monimutkaisen ekosysteemin navigointi vaatii kuitenkin varovaista lähestymistapaa. Pilvilouhintateollisuus on merkitty suurella määrällä huijauksia, joita ruokkii monien sijoittajien louhinnan ymmärtämisen puute. Houkuttelevat tarjoukset, jotka on paketoitu monin eri tavoin, voivat helposti johtaa harhaan niitä, jotka eivät ole hyvin informoituja. Toisaalta oman louhintalaitteiston omistaminen tarjoaa huomattavia etuja. Henkilökohtaisen tyydytyksen lisäksi, joka tulee aktiivisesta osallistumisesta Bitcoin-verkon turvallisuuteen ja palkkioiden näkemisestä omassa lompakossa, on houkutteleva näkökohta "neitsyt bitcoineista". Nämä ovat vasta louhittuja bitcoineja, joita ei ole koskaan käytetty ja joihin ei liity mitään historiaa. Näitä bitcoineja pidetään usein arvokkaampina, koska niitä ei ole "tahrattu", tarjoten jonkin verran takuuta hylkäämisen vastaisesti sääntelijöiden tai suurten vaihtoalustojen toimesta.
Mahdollisuus louhia neitsyt bitcoineja välttäen tunne-asiakkaasi (KYC) menettelyjä on toinen lisäarvo. Monet louhintapoolit eivät vaadi louhijoilta henkilöllisyyden todistamista, mahdollistaen heidän hankkia bitcoineja ilman aikaa vieviä henkilöllisyyden varmistamisen prosesseja. Neitsyt bitcoineja pidetään "puhtaina", ilman mitään menneisyyttä tai yhdistystä. Ne ovat erityisen haluttuja suurten institutionaalisten toimijoiden keskuudessa, jotka voivat taata digitaalisten varojensa laillisuuden sääntelyviranomaisille. Kuitenkin, huolimatta näistä eduista, on ratkaisevan tärkeää tunnistaa, että louhintateollisuus pysyy äärimmäisen kilpailukykyisenä ja volatiilina, ja odottamattomat tapahtumat voivat häiritä louhintatoimintoja.

Tässä kontekstissa itsenäisen ja sivistyneen lähestymistavan valitseminen louhintaan vaikuttaa viisaalta. Oman hashraten hankkiminen ja henkilökohtaiseen louhintalaitteistoon investoiminen, samalla tietoisena riskeistä ja haasteista, voi mahdollisesti tarjota turvallisemman ja tyydyttävämmän polun neitsyt bitcoinien hankkimiseen, vahvistaen samalla yksilön taloudellista suvereniteettia ja tukien koko Bitcoin-ekosysteemiä.

### Louhinta Kielletty Euroopassa?
Kysymyksellä mahdollisesta louhintakiellosta Euroopassa, keskustelut sääntelystä muuttuvat yhä merkityksellisemmiksi. Vaihteleva sääntelymaisema voi todellakin vaikuttaa merkittävästi Bitcoin-louhintateollisuuteen. Louhintakiellon mahdollisuus Euroopassa on kuviteltavissa, erityisesti ottaen huomioon ennakkotapaukset Kiinassa. Vaikka louhintatoiminnot jatkuvat Kiinassa huolimatta kiellosta, Eurooppa voisi seurata samankaltaista polkua. Hashraten laajempi jakautuminen eri alueille voisi auttaa vahvistamaan louhintayhteisöä Euroopassa, mahdollistaen heidän tehokkaasti vastustavan väärinkäsityksiä ja väärinkäsityksiä louhinnasta, sen ympäristövaikutuksista ja sen jalanjäljestä sähköverkossa.
![kuva](assets/overview/regulation.jpg)
Kampanjoiden, kuten Greenpeacen, ja tiettyjen tutkimusten usein harhaanjohtavien lukujen edessä paras ase on tarkka tieto. On olennaista informoida suurta yleisöä ja päätöksentekijöitä kaivostoiminnan todellisuudesta, sen monimutkaisuudesta ja vivahteista, sen sijaan, että annettaisiin heidän nojautua stereotypioihin ja epätarkkaan tietoon. Mitä enemmän tietoisia ja perillä olevia ihmisiä on kaivostoiminnasta, sitä paremmin ala voi puolustautua mahdollisia rajoittavia säädöksiä vastaan.

Yhteenvetona, huolimatta sääntelyriskistä ja mahdollisuudesta kaivostoiminnan kieltämiseen Euroopassa, tehokkain ase on edelleen koulutus ja tiedotus. Selkeä ja tarkka ymmärrys kaivostoiminnasta, sen toiminnasta ja vaikutuksista voi auttaa demystifioimaan alaa ja torjumaan väärää tietoa, tarjoten siten paremman vastustuksen mahdollisesti haitallisille säädöksille. Aloite ihmisten kouluttamiseen ja informoimiseen kaivostoiminnasta, kuten tämä keskustelu tekee, on askel oikeaan suuntaan varmistaakseen kaivostoiminnan kestävyyden ja kasvun Euroopassa ja koko maailmassa. Jatkuvat pyrkimykset kouluttaa ja informoida ovat olennaisia turvallisen ja vauraan tulevaisuuden varmistamiseksi Bitcoinin kaivosteollisuudelle.

## Haastattelu kaivosteollisuuden ammattilaisen kanssa

### Teollisen kaivostoiminnan kulissien takana - Sebastien Gouspillou

![Teollisen kaivostoiminnan kulissien takana - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Kotikaivostoiminta ja lämmön uudelleenkäyttö

## Attakai - mahdollistaa kotikaivostoiminnan ja tekee siitä saavutettavaa!

![Esittelyssä Attakai!](https://www.youtube.com/watch?v=gKoh44UCSnE&t=3s)

Attakai, joka japaniksi tarkoittaa "ihanteellista lämpötilaa", on nimi aloitteelle, jonka tavoitteena on tutustuttaa bitcoinin kaivostoimintaan lämmön uudelleenkäytön kautta, jonka ovat käynnistäneet @ajelexBTC ja @jimzap21 yhdessä Découvre Bitcoinin kanssa.
Tämä ASIC-muunnosopas toimii perustana oppimiselle lisää kaivostoiminnasta, sen toiminnasta ja taustalla olevasta taloudesta osoittamalla mahdollisuuden sopeuttaa Bitcoinin kaivostyöläinen toimimaan lämpöpattereina kodeissa. Tämä tarjoaa lisää mukavuutta ja säästöjä, mahdollistaen osallistujille saada ei-KYC BTC:n käteispalautusta sähkölämmityslaskustaan.

Bitcoin säätää automaattisesti kaivostoiminnan vaikeustasoa ja palkitsee kaivostyöläisiä heidän osallistumisestaan. Kuitenkin hashraten keskittyminen voi aiheuttaa riskejä verkon neutraalisuudelle. Bitcoinin laskentatehon käyttäminen lämmitysratkaisuihin hyödyttää suoraan verkkoa itseään lisäämällä laskentatehon jakautumista.

### Miksi uudelleenkäyttää ASIC:n tuottamaa lämpöä?

On tärkeää ymmärtää energian ja lämmöntuotannon suhde sähköjärjestelmässä.

Yhden kW:n sähköenergian investoinnilla sähköpatteri tuottaa 1 kW:n lämpöä, ei enempää eikä vähempää. Uudet patterit eivät ole tehokkaampia kuin perinteiset patterit. Niiden etu piilee niiden kyvyssä jakaa lämpöä jatkuvasti ja tasaisesti huoneessa, tarjoten enemmän mukavuutta verrattuna perinteisiin pattereihin, jotka vaihtelevat korkean lämmitystehon ja lämmityksen puuttumisen välillä, aiheuttaen säännöllisiä lämpötilan vaihteluita ja epämukavuutta.

Tietokone, tai laajemmin elektroninen piirilevy, ei kuluta energiaa laskelmien suorittamiseen, se tarvitsee vain energiaa komponenttiensa läpi virtaamiseen toimiakseen. Energiankulutus johtuu komponenttien sähköisestä vastuksesta, joka tuottaa häviöitä ja tuottaa lämpöä, tunnetaan Joulen vaikutuksena.
Jotkin yritykset ovat keksineet idean yhdistää laskentatehon tarpeet lämmitystarpeisiin käyttämällä lämpöpattereita/palvelimia. Ajatuksena on jakaa yrityksen palvelimet pieniin yksiköihin, jotka voitaisiin sijoittaa koteihin tai toimistoihin. Tämä idea kohtaa kuitenkin useita ongelmia. Palvelimien tarve ei liity lämmitystarpeeseen, ja yritykset eivät voi käyttää palvelimiensa laskentakykyä joustavasti. Myös yksilöiden käytettävissä olevalla kaistanleveydellä on rajoituksensa. Kaikki nämä rajoitukset estävät yritystä tekemästä näistä kalliista asennuksista kannattavia tai tarjoamasta vakaita online-palvelimia ilman datakeskuksia, jotka voivat ottaa vastuun, kun lämmitystä ei tarvita. "Tietokoneesi tuottama lämpö ei ole hukkaan, jos tarvitset lämmittää kotiasi. Jos käytät sähkölämmitystä asuinpaikassasi, tietokoneesi lämpö ei mene hukkaan. Sähkön tuottama lämpö maksaa saman verran kuin tietokoneellasi. Jos sinulla on sähkölämmitystä halvempi lämmitysjärjestelmä, hukka on vain kustannuserossa. Jos on kesä ja käytät ilmastointia, hukka on kaksinkertainen. Bitcoinien louhinnan tulisi tapahtua siellä, missä se on halvempaa. Ehkä se on paikassa, jossa ilmasto on kylmä ja missä lämmitys on sähköistä, missä louhinta muuttuu ilmaiseksi."
> Satoshi Nakamoto - 8. elokuuta 2010

Bitcoin ja sen proof of work -mekanismi erottuvat, koska ne säätävät automaattisesti louhintavaikeuden perustuen koko verkon suorittamaan laskentamäärään. Tätä määrää kutsutaan hashrateksi ja se ilmaistaan hasheina sekunnissa. Tänään se arvioidaan 380 eksahashiksi sekunnissa, mikä on 380 miljardia miljardia hasheja sekunnissa. Tämä hashrate edustaa työtä ja siten käytettyä energiamäärää. Mitä korkeampi hashrate, sitä korkeampi vaikeusaste, ja päinvastoin. Näin ollen Bitcoin-louhija voidaan aktivoida tai deaktivoida milloin tahansa vaikuttamatta verkkoon, toisin kuin lämpöpatterit/palvelimet, jotka tarvitsevat pysyä vakaina tarjotakseen palvelunsa. Louhija palkitaan osallistumisestaan suhteessa muihin, riippumatta siitä kuinka pieni se voi olla.

Yhteenvetona, sähkölämmitin ja Bitcoin-louhija tuottavat molemmat 1 kW lämpöä 1 kW sähköä kuluttaen. Louhija saa kuitenkin myös bitcoineja palkkiona. Riippumatta sähkön hinnasta, bitcoinin hinnasta tai Bitcoin-louhinnan kilpailusta verkossa, on taloudellisesti edullisempaa lämmittää louhijalla kuin sähkölämmittimellä.

### Lisäarvo Bitcoinille

On tärkeää ymmärtää, miten louhinta edistää Bitcoinin hajauttamista.
Useita olemassa olevia teknologioita on yhdistetty nerokkaasti tuomaan Nakamoton konsensus eloon. Tämä konsensus taloudellisesti palkitsee rehelliset osallistujat heidän panoksestaan Bitcoin-verkon toimintaan, samalla kun se estää epärehellisiä osallistujia. Tämä on yksi avainkohtia, joka mahdollistaa verkon kestävän olemassaolon.
Rehelliset toimijat, ne jotka louhivat sääntöjen mukaan, kilpailevat keskenään saadakseen mahdollisimman suuren osuuden palkkiosta uusien lohkojen tuottamisesta. Tämä taloudellinen kannustin johtaa luonnollisesti tietynlaiseen keskittymiseen, kun yritykset päättävät erikoistua tähän tuottoisaan toimintaan vähentämällä kustannuksiaan mittakaavaetujen kautta. Nämä teolliset toimijat ovat edullisessa asemassa koneiden hankinnassa ja ylläpidossa sekä tukkumyynnin sähköhintojen neuvotteluissa.

> "Aluksi useimmat käyttäjät pyörittäisivät verkkosolmuja, mutta kun verkko kasvaa tietyn pisteen yli, se jäisi yhä enemmän erikoistuneiden palvelinfarmien tehtäväksi, joissa on erikoistunutta laitteistoa. Palvelinfarmin tarvitsisi vain yksi solmu verkossa ja loput LAN yhdistäisivät siihen solmuun."
>
> - Satoshi Nakamoto - 2. marraskuuta 2008
Tietyt tahot hallitsevat merkittävää osuutta kokonaislouhintatehosta suurilla louhintatiloilla. Voimme havaita äskettäisen kylmäaallon Yhdysvalloissa, jossa merkittävä osa louhintatehosta otettiin pois käytöstä ohjatakseen energiaa kotitalouksiin, joilla oli poikkeuksellinen tarve sähkölle. Usean päivän ajan louhijat saivat taloudellisia kannustimia sammuttaakseen tilansa, ja tämä poikkeuksellinen säätila näkyy Bitcoinin louhintatehokäyrässä.
Tämä ongelma voisi muodostua ongelmalliseksi ja aiheuttaa merkittävän riskin verkon puolueettomuudelle. Toimija, jolla on yli 51% louhintatehosta, voisi helpommin sensuroida transaktioita, jos niin haluaisi. Siksi on tärkeää jakaa louhintateho useiden toimijoiden kesken sen sijaan, että se keskitettäisiin yksittäisille tahoille, jotka hallitus voisi esimerkiksi helpommin takavarikoida.

**Jos louhijat jakautuvat tuhansiin, tai jopa miljooniin, kotitalouksiin ympäri maailmaa, valtion on hyvin vaikea ottaa niitä hallintaansa.**

Tehtaasta tullessaan louhija ei sovellu käytettäväksi lämmittimenä kotona kahdesta pääsyystä: liiallinen melu ja säädettävyyden puute. Nämä ongelmat voidaan kuitenkin helposti ratkaista laitteisto- ja ohjelmistomuutoksin, jolloin saadaan paljon hiljaisempi louhija, jota voidaan säätää ja automatisoida kuten nykyaikaisia sähkölämmittimiä.

**Attakaï on koulutusaloite, joka opettaa sinulle, miten voit muuttaa Antminer S9:n kustannustehokkaasti.**

Tämä on erinomainen tilaisuus oppia käytännössä samalla kun saat palkkion osallistumisestasi KYC-vapaina satosheina.

## Osto-opas käytetylle ASIC:lle

![Johdanto Attakaïhin: Lämmitys Bitcoinilla](https://www.youtube.com/watch?v=U_PLo59lp-g)
Tässä osiossa keskustelemme parhaista käytännöistä käytetyn Bitmain Antminer S9:n ostamiseen, joka on laite, johon tämä lämmitysmuunnoksen opas perustuu. Tämä opas pätee myös muihin ASIC-malleihin, sillä se on yleinen osto-opas käytetylle louhintalaitteistolle.

Antminer S9 on laite, jonka Bitmain on tarjonnut toukokuusta 2016 lähtien. Se kuluttaa 1400W sähköä ja tuottaa 13,5 TH/s. Vaikka sitä pidetään vanhana, se on edelleen erinomainen vaihtoehto louhinnan aloittamiseen. Koska sitä on valmistettu suurissa määrin, varaosia on helppo löytää runsaasti monilta alueilta ympäri maailmaa. Yleensä sen voi hankkia vertaisverkossa sivustoilta kuten eBay tai LeBonCoin, sillä ammattimaiset jälleenmyyjät eivät enää tarjoa sitä sen alhaisemman kilpailukyvyn vuoksi verrattuna uudempiin koneisiin. Se on vähemmän tehokas kuin ASICit, kuten Antminer S19, jota on tarjottu maaliskuusta 2020 lähtien, mutta tämä tekee siitä edullisen käytetyn laitteiston ja sopivamman tekemillemme muutoksille.

Antminer S9 tulee useissa variaatioissa (i, j), jotka tekevät pieniä muutoksia ensimmäisen sukupolven laitteistoon. Emme usko, että tämän pitäisi vaikuttaa ostopäätökseesi, ja tämä opas toimii kaikille näille variaatioille.

ASICien hinta vaihtelee monien tekijöiden mukaan, kuten bitcoinin hinnan, verkon vaikeusasteen, koneen tehokkuuden ja sähkön hinnan mukaan. Siksi on vaikea antaa tarkkaa arviota käytetyn koneen ostosta. Helmikuussa 2023 Ranskassa odotettu hinta yleensä vaihtelee 100 €:sta 200 €:oon, mutta nämä hinnat voivat muuttua nopeasti.

![kuva](assets/guide-achat/1.jpeg)

Antminer S9 koostuu seuraavista osista:

- 3 hashboardia, jotka sisältävät sirut, jotka tuottavat louhintatehon.

![kuva](assets/guide-achat/2.jpeg)

- Ohjauskortti, joka sisältää paikan SD-kortille, Ethernet-portin ja liittimet hashboardeille ja tuulettimille. Tämä on ASICisi aivot.
![kuva](assets/guide-achat/3.jpeg)
- 3 datakaapelia, jotka yhdistävät hashboardit ohjauskorttiin.

![kuva](assets/guide-achat/4.jpeg)

- Virtalähde, joka toimii 220V jännitteellä ja voidaan kytkeä kuin tavallinen kotitalouslaite.

![kuva](assets/guide-achat/5.jpeg)

- 2 120mm tuuletinta.

![kuva](assets/guide-achat/6.jpeg)

- Uros C13 -kaapeli.

![kuva](assets/guide-achat/7.jpeg)
Ostaessasi käytettyä konetta on tärkeää tarkistaa, että kaikki osat ovat mukana ja toimivat. Vaihdon aikana sinun tulisi pyytää myyjää käynnistämään kone tarkistaaksesi sen toimivuuden. On tärkeää varmistaa, että laite käynnistyy oikein, ja sen jälkeen tarkistaa internet-yhteys kytkemällä Ethernet-kaapeli ja pääsemällä Bitmainin kirjautumisliittymään verkkoselaimen kautta samassa paikallisverkossa. Tämän IP-osoitteen löydät yhdistämällä internet-reitittimesi liittymään ja etsimällä yhdistettyjä laitteita. Osoitteen tulisi olla seuraavassa muodossa: 192.168.x.x
![kuva](assets/guide-achat/8.gif)

Tarkista myös, että oletusarvoiset tunnistetiedot toimivat (käyttäjätunnus: root, salasana: root). Jos oletusarvoiset tunnistetiedot eivät toimi, sinun on nollattava kone.

![kuva](assets/guide-achat/9.jpeg)

Yhdistämisen jälkeen sinun pitäisi pystyä näkemään kunkin hashboardin tila kojelaudalla. Jos louhija on yhdistetty louhintapooliin, sinun pitäisi nähdä kaikkien hashboardien toimivan. On tärkeää huomata, että louhijat pitävät paljon melua, mikä on normaalia. Varmista myös, että tuulettimet toimivat kunnolla.

Voit sen jälkeen poistaa edellisen omistajan louhintapoolin asettaaksesi oman myöhemmin. Halutessasi voit myös tarkastella hashboardeja purkamalla koneen. Tämä vaihe on kuitenkin monimutkaisempi ja vaatii enemmän aikaa ja joitakin työkaluja. Jos haluat edetä tämän purkamisen kanssa, voit viitata tämän oppaan seuraavaan osaan, jossa kerrotaan, miten se tehdään. On tärkeää huomata, että louhijat keräävät paljon pölyä ja vaativat säännöllistä huoltoa. Voit havaita tämän pölyn kertymisen ja huollon laadun purkamalla koneen.
Kaikkien näiden kohtien tarkastelun jälkeen voit ostaa koneesi suurella luottamuksella. Jos epäröit, konsultoi yhteisöä.

Tiivistääkseni tämän oppaan yhteen lauseeseen: **"Älä luota, varmista."**

[Voit myös kääntyä ammattilaisten puoleen, jotka ovat erikoistuneet louhintakoneiden kunnostukseen, kuten yhteistyökumppanimme 21energy. He tarjoavat testattuja S9-koneita, jotka on puhdistettu ja joihin on jo asennettu BraiiinOS+ -ohjelmisto. Affiliate-koodilla "decouvre" saat 10 % alennuksen S9:n ostosta samalla tukien Attakai-projektia.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Opas S9:n laitteistomuutosten hankintaan

![Johdanto Attakaïhin: lämmitys Bitcoinilla](https://www.youtube.com/watch?v=U_PLo59lp-g)
Antminer S9:n omistajana tiedät todennäköisesti, kuinka äänekäs ja tilaa vievä tämä laitteisto voi olla. On kuitenkin mahdollista muuntaa se hiljaiseksi ja yhdistetyksi lämmittimeksi noudattamalla muutamia yksinkertaisia vaiheita. Tässä osiossa esittelemme tarvittavat laitteet muutosten tekemiseen.

Jos olet taitava nikkaroi ja haluat muuntaa louhijan lämmittimeksi, tämä opas on sinulle. Haluamme varoittaa, että elektronisen laitteen muutokset voivat aiheuttaa sähköriskejä. On siis olennaista ryhtyä kaikkiin tarvittaviin varotoimiin vahinkojen tai vammojen välttämiseksi.
1. Vaihda tuulettimet
Antminer S9:n alkuperäiset tuulettimet ovat liian meluisia käyttääksesi Antmineriasi lämmittimenä. Ratkaisu on vaihtaa ne hiljaisempiin tuulettimiin. Tiimimme on testannut useita malleja Noctua-merkiltä ja on valinnut Noctua NF-A14 iPPC-2000 PWM:n parhaaksi kompromissiksi. Varmista, että valitset tuulettimien 12V version. Tämä 140mm tuuletin voi tuottaa jopa 1200W lämpöä ylläpitäen teoreettisen melutason 31 dB. Asentaaksesi nämä 140mm tuulettimet, tarvitset 140mm - 120mm adapterin, jonka löydät DécouvreBitcoin-kaupasta. Lisäämme myös 140mm suojaverkot.

![kuva](assets/piece/1.jpeg)
![kuva](assets/piece/2.jpeg)
![kuva](assets/piece/3.jpeg)

Virtalähteen tuuletin on myös melko meluisa ja se on vaihdettava. Suosittelemme Noctua NF-A6x25 PWM:ää. Huomaa, että Noctuan tuulettimien liittimet eivät ole samat kuin alkuperäisissä, joten tarvitset liitinadapterin niiden kytkemiseen. Kaksi riittää. Varmista jälleen, että valitset tuulettimen 12V version.

![kuva](assets/piece/4.jpeg)
![kuva](assets/piece/5.jpeg)

2. Lisää WIFI/Ethernet-silta

Ethernet-kaapelin sijaan voit yhdistää Antminerisi WIFIin lisäämällä WIFI/Ethernet-sillan. Olemme valinneet vonets vap11g-300:n, koska se mahdollistaa helposti WIFI-signaalin noutamisen Internet-boksistasi ja sen lähettämisen Antminerillesi Ethernetin kautta luomatta aliverkkoa. Jos sinulla on sähkötekniikan taitoja, voit kytkeä sen suoraan Antminerin virtalähteeseen ilman USB-laturin lisäämistä. Tätä varten tarvitset naaras 5.5mmx2.1mm jakin.

![kuva](assets/piece/6.jpeg)
![kuva](assets/piece/7.jpeg)

3. Vaihtoehtoinen: lisää älypistoke
Jos haluat kytkeä Antminerisi päälle/pois älypuhelimestasi ja seurata sen energiankulutusta, voit lisätä älypistokkeen. Testasimme ANTELA-pistoketta 16A versiona, joka on yhteensopiva smartlife-sovelluksen kanssa. Tämä älypistoke mahdollistaa päivittäisen ja kuukausittaisen energiankulutuksen tarkastelun ja yhdistää suoraan internet-reitittimeesi WiFi:n kautta.
![kuva](assets/piece/8.jpeg)

Laitteiden ja linkkien luettelo

* 2X 3D adapterikappale 140mm - 120mm

* [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

* [2X 140mm tuuletinsuojat](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
* [Sähköasentajan sokeri 2.5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
* [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Valinnainen ANTELA älypistoke](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - Antminer S9 -ohjelmiston muokkaus

## Vonet WIFI/Ethernet-sillan asettaminen

![Yhdistä Antminer S9 Wifi-verkkoon](https://www.youtube.com/watch?v=y4oYURBaPqg)

ASIC:n yhdistämiseksi WIFI-verkkoon tarvitset laitteen, jota kutsutaan sillaksi. Tämä laite mahdollistaa WIFI-signaalin vastaanottamisen reitittimeltäsi ja sen lähettämisen toiselle laitteelle Ethernetin kautta.

Monet laitteet voivat suorittaa tämän toiminnon, mutta suosittelemme VONETS WiFi Bridge/Repeateria sen kätevyyden vuoksi.

Virtalähteenä toimii USB-yhteys.

Tietokoneeltasi, yhdistä VONETS_****** WIFI-verkkoon salasanalla 12345678.

![kuva](assets/software/vonet1.png)

Kirjaudu sisään käyttäjänimellä "admin" ja salasanalla "admin".

![kuva](assets/software/vonet2.png)

Valitse Wizard.

![kuva](assets/software/vonet3.png)

Valitse WIFI-verkko, johon haluat yhdistää louhintalaitteesi, ja klikkaa sitten Next.

HUOM: Vonet-silta toimii vain 2.4GHz taajuudella. Nykyään reitittimet tarjoavat yleensä kaksi WIFI-verkkoa, yhden 2.4GHz ja toisen 5GHz taajuudella.
![kuva](assets/software/vonet4.png)
Syötä WIFI-verkkosi salasana "Lähde-WIFI-hotspotin salasana" -kenttään. Jos et halua käyttää Vonet-siltaasi WIFI-verkon laajentamiseen, valitse "Poista hotspot käytöstä" -ruutu. Muussa tapauksessa jätä se valitsematta.

Voit sen jälkeen klikata Käytä.

Lopuksi, klikkaa uudelleenkäynnistä käynnistääksesi sillan uudelleen. Uudelleenkäynnistyminen kestää muutaman minuutin.

Silta tulisi yhdistää reitittimeesi ja näkyä nimellä "[VONETS.COM](http://vonets.com/)". Jos se ei vieläkään yhdistä muutaman minuutin jälkeen, saatat joutua irrottamaan ja kytkeä sillan uudelleen.

Kun silta on yhdistetty, yhdistä Ethernet-kaapeli sillasta ASIC-laitteeseesi, ja kytke sitten ASIC virtalähteeseen. Voit sen jälkeen päästä ASIC-laitteen käyttöliittymään samalla tavalla kuin jos se olisi suoraan yhdistetty reitittimeesi Ethernetin kautta.

## Antminer S9:n nollaus

Ennen BraiinOS+:n asentamista voi olla tarpeen nollata S9 tehdasasetuksiin.
Tämä menetelmä voidaan soveltaa 2 minuutin ja 10 minuutin välillä louhijan käynnistämisen jälkeen.
2 minuuttia louhijan käynnistämisen jälkeen, paina "Reset" -nappia 5 sekunnin ajan, ja vapauta se sitten. Louhija palautetaan tehdasasetuksiin 4 minuutin kuluessa ja se käynnistyy uudelleen automaattisesti (sitä ei tarvitse sammuttaa).

![kuva](assets/software/1.jpeg)

## BraiinsOS+:n asentaminen Antminer S9:ään

![Braiins OS+:n asentaminen Antminer S9:ään](https://www.youtube.com/watch?v=luqwlvzGsO4)

Antminerin louhintakoneisiin asentama alkuperäinen ohjelmisto on rajallinen toiminnallisuudeltaan. Siksi tässä oppaassa asennamme toisen ohjelmiston nimeltä BraiinsOS+. Se on kolmannen osapuolen kehittämä ohjelmisto, joka on peräisin ensimmäisestä Bitcoin-louhintalta ja tarjoaa enemmän ominaisuuksia, mahdollistaen esimerkiksi koneen tehon muokkaamisen.

ASIC-laitteeseen on useita tapoja asentaa Braiins OS+. Voit viitata tähän oppaaseen sekä [viralliseen Braiins-dokumentaatioon](https://academy.braiins.com/en/braiins-os/about/).

Tässä näemme, miten voimme helposti asentaa Braiins OS+:n suoraan Antminerisi muistiin käyttäen BOS toolbox -ohjelmistoa, korvaten alkuperäisen käyttöjärjestelmän, seuraavien yksityiskohtaisten vaiheiden kautta.

1. Kytke Antminerisi päälle ja yhdistä se internet-laatikkoosi.
2. Lataa BOS toolbox Windowsille / Linuxille.
3. Pura ladattu tiedosto ja avaa bos-toolbox.bat-tiedosto. Valitse kieli, ja muutaman hetken kuluttua näet tämän ikkunan:

![kuva](assets/software/5.jpeg)

4. BOS toolbox mahdollistaa Antminerisi IP-osoitteen helposti löytämisen ja BraiinsOS+:n asentamisen. Jos tiedät jo koneesi IP-osoitteen, voit siirtyä suoraan vaiheeseen 8. Muussa tapauksessa siirry skannaus-välilehteen.

![kuva](assets/software/6.jpeg)

5. Yleensä kotiverkoissa IP-osoitealue on välillä 192.168.1.1 ja 192.168.1.255, joten syötä "192.168.1.0/24" IP-alue -kenttään. Jos verkkosi on erilainen, muuta näitä osoitteita vastaavasti. Klikkaa sitten "Aloita".

6. Huomio, jos Antminerissa on salasana, havaitseminen ei toimi. Jos näin on, yksinkertaisin ratkaisu on suorittaa nollaus.

7. Sinun pitäisi nähdä kaikki verkkosi Antminerit tässä, ja IP-osoite on 192.168.1.37.
![kuva](assets/software/7.jpeg)
8. Klikkaa "Takaisin" ja sitten "Asenna"-välilehteä, syötä aiemmin löytämäsi IP-osoite ja klikkaa "Aloita".

> Jos asennus ei toimi, voi olla tarpeen suorittaa resetointi ja yrittää uudelleen (katso edellinen osio).
![kuva](assets/software/8.jpeg)
9. Hetken kuluttua Antminerisi käynnistyy uudelleen ja pääset käsiksi Braiins OS+ -käyttöliittymään määritetyssä IP-osoitteessa, tässä tapauksessa 192.168.1.37, suoraan selaimen osoiteriviltä. Oletuskäyttäjänimi on "root" eikä oletussalasanaa ole.

## Määritä BraiinsOS+

![Määritä Antminer S9 Braiins OS+:lla](https://www.youtube.com/watch?v=dK0t8M8kLYg)

Sinun täytyy yhdistää ASIC-laitteeseesi käyttäen laitteesi paikallista IP-osoitetta verkossasi selaimen kautta.

Voit löytää koneesi IP-osoitteen käyttämällä BOS toolbox -työkalua tai suoraan reitittimesi verkkosivulta.

Oletuskirjautumistiedot ovat samat kuin alkuperäisessä käyttöjärjestelmässä.

- käyttäjänimi: root
- salasana: (ei mitään)

Tämän jälkeen sinut toivottaa tervetulleeksi Brains OS+ -hallintapaneeli.

### Hallintapaneeli

![kuva](assets/software/14.jpeg)

Tällä ensimmäisellä sivulla voit tarkkailla koneesi reaaliaikaista suorituskykyä.

- Kolme reaaliaikaista graafia, jotka näyttävät lämpötilan, hashraten ja koneesi kokonaistilan.
- Oikealla, todellinen hashrate, piirien keskimääräinen lämpötila, arvioitu tehokkuus W/THs:ssa ja virrankulutus.
- Alla, tuulettimen nopeus prosentteina maksiminopeudesta ja kierrosten määrä minuutissa.

![kuva](assets/software/15.jpeg)

- Alempana löydät yksityiskohtaisen näkymän kustakin hashboardista. Lautan keskimääräinen lämpötila ja sen sisältämien piirien lämpötila sekä jännite ja taajuus.
- Tiedot aktiivisista louhintapoolista Pools-osiossa.
- Autotunauksen tila Tuner Status -osiossa.
- Oikealla, tiedot poolille lähetetystä datasta.

### Määritys

![kuva](assets/software/16.jpeg)

### Järjestelmä

![kuva](assets/software/17.jpeg)

### Pikatoiminnot

![kuva](assets/software/18.jpeg)

# Attakai - Tuulettimen muokkaus

## Vaihda virtalähteen tuuletin

![Vaihda tuulettimet melun vähentämiseksi](https://www.youtube.com/watch?v=2CNGKZiveuc)

> VAROITUS: On olennaista, että olet aiemmin asentanut Braiins OS+:n tai muun ohjelmiston, joka voi vähentää koneesi suorituskykyä. Tämä toimenpide on kriittinen, koska melun vähentämiseksi asennamme vähemmän tehokkaita tuulettimia, jotka voivat hajottaa vähemmän lämpöä.

![kuva](assets/hardware/cover.jpeg)

### Tarvittavat materiaalit

- 1 Noctua NF-A6x25 PWM -tuuletin
- 2,5mm2 sähköasentajan sokeri

> VAROITUS: Ennen kaikkea, ennen kuin aloitat, varmista että olet irrottanut kaivostyöläisesi virtalähteestä välttääksesi sähköiskun vaaran.

![kuva](assets/hardware/1.jpeg)
Ensimmäiseksi, poista 6 ruuvia kotelon sivusta, jotka pitävät sen kiinni. Kun ruuvit on poistettu, avaa varovasti kotelo poistaaksesi muovisen suojan, joka peittää komponentit.
![kuva](assets/hardware/2.jpeg)
![kuva](assets/hardware/3.jpeg)
Seuraavaksi on aika poistaa alkuperäinen tuuletin varoen, ettei vahingoiteta muita komponentteja. Tätä varten poista ruuvit, jotka pitävät sitä paikallaan, ja varovasti kuori pois valkoinen liima liittimen ympäriltä. On tärkeää edetä varoen välttääkseen johdoille tai liittimille aiheutuvia vahinkoja.
![kuva](assets/hardware/4.jpeg)

Kun alkuperäinen tuuletin on poistettu, huomaat, että uuden Noctua-tuulettimen liittimet eivät vastaa alkuperäisen tuulettimen liittimiä. Itse asiassa uudessa tuulettimessa on 3 johtoa, mukaan lukien keltainen johto, joka mahdollistaa nopeudensäädön. Tässä tapauksessa tätä johtoa ei kuitenkaan käytetä. Uuden tuulettimen liittämiseksi suositellaan siis erityisen sovittimen käyttöä. On kuitenkin tärkeää huomata, että tämän sovittimen löytäminen voi joskus olla vaikeaa.

![kuva](assets/hardware/5.jpeg)

Jos sinulla ei ole tätä sovitinta, voit silti jatkaa uuden tuulettimen liittämistä käyttämällä sähköasentajan sokeripalaa. Tätä varten sinun on leikattava vanhan ja uuden tuulettimen kaapelit.

![kuva](assets/hardware/6.jpeg)
![kuva](assets/hardware/7.jpeg)

Uudessa tuulettimessa käytä leikkuria ja leikkaa varovasti pääsuojan ääriviivat 1cm päästä leikkaamatta alla olevien kaapelien suojia.

![kuva](assets/hardware/8.jpeg)

Vedä sitten pääsuoja alaspäin ja leikkaa punaisen ja mustan kaapelin suojat samalla tavalla kuin aiemmin. Ja leikkaa keltainen kaapeli tasaiseksi.

![kuva](assets/hardware/9.jpeg)

Vanhan tuulettimen kohdalla pääsuojan leikkaaminen vahingoittamatta punaisten ja mustien johtojen suojia on herkempi tehtävä. Tätä varten käytimme neulaa, jonka liu'utimme pääsuojan ja punaisten sekä mustien johtojen väliin.

![kuva](assets/hardware/10.jpeg)
![kuva](assets/hardware/11.jpeg)

Kun punaiset ja mustat johdot on paljastettu, leikkaa suojat varovasti välttääksesi sähköjohtojen vahingoittamisen.

![kuva](assets/hardware/12.jpeg)

Yhdistä sitten johdot sokeripalan avulla, musta johto mustaan ja punainen johto punaiseen. Voit myös lisätä sähköteippiä.

![kuva](assets/hardware/13.jpeg)
![kuva](assets/hardware/14.jpeg)
Kun yhteys on muodostettu, on aika asentaa uusi Noctua-tuuletin ritilän kanssa ja käyttää vanhoja ruuveja. Paketissa olevat uudet ruuvit käytetään myöhemmin uudelleen. Varmista, että asennat sen oikeaan suuntaan. Huomaat nuolen yhdellä puolella tuuletinta, joka osoittaa ilmavirran suunnan. On tärkeää asettaa tuuletin niin, että tämä nuoli osoittaa kotelon sisäpuolelle. Kytke sitten tuuletin uudelleen.
![kuva](assets/hardware/15.jpeg)
![kuva](assets/hardware/16.jpeg)

> Vaihtoehtoisesti: Jos olet perehtynyt sähkötekniikkaan, voit suoraan lisätä naaras 5.5mm jakkiliittimen 12V virtalähteeseen, joka syöttää suoraan virtaa Vonet Wi-Fi sillalle. Jos kuitenkin epäilet sähkötekniikan taitojasi, on parasta käyttää USB-liitintä älypuhelintyypin laturin kanssa välttääksesi oikosulun tai sähkövahingon riskin.

![kuva](assets/hardware/17.jpeg)

Kun yhteydet on muodostettu, aseta muovikansi kotelon muovin päälle eikä sisälle.

![kuva](assets/hardware/18.jpeg)

Lopuksi, aseta kotelon kansi takaisin paikalleen ja kiinnitä 6 ruuvia sivuille pitämään kaikki paikoillaan. Ja siinä se on, virtalähteesi kotelo on nyt varustettu uudella tuulettimella.

## Päätuulettimien vaihtaminen
![Vaihda tuulettimet melun vähentämiseksi](https://www.youtube.com/watch?v=2CNGKZiveuc)
> VAROITUS: On välttämätöntä, että olet aiemmin asentanut Braiins OS+:n tai muun ohjelmiston, joka pystyy vähentämään koneesi suorituskykyä. Tämä toimenpide on kriittinen, sillä melun vähentämiseksi asennamme vähemmän tehokkaita tuulettimia, jotka hajottavat vähemmän lämpöä.

![kuva](assets/hardware/cover.jpeg)

### Tarvittavat Materiaalit

- 2 kappaletta 3D-sovitinta 140mm - 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM -tuuletinta
- 2 140mm tuuletinsuojaa

> VAROITUS: Ennen aloittamista, varmista, että olet irrottanut louhijasi virtalähteestä välttääksesi sähköiskun vaaran.

1. Irrota ensin tuulettimet ja ruuvaa ne irti.

![kuva](assets/hardware/19.jpeg)

2. Uusien Noctua-tuulettimien liittimet eivät vastaa alkuperäisiä, mutta älä huoli! Ota veitsesi ja leikkaa varovasti pienet muoviset välilehdet, jotta liittimet sopivat täydellisesti louhijaasi.

![kuva](assets/hardware/20.jpeg)
![kuva](assets/hardware/21.jpeg)
3. Nyt on aika asentaa 3D-osat!
Kiinnitä ne louhijan molemmille puolille käyttäen tuulettimista irrottamiasi ruuveja. Kiristä ruuvit, kunnes ruuvin pää on tasainen 3D-osan kanssa ja se on tukevasti paikallaan. Ole varovainen, ettet kiristä liikaa, sillä saatat vahingoittaa osaa ja yksi ruuveista saattaa koskettaa kondensaattoria!

![kuva](assets/hardware/22.jpeg)

4. Siirrytään nyt tuulettimiin.

Kiinnitä ne 3D-osien avulla mukana tulleilla ruuveilla. Kiinnitä huomiota ilmavirran suuntaan, tuulettimien sivuilla olevat nuolet osoittavat suunnan. Mene Ethernet-portin puolelta toiselle puolelle. Katso alla oleva kuva.

![kuva](assets/hardware/23.jpeg)
![kuva](assets/hardware/24.jpeg)
![kuva](assets/hardware/25.jpeg)

5. Viimeinen vaihe: yhdistä tuulettimet ja kiinnitä suojukset päälle käyttämällä ruuveja, joita ei käytetty virtalähteen tuulettimen laatikossa. Sinulla on niitä vain 4, mutta 2 per suojus vastakkaisissa kulmissa riittää. Tarvittaessa voit etsiä samankaltaisia ruuveja rautakaupasta.

![kuva](assets/hardware/26.jpeg)
![kuva](assets/hardware/27.jpeg)

Odottaessasi tyylikkäämpää koteloasi uudelle lämmittimellesi, voit kiinnittää kotelon ja virtalähteen sähköasentajan nippusiteillä.

![kuva](assets/hardware/28.jpeg)

Ja viimeisenä silauksena, yhdistä Vonet-silta Ethernet-porttiin ja sen virtalähteeseen.

![kuva](assets/hardware/29.jpeg)

Siinä se, onnittelut! Olet juuri vaihtanut louhijasi koko mekaanisen osan. Nyt sinun pitäisi kuulla huomattavasti vähemmän melua.

# Attakai - Kokoonpano

## Liittyminen louhintapooliin

![Liittyminen louhintapooliin Antminer S9:llä](https://www.youtube.com/watch?v=wM-dRog6mls&t=166s)
Voit ajatella louhintapoolia maatalousosuuskuntana. Maanviljelijät kokoavat tuotantonsa yhteen vähentääkseen tarjonnan ja kysynnän vaihtelua ja saadakseen siten vakautta toimintaansa. Louhintapool toimii samalla tavalla, jaettuna resurssina ovat hashit. Todellakin, yhden kelvollisen hashin löytäminen mahdollistaa lohkon luomisen ja coinbase-palkinnon tai -palkkion voittamisen, joka on tällä hetkellä 6,25 BTC plus lohkoon sisältyvät siirtomaksut. Jos louhit yksin, saat palkkion vain, kun löydät lohkon. Kilpaillessasi kaikkia muita maailman louhijoita vastaan, sinulla olisi hyvin vähän mahdollisuuksia voittaa tämä arpajainen, ja sinun täytyisi silti maksaa louhijasi käyttöön liittyvät maksut ilman menestyksen takeita. Louhintapoolit ratkaisevat tämän ongelman yhdistämällä useiden (tuhansien) louhijoiden laskentatehon ja jakamalla palkinnot osallistumisprosentin mukaan poolin hashratesta, kun lohko löydetään. Visualisoidaksesi mahdollisuutesi louhia lohko yksin, voit käyttää tätä työkalua. Syöttämällä tiedot Antminer S9:stä, voimme nähdä, että mahdollisuudet löytää hash, joka mahdollistaa lohkon luomisen, ovat 1 24,777,849:stä jokaista lohkoa kohden tai 1 172,068:sta päivässä. Keskimäärin (vakiona hashratella ja vaikeudella) kestäisi 471 vuotta löytää lohko.
Kuitenkin, koska kaikki Bitcoinissa perustuu todennäköisyyteen, joskus käy niin, että yksin louhivat saavat palkkion tämän riskin ottamisesta: Yksinäinen Bitcoin-louhija ratkaisee lohkon Hash Rate:lla vain 10 TH/s, voittaen erittäin epätodennäköiset mahdollisuudet – Decrypt

Jos pidät uhkapelaamisesta, voit kokeilla, mutta oppaamme ei keskity siihen suuntaan. Sen sijaan keskitymme louhintapooliin, joka parhaiten vastaa tarpeitamme luoda lämmitysjärjestelmä.
Louhintapoolin valinnassa huomioon otettavia seikkoja ovat poolin palkkioiden toiminta, joka voi vaihdella, sekä vähimmäismäärä ennen kuin palkkioita voidaan nostaa osoitteeseen. Esimerkiksi Braiins, joka tarjoaa tässä keskustelemamme ohjelmiston, tarjoaa myös poolin. Tällä poolilla on palkkiojärjestelmä nimeltä "Score", joka kannustaa louhijoita louhimaan pitkiä aikoja. Osallistuminen sisältää käyttöajan tekijän, joka ilmaistaan "scoring hashratena". Meidän tapauksessamme, kun haluamme lämmitysjärjestelmän, joka voidaan kytkeä päälle vain muutamaksi minuutiksi, tämä ei ole ihanteellinen palkkiojärjestelmä. Suosimme palkkiojärjestelmää, joka antaa meille saman palkkion jokaisesta osallistumisesta. Lisäksi Braiins Poolin vähimmäisnostomäärä on 100 000 satsia ja On-Chain. Joten menetämme joitakin satseja siirtomaksuissa ja osa palkkiostamme voi jäädä lukkoon, jos emme louhi tarpeeksi talven aikana.

Meitä kiinnostava palkkiomalli on PPS, joka tarkoittaa "pay-per-share". Tämä tarkoittaa, että louhija saa palkkion jokaisesta kelvollisesta osuudesta. Tästä järjestelmästä on myös variantti, FPPS (Full Pay Per Share), joka jakaa paitsi coinbase-palkkion, myös lohkoon sisältyvät siirtomaksut. Louhintapoolit, joita suosittelemme yhdistämään louhinta-/lämmitysjärjestelmääsi, ovat Linecoin Pool (FPPS) ja Nicehash (PPS).

- Nicehash: Nicehashin etuna on, että nosto voidaan tehdä Lightningin kautta minimaalisin maksuin. Lisäksi vähimmäisnostomäärä on 2000 satsia. Haittapuolena on, että Nicehash käyttää hashrateaan tuottoisimpaan lohkoketjuun antamatta todellista kontrollia käyttäjälle, joten se ei välttämättä edistä Bitcoinin hashratea.
- Linecoin: Linecoinin etuna on tarjottavien ominaisuuksien määrä, kuten yksityiskohtainen hallintapaneeli, mahdollisuus tehdä nostoja Paynymilla (BIP 47) paremman yksityisyydensuojan saavuttamiseksi, sekä Telegram-botin integrointi ja suoraan mobiilisovelluksessa konfiguroitavat automaatiot. Tämä allas louhii ainoastaan Bitcoin-lohkoja, mutta nostojen vähimmäismäärä pysyy korkeana, 100 000 satoshissa. Tutkimme yhden näistä altaista käyttöliittymää tarkemmin tulevassa artikkelissa.
Braiins OS+:ssa altaan konfiguroimiseksi sinun on luotava tili valitsemassasi altaassa. Tässä otamme esimerkiksi Linecoinin:

![kuva](assets/software/19.jpeg)

Kun tilisi on luotu, klikkaa Yhdistä Altaaseen

Kopioi sitten Stratum-osoite ja käyttäjänimesi:

![kuva](assets/software/20.jpeg)

Voit nyt palata Braiins OS+ -käyttöliittymään syöttääksesi nämä tunnistetiedot. Salasana-kentän voit jättää tyhjäksi.

![kuva](assets/software/21.jpeg)
## Antminer S9:n suorituskyvyn optimointi
![Antminer S9:n suorituskyvyn optimointi auto-tuningin avulla](https://www.youtube.com/watch?v=yh8U9Ay1i-E&t=277s)

Sekä ylikellotus että auto-tuning sisältävät säätöjä louhintalautojen taajuuksissa ASIC:n suorituskyvyn parantamiseksi. Erot näiden kahden välillä ovat säätöjen monimutkaisuudessa.

Ylikellotus on yksinkertainen säätö, joka sisältää louhintalautojen taajuuden nostamisen koneen hashraten kasvattamiseksi. Alakellotus puolestaan tarkoittaa integroidun piirin kellotaajuuden pienentämistä alle sen nimellistaajuuden. ASIC:n kellotaajuuden pienentämällä alakellotuksen avulla myös laitteiston tuottama lämpö vähenee. Tämä mahdollistaa ASIC:n jäähdyttämiseen tarvittavien tuulettimien nopeuden vähentämisen, koska niiden ei tarvitse työskennellä yhtä kovasti sopivan lämpötilan ylläpitämiseksi. Tuulettimien nopeuden vähentämällä myös ASIC:n tuottama melu vähenee. Tämä voi olla erityisen hyödyllistä käyttäjille, jotka käyttävät ASIC:eja kotona ja haluavat minimoida louhintalaitteiston aiheuttamat meluhäiriöt.

Braiins OS+ tukee ylikellotusta, alakellotusta ja auto-tuningia ASIC:eille. Se mahdollistaa käyttäjien säätää laitteistonsa kellotaajuutta joustavasti maksimoidakseen suorituskyvyn tai säästääkseen energiaa heidän mieltymystensä mukaan.

### Antminer S9:n suorituskyvyn optimointi auto-tuningin avulla

Ennen vuotta 2018 louhijat saivat etua toiminnassaan kahdella tavalla: löytämällä sähköä kohtuulliseen hintaan ja hankkimalla tehokkaampaa laitteistoa. Kuitenkin vuonna 2018 löydettiin uusi edistysaskel louhintalaitteiston ohjelmisto- ja laiteohjelmistosektorilla, nimeltään AsicBoost. Tämä tekniikka mahdollistaa louhijoiden vähentää kustannuksiaan noin 13% muokkaamalla laitteissaan toimivaa laiteohjelmistoa.
Nykyään on olemassa uusi edistysaskel ohjelmisto- ja laiteohjelmistosektorilla louhinnassa, nimeltään auto-tuning, joka tarjoaa vielä suuremman edun kuin AsicBoost. ASIC:t koostuvat monista pienistä tietokonepiireistä, jotka suorittavat hashauksen. Nämä piirit on valmistettu piistä, samaa alkuainetta, jota käytetään laajalti puolijohteissa ja muissa mikroelektronisissa komponenteissa. Keskeinen ymmärrys tässä on, että kaikki piipiirit eivät ole identtisiä, vaan jokainen voi vaihdella hieman sähköisissä ominaisuuksissaan. Laitteiston valmistajat ovat tietoisia tästä ja julkaisevat louhintakoneidensa suorituskykyspesifikaatiot perustuen niiden toleranssien alarajaan. Toisin sanoen, valmistajat tietävät taajuuden, joka toimii parhaiten keskimääräisille piireille, ja he käyttävät tätä taajuutta yhtenäisesti kaikissa koneen piireissä.
Tämä asettaa ylärajan koneen hash-nopeudelle. Autotuning on prosessi, jossa algoritmit arvioivat optimaaliset taajuudet sirukohtaiseen hashaukseen, sen sijaan, että koko konetta kohdeltaisiin yhtenä yksikkönä. Tämä tarkoittaa, että korkealaatuisempi siru, joka pystyy suorittamaan enemmän hasheja sekunnissa, saa korkeamman taajuuden, ja alempilaatuinen siru, joka pystyy suorittamaan suhteellisesti vähemmän hasheja, saa alempaa taajuutta. Sirutason autotuning on käytännössä tapa optimoida ASIC:n suorituskykyä sen päällä toimivan ohjelmiston ja laiteohjelmiston kautta.

Lopputuloksena on korkeampi hash-nopeus wattia kohden, mikä tarkoittaa suurempia voittomarginaaleja louhijoille. Syy siihen, miksi koneita ei jaeta tämän tyyppisen ohjelmiston kanssa, on se, että koneiden vaihtelu on epätoivottavaa, koska asiakkaat haluavat tietää tarkalleen, mitä he saavat, joten valmistajille on huono idea myydä tuotetta, jolla ei ole johdonmukaista ja ennustettavaa suorituskykyä koneesta toiseen. Lisäksi sirutason autotuning vaatii huomattavia kehitysresursseja, koska sen toteuttaminen on monimutkaista. Valmistajat käyttävät jo paljon resursseja kehittäessään omia laiteohjelmistojaan. On olemassa ohjelmistoratkaisuja, jotka mahdollistavat autotuningin, kuten Braiins OS+. Lisäksi ASIC:n suorituskykyä voidaan parantaa jopa 20 %.

## Antminer S9:n ohjaaminen älypuhelimellasi

### Pikakuvakkeiden luominen iOS:ssä

![Antminer S9:n ohjaaminen älypuhelimellasi](https://www.youtube.com/watch?v=OsKmdB2iw88&t=60s)