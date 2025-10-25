---
name: Ride The Lightning (RTL)
description: Kasutage Ride The Lightning (RTL), et hallata oma Lightning-sõlme
---
![cover](assets/cover.webp)


## 1. Sissejuhatus



**Ride The Lightning (RTL)** on täielik Interface veebirakendus Lightning Network sõlme haldamiseks. See isehostitav veebirakendus pakub Lightning **"kokpit'i"**, millele on juurdepääs teie brauserist. RTL töötab kõigi peamiste Lightning-rakendustega (LND, Core Lightning/CLN ja Eclair) ning annab teile täieliku kontrolli oma sõlme ja kanalite üle. RTL on avatud lähtekoodiga (MIT-litsents) ja tasuta ning on vaikimisi integreeritud paljudesse sõlmede valmislahendustesse (RaspiBlitz, MyNode, Umbrel jne).



**Graafilise Interface puudumisel saab Lightning-sõlmi hallata ainult kasutajasõbralike CLI käskude abil. RTL lihtsustab neid toiminguid ergonoomilise Interface abil. Siin on peamised rakendused:**





- Vaadake oma kanaleid ja sõlme - armatuurlaual kuvatakse On-Chain saldo, Lightning likviidsus (kohalik/kaugjuhtimine), sünkroonimisolek, sõlme alias ja muud. Saate vaadata oma kanalite nimekirja, mahtu, kohalikku/kaugjaotust ja staatust. RTL pakub kontekstitundlikke armatuurlaudu, et analüüsida tegevust eri vaatenurkadest.





- **Kanalite välkjuhtimine** - avage/sulgege kanalid paari klõpsuga. RTL võimaldab teil luua ühenduse partneriga ja avada kanali ilma käsuta. Saate reguleerida marsruutimistasusid, vaadata saldoskoori või algatada ümmarguse tasakaalustamise, et tasakaalustada vahendeid kanalite vahel.





- **Jälgi ja tee makseid** - RTL haldab Lightning-tehinguid: saadab makseid arvete kaudu, genereerib arveid vastuvõtmiseks, jälgib tehinguid (maksed, marsruutimine) koos üksikasjaliku ajalooga. Interface analüüsib ka marsruutimist, et näha, millised maksed läbivad teie sõlme.





- **Wallet On-Chain haldamine ja varundamine** - On-Chain vahekaart võimaldab teil generate-aadresside ja tehingute saatmist. RTL teeb kanalite salvestamise lihtsaks, eksportides LND jaoks SCB-faili, mille automaatne uuendamine toimub iga kanali muutmise korral.



Lühidalt öeldes on RTL **võimsat armatuurlauda Lightning Network**, mis pakub Interface hariduslikku GW-d oma sõlme igapäevaseks piloteerimiseks. See õpetus juhatab teid selle paigaldamise ja kasutamise kaudu oma kanalite ja maksete haldamiseks.



## 2. RTLi tehniline toimimine



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Enne kui lähete asja juurde, on kasulik lühidalt mõista, **kuidas RTL teie Lightning-sõlmega** tehnilisel tasandil suhtleb.



**Üldine arhitektuur:** RTL on veebirakendus, mis on ehitatud Node.js (backend) ja Angular (frontend) abil. Konkreetselt öeldes töötab RTL väikese kohaliku veebiserverina (vaikimisi pordil 3000), mis suhtleb teie Lightningi rakendusega selle APIde kaudu. Sõltuvalt sellest, millist tüüpi :





- **LND** puhul kasutab RTL Lightning'i käskude täitmiseks LND REST API-d (port 8080). Ühendus on turvatud TLS-i abil ja nõuab LND autentimiseks **admin macaroon** faili.





- **Core Lightningiga (CLN)** kasutab RTL kas *c-lightning-REST* pakutavat REST API-d või **juurdepääsurünet** kommandoplugina kaudu. Sellised lahendused nagu Umbrel konfigureerivad need Elements automaatselt.





- **Eclairiga** ühendub RTL Eclair REST APIga, kasutades konfigureeritud autentimisparooli.



**Konfigureerimine ja turvalisus:** RTL konfigureeritakse JSON-faili (`RTL-Config.json`) abil, kus määratakse veebiport, juurdepääsuparool ja ühendusandmed teie sõlme jaoks. Interface veeb on kaitstud sisselogimise/parooliga (vaikimisi `parool`, mida saab muuta) ja toetab 2FA-d. Vaikimisi töötab RTL kohalikuna HTTP (`http://localhost:3000`), kuid kaugjuurdepääsuks kasutage alati turvalist ühendust (HTTPS läbi pöördproxy, Tor või VPN).



Lühidalt öeldes on RTL lisakomponent, mis ühendub teie sõlme turvaliste APIde kaudu, nõuab asjakohaseid juurdepääsutunnuseid ja pakub oma turvavõimalusi Layer. See modulaarne arhitektuur võimaldab teil isegi hallata **mitut Lightning-sõlme ühe RTL-i instantsiga**.



## 3. RTL paigaldus



Kuna RTL-i levitatakse avatud lähtekoodiga tarkvarana, on mitmeid viise, kuidas seda oma süsteemi paigaldada. Selles jaotises käsitleme kahte peamist lähenemist: käsitsi paigaldamine ja paigaldamine Umbreli kaudu.



### Manuaalne meetod



Käsitsi paigaldamine sobib, kui soovite säilitada peene kontrolli või kui integreerite RTL-i kohandatud konfiguratsiooni. Allpool toodud sammud on mõeldud LND sõlme jaoks, kus töötab Linux (nt Raspberry Pi või VPS, kus töötab Ubuntu/Debian), kuid on sarnased CLN/Eclairiga.



**Eelduseks:** veenduge, et teil on masinas **sünkroniseeritud** Bitcoin sõlme ja töötav Lightning-sõlm (LND, CLN või Eclair). RTL ei sisalda Lightning-sõlme iseenesest, see ühendab olemasoleva sõlme. Samuti on vaja paigaldatud **Node.js** (soovitatav versioon 14+). Saate kontrollida `node -v` abil või installida Node'i ametlikust saidist (https://nodejs.org/en/download/) või oma paketihaldurist.



Peamised paigaldusetapid on :



**Laadige alla RTL-kood**: Kloonige ametlik RTL GitHubi repositoorium enda valitud kataloogi. Näiteks:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installige sõltuvused**: RTL on Node.js rakendus, seega peate installima selle vajalikud moodulid. Käivitage RTL kaustas :



```bash
npm install --omit=dev --legacy-peer-deps
```



See käsk installeerib vajalikud NPM-i paketid (ignoreerides arendussõltuvusi). Võimalike Node'i sõltuvuskonfliktide vältimiseks on soovitatav kasutada valikut `--legacy-peer-deps`.



**RTL-Config**: Kui sõltuvused on paigas, valmistage ette konfiguratsioonifail. Kopeerige/ümbernimetage projekti juurest olev fail `Sample-RTL-Config.json` failiks `RTL-Config.json`. Avage see oma :





- **UI parool**: valige turvaline parool ja sisestage see `multiPass`i (vaikimisi `"parooli"` asemel).
- **Port**: vaikimisi 3000. Saate seda muuta, kui see port on teie masinas juba hõivatud.
- **Node**: kohandage oma sõlme parameetrid jaotises `nodes[0]`:
     - `lnNode`: kirjeldav nimi teie sõlme jaoks (nt `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (või `"CLN"`/`"ECL"` vastavalt vajadusele).
     - Punktis "Autentimine":
       - macaroonPath`: täpsustab täieliku tee kausta, mis sisaldab LND macaroon admini.
       - `configPath`: tee sõlme konfiguratsioonifaili (LND puhul `LND.conf`).
     - Seadete all:
       - `fiatConversion`: seadistage `true`, kui soovite fiat-valuuta konverteerimist.
       - `unannouncedChannels`: märkida `true`, et näha etteteatamata kanaleid.
       - themeColor` ja `themeMode`: Interface kohandamine.
       - channelBackupPath`: tee LND kanali varukoopiate jaoks.
       - `lnServerUrl`: Teie Lightning-sõlme URL (nt `https://127.0.0.1:8080`).



**Startige RTL-server**: Käivitage RTL kaustas :



```bash
node rtl
```



Rakendus käivitub ja seda saab kasutada aadressil `http://localhost:3000`.



**(Valikuline) Käivitage RTL teenusena**: Automaatseks käivitamiseks looge systemd :



Selleks:




- Avage oma masinas terminal.
- Looge uus teenusfail järgmise käsuga (asendage `nano` oma lemmikredaktoriga):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopeerige ja kleepige alljärgnev sisu sellesse faili:



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





- Asendage `/path/to/RTL/rtl` tegeliku teekonnaga `rtl` faili juurde teie masinas ja `<your_user>` teie Linuxi kasutajanimega.
- Salvestage ja sulgege fail.
- Laadige systemd konfiguratsioon uuesti:


```bash
sudo systemctl daemon-reload
```




- Aktiveerige ja käivitage RTL teenus:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL käivitub nüüd automaatselt iga kord, kui masin taaskäivitatakse. Selle olekut saate kontrollida käsuga :


```bash
sudo systemctl status RTL
```



### Paigaldamine vihmavarju kaudu



Kui kasutate [Umbrel](https://getumbrel.com), on RTL-i paigaldamine palju lihtsam:





- Juurdepääs Interface Umbrelile (tavaliselt `http://umbrel.local` kaudu)
- Mine **App Store**
- Otsi "Ride The Lightning"



**Tähtis märkus: Umbrel App Store'is on kaks eraldi RTL rakendust:**




- **Ride The Lightning** (LND jaoks): kasutamiseks koos Umbreli vaikimisi välgussõlmega (LND).
- **Ride The Lightning (Core Lightning)**: kasutage seda ainult siis, kui olete paigaldanud Umbrelile rakenduse *Core Lightning* ja soovite seda sõlme hallata RTL-i abil.



*Iga RTL-versioon on eelkonfigureeritud dialoogi pidamiseks vastava rakendusega (LND või Core Lightning). Kui te ei ole oma Lightning-sõlme muutnud, valige lihtsalt klassikaline LND versioon*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klõpsake nuppu **Installimine**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Tähtis:** Pärast installimist kuvab RTL ekraanil vaikimisi parooli. **Kopeerige ja salvestage see parool** - seda vajate Interface RTL-i sisselogimiseks. See parool kuvatakse iga kord, kui RTL käivitub, kuni te märgistate valiku "Don't show it again".



Umbrel hoolitseb automaatselt :




- Laadige alla ja konfigureerige RTL
- Lightning-sõlme juurdepääsu konfigureerimine
- Uuenduste haldamine
- Juurdepääsu tagamine Interface-le



Pärast installimist ilmub rakendus Umbreli menüüsse *rakendused*. Selle käivitamiseks klõpsake **Ride The Lightning**.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Sisestage sisselogimisekraanil eelnevalt kopeeritud parool. Kui olete sisse loginud, on Interface veebi RTL otse Umbreli armatuurlaualt kättesaadav, ilma et oleks vaja täiendavat konfigureerimist!



## 4. Interface RTLi tutvustamine ja kasutamine



Nüüd, kui RTL on käivitatud ja töötab, uurime selle Interface veebi ja selle põhifunktsioone. Käime läbi rakenduse erinevad jaotised, et anda teile täielik ülevaade.



### Peamine juhtpaneel



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Niipea, kui logite sisse, avaneb **peamine armatuurlaud**, mis annab teile ülevaate teie Lightning-sõlmest. See lehekülg koondab olulist teavet:




- Teie Lightning saldo kokku
- On-Chain tasakaalu saadaval
- Teie likviidsuse jaotus (sissetulev/väljaminev)
- Kiire juurdepääs Satss-i saatmisele ja vastuvõtmisele oma Lightning-sõlme kaudu



### Fondide haldamine On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Vahekaart **On-Chain** võimaldab teil hallata oma bitcoin'e otse peamises ahelas:




- Saldo kuvamine erinevates ühikutes (Sats, BTC, USD)
- Tehingute täielik loetelu
- Address põlvkond Taproot (P2TR), P2SH (NP2WKH) või Bech32 (P2WKH)
- UTXO haldamine, bitcoinide vastuvõtmine ja saatmine



### Välk: alammenüüde üksikasjalik esitus



Interface RTL sisaldab Lightning Network-le pühendatud külgmenüüd, mis koondab kõik olulised funktsioonid sõlme haldamiseks. Järgnevalt on esitatud iga alammenüü üksikasjad ekraanipildi järjekorras:



#### 1. Eakaaslased/kanalid



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



See alammenüü võimaldab teil :




- Vaadake oma ühendatud kolleegide ja avatud või ootavate Lightning-kanalite nimekirja.
- Lisage uus partner (ühendage teine Lightning-sõlm).
- Olemasolevate kanalite avamine, sulgemine või haldamine.
- Vaadake iga kanali üksikasju: mahutavus, kohalikud/kaugsaldod, staatus, kauplemisajalugu, saldoskoor jne.



#### 2. Tehingud



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Selles alammenüüs saate :




- Saatke välkmaksed (Invoice kaudu).
- generate ja hallata arveid maksete saamiseks.
- Vaadake saadetud ja saadud maksete täielikku ajalugu koos üksikasjadega (summa, kuupäev, staatus, tasud, ülekannete arv jne).



#### 3. Marsruudi määramine



Selles alammenüüs kuvatakse :




- Teie sõlme poolt teistele Lightning Network kasutajatele suunatud maksed.
- Marsruutimisstatistika: edastatud tehingute arv, teenitud tasud, esinenud vead.
- Eksporditav ajalugu täiustatud analüüsiks.



#### 4. Edasilükkamised



See alammenüü pakub :




- Üksikasjalikud aruanded teie Lightning-sõlme tegevuse kohta.
- Graafikud ja tabelid kanalite, maksete, tasude, mahu jne kohta.
- Tööriistad, et paremini mõista oma sõlme jõudlust.



#### 5. Graafiku otsing



See alammenüü võimaldab teil :




- Uurige Lightning Network topoloogiat.
- Konkreetsete sõlmede või kanalite otsimine.
- Hankige teavet ühenduvuse ja võrgu üldise läbilaskevõime kohta.



#### 6. Allkiri/kinnitus



See alammenüü pakub :




- Võimalus allkirjastada sõnum oma sõlme võtmega (tõend Ownership).
- Allkirja kontrollimine teiste sõlmede sõnumite autentimiseks.



#### 7. Varukoopia



See alammenüü on pühendatud varundamisele:




- Ekspordi kanali varukoopiafaili (SCB LND jaoks).
- Vajaduse korral taastage konfiguratsioon või kanalid.
- Näpunäiteid varunduste kaitsmiseks.



#### 8. Sõlm/võrk



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Sellest alammenüüst leiate :




- Täielik kokkuvõte Lightning-sõlme olekust: alias, versioon, värv, sünkroniseerimise olek.
- Statistika kanalite kohta (aktiivsed, ootavad, suletud), koguvõimsus, ühenduvus.
- Teave globaalse Lightning Network ja teie sõlme positsiooni kohta selles.



### Teenused: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz on privaatsussõbralik, Exchange mittekaitstav teenus, mis konverteerib bitcoin'id Lightning Network ja Blockchain Bitcoin (On-Chain) vahel. See pakub kahte tüüpi tööd: Reverse Submarine Swap (**Swap Out**) ja Submarine Swap (**Swap In**).



#### Väljavahetus (vastupidine allveelaevavahetus)



Swap Out konverteerib Lightning Networks saadaval olevad Satssid On-Chain bitcoinideks. See mehhanism on kasulik siis, kui sõlme sissetulev võimsus saab otsa või kui soovite saada raha tagasi On-Chain Address-lt. Protsess toimib järgmiselt:




- Kasutaja valib vahetatava summa
- Sõlm saadab Boltzile Lightning-makse
- Exchange-s blokeerib Boltz samaväärse summa On-Chain bitcoinides
- Kui tehing on kinnitatud, saab kasutaja raha tagasi nõuda, avaldades vahetuses kasutatud saladuse



See protsess on mittekaitstav, kuna Boltz ei hoia kunagi kasutaja raha käes.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (allveelaeva vahetus)



Swap In seevastu võimaldab On-Chain vahendeid Lightning Network-sse tagasi suunata. See on eriti kasulik teie kanalite väljundvõimsuse taastamiseks. Menetlus on järgmine:




- Kasutaja saadab bitcoinid konkreetsele Address, mille on genereerinud Boltz
- Neid vahendeid saab Boltz vabastada ainult siis, kui ta maksab kasutaja sõlme poolt genereeritud Lightning Invoice
- Kui Invoice on makstud, on vahendid Lightning-kanalis kättesaadavad, suurendades sõlme väljundvõimsust



![Configuration d'un swap-in](assets/fr/12.webp)



Need kaks mehhanismi võimaldavad Lightning-kanali likviidsust tõhusalt hallata, säilitades samas kasutaja suveräänsuse tema vahendite üle.



### Konfigureerimine ja kohandamine



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Vahekaardil **Node Config** saate kohandada oma kogemust:




- Etteteatamata kanalite aktiveerimine
- Kohandada müügi kuvamist
- Block explorer konfiguratsioon
- Interface reguleerimine



### Dokumentatsioon ja abi



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Lõpuks pakub **Help** jaotis põhjalikku dokumentatsiooni :




- Esialgne konfiguratsioon
- Peer ja kanali haldamine
- Maksed ja tehingud
- Varukoopiad ja taastamised
- Aruanded ja statistika
- Allkirjad ja kontrollid
- Sõlme ja rakenduse parameetrid



See terviklik Interface võimaldab teil hallata oma Lightning-sõlme tõhusalt, alates põhitoimingutest kuni täiustatud funktsioonideni, kõik intuitiivse ja hästi organiseeritud Interface abil.



## 5. Täiustatud kasutusjuhtumid ja turvalisus



Selles jaotises on kirjas, mida peate teadma, et minna RTLiga edasi ja kindlustada oma Lightning-sõlme:



### Järelevalve ja tõrkeotsing



Oma sõlme jälgimiseks saate eksportida RTL-andmeid (logid, CSV) ja vaadata neid sellistes tööriistades nagu Grafana. Probleemi korral (blokeeritud makse, mitteaktiivne kanal) vaadake LND/CLN-i logisid ja kasutage diagnostikakäske (`lncli listchannels`, `lncli pendingchannels` jne). RTL pakub ka Interface logisid marsruutimise sündmuste jälgimiseks.



### Turvaline kaugjuurdepääs



Ärge kunagi avaldage RTL-i otse Internetis. Eelistage :




- **VPN** (nt Tailscale) privaatse, krüpteeritud juurdepääsu jaoks
- **Tor** turvalise, anonüümse juurdepääsu jaoks
- Reverse proxy **HTTPS** (Nginx/Caddy) ainult siis, kui te teate, kuidas seda konfigureerida



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Head ohutustavad





- **Kaitske oma juurdepääsu**: ärge kunagi jagage admin.macaroon või oma RTL parooli. Piirake tundlike failide õigusi.
- **Regulaarsed varukoopiad**: eksportige kanali varukoopiate fail (SCB) pärast iga muudatust ja salvestage see väljaspool sõlme.
- **Uuendused**: hoiab RTLi, teie sõlme ja Umbreli viimaste turvaparandustega ajakohasena.
- **Konfidentsiaalsus**: anonüümne logid ja ekraanipildid enne nende jagamist. Ärge kunagi jagage oma saldosid või võrdsete isikute nimekirju avalikult.
- **Ühekordne juurdepääs**: RTL ei ole mitme kasutajaga. Ärge jagage administraatori juurdepääsu. Ainult lugemiseks kasutage vajaduse korral spetsiaalset makarooni.



Neid põhimõtteid rakendades saate oluliselt piirata riske ja säilitada kontrolli oma Lightning-sõlme üle.



## 7. Kokkuvõte



**Ride The Lightning** on oluline vahend Bitcoin/Lightning-sõlme tõhusaks haldamiseks, olenemata sellest, kas olete algaja või edasijõudnud kasutaja. See pakub selget Interface kanalite, maksete ja sõlme tervise kontrollimiseks, süvendades samal ajal teie Lightning Network mõistmist.



RTL paistab silma oma mitme rakenduse ühilduvuse, täiustatud funktsioonide (tasakaalustamine, vahetused, aruanded) ja pedagoogilise lähenemise poolest. Lihtsamate vajaduste jaoks piisab Interface Umbrel või Wallet mobile, kuid RTL on täiesti mõistlik aktiivse, optimeeritud sõlme haldamiseks.



Et rohkem teada saada :




- RTLi ametlik veebileht: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Tehnilised arutelud, projektiteated, tagasiside ja õppevahendid
- **Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Ametlik foorum, kus on spetsiaalne Bitcoin/Lightning sektsioon, juhendid ja lahendused tavalistele probleemidele
- **Lightning Network arendajad**: [github.com/lightning](https://github.com/lightning) - ametlik GitHubi repositoorium, kus saab jälgida arendustegevust ja panustada lähtekoodi
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Tehnilised küsimused ja vastused arendajatele ja edasijõudnutele



Lühidalt öeldes annab RTL teile täieliku kontrolli oma Lightning-sõlme üle kaasaegses, täisfunktsionaalses Interface-s.



**Allikad :** RTL ametlik veebileht; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network ressursid.



Selleks, et süvendada oma arusaamist Lightning Network tööpõhimõtetest, soovitan teil osaleda ka sellel tasuta kursusel:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb