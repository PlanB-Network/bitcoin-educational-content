---
name: Jade Plus - Sparrow
description: Jade Plussan edistynyt konfigurointi Sparrow-lompakon kanssa
---
![cover](assets/cover.webp)

Jade Plus on Blockstreamin suunnittelema pelkkä Bitcoin-laitelompakko. Se on klassisen Jaden seuraaja, jossa on ohjelmistoparannuksia, enemmän vaihtoehtoja ja uudelleen suunniteltu ergonomia intuitiivisempaa käyttöä varten. Tässä uudessa versiossa on upea 1,9-tuumainen LCD-näyttö, jossa on edeltäjäänsä laajempi väriskaala. Myös painikkeita ja valikkonavigointia on optimoitu.

Jade Plus -kameraa voi käyttää monella eri tavalla: langallisen USB-C-yhteyden kautta, *Air-Gap*-tilassa micro SD-kortin kanssa (adapteri tarvitaan), Bluetoothin kautta tai jopa QR-koodeja vaihtamalla integroidun kameran ansiosta. Tämä laitteistolompakko toimii akkukäyttöisenä.

Se on saatavana 149,99 dollarista alkaen mustana perusversiona, ja hinta voi nousta jopa 20 dollarilla "*Genesis Grey*" tai "*Lunar Silver*" -versioissa. Jade Plus on siis mielenkiintoinen valinta, jonka kehittyneet toiminnot ovat verrattavissa Coldcard Q:n tai Passport V2:n kaltaisten huippuluokan laitteistolompakoiden toimintoihin, mutta melko edulliseen hintaan, joka on lähellä keskihintaisia malleja.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus on yhteensopiva useimpien salkunhallintaohjelmistojen kanssa. Tässä on yhteenveto yhteensopivuudesta kirjoitushetkellä (tammikuu 2025):

| Työpöytä | Mobiili | USB | Bluetooth | QR | JadeLink | Hallintaohjelmisto | Hallintaohjelmisto

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobiili) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Varpunen | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

Tässä oppaassa asetamme Jade Plus -laitteen edistyneen kokoonpanon työpöydän Sparrow Wallet -ohjelmiston kanssa QR-koodit-tilassa. Tämä kokoonpano sopii erinomaisesti keskitason tai kokeneille käyttäjille. Jos etsit yksinkertaisempaa lähestymistapaa aloittelijoille, suosittelen tutustumaan tähän opetusohjelmaan, jossa käytämme Jade Plus -laitetta Green Walletin kanssa Bluetooth-yhteyden kautta:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Jade Plus -turvamalli

Jade Plus -järjestelmässä käytetään turvamallia, joka perustuu "virtuaaliseen turvalliseen elementtiin", joka on toteutettu "sokean oraakkelin" avulla. Konkreettisesti tämä mekanismi yhdistää käyttäjän valitseman PIN-koodin, Jadessa olevan salaisuuden ja oraakkelin (Blockstreamin ylläpitämä palvelin) hallussa olevan salaisuuden luodakseen AES-256-avaimen, joka on jaettu kahteen yksikköön. Aloitusvaiheessa ECDH-vaihto turvaa viestinnän oraakkelin kanssa ja salaa palautuslauseen laitteistolompakossa. Käytännössä, kun haluat käyttää siementä transaktioiden allekirjoittamista varten, tarvitset pääsyn :


- Itse Jade Plus -laite;
- PIN-koodin avaaminen laitteen lukituksen avaamiseksi ;
- Ja oraakkelin salaisuuteen.

Tämän lähestymistavan suurimpana etuna on se, että laitteistotasolla ei ole yhtä ainoaa vikapistettä, sillä jos hyökkääjä pääsee joskus käsiksi Jadeen, avainten poimiminen edellyttää sekä Jaden että oraakkelin vaarantamista. Tämä malli tarkoittaa myös sitä, että Jade Plus on täysin avoimen lähdekoodin tuote, jolloin vältetään rajoitukset, jotka liittyvät esimerkiksi Ledgerissä käytettyjen fyysisten turvalaitteiden käyttöön.

Tämän järjestelmän haittapuolena on, että Jade Plus -järjestelmän käyttö riippuu Blockstreamin ylläpitämästä oraakkelista. Jos tämä oraakkeli ei ole enää käytettävissä, laitteistolompakkoa ei ole enää mahdollista käyttää suoraan PIN-koodilla. Tämä ei kuitenkaan tarkoita sitä, että bitcoinisi ovat menetettyjä, sillä ne voidaan edelleen ottaa talteen käyttämällä palautuslausetta, jonka voit syöttää Jade Plus -lompakkoon "*stateless*"-tilassa. Voit kiertää tämän riippuvuuden myös konfiguroimalla ja hallinnoimalla omaa oracle-palvelinta.

Toinen vaihtoehto siementen hallintaan on yksinkertaisesti olla rekisteröimättä niitä Jade Plus -järjestelmään. Tällöin Jadesta tulee pelkkä allekirjoituslaite. Alustuksen aikana tavanomaisen palautuslauseen tallentamisen lisäksi sanoina, tallennat sen myös käsin luoduksi QR-koodiksi. Näin voit tuoda siemenen joka kerta, kun käytät lompakkoa, Jaden kameran avulla. Tämä voi olla mielenkiintoinen vaihtoehto edistyneille käyttäjille, riippuen turvallisuusstrategiastasi, mutta sinun on oltava varovainen sekä siemenen tallentamisessa että sen suojaamisessa, sillä QR-koodinakin se antaisi kenelle tahansa mahdollisuuden varastaa varojasi. Tarkastelemme tätä vaihtoehtoa tässä opetusohjelmassa, mutta se ei ole pakollinen.

## Jade Plus -laitteen purkaminen

Kun vastaanotat Jade Plus -laitteen, tarkista, että laatikko ja sinetti ovat hyvässä kunnossa ja että pakettia ei ole avattu.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Laatikosta löydät :


- Le Jade Plus;
- USB-C-kaapeli;
- Kortit, joihin voit tallentaa muistisanat sanoina tai "*CompactSeedQR*";
- Joitakin käyttöohjeita ;
- Naru;
- Joitakin tarroja.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Laitteessa on 4 navigointipainiketta:


- Oikealla alhaalla oleva painike kytkee Jaden päälle;
- Laitteen etuosassa olevaa suurta painiketta käytetään kohteen valitsemiseen;
- Yläreunan kahdella pienellä painikkeella voit navigoida vasemmalle ja oikealle;
- Voit valita kohteen myös napsauttamalla samanaikaisesti laitteen yläreunassa olevia kahta painiketta.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Uuden Bitcoin-lompakon perustaminen

Napsauta käynnistyspainiketta.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Napsauta "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Valitse "Lisäasetukset".

![Image](assets/fr/07.webp)

Napsauta sitten "*Luo uusi lompakko*" luodaksesi uuden siemenen. Voit valita 12- tai 24-sanaisen muistilausekkeen. Lompakkosi turvallisuus säilyy samana molemmilla vaihtoehdoilla, joten voi olla kätevämpää valita yksinkertaisin vaihtoehto eli 12 sanaa.

![Image](assets/fr/08.webp)

Napsauta "*Jatka*"-painiketta näyttääksesi uuden palautuslausekkeen.

![Image](assets/fr/09.webp)

Jade Plus näyttää 12-sanaisen muistisanan. **Tämä muistisana antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä Jade Plus -laitteeseesi. 12-sanainen lauseke palauttaa pääsyn bitcoineihisi, jos Jade häviää, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.**

Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.

![Image](assets/fr/10.webp)

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

näitä sanoja ei tietenkään saa koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkisalkkua käytetään vain Testnetissä, ja se poistetaan opetusohjelman päätyttyä.

Napsauta näytön oikeassa reunassa olevaa nuolta näyttääksesi seuraavat sanat.

![Image](assets/fr/11.webp)

Kun olet tallentanut lauseesi, Jade Plus pyytää sinua vahvistamaan sen. Valitse oikea sana järjestyksen mukaan laitteen yläosassa olevilla painikkeilla ja siirry seuraavaan sanaan napsauttamalla keskipainiketta.

![Image](assets/fr/12.webp)

Sinulla on sitten 2 vaihtoehtoa. Kuten johdannossa kerrottiin, voit tallentaa siemenesi suoraan laitteeseen ja käyttää Blockstreamin "*Virtual Secure Element*" -suojausjärjestelmää lompakkosi käyttämiseen (vaihtoehto 1) tai tallentaa siemenesi QR-koodina ja skannata sen aina kun käytät sitä (vaihtoehto 2).

Valitse vaihtoehdon 1 kohdalla "*Ei*" ja vaihtoehdon 2 kohdalla "*Kyllä*".

![Image](assets/fr/13.webp)

### Vaihtoehto 1: QR PIN-koodin avaaminen

Jos olet valinnut vaihtoehdon 1 (CompactSeedQR: "*Ei*"), siirryt suoraan liitäntätavan valintaan. Tässä opetusohjelmassa haluamme käyttää laitetta Air-Gap-tilassa QR-koodien vaihdon kautta, joten valitse "*QR*".

![Image](assets/fr/27.webp)

Napsauta "*Jatka*".

![Image](assets/fr/28.webp)

PIN-koodia käytetään Jaden lukituksen avaamiseen ja se suojaa luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu lompakkosi salausavainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, 12-sanaisen muistilausekkeen avulla voit saada bitcoinisi takaisin haltuusi, vaikka sinulla ei olisikaan pääsyä siihen. Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Varmista myös, että tallennat tämän koodin erilliseen paikkaan siitä, missä Jade on tallennettu, esimerkiksi salasanahallintaan.

Valitse 6-numeroinen PIN-koodi Jadella käyttämällä vasenta ja oikeaa painiketta numeroiden selaamiseen ja keskimmäistä painiketta kunkin numeron vahvistamiseen.

![Image](assets/fr/29.webp)

Vahvista PIN-koodi toisen kerran.

![Image](assets/fr/30.webp)

Kuten johdannossa selitettiin, siemenesi tallennetaan salattuna Jade Plus -laitteeseen. Jos haluat purkaa salauksen, sinun on annettava :


- Voimassa oleva PIN-koodi (jonka olemme juuri määrittäneet) ;
- Blockstreamin ylläpitämän oraakkelin salaisuus.

Tässä edistyneen oppaassa käytämme Sparrow-lompakkoa Bitcoin-lompakon hallintaan. Toisin kuin Blockstreamin Green Wallet -ohjelmisto, Sparrow ei kuitenkaan pääse käsiksi Blockstreamin palvelimilla olevaan oraakkeleihin. Siksi käytämme Blockstreamin verkkosivustoa oraakkelin salaisuuden hakemiseen aina, kun avaamme Jade Plus -lompakon lukituksen.

Käy osoitteessa https://jadefw.blockstream.com/pinqr/index.html

Napsauta "*Start QR Unlock*".

![Image](assets/fr/31.webp)

Napsauta "*Tehdään*", koska olet jo valinnut PIN-koodisi Jade Plus -laitteessa.

![Image](assets/fr/32.webp)

Skannaa Jaden näytöllä näkyvät QR-koodit tietokoneen kameran avulla.

![Image](assets/fr/33.webp)

Vahvista Jade, niin pääset seuraavaan näyttöön.

![Image](assets/fr/34.webp)

Skannaa QR-koodi, joka näkyy nyt verkkosivustolla, saadaksesi oraakkelin salaisuuden.

![Image](assets/fr/35.webp)

Nyt kun salkku on luotu, voit siirtyä seuraaviin vaiheisiin ja ohittaa alaluvun "*Vaihtoehto 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Napsauta aina käynnistyksen yhteydessä "*QR Mode*".

