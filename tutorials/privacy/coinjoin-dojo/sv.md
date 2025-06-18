---
name: CoinJoin - Dojo
description: Hur utför man en CoinJoin med sin egen Dojo?
---
![cover](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar inte Whirlpool-verktyget längre, inte ens för personer som har sin egen Dojo eller använder Sparrow Wallet. Det är dock fortfarande möjligt att detta verktyg kan återinföras under de kommande veckorna eller återlanseras på ett annat sätt. Dessutom är den teoretiska delen av denna artikel fortfarande relevant för att förstå principerna och målen för coinjoins i allmänhet (inte bara Whirlpool), samt för att förstå effektiviteten i Whirlpool-modellen.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

I den här handledningen lär du dig vad en CoinJoin är och hur du utför en med hjälp av Samourai Wallet-programvaran och Whirlpool-implementeringen, med hjälp av din egen Dojo. Enligt min mening är den här metoden för närvarande den bästa för att blanda dina bitcoins.


## Vad är en CoinJoin på Bitcoin?

**En CoinJoin är en teknik som bryter spårbarheten för bitcoins på Blockchain**. Den förlitar sig på en samarbetstransaktion med en specifik struktur med samma namn: CoinJoin-transaktionen.


Coinjoins förbättrar Bitcoin-användarnas integritet genom att komplicera kedjeanalysen för externa observatörer. Deras struktur gör det möjligt att slå samman flera mynt från olika användare till en enda transaktion, vilket suddar ut spåren och gör det svårt att fastställa länkarna mellan in- och utmatningsadresser.


Principen för CoinJoin bygger på ett samarbetsbaserat tillvägagångssätt: flera användare som vill blanda sina bitcoins sätter in identiska belopp som input i samma transaktion. Dessa belopp omfördelas sedan som outputs av lika värde till varje användare. I slutet av transaktionen blir det omöjligt att associera en specifik utgång med en känd användare vid ingången. Det finns ingen direkt länk mellan inputs och outputs, vilket bryter kopplingen mellan användarna och deras UTXO, liksom varje mynts historia.

![coinjoin](assets/notext/1.webp)


Exempel på en CoinJoin-transaktion (inte från mig): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


För att utföra en CoinJoin och samtidigt säkerställa att varje användare hela tiden har kontroll över sina medel börjar processen med att transaktionen konstrueras av en koordinator, som sedan skickar den till deltagarna. Varje användare signerar sedan transaktionen efter att ha verifierat att den passar dem. Alla insamlade signaturer integreras slutligen i transaktionen. Om en användare eller koordinatorn försöker avleda medel genom att modifiera CoinJoin-transaktionens utdata kommer signaturerna att visa sig vara ogiltiga, vilket leder till att noderna avvisar transaktionen.


Det finns flera implementeringar av CoinJoin, till exempel Whirlpool, JoinMarket eller Wabisabi, som alla syftar till att hantera samordning mellan deltagare och öka effektiviteten i CoinJoin-transaktioner.

I den här handledningen kommer vi att fördjupa oss i implementeringen av **Whirlpool**, som jag anser vara den mest effektiva lösningen för att utföra coinjoins på Bitcoin. Även om den finns tillgänglig på flera plånböcker, kommer vi i denna handledning uteslutande att utforska dess användning med Samourai Wallet mobilapplikation, utan Dojo.


## Varför utföra coinjoins på Bitcoin?

Ett av de första problemen med alla peer-to-peer-betalningssystem är dubbla utgifter: hur kan man förhindra att illvilliga individer spenderar samma monetära enheter flera gånger utan att en central myndighet måste agera som skiljedomare?


Satoshi Nakamoto gav en lösning på detta dilemma genom Bitcoin-protokollet, ett elektroniskt peer-to-peer-betalningssystem som fungerar oberoende av någon central myndighet. I sin vitbok betonar han att det enda sättet att certifiera att det inte förekommer några dubbla utgifter är att säkerställa att alla transaktioner inom betalningssystemet är synliga.


För att säkerställa att varje deltagare är medveten om transaktionerna måste de offentliggöras. Därför är Bitcoin:s verksamhet beroende av en transparent och distribuerad infrastruktur som gör det möjligt för alla nodoperatörer att verifiera hela kedjan av elektroniska signaturer och varje mynts historia, från det att det skapades av Miner.


Bitcoin:s Blockchain:s transparenta och distribuerade natur innebär att alla användare av nätverket kan följa och analysera alla andra deltagares transaktioner. Som ett resultat av detta är anonymitet på transaktionsnivå omöjlig. Anonymiteten bevaras dock på nivån för individuell identifiering. Till skillnad från det traditionella banksystemet där varje konto är kopplat till en personlig identitet, är medel i Bitcoin kopplade till par av kryptografiska nycklar, vilket ger användarna en form av pseudonymitet bakom kryptografiska identifierare.


Således äventyras konfidentialiteten på Bitcoin när externa observatörer lyckas associera specifika UTXO:er med identifierade användare. När denna koppling väl är etablerad blir det möjligt att spåra deras transaktioner och analysera historiken för deras bitcoins. CoinJoin är just en teknik som utvecklats för att bryta spårbarheten hos UTXO:er och därigenom erbjuda en viss Layer konfidentialitet för Bitcoin-användare på transaktionsnivå.


## Hur fungerar Whirlpool?

Whirlpool skiljer sig från andra CoinJoin-metoder genom att använda "_ZeroLink_"-transaktioner, som säkerställer att det inte finns någon teknisk koppling mellan alla inmatningar och alla utmatningar. Denna perfekta blandning uppnås genom en struktur där varje deltagare bidrar med ett identiskt belopp i input (med undantag för Mining-avgifter), vilket genererar outputs av perfekt lika stora belopp.

Detta restriktiva förhållningssätt till insatsvaror ger Whirlpool CoinJoin-transaktionerna en unik egenskap: den fullständiga avsaknaden av deterministiska kopplingar mellan insatsvaror och utdata. Med andra ord är det lika stor sannolikhet att varje output tillskrivs någon deltagare jämfört med alla andra outputs i transaktionen.

Inledningsvis var antalet deltagare i varje Whirlpool CoinJoin begränsat till 5, med 2 nya deltagare och 3 remixare (vi kommer att förklara dessa begrepp längre fram). Ökningen av transaktionsavgifterna i On-Chain som observerades 2023 fick dock Samourai-teamen att ompröva sin modell för att förbättra integriteten och samtidigt minska kostnaderna. Med hänsyn till marknadssituationen för avgifter och antalet deltagare kan samordnaren nu organisera coinjoins med 6, 7 eller 8 deltagare. Dessa förbättrade sessioner kallas "_Surge Cycles_". Det är viktigt att notera att det, oavsett upplägg, alltid bara finns 2 nya deltagare i Whirlpool coinjoins.


Whirlpool-transaktioner kännetecknas således av ett identiskt antal in- och utgångar, som kan vara:


- 5 ingångar och 5 utgångar;

![coinjoin](assets/notext/2.webp)


- 6 ingångar och 6 utgångar;

![coinjoin](assets/notext/3.webp)


- 7 ingångar och 7 utgångar;

![coinjoin](assets/notext/4.webp)


- 8 ingångar och 8 utgångar.

![coinjoin](assets/notext/5.webp)

Den modell som Whirlpool föreslår baseras således på små CoinJoin-transaktioner. Till skillnad från Wasabi och JoinMarket, där robustheten hos anonsets är beroende av volymen deltagare i en enda cykel, satsar Whirlpool på kedjandet av flera små cykler.


I den här modellen betalar användaren avgifter endast när de först kommer in i en pool, vilket gör att de kan delta i en mängd olika remixer utan ytterligare avgifter. Det är de nya deltagarna som täcker Mining-avgifterna för remixarna.


Med varje ytterligare CoinJoin som ett mynt deltar i, tillsammans med dess tidigare påträffade kamrater, kommer anonsets att växa exponentiellt. Målet är således att dra nytta av dessa gratis remixer som, med varje förekomst, bidrar till att öka tätheten av de anonsets som är associerade med varje blandat mynt.


Whirlpool utformades med hänsyn till två viktiga krav:


- Tillgängligheten för implementering på mobila enheter, med tanke på att Samourai Wallet främst är en smartphone-applikation;
- Hastigheten på omblandningscyklerna för att främja en betydande ökning av anonsets.

Dessa krav styrde de val som utvecklarna av Samourai Wallet gjorde vid utformningen av Whirlpool, och ledde dem till att begränsa antalet deltagare per cykel. För få deltagare skulle ha äventyrat effektiviteten i CoinJoin och drastiskt minskat antalet anonsets som genereras varje cykel, medan för många deltagare skulle ha medfört hanteringsproblem i mobilapplikationer och skulle ha hindrat cykelflödet.

**I slutändan finns det inget behov av att ha ett högt antal deltagare per CoinJoin på Whirlpool eftersom anonsets uppnås genom ackumulering av flera CoinJoin cykler.**


[-> Läs mer om Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Avgifter för pooler och CoinJoin

För att dessa multipla cykler effektivt ska öka de blandade myntens anonset måste ett visst ramverk upprättas för att begränsa de mängder UTXO som används. Whirlpool definierar således olika pooler.


En pool representerar en grupp användare som vill mixa tillsammans och som kommer överens om mängden UTXO som ska användas för att optimera CoinJoin-processen. Varje pool anger ett fast belopp för UTXO, som användaren måste följa för att kunna delta. För att utföra coinjoins med Whirlpool måste du alltså välja en pool. De pooler som för närvarande är tillgängliga är följande:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Genom att gå med i en pool med dina bitcoins kommer de att delas upp i generate UTXO:er som är helt homogena med de andra deltagarna i poolen. Varje pool har en maxgräns; för belopp som överstiger denna gräns kommer du därför att tvingas antingen göra två separata poster inom samma pool eller flytta till en annan pool med ett högre belopp:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Som tidigare nämnts anses en UTXO tillhöra en pool när den är redo att integreras i en CoinJoin. Detta innebär dock inte att användaren förlorar besittningen av den. **Genom de olika blandningscyklerna behåller du full kontroll över dina nycklar och följaktligen dina bitcoins.** Det är detta som skiljer CoinJoin-tekniken från andra centraliserade blandningstekniker.


För att delta i en CoinJoin-pool måste serviceavgifter samt Mining-avgifter betalas. Serviceavgifterna är fasta för varje pool och är avsedda att kompensera de team som ansvarar för utveckling och underhåll av Whirlpool.

Serviceavgifter för att använda Whirlpool ska betalas endast en gång när du går in i poolen. Efter detta steg har du möjlighet att delta i ett obegränsat antal remixer utan några ytterligare avgifter. Här är de aktuella fasta avgifterna för varje pool:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Dessa avgifter fungerar i huvudsak som en inträdesbiljett till den valda poolen, oavsett vilket belopp du lägger i CoinJoin. Oavsett om du går med i 0,01-poolen med exakt 0,01 BTC eller går in i den med 0,5 BTC, kommer avgifterna att förbli desamma i absolut värde.


Innan användaren går vidare till coinjoins kan han eller hon därför välja mellan två strategier:


- Välj en mindre pool för att minimera serviceavgifterna, i vetskap om att de kommer att få flera små UTXO:er i gengäld;
- Eller föredrar en större pool och går med på att betala högre avgifter för att i slutändan få ett minskat antal UTXO:er med högre värde.


Det avråds generellt från att slå samman flera blandade UTXO:er efter CoinJoin-cyklerna, eftersom detta kan äventyra den förvärvade sekretessen, särskilt på grund av CIOH-heuristiken (Common-Input-Ownership Heuristic). Därför kan det vara klokt att välja en större pool, även om det innebär att betala mer, för att undvika att få för många UTXO:er med litet värde vid utgången. Användaren måste väga in dessa avvägningar för att välja den pool som han eller hon föredrar.


Förutom serviceavgifterna måste även Mining-avgifterna som ingår i alla Bitcoin-transaktioner beaktas. Som Whirlpool-användare kommer du att behöva betala Mining-avgifterna för förberedelsetransaktionen (`Tx0`) samt för den första CoinJoin. Alla efterföljande remixer kommer att vara gratis, tack vare Whirlpool:s modell som bygger på betalning av nya deltagare.


I varje Whirlpool CoinJoin är två användare bland de inmatade uppgifterna faktiskt nya aktörer. De andra inmatningarna kommer från remixare. Följaktligen täcks Mining-avgifterna för alla deltagare i transaktionen av dessa två nya deltagare, som sedan också kommer att dra nytta av gratis remixer:

![coinjoin](assets/en/6.webp)

Tack vare detta avgiftssystem skiljer sig Whirlpool verkligen från andra CoinJoin-tjänster eftersom UTXO:ernas anonymitet inte står i proportion till det pris som användaren betalar. Det är således möjligt att uppnå avsevärt höga anonymitetsnivåer genom att endast betala poolens inträdesavgift och Mining-avgifterna för två transaktioner (`Tx0` och den initiala mixen).

Det är viktigt att notera att användaren också måste täcka Mining-avgifterna för att ta ut sina UTXO från poolen efter att ha slutfört sina flera coinjoins, såvida de inte har valt alternativet "mixa till", som vi kommer att diskutera i handledningen nedan.


### HD Wallet konton som används av Whirlpool

För att utföra en CoinJoin via Whirlpool måste Wallet generate flera distinkta konton. Ett konto, i samband med en HD (*Hierarkical Deterministic*) Wallet, utgör en sektion som är helt isolerad från de andra, denna separation sker på den tredje djupnivån i Wallet:s hierarki, det vill säga på nivån för "xpub".


En HD Wallet kan teoretiskt härleda upp till `2^(32/2)` olika konton. Det första kontot, som används som standard på alla Bitcoin-plånböcker, motsvarar indexet `0`.


För plånböcker som är anpassade till Whirlpool, som Samourai eller Sparrow, används 4 konton för att tillgodose behoven i CoinJoin-processen:


- Kontot **deposit**, identifierat med indexet `0`;
- Kontot **bad bank** (eller doxxic change), identifierat genom indexet `2 147 483 644'`;
- Kontot **premix**, identifierat genom indexet "2 147 483 645";
- Kontot **postmix**, identifierat genom indexet "2 147 483 646".


Vart och ett av dessa konton fyller en specifik funktion inom CoinJoin.


Alla dessa konton är länkade till en enda seed, vilket gör det möjligt för användaren att återställa åtkomst till alla sina bitcoins med hjälp av sin återställningsfras och, om det behövs, deras passphrase. Det är dock nödvändigt att under denna återställningsoperation ange de olika kontoindex som användes för programvaran.


Låt oss nu titta på de olika stadierna av en Whirlpool CoinJoin inom dessa konton.


### De olika stadierna av coinjoins på Whirlpool

**Steg 1: Tx0**

Utgångspunkten för alla Whirlpool CoinJoin är **deposit**-kontot. Det här kontot är det som du automatiskt använder när du skapar en ny Bitcoin Wallet. Detta konto måste krediteras med de bitcoins som man vill blanda.

`Tx0` representerar det första steget i Whirlpool-blandningsprocessen. Det syftar till att förbereda och utjämna UTXO för CoinJoin genom att dela upp dem i enheter som motsvarar mängden av den valda poolen, för att säkerställa homogeniteten i blandningen. De utjämnade UTXO skickas sedan till **premix**-kontot. När det gäller skillnaden som inte kan komma in i poolen separeras den till ett specifikt konto: **bad bank** (eller "doxxic change").

Denna inledande transaktion `Tx0` tjänar också till att reglera de serviceavgifter som ska betalas till mixsamordnaren. Till skillnad från de följande stegen är denna transaktion inte ett samarbete; användaren måste därför stå för alla Mining-avgifter:

![coinjoin](assets/en/7.webp)


I detta exempel på en `Tx0`-transaktion delas en inmatning på `372 000 Sats` från vårt **deposit**-konto upp i flera utmatningar UTXO, som fördelas enligt följande:


- Ett belopp på 5 000 Sats` avsett för samordnaren för serviceavgifter, motsvarande inträdet i poolen på 100 000 Sats`;
- Tre UTXO förberedda för mixning, omdirigerade till vårt **premix**-konto och registrerade hos koordinatorn. Dessa UTXO utjämnas till 108 000 Sats vardera för att täcka Mining-avgifterna för deras framtida inledande mixning;
- Det överskott som inte kan komma in i poolen, eftersom det är för litet, betraktas som en giftig förändring. Den skickas till sitt specifika konto. Här uppgår denna förändring till "40 000 Sats";
- Slutligen finns det "3 000 Sats" som inte utgör en output, utan är de Mining-avgifter som krävs för att bekräfta "Tx0".


Här är till exempel en riktig Whirlpool Tx0 (inte från mig): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Steg 2: Den doxiska förändringen**

Överskottet som inte kunde integreras i poolen, här motsvarande "40 000 Sats", omdirigeras till kontot **bad bank**, även kallat "doxxic change", för att säkerställa en strikt separation från de andra UTXO i Wallet.


Denna UTXO är farlig för användarens integritet eftersom den inte bara fortfarande är kopplad till sitt förflutna, och därför möjligen till sin ägares identitet, utan dessutom är noterad som tillhörande en användare som har utfört en CoinJoin.

Om denna UTXO slås samman med blandade utdata kommer de att förlora all den sekretess som uppnåtts under CoinJoin-cyklerna, särskilt på grund av Common-Input-Ownership-Heuristic (CIOH). Om det slås samman med andra doxiska förändringar riskerar användaren att förlora sekretessen eftersom detta kommer att länka samman de olika ingångarna i CoinJoin-cyklerna. Därför måste den hanteras med försiktighet. Sättet att hantera denna giftiga UTXO kommer att beskrivas i den sista delen av denna artikel, och framtida handledningar kommer att täcka dessa metoder mer noggrant på PlanB Network.


**Steg 3: Den inledande mixen**

När `Tx0` har slutförts skickas de utjämnade UTXO:erna till **premix**-kontot i vår Wallet, redo att introduceras i sin första CoinJoin-cykel, även kallad "initial mix". Om, som i vårt exempel, `Tx0` genererar flera UTXO:er avsedda för blandning, kommer var och en av dem att integreras i en separat initial CoinJoin.


I slutet av dessa första mixar kommer **premix**-kontot att vara tomt, medan våra mynt, som har betalat Mining-avgifterna för denna första CoinJoin, kommer att justeras exakt till det belopp som definieras av den valda poolen. I vårt exempel kommer våra ursprungliga UTXO:er på 108 000 Sats att ha reducerats till exakt 100 000 Sats.

![coinjoin](assets/en/8.webp)

**Steg 4: Remixerna**

Efter den första mixningen överförs UTXO:erna till kontot **postmix**. Detta konto samlar de redan mixade UTXO:erna och de som väntar på remixning. När Whirlpool-klienten är aktiv är de UTXO:er som finns på kontot **postmix** automatiskt tillgängliga för omblandning och kommer slumpmässigt att väljas ut för att delta i dessa nya cykler.


Som en påminnelse är remixerna sedan 100% gratis: inga ytterligare serviceavgifter eller Mining-avgifter krävs. Att hålla UTXO:erna på **postmix**-kontot bibehåller således deras värde intakt och förbättrar samtidigt deras anonsets. Det är därför det är viktigt att låta dessa mynt delta i flera CoinJoin-cykler. Det kostar dig absolut ingenting, och det ökar deras anonymitetsnivåer.


När du bestämmer dig för att spendera blandade UTXO:er kan du göra det direkt från detta **postmix**-konto. Det är tillrådligt att behålla de blandade UTXO:erna på detta konto för att dra nytta av gratis remixer och för att undvika att de lämnar Whirlpool-kretsen, vilket kan minska deras konfidentialitet.


Som vi kommer att se i följande handledning finns det också alternativet "mixa till" som ger möjlighet att automatiskt skicka dina blandade mynt till en annan Wallet, till exempel en Cold Wallet, efter ett definierat antal coinjoins.

Efter att ha gått igenom teorin, låt oss dyka in i praktiken med en handledning om hur man använder Whirlpool genom Samourai Wallet Android-applikationen, synkroniserad med Whirlpool CLI och GUI på din egen Dojo!

## Självstudier: CoinJoin Whirlpool med din egen dojo

Det finns många alternativ för att använda Whirlpool. Det jag vill presentera här är Samourai Wallet-alternativet, en öppen källkod Bitcoin Wallet-hanteringsapplikation på Android, men den här gången **med din egen Dojo**.


Att utföra coinjoins via Samourai Wallet med hjälp av din egen Dojo är enligt min mening den mest effektiva strategin för att genomföra coinjoins på Bitcoin hittills. Detta tillvägagångssätt kräver en viss initial investering när det gäller installation, men när den väl är på plats erbjuder den möjligheten att mixa och remixa dina bitcoins kontinuerligt, 24 timmar om dygnet, 7 dagar i veckan, utan att behöva hålla din Samourai-applikation aktiv hela tiden. Tack vare att Whirlpool CLI fungerar på en Bitcoin-nod är du alltid redo att delta i coinjoins. Samourai-applikationen ger dig sedan möjlighet att spendera dina blandade medel när som helst, var du än befinner dig, direkt från din smartphone. Dessutom har denna metod fördelen att den aldrig ansluter dig till servrar som hanteras av Samourai-teamen, vilket skyddar din `xpub` från all extern exponering.


Denna teknik är därför idealisk för dem som vill ha maximal integritet och CoinJoin-cykler av högsta kvalitet. Det kräver dock att du har en Bitcoin-nod till ditt förfogande och, som vi kommer att se senare, kräver det en del installation. Den är därför mer lämpad för användare på mellannivå till avancerad nivå. För nybörjare rekommenderar jag att man bekantar sig med CoinJoin genom dessa två andra handledningar, som visar hur man gör det från Sparrow Wallet eller Samourai Wallet (utan Dojo):


- [Sparrow Wallet CoinJoin tutorial](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### Förstå inställningarna

Till att börja med kommer du att behöva en Dojo! Dojo är en Bitcoin-nodimplementering baserad på Bitcoin Core, utvecklad av Samourai-teamen.


För att köra din egen Dojo har du möjlighet att antingen installera en Dojo-nod självständigt eller dra nytta av Dojo ovanpå en annan "node-in-box" Bitcoin-nodlösning. För närvarande är de tillgängliga alternativen:


- [RoninDojo](https://ronindojo.io/), som är en Dojo förbättrad med ytterligare verktyg, inklusive en installationsassistent och en administrationsassistent. Jag beskriver i detalj hur man installerar och använder RoninDojo i denna andra handledning: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel] (https://umbrel.com/) med applikationen "Samourai Server";
- [MyNode] (https://mynodebtc.com/) med applikationen "Dojo";
- [Nodl] (https://www.nodl.eu/) med applikationen "Dojo";
- [Citadel] (https://runcitadel.space/) med applikationen "Samourai".

![coinjoin](assets/notext/9.webp)

I vår installation kommer vi att interagera med tre olika gränssnitt:


- Samourai Wallet**, som kommer att vara värd för vår Bitcoin Wallet tillägnad coinjoins. Denna FOSS-applikation är tillgänglig gratis på Android och låter dig styra din mixning Wallet, särskilt för att spendera din postmix från din smartphone;
- Whirlpool CLI** (_Command Line Interface_), som kommer att fungera på den nod som är värd för Dojo. Denna programvara kommer att ha tillgång till nycklarna till din Samourai Wallet. Den är ansvarig för att kommunicera med koordinatorn och hantera coinjoins kontinuerligt. Den fungerar som en kopia av din Samourai Wallet på din nod, redo att delta i coinjoins när som helst;
- Whirlpool GUI** (_Graphical User Interface_), den grafiska användaren Interface som vi kommer att använda för att övervaka aktiviteten hos Whirlpool CLI och initiera mixning på distans. Whirlpool GUI ger en visuell representation av de operationer som utförs av Whirlpool CLI. Denna programvara måste installeras på en dator som är skild från Dojo. För användare av Umbrel, MyNode, Nodl och Citadel är Whirlpool GUI obligatoriskt. Men med RoninDojo är Whirlpool GUI Interface redan integrerat i din nods webb Interface via programmet `Whirlpool`. Därför behöver du inte installera den på en separat dator.


Enligt min mening är RoninDojo den bästa lösningen för att utföra coinjoins med en Dojo. Eftersom denna nod-i-box-programvara är i direkt partnerskap med Samourai-teamen är RoninDojo mycket mer optimerad för att göra detta. Dessutom förenklar integrationen av Whirlpool GUI i webben Interface avsevärt installationsprocessen. I den här handledningen kommer jag fortfarande att förklara hur man gör det med de andra lösningarna som integrerar Dojo (Umbrel, Nodl, MyNode och Citadel).


### Förbereda din dojo

För att börja måste du installera Dojo och få QR-koden eller länken som gör att du kan ansluta till den på distans. Den här länken är en Tor Address som slutar på `.onion`. Om du använder RoninDojo navigerar du helt enkelt till menyn `Pairing` för att komma åt den här informationen.

![coinjoin](assets/notext/10.webp)


Under `Samourai Dojo`, klicka på `Para nu` knappen.


![coinjoin](assets/notext/11.webp)


QR-koden för din anslutning och motsvarande länk kommer att visas.


![coinjoin](assets/notext/12.webp)


Om du är på Umbrel, gå till App Store och sök efter applikationen `Samourai Server`. Den finns i fliken `Bitcoin`.


![coinjoin](assets/notext/13.webp)


Installera programmet.


![coinjoin](assets/notext/14.webp)


När du öppnar applikationen kommer du att få tillgång till QR-koden för att ansluta till din Dojo.


![coinjoin](assets/notext/15.webp)


Om du använder en annan node-in-box-programvara som MyNode, Citadel eller Nodl är processen liknande den för Umbrel. Du måste installera Samourai- eller Dojo-programmet för att få den information som behövs för att ansluta till din Dojo.


![coinjoin](assets/notext/16.webp)


### Förberedelse av din Samourai Wallet

Efter att ha hämtat anslutningsinformationen till din Dojo är det nu dags att ställa in din Wallet för coinjoins. Det finns två scenarier: om du ännu inte har en Samourai Wallet på din smartphone är processen enkel, det är bara att skapa en ny.


Om du däremot redan har en Samourai Wallet måste du installera om programmet för att koppla det till en ny Dojo. Detta steg är nödvändigt eftersom anslutningen till en Dojo endast kan upprättas vid den första lanseringen av applikationen. Tack vare den automatiskt genererade krypterade säkerhetskopian från Samourai på din telefon är denna procedur dock enkel och snabb.


*Om du aldrig har använt Samourai kan du hoppa över de här inledande stegen och fortsätta direkt till installationen av programmet.*


Först och främst bör du kontrollera att din Samourai Wallet-applikation är uppdaterad. För att göra detta, kontrollera Google Play Store eller jämför versionen av din applikation i `Inställningar > Övrigt` med den som finns tillgänglig på Samourais webbplats.


![coinjoin](assets/notext/17.webp)


Se till att du har din Samourai Wallet återställningsfras och att den är läsbar. Gör sedan ett test av din BIP39 passphrase genom att navigera till `Inställningar > Felsökning > passphrase/Backup-test` för att bekräfta dess noggrannhet.


![coinjoin](assets/notext/18.webp)

Ange din passphrase och kontrollera sedan att Samourai bekräftar att den är giltig.

![coinjoin](assets/notext/19.webp)


Om din passphrase är ogiltig, eller om du inte har din återställningsfras, är det absolut nödvändigt att omedelbart stoppa proceduren! **I det här fallet rekommenderas att du överför dina pengar till en annan Wallet och börjar med en ny tom Samourai Wallet. Följande steg bör endast följas om du är säker på att du har all nödvändig säkerhetskopieringsinformation och att din passphrase är giltig.


Fortsätt sedan med att skapa en krypterad säkerhetskopia av din Wallet och kopiera den till ditt urklipp. För att utföra denna operation, klicka på de tre små prickarna längst upp till höger på skärmen och välj sedan `Export Wallet backup`.


![coinjoin](assets/notext/20.webp)


**Från och med detta steg ska du inte kopiera något annat till ditt urklipp! ** Det är absolut nödvändigt att du behåller din kopierade säkerhetskopia.


Om du har utfört de föregående stegen korrekt kan du nu på ett säkert sätt radera din Samourai Wallet. För att göra detta, gå till: `Inställningar > Wallet > Säker radering av Wallet`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Om du aldrig har använt Samourai och installerar programmet från början kan du fortsätta handledningen i detta steg.*


Din Samourai-applikation är nu återställd. Öppna applikationen och fortsätt med installationsstegen som om du använde den för första gången.


![coinjoin](assets/notext/23.webp)


I nästa steg kommer du till sidan där du kan konfigurera din Dojo. Välj alternativet `Dojo` och ange sedan inloggningsuppgifterna för din Dojo. För att göra detta har du möjlighet att skanna informationen genom att trycka på `Scan QR`.


![coinjoin](assets/notext/24.webp)


*För nya användare av Samourai blir det då nödvändigt att skapa en Wallet från början. Om du behöver hjälp kan du läsa instruktionerna för att konfigurera en ny Samourai Wallet [i den här handledningen, särskilt i avsnittet "Skapa en Software Wallet"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*


Om du fortsätter med återställningen av en redan befintlig Samourai Wallet, välj `Restore existing Wallet`, välj sedan `I have a Samourai backup file`.


![coinjoin](assets/notext/25.webp)

Normalt bör du alltid ha din återställningsfil i ditt urklipp. Klicka sedan på `PASTE` för att infoga din fil på den angivna platsen. För att dekryptera det kommer det också att vara nödvändigt att ange BIP39 passphrase för din Wallet i motsvarande fält, som ligger precis nedanför. För att avsluta, klicka på `FINISH`.

![coinjoin](assets/notext/26.webp)


Du kommer sedan att omdirigeras till din Samourai Wallet som den här gången kommer att vara ansluten till din egen Dojo.


![coinjoin](assets/notext/27.webp)


### Installera Whirlpool GUI

Det är nu dags att installera Whirlpool GUI, den grafiska användaren Interface som gör att du kan hantera dina CoinJoin-cykler från din vanliga PC. För RoninDojo-användare är detta steg inte nödvändigt eftersom hanteringen av coinjoins kan göras direkt via webben Interface i `Apps > Whirlpool`. Men om du använder en annan Bitcoin "node-in-box"-lösning är det absolut nödvändigt att fortsätta med denna installation.

![coinjoin](assets/notext/28.webp)

Gå till din dator och ladda ner programvaran Whirlpool från den officiella Samourai Wallet-webbplatsen och välj den version som motsvarar ditt operativsystem.


![coinjoin](assets/notext/29.webp)


Innan du startar Whirlpool GUI är det nödvändigt att installera JAVA 8 eller en högre version på din maskin. För detta kan [du installera OpenJDK] (https://adoptium.net/).

![coinjoin](assets/notext/30.webp)

Det är också nödvändigt att ha Tor daemon eller Tor Browser i drift i bakgrunden på din dator. Se till att starta Tor före varje användningssession av Whirlpool GUI. Om Tor ännu inte är installerat på din dator, [du kan ladda ner och installera det från den officiella projektwebbplatsen](https://www.torproject.org/download/), se till att starta det i bakgrunden.


![coinjoin](assets/notext/31.webp)


När JDK har installerats på ditt system och Tor har startats i bakgrunden kan du starta Whirlpool GUI.


![coinjoin](assets/notext/32.webp)


Från Whirlpool GUI, klicka på `Avancerat: Remote CLI` för att ansluta din Whirlpool CLI som finns på din Dojo. Du kommer att behöva Tor Address för din Whirlpool CLI.


![coinjoin](assets/notext/33.webp)


För att hitta din Tor Address på Umbrel och andra "node-in-box"-lösningar startar du helt enkelt Samourai Server eller Dojo-applikationen (namnet kan variera beroende på vilken programvara som används). Tor Address kommer att vara direkt synlig på applikationens sida.

![coinjoin](assets/notext/34.webp)

I Whirlpool GUI anger du Tor Address som du fick tidigare i fältet `CLI Address`. Behåll prefixet `http://`, men lägg inte till porten `:8899` i slutet. Klistra bara in Address så som du fick den.

![coinjoin](assets/notext/35.webp)


I fältet Tor Proxy anger du `socks5://127.0.0.1:9050` om du använder Tor daemon, eller `socks5://127.0.0.1:9150` om det är Tor Browser. När du först ansluter till Whirlpool CLI via Whirlpool GUI är det möjligt att lämna API-nyckelfältet tomt. Om detta inte är din första anslutning, vänligen ange din API-nyckel i det dedikerade utrymmet. Den här nyckeln kan finnas på samma sida som din Tor Address.


![coinjoin](assets/notext/36.webp)


När du har fyllt i alla uppgifter klickar du på knappen "Anslut". Vänligen vänta, anslutningen kan ta några minuter.


![coinjoin](assets/notext/37.webp)


### Para ihop din Samourai Wallet med Whirlpool GUI

*För RoninDojo-användare kan du återuppta handledningen här.*


Vi kommer nu att para ihop Samourai Wallet som vi konfigurerade tidigare med Whirlpool GUI-programvaran, eller direkt med RoninDojo för dem som använder denna programvara. Oavsett om du använder Whirlpool GUI eller RoninDojo kommer du att bli ombedd att klistra in eller skanna parningsinformationen för din Samourai Wallet.


![coinjoin](assets/notext/38.webp)


Du hittar den här informationen genom att gå till inställningarna för din Wallet.


![coinjoin](assets/notext/39.webp)


Klicka på `Transaktioner` och sedan på `Para till Whirlpool GUI`.


![coinjoin](assets/notext/40.webp)


Samourai kommer sedan att förse dig med den information som krävs för att upprätta anslutningen. Var försiktig, dessa uppgifter är känsliga! Du kan överföra dem till din dator antingen genom att kopiera dem direkt eller genom att skanna den QR-kod som visas med hjälp av datorns webbkamera efter att ha klickat på QR-kodsymbolen.


![coinjoin](assets/notext/41.webp)


Efter att ha utfört denna operation, i Whirlpool GUI, välj `Initialize GUI`. Vänligen vänta, eftersom detta steg kan ta en stund.


![coinjoin](assets/notext/42.webp)


Oavsett om du använder Whirlpool GUI eller RoninDojo, kommer du att bli ombedd att ange passphrase för din Samourai Wallet. Skriv in den i det avsedda fältet och tryck sedan på knappen `Login` för att fortsätta.


![coinjoin](assets/notext/43.webp)


Du kommer då att komma till hemsidan för Whirlpool CLI


![coinjoin](assets/notext/44.webp)


### Initiering av coinjoins från Whirlpool GUI

*För RoninDojo-användare är processen som ska följas identisk. Whirlpool-appen Interface som är integrerad i RoninDojo erbjuder samma alternativ och funktioner som Whirlpool GUI-programvaran på skrivbordet. Därför kan du följa dessa instruktioner på samma sätt.*

Nu när allt är konfigurerat är du redo att börja blanda dina bitcoins. För att göra detta överför du de bitcoins du vill blanda till **Deposit**-kontot på din Samourai Wallet. Denna operation kan utföras antingen direkt via Samourai Wallet-appen eller på Whirlpool GUI. Från huvudsidan klickar du på knappen `+ Insättning` längst upp till vänster.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI kommer att generate en mottagande Address. Det kommer också att visa det lägsta belopp som krävs för att delta i varje CoinJoin-pool. Detta belopp varierar beroende på avgiftsmarknaden. Det är tillrådligt att sätta in ett belopp som är något högre än det lägsta som krävs, eftersom om Mining-avgifterna inte minskar kanske din UTXO inte accepteras i önskad pool. Skicka därför dina bitcoins till den tillhandahållna Address. För att få en ny Address klickar du bara på knappen `Renew Address`.


![coinjoin](assets/notext/46.webp)


När insättningen har bekräftats kommer du att kunna se den i kontot **Deposit** på Whirlpool GUI.


![coinjoin](assets/notext/47.webp)


För att starta CoinJoin-cyklerna väljer du de UTXO:er som du vill blanda och trycker på knappen `Premix`. Var försiktig: om du väljer flera olika UTXO:er samtidigt kommer de att kombineras under förberedelsetransaktionen för `TX0`. Denna sammanslagning kan leda till minskad integritet, särskilt om UTXO:erna kommer från olika källor, på grund av Common Input Ownership Heuristic (CIOH).


![coinjoin](assets/notext/48.webp)


Whirlpool:s konfigurationssida öppnas. Du kan välja vilken pool du vill gå in i. Välj också Mining-avgifterna som är avsedda för `TX0` och de första coinjoins. Längst ner på denna sida kommer en sammanfattning att presentera dig med mängden doxxisk förändring samt mängden och antalet UTXO som kommer att utjämnas och inkluderas i CoinJoin-cyklerna. Om du är nöjd med denna konfiguration, tryck på `Premix`-knappen för att starta CoinJoin-cyklerna.

![coinjoin](assets/notext/49.webp)


När `TX0` har skapats kommer du att kunna se dina utjämnade UTXO:er i **Premix**-kontot, i väntan på bekräftelse. För att dina mynt ska kunna remixas automatiskt 24 timmar om dygnet, 7 dagar i veckan, rekommenderar jag att du aktiverar alternativet `Automatiskt mixa premix & postmix`. Du hittar den här funktionen i fliken `Konfiguration`, som finns till vänster om ditt Whirlpool GUI-fönster.

![coinjoin](assets/notext/50.webp)

När du har startat coinjoins kan du avsluta Whirlpool GUI samt Samourai Wallet. Endast din nod behöver förbli ansluten för att kunna delta i kontinuerliga coinjoins. Det är dock lämpligt att regelbundet kontrollera framstegen i dina CoinJoin-cykler. Om du märker att dina UTXO:er inte längre väljs för en CoinJoin under en tid kan detta tyda på en bugg. I så fall, gå till Whirlpool CLI och välj `Start` för att starta om din tillgänglighet för coinjoins.


![coinjoin](assets/notext/51.webp)


Dina blandade UTXO:er är synliga från **Postmix**-kontot på Whirlpool GUI. Dessutom har du möjlighet att visa och spendera dem direkt via Whirlpool Interface på din Samourai Wallet. För att komma åt den här menyn, klicka på det blå `+` längst ner på skärmen och välj sedan `Whirlpool`.


![coinjoin](assets/notext/52.webp)


Whirlpool-konton är lätt identifierbara på Samourai Wallet genom sin blå färg. Detta gör att du kan spendera dina blandade UTXO:er var som helst och när som helst, direkt från din smartphone.


![coinjoin](assets/notext/53.webp)


För att hålla reda på dina automatiska coinjoins rekommenderar jag också att du skapar en Watch-only wallet via Sentinel-appen. Lägg till ZPUB för ditt **Postmix**-konto och övervaka utvecklingen av dina CoinJoin-cykler i realtid. Om du vill förstå hur du använder Sentinel rekommenderar jag att du läser den här andra handledningen på PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)