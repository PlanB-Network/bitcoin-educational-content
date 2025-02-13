---
name: Bisq 2
description: Täydellinen opas Bisq 2:n käyttöön ja bitcoinien P2P-vaihtoon
---
![cover](assets/cover.webp)

## Johdanto

KYC-vapaat P2P-pörssit ovat olennaisen tärkeitä käyttäjien luottamuksellisuuden ja taloudellisen riippumattomuuden säilyttämiseksi. Ne mahdollistavat suorat transaktiot yksityishenkilöiden välillä ilman henkilöllisyyden todentamista, mikä on ratkaisevan tärkeää yksityisyyttä arvostaville. Jos haluat syvällisemmän käsityksen teoreettisista käsitteistä, tutustu BTC204-kurssiin:

https://planb.network/courses/btc204
### Mikä on Bisq 2?

Bisq 2 on uusi versio suositusta hajautetusta Bisq-pörssistä, joka julkaistiin vuonna 2024. Toisin kuin edeltäjänsä, Bisq 2 on kehitetty tukemaan useita vaihtoprotokollia, mikä tarjoaa käyttäjille enemmän joustavuutta.

**Keskeiset uudet ominaisuudet:**


- Tuki useille yksityisyysverkostoille (Tor, I2P)
- Useita identiteettejä luottamuksellisuuden lisäämiseksi
- REST API kaupankäynnin botteja varten
- Tuki useille salkkutyypeille
- Roolijärjestelmä, jossa on pakollinen talletus BSQ:ssa

Tämä opas keskittyy yksinomaan Bisq Easy -protokollaan, joka on tällä hetkellä ainoa saatavilla oleva protokolla. Bisq Easy on suunniteltu erityisesti uusille Bitcoin-käyttäjille. Tämän protokollan avulla käyttäjät voivat ostaa ja myydä Bitcoineja fiat-valuuttoja vastaan hajautetulla vertaisverkkopalvelualustalla. Transaktiot on rajoitettu 600 USD:n vasta-arvoon (minimi 6 USD), ja vaihdon turvallisuus perustuu BTC-myyjien maineeseen. Bisq Easyllä ei ole kaupankäyntimaksuja eikä vakuustalletusvaatimuksia. Bisq Easy korvaa Bisq 1:n alle 600 USD:n (tai vastaavan summan) käteisvaihtojen osalta.

**Pääominaisuudet:**


- Rajat ylittävä työpöytäsovellus
- Käytettävissä useita vaihtoprotokollia
- Hajautettu P2P-verkko
- Keskittyminen luottamuksellisuuteen (ei KYC:tä, Torin käyttö)
- Ei-puolustajuus (säilytät varojen hallinnan)
- Avoin lähdekoodi (AGPL)

### Erot Bisq 1:een verrattuna

**Ostajille:**


- Vakuutta ei vaadita
- Ei kaupankäyntimaksuja
- Ei kaivosmaksuja
- Myyjän maineeseen perustuva turvallisuus
- Alemmat kaupankäyntilimiitit (vastaavat 600 USD)

**Myyjille:**


- Vakuutta ei vaadita
- Maineen rakentaminen
- Mahdollisuus polttaa BSQ:ta tai luoda BSQ-sidoksia
- Mahdollisesti korkeampi myyntipalkkio (10-15 % markkinoita korkeampi)

**Tärkeä huomautus:** Kun Bisq Multisig -protokolla on otettu käyttöön Bisq 2:ssa, Bisqin vanha versio voidaan poistaa käytöstä. Bisq 1:tä käytetään kuitenkin jatkossakin Bisq CAD:n ja BSQ-BTC-pörssien hallintatyökaluna.

### Vaihtoprosessi


- Tarjouksen tekijä määrittelee vaihdon ehdot
- Kun kauppiaat ovat sopineet ehdoista (maksutapa ja hinta), vaihto alkaa
- Myyjä lähettää pankkitietonsa ostajalle, ja ostaja lähettää Bitcoin-osoitteensa myyjälle
- Ostaja suorittaa maksun käteisellä ja ilmoittaa siitä myyjälle
- Kun maksu on vastaanotettu, myyjä lähettää bitcoinit ostajan osoitteeseen
- Vaihto on valmis, kun ostaja vastaanottaa bitcoinit

### Tärkeitä sääntöjä


- Ennen maksutietojen vaihtoa vaihto voidaan peruuttaa ilman perusteluja
- Kun yksityiskohdat on vaihdettu, velvoitteiden laiminlyönti voi johtaa karkotukseen
- Kun kyseessä on pankkisiirto, ** älä koskaan käytä maksun perusteena termejä "Bisq" tai "Bitcoin "** (tämä voi johtaa varojen jäädyttämiseen tai jopa siihen, että vastaanottajan tai maksajan pankkitili jäädytetään)
- Toimijoiden on kirjauduttava sisään vähintään kerran päivässä seuratakseen prosessia
- Ongelmatilanteissa elinkeinonharjoittajat voivat turvautua sovittelijan palveluihin

## Asennus ja konfigurointi

### 1. Lataa ja tarkista Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Siirry osoitteeseen [bisq.network](https://bisq.network/downloads/)
- Lataa käyttöjärjestelmääsi vastaava Bisq 2 -versio (selaa sivua alaspäin)
- Tarkista ladatun tiedoston aitous (erittäin suositeltavaa). Yksityiskohtainen opas allekirjoituksen tarkistamisesta on seuraavassa oppaassa:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Asennus järjestelmän mukaan

Noudata käyttöjärjestelmääsi sopivia asennusvaiheita. Jos asennuksen aikana ilmenee ongelmia, voit tutustua [virallisen Bisq-wikin] (https://bisq.wiki/Downloading_and_installing) yksityiskohtaisiin ohjeisiin.

### 3. Ensimmäinen käynnistys


- Käynnistä Bisq 2 ja hyväksy käyttöehdot

![Conditions d'utilisation](assets/fr/01.webp)


- Luo uusi profiili valitsemalla nimi ja avatar

![Création du profil](assets/fr/02.webp)


- Tämän jälkeen sinut viedään sovelluksen pääkojelautaan, jossa voit käynnistää Bisq Easy -ohjelman ostaaksesi tai myydäksesi ensimmäiset bitcoinisi

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Maksutapojen määrittäminen


- Pääset maksutilit-osioon päävalikosta

![Liste des comptes de paiement](assets/fr/04.webp)


- Lisää uusi maksutapa täyttämällä tarvittavat tiedot

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Maksutapojen esiasentaminen on valinnaista, mutta suositeltavaa säästää aikaa kaupankäynnissä. Voit myös määrittää maksutavat suoraan kaupan aikana ottamalla yhteyttä vaihtokumppaniin.

### 5. Tilin turvallisuus

**Tietojen varmuuskopiointi:**

Toisin kuin Bisq 1, Bisq 2 ei tällä hetkellä integroi Bitcoin-lompakkoa: maksutapahtumat suoritetaan siis omien ulkoisten lompakoiden kautta. Suosittelemme kuitenkin, että varmuuskopioit Bisq 2:n tietokansiosi säännöllisesti. Löydät tietokansiosi [virallisesta Bisq-wikistä](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Identiteetin hallinta:**

Bisq 2:n avulla voit luoda useita identiteettejä. Jokaista identiteettiä voidaan käyttää erityyppisiin tapahtumiin. Identiteetit tallennetaan datakansioon.

## Bitcoinien ostaminen ja myyminen

### Miten ostaa Bitcoineja

**Vaihtoehto 1: Hyödynnä olemassa oleva tarjous****


- Valitse päänäytöltä "Bisq Easy", "Getting started" -välilehti ja napsauta sitten "Start trade wizard"

![Lancer trade wizard](assets/fr/06.webp)


- Valitse "Osta Bitcoin" ja valitse valuutta

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Määritä haluamasi maksutavat (SEPA, Revolut jne.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- Tässä vaiheessa sinulla on joko luettelo tarjouksista, jotka vastaavat aiempia kriteerejäsi, tai sinun on mentävä "tarjouskirjaan"

![Liste des offres](assets/fr/10.webp)


- Toisessa tapauksessa voit näyttää ja suodattaa tarjouksia käyttöliittymän oikeassa yläkulmassa olevilla painikkeilla

![Filtres des offres](assets/fr/11.webp)


- Kun olet valinnut tarjouksesi, sinun tarvitsee vain valita maksutapa ja vahvistaa kaupan yhteenveto

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Vaihtoehto 2: Luo oma tarjous**


- Valitse "Bisq Easy" ja sitten "tarjouskirja"
- Valitse kaupankäyntiparisi (esim. BTC/EUR)
- Klikkaa "Luo tarjous
- Seuraa ohjatun tarjouksen luomisen ohjattua toimintoa: Määritä määrä (kiinteä tai vaihteleva)

![Configuration du montant](assets/fr/20.webp)


- Valitse hyväksytyt maksutavat

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Tarkista yhteenveto ja julkaise tarjous

![Récapitulatif et publication](assets/fr/22.webp)

Kun vaihto on aloitettu :


- Lähetä Bitcoin-osoitteesi tai Lightning-lasku myyjälle

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Vastaanottaa myyjän pankkitiedot

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Suorita maksu (mainitsematta "Bisq" tai "Bitcoin")
- Ilmoita myyjälle maksusta

![Notification paiement](assets/fr/18.webp)


- Odota, että bitcoinit saapuvat

![Attente réception](assets/fr/19.webp)

### Miten myydä Bitcoineja?

Myyntiprosessi Bisq 2:ssa noudattaa samanlaista logiikkaa kuin ostoprosessi, ja sen päävaiheet ovat samat, mutta päinvastaisessa järjestyksessä. Voit joko luoda oman myyntitarjouksen tai vastata olemassa olevaan ostotarjoukseen. Tässä on erittely eri vaihtoehdoista ja prosessin vaiheista:

**Vaihtoehto 1: Luo myyntitarjous**


- Valitse "Bisq Easy" ja sitten "tarjouskirja"
- Napsauta "Luo tarjous" ja valitse "Myy Bitcoin"
- Määritä tarjouksesi :
 - Valitse valuutta (EUR, USD jne.)
 - Valitse hyväksytyt maksutavat
 - Määritä summa (6-600 USD)
 - Määritä hintasi (kiinteä tai % markkinoista)
- Tarkista tiedot ja julkaise tarjous

**Vaihtoehto 2: Ota vastaan olemassa oleva tarjous****


- Selaa tarjouksia "Tarjouskirja"-välilehdellä
- Suodata valuutan ja maksutavan mukaan
- Valitse sinulle sopiva tarjous
- Tarkista tiedot ja hyväksy tarjous

**Myyntiprosessi:**

Kun vaihto on aloitettu :


   - Lähetä pankkitietosi ostajalle
   - Odota ostajan Bitcoin-osoitetta
   - Tarkista, että osoite on voimassa

Maksuilmoituksen jälkeen :


   - Tarkista, että maksu on vastaanotettu tilillesi
   - Vahvista, että määrä ja tiedot täsmäävät
   - Lähetä bitcoineja annettuun osoitteeseen
   - Merkitse tapahtuma suoritetuksi

Viimeistely :


   - Odota vahvistusta ostajalta
   - Jätä palautetta tapahtumasta
   - Rakenna maineesi tulevaa myyntiä varten

**Tärkeä huomautus:** Myyjänä sinun on oltava erityisen valppaana veloitusten riskin suhteen. Suosi turvallisia maksutapoja ja tarkista aina ennen bitcoinien lähettämistä, että maksu on vastaanotettu.

## Hyvät käytännöt ja turvallisuus

### Turvallisuusvinkkejä

**Ostajille:**


- Aloita pienillä määrillä
- Tarkista myyjien maine (vähintään 30 000 pistettä)
- Käytä vain ehdotettuja maksutapoja
- Tarkista, että myyjä on aktiivinen ennen maksun lähettämistä
- Käytä vain vaihtokeskustelussa annettuja pankkitietoja
- Älä koskaan kommunikoi Bisq 2 -alustan ulkopuolella
- Säilytä maksutosite
- Älä koskaan lähetä arkaluonteisia tietoja

**Myyjille:**


- Ole varovainen uusien tilien kanssa
- Vältä maksutapoja, jotka ovat alttiita maksupalautuksille (PayPal, Venmo)
- Tarkista, että tilin tiedot vastaavat ostajan tietoja
- Rajoita viestintä chattiin Bisq 2
- Sovittelun aloittaminen epäselvissä tapauksissa

### Maineen rakentaminen (myyjille)

Parantaaksesi mainettasi myyjänä Bisqissä, tee säännöllisiä kauppoja ja pidä yllä ammattimaista viestintää ostajien kanssa. Vastaa nopeasti ostajan pyyntöihin varmistaaksesi positiivisen kokemuksen. Voit myös luoda BSQ-velkakirjan osoittaaksesi sitoutumisesi alustaan. Nämä toimet rakentavat luottamusta ja houkuttelevat lisää ostajia.

### Riitojen ratkaiseminen


- Ota yhteyttä vastapuoliisi chatin kautta
- Avaa tarvittaessa riita-asia
- Toimita kaikki pyydetyt todisteet
- Noudata sovittelijan ohjeita

### Tietosuojakäytäntö :


- Rekisteröintiä tai keskitettyä henkilöllisyyden todentamista ei tarvita
- Kaikki yhteydet kulkevat Tor-verkon (ja pian I2P:n) kautta
- Ei keskitettyä palvelinta tietojen tallentamista varten
- Transaktiotiedot ovat vain asianomaisten osapuolten luettavissa

### Suojaus sensuuria vastaan :


- Täysin hajautettu P2P-verkko
- Tor-verkon (ja pian I2P:n) käyttö sensuurin vastustamiseen
- DAO:n hallinnoima avoimen lähdekoodin hanke, jossa ei ole keskitettyä oikeushenkilöä

## Edut ja haitat

### Bisq 2:n edut


- Suurin mahdollinen luottamuksellisuus**: Ei KYC, Torin käyttö
- Hajauttaminen**: Ei keskitettyä palvelinta
- Turvallisuus**: Avoimen lähdekoodin, ei-säilyttävä koodi
- Intuitiivinen käyttöliittymä**: yksinkertaisempi kuin Bisq 1:ssä
- Joustavuus**: Useita vaihtoprotokollia

### Bisq 2:n haitat


- Rajoitettu likviditeetti** (tällä hetkellä) :
 - Uusi protokolla käynnistysvaiheessa
 - Muutamia myyntitarjouksia saatavilla
 - Mahdollisesti pitkät odotusajat ostajan löytämiseksi
- Kaupankäyntirajat**: USD 600 per transaktio (Bisq easy -palvelun kanssa)
- Vain työpöydälle**: Ei mobiilisovellusta

## Tulevat pöytäkirjat

Vaikka Bisq Easy on tällä hetkellä ainoa saatavilla oleva protokolla, useita muita protokollia on kehitteillä Bisq 2:lle:


- Bisq Lightning**: Vaihtoprotokolla, joka perustuu usean osapuolen laskentakryptografiaa käyttävään escrow-järjestelmään Lightning-verkossa.
- Bisq MuSig**: Siirtyminen pääprotokollasta Bisq 1:stä Bisq 2:een käyttäen 2 vs. 2 multisig-muuntosignaalia, jossa on vakuustalletuksia.
- BSQ Swaps**: Välittömät atomivaihdot BSQ:n ja BTC:n välillä.
- Likvidit swapit**: Varojen vaihtaminen Liquid-verkossa (USDT, BTC-L) atomisilla swapeilla.
- Moneron vaihtokaupat**: Atomivaihdot Bitcoinin ja Moneron välillä.
- Nestemäinen MuSig**: Multisig-protokollan versio, jossa käytetään L-BTC:tä alhaisempien kustannusten ja suuremman luottamuksellisuuden varmistamiseksi.
- Sukellusveneen vaihto**: Lightning-verkossa olevien Bitcoinien ja ketjussa olevien Bitcoinien väliset vaihdot.
- Stablecoin-swapit**: Atomivaihdot Bitcoinin ja USD-stabilcoinien välillä.
- Multisig-vaihtoehdot**: P2P-put- ja -call-optioiden luominen BTC-lukituksella ketjussa tapahtuvassa multisig-transaktiossa.
- Multisig Avoimet sopimukset**: Mahdollistaa räätälöityjen ehdollisten sopimusten luomisen käyttämällä 2-on-3 multisig-järjestelmää, jossa on arbitraasi.

Näitä protokollia kehitetään parhaillaan, ja ne integroidaan asteittain Bisq 2:een, mikä tarjoaa käyttäjille enemmän joustavuutta heidän erityistarpeidensa mukaan.

## Hyödyllisiä resursseja


- Virallinen verkkosivusto: [bisq.network](https://bisq.network)
- Dokumentaatio: [Bisq Wiki](https://bisq.wiki)
- Tuki: [Forum Bisq](https://bisq.community)
- Lähdekoodi : [GitHub](https://github.com/bisq-network)