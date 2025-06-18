---
name: Sateenvarjo
description: Tutustu ja asenna Umbrel - Bitcoin-solmusi ja kotipalvelimesi
---

![cover](assets/cover.webp)



## Johdanto



### Mikä on Bitcoin-solmu?



Bitcoin-solmu on tietokone, joka osallistuu Bitcoinverkkoon käyttämällä Bitcoin Core -ohjelmistoa tai vaihtoehtoista asiakasohjelmaa. Sen rooli on olennainen verkon toiminnan ja turvallisuuden kannalta:





- Blockchain varastointi**: Säilyttää täydellisen ja ajantasaisen kopion Blockchain:sta Bitcoin
- Tapahtumien todentaminen**: validoi jokaisen tapahtuman ja lohkon protokollan sääntöjen mukaisesti
- Tiedon levittäminen**: Jakaa uudet transaktiot ja lohkot muiden solmujen kanssa
- Konsensuksen luominen**: Osallistuu verkoston sääntöjen soveltamiseen



Oman Bitcoin-solmun ylläpitäminen on ratkaiseva askel kohti taloudellista riippumattomuutta, sillä se tarjoaa useita keskeisiä etuja:





- Luottamuksellisuus**: Jaa tapahtumasi paljastamatta tietojasi kolmansille osapuolille
- Sensuurin vastustaminen**: Kukaan ei voi estää sinua käyttämästä Bitcoin:ta
- Riippumaton tarkastus**: Sinun ei tarvitse luottaa muiden ihmisten solmuihin tapahtumiesi varmentamiseksi
- Konsensuksen rakentaminen**: Osallistutaan Bitcoin-verkon sääntöjen soveltamiseen
- Verkkotuki**: Ryhdy aktiiviseksi osallistujaksi verkon jakeluun ja hajauttamiseen



### Sateenvarjo: Bitcoin-solmun käyttämiseen yksinkertainen ratkaisu



Umbrel on avoimen lähdekoodin käyttöjärjestelmä, joka yksinkertaistaa Bitcoin-solmun asennusta ja hallintaa. Se myös muuttaa tietokoneen henkilökohtaiseksi ja yksityiseksi kotipalvelimeksi, jonka avulla on helppo isännöidä :





- Täydellinen Bitcoin-solmu
- Bitcoin olennaiset sovellukset (Electrs, Mempool.space)
- Muut henkilökohtaiset palvelut (pilvitallennus, suoratoisto, VPN jne.)



Umbrel tarjoaa tyylikkään ja intuitiivisen Interface-käyttäjän Interface:n avulla itse isännöidyt palvelut kaikkien saataville, mutta säilyttää samalla tietojen täydellisen hallinnan.



## Sateenvarjon asennusvaihtoehdot



Umbrel tarjoaa kaksi pääasiallista tapaa käyttää ratkaisuaan: avaimet käteen -vaihtoehto (Umbrel Home) ja ilmainen avoimen lähdekoodin versio (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Avaimet käteen -ratkaisu



Umbrel Home on valmiiksi konfiguroitu kotipalvelin, joka on suunniteltu erityisesti optimaalista käyttökokemusta varten. Tämä all-in-one-laitteistoratkaisu sisältää:



**Hardware-ominaisuudet**




- Suorituskykyinen prosessori, joka on optimoitu itseisännöintiä varten
- Esiasennettu nopea SSD-tallennustila
- Hiljainen jäähdytysjärjestelmä
- Kompakti, tyylikäs muotoilu
- Integroidut USB- ja Ethernet-portit



**Erityiset edut**




- Plug-and-play-asennus: kytke ja käynnistä
- Premium-tuki ja oma apu
- Taatut automaattiset päivitykset
- Integroitu migraatio-ohjattu toiminto
- Täysi laitteistotakuu
- Täysi tuki kaikille toiminnoille



**Hinta**: 399 € (hinta voi vaihdella sesongin mukaan)



### UmbrelOS: Avoimen lähdekoodin versio



UmbrelOS on ilmainen, avoimen lähdekoodin versio Umbrel-käyttöjärjestelmästä. Tämän joustavan ratkaisun avulla voit käyttää omaa laitteistoasi ja samalla hyödyntää Umbrelin keskeisiä ominaisuuksia.



**Hyötyjä**




- Täysin ilmainen
- Avoin, todennettavissa oleva lähdekoodi
- Valinnanvapaus
- Kehittyneet mukautusvaihtoehdot



**Tuetut alustat**




- Raspberry Pi 5: suosittu ja edullinen ratkaisu
- X86-järjestelmät: Tavallisiin PC-tietokoneisiin tai palvelimiin
- Virtuaalikone: Testausta tai käyttöä varten olemassa olevassa infrastruktuurissa



**rajoitukset




- Ainoastaan yhteisön tuki
- Joitakin Umbrel Home -palvelulle varattuja lisäominaisuuksia
- Tekninen alkukokoonpano
- Suorituskyky riippuu valitusta laitteistosta



Tämä versio on ihanteellinen :




- Tekniset käyttäjät
- Ne, joilla on jo yhteensopivat laitteet
- Ihmiset, jotka haluavat oppia ja kokeilla
- Kehittäjät, jotka haluavat osallistua hankkeeseen



Viralliset asennuslinkit :




- [Asennus Raspberry Pi 5:een](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Asennus x86-järjestelmiin (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Virtuaalikoneen asennus](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Tässä ohjeessa keskitymme UmbrelOS:n asentamiseen Raspberry Pi 5:lle, mutta perusperiaatteet ovat samanlaiset myös muilla alustoilla.



## Umbrel OS:n asentaminen Raspberry Pi 5:een



### Tarvittavat komponentit



Tätä asennusta varten tarvitset :





- Raspberry Pi 5 (4 GB tai 8 GB RAM)
- Virallinen Raspberry Pi -virta Supply (vakauden kannalta erittäin tärkeää!)
- MicroSD-kortti (vähintään 32 Gt)
- MicroSD-kortinlukija
- Ulkoinen SSD-levy tietojen tallentamista varten
- Ethernet-kaapeli
- USB-kaapeli SSD-aseman liittämistä varten



### Asennuksen vaiheet



** Lataa UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Käy [virallisilla verkkosivuilla](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Lataa uusin versio UmbrelOS:stä Raspberry Pi 5:lle



**Balena Etcher** asennus



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Lataa ja asenna [Balena Etcher](https://www.balena.io/etcher/) tietokoneellesi



**Microsd-kortin** valmistelu



![Insertion carte microSD](assets/fr/03.webp)




- Aseta microSD-kortti tietokoneen kortinlukijaan



**Kuvan vilkkuminen**



![Flashage UmbrelOS](assets/fr/04.webp)




- Balena Etcherin käynnistäminen
- Valitse ladattu UmbrelOS-kuva
- Valitse microSD-kortti määränpääksi
- Napsauta "Flash!" ja odota, että prosessi päättyy
- Poista kortti turvallisesti



**microSD-kortin asennus



![Installation microSD](assets/fr/05.webp)




- Aseta microSD-kortti Raspberry Pi 5:een



**Perifeerinen yhteys**



![Connexion périphériques](assets/fr/06.webp)




- Liitä ulkoinen SSD-levy käytettävissä olevaan USB-porttiin
- Kytke Ethernet-kaapeli Piin ja reitittimen välille



**Power on



![Démarrage du Pi](assets/fr/07.webp)




- Kytke virallinen Raspberry Pi -virta Supply
- Odota muutama minuutti, että järjestelmä käynnistyy



**Ensimmäinen pääsy**



![Accès interface web](assets/fr/08.webp)




- Avaa selain samaan verkkoon liitetyssä laitteessa
- Umbrelin Interface-verkkosivusto osoitteessa: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Jos `umbrel.local` ei toimi, sinun on löydettävä Raspberry Pi:n IP Address lähiverkosta. Voit :




- Tutustu reitittimen Interface
- Verkkoskannerin, kuten nmap, käyttäminen
- Käytä komentoa `arp -a` tietokoneen päätelaitteessa



## Ensimmäinen askel Umbrelilla



Kun Umbrel on käynnistetty ja käytettävissä selaimen kautta, aloita toiminta seuraavien ohjeiden mukaisesti:



### Alkuperäinen konfigurointi



**Luo tilisi**



![Création compte](assets/fr/10.webp)




- Valitse käyttäjänimi
- Aseta turvallinen salasana
- Tarvitset nämä tunnukset päästäksesi Umbreliin käsiksi



**Tilin vahvistus



![Confirmation compte](assets/fr/11.webp)




- Klikkaa "Seuraava" päästäksesi kojelautaan



** Interface:n löytäminen**



![Interface Umbrel](assets/fr/12.webp)




- Pääsy Umbrel App Storeen
- Tutustu moniin käytettävissä oleviin sovelluksiin
- Aloitetaan asentamalla Bitcoin:n keskeiset sovellukset



### Bitcoin-sovellusten asentaminen



**Bitcoin-solmu**



![Bitcoin Node](assets/fr/13.webp)




- Ensimmäinen asennettava sovellus
- Lataa ja tarkista koko Blockchain Bitcoin



**Valitsijat*



![Installation Electrs](assets/fr/14.webp)




- Electrum-palvelin Bitcoin-lompakoiden yhdistämiseen
- Synkronoi Bitcoin-solmun kanssa



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface-näyttö Blockchain:lle
- Seuraa tapahtumia ja lohkoja reaaliajassa



## Tapahtuman seuranta Mempool.space -palvelun avulla



Mempool.space on avoimen lähdekoodin Blockchain-etsintäohjelma, joka tarjoaa reaaliaikaisen visualisoinnin Bitcoin-verkosta. Sen avulla voit seurata transaktioitasi ja ymmärtää, miten transaktiot leviävät verkossa.



### Mempool:n ja vahvistusten ymmärtäminen



Mempool (muistialtaat) on kuin virtuaalinen odotushuone, johon kaikki vahvistamattomat Bitcoin-tapahtumat tallennetaan ennen niiden sisällyttämistä lohkoon. Näin transaktio käsitellään:



1. **Lähetys**: Kun lähetät tapahtuman, se lähetetään ensin Bitcoin-verkkoon


2. **Odotamme Mempool:ssa**: Odottaa, että Miner valitaan kustannusten perusteella


3. **Ensimmäinen vahvistus**: Alaikäinen sisällyttää sen lohkoon (1. vahvistus)


4. **Lisävahvistukset**: Jokainen uusi lohko, joka louhitaan sen lohkon jälkeen, joka sisältää transaktiosi, lisää vahvistuksen



Vahvistusten suositeltu määrä riippuu määrästä :




- Pienille määrille: 1-2 vahvistusta voi riittää
- Suurille määrille: 6 vahvistusta pidetään yleensä erittäin turvallisina



### Tutustu Interface:een Mempool.space:sta



1. **Kotisivulla** saat yleiskuvan Bitcoin-verkosta:




   - Äskettäin louhitut lohkot
   - Kustannusarviot eri prioriteeteille
   - Mempool:n nykytila



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Tapahtuman haku**: Jos haluat seurata tiettyä tapahtumaa, liitä sen tunniste (txid) sivun yläreunassa olevaan hakupalkkiin.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analysoi tapahtuman yksityiskohtia



Kun tapahtumasi on löydetty, Mempool.space esittää sinulle täydellisen analyysin:



1. **Tärkeitä tietoja** :




   - Tila (vahvistettu tai vahvistamaton)
   - Maksetut kulut (Sats/vB)
   - Arvioitu vahvistusaika



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Transaktiorakenne** :




   - Sisään- ja ulostulojen visuaalinen esitys
   - Yksityiskohtainen luettelo asianomaisista osoitteista
   - Siirretyt määrät



3. **Tekniset tiedot** :




   - Tapahtuman paino
   - Virtuaalinen koko
   - Käytetty muoto ja versio
   - Muut erityiset metatiedot



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Mempool.space on Umbrel -ohjelman käytön edut



1. **Salaisuuden suojaaminen**: Pyyntösi kulkevat oman solmusi kautta


2. **Iriippumattomuus**: Ei tarvitse luottaa kolmannen osapuolen palveluun


3. **Luotettavuus**: Pääsy tietoihin silloinkin, kun julkiset selaimet eivät ole käytettävissä



Tämän sovelluksen avulla voit seurata tehokkaasti tapahtumia, ymmärtää, miten maksut vaikuttavat vahvistusnopeuteen, ja ymmärtää paremmin, miten Bitcoin-verkko toimii.



## Wallet Bitcoin:n liittäminen solmuun



### Electrs kokoonpano



** Paikallinen yhteys



![Connexion locale](assets/fr/18.webp)




- Paikallisverkossa käytettäväksi
- Nopeampi ja helpompi asentaa



** Etäyhteys Torin kautta**



![Connexion Tor](assets/fr/19.webp)




- Voit käyttää solmua mistä tahansa
- Turvallisempi ja yksityisempi



### Yhteys Sparrow Wallet:een



** Pääsy parametreihin



![Paramètres Sparrow](assets/fr/20.webp)




- Avoin varpunen Wallet
- Siirry kohtaan Asetukset > Palvelin
- Napsauta "Muokkaa olemassa olevaa yhteyttä"



**Yhteystyypin valinta



Sparrow tarjoaa kolme yhteystapaa:



***Julkinen palvelin***




- Yhteys julkisiin palvelimiin (esim. blockstream.info, Mempool.space)
- Yksinkertainen mutta vähemmän yksityinen



***Bitcoin Core***




- Suora yhteys Bitcoin-solmuun
- Yksityinen mutta hitaampi



***Private Electrum***




- Muodosta yhteys Electrs-palvelimeen
- Yhdistää luottamuksellisuuden ja suorituskyvyn



**Valitsijoiden** kokoonpano



Valitse yhteystyyppisi aiemmin näkemämme Electrs-sovelluksen näyttämien tietojen perusteella:



Jätä molemmissa tapauksissa vaihtoehdot "Käytä SSL:ää" ja "Käytä välityspalvelinta" valitsematta.



** Paikallinen yhteys


Isäntä: umbrel.local


Sataman numero: 50001



** Etäyhteys (Tor)**


Isäntä : [your-Address-onion]


Sataman numero: 50001



Tor-yhteys on välttämätön, jos haluat käyttää solmua lähiverkon ulkopuolella.



![Configuration connexion](assets/fr/21.webp)


Jos haluat lisätietoja Sparrow Wallet -ohjelmistosta, meillä on kattava opetusohjelma :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Päätelmä



Sateenvarjosi on nyt käyttövalmis. Osallistut aktiivisesti Bitcoin-verkkoon ja pidät samalla täyden määräysvallan tietoihin. Tutustu vapaasti moniin muihin Umbrel App Storessa saatavilla oleviin sovelluksiin, joilla voit laajentaa kotipalvelimesi ominaisuuksia.



## Hyödyllisiä resursseja



### Viralliset asiakirjat




- [Virallinen sateenvarjosivusto](https://umbrel.com)
- [Sateenvarjo-asiakirjat](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin-sovellukset




- [Bitcoin Core] (https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Varpunen Wallet](https://sparrowwallet.com)



### Yhteisö




- [Foorumin sateenvarjo](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter-sateenvarjo](https://twitter.com/umbrel)