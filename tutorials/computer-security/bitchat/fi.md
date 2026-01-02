---
name: Bitchat
description: Hajautettu, Internet-vapaa viestinvälitys vapaata viestintää varten
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Tämä BTC Sessionsin opetusvideo opastaa sinua Bitchat!*:n perustamisessa ja käytössä


Bitchat syntyi nopean prototyyppien kehittämisen tuloksena, kun [@jack](https://primal.net/jack) kehitti alkuperäisen konseptin viikonlopun koodausistunnon aikana. [@calle](https://primal.net/calle) liittyi projektiin pian sen jälkeen kehittämään Android-toteutusta. Jack johtaa tällä hetkellä iOS-version kehittämistä, kun taas calle valvoo Android-versiota monien muiden osallistujien tuella.


## Johdanto: Chat vapaasti, ilman verkkoa


Kuvittele, että voit lähettää viestejä, kun internet ei toimi, luonnonkatastrofin aikana tai paikoissa, joissa viestintä on rajoitettua. Bitchat tekee tämän mahdolliseksi. Se on hajautettu, vertaisverkkoviestisovellus, joka ohittaa keskitetyt palvelimet ja antaa laitteiden keskustella suoraan keskenään täysin offline-tilassa Bluetoothin ja mesh-verkon avulla. Bitchat on suunniteltu yksityisyyden suojaa ja häiriönsietokykyä silmällä pitäen, ja se soveltuu erinomaisesti käytettäväksi alueilla, joilla perinteiset yhteydet ovat epäluotettavia tai niitä ei ole saatavilla - esimerkiksi katastrofien aikana, syrjäisissä paikoissa tai niille, jotka haluavat välttää valvontaa. Bitchat käyttää salausta varmistaakseen, että jokainen viesti on päästä päähän salattu, todennettu ja väärentämisen kestävä.


Tässä ohjeessa näytämme, miten Bitchat toimii ja miten voit käyttää sitä todella yksityiseen, offline-valmiiseen viestintään.


## 🚀 Tärkeimmät ominaisuudet


Bitchat mahdollistaa offline-viestien lähettämisen näiden [ominaisuuksien] avulla (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Ristiinalaisyhteensopiva**: Täysi yhteensopivuus iOS:n ja Androidin välillä.
- Hajautettu verkko**: Automaattinen vertaisten löytäminen ja monisatamaviestien välittäminen Bluetooth Low Energy (BLE) -verkossa
- End-to-End-salaus**: X25519-avainten vaihto + AES-256-GCM yksityisviestejä varten
- Kanavapohjaiset keskustelut**: Aihekohtainen ryhmäviestintä valinnaisella salasanasuojauksella
- Store & Forward**: 
- Yksityisyys ensin**: Ei tilejä, ei puhelinnumeroita, ei pysyviä tunnisteita
- IRC-tyyliset komennot: Tuttu `/join, /msg, /who` -tyylinen käyttöliittymä.
- Viestien säilyttäminen**: Valinnainen kanavanlaajuinen viestien tallennus, jota kanavan omistajat hallitsevat
- Hätäpyyhintä**: Tyhjennä kaikki tiedot välittömästi napauttamalla logoa kolmesti
- Moderni Android-käyttöliittymä**: Material Design 3:lla Jetpack Compose: Jetpack Compose with Material Design 3
- Tumma/vaalea Teemat**: Terminaalin inspiroima estetiikka, joka vastaa iOS-versiota
- Akun optimointi**: Mukautuva skannaus ja virranhallinta


## 1️⃣ Kuinka Bitchat toimii - yksinkertaisesti


Bitchatin avulla voit lähettää viestejä lähistöllä oleviin puhelimiin suoraan Bluetoothin kautta (`BLE`, kuten seuraavassa), eikä internet- tai matkapuhelinsignaalia tarvita. Kun aloitat keskustelun, puhelimet suorittavat suojatun kädenpuristuksen luodakseen ainutlaatuisen, väliaikaisen salausavaimen keskustelua varten. Jokainen viesti suojataan päästä päähän -salauksella, ja jokaiseen viestiin käytetään uutta avainta, jotta aiemmat viestit pysyvät turvassa, vaikka puhelimesi vaarantuisi myöhemmin. Lopuksi sovellus jakaa viestit pieniin osiin ja sekoittaa ne satunnaiseen tekaistuun dataan, jotta viestitoimintasi voidaan piilottaa. Suorissa laitteiden välisissä keskusteluissa se toimii vain ~100 metrin etäisyydellä. Se on kuin salattujen muistiinpanojen välittämistä tungoksessa - laitteet kuiskaavat suoraan toisilleen ja silppuavat avaimet jokaisen viestin jälkeen.


Bitchatin avulla voit myös liittyä sijaintiin perustuviin keskusteluhuoneisiin Nostr-protokollan ja `#geohashes` -tekstin avulla. Geohash on lyhyt koodi, kuten `#u33d`, joka edustaa tiettyä maantieteellistä aluetta yksittäisestä naapurustosta aina kokonaiseen kaupunkiin tai alueeseen asti. Voit `teleportoida` mihin tahansa geohash-keskusteluhuoneeseen ympäri maailmaa yksinkertaisesti syöttämällä sen tunnisteen. Viestisi lähetetään hajautetun releiden verkon kautta, joka suojaa tarkan sijaintisi. Lisäksi aina kun liityt geohash-huoneeseen, sinulle annetaan uusi, väliaikainen henkilöllisyys, mikä lisää yksityisyyden suojaa sijaintiin perustuviin keskusteluihisi.


Tarkempia teknisiä yksityiskohtia on [virallisessa Whitepaperissa] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Asennus ja asennus


### Mistä saada Bitchat


Voit asentaa Bitchatin kautta:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (iOS-laitteille)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (Android-laitteille)


Android-käyttäjillä on myös vaihtoehtoisia vaihtoehtoja:



- Lataa APK suoraan [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) -sivulta tai
- Asenna Nostr-yhteensopivan [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr) kautta


![image](assets/en/01.webp)


**Huomautus**: tämä opetusohjelma keskittyy ensisijaisesti Android-toteutukseen. IOS-versio saattaa poiketa siitä._


### Asennusprosessi


Asennuksen jälkeen avaa Bitchat ja näet tämän alkuperäisen käyttöoikeusnäytön. Sinun on tehtävä näin:


1. **Varaa nämä tarvittavat oikeudet:**


   - Bluetooth-yhteys** (löytää lähellä olevat Bitchat-käyttäjät)
   - Tarkka sijainti** (Android vaatii tämän Bluetooth-toiminnallisuuden vuoksi)
   - Ilmoitukset** (yksityisviestien vastaanottaminen)

2. **Poista akun optimointi käytöstä**:


   - Näin Bitchat voi toimia taustalla
   - Ylläpitää mesh-verkkoyhteyksiä jatkuvasti


Siirry seuraavaan näyttöön napauttamalla `Lupien myöntäminen`, noudata `Prompts` ja `Poista akun optimointi käytöstä`.


![image](assets/en/02.webp)


Tervetuloa Bitchatin päänäytölle. Aloitetaan suunnistaminen:


### Asetukset


Tärkeimmät asiat ensin. Asetukset-valikko avataan napauttamalla `Bitchat-logoa`.  Käytettävissä ovat seuraavat vaihtoehdot:



- Aseta "ulkonäkö" (järjestelmä/valo/tumma).
- ota käyttöön `Proof of work` geohashille roskapostin estämiseksi (valinnainen)
- Ota käyttöön `Tor` yksityisyyden parantamiseksi.


![image](assets/en/16.webp)


### Määritä identiteettisi


Valitse käyttäjätunnuksesi napauttamalla yläreunan `bitchat/anonXXXXXX`-kenttää. Näin muut näkevät sinut sekä Bluetooth- että Internet-tilassa. Voit esimerkiksi vaihtaa käyttäjänimen "anon2022" haluamaasi käyttäjänimeen.


![image](assets/en/03.webp)


### Valitse verkkokanavat


Vaihda yhteystyyppien välillä valikosta `#sijaintikanavat` (käyttäjätunnuksen oikealla puolella):



- BLE Mesh***: Oletus Bluetooth-tila (ei internetiä, 10-50 metrin kantama)
- #geohashes**: Internet-yhteensopivat maantieteelliset yhteisöt, jotka käyttävät [Nostr-protokollaa](https://nostr.com/)


Kun valitset `#geohashes`-tilan, Bitchat integroituu Nostr-protokollaan ja mahdollistaa maantieteelliset yhteisöt. Viestisi julkaistaan Bitchatin vertaisverkon sijasta "hajautettuihin Nostr-välityspisteisiin", mikä mahdollistaa laajemmat, mutta sijainnin mukaan suodatetut keskustelut. Bitchatin identiteettiavaimet allekirjoittavat kryptografisesti kaikki Nostr-tapahtumat autentikoinnin ylläpitämiseksi, ja geohash-tunnisteet (kuten `#u4pruyd` naapurustoa varten) suodattavat viestit valitsemallesi tarkkuustasolle. Tämä tarkoittaa, että voit osallistua paikallisiin keskusteluihin paljastamatta tarkkoja koordinaatteja, vaikka internetyhteys vaaditaankin.


![image](assets/en/04.webp)


### Seuraa vertaisia

lupa: CC-BY-SA-V4

Vertaislaskurissa näkyvät käyttäjät:



- Lähellä (BLE Mesh) tai
- Geohash-alueellasi (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Global Chat & yksityisviestit


Bitchat tarjoaa kaksi erilaista viestintätilaa eri tarpeisiin:



- Julkiset kanavat:** Avoimiin keskusteluihin muiden kanssa. Voit muodostaa yhteyden joko paikallisen BLE mesh -verkon kautta lähellä oleville käyttäjille tai maailmanlaajuisen #geohashin kautta internet-yhteensopiville, sijaintiin perustuville yhteisöille.
- Yksityisviestit:** Turvallisia, kahdenkeskisiä keskusteluja varten. Nämä luovat suoran, salatun yhteyden, jotta keskustelusi pysyvät luottamuksellisina.


Molempien tilojen ymmärtäminen auttaa sinua navigoimaan keskusteluissa.


### Julkiset kanavat: Yhteisön keskus


Sijaintikanavat-valikko (oikeassa yläkulmassa) säätelee julkista näkyvyyttäsi. Valitsemalla `mesh` saat yhteyden kaikkiin lähistöllä oleviin käyttäjiin BLE-verkon kautta, tyypillisesti 10-50 metrin säteellä oleviin laitteisiin. Tämä luo avoimen foorumin, jossa viestit lähetetään kaikille kantaman sisällä oleville, mikä on ihanteellista tapahtumailmoituksia tai paikallisia hälytyksiä varten.


Jos haluat laajemman maantieteellisen kattavuuden, voit liittyä internetin verkkoyhteisöihin, jotka on suodatettu sijainnin mukaan, valitsemalla minkä tahansa `#geohash`-tunnisteen. Nämä kanavat käyttävät Nostr-protokollan releitä, jotka mahdollistavat viestinnän yli kaupunkien tai alueiden rajojen ja säilyttävät samalla paikkaperusteisen relevanssin. Viestisi näkyvät suorassa lähetyksessä muille samassa kanavassa oleville, ja uudet osallistujat näkevät automaattisesti viimeisimmät viestit liittyessään.


![image](assets/en/06.webp)


### Yksityiset keskustelut: Salatut keskustelut: Turvallinen ja salattu


Voit aloittaa yksityisen keskustelun napauttamalla suoraan mitä tahansa käyttäjänimeä, joka näkyy "Vertaisten yleiskatsauksessa". Voit myös napauttaa tähti-kuvaketta merkitäksesi käyttäjän suosikiksi, jolloin hän pysyy näkyvissä yhteystietoluettelossasi, vaikka hän olisi offline-tilassa.


![image](assets/en/07.webp)


Bitchat aloittaa automaattisesti "turvakättelyn", kun aloitat yksityisen keskustelun. Laitteet vaihtavat hetkellisiä avaimia luodakseen salatun tunnelin nimenomaan keskustelua varten. Tämä prosessi varmistaa, että kaikki viestisi ja jaetut tiedostot pysyvät luottamuksellisina jatkuvan päästä päähän -salauksen ansiosta. Yksityiset viestit tukevat tekstin ja tiedostojen jakamista.


![image](assets/en/08.webp)


## 4️⃣ Lisäominaisuudet


Pääset toimintopaneeliin välittömästi kirjoittamalla `/` missä tahansa Bitchatissa. Tämä paljastaa komentovalikon pikatoimintoja varten.



- Yhteyksien hallinta**: `Blokkaa käyttäjät` tai `Poista vertaisvertaisvertaisvertaisvertaiset`
- Kanavasäätimet**: näytä kanavat" tai "Liity/luo kanava"
- Sosiaalinen vuorovaikutus**: lämmin halaus" tai "läpsäisy taimenella" 🎣
- Chatin ylläpito**: `Tyhjennä chat-viestit`
- Yksityisyydensuojatyökalut**: "Katso kuka on verkossa" tai "Lähetä yksityisviesti"


Komennot suoritetaan välittömästi - kuten `/block Satoshi` kriitikoiden hiljentämiseksi tai `/hug Hal` positiivisuuden levittämiseksi 🫂.


![image](assets/en/09.webp)


## 5️⃣ Kanavan luominen


Bitchatin kanavat mahdollistavat organisoidun viestinnän aiheiden, paikkojen tai yhteisöjen ympärille. Voit luoda oman kanavasi noudattamalla tätä työnkulkua:


### Vaihe 1: Luo kanava


Voit luoda kanavan kirjoittamalla `/j` tai `/join` ja sen jälkeen `kanavan nimi` missä tahansa chatissa (esim. `/j <kanavan nimi>`). Luomisen jälkeen näkyviin tulee uusi `ikoni ⧉`, joka osoittaa uuden kanavan. Muut käyttäjät voivat liittyä kirjoittamalla saman komennon (esim. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Vaihe 2: Määritä asetukset


Oletuskomentojen lisäksi kanavalla on käytettävissä seuraavat asetukset:



- `/save` tallentaa viestit paikallisesti
- `/transfer` kanavan omistuksen siirtämiseksi ja
- `/pass` vaihtaaksesi kanavan salasanan.


Yksityisissä yhteisöissä tämä komento ottaa käyttöön salasanasuojauksen, jolloin hyväksyttyjen jäsenten on syötettävä mukautettu salasana ennen liittymistä.


## 6️⃣ Paniikkitila


Puhutaanpa nyt tästä "paniikkitilasta": "Bitchat-logon" kolminkertainen napauttaminen käynnistää sovelluksen kaikkien paikallisten viestien ja tietojen täydellisen pyyhkimisen. Tämä on äärimmäinen yksityisyydensuojasi, täydellinen tilanteisiin, jotka vaativat välitöntä hienotunteisuutta.


**Tärkeä muistutus:** _Paniikkitila on pysyvä. Kerran aktivoituja tietoja ei voi palauttaa. Käytä varoen._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash-kanavat mahdollistavat kohdennetut keskustelut, jotka perustuvat "maantieteellisiin sijainteihin" perinteisten verkkoyhteyksien sijaan. Tämä ominaisuus muuttaa bitchatin sijaintitietoiseksi viestintävälineeksi, joka on ihanteellinen paikalliseen koordinointiin, yhteisön rakentamiseen ja paikkakuntakohtaisiin keskusteluihin.


### Miten `#geohashes` toimii


Järjestelmä jakaa maailman ruudukkoon käyttäen [Geohash-järjestelmää] (https://en.wikipedia.org/wiki/Geohash), jossa jokainen merkki hashissa edustaa suurempaa tarkkuutta:



- Taso 4** (esim. `u33d`): Kattaa noin 25 km × 25 km - ihanteellinen koko kaupungin laajuisiin keskusteluihin
- Taso 6** (esim. `u33d8z`): Kattaa noin 1,2 km × 1,2 km - naapuruston tarkkuus
- Taso 8** (esim. `u33d8z1k`): Kattavat noin 150 m × 150 m - kadun osittainen tarkkuus


Tarkkuusvalinta tasapainottaa yksityisyyden ja hyödyllisyyden: korkeammat tasot luovat suljetumpia alueita, mutta paljastavat sijaintisi tarkemmin.


### Liittyminen `#geohash`-kanaviin


1. Siirry `#sijaintikanavat`-valikkoon.

2. Valitse haluamasi tarkkuustaso ja syötä `#geohash` (esim. #u33d)

3. Napauta `Teleport`-painiketta liittyäksesi `#paikannuskanavaan`.


![image](assets/en/12.webp)


Vaihtoehtoisesti voit määrittää tarkkuustason karttanäkymän avulla napauttamalla karttakuvaketta ja liittyä "sijaintikanavaan" napauttamalla "valitse".


![image](assets/en/13.webp)


**Tärkeä muistutus**: _#geohash-toiminnot edellyttävät aktiivista internet-yhteyttä - toisin kuin BLE mesh, joka toimii offline-tilassa Bluetoothin kautta._


## 8️⃣ Heatmaps


Heatmaps ovat siisti tapa löytää Bitchat-tapahtumia ja -kanavia ympäri maailmaa. [Bitmap](https://bitmap.lat/) visualisoi ja seuraa anonyymeja, sijaintiin perustuvia viestejä Nostr-verkossa ja näyttää hetkelliset Nostr-tapahtumat. Tutustu ja liity paikkakuntakohtaisiin kanaviin ja keskusteluihin.


![image](assets/en/15.webp)


## 🎯 Päätelmät


Bitchat mahdollistaa turvallisen, hajautetun viestinnän tilanteissa, joissa perinteinen viestinvälitys epäonnistuu. Se pystyy toimimaan ilman internetinfrastruktuuria BLE mesh -verkon avulla, joten se soveltuu mielenosoituksiin, katastrofialueille ja syrjäisille alueille, joilla yhteydet ovat rajalliset tai sensuroidut. Sovellus varmistaa yksityisyyden ephemeral key -salauksella, geohash-pohjaisilla sijaintikanavilla ja paniikkitilassa tapahtuvalla tietojen poistamisella.


Sovellus on vielä alkuvaiheessa, mutta se on jo nyt lupaava. Käyttäjien on odotettava satunnaisia virheitä ja raportoitava ongelmista [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) kautta. Parannuksia on suunnitteilla, mukaan lukien `ecash`-integraatio yksityisiä sovelluksen sisäisiä transaktioita varten Cashu-protokollaa käyttäen.


![image](assets/en/14.webp)


## 📚 Bitchat Resources


[Github](https://github.com/permissionlesstech) | [Verkkosivusto ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)