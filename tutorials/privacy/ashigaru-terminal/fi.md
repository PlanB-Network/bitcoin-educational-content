---
name: Ashigaru Terminal
description: Käytä Ashigaru työpöydällä tehdä coinjoins
---

![cover](assets/cover.webp)



Ashigaru Terminal on Ashigaru-tiimin versio Sparrow Serveristä, joka toteuttaa Whirlpool coinjoin-protokollan. Tämä ohjelmisto on jatkoa Samourai Wallet:n aloittamalle työlle, erityisesti Whirlpool GUI:lle, jonka perusperiaatteita se noudattaa: itsesäilytys ja luottamuksellisuuden säilyttäminen.



Tämä ohjelmisto on Sparrow-palvelimen fork, joka on muokattu ja optimoitu täydellistä integrointia varten Whirlpool-ekosysteemiin, ZeroLink coinjoin-protokollaan, jonka Samourai-tiimit ovat alun perin kehittäneet.



Ashigaru Terminal toimii minimalistisen TUI-käyttöliittymän avulla, ja se voidaan ottaa käyttöön henkilökohtaisella tietokoneella tai erillisellä palvelimella. Sen avulla voit olla suoraan vuorovaikutuksessa Whirlpool:n kanssa käynnistääksesi "*Tx0*", hallinnoidaksesi "*Deposit*", "*Premix*", "*Postmix*" ja "*Badbank*" -tilejä sekä tehdä automaattisia remixejä vahvistaaksesi osien luottamuksellisuutta.



Lyhyesti sanottuna Ashigaru Terminal on erityisen hyödyllinen, jos haluat luoda coinjoineja Whirlpool:n avulla.



Tässä ensimmäisessä opetusohjelmassa käyn läpi Ashigaru Terminalin asennuksen ja käytön. Toinen, edistyneempi opetusohjelma on sitten omistettu varsinaiselle kolikkoliitosten luomiselle.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Asenna Ashigaru Terminal



Ashigaru Terminalin asentamiseen tarvitset Tor-selaimen, koska binäärit jaetaan vain Tor-verkon kautta. Jos et ole vielä tehnyt sitä, [asenna se koneellesi](https://www.torproject.org/download/).



### 1.1. lataa Ashigaru Terminal



Siirry Tor Browserista [heidän Git-tietovarastonsa julkaisusivulle](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) ladataksesi Ashigaru Terminalin uusimman version käyttöjärjestelmääsi.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Lataa seuraavat 2 tiedostoa käyttöjärjestelmääsi:




- Binaari (`ashigaru_terminal_v1.0.0_amd64.deb` Debian/Ubuntu, `.dmg` macOS tai `.zip` Windows) ;
- Allekirjoitettu hashed-tiedosto: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Tarkista Ashigaru Terminal



Ennen kuin käytät ohjelmistoa laitteessasi, sinun on tarkistettava sen aitous ja eheys. Tämä on tärkeä vaihe, sillä se estää sinua asentamasta väärennettyä versiota, joka voisi vaarantaa bitcoinisi tai tartuttaa koneesi.



Avaa uusi selaimen välilehti ja siirry [Keybase verification tool](https://keybase.io/verify). Liitä juuri lataamasi `.txt`-tiedoston sisältö sille varattuun kenttään ja napsauta sitten `Verify`-painiketta.



![Image](assets/fr/02.webp)



Jos haluat monipuolistaa todentamislähteitänne, voitte myös verrata viestiä siihen, joka on saatavilla clearnet-sivustolla [ashigaru.rs](https://ashigaru.rs/download/), kohdassa `/download`.



![Image](assets/fr/03.webp)



Jos allekirjoitus on pätevä, Keybase näyttää viestin, joka vahvistaa, että Ashigarun kehittäjät ovat allekirjoittaneet tiedoston.



![Image](assets/fr/04.webp)



Voit myös napsauttaa Keybasen näyttämää `ashigarudev`-profiilia ja tarkistaa, että hänen avaimensa sormenjälki täsmää täsmälleen : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Jos tässä vaiheessa ilmenee virhe, allekirjoitus on virheellinen. Tässä tapauksessa **en asenna ladattua ohjelmistoa**. Aloita alusta tai pyydä yhteisöltä apua ennen jatkamista.



Keybase on toimittanut sinulle sovelluksen todennetun hashin. Tarkistamme nyt, että lataamasi `.deb`-, `.zip`- tai `.dmg`-tiedoston hash täsmää Keybasen vahvistaman hashin kanssa. Tee tämä siirtymällä [HASH FILE ONLINE](https://hash-file.online/).



Napsauta `BROWSE...-painiketta ja valitse vaiheessa 1.1 ladattu `.deb`, `.zip` tai `.dmg`-tiedosto. Valitse sitten `SHA-256`-hash-funktio ja napsauta `CALCULATE HASH` -painiketta generate-tiedoston hashin laskemiseksi.



![Image](assets/fr/06.webp)



Sivusto näyttää sitten ohjelmiston hashin. Vertaa sitä Keybase.io-sivustolla tarkistamaasi hashiin. Jos ne täsmäävät täydellisesti, aitouden ja eheyden tarkistus on onnistunut. Voit sitten käyttää ohjelmistoa.



![Image](assets/fr/07.webp)



### 1.3 Ashigaru-terminaalin käynnistäminen





- Debian / Ubuntu



Asenna ohjelmisto suorittamalla komento :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Muuta järjestystä ladatun version mukaan.



Tarkista sitten asennus:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Käynnistä sitten ohjelmisto:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Napsauta hiiren kakkospainikkeella lataamaasi ja tarkistamaasi `.zip`-tiedostoa ja valitse sitten `Extract All...` poistaaksesi sen sisällön.



Kun purku on valmis, kaksoisnapsauta `Ashigaru-terminal.exe`-tiedostoa käynnistääksesi ohjelmiston.



![Image](assets/fr/08.webp)



## 2. Ashigaru Terminalin käytön aloittaminen



Ashigaru Terminal on TUI-ohjelma (*Text-based User Interface*) eli minimalistinen käyttöliittymä, joka toimii suoraan päätelaitteessa. Vuorovaikutat sen kanssa valikoiden ja pikanäppäinten avulla, mutta ilman mitään varsinaista klassista graafista ympäristöä.



![Image](assets/fr/09.webp)



Se on helppokäyttöinen: navigoi valikoissa näppäimistön nuolinäppäimillä ja paina Enter-näppäintä, kun haluat vahvistaa toiminnon tai vahvistaa valinnan.



## 3. Solmun liittäminen Ashigaru-terminaaliin



Oletusarvoisesti Ashigaru Terminal muodostaa yhteyden julkiseen Electrum-palvelimeen. Tämä aiheuttaa luonnollisesti riskejä luottamuksellisuuden ja suvereniteetin kannalta. Siksi konfiguroimme sen niin, että se muodostaa yhteyden suoraan omaan Electrum Server-palvelimeesi.



Voit tehdä tämän avaamalla valikon `Preferences > Server` (Asetukset > Palvelin).



![Image](assets/fr/10.webp)



Napsauta `< Muokkaa >` -painiketta.



![Image](assets/fr/11.webp)



Valitse `Private Electrum Server` ja napsauta sitten `<Jatka>`.



![Image](assets/fr/12.webp)



Kirjoita palvelimesi URL-osoite ja portti. Voit määrittää Tor-osoitteen muodossa `.onion`. Varmista yhteys napsauttamalla `< Test >`.



![Image](assets/fr/13.webp)



Jos yhteys onnistuu, näyttöön ilmestyy viesti `Success` ja palvelimen tiedot.



![Image](assets/fr/14.webp)



Jos sinulla ei vielä ole Bitcoin-solmua, suosittelen osallistumaan tälle kurssille:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Minun tapauksessani katkaisen tämän ohjeen ajaksi yhteyden Electrs-palvelimeen, koska työskentelen testnetissä. Toiminta pysyy kuitenkin täysin identtisenä mainnet:ssä.*



## 4. Luo portfolio Ashigaru Terminalissa



Nyt kun ohjelmisto on määritetty oikein, voimme lisätä Bitcoin-salkun.



Sinulla on kaksi vaihtoehtoa:




- Voit luoda uuden wallet:n tyhjästä ja käyttää sitä yksinomaan Ashigaru-terminaalissa. Tässä tapauksessa sinun on avattava tämä ohjelmisto aina, kun haluat olla vuorovaikutuksessa wallet:n kanssa;
- Vaihtoehtoisesti voit tuoda olemassa olevan Ashigaru wallet:n suoraan puhelimestasi Ashigaru Terminaliin. Tämän menetelmän haittapuolena on, että se heikentää hieman asetuksesi turvallisuutta, koska wallet on tällöin alttiina kahdelle riskialttiille ympäristölle yhden sijasta. Toisaalta sen etuna on se, että voit jättää Ashigaru Terminalin jatkuvasti toimimaan sekoittaaksesi kolikkojasi ja voit käyttää ne etänä Ashigaru-mobiilisovelluksen kautta.



Tässä opetusohjelmassa valitsemme toisen menetelmän. Jos kuitenkin haluat luoda kokonaan uuden portfolion, menettely on sama: ainoa ero on luomisvaiheessa, jolloin sinun on tallennettava uusi muistilauseke ja uusi passphrase.



Huomaa myös, että Ashigaru Terminal ei mahdollista bitcoinien suoraa käyttämistä. Voit joko synkronoida saman lompakon Ashigaru Terminalissa ja Ashigaru-sovelluksessa (mikä tehdään tässä oppaassa) tai Sparrow Walletissa.



Jos sinulla ei vielä ole wallet:tä Ashigaru-sovelluksessa, voit seurata tätä varten laadittua ohjetta:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Siirry Lompakot-valikkoon.



![Image](assets/fr/15.webp)



Valitse sitten `Luo / palauta wallet...`. Valinnalla `Open Wallet...` voit käyttää Ashigaru Terminaliin jo tallennettua portfoliota myöhemmin.



![Image](assets/fr/16.webp)



Anna salkullesi nimi.



![Image](assets/fr/17.webp)



Valitse sitten salkkutyyppi "Hot Wallet".






![Image](assets/fr/18.webp)



Tässä vaiheessa menettely vaihtelee alkuperäisen valintasi mukaan:




- Jos haluat luoda uuden salkun tyhjästä, napsauta `<Generate New Wallet>>, määrittele passphrase BIP39 ja tallenna sitten huolellisesti muistilauseesi ja passphrase fyysiselle tietovälineelle;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Jos haluat käyttää samaa wallet:tä kuin Ashigaru-sovelluksesi, syötä muistisanan 12 sanaa ja passphrase BIP39 suoraan vastaaviin kenttiin. Kirjoita sanat pienaakkosin, kokonaisina, järjestyksessä, välilyönnillä erotettuina, ilman numeroita tai ylimääräisiä merkkejä.



Kun tämä vaihe on valmis, napsauta `< Next >`.



*Huomautus*: Jos et voi napsauttaa tätä painiketta, muistilausekkeesi on virheellinen. Tarkista huolellisesti, ettei yksikään sana ole virheellinen tai väärin kirjoitettu.



![Image](assets/fr/19.webp)



Tämän jälkeen sinun on asetettava salasana. Tätä käytetään Ashigaru Terminal wallet:n lukituksen avaamiseen ja sen suojaamiseen luvattomalta fyysiseltä käytöltä. Se ei osallistu avaimesi kryptografiseen johtamiseen: toisin sanoen, vaikka salasanaa ei olisi, kuka tahansa, jolla on muistilausekkeesi ja passphrase, pystyy palauttamaan wallet:n ja käyttämään bitcoinisi.



Valitse pitkä, monimutkainen ja satunnainen salasana. Säilytä kopio turvallisessa paikassa: mieluiten fyysisellä tietovälineellä tai turvallisessa salasanahallintaohjelmassa.



Napsauta `< OK >`, kun olet valmis.



![Image](assets/fr/20.webp)



## 5. Salkun käyttäminen



Voit sitten valita, mitä tiliä haluat käyttää. Tällä hetkellä emme ole aloittaneet mitään sekoituksia, joten käytämme Talletus-tiliä.



![Image](assets/fr/21.webp)



Toiminta on tällöin identtistä Sparrow:n toiminnan kanssa, koska Ashigaru-terminaali on Sparrow-palvelimen fork. Löydät samat valikot:



![Image](assets/fr/22.webp)





- tapahtumat": voit tarkastella tähän tiliin liittyvien tapahtumien historiaa. Minun tapauksessani osa niistä on jo näkyvissä, koska olin tehnyt niitä Ashigaru-sovelluksella samalla wallet:llä.



![Image](assets/fr/23.webp)





- receive`: luo uuden, tyhjän kuittiosoitteen, jonka avulla satss asetetaan talletustilille.



![Image](assets/fr/24.webp)





- addresses`: näyttää luettelon kaikista osoitteistasi, riippumatta siitä, kuuluvatko ne tilisi sisäiseen vai ulkoiseen ketjuun.



![Image](assets/fr/25.webp)





- `UTXOs`: listaa kaikki käytettävissä olevat UTXO:t.



![Image](assets/fr/26.webp)





- `Settings`: antaa pääsyn salkun *kuvaajaan*. Voit myös tutustua seed:een, säätää *Gap Limit*:iä tai muuttaa salkkusi luontipäivämäärää.



![Image](assets/fr/27.webp)



Nyt tiedät, kuinka Ashigaru Terminal asennetaan ja otetaan käyttöön. Seuraavassa oppaassa näemme, kuinka tehdä coinjoineja tällä ohjelmistolla ja hallita varoja "*Postmix*"-tilassa.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
