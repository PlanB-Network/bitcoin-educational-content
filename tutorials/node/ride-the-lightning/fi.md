---
name: Ride The Lightning (RTL)
description: Käytä Ride The Lightning (RTL) -palvelua Lightning-solmun hallintaan
---
![cover](assets/cover.webp)


## 1. Johdanto



**Ride The Lightning (RTL)** on täydellinen Interface-verkkosovellus Lightning Network-solmun hallintaan. Tämä itse ylläpidettävä verkkosovellus tarjoaa Lightning-"ohjaamon", johon pääsee selaimella. RTL toimii kaikkien tärkeimpien Lightning-toteutusten kanssa (LND, Core Lightning/CLN ja Eclair) ja antaa sinulle täydellisen hallinnan solmusi ja kanaviesi yli. Avoimen lähdekoodin (MIT-lisenssi) ja maksuttomana RTL on oletusarvoisesti integroitu moniin avaimet käteen -noodiratkaisuihin (RaspiBlitz, MyNode, Umbrel jne.).



**Ilman graafista Interface:a Lightning-solmuja voidaan hallita vain käyttäjäystävällisillä CLI-komennoilla. RTL yksinkertaistaa näitä toimintoja ergonomisella Interface:lla. Tässä ovat pääsovellukset:**





- **Kanavien ja solmun tarkastelu** - Kojelaudalla näytetään On-Chain-saldo, Lightning-likviditeetti (paikallinen/etä), synkronoinnin tila, solmun alias ja paljon muuta. Voit tarkastella kanavaluetteloa, kapasiteettia, paikallista/etäjakelua ja tilaa. RTL tarjoaa kontekstisidonnaisia kojelautoja, joilla voit analysoida toimintaa eri näkökulmista.





- **Salamakanavien hallinta** - Avaa/sulje kanavia muutamalla napsautuksella. RTL:n avulla voit muodostaa yhteyden vertaisverkkoon ja avata kanavan ilman komentoa. Voit säätää reitityspalkkioita, tarkastella saldopisteitä tai käynnistää ympäripyöreän tasapainotuksen varojen tasapainottamiseksi kanavien välillä.





- **Seuraa ja tee maksuja** - RTL hallinnoi Lightning-tapahtumia: lähetä maksuja laskujen kautta, vastaanota generate-laskuja, seuraa tapahtumia (maksut, reititys) yksityiskohtaisella historiatiedolla. Interface analysoi myös reitityksen, jotta näet, mitkä maksut kulkevat solmusi kautta.





- **Wallet On-Chain: hallinta ja varmuuskopiointi** - On-Chain-välilehdellä voit generate-osoitteita ja lähettää tapahtumia. RTL helpottaa kanavien tallentamista viemällä LND:n SCB-tiedoston, joka päivittyy automaattisesti jokaisen kanavamuutoksen yhteydessä.



Lyhyesti sanottuna RTL on **tehokas kojelauta Lightning Network:lle**, joka tarjoaa opettavaisen Interface:n solmun päivittäiseen ohjaamiseen. Tämä opetusohjelma opastaa sinut sen asennuksen ja käytön läpi kanavien ja maksujen hallintaan.



## 2. RTL:n tekninen toiminta



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Ennen kuin siirrytään yksityiskohtiin, on hyödyllistä ymmärtää lyhyesti, **miten RTL toimii vuorovaikutuksessa Lightning-solmun kanssa** teknisellä tasolla.



**Yleinen arkkitehtuuri:** RTL on verkkosovellus, joka on rakennettu Node.js:llä (backend) ja Angularilla (frontend). Konkreettisesti RTL toimii pienenä paikallisena web-palvelimena (oletusarvoisesti portissa 3000), joka käy vuoropuhelua Lightning-toteutuksesi kanssa sen API:iden kautta. Riippuen :





- **LND**:n kanssa RTL käyttää LND:n REST API:ta (portti 8080) Lightning-komentojen suorittamiseen. Yhteys on suojattu TLS:llä, ja se vaatii LND:n **admin macaroon**-tiedoston todennusta varten.





- **Core Lightningin (CLN)** kanssa RTL käyttää joko *c-lightning-REST*:n tarjoamaa REST-rajapintaa tai `commando`-laajennuksen kautta käytettävää **saccess-runea**. Umbrelin kaltaiset ratkaisut konfiguroivat nämä Elements:t automaattisesti.





- Kun käytössä on **Eclair**, RTL muodostaa yhteyden Eclair REST API:han käyttämällä määritettyä todennussalasanaa.



**Konfigurointi ja tietoturva:** RTL konfiguroidaan JSON-tiedoston (`RTL-Config.json`) avulla, jossa määrittelet verkkoportin, salasanan ja solmun yhteystiedot. Interface-verkko on suojattu sisäänkirjautumisella/salasanalla (oletus `salasana`, joka voidaan muuttaa) ja tukee 2FA:ta. Oletusarvoisesti RTL toimii paikallisena HTTP-yhteytenä (`http://localhost:3000`), mutta etäkäyttöön kannattaa aina käyttää suojattua yhteyttä (HTTPS käänteisen välityspalvelimen, Torin tai VPN:n kautta).



Lyhyesti sanottuna RTL on lisäkomponentti, joka muodostaa yhteyden solmuun turvallisten sovellusrajapintojen kautta, vaatii asianmukaiset käyttöoikeuskoodit ja tarjoaa oman tietoturva Layer:nsä. Tämän modulaarisen arkkitehtuurin ansiosta voit jopa hallita **monia Lightning-solmuja yhdellä RTL-instanssilla**.



## 3. RTL-asennus



Koska RTL on avoimen lähdekoodin ohjelmisto, on useita tapoja asentaa se järjestelmääsi. Tässä luvussa käsittelemme kahta pääasiallista tapaa: manuaalista asennusta ja Umbrelin kautta tapahtuvaa asennusta.



### Manuaalinen menetelmä



Manuaalinen asennus sopii, jos haluat säilyttää hienojakoisen hallinnan tai jos integroit RTL:n mukautettuun kokoonpanoon. Alla olevat vaiheet koskevat LND-solmua, jossa on Linux (esim. Raspberry Pi tai VPS, jossa on Ubuntu/Debian), mutta ne ovat samanlaiset myös CLN/Eclairissa.



**Edellytys:** Varmista, että koneessa on **synkronoitu** Bitcoin-solmu ja toimiva Lightning-solmu (LND, CLN tai Eclair). RTL ei sinänsä sisällä Lightning-solmua, vaan se muodostaa yhteyden olemassa olevaan solmuun. Tarvitset myös **Node.js** asennettuna (versio 14+ suositellaan). Voit tarkistaa sen `node -v`:llä tai asentaa Noden viralliselta sivustolta (https://nodejs.org/en/download/) tai paketinhallinnasta.



Tärkeimmät asennusvaiheet ovat :



**Lataa RTL-koodi**: Kloonaa RTL:n virallinen GitHub-arkisto haluamaasi hakemistoon. Esim:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Asenna riippuvuudet**: RTL on Node.js-sovellus, joten sinun on asennettava sen tarvitsemat moduulit. Suorita RTL-kansiossa :



```bash
npm install --omit=dev --legacy-peer-deps
```



Tämä komento asentaa tarvittavat NPM-paketit (ei huomioi kehitysriippuvuuksia). Valintaa `--legacy-peer-deps` suositellaan mahdollisten Node-riippuvuuskonfliktien välttämiseksi.



**RTL-Config**: Kun riippuvuudet on otettu käyttöön, valmistele konfiguraatiotiedosto. Kopioi/uudelleen nimeä projektin juuressa oleva `Sample-RTL-Config.json`-tiedosto muotoon `RTL-Config.json`. Avaa se :





- **UI-salasana**: valitse turvallinen salasana ja kirjoita se `multiPass`-kenttään (oletusarvoisen `"salasanan"` sijaan).
- **Portti**: oletusarvo `3000`. Voit muuttaa sitä, jos tämä portti on jo varattu koneellasi.
- **Solmu**: Säädä solmun parametrit kohdassa `solmut[0]`:
     - `lnNode`: kuvaava nimi solmulle (esim. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (tai `"CLN"`/`"ECL"` tapauksen mukaan).
     - Kohdassa `autentikointi`:
       - macaroonPath`: määritä täydellinen polku kansioon, joka sisältää LND:n macaroon adminin.
       - `configPath`: polku solmun konfigurointitiedostoon (LND:n tapauksessa `LND.conf`).
     - Kohdassa "Asetukset":
       - `fiatConversion`: aseta arvoksi `true`, jos haluat fiat-valuutan muuntamisen.
       - `unannouncedChannels`: aseta arvoksi `true` nähdäksesi ilmoittamattomat kanavat.
       - themeColor` ja `themeMode`: Interface mukauttaminen.
       - channelBackupPath`: LND-kanavan varmuuskopioiden polku.
       - `lnServerUrl`: Lightning-solmun URL-osoite (esim. `https://127.0.0.1:8080`).



**Käynnistä RTL-palvelin**: Suorita RTL-kansiossa :



```bash
node rtl
```



Sovellus käynnistyy, ja sitä voi käyttää osoitteessa `http://localhost:3000`.



**(Valinnainen) Suorita RTL palveluna**: Automaattista käynnistystä varten luo systemd :



Tätä varten:




- Avaa pääteasema koneellasi.
- Luo uusi palvelutiedosto seuraavalla komennolla (korvaa `nano` suosikkieditorillasi):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopioi ja liitä alla oleva sisältö tähän tiedostoon:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Korvaa `/path/to/RTL/rtl` koneellasi olevan `rtl`-tiedoston todellisella polulla ja `<your_user>` Linux-käyttäjänimelläsi.
- Tallenna ja sulje tiedosto.
- Lataa systemd-konfiguraatio uudelleen:


```bash
sudo systemctl daemon-reload
```




- Aktivoi ja käynnistä RTL-palvelu:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL käynnistyy nyt automaattisesti aina, kun kone käynnistetään uudelleen. Voit tarkistaa sen tilan komennolla :


```bash
sudo systemctl status RTL
```



### Asennus sateenvarjon kautta



Jos käytät [Umbrelia](https://getumbrel.com), RTL-asennus on paljon yksinkertaisempi:





- Pääsy Interface Umbreliin (yleensä `http://umbrel.local` kautta)
- Siirry **App Storeen**
- Etsi "Ride The Lightning"



**Tärkeä huomautus: Umbrel App Storessa on kaksi erillistä RTL-sovellusta:**




- **Ride The Lightning** (LND:lle): käytettäväksi Umbrelin oletusarvoisen Lightning-solmun (LND) kanssa.
- **Ride The Lightning (Core Lightning)**: Käytä vain, jos olet asentanut *Core Lightning* -sovelluksen Umbreliin ja haluat hallita tätä solmua RTL:llä.



*Kukin RTL-versio on valmiiksi konfiguroitu käymään vuoropuhelua vastaavan toteutuksen (LND tai Core Lightning) kanssa. Jos et ole vaihtanut Lightning-solmua, valitse yksinkertaisesti klassinen LND-versio*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Napsauta **Asenna**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Tärkeää:** Asennuksen jälkeen RTL näyttää näytön, jossa on oletussalasana. **Kopioi ja tallenna tämä salasana** - tarvitset sitä kirjautuaksesi Interface RTL:ään. Tämä salasana näytetään joka kerta, kun RTL käynnistyy, kunnes valitset vaihtoehdon "Älä näytä sitä enää".



Umbrel huolehtii automaattisesti :




- Lataa ja määritä RTL
- Lightning-solmun käyttöoikeuksien määrittäminen
- Hallitse päivityksiä
- Interface:een pääsyn varmistaminen



Kun sovellus on asennettu, se ilmestyy Umbrelin *Apps*-valikkoon. Käynnistä se napsauttamalla **Ride The Lightning**.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Kirjoita kirjautumisnäytössä aiemmin kopioimasi salasana. Kun olet kirjautunut sisään, Interface web RTL:ää voi käyttää suoraan Umbrelin kojelaudalta, eikä lisämäärityksiä tarvita!



## 4. Interface RTL:n käyttöönotto ja käyttö



Nyt kun RTL on toiminnassa, tutustutaan sen Interface-verkkoon ja sen tärkeimpiin ominaisuuksiin. Käymme läpi sovelluksen eri osiot, jotta saat kattavan yleiskuvan.



### Pääohjauspaneeli



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Heti kun kirjaudut sisään, pääset **pääkojelautaan**, josta saat yleiskuvan Lightning-solmusta. Tälle sivulle on keskitetty olennaiset tiedot:




- Lightning-saldosi kokonaismäärä
- On-Chain saldo käytettävissä
- Likviditeettisi jakautuminen (tuleva/lähtevä)
- Nopea pääsy Satssin lähettämiseen ja vastaanottamiseen Lightning-solmun kautta



### Rahaston hallinnointi On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



**On-Chain**-välilehdellä voit hallita bitcoinejasi suoraan pääketjussa:




- Saldonäyttö eri yksiköissä (Sats, BTC, USD)
- Täydellinen luettelo liiketoimista
- Address-sukupolvi Taproot (P2TR), P2SH (NP2WKH) tai Bech32 (P2WKH)
- UTXO hallinta, bitcoinien vastaanottaminen ja lähettäminen



### Salama: yksityiskohtainen esitys alivalikoista



Interface RTL:ssä on Lightning Network:lle omistettu sivuvalikko, johon on koottu kaikki solmun hallintaan tarvittavat toiminnot. Seuraavassa on kunkin alivalikon tiedot kuvakaappauksen mukaisessa järjestyksessä:



#### 1. Vertaiset/kanavat



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Tässä alivalikossa voit :




- Näytä luettelo yhdistetyistä vertaisverkoistasi ja Lightning-kanavista, jotka ovat avoinna tai odottavat.
- Lisää uusi vertaisverkko (yhteys toiseen Lightning-solmuun).
- Avaa, sulje tai hallinnoi olemassa olevia kanavia.
- Tarkastele kunkin kanavan tietoja: kapasiteetti, paikalliset/etäsaldot, tila, kaupankäyntihistoria, saldopisteet jne.



#### 2. Tapahtumat



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Tässä alivalikossa voit :




- Lähetä Lightning-maksut (Invoice:n kautta).
- generate ja hallita laskuja maksujen vastaanottamiseksi.
- Tarkastele lähetettyjen ja vastaanotettujen maksujen täydellistä historiaa yksityiskohtineen (summa, päivämäärä, tila, maksut, ohitusten määrä jne.).



#### 3. Reititys



Tämä alivalikko näyttää :




- Maksut, jotka solmusi reitittää muille Lightning Network-käyttäjille.
- Reititystilastot: välitettyjen tapahtumien määrä, saadut maksut, kohdatut virheet.
- Viedä historiaa kehittynyttä analyysia varten.



#### 4. Lykkäykset



Tämä alavalikko tarjoaa :




- Yksityiskohtaiset raportit Lightning-solmun toiminnasta.
- Kaaviot ja taulukot kanavista, maksuista, maksuista, kapasiteetista jne.
- Työkalut, joiden avulla voit ymmärtää solmun suorituskykyä paremmin.



#### 5. Graafin haku



Tässä alivalikossa voit :




- Tutki Lightning Network:n topologiaa.
- Etsi tiettyjä solmuja tai kanavia.
- Hanki tietoja liitettävyydestä ja verkon kokonaiskapasiteetista.



#### 6. Allekirjoita/Varmista



Tämä alivalikko tarjoaa :




- Kyky allekirjoittaa viesti oman solmun avaimella (todiste Ownership:stä).
- Allekirjoituksen todentaminen muiden solmujen viestien todentamiseksi.



#### 7. Varmuuskopiointi



Tämä alivalikko on omistettu varmuuskopioinnille:




- Vie kanavan varmuuskopiotiedosto (SCB LND:lle).
- Palauta kokoonpano tai kanavat tarvittaessa.
- Vinkkejä varmuuskopioiden suojaamiseen.



#### 8. Solmu/verkko



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Tästä alavalikosta löydät :




- Täydellinen yhteenveto Lightning-solmun tilasta: alias, versio, väri, synkronoinnin tila.
- Tilastot kanavista (aktiiviset, odottavat, suljetut), kokonaiskapasiteetti, liitettävyys.
- Tietoja globaalista Lightning Network:sta ja solmusi sijainnista siinä.



### Palvelut: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz on yksityisyydensuojaa kunnioittava, huoltajuuteen perustumaton Exchange-palvelu, joka muuntaa bitcoineja Lightning Network:n ja Blockchain:n Bitcoin:n (On-Chain) välillä. Se tarjoaa kahdenlaisia toimintatapoja: Reverse Submarine Swap (**Swap Out**) ja Submarine Swap (**Swap In**).



#### Swap Out (käänteinen sukellusveneen vaihto)



Swap Out muuntaa Lightning Network:ssa saatavilla olevat Satssit On-Chain-bittikolikoiksi. Tämä mekanismi on hyödyllinen, kun solmusta loppuu saapuva kapasiteetti tai kun haluat saada varoja takaisin On-Chain Address:stä. Prosessi toimii seuraavasti:




- Käyttäjä valitsee vaihdettavan määrän
- Solmu lähettää Lightning-maksun Boltzille
- Exchange:ssä Boltz estää vastaavan määrän On-Chain-bittikolikoita
- Kun maksutapahtuma on vahvistettu, käyttäjä voi lunastaa varat paljastamalla vaihdossa käytetyn salaisuuden



Prosessi ei ole huoltajuuteen perustuva, eikä Boltzilla ole koskaan hallussaan käyttäjän varoja.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Sukellusveneen vaihto)



Swap In -vaihtoehdon avulla On-Chain:n varat voidaan puolestaan siirtää Lightning Network:een. Tämä on erityisen hyödyllistä kanavien lähtökapasiteetin palauttamisessa. Menettely on seuraava:




- Käyttäjä lähettää bitcoineja tiettyyn Address:een, jonka Boltz on luonut
- Boltz voi vapauttaa nämä varat vain, jos hän maksaa käyttäjän solmun tuottaman Lightning Invoice -maksun
- Kun Invoice on maksettu, varat ovat käytettävissä Lightning-kanavassa, mikä lisää solmun tuotantokapasiteettia



![Configuration d'un swap-in](assets/fr/12.webp)



Nämä kaksi mekanismia mahdollistavat Lightning-kanavan likviditeetin tehokkaan hallinnan, mutta samalla säilytetään käyttäjän määräysvalta varoihinsa.



### Konfigurointi ja mukauttaminen



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



**Node Config**-välilehdellä voit mukauttaa käyttökokemustasi:




- Ilmoittamattomien kanavien aktivointi
- Mukauta myyntinäyttöä
- Block explorer kokoonpano
- Interface:n säätäminen



### Dokumentaatio ja apu



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Lopuksi **Help**-osio tarjoaa kattavan dokumentaation :




- Alkuperäinen konfigurointi
- Vertaisten ja kanavien hallinta
- Maksut ja maksutapahtumat
- Varmuuskopiot ja palautukset
- Kertomukset ja tilastot
- Allekirjoitukset ja varmennukset
- Solmun ja sovelluksen parametrit



Tämän kattavan Interface:n avulla voit hallita Lightning-solmua tehokkaasti perustoiminnoista edistyneisiin ominaisuuksiin, kaikki intuitiivisessa, hyvin organisoidussa Interface:ssä.



## 5. Edistyneet käyttötapaukset ja turvallisuus



Tässä osassa kerrotaan, mitä sinun on tiedettävä, jotta voit edetä RTL:n kanssa pidemmälle ja turvata Lightning-solmusi:



### Seuranta ja vianmääritys



Voit seurata solmua viemällä RTL-tietoja (lokitiedot, CSV) ja tarkastelemalla niitä Grafanan kaltaisissa työkaluissa. Ongelmatilanteissa (estetty maksu, inaktiivinen kanava) voit tarkastella LND/CLN-lokeja ja käyttää diagnostiikkakomentoja (`lncli listchannels`, `lncli pendingchannels` jne.). RTL tarjoaa myös Interface-lokit reititystapahtumien seuraamista varten.



### Turvallinen etäkäyttö



Älä koskaan paljasta RTL:ää suoraan Internetissä. Suosittele :




- **VPN** (esim. Tailscale) yksityistä, salattua yhteyttä varten
- **Tor** turvalliseen, anonyymiin käyttöön
- Käänteinen välityspalvelin **HTTPS** (Nginx/Caddy) vain, jos osaat määrittää sen



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Hyvät turvallisuuskäytännöt





- **Suojaa käyttöoikeutesi**: älä koskaan jaa admin.macaroon tai RTL-salasanaasi. Rajoita arkaluonteisten tiedostojen käyttöoikeuksia.
- **Säännölliset varmuuskopiot**: vie kanavan varmuuskopiotiedosto (SCB) jokaisen muutoksen jälkeen ja säilytä se solmun ulkopuolella.
- **Päivitykset**: Pidä RTL, solmusi ja Umbrel ajan tasalla uusimpien tietoturvakorjausten kanssa.
- **Luottamuksellisuus**: anonymisoi lokit ja kuvakaappaukset ennen niiden jakamista. Älä koskaan jaa saldoja tai vertaislistoja julkisesti.
- **Yksittäinen pääsy**: RTL ei ole monikäyttäjäkäyttöinen. Älä jaa ylläpitäjän käyttöoikeuksia. Jos haluat vain lukuoikeudet, käytä tarvittaessa omaa makaroonia.



Soveltamalla näitä periaatteita voit rajoittaa riskejä huomattavasti ja säilyttää Lightning-solmun hallinnan.



## 7. Päätelmä



**Ride The Lightning** on tärkeä työkalu Bitcoin/Lightning-solmun tehokkaaseen hallintaan, olitpa sitten aloittelija tai edistynyt käyttäjä. Se tarjoaa selkeän Interface:n kanavien, maksujen ja solmun kunnon hallintaan ja syventää samalla Lightning Network:n ymmärrystäsi.



RTL erottuu edukseen yhteensopivuudellaan useiden sovellusten kanssa, kehittyneillä toiminnoillaan (uudelleentasapainotus, swapit, raportit) ja pedagogisella lähestymistavallaan. Yksinkertaisiin tarpeisiin riittää Interface Umbrel tai Wallet mobile, mutta RTL on täysin järkevä aktiiviseen, optimoituun solmujen hallintaan.



Lisätietoja :




- RTL:n virallinen verkkosivusto: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Tekniset keskustelut, projekti-ilmoitukset, palaute ja koulutusresurssit
- **Umbrel-yhteisöfoorumi**: [community.getumbrel.com](https://community.getumbrel.com) - Virallinen foorumi, jossa on oma Bitcoin/Lightning-osio, oppaita ja ratkaisuja yleisimpiin ongelmiin
- **Lightning Network Kehittäjät**: [github.com/lightning](https://github.com/lightning) - Virallinen GitHub-tietovarasto kehityksen seuraamista ja lähdekoodin tuottamista varten
- Pino Exchange **Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Tekniset kysymykset ja vastaukset kehittäjien ja edistyneiden käyttäjien kanssa



Lyhyesti sanottuna RTL antaa sinulle täydellisen hallinnan Lightning-solmusi yli modernissa, täysin varustellussa Interface:ssa.



**Lähteet :** RTL:n virallinen verkkosivusto; RTL GitHub; Umbrel App Store; Umbrel Community; Plan ₿ Academy -resurssit.



Jos haluat syventää ymmärrystäsi Lightning Network:n toiminnasta, suosittelen myös tätä ilmaista kurssia:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb