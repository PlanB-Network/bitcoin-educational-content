---
name: ThunderHub
description: Interface Välgussõlmede haldamise veeb LND
---
![cover](assets/cover.webp)



## Sissejuhatus



ThunderHub on **avatud lähtekoodiga Lightning-sõlmede (LND)** haldur, mis pakub intuitiivset Interface, millele on juurdepääs mis tahes seadmest või brauserist.



** Peamised omadused:**




- **Järelevalve**: Saldode, kanalite, tehingute ja marsruutimisstatistika üldine vaade
- **Juhtimine**: Kanalite avamine/sulgemine, sissetulevad/väljaminevad maksed, kanalite tasakaalustamine
- **Integratsioonid**: LNURL tugi, vahetused Boltz'i kaudu, Amboss varundamine
- **Interface reageerib**: Ühildub mobiili, tahvelarvuti ja lauaarvuti seadmetega tumedate/heledate teemadega



ThunderHub integreerub hõlpsasti **Umbrel**, **Voltage**, **RaspiBlitz** ja **MyNode**, lihtsustades teie sõlme igapäevast haldamist.



**ThunderHub sobib eriti hästi operaatoritele, kes otsivad ergonoomilist Interface kanalite haldamiseks, likviidsuse kontrollimiseks (tasakaalustamine), tehingute jälgimiseks ja kolmandate osapoolte teenuste, nagu Amboss, integreerimiseks. Turvalisus on tagatud kohaliku või Tor-ühenduse kaudu.**



Kui teil ei ole veel Lightning-sõlme, soovitame teil jälgida meie LND vihmavarju õpetust:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Paigaldamine



ThunderHubi saab paigaldada mitmel erineval viisil, sõltuvalt teie Lightning-sõlme hostingukeskkonnast. Kas kasutate valmislahendust (Umbrel, Voltage, RaspiBlitz, MyNode, Start9 jne) või käsitsi paigaldamist, ThunderHub on sageli ilma suurema vaevata saadaval. Järgnevalt kirjeldame kahte levinud lähenemisviisi: Umbrel App Store'i kaudu ja käsitsi paigaldamise kaudu (kohaldatav serverile või isehostitavale jaotusele).



### Paigaldamine vihmavarju kaudu



Umbrel integreerib ThunderHubi oma **App Store'i**, mis muudab installimise äärmiselt lihtsaks. Ei ole vaja käsurea või käsitsi seadistamist: kõik toimub Interface Umbreli kaudu. Järgige lihtsalt neid samme:





- **Avage Umbrel armatuurlaud**: Ühendage oma Umbreli sõlme Interface veebiga (nt `http://umbrel.local` oma kohalikus võrgus või selle `.onion` Address kaudu, kui kasutate Tor'i).
- **Juurdepääs App Store'ile**: Umbreli peamenüüs klõpsake "App Store" (või "App"). Otsige saadaval olevate rakenduste nimekirjast **ThunderHub**.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- Paigaldage **ThunderHub**: Klõpsake ThunderHubi rakendusel ja seejärel nupul install. Vajaduse korral kinnitage. Umbrel laeb automaatselt alla ja paigaldab ThunderHubi teie sõlme.





- **Käivitage rakendus**: Kui paigaldus on lõpule viidud (mõned kümned sekundid), ilmub ThunderHub teie avalehele. Selle avamiseks klõpsake ikoonil. ThunderHub käivitub teie brauseris.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Tähtis:** Kui ThunderHub esimest korda avatakse, kuvatakse automaatselt sisselogimiseks vajalik **eelistatud parool**. Valik "Ära näita seda uuesti" võimaldab teil seda kuvamist tulevaste ühenduste puhul varjata. **Soovitame tungivalt:**




- **Salvesta see parool kohe** oma paroolihaldurisse
- Kopeeri see kasutamiseks järgmises etapis
- Märkige "Ära näita seda uuesti", kui parool on salvestatud



![Page de connexion de ThunderHub](assets/fr/03.webp)



Seejärel suunatakse teid sisselogimise lehele, kus peate Interface avamiseks sisestama eelmises etapis kopeeritud parooli.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel hoolitseb taustal ThunderHubi varustamise eest LND ühendusinfoga (TLS-sertifikaat, administreerimismakroon jne), nii et te ei pea tegema mingeid täiendavaid seadistusi. Vaid paari klikiga on ThunderHub teie Umbrel-sõlmes käivitatud ja käivitatud.



### Käsitsi paigaldamine (isehostitav, välja arvatud Umbrel)



Väljaspool Umbrelit (nt isiklikul serveril, Raspberry Pi koos RaspiBlitziga või *iseseisva* paigaldusega) on ThunderHubi paigaldamiseks vaja teha mõned lisatoimingud. Järgnevalt kirjeldame installeerimist lähtekoodist ja konfiguratsiooni vastavalt [ametlikule ThunderHubi dokumentatsioonile](https://docs.thunderhub.io).



#### Paigaldamine



**Eeldused:** Veenduge, et teie süsteem vastab miinimumnõuetele vastavalt [dokumentatsiooni seadistamine](https://docs.thunderhub.io/setup):




- **Node.js** versioon 18 või uuem
- **npm** paigaldatud
- Juurdepääs LND autentimisfailidele :
  - LND TLS sertifikaat (`tls.cert`)
  - LND administreerimise makaron (`admin.macaroon`)
  - LND gRPC teenus Address (hostname:port) (vaikimisi `127.0.0.0.1:10009` kohapeal)



**1. Hankige ThunderHubi kood:** Kloonige projekti GitHubi repositoorium, nagu on kirjeldatud [paigaldusdokumentatsioonis](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. paigaldage sõltuvused ja ehitage rakendus:**



```bash
npm install
npm run build
```



Need käsud installivad kõik vajalikud moodulid ja seejärel kompileerivad rakenduse (ThunderHub on kirjutatud TypeScript/React keeles).



**3. Hilisem uuendamine:** ThunderHub pakub mitmeid meetodeid tulevaste uuenduste tegemiseks:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfigureerimine (seadistamine)



**1. Põhikonfiguratsioonifail:** Looge ThunderHubi kausta juurest fail `.env.local`, et kohandada konfiguratsiooni (see takistab teie seadete ülekirjutamist uuenduste ajal). Peamised muutujad vastavalt [setup documentation](https://docs.thunderhub.io/setup):



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



**2. Serveri kontode konfiguratsioon:** Luua YAML-faili, mis on määratud `ACCOUNT_CONFIG_PATH` :



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



**3. Kaugjuurdepääs:** Kaugse LND sõlme ühendamiseks lisage faili `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Turvalisus:** Esimesel käivitamisel peidab ThunderHub **automaatselt** YAML-faili "masterPassword" ja kõik kontode paroolid, et vältida paroolide olemasolu serveris selge tekstina.



**5. ThunderHubi käivitamine:**



```bash
npm start
```



Vaikimisi ootab server pordil 3000. Pöörduge `http://localhost:3000` (või `http://ip-serveur:3000` kohalikust võrgust).



**6. Dockeri alternatiiv:** ThunderHub pakub ametlikke Dockeri kujutisi:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Ilmub ThunderHubi sisselogimisleht. Valige konfigureeritud konto ja sisestage parool, et pääseda juhtpaneelile.



**Installatsioon muudesse distributsioonidesse:** Esipakendatud sõlmedistributsioonid (RaspiBlitz, MyNode, Start9 jne) pakuvad tavaliselt oma administreerimisliidese kaudu ThunderHubi tuge.



**Lisateabe saamiseks:** Vaadake täielikku ametlikku dokumentatsiooni :




- **Paigaldamine:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfiguratsioon:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Need ressursid kirjeldavad üksikasjalikult selliseid täiustatud võimalusi nagu SSO-kontod, krüpteeritud makaronid, TOR-konfiguratsioon ja palju muud.



Kui ThunderHub on paigaldatud ja juurdepääsetav, olete valmis kasutama kõiki selle funktsioone. Järgnevalt tutvustame Interface ThunderHubi ja selle erinevaid vahekaarte, et juhendada teid selle kasutamisel.



## Interface esitlus



Interface ThunderHub on üles ehitatud peamenüü ümber (tavaliselt kuvatakse vasakpoolses veerus), mis koosneb mitmest põhiosast. Iga jaotis vastab teie Lightning-sõlme haldamise aspektile. Käime need ükshaaval läbi:





- **Avaleht** - Avaleht, kus on üldine armatuurlaud (ülevaade teie sõlme ja kiirtehingute kohta).
- **Armatuurlaud** - Kohandatav armatuurlaud koos vidinate ja täiustatud mõõdikutega.
- **Peers** - Lightning peer management (ühendused teiste sõlmedega).
- **Kanalid** - välgukanalite üksikasjalik haldamine.
- **Rebalance** - kanalite tasakaalustamise vahend (ringmaksed).
- **Tehingud** - välkmaksete ajalugu (LN tehingud).
- **Edasi** - marsruutimisstatistika (teie sõlme poolt edastatud maksed).
- **Kett** - Node'i On-Chain portfell (On-Chain BTC: UTXOs, tehingud).
- **Amboss** - integratsioon Ambossiga (sõlmede jälgimine, varundamine jne).
- **Tööriistad** - mitmesugused tööriistad (varukoopiad, allkirjastatud sõnumid, makaronid, aruanded jne).
- **Vahetus** - On-Chain/Lightning vahetusfunktsioonid Boltzi kaudu.
- **Stats** - Täiustatud statistika ja sõlmede jõudlusnäitajad.



*(Märkus: sõltuvalt ThunderHubi versioonist võivad mõned jaotised olla veidi teistsuguste pealkirjade või lisafunktsioonidega, kuid üldpõhimõtted jäävad samaks)*



### Avaleht (üldine juhtpaneel)



ThunderHubi vahekaart **Kodu** on avaleht, mis ilmub pärast sisselogimist. See sisaldab **Üldine juhtpaneel**, mis annab **ülevaate** teie Lightning-sõlme olekust ja pakub **pikameetmeid** rutiinseteks toiminguteks. Tavaliselt leiate siit järgmist:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldod ja mahud:** Lehe ülaosas näitab ThunderHub teie olemasolevaid saldosid. Siin näete tavaliselt On-Chain saldot (Bitcoin On-Chain sõlme Wallet, mida sümboliseerib Anchor ⚓) ja Lightning saldot (teie kanalite võimsused, mida sümboliseerib välk Bolt ⚡). See annab teile otsese ettekujutuse teie vahenditest On-Chain ja Lightning. Kui teil on mitu kontot või kanalit, veenduge, et teil on õige konto (nt Mainnet vs Testnet).





- **Põhistatistika:** Armatuurlaual saab kuvada teie sõlme kohta mõningaid üldisi näitajaid - näiteks avatud kanalite arv, ühendatud eakaaslaste arv, teenitud marsruutimistasud (kui see on kohaldatav) jne. See on kokkuvõte sõlme hiljutisest aktiivsusest ja tervisest.





- **Kiiretoimingud:** Armatuurlaual on nupud kõige tavalisemate ülesannete kiireks täitmiseks, ilma et oleks vaja menüüdes navigeerida. Need kiiretoimingud hõlmavad järgmist:





- **Kummitus**: Seadistage Amboss'i kaudu kohandatud Lightning Address.
- **Annetada**: Tehke annetus välklambi kaudu.
- **Logi sisse/kuuluta**: Ühendage oma Amboss'i kontoga (Quick Connect) ja minge otse Amboss.space'i, et vaadata oma sõlme teavet.
- **Address**: Makse tegemiseks sisestage Lightning Address.
- **Avatud**: Avage uus Lightning-kanal. Klõpsates avaneb vorm, kuhu sisestatakse selle kaugsõlme URI, millele kanal avada, ning summa ja vajaduse korral maksimaalne On-Chain tasu, mida tuleb kasutada.
- **Dekodeeri**: Dekodeerige Lightning Invoice või LNURL, et vaadata üksikasju enne maksmist.
- **LNURL**: Töötlema LNURLi välkmaksete või väljamaksete tegemiseks.
- **LnMarkets sisselogimine**: Logi sisse LnMarkets kauplemiseks.



Need kiirtoimingud võimaldavad teil teostada kõige sagedamini kasutatavaid toiminguid otse avalehelt, ilma et peaksite navigeerima Interface eri vahekaartide vahel.



Lühidalt öeldes annab ThunderHubi armatuurlaud teile **kiire ülevaate** oma sõlme kohta ja võimaldab teil teha kõige sagedasemad toimingud (saatmine/vastuvõtmine, kanali avamine) ühe klõpsuga. See on ideaalne lähtepunkt igapäevaseks haldamiseks.



### Armatuurlaud



Jaotis **Dashboard** on vahekaardist Home eraldi ja pakub täiustatud, kohandatavat armatuurlauda. See jaotis võimaldab teil luua kohandatud vaate koos konkreetsete vidinatega vastavalt teie kui sõlmeoperaatori vajadustele.





- **Kohandatavad vidinad:** Erinevalt avalehelt, millel on fikseeritud paigutus, saate juhtpaneelil täpselt valida, milliseid Elements kuvada ja kuidas neid korraldada.



![Dashboard sans widgets activés](assets/fr/06.webp)



Kui vidinaid ei ole lubatud, kuvatakse teade "No Widgets Enabled!" ja nupp "Settings", mille abil pääseb kohandamisparameetritele ligi.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Seadetes saate valida paljude kategooriatesse jaotatud vidinate vahel: "Lightning - Info", "Lightning - Tabel", "Lightning - Graafik" jne. Iga vidinat saab eraldi aktiveerida või deaktiveerida nuppude "Show/Hide" abil.



![Bas de la page des paramètres](assets/fr/08.webp)



Seadete alt leiate nupu "To Dashboard", et naasta armatuurlauale, ja nupu "Reset Widgets", et lähtestada vaikimisi kuvamine.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Pärast seadistamist saab teie armatuurlaual kuvada erinevaid graafikuid ja mõõdikuid: Välkmaksete graafikud, väljastatud arvete arv, edasisuunamisstatistika, üksikasjalikud saldod jne.





- **Täiustatud mõõdikud:** Juurdepääs üksikasjalikumale statistikale sõlme jõudluse kohta koos graafikute ja reaalajas andmetega.





- **Konfigureeritav ülevaade:** Kohandage ekraan vastavalt sellele, kas olete juhuslik kasutaja või professionaalne operaator, kes haldab mitut marsruutimiskanalit.





- **Modulaarne Interface:** Lisage või eemaldage vidinaid vastavalt vajadusele: edasisuunamisgraafikud, likviidsusmõõdikud, sõlmede tervisehoiatused jne.



See jaotis on eriti kasulik edasijõudnud kasutajatele, kes soovivad jälgida konkreetseid näitajaid või saada oma Lightning-sõlme kohta tehnilist ülevaadet. See täiendab jaotist Home, pakkudes suuremat paindlikkust ja kontrolli teabe kuvamise üle.



### Eakaaslased



Jaotises **Peers** on loetletud kõik Lightning-sõlmed, mis on praegu teiega ühendatud kui partnerid. **Võrdluspartner** on Lightning Network-sõlmede vaheline otsene ühendus. Teie sõlm võib olla ühendatud eakaaslastega ka ilma avatud kanalita (nt lihtsalt Exchange kuulujututeabega võrgus), või muidugi tähendab iga avatud kanal automaatselt ühendatud eakaaslast.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Vahelehel näete :





- **Teabesambad:** Interface kuvab kasulikke andmeid, nagu sünkroniseerimise staatus, ühenduse tüüp (clearnet või Tor), ping, vastuvõetud/saadetud satoshid ja vahetatud andmete maht.
- **Peer'i lisamine:** ThunderHub võimaldab teil käsitsi uue peer'iga ühenduda **"Lisa"** nupu abil üleval paremas nurgas. Sa pead sisestama sõlme URI (formaat `<avalik_võti>@<socket>`). Pärast valideerimist saadab ThunderHub vastava käsu `lncli connect`. Kui sõlm on võrgus ja kättesaadav, lisatakse see teie partnerite nimekirja.



### Kanalid



Vahekaart **Kanalid** on Lightning'i kanalite haldamise süda. See on tõenäoliselt jaotis, mida te kõige sagedamini kasutate. See näitab **kõik milliseid teie Lightning-kanaleid** koos nende üksikasjadega ning võimaldab teil nende kanalite haldamistoiminguid teha.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Kanalite lehel leiate järgmist:





- **Kanalite loendi vaade:** Iga avatud (või avanev/sulgev) kanal on loetletud, tavaliselt koos kaugkeskuse aliasiga, kanali koguvõimsusega ja värvilise ribaga, mis näitab kohaliku ja kaugliikuvuse jaotust. ThunderHub kasutab kanali tasakaalu näitamiseks värvikoodi (sageli sinine/Green) või protsenti: näiteks sinine tähistab teie kohalikku osakaalu, Green kaugosakut. Kui kanal on täiesti tasakaalus (50/50), on tulp mõlemast värvist pool. See võimaldab teil ühe pilguga tuvastada, millised kanalid on tasakaalustamata (kõik sinised = peaaegu kõik kohalikud, kõik Green = peaaegu kõik kaugkanalid).





- **Teabesambad:** Interface kuvab üksikasjalikud veerud, sealhulgas olek, olemasolevad tegevused, partnerite andmed, kanali ID, võimsus, aktiivsus, tasud ja saldo koos graafilise likviidsuse kuvamisega.





- **Ekraani konfigureerimine:** Paremas ülemises nurgas asuv hammasratas võimaldab teil kohandada kanali kuvamist vastavalt oma eelistustele.





- **Staatus:** Näete ka staatuse indikaatoreid - nt "Aktiivne" (kanal on avatud ja töökorras), "Offline" (partner on lahti ühendatud, nii et kanal on hetkel kasutamiskõlbmatu), "Ootel" (avamise või sulgemise puhul ootab On-Chain kinnitust).





- **Tegevused kanalil:** ThunderHub pakub iga kanali jaoks tegevusnuppe (sageli ikoonide kujul):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Muuda tasusid:** Interface "Update Channel Policy" võimaldab teil kohandada kõiki kanali parameetreid: Põhitasu, tasumäär (ppm), CLTV delta, Max HTLC ja Min HTLC. See võimaldab teil kohandada oma tasupoliitikat individuaalselt iga kanali kohta, eesmärgiga meelitada (või heidutada) marsruutimisliiklust. *(Märkus: ThunderHub ei asenda automaatset tasude haldamise vahendit, kuid käsitsi reguleerimiseks on see väga tõhus)*
- Sulge kanal (**Sulge**): Interface "Sulge kanal" annab teile võimaluse valida **kooperatiivse sulgemise** (vaikimisi) või **vajutatud sulgemise** (*Force Close*) vahel, määratledes tasud (Sats/vByte). **Tähtis:** Eelistage võimaluse korral alati kooperatiivset sulgemist, et vältida On-Chain arveldamise viivitusi ja suuremaid tasusid. ThunderHub ütleb teile, kas vastaspool on võrgus (võimalik koostöö) või mitte. Force close'i korral kinnitage kindlasti, sest see on pöördumatu ja käivitab pühkimistehingu koos timelockiga (tavaliselt 144 plokki või ~1 päev Bitcoin Mainnet puhul).
- **Uue kanali avamine:** Uue kanali avamiseks klõpsake kanalite lehe paremal ülaosas oleval hammasrattaotsikul ja valige "Ava". Seejärel saate algatada kanali uuele või olemasolevale eakaaslasele. Selle lehe kasutamise eelis on see, et teil on ees nimekiri olemasolevatest kanalitest, mis aitab teil otsustada, kus uut kanalit avada.



Lühidalt öeldes annab kanalite sektsioon teile **täpse kontrolli iga kanali üle**. Siin saate juhtida likviidsuse jaotust, otsustada, milliseid kanaleid hoida või sulgeda, ja määrata kanalite marsruutimise parameetrid. ThunderHub pakub nende ülioluliste sõlme haldamise toimingute jaoks selget Interface.



### Uuesti tasakaalustamine



Vahekaart **Rebalance** on pühendatud **kanalite tasakaalustamisele**. Tasakaalustamine (või *tasakaalustamine*) hõlmab vahendite jaotuse korrigeerimist teie väljaminevate ja sissetulevate kanalite vahel, tehes Lightning Network kaudu **ringmakse** ühest teie kanalist teise kanalisse. See võimaldab teil ilma uusi vahendeid sisse toomata nihutada likviidsust liiga täis kanalilt liiga tühjale kanalile, muutes teie kanalid kasulikumaks (tasakaalustatud kanal saab nii makseid saata kui ka vastu võtta).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub lihtsustab seda toimingut oluliselt, mis muidu oleks käsureal tüütu. Siin on kirjeldatud, kuidas kasutada jaotist Rebalance:





- **Esialgne kanali vaade:** Uuesti tasakaalustamisse sisenedes kuvab ThunderHub teie kanalite nimekirja, kus iga kanali kohta on tasakaalunäitaja (sarnaselt kanalite lehel olevale). Näete kohe, millised kanalid on tasakaalust väljas. ThunderHub saab kanalid sorteerida tasakaalu suurenemise järjekorras, nii et kõige tasakaalustamata kanalid paistavad nimekirja ülaosas (0,0 tähendab täielikult kohalikke või kaugkasutatavaid kanaleid).





- **Peeride valik:** Interface võimaldab lihtsasti valida väljaminevad ja sissetulevad peerid tasakaalustamiseks.





- **Parameetri seaded:** Saate määrata :
  - **maksimaalne tasu** (Sats ja ppm), mida olete valmis maksma
  - **Tasakaalustatav summa** valikuga "Fikseeritud" või "Eesmärk"
- **Sõlmed, mida tuleb marsruutimisel vältida**
- **Maksimaalne katseaeg** marsruudi leidmiseks





- Valige **allikas** kanal: Valige kõigepealt **väljaminev (allikas)** kanal, st kanal, millest teil on liiga palju kohalikku likviidsust, et seda liigutada. Praktikas on see kanal, kus teie kohalik osakaal on suur (> 50%). Kujutame ette A-kanalit, kus on 1 000 000 Satss, millest 900 000 on kohalik - hea kandidaat Satsside saatmiseks mujale. Klõpsates sellel A-kanalil kui "väljamineval", märgistab ThunderHub selle allikaks.





- Valige **sihtkanal**: Järgmisena valige **saabuv (siht)** kanal, mis peab saama likviidsust. Tavaliselt on see kanal, kus see on vastupidi - enamik vahendeid on kaugemal (nt ainult 100 000 kohalikku Satsi 1 000 000-st). ThunderHub sorteerib pärast lähtekanali valimist teised kanalid vastupidises järjekorras (vähenev tasakaal), et aidata tuvastada kõige täiendavamad kanalid. Valige B-kanal, millel on ruumi kohalikul poolel. ThunderHub näitab seejärel selgelt, millised kaks kanalit on valitud (allikas A ja sihtpunkt B).





- **Tasu summa ja tolerantsi määramine:** Vorm võimaldab sisestada :





  - Ümber tasakaalustatav **summa** (Sats). Sageli valime summa, mis on võrdne sellega, mis tasakaalustaks mõlemad kanalid \~50/50. ThunderHub saab näiteks pool allikakanali ülemäärasest võimsusest eeltäita.
  - **maksimaalne tasu**, mida olete valmis selle toimingu eest maksma (vabatahtlik). See tasu on väljendatud Sats (ringristmiku marsruutimise kogukulu). Kui jätate selle tühjaks, otsib ThunderHub teekonda maksumusest sõltumata, mis ei ole üldiselt soovitatav (parem on seada piir, nt 10 Sats väikese ümberpööramise puhul või maksimaalne ppm).





- **Marsruudi leidmine:** Marsruudi leidmiseks klõpsake nupule. ThunderHub küsib LND-lt, et arvutada marsruut teie lähtekanalist läbi võrgu teie enda sihtkanalini. Kui ta leiab võimaliku marsruudi, mis vastab teie tasukriteeriumidele, kuvab ta selle koos üksikasjadega hüpete ja tasukulude kohta. Näiteks võib see näidata, et ta on leidnud 3-hobujõulise tee, mille tasudeks on kokku 2 Sats.





- Alusta tasakaalustamist: Kui oled kavandatud marsruudiga rahul, klõpsa **Tasakaalukanal**. Seejärel algatab ThunderHub LND kaudu ringmakse. Kui makse on edukas, näete teate õnnestumise kohta ning kanalite A ja B saldod muutuvad reaalajas. ThunderHub ajakohastab nende kanalite saldoindikaatorit (ideaalis on see rohelisem kui varem, mis näitab paremat saldot).





- **Kohandused ja iteratsioonid:** Kui marsruuti ei leita esimesel katsel (või kui see on liiga kallis), saate parameetreid kohandada:





  - Proovige väiksemat summat (mõnikord läheb osaline tasakaalustamine läbi, samas kui suur summa ebaõnnestub).
  - Suurendage maksimaalset tasu järk-järgult, kuid olge ettevaatlik, et mitte maksta rohkem tasu, kui see on väärt.
  - Kasutage nuppu **Võta teine marsruut**, kui see on saadaval, et proovida alternatiivset marsruuti.
  - Proovige teist paari kanaleid, kui asi tõesti takerdub.



ThunderHub muudab protsessi väga **intuitiivseks ja visuaalseks**. Vaid 4 sammuga (valige väljaminev kanal, valige sissetulev kanal, summa, valideerige) saate teha seda, mis varem nõudis keerulisi käsitsikorraldusi. See tööriist on hindamatu väärtusega tasakaalustatud sõlme säilitamisel, parandades teie marsruutimise tulemuslikkust ja kogemust (lihtsam makseid saata ja vastu võtta kõigis teie kanalites).



Lõpetuseks, pange tähele, et tasakaalustamine kulutab marsruutimiskulusid (mis makstakse vahendatud sõlmedele), seega on see **investeering**, et muuta sõlme sujuvamaks. Kasutage seda targalt, näiteks selleks, et toetada kanalit teenusele, mida kasutate sageli (sissetulev likviidsus), või et tasakaalustada suurt marsruutimiskanalit. ThunderHub võimaldab teil seda teha **lihtsalt ja tõhusalt**.



### Tehingud



ThunderHubi jaotis **Tehingud** vastab teie sõlme **Lightning** tehingute ajaloole, st kanalite kaudu makstud või saadud maksetele ja arvetele. See on teie LN toimingute omamoodi konto väljavõte.



![Historique des transactions Lightning](assets/fr/14.webp)



Sellel vahekaardil leiate :





- **Invoice graafik:** Paremas ülemises nurgas olev graafik näitab saadud arvete arengut aja jooksul, mis võimaldab teil visualiseerida oma sõlme tegevust.





- Kronoloogiline nimekiri kõigist Lightning-tehingutest, mis on tehtud *sõlme* või *sõlme* kaudu. Iga kirje võib näidata :





  - Tegevuse tüüp: **saadetud makse** (väljaminev makse) või **saadud makse** (sissetulev makse, tasulise Invoice kaudu).
  - Summa Sats.
  - Kuupäev/kellaaeg.
  - Makse ID (Hash või RHash eelpilt) või kommentaar (kui lisasite Invoice-le märkuse).
- Staatus: **(nt lahendamist ootav makse, kuid üldiselt menetleb LND seda kiiresti, nii et võrreldes On-Chain tehingutega on siin vähe "ootel").**



Lühidalt öeldes on tehingute osa teie **LN tegevuspäevik**. See on väga kasulik, et kontrollida, kas makse on läbi läinud, kui palju tasusid see maksis või jälgida oma Lightning-vahetuste ajalugu. Koos jaotisega Forwards (mida kirjeldatakse allpool) on teil täielik ülevaade teie sõlme läbinud rahast.



### Edasi



Vahekaardil **Väljundid** käsitletakse teie sõlme **rutiini** tegevust, st makseid, mis **läbivad** teie kanalite kaudu (kui te tegutsete Lightning Network vahendava sõlmpunktina). Kui te kasutate oma sõlme marsruutimise sõlmpunktina, on see jaotis oluline teie tegevuse jälgimiseks.



![Statistiques de routage Lightning](assets/fr/15.webp)



Edasi, ThunderHub esitleb :





- **Filtrid ja kuvamisvõimalused:** Paremal üleval olevad filtrid võimaldavad sorteerida andmeid päeva/nädala/kuu/aasta järgi ning valida graafilise või tabeli kujulise kuvamise vahel.





- **Tegevusteade:** Kui valitud ajavahemiku jooksul ei ole marsruutimist teostatud, kuvab Interface "No forwards for this period", nagu on näidatud käesolevas näites.





- **Tabel hiljutistest edastustest**: iga kirje vastab maksele, mis on **edastatud** teie sõlme kaudu. Iga edasisaatmise puhul näeme tavaliselt :





  - Timestamp,
  - suunatav summa (Sats),
  - selle edastamise eest teenitud **tasu** (Sats puhul on see erinevus sissetuleval kanalil saadud ja väljamineval kanalil saadetud summade vahel),
  - kasutatavad sissetulevad ja väljaminevad kanalid (sageli identifitseeritud vastastikusest aliasist või kanali ID-st).
  - staatus (tavaliselt *täidetud* või ebaõnnestumine, kui edastamine teel ebaõnnestus).





- **Koondstatistika**: ThunderHub arvutab ja kuvab lehe ülaosas kokkuvõtteid ja statistikat teatud ajavahemiku kohta (nt viimased 24 tundi või 7 päeva jne, mõnikord seadistatav).



Lühidalt öeldes pakub jaotis Forwards **reaalajas ülevaadet teie Lightning-sõlme marsruutimisaktiivsusest**. Koos jaotiste Channels ja Rebalance osadega moodustab see tervikliku paketi teie sõlme optimeerimiseks: Channels/Rebalance likviidsuse jaoks, Forwards tulemuste (voogude ja kasumi) jälgimiseks.



### Kett



Jaotis **Kett** vastab teie LND-sõlme Bitcoin On-Chain portfellihaldusele. See Interface võimaldab teil vaadata ja hallata Bitcoin vahendeid, mida kasutatakse kanalite avamiseks või suletud kanalite vahendite vastuvõtmiseks.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Kettas leiate :





- Saldo On-Chain: **Kuvab Wallet LND olemasoleva BTC kogusaldo.**





- **UTXO nimekiri:** Vaadake kõiki kasutamata väljundeid (UTXO) koos summa, kinnituste, Address ja vorminguga iga väljundi kohta.





- **Tehingute ajalugu:** Üksikasjalik tabel kõigi Bitcoin tehingute kohta koos tüübi (sisse/välja), kuupäeva, summa, tasude, kinnituste, lisabloki, aadresside ja txid-ga.



### Amboss



ThunderHub on integreeritud platvormiga **Amboss** (amboss.space), mis pakub üksikasjalikku teavet Lightning-sõlmede kohta, likviidsusturgu ja kasulikke funktsioone, nagu krüpteeritud kanalite varundamine ja kättesaadavuse jälgimine.



![Intégration Amboss avec ses options](assets/fr/17.webp)



ThunderHubi Amboss'i sektsioon võimaldab teil **liita** oma sõlme oma Amboss'i kontoga:





- **Ghost Address:** Seadistage oma sõlme jaoks **isikupärastatud Lightning Address**, mis hõlbustab sissetulevaid makseid.





- Automaatne kanali varundamine:** Krüpteeritud kanali varundamine** (SCB-failid) Ambossil. Aktiveerige seadetes **Amboss Auto Backup = Jah**, et saata automaatselt krüpteeritud varukoopiate uuendused iga kord, kui vahetate kanaleid. Rikke korral saate tänu sellele välisele varukoopiale oma vahendid taastada.





- **Tervisekontrollid:** Aktiveerige **Amboss Healthcheck = Jah**, et teie sõlmpunkt saadaks Ambossile regulaarselt pings'e. Saate teateid, kui teie sõlme näib olevat offline.





- **Muud funktsioonid:** Automaatne saldopüstitus, **Magma/Hydro** integratsioon (likviidsuse turg) ja juurdepääs üksikasjalikule tulemuslikkuse statistikale.



Amboss'i integreerimine lisab olulise **turvalisuse Layer** koos automaatse välise varundamise ja kättesaadavuse jälgimisega, millele on juurdepääs otse ThunderHubist.



### Tööriistad



Jaotises **Tööriistad** on koondatud mitmesugused täiustatud tööriistad sõlme haldamiseks. Siin on peamised Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Varukoopiad:** Manuaalselt hallata oma kanali varukoopiaid (SCB). ThunderHub võimaldab teil **laadida alla oma kanalite täieliku varukoopia** (valik "Kõigi kanalite varundamine -> Laadige alla"). Hoidke seda `channel-all.bak` faili turvalises kohas - see on hädavajalik teie vahendite taastamiseks krahhi korral. Saate ka **importida** varukoopiafaili, kui võtate sõlme uuesti kasutusele.





- **Raamatupidamine:** Finantsaruannete ekspordivahend, sealhulgas teenitud/makstud tasud ja antud perioodi jooksul suunatud mahud.
- **Allkirjastatud sõnumid:** allkirjastage või kontrollige sõnumeid oma sõlme abil, et tõestada oma Lightning-sõlme Ownership krüptograafilise allkirja abil.
- Makroonid (pagaritoodete sektsioon):** Halda LND** makroonid, et luua kohandatud juurdepääs. Interface "Bakery" võimaldab teil täpselt valida iga kasutusõiguse: "Peeride lisamine või eemaldamine", "Loo ketiaadressid", "Loo arved", "Loo makaronid", "Tuleta võtmed", "Võta juurdepääsukoodid", "Võta ketitehingud", "Võta arved", "Võta Wallet info", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages" jne. Iga luba saab eraldi aktiveerida nuppudega "Jah/ei", et luua kohandatud makaron.
- **Süsteemi teave:** Wallet versiooni ja aktiveeritud RPC-de kuvamine.



Lühidalt öeldes koondab tööriistade sektsioon täiustatud haldusfunktsioonid - varundamine, raamatupidamine, turvalisus ja juurdepääsu haldamine - ühtsesse Interface-sse.



### Vahetus



ThunderHubi vahekaart **Swap** võimaldab teil vahetada Lightning satoshis Bitcoin On-Chain vastu Boltzi teenuse kaudu. See funktsioon on kasulik liigse Lightning'i likviidsuse "dumpinguks" kanalisse ilma kanalit sulgemata.



![Interface de swap via Boltz](assets/fr/19.webp)



Protsess on lihtne:





- **Summa**: Määrake vahetatav summa
- **Address**: Sisestage Bitcoin vastuvõtt Address
- **Täitmine**: ThunderHub suhtleb Boltziga, et automaatselt töödelda Exchange



**Hüvitised:**




- Mittehooldusteenus (ei ole sularahahooldus)
- Säilitage oma olemasolevad kanalid
- Lihtsalt kasutatav integreeritud Interface



Boltz võtab väikese vahendustasu ja te maksate standardse Bitcoin tehingutasu. ThunderHub kuvab kõik kulud enne kinnitust.



### Statistika



ThunderHubi **Stats** jaotis pakub **täiustatud statistikat** teie Lightning-sõlme kohta, et analüüsida jõudlust ja optimeerida marsruutimist.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



See osa on oluline teie kulude optimeerimiseks, edukate kanalite tuvastamiseks ja sõlme laiendamise kavandamiseks.



## Kokkuvõte



**ThunderHub** on end tõestanud kui oluline vahend Lightning **LND** sõlme lihtsaks haldamiseks. See kaasaegne Interface pakub kõiki olulisi funktsioone: kanalite haldamine, maksed, seire, koos täiustatud funktsioonidega, nagu automaatne tasakaalustamine ja Amboss'i integreerimine.



**Vaimne eelis:**




- Interface elegantne ja intuitiivne
- Võimsad tööriistad (rebalance, Boltz swaps, automaatsed varukoopiad)
- Ühildub Umbrel, Voltage, RaspiBlitz ja teiste distributsioonidega



ThunderHub demokratiseerib täiustatud Lightning-sõlmede haldamise, muutes kättesaadavaks selle, mis varem nõudis keerulisi tehnilisi käsklusi. Olenemata sellest, kas olete algaja või kogenud operaator, ThunderHub võimaldab teil tõhusalt hallata oma Lightning-sõlme kaasaegse, tervikliku Interface kaudu.



## Ressursid



**Official links:**




- **Ametlik veebisait:** [thunderhub.io](https://thunderhub.io)
- **Dokumentatsioon:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **GitHubi lähtekood:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)