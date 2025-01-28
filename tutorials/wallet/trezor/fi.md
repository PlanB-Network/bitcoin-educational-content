---
name: Trezor model One
description: Trezor model Onen käyttöönotto ja käyttö
---

![cover](assets/cover.webp)

Kylmä laitteistolompakko – 60€ – Aloittelija – Turvaa 2 000€ ja 50 000€ välillä.

Kylmänä fyysisenä lompakkona Trezor on ihanteellinen Bitcoinin aloittamiseen. Se on helppokäyttöinen, ei liian kallis ja toiminnallinen.

Olemme jo tehneet ohjeita sen käyttöön:

1. Laitteen käyttöönotto
2. Bitcoinien palauttaminen
3. Bitcoinien käyttö, lähettäminen ja vastaanottaminen

Haluaisitko sinäkin omistaa Trezorin?
Voit tukea projektia klikkaamalla alla!

käyttöönotto -https://www.youtube.com/watch?v=q-BlT6R4_bE

palautus: https://www.youtube.com/watch?v=3n4d4egjiFM

käyttö: https://www.youtube.com/watch?v=syouZjLC1zY

## kirjoitusopas

oppaan tarjoaa https://armantheparman.com/trezor/

## Trezorin käyttöönotto

Trezor toimitetaan oman mikro-USB-kaapelinsa kanssa. Varmista, että käytät sitä etkä mitä tahansa vanhaa kaapelia, joka lojuu ympäriinsä. Jotkut USB-kaapelit ovat vain virtaa varten. Tämä kaapeli siirtää sekä dataa ETTÄ virtaa. Jos käytät laitetta puhelimen latauskaapelilla, laite ei ehkä yhdisty.

Yhdistä se tietokoneeseesi ja laite käynnistyy. Saat viestin, joka sanoo "Mene osoitteeseen Trezor.io/start". Tee niin ja lataa Trezor Suite tietokoneellesi.

![image](assets/0.webp)

Klikkaa latauspainiketta ("Get Desktop App")

![image](assets/1.webp)

Huomaa Allekirjoitus ja Allekirjoitusavaimen linkit. Latauksen vahvistamiseksi (tarkista, että lataustasi ei ole manipuloitu) on lisävaiheita, jotka ovat valinnaisia aloittaessasi, mutta PAKOLLISIA, jos sinulla on merkittävästi varallisuutta turvattavana. Ohjeet siihen löytyvät Liitteestä A (oppaan lopussa)

Yhdistä Trezor tietokoneeseen mikro-USB-kaapelilla ja asenna ja käynnistä ohjelma. Näin se näyttää Macissa:

![image](assets/2.webp)

Ohjelman suorittamisen jälkeen saat hassun varoituksen, jatka vain:

![image](assets/3.webp)

Klikkaa "Setup Trezor"

![image](assets/4.webp)

Jos laiteohjelmisto on vanhentunut, salli Trezorin päivittää laiteohjelmisto.

Seuraavaksi voit luoda uuden siemenen tai palauttaa lompakon eri laitteesta jo olemassa olevalla siemenelläsi. Käyn läpi uuden siemenen luomisen.

![image](assets/5.webp)

Klikkaa "Luo uusi lompakko" – ja vahvista haluavasi tehdä tämän itse laitteella klikkaamalla vahvistuspainiketta.

Sitten klikkaa ainoa vaihtoehto "Standard seed backup"

![image](assets/6.webp)

Sitten klikkaa "luo varmuuskopio"

![image](assets/7.webp)

Klikkaa kolmea valintamerkkiä muuttaaksesi ne vihreiksi (luonnollisesti lue jokainen viesti), ja sitten klikkaa "aloita varmuuskopio".

![image](assets/8.webp)

Seuraavaksi näet tämän:

![image](assets/9.webp)

Laitteessa, katso sinulle yksi kerrallaan esitetyt sanat ja kirjoita ne SIISTISTI ja JÄRJESTYKSESSÄ.

![image](assets/10.webp)

Aseta PIN-koodi lukitaksesi laitteen (tämä ei ole osa siementäsi, se on vain lukitaksesi laitteen, jotta kukaan ei pääse käsiksi sen sisällä olevaan siemeneen).

![image](assets/11.webp)
Sinulla on vaihtoehtoja lisätä shitcoineja lompakkoosi – kehotan sinua olemaan tekemättä niin ja säästämään vain Bitcoiniin, kuten selitän täällä (miksi bitcoin) ja täällä (miksi vain bitcoin).
![kuva](assets/12.webp)

Nimeä lompakkosi ja klikkaa "Access Suite":

![kuva](assets/13.webp)

Yksinkertaisinta on luoda lompakko ilman salasanaa, mutta parasta on luoda yksi salasanalla (oikea lompakkosi) JA yksi ilman salasanaa (harhautuslompakkosi). Joka kerta, kun käytät laitetta Trezor Suiten kautta, sinulta kysytään, haluatko "soveltaa" salasanaa vai ei.

![kuva](assets/14.webp)

Valitsin "Hidden Wallet" ja kirjoitin keksimäni salasanan "craigwrightisaliarandafraud"

![kuva](assets/15.webp)

Pidän siitä, että sitä kutsutaan "piilotetuksi" lompakoksi, koska se selittää osittain, miten salasanat toimivat.

Vahvista salasana laitteessa.

Koska tämä lompakko on tyhjä, minua pyydettiin vahvistamaan, että salasana on oikein:

![kuva](assets/16.webp)

Sinulta kysytään sitten, haluaisitko ottaa käyttöön merkinnät. En ole tutkinut tätä, mutta se kuulostaa tavalta, jolla voit merkitä transaktiosi ja tallentaa tiedot tietokoneellesi tai pilveen.

![kuva](assets/17.webp)

Lopulta lompakkosi on käytettävissä:

![kuva](assets/18.webp)

Se, mitä sinulla on tietokoneellasi, on niin kutsuttu "watching wallet", koska siinä on julkiset avaimet (ja osoitteet), mutta ei yksityisiä avaimia. Tarvitset yksityiset avaimet kuluttaaksesi (allekirjoittamalla transaktiot yksityisillä avaimilla). Tämän voi tehdä yhdistämällä laitteiston lompakon. Laitteiston lompakon pointti on, että transaktioita voidaan siirtää edestakaisin tietokoneen ja Trezorin välillä, allekirjoitus voidaan soveltaa Trezorin sisällä, ja yksityinen avain pysyy aina laitteen sisällä (turvana tietokoneen haittaohjelmia vastaan).

Trezor Suite on huono watching-wallet eri syistä. Se on OK vähimmäisvaatimuksiin, mutta jos haluat edetä, lue eteenpäin ja opi, miten yhdistää laite Sparrow Bitcoin Walletiin.

## Watching Wallet

Aiemmissa artikkeleissa selitin, miten ladata ja varmistaa Sparrow Bitcoin Wallet, ja miten yhdistää se omaan nodeen tai julkiseen nodeen. Voit seurata näitä ohjeita:

- Asenna Bitcoin Core
- Asenna Sparrow Bitcoin Wallet
- Yhdistä Sparrow Bitcoin Wallet Bitcoin Coreen

Vaihtoehto Sparrow Bitcoin Walletin käytölle on Electrum Desktop Wallet, mutta jatkan Sparrow Bitcoin Walletin selittämistä, koska pidän sitä parhaana useimmille ihmisille. Edistyneet käyttäjät saattavat pitää Electrumia vaihtoehtona (katso opas).

Ladataan nyt Sparrow ja yhdistetään Trezor (siemenlauseella mutta nyt salasanalla). Tätä lompakkoa ei ole koskaan altistettu Trezor Suitelle, koska se luodaan SEN JÄLKEEN, kun olemme yhdistäneet laitteen Trezor Suiten kanssa. Varmista, ettet koskaan yhdistä sitä uudelleen Trezor Suiteen, jotta et altista uutta lompakkoasi. (Voit yhdistää sen ilman salasanaa, koska se voi olla harhautuslompakkosi).

Luo uusi lompakko:

![kuva](assets/19.webp)

Nimeä se joksikin kauniiksi

![kuva](assets/20.webp)

Klikkaa "Connected Hardware Wallet".

![kuva](assets/21.webp)

![kuva](assets/22.webp)
Napsauta "Scan" ja sitten seuraavalla näytöllä "set passphrase" luodaksesi aivan uuden lompakon (käytä aivan uutta salasanaa, esim. vanha salasana jonka perään on lisätty numero toimisi). Sen jälkeen "send passphrase", ja vahvista se laitteessa.
![image](assets/23.webp)

Sen jälkeen klikkaa "import keystore".

Seuraavalla näytöllä ei ole mitään muokattavaa, Trezor on täyttänyt sen puolestasi. Klikkaa "Apply"

![image](assets/24.webp)

Seuraava näyttö mahdollistaa salasanan lisäämisen. Älä sekoita tätä "passphraseen"; monet ihmiset tekevät niin. Nimeäminen on valitettavaa. Salasana mahdollistaa tämän lompakon lukitsemisen tietokoneellasi. Se on spesifinen tälle ohjelmistolle tällä tietokoneella. Se ei ole osa Bitcoinin yksityisavaintasi.

Klikkaa "Apply"

![image](assets/25.webp)

Tauon jälkeen, kun tietokone miettii, näet vasemmalla olevien painikkeiden vaihtuvan harmaasta siniseksi. Onnittelut, lompakkosi on nyt valmis käytettäväksi. Tee ja lähetä transaktioita sydämesi kyllyydestä.

![image](assets/26.webp)

Vastaanottaminen

Vastaanottaaksesi hieman bitcoineja, mene vasemmalla olevaan Addresses-välilehteen ja valitse yksi osoitteista vastaanottoon. Klikkaa oikealla haluamaasi osoitetta ja valitse "copy address". Mene sitten vaihtopalveluun, josta raha lähetetään, ja liitä se sinne. Tai voit antaa osoitteen asiakkaalle, joka voi käyttää sitä maksamiseen sinulle.

Kun käytät lompakkoa ensimmäistä kertaa, sinun pitäisi vastaanottaa hyvin pieni määrä, harjoittele sen lähettämistä toiseen osoitteeseen, joko lompakon sisällä tai takaisin vaihtopalveluun, todistaaksesi, että lompakko toimii odotetusti.

Kun olet tehnyt sen, sinun täytyy varmuuskopioida sanat, jotka kirjoitit ylös. Yksi kopio ei riitä. Pidä vähintään kaksi paperikopiota (metalli on parempi), ja säilytä niitä kahdessa eri, hyvin turvatussa paikassa. Tämä vähentää luonnonkatastrofin riskiä tuhoamasta HWW:täsi ja paperivarmuuskopiota yhdessä tapahtumassa. Katso "Using Bitcoin Hardware Wallets" täydelliseen keskusteluun tästä.

## Lähettäminen

![image](assets/27.webp)

Maksua tehdessäsi sinun täytyy liittää osoite, johon maksat, "Pay to" -kenttään. Et voi jättää Label-kenttää tyhjäksi, se on vain omien lompakkojesi kirjanpitoa varten, mutta Sparrow ei salli sitä – kirjoita vain jotain (vain sinä näet sen). Syötä summa ja voit myös manuaalisesti säätää haluamaasi maksua.

Lompakko ei voi allekirjoittaa transaktiota, ellei HWW ole yhdistetty. Se on HWW:n tehtävä – vastaanottaa transaktio, allekirjoittaa se ja palauttaa se allekirjoitettuna. Varmista, kun allekirjoitat laitteessa, että visuaalisesti tarkistat maksamasi osoitteen olevan sama laitteessa ja tietokoneen näytöllä, sekä saamassasi laskussa (esim. saatat olla saanut sähköpostin maksusta tiettyyn osoitteeseen).

Kiinnitä myös huomiota siihen, että jos valitset maksun määrää suuremman kolikon, loput lähetetään yhteen lompakkosi vaihto-osoitteista. Jotkut ihmiset eivät ole tienneet tätä ja ovat tarkistaneet transaktionsa julkisessa lohkoketjussa, ja luulleet, että jotkin bitcoinit on lähetetty hyökkääjän osoitteeseen, mutta itse asiassa se oli heidän oma vaihto-osoitteensa.
Firmware

Firmwaren päivittämiseksi sinun on yhdistettävä Trezor Suiteen. Jos haluat tehdä tämän, varmista, että sinulla on varmuuskopiosanasi ja salasanasi saatavilla laitteen palauttamiseksi, siltä varalta että laite nollautuu.
Johtopäätös
Tämä artikkeli näytti sinulle, kuinka käyttää Trezor HWW:ta turvallisemmin ja yksityisemmin kuin mainostettu – mutta tämä artikkeli yksinään ei riitä. Kuten sanoin alussa, sinun tulisi yhdistää se tietoihin, jotka on annettu kohdassa "Bitcoin-laitelompakoiden käyttö".

## Liite A - Vahvista ohjelmiston lataus

![kuva](assets/28 .webp)

Lataa allekirjoitus (tekstitiedosto) ja allekirjoitusavain (tekstitiedosto) ja tee muistiinpano tiedostonimistä ja siitä, minne latasit tiedoston.

Seuraavaksi Macille tarvitset GPG Suiten (Katso ohjeet täältä).

Windowsille tarvitset GPG4winin (Katso ohjeet täältä).

Linuxille GPG on jo osa jokaista pakettia. Jos sinulla ei sitä ole, hanki se komennolla: sudo apt-get install gpg

Seuraavaksi Macille/Windowsille tai Linuxille, avaa terminaali ja syötä komento:

```bash
gpg –import XXXXXXXXXX
```

missä XXXXXXXXXX on allekirjoitusavaintiedoston koko polku (koko polku tarkoittaa hakemistoa ja tiedostonimeä, jossa tiedosto sijaitsee). Sinun pitäisi nähdä vahvistus onnistuneesta avaimen tuonnista.

Sitten

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

missä ZZZZZZZZZZ on allekirjoitustiedoston koko polku ja WWWWWWWWWW on Trezor Suiten ohjelman koko polku, jonka latasit.

Sinun pitäisi nähdä viesti "Hyvä allekirjoitus SatoshiLabsilta" jossain tulosteessa. Alhaalla on varoitus, jonka voi jättää huomiotta.