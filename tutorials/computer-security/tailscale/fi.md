---
name: Tailscale
description: Edistynyt Tailscale opetusohjelma
---
![cover](assets/cover.webp)



## 1. Johdanto



Tailscale on seuraavan sukupolven VPN, joka luo salatun mesh-verkon laitteidesi välille. Sen avulla voit yhdistää etäkoneet ikään kuin ne olisivat samassa lähiverkossa ilman monimutkaista konfigurointia tai porttien avaamista.



Itse isännöintiä varten Tailscale määrittää jokaiselle laitteelle kiinteän yksityisen IP-osoitteen virtuaaliverkossa, mikä tarjoaa vakaan pääsyn palveluihisi, vaikka julkinen IP-osoitteesi muuttuisi. Tämä tarkoittaa, että voit hallita palvelimiasi etänä ilman, että palvelimesi ovat suoraan yhteydessä Internetiin.



**Pääsovellukset:**




- Hallitse henkilökohtaista palvelinta ulkopuolelta
- Umbrel/Lightning-solmujen hallinta nopeammin kuin Torin
- Turvallinen pääsy Raspberry Pi:hen tai NAS:iin
- Yhteys palveluihin SSH:n tai HTTP:n kautta ilman monimutkaisia verkkokonfiguraatioita



Tämä yksinkertaisuuteen keskittyvä lähestymistapa antaa itsepalvelun tarjoajille mahdollisuuden käyttää palvelujaan turvallisesti ja välttää perinteisten VPN:ien sudenkuopat.



## 2. Miten Tailscale toimii



Toisin kuin perinteiset VPN:t, jotka ohjaavat kaiken liikenteen keskitetyn palvelimen kautta, Tailscale luo mesh-verkon, jossa laitteet kommunikoivat suoraan toistensa kanssa. Keskuspalvelin huolehtii vain todennuksesta ja avainten jakelusta näkemättä käyttäjätietoja.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Kuva 1: Perinteinen VPN, jossa on hub-and-spoke-arkkitehtuuri, jossa kaikki liikenne kulkee keskuspalvelimen kautta*



WireGuardin avulla jokainen laite luo omat salausavaimensa. Koordinaatiopalvelin jakaa julkiset avaimet solmuille, jotka sitten luovat päästä päähän salattuja tunneleita suoraan keskenään. Palomuurien läpi pääsemiseksi Tailscale käyttää NAT:n ohitusta ja viimeisenä keinona DERP-välittäjiä, jotka ylläpitävät salausta.



![VPN maillé (mesh)](assets/fr/02.webp)


*Kuva 2: Tailscale mesh -verkko, jossa laitteet kommunikoivat suoraan toistensa kanssa*



Kaikki viestintä salataan WireGuardilla. Tailscale näkee vain metatiedot (yhteydet), mutta ei koskaan viestien sisältöä. Suuremman riippumattomuuden vuoksi Headscale mahdollistaa koordinointipalvelimen itse isännöinnin.



**Turvallisuus ja luottamuksellisuus:** WireGuardin ansiosta kaikki Tailscalen viestintä on päästä päähän salattua. Tailscale ei voi lukea liikennettäsi - vain laitteillasi on tarvittavat yksityiset avaimet. Palvelu näkee vain metatiedot: IP-osoitteet, laitteiden nimet, yhteyden aikaleimat ja vertaisverkkoyhteyden lokit (ilman sisältöä).



Tämä arkkitehtuuri on kuitenkin riippuvainen Tailscale Inc:stä verkon koordinoinnin osalta. Tämän riippuvuuden poistamiseksi Headscale tarjoaa avoimen lähdekoodin vaihtoehdon, jonka avulla voit itse isännöidä ohjauspalvelinta ja käyttää samalla virallisia Tailscale-asiakkaita, mikä takaa täydellisen määräysvallan verkkoinfrastruktuurissasi, mutta teknisen kokoonpanon kustannuksella.



**Kun haluat yksityiskohtaisen selityksen Tailscalen sisäisestä toiminnasta, mukaan lukien ohjaustasojen hallinta, NAT:n ylitys ja DERP-releet, suosittelemme virallisen blogin erinomaista artikkelia [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works). Tässä artikkelissa selitetään perusteellisesti tekniset käsitteet, jotka tekevät Tailscalen niin tehokkaaksi.



## 3. Tailscalen asentaminen



Tailscale toimii **yleisimmissä** käyttöjärjestelmissä (Windows, macOS, Linux, iOS, Android). Asennuksen sanotaan olevan "nopea ja helppo" kaikilla alustoilla. Aloitetaan tarkastelemalla Interface:ta ja tilien luomista, minkä jälkeen siirrytään eri ympäristöjen asennustoimenpiteisiin.



### 3.1 Tailscale-tilin luominen



Mene osoitteeseen [https://tailscale.com/](https://tailscale.com/) ja napsauta sivun oikeassa yläkulmassa olevaa "Get Started" -painiketta.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscalen kotisivulla selitetään konsepti ja tarjotaan ilmainen aloitus*



Jotta voit käyttää Tailscalea, sinun on ensin luotava tili identiteetin tarjoajan kautta:



![Page de connexion Tailscale](assets/fr/04.webp)


*Tailscaleen liitettävän identiteetin tarjoajan valinta (Google, Microsoft, GitHub, Apple jne.)*



Kun olet kirjautunut sisään, Tailscale pyytää sinulta joitakin tietoja käyttötarkoituksestasi:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Lomake, jotta ymmärtäisimme paremmin käyttötarkoitustasi (henkilökohtainen tai ammatillinen)*



Kun olet luonut tilisi, voit asentaa Tailscalen laitteillesi:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscalen avulla voit asentaa sovelluksen eri järjestelmiin*



### 3.2 Asennus eri alustoille





- Windows ja macOS:** Lataa graafinen sovellus Tailscalen viralliselta verkkosivustolta ja asenna se (.msi-tiedosto Windowsissa, .dmg-tiedosto Macissa). Kun sovellus on asennettu, se käynnistää graafisen Interface:n, jonka avulla voit muodostaa (selaimen kautta) yhteyden Tailscale-tiliisi koneen todennusta varten.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*MacBookin liittäminen takaverkkoon*



![Connexion réussie](assets/fr/09.webp)


*Vahvistus siitä, että laite on liitetty Tailscale*-verkkoon





- Linuxissa (Debian, Ubuntu jne.):** Sinulla on useita vaihtoehtoja. Yksinkertaisin tapa on ajaa virallinen asennusskripti: esimerkiksi Debian/Ubuntussa:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Tämä skripti lisää virallisen Tailscale-tietovaraston ja asentaa paketin. Voit myös [lisätä APT-arkiston manuaalisesti](https://pkgs.tailscale.com) tai käyttää tavallisia Snap- tai apt-paketteja. Kun daemon `tailscaled` on asennettu, se toimii taustalla. Tämän jälkeen sinun on **autentikoitava solmu** (katso Interface CLI vs. web alla). Muissa jakeluissa (Fedora, Arch...) paketti on saatavilla myös vakiovarastojen tai universaalin asennusskriptin kautta. Headless-palvelimessa käytä CLI:ää: esimerkiksi `sudo tailscale up --auth-key <key>`, jos käytät valmiiksi luotua tunnistusavainta, tai yksinkertaisesti `tailscale up` interaktiivista kirjautumista varten (joka antaa URL-osoitteen, johon mennään laitteen todentamiseksi).





- ARM-pohjaisissa järjestelmissä (Raspberry Pi jne.):** Käytämme yleensä Linuxia, joten sama lähestymistapa kuin edellä (skripti tai paketti). Huomaa, että Tailscale tukee ARM32/ARM64-arkkitehtuuria ongelmitta. Monet käyttäjät asentavat Tailscalen Raspberry Pi -käyttöjärjestelmään apt:n kautta tai kevyisiin jakeluihin (DietPi jne.), jotta he pääsevät käsiksi Piinsä kaikkialla.





- IOS- ja Android-käyttöjärjestelmissä:** Tailscale tarjoaa **virallisia** mobiilisovelluksia. Asenna *Tailscale* [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) tai [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Vaiheet Tailscalen asentamiseksi iPhoneen: tervetuloa, yksityisyys, ilmoitukset, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Muodosta yhteys tailnetiin, valitse tili ja vahvista se iPhonessa*



Kun sovellus on asennettu, se pyytää sinua ensimmäisellä käynnistyskerralla todentamaan itsesi valitun palveluntarjoajan kautta (Google, Apple ID, Microsoft jne., riippuen siitä, mitä käytät Tailscale-ohjelmassa) - menettely on sama kuin muilla alustoilla, yleensä se ohjaa sinut OAuth-verkkosivulle. Tämän jälkeen mobiilisovellus luo VPN:n (iOS:ssä sinun on hyväksyttävä VPN-konfiguraatiolisäosa). Sovellus voi sitten toimia taustalla, jolloin pääset tailnetiin mistä tahansa. *Huomaa:* Mobiilissa sinulla voi olla vain **yksi aktiivinen VPN kerrallaan** - varmista siis, ettei sinulla ole toista VPN:ää kytkettynä samaan aikaan, tai Tailscale ei pysty luomaan omaa VPN:ää. Androidissa voit määrittää erillisen työprofiilin, jos haluat eristää tietyt käyttötarkoitukset (esim. profiili, jossa Tailscale on aktiivinen tiettyä sovellusta varten).



### 3.3 Useiden laitteiden lisääminen ja validointi



Kun ensimmäinen laite on yhdistetty, Tailscale pyytää sinua lisäämään muita laitteita verkkoon:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface näyttää ensimmäisen kytketyn laitteen ja odottaa muita laitteita*



Kun olet lisännyt useita laitteita, voit tarkistaa, että ne voivat kommunikoida keskenään:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Vahvistus siitä, että laitteet voivat kommunikoida toistensa kanssa pingin avulla*



Tailscale ehdottaa sen jälkeen lisämäärityksiä, jotka parantavat käyttökokemustasi:



![Suggestions de configuration](assets/fr/14.webp)


*Ehdotuksia DNS:n määrittämiseen, laitteiden jakamiseen ja käyttöoikeuksien hallintaan*



### 3.4 Hallinnon kojelauta



Verkkohallintakonsolin avulla voit tarkastella ja hallita kaikkia liitettyjä laitteita:



![Tableau de bord des machines](assets/fr/15.webp)


*Luettelo liitetyistä laitteista ja niiden ominaisuuksista ja tilasta*



**Interface Web vs. Interface CLI:** Tailscale tarjoaa kaksi toisiaan täydentävää tapaa olla vuorovaikutuksessa verkon kanssa: **Interface web-hallinta** ja **komentoriviasiakasohjelma (CLI)**.





- Interface Web (hallintakonsoli)**: Tämä verkkokonsoli, johon pääsee osoitteesta [https://login.tailscale.com](https://login.tailscale.com), on Tailscale-verkkosi keskeinen kojelauta. Siinä luetellaan kaikki laitteet (*Koneet*), niiden online/offline-tila, niiden Tailscale IP-osoitteet ja paljon muuta. Täällä voit **hallita laitteita** (nimetä uudelleen, vanhentuneita avaimia, valtuuttaa reittejä, poistaa solmun käytöstä), **hallita käyttäjiä** (organisaatiokontekstissa) ja määritellä suojaussääntöjä (ACL). Täällä voit myös määrittää yleisiä asetuksia, kuten MagicDNS:n, tunnisteet tai auth-avaimet (ennen generate:ää auth-avaimet laitteiden automaattista lisäämistä varten). Interface-verkkopalvelin on erittäin kätevä yleiskatsauksen saamiseksi ja sellaisten muutosten soveltamiseksi, jotka siirretään koordinointipalvelimen kautta kaikkiin solmuihin. *Esimerkki:* **aliverkon reitin** tai **poistumissolmun** aktivointi tapahtuu yhdellä napsautuksella konsolissa, kun kyseinen solmu on ilmoittanut itsensä sellaiseksi.





- Interface:n komentorivi (CLI):** Komento `tailscale` on käytettävissä CLI:ssä jokaisessa laitteessa, johon Tailscale on asennettu. Tämän CLI:n avulla voit tehdä kaiken paikallisesti: muodostaa yhteyden (`tailscale up`), tarkastaa tilan (`tailscale status` nähdäksesi, mitkä vertaisverkot ovat yhteydessä), debugata (`tailscale ping <ip>`) ja niin edelleen. Jotkin ominaisuudet ovat jopa **yksinoikeudella CLI:lle** tai kehittyneempiä, esimerkiksi:





  - `tailscale up --advertise-routes=192.168.0.0/24` mainostaa aliverkon reittiä,
  - `tailscale up --advertise-exit-node` ehdottaa konettasi poistumissolmuksi,
  - `tailscale set --accept-routes=true` (tai `--exit-node=<IP>`) käyttääksesi reittiä tai poistumissolmua,
  - `tailscale ip -4` näyttääksesi laitteen Tailscale IP:n,
  - `tailscale lock/unlock` (jos käytössä on *tailnet-lock*, kehittynyt turvaominaisuus),
  - tai `tailscale file send <node>` käyttääksesi **Taildrop** (tiedostojen siirto laitteiden välillä).


CLI on erittäin hyödyllinen palvelimilla, joilla ei ole Interface-grafiikkaa, ja tiettyjen toimintojen skriptaamiseen. **Käytön erot:** Useimmat peruskonfiguraatiot voidaan tehdä joko Webin tai CLI:n kautta. Esimerkiksi laitteen lisääminen tapahtuu joko pyytämällä konsolin kautta tai suorittamalla `tailscale up` laitteelle ja vahvistamalla se webin kautta. Samoin laitteen nimeäminen uudelleen voidaan tehdä konsolin kautta tai komennolla `tailscale set --hostname`. **Yhteenvetona**, web-konsoli on ihanteellinen verkon globaaliin hallintaan (erityisesti useiden koneiden/käyttäjien kanssa), kun taas CLI on kätevä tietyn koneen hienojakoiseen hallintaan, automaatioskripteihin tai käyttöön järjestelmässä, jossa ei ole graafista käyttöliittymää.



## 4. Tailscalen käyttö Umbrelissa



Umbrel on suosittu itsepalvelualusta (jota käytetään erityisesti Bitcoin/Lightning-solmujen ja muiden itsepalveluiden osalta sen App Storen kautta). Umbrelin asentamista ja konfigurointia varten suosittelemme seuraamaan omaa opetusohjelmaamme:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Umbrelin ja Tailscalen käyttäminen yhdessä on erityisen mielenkiintoinen käyttötapaus, sillä Umbrel integroi natiivisti helposti käyttöönotettavan Tailscale-moduulin. Tässä kerrotaan, miten Tailscale integroituu Umbreliin ja mitä se tuo mukanaan:



### 4.1 Sateenvarjon asennus ja konfigurointi





- Tailscalen asentaminen Umbreliin:** Umbrelilla on virallinen Tailscale-sovellus App Storessa. Asennus ei voisi olla yksinkertaisempi:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Tailscale-sovelluksen sivu Umbrel App Storessa*



Avaa Interface Web Umbrelista App Store, etsi **Tailscale** ja napsauta *Asenna*. Muutaman sekunnin kuluttua sovellus on asennettu Umbreliin. Kun avaat sen, Umbrel näyttää sivun, jolla voit yhdistää solmun Tailscaleen.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Tailscale-liitännän näyttö Umbrel's Interface*:ssa



Napsauta vain **klikkaa "Kirjaudu sisään "**, joka ohjaa sinut Tailscalen todennussivulle:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Yhdistäminen Tailscaleen identiteetin tarjoajan kautta*



Voit tunnistautua Tailscale-tililläsi (Google/GitHub jne.) tai syöttää sähköpostiosoitteesi. Yleensä Umbrelissa Interface pyytää sinua käymään osoitteessa [https://login.tailscale.com](https://login.tailscale.com) ja kirjautumaan sisään - tämä todentaa Umbrelin Tailscale-sovelluksen.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Vahvistus siitä, että Umbrel-laite on liitetty Tailscale-verkkoon*



Kun tämä on tehty, Umbrel on "sisällä" Tailscale-verkossa ja näkyy konsolissasi nimellä (esim. *umbrel*). Tämän jälkeen voit kopioida laitteesi IP Address:n, hakea IPv6 Address:n tai laitteeseesi liittyvän MagicDNS:n napsauttamalla sitä.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscalen hallintakonsoli, jossa näkyy useita liitettyjä laitteita, mukaan lukien Umbrel*




### 4.2 Umbrel-palvelujen etäkäyttö



Kun Umbrel on yhdistetty Tailscaleen, **voit käyttää Interface Umbrelia ja siinä toimivia sovelluksia mistä tahansa, aivan kuin olisit paikallisverkossa**. Tämä on yksi tärkeimmistä eduista Toriin verrattuna.



Pääsy on huomattavan yksinkertaista: sen sijaan, että käyttäisit `umbrel.local` (joka toimii vain paikallisverkossa), voit käyttää Umbrelin Tailscale IP Address:tä (`http://100.x.y.z`) suoraan mistä tahansa laitteesta, joka on liitetty tailnetiin. Tämä toimii riippumatta siitä, missä olet tai mitä internet-yhteyttä käytät (4G, julkinen Wi-Fi, yritysverkko).



** Esimerkkejä Umbrelin isännöimistä sovelluksista, joihin pääsee käsiksi Tailscalen kautta:**





- Interface-sateenvarjo**: Pääset Umbrelin kojelautaan yksinkertaisesti kirjoittamalla selaimeen `http://100.x.y.z`
- Bitcoin-solmu**: Hallitse Bitcoin-solmua ilman viiveitä, katso synkronointia ja tilastoja
- Salamasolmu**: Käytä ThunderHubia, RTL:ää tai muita Lightningin hallintaliittymiä välittömällä reagointikyvyllä
- Mempool**: Tarkastele Bitcoin-tapahtumia ja Mempool-tapahtumia ilman Tor-viiveitä
- noStrudel**: Pääset käsiksi Nostr-palveluihisi, jotka sijaitsevat Umbrelissa



**Kytke ulkoiset lompakot Bitcoin- tai salamasolmuihin Tailscalen kautta:**



Tailscale mahdollistaa myös sen, että muihin laitteisiin asennetut Bitcoin- ja Lightning-lompakot voivat muodostaa yhteyden suoraan Umbrel-solmuun:





- Sparrow wallet (Bitcoin)**: Tämä ulkoinen Wallet Bitcoin voi muodostaa yhteyden suoraan Umbrelin Electrum-palvelimeen Tailscale IP Address:n avulla:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Yksityisen Electrum-palvelimen konfigurointi Sparrow wallet:ssä Umbrelin Tailscale IP Address*:n avulla



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Luettelo Electrum-palvelimen aliaksista Sparrow:ssä, jossa on Umbrel Tailscale IP Address*



Lue täydellinen oppaamme Sparrow wallet:n konfiguroinnista Bitcoin-solmun kanssa:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Salama)**: Tämä Wallet-mobiilisalama voi muodostaa yhteyden Umbrelin salamasolmuun. Sen sijaan, että konfiguroisit päätepisteen `.onion', aseta vain Umbrelin Tailscale-IP ja Lightning API -portti. Yhteys on Toriin verrattuna välitön.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Zeuksen konfigurointi yhteyden muodostamiseksi Lightning-solmuun Tailscale* IP Address:n kautta



Jos haluat määrittää Zeuksen Lightning-solmun kanssa, katso yksityiskohtainen ohjeemme:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Lisätietoja Lightning Network:stä ja sen toiminnasta Umbrelissa saat osoitteesta:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Edut Toriin verrattuna



Umbrel tarjoaa etäyhteyden Torin kautta (tarjoamalla www-palveluilleen .onion-osoitteita). Vaikka Torin etuna on luottamuksellisuus (anonymiteetti) eikä se vaadi rekisteröitymistä, monet käyttäjät pitävät **Toria hitaana ja epävakaana** jokapäiväisessä käytössä (sivut latautuvat hitaasti, aikakatkaisut jne.) - *"Umbrel Torin kautta on niin hidas "*, jotkut valittavat.



Tailscale tarjoaa yleensä **nopeamman, matalan viiveen** yhteyden, koska liikenne kulkee suoraan (tai nopean välittäjän kautta) sen sijaan, että se kiertäisi 3 Tor-solmua. Lisäksi Tailscale tarjoaa "lähiverkkokokemuksen": käytetään yksityisiä IP-osoitteita, ja sovellukset voidaan kartoittaa suoraan (esim. SMB-verkkoasema osoitteessa \100.x.y.z).



Torin etuna on kuitenkin se, että se on hajautettu ja "out of the box" Umbrelissa, kun taas Tailscale edellyttää luottamusta kolmanteen osapuoleen (tai headscale-hostingiin). Tor on myös hyödyllinen asiakaskäyttöön (mistä tahansa Tor-selaimesta voit käyttää Umbrelin käyttöliittymää, kun taas Tailscale edellyttää, että asiakas on asennettu käyttölaitteeseen).



**Yhteenvetona**, vuorovaikutteisessa käytössä (Lightning-lompakot, usein käytetyt web-käyttöliittymät) Tailscale tarjoaa tuntuvaa mukavuutta ja nopeutta Toriin verrattuna, mutta se on hieman riippuvainen ulkoisista tekijöistä. Monet ihmiset päättävät käyttää *kumpaa*: Tailscalen päivittäiseen käyttöön ja Torin varajärjestelmänä tai jos haluaa jakaa pääsyn jonkun kanssa kutsumatta häntä VPN:ään.



### 4.4 Turvallisuus



Käyttämällä Tailscalea Umbrelin kanssa vältät Umbrelin altistamisen Internetille. Umbrel-solmuun pääsevät käsiksi vain muut todennetut laitteet Tailnetissä, mikä vähentää huomattavasti hyökkäyspintaa (ei portteja, jotka ovat avoinna vieraille, eikä hyökkäysriskiä verkkopalveluun Internetin kautta).



Viestintä salataan (WireGuard) sen lisäksi, että palvelut jo salataan (esim. jopa sisäinen HTTP on tunnelissa). Voit silti käyttää Tailscale ACL:iä esimerkiksi estämään tietyn tailnet-laitteen pääsyn Umbreliin, jos haluat jakaa verkon. Umbrel itse ei näe eroa - se luulee palvelevansa paikallisesti.



---

Lopuksi totean, että Tailscalen integroiminen Umbreliin vie vain muutaman napsautuksen ja **parantaa huomattavasti itse isännöidyn solmun saavutettavuutta**. Voit hallinnoida Umbrelia ja sen palveluja mistä tahansa, turvallisesti ja tehokkaasti, aivan kuin olisit kotona. Tämä on erityisen hyödyllinen ratkaisu reaaliaikaisille sovelluksille (Lightning), jotka kärsivät Tor-viiveestä, tai yleisemmin kaikille itsehallinnoijille, jotka haluavat yksinkertaisen yksityisen yhteyden. Kaikki tämä paljastamatta yhtään porttia** laitteessasi ja ilman monimutkaisia verkkokonfiguraatioita.



## 5. Edistynyt hallinta ja käyttötapaukset



### 5.1 Tailscalen lisäominaisuudet



**Verkon hallinta:** Hallintakonsolin (login.tailscale.com) avulla voit hallita laitteita, tarkastella yhteyksiä ja määrittää pääsysääntöjä.



**MagicDNS:** Ratkaisee automaattisesti laitteiden nimet (esim. `raspberrypi.tailnet.ts.net`) välttääkseen IP-osoitteiden muistamisen.



**ACL ja pääsynvalvonta:** Määritä tarkasti, kuka voi käyttää mitä verkossa JSON-sääntöjen avulla, mikä on ihanteellista tiettyjen laitteiden eristämiseen tai tiettyjen palvelujen käytön rajoittamiseen.



**Laitteen jakamisen avulla voit kutsua jonkun käyttämään tiettyä laitetta antamatta hänelle pääsyä koko verkkoon.



**Subnet Router:** Tailscale-kone voi toimia koko aliverkon yhdyskäytävänä, mikä mahdollistaa pääsyn muihin kuin Tailscale-laitteisiin (IoT, tulostimet jne.) yhden määritetyn koneen kautta.



**Exit Node:** Käytä konetta Internet-yhdyskäytävänä, joka poistuu IP-osoitteensa avulla. Hyödyllinen julkisessa Wi-Fi:ssä tai maantieteellisten rajoitusten kiertämiseen.



**Taildrop:** Turvallinen vaihtoehto AirDropille, jonka avulla voit siirtää tiedostoja Tailscale-laitteiden välillä niiden alustasta tai sijainnista riippumatta. Toisin kuin AirDrop, joka rajoittuu Applen ekosysteemiin ja fyysiseen läheisyyteen, Taildrop toimii kaikkien laitteidesi välillä (Windows, Mac, Linux, Android, iOS), vaikka ne olisivat eri maissa. Tiedostot siirretään suoraan laitteiden välillä päästä päähän -salauksella, ilman että ne kulkevat keskitetyn palvelimen kautta. Käytä komentorivillä `taildrop file cp` tai graafista Interface-sovellusta järjestelmästäsi riippuen.



### 5.2 Vertailu muihin ratkaisuihin



**Vs OpenVPN:** Tailscale on paljon yksinkertaisempi konfiguroida (ei avattavia portteja, ei varmenteiden hallintaa), mutta se on riippuvainen kolmannen osapuolen palvelusta. OpenVPN on täysin hallittavissa, mutta vaatii enemmän asiantuntemusta.



**Suorana kilpailijana ZeroTier toimii Layer 2:lla (Ethernet) ja mahdollistaa broadcast/multicastin, kun taas Tailscale toimii Layer 3:lla (IP). ZeroTier tarjoaa suuremman verkkojoustavuuden, kun taas Tailscale suosii helppokäyttöisyyttä.



**Vs Tor:** Tor tarjoaa anonymiteettiä, jota Tailscale ei tarjoa, mutta on paljon hitaampi. Tor on hajautettu eikä vaadi tiliä, kun taas Tailscale on nopeampi ja tarjoaa lähiverkon kaltaisen kokemuksen.



**Vs WireGuard manuaalisesti:** Tailscale automatisoi kaiken avainten ja yhteyksien hallinnan, jota WireGuard raw vaatii sinua käsittelemään manuaalisesti. Se on käytännössä WireGuard + yksinkertaistettu hallinta Layer.



Yhteenvetona voidaan todeta, että Tailscale on nykyaikainen, yksinkertaisuuspainotteinen ratkaisu, joka sopii henkilökohtaiseen käyttöön ja pienille tiimeille. Täydellistä hallintaa kaipaaville puristeille Headscale tarjoaa itsehosting-vaihtoehdon.



## 6. Päätelmä



**Tailscalen edut:** Tailscale tarjoaa useita etuja itsepalveluhostingille:





- Yksinkertaisuus ja suorituskyky** - Nopea asennus kaikille alustoille ilman monimutkaisia verkkokokoonpanoja. Liikenne kulkee suorinta reittiä koneidesi välillä (P2P mesh) WireGuard-protokollan suorituskyvyn ansiosta, eikä keskitetty palvelin rajoita läpimenoa.
- Turvallisuus ja joustavuus** - Loppupäästä päähän -salaus, pienennetty hyökkäyspinta ja kehittyneet ominaisuudet (ACL, SSO/MFA-todennus). Toimii jopa NAT:ien takana tai liikkeellä, aliverkon reitittimien ja poistumissolmujen avulla voit mukauttaa verkon tarpeittesi mukaan.



**Rajat:** Pidä myös mielessä:





- Ulkoinen riippuvuus** - Palvelu on vakioversiossaan riippuvainen Tailscale Inc:n infrastruktuurista. Tämä riippuvuus voidaan ohittaa Headscalen avulla (itse isännöivä vaihtoehto).
- Muut rajoitukset** - Osittain suljettu lähdekoodi, ilmaisen version rajoitukset tietyille edistyneille käyttötarkoituksille, ei tukea Layer 2:lle (broadcast/multicast) ja yhteyden muodostaminen edellyttää Internet-yhteyttä.



**Tailscale on ihanteellinen yksittäisille itse isännöiville ja pienille tiimeille, kehittäjille, jotka tarvitsevat pääsyä hajautettuihin resursseihin, VPN-aloittelijoille ja mobiilikäyttäjille. Täydellistä hallintaa vaativille yrityksille muut ratkaisut, kuten Headscale tai WireGuard suoraan, voivat olla suositeltavampia.



** Tutustu Headscaleen, joka tarjoaa täydellisen itsepalvelun, API- ja DevOps-integraatiot (Terraform), tai vaihtoehtoihin, kuten Innernet (samanlainen, mutta täysin itsepalveluna) ja Netmaker.



Tailscale on yksinkertainen ja tehokas väline, joka on olennainen väline itsepalveluhostingissa, sillä sen ansiosta yksityinen infrastruktuurisi on yhtä helposti käytettävissä kuin pilvipalvelussa, mutta hallinta pysyy kotona.



## 7. Hyödyllisiä resursseja



### Viralliset asiakirjat





- Tailscale Documentation Center**: [docs.tailscale.com](https://docs.tailscale.com) - Täydellinen englanninkielinen dokumentaatio, asennusoppaat, opetusohjelmat ja tekniset viitteet.
- Miten Tailscale toimii**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Yksityiskohtainen artikkeli, jossa selitetään Tailscalen sisäinen toiminta.
- Muutosluettelo**: [tailscale.com/changelog](https://tailscale.com/changelog) - Seuraa päivityksiä ja uusia ominaisuuksia.



### Käytännön oppaat





- Kotilaboratorio** opetusohjelmat: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Erityisoppaat itsehostausta varten.
- Poistumissolmun määrittäminen**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Yksityiskohtainen opas Exit-solmujen konfiguroinnista.
- Käytä Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Siirrä tiedostoja Tailscale-laitteiden välillä.



### Vertailut





- Tailscale vs. muut ratkaisut**: [tailscale.com/compare](https://tailscale.com/compare) - Yksityiskohtaiset vertailut muihin VPN- ja verkkoratkaisuihin (ZeroTier, OpenVPN jne.).



### Yhteisö





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Keskustelua, kysymyksiä ja palautetta.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Asiakkaan lähdekoodi, jossa voi seurata kehitystä ja raportoida ongelmista.
- Keskustelu**: [discord.gg/tailscale](https://discord.gg/tailscale) - Käyttäjien ja kehittäjien yhteisö.



Tailscale tarjoaa säännöllisesti uutta sisältöä ja ominaisuuksia. Tarkista heidän [virallinen bloginsa] (https://tailscale.com/blog/) uusimmat uutiset ja tapaustutkimukset.