---
name: Konfigurera din första Bitcoin-nod
goal: Förstå, installera, konfigurera och använda en Bitcoin-nod
objectives: 


  - Förstå rollen och syftet med en Bitcoin-nod.
  - Identifiera de olika hårdvaru- och mjukvarulösningar som finns tillgängliga.
  - Installera och konfigurera en Full node (Bitcoin core).
  - Använd Interface Umbrel och lägg till användbara applikationer.
  - Anslut en personlig Wallet till sin egen nod.
  - Utforska avancerade inställningar och bästa säkerhetsrutiner.


---
# Bli en suverän bitcoiner



Du är förmodligen bekant med ordspråket "Inte dina nycklar, inte dina mynt", som uppmuntrar till självförvaring av dina bitcoins. Att hålla dina egna nycklar är verkligen ett viktigt första steg, men det räcker inte. För att uppnå sann monetär suveränitet måste du också installera och använda din egen Bitcoin-nod. Den här kursen är utformad för att vägleda dig genom detta grundläggande steg i din Bitcoin-resa!



BTC 202 är en lättillgänglig kurs som är utformad för att lära dig att spinna din egen Bitcoin-knut, även om du inte är en teknisk expert. Vi börjar med att definiera vad en Bitcoin-knut är, vad den är till för och varför det är absolut nödvändigt att snurra en själv. Sedan guidar jag dig steg för steg genom att välja maskinvara, installera nödvändig programvara, ansluta din Wallet och göra de första möjliga optimeringarna för att ta den vidare.



Att köra en Bitcoin-nod är inte bara ett alternativ för experter; det är en nödvändighet. Det är ett motståndskraftsverktyg som varje användare behöver förstå och implementera. Den här kursen är din startpunkt för att bli en suverän bitcoiner!




+++




# Inledning


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Kursöversikt


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Välkommen till BTC 202, där du får lära dig att installera, konfigurera och använda en Bitcoin-nod på ett enkelt och självständigt sätt. Men det är inte allt: du kommer också att lära dig mer om nodernas plats och funktion i Bitcoin-systemet. Kursen växlar mellan teoretiska förklaringar och handledd praktisk övning.



### Del 1 - Inledning



I denna första del av kursen kommer vi att klargöra de grundläggande begreppen och sedan gå vidare till mer exakta definitioner. Vad är en nod? Vilka är skillnaderna mellan nod, Wallet och Miner? Därefter får du lära dig mer om Bitcoin core och protokollets implementationer. Syftet är att tala samma språk, undvika förvirring och skapa en solid teoretisk grund.



### Del 2 - Att bli en suverän bitcoiner



I den här andra delen börjar jag med att förklara varför det är viktigt att köra din egen Bitcoin-nod. Vi kommer sedan att utforska de olika typerna av noder som finns (komplett, pruned, SPV ...), hur de fungerar och deras tekniska konsekvenser.



Vi ger dig sedan en översikt över den programvara som finns tillgänglig för att köra en Bitcoin-nod, inklusive dess fördelar och nackdelar. Slutligen kommer vi att avsluta med några mycket praktiska rekommendationer för att välja rätt hårdvara för dina behov och din budget.



Detta avsnitt illustrerar därför vägen för den suveräna bitcoinern: förstå varför det är nödvändigt att köra en nod, välja typ av nod, baserat på detta val, välja programvara och, beroende på den valda programvaran, bestämma lämplig hårdvara.



### Del 3 - Enkel installation av en Bitcoin-nod



När denna förberedelse är klar är det dags att bli praktisk med del 3 som ägnas åt Umbrel: hemmamolnets operativsystem som förenklar självhosting och installation av en Bitcoin- och Lightning-nod.



Efter en kort introduktion till Umbrel kommer vi att ge en detaljerad handledning för att guida dig genom installations- och konfigurationsprocessen på din egen DIY-maskin. Målet med denna del är tydligt: att ha din första fullt fungerande och synkroniserade Bitcoin-nod.



### Del 4 - Ansluta din Wallet till din nod



Nu när du har ställt in en Bitcoin-nod är det dags att använda den! I det här avsnittet lär du dig hur du ansluter din Wallet-hanteringsprogramvara (som Sparrow wallet) till din egen Address-indexerare (Electrs eller Fulcrum), eller direkt till Bitcoin core, så att du inte längre är beroende av offentliga servrar.



Vi kommer också att undersöka indexerarnas roll och de olika metoderna för att ansluta till din nod (LAN, Tor, Tailscale, etc.). Slutligen, i det sista kapitlet, kommer vi att granska de mest användbara applikationerna som finns tillgängliga på Umbrel för den dagliga bitcoinern.



### Del 5 - Avancerade koncept och bästa praxis



I den här sista delen av BTC 202 är målet att fördjupa din kunskap. Först ska vi titta på de bästa metoderna för att använda din nya Bitcoin-nod och hur du underhåller den på lång sikt.



Vi tar oss sedan tid att gå igenom en del av den teori som behandlats tidigare i kursen, inklusive att förstå IBD-processen och peer discovery i detalj, utforska en nods anatomi och slutligen lära oss hur man använder filen `Bitcoin.conf` för att finjustera dina inställningar.



### Del 6 - Sista avsnittet



Som med alla Plan ₿ Network-kurser hittar du i det sista avsnittet ett slutprov för att testa dina kunskaper om Bitcoin-noder.



Så, är du redo att slå på din första Bitcoin-nod? Sätt kurs mot suveränitet!



## Vad är en Bitcoin-nod?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Såsom det beskrivs av dess skapare, Satoshi Nakamoto, presenterar sig Bitcoin som ett elektroniskt kontantsystem peer-to-peer. Denna enkla mening, som är titeln på vitboken, innehåller många ledtrådar till Bitcoin:s natur:




- Först och främst beskriver Satoshi Bitcoin som ett "system", med andra ord en sammanhängande uppsättning hårdvaru- och mjukvarukomponenter som samverkar för att tillhandahålla en specifik tjänst eller utföra en specifik funktion;
- Därefter förklarar han att detta system gör det möjligt att använda elektroniska kontanter, dvs. en form av immateriell valuta;
- Slutligen påpekar han att detta system inte är beroende av någon central enhet: det är "peer-to-peer", vilket innebär att det är användarna själva som driver systemet.



Eftersom Bitcoin är ett system måste det nödvändigtvis köras på datorer. Och på grund av dess peer-to-peer-karaktär är det användarna själva som tar ansvar för att köra dessa maskiner. Vad vi kallar en "Bitcoin-nod" är just den dator på vilken programvara som implementerar Bitcoin-protokollet (som Bitcoin core, men vi återkommer till det senare) körs. Det är detta som gör att Bitcoin kan fungera utan en central myndighet: validering utförs på ett distribuerat sätt, av tusentals oberoende maskiner som tillhör tusentals användare.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Ett elektroniskt peer-to-peer-kontantsystem*. https://Bitcoin.org/Bitcoin.pdf



Det är just dessa användare som säkerställer Bitcoin:s säkerhet. Som Eric Voskuil förklarar i sin bok *Cryptoeconomics* är säkerheten för Bitcoin varken beroende av Blockchain, hashkraft, validering, decentralisering, kryptografi, öppen källkod eller spelteori. Säkerheten för Bitcoin beror främst på de individer som är villiga att utsätta sig för personlig risk. Decentralisering gör att denna risk kan spridas över ett stort antal individer, och det är bara deras förmåga att stå emot som säkerställer systemets robusthet.



Principen är lätt att förstå: om Bitcoin var beroende av en enda nod som ägdes av en enda person skulle det räcka med att fängsla den personen för att stänga ner nätverket, eftersom denne ensam skulle stå för alla risker. Med tiotusentals noder spridda över hela världen sprids risken: var och en av dessa operatörer skulle behöva neutraliseras för att stänga av Bitcoin.



![Image](assets/fr/048.webp)



Vi kan alltså urskilja och namnge flera begrepp för att klargöra saker och ting för resten av den här kursen:




- Bitcoin valuta: den beräkningsenhet som används för transaktioner inom detta system;
- Bitcoin-nätverket: uppsättningen av alla anslutna noder;
- Bitcoin-noder: maskiner som kör en implementation av Bitcoin;
- Bitcoin-implementeringar: programvara som översätter protokollet till körbara instruktioner;
- Bitcoin protokoll: den uppsättning regler som styr systemets funktion;
- Bitcoin-systemet: den sammanhängande kombinationen av alla dessa Elements.



### Bitcoin-nodens roll



Bitcoin-noderna bildar tillsammans det så kallade Bitcoin-nätverket. De gör det möjligt för hela systemet att fungera autonomt, utan att behöva vända sig till en central myndighet eller en hierarki av servrar.



Bitcoin var från början utformad för att varje användare skulle kunna köra en personlig nod. Detta är fortfarande fallet med dagens Bitcoin core-programvara, som kombinerar rollerna som Wallet och nod. Men nuförtiden är denna funktion ofta åtskild: många moderna Bitcoin-plånböcker är bara plånböcker som ansluter till externa noder (som ägs av samma person eller inte).



### Behåll Blockchain



Den första uppgiften för en nod är att upprätthålla en lokal kopia av Blockchain. För att förhindra Double-spending på Bitcoin utan att involvera en central myndighet måste varje användare kontrollera att det inte finns någon transaktion i systemet. Det enda sättet att vara säker på detta är att känna till alla transaktioner som gjorts på Bitcoin. Av denna anledning tidsstämplas alla transaktioner och grupperas i block, och varje nod lagrar hela Blockchain.



> Det enda sättet att bekräfta att en transaktion inte har ägt rum är att vara medveten om alla transaktioner.

Nakamoto, S. (2008). *Bitcoin: Ett elektroniskt peer-to-peer-system för kontanter*. https://Bitcoin.org/Bitcoin.pdf



Blockchain är därför ett register som utvecklas: varje gång ett nytt block publiceras av en Miner kontrollerar noden dess giltighet innan den lägger till det i sin egen lokala kopia av kedjan. I dag (juli 2025) är hela Blockchain över 675 GB, och storleken fortsätter att växa eftersom ett nytt block läggs till i genomsnitt var 10:e minut.



![Image](assets/fr/049.webp)



Noden upprätthåller också ett lokalt register över alla UTXO som finns vid en given tidpunkt, känt som **UTXO-uppsättningen**. Denna databas innehåller alla oanvända Bitcoin-fragment. Vi återvänder till detta ämne i detalj i den sista delen av kursen.



### Verifiera och distribuera transaktioner



Den andra rollen för en nod är att säkerställa verifiering och spridning av transaktioner. När en ny transaktion når noden (antingen via Wallet-mjukvaran eller en annan nod) kontrollerar den att den följer en uppsättning regler (konsensusregler och reläregler). Ett exempel:




- förbrukade bitcoins måste finnas i dess UTXO-uppsättning (databasen med outnyttjade utgångar);
- signaturen måste vara giltig och alla utgiftsvillkor måste vara uppfyllda (giltigt manus);
- den totala mängden prestationer får inte överstiga den totala mängden insatser, vilket innebär att kostnaderna inte kan vara negativa.



![Image](assets/fr/050.webp)



Efter validering lagras transaktionen i nodens Mempool, ett tillfälligt minnesutrymme som reserverats för obekräftade transaktioner, och vidarebefordras sedan till de andra nätverksmotparter som den är ansluten till. Denna distributions- och valideringsmekanism fortsätter från nod till nod. På så sätt sprids transaktionen över Bitcoin-nätverket och varje nod lagrar den i Mempool tills den inkluderas i ett giltigt block av en Miner, som sedan agerar på dess första bekräftelse.



### Kontrollera och distribuera block



Nodens tredje roll handlar om att hantera minade block. När en Miner upptäcker ett nytt block med en giltig Proof of Work sänds det ut i nätverket. Noderna tar emot det, kontrollerar att det överensstämmer med alla protokollregler och integrerar det sedan i sin egen lokala kopia av Blockchain om det är giltigt. Precis som med transaktioner vidarebefordras nyligen validerade block till alla peers som är anslutna till noden. Denna process fortsätter tills alla noder i Bitcoin-nätverket är medvetna om det nya blocket.



![Image](assets/fr/051.webp)



## Vad är skillnaden mellan en pilbåge och en Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Det är viktigt att skilja mellan två olika typer av programvara när du använder Bitcoin: noden och Wallet.



En Bitcoin-nod är, som nämnts ovan, en mjukvara som aktivt deltar i peer-to-peer-nätverket. Den utför tre huvuduppgifter:




- backup av Blockchain,
- validering och vidarebefordran av transaktioner,
- blockvalidering och relä.



En Bitcoin Wallet är å andra sidan en programvara som är utformad för att lagra och hantera dina privata nycklar. Dessa nycklar gör att du kan spendera dina bitcoins genom att uppfylla låsskripten (vanligtvis genom en signatur). En Wallet kan ansluta till en nod (oavsett om den är lokal eller fjärransluten) för att se statusen för Blockchain och sända de transaktioner som den bygger upp, men den är inte i sig en deltagare i nätverket.



I vissa fall samexisterar dessa två funktioner inom samma programvara, vilket är fallet med Bitcoin core, som fungerar som både en Full node och en Wallet. Många populära Wallet-program (Sparrow, BlueWallet etc.) kräver dock en anslutning till en extern nod (antingen din egen eller en tredje parts) för att sända transaktioner och fastställa Wallet-saldot.



![Image](assets/fr/052.webp)



## Vad är skillnaden mellan en nod och en Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Begreppen nod och Miner förväxlas ofta. Ändå utför dessa två Elements radikalt olika funktioner inom systemet.



När Bitcoin lanserades av Satoshi Nakamoto 2009 förväntades varje användare delta i nätverket som helhet. Den ursprungliga programvaran Bitcoin kombinerade därför flera funktioner samtidigt: den fungerade som en Wallet, en nod, och även som en Miner, som kunde generera nya block. Vid den här tiden var svårighetsgraden för Mining mycket låg. Allt du behövde göra var att köra programvaran Bitcoin på din dator för att hitta block och få bitcoins som belöning.



I och med den gradvisa populariseringen av Bitcoin och ökningen av antalet gruvarbetare har dock konkurrenslandskapet i Mining genomgått en radikal förändring. Idag har Mining blivit en extremt konkurrensutsatt aktivitet som domineras av industriella aktörer utrustade med specialiserad infrastruktur. Den kraft som krävs för att bryta ett nytt block är nu så stor att det är praktiskt taget omöjligt för en enskild användare att åstadkomma detta med hjälp av endast en konventionell dator. Som ett resultat av detta utförs Mining nu främst med hjälp av specialiserade maskiner som kallas ASICs (*Application-Specific Integrated Circuits*). Dessa chip är optimerade uteslutande för att köra dubbel SHA-256, den algoritm som används för Mining på Bitcoin.



![Image](assets/fr/053.webp)



Mot bakgrund av denna utveckling har rollerna för Bitcoin-noden och Miner blivit tydligt åtskilda. Som visas ovan är rollen för en Bitcoin-nod enbart informations- och valideringsbaserad. Miner:s roll är annorlunda:




- Den väljer ut pågående transaktioner i Mempool.
- Den bygger upp ett kandidatblock som integrerar dessa transaktioner.
- Han söker efter en giltig Proof of Work genom att pröva sig fram.
- Om den hittar ett giltigt bevis sänder den blocket via sin nod till de andra noderna.



En Miner behöver en Bitcoin-nod för att interagera med nätverket.



Miner:s roll skiljer sig också ibland från hackarens. En huggare är en maskin vars uppgift är att Hash mallblock som levereras av en pools server, leta efter hashes som uppfyller svårighetsmålet som definierats för aktier, och inte Bitcoin. Resten av Mining-processen, som inkluderar faktisk blockkonstruktion, transaktionsval eller Proof-of-Work-sökning enligt Bitcoin:s egen svårighetsgrad, samt distribution, utförs direkt av poolerna.



![Image](assets/fr/054.webp)



Slutligen finns det en viktig skillnad i fråga om ekonomiska incitament mellan Miner och noden. Att driva en Bitcoin-nod ger ingen direkt monetär fördel. Att delta i Mining ger å andra sidan belöningar (subventioner och transaktionsavgifter) för varje block som hittas.



I del 2 kommer vi att utforska mer i detalj de praktiska och personliga fördelarna med att installera och använda en Bitcoin-nod, utöver de rent ekonomiska.



## Bitcoin core och protokollimplementeringar


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin-protokollet är ingen programvara, utan en uppsättning tysta regler som delas mellan nätverksanvändare. Det definierar villkor för transaktionsgiltighet, mekanismer för skapande av pengar, blockformat, Proof-of-Work-villkor och många andra specifikationer. För att interagera med detta protokoll måste användarna köra programvara som implementerar dessa regler: detta kallas en **implementering** av Bitcoin.



En implementering är därför nodprogramvara: ett program som kan samverka med andra maskiner i Bitcoin-nätverket, ladda ner, verifiera, lagra och sprida block och transaktioner samt lokalt upprätthålla konsensus- och reläregler. Varje implementation är en konkret tolkning av protokollet, skriven i ett givet programmeringsspråk, med sin egen arkitektur, prestanda och ergonomi. Varje implementation kommer också att ha sin egen utvecklingsorganisation, med sin egen ansvarsfördelning.



Bland dessa implementeringar dominerar en överlägset: **Bitcoin core**.



![Image](assets/fr/055.webp)



### En historisk implementering som har blivit ett riktmärke



Bitcoin core är referensprogramvaran för Bitcoin-protokollet. Den härstammar från den ursprungliga koden som skrevs av Satoshi Nakamoto 2008-2009 och är en direkt fortsättning på den. Ursprungligen känd som "*Bitcoin*", sedan "*Bitcoin QT*" (på grund av tillägget av en grafisk Interface via Qt-biblioteket), döptes den om till "*Bitcoin core*" 2014 för att tydligt skilja programvaran från nätverket. Sedan version 0.5 har den distribuerats med två komponenter: `Bitcoin-qt` (den grafiska Interface) och `bitcoind` (kommandoraden Interface).



I teorin representerar Bitcoin core inte Bitcoin-protokollet; det är snarare bara en implementering bland många. Det utmärker sig dock genom sin massiva användning, sin ålder, robustheten i sin kod och stringensen i sin utvecklingsprocess. I praktiken är därför de regler som tillämpas av Bitcoin core de facto de som gäller för Bitcoin-protokollet: användare, utvecklare, gruvarbetare och ekosystemtjänster hänvisar nästan uteslutande till det.



### Nuvarande fördelning av implementeringar



Enligt [data som samlades in i augusti 2025 av Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (en välkänd utvecklare i ekosystemet) är fördelningen av implementeringar bland nätverkets publika noder enligt följande:




- Bitcoin core**: 87.3% av noderna
- Bitcoin Knots**: 12.5
- Andra kumulativa implementeringar**: 0.2% (btcsuite, Bcoin, BTCD ...)



![Image](assets/fr/056.webp)



Med andra ord kör cirka 9 av 10 publika noder Bitcoin core. Resten av nätverket förlitar sig på mer marginella klienter (även om Knots andel har ökat kraftigt under de senaste månaderna, inte minst i kölvattnet av debatterna om storleksgränsen för `OP_RETURN`). Dessa alternativa implementeringar underhålls ofta av en enda person eller ett litet team.



**Anmärkning:** Dessa siffror är dock fortfarande uppskattningar, eftersom de främst baseras på *lyssnande noder*, dvs. noder som accepterar inkommande anslutningar (med port 8333 öppen). Icke-lyssnande noder* är mycket mer komplicerade att räkna, eftersom det är omöjligt att ansluta till dem direkt: du måste vänta på att initiativet ska komma från dem, i form av en utgående anslutning. Luke Dashjrs webbplats påstår sig försöka räkna dessa *icke-lyssnande noder* också, men det är fortfarande omöjligt att få helt korrekta uppgifter om dem, och uppdateringen av denna statistik släpar oundvikligen efter verkligheten.



### Intern drift av Bitcoin core



Bitcoin core är skrivet i C++. Det är också ett projekt med öppen källkod som underhålls av en grupp utvecklare som arbetar frivilligt eller får betalt av olika enheter (ofta av företag i ekosystemet som har ett intresse av Cores utveckling). [Koden finns på GitHub] (https://github.com/Bitcoin/Bitcoin) och utvecklingen följer en rigorös:




- Bidragsgivare** skickar in förslag i form av _pull requests_ (PR). I princip kan vem som helst föreslå en ändring, men den måste testas, dokumenteras och genomgå en peer review-process.
- **Underhållarna** har rätt att godkänna och sammanfoga PR:er. Det är de som garanterar att projektet är sammanhängande och stabilt. I juli 2025 finns det fem av dem: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao och Ryan Ofsky.
- Det har inte funnits någon **principal underhållare** sedan februari 2023. Denna roll innehades ursprungligen av Satoshi Nakamoto vid lanseringen av Bitcoin, sedan av Gavin Andresen efter Nakamotos avgång i början av 2011, och slutligen av Wladimir J. Van Der Laan från 2014 till 2023.



![Image](assets/fr/057.webp)



Utvecklingen av Bitcoin core följer en meritokratisk logik: nya bidragsgivare uppmuntras att granska och testa koden innan de själva föreslår några ändringar. Besluten baseras på teknisk konsensus och större ändringar (särskilt inom områden där konsensus råder) kräver diskussioner uppströms på offentliga kanaler, t.ex. e-postlistor eller PR-recensionsklubbar.



### Andra Bitcoin-implementeringar



Även om de är marginella när det gäller adoption finns det andra klienter. Den viktigaste är Bitcoin Knots, utvecklad av Luke Dashjr, en Fork av Bitcoin core som innehåller ytterligare alternativ och en mer konservativ inställning till utveckling. Dessa inkluderar strängare restriktioner för transaktionsformat.



![Image](assets/fr/058.webp)



Vi kan också nämna:




- Libbitcoin**: ett modulärt C++-bibliotek som utvecklats av Amir Taaki och underhålls av Eric Voskuil;
- Bcoin**: en JavaScript-implementering, som inte längre underhålls aktivt;
- BTCD/btcsuit**e: en implementering i Go.



Dessa projekt bidrar till mångfalden i ekosystemet, men deras användning är fortfarande mycket begränsad, vilket gör det svårt för Bitcoin core att utvecklas självständigt.



### Kraften hos Core-utvecklare



Du kanske tror att Bitcoin core-utvecklare har direkt kontroll över Bitcoin, men så är inte fallet. De kan inte införa en ändring av protokollet. Deras roll är att föreslå kod. Det är upp till varje användare, via sin nod, att besluta om de vill använda denna kod eller inte.



Det innebär att om en ändring i Bitcoin core inte når konsensus kan den ignoreras av noderna, antingen genom att inte uppdatera Bitcoin core eller genom att helt enkelt ändra implementeringen. Omvänt, om en funktion som användarna vill ha blockeras i Core-utvecklingsprocessen, är det alltid möjligt att byta till en annan implementering eller Fork projektet.



Som vi kommer att diskutera senare i den här kursen är det noderna, enligt deras ekonomiska vikt (dvs. handlarna), som ger nytta till en version av protokollet (och därmed till motsvarande valuta) genom att acceptera enheter som respekterar dess regler. Den verkliga makten att styra över Bitcoin ligger därför hos dessa handlare, inte hos utvecklarna.




# Bli en suverän bitcoiner


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Varför slå knut på sig själv?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Det finns en utbredd uppfattning om att driften av en Bitcoin-nod är en rent altruistisk handling, utan personlig vinning, enbart i syfte att decentralisera nätverket. Vissa anser att det är en form av plikt för bitcoiners att stödja systemet och visa sin tacksamhet till Bitcoin.



Som vi påpekade i de föregående kapitlen finns det ingen direkt ekonomisk vinning i att slå en knut. Man kan därför tycka att det inte finns något personligt intresse av att göra det. Ändå ger det många individuella fördelar att driva en egen nod. För att övertyga dig om detta kommer jag i det här kapitlet att presentera alla skäl, både tekniska och strategiska, till varför du bör installera och använda din egen Bitcoin-nod.



### Mer konfidentiell spridning av transaktioner



När Wallet-programvaran ansluter till en extern nod överför den sina transaktioner till en infrastruktur som inte står under din kontroll. Detta medför uppenbara risker för övervakning: operatören av den externa noden kan analysera detaljerna i dina transaktioner, inklusive belopp och frekvenser, och genom att dubbelkolla vissa metadata (t.ex. IP-adresser, tidpunkter och platser) kan de eventuellt koppla dem till din identitet.



Som påpekades i ett tidigare kapitel kommunicerar plånböcker inte med Bitcoin-nätverket genom magi; de måste ansluta till en nod för att kunna konsultera saldon eller sända transaktioner. Om du aldrig har satt upp en egen nod innebär det att din Wallet är beroende av infrastrukturen hos en tredje part (vanligtvis företaget bakom programvaran). Denna tredje part, särskilt om det är ett företag, kan observera, utnyttja eller till och med avslöja dessa data: antingen av kommersiella skäl, under juridisk begränsning eller som ett resultat av piratkopiering.



![Image](assets/fr/059.webp)



Genom att använda din egen nod sänder du dina transaktioner direkt till nätverket och kringgår mellanhänder. Förutsatt att du säkrar din nod ordentligt (vilket vi kommer att diskutera senare) eller följer vissa standarder, exponeras ingen information: varken din IP Address eller detaljerna i dina transaktioner passerar genom en enhet som du inte kontrollerar. Detta är en grundläggande förutsättning för att bevara din konfidentialitet på Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Icke-skadliga transaktioner



Av samma skäl som nämns ovan är Wallet-programvara som baseras på en tredjepartsnod sårbar för censurrisker: operatören av fjärrnoden kan av olika skäl vägra att vidarebefordra vissa transaktioner. Den kan anse att de är misstänkta eller strider mot dess policy. Transaktionen kan också blockeras om den inte överensstämmer med nodens regler för vidarebefordran. Slutligen kan operatören rikta in sig specifikt på din IP Address för att blockera sändningen av dina transaktioner.



Omvänt, genom att använda din egen nod säkerställer du spridningen av dina transaktioner inom peer-to-peer-nätverket. Detta innebär att du behåller total kontroll över distributionen av dina transaktioner, utan att vara beroende av en mellanhand. Så länge som transaktionen följer konsensus- och reläreglerna för de noder som är anslutna till din, kommer den att sändas ut i nätverket och sedan, förutsatt att tillräckliga avgifter ingår, integreras i ett block av en Miner. Att ha din egen nod garanterar en neutral, tillståndsfri bekräftelse av dina transaktioner.



### Oberoende verifiering av data



Utan en personlig nod är du beroende av en tredje part för att få tillgång till information, t.ex. ditt Address-saldo, status för transaktionsbekräftelse och blockgiltighet. Detta innebär ett underförstått förtroende för den externa nodens riktighet och integritet.



![Image](assets/fr/060.webp)



Att köra en Full node innebär att du kan kontrollera alla protokollregler själv, för varje transaktion och varje block. Som ett resultat är saldot som visas av din Wallet inte data som tas emot från en fjärrserver, utan ett resultat som beräknas lokalt från en fullständig kopia av Blockchain, validerad block för block. Detta tillvägagångssätt ger full mening åt bitcoiners maxim:



> Lita inte, verifiera.

### Bättre fördelning av systemsäkerhet



Varje nod som ansluter sig till nätverket förstärker Bitcoin:s redundans och motståndskraft. Det underlättar spridningen av information och gör det möjligt för nya peers att ansluta till varandra. Utan noderna skulle systemet helt enkelt vara obrukbart.



Som vi har sett är Bitcoin:s säkerhet inte baserad på decentralisering, Mining eller kryptografi: som med alla system är den beroende av individer. Mer exakt beror det på nodoperatörernas förmåga att motstå tvång.



Det som utmärker decentraliserade system som Bitcoin är riskfördelningen mellan alla som är involverade i deras drift. Att driva din egen Bitcoin-nod innebär att du accepterar en del av denna risk genom att säkerställa säkerheten för din instans; genom att göra det lättar du också riskbördan för andra nodoperatörer.



Så det är inte en direkt personlig fördel: att driva en nod gör dig delvis ansvarig för nätverkets säkerhet. Framför allt är det en kollektiv fördel, eftersom ditt engagemang bidrar till att sprida risken. I sin tur ökar du din egen förmåga att använda Bitcoin på ett tillförlitligt sätt.



### Fördjupa din förståelse för systemet



Att installera en Full node är ingen trivial operation. Det handlar om att installera programvara, förstå grundläggande funktioner, övervaka synkronisering, granska loggar vid problem och till och med använda terminalen. Detta kommer med nödvändighet att leda till att du fördjupar din förståelse för protokollet. Detta är en indirekt, men inte obetydlig fördel.



Att skaffa sig denna kunskap stärker ditt förtroende för verktyget och kan minska risken för fel eller att du utsätts för bedrägerier. Att snurra sin egen knut är också en form av lärande.



### Välja vilka regler som ska tillämpas



En viktig aspekt, som ofta missförstås, är att man genom att driva en nod kan välja vilka regler som ska gälla lokalt. Det finns två huvudtyper av regler:





- Samförstånd råder**:



Dessa är de grundläggande reglerna i Bitcoin-protokollet, som säkerställer systemets integritet och fastställer kriterierna för validering av transaktioner och block. En transaktion som inte följer dessa konsensusregler kan aldrig ingå i ett giltigt block. Till exempel kommer en transaktion med en ogiltig signatur på en av sina poster systematiskt att uteslutas.



Att ändra dessa regler är detsamma som att ändra protokollet och därmed valutan (Hard Fork). Men även utan att försöka ändra dem ger det enkla faktum att de befintliga reglerna tillämpas strikt en viss makt: om ett block bryter mot reglerna avvisar noden det omedelbart.





- Stafettregler**:



Detta är regler som är specifika för varje Bitcoin-nod och som läggs till konsensusreglerna för att definiera strukturen för obekräftade transaktioner som accepteras i Mempool och vidarebefordras till peers. Varje nod konfigurerar och tillämpar dessa regler lokalt, vilket förklarar varför de kan skilja sig från en nod till en annan. De gäller endast obekräftade transaktioner: en transaktion som av en nod anses vara "icke-standard" kommer endast att accepteras om den redan finns i ett giltigt block. Att ändra dessa regler utesluter inte noden från Bitcoin-systemet.



Till exempel är en transaktion utan avgifter enligt konsensusreglerna helt giltig, men den kommer att avvisas som standard enligt Bitcoin core:s reläpolicy, eftersom parametern `minRelayTxFee` är inställd på `0,00001` (i BTC/kB). Det är dock möjligt att på din egen nod sänka detta tröskelvärde för att vidarebefordra transaktioner med lägre avgifter, eller omvänt att höja gränsen, till exempel till 2 Sats/vB, för att undvika att vidarebefordra transaktioner med låga avgifter.



Att spinna sin egen nod innebär att hävda: "Jag validerar det jag väljer att validera, enligt de regler som jag själv har antagit"*. Du blir därmed en aktör i styrningen av systemet, och kan avvisa en utveckling som verkar oacceptabel för dig, eller godkänna en uppdatering enligt dina egna kriterier.



Så vi kan snabbt försöka förstå hur mycket makt du har över reglerna tack vare din nod. Och omfattningen av denna makt beror på typen av regel.



#### För reläregler



När det gäller reglerna för vidarebefordran är det viktigaste helt enkelt att äga en nod, oavsett dess ekonomiska aktivitet. Det som står på spel här är huruvida du går med på att vidarebefordra vissa typer av transaktioner eller inte.



Om du till exempel anser att transaktioner med avgifter på mindre än 1 sat/vB bör accepteras på Bitcoin, kan du justera denna regel på din nod så att den sänder dessa transaktioner, vilket underlättar deras spridning i nätverket tills en Miner så småningom inkluderar dem i ett giltigt block. I grund och botten är det alltså en fråga om makt över spridningen av transaktioner: varje nod har beslutsfattande makt, eftersom att gå med på att vidarebefordra en typ av transaktion är liktydigt med att främja dess acceptans i Bitcoin-nätverket. Om du driver flera noder har du därför större inflytande över vidarebefordringspolicyn, eftersom varje nod har sina egna anslutningar och påverkansområden i nätverket.



Att ha en eller flera noder som är konfigurerade med specifika reläregler innebär att man bestämmer vilken del av nätverket som accepterar att sprida en viss typ av transaktion. Att sprida ett meddelande i en peer-to-peer-graf, som är fallet för Bitcoin-transaktioner, följer logiken i perkolationsteorin. Föreställ dig att varje nod är en plats som kan vara aktiv (`p` = den vidarebefordrar) eller inaktiv (`1-p`). Så snart andelen `p` passerar en kritisk tröskel (`p_c`) uppstår en jättekomponent: transaktionen lyckas korsa nätverket och har alla chanser att nå en Miner. I ett nätverk som Bitcoin, där varje nod har i genomsnitt 8 utgående förbindelser, är tröskeln för `p_c` i allmänhet bara några procent, och ännu lägre om vissa noder har ett mycket stort antal förbindelser.



![Image](assets/fr/061.webp)



Så länge `p` är lägre än `p_c` förblir en transaktion begränsad till isolerade fickor och når inte Miner. Så snart denna tröskel överskrids sprider den sig nästan omedelbart genom hela nätverket.



I slutändan är det alltid miners som beslutar om en transaktion ska ingå i ett block eller inte. Noderna ingriper dock uppströms genom att påverka fördelningen av transaktioner: de avgör om utvinnarna kommer att känna till en viss transaktion eller inte. Om en transaktion inte vidarebefordras till utvinnarna är det naturligtvis omöjligt för dem att inkludera den i ett block.



Att lägga till några fler noder kommer därför bara att ha en marginell inverkan om nätverket redan befinner sig i perkolationsfasen för en viss typ av transaktion, men det kan visa sig vara avgörande när perkolationströskeln närmar sig. Att äga eller påverka flera noder, särskilt om de är väl anslutna, kan öka eller minska värdet på `p` och följaktligen indirekt styra de reläregler som avgör vilka transaktioner som ses och så småningom accepteras av miners.



#### För konsensusregler



När det gäller din nods inflytande på konsensusreglerna är det framför allt dess ekonomiska vikt som kommer att vara avgörande. Detta är ett avgörande koncept: värdet på en valuta är direkt relaterat till dess förmåga att underlätta Exchange. Om ett objekt inte accepteras av någon i Exchange för varor eller tjänster, har det teoretiskt sett ingen monetär nytta. Om till exempel ingen köpman accepterar småsten som betalningsmedel har de ingen användning som pengar. Naturligtvis är nyttan ett subjektivt begrepp på en individuell skala, men i ett givet territorium är det mer sannolikt att ett föremål har en monetär nytta för de människor som bor i detta territorium ju fler handlare som accepterar ett föremål som betalningsmedel i Exchange.



Låt oss ta exemplet med en by där många handlare accepterar guld i Exchange för varor: chansen är stor att guld har en monetär nytta för byborna. Detta tyder på att nyttan av en valuta är direkt beroende av handlarnas beslut att acceptera eller förkasta den.



Detta koncept är avgörande för att förstå den maktdynamik som är i spel i Bitcoin-systemet. Satoshi gör det klart: Bitcoin är ett elektroniskt kontantsystem; med andra ord tillhandahåller det en tjänst som erbjuder en form av valuta, Bitcoin (eller BTC). När protokollreglerna ändras på ett sätt som inte är bakåtkompatibelt (Hard Fork) innebär detta att ett nytt system skapas och därmed en ny valuta. Hur framgångsrik eller misslyckad denna Fork blir beror på storleken på dess ekonomi, som i sin tur bestäms av antalet handlare som accepterar denna nya form av valuta.



![Image](assets/fr/062.webp)



Låt oss ta ett exempel: låt oss anta att Bitcoin drabbas av en Hard Fork. Det skulle då finnas 2 distinkta former av valuta: BTC-1 (den ursprungliga, oförändrade versionen) och BTC-2 (den nya valutan med andra konsensusregler). Om alla handlare som accepterade BTC-1 fortsätter att göra det, men avvisar BTC-2, kommer den senare i teorin att ha mycket begränsad monetär nytta. Som användare skulle jag inte ha något intresse av att behålla och använda BTC-2, eftersom jag vet att ingen handlare skulle vilja ha den i Exchange för varor eller tjänster. Omvänt, om 50% av handlarna väljer att acceptera BTC-2 exklusivt och de återstående 50% endast tar BTC-1, kommer nyttan av BTC-1 i teorin att ha halverats. Jag använder uttrycket "i teorin" eftersom nyttan förblir subjektiv på individnivå och beror på en mängd faktorer (t.ex. territorium och konsumtionsvanor) som är svåra att förstå från fall till fall.



På Bitcoin inkluderar rollen som "handlare", förstås som alla enheter med en viss ekonomisk vikt, naturligtvis företag (fysiska butiker, onlineförsäljningssajter, tjänsteleverantörer etc.), men också Exchange-plattformar, eftersom de accepterar Bitcoin i Exchange för andra valutor, och gruvarbetare, eftersom de accepterar Bitcoin via avgifter i Exchange för tjänsten att inkludera en transaktion i ett block.



När det gäller konsensusregler kan du med din nod styra din ekonomiska aktivitet mot den ena eller andra valutan. Om du till exempel har 10 fulla noder hemma, men ingen betydande ekonomisk aktivitet, kommer ditt inflytande under en Fork att vara nästan noll. Omvänt, en enda nod som används för att hantera en kedja med 200 butiker som accepterar Bitcoin ger betydande ekonomisk vikt.



Det är alltså inte antalet noder som spelar roll, utan vikten av den ekonomiska aktivitet som de stöder. Om din ekonomiska aktivitet är beroende av en nod som du inte kontrollerar kommer dessutom dess ägare att bestämma vilken valuta du använder, så länge du är ansluten till den noden. Det är därför som det är särskilt viktigt att driva och använda sin egen nod i samband med systemstyrning:



> Inte din knut, inte dina regler.


## De olika typerna av Bitcoin-noder


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



En Bitcoin-nod är därför en maskin som kör en implementering av Bitcoin-protokollet. Bakom denna gemensamma definition av noder finns flera möjliga konfigurationer, som inte alla erbjuder samma nivå av autonomi, resursförbrukning och användbarhet för nätverket. I det här kapitlet försöker vi förstå dessa skillnader för att hjälpa dig att välja en nodarkitektur som passar din användning och dina maskinvarubegränsningar.



### Den kompletta knuten



En Full node är helt enkelt en Bitcoin-nod som laddar ner hela Blockchain från Genesis-blocket, validerar varje block oberoende av varandra och lagrar historiken för hela Blockchain lokalt. Detta är den "normala" formen av en Bitcoin-nod, som den föreställdes av Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Full node behöver inte lita på någon eftersom den validerar och känner till all information i systemet. Det är den typ av nod som ger dig flest garantier: du vet, utan att förlita dig på en tredje part, om en betalning är giltig, om ett block är giltigt, om en omorganisation är legitim och så vidare.



I praktiken kräver en Full node icke-triviala resurser, inklusive flera hundra gigabyte för blockfiler, en processor som kan validera skript, RAM-minne för Mempool och cacheminnet samt stabil bandbredd. Den första synkroniseringen (*IBD*) läser och verifierar hela historiken: det är intensivt, men sker bara en gång. En Full node deltar aktivt i nätverket, vidarebefordrar block och transaktioner och kan acceptera inkommande anslutningar för att hjälpa andra peers.



Beroende på dina behov kan du lägga till en indexerare till din Full node. Bitcoin core erbjuder transaktionsindexering som en valfri funktion (avaktiverad som standard), vilket kan vara användbart för specifika ändamål. Den innehåller dock inte en Address-indexerare, vilket ofta är den mest eftertraktade funktionen för enskilda användare. För att åtgärda detta kan du installera dedikerad programvara på din nod, till exempel Electrs eller Fulcrum, för att påskynda Address-balansverifieringsförfrågningar från associerade UTXO:er. Vi kommer att återkomma till indexerarens roll mer i detalj i ett separat kapitel.



### pruned-knuten



pruned-noden validerar allt som en Full node, från Genesis-blocket till huvudet på kedjan med mest arbete, men **behåller bara den senaste delen av blockfilerna**. När de gamla blocken har kontrollerats raderas de gradvis för att hålla sig under en utrymmesgräns som du kan ställa in. Den här konfigurationen är idealisk om du har begränsat diskutrymme: du behåller blockvalideringens oberoende utan att behöva lagra hela Blockchain-historikarkivet. Det här alternativet är särskilt användbart om du helt enkelt vill installera Bitcoin core på din persondator utan att använda en dedikerad maskin.



![Image](assets/fr/064.webp)



De tekniska konsekvenserna av detta alternativ är ganska enkla: pruned-noden är fullt kapabel att sända dina transaktioner, delta i reläet, verifiera block och transaktioner samt spåra kedjan. Å andra sidan kan den inte fungera som en källa till historiska data bortom sina gränser för andra applikationer (t.ex. full explorers, indexers, wallets). Funktioner som kräver arkivet (eller ett globalt index) kommer därför inte att vara tillgängliga.



I praktiken kan du använda en pruned-nod för att ansluta Wallet-hanteringsprogramvara som Sparrow wallet. Du kommer dock inte att kunna skanna transaktioner på din Wallet som föregår beskärningsgränsen. Om du t.ex. har en transaktion registrerad i block 901 458, men din nod endast behåller block från 905 402 och uppåt (eftersom de äldsta har varit pruned), kommer du inte att kunna skanna denna transaktion. Å andra sidan, om du redan hade skannat den när din nod fortfarande hade denna blockhöjd, kommer din Wallet-hanteringsprogramvara att lagra informationen och visa saldot för motsvarande UTXO:er korrekt.



Kort sagt fungerar Wallet-spårning utan problem på en pruned-nod om du skapar en ny Wallet medan din programvara redan är ansluten till den noden. Å andra sidan kan du stöta på svårigheter om du återställer en gammal Wallet, eftersom tidigare transaktioner som inte längre sparas av noden uppenbarligen inte kommer att kunna hämtas.



### Den lätta knuten / SPV



En SPV-nod (*Simplified Payment Verification*), eller lättviktsnod, behåller endast blockheaders, inte transaktionsdetaljer, och förlitar sig på andra fullständiga noder för att få bevis på att en transaktion finns i ett block (Merkle-bevis via träd) för vilket den har headern. Konceptet med förenklad betalningsverifiering är inte nytt, utan har föreslagits av Satoshi Nakamoto själv i del 8 av vitboken.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Ett elektroniskt peer-to-peer-system för kontanter*. https://Bitcoin.org/Bitcoin.pdf



Den här typen av nod är naturligtvis mycket lättare när det gäller lagring och CPU-användning än en Full node- eller till och med en pruned-nod. SPV-noden är därför väl lämpad för mindre enheter och intermittenta anslutningar. Faktum är att den ofta integreras direkt i Wallet, särskilt mobil programvara som Blockstream-appen.



Kompromissen är tillit och sekretess: en SPV-klient kontrollerar inte skript eller valideringspolicyer själv; den antar att kedjan med mest arbete är giltig och är beroende av en eller flera fullständiga noder för svar. Att använda den här typen av nod är därför ett bättre alternativ än att ansluta till en tredjepartsnod, men det är fortfarande mindre fördelaktigt än att ha en Full node- eller till och med en pruned-nod.



![Image](assets/fr/065.webp)



### Vilken nod för vilket behov?





- Mobil / nybörjare



För en nybörjare med bara en Wallet i en mobilapp är en SPV-nod säkert det bästa sättet att komma igång. Installationen går snabbt, kräver få resurser och upplevelsen är enkel och flytande. Detta innebär att du kan verifiera viss information själv och därför förlita dig mindre på tredjepartsnoder samtidigt som du är mer oberoende när det gäller att sända transaktioner.





- PC / medelmåttig användare



En mellananvändare med en PC kan installera en pruned-nod för att dra nytta av nästan alla fördelar med en Full node, utan att överbelasta sin maskin dagligen: fullständig validering, måttlig diskanvändning och enkelt underhåll. Det är en idealisk lösning för att ansluta dina stationära plånböcker och förbli oberoende i distributionen av dina transaktioner, utan att investera i en dedikerad maskin eller överbelasta ditt diskutrymme.





- Suverän Bitcoiner / avancerad



En Full node är fortfarande den bästa lösningen om du vill vara helt oberoende i din användning av Bitcoin och inte begränsa dig själv senare till avancerade användningsområden som en indexerare, en Lightning-nod eller till och med en Block explorer. Det är precis vad vi kommer att utforska i den här kursen!



## Översikt över mjukvarulösningar


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



På mjukvarusidan finns det två huvudsakliga sätt att köra en Bitcoin-nod:




- direkt installera en protokollimplementering, t.ex. Bitcoin core (rekommenderas) eller Bitcoin Knots,
- eller använda en nyckelfärdig distribution (ofta kallad "_node-in-a-box_") som integrerar en Bitcoin-implementering på samma sätt, men som också innehåller ett Interface-administrationssystem, en applikationsbutik och färdiga verktyg (Lightning, webbläsare, indexservrar, till och med självhostande applikationer utanför Bitcoin ...).



Båda metoderna leder till samma mål: att ha en egen nod, men de skiljer sig åt när det gäller installation och användning av Interface, underhåll, utbyggnadsmöjligheter och kostnader. Det är vad vi kommer att utforska i det här kapitlet.



### Implementering av rå Bitcoin-nod



Att installera en rå implementering innebär att du direkt använder programvaran för en Bitcoin-protokollimplementering (t.ex. Core), utan någon ytterligare programvara Layer. Du hanterar själv konfiguration, uppdateringar och tillhörande tjänster (indexering, API, Lightning, säkerhetskopior etc.) enligt dina behov.



Det här är det mest suveräna och flexibla tillvägagångssättet: du vet exakt vad som körs, var data finns och hur allt fungerar. Å andra sidan blir det mer komplext så snart du vill gå utöver den enkla driften av en Bitcoin-nod. Om ditt mål bara är att ha en nod är komplexiteten jämförbar med den för en nod i en låda, eller till och med mindre, eftersom det bara handlar om att installera programvara.



#### Bitcoin core (ultramajoritetskund)



[Bitcoin core är nätverkets ultramajoritetsklient] (https://bitcoincore.org/). Den hämtar, validerar och underhåller Blockchain, tillhandahåller RPC/REST API:er och kan integrera en Wallet. Om du föredrar standardverktyg och känner dig bekväm med att lägga till tjänster själv (t.ex. Electrum-server, explorer och LND) är det bättre att använda Core som det är.



**Fördelar:** Maximal stabilitet, förutsägbart beteende, obearbetad erfarenhet, enkel att installera och konfigurera.



**Nackdelar:** Du måste manuellt bygga resten av stacken för att skapa en komplett applikationsmiljö, snarare än bara en Bitcoin-nod.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (huvudalternativ kund)



[Bitcoin Knots är en Fork av Bitcoin core](https://bitcoinknots.org/), underhålls av Luke Dashjr. Det är den huvudsakliga alternativa klienten till Core för implementering av Bitcoin-protokollet. Den är helt kompatibel med resten av nätverket (den är inte på något sätt en Hard Fork som Bitcoin Cash), men erbjuder ändå ytterligare funktioner, inklusive alternativ för reläpolicy som saknas i Core, eller som tillämpas striktare som standard för att begränsa vad vissa anser vara skräppost.



Det finns två möjliga skäl till att välja Knots framför Core:




- Tekniker**: Olika alternativ från Core, särskilt när det gäller relähantering, genom att bestämma vilka transaktioner som accepteras och sänds av din nod.
- Policy**: En del människor föredrar att använda alternativa klienter som Knots av icke-tekniska skäl, framför allt för att stödja ett alternativ till Core och därmed minska dess monopol. Om Core någonsin skulle äventyras skulle det vara bra att inte bara ha solida, väl underhållna alternativa klienter utan också att veta hur man använder dem på ett effektivt sätt. Andra använder Knots i protestsyfte, eftersom de har tappat förtroendet för Core-utvecklarna eller ogillar majoriteten av klientens ledning.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Personligen rekommenderar jag att du väljer Core, främst för att dra nytta av säkerhetsuppdateringar snabbare. Faktum är att vissa sårbarheter som upptäcks i Knots korrigeras med en fördröjning. Mer generellt är Core's utvecklingsprocess solidt strukturerad och stöds av ett stort antal bidragsgivare, medan Knots underhålls av en enda person och har en mycket mindre gemenskap. Å andra sidan tenderar reläregler att förlora sin användbarhet idag, särskilt när de tillämpas av endast en liten del av nätverket (enligt perkolationsteorin).



### Node-in-a-box-distributioner



Den _node-in-a-box_ kombinerar Bitcoin core (eller Knots) med ett förkonfigurerat operativsystem, en Interface-webb och en App Store med självhosting-tjänster (Lightning, explorers, Electrum-server, Mempool, BTCPay Server, Nextcloud etc.). Med bara ett klick kan du installera, uppdatera och sammankoppla dessa olika moduler.



Det är en mycket enklare lösning för att starta upp och hantera ett stort antal tilläggsapplikationer på daglig basis. Nackdelen är att när ett problem uppstår (t.ex. Docker-image-konflikt, felaktig uppdatering, skadad databas) kan felsökningen bli mycket komplex, eftersom du är beroende av distributionens egen integration. Dessutom är community- eller officiellt stöd ofta komplicerat.



En node-in-a-box är alltså extremt enkel att använda så länge allt fungerar som det ska, men om det uppstår en bugg måste du vara beredd på att göra långa sökningar, vänta på hjälp och smutsa ner händerna.



De flesta av dessa lösningar finns tillgängliga i två format:




- Förmonterad maskin: en komplett dator med redan installerat operativsystem. Dessa "pay-as-you-go"-maskiner behöver bara anslutas till elnätet och till Internet för att vara i drift. Om din budget tillåter det, har detta alternativ fördelen att det är mycket enkelt att installera, ofta erbjuder prioriterad support och bidrar till finansieringen av utvecklingen, eftersom affärsmodellen för dessa företag i allmänhet bygger på försäljning av hårdvara.
- Gör det själv: installera distributionens operativsystem på din egen maskin (gammal dator, NUC, Raspberry Pi, hemserver ...). Detta är den mest ekonomiska lösningen, eftersom du kan återvinna en gammal maskin eller välja maskinvara som exakt matchar dina behov och din budget. Det är också det mest flexibla alternativet och det som är mest tillfredsställande att konfigurera. Det är detta tillvägagångssätt som vi kommer att utforska i den praktiska delen av kursen.



Här är en översikt över de viktigaste node-in-a-box-lösningarna som finns tillgängliga (2025):



### Umbrel (umbrelOS & Umbrel Home)



[Umbrel är idag ledande inom "node-in-a-box"-lösningar (https://umbrel.com/). Framgången beror till stor del på den enkla installationen (när Umbrel lanserades på en enkel Raspberry Pi), den eleganta och intuitiva Interface och ett ekosystem av applikationer som har vuxit snabbt och nu är extremt omfattande.



![Image](assets/fr/067.webp)



Umbrel lanserades 2020 som en enkel Bitcoin-nod tillsammans med ett fåtal underordnade applikationer och har gradvis utvecklats till ett modernt hemmamoln med alla funktioner.



Jag kommer inte att gå in mer i detalj här om hur det fungerar och dess specifika funktioner, eftersom vi kommer att undersöka dessa mer djupgående i det första kapitlet i nästa del. För denna BTC 202-kurs har jag faktiskt valt att använda UmbrelOS, som jag tror är den bästa nuvarande node-in-a-box-lösningen för nybörjare och mellanliggande användare.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 erbjuder StartOS (https://start9.com/), ett system som är utformat för "sovereign computing": målet är att alla ska äga och hantera sin egen privata server, förstärkt av en marknadsplats för applikationer med egen värd. Du kan köpa en Start9-server (Server One för 619 dollar, Server Pure för 899 dollar) eller montera din egen i DIY-läge på din egen maskin.



På Bitcoin-sidan kan du med StartOS installera en Full node, en Lightning-nod, BTCPay Server, Electrs och många andra tjänster. Start9:s dragningskraft sträcker sig dock längre än så: det erbjuder möjligheten att upptäcka, konfigurera och exponera olika programvaror (filmoln, meddelanden, övervakning) på ett enhetligt sätt, med fullständig kontroll. Projektet riktar sig därför till användare som vill ha en robust plattform för självhosting, inte bara en enkel Bitcoin-nod. Det är förmodligen det mest kompletta ekosystemet efter Umbrel.



![Image](assets/fr/068.webp)



Den största skillnaden med Umbrel ligger i Interface. Umbrel förlitar sig på ett mycket polerat UX, medan Start9 erbjuder en råare, mer funktionell Interface. Start9:s applikationsekosystem är mindre rikt än Umbrels, men det kompenserar för detta med flera tekniska fördelar: åtkomst till avancerade applikationsinställningar är förenklad, medan Umbrel snabbt blir restriktivt om det önskade alternativet inte tillhandahålls av Interface. Start9 utmärker sig också när det gäller säkerhetskopieringshantering: förutom Umbrels effektiva lösning för LND finns det ingen enhetlig mekanism, till skillnad från Start9. Dessutom erbjuder den mer lättillgängliga övervakningsverktyg och en krypterad fjärranslutning (`https`), medan lokal åtkomst till Umbrel sker via `http`.



Kort sagt, om du helt enkelt behöver de viktigaste applikationerna för Bitcoin, utan något särskilt intresse för Umbrels mycket rika ekosystem, och Interface-användaren inte är en prioritet, är Start9 ett bättre alternativ. Annars är Umbrel det bättre valet.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode är en distribution som uteslutande fokuserar på Bitcoin och Lightning] (https://mynodebtc.com/) och erbjuder en webb Interface, en marknadsplats för applikationer och uppgraderingar med ett klick. Du kan antingen köpa färdig hårdvara (*Model Two* finns för 549 dollar) eller installera MyNode gratis på din egen maskin. Projektet erbjuder också en *Premium*-version av programvaran (94 dollar), som inkluderar prioriterad support och avancerade funktioner.



![Image](assets/fr/069.webp)



I praktiken samlar MyNode alla de grundläggande byggstenar som behövs för att driva en Full node, samt de applikationer som är viktiga för Bitcoin-användare. Därför är det en lämplig lösning om du inte behöver applikationer utanför Bitcoin-ekosystemet, till exempel självhanterade appar som finns i Start9- och Umbrel-system.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz är ett projekt med 100% öppen källkod](https://docs.raspiblitz.org/) (MIT-licens) för montering av en Bitcoin-nod och en Lightning-nod på en Raspberry Pi. Ladda bara ner avbildningen, starta upp och följ sedan guiden för att få en fungerande nod i en låda på din Raspberry Pi. Förmonterade kit finns också tillgängliga från tredje part, vanligtvis mellan 300 och 400 dollar, beroende på hårdvaran. RaspiBlitz erbjuder också en rad ytterligare applikationer som är enkla att installera.



![Image](assets/fr/070.webp)



Om du äger en Raspberry Pi är det här ett utmärkt alternativ, eftersom mer kompletta system som Umbrel blir allt tyngre för den här typen av mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo är en integritetsfokuserad node-in-a-box] (https://wiki.ronindojo.io/en/home) som automatiserar distributionen av Samurai Dojo och Whirlpool, med en dedikerad Interface och plugins som är särskilt utformade för Samurai-ekosystemet.



Principen är enkel: om du använder Ashigaru Wallet (Fork efterföljaren till Samurai Wallet, efter arresteringen av dess utvecklare) eller om du vill dra nytta av avancerade integritetsverktyg, är RoninDojo något för dig.



![Image](assets/fr/071.webp)



Projektet erbjöd tidigare en förkonfigurerad maskin kallad Tanto, men denna är för närvarande inte tillgänglig. Den kan komma tillbaka vid ett senare tillfälle. Under tiden är det möjligt att enkelt installera RoninDojo på en Rock5B+ eller Rockpro64, eller till och med indirekt på en Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



En annan [node-in-a-box-lösning är Nodl] (https://www.nodl.eu/). Precis som med de tidigare projekten kan du antingen köpa den förkonfigurerade hårdvaran (mellan 599 och 799 euro, beroende på modell) eller installera den själv i DIY-läge.



På mjukvarusidan integrerar Nodl Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL samt BTC RPC Explorer, alla med en integrerad uppdateringskedja och öppen källkod under MIT-licensen.



![Image](assets/fr/072.webp)



Efter att ha utforskat de olika mjukvarulösningarna är det nu dags att välja den maskin som ska vara värd för din nod!




## Översikt över hårdvarulösningar


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nu när vi har utforskat alla möjligheter med programvaran ska vi fokusera på den maskinvara som krävs för din nod. Jag ska ge dig några konkreta råd om hur du väljer dina komponenter, tillsammans med konfigurationer som är skräddarsydda för att passa olika budgetar. Naturligtvis är detta min personliga åsikt och feedback: det finns säkert andra relevanta alternativ utöver de som presenteras här. Dessutom kommer jag inte att gå in på de färdigmonterade maskiner som erbjuds av node-in-a-box-projekt, som vi redan har behandlat i föregående kapitel. Här kommer vi uteslutande att fokusera på DIY-lösningar.



### Behöver du verkligen en dedikerad maskin?



Under de senaste åren har bitcoiners blivit alltmer medvetna om en vanlig missuppfattning, särskilt med populariseringen av node-in-a-box i början av 2020-talet: en Bitcoin-nod bör nödvändigtvis köras på en maskin som uteslutande är avsedd för detta ändamål. Men detta är inte sant. Du behöver inte nödvändigtvis en dedikerad dator för att köra en Bitcoin-nod: Bitcoin core kan mycket väl köras på din vanliga PC. Om du har tillräckligt med diskutrymme för Blockchain eller aktiverar beskärning kan du validera kedjan, ansluta din Wallet och till och med stänga programmet när du är klar med att använda det. Fördelen med detta tillvägagångssätt är betydande: noll initial investering och minimal komplexitet.



![Image](assets/fr/074.webp)



Med det sagt är det ofta bekvämare att använda en dedikerad maskin. Den kan köras kontinuerligt (24/7), vara fjärråtkomlig hela tiden, inte monopolisera resurserna på din huvudmaskin och, framför allt, isolera användningar (en bra säkerhetspraxis: om din personliga dator stöter på problem fortsätter din nod att fungera och vice versa). Så frågan är inte "Behöver jag dedikera en maskin?", utan snarare "Behöver jag en nod som ständigt är online, tillgänglig för andra enheter och som kan utvecklas?" (Lightning, indexerare, ytterligare applikationer ...). Om svaret är ja kommer det att bli mycket enklare att välja en separat maskin.



### 3 anskaffningsmetoder: återvinning, begagnat och nytt



#### Återvinning av en gammal PC



Det är den mest ekonomiska lösningen. De flesta av oss har en gammal PC som samlar Dust hemma, eller hos vänner och familj: det här är det perfekta tillfället att ta den i bruk igen! För att anpassa den för användning som en Bitcoin-nod behöver du bara lägga till en 2TB SSD och, beroende på dina behov, byta ut eller lägga till RAM-stänger för att öka RAM-minnet. Räkna med att betala mellan 100 och 200 euro för en fullt fungerande maskin.



Innan du köper hårdvara bör du kontrollera antalet tillgängliga diskplatser, typ av anslutning (M.2 eller SATA), RAM-format (SODIMM eller DIMM) och generation (DDR4, etc.). Du bör också ta tillfället i akt att rengöra maskinen, särskilt fläkten, för att säkerställa optimal prestanda.



Var dock försiktig om du använder en bärbar dator: batteriet kan bli ett problem med tiden (mer om detta längre fram i kapitlet).



#### Rekonditionerad eller begagnad



Marknaden är full av renoverade mini-PC-datorer för företag, t.ex. * Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* eller *Dell OptiPlex Micro*. Dessa maskiner är solida, kompakta, tysta och energieffektiva. Priset ligger långt under nypris och det är lätt att hitta modeller utrustade med 6:e till 10:e generationens i5/i7-processorer och 8 till 16 GB RAM, allt till mycket attraktiva priser, i allmänhet mellan 70 och 200 euro, beroende på konfiguration. Enligt min mening är detta sannolikt det bästa alternativet om du söker en dedikerad maskin för din Bitcoin-nod.



![Image](assets/fr/075.webp)



Det går också att hitta begagnade PC och bärbara datorer som är några år gamla, med intressanta konfigurationer och utmärkt valuta för pengarna.



**Note:** Maskiner från företagsflottor, t.ex. *ThinkCentre Tiny*, är ofta endast utrustade med en *DisplayPort* (DP)-port för skärmen, utan HDMI-utgång. Glöm därför inte att ta med en adapter eller en DP-till-HDMI-kabel om du behöver en sådan.



#### Köpa nytt



Om din budget tillåter det kan du också välja en ny maskin. Detta är ett bra alternativ om du vill ha ny hårdvara med bra prestanda, särskilt om du planerar att använda Umbrel eller Start9 med ytterligare applikationer utanför Bitcoin-ekosystemet för självhosting.



### Vilken typ av maskin ska jag välja?



#### Mini-PC "NUC" / barebone



Mini-PC:er är enligt min mening den bästa kompromissen för att ha en Bitcoin-nod hemma. De är platsbesparande, får lätt plats på en hylla, förbrukar minimalt med ström och lämpar sig för enkla hårdvarumodifieringar, som att lägga till RAM eller byta ut SSD-enheten.



Personligen föredrar jag * Lenovo ThinkCentre Tiny*, som är mycket utbredd på begagnatmarknaden (från företagsflottor); de är särskilt robusta och lätta att modifiera. Det finns naturligtvis många motsvarigheter från andra tillverkare: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Höjdpunkter:** litet fotavtryck, måttlig strömförbrukning, låg ljudnivå, skalbarhet (beroende på modell) och tillförlitlighet.



**Svagheter:** något dyrare än en SBC av typen Raspberry Pi, ingen inbyggd skärm (fjärråtkomst eller via extern bildskärm), inget batteri (plötslig avstängning vid strömavbrott).



#### Dedikerad bärbar dator



Det är ett utmärkt lågkostnadsalternativ till mini-PC: idag kan du hitta begagnade eller till och med nya bärbara datorer till låga priser, utrustade med anständiga processorer, många portar samt en integrerad skärm och tangentbord (mycket praktiskt för första installationen). Framför allt fungerar batteriet som en naturlig UPS: i händelse av strömavbrott stängs inte noden av plötsligt utan kan till och med vara i drift i flera timmar.



![Image](assets/fr/076.webp)



**Höjdpunkter:** Allt-i-ett-lösning, batteriet fungerar som en UPS (inga strömavbrott), förenklad installation tack vare en integrerad skärm och tangentbord, ett integrerat Wi-Fi-kort och ett brett urval av begagnade och nya marknader (vilket ofta innebär att du kan förhandla om priser).



**Svagheter:** något högre strömförbrukning än en ren Mini-PC, gradvis batterislitage vid 24/7-drift med kapacitetsförlust, sällsynt men verklig risk för batterisvullnad eller termisk skenande med åldern. Det är främst denna aspekt som gör att jag anser att mini-PC:n är ett bättre alternativ än den bärbara datorn: den gradvisa försämringen av batteriet och de därmed förknippade riskerna.



Om du väljer den här lösningen rekommenderar jag att du håller ett vakande öga på batteriets skick för att undvika fara. Håll utkik efter överdriven värme, ovanliga lukter, instabilitet eller ett deformerat skal. Om du får ett larm ska du omedelbart stänga av datorn och dra ur kontakten, och sedan lämna in batteriet till en specialiserad återvinningsanläggning.



**Tips: ** Om BIOS/UEFI eller tillverkarens verktyg tillåter det kan du ställa in en belastningsgräns (t.ex. 60 % eller 80 %) för att förlänga batteriets livslängd.



#### Raspberry Pi och andra SBC-enheter: fel idé



I början av 2020-talet, med ökningen av mjukvaran "node-in-a-box", uppstod Raspberry Pi-trenden som ett sätt att köra en Bitcoin-nod. Idén verkade attraktiv: billig, kompakt och tillgänglig.



![Image](assets/fr/073.webp)



I praktiken kan en Raspberry Pi vara tillräcklig om ditt mål endast är att köra en Bitcoin-nod utan ytterligare applikationer. Men så snart du vill använda Umbrel, Start9 eller ett rikare ekosystem (Block explorer, Address indexer, Lightning-nod, självhostande appar ...) når maskinen snabbt sina gränser.



Raspberry Pi har ett antal nackdelar:




- processorer som är för tunna, med en ARM-arkitektur som ibland är inkompatibel med viss programvara eller kräver mer hantering;
- Lödda RAM-minnen, omöjliga att uppgradera, med begränsade konfigurationer (ofta max 8 GB);
- externa lådor för SSD-enheter som är anslutna med kabel, ofta källor till buggar, vilket kräver köp av ett specifikt kort för en stabil SSD;
- tendens att värmas upp snabbt och svårigheter att säkerställa korrekt kylning;
- behöver köpa ytterligare hårdvara (hölje, fläkt, SSD-kort etc.);
- mycket begränsade anslutningsmöjligheter.



Historiskt sett var den stora fördelen med SBC:er som Raspberry Pi deras pris: för några dussin euro kunde du få en dedikerad maskin. Men idag har priserna stigit kraftigt, och när du har lagt till all nödvändig extra hårdvara närmar sig kostnaden den för de första begagnade eller renoverade x86-minidatorerna, som enligt min mening erbjuder mycket fler fördelar. Av denna anledning rekommenderar jag inte att du väljer en SBC.



### Val av komponenter



#### Disklagring: SSD obligatoriskt, minst 2 TB



Tekniskt sett är det möjligt att köra en Bitcoin-nod på en hårddisk. Problemet är att allt kommer att sakta ner avsevärt, särskilt IBD, som kommer att bli extremt lång på grund av Bitcoin core:s intensiva användning av disken som cache (särskilt för UTXO-uppsättningen). Det är därför jag starkt avråder från att använda en hårddisk: den skapar en verklig flaskhals, begränsar kraftigt framtida utveckling (t.ex. för en Lightning-nod) och kan till och med leda till en synkroniseringsmissmatchning med Blockchain-huvudet. Dessutom ökar den konstanta påfrestningen på den mekaniska disken risken för förtida slitage.



SSD-enheter förändrar din användarupplevelse radikalt: allt blir snabbare och smidigare, med mycket högre tillförlitlighet. Användningen av en SSD är därför (nästan) obligatorisk för din nod, och du kommer inte att ångra det, särskilt eftersom modeller med hög kapacitet nu är relativt prisvärda.



![Image](assets/fr/077.webp)



När det gäller kapacitet håller 2 TB gradvis på att etablera sig som det nya rimliga minimumet. Sommaren 2025 närmar sig Blockchain redan 700 GB, och om du lägger till Umbrel, en Address-indexerare och några få applikationer kommer en 1 TB SSD snabbt att bli mättad. Med 2 TB har du en bekväm marginal för de kommande åren (i en bred uppskattning, mellan 5 och 15 år). Du kan också välja 4 TB om du planerar att använda många applikationer på Umbrel, lagra stora filer i self-hosting eller om du vill förutse dina diskutrymmesbehov i stor utsträckning.



![Image](assets/fr/078.webp)



När det gäller formatet beror detta på de portar som finns tillgängliga på din maskin, men om möjligt rekommenderar jag att du använder en NVMe M.2 SSD.



#### Minne (RAM): 8 till 16 GB



För enbart Bitcoin core (utan Umbrel-overlay) rekommenderar utvecklaren ett minimum av 256 MB RAM med inställningarna justerade till den lägsta inställningen, 512 MB med standardinställningar och 1 GB för normal användning.



Om du å andra sidan använder ett node-in-a-box-system som Umbrel eller Start9 är RAM-kraven betydligt högre. Umbrel-utvecklarna rekommenderar minst 4 GB RAM. Det kan räcka för att köra Core only, men du kommer snart att vara begränsad. De rekommenderar därför 8 GB, vilket jag också anser vara minimum för en grundläggande konfiguration runt Bitcoin (Core, LND, indexerare och några applikationer). Enligt min erfarenhet, med Umbrel och några ytterligare tjänster, är 8 GB fortfarande lite snävt. För att vara riktigt bekväm och ha lite marginal skulle jag rekommendera 16 GB RAM.



#### Processor (CPU)



För en Umbrel-nod är minimikravet en dubbelkärnig 64-bitars processor från Intel eller AMD. Om du vill använda några applikationer utöver Bitcoin core kommer en fyrkärnig (eller högre) att göra en verklig skillnad när det gäller flyt. Till exempel är 6:e till 10:e generationens i5/i7-processorer utmärkta alternativ på begagnatmarknaden.



### Exempel på konkreta konfigurationer



Nedan föreslår jag tre konkreta konfigurationer, anpassade till olika budgetar och behov, med exakta modeller som stöd. Dessa val ges som exempel för att illustrera informationen i det här kapitlet; du är inte skyldig att välja exakt dessa modeller. Eftersom jag anser att Mini-PC är det bästa alternativet på lång sikt kommer jag att använda mig av detta format för de tre föreslagna konfigurationerna.



*Priserna nedan är endast vägledande och kan variera beroende på region, leverantör och period*



Först och främst behöver du en SSD som är tillräckligt stor för att rymma Blockchain, samtidigt som den lämnar utrymme för manövrering. SSD-enheter har en begränsad livslängd när det gäller skrivcykler och den totala volymen data som skrivs. En Bitcoin-nod lägger dock en betydande belastning på disken när den skriver. Det är därför jag inte rekommenderar instegsmodellerna; istället föreslår jag en NVMe SSD, som erbjuder betydligt bättre prestanda.



Som ett exempel har jag för denna kurs valt följande modell: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, tillgänglig för cirka 120 € på Amazon. Du kan också välja andra välkända märken som Crucial, Western Digital eller Kingston.



![Image](assets/fr/046.webp)



#### Lågbudgetkonfiguration



Om din budget är mycket begränsad (under 200 euro) skulle jag naturligtvis råda dig att inte investera i en dedikerad maskin, utan att installera Bitcoin core direkt på din vanliga dator (i pruned-läge om du har ont om diskutrymme).



Annars rekommenderar jag *HP EliteDesk 800 G2 Mini* för en budget på ingångsnivå. Jag hittade en renoverad modell för € 96 på Amazon, utrustad med en 6: e generationens Intel Core i5-processor och 8 GB RAM. Detta är ett särskilt intressant alternativ för nybörjare: denna processor och denna mängd minne är mer än tillräckligt för att köra Core on Umbrel, liksom flera applikationer samtidigt, till exempel en Electrs-indexerare, en Lightning-nod och en Mempool-instans, förutsatt att du inte tilldelar för mycket cache till Core. Dessutom gör den här typen av mini-PC det enkelt att öka RAM-minnet till exempelvis 16 GB om behovet skulle uppstå (räkna med att betala cirka 30-40 euro extra för ett eller två minneskort av hög kvalitet).



![Image](assets/fr/045.webp)



Sedan är det bara att lägga till SSD-enheten i budgeten. Om vi börjar med Samsung 2TB för 120 euro får vi en totalkostnad på 216 euro för en komplett, funktionell maskin.



#### Konfiguration med medelhög budget



Om du har en genomsnittlig budget på cirka 300 euro för den maskin som ska vara värd för din nod rekommenderar jag till exempel en *Lenovo ThinkCentre Tiny*, utrustad med en högpresterande processor och tillräckligt med RAM-minne. Jag hittade en renoverad modell på Amazon för 180 €, med en 6:e generationens Intel Core i7-processor och 16 GB RAM. Med tillägget av 2TB SSD för 120 € blir den totala kostnaden 300 €.



![Image](assets/fr/044.webp)



Med den här maskinen har du en bekväm konfiguration: en snabb IBD och möjlighet att köra många applikationer på din Umbrel eller Start9 utan problem. Det är just den här konfigurationen jag använder för den här BTC 202-kursen.



#### Avancerad konfiguration



Med en större budget blir möjligheterna betydligt bredare. Du kan välja en DIY-konfiguration eller till och med välja en förmonterad maskin som erbjuds direkt av ett node-in-a-box-projekt.



Till exempel finns *ASUS NUC 14 Pro* tillgänglig ny från Amazon för 540 €. För detta pris får du en Intel Core Ultra 5-processor (ny och särskilt högpresterande), tillsammans med 16 GB DDR5 RAM. Med en sådan konfiguration kommer du att kunna slutföra en IBD på rekordtid och installera krävande applikationer utan problem.



Det här är en extremt bekväm konfiguration, till och med overkill om det ursprungliga målet helt enkelt är att köra en Bitcoin-nod. Om du å andra sidan vill dra full nytta av alla de självhostande applikationer som finns tillgängliga på Umbrel och Start9, är den här effektnivån helt rätt för dig.



![Image](assets/fr/043.webp)



Beroende på vad du vill använda den till kan du välja antingen en 2 TB SSD, som i de andra konfigurationerna, eller direkt en 4 TB SSD för 260 euro om du även vill lagra personliga filer och utöka din användning av self-hosting. Med en 2TB SSD är den totala kostnaden för konfigurationen €660, medan den med en 4TB SSD når €800.



### Några fler tips





- Om du vill köpa begagnad utrustning och betala med bitcoins, kom till en träff nära dig! Genom att chatta med andra deltagare kommer du säkert att hitta lämplig utrustning till ett bra pris, samtidigt som du hjälper till att hålla den cirkulära ekonomin runt Bitcoin vid liv. Det är också en möjlighet att dra nytta av goda råd från samhället.





- För internetanslutningen behöver du naturligtvis en RJ45 Ethernet-kabel, åtminstone för systeminstallationen.





- I vissa miljöer, t.ex. Umbrel, kan du använda Wi-Fi, men prestandan blir i allmänhet sämre (särskilt om du vill använda din Lightning-nod på distans, eftersom detta kan ha en inverkan). Om du väljer Wi-Fi ska du se till att din maskin har ett inbyggt kort eller lägga till en kompatibel dongel.





- Använd alltid originaltillverkarens strömförsörjning Supply för din maskin. Detta är avgörande för att förhindra skador på utrustningen och för att förebygga risken för att starta en brand.





- Om din maskin inte har ett inbyggt batteri är det en god idé att investera i en växelriktare för att undvika plötsliga avstängningar.





- Beroende på utrustningens värde och det geografiska läget kan det också vara lämpligt att installera ett åskskyddssystem, antingen direkt i elcentralen eller i det grenuttag som används.





- Slutligen, kom ihåg att optimera kylningen av din maskin: rengör den regelbundet och installera den på en sval, välventilerad och ostörd plats för att undvika överhettning, vilket kan leda till throttling (frivillig begränsning av processorns hastighet).



# Enkel installation av en Bitcoin-nod


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: mycket mer än en Bitcoin-nod


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel är ett personligt serveroperativsystem som är utformat för att göra självhosting tillgängligt: du installerar Umbrel, öppnar en webbläsare på `umbrel.local` och hanterar allt via en enkel fjärrkontroll Interface.



Projektet populariserade först idén om en Bitcoin och Lightning-nod med ett klick, och expanderade sedan till ett veritabelt "hemmamoln": fil- och fotolagring, multimediastreaming, nätverksverktyg, hemautomation, lokal AI och hundratals appar som kan installeras från en integrerad App Store.



I Umbrel körs varje applikation i en Docker-container (isolering, atomära uppdateringar, oberoende start/stopp). Interface centraliserar åtkomsten till alla dessa appar och erbjuder single sign-on (med 2FA som tillval), uppdateringar med ett klick för OS och appar, liveövervakning av maskinen (CPU, RAM, temperatur, lagring), behörighetshantering mellan appar och en översikt över deras förbrukning.



Umbrels mål är därför att ge dig tillbaka kontrollen och sekretessen över dina data, utan att förlita dig på molntjänster, utöver att bara driva en Bitcoin-nod.



### Umbrel Home vs umbrelOS



Umbrel erbjuder två olika tillvägagångssätt:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): detta är en färdig miniserver, speciellt utformad och optimerad för umbrelOS. Den är kompakt, tyst, Ethernet-ansluten och utrustad med en NVMe SSD (upp till 4 TB som tillval), 16 GB RAM och en fyrkärnig CPU. Du beställer den, kopplar in den och går till `umbrel.local`. Du kan ha en operativ Umbrel igång på några minuter. Det är plug-and-play-alternativet.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): detta är operativsystemet som du kan installera själv på din egen hårdvara (mini-PC, NUC, torn, dedikerad bärbar dator...). Du har samma Interface och samma App Store som på Umbrel Home.



![Image](assets/fr/080.webp)



I båda fallen är användarupplevelsen identisk på mjukvarusidan: webbläsarbaserad administration, uppdateringar med ett klick, installation av applikationer på begäran ... DIY-lösningen är ofta mer ekonomisk än att köpa en Umbrel Home (beroende på vilken maskin som används). Jag skulle dock inte nödvändigtvis rekommendera att du alltid väljer DIY-alternativet, eftersom **köp av en Umbrel Home bidrar direkt till att finansiera projektets utveckling**, eftersom dess affärsmodell bygger på försäljning av hårdvara. Och ärligt talat, med 389 euro för 2 TB lagring, är priset fortfarande mycket rimligt med tanke på kvaliteten på den maskin som erbjuds.



![Image](assets/fr/079.webp)



I nästa kapitel kommer vi att utforska hur du installerar umbrelOS DIY på din egen maskin. Du kan dock följa denna BTC 202-kurs på samma sätt om du har valt ett Umbrel Home.



### Användningsfall: från Bitcoin-noden till hemmamolnet



Umbrel kan förbli mycket minimalistisk och fokuserad enbart på Bitcoin, eller utvecklas till en sann multifunktionell personlig server, beroende på dina behov. Här är de viktigaste användningsområdena för Umbrel:





- Enkel Bitcoin-nod**: detta är den grundläggande användningen som Umbrel har förlitat sig på från början. Du kan köra Bitcoin core (eller Knots), ansluta dina plånböcker direkt till din nod, exponera en Electrum-server, vara värd för din Mempool Block explorer för att visa Blockchain och uppskatta avgifter... Det är dessa användningsområden som vi kommer att fokusera på i den här kursen.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel låter dig också distribuera LND eller Core Lightning, två implementeringar av Lightning Network, för att hantera din egen Lightning-nod. Du kommer att kunna öppna kanaler, hantera din likviditet, göra betalningar, automatisera balansering, erbjuda tjänster, ansluta en fjärransluten Wallet eller dra nytta av avancerad Interface-hantering tack vare de många tillgängliga applikationerna. Vi kommer att titta på detta specifika användningsfall i vår nästa LNP 202-kurs.



![Image](assets/fr/083.webp)





- Allmän självhosting**: med Nextcloud, Immich, Jellyfin/Plex, DNS-breda annonsblockerare (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), hemautomation (Home Assistant), säkerhetskopiering, anteckningshantering, kontorsverktyg, lokal AI (Ollama + Open WebUI) ... Umbrel kan bli din personliga server, så att du kan återfå kontrollen över dina data. Du är själv värd för de tjänster du använder varje dag, med en polerad användarupplevelse som liknar externa lösningar, samtidigt som du behåller total kontroll över dina data och din integritet.



Genom att distribuera applikationer i containrar kan du forma Umbrel som du vill: börja med en enkel Bitcoin-nod och några appar kopplade till dess ekosystem, installera sedan en Lightning-nod vid sidan av din Bitcoin-nod och gradvis berika din instans med de självhostande applikationer du behöver.



### Gemenskap och ömsesidigt bistånd



En av Umbrels viktigaste fördelar jämfört med sina konkurrenter är dess stora och mycket aktiva användargemenskap. Du kan nå dem främst via [deras Discord] (https://discord.gg/efNtFzqtdx) och [deras onlineforum] (https://community.umbrel.com/). Här hittar du inte bara praktiska råd utan framför allt lösningar för att lösa problem eller fixa buggar. Det är ett bra ställe att börja, att utvecklas och så småningom hjälpa andra användare, så att du inte blir ensam med din Coin.



![Image](assets/fr/084.webp)



### UmbrelOS-licens



Umbrels kod är offentligt tillgänglig (du kan se, Fork och ändra den), men den är inte under en riktig öppen källkodslicens. Faktum är att umbrelOS distribueras under [*PolyForm Noncommercial 1.0*]-licensen (https://polyformproject.org/licenses/noncommercial/1.0.0/), även om vissa tillhörande utvecklingsverktyg är tillgängliga under MIT-licensen.



I praktiken kan du göra i stort sett vad du vill med umbrelOS, så länge det är för personligt, icke-kommersiellt bruk: modifiering, vidaredistribution för icke-vinstdrivande ändamål, skapande av derivat för dig själv eller för icke-vinstdrivande organisationer, förutsatt att du respekterar de juridiska meddelandena.



Det är dock förbjudet att sälja Umbrel eller dess derivat (t.ex. en förmonterad maskin med umbrelOS förinstallerat), att erbjuda Umbrel-relaterade tjänster kommersiellt eller att integrera dess kod i en produkt för vinst.



Tekniskt sett begränsar denna licens inte installationen, granskningen eller anpassningen av Umbrel för personligt bruk. Juridiskt sett skyddar den projektet mot obehörig återförsäljning eller kommersiell hosting, särskilt av molnleverantörer. Umbrel är därför inte öppen källkod, även om dess kod förblir allmänt tillgänglig.



Varje applikation i Store har dock sin egen licens, ofta öppen källkod.




## Installera en Full node med Umbrel


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nu när vi har all nödvändig information är det dags att fördjupa sig i detaljerna. I den här handledningen visar vi dig hur du installerar en komplett Bitcoin-nod med UmbrelOS.



### Material som krävs



Här kommer vi att använda UmbrelOS x86-bilden (mer exakt, x86_64-versionen). Du kommer att kunna följa den här guiden på vilken maskin du än väljer, så länge den inte är utrustad med en ARM-arkitekturprocessor (ingen Apple Silicon, Raspberry Pi, etc.). Detta innebär att vilken dator som helst med en Intel eller AMD 64-bitars processor räcker, så länge den uppfyller minimikraven, beroende på hur du tänker använda din Umbrel (minst en dubbelkärnig processor rekommenderas).



Om du har valt en Raspberry Pi 5 (ett alternativ som jag inte rekommenderar, som nämnts i föregående avsnitt), är installationen något annorlunda. Du kan sedan följa denna dedikerade handledning och återvända till min kurs en gång på Interface-webben `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Som nämndes i föregående avsnitt valde jag att köra den här handledningen på en liten renoverad dator som jag hittade till ett bra pris: en *Lenovo ThinkCentre M900 Tiny* utrustad med en Intel Core i7-processor och 16 GB RAM. Det här är en mycket bekväm konfiguration för att köra Umbrel, särskilt för en Bitcoin-nod. Jag valde dock den här konfigurationen eftersom jag vill installera en Lightning-nod och andra mer krävande applikationer senare. Jag har också lagt till en 2 TB SSD i min ThinkCentre för att behålla hela Blockchain och ändå ha en bekväm marginal. Med den här konfigurationen är den totala kostnaden 270 euro, inklusive alla utgifter.



![Image](assets/fr/001.webp)



Jag är särskilt förtjust i Lenovos ThinkCentre Tiny-serie, eftersom det är kompakta, tysta och mycket robusta maskiner. Dessa datorer är mycket populära bland företag och finns därför i överflöd på begagnatmarknaden, där du kan hitta intressanta konfigurationer mellan 70 och 200 euro.



Om du, som jag, har valt en dator utan bildskärm, **behöver du bara ansluta bildskärm och tangentbord** under installationen. Därefter kommer du att kunna komma åt den på distans från en annan dator i samma nätverk (eller via andra metoder som vi går igenom i senare kapitel). Du behöver också en RJ45 Ethernet-kabel för att ansluta din maskin till det lokala nätverket och ett USB-minne på minst 4 GB för att lagra installationsavbildningen.



Här följer en sammanfattning av utrustningskraven:




- Dator med x86_64-processor (minst Dual-core, rekommenderas Quad-core);
- RAM-minne (minst 4 GB, 8 GB rekommenderas eller mer för utökad användning);
- SSD (rekommenderas + 2 TB);
- USB-minne (+ 4 GB) för installation av UmbrelOS-bilder;
- Bildskärm och tangentbord (endast användbart vid första installationen om datorn inte är utrustad med ett sådant);
- RJ45 Ethernet-kabel.



### Steg 1 - Montera datorn



Beroende på vilken maskinvara du har valt är det första steget att montera de olika komponenterna i din dator. I mitt fall hade till exempel den ursprungliga SSD-enheten en kapacitet på endast 256 GB, så jag kommer att återvinna den för annan användning och ersätta den med en 2 TB SSD. Om du också vill byta ut RAM-modulerna är det dags att göra det nu.



### Steg 2: Förbered en startbar USB-nyckel



Innan du installerar UmbrelOS på din maskin måste du skapa ett startbart USB-minne som innehåller operativsystemet. Alla steg i steg 2 måste utföras på din personliga dator (och inte direkt på den dator som ska bli din nod).





- Börja med att ladda ner den senaste versionen av UmbrelOS i USB-format:



Gå till [den officiella Umbrel-webbplatsen för att ladda ner ISO-bilden](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) för installation via USB-nyckel. Se till att du väljer den version som är kompatibel med x86_64-arkitekturen (fil med namnet `umbrelos-amd64-usb-installer.iso`). Nedladdningen kan ta lite tid eftersom avbildningen är ganska stor.



![Image](assets/fr/002.webp)





- Installera Balena Etcher:



För att skapa det startbara USB-minnet använder du ett enkelt plattformsoberoende verktyg som heter [Balena Etcher] (https://www.balena.io/etcher/). Ladda ner och installera det på din dator.



![Image](assets/fr/003.webp)





- Sätt i ett tomt USB-minne på minst 4 GB:



Anslut en USB-nyckel till din dator (den som du just har laddat ner UmbrelOS och Balena Etcher-bilden till). **Varning: all data på nyckeln kommer att raderas**. Se till att den inte innehåller några viktiga filer.





- Bränn ISO-imagen till USB-minnet med Balena Etcher:



Starta Balena Etcher och välj ISO-filen `umbrelos-amd64-usb-installer.iso` som du just har laddat ner genom att klicka på knappen "*Flash from file*". Välj sedan USB-nyckeln som målenhet och klicka på "*Flash!*" för att börja skriva.



![Image](assets/fr/004.webp)



När operationen är klar har du en startbar USB-nyckel som innehåller UmbrelOS, redo att starta och installera Umbrel på din maskin.



![Image](assets/fr/005.webp)



### Steg 3: Starta datorn från USB-nyckeln



Nu när ditt startbara USB-minne som innehåller UmbrelOS är klart kan du starta din dator på det för att starta systeminstallationen. Koppla ur USB-minnet från din huvuddator och sätt in det i den enhet där du vill installera Umbrel och din Bitcoin-nod.



Som vi förklarade i början av det här kapitlet behöver du en bildskärm och en inmatningsenhet för att slutföra installationen. Anslut en bildskärm via HDMI (eller annan port, beroende på din dator) och anslut ett tangentbord via USB till din maskin. Dessa enheter krävs endast för installationen; du kommer inte att behöva dem efteråt, eftersom Umbrel kommer att nås på distans från en annan dator. Anslut dessa två enheter till din dator.



**Tips:** Om du inte har en extern skärm hemma kan du använda din TV. Med sin HDMI-ingång (eller annan ingång) kan den användas som en tillfällig skärm medan du installerar operativsystemet.



Umbrel kräver självklart en internetanslutning. Anslut RJ45 Ethernet-kabeln mellan din enhet och din router.



![Image](assets/fr/006.webp)



Slå på din maskin. I de flesta fall bör den automatiskt upptäcka USB-nyckeln och starta från den. Du kommer då att se installationsskärmen för UmbrelOS Interface visas.



Om enheten startar i ett annat system eller visar ett felmeddelande betyder det förmodligen att den inte startar automatiskt från USB-nyckeln. I så fall måste du starta om och gå in i BIOS/UEFI-inställningarna (vanligtvis genom att trycka på `DEL`, `F2`, `F12` eller `ESC`, beroende på datortillverkare). Ändra sedan startordningen så att USB-nyckeln prioriteras. Starta sedan om enheten för att starta UmbrelOS.



### Steg 4: Installera UmbrelOS på din dator



När enheten har startat från USB-minnet kommer du att mötas av Interface UmbrelOS-installationen. Detta steg innebär att systemet installeras direkt på maskinens interna Hard-disk.



På skärmen som visas visas en lista över alla interna lagringsenheter som datorn har identifierat. Varje disk åtföljs av ett nummer, ett namn och en lagringskapacitet. Leta reda på den disk som du vill installera Umbrel på. **Varning: alla filer på den här disken kommer att raderas permanent.**



![Image](assets/fr/007.webp)



När du har hittat rätt diskett (vanligtvis den med störst kapacitet, för Blockchain), noterar du numret som tilldelats den. Om den disk som du har valt till exempel har numret "2", skriver du in "2" och trycker sedan på tangenten "Enter" på tangentbordet.



![Image](assets/fr/008.webp)



Programmet kommer att formatera den valda disken, installera UmbrelOS och automatiskt konfigurera systemet. Detta kan ta några minuter. Låt processen löpa utan avbrott.



![Image](assets/fr/009.webp)



När installationen är klar kommer du att uppmanas att stänga av enheten. Tryck på valfri tangent för att stänga av datorn.



![Image](assets/fr/010.webp)



Du kan nu ta bort USB-nyckeln, tangentbordet och skärmen, som inte längre behövs för din Umbrel. Allt som återstår av din nod är strömförsörjningen Supply och RJ45 Ethernet-kabeln.



![Image](assets/fr/011.webp)



Innan du startar om enheten ska du kontrollera följande två punkter:





- USB-nyckeln är urkopplad**: om den förblir ansluten kan systemet starta om på den istället för på den interna disken;
- Ethernet-kabeln är inkopplad**: enheten måste vara ansluten till routern för att fungera.



Tryck på strömbrytaren. Systemet startar automatiskt från den interna hårddisk där UmbrelOS installerades. Den första uppstarten kan ta ungefär **5 minuter**. Under denna tid initialiserar Umbrel sina tjänster och Interface.



Från en annan dator (din vanliga PC) som är ansluten till **samma lokala nätverk**, öppna en webbläsare (Firefox, Chrome...) och gå till:



```
http://umbrel.local
```



Denna Address används för att fjärråtkomst till Umbrel Interface grafiska användargränssnitt Interface och påbörja konfigurationen.



Om Address `http://umbrel.local` inte fungerar i din webbläsare efter att ha väntat i minst 5 minuter, försök helt enkelt:



```
http://umbrel
```



Om detta fortfarande inte fungerar, ange din Umbrels lokala IP Address direkt i webbläsaren. Till exempel (ersätt `42` med numret på din maskin som är värd för Umbrel i det lokala nätverket):



```
http://192.168.1.42
```



För att identifiera din Umbrells IP Address finns det flera metoder, från de enklaste till de mest avancerade:





- Gå in i routerns administration Interface och hitta IP Address för Umbrel-enheten i det lokala nätverket.





- Använd programvara för nätverksskanning, t.ex. Angry IP Scanner, för att upptäcka anslutna enheter och lokalisera Umbrells IP Address.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Som en sista utväg kan du återansluta en bildskärm och ett tangentbord till enheten, logga in (standardinloggning: `umbrel`, lösenord: `umbrel`) och sedan skriva följande kommando:



```
hostname -I
```



Nu är du redo att använda Umbrel!



### Steg 5: Att komma igång med Umbrel



För att börja konfigurera din Umbrel, klicka på knappen "*Start*".



![Image](assets/fr/013.webp)



#### Skapa ett konto



Välj en pseudonym eller ange ditt namn och ange sedan ett starkt lösenord. Var försiktig: detta lösenord är den enda barriären som skyddar åtkomst till din Umbrel från ditt nätverk (och därför potentiellt till dina bitcoins om du kör en Lightning-nod på Umbrel). Det skyddar också fjärråtkomst via Tor eller VPN, om dessa tjänster är aktiverade.



Välj ett starkt lösenord och se till att du har minst en säkerhetskopia (en lösenordshanterare rekommenderas).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

När du har skrivit in ditt lösenord klickar du på knappen "*Create*".



![Image](assets/fr/014.webp)



Din Umbrel-konfiguration är nu komplett.



![Image](assets/fr/015.webp)



#### Upptäckten av Interface



Umbrels Interface är ganska intuitiv:





- På startsidan kan du se dina installerade program och widgetar.



![Image](assets/fr/016.webp)





- I "*App Store*" kan du installera nya applikationer,



![Image](assets/fr/017.webp)





- Menyn "*Filer*" samlar alla dokument som finns lagrade på din Umbrel.



![Image](assets/fr/018.webp)





- I menyn "*Settings*" kan du ändra inställningarna för din Umbrel och komma åt information om den, t.ex:
    - Uppdatera, starta om eller stoppa din maskin;
    - Kontrollera tillgängligt lagringsutrymme, RAM-användning och processortemperatur;
    - Byt bakgrundsbild;
    - Hantera fjärråtkomst via Tor, aktivera Wi-Fi eller 2FA.



![Image](assets/fr/019.webp)



#### Säkerhets- och anslutningsinställningar



Först och främst rekommenderar jag starkt att du aktiverar tvåfaktorsautentisering (2FA). Detta lägger till en extra Layer av säkerhet till ditt lösenord. Det är nästan oumbärligt om du planerar att använda din Umbrel för att lagra personliga filer, köra en Lightning-nod eller utföra någon annan känslig aktivitet.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

För att göra detta klickar du på motsvarande ruta i inställningarna.



![Image](assets/fr/020.webp)



Skanna sedan QR-koden som visas med hjälp av din autentiseringsapplikation. Ange sedan den 6-siffriga dynamiska koden i det fält som finns på din Umbrel.



Från och med nu kommer varje ny anslutning till din Umbrel att kräva både lösenordet och den 6-siffriga koden som genereras av din 2FA-applikation (tvåfaktorsautentisering).



![Image](assets/fr/021.webp)



När det gäller fjärråtkomst via Tor, om du inte behöver det, rekommenderar jag att du låter det här alternativet vara avaktiverat för att begränsa attackytan för din Umbrel. Som standard kan din nod endast nås från en maskin som är ansluten till samma lokala nätverk. Om du aktiverar åtkomst via Tor kan du ändå hantera din Umbrel när du är på resande fot.



Om du aktiverar den här funktionen blir det teoretiskt möjligt för vilken maskin som helst i världen att försöka ansluta till din nod, förutsatt att den känner till Tor Address. Ditt lösenord och 2FA kommer dock fortfarande att skydda dig.



Om du aktiverar det här alternativet ska du se till att du har aktiverat tvåfaktorsautentisering (2FA), ett starkt lösenord och aldrig avslöja din Tor-anslutning Address.



Ange bara detta Tor Address i din Tor-webbläsare för att komma åt Umbrels Interface från vilket nätverk som helst.



![Image](assets/fr/026.webp)



Slutligen kan du på den här inställningssidan också aktivera Wi-Fi-anslutningen. Om din maskin som är värd för Umbrel har ett Wi-Fi-nätverkskort eller en Wi-Fi-dongle, kan du komma åt Internet utan att använda RJ45-kabeln. Beroende på din konfiguration kan denna lösning dock göra anslutningen långsammare, vilket kan påverka den initiala synkroniseringen (IBD) och framtida användning av noden (t.ex. för Lightning-transaktioner). Personligen rekommenderar jag inte det här alternativet, eftersom en nod inte är avsedd för mobil användning: den är alltid åtkomlig på distans, så du kan lika gärna låta den vara inkopplad.



### Steg 6: Installera en Bitcoin-nod på Umbrel



Nu när UmbrelOS är korrekt installerat och konfigurerat på din maskin kan du fortsätta med att installera din Bitcoin-nod. Ingenting kan vara enklare: gå till App Store, öppna kategorin "*Bitcoin*" och välj sedan applikationen "*Bitcoin Node*" (det är faktiskt Bitcoin core).



![Image](assets/fr/022.webp)



Klicka sedan på knappen "*Install*".



![Image](assets/fr/023.webp)



När installationen är klar kommer din Bitcoin-nod att starta sin IBD (*Initial Block Download*): den kommer att ladda ner och validera alla transaktioner och block sedan Bitcoin skapades 2009.



![Image](assets/fr/024.webp)



Detta steg är särskilt tidskrävande eftersom det beror på flera faktorer, bland annat hur mycket RAM-minne som har tilldelats nodcachen, diskhastigheten, Internetanslutningens hastighet och processorns effekt. Varaktigheten är därför mycket varierande beroende på konfiguration. Med en högpresterande dator (NVMe SSD, +32 GB RAM, kraftfull processor och bra internetanslutning) kan IBD slutföras på cirka tio timmar. Å andra sidan kan en gammal processor, lågt RAM-minne eller, ännu värre, en mekanisk Hard-disk (starkt avrådd) förlänga denna operation till flera veckor.



Med en dator med normal konfiguration (en hyfsad processor, 8 till 16 GB RAM och en SSD-enhet) räcker den i cirka 2 till 7 dagar.



För att snabba upp IBD något kan du öka RAM-minnet som allokeras till nodcachen (används främst för UTXO-uppsättningen, som vi återkommer till senare i kursen) via parametern `dbcache`. På Umbrel görs denna modifiering i dina nodparametrar, på fliken "*Optimization*".



![Image](assets/fr/025.webp)



Som standard är värdet för parametern `dbcache` i Bitcoin core inställt på 450 MiB, eller cirka 472 MB. Genom att öka detta värde kan du snabba upp IBD något. Jag skulle dock inte nödvändigtvis rekommendera att du sätter den här parametern för högt: även om du sätter den till 4 GiB blir synkroniseringen bara ca 10% snabbare, och du kan förlora tid om det blir ett avbrott under IBD.



Var försiktig så att du inte allokerar ett värde som är för stort för din maskin. Om det RAM-minne som är tillgängligt för UmbrelOS tar slut kan din nod stanna plötsligt, vilket avbryter IBD och kräver att du startar om den manuellt, vilket leder till en avsevärd tidsförlust.



Om du vill veta mer om hur parametern `dbcache` påverkar den initiala synkroniseringen rekommenderar jag den här analysen av Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*] (https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



När IBD för din nod har slutförts (100% synkronisering), har du nu en fullt fungerande Bitcoin-nod. Gratulerar, du är nu en integrerad del av Bitcoin-nätverket!



![Image](assets/fr/027.webp)



I nästa del ska vi utforska den praktiska användningen av din nya nod: hur du ansluter din Wallet till den och vilka program du bör installera för att bli en suverän Bitcoiner.





# Ansluta din Wallet till din nod


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexerare: roll, funktion och lösningar


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Om du redan har utforskat Bitcoin-noder innan du går den här kursen kanske du har stött på termen "indexerare". Det här är verktyg som Electrs eller Fulcrum, som kan läggas till i en Bitcoin core-nod. Men vad är egentligen deras roll? Hur fungerar de i praktiken? Och bör du installera en sådan på din nya Bitcoin-nod? Det är vad vi ska utforska i det här kapitlet.



### Vad är en indexerare?



Generellt sett är en indexerare ett program som skannar en uppsättning rådata, extraherar relevanta nycklar (t.ex. ord, identifierare och adresser) och bygger upp en extra fil, ett s.k. index, där varje nyckel hänvisar till den exakta platsen för data i korpusen. Denna förbehandlingsfas tar CPU-tid i anspråk och kräver en del diskutrymme, men den eliminerar behovet av att bearbeta hela korpusen varje gång databasen tillfrågas; en enkel förfrågan i indexet ger ett nästan omedelbart svar.



I lekmannatermer är det samma princip som ett index i en bok: om du letar efter en viss information, i stället för att läsa om hela boken, konsulterar du indexet för att direkt hitta den sida där den information du letar efter finns.



I en Bitcoin-nod, som Bitcoin core, lagras Blockchain-data i sin råa, kronologiska form. Varje block innehåller transaktioner, som i sin tur innehåller in- och utdata, utan någon särskild klassificering efter Address, identifierare eller Wallet. Denna linjära organisation är optimerad för blockvalidering, men olämplig för riktade sökningar. Om du t.ex. vill hitta alla transaktioner som är kopplade till en viss Address i en icke-indexerad nod måste du manuellt granska hela Blockchain, block för block och transaktion för transaktion. Det är just här som indexeraren på din Bitcoin-nod kommer in i bilden.



![Image](assets/fr/085.webp)



En indexerare är ett specialiserat program som analyserar denna massa av rådata (Blockchain, Mempool, UTXO set) och extraherar nycklar, såsom transaktionsidentifierare, adresser och blockhöjder. Från dessa nycklar bygger den sitt index och associerar varje nyckel med den exakta platsen för informationen i nodens lagring.



![Image](assets/fr/086.webp)



Indexering gör att du kan söka efter information på din nod snabbt, exakt och effektivt. När du till exempel ansluter en Wallet som Sparrow till din nod kan den visa saldot för en Address nästan omedelbart. I konkreta termer frågar den indexeraren med en begäran som: "_Vilka UTXO:er är associerade med detta skript-Hash?_" Indexeraren svarar nästan omedelbart, utan att behöva läsa om hela Blockchain, eftersom dessa data redan finns listade i dess databas.



### Har Bitcoin core en indexerare?



Utan behov av ytterligare programvara erbjuder Bitcoin core strängt taget inte en komplett Address-indexerare som kan jämföras med dem som finns i programvara som Electrs eller Fulcrum. Trots detta innehåller den flera interna indexeringsmekanismer, liksom valfria alternativ för att utöka dess frågefunktioner. För att fullt ut förstå situationen måste vi ta en omväg in i projektets historia.



Fram till Bitcoin core version 0.8.0 baserades transaktionsvalideringen på ett globalt transaktionsindex, känt som "txindex". Detta index refererade till alla Blockchain-transaktioner och deras utdata. När en nod tog emot en ny transaktion konsulterade den detta index för att verifiera att de förbrukade utdata (i inputs) faktiskt existerade och inte redan hade spenderats. `txindex` var därför oumbärligt för transaktionsvalidering vid den tiden.



Detta tillvägagångssätt hade dock sina begränsningar: det var långsamt, kostsamt i fråga om lagring och överflödigt i fråga om information. För att åtgärda detta introducerar version 0.8.0 en översyn av valideringsmodellen som kallas ***Ultraprune***. Istället för att lagra allt i form av transaktionsindex upprätthåller Bitcoin core en enkel databas som endast är avsedd för UTXO:er, kallad "chainstate" (på vardagsspråk kallas detta "UTXO set"), och uppdaterar dess lista när utgångar konsumeras och skapas.



Denna metod är mycket snabbare och lagrar endast registrets aktuella tillstånd, vilket gör indexeraren `txindex` onödig. Men istället för att ta bort `txindex`-koden har utvecklarna valt att behålla denna funktionalitet bakom en enkel parameter (`txindex=1`). Genom att aktivera detta alternativ på din nod kan du fråga vilken transaktion som helst från dess `txid`.



I motsats till vad många tror erbjuder Bitcoin core inte Address-baserad indexering som Electrs eller Fulcrum. Det finns flera anledningar till detta val:





- Bitcoin core:s roll är inte att bli en komplett Block explorer eller att tillhandahålla ett API som är skräddarsytt för varje användning. Att integrera ett Address-baserat index skulle innebära ett långsiktigt underhåll av Commitment som går utöver programvarans ursprungliga omfattning.





- De flesta användningsfall kan redan täckas på andra sätt. Om du t.ex. vill uppskatta balansen för en Address kan du använda kommandot `scantxoutset`, som direkt frågar efter UTXO-uppsättningen utan att kräva ett fullständigt index.





- Varje program har specifika krav på formatet eller typen av data som ska indexeras (Address, Hash-skript, proprietär tagg etc.). Det är mer flexibelt och logiskt att låta dessa program bygga sina egna anpassade index än att fixa en generisk lösning i Bitcoin core.



Bitcoin core har en valfri transaktionsindexerare (`txindex`), en kvarleva av dess historiska funktion, men den tillhandahåller inte ett Address-index eller en direkt Interface för komplexa sökningar. I vissa fall kan det därför vara användbart att lägga till en extern indexerare.



### Bör du lägga till en Address indexerare till din nod?



Det är inte obligatoriskt att lägga till en Address indexerare, t.ex. Electrs eller Fulcrum, utan det beror på dina specifika behov.



Om du helt enkelt vill ansluta en Wallet, till exempel Sparrow, till din nod för att se saldon och sända transaktioner, är detta fullt möjligt direkt via Bitcoin core:s Interface RPC, antingen lokalt eller på distans via Tor.



Å andra sidan, för att använda mer avancerad programvara, till exempel att köra en Mempool.Lokalt blir installationen av en Address-indexerare oumbärlig för utrymmet Block explorer.



Indexeraren kräver en viss synkroniseringstid (mindre än IBD) och kommer att uppta ytterligare diskutrymme. Om din SSD fortfarande har tillräckligt med ledigt utrymme efter att du har laddat ner Blockchain kan du enkelt lägga till en indexerare.



### Vilken indexerare ska man välja?



Två programvaror används ofta för att bygga upp den här typen av Address-index och göra det tillgängligt: **Electrs** och **Fulcrum**. Dessa verktyg indexerar Blockchain enligt script-Hash (adresser) och föreslår sedan en standardiserad Interface (Electrum-protokollet), till vilken många plånböcker, såsom Electrum Wallet, Sparrow eller Phoenix, ansluter.



![Image](assets/fr/087.webp)



Enkelt uttryckt är Electrs ganska kompakt: det indexerar Blockchain snabbare och tar upp mindre diskutrymme, men presterar något sämre än Fulcrum på frågor. Fulcrum däremot förbrukar mer diskutrymme och tar längre tid att indexera, men erbjuder överlägsen frågeprestanda.



För privat bruk rekommenderar jag Electrs: det tar mindre utrymme, är väl underhållet och även om det är något långsammare på vissa förfrågningar än Fulcrum är det fortfarande mer än tillräckligt för daglig användning. Om du har tid och diskutrymme kan du också prova Fulcrum, som kommer att prestera betydligt bättre, särskilt på plånböcker med många adresser som ska verifieras.



Konkret kommer Electrs i augusti 2025 att kräva cirka 56 GB lagringsutrymme, jämfört med cirka 178 GB för Fulcrum. Ditt val av indexerare beror därför också på din lagringskapacitet:




- Om ditt diskutrymme är mycket begränsat måste du nöja dig med Bitcoin core utan en extern Address-indexerare.
- Om du vill använda en indexerare, men fortfarande har kapacitetsbegränsningar, ska du välja Electrs.
- Om du har gott om diskutrymme kan Fulcrum vara precis vad du letar efter.



Under resten av den här BTC 202-kursen kommer jag att använda Electrs, men du kan enkelt följa med Fulcrum: installationsproceduren är identisk, liksom Interface-anslutningen till Wallet, eftersom båda exponerar en Electrum-server.



### Hur installerar jag en indexerare på Umbrel?



För att installera Electrs (eller Fulcrum) på din Umbrel är proceduren enkel: gå till App Store, sök efter den relevanta applikationen (som finns på fliken Bitcoin) och klicka sedan på knappen "*Install*".



![Image](assets/fr/028.webp)



När installationen är klar kommer Electrs att fortsätta med en synkroniseringsfas (indexering), som kan ta flera timmar.



![Image](assets/fr/029.webp)



När synkroniseringen är klar kan du ansluta din Wallet-programvara till din Electrum-server, som är hostad på Umbrel.



## Hur ansluter jag min Wallet till min Bitcoin-nod?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nu när du har en komplett Bitcoin-nod är det dags att använda den på ett bra sätt! I nästa kapitel kommer vi att utforska andra potentiella användningsområden för din Umbrel-instans. Men låt oss börja med grunderna: att ansluta din Wallet-programvara för att använda information från din egen Blockchain och distribuera transaktioner via din egen nod.



Som nämnts ovan finns det två huvudsakliga anslutningsgränssnitt:




- Direkt anslutning till Bitcoin core via RPC;
- Eller anslut till en Electrum-server (Electrs eller Fulcrum).



I den här handledningen koncentrerar vi oss på att ansluta till din nod via Tor, eftersom detta är både en enkel och säker lösning för nybörjare. Jag avråder starkt från att exponera din nods RPC-port i klartext, eftersom felaktig konfiguration utgör en betydande risk för säkerheten och sekretessen för dina data. Den största nackdelen med kommunikation via Tor är dess långsamhet. I nästa kapitel kommer vi att utforska ett snabbt och säkert alternativ till Tor för fjärråtkomst till din nod: VPN.



Vi använder Sparrow som exempel i det här kapitlet, men proceduren är densamma för alla andra Wallet-hanteringsprogram som accepterar anslutningar till Electrum-servrar. Leta helt enkelt upp motsvarande inställning i dina programparametrar (vanligtvis i "*Server*", "*Network*", "*Node*"...).



På Sparrow öppnar du fliken "*File*" och går till menyn "Settings".



![Image](assets/fr/030.webp)



Klicka sedan på "*Server*" för att komma åt anslutningsparametrarna.



![Image](assets/fr/031.webp)



Du kommer sedan att upptäcka tre alternativ för att länka din programvara till en Bitcoin-nod:




- Public Server* (gul): som standard, om du inte äger en Bitcoin-nod, ansluter det här alternativet dig till en offentlig nod som du inte äger (vanligtvis ett företags). Det här alternativet är inte relevant här, eftersom du har din egen nod på Umbrel.
- Bitcoin core* (Green): detta alternativ motsvarar anslutning via Interface RPC, dvs. direkt till Bitcoin core.
- Private Electrum* (blå): med det här alternativet kan du ansluta via din indexerares Interface Electrum Server (Electrs eller Fulcrum).



### Anslutning till Bitcoin core RPC



Om din Umbrel-nod inte har en indexerare är detta det alternativ du måste välja. På Sparrow klickar du på "*Bitcoin core*".



![Image](assets/fr/032.webp)



Du kommer sedan att behöva ange flera uppgifter för att upprätta anslutningen till din nod. Alla dessa data kan nås från applikationen "*Bitcoin Node*" på Umbrel genom att klicka på knappen "*Connect*" i det övre högra hörnet på Interface.



![Image](assets/fr/033.webp)



Fliken "*RPC Details*" visar all information som behövs för anslutningen. Välj att ansluta via Tor Address (i `.onion`).



![Image](assets/fr/034.webp)



Ange dessa data i motsvarande fält på Sparrow wallet och klicka sedan på knappen "*Test Connection*".



![Image](assets/fr/035.webp)



Om anslutningen lyckas visas en Green-bock och ett bekräftelsemeddelande.



![Image](assets/fr/036.webp)



Bocken längst ned till höger på Interface Sparrow wallet kommer nu att vara Green (vilket indikerar en direkt anslutning till Bitcoin core).



**Note:** För att anslutningen ska lyckas måste din nod vara 100% synkroniserad. Om detta inte är fallet, vänligen vänta till slutet av IBD.



### Anslut till Electrs



Om din nod har en indexerare är det bättre att ansluta till den än att använda Bitcoin core direkt, eftersom dina frågor kommer att behandlas snabbare.



På Sparrow, gå till fliken "*Private Electrum*".



![Image](assets/fr/037.webp)



Du måste sedan ange flera uppgifter för att upprätta förbindelsen med din indexerare. Du hittar dessa uppgifter i applikationen "*Electrs*" (eller, i förekommande fall, "*Fulcrum*") på Umbrel.



Välj fliken "*Tor*" för att få `.onion`-anslutningen Address. Om du vill ansluta en mobil Wallet-programvara kan du också skanna QR-koden direkt.



![Image](assets/fr/038.webp)



Ange bara Tor Address för din Electrum-server i fältet "*URL*" och klicka sedan på knappen "*Test Connection*".



![Image](assets/fr/039.webp)



Om anslutningen lyckas visas en bockmarkering och ett bekräftelsemeddelande.



![Image](assets/fr/040.webp)



Fästingen i det nedre högra hörnet på Interface Sparrow wallet blir blå (den färg som associeras med anslutning till en Electrum-server).



**Anmärkning:** För att anslutningen ska fungera måste indexeraren vara 100% synkroniserad. Om så inte är fallet, vänta tills indexeringsprocessen är klar.



Nu vet du hur du ansluter din Wallet till din Bitcoin-nod! I nästa kapitel kommer jag att introducera dig till flera ytterligare applikationer som finns tillgängliga på Umbrel som jag är särskilt förtjust i, och som gör att du kan förbättra din dagliga användning av Bitcoin via din nod.




## Översikt över tillgängliga applikationer


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel erbjuder en omfattande applikationsbutik. Som du kommer att se finns det många verktyg som är relaterade till Bitcoin, men också ett brett utbud av applikationer inom mycket olika områden: self-hosting-lösningar för tjänster och filer, produktivitetsapplikationer, mer allmänna finansiella verktyg, mediehantering, nätverkssäkerhet och administration, utveckling, artificiell intelligens, sociala nätverk och till och med hemautomation.



I denna BTC 202-kurs kommer vi att koncentrera oss uteslutande på Bitcoin-relaterade applikationer. Du är dock välkommen att utforska resten av katalogen för verktyg som kan vara till nytta för dig.



Det skulle naturligtvis vara omöjligt att lista alla Bitcoin-applikationer här. I det här kapitlet vill jag presentera de viktigaste verktygen som kommer att underlätta och berika din dagliga användning av Bitcoin.



### Mempool.space



I den dagliga användningen av Bitcoin, om det finns ett verktyg som verkligen är oumbärligt, är det Block explorer. Oavsett om den är tillgänglig online eller installerad lokalt omvandlar den Blockchain:s rådata till ett strukturerat, tydligt och lättläst format. Den har också en sökmotor som gör det möjligt för användare att snabbt hitta ett specifikt block, en transaktion eller Address.



Konkret innebär det att du kan uppskatta de avgifter som krävs för att din transaktion ska ingå i ett block, sedan följa dess utveckling: ta reda på om det är troligt att den kommer att ingå inom en snar framtid, beroende på avgiftsmarknaden, och slutligen bekräfta att den verkligen har ingått i ett block. Det ger också möjlighet att analysera dina tidigare transaktioner och konsultera deras historik. Kort sagt, det är bitcoinerns schweiziska armékniv.



Som tidigare nämnts kan en explorer finnas online på en webbplats eller köras lokalt på din dator. En stor nackdel med onlinetjänster är att de kan äventyra din integritet. Utan VPN eller Tor kan servern som är värd för utforskaren koppla din IP Address till de transaktioner du tittar på, vilket kan ge en idealisk ingångspunkt för kedjeanalys.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dessutom kan din Internetleverantör (ISP) veta att du tittar på en viss transaktion via Block explorer-webbplatsen. Detta väcker också en fråga om förtroende: du måste lita på att onlinetjänsten ger dig korrekt information om dina transaktioner, utan att själv kunna verifiera dess sanningsenlighet.



Det är därför det alltid är bäst att använda din egen lokala Block explorer. På så sätt läcker inga data relaterade till din sökaktivitet ut, eftersom alla frågor behandlas direkt på en maskin som du kontrollerar, utan att passera genom Internet. Dessutom förlitar sig en lokal utforskare på data från din egen Bitcoin-nod, som du själv har validerat, enligt dina egna regler, och som du kan lita på.



Umbrel erbjuder flera blockutforskare:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Jag är särskilt förtjust i Mempool.Space, som jag har installerat på min nod. Observera: för att använda de flesta blockutforskare på Umbrel krävs en Address indexerare. Du behöver därför applikationen Bitcoin Node (eller Bitcoin Knots), som har en 100% synkroniserad Blockchain, samt en indexerare som Electrs eller Fulcrum, som också är 100% synkroniserad.



När programmet är installerat är det bara att öppna det för att få tillgång till din egen explorer.



![Image](assets/fr/041.webp)



Om du vill lära dig mer om hur du använder Mempool.Space explorer rekommenderar jag denna omfattande handledning:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Blixtnod



Nu när du har din egen Bitcoin-nod kan du också sätta upp din egen Lightning-nod för att utföra off-chain-transaktioner utan att förlita dig på en infrastruktur från tredje part.



Umbrel erbjuder ett antal applikationer som hjälper dig att få igång din Lightning-nod. Du kan redan välja mellan två huvudsakliga implementeringar:




- LND, via applikationen *Lightning Node*;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Du kan sedan administrera din nod från huvud-Interface, eller, för ännu större funktionalitet och avancerade alternativ, installera *Ride The Lightning* eller *ThunderHub*. Dessa verktyg kommer att ge dig ett mycket mer omfattande webbaserat Interface-hanteringssystem för din nod.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Slutligen rekommenderar jag applikationen * Lightning Network+*, som gör det möjligt för dig att hitta kamrater som du kan öppna kanaler med, vilket möjliggör både utgående och inkommande kontanttransaktioner.



![Image](assets/fr/089.webp)



Tack vare Umbrel har det blivit mycket enklare att hantera en personlig Lightning-nod, men det är fortfarande relativt komplext. Av denna anledning kommer vi att titta närmare på detta ämne i en framtida kurs som helt ägnas åt denna användning.



### Svansvåg



En annan applikation som jag särskilt gillar på Umbrel är Tailscale. Det är en VPN-applikation som är utformad för att förenkla skapandet av säkra nätverk mellan flera enheter, oavsett var de kan vara i världen. Till skillnad från traditionella VPN, som förlitar sig på centraliserade servrar, använder Tailscale WireGuard-protokollet för att upprätta end-to-end-krypterade anslutningar mellan dina olika maskiner. Detta innebär att du kan distribuera ett fungerande VPN på bara några minuter, utan behov av komplicerade nätverkskonfigurationer.



På Umbrel ansluter Tailscale-installationen din Bitcoin-nod till ditt eget virtuella privata nätverk. När den har konfigurerats får din nod en privat Tailscale IP Address, som endast är tillgänglig från andra enheter som är anslutna till samma Tailscale-nätverk (t.ex. datorer, smartphones och surfplattor). Den här anslutningen är krypterad från början till slut och passerar inte genom ett oskyddat offentligt nätverk, vilket avsevärt förbättrar säkerheten jämfört med en okrypterad anslutning.



![Image](assets/fr/090.webp)



Konkret innebär Tailscale att du får flera fördelar när du använder din Umbrel:





- Du kan administrera Interface Umbrel eller komma åt de applikationer som är kopplade till din nod (t.ex. Mempool, Ride The Lightning, ThunderHub ...) var som helst, som om du var på samma lokala nätverk, utan att exponera portar på Internet och utan att gå igenom Tor, vilket är mycket långsamt;





- Du kan ansluta till din Electrum-server (Electrs eller Fulcrum) eller direkt till Bitcoin core via ditt VPN och kringgå Tor. Detta ger en säker anslutning, jämförbar med att använda Tor, men med mycket högre hastighet och minskad latens. Kort sagt, du behåller integritets- och säkerhetsfördelarna med Tor samtidigt som du får hastigheten hos en Clearnet-anslutning. För en On-Chain Wallet kan denna vinst verka marginell, men om du planerar att sätta upp din egen Lightning-nod vid ett senare tillfälle är skillnaden avsevärd. Att göra betalningar via din nod på resande fot på Tor är faktiskt extremt långsamt på grund av de många utbyten som krävs, medan det med Tailscale fungerar perfekt.





- Du behöver inte konfigurera NAT-regler, öppna portar eller sätta upp en vanlig VPN-server. När applikationen har installerats på Umbrel och dina enheter upprättas nätverket automatiskt.



Tailscale på Umbrel är därför en mycket intressant lösning om du vill komma åt din nod från var som helst i världen på ett säkert, högpresterande och lättkonfigurerat sätt, utan att göra avkall på integritet eller säkerhet.



För att installera och konfigurera Tailscale på din Umbrel, se denna handledning, avsnitt 4: "*Använda Tailscale på Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, en akronym för "*Notes and Other Stuff Transmitted by Relays*", är ett öppet, decentraliserat protokoll som är utformat för att göra det möjligt att publicera och utbyta meddelanden på Internet utan att vara beroende av en centraliserad plattform. Varje användare har ett par kryptografiska nycklar: den publika nyckeln (npub), som fungerar som en identifierare, och den privata nyckeln (nsec), som används för att signera meddelanden och garantera deras äkthet.



Meddelanden överförs via ett nätverk av oberoende reläer. Denna distribuerade arkitektur gör Nostr motståndskraftigt mot censur: ingen enskild server kontrollerar åtkomst eller distribution, och en användare kan ansluta sig till så många reläer som de vill.



Detta protokoll är mycket populärt inom Bitcoin-communityn eftersom Nostr, precis som Bitcoin, tar upp frågor om digital suveränitet och datakontroll. Dess skapare, Fiatjaf, är en utvecklare som redan är erkänd i ekosystemet för sina många bidrag.



Med din Umbrel kan du optimera din användning av Nostr. Genom att installera applikationen ***Nostr Relay*** kan du vara värd för ditt eget privata relä direkt på din maskin, vilket säkerställer att alla dina inlägg och interaktioner på Nostr sparas lokalt och inte kan gå förlorade genom radering av offentliga reläer.



Nostr-klienterna ***noStrudel*** eller ***Snort*** är också tillgängliga på Umbrel. Tack vare dessa applikationer kan du publicera, läsa, söka efter profiler och interagera med Nostr-ekosystemet direkt från Interface-webben på din Umbrel.



Slutligen finns det ***Nostr Wallet Connect***-appen på Umbrel, som möjliggör inbyggda Lightning-betalningar i Nostr. Konkret kan du länka din framtida Lightning-nod till dina Nostr-kunder för att skicka mikrobetalningar, så kallade "*zaps*", för att belöna innehåll eller interagera på ett monetärt sätt, utan att behöva gå via en tredjepartstjänst. Dessa betalningar skickas direkt från din personliga nod via dina kanaler.



För att ta reda på hur du använder alla dessa applikationer rekommenderar jag att du tar en titt på den här fullständiga handledningen:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay-server



BTCPay Server är en kostnadsfri betalningsprocessor med öppen källkod som gör att du kan ta emot betalningar via Bitcoin och Lightning Network utan mellanhänder, samtidigt som du behåller egen förvaring av medel.



BTCPay Servers arkitektur är baserad på en Bitcoin-nod och, för Lightning, på en kompatibel implementering (LND, Core Lightning ...), vilket gör den till en av de enda helt icke-frihetsberövande PoS-lösningarna. Det är också den mest omfattande programvaran för spårning och redovisning.



![Image](assets/fr/091.webp)



Om du äger ett företag och vill acceptera Bitcoin-betalningar direkt via din Umbrel-nod är BTCPay Server-applikationen idealisk för dig. För att ta reda på mer om detta ämne rekommenderar jag att du konsulterar följande resurser:





- BIZ 101-kursen om hur du använder Bitcoin i ditt företag:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- POS 305-kursen om att använda BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Handledning för BTCPay Server:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Avancerade koncept och bästa praxis


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Underhåll av din Umbrel-knut


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



För att inleda detta sista avsnitt, och innan vi går vidare till mer avancerad teori, vill jag undersöka de bästa metoderna och konkreta åtgärder som du kan vidta när din Umbrel-nod är installerad, synkroniserad och korrekt konfigurerad i detta korta kapitel. Hur underhåller du den på daglig basis?



### Hålla utrustningen frisk



En tillförlitlig nod börjar med stabil maskinvara. Se till att maskinen som inrymmer noden är ordentligt ventilerad, Dust-fri och installerad i en torr miljö, borta från alla källor till värme och luftfuktighet. Undvik att klämma in den i ett trångt utrymme och välj en väl ventilerad plats.



På Raspberry Pi och mini-PC:er täpper Dust så småningom till kylflänsarna, vilket höjer temperaturen och leder till strypning (frivillig begränsning av resursanvändning), vilket i sin tur leder till att nodens effektivitet sjunker. Det är därför jag rekommenderar att du rengör luftintaget och fläkten regelbundet, helst varannan månad.



Se till att du använder en högkvalitativ strömförsörjning Supply, eftersom instabil spänning kan leda till systemförstöring och till och med utgöra en brandrisk. Helst bör du använda originalström Supply som levereras av tillverkaren av din maskin. Se också upp för överhettning på grund av Joule-effekten på grenuttag: respektera alltid den högsta tillåtna effekten och anslut aldrig flera grenuttag i kaskad.



Jag rekommenderar också att du investerar i en UPS. Detta skyddar din nod från plötsliga nedstängningar, gör det möjligt för Umbrel att stänga av rent i händelse av ett avbrott och säkerställer kontinuitet i driften under mikroavbrott eller kortvariga fel.



På lagringssidan bör du hålla ett öga på utvecklingen: om disken närmar sig mättnad bör du överväga att frigöra utrymme (avinstallera oanvända appar, justera indexeringsinställningarna) eller migrera till en större SSD. Nackdelen med en full Bitcoin-nod är att dess lagringskrav ökar kontinuerligt, eftersom ett nytt block genereras var 10:e minut och gamla block inte kan raderas (såvida inte noden är pruned). Jag råder dig därför att planera för en tillräckligt stor kapacitet när du köper din hårdvara (minst 2 TB).



### Uppdatering



Node-uppdateringar är viktiga av tre huvudsakliga skäl: för det första säkerhet (sårbarhetsuppdateringar, nätverkshärdning och DoS-skydd); för det andra kompatibilitet (reläpolicyändringar, formatändringar och protokolluppgraderingar); och för det tredje tillförlitlighet och prestanda (buggfixar, resursförbrukning och andra förbättringar). Så kontrollera regelbundet att UmbrelOS och dina appar är uppdaterade:





- För att uppdatera systemet: Öppna inställningsmenyn och klicka sedan på knappen "*Check for Update*" bredvid parametern "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Så här uppdaterar du program: Gå till App Store. Om någon av dina applikationer behöver uppdateras visas en knapp med en röd bubbla i det övre högra hörnet på Interface. Klicka bara på den och uppdatera sedan varje applikation.



Utför denna åtgärd regelbundet för att hålla ditt operativsystem och dina program uppdaterade.



### Säkerhetskopior



Om du bara använder din Bitcoin-nod för att validera och distribuera dina transaktioner, men dina plånböcker hanteras utanför Umbrel (t.ex. med en Hardware Wallet och Sparrow wallet), finns det inget att säkerhetskopiera direkt till Umbrel. I det här fallet förblir den väsentliga säkerhetskopian den för återställningsfrasen och Descriptor för din externa Wallet, och detta gäller oavsett om du använder din egen nod eller inte. Så ingenting förändras från din tidigare konfiguration.



Å andra sidan, beroende på de ytterligare applikationer du använder på Umbrel, kan ytterligare säkerhetskopior krävas. Detta är särskilt fallet om du driver en Lightning-nod på Umbrel. I det här fallet är det absolut nödvändigt att säkerhetskopiera seed som levererades när du installerade din Lightning-nod. Förutom seed behöver du en uppdaterad ***Static Channel Backup (SCB)*** för att kunna återställa din Lightning-nod i händelse av problem. SCB gör att du kan återfå dina pengar genom att tvångsstänga kanaler. Om antingen seed eller SCB saknas är det omöjligt att återställa en Lightning-nod.



Umbrel erbjuder också möjligheten att automatiskt och dynamiskt säkerhetskopiera denna SCB på sina servrar, via Tor, för att säkerställa att en uppdaterad fil alltid finns tillgänglig. I detta fall behövs endast seed för att återställa noden.



Vi kommer att gå igenom dessa aspekter i detalj i nästa LNP202-kurs.



### Daglig driftsäkerhet



När det gäller säkerhet, använd ett långt, unikt och slumpmässigt lösenord för Interface Umbrel och kom ihåg att aktivera tvåfaktorsautentisering (2FA). För applikationer som erbjuder både lösenord och 2FA-skydd ska du alltid aktivera båda och ändra standardlösenorden.



Exponera aldrig instrumentpanelen mot Internet utan att använda en säker gateway (t.ex. VPN, Tor eller endast lokal åtkomst). Begränsa antalet program du installerar och radera regelbundet de du inte längre behöver för att minska attackytan.



För att fördjupa dina kunskaper om datasäkerhet i allmänhet rekommenderar jag starkt att du kollar in den här andra gratis kursen:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnos och hjälp till självhjälp



I händelse av en bugg på din Umbrel, först generate ett diagnostikpaket via felsökningsavsnittet i UmbrelOS eller den berörda applikationen, starta sedan om applikationen. Om det behövs, försök också med en fullständig omstart av systemet.



Om problemet kvarstår rekommenderar jag att du [går med i Umbrels användargrupp på deras Discord] (https://discord.gg/efNtFzqtdx). Börja med att göra en sökning för att avgöra om någon redan har stött på samma problem och hittat en lösning. Om inte, kan du posta ett meddelande i kanalen `general-support`. Du kan också använda [the Umbrel forum](https://community.umbrel.com/).



Där kan du inte bara följa säkerhetsmeddelanden och uppdateringar, utan också ställa frågor och i slutändan hjälpa andra användare. Det är ofta i dessa utbyten som bästa praxis upptäcks.



Med dessa enkla vanor kommer din Umbrel-nod att förbli stabil, säker och användbar, både för dig och för Bitcoin-nätverket.




## Förståelse för IBD och peer discovery-processen


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Din Bitcoin-nod startar upp utan någon tidigare kunskap om transaktionshistoriken. Till en början är det bara en dator som kör programvara (Bitcoin core eller liknande). För att bli en fullt synkroniserad och operativ Bitcoin-nod måste den lokalt rekonstruera tillståndet för Ledger genom att kontrollera alla block som publicerats sedan Genesis-blocket (block 0, publicerat av Satoshi Nakamoto den 3 januari 2009). Detta steg kallas **IBD (_Initial Block Download_)**.



IBD består av att ladda ner och verifiera varje block och transaktion individuellt, med tillämpning av konsensusreglerna, för att bygga sin egen version av Blockchain. Syftet är inte bara att hämta en kopia av overifierad data, utan att komma fram till samma slutsats helt oberoende, som den ärliga majoriteten av nätverket.



![Image](assets/fr/092.webp)



### Milstolpar inom IBD



Synkroniseringen börjar med steget _**headers-first**_. Din nod begär sekvensen av blockheaders från flera peers och verifierar för var och en av dem Proof of Work, svårighetsjustering, syntax samt Timestamp och reglerna för versionsnummer. Kort sagt, den säkerställer att varje header som tas emot överensstämmer med konsensusreglerna.



![Image](assets/fr/093.webp)



Som en påminnelse består ett Bitcoin-block av en header på 80 byte och en lista med transaktioner. Blockets fingeravtryck erhålls genom att tillämpa en dubbel SHA-256 Hash på detta huvud, som innehåller 6 fält:




- version
- Hash av föregående block
- Merkle Root av transaktioner
- Timestamp (längre än mediantiden för de föregående 11 blocken)
- svårighet mål
- Nonce



![Image](assets/fr/094.webp)



Transaktionerna överförs till ett Merkle Tree. Detta är en struktur som sammanfattar en stor uppsättning data (i det här fallet alla transaktioner i blocket) genom att aggregera deras hashvärden successivt två och två ner till en enda "rot", vilket bevisar att ett element tillhör uppsättningen (och upptäcker eventuella ändringar). På så sätt modifierar varje ändring av en transaktion också roten i Merkle Tree och därmed blockhuvudets fingeravtryck. SegWit har infört en separat ytterligare Commitment för cookies (signaturer), placerad i myntbasen.



![Image](assets/fr/095.webp)



Detta _**headers-first**_-steg gör det möjligt för noden att identifiera den gren som har mest arbete (oavsett antal block), vilket är den gren som Bitcoin-noderna synkroniserar på. När denna gren har identifierats hämtar noden innehållet i blocken parallellt från flera anslutningar och validerar sedan varje transaktion: format, giltighet för skript (utom `assumevalid=1`), belopp och frånvaro av dubbla utgifter. Vid varje lyckad kontroll uppdateras det aktuella tillståndet för outnyttjade mynt (UTXO-uppsättningen) i databasen `chainstate/`: förbrukade utgångar tas bort, medan nya giltiga utgångar läggs till.



Mempool spelar däremot bara in när man närmar sig kedjans spets: så länge noden är sen har den inga väntande transaktioner att lagra.



När IBD är klar går noden in i sin normala fas: den validerar nya block när de publiceras, underhåller sin Mempool med väntande transaktioner enligt sina reläregler, vidarebefordrar transaktioner och block och hanterar eventuella omorganisationer av kedjan.



### AntaGiltig



Bitcoin core innehåller en mekanism som är utformad för att minska den tid som krävs innan en nod är fullt operativ, samtidigt som kärnan i den autonoma verifieringsprincipen bibehålls: AntaGiltig.



Parametern `assumevalid` är baserad på ett tidigare referensblock, vars Hash integreras i varje programvaruversion. Om din nod under IBD upptäcker att detta block verkligen finns på den gren som har mest arbete, kan den ignorera skriptverifiering för alla transaktioner före denna punkt.



Alla andra regler (blockstruktur, Proof of Work, storleksgränser, transaktionsbelopp, UTXO, etc.) förblir fullständigt verifierade. Endast beräkningen av skript före detta referensblock ignoreras. Prestandavinsten är betydande på IBD, eftersom signaturverifiering står för en stor del av CPU-belastningen. Efter detta referensblock återgår verifieringen till sitt normala tillstånd.



Du kan tvinga fram fullständig validering av alla skript genom att inaktivera denna mekanism, till priset av en mycket längre IBD, med hjälp av parametern `assumevalid=0` i filen `Bitcoin.conf`.



### AntaUTXO



`assumeutxo` är en annan befintlig parameter, men till skillnad från `assumevalid` är den inte aktiverad som standard. Denna mekanism gör det möjligt för programvaran att ladda en ögonblicksbild av UTXO-uppsättningen, tillsammans med dess metadata, och preliminärt betrakta den som ett referenstillstånd, efter att ha verifierat att rubrikerna verkligen leder till Blockchain med mest arbete.



Noden blir därmed snabbt operativ för vanliga användningsområden (RPC, anslutning av plånböcker etc.), samtidigt som den fullständiga, verifierade rekonstruktionen av sin egen UTXO-uppsättning startas i bakgrunden. När detta steg är slutfört ersätts den ursprungliga ögonblicksbilden av det lokalt rekonstruerade tillståndet. Detta tillvägagångssätt separerar snabb tillhandahållande av noder från fullständig verifiering, utan att kompromissa med den senare.



### Upptäckt av kollegor: Hur hittar din nod Bitcoin-nätverket?



När en nod startas upp för första gången känner den ännu inte till några peers. Den måste dock hitta andra Bitcoin-noder på Internet för att begära headers och sedan block för att kunna slutföra sin IBD. För att initiera dessa anslutningar följer Bitcoin core en prioriterad logik.



![Image](assets/fr/096.webp)



När noden startas om efter att redan ha använts försöker Core först återansluta till utgående peers som registrerades före avstängningen, information som lagras i filen `anchors.dat`. Sedan konsulterar den sin IP Address-bok **`peers.dat`**, som lagrar listan över tidigare påträffade peers, för att återansluta till dem. Detta är helt enkelt en lokal fil, som uppdateras och bevaras av Core. För en ny nod som precis har startats är dessa två filer däremot tomma, eftersom den ännu aldrig har kommunicerat med andra Bitcoin-noder.



I detta fall ställer programvaran frågor till _**DNS seeds**_. Dessa är [servrar som underhålls av erkända ekosystemutvecklare](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), som returnerar en lista med IP-adresser till förmodat aktiva noder. Dessa adresser gör det möjligt för den nya noden att initiera sina första anslutningar och begära nödvändiga data från IBD. Här är listan över *DNS seeds* som är aktiva hittills (augusti 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-lista-över-P2P-noder.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: "seed. Mainnet. Achownodes. xyz



I de allra flesta fall är steget *DNS seeds* tillräckligt för att upprätta de första förbindelserna med andra noder. Om dessa servrar undantagsvis inte svarar inom 60 sekunder byter noden till en annan metod: [en statisk lista med över 1 000 adresser](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) med _seed-noder_ är inbyggd i Bitcoin core:s kod och uppdateras regelbundet. Om de två första metoderna för att skaffa IP-adresser misslyckas upprättar denna sista lösning en första anslutning, från vilken noden sedan kan begära nya IP-adresser.



![Image](assets/fr/097.webp)



Som en sista utväg kan du manuellt Supply IP-adresser via filen `peers.dat` för att tvinga fram specifika anslutningar.



Efter uppstart diversifierar den interna Address-hanteraren källorna (separata autonoma nätverk, clearnet och Tor, samt olika geografiska områden) för att minska risken för topologisk isolering. Noden upprättar dessa utgående anslutningar (anslutningar som den själv väljer och som därför är säkrare).



Om din nod lyssnar på en öppen port (som standard 8333) accepterar den inkommande anslutningar. Dessa förstärker nätverkets övergripande motståndskraft genom att tillhandahålla en kontaktpunkt för nya noder, utan att ge någon särskild fördel för din egen IBD. Om din nod körs på Tor förblir logiken densamma, men de adresser som används är `.onion`-tjänster.




## Anatomin hos din Bitcoin-knut


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



När noden har slutfört sin första synkronisering lagrar den flera kompletterande datauppsättningar lokalt, vilket gör att den kan validera block och transaktioner, betjäna nätverkskollegor och starta om snabbt samtidigt som den behåller sitt tillstånd. 3 huvudstenar är viktiga på en nod:




- gW-402 **block** lagrade på disk,
- **UTXO-uppsättningen** i en databas med nyckelvärden,
- och **Mempool** lagras i RAM-minnet och serialiseras periodiskt.



Dessutom kompletteras bilden av flera hjälpfiler (peers, arvodesberäkningar, uteslutningslistor, plånböcker etc.). Låt oss ta reda på vad alla dessa filer har för roll.



### Var finns egentligen nodens data?



Som standard sparar Bitcoin core sina data i en specifik arbetskatalog. Under GNU/Linux är detta vanligtvis i `~/.Bitcoin/`, under Windows i `%APPDATA%\Bitcoin/` och under macOS i `~/Library/Application Support/Bitcoin/`. Om du använder en paketerad lösning (t.ex. inom en noddistribution) kan den här katalogen vara monterad någon annanstans, men dess struktur förblir densamma. De viktiga undermapparna och filerna som beskrivs nedan finns fortfarande här.



![Image](assets/fr/098.webp)



### Blocken



Blockchain är därför en samling block. En Full node lagrar dessa block som sekventiella platta filer och upprätthåller ett parallellt index för snabb hämtning. Vid behov (omorganisering, Wallet rescan, peer service) läses dessa data om som de är.



**En omorganisering, eller resynkronisering, är ett fenomen där Blockchain genomgår en modifiering av sin struktur på grund av att det finns konkurrerande block på samma höjd. Detta sker när en del av Blockchain ersätts av en annan kedja med en större mängd ackumulerat arbete. Dessa resynkroniseringar är en naturlig del av Bitcoin:s verksamhet, där olika gruvarbetare kan hitta nya block nästan samtidigt och därmed dela Bitcoin-nätverket i två. I sådana fall kan nätverket tillfälligt delas upp i konkurrerande kedjor. Så småningom, när en av dessa kedjor ackumulerar mer arbete, överges de andra kedjorna av noderna och deras block blir kända som "föråldrade block" eller "föräldralösa block" Denna process, där en kedja ersätts med en annan, kallas resynkronisering.



#### Blk*.dat-filer (rå blockdata)



Mottagna och validerade block skrivs till sekventiella behållare med namnet `blkNNNNN.dat`, som lagras i mappen `blocks/`. Varje fil fylls i sekvens tills den når en maximal storlek på 128 MiB, varvid Core öppnar nästa fil. Varje block är serialiserat i nätverksformat och föregås av en magisk identifierare och en längd. Den här organisationen möjliggör snabb skrivning till disk och underlättar blockservice för att synkronisera peers.



![Image](assets/fr/099.webp)



I pruned-läget behåller noden endast ett nytt fönster av dessa filer för att begränsa diskavtrycket. Den raderar de äldsta `blk*.dat`-containrarna så snart det konfigurerade utrymmesmålet nås, samtidigt som den behåller tillräckligt med historik för att förbli konsekvent med den mest kända kedjan. Indexet och UTXO-uppsättningen förblir normala, vilket gör att nästa transaktioner och block kan valideras.



#### Rev*.dat-filer (annulleringsdata)



För att kunna gå tillbaka i tiden under en omorganisation sparar Core, parallellt med varje `blk`-fil, en `revNNNNN.dat`-fil i `blocks/`. Denna fil innehåller den information som behövs för att upphäva effekten av ett block på UTXO-uppsättningen: för varje utgång som förbrukas av blocket lagras det tidigare tillståndet för motsvarande UTXO (mängd, skript, höjd ...). Om ett block avbryts kan noden snabbt återskapa det tidigare tillståndet utan att behöva skanna om hela kedjan.



![Image](assets/fr/100.webp)



#### Blockindex (block/index)



Att söka efter ett block direkt i de platta filerna skulle vara för tidskrävande. Core upprätthåller därför en LevelDB-databas i `blocks/index/` som för varje känt block listar metadata som Hash, höjd, valideringsstatus, `blk`-fil och offset där det finns. När en peer begär ett block, eller när en intern komponent behöver komma åt ett specifikt block, ger detta index snabb åtkomst. Utan detta index skulle det krävas alltför många operationer.



![Image](assets/fr/101.webp)



#### Valfria index (indexes/)



Vissa index är valfria och inaktiveras som standard eftersom de ökar diskutrymmet:




- `indexes/txindex/`, som vi redan har nämnt, tillhandahåller en mappningstabell för transaktion → plats, vilket gör det möjligt att hämta en bekräftad transaktion utan att känna till blocket som innehåller den. Detta är användbart för RPC-frågor av typen `getrawtransaction` utanför Wallet, men det är ganska dyrt.
- indexes/blockfilter/` som kan innehålla kompakta blockfilter (BIP157/158) för tunna klienter. Dessa strukturer påskyndar verifiering på klientsidan på bekostnad av ytterligare lagring på indexeringsnoden.



### UTXO uppsättning (kedjestat)



Modellen UTXO (*Unspent Transaction Output*) är den redovisningsmässiga representationen av Bitcoin: varje outnyttjad output är en tillgänglig "Coin" som kan användas som input för en framtida transaktion.



![Image](assets/fr/102.webp)



Alla dessa delar vid en given tidpunkt T utgör UTXO-uppsättningen: en stor lista över alla delar som nu är tillgängliga. Det är detta tillstånd som noden konsulterar för att avgöra om en transaktion spenderar legitima enheter som inte redan använts i en tidigare transaktion (för att undvika Double-spending).



![Image](assets/fr/103.webp)



UTXO-uppsättningen lagras i mappen `chainstate/` som en kompakt LevelDB-databas. Varje del associerar en nyckel som härrör från Hash för transaktionen och utgångsindexet med ett värde som innehåller: beloppet, `scriptPubKey` -låset, höjden på skapelseblocket och en coinbase-indikator.



![Image](assets/fr/104.webp)



Noden upprätthåller en minnescache ovanför LevelDB för att absorbera frekventa läs- och skrivoperationer. Parametern `dbcache` kan användas för att ändra storleken på denna cache: ju större den är, desto mer minnesåtkomst drar IBD och aktuell validering nytta av, till priset av högre RAM-förbrukning. När ett nytt block hittas av en Miner raderar noden från UTXO-uppsättningen de utdata som spenderats (eller förbrukats) av de transaktioner som ingår i blocket och lägger till de nyskapade utdata.



Teoretiskt sett skulle vi kunna validera en transaktion genom att skanna blockhistoriken på nytt för att kontrollera att ett uttag aldrig har använts. I praktiken skulle detta dock vara alldeles för tidskrävande, eftersom hela Blockchain skulle behöva skannas för varje ny transaktion. UTXO-uppsättningen ger därför den minimivy som krävs för att lokalt och inom rimlig tid bevisa att Double-spending inte finns.



Observera att UTXO-uppsättningen ofta är kärnan i oron för Bitcoin:s decentralisering, eftersom dess storlek naturligtvis ökar snabbt. Detta beror delvis på det stigande priset på Bitcoin, som uppmuntrar till fragmentering av delar, och delvis på den växande användningen av systemet: ju fler användare det finns, desto större är efterfrågan på UTXO:er.



![Image](assets/fr/105.webp)



Tillväxten av UTXO-uppsättningen härrör också från strukturen för enkla betalningstransaktioner på Bitcoin. När du gör en betalning konsumerar du faktiskt en enda UTXO som input och skapar 2 nya UTXO som output (en för betalningen och den andra för Exchange). Slutligen ger en heuristik för kedjeanalys, kallad CIOH (*Common Input Ownership Heuristic*), ytterligare ett incitament att undvika konsolidering av Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Eftersom en del av den måste förvaras i RAM-minnet för att transaktioner ska kunna verifieras inom rimlig tid, kan UTXO-uppsättningen gradvis göra driften av en Full node alltför kostsam. För att lösa detta problem finns det redan några förslag, bland annat [Utreexo] (https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool är den lokala uppsättningen av giltiga transaktioner som har tagits emot men ännu inte bekräftats. Som en påminnelse är en "bekräftad transaktion" en transaktion som har inkluderats i ett giltigt block. Varje nod upprätthåller sin egen Mempool, som kan skilja sig från andra noders i nätverket beroende på:




- den storlek som tilldelas Mempool via parametern `maxmempool`: en nod med en större Mempool kommer att kunna rymma fler transaktioner än en nod med en mindre Mempool (såvida inte den senare blir tom);
- gW-433-regler: dessa är en delmängd av nodens reläregler och definierar de egenskaper som en obekräftad transaktion måste uppfylla för att kunna accepteras i Mempool;
- transaktionsperkolation: På grund av olika faktorer kan en viss transaktion ha distribuerats till en del av nätverket, men ännu inte nått en annan del.



Det är viktigt att notera att nodernas mempooler inte har något konsensusvärde. Bitcoin fungerar perfekt även om varje nod har en annan Mempool. I slutändan är de auktoritativa blocken alltid de som läggs till i Blockchain. Till exempel, även om en nod initialt avvisar en given transaktion i sin Mempool (giltig enligt konsensusreglerna), kommer den att vara skyldig att acceptera den om den så småningom inkluderas i ett block med en giltig Proof of Work. Om den inte gör det och avvisar detta block, trots att det följer konsensusreglerna, utlöser det en Hard Fork, dvs. skapandet av en ny, separat Bitcoin som den är ensam om.



#### Policy och hantering av minnen



När en transaktion tas emot gör Core en rad kontroller mot konsensusregler (syntax, giltiga skript, inga dubbla utgifter etc.) och Mempool-regler, som är en lokal policy (RBF, lägsta avgiftströsklar, datagräns i `OP_RETURN` etc.). Om transaktionen följer dessa regler lagras den i minnet.



Storleken på Mempool begränsas av parametern `maxmempool` i filen `Bitcoin.conf` (mer om detta i nästa kapitel). Som standard är gränsen 300 MB. När den är full höjer noden dynamiskt sin lägsta avgiftströskel och utvisar de minst lönsamma transaktionerna först (dvs. den behåller transaktioner som bör minas först). Transaktioner som är för gamla kan också förfalla efter en konfigurerad fördröjning.



#### Mempool uthållighet på disk



För att påskynda omstarter serialiserar Core periodiskt Mempool:s tillstånd i filen `Mempool.dat` när noden stängs av. Förutom den faktiska Mempool, som finns kvar i minnet, lagrar Core filen `Mempool.dat` på disken. Nästa gång noden startas laddar den om denna ögonblicksbild och tar bort allt som inte längre är giltigt för den aktuella Blockchain.



### Extra filer och databaser



Flera andra filer på samma nivå som `blocks/`, `chainstate/` och `indexes/` medverkar till att systemet fungerar korrekt:




- `peers.dat` innehåller en IP Address-bok över potentiella peers, som matas in genom inledande DNS-upptäckt, nätverksutbyten och manuella tillägg. När noden startar kan den använda den här filen för att upprätta utgående anslutningar.
- När noden stängs av sparar `anchors.dat` adresserna till utgående peers, så att du snabbt kan försöka kontakta dem igen nästa gång du startar upp.
- `banlist.json` innehåller lokala förbud som beslutats av operatören eller av noden (upprepat ogiltigt beteende), för att förhindra att noden återansluter eller accepterar anslutningar från dessa specifika peers.
- i `fee_estimates.dat` lagras tidshorisontstatistik över observerade bekräftelser, som används av avgiftsberäknaren för att föreslå avgiftssatser som överensstämmer med de fördröjningsmål som valts när en transaktion skapades.
- gW-446.conf` innehåller din nods konfigurationsparametrar. Det är här du kan justera reläreglerna. Jag ska berätta mer om detta i nästa kapitel.
- `settings.json` innehåller ytterligare parametrar till `Bitcoin.conf`.
- `debug.log` är en diagnostisk textlogg som kan användas för att förstå nodens aktivitet om det uppstår en bugg.
- gW-448.pid` lagrar processidentifieraren vid körning, vilket gör att andra program eller skript enkelt kan identifiera bitcoind (*Bitcoin daemon*) och interagera med den vid behov. Den skapas vid nodstart och raderas vid nedstängning.
- `ip_asn.map` är en mappningstabell för IP → ASN (fristående system) som används för bucketing och peer-diversifiering (alternativet `-asmap`).
- `onion_v3_private_key` lagrar den privata nyckeln för Tor v3-tjänsten när alternativet `-listenonion` är aktiverat, för att hålla en stabil lök Address mellan omstarter.
- `i2p_private_key` lagrar I2P:s privata nyckel när `-i2psam=` används, för att göra utgående och eventuellt inkommande anslutningar på I2P.
- `.cookie` innehåller en efemär RPC autentisering token (skapas vid uppstart, raderas vid nedstängning) när cookie-autentisering används. Detta kan t.ex. användas för att ansluta Wallet-programvara.
- `.lock` är datakataloglåset, som hindrar flera instanser från att skriva till samma datakatalog samtidigt.
- `guisettings.ini.bak` är den automatiska sparningen av GUI-inställningar (*Bitcoin Qt*) när alternativet `-resetguisettings` används.



Som vi såg i de första delarna av denna BTC 202-kurs är Bitcoin core både Bitcoin nodprogramvara och Wallet. Det är dock inte nödvändigtvis den lösning jag skulle rekommendera för att hantera dina plånböcker, eftersom dess Interface förblir grundläggande och dess funktioner är begränsade jämfört med modern programvara som Sparrow eller Liana. Core innehåller också filer för att hantera dina plånböcker:





- `wallets/` är standardkatalogen som är värd för en eller flera;
- `wallets/<name>/Wallet.dat` är SQLite-databasen för Wallet (nycklar, deskriptorer, transaktionsmetadata etc.);
- wallets/<name>/Wallet.dat-journal` är SQLite rollback-loggen.



Sammanfattningsvis är detta filstrukturen för Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Valideringsvägen för ett nytt block



Vid mottagandet av ett nytt block kontrollerar din nod Proof of Work och, mer allmänt, efterlevnaden av konsensusreglerna. Om allt är bra tillämpar den ändringarna transaktion för transaktion på sin UTXO-uppsättning: den kontrollerar att varje post spenderar befintliga UTXO:er med ett giltigt skript, tar bort dessa UTXO:er och lägger till de nya utgångarna. Om allt är giltigt överförs ändringarna till `chainstate/`.



Parallellt med detta skrivs ångerdata till `rev*.dat` och metadata till indexet `blocks/index/`. Blocket serialiseras sedan till rätt fil `blk*.dat`. I händelse av en omorganisation läser noden `rev*.dat` i omvänd ordning för att rent koppla bort de övergivna blocken, återställa UTXO-uppsättningen och sedan ansluta blocken i den nya bästa kedjan.





## Förståelse av Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Filen `Bitcoin.conf` är den huvudsakliga konfigurationsfilen för Interface för Bitcoin core. Den gör att du kan justera beteendet och parametrarna för din nod utan att behöva kompilera om källkoden eller göra ändringar i kommandoraden. Konkret är det en ren textfil som är strukturerad i nyckel-värde-par, vilket innebär att varje rad i filen refererar till en specifik parameter (nyckeln) och dess associerade värde, som kan ändras för att justera den parametern.



Parametrar för nätverk, transaktionsrelä, prestanda, indexering, loggning och RPC-åtkomst kan definieras i `Bitcoin.conf`. Den här konfigurationsfilen ändrar dock aldrig protokollets konsensusregler: den anger endast nodens lokala policy (vidarebefordringsregler), hur den ansluter, indexerar och exponerar tjänster.



### Plats och prioritet



Som standard finns `Bitcoin.conf` i Bitcoin core:s datakatalog. Detta är den berömda katalogen som vi nämnde i föregående kapitel. Den här filen skapas dock inte automatiskt av Bitcoin core, utom i vissa miljöer, till exempel Umbrel. Om den inte redan finns måste du generate skapa den själv genom att helt enkelt skapa en fil med namnet `Bitcoin.conf` och sedan öppna den i en textredigerare för att göra dina ändringar.



De parametrar som definieras i `Bitcoin.conf` kan åsidosättas av 2 lager:




- `settings.json` (skrivs dynamiskt av Interface grafik eller vissa RPC),
- och alternativ som ändras via kommandorader.



Observera att alla ändringar i `Bitcoin.conf` kräver en omstart av noden för att träda i kraft.



### Format och struktur



Formatet på `Bitcoin.conf` är därför mycket enkelt: en rad per alternativ, i formen `alternativ=värde`. Onödiga mellanslag och tomma rader ignoreras och kodkommentarer börjar med `#`.



Nästan alla booleska alternativ kan inaktiveras med prefixet `no`. Till exempel är `listen=0` och `nolisten=1` likvärdiga beroende på version.



Om du vill dela upp konfigurationen efter nätverk kan du använda sektioner: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternativt kan du prefixera namnet på alternativet med `regtest.maxmempool=100`.



### Vad Bitcoin.conf kan och inte kan göra



Som förklarats ovan är konsensusregler uppenbarligen inte konfigurerbara i `Bitcoin.conf`, eftersom detta skulle kunna skapa en Hard Fork. Å andra sidan är många andra aspekter konfigurerbara. Det finns 3 användbara klasser att hålla i minnet:




- Rent lokala parametrar. Dessa påverkar endast din nod: cachestorlek (`dbcache`), pruned-läge (`prune`), valfria index ... De påverkar din maskins prestanda, men inte nätverket.
- Policyer för reläer och Mempool. Dessa bestämmer vad din nod accepterar, behåller och vidarebefordrar före bekräftelse: lägsta avgiftströskel (`minrelaytxfee`), Mempool-storlek och lagringstid (`maxmempool`, `mempoolexpiry`), transaktionsersättning (RBF)... Dessa regler är inte en del av konsensus, så två olika noder kan ha olika policyer och ändå vara helt kompatibla. Å andra sidan kommer dessa parametrar att påverka Bitcoin-nätverket (vilket förklarades i den första delen, särskilt med perkolationsteorin).
- Nätverksanslutning. Dessa alternativ avgör hur noden hittar peers, lyssnar, passerar en NAT, använder Tor eller en proxy eller begränsar sin bandbredd. De formar din topologi, men ändrar inte vidarebefordran av transaktioner.



Det är viktigt att förstå denna åtskillnad: om en transaktion inte följer konsensusreglerna kommer din nod att avvisa den i vilket fall som helst. Men en striktare lokal policy kan vägra att vidarebefordra en transaktion som är giltig enligt konsensus.



### Nätverk och topologi



Först och främst är det viktigt att tydligt skilja mellan de två typer av anslutningar som en Bitcoin-nod kan ha:




- Utgående anslutningar, som initieras av vår nod till en annan nod;



![Image](assets/fr/106.webp)





- Inkommande anslutningar, initierade av en annan nod till vår.



![Image](assets/fr/107.webp)



Dessa två typer av anslutningar är fullt kapabla att utbyta samma data i båda riktningarna; det är inte en fråga om att begränsa flödesriktningen, utan bara om en skillnad i initieraren av anslutningen. Ur vår nods synvinkel anses utgående anslutningar i allmänhet vara säkrare, eftersom vi initierar dem och väljer exakt vilken nod vi ska ansluta till, vilket gör det osannolikt att anslutningen är skadlig. Som standard upprätthåller Bitcoin core 10 utgående anslutningar (8 "*full-relay*" + 2 "*block-relay-only*").



En Full node tillför mer värde till nätverket genom att acceptera inkommande anslutningar. Parametern `listen=1` gör det möjligt att lyssna på standardporten 8333 i nätverket i fråga, vilket gör att dessa inkommande anslutningar kan tas emot på clearnet. För att detta ska fungera måste den här porten också vara öppen på din router. Om den inte är det kommer din nod att fortsätta att fungera med endast utgående anslutningar, vilket inte kommer att påverka din personliga användning av Bitcoin. Valet om att tillåta inkommande anslutningar är ditt, det finns inget "bästa val"



Om du föredrar att inte öppna en port på din router, men ändå acceptera inkommande anslutningar, kan du aktivera parametern `listenonion=1`. Detta kommer att uppnå samma resultat, men bara genom Tor-nätverket snarare än clearnet.



På nätverksnivå har vi också:




- `addnode`: lägger till en vänlig kollega att kontakta utöver den vanliga upptäckten (kan anges flera gånger).
- connect`: begränsar strikt anslutningar till den Address som tillhandahålls (kan anges flera gånger). Kärnan kommer inte att ansluta till någon annan nod.
- `seednode`: används endast för att fylla i boken-Address när du ansluter till en nod och sedan kopplar bort.
- `maxconnections`: definierar det globala taket för inkommande + utgående anslutningar. Som standard är denna parameter inställd på 125, vilket innebär att din nod aldrig kommer att acceptera fler än 125 anslutningar.
- maxuploadtarget`: begränsar uppladdningar för att begränsa bandbredden under ett glidande 24-timmarsfönster. Detta tak offrar inte spridningen av viktiga nya Elements.
- `onlynet`: begränsar utgående anslutningar till endast utvalda nätverk (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Om du t.ex. vill att din nod endast ska ansluta till Bitcoin-nätverket via Tor kan du aktivera parametern `onlynet=onion` och inaktivera inkommande anslutningar (eller endast tillåta anslutningar via Tor också).
- `dnsseed`: tillåter eller förbjuder _DNS seeds_ att begära peers när din lokala Address-pool är låg (standard: `1`, om inte `-connect` eller `-maxconnections=0`).
- `forcednsseed`: tvingar _DNS seeds_ att begäras vid start, även om du redan har adresser i lager (standard: `0`).
- `fixedseeds`: Tillåt användning av *seed-noder* (hårdkodad Address-lista) om _DNS seeds_ misslyckas eller är inaktiverade (standard: `1`).
- `dns`: Godkänner DNS-upplösningar i allmänhet (t.ex. för `-addnode`/`-seednode`/`-connect`).



Som standard kommunicerar din nod över clearnet, Tor och I2P. Detta innebär att de peers som den ansluter till på clearnet kan se din offentliga IP Address, och din internetleverantör kommer sannolikt att kunna upptäcka att du kör en Bitcoin-nod (även om P2P Transport V2 gör det svårare för en internetleverantör att avlyssna). Det här är inte nödvändigtvis ett problem, men om du vill undvika att den här informationen läcker ut kan du ansluta din nod uteslutande via Tor-nätverket.



För att vara helt Tor-aktiverad måste du tvinga Bitcoin core att endast använda detta nätverk och att skapa en dold tjänst för inkommande anslutningar (om du vill aktivera dem). I `Bitcoin.conf` måste du lägga till den här konfigurationen:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `lyssna=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Alla dina P2P-anslutningar går genom Tor. Din nod tar emot en `.onion` Address för inkommande anslutningar, så inga portar behöver öppnas på routern. Din internetleverantör ser bara Tor-trafik och dina kollegor är omedvetna om din faktiska offentliga IP Address.



För att undvika DNS-upplösning i klartext kan du lägga till `dnsseed=0` och `dns=0` i din konfiguration. Du måste sedan manuellt tillhandahålla `.onion'-peers via `seednode=` eller `addnode=`, eftersom det annars kommer att vara svårt att upptäcka nya noder.



Om du är nybörjare skulle jag naturligtvis råda dig att låta alla dessa nätverksinställningar vara för tillfället. Standardkonfigurationen är ofta tillräcklig.



### Mempool och reläpolicy



#### Grundläggande parametrar



Här är de grundläggande parametrarna som du kan ändra i din `Bitcoin.conf` när det gäller hanteringen av din Mempool och vidarebefordran av obekräftade transaktioner:





- `maxmempool=<n>`: Begränsar den maximala storleken på den lokala Mempool till `<n>` megabyte (standard: `300`). När gränsen nås höjer noden dynamiskt sin effektiva avgiftströskel och prioriterar de minst lönsamma transaktionerna (baserat på avgiftssatsen, inte det absoluta värdet) för att hålla sig under gränsen. Du kan lämna den här inställningen som standard. Att öka den kan vara användbart om du är Mining solo, eller om du vill få en mer exakt bild av Mempool överbelastning och förbättra avgiftsberäkningen. Omvänt kommer en minskning att spara RAM-minne och, i mindre utsträckning, andra systemresurser.





- `mempoolexpiry=<n>`: Maximal lagringstid för obekräftade transaktioner i Mempool (i timmar, standard: `336`). Efter denna tid tas transaktioner bort även om utrymme fortfarande finns tillgängligt.





- `persistmempool=1`: Sparar en ögonblicksbild av Mempool vid stillastående och laddar om den vid omstart (standard: `1`). Detta påskyndar återhämtningen efter omstart och gör att du inte behöver lära dig tillståndet på nytt via nätverket.





- `maxorphantx=<n>`: Maximalt antal orphan-transaktioner som behålls (beroende på input från UTXO:er som ännu inte setts i UTXO-uppsättningen, standard: `100`). Över detta tröskelvärde raderas de äldsta transaktionerna för att undvika okontrollerad tillväxt av cacheminnet.





- blocksonly=1`: Avaktiverar godkännande och återsändning av obekräftade transaktioner som tas emot från peers (om inte särskilda behörigheter beviljas). Noden laddar nu bara upp och annonserar block. Transaktioner som skapas lokalt kan fortfarande sändas (för att använda din nod med din Wallet-programvara). Detta minskar kraftigt kraven på bandbredd och RAM-minne, om än på bekostnad av minskad användbarhet för reläet och total obekantskap med Mempool.





- `minrelaytxfee=<n>`: Minsta avgiftssats (i BTC/kvB) under vilken transaktioner inte accepteras i nodens Mempool och inte vidarebefordras till peers (standard: `0,00001` = 1 sat/vB). Ju högre detta värde är, desto mer aggressivt filtrerar din nod lågkostnadstransaktioner.





- `mempoolfullrbf=1`: Acceptera RBF-transaktioner även utan uttrycklig RBF-signalering i den ersatta transaktionen. Med denna "*full-RBF*"-policy kan en transaktion som erbjuder en högre avgiftssats ersätta en annan i Mempool om de andra ersättningsvillkoren är uppfyllda.



Som en påminnelse är RBF en transaktionsmekanism som gör det möjligt för avsändaren att ersätta en transaktion med en som har högre avgifter för att påskynda bekräftelsen. Om en transaktion med för låg avgift förblir blockerad kan avsändaren använda *Replace-by-fee* för att höja avgiften och prioritera sin ersättningstransaktion i mempools och hos miners.



#### Avancerade och specifika inställningar



Här är de avancerade inställningarna för Mempool och reläpolicy. Om du är nybörjare behöver du inte ändra de här inställningarna:





- datacarrier=1`: Tillåter vidarebefordran och (om Mining via nod) inkludering av transaktioner som innehåller icke-finansiella data via en `OP_RETURN`-utgång (standard: `1`). Om du avaktiverar denna parameter minskar ytan för spam med icke-finansiella data något, till priset av minskad kompatibilitet med vissa användningsområden. I samtliga fall måste du acceptera minerad `OP_RETURN`.





- `datacarriersize=<n>`: Maximal storlek (i byte) på den `OP_RETURN` som noden vidarebefordrar (standard: `83`). Om du sänker detta värde begränsas nyttolasten som transporteras via `OP_RETURN`. Observera att denna gräns kommer att tas bort som standard i en framtida version av Bitcoin core.





- `bytespersigop=<n>`: Parameter som omvandlar signaturtransaktioner till motsvarande bytes för utvärdering av relägränser (standard: `20`). Detta kommer att påverka godkännandet av transaktioner med `sigops` enligt lokala policyregler.





- `permitbaremultisig=1`: Tillåter vidarebefordran av *bara-Multisig* P2MS-transaktioner (standard: `1`). Detta är den äldsta skriptmallen för att upprätta multisignaturvillkor på en UTXO (uppfanns 2011 av Gavin Andresen).





- `whitelistrelay=1`: Ger automatiskt reläbehörighet till inkommande peers på vitlistan (standard: `1`). Dessa peers får sina transaktioner accepterade av reläet även om din nod inte är i allmänt reläläge.





- `whitelistforcerelay=1`: Tilldelar behörigheten "*forcerelay*" till vitlistade peers med standardbehörigheter (standard: `0`). Noden vidarebefordrar sedan deras transaktioner även om de redan finns i Mempool, och kringgår därmed mekanismerna för anti-redundans.





- `whitebind=<[behörigheter@]addr>` / `whitelist=<[behörigheter@]CIDR>`: Binder ett Interface- eller Address-område och tilldelar finkorniga behörigheter till motsvarande peers: `relay`, `forcerelay`, `Mempool` (Mempool innehållsbegäran), `noban`, `download`, `addr`, `bloomfilter`. Detta kan vara användbart för att bevilja privilegierad behandling till betrodda peers (t.ex. gateways, LAN och interna tjänster).





- peerbloomfilters=1`: Aktivera stöd för Bloom-filter (BIP37) för att servera filtrerade block/transaktioner till tunna klienter (standard: `0`). Varning: detta ökar belastningen på dina resurser.





- peerblockfilters=1`: Serverar kompaktfilter för BIP157 (*Neutrino*) till peers (standard: `0`).





- `blockreconstructionextratxn=<n>`: Ytterligare antal transaktioner som behålls i minnet för att bygga om kompakta block (standard: `100`). Förbättrar möjligheterna att lyckas med rekonstruktioner under synkroniseringar av kompakta block, på bekostnad av lite minne.



Som en påminnelse har alla dessa reläregler ingen inverkan på giltigheten av transaktioner som ingår i ett giltigt block. De tjänar till att justera ditt bidrag till reläet, skydda dina resurser och göra din nod förutsägbar i begränsade miljöer, men ger dig aldrig möjlighet att vägra block som respekterar konsensusreglerna.



### Plånböcker



Du kan också justera hur dina plånböcker ska hanteras i filen `Bitcoin.conf`. Om du inte använder Wallet direkt i Core, utan snarare extern hanteringsprogramvara som Sparrow eller Liana, kommer dessa parametrar att vara av liten betydelse:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Definierar formatet för Wallet-genererade adresser för mottagning.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Tvinga fram Exchange Address-format (återstoden av en inmatning på en enda betalning).





- `Wallet=<väg>`: Laddar en befintlig Wallet vid start (kan upprepas för att ladda flera plånböcker).





- `walletdir=<dir>`: Katalog som innehåller plånböcker (standard: `<datadir>/wallets` om den finns, annars `<datadir>`). Detta kan vara användbart om du vill lagra plånböcker på en dedikerad eller krypterad volym.





- `walletbroadcast=1`: Sänder automatiskt transaktioner som skapats av laddade plånböcker (standard: `1`). Ställ in till "0" om du vill hantera sändning via en annan kanal.





- `walletrbf=1`: Aktiverar RBF opt-in för att signalera RBF på alla transaktioner (standard: `1`). Gör att du kan höja avgifterna senare i händelse av en blockerad transaktion.





- `txconfirmtarget=<n>`: Mål för bekräftelse av transaktionen (i antal block, standard: `6`). Wallet kommer automatiskt att ställa in avgiften för transaktionen så att den bekräftas inom detta antal block.





- `paytxfee=<amt>`: Fast avgiftssats (BTC/kvB) som tillämpas på Wallet-transaktioner. Undvik i allmänhet: använd adaptiv uppskattning via `txconfirmtarget`.





- fallbackfee=<amt>`: Reservränta (BTC/kvB) som används om estimatorn får slut på data (standard: `0.00`). Om den sätts till 0 inaktiveras fallback helt.





- `mintxfee=<amt>`: Minsta tröskel (BTC/kvB) för att Wallet ska skapa transaktioner (standard: `0,00001`). Wallet kommer att vägra att skapa en transaktion under detta tröskelvärde.





- `maxtxfee=<amt>`: Absolut tak på totala avgifter för en Wallet-transaktion (standard: `0,10` BTC). Skyddar mot onormalt höga avgifter som i onödan skulle förstöra bitcoins.





- `avoidpartialspends=1`: Väljer UTXO:er efter Address-kluster för att undvika partiella utgifter.





- `spendzeroconfchange=1`: Tillåter att en obekräftad UTXO Exchange återanvänds som en post i en ny transaktion (standard: `1`).





- `consolidatefeerate=<amt>`: Maximal hastighet (BTC/kvB) bortom vilken Wallet undviker att lägga till fler insatsvaror än nödvändigt för att konsolidera. Detta möjliggör opportunistiska konsolideringar till låga priser och minskar kostnaderna när kostnaderna är höga.





- `maxapsfee=<n>`: Budget för ytterligare avgifter (BTC, absolut värde) som Wallet samtycker till att betala för att aktivera alternativet "*avoid partial spends*".





- `discardfee=<amt>`: Pris (BTC/kvB) som anger din tolerans att kasta bort Exchange genom att lägga till det till avgiften. Utgångar som skulle kosta mer än en tredjedel av sitt värde med denna avgift slopas.





- `keypool=<n>`: Storlek på den förgenererade Address-poolen (standard: `1000`). Om värdena är för små ökar risken för ofullständiga återställningar.





- `disablewallet=1`: Startar Bitcoin core utan delsystemet Wallet och inaktiverar tillhörande RPC:er. Minskar attackytan och fotavtrycket om noden endast används för validering/release.



### Lagring, indexering och prestanda



Med konfigurationsfilen kan du också justera parametrarna för din maskin. Detta kan vara särskilt relevant om du har begränsade resurser eller, tvärtom, en stor mängd tillgänglig kapacitet:





- `datadir=<dir>`: Ställer in Bitcoin core:s huvuddatakatalog.





- `blocksdir=<dir>`: Kopplar bort platsen för blockfilerna (`blocks/blk*.dat` och `blocks/rev*.dat`) från `datadir`. Detta kan vara användbart för att placera blockarkivet på en annan volym, medan tillståndsbasen (`chainstate/`) behålls på ett snabbare medium, till exempel.





- `dbcache=<n>`: Tilldelar `<n>` MiB till databascachen (*LevelDB*) som används av blockindexet och `chainstate` (standard: `450`). Ju högre värde, desto snabbare IBD och aktuell validering, på bekostnad av högre RAM-förbrukning.





- `prune=<n>`: Aktiverar beskärning av blockfiler och anger ett mål för diskutrymme i MiB (standard: `0` = inaktiverad; `1` = manuell beskärning via RPC; `>=550` = automatisk beskärning under målet). Inkompatibel med `txindex=1`. Noden förblir en fullt validerande nod, men kan inte längre tillhandahålla den gamla historiken. Det här alternativet är särskilt användbart om du har begränsat diskutrymme, t.ex. när du installerar en nod på din hemdator.





- txindex=1`: Skapar och underhåller ett globalt index över bekräftade transaktioner. Väsentligt för vissa frågor (`getrawtransaction` ej Wallet) och för utforskningsändamål, men ökar diskavtrycket avsevärt. Inkompatibel med pruned-läget.





- `assumevalid=<hex>`: Anger ett block som antas vara giltigt, vilket gör att du kan hoppa över skriptkontroller för dess förfäder (ange `0` för att kontrollera allt). Se föregående kapitel för mer information.





- `reindex=1`: Rekonstruerar blockindex och tillstånd (`chainstate`) från `blk*.dat`-filer på disken. Återskapar även valfria aktiva index. Det här är en tidskrävande operation som kan användas för att reparera en skadad databas eller för att aktivera/avaktivera tunga index på ett rent sätt.





- `reindex-kedjestatus=1`: Återskapar endast `chainstate` från det aktuella blockindexet. Föredras när blockfilerna är friska.





- `blockfilterindex=<typ>`: Underhåller index för kompakta blockfilter (t.ex. `basic`) som används av tunna klienter (BIP157/158) och vissa RPC:er. Inaktiverad som standard (`0`). Förbrukar extra diskutrymme och indexeringstid.





- `coinstatsindex=1`: Upprätthåller ett UTXO-statistikindex som drivs av anropet `gettxoutsetinfo`. Användbart för revisioner och mätvärden, vilket eliminerar behovet av kostsam omräkning. Inaktiverad som standard.





- `loadblock=<fil>`: Importerar block vid start från en extern fil `blk*.dat`. Används för att ladda historik från en offline-källa (lokal kopia, extern media) för att snabba upp initieringen.





- `par=<n>`: Ställer in antalet trådar för skriptverifiering (från `-10` till `15`, `0` = auto, `<0` = lämnar detta antal kärnor lediga). Gör att du kan justera CPU-parallellismen under valideringen. Autoläget är lämpligt i de flesta fall.





- `debuglogfile=<file>`: Anger platsen för loggen `debug.log`.





- `shrinkdebugfile=1`: Minskar storleken på `debug.log` vid uppstart (standard: `1` när `debug` inte är aktiv).





- `settings=<file>`: Sökväg till dynamisk inställningsfil `settings.json`.



### RPC tillträde och driftsäkerhet



Slutligen kan du i filen `Bitcoin.conf` även konfigurera åtkomstparametrarna för din nod. Var försiktig med dessa inställningar, särskilt om du precis har börjat: undvik att ändra dem utan en grundlig förståelse av konsekvenserna, eftersom detta kan införa sårbarheter.





- `server=1`: Aktiverar JSON-RPC-servern. Viktigt om du kör `bitcoind` via `bitcoin-cli` eller en tredjepartsapplikation. Avaktivera (`0`) på en ren valideringsnod som inte exponerar något API, eller redan använder en Electrum-server.





- `rpcbind=<addr>[:port]`: RPC-server lyssnar Address/port. Som standard sker lyssnandet endast lokalt (`127.0.0.1` och `::1`). Denna parameter ignoreras om inte `rpcallowip` också är definierad. Använd den för att uttryckligen begränsa Interface.





- `rpcport=<port>`: RPC-port (standard: `8332` på Mainnet, `18332` på Testnet, `38332` på bookmark, `18443` på regtest).





- `rpcallowip=<ip|cidr>`: Tillåter RPC-klienter från en given IP eller subnät (kan upprepas). Används tillsammans med `rpcbind` för att exponera API:et endast för ett betrott segment (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Rekommenderad RPC-autentiseringsmetod (hashat lösenord). Tillåter flera poster och undviker att lagra en hemlighet i klartext.





- `rpccookiefile=<stig>`: Sökväg till autentiseringscookien (standard: filen `.cookie` under `datadir/`). Detta används för lokal åtkomst av samma användare utan att hantera permanenta lösenord. Du kan t.ex. använda den för att ansluta Liana Wallet till din Bitcoin core på samma maskin.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Klassisk RPC-autentisering med lösenord i klartext. Undvik att använda detta till förmån för `rpcauth` eller en cookie.





- `rpcthreads=<n>`: Antal trådar som ska betjäna RPC-anrop (standard: `4`). Öka det om du har höga anropstoppar på övervakningssidan/externa verktyg.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Vitlista med auktoriserade API:er. Minskar attackytan genom att begränsa tillgängliga metoder.





- `rpcwhitelistdefault=1|0`: Standardbeteende för vitlista: om den är aktiverad och en vitlista används, nekas olistade samtal. Detta kan också tvinga fram en tom standarduppsättning (inga samtal tillåts) så länge inget uttryckligen listas.





- `rest=1`: Aktivera offentligt REST API (inaktiverat som standard). Ska endast exponeras på ett betrott nätverk (samma försiktighet som med JSON-RPC).





- `conf=<fil>`: Anger, endast på kommandoraden, en skrivskyddad konfigurationsfil. Användbar för att frysa en körprofil (oföränderlig) på ops-sidan.





- `includeconf=<fil>`: Läser in ytterligare en konfigurationsfil (sökväg i förhållande till `datadir/`). Tillåter åtskillnad av roller: gemensam bas + känslig lokal överbelastning.





- `daemon=1` / `daemonwait=1`: Startar `bitcoind` i bakgrunden och, med `daemonwait`, väntar på att initialiseringen ska slutföras innan den överlämnas. Detta underlättar integration med övervakare (systemd, runit).





- `pid=<fil>`: Plats för PID-fil.





- `sandbox=<log-and-abort|abort>`: Aktiverar sandboxning av experimentella syscalls: endast förväntade syscalls tillåts.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Utför ett kommando vid uppstart eller nedstängning.





- `alertnotify=<cmd>`: Utlöser ett kommando vid mottagande av en avisering.





- `blocknotify=<cmd>`: Exekverar ett kommando för varje nytt block.





- `debug=<category>|1` / `debugexclude=<category>`: Aktiverar/avaktiverar detaljerade loggkategorier (t.ex. `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Loggar IP-adresser.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Lägger till källplatser, trådnamn och exakta tidsstämplar i loggarna.





- `printtoconsole=1`: Skickar spår/debuggar till konsolen (*stdout*).





- `help-debug=1`: Visar hjälp för debug-alternativet och avslutar.





- `uacomment=<cmt>`: Lägger till en kommentar till User-Agent P2P.



Vi är nu färdiga med att lista de flesta konfigurationsparametrarna. Denna fil `Bitcoin.conf` utgör således den verkliga instrumentpanelen för din nod: den definierar nätverkskonfiguration, Mempool-hantering, disk- och minnesanvändning, indexering och allmän administration. Om du vill lära dig mer om den här filen och skapa en som är skräddarsydd efter dina behov rekommenderar jag att du använder [Jameson Lopps generator] (https://jlopp.github.io/Bitcoin-core-config-generator/).



Vi har nått slutet av denna BTC 202-kurs, som kommer att ha gjort det möjligt för dig att inte bara förstå grunderna i hur noder fungerar och hur de interagerar inom systemet, utan också att skapa din egen. Du är nu en suverän Bitcoiner, med din egen självförvarare Wallet, som sänder dina transaktioner via din egen nod. Vi gratulerar dig!



Du kan nu gå vidare till den sista delen av kursen, där du kommer att kunna utvärdera BTC 202 och sedan ta ditt diplom för att kontrollera att du behärskar alla begrepp som omfattas.



Du har nu flera alternativ öppna för dig. Nästa logiska steg är att sätta upp din egen Lightning-nod, så att du kan vara helt oberoende för dina off-chain-transaktioner. Detta kommer att bli föremål för en kommande kurs, som kommer att publiceras i höst 2025 på Plan ₿ Network.



Under tiden inbjuder jag dig att upptäcka BTC 204-utbildningen, som gör det möjligt för dig att förstå och behärska principerna för integritetsskydd i din användning av Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Sista delen


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Recensioner & betyg


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Slutlig examination


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Slutsats


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>