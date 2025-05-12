---
name: Lightning Network Daemon (Linux)
description: Lightning Network Daemon:n asentaminen ja käyttäminen Linuxissa
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network on Bitcoin:n toinen Layer, jonka ansiosta se voi saada salamannopeat mittasuhteet erityisesti sen tarjoamien transaktioiden nopeuden ja edullisuuden ansiosta.



Tässä ohjeessa asennamme Lightning Network Daemon-toteutuksen Linux-koneeseemme (Ubuntu 24.04 -jakelu).



## Mikä on Lightning Network Daemon?



Lightning Network Daemon on täydellinen Go-toteutus Lightning Network:sta. Sen on luonut Lightning Labs, ja sen avulla voit käyttää Lightning-solmun täydellistä instanssia koneellasi.


Toisin sanoen, tällä toteutuksella voit :





- Vuorovaikutus Lightning Network**:n kanssa: Voit käyttää komentoriviä Lightning-salkkujen luomiseen, maksukanavien ja -reittien hallintaan ja paljon muuta suoraan koneen päätelaitteesta.
- Etäisen Bitcoin-solmun tai oman Bitcoin Core-instanssin linkittäminen**: LND:n avulla voit linkittää Bitcoin-instanssin ja käyttää sitä backendinäsi. Tämän toteutuksen käyttämiseksi sinun ei tarvitse käyttää Bitcoin Core -instanssia koneellasi.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Miksi oma Lightning-solmu?


Lightning on Bitcoin-päällyste, joka optimoi siirtoprosessin ja vähentää transaktiokustannuksia.



Kiertämällä Lightning-solmusi saat itsemääräämisoikeuden ja autonomian. Hallitset varojasi, joten pidä mielessä:



"Ei avaimiasi, ei bitcoinejasi."



Tässä mielessä Lightning-solmun käyttäminen lisää tietojesi turvallisuutta ja eheyttä seuraavilla tavoilla:





- Täydellinen valvonta**: Hallitse omia maksukanavia, tule omaksi pankiksesi ja hallitse omaisuuttasi.
- Luottamuksellisuus**: Suorita liiketoimia turvautumatta yksityisyytesi suojaamiseen kolmansien osapuolten toimesta.
- Oppiminen ja itsenäisyys**: `lncli`-komentojen ansiosta voit ymmärtää paremmin Lightningin taustalla olevia prosesseja soveltamalla niitä itse päätelaitteesta käsin.
- Hajauttaminen**: Osallistu aktiivisesti Bitcoin:n / Lightning Network:n vahvistamiseen ja hajauttamiseen.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Sinulla on kaksi vaihtoehtoa LND-toteutuksen käyttämiseen koneellamme. Voimme joko perustaa ympäristön omalle koneellemme paikallisesti ajettavaksi tai asentaa LND:n Docker-säiliöstä. Tässä keskitymme ensimmäiseen vaihtoehtoon ja katsomme, miten Dockerin kanssa edetään myöhemmässä opetusohjelmassa.


## Asenna LND lähdekoodista



### Edellytykset


Koska LND on kirjoitettu Go-kielellä, sinun on varmistettava, että sinulla on GoLang-ympäristö ja tarvittavat riippuvuudet Linux-koneellasi.





- Laitteistovaatimukset:**


Sujuvan ja saumattoman käyttökokemuksen takaamiseksi koneellasi on oltava tarvittava kapasiteetti LND Lightning -solmun käyttämiseen.



Tarvitset :


1. **8 GB RAM-muistia** optimaalisen sujuvuuden varmistamiseksi,


2. **Moniydinprosessori (neliydin tai enemmän)**, joka hallinnoi solmun toimintoja tehokkaasti,


3. ** Vähintään 5 Gt levytilaa** karsittua solmua varten ja 1 Tt Bitcoin Corea varten (valinnainen, jos käytät etäsolmua)





- Asenna hyödyllisiä riippuvuuksia:**


Alla olevan komennon avulla voit asentaa koneellesi työkalut, joita tarvitset LND:n käyttämiseen. Sinun on muun muassa asennettava `Git`, versiointityökalu, ja `make`, joka voi suorittaa ja rakentaa LND-toteutuksen lähdekoodista.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Asenna GoLang Linux-koneellesi**



Tämän ohjeen päivämääränä LND vaatii Go***:n version 1.23.6 asennusta varten.



Jos sinulla oli jo asennettuna edellinen versio, poista se uutta Go-asennusta varten.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go**-ympäristön konfigurointi


Alusta seuraavat ympäristömuuttujat tiedostossa `~/.bashrc` lisätäksesi Go:n Linux-järjestelmääsi.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Asennuksen tarkistus** (ranskaksi)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Kloonaa LND GitHub-arkisto



Käytä Gitiä saadaksesi kopion LND:n lähdekoodista paikallisesti koneellesi


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Rakenna ja asenna



Aiemmin asennetun `make`-työkalun avulla voit rakentaa suoritettavan tiedoston LND:n lähdekoodista ja jatkaa asennusta.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Asenna LND koneellesi



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Asennuksen tarkistaminen** (ranskaksi)



Varmistaaksesi, että kaikki sujui moitteettomasti, tämän komennon suorittamisen pitäisi antaa sinulle tällä hetkellä käyttämäsi LND:n versio.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Ylläpito ja päivitykset



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **TÄRKEÄÄ**: LND-päivitykset saattavat vaatia Go:n uudempia versioita, joten muista päivittää järjestelmäsi, jotta vältät riippuvuusongelmat asennuksen aikana.


### Lightning Network Daemon:n määrittäminen



Lightning LND -solmun konfigurointi on samanlainen kuin Bitcoin:n, ja se tehdään konfigurointitiedostossa, joka sisältää kaikki solmun parametrit. Voit tehdä tämän luomalla koneesi juureen piilotetun kansion `.LND` ja luomalla konfigurointitiedoston `LND.conf` tähän kansioon.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Määritystiedostossa voit määrittää LND-solmun.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Kokoonpanon ymmärtäminen



On tärkeää, että ymmärrät vähimmäiskokoonpanon, jonka tarvitset LND-solmun oikeaan ja täydelliseen asennukseen.



Seuraavassa on kenttien yksityiskohdat tiedoston `~/.LND/LND.conf` sisällön perusteella:





- noseedbackup**: Voit valita, haluatko LND:n tekevän automaattisia varmuuskopioita salkuistasi.  Asettamalla tämän ominaisuuden arvoksi `0` voit tallentaa palautustiedot manuaalisesti henkilökohtaisesti valitsemaasi turvalliseen paikkaan.





- debuglevel**: Mahdollistaa virheiden ja lokien yksityiskohtaisuuden tason määrittelyn, jos toiminnon aikana tapahtuu virheitä.





- Bitcoin.active**: Ohjaa LND:ta toimimaan Bitcoin-solmuna ja olemaan vuorovaikutuksessa Bitcoin-verkon kanssa.





- Bitcoin.Mainnet**: Bitcoin Signet- ja Bitcoin Regtest-verkkoja varten voidaan asettaa arvot `bitcoind.signet` ja `bitcoind.regtest`





- Bitcoin.node**: Määrittää sen Bitcoin-solmun tyypin, johon LND:n pitäisi muodostaa yhteys.





- Bitcoin.rpcuser** ja **Bitcoin.rpcpassword** : Edustavat.


vastaavasti käyttäjätunnukset (käyttäjä, salasana), joilla voit muodostaa yhteyden Bitcoin-solmuun





- bitcoind.zmqpubrawblock** ja **bitcoind.zmqpubrawtx**: määrittelevät ZeroMQ-päätepisteet, jotka vastaanottavat ilmoituksia uusista lohkoista ja transaktioista Bitcoin-verkossa.




## Asennuksen tarkistaminen LND:llä



Haluat todennäköisesti varmistaa, että prosessi on onnistunut ja että synkronoit Lightning Network:n kanssa, jotta solmun tiedot pysyvät ajan tasalla.



Käynnistääksesi LND-toteutuksen ja saadaksesi tietoja solmusta, kirjoita komento :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Toimenpiteiden suorittaminen LND:ssä



Kun asennus on valmis ja tarkistettu, voit aloittaa sen käytön.


Tässä ovat keskeiset komennot, joilla pääset alkuun.



### Luo portfolio


Salamasalkkusi on ensimmäinen askel kaikissa varojesi hallinnointiin liittyvissä toimissa.



⚠️ **TÄRKEÄÄ**: Huomioi huolellisesti 24-sanainen **seed-lause**. Tarvitset sitä saadaksesi rahasi takaisin ongelmatilanteissa.



Tallenna myös Wallet:n salasana, jotta voit avata sen lukituksen komennolla `lncli unlock`, kun käynnistät LND-solmun uudelleen.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Tarkista saldosi



Tutustu tileihisi suoraan päätelaitteesta:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Solmua koskevat tiedot



Alla olevalla komennolla voit selvittää, mitkä kanavat ovat aktiivisia solmussasi.



```bash
lncli listchannels
```



Voit myös saada luettelon solmuista, joihin olet yhteydessä.



```bash
lncli listpeers
```



### Kanavien hallinta



Lightning-kanavan avulla voit muodostaa **suoran, pareittaisen yhteyden Lightning Network:n toiseen solmuun**. Tässä kanavassa voit käyttää vapaasti Exchange Satoshia kanavan kapasiteettiin asti.



### Yhdistä solmuun



Yhteyden muodostaminen muihin Lightning-solmuihin on perustavanlaatuinen toimenpide, jos haluat osallistua aktiivisesti Lightningin toimintaan ja hyötyä siitä.



Jos haluat muodostaa yhteyden vertaisverkkoon (Lightning-solmuun), tarvitset kolme tietoa:




- Solmun julkinen avain**: Tämä on solmun yksilöllinen tunniste Bitcoin-verkossa;
- IP** : Sen koneen IP-osoite, johon solmu on asennettu;
- PORT** :  Koneessa avattu portti, joka sallii kommunikoinnin tämän solmun kanssa.



Löydät solmuja, joihin voit muodostaa yhteyden, [amboss](https://amboss.space/) -alustalta, jossa luetellaan tietoja Lightning-solmuista.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Varmista, että muodostat yhteyden **luotettaviin solmuihin**, jotta oman järjestelmäsi eheys säilyy. Seuraavassa on joitakin suosituksia oikeiden yhteyksien valintaan.





- Maantieteellinen monipuolistuminen**: Yhteys eri alueiden solmukohtiin.





- Maine**: Valitse solmut, joilla on hyvä saatavuus.





- Kapasiteetti**: Valitse solmut, joilla on hyvä maksuvalmius.





- Syytteet**: Shekin reititysmaksut.


### Avaa maksukanava


Kun haluat avata maksukanavan, varmista, että olet **yhteydessä** vertaissolmuun, määritä sitten **kapasiteetti** (satoshien määrä), jonka haluat estää tässä kanavassa.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Luo Lightning Invoice



Lightning Invoice edustaa merkkijonoa, joka ilmaisee toiveesi saada satosheja Lightning Wallet:ään.


Luomalla Lightning-laskuja omalla solmulla voit suojata tietosi (maantieteelliset ja henkilökohtaiset) ja voit hallita varojasi 100-prosenttisesti itsenäisesti.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Salaman maksaminen Invoice



```bash
lncli payinvoice <FACTURE>
```


### Sulje kanava



Nykyisen solmun aktiivisen kanavan voi sulkea kahdella tavalla.





- Osuuskunnan sulkeminen**: Tämä ilmaisee solmusi halun vetäytyä maksukanavasta, jolloin varmistetaan, että käynnissä olevat tehtävät on suoritettu loppuun ja että tiedot varmuuskopioidaan varojen menettämisen välttämiseksi.


```
lncli closechannel <ID_CANAL>
```




- Pakkosulkeminen**: ⚠️ Vältä mahdollisuuksien mukaan, sillä tämä toimenpide keskeyttää käynnissä olevat prosessit maksukanavassasi ja lisää varojen menettämisen riskiä.


```
lncli closechannel --force <ID_CANAL>
```


## LND-solmun parhaat käytännöt ja turvallisuus.


Turvallisuus on ensiarvoisen tärkeää Bitcoin/ Lightning-solmua käytettäessä. Seuraavassa on muutamia kohtia, jotka vahvistavat asennuksen turvallisuutta:





- Säilytä `seed-lause` turvallisessa, offline-sijainnissa.





- Tee säännöllisiä varmuuskopioita tiedostosta `~/.LND/channel.backup`: Tämä tiedosto tallentaa kanavien tilat aina, kun solmussasi avataan uusi kanava (tai suljetaan vanha kanava).


⚠️ Mahdollistaa kanavien palauttamisen ja maksukanaviin jäädytettyjen varojen palauttamisen, jos tiedot katoavat tai solmupisteessä tapahtuu vika



Voit palauttaa varat alla olevalla komennolla määrittämällä tämän tiedoston varmuuskopiointipolun:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Varmista, että olet tallentanut Lightning Wallet:n palautussanat ja salasanan.
- Pidä järjestelmäsi ajan tasalla.



## Nykyinen vianmääritys


### Usein esiintyvät ongelmat




- bitcoind yhteysvirhe** : Tarkista RPC kirjautumistietosi
- Synkronointi estetty** : Tarkista Internet-yhteys
- Lupavirhe**: Tarkista kansion `~/.LND` oikeudet




Olet siis tullut tämän ohjeen loppuun. Jos haluat oppia lisää Lightningista, tarjoamme tämän johdantokurssin, jolla saat paremman käsityksen Lightning Network:n taustalla olevista käsitteistä ja käytännöistä.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb