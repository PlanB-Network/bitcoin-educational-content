---
name: Teoreettinen johdatus Lightning-verkkoon
goal: Lightning-verkon teknisen näkökulman löytäminen
objectives:
  - Verkon kanavien toiminnan ymmärtäminen.
  - HTLC:n, LNURL:n ja UTXO:n kaltaisten termien tutuksi tuleminen.
  - LNN:n likviditeetin ja maksujen hallinnan omaksuminen.
  - Lightning-verkon tunnistaminen verkostona.
  - Lightning-verkon teoreettisten käyttötarkoitusten ymmärtäminen.
---

# Matka Bitcoinin toiseen kerrokseen

Tämä kurssi on teoreettinen oppitunti Lightning-verkon teknisestä toiminnasta.

Tervetuloa jännittävään Lightning-verkon maailmaan, joka on Bitcoinin toinen kerros ja joka on sekä monimutkainen että täynnä potentiaalia. Olemme sukeltamassa tämän teknologian teknisiin syvyyksiin keskittymättä tiettyihin opastuksiin tai käyttötapauksiin. Jotta saat tästä kurssista kaiken irti, on olennaista ymmärtää Bitcoinin perusteet. Tämä on kokemus, joka vaatii vakavaa ja keskittynyttä lähestymistapaa. Voit myös harkita LN 202 -kurssin suorittamista rinnakkain, joka tarjoaa käytännöllisemmän näkökulman tähän tutkimukseen. Valmistaudu aloittamaan matka, joka saattaa muuttaa käsitystäsi Bitcoin-ekosysteemistä.

Nauti löydöstä!

+++

# Perusteet
## Lightning-verkon ymmärtäminen

![Lightning-verkon ymmärtäminen](https://youtu.be/PszWk046x-I)

Lightning-verkko on toisen kerroksen maksuinfrastruktuuri, joka on rakennettu Bitcoin-verkon päälle ja mahdollistaa nopeat ja edulliset transaktiot. Jotta voimme ymmärtää, miten Lightning-verkko toimii, on olennaista ymmärtää, mitä maksukanavat ovat ja miten ne toimivat.

Lightning-maksukanava on eräänlainen "yksityinen kaista" kahden käyttäjän välillä, joka mahdollistaa nopeat ja toistuvat Bitcoin-siirrot. Kun kanava avataan, sille annetaan kiinteä kapasiteetti, joka määritellään etukäteen käyttäjien toimesta. Tämä kapasiteetti edustaa maksimaalista Bitcoin-määrää, joka voidaan siirtää kanavassa milloin tahansa.

Maksukanavat ovat kaksisuuntaisia, mikä tarkoittaa, että niillä on kaksi "puolta". Esimerkiksi, jos Alice ja Bob avaavat maksukanavan, Alice voi lähettää Bitcoinia Bobille, ja Bob voi lähettää Bitcoinia Alicelle. Transaktiot kanavan sisällä eivät muuta kanavan kokonaiskapasiteettia, mutta ne muuttavat kapasiteetin jakautumista Alicen ja Bobin välillä.

![selitys](assets/chapitre1/0.JPG)

Jotta transaktio olisi mahdollinen Lightning-maksukanavassa, rahaa lähettävällä käyttäjällä on oltava tarpeeksi Bitcoinia kanavansa puolella. Jos Alice haluaa lähettää 1 Bitcoinin Bobille kanavansa kautta, hänen on oltava vähintään 1 Bitcoin hänen puolellaan kanavassa.
Rajoitukset ja maksukanavien toiminta Lightning-verkossa.
Vaikka Lightning-maksukanavan kapasiteetti on kiinteä, se ei rajoita kokonaisten transaktioiden määrää tai Bitcoinin kokonaismäärää, joka voidaan siirtää kanavan kautta. Esimerkiksi, jos Alicella ja Bobilla on kanava, jonka kapasiteetti on 1 Bitcoin, he voivat suorittaa satoja 0,01 Bitcoinin transaktioita tai tuhansia 0,001 Bitcoinin transaktioita, kunhan kanavan kokonaiskapasiteettia ei ylitetä milloin tahansa.

Huolimatta näistä rajoituksista, Lightning-maksukanavat ovat tehokas tapa suorittaa nopeita ja edullisia Bitcoin-siirtoja. Ne mahdollistavat käyttäjille Bitcoinin lähettämisen ja vastaanottamisen maksamatta korkeita siirtomaksuja tai odottamatta pitkiä vahvistusaikoja Bitcoin-verkossa.

Yhteenvetona, Lightning-maksukanavat tarjoavat tehokkaan ratkaisun niille, jotka haluavat suorittaa nopeita ja edullisia Bitcoin-siirtoja. On kuitenkin olennaista ymmärtää niiden toiminta ja rajoitukset, jotta niistä voi täysin hyötyä.

![selitys](assets/chapitre1/1.JPG)

Esimerkki:

- Alicella on 100 000 SAT
- Bobilla on 30 000 SAT
Tämä on kanavan nykytila. Siirrossa Alice päättää lähettää 40 000 SAT Bobille. Hän voi tehdä niin, koska 40 000 < 100 000.
Kanavan uusi tila on siis:

- Alice 60 000 SAT
- Bob 70 000 SAT

```
Kanavan alkutila:
Alice (100 000 SAT) ============== Bob (30 000 SAT)

Alicen siirrettyä 40 000 SAT Bobille:
Alice (60 000 SAT) ============== Bob (70 000 SAT)

```
![selitys](assets/chapitre1/2.JPG)

Nyt Bob haluaa lähettää 80 000 SAT Alicelle. Koska hänellä ei ole tarpeeksi likviditeettiä, hän ei voi tehdä niin. Kanavan maksimikapasiteetti on 130 000 SAT, mahdollistaen enintään 60 000 SAT menot Alicelle ja 70 000 SAT Bobille.

![selitys](assets/chapitre1/3.JPG)

## Bitcoin, osoitteet, UTXO ja siirrot

![bitcoin, osoitteet, utxo ja siirrot](https://youtu.be/cadCJ2V7zTg)

Tässä toisessa luvussa käymme läpi, miten Bitcoin-siirrot todellisuudessa toimivat, mikä on erittäin hyödyllistä Lightningin ymmärtämiseksi. Käsittelemme myös lyhyesti moniallekirjoitusosoitteiden konseptia, joka on keskeinen seuraavan luvun ymmärtämiseksi Lightning Networkin kanavien avaamisesta.

- Yksityinen avain > Julkinen avain > Osoite: Siirrossa Alice lähettää rahaa Bobille. Jälkimmäinen antaa osoitteen, jonka hänen julkinen avaimensa tuottaa. Alice, joka itse sai rahat osoitteeseen hänen julkisen avaimensa kautta, käyttää nyt yksityistä avaintaan allekirjoittaakseen siirron ja näin vapauttaakseen bitcoinit osoitteesta.
- Bitcoin-siirrossa kaikki bitcoinit on siirrettävä. Nimeltään UTXO (Unspend Transaction Output), bitcoinin palaset lähtevät kaikki vain palatakseen omistajalleen myöhemmin.
  Alicella on 0,002 BTC, Bobilla on 0 BTC. Alice päättää lähettää 0,0015 BTC Bobille. Hän allekirjoittaa 0,002 BTC siirron, josta 0,0015 menee Bobille ja 0,0005 palaa hänen lompakkoonsa.

![selitys](assets/chapitre2/0.JPG)

Tässä, yhdestä UTXO:sta (Alicella on 0,0002 BTC osoitteessa), olemme luoneet 2 UTXO:a (Bobilla on 0,0015 ja Alicella on uusi UTXO (riippumaton edellisestä) 0,0005 BTC).

```
Alice (0,002 BTC)
  |
  V
Bitcoin-siirto (0,002 BTC)
  |
  |----> Bob (0,0015 BTC)
  |
  V
Alice (uusi UTXO: 0,0005 BTC)
```

Lightning Networkissa käytetään moniallekirjoituksia. Siksi varojen vapauttamiseen tarvitaan 2 allekirjoitusta, eli kaksi yksityistä avainta rahan siirtämiseksi. Tämä voi olla Alice ja Bob, jotka yhdessä, täytyy suostua vapauttamaan rahat (UTXO). LN:ssä erityisesti, ne ovat 2/2 siirtoja, joten molemmat allekirjoitukset ovat ehdottoman välttämättömiä, toisin kuin 2/3 tai 3/5 moniallekirjoituksissa, joissa tarvitaan vain avainten täydellisen määrän yhdistelmä.

![selitys](assets/chapitre2/1.JPG)

# Kanavien avaaminen ja sulkeminen
## Kanavan Avaaminen

![avaa kanava](https://youtu.be/B2caBC0Rxko)

Nyt tarkastelemme lähemmin kanavan avaamista ja miten se tehdään Bitcoin-siirron kautta.
Salama-verkolla on eri tasoisia kommunikaatioita:
- P2P-kommunikaatio (Salama-verkon protokolla)
- Maksukanava (Salama-verkon protokolla)
- Bitcoin-siirto (Bitcoin-protokolla)

![selitys](assets/chapitre3/0.JPG)

Kanavan avaamiseksi kaksi vertaista kommunikoi kommunikaatiokanavan kautta:

- Alice: "Hei, haluan avata kanavan!"
- Bob: "Ok, tässä on julkinen osoitteeni."

![selitys](assets/chapitre3/1.JPG)

Alicella on nyt 2 julkista osoitetta luodakseen 2/2 multi-sig -osoitteen. Hän voi nyt tehdä bitcoin-siirron lähettääkseen rahaa siihen.

Oletetaan, että Alicella on UTXO, joka on 0.002 BTC ja hän haluaa avata kanavan Bobin kanssa, joka on 0.0013 BTC. Hän luo siirron, jossa on 2 UTXOa lähtönä:

- UTXO, joka on 0.0013 2/2 multi-sig -osoitteeseen
- UTXO, joka on 0.0007 yhteen hänen vaihto-osoitteistaan (UTXOjen palautus).

Tämä siirto ei ole vielä julkinen, koska tässä vaiheessa hän luottaa Bobiin, että tämä pystyy vapauttamaan rahat multi-sigistä.

Mutta miten sitten edetä?

Alice luo toisen siirron, jota kutsutaan "nostosiirroksi", ennen kuin hän julkaisee varojen talletuksen multi-sigiin.

![selitys](assets/chapitre3/2.JPG)

Nostosiirto käyttää varoja multi-sig -osoitteesta hänen omaan osoitteeseensa (tämä tehdään ennen kaiken julkaisemista).
Kun molemmat siirrot on rakennettu, Alice kertoo Bobille, että se on tehty, ja pyytää häntä allekirjoittamaan julkisella avaimellaan, selittäen, että näin hän voi palauttaa varansa, jos jotain menee pieleen. Bob suostuu, koska hän ei ole epärehellinen.

Alice voi nyt palauttaa varat yksin, koska hänellä on jo Bobin allekirjoitus. Hän julkaisee siirrot. Kanava on nyt avoinna 0.0013 BTC (130 000 SAT) Alicen puolella.

![selitys](assets/chapitre3/3.JPG)

## Salama-siirto & Sitoutumissiirto

![Salama-siirto & Sitoutumissiirto](https://youtu.be/aPqI34tpypM)

![kansi](assets/chapitre4/1.JPG)

Katsotaanpa nyt, mitä todella tapahtuu kulissien takana, kun varoja siirretään kanavan toiselta puolelta toiselle Salama-verkossa, sitoutumissiirron käsitteen kanssa. Ketjussa tapahtuva nosto-/sulkemissiirto edustaa kanavan tilaa, taaten kuka omistaa varat jokaisen siirron jälkeen. Joten Salama-verkon siirron jälkeen, tämän siirron/sopimuksen tila päivitetään toteuttamattomana kahden vertaisen, Alicen ja Bobin, välillä, jotka luovat saman siirron nykyisellä kanavan tilalla sulkemistapauksessa:

- Alice avaa kanavan Bobin kanssa 130 000 SAT omalla puolellaan. Molempien hyväksymä nostosiirto sulkemistapauksessa toteaa, että 130 000 SAT menee Alicelle sulkemisen yhteydessä, ja Bob suostuu, koska se on reilua.

![kansi](assets/chapitre4/2.JPG)

- Alice lähettää 30 000 SAT Bobille. Nyt on uusi nostosiirto, joka toteaa, että sulkemistapauksessa Alice saa 100 000 SAT ja Bob 30 000 SAT. Molemmat suostuvat, koska se on reilua.

![kansi](assets/chapitre4/3.JPG)

- Alice lähettää 10 000 SAT Bobille, ja luodaan uusi nostosiirto, joka toteaa, että Alice saa 90 000 SAT ja Bob 40 000 SAT sulkemistapauksessa. Molemmat suostuvat, koska se on reilua.
![kansi](assets/chapitre4/4.JPG)

```
Kanavan alkutila:
Alice (130,000 SAT) =============== Bob (0 SAT)

Ensimmäisen siirron jälkeen:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Toisen siirron jälkeen:
Alice (90,000 SAT) =============== Bob (40,000 SAT)

```

Rahat eivät liiku, mutta lopullinen saldo päivitetään allekirjoitetulla, mutta julkaisemattomalla on-chain transaktiolla. Nostotransaktio on siis sitoumustapahtuma. Satoshi-siirrot ovat toinen, uudempi sitoumustapahtuma, joka päivittää saldon.

## Sitoumustapahtumat

![transactions part 2](https://youtu.be/RRvoVTLRJ84)

Jos sitoumustapahtumat määrittävät kanavan tilan likviditeetillä ajankohtana X, voimmeko huijata julkaisemalla vanhan tilan? Vastaus on kyllä, koska meillä on jo molempien osapuolten ennakkoon allekirjoitus julkaisemattomassa transaktiossa.

![ohje](assets/Chapitre5/0.JPG)

Ratkaisuksi lisäämme monimutkaisuutta:

- Timelock = varat lukittuina lohkoon N asti
- Revocation key = Alicen salaisuus ja Bobin salaisuus'

Nämä kaksi elementtiä lisätään sitoumustapahtumaan. Tuloksena on, että Alicen on odotettava Timelockin päättymistä, ja kuka tahansa, jolla on revocation key, voi siirtää varoja odottamatta Timelockin päättymistä. Jos Alice yrittää huijata, Bob käyttää revocation keytä varastaakseen ja rangaistakseen Alicea.

![ohje](assets/Chapitre5/1.JPG)

Nyt (ja todellisuudessa) sitoumustapahtuma ei ole sama Alicelle ja Bobille, ne ovat symmetrisiä mutta kummallakin on erilaiset rajoitukset, he antavat toisilleen salaisuutensa luodakseen edellisen sitoumustapahtuman revocation keyn. Joten luodessaan, Alice luo kanavan Bobin kanssa, 130,000 SAT hänen puolellaan, hänellä on Timelock, joka estää häntä välittömästi saamasta rahojaan takaisin, hänen on odotettava hetki. Revocation key voi avata rahat, mutta vain Alicella on se (Alicen sitoumustapahtuma). Kun siirto tapahtuu, Alice antaa vanhan salaisuutensa Bobille ja näin ollen jälkimmäinen voi tyhjentää kanavan edelliseen tilaan, jos Alice yrittää huijata (Alice siis rangaistaan).

![ohje](assets/Chapitre5/2.JPG)

Samoin Bob antaa salaisuutensa Alicelle. Joten jos hän yrittää huijata, Alice voi rangaista häntä. Toiminto toistetaan jokaiselle uudelle sitoumustapahtumalle. Uusi salaisuus päätetään ja uusi revocation key. Joten jokaiselle uudelle transaktiolle, edellinen sitoumustapahtuma on tuhottava antamalla revocation salaisuus. Näin ollen jos Alice tai Bob yrittää huijata, toinen voi toimia ennen (Timelockin ansiosta) ja näin välttää huijauksen. Transaktiossa #3, transaktion #2 salaisuus annetaan siis mahdollistamaan Alicen ja Bobin puolustautumisen Alicen tai Bobin huijausta vastaan.

![ohje](assets/Chapitre5/3.JPG)

Henkilö, joka luo transaktion Timelockilla (se, joka lähettää rahat), voi käyttää revocation keytä vasta Timelockin jälkeen. Kuitenkin henkilö, joka vastaanottaa rahat, voi käyttää sitä ennen Timelockia, jos toisella puolella kanavaa Lightning Networkissa tapahtuu huijaus. Erityisesti selitämme mekanismeja, jotka suojaavat mahdollista huijausta vastaan kanavassa olevan vertaisen toimesta.

## Kanavan Sulkeminen

![sulje kanava](https://youtu.be/FVmQvNpVW8Y)
Olemme kiinnostuneita kanavan sulkemisesta Bitcoin-siirron kautta, joka voi ottaa eri muotoja tapauksesta riippuen. Kanavan sulkemisessa on 3 tyyppiä:
- Hyvä: yhteistyöllinen sulkeminen
- Raaka: pakotettu sulkeminen (ei-yhteistyöllinen)
- Huijari: sulkeminen huijarin toimesta

![ohje](assets/chapitre6/1.JPG)
![ohje](assets/chapitre6/0.JPG)

### Hyvä

Kaksi vertaisosapuolta kommunikoi ja sopii kanavan sulkemisesta. He lopettavat kaikki siirrot ja vahvistavat kanavan lopullisen tilan. He sopivat verkkomaksuista (kanavan avannut henkilö maksaa sulkemismaksut). Nyt he luovat sulkemissiirron. Sulkemissiirto eroaa sitoutumissiirroista, koska siinä ei ole aikalukkoa eikä peruutusavainta. Siirto julkaistaan, ja Alice ja Bob saavat omat saldonsa. Tämä sulkemistyyppi on nopea (koska aikalukkoa ei ole) ja yleensä edullinen.

![ohje](assets/chapitre6/3.JPG)

### Raaka

Alice haluaa sulkea kanavan, mutta Bob ei vastaa, koska hän on offline-tilassa (internet- tai sähkökatkos). Alice julkaisee silloin viimeisimmän sitoutumissiirron (viimeisen). Siirto julkaistaan, ja aikalukko aktivoituu. Silloin, kun tämä siirto luotiin X aika sitten, maksut oli päätetty! MemPool on verkko, joka on muuttunut siitä lähtien, joten protokolla olettaa maksuiksi 5 kertaa korkeammat kuin nykyiset, kun siirto luotiin. Luomismaksu 10 SAT, joten siirtoa pidetään 50 SAT:n arvoisena. Pakotetun sulkemisen aikaan verkko on:

- 1 SAT = yli maksettu 50\*
- 100 SAT = alimaksettu 2\*

Tämä tekee pakotetusta sulkemisesta pidemmän (aikalukko) ja erityisesti riskialttiimman maksujen ja mahdollisen louhijoiden validoinnin kannalta.

![ohje](assets/chapitre6/4.JPG)

### Huijari

Alice yrittää huijata julkaisemalla vanhan sitoutumissiirron. Mutta Bob tarkkailee MemPoolia ja etsii siirtoja, jotka yrittävät julkaista vanhoja. Jos hän löytää sellaisen, hän käyttää peruutusavainta rangaistakseen Alicea ja ottaakseen kaikki SAT:t kanavalta.

![ohje](assets/chapitre6/5.JPG)

Yhteenvetona voidaan sanoa, että kanavan sulkeminen Lightning-verkossa on ratkaiseva vaihe, joka voi ottaa eri muotoja. Yhteistyöllisessä sulkemisessa molemmat osapuolet kommunikoivat ja sopivat kanavan lopullisesta tilasta. Tämä on nopein ja vähiten kallis vaihtoehto. Toisaalta pakotettu sulkeminen tapahtuu, kun toinen osapuoli ei vastaa. Tämä on kalliimpi ja pidempi tilanne ennakoimattomien siirtomaksujen ja aikalukon aktivoitumisen vuoksi. Lopuksi, jos osallistuja yrittää huijata julkaisemalla vanhan sitoutumissiirron, huijari, he voivat menettää kaikki SAT:t kanavalta. On siis ratkaisevan tärkeää ymmärtää nämä mekanismit tehokkaan ja reilun Lightning-verkon käytön kannalta.

# Likviditeettiverkko
## Lightning-verkko

![Lightning-verkko](https://youtu.be/RAZAa3v41DM)

Tässä seitsemännessä luvussa tutkimme, miten Lightning toimii kanavien verkostona ja miten maksut reititetään niiden lähteestä määränpäähän.

![kansi](assets/Chapitre7/0.JPG)
![kansi](assets/Chapitre7/1.JPG)

Lightning on maksukanavien verkosto. Tuhannet vertaisosapuolet omilla likviditeettikanavillaan ovat yhteydessä toisiinsa, ja näin ollen itse käyttävät toimintoja suorittaakseen siirtoja yhteydettömien vertaisten välillä. Näiden kanavien likviditeettiä ei voida siirtää muihin likviditeettikanaviin.
Alice -> Eden -> Bob. Satoshit eivät ole siirtyneet suoraan Alicelta Bobille, vaan reitti on kulkenut Alicelta Edenin kautta Bobille.
Jokaisella henkilöllä ja kanavalla on eri likviditeetti. Maksujen suorittamiseksi sinun on löydettävä verkosta reitti, jolla on tarpeeksi likviditeettiä. Jos likviditeettiä ei ole tarpeeksi, maksu ei mene läpi.

Harkitse seuraavaa verkkoa:

```
Verkon alkutila:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.JPG)

Jos Alicen on siirrettävä 40 SAT Bobille, likviditeetti uudelleenjakautuu kahden osapuolen välisellä reitillä.

```
Alicen siirrettyä 40 SAT Bobille:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)

Alkutilanteessa Bob ei kuitenkaan voi lähettää 40 SAT Alicelle, koska Susiella ei ole likviditeettiä Alicen kanssa lähettääkseen 40 SAT, joten maksu ei ole mahdollinen tätä reittiä pitkin. Tarvitsemme siis toisen reitin, jossa transaktio on mahdoton.

Ensimmäisessä esimerkissä on selvää, että Susie ja Eden eivät ole menettäneet mitään eivätkä saaneet mitään. Lightning Network -solmut veloittavat maksun suostuessaan reitittämään transaktion!

Maksut vaihtelevat sen mukaan, missä likviditeetti sijaitsee

Alice - Bob

- Alicen maksu = Alice -> Bob
- Bobin maksu = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

On kahdenlaisia maksuja:

- kiinteä maksu määrästä riippumatta: 1 SAT (oletusarvo, mutta voidaan muuttaa)
- muuttuva maksu (oletusarvoisesti 0,01%)

Maksuesimerkki:

- Alice - Susie; 1/1 (1 kiinteä maksu ja 1 muuttuva maksu)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Siispä:

- Maksu 1: (Alicen itselleen maksama) 1 + (40,000\*0.000001)
- Maksu 2: 0 + 40,000 \* 0.0002 = 8 SAT
- Maksu 3: 1 + 40,000\* 0.000001 = 0.4 SAT

![cover](assets/Chapitre7/6.JPG)

Lähetykset:

1. Lähetys 40,009.04 Alice -> Susie; Alice maksaa omat kulunsa, joten sitä ei lasketa
2. Susie tekee Edenille palveluksen lähettämällä 40 001.04; hän ottaa tästä komission 8 SAT
3. Eden tekee palveluksen lähettämällä 40,000 Bobille, hän ottaa 1.04 SAT maksun.

Alice maksoi 9.04 SAT maksun ja Bob sai 40,000 SAT.

![cover](assets/Chapitre7/7.JPG)

Lightning Networkissa on Alicen solmu, joka päättää reitin ennen maksun lähettämistä. Siksi etsitään paras reitti ja vain Alice tietää reitin ja hinnan. Maksu lähetetään, mutta Susiella ei ole tietoa.

![cover](assets/Chapitre7/9.JPG)
Susie tai Eden varten: he eivät tiedä, kuka on lopullinen vastaanottaja, eivätkä kuka maksun lähettää. Tämä on sipulireititystä. Solmun on pidettävä suunnitelmaa verkostosta löytääkseen reittinsä, mutta yksikään välittäjistä ei omaa mitään tietoa.
## HTLC - Hashed Time Locked Contract

![HTLC](https://youtu.be/-JC4mkq7H48)

Perinteisessä reititysjärjestelmässä, miten voimme varmistaa, että Eden ei huijaa ja kunnioittaa sopimuksensa osaa?

HTLC on maksusopimus, joka voidaan avata vain salaisuudella. Jos sitä ei paljasteta, sopimus vanhenee. Se on siis ehdollinen maksu. Miten niitä käytetään?

![ohje](assets/chapitre8/0.JPG)

Harkitse seuraavaa tilannetta:
`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob luo salaisuuden S (esikuva) ja laskee hashin r = hash(s)
- Bob lähettää laskun Alicelle, jossa on mukana "r"
- Alice lähettää HTLC:n 40,000 SAT Susielle ehdolla, että paljastetaan "s'", jotta hash(s') = r
- Susie lähettää samanlaisen HTLC:n Bobille
- Bob avaa Susien HTLC:n näyttämällä hänelle "s"
- Susie avaa Alicen HTLC:n näyttämällä hänelle "S"

Jos Bob on offline-tilassa eikä koskaan hanki salaisuutta, joka antaa hänelle oikeuden saada rahat, HTLC vanhenee tietyn määrän lohkojen jälkeen.

![ohje](assets/chapitre8/1.JPG)

HTLC:t vanhenevat käänteisessä järjestyksessä: Susie-Bob vanhentuminen, sitten Alice-Susie vanhentuminen. Näin ollen, jos Bob palaa, se ei muuta mitään. Muussa tapauksessa, jos Alice peruuttaa, kun Bob palaa, seuraa sotku ja ihmiset ovat saattaneet tehdä työtä turhaan.

Joten, mitä tapahtuu sulkemistapauksessa? Itse asiassa sitoutumistransaktiomme ovat vielä monimutkaisempia. Meidän on esitettävä välimuistisaldo, jos kanava suljetaan.

Siksi sitoutumistransaktiossa on HTLC-ulostulo 40,000 satoshista (aiemmin nähtyjen rajoitusten kanssa) ulostulossa #3.

![ohje](assets/chapitre8/2.JPG)

Alicella on sitoutumistransaktiossa:

- Ulostulo #1: 60,000 SAT Alicelle aikarajalla ja peruutusavaimella (mitä hänelle jää)
- Ulostulo #2: 30,000, joka jo kuuluu Susielle
- Ulostulo #3: 40,000 HTLC:ssä

Alicen sitoutumistransaktio on HTLC-ulostulolla, koska hän lähettää HTLC-sisääntulon vastaanottajalle, Susielle.

![ohje](assets/chapitre8/3.JPG)

Siksi, jos julkaisemme tämän sitoutumistransaktion, Susie voi hakea HTCL-rahat "s" kuvalla. Jos hänellä ei ole esikuvaa, Alice hakee rahat, kun HTCL vanhenee. Ajattele ulostuloja (UTXO) eri maksuina eri ehdoilla.
Kun maksu on suoritettu (vanhentuminen tai suoritus), kanavan tila muuttuu ja transaktio HTCL:llä lakkaa olemasta. Palaamme johonkin klassiseen.
Yhteistyöllisen sulkemisen tapauksessa: lopetamme maksut ja odotamme siirtojen/HTCL:n suorittamista, transaktio on kevyt, joten vähemmän kallis, koska siinä on enintään 1 tai 2 ulostuloa.
Jos pakotettu sulkeminen: julkaisemme kaikki meneillään olevat HTLC:t, joten siitä tulee erittäin raskas ja kallis. Ja se on sotku.
Yhteenvetona, Lightning Networkin reititysjärjestelmä käyttää Hash Time-Locked Contracteja (HTLC) varmistaakseen turvalliset ja todennettavat maksut. HTLC:t mahdollistavat ehdolliset maksut, joissa rahat voidaan vapauttaa vain salaisuudella, varmistaen näin, että osapuolet täyttävät sitoumuksensa. Esimerkissä Alice haluaa lähettää SAT:ia Bobille Susien kautta. Bob luo salaisuuden, luo siitä hashin ja lähettää sen Alicelle. Alice ja Susie perustavat tämän hashin perusteella HTLC:n. Kun Bob paljastaa Susielle salaisuuden, Susie voi vapauttaa Alicen HTLC:n.
Jos Bob ei paljasta salaisuutta tietyn ajan kuluessa, HTLC vanhenee. Vanheneminen tapahtuu käänteisessä järjestyksessä, varmistaen, että jos Bob tulee takaisin linjoille, ei ole ei-toivottuja seurauksia.

Kanavan sulkemisessa, jos kyseessä on yhteistyöllinen sulkeminen, maksut keskeytetään ja HTLC:t ratkaistaan, mikä on yleensä vähemmän kallista. Jos sulkeminen on pakotettu, kaikki käynnissä olevat HTLC-transaktiot julkaistaan, mikä voi tulla hyvin kalliiksi ja sotkuiseksi.
Yhteenvetona, HTLC-mekanismi lisää lisäkerroksen turvallisuutta Lightning Networkiin, varmistaen, että maksut suoritetaan oikein ja että käyttäjät täyttävät sitoumuksensa.

## Tien löytäminen

![tien löytäminen](https://youtu.be/wnUGJjOxd9Q)

Ainoa julkinen tieto on kanavan kokonaiskapasiteetti (Alice + Bob), mutta emme tiedä, missä likviditeetti sijaitsee.
Saadaksemme lisätietoja, solmumme kuuntelee LN-viestintäkanavaa uusien kanavien ilmoituksista ja kanavamaksujen päivityksistä. Solmumme tarkastelee myös lohkoketjua kanavien sulkemisista.

Koska meillä ei ole kaikkea tietoa, meidän on etsittävä graafia/reittiä sillä tiedolla, joka meillä on (maksimikanavakapasiteetti, ei missä likviditeetti sijaitsee).

Kriteerit:

- Onnistumisen todennäköisyys - Maksut
- HTLC:n vanhenemisaika
- Välisolmujen määrä
- Satunnaisuus

![graafi](assets/chapitre9/1.JPG)

Joten jos on 3 mahdollista reittiä:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Etsimme teoriassa parasta reittiä, jolla on alhaisimmat maksut ja suurin onnistumisen mahdollisuus: maksimaalinen likviditeetti ja mahdollisimman vähän hyppyjä.

Esimerkiksi, jos 2-3:lla on vain 130 000 SAT:n kapasiteetti, 100 000:n lähettäminen on hyvin epätodennäköistä, joten vaihtoehto #3 ei onnistu.

![graafi](assets/chapitre9/2.JPG)

Nyt algoritmi on tehnyt 3 valintaa ja yrittää ensimmäistä:

Valinta 1:

- Alice lähettää 100 000 SAT:n HTLC:n 1:lle;
- 1 tekee 100 000 SAT:n HTLC:n 2:lle;
- 2 tekee 100 000 SAT:n HTLC:n 5:lle, mutta 5 ei voi tehdä sitä, joten se ilmoittaa siitä.

Tiedot lähetetään takaisin, joten Alice päättää yrittää toista reittiä:

- Alice lähettää 100 000 SAT:n HTLC:n 1:lle;
- 1 tekee 100 000 SAT:n HTLC:n 2:lle;
- 2 tekee 100 000 SAT:n HTLC:n 4:lle;
- 4 tekee 100 000 SAT:n HTLC:n Bobille. Bobilla on likviditeetti, joten se on ok.
- Bob käyttää HTLC:n preimagea (hash) ja käyttää näin salaisuutta hakeakseen 100 000 SAT:n
- 5:llä on nyt HTLC:n salaisuus hakeakseen estetyn HTLC:n 4:ltä
- 4 on nyt saanut HTLC:n salaisuuden, jotta voi hakea estetyn HTLC:n 2:lta
- 2 on nyt saanut HTLC:n salaisuuden, jotta voi hakea estetyn HTLC:n 1:ltä
- 1 on nyt saanut HTLC:n salaisuuden, jotta voi hakea Alicen estetyn HTLC:n

Alice ei nähnyt reitin 1 epäonnistumista, hän vain odotti yhden sekunnin pidempään. Maksun epäonnistuminen tapahtuu, kun mahdollista reittiä ei ole. Reitin etsimisen helpottamiseksi Bob voi antaa Alicelle tietoja, jotka auttavat hänen laskunsa kanssa:

- Summa
- Hänen osoitteensa
- Preimage-hash, jotta Alice voi luoda HTLC:n
- Merkinnät Bobin kanavista

Bob tietää kanavien 5 ja 3 likviditeetin, koska hän on suoraan yhteydessä niihin, hän voi ilmoittaa tämän Alicelle. Hän varoittaa Alicea, että solmu 3 on hyödytön, mikä estää Alicen mahdollisesti tekemästä reittiään.
Toinen elementti voisi olla yksityiset kanavat (joten ei julkaistu verkossa), joita Bobilla voi olla. Jos Bobilla on yksityinen kanava 1:n kanssa, hän voi kertoa Alicelle käyttää sitä ja se antaisi Alicelle > 1 > Bob'.

![graph](assets/chapitre9/3.JPG)

Yhteenvetona voidaan sanoa, että transaktioiden reititys Lightning-verkossa on monimutkainen prosessi, joka vaatii erilaisten tekijöiden huomioon ottamista. Vaikka kanavien kokonaiskapasiteetti on julkinen, tarkan likviditeetin jakautuminen ei ole suoraan saavutettavissa. Tämä pakottaa solmut arvioimaan todennäköisimmin onnistuneet reitit, ottaen huomioon kriteerit kuten maksut, HTLC:n vanhenemisaika, välisolmujen määrä ja satunnaisuustekijä. Kun useita reittejä on mahdollisia, solmut pyrkivät minimoimaan maksut ja maksimoimaan onnistumisen mahdollisuudet valitsemalla kanavia, joilla on riittävä likviditeetti ja mahdollisimman vähän hyppyjä. Jos transaktioyritys epäonnistuu riittämättömän likviditeetin vuoksi, toista reittiä kokeillaan kunnes onnistunut transaktio tehdään.

Lisäksi reitin etsimisen helpottamiseksi vastaanottaja voi antaa lisätietoja, kuten osoitteen, summan, preimage-hashin ja merkinnät kanavistaan. Tämä voi auttaa tunnistamaan kanavia, joilla on riittävä likviditeetti ja välttämään tarpeettomia transaktioyrityksiä. Lopulta Lightning-verkon reititysjärjestelmä on suunniteltu optimoimaan transaktioiden nopeus, turvallisuus ja tehokkuus säilyttäen samalla käyttäjän yksityisyyden.

# Lightning-verkon työkalut
## Lasku, LNURL, Keysend

![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![cover](assets/chapitre10/0.JPG)

LN-lasku (tai lasku) on pitkä ja epämiellyttävä lukea, mutta se mahdollistaa tiiviin esityksen maksupyynnöstä.

Esimerkki:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = luettava osa
- 1 = erottelu lopusta
- Sitten loppu
- Bc1 = Bech32-koodaus (base 32), joten käytetään 32 merkkiä.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = ei "b-i-o" eikä "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (pääverkko)
- 1 = määrä
- M = milli (10^-3 / u = mikro 10^-6 / n = nano 10^-9 / p = pikko 10^-12)
  Tässä 1m = 1 \* 0.0001btc = 100 000 BTC
  "Ole hyvä ja maksa 100 000 SAT Lightning-verkossa Bitcoinin pääverkkoon osoitteeseen pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Aikaleima (luontihetkellä)

Se sisältää 0 tai useampia lisäosia:

- Esikuvan hash
- Maksusalaisuus (sipulireititys)
- Satunnainen data
- Vastaanottajan LN julkinen avain
- Vanhentumisaika (oletus 1 tunti)
- Reititysvihjeet
- Koko laskun allekirjoitus

On muitakin laskutyyppejä. LNURL-metaprotokolla mahdollistaa suoran satoshi-määrän tarjoamisen pyynnön sijaan. Tämä on erittäin joustavaa ja mahdollistaa monia parannuksia käyttäjäkokemuksen kannalta.

![kansi](assets/chapitre10/2.JPG)

Keysend mahdollistaa Alicen lähettää rahaa Bobille ilman, että Bobin tarvitsee pyytää sitä. Alice hakee Bobin ID:n, luo esikuvan kysymättä Bobilta, ja sisällyttää sen maksuunsa. Näin Bob saa yllätyspyynnön, jossa hän voi vapauttaa rahat, koska Alice on jo tehnyt työn.

![kansi](assets/chapitre10/3.JPG)

Yhteenvetona voidaan sanoa, että Lightning Networkin lasku, vaikka se ensi silmäyksellä vaikuttaa monimutkaiselta, koodaa tehokkaasti maksupyynnön. Laskun jokainen osa sisältää keskeistä tietoa, mukaan lukien maksettava summa, vastaanottaja, luontiaikaleima ja mahdollisesti muuta tietoa kuten esikuvan hash, maksusalaisuus, reititysvihjeet ja vanhentumisaika. Protokollat kuten LNURL ja Keysend tarjoavat merkittäviä parannuksia joustavuuden ja käyttäjäkokemuksen suhteen, mahdollistaen esimerkiksi varojen lähettämisen ilman toisen osapuolen etukäteispyyntöä. Nämä teknologiat tekevät maksuprosessista sujuvamman ja tehokkaamman Lightning-verkossa.

## Likviditeetin hallinta

![likviditeetin hallinta](https://youtu.be/YuPrbhEJXbg)

![ohje](assets/chapitre11/0.JPG)

Tarjoamme joitakin yleisiä ohjeita ikuiseen kysymykseen likviditeetin hallinnasta Lightning-verkossa.

LN:ssä on 3 tyyppistä ihmistä:

- Ostajat: heillä on lähtevää likviditeettiä, mikä on yksinkertaisinta, koska heidän tarvitsee vain avata kanavia
- Kauppiaat: se on monimutkaisempaa, koska he tarvitsevat saapuvaa likviditeettiä muilta solmuilta ja toimijoilta. Heidän täytyy saada ihmisiä yhdistämään heihin
- Reitityssolmut: ne haluavat olla tasapainossa likviditeetin kanssa molemmilla puolilla ja olla hyvässä yhteydessä moniin solmuihin, jotta niitä voidaan käyttää mahdollisimman paljon.
Joten jos tarvitset tulevaa likviditeettiä, voit ostaa sitä palveluilta.

![instruction](assets/chapitre11/1.JPG)

Alice ostaa kanavan Susielle 1 miljoonalla satoshilla, joten hän avaa kanavan suoraan 1,000,000 SAT tulevalle puolelle. Hän voi sitten hyväksyä maksuja jopa 1 miljoonaan SAT asti asiakkailta, jotka ovat yhteydessä Susieen (joka on hyvin yhdistetty).

Toinen ratkaisu olisi tehdä maksuja; maksat 100,000 X syystä, nyt voit vastaanottaa 100,000.

![instruction](assets/chapitre11/2.JPG)

### Loop Out -ratkaisu: Atomivaihto LN - BTC

Alice 2 miljoonaa - Susie 0

![instruction](assets/chapitre11/3.JPG)

Alice haluaa lähettää likviditeettiä Susielle, joten hän tekee Loop outin (erikoissolmu, joka tarjoaa pro-palvelun LN/BTC:n tasapainottamiseksi).
Alice lähettää 1 miljoonan Loopille Susien solmun kautta, joten Susiella on likviditeetti ja Loop lähettää ketjussa olevan saldon takaisin Alicen solmuun.

![instruction](assets/chapitre11/4.JPG)

Joten 1 miljoona menee Susielle, Susie lähettää 1 miljoonan Loopille, Loop lähettää 1 miljoonan Alicelle. Alice on siis siirtänyt likviditeettiä Susielle maksamalla joitakin maksuja Loopille palvelusta.

LN:ssä kaikkein monimutkaisinta on pitää likviditeetti.

![instruction](assets/chapitre11/5.JPG)

Yhteenvetona voidaan sanoa, että likviditeetin hallinta Lightning Networkissa on keskeinen kysymys, joka riippuu käyttäjätyypistä: ostaja, kauppias tai reitityssolmu. Ostajilla, jotka tarvitsevat lähtevää likviditeettiä, on yksinkertaisin tehtävä: he vain avaavat kanavia. Kauppiaat, jotka tarvitsevat tulevaa likviditeettiä, on oltava yhdistettyinä muihin solmuihin ja toimijoihin. Reitityssolmut puolestaan pyrkivät ylläpitämään tasapainoa likviditeetissä molemmilla puolilla. Likviditeetin hallintaan on olemassa useita ratkaisuja, kuten kanavien ostaminen tai maksaminen vastaanottokapasiteetin lisäämiseksi. "Loop Out" -vaihtoehto, joka mahdollistaa atomivaihdon LN:n ja BTC:n välillä, tarjoaa mielenkiintoisen ratkaisun likviditeetin tasapainottamiseksi. Näistä strategioista huolimatta likviditeetin ylläpitäminen Lightning Networkissa pysyy monimutkaisena haasteena.

# Mene pidemmälle
## Kurssin yhteenveto

![conclusion](https://youtu.be/MaWpD0rbkVo)

Tavoitteenamme oli selittää, miten Lightning Network toimii ja miten se nojaa Bitcoiniin toimiakseen.

Lightning Network on maksukanavien verkosto. Olemme nähneet, miten maksukanava toimii kahden osapuolen välillä, mutta olemme myös laajentaneet näkemystämme koko verkkoon, maksukanavien verkon käsitteeseen.

![instruction](assets/chapitre12/0.JPG)

Kanavat avataan Bitcoin-siirrolla ja ne voivat sisältää niin monta siirtoa kuin mahdollista. Kanavan tila esitetään sitoutumistransaktiolla, joka lähettää kummallekin osapuolelle sen, mitä heillä on kanavan puolellaan. Kun kanavassa tapahtuu siirto, osapuolet sitoutuvat uuteen tilaan hylkäämällä vanhan tilan ja rakentamalla uuden sitoutumistransaktion.

![instruction](assets/chapitre12/1.JPG)

Parit suojaavat itseään huijauksilta peruutusavaimilla ja aikalukolla. Kanavan sulkemiseen suositaan molemminpuolista suostumusta. Pakotetussa sulkemisessa julkaistaan viimeisin sitoutumistransaktio.

![instruction](assets/chapitre12/3.JPG)
Maksut voivat lainata kanavia muilta välisolmuilta. Ehdolliset maksut hash-aika-lukon (HTLC) avulla mahdollistavat varojen lukitsemisen, kunnes maksu on kokonaan selvitetty. Sipulireititystä käytetään Lightning-verkossa. Välisolmut eivät tiedä maksujen lopullista määränpäätä. Alicen on laskettava maksureitti, mutta hänellä ei ole kaikkea tietoa välisolmujen likviditeetistä.
![ohje](assets/chapitre12/4.JPG)

Maksun lähettämisessä Lightning-verkon kautta on todennäköisyyskomponentti.

![ohje](assets/chapitre12/5.JPG)

Maksujen vastaanottamiseksi kanavien likviditeettiä on hallinnoitava, mikä voidaan tehdä pyytämällä muita avaamaan kanavia meille, avaamalla kanavia itse ja käyttämällä työkaluja kuten Loop tai ostamalla/vuokraamalla kanavia markkinapaikoilta.

## Faniksen haastattelu

![Faniksen haastattelu](https://youtu.be/VeJ4oJIXo9k)

Tässä on yhteenveto haastattelusta:

Lightning-verkko on erittäin nopea maksuratkaisu Bitcoinille, joka mahdollistaa verkon skaalautuvuuteen liittyvien rajoitusten kiertämisen. Kuitenkin bitcoinit Lightning-verkossa eivät ole yhtä turvallisia kuin Bitcoin-ketjussa, koska skaalautuvuus asetetaan etusijalle hajauttamisen ja turvallisuuden kustannuksella.

Liiallinen lohkokoon kasvattaminen ei ole hyvä ratkaisu, koska se vaarantaa solmut ja datan kapasiteetin. Sen sijaan Lightning-verkko mahdollistaa maksukanavien luomisen kahden Bitcoin-käyttäjän välille näyttämättä transaktioita lohkoketjussa, säästäen tilaa lohkoissa ja mahdollistaen Bitcoinin skaalautumisen tänään.

Kuitenkin on kritiikkiä Lightning-verkon skaalautuvuuden ja keskittymisen suhteen, potentiaalisine ongelmineen liittyen kanavien sulkemiseen ja korkeisiin transaktiomaksuihin. Näiden ongelmien ratkaisemiseksi suositellaan välttämään pienten kanavien avaamista tulevaisuuden ongelmien välttämiseksi ja transaktiomaksujen kasvattamista Child Pay for Parent -toiminnolla.

Tulevaisuuden ratkaisuina Lightning-verkolle pidetään transaktioiden niputtamista ja kanavien luomista ryhmissä transaktiomaksujen vähentämiseksi, sekä lohkokoon kasvattamista pitkällä aikavälillä. On kuitenkin tärkeää huomata, että Lightning-verkon bitcoinit eivät ole yhtä turvallisia kuin Bitcoin-ketjun bitcoinit.

Yksityisyys Bitcoinissa ja Lightningissa ovat yhteydessä toisiinsa, sipulireitityksen tarjotessa tietyn tason yksityisyyttä transaktioille. Kuitenkin Bitcoinissa kaikki on oletusarvoisesti läpinäkyvää, heuristiikkojen avulla seuraten bitcoineja osoitteesta toiseen Bitcoin-ketjussa.

Bitcoinien ostaminen KYC:n avulla mahdollistaa vaihdon tietää nostotransaktiot, kun taas pyöreät summat ja vaihto-osoitteet mahdollistavat tietää, mikä osa transaktiosta on tarkoitettu toiselle henkilölle ja mikä osa itselle.

Yksityisyyden parantamiseksi yhteistoiminnot ja coinjoinit mahdollistavat todennäköisyyslaskelmien rikkomisen tekemällä transaktioita, joissa useat ihmiset tekevät transaktion yhdessä. Ketjuanalyysiyhtiöillä on vaikeampi määrittää, mitä teet bitcoineillasi seuraamalla.

Lightning-verkossa vain kaksi ihmistä tietää transaktiosta, ja se on luottamuksellisempi kuin Bitcoin. Sipulireititys tarkoittaa, että välisolmu ei tiedä maksun lähettäjää ja vastaanottajaa.

Lightning-verkon käyttämiseksi suositellaan seuraamaan koulutusta YouTube-kanavallasi tai suoraan discover Bitcoin -verkkosivustolla, tai käyttämään koulutusta Umbrellissa. On myös mahdollista lähettää mielivaltaista tekstiä maksun aikana Lightning-verkossa käyttämällä tähän tarkoitettua kenttää, mikä voi olla hyödyllistä lahjoituksissa tai viestinnässä.
On kuitenkin tärkeää huomata, että Lightning-reitityssolmuja saatetaan säädellä tulevaisuudessa, joissakin valtioissa pyrittäessä säätämään reitityssolmuja. Kauppiaiden on hallinnoitava likviditeettiä hyväksyäkseen maksuja Lightning-verkossa, nykyisten rajoitusten voitettavissa sopivilla ratkaisuilla.

Lopuksi, Bitcoinin tulevaisuus on lupaava mahdollisen miljoonan arvon ennustuksella viidessä vuodessa. Alan ammattimaistumisen ja olemassa olevan pankkijärjestelmän vaihtoehdon luomisen varmistamiseksi on tärkeää osallistua verkkoon ja lopettaa luottaminen.

## Kiitokset ja jatka kaninkolon tutkimista
Onnittelut! 🎉Olet suorittanut LN 201 -koulutuksen - Johdatus Lightning Networkiin!
Voit olla ylpeä itsestäsi, sillä se ei ole helppoa. Tiedä, että vain harvat ihmiset sukeltavat näin syvälle Bitcoinin maailmaan.

Ensinnäkin suuri kiitos Fanis Makalakisille, joka tarjosi meille tämän mahtavan ilmaisen kurssin Lightningin etnisemmästä näkökulmasta. Älä epäröi seurata häntä Twitterissä, hänen blogissaan tai hänen työssään LN-markkinalla.

Sitten, jos haluat auttaa projektia, älä epäröi sponsoroida meitä Patreonissa. Lahjoituksiasi käytetään uusien koulutuskurssien sisällön tuottamiseen ja tietenkin sinulle ilmoitetaan ensimmäisenä (mukaan lukien Faniksen seuraava, joka on työn alla!).

Lightning Network -seikkailu jatkuu Umbrel-koulutuksella ja Lightning Network -solmun toteuttamisella. Teoria on ohi ja on aika siirtyä käytäntöön nyt LN 202 -koulutuksen myötä!

Pusut ja nähdään pian!

Rogzy