![Image](assets/fr/37.webp)

Valitse "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Syötä PIN-koodi.

![Image](assets/fr/39.webp)

Mene sitten [Blockstreamin verkkosivustolle] (https://jadefw.blockstream.com/pinqr/qrpin.html) vaihtaaksesi QR-koodeja oraakkelin kanssa.

![Image](assets/fr/40.webp)

Jade on nyt avattu.

![Image](assets/fr/41.webp)

### Vaihtoehto 2: CompactSeedQR

Jos olet valinnut vaihtoehdon 2 (CompactSeedQR: "*Kyllä*"), napsauta uudelleen "*Kyllä*".

![Image](assets/fr/14.webp)

Napsauta "*Start*".

![Image](assets/fr/15.webp)

Voit käyttää Jade Plus -laatikon mukana toimitettua QR-koodipohjaa. Valitse sopiva laatikko sen mukaan, oletko valinnut 12- vai 24-sanaisen lauseen. Voit myös [tulostaa mallin Blockstreamin verkkosivustolta](https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus näyttää QR-koodin jokaisen alueen.

![Image](assets/fr/16.webp)

Väritä neliöt kynällä ja jäljennä siemenesi QR-koodiksi. Ole tarkka, jotta Jade Plus -kamera voi skannata sen myöhemmin. Siirry seuraavaan alueeseen nuolinäppäimellä.

![Image](assets/fr/17.webp)

Kun olet valmis, napsauta "*Tehdään*".

![Image](assets/fr/18.webp)

Skannaa käsintehty QR-koodi Jade Plus -laitteella tarkistaaksesi sen voimassaolon.

![Image](assets/fr/19.webp)

Jos paperin varmuuskopio on oikein, napsauta "*Jatka*".

![Image](assets/fr/20.webp)

Tässä ohjeessa käytämme yksinomaan QR-koodin skannaukseen perustuvaa yhteystilaa, joten valitse "*QR*".

![Image](assets/fr/21.webp)

Voit myös lisätä PIN-koodin CompactSeedQR-varmuuskopion lisäksi, kuten vaihtoehdossa 1. Näin lompakkoasi pääsee käsiksi kahdella tavalla: joko PIN-koodin ja Blockstreamin "Virtual Secure Element" -järjestelmän kautta tai CompactSeedQR:n kautta.

Jos valitset kaksois-PIN-vaihtoehdon, valitse "*PIN*" ja noudata samoja ohjeita kuin vaihtoehdossa 1 PIN-koodin asettamiseksi.

Jos haluat jatkaa vain CompactSeedQR:llä, valitse "*SeedQR*".

![Image](assets/fr/22.webp)

Nyt kun portfoliosi on luotu, voit siirtyä seuraaviin vaiheisiin.

![Image](assets/fr/23.webp)

Napsauta aina käynnistyksen yhteydessä "*QR Mode*"-painiketta ja sitten "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Skannaa tallennettu siemen QR-koodiksi laitteen kameran avulla.

![Image](assets/fr/25.webp)

Jade on nyt avattu.

![Image](assets/fr/26.webp)

## Lisää BIP39-salasana

BIP39-salasana on valinnainen salasana, jonka voit valita vapaasti ja joka lisätään muistilausekkeeseen lompakon turvallisuuden vahvistamiseksi. Kun tämä ominaisuus on käytössä, Bitcoin-lompakkoon pääsy edellyttää sekä muistisääntöä että salasanaa. Ilman kumpaakaan lompakkoa olisi mahdotonta palauttaa.

Ennen kuin määrität tämän vaihtoehdon Jade Plus -laitteeseesi, on erittäin suositeltavaa, että luet tämän artikkelin, jotta ymmärrät täysin salasanan teoreettisen toiminnan ja vältät virheet, jotka voivat johtaa bitcoinien menettämiseen:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kun Jade on edelleen lukittuna (salasana voidaan syöttää vain, kun laitteen lukitusta ei ole avattu), avaa "*Options*"-valikko.

![Image](assets/fr/42.webp)

Valitse "*BIP39-salasana*".

![Image](assets/fr/43.webp)

Vaihtoehdossa "*Tiheys*" voit valita, pyytääkö Jade Plus sinua syöttämään salasanasi joka kerta, kun se käynnistyy:


- "*Ei käytössä*" poistaa salasanan käytön käytöstä;
- "*Next Login Only*" edellyttää, että palaat tähän valikkoon aktivoidaksesi salasanasi pyytämisen seuraavan käynnistyksen yhteydessä. Tämän vaihtoehdon avulla et voi paljastaa sen käyttöä;
- "**Always Ask**" (Kysy aina) saa Jaden systemaattisesti kysymään salasanaa joka kerta, kun se käynnistyy, jolloin paljastuu, että lompakkosi on suojattu salasanalla.

Valitse turvastrategian mukainen vaihtoehto. Henkilökohtaisesti valitsen esimerkissä vaihtoehdon "*Kysy aina*".

![Image](assets/fr/44.webp)

Tämän jälkeen voit valita kahden menetelmän välillä salasanan syöttämiseksi:


- "*Käsikirja*: Kirjoita kirjaimet (isot ja pienet kirjaimet), numerot ja symbolit merkki kerrallaan virtuaalinäppäimistön avulla. Tämä on kaikkien laitteistolompakoiden vakiotapa;
- "*Sanaluettelo*": Se nopeuttaa salasanan syöttämistä ja lisää sen entropiaa. Syötön aikana järjestelmä ehdottaa sanoja BIP39-luettelosta, mikä helpottaa lukituksen avaamista. Tämä menetelmä luo automaattisesti lauseen yhdistämällä valitut sanat välilyönneillä erotettuina (esimerkki: `abandon ability able`).

Itse suosittelen käyttämään ensimmäistä menetelmää, koska se on standardi, joka löytyy kaikista muista salkkutukista.

![Image](assets/fr/45.webp)

Tämän jälkeen voit palata aloitusnäyttöön ja avata lompakon lukituksen normaalisti joko PIN-koodilla tai CompactSeedQR-koodilla (kuten yllä näkyy). Tämän jälkeen sinua pyydetään syöttämään tunnuslauseesi.

![Image](assets/fr/46.webp)

Kirjoita se Jade-näppäimistöllä ja muista tehdä yksi tai useampi varmuuskopio fyysiselle tietovälineelle (paperille tai metallille). Esimerkissä käytän hyvin heikkoa salasanaa, mutta sinun on valittava vahva, satunnainen salasana, joka sisältää kaikentyyppisiä merkkejä ja on riittävän pitkä (kuten vahva salasana).

![Image](assets/fr/47.webp)

Jos tunnuslauseesi on voimassa, vahvista.

![Image](assets/fr/48.webp)

Huomaa, että BIP39-salasanat ovat isojen ja pienten kirjainten suhteen herkkiä. Jos syötät hieman erilaisen salasanan kuin alun perin määritetty, Jade ei ilmoita virheestä, vaan se johtaa toisen salausavaimen, joka ei ole alkuperäisen salkun mukainen.

Siksi on tärkeää, että kirjaat konfiguroinnin yhteydessä muistiin pääavaimen sormenjäljen, joka löytyy näytön oikeasta alakulmasta. Esimerkiksi tunnuslauseellani `PBN` pääavaimeni sormenjälki on `3AD1AE65`.

![Image](assets/fr/49.webp)

Aina kun avaat Jaden lukituksen salasanalla, tarkista, että sormenjälki on sama kuin konfiguroinnin aikana syöttämäsi sormenjälki. Jos se on, salasanasi on oikea ja käytät oikeaa Bitcoin-lompakkoa. Jos se ei ole, olet väärällä lompakolla ja sinun on yritettävä uudelleen ja varottava syöttövirheitä.

Ennen kuin saat ensimmäiset bitcoinit lompakkoosi, **neuvon sinua tekemään tyhjän palautustestin**. Kirjoita muistiin joitakin viitetietoja, kuten xpub- tai ensimmäinen vastaanottava osoite, ja poista lompakkosi Jade Plus -laitteesta, kun se on vielä tyhjä (`Options -> Device -> Factory Reset`). Yritä sitten palauttaa lompakkosi käyttämällä paperitallennuksia muistilausekkeesta ja mahdollisesta salasanasta. Tarkista, että palautuksen jälkeen luodut evästetiedot vastaavat alun perin kirjoittamiasi tietoja. Jos ne täsmäävät, voit olla varma, että paperiset varmuuskopiot ovat luotettavia. Jos haluat lisätietoja testipalautuksen suorittamisesta, tutustu tähän toiseen opetusohjelmaan:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Lompakon määrittäminen Sparrow Walletissa

Tässä opetusohjelmassa esittelen Jade Plussan edistyneen käytön Sparrow-lompakon avulla. Tämä laitteistolompakko on kuitenkin yhteensopiva monien muiden ohjelmien, kuten Liana, Nunchuk, Specter, Green ja Keeper, kanssa. Nämä yhteensopivuudet vaihtelevat yhteyksien suhteen: USB, Bluetooth tai QR-koodi (katso lisätietoja johdannossa olevasta taulukosta).

Aloita lataamalla ja asentamalla Sparrow Wallet [virallisilta verkkosivuilta](https://sparrowwallet.com/) tietokoneellesi, jos et ole jo tehnyt sitä.

![Image](assets/fr/50.webp)

Varmista ohjelmiston aitous ja eheys ennen asennusta. Jos et tiedä, miten tämä tehdään, tutustu tähän ohjeeseen:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kun Sparrow Wallet on avattu, napsauta välilehteä "*File*" ja sitten "*New Wallet*".

![Image](assets/fr/51.webp)

Anna lompakollesi nimi ja napsauta sitten "*Luo lompakko*".

![Image](assets/fr/52.webp)

Valitse "*Airapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Napsauta "*Scan...*" vaihtoehdon "*Jade*" vieressä.

![Image](assets/fr/54.webp)

Avaa Jade Plus -luurisi lukitus ja syötä tunnuslauseesi, jos käytät sellaista. Mene sitten "*Options*"-valikkoon, valitse "*Wallet*" ja napsauta "*Export Xpub*".

![Image](assets/fr/55.webp)

Jade näyttää Keystoren useiden QR-koodien avulla. Skannaa ne koneellasi Sparrow'n avulla.

![Image](assets/fr/56.webp)

Sinun pitäisi nyt nähdä xpub ja pääavaimesi sormenjälki, jonka pitäisi vastata Jade Plus -järjestelmässä olevaa sormenjälkeä. Napsauta "*Apply*".

![Image](assets/fr/57.webp)

Aseta vahva salasana, jolla varmistat pääsyn Sparrow-lompakkoosi. Tämä salasana suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä. Salasana kannattaa tallentaa salasanahallintaan, jotta et unohda sitä.

![Image](assets/fr/58.webp)

Salkkusi on nyt määritetty oikein Sparrow'ssa.

![Image](assets/fr/59.webp)

## Vastaanottaa bitcoineja

Nyt kun Jade Plus on konfiguroitu, olet valmis vastaanottamaan ensimmäiset satelliitit uuteen Bitcoin-lompakkoosi. Tee se Sparrow'ssa napsauttamalla "*Vastaanottaa*"-valikkoa.

![Image](assets/fr/60.webp)

Sparrow näyttää portfoliosi ensimmäisen tyhjän vastaanotto-osoitteen.

![Image](assets/fr/61.webp)

Ennen käyttöä tarkistetaan Jade Plus -näytöltä, että se kuuluu Bitcoin-lompakkoon. Napsauta Jadessa "*Scan QR*" ja skannaa sitten Sparrow'ssa näkyvän osoitteen QR-koodi.

![Image](assets/fr/62.webp)

Tarkista, että Jaden näytöllä näkyvä osoite vastaa Sparrow Walletissa näkyvää osoitetta. Jos se vastaa, jatka klikkaamalla valintamerkkiä.

![Image](assets/fr/63.webp)

Tämän jälkeen laitteistolompakkosi vahvistaa, että tämä osoite on osa lompakkoasi ja että sillä on siihen liittyvä yksityinen avain.

![Image](assets/fr/64.webp)

Jos Jade on vahvistanut osoitteen, voit nyt käyttää sitä bitcoinien vastaanottamiseen. Kun transaktio lähetetään verkkoon, se näkyy Sparrow'ssa. Odota, kunnes olet saanut tarpeeksi vahvistuksia, jotta voit pitää tapahtumaa lopullisena.

![Image](assets/fr/65.webp)

## Lähetä bitcoineja

Nyt kun lompakossasi on muutama sati, voit myös lähettää niitä. Voit tehdä niin klikkaamalla "*UTXOs*"-valikkoa.

![Image](assets/fr/66.webp)

Valitse UTXO:t, joita haluat käyttää tämän tapahtuman syötteinä, ja napsauta sitten "*Send Selected*".

![Image](assets/fr/67.webp)

Kirjoita vastaanottajan osoite, etiketti, joka muistuttaa sinua tapahtuman tarkoituksesta, ja summa, jonka haluat lähettää tähän osoitteeseen.

![Image](assets/fr/68.webp)

Säädä palkkio nykyisten markkinaolosuhteiden mukaan ja napsauta sitten "*Luo transaktio*".

![Image](assets/fr/69.webp)

Tarkista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Viimeistele tapahtuma allekirjoitusta varten*".

![Image](assets/fr/70.webp)

Klikkaa "*Show QR*" näyttääksesi PSBT:n (*Partially Signed Bitcoin Transaction*). Sparrow on rakentanut transaktion, mutta siitä puuttuvat vielä allekirjoitukset, jotta syötössä käytetyt bitcoinit voitaisiin avata. Nämä allekirjoitukset voi suorittaa vain Jade Plus, joka isännöi siemenesi ja antaa pääsyn transaktion allekirjoittamiseen tarvittaviin yksityisiin avaimiin.

![Image](assets/fr/71.webp)

Napsauta Jade Plus -laitteessasi "*Scan QR*" skannataksesi Sparrow'ssa näkyvän PSBT:n.

![Image](assets/fr/72.webp)

Vahvista, että toimitusosoite ja lähetettävä summa ovat oikein, ja vahvista se napsauttamalla nuolta.

![Image](assets/fr/73.webp)

Varmista, että maksun määrä on valitsemasi, ja allekirjoita maksutapahtuma napsauttamalla käyttöliittymän vasemmassa yläkulmassa olevaa rasti-kuvaketta.

![Image](assets/fr/74.webp)

Napsauta Sparrow Walletissa "*Scan QR*" ja skannaa Jadessa näkyvä QR-koodi.

![Image](assets/fr/75.webp)

Allekirjoittamasi transaktio on nyt valmis lähetettäväksi Bitcoin-verkkoon ja sisällytettäväksi louhijan lohkoon. Jos kaikki on oikein, napsauta "*Lähetä transaktio*".

![Image](assets/fr/76.webp)

Tapahtumasi on lähetetty ja odottaa vahvistusta.

![Image](assets/fr/77.webp)

Onneksi olkoon, tiedät nyt, miten Jade Plus -laite asetetaan ja sitä käytetään QR-tilassa. Jos tämä opetusohjelma oli mielestäsi hyödyllinen, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos jakamisesta!

Jos haluat mennä pidemmälle, suosittelen tätä toista Jade Plus -ohjelmaa, jossa konfiguroimme sen Bluetoothilla Greenin mobiilisovelluksen avulla:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0