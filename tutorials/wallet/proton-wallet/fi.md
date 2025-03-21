---
name: Proton lompakko
description: Proton Bitcoin-lompakon asentaminen ja käyttö
---
![cover](assets/cover.webp)

Proton on digitaaliseen yksityisyyteen erikoistunut sveitsiläinen yritys, jonka CERNin tutkijat perustivat vuonna 2014. Avoimen lähdekoodin ratkaisuista tunnettu Proton tarjoaa palvelukokonaisuuksia, kuten Proton Mail, Proton VPN ja Proton Drive.

Proton esitteli hiljattain Proton Walletin, avoimen lähdekoodin Bitcoin-lompakon, joka on saatavilla mobiilisovelluksena tai verkkoasiakkaana, joka on yhteydessä Proton-tiliisi. Lompakon toiminnot ovat toistaiseksi suhteellisen klassisia, ja siinä on hyvältä Bitcoin-lompakolta odotettavissa olevat keskeiset työkalut, kuten RBF (*Replace-By-Fee*), merkintä tai mahdollisuus lisätä BIP39-salasana.

Tämän lompakon erityispiirre on mahdollisuus lähettää bitcoineja vastaanottajan sähköpostiosoitteella, jota varten Proton luo automaattisesti tyhjän Bitcoin-osoitteen, joka on linkitetty käyttäjän lompakkoon. Proton aikoo lisätä uusia ominaisuuksia tulevaisuudessa, kuten Lightning ja coinjoins (luultavasti Whirlpoolin avulla, kuten heidän GitHub-arkistossaan tapahtuneen toiminnan perusteella on ehdotettu).

## Luo Proton-tili

Proton Walletin käyttäminen edellyttää Proton-tiliä. Voit luoda sellaisen ilmaiseksi seuraamalla tämän Proton-postilaatikon luomiseen tarkoitetun ohjeen ensimmäisiä vaiheita (vain kohta "*Proton-tilin luominen*"). Kun tilisi on luotu, voit jatkaa tämän ohjeen loppuosaa.

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Yhdistä Proton-lompakkoon

