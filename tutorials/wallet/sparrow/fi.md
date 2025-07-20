---
name: Varpunen Wallet
description: Sparrow Wallet:n asentaminen, konfigurointi ja käyttö
---
![cover](assets/cover.webp)

Sparrow Wallet on Craig Rawin kehittämä Bitcoin-salkunhallintaohjelmisto. Tämä avoimen lähdekoodin ohjelmisto on bitcoin-käyttäjien arvostama sen monien ominaisuuksien ja intuitiivisen Interface:n vuoksi.

Sparrow'ta voi käyttää kahdella tavalla:


- Kuten Hot Wallet, jossa yksityiset avaimesi on tallennettu tietokoneellesi.
- Cold:n Wallet:n hallinnoijana, kun yksityisiä avaimia säilytetään Hardware Wallet:ssä. Tässä tilassa Sparrow käsittelee vain julkisia Wallet-tietoja, seuraa varoja, luo osoitteita ja luo tapahtumia, mutta Hardware Wallet:n allekirjoitus vaaditaan, jotta nämä tapahtumat olisivat voimassa. Näin ollen se voi korvata Ledger Liven tai Trezor Suiten kaltaiset sovellukset.

Sparrow tukee yhden ja usean allekirjoituksen lompakoita ja mahdollistaa useiden lompakoiden sujuvan hallinnan. Voit esimerkiksi hallita samanaikaisesti yhtä Wallet:ta, joka on yhdistetty Ledger:een, toista Trezoriin ja myös Hot Wallet:ta.

Ohjelmisto tarjoaa myös kehittyneitä kolikoiden valvontaominaisuuksia, joiden avulla voit valita tarkasti, mitä UTXO-yksiköitä käytät transaktioissasi luottamuksellisuuden optimoimiseksi.

Yhteyden osalta Sparrow antaa sinun muodostaa yhteyden omaan Bitcoin-solmuun joko etänä Electrum-palvelimen kautta tai Bitcoin Core -palvelimella. On myös mahdollista käyttää julkista solmua, jos sinulla ei vielä ole omaa solmua. Etäyhteydet muodostetaan Torin kautta.

## Asenna Sparrow Wallet

Siirry [Sparrow Wallet:n viralliselle lataussivulle] (https://sparrowwallet.com/download/) ja valitse käyttöjärjestelmääsi vastaava ohjelmistoversio.

![Image](assets/fr/01.webp)

On tärkeää tarkistaa ohjelmiston eheys ja aitous ennen sen asentamista. Jos et tiedä, miten tämä tehdään, löydät täydellisen ohjeen täältä :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kun Sparrow on asennettu, voit ohittaa ensimmäiset selittävät näytöt ja siirtyä suoraan yhteydenhallintanäyttöön.

![Image](assets/fr/02.webp)

## Yhteyden muodostaminen Bitcoin-verkkoon

Jotta Sparrow voi olla yhteydessä Bitcoin-verkkoon ja lähettää tapahtumia, sen on oltava yhteydessä Bitcoin-solmuun. Yhteys voidaan muodostaa kolmella eri tavalla:


- 🟡 Julkisen solmun käyttäminen, eli yhteyden muodostaminen kolmannen osapuolen solmuun, joka sallii tällaiset yhteydet. Jos sinulla ei ole omaa Bitcoin-solmua, tämän vaihtoehdon avulla pääset nopeasti alkuun Sparrow'n kanssa. Solmu, johon muodostat yhteyden, näkee kuitenkin kaikki tapahtumasi, mikä voi vaarantaa luottamuksellisuutesi. Avainten hallinta on tärkeää, mutta oma solmu on vielä parempi. Käytä tätä vaihtoehtoa siis vain, jos olet vasta aloittamassa ja olet tietoinen yksityisyyteesi kohdistuvista riskeistä.
- 🟢 Yhteyden muodostaminen Bitcoin Core -solmuun. Jos sinulla on oma Bitcoin Core -solmu, voit liittää sen Sparrow Wallet:een joko paikallisesti, jos Bitcoin Core on asennettu samaan koneeseen, tai etänä.
- 🔵 Yhteys Electrum-palvelimen kautta. Jos Bitcoin-solmusi on varustettu Electrilla, kuten esimerkiksi Umbrelin tai Start9:n kaltaisissa node-in-a-box -ratkaisuissa, voit muodostaa siihen yhteyden etänä Sparrow'sta.

**On suositeltavaa käyttää Electrs- tai Bitcoin Core -yhteyttä omassa solmussasi, jotta vähennät tarvetta luottaa kolmanteen osapuoleen ja optimoit luottamuksellisuuden**

### Yhteys julkiseen solmuun 🟡

Yhteyden muodostaminen julkiseen solmuun on hyvin yksinkertaista. Napsauta "*Julkinen palvelin*"-välilehteä.

![Image](assets/fr/03.webp)

Valitse solmu avattavasta luettelosta.

![Image](assets/fr/04.webp)

Napsauta sitten "*Testiyhteys*".

![Image](assets/fr/05.webp)

Kun yhteys on muodostettu, Sparrow Wallet näyttää keltaisen rastin Interface:n oikeassa alakulmassa osoituksena siitä, että olet yhteydessä julkiseen solmuun.

![Image](assets/fr/06.webp)

### Kytkeminen Bitcoin-ytimeen 🟢

Toinen tapa muodostaa yhteys Bitcoin-solmuun on yhdistää Sparrow Bitcoin Coreen. Jos Bitcoin Core on asennettu samaan koneeseen, todennus tapahtuu evästetiedoston avulla. Jos Bitcoin Core on etäkoneessa, sinun on käytettävä salasanaa, joka on määritelty `Bitcoin.conf`-tiedostossa.

Huomaa, että jos käytät karsittua Bitcoin Core-solmua, et voi palauttaa Wallet:ää, joka sisältää tapahtumia, jotka edeltävät paikallisesti tallennettuja lohkoja. Sparrow'lla luodun uuden Wallet:n kohdalla tämä ei kuitenkaan ole ongelma: uudet tapahtumat näkyvät, vaikka solmu olisi karsittu.

Bitcoin Core -solmun konfiguroimiseksi voit tutustua johonkin seuraavista ohjeista käyttöjärjestelmästäsi riippuen:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Siirry Sparrow'ssa välilehdelle "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

Jos Bitcoin Core on asennettu tietokoneellesi, etsi Bitcoin.conf-tiedosto ohjelmistotiedostojen joukosta. Jos tätä tiedostoa ei ole olemassa, voit luoda sen. Avaa se tekstieditorilla ja lisää seuraava rivi:

```ini
server=1
```

Tallenna sitten muutokset.

Voit tehdä tämän myös Bitcoin-QT:n Interface-grafiikan kautta siirtymällä kohtaan "*Asetukset*" > "*Options...*" ja aktivoi vaihtoehto "*Enable RPC server*".

Muista käynnistää ohjelmisto uudelleen näiden muutosten tekemisen jälkeen.

![Image](assets/fr/08.webp)

Palaa sitten Sparrow Wallet:een ja syötä evästetiedoston polku, joka sijaitsee yleensä samassa kansiossa kuin `Bitcoin.conf`, käyttöjärjestelmästäsi riippuen:

| **macOS** | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Jätä muut parametrit oletusarvoisiksi, URL `127.0.0.1` ja portti `8332`, ja napsauta sitten "*Testausyhteys*".

![Image](assets/fr/10.webp)

Yhteys on muodostettu. Oikeaan alakulmaan ilmestyy Green-merkki, joka osoittaa, että olet yhteydessä Bitcoin Core -solmuun.

![Image](assets/fr/11.webp)

**With Bitcoin Core remote:**

Jos Bitcoin Core on asennettu toiseen koneeseen, joka on liitetty samaan verkkoon, etsi ensin Bitcoin.conf-tiedosto ohjelmistotiedostojen joukosta. Jos tätä tiedostoa ei vielä ole, voit luoda sen. Avaa tämä tiedosto tekstieditorilla ja lisää seuraava rivi:

```ini
server=1
```

Kun olet muokannut tiedostoa, varmista, että tallennat sen käyttöjärjestelmääsi sopivaan kansioon:

| **macOS** | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin | ~/.Bitcoin |

Tämä toiminto voidaan suorittaa myös Bitcoin-QT Interface:n graafisen Interface:n kautta. Siirry "*Settings*"-valikkoon, sitten "*Options...*" ja aktivoi "*Enable RPC server*"-vaihtoehto merkitsemällä vastaava ruutu. Jos `Bitcoin.conf`-tiedostoa ei ole olemassa, voit luoda sen suoraan tästä Interface:stä napsauttamalla "*Open Configuration File*".

![Image](assets/fr/12.webp)

Etsi Bitcoin Corea isännöivän koneen IP Address lähiverkosta. Voit tehdä tämän käyttämällä työkalua, kuten [Angry IP Scanner](https://angryip.org/). Oletetaan, että solmusi IP Address on `192.168.1.18`.

Lisää seuraavat rivit tiedostoon `Bitcoin.conf` ja aseta `rpcbind=192.168.1.18` vastaamaan solmusi IP Address:ää.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Lisää Bitcoin.conf-tiedostoon käyttäjätunnus ja salasana etäyhteyksiä varten. Muista korvata `loic` käyttäjänimelläsi ja `my_password` vahvalla salasanalla:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Kun olet muuttanut ja tallentanut tiedoston, käynnistä Bitcoin-QT-ohjelmisto uudelleen.

Voit nyt palata Sparrow Wallet:ään. Siirry "*Käyttäjä / Pass*" -välilehdelle. Kirjoita käyttäjätunnus ja salasana, jotka olet määrittänyt Bitcoin.conf-tiedostossa. Jätä muut parametrit oletusarvoisiksi, eli URL-osoite `127.0.0.0.1` ja portti `8332`. Napsauta sitten "*Test Connection*".

![Image](assets/fr/15.webp)

Yhteys on muodostettu. Oikeaan alakulmaan ilmestyy Green-merkki, joka osoittaa, että olet yhteydessä Bitcoin Core -solmuun.

![Image](assets/fr/16.webp)

### Yhteyden muodostaminen Electrum-palvelimeen 🔵

Viimeinen vaihtoehto yhteyden muodostamiseen on käyttää Electrumin etäpalvelinta. Tämän menetelmän avulla voit muodostaa yhteyden solmuun Torin kautta toisesta laitteesta ja hyödyntää indeksointia, jotta voit selata salkkujasi Sparrow'ssa nopeammin. Se sopii erityisen hyvin, jos käytössäsi on Umbrelin tai Start9:n kaltainen node-in-a-box -ratkaisu, jonka avulla voit asentaa Electrumin yhdellä napsautuksella.

Tätä varten hanki Electrum-palvelimesi Tor `.onion' Address. Esimerkiksi Umbrelissa löydät sen Electrsovelluksesta.

![Image](assets/fr/17.webp)

Siirry Sparrow Wallet:ssa välilehdelle "*Private Electrum*".

![Image](assets/fr/18.webp)

Kirjoita Tor Address -numerosi sille varattuun tilaan. Muut asetukset voivat jäädä oletusasetuksiksi. Napsauta sitten "*Testaa yhteys*".

![Image](assets/fr/19.webp)

Yhteys on vahvistettu. Jos suljet tämän ikkunan, oikeaan alakulmaan ilmestyy sininen rasti, joka osoittaa, että olet yhteydessä Electrum-palvelimeen.

![Image](assets/fr/20.webp)

## Luo lämmin salkku

Nyt kun Sparrow Wallet on konfiguroitu kommunikoimaan Bitcoin-verkon kanssa, olet valmis luomaan ensimmäisen Wallet:n. Tässä osiossa opastetaan Hot Wallet:n eli sellaisen Wallet:n luominen, jonka yksityiset avaimet on tallennettu tietokoneellesi. Koska tietokoneesi on monimutkainen kone, joka on yhteydessä Internetiin, se muodostaa erittäin suuren hyökkäyspinnan. Näin ollen Hot Wallet:ää tulisi käyttää vain rajoitettuihin määriin bitcoineja. Jos haluat säilyttää suurempia määriä, valitse turvallinen Wallet ja Hardware Wallet. Jos etsit tätä, voit siirtyä seuraavaan osioon.

Voit luoda Hot Wallet:n napsauttamalla Sparrow Wallet:n aloitusnäytöstä välilehteä "*Tiedosto*" ja sitten "*Uusi Wallet*".

![Image](assets/fr/21.webp)

Anna salkulle nimi ja napsauta "*Luo Wallet*".

![Image](assets/fr/22.webp)

Interface:n yläreunassa voit valita, haluatko luoda "*Single Signature*"- vai "*Multi Signature*"-salkun. Heti sen alapuolella voit valita UTXO:iden lukitsemiseen käytettävän käsikirjoitustyypin. Suosittelen käyttämään uusinta standardia: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Napsauta sitten "*Uusi tai tuotu Software Wallet*".

![Image](assets/fr/24.webp)

Valitse BIP39-standardi, sillä sitä tukevat lähes kaikki Bitcoin-salkun ohjelmistot. Valitse seuraavaksi palautuslausekkeen pituus. Tällä hetkellä 12-sanainen lauseke on riittävä, sillä molemmat tarjoavat samanlaisen turvallisuuden, mutta 12-sanainen lauseke on helpompi tallentaa.

![Image](assets/fr/25.webp)

Napsauta "*generate New*"-painiketta generate Wallet:n Mnemonic-lauseen generate:n käyttämiseksi. Tämä lauseke antaa täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä tietokoneeseesi.

12-sanainen lause palauttaa pääsyn bitcoineihisi, jos tietokoneesi katoaa, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kaivertaa sen paperille tai, jos haluat lisätä turvallisuutta, kaiverruttaa sen ruostumattomaan teräkseen, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta. Väliaineen valinta Mnemonic:lle riippuu turvallisuusstrategiastasi, mutta jos käytät Sparrow'ta lämpimänä Wallet:tä, joka sisältää kohtuullisia määriä, paperin pitäisi riittää.

Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseesi, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Ei näitä sanoja saa tietenkään koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet käytetään vain Testnet:lla ja se poistetaan opetusohjelman lopussa.**

Voit myös lisätä passphrase BIP39:n napsauttamalla "*Käytä passphrase:tä*"-ruutua. Varoitus: passphrase:n käyttäminen voi olla erittäin hyödyllistä, mutta jos et ymmärrä, miten se toimii, se voi olla hyvin riskialtista. Siksi kehotan sinua lukemaan tämän lyhyen teoreettisen artikkelin aiheesta:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kun olet tallentanut Mnemonic:n ja kaikki passphrase:t fyysiselle tietovälineelle, napsauta "*Vahvista varmuuskopiointi*".

![Image](assets/fr/27.webp)

Kirjoita 12 sanaa uudelleen varmistaaksesi, että ne on tallennettu oikein, ja napsauta sitten "*Luo avainsäilö*".

![Image](assets/fr/28.webp)

Napsauta sitten "*Import Keystore*" generate salkun avaimia Mnemonic lauseesta.

![Image](assets/fr/29.webp)

Napsauta "*Apply*" viimeistelläksesi salkun luomisen.

![Image](assets/fr/30.webp)

Aseta vahva salasana, jolla varmistat pääsyn Sparrow-salkkuusi. Salasana kannattaa säilyttää salasanahallinnassa, jotta et unohda sitä. Huomaa, että salasanalla ei ole merkitystä avainten muodostamisessa. Sitä käytetään vain Wallet:n käyttämiseen Sparrow Wallet:n kautta. Joten ilman tätä salasanaa Mnemonic-lauseesi riittää käyttämään bitcoinejasi mistä tahansa BIP39-yhteensopivasta sovelluksesta.

![Image](assets/fr/31.webp)

Hot Wallet on nyt luotu. Voit siirtyä tämän ohjeen *Bitcoinien vastaanottaminen* -osioon, jos et aio käyttää Hardware Wallet:ta Sparrow'n kanssa.

## Cold-salkun hallinta

Toinen tapa käyttää Sparrow Wallet:a on määrittää se salkunhoitajaksi Hardware Wallet:n kanssa. Tässä kokoonpanossa Bitcoin Wallet:n yksityiset avaimet pysyvät yksinomaan Hardware Wallet:ssa, kun taas Sparrow pääsee käsiksi vain julkisiin tietoihin. Tämä lähestymistapa tarjoaa korkeamman turvallisuustason kuin edellä käsitellyt Hot-lompakot, sillä yksityiset avaimet säilytetään erikoistuneessa laitteessa, jossa on usein suojattu siru ja joka ei ole yhteydessä Internetiin ja joka näin ollen muodostaa paljon pienemmän hyökkäyspinnan kuin perinteinen tietokone.

Hardware Wallet voidaan liittää Sparrowiin kahdella tavalla:


- Kaapelilla, jota käytetään yleisesti aloittelevan tason malleissa, kuten Trezor Safe 3 tai Ledger Nano S Plus ;
- Air-Gap-tilassa, eli ilman suoraa langallista yhteyttä, MicroSD-kortin tai QR-koodin Exchange avulla.

Sparrow tukee kaikkia näitä viestintämenetelmiä ja on yhteensopiva useimpien markkinoilla olevien laitteistolompakoiden kanssa.

Tässä ohjeessa käytän Ledger Nano S:ää, jossa on kaapeli, mutta menettely on samanlainen Air-Gap-tilassa. Löydät Hardware Wallet:aa koskevat yksityiskohdat Plan ₿ Network:ää koskevasta oppaasta.

Varmista ennen aloittamista, että Wallet on jo määritetty Hardware Wallet:een. Jos käytät langallista yhteyttä, liitä se tietokoneeseen kaapelilla.

Jos haluat tuoda niin sanotun "*Keystore*"-tietokannan (salkun hallintaan tarvittavat julkiset tiedot) Sparrow Wallet:aan, napsauta välilehteä "*File*" ja sitten "*New Wallet*".

![Image](assets/fr/32.webp)

Nimeä salkkusi ja napsauta "*Luo Wallet*". Suosittelen, että kirjoitat Hardware Wallet:n nimen, jotta se on helppo tunnistaa myöhemmin.

![Image](assets/fr/33.webp)

Valitse Interface:n yläosassa "*Single Signature*"- tai "*Multi Signature*"-salkku. Esimerkkiämme varten konfiguroimme yhden allekirjoituksen salkun.

Valitse alapuolelta UTXO:n lukitsemiseen tarkoitettu skriptityyppi. Jos Hardware Wallet tukee sitä, suosittelen valitsemaan "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Seuraavaksi menettely vaihtelee yhteysmenetelmän mukaan. Jos käytät Air-Gap-menetelmää, valitse "*Airgapped Hardware Wallet*". Noudata sitten laitekohtaisia ohjeita.

![Image](assets/fr/35.webp)

Jos käytät kaapeliyhteyttä, kuten minun tapauksessani, valitse "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Napsauta "*Scan*", jotta Sparrow havaitsee laitteesi. Varmista, että laite on kytketty ja lukitus on avattu. Joissakin malleissa, kuten Ledger, sinun on avattava "*Bitcoin*"-sovellus, jotta laite havaitaan.

![Image](assets/fr/37.webp)

Valitse "*Import Keystore*".

![Image](assets/fr/38.webp)

Napsauta "*Apply*" viimeistelläksesi salkun luomisen.

![Image](assets/fr/39.webp)

Aseta vahva salasana Sparrow Wallet:n käytön turvaamiseksi. Tämä salasana suojaa julkiset avaimet, osoitteet ja tapahtumahistorian. Suosittelemme, että tallennat sen salasanan salasanahallintaan. Huomaa, että tämä salasana ei vaikuta avainten johtamiseen. Ilman sitäkin voit saada bitcoinisi takaisin Mnemonic:lläsi minkä tahansa BIP39-yhteensopivan ohjelmiston avulla.

![Image](assets/fr/40.webp)

Hallintasalkkusi on nyt määritetty Sparrow'ssa.

![Image](assets/fr/41.webp)

## Vastaanottaa bitcoineja

Nyt kun Wallet on määritetty Sparrowiin, voit vastaanottaa bitcoineja. Siirry yksinkertaisesti "*Vastaanottaa*"-valikkoon.

![Image](assets/fr/42.webp)

Sparrow näyttää ensimmäisen käyttämättömän Address:n Wallet:ssa. Voit lisätä tähän Address:een "*Label*", joka muistuttaa sinua tulevaisuudessa näiden satoshien alkuperästä.

![Image](assets/fr/43.webp)

Jos käytät Hot Wallet:tä, näytettyä Address:ää voidaan käyttää välittömästi joko kopioimalla se tai skannaamalla siihen liittyvä QR-koodi.

Jos käytät Hardware Wallet:ää, on erittäin tärkeää tarkistaa Address laitteen näytöltä ennen käyttöä. Jos käytät langallisia laitteita, kytke Hardware Wallet ja avaa lukitus ja napsauta sitten Sparrowissa "*näytä Address*". Varmista, että Hardware Wallet-laitteessa näkyvä Address vastaa Sparrow'ssa näkyvää Address:ta.

![Image](assets/fr/44.webp)

Hardware Wallet Air-Gap -käyttäjille Address-varmennus vaihtelee laitemallin mukaan. Katso tarkat ohjeet Plan ₿ Network-oppaasta.

Kun maksaja on lähettänyt maksutapahtuman, näet sen "*Tapahtumat*"-välilehdellä. Voit napsauttaa sitä saadaksesi lisätietoja, kuten txid:n.

![Image](assets/fr/45.webp)

Välilehdellä "*Addressit*" on luettelo kaikista postilaatikko-osoitteistasi. Näet, onko niitä jo käytetty ja onko niihin lisätty tarra. *Vastaanottaa*" -osoitteet ovat osoitteita, jotka Sparrow näyttää, kun napsautat "*Vastaanottaa*", ja ne on tarkoitettu saapuvia maksuja varten. "*Vaihda*"-osoitteita käytetään Exchange:n tapahtumissasi, eli UTXO:n käyttämättömän osan takaisin saamiseksi tuloissa.

![Image](assets/fr/46.webp)

"*UTXOs*"-välilehdellä näet kaikki UTXOt, eli hallussasi olevat Bitcoin-fragmentit. Näet kunkin UTXO:n määrän ja siihen liittyvän merkinnän.

![Image](assets/fr/47.webp)

## Lähetä bitcoineja

Nyt kun sinulla on Wallet:ssa muutama satelliitti, voit myös lähettää niitä. Vaikka tähän on useita tapoja, suosittelen, että käytät "*UTXOs*"-valikkoa, jotta voit tarkemmin hallita käyttämiäsi kolikoita (*coin control*), sen sijaan että menisit suoraan "*Send*"-valikkoon (vaikka jälkimmäinen voi riittää, jos olet aloittelija).

![Image](assets/fr/48.webp)

Valitse UTXO:t, joita haluat käyttää tämän tapahtuman syötteinä, ja napsauta sitten "*Send Selected*". Tämän lähestymistavan avulla voit valita UTXO-tietueistasi sopivimmat lähteet kulujesi ja niiden vastaanottamisen yhteydessä käytettävien merkintöjen mukaan, jotta maksujen luottamuksellisuus voidaan optimoida. Varmista, että valittujen UTXO:iden summa on suurempi kuin summa, jonka haluat lähettää.

![Image](assets/fr/49.webp)

Kirjoita vastaanottajan Address-koodi kenttään "*Maksajalle*". Voit myös skannata Address:n webbikameralla napsauttamalla kamerakuvaketta. "*+Lisää*"-painikkeella voit maksaa useita osoitteita yhdellä tapahtumalla.

![Image](assets/fr/50.webp)

Lisää tapahtumaan etiketti, joka muistuttaa sinua sen tarkoituksesta. Tämä etiketti liitetään myös mahdolliseen Exchange:aan.

![Image](assets/fr/51.webp)

Kirjoita tähän Address:ään lähetettävä summa.

![Image](assets/fr/52.webp)

Mukauta maksua nykyisten markkinaolosuhteiden mukaan. Voit tehdä tämän syöttämällä absoluuttisen maksuarvon tai säätämällä maksua liukusäätimellä.

![Image](assets/fr/53.webp)

Interface:n alareunassa voit valita "*Tehokkuus*" ja "Yksityisyys*". Minun tapauksessani "*Privacy*"-vaihtoehto ei ole käytettävissä, koska minulla on vain yksi UTXO tässä salkussa. "*Efficiency*" vastaa klassista transaktiota, kun taas "*Privacy*" on Stonewall-tyyppinen transaktio, transaktiorakenne, joka vahvistaa luottamuksellisuuttasi simuloimalla mini-CoinJoin:tä, mikä tekee ketjuanalyysistä monimutkaisempaa.

![Image](assets/fr/54.webp)

Sparrow näyttää yhteenvetokaavion, jossa näkyvät panokset, tuotokset ja transaktiomaksut (huomaa, että maksut eivät ole tuotos, toisin kuin kaavio antaa ymmärtää). Jos olet tyytyväinen kaikkeen, napsauta "*Create Transaction*".

![Image](assets/fr/55.webp)

Tämä vie sinut sivulle, jossa kerrotaan yksityiskohtaisesti tapahtuman Elements. Tarkista, että kaikki tiedot ovat oikein, ja napsauta sitten "*Finalize Transaction for Signing*".

![Image](assets/fr/56.webp)

On tärkeää säilyttää oletusarvoinen Sighash. Jos haluat ymmärtää, miksi, katso tätä koulutusta, jossa selitän kaiken, mitä sinun on tiedettävä Sighashista:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Seuraavassa näytössä vaihtoehdot vaihtelevat käyttämäsi Wallet:n tyypin mukaan:


- Hardware Wallet Air-Gapin osalta napsauta "*Show QR*" näyttääksesi PSBT:n, jonka voit allekirjoittaa laitteellasi, ja lataa sitten allekirjoitettu PSBT Sparrowiin käyttämällä "*Scan QR*". "*Save Transaction*" -vaihtoehto toimii samalla tavalla, mutta vaihtojen kanssa microSD-kortilla ;
- Jos kyseessä on Hot Wallet, napsauta "*Sign*" ja anna Wallet-salasana allekirjoitusta varten;
- Jos kyseessä on langallinen Hardware Wallet, voit myös lähettää allekirjoittamattoman tapahtuman laitteeseesi napsauttamalla "*Sign*".

![Image](assets/fr/57.webp)

Tarkista Hardware Wallet:stä vastaanottajan Address, lähetetty summa ja maksut. Jos kaikki on oikein, jatka allekirjoittamista.

Kun transaktio on allekirjoitettu, se ilmestyy uudelleen Sparrow'hun ja on valmis lähetettäväksi Bitcoin-verkkoon, jotta se voidaan myöhemmin sisällyttää lohkoon. Jos kaikki on oikein, napsauta "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Tapahtumasi on nyt lähetetty ja odottaa vahvistusta.

![Image](assets/fr/59.webp)

## Salkkujen hallinta ja määrittäminen Sparrow'ssa

"*Asetukset*"-välilehdeltä löydät yksityiskohtaisia tietoja salkustasi, kuten :


- Salkkutyyppi (single-sig tai multi-sig) ;
- Käytetty käsikirjoitustyyppi ;
- Nimi, jonka olet antanut salkulle ;
- Pääavaimen painatus;
- Ohitusreitti ;
- Tilin laajennettu julkinen avain.

![Image](assets/fr/60.webp)

"*Vie*"-painikkeella voit viedä salkun tiedot, jotta voit käyttää niitä muissa ohjelmissa säilyttäen samalla Sparrow'ssa määritetyt tiedot.

"*Lisää tili*"-painikkeella voit lisätä salkkuusi uuden tilin. Tili vastaa erillistä postilaatikon osoitekokonaisuutta. Tämä toiminto voi olla hyödyllinen esimerkiksi silloin, jos haluat erottaa henkilökohtaisen ja yritystilin toisistaan yhdellä Mnemonic-lauseella.

"*Advanced*"-painikkeella pääset lisäasetuksiin, kuten Sparrow'n Address-haun mukauttamiseen ja salkun salasanan vaihtamiseen.

![Image](assets/fr/61.webp)

Kun suljet Sparrow Wallet:n, Wallet lukittuu automaattisesti. Kun avaat ohjelmiston seuraavan kerran, ikkuna kehottaa sinua avaamaan Wallet:n lukituksen salasanalla.

![Image](assets/fr/62.webp)

Jos tämä ikkuna ei avaudu tai jos haluat avata toisen salkun Sparrow'ssa, napsauta välilehteä "*File*" ja valitse "*Open Wallet*".

![Image](assets/fr/63.webp)

Tämä avaa tiedostonhallinnan kansioon, jossa Sparrow tallentaa lompakot. Valitse vain Wallet, jonka haluat avata, ja anna salasana avataksesi sen lukituksen.

![Image](assets/fr/64.webp)

"*Tiedosto*"-valikossa kohdassa "*Asetukset*" on Bitcoin:n verkkoyhteysparametrit, joita on jo tutkittu aiemmissa osioissa. Voit myös säätää erilaisia parametreja, kuten käytettyä yksikköä, muunnoksia varten käytettävää fiat-valuuttaa ja tietolähteitä.

![Image](assets/fr/65.webp)

"*Näkymä*"-välilehti tarjoaa mukautusvaihtoehtoja ja pääsyn joihinkin hyödyllisiin komentoihin, kuten "*Virkistä Wallet*", joka päivittää salkun tapahtumahakua.

![Image](assets/fr/66.webp)

"*Työkalut*"-välilehdelle on koottu useita kehittyneitä työkaluja, kuten :


- "*Sign/Verify Message*" (allekirjoita/varmenna viesti*) -valinnalla voit todistaa vastaanottavan Address:n hallussapidon tai vahvistaa allekirjoituksen.
- "*Lähetys monelle*" tarjoaa yksinkertaistetun Interface:n, jolla voidaan suorittaa tapahtumia useisiin vastaanottajaosoitteisiin kerralla, mikä on kätevää eräkuluja varten.
- "*Sweep Private Key*" mahdollistaa bitcoinien hakemisen yksinkertaisella yksityisellä avaimella suojattuna ja niiden siirtämisen Sparrow Wallet:een. Tämä voi olla erityisen hyödyllistä niille, joiden bitcoinit ovat peräisin 2010-luvun alusta, ennen HD-lompakoiden aikakautta.
- "Tarkista lataus" tarkistaa ladatun ohjelmiston eheyden ja aitouden ennen sen asentamista laitteeseen.
- "*Restart In*" mahdollistaa siirtymisen lompakoihin Testnet- tai Signet-verkoissa. Tämä voi olla hyödyllistä, jos haluat käyttää testiverkkoja kolikoilla, joilla ei ole todellista arvoa.

![Image](assets/fr/67.webp)

Tiedät nyt kaiken Sparrow Wallet -ohjelmistosta, joka on erinomainen työkalu Bitcoin-salkkujen päivittäiseen hallintaan.

Jos löysit tämän ohjeen hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa sen sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tätä toista opetusohjelmaa, jossa selitän, miten Hardware Wallet COLDCARD Q konfiguroidaan Sparrow Wallet:n kanssa:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3