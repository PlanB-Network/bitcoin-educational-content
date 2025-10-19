---
name: Karta ₿ Academy - Pears App
description: Hur installerar och använder jag programmet Plan ₿ Academy på Pears?
---

![cover](assets/cover.webp)



Som du säkert vet är Plan ₿ Academy den största utbildningsdatabasen tillägnad Bitcoin, som samlar kurser, handledning och tusentals resurser som publiceras under en öppen licens. Ursprungligen var Plan ₿ Academy en webbplats. Men vad skulle hända om du inte längre kunde komma åt den normalt, till exempel i händelse av censur?



I den här handledningen lär vi oss hur man kör **Plan ₿ Academy**-plattformen på ett verkligt oöverskådligt sätt tack vare **Pears**, en peer-to-peer (P2P)-teknik som utvecklats av **Holepunch** och stöds av **Tether**.



Pears är den programvara som gör det möjligt för oss att köra Plan ₿ Academy-plattformen utan att förlita oss på en centraliserad webbplats. I den här handledningen installerar vi Pears på din dator för att komma åt Plan ₿ Academy via Pears.



Pears mål är enkelt: att göra det möjligt att distribuera och använda webbapplikationer utan att förlita sig på någon centraliserad infrastruktur (inga servrar, inga värdar, inga mellanhänder). Med andra ord, även om en molnleverantör stänger ner eller ett land blockerar en domän, lever applikationen vidare bland nätverkets kamrater. Det är detta tillvägagångssätt som gör det möjligt för vår utbildningsplattform Plan ₿ Academy att vara tillgänglig var som helst i världen, utan en enda punkt för fel.



---

**TL;DR :**





- Installera Päron ;





- Kör följande kommando för att starta programmet Plan ₿ Academy:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Installera Päron



### 1.1 Vad är Päron?



Pears är en runtime-miljö, ett utvecklingsverktyg och en distributionsplattform för peer-to-peer-applikationer. Detta verktyg med öppen källkod gör det möjligt att bygga, dela och köra programvara utan en server eller infrastruktur, direkt mellan användare. Konkret innebär detta att varje användare, istället för att hysa en applikation på en central server, blir en nätverksnod som delar en del av applikationen och data med andra användare. Hela systemet utgör ett distribuerat nätverk, där varje instans samarbetar för att hålla tjänsten tillgänglig.



![Image](assets/fr/01.webp)



Detta tillvägagångssätt bygger på en uppsättning modulära programvarublock som utvecklats av Holepunch:




- Hypercore**: en distribuerad logg som garanterar datakonsistens och säkerhet utan en central databas.
- Hyperbee**: en indexerare ovanpå Hypercore, för effektiv organisering och bläddring av data.
- Hyperdrive**: ett distribuerat filsystem som används för att lagra och synkronisera programfiler mellan peers.
- Hyperswarm** och **HyperDHT**: nätverkslager som möjliggör upptäckt och anslutning mellan peers över hela världen, utan en central server.
- Secretstream**: ett E2E-krypteringsprotokoll för att säkra utbyten mellan två peers.



Genom att kombinera dessa komponenter gör Pears det möjligt att skapa autonoma, krypterade och distribuerade applikationer, där varje användare aktivt deltar i nätverket. Denna decentraliserade arkitektur eliminerar infrastrukturkostnader, censurrisker och SPOF:er (*Single Point of Failure*).



Pears utvecklas av Holepunch, ett företag som grundades av Mathias Buus och Paolo Ardoino (VD för Tether och CTO för Bitfinex), med uppdraget att utöka peer-to-peer-logiken bortom Bitcoin. Deras ambition är att bygga "Peer-to-Peer Internet", där varje applikation kan köras utan auktorisering, utan servrar och utan mellanhänder. Holepunch ligger redan bakom **Keet**, en videokonferens- och meddelandeapplikation som är helt i linje med P2P.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Denna installationshandledning för Pears är uppdelad i flera avsnitt beroende på ditt operativsystem. Gå direkt till det avsnitt som motsvarar din miljö för att följa de lämpliga instruktionerna :*




- Linux (Debian)** → Del **1.2.**
- Windows** → Del **1.3.**
- macOS** → Del **1.4.**




### 1.2 - Hur installerar jag Pears på Linux (Debian)?



Att installera Pears på ett Debian-system är relativt enkelt, men kräver några förutsättningar, som vi förklarar i detalj i det här avsnittet.



#### 1.2.1. Uppdatering av systemet



Först och främst är det viktigt att se till att ditt system är uppdaterat.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Installera beroenden



Pears förlitar sig på ett antal systembibliotek, inklusive `libatomic1`, som används av Bare JavaScript-körtiden. Installera det med följande kommando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Installera Node.js och npm via NVM



Pears distribueras via *npm*, *Node.js*-pakethanteraren. Även om Pears inte är direkt beroende av *Node.js* för att fungera, är det nödvändigt för installationen. Den rekommenderade metoden för att installera *Node.js* på Linux är *NVM* (*Node Version Manager*), som gör att du kan hantera flera versioner av Node parallellt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Ladda sedan om din terminal för att aktivera *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Kontrollera att *NVM* är installerat:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Installera sedan en stabil version av *Node.js* (t.ex. den aktuella LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Kontrollera installationer av *Node.js* och *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Installera Pears med npm



När *npm* är tillgängligt kan du installera Pears CLI globalt på ditt system. Detta gör att du kan köra kommandot `pear` från vilken katalog som helst.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Initialisera Pears



Efter installationen kör du helt enkelt följande kommando i din terminal:



```bash
pear
```



Vid första uppstarten kommer Pears att ansluta till peer-to-peer-nätverket för att ladda ner de nödvändiga komponenterna. Denna process kräver ingen central server, utan filerna hämtas direkt från andra peer-to-peers.



![Image](assets/fr/10.webp)



När nedladdningen är klar kör du kommandot igen för att kontrollera att allt fungerar:



```bash
pear
```



![Image](assets/fr/11.webp)



Om allt är korrekt installerat kommer Pears Help att visas med en lista över tillgängliga kommandon.



#### 1.2.6. Test av päron med Keet



För att kontrollera att Pears är i full drift kan du starta en P2P-applikation som redan finns tillgänglig i nätverket, till exempel Keet, Holepunchs programvara för meddelanden och videokonferenser med öppen källkod.



```bash
pear run pear://keet
```



Detta kommando laddar programmet Keet direkt från Pears-nätverket utan att gå via en central server. Om Keet startas korrekt är din Pears-installation fullt fungerande.



![Image](assets/fr/12.webp)



Ditt Linux-system är nu redo att köra och vara värd för peer-to-peer-applikationer med Pears.



### 1.3 - Hur installerar jag Pears på Windows?



Det är lika enkelt att installera Pears på Windows som på Linux, men det krävs några specialverktyg.



*Om du använder Linux och redan har installerat Pears kan du gå direkt till steg 2



#### 1.3.1. Öppna PowerShell i administratörsläge



Först och främst, kör PowerShell med administratörsrättigheter :




- Klicka på Start-menyn;
- Typ PowerShell ;
- Högerklicka på "*Windows PowerShell*" ;
- Välj "*Kör som administratör*".



![Image](assets/fr/15.webp)



#### 1.3.2. Ladda ner NVS



Pears installeras via *npm*, *Node.js*-pakethanteraren. På Windows är den metod som rekommenderas av Holepunch att använda *NVS* (*Node Version Switcher*), som är mer stabil än *NVM* på detta system.



I PowerShell kör du följande kommando för att installera den senaste versionen av *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Installera Node.js



Efter installationen startar du om PowerShell och skriver in följande kommando:



```powershell
nvs
```



Du bör se en lista över tillgängliga *Node.js*-versioner. Välj den första genom att trycka på tangenten `a` på ditt tangentbord.



![Image](assets/fr/17.webp)



*Node.js* är installerat.



![Image](assets/fr/18.webp)



#### 1.3.4. Kontrollera installationer



Kontrollera att *Node.js* och *npm* är tillgängliga:



```powershell
node -v
npm -v
```



Båda kommandona måste returnera ett versionsnummer.



![Image](assets/fr/19.webp)



#### 1.3.5. Installera Pears med npm



När *Node.js* och *npm* är tillgängliga installerar du **Pears CLI** globalt på ditt system:



```powershell
npm install -g pear
```



Detta kommer att installera `pear` binärfilen i din globala *npm*-katalog.



![Image](assets/fr/20.webp)



#### 1.3.6. Kontrollera och initiera Pears



När installationen är klar kör du :



```powershell
pear
```



Vid den första lanseringen kommer Pears automatiskt att ladda ner de nödvändiga komponenterna från peer-to-peer-nätverket. Denna process kan ta några ögonblick.



![Image](assets/fr/21.webp)



Om allt har gått bra visas hjälpskärmen för CLI Pears med en lista över tillgängliga underkommandon (run, seed, info...).



#### 1.3.7. Test av päron med Keet



För att kontrollera att Pears fungerar fullt ut kan du starta en P2P-applikation som redan finns tillgänglig i nätverket, till exempel Keet, Holepunchs programvara för meddelanden och videokonferenser med öppen källkod.



```bash
pear run pear://keet
```



Detta kommando laddar programmet Keet direkt från Pears-nätverket utan att gå via en central server. Om Keet startas korrekt är din Pears-installation fullt fungerande.



![Image](assets/fr/22.webp)



Ditt Windows-system är nu redo att köra och vara värd för peer-to-peer-applikationer med Pears.



### 1.4. Hur installerar man Pears på macOS?



Att installera Pears på macOS liknar att installera det på Linux, men kräver några justeringar som är specifika för Apple-miljön. Låt oss upptäcka dessa steg tillsammans.



*Om du använder Linux eller Windows och redan har installerat Pears kan du gå direkt till steg 2



#### 1.4.1. Kontrollera systemkraven



Innan du installerar måste du se till att *Xcode Command Line Tools* finns på ditt system. Detta paket innehåller de nödvändiga kompileringsverktygen för _Node.js_ och dess beroenden.



För att göra detta öppnar du en terminal med kortkommandot `Cmd + mellanslagstangenten`, skriver sedan `Terminal` och trycker på `Enter`. Du kan sedan ange det här kommandot i terminalen för att starta installationen:



```bash
xcode-select --install
```



Om verktygen redan är installerade på ditt system kommer macOS att informera dig om detta.



#### 1.4.2. Installera NVM



Pears distribueras via *npm*, *Node.js*-pakethanteraren. Även om Pears inte är direkt beroende av *Node.js* för att fungera, är det nödvändigt för installationen. Den rekommenderade metoden för att installera *Node.js* på macOS är *NVM* (*Node Version Manager*), som gör att du kan hantera flera versioner av Node parallellt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Ladda sedan om din terminal för att aktivera *NVM* :



```bash
source ~/.zshrc
```



Om du använder *bash* i stället för *zsh* kör du :



```bash
source ~/.bashrc
```



Kontrollera sedan att *NVM* är installerat:



```bash
nvm --version
```



Terminalen bör visa den version av *NVM* som finns installerad på ditt system.



#### 1.4.3 Installera Node.js och npm



Installera sedan en stabil version av *Node.js* (t.ex. den aktuella LTS):



```bash
nvm install --lts
```



När installationen är klar kontrollerar du de installerade versionerna:



```bash
node -v
npm -v
```



Båda kommandona måste returnera ett versionsnummer.



#### 1.4.4 Installera Pears med npm



När *npm* är tillgängligt kan du installera Pears CLI globalt på ditt system. Detta gör att du kan köra kommandot `pear` från vilken katalog som helst.



```bash
npm install -g pear
```



#### 1.4.5. Initialisera Pears



Efter installationen kör du helt enkelt följande kommando i din terminal:



```bash
pear
```



Vid första uppstarten kommer Pears att ansluta till peer-to-peer-nätverket för att ladda ner de nödvändiga komponenterna. Denna process kräver ingen central server, utan filerna hämtas direkt från andra peer-to-peers.



När nedladdningen är klar kör du kommandot igen för att kontrollera att allt fungerar:



```bash
pear
```



Om allt är korrekt installerat kommer Pears Help att visas med en lista över tillgängliga kommandon.



#### 1.4.6. Test av päron med Keet



För att kontrollera att Pears är i full drift kan du starta en P2P-applikation som redan finns tillgänglig i nätverket, till exempel Keet, Holepunchs programvara för meddelanden och videokonferenser med öppen källkod.



```bash
pear run pear://keet
```



Detta kommando laddar programmet Keet direkt från Pears-nätverket utan att gå via en central server. Om Keet startas korrekt är din Pears-installation fullt fungerande.



Ditt macOS-system är nu redo att köra och vara värd för peer-to-peer-program med Pears.



## 2. Hur använder jag Plan ₿ Academy på päron?



När Pears är installerat och igång kan du köra **Plan ₿ Academy**-plattformen direkt via P2P-nätverket. Kör helt enkelt följande kommando i din terminal (det är samma kommando för Linux, Windows och macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



När Plan ₿ Academy har laddats upp öppnas den i din Pears-miljö, redo att användas som på den ursprungliga webbplatsen, men utan något beroende av en central server.



![Image](assets/fr/14.webp)