---
name: SeedSigner
description: DIY, tilaton, edullinen ja täysin ilmakapseloitu wallet-laitteisto
---

![cover](assets/cover.webp)



SeedSigner on avoimen lähdekoodin wallet Bitcoin-laitteisto, jonka kuka tahansa voi rakentaa itse käyttämällä edullisia yleiskäyttöisiä elektronisia komponentteja. Toisin kuin kaupalliset tuotteet, kuten Ledger, Coldcard tai Trezor, tämä ei ole yrityksen valmistama valmis laite: kyseessä on yhteisöprojekti, jonka avulla kuka tahansa voi luoda oman laitteensa ja valvoa jokaista vaihetta.



SeedSigner on suunniteltu olemaan 100-prosenttisesti ***air-gapped***: se ei koskaan yhdisty Internetiin, siinä ei ole Wi-Fi- tai Bluetooth-yhteyttä (Raspberry Pi Zero v1.3:n tapauksessa) eikä sitä koskaan yhdistetä tietokoneeseen tietojen vaihtoa varten. Viestintä tapahtuu yksinomaan QR-koodien vaihtojärjestelmän kautta. Konkreettisesti sanottuna salkunhallintaohjelmistosi (kuten Sparrow Wallet) näyttää allekirjoitettavan tapahtuman QR-koodien muodossa; skannaat ne SeedSignerin kameralla, minkä jälkeen laite allekirjoittaa tapahtuman käyttämällä RAM-muistiinsa väliaikaisesti tallennettuja yksityisiä avaimiasi. Lopuksi laite luo QR-koodit, jotka sisältävät allekirjoitetun tapahtuman, jonka skannaat ohjelmallasi lähettääksesi sen Bitcoin-verkkoon.



![Image](assets/fr/001.webp)



SeedSigner on myös ***tilaton***. Toisin sanoen se ei tallenna seed:ääsi tai yksityisiä avaimiasi pysyvästi, toisin kuin muut laitteistolompakot. Aina kun käynnistät laitteen uudelleen, sen muisti on täysin tyhjä, ellet määritä laitetta tallentamaan asetuksiasi microSD-kortille. Sinun on siis syötettävä seed joka kerta uudelleen, kun käytät sitä, ja käytännöllisin tapa on tallentaa se QR-koodin muodossa, joka skannataan käynnistyksen yhteydessä SeedSignerin kameralla. Tämä toimintatapa pienentää hyökkäyspintaa huomattavasti: vaikka varas varastaisi laitteesi, hän ei löydä siitä mitään tietoja, koska se on oletusarvoisesti aina tyhjä.



Toinen vaihtoehto seed:n tallentamiseen ja käyttämiseen SeedSignerin kanssa on käyttää *SeedKeeper*-älykorttia yhdessä yhteensopivan lukijan kanssa. Näin saat erittäin vankan *Secure Elementin* seed:n tallentamiseen, kun käytät SeedSigner-näyttöä tapahtumien allekirjoittamiseen. Mutta tämä erityinen kokoonpano on aiheena toisessa erillisessä opetusohjelmassa. Tässä keskitymme SeedSignerin peruskäyttöön:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner-hankkeella on tärkeä asema Bitcoin-ekosysteemissä, sillä se tarjoaa kaikille kaikkialla maailmassa mahdollisuuden hyötyä kehittyneestä turvallisuudesta bitcoiniensa suojaamiseksi. Sen tärkein etu on sen helppokäyttöisyys: tarvittavan laitteiston voi ostaa alle 50 dollarilla. Lisäksi rajoitetuissa maissa asuvat ihmiset voivat rakentaa oman wallet-laitteistonsa tavallisista tietokonekomponenteista, joita on helppo löytää ja joihin ei kohdistu niin paljon sääntelyrajoitteita.



SeedSigner voi kuitenkin olla mielenkiintoinen vaihtoehto myös näiden erityisten tilanteiden ulkopuolella: se on avoimen lähdekoodin, toimii tilattomasti ja ilman ilmakapselia ja vähentää wallet-laitteiston toimitusketjuun liittyviä hyökkäysvektoreita.



## 1. Tarvittavat laitteet



SeedSignerin rakentamiseen tarvitset seuraavat komponentit:





