---
name: Portaali
description: TwentyTwo-Devices-laitteiston lompakkoportaalin määrittäminen ja käyttö
---
![cover](assets/cover.webp)

Portal on Bitcoin-laitteistolompakko, jonka on suunnitellut TwentyTwo Devices, yritys, joka on erikoistunut avoimen lähdekoodin laitteistolompakoiden luomiseen bitcoin-käyttäjille. Magical Bitcoin -projektin ([jatkossa nimeltään BDK](https://github.com/bitcoindevkit)) luoja Alekos Filini on perustanut yrityksen, joka on työskennellyt Blockstreamille ja BHB Networkille, ja TwentyTwo Devicesin tavoitteena on keskittyä käyttäjän itsenäisyyteen, yksinkertaisuuteen ja turvallisuuteen.

Se, mikä erottaa Portalin muista markkinoilla olevista laitteistolompakoista, on sen natiivi integrointi älypuhelimiin. Se toimii ilman kaapeleita tai akkuja. Se käyttää NFC-tekniikkaa virran syöttämiseen ja kommunikointiin minkä tahansa yhteensopivan mobiililompakon kanssa. Sen kiehtova muotoilu on suunniteltu ergonomiseen käyttöön. Pyöreä osa on sijoitettu älypuhelimen takaosaan, josta paljastuu näyttö, josta voit tarkistaa maksutapahtumien yksityiskohdat ennen niiden allekirjoittamista siihen tarkoitetulla painikkeella.

![Image](assets/fr/01.webp)

Täysin avoimen lähdekoodin portaali perustuu Rust-kielellä kirjoitettuun laiteohjelmistoon ja käyttää BDK:ta (Bitcoin Dev Kit) avainten ja tapahtumien hallintaan. Se maksaa 89 euroa [virallisilla verkkosivuilla](https://store.twenty-two.xyz/products/portal-hardware-wallet).

Tätä kirjoitettaessa portaali on yhteensopiva Nunchuk- ja Bitcoin Keeper -sovellusten kanssa. Tässä opetusohjelmassa konfiguroimme sen Nunchukin kanssa.

## Unboxing

Kun saat portaalin, tarkista, että laatikko ja sen sinetöivä etiketti ovat hyvässä kunnossa. Sisällä portaali on sinetöidyssä pussissa.

Varmista, että sinetti on ehjä, jotta voit varmistaa, että pussia ei ole avattu. Pussissa suurilla kirjaimilla näkyvän yksilöllisen numeron on vastattava sinisen sinetin alle mustalla kirjoitettua numeroa, laatikon etiketissä olevaa numeroa ja sitä numeroa, joka näkyy näytölläsi, kun käynnistät laitteen ensimmäisen kerran.

![Image](assets/fr/02.webp)

## Nunchukin asennus

Käytämme portaalissa sijaitsevan lompakon hallintaan Nunchuk-sovellusta. Lataa sovellus [Google Play Storesta](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Storesta](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) tai suoraan [tiedosto `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).

![Image](assets/fr/03.webp)

Jos käytät Nunchukia ensimmäistä kertaa, sovellus pyytää sinua luomaan tilin. Tässä ohjeessa käyttäjätunnuksen luominen ei ole tarpeen. Valitse "*Jatka vieraana*" jatkaaksesi ilman tiliä.

![Image](assets/fr/04.webp)

## Portaalin konfigurointi

Napsauta Nunchukin aloitusnäytössä näytön yläreunassa olevaa "*NFC*"-logoa.

![Image](assets/fr/05.webp)

Aseta portaali älypuhelimen takapuolelle sen aktivoimiseksi.

![Image](assets/fr/06.webp)

Nunchuk tunnistaa portaalisi. Napsauta sitten "*Jatka*".

![Image](assets/fr/07.webp)

Jos haluat luoda uuden salkun, valitse "*Generate seed on Portal*" ja napsauta sitten "*Continue*".

![Image](assets/fr/08.webp)

Voit valita 12- tai 24-sanaisen muistilausekkeen. Molempien vaihtoehtojen tarjoama turvallisuus on samanlainen, joten voit valita sen, joka on helpointa tallentaa, eli 12 sanaa.

![Image](assets/fr/09.webp)

Tämän jälkeen sinua pyydetään valitsemaan salasana. Salasana avaa portaalin lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. Salasana ei osallistu lompakkosi kryptografisten avainten johtamiseen. Joten vaikka salasanaa ei olisikaan saatavilla, 12- tai 24-sanaisen muistisanan avulla voit saada bitcoinisi takaisin haltuusi, vaikka sinulla ei olisikaan pääsyä salasanaan. On suositeltavaa valita mahdollisimman satunnainen ja riittävän pitkä salasana. Varmista, että tallennat tämän salasanan erilliseen paikkaan siitä, missä portaali on tallennettu (esim. salasanahallintaan).

![Image](assets/fr/10.webp)

Portaalisi näyttää 12-sanaisen muistisanan. Tämä muistisana antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varasi, vaikka hänellä ei olisi fyysistä pääsyä portaaliin.

12-sanainen lause palauttaa pääsyn bitcoineihisi, jos portaali katoaa, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kaivertaa sen paperille, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

näitä sanoja ei tietenkään saa koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkisalkkua käytetään vain Testnetissä, ja se poistetaan opetusohjelman päätyttyä.**_

Paina portaalin painiketta lujasti siirtyäksesi seuraaviin sanoihin. Varmista, että asetat koko sormesi painikkeelle ja pidät painetta painettuna muutaman sekunnin ajan, jotta vuorovaikutus havaitaan kunnolla.

![Image](assets/fr/11.webp)

Portaali vahvistaa tämän jälkeen Nunchukiin syöttämäsi salasanan.

![Image](assets/fr/12.webp)

Olet nyt saanut valmiiksi portaalisi konfiguroinnin ja muistilauseen luomisen!

![Image](assets/fr/13.webp)

## Bitcoin-lompakon kokoonpano

Napsauta Nunchukilla "*Jatka*" ja pidä portaali edelleen puhelimen takaosaa vasten.

![Image](assets/fr/14.webp)

Tässä opetusohjelmassa aion perustaa yhden tunnuksen salkun, joten valitsen tämän vaihtoehdon.

![Image](assets/fr/15.webp)

Käytä oletustiliä eli lompakon ensimmäistä tiliä (numero 0). Nunchuk pyytää sinua sitten vahvistamaan Portal-salasanasi avataksesi lukituksen.

![Image](assets/fr/16.webp)

Vahvista portaalissa xpubin vienti Nunchukiin. Näin voit hallinnoida lompakkoa älypuhelimestasi ilman, että voit käyttää bitcoineja ilman portaalia. Vahvista painamalla painiketta.

Huomaa, että sinun tapauksessasi ilmoitettu johdannaispolku on erilainen kuin minun, koska tämä opetusohjelma suoritetaan Testnetissä.

![Image](assets/fr/17.webp)

Anna portfoliollesi nimi, esimerkiksi "*Portal*", ja napsauta sitten "*Jatka*".

![Image](assets/fr/18.webp)

Nunchuk näyttää sitten kuvaajasi. On hyvä idea tehdä varmuuskopio. Vaikka Descriptorin avulla et voi käyttää bitcoineja, sen avulla voit jäljittää avaimesi johdannaispolut muistilauseestasi, jos lompakko palautetaan. Säilytä se turvallisessa paikassa, sillä vaikka sen vuotaminen ei ehkä aiheuta turvallisuusongelmaa, se on kuitenkin luottamuksellisuusongelma.

Napsauta "*Tehdään*".

![Image](assets/fr/19.webp)

Sinun on nyt luotava julkiset avaimet Bitcoin-lompakkoasi varten. Tee tämä napsauttamalla "*Luo uusi lompakko*"-painiketta.

![Image](assets/fr/20.webp)

Napsauta uudelleen "*Luo uusi lompakko*". Valitse sitten vaihtoehto "*Luo uusi lompakko käyttäen olemassa olevia avaimia*".

![Image](assets/fr/21.webp)

Valitse salkullesi nimi ja napsauta "*Jatka*".

![Image](assets/fr/22.webp)

Valitse portaali tämän uuden avainsarjan allekirjoitusvälineeksi ja napsauta sitten "*Jatka*".

![Image](assets/fr/23.webp)

Jos olet tyytyväinen kaikkeen, validoi luomus.

![Image](assets/fr/24.webp)

Tämän jälkeen voit tallentaa lompakon asetustiedoston. Tämä tiedosto sisältää vain julkiset avaimesi, mikä tarkoittaa, että vaikka joku pääsisi siihen käsiksi, hän ei pysty varastamaan bitcoinejasi. Hän pystyy kuitenkin seuraamaan kaikki tapahtumasi. Tämä tiedosto on siis vain riski yksityisyydellesi. Joissakin tapauksissa se voi olla välttämätön lompakkosi palauttamiseksi.

![Image](assets/fr/25.webp)

Ja siinä kaikki!

![Image](assets/fr/26.webp)

## Miten voin vastaanottaa bitcoineja Portalilla?

Jos haluat vastaanottaa bitcoineja, valitse lompakko.

![Image](assets/fr/27.webp)

Ennen kuin käytät luotua osoitetta, tarkista se portaalin näytöltä. Tee tämä napsauttamalla "*Vastaanottaa*".

![Image](assets/fr/28.webp)

Napsauta kolmea pistettä ja valitse sitten "*Varmista osoite PORTALin kautta*". Syötä sitten salasanasi.

![Image](assets/fr/29.webp)

Aseta portaali puhelimen takaosaan ja vahvista painamalla painiketta.

![Image](assets/fr/30.webp)

Varmista, että portaalissa näkyvä osoite vastaa Nunchukissa olevaa osoitetta, ja vahvista sitten painamalla painiketta uudelleen. Jos osoitteet ovat samat, voit antaa tämän osoitteen maksajalle.

![Image](assets/fr/31.webp)

Kun maksajan maksutapahtuma on lähetetty, näet sen lompakossasi.

![Image](assets/fr/32.webp)

Napsauta "*Katsele kulmia*".

![Image](assets/fr/33.webp)

Valitse uusi UTXO.

![Image](assets/fr/34.webp)

Klikkaa "*+*" "*Tags*" -kohdan vieressä lisätäksesi UTXO:lle tunnisteen. Tämä on hyvä käytäntö, sillä se auttaa sinua muistamaan, mistä kolikkosi ovat peräisin, ja optimoi yksityisyytesi, kun käytät niitä tulevaisuudessa.

![Image](assets/fr/35.webp)

Valitse olemassa oleva tunniste tai luo uusi ja napsauta sitten "*Tallenna*". Voit myös luoda "*kokoelmia*" järjestelläksesi osia jäsennellymmin.

![Image](assets/fr/36.webp)

## Miten lähetän bitcoineja portaalin avulla?

Nyt kun lompakossasi on bitcoineja, voit myös lähettää niitä. Klikkaa valitsemaasi lompakkoa.

![Image](assets/fr/37.webp)

Napsauta "*lähettää*"-painiketta.

![Image](assets/fr/38.webp)

Valitse lähetettävä summa ja napsauta sitten "*Jatka*".

![Image](assets/fr/39.webp)

Lisää tulevaan tapahtumaan "*merkintä*", joka muistuttaa sinua sen tarkoituksesta.

![Image](assets/fr/40.webp)

Kirjoita sitten vastaanottajan osoite sille varattuun kenttään. Voit myös skannata QR-koodiksi koodatun osoitteen napsauttamalla näytön oikeassa yläkulmassa olevaa kuvaketta. Napsauta sitten "*Luo tapahtuma*"-painiketta.

![Image](assets/fr/41.webp)

Tarkista maksutapahtuman tiedot, napsauta sitten portaalin vieressä olevaa "*Sign*"-painiketta ja syötä salasanasi.

![Image](assets/fr/42.webp)

Aseta portaali puhelimen takaosaan. Tarkista, että vastaanottajan osoite ja summa ovat oikein. Jos näin on, jatka painamalla painiketta.

![Image](assets/fr/43.webp)

Tarkista, että tapahtumamaksu on oikea, ja allekirjoita tapahtuma painamalla painiketta uudelleen.

![Image](assets/fr/44.webp)

Tapahtumasi on allekirjoitettu. Voit tarkistaa sen yksityiskohdat vielä kerran Nunchukista ja lähettää sen sitten Bitcoin-verkkoon napsauttamalla "*Lähetä transaktio*" -painiketta.

![Image](assets/fr/45.webp)

Tapahtumasi odottaa nyt vahvistusta.

![Image](assets/fr/46.webp)

Onneksi olkoon, olet nyt oppinut käyttämään Portalia! Jos löysit tämän opetusohjelman hyödylliseksi, olisin kiitollinen, jos jättäisit alle vihreän peukalon. Voit vapaasti jakaa tätä artikkelia sosiaalisissa verkostoissa. Kiitos paljon!

Jos haluat lisätietoja, tutustu täydelliseen koulutuskurssiimme HD-portfolioiden toiminnasta:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
