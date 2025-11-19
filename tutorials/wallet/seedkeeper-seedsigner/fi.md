---
name: Seedkeeper x SeedSigner
description: Miten käytän Seedkeeperiä SeedSignerin kanssa?
---

![cover](assets/cover.webp)



*Kiitokset [Satochip](https://satochip.io/) -tiimille siitä, että he suostuivat käyttämään [heidän videoitaan](https://www.youtube.com/@satochip/videot) tässä ohjeessa. Kiitos myös [Crypto Guide](https://www.youtube.com/@CryptoGuide/) SeedSigner-ohjelmiston fork:sta, joka mahdollistaa älykorttien tuen



---

SeedSigner on wallet-laitteisto, jonka kokoat itse vakiolaitteistosta, yleensä Raspberry Pi Zerosta. Tätä wallet:ta kutsutaan "*tilattomaksi*": toisin kuin useimmat muut markkinoilla olevat mallit (Coldcard, Trezor, Ledger jne.), se ei tallenna mitään tietoja pysyvään muistiin, vaan se toimii vain RAM-muistista. Tämän seurauksena salkkusi seed ei koskaan tallennu SeedSigneriin. Joka kerta, kun käynnistät sen uudelleen, sinun on täytettävä se, jotta laite voi allekirjoittaa tapahtumasi. Yleisin tapa on tallentaa seed QR-koodina, jonka skannaat joka kerta, kun käytät sitä (*SeedQR*).



Tähän lähestymistapaan liittyy kuitenkin merkittävä riski: seed:n on pysyttävä saatavilla selkeänä tekstinä, jotta se voidaan skannata. Varkauden tai tunkeutumisen sattuessa hyökkääjä voi helposti saada sen haltuunsa ja varastaa bitcoinisi.



Tämän heikkouden poistamiseksi SeedSigner voidaan yhdistää [**Seedkeeper**](https://satochip.io/product/seedkeeper/), Satochipin kehittämän älykortin kanssa. Sen avulla muistisanat (tai muut salaisuudet) voidaan tallentaa secure element-korttiin, joka on suojattu PIN-koodilla. Seedkeeper-sovellus on avointa lähdekoodia, ja sen secure element:llä on EAL6+-sertifiointi. Yhdessä SeedSignerin kanssa käytettynä se tarjoaa erittäin mielenkiintoisen turvaominaisuuden: avaimia hallinnoidaan täysin offline-tilassa, maksutapahtumat allekirjoitetaan luotettavalla näytöllä, ja seed on fyysisesti suojattu älykortissa, joka kestää fyysisiä hyökkäyksiä.



Tarvitset asennuksen loppuunsaattamiseen vain seuraavat osat:




- Klassiseen SeedSigneriin tarvitaan tavanomaiset laitteet: Raspberry Pi Zero, Waveshare 1,3" näyttö, yhteensopiva kamera ja microSD-kortti (lisätietoja löydät SeedSigner-oppaasta alla);
- SeedSigner-laajennussarja, joka on saatavilla [Satochipin virallisessa kaupassa](https://satochip.io/product/seedsigner-extension-kit/), jonka avulla voit lukea ja kirjoittaa älykorttiin suoraan SeedSigneristäsi. Toinen vaihtoehto on käyttää ulkoista älykortinlukijaa, joka voidaan liittää kaapelilla Raspberry Pi:n Micro-USB-porttiin. En ole kuitenkaan testannut tätä ratkaisua itse;
- Seedkeeper tai vaihtoehtoisesti tyhjä älykortti, johon Seedkeeper-sovellus asennetaan (Satochipin myymä laajennussarja sisältää jo tyhjän älykortin).



![Image](assets/fr/01.webp)



Tämä opetusohjelma kattaa kaksi skenaariota:




- Jos sinulla on jo Bitcoin-salkku, jota hallitaan SeedSignerin kautta, asenna vain uusi laiteohjelmisto. Voit sitten jatkaa nykyisen wallet:n käyttöä, mutta tällä kertaa käyttämällä Seedkeeperiä lisäturvallisuuden takaamiseksi.
- Jos sinulla ei ole vielä Bitcoin wallet:aa yhdistettynä SeedSigneriin, sinun on noudatettava alla mainitun ohjeen vaiheita **5** ja **6**. Näissä kohdissa selitetään, miten generate-muistilauseke tallennetaan SeedSignerillä, tallennetaan *SeedQR*:n avulla ja liitetään sitten tämä wallet Sparrow Wallet:een sen hallintaa varten. En käsittele näitä menettelyjä tässä, ja **oletan, että sinulla on jo toimiva Bitcoin wallet, joka on konfiguroitu Sparrow:n ja SeedSignerin kanssa**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Asenna laiteohjelmisto



Jos haluat käyttää SeedSigneriäsi Seedkeeperillä, sinun on asennettava vaihtoehtoinen laiteohjelmisto, joka eroaa alkuperäisen SeedSignerin laiteohjelmistosta, jotta se tukee älykorttien lukemista. Tätä varten [suosittelen fork:n käyttämistä "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Lataa [uusin versio kuvasta](https://github.com/3rdIteration/seedsigner/releases) (`.zip`), joka vastaa käyttämääsi Raspberry Pi -mallia.



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



Nyt kun siementarkkailijasi on toiminnassa, voit tallentaa Bitcoin wallet -muistitietosi älykorttiin. Aloita käynnistämällä SeedSigner tavalliseen tapaan ja skannaa sitten wallet:n *SeedQR* ladataksesi sen laitteeseen. Kun seed on tuotu, valitse yksinkertaisesti `Done`.



![Image](assets/fr/15.webp)



Kun seed on ladattu, avaa `Backup Seed`-valikko.



![Image](assets/fr/16.webp)



Aseta sitten Seedkeeper SeedSigner-asemaan ja valitse vaihtoehto `To SeedKeeper`.



![Image](assets/fr/17.webp)



Tämän jälkeen SeedSigner pyytää sinua syöttämään PIN-koodin Seedkeeperiäsi varten. Koska kyseessä on tyhjä kortti, koodia ei ole vielä määritelty. Syötä mikä tahansa koodi ohittaaksesi tämän vaiheen ja vahvista sitten.



![Image](assets/fr/18.webp)



SeedSigner havaitsee, että Seedkeeperiä ei ole vielä alustettu (eli salasanaa ei ole asetettu). Jatka klikkaamalla `I Understand`.



![Image](assets/fr/19.webp)



Valitse nyt siemenenvartijan uusi PIN-koodi, jonka pituus on 4-16 merkkiä. Lisäturvallisuuden vuoksi valitse pitkä, satunnainen koodi: se on ainoa este, joka suojaa fyysistä pääsyä muistilauseeseesi.



Muista tallentaa PIN-koodi heti sen luomisen jälkeen joko luotettavaan salasanahallintaan tai erilliselle fyysiselle tietovälineelle strategiastasi riippuen. Jälkimmäisessä tapauksessa varmista, että PIN-koodin sisältävää tallennusvälinettä ei koskaan säilytetä samassa paikassa kuin Seedkeeperiä, sillä muuten suojaus jää tehottomaksi. On tärkeää, että sinulla on varmuuskopio: ** Ilman tätä PIN-koodia et pääse käsiksi seed:ään, ja bitcoinisi menetetään**.



![Image](assets/fr/20.webp)



Voit sitten määritellä muistisääntöön liittyvän `Label` -merkinnän. Tämä etiketti on hyödyllinen, jos tallennat useita salaisuuksia Seedkeeperiin, jotta voit helposti tunnistaa ne.



![Image](assets/fr/21.webp)



Muistilauseesi on nyt tallennettu älykorttiin.



![Image](assets/fr/22.webp)



Turvallisuusstrategian osalta on mahdollista valita useita lähestymistapoja tarpeiden ja riskinoton tason mukaan. Itse suosittelen, että säilytät vähintään kaksi kopiota seed:stä:




- Tämä on ensimmäinen älykortti, jota voit pitää helposti saatavilla jokapäiväisiä toimintoja, kuten osoitteiden tarkistamista tai maksutapahtumien allekirjoittamista varten. Menetelmä on käytännöllinen (kuten osassa 5 nähdään) ja turvallinen PIN-koodin tarjoaman suojan ansiosta, joten voit pitää kortin saatavilla ilman suurempia riskejä;
- Toinen kopio salaamattomasta muistilausekkeestasi, joka toimii salkkusi lopullisena varmuuskopiona ja jota käytetään vain siinä tapauksessa, että Seedkeeper katoaa tai varastetaan. Koska tämä versio on salaamaton, sitä on säilytettävä erillisessä, turvallisemmassa paikassa, jotta kahden varmuuskopion samanaikainen vaarantuminen voidaan estää.



Suojausstrategiastasi ja riskiprofiilistasi riippuen voit myös kopioida seed:n useisiin eri siemenvartijoihin tai luoda useita fyysisiä kopioita muistitikusta. Jos haluat lisätietoja näistä käytännöistä, tutustu seuraavaan opetusohjelmaan:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. seed:n lataaminen Seedkeeperistä



![video](https://youtu.be/ms0Iq_IyaoE)



Voit nyt käyttää Seedkeeperiäsi lataamaan muistilauseesi SeedSigneriin käynnistyksen yhteydessä ja näin allekirjoittaa Bitcoin-tapahtumat. Aloita käynnistämällä SeedSigner kytkemällä se ja avaa sitten `Seeds`-valikko.



![Image](assets/fr/23.webp)



Valitse sitten vaihtoehto `From SeedKeeper`.



![Image](assets/fr/24.webp)



Työnnä Seedkeeper älykortinlukijaan ja avaa lukitus syöttämällä PIN-koodi. Vahvista syöttösi painamalla oikeassa alakulmassa olevaa vahvistuspainiketta, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper voi sisältää useita salaisuuksia, joten SeedSigner pyytää sinua valitsemaan sen, jonka haluat ladata. Näytössä näkyvä etiketti vastaa vaiheessa 4 määrittelemääsi nimeä. Jos, kuten minun tapauksessani, olet rekisteröinyt vain yhden seed:n, vain yksi vaihtoehto on käytettävissä.



![Image](assets/fr/26.webp)



seed on nyt ladattu. Tarkista, että kyseessä on oikea wallet, vertaamalla näytöllä näkyvää sormenjälkeä Sparrow Wallet-asetuksissa määritettyyn sormenjälkeen. Tämä sormenjälki annettiin myös, kun wallet luotiin ensimmäisen kerran.



Jos käytät passphrase:ää, voit käyttää sitä tässä vaiheessa (katso tämän ohjeen osa 6). Muussa tapauksessa napsauta yksinkertaisesti `Done`.



![Image](assets/fr/27.webp)



Sen jälkeen voit käyttää wallet:tä tavalliseen tapaan: tarkistaa toimitusosoitteet ja allekirjoittaa tapahtumia, aivan kuten perinteisellä SeedSignerilla. Jos haluat lisätietoja sen käytöstä, katso oma opetusohjelma :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Seedkeeperin käyttö passphrase BIP39:n kanssa



Käytätkö passphrase:ta Bitcoin-salkkusi suojaamiseen? Voit rekisteröidä sen myös Seedkeeperiin seed:n rinnalle. Tämän ratkaisun avulla voit ladata wallet:n nopeasti SeedSigneriin, eikä sinun tarvitse syöttää passphrase:ta manuaalisesti pienellä näppäimistöllä joka kerta, kun käytät sitä.



Mielestäni tämä menetelmä on erityisen mielenkiintoinen, koska sen avulla voit hyödyntää passphrase:n turvallisuusetuja ja poistaa samalla sen päivittäiseen käyttöön liittyvät rajoitukset. Tässä on esimerkki kokoonpanosta, jota suosittelen:




- Pidä seed ja passphrase siemenvarastossa, joka on suojattu vahvalla PIN-koodilla (tämä on tärkeää). Tämän varmuuskopion avulla voit helposti käyttää wallet:aa päivittäin. Voit halutessasi kopioida nämä tiedot toiseen Seedkeeperiin;
- Pidä myös selkeä kopio muistisäännöistäsi ja passphrase:stä, paperilla tai metallilla. Tämä on viimeisin varmuuskopio, jos menetät Seedkeeperisi tai sen PIN-koodin. Muista säilyttää nämä kopiot eri paikoissa, jotta niitä ei voida vaarantaa samanaikaisesti.



Tässä kokoonpanossa, jos joku saa käsiinsä pelkän selkotekstin mnemoniikkasi, hän ei pysty varastamaan mitään tuntematta passphrase:tä (edellyttäen tietenkin, että se on tarpeeksi vahva kestääkseen brute-force-hyökkäyksen). Jos taas joku löytää passphrase:n selkokielisenä, se on käyttökelvoton ilman vastaavaa muistisääntöä.



Jos joku onnistuu pääsemään fyysisesti käsiksi seed:n ja passphrase:n sisältävään siemenvarastoosi, hän ei pysty poistamaan mitään tietämättä PIN-koodia. Toisin kuin passphrase:ssa, tätä koodia ei voi murtaa, sillä älykortti lukitsee itsensä automaattisesti viiden virheellisen yrityksen jälkeen.



Tämän kokoonpanon turvallisuus perustuu siis kahteen keskeiseen seikkaan:




- **passphrase strong**: sen on oltava pitkä, satunnainen ja sisällettävä monenlaisia merkkejä. Sen monimutkaisuus ei ole sinulle ongelma, koska sinun tarvitsee syöttää se vain kerran näppäimistöllä alustuksen aikana; sen jälkeen Seedkeeper lähettää sen;
- **vahva PIN-koodi** siementen tallentajalle: myös satunnainen ja koostuu 16 merkistä.



Aseta tämä asetus lataamalla passphrase SeedSigneriin tavalliseen tapaan. Voit noudattaa tässä ohjeessa esitettyä menettelyä:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kun salkku, jossa on passphrase, on ladattu oikein SeedSigneriin, avaa `Seeds`-valikko ja valitse tätä salkkua vastaava jalanjälki. Huomaa, että tämä jalanjälki eroaa salkun jalanjäljestä ilman passphrase:ta.



![Image](assets/fr/28.webp)



Napsauta sitten `Backup Seed`, aseta Seedkeeper asemaan ja valitse `To SeedKeeper`.



![Image](assets/fr/29.webp)



Anna PIN-koodisi avataksesi Seedkeeperin lukituksen ja määritä sitten tarra tälle salaisuudelle. Voit jättää sormenjäljen merkinnäksi, jos haluat säilyttää jonkinlaisen uskottavan kiistettävyyden, tai voit esimerkiksi ilmoittaa nimenomaisesti `Passphrase Wallet`.



![Image](assets/fr/30.webp)



passphrase-salkkusi on nyt rekisteröity Seedkeeperiin.



![Image](assets/fr/31.webp)



Seuraavan kerran kun käynnistät koneen, aseta Seedkeeper asemaan ja siirry sitten kohtaan `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Anna PIN-koodi älykortin lukituksen avaamiseksi ja valitse sitten passphrase:tä vastaava wallet.



![Image](assets/fr/33.webp)



Tarkista passphrase:n ja wallet:n jälki ja vahvista sitten.



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
 - Tallenna tai lataa kuvaajat (hyödyllinen toiminto multi-sig-salkkuja varten).





- DIY Tools -valikossa voit :
 - Seedkeeper-sovelluksen kääntäminen ;
 - Asenna sovellus tyhjälle kortille;
 - Poista Seedkeeper-sovellus nollataksesi sen ja tehdäksesi siitä taas tyhjän.



Nyt tiedät, miten voit käyttää Seedkeeperiä varmuuskopioida salkkusi turvallisesti yhdessä SeedSignerin kanssa.



Jos tämä asetelma on vakuuttanut sinut, älä epäröi tukea hankkeita, jotka tekevät sen mahdolliseksi:




- Ostamalla laitteesi suoraan [Satochipin verkkosivuilta](https://satochip.io/shop/);
- Tekemällä [lahjoituksen SeedSigner-hankkeelle](https://seedsigner.com/donate/);
- Tilaamalla [Crypto Guiden YouTube-kanavan](https://www.youtube.com/@CryptoGuide/), jota ylläpitää henkilö, joka ylläpitää GitHub-tietokanavaa, jossa muokattu laiteohjelmisto sijaitsee.