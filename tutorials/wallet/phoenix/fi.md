---
name: Phoenix
description: Phoenix Walletin asentaminen ja käyttö
---
![cover](assets/cover.webp)

Phoenix on Lightning-pohjaisiin ohjelmistoratkaisuihin erikoistuneen ranskalaisen ACINQ-yrityksen kehittämä Lightning-lompakko ja -solmu. Toisin kuin Wallet of Satoshin kaltaiset Lightning-lompakot, joissa bitcoinit ovat kolmannen osapuolen hallussa, Phoenix antaa käyttäjille mahdollisuuden pitää yksityiset avaimensa täysin hallinnassaan.

Itse asiassa Phoenix toimii kuin puhelimeen upotettu oikea Lightning-solmu, joka avaa automaattisesti kanavan ACINQ:n Lightning-solmun kanssa. Sovellus perustuu Eclairiin, ACINQ:n kehittämään Lightning-toteutukseen. Toisin kuin muut Lightning-solmuratkaisut, Phoenix yksinkertaistaa hallintaa huomattavasti. Käyttäjien ei tarvitse hallita kanavien avaamista ja sulkemista, pyörittää Bitcoin-solmua tai hallita likviditeettiään Lightning-verkossa. Phoenix hoitaa kaikki nämä tekniset toiminnot taustalla.

Tässä sovelluksessa yhdistyvät Lightning-mobiililompakoiden helppokäyttöisyys ja mukavuus sekä aidon henkilökohtaisen Lightning-solmun turvallisuus ja riippumattomuus. Phoenix mahdollistaa Lightning-verkon turvallisen, tehokkaan ja itsenäisen käytön sekä sujuvan ja intuitiivisen käyttökokemuksen.

Vastineeksi peritään tiettyjä maksuja:


- Salaman kautta lähettäminen maksaa 0,4 % summasta plus 4 satsia ;
- Jos käteistä tarvitaan Lightningin kautta tapahtuvaan vastaanottoon, veloitetaan 1 % summasta;
- Jokaisen kanavan avaaminen maksaa 1000 satsia.

Mielestäni Phoenix on erinomainen välivaiheen ratkaisu Lightning-salkkujen hallinnoinnin ja Lightning-solmun manuaalisen hallinnan välillä. Tämä sovellus sopii yhtä hyvin aloittelijoille kuin edistyneille käyttäjille, jotka eivät halua paneutua oman LND:n tai Core Lightningin hallinnan yksityiskohtiin. Selvitetään, miten sitä käytetään!

![Image](assets/fr/01.webp)

## Asenna sovellus

Mene sovelluskauppaan ja asenna Phoenix :


- [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet);
- [App Storessa](https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

Voit myös asentaa sovelluksen [apk-tiedoston avulla heidän GitHub-arkistostaan](https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Portfolion luominen

Kun sovellus on käynnistynyt, voit ohittaa esityksen napsauttamalla "*Seuraava*"-painiketta ja sitten "*Aloita*"-painiketta.

![Image](assets/fr/04.webp)

Valitse "*Luo uusi lompakko*".

![Image](assets/fr/05.webp)

Siinä kaikki, Lightning-lompakkosi ja solmusi on nyt luotu.

![Image](assets/fr/06.webp)

## Tallenna muistisääntö

Ennen kuin aloitamme, meidän on tallennettava 12-sanainen muistisääntö. Tämä lause antaa täydellisen, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lause, voi varastaa varasi, vaikka hänellä ei olisi fyysistä pääsyä puhelimeesi.

12-sanainen lause palauttaa pääsyn bitcoineihisi, jos puhelimesi katoaa, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kirjoittaa sen paperille tai kaivertaa sen ruostumattomaan teräkseen, jotta se on suojattu tulipalolta, tulvalta tai romahdukselta. Muistilapun välinevalinta riippuu turvallisuusstrategiastasi, mutta jos käytät Phoenixia kohtuullisia summia sisältävänä menosalkkuna, paperin pitäisi riittää.

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
Napsauta käyttöliittymän yläreunassa näkyvää viestiä "*Tallenna lompakkosi...*".

![Image](assets/fr/07.webp)

Napsauta sitten "*Tallenna lompakkoni*".

![Image](assets/fr/08.webp)

Napsauta sitten "*Katsele avaimeni*" ja tallenna muistisääntösi fyysiselle tietovälineelle.

![Image](assets/fr/09.webp)

Tarkista käyttöliittymän alaosassa olevat kaksi ruutua vahvistaaksesi, että varmuuskopiointi on suoritettu onnistuneesti.

![Image](assets/fr/10.webp)

## Sovelluksen asennus

Ennen kuin teet ensimmäiset maksutapahtumat, voit mukauttaa asetuksia napsauttamalla käyttöliittymän vasemmassa alareunassa olevaa hammasrataskuvaketta.

![Image](assets/fr/11.webp)

"*Näyttö*"-valikossa voit valita sovelluksen teeman, bitcoinien nimellisarvon ja paikallisen fiat-valuutan.

![Image](assets/fr/12.webp)

Kohdasta "*Maksuvaihtoehdot*" löydät erilaisia Lightning-maksujen lisäasetuksia. Voit säilyttää oletusasetukset.

![Image](assets/fr/13.webp)

Aseta kohdassa "*Kanavanhallinta*" maksimimaksu, jonka olet valmis maksamaan Lightning-kanavaa avatessasi.

![Image](assets/fr/14.webp)

Suosittelen vahvasti, että aktivoit "*Käytönvalvonta*"-valikossa todennusjärjestelmän, jolla turvataan pääsy puhelimen sovellukseen. Tämä estää ketään, jolla on pääsy lukitsemattomaan puhelimeesi, pääsemästä Phoenixiin ja varastamasta bitcoinejasi.

![Image](assets/fr/15.webp)

Jos sinulla on Electrs-palvelin, voit liittää sen "*Electrum-palvelin*"-valikossa transaktioiden lähettämistä varten.

![Image](assets/fr/16.webp)

Voit parantaa yhteyksien luottamuksellisuutta ottamalla käyttöön Tor-yhteydet "*Tor*"-valikossa. Vaikka Torin käyttäminen saattaa hieman hidastaa maksuja ja edellyttää, että Phoenix-sovellus on avoinna etualalla vastaanottamisen aikana, se lisää yksityisyyttäsi huomattavasti.

![Image](assets/fr/17.webp)

## Vastaanota bitcoineja ketjussa

Ensimmäisellä käyttökerralla voit ladata Phoenix-lompakkoon ketjussa olevia varoja. Voit myös tehdä tämän ensimmäisen talletuksen suoraan Lightningista (katso seuraava kohta), mutta kummassakin tapauksessa ensimmäisen kanavan avaamisesta peritään lisämaksuja.

Napsauta "*Vastaanottaa*"-painiketta.

![Image](assets/fr/18.webp)

Pyyhkäise QR-koodia oikealle paljastaaksesi Bitcoinin vastaanotto-osoitteen. Lähetä siihen summa, jonka haluat tallettaa Phoenixiin.

![Image](assets/fr/19.webp)

Ketjussa vastaanotettu summa näkyy ensin salkkusi saldon alla odottavana. Kestää 3 vahvistusta, ennen kuin varat ovat käytettävissä.

![Image](assets/fr/20.webp)

Kun varat on vastaanotettu, Phoenix avaa sinulle automaattisesti Lightning-kanavan. Voit nyt lähettää ja vastaanottaa bitcoineja Lightning-verkon kautta.

![Image](assets/fr/21.webp)

## Vastaanota bitcoineja Lightningin kautta

Jos haluat vastaanottaa satelliitteja Lightning-verkon kautta, napsauta "*Vastaanottaa*"-painiketta.

![Image](assets/fr/22.webp)

Phoenix luo Lightning-laskun. Voit joko skannata sen tai lähettää sen henkilölle, joka haluaa siirtää satsit sinulle.

![Image](assets/fr/23.webp)

Napsauttamalla "*Muokkaa*"-painiketta voit lisätä kuvauksen, joka näkyy maksajalle laskussa, ja määrittää tietyn summan, joka maksajan on lähetettävä.

![Image](assets/fr/24.webp)

Edellä mainittuja klassisia laskuja voi käyttää vain kerran. Voit käyttää uudelleenkäytettävää maksutapaa käyttämällä uudelleenkäytettävää QR-koodia, joka on BOLT12-tarjous.

![Image](assets/fr/25.webp)

Kun lasku tai BOLT12-tarjous on maksettu, tapahtuma näkyy Lightning-lompakossasi.

![Image](assets/fr/26.webp)

## Lähetä bitcoineja Lightningin kautta

Nyt kun sinulla on satsit Phoenixissa, voit suorittaa maksuja Lightning Networkin kautta. Aloita napsauttamalla "*lähettää*"-painiketta.

![Image](assets/fr/27.webp)

Käytettävissäsi on useita vaihtoehtoja. Klikkaamalla "*Scan QR-koodi*" voit skannata Lightning-laskun, BOLT12-tarjouksen tai jopa vastaanottoosoitteen ketjussa tapahtuvaa maksua varten.

![Image](assets/fr/28.webp)

Voit myös syöttää nämä tiedot manuaalisesti näppäimistöllä käyttöliittymän yläosassa olevaan kenttään tai syöttää Lightning-osoitteen (BOLT12 tai LNURL). Voit myös liittää tiedot suoraan "*Täytä*"-painikkeella.

![Image](assets/fr/29.webp)

Tässä esimerkissä olen skannannut 10 000 satsin laskun. Voit suorittaa maksun klikkaamalla "*Maksa*".

![Image](assets/fr/30.webp)

Kauppa on suoritettu.

![Image](assets/fr/31.webp)

Onneksi olkoon, tiedät nyt, miten Phoenixia määritetään ja käytetään. Jos löysit tämän opetusohjelman hyödylliseksi, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos jakamisesta!

Jos haluat mennä askeleen pidemmälle, tutustu tähän Alby Hubin ohjeeseen, joka on toinen innovatiivinen ja helppokäyttöinen ratkaisu oman Lightning-solmun käynnistämiseen:

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
Ja jos haluat tietää enemmän Lightning Networkin teknisestä toiminnasta, löydät Fanis Michalakisin erinomaisen ilmaisen koulutuksen Plan ₿ Networkista :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb