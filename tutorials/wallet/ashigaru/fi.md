---
name: Ashigaru
description: Samourain fork Wallet turvaa, hallitsee ja sekoittaa bitcoinit
---

![cover](assets/cover.webp)



Ashigaru on Bitcoin-mobiilikäyttöön tarkoitettu wallet-sovellus, joka on jatkoa Samourai Wallet -projektille, mutta uudessa muodossa. Tämä ohjelmisto syntyi erityisessä tilanteessa: huhtikuussa 2024 Yhdysvaltain viranomaiset pidättivät Samourai Wallet:n perustajat ja heidän palvelimensa takavarikoitiin. Vaikka itse Samurai-sovellus säilyi käyttökelpoisena, sitä ei tällä hetkellä enää ylläpidetä. Ashigaru on ilmainen fork-versio Samurai Wallet:sta, jota ylläpitää anonyymi tiimi, joka takaa Samurain toiminnallisuuden jatkuvuuden ja turvaa sen alkuperäisen filosofian: Bitcoin:n käyttäjien yksityisyyden ja itsemääräämisoikeuden puolustamisen.



Ashigaru ottaa paljon Samourain DNA:sta: samankaltainen käyttöliittymä, ilmeisen itsehuolellinen lähestymistapa, avoin lähdekoodi ja keskittyminen yksityisyyteen. Koodi jaetaan GNU GPLv3 -lisenssillä, joka takaa, että kuka tahansa voi tarkastaa, muokata tai levittää ohjelmistoa.



Ashigaru-sovellus sisältää joukon kehittyneitä työkaluja UTXO:iden luottamuksellisuutta ja hallintaa varten:




- Whirlpool**, Zerolinkiin perustuva kolikkoliitosprotokolla, jonka avulla voit katkaista deterministiset yhteydet transaktioiden sisään- ja ulostulojen välillä menettämättä kuitenkaan rahojesi hallintaa.
- PayNym**, joka toteuttaa uudelleenkäytettäviä maksukoodeja (BIP47), nyt "*Pepehash*"-avattarijärjestelmän avulla.
- Ricochet**, ominaisuus, joka lisää tapahtumiin välihyppyjä vaikeuttaakseen niiden jäljittämistä.
- Ja tietenkin ***Coin Control***, jolla voit valita, jäädyttää ja merkitä UTXO:t tarkasti.
- Eräkohtainen lähetys***, jolla voidaan vähentää kustannuksia ryhmittelemällä useita maksuja yhdeksi maksutapahtumaksi.
- **Stealth Mode**, joka piilottaa sovelluksen kännykkääsi tekaistun käynnistysohjelman taakse, jotta se jää huomaamatta puhelimen fyysisen tarkastuksen aikana.
- Edistyneet kulutustyökalut luottamuksellisuuden optimoimiseksi (payjoin, stonewall...).
- Optimoitu palautusjärjestelmä, jossa käytetään salasanaa BIP39.
- Järjestelmä transaktiomaksujen valinnan automaattista optimointia varten.



![Image](assets/fr/01.webp)



Ashigaru on siis suunnattu käyttäjille, jotka ovat tietoisia Bitcoin:n liiketoimien jäljitettävyyteen liittyvistä ongelmista. Olitpa sitten yksityisyydestä tietoinen käyttäjä, kokenut bitcoin-käyttäjä, joka on sitoutunut omavalvontaan, tai yksityishenkilö, joka on alttiina lisääntyneen valvonnan riskeille, tämä wallet-sovellus tarjoaa sinulle työkalut, joita tarvitset saadaksesi toimintasi hallinnan takaisin Bitcoin:ssa.



Ashigarusta on saatavilla mobiiliversio sen sovelluksen kautta, johon tutustumme tässä oppaassa. Sitä voidaan kuitenkin käyttää myös tietokoneella ***Ashigaru Terminal***:n avulla, jonka esittelemme tulevassa oppaassa.



![Image](assets/fr/02.webp)



Tässä opetusohjelmassa esittelen sinulle Ashigarun peruskäytön: asennuksen, yhteyden Dojoon, varmuuskopioinnin, bitcoinien vastaanottamisen ja lähettämisen. Edistyneemmät työkalut esitellään muissa niille omistetuissa opetusohjelmissa.



## 1. Ashigarun edellytykset



Sovellus vaatii muutamia ennakkoedellytyksiä toimiakseen kunnolla. Ensinnäkin se ei ole sovellus, joka on saatavilla klassisissa kaupoissa, kuten Google Play Storessa tai App Storessa. Se asentuu manuaalisesti puhelimeesi vain sen `.apk`-tiedostosta, joka on ladattavissa Tor-verkon kautta. Jos siis käytät iPhonea, tämä menetelmä ei toimi: tarvitset Android-laitteen.



Jotta voit ladata .apk-tiedoston Torin kautta, tarvitset selaimen, joka pystyy käyttämään .onion-sivustoja. Helpoin tapa on asentaa Tor Browser -sovellus puhelimeesi, joka on saatavilla [Google Play Storesta](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) tai suoraan [sen `.apk`-tiedoston kautta](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Uusimmat älypuhelimet estävät oletusarvoisesti tuntemattomista lähteistä tulevien sovellusten asennuksen. Sinun on aktivoitava tämä vaihtoehto Tor Browserille väliaikaisesti laitteen asetuksissa, jotta asennus sallitaan. Kun sovellus on asennettu, muista poistaa tämä toiminto käytöstä puhelimesi turvallisuuden vahvistamiseksi.



Toinen Ashigarun käytön olennainen edellytys on Bitcoin Dojo-solmu. Turvallisuussyistä Ashigaru-tiimi ei ylläpidä keskitettyä palvelinta, johon sovelluksesi voidaan liittää. Sinun on siis käytettävä omaa Dojo-instanssia tai muodostettava yhteys luotettuun Dojo-instanssiin.



Dojon avulla Ashigaru-sovelluksesi voi käyttää lohkoketjutietoja, tarkastella osoitteidesi saldoja ja lähettää transaktioitasi Bitcoin-verkossa.



Jos haluat tietää lisää Dojosta ja oppia asentamaan sen, pyydän sinua seuraamaan tätä opetusohjelmaa :



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Jos sinulla ei todellakaan ole varaa ylläpitää omaa Dojoa, voit löytää ihmisiä, jotka haluavat jakaa instanssinsa ilmaiseksi osoitteessa [dojobay.pw](https://www.dojobay.pw/mainnet/). Tämä voi olla väliaikainen ratkaisu, mutta pitkällä aikavälillä suosittelen käyttämään omaa Dojoa, jotta voit taata itsemääräämisoikeutesi ja luottamuksellisuutesi.



## 2. Tarkista ja asenna Ashigaru-sovellus



### 2.1. Lataa Ashigaru-sovellus



Avaa puhelimessasi Tor Browser ja siirry [Ashigarun virallisen verkkosivuston] (https://ashigaru.rs/download/) "Lataa"-osioon. Napsauta sitten `Download for Android`-painiketta ladataksesi asennustiedoston.



![Image](assets/fr/04.webp)



Ennen sovelluksen asentamista laitteeseesi tarkistamme sen aitouden ja eheyden. Tämä on erittäin tärkeä vaihe, varsinkin kun asennat sovelluksen suoraan .apk-tiedostosta.



### 2.2. Tarkista Ashigaru-sovellus



Mene takaisin [Ashigarun viralliselle verkkosivustolle] (https://ashigaru.rs/download/) `Lataus`-osioon ja kopioi sitten otsikon `SHA-256 Hash of the APK file` alla näkyvä viesti. Kopioi koko lohko, alkaen `BEGIN PGP SIGNED MESSAGE` ja päättyen `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Avaa edelleen puhelimessasi uusi välilehti Tor Browserissa ja siirry [Keybase-varmistustyökaluun](https://keybase.io/verify). Liitä juuri kopioimasi viesti sille varattuun kenttään ja napsauta sitten `Verify`-painiketta.



![Image](assets/fr/06.webp)



Jos allekirjoitus on aito, Keybase näyttää viestin, joka vahvistaa, että Ashigaru-kehittäjät ovat allekirjoittaneet tiedoston. Voit myös napsauttaa Keybasen osoittamaa `ashigarudev`-profiilia ja tarkistaa, että heidän avaimensa sormenjälki vastaa täsmälleen : `A138 06B1 FA2A 676B`.



Jos tässä vaiheessa kuitenkin ilmenee virhe, se tarkoittaa, että allekirjoitus on virheellinen. Tässä tapauksessa **en asenna APK:ta**. Aloita alusta tai pyydä yhteisöltä apua ennen jatkamista.



![Image](assets/fr/07.webp)



Keybase on toimittanut sinulle sovelluksen hashin. Tarkistamme nyt, että lataamasi .apk-tiedoston hash vastaa Keybasen tarkistamaa hashia. Tee tämä siirtymällä [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Napsauta `BROWSE...`-painiketta ja valitse vaiheessa 2.1 ladattu `.apk`-tiedosto.


Valitse sitten hash-funktio `SHA-256` ja napsauta `CALCULATE HASH` laskeaksesi tiedostosi hashin.



![Image](assets/fr/09.webp)



Sivusto näyttää .apk-tiedoston hashin. Vertaa sitä Keybase.io-sivustolla vahvistamaasi hashiin. Jos nämä kaksi hashia ovat identtiset, aitouden ja eheyden tarkistus on onnistunut. Voit nyt jatkaa sovelluksen asentamista.



![Image](assets/fr/10.webp)



### 2.3. asenna Ashigaru-sovellus



Asenna sovellus avaamalla puhelimesi tiedostonhallinta ja siirtymällä latauskansioon. Napsauta sitten äsken tarkistamaasi .apk-tiedostoa ja vahvista asennus kehotettaessa.



![Image](assets/fr/11.webp)



Ashigaru on nyt asennettu puhelimeesi.



## 3. Alusta sovellus ja luo Bitcoin-salkku



Kun käynnistät sovelluksen ensimmäistä kertaa, valitse `MAINNET`.



![Image](assets/fr/12.webp)



Napsauta sitten `Get Started`.



![Image](assets/fr/13.webp)



Luomme nyt uuden Bitcoin-salkun. Paina "Luo uusi wallet" -painiketta.



![Image](assets/fr/14.webp)



### 3.1. luo Bitcoin-salkku



Ashigaru vaatii passphrase BIP39:n. Valitse passphrase ja syötä se asianmukaisiin kenttiin. Sen on oltava mahdollisimman pitkä ja sattumanvarainen, jotta se kestää brute-force-hyökkäyksen.



Tee välittömästi fyysinen varmuuskopio tästä passphrase:stä. Tämä on erittäin tärkeä vaihe: jos kadotat puhelimesi, **jos sinulla ei enää ole tätä passphrase:tä, et voi enää käyttää Ashigaru wallet:een tallennettuja bitcoinejasi**. Tätä samaa passphrase:ää käytetään myös wallet:n palautustiedoston salaamiseen.



Jos et tiedä, mikä passphrase on, tai et täysin ymmärrä, miten se toimii, suosittelen, että luet tämän lisäoppaan. Tämä on tärkeää, koska passphrase on kriittinen osa turvallisuuttasi: sen käytön väärin ymmärtäminen voi johtaa varojen pysyvään menettämiseen.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kun olet syöttänyt passphrase:n, napsauta `NEXT`.



![Image](assets/fr/15.webp)



Valitse sitten PIN-koodi. Tätä koodia käytetään Ashigaru wallet:n lukituksen avaamiseen ja sen suojaamiseen luvattomalta fyysiseltä käytöltä. Se ei osallistu wallet:n avainten kryptografiseen johtamiseen. Tämä tarkoittaa sitä, että vaikka PIN-koodi ei olisi tiedossa, kuka tahansa, jolla on muistilausekkeesi ja passphrase, pääsee takaisin käsiksi bitcoineihisi.



Valitse pitkä, satunnainen PIN-koodi. Muista pitää varmuuskopio puhelimestasi erillään, jotta ne eivät voi vaarantua samanaikaisesti.



![Image](assets/fr/16.webp)



Kun PIN-koodi on luotu, Ashigaru näyttää wallet:n muistisanan. Varoitus: tämä lause yhdessä passphrase:n kanssa antaa täyden pääsyn bitcoineihisi. Kuka tahansa, jolla se on hallussaan, voi ottaa rahasi haltuunsa, vaikka hänellä ei olisi pääsyä puhelimeesi. Tätä 12 sanan jaksoa voidaan käyttää wallet:n palauttamiseen, jos puhelimesi katoaa, varastetaan tai rikkoutuu. Siksi on tärkeää tallentaa se äärimmäisen huolellisesti fyysiselle välineelle (paperille tai metallille).



Älä koskaan tallenna tätä lausetta digitaalisessa muodossa, tai saatat altistaa varasi varkauksille. Turvallisuusstrategiastasi riippuen voit luoda useita fyysisiä kopioita, mutta älä koskaan jaa sitä. Säilytä sanat täsmällisessä järjestyksessä ja varmista, että ne on numeroitu.



Älä koskaan säilytä muistisääntöä ja passphrase:ää samassa paikassa. Jos molemmat vaarantuisivat samanaikaisesti, hyökkääjä voisi päästä käsiksi wallet:aan.



![Image](assets/fr/17.webp)



Jos haluat lisätietoja siitä, miten muistilauseen suojaaminen onnistuu, tutustu tähän täydentävään oppaaseen :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru pyytää sinua sitten vahvistamaan passphrase:n. Käytä tämä tilaisuus hyväksenne ja tarkista, että fyysinen varmuuskopio on oikein.



![Image](assets/fr/18.webp)



### 3.2. yhdistä dojo



Seuraavaksi on vuorossa yhteyden muodostaminen Dojoon. Kuten johdannossa selitettiin, Ashigarun on oltava yhteydessä Dojoon, jotta se voi toimia Bitcoin-verkon kanssa.



Kirjaudu sisään Dojon "ylläpitotyökaluun" ja avaa `PAIRING`-valikko.



![Image](assets/fr/19.webp)



Paina Ashigarussa `Scan QR`-painiketta ja skannaa sitten DMT:n näyttämä yhteys-QR-koodi. Vahvista sitten painamalla `Jatka`.



![Image](assets/fr/20.webp)



Anna PIN-koodi avataksesi wallet:n lukituksen. Tämä vie sinut synkronointisivulle. On normaalia nähdä *PayNym*-virheitä tässä vaiheessa, koska wallet on uusi. Napsauta vain `Jatka`.



![Image](assets/fr/21.webp)



Tämän jälkeen pääset portfoliosi etusivulle.



![Image](assets/fr/22.webp)



Ennen kuin jatkat eteenpäin, suosittelen, että teet testitallennuksen, kun wallet:ssa ei vielä ole bitcoineja. Näin voit tarkistaa, että paperiset varmuuskopiot toimivat oikein. Saat selville, miten se onnistuu, seuraamalla tätä ohjetta:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Ashigaru-sovelluksen määrittäminen



Pääset sovelluksen asetuksiin napsauttamalla vasemmassa yläkulmassa olevaa *PayNymin* kuvaa ja valitsemalla sitten "Asetukset".



![Image](assets/fr/23.webp)



Täältä löydät useita vaihtoehtoja, joilla voit mukauttaa Ashigarun toiminnan tarpeisiisi. Suosittelen kuitenkin vahvasti, että aktivoit kaksi tärkeää parametria heti alusta alkaen.



Aloita avaamalla `Turvallisuus > Piilotustila`-valikko ja aktivoi sitten tämä ominaisuus, jos tarvitset sitä. Se piilottaa Ashigaru-sovelluksen puhelimeen asennetun tavallisen sovelluksen nimen, logon ja käyttöliittymän taakse. Tarkoituksena on estää ketään tunnistamasta Ashigarua, jos puhelimesi tarkastetaan fyysisesti.



![Image](assets/fr/24.webp)



Jokaisella tarjolla olevalla väärennetyllä sovelluksella on oma menetelmänsä aidon Ashigaru-käyttöliittymän avaamiseksi. Jos esimerkiksi valitset laskimen, Ashigaru-sovellus katoaa aloitusnäytöltä ja tilalle tulee väärennetty laskin. Kun avaat sen, näet klassisen toimivan laskimen käyttöliittymän, mutta Ashigarun käyttämiseksi sinun tarvitsee vain napauttaa `=`-symbolia viisi kertaa nopeasti.



Toinen tärkeä aktivoitava parametri on [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Tämän vaihtoehdon avulla voit korottaa tapahtuman kustannuksia, jos se juuttuu mempoolitilaan, koska kustannukset ovat liian alhaiset. Voit ottaa sen käyttöön valikosta `Transaktiot > Kuluta käyttäen RBF`.



![Image](assets/fr/25.webp)



Vihje: Voit vaihtaa salkkusi näyttöyksikön `BTC`:stä `sat`:ksi klikkaamalla etusivulla näkyvää kokonaissaldoa.



## 5. Vastaanottaa bitcoins on Ashigaru



Nyt kun salkkusi on toiminnassa, voit vastaanottaa satss. Voit tehdä sen painamalla käyttöliittymän oikeassa alakulmassa olevaa `+`-painiketta ja sitten vihreää `Vastaanota`-painiketta.



![Image](assets/fr/26.webp)



Ashigaru näyttää sitten wallet:n ensimmäisen käyttämättömän vastaanottavan osoitteen, jotta osoitteen uudelleenkäyttö estetään (osoitteen uudelleenkäyttö on erittäin huono käytäntö yksityisyyden kannalta). Voit sitten välittää tämän osoitteen henkilölle tai palvelulle, jonka on lähetettävä sinulle bitcoineja.



![Image](assets/fr/27.webp)



Kun tapahtuma on lähetetty verkkoon, se näkyy automaattisesti sovelluksen etusivulla.



![Image](assets/fr/28.webp)



## 6. Lähetä bitcoineja Ashigarun kanssa



Nyt kun sinulla on bitcoineja Ashigaru wallet:ssäsi, voit myös lähettää niitä. Tee se painamalla `+`-painiketta oikeassa alakulmassa ja valitsemalla sitten punainen `lähettää`-painike.



![Image](assets/fr/29.webp)



Valitse sitten tili, jolta haluat tehdä menon. Tällä hetkellä emme ole vielä käsitelleet "Postmix"-tiliä, joka on varattu kolikkoliitoksia varten ja jota tarkastelemme myöhemmässä opetusohjelmassa. Lähetämme siis varoja päätalletustililtä.



![Image](assets/fr/30.webp)



Anna tapahtuman tiedot: lähetettävä summa ja vastaanottajan Bitcoin-osoite.



![Image](assets/fr/31.webp)



Klikkaamalla kolmea pientä pistettä oikeassa yläkulmassa ja sitten `Näytä käyttämättömät tuotokset` voit myös valita tarkalleen, mitkä UTXO:t haluat käyttää, jotta yksityisyytesi paranisi.



![Image](assets/fr/32.webp)



Kun olet täyttänyt kaikki tiedot, jatka klikkaamalla käyttöliittymän alareunassa olevaa valkoista nuolta.



Tämän jälkeen pääset yhteenvetosivulle, jossa näkyvät kaikki maksutapahtuman yksityiskohdat. Näytössä on useita tärkeitä elementtejä:




- Tarkista vielä kerran lohkossa `Kohde`, että vastaanottajan osoite ja lähetettävä summa ovat oikein;
- Maksut -lohkossa voit tarkastella Ashigarun automaattisesti valitsemaa maksua ja tarvittaessa muuttaa sitä klikkaamalla `MANAGE` ;
- Lohko `Transaction` osoittaa, minkä tyyppistä transaktiota olet suorittamassa. Tässä puhumme yksinkertaisesta transaktiosta, mutta Ashigaru tukee myös muunlaisia yksityisyydensuojaan optimoituja transaktioita, joita käsittelemme yksityiskohtaisesti tulevassa opetusohjelmassa;
- Punainen "Transaktiohälytys"-lohko varoittaa sinua, jos tapahtumassasi on havaittavissa ketjuanalyysityökalujen tunnistamia malleja, jotka voivat vaarantaa yksityisyytesi. Klikkaamalla sitä voit tarkastella yksityiskohtia. Esimerkiksi minun tapauksessani Ashigaru kertoo, että lähetetty summa on pyöreä (`3000 sats`), jolloin voin päätellä, kumpi tuloste vastaa kuluja ja kumpi vaihtoa. Jos haluat lisätietoja näistä ketjuanalyysin heuristiikoista, kutsun sinut seuraamaan BTC 204 -koulutustani Plan ₿ Academyssa ;
- Lopuksi voit lisätä tapahtumaan tarran, jotta voit pitää kirjaa sen tarkoituksesta.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kun olet tarkistanut kaikki tiedot, lähetä bitcoinit vihreällä nuolella. Pidä nuoli alhaalla ja vedä sitä sitten oikealle vahvistaaksesi lähetyksen.



![Image](assets/fr/33.webp)



Tapahtumasi on lähetetty Bitcoin-verkkoon.



![Image](assets/fr/34.webp)



## 7. Ashigaru wallet:n palauttaminen



Ashigaru wallet:n talteenotto eroaa hieman klassisen Bitcoin wallet:n talteenotosta, sillä siinä käytetään samoja menetelmiä kuin Samurai Wallet:ssä. Jos menetät pääsyn wallet:een (joko siksi, että olet unohtanut PIN-koodisi, poistanut sen asennuksen tai kadottanut puhelimesi), bitcoinien palauttamiseen on useita tapoja.



Jos sinulla on vielä pääsy puhelimeesi tai jos olet tehnyt varmuuskopion tästä tiedostosta, yksinkertaisin tapa on käyttää varmuuskopiotiedostoa `ashigaru.txt`. Tämä tiedosto sisältää kaikki tiedot, joita tarvitset salkkusi palauttamiseen uudessa Ashigaru-instanssissa (tai Sparrow Wallet:ssä), mutta se on salattu passphrase:lla, jonka määrittelit tämän ohjeen vaiheessa 3.1. Tämän vuoksi sinulla on oltava sekä `ashigaru.txt`-tiedosto että passphrase, jotta voit käyttää tätä menetelmää.



Näiden kahden elementin avulla voit esimerkiksi palauttaa salkkusi Sparrow Wallet:ään.



![Image](assets/fr/35.webp)



Jos sinulla ei ole pääsyä `ashigaru.txt`-tiedostoon, voit silti saada rahasi takaisin passphrase-muistilauseen avulla, aivan kuten minkä tahansa muun Bitcoin-salkun kohdalla. Suosittelen, että teet tämän palautuksen joko uudella Ashigaru-instanssilla tai suoraan Sparrow Wallet:lla, jotta voit helposti palauttaa Whirlpool:n ohituspolut, jos käytit sitä. Vaihtoehtoisesti voit tuoda nämä tiedot mihin tahansa muuhun BIP39-yhteensopivaan ohjelmistoon syöttämällä johdatuspolut manuaalisesti.



Jos haluat lisätietoja tästä prosessista, tutustu täydelliseen oppaaseen, jonka olen kirjoittanut Wallet Samurai wallet:n palauttamisesta. Koska Ashigaru on fork, menettely on identtinen:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Kuten huomaat, passphrase on välttämätön, käytitpä mitä tahansa kunnostusmenetelmää. Muista siis varmistaa se huolellisesti. Voit myös tehdä useita kopioita, riippuen turvallisuusstrategiastasi.



## 8. Päivitä sovellus



Koska asensit Ashigaru-sovelluksen .apk-tiedostosta etkä Play Storen kautta kuten tavallisen sovelluksen, sinun on ladattava päivitettyä versiota vastaava uusi .apk-tiedosto ja asennettava se sitten manuaalisesti.



Toista tämän ohjeen osassa 2 kuvatut vaiheet, paitsi että kun napsautat .apk-tiedostoa käynnistääksesi asennuksen, **Android-puhelimesi pitäisi tarjota sinulle `Update`-vaihtoehtoa, ei `Install`**.



![Image](assets/fr/41.webp)



Tämä on erittäin tärkeä asia: jos Android näyttää `Install` eikä `Update`, olet todennäköisesti asentamassa väärennettyä versiota. Keskeytä asennusprosessi tässä tapauksessa välittömästi.



Kuten ensimmäisen asennuksen yhteydessä, tarkista .apk-tiedoston aitous ja eheys ennen päivityksen aloittamista.



Saat tietää, milloin uusi versio on saatavilla, tarkistamalla Ashigarun virallisilta verkkosivuilta aika ajoin. Voit olla varma, että Ashigaru on vakaa, kypsä sovellus, joka on periytynyt Samourai Wallet:stä, ja päivitykset ovat suhteellisen harvinaisia verrattuna nuorempiin ohjelmistoihin.



## 9. Lahjoita Ashigaru-hankkeelle



Ashigaru on avoimen lähdekoodin projekti. Jos haluat tukea sen kehittämistä, voit tehdä lahjoituksen suoraan sovelluksesta PayNymin kautta.



Napsauta tätä varten PayNymiäsi käyttöliittymän oikeassa yläkulmassa ja valitse sitten maksukoodisi, joka alkaa kirjaimella `PM...`.



![Image](assets/fr/36.webp)



Paina sitten näytön oikeassa alareunassa olevaa "+"-painiketta.



![Image](assets/fr/37.webp)



Valitse vastaanottajaksi `Ashigaru Open Source Project`.



![Image](assets/fr/38.webp)



Napsauta `CONNECT`-painiketta BIP47-viestintäkanavan luomiseksi (lisätietoja tästä protokollasta alla olevassa ohjeessa).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Kun ilmoitustapahtuma on vahvistettu, voit lähettää lahjoituksesi projektille napsauttamalla käyttöliittymän oikeassa yläkulmassa olevaa pientä valkoista nuolta.



![Image](assets/fr/40.webp)



Osaat nyt käyttää Ashigaru-sovelluksen perusominaisuuksia. Tulevissa opetusohjelmissa tarkastelemme, miten voit hyödyntää kehittyneitä kulutustapahtumia sekä Whirlpool:a, Samurai Wallet:stä periytyvää coinjoin-toteutusta.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
