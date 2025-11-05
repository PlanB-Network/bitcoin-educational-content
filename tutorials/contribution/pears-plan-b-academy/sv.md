---
name: Plan ₿ Akademin - Päron App
description: Hur installerar och använder man Plan ₿ Academy-applikationen på Pears?
---

![cover](assets/cover.webp)


Du vet förmodligen redan att Plan ₿ Academy är den största utbildningsdatabasen som är tillägnad Bitcoin, som samlar kurser, handledning och tusentals resurser med öppen källkod. Ursprungligen var Plan ₿ Academy en webbplats. Men vad skulle hända om du inte längre kunde komma åt den normalt, till exempel i händelse av censur?


I den här handledningen lär vi oss hur man kör **Plan ₿ Academy**-plattformen på ett verkligt censurresistent sätt med hjälp av **Pears**, en peer-to-peer (P2P)-teknik som utvecklats av **Holepunch** och stöds av **Tether**.


Pears är den programvara som gör att vi kan köra Plan ₿ Academy-plattformen utan att förlita oss på en centraliserad webbplats. I den här handledningen kommer vi att installera Pears på din dator för att få tillgång till Plan ₿ Academy via Pears.


Målet med Pears är enkelt: att göra det möjligt att distribuera och använda webbapplikationer utan att vara beroende av någon centraliserad infrastruktur (inga servrar, inga värdar, inga mellanhänder). Med andra ord, även om en molnleverantör stängs ner eller ett land blockerar en domän, fortsätter applikationen att leva bland nätverkets kamrater. Detta tillvägagångssätt gör att vår utbildningsplattform, Plan ₿ Academy, kan vara tillgänglig över hela världen, utan en enda punkt av misslyckande.


---

**TL;DR:**



- Installera Pears;



- Kör följande kommando för att starta appen Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Vad är Pears?


Pears är på en och samma gång en runtime-miljö, ett utvecklingsverktyg och en distributionsplattform för peer-to-peer-applikationer. Med detta verktyg med öppen källkod kan du bygga, dela och köra programvara utan servrar eller infrastruktur, direkt mellan användare. I praktiken innebär detta att varje användare blir en nod i nätverket i stället för att ha en applikation på en central server: de delar en del av applikationen och data med andra peers. Hela systemet bildar ett distribuerat nätverk där varje instans samarbetar för att hålla tjänsten tillgänglig.


![Image](assets/fr/01.webp)


Detta tillvägagångssätt bygger på en uppsättning modulära programvarukomponenter som utvecklats av Holepunch:



- Hypercore**: en distribuerad logg som säkerställer datakonsistens och säkerhet utan en central databas.
- Hyperbee**: ett index som byggs ovanpå Hypercore och som gör det möjligt att organisera och söka data på ett effektivt sätt.
- Hyperdrive**: ett distribuerat filsystem som används för att lagra och synkronisera programfiler mellan peers.
- Hyperswarm** och **HyperDHT**: nätverkslager som möjliggör upptäckt av kollegor och anslutningar över hela världen utan en central server.
- Secretstream**: ett end-to-end-krypteringsprotokoll som säkrar kommunikationen mellan peers.


Genom att kombinera dessa komponenter gör Pears det möjligt att skapa autonoma, krypterade och distribuerade applikationer där varje användare aktivt deltar i nätverket. Denna decentraliserade arkitektur eliminerar infrastrukturkostnader, censurrisker och SPOF:er (*Single Points of Failure*).


Pears utvecklas av Holepunch, ett företag som grundades av Mathias Buus och Paolo Ardoino (VD för Tether och CTO för Bitfinex), med uppdraget att utöka peer-to-peer-logiken bortom Bitcoin. Deras ambition är att bygga "*Internet of peers*", där varje applikation kan fungera utan tillstånd, utan servrar och utan mellanhänder. Holepunch ligger redan bakom **Keet**, en helt P2P-anpassad app för videokonferenser och meddelanden.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Denna installationshandledning för Pears är uppdelad i flera avsnitt beroende på ditt operativsystem. Gå direkt till det som motsvarar din miljö för att följa lämpliga instruktioner:*



- Linux (Debian)** → Avsnitt **2**
- Windows** → Sektion **3**
- macOS** → Avsnitt **4**


## 2. Hur installerar man Pears på Linux (Debian)?


Att installera Pears på Debian är relativt enkelt men kräver några förutsättningar, som vi kommer att beskriva i det här avsnittet.


### 2.1. Uppdatera systemet


Innan något annat är det viktigt att se till att ditt system är uppdaterat.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Installera beroenden


Pears förlitar sig på vissa systembibliotek, inklusive `libatomic1`, som används av Bare JavaScript runtime engine. Installera det med följande kommando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Installera Node.js och npm via NVM


Pears distribueras genom *npm*, *Node.js*-pakethanteraren. Även om Pears inte är direkt beroende av *Node.js* för att köras, krävs det för installationen. Det rekommenderade sättet att installera *Node.js* på Linux är genom *NVM* (*Node Version Manager*), som gör att du kan hantera flera versioner av Node sida vid sida.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Ladda sedan om din terminal för att aktivera *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Kontrollera att *NVM* är korrekt installerad:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Installera sedan en stabil version av *Node.js* (t.ex. den aktuella LTS-versionen):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Kontrollera att *Node.js* och *npm* är korrekt installerade:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Installera Pears med npm


När *npm* är tillgängligt kan du installera Pears CLI globalt på ditt system. Detta gör att du kan köra kommandot `pear` från vilken katalog som helst.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Initialisera Pears


Efter installationen kör du helt enkelt följande kommando i din terminal:


```bash
pear
```


Vid första lanseringen kommer Pears att ansluta till peer-to-peer-nätverket för att ladda ner de nödvändiga komponenterna. Denna process förlitar sig inte på någon central server - filerna hämtas direkt från andra peers.


![Image](assets/fr/10.webp)


När nedladdningen är klar kör du kommandot igen för att bekräfta att allt fungerar:


```bash
pear
```


![Image](assets/fr/11.webp)


Om allt är korrekt installerat kommer Pears hjälpmeny att visas med en lista över tillgängliga kommandon.


### 2.6. Testa päron med Keet


För att verifiera att Pears fungerar fullt ut kan du starta en befintlig P2P-applikation som finns tillgänglig i nätverket, t.ex. Keet, en programvara för meddelanden och videokonferenser med öppen källkod som utvecklats av Holepunch.


```bash
pear run pear://keet
```


Detta kommando laddar Keet-programmet direkt från Pears-nätverket, utan att använda en central server. Om Keet startas korrekt betyder det att din Pears-installation är fullt fungerande.


![Image](assets/fr/12.webp)


Ditt Linux-system är nu redo att köra och vara värd för peer-to-peer-applikationer med Pears.


## 3. Hur man installerar Pears på Windows


Det är lika enkelt att installera Pears på Windows som på Linux, men det krävs några särskilda verktyg.


*Om du använder Linux och redan har installerat Pears kan du hoppa direkt till **Steg 5**.*


### 3.1. Öppna PowerShell som administratör


Starta först PowerShell med administratörsbehörighet:



- Klicka på Start-menyn;
- Skriv "PowerShell";
- Högerklicka på "*Windows PowerShell*";
- Välj "*Kör som administratör*".


![Image](assets/fr/15.webp)


### 3.2. Ladda ner NVS


Pears installeras via *npm*, *Node.js*-pakethanteraren. På Windows är den metod som rekommenderas av Holepunch att använda *NVS* (*Node Version Switcher*), som är mer stabil än *NVM* på detta system.


I PowerShell kör du följande kommando för att installera den senaste versionen av *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Installera Node.js


Efter installationen startar du om PowerShell och skriver sedan följande kommando:


```powershell
nvs
```


Du bör se en lista över tillgängliga *Node.js*-versioner. Välj den första genom att trycka på tangenten `a` på ditt tangentbord.


![Image](assets/fr/17.webp)


*Node.js* är nu installerat.


![Image](assets/fr/18.webp)


### 3.4. Verifiera installationer


Kontrollera att *Node.js* och *npm* är tillgängliga:


```powershell
node -v
npm -v
```


Båda kommandona bör returnera ett versionsnummer.


![Image](assets/fr/19.webp)


### 3.5. Installera Pears med npm


När *Node.js* och *npm* är tillgängliga installerar du **Pears CLI** globalt på ditt system:


```powershell
npm install -g pear
```


Detta installerar binärfilen `pear` i din globala *npm*-katalog.


![Image](assets/fr/20.webp)


### 3.6. Verifiera och initiera Pears


När installationen är klar kör du:


```powershell
pear
```


Vid första lanseringen kommer Pears automatiskt att ladda ner de nödvändiga komponenterna från peer-to-peer-nätverket. Denna process kan ta några ögonblick.


![Image](assets/fr/21.webp)


Om allt gick bra bör du se Pears CLI hjälpmeny med en lista över tillgängliga underkommandon (run, seed, info...).


### 3.7. Testa päron med Keet


För att verifiera att Pears fungerar fullt ut kan du starta en befintlig P2P-applikation som finns tillgänglig i nätverket, till exempel Keet - meddelande- och videokonferensprogramvaran med öppen källkod som utvecklats av Holepunch.


```bash
pear run pear://keet
```


Detta kommando laddar Keet-programmet direkt från Pears-nätverket, utan att använda någon central server. Om Keet startas framgångsrikt betyder det att din Pears-installation är fullt fungerande.


![Image](assets/fr/22.webp)


Ditt Windows-system är nu redo att köra och vara värd för peer-to-peer-applikationer med Pears.


## 4. Så här installerar du Pears på macOS


Att installera Pears på macOS liknar Linux men kräver några justeringar som är specifika för Apples miljö. Låt oss gå igenom dessa steg tillsammans.


*Om du använder Linux eller Windows och redan har installerat Pears kan du hoppa direkt till **Steg 5**.*


### 4.1. Kontrollera systemförutsättningarna


Före installationen ska du kontrollera att *Xcode Command Line Tools* är installerat på ditt system. Detta paket innehåller de nödvändiga byggverktygen för *Node.js* och dess beroenden.


För att göra detta, öppna en terminal med hjälp av genvägen `Cmd + mellanslagstangenten`, skriv `Terminal` och tryck på `Enter`. Kör sedan följande kommando i terminalen för att installera det:


```bash
xcode-select --install
```


Om verktygen redan är installerade på ditt system kommer macOS att meddela dig.


### 4.2. Installera NVM


Pears distribueras via *npm*, *Node.js*-pakethanteraren. Även om Pears inte är direkt beroende av *Node.js* för att fungera, krävs det för installationen. Den rekommenderade metoden för att installera *Node.js* på macOS är *NVM* (*Node Version Manager*), som gör att du kan hantera flera Node-versioner samtidigt.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Ladda sedan om din terminal för att aktivera *NVM*:


```bash
source ~/.zshrc
```


Om du använder *bash* i stället för *zsh* kör du:


```bash
source ~/.bashrc
```


Kontrollera sedan att *NVM* är korrekt installerat:


```bash
nvm --version
```


Din terminal bör visa den installerade *NVM*-versionen.


### 4.3. Installera Node.js och npm


Installera sedan en stabil version av *Node.js* (t.ex. den aktuella LTS-versionen):


```bash
nvm install --lts
```


När installationen är klar ska du verifiera de installerade versionerna:


```bash
node -v
npm -v
```


Båda kommandona bör returnera ett versionsnummer.


### 4.4. Installera Pears med npm


När *npm* är tillgängligt kan du installera Pears CLI globalt på ditt system. Detta gör att du kan köra kommandot `pear` från vilken katalog som helst.


```bash
npm install -g pear
```


### 4.5. Initialisera Pears


Efter installationen kör du helt enkelt följande kommando i din terminal:


```bash
pear
```


Vid första lanseringen ansluter Pears till peer-to-peer-nätverket för att ladda ner de nödvändiga komponenterna. Den här processen kräver ingen central server - filer hämtas direkt från andra peers.


När nedladdningen är klar kör du kommandot igen för att kontrollera att allt fungerar:


```bash
pear
```


Om allt är korrekt installerat kommer Pears hjälpmeny att visas med en lista över tillgängliga kommandon.


### 4.6. Testa päron med Keet


För att verifiera att Pears är i full drift kan du starta en P2P-applikation som redan finns tillgänglig i nätverket, till exempel Keet, Holepunchs programvara för meddelanden och videokonferenser med öppen källkod.


```bash
pear run pear://keet
```


Detta kommando laddar Keet-appen direkt från Pears-nätverket, utan att använda en central server. Om Keet startar framgångsrikt betyder det att din Pears-installation är fullt fungerande.


Ditt macOS-system är nu redo att köra och vara värd för peer-to-peer-program med Pears.


## 5. Hur man använder Plan ₿ Academy på päron


När Pears är installerat och igång kan du direkt starta **Plan ₿ Academy**-plattformen via P2P-nätverket. Kör helt enkelt följande kommando i din terminal (samma kommando fungerar på Linux, Windows och macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


När laddningen är klar kommer Plan ₿ Academy att öppnas i din Pears-miljö, redo att användas precis som den ursprungliga webbplatsen - men utan något beroende av en central server.


![Image](assets/fr/14.webp)


## 6. Hur man sår plan ₿ Akademi om päron


I Pears-nätverket innebär att *seed* en applikation att den distribueras vidare till andra peers från din egen maskin. I praktiken, när du seed Plan ₿ Academy, blir din dator en datakälla som gör det möjligt för andra användare att ladda ner applikationen utan att förlita sig på en central server.


Denna mekanism stärker motståndskraften och censurresistensen hos vår applikation i Pears-nätverket. Ju fler peers seed en applikation har, desto mer tillgänglig och decentraliserad blir den, även om vissa ursprungliga noder går offline.


För att hjälpa till att distribuera Plan ₿ Academy kör du bara följande kommando:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Så länge detta kommando är aktivt kommer din enhet att delta i distributionen av programmets filer. Om du stänger terminalen stoppas delningsprocessen.


För att fortsätta sådd efter en omstart kan du köra kommandot i bakgrunden eller skapa en systemtjänst - till exempel en systemd-tjänst på Linux, en LaunchAgent på macOS eller en schemalagd uppgift på Windows. Dessa metoder säkerställer att Plan ₿ Academy-programmet automatiskt återupptar sådd vid systemstart.


Tack för att du bidrar till den decentraliserade distributionen av Plan ₿ Academy on Pears och hjälper till att göra Bitcoin-utbildning verkligt censurresistent!