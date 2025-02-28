---
name: Attakaï

description: muuttaa S9:n kotilämmitysjärjestelmäksi
---

![cover](assets/cover.webp)

# Attakai - mahdollistaa kotilouhinnan ja tekee siitä saavutettavaa!

"Attakaï"-aloite tutkii Bitcoin-louhintaa tuotetun lämmön hyödyntämisen kautta. Opas tarjoaa ratkaisuja louhintalaitteiden muokkaamiseksi sopiviksi käytettäväksi lämpöpattereina kodeissa, tarjoten lisää mukavuutta ja energiansäästöjä. Bitcoin säätää automaattisesti louhintavaikeutta ja palkitsee louhijat heidän työstään. Kuitenkin hashraten keskittyminen voi aiheuttaa riskejä verkon neutraaliudelle. "Attakaï" tarjoaa käytännöllisen oppaan louhintalaitteiden taloudelliseen muokkaamiseen, mahdollistaen osallistujien sähkölaskujen pienentämisen ja palkitsemisen satosheilla ilman KYC:tä.

## Johdanto

"Attakaï", joka japaniksi tarkoittaa "ihanteellista lämpötilaa", on aloitteen nimi, joka pyrkii tutkimaan bitcoin-louhintaa lämmön uudelleenkäytön kautta, jonka ovat käynnistäneet @ajelexBTC ja @BlobOnChain yhdessä Découvre Bitcoinin kanssa. Tämä ASIC-laitteiden muokkausopas toimii perustana oppia lisää louhinnasta, sen toiminnasta, viimeaikaisesta historiasta ja taustalla olevasta taloudesta.

### Miksi hyödyntää ASIC:sta tulevaa lämpöä?

On tärkeää ymmärtää suhde energian ja lämmöntuotannon välillä sähköjärjestelmässä.

1 kW:n sähköenergian investoinnilla sähköpatteri tuottaa 1 kW:n lämpöä, ei enempää eikä vähempää. Uudet patterit eivät ole tehokkaampia kuin perinteiset patterit. Niiden etu on kyvyssä jakaa lämpöä jatkuvasti ja tasaisesti huoneessa, tarjoten enemmän mukavuutta verrattuna perinteisiin pattereihin, jotka vaihtelevat korkean lämmitystehon ja lämmityksen puuttumisen välillä, aiheuttaen säännöllisiä lämpötilan vaihteluita ja epämukavuutta.

Tietokone, tai laajemmin elektroninen piirilevy, ei kuluta energiaa laskelmien suorittamiseen; se tarvitsee vain energiaa komponenttiensa läpi virtaamiseen toimiakseen. Energiankulutus johtuu komponenttien sähköisestä vastuksesta, mikä tuottaa häviöitä ja siten tuottaa lämpöä, jota kutsutaan Joulen ilmiöksi.
Jotkut yritykset ovat keksineet idean yhdistää laskentatehon tarve ja lämmitystarve lämpöpatteri/palvelimien kautta. Idea on jakaa yrityksen palvelimet pieniin yksiköihin, jotka voitaisiin sijoittaa koteihin tai toimistoihin. Tämä idea kohtaa kuitenkin useita ongelmia. Palvelimien tarve ei liity lämmitystarpeeseen, ja yritykset eivät voi käyttää palvelimiensa laskentakapasiteettia joustavasti. Myös yksilöiden käytettävissä olevalla kaistanleveydellä on rajoituksensa. Kaikki nämä rajoitukset estävät yritystä tekemästä näistä kalliista asennuksista kannattavia tai tarjoamasta vakaa online-palvelin tarjontaa ilman datakeskuksia, jotka voivat ottaa vastuun, kun lämmitystä ei tarvita.

> "Tietokoneesi lämpö ei ole hukkaan, jos tarvitset lämmittää kotiasi. Jos käytät sähkölämmitystä siellä missä asut, silloin tietokoneesi lämpö ei ole hukkaan. Se maksaa saman, jos tuotat tämän lämmön tietokoneellasi. Jos sinulla on halvempi lämmitysjärjestelmä kuin sähkö, hukka on vain kustannuserossa. Jos on kesä ja käytät ilmastointia, silloin se on kaksinkertainen.
> Bitcoin-louhinnan tulisi tapahtua siellä, missä se on halvempaa. Ehkä se on paikoissa, joissa ilmasto on kylmä ja missä lämmitys on sähköistä, missä louhinta voisi muuttua ilmaiseksi."
> Satoshi Nakamoto - 8. elokuuta 2010
Bitcoin ja sen proof of work -mekanismi erottuvat siksi, että ne säätävät automaattisesti louhinnan vaikeustasoa koko verkon suorittaman laskentatyön määrän perusteella. Tätä määrää kutsutaan hashrateksi ja se ilmoitetaan hasheina sekunnissa. Nykyään sen arvioidaan olevan 280 eksahashia sekunnissa eli 280 miljardia miljardia hashea sekunnissa. Tämä hashrate edustaa työtä ja siten käytettyä energiamäärää. Mitä korkeampi hashrate on, sitä enemmän vaikeustaso nousee, ja päinvastoin. Näin ollen Bitcoin-louhija voidaan aktivoida tai deaktivoida milloin tahansa ilman vaikutusta verkkoon, toisin kuin lämpöpatteri/palvelimet, jotka tarvitsisivat pysyä vakaina tarjotakseen palveluaan. Louhija palkitaan suoritetusta työstä suhteessa muiden tekemään työhön, riippumatta siitä, kuinka pieni tämä osallistuminen saattaa olla.

Yhteenvetona voidaan todeta, että sekä sähkölämmitin että Bitcoin-louhija tuottavat 1 kW lämpöä 1 kW sähköä kuluttaen. Louhija saa kuitenkin palkkioksi bitcoineja. Riippumatta sähkön hinnasta, bitcoinin hinnasta tai Bitcoin-verkon louhintatoiminnan kilpailusta, taloudellisesti on edullisempaa lämmittää louhijalla kuin sähköpatterilla.

