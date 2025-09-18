---
name: Blockstream App - Desktop
description: Hur använder man sin Hardware Wallet med Blockstream App på en dator?
---
![cover](assets/cover.webp)



## 1. Inledning



### 1.1 Mål för handledning





- Den här handledningen förklarar hur du använder **Blockstream App** på en dator för att hantera en Bitcoin **onchain** Wallet med en **Hardware Wallet**, vilket möjliggör säkra transaktioner som registreras på den huvudsakliga Blockchain Bitcoin.
- Den omfattar installation, inledande konfiguration, anslutning av en Hardware Wallet samt mottagning och sändning av bitcoins i kedjan.
- Obs: Andra handledningar i bilagorna handlar om Liquid, Watch-Only och mobilapplikationen.



### 1.2 Målgrupp





- **Nybörjare**: Användare som vill hantera sina bitcoins med säker skrivbordsprogramvara och en Hardware Wallet.
- **Användare på mellannivå**: Personer som vill förstå hur man använder en Hardware Wallet för onchain-transaktioner och integritetsalternativ som Tor eller SPV.



### 1.3. Bakgrund om hårdvaruplånböcker





- **Hardware Wallet**, **Cold Wallet**: En fysisk enhet som lagrar privata nycklar offline, vilket ger en hög säkerhetsnivå mot cyberattacker, till skillnad från **Hot plånböcker** (mjukvaruplånböcker på anslutna enheter).
- **Rekommenderad användning**:
    - Perfekt för att säkra stora belopp eller långsiktigt sparande.
    - Lämplig för säkerhetsfokuserade användare som vill skydda sina medel från de risker som är förknippade med anslutna enheter.
- **Begränsningar**: Kräver programvara som Blockstream App för att visa saldon, generate-adresser och sända Hardware Wallet-signerade transaktioner.



## 2. Vi presenterar Blockstream App





- **Blockstream App** är en mobil (iOS, Android) och stationär applikation för hantering av Bitcoin-plånböcker och tillgångar på Liquid Network. Den förvärvades av Blockstream 2016 och kallades *GreenAddress*, döptes om till *Blockstream Green* (2019) och kallas nu *Blockstream app* (2025).
- **Viktiga egenskaper**:
- **Onchain** transaktioner på Blockchain Bitcoin.
    - Transaktioner på **Liquid**-nätverket (Sidechain för snabba, konfidentiella utbyten).
- **Watch-only**-portföljer för övervakning av fonder utan tillgång till nycklar.
    - Sekretessalternativ: anslutning via **Tor**, anslutning till en **personlig nod** via Electrum, eller **SPV**-verifiering för att minska beroendet av tredjepartsnoder.
    - Fungerar **Replace-by-fee (RBF)** för att påskynda obekräftade transaktioner.
- **Kompatibilitet**: Integrerar hårdvaruplånböcker som **Blockstream Jade**.
- **Interface**: Intuitiv för nybörjare, med avancerade alternativ för experter.
- **Obs**: Den här guiden fokuserar på användning av onchain med en Hardware Wallet på skrivbordsversionen. Andra handledningar som tillhandahålls som bilagor täcker användning i mobilapplikationer, för onchain, Liquid och Watch-Only-funktioner.



## 3. Installera och konfigurera Blockstream App Desktop



### 3.1. Ladda ner





- Gå till den [officiella webbplatsen] (https://blockstream.com/app/) och klicka på "_Download Now_". Ladda ner den version som motsvarar ditt operativsystem (Windows, macOS, Linux).
- **Obs**: Var noga med att ladda ner från den officiella källan för att undvika bedräglig programvara.



### 3.2. Initial konfiguration





- **Startskärm**: När programmet öppnas för första gången visas en skärm utan en konfigurerad Wallet. Skapade eller importerade portföljer kommer att visas här senare.



![image](assets/fr/02.webp)





- **Anpassa inställningar**: Klicka på inställningsikonen längst ned till vänster, justera alternativen nedan och lämna sedan Interface för att fortsätta.



![image](assets/fr/03.webp)



#### 3.2.1. Allmänna parametrar





- I menyn Inställningar klickar du på "**Allmänt**".
- **Funktion**: Ändra programvarans språk och aktivera experimentella funktioner vid behov.



![image](assets/fr/04.webp)



#### 3.2.2. Anslutning via Tor





- I menyn Inställningar klickar du på "**Nätverk**".
- **Funktion**: Dirigera nätverkstrafik via **Tor**, ett anonymt nätverk som krypterar dina anslutningar.
- **Varför?**: Dölj din IP Address och skydda din integritet, perfekt om du inte litar på ditt nätverk (t.ex. offentligt Wi-Fi).
- **Nackdel**: Kan göra programmet långsammare på grund av kryptering.
- **Rekommendation**: Aktivera Tor om sekretess är en prioritet, men testa anslutningshastigheten.



![image](assets/fr/05.webp)



#### 3.2.3. Ansluta till en personlig nod





- I menyn Inställningar klickar du på "**Custom servers and validation**".
- **Funktion**: Ansluter applikationen till din egen **kompletta Bitcoin-nod** via en **Electrum-server**.
- Varför? Ger total kontroll över Blockchain-data, vilket eliminerar beroendet av Blockstream-servrar.
- **Förutsättning**: En konfigurerad Bitcoin-nod.
- **Rekommendation**: Avancerade användare som vill ha maximal suveränitet.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verifiering av SPV





- I menyn Inställningar klickar du på "**Custom servers and validation**".
- **Funktion**: Använder **Simplified Payment Verification (SPV)** som hämtar blockheaders och verifierar dina transaktioner genom bevis på inkludering (Merkle), utan att lagra hela Blockchain.
- Varför? Minskar beroendet av Blockstreams standardnod, samtidigt som den förblir lättviktig för enheter.
- **Nackdel**: Mindre säker än en Full node, eftersom den förlitar sig på tredjepartsnoder för viss information.
- **Rekommendation**: Aktivera SPV om du inte kan använda en personlig nod, men föredrar en Full node för optimal säkerhet.



![image](assets/fr/07.webp)



## 4. Ansluta en Hardware Wallet till Blockstream-appen



### 4.1. Inledande överväganden



#### 4.1.1. För Ledger-användare





- Blockstream Green stöder endast applikationen **Bitcoin Legacy** på Ledger-enheter (Nano S, Nano X).
- Steg att följa i **Ledger Live** innan du ansluter din enhet :


1. Gå till **"Inställningar"** → **"Experimentella funktioner"** och aktivera **utvecklarläge**.


2. Gå till **"My Ledger"** → **"App Catalogue"** och installera sedan applikationen **Bitcoin Legacy**


3. Öppna programmet **Bitcoin Legacy** på din Ledger innan du startar Blockstream Green för att upprätta anslutningen.




- **Obs**: Se till att din Ledger är upplåst med din PIN-kod och att Bitcoin Legacy-applikationen är aktiv när du ansluter.



#### 4.1.2 Initialisering av en Hardware Wallet





- Om din Hardware Wallet (Ledger, Trezor eller Blockstream Jade) aldrig har använts (antingen med Blockstream Green eller med annan programvara som Ledger Live) måste du först initialisera den. Detta steg innebär att i en säker miljö, utan kameror eller observatörer:


1. **seed frasgenerering / Mnemonic fras** (12, 18 eller 24 ord): Skriv ner den noggrant på ett papper.


2. **seed verifiering av fras**: Testa Wallet-importen från de noterade orden, t.ex. genom att verifiera den utökade publika nyckeln. Ska utföras innan du skickar pengar till Wallet och permanent säkrar seed-frasen.


3. **Skydda seed-frasen**: Förvara frasen på ett fysiskt medium (papper eller metall) och på en säker plats. Förvara den aldrig digitalt (inga skärmdumpar, moln eller e-post).




- **Viktigt**: seed-frasen är ditt enda sätt att återfå dina pengar om enheten försvinner eller inte fungerar som den ska. Vem som helst med åtkomst kan stjäla dina bitcoins.
- **Resurser** för säkerhetskopiering och kontroll av seed-meningen :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfiguration för denna handledning :





- Vi antar att Hardware Wallet redan har initialiserats med en seed-fras och en PIN-kod för låsning.
- Vi antar att Hardware Wallet aldrig har varit ansluten till Blockstream App, vilket kräver att ett nytt konto skapas. Om Hardware Wallet redan har använts med Blockstream App kommer kontot automatiskt att visas när applikationen öppnas.



### 4.2. Starta anslutningen





- Från startskärmen klickar du på "**Setup a New Wallet**", sedan godkänner du villkoren och klickar på "**Get Started**":



![image](assets/fr/08.webp)





- Välj alternativet "**På Hardware Wallet**":



![image](assets/fr/09.webp)





- Om du använder en **Blockstream Jade** klickar du på motsvarande knapp. I annat fall väljer du "**Ansluter en annan maskinvaruenhet**":



![image](assets/fr/10.webp)





- Anslut din Hardware Wallet till datorn via USB och välj den i Blockstream App :



![image](assets/fr/22.webp)





- Vänligen vänta medan Blockstream App importerar din portföljinformation:



![image](assets/fr/23.webp)



### 4.3. Skapa ett konto





- Om din Hardware Wallet redan har använts med Blockstream App kommer ditt konto automatiskt att visas i Interface efter importen. Annars skapar du ett konto genom att klicka på "**skapa konto**":



![image](assets/fr/24.webp)





- Välj "**Standard**" för att konfigurera en klassisk Bitcoin-portfölj:



![image](assets/fr/25.webp)





- När ditt konto har skapats kan du komma åt din huvudsakliga Interface-portfölj:



![image](assets/fr/26.webp)





## 5. Använda Wallet i kedjan med en Hardware Wallet



### 5.1. Ta emot bitcoins





- Klicka på "**Receive**" på huvudskärmen för portföljen:



![image](assets/fr/27.webp)





- Programmet visar en **blank mottagning Address**. Genom att använda en ny Address för varje mottagning förbättras din sekretess. Klicka på "**Kopiera Address**" för att kopiera Address eller låt avsändaren skanna den QR-kod som visas:



![image](assets/fr/12.webp)



**Optioner** :




- (1) Klicka på pilarna för att generate ett nytt Address kopplat till din portfölj.
- (2) För att begära ett specifikt belopp, klicka på "**Mera alternativ**" och sedan på "**Begära belopp**". QR kommer att uppdateras och Address kommer att ersättas av en Bitcoin betalnings URI som t.ex: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Om du vill återanvända en tidigare Address klickar du på "**Fler alternativ**" och sedan på "**Adresslista**":



![image](assets/fr/14.webp)





- **Verifiering**: Kontrollera noggrant den delade Address för att undvika fel eller attacker (t.ex. skadlig kod som ändrar urklipp).
- När transaktionen har sänts ut i nätverket kommer den att visas i din Wallet. Vänta på 1 till 6 bekräftelser för att betrakta transaktionen som oföränderlig.



![image](assets/fr/28.webp)



### 5.2. skicka bitcoins





- Klicka på "**Sänd**" på portföljens huvudskärm.



![image](assets/fr/29.webp)





- **Ange detaljer**:
    - (1) Kontrollera att den valda tillgången är **Bitcoin** (onchain).
    - (2) Ange mottagarens **Address** genom att klistra in den eller skanna en QR-kod med din webbkamera.
    - (3) Ange det **belopp** som ska skickas (i BTC, satoshis eller andra enheter).




![image](assets/fr/16.webp)





- Välj **transaktionsavgifter** (valfritt) :
 - Välj bland de föreslagna alternativen (snabb, medel, långsam) beroende på hur brådskande det är, med en beräknad bekräftelsetid.
 - För anpassade avgifter justerar du manuellt antalet satoshis per vbyte. Dessa visas på startskärmen. Se även [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- Manuellt val av **UTXO** (valfritt): Klicka på "**Manual Coin selection**" för att välja de specifika UTXO:er som ska användas i transaktionen.



![image](assets/fr/18.webp)





- **Preliminär verifiering**: Kontrollera Address, belopp och avgifter på sammanfattningsskärmen och klicka sedan på "**Bekräfta transaktion**". I verkligheten kommer transaktionen inte att släppas till nätverket förrän du har signerat den med din Hardware Wallet, som ensam har de hemliga nycklarna som är kopplade till de adresser från vilka UTXO (satoshis) kommer att debiteras.



![image](assets/fr/19.webp)





- **Slutlig kontroll och underskrift**: Kontrollera att alla transaktionsparametrar är korrekta **på din Hardware Wallet**-skärm och underteckna sedan transaktionen med hjälp av den. Ett Address-fel kan leda till oåterkallelig förlust av medel.





- **Sändning**: När den har undertecknats sänder Blockstream App automatiskt transaktionen i Bitcoin-nätverket.



![image](assets/fr/20.webp)





- **Uppföljning**:
 - Transaktionen visas på Wallet:s startskärm som "väntande" tills den har bekräftats.
 - Så länge transaktionen inte har bekräftats kan funktionen **Replace-by-fee (RBF)** användas för att påskynda bekräftelsen genom att höja avgiften (se bilaga).



![image](assets/fr/21.webp)



## Bilagor



### A1. Övriga Blockstream handledningsprogram





- Använda Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importera och spåra en portfölj i "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Använda Blockstream-appen på mobiltelefoner (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Förklaring av Replace-by-fee (RBF)





- **Definition**: Replace-by-fee (RBF) är en funktion i Bitcoin-nätverket som gör det möjligt för avsändaren att påskynda bekräftelsen av en **onchain**-transaktion genom att höja avgiften.
- **Gränser**:
    - RBF är inte tillgänglig för Liquid eller Lightning-transaktioner.
    - Den första transaktionen måste markeras som RBF-kompatibel, vilket Blockstream App gör automatiskt.
- För mer information, se [vår ordlista] (https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Bästa praxis





- **Säkra din återställningsfras**:
    - Spara din Hardware Wallet:s Mnemonic-fras på ett fysiskt medium (papper, metall) på en säker plats.
    - Spara den aldrig digitalt (moln, e-post, skärmdump).
    - Självstudier : Spara din Mnemonic-fras :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Skydda din integritet**:





    - generate en ny Address för varje onchain-mottagning.
    - Aktivera **Tor** eller **SPV** för att begränsa spårningen.
    - Anslut till din egen Bitcoin-nod via Electrum för maximal suveränitet.
- **Kontrollera alltid leveransadresser**:





    - Kontrollera Address på din Hardware Wallet-skärm innan du signerar.
    - Använd kopiera/klistra in eller en QR-kod för att undvika manuella fel.
- **Optimera kostnaderna**:





    - Justera avgifterna efter brådska och överbelastning av nätet (se [Mempool.space](https://Mempool.space/)).
    - Använd Liquid eller Lightning för snabba transaktioner till låg kostnad som inte kräver säkerhet i kedjan.
- **Uppdatera programvaran**:





    - Håll din Blockstream-app och Hardware Wallet-firmware uppdaterad med de senaste funktionerna och säkerhetsuppdateringarna.



### A4. Ytterligare resurser





- **Officiella länkar**:
    - [Officiell webbplats](https://blockstream.com/)
    - [Support för Blockstream-appen](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentation och chatt
    - [GitHub] (https://github.com/Blockstream/green_qt)





- **Block Explorers**:
    - På kedjan : [Mempool.space] (https://Mempool.space/)
    - Liquid : [Blockstream Info] (https://blockstream.info/Liquid)
    - Blixt : [1ML (Lightning Network)](https://1ml.com/)





- **Säkra din återställningsfras:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Ordlista] (https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Ordlista] (https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb