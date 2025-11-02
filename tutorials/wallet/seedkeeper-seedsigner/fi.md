---
name: Seedkeeper x SeedSigner
description: Miten käytän Seedkeeperiä SeedSignerin kanssa?
---

![cover](assets/cover.webp)



*Kiitokset [Satochip](https://satochip.io/) -tiimille siitä, että he suostuivat käyttämään [heidän videoitaan](https://www.youtube.com/@satochip/videot) tässä ohjeessa. Kiitos myös [Crypto Guide](https://www.youtube.com/@CryptoGuide/) SeedSigner-ohjelmiston Fork:sta, joka mahdollistaa älykorttien tuen



---

SeedSigner on Hardware Wallet, jonka kokoat itse vakiolaitteistosta, yleensä Raspberry Pi Zeron ympärille. Tätä Wallet:a kutsutaan "*tilattomaksi*": toisin kuin useimmat muut markkinoilla olevat mallit (Coldcard, Trezor, Ledger jne.), se ei tallenna mitään tietoja pysyvään muistiin, vaan se toimii vain RAM-muistista. Tämän seurauksena salkkusi seed ei koskaan tallennu SeedSigneriin. Joka kerta, kun käynnistät sen uudelleen, sinun on täytettävä se, jotta laite voi allekirjoittaa tapahtumasi. Yleisin tapa on tallentaa seed QR-koodina, jonka skannaat joka kerta, kun käytät sitä (*SeedQR*).



Tähän lähestymistapaan liittyy kuitenkin merkittävä riski: seed:n on pysyttävä saatavilla selkeänä tekstinä, jotta se voidaan skannata. Varkauden tai tunkeutumisen sattuessa hyökkääjä voi helposti saada sen haltuunsa ja varastaa bitcoinisi.



Tämän heikkouden poistamiseksi SeedSigner voidaan yhdistää [**Seedkeeper**](https://satochip.io/product/seedkeeper/), Satochipin kehittämän älykortin kanssa. Näin Mnemonic-lauseet (tai muut salaisuudet) voidaan tallentaa secure element-korttiin, joka on suojattu PIN-koodilla. Seedkeeper-sovellus on avointa lähdekoodia, ja sen secure element:lla on EAL6+-sertifiointi. Yhdessä SeedSignerin kanssa käytettynä se tarjoaa erittäin mielenkiintoisen tietoturvaominaisuuden: avaimia hallinnoidaan täysin offline-tilassa, allekirjoitat tapahtumat luotettavalla näytöllä, ja seed on fyysisesti suojattu älykortissa, joka kestää fyysisiä hyökkäyksiä.



Tarvitset asennuksen loppuunsaattamiseen vain seuraavat osat:




- Klassiseen SeedSigneriin tarvitaan tavanomaiset laitteet: Raspberry Pi Zero, Waveshare 1,3" näyttö, yhteensopiva kamera ja microSD-kortti (lisätietoja löydät SeedSigner-oppaasta alla);
- SeedSigner-laajennussarja, joka on saatavilla [Satochipin virallisessa kaupassa](https://satochip.io/product/seedsigner-extension-kit/), jonka avulla voit lukea ja kirjoittaa älykorttiin suoraan SeedSigneristäsi. Toinen vaihtoehto on käyttää ulkoista älykortinlukijaa, joka voidaan liittää kaapelilla Raspberry Pi:n Micro-USB-porttiin. En ole kuitenkaan testannut tätä ratkaisua itse;
- Seedkeeper tai vaihtoehtoisesti tyhjä älykortti, johon Seedkeeper-sovellus asennetaan (Satochipin myymä laajennussarja sisältää jo tyhjän älykortin).



![Image](assets/fr/01.webp)



Tämä opetusohjelma kattaa kaksi skenaariota:




- Jos sinulla on jo Bitcoin-salkku, jota hallitaan SeedSignerin kautta, asenna vain uusi laiteohjelmisto. Voit sitten jatkaa nykyisen Wallet:n käyttöä, mutta tällä kertaa käyttämällä Seedkeeperiä lisäturvallisuuden takaamiseksi.
- Jos sinulla ei ole vielä Bitcoin Wallet:ta yhdistettynä SeedSigneriin, sinun on noudatettava alla mainitun ohjeen vaiheita **5** ja **6**. Näissä kohdissa selitetään, miten generate Mnemonic-lauseen Mnemonic:n ja SeedSignerin välille tallennetaan *SeedQR*:n avulla ja sitten tämä Wallet liitetään Sparrow wallet:een sen hallintaa varten. En käsittele näitä menettelyjä tässä, ja **oletan, että sinulla on jo toimiva Bitcoin Wallet, joka on konfiguroitu Sparrow:llä ja SeedSignerilläsi**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Asenna laiteohjelmisto



Jos haluat käyttää SeedSigneriäsi Seedkeeperillä, sinun on asennettava vaihtoehtoinen laiteohjelmisto, joka eroaa alkuperäisen SeedSignerin laiteohjelmistosta, jotta se tukee älykorttien lukemista. Tätä varten [suosittelen Fork:n käyttöä "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Lataa [uusin versio kuvasta](https://github.com/3rdIteration/seedsigner/releases) (`.zip`), joka vastaa käyttämääsi Raspberry Pi -mallia.



![Image](assets/fr/02.webp)



Jos sinulla ei vielä ole sitä, lataa [Balena Etcher] -ohjelmisto (https://etcher.balena.io/) ja toimi sitten seuraavasti:




- Aseta microSD-kortti tietokoneeseen;
- Launch Etcher ;
- Valitse juuri lataamasi `.zip`-tiedosto;
- Valitse kohteeksi microSD-kortti;
- Klikkaa `Flash!`.



![Image](assets/fr/03.webp)



Odota, että prosessi on valmis: microSD-korttisi on nyt käyttövalmis. Voit nyt siirtyä laitteen kokoamiseen.



Lisätietoja laiteohjelmiston asentamisesta ja ohjelmiston tarkistamisesta (suosittelen vahvasti, että teet sen) on seuraavassa oppaassa:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Älykortinlukijan kokoaminen



![video](https://youtu.be/jqE8HDMCImA)



Aloita asentamalla kamera Raspberry Pi Zeroon asettamalla se varovasti kameratappiin ja lukitsemalla se mustalla kielekkeellä. Aseta sitten Pi kotelon pohjalle ja varmista, että portit kohdistuvat vastaaviin aukkoihin.



![Image](assets/fr/04.webp)



Liitä sitten älykortinlukija Raspberry Pi Zeron GPIO-nastoihin.



![Image](assets/fr/05.webp)



Liu'uta muovinen suojus älykortinlukijan päälle, kunnes se on oikein paikallaan.



![Image](assets/fr/06.webp)



Lisää sitten näyttö laajennuksen GPIO-nastoihin.



![Image](assets/fr/07.webp)



Aseta lopuksi laiteohjelmiston sisältävä microSD-kortti Raspberry Pi Zeron sivuporttiin.



![Image](assets/fr/08.webp)



Voit nyt liittää SeedSignerin joko Raspberry Pi Zeron Micro-USB-portin tai laajennuksen USB-C-portin kautta. Molemmat vaihtoehdot toimivat. Odota muutama sekunti käynnistystä, minkä jälkeen sinun pitäisi nähdä tervetuliaisnäyttö.



![Image](assets/fr/09.webp)



Jos haluat lisätietoja SeedSignerin alkuasetuksista, suosittelen seuraavaa ohjetta:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashaa älykortti Seedkeeper-sovelluksella (valinnainen)



![video](https://youtu.be/NF4HemyEcOY)



Jos sinulla on jo Seedkeeper, voit ohittaa tämän vaiheen ja siirtyä suoraan vaiheeseen 4. Tässä osassa tarkastellaan, miten Seedkeeper-sovellus asennetaan tyhjään älykorttiin (DIY-menetelmä).



Aloita avaamalla SeedSignerisi `Tools > Smartcard Tools` -valikko.



![Image](assets/fr/10.webp)



Valitse sitten `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Aseta älykorttisi SeedSigner-lukijaan siru alaspäin ja valitse sitten `SeedKeeper`-sovellus.



![Image](assets/fr/12.webp)



Ole kärsivällinen asennuksen aikana: prosessi voi kestää useita kymmeniä sekunteja.



![Image](assets/fr/13.webp)



Kun sovellus on asennettu onnistuneesti, voit siirtyä vaiheeseen 4.



![Image](assets/fr/14.webp)



## 4. Tallenna olemassa oleva SeedQR Seedkeeperiin



![video](https://youtu.be/X-vmFHU9Ec8)



Nyt kun Seedkeeper on toiminnassa, voit tallentaa Bitcoin Wallet Mnemonic älykortille. Aloita käynnistämällä SeedSigner tavalliseen tapaan ja skannaa sitten Wallet:n *SeedQR* ladataksesi sen laitteeseen. Kun seed on tuotu, valitse yksinkertaisesti `Done`.



![Image](assets/fr/15.webp)



Kun seed on ladattu, avaa valikko `Backup seed`.



![Image](assets/fr/16.webp)



Aseta sitten Seedkeeper SeedSigner-asemaan ja valitse vaihtoehto `To SeedKeeper`.



![Image](assets/fr/17.webp)



Tämän jälkeen SeedSigner pyytää sinua syöttämään PIN-koodin Seedkeeperiäsi varten. Koska kyseessä on tyhjä kortti, koodia ei ole vielä määritelty. Syötä mikä tahansa koodi ohittaaksesi tämän vaiheen ja vahvista sitten.



![Image](assets/fr/18.webp)



SeedSigner havaitsee, että Seedkeeperiä ei ole vielä alustettu (eli salasanaa ei ole asetettu). Jatka klikkaamalla `I Understand`.



![Image](assets/fr/19.webp)



Valitse nyt siemenenvartijan uusi PIN-koodi, jonka pituus on 4-16 merkkiä. Lisäturvaa saat valitsemalla pitkän, satunnaisen koodin: se on ainoa este, joka suojaa fyysisen pääsyn Mnemonic-lauseeseesi.



Muista tallentaa PIN-koodi heti sen luomisen jälkeen joko luotettavaan salasanahallintaan tai erilliselle fyysiselle tietovälineelle strategiastasi riippuen. Jälkimmäisessä tapauksessa varmista, että PIN-koodin sisältävää tallennusvälinettä ei koskaan säilytetä samassa paikassa kuin Seedkeeperiä, sillä muuten suojaus jää tehottomaksi. On tärkeää, että sinulla on varmuuskopio: ** Ilman tätä PIN-koodia et pääse käsiksi seed:ään, ja bitcoinisi menetetään**.



![Image](assets/fr/20.webp)



Voit sitten määritellä Mnemonic-lauseeseen liittyvän `Label`-merkinnän. Tämä etiketti on hyödyllinen, jos tallennat useita salaisuuksia Seedkeeperiin, jotta voit helposti tunnistaa ne.



![Image](assets/fr/21.webp)



Mnemonic-lauseesi on nyt tallennettu älykorttiin.



![Image](assets/fr/22.webp)



Turvallisuusstrategian osalta on mahdollista valita useita lähestymistapoja tarpeiden ja riskinoton tason mukaan. Itse suosittelen, että säilytät vähintään kaksi kopiota seed:stä:




- Tämä on ensimmäinen älykortti, jota voit pitää helposti saatavilla jokapäiväisiä toimintoja, kuten osoitteiden tarkistamista tai maksutapahtumien allekirjoittamista varten. Menetelmä on käytännöllinen (kuten osassa 5 nähdään) ja turvallinen PIN-koodin tarjoaman suojan ansiosta, joten voit pitää kortin saatavilla ilman suurempia riskejä;
- Toinen kopio salaamattomasta Mnemonic-lausekkeestasi, joka toimii salkkusi lopullisena varmuuskopiona ja jota käytetään vain siinä tapauksessa, että Seedkeeper menetetään tai varastetaan. Koska tämä versio on salaamaton, sitä on säilytettävä erillisessä, turvallisemmassa paikassa, jotta kahden varmuuskopion samanaikainen vaarantuminen voidaan estää.



Suojausstrategiastasi ja riskiprofiilistasi riippuen voit myös kopioida seed:n useisiin eri siemenvartijoihin tai luoda useita fyysisiä kopioita Mnemonic:stä. Jos haluat lisätietoja näistä käytännöistä, tutustu seuraavaan opetusohjelmaan:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. seed:n lataaminen Seedkeeperistä



![video](https://youtu.be/ms0Iq_IyaoE)



Voit nyt käyttää Seedkeeperiäsi lataamaan Mnemonic-lauseesi SeedSigneriin käynnistyksen yhteydessä ja näin allekirjoittaa Bitcoin-tapahtumat. Aloita käynnistämällä SeedSigner kytkemällä se ja avaa sitten `Seeds`-valikko.



![Image](assets/fr/23.webp)



Valitse sitten vaihtoehto `From SeedKeeper`.



![Image](assets/fr/24.webp)



Työnnä Seedkeeper älykortinlukijaan ja avaa lukitus syöttämällä PIN-koodi. Vahvista syöttösi painamalla oikeassa alakulmassa olevaa vahvistuspainiketta, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper voi sisältää useita salaisuuksia, joten SeedSigner pyytää sinua valitsemaan sen, jonka haluat ladata. Näytössä näkyvä etiketti vastaa vaiheessa 4 määrittelemääsi nimeä. Jos, kuten minun tapauksessani, olet rekisteröinyt vain yhden seed:n, vain yksi vaihtoehto on käytettävissä.



![Image](assets/fr/26.webp)



seed on nyt ladattu. Tarkista, että kyseessä on oikea Wallet, vertaamalla näytöllä näkyvää sormenjälkeä Sparrow wallet:n asetuksissa määritettyyn sormenjälkeen. Tämä sormenjälki annettiin myös, kun Wallet luotiin ensimmäisen kerran.



Jos käytät passphrase:a, voit käyttää sitä tässä vaiheessa (katso tämän ohjeen osa 6). Muussa tapauksessa napsauta yksinkertaisesti `Done`.



![Image](assets/fr/27.webp)



Sen jälkeen voit käyttää Wallet:ää tavalliseen tapaan: tarkistaa toimitusosoitteet ja allekirjoittaa tapahtumia, aivan kuten perinteisellä SeedSignerilla. Jos haluat lisätietoja sen käytöstä, katso oma opetusohjelma :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Seedkeeperin käyttö passphrase BIP39:n kanssa



Käytätkö passphrase:tä Bitcoin-salkkusi suojaamiseen? Voit rekisteröidä sen myös Seedkeeperiin seed:n rinnalle. Tämän ratkaisun avulla voit ladata Wallet:n nopeasti SeedSigneriin, eikä sinun tarvitse syöttää passphrase:ää manuaalisesti pienelle näppäimistölle joka kerta, kun käytät sitä.



Mielestäni tämä menetelmä on erityisen mielenkiintoinen, koska sen avulla voit hyödyntää passphrase:n turvallisuusetuja ja poistaa samalla sen päivittäiseen käyttöön liittyvät rajoitukset. Tässä on esimerkki kokoonpanosta, jota suosittelen:




- Pidä seed ja passphrase siemenvarastossa, joka on suojattu vahvalla PIN-koodilla (tämä on tärkeää). Tämän varmuuskopion avulla voit helposti käyttää Wallet:ää päivittäin. Voit halutessasi kopioida nämä tiedot toiseen Seedkeeperiin;
- Säilytä myös selkeä kopio Mnemonic- ja passphrase-asiakirjoista paperilla tai metallilla. Tämä on viimeinen vaihtoehto varmuuskopioksi, jos menetät Seedkeeperisi tai sen PIN-koodin. Muista säilyttää nämä kopiot eri paikoissa, jotta niitä ei voida vaarantaa samanaikaisesti.



Tässä kokoonpanossa, jos joku saa käsiinsä pelkän selkotekstin Mnemonic, hän ei pysty varastamaan mitään tuntematta passphrase:tä (edellyttäen tietysti, että se on tarpeeksi vahva kestääkseen brute-force-hyökkäyksen). Jos taas joku saa selvätekstisi passphrase selville, se on käyttökelvoton ilman vastaavaa Mnemonic-lausetta.



Jos joku onnistuu pääsemään fyysisesti käsiksi seed:n ja passphrase:n sisältävään siemenvarastoosi, hän ei pysty poistamaan mitään tietämättä PIN-koodia. Toisin kuin passphrase:ssa, tätä koodia ei voi murtaa, sillä älykortti lukitsee itsensä automaattisesti viiden virheellisen yrityksen jälkeen.



Tämän kokoonpanon turvallisuus perustuu siis kahteen keskeiseen seikkaan:




- **passphrase strong**: sen on oltava pitkä, satunnainen ja sisällettävä monenlaisia merkkejä. Sen monimutkaisuus ei ole sinulle ongelma, koska sinun tarvitsee syöttää se vain kerran näppäimistöllä alustuksen aikana, minkä jälkeen Seedkeeper lähettää sen;
- **vahva PIN-koodi** siementen tallentajalle: myös satunnainen ja koostuu 16 merkistä.



Aseta tämä asetus lataamalla passphrase SeedSigneriin tavalliseen tapaan. Voit noudattaa tässä ohjeessa esitettyä menettelyä:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kun passphrase:ää sisältävä salkku on ladattu oikein SeedSigneriin, avaa `Seeds`-valikko ja valitse salkkua vastaava jalanjälki. Huomaa, että tämä jalanjälki eroaa salkusta, jossa ei ole passphrase:ää.



![Image](assets/fr/28.webp)



Napsauta sitten `Backup seed`, aseta Seedkeeper asemaan ja valitse `To SeedKeeper`.



![Image](assets/fr/29.webp)



Anna PIN-koodisi avataksesi Seedkeeperin lukituksen ja määritä sitten tarra tälle salaisuudelle. Voit jättää sormenjäljen merkinnäksi, jos haluat säilyttää jonkinlaisen uskottavan kiistettävyyden, tai ilmoittaa nimenomaisesti esimerkiksi "passphrase Wallet".



![Image](assets/fr/30.webp)



passphrase-salkkusi on nyt rekisteröity Seedkeeperiin.



![Image](assets/fr/31.webp)



Seuraavan kerran kun käynnistät koneen, aseta Seedkeeper asemaan ja siirry sitten kohtaan `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Anna PIN-koodi älykortin lukituksen avaamiseksi ja valitse sitten passphrase:ta vastaava Wallet.



![Image](assets/fr/33.webp)



Tarkista passphrase:n ja Wallet:n jälki ja vahvista sitten.



![Image](assets/fr/34.webp)



Voit nyt käyttää salkkuasi passphrase:lla ja allekirjoittaa tapahtumat kuten normaalisti SeedSignerillä.



## 7. Lisävaihtoehdot



Työkalut > Älykorttityökalut -valikosta löydät useita vaihtoehtoja Seedkeeperisi hallintaan:





- Yleiset työkalut -valikossa voit :
 - Tarkista kortin aitous;
 - Vaihda PIN-koodi ;
 - Muuta salaisuuksiisi liittyviä merkintöjä ;
 - Poista NFC-toiminto käytöstä (suositellaan, jos käytetään vain sirulukijaa) ;
 - Suorita tehdasasetusten palautus.





- SeedKeeper-toiminnot -valikossa voit :
 - Tutustu rekisteröityjen salaisuuksien luetteloon ;
 - Tallenna uusi salaisuus ;
 - Olemassa olevan salaisuuden poistaminen ;
 - Tallenna tai lataa kuvaajat (hyödyllinen toiminto Multisig-salkkuja varten).





- DIY Tools -valikossa voit :
 - Seedkeeper-sovelluksen kääntäminen ;
 - Asenna sovellus tyhjälle kortille;
 - Poista Seedkeeper-sovellus nollataksesi sen ja tehdäksesi siitä taas tyhjän.



Nyt tiedät, miten voit käyttää Seedkeeperiä varmuuskopioida salkkusi turvallisesti yhdessä SeedSignerin kanssa.



Jos tämä asetelma on vakuuttanut sinut, älä epäröi tukea hankkeita, jotka tekevät sen mahdolliseksi:




- Ostamalla laitteesi suoraan [Satochipin verkkosivuilta](https://satochip.io/shop/);
- Tekemällä [lahjoituksen SeedSigner-hankkeelle](https://seedsigner.com/donate/);
- Tilaamalla [Crypto Guiden YouTube-kanavan](https://www.youtube.com/@CryptoGuide/), jota ylläpitää henkilö, joka ylläpitää GitHub-tietokanavaa, jossa muokattu laiteohjelmisto sijaitsee.