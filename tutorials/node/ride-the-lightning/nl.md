---
name: Ride The Lightning (RTL)
description: Gebruik Ride The Lightning (RTL) om je Lightning-knooppunt te beheren
---
![cover](assets/cover.webp)


## 1. Inleiding



**Ride The Lightning (RTL)** is een complete Interface webapplicatie voor het beheren van een Lightning Network node. Deze zelf gehoste webapplicatie biedt een Lightning **"cockpit"** die toegankelijk is vanuit je browser. RTL werkt met alle belangrijke Lightning-implementaties (LND, Core Lightning/CLN en Eclair) en geeft je totale controle over je knooppunt en kanalen. Open-source (MIT-licentie) en gratis, RTL is standaard geïntegreerd in veel kant-en-klare node-oplossingen (RaspiBlitz, MyNode, Umbrel, enz.).



**Zonder een grafische Interface kunnen Lightning nodes alleen via gebruiksvriendelijke CLI commando's worden beheerd. RTL vereenvoudigt deze handelingen met een ergonomische Interface. Dit zijn de belangrijkste toepassingen:**





- Bekijk uw kanalen en node - Het dashboard toont On-Chain balans, Lightning liquiditeit (lokaal/op afstand), synchronisatiestatus, node alias en meer. U kunt uw kanaallijst, capaciteit, lokale/remote distributie en status bekijken. RTL biedt contextgevoelige dashboards om de activiteit vanuit verschillende invalshoeken te analyseren.





- **Lightning kanaalbeheer** - Open/sluit kanalen met een paar klikken. Met RTL kun je zonder opdracht verbinding maken met een peer en een kanaal openen. Je kunt routeringskosten aanpassen, de saldoscore bekijken of een circulaire herbalancering starten om fondsen tussen kanalen opnieuw in balans te brengen.





- **Traceer en doe betalingen** - RTL beheert Lightning-transacties: stuur betalingen via facturen, generate facturen om te ontvangen, volg transacties (betalingen, routering) met gedetailleerde geschiedenis. Interface analyseert ook routing om te zien welke betalingen via uw knooppunt lopen.





- **Wallet On-Chain beheer en back-up** - Met het On-Chain tabblad kun je generate adressen beheren en transacties verzenden. RTL maakt het gemakkelijk om kanalen op te slaan door het SCB-bestand voor LND te exporteren, met automatische update voor elke kanaalwijziging.



Kortom, RTL is een **krachtig dashboard voor de Lightning Network**, dat een leerzame Interface biedt om je node dagelijks te besturen. Deze tutorial leidt je door de installatie en het gebruik om je kanalen en betalingen te beheren.



## 2. Technische werking van RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Voordat we de puntjes op de i zetten, is het handig om kort te begrijpen **hoe RTL op technisch niveau interageert met je Lightning-knooppunt**.



**Algemene architectuur:** RTL is een webapplicatie gebouwd met Node.js (backend) en Angular (frontend). Concreet draait RTL als een kleine lokale webserver (standaard op poort 3000) die via zijn API's in dialoog gaat met je Lightning-implementatie. Afhankelijk van het type :





- Met **LND** gebruikt RTL de REST API (poort 8080) van LND om Lightning-commando's uit te voeren. De verbinding is beveiligd met TLS en vereist LND's **admin macaroon** bestand voor authenticatie.





- Met **Core Lightning (CLN)** gebruikt RTL ofwel de REST API geleverd door *c-lightning-REST*, of een **access rune** via de `commando` plugin. Oplossingen zoals Umbrel configureren deze Elements automatisch.





- Met **Eclair** maakt RTL verbinding met de Eclair REST API met behulp van het geconfigureerde authenticatiewachtwoord.



**Configuratie en beveiliging:** RTL wordt geconfigureerd via een JSON-bestand (`RTL-Config.json`) waarin je de webpoort, het toegangswachtwoord en de verbindingsinformatie met je node definieert. Het Interface web is beveiligd met een login/wachtwoord (standaard `wachtwoord` dat gewijzigd kan worden) en ondersteunt 2FA. Standaard draait RTL als lokale HTTP (`http://localhost:3000`), maar gebruik voor toegang op afstand altijd een beveiligde verbinding (HTTPS via reverse-proxy, Tor of VPN).



Kortom, RTL is een extra component dat verbinding maakt met je knooppunt via beveiligde API's, de juiste toegangstokens nodig heeft en zijn eigen Layer beveiliging biedt. Dankzij deze modulaire architectuur kun je zelfs **meerdere Lightning-nodes beheren met één enkele RTL-instantie**.



## 3. RTL-installatie



Omdat RTL wordt gedistribueerd als open-source software, zijn er verschillende manieren om het op je systeem te installeren. In dit hoofdstuk behandelen we twee belangrijke benaderingen: handmatige installatie en installatie via Umbrel.



### Handmatige methode



Handmatige installatie is geschikt als je fijnkorrelige controle wilt houden, of als je RTL in een aangepaste configuratie integreert. De onderstaande stappen zijn voor een LND node met Linux (bijvoorbeeld een Raspberry Pi of VPS met Ubuntu/Debian), maar zijn vergelijkbaar voor CLN/Eclair.



**Voorwaarde:** zorg ervoor dat je een **gesynchroniseerd** Bitcoin knooppunt en een werkend Lightning knooppunt (LND, CLN of Eclair) op de machine hebt. RTL bevat niet per se een Lightning node, het maakt verbinding met een bestaande node. Je moet ook **Node.js** geïnstalleerd hebben (versie 14+ aanbevolen). Je kunt dit controleren met `node -v` of Node installeren vanaf de officiële site (https://nodejs.org/en/download/) of je pakketbeheerder.



De belangrijkste installatiefasen zijn :



**Download RTL code**: Kloon de officiële GitHub repository van RTL in de map van je keuze. Bijvoorbeeld:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installeer afhankelijkheden**: RTL is een Node.js-applicatie, dus je moet de benodigde modules installeren. Voer in de RTL-map :



```bash
npm install --omit=dev --legacy-peer-deps
```



Dit commando installeert de benodigde NPM pakketten (ontwikkelingsafhankelijkheden negerend). De `--legacy-peer-deps` optie wordt aangeraden om mogelijke Node afhankelijkheidsconflicten te vermijden.



**RTL-Config**: Zodra de afhankelijkheden aanwezig zijn, maak je het configuratiebestand klaar. Kopieer/hernoem het `Sample-RTL-Config.json` bestand in de project root naar `RTL-Config.json`. Open het in uw :





- **UI-wachtwoord**: kies een veilig wachtwoord en voer dit in `multiPass` in (in plaats van het standaard `"wachtwoord"`).
- **Poort**: standaard `3000`. U kunt dit wijzigen als deze poort al bezet is op uw machine.
- **Node**: pas in de `nodes[0]` sectie de parameters voor je node aan:
     - `lnNode`: een beschrijvende naam voor je knooppunt (bijvoorbeeld `"LND Node Maison"`).
     - lnImplementatie`: `"LND"` (of `"CLN"`/`"ECL"` al naar gelang).
     - Onder `authenticatie`:
       - macaroonPath`: geef het volledige pad op naar de map met de macaroon-admin van LND.
       - `configPath`: pad naar het configuratiebestand van het knooppunt (`LND.conf` voor LND).
     - Onder `instellingen`:
       - `fiatConversion`: stel in op `true` als je fiat valuta conversie wilt.
       - `unannouncedChannels`: zet op `true` om onaangekondigde kanalen te zien.
       - themeColor` en `themeMode`: Interface aanpassingen.
       - channelBackupPath`: pad voor LND kanaalback-ups.
       - `lnServerUrl`: URL van je Lightning-knooppunt (bijvoorbeeld `https://127.0.0.1:8080`).



**Start de RTL-server**: Voer in de RTL-map :



```bash
node rtl
```



De applicatie start op en kan worden geopend op `http://localhost:3000`.



**(Optioneel) Voer RTL uit als een service**: Maak voor automatisch opstarten een systemd :



Om dit te doen:




- Open een terminal op uw machine.
- Maak een nieuw servicebestand met het volgende commando (vervang `nano` door je favoriete editor):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopieer en plak de inhoud hieronder in dit bestand:



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





- Vervang `/path/to/RTL/rtl` door het daadwerkelijke pad naar het `rtl` bestand op je machine en `<your_user>` door je Linux gebruikersnaam.
- Sla het bestand op en sluit het.
- Laad de systemd configuratie opnieuw:


```bash
sudo systemctl daemon-reload
```




- Activeer en start de RTL-service:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL start nu automatisch elke keer als de machine opnieuw wordt opgestart. Je kunt de status controleren met :


```bash
sudo systemctl status RTL
```



### Installatie via Umbrel



Als je [Umbrel](https://getumbrel.com) gebruikt, is de installatie van RTL veel eenvoudiger:





- Toegang tot Interface Umbrel (meestal via `http://umbrel.local`)
- Ga naar de **App Store**
- Zoek naar "Berijd de bliksem



**Belangrijke opmerking: er zijn twee aparte RTL-toepassingen in de Umbrel App Store:**




- **Ride The Lightning** (voor LND): voor gebruik met het standaard Bliksemknooppunt van Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: alleen gebruiken als u de *Core Lightning* toepassing op Umbrel hebt geïnstalleerd en dit knooppunt met RTL wilt beheren.



*Elke RTL-versie is vooraf geconfigureerd om een dialoog aan te gaan met de overeenkomstige implementatie (LND of Core Lightning). Als u uw Lightning-knooppunt niet hebt gewijzigd, kiest u gewoon de klassieke LND-versie*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klik op **Installeren**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Belangrijk:** Na de installatie toont RTL een scherm met het standaard wachtwoord. **Kopieer en bewaar dit wachtwoord** - je hebt het nodig om in te loggen bij Interface RTL. Dit wachtwoord wordt elke keer getoond als RTL opstart, totdat je de optie "Niet meer tonen" aanvinkt.



Umbrel zorgt automatisch voor :




- RTL downloaden en configureren
- Toegang tot het Lightning-knooppunt configureren
- Updates beheren
- Toegang tot Interface beveiligen



Eenmaal geïnstalleerd verschijnt de applicatie in je *Apps* menu op Umbrel. Klik op **Ride The Lightning** om het te starten.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Voer op het inlogscherm het wachtwoord in dat u eerder hebt gekopieerd. Eenmaal ingelogd is de Interface web RTL direct toegankelijk vanuit het Umbrel dashboard, zonder dat er extra configuratie nodig is!



## 4. Introductie en gebruik van Interface RTL



Nu RTL draait, gaan we het Interface web en de belangrijkste functies verkennen. We doorlopen de verschillende onderdelen van de applicatie om je een compleet overzicht te geven.



### Het hoofdbedieningspaneel



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Zodra je inlogt, krijg je toegang tot het **hoofddashboard**, dat je een overzicht geeft van je Lightning-node. Deze pagina centraliseert essentiële informatie:




- Uw totale Lightning-saldo
- On-Chain saldo beschikbaar
- De uitsplitsing van je liquiditeit (inkomend/uitgaand)
- Snelle toegang tot het verzenden en ontvangen van Satss via je Lightning-knooppunt



### Fondsbeheer On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Met het tabblad **On-Chain** kunt u uw bitcoins rechtstreeks op de hoofdketen beheren:




- Saldoweergave in verschillende eenheden (Sats, BTC, USD)
- Volledige lijst met transacties
- Address generatie Taproot (P2TR), P2SH (NP2WKH) of Bech32 (P2WKH)
- UTXO beheer, ontvangen en verzenden van bitcoins



### Lightning: gedetailleerde presentatie van submenu's



Interface RTL heeft een zijmenu gewijd aan Lightning Network, waarin alle essentiële functies voor het beheren van je knooppunt zijn samengebracht. Hier zijn de details van elk submenu, in de volgorde van de schermafbeelding:



#### 1. Collega's/Kanalen



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Met dit submenu kunt u :




- Bekijk de lijst van je verbonden peers en Lightning-kanalen die open staan of wachten.
- Een nieuwe peer toevoegen (verbinding maken met een ander Lightning-knooppunt).
- Open, sluit of beheer bestaande kanalen.
- Bekijk details van elk kanaal: capaciteit, lokale/externe saldi, status, handelsgeschiedenis, balansscore, etc.



#### 2. Transacties



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



In dit submenu kunt u :




- Lightning-betalingen verzenden (via Invoice).
- generate en facturen beheren om betalingen te ontvangen.
- Bekijk de volledige geschiedenis van verzonden en ontvangen betalingen, met details (bedrag, datum, status, kosten, aantal overslagen, enz.)



#### 3. Routing



In dit submenu wordt :




- Betalingen die door uw knooppunt worden gerouteerd voor andere Lightning Network gebruikers.
- Routingstatistieken: aantal doorgegeven transacties, verdiende vergoedingen, fouten.
- Exporteerbare geschiedenis voor geavanceerde analyse.



#### 4. Uitstel



Dit submenu biedt :




- Gedetailleerde rapporten over de activiteit van je Lightning-knooppunt.
- Grafieken en tabellen over kanalen, betalingen, vergoedingen, capaciteit, enz.
- Tools om de prestaties van je node beter te begrijpen.



#### 5. Grafiek opzoeken



Met dit submenu kunt u :




- Verken de topologie van de Lightning Network.
- Zoeken naar specifieke knooppunten of kanalen.
- Verkrijg informatie over connectiviteit en algemene netwerkcapaciteit.



#### 6. Ondertekenen/Verifiëren



Dit submenu biedt :




- De mogelijkheid om een bericht te ondertekenen met de sleutel van je node (bewijs van Ownership).
- Handtekeningverificatie om berichten van andere nodes te verifiëren.



#### 7. Back-up



Dit submenu is gewijd aan back-ups:




- Export kanaal backup bestand (SCB voor LND).
- Herstel de configuratie of kanalen indien nodig.
- Tips voor het beveiligen van je back-ups.



#### 8. Knooppunt/Netwerk



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



In dit submenu vindt u :




- Een compleet overzicht van de status van je Lightning-node: alias, versie, kleur, synchronisatiestatus.
- Statistieken over kanalen (actief, wachtend, gesloten), totale capaciteit, connectiviteit.
- Informatie over de globale Lightning Network en de positie van jouw knooppunt daarin.



### Diensten: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz is een privacy-vriendelijke, niet-betaalbare Exchange service die bitcoins omzet tussen de Lightning Network en Blockchain Bitcoin (On-Chain). Het biedt twee soorten operaties: Reverse Submarine Swap (**Swap Out**) en Submarine Swap (**Swap In**).



#### Swap Out (omgekeerde duikbootruil)



Swap Out zet beschikbare Satss op de Lightning Network om in On-Chain bitcoins. Dit mechanisme is handig wanneer een knooppunt geen inkomende capaciteit meer heeft, of wanneer je geld wilt terughalen van een On-Chain Address. Het proces werkt als volgt:




- De gebruiker selecteert een bedrag dat moet worden ingewisseld
- Het knooppunt stuurt een Lightning-betaling naar Boltz
- In Exchange blokkeert Boltz een equivalent bedrag in On-Chain bitcoins
- Zodra de transactie is bevestigd, kan de gebruiker het geld opeisen door een geheim te onthullen dat bij de ruil is gebruikt



Dit proces is niet bindend, Boltz houdt het geld van de gebruiker nooit vast.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Onderzeeër Swap)



Met Swap In daarentegen kunnen On-Chain fondsen opnieuw in de Lightning Network worden geïnjecteerd. Dit is vooral handig om de uitgangscapaciteit van je kanalen te herstellen. De procedure is als volgt:




- De gebruiker stuurt bitcoins naar een specifieke Address gegenereerd door Boltz
- Deze fondsen kunnen alleen door Boltz worden vrijgegeven als hij een Lightning Invoice betaalt die wordt gegenereerd door het knooppunt van de gebruiker
- Zodra de Invoice is betaald, is het geld beschikbaar op het Lightning-kanaal, waardoor de uitgangscapaciteit van het knooppunt toeneemt



![Configuration d'un swap-in](assets/fr/12.webp)



Met deze twee mechanismen kan de liquiditeit van het Lightning-kanaal efficiënt worden beheerd, terwijl de gebruiker de soevereiniteit over zijn geld behoudt.



### Configuratie en aanpassing



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Op het tabblad **Node Config** kun je je ervaring aanpassen:




- Activering van onaangekondigde kanalen
- Verkoopweergave aanpassen
- Block explorer configuratie
- De Interface afstellen



### Documentatie en hulp



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Tot slot biedt de **Help** sectie uitgebreide documentatie over :




- Eerste configuratie
- Peer- en kanaalmanagement
- Betalingen en transacties
- Back-ups en herstel
- Rapporten en statistieken
- Handtekeningen en verificaties
- Node- en applicatieparameters



Met deze uitgebreide Interface kun je je Lightning-node efficiënt beheren, van basisbewerkingen tot geavanceerde functies, alles in een intuïtieve, overzichtelijke Interface.



## 5. Geavanceerde gebruikssituaties & beveiliging



In dit gedeelte lees je wat je moet weten om verder te gaan met RTL en je Lightning-node te beveiligen:



### Bewaking en probleemoplossing



Om je node te monitoren, kun je RTL-gegevens exporteren (logs, CSV) en ze bekijken in tools zoals Grafana. Als er een probleem is (geblokkeerde betaling, inactief kanaal), raadpleeg dan de LND/CLN logs en gebruik de diagnostische commando's (`lncli listchannels`, `lncli pendingchannels`, enz.) RTL biedt ook Interface logs voor het monitoren van routinggebeurtenissen.



### Veilige toegang op afstand



Zet RTL nooit rechtstreeks op internet. Geef de voorkeur aan :




- **VPN** (bijv. Tailscale) voor privé, versleutelde toegang
- **Tor** voor veilige, anonieme toegang
- Reverse proxy HTTPS (Nginx/Caddy) alleen als je weet hoe het te configureren



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Goede veiligheidspraktijken





- **Bescherm je toegang**: deel nooit admin.macaroon of je RTL wachtwoord. Beperk de rechten op gevoelige bestanden.
- **Regelmatige back-ups**: exporteer het kanaalback-upbestand (SCB) na elke wijziging en sla het op buiten het knooppunt.
- **Updates**: houd RTL, je knooppunt en Umbrel up-to-date met de nieuwste beveiligingsoplossingen.
- **Vertrouwelijkheid**: anonimiseer logs en screenshots voordat je ze deelt. Deel je balansen of peer-lijsten nooit publiekelijk.
- **Enkele toegang**: RTL is niet geschikt voor meerdere gebruikers. Gebruik geen gedeelde beheerderstoegang. Gebruik indien nodig een speciale macaroon voor alleen-lezen toegang.



Door deze principes toe te passen, beperk je de risico's aanzienlijk en behoud je de controle over je Lightning-node.



## 7. Conclusie



**Ride The Lightning** is een essentieel hulpmiddel voor het effectief beheren van een Bitcoin/Lightning-knooppunt, of je nu een beginner of een gevorderde gebruiker bent. Het biedt een duidelijke Interface voor het beheren van je kanalen, betalingen en de gezondheid van je node, terwijl het je inzicht in Lightning Network verdiept.



RTL onderscheidt zich door zijn compatibiliteit met meerdere implementaties, zijn geavanceerde functies (rebalancing, swaps, rapporten) en zijn pedagogische benadering. Voor eenvoudige toepassingen volstaat de Interface Umbrel of een Wallet mobile, maar RTL is perfect geschikt voor actief, geoptimaliseerd knooppuntbeheer.



Voor meer informatie:




- Officiële website van RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Technische discussies, projectaankondigingen, feedback en educatieve bronnen
- **Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Officieel forum met speciale Bitcoin/Lightning-sectie, gidsen en oplossingen voor veelvoorkomende problemen
- **Lightning Network Ontwikkelaars**: [github.com/lightning](https://github.com/lightning) - Officiële GitHub repository voor het volgen van de ontwikkeling en het bijdragen van broncode
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Technische vraag en antwoord met ontwikkelaars en gevorderde gebruikers



Kortom, RTL geeft je totale controle over je Lightning-node, in een moderne Interface met alle functies.



**Bronnen :** RTL officiële website; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network bronnen.



Om je inzicht in de werking van de Lightning Network te verdiepen, raad ik je ook aan deze gratis cursus te volgen:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb