---
name: Sonni Bitcoin Wallet
description: Selvitä, miten Wallet Bull Bitcoin:ta käytetään
---

![cover](assets/cover.webp)



Tässä oppaassa kerrotaan Bull Bitcoin Mobile -laitteen asennuksesta, konfiguroinnista ja käytöstä. Opit, miten vastaanotat ja lähetät varoja kolmessa verkossa: onchain-, Liquid- ja Lightning-verkoissa ja miten Bitcoin:ää siirretään verkosta toiseen. Liitteissä on resursseja ja yhteystietoja, taustatietoja ja lyhyitä selityksiä teknisistä käsitteistä.



## Johdanto



**Bull Bitcoin Mobile**, jonka on kehittänyt **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)), on **itseohjautuva** Bitcoin Wallet, mikä tarkoittaa, että sinulla on täysi määräysvalta yksityisiin avaimiisi ja siten varoihisi ilman, että olet riippuvainen kolmannesta osapuolesta. Avoimen lähdekoodin Cypherpunk-filosofiaan perustuvassa Wallet:ssä yhdistyvät yksinkertaisuus, luottamuksellisuus ja edistykselliset ominaisuudet, kuten verkkojen väliset vaihdot ja PayJoin-tuki. Sen avulla voit hallita bitcoinejasi kolmessa verkossa: **Bitcoin onchain**, **Liquid** ja **Lightning**, joista jokainen on räätälöity tiettyihin käyttötarkoituksiin.



### Kehityskonteksti



Wallet vastaa suureen haasteeseen: Bitcoin-verkkomaksut eivät sovellu pieniin maksuihin tai pienten itse isännöityjen Lightning-kanavien avaamiseen. Wallet Bull Bitcoin Mobile tarjoaa itsehallinnoitavan ratkaisun ja tukeutuu samalla kolmeen tärkeimpään Bitcoin-verkkoon:





- Bitcoin-verkko (onchain)**: Ihanteellinen keskipitkän ja pitkän aikavälin UTXO-varastointiin ja suurten arvojen transaktioihin, joissa maksut ovat suhteellisesti merkityksettömiä.
- Liquid Network**: Suunniteltu nopeisiin (~2 minuuttia), luottamuksellisempiin (piilotetut summat) ja edullisiin tapahtumiin, jotka sopivat täydellisesti pienten summien keräämiseen tai yksityisyyden suojaamiseen.
- Lightning**-verkko: Soveltuu pieniin ja keskisuuriin päivittäisiin maksutapahtumiin.



Esimerkiksi Bull Bitcoin Mobile -mobiililla voit kerätä pieniä summia **Liquid**- tai **Lightning**-salkkuihin ja sitten, kun olet saavuttanut merkittävän summan, voit :





- Siirto onchain-verkkoon turvallista keskipitkän tai pitkän aikavälin varastointia varten, jossa on parannettu luottamuksellisuutta Liquid:n ja/tai Lightningin avulla ja jossa onchain-maksuja peritään yhdestä transaktiosta



### Jatkuva kehitys



Wallet kehittyy jatkuvasti, joten älä ylläty, jos huomaat ristiriitaisuuksia tämän ohjeen ja ajantasaisen sovelluksesi välillä.




