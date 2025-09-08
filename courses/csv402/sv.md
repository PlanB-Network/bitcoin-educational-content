---
name: RGB-protokollet, från teori till praktik
goal: Förvärva de färdigheter som krävs för att förstå och använda RGB
objectives: 

  - Förstå de grundläggande begreppen i RGB-protokollet
  - Behärska principerna för Client-side Validation- och Bitcoin-åtaganden
  - Lär dig hur du skapar, hanterar och överför RGB-kontrakt
  - Hur man använder en RGB-kompatibel Lightning-nod


---
# Upptäcka RGB-protokollet


Dyk in i världen av RGB, ett protokoll som är utformat för att implementera och genomdriva digitala rättigheter, i form av kontrakt och tillgångar, baserat på konsensusreglerna och verksamheten i Bitcoin Blockchain. Denna omfattande utbildningskurs guidar dig genom de tekniska och praktiska grunderna för RGB, från begreppen "Client-side Validation" och "Single-use Seals" till implementeringen av avancerade smarta kontrakt.


Genom ett strukturerat steg-för-steg-program kommer du att upptäcka mekanismerna i Client-side Validation, deterministiska åtaganden på Bitcoin och interaktionsmönster mellan användare. Lär dig hur du skapar, hanterar och överför RGB-tokens på Bitcoin eller Lightning Network.


Oavsett om du är utvecklare, Bitcoin-entusiast eller bara nyfiken på att lära dig mer om den här tekniken kommer den här kursen att ge dig de verktyg och kunskaper du behöver för att bemästra RGB och bygga innovativa lösningar på Bitcoin.


Kursen är baserad på ett liveseminarium som anordnas av Fulgur'Ventures och undervisas av tre välkända lärare och RGB-experter.


+++
# Inledning


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## Presentation av kursen


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


Hej och välkommen till denna utbildning om RGB, ett validerat Smart contract-system på klientsidan som körs på Bitcoin och Lightning Network. Kursens struktur är utformad för att möjliggöra en djupgående utforskning av detta komplexa ämne. Här är hur kursen är organiserad:


**Avsnitt 1: Teori**


Det första avsnittet ägnas åt de teoretiska begrepp som behövs för att förstå grunderna i Client-side Validation och RGB. Som du kommer att upptäcka i den här kursen introducerar RGB en mängd tekniska koncept som vanligtvis inte ses i Bitcoin. I det här avsnittet hittar du också en ordlista med definitioner av alla termer som är specifika för RGB-protokollet.


**Avsnitt 2: Övning**


Det andra avsnittet kommer att fokusera på tillämpningen av de teoretiska begrepp som ses i avsnitt 1. Vi lär oss hur man skapar och manipulerar RGB-kontrakt. Vi kommer också att se hur man programmerar med dessa verktyg. Dessa två första avsnitt presenteras av Maxim Orlovsky.


**Avsnitt 3: Tillämpningar**


Det sista avsnittet leds av andra talare som presenterar konkreta RGB-baserade applikationer för att belysa verkliga användningsfall.


---
Denna utbildningskurs växte ursprungligen fram ur ett tvåveckors bootcamp för avancerad utveckling i Viareggio, Toscana, organiserat av [Fulgur'Ventures] (https://fulgur.ventures/). Den första veckan, som fokuserade på Rust och SDK:er, finns i denna andra kurs:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

I den här kursen fokuserar vi på den andra veckan i bootcampen, som fokuserar på RGB.


**Vecka 1 - LNP402:**


![RGB-Bitcoin](assets/fr/001.webp)


**Vecka 2 - Aktuell utbildning CSV402:**


![RGB-Bitcoin](assets/fr/002.webp)


Stort tack till arrangörerna av dessa livekurser och till de 3 lärare som deltog:




- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotteknik, transhumanism. Skapare av RGB, Prime, Radiant och lnp_bp, mycitadel_io & cyphernet_io*;
- Hunter Trujilo: *Utvecklare, Rust, Bitcoin, Lightning, RGB*;
- Federico Tenga: *Jag gör mitt för att förvandla världen till en Cypherpunk-dystopi. Arbetar för närvarande med RGB på Bitfinex*.


Den skriftliga versionen av denna utbildning har utarbetats med hjälp av två huvudresurser:




- Videor från Maxim Orlovsky, Hunter Trujilo och Frederico Tengas seminarium på Lightning Bootcamp;
- RGB-dokumentationen, vars produktion sponsrades av [Bitfinex] (https://www.bitfinex.com/).


Är du redo att dyka in i den komplexa och fascinerande världen av RGB? Då kör vi!


# RGB i teorin


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## Introduktion till koncept för distribuerade datorsystem


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB är ett protokoll som är utformat för att tillämpa och genomdriva digitala rättigheter (i form av avtal och tillgångar) på ett skalbart och konfidentiellt sätt, baserat på konsensusreglerna och verksamheten i Bitcoin Blockchain. Syftet med detta första kapitel är att presentera de grundläggande begreppen och terminologin kring RGB-protokollet, och särskilt belysa dess nära kopplingar till grundläggande distribuerade datorkoncept som Client-side Validation och Single-use Seals.


I det här kapitlet utforskar vi grunderna i **distribuerade konsensussystem** och ser hur RGB passar in i denna familj av tekniker. Vi introducerar också huvudprinciperna som hjälper oss att förstå varför RGB strävar efter att vara utbyggbar och oberoende av Bitcoin:s egen konsensusmekanism, samtidigt som den förlitar sig på den när det behövs.


### Inledning


Distributed computing, en särskild gren inom datavetenskapen, studerar de protokoll som används för att cirkulera och bearbeta information i ett nätverk av noder. Tillsammans utgör dessa noder och protokollreglerna det som kallas ett distribuerat system. Bland de väsentliga egenskaper som kännetecknar ett sådant system finns några:




- Möjligheten till oberoende verifiering och validering** av vissa data av varje nod;
- Möjligheten för noder att (beroende på protokoll) skapa en fullständig eller partiell bild av informationen. Dessa vyer är **tillstånden** i det distribuerade systemet;
- Den **kronologiska ordningen** av operationer, så att data är tillförlitligt tidsstämplade och det finns ett samförstånd om sekvensen av händelser (sekvens av tillstånd).


Begreppet **konsensus** i ett distribuerat system omfattar framför allt två aspekter:




- Erkännande av giltigheten** av tillståndsändringar (enligt protokollregler);
- Överenskommelsen om ordningen** på dessa tillståndsändringar, vilket gör det omöjligt att skriva om eller vända validerade operationer i efterhand (detta kallas också "double-spend protection" i Bitcoin).


Den första funktionella, behörighetsfria implementeringen av en distribuerad konsensusmekanism introducerades av Satoshi Nakamoto med Bitcoin, tack vare den kombinerade användningen av en Blockchain-datastruktur och en Proof-of-Work (PoW)-algoritm. I det här systemet beror blockhistorikens trovärdighet på den datorkraft som noderna (miners) ägnar åt den. Bitcoin är därför ett viktigt och historiskt exempel på ett distribuerat konsensussystem som är öppet för alla (*permissionless*).


I världen av Blockchain och distribuerade datorsystem kan vi urskilja två grundläggande paradigm: ***Blockchain*** i traditionell mening och ***statskanaler***, där det bästa exemplet i produktion är Lightning Network. Blockchain definieras som ett register över kronologiskt ordnade händelser, replikerade genom konsensus inom ett öppet, tillståndsfritt nätverk. State channels, å andra sidan, är peer-to-peer-kanaler som gör det möjligt för två (eller fler) deltagare att upprätthålla ett uppdaterat tillstånd off-chain, med användning av Blockchain endast när dessa kanaler öppnas och stängs.


I samband med Bitcoin är du utan tvekan bekant med principerna för Mining, decentralisering och slutgiltighet av transaktioner på Blockchain, samt hur betalningskanaler fungerar. Med RGB introducerar vi ett nytt paradigm som kallas **Client-side Validation**, som till skillnad från Blockchain eller Lightning består i att lokalt (på klientsidan) lagra och validera tillståndsövergångarna för en Smart contract. Detta skiljer sig också från andra "DeFi-tekniker" (_rollups_, _plasma_, _ARK_, etc.), där Client-side Validation förlitar sig på Blockchain för att förhindra Double-spending och för att ha ett tidsstämplingssystem, samtidigt som registret över off-chain-tillstånd och -övergångar endast hålls tillgängligt för de berörda deltagarna.


![RGB-Bitcoin](assets/fr/003.webp)


Senare kommer vi också att introducera en viktig term: begreppet "**Stash**", som hänvisar till den uppsättning data på klientsidan som krävs för att bevara tillståndet för en Contract, eftersom dessa data inte replikeras globalt över nätverket. Slutligen tittar vi på tanken bakom RGB, ett protokoll som drar nytta av Client-side Validation, och varför det kompletterar befintliga metoder (Blockchain och tillståndskanaler).


### Trilemman i distribuerade datorsystem


För att förstå hur Client-side Validation och RGB Address problem inte löstes av Blockchain och Lightning, låt oss upptäcka 3 stora "trilemman" inom distribuerad databehandling:




- Skalbarhet, decentralisering, integritet**;
- CAP**-teoremet (konsistens, tillgänglighet, tolerans mot partitionering);
- CIA**-trilemmat (konfidentialitet, integritet, tillgänglighet).


#### 1. Skalbarhet, decentralisering och sekretess




- Blockchain (Bitcoin)**


Blockchain är mycket decentraliserat, men inte särskilt skalbart. Eftersom allt finns i ett globalt, offentligt register är dessutom sekretessen begränsad. Vi kan försöka förbättra sekretessen med nollkunskapstekniker (Confidential Transactions, mimblewimble-system etc.), men den offentliga kedjan kan inte dölja transaktionsgrafen.




- Blixtnedslag/Statskanaler**


Statliga kanaler (som med Lightning Network) är mer skalbara och mer privata än Blockchain, eftersom transaktioner sker off-chain. Skyldigheten att offentligt tillkännage vissa Elements (finansieringstransaktioner, nätverkstopologi) och övervakningen av nätverkstrafiken kan dock delvis äventyra sekretessen. Decentraliseringen blir också lidande: routing är kontantintensivt och större noder kan bli centraliseringspunkter. Det är just detta fenomen vi börjar se på Lightning.




- Client-side Validation (RGB)**


Det här nya paradigmet är ännu mer skalbart och mer konfidentiellt, eftersom vi inte bara kan integrera tekniker för proof-of-knowledge med nollavslöjande, utan det finns inte heller någon global graf över transaktioner, eftersom ingen har hela registret. Å andra sidan innebär det också en viss kompromiss när det gäller decentralisering: utfärdaren av en Smart contract kan ha en central roll (som en "Contract deployer" i Ethereum). Men till skillnad från Blockchain lagrar och validerar du med Client-side Validation bara de kontrakt du är intresserad av, vilket förbättrar skalbarheten genom att du slipper ladda ner och verifiera alla befintliga tillstånd.


![RGB-Bitcoin](assets/fr/004.webp)


#### 2. CAP-teoremet (Konsistens, Tillgänglighet, Partitionstolerans)


CAP-teoremet understryker att det är omöjligt för ett distribuerat system att samtidigt uppfylla *Konsistens*, *Tillgänglighet* och *Partitionstolerans*.




- Blockchain**


Blockchain gynnar konsekvens och tillgänglighet, men fungerar inte så bra med nätverksuppdelning: om du inte kan se ett block kan du inte agera och ha samma vy som hela nätverket.




- Blixten**


Ett system med statskanaler har tillgänglighets- och partitioneringstolerans (eftersom två noder kan förbli anslutna till varandra även om nätverket är fragmenterat), men den övergripande konsistensen beror på öppning och stängning av kanaler på Blockchain.




- Client-side Validation (RGB)**


Ett system som RGB erbjuder konsistens (varje deltagare validerar sina data lokalt, utan tvetydighet) och partitioneringstolerans (du behåller dina data självständigt), men garanterar inte global tillgänglighet (alla måste se till att de har de relevanta delarna av historien, och vissa deltagare kanske inte publicerar någonting eller slutar dela viss information).


![RGB-Bitcoin](assets/fr/005.webp)


#### 3. CIA-trilemmat (konfidentialitet, integritet, tillgänglighet)


Detta trilemma påminner oss om att konfidentialitet, integritet och tillgänglighet inte alla kan optimeras samtidigt. Blockchain, Lightning och Client-side Validation faller på olika sätt in i denna balans. Tanken är att inget enskilt system kan erbjuda allt; det är nödvändigt att kombinera flera metoder (Blockchain:s tidsstämpling, Lightnings synkrona metod och lokal validering med RGB) för att få ett sammanhängande paket som ger goda garantier i varje dimension.


![RGB-Bitcoin](assets/fr/006.webp)


### Blockchain:s roll och begreppet sharding


Blockchain (i det här fallet Bitcoin) fungerar främst som en mekanism för _tidsstämpling_ och skydd mot dubbla utgifter. Istället för att infoga fullständiga data från ett Smart contract eller decentraliserat system, inkluderar vi helt enkelt **kryptografiska åtaganden** för transaktioner (i den mening som avses i Client-side Validation, som vi kallar "tillståndsövergångar"). På detta sätt:




- Vi befriar Blockchain från en stor mängd data och logik;
- Varje användare lagrar endast den historik som krävs för den egna delen av Contract (hans "*Shard*"), i stället för att replikera Global State.


Sharding är ett koncept som har sitt ursprung i distribuerade databaser (t.ex. MySQL för sociala nätverk som Facebook eller Twitter). För att lösa problemet med datavolym och synkroniseringsfördröjningar segmenteras databasen i _shards_ (USA, Europa, Asien etc.). Varje segment är lokalt konsekvent och endast delvis synkroniserat med de andra.


För smarta kontrakt av typen RGB använder vi Shard enligt själva kontrakten. Varje Contract är en oberoende _shard_. Om du till exempel bara håller USDT-tokens behöver du inte lagra eller validera hela historiken för en annan token som USDC. På Bitcoin gör Blockchain inte _sharding_: du har en global uppsättning UTXO:er. Med Client-side Validation behåller varje deltagare endast de Contract-data som den innehar eller använder.


Vi kan därför föreställa oss ekosystemet på följande sätt:




- Blockchain (Bitcoin)** som en grund som säkerställer fullständig replikering av ett minimalt register och fungerar som en tidsstämpel Layer;
- Lightning Network** for fast, Confidential Transactions, fortfarande baserat på säkerheten och den slutliga regleringen av Bitcoin Blockchain;
- RGB och Client-side Validation** för att lägga till mer komplex Smart contract-logik, utan att Blockchain blir överflödig eller förlorar konfidentialitet.


![RGB-Bitcoin](assets/fr/007.webp)


Dessa tre Elements bildar en triangulär helhet, snarare än en linjär stapel med "Layer 2", "Layer 3" och så vidare. Lightning kan ansluta direkt till Bitcoin eller vara associerad med Bitcoin-transaktioner som innehåller RGB-data. På samma sätt kan en "BiFi" (finans på Bitcoin) kombineras med Blockchain, med Lightning och med RGB beroende på behov av sekretess, skalbarhet eller Contract-logik.


![RGB-Bitcoin](assets/fr/008.webp)


### Begreppet tillståndsövergångar


I alla distribuerade system är syftet med valideringsmekanismen att kunna **bestämma giltigheten och den kronologiska ordningen för tillståndsändringar**. Målet är att verifiera att protokollreglerna har följts och att bevisa att dessa tillståndsändringar följer på varandra i en definitiv, oantastlig ordning.


För att förstå hur denna validering fungerar i samband med **Bitcoin** och, mer allmänt, för att förstå filosofin bakom Client-side Validation, låt oss först ta en titt tillbaka på mekanismerna i Bitcoin Blockchain, innan vi ser hur Client-side Validation skiljer sig från dem och vilka optimeringar den möjliggör.


![RGB-Bitcoin](assets/fr/009.webp)


När det gäller Bitcoin Blockchain baseras transaktionsvalideringen på en enkel regel:




- Alla nätverksnoder laddar ner varje block och transaktion;
- De validerar dessa transaktioner för att verifiera den korrekta utvecklingen av UTXO-uppsättningen (alla outnyttjade utgångar);
- De lagrar dessa data (i form av block) så att historiken kan spelas upp på nytt vid behov.


![RGB-Bitcoin](assets/fr/010.webp)


Denna modell har dock två stora nackdelar:




- Skalbarhet**: Eftersom varje nod måste bearbeta, verifiera och arkivera allas transaktioner finns det en uppenbar gräns för transaktionskapaciteten, särskilt kopplad till den maximala blockstorleken (1 MB i genomsnitt under 10 minuter för Bitcoin, exklusive cookies);
- Sekretess**: allt sänds och lagras offentligt (belopp, destinationsadresser etc.), vilket begränsar sekretessen i utbytet.


![RGB-Bitcoin](assets/fr/012.webp)


I praktiken fungerar denna modell för Bitcoin som en bas Layer (Layer 1), men kan bli otillräcklig för mer komplexa användningar som samtidigt kräver hög transaktionsgenomströmning och en viss grad av sekretess.


Client-side Validation bygger på den motsatta idén: i stället för att kräva att hela nätverket validerar och lagrar alla transaktioner, kommer varje deltagare (klient) att validera endast den del av historiken som berör honom eller henne:




- När en person tar emot en tillgång (eller någon annan digital egendom) behöver han eller hon bara känna till och verifiera den kedja av operationer (tillståndsövergångar) som leder till tillgången och bevisa dess legitimitet;
- Denna sekvens av transaktioner, från ***Genesis*** (första emissionen) till den senaste transaktionen, bildar en acyklisk riktad graf (DAG) eller Shard, dvs. en del av den totala historiken.


![RGB-Bitcoin](assets/fr/013.webp)


Samtidigt förlitar sig Client-side Validation på begreppet ***Commitment*** så att resten av nätverket (eller mer exakt, den underliggande Layer, såsom Bitcoin) kan låsa det slutliga tillståndet utan att se detaljerna i dessa data.


En *Commitment* är en kryptografisk Commitment, vanligtvis en _hash_ (t.ex. SHA-256) som infogas i en Bitcoin-transaktion och som bevisar att privata data har inkluderats, utan att avslöja dessa data.


Tack vare dessa _engagemang_ kan vi bevisa:




- Förekomsten av information (eftersom den är kopplad till en Hash);
- Informationens anterioritet (eftersom den är förankrad och tidsstämplad i Blockchain, med datum- och blockordning).


Det exakta innehållet avslöjas dock inte, vilket bevarar dess konfidentialitet.


I konkreta termer fungerar en RGB State Transition så här:




- Du förbereder en ny State Transition (t.ex. överföring av en RGB token);
- Du generate en kryptografisk Commitment till denna övergång och infogar den i en Bitcoin-transaktion (dessa åtaganden kallas "*anchors*" i RGB-protokollet);
- Motparten (mottagaren) hämtar historiken på kundsidan som är kopplad till denna tillgång och kontrollerar att den är konsekvent från början till slut, från Genesis i Smart contract till den övergång som du sänder till den.


![RGB-Bitcoin](assets/fr/014.webp)


Client-side Validation erbjuder två stora fördelar:




- Skalbarhet:**


De *åtaganden* som ingår i Blockchain är små (i storleksordningen några dussin byte). Detta säkerställer att blockutrymmet inte är mättat, eftersom endast Hash behöver inkluderas. Det gör också att off-chain-protokollet kan utvecklas, eftersom varje användare bara behöver lagra sitt historiska fragment (sin _stash_).




- Sekretess:**


Transaktionerna i sig (dvs. deras detaljerade innehåll) publiceras inte On-Chain. Endast deras fingeravtryck (*Hash*) är det. Belopp, adresser och Contract-logik förblir således privata, och mottagaren kan lokalt verifiera giltigheten av sin Shard genom att inspektera alla tidigare övergångar. Det finns ingen anledning för mottagaren att offentliggöra dessa uppgifter, utom i händelse av en tvist eller om bevis krävs.


I ett system som RGB kan flera tillståndsövergångar från olika kontrakt (eller olika tillgångar) aggregeras till en enda Bitcoin-transaktion via en enda _commitment_. Denna mekanism etablerar en deterministisk, tidsstämplad länk mellan On-Chain-transaktionen och off-chain-data (de validerade övergångarna på klientsidan) och gör det möjligt att samtidigt registrera flera shards i en enda Anchor-punkt, vilket ytterligare minskar kostnaden och fotavtrycket för On-Chain.


När denna Bitcoin-transaktion valideras "låser" den i praktiken permanent tillståndet för de underliggande kontrakten, eftersom det blir omöjligt att ändra den Hash som redan är inskriven i Blockchain.


![RGB-Bitcoin](assets/fr/015.webp)


### Stash-konceptet


En **Stash** är den uppsättning data på klientsidan som en deltagare absolut måste behålla för att upprätthålla integriteten och historiken för en RGB Smart contract. Till skillnad från en Lightning-kanal, där vissa tillstånd kan rekonstrueras lokalt från delad information, replikeras inte Stash för en RGB Contract någon annanstans: om du förlorar den kommer ingen att kunna återställa den till dig, eftersom du är ansvarig för din del av historiken. Det är därför du måste införa ett system med tillförlitliga rutiner för säkerhetskopiering i RGB.


![RGB-Bitcoin](assets/fr/016.webp)


### Single-Use Seal: ursprung och funktion


När man tar emot en tillgång som en valuta är två garantier nödvändiga:




- Äktheten av det mottagna föremålet;
- Det unika med det mottagna objektet, för att undvika dubbla kostnader.


För fysiska tillgångar, t.ex. en sedel, räcker det med fysisk närvaro för att bevisa att den inte har duplicerats. I den digitala världen, där tillgångarna enbart är information, är denna verifiering dock mer komplicerad, eftersom information lätt kan mångfaldigas och dupliceras.


Som vi såg tidigare gör avsändarens avslöjande av historiken för tillståndsövergångar det möjligt för oss att säkerställa äktheten hos en RGB token. Genom att ha tillgång till alla transaktioner sedan Genesis-transaktionen kan vi bekräfta token:s äkthet. Denna princip liknar den i Bitcoin, där myntens historia kan spåras tillbaka till den ursprungliga Coinbase Transaction för att verifiera deras giltighet. Till skillnad från Bitcoin är dock denna historik över tillståndsövergångar i RGB privat och förvaras på klientsidan.


För att förhindra Double-spending av RGB-tokens använder vi en mekanism som kallas "**Single-Use Seal**". Detta system säkerställer att varje token, när den väl har använts, inte kan återanvändas på ett bedrägligt sätt en andra gång.


Engångsförseglingar är kryptografiska primitiver, föreslagna 2016 av Peter Todd, som liknar konceptet med fysiska förseglingar: när en Seal har placerats på en behållare blir det omöjligt att öppna eller modifiera den utan att bryta Seal på ett irreversibelt sätt.


![RGB-Bitcoin](assets/fr/018.webp)


Detta tillvägagångssätt, överfört till den digitala världen, gör det möjligt att bevisa att en sekvens av händelser verkligen har ägt rum och att den inte längre kan ändras i efterhand. Engångsförseglingar går således utöver den enkla logiken med "Hash + Timestamp" och lägger till begreppet Seal som kan stängas **en enda gång**.


![RGB-Bitcoin](assets/fr/017.webp)


För att engångsförseglingar ska fungera krävs ett publikationssäkert medium som kan bevisa existensen eller frånvaron av en publikation och som är svårt (om inte omöjligt) att förfalska när informationen väl har spridits. En **Blockchain** (som Bitcoin) kan fylla denna roll, liksom en papperstidning med allmän spridning, som ett exempel. Idén är som följer:




- Vi vill bevisa att en viss Commitment på ett meddelande `h(m)` har publicerats för en publik utan att avslöja innehållet i meddelandet `m`;
- Vi vill bevisa att inget annat konkurrerande `h(m')`meddelande Commitment har publicerats i stället för `h(m)`;
- Vi vill också kunna kontrollera att meddelandet `m` existerar före ett visst datum.


En Blockchain lämpar sig utmärkt för denna roll: så snart en transaktion ingår i ett block har hela nätverket samma ofelbara bevis på dess existens och innehåll (åtminstone delvis, eftersom _commitment_ kan dölja detaljerna samtidigt som det bevisar meddelandets äkthet).


En Single-Use Seal kan därför ses som ett formellt löfte om att publicera ett meddelande (som fortfarande är okänt i det här skedet) en gång och endast en gång, på ett sätt som kan verifieras av alla berörda parter.


Till skillnad från enkla _commitments_ (Hash) eller tidsstämplar, som intygar ett existensdatum, ger en Single-Use Seal ytterligare en garanti för att **inga alternativa Commitment** kan existera samtidigt: du kan inte stänga samma Seal två gånger eller försöka ersätta det förseglade meddelandet.


Följande jämförelse hjälper till att förstå denna princip:




- Kryptografisk Commitment (Hash)**: Med en Hash-funktion kan du binda dig till en uppgift (ett nummer) genom att publicera dess Hash. Uppgifterna förblir hemliga tills du avslöjar förbilden, men du kan bevisa att du kände till dem i förväg;
- Timestamp (Blockchain)**: Genom att infoga denna Hash i Blockchain bevisar vi också att vi kände till den vid en exakt tidpunkt (den tidpunkt då den infogades i ett block);
- Single-Use Seal**: Med förseglingar för engångsbruk går vi ett steg längre genom att göra Commitment unik. Med en enda Hash kan du skapa flera motsägelsefulla åtaganden parallellt (problemet med läkaren som meddelar "*Det är en pojke*" till familjen och "*Det är en flicka*" i sin personliga dagbok). Single-Use Seal eliminerar denna möjlighet genom att ansluta Commitment till ett bevis-på-publiceringsmedium, såsom Bitcoin Blockchain, så att en utgift av UTXO slutgiltigt förseglar Commitment. När den väl har använts kan samma UTXO inte användas igen för att ersätta Commitment.
- Kryptografisk Commitment (Hash)**: Med en Hash-funktion kan du binda dig till en uppgift (ett tal) genom att publicera dess Hash. Uppgifterna förblir hemliga tills du avslöjar förbilden, men du kan bevisa att du kände till dem i förväg;
- Timestamp (Blockchain)**: Genom att infoga denna Hash i Blockchain bevisar vi också att vi kände till den vid en exakt tidpunkt (när den infogades i ett block);
- Single-Use Seal**: Med förseglingar för engångsbruk går vi ett steg längre genom att göra Commitment unik. Med en enda Hash kan du skapa flera motsägelsefulla åtaganden parallellt (problemet med läkaren som meddelar "*Det är en pojke*" till familjen och "*Det är en flicka*" i sin personliga dagbok). Single-Use Seal eliminerar denna möjlighet genom att ansluta Commitment till ett bevis-på-publiceringsmedium, såsom Bitcoin Blockchain, så att en utgift av UTXO slutgiltigt förseglar Commitment. När samma UTXO har spenderats kan den inte spenderas igen för att ersätta Commitment.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

Tätningar för engångsbruk fungerar i tre huvudsakliga steg:


**Seal Definition:**




- Alice definierar i förväg reglerna för publicering av Seal (när, var och hur meddelandet kommer att publiceras);
- Bob accepterar eller erkänner dessa villkor.


![RGB-Bitcoin](assets/fr/021.webp)


**Seal Stängningsdatum:**




- Vid körning stänger Alice Seal genom att publicera det faktiska meddelandet (vanligtvis i form av en _commitment_, t.ex. en Hash);
- Det ger också ett **vittne** (kryptografiskt bevis) som bevisar att Seal är stängd och oåterkallelig.


![RGB-Bitcoin](assets/fr/019.webp)


**Seal Verifiering:**




- När Seal är stängd kan Bob inte längre öppna den: han kan bara kontrollera att den har stängts;
- Bob samlar in Seal, **vittnet** och meddelandet (eller hans Commitment) för att se till att allt stämmer överens och att det inte finns några konkurrerande sigill eller olika versioner.


Processen kan sammanfattas enligt följande:


```txt
# Defined by Alice, validated or accepted by Bob
seal <- Define()
# Seal is closed by Alice with the message
witness <- Close(seal, message)
# Verification by Bob
bool <- Verify(seal, witness, message)
```


Client-side Validation går dock ett steg längre: om själva definitionen av en Seal ligger utanför Blockchain, är det (i teorin) möjligt för någon att ifrågasätta existensen eller legitimiteten av Seal i fråga. För att lösa detta problem används en kedja av sammanlänkande engångsförseglingar:




- Varje stängd Seal innehåller definitionen av följande Seal;
- Vi registrerar dessa stängningar (med deras _commitments_) inom Blockchain (i en Bitcoin-transaktion);
- Varje försök att ändra en tidigare Seal skulle således strida mot den historia som finns inbäddad i Bitcoin.


Detta är precis vad RGB-systemet gör:




- Publicerade meddelanden är _åtaganden_ till validerad data på klientsidan;
- Seal Definition är associerad med en Bitcoin UTXO;
- Seal stängs när denna UTXO spenderas eller när en ny produktion krediteras samma Commitment;
- Transaktionskedjan som spenderar dessa UTXO:er motsvarar beviset på publicering: varje övergång eller ändring av tillstånd på RGB är således förankrad i Bitcoin.


För att sammanfatta:




- Den _förseglade definitionen_ är den UTXO som du avser att Seal en framtida Commitment;
- _seal closing_ inträffar när du spenderar denna UTXO, vilket skapar en transaktion som innehåller Commitment;
- _vittnet_ är själva transaktionen, som bevisar att du har stängt Seal med detta innehåll;
- Du kan inte bevisa att en Seal inte har stängts (du kan inte vara helt säker på att en UTXO inte redan har använts eller inte kommer att användas i ett kvarter som du inte har sett än), men du kan bevisa att den faktiskt har stängts.


Denna unikhet är viktig för Client-side Validation: när du validerar en State Transition kontrollerar du att den motsvarar en unik UTXO, som inte tidigare har spenderats i en konkurrerande Commitment. Det är detta som garanterar att det inte förekommer dubbla utgifter i off-chain smarta kontrakt.


### Flera åtaganden och rötter


En RGB Smart contract kan behöva spendera flera engångsförseglingar (flera UTXO:er) samtidigt. Dessutom kan en enda Bitcoin-transaktion referera till flera olika kontrakt, som var och en förseglar sin egen State Transition. Detta kräver en **multi-Commitment**-mekanism för att på ett deterministiskt och unikt sätt bevisa att inget av åtagandena existerar i duplikat. Det är här begreppet **Anchor** kommer in i bilden i RGB: en speciell struktur som länkar en Bitcoin-transaktion och ett eller flera åtaganden på klientsidan (tillståndsövergångar), som alla potentiellt tillhör en annan Contract. Vi kommer att titta närmare på detta koncept i nästa kapitel.


![RGB-Bitcoin](assets/fr/023.webp)


Två av projektets huvudsakliga GitHub-arkiv (under LNPBP-organisationen) samlar de grundläggande implementeringarna av dessa koncept som studerades i det första kapitlet:




- validering på klientsidan**: Innehåller Rust-primitiver för lokal validering;
- tätningar för engångsbruk**: Implementerar logiken för att definiera och stänga dessa förseglingar på ett säkert sätt.


![RGB-Bitcoin](assets/fr/020.webp)


Observera att dessa programvarublock är Bitcoin-agnostiska; i teorin kan de tillämpas på vilket annat medium som helst för bevis på publicering (ett annat register, en tidskrift etc.). I praktiken förlitar sig RGB på Bitcoin för dess robusthet och breda konsensus.


![RGB-Bitcoin](assets/fr/021.webp)


### Frågor från allmänheten


#### Mot en bredare användning av engångstätningar


Peter Todd skapade också _Open Timestamps_-protokollet, och Single-Use Seal-konceptet är en naturlig förlängning av dessa idéer. Utöver RGB kan man tänka sig andra användningsområden, t.ex. konstruktion av _sidechains_ utan att behöva använda _merge mining_ eller drivechain-relaterade förslag som BIP300. Alla system som kräver en enda Commitment kan i princip utnyttja denna kryptografiska primitivitet. Idag är RGB den första större fullskaliga implementeringen.


#### Problem med datatillgänglighet


Eftersom varje användare i Client-side Validation lagrar sin egen del av historiken, garanteras inte datatillgänglighet globalt. Om en Contract-utgivare håller tillbaka eller återkallar viss information kan du vara omedveten om den faktiska utvecklingen av erbjudandet. I vissa fall (t.ex. stablecoins) förväntas emittenten upprätthålla offentliga data för att bevisa volymen i omlopp, men det finns ingen teknisk skyldighet att göra det. Det är därför möjligt att utforma avsiktligt ogenomskinliga kontrakt med obegränsad Supply, vilket väcker frågor om förtroende.


#### Sharding och Contract-isolering


Varje Contract representerar en isolerad _skärva_: USDT och USDC behöver till exempel inte dela med sig av sin historik. Atombyten är fortfarande möjliga, men detta innebär inte att deras register slås samman. Allt görs med kryptografiska Commitment, utan att avslöja hela historikgrafen för varje deltagare.


### Slutsats


Vi har sett var begreppet Client-side Validation passar in med Blockchain och _statskanaler_, hur det svarar på distribuerade databehandlingstrilemman och hur det utnyttjar Bitcoin Blockchain unikt för att undvika Double-spending och för *tidsstämpling*. Idén bygger på begreppet **Single-Use Seal**, som gör det möjligt att skapa unika åtaganden som inte kan spenderas om hur som helst. På så sätt laddar varje deltagare endast upp den historik som är absolut nödvändig, vilket ökar skalbarheten och sekretessen för smarta kontrakt samtidigt som säkerheten för Bitcoin bibehålls som en bakgrund.


Nästa steg blir att förklara mer i detalj hur denna Single-Use Seal-mekanism tillämpas i Bitcoin (via UTXO:er), hur ankare skapas och valideras, och sedan hur kompletta smarta kontrakt byggs i RGB. I synnerhet kommer vi att titta på frågan om multipla åtaganden, den tekniska utmaningen att bevisa att en Bitcoin-transaktion samtidigt förseglar flera tillståndsövergångar i olika kontrakt, utan att införa sårbarheter eller dubbla åtaganden.


Innan du dyker in i de mer tekniska detaljerna i det andra kapitlet, läs gärna om de viktigaste definitionerna (Client-side Validation, Single-Use Seal, ankare etc.) och kom ihåg den övergripande logiken: vi vill förena styrkorna hos Bitcoin Blockchain (säkerhet, decentralisering, tidsstämpling) med styrkorna hos off-chain-lösningar (hastighet, konfidentialitet, skalbarhet), och det är precis vad RGB och Client-side Validation försöker uppnå.


## Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


I detta kapitel tittar vi på implementeringen av Client-side Validation och engångsförseglingar inom Bitcoin Blockchain. Vi kommer att presentera huvudprinciperna för RGB:s **Commitment Layer** (Layer 1), med särskilt fokus på **TxO2**-systemet, som RGB använder för att definiera och stänga en Seal i en Bitcoin-transaktion. Därefter kommer vi att diskutera två viktiga punkter som ännu inte har behandlats i detalj:




- De _deterministiska Bitcoin-åtagandena_;
- Åtaganden för flera protokoll.


Det är kombinationen av dessa begrepp som gör det möjligt för oss att lägga flera system eller kontrakt ovanpå en enda UTXO och därmed en enda Blockchain.


Man bör komma ihåg att de kryptografiska operationer som beskrivs kan tillämpas, i absoluta termer, på andra blockkedjor eller publiceringsmedier, men Bitcoin:s egenskaper (när det gäller decentralisering, motstånd mot censur och öppenhet för alla) gör det till den perfekta grunden för att utveckla avancerad programmerbarhet som krävs av **RGB**.


### Commitment-system i Bitcoin och deras användning av RGB


Som vi såg i kursens första kapitel är engångsförseglingar ett allmänt koncept: vi lovar att inkludera en Commitment (_commitment_) på en specifik plats i en transaktion, och denna plats fungerar som en Seal som vi stänger i ett meddelande. På Bitcoin Blockchain finns det dock flera alternativ för att välja var denna _commitment_ ska placeras.


För att förstå logiken, låt oss komma ihåg den grundläggande principen: för att stänga en _single-use seal_, spenderar vi det förseglade området genom att infoga _commitment_ på ett visst meddelande. I Bitcoin kan detta göras på ett antal olika sätt:




- Använd en publik nyckel eller Address**


Vi kan bestämma att en viss offentlig nyckel eller Address är _försegling för engångsbruk_. Så snart denna nyckel eller Address förekommer On-Chain i en transaktion, betyder det att Seal är stängd med ett visst meddelande.




- Använd en **Bitcoin** transaktionsutgång


Detta innebär att en _försegling för engångsbruk_ definieras som en exakt _utgångspunkt_ (ett txid + utgångsnummerpar). Så snart denna _utgångspunkt_ är förbrukad stängs Seal.


Under arbetet med RGB identifierade vi minst 4 olika sätt att implementera dessa tätningar på Bitcoin:




- Definiera Seal via en publik nyckel och stäng den i en _output_;
- Definiera Seal med en _outpoint_ och stäng den med en _output_;
- Definiera Seal via värdet på en publik nyckel och stäng den i en _input_;
- Definiera Seal via en _outpoint_ och stäng den i en _input_.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


Vi kommer inte att gå in i detalj på var och en av dessa konfigurationer, eftersom vi i RGB har valt att använda **en _utpunkt_ som definition av Seal** och att placera _åtagandet_ i utgången av den transaktion som spenderar denna _utpunkt_. Vi kan därför införa följande begrepp för fortsättningen:




- "Seal Definition"**: En given _utgångspunkt_ (identifierad av txid + utgångsnr);
- "Seal stänger "**: Transaktionen som spenderar denna _outpoint_, i vilken ett _commitment_ läggs till ett meddelande.


Detta system har valts för att det är kompatibelt med RGB-arkitekturen, men andra konfigurationer kan vara användbara för olika ändamål.


"O2" i "TxO2" påminner oss om att både definition och avslut baseras på utgiften (eller skapandet) av en transaktionsutgång.


### Exempel på TxO2-diagram


Som en påminnelse kräver inte definitionen av en _försegling för engångsbruk_ nödvändigtvis att en On-Chain-transaktion publiceras. Det räcker till exempel att Alice redan har en outnyttjad UTXO. Hon kan besluta: "Denna _utpunkt_ (redan existerande) är nu min Seal". Hon noterar detta lokalt (_klientsidan_), och tills denna UTXO är förbrukad anses Seal vara öppen.


![RGB-Bitcoin](assets/fr/024.webp)


Den dag den vill stänga Seal (för att signalera en händelse eller för att Anchor ett visst meddelande) spenderar den denna UTXO i en ny transaktion (denna transaktion kallas ofta "_vittnestransaktion_" (inte relaterad till _segwit_, det är bara den term vi ger den). Denna nya transaktion kommer att innehålla _åtagandet_ till meddelandet.


![RGB-Bitcoin](assets/fr/025.webp)


Observera att i detta exempel:




- Ingen annan än Bob (eller de personer som Alice väljer att avslöja det fullständiga beviset för) kommer att veta att ett visst meddelande är dolt i denna transaktion;
- Alla kan se att _outpoint_ har spenderats, men endast Bob har beviset på att meddelandet faktiskt är förankrat i transaktionen.


För att illustrera detta TxO2-system kan vi använda en _single-use seal_ som en mekanism för att återkalla en PGP-nyckel. Istället för att publicera ett återkallningscertifikat på servrar, kan Alice säga: "Denna Bitcoin-utgång, om den används, innebär att min PGP-nyckel återkallas".


Alice har därför en specifik UTXO, till vilken ett visst tillstånd eller vissa data (som endast är kända för henne) är associerade lokalt (på klientsidan).


Alice informerar Bob om att om denna UTXO spenderas kommer en viss händelse att anses ha inträffat. Från utsidan är allt vi ser en Bitcoin-transaktion, men Bob vet att denna utgift har en dold betydelse.


![RGB-Bitcoin](assets/fr/026.webp)


När Alice spenderar denna UTXO, stänger hon Seal på ett meddelande som anger hennes nya nyckel, eller helt enkelt återkallandet av den gamla. På detta sätt kommer alla som övervakar On-Chain att se att UTXO spenderas, men endast de som har det fullständiga beviset kommer att veta att det är just återkallandet av PGP-nyckeln.


![RGB-Bitcoin](assets/fr/027.webp)


För att Bob eller någon annan inblandad ska kunna kontrollera det dolda meddelandet måste Alice förse honom med information från off-chain.


![RGB-Bitcoin](assets/fr/028.webp)


Alice måste därför förse Bob med följande:




- Själva meddelandet (t.ex. den nya PGP-nyckeln);
- Kryptografiskt bevis för att meddelandet var inblandat i transaktionen (kallas _extra transaction proof_ eller _anchor_).


![RGB-Bitcoin](assets/fr/029.webp)


Tredje part har inte denna information. De ser bara att en UTXO har använts. Konfidentialiteten är därför garanterad.


För att förtydliga strukturen sammanfattar vi processen i två transaktioner:




- Transaktion 1**: Detta innehåller _seal-definitionen_, dvs. den _utpunkt_ som kommer att fungera som Seal.


![RGB-Bitcoin](assets/fr/031.webp)




- Transaktion 2**: Spenderar denna _outpoint_. Detta stänger Seal och, i samma transaktion, infogar _commitment_ på meddelandet.


![RGB-Bitcoin](assets/fr/033.webp)


Vi kallar därför den andra transaktionen för "_vittnestransaktionen_".


För att illustrera detta från en annan vinkel kan vi representera två lager:




- Toppen Layer (Blockchain, offentlig)**: alla ser transaktionen och vet att en _outpoint_ har spenderats;
- Den lägre Layer (klientsidan, privat)**: endast Alice (eller den berörda personen) vet att den här kostnaden motsvarar det och det meddelandet, via det kryptografiska beviset och det meddelande som hon förvarar lokalt.


![RGB-Bitcoin](assets/fr/034.webp)


Men när man stänger Seal uppstår frågan om var _commitment_ ska infogas.


I föregående avsnitt nämnde vi kortfattat hur Client-side Validation-modellen kan tillämpas på RGB och andra system. Här tar vi itu med delen om **deterministiska Bitcoin-åtaganden** och hur man integrerar dem i en transaktion. Tanken är att förstå varför vi försöker infoga en enda Commitment i _vittnestransaktionen_, och framför allt hur vi kan säkerställa att det inte kan finnas några andra konkurrerande åtaganden som inte avslöjas.


### Commitment platser i en transaktion


När du ger någon bevis på att ett visst meddelande är inbäddat i en transaktion, måste du kunna garantera att det inte finns en annan form av Commitment (ett andra, dolt meddelande) i samma transaktion som inte har avslöjats för dig. För att Client-side Validation ska förbli robust behöver du en **deterministisk** mekanism för att placera ett enda _åtagande_ i den transaktion som stänger _förseglingen för engångsbruk_.


I _vittnestransaktionen_ spenderas den berömda UTXO (eller _seal definition_) och denna utgift motsvarar stängningen av Seal. Tekniskt sett vet vi att varje outpoint bara kan spenderas en gång. Det är just detta som ligger till grund för Bitcoin:s motstånd mot dubbla utgifter. Men utgiftstransaktionen kan ha flera _inputs_, flera _outputs_ eller vara sammansatt på ett komplext sätt (coinjoins, Lightning channels etc.). Vi måste därför tydligt definiera var vi ska infoga _åtagandet_ i denna struktur, otvetydigt och enhetligt.


Oavsett metod (PkO, TxO2, etc.) kan _åtagandet_ införas:




- I en **Input** via:
    - Sigtweak** (modifierar `r`-komponenten i ECDSA-signaturen, liknande "Sign-to-Contract"-principen);
    - Witweak** (transaktionens _segregerade vittnesuppgifter_ ändras).
- I en **utgång** via:
    - Keytweak** (mottagarens publika nyckel "tweakas" med meddelandet);
    - Opret** (meddelandet är placerat i en icke-spenderbar utgång `OP_RETURN`);
    - Tapret** (eller _Taptweak_), som bygger på Taproot för att infoga Commitment i skriptdelen av en Taproot-nyckel och därmed ändra den publika nyckeln på ett deterministiskt sätt.


![RGB-Bitcoin](assets/fr/035.webp)


Här är detaljerna för varje metod:


![RGB-Bitcoin](assets/fr/038.webp)


***Sig tweak (sign-to-Contract):***


Ett tidigare system innebar att man utnyttjade den slumpmässiga delen av en signatur (ECDSA eller Schnorr) för att bädda in _åtagandet_: detta är den teknik som kallas "**Sign-to-Contract**". Du ersätter den slumpmässigt genererade Nonce med en Hash som innehåller data. På så sätt avslöjar signaturen implicit din Commitment, utan något ytterligare utrymme i transaktionen. Detta tillvägagångssätt har ett antal fördelar:




- Ingen överbelastning av On-Chain (du använder samma plats som den grundläggande Nonce);
- I teorin kan detta vara ganska diskret, eftersom Nonce ursprungligen är ett slumpmässigt datum.


Två stora nackdelar har dock framkommit:




- Multisig före Taproot: När du har flera undertecknare måste du bestämma vilken signatur som ska bära _commitment_. Signaturer kan beställas på olika sätt, och om en undertecknare vägrar förlorar du kontrollen över resultatet av _commitment_;
- MuSig och den delade Nonce: med Schnorr Multisig (*MuSig*) är genereringen av Nonce en flerpartsalgoritm och det blir praktiskt taget omöjligt att justera Nonce individuellt.


I praktiken är **sig tweak** inte heller särskilt kompatibel med befintlig hårdvara (hårdvaruplånböcker) och format (Lightning, etc.). Så den här fantastiska idén är Hard att genomföra i praktiken.


***Nyckeljustering (betala till Contract):***


**key tweak** tar upp det historiska konceptet _pay-to-contract_. Vi tar den offentliga nyckeln `X` och ändrar den genom att lägga till värdet `H(meddelande)`. Om X = x * G och h = H(meddelande) blir den nya nyckeln X' = X + h * G. Den här modifierade nyckeln döljer Commitment till `meddelandet`. Innehavaren av den ursprungliga privata nyckeln kan, genom att lägga till `h` till sin privata nyckel `x`, bevisa att han har nyckeln för att spendera utmatningen. I teorin är detta elegant, eftersom:




- _åtagandet_ anges utan att några ytterligare fält läggs till;
- Du lagrar inte några ytterligare On-Chain-data.


I praktiken stöter vi dock på följande svårigheter:




- Plånböcker känner inte längre igen den publika standardnyckeln, eftersom den har "tweakats", så de kan inte enkelt associera UTXO med din vanliga nyckel;
- Hårdvaruplånböcker är inte utformade för att signera med en nyckel som inte härrör från deras standardderivat;
- Du måste anpassa dina skript, beskrivningar etc.


I samband med RGB planerades denna väg fram till 2021, men det visade sig vara för komplicerat att få den att fungera med nuvarande standarder och infrastruktur.


***Vittnesändring:***


En annan idé, som vissa protokoll som _inscriptions Ordinals_ har tillämpat, är att placera uppgifterna direkt i transaktionens vittnesavsnitt (därav uttrycket "witness tweak"). Denna metod är dock:




- Gör engagemanget omedelbart synligt (du klistrar bokstavligen in rådata i vittnet);
- Kan vara föremål för censur (miners eller noder kan vägra att vidarebefordra om den är för stor eller någon annan godtycklig egenskap);
- Kräver utrymme i kvarteren, i strid med RGB:s mål om diskretion och lätthet.


Dessutom är witness utformat för att kunna beskäras i vissa sammanhang, vilket kan göra det mer komplicerat att ha robusta bevis.


***Open-return (opret):***


En `OP_RETURN` är mycket enkel till sin funktion och gör att du kan lagra en Hash eller ett meddelande i ett speciellt fält i transaktionen. Men det är omedelbart upptäckbart: alla ser att det finns ett _åtagande_ i transaktionen, och det kan censureras eller kasseras, samt lägga till extra utdata. Eftersom detta ökar transparensen och storleken anses det vara mindre tillfredsställande ur en Client-side Validation-lösnings synvinkel.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


Det sista alternativet är att använda **Taproot** (introducerad med BIP341) med *Tapret*-systemet. *Tapret* är en mer komplex form av deterministisk Commitment, som ger förbättringar när det gäller fotavtryck på Blockchain och sekretess för Contract-operationer. Huvudidén är att dölja Commitment i `Script Path Spend`-delen av en [Taproot-transaktion] (https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki).


![RGB-Bitcoin](assets/fr/036.webp)


Innan vi beskriver hur Commitment infogas i en Taproot-transaktion, låt oss titta på den **exakta formen** av Commitment, som **imperativt** måste motsvara en 64-byte sträng [konstruerad](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) enligt följande:


```txt
64-byte_Tapret_Commitment =

OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- De 29 byte `OP_RESERVED`, följt av `OP_RETURN`, sedan `OP_PUSHBYTE_33`, bildar den 31 byte långa _prefix_-delen;
- Därefter kommer en 32-byte _commitment_ (vanligtvis Merkle Root från **MPC**), till vilken vi lägger till 1 byte **Nonce** (totalt 33 byte för denna andra del).


Så 64-bytesmetoden `Tapret` ser ut som en `Opret` till vilken vi har prefixat 29 byte `OP_RESERVED` och lagt till en extra byte som en Nonce.


För att bibehålla flexibiliteten när det gäller implementering, sekretess och skalning tar Tapret-systemet hänsyn till olika användningsfall, beroende på kraven:




- Unikt införlivande av en Tapret Commitment i en Taproot-transaktion utan en befintlig Script Path-struktur;
- Integrering av en Tapret Commitment i en Taproot-transaktion som redan är utrustad med en Script Path.


Låt oss ta en närmare titt på vart och ett av dessa två scenarier.


#### Tapret-inkorporering utan befintligt manus Path


I det här första fallet utgår vi från en Taproot-utmatningsnyckel (*Taproot Output Key*) `Q` som endast innehåller den interna publika nyckeln `P` *(Internal Key*), utan någon associerad skriptsökväg (*Script Path*):


![RGB-Bitcoin](assets/fr/047.webp)




- "P": den interna offentliga nyckeln för _Key Path Spend_.
- `G`: den elliptiska kurvans genereringspunkt [secp256k1] (https://en.Bitcoin.it/wiki/Secp256k1).

-`t = tH_TWEAK(P)` är tweakfaktorn, beräknad via en _taggad hash_ (t.ex. `SHA-256(SHA-256(TapTweak) || P)`), i enlighet med [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation). Detta bevisar att det inte finns något dolt skript.


För att inkludera en **Tapret** Commitment, lägg till en **Script Path Spend** med ett **unikt script**, enligt följande:


![RGB-Bitcoin](assets/fr/048.webp)




- `t = tH_TWEAK(P || Script_root)` blir då den nya tweakfaktorn, inklusive **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` representerar roten till detta **script**, som helt enkelt är en Hash av typen `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.


Beviset för inkludering och unikhet i Taproot-trädet här kokar ner till den enda interna offentliga nyckeln `P`.


#### Tapret-integration i en redan befintlig Script Path


Det andra scenariot gäller en mer komplex `Q` **Taproot**-utskrift, som redan innehåller flera skript. Vi har t.ex. ett träd med 3 skript:


![RGB-Bitcoin](assets/fr/049.webp)




- `tH_LEAF(x)` betecknar den normaliserade taggade Hash-funktionen för ett bladskript.
- `A, B, C` representerar skript som redan ingår i Taproot-strukturen.


För att lägga till Tapret Commitment måste vi infoga ett *unspendable script* på trädets första nivå och flytta de befintliga scripten en nivå nedåt. Visuellt blir trädet:


![RGB-Bitcoin](assets/fr/050.webp)




- `tHABC` representerar den taggade Hash av toppnivågrupperingen `A, B, C`.
- `tHT` representerar Hash i skriptet som motsvarar 64-byte `Tapret`.


Enligt Taproot-reglerna måste varje gren/blad kombineras i enlighet med en lexikografisk Hash-ordning. Det finns två möjliga fall:




- `tHT` > `tHABC`**: Tapret Commitment flyttas till höger om trädet. Unikhetsbeviset behöver bara `tHABC` och `P`;
- `tHT` < `tHABC`**: Tapret Commitment är placerad till vänster. För att bevisa att det inte finns någon annan Tapret Commitment till höger måste `tHAB` och `tHC` avslöjas för att visa att det inte finns någon annan sådan skrift.


Visuellt exempel för det första fallet (`tHABC < tHT`):


![RGB-Bitcoin](assets/fr/051.webp)


Exempel för det andra fallet (`tHABC > tHT`):


![RGB-Bitcoin](assets/fr/052.webp)


#### Optimering med Nonce


För att förbättra sekretessen kan vi "bryta" (en mer korrekt term skulle vara "bruteforcing") värdet på `<Nonce>` (den sista byten i 64-bytes `Tapret`) i ett försök att få en Hash `tHT` så att `tHABC < tHT`. I det här fallet placeras Commitment till höger, vilket gör att användaren inte behöver avslöja hela innehållet i befintliga skript för att bevisa att Tapret är unikt.


Sammanfattningsvis erbjuder `Tapret` ett diskret och deterministiskt sätt att införliva en Commitment i en Taproot-transaktion, samtidigt som det respekterar kravet på unikhet och entydighet som är väsentligt för RGB:s Client-side Validation- och Single-Use Seal-logik.


#### Giltiga utgångar


För RGB Commitment-transaktioner är huvudkravet för ett giltigt Bitcoin Commitment-schema följande: Transaktionen (*Witness Transaction*) måste bevisligen innehålla en enda Commitment. Detta krav gör det omöjligt att konstruera en alternativ historik för validerade data på klientsidan inom samma transaktion. Detta innebär att det meddelande kring vilket _single-use seal_ sluter sig är unikt.


För att uppfylla denna princip, och oavsett antalet utgångar i en transaktion, kräver vi att **en och endast en utgång** kan innehålla en Commitment. För vart och ett av de system som används (*Opret* eller *Tapret*) är de enda giltiga utgångar som kan innehålla ett RGB _åtagande_ följande:




- Den första utskriften `OP_RETURN` (om sådan finns) för *Opret*-systemet;
- Den första Taproot-utgången (om sådan finns) för *Tapret*-systemet.


Observera att det är fullt möjligt för en transaktion att innehålla en enda `Opret` Commitment och en enda `Tapret` Commitment i två separata utgångar. Tack vare den deterministiska karaktären hos Seal Definition motsvarar dessa två åtaganden två olika delar av data som validerats på klientsidan.


### Analys och praktiska val i RGB


När vi startade RGB gick vi igenom alla dessa metoder för att avgöra var och hur man placerar ett _åtagande_ i en transaktion på ett deterministiskt sätt. Vi definierade några kriterier:




- Kompatibilitet med olika scenarier (t.ex. Multisig, Lightning, hårdvaruplånböcker m.m.);
- Påverkan på On-Chain-utrymmet;
- Svårighet att genomföra och underhålla;
- Konfidentialitet och motstånd mot censur.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






Under studiens gång blev det tydligt att inget av Commitment-systemen var helt kompatibelt med den nuvarande Lightning-standarden (som inte använder Taproot, _muSig2_ eller ytterligare _commitment_-stöd). Ansträngningar pågår för att modifiera Lightnings kanalkonstruktion (*BiFrost*) för att möjliggöra införandet av RGB-åtaganden. Detta är ytterligare ett område där vi behöver se över transaktionsstrukturen, nycklarna och sättet på vilket kanaluppdateringar signeras.


Analysen visade att andra metoder (key tweak, sig tweak, witness tweak etc.) i själva verket medförde andra former av komplikationer:




- Antingen har vi en stor On-Chain-volym;
- Antingen finns det en radikal inkompatibilitet med den befintliga Wallet-koden;
- Antingen är lösningen inte genomförbar i icke-samarbetande Multisig.


För RGB är det framför allt två metoder som sticker ut: ***Opret*** och ***Tapret***, som båda klassificeras som "Transaction Output" och är kompatibla med TxO2-läget som används av protokollet.


### Åtaganden enligt flera protokoll - MPC


I detta avsnitt tittar vi på hur **RGB** hanterar aggregeringen av flera kontrakt (eller, mer exakt, deras _transition bundles_) inom en enda Commitment (*Commitment*) som registrerats i en Bitcoin-transaktion via ett deterministiskt schema (enligt `Opret` eller `Tapret`). För att uppnå detta sker ordningen för merkelisering av de olika kontrakten i en struktur som kallas **MPC Tree** (_Multi Protocol Commitment Tree_). I det här avsnittet tittar vi på konstruktionen av detta MPC-träd, hur man får fram dess rot och hur flera kontrakt kan dela samma transaktion konfidentiellt och otvetydigt.


Multi Protocol Commitment (MPC) är utformad för att tillgodose två behov:




- Konstruktionen av `mpc::Commitment` Hash: detta kommer att ingå i Bitcoin Blockchain enligt ett `Opret` eller `Tapret` schema, och måste återspegla alla tillståndsändringar som ska valideras;
- Samtidig lagring av flera kontrakt i ett enda _commitment_, vilket gör att separata uppdateringar av flera tillgångar eller RGB-kontrakt kan hanteras i en enda Bitcoin-transaktion.


I konkreta termer tillhör varje _transition bundle_ en viss Contract. All denna information sätts in i ett **MPC-träd**, vars rot (`mpc::Root`) sedan hashas igen för att ge `mpc::Commitment`. Det är denna sista Hash som placeras i Bitcoin-transaktionen (_vittnestransaktion_), enligt den deterministiska metod som valts.


![RGB-Bitcoin](assets/fr/042.webp)


#### MPC Root Hash


Det värde som faktiskt skrivs On-Chain (i `Opret` eller `Tapret`) kallas `mpc::Commitment`. Detta beräknas i form av [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki), enligt formeln:


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


var:




- `mpc_tag` är en tagg: `urn:ubideco:mpc:Commitment#2024-01-31`, vald enligt [RGB tagging conventions] (https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) anger djupet på *MPC Tree*;
- cofactor` (16 bitar, i Little Endian) är en parameter som används för att främja unikheten i de positioner som tilldelats varje Contract i trädet;
- `mpc::Root` är roten till *MPC Tree*, beräknad enligt den process som beskrivs i nästa avsnitt.


![RGB-Bitcoin](assets/fr/044.webp)


#### MPC Trädkonstruktion


För att bygga detta MPC-träd måste vi se till att varje Contract motsvarar en unik bladposition. Anta att vi har:




- `c` kontrakt som skall inkluderas indexerade av `i` i `i` = {0,1,...,C-1};
- För varje Contract `c_i` har vi en identifierare `ContractId(i) = c_i`.


Vi konstruerar sedan ett träd med bredden `w` och djupet `d` så att `2^d = w`, med `w > C`, så att varje Contract kan placeras i ett separat _blad_. Positionen `pos(c_i)` för varje Contract i trädet bestäms av:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


där "cofactor" är ett heltal som ökar sannolikheten för att erhålla distinkta positioner för varje Contract. I praktiken följer konstruktionen en iterativ process:




- Vi startar från ett minimidjup (`d=3` enligt konvention för att dölja det exakta antalet kontrakt);
- Vi provar olika "cofaktorer" (upp till "w/2", eller maximalt 500 av prestandaskäl);
- Om vi inte lyckas placera alla kontrakt utan kollision, inkrementerar vi `d` och börjar om.


Målet är att undvika för höga träd och samtidigt minimera risken för kollisioner. Observera att kollisionsfenomenet följer en slumpmässig fördelningslogik, kopplad till [Anniversary Paradox] (https://en.wikipedia.org/wiki/Birthday_problem).


#### Bebodda löv


När `C` olika positioner `pos(c_i)` har erhållits för kontrakt `i = {0,1,...,C-1}`, fylls varje ark med en Hash-funktion (*märkt Hash*):


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


var:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, väljs alltid i enlighet med Merkle-konventionerna i RGB;
- `0x10` identifierar ett _kontraktsblad_;
- `c_i` är Contract-identifieraren på 32 byte (härledd från Genesis Hash);
- bundleId(c_i)` är en 32-byte Hash som beskriver uppsättningen `State Transitions` i förhållande till `c_i` (samlad i en *Transition Bundle*).


#### Obebodda löv


De återstående bladen, som inte tilldelats en Contract (dvs. `w - C`-bladen), fylls med ett "dummy"-värde (_entropiblad_):


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


var:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, väljs alltid i enlighet med Merkle-konventionerna i RGB;
- `0x11` betecknar ett _entropiblad_;
- `entropy` är ett slumpmässigt värde på 64 byte som väljs av den som bygger trädet;
- `j` är positionen (i 32 bitars Little Endian) för detta blad i trädet.


#### MPC-noder


Efter att ha genererat `w` löv (bebodda eller inte) fortsätter vi med merkelisering. Alla interna noder hashas enligt följande:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


var:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, väljs alltid i enlighet med Merkle-konventionerna i RGB;
- b` är _förgreningsfaktorn_ (8 bitar). Oftast är `b=0x02` eftersom trädet är binärt och komplett;
- d` är nodens djup i trädet;
- `w` är trädets bredd (i 256-bitars Little Endian binär);
- tH1` och `tH2` är hashvärdena för underordnade noder (eller blad), redan beräknade enligt ovan.


Om vi fortsätter på detta sätt får vi roten `mpc::Root`. Vi kan sedan beräkna `mpc::Commitment` (som förklarats ovan) och infoga den On-Chain.


För att illustrera detta, låt oss föreställa oss ett exempel där `C=3` (tre kontrakt). Deras positioner antas vara `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. De andra bladen (positionerna 0, 1, 3, 5, 6) är _entropiblad_. Diagrammet nedan visar sekvensen av hashes till roten med:




- `BUNDLE_i` som representerar `BundleId(c_i)`;
- `tH_MPC_LEAF(A)` och så vidare, som representerar löv (vissa för kontrakt, andra för entropi);
- Varje gren `tH_MPC_BRANCH(...)` kombinerar hasharna för sina två barn.


Slutresultatet är **mpc::Root** och därefter `mpc::Commitment`.


![RGB-Bitcoin](assets/fr/053.webp)


#### MPC axelkontroll


När en verifierare vill försäkra sig om att en Contract från `c_i` (och dess `BundleId`) ingår i den slutliga `mpc::Commitment`, får han helt enkelt ett Merkle-bevis. Detta bevis anger de noder som behövs för att spåra löven (i detta fall `c_i` s _kontraktsblad_) tillbaka till roten. Det finns inget behov av att avslöja hela *MPC-trädet*: detta skyddar sekretessen för andra kontrakt.


I exemplet behöver en `c_2`-verifierare bara en mellanliggande Hash (`tH_MPC_LEAF(D)`), två `tH_MPC_BRANCH(...)`, `pos(c_2)`-positionsbeviset och `cofactor`-värdet. Den kan sedan lokalt rekonstruera roten, sedan räkna om `mpc::Commitment` och jämföra det med det som skrevs i Bitcoin-transaktionen (inom `Opret` eller `Tapret`).


![RGB-Bitcoin](assets/fr/054.webp)


Denna mekanism säkerställer att:




- Statusen för `c_2` ingår verkligen i det samlade informationsblocket (klientsidan);
- Ingen kan bygga en alternativ historia med samma transaktion, eftersom On-Chain _commitment_ pekar på en enda MPC-rot.


#### Sammanfattning av MPC:s struktur


Multi Protocol Commitment* (MPC) är den princip som gör det möjligt för RGB att aggregera flera kontrakt till en enda Bitcoin-transaktion, samtidigt som åtagandenas unikhet och sekretess gentemot andra deltagare bibehålls. Tack vare den deterministiska konstruktionen av trädet tilldelas varje Contract en unik position, och förekomsten av "dummy"-blad (*Entropy Leaves*) döljer delvis det totala antalet kontrakt som deltar i transaktionen.


Hela Merkle Tree lagras aldrig på klienten. Vi gör helt enkelt generate en _Merkle path_ för varje berörd Contract, som överförs till mottagaren (som sedan kan validera Commitment). I vissa fall kan du ha flera tillgångar som har passerat genom samma UTXO. Du kan då slå samman flera _Merkle paths_ till ett s.k. _multiprotokoll Commitment-block_ för att undvika att duplicera för mycket data.


Varje _Merkle-bevis_ är därför lättviktigt, särskilt som träddjupet inte kommer att överstiga 32 i RGB. Det finns också ett begrepp "Merkle-block", som innehåller mer information (tvärsnitt, entropi etc.), vilket är användbart för att kombinera eller separera flera grenar.


Det är därför det tog så lång tid att slutföra RGB. Vi hade den övergripande visionen från 2019: att lägga allt på klientsidan och cirkulera tokens off-chain. Men för detaljer som sharding för flera kontrakt, strukturen för Merkle Tree, hur man hanterar kollisioner och sammanfogningsbevis ... allt detta krävde iterationer.


### Ankare: en global samling


Efter konstruktionen av våra åtaganden (`Opret` eller `Tapret`) och vår MPC (*Multi Protocol Commitment*) behöver vi Address begreppet **Anchor** i RGB-protokollet. En Anchor är en validerad struktur på klientsidan som sammanför de Elements som behövs för att verifiera att en Bitcoin Commitment faktiskt innehåller specifik avtalsinformation. Med andra ord sammanfattar en Anchor alla data som behövs för att validera de _åtaganden_ som beskrivs ovan.


En Anchor består av tre ordnade fält:




- `txid`
- `MPC Proof`
- extra transaktionsbevis - ETP


Vart och ett av dessa fält spelar en roll i valideringsprocessen, oavsett om det handlar om att rekonstruera den underliggande Bitcoin-transaktionen eller bevisa förekomsten av en dold Commitment (särskilt i fallet med `Tapret`).


#### txid


Fältet `txid` motsvarar 32-byte-identifieraren för den Bitcoin-transaktion som innehåller `Opret` eller `Tapret` Commitment.


I teorin skulle det vara möjligt att hitta denna `txid` genom att spåra kedjan av tillståndsövergångar som i sig pekar på varje Witness Transaction, enligt logiken för engångsförseglingar. Men för att underlätta och påskynda verifieringen ingår denna `txid` helt enkelt i Anchor, vilket gör att valideraren inte behöver gå tillbaka genom hela off-chain-historiken.


#### MPC Bevis


Det andra fältet, `MPC Proof`, hänvisar till beviset för att denna speciella Contract (t.ex. `c_i`) ingår i _Multi Protocol Commitment_. Det är en kombination av:




- `pos_i`, positionen för denna Contract i MPC-trädet;
- cofactor", det värde som definieras för att lösa positionskollisioner;
- "Merkle Proof", dvs. den uppsättning noder och hashar som används för att rekonstruera MPC-roten och verifiera att Contract-identifieraren och dess "Transition Bundle" är kopplade till roten.


Denna mekanism beskrevs i det föregående avsnittet om att bygga *MPC-trädet*, där varje Contract får ett unikt blad tack vare:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


Därefter används ett deterministiskt merkeliseringsschema för att aggregera alla löv (kontrakt + entropi). I slutändan gör `MPC Proof` att roten kan rekonstrueras lokalt och jämföras med `mpc::Commitment` som inkluderade On-Chain.


#### Extra transaktionsbevis - ETP


Det tredje fältet, **ETP**, beror på vilken typ av Commitment som används. Om Commitment är av typen `Opret` krävs inget ytterligare bevis. Valideraren inspekterar transaktionens första `OP_RETURN`-utdata och hittar `mpc::Commitment` direkt där.


**Om Commitment är av typen `Tapret`**, måste ett ytterligare bevis som kallas *Extra Transaction Proof - ETP* tillhandahållas. Det innehåller:




- Den interna publika nyckeln (`P`) för Taproot-utgången i vilken *Commitment* är inbäddad;
- Partnernoderna för `Script Path Spend` (när Tapret *Commitment* infogas i ett skript), för att bevisa den exakta platsen för detta skript i Taproot-trädet:
 - Om `Tapret` *Commitment* ligger på den högra grenen, avslöjar vi den vänstra noden (t.ex. `tHABC`),
 - Om `Tapret` *Commitment* finns till vänster måste du avslöja 2 noder (t.ex. `tHAB` och `tHC`) för att bevisa att ingen annan *Commitment* finns på höger sida.
- Nonce kan användas för att "gräva fram" den bästa konfigurationen, vilket gör att * Commitment* kan placeras till höger om trädet (bevisoptimering).


Detta ytterligare bevis är viktigt eftersom, till skillnad från `Opret`, `Tapret` Commitment är integrerad i strukturen för ett Taproot-skript, vilket kräver att en del av Taproot-trädet avslöjas för att korrekt validera platsen för *Commitment*.


![RGB-Bitcoin](assets/fr/045.webp)


**Anchors** kapslar därför in all information som krävs för att validera en Bitcoin Commitment i samband med RGB. De anger både den relevanta transaktionen (`txid`) och beviset på Contract positionering (`MPC Proof`), samtidigt som de hanterar det ytterligare beviset (`ETP`) i fallet med `Tapret`. På detta sätt skyddar en Anchor integriteten och det unika i off-chain-tillståndet genom att säkerställa att samma transaktion inte kan omtolkas för andra avtalsdata.


### Slutsats


I detta kapitel har vi gått igenom:




- Hur man tillämpar konceptet Single-use Seals i Bitcoin (i synnerhet via en _outpoint_);
- De olika metoderna för att på ett deterministiskt sätt infoga en _commitment_ i en transaktion (Sig tweak, Key tweak, witness tweak, OP_RETURN, Taproot/Tapret);
- Anledningarna till att RGB fokuserar på Tapret-åtaganden;
- Multi-Contract-hantering via _multi-protocol commitments_, viktigt om du inte vill exponera en hel stat eller andra kontrakt när du vill bevisa en specifik punkt;
- Vi har också sett vilken roll _Anchors_ spelar, som sammanför allt (transaktion txid, Merkle Tree proof och Taproot proof) i ett enda paket.


I praktiken är den tekniska implementeringen uppdelad mellan flera dedikerade Rust _crates_ (i _client_side_validation_, _commit-verify_, _bp_core_, etc.). De grundläggande begreppen finns där:


![RGB-Bitcoin](assets/fr/046.webp)


I nästa kapitel ska vi titta på den rena off-chain-komponenten i RGB, nämligen Contract-logik. Vi kommer att se hur RGB-kontrakt, organiserade som delvis replikerade _finita tillståndsmaskiner_, uppnår mycket högre uttrycksfullhet än Bitcoin-skript, samtidigt som de bevarar sekretessen för sina data.


## Introduktion till smarta kontrakt och deras status


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


I detta och nästa kapitel kommer vi att titta på begreppet **Smart contract** i RGB-miljön och utforska de olika sätt på vilka dessa kontrakt kan definiera och utveckla sin *status*. Vi kommer att se varför RGB-arkitekturen, med hjälp av den ordnade sekvensen av engångsförseglingar, gör det möjligt att utföra olika typer av ***Contract-operationer*** på ett skalbart sätt och utan att gå igenom ett centraliserat register. Vi kommer också att titta på den grundläggande roll som ***Business Logic*** spelar för att rama in utvecklingen av Contract State.


### Smarta kontrakt och digitala innehavarrättigheter


RGB:s mål är att tillhandahålla en infrastruktur för att implementera smarta kontrakt på Bitcoin. Med "Smart contract" menar vi ett avtal mellan flera parter som verkställs automatiskt och beräkningsmässigt, utan mänsklig inblandning för att verkställa klausulerna. Med andra ord upprätthålls lagen i Contract av programvaran, inte av en betrodd tredje part.


Denna automatisering väcker frågan om decentralisering: hur kan vi frigöra oss från ett centraliserat register (t.ex. en central plattform eller databas) för att hantera Ownership- och Contract-prestanda? Den ursprungliga idén, som togs upp av RGB, är att återgå till ett läge för Ownership som kallas "innehavarinstrument". Historiskt sett utfärdades vissa värdepapper (obligationer, aktier etc.) i innehavarform, vilket gjorde det möjligt för alla som fysiskt innehade dokumentet att hävda sina rättigheter.


![RGB-Bitcoin](assets/fr/055.webp)


RGB tillämpar detta koncept på den digitala världen: rättigheter (och skyldigheter) är inkapslade i data som manipuleras off-chain och statusen för dessa data valideras av deltagarna själva. Detta möjliggör, a priori, en mycket högre grad av konfidentialitet och oberoende än vad som erbjuds av andra metoder som baseras på offentliga register.


### Introduktion till Smart contract RGB status


En Smart contract i RGB kan ses som en tillståndsmaskin, definierad av:




- En **State**, dvs. den uppsättning information som återspeglar den aktuella konfigurationen av Contract;
- En **Business Logic** (uppsättning regler), som beskriver under vilka förhållanden och av vem tillståndet kan ändras.


![RGB-Bitcoin](assets/fr/056.webp)


Det är viktigt att förstå att dessa avtal inte är begränsade till en enkel överföring av tokens. De kan innehålla ett brett utbud av applikationer: från traditionella tillgångar (tokens, aktier, obligationer) till mer komplexa mekaniker (användningsrättigheter, kommersiella villkor etc.). Till skillnad från andra blockkedjor, där Contract-koden är tillgänglig och körbar för alla, avgränsar RGB:s tillvägagångssätt åtkomst och kunskap om Contract till deltagare ("***Contract-deltagare***"). Det finns flera roller:




- Utfärdaren** eller skaparen av Contract, som definierar Genesis av Contract och dess initiala variabler;
- Parter med rättigheter** (*Ownership*) eller andra verkställighetsmöjligheter;
- Observatörer**, potentiellt begränsade till att se viss information, men som inte kan utlösa ändringar.


Denna rollfördelning bidrar till censurresistens genom att säkerställa att endast behöriga personer kan interagera med kontraktsstaten. Det ger också RGB möjlighet att skala horisontellt: majoriteten av valideringarna sker utanför Blockchain, och endast kryptografiska ankare (*åtagandena*) skrivs in på Bitcoin.


### Status och Business Logic i RGB


Ur praktisk synvinkel tar Contract:s **Business Logic** formen av regler och skript, definierade i vad RGB kallar en **Schema**. Schema kodar:




- Statlig struktur (vilka fält är offentliga? Vilka fält ägs av vilka parter?
- Giltighetsvillkor (vad måste kontrolleras innan en statusuppdatering godkänns?);
- Behörigheter (vem kan initiera en *State Transition*? Vem kan bara observera?).


Samtidigt bryts ** Contract State ** ofta ner i två komponenter:




- A **Global State**: offentlig del, potentiellt observerbar av alla (beroende på konfiguration);
- Owned States**: privata delar som tilldelats specifikt till ägare via UTXO:er som det hänvisas till i Contract-logiken.


Som vi kommer att se i de följande kapitlen måste varje statusuppdatering (*Contract Operation*) docka till ett Bitcoin _åtagande_ (via `Opret` eller `Tapret`) och följa *Business Logic*-skript för att anses giltig.


### Contract Verksamhet: statens uppkomst och utveckling


I RGB-universumet är en ***Contract Operation*** en händelse som ändrar Contract från ett **gammalt tillstånd** till ett **nytt tillstånd**. Dessa operationer följer följande logik:




- Vi noterar den aktuella statusen för Contract;
- Vi tillämpar regeln eller operationen (en ***State Transition***, en ***Genesis*** om det är det allra första tillståndet, eller en ***State Extension*** om det finns en offentlig *Valency* att återutlösa);
- Vi Anchor modifieringen via ett nytt _åtagande_ på Blockchain, stänger en _försegling för engångsbruk_ och skapar en annan;
- De berörda rättighetshavarna validerar lokalt (*klientsidan*) att övergången överensstämmer med *Schema* och att den tillhörande Bitcoin-transaktionen är registrerad On-Chain.


![RGB-Bitcoin](assets/fr/057.webp)


Slutresultatet är en uppdaterad Contract, nu med ett annat tillstånd. Denna övergång kräver inte att hela Bitcoin-nätverket bryr sig om detaljerna, eftersom endast ett litet kryptografiskt fingeravtryck (_åtagandet_) registreras i Blockchain. Sekvensen av förseglingar för engångsbruk förhindrar all Double-spending eller dubbelanvändning av tillståndet.


### Verksamhetskedjan: från Genesis till Terminal State


För att sätta detta i perspektiv börjar en RGB Smart contract med en **Genesis**, det allra första tillståndet. Därefter följer olika Contract-operationer på varandra och bildar en DAG (*Directed Acyclic Graph*) av operationer:




- Varje övergång baseras på ett tidigare tillstånd (eller flera, om det rör sig om konvergerande övergångar);
- Den kronologiska ordningen garanteras genom att varje övergång ingår i ett Bitcoin Anchor, tidsstämplat och oföränderligt tack vare konsensus genom Proof-of-Work;
- När inga fler operationer pågår nås ett **Terminaltillstånd**: det senaste och fullständiga tillståndet för Contract.


![RGB-Bitcoin](assets/fr/012.webp)


Denna DAG-topologi (i stället för en enkel linjär kedja) återspeglar möjligheten att olika delar av Contract kan utvecklas parallellt, så länge de inte motsäger varandra. RGB tar sedan hand om att undvika eventuella inkonsekvenser genom *klientsidans* verifiering av varje inblandad deltagare.


### Sammanfattning


Smarta kontrakt i RGB introducerar en modell av digitala innehavarinstrument, decentraliserade men förankrade i Bitcoin för att tidsstämpla och garantera ordningen på transaktioner. Automatiserat utförande av dessa kontrakt baseras på:




- En **Contract State**, som anger den aktuella konfigurationen av Contract (rättigheter, saldon, variabler etc.);
- En **Business Logic** (*Schema*), som definierar vilka övergångar som är tillåtna och hur de måste valideras;
- Contract Operationer**, som uppdaterar detta tillstånd steg för steg, tack vare åtaganden som är förankrade i Bitcoin transaktioner.


I nästa kapitel kommer vi att gå in mer i detalj på den konkreta representationen av dessa ***tillstånd*** och ***tillståndsövergångar*** på off-chain-nivå, och hur de relaterar till UTXO:er och engångsförseglingar som är inbäddade i Bitcoin. Detta kommer att vara en möjlighet att se hur RGB:s interna mekanik, baserad på Client-side Validation, lyckas upprätthålla konsistensen hos smarta kontrakt samtidigt som datakonfidentialiteten bevaras.


## RGB Contract drift


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


I det här kapitlet tittar vi på hur operationer i smarta kontrakt och tillståndsövergångar fungerar, återigen inom RGB-protokollet. Syftet är också att förstå hur flera deltagare samarbetar för att överföra Ownership en tillgång.


### Tillståndsövergångar och deras mekanik


Den allmänna principen är fortfarande den i Client-side Validation, där statliga data innehas av ägaren och valideras av mottagaren. Det specifika här med RGB ligger dock i det faktum att Bob, som mottagare, ber Alice att införliva viss information i Contract-data för att ha verklig kontroll över den mottagna tillgången, via en dold hänvisning till en av hans UTXO:er.


För att illustrera processen för en *State Transition* (som är en av de grundläggande ***Contract-operationerna*** i RGB), låt oss ta ett steg-för-steg-exempel på en tillgångsöverföring mellan Alice och Bob:


**Inledande situation: **


Alice har en ***Stash RGB*** med lokalt validerade data (*klientsidan*). Denna Stash hänvisar till en av hennes UTXO:er på Bitcoin. Detta innebär att en _seal definition_ i dessa data pekar på en UTXO som tillhör Alice. Tanken är att göra det möjligt för henne att överföra vissa digitala rättigheter kopplade till en tillgång (t.ex. RGB-tokens) till Bob.


![RGB-Bitcoin](assets/fr/058.webp)


**Bob har också UTXO:er:**


Bob, å andra sidan, har minst en egen UTXO, utan någon direkt länk till Alice:s. Om Bob inte har någon UTXO är det fortfarande möjligt att göra överföringen till honom med hjälp av själva *Witness Transaction*: resultatet av denna transaktion kommer då att inkludera Commitment (_commitment_) och implicit associera Ownership i den nya Contract med Bob.


![RGB-Bitcoin](assets/fr/059.webp)


**Uppförande av den nya fastigheten (*New State*):**


Bob skickar Alice information kodad i form av en ***Invoice*** (vi kommer att gå in mer i detalj på Invoice-konstruktion i senare kapitel) och ber henne att skapa ett nytt tillstånd som överensstämmer med reglerna i Contract. Detta tillstånd kommer att innehålla en ny *Seal Definition* som pekar på en av Bob:s UTXO:er. På detta sätt får Bob Ownership av de tillgångar som definieras i detta nya tillstånd, till exempel en viss mängd RGB-tokens.


![RGB-Bitcoin](assets/fr/060.webp)


**Förberedelse av transaktionsexemplet: **


Alice skapar sedan en Bitcoin-transaktion som spenderar den UTXO som refererades till i föregående Seal (den som legitimerade henne som innehavare). I resultatet av denna transaktion infogas en *Commitment* (via `Opret` eller `Tapret`) till Anchor det nya RGB-tillståndet. Åtagandena `Opret` eller `Tapret` härleds från ett *MPC-träd* (som vi sett i tidigare kapitel), som kan aggregera flera övergångar från olika kontrakt.


**Överföring av *Consignment* till Bob:**


Innan transaktionen sänds ut skickar Alice en ***Consignment*** till Bob som innehåller alla nödvändiga data från *klientsidan* (hans *Stash*) och den nya statusinformationen till Bob:s fördel. Vid denna tidpunkt tillämpar Bob RGB:s konsensusregler:




- Den validerar alla RGB-data som finns i *Consignment*, inklusive det nya tillståndet som ger den Ownership av tillgången;
- Med hjälp av de *Anchors* som ingår i *Consignment* verifieras kronologin för vittnestransaktioner (från Genesis till den senaste övergången) och motsvarande åtaganden i Blockchain valideras.


**Övergångens slutförande:**


Om Bob är nöjd kan han ge sitt godkännande (t.ex. genom att underteckna *Consignment*). Alice kan sedan sända ut den förberedda provtransaktionen. När detta har bekräftats stängs Seal som tidigare innehades av Alice och Ownership formaliseras av Bob. Anti-Double-spending-säkerheten baseras sedan på samma mekanism som i Bitcoin: UTXO förbrukas, vilket bevisar att Alice inte längre kan återanvända den.


![RGB-Bitcoin](assets/fr/061.webp)


Det nya tillståndet refererar nu till Bob:s UTXO, vilket ger Bob den Ownership som tidigare innehades av Alice. Bitcoin-utgången där RGB-data är förankrade blir det oåterkalleliga beviset på överföringen av Ownership.


Ett exempel på en minimal DAG (*Directed Acyclic Graph*) som omfattar två Contract-operationer (en **Genesis** och sedan en ***State Transition***) kan illustrera hur RGB-tillståndet (*klientsidan* Layer, i rött) ansluter till Bitcoin Blockchain (*Commitment* Layer, i orange).


![RGB-Bitcoin](assets/fr/062.webp)


Den visar att en Genesis definierar en Seal (*Seal Definition*), sedan stänger en *State Transition* denna Seal för att skapa en ny i en annan UTXO.


I det här sammanhanget kommer här några påminnelser om terminologi:




- En ***Assignment*** kombinerar följande:
    - En ***Seal Definition*** (som pekar på en UTXO);
    - Ägda stater**, dvs. uppgifter kopplade till Ownership (t.ex. antalet överförda tokens).
- En **Global State** sammanför de allmänna egenskaperna hos Contract, synlig för alla, och säkerställer den globala konsekvensen av utvecklingar.


**State Transitions**, som beskrivs i föregående kapitel, är den huvudsakliga formen av Contract Operation. De hänvisar till ett eller flera tidigare tillstånd (från Genesis eller en annan State Transition) och uppdaterar dem till ett nytt tillstånd.


![RGB-Bitcoin](assets/fr/063.webp)


Detta diagram visar hur, i en *State Transition Bundle*, flera förseglingar kan stängas i en enda provtransaktion, samtidigt som nya förseglingar öppnas. En intressant egenskap hos RGB-protokollet är dess förmåga att skala: flera övergångar kan aggregeras till en Transition Bundle, där varje aggregering är associerad med ett distinkt blad i *MPC-trädet* (en unik bundle identifier). Tack vare mekanismen *Deterministic Bitcoin Commitment* (DBC) kan hela meddelandet infogas i en `Tapret`- eller `Opret`-utgång, samtidigt som tidigare förseglingar stängs och eventuellt nya definieras. Anchor fungerar som en direktlänk mellan Commitment som lagras i Blockchain och Client-side Validation-strukturen (*klient-sidan*).


I följande kapitel kommer vi att titta på alla komponenter och processer som är involverade i att bygga och validera en State Transition. De flesta av dessa Elements är en del av RGB-konsensus, som implementeras i **RGB Core Library**.


### Transition Bundle


På RGB är det möjligt att bunta ihop olika tillståndsövergångar som tillhör samma Contract (dvs. som delar samma **ContractId**, härlett från Genesis **OpId**). I det enklaste fallet, som mellan Alice och Bob i exemplet ovan, innehåller en **Transition Bundle** bara en övergång. Men stöd för operationer med flera betalare (t.ex. coinjoins, Lightning channel openings etc.) innebär att flera användare kan kombinera sina State Transitions i ett enda paket.


När dessa övergångar har samlats in förankras de (genom MPC + DBC-mekanismen) i en enda Bitcoin-transaktion:




- Varje State Transition är hashad och grupperad i en Transition Bundle;
- Transition Bundle är själv hashad och infogad i MPC-trädbladet som motsvarar denna Contract (ett BundleId);
- MPC-trädet är slutligen engagerat via `Opret` eller `Tapret` i Witness Transaction, som därmed stänger de förbrukade tätningarna och definierar de nya tätningarna.


Tekniskt sett erhålls **BundleId** som infogas i MPC-arket från en taggad Hash som tillämpas på den strikta serialiseringen av buntens *InputMap*-fält:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


I vilken `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` till exempel.


*InputMap* är en datastruktur som för varje input `i` i provtransaktionen listar referensen till *OpId* för motsvarande State Transition. Till exempel


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- `N` är det totala antalet poster i transaktionen som hänvisar till en `OpId`;
- opId(input_j)` är åtgärdsidentifieraren för en av de tillståndsövergångar som finns i paketet.


Genom att hänvisa till varje post endast en gång och på ett ordnat sätt förhindrar vi att samma Seal används två gånger i två samtidiga State Transitions.


### Generering av tillstånd och aktivt tillstånd


State Transitions kan därför användas för att överföra Ownership en tillgång från en person till en annan. De är dock inte de enda möjliga operationerna i RGB-protokollet. Protokollet definierar tre **Contract operationer**:




- State Transition**;
- Genesis**;
- State Extension**.


Bland dessa kallas **Genesis** och **State Extension** ibland för "*State Generation operations*", eftersom de skapar nya tillstånd utan att omedelbart stänga något. Detta är en mycket viktig punkt: **Genesis** och **State Extension** innebär inte att en Seal stängs. Snarare definierar de en ny Seal, som sedan måste spenderas av en efterföljande **State Transition** för att verkligen valideras i Blockchain-historiken.


![RGB-Bitcoin](assets/fr/064.webp)


Det **Aktiva tillståndet** för en Contract definieras ofta som uppsättningen av de senaste tillstånden som härrör från transaktionshistoriken (DAG), med början i Genesis och efter alla ankare i Bitcoin Blockchain. Eventuella gamla tillstånd som redan är föråldrade (dvs. kopplade till förbrukade UTXO:er) anses inte längre vara aktiva, men är fortfarande viktiga för att kontrollera historikens konsistens.


### Genesis


Genesis är startpunkten för varje RGB Contract. Den skapas av utfärdaren av Contract och definierar de initiala parametrarna i enlighet med **Schema**. När det gäller en RGB token kan Genesis till exempel specificera:




- Antalet tokens som ursprungligen skapades och deras ägare;
- Totalt tak för möjliga problem;
- Eventuella regler för återutgivning och vilka deltagare som är berättigade.


Som den första transaktionen i Contract refererar Genesis inte till något tidigare tillstånd, och den stänger inte heller någon Seal. För att visas i historiken och valideras måste dock Genesis **konsumeras** (stängas) av en första State Transition (ofta en skanning/auto-spend-transaktion till själva utfärdaren, eller den första distributionen till användarna).


### State Extension


**State Extensions** erbjuder en originalfunktion för smarta kontrakt. De gör det möjligt att Redeem vissa digitala rättigheter (*Valencies*) som anges i Contract-definitionen, utan att omedelbart stänga Seal. Oftast gäller detta:




- Distribuerade token-problem;
- Mekanismer för tillgångsswappar;
- Villkorade återutgivningar (som kan innefatta förstörelse av andra tillgångar etc.).


Tekniskt sett hänvisar en State Extension till en *Redeem* (en viss typ av RGB-ingång) som motsvarar en *Valency* som definierats tidigare (t.ex. i Genesis eller en annan State Transition). Den definierar en ny Seal, tillgänglig för den person eller det tillstånd som drar nytta av den. För att denna Seal ska träda i kraft måste den användas av en efterföljande State Transition.


![RGB-Bitcoin](assets/fr/065.webp)


Till exempel: Genesis skapar en rätt till utfärdande (*Valency*). Denna kan utövas av en auktoriserad aktör, som sedan bygger en State Extension:




- Det hänvisar till Valency (Redeem);
- Den skapar en ny *Assignment* (nya *Owned State*-data) som pekar på en UTXO;
- En framtida State Transition, utfärdad av ägaren till denna nya UTXO, kommer faktiskt att överföra eller distribuera de nyemitterade tokens.


### Komponenter i en Contract Operation


Jag skulle nu vilja ta en detaljerad titt på var och en av de ingående Elements i en **Contract Operation** i RGB. En Contract Operation är den åtgärd som ändrar tillståndet för en Contract, och som valideras på klientsidan, på ett deterministiskt sätt, av den legitima mottagaren. Vi kommer särskilt att se hur Contract Operation tar hänsyn till å ena sidan det **gamla tillståndet** i Contract och å andra sidan definitionen av ett **nytt tillstånd** .


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


Om vi tittar på diagrammet ovan kan vi se att en Contract Operation innehåller Elements som hänvisar till **New State** och andra som hänvisar till den uppdaterade **Old State**.


Elements i den **nya staten** är:




- Uppdrag**, i vilka definieras:
 - **Seal Definition**;
 - **Owned State**.
- **Global State**, som kan modifieras eller berikas;
- Valencies**, eventuellt definierade i State Transition eller Genesis.


Den **gamla staten** refereras till via:




- Inputs**, som pekar på *Assignments* av tidigare tillståndsövergångar (finns inte i Genesis);
- Redeems**, som hänvisar till tidigare definierade Valencies (endast i State Extensions).


Dessutom innehåller en Contract Operation mer allmänna fält som är specifika för verksamheten:




- `ffv` (*Fast-forward version*): heltal på 2 byte som anger Contract-versionen;
- `transitionType` eller `ExtensionType`: 16-bitars heltal som anger övergångs- eller förlängningstyp enligt Business Logic;
- `ContractId`: 32-bytesnummer som hänvisar till *OpId* för Contract Genesis. Ingår i Transitions and Extensions, men inte i Genesis;
- schemaId: finns endast i Genesis, detta är den 32-byte Hash som representerar strukturen (*Schema*) i Contract;
- `Testnet`: Boolean som anger om du befinner dig i Testnet- eller Mainnet-nätverket. Endast Genesis;
- altlayers1: variabel som identifierar det alternativa Layer (Sidechain eller annat) som används för Anchor-data utöver Bitcoin. Endast närvarande i Genesis;
- metadata: fält som kan lagra tillfällig information som är användbar för att validera en komplex Contract, men som inte får registreras i den slutliga statushistoriken.


Slutligen kondenseras alla dessa fält genom en anpassad hashprocess för att producera ett unikt fingeravtryck, `OpId`. Detta `OpId` integreras sedan i Transition Bundle, vilket gör att den kan autentiseras och valideras inom protokollet.


Varje *Contract Operation* identifieras därför av en 32-byte Hash med namnet `OpId`. Denna Hash beräknas genom en SHA256 Hash av alla de Elements som utgör operationen. Med andra ord har varje *Contract Operation* sin egen kryptografiska Commitment, som innehåller alla de uppgifter som behövs för att verifiera transaktionens äkthet och konsekvens.


En RGB Contract identifieras sedan av ett `ContractId`, som härleds från Genesis `OpId` (eftersom det inte finns någon operation före Genesis). Konkret tar vi Genesis:s `OpId`, vänder byteordningen och tillämpar en Base58-kodning. Denna kodning gör `ContractId` lättare att hantera och känna igen.

### Metoder och regler för statusuppdateringar


**Contract State** representerar den uppsättning information som RGB-protokollet måste spåra för en given Contract. Den består av följande:




- En enda Global State**: detta är den offentliga, globala delen av Contract som är synlig för alla;
- En eller flera ägda stater**: varje Owned State är förknippad med en unik Seal (och därför en UTXO på Bitcoin). En åtskillnad görs mellan:
    - De **offentligt** ägda staterna,
    - De **privat** ägda staterna.


![RGB-Bitcoin](assets/fr/066.webp)


*Global State* ingår direkt i *Contract Operation* som ett enda block. De *ägda staterna* definieras i varje *Assignment*, tillsammans med *Seal Definition*.


En viktig egenskap hos RGB är det sätt på vilket Global State och Owned States modifieras. Det finns i allmänhet två typer av beteende:




- Mutable**: När ett tillståndselement beskrivs som mutable, ersätter varje ny operation det tidigare tillståndet med ett nytt tillstånd. De gamla uppgifterna anses då vara föråldrade;
- Ackumulerande**: När ett tillståndselement definieras som ackumulerande, lägger varje ny operation till ny information till det tidigare tillståndet, utan att skriva över den. Resultatet blir en slags ackumulerad historia.


Om ett tillståndselement i Contract inte definieras som föränderligt eller kumulativt kommer detta element att förbli tomt för efterföljande operationer (med andra ord finns det inga nya versioner för detta fält). Det är Contract Schema (dvs. den kodade Business Logic) som avgör om ett tillstånd (globalt eller eget) är föränderligt, kumulativt eller fast. När Genesis har definierats kan dessa egenskaper endast ändras om Contract själv tillåter det, t.ex. via en specifik State Extension.


Tabellen nedan visar hur varje typ av Contract Operation kan manipulera (eller inte manipulera) Global State och Owned State:


|                              | Genesis | State Extension | State Transition |
| ---------------------------- |:-----: |:-------------: |:--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`**: åtgärd möjlig om Contract:s Schema tillåter det.


**`-`**: åtgärden måste bekräftas av en efterföljande State Transition (enbart State Extension stänger inte Single-Use Seal).


Dessutom kan den tidsmässiga omfattningen och uppdateringsrättigheterna för varje typ av data särskiljas i följande tabell:


|                        | Metadata                                | Global State                                     | Owned State                                                                                              |
| ---------------------- | --------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Scope**              | Defined for a single Contract Operation | Defined globally for the contract                | Defined for each seal (*Assignment*)                                                                     |
| **Who can update it?** | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)        | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction) |
| **Temporal Scope**     | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


Global State beskrivs ofta som "ingen äger, alla vet". Den innehåller allmän information om Contract, som är allmänt synlig. I en token-utfärdande Contract innehåller den till exempel potentiellt:




- Tickern (symbolisk förkortning av token): `ticker`;
- Det fullständiga namnet på token: `namn`;
- Precision (antal decimaler): `precision`;
- Initialt erbjudande (och/eller maximal token-gräns): utfärdade leveranser;
- Utgivningsdatum: "skapad";
- Rättsliga uppgifter eller annan offentlig information: "data".


Denna Global State kan placeras på offentliga resurser (webbplatser, IPFS, Nostr, Torrent, etc.) och distribueras till samhället. Dessutom driver det ekonomiska incitamentet (behovet av att inneha och överföra dessa tokens etc.) naturligtvis Contract-användare att själva underhålla och sprida dessa data.


### Uppdrag


*Assignment* är den grundläggande strukturen för att definiera:




- Seal (*Seal Definition*), som pekar på en specifik UTXO;
- *Owned State*, dvs. den egenskap eller de data som är kopplade till denna Seal.


En *Assignment* kan ses som en motsvarighet till en Bitcoin transaktionsutskrift, men med större flexibilitet. Häri ligger logiken för överföring av egendom: *Assignment* associerar en viss typ av tillgång eller rättighet (`AssignmentType`) med en Seal. Den som innehar den privata nyckeln till den UTXO som är kopplad till denna Seal (eller den som kan spendera denna UTXO) anses vara ägare till denna *Owned State*.


En av RGB:s stora styrkor ligger i möjligheten att *avslöja* eller dölja (*koncepera*) fälten *Seal Definition* och *Owned State* efter behag. Detta ger en kraftfull kombination av sekretess och selektivitet. Du kan t.ex. bevisa att en övergång är giltig utan att avslöja alla data genom att tillhandahålla den avslöjade versionen till den person som måste validera den, medan tredje part endast ser den dolda versionen (en Hash). I praktiken beräknas alltid `OpId` för en övergång från de *dolda* uppgifterna.


![RGB-Bitcoin](assets/fr/067.webp)


#### Seal Definition


*Seal Definition*, i sin avslöjade form, har fyra grundläggande fält: `txptr`, `vout`, `blinding` och `method`:




- txptr**: detta är en referens till en UTXO på Bitcoin:
    - När det gäller en **Genesis Seal** pekar den direkt på en befintlig UTXO (den som är associerad med Genesis);
    - I fallet med en **Graph Seal** kan vi ha:
        - En enkel `txid`, om den pekar på en specifik UTXO,
        - Eller en `WitnessTx`, som betecknar en självreferens: Seal pekar på själva transaktionen. Detta är särskilt användbart när ingen extern UTXO finns tillgänglig, t.ex. vid öppningstransaktioner för blixtkanaler, eller om mottagaren inte har någon UTXO.
- vout**: Utgångsnummer för den transaktion som anges av `txptr`. Finns endast för en standardgraf Seal (inte för `WitnessTx`);
- blinding**: ett slumpmässigt tal på 8 byte, för att förstärka sekretessen och förhindra brute force-försök på UTXO:s identitet;
- method**: anger den förankringsmetod som används (`Tapret` eller `Opret`).


Den * dolda* formen av Seal Definition är en SHA256 Hash (taggad) av sammankopplingen av dessa 4 fält, med en tagg som är specifik för RGB.


![RGB-Bitcoin](assets/fr/068.webp)


#### Ägda stater


Den andra komponenten i *Assignment* är Owned State. Till skillnad från Global State kan den existera i offentlig eller privat form:




- Public Owned State**: alla känner till de data som är kopplade till Seal. Till exempel en offentlig bild;
- Private Owned State**: uppgifterna är dolda och endast kända av ägaren (och eventuellt valideraren vid behov). Till exempel antalet tokens som innehas.


RGB definierar fyra möjliga tillståndstyper (*StateTypes*) för en Owned State:




- Deklarativ**: innehåller inga numeriska data, utan bara en deklarativ rättighet (t.ex. rösträtt). Den dolda och den avslöjade formen är identiska;
- Fungible**: representerar en fungibel kvantitet (som polletter). I avslöjad form har vi `amount` och `blinding`. I dold form har vi en enda *Pedersen commitment* som döljer beloppet och blindningen;
- Structured**: lagrar strukturerad data (upp till 64 kB). I avslöjad form är det datablobben. I dold form är det en taggad Hash av denna blob:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


Med, till exempel:


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- Attachments**: länkar en fil (ljud, bild, binär etc.) till Owned State och lagrar filen Hash `file_hash`, MIME-typen `media type` och ett kryptografiskt salt `salt`. Själva filen är hostad någon annanstans. I dold form är det en Hash som är taggad med de tre föregående dataposterna:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


Med, till exempel:


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


Sammanfattningsvis är här de 4 möjliga typerna av tillstånd i den offentliga och dolda formen:


```txt
State                      Concealed form                              Revealed form

+---------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+

```



| **Element**     | **Declarative** | **Fungible**                      | **Structured**       | **Attachments**        |
| --------------- | --------------- | --------------------------------- | -------------------- | ---------------------- |
| **Data**        | None            | Signed or unsigned 64-bit integer | Any strict data type | Any file               |
| **Info Type**   | None            | Signed or unsigned                | Strict types         | MIME Type              |
| **Privacy**     | Not required    | Pedersen commitment               | Hash with blinding   | Hashed file identifier |
| **Size Limits** | N/A             | 256 bytes                         | Up to 64 KB          | Up to ~500 GB          |


### Ingångar


Ingångarna i en *Contract Operation* hänvisar till de *Attribut* som används i denna nya verksamhet. En Ingång indikerar:




- prevOpId: Identifieraren (OpId) för den föregående åtgärd där *Assignment* fanns;
- `assignmentType`: typ av *Assignment* (t.ex. `assetOwner` för en token);
- index: Index för *Assignment* i den lista som är kopplad till föregående `OpId`, fastställt efter en lexikografisk sortering av de dolda sigillen.


Ingångar förekommer aldrig i Genesis, eftersom det inte finns några tidigare Tilldelningar. De förekommer inte heller i delstatsutvidgningar (eftersom delstatsutvidgningar inte avslutar förseglingar, utan snarare omdefinierar nya förseglingar baserat på valenser).


När vi har Owned States av typen `Fungible` kontrollerar valideringslogiken (via skriptet AluVM som tillhandahålls i Schema) att summorna är konsekventa: summan av inkommande tokens (*Inputs*) måste vara lika med summan av utgående tokens (i de nya *Assignments*).


### Metadata


Fältet **Metadata** kan vara upp till 64 KiB och används för att inkludera tillfälliga data som är användbara för validering, men som inte är integrerade i Contract:s permanenta tillstånd. Här kan t.ex. mellanliggande beräkningsvariabler för komplexa skript lagras. Detta utrymme är inte avsett att lagras i den globala historiken, vilket är anledningen till att det ligger utanför tillämpningsområdet för Owned States eller Global State.


### Valenser


**Valencies** är en ursprunglig RGB protokollmekanism. De kan hittas i Genesis, State Transitions eller State Extensions. De representerar numeriska rättigheter som kan aktiveras av en State Extension (via *Redeems*) och sedan slutföras av en efterföljande Transition. Varje Valency identifieras av en `ValencyType` (16 bitar). Dess semantik (återutgivningsrätt, token-swap, burn right, etc.) definieras i Schema.


I konkreta termer kan vi tänka oss att en Genesis definierar en "rätt att återutge" Valency. En State Extension kommer att konsumera den (*Redeem*) om vissa villkor är uppfyllda, för att introducera en ny mängd tokens. Sedan kan en State Transition som härrör från innehavaren av den Seal som skapats på detta sätt överföra dessa nya tokens.


### Löser in


Redeems är Valency:s motsvarighet till Inputs för Assignments. De förekommer endast i State Extensions, eftersom det är där en tidigare definierad Valency aktiveras. En Redeem består av två fält:




- `PrevOpId`: `OpId` för den åtgärd där Valency specificerades;
- `ValencyType`: den typ av Valency som du vill aktivera (varje `ValencyType` kan endast användas en gång av State Extension).


Exempel: en Redeem kan motsvara en CoinSwap-körning, beroende på vad som kodades i Valency.


### RGB status egenskaper


Vi ska nu ta en titt på flera grundläggande tillståndsegenskaper i RGB. I synnerhet kommer vi att titta på:




- **Strict Type System**, som föreskriver en exakt och typad organisation av data;
- Vikten av att skilja **validering** från **Ownership**;
- Systemet **konsensusutveckling** i RGB, som innehåller begreppen *fast-forward* och *push-back*.


Som alltid ska du komma ihåg att allt som har att göra med Contract-status valideras på klientsidan enligt konsensusregler som anges i protokollet, och vars ultimata kryptografiska referens är förankrad i Bitcoin-transaktioner.


#### Strikt typsystem


RGB använder ett *Strikt typsystem* och ett deterministiskt serialiseringsläge (*Strikt kodning*). Denna organisation är utformad för att garantera perfekt reproducerbarhet och precision i definitionen, hanteringen och valideringen av Contract-data.


I många programmeringsmiljöer (JSON, YAML ...) kan datastrukturen vara flexibel, till och med för tillåtande. I RGB, å andra sidan, definieras strukturen och typerna för varje fält med uttryckliga begränsningar. Till exempel




- Varje variabel har en specifik typ (t.ex. ett 8-bitars osignerat heltal `u8`, eller ett 16-bitars signerat heltal, etc;)
- Typer kan vara sammansatta (nästlade typer). Det innebär att du kan definiera en typ baserat på andra typer (t.ex. en aggregerad typ som innehåller ett `u8`-fält, ett `bool`-fält etc.);
- Samlingar kan också anges: listor (*list*), set (*set*) eller dictionaries (*map*), med en deterministisk ordningsföljd;
- Varje fält är avgränsat (*nedre gräns* / *övre gräns*). Vi sätter också gränser för antalet Elements i samlingar (containment);
- Data är byte-alignerade och serialisering är strikt definierad och entydig.


Tack vare detta strikta kodningsprotokoll:




- Ordningen på fälten är alltid densamma, oavsett vilken implementation eller vilket programmeringsspråk som används;
- De hashar som beräknas på samma datamängd är därför reproducerbara och identiska (strikt deterministiska *åtaganden*);
- Gränser förhindrar okontrollerad tillväxt av datastorleken (t.ex. för många fält);
- Denna form av kodning underlättar kryptografisk verifiering, eftersom varje deltagare vet exakt hur data ska serialiseras och Hash.


I praktiken sammanställs strukturen (*Schema*) och den resulterande koden (*Interface* och tillhörande logik). Ett beskrivande språk används för att definiera Contract (typer, fält, regler) och generate ett strikt binärt format. Vid kompileringen blir resultatet:




- En *Memory Layout* för varje fält;
- Semantiska identifierare (som anger om en ändring av ett variabelnamn påverkar logiken, även om minnesstrukturen förblir densamma).


Det strikta typsystemet möjliggör också exakt övervakning av ändringar: varje ändring av strukturen (till och med en ändring av fältnamnet) kan upptäckas och kan leda till en ändring av det totala fotavtrycket.


Slutligen ger varje kompilering ett fingeravtryck, en kryptografisk identifierare som intygar den exakta versionen av koden (data, regler, validering). Till exempel en identifierare av formen:


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


Detta gör det möjligt att hantera uppdateringar av konsensus eller implementering, samtidigt som man säkerställer detaljerad spårbarhet av de versioner som används i nätverket.


För att förhindra att tillståndet för en RGB Contract blir för besvärligt att validera på klientsidan, föreskriver en konsensusregel en maximal storlek på `2^16` byte (64 Kio) för alla data som är involverade i valideringsberäkningar. Detta gäller för varje variabel eller struktur: inte mer än 65536 byte, eller motsvarande i siffror (32768 16-bitars heltal etc.). Detta gäller även för samlingar (listor, set, maps), som inte får överstiga `2^16` Elements.


Denna gräns garanterar:




- Styr den maximala storleken på data som ska manipuleras under en State Transition;
- Kompatibilitet med den virtuella maskin (*AluVM*) som används för att köra valideringsskripten.


#### Valideringen != Ownership paradigm


En av RGB:s stora innovationer är den strikta separationen mellan två koncept:




- Validering**: kontroll av att en State Transition följer reglerna i Contract (Business Logic, historik, etc.);
- **Ownership** (Ownership, eller kontroll): det faktum att man äger Bitcoin UTXO som gör att Single-Use Seal kan spenderas (eller stängas), och därmed att State Transition kan äga rum.


**Validering** sker på nivån för RGB:s programvarustack (bibliotek, protokoll för *åtaganden*, etc.). Dess roll är att säkerställa att de interna reglerna i Contract (belopp, behörigheter, etc.) respekteras. Observatörer eller andra deltagare kan också validera datahistoriken.


**Ownership**, å andra sidan, är helt beroende av Bitcoin:s säkerhet. Att äga den privata nyckeln till en UTXO innebär att man kontrollerar möjligheten att starta en ny övergång (stänga Single-Use Seal). Så även om någon kan se eller validera data kan de inte ändra tillståndet om de inte äger den berörda UTXO.


![RGB-Bitcoin](assets/fr/069.webp)


Detta tillvägagångssätt begränsar de klassiska sårbarheter som förekommer i mer komplexa blockkedjor (där all kod i en Smart contract är offentlig och kan ändras av vem som helst, vilket ibland har lett till hackningar). På RGB kan en angripare inte bara interagera med On-Chain-tillståndet, eftersom rätten att agera på tillståndet (*Ownership*) skyddas av Bitcoin Layer.


Dessutom gör denna frikoppling att RGB kan integreras naturligt med Lightning Network. Lightning-kanaler kan användas för att engagera och flytta RGB-tillgångar utan att engagera On-Chain *engagemang* varje gång. Vi kommer att titta närmare på denna integration av RGB på Lightning i senare kapitel av kursen.


#### Utveckling av samförstånd i RGB


Förutom versionering av semantiska koder innehåller RGB ett system för att utveckla eller uppdatera en Contract:s konsensusregler över tid. Det finns två huvudsakliga former av utveckling:




- Snabbspolning**
- Push-back** (på franska)


En fast-forward inträffar när en tidigare ogiltig regel blir giltig. Till exempel, om Contract utvecklas för att tillåta en ny typ av `AssignmentType` eller ett nytt fält:




- Detta kan inte jämföras med en klassisk Blockchain hardfork, eftersom RGB fungerar i Client-side Validation och inte påverkar den övergripande kompatibiliteten hos Blockchain;
- I praktiken indikeras denna typ av ändring av fältet `Ffv` (*fast-forward version*) i Contract Operation;
- Nuvarande innehavare skadas inte: deras status förblir giltig;
- Nya förmånstagare (eller nya användare) måste å andra sidan uppdatera sin programvara (sin Wallet) för att känna igen de nya reglerna.


En push-back innebär att en tidigare giltig regel blir ogiltig. Det är därför en "härdning" av reglerna, men inte i strikt mening en softfork:




- Befintliga innehavare kan komma att påverkas (de kan komma att ha tillgångar som blir föråldrade eller ogiltiga i den nya versionen);
- Vi kan tänka oss att vi i själva verket skapar ett nytt protokoll: den som antar den nya regeln frångår den gamla;
- Utgivaren kan besluta att återutge tillgångar i det nya protokollet, vilket tvingar användarna att ha två separata plånböcker (en för det gamla protokollet och en för det nya) om de vill hantera båda versionerna.


I detta kapitel om RGB Contract-operationer har vi utforskat de grundläggande principerna bakom detta protokoll. Som du säkert har märkt kräver den inneboende komplexiteten i RGB-protokollet att många tekniska termer används. I nästa kapitel kommer jag därför att ge dig en ordlista som sammanfattar alla begrepp som tas upp i den här första teoretiska delen, med definitioner av alla tekniska termer som rör RGB. Sedan, i nästa avsnitt, tar vi en praktisk titt på definitionen och implementeringen av RGB-kontrakt.


## RGB Ordlista


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


Om du behöver komma tillbaka till den här korta ordlistan med viktiga tekniska termer som används i RGB-världen (listade i alfabetisk ordning) kommer du att ha nytta av den. Det här kapitlet är inte nödvändigt om du redan har förstått allt vi har gått igenom i det första avsnittet.


#### AluVM


Förkortningen AluVM står för "_Algorithmic logic unit Virtual Machine_", en registerbaserad virtuell maskin utformad för Smart contract-validering och distribuerad databehandling. Den används (men är inte uteslutande reserverad) för validering av RGB-kontrakt. Skript eller operationer som ingår i ett RGB Contract kan således köras i AluVM-miljön.


För ytterligare information: [AluVM officiella webbplats](https://www.AluVM.org/)


#### Anchor


En Anchor representerar en uppsättning data på klientsidan som används för att bevisa att en unik _commitment_ ingår i en transaktion. I RGB-protokollet består en Anchor av följande Elements:




- Bitcoin-transaktionsidentifieraren (txid) för **Witness Transaction**;
- Den **Multi Protocol Commitment (MPC)**;
- Den **Deterministic Bitcoin Commitment (DBC)**;
- **Extra Transaction Proof (ETP)** om mekanismen **Tapret** Commitment används (se avsnittet om denna modell).


En Anchor tjänar därför till att upprätta en verifierbar länk mellan en specifik Bitcoin-transaktion och privata data som validerats av RGB-protokollet. Det garanterar att dessa data verkligen ingår i Blockchain, utan att deras exakta innehåll exponeras offentligt.


#### Assignment


I RGB:s logik är en Assignment motsvarigheten till en transaktionsutgång som modifierar, uppdaterar eller skapar vissa egenskaper inom tillståndet för en Contract. En Assignment består av två Elements:




- A **Seal Definition** (hänvisning till en specifik UTXO);
- En **Owned State** (uppgifter som beskriver den stat som är kopplad till den nya ägaren).


En Assignment anger därför att en del av staten (t.ex. en tillgång) nu är allokerad till en viss innehavare, identifierad via en Single-Use Seal kopplad till en UTXO.


#### Business Logic


Business Logic grupperar alla regler och interna operationer i en Contract, som beskrivs av dess **Schema** (dvs. strukturen i själva Contract). Den dikterar hur Contract:s tillstånd kan utvecklas och under vilka förhållanden.


#### Client-side Validation


Client-side Validation hänvisar till den process genom vilken varje part (klient) verifierar en uppsättning data som utbyts privat, enligt reglerna i ett protokoll. När det gäller RGB grupperas dessa utbytta data i vad som kallas **sändningar**. Till skillnad från Bitcoin-protokollet, som kräver att alla transaktioner publiceras On-Chain, tillåter RGB endast att _commitments_ (förankrade i Bitcoin) lagras offentligt, medan den väsentliga Contract-informationen (transitions, attestations, proofs) förblir off-chain, delad endast mellan de berörda användarna.


#### Commitment


En Commitment (i kryptografisk mening) är ett matematiskt objekt, betecknat `C`, som härleds deterministiskt från en operation på strukturerad data `m` (meddelandet) och ett slumpmässigt värde `r`. Vi skriver:


$$
C = \text{commit}(m, r)
$$


Denna mekanism består av två huvudsakliga operationer:




- Commit**: En kryptografisk funktion tillämpas på ett meddelande `m` och ett slumpmässigt tal `r` för att producera `C`;
- Verify**: vi använder `C`, `m`-meddelandet och `r`-värdet för att kontrollera att denna Commitment är korrekt. Funktionen returnerar `True` eller `False`.


En Commitment måste respektera två egenskaper:




- Binding**: det måste vara omöjligt att hitta två olika meddelanden som ger samma `C`:


$$
m': \, | \,: m' \neq m \quad \text{and} \quad r': \, | \,: r' \neq r \quad
$$


Som till exempel:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Hiding**: Kunskap om `C` får inte avslöja innehållet i `m`.


I RGB-protokollet ingår en Commitment i en Bitcoin-transaktion för att bevisa att en viss information finns vid en viss tidpunkt, utan att avslöja själva informationen.


#### Consignment


En **Consignment** grupperar de uppgifter som utbyts mellan parterna, med förbehåll för Client-side Validation i RGB. Det finns två huvudkategorier av Consignment:




- Contract Consignment**: tillhandahålls av *utfärdaren* (Contract issuer) och innehåller initialiseringsinformation såsom Schema, Genesis, Interface och Interface Implementation.
- Överföring Consignment**: tillhandahålls av den betalande parten (*betalaren*). Den innehåller hela historiken av tillståndsövergångar som leder fram till Terminal Consignment (dvs. det slutliga tillstånd som betalaren har mottagit).


Dessa sändningar registreras inte offentligt på Blockchain utan utväxlas direkt mellan de berörda parterna via den kommunikationskanal de själva väljer.


#### Contract


En Contract är en uppsättning rättigheter som verkställs digitalt mellan flera aktörer via RGB-protokollet. Den har ett aktivt tillstånd och en Business Logic, definierad av en Schema, som anger vilka operationer som är auktoriserade (överföringar, anknytningar etc.). Tillståndet för en Contract, liksom dess giltighetsregler, uttrycks i Schema. Vid varje given tidpunkt utvecklas Contract endast i enlighet med vad som tillåts av denna Schema och av valideringsskript (som t.ex. körs i AluVM).


#### Contract Operation


En Contract Operation är en Contract statusuppdatering som utförs enligt Schema regler. Följande operationer finns i RGB:




- State Transition**;
- Genesis**;
- State Extension**.


Varje operation ändrar tillståndet genom att lägga till eller ersätta vissa data (Global State, Owned State...).


#### Contract Participant


En Contract Participant är en aktör som deltar i operationer som rör Contract. I RGB görs en åtskillnad mellan:




- Utfärdaren av Contract, som skapar Genesis (ursprunget till Contract);
- Contract-parterna, dvs. innehavarna av rättigheter till Contract:s tillstånd;
- Offentliga parter, som kan bygga State Extensions om Contract erbjuder Valencies som är tillgängliga för allmänheten.


#### Contract Rights


Contract Rights hänvisar till de olika rättigheter som kan utövas av dem som är inblandade i en RGB Contract. De kan delas in i flera kategorier:




- Ownership-rättigheter**, associerade med Ownership för en viss UTXO (via en _Seal Definition_);
- Verkställande rättigheter**, dvs. möjligheten att bygga en eller flera övergångar (State Transitions) i enlighet med Schema;
- Offentliga rättigheter**, när Schema tillåter vissa offentliga användningar, till exempel skapandet av en State Extension genom inlösen av en Valency.


#### Contract State


Contract State motsvarar det aktuella tillståndet för en Contract vid en given tidpunkt. Den kan bestå av både offentliga och privata data, som återspeglar tillståndet för Contract. RGB gör åtskillnad mellan:




- **Global State**, som innehåller Contract:s offentliga egenskaper (konfigurerade i Genesis eller tillagda via auktoriserade uppdateringar);
- Owned States**, som tillhör specifika ägare, identifierade genom sina UTXO.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment (DBC) är den uppsättning regler som används för att bevisligen och unikt registrera en _commitment_ i en Bitcoin-transaktion. I RGB-protokollet finns det två huvudformer av DBC:




- Opret**
- Tapret**


Dessa mekanismer definierar exakt hur _åtagandet_ kodas i utdata eller struktur för en Bitcoin-transaktion, för att säkerställa att denna Commitment är deterministiskt spårbar och verifierbar.


#### Directed Acyclic Graph - DAG


En DAG (eller *Acyclic Guided Graph*) är en cykelfri graf som möjliggör topologisk schemaläggning. Blockkedjor, som _shards_ i RGB-kontrakt, kan representeras av DAG:ar.


För ytterligare information: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### Gravyr


Gravyr är en valfri datasträng som efterföljande ägare av en Contract kan ange i Contract-historiken. Denna funktion finns t.ex. i **RGB21** Interface och gör det möjligt att lägga till minnes- eller beskrivningsinformation i Contract-historiken.


#### Extra transaktionsbevis - ETP


ETP (*Extra Transaction Proof*) är den del av Anchor som innehåller de ytterligare data som krävs för att validera en **Tapret** *Commitment* (i samband med _taproot_). Den innehåller bland annat Taproot-skriptets interna offentliga nyckel (_internal PubKey_) och information som är specifik för _Script Path Spend_.


#### Genesis


Genesis hänvisar till den uppsättning data, styrd av en Schema, som utgör det initiala tillståndet för alla Contract i RGB. Det kan jämföras med Bitcoin:s _Genesis Block_-koncept, eller med Coinbase Transaction-konceptet, men här på _klientsidan_- och RGB token-nivå.


#### Global State


Global State är den uppsättning offentliga egenskaper som ingår i Contract State. Den definieras i Genesis och kan, beroende på Contract-reglerna, uppdateras av auktoriserade övergångar. Till skillnad från Owned States tillhör Global State inte en viss enhet, utan ligger närmare ett offentligt register inom Contract.


#### Interface


Interface är den uppsättning instruktioner som används för att avkoda binärdata som sammanställts i en Schema eller i Contract-operationer och deras tillstånd, för att göra dem läsbara för användaren eller hans Wallet. Den fungerar som en tolkning Layer.


#### Interface Implementation


Interface Implementation är den uppsättning deklarationer som länkar en **Interface** till en **Schema**. Den möjliggör den semantiska översättning som utförs av Interface själv, så att rådata i en Contract kan förstås av användaren eller den programvara som är inblandad (plånböckerna).


#### Invoice


En Invoice har formen av en URL kodad i [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), som innehåller de uppgifter som krävs för att skapa en **State Transition** (av betalaren). Med andra ord är det en Invoice som gör det möjligt för motparten (*betalaren*) att skapa motsvarande övergång för att överföra tillgången eller uppdatera tillståndet för Contract.


#### Lightning Network


Lightning Network är ett decentraliserat nätverk av betalningskanaler (eller _statskanaler_) på Bitcoin, som består av 2/2 plånböcker med flera signaturer. Det möjliggör snabba, billiga _off-chain_-transaktioner, samtidigt som det förlitar sig på Bitcoin:s Layer 1 för skiljedom (eller stängning) vid behov.


För mer information om hur Lightning fungerar rekommenderar jag att du går den här andra kursen:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment (MPC) hänvisar till Merkle Tree-strukturen som används i RGB för att, inom en enda Bitcoin-transaktion, inkludera flera **Transition Bundles** från olika kontrakt. Tanken är att gruppera ihop flera åtaganden (som potentiellt motsvarar olika kontrakt eller olika tillgångar) i en enda Anchor-punkt för att optimera utnyttjandet av blockutrymme.


#### Owned State


En Owned State är den del av en Contract State som är innesluten i en Assignment och associerad med en viss innehavare (via en Single-Use Seal som pekar på en UTXO). Detta representerar t.ex. en digital tillgång eller en specifik avtalsenlig rättighet som tilldelats den personen.


#### Ownership


Ownership avser möjligheten att kontrollera och spendera en UTXO som refereras av en Seal Definition. När en Owned State är länkad till en UTXO har ägaren till denna UTXO potentiell rätt att överföra eller utveckla det associerade tillståndet, enligt reglerna för Contract.


#### Partially Signed Bitcoin Transaction - PSBT


En PSBT (_Partially Signed Bitcoin Transaction_) är en Bitcoin-transaktion som ännu inte är fullständigt signerad. Den kan delas mellan flera enheter, som var och en kan lägga till eller verifiera vissa Elements (signaturer, skript ...), tills transaktionen anses vara redo för On-Chain-distribution.


För ytterligare information: [BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)


#### Pedersen commitment


En Pedersen commitment är en typ av kryptografisk Commitment med egenskapen att vara **homomorf** med avseende på additionsoperationen. Detta innebär att det är möjligt att validera summan av två åtaganden utan att avslöja de individuella värdena.


Formellt sett, om:


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


...då:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Denna egenskap är till exempel användbar för att dölja mängden tokens som utbyts, samtidigt som det fortfarande går att verifiera totalsummorna.


Ytterligare information: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


I en State Extension hänvisar en Redeem till åtgärden att återkräva (eller utnyttja) en tidigare deklarerad **Valency**. Eftersom en Valency är en allmän rättighet tillåter Redeem en auktoriserad deltagare att göra anspråk på en specifik Contract State Extension.


#### Schema


En Schema i RGB är en deklarativ koddel som beskriver uppsättningen variabler, regler och Business Logic (*Business Logic*) som styr driften av en Contract. Schema definierar tillståndsstrukturen, de typer av övergångar som tillåts och valideringsvillkoren.


#### Seal Definition


Seal Definition är den del av en Assignment som associerar _åtagandet_ med en UTXO som ägs av den nya innehavaren. Med andra ord anger den var villkoret är beläget (i vilken UTXO) och etablerar Ownership för en tillgång eller rättighet.


#### Shard


En Shard representerar en gren i DAG för tillståndsövergångarnas historik för en RGB Contract. Med andra ord är det en sammanhängande delmängd av Contract:s övergripande historik, som till exempel motsvarar den sekvens av övergångar som krävs för att bevisa giltigheten av en viss tillgång sedan _Genesis_.


#### Single-Use Seal


En Single-Use Seal är ett kryptografiskt löfte om Commitment till ett ännu okänt meddelande, som kommer att avslöjas endast en gång i framtiden och som måste vara känt av alla medlemmar i en specifik publik. Syftet är att förhindra att det skapas flera konkurrerande åtaganden för samma Seal.


#### Stash


Stash är den uppsättning data på klientsidan som en användare lagrar för ett eller flera RGB-kontrakt, i syfte att validera (*Client-side Validation*). Detta inkluderar övergångshistorik, sändningar, giltighetsbevis, etc. Varje innehavare behåller endast de delar av historiken som de behöver (*shards*).


#### State Extension


En State Extension är en Contract Operation som används för att återutlösa statusuppdateringar genom att lösa in tidigare deklarerade **Valencies**. För att vara effektiv måste en State Extension sedan stängas av en State Transition (som uppdaterar det slutliga tillståndet för Contract).


#### State Transition


State Transition är den operation som ändrar tillståndet för en RGB Contract till ett nytt tillstånd. Den kan modifiera Global State och/eller Owned State data. I praktiken verifieras varje övergång av Schema-regler och förankras i Bitcoin Blockchain via ett _commitment_.


#### Taproot


Hänvisar till Bitcoin:s SegWit v1 transaktionsformat, introducerat av [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) och [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot förbättrar sekretessen och flexibiliteten för skript, i synnerhet genom att göra transaktioner mer kompakta och svårare att skilja från varandra.


#### Terminal Consignment - Consignment Endpoint


Terminal Consignment (eller _Consignment Endpoint_) är en *överförings-Consignment* som innehåller det slutliga tillståndet för Contract, inklusive State Transition som skapats från mottagarens Invoice (*betalningsmottagare*). Det är därför slutpunkten för en överföring, med nödvändiga data för att bevisa att Ownership eller tillstånd har överförts.


#### Transition Bundle


En Transition Bundle är en uppsättning RGB State Transitions (som hör till samma Contract) som alla är engagerade i samma ***Witness Transaction*** Bitcoin. Detta gör det möjligt att samla flera uppdateringar eller överföringar i en enda On-Chain Anchor.


#### UTXO


En Bitcoin UTXO (*Unspent Transaction Output*) definieras av Hash för en transaktion och utgångsindexet (*vout*). Det kallas också ibland för en _outpoint_. I RGB-protokollet möjliggör en referens till en UTXO (via en **Seal Definition**) lokaliseringen av **Owned State**, dvs. den egendom som finns på Blockchain.


#### Valency


En Valency är en allmän rättighet som inte kräver statlig lagring som sådan, men som kan lösas in via en **State Extension**. Det är därför en form av möjlighet som är öppen för alla (eller vissa spelare), förklarad i logiken för Contract, för att genomföra en viss utökning vid ett senare tillfälle.


#### Witness Transaction


Witness Transaction är den Bitcoin-transaktion som stänger Single-Use Seal runt ett meddelande som innehåller en Multi Protocol Commitment (MPC). Denna transaktion spenderar en UTXO eller skapar en, så att Seal Commitment kopplas till RGB-protokollet. Den fungerar som ett On-Chain bevis på att tillståndet har ställts in vid en viss tidpunkt.


# Programmering på RGB


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## Implementering av RGB-avtal


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


I detta kapitel tar vi en närmare titt på hur en RGB Contract definieras och implementeras. Vi kommer att se vilka komponenterna i en RGB Contract är, vilka roller de har och hur de är konstruerade.


### Komponenterna i en RGB Contract


Hittills har vi redan diskuterat **Genesis**, som utgör startpunkten för en Contract, och vi har sett hur den passar in i logiken för en *Contract Operation* och protokollets status. Den fullständiga definitionen av en RGB Contract är dock inte begränsad till enbart Genesis: den omfattar tre kompletterande komponenter som tillsammans utgör hjärtat i implementeringen.


Den första komponenten kallas **Schema**. Detta är en fil som beskriver den grundläggande strukturen och Business Logic (*Business Logic*) för Contract. Den specificerar de datatyper som används, valideringsreglerna, de operationer som är tillåtna (t.ex. initial token-utfärdande, överföringar, särskilda villkor etc.) - kort sagt, det allmänna ramverk som dikterar hur Contract fungerar.


Den andra komponenten är **Interface**. Den fokuserar på hur användare (och i förlängningen portföljprogramvara) kommer att interagera med denna Contract. Den beskriver semantiken, d.v.s. den läsbara representationen av de olika fälten och åtgärderna. Så medan Schema definierar hur Contract fungerar tekniskt, definierar Interface hur man presenterar och exponerar dessa funktioner: metodnamn, datavisning etc.


Den tredje komponenten är **Interface Implementation**, som kompletterar de två föregående genom att fungera som en slags brygga mellan Schema och Interface. Med andra ord associerar den den semantik som uttrycks av Interface med de underliggande regler som definieras i Schema. Det är denna implementering som kommer att hantera t.ex. konverteringen mellan en parameter som anges i Wallet och den binära struktur som protokollet föreskriver, eller kompileringen av valideringsregler i maskinspråk.


Denna modularitet är en intressant egenskap hos RGB, eftersom den gör det möjligt för olika grupper av utvecklare att arbeta separat med dessa aspekter (*Schema*, *Interface*, *Implementation*), så länge de följer protokollets konsensusregler.


Sammanfattningsvis består varje Contract av:




- Genesis**, som är det initiala tillståndet för Contract (och kan liknas vid en särskild transaktion som definierar den första Ownership av en tillgång, en rättighet eller någon annan parameteriserbar data);
- Schema**, som beskriver Contract:s Business Logic (datatyper, valideringsregler etc.);
- Interface**, som ger en semantisk Layer för både plånböcker och mänskliga användare, vilket förtydligar läsning och utförande av transaktioner;
- Implementering** Interface, som överbryggar gapet mellan Business Logic och presentation, för att säkerställa att Contract-definitionen överensstämmer med användarupplevelsen.


![RGB-Bitcoin](assets/fr/070.webp)


Det är viktigt att notera att för att en Wallet ska kunna hantera en RGB-tillgång (vare sig det är en fungibel token eller en rättighet av något slag), måste den ha alla dessa Elements sammanställda: *Schema*, *Interface*, *Interface Implementation* och *Genesis*. Detta överförs via en ***Contract Consignment***, dvs. ett datapaket som innehåller allt som behövs för att validera Contract på klientsidan.


För att hjälpa till att klargöra dessa begrepp finns här en sammanfattande tabell som jämför komponenterna i en RGB Contract med begrepp som redan är kända antingen inom objektorienterad programmering (OOP) eller i Ethereums ekosystem:


| RGB Contract Component       | Meaning                        | OOP Equivalent                                     | Ethereum Equivalent                |
| ---------------------------- | ------------------------------ | -------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | Initial state of the contract  | Class constructor                                  | Contract constructor               |
| **Schema**                   | Business logic of the contract | Class                                              | Contract                           |
| **Interface**                | Semantics of the contract      | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                       |
| **Interface Implementation** | Mapping semantics and logic    | Impl (Rust) / Implements (Java)                    | Application Binary Interface (ABI) |


Den vänstra kolumnen visar Elements som är specifik för RGB-protokollet. I mittenkolumnen visas den konkreta funktionen för varje komponent. I kolumnen "OOP equivalent" hittar vi sedan den motsvarande termen i objektorienterad programmering:




- **Genesis** spelar en roll som liknar den för en *Klasskonstruktör*: det är här Contract:s tillstånd initialiseras;
- **Schema** är beskrivningen av en klass, d.v.s. definitionen av dess egenskaper, metoder och underliggande logik;
- **Interface** motsvarar *interfaces* (Java), *traits* (Rust) eller *protocols* (Swift): dessa är de offentliga definitionerna av funktioner, händelser, fält...;
- **Interface Implementation** motsvarar *Impl* i Rust eller *Implements* i Java, där vi anger hur koden faktiskt kommer att utföra de metoder som anges i Interface.


I Ethereum-sammanhang är Genesis närmare *Contract-konstruktören*, Schema är Contract-definitionen, Interface är en standard som ERC-20 eller ERC-721 och Interface Implementation är ABI (*Application Binary Interface*), som anger formatet för interaktioner med Contract.


Fördelen med RGB:s modularitet ligger också i det faktum att olika intressenter kan skriva, till exempel, sin egen Interface Implementation, så länge de respekterar logiken i *Schema* och semantiken i *Interface*. En emittent skulle således kunna utveckla en ny, mer användarvänlig front-end (Interface) utan att ändra logiken i Contract, eller omvänt, man skulle kunna utöka Schema för att lägga till funktionalitet och tillhandahålla en ny version av den anpassade Interface Implementation, medan de gamla implementeringarna skulle förbli giltiga för grundläggande funktionalitet.


När vi sammanställer en ny Contract, generate vi en Genesis (det första steget i att utfärda eller distribuera tillgången), samt dess komponenter (Schema, Interface, Interface Implementation). Efter detta är Contract i full drift och kan spridas till plånböcker och användare. Denna metod, där Genesis kombineras med dessa tre komponenter, garanterar en hög grad av anpassning (varje Contract kan ha sin egen logik), decentralisering (alla kan bidra till en viss komponent) och säkerhet (validering förblir strikt definierad av protokollet, utan att vara beroende av godtycklig on-chain code som ofta är fallet på andra blockkedjor).


Jag skulle nu vilja titta närmare på var och en av dessa komponenter: **Schema**, **Interface** och **Interface Implementation**.


### Schema


I föregående avsnitt såg vi att i ekosystemet RGB består en Contract av flera Elements: Genesis, som fastställer det initiala tillståndet, och flera andra kompletterande komponenter. Syftet med Schema är att deklarativt beskriva alla Business Logic i Contract, dvs. datastrukturen, de typer som används, de tillåtna operationerna och deras villkor. Det är därför ett mycket viktigt element för att göra en Contract operativ på klientsidan, eftersom varje deltagare (t.ex. en Wallet) måste kontrollera att de tillståndsövergångar som den tar emot överensstämmer med den logik som definieras i Schema.


En Schema kan liknas vid en "klass" i objektorienterad programmering (OOP). Generellt sett fungerar den som en modell som definierar komponenterna i en Contract, t.ex:




- De olika typerna av Owned States och Assignments;
- Valencies, d.v.s. särskilda rättigheter som kan utlösas (*inlösas*) för vissa transaktioner;
- Global State-fält, som beskriver globala, offentliga och delade egenskaper hos Contract;
- Genesis-strukturen (den allra första åtgärden som aktiverar Contract);
- De tillåtna formerna av State Transitions och State Extensions och hur dessa operationer kan modifiera ;
- Metadata som är kopplade till varje operation, för att lagra tillfällig eller ytterligare information;
- Regler som bestämmer hur interna Contract-data kan utvecklas (t.ex. om ett fält är föränderligt eller kumulativt);
- Sekvenser av operationer som anses giltiga: t.ex. en ordning av övergångar som ska respekteras eller en uppsättning logiska villkor som ska uppfyllas.


![RGB-Bitcoin](assets/fr/071.webp)


När *utgivaren* av en tillgång på RGB publicerar en Contract, tillhandahåller den Genesis och Schema som är associerade med den. Användare eller plånböcker som vill interagera med tillgången hämtar denna Schema för att förstå logiken bakom Contract och för att senare kunna verifiera att de övergångar de kommer att delta i är legitima.


Det första steget, för alla som får information om en RGB-tillgång (t.ex. en token-överföring), är att validera denna information mot Schema. Detta innebär att använda Schema-sammanställningen för att:




- Kontrollera att Owned States, Assignments och andra Elements är korrekt definierade och att de följer de föreskrivna typerna (det så kallade *strikta typsystemet*);
- Kontrollera att övergångsreglerna (valideringsskript) uppfylls. Dessa skript kan köras via AluVM, som finns på klientsidan och ansvarar för att validera överensstämmelsen med Business Logic (överföringsbelopp, särskilda villkor etc.).


I praktiken är Schema inte körbar kod, vilket kan ses i blockkedjor som lagrar på chain code (EVM på Ethereum). Tvärtom separerar RGB Business Logic (deklarativ) från körbar kod på Blockchain (som är begränsad till kryptografiska ankare). Schema fastställer således reglerna, men tillämpningen av dessa regler sker utanför Blockchain, på varje deltagares webbplats, enligt principen i Client-side Validation.


En Schema måste kompileras innan den kan användas av RGB-applikationer. Denna kompilering producerar en binär fil (t.ex. `.RGB`) eller en krypterad binär fil (`.rgba`). När Wallet importerar den här filen vet den:




- Hur varje datatyp (heltal, strukturer, arrayer ...) ser ut tack vare det strikta typsystemet;
- Hur Genesis bör struktureras (för att förstå initiering av tillgångar);
- De olika typerna av operationer (State Transitions, State Extensions) och hur de kan modifiera tillståndet;
- De skriptregler (introducerade i Schema) som AluVM-motorn kommer att tillämpa för att kontrollera giltigheten av operationer.


Som förklarats i tidigare kapitel ger *strikt typsystem* oss ett stabilt, deterministiskt kodningsformat: alla variabler, oavsett om det är Owned States, Global States eller Valencies, beskrivs exakt (storlek, nedre och övre gränser vid behov, signerad eller osignerad typ etc.) Det är också möjligt att definiera nästlade strukturer, t.ex. för att stödja komplexa användningsfall.


Eventuellt kan Schema referera till en rot `SchemaId`, vilket underlättar återanvändningen av en befintlig grundstruktur (en mall). På så sätt kan du utveckla en Contract eller skapa variationer (t.ex. en ny typ av token) från en redan beprövad mall. Denna modularitet undviker behovet av att återskapa hela kontrakt och uppmuntrar till standardisering av bästa praxis.


En annan viktig punkt är att logiken för tillståndsutveckling (överföringar, uppdateringar etc.) beskrivs i Schema i form av skript, regler och villkor. Så om Contract-designern vill auktorisera en nyutgivning eller införa en brännmekanism (förstörelse av tokens), kan han specificera motsvarande skript för AluVM i valideringsdelen av Schema.


#### Skillnad från programmerbara On-Chain-blockkedjor


Till skillnad från system som Ethereum, där Smart contract-koden (körbar) skrivs in i själva Blockchain, lagrar RGB Contract (dess logik) off-chain, i form av ett kompilerat deklarativt dokument. Detta innebär att:




- Det finns ingen Turing-komplett VM som körs i varje nod i Bitcoin-nätverket. Reglerna för en RGB Contract exekveras inte på Blockchain, utan i varje användare som vill validera ett tillstånd;
- Contract-data förorenar inte Blockchain: endast kryptografiska bevis (*åtaganden*) är inbäddade i Bitcoin-transaktioner (via `Tapret` eller `Opret`);
- Schema kan uppdateras eller avvisas (*fast-forward*, *push-back*, etc.), utan att kräva en Fork på Bitcoin Blockchain. Plånböckerna behöver helt enkelt importera den nya Schema och anpassa sig till konsensusändringar.


#### Användning av emittenten och av användarna


När en *utfärdare* skapar en tillgång (t.ex. en icke-inflatorisk fungibel token), förbereder den sig:




- En Schema som beskriver reglerna för utsläpp, överföring etc;
- En Genesis som är anpassad till denna Schema (med det totala antalet utgivna polletter, den ursprungliga ägarens identitet, eventuella särskilda valenser för återutgivning etc.).


Den gör sedan den kompilerade Schema (en `.RGB`-fil) tillgänglig för användare, så att alla som tar emot en överföring av denna token kan kontrollera att operationen är konsekvent lokalt. Utan denna Schema skulle en användare inte kunna tolka statusdata eller kontrollera att de överensstämmer med Contract-reglerna.


Så när en ny Wallet vill stödja en tillgång behöver den helt enkelt integrera den relevanta Schema. Denna mekanism gör det möjligt att lägga till kompatibilitet för nya RGB-tillgångstyper utan att invasivt ändra Wallet:s programvarubas: allt som krävs är att importera Schema-binären och förstå dess struktur.


Schema definierar Business Logic i RGB. Den listar utvecklingsreglerna för en Contract, strukturen för dess data (ägda stater, Global State, valenser) och de associerade valideringsskripten (körbara av AluVM). Tack vare detta deklarativa dokument är definitionen av en Contract (kompilerad fil) tydligt åtskild från det faktiska utförandet av reglerna (klientsidan). Denna frikoppling ger RGB stor flexibilitet, vilket möjliggör ett brett spektrum av användningsfall (fungibla tokens, NFT, mer sofistikerade kontrakt) samtidigt som man undviker den komplexitet och de brister som är typiska för programmerbara On-Chain-blockkedjor.


#### Schema exempel


Låt oss ta en titt på ett konkret exempel på Schema för en RGB Contract. Detta är ett utdrag i Rust från filen `nia.rs` (initialer för "*Non-Inflatable Assets*"), som definierar en modell för fungibla tokens som inte kan återutges utöver deras ursprungliga Supply (en icke-inflatorisk tillgång). Denna typ av token kan ses som motsvarigheten, i RGB-universumet, till ERC20 på Ethereum, dvs. fungibla tokens som respekterar vissa grundläggande regler (t.ex. för överföringar, Supply-initialisering etc.).


Innan du dyker in i koden är det värt att komma ihåg den allmänna strukturen för en RGB Schema. Det finns en serie deklarationer som ramar in:




- Ett möjligt `SchemaId` som anger användningen av en annan grundläggande Schema som mall;
- **Globala stater** och **ägda stater** (med deras strikta typer);
- Valencer** (om sådana finns);
- De **Operationer** (Genesis, State Transitions, State Extensions) som kan referera till dessa tillstånd och valenser;
- Det **Strict Type System** som används för att beskriva och validera data;
- Valideringsskript** (körs via AluVM).


![RGB-Bitcoin](assets/fr/072.webp)


Koden nedan visar den fullständiga definitionen av Rust Schema. Vi kommer att kommentera den del för del, enligt kommentarerna (1) till (9) nedan:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {

// definitions of libraries and variables

// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),

// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},

// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},

// ===== PART 5: Valencies =====
valency_types: none!(),

// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},

// ===== PART 7: Extensions =====
extensions: none!(),

// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},

// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - Funktionshuvud och SubSchema**


Funktionen `nia_schema()` returnerar ett `SubSchema`, vilket indikerar att denna Schema delvis kan ärva från en mer generisk Schema. I RGB-ekosystemet gör denna flexibilitet det möjligt att återanvända vissa standard-Elements från en master-Schema och sedan definiera regler som är specifika för Contract i fråga. Här väljer vi att inte aktivera arv, eftersom `subset_of` kommer att vara `None`.




- (2) - Allmänna egenskaper: ffv, subset_of, type_system**


Egenskapen `ffv` motsvarar *fast-forward*-versionen av Contract. Ett värde på `noll!()` här anger att vi befinner oss i version 0 eller den första versionen av denna Schema. Om du senare vill lägga till nya funktioner (ny typ av operation, etc.), kan du inkrementera denna version för att ange en konsensusändring.


Egenskapen `subset_of: None" bekräftar att det inte finns någon nedärvning. Fältet `type_system` hänvisar till det strikta typsystem som redan definierats i biblioteket `types`. Denna rad anger att alla data som används av Contract använder den strikta serialiseringsimplementering som tillhandahålls av biblioteket i fråga.




- (3) - Globala stater


I blocket `global_types` deklarerar vi fyra Elements. Vi använder nyckeln, till exempel `GS_NOMINAL` eller `GS_ISSUED_SUPPLY`, för att referera till dem senare:




- `GS_NOMINAL` hänvisar till en `DivisibleAssetSpec`-typ, som beskriver olika fält i den skapade token (fullständigt namn, ticker, precision...);
- `GS_DATA` representerar allmänna data, t.ex. en friskrivningsklausul, metadata eller annan text;
- `GS_TIMESTAMP` hänvisar till ett utgivningsdatum;
- `GS_ISSUED_SUPPLY` anger det totala Supply, dvs. det maximala antalet tokens som kan skapas.


Nyckelordet `once(...)` betyder att vart och ett av dessa fält bara kan förekomma en gång.




- (4) - Ägda typer


I `owned_types` deklarerar vi `OS_ASSET`, som beskriver ett fungibelt tillstånd. Vi använder `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, vilket indikerar att mängden tillgångar (tokens) lagras som ett 64-bitars osignerat heltal. Således kommer varje transaktion att skicka ett visst antal enheter av denna token, som kommer att valideras enligt denna strikt typade numeriska struktur.




- (5) - **Valency**


Vi anger `valency_types: none!()`, vilket innebär att det inte finns några valenser i denna Schema, med andra ord inga speciella eller extra rättigheter (såsom återutgivning, villkorlig bränning, etc.). Om en Schema innehöll några sådana skulle de deklareras i detta avsnitt.




- (6) - Genesis: första operationerna


Här kommer vi in på den del som förklarar Contract Operations. Genesis beskrivs av:




- Avsaknaden av `metadata` (fältet `metadata: Ty::<SemId>::UNIT.id(None)`);
- Globala tillstånd som måste vara närvarande en gång vardera (`Once`);
- En uppdragslista där `OS_ASSET` måste förekomma `En gång eller flera gånger`. Detta innebär att Genesis kräver minst en `OS_ASSET` Assignment (en första innehavare);
- Nej Valency: `valencies: none!()`.


Det är så här vi begränsar definitionen av den första token-utgivningen: vi måste deklarera den Supply som utfärdats (`GS_ISSUED_SUPPLY`), plus minst en innehavare (en Owned State av typen `OS_ASSET`).




- (7) - Förlängningar


Fältet `extensions: none!()` anger att ingen State Extension förutses i denna Contract. Detta innebär att det inte finns någon åtgärd för att Redeem en digital rättighet (Valency) eller för att utföra en State Extension före en övergång. Allt görs via Genesis eller tillståndsövergångar.




- (8) - Övergångar: TS_TRANSFER


I `transitions` definierar vi operationstypen `TS_TRANSFER`. Vi förklarar det:




- Den har inga metadata;
- Den ändrar inte Global State (som redan är definierad i Genesis);
- Den tar en eller flera `OS_ASSETs` som input. Detta innebär att den måste spendera befintliga Owned States;
- Det skapar (`assignments`) minst en ny `OS_ASSET` (med andra ord, mottagaren eller mottagarna får tokens);
- Det genererar ingen ny Valency.


Detta modellerar beteendet hos en grundläggande överföring, som förbrukar tokens på en UTXO, sedan skapar nya Owned States till förmån för mottagarna och därmed bevarar jämlikheten i det totala beloppet mellan inmatningar och utmatningar.




- (9) - AluVM-skript och ingångspunkter** (på franska)


Slutligen deklarerar vi ett AluVM-skript (`Script::AluVM(AluScript { ... })`). Detta skript innehåller:




- Ett eller flera externa bibliotek (`libs`) som ska användas under valideringen;
- Ingångspunkter som pekar på funktionsoffsets i AluVM-koden, motsvarande validering av Genesis (`ValidateGenesis`) och varje deklarerad Transition (`ValidateTransition(TS_TRANSFER)`).


Denna valideringskod är ansvarig för att tillämpa Business Logic. Till exempel kommer den att kontrollera:




- Att `GS_ISSUED_SUPPLY` inte överskrids under Genesis;
- Att summan av `inputs` (förbrukade tokens) är lika med summan av `assignments` (mottagna tokens) för `TS_TRANSFER`.


Om dessa regler inte följs kommer övergången att betraktas som ogiltig.


Detta exempel på en "*Inte uppblåsbar fungibel tillgång*" Schema ger oss en bättre förståelse för strukturen hos en enkel RGB fungibel token Contract. Vi kan tydligt se separationen mellan databeskrivning (globala och ägda stater), operationsdeklaration (Genesis, övergångar, tillägg) och valideringsimplementering (AluVM-skript). Tack vare denna modell beter sig en token som en klassisk fungibel token, men förblir validerad på klientsidan och är inte beroende av On-Chain-infrastrukturen för att exekvera sin kod. Endast kryptografiska åtaganden är förankrade i Bitcoin Blockchain.


### Interface


Interface är den Layer som utformats för att göra en Contract läsbar och manipulerbar, både av användare (mänsklig läsning) och av portföljer (programvaruläsning). Interface spelar därför en roll som kan jämföras med en Interface i ett objektorienterat programmeringsspråk (Java, Rust trait, etc.), genom att den exponerar och klargör den funktionella strukturen hos en Contract, utan att nödvändigtvis avslöja de interna detaljerna hos Business Logic.


Till skillnad från Schema, som är rent deklarativ och kompilerad till en binär fil som är svår att använda som den är, tillhandahåller Interface de läsnycklar som behövs för att:




- Lista och beskriv de globala stater och ägda stater som ingår i Contract;
- Få tillgång till namn och värden för varje fält så att de kan visas (t.ex. för en token, ta reda på dess ticker, högsta belopp etc;)
- Tolka och konstruera Contract-operationer (Genesis, State Transition eller State Extension) genom att associera data med begripliga namn (t.ex. utföra en överföring genom att tydligt ange "belopp" i stället för en binär identifierare).


![RGB-Bitcoin](assets/fr/073.webp)


Tack vare Interface kan du t.ex. skriva kod i en Wallet som, istället för att manipulera fält, direkt manipulerar etiketter som "antal tokens", "tillgångsnamn", etc. På så sätt blir hanteringen av en Contract mer intuitiv. På detta sätt blir hanteringen av Contract mer intuitiv.


#### Allmän drift


Denna metod har många fördelar:




- Standardisering:**


Samma typ av Contract kan stödjas av en standard Interface, som delas mellan flera Wallet-implementeringar. Detta underlättar kompatibilitet och återanvändning av kod.




- Tydlig åtskillnad mellan Schema och Interface:**


I RGB-designen är Schema (Business Logic) och Interface (presentation och manipulation) två oberoende enheter. De utvecklare som skriver logiken för Contract kan koncentrera sig på Schema utan att bekymra sig om ergonomi eller datarepresentation, medan ett annat team (eller samma team, men med en annan tidslinje) kan utveckla Interface.




- Flexibel utveckling:**


Interface kan modifieras eller läggas till efter att tillgången har utfärdats, utan att Contract själv behöver ändras. Detta är en stor skillnad mot vissa On-Chain Smart contract-system, där Interface (ofta blandad med exekveringskoden) är fryst i Blockchain.




- Multi-Interface-kapacitet


Samma Contract kan exponeras genom olika gränssnitt som är anpassade till olika behov: en enkel Interface för slutanvändaren, en annan mer avancerad för utgivaren som behöver hantera komplexa konfigurationsåtgärder. Wallet kan sedan välja vilken Interface som ska importeras, beroende på dess användning.


![RGB-Bitcoin](assets/fr/074.webp)


I praktiken, när Wallet hämtar en RGB Contract (via en `.RGB` eller `.rgba`-fil), importerar den också den tillhörande Interface, som också kompileras. Vid körning kan Wallet t.ex:




- Bläddra i listan över stater och läs deras namn för att visa Ticker, Initial Amount, Issue Date etc. på användarens Interface, i stället för en oläslig numerisk identifierare;
- Bygg en operation (t.ex. en överföring) med hjälp av explicita parameternamn: istället för att skriva `assignments { OS_ASSET => 1 }` kan den erbjuda användaren ett "Amount"-fält i ett formulär och översätta denna information till de strikt typade fält som Contract förväntar sig.


#### Skillnad från Ethereum och andra system


På Ethereum härleds Interface (som beskrivs via ABI, *Application Binary Interface*) i allmänhet från On-Chain:s lagrade kod (Smart contract). Det kan vara kostsamt eller komplicerat att modifiera en specifik del av Interface utan att röra själva Contract. RGB är dock baserad på en helt och hållet off-chain-logik, med data förankrade i *åtaganden* på Bitcoin. Denna design gör det möjligt att modifiera Interface (eller dess implementering) utan att påverka den grundläggande säkerheten i Contract, eftersom valideringen av affärsreglerna kvarstår i Schema och den refererade AluVM-koden.


#### Interface sammanställning


Precis som med Schema definieras Interface i källkod (ofta i Rust) och kompileras till en `.RGB`- eller `.rgba`-fil. Denna binärfil innehåller all information som krävs av Wallet för att:




- Identifiera fält med namn;
- Koppla varje fält (och dess värde) till den strikta systemtyp som definieras i Contract;
- Känna till de olika tillåtna operationerna och hur man bygger dem.


När Interface har importerats kan Wallet visa Contract på rätt sätt och föreslå interaktioner för användaren.


### Gränssnitt som standardiserats av LNP/BP-associationen


I RGB-ekosystemet används en Interface för att ge en läsbar och manipulerbar innebörd till data och operationer i en Contract. Interface kompletterar därmed Schema, som beskriver Business Logic internt (strikta typer, valideringsskript etc.). I det här avsnittet tittar vi på de standardgränssnitt som utvecklats av LNP/BP Association för vanliga Contract-typer (fungible tokens, NFT, etc.).


Som en påminnelse är tanken att varje Interface beskriver hur man visar och manipulerar en Contract på Wallet-sidan, med tydlig namngivning av fälten (t.ex. `spec`, `ticker`, `issuedSupply`...) och definition av möjliga operationer (t.ex. `Transfer`, `Burn`, `Rename`...). Flera gränssnitt är redan i drift, men det kommer att bli fler och fler i framtiden.


#### Några färdiga gränssnitt att använda


**RGB20** är Interface för fungibla tillgångar, vilket kan jämföras med Ethereums ERC20-standard. Den går dock ett steg längre och erbjuder mer omfattande funktionalitet:




- Till exempel möjligheten att byta namn på tillgången (ändring av *ticker* eller fullständigt namn) efter att den har emitterats, eller att justera dess precision (*aktiesplit*);
- Den kan också beskriva mekanismer för sekundär återutgivning (begränsad eller obegränsad) och för förstöring och sedan ersättning, i syfte att ge emittenten rätt att förstöra och sedan återskapa tillgångar under vissa förutsättningar;


RGB20 Interface kan t.ex. länkas till **Non-Inflatable Asset (NIA)-systemet**, som inför en icke-inflatable initial Supply, eller till andra mer avancerade system efter behov.


**RGB21** gäller avtal av NFT-typ, eller mer allmänt, allt unikt digitalt innehåll, såsom representation av digitala medier (bilder, musik etc.). Förutom att beskriva utfärdandet och överföringen av en enda tillgång innehåller den funktioner som:




- Integrerat stöd för direkt inkludering av en fil (upp till 16 MB) i Contract (för hämtning på klientsidan);
- Möjligheten för ägaren att ange en "*engravering*" i historiken för att bevisa tidigare Ownership av en NFT.


**RGB25** är en hybridstandard som kombinerar fungibla och icke-fungibla aspekter. Den är utformad för delvis fungibla tillgångar, såsom tokenisering av fastigheter, där du vill dela upp en fastighet samtidigt som du behåller en länk till en enda rottillgång (med andra ord har du fungibla delar av ett hus, länkade till ett icke-fungibelt hus). Tekniskt sett kan denna Interface länkas till **Collectible Fungible Asset* (CFA)** Schema, som tar hänsyn till begreppet uppdelning samtidigt som den ursprungliga tillgången spåras.


#### Gränssnitt under utveckling


Andra gränssnitt planeras för mer specialiserade användningsområden, men är ännu inte tillgängliga:




- RGB22**, tillägnad digitala identiteter, för att hantera identifierare och On-Chain-profiler i RGB-ekosystemet;
- RGB23**, för avancerad tidsstämpling, som använder några av idéerna från *Opentimestamps*, men med spårbarhetsfunktioner;
- RGB24**, som syftar till att motsvara ett decentraliserat domännamnssystem (DNS) liknande *Ethereum Name Service*;
- RGB26**, utformad för att hantera DAO:er (*Decentralized Autonomous Organization*) i ett mer komplext format (styrning, röstning etc.);
- RGB30**, mycket lik RGB20 men med den speciella egenskapen att den tar hänsyn till decentraliserad initial emission och använder State Extensions. Detta skulle användas för tillgångar vars återutgivning hanteras av flera enheter, eller som omfattas av finare villkor.


Beroende på vilket datum du läser den här kursen kan dessa gränssnitt naturligtvis redan vara i drift och tillgängliga.


#### Interface exempel


Denna Rust-kodsnutt visar en [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (fungibel tillgång). Den här koden är hämtad från filen `rgb20.rs` i standardbiblioteket RGB. Låt oss ta en titt på den för att förstå strukturen hos en Interface och hur den utgör en bro mellan, å ena sidan, Business Logic (definierad i Schema) och, å andra sidan, de funktioner som exponeras för plånböcker och användare.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());

Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


I denna Interface ser vi likheter med Schema-strukturen: vi hittar en deklaration av Global State, Owned States, Contract Operations (Genesis och Transitions), samt felhantering. Men Interface fokuserar på presentation och manipulation av dessa Elements för en Wallet eller någon annan applikation.


Skillnaden mot Schema ligger i typens natur. Schema använder strikta typer (t.ex. `FungibleType::Unsigned64Bit`) och mer tekniska identifierare. Interface använder fältnamn, makron (`fname!()`, `tn!()`) och referenser till argumentklasser (`ArgSpec`, `OwnedIface::Rights`...). Syftet här är att underlätta den funktionella förståelsen och organisationen av Elements för Wallet.


Dessutom kan Interface introducera ytterligare funktionalitet till den grundläggande Schema (t.ex. hantering av en `burnEpoch`-rättighet), så länge som detta förblir förenligt med den slutliga validerade logiken på klientsidan. AluVM:s "skript"-avsnitt i Schema kommer att säkerställa kryptografisk validitet, medan Interface beskriver hur användaren (eller Wallet) interagerar med dessa tillstånd och övergångar.


#### Global State och uppdrag


I avsnittet `global_state` hittar vi fält som `spec` (tillgångsbeskrivning), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Det här är fält som Wallet kan läsa och presentera. Till exempel




- `spec` visar konfigurationen för token;
- `issuedSupply` eller `burnedSupply` ger oss det totala antalet tokens som utfärdats eller bränts, etc.


I avsnittet `assignments` definierar vi olika roller eller rättigheter. Till exempel




- `assetOwner` motsvarar innehav av polletter (det är den fungibla *Owned State*);
- `burnRight` motsvarar möjligheten att bränna polletter;
- updateRight` motsvarar rätten att byta namn på tillgången.


Nyckelordet `public` eller `private` (t.ex. `AssignIface::public(...)`) anger om dessa tillstånd är synliga (`public`) eller konfidentiella (`private`). När det gäller `Req::NoneOrMore`, `Req::Optional`, anger de den förväntade förekomsten.


#### Genesis och övergångar


Delen `Genesis` beskriver hur tillgången initieras:




- Fälten `spec`, `data`, `created`, `issuedSupply` är obligatoriska (`ArgSpec::required()`);
- Tilldelningar som `assetOwner` kan finnas i flera kopior (`ArgSpec::many()`), vilket gör att tokens kan distribueras till flera ursprungliga innehavare;
- Fält som `inflationAllowance` eller `burnEpoch` kan (eller kan inte) ingå i Genesis.


Sedan, för varje Transition (`Transfer`, `Issue`, `Burn`...), definierar Interface vilka fält som operationen förväntar sig som input, vilka fält som operationen kommer att producera som output, och eventuella fel som kan uppstå. Till exempel


**Transition:**




- Ingångar: `previous` → måste vara en `assetOwner`;
- Tilldelningar: `beneficiary` → kommer att vara en ny `assetOwner`;
- Fel: `NON_EQUAL_AMOUNTS` (Wallet kommer alltså att kunna hantera fall där inmatningssumman inte motsvarar utmatningssumman).


**Transition `Issue`:**




- Valfritt (`optional: true`), eftersom ytterligare utsläpp inte nödvändigtvis är aktiverade;
- Ingångar: `used` → en `inflationAllowance`, d.v.s. tillåtelse att lägga till fler tokens;
- Tilldelningar: `beneficiary` (nya mottagna polletter) och `future` (återstående `inflationAllowance`);
- Möjliga fel: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.


**Brännövergång:**




- Ingångar: `used` → a `burnRight`;
- Globals: `burnedSupply` krävs;
- Uppdrag: `future` → en möjlig fortsättning på `burnRight` om vi inte har bränt allt;
- Felaktigheter: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.


Varje operation beskrivs därför på ett sätt som är läsbart för en Wallet. Detta gör det möjligt att visa en grafisk Interface där användaren tydligt kan se: "Du har rätt att bränna. Skulle du vilja bränna en viss mängd? Koden vet att den ska fylla i ett `burnedSupply`-fält och kontrollera att `burnRight` är giltig.


Sammanfattningsvis är det viktigt att komma ihåg att en Interface, hur komplett den än är, inte i sig själv definierar den interna logiken i Contract. Hjärtat av arbetet utförs av **Schema**, som inkluderar strikta typer, Genesis-struktur, övergångar och så vidare. Interface exponerar helt enkelt dessa Elements på ett mer intuitivt och namngivet sätt, för användning i en applikation.


Tack vare RGB:s modularitet kan Interface uppgraderas (t.ex. genom att lägga till en `Rename`-övergång, korrigera visningen av ett fält etc.) utan att behöva skriva om hela Contract. Användare av denna Interface kan sedan omedelbart dra nytta av dessa förbättringar, så snart de uppdaterar filen `.RGB` eller `.rgba`.


Men när du har deklarerat en Interface måste du länka den till motsvarande Schema. Detta görs via ***Interface Implementation***, som anger hur varje namngivet fält (t.ex. `fname!("assetOwner")`) ska mappas till det strikta ID (t.ex. `OS_ASSET`) som definieras i Schema. Detta säkerställer, till exempel, att när en Wallet manipulerar ett `burnRight`-fält, är detta det tillstånd som i Schema beskriver möjligheten att bränna tokens.


### Interface Implementation


I RGB-arkitekturen har vi sett att varje komponent (Schema, Interface, etc.) kan utvecklas och kompileras oberoende av varandra. Det finns dock fortfarande ett oumbärligt element som länkar samman dessa olika byggstenar: ***Interface Implementation***. Det är detta som explicit mappar de identifierare eller fält som definieras i Schema (på Business Logic-sidan) till de namn som deklareras i Interface (på presentations- och användarinteraktionssidan). Så när en Wallet laddar en Contract kan den förstå exakt vilket fält som motsvarar vad, och hur en operation som namnges i Interface relaterar till logiken i Schema.


En viktig punkt är att Interface Implementation inte nödvändigtvis är avsedd att exponera alla Schema-funktionaliteter eller alla Interface-fält: den kan begränsas till en delmängd. I praktiken gör detta det möjligt att begränsa eller filtrera vissa aspekter av Schema. Du kan t.ex. ha en Schema med fyra typer av operationer, men en Implementation Interface som endast mappar två av dem i ett givet sammanhang. Omvänt, om en Interface föreslår ytterligare slutpunkter, kan vi välja att inte implementera dem här.


Här är ett klassiskt exempel på Interface Implementation, där vi associerar en *Non-Inflatable Asset* (NIA) Schema med RGB20 Interface:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();

IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


I denna Implementation Interface:




- Vi refererar uttryckligen till Schema, via `nia_schema()`, och Interface, via `Rgb20::iface()`. Anropen `Schema.schema_id()` och `iface.iface_id()` används för att Anchor Interface Implementation på kompileringssidan (detta associerar de kryptografiska identifierarna för dessa två komponenter);
- En mappning upprättas mellan Schema Elements och Interface Elements. Till exempel är fältet `GS_NOMINAL` i Schema länkat till strängen `"spec"` på Interface-sidan (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Vi gör samma sak för operationer, till exempel `TS_TRANSFER`, som vi länkar till `"Transfer"` i Interface...;
- Vi kan se att det inte finns några valencies (`valencies: none!()`) eller extensions (`extensions: none!()`), vilket återspeglar det faktum att detta NIA Contract inte använder dessa funktioner.


Resultatet efter kompilering är en separat `.RGB` eller `.rgba`-fil, som ska importeras till Wallet utöver Schema och Interface. Programvaran vet alltså hur den konkret ska ansluta denna NIA Contract (vars logik beskrivs av dess Schema) till "RGB20" Interface (som tillhandahåller mänskliga namn och ett interaktionsläge för fungibla tokens), genom att använda denna Interface Implementation som en gateway mellan de två.


#### Varför separat Interface Implementation?


Separering ökar flexibiliteten. En enda Schema kan ha flera olika Interface-implementeringar, var och en mappande en annan uppsättning funktioner. Dessutom kan själva Interface Implementation utvecklas eller skrivas om utan att det krävs en förändring i vare sig Schema eller Interface. Detta bibehåller RGB:s princip om modularitet: varje komponent (Schema, Interface, Interface Implementation) kan versionshanteras och uppdateras oberoende av varandra, så länge som de kompatibilitetsregler som protokollet föreskriver respekteras (samma identifierare, enhetliga typer, etc.).


Vid konkret användning, när Wallet laddar en Contract, måste den göra det:




- Ladda den kompilerade **Schema** (för att känna till Business Logic:s struktur);
- Ladda in kompilerad **Interface** (för att förstå namn och operationer på användarsidan);
- Ladda kompilerad **Interface Implementation** (för att koppla Schema-logik till Interface-namn, operation för operation, fält för fält).


Denna modulära arkitektur möjliggör användningsscenarier som t.ex:




- Begränsa vissa funktioner för vissa användare: Erbjud en partiell Implementation Interface som endast ger tillgång till grundläggande överföringar, utan att erbjuda t.ex. bränn- eller uppdateringsfunktioner;
- Förändringspresentation: utforma en Interface Implementation som byter namn på ett fält i Interface eller mappar det på ett annat sätt, utan att ändra grunden för Contract;
- Stöd för flera system: en Wallet kan ladda flera Interface-implementeringar för samma Interface-typ, för att hantera olika system (olika token-logiker), förutsatt att deras struktur är kompatibel.


I nästa kapitel kommer vi att titta på hur en Contract-överföring fungerar och hur RGB-fakturor genereras.


## Contract överföringar


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


I det här kapitlet kommer vi att analysera processen för en Contract-överföring i RGB-ekosystemet. För att illustrera detta tar vi en titt på Alice och Bob, våra vanliga huvudpersoner, som vill Exchange en RGB-tillgång. Vi kommer också att visa några kommandoutdrag från kommandoradsverktyget `RGB` för att se hur det fungerar i praktiken.


### Förståelse RGB Contract överföring


Låt oss ta ett exempel på en överföring mellan Alice och Bob. I det här exemplet antar vi att Bob precis har börjat använda RGB, medan Alice redan har RGB-tillgångar i sin Wallet. Vi kommer att se hur Bob ställer in sin miljö, importerar relevant Contract, sedan begär en överföring från Alice, och slutligen hur Alice utför den faktiska transaktionen på Bitcoin Blockchain.


#### 1) Installera RGB Wallet


Först och främst måste Bob installera en RGB Wallet, dvs. programvara som är kompatibel med protokollet. Detta innehåller inga kontrakt i början. Bob kommer också att behöva:




- En Bitcoin Wallet för att hantera dina UTXO:er;
- En anslutning till en Bitcoin-nod (eller till en Electrum-server), så att du kan identifiera dina UTXO:er och sprida dina transaktioner i nätverket.


Som en påminnelse hänvisar **Owned States** i RGB till Bitcoin UTXOs. Vi måste därför alltid kunna hantera och spendera UTXO:er i en Bitcoin-transaktion som innehåller kryptografiska åtaganden (`Tapret` eller `Opret`) som pekar på RGB-data.


#### 2) Contract informationsinhämtning


Bob behöver sedan hämta de Contract-data som han är intresserad av. Dessa data kan cirkulera via vilken kanal som helst: webbplats, e-post, meddelandeprogram... I praktiken grupperas de i en ***Consignment***, dvs. ett litet paket med data som innehåller:




- **Genesis**, som definierar det initiala tillståndet för Contract;
- **Schema**, som beskriver Business Logic (strikta typer, valideringsskript etc.);
- **Interface**, som definierar presentationen Layer (fältnamn, tillgängliga operationer);
- **Interface Implementation**, som konkret kopplar Schema till Interface.


![RGB-Bitcoin](assets/fr/075.webp)


Den totala storleken är ofta i storleksordningen några kilobyte, eftersom varje komponent i allmänhet väger mindre än 200 byte. Det kan också vara möjligt att sända denna Consignment i Base58, via censurresistenta kanaler (som Nostr eller via Lightning Network, till exempel), eller som en QR-kod.


#### 3) Import och validering av Contract


När Bob har tagit emot Consignment importerar han den till sin RGB Wallet. Detta kommer då att:




- Kontrollera att Genesis och Schema är giltiga;
- Ladda Interface och Interface Implementation;
- Uppdatera dina data på klientsidan Stash.


Bob kan nu se tillgången i sin Wallet (även om han inte äger den ännu) och förstå vilka fält som är tillgängliga, vilka operationer som är möjliga ... Han behöver sedan kontakta en person som faktiskt äger den tillgång som ska överföras. I vårt exempel är detta Alice.


Processen för att upptäcka vem som innehar en viss RGB tillgång liknar att hitta en Bitcoin betalare. Detaljerna i denna anslutning beror på användningen (marknadsplatser, privata chattkanaler, fakturering, försäljning av varor och tjänster, lön ...).


#### 4) Utfärdande av en Invoice


För att initiera överföringen av en RGB-tillgång måste Bob först utfärda en Invoice. Denna Invoice används för att:




- Tala om för Alice vilken typ av operation som ska utföras (t.ex. en `Transfer` från en RGB20 Interface);
- Förse Alice med Bob:s *Seal Definition* (dvs. den UTXO där han önskar ta emot tillgången);
- Ange den mängd aktiv ingrediens som krävs (t.ex. 100 enheter).


Bob använder verktyget `RGB` på kommandoraden. Anta att han vill ha 100 enheter av en token vars `ContractId` är känt, vill förlita sig på `Tapret` och specificerar dess UTXO (`456e3..dfe1:0`):


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


Vi tittar närmare på strukturen för RGB-fakturor i slutet av detta kapitel.


#### 5) Invoice överföring


Den genererade Invoice (t.ex. som URL: `RGB:2WBcas9.../RGB20/100+utxob:...`) innehåller all information som Alice behöver för att förbereda överföringen. Precis som med Consignment kan den kodas kompakt (Base58 eller annat format) och skickas via en meddelandeapplikation, e-post, Nostr...


![RGB-Bitcoin](assets/fr/076.webp)


#### 6) Transaktionsförberedelser på Alice-sidan


Alice tar emot Bob:s Invoice. I sin RGB Wallet har hon en Stash som innehåller den tillgång som ska överföras. För att spendera den UTXO som innehåller tillgången måste hon först generate en PSBT (*Partially Signed Bitcoin Transaction*), dvs. en ofullständig Bitcoin-transaktion, med hjälp av den UTXO hon har:


```bash
alice$ wallet construct tx.psbt
```


Denna grundläggande transaktion (osignerad för tillfället) kommer att användas för att Anchor den kryptografiska Commitment kopplad till överföringen till Bob. Alice:s UTXO kommer således att spenderas, och i utmatningen kommer vi att placera `Tapret` eller `Opret` Commitment för Bob.


#### 7) Generering av överföring Consignment


Därefter bygger Alice ***Terminal Consignment*** (ibland kallad "transfer Consignment") via kommandot:


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


Den här nya filen `Consignment.RGB` innehåller:




- Den fullständiga historiken över statliga övergångar som krävs för att validera tillgången fram till nutid (sedan Genesis);
- Den nya State Transition som överför tillgångar från Alice till Bob, enligt den Invoice som Bob har utfärdat;
- Den ofullständiga Bitcoin-transaktionen (*Witness Transaction*) (`tx.PSBT`), som spenderar Alice:s Single-Use Seal, modifierad för att inkludera den kryptografiska Commitment till Bob.


I det här skedet sänds transaktionen ännu inte ut i Bitcoin-nätverket. Consignment är större än en grundläggande Consignment, eftersom den innehåller hela historiken (*bevisningskedjan*) för att bevisa tillgångens legitimitet.


#### 8) Bob kontrollerar och accepterar Consignment


Alice sänder denna **Terminal Consignment** till Bob. Bob kommer då att:




- Kontrollera giltigheten för State Transition (se till att historiken är konsekvent, att Contract-reglerna respekteras etc.);
- Lägg till den i din lokala Stash;
- Möjligen generate en signatur (`sig:...`) på Consignment, för att visa att den har granskats och godkänts (ibland kallad "*payslip*").


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/fr/077.webp)


#### 9) Alternativ: Bob skickar bekräftelse tillbaka till Alice (*betalningskvitto*)


Om Bob så önskar kan han skicka tillbaka denna signatur till Alice. Detta indikerar:




- Att den erkänner övergången som giltig;
- Att han samtycker till att Bitcoin-transaktionen sänds.


Detta är inte obligatoriskt, men det kan ge Alice en försäkran om att det inte kommer att uppstå några efterföljande tvister om överföringen.


#### 10) Alice undertecknar och publicerar transaktionen


Alice kan då:




- Kontrollera Bob:s signatur (`RGB check <sig>`);
- Signera *Witness Transaction* som fortfarande är en PSBT (`Wallet sign`);
- Publicera Witness Transaction på Bitcoin-nätverket (`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/fr/078.webp)


När denna transaktion har bekräftats markerar den avslutningen av överföringen. Bob blir den nya ägaren av tillgången: han har nu en Owned State som pekar på UTXO som han kontrollerar, vilket bevisas av Commitment:s närvaro i transaktionen.


Sammanfattningsvis följer här den fullständiga överföringsprocessen:


![RGB-Bitcoin](assets/fr/079.webp)


### Fördelar med RGB-överföringar




- Konfidentialitet**:


Endast Alice och Bob har tillgång till alla State Transition-data. De Exchange denna information utanför Blockchain, via sändningar. De kryptografiska åtagandena i Bitcoin-transaktionen avslöjar inte typen av tillgång eller beloppet, vilket garanterar mycket större sekretess än andra On-Chain token-system.




- Validering på kundsidan**:


Bob kan kontrollera att överföringen är konsekvent genom att jämföra *Consignment* med *ankarna* i Bitcoin Blockchain. Han behöver inte validering från tredje part. Alice behöver inte publicera hela historiken på Blockchain, vilket minskar belastningen på basprotokollet och förbättrar sekretessen.




- Förenklad atomicitet**:


Komplexa utbyten (atomära swappar mellan BTC och en RGB-tillgång, till exempel) kan utföras inom en enda transaktion, vilket undviker behovet av HTLC- eller PTLC-skript. Om avtalet inte sänds ut kan alla återanvända sina UTXO:er på andra sätt.


### Sammanfattande diagram för överföring


Innan vi tittar närmare på fakturorna följer här ett översiktligt diagram över det övergripande flödet i en RGB-överföring:




- Bob installerar en RGB Wallet och erhåller den ursprungliga Contract Consignment;
- Bob utfärdar en Invoice som nämner UTXO var tillgången ska tas emot;
- Alice tar emot Invoice, bygger PSBT och genererar Terminal Consignment;
- Bob accepterar det, kontrollerar, lägger till uppgifterna i sin Stash och signerar (*betalningsbevis*) om det behövs;
- Alice publicerar transaktionen i Bitcoin:s nätverk;
- Genom att bekräfta transaktionen blir överföringen officiell.


![RGB-Bitcoin](assets/fr/080.webp)


Överföringen illustrerar all kraft och flexibilitet i RGB-protokollet: en privat Exchange, validerad på klientsidan, minimalt och diskret förankrad på Bitcoin Blockchain, och behåller det bästa av protokollets säkerhet (ingen risk för Double-spending). Detta gör RGB till ett lovande ekosystem för värdeöverföringar som är mer konfidentiella och skalbara än On-Chain programmerbara blockkedjor.


### Fakturor RGB


I det här avsnittet förklarar vi i detalj hur **fakturor** fungerar i RGB-ekosystemet och hur de gör det möjligt att utföra transaktioner (i synnerhet överföringar) med en Contract. Först tittar vi på de identifierare som används, sedan på hur de kodas och slutligen på strukturen för en Invoice uttryckt som en URL (ett format som är tillräckligt praktiskt för att användas i plånböcker).


#### Identifierare och kodning


En unik identifierare definieras för var och en av följande Elements:




- En RGB Contract;
- Det är Schema (Business Logic);
- Det är Interface och Interface Implementation;
- Dess tillgångar (tokens, NFT, etc.),


Denna unikhet är mycket viktig, eftersom varje komponent i systemet måste kunna särskiljas. En Contract X får t.ex. inte förväxlas med en annan Contract Y, och två olika gränssnitt (t.ex. RGB20 jämfört med RGB21) måste ha olika identifierare.


För att göra dessa identifierare både effektiva (liten storlek) och läsbara använder vi:




- Base58-kodning, som undviker användningen av förvirrande tecken (t.ex. `0` och bokstaven `O`) och ger relativt korta strängar;
- Ett prefix som anger identifierarens art, vanligtvis i form av `RGB:` eller ett liknande URN.


Till exempel kan ett `ContractId` representeras av något liknande:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Prefixet `RGB:` bekräftar att detta är en RGB-identifierare, och inte en HTTP-länk eller annat protokoll. Tack vare det här prefixet kan plånböcker tolka strängen korrekt.


#### Segmentering av identifierare


RGB-identifierare är ofta ganska långa, eftersom den underliggande (kryptografiska) säkerheten kan kräva fält på 256 bitar eller mer. För att underlätta mänsklig läsning och verifiering delar vi upp dessa strängar i flera block som åtskiljs av ett bindestreck (`-`). I stället för att ha en lång, oavbruten teckensträng delar vi alltså upp den i kortare block. Detta är vanligt för kreditkorts- och telefonnummer, och det gäller även här för att underlätta verifiering. Så till exempel kan en användare eller partner få veta: "*Kontrollera att det tredje blocket är `9GEgnyMj7`*", i stället för att behöva jämföra allt på en gång. Det sista blocket används ofta som en **checksumma**, för att ha ett system för att upptäcka fel eller skrivfel.


Som ett exempel kan en `ContractId` i base58 kodad och segmenterad vara:


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Varje bindestreck delar upp strängen i avsnitt. Detta påverkar inte kodens semantik, utan endast dess presentation.


#### Använda webbadresser för fakturor


En RGB Invoice presenteras som en URL. Det innebär att den kan klickas på eller skannas (som en QR-kod), och en Wallet kan direkt tolka den för att genomföra en transaktion. Denna enkla interaktion skiljer sig från vissa andra system där man måste kopiera och klistra in olika uppgifter i olika fält i programvaran.


En Invoice för en fungibel token (t.ex. en RGB20 token) kan se ut så här:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Låt oss analysera den här webbadressen:




- `RGB:`** (prefix): anger en länk som anropar RGB-protokollet (analogt med `http:` eller `Bitcoin:` i andra sammanhang);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: representerar `ContractId` för den token som du vill manipulera;
- `/RGB20/100`**: anger att Interface `RGB20` används och att 100 enheter av tillgången begärs. Syntaxen är: `/Interface/amount`;
- `+utxob:`**: anger att information om mottagaren UTXO (eller, mer exakt, definitionen av Single-Use Seal) läggs till;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: detta är *blinded* UTXO (eller Seal Definition). Med andra ord har Bob maskerat sin exakta UTXO, så avsändaren (Alice) vet inte vad den exakta Address är. Hon vet bara att det finns en giltig Seal som hänvisar till en UTXO som kontrolleras av Bob.


Det faktum att allt ryms i en enda URL gör livet enklare för användaren: ett enkelt klick eller skanning i Wallet, och operationen är redo att utföras.


Man skulle kunna tänka sig system där en enkel ticker (t.ex. "USDT") används i stället för "ContractId". Detta skulle dock ge upphov till stora problem med förtroende och säkerhet: en ticker är inte en unik referens (flera kontrakt skulle kunna hävda att de kallas `USDT`). Med RGB vill vi ha en unik, otvetydig kryptografisk identifierare. Därav antagandet av 256-bitars strängen, kodad i base58 och segmenterad. Användaren vet att han manipulerar just den Contract vars ID är `2WBcas9-yjz...` och inte någon annan.


#### Ytterligare URL-parametrar


Du kan också lägga till ytterligare parametrar i URL:en, på samma sätt som med HTTP, t.ex:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- `?sig=...`: representerar t.ex. en signatur som är associerad med Invoice, som vissa plånböcker kan verifiera;
- Om en Wallet inte hanterar denna signatur ignorerar den helt enkelt denna parameter.


Låt oss ta fallet med en NFT via RGB21 Interface. Till exempel kan vi ha:


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Här ser vi:




- `RGB:`**: URL-prefix;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT);
- rGB21**: Interface för icke avyttringsbara tillgångar (NFT);
- `DbwzvSu-4BZU81jEp-...`**: en uttrycklig hänvisning till den unika delen av NFT, t.ex. en Hash av datablobben (media, metadata...);
- "Seal Definition.


Tanken är densamma: sända en unik länk som Wallet kan tolka och som tydligt identifierar den unika tillgång som ska överföras.


#### Andra operationer via URL


RGB-URL:er används inte bara för att begära en överföring. De kan också koda mer avancerade operationer, som att utfärda nya tokens (*issuance*). Ett exempel:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Här hittar vi:




- `RGB:`: protokoll;
- `2WBcas9-...`: Contract ID;
- `/RGB20/issue/100000`: anger att du vill använda "*Issue*"-övergången för att skapa ytterligare 100 000 tokens;
- `+utxob:`: Seal Definition.


Till exempel kan Wallet lyda: "Jag har blivit ombedd att utföra en `emission` från `RGB20` Interface, på den och den Contract, för 100.000 enheter, till förmån för den och den Single-Use Seal.*"


Nu när vi har tittat på de viktigaste Elements i RGB-programmering tar jag dig genom nästa kapitel om hur du ritar upp en RGB Contract.


## Utarbeta smarta kontrakt


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


I det här kapitlet går vi steg för steg igenom hur man skriver en Contract med hjälp av kommandoradsverktyget `RGB`. Syftet är att visa hur man installerar och manipulerar CLI, kompilerar en **Schema**, importerar **Interface** och **Interface Implementation** och sedan utfärdar (*issue*) en tillgång. Vi tittar också på den underliggande logiken, inklusive kompilering och validering av tillstånd. I slutet av det här kapitlet ska du kunna reproducera processen och skapa dina egna RGB-kontrakt.


Som en påminnelse är den interna logiken i RGB baserad på Rust-bibliotek som du som utvecklare kan importera till dina projekt för att hantera Client-side Validation-delen. Dessutom arbetar LNP/BP Association-teamet med bindningar för andra språk, men detta har ännu inte slutförts. Dessutom utvecklar andra enheter som Bitfinex sina egna integrationsstackar (vi kommer att prata om dessa i de sista 2 kapitlen i kursen). För tillfället är därför `RGB` CLI den officiella referensen, även om den fortfarande är relativt opolerad.


### Installation och presentation av RGB-verktyget


Huvudkommandot kallas helt enkelt `RGB`. Det är utformat för att påminna om `git`, med en uppsättning underkommandon för att manipulera kontrakt, åberopa dem, utfärda tillgångar och så vidare. Bitcoin Wallet är för närvarande inte integrerat, men kommer att vara det i en kommande version (0.11). Denna nästa version kommer att göra det möjligt för användare att skapa och hantera sina plånböcker (via deskriptorer) direkt från `RGB`, inklusive PSBT-generering, kompatibilitet med extern hårdvara (t.ex. en Hardware Wallet) för signering och interoperabilitet med programvara som Sparrow. Detta kommer att förenkla hela scenariot för utfärdande och överföring av tillgångar.


#### Installation via Cargo


Vi installerar verktyget i Rust med:


```bash
cargo install rgb-contracts --all-features
```


(Notera: Lådan heter `RGB-contracts`, och det installerade kommandot kommer att heta `RGB`. Om en crate med namnet `RGB` redan existerade, kan det ha skett en kollision, därav namnet)


Installationen sammanställer ett stort antal beroenden (t.ex. kommandoparsning, Electrum-integrering, hantering av nollkunskapsbevis etc.)


När installationen är klar kommer


```bash
rgb
```


Om du kör `RGB` (utan argument) visas en lista över tillgängliga underkommandon, till exempel `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, etc. Du kan ändra den lokala lagringskatalogen (en Stash som innehåller alla loggar, scheman och implementeringar), välja nätverk (Testnet, Mainnet) eller konfigurera din Electrum-server.


![RGB-Bitcoin](assets/fr/081.webp)


#### Första översikten över kontroller


När du kör följande kommando kommer du att se att en `RGB20` Interface redan är integrerad som standard:


```bash
rgb interfaces
```


Om denna Interface inte är integrerad, klona den:


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Kompilera den:


```bash
cargo run
```


Importera sedan den Interface som du vill ha:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-Bitcoin](assets/fr/082.webp)


Å andra sidan har vi fått veta att ingen Schema ännu har importerats till programvaran. Det finns inte heller någon Contract i Stash. För att se det, kör kommandot:


```bash
rgb schemata
```


Du kan sedan klona arkivet för att hämta vissa scheman:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/fr/083.webp)


Detta arkiv innehåller, i katalogen `src/`, flera Rust-filer (till exempel `nia.rs`) som definierar scheman (NIA för "*Non Inflatable Asset*", UDA för "*Unique Digital Asset*", etc.). För att kompilera kan du sedan köra:


```bash
cd rgb-schemata
cargo run
```


Detta genererar flera `.RGB`- och `.rgba`-filer som motsvarar de sammanställda schemana. Till exempel hittar du `NonInflatableAsset.RGB`.


#### Import av Schema och Interface Implementation


Du kan nu importera schemat till `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/fr/084.webp)


Detta lägger till den till den lokala Stash. Om vi kör följande kommando ser vi att Schema nu visas:


```bash
rgb schemata
```


### Contract skapande (utgivning)


Det finns två sätt att skapa en ny tillgång:




- Antingen använder vi ett skript eller kod i Rust som bygger en Contract genom att fylla i Schema-fält (Global State, Owned States, etc.) och producerar en `.RGB`- eller `.rgba`-fil;
- Eller använd underkommandot `issue` direkt, med en YAML-fil (eller TOML-fil) som beskriver token:s egenskaper.


Du kan hitta exempel i Rust i mappen `examples`, som illustrerar hur du bygger en `ContractBuilder`, fyller i `Global State` (tillgångsnamn, ticker, Supply, datum, etc.), definierar Owned State (till vilken UTXO den är tilldelad), och sedan sammanställer allt detta till en *Contract Consignment* som du kan exportera, validera och importera till en Stash.


Det andra sättet är att manuellt redigera en YAML-fil för att anpassa `ticker`, `name`, `Supply` och så vidare. Anta att filen heter `RGB20-demo.yaml`. Du kan ange:




- `spec`: ticker, namn, precision;
- "Terms": ett fält för juridiska meddelanden;
- issuedSupply: mängden token som utfärdats;
- `assignments`: anger Single-Use Seal (*Seal Definition*) och den mängd som är upplåst.


Här är ett exempel på en YAML-fil som kan skapas:


```yaml
interface: RGB20Fixed

globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000

assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-Bitcoin](assets/fr/085.webp)


Sedan är det bara att köra kommandot:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/fr/086.webp)


I mitt fall är den unika Schema-identifieraren (som ska omslutas av enkla citattecken) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` och jag har inte lagt till någon emittent. Så min order är:


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Om du inte känner till Schema ID, kör kommandot:


```bash
rgb schemata
```


CLI svarar att en ny Contract har utfärdats och lagts till i Stash. Om vi skriver följande kommando ser vi att det nu finns ytterligare en Contract, motsvarande den som just utfärdats:


```bash
rgb contracts
```


![RGB-Bitcoin](assets/fr/087.webp)


Nästa kommando visar sedan de globala staterna (namn, ticker, Supply...) och listan över Owned States, dvs. tilldelningar (till exempel 1 miljon `PBN` tokens definierade i UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/fr/088.webp)


### Export, import och validering


För att dela denna Contract med andra användare kan den exporteras från Stash till en:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/fr/089.webp)


Filen `myContractPBN.RGB` kan vidarebefordras till en annan användare, som kan lägga till den i sin Stash med kommandot:


```bash
rgb import myContractPBN.rgb
```


Vid import, om det är en enkel *Contract Consignment*, får vi ett "`Importing Consignment RGB`"-meddelande. Om det är en större *State Transition Consignment* kommer kommandot att vara annorlunda (`RGB accept`).


För att säkerställa giltigheten kan du också använda den lokala valideringsfunktionen. Du kan till exempel köra:


```bash
rgb validate myContract.rgb
```


#### Användning, verifiering och visning av Stash


Som en påminnelse är Stash en lokal inventering av scheman, gränssnitt, implementeringar och kontrakt (Genesis + övergångar). Varje gång du kör "import" lägger du till ett element i Stash. Denna Stash kan ses i detalj med kommandot:


```bash
rgb dump
```


![RGB-Bitcoin](assets/fr/090.webp)


Detta kommer att generate en mapp med detaljer om hela Stash.


### Överföring och PSBT


För att genomföra en överföring måste du manipulera en lokal Bitcoin Wallet för att hantera åtagandena `Tapret` eller `Opret`.


#### generate och Invoice


I de flesta fall sker interaktionen mellan deltagarna i en Contract (t.ex. Alice och Bob) via genereringen av en Invoice. Om Alice vill att Bob ska utföra något (en token-överföring, en återutgivning, en åtgärd i en DAO, etc.) skapar Alice en Invoice som beskriver hennes instruktioner till Bob. Så vi har:




- Alice** (utgivaren av Invoice);
- Bob** (som tar emot och verkställer Invoice).


Till skillnad från andra ekosystem är en RGB Invoice inte begränsad till begreppet betalning. Den kan bädda in vilken begäran som helst som är kopplad till Contract: återkalla en nyckel, rösta, skapa en gravyr (*gravyr*) på en NFT, etc. Motsvarande operation kan beskrivas i Contract Interface. Motsvarande operation kan beskrivas i Contract Interface.


Följande kommando genererar en RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Med:




- `$Contract`: Contract identifierare (*ContractId*);
- `$Interface`: den Interface som ska användas (t.ex. `RGB20`);
- `$ACTION`: namnet på den åtgärd som anges i Interface (för en enkel fungibel token-överföring kan detta vara "Transfer"). Om Interface redan innehåller en standardåtgärd behöver du inte ange den igen här;
- `$STATE`: de statusdata som ska överföras (t.ex. ett antal tokens om en fungibel token överförs);
- `$Seal`: mottagarens (Alice:s) Single-Use Seal, dvs. en uttrycklig hänvisning till en UTXO. Bob kommer att använda denna information för att bygga Witness Transaction, och motsvarande utdata kommer sedan att tillhöra Alice (i *blinded UTXO* eller okrypterad form).


Till exempel med följande kommandon


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI kommer generate och Invoice att gilla:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Den kan överföras till Bob via valfri kanal (text, QR-kod etc.).


#### Att göra en överföring


För att överföra från denna Invoice:




- Bob (som innehar polletterna i sin Stash) har en Bitcoin Wallet. Han måste förbereda en Bitcoin-transaktion (i form av en PSBT, t.ex. `tx.PSBT`) som spenderar UTXO:erna där de nödvändiga RGB-tokens finns, plus en UTXO för valuta (Exchange);
- Bob utför följande kommando:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Detta genererar en `Consignment.RGB`-fil som innehåller:
 - Övergångshistoriken bevisar för Alice att polletterna är äkta;
 - Den nya övergången som överför tokens till Alice:s Single-Use Seal;
 - A Witness Transaction (osignerad).
- Bob skickar denna `Consignment.RGB`-fil till Alice (via e-post, en delningsserver eller ett RGB-RPC-protokoll, Storm, etc.);
- Alice tar emot `Consignment.RGB` och accepterar det i sin egen Stash:


```bash
alice$ rgb accept consignment.rgb
```




- CLI kontrollerar giltigheten av övergången och lägger till den i Alice:s Stash. Om kommandot är ogiltigt misslyckas det med detaljerade felmeddelanden. Annars lyckas det och rapporterar att provtransaktionen ännu inte har sänts ut i Bitcoin-nätverket (Bob väntar på Alice:s Green-lampa);
- Som bekräftelse returnerar kommandot `accept` en signatur (*payslip*) som Alice kan skicka till Bob för att visa honom att hon har validerat *Consignment*;
- Bob kan sedan signera och publicera (`--publish`) sin Bitcoin-transaktion:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Så snart denna transaktion bekräftas On-Chain, anses Ownership av tillgången ha överförts till Alice. Alice:s Wallet, som övervakar transaktionens Mining, ser den nya Owned State visas i dess Stash.


I nästa kapitel tar vi en närmare titt på integreringen av RGB i Lightning Network.


## RGB på Lightning Network


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


I det här kapitlet föreslår jag att vi undersöker hur RGB kan användas inom Lightning Network för att integrera och flytta RGB-tillgångar (tokens, NFT:er etc.) via off-chain-betalningskanaler.


Grundtanken är att RGB State Transition (*State Transition*) kan överföras till en Bitcoin-transaktion som i sin tur kan förbli off-chain tills Lightning-kanalen stängs. Så varje gång kanalen uppdateras kan en ny RGB State Transition införlivas i den nya bindande transaktionen, som sedan ogiltigförklarar den gamla övergången. På detta sätt kan Lightning-kanaler användas för att överföra RGB-tillgångar och kan dirigeras på samma sätt som konventionella Lightning-betalningar.


### Skapande och finansiering av kanaler


För att skapa en Lightning-kanal som bär RGB-tillgångar behöver vi två Elements:




- Bitcoin finansiering för att skapa kanalens 2/2 Multisig (den grundläggande UTXO för kanalen);
- RGB-finansiering, som skickar tillgångar till samma Multisig.


I Bitcoin-termer måste finansieringstransaktionen existera för att definiera referens UTXO, även om den endast innehåller en liten mängd Sats (det är bara en fråga om att varje produktion i framtida Commitment-transaktioner ändå förblir över Dust-gränsen). Till exempel kan Alice besluta att tillhandahålla 10k Sats och 500 USDT (utfärdat som en RGB-tillgång). På finansieringstransaktionen lägger vi till en Commitment (`Opret` eller `Tapret`) som förankrar RGB State Transition.


![RGB-Bitcoin](assets/fr/091.webp)


När finansieringstransaktionen har förberetts (men ännu inte sänts) skapas Commitment-transaktioner så att endera parten kan stänga kanalen ensidigt när som helst. Dessa transaktioner liknar Lightnings klassiska Commitment-transaktioner, förutom att vi lägger till ytterligare en utgång som innehåller RGB Anchor (OP_RETURN eller Taproot) länkad till den nya State Transition.


RGB State Transition flyttar sedan tillgångarna från finansieringens 2/2 Multisig till Commitment Transaction:s utgångar. Fördelen med denna process är att säkerheten i RGB-läget exakt matchar Lightnings bestraffningsmekanik: om Bob sänder ett gammalt kanalläge kan Alice bestraffa honom och spendera utdata för att återfå både Sats- och RGB-tokens. Incitamentet är därför ännu starkare än i en Lightning-kanal utan RGB-tillgångar, eftersom en angripare kan förlora inte bara Sats utan även kanalens RGB-tillgångar.


En Commitment Transaction som signeras av Alice och skickas till Bob skulle därför se ut så här:


![RGB-Bitcoin](assets/fr/092.webp)


Och den medföljande Commitment Transaction, undertecknad av Bob och skickad till Alice, kommer att se ut så här:


![RGB-Bitcoin](assets/fr/093.webp)


### Uppdatering av kanaler


När en betalning sker mellan två kanaldeltagare (eller om de vill ändra tillgångsfördelningen) skapar de ett nytt par Commitment-transaktioner. Beloppet i Sats på varje utgång kan eller kan inte förbli oförändrat, beroende på implementeringen, eftersom dess huvudsakliga roll är att möjliggöra konstruktionen av giltiga UTXO:er. Å andra sidan måste utgången OP_RETURN (eller Taproot) modifieras för att innehålla den nya RGB Anchor, som representerar den nya fördelningen av tillgångar i kanalen.


Till exempel, om Alice överför 30 USDT till Bob i kanalen, kommer den nya State Transition att återspegla ett saldo på 400 USDT för Alice och 100 USDT för Bob. Commit-transaktionen läggs till (eller ändras av) OP_RETURN/Taproot Anchor för att inkludera denna övergång. Observera att från RGB:s synvinkel förblir ingången till övergången den ursprungliga Multisig (där On-Chain:s tillgångar faktiskt allokeras tills kanalen stängs). Endast RGB:s utdata (allokeringar) ändras, beroende på vilken omfördelning som beslutas.


Commitment Transaction signerad av Alice, redo att distribueras av Bob:


![RGB-Bitcoin](assets/fr/094.webp)


Commitment Transaction undertecknad av Bob, redo att distribueras av Alice:


![RGB-Bitcoin](assets/fr/095.webp)


### HTLC hantering


I verkligheten gör Lightning Network det möjligt att dirigera betalningar via flera kanaler med hjälp av HTLC:er (*Hashed Time-Locked Contracts*). Det är samma sak med RGB: för varje betalning som transiteras genom kanalen läggs en HTLC-utgång till den bindande transaktionen, och en RGB-tilldelning länkas till denna HTLC. Således återfår den som spenderar HTLC-utgången (tack vare hemligheten eller efter utgången av tidslåset) både Sats och de associerade RGB-tillgångarna. Å andra sidan måste du uppenbarligen ha tillräckligt med kontanter på vägen när det gäller både Sats- och RGB-tillgångar.


![RGB-Bitcoin](assets/fr/096.webp)


Användningen av RGB på Lightning måste därför betraktas parallellt med den för Lightning Network själv. Om du vill fördjupa dig i detta ämne rekommenderar jag starkt att du tar en titt på denna andra omfattande utbildningskurs:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB kodkarta


Slutligen, innan jag går vidare till nästa avsnitt, vill jag ge dig en översikt över koden som används i RGB. Protokollet är baserat på en uppsättning Rust-bibliotek och specifikationer för öppen källkod. Här är en översikt över de viktigaste lagren och lådorna:


![RGB-Bitcoin](assets/fr/097.webp)


#### Client-side Validation




- Förvaringsplats**: [validering på klientsidan] (https://github.com/LNP-BP/client_side_validation)
- Lådor**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)


Hantering av off-chain-validering och logik för engångsförseglingar.


#### Deterministiska Bitcoin-engagemang (DBC)




- Förvaringsplats**: [bp-core](https://github.com/BP-WG/bp-core)
- Lådan**: [bp-dbc](https://crates.io/crates/bp-dbc)


Hantering av deterministisk förankring i Bitcoin-transaktioner (Tapret, OP_RETURN, etc.).


#### Multi Protocol Commitment (MPC)




- Förvaringsplats**: [validering på klientsidan] (https://github.com/LNP-BP/client_side_validation)
- Lådan**: [commit_verify](https://crates.io/crates/commit_verify)


Flera olika kombinationer och integrering med olika protokoll.


#### Strikta typer och strikt kodning




- Specifikationer**: [webbplats strict-types.org](https://www.strict-types.org/)
- Förvaringsplatser**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Lådor**: [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)


Det strikta typningssystemet och den deterministiska serialiseringen som används för Client-side Validation.


#### RGB Kärna




- Förvaringsplats**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- Lådan**: [RGB-core](https://crates.io/crates/RGB-core)


Protokollets kärna, som omfattar huvudlogiken i RGB-valideringen.


#### RGB Standardbibliotek & Wallet




- Förvaringsplats**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- Lådan**: [RGB-std](https://crates.io/crates/RGB-std)


Standardimplementeringar, Stash och Wallet hantering.


#### RGB CLI




- Förvaringsplats**: [RGB](https://github.com/RGB-WG/RGB)
- Lådor**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


`RGB` CLI och crate Wallet, för kommandoradshantering av kontrakt.


#### RGB Schema




- Förvaringsplats**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


Innehåller exempel på scheman (NIA, UDA, etc.) och deras implementeringar.


#### AluVM




- Info**: [AluVM.org](https://www.AluVM.org/)
- Förvaringsplatser**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- Lådor**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)


Registerbaserad virtuell maskin som används för att köra valideringsskript.


#### Bitcoin Protokoll - BP




- Förråd**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Tillägg för att stödja Bitcoin-protokollet (transaktioner, förbikopplingar etc.).


#### Allestädes närvarande deterministisk databehandling - UBIDECO




- Förvaringsplats**: [UBIDECO](https://github.com/UBIDECO)


Ekosystem kopplat till deterministisk utveckling med öppen källkod.


# Byggnad på RGB


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA och Bitmask-projektet


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


Den här sista delen av kursen baseras på presentationer som gjordes av olika talare på RGB bootcamp. Det innehåller vittnesmål och reflektioner om RGB och dess ekosystem, samt presentationer av verktyg och projekt baserade på protokollet. Det här första kapitlet modereras av Hunter Beast och de två följande av Frederico Tenga.


### Från JavaScript till Rust och in i Bitcoin-ekosystemet


Till en början arbetade Hunter Beast huvudsakligen i JavaScript. Sedan upptäckte han **Rust**, vars syntax till en början verkade oattraktiv och frustrerande. Han kom dock att uppskatta kraften i språket, kontrollen över minnet (*heap* och *stack*) samt den säkerhet och prestanda som följer med det. Han betonar att Rust är en utmärkt träningsplats för en djupgående förståelse av hur en dator fungerar.


Hunter Beast berättar om sin bakgrund i olika projekt i *Altcoin*-ekosystemet, till exempel Ethereum (med Solidity, TypeScript etc.) och senare Filecoin. Han förklarar att han inledningsvis var imponerad av några av protokollen, men att han till slut blev desillusionerad av de flesta av dem, inte minst på grund av deras tokenomics. Han fördömer de tvivelaktiga ekonomiska incitamenten, det inflationsdrivande skapandet av tokens som späder ut investerarna och den potentiellt exploaterande aspekten av dessa projekt. Så det slutade med att han antog en **Bitcoin Maximalist**-ståndpunkt, inte minst för att vissa människor öppnade hans ögon för Bitcoin:s sundare ekonomiska mekanismer och för robustheten i detta system.


### RGB:s attraktionskraft och att bygga på lager


Det som definitivt övertygade honom om Bitcoin:s relevans var, enligt honom, upptäckten av RGB och konceptet med lager. Han tror att befintliga funktioner på andra blockkedjor skulle kunna reproduceras på högre lager, ovanför Bitcoin, utan att ändra det grundläggande protokollet.


I februari 2022 gick han med i **DIBA** för att arbeta specifikt med RGB, och i synnerhet med **Bitmask** Wallet. Vid den tidpunkten var Bitmask fortfarande i version 0.01 och körde RGB i version 0.4, endast för hantering av enstaka tokens. Han konstaterar att detta var mindre självförvarsorienterat än idag, eftersom logiken delvis var serverbaserad. Sedan dess har arkitekturen utvecklats mot denna modell, vilket uppskattas mycket av bitcoiners.


### Grunderna i RGB-protokollet


Protokollet ** RGB** är det senaste och mest avancerade utförandet av konceptet _färgade mynt_, som redan utforskades runt 2012-2013. Vid den tiden ville flera team associera olika Bitcoin-värden på UTXO, vilket ledde till flera spridda implementeringar. Denna brist på standardisering och den låga efterfrågan vid den tiden hindrade dessa lösningar från att få ett varaktigt fotfäste.


Idag utmärker sig RGB för sin konceptuella robusthet och sina enhetliga specifikationer via LNP/BP-associationen. Principen är baserad på Client-side Validation. Bitcoin Blockchain lagrar endast kryptografiska åtaganden (_commitments_, via Taproot eller OP_RETURN), medan majoriteten av data (Contract definitioner, överföringshistorik, etc.) lagras av de berörda användarna. På detta sätt fördelas lagringsbelastningen och utbytenas konfidentialitet förstärks, utan att Blockchain tyngs ner. Detta tillvägagångssätt gör det möjligt att skapa fungibla tillgångar (**RGB20**-standard) eller unika tillgångar (**RGB21**-standard) inom ett modulärt och skalbart ramverk.


### token:s funktion (RGB20) och unika tillgångar (RGB21)


Med **RGB20** definierar vi en fungibel token på Bitcoin. Utgivaren väljer en _tillgång_, en _precision_ och skapar ett _kontrakt_ där han sedan kan göra överföringar. Varje överföring refereras till en Bitcoin UTXO, som fungerar som en *Single-Use Seal*. Denna logik säkerställer att användaren inte kommer att kunna spendera samma tillgång två gånger, eftersom endast den person som kan spendera UTXO faktiskt har nyckeln för att uppdatera tillståndet för Contract på klientsidan.


**RGB21** riktar in sig på unika tillgångar (eller "NFT"). Tillgången har en Supply på 1 och kan associeras med metadata (bildfil, ljud etc.) som beskrivs via ett specifikt fält. Till skillnad från NFT:er på offentliga blockkedjor kan data och deras MIME-identifierare förbli privata och distribueras peer-to-peer efter ägarens gottfinnande.


### Bitmask-lösningen: en Wallet för RGB


För att utnyttja RGB:s möjligheter i praktiken har **DIBA**-projektet utformat en Wallet som kallas [Bitmask] (https://bitmask.app/). Tanken är att tillhandahålla ett icke-frihetsberövande, Taproot-baserat verktyg, tillgängligt som en webbapplikation eller ett webbläsartillägg. Bitmask hanterar både RGB20- och RGB21-tillgångar och integrerar olika säkerhetsmekanismer:




- Kärnkoden är skriven i Rust, sedan kompilerad i WebAssembly för att köras i en JavaScript-miljö (React);
- Nycklar genereras lokalt och lagras sedan krypterade lokalt;
- Statsdata (Stash) lagras i minnet, serialiseras och krypteras via biblioteket **Carbonado**, som utför komprimering, felkorrigering, kryptering och strömverifiering med hjälp av Blake3.


Tack vare denna arkitektur sker alla tillgångstransaktioner på klientsidan. Från utsidan är Bitcoin-transaktionen inget annat än en klassisk Taproot-utgiftstransaktion, som ingen skulle misstänka också bär en överföring av fungibla tokens eller NFT. Avsaknaden av On-Chain-överbelastning (inga offentligt lagrade metadata) garanterar en viss grad av diskretion och gör det lättare att motstå eventuella censurförsök.


### Säkerhet och distribuerad arkitektur


I den mån RGB-protokollet kräver att varje deltagare behåller sin transaktionshistorik (för att bevisa giltigheten av de överföringar som den tar emot) uppstår frågan om lagring. Bitmask föreslår att denna Stash serialiseras lokalt och sedan skickas till flera servrar eller moln (valfritt). Uppgifterna förblir krypterade av användaren via **Carbonado**, så att en server inte kan läsa dem. I händelse av partiell korruption kan felkorrigeringen Layer återskapa innehållet.


Användningen av CRDT (_Conflict-free replicated data type_) gör att olika versioner av Stash kan slås samman om de skulle skilja sig åt. Det står var och en fritt att hosta dessa data var de vill, eftersom ingen enskild Full node innehåller all information som är kopplad till tillgången. Detta återspeglar exakt *Client-side Validation*-filosofin, där varje ägare är ansvarig för att lagra bevis på giltigheten för sin RGB-tillgång.


### Mot ett bredare ekosystem: marknadsplats, interoperabilitet och nya funktioner


Företaget bakom Bitmask begränsar sig inte till den enkla utvecklingen av en Wallet. DIBA har för avsikt att utveckla:




- En **marknadsplats** för utbyte av tokens, särskilt i form av **RGB21**;
- Kompatibilitet med andra plånböcker (t.ex. *Iris Wallet*);
- Transfer batching**-teknik, dvs. möjligheten att inkludera flera på varandra följande RGB-överföringar i en enda transaktion.


Samtidigt arbetar vi på **WebBTC** eller **WebLN** (standarder som gör det möjligt för webbplatser att be Wallet att signera Bitcoin- eller Lightning-transaktioner), samt på möjligheten att "teleburn" Ordinals-poster (om vi vill repatriera Ordinals till ett mer diskret och flexibelt RGB-format).


### Slutsats


Hela processen visar hur RGB-ekosystemet kan distribueras och göras tillgängligt för slutanvändare genom robusta tekniska lösningar. Övergången från ett Altcoin-perspektiv till en mer Bitcoin-centrerad vision, i kombination med upptäckten av * Client-side Validation*, illustrerar en ganska logisk väg: vi förstår att det är möjligt att implementera olika funktioner (fungibla tokens, NFT, smarta kontrakt ...) utan att gaffla Blockchain, helt enkelt genom att dra nytta av kryptografiska åtaganden på Taproot-transaktioner eller OP_RETURNs.


**Bitmask** Wallet är en del av detta tillvägagångssätt: på Blockchain-sidan är allt du ser en vanlig Bitcoin-transaktion; på användarsidan manipulerar du en webb Interface där du skapar, Exchange och lagrar alla typer av off-chain-tillgångar. Denna modell separerar tydligt den monetära infrastrukturen (Bitcoin) från utgivnings- och överföringslogiken (RGB), samtidigt som den säkerställer en hög nivå av konfidentialitet och bättre skalbarhet.


## Bitfinex arbete med RGB


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


I detta kapitel, baserat på en presentation av Frederico Tenga, tittar vi på en uppsättning verktyg och projekt som skapats av Bitfinex-teamet tillägnad RGB, i syfte att främja framväxten av ett rikt och varierat ekosystem kring detta protokoll. Teamets ursprungliga mål är inte att släppa en specifik kommersiell produkt, utan snarare att tillhandahålla mjukvarubyggstenar, bidra till själva RGB-protokollet och föreslå konkreta implementeringsreferenser som en mobil Wallet (* Iris Wallet *) eller en RGB-kompatibel Lightning-nod.


### Bakgrund och mål


Sedan omkring 2022 har Bitfinex RGB-team koncentrerat sig på att utveckla den teknikstack som gör att RGB kan utnyttjas och testas effektivt. Flera bidrag har gjorts:




- Deltagande i källkods- och protokollspecifikationer, inklusive att skriva förbättringsförslag, åtgärda buggar etc;
- Verktyg för utvecklare för att förenkla integrationen av RGB i deras applikationer;
- Design av en mobil Wallet med namnet [Iris] (https://iriswallet.com/) för att experimentera och illustrera bästa praxis för användning av RGB;
- Skapande av en anpassad Lightning-nod som kan hantera kanaler med RGB-tillgångar;
- Stödja andra team som bygger lösningar på RGB, för att uppmuntra mångfald och ett starkt ekosystem.


Detta tillvägagångssätt syftar till att täcka hela behovskedjan: från lågnivåbiblioteket (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*), som möjliggör implementering av en Wallet, till produktionsaspekten (en Lightning-nod, en Wallet för Android, etc.).


### RGBlib-biblioteket: förenklar utvecklingen av RGB-applikationer


En viktig punkt för att demokratisera skapandet av RGB-plånböcker och applikationer är att göra en abstraktion tillgänglig som är tillräckligt enkel så att utvecklare inte behöver lära sig allt om protokollets interna logik. Detta är just syftet med **RGBlib**, som är skrivet i Rust.


RGBlib fungerar som en bro mellan de mycket flexibla (men ibland komplexa) kraven i RGB som vi har kunnat studera i tidigare kapitel och de konkreta behoven hos en applikationsutvecklare. Med andra ord kan en Wallet (eller tjänst) som vill hantera token-överföringar, utfärdande av tillgångar, verifiering etc. förlita sig på RGBlib utan att känna till varje kryptografisk detalj eller varje anpassningsbar RGB-parameter.


Bokhandeln erbjuder:




- Nyckelfärdiga funktioner för utfärdande (_issuance_) av tillgångar (fungibla eller ej);
- Förmåga att överföra (skicka/ta emot) tillgångar genom att manipulera enkla objekt (adresser, belopp, UTXO etc.);
- En mekanism för att lagra och ladda den statusinformation (*sändningar*) som krävs för Client-side Validation.


RGBlib förlitar sig därför på komplexa begrepp som är specifika för RGB (Client-side Validation, Tapret/Opret-ankare), men kapslar in dem så att den slutliga applikationen inte behöver programmera om allt eller fatta riskabla beslut. Dessutom är RGBlib redan bundet i flera språk (Kotlin och Python), vilket öppnar dörren för användningsområden utöver ett enkelt Rust-universum.


### Iris Wallet: ett exempel på en RGB Wallet på Android


För att bevisa effektiviteten hos RGBlib har Bitfinex-teamet utvecklat **Iris Wallet**, exklusivt på Android i detta skede. Det är en mobil Wallet som illustrerar en användarupplevelse som liknar den för en vanlig Bitcoin Wallet: du kan utfärda en tillgång, skicka den, ta emot den och se dess historik, samtidigt som du förblir på en självförvarsmodell.


Iris har ett antal intressanta funktioner:


**Använda en Electrum-server:**


Precis som alla Wallet behöver Iris känna till transaktionsbekräftelser på Blockchain. Istället för att bädda in en komplett nod använder Iris som standard en Electrum-server som underhålls av Bitfinex-teamet. Användare kan dock konfigurera sin egen server eller en annan tjänst från tredje part. På så sätt kan Bitcoin-transaktioner valideras och information hämtas (indexering) på ett modulärt sätt.


**Proxyservern RGB:**


Till skillnad från Bitcoin kräver RGB Exchange av off-chain metadata (*consignments*) mellan avsändare och mottagare. För att förenkla denna process erbjuder Iris en lösning där kommunikationen sker via en proxyserver. Den mottagande Wallet genererar en *Invoice* som anger vart avsändaren ska skicka data på *klientsidan*. Som standard pekar webbadressen till en proxy som Bitfinex-teamet är värd för, men du kan ändra denna proxy (eller vara värd för din egen). Tanken är att återgå till en välbekant användarupplevelse där mottagaren visar en QR-kod och avsändaren skannar denna kod för transaktionen, utan några komplexa ytterligare manipulationer.


**Kontinuerlig säkerhetskopiering:**


I ett strikt Bitcoin-sammanhang räcker det i allmänhet med att säkerhetskopiera din seed (även om vi numera rekommenderar att du säkerhetskopierar seed och deskriptorerna istället). Med RGB är detta inte tillräckligt: du måste också behålla den lokala historiken (*konsigneringarna*) som bevisar att du verkligen äger en RGB-tillgång. Varje gång du får ett kvitto lagrar enheten nya data, vilket är viktigt för efterföljande utgifter. Iris hanterar automatiskt en krypterad säkerhetskopia i användarens Google Drive. Detta kräver inget särskilt förtroende för Google, eftersom säkerhetskopian är krypterad, och mer robusta alternativ (t.ex. en personlig server) planeras för framtiden för att undvika alla risker för censur eller radering av en tredjepartsoperatör.


**Övriga funktioner: **




- Skapa en Faucet för att snabbt testa eller distribuera tokens för experiment eller marknadsföring;
- Ett certifieringssystem (för närvarande centraliserat) för att skilja en legitim token från en falsk som kopierar en berömd ticker. I framtiden kan denna certifiering bli mer decentraliserad (via DNS eller andra mekanismer).


Sammantaget erbjuder Iris en användarupplevelse som ligger nära den för en klassisk Bitcoin Wallet, vilket maskerar den extra komplexiteten (Stash-hantering, * Consignment*-historik etc.) tack vare RGBlib och användningen av en proxyserver.


### Proxyserver och användarupplevelse


Proxyservern som introducerades ovan förtjänar att beskrivas i detalj, eftersom den är nyckeln till en smidig användarupplevelse. Istället för att avsändaren manuellt måste överföra *försändelserna* till mottagaren, sker RGB-transaktionen i bakgrunden via en :




- Mottagaren genererar en *Invoice* (innehållande bl.a. fullmakten Address);
- Avsändaren skickar (via en HTTP-begäran) ett övergångsprojekt (*Consignment*) till proxyn;
- Mottagaren hämtar detta projekt, utför valideringen på *klientsidan* lokalt;
- Mottagaren publicerar sedan, via proxyn, godkännandet (eller eventuellt avvisandet) av State Transition;
- Avsändaren kan se valideringsstatusen och, om den accepteras, sända Bitcoin-transaktionen som slutför överföringen.


På så sätt beter sig Wallet nästan som en vanlig Wallet. Användaren är omedveten om alla mellanliggande steg. Visserligen är den nuvarande proxyn varken krypterad eller autentiserad (vilket ger upphov till problem med konfidentialitet och integritet), men dessa förbättringar är möjliga i senare versioner. Proxykonceptet är fortfarande extremt användbart för att återskapa upplevelsen "Jag skickar en QR-kod, du skannar för att betala".


### RGB-integration på Lightning Network


Ett annat viktigt fokus för Bitfinex-teamets arbete är att göra Lightning Network kompatibel med RGB-tillgångar. Syftet är att möjliggöra Lightning-kanaler i USDT (eller någon annan token) och att dra nytta av samma fördelar som Bitcoin på Lightning (nästan omedelbara transaktioner, routing etc.). I konkreta termer innebär detta att skapa en Lightning-nod som är modifierad för att:




- Öppna en kanal genom att placera inte bara satoshis utan även en eller flera RGB tillgångar i finansieringen UTXO Multisig;
- generate Lightning Commitment-transaktioner (Bitcoin-sidan) åtföljda av motsvarande RGB-tillståndsövergångar. Varje gång kanalen uppdateras omdefinierar en RGB-övergång tillgångsfördelningen i Lightning-utgångarna;
- Möjliggör ensidig stängning, där tillgången hämtas i en exklusiv UTXO, i enlighet med Lightning Network regler (HTLC, tidslås, bestraffning, etc.).


Denna lösning, kallad "**RGB Lightning Node**", använder LDK (*Lightning Dev Kit*) som bas och lägger till de mekanismer som behövs för att injicera RGB-tokens i kanalerna. Lightning-åtaganden behåller den klassiska strukturen (punkterbara utgångar, tidslås ...), och dessutom Anchor och RGB State Transition (via `Opret` eller `Tapret`). För användaren öppnar detta vägen till Lightning-kanaler i stablecoins eller i någon annan tillgång som emitteras via RGB.


### DEX-potential och påverkan på Bitcoin


När flera tillgångar hanteras via Lightning blir det möjligt att föreställa sig en **atomisk Exchange** på en enda Lightning-routingväg, med samma logik för hemligheter och tidslås. Till exempel innehar användare A Bitcoin på en Lightning-kanal och användare B innehar USDT RGB på en annan Lightning-kanal. De kan bygga en väg som länkar deras två kanaler och samtidigt Exchange BTC för USDT, utan behov av förtroende. Detta är inget annat än en **atomisk swap** som äger rum i flera hopp, vilket gör att externa deltagare nästan glömmer bort det faktum att de gör en handel, inte bara en routing. Detta tillvägagångssätt erbjuder:




- Mycket låg latens, eftersom allt förblir off-chain på Lightning.
- En överlägsen **privacy**: ingen vet att det är en handel och inte en normal routing;
- Undviker frontrunning, ett återkommande problem för On-Chain DEX;
- Sänkta kostnader (du betalar inte blockspace, bara Lightning routing-avgifter).


Vi kan sedan föreställa oss ett ekosystem där Lightning-noder erbjuder swappriser (genom att tillhandahålla likviditet). Varje nod kan, om den så önskar, spela rollen som _market maker_ och köpa och sälja olika tillgångar på Lightning. Denna möjlighet till en _layer-2_ DEX förstärker idén att det inte är nödvändigt att Fork eller använda blockkedjor från tredje part för att få decentraliserade tillgångsbörser.


Påverkan på Bitcoin kan vara positiv: Lightnings infrastruktur (noder, kanaler och tjänster) skulle utnyttjas mer fullständigt tack vare de volymer som genereras av dessa *stablecoins*, derivat och andra tokens. Handlare som är intresserade av USDT-betalningar på Lightning skulle mekaniskt upptäcka BTC-betalningar på Lightning (hanteras av samma stack). Underhåll och finansiering av Lightning Network-infrastrukturen kan också dra nytta av multiplikationen av dessa icke-BTC-flöden, vilket indirekt skulle gynna Bitcoin-användare.


### Slutsats och resurser


Bitfinex-teamet som är dedikerat till RGB illustrerar genom sitt arbete mångfalden av vad som kan göras ovanpå protokollet. Å ena sidan finns RGBlib, ett bibliotek som underlättar utformningen av plånböcker och applikationer. Å andra sidan har vi Iris Wallet, en praktisk demonstration på Android av en snygg slutanvändare Interface. Slutligen visar integrationen av RGB med Lightning att stablecoin-kanaler är möjliga, och öppnar vägen för en potentiell decentraliserad DEX på Lightning.


Detta tillvägagångssätt är till stor del experimentellt och fortsätter att utvecklas: RGBlib-biblioteket förfinas under tiden, Iris Wallet får regelbundna förbättringar och den dedikerade Lightning-noden är ännu inte en vanlig Lightning-klient.


För den som vill veta mer eller bidra finns flera resurser att tillgå, bland annat




- [GitHub RGB Tools repositories] (https://github.com/RGB-Tools);
- [En informationswebbplats tillägnad Iris Wallet] (https://iriswallet.com/) för att testa Wallet på Android.


I nästa kapitel tar vi en närmare titt på hur man startar en RGB Lightning-nod.


## RLN - RGB Blixtnod


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


I det här sista kapitlet tar Frederico Tenga dig steg för steg genom att konfigurera en Lightning RGB-nod i en Regtest-miljö och visar hur du skapar RGB-tokens på den. Genom att starta två separata noder kommer du också att upptäcka hur man öppnar en Lightning-kanal mellan dem och Exchange RGB-tillgångar.


Den här videon fungerar som en handledning, liknande det vi gick igenom i ett tidigare kapitel, men med särskilt fokus på Lightning den här gången!


Huvudresursen för den här videon är Github-arkivet [RGB Lightning Node] (https://github.com/RGB-Tools/RGB-lightning-node), vilket gör det enkelt för dig att starta den här konfigurationen i Regtest.


### Driftsättning av en RGB-kompatibel Lightning-nod


Processen tar upp och omsätter i praktiken alla de begrepp som behandlats i de tidigare kapitlen:




- Tanken att **UTXO** blockerad på en 2/2 Multisig av en Lightning-kanal inte bara kan ta emot bitcoins, utan också vara en Single-Use Seal av RGB tillgångar (fungibla eller inte);
- Tillägget, i varje Lightning engagement-transaktion, av en utgång (`Tapret` eller `Opret`) avsedd för förankring av RGB State Transition;
- Den tillhörande infrastrukturen (bitcoind/indexer/proxy) för att validera Bitcoin-transaktioner och Exchange-data på *klientsidan*.


### Introduktion av RGB-lightning-node


Projektet **`RGB-lightning-node`** är en Rust daemon baserad på en `Rust-lightning` (LDK) Fork modifierad för att ta hänsyn till förekomsten av RGB tillgångar i en kanal. När en kanal öppnas kan förekomsten av tillgångar specificeras, och varje gång kanaltillståndet uppdateras skapas en RGB-övergång som återspeglar fördelningen av tillgången i Lightning-utgångarna. Detta gör det möjligt:




- Öppna blixtkanaler i USDT, till exempel;
- Dirigera dessa tokens genom nätverket, förutsatt att dirigeringsvägarna har tillräcklig likviditet;
- Utnyttja Lightnings bestraffnings- och tidslåsningslogik utan modifiering: helt enkelt Anchor RGB-övergången i en extra utgång från Commitment Transaction.


Koden befinner sig fortfarande i alfa-stadiet: vi rekommenderar att du endast använder den i **regtest** eller på **Testnet**.


### Installation av noder


För att kompilera och installera binärfilen `RGB-lightning-node` börjar vi med att klona förvaret och dess undermoduler, sedan kör vi :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/fr/098.webp)




- Alternativet `--recurse-submodules` klonar också de nödvändiga underenheterna (inklusive den modifierade versionen av `Rust-lightning`);
- Alternativet `--shallow-submodules` begränsar klonens djup för att påskynda nedladdningen, samtidigt som det ger tillgång till viktiga åtaganden.


Från projektets rot kör du följande kommando för att kompilera och installera binärfilen:


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/fr/099.webp)




- `--locked` säkerställer att versionen av beroenden respekteras strikt;
- `--debug` är inte obligatoriskt, men kan hjälpa dig att fokusera (du kan använda `--release` om du föredrar det);
- `--path .` säger till `cargo install` att installera från den aktuella katalogen.


I slutet av detta kommando kommer en körbar `RGB-lightning-node` att finnas tillgänglig i din `$CARGO_HOME/bin/`. Se till att den här sökvägen finns i din `$PATH` så att du kan anropa kommandot från vilken katalog som helst.


### Krav på prestanda


För att fungera kräver `RGB-lightning-node` daemon närvaro och konfiguration av:




- A **`bitcoind`** nod


Varje RLN-instans kommer att behöva kommunicera med `bitcoind` för att sända och övervaka sina On-Chain-transaktioner. Autentisering (inloggning/lösenord) och URL (host/port) måste tillhandahållas till daemon.




- En indexerare** (Electrum eller Esplora)


daemon måste kunna lista och utforska On-Chain-transaktioner, i synnerhet för att hitta den UTXO som en tillgång har förankrats på. Du måste ange webbadressen till din Electrum-server eller Esplora.




- En **RGB** proxy


Som vi sett i tidigare kapitel är **proxyservern** en komponent (valfri, men rekommenderas starkt) för att förenkla Exchange av *konsigneringar* mellan Lightning-peers. Återigen måste en URL anges.


ID:n och URL:er anges när daemon _låser upp_ via API:et. Mer om detta senare.


### Regtest lansering


För enkel användning finns det ett skript `regtest.sh` som automatiskt startar, via Docker, en uppsättning tjänster: `bitcoind`, `electrs` (indexerare), `RGB-proxy-server`.


![RGB-Bitcoin](assets/fr/100.webp)


Detta gör att du kan starta en lokal, isolerad och förkonfigurerad miljö. Den skapar och förstör behållare och datakataloger vid varje omstart. Vi börjar med att starta:


```bash
./regtest.sh start
```


Detta manus kommer:




- Skapa en `docker/`-katalog för lagring;
- Kör `bitcoind` i regtest, liksom indexeraren `electrs` och `RGB-proxy-servern`;
- Vänta tills allt är klart att använda.


![RGB-Bitcoin](assets/fr/101.webp)


Nu ska vi starta flera RLN-noder. I separata skal kör du till exempel (för att starta 3 RLN-noder):


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RGB-Bitcoin](assets/fr/102.webp)




- Parametern `--network regtest` anger att konfigurationen regtest ska användas;
- `--daemon-listening-port` anger på vilken REST-port Lightning-noden kommer att lyssna på API-anrop (JSON);
- `--ldk-peer-listening-port` anger vilken Lightning P2P-port som ska lyssna på;
- `dataldk0/`, `dataldk1/` är sökvägarna till lagringskatalogerna (varje nod lagrar sin information separat).


Du kan också köra kommandon på dina RLN-noder från din webbläsare:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


För att en nod ska kunna öppna en kanal måste den först ha bitcoins på en Address som genererats med följande kommando (till exempel för nod nr 1):


```bash
curl -X POST http://localhost:3001/address
```


Svaret kommer att ge dig en Address.


![RGB-Bitcoin](assets/fr/103.webp)


På `bitcoind` Regtest kommer vi att bryta några bitcoins. Kör:


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/fr/104.webp)


Skicka pengarna till noden Address som genererats ovan:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/fr/105.webp)


Minera sedan ett block för att bekräfta transaktionen:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/fr/106.webp)


### Lansering av Testnet (utan Docker)


Om du vill testa ett mer realistiskt scenario kan du starta 3 RLN-noder på Testnet istället för i Regtest, som pekar mot offentliga tjänster:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Om ingen konfiguration hittas kommer daemon som standard att försöka använda den:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332``
- indexer_url`: `ssl://electrum.iriswallet.com:50013``
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Med inloggning:




- `bitcoind_rpc_username`: `användare`
- `bitcoind_rpc_username`: `lösenord`


Du kan också anpassa dessa Elements via API:et `init`/`unlock`.


### Utfärdande av en RGB token


För att utfärda en token börjar vi med att skapa "färgbara" UTXO:er:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RGB-Bitcoin](assets/fr/107.webp)


Du kan naturligtvis anpassa beställningen. För att bekräfta transaktionen, vi min a:


```bash
./regtest.sh mine 1
```


Vi kan nu skapa en RGB-tillgång. Kommandot beror på vilken typ av tillgång du vill skapa och dess parametrar. Här skapar jag en NIA (*Non Inflatable Asset*) token med namnet "PBN" med en Supply på 1000 enheter. Med `precision` kan du definiera enheternas delbarhet.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RGB-Bitcoin](assets/fr/108.webp)


Svaret innehåller ID för den nyligen skapade tillgången. Kom ihåg att notera denna identifierare. I mitt fall är det:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/fr/109.webp)


Du kan sedan överföra den On-Chain, eller allokera den i en Lightning-kanal. Det är precis vad vi ska göra i nästa avsnitt.


### Öppnande av en kanal och överföring av en RGB-tillgång


Du måste först ansluta din nod till en peer på Lightning Network med hjälp av kommandot `/connectpeer`. I mitt exempel kontrollerar jag båda noderna. Så jag hämtar den publika nyckeln för min andra Lightning-nod med det här kommandot:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Kommandot returnerar den publika nyckeln för min nod nr 2:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RGB-Bitcoin](assets/fr/110.webp)


Därefter öppnar vi kanalen genom att ange den relevanta tillgången (`PBN`). Med kommandot `/openchannel` kan du definiera kanalens storlek i satoshis och välja att inkludera RGB-tillgången. Det beror på vad du vill skapa, men i mitt fall är kommandot:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Läs mer om detta här:




- `peer_pubkey_och_opt_addr`: Identifierare för den peer som vi vill ansluta till (den publika nyckel som vi hittade tidigare);
- kapacitet i sat: Total kanalkapacitet i satoshis;
- `push_msat`: Belopp i millisatoshis som initialt överförs till motparten när kanalen öppnas (här överför jag omedelbart 10 000 Sats så att han kan göra en överföring RGB senare);
- `asset_amount`: Belopp för RGB-tillgångar som ska överföras till kanalen;
- `tillgång_id`: Unik identifierare för den RGB-tillgång som är engagerad i kanalen;
- "Offentlig": Anger om kanalen ska göras offentlig för routing i nätverket.


![RGB-Bitcoin](assets/fr/111.webp)


För att bekräfta transaktionen bryts 6 block:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/fr/112.webp)


Lightning-kanalen är nu öppen och innehåller också 500 `PBN`-tokens på nod n°1:s sida. Om nod n°2 vill ta emot `PBN`-tokens måste den generate och Invoice. Så här gör du för att göra det:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Med:




- `amt_msat`: Invoice-belopp i millisatoshis (minst 3000 Sats);
- `expiry_sec`: Invoice:s expeditionstid i sekunder;
- `tillgång_id`: Identifierare för den RGB-tillgång som är associerad med Invoice;
- `tillgång_belopp`: Belopp för RGB-tillgång som ska överföras med denna Invoice.


Som svar får du en RGB Invoice (enligt beskrivningen i tidigare kapitel):


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/fr/113.webp)


Vi kommer nu att betala denna Invoice från den första noden, som har de nödvändiga kontanterna med `PBN` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/fr/114.webp)


Betalning har gjorts. Detta kan verifieras genom att köra kommandot:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/fr/115.webp)


Så här distribuerar du en Lightning-nod som är modifierad för att bära RGB-tillgångar. Denna demonstration är baserad på:




- En regtest-miljö (via `./regtest.sh`) eller Testnet;
- En Lightning-nod (`RGB-lightning-node`) baserad på en `bitcoind`, en indexerare och en `RGB-proxyserver`;
- En serie JSON REST API:er för att öppna/stänga kanaler, utfärda tokens, överföra tillgångar via Lightning etc.


Tack vare den här processen:




- Lightning engagement-transaktioner inkluderar en ytterligare utgång (OP_RETURN eller Taproot) med förankring av en RGB-övergång;
- Överföringar görs på exakt samma sätt som traditionella blixtbetalningar, men med tillägg av en RGB token;
- Flera RLN-noder kan kopplas samman för att dirigera och experimentera med betalningar över flera noder, förutsatt att det finns tillräcklig likviditet i både bitcoins och tillgång RGB på vägen.


Projektet befinner sig fortfarande i alfa-stadiet. Det rekommenderas därför starkt att du begränsar dig till testmiljöer (regtest, Testnet).


Möjligheterna som öppnas genom denna LN-RGB-kompatibilitet är betydande: stablecoins på Lightning, DEX Layer-2, överföring av fungibla tokens eller NFT:er till mycket låg kostnad ... I de föregående kapitlen har vi beskrivit den konceptuella arkitekturen och valideringslogiken. Nu har du en praktisk bild av hur du får en sådan nod igång, för din framtida utveckling eller tester.


# Sista avsnittet


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Recensioner & betyg


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## Slutsats


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>