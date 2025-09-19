---
name: Umbrel LND
description: Edistyneempi ohje Lightning Network Daemon:n (LND) asentamiseen ja konfigurointiin Umbrelissa
---
![cover](assets/cover.webp)




## Johdanto



Tämä edistynyt opetusohjelma opastaa sinua askel askeleelta Lightning Node (LND) -sovelluksen asennuksessa, konfiguroinnissa ja käytössä Umbrel-solmussasi. Opit avaamaan kanavia, hallitsemaan likviditeettiäsi ja synkronoimaan solmusi mobiilisovelluksen kanssa.



## 1. Edellytys: toimiva Bitcoin Umbrel-solmu



Ennen Lightningin käyttöönottoa sinulla on oltava täysin toimiva Bitcoin-solmu Umbrelissa. Tämä edellyttää Umbrelin asentamista (Raspberry Pi:lle, NAS:lle tai muulle koneelle) ja Blockchain Bitcoin:n täydellistä synkronointia.



Umbrelin asentamiseksi ja Bitcoin-solmun konfiguroimiseksi suosittelemme seuraamaan omaa opetusohjelmaamme :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Varmista, että Bitcoin-solmusi on ajan tasalla ja toimii oikein, sillä Lightning Network käyttää sitä kaikissa off-chain-tapahtumissa.



## 2. Johdanto Lightning Network:een



Lightning Network on toinen Layer-protokolla, joka on suunniteltu nopeuttamaan ja vähentämään Bitcoin-tapahtumien kustannuksia suorittamalla ne pää-Blockchain:n ulkopuolella.



Konkreettisesti Lightning käyttää solmujen välisten maksukanavien verkkoa: kaksi käyttäjää avaa kanavan estämällä On-Chain BTC:tä (alustava maksutapahtuma), minkä jälkeen he voivat välittömästi suorittaa Exchange-maksuja tämän kanavan sisällä. Näitä off-chain-tapahtumia ei kirjata Blockchain:een, minkä vuoksi ne ovat nopeita ja lähes maksuttomia.



Maksut voidaan ohjata useiden kanavien kautta (välittäjäsolmujen ansiosta) mihin tahansa verkon vastaanottajaan, mikä mahdollistaa lähes rajattoman määrän välittömiä maksutapahtumia. Lightning tarjoaa siis erittäin nopeita ja edullisia maksutapahtumia, jotka ovat ihanteellisia jokapäiväisiin maksuihin tai mikrotransaktioihin, ja keventää samalla Blockchain Bitcoin:n kuormitusta.



Toimiakseen Lightning-solmun on oltava pysyvästi yhteydessä verkkoon ja oltava vuorovaikutuksessa muiden Lightning-solmujen kanssa. Ohjelmistototeutuksia on erilaisia (LND, Core Lightning, Eclair jne.), jotka ovat kaikki yhteensopivia keskenään. Umbrel käyttää LND:a (Lightning Network Daemon) osana virallista Lightning Node -sovellustaan. Tämä opetusohjelma keskittyy LND:een.



Jos haluat täydellisen teoreettisen johdatuksen Lightning Network:een, suosittelemme, että osallistut siihen tarkoitukseen varattuun kurssiimme :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Tällä kurssilla saat perusteellisen perehdytyksen Lightning Network:n peruskäsitteisiin, ennen kuin siirryt harjoittelemaan LND-solmun kanssa.



## 3. Miksi itse isännöidä LND:ää?



Oman Lightning-solmun (LND) käyttäminen Umbrelissa antaa sinulle täydellisen määräysvallan varoistasi ja kanavistasi verrattuna säilytysratkaisuihin tai puoliksi säilytysratkaisuihin.



### Salamaratkaisujen vertailu :



**Solutions custodiales (esim. Wallet ja Satoshi)** :




- Lightning-bittikolikkojasi hallinnoi luotettava kolmas osapuoli
- Helppokäyttöinen, ei teknistä monimutkaisuutta
- Operaattori pitää rahojasi hallussaan ja voi jäljittää maksutapahtumasi
- Uhraat valvonnan ja luottamuksellisuuden



**Ei-hyödykesalkut (esim. Phoenix, Breez)** :




- Käyttäjät säilyttävät yksityiset avaimensa ja siten Ownership BTC:nsä
- Ei täydellistä solmujen hallintaa - sovellus hallitsee kanavia taustalla
- Kompromissi yksinkertaisuuden ja suvereniteetin välillä
- Riippuvuus toimittajien infrastruktuurista maksuvalmiuden kannalta
- Tekniset rajoitukset (yksi älypuhelin ei voi reitittää maksuja muille)



**Self-hosted LND-solmu (Umbrel)** :




- Maksimaalinen suvereniteetti: On-Chain- ja off-chain BTC:t ovat täysin sinun hallinnassasi
- Kolmannet osapuolet eivät osallistu kanavien avaamiseen tai maksujen hallinnointiin
- Lisääntynyt luottamuksellisuus (kanavasi ja tapahtumasi ovat vain sinun ja suorien kollegojesi tiedossa)
- Käytön vapaus: liity omiin palveluihisi ja lompakkoihisi
- Mahdollisuus reitittää liiketoimia muiden puolesta (mikropalkkio)
- Lisääntynyt tekninen vastuu (ylläpito, likviditeetin hallinta, varmuuskopiot)



Lyhyesti sanottuna itse isännöivä LND antaa sinulle maksimaalisen hallinnan, mutta vaatii enemmän teknisiä taitoja. Se on kompromissi mukavuuden ja itsenäisyyden välillä.



## 4. Vaiheittainen opetusohjelma



### 4.1 Lightning Node -sovelluksen asentaminen ja konfigurointi Umbrelissa



Kun Umbrel-solmusi (Bitcoin) on synkronoitu, noudata seuraavia ohjeita :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Asenna Lightning Node -sovellus Interface Umbrelin App Store -osiosta.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) otetaan käyttöön Umbrelissasi sovelluksena. Kun avaat sen ensimmäisen kerran, näet varoitusviestin, jossa kerrotaan, että Lightning on kokeellinen teknologia.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Voit valita, luotko uuden solmun vai palautatko solmun varmuuskopiosta/seed. Kun kyseessä on ensiasennus, valitse uuden solmun luominen. Lightning Node -sovellus antaa generate 24-sanaisen Mnemonic-lauseen (seed Lightning-varasi): kirjoita se hyvin huolellisesti muistiin (mieluiten offline-tilassa paperille), sillä sitä käytetään tarvittaessa Lightning-varasi palauttamiseen.



**Huomaa: Umbrelin uusimmissa versioissa Lightning-sovelluksen asennus tarjoaa tämän 24-sanaisen seed:n (itse Bitcoin Umbrel-solmu ei tarjoa).**



![Interface principale de Lightning Node](assets/fr/04.webp)



Alustamisen jälkeen pääset Lightning Noden pää Interface:een.



![Paramètres de l'application](assets/fr/05.webp)



Sovelluksen asetuksista löydät useita tärkeitä vaihtoehtoja:




   - Kysy solmun ID-tunnusta (solmun yksilöllinen tunniste)
   - Ulkoisen Wallet:n liittäminen (Connect Wallet)
   - Näytä salaiset sanat
   - Pääsy lisäasetuksiin
   - Palauta kanavat
   - Lataa kanavan varmuuskopiotiedosto
   - Ota automaattiset varmuuskopiot käyttöön
   - Määritä varmuuskopiointi Torin kautta (Backup over Tor)



Nämä vaihtoehdot ovat välttämättömiä Lightning-solmun turvallisuuden ja hallinnan kannalta. Varmista, että aktivoit automaattiset varmuuskopiot ja pidät salaiset sanasi turvassa.



**Hyödyllisiä resursseja:**




- [Umbrel Community](https://community.umbrel.com) - Keskustelufoorumi, jossa käyttäjät voivat jakaa Umbreliin ja sen ekosysteemiin liittyviä ongelmia ja ratkaisuja


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Lightning Node -sovelluksen ominaisuuksien kuvaus Umbrelissa
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - LND:n virallinen dokumentaatio

### 4.2 Salamakanavan avaaminen



Kun LND on toiminnassa, voit avata ensimmäisen Lightning-kanavasi. Löydät laadukkaita solmuja, joihin voit muodostaa yhteyden:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) on etsintäohjelma luotettavien solmujen löytämiseksi kanavien avaamista varten.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Esimerkiksi [ACINQ-solmu] (https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) on tunnustettu solmu, jolla on erinomaiset saatavuus- ja likviditeettitilastot.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Tässä opetusohjelmassa avaamme kanavan [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Yhteyden muodostamiseen tarvittavat tiedot (pubkey@ip:port) on annettu heidän Amboss-sivullaan.



Kanavan avaaminen :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Napsauta Lightning Node -etusivulla painiketta "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



Kanavan määrityssivulla :




   - Liitä Ambossista kopioitu solmutunnus (muoto: pubkey@ip:port)
   - Määritä kanavakapasiteetin määrä (joillakin solmuilla, kuten ACINQ:lla, on vähimmäismäärät, esim. 400k Sats)
   - Mukauta tarvittaessa avaustapahtumamaksuja



![Canal en cours d'ouverture](assets/fr/11.webp)



Kun maksutapahtuma on lähetetty, kanava näkyy etusivulla "avautuneena". Odota vahvistusta On-Chain-tapahtumasta.



![Détails du canal](assets/fr/12.webp)



Klikkaa kanavaa nähdäksesi sen tiedot:




   - Nykytila
   - Kokonaiskapasiteetti
   - Maksuvalmiuden jakautuminen (tuleva/lähtevä)
   - Etäisen solmun julkinen avain
   - Ja muut tekniset tiedot



### Lightning Network+:n käyttäminen saapuvan likviditeetin hankkimiseen



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ on saatavilla Umbrel App Storessa, mikä helpottaa saapuvan käteisen hankkimista.



![Interface principale de LN+](assets/fr/14.webp)



Interface:n päävalikossa on kolme tärkeää vaihtoehtoa:




- "Maksuvalmiusswapit: tutustu saatavilla oleviin swap-tarjouksiin"
- "Open For Me": suodata swapit, joihin olet oikeutettu
- "To Docs": pääsy dokumentaatioon



![Message d'erreur LN+](assets/fr/15.webp)



Huomautus: Jos kanavaa ei ole vielä avattu, näet tämän virheilmoituksen, kun napsautat "Avaa minulle".



![Liste des swaps disponibles](assets/fr/16.webp)



Sivulla "Liquidity Swaps" näkyvät kaikki verkossa saatavilla olevat swap-tarjoukset.



![Swaps éligibles](assets/fr/17.webp)



"Avaa minulle" suodattaa vain ne vaihdot, joiden osalta solmusi täyttää vaaditut ehdot.



![Détails d'un swap](assets/fr/18.webp)



Esimerkki vaihtotiedoista :




- Pentagonin kokoonpano (5 osallistujaa)
- Kapasiteetti 300k Sats per kanava
- Edellytys: vähintään 10 avointa kanavaa, joiden kokonaiskapasiteetti on 1M Sats
- Vapaita paikkoja: 4/5



### 4.3 Synkronointi mobiilisovelluksen (Zeus) kanssa



Voit hallita Lightning-solmua etänä (älypuhelimella) käyttämällä Zeus-sovellusta (avoimen lähdekoodin sovellus, joka on saatavilla iOS:lle/Androidille).



**Zeuksen kokoonpano sateenvarjon kanssa :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Varmista, että Umbrel-solmusi on käytettävissä (oletusarvoisesti Torin kautta).


Avaa Lightning Node -sovellus Interface Umbrelissa ja napsauta sitten nuolella osoitettua "Connect Wallet" -painiketta.



![Page de connexion avec QR code](assets/fr/20.webp)



Näyttöön ilmestyy QR-koodi, joka sisältää LND:n käyttötiedot lndconnect-muodossa. Tämä QR-koodi sisältää erityisen paljon tietoa, joten älä epäröi suurentaa sitä lukemisen helpottamiseksi.



![Configuration initiale de Zeus](assets/fr/21.webp)



Puhelimessa :




   - Avaa Zeus
   - Napsauta etusivulla "Lisäasetukset" kytkeäksesi oman Lightning-solmun
   - Valitse parametreista "Luo tai liitä Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Zeuksessa:




   - Valitse yhteystyypiksi "LND (REST)"
   - Voit joko skannata QR-koodin (suositeltava menetelmä) tai syöttää tiedot manuaalisesti. (Älä epäröi zoomata sateenvarjon QR-koodia, sillä se on hyvin tiheä)
   - Tärkeää: aktivoi "Käytä Toria" -vaihtoehto, jos Umbreliin pääsee käsiksi vain Torin kautta (oletusasetus)
   - Tallenna kokoonpano



Zeus on nyt yhdistetty Umbrel-solmuun, ja voit tehdä Lightning-maksuja, tarkastella kanavia, saldoja jne., mutta voit silti hallita itse itseäsi.



**Edistyneet yhteysvaihtoehdot:**



Oletusarvoisesti Zeus ↔ Umbrel -yhteys toimii Torin kautta. Nopeampaa yhteyttä varten on kaksi vaihtoehtoa:



**Lightning Node Connect (LNC)** :




   - Lightning Labsin salattu yhteysmekanismi
   - Asenna Lightning Terminal -sovellus Umbreliin (sisältää LNC-käytön)
   - generate yhteys QR-koodi Lightning Terminalissa (Connect → Connect Zeus via LNC)
   - Skannaa se Zeukseen (valitse yhteystyypiksi "LNC")



**VPN Tailscale**:




   - Helposti konfiguroitava mesh VPN
   - Asenna Tailscale Umbreliin (App Store) ja matkapuhelimeesi
   - Yhdistä Zeus Tailscalen yksityisen IP:n kautta Tor Address:n sijaan



Nämä vaihtoehdot eivät ole pakollisia, ja Tor + Zeus -ratkaisu toimii hyvin useimmissa tapauksissa.



> **Hyödyllisiä resursseja:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Virallinen opas Zeuksen ja Umbrelin yhdistämiseen
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Avoimen lähdekoodin Zeus-projekti
> - [Umbrel Community - Zeuksen liittäminen Tailscalen kautta](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Opas Zeuksen liittämiseen Umbreliin Tailscalen avulla

## 5. Turvallisuus ja parhaat käytännöt



Itse isännöidyn Lightning-solmun hallinta edellyttää erityistä huomiota tietoturvaan.



### Solmun varmuuskopiointi ja turvallisuus



**Välttämättömät varmuuskopiotyypit**



Lightning Umbrel -solmusi tarvitsee kahdenlaisia varmuuskopioita:



**seed-lause (24 sanaa)**




- On-Chain-varojen takaisinperintä
- Tarvitaan Wallet Lightningin uudelleenluomiseen
- Erittäin turvalliseen tallennukseen (offline, paperilla)



**Static Channel Backup (SCB)** -tiedosto




- Sisältää salamakanavan tiedot
- Mahdollistaa pakotetun kanavan sulkemisen kaatumisen yhteydessä
- **Tärkeää:** Älä koskaan tallenna `channel.db`-tiedostoa manuaalisesti (rangaistusten vaara)



**Manuaalinen varmuuskopiointimenettely**



Kanavien tallentaminen manuaalisesti :


1. Pääset Lightning Node -valikkoon (kolme pistettä "⋮" kohdan "+ Open Channel" vieressä)


2. Lataa kanavan varmuuskopiotiedosto


3. Vie uusi SCB jokaisen kanavan muutoksen jälkeen


4. Säilytä SCB turvallisesti (salattu media, kopio muualla kuin toimipaikassa)



**Umbrel** automaattinen varmuuskopiointijärjestelmä



Umbrelissa on kehittynyt automaattinen varmuuskopiointijärjestelmä, joka varmistaa :



*Tietosuoja:*




- Asiakaspuolen salaus ennen lähetystä
- Lähettäminen Tor-verkon kautta
- Satunnaistäytteellä täydennetyt tiedot
- Laitteesi yksilöllinen salausavain



*Parannettu turvallisuus:*




- Välittömät varmuuskopiot tilamuutoksista
- Harhautus" varmuuskopiot satunnaisin väliajoin
- Piilota varmuuskopion koon muutokset
- Suojaus aika-analyysiltä



*Palauttamisprosessi:*




- seed-sateenvarjostasi johdettu tunniste ja avain
- Täydellinen restaurointi mahdollista vain Mnemonic-lauseella
- Viimeisimpien varmuuskopioiden automaattinen palautus
- Kanava-asetusten ja -tietojen palauttaminen



### Törmäyksen palauttaminen



Jos solmu on kadonnut (laitteistovika, vioittunut SD-kortti) :




- Asenna sateenvarjo takaisin
- Kirjoita 24-sanainen seed Lightning-sovellukseen
- Tuo SCB-tiedosto palauttamisen aikana



LND ottaa yhteyttä vanhojen kanaviesi kaikkiin kumppaneihin sulkeakseen ne ja saadakseen takaisin osuutesi On-Chain:n varoista. Kanavat suljetaan pysyvästi (ne voidaan avata tarvittaessa uudelleen).



### Saatavuus ja petostentorjunta



Ihannetapauksessa jätä solmusi verkkoon mahdollisimman usein. Jos poissaolo kestää pidempään:




- Haitallinen vertaisvertainen voi yrittää lähettää vanhan kanavan tilan
- Lightning tarjoaa "protestiajan" (noin 2 viikkoa LND:n osalta)
- Jos aiot olla poissa pitkän aikaa, perustakaa Watchtower



**Watchtower kokoonpano:**




- Lisää LND:n lisäasetuksissa luotetun Watchtower-palvelimen URL-osoite
- Voit käyttää julkista palvelua tai asentaa oman Watchtower:n




Jos haluat tietää lisää Watchtowerin konfiguroinnista ja käytöstä, suosittelemme, että tutustut omaan opetusohjelmaamme :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Muut parhaat käytännöt





- **Ohjelmistopäivitykset:** Pidä Umbrel ja LND ajan tasalla (tietoturvakorjaukset)
- **Laitteiston suojaus:** Käytä vakaata järjestelmää (Raspberry Pi SSD-levyllä, mini-PC) ja UPS:ää
- **Verkkoturvallisuus:** Pidä Torin oletuskonfiguraatio, vaihda Umbrelin ylläpitäjän salasana (oletus: "moneyprintergobrrr")
- **Salaus:** Ota levyn salaus käyttöön, jos mahdollista



## 6. Lisätyökalut



Umbrelin Lightning Node -sovellus tarjoaa kanavien hallintaan tarvittavat perusominaisuudet, mutta kolmannen osapuolen työkalut tarjoavat lisätoimintoja.



### ThunderHub



Interface moderni verkkopohjainen Lightning-solmujen hallintajärjestelmä, joka on asennettavissa Umbrel App Storen kautta.



**Ominaisuudet:**




- Kanavien reaaliaikainen visualisointi (kapasiteetit, saldot)
- Integroidut tasapainotustyökalut
- Tuki monipolkulaskutukselle (MPP)
- QR-koodin luominen LNURL
- Tapahtumien hallinta On-Chain



ThunderHub on ihanteellinen aktiivisen reitityssolmun valvontaan ja yksinkertaiseen tasapainottamiseen.



### Ride The Lightning (RTL)



Interface on yhteensopiva useiden Lightning-toteutusten kanssa (LND, Core Lightning, Eclair).



**Highlights:**




- Usean solmun hallinta
- Kontekstiherkät kojelaudat
- Tuki sukellusveneen vaihtamiselle (Lightning Loop)
- 2-tekijätodennus
- Kanavan varmuuskopioiden vienti/tuonti



RTL on täydellinen "sveitsiläinen armeijan veitsi" Lightning-solmun hallintaan asiantuntijalähtöisemmällä lähestymistavalla.



### Muita hyödyllisiä työkaluja





- **Lightning Shell**: Komentorivi (lncli) selaimen kautta
- **BTC RPC Explorer & Mempool**: Seuranta Blockchain
- **LNmetrics & Torq**: Reitityksen suorituskykyanalyysi
- **Amboss & 1ML**: solmun "sosiaalinen" hallinta (aliakset, yhteystiedot, verkostoanalyysi)



Nämä työkalut voidaan asentaa muutamalla napsautuksella Umbrel App Storesta ilman monimutkaisia asetuksia.



**Lisätyökaluresurssit:**




- [ThunderHub.io - Ominaisuudet](https://thunderhub.io) - Yleiskatsaus ThunderHubin ominaisuuksiin
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL dokumentaatio
- [David Kaspar - tasapainottaminen ThunderHubin kautta](https://blog.davidkaspar.com) - Käytännön opas tasapainottamiseen
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Laajennettu dokumentaatio tehokäyttäjille



## Päätelmä



Oman LND-solmun käyttäminen Umbrelissa on tärkeä askel kohti taloudellista riippumattomuutta. Vaikka se vaatii enemmän teknistä panostusta kuin säilytysratkaisu, sen tuomat hyödyt valvonnan, luottamuksellisuuden ja aktiivisen osallistumisen muodossa Lightning Network:n toimintaan ovat huomattavat.



Tämän oppaan avulla sinun pitäisi nyt pystyä asentamaan LND, avaamaan kanavia, hallinnoimaan likviditeettiäsi ja käyttämään solmua etänä. Voit vapaasti tutustua vähitellen lisäominaisuuksiin ja lisätyökaluihin, kun tutustut ekosysteemiin paremmin.



Muista, että varojesi turvallisuus on riippuvainen suojatoimista ja käytännöistäsi. Käytä aikaa ymmärtääksesi kaikki näkökohdat, ennen kuin sitoudut suuriin summiin.