- Esimerkiksi 19.07.2025 alkaen **"Osta / Myy / Maksa "**-painikkeet ovat näkyvissä, mutta harmaina sovelluksessa, koska nämä vaihtoehdot, jotka ovat saatavilla Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel) -palvelussa, integroidaan pian yhtenäiseen kokemukseen. Niiden käyttö pysyy täysin vapaaehtoisena. Monet muut kehitystyöt ovat käynnissä tai suunnitteilla: usean Wallet:n hallinta, passphrase, yhteensopivuus laitteistolompakoiden kanssa...
- [BullBitcoin GitHubissa](https://github.com/orgs/SatoshiPortal/projects/49) voit tutustua ajankohtaisiin aiheisiin ja tuleviin kehityskohteisiin. Koska hanke on 100-prosenttisesti avoimen lähdekoodin ja "julkisesti rakennettu", voit myös lähettää meille ehdotuksesi ja kaikki havaitsemasi virheet.




## 1. Edellytykset



Ennen kuin aloitat **Bull Bitcoin Mobile**:n käytön, varmista, että sinulla on seuraavat tavarat:





- Yhteensopiva älypuhelin**: **iOS** (iPhone tai iPad) tai **Android** -laite
- Internet-yhteys
- Turvallinen varmuuskopiointiväline**: Kirjoita **palautuslauseke** (12 sanaa) paperille tai metallille ja säilytä se turvallisessa paikassa.
- Perustiedot**: Bitcoin:n käsitteiden (osoitteet, maksutapahtumat, maksut) vähimmäistuntemus on hyödyllistä, vaikka tässä oppaassa selitetäänkin jokainen vaihe aloittelijoille.



## 2. Asennus





- Lataa hakemus** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Lataa sovelluskaupasta Android-laitteille
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Lataa APK Android-laitteille suoraan**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Lataa TestFlightin kautta Applen laitteille
 - Tarkista kehittäjän nimi (Bull Bitcoin) välttääksesi vilpilliset hakemukset.
 - Varmista, että ladattu versio vastaa GitHubissa ilmoitettua viimeisintä vakaata versiota.
 - Bull Bitcoin Mobile on **avoin lähdekoodi**. Voit tarkastella koodia: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Asenna sovellus




## 3. Alkuperäinen konfigurointi



### 3.1 Käynnistä sovellus :



Sovelluksessa käytetään molemmissa salkuissa ainutlaatuista 12-sanaista palautuslausetta:




 - gW-26' Wallet**: Bitcoin-verkossa tapahtuviin liiketoimiin (onchain)
 - instant Payments' Wallet**: Liquid- ja Lightning-verkoissa tapahtuviin välittömiin maksutapahtumiin



Kun avaat sen, sinua pyydetään tuomaan olemassa oleva palautuslauseke tai luomaan uusi Wallet :



![image](assets/fr/02.webp)



### 3.2 Palautuslauseke :



Jos haluat käyttää olemassa olevaa Wallet:tä uudelleen, napsauta "**Recover Wallet**" ja täytä 12 sanaa palautuslausetta.



Muussa tapauksessa napsauta "**Luo uusi Wallet**" :




- Kirjoita toipumislauseesi ylös äärimmäisen huolellisesti. Kirjoita se paperille tai metallille ja säilytä sitä turvallisessa paikassa (tallelokerossa, offline-sijainnissa). Tämä lauseke on ainoa keinosi päästä käsiksi bitcoineihisi, jos laitteesi katoaa tai sovellus poistetaan.
- On myös tärkeää huomata, että kuka tahansa, jolla on tämä lause, voi varastaa kaikki bitcoinisi. Älä koskaan säilytä niitä digitaalisesti:
 - Ei kuvakaappausta
 - Ei pilvi-, sähköposti- tai viestinnän varmuuskopioita
 - Ei kopiointia/liittämistä (riski tallentaa leikepöydälle)



**! Tämä kohta on kriittinen**. Lisätietoja :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Pääsyn varmistaminen :





- Siirry asetuksiin ja napsauta sitten **PIN-koodi**.
- Määritä vankka **PIN-koodi** sovelluksen käytön suojaamiseksi.
- Tämä vaihe on valinnainen, mutta sitä suositellaan, jotta kukaan, jolla on pääsy puhelimeesi, ei pääse käsiksi Wallet:een.



![image](assets/fr/03.webp)



### 3.4 Yhteys henkilökohtaiseen solmuun (valinnainen):



Wallet BullBitcoin muodostaa oletusarvoisesti yhteyden Electrum-palvelimiin: ensimmäiseen Bull Bitcoin:n hallinnoimaan palvelimeen ja toiseen Blockstreamin palvelimeen, joiden molempien katsotaan pitävän lokitietoja, mikä vähentää jäljitysriskiä.



Suurempaa luottamuksellisuutta varten voit liittää sovelluksen omaan Bitcoin-solmuun Electrum-palvelimen kautta (ohjeet saatavilla [BullBitcoinin GitHubissa](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Varojen vastaanottaminen



Varojen vastaanottaminen **Bull Bitcoin Mobile**:n avulla on yksinkertaista ja räätälöity tarpeisiisi, käytitpä sitten :




  - **Bitcoin (onchain)** -verkko pitkäaikaista säilyttämistä varten,
  - **Liquid**-verkko nopeaa, enemmän Confidential Transactions:ää varten,
  - **Lightning**-verkkoon välittömiä, arvoltaan vähäisiä maksuja varten.



Sovellus luo automaattisesti Lightning-vastaanotto- tai Invoice-osoitteet valitun verkon mukaan. Näin menetellään kunkin verkon osalta.



### 4.1. onchain (Bitcoin-verkko)



Aloitusnäytössä voit :




- tai valitse **Secure Bitcoin Wallet** ja napsauta sitten "**Vastaanottaa "** :



![image](assets/fr/04.webp)





- tai napsauta "**Vastaanottaa "** ja valitse sitten **Bitcoin**-verkko:



![image](assets/fr/05.webp)



#### 4.1.1. Copy or scan Address only" -vaihtoehto pois käytöstä (oletus)



![image](assets/fr/06.webp)





- Tämä antaa pääsyn valinnaisiin lisäparametreihin. Voit määrittää :
 - **Määrä** BTC:nä, Sats:nä tai fiat-rahana.
 - **henkilökohtainen huomautus**, joka sisällytetään URI- / QR-koodin kopioon.
 - **PayJoin**:n aktivointi (ks. lisäys 3), joka parantaa luottamuksellisuutta yhdistämällä lähettäjän ja vastaanottajan tiedot.





- Esimerkki automaattisesti luodusta URI:stä** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Käyttö**: Kopioi URI jaa lähettäjän kanssa tai anna hänen skannata QR-koodi.



#### 4.1.2. Copy or scan Address only" -vaihtoehto käytössä



![image](assets/fr/07.webp)





- Kun **"Copy or scan Address only "** -vaihtoehto on käytössä, sovellus luo yksinkertaisen Bitcoin Address:n SegWit (bech32) -muodossa.





- Esimerkki:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Vaikka kirjoittaisit summan tai huomautuksen, niitä ei sisällytetä QR-koodiin tai Address-kopioon





- Käyttö**: Kopioi Address jaa se lähettäjän kanssa tai anna hänen skannata QR-koodi.



#### 4.1.3. Uuden Address:n luominen





- Miksi käyttää uutta Address:ää jokaista tapahtumaa varten? Tämä **suojaa yksityisyyttäsi** estämällä useiden maksujen yhdistämisen samaan Address:ään ja rajoittamalla Blockchain:n jäljitysmahdollisuuksia.
 - Oletusarvoisesti Bull Bitcoin luo automaattisesti käyttämättömän Address.**
 - Voit pakottaa uuden Address:n luomiseen napsauttamalla näytön alareunassa olevaa **"New Address"**.
 - Kaikki osoitteesi on yhdistetty seed-lauseeseen: riippumatta siitä, kuinka monta osoitetta käytät, salkussasi näkyy yksi saldo, ja se voi automaattisesti yhdistää varat, kun lähetys tehdään.





- Vinkki: Käytä aina Bull Bitcoin:n tarjoamaa uutta Address**, ellei sinulla ole erityistä tarvetta (esim. julkinen Address lahjoitusten vastaanottamista varten).



### 4.2. Liquid



Aloitusnäytössä voit :




- tai valitse **Pikamaksut Wallet** ja napsauta sitten **"Vastaanota "** ja **"Liquid"** :



![image](assets/fr/08.webp)





- tai napsauta "**Vastaanottaa "** ja valitse sitten **Liquid**-verkko:



![image](assets/fr/09.webp)



Kun olet **"Vastaanota "** -näytöllä, kopioi Liquid Address:





- Ei summaa tai merkintää. Esimerkki:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Tai määrittämällä **summan** (BTC:nä, Sats:nä tai fiat-rahana) ja/tai **henkilökohtaisen viestin**, joka sisällytetään URI- / QR-koodin kopioon. Esimerkki:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Käyttö**: Kopioi Address/URI jaa se lähettäjän kanssa tai anna hänen skannata QR-koodi.



### 4.3. Salama



Aloitusnäytössä voit :




- tai valitse **Pikamaksut Wallet** ja napsauta sitten "**Vastaanottaa "** :



![image](assets/fr/10.webp)





- tai napsauta "**Vastaanottaa "** ja valitse sitten **Valo**-verkko:



![image](assets/fr/11.webp)



#### 4.3.1. Toiminta, rajoitukset ja hyödyt





- Mekanismi**: Bull Bitcoin Wallet on Wallet, joka mahdollistaa maksujen suorittamisen ja vastaanottamisen Lightningin kautta. Lightningin kautta vastaanotetut varat tallennetaan **Liquid**-verkkoon (Wallet-pikamaksuihin) **Boltzin** kautta tapahtuvan automaattisen vaihdon ansiosta. Tämä antaa sinulle mahdollisuuden olla vuorovaikutuksessa Lightningin kanssa ilman likviditeettikanavien hallintaa, ja samalla pysyt itse säilössä.





- Rajoitukset:**
 - Vähimmäismäärä** on 100 satoshia (19.07.2025 alkaen), kun käytät generate Invoice:ää.
 - Maksat kulut**, jotka vähennetään lähettäjän lähettämästä summasta, toisin kuin Wallet Lightning Native -lähetyksessä, jossa vain lähettäjä maksaa siirtokulut lähetetyn summan lisäksi. 19/07/2025, 47 Sats vähennetään lähetetystä summasta.





- Edut** :
 - Omahuoltajuus**: Varasi pysyvät hallinnassasi, ne säilytetään Liquid Network:ssä.
 - Ei korkeita onchain-maksuja**: Tallentaminen Liquid:ssä välttää kalliit talletukset ketjussa Lightning-kanavan avaamiseksi tai likviditeetin lisäämiseksi. Nämä operaatiot voidaan suorittaa myöhemmin, kun Liquid:een kertynyt määrä oikeuttaa maksut.





- Vihje:** Jos lähettäjällä on Wallet Bull Bitcoin, käytä suoraan Liquid Network:ta välttääksesi vaihtomaksut



#### 4.3.2. generate Invoice





- Kirjoita **summa** (BTC:nä, Sats:nä tai fiat-rahana)





- Lisää **henkilökohtainen huomautus**, joka liitetään Invoice:aan. Jos lähettäjä maksaa Invoice:n, myös Wallet:si sisällyttää sen tapahtuman tietoihin.





- Invoice:n voimassaoloaika:** Salama Invoice on voimassa **12 tuntia**. Tämän ajan jälkeen se vanhenee, eikä sitä voi enää maksaa. Uusi Invoice on luotava.





- Käyttö**: Kopioi Invoice jaa se lähettäjän kanssa tai anna hänen skannata QR-koodi.




## 5. Varojen lähettäminen



### 5.1. Perusperiaate



Joko kotisivulta tai lompakoista :



![image](assets/fr/12.webp)



päästäksesi lähetysnäyttöön:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** tekee rahan lähettämisestä helppoa tunnistamalla automaattisesti verkon (Bitcoin, Liquid tai Lightning) syötetyn Address- tai Invoice-koodin (kopioitu tai skannattu QR-koodilla) perusteella.



### 5.2. ketjussa tapahtuva siirto (Bitcoin-verkko)



#### 5.2.1. Lähetä-näyttö



**Toimi**: Syötä tai skannaa Bitcoin onchain Address





- Jos määrää ei ole määritelty, esimerkiksi :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Sitten voit valita lähetysnäytössä :
 - Summa BTC:nä, sat tai fiat. Vähimmäissumma: 546 satoshia 22/07/2025.
 - Valinnainen huomautus tapahtuman yksilöimiseksi. Näkyy vain sinulle tapahtuman tiedoissa.



![image](assets/fr/14.webp)





- Jos määrä on jo määritelty, esimerkiksi :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Tämän jälkeen pääset suoraan alla olevaan vahvistusnäyttöön.



#### 5.2.2 Vahvistusnäyttö



Tarkista ajoissa kaikki parametrit, erityisesti summa, määränpää Address ja maksut.


Sitten voit säätää parametreja:



![image](assets/fr/15.webp)




- Maksut**: Voit valita :
  - Arvioidaan joko tapahtuman toteuttamisnopeus** ja siihen liittyvät maksut
  - Arvioidaan joko maksut** Absoluuttiset maksut (kokonaismaksut satosheina) tai Suhteelliset maksut (maksut tavua kohti) -tilassa sekä tapahtuman nopeus





- Lisäasetukset** :





 - Replace-by-fee (RBF)** : Tämä toiminto on oletusarvoisesti aktivoitu, ja se nopeuttaa maksutapahtumaa maksamalla korkeamman maksun (katso lisätietoja liitteestä 4).





 - UTXO**:n manuaalinen valinta: Jos varoja on tallennettu useisiin eri Wallet-osoitteisiin, voit valita osoitteet, joista varat lähetetään. Miksi sinun pitäisi tehdä näin? Bitcoin:n yleistymisen myötä siirtomaksut nousevat. Lähetys useista osoitteista pienillä summilla on kalliimpaa kuin lähetys yhdestä Address-osoitteesta, mutta jos teet sen nyt, vältyt myöhemmiltä maksuilta, jolloin maksut nousevat entisestään. Tätä kutsutaan ** UTXO:n konsolidoinniksi**



![image](assets/fr/16.webp)





- Lähettäminen PayJoin**:n kanssa: Jos URI:n toimittanut vastaanottaja on aktivoinut toiminnon, esim. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Tämän jälkeen Bull Bitcoin Mobile määrittää lähetyksen yhdistämällä UTXO:t ja vastaanottajan UTXO:t syötteenä, mikä parantaa luottamuksellisuutta (katso lisätietoja liitteestä 3).



### 5.3. Lähetä Liquid:aan



#### 5.3.1 Lähetä-näyttö



** Liquid**-verkko mahdollistaa nopeat transaktiot (~2 minuuttia yhden lohkon minuutissa ansiosta), luottamuksellisemmat (peitetyt summat) kuin onchain-verkossa ja erittäin alhaiset maksut. Varat nostetaan **Instant Payments Wallet** -verkosta.



**Toimi**: Syötä tai skannaa Liquid Address





- Jos määrää ei ole määritelty, esimerkiksi :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Sitten voit valita lähetysnäytössä :




- Summa BTC:nä, sat tai fiat. Ei vähimmäismäärää, 1 Satoshi mahdollista;
- Valinnainen huomautus tapahtuman yksilöimiseksi. Näkyy vain sinulle tapahtuman tiedoissa.



![image](assets/fr/17.webp)





- Jos määrä on jo määritelty, esimerkiksi :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Tämän jälkeen pääset suoraan alla olevaan vahvistusnäyttöön.



#### 5.3.2 Vahvistusnäyttö



Tarkista kaikki parametrit, erityisesti määrä ja määränpää Address.



![image](assets/fr/18.webp)





- Maksut**: Yleensä 0,1 sat/vB, eli 20-40 satoshia yksinkertaisesta transaktiosta (33 Sats 07/22/2025).



### 5.4. Lähetä Lightningiin



#### 5.4.1 Lähetä-näyttö



**Lightning**-verkko mahdollistaa välittömät ja edulliset maksut pienistä summista, mikä sopii erinomaisesti pieniin päivittäisiin maksutapahtumiin.



**Toimi**: Syötä tai skannaa Lightning Invoice





- Jos skannaat LN-URL Address, jonka avulla voit asettaa määrän


Esimerkki: `orangepeel@walletofsatoshi.com`.


voit valita lähetysnäytössä :




 - Summa BTC:nä, sat tai fiat. Vähimmäismäärä 1000 satoshia 23/07/2025
 - Valinnainen huomautus tapahtuman yksilöimiseksi. Se lähetetään vastaanottajalle.



![image](assets/fr/19.webp)





- Jos skannaat Lightning Invoice:n, joka sisältää tietyn määrän


Esimerkki:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Tämän jälkeen pääset suoraan alla olevaan vahvistusnäyttöön.



Huomautus: määrän on oltava suurempi kuin 21 Sats 23.07.2025



#### 5.4.2 Toiminta, rajoitukset ja hyödyt





- Mekanismi**: Varat otetaan **Pikamaksut Wallet**:sta (Liquid) ja muunnetaan **Liquid → Lightning**-swapilla **Boltzin** kanssa.





- Rajoitukset:**
 - Vähimmäismäärä** suurempi kuin Wallet Lightning native (ks. edellä)
 - Kulut** plus Liquid → Salamanvaihto Boltzin välityksellä





- Edut** :
 - Omahuoltajuus**: Varasi pysyvät hallinnassasi, ne on tallennettu Liquid Network:een ja siirrettävissä tarvittaessa Lightningin kautta
 - Ei korkeita onchain-maksuja**: Tallentaminen Liquid:een on säästänyt sinut kalliilta onchain-talletuksilta Lightning-kanavan avaamiseksi tai likviditeetin lisäämiseksi. Nämä operaatiot voidaan suorittaa myöhemmin, kun Liquid:een kertynyt määrä oikeuttaa maksut.





- Vihje:** Jos vastaanottajalla on Wallet Bull Bitcoin, käytä suoraan Liquid Network:ää välttääksesi vaihtokustannukset



#### 5.3.3 Vahvistusnäyttö



Tarkista kaikki parametrit, erityisesti määrä ja määränpää Address.



![image](assets/fr/20.webp)




## 6. Näytä historia



**Bull Bitcoin Mobile**:n avulla on helppo seurata transaktioitasi **Bitcoin (onchain)**, **Liquid** ja **Lightning** -verkoissa. Historiaa voi tarkastella kahdella tavalla, ja se näyttää yksityiskohtaiset tiedot kustakin tapahtumatyypistä. Voit myös tarkistaa tapahtumasi käyttämällä ulkoisia lohkoselaimia.



### 6.1. Pääsyhistoria





- Aloitusnäytön kautta** :
 - Napsauta **Secure Bitcoin Wallet** nähdäksesi **onchain**-tapahtumat tai **Instant Payments Wallet** **Liquid**- ja **Lightning**-tapahtumia.
 - Historia näytetään suoraan salkun kokonaismäärän alapuolella, ja se suodatetaan valitun Wallet-tyypin mukaan.



![image](assets/fr/21.webp)





- Oman sivun kautta** :
 - Napsauta aloitusnäytössä **historiasymbolia** (kellokuvake tai vastaava).
 - Pääset sivulle, jossa luetellaan kaikki tapahtumat ja jossa on suodattimia toimintatyypin mukaan: **(Huomautus: Myynti ja osto ovat kehitteillä, eivätkä ne ole käytettävissä tällä hetkellä, 20. heinäkuuta 2025).



![image](assets/fr/22.webp)



### 6.2. Tapahtuman tiedot



Jokaisesta tapahtumasta näytetään erityiset tiedot verkosta ja toimintatyypistä (lähettäminen tai vastaanottaminen) riippuen. Tässä ovat **transaktion onchain** tiedot:



![image](assets/fr/23.webp)



### 6.3. Tarkastus Block explorer:n kautta



Lisäyksessä 4 on luettelo **Bitcoin onchain**-, **Liquid**- ja **Lightning**-verkkojen tutkimusmatkailijoista.



**Lightning**:n osalta tapahtumat eivät näy julkisissa selaimissa. Tarkista yksityiskohdat (mukaan lukien Boltzin swap-tunnus) hakemuksesta.




## 7. Asetukset



Asetukset-sivulle pääsee suoraan Bull Bitcoin -sovelluksen etusivulta, ja sitä käytetään portfolion ja käyttäjäkokemuksen eri näkökohtien määrittämiseen ja hallintaan.



![image](assets/fr/24.webp)





- Wallet Varmuuskopio**: Näyttää salkun palautuslauseen turvallista varmuuskopiointia varten. Katso palautuslausekkeen hallintaan ja tallentamiseen liittyviä parhaita käytäntöjä salkun luomista käsittelevästä kohdasta 3..





- Wallet Yksityiskohdat** :
 - Pubkey**: Wallet:een liittyvä julkinen avain, jota käytetään generate Bitcoin:n vastaanotto-osoitteisiin.
 - Johdannaispolku**: Johdatuspolku, jota käytetään generate Wallet-osoitteiden johtamiseen yksityisestä avaimesta.





- Electrum-palvelin (Bitcoin-solmu)**: Määritä yhteys räätälöityyn Bitcoin-solmuun ketjussa tapahtuvia transaktioita varten.





- PIN-koodi**: Aktivoi ja/tai muuta turvakoodi, jolla suojataan pääsy sovellukseen ja Wallet-toimintoihin.





- Valuutta**: Valitse, näytetäänkö summat BTC:nä vai Sats:nä, ja oletusvaluutta (dollari, euro jne.).





- Automaattiset vaihto-asetukset**: Automaattivaihto -toiminnon avulla voit automatisoida BTC-siirron **Instant Payments Wallet (Liquid)**:stä **Bitcoin On-Chain** Wallet:een heti, kun summa saavuttaa kynnysarvon, jonka katsot riittävän korkeaksi transaktiopalkkion maksamiseksi.





- Lokit**: Tarkasteltavissa olevat toimintalokit, jotka voidaan jakaa teknisen tuen kanssa vianmäärityksen helpottamiseksi.





- Telegram-yhteys tukea varten** : Suora linkki viralliseen Telegram-kanavaan, josta saa tukea käyttäjille.





- Github-käyttöoikeus** : Linkki [Bull Bitcoin Github-tietokantaan](https://github.com/SatoshiPortal) avoimen lähdekoodin koodin tarkastelemiseksi tai ongelmien raportoimiseksi.




## LIITTEET



### A1. PayJoin:n selitys (P2EP)



![image](assets/fr/25.webp)



**Määritelmä** :




- PayJoin eli **Pay-to-EndPoint (P2EP)** on Bitcoin-tapahtumatekniikka, joka parantaa luottamuksellisuutta **onchain**-verkossa. Siinä yhdistetään lähettäjän ja vastaanottajan merkinnät yhdeksi transaktioksi, jolloin summia ja osoitteita on vaikeampi jäljittää.



**Toiminta:**




- PayJoin-tapahtumassa lähettäjä ja vastaanottaja tekevät yhteistyötä yhteensopivan PayJoin-palvelimen kautta generate-yhteistapahtuman toteuttamiseksi.
- Sen sijaan, että vain lähettäjä toimittaisi merkintöjä (UTXO), myös vastaanottaja osallistuu yhdellä omalla UTXO:lla. Tämä hämärtää Blockchain:ssa näkyvää tietoa: todellista määrää vastaavan yhden merkinnän sijasta merkintöjä on nyt kaksi, eivätkä tuotokset suoraan vastaa vaihdettua määrää.
- Lopullinen maksutapahtuma muistuttaa tavallista Bitcoin-transaktiota (monisyöttöinen/monisyöttöinen maksutapahtuma), mutta piilottaa todellisen lähetetyn summan ja osoitteiden väliset yhteydet steganografisen rakenteen ansiosta.



**Käyttöön Bull Bitcoin Mobile** -mallissa




- Vastaanottaa** (Address Supply): PayJoin on oletusarvoisesti käytössä.
- Lähetä** : Wallet tunnistaa automaattisesti PayJoin URI:n ja konfiguroi tapahtuman sen mukaisesti, esimerkiksi:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Hyötyjä**




- Parannettu luottamuksellisuus**: PayJoin kumoaa oletuksen, että kaikki tapahtuman merkinnät kuuluvat yhdelle taholle. PayJoin:ssä syötteet tulevat sekä lähettäjältä että vastaanottajalta, mikä rikkoo tämän oletuksen.
- Määrän peittäminen** : Todellinen vaihdettu määrä ei näy suoraan tulosteissa. Se lasketaan vastaanottajan saapuvan ja lähtevän UTXO:n erotuksena, mikä tekee analyysistä harhaanjohtavan.



**Limits**




- PayJoin edellyttää, että lähettäjä ja vastaanottaja käyttävät yhteensopivia lompakoita, muuten käytetään tavallista ketjussa tapahtuvaa transaktiota.
- Liiketoimi on hieman monimutkaisempi (enemmän panoksia ja tuotoksia), minkä vuoksi kustannukset ovat hieman korkeammat.
- Vaikka se on suunniteltu muistuttamaan tavanomaista transaktiota, kehittyneet heuristiikat (esim. moniselitteiset tuotokset, tunnetut PayJoin-palvelimet) voivat antaa aihetta epäillä sen käyttöä, vaikkei siitä olekaan täyttä varmuutta.



**Lisätietoa:**




- [Sanasto](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Replace-by-fee:n (RBF) selitys



**Määritelmä**: Replace-by-fee (RBF) on Bitcoin-verkon ominaisuus, jonka avulla lähettäjä voi nopeuttaa **ketjussa** tapahtuvan transaktion vahvistamista suostumalla maksamaan korkeamman maksun.



**Rajat** :




- RBF ei ole käytettävissä Liquid- tai Lightning-tapahtumien yhteydessä.
- Alkuperäisen tapahtuman on oltava merkitty RBF-yhteensopivaksi, kun se luodaan, minkä Bull Bitcoin Mobile tekee automaattisesti, ellei sitä ole poistettu käytöstä.



**Lisätietoa:**




- [Sanasto](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Parhaat käytännöt



Jos haluat käyttää **Bull Bitcoin Mobilea** turvallisesti ja tehokkaasti, noudata seuraavia suosituksia. Ne auttavat sinua suojaamaan varojasi, optimoimaan tapahtumasi ja säilyttämään luottamuksellisuutesi **Bitcoin (onchain)**-, **Liquid**- ja **Lightning**-verkoissa.





- Turvaa palautuslausekkeesi** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Käytä suojattua todennusta** :
 - Aktivoi **vahva PIN-koodi** tai **biometrinen tunnistus** (sormenjälki tai kasvojentunnistus) sovelluksen käytön suojaamiseksi.
 - Älä koskaan jaa PIN-koodia tai biometrisiä tietoja.





- Suojaa yksityisyytesi** :
 - generate uusi Address jokaista onchain- tai Liquid-vastaanottoa varten, jotta Blockchain:n jäljitystä voidaan rajoittaa.
 - Käytä PayJoin:tä, kun se on saatavilla, jotta ketjussa lähetetyn määrän luottamuksellisuus lisääntyy
 - Jos haluat maksimaalisen luottamuksellisuuden, yhdistä Wallet omaan Bitcoin-solmuun Electrum-palvelimen kautta sen sijaan, että käyttäisit julkista solmua





- Valitse tarpeisiisi parhaiten sopiva verkko** :
 - Onchain**: (palkkiot ovat vähäisiä suhteessa määrään).
 - Liquid**: Käytä nopeisiin, edullisiin siirtoihin, joissa on parempi luottamuksellisuus.
 - Salama**: Valitse välitön, edullinen siirto pienille summille. Jos sinulla on kaksi Wallet Bull Bitcoin -käyttäjää, valitse Liquid välttääksesi Lightning <> Liquid -vaihtomaksut Boltzin kautta.





- Tarkista aina toimitusosoitteet** :
 - Tarkista Address huolellisesti ennen varojen lähettämistä. Väärään Address:een lähetetyt varat menetetään lopullisesti. Käytä kopiointia/liittämistä tai QR-koodin skannausta, älä koskaan kopioi/muuta Address:ta käsin.





- Optimoi kustannukset** :
 - Valitse ketjutapahtumille sopivat maksut (hidas, keskitasoinen, nopea) kiireellisyyden ja verkon ruuhkautumisen mukaan.
 - Käytä Liquid:a tai Lightningia pieniin määriin.
 - Aktivoi Replace-by-fee (RBF) (ks. liite 4) ketjulähetyksiä varten, jos ennakoit tarvetta nopeuttaa vahvistusta.





- Pidä hakemus ajan tasalla




### A4. Lisäresurssit





- Viralliset linkit ja tuki:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : tukisähköpostiosoite
 - [Bull Bitcoin:n virallinen verkkosivusto](https://bullbitcoin.com/) :** Tietoa Bull Bitcoin:n palveluista, tilin luominen, sovelluksen käyttömahdollisuudet
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Katso koodia, kehitystä ja etenemissuunnitelmaa, osallistu kehitykseen ja...
 - [Tili X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Telegram**-ryhmä Wallet-mobiililaitteelle: ryhmäkeskustelu tuen kanssa, katso "Asetukset"-sivu.





- Kortteleiden tutkijat :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Salama: **[1ML (Lightning Network)](https://1ml.com/)**





- Oppiminen ja opetusohjelmat:** **[Plan ₿ Network](https://planb.network/)** :
 - Elvytyslausekkeen turvaaminen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Sanasto](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Sanasto](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Yrityksen yleiskatsaus



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, on vanhin ei-talletusmuotoinen Exchange-foorumi, joka on omistettu yksinomaan Bitcoin:lle, ja se perustettiin vuonna 2013 Bitcoin-suurlähetystössä Montrealissa, Kanadassa. Yrityksen johtajana toimii Francis Pouliot, joka on tunnustettu Bitcoin-ekosysteemin pioneeri, ja se on keskeinen toimija taloudellisen riippumattomuuden ja käyttäjien itsenäisyyden edistämisessä. Sen tehtävänä on antaa yksityishenkilöille mahdollisuus saada rahansa hallinta takaisin käyttämällä Bitcoin:a vapauden ja maksamisen välineenä ja hylkäämällä samalla fiat-valuutat ja muut kryptovaluutat kuin Bitcoin.



![image](assets/fr/26.webp)



[Luo tili](https://app.bullbitcoin.com/registration/orangepeel) 0,25% alennuksella Bitcoin-ostoksista ja -myynneistä.



#### Arvot ja filosofia



Bull Bitcoin erottuu edukseen Commitment-Cypherpunk-periaatteidensa ja Bitcoin-etiikkansa ansiosta:





- Yksinomainen keskittyminen Bitcoin:een** : Alusta on uskollinen visiolle hajautetusta, sensuurin kestävästä valuutasta.





- Muu kuin säilyttäjä** : Käyttäjät säilyttävät täyden määräysvallan Bitcoineihinsa lähettämällä varoja omiin salkkuihinsa.





- Luottamuksellisuus**: KYC-vapaat ostovaihtoehdot alle 999 USD:n tapahtumille. Tiedot on suojattu säännösten mukaisesti (FINTRAC Kanadassa, AMF Ranskassa).





- Avoimuus**: Kulut sisältyvät hintaan (osto- ja myyntihintojen erotus).





- Taloudellinen riippumattomuus**: Bull Bitcoin edistää riippumattomuutta perinteisistä pankkijärjestelmistä ja keskitetyistä laitoksista.



#### Tärkeimmät palvelut





- Fiatin talletus** : Käyttäjät voivat tallettaa Bull Bitcoin -tililleen fiat-valuuttaa (CAD, EUR jne.) pankkisiirrolla tai käteisellä/pankkikortilla tietyissä Kanadan postitoimistoissa.





- Bitcoin** ostaminen : Käyttäjät voivat ostaa Bitcoin:n, joka lähetetään suoraan omaan salkkuunsa, joka ei ole säilytyspaikka, mikä takaa varojen täydellisen hallinnan.





- Suunniteltu Bitcoin-ostos**: Bull Bitcoin tarjoaa automaattisen toistuvan ostopalvelun (DCA - Dollar Cost Averaging) säännöllisin väliajoin käytettävissä olevasta saldostasi, ja Bitcoins siirretään suoraan käyttäjän hallitsemaan Wallet:een, mikä vähentää hintavaihteluiden vaikutusta.



Huomaa, että "AutoBuy"-vaihtoehdon avulla voit muuntaa fiatteja heti, kun ne koskettavat Bull Bitcoin -saldoasi, ja lähettää bitcoinit omaan Wallet:een. Tämä vaihtoehto voidaan myös yhdistää pankkisi kanssa ajoitettuun toistuvaan pankkisiirtoon DCA:n tekemiseksi. Tämä vaihtoehto automatisoi Bitcoin-kertymäsi ilman, että sinun tarvitsee koskaan avata sovellusta.






- Osta Bitcoin kiinteään hintaan 'Limit Order'**: Se toteutetaan automaattisesti, kun Bull Bitcoin -indeksin hinta saavuttaa tai alittaa asetetun rajan.





- Myydään Bitcoin**: Käyttäjät voivat myydä Bitcoinejaan ja saada varat fiat-valuutassa suoraan pankkitililleen pankki- tai SEPA-siirrolla.





- Kolmannen osapuolen maksut**: Bull Bitcoin:n avulla käyttäjät voivat lähettää fiat-rahaa pankkitileille bitcoineistaan täysin läpinäkyvästi vastaanottajalle.





- Bull Bitcoin Prime**: Bull Bitcoin Prime on varakkaille ja yritysasiakkaille tarkoitettu premium-palvelu, joka tarjoaa räätälöityjä ratkaisuja ja ensiluokkaista tukea. Siihen sisältyy pääsy alennettuihin maksuihin, oma tilinhoitaja ja räätälöityjä yrityspalveluja. Tämä palvelu on suunnattu instituutioille, ammattimaisille kauppiaille ja yritysasiakkaille, jotka haluavat syvällistä asiantuntemusta ja ensisijaista kohtelua.





- Mobiili Wallet**: Bull Bitcoin tarjoaa avoimen lähdekoodin omaehtoisen Wallet-mobiililaitteen, joka on saatavilla Android- ja iOS-käyttöjärjestelmillä ja joka tukee onchain-, Liquid- ja Lightning Network-tapahtumia.





- Koulutuksellinen tuki**: Maksuttomat oppaat ja henkilökohtainen valmennus, jotka auttavat käyttäjiä luomaan, turvaamaan ja hallinnoimaan Bitcoin-salkkujaan ja vahvistavat taloudellista itsenäisyyttä.



#### Vaatimustenmukaisuus ja turvallisuus





- Sääntely**: Bull Bitcoin täyttää KYC/AML-vaatimukset.





- Turvallisuus**: Suojattujen salkkujen ja offline-tallennussuositusten käyttö. Henkilötietoja säilytetään Bullin Bitcoin-infrastruktuurissa, joka on 100-prosenttisesti itse isännöity eikä ole riippuvainen mistään kolmannesta osapuolesta.