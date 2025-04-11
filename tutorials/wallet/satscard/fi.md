---
name: Satscard
description: Satscardin asettaminen ja käyttäminen Nunchukin kanssa
---
![cover](assets/cover.webp)

Bitcoin on elektroninen käteisjärjestelmä, joka mahdollistaa vertaisverkkotransaktiot. Jotta voimme olla varmoja transaktion muuttumattomuudesta, on odotettava useita vahvistuksia (yleensä 6), jotta voidaan välttää lähettäjän mahdolliset kaksinkertaiset kulutukset. Tämä vahvistusviive voi joskus olla epäkäytännöllinen, erityisesti kun halutaan välitöntä lopullisuutta, joka on samankaltainen kuin fyysisen käteisen kanssa. Toisin kuin käteisen kohdalla, jossa setelin omistus siirtyy välittömästi, Bitcoin-transaktiot sisältävät odotusajan ennen kuin ne katsotaan lopullisesti peruuttamattomiksi.

Tässä kohtaa Satscard tulee mukaan kuvaan. Se tarjoaa menetelmän fyysisten ja välittömien bitcoinien siirtoon, ilman että tarvitsee suorittaa ketjutransaktiota. Satscard toimii haltijakorttina, joka mahdollistaa bitcoinien omistusoikeuden turvallisen siirron, tarjoten näin kokemuksen, joka on lähempänä perinteistä käteistä. Tässä oppaassa esittelen sinulle tämän ratkaisun.

## Mikä on Satscard?

Coinkiten Satscard on Opendimen seuraaja. Se on NFC-kortti, joka mahdollistaa bitcoinien fyysisen siirron, samankaltaisesti kuin seteli tai kolikko. Toisin kuin perinteinen laitteistolompakko, Satscard on haltijakortti, mikä tarkoittaa, että kortin fyysinen hallussapito vastaa sen turvaamien bitcoinien omistusta. Sen hinta vaihtelee $6.99 ja $17.99 välillä valitun designin mukaan.

![SATSCARD](assets/notext/01.webp)

Satscard-piiri on varustettu 10 paikalla, joiden avulla se voi varastoida bitcoineja jopa 10 kertaa 10 eri osoitteeseen. Jokainen paikka toimii itsenäisesti ja teoriassa sitä tulisi käyttää vain kerran bitcoinien lukitsemiseen siihen. Bitcoinien käyttämiseksi riittää, että avaat paikan yhteensopivalla sovelluksella, kuten Nunchuk, syöttämällä Satscardin takana olevan 6-numeroisen varmistuskoodin.

Kortti varmistaa, että bitcoinien turvaamiseen käytetty yksityinen avain ei voi jäädä entisen omistajan hallintaan, kun he fyysisesti luopuvat kortista. Vastaanottaja voi myös tarkistaa paikan pätevyyden ja siinä olevan määrän vaihdon hetkellä.

Tämä järjestelmä on erityisen hyödyllinen fyysisten tavaroiden ostamiseen bitcoineilla tai bitcoinien antamiseen lahjaksi.

## Miten ostaa Satscard?

