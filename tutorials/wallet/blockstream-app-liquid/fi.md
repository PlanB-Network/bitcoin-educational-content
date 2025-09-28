---
name: Blockstream App - Liquid
description: Blockstream App -sovelluksen määrittäminen ja Liquid Network:n käyttäminen
---
![cover](assets/cover.webp)


## 1. Johdanto


### 1.1 Tutoriaalin tavoite





- Tässä ohjeessa kerrotaan, miten **Blockstream App** -mobiilisovellusta käytetään **Bitcoin Liquid** -salkun hallintaan, eli suoraan Bitcoin "Liquid" -sivuketjuun kirjattuihin transaktioihin.
- Se kattaa asennuksen, alustavan konfiguroinnin, Software Wallet:n luomisen sekä bitcoinien vastaanottamiseen ja lähettämiseen liittyvät toiminnot Liquid:ssä.
- Huomautus: Liitteissä olevat muut opetusohjelmat käsittelevät Onchain-, Watch-Only- ja työpöytäversiota.



### 1.2 Kohderyhmä





- **Aloittelijoille**: Käyttäjät, jotka haluavat hallita bitcoinejaan intuitiivisella mobiilisovelluksella, joka integroi Liquid Network:n.
- **Keskitason käyttäjät**: Ihmiset, jotka haluavat ymmärtää onchain-toimintoja ja yksityisyysvaihtoehtoja, kuten Tor tai SPV.



### 1.3 Liquid:n esittely



**Liquid** on **[Blockstream](https://blockstream.com/Liquid/)** kehittämä Bitcoin:n **Sidechain**, joka on suunniteltu tarjoamaan nopeampia, enemmän Confidential Transactions:aa ja kehittyneempiä toimintoja, mutta joka on edelleen yhteydessä Blockchain Bitcoin:een.



Sidechain on itsenäinen Blockchain, joka toimii rinnakkain Bitcoin:n kanssa käyttäen mekanismia, joka tunnetaan nimellä **kaksisuuntainen tappi**. Tämä järjestelmä lukitsee bitcoineja pää-Blockchain:ään luodakseen **Liquid-bitcoineja (L-BTC)**, jotka kiertävät Liquid Network:ssa säilyttäen samalla arvonsa alkuperäisten bitcoinien kanssa. Varat voidaan palauttaa Blockchain Bitcoin:een milloin tahansa.



![image](assets/fr/17.webp)






- (1) **Kiinnitys**: Bitcoinit (BTC) lukitaan Liquid-liiton toimesta Blockchain:n pääjärjestelmään. Vastineeksi Blockchain Liquid-ketjussa lasketaan liikkeeseen ja lähetetään käyttäjälle vastaava määrä Liquid-bitcoineja (L-BTC), jolla varmistetaan kahden ketjun välinen pariteetti.





- (2) **Riippumattomat liiketoimet**: Tapahtumia voidaan suorittaa samanaikaisesti ja itsenäisesti pääkoneissa Blockchain (BTC) ja Sidechain Liquid (L-BTC) käyttäjän tarpeiden mukaan.





- (3) **Kiinni**: Käyttäjä lähettää Liquid-bitcoineja (L-BTC) takaisin Liquid-liittoon. Tämän jälkeen liitto avaa vastaavan määrän bitcoineja (BTC) Blockchain:n pääkeskuksessa ja siirtää ne käyttäjälle.



Liquid perustuu luotettavien osallistujien (pörssit, tunnustetut Bitcoin-yritykset) **liittoon**, joka hallinnoi lohkojen validointia ja kahdenvälistä ankkurointia. Toisin kuin Blockchain Bitcoin, joka on hajautettu ja luottaa louhijoihin, Liquid on **liittoutunut** verkko, mikä tarkoittaa, että sen turvallisuus ja hallinto riippuvat näistä osallistujista. Vaikka tämä merkitsee kompromissia hajautuksesta, se mahdollistaa optimoidun suorituskyvyn ja kehittyneet toiminnot.



![image](assets/fr/18.webp)



##### Miksi käyttää Liquid:aa?





- **Nopeus**: Liquid:ssä tapahtuvat transaktiot vahvistetaan noin **1 minuutissa**, kun taas ketjussa tapahtuvissa transaktioissa aikaa kuluu 10 minuuttia tai enemmän, koska validoijien liitto luo lohkoja joka minuutti.
- **Parannettu luottamuksellisuus**: Liquid käyttää **Confidential Transactions**:tä, joka piilottaa siirrettyjen varojen määrän ja tyypin, mikä tekee transaktioista yksityisempiä (vaikka osoitteet pysyvätkin näkyvissä).
- **Alhaiset maksut**: Liquid:lla tehtävät maksut ovat yleensä edullisempia, joten ne sopivat erinomaisesti usein tehtäviin siirtoihin tai pieniin summiin.
- **Useita omaisuuseriä**: Liquid tukee L-BTC:iden lisäksi muiden digitaalisten omaisuuserien, kuten stablecoins tai tokenien, liikkeeseenlaskua erityissovelluksissa käytettäväksi.
- **Käyttötapaukset**: Liquid soveltuu erityisesti alustojen väliseen vaihtoon, nopeisiin maksuihin tai älykkäitä sopimuksia vaativiin sovelluksiin, mutta se on samalla yhteydessä Bitcoin:n turvallisuuteen.



**Huomautus: Tämä opetusohjelma keskittyy Liquid:n käyttöön Blockstream-sovelluksen kautta. Liquid Network:n perusteellista ymmärtämistä varten löydät resursseja liitteestä.**



### 1.4. Hot Wallet muistutus





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: kaikki nimitykset sovellukselle, joka on asennettu älypuhelimeen, tietokoneeseen tai mihin tahansa Internetiin liitettyyn laitteeseen ja jonka avulla Bitcoin Wallet:n yksityisiä avaimia voidaan hallita ja suojata.
- Toisin kuin **hardwarelompakot**, jotka tunnetaan myös nimellä **Cold-lompakot** ja jotka eristävät avaimet offline-tilassa, ohjelmistolompakot toimivat verkottuneessa ympäristössä, mikä tekee niistä haavoittuvampia tietoverkkohyökkäyksille.





- **Suositeltu käyttö**:
    - Ihanteellinen Bitcoin:n kohtuullisten määrien hallintaan, erityisesti päivittäisissä liiketoimissa.
    - Sopii aloittelijoille tai käyttäjille, joilla on vain vähän varoja ja joille Hardware Wallet voi tuntua tarpeettomalta.





- **Rajoitukset**: Vähemmän turvallinen suurten varojen tai pitkäaikaisten säästöjen säilyttämiseen. Valitse tässä tapauksessa Hardware Wallet.




## 2. Esittelyssä Blockstream App





- **Blockstream App** on mobiili- (iOS, Android) ja työpöytäsovellus Bitcoin-lompakoiden ja varojen hallintaan Liquid Network:ssä. [Blockstream](https://blockstream.com/) osti sen vuonna 2016, ja se oli aiemmin nimeltään *Green Address* ja sitten *Blockstream Green*.
- **Tärkeimmät ominaisuudet**:
- **Onchain-tapahtumat** Blockchain Bitcoin.
    - Tapahtumat **Liquid**-verkossa (Sidechain nopeaan ja luottamukselliseen vaihtoon).
- **Watch-only** -salkut rahastojen seurantaan ilman pääsyä avaimiin.
    - Tietosuojavaihtoehdot: yhteys **Torin** kautta, yhteys **persoonalliseen solmuun** Electrumin kautta tai **SPV**-varmistus, jolla vähennetään riippuvuutta kolmannen osapuolen solmuista.
    - Toiminnot **Replace-by-fee (RBF)** vahvistamattomien tapahtumien nopeuttamiseksi.
- **Yhteensopivuus**: **Blockstream Jade**.
- **Interface**: Intuitiivinen aloittelijoille, edistyneet vaihtoehdot asiantuntijoille.
- **Huomautus**: Tämä opas keskittyy ketjukäyttöön. Muut liitteissä olevat oppaat käsittelevät Onchainia, Watch-Onlya ja työpöytäversiota.




## 3. Blockstream-sovelluksen asentaminen ja määrittäminen



### 3.1. lataa





- **Androidille**:
    - Lataa [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) Google Play Storesta.
    - Vaihtoehto: Asenna APK-tiedoston kautta, joka on saatavilla [Blockstreamin virallisella GitHub-sivustolla](https://github.com/Blockstream/green_android).
- **IOS**:
    - Lataa [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) App Storesta.
- **Huomautus**: Varmista, että lataat virallisista lähteistä, jotta vältät vilpilliset sovellukset.



### 3.2. alkukonfigurointi





- **Aloitusnäyttö**: Kun sovellus avataan ensimmäisen kerran, se näyttää näytön ilman määritettyä Wallet:a. Luodut tai tuodut portfoliot näkyvät tässä myöhemmin.



![image](assets/fr/02.webp)





- **Mukauta asetuksia**: Napsauta "Sovelluksen asetukset", säädä alla olevia vaihtoehtoja, napsauta "Tallenna", käynnistä sovellus uudelleen ja luo portfoliosi.



![image](assets/fr/03.webp)



#### 3.2.1. Parannettu yksityisyys (vain Android)





- **Toiminto**: Poistaa kuvakaappaukset käytöstä, piilottaa sovellusten esikatselukuvat Tehtävienhallinnassa ja lukitsee pääsyn, kun puhelin on lukittu.
- **Miksi?**: Suojaa tietosi luvattomalta fyysiseltä käytöltä tai näytön sieppaavilta haittaohjelmilta.



#### 3.2.2. Yhteys Torin kautta





- **Toiminto**: Reititä verkkoliikenne **Tor**:n, anonyymin verkon kautta, joka salaa yhteydet.
- **Miksi?**: Tämä on ihanteellista, jos et luota verkkoosi (esimerkiksi julkiseen Wi-Fi-verkkoon).
- **Haitta**: Voi hidastaa sovellusta salauksen takia.
- **Suositus**: Aktivoi Tor, jos luottamuksellisuus on etusijalla, mutta testaa yhteyden nopeus.



#### 3.2.3. Yhteyden muodostaminen henkilökohtaiseen solmuun





- **Toiminto**: Yhdistää sovelluksen omaan **täydelliseen Bitcoin-solmuun** **Electrum-palvelimen** kautta.
- **Miksi?**: Tarjoaa Blockchain:n tietojen täydellisen hallinnan, mikä poistaa riippuvuuden Blockstream-palvelimista.
- **Edellytys**: Konfiguroitu Bitcoin-solmu.
- **Suositus**: Edistyneet käyttäjät, jotka haluavat maksimaalisen riippumattomuuden.



#### 3.2.4. SPV:n todentaminen





- **Toiminto**: Käyttää **Yhdennettyä maksun todentamista (SPV)** tiettyjen Blockchain-tietojen suoraan todentamiseen lataamatta koko ketjua.
- **Miksi?**: Vähentää riippuvuutta Blockstreamin oletussolmusta ja on samalla kevyt mobiililaitteille.
- **Haitta**: Full nodeää vähemmän turvallinen, koska se on riippuvainen kolmansien osapuolten solmuista joidenkin tietojen saamiseksi.
- **Suositus**: Aktivoi SPV, jos et voi käyttää henkilökohtaista solmua, mutta haluat Full node:n optimaalisen turvallisuuden vuoksi.





## 4. Bitcoin onchain-salkun luominen



### 4.1. Aloita luominen





- **Varoitus**: Aseta salkku yksityiseen ympäristöön, jossa ei ole kameroita tai tarkkailijoita.
- Napsauta aloitusnäytöltä "Get Started" :



![image](assets/fr/04.webp)





- Jos haluat hallita **Cold Wallet** (offline Wallet): klikkaa **"Connect Jade "** käyttääksesi Hardware Wallet Blockstream Jadea tai muita yhteensopivia Cold-lompakoita.



![image](assets/fr/05.webp)






- Seuraava näyttö tulee näkyviin:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Luo uusi Hot Wallet (Hot Wallet).
- (2) **"Palauta varmuuskopiosta "**: Tuo olemassa oleva salkku käyttämällä Mnemonic-lauseen (12 tai 24 sanaa). Varoitus: Älä tuo lausetta Cold Wallet:sta, koska se paljastuu liitetyssä laitteessa, mikä mitätöi sen turvallisuuden.
- (3) **"Vain tarkkailuun "**: Tuo olemassa oleva vain lukuoikeudellinen salkku, jotta voit tarkastella saldoa (esim. Cold Wallet) paljastamatta Mnemonic-lauseen tietoja. Katso "Watch Only" -ohjeet liitteessä.



**Tässä opetusohjelmassa**: Klikkaa **"Setup Mobile Wallet"** luodaksesi Hot Wallet.


Wallet luodaan automaattisesti, ja Wallet:n etusivu, jonka nimi on tässä "My Wallet 5", tulee näkyviin:



![image](assets/fr/07.webp)



**Tärkeää**: Wallet:n luomista on yksinkertaistettu siten, että 12-sanaista seed-lausetta ei näytetä automaattisesti. *Vaikka salkku luodaan nyt yhdellä napsautuksella, vaarana on, että menetät pääsyn varoihisi, jos et tallenna seed-lausetta*.



### 4.2. Tallenna seed-lause





- Napsauta Wallet:n aloitusnäytössä "Security"-välilehteä ja sitten "Back Up"-kehotetta tai "Recovery Phrase"-valikkoa:



![image](assets/fr/08.webp)



seed 12-sanainen lause näytetään tallennettavaksi.





- Kirjoita toipumislauseesi ylös äärimmäisen huolellisesti. Kirjoita se paperille tai metallille ja säilytä se turvallisessa paikassa (turvallinen, offline-sijainti). Tämä lauseke on ainoa keinosi päästä käsiksi bitcoineihisi, jos laitteesi katoaa tai sovellus poistetaan.
- On myös tärkeää huomata, että kuka tahansa, jolla on tämä lause, voi varastaa kaikki bitcoinisi. Älä koskaan säilytä niitä digitaalisesti:
 - Ei kuvakaappausta
 - Ei pilvi-, sähköposti- tai viestinnän varmuuskopioita
 - Ei kopiointia/liittämistä (riski tallentaa leikepöydälle)



**! Tämä kohta on kriittinen**. Lisätietoja varmuuskopioinnista :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Tarkista seed-lause



Ennen kuin lähetät varoja Address:een, joka liittyy tähän seed-lauseeseen, sinun on testattava 12 sanan varmuuskopiointi.


Tätä varten kirjoitamme viitteen, poistamme Wallet:n, palautamme sen varmuuskopion avulla ja tarkistamme, että viite ei ole muuttunut.





- Napsauta Wallet:n aloitusnäytössä "Settings"-välilehteä, sitten "Wallet Details" ja kopioi zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Huomautus: zpub Address voidaan tuoda Blockstream-sovellukseen "Watch Only" -toimintoa varten (katso liite).





- Poista sovellus, palauta Wallet sitten **"Restore from Backup "** kautta syöttämällä Mnemonic-lause ja tarkista, että zpub ei ole muuttunut. Jos vastaus on kyllä, varmuuskopio on oikea, ja voit lähettää varoja Wallet:lle.





- Jos haluat lisätietoja palautustestin suorittamisesta, tässä on oma opetusohjelma :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Sovelluksen käytön varmistaminen



Lukitse sovelluksen käyttöoikeus vahvalla PIN-koodilla:




- Siirry Wallet:n aloitusnäytöstä kohtaan **"Turvallisuus "** ja napsauta sitten **"PIN "**
- Syötä ja vahvista **sattumanvarainen 6-numeroinen PIN-koodi**.



**Biometrinen vaihtoehto**: Käytettävissä lisämukavuuden lisäämiseksi, mutta vähemmän turvallinen kuin vankka PIN-koodi (luvattoman pääsyn riski, esim. sormenjälki- tai kasvoskannaus unen aikana).



**Huomautus**: PIN-koodi suojaa laitteen, mutta vain seed-lausetta voidaan käyttää varojen palauttamiseen.





## 5. Liquid Wallet:n käyttö



### 5.1. Vastaanota "L-BTC" -bitcoineja



Liquid-bitcoinien (L-BTC) vastaanottamiseen on useita vaihtoehtoja. Voit pyytää jotakuta lähettämään sinulle niitä suoraan jakamalla Liquid:n vastaanottavan Address:n, mikä on kuvattu tarkemmin alla.



Vaihtoehtoisesti Exchange bitcoinit onchain tai kautta Lightning Network L-BTC käyttäen [silta kuten Boltz](https://boltz.Exchange/): kirjoita Liquid vastaanottava Address, tee maksu haluamallasi tavalla ja vastaanota L-BTC.





- Napsauta salkun aloitusnäytöltä "**Transaktio**" ja sitten **"Vastaanota "**.



![image](assets/fr/19.webp)





- Oletusarvoisesti sovellus näyttää tyhjän **kuitin Address, onchain** (SegWit v0 -muoto, joka alkaa kirjaimella `bc1q...`). Valitse **Liquid Bitcoin** napsauttamalla "Bitcoin":



![image](assets/fr/20.webp)





- **Vaihtoehdot**:
 - (1) Valitse toinen uusi Address, joka liittyy tähän seed-lauseeseen, napsauttamalla nuolia.
    - (2) Voit myös valita Address:n jo käytetyistä/näytetyistä osoitteista klikkaamalla kolmea pistettä oikeassa yläkulmassa ja sitten "Osoiteluettelo"
    - (3) Jos haluat pyytää tietyn summan, napsauta kolmea pistettä oikeassa yläkulmassa, valitse "Pyydä summa" ja syötä haluamasi summa. QR päivittyy, ja Address korvataan Bitcoin-maksun URI:llä.



![image](assets/fr/21.webp)





- Jaa Address/URI klikkaamalla "**Jaa**", kopioimalla teksti tai skannaamalla QR-koodi.
- **Tarkastus**: Tarkista vastaanottajan kanssa jaettu Address niin pitkälle kuin mahdollista virheiden tai hyökkäysten välttämiseksi (esim. leikepöydän muokkaaminen haittaohjelmilla).



### 5.2. lähetä bitcoineja





- Napsauta salkun aloitusnäytöltä "**Transaktio**" ja sitten **"Lähetä "** :



![image](assets/fr/22.webp)





- **Anna tiedot**:
    - (1) Syötä vastaanottajan **Address** kiinni kiinnittämällä se tai skannaamalla QR-koodi.
    - (2) Tarkista varat ja tili, jolta varat lähetetään.
    - (3) Ilmoita lähetettävä **määrä**. Voit valita yksikön: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **Tarkista**:
    - Tarkista Address, määrä ja maksut yhteenvetonäytöltä.
    - Address-virhe voi johtaa peruuttamattomaan varojen menetykseen. Varo leikepöytää muokkaavia haittaohjelmia.



![image](assets/fr/24.webp)





- **Vahvistus**: Allekirjoita ja lähetä tapahtuma liu'uttamalla "Lähetä"-painiketta.
- **Seuranta**: Wallet:n "Transact"-välilehdellä tapahtuma näkyy ensin "Unconfirmed", sitten "Confirmed" ja sitten "Completed":



![image](assets/fr/25.webp)





- Kahden lohkon välinen aika on 1 minuutti Liquid:llä, joten transaktio vahvistetaan ja suoritetaan nopeasti.




## Liitteet



### A1. Muut Blockstream-sovelluksen opetusohjelmat



Onchain-verkon käyttö



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Wallet:n tuonti ja seuranta "Watch Only" -tilassa



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop-versio



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Parhaat käytännöt



Jos haluat käyttää **Blockstream-sovellusta** turvallisesti ja tehokkaasti, noudata näitä suosituksia. Ne auttavat sinua suojaamaan varojasi, optimoimaan tapahtumia ja säilyttämään luottamuksellisuutesi **Bitcoin (onchain)**, **Liquid** ja **Lightning**-verkoissa.





- **Turvaa palautuslausekkeesi**:
 - Tutorial: Mnemonic-lauseen tallentaminen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Käytä suojattua todennusta**:
 - Ota käyttöön **vahva PIN-koodi** tai **biometrinen tunnistus** (sormenjälki tai kasvojentunnistus) sovelluksen käytön suojaamiseksi.
 - Älä koskaan jaa PIN-koodia tai biometrisiä tietoja.





- **Suojaa yksityisyytesi**:
 - generate uusi Address jokaista ketjussa tapahtuvaa vastaanottoa varten tai Liquid Blockchain:n jäljittämisen rajoittamiseksi.
 - Aktivoi "Enhanced Privacy", "Tor" ja "SPV" -toiminnot.
 - Jos haluat maksimaalisen luottamuksellisuuden, yhdistä Wallet omaan Bitcoin-solmuun Electrum-palvelimen kautta sen sijaan, että käyttäisit julkista solmua





- Valitse tarpeisiisi parhaiten sopiva **verkko**:
- **Onchain**: (palkkiot ovat vähäisiä suhteessa määrään).
- **Liquid**: Käytä nopeisiin, edullisiin siirtoihin, joissa on parempi luottamuksellisuus.
- **Salama**: Valitse välittömät, edulliset siirrot pienille summille.





- Tarkista aina **toimitusosoitteet**:
 - Tarkista Address huolellisesti ennen varojen lähettämistä. Väärään Address:een lähetetyt varat menetetään lopullisesti. Käytä kopiointia/liittämistä tai QR-koodin skannausta, älä koskaan kopioi/muuta Address:ta käsin.





- **Optimoi kustannukset**:
 - Valitse ketjutapahtumille sopivat maksut (hidas, keskitasoinen, nopea) kiireellisyyden ja verkon ruuhkautumisen mukaan.
 - Käytä Liquid:ää tai Lightningia pieniin määriin.





- Pidä hakemus ajan tasalla




### A3. Lisäresurssit





- **Viralliset linkit:**
- [Virallinen verkkosivusto](https://blockstream.com/)
- [Tuki mobiilisovellukselle](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentaatio ja chat
- [GitHub](https://github.com/Blockstream/green_android)





- Kortteleiden tutkijat:
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Salama: **[1ML (Lightning Network)](https://1ml.com/)**





- **Oppiminen ja opetusohjelmat:** **[Plan ₿ Network](https://planb.network/)** :
 - Elvytyslausekkeen turvaaminen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Sanasto](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Sanasto](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb