---
name: Blockstream App - Desktop
description: Kuinka käyttää Hardware Wallet:ta Blockstream-sovelluksella tietokoneella?
---
![cover](assets/cover.webp)



## 1. Johdanto



### 1.1 Tutoriaalin tavoite





- Tässä ohjeessa selitetään, miten **Blockstream-sovellusta** käytetään tietokoneella Bitcoin:n **onchain** Wallet:n hallintaan **Hardware Wallet:n** kanssa, mikä mahdollistaa suojatut tapahtumat, jotka on tallennettu Blockchain Bitcoin:een.
- Se kattaa asennuksen, alkukonfiguraation, Hardware Wallet:n liittämisen sekä onchain-bittikolikoiden vastaanottamisen ja lähettämisen.
- Huomautus: Liitteissä olevat muut opetusohjelmat käsittelevät Liquid:ta, Watch-Onlya ja mobiilisovellusta.



### 1.2 Kohderyhmä





- **Aloittelijoille**: Käyttäjät, jotka haluavat hallita bitcoinejaan turvallisella työpöytäohjelmistolla ja Hardware Wallet:llä.
- **Keskitason käyttäjät**: Ihmiset, jotka haluavat ymmärtää, miten Hardware Wallet:a käytetään onchain-tapahtumiin ja yksityisyysvaihtoehtoihin, kuten Toriin tai SPV:hen.



### 1.3. Taustaa laitteistolompakoista





- **Hardware Wallet**, **Cold Wallet**: Fyysinen laite, joka tallentaa yksityisiä avaimia offline-tilassa ja tarjoaa korkean tason tietoturvan verkkohyökkäyksiä vastaan, toisin kuin **Hot-lompakot** (ohjelmistolompakot liitetyissä laitteissa).
- **Suositeltu käyttö**:
    - Ihanteellinen suurten summien tai pitkäaikaisten säästöjen turvaamiseen.
    - Sopii tietoturvaan keskittyneille käyttäjille, jotka haluavat suojata varojaan yhdistettyihin laitteisiin liittyviltä riskeiltä.
- **Rajoitukset**: Tarvitaan ohjelmisto, kuten Blockstream App, jotta voidaan tarkastella saldoja, generate-osoitteita ja lähettää Hardware Wallet-signoituja tapahtumia.



## 2. Esittelyssä Blockstream App





- **Blockstream App** on mobiili- (iOS, Android) ja työpöytäsovellus Bitcoin-lompakoiden ja varojen hallintaan Liquid Network:ssä. Blockstream osti sen vuonna 2016, ja sen nimi oli *GreenAddress*, se nimettiin uudelleen *Blockstream Greeniksi* (2019), ja nyt sen nimi on *Blockstream app* (2025).
- **Tärkeimmät ominaisuudet**:
- Blockchain:n ja Bitcoin:n **onchain**-tapahtumat.
    - Tapahtumat **Liquid**-verkossa (Sidechain nopeaan ja luottamukselliseen vaihtoon).
- **Watch-only** -salkut rahastojen seurantaan ilman pääsyä avaimiin.
    - Tietosuojavaihtoehdot: yhteys **Torin** kautta, yhteys **persoonalliseen solmuun** Electrumin kautta tai **SPV**-varmistus, jolla vähennetään riippuvuutta kolmannen osapuolen solmuista.
    - Toiminnot **Replace-by-fee (RBF)** vahvistamattomien tapahtumien nopeuttamiseksi.
- **Yhteensopivuus**: **Blockstream Jade**.
- **Interface**: Intuitiivinen aloittelijoille, edistyneet vaihtoehdot asiantuntijoille.
- **Huomautus**: Tämä opas keskittyy ketjun käyttöön Hardware Wallet:n kanssa työpöytäversiossa. Muut liitteinä olevat oppaat käsittelevät käyttöä mobiilisovelluksessa, onchain-, Liquid- ja Watch-Only-ominaisuuksia.



## 3. Blockstream App Desktopin asentaminen ja käyttöönotto



### 3.1. lataa





- Siirry [viralliselle verkkosivustolle] (https://blockstream.com/app/) ja napsauta "_Download Now_". Lataa käyttöjärjestelmääsi (Windows, macOS, Linux) vastaava versio.
- **Huomautus**: Varmista, että lataat virallisen lähteen, jotta vältät vilpilliset ohjelmistot.



### 3.2. alkukonfigurointi





- **Aloitusnäyttö**: Kun sovellus avataan ensimmäisen kerran, se näyttää näytön ilman määritettyä Wallet:ta. Luodut tai tuodut portfoliot näkyvät tässä myöhemmin.



![image](assets/fr/02.webp)





- **Mukauta asetuksia**: Napsauta vasemmalla alhaalla olevaa asetuskuvaketta, säädä alla olevia vaihtoehtoja ja poistu sitten Interface:stä jatkaaksesi.



![image](assets/fr/03.webp)



#### 3.2.1. Yleiset parametrit





- Napsauta Asetukset-valikossa kohtaa "**Yleistä**".
- **Toiminto**: Vaihda ohjelmiston kieltä ja aktivoi tarvittaessa kokeellisia toimintoja.



![image](assets/fr/04.webp)



#### 3.2.2. Yhteys Torin kautta





- Napsauta Asetukset-valikossa kohtaa "**Verkko**".
- **Toiminto**: Reititä verkkoliikenne **Tor**:n, anonyymin verkon kautta, joka salaa yhteydet.
- **Miksi?**: Tämä on ihanteellista, jos et luota verkkoosi (esimerkiksi julkiseen Wi-Fi-verkkoon).
- **Haitta**: Voi hidastaa sovellusta salauksen takia.
- **Suositus**: Aktivoi Tor, jos luottamuksellisuus on etusijalla, mutta testaa yhteyden nopeus.



![image](assets/fr/05.webp)



#### 3.2.3. Yhteyden muodostaminen henkilökohtaiseen solmuun





- Napsauta Asetukset-valikossa kohtaa "**Tilaustyönä käytettävät palvelimet ja validointi**".
- **Toiminto**: Yhdistää sovelluksen omaan **täydelliseen Bitcoin-solmuun** **Electrum-palvelimen** kautta.
- **Miksi?**: Tarjoaa täydellisen hallinnan Blockchain-tietoihin ja poistaa riippuvuuden Blockstream-palvelimista.
- **Edellytys**: Konfiguroitu Bitcoin-solmu.
- **Suositus**: Edistyneet käyttäjät, jotka haluavat maksimaalisen riippumattomuuden.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV:n todentaminen





- Napsauta Asetukset-valikossa kohtaa "**Tilaustyönä käytettävät palvelimet ja validointi**".
- **Toiminto**: Joka lataa lohkootsikot ja tarkistaa tapahtumat sisällyttämistodistuksen (Merkle) avulla tallentamatta koko Blockchain:ta.
- **Miksi?**: Vähentää riippuvuutta Blockstreamin oletussolmusta ja on samalla kevyt laitteille.
- **Haitta**: Full node on turvattomampi, koska se on riippuvainen kolmansien osapuolten solmuista joidenkin tietojen saamiseksi.
- **Suositus**: Aktivoi SPV, jos et voi käyttää henkilökohtaista solmua, mutta haluat Full node:n optimaalisen turvallisuuden vuoksi.



![image](assets/fr/07.webp)



## 4. Hardware Wallet:n liittäminen Blockstream-sovellukseen



### 4.1. Alustavat huomiot



#### 4.1.1. Ledger-käyttäjille





- Blockstream Green tukee vain **Bitcoin Legacy** -sovellusta Ledger-laitteissa (Nano S, Nano X).
- Vaiheet, joita on noudatettava **Ledger Livessä** ennen laitteen liittämistä :


1. Mene kohtaan **"Asetukset "** → **"Kokeelliset ominaisuudet "** ja aktivoi **kehittäjätila**.


2. Siirry kohtaan **"Oma Ledger"** → **"Sovelluskatalogi "** ja asenna sitten **Bitcoin Legacy -sovellus**


3. Avaa **Bitcoin Legacy** -sovellus Ledger:ssä ennen Blockstream Green:n käynnistämistä yhteyden muodostamiseksi.




- **Huomautus**: Varmista, että Ledger on avattu PIN-koodilla ja että Bitcoin Legacy -sovellus on aktiivinen, kun muodostat yhteyden.



#### 4.1.2 Hardware Wallet:n alustaminen





- Jos Hardware Wallet:tä (Ledger, Trezor tai Blockstream Jade) ei ole koskaan käytetty (joko Blockstream Green:n tai muun ohjelmiston, kuten Ledger Liven, kanssa), se on ensin alustettava. Tähän vaiheeseen kuuluu, turvallisessa ympäristössä, ilman kameroita tai tarkkailijoita:


1. **seed-lauseen luominen / Mnemonic-lause** (12, 18 tai 24 sanaa): Kirjoita se huolellisesti paperille.


2. **seed-lauseen vahvistus**: Testaa Wallet-tuonti merkityistä sanoista, esim. tarkistamalla laajennettu julkinen avain. Suoritetaan ennen varojen lähettämistä Wallet:lle ja seed-lauseen pysyvää varmistamista.


3. **seed-lauseen turvaaminen**: Säilytä lauseke fyysisellä tietovälineellä (paperi tai metalli) ja turvallisessa paikassa. Älä koskaan säilytä sitä digitaalisesti (ei kuvakaappauksia, pilvipalvelua tai sähköpostia).




- **Tärkeää**: seed-lause on ainoa keino saada rahasi takaisin, jos laite katoaa tai siinä ilmenee toimintahäiriöitä. Kuka tahansa, jolla on pääsy laitteeseen, voi varastaa bitcoinisi.
- **Resurssit** seed-lauseen varmuuskopiointia ja tarkistamista varten :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Tämän opetusohjelman konfigurointi :





- Oletamme, että Hardware Wallet on jo alustettu seed-lauseella ja lukituksen PIN-koodilla.
- Oletamme, että Hardware Wallet:tä ei ole koskaan yhdistetty Blockstream App -sovellukseen, mikä edellyttää uuden tilin luomista. Jos Hardware Wallet:tä on jo käytetty Blockstream App -sovelluksen kanssa, tili tulee automaattisesti näkyviin, kun sovellus avataan.



### 4.2. Aloita yhteys





- Napsauta aloitusnäytöltä "**Setup a New Wallet**", vahvista sitten ehdot ja napsauta "**Get Started**" :



![image](assets/fr/08.webp)





- Valitse vaihtoehto "**Hardware Wallet:ssa**":



![image](assets/fr/09.webp)





- Jos käytät **Blockstream Jadea**, napsauta vastaavaa painiketta. Muussa tapauksessa valitse "**Connect a different Hardware Device**" :



![image](assets/fr/10.webp)





- Liitä Hardware Wallet tietokoneeseen USB:n kautta ja valitse se Blockstream App -sovelluksessa:



![image](assets/fr/22.webp)





- Odota, kun Blockstream App tuo salkkutietosi:



![image](assets/fr/23.webp)



### 4.3. Luo tili





- Jos Hardware Wallet:tä on jo käytetty Blockstream App -sovelluksen kanssa, tilisi näkyy automaattisesti Interface:ssa tuonnin jälkeen. Muussa tapauksessa luo tili napsauttamalla "**Luo tili**" :



![image](assets/fr/24.webp)





- Valitse "**Standard**" määrittääksesi klassisen Bitcoin-salkun:



![image](assets/fr/25.webp)





- Kun tilisi on luotu, pääset käyttämään Interface-pääsalkkuasi:



![image](assets/fr/26.webp)





## 5. Onchain Wallet:n käyttö Hardware Wallet:n kanssa



### 5.1. Vastaanota bitcoineja





- Napsauta portfolion päänäytöltä "**Vastaanottaa**" :



![image](assets/fr/27.webp)





- Sovellus näyttää **tyhjän vastaanoton Address**. Uuden Address:n käyttäminen jokaista vastaanottoa varten parantaa luottamuksellisuutta. Kopioi Address napsauttamalla "**Kopioi Address**" tai anna lähettäjän skannata näytetty QR-koodi:



![image](assets/fr/12.webp)



**Vaihtoehdot** :




- (1) Napsauta nuolinäppäimiä generate uuden Address:n linkittämiseksi salkkuusi.
- (2) Jos haluat pyytää tiettyä summaa, napsauta "**Muut vaihtoehdot**" ja sitten "**Pyydä summa**". QR päivittyy, ja Address korvataan Bitcoin-maksun URI:llä, kuten esimerkiksi: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Jos haluat käyttää edellisen Address:n uudelleen, napsauta "**Lisäasetukset**" ja sitten "**Osoiteluettelo**" :



![image](assets/fr/14.webp)





- **Tarkastus**: Tarkista jaettu Address huolellisesti virheiden tai hyökkäysten välttämiseksi (esim. leikepöydän muokkaaminen haittaohjelmilla).
- Kun tapahtuma on lähetetty verkkoon, se näkyy Wallet:ssa. Odota 1-6 vahvistusta, jotta tapahtumaa ei voida muuttaa.



![image](assets/fr/28.webp)



### 5.2. lähetä bitcoineja





- Napsauta portfolion päänäytöltä "**lähettää**".



![image](assets/fr/29.webp)





- **Anna tiedot**:
    - (1) Tarkista, että valittu hyödyke on **Bitcoin** (onchain).
    - (2) Syötä vastaanottajan **Address** liittämällä se tai skannaamalla QR-koodi webbikameralla.
    - (3) Ilmoita lähetettävä **summa** (BTC:nä, satosheina tai muina yksikköinä).




![image](assets/fr/16.webp)





- Valitse **transaktiomaksut** (valinnainen) :
 - Valitse ehdotetuista vaihtoehdoista (nopea, keskipitkänopea, hidas) kiireellisyyden mukaan ja arvioitu vahvistusaika.
 - Jos haluat mukautettuja maksuja, säädä manuaalisesti satoshien määrää vbyteä kohti. Nämä näkyvät aloitusnäytössä. Katso myös [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **UTXO:n manuaalinen valinta** (valinnainen): Napsauta "**Manuaalinen Coin-valinta**" valitaksesi tietyt UTXO:t, joita käytetään tapahtumassa.



![image](assets/fr/18.webp)





- **Alustava tarkastus**: Tarkista Address, summa ja maksut yhteenvetonäytöltä ja napsauta sitten "**Vahvista tapahtuma**". Todellisuudessa tapahtumaa ei vapauteta verkkoon ennen kuin olet allekirjoittanut sen Hardware Wallet:lla, jossa on yksin salaiset avaimet, jotka liittyvät osoitteisiin, joista UTXO:t (satoshit) veloitetaan.



![image](assets/fr/19.webp)





- **Lopputarkastus ja allekirjoitus**: Varmista, että kaikki tapahtumaparametrit ovat oikein **Hardware Wallet** -näytölläsi, ja allekirjoita sitten tapahtuma sen avulla. Address:n virhe voi johtaa varojen peruuttamattomaan menetykseen.





- **Lähetys**: Blockstream App lähettää tapahtuman automaattisesti Bitcoin-verkkoon, kun se on allekirjoitettu.



![image](assets/fr/20.webp)





- **Seuranta**:
 - Tapahtuma näkyy Wallet:n aloitusnäytössä "odottavana", kunnes se vahvistetaan.
 - Niin kauan kuin maksutapahtumaa ei ole vahvistettu, **Replace-by-fee (RBF)**-toimintoa voidaan käyttää vahvistuksen nopeuttamiseen korottamalla maksua (katso liite).



![image](assets/fr/21.webp)



## Liitteet



### A1. Muut Blockstreamin opetusohjelmat





- Liquid Network:n käyttäminen :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Tuo ja seuraa salkkua "Watch-Only" -tilassa:



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Blockstream-sovelluksen käyttäminen matkapuhelimissa (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Replace-by-fee:n (RBF:n) selitys





- **Määritelmä**: Replace-by-fee (RBF) on Bitcoin-verkon ominaisuus, jonka avulla lähettäjä voi nopeuttaa **ketjussa tapahtuvan** tapahtuman vahvistamista korottamalla maksua.
- **Rajat**:
    - RBF ei ole käytettävissä Liquid- tai Lightning-tapahtumissa.
    - Alkuperäinen transaktio on merkittävä RBF-yhteensopivaksi, minkä Blockstream App tekee automaattisesti.
- Lisätietoja on [sanastossamme](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Parhaat käytännöt





- **Suojaa palautuslausekkeesi** :
    - Tallenna Hardware Wallet:n Mnemonic-lause fyysisellä välineellä (paperi, metalli) turvalliseen paikkaan.
    - Älä koskaan tallenna sitä digitaalisesti (pilvi, sähköposti, kuvakaappaus).
    - Ohje : Tallenna Mnemonic-lauseesi :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Suojaa yksityisyytesi**:





    - generate uusi Address jokaista ketjussa tapahtuvaa vastaanottoa varten.
    - Aktivoi **Tor** tai **SPV** seurannan rajoittamiseksi.
    - Yhdistä omaan Bitcoin-solmuun Electrumin kautta, jotta voit olla mahdollisimman suvereeni.
- Tarkista aina **toimitusosoitteet**:





    - Tarkista Address Hardware Wallet-näytöltä ennen allekirjoittamista.
    - Käytä kopiointia/liittämistä tai QR-koodia manuaalisten virheiden välttämiseksi.
- **Optimoi kustannukset**:





    - Säädä maksuja kiireellisyyden ja verkon ruuhkautumisen mukaan (katso [Mempool.space](https://Mempool.space/)).
    - Käytä Liquid:ta tai Lightningia nopeisiin ja edullisiin maksutapahtumiin, jotka eivät vaadi ketjun sisäistä suojausta.
- **Päivitä ohjelmisto**:





    - Pidä Blockstream-sovellus ja Hardware Wallet-firmware ajan tasalla uusimpien ominaisuuksien ja tietoturvakorjausten kanssa.



### A4. Lisäresurssit





- **Viralliset linkit**:
    - [Virallinen verkkosivusto](https://blockstream.com/)
    - [Tuki Blockstream-sovellukselle](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentaatio ja chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Block Explorers**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Salama : [1ML (Lightning Network)](https://1ml.com/)





- **Palautuslausekkeen turvaaminen:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Sanasto](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Sanasto](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb