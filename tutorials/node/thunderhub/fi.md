---
name: ThunderHub
description: Interface Salamasolmun hallintaverkkosivusto LND
---
![cover](assets/cover.webp)



## Johdanto



ThunderHub on **avoimen lähdekoodin Lightning-solmujen (LND)** hallintaohjelma, joka tarjoaa intuitiivisen Interface:n, jota voi käyttää millä tahansa laitteella tai selaimella.



**Pääominaisuudet:**




- **Seuranta**: Maailmanlaajuinen näkymä saldoista, kanavista, tapahtumista ja reititystilastoista
- **Johto**: Kanavien avaaminen/sulkeminen, saapuvat/ulostulevat maksut, kanavien tasapainottaminen
- **Integraatiot**: Ambossin varmuuskopiointi: LNURL-tuki, vaihdot Boltzin kautta
- **Interface reagoi**: Yhteensopiva mobiili-, tablet- ja työpöytälaitteiden kanssa tummilla/vaaleilla teemoilla



ThunderHub integroituu helposti **Umbrel**, **Voltage**, **RaspiBlitz** ja **MyNode** -palveluihin, mikä yksinkertaistaa solmun päivittäistä hallintaa.



**ThunderHub soveltuu erityisesti operaattoreille, jotka etsivät ergonomista Interface:tä kanaviensa hallintaan, likviditeetin valvontaan (uudelleentasapainottaminen), transaktioiden seurantaan ja kolmansien osapuolten palvelujen, kuten Ambossin, integrointiin. Turvallisuus varmistetaan paikallisen tai Tor-yhteyden avulla.**



Jos sinulla ei vielä ole Lightning-solmua, suosittelemme, että seuraat LND Umbrel -opastusta:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Asennus



ThunderHub voidaan asentaa useilla eri tavoilla Lightning-solmun hosting-ympäristöstä riippuen. Käytitpä sitten avaimet käteen -ratkaisua (Umbrel, Voltage, RaspiBlitz, MyNode, Start9 jne.) tai manuaalista asennusta, ThunderHub on usein käytettävissä ilman suurempaa vaivaa. Alla kuvaamme kaksi yleistä lähestymistapaa: Umbrel App Storen kautta ja manuaalisen asennuksen kautta (sovellettavissa palvelimelle tai itse isännöidylle jakelulle).



### Asennus sateenvarjon kautta



Umbrel integroi ThunderHubin omaan **App Storeen**, mikä tekee asennuksesta erittäin helppoa. Komentoriviä tai manuaalista konfigurointia ei tarvita: kaikki tehdään Interface Umbrelin kautta. Seuraa vain näitä ohjeita:





- **Avaa Umbrel-kojelauta**: Muodosta yhteys Umbrel-solmusi Interface-verkkoon (esim. `http://umbrel.local` lähiverkossasi tai sen `.onion` Address:n kautta, jos käytät Toria).
- Pääset App Storeen: Napsauta Umbrelin päävalikossa "App Store" (tai "App"). Etsi **ThunderHub** käytettävissä olevien sovellusten luettelosta.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Asenna ThunderHub**: Napsauta ThunderHub-sovellusta ja sitten asennuspainiketta. Vahvista tarvittaessa. Umbrel lataa ja ottaa ThunderHubin automaattisesti käyttöön solmussasi.





- **Käynnistä sovellus**: Kun asennus on valmis (muutama kymmenen sekuntia), ThunderHub ilmestyy etusivullesi. Avaa se napsauttamalla kuvaketta. ThunderHub käynnistyy selaimessasi.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Tärkeää:** Kun ThunderHub avataan ensimmäisen kerran, se näyttää automaattisesti kirjautumiseen tarvittavan **perussalasanan**. "Älä näytä tätä enää" -vaihtoehdon avulla voit piilottaa tämän näytön tulevia yhteyksiä varten. **Suosittelemme vahvasti, että:**




- Tallenna tämä salasana välittömästi **salasanahallintaasi**
- Kopioi se käytettäväksi seuraavassa vaiheessa
- Tarkista "Älä näytä tätä uudelleen", kun salasana on tallennettu



![Page de connexion de ThunderHub](assets/fr/03.webp)



Tämän jälkeen pääset kirjautumissivulle, jossa sinun on annettava edellisessä vaiheessa kopioimasi salasana Interface:n lukituksen avaamiseksi.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel huolehtii siitä, että ThunderHub saa LND-yhteystietoja (TLS-varmenne, hallintamakrooni jne.) taustalla, joten sinun ei tarvitse tehdä mitään lisämäärityksiä. Muutamalla klikkauksella saat ThunderHubin toimimaan Umbrel-solmussasi.



### Manuaalinen asennus (itse isännöity, pois lukien Umbrel)



Umbrelin ulkopuolisille käyttäjille (esim. henkilökohtaisella palvelimella, Raspberry Pi:llä RaspiBlitzin kanssa tai *yksittäisellä* asennuksella) ThunderHubin asennus vaatii muutaman ylimääräisen vaiheen. Seuraavassa kuvataan asennus lähdekoodista ja konfigurointi [ThunderHubin virallisen dokumentaation](https://docs.thunderhub.io) mukaisesti.



#### Asennus



**Edellytykset:** Varmista, että järjestelmäsi täyttää [documentation setup](https://docs.thunderhub.io/setup) mukaiset vähimmäisvaatimukset:




- **Node.js** versio 18 tai uudempi versio
- **npm** asennettu
- Pääsy LND-todennustiedostoihin :
  - LND TLS-sertifikaatti (`tls.cert`)
  - LND hallintamakrooni (`admin.macaroon`)
  - LND gRPC-palvelu Address (isäntänimi:portti) (oletusarvo `127.0.0.0.1:10009` paikallisesti)



**1. Hae ThunderHub-koodi:** Kloonaa projektin GitHub-tietovarasto [asennusdokumentaatiossa](https://docs.thunderhub.io/installation) kuvatulla tavalla:



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. asenna riippuvuudet ja rakenna sovellus:**



```bash
npm install
npm run build
```



Nämä komennot asentavat kaikki tarvittavat moduulit ja kääntävät sovelluksen (ThunderHub on kirjoitettu TypeScript/React-kielellä).



**3. Päivitä myöhemmin:** ThunderHub tarjoaa useita menetelmiä tulevia päivityksiä varten:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfigurointi (asetukset)



**1. Pääasetustiedosto:** Luo ThunderHub-kansion juureen tiedosto `.env.local`, jolla voit muokata asetuksia (tämä estää asetuksiasi ylittymästä päivitysten aikana). Päämuuttujat [setup documentation](https://docs.thunderhub.io/setup) mukaan:



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Palvelintilien konfigurointi:** Luo kohdassa `ACCOUNT_CONFIG_PATH` määritetty YAML-tiedosto:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Etäkäyttö:** Jos haluat muodostaa yhteyden etä-LND-solmuun, lisää tiedostoon `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Tietoturva:** Ensimmäisen käynnistyksen yhteydessä ThunderHub **automaattisesti** piilottaa `masterPassword` ja kaikki tilien salasanat YAML-tiedostossa, jotta salasanat eivät olisi selvänä tekstinä palvelimella.



**5. Käynnistä ThunderHub:**



```bash
npm start
```



Oletusarvoisesti palvelin kuuntelee porttia 3000. Siirry osoitteeseen `http://localhost:3000` (tai `http://ip-serveur:3000` lähiverkosta).



**6. Docker-vaihtoehto:** ThunderHub tarjoaa virallisia Docker-kuvia:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



ThunderHubin kirjautumissivu tulee näkyviin. Valitse määritetty tili ja anna salasana, jotta pääset kojelautaan.



**Asennus muihin jakeluihin:** Valmiiksi pakatut solmujakelut (RaspiBlitz, MyNode, Start9 jne.) tarjoavat yleensä natiivin ThunderHub-tuen omien hallintaliittymiensä kautta.



**Lisätietoa:** Tutustu täydelliseen viralliseen dokumentaatioon :




- **Asennus:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfigurointi:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Näissä resursseissa kerrotaan yksityiskohtaisesti edistyneistä vaihtoehdoista, kuten SSO-tileistä, salatuista makaronista, TOR-konfiguraatiosta ja paljon muuta.



Kun ThunderHub on asennettu ja käytettävissä, voit hyödyntää kaikkia sen ominaisuuksia. Seuraavassa osiossa tarkastelemme Interface ThunderHubia ja sen eri välilehtiä ja opastamme sinua sen käytössä.



## Interface esittely



Interface ThunderHub on rakennettu päävalikon ympärille (joka näkyy yleensä vasemmanpuoleisessa sarakkeessa), jossa on useita keskeisiä osioita. Kukin vastaa Lightning-solmun hallintaan liittyvää näkökohtaa. Käydään ne läpi yksi kerrallaan:





- **Home** - Home-välilehti, jossa on yleinen kojelauta (yleiskuva solmusta ja pikatoiminnot).
- **Kojelauta** - Mukautettava kojelauta, jossa on widgettejä ja kehittyneitä mittareita.
- **Peers** - Lightning peer management (yhteydet muihin solmuihin).
- **Kanavat** - Salamakanavien yksityiskohtainen hallinta.
- **Rebalance** - Kanavien tasapainottamisväline (kiertomaksut).
- **Tapahtumat** - Salamamaksuhistoria (LN-tapahtumat).
- **Forwards** - Reititystilasto (solmun välittämät maksut).
- **Ketju** - Noden On-Chain-salkku (On-Chain BTC: UTXOs, transaktiot).
- **Amboss** - Integrointi Ambossin kanssa (solmujen seuranta, varmuuskopiot jne.).
- **Työkalut** - Erilaiset työkalut (varmuuskopiot, allekirjoitetut viestit, makaronit, raportit jne.).
- **Vaihto** - On-Chain/Lightning-vaihtotoiminnot Boltzin kautta.
- **Stats** - Laajennetut tilastot ja solmujen suorituskykymittarit.



*(Huomautus: ThunderHub-versiosta riippuen joillakin osioilla voi olla hieman erilaiset otsikot tai lisäominaisuuksia, mutta yleiset periaatteet pysyvät samoina)*



### Home (Yleinen ohjauspaneeli)



ThunderHubin **Koti**-välilehti on etusivu, joka tulee näkyviin kirjautumisen jälkeen. Se sisältää **Yleisen kojelaudan**, joka tarjoaa **yleiskatsauksen** Lightning-solmusi tilasta ja ehdottaa **nopeita toimia** rutiinitoimenpiteitä varten. Näet tyypillisesti seuraavaa:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldot ja kapasiteetti:** Sivun yläosassa ThunderHub näyttää käytettävissä olevat saldosi. Täällä näet tyypillisesti On-Chain-saldon (Bitcoin On-Chain solmun Wallet:ssä, jota symboloi Anchor ⚓) ja Salama-saldon (kanaviesi kapasiteetit, jota symboloi salama Bolt ⚡). Näin saat välittömän käsityksen varoistasi, joita sinulla on On-Chain:ssä ja Salamassa. Jos sinulla on useita tilejä tai kanavia, varmista, että olet oikeassa kanavassa (esim. Mainnet vs. Testnet).





- **Keskeiset tilastot:** Kojelauta voi näyttää joitakin solmun yleisiä mittareita - esimerkiksi avoimien kanavien määrän, yhdistettyjen vertaisverkon käyttäjien määrän, ansaitut reititysmaksut (jos mahdollista) jne. Se on yhteenveto solmun viimeaikaisesta toiminnasta ja kunnosta.





- **Pikatoiminnot:** Kojelaudassa on painikkeita, joiden avulla voit suorittaa yleisimmät tehtävät nopeasti ilman, että sinun tarvitsee selata valikoita. Näitä pikatoimintoja ovat mm:





- **Aave**: Aseta mukautettu Lightning Address Ambossin kautta.
- **Lahjoittaa**: Tee lahjoitus Lightningin kautta.
- Kirjaudu sisään / mene osoitteeseen: Yhdistä Amboss-tiliisi (Quick Connect) ja siirry suoraan **Amboss.space**-sivustolle katsomaan solmusi tietoja.
- **Address**: Kirjoita Lightning Address maksun suorittamista varten.
- **Avaa**: Avaa uusi Lightning-kanava. Napsauttamalla avautuu lomake, johon syötetään sen etäsolmun URI, johon kanava avataan, sekä käytettävä summa ja tarvittaessa On-Chain:n enimmäismaksu.
- **Dekoodaa**: Salama Invoice tai LNURL:n dekoodaaminen nähdäksesi yksityiskohdat ennen maksua.
- **LNURL**: Käsittele LNURL:t Lightning-maksuja tai -nostoja varten.
- **LnMarkets Login**: Kirjaudu sisään LnMarketsiin kaupankäyntiä varten.



Näiden pikatoimintojen avulla voit suorittaa yleisimmät toiminnot suoraan etusivulta ilman, että sinun tarvitsee selata Interface:n eri välilehtiä.



Lyhyesti sanottuna ThunderHubin kojelauta antaa sinulle **nopean katsauksen** solmuun ja antaa sinun suorittaa yleisimmät toiminnot (lähetä/vastaanota, avaa kanava) yhdellä napsautuksella. Se on ihanteellinen lähtökohta päivittäiseen hallinnointiin.



### Kojelauta



**Dashboard**-osio on erillään Home-välilehdestä, ja se tarjoaa edistyneemmän, muokattavissa olevan kojelaudan. Tämän osion avulla voit luoda räätälöidyn näkymän, jossa on erityisiä widgettejä solmupisteen operaattorin tarpeidesi mukaan.





- **Mukautettavat widgetit:** Toisin kuin etusivulla, jolla on kiinteä ulkoasu, Dashboardissa voit valita tarkalleen, mitkä Elements näytetään ja miten ne järjestetään.



![Dashboard sans widgets activés](assets/fr/06.webp)



Jos mitään widgettejä ei ole käytössä, näet viestin "No Widgets Enabled!" (Ei widgettejä käytössä!) ja "Settings" (Asetukset) -painikkeen, jolla pääset mukautusparametreihin.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Asetuksissa voit valita laajan valikoiman widgettejä, jotka on järjestetty luokkiin: "Lightning - Info", "Lightning - Taulukko", "Lightning - Graafi" ja niin edelleen. Kukin widget voidaan aktivoida tai poistaa käytöstä erikseen "Show/Hide"-painikkeilla.



![Bas de la page des paramètres](assets/fr/08.webp)



Asetusten alareunassa on "Kojelaudalle" -painike, jolla voit palata kojelaudalle, ja "Nollaa widgetit" -painike, jolla voit palauttaa oletusnäytön.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Kun kojelauta on määritetty, se voi näyttää erilaisia kaavioita ja mittareita: Maksujen salamakuvaajat, laadittujen laskujen määrä, eteenpäin toimitetut tilastot, yksityiskohtaiset saldot jne.





- **Tarkemmat mittarit:** Pääset käyttämään yksityiskohtaisempia tilastoja solmun suorituskyvystä graafien ja reaaliaikaisten tietojen avulla.





- **Muokattava yleiskuva:** Räätälöi näyttö sopivaksi, olitpa satunnainen käyttäjä tai useita reitityskanavia hallinnoiva ammattilainen.





- **Modulaarinen Interface:** Lisää tai poista widgetejä tarpeen mukaan: etenemiskaaviot, likviditeettimittarit, solmujen terveyshälytykset jne.



Tämä osio on erityisen hyödyllinen edistyneille käyttäjille, jotka haluavat seurata tiettyjä mittareita tai saada teknisemmän yleiskuvan Lightning-solmusta. Se täydentää Home-osiota tarjoamalla enemmän joustavuutta ja hallintaa tietojen näyttämiseen.



### Vertaiset



Osiossa **Peers** luetellaan kaikki Lightning-solmut, jotka ovat tällä hetkellä yhteydessä sinun solmusi vertaisverkkoihin. **Vertainen** on suora solmujen välinen yhteys Lightning Network:ssa. Solmusi voi olla yhteydessä vertaisiin myös ilman avointa kanavaa (esim. vain Exchange:n juorutietoihin verkossa), tai tietysti jokainen avoin kanava merkitsee automaattisesti yhdistettyä vertaista.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Vertaiset-välilehdellä näet :





- **Tietosarakkeet:** Interface näyttää hyödyllisiä tietoja, kuten synkronointitilan, yhteyden tyypin (clearnet tai Tor), pingin, vastaanotetut/lähetetyt satoshit ja vaihdettujen tietojen määrän.
- **Vertaisverkon lisääminen:** ThunderHubin avulla voit muodostaa manuaalisesti yhteyden uuteen vertaisverkkoon oikeassa yläkulmassa olevan **"Lisää"**-painikkeen avulla. Sinun täytyy syöttää solmun URI (muodossa `<julkinen_avain>@<socket>`). Kun se on vahvistettu, ThunderHub lähettää vastaavan `lncli connect`-komennon. Jos solmu on verkossa ja tavoitettavissa, se lisätään vertaisvertaisverkostojen luetteloon.



### Kanavat



**Kanavat**-välilehti on Lightning-kanavien hallinnan ydin. Se on luultavasti se osio, jota käytät useimmin. Siinä esitellään **kaikki Lightning-kanavasi** ja niiden tiedot, ja voit suorittaa hallintatoimia näille kanaville.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Kanavat-sivulla on seuraavat tiedot:





- **Kanavaluettelonäkymä:** Kukin avoin (tai avautuva/sulkeutuva) kanava on lueteltu, ja siinä on yleensä etäsolmun alias, kanavan kokonaiskapasiteetti ja värillinen palkki, joka havainnollistaa paikallisen ja etäluettavan likviditeetin jakautumista. ThunderHub käyttää värikoodia (usein sininen/Green) tai prosenttilukua kanavan tasapainon osoittamiseen: esimerkiksi sininen tarkoittaa paikallista osuutta, Green etäosuutta. Jos kanava on täysin tasapainossa (50/50), palkki on puolet kummastakin väristä. Näin voit tunnistaa yhdellä silmäyksellä, mitkä kanavat ovat epätasapainossa (kaikki sininen = lähes kaikki paikalliset, kaikki Green = lähes kaikki kauko-osuudet).





- **Tietosarakkeet:** Interface näyttää yksityiskohtaiset sarakkeet, mukaan lukien tila, käytettävissä olevat toimet, vertaistiedot, kanavatunnus, kapasiteetti, toiminta, maksut ja saldo graafisella likviditeettinäytöllä.





- **Näytön konfigurointi:** Oikeassa yläkulmassa olevan hammaspyörän avulla voit mukauttaa kanavanäytön mieltymyksiisi sopivaksi.





- **Tila:** Näet myös tilamerkinnät - esim. "Aktiivinen" (kanava on avoinna ja toiminnassa), "Pois päältä" (vertaisverkon yhteys on katkaistu, joten kanava on hetkellisesti käyttökelvoton), "Vireillä" (avaukset tai sulkemiset odottavat On-Chain:n vahvistusta).





- **Toiminnot kanavalla:** ThunderHub tarjoaa kullekin kanavalle toimintopainikkeet (usein kuvakkeiden muodossa):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- Muokkaa maksuja: **Interface:n "Päivitä kanavakäytäntö" -valinnalla voit säätää kaikkia kanavaparametreja: Maksuasetukset: Perusmaksu, maksuprosentti (ppm:nä), CLTV-delta, Max HTLC ja Min HTLC. Näin voit säätää maksukäytäntöjä erikseen kanavakohtaisesti tavoitteena houkutella (tai estää) reititysliikennettä.** *(Huomautus: ThunderHub ei korvaa automaattista maksujenhallintatyökalua, mutta manuaaliseen säätöön se on erittäin tehokas)*
- Sulje kanava (**Sulje**): Interface:n "Suljinkanava" antaa sinulle mahdollisuuden valita joko **yhteistyösuljin** (oletus) tai **pakotettu sulku** (**Pakkosuljin**) määrittelemällä maksut (Sats/vByte). **Tärkeää:** suosi aina yhteistyöhön perustuvaa sulkemista, kun se on mahdollista, jotta vältät On-Chain-tilityksen viivästykset ja korkeammat maksut. ThunderHub kertoo, onko vertaisosaaminen online (yhteistyö mahdollista) vai ei. Jos kyseessä on force close, varmista, että vahvistat sen, sillä se on peruuttamaton ja käynnistää pyyhkäisevän transaktion aikalukolla (yleensä 144 lohkoa tai ~1 päivä Bitcoin Mainnet:ssä).
- **Uuden kanavan avaaminen:** Voit avata uuden kanavan napsauttamalla Kanavat-sivun oikeassa yläkulmassa olevaa hammaspyörää ja valitsemalla sitten "Avaa". Tämän jälkeen voit aloittaa kanavan uudelle tai olemassa olevalle vertaiskumppanille. Tämän sivun käytön etuna on, että sinulla on edessäsi luettelo olemassa olevista kanavistasi, mikä voi auttaa sinua päättämään, mihin haluat avata uuden kanavan.



Lyhyesti sanottuna Kanavat-osiossa voit **hienosäätää jokaista kanavaa**. Täällä määrität likviditeetin jakamisen, päätät, mitkä kanavat säilytetään tai suljetaan, ja asetat kanavakohtaiset reititysparametrit. ThunderHub tarjoaa selkeän Interface:n näitä ratkaisevia solmunhallintatoimintoja varten.



### Uudelleen tasapainottaminen



Välilehti **Rebalance** on tarkoitettu **kanavien tasapainottamiseen**. Tasapainottaminen (tai *tasapainottaminen*) tarkoittaa, että varojen jakoa lähtevien ja tulevien kanavien välillä säädetään uudelleen tekemällä **kiertomaksu** yhdestä kanavasta toiseen kanavaan Lightning Network:n kautta. Näin voit siirtää likviditeettiä liian täydestä kanavasta liian tyhjään kanavaan ilman uusien varojen lisäämistä, jolloin kanavistasi tulee hyödyllisempiä (tasapainossa oleva kanava voi sekä lähettää että vastaanottaa maksuja).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub helpottaa huomattavasti tätä toimintoa, joka muuten olisi työlästä komentorivillä. Tässä kerrotaan, miten Rebalance-osiota käytetään:





- **Alkuperäinen kanavanäkymä:** Kun ThunderHub siirtyy uudelleentasapainotukseen, se näyttää luettelon kanavistasi ja kunkin kanavan saldomittarin (samanlaisen kuin Kanavat-sivulla). Näet heti, mitkä kanavat ovat epätasapainossa. ThunderHub voi lajitella kanavat tasapainon lisääntymisjärjestykseen niin, että kaikkein epätasapainoisimmat kanavat erottuvat luettelon kärjessä (0.0 tarkoittaa täysin paikallisia tai kauko-ohjattavia kanavia).





- **Vertaisverkon valinta:** Interface:n avulla on helppo valita lähtevät ja saapuvat vertaisverkot uudelleentasapainotusta varten.





- **Parametriasetukset:** Voit asettaa :
  - **maksimi** (Sats ja ppm), jonka olet valmis maksamaan
  - **Tasapainotettava määrä** "Kiinteä" tai "Tavoite"-vaihtoehdolla
- **Reitityksessä vältettävät solmut**
- **Reitinhakuun käytettävä enimmäiskokeiluaika**





- Valitse **lähde kanava**: Valitse ensin **lähtevä (lähde)** kanava, eli kanava, josta sinulla on liikaa paikallista likviditeettiä siirrettäväksi. Käytännössä tämä on kanava, jossa paikallinen osuutesi on suuri (> 50 %). Kuvitellaan A-kanava, jossa on 1 000 000 Satssia, joista 900 000 on paikallisia - hyvä ehdokas Satssin lähettämiseen muualle. Klikkaamalla tätä A-kanavaa "lähteväksi" ThunderHub merkitsee sen lähteeksi.





- Valitse **kohdekanava**: Valitse seuraavaksi **tuleva (kohde)** kanava, jonka on saatava likviditeettiä. Tyypillisesti tämä on kanava, jossa tilanne on päinvastainen - suurin osa rahastoista on kaukana (esim. vain 100 000 paikallista Satss 1 000 000:sta). Kun lähdekanava on valittu, ThunderHub lajittelee muut kanavat käänteisessä järjestyksessä (vähenevä saldo) auttaakseen tunnistamaan parhaiten täydentävät kanavat. Valitse B-kanava, jolla on tilaa paikallisella puolella. ThunderHub näyttää tällöin selvästi, mitkä kaksi kanavaa on valittu (lähde A ja kohde B).





- **Aseta maksun määrä ja toleranssi:** Lomakkeella voit syöttää :





  - Uudelleen tasapainotettava **määrä** (Sats:nä). Usein valitsemme määrän, joka vastaa molempien kanavien tasapainoa \~50/50:llä. ThunderHub voi esitäyttää esimerkiksi puolet lähdekanavan ylimääräisestä kapasiteetista.
  - **Maksimi**, jonka olet valmis maksamaan tästä toimenpiteestä (vapaaehtoinen). Maksu ilmaistaan muodossa Sats (kiertoreitityksen kokonaiskustannukset). Jos jätät sen tyhjäksi, ThunderHub etsii reitin kustannuksista riippumatta, mikä ei yleensä ole suositeltavaa (on parempi asettaa raja, esim. 10 Sats pienelle uudelleentasapainotukselle tai maksimi ppm).





- Etsi reitti: Etsi reitti napsauttamalla painiketta. ThunderHub kysyy LND:lta laskeakseen reitin lähdekanavalta verkon kautta omaan kohdekanavaan. Jos se löytää mahdollisen reitin, joka täyttää maksukriteerisi, se näyttää sen ja ilmoittaa yksityiskohtaiset tiedot siirtymisistä ja maksukustannuksista. Se voi esimerkiksi ilmoittaa, että se on löytänyt kolmen hypyn reitin, jossa on yhteensä 2 Sats:n maksua.





- Aloita tasapainotus: Jos olet tyytyväinen ehdotettuun reittiin, napsauta **Tasapainotuskanava**. ThunderHub käynnistää sitten kiertomaksun LND:n kautta. Jos maksu onnistuu, näet ilmoituksen onnistumisesta, ja kanavien A ja B saldot muuttuvat reaaliaikaisesti. ThunderHub päivittää näiden kanavien saldoindikaattorin (mieluiten se on vihreämpi kuin ennen, mikä osoittaa parempaa saldoa).





- **Säädöt ja iteraatiot:** Jos reittiä ei löydy ensimmäisellä yrittämällä (tai jos se on liian kallis), voit säätää parametreja:





  - Kokeile pienempää määrää (joskus osittainen tasapainotus onnistuu, kun taas suuri määrä epäonnistuu).
  - Nosta maksun enimmäismäärää asteittain, mutta varo, ettet maksa maksuja enemmän kuin se on arvokasta.
  - Kokeile vaihtoehtoista reittiä **Vaihda reittiä**-painikkeella, jos se on käytettävissä.
  - Kokeile toista kanavaparia, jos asiat todella käyvät hankaliksi.



ThunderHub tekee prosessista hyvin **intuitiivisen ja visuaalisen**. Vain neljässä vaiheessa (valitse lähtevä kanava, valitse saapuva kanava, määrä, vahvista) voit tehdä sen, mikä aiemmin vaati monimutkaisia manuaalisia komentoja. Työkalu on korvaamaton tasapainoisen solmun ylläpitämisessä, reitityksen suorituskyvyn ja käyttökokemuksen parantamisessa (maksujen lähettäminen ja vastaanottaminen kaikissa kanavissa on helpompaa).



Huomaa lopuksi, että tasapainottaminen kuluttaa reitityskustannuksia (jotka maksetaan välillisille solmuille), joten se on **sijoitus** solmun muuttamiseksi sujuvammaksi. Käytä sitä viisaasti, esimerkiksi tukeaksesi kanavaa usein käyttämääsi palveluun (saapuva likviditeetti) tai tasapainottaaksesi suurta reitityskanavaa. ThunderHubin avulla voit tehdä tämän **yksinkertaisesti ja tehokkaasti**.



### Tapahtumat



ThunderHubin **Tapahtumat**-osio vastaa solmun **Lightning**-tapahtumahistoriaa eli kanavien kautta maksettuja tai vastaanotettuja maksuja ja laskuja. Se on eräänlainen tiliote LN-toiminnoistasi.



![Historique des transactions Lightning](assets/fr/14.webp)



Tästä välilehdestä löydät :





- **Invoice-kuvaaja:** Oikeassa yläkulmassa oleva kuvaaja näyttää vastaanotettujen laskujen kehityksen ajan myötä, jolloin voit havainnollistaa solmun toimintaa.





- Kronologinen luettelo kaikista Lightning-transaktioista, jotka on tehty *solmusta* tai *solmuun*. Jokainen merkintä voi näyttää :





  - Toimenpidetyyppi: **lähetetty maksu** (lähtevä maksu) tai **vastaanotettu maksu** (saapuva, maksetun Invoice:n kautta).
  - Sats:n määrä.
  - Päivämäärä/aika.
  - Maksun tunniste (Hash tai RHash-esikuva) tai kommentti (jos lisäsit muistion Invoice:ään).
- Tilanne: **(esim. maksu odottaa ratkaisua, mutta yleensä LND käsittelee tämän nopeasti, joten "vireillä" on vain vähän On-Chain:n tapahtumiin verrattuna).**



Lyhyesti sanottuna Transactions-osiota käytetään **LN-toimintalokina**. Se on erittäin hyödyllinen, kun haluat tarkistaa, että maksu on mennyt läpi, kuinka paljon maksuja se maksoi tai seurata Lightning-vaihtojesi historiaa. Yhdessä Forwards-osan (kuvattu seuraavaksi) kanssa sinulla on täydellinen näkymä solmusi kautta kulkeneesta rahasta.



### Eteenpäin



Välilehdellä **Lähetys** käsitellään solmusi **reititystoimintaa**, eli maksuja, jotka **kulkevat** kanaviesi kautta (kun toimit Lightning Network:n välittäjänä). Jos käytät solmua reitityssolmuna, tämä on tärkeä osio suorituskykysi seuraamiseksi.



![Statistiques de routage Lightning](assets/fr/15.webp)



Eteenpäin, ThunderHub esittelee :





- **Suodattimet ja näyttövaihtoehdot:** Oikealla ylhäällä olevilla suodattimilla voit lajitella tiedot päivän/viikon/kuukauden/vuoden mukaan ja valita graafisen tai taulukkomuodon.





- **Toimintaviesti:** Jos reititystä ei ole suoritettu valitun ajanjakson aikana, Interface näyttää "Ei eteenpäinlähetyksiä tälle ajanjaksolle", kuten tässä esimerkissä näkyy.





- **Taulukko viimeisimmistä välityksistä**: jokainen merkintä vastaa maksua, joka on **välitetty** solmusi kautta. Kunkin välityksen kohdalla näkyy yleensä :





  - Timestamp,
  - reititetty määrä (Sats:ssa),
  - **tulot** tästä eteenpäinlähetyksestä (Sats:ssa tämä on erotus sen välillä, mitä sait saapuvalta kanavalta ja mitä lähetit lähtevältä kanavalta),
  - käytetyt saapuvat ja lähtevät kanavat (usein tunnistetaan vertaisverkon alias- tai kanavatunnuksella).
  - tila (yleensä *valmistunut* tai epäonnistunut, jos välitys epäonnistui matkalla).





- **Yhteenlasketut tilastot**: ThunderHub laskee ja näyttää sivun yläreunassa tietyn ajanjakson (esim. viimeiset 24 tuntia tai 7 päivää jne., joskus määritettävissä) yhteenlasketut summat ja tilastot.



Lyhyesti sanottuna Forwards-osio tarjoaa **reaaliaikaisen yleiskatsauksen Lightning-solmun reititysaktiviteeteista**. Yhdessä Channels- ja Rebalance-osioiden kanssa tämä muodostaa täydellisen paketin solmun optimointiin: Channels/Rebalance maksuvalmiutta varten, Forwards tulosten (virtojen ja voittojen) tarkkailua varten.



### Ketju



**Ketju**-osio vastaa LND-solmun Bitcoin On-Chain-salkunhallintaa. Tämän Interface:n avulla voit tarkastella ja hallita Bitcoin-varoja, joita käytetään kanavien avaamiseen tai varojen vastaanottamiseen suljetuista kanavista.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Ketjusta löydät :





- Saldo On-Chain: **Näyttää Wallet LND:ssä käytettävissä olevan BTC:n kokonaissaldon.**





- **Luettelo UTXO:** Näytä kaikki käyttämättömät tuotot (UTXO) sekä kunkin tuoton määrä, vahvistukset, Address ja muoto.





- **Tapahtumahistoria:** Yksityiskohtainen taulukko kaikista Bitcoin-tapahtumista, jossa on tyyppi (sisään/ulos), päivämäärä, summa, maksut, vahvistukset, sisällyttämislohko, osoitteet ja txid.



### Amboss



ThunderHub on integroitu **Amboss**-alustaan (amboss.space), joka tarjoaa yksityiskohtaisia tietoja Lightning-solmuista, likviditeettimarkkinapaikan ja hyödyllisiä ominaisuuksia, kuten salatun kanavan varmuuskopioinnin ja saatavuuden valvonnan.



![Intégration Amboss avec ses options](assets/fr/17.webp)



ThunderHubin Amboss-osiossa voit **linkittää** solmun Amboss-tilillesi:





- **Ghost Address:** Aseta solmullesi **yksilöllinen Lightning Address**, joka helpottaa saapuvia maksuja.





- Automaattiset kanavien varmuuskopiot:** Ambossin salattujen kanavien varmuuskopioiden** (SCB-tiedostot) lippulaivaominaisuus. Aktivoi asetuksissa **Ambossin automaattinen varmuuskopiointi = Kyllä**, jotta voit lähettää salattujen varmuuskopioiden päivitykset automaattisesti aina, kun vaihdat kanavaa. Vian sattuessa voit palauttaa varasi tämän ulkoisen varmuuskopion ansiosta.





- **Terveystarkistukset:** Aktivoi **Amboss Healthcheck = Kyllä**, jotta solmusi lähettää säännöllisesti pingejä Ambossille. Saat hälytyksiä, jos solmusi näyttää olevan offline-tilassa.





- Muita ominaisuuksia: Automaattinen saldon siirto, **Magma/Hydro**-integraatio (likviditeettimarkkinapaikka) ja pääsy yksityiskohtaisiin suorituskykytilastoihin.



Amboss-integraatio lisää olennaisen tärkeän **turvallisuuden Layer** automaattisella ulkoisella varmuuskopioinnilla ja käytettävyyden valvonnalla, johon pääsee suoraan ThunderHubista.



### Työkalut



**Työkalut** -osioon on koottu erilaisia kehittyneitä työkaluja solmun hallintaan. Tässä ovat tärkeimmät Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Varmuuskopiot:** Hallitse manuaalisesti kanavan varmuuskopioita (SCB). ThunderHubin avulla voit **ladata kanaviesi täydellisen varmuuskopiotiedoston** (vaihtoehto "Varmuuskopioi kaikki kanavat -> Lataa"). Säilytä tämä `channel-all.bak`-tiedosto turvallisessa paikassa - se on välttämätön, jotta voit palauttaa varasi kaatumisen sattuessa. Voit myös **tuoda** varmuuskopiotiedoston, kun otat solmun uudelleen käyttöön.





- **Kirjanpito:** Vientityökalu talousraportteja varten, mukaan lukien ansaitut/maksetut palkkiot ja tietyn ajanjakson aikana reititetyt määrät.
- **Allekirjoitetut viestit:** Allekirjoita tai vahvista viestit solmun kanssa todistaaksesi Lightning-solmun omistajuus kryptografisen allekirjoituksen avulla.
- Makaroonit (leipomo-osasto):** Hallitse LND** makarooneja räätälöidyn pääsyn luomiseksi. Interface "Leipomo" -osiossa voit valita tarkasti jokaisen käyttöoikeuden: "Lisää tai poista vertaisia", "Luo ketjuosoitteita", "Luo laskuja", "Luo makaroneja", "Johdanna avaimia", "Hae käyttöoikeusavaimia", "Hae ketjutapahtumia", "Hae laskuja", "Hae Wallet tietoja", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages", ja niin edelleen. Jokainen lupa voidaan aktivoida erikseen "Kyllä/Ei"-painikkeilla, jolloin voidaan luoda räätälöity makaroni.
- **Järjestelmätiedot:** Wallet-version ja aktivoitujen RPC:iden näyttö.



Lyhyesti sanottuna Työkalut-osiossa on yhdistetty edistyneet hallintatoiminnot - varmuuskopiot, kirjanpito, tietoturva ja käyttöoikeuksien hallinta - yhtenäiseen Interface:ään.



### Vaihda



ThunderHubin **Swap**-välilehdellä voit vaihtaa Lightning-satoshit Bitcoin On-Chain:een Boltz-palvelun kautta. Tämä ominaisuus on hyödyllinen ylimääräisen Lightning-likviditeetin "dumppaamiseen" kanavaan sulkematta kanavaa.



![Interface de swap via Boltz](assets/fr/19.webp)



Prosessi on yksinkertainen:





- **Määrä**: Määritä vaihdettava määrä
- **Address**: Syötä Bitcoin vastaanotto Address
- **Toteutus**: ThunderHub kommunikoi Boltzin kanssa käsitelläkseen Exchange:n automaattisesti



**Hyötyjä:**




- Muu kuin huoltajapalvelu (ei rahahuoltoa)
- Säilytä nykyiset kanavasi
- Helppokäyttöinen integroitu Interface



Boltz veloittaa pienen palkkion, ja sinä maksat tavanomaisen Bitcoin-tapahtumamaksun. ThunderHub näyttää kaikki kustannukset ennen vahvistusta.



### Tilastot



ThunderHubin **Tilastot** -osio tarjoaa **edistyneitä tilastoja** Lightning-solmusta suorituskyvyn analysoimiseksi ja reitityksen optimoimiseksi.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Tämä osio on olennaisen tärkeä kustannusten optimoimiseksi, menestyksekkäiden kanavien tunnistamiseksi ja solmun laajentamisen suunnittelemiseksi.



## Päätelmä



**ThunderHub** on vakiinnuttanut asemansa Lightning **LND** -solmun helppoon hallintaan välttämättömänä työkaluna. Tämä nykyaikainen Interface tarjoaa kaikki olennaiset toiminnot: kanavien hallinta, maksut, seuranta ja lisäominaisuudet, kuten automaattisen tasapainotuksen ja Amboss-integraation.



**Keskeiset edut:**




- Interface tyylikäs ja intuitiivinen
- Tehokkaat työkalut (tasapainottaminen, Boltz-vaihdot, automaattiset varmuuskopiot)
- Yhteensopiva Umbrelin, Voltagen, RaspiBlitzin ja muiden jakeluiden kanssa



ThunderHub demokratisoi kehittyneen Lightning-solmujen hallinnan ja mahdollistaa sen, mikä aiemmin vaati monimutkaisia teknisiä komentoja. Olitpa sitten aloittelija tai kokenut operaattori, ThunderHubin avulla voit hallita Lightning-solmua tehokkaasti nykyaikaisen, kattavan Interface:n kautta.



## Resurssit



**Viralliset linkit:**




- **Virallinen verkkosivusto:** [thunderhub.io](https://thunderhub.io)
- **Dokumentaatio:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **GitHub-lähdekoodi:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)