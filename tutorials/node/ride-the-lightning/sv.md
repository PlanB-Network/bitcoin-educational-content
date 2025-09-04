---
name: Ride The Lightning (RTL)
description: Använd Ride The Lightning (RTL) för att hantera din Lightning-nod
---
![cover](assets/cover.webp)


## 1. Inledning



**Ride The Lightning (RTL)** är en komplett Interface-webbapplikation för hantering av en Lightning Network-nod. Denna självhostade webbapplikation erbjuder en Lightning** "cockpit" som är tillgänglig från din webbläsare. RTL fungerar med alla större Lightning-implementeringar (LND, Core Lightning/CLN och Eclair) och ger dig total kontroll över din nod och dina kanaler. RTL är kostnadsfritt och med öppen källkod (MIT-licens) och integreras som standard i många nyckelfärdiga nodlösningar (RaspiBlitz, MyNode, Umbrel etc.).



**Utan en grafisk Interface kan Lightning-noder endast hanteras via användarvänliga CLI-kommandon. RTL förenklar dessa operationer med en ergonomisk Interface. Här är de **huvudsakliga applikationerna**:





- Visa dina kanaler och noder** - Instrumentpanelen visar On-Chain-saldo, Lightning-likviditet (lokal/fjärr), synkroniseringsstatus, nodalias med mera. Du kan visa din kanallista, kapacitet, lokal/fjärr distribution och status. RTL erbjuder kontextkänsliga instrumentpaneler för att analysera aktivitet från olika vinklar.





- Blixtsnabb kanalhantering** - Öppna/stäng kanaler med några få klick. Med RTL kan du ansluta till en peer och öppna en kanal utan ett kommando. Du kan justera routingavgifter, visa balanspoängen eller initiera en cirkulär ombalansering för att ombalansera medel mellan kanaler.





- Spåra och gör betalningar** - RTL hanterar Lightning-transaktioner: skicka betalningar via fakturor, generate-fakturor att ta emot, spåra transaktioner (betalningar, routing) med detaljerad historik. Interface analyserar även routing för att se vilka betalningar som passerar genom din nod.





- Wallet On-Chain-hantering och backup** - På fliken On-Chain kan du generate-adresser och skicka transaktioner. RTL gör det enkelt att spara kanaler genom att exportera SCB-filen för LND, med automatisk uppdatering för varje kanaländring.



Kort sagt, RTL är en ** kraftfull instrumentpanel för Lightning Network**, som erbjuder en pedagogisk Interface för att styra din nod på daglig basis. Denna handledning kommer att vägleda dig genom installationen och användningen för att hantera dina kanaler och betalningar.



## 2. Teknisk drift av RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Innan vi går in på detaljerna är det bra att kortfattat förstå **hur RTL interagerar med din Lightning-nod** på en teknisk nivå.



**Generell arkitektur:** RTL är en webbapplikation byggd med Node.js (backend) och Angular (frontend). Rent konkret körs RTL som en liten lokal webbserver (på port 3000 som standard) som kommunicerar med din Lightning-implementering via dess API:er. Beroende på vilken typ av :





- Med **LND** använder RTL LND:s REST API (port 8080) för att utföra Lightning-kommandon. Anslutningen säkras av TLS och kräver LND:s **admin macaroon**-fil för autentisering.





- Med **Core Lightning (CLN)** använder RTL antingen REST API som tillhandahålls av *c-lightning-REST*, eller en **access rune** via `commando` plugin. Lösningar som Umbrel konfigurerar automatiskt dessa Elements.





- Med **Eclair** ansluter RTL till Eclair REST API med hjälp av det konfigurerade autentiseringslösenordet.



**Konfiguration och säkerhet:** RTL konfigureras via en JSON-fil (`RTL-Config.json`) där du definierar webbport, lösenord och anslutningsinformation till din nod. Interface-webben skyddas av en inloggning/lösenord (standard `lösenord` som kan ändras) och stöder 2FA. Som standard körs RTL som lokal HTTP (`http://localhost:3000`), men för fjärråtkomst ska du alltid använda en säker anslutning (HTTPS via reverse-proxy, Tor eller VPN).



Kort sagt är RTL en extra komponent som ansluter till din nod via säkra API:er, kräver lämpliga åtkomsttokens och erbjuder sin egen säkerhet Layer. Denna modulära arkitektur gör att du till och med kan hantera **flera Lightning-noder med en enda RTL-instans**.



## 3. RTL-installation



Eftersom RTL distribueras som programvara med öppen källkod finns det flera sätt att installera det på ditt system. I det här avsnittet går vi igenom två huvudmetoder: manuell installation och installation via Umbrel.



### Manuell metod



Manuell installation är lämplig om du vill behålla finkornig kontroll eller om du integrerar RTL i en anpassad konfiguration. Stegen nedan gäller för en LND-nod som kör Linux (t.ex. Raspberry Pi eller VPS som kör Ubuntu/Debian), men är liknande för CLN/Eclair.



**Förutsättning:** se till att du har en **synkroniserad** Bitcoin-nod och en fungerande Lightning-nod (LND, CLN eller Eclair) på maskinen. RTL innehåller inte en Lightning-nod i sig, den ansluter till en befintlig nod. Du behöver också **Node.js** installerat (version 14+ rekommenderas). Du kan kontrollera med `node -v` eller installera Node från den officiella webbplatsen (https://nodejs.org/en/download/) eller din pakethanterare.



De viktigaste installationsstegen är :



**Ladda ner RTL-koden**: Klona det officiella RTL GitHub-förvaret i den katalog du väljer. Till exempel:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installera beroenden**: RTL är en Node.js-applikation, så du måste installera de moduler som krävs. I RTL-mappen kör du :



```bash
npm install --omit=dev --legacy-peer-deps
```



Detta kommando installerar de nödvändiga NPM-paketen (ignorerar utvecklingsberoenden). Alternativet `--legacy-peer-deps` rekommenderas för att undvika eventuella konflikter med Node-beroenden.



**RTL-Config**: När beroendena är på plats förbereder du konfigurationsfilen. Kopiera/byt namn på filen `Sample-RTL-Config.json` i projektets rot till `RTL-Config.json`. Öppna den i din :





   - UI-lösenord**: välj ett säkert lösenord och ange det i `multiPass` (i stället för standardlösenordet `"password"`).
   - Port**: standard `3000`. Du kan ändra den om den här porten redan är upptagen på din maskin.
   - Node**: i avsnittet `nodes[0]` justerar du parametrarna för din nod:
     - `lnNode`: ett beskrivande namn för din nod (t.ex. `"LND Node Maison"`).
     - lnImplementation`: ``LND`` (eller ``CLN``/`ECL`` beroende på vad som är tillämpligt).
     - Under `autentisering`:
       - macaroonPath`: ange den fullständiga sökvägen till mappen som innehåller LND:s macaroon admin.
       - `configPath`: sökväg till nodens konfigurationsfil (`LND.conf` för LND).
     - Under `inställningar`:
       - `fiatConversion`: sätt till `true` om du vill ha fiat-valutakonvertering.
       - `unannouncedChannels`: sätt till `true` för att se oannonserade kanaler.
       - themeColor` och `themeMode`: Interface-anpassning.
       - channelBackupPath`: sökväg för säkerhetskopior av LND-kanaler.
       - `lnServerUrl`: URL till din Lightning-nod (t.ex. `https://127.0.0.1:8080`).



**Starta RTL-servern**: I RTL-mappen kör du :



```bash
node rtl
```



Programmet startar och kan nås på `http://localhost:3000`.



**(Valfritt) Kör RTL som en tjänst**: För automatisk start, skapa en systemd :



För att göra detta:




- Öppna en terminal på din maskin.
- Skapa en ny servicefil med följande kommando (ersätt `nano` med din favoritredigerare):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopiera och klistra in innehållet nedan i den här filen:



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





- Ersätt `/path/to/RTL/rtl` med den faktiska sökvägen till filen `rtl` på din dator och `<your_user>` med ditt Linux-användarnamn.
- Spara och stäng filen.
- Ladda om systemd-konfigurationen:


```bash
sudo systemctl daemon-reload
```




- Aktivera och starta RTL-tjänsten:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL kommer nu att starta automatiskt varje gång maskinen startas om. Du kan kontrollera dess status med :


```bash
sudo systemctl status RTL
```



### Installation via Umbrel



Om du använder [Umbrel] (https://getumbrel.com) är RTL-installationen mycket enklare:





- Access Interface Paraply (vanligtvis via `http://umbrel.local`)
- Gå till **App Store**
- Sök efter "Ride The Lightning"



**Viktigt: det finns två separata RTL-applikationer i Umbrel App Store:**




- Ride The Lightning** (för LND): för användning med Umbrels standardnod Lightning (LND).
- Ride The Lightning (Core Lightning)**: använd endast om du har installerat applikationen *Core Lightning* på Umbrel och vill hantera den här noden med RTL.



*Varje RTL-version är förkonfigurerad för dialog med motsvarande implementering (LND eller Core Lightning). Om du inte har ändrat din Lightning-nod väljer du helt enkelt den klassiska LND-versionen*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klicka på **Install**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Viktigt:** Efter installationen visar RTL en skärm med standardlösenordet. **Kopiera och spara detta lösenord** - du behöver det för att logga in på Interface RTL. Detta lösenord kommer att visas varje gång RTL startar tills du markerar alternativet "Don't show it again" (Visa det inte igen).



Umbrel tar automatiskt hand om :




- Ladda ner och konfigurera RTL
- Konfigurera åtkomst till Lightning-noden
- Hantera uppdateringar
- Säkra tillgången till Interface



När applikationen har installerats visas den i din *Apps*-meny på Umbrel. Klicka på **Ride The Lightning** för att starta den.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



På inloggningsskärmen anger du det lösenord som du kopierade tidigare. När du är inloggad kommer Interface web RTL att vara tillgänglig direkt från Umbrel-instrumentpanelen, utan att någon ytterligare konfiguration krävs!



## 4. Introduktion och användning av Interface RTL



Nu när RTL är igång, låt oss utforska Interface-webben och dess viktigaste funktioner. Vi kommer att gå igenom de olika delarna av applikationen för att ge dig en fullständig översikt.



### Huvudkontrollpanelen



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Så snart du loggar in får du tillgång till **huvudinstrumentpanelen**, som ger dig en översikt över din Lightning-nod. På den här sidan finns viktig information samlad:




- Ditt totala blixtsaldo
- On-Chain balans tillgänglig
- Fördelningen av din likviditet (inkommande/utgående)
- Snabb åtkomst till att skicka och ta emot Satss via din Lightning-nod



### Fondförvaltning On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Med fliken **On-Chain** kan du hantera dina bitcoins direkt på huvudkedjan:




- Saldovisning i olika enheter (Sats, BTC, USD)
- Fullständig lista över transaktioner
- Address generation Taproot (P2TR), P2SH (NP2WKH) eller Bech32 (P2WKH)
- UTXO-hantering, mottagande och sändning av bitcoins



### Lightning: detaljerad presentation av undermenyer



Interface RTL har en sidomeny som är dedikerad till Lightning Network, som samlar alla viktiga funktioner för att hantera din nod. Här är detaljerna för varje undermeny, i den ordning som visas på skärmdumpen:



#### 1. Kollegor/kanaler



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



I den här undermenyn kan du :




- Visa listan över dina anslutna kollegor och Lightning-kanaler som är öppna eller väntar.
- Lägg till en ny peer (anslut till en annan Lightning-nod).
- Öppna, stänga eller hantera befintliga kanaler.
- Se detaljer om varje kanal: kapacitet, lokala/fjärrstyrda saldon, status, handelshistorik, saldotal etc.



#### 2. Transaktioner



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



I den här undermenyn kan du :




- Skicka Lightning-betalningar (via Invoice).
- generate och hantera fakturor för att ta emot betalningar.
- Se hela historiken för skickade och mottagna betalningar med detaljer (belopp, datum, status, avgifter, antal överhoppningar etc.)



#### 3. Routning



Denna undermeny visar :




- Betalningar som dirigeras av din nod för andra Lightning Network-användare.
- Routing-statistik: antal transaktioner som vidarebefordrats, avgifter som tagits ut, fel som uppstått.
- Exporterbar historik för avancerad analys.



#### 4. Förskjutningar



Denna undermeny erbjuder :




- Detaljerade rapporter om aktiviteten i din Lightning-nod.
- Diagram och tabeller över kanaler, betalningar, avgifter, kapacitet etc.
- Verktyg för att bättre förstå din nods prestanda.



#### 5. Grafuppslagning



I den här undermenyn kan du :




- Utforska Lightning Network:s topologi.
- Sök efter specifika noder eller kanaler.
- Få information om anslutningsmöjligheter och övergripande nätverkskapacitet.



#### 6. Signera/verifiera



Denna undermeny erbjuder :




- Möjligheten att signera ett meddelande med din nods nyckel (bevis på Ownership).
- Signaturverifiering för att autentisera meddelanden från andra noder.



#### 7. Säkerhetskopiering



Den här undermenyn är avsedd för säkerhetskopiering:




- Exportera backup-fil för kanal (SCB för LND).
- Återställ konfiguration eller kanaler om det behövs.
- Tips för att säkra dina säkerhetskopior.



#### 8. Nod/Nätverk



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



I denna undermeny hittar du :




- En fullständig sammanfattning av statusen för din Lightning-nod: alias, version, färg, synkroniseringsstatus.
- Statistik över kanaler (aktiva, väntande, stängda), total kapacitet, konnektivitet.
- Information om den globala Lightning Network och din nods position i den.



### Tjänster: Boltz Swappar



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz är en integritetsvänlig, icke-förvarad Exchange-tjänst som konverterar bitcoins mellan Lightning Network och Blockchain Bitcoin (On-Chain). Den erbjuder två typer av operationer: Reverse Submarine Swap (**Swap Out**) och Submarine Swap (**Swap In**).



#### Swap Out (omvänt ubåtsbyte)



Swap Out konverterar Satss som är tillgängliga på Lightning Network till On-Chain bitcoins. Denna mekanism är användbar när en nod får slut på inkommande kapacitet, eller när du vill återfå medel från en On-Chain Address. Processen fungerar på följande sätt:




- Användaren väljer ett belopp som ska växlas
- Noden skickar en Lightning-betalning till Boltz
- I Exchange blockerar Boltz ett motsvarande belopp i On-Chain bitcoins
- När transaktionen har bekräftats kan användaren göra anspråk på pengarna genom att avslöja en hemlighet som användes i bytet



Denna process är inte frihetsberövande, och Boltz innehar aldrig användarens medel.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Submarine Swap)



Swap In, å andra sidan, gör det möjligt att återföra medel från On-Chain till Lightning Network. Detta är särskilt användbart för att återställa utgångskapaciteten på dina kanaler. Proceduren är som följer:




- Användaren skickar bitcoins till en specifik Address som genereras av Boltz
- Dessa medel kan endast frigöras av Boltz om han betalar en Lightning Invoice som genereras av användarens nod
- När Invoice har betalats är pengarna tillgängliga på Lightning-kanalen, vilket ökar nodens produktionskapacitet



![Configuration d'un swap-in](assets/fr/12.webp)



Dessa två mekanismer gör det möjligt att hantera likviditeten i Lightning-kanalen på ett effektivt sätt, samtidigt som användarens suveränitet över sina medel bibehålls.



### Konfiguration och anpassning



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



På fliken **Node Config** kan du anpassa din upplevelse:




- Aktivering av oannonserade kanaler
- Anpassa försäljningsdisplay
- Block explorer-konfiguration
- Justering av Interface



### Dokumentation och hjälp



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Slutligen innehåller avsnittet **Hjälp** omfattande dokumentation om :




- Inledande konfiguration
- Peer- och kanalhantering
- Betalningar och transaktioner
- Säkerhetskopiering och återställning
- Rapporter och statistik
- Underskrifter och verifikationer
- Node- och applikationsparametrar



Med denna omfattande Interface kan du hantera din Lightning-nod effektivt, från grundläggande funktioner till avancerade funktioner, allt i en intuitiv och välorganiserad Interface.



## 5. Avancerade användningsområden och säkerhet



I det här avsnittet får du veta vad du behöver veta för att gå vidare med RTL och säkra din Lightning-nod:



### Övervakning och felsökning



För att övervaka din nod kan du exportera RTL-data (loggar, CSV) och visa dem i verktyg som Grafana. Om det uppstår problem (blockerad betalning, inaktiv kanal) kan du läsa LND/CLN-loggar och använda diagnostiska kommandon (`lncli listchannels`, `lncli pendingchannels`, etc.). RTL erbjuder också Interface-loggar för övervakning av routinghändelser.



### Säker fjärråtkomst



Exponera aldrig RTL direkt på Internet. Ge företräde åt :




- VPN** (t.ex. Tailscale) för privat, krypterad åtkomst
- Tor** för säker, anonym åtkomst
- Omvänd proxy HTTPS** (Nginx/Caddy) endast om du vet hur man konfigurerar den



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### God säkerhetspraxis





- Skydda din åtkomst**: dela aldrig admin.macaroon eller ditt RTL-lösenord. Begränsa behörigheterna för känsliga filer.
- Regelbundna säkerhetskopior**: exportera kanalens säkerhetskopieringsfil (SCB) efter varje ändring och lagra den utanför noden.
- Uppdateringar**: Håll RTL, din nod och Umbrel uppdaterade med de senaste säkerhetsfixarna.
- Sekretess**: anonymisera loggar och skärmdumpar innan du delar dem. Dela aldrig dina balanser eller peer-listor offentligt.
- Enkel åtkomst**: RTL är inte fleranvändarprogram. Dela inte administratörsåtkomst. För skrivskyddad åtkomst, använd en dedikerad macaroon om det behövs.



Genom att tillämpa dessa principer begränsar du riskerna avsevärt och behåller kontrollen över din Lightning-nod.



## 7. Slutsats



**Ride The Lightning** är ett viktigt verktyg för att effektivt hantera en Bitcoin/Lightning-nod, oavsett om du är nybörjare eller avancerad användare. Det ger en tydlig Interface för att kontrollera dina kanaler, betalningar och nodhälsa, samtidigt som du fördjupar din förståelse för Lightning Network.



RTL sticker ut genom sin kompatibilitet med flera implementeringar, sina avancerade funktioner (ombalansering, swappar, rapporter) och sitt pedagogiska tillvägagångssätt. För enkla behov räcker det med Interface Umbrel eller Wallet Mobile, men RTL är perfekt för aktiv, optimerad nodhantering.



För att ta reda på mer :




- RTL:s officiella webbplats: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Tekniska diskussioner, projektmeddelanden, feedback och utbildningsresurser
- Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Officiellt forum med en särskild Bitcoin/Lightning-sektion, guider och lösningar på vanliga problem
- Lightning Network utvecklare**: [github.com/lightning](https://github.com/lightning) - Officiellt GitHub-arkiv för att följa utvecklingen och bidra med källkod
- Stack Exchange Bitcoin** : [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Tekniska frågor och svar med utvecklare och avancerade användare



Kort sagt, RTL ger dig total kontroll över din Lightning-nod, i en modern, fullfjädrad Interface.



**Källor :** RTL:s officiella webbplats; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Nätverksresurser.



För att fördjupa din förståelse för hur Lightning Network fungerar rekommenderar jag också att du går den här kostnadsfria kursen:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb