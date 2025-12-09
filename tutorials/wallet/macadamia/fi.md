---
name: Macadamia Wallet
description: Cashu mobiili wallet anonyymeihin ja välittömiin BTC-maksuihin
---

![cover](assets/cover.webp)



Macadamia Wallet on iOS-mobiilikäyttöön tarkoitettu wallet, joka toteuttaa Cashu-protokollan, Chaumian ecash-järjestelmän, joka mahdollistaa täysin anonyymit Bitcoin-maksut. Sokeiden allekirjoitusten ansiosta kukaan tarkkailija ei voi yhdistää talletuksiasi ja rahankäyttöäsi, joten luottamuksellisuus on samanlainen kuin fyysisen käteisen rahan kohdalla.



Tässä opetusohjelmassa katsomme, miten Macadamia asennetaan ja konfiguroidaan, suoritetaan ensimmäiset Cashu-transaktiot (Mint, Send, Receive, Melt) ja hallitaan useita minttuja varojen turvaamiseksi.



## Mikä on Macadamia Wallet?



### Cashun protokolla



Cashu käyttää David Chaumin keksimää sokeaa allekirjoitusta: talletat bitcoineja "minttupalvelimelle", joka laskee liikkeelle vastaavia rahakkeita satoshina. Rahapaja allekirjoittaa nämä rahakkeet näkemättä niiden sisältöä, joten token:ää ei voida yhdistää käyttäjään. Vaihdot ovat off-chain, vertaisverkkopohjaisia ja täysin läpinäkymättömiä - edes rahapaja ei voi seurata, kuka maksaa kenellekin.



Macadamia on avoimen lähdekoodin wallet iOS, joka on kehitetty Swift/SwiftUI:lla. Se toimii ilman tiliä tai KYC:tä, tunnisteesi tallennetaan paikallisesti ja suojataan seed-lauseella. Koodi on auditoitavissa GitHubissa, ja tokenit ovat yhteentoimivia muiden Cashu-lompakoiden kanssa (Minibits, Cashu.me).



### Säilytysmalli ja kompromissi



**Tärkeää**: Cashu toimii huoltajamallilla. Merkit ovat maksulupauksia (IOU), joiden vakuutena ovat rahapajan Bitcoin-reservit. Jos rahapaja katoaa, rahakkeesi menettävät arvonsa. Tämä on kompromissi maksimaalisen luottamuksellisuuden saavuttamiseksi.



Käytä Macadamiaa fyysisenä wallet: vain pieniä määriä. Hajauta varojasi useisiin minttuihin riskin laimentamiseksi.



## Tärkeimmät ominaisuudet



Macadamia toteuttaa Cashu-protokollan neljä perustoimintoa. **Mint** muuntaa satoshisi rahakkeiksi Lightning-laskun kautta. **Send** avulla voit lähettää tokeneita ilmaiseksi QR-koodin tai linkin kautta, täysin off-chain. **Vastaanottaa** voit vastaanottaa rahakkeita tai generate Lightning-laskun. **Sulatus** maksaa salamalaskun tuhoamalla rahakkeesi.



wallet tukee useiden miinojen samanaikaista hallintaa. Voit vaihtaa rahakkeita eri rahapajojen välillä Lightningin kautta.



## Tuetut alustat



Macadamia on saatavilla vain iOS 17:ssä tai uudemmassa iPhonessa ja iPadissa. Natiivi Swift/SwiftUI-sovellus tarjoaa optimaalisen integraation Applen ekosysteemiin.



Cashu-protokolla takaa lompakoiden välisen yhteentoimivuuden. Voit palauttaa seed-lauseesi muissa sovelluksissa, kuten Minibitsissä Androidissa tai Nutstashissa työpöydällä.



Nykyinen versio jaetaan TestFlightin kautta. Käytä vain pieniä määriä tämän beta-version kanssa.



## Asennus



Macadamia on tällä hetkellä saatavilla TestFlightin, Applen beta-testausohjelman, kautta. Näin se asennetaan:



### Asennus TestFlightin kautta



**Vaihe 1: Lataa TestFlight**



Jos sinulla ei vielä ole TestFlight-sovellusta laitteessasi, etsi "TestFlight" App Storesta ja asenna se. TestFlight on Applen virallinen sovellus iOS-sovellusten beta-versioiden testaamiseen.



**Vaihe 2: Liity Macadamia-betaohjelmaan** (ranskaksi)



Kun TestFlight on asennettu, seuraa tätä kutsulinkkiä iPhonesta tai iPadista: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Linkki avaa automaattisesti TestFlightin ja tarjoaa sinulle mahdollisuuden asentaa Macadamia Wallet. Kosketa "Hyväksy" ja sitten "Asenna" aloittaaksesi latauksen. Sovellus painaa noin kymmenen megatavua ja sen asentaminen kestää vain muutaman sekunnin.



![Installation TestFlight](assets/fr/01.webp)



### Tärkeää tietoa beta-versioista



Macadamia on edelleen aktiivisessa kehitysvaiheessa. TestFlight-versioita päivitetään usein, ja ne saattavat sisältää uusia ominaisuuksia tai korjata virheitä. Kuten missä tahansa beta-versiossa, toimintahäiriöitä voi kuitenkin esiintyä. **Suosittelemme vahvasti, että käytät vain pieniä määriä**, jotka hyväksyt, että ne voivat hävitä teknisen ongelman sattuessa.



Macadamia ei kerää käyttäjätietoja näytetyn tietosuojakäytännön mukaisesti. Varmista asennuksen yhteydessä, että kehittäjä on cypherbase UG.



## Alkuperäinen konfigurointi



Ensimmäisellä käynnistyskerralla Macadamia luo BIP-39-lauseen, jossa on 12 sanaa. Kirjoita ne ylös turvalliseen paikkaan - älä koskaan kuvakaappauksena. Näiden sanojen avulla voit luoda wallet:n uudelleen ja käyttää polettejasi.



![Configuration initiale](assets/fr/02.webp)



Seuraa neljää vaihetta: tervetuloa, hyväksy ehdot, tallenna seed-lause ja lopullinen vahvistus.



![Interface principale](assets/fr/03.webp)



Kun konfigurointi on valmis, Macadamia näyttää kolme päävälilehteä. **Wallet** näyttää saldon ja tapahtumahistorian. **Mints** avulla voit hallita Cashu-palvelimia. **Asetukset** antaa pääsyn asetuksiin ja seed-lauseeseesi.



![Ajout d'un mint](assets/fr/04.webp)



Nyt sinun on määritettävä minttu eli Cashu-palvelin, joka antaa tunnukset. Siirry "Mints"-välilehdelle, napauta "Add new Mint URL" ja syötä valitsemasi mintin osoite (esim. mint.cubabitcoin.org). Tarkista bitcoinmints.com tai cashu.space hyvämaineisten julkisten minttujen osalta. Vahvista vain sellaiset rahapajat, joiden maineen olet tarkistanut, sillä ne pitävät huolta satoshistasi.



## Päivittäinen käyttö



### Uusien rahakkeiden luominen (Mint)



Jos haluat syöttää wallet Macadamia -laitteellesi ecashia, sinun on suoritettava "Mint"-operaatio (luodaksesi rahakkeita). Kosketa "Vastaanota" ja valitse sitten "Salama"-vaihtoehto. Syötä haluamasi määrä (esim. 1000 sats), valitse käytettävä minttukone ja valitse sitten generate Lightning-lasku.



![Opération Mint](assets/fr/05.webp)



Maksa Lightning-lasku tavallisella wallet:lla (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu-kyltit näkyvät heti saldossasi maksun jälkeen.



### Lähetä merkkejä



Jos haluat lähettää Cashu-kuponkeja toiselle käyttäjälle, kosketa päänäytön "Lähetä"-painiketta ja valitse sitten "Ecash". Kirjoita lähetettävä summa (esim. 50 sats) ja lisää tarvittaessa kuvaava muistio.



![Envoi Ecash](assets/fr/07.webp)



Jaa QR-koodi tai luotu teksti iMessagen, Signalin tai Telegramin kautta. Vastaanottaja lunastaa varat välittömästi ja maksutta.



### Vastaanottaa poletteja



Jos haluat vastaanottaa toisen käyttäjän lähettämiä Cashu-tunnuksia, kosketa "Vastaanota" ja valitse sitten "Ecash". Skannaa token QR-koodi tai liitä saamasi token-linkki.



![Réception Ecash](assets/fr/08.webp)



Kosketa "Redeem" saadaksesi token.



### Salama (sulaa) maksut



Jos haluat maksaa Lightning-laskun Cashu-tunnuksillasi, kosketa "Lähetä" ja valitse sitten "Lightning". Liitä BOLT11-lasku, jonka haluat maksaa.



![Paiement Lightning](assets/fr/11.webp)



Rahapaja tuhoaa rahakkeesi ja suorittaa Lightning-maksun. Voit siis maksaa mistä tahansa Lightning-palvelusta säilyttäen samalla anonymiteettisi.



### Vaihda minttujen välillä



Kun saat rahapajakkeita rahapajalta, jota et ole määrittänyt, Macadamia tarjoaa useita vaihtoehtoja näiden rahakkeiden hallintaan.



![Swap inter-mints](assets/fr/09.webp)



Lisää uusi rahapaja tai vaihda merkit olemassa olevaan rahapajaan. Vaihdossa käytetään Lightningia siltana, jonka kautta voit siirtää varoja nimettömästi.



### Edistyksellinen moniminttien hallinta



Macadamia tarjoaa kehittyneitä työkaluja useiden minttujen samanaikaiseen hallintaan ja varojen strategiseen kohdentamiseen.



![Gestion multi-mints](assets/fr/10.webp)



"Jaa varat" jakaa saldosi automaattisesti prosentuaalisesti (esim. 50/50). "Transfer" mahdollistaa manuaaliset siirrot rahapajojen välillä riskien hajauttamiseksi.



## Edut ja rajoitukset



**Highlights** :





- Suurin mahdollinen luottamuksellisuus**: Tapahtumia ei voida jäljittää, edes rahapajan toimesta. Ei lohkoketjun metatietoja, jäljittämätön vertaisvertaisvaihto.
- Nopea ja ilmainen**: Maksuttomat pikasiirrot minttitilin sisällä, ihanteellinen mikromaksuille.
- Yhteentoimivuus**: standardoidut Cashu-tunnukset käytettäväksi muiden yhteensopivien lompakoiden kanssa (Minibits, Nutstash).
- Yksinkertaisuus**: Interface iOS-natiivi on aloittelijoidenkin käytettävissä, mutta samalla se on tarkastettavissa (avoin lähdekoodi).



**Orajoitukset** :





- Säilytysmalli**: tarvitaan minttusijoitus. Jos rahapaja katoaa, rahakkeesi menettävät arvonsa.
- vain iOS**: Ei Android/desktop-versiota. Cashun yhteentoimivuus mahdollistaa käytön muiden lompakoiden kautta, mutta optimaalinen kokemus on edelleen iOS.
- Minttu riippuvuus**: Mint offline = ei pysty suorittamaan liiketoimia, jotka vaativat sen toimintaa (Mint, Melt).
- Kehittyvä teknologia** : Aktiivinen kehitys, mahdolliset virheet, kehittyvät standardit.



## Parhaat käytännöt





- Monipuolistakaa minttupakkauksia**: Hajauta pelimerkkisi useisiin hyvämaineisiin rahapajoihin riskin laimentamiseksi.
- Rajoitusmäärät**: Käytä Macadamiaa fyysisenä wallet:na päivittäisiä maksuja varten, ei kassakaappina.
- Varmista seed**: Säilytä 12-sanainen lauseesi paperilla turvallisessa paikassa. Testaa palauttamista silloin tällöin.
- Tarkista minttupalat**: Cashu.space ja yhteisön foorumit ennen minttujen lisäämistä. Valitse ne, joilla on hyvä käytettävyys ja hyvä maine.
- VPN tai Tor**: Piilota IP-osoitteesi VPN:n tai Torin avulla maksimoidaksesi verkon yksityisyyden.
- Liity yhteisöön**: Telegram/Discord Cashu -ryhmiin, joissa saat päivityksiä, mintasuosituksia ja parhaita käytäntöjä.



## Päätelmä



Macadamia Wallet tuo fyysisen rahan ominaisuudet digitaaliseen Bitcoin:een. Yhdistämällä Chaum- ja Lightning-sokosignaatiot se tarjoaa tyylikkään ratkaisun transaktioiden luottamuksellisuuteen. Sen natiivin iOS-käyttöliittymän ansiosta kehittynyt salaustekniikka on käytettävissä, mutta se on samalla avointa lähdekoodia ja yhteentoimiva Cashu-ekosysteemin kanssa.



Säilytysmalli edellyttää valppautta ja hyviä turvallisuuskäytäntöjä. Oikein käytettynä Macadamia on korvaamaton väline anonymiteettiä vaativiin jokapäiväisiin maksuihin, ja se täydentää muita kuin säilytyslompakoita säästöihin.



## Resurssit



### Viralliset asiakirjat




- Virallinen verkkosivusto: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub-lähdekoodi: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashun dokumentaatio




- Tekninen dokumentaatio: [docs.cashu.space](https://docs.cashu.space)
- Luettelo julkisista rahapajoista: [bitcoinmints.com](https://bitcoinmints.com)
- Virallinen protokollasivusto: [cashu.space](https://cashu.space)



### Yhteisö




- Telegram Cashu ryhmä: [t.me/cashu_ecash](https://t.me/cashu_ecash)