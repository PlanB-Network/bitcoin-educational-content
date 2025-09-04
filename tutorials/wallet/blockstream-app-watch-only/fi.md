---
name: Blockstream-sovellus - Vain katselu
description: Miten konfiguroin Watch-only wallet:n Blockstream App -sovelluksessa?
---

![cover](assets/cover.webp)


## 1. Johdanto


### 1.1 Ohjeen tavoite





- Tässä oppaassa selitetään, miten **Blockstream App** -mobiilisovelluksen **Watch-Only** -ominaisuus asetetaan ja miten sitä käytetään Bitcoin Wallet:n valvomiseen ilman pääsyä sen yksityisiin avaimiin.
- Se kattaa asennuksen, alkukonfiguraation, laajennetun julkisen avaimen tuonnin ja sen käytön saldojen ja generate-vastaanottoosoitteiden seurantaan.
- Huomautus: Liitteessä on muita opetusohjelmia, jotka käsittelevät Onchainia, Liquid:ää ja työpöytäversiota.



### 1.2. Kohdeyleisö





- Aloittelijoille**: Käyttäjät, jotka haluavat seurata Bitcoin-salkkua (joka usein liittyy Hardware Wallet:een) intuitiivisen mobiilisovelluksen avulla.
- Keskitason käyttäjät**: Henkilöt, jotka haluavat hallita vain lukusalkkuja ja käyttää yksityisyysvaihtoehtoja, kuten Tor tai SPV.
- Hardware Wallet:n omistajat**: Tarkistaa saldonsa ja generate-osoitteensa liittämättä laitettaan.
- Yritykset ja kaupat** :
 - Seuraa tapahtumia kirjanpitoa varten paljastamatta yksityisiä avaimiasi.
 - Varmentaa maksutapahtumat, jotka on vastaanotettu ilman yksityisten avainten syöttämistä verkkomaksujärjestelmiin.
 - Mahdollistaa työntekijöille generate:n uusien vastaanotto-osoitteiden käytön ilman, että heillä on pääsy yksityisiin avaimiin.
- Järjestöt ja joukkorahoitus**: Näyttäkää saldo avoimesti lahjoittajille sallimatta varojen käyttöä.



### 1.3. Vain kellonajan käyttöönotto



**Watch-Only** Wallet:n avulla voit seurata Bitcoin Wallet:n tapahtumia ja saldoa ilman, että sinulla on pääsy yksityisiin avaimiin. Toisin kuin tavanomainen Wallet, se tallentaa vain julkisia tietoja, kuten **laajennetun **julkisen avaimen** (josta syntyi **xpub**, sitten zpub, ypub jne.), jonka avulla se voi saada vastaanottoosoitteet ja seurata tapahtumahistoriaa Blockchain Bitcoin:ssä. Yksityisten avainten puuttuminen tekee mahdottomaksi varojen maksamisen sovelluksesta, mikä takaa paremman turvallisuuden.



![image](assets/fr/10.webp)



**Miksi käyttää Watch-only wallet:aa?





- Turvallisuus**: **Hardware Wallet**:llä suojatun portfolion valvontaan ilman, että liitetyn laitteen yksityiset avaimet paljastuvat.
- Mukavuus**: Hardware Wallet:tä kytkemättä voit tarkistaa saldon ja generate:n uudet vastaanottajaosoitteet.
- Luottamuksellisuus**: Yhteensopiva sellaisten vaihtoehtojen kanssa kuin **Tor** tai **SPV**, joilla rajoitetaan riippuvuutta kolmannen osapuolen palvelimista.
- Käyttötapaukset**: Varojen seuranta liikkeellä, osoitteiden luominen maksujen vastaanottamista varten tai tapahtumien varmentaminen ilman yksityisten avainten vaarantamista.



![image](assets/fr/01.webp)



### 1.4. Laajennetut julkiset avaimet



**laajennettu julkinen avain** (xpub, ypub, zpub jne.) on Bitcoin Wallet:sta johdettu tieto, joka tuottaa kaikki julkiset ala-avaimet ja niihin liittyvät vastaanotto-osoitteet antamatta pääsyä yksityisiin avaimiin.





- Miten se toimii** : Laajennettu julkinen avain luodaan seed-lauseesta deterministisen prosessin avulla (BIP-32). Se luo hierarkkisen puun julkisista lapsiavaimista, joista jokainen voidaan muuntaa vastaanottavaksi Address-avaimeksi. Käyttämällä samaa johdannaispolkua (esim. `m/44'/0'/0'/0'`) kuin valvottu Wallet, Watch-only wallet tuottaa samat osoitteet, jolloin varoja voidaan seurata ja uusia vastaanotto-osoitteita luoda.



![image](assets/fr/11.webp)





- Laajennetut julkiset avaintyypit
 - xpub**: Käytetään Legacy-salkuissa (osoitteet alkavat "1", BIP-44) ja Taproot-salkuissa (osoitteet alkavat "bc1p", BIP-86).
 - ypub**: Suunniteltu yhteensopiville SegWit-lompakoille (osoitteet alkavat "3", BIP-49).
 - zpub**: Liittyy natiiviin SegWit-salkkuun (osoitteet, jotka alkavat 'bc1q', BIP-84).
 - Muut (tpub, upub, vpub jne.)**: Käytetään vaihtoehtoisia verkkoja (kuten Testnet) tai tiettyjä standardeja varten. Esimerkiksi tpub on Testnet-verkkoa varten.





- Erinomaisuus** : Valinta xpubin, ypubin tai zpubin välillä riippuu Address:n tyypistä (legacy, SegWit, Taproot tai nested SegWit) ja Wallet:n käyttämästä BIP-standardista. Tarkista lähdesalkun edellyttämä formaatti varmistaaksesi yhteensopivuuden Blockstream App -sovelluksen kanssa.





- Turvallisuus ja luottamuksellisuus** : Laajennettu julkinen avain ei ole turvallisuuden kannalta arkaluonteinen, koska se ei salli varojen käyttöä (ei pääsyä yksityisiin avaimiin). Se on kuitenkin arkaluonteinen luottamuksellisuuden kannalta, koska se paljastaa kaikki julkiset osoitteet ja niihin liittyvän tapahtumahistorian.



**Suositus**: Suojaa laajennettu julkinen avaimesi arkaluonteisena tietona.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet muistutus





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: kaikki nimet sovellukselle, joka on asennettu älypuhelimeen, tietokoneeseen tai mihin tahansa Internetiin liitettyyn laitteeseen ja jonka avulla Bitcoin Wallet:n yksityisiä avaimia voidaan hallita ja suojata.
- Toisin kuin **hardwarelompakot**, jotka tunnetaan myös nimellä **Cold-lompakot** ja jotka eristävät avaimet offline-tilassa, ohjelmistolompakot toimivat verkkoympäristössä, mikä tekee niistä haavoittuvampia tietoverkkohyökkäyksille.





- Suositeltu käyttö** :
    - Ihanteellinen Bitcoin:n kohtuullisten määrien hallintaan, erityisesti päivittäisissä liiketoimissa.
    - Sopii aloittelijoille tai käyttäjille, joilla on vain vähän varoja ja joille Hardware Wallet voi tuntua tarpeettomalta.





- Rajoitukset**: Vähemmän turvallinen suurten varojen tai pitkäaikaisten säästöjen säilyttämiseen. Valitse tässä tapauksessa Hardware Wallet.




## 2. Esittelyssä Blockstream App





- Blockstream App** on mobiili- (iOS, Android) ja työpöytäsovellus Bitcoin-salkkujen ja varojen hallintaan Liquid Network:lla. [Blockstream] (https://blockstream.com/) osti sen vuonna 2016, ja se oli aiemmin nimeltään *Green Address* ja sitten *Blockstream Green*.
- Tärkeimmät ominaisuudet** :
    - Onchain**-tapahtumat Blockchain:ssa Bitcoin:ssä.
    - Tapahtumat **Liquid**-verkossa (Sidechain nopeaan, luottamukselliseen vaihtoon).
    - Watch-only** -salkut rahastojen seurantaan ilman pääsyä avaimiin.
    - Tietosuojavaihtoehdot: yhteys **Torin** kautta, yhteys **persoonalliseen solmuun** Electrumin kautta tai **SPV**-varmistus, jolla vähennetään riippuvuutta kolmannen osapuolen solmuista.
    - Toiminnot **Replace-by-fee (RBF)** vahvistamattomien tapahtumien nopeuttamiseksi.
- Yhteensopivuus**: **Blockstream Jade**.
- Interface**: Intuitiivinen aloittelijoille, edistyneet vaihtoehdot asiantuntijoille.
- Huomautus**: Tämä opas keskittyy ketjukäyttöön. Muut liitteissä olevat oppaat käsittelevät Onchainia, Watch-Onlya ja työpöytäversiota.




## 3. Blockstream-sovelluksen asentaminen ja määrittäminen



### 3.1. lataa





- Androidille** :
    - Lataa [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) Google Play Storesta.
    - Vaihtoehto: Asenna APK-tiedoston kautta, joka on saatavilla [Blockstreamin virallisella GitHub-sivustolla](https://github.com/Blockstream/green_android).
- IOS** :
    - Lataa [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) App Storesta.
- Huomautus**: Varmista, että lataat virallisista lähteistä, jotta vältät vilpilliset sovellukset.



### 3.2. alkukonfigurointi





- Aloitusnäyttö**: Kun sovellus avataan ensimmäisen kerran, se näyttää näytön ilman määritettyä Wallet:ta. Luodut tai tuodut portfoliot näkyvät tässä myöhemmin.



![image](assets/fr/02.webp)





- Mukauta asetuksia**: Napsauta "Sovelluksen asetukset", säädä alla olevia vaihtoehtoja, napsauta "Tallenna", käynnistä sovellus uudelleen ja luo portfoliosi.



![image](assets/fr/03.webp)



#### 3.2.1. Parannettu yksityisyys (vain Android)





- Toiminto**: Toiminto: Poistaa kuvakaappaukset käytöstä, piilottaa sovellusten esikatselukuvat Tehtävienhallinnassa ja lukitsee pääsyn, kun puhelin on lukittu.
- Miksi?** : Suojaa tietosi luvattomalta fyysiseltä käytöltä tai näytön sieppaavilta haittaohjelmilta.



#### 3.2.2. Yhteys Torin kautta





- Toiminto**: Reititä verkkoliikenne **Tor**:n, anonyymin verkon kautta, joka salaa yhteydet.
- Miksi?**: Tämä on ihanteellista, jos et luota verkkoosi (esimerkiksi julkiseen Wi-Fi-verkkoon).
- Haitta**: Voi hidastaa sovellusta salauksen takia.
- Suositus**: Aktivoi Tor, jos luottamuksellisuus on etusijalla, mutta testaa yhteyden nopeus.



#### 3.2.3. Yhteyden muodostaminen henkilökohtaiseen solmuun





- Toiminto**: Yhdistää sovelluksen omaan **täydelliseen Bitcoin-solmuun** **Electrum-palvelimen** kautta.
- Miksi?**: Tarjoaa Blockchain:n tietojen täydellisen hallinnan, mikä poistaa riippuvuuden Blockstream-palvelimista.
- Edellytys**: Konfiguroitu Bitcoin-solmu.
- Suositus**: Edistyneet käyttäjät, jotka haluavat maksimaalisen riippumattomuuden.



#### 3.2.4. SPV:n todentaminen





- Toiminto**: Käyttää **Yhdennettyä maksun todentamista (SPV)** tiettyjen Blockchain-tietojen suoraan todentamiseen lataamatta koko ketjua.
- Miksi?**: Vähentää riippuvuutta Blockstreamin oletussolmusta ja on samalla kevyt mobiililaitteille.
- Haitta**: Vähemmän turvallinen kuin Full node, koska se on riippuvainen kolmansien osapuolten solmuista joidenkin tietojen saamiseksi.
- Suositus**: Aktivoi SPV, jos et voi käyttää henkilökohtaista solmua, mutta haluat Full node:n optimaalisen turvallisuuden vuoksi.





## 4. Bitcoin "Watch-only" -salkun luominen



### 4.1. Palauta laajennettu julkinen avain



Watch-only wallet:n käyttöönottoa varten on ensin hankittava valvottavan Wallet:n laajennettu julkinen avain (xpub, ypub, zpub jne.). Nämä tiedot löytyvät yleensä ohjelmiston tai Hardware Wallet:n asetuksista tai "Wallet information" -osiosta.





- Esimerkki Blockstream-sovelluksen kanssa: Valitse Wallet:n aloitusnäytöltä "Settings", sitten "Wallet Details" ja kopioi zpub :



![image](assets/fr/09.webp)





- Vaihtoehto 1: generate lähettää laajennetun julkisen avaimen sisältävän QR-koodin, joka skannataan seuraavassa vaiheessa.
- Vaihtoehto 2: Käytä output descriptor:tä, jos Wallet tarjoaa sen.



### 4.2. tuo Wallet Watch-only





- Varoitus**: Aseta salkku yksityiseen ympäristöön, jossa ei ole kameroita tai tarkkailijoita.
- Napsauta aloitusnäytöltä "Set up a new portfolio" ja sitten "Get Started" :



![image](assets/fr/04.webp)





- Seuraava näyttö tulee näkyviin:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Luo uusi Hot Wallet. Katso lisäyksen "Blockstream App - Onchain" -opas.
- (2) **"Palauta varmuuskopiosta "**: Tuo olemassa oleva salkku käyttämällä Mnemonic-lauseen (12 tai 24 sanaa). Varoitus: Älä tuo lausetta Cold Wallet:sta, koska se paljastuu liitetyssä laitteessa, mikä mitätöi sen suojauksen.
- (3) **"Watch-Only "**: vaihtoehto, josta olemme kiinnostuneita tässä opetusohjelmassa.





- Valitse sitten "**Yksittäinen allekirjoitus**" ja "**Bitcoin**"-verkko:



![image](assets/fr/12.webp)





- Liitä laajennettu julkinen avain (xpub, ypub, zpub jne.), skannaa vastaava QR-koodi tai syötä output descriptor. Vaikka sovellus määrittäisi "xpub", myös avaimet ypub, zpub jne. ovat valtuutettuja. Napsauta sitten "Connect":



![image](assets/fr/13.webp)




### 4.3. Wallet Watch-only -laitteen käyttäminen



Tuonnin jälkeen Watch-only wallet näyttää laajennetusta julkisesta avaimesta johdettujen osoitteiden kokonaissaldon ja tapahtumahistorian. Ainoastaan ketjun sisäiset tapahtumat ovat näkyvissä (Liquid-tapahtumia ei oteta huomioon). Jos haluat seurata Liquid Wallet:a, toista tuonti valitsemalla "Liquid" edellisessä vaiheessa.





- Saldon ja tapahtumahistorian tarkastelu**: Aloitusnäytöltä voit tarkastella kokonaissaldoa ja tapahtumahistoriaa:



![image](assets/fr/14.webp)





- generate a vastaanottaa Address**: Klikkaa "Transact" ja sitten "Receive" luodaksesi uuden ketjussa olevan Address:n. Jaa se QR-koodilla tai kopioi se varojen vastaanottamiseksi:



![image](assets/fr/15.webp)





- Lähetä varoja**: Klikkaa **"Transact "** ja sitten **"Send "**. Voit syöttää :
 - Vastaanottajan Address.
 - Tapahtuman määrä.
 - Transaktiomaksut.



Koska Watch-only wallet ei kuitenkaan pidä hallussaan yksityisiä avaimia, et voi lähettää varoja suoraan. Voit allekirjoittaa maksutapahtuman yhdistämällä Hardware Wallet- tai Exchange PSBT-laitteesi skannaamalla QR-koodit (tämä vaihtoehto on käytettävissä esimerkiksi Coldcard Q:ssa).



![image](assets/fr/16.webp)





- Huomautus**: Tarkista aina vastaanottava Address ja tapahtuman tiedot virheiden välttämiseksi. Väärään Address:een lähetettyjä varoja ei voida periä takaisin.




## Liitteet



### A1. Muut Blockstream-sovelluksen opetusohjelmat





- Onchain-verkon käyttäminen :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Liquid Network:n käyttäminen :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Työpöytäversio :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Laajennetut julkiset avaimet





- Sanasto :
 - [Laajennetut julkiset avaimet](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurssi :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Parhaat käytännöt



Jos haluat käyttää **Blockstream-sovellusta** turvallisesti ja tehokkaasti, noudata seuraavia suosituksia. Ne auttavat sinua suojaamaan varojasi, optimoimaan tapahtumia ja säilyttämään luottamuksellisuutesi **Bitcoin (onchain)**, **Liquid** ja **Lightning**-verkoissa.





- Turvaa palautuslausekkeesi** :
 - Tutorial: Mnemonic-lauseen tallentaminen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Käytä suojattua todennusta** :
 - Ota käyttöön **vahva PIN-koodi** tai **biometrinen tunnistus** (sormenjälki tai kasvojentunnistus) sovelluksen käytön suojaamiseksi.
 - Älä koskaan jaa PIN-koodia tai biometrisiä tietoja.





- Suojaa yksityisyytesi** :
 - generate uusi Address kutakin ketjussa olevaa tai Liquid-vastaanottoa varten, jotta Blockchain:n jäljitystä voidaan rajoittaa.
 - Aktivoi "Enhanced Privacy", "Tor" ja "SPV" -toiminnot.
 - Jos haluat maksimaalisen luottamuksellisuuden, yhdistä Wallet omaan Bitcoin-solmuun Electrum-palvelimen kautta sen sijaan, että käyttäisit julkista solmua





- Valitse tarpeisiisi parhaiten sopiva verkko** :
 - Onchain**: (palkkiot ovat vähäisiä suhteessa määrään).
 - Liquid**: Käytä nopeisiin, edullisiin siirtoihin, joissa on parempi luottamuksellisuus.
 - Salama**: Valitse välittömät, edulliset siirrot pienille summille.





- Tarkista aina toimitusosoitteet** :
 - Tarkista Address huolellisesti ennen varojen lähettämistä. Väärään Address:een lähetetyt varat menetetään lopullisesti. Käytä kopiointia/liittämistä tai QR-koodin skannausta, älä koskaan kopioi/muuta Address:ta käsin.





- Optimoi kustannukset** :
 - Valitse ketjutapahtumille sopivat maksut (hidas, keskitasoinen, nopea) kiireellisyyden ja verkon ruuhkautumisen mukaan.
 - Käytä Liquid:a tai Lightningia pieniin määriin.





- Pidä hakemus ajan tasalla




### A4. Lisäresurssit





- Viralliset Blockstream-linkit:**
 - [Virallinen verkkosivusto](https://blockstream.com/)**
 - [Tuki mobiilisovellukselle](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentaatio ja chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Kortteleiden tutkijat :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Salama: **[1ML (Lightning Network)](https://1ml.com/)**





 - Oppiminen ja opetusohjelmat:** **[Plan ₿ Network](https://planb.network/)** :
  - Elvytyslausekkeen turvaaminen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Sanasto](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Sanasto](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
