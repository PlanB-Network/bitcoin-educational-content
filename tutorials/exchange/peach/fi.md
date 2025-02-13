---
name: Persikka
description: Täydellinen opas Peachin käyttöön ja bitcoinien P2P-vaihtoon
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Johdanto

KYC-vapaat P2P-pörssit ovat olennaisen tärkeitä käyttäjien luottamuksellisuuden ja taloudellisen riippumattomuuden säilyttämiseksi. Ne mahdollistavat suorat transaktiot yksityishenkilöiden välillä ilman henkilöllisyyden todentamista, mikä on ratkaisevan tärkeää yksityisyyttä arvostaville. Jos haluat syvällisemmän käsityksen teoreettisista käsitteistä, tutustu BTC204-kurssiin:

https://planb.network/courses/btc204
### 1. Mikä on persikka?

Peach on P2P-pörssialusta, jonka avulla käyttäjät voivat ostaa ja myydä bitcoineja ilman KYC:tä. Se tarjoaa intuitiivisen käyttöliittymän ja kehittyneitä turvaominaisuuksia. Verrattuna muihin ratkaisuihin, kuten Bisqiin, HodlHodliin ja Robosatiin, Peach erottuu edukseen helppokäyttöisyytensä ja edullisten maksujensa ansiosta.

### 2. Tietosuoja ja tiedonkeruu

**Mitä tietoja Peach kerää?

Peach pyrkii tallentamaan mahdollisimman vähän tietoja käyttäjistään. Seuraavassa on yleiskatsaus sen palvelimille tallennetuista tiedoista:


- Yksilöllisen sovellustunnuksesi (AdID) hash-tunnus
- Maksutietojesi hash-tiedosto
- Salatut keskustelut
- Transaktiotiedot sen varmistamiseksi, että anonyymit käyttäjät eivät ylitä kaupankäyntilimiittiä (käytetyt maksutavat, osto- ja myyntimäärät)
- Osoitteet, joilla lähetetään ja vastaanotetaan tietoja escrow-tililtä
- Käyttötiedot (Firebase & Google Analytics), vain suostumuksellasi

Muistutuksena mainittakoon, että hash on tietoa, joka on tehty tunnistamattomaksi, samoin kuin salaus. Sama data tuottaa aina saman hash-määritteen, joten kaksoiskappaleet voidaan havaita tuntematta alkuperäistä dataa.

*Jos haluat lisätietoa hashingista, voit seurata tätä kurssia:*

https://planb.network/courses/cyp201
**Kuka näkee maksutietoni?


- Vain vastapuolesi näkee maksutietosi
- Tiedot siirretään Peach-palvelimien kautta, mutta ne ovat täysin salattuja päästä päähän
- Riitatilanteessa maksutietosi ja keskusteluhistoriasi ovat nimetyn Peach-sovittelijan nähtävillä

## Asennus ja konfigurointi

### 1. Asenna Peach-sovellus

![Installation de Peach](assets/fr/01.webp)


- Lataa sovellus osoitteesta [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Seuraa laitteesi asennusohjeita.
- Asennuksen aikana sinua pyydetään valitsemaan, haluatko jakaa tiettyjä tietoja Peach-sovelluksen parantamiseksi (kuva 1)
- Seuraavassa näytössä (kuva 2) on kaksi vaihtoehtoa:
 - Jos olet uusi käyttäjä, klikkaa "Uusi käyttäjä" luodaksesi uuden profiilin
 - Jos sinulla on jo tili, voit palauttaa nykyisen profiilisi käyttämällä "Palauta"
- Jos sinulla on suosittelukoodi, voit syöttää sen tähän.
- Jos haluat palauttaa olemassa olevan tilin (kuva 3), tarvitset :
 - Varmuuskopiotiedostosi
 - Salasana tiedoston salauksen purkamiseen

### 2. Yleiskatsaus päänäytöihin

Peach-sovellus on järjestetty neljän päänäytön ympärille, joihin pääsee alhaalta navigointipalkista:

![Navigation dans l'application](assets/fr/02.webp)


- Etusivu** : Bitcoinien ostamisen ja myymisen päänäyttö. Täällä voit luoda uusia transaktioita ja tarkastella saatavilla olevia tarjouksia.
- Lompakko**: Integroitu Bitcoin-lompakko, jonka avulla voit :
 - Tarkista saldosi
 - Vastaanottaa bitcoineja
 - Lähetä bitcoineja
 - Tarkastele tapahtumahistoriaasi
- Kaupat** : Kaupan hallintakeskuksesi, josta löydät :
 - Nykyiset tapahtumat
 - Täydellinen historia vaihdoista
 - Kunkin tapahtuman tila
- Asetukset** : Tilisi asetuskeskus :
 - Hallitse maksutapojasi
 - Määritä varmuuskopiot
 - Mukauta mieltymyksiäsi
 - Apua ja tukea

### 3. Määritä maksutavat

![Accès aux paramètres de paiement](assets/fr/03.webp)

Pääset maksutapoihin Asetukset-välilehden kautta (kuva 8)

**Online-maksut

![Configuration des paiements en ligne](assets/fr/04.webp)


- Lisää uusi maksutapa napsauttamalla painiketta
- Valitse valuutta
- Valitse haluamasi maksutapa

*Käytettävissä olevat maksutavat:*

***Pankkisiirrot saatavilla: ***


- SEPA (vakio- tai pikakortti)
- Täytä SEPA-pankkitietosi

***Online-lompakot hyväksytään :***


- Käytettävissä on useita vaihtoehtoja maasta riippuen (Revolut, Paypal, Wise, Strike jne.)
- Seuraa ohjeita lisätäksesi kirjautumistietosi

***Lahjakortti, jota voi käyttää :*** ***


- Amazon
- Syötä kortin myöntäjämaa ja muut tarvittavat tiedot

***Kansalliset maksuvaihtoehdot:***

Maakohtaiset maksujärjestelmät :


- Satispay (Italia)
- MB Way (Portugali)
- Bizum (Espanja)
- Nopeammat maksut (Yhdistynyt kuningaskunta)

***Maksut henkilökohtaisesti:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Valitse "Meetup
- Valitse sitten tapaamisesi luettelosta

### Käyttöohjeet


- Voit määrittää useita maksutapoja samanaikaisesti
- Mitä enemmän menetelmiä lisäät, sitä laajempi valikoima tarjouksia on käytettävissäsi
- Tarkista, että tietosi ovat oikein ennen rekisteröitymistä
- Voit muuttaa tai poistaa maksutapojasi milloin tahansa

**Turvahuomautus**: Maksutietosi salataan ja jaetaan vain vaihtokumppanisi kanssa tapahtuman aikana.

### 4. Kuinka turvata salkkusi

**Ymmärtää Peach-tiliäsi

Peach-tili ei ole perinteinen käyttäjätunnus ja salasana. Se on tiedosto, joka on tallennettu paikallisesti puhelimeesi, joten Peachin ei tarvitse tallentaa tietojasi tai tietää henkilöllisyyttäsi: sinä hallitset tilannetta. Tämä tiedosto sisältää kaikki tietosi bitcoin-lompakon avaimista maksutietoihin.

Tämä lähestymistapa takaa suuremman luottamuksellisuuden, mutta merkitsee myös suurempaa vastuuta. Puhelimen menettäminen ilman varmuuskopiota tarkoittaa, että menetät pääsyn Peach-tilillesi ja varoihisi. On siis erittäin tärkeää varmuuskopioida tämä tiedosto ja suojata se vahvalla salasanalla.

**Luo varmuuskopiot**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Pääset asetuksiin aloitusnäytön oikeassa alareunassa olevasta välilehdestä
- Valitse asetusvalikosta vaihtoehto "varmuuskopiot"

![Processus de sauvegarde](assets/fr/06.webp)

Käytettävissä on kahdenlaisia varmuuskopioita:

**Tallenna tilitiedosto (kuva 14)**


- Napsauta "Luo uusi varmuuskopio"
- Luo vahva salasana varmuuskopiotiedoston salaamiseen
- Säilytä tämä tiedosto turvallisessa paikassa

Tiedoston varmuuskopiointi palauttaa koko Peach-tilisi, mukaan lukien :


- Salkkusi
- Maksutapasi
- Keskustelun historia
- Maksutiedot
- Transaktiohistoria ja vastapuolen tiedot

**Palautuslauseen tallentaminen (kuva 15)**


- Seuraa ohjeita näyttääksesi palautuslauseesi
- Kirjoita sanat huolellisesti oikeaan järjestykseen
- Säilytä tämä varmuuskopio turvallisessa paikassa, mieluiten eri paikassa kuin tilitiedosto

Palautuslausekkeella palautetaan vain :


- Pääsy tilillesi
- Bitcoin-varasi

Menetät :


- Keskustelun historia
- Maksutiedot
- Vastapuolen tiedot tapahtumahistoriassa

Optimaalisen turvallisuuden varmistamiseksi suosittelemme, että teet molempien varmuuskopiointityyppien varmuuskopiot.

## Bitcoinien ostaminen ja myyminen

### 1. Miten ostaa Bitcoineja

![Création et vue des offres](assets/fr/07.webp)


- Napsauta aloitusnäytössä "Osta"-painiketta (kuva 16)
- Määritä ostoksesi mieltymystesi mukaan (kuva 17)
- Selaa saatavilla olevien tarjousten luetteloa (kuva 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Valitse sinulle sopiva tarjous (kuva 19)
- Suorita maksu sovitulla tavalla
- Vahvista maksu sovelluksessa ja arvioi tapahtuma (kuva 20)

![Réception des bitcoins](assets/fr/09.webp)


- Seuraa tapahtuman tilaa
- Tarkista vahvistus bitcoinien vastaanottamisesta
- Varat ovat käytettävissä Peach-salkussasi

### 2. Kuinka myydä Bitcoineja

![Création d'un ordre de vente](assets/fr/10.webp)


- Määritä myyntitarjouksesi (kuva 24)
- Rahoita transaktio lähettämällä bitcoinit annettuun osoitteeseen (kuva 25)
- Odota tapahtuman vahvistusta (kuva 26)
- Tarjouksesi on nyt ostajien nähtävillä (kuva 27)

![Attente du paiement](assets/fr/11.webp)


- Seuraa tarjouksesi tilaa
- Odota ostajan maksuvahvistusta
- Tarkista tapahtuman tiedot

![Finalisation de la vente](assets/fr/12.webp)


- Tarkista maksun tila
- Vahvista maksun vastaanotto
- Arvioi liiketoimi
- Bitcoins vapautetaan automaattisesti ostajalle

**Vinkkejä onnistuneeseen kauppaan**


- Vastapuolen viesteihin vastaaminen nopeasti
- Tarkista maksutiedot huolellisesti
- Älä epäröi käyttää sovittelupalvelua, jos sinulla on ongelmia

**Turvahuomautus**: Älä koskaan vahvista maksun vastaanottamista ennen kuin olet varmistanut, että maksu on saapunut tilillesi.

## Edut ja haitat

### Persikan edut


- KYC:tä ei tarvita**: Säilyttää käyttäjän luottamuksellisuuden.
- Ei pääsyä pankkitietoihin**: Peach ei pääse käsiksi pankkitietoihisi tai henkilöllisyyteesi.
- Intuitiivinen käyttöliittymä**: Helppokäyttöinen keskitason käyttäjille.
- Avoin lähdekoodi** : Lähdekoodi on julkinen ja yhteisön tarkistettavissa.

### Persikan haitat


- Rajoitettu likviditeetti**: Pienempi kaupankäyntivolyymi kuin vakiintuneemmilla alustoilla.
- Sääntelyriski** : Sovellusta hallinnoi sveitsiläinen yritys. Siksi siihen sovelletaan sveitsiläisiä säädöksiä, jotka voivat kehittyä ja mahdollisesti sensuroida sovelluksen.

## Hyödyllisiä resursseja


- Ranskankielinen selittävä video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Pikaopas: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)