- Raspberry Pi Zero
    - Versiota 1.3 suositellaan, koska siinä ei ole Wi-Fi- eikä Bluetooth-yhteyttä, mikä takaa täydellisen eristyksen.
 - W- ja v2-versiot ovat myös yhteensopivia, mutta niissä on Wi-Fi/Bluetooth-siru. Siksi on suositeltavaa poistaa se fyysisesti käytöstä poistamalla radiomoduuli kortista. Toimenpide on suhteellisen yksinkertainen, mutta vaatii tarkkuutta (Zero W -mallissa riittää hienot pihdit, kun taas v2-mallissa tarvitaan kuumakynää moduulin piilottavan metallilevyn irrottamiseen). En mene yksityiskohtiin tässä ohjeessa, mutta löydät kaikki ohjeet tästä asiakirjasta: *[WiFi-/Bluetooth-yhteyden poistaminen käytöstä laitteiston avulla](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Huomaa: joitakin Raspberry Pi Zero -malleja myydään ilman valmiiksi juotettuja GPIO-nastoja. Voit joko ostaa suoraan integroidut nastat sisältävän version (yksinkertaisin ratkaisu) tai ostaa nastat erikseen ja juottaa ne itse (monimutkaisempi ratkaisu).
 - Älä unohda sisällyttää mikro-USB-virtalähdettä.



![Image](assets/fr/002.webp)





- Waveshare 1,3" näyttö (240×240 px)** (ranskaksi)
    - On tärkeää valita juuri tämä malli: on olemassa muitakin samanlaisia näyttöjä, mutta eri resoluutiolla. Ilman 240×240 px:n tarkkuutta näyttö on käyttökelvoton.
    - Näytössä on kolme painiketta ja minijoystick käyttöliittymää varten.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-yhteensopiva kamera
    - Vaihtoehto 1: vakiokamera, jossa on leveä kultamatto (tarkista yhteensopivuus kotelon kanssa).
    - Vaihtoehto 2: kompaktimpi "*Zero*"-kamera, joka on suunniteltu erityisesti Pi Zeroa varten.



![Image](assets/fr/004.webp)





- MicroSD**-kortti
    - Suositeltava kapasiteetti: 4-32 Gt.





- Asuminen (valinnainen mutta suositeltava)** (valinnainen mutta suositeltava)** (valinnainen mutta suositeltava)** (valinnainen mutta suositeltava)**)
    - Suojaa laitetta ja tekee siitä helppokäyttöisen.
    - Suosituin malli on "*Orange Pill Case*", jonka [avoimen lähdekoodin STL-tiedostot ovat saatavilla 3D-tulostusta varten](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Laatikoita on saatavana myös [hankkeeseen liittyvät riippumattomat jälleenmyyjät](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Voit ostaa nämä komponentit erikseen tai yksinkertaisemmin valita valmiita paketteja, jotka sisältävät kaikki tarvittavat laitteistot. Itse tilasin pakettini [tältä ranskalaiselta sivustolta](https://bitcoinbazar.fr/), mutta löydät myös luettelon myyjistä eri puolilla maailmaa [SeedSigner-projektin laitteistosivulta](https://seedsigner.com/hardware/). Jos haluat ostaa komponentit yksitellen, niitä on saatavilla suurimmilta sähköisen kaupankäynnin alustoilta tai erikoisliikkeistä.



## 2. Ohjelmiston valmistelu



Kun olet koonnut laitteistosi, sinun on valmisteltava microSD-kortti asentamalla siihen SeedSigner-järjestelmä. Voit tehdä tämän menemällä jokapäiväiseen henkilökohtaiseen tietokoneeseesi ja liittämällä SeedSignerille tarkoitetun microSD-kortin.



### 2.1. Lataa



Siirry [projektin viralliseen GitHub-arkistoon](https://github.com/SeedSigner/seedsigner/releases). Ohjelmiston uusin versio, lataa :




- Pi-malliasi vastaava .img-kuva.
- Tiedosto `.sha256.txt`.
- Tiedosto `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Ennen asennuksen aloittamista tarkistetaan ohjelmisto.



### 2.2 Verifiointi Linuxissa ja macOS:ssä



Aloita tuomalla SeedSigner-projektin virallinen julkinen avain suoraan Keybasesta :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Pääte ilmoittaa, että avain on tuotu tai päivitetty. Suorita seuraavaksi allekirjoitustiedoston tarkistuskomento (muista muuttaa komento versiosi mukaan, tässä `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Jos kaikki on oikein, tulosteen pitäisi olla `Hyvä allekirjoitus`. Tämä tarkoittaa, että tiedosto `.sha256.txt` on allekirjoitettu juuri tuodulla avaimella ja että allekirjoitus on pätevä. Älä välitä varoitusviestistä `VAROITUS: Tätä avainta ei ole varmennettu luotettavalla allekirjoituksella`: tämä on normaalia, sillä nyt sinun on tarkistettava, että käytetty avain kuuluu SeedSigner-projektiin.



Tätä varten vertaa näytetyn sormenjäljen 16 viimeistä merkkiä [Keybase.io/SeedSigner](https://keybase.io/seedsigner), [virallisessa Twitterissä](https://twitter.com/SeedSigner/status/1530555252373704707) tai [SeedSigner.com](https://seedsigner.com/keybase.txt) julkaistussa tiedostossa oleviin merkkeihin. Jos nämä tunnisteet täsmäävät, voit olla varma, että avain on todellakin projektin avain. Jos olet epävarma, lopeta heti ja pyydä apua SeedSigner-yhteisöltä (Telegram, X, GitHub...).



Kun avain on vahvistettu, voit tarkistaa, että ladattua kuvaa ei ole muutettu (muista muuttaa komento versiosi mukaan, tässä `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Linuxissa tämä komento on sisäänrakennettu.
- Varoitus: MacOS-versiot ennen `Big Sur (11)` eivät tunnista `--ignore-missing`-vaihtoehtoa. Tässä tapauksessa poista se ja jätä huomiotta varoitukset puuttuvista tiedostoista.



Odotettavissa oleva tulos on "OK" tiedoston ".img" vieressä. Tämä vahvistaa, että ladattu kuva on identtinen projektin julkaiseman kuvan kanssa eikä sitä ole muutettu.



### 2.3 Windows-varmistus



Windowsissa menettely on samanlainen, mutta komennot ovat erilaiset. Aloita asentamalla [Gpg4win](https://www.gpg4win.org/) ja avaa *Kleopatra*-sovellus. Tuo SeedSigner-projektin julkinen avain URL-osoitteesta Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Avaa seuraavaksi PowerShell kansiosta, jossa ladatut tiedostot sijaitsevat (Vaihto + hiiren kakkospainike > Avaa PowerShell tästä). Suorita seuraava komento manifestin allekirjoituksen tarkistamiseksi (muista muuttaa komento versiosi mukaan, tässä `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Jos kaikki on oikein, tulosteen pitäisi olla `Hyvä allekirjoitus`. Tämä tarkoittaa, että tiedosto `.sha256.txt` on allekirjoitettu juuri tuodulla avaimella ja että allekirjoitus on pätevä. Älä välitä varoitusviestistä `VAROITUS: Tätä avainta ei ole varmennettu luotettavalla allekirjoituksella`: tämä on normaalia, sillä nyt sinun on tarkistettava, että käytetty avain kuuluu SeedSigner-projektiin.



Tätä varten vertaa näytetyn sormenjäljen 16 viimeistä merkkiä [Keybase.io/SeedSigner](https://keybase.io/seedsigner), [virallisessa Twitterissä](https://twitter.com/SeedSigner/status/1530555252373704707) tai [SeedSigner.com](https://seedsigner.com/keybase.txt) julkaistussa tiedostossa oleviin merkkeihin. Jos nämä tunnisteet täsmäävät, voit olla varma, että avain on todellakin projektin avain. Jos olet epävarma, lopeta heti ja pyydä apua SeedSigner-yhteisöltä (Telegram, X, GitHub...).



Kun avain on vahvistettu, sinun on tarkistettava, ettei kuvatiedosto ole vioittunut. Voit tehdä tämän käyttämällä PowerShellissä seuraavaa komentoa :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Esimerkki Raspberry Pi Zero 2:lle (muista muuttaa komento version mukaan, tässä `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell laskee sen jälkeen kuvatiedoston SHA256-hashin. Vertaa tätä hash-arvoa vastaavaan arvoon tiedostossa `seedsigner.0.8.6.sha256.txt`.




- Jos nämä kaksi arvoa ovat täysin identtiset, tarkistus on onnistunut ja voit jatkaa.
- Jos ne eroavat toisistaan, tiedosto on vioittunut tai korruptoitunut. Älä käytä sitä ja aloita lataus uudelleen.



![Image](assets/fr/013.webp)



Onnistunut todentaminen takaa, että .img-tiedostosi on sekä aito (SeedSignerin allekirjoittama) että muuttumaton (muuttamaton). Tämän jälkeen voit siirtyä turvallisesti seuraavaan vaiheeseen.



### 2.4. Kuvan välähdys



Jos sinulla ei vielä ole sitä, lataa [Balena Etcher] -ohjelmisto (https://etcher.balena.io/) ja :




- Aseta microSD-kortti tietokoneeseen.
- Launch Etcher.
- Valitse ladattu ja tarkistettu .img-tiedosto.
- Valitse kohteeksi microSD-kortti.
- Klikkaa `Flash!`.



![Image](assets/fr/014.webp)



Odota, kunnes prosessi on valmis: microSD-korttisi on käyttövalmis. Nyt on aika koota!



## 3. SeedSigner-kokoonpano



Kun microSD-kortti on valmisteltu ja flashattu SeedSigner-ohjelmistolla, voit jatkaa lopullista kokoonpanoa. Ota aikaa, sillä jotkin osat ovat herkkiä (erityisesti pöytäliina, kamera ja GPIO-nastat).



### 3.1 Kotelon valmistelu



Avaa ensin kotelosi. Tarkista, että se on puhdas ja että sisäisten kiinnikkeiden tiellä ei ole 3D-tulostuksen muovijäämiä. Etsi :




- Kameran sijainti (pieni pyöreä reikä edessä).
- Näytön aukko.
- Raspberry Pi Zeron mikro-USB-porttien ja microSD-korttipaikan aukot.



### 3.2 Kameran asennus



Etsi Raspberry Pi Zeron kameranauhaliitin: se on ohut musta kaistale piirilevyn sivussa, jota voi avata nostamalla sitä hieman. Nosta sitä varovasti ylös pakottamatta: sen pitäisi vain kallistua muutaman millimetrin.



![Image](assets/fr/015.webp)



Aseta kameran kansi paikalleen. Ruskean/kuparisen osan on oltava alaspäin. Varmista, että se on tiukasti kiinni liittimessä ilman kiertymistä.



![Image](assets/fr/016.webp)



Sulje musta palkki pöytäliinan lukitsemiseksi (kuulet pienen naksahduksen). Tarkista varovasti, että se pysyy paikallaan eikä liiku.



![Image](assets/fr/017.webp)



Aseta sitten kameramoduuli kotelon sopivaan reikään. Mallista riippuen se voi napsahtaa suoraan paikalleen tai sen kiinnittämiseen tarvitaan pieni liimanauha. Linssin on oltava täydellisesti kohdakkain, ulospäin.



### 3.3 Raspberry Pi Zeron asentaminen



Jos käytät koteloa, aseta Raspberry Pi Zero -alusta sen sisään. Kohdista portit huolellisesti niille varattuihin aukkoihin.



Aseta sitten Waveshare-näyttö Raspberry Pi Zeron päälle. Piin GPIO-nastojen pitäisi olla täydellisesti linjassa näytön naarasliittimen kanssa. Paina näyttöä hitaasti nastojen päälle ja paina tasaisesti molemmilta puolilta, jotta ne eivät taivu.



![Image](assets/fr/018.webp)



Jos sinulla on kotelo, viimeistele kokoonpano lisäämällä etupaneeli ja ohjaussauva.



Aseta lopuksi flashattu ohjelmisto sisältävä microSD-kortti Raspberry Pi Zeron reunimmaiseen korttipaikkaan. Varmista, että se napsahtaa paikalleen.



### 3.4 Ensimmäinen käynnistys



Liitä mikro-USB-virtakaapeli omaan porttiin. Odota noin minuutti. SeedSigner-logon pitäisi tulla näkyviin, ja sen jälkeen aloitusnäyttö.



![Image](assets/fr/019.webp)



Tarkista aluksi, että eri komponentit toimivat oikein, menemällä valikkoon `Asetukset > I/O-testi`.



![Image](assets/fr/020.webp)



Testaa kaikki painikkeet ja varmista, että ne reagoivat oikein. Tarkista sitten napsauttamalla `KEY1`-painiketta, että kamera toimii odotetulla tavalla. Tämä ottaa kuvan.



![Image](assets/fr/021.webp)



### 3.5 Kameran säätö



Riippuen siitä, miten olet asentanut SeedSignerin, kamera saattaa näyttää käänteisen kuvan. Voit korjata tämän valitsemalla `Asetukset > Lisäasetukset > Kameran kierto` ja valitsemalla tarvittaessa 180°:n kierron.



![Image](assets/fr/022.webp)



Jos olet muuttanut kameran suuntausta tai haluat muuttaa muita asetuksia (kuten käyttöliittymän kieltä) myöhemmin, sinun on otettava käyttöön asetusten pysyvyys microSD-kortilla. Muuten asetukset palautuvat oletusasetuksiin aina uudelleenkäynnistyksen yhteydessä, sillä Raspberry Pi Zerossa ei ole pysyvää muistia.



Voit tehdä tämän avaamalla valikon `Asetukset > Pysyvät asetukset` ja valitsemalla sitten `Ohjattu`.



![Image](assets/fr/023.webp)



Jos kaikki on kunnossa, SeedSigner on nyt käyttövalmis!



## 4. SeedSignerin asetukset



Ennen Bitcoin wallet:n luomista määritetään SeedSigner. Koska se toimii Raspberry Pi Zerossa ilman pysyvää muistia, sen asetukset eivät tallennu automaattisesti, ellet tallenna niitä microSD-kortille. Varmista siis, että olet ottanut tämän vaihtoehdon käyttöön, muuten asetukset menetetään uudelleenkäynnistyksen yhteydessä (katso vaihe 3.5).



### 4.1 Parametrivalikon käyttö



Käynnistä SeedSigner ja odota, että aloitusnäyttö tulee näkyviin. Siirry joystickillä kohtaan `Settings` (Asetukset) ja vahvista sitten painamalla keskipainiketta. Pääset nyt pääasetusvalikkoon.



![Image](assets/fr/024.webp)



### 4.2 Salkunhallintaohjelmiston valinta



Siirry sitten valikkoon `Coordinator software`.



![Image](assets/fr/025.webp)



Koordinaattori tarkoittaa salkunhallintaohjelmistoa, jonka kanssa SeedSigner kommunikoi QR-koodien avulla. Tämä ohjelmisto asennetaan joko tietokoneeseen tai älypuhelimeen. Sen avulla voit hallinnoida bitcoinejasi, mutta ilman, että pääset koskaan käsiksi yksityisiin avaimiisi. SeedSigner pysyy ainoana laitteena, joka pystyy allekirjoittamaan transaktiosi.



Nykyinen laiteohjelmistoversio tukee useita ohjelmia: Sparrow, Specter, BlueWallet, Nunchuk ja Keeper. Omassa tapauksessani käytän **Sparrow Wallet**, jota suosittelen erityisesti sen yksinkertaisuuden ja runsaan toiminnallisuuden vuoksi.



Jos et tiedä, miten se asennetaan, voit seurata tätä ohjetta:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Valitse vain haluamasi ohjelmisto valikosta.



![Image](assets/fr/026.webp)



### 4.3 Yksiköiden ja määrän näyttö



Valikossa `Denomination Display` voit valita yksikön, jossa määrät näytetään:




- `BTC`
- mBTC` (milli-bittikolikko, tai 0,001 BTC)
- gW-15 (satoshi eli 1/100 000 000 BTC)



**sats**-yksikkö on yleensä käytännöllisin pienille määrille.



![Image](assets/fr/027.webp)



### 4.4 Lisäasetukset



Siirry nyt Lisäasetukset-valikkoon. Täältä löydät useita hyödyllisiä vaihtoehtoja:




- gW-17 network`: muutetaan vain, jos haluat käyttää SeedSigneria Testnet:ssä.
- qR-koodin tiheys`: säätää kunkin QR-koodin sisältämän tiedon määrää. Voit jättää oletusarvon, ellet koe sen lukemista vaikeaksi skannauksen aikana.
- `Xpub export`: ottaa käyttöön tai poistaa käytöstä laajennetun julkisen avaimesi (`xpub`, `ypub`, `zpub`) viennin salkunhallintaohjelmistoon QR-koodin avulla (toiminto, jota käytämme myöhemmin, joten jätä se toistaiseksi käyttöön).
- `Skriptityypit`: määrittelee skriptityypit, joiden avulla bitcoinit voidaan lukita. Tätä parametria ei tarvitse muuttaa, sillä skriptityyppi asetetaan suoraan arvoon Sparrow. Tässä tapauksessa kyse on vain skripteistä, joita SeedSignerilla on oikeus käsitellä.



### 4.5 Kielen valinta



Lopuksi voit vaihtaa käyttöliittymän kielen haluamallasi tavalla Kieli-valikossa.



![Image](assets/fr/028.webp)



## 5. seed:n luominen ja tallentaminen



seed (tai muistisääntö) muodostaa Bitcoin-salkun perustan. Sitä käytetään yksityisten avainten ja osoitteiden johtamiseen, ja sen avulla pääset käsiksi varoihisi. SeedSigner tarjoaa useita menetelmiä sen luomiseen, joita tarkastelemme tässä jaksossa.



Ennen kuin aloitamme, muutama tärkeä muistutus:




- Tämä lause antaa täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi.** Kuka tahansa, jolla on tämä lause hallussaan, voi varastaa varasi, vaikka hänellä ei olisi fyysistä pääsyä SeedSigneriin;
- Yleensä wallet-laitteiston palauttamiseen wallet-laitteiston katoamisen tai varkauden yhteydessä käytetään 12-sanaista lausetta. Mutta koska SeedSigner on *tilaton* laite, se ei koskaan rekisteröi seed-laitettasi. Fyysiset varmuuskopiot eivät siis ole pelkkiä varmuuskopioita, vaan **ainoa tapa käyttää wallet:ta**. Jos menetät nämä varmuuskopiot, bitcoinisi menetetään pysyvästi. Varmuuskopioi ne siis huolellisesti, useille eri välineille ja turvallisiin paikkoihin;
- Jos olet vasta aloittamassa, suosittelen vahvasti lukemaan tämän opetusohjelman, jotta saat yksityiskohtaisen käsityksen muistikielilauseen hallintaan liittyvistä riskeistä:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 seed:n luontityökalun käyttäminen



Siirry SeedSignerin aloitusnäytöltä `Tools`-valikkoon.



![Image](assets/fr/029.webp)



Nyt generate on seed. seed on yksinkertaisesti suuri satunnaisluku. Mitä satunnaisemmin se on luotu, sitä varmempi se on. SeedSigner tarjoaa kaksi tapaa tehdä tämä:




- kamera": seed syntyy valokuvan visuaalisesta kohinasta. Otetaan kuva satunnaisesta ympäristöstä (esine, maisema, kasvot jne.), jonka pikselivaihteluita käytetään generate entropian määrittämiseen. Menetelmä on nopea, mutta ei toistettavissa.
- nopanheitto": heität noppaa luodaksesi tarvittavan entropian. Se on aikaa vievämpää, mutta toistettavissa ja siten todennettavissa. Jos valitset tämän menetelmän, noudata tämän ohjeen neuvoja (tarkistussummaa ei tarvitse laskea, SeedSigner huolehtii siitä):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 seed:n luominen valokuvan avulla



Jos valitset valokuvamenetelmän, napsauta `Uusi seed` (kamerakuvakkeella), ota kuva ja vahvista. Valitse sitten lauseen pituus (12 tai 24 sanaa), joka ilmestyy näytölle tallennusta varten. Seuraavat vaiheet ovat samat kuin osassa 5.3.



### 5.3 seed:n luominen noppien avulla



Tässä ohjeessa käytämme **Nopanheittomenetelmää**. Napsauta `New seed` (jossa on noppakuvake).



![Image](assets/fr/030.webp)



Valitse sitten muistisääntölauseesi pituus. 12 sanaa tarjoaa jo riittävän turvatason, joten suosittelen tätä vaihtoehtoa.



![Image](assets/fr/031.webp)



Heitä noppaa ja kirjoita tuloksena olevat numerot kursorin avulla. Vahvista jokainen syöttö painamalla keskipainiketta. Jos teet virheen, voit palata takaisin. Käytä useita eri noppia vähentääksesi epätasapainoisten noppien vaikutusta. Varmista, ettei sinua tarkkailla tämän toiminnon aikana.



![Image](assets/fr/032.webp)



Kun olet syöttänyt 50 heittoa, SeedSigner luo lauseesi. **Seuraa tämän ohjeen ohjeita huolellisesti, jos olet vasta aloittamassa:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 seed:n näyttäminen ja tallentaminen



Kirjoita muistisanan sanat huolellisesti sopivalle fyysiselle alustalle (paperille tai metallille).



![Image](assets/fr/033.webp)



### 5.5 Varmuuskopion tarkistaminen



Varmuuskopiointivirheiden välttämiseksi SeedSigner pyytää sinua tarkistamaan varmuuskopion. Klikkaa `Verify`.



![Image](assets/fr/034.webp)



Kirjoita sitten pyydetty sana sen mukaan, missä järjestyksessä se on lauseessa. Esimerkiksi tässä tapauksessa minun on valittava lauseen kolmas sana.



![Image](assets/fr/035.webp)



Jos teet virheen, SeedSigner ilmoittaa sinulle siitä, ja sinun on aloitettava alusta. Muista merkitä muistisääntösi muistiin, kun se annetaan sinulle. Tämä varmennusvaihe varmistaa, että varmuuskopiosi on oikea ja täydellinen. Kun varmennus on vahvistettu, näytöllä näkyy `Backup Verified`.



![Image](assets/fr/036.webp)



Jos haluat tehdä täydellisemmän palautustestin, seuraa tätä ohjetta :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Tilattoman laitteen käsitteen ymmärtäminen



SeedSigner on laite, jolla ei ole pysyvää muistia. Tämä tarkoittaa, että seed:tä ei koskaan tallenneta laitteen sisälle (toisin kuin esimerkiksi Ledger:ää, Trezoria tai Coldcardia). Heti kun katkaiset laitteen virran, seed katoaa kokonaan sen RAM-muistista. Kun käynnistät laitteen uudelleen, SeedSigner palaa tyhjään tilaan: sinun on sitten annettava sille seed uudelleen, jotta se voi allekirjoittaa tapahtumasi.



Tämä tarjoaa välttämättömän suojan. Toisin kuin muut laitteistolompakot, SeedSigner perustuu Raspberry Pi Zeroon, jossa ei ole fyysistä suojausta, kuten *Secure Element*. Koska arkaluonteisia tietoja ei kuitenkaan tallenneta, hyökkääjä ei voisi edes fyysisesti vahingoittuneen laitteen avulla poimia yksityisiä avaimiasi tai käyttää bitcoinejasi.



Toisaalta tähän arkkitehtuuriin liittyy lisävastuu: ilman varmuuskopiota varasi ovat lopullisesti menetettyjä. Siksi suosittelen **tupla-varmuuskopiointia**. Sinulla on jo palautuslausekkeesi: tämä on tärkein pitkäaikainen varmuuskopio, jota säilytetään turvallisessa paikassa. Nyt luomme tästä lauseesta kopion **QR-koodin** muodossa.



Aina kun käytät SeedSigneria, skannaat tämän QR-koodin laitteen kameralla, jolloin laite lataa seed:n väliaikaisesti muistiinsa sillä aikaa, kun allekirjoitat tapahtumia. Myös tätä toista, jokapäiväiseen käyttöön tarkoitettua varmuuskopiota on säilytettävä erittäin huolellisesti: kuka tahansa, jolla on hallussaan tämä QR-koodi, pääsee täysin käsiksi bitcoineihisi.


Suosittelen myös säilyttämään QR-koodin ja muistisäännön kahdessa eri paikassa, jotta kaikki ei katoa vahinkotapauksessa.



Kehittyneempi ja turvallisempi vaihtoehto on käyttää SeedSigneriä yhdessä **SeedKeeper**:n kanssa, joka tallentaa seed:n secure element:ään. Jos haluat lisätietoja, katso tämä opetusohjelma:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Kirjoita pääavaimen sormenjälki



Kun varmennus on valmis, SeedSigner näyttää wallet:n pääavaimen sormenjäljen. Tämä sormenjälki tunnistaa wallet:n ja varmistaa, että käytät oikeaa palautuslausetta tulevaisuudessa. Se ei paljasta mitään tietoja yksityisistä avaimista, joten voit tallentaa sen turvallisesti digitaaliselle tietovälineelle. Varmista vain, että säilytät kopion, johon on pääsy, etkä koskaan hukkaa sitä.



![Image](assets/fr/037.webp)



Tässä vaiheessa voit myös lisätä **passphrase BIP39**:n vahvistamaan wallet:n turvallisuutta. Varmuuskopiointistrategiastasi riippuen tämä vaihtoehto voi olla kannattava, mutta siihen liittyy myös riskejä: jos menetät passphrase:n, pääsy bitcoineihisi menetetään pysyvästi.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Jos passphrase-käsite ei ole vielä tuttu, kehotan sinua lukemaan tämän kattavan oppaan aiheesta:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 seed:n tallentaminen QR-muodossa (*SeedQR*)



SeedSignerin avulla voit muuntaa seed:n paperiseksi QR-koodiksi, jota kutsutaan *SeedQR*:ksi. Tämä menetelmä yksinkertaistaa wallet:n lataamista, koska sen avulla vältetään jokaisen sanan kirjoittaminen uudelleen manuaalisesti.



Tätä varten tarvitset tyhjän paperin tai metallisen QR-koodin, joka vastaa muistilauseesi pituutta. Jos olet ostanut täydellisen paketin SeedSigneriäsi varten, mallit ovat yleensä mukana. Jos näin ei ole, voit ladata ja tulostaa ne (tai jäljentää ne käsin) täältä :




- [12 sanan muodossa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24 sanan muodossa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompakti muoto 12 sanaa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompakti muoto 24 sanaa](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Valitse seed-näytöltä `Backup Seed`.



![Image](assets/fr/039.webp)



Valitse sitten `Export as SeedQR`.



![Image](assets/fr/040.webp)



Valitse sitten haluamasi muoto (normaali tai kompakti) käytettävissä olevan paperimallien mukaan.



![Image](assets/fr/041.webp)



Aloita *SeedQR*:n luominen napsauttamalla `Begin`. SeedSigner näyttää tämän jälkeen sarjan ruudukoita (A1, A2, B1 jne.), joista kukin vastaa koodin osaa.



![Image](assets/fr/042.webp)



Jäljennä huolellisesti jokainen musta piste tallennuslomakkeellesi ja siirry sitten joystickillä seuraavaan lohkoon. Ota aikaa: yksinkertainen virheellinen kohdistus voi tehdä QR-koodista käyttökelvottoman.



Muutamia vinkkejä:




- Aloita lyijykynällä, jotta voit korjata mahdolliset virheet, ja palaa sitten takaisin hienoon mustaan kynään, kun olet valmis;
- Tarvitset vain hyvin keskitetyn pisteen neliön keskelle, sitä ei tarvitse täyttää kokonaan.



![Image](assets/fr/043.webp)



Napsauta sitten `Vahvista SeedQR` ja skannaa QR-koodisi tarkistaaksesi, että se toimii oikein.



![Image](assets/fr/044.webp)



Jos näyttöön tulee viesti `Success`, *SeedQR* on voimassa: voit siirtyä seuraavaan vaiheeseen.



![Image](assets/fr/045.webp)



**Pitäkää tämä lomake yhtä tiukasti tallessa kuin toipumislauseenne. Kuka tahansa, jolla on hallussaan tämä QR-koodi, voi rekonstruoida yksityiset avaimesi ja varastaa bitcoinisi.** *



Onnittelut, Bitcoin-salkkusi on nyt toiminnassa! Tuomme nyt sen julkiset komponentit **Sparrow Wallet**:ään, jotta sitä on helppo hallita.



## 6. Tuo wallet Sparrow:een



Kun SeedSigner on perustettu ja seed on luotu ja tallennettu oikein, seuraava vaihe on yhdistää tämä salkku hallintaohjelmistoon, kuten Sparrow Wallet:een. seed pysyy aina offline-tilassa, sillä vain salkun julkinen osa siirretään Sparrow:een. Näin ohjelmisto voi näyttää osoitteesi, transaktiosi ja rakentaa uusia transaktioita ilman, että voit koskaan käyttää bitcoinejasi. Käyttääksesi bitcoinejasi SeedSignerisi on aina allekirjoitettava Sparrow:n valmistelemat transaktiot.



### 6.1 SeedSignerin valmistelu



Aseta käyttöjärjestelmän sisältävä microSD-muistikortti paikalleen, kytke SeedSigner päälle ja lataa sitten seed, jonka olet juuri luonut varmuuskopion QR-koodista. Valitse aloitusnäytössä `Scan` ja skannaa sitten SeedQR SeedSignerillä.



![Image](assets/fr/046.webp)



Tarkista, että pääavaimessa oleva sormenjälki vastaa wallet:n sormenjälkeä. Jos käytät passphrase:ta, syötä se tässä vaiheessa.



![Image](assets/fr/047.webp)



Tämä vie sinut salkkusi valikkoon, jonka nimi on minun tapauksessani `d4149b27`. Jos olet taas aloitusnäytöllä, valitse `Seeds` ja valitse sitten portfoliota vastaava tuloste. Napsauta sitten `Export Xpub`.



![Image](assets/fr/048.webp)



Valitse salkkutyyppi. Meidän tapauksessamme kyseessä on yksittäinen salkku: valitse `Single Sig`.



![Image](assets/fr/049.webp)



Seuraavaksi on vuorossa skriptistandardin valinta. Uusin ja transaktiokustannuksiltaan edullisin on Taproot. Siksi suosittelen valitsemaan tämän standardin.



![Image](assets/fr/050.webp)



Näyttöön tulee varoitusviesti. Tämä on normaalia: tämän laajennetun julkisen avaimen (`xpub`) avulla voit tarkastella kaikkia seed:stä johdettuja osoitteita (ensimmäisellä tilillä). Sen avulla et voi käyttää varojasi, mutta se paljastaa salkkusi rakenteen. Jos se joskus vuotaa, se on ongelma yksityisyydellesi, mutta ei bitcoinien turvallisuudelle: sen avulla voit nähdä ne, mutta et käyttää niitä.



Napsauta `I Understand` ja sitten `Export Xpub`, jos olet tyytyväinen näytettyihin tietoihin.



Sen jälkeen SeedSigner luo xpubin dynaamisen QR-koodin muodossa, joka sisältää kaikki tiedot, joita tarvitset salkkusi hallintaan Sparrow Wallet:ssä.



![Image](assets/fr/051.webp)



Voit säätää näytön kirkkautta joystickillä QR-koodin skannauksen helpottamiseksi.



### 6.2 Uuden salkun tuominen Sparrow:een Wallet:een



Varmista, että Sparrow Wallet -ohjelmisto on asennettu tietokoneeseen. Jos et tiedä, miten se ladataan, tarkistetaan ja asennetaan oikein, katso koko ohjeemme aiheesta:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Avaa tietokoneella Sparrow Wallet ja valitse sitten valikkoriviltä `File → Import Wallet`.



![Image](assets/fr/052.webp)



Selaa alaspäin kohtaan `SeedSigner` ja valitse sitten `Scan...`. Webbikamerasi avautuu: skannaa SeedSigner-näytössä näkyvä dynaaminen QR-koodi.



![Image](assets/fr/053.webp)



Anna salkullesi nimi ja napsauta sitten `Create Wallet`. Sparrow pyytää sinua asettamaan salasanan, jolla lukitset paikallisen pääsyn tähän wallet:een. Valitse vahva salasana: se suojaa pääsyn salkun tietoihin Sparrow:ssä (julkiset avaimet, osoitteet, tarrat ja tapahtumahistoria). Tätä salasanaa ei tarvita salkun palauttamiseen myöhemmin: tähän tarkoitukseen tarvitaan vain muistisana (ja mahdollisesti passphrase).



Suosittelen, että tallennat tämän salasanan salasanahallintaan, jotta et menetä sitä.



![Image](assets/fr/054.webp)



Avaintallennustietokantasi on nyt onnistuneesti tuotu.



![Image](assets/fr/055.webp)



Tarkista sitten, että Sparrow:ssa näkyvä `Master fingerprint` vastaa SeedSignerissä aiemmin merkittyä sormenjälkeä.



SeedSigner ja Sparrow Wallet ovat nyt turvallisesti yhteydessä toisiinsa. Sparrow toimii täydellisenä hallintaliittymänä, kun taas SeedSigner on edelleen ainoa laite, joka pystyy allekirjoittamaan tapahtumia. Olet nyt valmis vastaanottamaan ja lähettämään bitcoineja täysin ilmaverkossa.



## 7. Bitcoinien vastaanottaminen ja lähettäminen



SeedSigner ja Sparrow Wallet on nyt määritetty toimimaan yhdessä. Tässä viimeisessä osiossa tarkastelemme, miten voit vastaanottaa ja lähettää bitcoineja tämän kokoonpanon avulla.



### 7.1 Bitcoinien vastaanottaminen



#### 7.1.1 Vastaanotto-osoitteen luominen



Avaa tietokoneella Sparrow Wallet ja avaa SeedSigner wallet -lukitus salasanalla. Varmista, että ohjelmisto on yhdistetty palvelimeen (lovi oikeassa alakulmassa). Napsauta sivupalkissa `Vastaanottaa`.



![Image](assets/fr/056.webp)



Uusi Bitcoin-osoite näytetään. Näet :




- Tekstiosoite (joka alkaa kirjaimella `bc1p...`, jos käytät P2TR:tä kuten minä),
- Vastaava QR-koodi,
- `Label`-kenttä tapahtumien seurantaa varten.



Suosittelen lämpimästi, että lisäät tarran jokaiseen bitcoin-kuittiin wallet:ssa. Näin voit helposti tunnistaa jokaisen UTXO:n alkuperän ja parantaa yksityisyydenhallintaa. Jos haluat syventyä tähän tärkeään aiheeseen tarkemmin, voit tutustua Plan ₿ Academyn omaan koulutukseen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Voit lisätä etiketin yksinkertaisesti kirjoittamalla nimen `Label`-kenttään ja vahvistamalla sen jälkeen.



Esimerkiksi:



```txt
Label : Sale of the Raspberry Pi Zero
```



Osoitteesi on nyt yhdistetty tähän merkkiin kaikissa Sparrow-osastoissa.



![Image](assets/fr/057.webp)



#### 7.1.2 Address-tarkastus SeedSignerissa



Ennen kuin jaat vastaanotto-osoitteesi, on erittäin tärkeää tarkistaa, että se kuuluu seed:lle. Tämä vaihe varmistaa, että SeedSigner voi allekirjoittaa tähän osoitteeseen liittyviä tapahtumia. Se suojaa myös mahdollisilta hyökkäyksiltä, joissa Sparrow näyttää väärän osoitteen. Muista, että Sparrow toimii turvattomassa ympäristössä (tietokoneessasi), jossa on paljon suurempi hyökkäyspinta kuin SeedSignerissäsi, joka on täysin eristetty. Siksi sinun ei koskaan pidä sokeasti uskoa Sparrow:n esittämiä vastaanottoosoitteita, ennen kuin olet tarkistanut ne wallet-laitteistollasi.



Sparrow:ssä voit suurentaa osoitteen QR-koodia napsauttamalla sitä, jolloin se näkyy koko näytöllä.



![Image](assets/fr/058.webp)



Valitse SeedSignerin päävalikosta `Scan`. Skannaa tietokoneen näytöllä näkyvä QR-koodi ja valitse sitten wallet:tä vastaava seed (minun tapauksessani sormenjälki `d4149b27`).



![Image](assets/fr/059.webp)



Jos skannattu osoite vastaa seed:sta saatua osoitetta, SeedSigner-näytöllä näkyy viesti: "Address vahvistettu".



![Image](assets/fr/060.webp)



Tämä vahvistaa, että osoite kuuluu wallet:ään ja että voit vastaanottaa siitä bitcoineja.



#### 7.1.3 Varojen vastaanottaminen



Voit nyt välittää tämän osoitteen (tekstinä tai QR-koodina) henkilölle tai osastolle, jonka on lähetettävä sinulle satss. Kun maksutapahtuma on lähetetty verkossa, se näkyy Sparrow Wallet:n "maksutapahtumat"-välilehdellä.



![Image](assets/fr/061.webp)



### 7.2 Lähetä bitcoineja



Bitcoinien lähettäminen SeedSignerin avulla on kolmivaiheinen prosessi:




- Tapahtuman luominen Sparrow:ssä ;
- SeedSigner-tapahtuman allekirjoitus ;
- Liiketoimen lopullinen jakelu Sparrow:n kautta.



Kaikki näiden kahden laitteen välinen vaihto tapahtuu yksinomaan QR-koodien avulla.



#### 7.2.1 Tapahtuman luominen Sparrow:ssä



Sparrow Wallet:ssä voit napsauttaa vasemmanpuoleisen sivupalkin Lähetä-välilehteä. Käytän kuitenkin mieluummin `UTXOs`-välilehteä, jonka avulla voit harjoitella "*Coin Control*". Tämä menetelmä antaa sinulle tarkan kontrollin käytettävistä UTXO:ista, joten voit hallita tietoja, jotka paljastat tapahtuman aikana.



Valitse `UTXOs`-välilehdeltä kolikot, jotka haluat käyttää, ja napsauta sitten `Send Selected`.



![Image](assets/fr/062.webp)



Täytä sitten tapahtumakentät:




- Liitä vastaanottajan osoite kohtaan "Maksa vastaanottajalle" tai skannaa QR-koodi napsauttamalla kamerakuvaketta;
- Lisää kohtaan `Label` merkintä, jolla tätä kulua seurataan;
- Kirjoita lähetettävä summa kohtaan `Määrä`;
- Valitse lopuksi nykyisiin markkinaolosuhteisiin perustuva maksuprosentti (arvioita on saatavilla osoitteessa [mempool.space](https://mempool.space/)).



Kun kentät on täytetty, tarkista tiedot huolellisesti ja napsauta sitten "Luo tapahtuma >>".



![Image](assets/fr/063.webp)



Tarkista tapahtuman tiedot varmistaaksesi, että kaikki on oikein, ja napsauta sitten "Viimeistele tapahtuma allekirjoitusta varten".



![Image](assets/fr/064.webp)



Kauppa on nyt valmis, mutta sitä ei ole vielä allekirjoitettu. Jos haluat näyttää [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) QR-koodina, napsauta `Show QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Tapahtuman allekirjoittaminen SeedSignerin kanssa



Kytke SeedSigner päälle ja skannaa SeedQR:si päästäksesi salkkuusi käsiksi tavalliseen tapaan. Valitse aloitusnäytöltä `Scan` ja skannaa sitten Sparrow:ssä näkyvä QR-koodi.



![Image](assets/fr/066.webp)



Valitse sitten salkkuusi sopiva seed.



![Image](assets/fr/067.webp)



SeedSigner tunnistaa automaattisesti, että kyseessä on PSBT, ja näyttää yhteenvedon tapahtumasta:




   - Lähetetty määrä,
   - Lähtöosoitteet,
   - Siihen liittyvät transaktiokustannukset.



Klikkaa `Review Details` ja tarkista kaikki tiedot huolellisesti suoraan SeedSigner-näytöltä. Tärkeimmät tarkistettavat tiedot ovat lähetetty summa, vastaanottajan osoite ja veloitettujen maksujen määrä.



![Image](assets/fr/068.webp)



Jos kaikki on kunnossa, valitse "Hyväksy PSBT" allekirjoittaaksesi tapahtuman käyttämällä vastaavaa yksityistä avainta tai vastaavia yksityisiä avaimia.



![Image](assets/fr/069.webp)



Allekirjoituksen jälkeen SeedSigner luo uuden QR-koodin, joka sisältää allekirjoitetun tapahtuman ja on valmis skannattavaksi Sparrow:llä.



![Image](assets/fr/070.webp)



#### 7.2.3 Tapahtuman lähetys Sparrow:stä



Nyt kun transaktio on voimassa, se on lähetettävä Bitcoin-verkossa, jotta se saavuttaa louhijan, joka lisää sen lohkoon.



Napsauta Sparrow:ssa "QR Scan".



![Image](assets/fr/071.webp)



Näytä SeedSignerin näyttämä QR-koodi (allekirjoitetun tapahtuman QR-koodi) web-kameralle. Sparrow purkaa allekirjoituksen ja näyttää kaikki tapahtuman tiedot. Tarkista vielä, että kaikki tiedot ovat oikein, ja lähetä transaktio Bitcoin-verkkoon napsauttamalla Broadcast Transaction.



![Image](assets/fr/072.webp)



Tapahtumasi on nyt lähetetty Bitcoin-verkkoon. Voit seurata sen etenemistä Sparrow Wallet:n `Transaktiot`-välilehdellä.



![Image](assets/fr/073.webp)



Olet nyt oppinut SeedSignerin käytön perusteet. Jos haluat syventää tietämystäsi ja tutustua edistyneempiin käyttötapoihin, voit tutustua seuraavaan opetusohjelmaan:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Voit myös tukea avoimen lähdekoodin SeedSigner-projektin kehitystä tekemällä lahjoituksen bitcoineina!](https://seedsigner.com/donate/)**



*Luotto: osa tämän ohjeen kuvista on peräisin [SeedSigner-projektin virallisilta verkkosivuilta](https://seedsigner.com/) ja [GitHub-arkistosta](https://github.com/SeedSigner/seedsigner).*