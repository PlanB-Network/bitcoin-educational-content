---
name: Jade Plus - vihreä
description: Helppo konfiguroida Jade Plus Greenin kanssa
---
![cover](assets/cover.webp)

Jade Plus on Blockstreamin suunnittelema pelkkä Bitcoin-laitelompakko. Se on klassisen Jaden seuraaja, jossa on ohjelmistoparannuksia, enemmän vaihtoehtoja ja uudelleen suunniteltu ergonomia intuitiivisempaa käyttöä varten. Tässä uudessa versiossa on upea 1,9-tuumainen LCD-näyttö, jossa on edeltäjäänsä laajempi väriskaala. Myös painikkeita ja valikkonavigointia on optimoitu.

Jade Plus -kameraa voi käyttää monella eri tavalla: langallisen USB-C-yhteyden kautta, *Air-Gap*-tilassa micro SD-kortin kanssa (adapteri tarvitaan), Bluetoothin kautta tai jopa QR-koodeja vaihtamalla integroidun kameran ansiosta. Tämä laitteistolompakko toimii akkukäyttöisenä.

Se on saatavana 149,99 dollarista alkaen mustana perusversiona, ja hinta voi nousta jopa 20 dollarilla "*Genesis Grey*" tai "*Lunar Silver*" -versioissa. Jade Plus on siis mielenkiintoinen valinta, jonka kehittyneet toiminnot ovat verrattavissa Coldcard Q:n tai Passport V2:n kaltaisten huippuluokan laitteistolompakoiden toimintoihin, mutta melko edulliseen hintaan, joka on lähellä keskihintaisia malleja.

![JADE-PLUS-GREEN](assets/fr/01.webp)

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

Tässä oppaassa asetamme Jade Plussan ja Blockstreamin Green Wallet -mobiilisovelluksen käyttöön Bluetooth-yhteyden kautta. Tämä asennus sopii erinomaisesti aloittelijoille. Jos etsit edistyneempää lähestymistapaa, suosittelen tutustumaan tähän opetusohjelmaan, jossa käytämme Jade Plus -laitetta Sparrow-lompakon kanssa QR-kooditilassa:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## Jade Plus -turvamalli

Jade Plus -järjestelmässä käytetään turvamallia, joka perustuu "virtuaaliseen turvalliseen elementtiin", joka on toteutettu "sokean oraakkelin" avulla. Konkreettisesti tämä mekanismi yhdistää käyttäjän valitseman PIN-koodin, Jadessa olevan salaisuuden ja oraakkelin (Blockstreamin ylläpitämä palvelin) hallussa olevan salaisuuden luodakseen AES-256-avaimen, joka on jaettu kahteen yksikköön. Aloitusvaiheessa ECDH-vaihto turvaa viestinnän oraakkelin kanssa ja salaa palautuslauseen laitteistolompakossa. Käytännössä, kun haluat käyttää siementä transaktioiden allekirjoittamista varten, tarvitset pääsyn :


- Itse Jade Plus -laitteeseen;
- PIN-koodin avaaminen laitteen lukituksen avaamiseksi ;
- Ja oraakkelin salaisuuteen.

Tämän lähestymistavan suurimpana etuna on se, että laitteistotasolla ei ole yhtä ainoaa vikapistettä, sillä jos hyökkääjä pääsee joskus käsiksi Jadeen, avainten poimiminen edellyttää sekä Jaden että oraakkelin vaarantamista. Tämä malli tarkoittaa myös sitä, että Jade Plus on täysin avoimen lähdekoodin tuote, jolloin vältytään rajoituksilta, jotka liittyvät esimerkiksi Ledgerissä käytettyjen fyysisten turvalaitteiden käyttöön.

Tämän järjestelmän haittapuolena on, että Jade Plus -järjestelmän käyttö riippuu Blockstreamin ylläpitämästä oraakkelista. Jos tämä oraakkeli ei ole enää käytettävissä, laitteistolompakkoa ei ole enää mahdollista käyttää suoraan PIN-koodilla. Tämä ei kuitenkaan tarkoita sitä, että bitcoinisi ovat menetettyjä, sillä ne voidaan edelleen ottaa talteen käyttämällä palautuslausetta, jonka voit syöttää Jade Plus -lompakkoon "*stateless*"-tilassa. Voit kiertää tämän riippuvuuden myös konfiguroimalla ja hallinnoimalla omaa oracle-palvelinta.

## Jade Plus -laitteen purkaminen

Kun vastaanotat Jade Plus -laitteen, tarkista, että laatikko ja sinetti ovat hyvässä kunnossa ja että pakettia ei ole avattu.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Laatikosta löydät :


- Le Jade Plus;
- USB-C-kaapeli;
- Kortit, joihin voit tallentaa muistisanat sanoina tai "*CompactSeedQR*";
- Joitakin käyttöohjeita ;
- Naru;
- Joitakin tarroja.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Laitteessa on 4 navigointipainiketta:


- Oikealla alhaalla oleva painike kytkee Jaden päälle;
- Laitteen etuosassa olevaa suurta painiketta käytetään kohteen valitsemiseen;
- Yläreunan kahdella pienellä painikkeella voit navigoida vasemmalle ja oikealle;
- Voit valita kohteen myös napsauttamalla samanaikaisesti laitteen yläreunassa olevia kahta painiketta.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Uuden Bitcoin-lompakon perustaminen

Napsauta käynnistyspainiketta.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Napsauta "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Valitse "Begin Setup". "*Advanced Setup*"-vaihtoehto tekee saman asian, mutta siinä on pääsy lisäasetuksiin.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Napsauta sitten "*Luo uusi lompakko*" luodaksesi uuden siemenen.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Napsauta "*Jatka*"-painiketta näyttääksesi uuden palautuslausekkeen.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus näyttää 12-sanaisen muistisanan. **Tämä muistisana antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä Jade Plus -laitteeseesi. 12-sanainen lauseke palauttaa pääsyn bitcoineihisi, jos Jade häviää, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***Ei näitä sanoja saa tietenkään koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkisalkkua käytetään vain Testnetissä, ja se poistetaan opetusohjelman päätyttyä

Napsauta näytön oikeassa reunassa olevaa nuolta näyttääksesi seuraavat sanat.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Kun olet tallentanut lauseesi, Jade Plus pyytää sinua vahvistamaan sen. Valitse oikea sana järjestyksen mukaan laitteen yläosassa olevilla painikkeilla ja siirry seuraavaan sanaan napsauttamalla keskipainiketta.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Jade Plussan liittäminen Green Walletiin

Tässä ohjeessa käytämme Green Wallet -sovellusta Jade Plus -laitteessa olevan lompakon hallintaan. Tämä menetelmä sopii erityisesti aloittelijoille. Jos haluat hallita Bitcoin-lompakkoasi yksityiskohtaisemmin, voit käyttää myös Sparrow Wallet -sovellusta, jota käsittelemme erillisessä opetusohjelmassa:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
Blockstream Green -sovelluksen asennus- ja asetusohjeet ovat tämän toisen ohjeen ensimmäisessä osassa:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
Kun olet Blockstream Green -sovelluksessa, napsauta "*Konfiguroi uusi salkku*" -painiketta.

![JADE-PLUS-GREEN](assets/fr/13.webp)

Valitse "*Laitteiston lompakossa*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktivoi Bluetooth älypuhelimessasi ja napsauta sitten "*Connect your Jade*" -painiketta.

![JADE-PLUS-GREEN](assets/fr/15.webp)

Valtuuttaa Green-sovelluksen käyttämään Bluetooth-yhteyksiä.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Sovellus etsii Jade Plus -korttiasi.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Napsauta Jade Plus -laitteessa "*Bluetooth*"-valikkoa.

![JADE-PLUS-GREEN](assets/fr/18.webp)

Valitse laitteesi Green-sovelluksessa.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Vahvista pariliitoskoodi Jade Plus -laitteessasi.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green tarjoaa sinulle testin, jolla voit varmistaa, että Jade on aito. Klikkaa painiketta tehdäksesi sen.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Vahvista Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Vihreä väri vahvistaa, että laite on aito.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## PIN-koodin asettaminen

Valitse Jaden PIN-koodi napsauttamalla "*Jatka*"-painiketta.

![JADE-PLUS-GREEN](assets/fr/24.webp)

PIN-koodi avaa Jaden lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu lompakkosi kryptografisten avainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, 12-sanaisen muistilausekkeen avulla voit siis saada bitcoinisi takaisin haltuusi, vaikka sinulla ei olisikaan pääsyä siihen. Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Muista myös tallentaa tämä koodi erilliseen paikkaan siitä, missä Jade on tallennettu (esim. salasanahallintaan).

Valitse 6-numeroinen PIN-koodi Jadessa käyttämällä oikeaa ja vasenta painiketta numeroiden selaamiseksi ja keskimmäistä painiketta numeron vahvistamiseksi.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Vahvista PIN-koodi toisen kerran.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Bitcoin-lompakkosi on luotu.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Luo Bitcoin-tili

Sinun on nyt luotava tili salkkuusi. Napsauta "*Luo tili*" -painiketta.

![JADE-PLUS-GREEN](assets/fr/28.webp)

Valitse "*Standardi*", jos haluat luoda klassisen yhden tunnuksen salkun.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Jos haluat lisätietoja "*2FA*"-vaihtoehdosta, voit seurata tätä ohjetta:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
Tilisi on luotu.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Jos haluat muokata vihreää salkkuasi, napsauta kolmea pientä pistettä oikeassa yläkulmassa.

![JADE-PLUS-GREEN](assets/fr/31.webp)

"*Rename*"-vaihtoehdon avulla voit muokata portfolion nimeä, mikä on erityisen hyödyllistä, jos hallinnoit useita portfolioita samassa sovelluksessa. "*Yksikkö*"-valikon avulla voit vaihtaa salkun perusyksikön. Voit esimerkiksi valita, että se näytetään satoshina eikä bitcoineina. Lopuksi "*Parametrit*"-valikosta pääset käyttämään muita vaihtoehtoja. Täältä löydät esimerkiksi laajennetun julkisen avaimesi ja sen kuvaajan, mikä on hyödyllistä, jos aiot perustaa vain kellon lompakon Jadesta.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Jos haluat muodostaa yhteyden Jadeen uudelleen sen sammuttamisen jälkeen, paina laitteen pohjassa olevaa on/off-painiketta. Valitse Green-sovelluksessa laitteesi etusivulta:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Syötä sitten Jadessa oleva PIN-koodi, ja yhteys muodostuu uudelleen.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Jade vapautetaan Blockstreamin "virtuaalisen turvallisen elementin" avulla (katso tämän ohjeen ensimmäinen osa). Tämä edellyttää Bluetooth-yhteyttä Green-sovelluksen kanssa. Jos Bluetooth-yhteydessä on ongelmia lukituksen avaamisen aikana, yritä irrottaa ja yhdistää laitteet uudelleen. Jos ongelma ei poistu, voit silti avata Jaden lukituksen valitsemalla "*QR Scan*"-vaihtoehdon ja noudattamalla [Blockstreamin verkkosivustolla](https://jadefw.blockstream.com/pinqr/index.html) olevia ohjeita.

Ennen kuin saat ensimmäiset bitcoinit lompakkoosi, **neuvon sinua tekemään tyhjän palautustestin**. Merkitse muistiin joitakin viitetietoja, kuten xpub- tai ensimmäinen vastaanottava osoite, ja poista lompakkosi Green-sovelluksessa ja Jade Plussassa, kun se on vielä tyhjä (`Options -> Device -> Factory Reset`). Yritä sitten palauttaa lompakkosi käyttämällä paperisia varmuuskopioitasi muistikirjoituslauseen avulla. Tarkista, että palautuksen jälkeen luotu evästetieto vastaa alun perin kirjoittamaasi evästetietoa. Jos se täsmää, voit olla varma, että paperiset varmuuskopiosi ovat luotettavia. Jos haluat lisätietoja testipalautuksen suorittamisesta, tutustu tähän toiseen opetusohjelmaan :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Vastaanottaa bitcoineja

Nyt kun Bitcoin-lompakkosi on perustettu, olet valmis vastaanottamaan ensimmäiset satsisi! Napsauta vain vihreän sovelluksen "*Vastaanota*"-painiketta.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Vihreä näyttää vastaanotto-osoitteen, mutta ennen sen käyttämistä on tärkeää tarkistaa se Jadesta varmistaaksesi, että se todella kuuluu salkkuumme. Voit tehdä tämän napsauttamalla "*Varmista laitteessa*" -painiketta.

![JADE-PLUS-GREEN](assets/fr/36.webp)

Tarkista Jadesta, että osoite on sama kuin Greenissä, ja vahvista se napsauttamalla painiketta.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Voit nyt jakaa osoitteen maksajan kanssa saadaksesi bitcoineja lompakkoosi. Kun maksutapahtuma lähetetään verkossa, se näkyy lompakossasi. Odota, kunnes olet saanut tarpeeksi vahvistuksia, jotta voit pitää transaktiota lopullisena.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Lähetä bitcoineja

Kun lompakossasi on bitcoineja, voit nyt myös lähettää bitcoineja. Klikkaa "*lähettää*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Kirjoita seuraavalla sivulla vastaanottajan osoite. Voit syöttää sen manuaalisesti tai skannata QR-koodin.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Valitse maksun määrä.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Näytön alareunassa voit valita maksutapahtuman maksun. Voit joko noudattaa sovelluksen suosituksia tai mukauttaa maksuja. Mitä korkeampi maksu on suhteessa muihin vireillä oleviin tapahtumiin, sitä nopeammin tapahtuma käsitellään. Maksumarkkinoita koskevia tietoja löydät [Mempool.space](https://mempool.space/) kohdasta "*Transaktiomaksut*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klikkaa "*Seuraava*" siirtyäksesi tapahtumien yhteenvetonäyttöön. Tarkista, että osoite, summa ja maksut ovat oikein.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Jos kaikki sujuu hyvin, liu'uta näytön alareunassa olevaa vihreää painiketta oikealle allekirjoittaaksesi ja lähettääksesi tapahtuman Bitcoin-verkkoon.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Sinua pyydetään nyt vahvistamaan tapahtuma Jadessa.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Varmista, että vastaanottajan osoite on oikein. Vahvista klikkaamalla valintamerkkiä.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Tarkista, että maksun määrä on oikea, ja vahvista sitten.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Tapahtumasi on allekirjoitettu ja lähetetty Greenistä.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Onneksi olkoon, tiedät nyt, miten Jade Plus -laite asetetaan ja käytetään Blockstream Green -mobiilisovelluksen kanssa Bluetooth-yhteyden kautta. Jos pidit tätä opetusohjelmaa hyödyllisenä, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos jakamisesta!

Jos haluat edetä askeleen pidemmälle, suosittelen tätä Jade Plus -ohjetta, jossa konfiguroimme sen Sparrow Wallet -ohjelmiston kanssa QR-tilassa. Opit myös käyttämään laitteiston lompakon lisäasetuksia:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262