Satscardin voi ostaa [virallisilta Coinkiten verkkosivuilta](https://store.coinkite.com/store/category/satscard). Jos haluat ostaa sen fyysisestä kaupasta, voit myös löytää [sertifioitujen jälleenmyyjien listan](https://coinkite.com/resellers) sivustolta.
Tarvitset myös NFC-yhteyksiä tukevan puhelimen tai USB-laitteen NFC-korttien lukemiseen 13.56 MHz:n standarditaajuudella.
## Miten ladata paikka Satscardiin?

Kun olet saanut Satscardisi, ensimmäinen askel on tarkistaa pakkaus varmistaaksesi, ettei sitä ole avattu. Jos pakkaus on vahingoittunut, se voi viitata siihen, että kortti on saattanut olla kompromissin kohteena ja se ei ehkä ole aito.

Satscardin hallintaan käytämme **Nunchuk Wallet** -mobiilisovellusta. Varmista, että älypuhelimesi tukee NFC:tä, ja lataa sitten Nunchuk [Google Play Kaupasta](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Storesta](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) tai suoraan sen [`.apk` tiedostosta](https://github.com/nunchuk-io/nunchuk-android/releases).
Teoriassa voisit lähettää bitcoineja suoraan Satscardisi takana olevaan osoitteeseen käyttämättä Nunchukia. Kuitenkin neuvon olemaan tekemättä näin, sillä ensin varmistamme, että ensimmäisen paikan osoite on todella johdettu Satscardiin tallennetusta yksityisavaimesta eikä se ole huijausosoite.

Jos käytät Nunchukia ensimmäistä kertaa, sovellus tarjoaa sinulle mahdollisuuden luoda tilin. Tämän oppaan tarkoituksiin tilin luominen ei ole tarpeen. Valitse siis "*Jatka vieraana*" jatkaaksesi ilman tiliä.

Sitten klikkaa "*Avustamaton lompakko*".

Seuraavaksi klikkaa "*Tutkin itse*" -painiketta.

Kun olet Nunchukin kotinäytöllä, klikkaa näytön yläosassa olevaa "*NFC*" -logoa.

Pidä Satscardisi puhelimesi takana skannataksesi sen.

Nunchuk näyttää vastaanotto-osoitteen, joka vastaa Satscardisi ensimmäistä paikkaa. Normaalisti tämän osoitteen tulisi olla identtinen kortin takana käsin kirjoitetun osoitteen kanssa. Kopioi tämä osoite ja käytä sitä siirtääksesi bitcoineja, jotka haluat lukita tähän paikkaan.

## Kuinka tarkistaa bitcoinien määrä paikassa?

Kun siirto on vahvistettu, voit tarkistaa Satscardisi paikan saldoa skannaamalla sen Nunchukilla. Näin ollen siirron aikana bitcoinien vastaanottaja voi välittömästi tarkistaa Nunchuk-sovelluksellaan, että kortti todella sisältää heille velkaa olevat bitcoinit.

Jos vastapuolella ei ole Nunchuk-sovellusta, he voivat silti tarkistaa Satscardin validiteetin. Aktivoi vain NFC älypuhelimessasi ja aseta Satscard laitteen taakse. Tämä avaa automaattisesti Satscard-verkkosivuston selaimessa, jossa voi tarkistaa kortin validiteetin sekä siihen liittyvän bitcoin-määrän.

## Kuinka nostaa bitcoineja paikasta?

Nyt kun Satscardisi ensimmäinen paikka on ladattu tietyllä määrällä bitcoineja, voit antaa kortin maksun saajalle.

Jos olet vastaanottaja, sinun on asennettava Nunchuk. Sovelluksessa ollessasi klikkaa näytön yläosassa olevaa "*NFC*" -logoa.

Aseta Satscardisi puhelimesi taakse.

Nunchuk paljastaa osoitteeseen turvatun määrän.

Avataksesi yksityisavaimen ja siirtääksesi bitcoinit omaan osoitteeseesi, klikkaa "*Avaa ja pyyhkäise saldo*" -painiketta.

"*Pyyhkäise lompakkoon*" -vaihtoehto mahdollistaa bitcoinien suoran lähettämisen Nunchuk-sovelluksessasi jo olevaan lompakkoon. Siirtääksesi varat eri vastaanotto-osoitteeseen, valitse "*Nosta osoitteeseen*".
![SATSCARD](assets/notext/16.webp)
Syötä vastaanotto-osoite, johon haluat lähettää Satscardilla turvatut bitcoinit. Varmista, että syötetty osoite on oikein (tämä on ainoa kerta, kun voit varmistaa sen), ja klikkaa sitten "*Luo transaktio*" -painiketta.

![SATSCARD](assets/notext/17.webp)

Syötä Satscardisi PIN-koodi. Tämä 6-numeroinen koodi on merkitty fyysisen kortin taakse.

![SATSCARD](assets/notext/18.webp)

Pidä Satscardisi älypuhelimesi takana allekirjoittaessasi transaktion yksityisavaimella, joka on tallennettu NFC-kortille.

![SATSCARD](assets/notext/19.webp)

Transaktiosi on nyt allekirjoitettu ja lähetetty Bitcoin-verkkoon, mikä tarkoittaa, että käyttämäsi paikka Satscardissasi on nyt tyhjä.

![SATSCARD](assets/notext/20.webp)

## Kuinka käyttää Satscardia uudelleen?

Toisin kuin kertakäyttöiset ratkaisut, kuten Opendime, Satscardissa on siru, joka sisältää 10 itsenäistä paikkaa, mahdollistaen jopa 10 toimintoa yhdellä kortilla. Ensimmäinen paikka, joka on esiasetettu tehtaalla Coinkiten toimesta, vastaa vastaanotto-osoitetta, joka on kirjoitettu Satscardisi taakse.

![SATSCARD](assets/notext/21.webp)
Aktivoidaksesi 9 muuta paikkaa, sinun on luotava avainpari ja osoite Nunchuk-sovelluksen kautta. Sovelluksen kotisivulla klikkaa "*NFC*" -logoa näytön yläosassa.
![SATSCARD](assets/notext/22.webp)

Aseta Satscardisi puhelimesi taakse.

![SATSCARD](assets/notext/23.webp)

Nunchuk ilmoittaa, että kortissa ei ole aktiivisia paikkoja, mikä on normaalia, koska ensimmäinen on jo käytetty ja toista ei ole vielä luotu. Nähdäksesi aiemmin käytetyt paikat, klikkaa "*Näytä avatut paikat*". Näiden paikkojen uudelleenkäyttöä suositellaan välttämään, koska se johtaisi osoitteen uudelleenkäyttöön, mikä on haitallista ketjusi yksityisyydelle. Siksi asetamme uuden paikan klikkaamalla "*Kyllä*" -painiketta.

![SATSCARD](assets/notext/24.webp)

Sinun on nyt päätettävä, miten luot master chain -koodisi.

Satscardin paikat noudattavat BIP32-standardia, mikä tarkoittaa, että kryptografisten avainten johdannainen, jotka turvaavat bitcoinit, ei perustu mnemoniseen lauseeseen kuten BIP39-lompakoissa, vaan suoraan master yksityisavaimelle ja master chain -koodille. Nämä kaksi elementtiä käytetään syötteenä HMAC-SHA512-funktiossa lapsiavainparin luomiseksi. Jokaisella paikalla on oma master-avaimensa ja oma master chain -koodinsa. Kullakin paikalla on vain yksi johdannaisen taso.

Ensimmäisen paikan avainpari on esiluotu Coinkiten toimesta. Tämän vuoksi sinulla on suora pääsy siihen Nunchukin kautta, ja siksi vastaanotto-osoite on kirjoitettu NFC-kortin taakse. Muiden paikkojen osalta olet kuitenkin vastuussa avainten luomisesta.

Kunkin paikan master yksityisavain luodaan suoraan Satscardilla, ja master chain -koodit on toimitettava ulkopuolelta. Uuden paikkasi chain -koodille sinulla on kaksi vaihtoehtoa: anna Nunchukin luoda se automaattisesti valitsemalla "*Automaattinen*", tai luo se itse valitsemalla "*Edistynyt*" ja syöttämällä se omistetussa tilassa. Chain -koodin on oltava mahdollisimman satunnainen ollakseen tehokas.

![SATSCARD](assets/notext/25.webp)
Syötä 6-numeroinen PIN, joka on merkitty Satscardisi taakse.
![SATSCARD](assets/notext/26.webp)

Aseta Satscardisi puhelimesi taakse.

![SATSCARD](assets/notext/27.webp)

Uusi paikka on konfiguroitu onnistuneesti. Voit nyt nähdä vastaanotto-osoitteen, johon voit tallettaa bitcoineja. Jatkaaksesi lataamista, noudata ohjeita kohdassa "*Kuinka ladata paikka Satscardiin?*" tässä oppaassa.
Voit toistaa tämän prosessin jopa 10 kertaa kullakin Satscardilla.

Onneksi olkoon, olet nyt ajan tasalla Satscardin käytöstä! Jos pidit tätä opasta hyödyllisenä, arvostaisin, jos voisit jättää peukun ylös alla. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissasi. Paljon kiitoksia!