Mene [Proton Wallet -sivustolle] (https://proton.me/wallet) ja napsauta "*Get Proton Wallet*" -painiketta.

![Image](assets/fr/01.webp)

Valitse "*Free*" -tilausvaihtoehto ja napsauta sitten "*Sign In*".

![Image](assets/fr/02.webp)

Kirjaudu sisään syöttämällä Proton-tiliisi liittyvä sähköpostiosoite ja salasana.

![Image](assets/fr/03.webp)

Tilisi pitäisi nyt näkyä. Klikkaa "*Aloita Proton Walletin käyttö nyt*".

![Image](assets/fr/04.webp)

## Luo Bitcoin-lompakko

Valitse tilisi oletusvaluutta ja napsauta sitten "*Luo uusi lompakko*".

![Image](assets/fr/05.webp)

Bitcoin-lompakkosi on nyt luotu. Voit teoriassa aloittaa sen käytön välittömästi, mutta on erittäin tärkeää tallentaa muistitietosi ensin. Tee tämä napsauttamalla käyttöliittymän oikeassa yläkulmassa olevaa "*Turvaa lompakkosi*".

![Image](assets/fr/06.webp)

Jos et ole vielä tehnyt sitä Protonissa, sinua pyydetään ottamaan tilistäsi varmuuskopio ja suojaamaan se 2FA-menetelmällä. Vaikka nämä turvatoimet koskevat koko Proton-tiliäsi, ne ovat sitäkin tärkeämpiä, kun Bitcoin-lompakkosi on integroitu siihen. Suosittelen vahvasti, että otat ne käyttöön.

![Image](assets/fr/07.webp)

Jos haluat tallentaa muistilauseesi, napsauta "*Tallenna tämän lompakon siemenlause*".

![Image](assets/fr/08.webp)

Syötä Proton-salasanasi.

![Image](assets/fr/09.webp)

Napsauta sitten "*View wallet seed phrase*" näyttääksesi lompakkosi muistilausekkeen.

![Image](assets/fr/10.webp)

Proton Wallet näyttää 12-sanaisen muistisanan. **Tämä muistisana antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi**. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi pääsyä Proton-tilillesi. 12-sanaisen lausekkeen avulla voit palauttaa pääsyn bitcoineihisi, jos menetät pääsyn tilillesi. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kirjoittaa sen paperille, tai jos haluat lisätä turvallisuutta, suosittelen kaiverruttamaan sen ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.

![Image](assets/fr/11.webp)

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Ei tietenkään koskaan pidä ottaa kuvaa näistä sanoista, toisin kuin minä teen tässä ohjeessa.**_

Napsauta "*Tehdään*"-painiketta, kun olet tallentanut lauseesi.

![Image](assets/fr/12.webp)

## Tutustu käyttöliittymään

Proton Walletin käyttöliittymä on erittäin intuitiivinen. Vasemmalla näet eri lompakot ja niihin liittyvät tilit. "*Primary*"-tili on päätilisi. Luottamuksellisuussyistä Proton-sähköpostiosoitteen kautta saadut bitcoinit sijoitetaan erilliselle tilille, jonka nimi on "*Bitcoin via Email*".

![Image](assets/fr/13.webp)

Voit lisätä uuden tilin napsauttamalla "*Lisää tili*".

![Image](assets/fr/14.webp)

Jos haluat luoda uuden salkun, napsauta "*+*"-symbolia "*Lompakot*" -kohdan vieressä.

![Image](assets/fr/15.webp)

Tässä voit lisätä BIP39-salasanan uuteen lompakkoon.

![Image](assets/fr/16.webp)

Jos haluat syventää tietämystäsi salasanasta, suosittelen tätä opetusohjelmaa:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Vastaanottaa bitcoineja

Jos haluat vastaanottaa bitcoineja lompakkoosi, valitse haluamasi tili käyttöliittymän vasemmasta reunasta ja napsauta sitten "*Vastaanottaa*"-painiketta.

![Image](assets/fr/17.webp)

Proton Wallet luo sitten automaattisesti uuden, tyhjän osoitteen.

![Image](assets/fr/18.webp)

Kun maksutapahtuma on suoritettu, löydät sen "*Tapahtumat*"-osiosta. Napsauta "*+Lisää*" määrittääksesi tapahtumalle etiketin.

![Image](assets/fr/19.webp)

## Lähetä bitcoineja

Nyt kun lompakossasi on bitcoineja, voit lähettää niitä. Valitse haluamasi tili käyttöliittymän vasemmasta reunasta ja napsauta sitten "*lähettää*".

![Image](assets/fr/20.webp)

Kirjoita vastaanottajan Bitcoin-osoite. Voit skannata QR-koodin napsauttamalla pientä logoa. Jos haluat lähettää sähköpostiosoitteeseen, kirjoita se suoraan tähän kenttään. Kun olet syöttänyt Bitcoin-osoitteen, napsauta pientä nuolta ja sitten "*Vahvista*".

![Image](assets/fr/21.webp)

Kirjoita lähetettävä summa joko fiat-valuutassa tai bitcoineina ja napsauta sitten "*Review*".

![Image](assets/fr/22.webp)

Valitse transaktiomaksu senhetkisen markkinatilanteen mukaan.

![Image](assets/fr/23.webp)

Lisää tapahtumaan etiketti ja tarkista sitten kaikki tiedot. Jos kaikki on oikein, klikkaa "*Vahvista ja lähetä*" allekirjoittaaksesi ja lähettääksesi tapahtuman.

![Image](assets/fr/24.webp)

Maksutapahtumasi näkyy nyt vahvistusta odottavana tilisi "*Tapahtumat*"-osiossa.

![Image](assets/fr/25.webp)

## Kirjaudu sisään sovellukseen

Web-asiakkaan lisäksi Proton Wallet on käytettävissä myös mobiilisovelluksella. Kun linkität lompakon Proton-tiliisi, voit synkronoida lompakkosi web-asiakkaan ja mobiilisovelluksen välillä.

Lataa Proton Wallet sovelluskaupastasi:


- [App Storessa](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [Google Play Storessa](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Asennuksen jälkeen napsauta "*Log in*" ja syötä sähköpostiosoitteesi ja Proton-salasanasi.

![Image](assets/fr/27.webp)

Tämän jälkeen pääset Bitcoin-lompakkoosi, jossa on samat ominaisuudet kuin verkkoasiakkaassa.

![Image](assets/fr/28.webp)

Onneksi olkoon, tiedät nyt, miten Proton Wallet asetetaan ja miten sitä käytetään. Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos jakamisesta!

Jos haluat mennä pidemmälle, suosittelen tätä opetusohjelmaa Jade Plusista, Blockstreamin uusimmasta laitteistolompakosta:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
