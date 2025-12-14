---
name: Bygga med Elements och Liquid Network
goal: Lär dig använda och utveckla med Elements-plattformen Blockchain med öppen källkod och dess viktigaste funktioner
objectives: 

  - Förstå de grundläggande koncepten för Elements Blockchain-plattformen och Liquid-sidokedjorna.
  - Lär dig att konfigurera och köra Elements-noder för fristående och Sidechain-konfigurationer.
  - Få praktisk erfarenhet av federerade block signing och Federated 2-Way Peg.
  - Konfigurera och hantera säkra, effektiva Blockchain-miljöer för verkliga användningsfall.

---

# Bygga vidare på Liquid och Elements


Upptäck de avancerade funktionerna och möjligheterna med Liquid och Elements och lär dig hur du effektivt kan använda dessa verktyg för att förbättra dina utvecklingsprojekt. Den här utbildningen ger en komplett teoretisk och praktisk grund, så att du kan bemästra funktioner som Confidential Transactions, Issued Assets och Federated block signing.


Liquid, baserat på Elements-ramverket, är utformat för att förbättra sekretess, skalbarhet och funktionalitet för finansiella och tekniska lösningar. I den här kursen får du praktisk erfarenhet av utfärdande och hantering av tillgångar, Federated 2-Way Peg och användning av verktyg som elementsd och elements-cli, vilket ger dig möjlighet att skapa innovativa lösningar som är skräddarsydda för dina behov.


Den här kursen är skräddarsydd för utvecklare på alla erfarenhetsnivåer. Nybörjare och användare på mellannivå kommer att hitta lättillgängliga förklaringar och praktiska exempel, medan avancerade användare kan fördjupa sig i tekniska detaljer och mindre kända funktioner i Liquid och Elements.


Följ med oss för att höja dina färdigheter, frigöra den fulla potentialen hos Liquid och Elements och skapa effektiva verktyg för framtiden för Liquid-innovationen.

+++

# Inledning


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Kursöversikt


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


Välkommen till SID202-kursen!


Målet med *Elements Academy* är att introducera och förklara de viktigaste begreppen i *Elements*, den plattform med öppen källkod som Liquid Sidechain bygger på. I slutet av den här kursen bör du ha en gedigen förståelse för huvudfunktionerna i Elements, till exempel Confidential Transactions och Issued Assets, samt de processer som är involverade i driften av Elements Core. Varje avsnitt i kursen innehåller lektioner med förklarande texter och videor, följt av en frågesport.


Den här utbildningen syftar till att lära dig hur du använder och utvecklar med open source-plattformen Elements, med fokus på Liquid Network. Du kommer att upptäcka hur dessa tekniker kan förbättra integriteten, skalbarheten och funktionaliteten i dina utvecklingsprojekt. Oavsett om du är nybörjare eller en erfaren utvecklare kommer den här kursen att ge dig en stark grund för att behärska de grundläggande begreppen Elements och Liquid samt deras praktiska tillämpningar.


**Avsnitt 1: Inledning**

Vi börjar med en omfattande översikt över Elements-koncept. Du kommer att lära dig hur denna plattform utformades för att ge en modulär och flexibel grund för att skapa sidokedjor som Liquid. Målet är att förstå strukturen hos Elements innan vi dyker ner i dess praktiska tillämpningar.


**Avsnitt 2: Elements**

Det här avsnittet fokuserar på hur Elements fungerar. Du får lära dig hur du konfigurerar en Elements-nod, använder den i fristående läge eller använder den som en Sidechain.


**Avsnitt 3: Använda Elements - Praktiska användningsfall**

När du har lärt dig de teoretiska grunderna går vi igenom de praktiska tillämpningarna av Elements. Du kommer att lära dig hur du utför Confidential Transactions, utfärdar tillgångar och hanterar återutgivning av tillgångar.


**Avsnitt 4: Elements Federation**

Här kommer vi att utforska avancerade mekanismer, inklusive federerade block signing, använda Elements som en Sidechain och skapa oberoende blockkedjor. Detta avsnitt hjälper dig att förstå hur du kan säkerställa säkerhet, integritet och interoperabilitet för Elements-baserade blockkedjor.


Är du redo att utforska potentialen i Elements och Liquid Sidechain? Låt oss komma igång!



## Elements Översikt


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements är en Blockchain-plattform med öppen källkod och Sidechain-kompatibilitet som ger tillgång till kraftfulla funktioner som utvecklats av medlemmar i communityt, till exempel Confidential Transactions och Issued Assets.


Elements är i grunden ett protokoll som gör det möjligt att skapa konsensus kring transaktionshistoriken och de regler som styr överföringen och skapandet av tillgångar som lagras i en distribuerad Blockchain Ledger.