![Videoesittely](https://youtu.be/gKoh44UCSnE)

### Lisäarvo Bitcoinille

Emme mene tässä yksityiskohtiin louhintatoiminnasta (resursseja saatavilla tarvittaessa akatemiassa). Tärkeää on ymmärtää, miten louhinta edistää Bitcoinin hajauttamista. Useita olemassa olevia teknologioita on yhdistetty nerokkaasti tuomaan Nakamoton konsensus eloon. Tämä konsensus taloudellisesti palkitsee rehellisiä toimijoita heidän osallistumisestaan Bitcoin-verkon toimintaan samalla kun se kannustaa epärehellisiä toimijoita. Tämä on yksi avainkohdista, joka mahdollistaa verkon kestävän olemassaolon.

Rehelliset toimijat, ne jotka louhivat sääntöjen mukaan, kilpailevat keskenään saadakseen mahdollisimman suuren osan palkkiosta uusien lohkojen tuottamisesta. Tämä taloudellinen kannustin johtaa luonnollisesti tietynlaiseen keskittymiseen, kun yritykset päättävät erikoistua tähän tuottoisaan toimintaan vähentämällä kustannuksiaan mittakaavaetujen kautta. Nämä teolliset toimijat ovat edullisessa asemassa koneiden ostamisessa ja ylläpidossa sekä neuvotellessaan sähkön tukkuhinnasta.

> "Aluksi useimmat käyttäjät pyörittäisivät verkkosolmuja, mutta kun verkko kasvaisi tietyn pisteen yli, se jäisi yhä enemmän erikoistuneiden palvelinfarmien tehtäväksi, joissa on erikoistunutta laitteistoa. Palvelinfarmi tarvitsisi pyörittää vain yhtä solmua verkossa ja loput LAN yhdistäisi siihen yhteen solmuun." - Satoshi Nakamoto - 2. marraskuuta 2008

Tietyt tahot hallitsevat merkittävää osuutta koko hashratesta suurissa louhintafarmeissa. Voimme havaita äskettäisen kylmäaallon Yhdysvalloissa, jossa merkittävä osa hashratesta otettiin pois käytöstä ohjaamaan energiaa kotitalouksiin, joilla oli poikkeuksellinen tarve sähkölle. Usean päivän ajan louhijat olivat taloudellisesti kannustettuja sammuttamaan farmejaan, ja näin voimme nähdä tämän poikkeuksellisen sään vaikutuksen Bitcoinin hashrate-käyrässä.

Tämä kysymys voisi muodostua ongelmalliseksi ja aiheuttaa merkittävän riskin verkon puolueettomuudelle. Toimija, jolla on yli 51% hashratesta, voisi helpommin sensuroida transaktioita, jos haluaisi. Siksi on tärkeää jakaa hashrate useiden toimijoiden kesken pikemminkin kuin keskittää se helpommin hallituksen esimerkiksi takavarikoitavissa oleville keskitetyille tahoille.

**Jos louhijat ovat hajallaan tuhansissa, tai jopa miljoonissa, kotitalouksissa ympäri maailmaa, valtiolle tulee hyvin monimutkaista ottaa niitä hallintaansa.**
Tehtaalla louhintalaite ei sovellu käytettäväksi lämpöpatterina asuinoloissa kahdesta pääsyystä: liiallinen melu ja säädettävyyden puute. Nämä ongelmat voidaan kuitenkin helposti ratkaista tekemällä yksinkertaisia muutoksia laitteiston ja ohjelmiston osalta, mikä mahdollistaa paljon hiljaisemman louhintalaitteen, jota voidaan konfiguroida ja automatisoida kuten nykyaikaisia sähkölämmittimiä.
**Attakaï on koulutusaloite, joka opettaa sinulle, miten voit muuttaa Antminer S9:n mahdollisimman kustannustehokkaasti.**

Tämä tarjoaa erinomaisen mahdollisuuden oppia käytännön kautta. Sähkölaskusi pienentämisen lisäksi saat palkkioksi osallistumisestasi ilmaisia KYC satseja.

## Luku 1: Käytetyn ASIC:n ostaminen

Tässä osiossa käsittelemme parhaita käytäntöjä käytetyn Bitmain Antminer S9:n ostamiseen, joka on tämän lämpöpatterimuunnoksen opetusohjelman perustana oleva laite. Tämä opas pätee myös muihin ASIC-malleihin, sillä se on yleinen opas käytetyn louhintalaitteiston ostamiseen.

Antminer S9 on laite, jonka Bitmain on tarjonnut toukokuusta 2016 lähtien. Se kuluttaa 1323W sähköä ja tuottaa 13,5 TH/s. Vaikka sitä pidetään vanhana, se on edelleen erinomainen vaihtoehto louhinnan aloittamiseen. Koska sitä on tuotettu suurissa määrin, varaosia on helppo löytää runsaasti monilta alueilta ympäri maailmaa. Yleensä sen voi hankkia vertaisverkossa sivustoilta kuten Ebay tai LeBonCoin, sillä ammattimaiset jälleenmyyjät eivät enää tarjoa sitä sen alhaisemman kilpailukyvyn vuoksi verrattuna uudempiin koneisiin. Se on vähemmän tehokas kuin maaliskuusta 2020 lähtien esitellyt ASIC:t, kuten Antminer S19, mutta tämä tekee siitä edullisen käytetyn laitteiston ja sopivamman tekemillemme muutoksille.

Antminer S9 on saatavilla useina versioina (i, j), jotka tuovat pieniä muutoksia ensimmäisen sukupolven laitteistoon. Emme usko, että tämän tulisi vaikuttaa ostospäätökseesi, ja tämä opas toimii kaikille näille versioille.

ASIC:ien hinta vaihtelee monien tekijöiden mukaan, kuten bitcoinin hinnan, verkon vaikeusasteen, koneen tehokkuuden ja sähkön hinnan mukaan. Siksi on vaikea antaa tarkkaa arviota käytetyn koneen ostamisesta. Helmikuussa 2023 odotettu hinta Ranskassa yleensä vaihtelee 100 ja 200 euron välillä, mutta nämä hinnat voivat muuttua nopeasti.

![kuva](assets/guide-achat/1.webp)

Antminer S9 koostuu seuraavista osista:

- 3 hashboardia, joissa sijaitsevat sirut, jotka tuottavat louhintatehon

![kuva](assets/guide-achat/2.webp)

- Ohjauskortti, joka sisältää paikan SD-kortille, Ethernet-portin sekä liittimet hashboardeille ja tuulettimille. Tämä on ASIC:si aivot.
  ![kuva](assets/guide-achat/3.webp)

- 3 datakaapelia, jotka yhdistävät hashboardit ohjauskorttiin.

![kuva](assets/guide-achat/4.webp)

- Virtalähde, joka toimii 220V:lla ja voidaan kytkeä kuten tavallinen kotitalouslaite.

![kuva](assets/guide-achat/5.webp)

- 2 120mm tuuletinta.

![kuva](assets/guide-achat/6.webp)

- Uros C13 -kaapeli.

![kuva](assets/guide-achat/7.webp)
Kun ostat käytetyn koneen, on tärkeää tarkistaa, että kaikki osat ovat mukana ja toimivat. Vaihdon aikana sinun tulisi pyytää myyjää käynnistämään kone varmistaaksesi sen asianmukaisen toiminnan. On tärkeää tarkistaa, että laite käynnistyy oikein, ja sen jälkeen tarkistaa internet-yhteys liittämällä Ethernet-kaapeli ja käyttämällä Bitmain-yhteysliittymää verkkoselaimen kautta samassa paikallisverkossa. Tämän IP-osoitteen löydät yhdistämällä internet-reitittimesi käyttöliittymään ja etsimällä yhdistettyjä laitteita. Osoitteen tulisi olla seuraavassa muodossa: 192.168.x.x
![kuva](assets/guide-achat/8.webp)

Tarkista myös, että oletusarvoiset tunnistetiedot toimivat (käyttäjätunnus: root, salasana: root). Jos oletusarvoiset tunnistetiedot eivät toimi, sinun on suoritettava koneen nollaus.

![kuva](assets/guide-achat/9.webp)

Yhdistämisen jälkeen sinun pitäisi pystyä näkemään kunkin hashboardin tila kojelaudalla. Jos louhija on yhdistetty louhintapooliin, sinun pitäisi nähdä kaikkien hashboardien toimivan. On tärkeää huomata, että louhijat pitävät paljon melua, mikä on normaalia. Varmista myös, että tuulettimet toimivat kunnolla.

Voit sen jälkeen poistaa edellisen omistajan louhintapoolin asettaaksesi oman myöhemmin. Halutessasi voit myös tarkastella hashboardeja purkamalla koneen. Tämä vaihe on kuitenkin monimutkaisempi ja vaatii enemmän aikaa ja tiettyjä työkaluja. Jos haluat edetä tämän purkamisen kanssa, voit viitata tämän oppaan seuraavaan osaan, jossa kerrotaan, miten se tehdään. On tärkeää huomata, että louhijat keräävät paljon pölyä ja vaativat säännöllistä huoltoa. Voit havaita tämän pölyn kertymisen ja huollon laadun purkamalla koneen.
Kaikkien näiden kohtien tarkistamisen jälkeen voit ostaa koneesi suurella luottamuksella. Jos epäröit, ota yhteyttä yhteisöön, ja jos tarvitset laitteita tämän oppaan suorittamiseen, lähetä meille viesti.
Tiivistääkseni tämän oppaan yhteen lauseeseen: **"Älä luota, varmista."**

## Luku 2: Osto-opas muutostyön osille

![kuva](assets/piece/1.webp)

### Kuinka muuttaa Antminer S9 hiljaiseksi ja yhdistetyksi lämmittimeksi?

Jos omistat Antminer S9:n, tiedät todennäköisesti, kuinka äänekäs ja kömpelö se voi olla. On kuitenkin mahdollista muuttaa se hiljaiseksi ja yhdistetyksi lämmittimeksi noudattamalla muutamia yksinkertaisia vaiheita. Tässä artikkelissa esittelemme tarvittavat laitteet muutosten tekemiseen, kun taas myöhemmässä artikkelissa selitetään yksityiskohtaisesti vaiheet, joita seurata näiden muutosten tekemiseksi.

### 1. Vaihda tuulettimet

Antminer S9:n alkuperäiset tuulettimet ovat liian äänekkäitä käyttääkseen sitä lämmittimenä. Ratkaisu on vaihtaa ne hiljaisempiin tuulettimiin. Tiimimme on testannut useita malleja Noctua-merkiltä ja valinnut Noctua NF-A14 iPPC-2000 PWM:n parhaaksi kompromissiksi. Varmista, että valitset 12V version tuulettimista. Tämä 140mm tuuletin voi tuottaa jopa 1300W lämpöä ylläpitäen teoreettisen melutason 31 dB. Näiden 140mm tuulettimien asentamiseen tarvitset 140mm - 120mm sovittimen, jonka löydät DécouvreBitcoin-kaupasta. Lisäämme myös 140mm suojaverkot.

![kuva](assets/piece/1.webp)
![kuva](assets/piece/2.webp)
![kuva](assets/piece/3.webp)
Virtalähteen tuuletin on myös melko äänekäs ja se täytyy vaihtaa. Suosittelemme Noctua NF-A6x25 PWM -mallia. Huomaa, että Noctuan tuulettimien liittimet eivät ole samanlaisia kuin alkuperäiset, joten tarvitset liitinadapterin niiden kytkemiseen. Kaksi pitäisi riittää. Varmista jälleen, että valitset tuulettimen 12V version.
![kuva](assets/piece/4.webp)
![kuva](assets/piece/5.webp)

### 2. Lisää WIFI/Ethernet-silta

Ethernet-kaapelin sijaan voit yhdistää Antminerisi WIFIin lisäämällä WIFI/Ethernet-sillan. Olemme valinneet vonets vap11g-300:n, koska se mahdollistaa helposti WIFI-signaalin noutamisen Internet-laitteestasi ja sen lähettämisen Antminerillesi Ethernetin kautta luomatta aliverkkoa. Jos sinulla on sähkötekniikan taitoja, voit kytkeä sen suoraan Antminerisi virtalähteeseen ilman USB-laturin lisäämistä. Tätä varten tarvitset naaraspuolisen 5,5mmx2,1mm jakin.

![kuva](assets/piece/6.webp)
![kuva](assets/piece/7.webp)

### 3. Valinnainen: Lisää älypistoke

Jos haluat kytkeä Antminerisi päälle/pois päältä älypuhelimellasi ja seurata sen energiankulutusta, voit lisätä älypistokkeen. Testasimme ANTELA-pistoketta 16A versiona, joka on yhteensopiva smartlife-sovelluksen kanssa. Tämä älypistoke mahdollistaa päivittäisen ja kuukausittaisen energiankulutuksen tarkistamisen ja yhdistää suoraan Internet-laitteeseesi WIFI:n kautta.
![kuva](assets/piece/8.webp)

> Laitteiden ja linkkien lista
>
> - 2X 3D adapterikappale 140mm to 120mm
> - 2X NF-A14 iPPC-2000 PWM [linkki](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X 140mm tuuletinsuojat [linkki](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [linkki](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
- Sähköasentajan sokeri 2,5mm2 [linkki](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- Vonets vap11g-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
- Vaihtoehtoinen ANTELA älypistoke https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

## Luku 3 - OPAS: Kuinka muuttaa louhija lämmittimeksi?

![kuva](assets/hardware/0.webp)

Jos olet taitava tee-se-itse -henkilö ja haluat muuttaa louhijan lämmittimeksi, tämä opas on sinua varten. Haluamme varoittaa, että elektronisen laitteen muokkaaminen voi aiheuttaa sähkö- ja tulipaloriskejä. On välttämätöntä ryhtyä kaikkiin tarvittaviin varotoimiin vahinkojen tai loukkaantumisten välttämiseksi.
Tehtaalta tullessaan louhija ei oikein sovellu kodin patteriksi, koska se on liian meluisa eikä säädettävissä. On kuitenkin mahdollista tehdä yksinkertaisia muutoksia näiden ongelmien ratkaisemiseksi.

> VAROITUS: On välttämätöntä, että olet aiemmin asentanut Braiins OS+:n louhijaasi tai jonkin muun ohjelmiston, joka voi vähentää koneesi suorituskykyä. Tämä toimenpide on ratkaisevan tärkeä, koska melun vähentämiseksi asennamme vähemmän tehokkaita tuulettimia, jotka voivat hajottaa vähemmän lämpöä.

### Tarvittavat Materiaalit

- 2 kpl 3D-sovitinta 140mm - 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM -tuuletinta
- 2 140mm tuuletinsuojaa
- 1 Noctua NF-A6x25 PWM -tuuletin
- 2,5mm2 sähköasentajan sokeri
- Vonets VAP11G-300
- Vaihtoehtoinen: ANTELA älypistoke

### Tuulettimien vaihtaminen

Aloitamme virtalähteen tuulettimen vaihtamisella.

> VAROITUS: Ennen kaikkea, ennen kuin aloitat, varmista, että olet irrottanut louhijan pistorasiasta välttääksesi sähköiskun vaaran.

![kuva](assets/hardware/1.webp)

Aloitamme virtalähteen tuulettimen vaihtamisella.

Ensimmäiseksi, poista 6 ruuvia kotelon sivusta, jotka pitävät sen kiinni. Kun ruuvit on poistettu, avaa varovasti kotelo poistaaksesi muovikannen, joka suojaa komponentteja.

![kuva](assets/hardware/2.webp)
![kuva](assets/hardware/3.webp)
Seuraavaksi on aika poistaa alkuperäinen tuuletin varoen, ettei vahingoita muita komponentteja. Tätä varten irrota ruuvit, jotka pitävät sitä paikallaan, ja varovasti kuori pois valkoinen liima liittimen ympäriltä. On tärkeää edetä hienovaraisesti välttääkseen johdoille tai liittimille aiheutuvia vahinkoja. ![kuva](assets/hardware/4.webp)

Kun alkuperäinen tuuletin on poistettu, huomaat, että uuden Noctua-tuulettimen liittimet eivät vastaa alkuperäisen tuulettimen liittimiä. Uudessa tuulettimessa on nimittäin 3 johtoa, mukaan lukien keltainen johto, joka mahdollistaa nopeudensäädön. Tässä tapauksessa tätä johtoa ei kuitenkaan käytetä. Uuden tuulettimen liittämiseksi suositellaan erityisen sovittimen käyttöä. On kuitenkin tärkeää huomata, että tämä sovitin voi joskus olla vaikea löytää.

![kuva](assets/hardware/5.webp)

Jos sinulla ei ole tätä sovitinta, voit silti jatkaa uuden tuulettimen liittämistä käyttämällä johdon mutteria. Tätä varten sinun on leikattava sekä vanhan että uuden tuulettimen kaapelit.

![kuva](assets/hardware/6.webp)
![kuva](assets/hardware/7.webp)

Uudessa tuulettimessa käytä leikkuria ja leikkaa varovasti pääsuojan ääriviivat 1cm päästä leikkaamatta alla olevien kaapeleiden suojia.

![kuva](assets/hardware/8.webp)

Vedä sitten pääsuoja alaspäin ja leikkaa punaisen ja mustan kaapelin suojat samalla tavalla kuin aiemmin. Ja leikkaa keltainen kaapeli tasaiseksi.

![kuva](assets/hardware/9.webp)

Vanhan tuulettimen kohdalla pääsuojan leikkaaminen vahingoittamatta punaisten ja mustien johtojen suojia on herkempi tehtävä. Tätä varten käytimme neulaa, jonka liu'utimme pääsuojan ja punaisten sekä mustien johtojen väliin.

![kuva](assets/hardware/10.webp)
![kuva](assets/hardware/11.webp)

Kun punaiset ja mustat johdot ovat paljaana, leikkaa suojat varovasti välttääksesi sähköjohtojen vahingoittamisen.

![kuva](assets/hardware/12.webp)

Tämän jälkeen yhdistä kaapelit johdon mutterilla, musta johto mustan kanssa ja punainen johto punaisen kanssa. Voit myös lisätä sähköteippiä.

![kuva](assets/hardware/13.webp)
![kuva](assets/hardware/14.webp)

Kun yhteys on muodostettu, on aika asentaa uusi Noctua-tuuletin ritilän kanssa ja käyttää vanhoja ruuveja, uudet ruuvit laatikosta käytetään myöhemmin. Varmista, että asennat sen oikeaan suuntaan. Huomaat nuolen yhdellä puolella tuuletinta, joka osoittaa ilmavirran suunnan. On tärkeää asettaa tuuletin siten, että tämä nuoli osoittaa kotelon sisäpuolelle. Kytke sitten tuuletin uudelleen.
![kuva](assets/hardware/15.webp)![kuva](assets/hardware/16.webp)

> Vaihtoehtoisesti: Jos olet taitava sähköasioissa, voit suoraan lisätä naaras 5.5mm jakkiliittimen 12V virtalähteeseen, mikä mahdollistaa Vonet Wi-Fi sillan suoran virransyötön. Jos kuitenkin epäilet sähköosaamistasi, on turvallisempaa käyttää USB-liitintä älypuhelimen laturin kanssa välttääksesi oikosulun tai sähkövahingon riskin.

![kuva](assets/hardware/17.webp)

Kun yhteydet on muodostettu, varmista, että asetat muovikannen muovikotelon päälle eikä sisälle.

![kuva](assets/hardware/18.webp)
Lopuksi aseta kotelon kansi takaisin paikalleen ja kiristä kuusi ruuvia sivuilla pitääksesi kaiken turvallisesti paikoillaan. Ja siinä se, virtalähteesi kotelo on nyt varustettu uudella tuulettimella.
### Kahden päätuulettimen vaihto

1. Irrota ensin tuulettimet ja ruuvaa ne irti.
   ![image](assets/hardware/19.webp)

2. Uusien Noctua-tuulettimien liittimet eivät sovi alkuperäisiin, mutta älä hätäänny! Ota veitsesi esiin ja leikkaa varovasti pienet muoviset välilehdet pois, jotta liittimet sopivat täydellisesti louhijaasi.

![image](assets/hardware/20.webp)
![image](assets/hardware/21.webp)

3. On aika asentaa 3D-osat!
   Kiinnitä ne louhijan molemmille puolille käyttäen tuulettimista irrottamiasi ruuveja. Kiristä ruuvi, kunnes ruuvin pää uppoaa 3D-osaan ja se on turvallisesti paikoillaan. Ole varovainen, ettet kiristä liikaa, sillä saatat vahingoittaa osaa ja yksi ruuveista saattaa koskettaa kondensaattoria! Leikkaa sitten varovasti pienet muoviset välilehdet pois, jotta liittimet sopivat täydellisesti louhijaasi.

![image](assets/hardware/22.webp)

4. Nyt siirrytään tuulettimiin.
   Kiinnitä ne 3D-osiin mukana tulleilla ruuveilla. Kiinnitä huomiota ilmavirran suuntaan, tuulettimien sivuilla olevat nuolet osoittavat suunnan. Mene Ethernet-portin puolelta toiselle puolelle. Katso alla oleva kuva.

![image](assets/hardware/23.webp)
![image](assets/hardware/24.webp)
![image](assets/hardware/25.webp)

5. Viimeinen vaihe: kytke tuulettimet ja kiinnitä ritilät päälle käyttämättömillä ruuveilla tuuletinlaatikosta. Sinulla on vain 4, mutta 2 ritilää kohden vastakkaisissa kulmissa riittää. Tarvittaessa voit myös etsiä muita samanlaisia ruuveja rautakaupasta.

![image](assets/hardware/26.webp)
'![image](assets/hardware/27.webp)

Odottaessasi, että voimme tarjota seksikkäämmän kotelon uudelle lämmittimellesi, voit kiinnittää kotelon ja virtalähteen yhteen sähköasentajan nippusiteillä.

![image](assets/hardware/28.webp)

Ja viimeisenä silauksena, yhdistä Vonet-silta virtalähteen Ethernet-porttiin. Jos et ole vielä tehnyt niin, voit seurata tätä opasta sillan asettamiseksi.

![image](assets/hardware/29.webp)

Ja siinä se, onnittelut! Olet juuri vaihtanut louhijasi koko mekaanisen osan. Nyt sinun pitäisi kuulla huomattavasti vähemmän melua.

## Luku 4 - Ohjelmiston muokkaus - Antminer S9:n nollaus

**Artikkelisarjan tarjoavat BlobOnChain & Ajelex - 15.02.2023**

### Nollaus "Reset"-painikkeella

Tätä menetelmää voidaan soveltaa 10 minuutin kuluessa louhijan käynnistämisestä.

Kun louhija on ollut päällä 2 minuuttia, paina "Reset"-painiketta 5 sekunnin ajan ja vapauta se sitten. Louhija palautuu tehdasasetuksiin 4 minuutin kuluessa ja käynnistyy automaattisesti uudelleen (sinun ei tarvitse sammuttaa sitä).

![image](assets/software/1.webp)

Palautus verkkopuolelta

Kirjaudu louhijasi käyttöliittymään, klikkaa "Upgrade" >> "Perform a reset", ja klikkaa sitten "OK" ponnahdusikkunassa.

### Alkuperäinen käyttöjärjestelmä
Tässä osiossa oletetaan, että kone toimii, on käynnissä ja sen alkuperäinen käyttöjärjestelmä on asennettu. Näemme lyhyesti Bitmainin tarjoaman alkuperäisen käyttöjärjestelmän käyttöliittymän.
Ensiksi, yhdistä koneeseesi paikallisverkon kautta:

![kuva](assets/software/2.webp)

Kirjautumissivulla sinun tulee kirjautua ASICiin oletustunnuksilla:

- käyttäjäname: root
- salasana: root

(Miten nollata, jos oletussalasana ei toimi?)

Pääkäyttöjärjestelmä on suhteellisen perus. Neljällä välilehdellä: Järjestelmä, Louhijan Konfiguraatio, Louhijan Tila, Verkko. Louhijan Konfiguraatio -välilehdellä voit konfiguroida jopa 3 louhintapoolia.

![kuva](assets/software/3.webp)

Louhijan Tila -välilehdellä voit tarkastella erilaisia tietoja ASICin reaaliaikaisesta toiminnasta. Hashrate ilmaistaan GH/s:ssä, tarkempia tietoja poolista sekä tietoja kunkin hashboardin tilasta ja tuulettimen nopeudesta kierroksina/minuutti.

![kuva](assets/software/4.webp)

### Braiins OS+'

Nyt tutkimme ASICien Braiins OS+ -ohjelmistoa (https://braiins.com/os/plus). Ohjelmiston on kehittänyt Braiins-yritys (https://braiins.com/), joka on louhintapoolin Braiins Pool (https://braiins.com/pool) emoyhtiö. Tämä louhintapooli omistaa tällä hetkellä 4,39% globaalista hashratesta (https://mempool.space/fr/mining/pool/slushpool) kirjoitushetkellä. Prahaan perustettu yritys tunnettiin aiemmin nimellä Slushpool ja se on ensimmäinen louhintapooli, joka aloitti marraskuussa 2010. Nykyään yritys tarjoaa louhinnan kannattavuuden tutkimustyökaluja (https://insights.braiins.com/en), louhintatilan hallintaratkaisuja yhdessä pool-toimintansa ja ASICien optimointiohjelmistonsa kanssa. Se tarjoaa myös louhintaa uudella Stratum V2 -protokollalla (https://braiins.com/bitcoin-mining-stack-upgrade).

Tutkimme siis tarkemmin Bitmain-laitteiden toimintaa, jotka ovat tällä hetkellä ainoat yhteensopivat mallit:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Braiins OS -ohjelmiston voi helposti asentaa kaikkiin yllä mainittuihin koneisiin. Se mahdollistaa tarkemman koneen hallinnan sallimalla ylikellotuksen tai alikellotuksen. Se mahdollistaa myös kunkin piirin taajuuden hienosäädön automaattisen optimointiominaisuuden, kutsuttu autotuning, avulla. Koska jokainen hashaavapiiri on hieman erilainen valmistusprosessinsa vuoksi, ohjelmisto testaa optimaalisen taajuuden jokaiselle piirille saavuttaakseen maksimaalisen tehokkuuden (W/THs). Ohjelmiston väitetään saavuttavan suorituskyvyn, joka voi olla 25% korkeampi kuin alkuperäinen. Mittaustemme mukaan nämä luvut ovat saavutettavissa.

## Braiins OS+:n asentaminen

ASICiin voi asentaa Braiins OS+:n usealla eri tavalla. Voit viitata tähän oppaaseen sekä Braiinsin viralliseen dokumentaatioon ja video-oppaisiin.
Asenna Braiins OS+ suoraan Antminerisi muistiin käyttäen BOS-työkalupakkia, korvaten alkuperäisen käyttöjärjestelmän, seuraavien yksityiskohtaisten vaiheiden avulla. Jos haluat säilyttää alkuperäisen käyttöjärjestelmän rinnalla, voit asentaa Braiins OS+:n SD-kortille.
1. Käynnistä Antminerisi ja yhdistä se internet-laatikkoosi.
2. Lataa BOS toolbox Windowsille / Linuxille.
3. Pura ladattu tiedosto ja avaa bos-toolbox.bat-tiedosto, valitse kieli, ja hetken kuluttua näet tämän ikkunan:
   ![kuva](assets/software/5.webp)

4. BOS toolbox mahdollistaa Antminerisi IP-osoitteen helposti löytämisen ja Braiins OS+:n asentamisen. Jos tiedät jo koneesi IP-osoitteen, voit siirtyä suoraan vaiheeseen 8. Muussa tapauksessa siirry skannaus-välilehteen.

![kuva](assets/software/6.webp)

5. Yleensä kotiverkoissa IP-osoitteen alue on välillä 192.168.1.1 ja 192.168.1.255, joten syötä "192.168.1.0/24" IP-alue -kenttään. Jos verkkosi on erilainen, vaihda nämä osoitteet. Sen jälkeen klikkaa "Aloita".

6. Huomio, jos Antminerissasi on salasana, havaitseminen ei toimi. Jos näin on, yksinkertaisin ratkaisu on suorittaa tehdasasetusten palautus.

7. Sinun pitäisi nähdä kaikki verkkosi Antminerit, tässä IP-osoite on 192.168.1.37.

![kuva](assets/software/7.webp)

8. Klikkaa Takaisin, siirry sitten asennus-välilehteen, syötä aiemmin löydetty IP-osoite Miner(s)-kenttään ja "admin" (tai "root") Salasana-kenttään, joka on oletussalasana, ja klikkaa sitten "Aloita".
   Jos asennus ei toimi "admin" tai "root" salasanalla, voi olla tarpeen suorittaa tehdasasetusten palautus ja yrittää uudelleen.

![kuva](assets/software/8.webp)

9. Hetken kuluttua Antminerisi käynnistyy uudelleen ja pääset käsiksi Braiins OS+:n käyttöliittymään kyseisessä IP-osoitteessa, tässä 192.168.1.37, suoraan selaimesi osoiteriviltä. Oletuskäyttäjänimi on "root" ja oletussalasanaa ei ole.
   Braiins OS+:n asentaminen SD-kortille

![kuva](assets/software/9.webp)

![kuva](assets/software/10.webp)

Toinen menetelmä käyttää Antminerisi alkuperäistä käyttöliittymää. Tämä menetelmä toimii koneilla, joiden käyttöjärjestelmä on vuodelta 2019 tai sitä vanhempi.

### Antminerin Käyttöliittymä

1. Lataa asennettava uusi käyttöjärjestelmä täältä.
2. Kuten edellisessä osiossa, yhdistä koneeseesi paikallisverkon kautta.
3. Siirry Järjestelmä-välilehteen ja sitten Päivitykseen.
4. Lataa ladattu tiedosto ja flashaa kuva.

![kuva](assets/software/11.webp)

### Micro SD -kortti

Toinen menetelmä mahdollistaa micro SD -kortin käytön. Tämä menetelmä toimii vain koneilla, joiden käyttöjärjestelmä on vuodelta 2019 tai sen jälkeen.

1. Lataa asennettava uusi käyttöjärjestelmä täältä.

2. Flashaa ladattu kuva micro SD -kortille. Tähän voit käyttää Etcher-ohjelmaa. Pelkkä tiedoston kopioiminen micro SD -kortille ei toimi.
3. Jos omistat Antminer S9:n tai sen muunnelmat (S9i, S9j), sinun täytyy säätää hyppylankoja pakottaaksesi ASIC:si käynnistymään tiedostosta mikro SD-kortilla NAND:n sijaan. Jos sinulla on eri malli, voit siirtyä osaan 4. Hyppylangat sijaitsevat ohjauslevyllä ASIC:n yläosassa, lähellä Ethernet-porttia. Sinun täytyy poistaa se liu'uttamalla sitä taaksepäin. Kun hyppylangan asento on muutettu kuvien alla näytetyllä tavalla BOOT FROM SD, voit asettaa ohjauslevyn takaisin paikalleen ja kytkeä S9:n uudelleen.
![kuva](assets/software/12.webp)

![kuva](assets/software/13.webp)

4. Aseta mikro SD-kortti ASIC:iin.
5. Käynnistä ASIC. Jos automaattisen asennuksen versio oli käytössä, uusi käyttöjärjestelmä asennetaan automaattisesti. Asennus on valmis, kun molemmat LEDit syttyvät samanaikaisesti. Voit käynnistää ASIC:n uudelleen ja poistaa mikro SD-kortin. Jos latasit toisen version, sinun täytyy jättää mikro SD-kortti ASIC:iin.

Lisätietoja asennuksesta löydät Braiins-verkkosivuston tästä osiosta.

## Käyttöliittymä

Sinun täytyy muodostaa yhteys ASIC:iisi samankaltaisella tavalla. Käyttämällä laitteesi paikallista IP-osoitetta verkossasi selaimen kautta.

Oletuskäyttäjätunnukset ovat samat kuin alkuperäisessä käyttöjärjestelmässä.

- käyttäjätunnus: root
- salasana: root

Tämän jälkeen sinut toivottaa tervetulleeksi Brains OS+ -hallintapaneeli.

### Hallintapaneeli

![kuva](assets/software/14.webp)

Tällä ensimmäisellä sivulla voit tarkkailla koneesi reaaliaikaista suorituskykyä.

- Kolme reaaliaikaista graafia, jotka näyttävät lämpötilan, hashraten ja koneen kokonaistilan.
- Oikealla todellinen hashrate, piirien keskimääräinen lämpötila, arvioitu tehokkuus W/THs:ssa ja virrankulutus.
- Alla tuulettimen nopeus prosentteina maksiminopeudesta ja kierrosten määrä minuutissa.

![kuva](assets/software/15.webp)

- Alempana löydät yksityiskohtaisen näkymän kustakin hashboardista. Lautan keskimääräinen lämpötila ja sen sisältämät piirit, jännite ja taajuus.
- Tiedot aktiivisista louhintapoolista Pools-osiossa.
- Autotunauksen tila Tuner Status -osiossa.
- Oikealla tiedot poolille lähetetyistä osuuksista.

### Konfiguraatio

![kuva](assets/software/16.webp)

### Järjestelmä

![kuva](assets/software/17.webp)

### Pikatoiminnot

![kuva](assets/software/18.webp)

Louhintapoolin konfigurointi
Voit ajatella louhintapoolia maatalousosuuskuntana. Maanviljelijät kokoavat tuotantonsa yhteen vähentääkseen tarjonnan ja kysynnän vaihtelua ja siten saadakseen vakautta toimintaansa. Louhintapool toimii samalla tavalla, ja yhteen koottava raaka-aine on hasheja. Itse asiassa yhden kelvollisen hashin löytäminen mahdollistaa lohkon luomisen ja siten kolikkoalustan tai palkkion voittamisen, joka on tällä hetkellä 6,25 BTC:n lisäksi lohkoon sisältyvät transaktiomaksut. Jos louhit yksin, saat palkkion vain löytäessäsi lohkon. Kilpaillessasi kaikkia muita louhijoita vastaan maapallolla, sinulla olisi hyvin vähän mahdollisuuksia voittaa tämä suuri arpajainen, ja sinun täytyisi silti maksaa louhintalaitteesi käyttöön liittyvät maksut ilman menestyksen takeita. Louhintapoolit ratkaisevat tämän ongelman yhdistämällä useiden (tuhansien) louhijoiden laskentatehon ja jakamalla palkinnot osallistumisprosentin mukaan poolin hashrateen, kun lohko löydetään. Voit visualisoida mahdollisuutesi louhia lohko yksin käyttämällä tätä työkalua. Syöttämällä Antminer S9:n tiedot näemme, että mahdollisuudet löytää hash, joka mahdollistaa lohkon luomisen, ovat 1 24 777 849:stä jokaista lohkoa kohden tai 1 172 068:ssa päivässä. Keskimäärin (jatkuvalla hashratella ja vaikeustasolla) kestäisi 471 vuotta löytää lohko.
Kuitenkin, koska kaikki Bitcoinissa perustuu todennäköisyyteen, joskus käy niin, että yksin louhivat louhijat palkitaan tämän riskin ottamisesta: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Jos pidät uhkapelaamisesta, voit kokeilla, mutta oppaamme ei keskity siihen suuntaan. Sen sijaan keskitymme löytämään louhintapoolin, joka parhaiten vastaa tarpeitamme luoda lämmitysjärjestelmä.
Louhintapoolia valittaessa huomioon otettavia seikkoja ovat poolin palkkioiden toiminta, joka voi olla erilainen, sekä vähimmäismäärä ennen kuin palkkiot voidaan nostaa osoitteeseen. Esimerkiksi Braiins, joka tarjoaa tässä puhuttavan ohjelmiston, tarjoaa myös poolin. Tällä poolilla on palkkiojärjestelmä nimeltä "Score", joka kannustaa louhijoita louhimaan pitkiä aikoja. Osallistuminen sisältää aktiivisuusajan tekijän, joka ilmaistaan "scoring hashratella". Tapauksessamme, kun haluamme lämmitysjärjestelmän, joka voidaan kytkeä päälle vain muutamaksi minuutiksi, tämä ei ole ihanteellinen palkkiojärjestelmä. Suosimme palkkiojärjestelmää, joka antaa meille saman palkkion jokaisesta osallistumisesta. Lisäksi Braiins Poolin vähimmäisnostomäärä on 100 000 satsia ja On-Chain. Joten menetämme joitakin satseja transaktiomaksuissa ja osa palkkiostamme voi jäädä lukkoon, jos emme louhi tarpeeksi talven aikana.

Meitä kiinnostava palkkiomalli on PPS, joka tarkoittaa "pay-per-share". Tämä tarkoittaa, että louhija saa palkkion jokaisesta kelvollisesta osuudesta. Tästä järjestelmästä on myös variantti, FPPS (Full Pay Per Share), joka jakaa paitsi kolikkoalustan palkkion, myös lohkoon sisältyvät transaktiomaksut. Louhintapooleja, joita suosittelemme yhdistämään louhinta-/lämmitysjärjestelmääsi, ovat Linecoin Pool (FPPS) ja Nicehash (PPS).

- Nicehash: Nicehashin etuna on, että nosto voidaan tehdä käyttäen Lightningia minimaalisin maksuin. Lisäksi vähimmäisnostomäärä on 2000 satsia. Haittapuolena on, että Nicehash käyttää hashrateaan tuottoisimpaan lohkoketjuun antamatta todellista kontrollia käyttäjälle, joten se ei välttämättä osallistu Bitcoinin hashrateen.
- Linecoin: Linecoinin etuna on tarjottavien ominaisuuksien määrä, kuten yksityiskohtainen hallintapaneeli, mahdollisuus tehdä nostoja Paynymilla (BIP 47) paremman yksityisyydensuojan saavuttamiseksi, sekä Telegram-botin integrointi että suoraan mobiilisovelluksessa konfiguroitavat automaatiot. Tämä allas louhii vain Bitcoin-lohkoja, mutta nostojen minimimäärä pysyy korkeana, 100 000 satoshissa. Tarkastelemme yhden näistä altaista käyttöliittymää tarkemmin tulevassa artikkelissa.
Braiins 0S+:ssa altaan konfiguroimiseksi sinun on luotava tili valitsemassasi altaassa. Tässä otamme esimerkiksi Linecoinin:

![kuva](assets/software/19.webp)

Kun tilisi on luotu, klikkaa Yhdistä altaaseen

Kopioi sitten Stratum-osoite sekä käyttäjänimesi:

![kuva](assets/software/20.webp)

Voit nyt palata Braiins OS+ -käyttöliittymään syöttääksesi nämä tunnistetiedot. Salasanakentän voit jättää tyhjäksi.

![kuva](assets/software/21.webp)

### Ylikellotus ja Alakellotus

Ylikellotus ja autotuning molemmat sisältävät taajuuden säätämisen louhintakorteissa ASIC-suorituskyvyn parantamiseksi. Ero näiden kahden välillä on näiden taajuusasetusten monimutkaisuudessa.

**Ylikellotus** on yksinkertainen säätö, joka sisältää taajuuden nostamisen louhintakorteissa koneen hashraten kasvattamiseksi. Alakellotus puolestaan sisältää integroidun piirin kellotaajuuden pienentämisen alle sen nimellistaajuuden. ASICin kellotaajuuden pienentämällä alakellotuksen avulla myös laitteiston tuottama lämpö vähenee. Tämä mahdollistaa ASICin jäähdyttämiseen tarvittavien tuulettimien nopeuden vähentämisen, koska niiden ei tarvitse työskennellä yhtä kovasti sopivan lämpötilan ylläpitämiseksi. Tuulettimien nopeuden vähentämällä myös ASICin tuottama melu vähenee. Tämä voi olla erityisen hyödyllistä käyttäjille, jotka käyttävät ASICeja kotona ja pyrkivät minimoimaan louhintalaitteiston aiheuttamat meluhäiriöt.

On tärkeää huomata, että alakellotus voi johtaa ASICin suorituskyvyn heikkenemiseen, joten on tärkeää löytää hyvä tasapaino suorituskyvyn ja melun välillä.

Braiins OS+ tukee ASICien ylikellotusta, alakellotusta ja autotuningia. Se mahdollistaa käyttäjien säätää joustavasti laitteistonsa kellotaajuutta maksimoidakseen suorituskyvyn tai säästääkseen energiaa heidän mieltymystensä mukaan.

### Autotuning

Ennen vuotta 2018, louhijat saivat etua toiminnassaan kahdella tavalla: löytämällä sähköä kohtuulliseen hintaan ja ostamalla tehokkaampaa laitteistoa. Kuitenkin vuonna 2018, kaivosohjelmistojen ja -firmwaren alalla löydettiin uusi edistysaskel, nimeltään AsicBoost. Tämä tekniikka mahdollistaa louhijoiden vähentää kustannuksiaan noin 13% muokkaamalla laitteissaan toimivaa firmwarea.
Nykyään on olemassa uusi edistysaskel ohjelmisto- ja firmware-kaivossektorilla nimeltään autotuning, joka tarjoaa vielä suuremman edun kuin AsicBoost. ASICit koostuvat monista pienistä tietokonepiireistä, jotka suorittavat hashauksen. Nämä piirit on valmistettu piistä, samaa alkuainetta, jota käytetään laajalti puolijohteissa ja muissa mikroelektronisissa komponenteissa. Keskeinen ymmärrys tässä on, että kaikki pii-piirit eivät ole identtisiä - jokainen voi vaihdella hieman sähköisissä ominaisuuksissaan. Laitteiden valmistajat tietävät tämän ja julkaisevat kaivoskoneidensa suorituskykyspesifikaatiot perustuen niiden toleranssien alarajaan. Toisin sanoen, valmistajat tietävät taajuuden, joka toimii parhaiten keskimääräisille piireille, ja he käyttävät tätä taajuutta yhtenäisesti kaikille koneen piireille.
Tämä asettaa ylärajan sille, kuinka suuren hashraten kone voi saavuttaa. Autotuning on prosessi, jossa algoritmit arvioivat optimaaliset taajuudet piiri piiriltä tapahtuvalle hashaukselle, sen sijaan, että koko konetta kohdeltaisiin yhtenä yksikkönä. Tämä tarkoittaa, että laadukkaampi piiri, joka pystyy suorittamaan enemmän hasheja sekunnissa, saa korkeamman taajuuden, ja laadultaan heikompi piiri, joka pystyy suorittamaan suhteellisesti vähemmän hasheja, saa matalamman taajuuden. Piiritason autotuning on olennaisesti tapa optimoida ASIC:n suorituskykyä sen päällä toimivan ohjelmiston ja firmwaren avulla.

Lopputuloksena on korkeampi hashrate wattia kohden, mikä tarkoittaa suurempia voittomarginaaleja louhijoille. Syy siihen, miksi koneita ei jaeta tämän tyyppisen ohjelmiston kanssa, on se, että koneiden vaihtelu on epätoivottavaa, koska asiakkaat haluavat tietää tarkalleen, mitä he saavat, ja siksi on huono idea valmistajille myydä tuotetta, joka ei tarjoa johdonmukaista ja ennustettavaa suorituskykyä koneesta toiseen. Lisäksi, piiritason autotuning vaatii huomattavia kehitysresursseja, koska sen toteuttaminen on monimutkaista. Valmistajat käyttävät jo paljon resursseja kehittäessään omia firmwarejaan. On olemassa ohjelmistoratkaisuja, jotka mahdollistavat autotuningin, kuten Braiins OS+. Lisäksi ASIC:n suorituskykyä voidaan parantaa jopa 20%.

> Opas luotu DecouvreBitcoinin toimesta, lisätietoja MINAGE 201 - luotto Jim ja Ajelex'