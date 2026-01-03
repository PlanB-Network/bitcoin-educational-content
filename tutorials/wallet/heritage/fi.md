---
name: Heritage
description: Bitcoin-salkku, jossa on integroitu periytymismekanismi Taproot-skriptien kautta
---

![cover](assets/cover.webp)



Bitcoinien siirtäminen eteenpäin kuoleman tai työkyvyttömyyden yhteydessä on suuri haaste kaikille kryptovarallisuuden haltijoille. Ilman sopivaa perintösuunnitelmaa nämä varat jäävät perimättä omaisilta.



Heritage tarjoaa tyylikkään vastauksen toteuttamalla dead-man switch -mekanismin suoraan Bitcoin-lohkoketjuun. Tämä avoimen lähdekoodin wallet mahdollistaa on-chain:n perintöehtojen määrittämisen: jos omistaja ei tee enää transaktioita tiettyyn ajanjaksoon, ennalta määritellyt vaihtoehtoiset avaimet voivat vapauttaa varat.



## Mitä on perintö?



Heritage on Bitcoin-salkku, johon on natiivisti integroitu periytymismekanismi Taproot-skriptien avulla. Jérémie Rodonin MIT-lisenssillä kehittämä avoimen lähdekoodin ohjelmisto takaa avoimuuden ja kestävyyden.



Heritage käyttää Taproot-skriptejä, jotka on koodattu Bitcoin-osoitteilla. Kukin UTXO sisältää kahdenlaisia menoehtoja:





- Ensisijainen polku** : Omistaja voi käyttää bitcoinejaan milloin tahansa ensisijaisella avaimellaan
- Vaihtoehtoiset polut**: Jokaisen nimetyn perillisen kohdalla käsikirjoitus yhdistää sen julkisen avaimen ja aikalukon..



Jokainen omistajatapahtuma lykkää automaattisesti perintölausekkeiden aktivointipäivää. Pitkittyneen toimimattomuuden (kuolema, työkyvyttömyys) tapauksessa ehdot aktivoituvat automaattisesti.



## Perintöpalvelu (valinnainen)



Heritage tarjoaa kaksi käyttövaihtoehtoa:



** Tee se itse (ilmaiseksi)**: Avoimen lähdekoodin sovellus yksin. Hallitset kaikkea itsenäisesti omalla solmulla. Tämä vaihtoehto tarjoaa sisäänrakennetun varmuuskopiointikäytön, sisäänrakennetun perinnön ja yksinoikeuden hallita bitcoinejasi. Sinun on kuitenkin luotava omat hälytykset (kalenteri, muistutukset), jotta et unohda uudistaa timelockiasi, eikä perillisille ole automaattisia ilmoituksia.



**Käytä palvelua (0,05 % vuodessa)** : Btc-heritage.com-palvelu lisää ominaisuuksia, jotka yksinkertaistavat hallintaa:




- Automaattiset muistutukset ennen määräaikojen päättymistä
- Automaattiset ilmoitukset perillisille elvytysprosessin ohjaamiseksi
- Ensisijainen tuki
- Yksinkertaistettu kuvaajien hallinta



Palkkio: 0,05 % hallinnoidusta summasta vuodessa, vähintään 0,5 mBTC/vuosi. Ensimmäinen vuosi ilmainen.



Palvelu ei ole säilytyspalvelu: yksityiset avaimesi eivät koskaan poistu laitteestasi. Heritage ei pääse käsiksi varoihisi.



## Heritage CLI



Edistyneille käyttäjille, jotka haluavat käyttää päätelaitetta, Heritage tarjoaa komentorivityökalun (CLI) rakeista ohjausta ja koneen toimintaa ilmavälien avulla.



![Page Heritage CLI](assets/fr/03.webp)



Täydellinen CLI-dokumentaatio on saatavilla osoitteessa [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Täältä löydät ohjeet lataamiseen, palveluun yhdistämiseen, lompakoiden luomiseen (Ledger:lla tai paikallisilla avaimilla), perillisten ja transaktioiden hallintaan.



Tässä oppaassa keskitytään työpöytäsovellukseen, joka on helpommin useimpien käyttäjien käytettävissä.



## Heritage Desktop



Heritage Desktop on graafinen sovellus, jonka intuitiivinen käyttöliittymä opastaa käyttäjää konfigurointiprosessin kaikissa vaiheissa.



### Lataa



Mene osoitteeseen [btc-heritage.com](https://btc-heritage.com) ja klikkaa "Lataa sovellus".



![Page d'accueil Heritage](assets/fr/01.webp)



Valitse käyttöjärjestelmääsi vastaava versio (Linux 64bits tai Windows 64bits). Binäärejä ei ole allekirjoitettu digitaalisesti, mikä voi aiheuttaa turvallisuusvaroituksia.



![Page de téléchargement](assets/fr/02.webp)



### Asennus Linuxiin



Linuxissa sovellus jaetaan AppImage-muodossa. Ennen kuin voit käyttää sitä, sinun on asennettava `libfuse2`-riippuvuus:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Tee sitten tiedostosta suoritettava ja suorita se:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Ensimmäinen laukaisu



Ensimmäisellä käynnistyskerralla ohjatun käyttöönoton aikana saat kolme vaihtoehtoa:



![Onboarding initial](assets/fr/05.webp)





- Aseta Heritage Wallet**: Luo uusi wallet, jossa on kulttuuriperintösuunnitelma
- Periä bitcoineja**: Ota bitcoinit takaisin perijänä
- Tutki itse**: Tutustu toimintoihin ilman apua



Valitse "Setup an Heritage Wallet" luodaksesi ensimmäisen wallet:n.



### Bitcoin verkkoyhteys



Valitse, miten yhteys Bitcoin-verkkoon muodostetaan:



![Choix connexion](assets/fr/06.webp)





- Heritage-palvelun käyttäminen**: Hallittu infrastruktuuri, yksinkertaisempi perillisille
- Käytän omaa solmua**: Yhdistä omaan Bitcoin Core- tai Electrum-solmuun



Tässä ohjeessa käytämme omaa solmua.



### Yksityisen avaimen hallinta



Valitse, miten yksityisiä avaimia hallitaan:



![Gestion des clés](assets/fr/07.webp)





- Ledger-laitteiston kanssa** : Maksimaalinen turvallisuus wallet-laitteiston kanssa (suositellaan)
- Paikallinen tallennus salasanalla**: Paikallisesti tallennetut avaimet salasanasuojauksella
- Olemassa olevan wallet:n palauttaminen** : Palauta olemassa oleva seed



### Solmun konfigurointi



Jos käytät omaa solmua, sovellus opastaa sinua sen määrityksessä. Varmista, että Bitcoin- tai Electrum-solmusi on :




- Asennettu ja käynnissä
- Synkronoitu Bitcoin-verkon kanssa
- Määritetty hyväksymään RPC-yhteydet (Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Napsauta "Bitcoin-solmuni on toiminnassa", kun solmusi on valmis.



### Tilapaneeli



Napsauta oikeassa yläkulmassa olevaa "Status"-painiketta ja sitten "Open Configuration" (Avaa konfiguraatio) päästäksesi yhteysparametreihin.



![Panneau Status](assets/fr/09.webp)



Aseta Electrum-palvelimesi URL-osoite (esim. `umbrel.local:50001`, jos käytät Umbrel:a).



![Configuration Electrum](assets/fr/10.webp)



### wallet:n luominen



Kun yhteys on muodostettu, napsauta WALLETS-välilehdellä "Create Wallet".



![Créer wallet](assets/fr/11.webp)



Ponnahdusikkuna selittää Heritage-ohjelman jaetun arkkitehtuurin:



![Architecture split](assets/fr/12.webp)



1. **Key Provider (Offline)**: Hallinnoi yksityisiä avaimiasi ja allekirjoittaa tapahtumia. Voi olla Ledger- tai wallet-ohjelmisto.


2. **Online Wallet**: Käsittelee synkronoinnin Bitcoin-verkon kanssa, osoitteiden luomisen ja tapahtumien lähettämisen.



Täytä luomislomake :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Nimi**: Yksilöllinen nimi wallet:n tunnistamiseksi
- Avaintoimittaja**: Valitse tätä opetusohjelmaa varten Local Key Storage
- Uusi/uudistettu**: Valitse "Uusi", jos haluat luoda uuden generate:n seed:n
- Sanamäärä**: 24 sanaa suositellaan maksimaalisen turvallisuuden takaamiseksi



Anna vahva salasana ja valitse vaihtoehdot Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Paikallinen solmu**: Käyttää omaa Electrum- tai Bitcoin-ydinsolmua
- Perintöpalvelu**: Käyttää Heritage-palvelua (suositellaan ilmoitustoimintoja varten)



Klikkaa "Create Wallet" viimeistelläksesi luomisen.



### Interface alkaen wallet



wallet on nyt luotu. Käyttöliittymä näyttää :



![Interface wallet](assets/fr/15.webp)





- Balance
- SEND- ja RECEIVE-painikkeet
- Tapahtumahistoria
- Perinnekonfiguraation historia
- wallet-osoitteet



### Perillisten luominen



Siirry "PERILLISET"-välilehdelle luodaksesi perilliset.



![Page Heirs](assets/fr/16.webp)



Ponnahdusikkunassa kerrotaan:




- Perilliset ovat Bitcoin:n julkisia avaimia, jotka liittyvät yksilöihin
- Jokaisella perillisellä on oma muistisääntö
- Ensimmäisen perijän pitäisi olla "varmuuskopio" itsellesi (siltä varalta, että wallet menetetään)



#### Varmuuskopion perillisen luominen



Napsauta "Luo perillinen" ja nimeä se "Varmuuskopio".



![Création héritier Backup](assets/fr/17.webp)



Ponnahdusikkunassa selitetään, miksi 12-sanainen lause ilman passphrase:ää on turvallinen perillisille:


1. **Ei välitöntä pääsyä**: Perijäavaimet eivät voi käyttää varoja ennen kuin aikarajoitus on päättynyt


2. **Poikkeamien havaitseminen**: Jos joku pääsee käsiksi lauseeseen, voit päivittää Heritage-konfiguraation


3. **Pitkän aikavälin saavutettavuus**: passphrase voi unohtua vuosien kuluttua



Määritä perillinen :



![Configuration héritier](assets/fr/18.webp)





- Avaintarjoaja** : Paikallinen avainvarasto
- Uusi**: Luo uusi seed
- Sanamäärä**: 12 sanaa



Viimeistele luominen :



![Finalisation héritier](assets/fr/19.webp)





- Perillisen tyyppi**: Laajennettu julkinen avain
- Vie palveluun**: Valinnainen, mahdollistaa automaattisen ilmoituksen perillisille



Varmuuskopiointiperillinen on nyt luotu:



![Héritier créé](assets/fr/20.webp)



#### Perillisen muistisanan tallentaminen



Napsauta varmuuskopiointiperää ja sitten "Näytä Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**TÄRKEÄÄ: Kirjoita nämä 12 sanaa muistiin ja säilytä ne turvallisessa paikassa. Tämä on avain varojen takaisin saamiseen.



![Phrase mnémotechnique](assets/fr/22.webp)



#### seed:n poistaminen sovelluksesta



Kun olet kirjoittanut lauseen muistiin, siirry perintöparametreihin (hammasrataskuvake):



![Paramètres héritier](assets/fr/23.webp)



Poista yksityinen avain sovelluksesta "Strip Heir Seed" -toiminnolla. Vahvista, että olet tallentanut lauseen.



![Strip Heir Seed](assets/fr/24.webp)



Tämä on turvatoimenpide: vain julkinen avain jää sovellukseen, mikä riittää perinnöllisyyden määrittämiseen.



#### Toisen perillisen luominen



Toista prosessi luodaksesi toisen perillisen (esim. "Satoshi"). Sinulla on nyt kaksi perillistä:



![Deux héritiers](assets/fr/25.webp)





- Varmuuskopiointi**: Henkilökohtainen hätäavain
- Satoshi**: Nimetty perillinen



### Heritage-kokoonpano



Palaa wallet:een ja napsauta Asetukset-kuvaketta:



![Paramètres wallet](assets/fr/26.webp)



Napsauta "Heritage Configuration" -osiossa "Create" (Luo):



![Heritage Configuration](assets/fr/27.webp)



Aseta aikarajat kullekin perijälle:



![Configuration délais](assets/fr/28.webp)





- Varmuuskopiointi**: - Eräpäivä: 2026-06-18 - Eräpäivä: 2026-06-18
- Satoshi**: - Eräpäivä: 2027-03-20



**Tärkeää**: Jokaisella perillisellä on oltava pidempi viive kuin edellisellä. Ensimmäinen perillinen (varmuuskopio) saa varat käyttöönsä ensimmäisenä.



Myös konfiguroida :



![Configuration finale](assets/fr/29.webp)





- Viitepäivä**: Läpimenoaikojen laskennan alkamispäivä
- Vähimmäismaturiteettiviive**: Vähimmäisviive tapahtuman jälkeen (suositellaan 10 päivää)



Vahvista kokoonpano napsauttamalla "Luo".



Heritage-konfiguraatio on nyt aktiivinen:



![Configuration active](assets/fr/30.webp)



Se näyttää molemmat perilliset sekä niiden määräajat ja voimassaolon päättymispäivät.



### Kuvaajien tallentaminen



**Tärkeää**: Tallenna wallet-kuvaajat. Ilman niitä, vaikka muistisääntöä käytettäisiinkin, rahastojen palauttaminen on mahdotonta.



Napsauta "Backup Descriptors" :



![Bouton Backup](assets/fr/31.webp)



Tallenna Bitcoin-kuvaajat sisältävä JSON-tiedosto:



![Backup descripteurs](assets/fr/32.webp)



Tämä tiedosto on siirrettävä perillisillesi yhdessä heidän muistisääntöjensä kanssa.



### Vastaanottaa bitcoineja



Napsauta "RECEIVE" generate-vastaanotto-osoitetta:



![Recevoir bitcoins](assets/fr/33.webp)



Onnittelut! Heritage Wallet on valmis vastaanottamaan bitcoineja. Jokainen luotu osoite sisältää automaattisesti Heritage-olosuhteesi.



Saldosi päivittyy tapahtuman vastaanottamisen jälkeen:



![Solde mis à jour](assets/fr/34.webp)



Historiassa näytetään tapahtuma ja siihen liittyvä Heritage-konfiguraatio.



---

## Perillisen takaisinperintä



Kun asetettu aika on kulunut, perillinen voi vaatia varat takaisin.



### Edellytykset



Perillinen tarvitsee :


1. Hänen 12-sanainen muistisanansa


2. Alkuperäinen wallet-kuvaajan varmuuskopiotiedosto (JSON)



### Perillisen luominen Wallet



"PERINNÖT"-välilehdellä ponnahdusikkuna muistuttaa sinua näistä edellytyksistä:



![Page Heir Wallets](assets/fr/35.webp)



**Huomaa**: Ilman kuvaajan varmuuskopiotiedostoa varojen käyttö on mahdotonta, vaikka käytössä olisi oikea muistisääntö.



Napsauta "Luo perillinen Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Täytä lomake:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Perillinen Wallet Nimi**: Nimi, jolla tämä perillinen tunnistetaan wallet
- Avaintarjoaja** : Paikallinen avainvarasto
- Palauta**: Valitse tämä vaihtoehto syöttääksesi olemassa olevan lauseen



Syötä perillisen muistisääntölauseen 12 sanaa ja määritä Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Perinnön tuottaja**: "Paikallinen" käyttääksesi omaa solmua varmuuskopiotiedoston kanssa



Lataa JSON-varmuuskopiotiedosto ja napsauta "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Perillinen Wallet



Perijä Wallet on luotu. Jos aikarajoitus ei ole vielä päättynyt, perintö ei ole aluksi käytettävissä:



![Pas d'héritage disponible](assets/fr/40.webp)



Kun viive on kulunut ja varat on synkronoitu Bitcoin-verkon kanssa, ne näkyvät perintöluettelossa:



![Héritage disponible](assets/fr/41.webp)



Käyttöliittymässä näkyy :




- Avaintyyppi ja sormenjälki
- Perinnölliset varat yhteensä
- Nykyinen käyttökelpoinen määrä (0 sat, jos aikarajoitus ei ole vielä päättynyt)
- Erääntymis- ja voimassaolopäivät



Kun eräpäivä on saavutettu, "Spend"-painike siirtää bitcoinit henkilökohtaiseen wallet:ään.



---

## Parhaat käytännöt



### Kuvaajien tallentaminen



wallet-kuvaajat ovat välttämättömiä perintöosoitteiden rekonstruoimiseksi. ** Ilman kuvaajia et pysty löytämään rahastojasi edes muistisäännön avulla.



### Avainten turvallisuus





- Käytä Ledger:ää pääavaimena, jos mahdollista
- Älä koskaan säilytä perillisten tuomioita samassa paikassa kuin omia tuomioitasi
- Tiedon levittäminen useissa tiedotusvälineissä ja paikoissa



### Dokumentaatio läheisiäsi varten



Kirjoita selkeät ohjeet, joissa selitetään jokainen palautusprosessin vaihe. Perillisesi eivät ehkä tunne Bitcoin:tä kriittisellä hetkellä.



## Vaihtoehdot



Bitcoineidesi siirtoa varten on olemassa muitakin ratkaisuja, kuten Liana ja Bitcoin Keeper. Löydät opetusohjelmamme alta:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Päätelmä



Heritage antaa sinulle mahdollisuuden suunnitella Bitcoin:n perintöjä suvereenisti työpöytäsovelluksen avulla. Toteutus edellyttää harkittua harkintaa sopivista aikatauluista ja salaisuuksien turvaamisesta. Älä unohda siirtää perillisiäsi:




- Heidän 12-sanainen muistisanansa
- Kuvaajan varmuuskopiotiedosto
- Elvytysohjeet



## Resurssit





- [Perinnön virallinen verkkosivusto](https://btc-heritage.com)
- [Dokumentaatio CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)