Mer bakgrundsinformation om Elements finns på Elements-projektets webbplats (https://elementsproject.org/), den officiella Liquid-bloggen (https://blog.Liquid.net/) och utvecklarportalen (https://Liquid.net/devs).


### Elements


Elements lanserades 2015 och minskar interna utvecklings- och forskningskostnader och utnyttjar den allra senaste Blockchain-tekniken, vilket öppnar upp för många nya användningsområden för implementering. En Elements-baserad Blockchain kan antingen fungera som en fristående Blockchain eller kopplas till en annan och köras som en Sidechain. Att köra Elements som en Sidechain gör att tillgångar kan överföras på ett verifierbart sätt mellan olika blockkedjor.


Genom att bygga på och utöka Bitcoin:s kodbas kan utvecklare som är bekanta med bitcoind API snabbt och kostnadseffektivt skapa fungerande blockkedjor och testa proof-of-concept-projekt. Genom att bygga på Bitcoin:s kodbas kan Elements också fungera som en testbädd för förändringar av själva Bitcoin-protokollet.


Några av de viktigaste funktionerna i Elements listas nästa.


#### Confidential Transactions


Som standard är alla adresser i Elements blinded som använder Confidential Transactions. Blinding är den process genom vilken beloppet och typen av tillgång som överförs är kryptografiskt dold för alla, utom deltagarna och de som de väljer att avslöja Blinding key för.


#### Issued Assets


Issued Assets på Elements gör att flera typer av tillgångar kan utfärdas och överföras mellan nätverksdeltagare. En utfärdad tillgång drar också nytta av Confidential Transactions och kan utfärdas på nytt eller förstöras av alla som innehar relevant reissuance token.


#### Federated 2-Way Peg


Elements är en Blockchain-plattform för allmänna ändamål som också kan "kopplas" till en befintlig Blockchain (t.ex. Bitcoin) för att möjliggöra tvåvägsöverföring av tillgångar från en kedja till den andra. Genom att implementera Elements som en Sidechain kan du kringgå några av de inneboende egenskaperna hos huvudkedjan, samtidigt som du behåller en god grad av den säkerhet som tillhandahålls av tillgångar som är säkrade på huvudkedjan.


#### Signerade block


Elements använder en Strong Federation av signatärer, så kallade Block Signers, som signerar och skapar block på ett tillförlitligt sätt och i rätt tid. Detta tar bort transaktionsfördröjningen i PoW Mining-processen, som är föremål för stor blocktidsvarians på grund av dess slumpmässiga poissonfördelning. Den federerade block signing-processen uppnår tillförlitlig blockskapande utan att införa behovet av tredje parts förtroende eller beräkningsalgoritmbaserad Mining.


Elements lägger till alla dessa funktioner ovanpå Bitcoin Core-kodbasen, vilket utökar förmågan hos mainchain-protokollet och möjliggör nya affärsanvändningsfall när det distribueras som en Sidechain eller som en fristående Blockchain-lösning.


# Element


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Hur Elements fungerar


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements tillhandahåller en teknisk lösning på problem som Blockchain-användare möter dagligen; transaktionsfördröjning, brist på integritet och risk för fungibilitet.


Elements löser dessa problem genom att använda Federated block signing och Confidential Transactions.


Till skillnad från Bitcoin-nätverket är processen för block signing inom Elements inte beroende av DMMS (Dynamic Membership Multiparty Signatures) och Proof of Work (PoW). Istället använder Elements en Strong Federation av signatärer, så kallade Block Signers, som kan signera och skapa block på ett tillförlitligt sätt och i rätt tid. Detta tar bort transaktionsfördröjningen i PoW Mining-processen, som är föremål för stor blocktidsvarians på grund av dess slumpmässiga poissonfördelning. Den federerade block signing-processen uppnår tillförlitlig blockskapande utan att införa behovet av tredje parts förtroende.


Elements kan köras som en Sidechain till en annan Blockchain, t.ex. Bitcoin, eller som en fristående Blockchain utan beroenden till andra nätverk.


När Strong Federation används som en Sidechain innehåller den även medlemmar som möjliggör en säker och kontrollerad överföring av tillgångar mellan en huvudkedja och en Elements Sidechain. Den kontrollerade överföringen av tillgångar kallas Federated 2-Way Peg och medlemmar som utför rollen som överföring av tillgångar kallas watchmen.


De processer som är involverade i driften av ett Elements-nätverk och rollerna för deltagarna i nätverket är viktiga för att förstå hur Elements fungerar.


Oavsett om den implementeras som en Sidechain eller en fristående Blockchain använder Elements Strong Federations of Block Signers för att producera block.


### Starka federationer


Elements använder en konsensusmodell som först föreslogs av Blockstream och som kallas Strong Federations. En Strong Federation behöver inte Proof of Work (PoW) och förlitar sig istället på de kollektiva handlingarna från en grupp deltagare som litar på varandra, så kallade funktionärer.


De roller som en funktionär kan uppfylla inom en Strong Federation är: Blocksignatörer och watchmen. Blocksigners krävs om du kör Elements i antingen Sidechain- eller fristående Blockchain-läge, medan watchmen endast krävs i en Sidechain-konfiguration.


De åtgärder som en medlem i en Strong Federation kan utföra är uppdelade på två olika roller för att förbättra säkerheten och begränsa den skada som en angripare kan orsaka.


I kombination gör dessa deltagares roller att Elements kan leverera både snabb blockskapande (snabbare och slutlig transaktionsbekräftelse) och säkra, överförbara tillgångar (peggade tillgångar som är direkt länkbara till en annan Blockchain).


Du kan läsa whitepaper om starka federationer här: https://blockstream.com/strong-federations.pdf


### Blocktecknare


En Blockchain som Bitcoin:s förlängs när någon som ingår i en dynamisk grupp av blocksignatörer förlänger kedjan genom att visa att Proof of Work har förbrukats. Den dynamiska karaktären hos uppsättningen introducerar de latensproblem som är inneboende i sådana system.


Genom att använda en fast uppsättning undertecknare ersätter en Federated-modell den dynamiska uppsättningen med en känd uppsättning med flera signaturer. Genom att minska antalet deltagare som behövs för att utöka Blockchain ökar systemets hastighet och skalbarhet, samtidigt som validering av alla parter säkerställer transaktionshistorikens integritet.


Federated block signing består av flera faser:



- Steg 1 - Blocksignatörer föreslår kandidatblock i en rundgång till alla andra deltagande blocksignatörer.



- Steg 2 - Varje block signer signalerar sin avsikt genom att i förväg förbinda sig att underteckna det givna kandidatblocket.



- Steg 3 - Om det givna tröskelvärdet för pre-Commitment uppfylls, undertecknar varje block signer blocket.



- Steg 4 - Om signaturtröskeln (som kan skilja sig från den i steg 3) uppfylls accepteras blocket och skickas till nätverket. Strong Federation har nått konsensus om det senaste transaktionsblocket.



- Steg 5 - Nästa block föreslås sedan av nästa block signer i rundgången och processen upprepas.


Eftersom Strong Federation:s blockgenerering inte är probabilistisk och baseras på en fast uppsättning undertecknare, kommer den aldrig att bli föremål för omorganiseringar av flera block. Detta möjliggör en betydande minskning av väntetiden i samband med bekräftelse av transaktioner. Det tar också bort incitamentet att minera för vinst (dvs. blockbelöningarna) och ersätter det med ett incitament att produktivt delta i ett nätverk där alla deltagare har samma delade mål; att se till att nätverket fortsätter att fungera på ett sätt som är fördelaktigt för alla. Detta görs utan att införa en enda punkt av misslyckande eller högre förtroendekrav.


### Elements som en Sidechain - watchmen och Federated 2-Way Peg


När den körs som en Sidechain har vissa medlemmar av Strong Federation en ytterligare roll att uppfylla, den som watchmen. watchmen är ansvariga för överföringen av tillgångar till och från en Elements Sidechain, processer som kallas "Peg-In" och "Peg-Out".


För att en Sidechain ska fungera på ett tillförlitligt sätt måste den tillåta deltagare att verifiera att Supply av tillgångar är kontrollerad och verifierbar. En Elements Sidechain använder en 2-vägs federated peg för att möjliggöra tvåvägsöverföring av tillgångar in i och ut ur en Elements Blockchain. Detta uppfyller kraven på bevisbar utgivning och överföringar mellan kedjor.


Federated 2-Way Peg-funktionen gör det möjligt för en tillgång att vara interoperabel med andra blockkedjor och representativ för en annan Blockchain:s ursprungliga tillgång. Genom att koppla din Blockchain till en annan kan du utöka kapaciteten hos mainchain och övervinna några av dess inneboende begränsningar.


På en hög nivå sker överföringar till Sidechain när någon skickar mainchain-tillgångar till en Address som kontrolleras av en watchmen Wallet med flera signaturer. Detta fryser effektivt tillgångarna på mainchain. watchmen validerar sedan transaktionen och frigör samma belopp av den associerade tillgången inom Sidechain. De frigjorda tillgångarna skickas till en Sidechain Wallet som kan bevisa anspråk på de ursprungliga mainchain-tillgångarna. Denna process flyttar effektivt tillgångar från den överordnade kedjan till Sidechain.


För att överföra tillgångar tillbaka till mainchain gör en användare en särskild peg-out-transaktion på Sidechain. Denna transaktion kontrolleras av watchmen som sedan signerar en transaktionsutgift från multisignaturen Wallet som de kontrollerar på mainchain. Ett tröskelantal av deltagare i federationen måste signera innan mainchain-transaktionen blir giltig. När watchmen skickar tillbaka en tillgång till mainchain förstör de också motsvarande belopp på Sidechain, vilket effektivt överför tillgångarna mellan blockkedjorna.


## Konfigurera och köra Elements


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Eftersom Elements är baserad på Bitcoin-kodbasen är komponenterna som utgör ett fungerande nätverk mycket lika.


Själva nodprogramvaran Elements kallas "elementsd" och körs som en daemon på en användares dator. En daemon (eller tjänst i Windows) är ett program som körs som en bakgrundstjänst utan att kräva direkt kontroll av en inloggad användare.


Observera: I det här dokumentet kommer vi alltid att hänvisa till elementsd som daemon-versionen, men allt kan göras med Elements-qt, förutsatt att serveralternativet är aktiverat.


Elements daemon ansluter till andra noder i nätverket så att den kan Exchange transaktions- och blockdata, validera och utöka sin lokala kopia av nätverkets Blockchain.


Elements-programvaran består också av ett klientprogram som heter `elements-cli` som gör att du kan skicka Remote Procedure Call (RPC)-kommandon till elementsd från kommandoraden. Detta kan t.ex. användas för att fråga om ett Wallet-saldo, visa transaktions- eller blockdata eller sända en transaktion. Den här konfigurationen bör vara bekant för alla som har använt Bitcoin-ekvivalenterna bitcoind och bitcoin-cli.


Eftersom en Elements-nod kan konfigureras genom att skicka in parametrar vid uppstart eller via en konfigurationsfil är det möjligt att ha mer än en instans som körs på samma maskin. Detta är användbart för test- och utvecklingsändamål eftersom du kan konfigurera ditt eget lokala nätverk på en enda maskin, där varje Elements-nod har sin egen kopia av Blockchain-data, hanterar sin egen pool av obekräftade giltiga transaktioner och lyssnar på RPC-förfrågningar på olika portar.


### Elements:s kodförråd och gemenskap


Elements är ett projekt med öppen källkod och dess källkod finns i Elements GitHub-repository på https://github.com/ElementsProject/Elements. Förvaret innehåller källkoden för programmen elementsd och elements-cli tillsammans med stödjande installations- och byggverktyg, en uppsättning tester och viss instruktionsdokumentation.


Som komplement till kodarkivet finns också webbplatsen https://elementsproject.org, en community-fokuserad resurs som innehåller förklaringar av vad Elements är, hur det fungerar och en omfattande handledningssektion. Handledningen fokuserar på att lära sig om Elements genom att följa kommandoradsexempel och visar hur man bygger enkla skrivbords- och webbapplikationer ovanpå den. Webbplatsen listar också populära Elements-diskussionsforum och är själv värd på GitHub, vilket gör det möjligt för gemenskapen att bidra till webbplatsens innehåll.


För att kunna köra Elements på din maskin måste du först klona (ladda ner en kopia av) källkoden, installera alla beroenden som koden har och slutligen bygga daemon och klientens körbara filer. Elements-programvaran är sedan redo att konfigureras och köras.


## Konfigurera noder och nätverk


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Konfigurationsinställningar kan skickas till en Elements-nod vid start för att ändra hur den körs, validerar data, ansluter till andra noder och initierar sina Blockchain-data.


Inställningarna laddas antingen från den angivna filen `Elements.conf` eller skickas in som parametrar via kommandoraden.


Vissa saker kan ändras med hjälp av dessa parametrar:



- Namnet på den default asset som används i en fristående Blockchain-implementering.
- Numret på den första tillgång som skapats.
- Den tillgång som ska användas vid betalning av transaktionsavgifter i nätverket.
- Lagringsplatsen för Blockchain-datafilerna.
- RPC-autentiseringsuppgifter som används för att ansluta till en Bitcoin-nod.
- Tröskelvärdet "n av m" som ska uppfyllas och de giltiga publika nycklar som kan signera block.
- Det skript som måste uppfyllas för att överföra tillgångar till och från en Sidechain.
- Om du vill ansluta till en Bitcoin-nod som en Sidechain eller inte.


Många av dessa utgör en del av nätverkets konsensusregler, så det är viktigt att de tillämpas på alla noder vid uppstart. Vissa kan ändras efter att en kedja har initierats, medan andra måste åtgärdas efter att de har använts för att initiera en kedja.


Användningen av parametrar kommer att behandlas senare i kursen när de är relaterade till varje avsnitt.


### Grundläggande funktioner på kommandoraden


I den här kursen visas exempel där programmet `elements-cli` används för att göra RPC-anrop till en eller flera Elements-noder. Detta görs från en terminalsession och för att göra kommandona kortare kommer en "alias" att användas. Genom denna konvention när du ser något som följande kommandon:


```bash
e1-dae

e1-cli getnewaddress
```


`e1-dae` och `e1-CLI` är egentligen en typografisk genväg som utnyttjar terminalens `alias`-funktion. `e1-dae` och `e1-CLI` kommer faktiskt att ersättas när kommandot utförs och kommandot som körs kommer att se ut ungefär som:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


Det vi ser ovan är ett anrop för att starta Elements daemon och ett anrop till elements-cli-programmen som finns i katalogen `$HOME/Elements/src` och ett värde för parametern `datadir`. Med parametern `datadir` kan vi tala om för daemon och klientinstanserna var de ska hitta sina konfigurationsfiler och, i fallet med daemon, var de ska lagra sin kopia av Blockchain. Eftersom de delar en konfigurationsfil kommer klienten att kunna göra RPC-anrop till daemon.


Genom att köra ovanstående kommando igen, men med ett annat `datadir`-värde, kan vi starta mer än en instans av Elements, var och en med sin egen separata kopia av Blockchain och konfigurationsinställningar. Genom denna konvention kommer vi att använda alias `e2-dae` och `e2-CLI` i kursen för att hänvisa till en annan datadir-katalog än e1:s. Så ovanstående exempel för vår andra `e2`-instans skulle vara:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Detta kommer att göra det möjligt för oss att utföra alla typer av operationer som att överföra tillgångar mellan noder, utfärda tillgångar och kontrollera användningen av blinding i Confidential Transactions mellan olika noder i samma nätverk.


# Använda element Praktiskt användningsfall


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


I det här avsnittet får du lära dig hur du använder Confidential Transactions-funktionen i Elements.


Alla adresser i Elements är som standard blinded som använder Confidential Transactions, vilket gör att mängden och typen av tillgångar som överförs endast är synliga för deltagarna i transaktionen (och de som de väljer att avslöja Blinding key för), samtidigt som det kryptografiskt garanterar att inte fler mynt kan spenderas än vad som finns tillgängliga.


### Konfidentiella adresser och Confidential Transactions


När du skapar en ny Address i Elements med kommandot `getnewaddress` skapas den som standard som en Confidential Address.


För att demonstrera Confidential Transactions låter vi e2 skicka pengar till sig själv och sedan försöka se transaktionen från e1. Detta kommer att demonstrera transaktionernas konfidentiella natur i Elements.


Varje ny Address som genereras av en Elements-nod är konfidentiell som standard. Vi kan demonstrera detta genom att få e2 att generate en ny Address.


```
e2-cli getnewaddress
```


Observera att Address börjar med e1. Detta identifierar den som en Confidential Address. Om du undersöker Address mer i detalj med kommandot getaddressinfo visas mer information om Address.


```
e2-cli getaddressinfo <address>
```


Du kan se att det finns en confidential_key-egenskap som talar om för oss att det är en Confidential Address.


Confidential_key är den publika Blinding key, som läggs till själva Confidential Address. Detta är anledningen till att en Confidential Address är så lång.


Den har också en tillhörande Unconfidential address. Om du vill använda vanliga, icke-konfidentiella, transaktioner inom Elements, ska tillgångar skickas till denna Address istället för den med prefixet lq1.


Vi kan nu låta e2 skicka lite pengar till Address som den genererade. Detta kommer senare att visa att e1, eftersom den inte är en av de handlande parterna, inte kommer att kunna se detaljerna i transaktionen.


```
e2-cli sendtoaddress <address>
```


Notera transaction ID. Bekräfta transaktionen.


```
e2-cli -generate 101
```


Om man tittar på transaktionen där e2 skickade några medel till sig själv från e2:s perspektiv.


```
e2-cli gettransaction <txid>
```


Om du bläddrar upp i transaktionsinformationen kan du se att e2 kan se de belopp som skickats och mottagits samt den tillgång som transaktionen avser. Du kan också se egenskaperna amountblinder och assetblinder, som används för att dölja detaljerna för andra noder som inte är inblandade i transaktionen.


För att kontrollera detaljerna för samma transaktion från e1 måste vi först få de obearbetade transaktionsdetaljerna.


```
e1-cli getrawtransaction <txid>
```


Det returnerar rå transaktionsinformation. Om du tittar inom vout-avsnittet kan du se att det finns tre instanser. De två första instanserna är mottagnings- och ändringsbeloppen, och den tredje är transaktionsavgiften. Av dessa tre belopp är avgiften den enda där du kan se ett värde, eftersom avgiften i sig alltid är unblinded inom Elements.


### Bländande nycklar


Vad de två första vout-sektionerna visar är "Blinded ranges" av värdebeloppen och Commitment-data som fungerar som bevis på det faktiska beloppet och typen av tillgång som transaktionen avser.


Även om vi skulle importera e2:s privata nyckel till e1:s Wallet, skulle den fortfarande inte kunna se beloppen och typen av tillgång som transigerats eftersom den fortfarande inte har någon kunskap om den Blinding key som används av e2. Vi ska bevisa detta genom att importera den privata nyckel som används av e2:s Wallet till e1:s. Först måste vi exportera nyckeln från e2


```
e2-cli dumpprivkey <address>
```


Importera den sedan till e1.


```
e1-cli importprivkey <privkey>
```


Nu kan vi bevisa att e1 fortfarande inte kan se värdena.


```
e1-cli gettransaction <txid>
```


I själva verket visar den 0 som tx-beloppet när det faktiskt var 1.


För att kunna se det faktiska, olinjära värdet behöver vi Blinding key. För att göra detta exporterar vi först Blinding key från e2.


```
e2-cli dumpblindingkey <address>
```


Importera den sedan till e1.


```
e1-cli importblindingkey <address> <blinding key>
```


Nu när vi får transaktionsuppgifterna från e1.


```
e1-cli gettransaction <txid>
```


Det visar att med den importerade Blinding key kan vi nu se det faktiska värdet av 1 inom transaktionen.


I det här avsnittet har vi sett att användningen av en Blinding key döljer beloppet och typen av tillgångar i en transaktion, och att vi genom att importera rätt Blinding key kan avslöja dessa värden. I praktisk användning kan en Blinding key t.ex. ges till en revisor, om det finns behov av att verifiera belopp och typer av tillgångar som innehas av en part. Confidential Transactions-funktionen i Elements gör det också möjligt att utföra "intervallbevis". Range proofs kan bevisa att ett belopp av en tillgång hålls inom ett givet intervall, utan att det faktiska beloppet behöver exponeras.


Vi har också sett att Confidential Transactions är valfria, men aktiveras som standard när en ny Address genereras.


Det var allt för den här lektionen; lycka till med frågesporten och vi ses i nästa!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


I det här avsnittet får du lära dig hur du använder funktionen Issued Assets i Elements.


Issued Assets möjliggör att flera typer av tillgångar kan utfärdas och överföras mellan Elements nätverksdeltagare. Varje nod i nätverket kan utfärda sina egna tillgångar. Emissioner kan representera fungibla Ownership av vilken tillgång som helst inklusive vouchers, kuponger, valutor, insättningar, obligationer, aktier etc. Issued Assets öppnar dörren för att bygga Trustless börser, optioner och andra avancerade smarta kontrakt som involverar själv-Issued Assets.


En utställd tillgång drar också nytta av Confidential Transactions och de kan återutställas av alla som innehar den tillhörande token.


Det första steget är att vi behöver tillgång till två Elements-noder, som vi kallar e1 och e2. Noderna har fått sina blockkedjor återställda och default asset delade mellan dem.


De två noderna finns i samma lokala nätverk och är anslutna till varandra, och delar därför samma transaktioner i sina transaktion Mempool och identiska blockkedjor. Även om de körs på samma maskin är det värt att notera att de inte delar samma faktiska Blockchain-filer. Varje nod hanterar sin egen lokala kopia av Blockchain, som innehåller samma transaktionshistorik eftersom de är i konsensus och följer samma protokollregler som varandra.


Låt oss börja med att kontrollera varje nods syn på de befintliga tillgångsutgivningarna i nätverket.


Detta görs med hjälp av kommandot listissuances.


```
e1-cli listissuances

e2-cli listissuances
```


Som du kan se visar båda noderna samma emissionshistorik. De visar båda en tillgång, den initiala emissionen av 21 miljoner Bitcoin som skapades on chain initialisering. Du kan se tillgångens hex-id i resultatet av att köra kommandot ovan och även etiketten som tilldelats tillgången, som är "Bitcoin".


Det är värt att notera att default asset alltid får en etikett när kedjan initieras. När du utfärdar dina egna tillgångar kan du själv ange etiketter för dem, vilket vi kommer att göra inom kort. Innan vi kan göra det måste vi utfärda vår egen tillgång.


Vi låter e1 utfärda den nya tillgången. Detta görs med hjälp av kommandot issueasset.


```
e1-cli issueasset 100 1 false
```


`issueasset` accepterar 3 parametrar.


Beloppet för den nya tillgången som ska utfärdas, vi har använt 100. Mängden tokens som ska skapas (tokens används för att återutge mängder av en tillgång), varav vi valde 1. Den sista parametern talar om för Elements att antingen skapa tillgångsemissionen som blinded eller unblinded. Vi kommer att använda unblinded eftersom vi vill se emissionsbeloppen från e2 om en minut, så vi anger false.


Om du kör kommandot returneras data om utfärdandet. Dessa inkluderar transaction ID, som du kan ta en kopia av för senare användning, tillgångens unika hexvärde och det unika hexvärdet för tillgångens token.


generate ett block för att bekräfta utgivningstransaktionen.


```
e1-cli -generate 1
```


Kör kommandot `listissuances` mot e1 igen.


```
e1-cli listissuances
```


Det visar oss att e1 nu är medveten om 2 emissioner, den ursprungliga emissionen av Bitcoin och vår nyemitterade tillgång, som vi kan se 100 av. Notera hex-värdet för den nya tillgången och att det inte finns någon tillhörande tillgångsetikett, som det finns för Bitcoin-emissionen.


Kontrollera e2:s lista över kända utgåvor igen.


```
e2-cli listissuances
```


Det visar oss att e2 inte är medveten om den tillgångsemission som e1 gjorde. Den kan bara se den första emissionen av Bitcoin som den redan kunde se.


Detta beror på att e2 inte känner till, och inte bevakar, den Address som den nya tillgången skickades till när den utfärdades av e1.


Det är värt att notera att även om e2 inte kan se själva emissionen, kan e1 ändå skicka en del av tillgången till e2. Den nya tillgången skulle då dyka upp som ett tillgängligt saldo i e2:s Wallet, även om den inte är medveten om den ursprungliga emissionen.


För att e2 ska kunna se det faktiska utfärdandet (och därmed det utfärdade beloppet) måste vi lägga till Address i e2 som en bevakad Address.


För att göra detta måste vi ta reda på vilken Address som tillgången skickades till. För detta kommer vi att använda transaction ID som vi kopierade tidigare och låta e1 hämta detaljerna för den transaktionen så att vi kan ta reda på rätt Address att lägga till i Wallet-övervakningslistan för e2.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


Om du bläddrar upp förbi hex för transaktionsdata kommer du att se Address som fick 100 av vår nya tillgång, identifierad med sitt hexvärde.


Ta Address och kopiera den så att vi kan importera den till e2.


Låt oss nu importera Address till e2. För att göra detta använder vi kommandot importaddress.


```
e2-cli importaddress <the-issued-to-address>
```


Om vi nu kollar e2:s lista över utgivningar.


```
e2-cli listissuances
```


Du kan se att vår nyemitterade tillgång nu finns med i listan. E2-noden kan också fastställa beloppet för den tillgång som utfärdades, tillsammans med beloppet för den tillhörande token, eftersom utfärdandet var ett unblinded-utfärdande. För att aktivera användningen av tillgångs-ID till namnmappning inom Elements, stoppa först Elements.


```
e1-cli stop
```


Starta sedan om den med en ytterligare parameter som mappar tillgångens hex till den angivna etiketten. Detta gör att noden kan visa data om tillgången för oss i ett mer lättläst format. Du kan lägga till detta i slutet av Elements.conf om du föredrar det, då behöver du inte lägga till argumentet till daemon varje gång du startar den. Till exempel


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Men vi kommer att använda argumentmetoden här.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


Förfrågan till noden om en lista över utgivningar igen.


```
e1-cli listissuances
```


Det visar oss att mappningen av tillgångens hexadecimalvärde till dess etikett fungerar. Kontrollerar igen på e2-nodens lista över utgivningar.


```
e2-cli listissuances
```


Du kan se att noden e2 inte har tillgång till denna etikett, eftersom etiketter endast är tillgängliga för den nod som har ställt in dem. Vi kan faktiskt tilldela samma tillgångshex en annan etikett på e2 än vi gjorde på e1. Stoppa först noden e2.


```
e2-cli stop
```


Omstart med en annan etikett som tilldelats hex för vår nya tillgång.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


Listning av emissioner från e2.


```
e2-cli listissuances
```


Tillgångsetiketter är lokala för varje nod, endast tillgångens hex identifieras av andra noder i nätverket.


Mappningen av etikett till tillgångshex är användbar när du utför åtgärder som transaktioner och Wallet-saldofrågor, eftersom det möjliggör ett kortfattat sätt att hänvisa till en tillgång. Om vi t.ex. vill skicka en del av vår nya tillgång (ett belopp på 10) från e1 till e2 utan att använda etiketten.


Först måste vi skaffa en Address att skicka tillgången till.


```
e2-cli getnewaddress
```


Använd sedan kommandot sendtoaddress.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


Bekräfta transaktionen genom att generera ett block.


```
generate 1
```


Kontroll av att tillgången togs emot på e2.


```
e2-cli getwalletinfo
```


Vi kan se att tillgången verkligen togs emot.


Observera att e2 mappar hex för den mottagna tillgången och visar den med sin egen etikett. Ett enklare sätt att göra samma sak skulle vara att använda e1:s tillgångsetikett vid sändning.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Bakom kulisserna mappar Elements lokala etiketter till hexadecimala värden för att förenkla användningen av Issued Assets.


I detta avsnitt har vi sett hur man ger ut och märker tillgångar. I nästa avsnitt kommer vi att titta på återutgivning och förstöring av belopp av en utfärdad tillgång.


## Återutgivning av tillgångar


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


I det här avsnittet får du lära dig hur du kan ge ut mer av en redan utgiven tillgång och hur du kan förstöra en viss mängd av en utgiven tillgång.


Behovet av att återutge (skapa mer) av en tillgång eller förstöra ett belopp av tillgången är något som sannolikt kommer att uppstå när tillgången representerar något som inte har en fast Supply. Detta kan till exempel gälla tillgångar som representerar guld som förvaras i ett valv; när guldenheter rör sig in och ut ur valvet måste tillgången som representerar valvets Supply justeras upp eller ned i enlighet därmed.


Återutgivning av ett belopp av en tillgång kräver Ownership av den tillhörande token som skapades tillsammans med tillgången när den ursprungligen utgivits.


När du skapar mer av en tillgång spelar det ingen roll vilken nod som utfärdade tillgången i första hand, så länge den nod som återutger en mängd av en tillgång har vad som vanligtvis kallas tillgångens reissuance token. Vi kommer att titta på hur man initialt skapar reissuance token, hur man använder den för att återutge en mängd av en tillgång och även hur man överför reissuance token till andra noder, så att de också har behörighet att återutge tillgången.


Vi behöver tillgång till två Elements-noder, som vi kallar e1 och e2. Noderna har fått sina blockkedjor återställda och default asset har delats mellan dem.


Vi låter e1 emittera ett belopp på 100 av en ny tillgång och skapa 1 reissuance token för samma tillgång. Vi skapar emissionen som unblinded för att förenkla exemplet. Så låt oss gå vidare och emittera tillgången och dess tillhörande reissuance token.


```
e1-cli issueasset 100 1 false
```


Notera tillgångens ID och även ID:t för token (nyutgåva).


Eftersom vi senare kommer att återutge mer av tillgången från e2 måste vi notera den transaction ID som tillgången utfärdades i och använda den för att importera den Address som tillgången skickades till.


Bekräfta transaktionen.


```
e1-cli -generate 1
```


Vi ska nu kontrollera transaktionens detaljer med hjälp av kommandot gettransaction:


```
e1-cli gettransaction <txid>
```


Om du bläddrar upp förbi hexadelen av transaktionens data ser du att e1 i transaktionen erhöll 1 reissuance token och 100 av den tillhörande tillgången.


Ta en kopia av Address så att vi kan importera den till e2.


Och nu importerar jag Address till e2:s Wallet.


```
e2-cli importaddress <address>
```


Vi kan nu se att både e1 och e2 är medvetna om emissionen av tillgången.


```
e1-cli listissuances

e2-cli listissuances
```


För närvarande innehar e1 ett belopp av tillgången och 1 reissuance token men e2 gör det inte.


```
e1-cli getwalletinfo
```


Notera också att e1 har mindre av default asset än tidigare eftersom de betalade en liten summa för att täcka transaktionsavgifter. Detta belopp ska samlas in av e1 när det block som skapats är moget över 100 block djupt.


```
e2-cli getwalletinfo
```


Eftersom e1 innehar reissuance token kan den återutge fler av den. Detta görs genom att använda kommandot reissueasset. Låt oss låta e1 återutge ytterligare 100 av tillgången.


```
e1-cli reissueasset <asset-id> 100
```


Kontroll av att återutgivningen fungerade.


```
e1-cli getwalletinfo
```


Du kan se att e1 nu innehar 200 av tillgången som förväntat.


Eftersom e2 inte innehar ett belopp av reissuance token kommer de att få ett felmeddelande om de försöker ge ut tillgången på nytt.


```
e2-cli reissueasset <asset-id> 100
```


Notera felmeddelandet.


Vi kan visa detaljerna för återutfärdandet från e1 med kommandot listissuances.


```
e1-cli listissuances
```


Observera flaggan `is_reissuance`.


Om vi nu skickar e2 ett belopp av reissuance token kommer de att kunna återutge ett belopp av tillgången själva. Först behöver vi en Address att skicka den till. Det är värt att notera att reissuance token behandlas precis på samma sätt som alla andra tillgångar inom Elements vid sändning och visning av saldon och att den också kan brytas ned till mindre valörer som alla andra tillgångar, så vi behöver inte skicka 1 reissuance token till e2 för att de ska kunna återutge tillgången. Alla valörer är tillräckliga. Generera en Address för e2 för att ta emot reissuance token.


```
e2-cli getnewaddress
```


Skicka sedan en del av RIT från e1 till e2.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bekräfta transaktionen.


```
e1-cli -generate 1
```


Vi kan nu se att e2 håller de 0,1 som den skickades.


```
e2-cli getwalletinfo
```


Detta innebär att e2 nu kan återutge mer av tillgången som är kopplad till RIT som den innehar i sin Wallet. Vi kommer att låta e2 återutge 500 av tillgången.


```
e2-cli reissueasset <asset-id> 500
```


Kontrollera resultatet av återutfärdandet.


```
e2-cli getwalletinfo
```


Du kan se att e2 nu har det återutgivna beloppet i sitt Wallet-saldo och att RIT i sig inte förbrukas i processen för återutgivning av tillgångar.


Att förstöra ett belopp av en tillgång är något som alla som innehar minst det belopp som förstörs kan göra, det styrs inte av reissuance token.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


I detta avsnitt har vi sett hur man emitterar en tillgång och hur man använder reissuance token som eventuellt skapas som en del av emissionen av tillgången. Vi har också sett hur överföring av en reissuance token är lika enkelt som överföring av vilken annan tillgång som helst, och att innehav av en reissuance token ger innehavaren rätt att emittera mer av den associerade tillgången. Det är därför mycket viktigt att kontrollera vem som har tillgång till reissuance tokens i ditt nätverk. Vi har också sett hur man förstör en mängd av en tillgång och att denna process inte styrs av innehavet av reissuance token.


# Element Federation


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements stöder en federerad signeringsmodell som gör att du kan ange antalet Strong Federation-medlemmar som måste signera ett föreslaget block för att producera ett giltigt block.


Tidigare, och för att underlätta exemplet, har vi skapat block med hjälp av kommandot `generate`, som inte har behövt uppfylla ett krav på multisignatur för att de skapade blocken ska accepteras av nätverket som giltiga.


Vi kommer att ställa in våra noder så att de kräver skapande av 2-av-2 Multisig-block. Detta kommer att ställas in med parametern signblockscript, som kan läggas till i konfigurationsfilen eller skickas in i noden vid start. För att initiera en kedja med den här parametern måste vi först bygga skriptet som den består av.


Vi gör detta med hjälp av några befintliga noder, sparar de data de matar ut och raderar sedan kedjan så att vi kan starta om den med vår signblockscript-parameter. Detta är nödvändigt eftersom skriptet utgör en del av nätverkets konsensusregler och måste ställas in on chain initialisering. Det kan inte läggas till vid ett senare tillfälle i en redan befintlig kedja.


Vi behöver tillgång till två Elements-noder, som vi kallar e1 och e2. Noderna har fått sina blockkedjor återställda och default asset delat mellan sig.


Se till att parametern con_max_block_sig_size är inställd på ett högt värde i filen Elements.conf, annars kommer block signing att misslyckas längre fram i detta avsnitt. Vi har ställt in con_max_block_sig_size=2000 för den här handledningen.


Eftersom vi kommer att återställa Blockchain och radera plånböckerna som är kopplade till e1 och e2 måste vi ta en kopia av adresserna, de offentliga nycklarna och de privata nycklarna som vi använder för att generate block signing-skriptet så att vi kan använda dem senare.


Först behöver vi var och en av vad som kommer att vara block signing-noderna till generate en ny Address, som du måste ta en kopia av.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Sedan måste vi ta fram de publika nycklarna från adresserna och spara dem för senare användning.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Extrahera sedan de privata nycklarna, som vi återimporterar senare så att noderna kan signera blocken efter att vi återinitialiserar våra Blockchain- och Wallet-data.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Nu måste vi generate ett Redeem-skript med ett 2 av 2 multisignaturkrav. Vi gör detta genom att använda kommandot createmultisig och ange den första parametern som 2 och sedan tillhandahålla två offentliga nycklar. Det är dessa nycklar som Ownership of behöver bevisa senare när blocket skapas.


Vilken nod som helst, e1 eller e2, kan generate Multisig.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


Det ger oss vår redeemscript, som du kan kopiera för senare användning.


Nu måste vi radera de befintliga Blockchain- och Wallet-datan så att vi kan börja om med den nya signblockscript som en del av kedjans konsensusregler. Det är därför vi behövde ta en kopia av vissa data tidigare, till exempel de privata nycklar som kommer att användas i den nya kedjan för att signera block. Du måste göra detta innan du fortsätter.


Med våra befintliga Wallet- och kedjedata raderade kan vi nu starta våra noder och få dem att initiera en ny kedja med hjälp av parametern signblockscript. Låt oss skicka in -evbparams=dynafed:0::: för att inaktivera dynafed-aktivering, eftersom vi inte behöver den avancerade funktionen i det här exemplet.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Nu måste vi importera de privata nycklar som vi sparade tidigare så att våra noder kan signera och hjälpa till att slutföra föreslagna block.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


Användningen av generate-kommandot bör nu misslyckas eftersom det inte uppfyller de nödvändiga block signing-reglerna som nu tillämpas av våra noder.


```
e1-cli -generate 1
```


För att föreslå ett nytt block kan endera noden anropa kommandot getnewblockhex. Detta returnerar hexadecimalvärdet för ett nytt block som måste signeras innan det accepteras av några noder i vårt nätverk.


```
e1-cli getnewblockhex
```


Kom ihåg att kommandot bara skapar ett föreslaget block, det gör inte generate ett.


För att bekräfta detta kan vi se att det för närvarande inte finns några block i vår Blockchain.


```
e1-cli getblockcount
```


Om vi försöker skicka in blockhexen utan att först signera den.


```
e1-cli submitblock <block-hex>
```


Vi får ett meddelande som säger att blockbeviset är ogiltigt. Detta beror på att det ännu inte har undertecknats av två av de två parter som krävs.


Så låt oss få e1 att underteckna det föreslagna blocket.


```
e1-cli signblock <block-hex>
```


Låt e2 underteckna hexagonen.


```
e2-cli signblock <block-hex>
```


Lägg märke till att e2 inte signerar utdata som skapats genom att e1 signerat det föreslagna blocket. De signerar båda det föreslagna blockets hex oberoende av varandras resultat.


Nu måste vi kombinera blocksignaturerna för e1 och e2. Båda noderna kan göra detta, allt de behöver är den signerade blockhexen från den andra noden.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


Du kan se att kommandot combineblocksigs matar ut hex för det signerade blocket samt statusen complete, vilket innebär att blockets hex är redo att skickas in.


Nu kan endera noden skicka in den färdiga blockhexen. Vi låter e1 göra det.


```
e1-cli submitblock <combined-signed-hex>
```


Kontroll av att inlämningen var giltig.


```
e1-cli getblockcount

e2-cli getblockcount
```


Du kan se att både e1 och e2 har accepterat blocket som giltigt och lagt till det i spetsen på sina lokala kopior av Blockchain.


För att sammanfatta processen. I detta avsnitt har vi:


- Föreslog ett block.
- Fick varje nod att skriva under det.
- Kombinerade signaturerna.
- Kontrollerade att signaturerna är giltiga och uppfyller kedjans redeemscript-tröskel.
- Lämnade in blocket.


Varje nod i nätverket validerade blocket och lade till det i sin lokala kopia av Blockchain.


### block signing


Även om processen till en början verkar komplex är sekvensen block signing i Elements alltid densamma och den inledande installationen behöver bara utföras en gång:


1. Initial inställning (utförs en gång)

2. En multisignatur Address skapas med namnet `signblockscript` med hjälp av de offentliga nycklarna för Federated Block Signers.

3. Redeem-skriptet från detta används för att starta en ny Blockchain.

4. Blockproduktion (pågående)

5. Föreslagna block genereras och utväxlas för signering.


När ett visst antal personer har signerat det föreslagna blocket kombineras det och skickas till nätverket. Om det uppfyller kriterierna i kedjans `signblockscript` accepterar noderna det som ett giltigt block.


## Element som sidokedja


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements är en Blockchain-plattform med öppen källkod och allmänt användningsområde som också kan "kopplas" till en befintlig Blockchain, t.ex. Bitcoin. När Elements är peggad till en annan Blockchain sägs den fungera som en "Sidechain". Sidokedjor möjliggör dubbelriktad överföring av tillgångar från en kedja till en annan. Genom att implementera Elements som en Sidechain kan du arbeta runt några av de inneboende begränsningarna hos mainchain, samtidigt som du behåller en god grad av den säkerhet som tillhandahålls av tillgångar som är säkrade på mainchain.


Medan en Sidechain är medveten om mainchain och dess transaktionshistorik, har mainchain ingen medvetenhet om Sidechain och ingen krävs för dess drift. Detta gör det möjligt för sidokedjor att förnya sig utan begränsningar eller de förseningar som är förknippade med mainchain-protokollets förbättringsförslag. Istället för att försöka ändra det direkt, gör utvidgningen av huvudprotokollet att mainchain själv kan förbli säker och specialiserad, vilket understödjer den smidiga driften av Sidechain.


Genom att utöka funktionaliteten i Bitcoin och utnyttja dess underliggande säkerhet kan en Elements-baserad Sidechain tillhandahålla ny funktionalitet som tidigare inte var tillgänglig för användare av mainchain. Ett exempel på en Elements-baserad Sidechain som används i produktion är Liquid Network.


För att initiera en Elements Blockchain som en Sidechain måste vi använda parametern federated peg script. Denna parameter kan ställas in i en nods konfigurationsfil eller skickas in vid uppstart.


federated peg script definierar vilka medlemmar av Strong Federation som kan utföra peg-in- och peg-out-funktioner. Dessa funktionärer kallas `watchmen` eftersom de bevakar mainchain och Sidechain för giltiga peg-in och peg-out transaktioner och agerar på dem om de är giltiga. Att "pegga ut" innebär att flytta peggade tillgångar från Sidechain till mainchain och att "pegga in" innebär att flytta peggade tillgångar till Sidechain från mainchain. När vi säger "flytta in i Sidechain", menar vi egentligen att medlen låses i en multisignatur Address på mainchain och att ett motsvarande belopp av tillgången skapas på Elements Sidechain. När vi säger "flytta ut från Sidechain" menar vi att tillgångar förstörs på Elements Sidechain och att motsvarande belopp frigörs från de låsta medel som hålls på mainchain. Tillstånd att utföra peg-in- och peg-out-funktionerna kräver att funktionärerna bevisar Ownership de publika nycklar som används i federated peg script. Detta görs med hjälp av motsvarande privata nycklar.


För att kunna skapa en federated peg script måste vi därför först ha en publik nyckel för var och en av våra noder generate. Vi måste också lagra de tillhörande privata nycklarna för senare användning eftersom vi måste radera alla befintliga kedjedata och initiera en ny kedja med hjälp av federated peg script. Detta beror på att federated peg script utgör en del av konsensusreglerna för en Sidechain, och den kan inte tillämpas på en befintlig, icke-peggad, Blockchain vid ett senare tillfälle.


Så låt oss generate en Address med var och en av våra noder, lagra relevanta data för senare användning och generate federated peg script som vi kommer att använda för att initiera vår Sidechain senare.


Först måste var och en av våra noder, som kommer att fungera som watchmen i vårt nätverk, generate en ny Address.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Sedan validerar vi Address för att få de publika nycklarna.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Och hämta sedan de privata nycklar som är kopplade till varje Address.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Förvara de privata och offentliga nycklarna för senare användning.


Nu måste vi radera de befintliga Blockchain- och Wallet-data eftersom vi kommer att initiera en ny kedja med en federated peg script. Du kan göra detta nu. Glöm inte att starta Bitcoin daemon, som vi kommer att behöva pegga in.


Nu kan vi initiera en ny kedja med en federated peg script som skapats med hjälp av de publika nycklar vi lagrade tidigare. Siffrorna som vi anger och som omger våra publika nycklar definierar och avgränsar antalet nycklar som används, och nyckeln Ownership som måste bevisas för att kunna pegga in och ut ur vår Sidechain.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Nu ska vi importera de privata nycklar som vi sparade tidigare, så att våra noder senare kan signera och slutföra överföringen av tillgångar mellan kedjor och uppfylla kraven i federated peg script.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


Vi behöver nu mogna några block på båda kedjorna. Att blocken mognar är ett krav för peg-processen eftersom det skyddar mot blockomorganiseringar på mainchain som leder till en inflation av pegged asset Supply inom Sidechain.


För att hålla det här avsnittet fokuserat på federated peg kommer vi att generera block utan att använda block signing-modellen som vi tittade på i förra avsnittet, och återgå till att använda kommandot "generate" för att skapa nya block.


```
b-cli generate 101

e1-cli generate 1
```


Vi behöver inte nödvändigtvis generate block just nu för Elements. Men, låt oss generate ett ändå. Det är god praxis för att undvika potentiella inkonsekvenser.


Nu är vår kedja redo att peggas in. För att kunna pegga in måste vi generate en speciell typ av Address med kommandot getpeginaddress. Observera att tiden mellan att generera en peg-in Address med getpeginaddress och att göra anspråk på den med claimpegin bör hållas så kort som möjligt. peg-in-adresser är inte långsiktigt hållbara och bör inte återanvändas.


```
e1-cli getpeginaddress
```


Du kan se att kommandot skapar en ny mainchain Address, samt ett nytt skript som måste uppfyllas för att göra anspråk på peg-in-pengarna. mainchain Address är ett `betala till skript Hash` Address som kommer att användas av funktionärer som utför watchmen-rollen inom Elements-nätverket.


Precis som getnewaddress lägger getpeginaddress till en ny hemlighet i den anropande nodens Wallet, så det är viktigt att ta hänsyn till säkerhetskopiering av Wallet-filen i din nodhanteringsprocess.


Vi kommer nu att skicka lite Bitcoin från mainchain till Sidechain. Vårt mainchain regressionstest Wallet innehåller redan några medel.


```
b-cli getwalletinfo
```


Vi kan se att Wallet rymmer 50 Bitcoin. Vi skickar en Bitcoin från mainchain till Sidechain. Vi måste skicka pengar till mainchain Address som vår nod genererade tidigare.


```
b-cli sendtoaddress <e1-pegin-address>
```


Vi måste behålla ID:t för den här transaktionen eftersom vi behöver det som bevis på finansiering senare.


Vi kan nu se att saldot för mainchain Wallet har minskat med det belopp vi skickade, plus ytterligare ett litet belopp för att täcka transaktionsavgifterna.


```
b-cli getwalletinfo
```


Vi måste mogna transaktionen igen.


```
b-cli generate 101
```


För att vår Elements-nod ska kunna göra anspråk på peg-in-medlen måste vi få ett "bevis" på att peg-in-transaktionen har gjorts. Det kryptografiska beviset använder finansieringen transaction ID för att beräkna merkelvägen och bevisar att transaktionen finns i ett bekräftat block.


```
b-cli gettxoutproof '["<tx-id>"]'
```


Vi behöver också rådata om transaktionerna.


```
b-cli getrawtransaction <tx-id>
```


Med beviset och rådata för peg-in-transaktionen kan vår Elements-nod nu göra anspråk på peg-in med hjälp av rådatatransaktionen och transaktionsbeviset.


```
e1-cli claimpegin <raw> <proof>
```


Observera att det finns ett valfritt tredje argument som vi kunde ha gett till claimpegin. Denna tredje parameter kan användas för att ange till vilket Sidechain Address de begärda medlen ska skickas. Detta behövdes inte i vårt exempel eftersom vi anropade kommandot från samma nod som äger det Address som de begärda medlen ska skickas till.


Kontroll av saldot för e1.


```
e1-cli getwalletinfo
```


Genererar ett block för att bekräfta anspråket.


```
e1-cli generate 1
```


Kontroll av saldot för e1.


```
e1-cli getwalletinfo
```


Vi kan se att peg-in har tagits i anspråk på ett framgångsrikt sätt.


För att pegga ut är processen liknande. Genom att en Address genereras, medel skickas till den och medlen frigörs om transaktionen är giltig. Vi kommer inte att täcka hela peg-out-processen eftersom det innebär arbete med mainchain som ligger utanför omfattningen av denna kurs. Stegen när det gäller Elements-händelserna är att en Address genereras på mainchain.


```
b-cli getnewaddress
```


Pengar skickas till mainchain Address från en Elements-nod med hjälp av kommandot sendtomainchain.


```
e1-cli sendtomainchain <new-address> 1
```


Genererar ett block för att bekräfta transaktionen.


```
e1-cli generate 1
```


Kontrollera saldot på nodens Wallet.


```
e1-cli getwalletinfo
```


Och se att saldot har minskat.


I detta avsnitt har vi sett hur man:


- generate a federated peg script.
- Initiera en ny kedja som använder skriptet som en parameterregel för nätverksöverenskommelse.
- Skicka pengar från mainchain till Sidechain.
- Gör anspråk på medlen inom Elements Sidechain.
- Förstå hur sändning av medel tillbaka till mainchain startas.


### FederatedPegScript



För att Elements ska kunna fungera som en Sidechain måste Genesis-blocket i dess Blockchain skapas med ett `fedpegscript` på plats. Detta görs genom att skicka in parametern `fedpegscript` vid nodstart. Skriptet kommer sedan att utgöra en del av Elements Blockchain:s konsensusregler och tillåta att peg-in- och peg-out-begäranden valideras och åtgärdas.


"Fedpegscript" består av publika nycklar som kontrolleras av dem som är behöriga att utföra peg-handlingarna. Följande visar ett exempel på formatet för ett 2-av-2 multisignatur fedpegscript:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Observera: Tecknen utanför de publika nycklarna är avgränsare som anger krav på publika nycklar och `n av m`. Till exempel skulle mallen för ett 1-av-1 fedpegscript vara '5121<pub key 1>51ae'.


### Peg-in


Innan en peg-in kan accepteras av en Elements Sidechain måste den ha tillräckliga bekräftelser på mainchain. Detta är nödvändigt för att undvika inflation i Supply av pegged asset på Elements Sidechain som skulle kunna orsakas av en omorganisation av mainchain.


Korta omorganiseringar av spetsen på Bitcoin Blockchain förväntas som en del av den normala driften av Proof of Work (PoW) konsensusmekanism. Som sådan accepterar Elements endast en peg-in som giltig när den har tillräckligt djup inom Bitcoin Blockchain. Detta förhindrar Elements från att acceptera samma peg-in mer än en gång.


### Peg-Out


En peg-out inträffar när en Elements-nod anropar kommandot `sendtomainchain`, som tar som indata en mainchain Address (peg-out-destinationen) samt beloppet för pegged asset som ska `uttagas`. Detta skapar en peg-out-transaktion på Sidechain. När de funktionärer som agerar som watchmen upptäcker att peg-out-transaktionen har bekräftats på Sidechain, tar de hand om att faktiskt frigöra tillgången på mainchain till peg-out-destinationen, som vi lärde oss i tidigare avsnitt av kursen.


## Elements som en fristående Blockchain


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Hittills har vi tittat på hur man kör Elements som en Sidechain. Men den kan också fungera som en fristående Blockchain-lösning med sin egen standardtillgång. I den här konfigurationen behåller en Elements Blockchain fortfarande alla funktioner i en Sidechain-implementering, såsom Confidential Transactions och Issued Assets, men behöver inte peg-in eller peg-out för att lägga till eller ta bort default asset-belopp från cirkulationen.


I detta avsnitt kommer vi att:


Initiera en ny Elements Blockchain med en default asset med namnet `newasset`.


Ange 1 000 000 `nya tillgångar` som ska skapas tillsammans med 2 återutgivningstokens för den.


Gör anspråk på alla anyone-can-spend `nya tillgångar`-mynt.


Gör anspråk på alla anyone-can-spend-återutgivningstoken för "newasset".


Skicka tillgången och dess reissuance token till en annan nods Wallet.


Återutge mer "newasset" från båda noderna.


För att initiera ett Elements-nätverk så att det fungerar som en fristående Blockchain måste varje nod startas med några grundläggande parametrar. De används för att tala om för noden att den inte ska försöka validera peg-ins från en annan Blockchain, namnet på nätverkets default asset och hur många default asset och tillhörande reissuance token som ska skapas.


Vi startar en ny kedja med dessa parametrar på våra två anslutna Elements-noder nu. Vi namnger default asset `newasset` och ger ut en miljon av dem och två `newasset` återutgivningstokens.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Observera att de belopp som används här är i den minsta valör som nätverket kan acceptera, så de tvåhundra miljoner återutgivningstokens motsvarar faktiskt två hela tokens. Detsamma gäller för valören på de första gratismynten.


Kontrollera vår nods aktuella Wallet-saldon.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Vi kan konstatera att initieringen fungerade korrekt.


Eftersom den första emissionen av tillgångar skapas som "vem som helst kan spendera", kommer vi att låta e1 göra anspråk på dem alla så att vi kan ta bort e2: s tillgång till dem.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Observera att vi inte behöver ange "newasset" som den tillgång som ska skickas eftersom det redan är default asset. och därmed också den default asset som används för att betala nätavgifter.


Inom Elements kan du skicka flera tillgångstyper till samma Address, så vi kan återanvända den Address som vi just genererade för att ta emot default asset och använda den som destination Address för återutgivningstokens.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bekräfta transaktionerna.


```
e1-cli generate 101
```


Vi kommer att kontrollera att e1 är den enda innehavaren av tillgången och dess reissuance token nu.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Vilket vi kan se verkligen är fallet.


Nu skickar vi en del av "newasset" till e2, som för närvarande har ett saldo på noll.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Observera att vi inte behövde ange vilken typ av tillgång som skulle skickas, eftersom `newasset` har skapats som nätverkets default asset


Låt oss också skicka några av de återutfärdade tokens för `newasset` till e2.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bekräfta transaktionerna.


```
e1-cli generate 101
```


Vi kan kontrollera att plånböckerna har uppdaterats i enlighet med detta.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Nu ska vi återutge några av default asset från e1. Observera att möjligheten att göra detta aktiveras av startparametern initialreissuancetokens. Som om den utelämnas eller sätts till noll kommer att resultera i en default asset som inte kan återutges vid ett senare tillfälle.


```
e1-cli reissueasset newasset 100
```


Vi kunde använda etiketten `newasset` istället för att behöva ange hex-id-värdet eftersom en Elements-kedja alltid märker sin default asset.


Kontroll av att återutgivningen av default asset fungerade:


```
e1-cli generate 101

e1-cli getwalletinfo
```


Vi kommer nu att bevisa att eftersom e2 innehar några av `newasset` återutgivningstoken, kan det också återutge default asset.


```
e2-cli reissueasset newasset 100
```


Kontrollerar att återutgivningen av default asset av e2 fungerade.


```
e2-cli generate 101

e2-cli getwalletinfo
```


I det här avsnittet har vi konfigurerat Elements som en fristående Blockchain och kontrollerat att de grundläggande funktionerna fungerar som vi förväntar oss.


Vi använde startparametrar för att:


Initiera en ny Elements Blockchain med en default asset med namnet "newasset".


Ange mängden default asset för att skapa on chain-initialisering.


Skapa några återutgivningstoken för default asset och återutge fler av default asset från båda noderna.


I vårt fristående Blockchain Elements-nätverk kommer alla andra transaktionella operationer att fungera på samma sätt som de exempel som behandlas i kursens huvudavsnitt, men kommer att använda "newasset" istället för `Bitcoin` som standard- och avgiftstillgång.


### Parametrar för start av nod och initialisering av kedja


För att en Elements-nod ska kunna fungera som en fristående Blockchain måste några parametrar användas tillsammans. Vi ska ta en titt på var och en av dem nu och ta reda på vad de gör.


#### `validatepegin=0`

Eftersom en fristående Blockchain inte behöver validera några peg-in- eller peg-out-transaktioner måste vi inaktivera dessa kontroller. Med den här inställningen behöver du inte köra Bitcoin-klientprogramvaran eller lagra en kopia av Bitcoin Blockchain, eftersom Elements-nätverket kommer att fungera självständigt.


#### `defaultpeggedassetname`

Här kan du ange namnet på den default asset som skapas vid initiering av Blockchain.


#### `initialfreecoins`

Antalet (i motsvarigheten till Bitcoin:s Satoshi-enhet) default asset som ska skapas.


#### `initialutfärdande av teckensedlar`

Antalet (i motsvarigheten till Bitcoin:s Satoshi-enhet) av återutgivningstoken för default asset att skapa. Utan detta skulle det vara omöjligt att skapa mer av default asset. Om du inte vill att det ska vara möjligt att skapa fler default asset kan detta sättas till noll eller utelämnas.


Med hjälp av dessa parametrar skulle den vanliga starten av en nod se ut ungefär så här:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Grundläggande funktioner


Parametern `defaultpeggedassetname` ger en etikett till default asset. Utan denna inställning kommer default asset automatiskt att få namnet `Bitcoin`. I tidigare avsnitt, när vi skickade tillgångar som vi själva utfärdat till en annan nod, var vi tvungna att ange antingen tillgångens hex eller den lokalt tillämpade tillgångsetiketten för att tala om för Elements vilken tillgång vi skickade. Eftersom `defaultpeggedassetname` gäller för alla noder behöver vi inte namnge den när vi skickar den, även om dess namn inte är `Bitcoin`. Varje funktion som tidigare skulle ha skickat `Bitcoin` som standard kommer nu att skicka det som du valde att märka default asset som.


Så att skicka 10 av de nya default asset till en Address är så enkelt som:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Om du också har försett noden med ett värde för `initialreissuancetokens` större än noll så kommer du också att kunna återutge fler default asset, något som inte är möjligt om du kör Elements som en Sidechain.


För att göra detta behöver varje nod som innehar en mängd av token associerad med default asset bara utfärda ett kommando i formen:


```
e1-cli reissueasset <default asset name> <amount>
```


Genom att använda ovanstående parametrar kan du driva Elements som en fristående Blockchain med sin egen default asset, frikopplad från Bitcoin och andra blockkedjor.


## Slutsats


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


I den här kursen har vi lärt oss att Elements är ett nätverksprotokoll med öppen källkod som kan implementeras som en Sidechain till en annan Blockchain eller som en fristående Blockchain-lösning.


Vi har sett att källkoden och webbplatsen för Elements (https://github.com/ElementsProject/Elements) finns på GitHub och att det finns gemensamma diskussionsforum, som Build On L2 (https://community.Liquid.net/c/developers/) eller Liquid Developers Telegram (https://t.me/liquid_devel), som kan användas för att lära sig mer om att distribuera och utveckla applikationer på Elements och Liquid. Viktiga funktioner som Confidential Transactions och Issued Assets behandlades, tillsammans med hur medlemmar i en Strong Federation möjliggör federerad block signing och 2-vägs Peg-mekanismen.


Nästa steg är att utmana dig själv med en kumulativ frågesport som täcker alla tidigare avsnitt, för att sedan påbörja din Elements-resa ... lycka till!


# Sista avsnittet


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Recensioner & betyg


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Slutsats


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>