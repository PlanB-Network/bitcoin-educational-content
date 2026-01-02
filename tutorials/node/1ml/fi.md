---
name: 1ML
description: Opi käyttämään 1ML Explorer -ohjelmaa Bitcoin:n Lightning-verkon ymmärtämiseen ja analysointiin.
---
![cover](assets/cover.webp)



## Johdanto



Lightning Network on Bitcoin:n päälle rakennettu nopea ja edullinen maksuratkaisu, joka mahdollistaa välittömät ja turvalliset maksutapahtumat. Verkon toiminnan, sen topologian ja sen muodostavien solmujen tilan ymmärtäminen edellyttää tämän verkon tarkkailua. 1ML:n kaltaista Lightning-etsintäohjelmaa käytetään visualisoimaan verkon julkisia tietoja, kuten aktiivisia solmuja, avoimia kanavia ja käytettävissä olevaa kapasiteettia, ja se tarjoaa arvokkaan yleiskuvan käyttäjille, kehittäjille ja solmujen operaattoreille.



## Pääset 1ML:ään ja ymmärrät etusivun



Pääset 1ML:ään yksinkertaisesti avaamalla verkkoselaimen ja kirjoittamalla [https://1ml.com](https://1ml.com). Tämä vie sinut etusivulle, joka toimii Lightning Network:n yleisenä kojelautana.



![capture](assets/fr/03.webp)



Tällä sivulla näytetään useita tärkeitä tilastoja näytön yläreunassa, kuten :





- Verkon **aktiivisten solmujen** eli Salamamaksujen lähettämiseen ja vastaanottamiseen osallistuvien tietokoneiden kokonaismäärä.
- Avoimien kanavien **lukumäärä**, joka vastaa näiden solmujen välisiä yhteyksiä, jotka mahdollistavat varainsiirrot.
- Verkon **kokonaiskapasiteetti** bitcoineina (BTC) ilmaistuna, joka on kaikkien julkisten kanavien kapasiteetin summa.



Luvut päivitetään säännöllisesti vastaamaan verkon nykytilaa. Ne antavat käsityksen verkon koosta, kasvusta ja kestävyydestä.



![capture](assets/fr/04.webp)



Aivan sivun alapuolella on luetteloita ja ranking-listoja:





- **Pienimmin yhdistetyt solmut**, joilla on eniten avoimia kanavia muihin solmuihin.
- Solmujen **korkein kapasiteetti**, joka osoittaa, mitkä solmut voivat siirtää suurimmat määrät.
- Kapasiteetin kannalta tärkeimmät kanavat.



Suodattimien avulla voit myös tarkentaa näitä luetteloita maantieteellisen sijainnin tai muiden kriteerien mukaan.



Tämä sivu on ihanteellinen lähtökohta Lightning Network:n tutkimiseen ja sen yleisen topologian ymmärtämiseen.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Lightning-solmujen tutkiminen



Jos haluat tutkia 1ML:n solmua, aloita sivun yläreunassa olevan hakupalkin avulla. Voit syöttää solmun **Node ID** eli solmun yksilöllisen tunnisteen tai sen **alias**, joka on helpommin muistettava nimi.



Kun haku on valmis, pääset yksityiskohtaiselle sivulle napsauttamalla vastaavaa solmua.



![capture](assets/fr/07.webp)



Tällä sivulla näytetään useita tärkeitä tietoja:





- Solmutunnus**: Tämä yksilöllinen tunniste on pitkä merkkijono, jonka avulla solmu voidaan tunnistaa tarkasti koko verkossa.



![capture](assets/fr/08.webp)





- Alias**: tämä on solmun omistajan valitsema nimi, jolla solmu esitetään julkisesti.



![capture](assets/fr/09.webp)





- **Kanavien määrä** kertoo, kuinka monta yhteyttä solmulla on avoinna muihin solmuihin, kun taas **kokonaiskapasiteetti** edustaa näissä kanavissa käytettävissä olevien bitcoinien summaa. Solmu, jolla on suuri määrä kanavia ja suuri kapasiteetti, on yleensä hyvin verkottunut ja pystyy siirtämään suuria rahamääriä nopeasti verkon kautta.



![capture](assets/fr/10.webp)





- **Yleisaika** eli saatavuus mittaa, kuinka kauan solmu on ollut aktiivinen ja käytettävissä verkossa, mikä kuvastaa sen luotettavuutta. Solmun **ikä** puolestaan kertoo, kuinka kauan se on ollut verkossa, mikä kuvastaa sen vakautta ja kokemusta Lightning Network:ssä.



![capture](assets/fr/11.webp)



Nämä tiedot auttavat sinua ymmärtämään solmun merkitystä ja luotettavuutta Lightning Network:ssa. Esimerkiksi solmu, jolla on suuri määrä kanavia, suuri kapasiteetti ja korkea käytettävyys, on usein merkittävä toimija verkossa.



## Salamakanavien tutkiminen



### Mikä on salamakanava?



Salamakanava on suora yhteys kahden verkon solmun välillä. Sen avulla nämä kaksi solmua voivat vaihtaa välittömiä ja edullisia maksuja ilman, että ne joutuvat käymään Bitcoin-pääketjun läpi jokaista tapahtumaa varten. Kanavat ovat perusta, joka tekee Lightning Network:stä nopean ja skaalautuvan.



### Lue kanavatiedot 1ML:stä



1ML:ssä kullakin kanavalla on oma sivunsa tai kuvauslomakkeensa, joka sisältää useita tärkeitä tietoja:



Solmun sivulta voit tarkastella luetteloa sen kanavista. Kun napsautat kanavaa, 1ML näyttää sille tarkoitetun sivun, jossa on useita tärkeitä tietoja.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Tärkeimmät näkyvät tiedot ovat seuraavat:





- Kumppanuussolmut**: kukin kanava yhdistää kaksi solmua. 1ML näyttää molemmat tunnukset ja niiden aliakset.



![capture](assets/fr/14.webp)





- Kanavan kapasiteetti**: tämä on tähän kanavaan lukittujen bitcoinien kokonaismäärä. Tämä kapasiteetti edustaa maksujen enimmäismäärää, jotka voivat kulkea tämän kanavan kautta.



![capture](assets/fr/15.webp)





- Kanavan ikä**: kertoo, kuinka kauan kanava on ollut auki. Vanha kanava on usein merkki kahden solmun välisestä vakaasta suhteesta.



![capture](assets/fr/16.webp)



### Kanavan näkyvyysrajat



On tärkeää ymmärtää, että 1ML näyttää vain **osan** Lightning Network:stä. Explorer näyttää vain **julkiset kanavat** eli ne, jotka on ilmoitettu verkossa. Yksityiset kanavat, joita käytetään usein luottamuksellisuuteen tai strategiaan liittyvistä syistä, eivät näy. 1ML ei myöskään näytä varojen tarkkaa jakautumista kanavan kummallekin puolelle, eikä suoritettuja maksuja eikä tiettynä hetkenä tosiasiallisesti käytettävissä olevaa likviditeettiä. Näytettävien tietojen avulla voidaan siis analysoida **verkon yleistä rakennetta**, mutta ei sen todellista taloudellista toimintaa tai yksityiskohtaista likviditeettitilannetta.



## Tutustu Lightning Network:een sijainnin mukaan



### Solmut maittain ja alueittain



1ML:n avulla voit tutkia Lightning Network:tä **maantieteellisen jaottelun** mukaan. Etusivulta tai omien osioiden kautta on mahdollista näyttää solmuja maittain tai alueittain. Tämä ominaisuus perustuu solmujen ylläpitäjien ilmoittamiin sijaintitietoihin.


Navigointipalkissa on **Sijainti**-linkki. Sivulla solmut on ryhmitelty maanosan, maan ja kaupungin mukaan.



![capture](assets/fr/17.webp)



Kun valitset maan, 1ML näyttää luettelon siihen liittyvistä solmuista sekä koottuja tilastoja, kuten solmujen määrän ja näkyvän kokonaiskapasiteetin kyseisellä maantieteellisellä alueella.



#### Mitä tämä kertoo paikallisesta adoptiosta





- Teknologian käyttöönotto**: Suuri määrä solmuja alueella osoittaa, että Bitcoin:n käyttäjät, yritykset tai palvelut ottavat Lightning Network:n aktiivisesti käyttöön. Tämä osoittaa teknologista kypsyyttä ja halukkuutta hyödyntää Lightningin etuja (nopeat transaktiot, alhaisemmat kustannukset).
- Taloudellinen ekosysteemi** : Solmupisteiden tiheä läsnäolo voi myös merkitä paikallista taloudellista rakennetta Bitcoin:n ympärillä: kauppiaat hyväksyvät Lightningia, startup-yritykset kehittävät työkaluja, yhteisötapahtumia jne.
- Turvallisuus ja kestävyys**: Monipuolinen maantieteellinen jakelu parantaa verkon häiriönsietokykyä paikallisten katkosten tai rajoitusten varalta. Mitä hajautetummat solmut, sitä hajautetumpi ja vaikeammin sensuroitavissa oleva verkko.
- Politiikat ja määräykset**: Joissakin maissa käyttöönotto saattaa nopeutua suotuisan sääntelykehyksen tai ennakoivan yhteisön ansiosta. Sitä vastoin alueilla, joilla sääntely on tiukkaa tai vihamielistä, solmujen määrä on pienempi.



#### Paikkatietojen rajat



Muista kuitenkin, että Lightning-solmujen maantieteellisellä sijainnilla on rajansa ja ennakkoluulonsa:





- IP-osoitteen likimääräinen sijainti**: 1ML käyttää yleensä solmujen julkista IP-osoitetta niiden sijainnin arvioimiseksi. Tätä menetelmää voi kuitenkin vääristää VPN:ien, pilvipalvelimien (AWS, Google Cloud) käyttö tai hosting eri maissa kuin solmun omistajan todellinen kotipaikka.
- Virtuaaliset solmut**: Jotkut operaattorit isännöivät solmujaan etäpalvelimilla luotettavuuden ja saatavuuden vuoksi, mikä voi antaa väärän käsityksen fyysisestä sijainnista.
- Käyttäjän liikkuvuus**: Solmujen ylläpitäjä voi vaihtaa sijaintia, siirtää infrastruktuuriaan tai avata useita solmuja eri alueilla, mikä tekee tietojen lukemisesta monimutkaisempaa.
- Yksityisten solmujen näkymättömyys**: Jotkin solmut eivät julkaise IP-osoitettaan tai käyttävät menetelmiä sijaintinsa piilottamiseksi, jolloin maantieteellinen paikannus on mahdotonta.



## 1ML:n konkreettiset käyttötapaukset



### Verkon topologian ymmärtäminen



1ML:n avulla voit visualisoida Lightning Network:n **yleisrakenteen**. Tarkastelemalla solmujen välisiä yhteyksiä, kanavien lukumäärää ja kokonaiskapasiteettia on mahdollista ymmärtää, miten verkko on organisoitu, mitkä solmut ovat keskeisessä asemassa ja miten maksuvirrat voivat teoriassa kiertää.



Tämä ymmärrys on olennaisen tärkeää, jos haluamme ymmärtää, miten Lightning Network toimii, eikä vain salkun käyttöä varten.



### Tärkeiden solmukohtien tunnistaminen



1ML:n tarjoamien luokitusten (eniten yhdistetyt solmut, suurin kapasiteetti, ikä) ansiosta on mahdollista tunnistaa solmut, joilla on tärkeä asema verkossa. Nämä solmut toimivat usein tärkeimpinä Lightning-maksujen yhdyskäytävinä.



![capture](assets/fr/18.webp)



### Tarkista solmun julkinen näkyvyys



Solmun operaattorille 1ML:n avulla voit tarkistaa, onko solmusi **julkisesti mainostettu** Lightning Network:ssä. Jos solmu näkyy 1ML:ssä, se tarkoittaa, että se on näkyvissä ja muiden solmujen käytettävissä julkisten kanavien avaamista varten.


Tästä voi olla hyötyä näkyvyys- tai yhteysongelmien diagnosoinnissa.



### Lightning Network:n kehittymisen seuraaminen ajan myötä



Vertailemalla eri ajanjaksojen kokonaistilastoja 1ML:n avulla voidaan tarkkailla Lightning Network:n kehitystä: solmujen lukumäärän lisääntymistä tai vähenemistä, kokonaiskapasiteetin vaihtelua tai maantieteellisen jakautumisen muutoksia.


Nämä havainnot tarjoavat mielenkiintoisen näkökulman Lightning Network:n kasvuun, kypsyyteen ja kehityssuuntauksiin.



## 1ML:n parhaat käytännöt ja rajoitukset



### Julkiset tiedot ≠ täydellinen todellisuus



1ML perustuu yksinomaan Lightning Network:tä koskeviin **julkisesti julkistettuihin** tietoihin. Tämä tarkoittaa, että työkalu näyttää vain osan todellisuudesta. Monet kanavat voivat olla yksityisiä, joitakin solmuja ei ehkä mainosteta, eikä kanavissa saatavilla oleva todellinen likviditeetti ole näkyvissä. Siksi on tärkeää käyttää 1ML:ää yleisenä analyysivälineenä, ei tyhjentävänä kuvauksena verkosta.



### Yksityisyys ja salama



Lightning Network on suunniteltu siten, että siinä on kiinnitetty erityistä huomiota **maksujen yksityisyyteen**. Yksittäiset maksutapahtumat eivät näy 1ML:ssä, eivätkä tarkat kanavasaldot ole julkisia. Tämä rajoitus ei ole explorerin vika, vaan Lightning Network:n perusominaisuus, joka on suunniteltu suojaamaan käyttäjien yksityisyyttä.



### Älä tee hätiköityjä johtopäätöksiä



Solmu, jolla on suuri kapasiteetti tai monta kanavaa, ei välttämättä ole kaikissa tapauksissa "luotettavampi" tai "tehokkaampi". Samoin verkon kokonaiskapasiteetin tilapäinen lasku ei välttämättä tarkoita rakenteellista ongelmaa. Luvut on aina tulkittava jälkikäteen ja asetettava asiayhteyteen.



### Täydentävyys muiden välineiden kanssa



1ML on erinomainen lähtökohta Lightning Network:n tutkimiseen, mutta sitä on parasta käyttää yhdessä muiden työkalujen, kuten Lightning-portfolioiden, solmujen hallintaliittymien ja muiden etsintätyökalujen kanssa. Tämä lähestymistapa tarjoaa täydellisemmän ja vivahteikkaamman näkymän verkosta.



## 1ML-liitäntävaihtoehto (edistyneet toiminnot)



1ML tarjoaa sivustolla näkyvän **kirjautumis-/luo tili** -vaihtoehdon, mutta se ei ole **tarvittava** Lightning Network:n tietojen tarkastelemiseksi. Kaikki tässä oppaassa tähän mennessä käsitellyt ominaisuudet ovat käytettävissä **ilman tiliä**.



Yhteys on suunnattu ensisijaisesti **Valokytkentäsolmujen operaattoreille**. Sen avulla solmuun voidaan liittää 1ML-tili, jonka avulla voidaan hallita tiettyjä julkisia tietoja, kuten solmun esittelyä, yhteystietolinkkejä ja muita metatietoja. Tämän ominaisuuden tarkoituksena on parantaa solmun näkyvyyttä ja tunnistettavuutta etsintäohjelmassa.



On tärkeää huomata, että 1ML ei ole **ei säilytyspalvelu**. Tilin luominen ei anna pääsyä solmun varoihin, kanaviin tai maksuihin. Se palvelee ainoastaan vuorovaikutusta explorerin kanssa deklaratiivisesta ja informatiivisesta näkökulmasta.



Lightning Network:n opettelun tai tutustumisen yhteydessä tätä vaihtoehtoa voidaan siksi pitää **valinnaisena** ja se on varattu edistyneemmille käyttäjille.



## Päätelmä



1ML on arvokas työkalu Lightning Network:n havainnointiin ja ymmärtämiseen sen julkisten tietojen perusteella. Sen avulla voit tutkia verkon rakennetta, analysoida solmuja ja kanavia sekä seurata Lightning Network:n yleiskehitystä ajan myötä. Ilman tilin tarvetta tai varojen käsittelyä 1ML tarjoaa helposti lähestyttävän portin kaikille, jotka haluavat syventää ymmärrystään Lightningin toiminnasta.


Jos haluat edetä pidemmälle Lightning Network:n kanssa, suosittelen täydellistä Johdatus Lightning Network:ään -kurssia:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb