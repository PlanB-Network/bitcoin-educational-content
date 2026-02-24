---
name: Blitz Wallet
description: Yksinkertaisin Bitcoin-lompakko.
---

![cover](assets/cover.webp)

Käyttökokemus on yksi ratkaisevista tekijöistä Bitcoin-lompakon valinnassa. Tässä oppaassa esittelemme Blitz Walletin, lompakon, joka asettaa yksinkertaisuuden lähestymistapansa keskiöön: **Spark**-protokollan integroinnin ansiosta Blitz tarjoaa yhden markkinoiden yksinkertaisimmista ja kattavimmista Bitcoin-lompakoista, välittömillä maksuilla ja ilman teknistä hallinnointia.

## Mikä on Blitz Wallet?

Blitz Wallet on **self-custodial** ja **open source** Bitcoin-lompakko, joka panostaa itsemääräämisoikeuteesi sekä sujuvaan ja intuitiiviseen käyttökokemukseen.

[Blitz Wallet](https://blitz-wallet.com/) on mobiilisovellus, joka on saatavilla Androidille (Play Store) ja iOS:lle (App Store).

Toisin kuin perinteiset Lightning-lompakot, jotka edellyttävät maksukanavien ja saapuvan likviditeetin hallintaa, Blitz Wallet nojaa **Spark-protokollaan** näiden teknisten monimutkaisuuksien poistamiseksi. Tulos: välittömät maksut heti ensimmäisestä vastaanotetusta satoshista alkaen, ilman mitään ennakkoasetuksia. Blitzin tavoitteena on tehdä bitcoin-maksut yhtä helpoiksi kuin tavallisessa maksusovelluksessa, tinkimättä koskaan varojesi self-custodysta.

Blitz Wallet tukee myös **luettavia osoitteita** muodossa `käyttäjä@verkkotunnus.com` (LNURL:n kautta), mikä mahdollistaa bitcoinien lähettämisen yhtä helposti kuin sähköpostin, ilman että jokaisessa tapahtumassa tarvitsee käsitellä pitkiä invoice-merkkijonoja tai QR code -koodeja.

## Spark-protokollan ymmärtäminen

Ennen käytännön osuutta on hyödyllistä ymmärtää teknologia, joka toimii Blitz Walletin taustalla: **Spark-protokolla**.

### Mikä on Spark?

Spark on open source -ylimääräinen kerrosprotokolla, joka on rakennettu Bitcoinin päälle ja jonka on kehittänyt Lightspark-tiimi. Se mahdollistaa välittömät ja edulliset tapahtumat säilyttäen samalla bitcoiniesi self-custodyn.

Toisin kuin Lightning Network, joka perustuu kahden osapuolen välisten **maksukanavien** käyttöön, Spark hyödyntää teknologiaa nimeltä **statechain** (tilaketju). Perusperiaate on seuraava: sen sijaan, että bitcoineja siirrettäisiin lohkoketjussa jokaisen tapahtuman yhteydessä, Spark siirtää **käyttöoikeuden** käyttäjältä toiselle ilman on-chain-siirtoa.

### Miten se toimii?

Ymmärtääksemme Sparkia intuitiivisesti, kuvitellaan että bitcoinin käyttäminen Sparkissa edellyttää kahden palan palapelin kokoamista:
- Yksi pala on käyttäjän hallussa (esimerkiksi Alicella).
- Toinen pala on operaattoriryhmän hallussa, jota kutsutaan nimellä **Spark Entity (SE)**.

Vain kahden vastaavan palan yhdistelmä mahdollistaa bitcoinien käyttämisen.

Kun Alice haluaa lähettää bitcoininsa Bobille, tapahtuu seuraavaa: uusi palapeli luodaan yhteisesti Bobin ja SE:n välille. Palapeli säilyttää saman muodon, mutta sen palat vaihtuvat. Nyt Bobin pala vastaa SE:n palaa. Alicen vanha pala muuttuu käyttökelvottomaksi, koska SE on tuhonnut sitä vastaavan palansa. Bitcoinien omistajuus on vaihtunut **ilman mitään lohkoketjutapahtumaa**.

Bob voi sitten toistaa saman prosessin lähettääkseen nämä bitcoinit Carolille, ja niin edelleen. Jokainen siirto toimii palapelin palojen vaihtamisella, ei varojen on-chain-siirtämisellä.

### Miksi se on turvallinen?

Oikeutettu kysymys herää: mitä tapahtuu, jos SE ei oikeasti tuhoa vanhaa palaansa?

Spark Entity ei ole yksittäinen toimija: se on ryhmä riippumattomia operaattoreita. SE:n palaa ei koskaan hallinnoi yksittäinen operaattori. Palapelin vaihtaminen edellyttää useiden operaattorien yhteistyötä. Riittää, että **yksi ainoa operaattori on rehellinen** siirron aikana, jotta vanhan palapelin uudelleenaktivointi estyy. Yksikään yksittäinen operaattori ei voi salaa säilyttää vanhaa aktiivista palapeliä tai luoda sitä uudelleen myöhemmin.

Lisäksi Spark sisältää yksipuolisen poistumismekanismin: voit aina noutaa bitcoinisi on-chain ilman SE:n yhteistyötä. Tämä varahallintamekanismi on olennainen osa Sparkin arkkitehtuuria ja takaa, ettet ole koskaan riippuvainen verkosta päästäksesi varoihisi.

### Spark vs Lightning Network

Spark ja Lightning eivät kilpaile keskenään: ne ovat **toisiaan täydentäviä**. Blitz Wallet integroi molemmat, mikä mahdollistaa molempien etujen hyödyntämisen.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Teknologia**                | Statechains (tilaketjut)     | Maksukanavat          |
| **Kanavien hallinta**         | Ei vaadita                   | Vaaditaan             |
| **Saapuva likviditeetti**     | Ei vaadita                   | Vaaditaan             |
| **Välittömät tapahtumat**     | Kyllä                        | Kyllä                 |
| **Self-custody**              | Kyllä                        | Kyllä                 |
| **Lightning-yhteensopivuus**  | Kyllä (atomic swaps -tekniikalla) | Natiivi          |

Lightning Network on edelleen erinomainen protokolla välittömiin maksuihin, mutta se asettaa teknisiä rajoitteita (kanavien hallinta, saapuva likviditeetti, solmun oltava verkossa...), jotka voivat hidastaa aloittelijoita. Spark poistaa nämä rajoitteet säilyttäen samalla Lightning-yhteensopivuuden.

## Asennus ja määritykset

Tässä oppaassa käytämme Blitz Walletin Android-versiota, mutta kaikki alla esitetyt prosessit pätevät myös iOS:lla.

![installation](assets/fr/01.webp)

Koska Blitz Wallet on self-custody-lompakko, voit valita **uuden lompakon luomisen** tai **palautuslauseen tuomisen** (12 tai 24 sanaa) olemassa olevasta lompakosta.

Tässä luomme uuden lompakon. Alta löydät suosituksemme palautuslauseen varmuuskopiointiin:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **TÄRKEÄÄ** : Nämä 12 tai 24 palautussanaa ovat **ainoa avain bitcoineihisi**. Blitz on self-custodial-lompakko: Blitzillä eikä Sparkilla ole pääsyä palautuslauseeseesi eikä varoihisi. Jos kadotat nämä sanat, menetät lopullisesti pääsyn bitcoineihisi. Älä jaa niitä kenellekään: kuka tahansa, jolla ne ovat hallussaan, voi käyttää bitcoinejasi.

Luo seuraavaksi **PIN**-koodi lompakon pääsyn suojaamiseksi.

![setup-wallet](assets/fr/02.webp)

## Blitzin käytön aloittaminen

Tapahtumien suorittaminen Blitzillä on intuitiivisempaa kuin useimmissa muissa Bitcoin-lompakoissa. Käyttöliittymä on minimalistinen ja keskittyy kolmeen päätoimintoon: lähettäminen, skannaaminen ja vastaanottaminen.

### Bitcoinien vastaanottaminen

Vastaanottaaksesi bitcoineja Blitz-lompakkoosi, napsauta **"Nuoli alas"** -kuvaketta (↓), syötä satosheina määrä jonka haluat vastaanottaa, lisää valinnainen kuvaus, ja lompakko luo laskun (invoice), jonka voit jakaa lähettäjällesi.

⚠️ **HUOMAUTUS** : Satoshi (tai "sat") on bitcoinin pienin yksikkö: **1 bitcoin = 100 000 000 satoshia**.

Yksi Blitz Walletin erityispiirteistä on, että se tukee useita Bitcoin-ekosysteemin verkkoja ja protokollia:

- **Lightning Network** : Yksi Bitcoinin ylimääräisistä kerroksista, joka mahdollistaa välittömät mikromaksut erittäin pienillä maksuilla. Ihanteellinen päivittäisiin pieniin summiin.

- **Bitcoin (on-chain)** : Bitcoin-protokollan päälohkoketju, joka soveltuu suurempien summien tapahtumiin, joissa maksimaalinen turvallisuus ja lopullisuus ovat ensisijaisia.

- **Liquid Network** : Blockstreamin kehittämä Bitcoinin sidechain (rinnakkaisketju), joka mahdollistaa nopeat ja luottamukselliset tapahtumat käyttäen Liquid Bitcoin (L-BTC) -yksiköitä.

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Oletuksena Blitz luo Lightning-laskun, mutta voit valita verkon, jossa haluat vastaanottaa satoshisi, napsauttamalla **"Choose format"** -painiketta (Valitse muoto).

![receive-sats](assets/fr/03.webp)

### Yhteystietojen luominen

Blitz Wallet yksinkertaistaa toistuvien bitcoin-lähetysten tekemistä yhteystietojärjestelmänsä avulla.

**Contacts**-valikossa voit tallentaa Blitz-käyttäjänimiä tai Lightning-osoitteita (LNURL), joiden kanssa olet usein tekemisissä.

Näin voit lähettää satosheja näihin osoitteisiin muutamalla napsautuksella ilman, että sinun tarvitsee skannata QR code -koodia tai syöttää osoitetta manuaalisesti joka kerta.

### Bitcoinien lähettäminen

Tavanomaisten bitcoin-lähetystapojen (QR code -skannaus, osoitteen manuaalinen syöttäminen) lisäksi Blitz tarjoaa useita käytännöllisiä vaihtoehtoja:

- **Kuvasta** (*From Image*) : Tuo QR code kuvakirjastostasi.
- **Leikepöydältä** (*From Clipboard*) : Liitä aiemmin kopioitu osoite tai lasku.
- **Manuaalinen syöttö** (*Manual Input*) : Syötä suoraan Bitcoin-osoite, Lightning-lasku tai luettava osoite (esimerkiksi `käyttäjä@walletofsatoshi.com`).
- **Yhteystiedoista** : Valitse ennalta tallennettu vastaanottaja ja lähetä muutamalla napsautuksella.

**Wallet**-valikossa napsauta **"Nuoli ylös"** -painiketta (↑), valitse lähetystapa, syötä lähetettävä määrä, lisää kuvaus ja vahvista tapahtuma.

Lähetyksen vähimmäismäärä on tällä hetkellä **1 000 satoshia**.

![send-bitcoin](assets/fr/05.webp)

## Blitz-kauppa

Bitcoin-siirtojen lisäksi Blitz Wallet sisältää kaupan, jossa voit käyttää bitcoinejasi digitaalisten palveluiden ostamiseen suoraan sovelluksesta.

Napsauta päävalikon **Store**-välilehteä päästäksesi kauppaan. Löydät sieltä myös pääsyn **Bitrefill**-alustalle, jonka kautta voit ostaa lahjakortteja tuhansilta kauppiailta ympäri maailmaa suoraan bitcoineilla.

- **Tekoäly** : Käytä uusimpia generatiivisen tekoälyn malleja (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) ja maksa krediittisi suoraan satosheina. Tarjolla on useita paketteja tarpeidesi mukaan (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonyymit tekstiviestit** : Lähetä ja vastaanota tekstiviestejä kaikkialla maailmassa paljastamatta henkilökohtaista puhelinnumeroasi. Palvelusta veloitetaan satosheina jokaisesta lähetetystä viestistä.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard** : Suojaa yksityisyyttäsi verkossa tilaamalla WireGuard VPN -tilaus (viikoittainen, kuukausittainen tai neljännesvuosittainen), maksettavissa bitcoineilla suoraan Blitz-kaupasta. Sinun tarvitsee vain ladata WireGuard-asiakassovellus laitteellesi.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet kulissien takana: syventävä katsaus

Blitz Walletin käyttöhelppouden takana piilee hyvin suunniteltu tekninen arkkitehtuuri, joka yhdistää useita Bitcoin-ekosysteemin kerroksia.

### Saldosi jakautuminen

Blitz Wallet hallinnoi saldoasi läpinäkyvästi jakamalla varasi eri protokollien välille tarpeiden mukaan. Kun saldosi on alle 500 000 satoshia, Blitz käyttää **Liquid Networkia** ja atomic swaps -teknologiaa tarjotakseen sujuvan kokemuksen ja mahdollistaakseen Lightning Network -tapahtumat myös pienillä summilla.

Tämä lähestymistapa takaa yksinkertaisen käyttöönoton uusille käyttäjille ilman, että heidän tarvitsee ymmärtää taustalla olevia mekanismeja. Voit tarkastella saldosi jakautumista eri kerroksien välillä valikossa **Asetukset > Balance Info**.

![balance](assets/fr/09.webp)

### Lightning-tila (valinnainen)

Oletuksena Blitz Wallet käyttää Liquid Networkia ja Spark-protokollaa tarjotakseen sujuvan kokemuksen ilman teknistä määritystä. Blitz antaa kuitenkin mahdollisuuden aktivoida **Lightning-tilan**, joka avaa automaattisesti maksukanavan, kun saldosi saavuttaa **500 000 satoshia** (0,005 BTC).

Aktivoidaksesi Lightning-tilan, siirry **Asetuksiin** ja napsauta sitten **Tekniset asetukset** -osiossa **Node Info** -vaihtoehtoa.

![enable-lightning](assets/fr/10.webp)

Spark-protokollan ansiosta tämä aktivointi on **valinnainen**: Spark mahdollistaa jo Lightning-yhteensopivat maksut ilman kanavan avaamista tai saapuvan likviditeetin hallintaa. Natiivi Lightning-tila on hyödyllinen edistyneille käyttäjille, jotka haluavat oman Lightning-solmun sovelluksen sisälle.

### Myyntipiste (PoS)

Blitz Wallet sisältää **myyntipiste**-toiminnon, jonka avulla kauppiaat voivat hyväksyä bitcoin-maksuja suoraan sovelluksesta.

**Asetukset > Point-of-sale** -valikossa voit määrittää:

- Kauppasi yksilöllisen tunnisteen
- Paikallisen fiat-valuutan hintojen näyttämiseen
- Ohjeet työntekijöillesi
- Tippausvaihtoehdon asiakkaillesi

Asiakkaidesi tarvitsee vain skannata generoitu QR code suorittaakseen bitcoin-maksunsa välittömästi.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Tämän oppaan kirjoittamisessa käytetyt lähteet:
- [Breez](https://breez.technology/) Technologyn blogi: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
