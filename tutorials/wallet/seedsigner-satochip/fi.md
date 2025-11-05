---
name: Satochip x SeedSigner
description: Kuinka käyttää Satochipiä SeedSignerin kanssa?
---

![cover](assets/cover.webp)



*Kiitos [Crypto Guide](https://www.youtube.com/@CryptoGuide/) sen fork of the SeedSigner firmware for smartcard support, jota käytämme tässä opetusohjelmassa



---

Satochip on wallet-älykorttimuotoinen laitteisto, jossa on EAL6+-sertifioitu tietoturvaelementti, joka on yksi korkeimmista turvallisuusstandardeista. Sen on suunnitellut ja valmistaa samanniminen belgialainen yritys Satochip.



Noin 25 euron hintainen Satochip erottuu kilpailijoista erinomaisen hinta-laatusuhteensa ansiosta. Turvallisen sirunsa ansiosta se kestää fyysisiä hyökkäyksiä. Lisäksi sen sovellusten lähdekoodi on täysin avointa lähdekoodia, joka on lisensoitu *AGPLv3*-lisenssillä.



Toisaalta sen muoto asettaa tiettyjä toiminnallisia rajoituksia. Satochipin suurin haittapuoli on se, että siinä ei ole integroitua näyttöä: käyttäjien on siis allekirjoitettava maksutapahtumat sokeasti ja luotettava ainoastaan tietokoneen näyttöön.



Tämän heikkouden voittamiseksi erityisen mielenkiintoinen kokoonpano on käyttää sitä yhdessä SeedSignerin kanssa. Tässä kokoonpanossa viestintä ei enää tapahdu suoraan tietokoneen ja Satochipin välillä, vaan tietokoneen ja SeedSignerin välisen QR-koodien vaihdon kautta. SeedSigner toimii tällöin luottamusnäyttönä: se näyttää allekirjoitettavat tiedot, kun taas itse allekirjoituksen suorittaa Satochip. Toisin kuin tavanomaisessa SeedSigner-käytössä (tai jopa Seedkeeper-ohjelman kanssa yhdistetyssä käytössä), seed:ta ei koskaan ladata SeedSigneriin. SeedSigneristä tulee siten Satochipin näyttö, mikä poistaa sokeaan allekirjoittamiseen liittyvät riskit.



Jos tarkastelemme ongelmaa toisinpäin, SeedSignerin käyttäminen Satochipin kanssa täyttää SeedSignerin tärkeän aukon: mahdollisuuden tallentaa ja käyttää seed:ää secure element:n sisällä.



Mielestäni tämä kokoonpano tarjoaa useita etuja perinteisiin laitteistolompakoihin verrattuna:




- Satochip maksaa noin 25 euroa, ja koska sovellus on avointa lähdekoodia, voit asentaa sen itse tyhjään älykorttiin. Tämän jälkeen sinun on lisättävä SeedSigner-komponenttien ja älykorttien lukemiseen tarkoitetun laajennuksen kustannukset: riippuen siitä, mistä ostat laitteiston, kokonaiskustannusten pitäisi olla 70-100 euroa.
- Kaikki asennukseen liittyvät ohjelmistot ovat avoimen lähdekoodin ohjelmistoja: SeedSigner-firmware ja Satochip-sovellus.
- Sinä hyödyt sertifioidusta turvallisuustekijästä.
- Konfigurointi voidaan tehdä täysin itse ilman Bitcoin-käyttöön tarkoitettuja laitteita, mikä voi tarjota eräänlaisen uskottavan kieltämisen ja vastustuskyvyn tiettyjä ulkoisia uhkia vastaan (mukaan lukien valtiollinen painostus maasta riippuen). Tämä on myös mielenkiintoinen ratkaisu, jos kaupallisten laitteistojen lompakoiden saatavuus on rajoitettua tai mahdotonta alueellasi.




## 1. Tarvittavat materiaalit



Tämän asennuksen tekemiseen tarvitset seuraavat tarvikkeet:




- Klassisen SeedSignerin tarvitsemat tavanomaiset laitteet :
 - raspberry Pi Zero, jossa on GPIO-nastat,
 - 1.3" Waveshare-näyttö,
 - yhteensopiva kamera,
 - microSD-kortti.



![Image](assets/fr/01.webp)





- SeedSigner-laajennussarja, saatavilla [Satochipin virallisesta kaupasta](https://satochip.io/product/seedsigner-extension-kit/), jonka avulla voit lukea ja kirjoittaa älykortille suoraan SeedSigneristäsi. Toinen vaihtoehto on käyttää [ulkoista älykortinlukijaa](https://satochip.io/product/chip-card-reader/), joka voidaan liittää kaapelilla Raspberry Pi:n Micro-USB-porttiin. En ole kuitenkaan testannut tätä ratkaisua itse;
- [A Satochip](https://satochip.io/product/satochip/) tai vaihtoehtoisesti [tyhjä älykortti](https://satochip.io/product/card-for-diy-project/), johon Satochip-sovellus asennetaan (Satochipin myymä laajennussarja sisältää jo tyhjän älykortin). Satochipin laajennussarja tukee myös [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/) -formaattia. Voit siis halutessasi valita tämän muodon.



![Image](assets/fr/02.webp)



Lisätietoja SeedSignerin kokoamiseen tarvittavista laitteista on tämän toisen opetusohjelman osassa 1:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Asenna laiteohjelmisto



Jos haluat käyttää SeedSigneria Satochipin kanssa, sinun on asennettava vaihtoehtoinen laiteohjelmisto, joka eroaa alkuperäisen SeedSignerin laiteohjelmistosta, jotta se tukee älykortin lukemista. Tätä varten [suosittelen fork:n käyttämistä "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Lataa [uusin versio kuvasta](https://github.com/3rdIteration/seedsigner/releases) (`.zip`), joka vastaa käyttämääsi Raspberry Pi -mallia.



![Image](assets/fr/03.webp)



Jos sinulla ei vielä ole sitä, lataa [Balena Etcher] -ohjelmisto (https://etcher.balena.io/) ja toimi sitten seuraavasti:




- Aseta microSD-kortti tietokoneeseen;
- Launch Etcher ;
- Valitse juuri lataamasi `.zip`-tiedosto;
- Valitse kohteeksi microSD-kortti;
- Klikkaa `Flash!`.



![Image](assets/fr/04.webp)



Odota, että prosessi on valmis: microSD-korttisi on nyt käyttövalmis. Voit nyt siirtyä laitteen kokoamiseen.



Lisätietoja laiteohjelmiston asentamisesta ja ohjelmiston tarkistamisesta (suosittelen vahvasti, että teet sen) on seuraavassa oppaassa:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Älykortinlukijan kokoaminen



Aloita asentamalla kamera Raspberry Pi Zeroon asettamalla se varovasti kameratappiin ja lukitsemalla se mustalla kielekkeellä. Aseta sitten Pi kotelon pohjalle ja varmista, että portit kohdistuvat vastaaviin aukkoihin.



![Image](assets/fr/05.webp)



Liitä sitten älykortinlukija Raspberry Pi Zeron GPIO-nastoihin.



![Image](assets/fr/06.webp)



Liu'uta muovinen suojus älykortinlukijan päälle, kunnes se on oikein paikallaan.



![Image](assets/fr/07.webp)



Lisää sitten näyttö laajennuksen GPIO-nastoihin.



![Image](assets/fr/08.webp)



Aseta lopuksi laiteohjelmiston sisältävä microSD-kortti Raspberry Pi Zeron sivuporttiin.



![Image](assets/fr/09.webp)



Voit nyt liittää SeedSignerin joko Raspberry Pi Zeron Micro-USB-portin tai laajennuksen USB-C-portin kautta. Molemmat vaihtoehdot toimivat. Odota muutama sekunti käynnistystä, minkä jälkeen sinun pitäisi nähdä tervetuliaisnäyttö.



![Image](assets/fr/10.webp)



Jos haluat lisätietoja SeedSignerin alkuasetuksista, suosittelen, että tutustut seuraavan ohjeen osaan 4:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flashaa älykortti Satochip-sovelluksella (valinnainen)



Jos sinulla on jo Satochip, voit ohittaa tämän vaiheen ja siirtyä suoraan vaiheeseen 4. Tässä osassa tarkastellaan, miten Satochip-sovellus asennetaan tyhjään älykorttiin (DIY-menetelmä). Appletti on yksinkertaisesti pieni älykortilla toimiva ohjelma, jonka avulla voimme hallita tiettyjä toimintoja.



Aloita avaamalla SeedSignerisi `Tools > Smartcard Tools` -valikko.



![Image](assets/fr/11.webp)



Valitse sitten `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Aseta älykorttisi SeedSigner-lukijaan siru alaspäin ja valitse `Satochip`-sovellus.



![Image](assets/fr/13.webp)



Ole kärsivällinen asennuksen aikana: prosessi voi kestää useita kymmeniä sekunteja.



![Image](assets/fr/14.webp)



Kun sovellus on asennettu onnistuneesti, voit siirtyä vaiheeseen 4.



![Image](assets/fr/15.webp)




## 5. seed:n luominen ja tallentaminen



### 5.1. Luo seed



Nyt kun kaikki laitteistosi ja ohjelmistosi toimivat kunnolla, voit aloittaa Bitcoin-salkun luomisen. Kytke SeedSigner ja generate sitten seed kuten tavallisessa SeedSignerissä, joko heittämällä noppaa tai ottamalla valokuva:




- Mene valikkoon `Työkalut > Kamera / Nopanheitot`;
- Seuraa sitten entropian tuottamisprosessia valitun menetelmän mukaisesti;
- Varmuuskopioi seed fyysiselle tietovälineelle ja tarkista varmuuskopio huolellisesti.



![Image](assets/fr/16.webp)



Jos haluat nähdä tämän menettelyn yksityiskohdat, seuraa tämän ohjeen osaa 5:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. seed:n tallentaminen siementenkasvattajalle



Kun seed on luotu, se on vain tämän kerran SeedSignerin RAM-muistissa. Minun tapauksessani haluan tallentaa sen [Seedkeeper](https://satochip.io/product/seedkeeper/), joka on toinen salaisuuksien säilyttämiseen suunniteltu Satochipin tuote. Käytän tätä laitetta viimeisenä keinona, jos Satochipini katoaa.



Tässä valittu varmuuskopiointistrategia riippuu mieltymyksistäsi, mutta on ehdottoman tärkeää, että sinulla on ainakin yksi kopio muistisääntöjä sisältävästä lauseesta joko fyysisellä tietovälineellä (paperilla tai metallilla) tai, kuten tässä tapauksessa, Seedkeeperissä. Voit myös moninkertaistaa varmuuskopioiden määrän tarpeen mukaan. Jos haluat lisätietoja salkun varmuuskopiointistrategioista, suosittelen lukemaan tämän opetusohjelman :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Jos haluat varmuuskopioida seed:n Seedkeeperillä, siirry suoraan `Backup Seed` -valikkoon.



![Image](assets/fr/17.webp)



Aseta sitten Seedkeeper älykortinlukijaan ja valitse `To SeedKeeper`.



![Image](assets/fr/18.webp)



Anna PIN-koodi avataksesi lukituksen.



![Image](assets/fr/19.webp)



Valitse `Label`, jotta voit helposti tunnistaa Seedkeeperiin tallennetut eri salaisuutesi. Voit esimerkiksi säilyttää wallet-merkin tai ilmoittaa nimenomaisesti `Seed`. Valinta riippuu mieltymyksestäsi ja riskeistäsi.



![Image](assets/fr/20.webp)



Jos varmuuskopiointistrategiasi perustuu pelkästään tähän Seedkeeperiin, suosittelen, että suoritat nyt tyhjän palautustestin ja vertaat sitten sormenjälkiä tarkistaaksesi, että varmuuskopiointi toimii.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper PIN-koodin olisi oltava mahdollisimman pitkä ja satunnainen, jotta estetään raa'an väkivallan yritykset kortin fyysisen vaarantamisen yhteydessä. PIN-koodista on myös pidettävä varmuuskopio, joka on tallennettu Seedkeeperistä erilliseen paikkaan. Ilman tätä PIN-koodia et pääse käsiksi Seedkeeperiin tallennettuun muistikirjaan, ja bitcoinisi menetetään pysyvästi.



### 5.3. Tallenna seed Satochipissä



Nyt kun salkkusi on luotu, tallennettu ja vahvistettu, siirrämme sen Satochipiin. Varmista tätä varten, että seed on ladattu SeedSignerin RAM-muistiin. Siirry sitten kohtaan `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Aseta Satochip älykortinlukijaan ja valitse sitten `Initialise with Seed`.



![Image](assets/fr/22.webp)



Laite pyytää sinua syöttämään Satochipin PIN-koodin; koska kortti on uusi ja alustamaton, PIN-koodia ei ole vielä olemassa. Syötä mikä tahansa koodi ohittaaksesi tämän vaiheen (se ei ole estävä).



![Image](assets/fr/23.webp)



SeedSigner havaitsee, että Satochipiäsi ei ole alustettu. Vahvista se napsauttamalla `I Understand`.



![Image](assets/fr/24.webp)



Tämän jälkeen voit asettaa Satochipin PIN-koodin, jonka pituus on 4-16 merkkiä. Vahvistaaksesi wallet:n turvallisuutta valitse pitkä, satunnainen koodi: se on ainoa suoja muistilauseen fyysistä käyttöä vastaan.



Muista tallentaa PIN-koodi heti sen luomisen jälkeen joko turvalliseen salasanahallintaohjelmaan tai fyysiselle tietovälineelle henkilökohtaisen strategiasi mukaan. Jälkimmäisessä tapauksessa varmista, ettet koskaan säilytä PIN-koodin sisältävää tallennusvälinettä samassa paikassa kuin Satochip-sovellusta, sillä muuten suojaus on hyödytön. On tärkeää, että sinulla on varmuuskopio: ** Ilman tätä PIN-koodia et pääse käsiksi seed:een, ja bitcoinisi menetetään lopullisesti**.



![Image](assets/fr/25.webp)



SeedSigner kysyy sitten, minkä seed:n haluat tuoda Satochipiin. Valitse se, jonka sormenjälki vastaa juuri luomasi salkun sormenjälkeä.



![Image](assets/fr/26.webp)



seed on nyt tuotu Satochipiin.



![Image](assets/fr/27.webp)



Voit nyt kytkeä SeedSignerin pois päältä.



Jos haluat käyttää passphrase BIP39:ää wallet:n turvallisuuden parantamiseksi, katso tämän ohjeen osa 6:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Tuo wallet Sparrow:een



Nyt kun salkkusi on valmiina ja toiminnassa, tuomme sen julkiset tiedot (*keystore*) Sparrow Wallet:een tai muuhun salkunhallintaohjelmistoon. Tätä ohjelmistoa käytetään transaktioiden luomiseen, jakeluun ja seurantaan. Se ei kuitenkaan pysty allekirjoittamaan niitä, sillä vain Satochipissä (ja mahdollisissa varmuuskopioissa) on tähän tarvittavat yksityiset avaimet.



### 6.1 SeedSignerin ja Satochipin valmistelu



Aseta käyttöjärjestelmän sisältävä microSD-kortti paikalleen ja käynnistä sitten SeedSigner. Tällä hetkellä se ei voi tehdä mitään, koska se ei vielä tunne seed:ääsi. Sinun on aloitettava asettamalla Satochip älykortinlukijaan, koska siinä on seed:si.



Siirry aloitusnäytöstä valikkoon `Työkalut > Älykorttityökalut > Satochip-toiminnot`.



![Image](assets/fr/28.webp)



Napsauta sitten `Export Xpub`.



![Image](assets/fr/29.webp)



Valitse salkkutyyppi. Meidän tapauksessamme kyseessä on yksittäinen salkku: valitse `Single Sig`.



![Image](assets/fr/30.webp)



Seuraavaksi on vuorossa skriptistandardin valinta. Valitse uusin: `Native SegWit`.



![Image](assets/fr/31.webp)



Valitse lopuksi "Koordinaattori" eli salkunhallintaohjelmisto, jota haluat käyttää. Tässä tapauksessa käytämme Sparrow Wallet:ta.



![Image](assets/fr/32.webp)



Näyttöön tulee varoitusviesti: tämä on täysin normaalia. Laajennetun julkisen avaimen (`xpub`) avulla voit tarkastella kaikkia seed:sta johdettuja osoitteita (ensimmäisellä tilillä). Se ei kuitenkaan anna pääsyä varoihisi: sen paljastaminen vaarantaisi yksityisyytesi, mutta ei bitcoinien turvallisuutta. Toisin sanoen sen avulla voit tarkkailla saldojasi, mutta et käyttää niitä.



Napsauta `Ymmärrän`.



![Image](assets/fr/33.webp)



Anna sitten Satochipin PIN-koodi avataksesi sen lukituksen. Tämä on koodi, jonka määrittelit ja tallensit vaiheessa 5.



![Image](assets/fr/34.webp)



Napsauta lopuksi `Export Xpub`, jos olet tyytyväinen näytettyihin tietoihin.



![Image](assets/fr/35.webp)



Sen jälkeen SeedSigner luo xpubin dynaamisen QR-koodin muodossa, joka sisältää kaikki tiedot, joita tarvitset salkkusi hallintaan Sparrow Wallet:ssä. Voit säätää näytön kirkkautta joystickillä, jotta QR-koodin skannaaminen olisi helpompaa.



### 6.2 Uuden salkun tuominen Sparrow Wallet:ään Wallet:ään



Varmista, että Sparrow Wallet -ohjelmisto on asennettu tietokoneeseen. Jos et tiedä, miten se ladataan, tarkistetaan sen aitous ja asennetaan oikein, katso koko ohjeemme aiheesta :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Avaa tietokoneessa Sparrow Wallet ja valitse sitten valikkoriviltä "Tiedosto → Tuo Wallet".



![Image](assets/fr/36.webp)



Selaa alaspäin kohtaan `SeedSigner` ja valitse sitten `Scan...`. Webbikamerasi aktivoituu: skannaa SeedSigner-näytössä näkyvä dynaaminen QR-koodi.



![Image](assets/fr/37.webp)



Anna salkullesi nimi ja napsauta sitten `Create Wallet`. Sparrow pyytää sinua asettamaan salasanan, jolla lukitset paikallisen pääsyn tähän wallet:een. Valitse vahva salasana: se suojaa tietojasi Sparrow:ssa (julkiset avaimet, osoitteet, tarrat ja tapahtumahistoria). Tätä salasanaa ei kuitenkaan tarvita wallet:n palauttamiseen tulevaisuudessa: vain muistisana (ja mahdollisesti passphrase) tarvitaan.



Suosittelen, että tallennat tämän salasanan salasanahallintaohjelmaan, jotta et menetä sitä.



![Image](assets/fr/38.webp)



Avaintallennustietokantasi on onnistuneesti tuotu.



![Image](assets/fr/39.webp)



Tarkista nyt, että Sparrow:ssa Wallet:ssä näkyvä `Master fingerprint` vastaa SeedSigneristäsi aiemmin löytynyttä sormenjälkeä.



Sen jälkeen SeedSigner pyytää sinua skannaamaan satunnaisen vastaanotto-osoitteen Sparrow wallet:sta vahvistaaksesi tuonnin oikeellisuuden.



![Image](assets/fr/40.webp)



Satochip (SeedSignerin kautta) ja Sparrow Wallet ovat nyt turvallisesti yhteydessä toisiinsa. Sparrow toimii täydellisenä hallintaliittymänä, kun taas Satochip on ainoa laite, joka pystyy allekirjoittamaan tapahtumasi. Olet nyt valmis vastaanottamaan ja lähettämään bitcoineja täysin ilmassa olevassa kokoonpanossa.



![Image](assets/fr/41.webp)



## 7. Bitcoinien vastaanottaminen ja lähettäminen



Satochip ja Sparrow Wallet on nyt määritetty toimimaan yhdessä. Tässä osiossa selitämme askel askeleelta, miten voit vastaanottaa ja lähettää bitcoineja tässä tilassa.



### 7.1 Bitcoinien vastaanottaminen



#### 7.1.1 Vastaanotto-osoitteen luominen



Avaa tietokoneellasi Sparrow Wallet ja avaa `Satochip-SeedSigner` wallet lukitus salasanalla. Tarkista, että ohjelmisto on yhdistetty palvelimeen (ilmaisin oikeassa alakulmassa). Napsauta sitten sivupalkissa `Vastaanottaa`.



![Image](assets/fr/42.webp)



Uusi Bitcoin-osoite tulee näkyviin. Löydät :




- Osoite tekstimuodossa (alkaa kirjaimella `bc1q...`, jos käytät P2WPKH:ää, kuten tässä esimerkissä) ;
- Liittyvä QR-koodi ;
- `Label`-kenttä, joka on hyödyllinen tapahtumien jäljittämisessä.



Suosittelen lämpimästi, että lisäät tarran jokaiseen bitcoin-kuittiin wallet:ssa. Näin voit helposti tunnistaa jokaisen UTXO:n alkuperän ja hallita yksityisyyttäsi paremmin. Jos haluat lisätietoja tästä tärkeästä aiheesta, tutustu Plan ₿ Academyn omaan koulutukseen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Voit lisätä etiketin yksinkertaisesti kirjoittamalla nimen `Label`-kenttään ja vahvistamalla sen jälkeen.



Esimerkiksi:



```txt
Label : Sale of the Raspberry Pi Zero
```



Osoitteesi on nyt yhdistetty tähän merkkiin kaikissa Sparrow-osastoissa.



![Image](assets/fr/43.webp)



#### 7.1.2 Address-tarkastus SeedSignerissa



Ennen kuin ilmoitat vastaanotto-osoitteesi maksajalle, on tärkeää tarkistaa, että se kuuluu seed:lle. Tällä vaiheella varmistetaan, että Satochip pystyy allekirjoittamaan tähän osoitteeseen liittyvät tapahtumat. Se estää myös mahdolliset hyökkäykset, joissa Sparrow näyttää väärän osoitteen. Muista, että Sparrow toimii turvattomassa ympäristössä (tietokoneessasi), jonka hyökkäyspinta on paljon suurempi kuin Satochipin, joka on täysin eristetty. Tämän vuoksi sinun ei pitäisi koskaan luottaa sokeasti Sparrow:n näyttämiin osoitteisiin, ennen kuin tarkistat ne wallet-laitteistossasi.



Sparrow:ssä voit suurentaa osoitteen QR-koodia napsauttamalla sitä, jolloin se näkyy koko näytön kokoisena.



![Image](assets/fr/44.webp)



Aseta Satochip SeedSigner-laitteessa lukijaan ja valitse päävalikosta `Scan`. Skannaa tietokoneessa näkyvä QR-koodi ja valitse sitten `Käytä Satochip-korttia`.



![Image](assets/fr/45.webp)



Vahvista sitten käytetyn komentosarjan tyyppi (tässä tapauksessa `Native SegWit`), syötä Satochipin PIN-koodi sen lukituksen avaamiseksi ja vahvista `xpub`-tiedot.



![Image](assets/fr/46.webp)



Jos skannattu osoite vastaa seed:sta saatua osoitetta, SeedSigner näyttää viestin: "Address vahvistettu".



![Image](assets/fr/47.webp)



Näin voit olla varma, että osoite kuuluu salkkuusi.



#### 7.1.3 Varojen vastaanottaminen



Voit nyt lähettää tämän osoitteen tekstimuodossa tai QR-koodin avulla henkilölle tai osastolle, jonka on lähetettävä sinulle satss. Kun tapahtuma on lähetetty verkossa, se näkyy Sparrow Wallet:n `Transaktiot`-välilehdellä.



![Image](assets/fr/48.webp)



### 7.2 Lähetä bitcoineja



Bitcoinien lähettäminen Satochip-SeedSigner-kokoonpanolla sisältää 3 vaihetta:




- Tapahtuman luominen Sparrow:ssä ;
- Tämän tapahtuman allekirjoittaminen Satochipissä SeedSigner-ohjelman kautta ;
- Lopuksi tapahtuma lähetetään verkon kautta Sparrow:sta.



Kaikki näiden kahden laitteen välinen vaihto tapahtuu yksinomaan QR-koodien avulla.



#### 7.2.1 Tapahtuman luominen Sparrow:ssa



Sparrow Wallet:ssä voit luoda tapahtuman napsauttamalla vasemmanpuoleisen sivupalkin Lähetä-välilehteä. Käytän kuitenkin mieluummin `UTXOs`-välilehteä, jonka avulla voit harjoitella *Coin Control*. Tämä menetelmä tarjoaa tarkan valvonnan käytetyille UTXO:ille, jotta voit rajoittaa tapahtumien aikana paljastuvia tietoja.



Valitse `UTXOs`-välilehdeltä kolikot, jotka haluat käyttää, ja napsauta sitten `Send Selected`.



![Image](assets/fr/49.webp)



Täytä sitten tapahtumakentät:




- Liitä vastaanottajan osoite kohtaan "Maksa vastaanottajalle" tai skannaa hänen QR-koodinsa kamerakuvakkeella ;
- Lisää kohtaan `Label` merkintä, jolla tämä kulu voidaan jäljittää;
- Kirjoita lähetettävä summa kohtaan `Määrä`;
- Valitse lopuksi latausnopeus nykyisten verkko-olosuhteiden mukaan (arviot ovat saatavilla osoitteessa [mempool.space](https://mempool.space/)).



Kun olet täyttänyt kaikki kentät, tarkista tiedot huolellisesti ja napsauta sitten "Luo tapahtuma >>".



![Image](assets/fr/50.webp)



Tarkista tapahtuman tiedot vielä kerran niiden oikeellisuuden varmistamiseksi ja napsauta sitten "Viimeistele tapahtuma allekirjoitusta varten".



![Image](assets/fr/51.webp)



Kauppa on nyt valmis, mutta sitä ei ole vielä allekirjoitettu. Jos haluat näyttää [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) QR-koodina, napsauta `Show QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Kaupan allekirjoittaminen Satochipin kanssa



Käynnistä SeedSigner ja aseta Satochip tavalliseen tapaan. Valitse aloitusnäytöltä `Scan` ja skannaa sitten Sparrow:ssä näkyvä QR-koodi.



![Image](assets/fr/53.webp)



Valitse vaihtoehto `Käytä Satochip-korttia`.



![Image](assets/fr/54.webp)



Anna PIN-koodi älykortin lukituksen avaamiseksi.



![Image](assets/fr/55.webp)



SeedSigner havaitsee, että kyseessä on PSBT, ja näyttää yhteenvedon tapahtumasta:




   - Lähetetty määrä,
   - Kohdeosoitteet,
   - Siihen liittyvät transaktiokustannukset.



Klikkaa `Review Details` ja tutki kaikki tiedot suoraan SeedSignerin näytöllä. Tärkeimmät tarkistettavat kohdat ovat lähetetyt summat, kohdeosoitteet ja transaktiomaksut.



![Image](assets/fr/56.webp)



Jos kaikki on kunnossa, valitse "Hyväksy PSBT" allekirjoittaaksesi tapahtuman Satochipin avulla.



![Image](assets/fr/57.webp)



Kun allekirjoitus on valmis, SeedSigner luo uuden QR-koodin, joka sisältää allekirjoitetun tapahtuman ja on valmis skannattavaksi Sparrow:lla.



#### 7.2.3 Tapahtuman lähetys Sparrow:sta



Nyt kun transaktio on allekirjoitettu ja validoitu, se täytyy vain lähettää Bitcoin-verkkoon, jotta louhija voi sisällyttää sen lohkoon. Napsauta Sparrow:ssä `Scan QR`.



![Image](assets/fr/58.webp)



Näytä SeedSignerissä näkyvä QR-koodi (allekirjoitetun tapahtuman sisältävä koodi) web-kameraan. Sparrow näyttää sitten kaikki tapahtuman tiedot. Tarkista, että kaikki tiedot ovat oikein, ja lähetä transaktio Bitcoin-verkkoon napsauttamalla "Broadcast Transaction".



![Image](assets/fr/59.webp)



Tapahtumasi on nyt lähetetty verkkoon. Voit seurata sen vahvistusta Sparrow Wallet:n `Transaktiot`-välilehdeltä.



![Image](assets/fr/60.webp)



## 8. Hanki wallet takaisin



Kuten olemme nähneet edellisissä osioissa, turvallisuusstrategiastasi riippuen on useita tapoja varmuuskopioida palautuslauseesi Satochipin lisäksi:




- Klassisen *SeedQR*:n käyttäminen SeedSignerin kanssa ;
- Tallentamalla muistilause fyysiselle tietovälineelle;
- Tai tallentamalla se Seedkeeperiin, kuten kohdassa 5.2 selitetään.



Joka tapauksessa on kaksi päätilannetta, joissa sinun on puututtava asiaan: Satochipin menetys tai SeedSignerin menetys. Katsotaanpa, miten toimia kummassakin tilanteessa.



### 8.1. Hae wallet Satochipin avulla



Jos sinulla on yhä Satochip, mutta SeedSigner on rikki tai kadonnut, tilanne on melko helppo hallita, koska wallet on yhä Satochipissä.



Paras vaihtoehto on suositella tarvittavia komponentteja ja rakentaa uusi SeedSigner tyhjästä. Koska kyseessä on "tilaton" laite, ei ole väliä, käytätkö samaa vai toista SeedSigneria: kunhan voit asettaa Satochipin, kaikki toimii normaalisti.



Jos et halua rakentaa sellaista uudelleen, voit käyttää Satochipiäsi myös perinteisellä tavalla eli suoraan tietokoneeltasi ilman SeedSigneria. Tämä menetelmä toimii täydellisesti, mutta se heikentää huomattavasti Bitcoin wallet:n turvallisuutta: menetät "*ilmanvahdin*" eristyksen ja sinun on nyt allekirjoitettava sokeasti, koska SeedSigner toimi luotettuna näytönä. Tämä voi kuitenkin olla väliaikainen ratkaisu hätätilanteessa tai jos et pysty rakentamaan SeedSigneria uudelleen.



Tätä varten tarvitset USB-älykortin tai NFC-lukijan. Avaa wallet, jonka haluat palauttaa Sparrow:ssä, siirry sitten "Asetukset"-välilehdelle ja valitse "Korvaa".



![Image](assets/fr/61.webp)



Aseta Satochip tietokoneeseen kytkettyyn älykortinlukijaan ja napsauta sitten Satochipin vieressä olevaa kohtaa `Import`.



![Image](assets/fr/62.webp)



Kirjoita lopuksi älykortin PIN-koodi avataksesi lukituksen. Sen jälkeen voit käyttää wallet:ää, luoda maksutapahtumia ja allekirjoittaa ne suoraan liitetyn Satochipin avulla.



### 8.2. Hae salkkusi SeedSignerin avulla



Toinen, arkaluontoisempi skenaario on se, että menetät pääsyn seed:n sisältävään Satochip-tietokoneeseesi: se voi olla rikki, kadonnut, varastettu tai olet unohtanut sen PIN-koodin. Jos Satochipisi on varastettu tai kadonnut, suosittelemme vahvasti, että siirrät bitcoinisi välittömästi uuteen wallet:aan, joka on luotu eri seed:llä, heti kun varojesi käyttöoikeus on palautettu. Näin varmistetaan, että mahdollinen hyökkääjä ei koskaan pääse käsiksi satsiisi.



Jos haluat saada salkkusi takaisin käyttöösi ja siirtää varojasi, lataa seed-rahastosi SeedSigneriin. Käyttämästäsi varmuuskopiomediasta riippuen sinulla on useita vaihtoehtoja:





- Kirjoita muistisana manuaalisesti valikossa `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Skannaa *SeedQR* klikkaamalla etusivun `Scan`-painiketta.



![Image](assets/fr/64.webp)





- Tai lataa seed Seedkeeperistä valikosta `Seeds > From SeedKeeper` (tätä menetelmää käytän tässä ohjeessa). Sinun tarvitsee vain syöttää Seedkeeper PIN-koodi ja valita salaisuus, jota käytetään seed:na SeedSignerissä.



![Image](assets/fr/65.webp)



Kun seed on ladattu SeedSigneriin, voit allekirjoittaa yhden tai useamman skannaustapahtuman siirtääksesi bitcoinisi uuteen, suojaamattomaan wallet:een. Lue, miten tämä tehdään, seuraavan ohjeen osasta 7.2:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nyt tiedät, miten Satochipin avulla voit hallita Bitcoin-salkkuasi turvallisesti yhdessä SeedSignerin kanssa.



Jos tämä asetelma on vakuuttanut sinut, älä epäröi tukea hankkeita, jotka tekevät sen mahdolliseksi:




- Ostamalla laitteesi suoraan [Satochipin verkkosivuilta](https://satochip.io/shop/);
- Tekemällä [lahjoituksen SeedSigner-hankkeelle](https://seedsigner.com/donate/);
- Tilaamalla [Crypto Guiden YouTube-kanavan](https://www.youtube.com/@CryptoGuide/), jota ylläpitää henkilö, joka ylläpitää GitHub-arkistoa, jossa on tässä ohjeessa käyttämämme muokattu laiteohjelmisto.