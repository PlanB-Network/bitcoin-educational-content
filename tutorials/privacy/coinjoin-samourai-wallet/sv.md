---
name: CoinJoin - Samourai Wallet
description: Hur utför man en CoinJoin på Samourai Wallet?
---
![cover](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Whirlpool-verktyget inte längre, inte ens för personer som har sin egen Dojo eller använder Sparrow Wallet. Det är dock fortfarande möjligt att detta verktyg kan återinföras under de kommande veckorna eller återlanseras på ett annat sätt. Dessutom är den teoretiska delen av denna artikel fortfarande relevant för att förstå principerna och målen för coinjoins i allmänhet (inte bara Whirlpool), samt för att förstå effektiviteten i Whirlpool-modellen.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg för kriminella ändamål. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *en Bitcoin Wallet för gatorna*

I den här handledningen lär du dig vad en CoinJoin är och hur du utför en CoinJoin med hjälp av Samourai Wallet-programvaran och Whirlpool-implementeringen.


## Vad är en CoinJoin på Bitcoin?

**CoinJoin är en teknik som bryter spårbarheten för bitcoins på Blockchain**. Den förlitar sig på en samarbetstransaktion med en specifik struktur med samma namn: CoinJoin-transaktionen.


Coinjoins förbättrar Bitcoin-användarnas integritet genom att komplicera kedjeanalysen för externa observatörer. Deras struktur gör det möjligt att slå samman flera mynt från olika användare till en enda transaktion, vilket döljer spåren och gör det svårt att fastställa länkarna mellan in- och utmatningsadresser.


Principen för CoinJoin bygger på ett samarbetsbaserat tillvägagångssätt: flera användare som vill blanda sina bitcoins sätter in identiska belopp som input i samma transaktion. Dessa belopp omfördelas sedan som outputs av lika värde till varje användare. I slutet av transaktionen blir det omöjligt att associera en specifik output med en känd användare i input. Det finns ingen direkt länk mellan inputs och outputs, vilket bryter kopplingen mellan användare och deras UTXO, liksom varje mynts historia.

![coinjoin](assets/notext/1.webp)


Exempel på en CoinJoin-transaktion (inte från mig): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


För att genomföra en CoinJoin och samtidigt säkerställa att varje användare hela tiden har kontroll över sina medel börjar processen med att en koordinator skapar transaktionen, som sedan överförs till deltagarna. Varje användare signerar sedan transaktionen efter att ha verifierat att den passar dem. Alla insamlade signaturer integreras slutligen i transaktionen. Om en användare eller koordinatorn försöker avleda medel genom att ändra utdata från CoinJoin-transaktionen kommer signaturerna att visa sig vara ogiltiga, vilket leder till att noderna avvisar transaktionen.


Det finns flera implementeringar av CoinJoin, till exempel Whirlpool, JoinMarket eller Wabisabi, som alla syftar till att hantera samordning mellan deltagare och öka effektiviteten i CoinJoin-transaktioner.

I den här handledningen kommer vi att fördjupa oss i implementeringen av **Whirlpool**, som jag anser vara den mest effektiva lösningen för att utföra coinjoins på Bitcoin. Även om den finns tillgänglig på flera plånböcker, kommer vi i denna handledning uteslutande att utforska dess användning med Samourai Wallet mobilapplikation, utan Dojo.


## Varför utföra coinjoins på Bitcoin?

Ett av de första problemen med alla peer-to-peer-betalningssystem är dubbla utgifter: hur kan man förhindra att illvilliga individer spenderar samma monetära enheter flera gånger utan att en central myndighet måste agera som skiljedomare?


Satoshi Nakamoto erbjöd en lösning på detta dilemma genom Bitcoin-protokollet, ett elektroniskt betalningssystem mellan två parter som fungerar oberoende av någon central myndighet. I sin vitbok framhåller han att det enda sättet att certifiera att det inte förekommer dubbla utgifter är att säkerställa att alla transaktioner inom betalningssystemet är synliga.


För att garantera att alla deltagare känner till transaktionerna måste de offentliggöras. Därför är Bitcoin:s verksamhet beroende av en transparent och distribuerad infrastruktur som gör det möjligt för alla nodoperatörer att verifiera hela kedjan av elektroniska signaturer och varje mynts historia, från det att det skapades av en Miner.


Den transparenta och distribuerade karaktären hos Bitcoin:s Blockchain innebär att alla nätverksanvändare kan följa och analysera alla andra deltagares transaktioner. Som ett resultat av detta är anonymitet på transaktionsnivå omöjlig. Anonymiteten bevaras dock på nivån för individuell identifiering. Till skillnad från det traditionella banksystemet där varje konto är kopplat till en personlig identitet, är medel i Bitcoin kopplade till par av kryptografiska nycklar, vilket ger användarna en form av pseudonymitet bakom kryptografiska identifierare.


Bitcoin:s konfidentialitet äventyras således när externa observatörer lyckas associera specifika UTXO:er med identifierade användare. När denna koppling väl är etablerad blir det möjligt att spåra deras transaktioner och analysera historiken för deras bitcoins. CoinJoin är just en teknik som utvecklats för att bryta spårbarheten hos UTXO:er och därigenom erbjuda en viss Layer av konfidentialitet till Bitcoin-användare på transaktionsnivå.


## Hur fungerar Whirlpool?

Whirlpool skiljer sig från andra CoinJoin-metoder genom att använda "_ZeroLink_"-transaktioner, som säkerställer att det inte finns någon teknisk koppling mellan alla inmatningar och alla utmatningar. Denna perfekta blandning uppnås genom en struktur där varje deltagare bidrar med ett identiskt belopp i input (med undantag för Mining-avgifter), vilket genererar outputs av perfekt lika stora belopp.

Detta restriktiva förhållningssätt till inputs ger Whirlpool CoinJoin-transaktioner en unik egenskap: den totala avsaknaden av deterministiska kopplingar mellan inputs och outputs. Med andra ord har varje output lika stor sannolikhet att tillskrivas någon deltagare, jämfört med alla andra outputs i transaktionen.

Inledningsvis var antalet deltagare i varje Whirlpool CoinJoin begränsat till 5, med 2 nya deltagare och 3 remixare (vi kommer att förklara dessa begrepp längre fram). Ökningen av transaktionsavgifterna i On-Chain som observerades 2023 fick dock Samourai-teamen att ompröva sin modell för att förbättra integriteten och samtidigt minska kostnaderna. Med hänsyn till marknadssituationen för avgifter och antalet deltagare kan samordnaren nu organisera coinjoins med 6, 7 eller 8 deltagare. Dessa förbättrade sessioner kallas "_Surge Cycles_". Det är viktigt att notera att det, oavsett konfiguration, alltid bara finns 2 nya deltagare i Whirlpool coinjoins.


Whirlpool-transaktioner kännetecknas således av ett identiskt antal in- och utgångar, som kan vara:


- 5 ingångar och 5 utgångar;

![coinjoin](assets/notext/2.webp)


- 6 ingångar och 6 utgångar;

![coinjoin](assets/notext/3.webp)


- 7 ingångar och 7 utgångar;

![coinjoin](assets/notext/4.webp)


- 8 ingångar och 8 utgångar.

![coinjoin](assets/notext/5.webp)

Den modell som föreslås av Whirlpool baseras således på små CoinJoin-transaktioner. Till skillnad från Wasabi och JoinMarket, där anonsets robusthet är beroende av volymen deltagare i en enda cykel, satsar Whirlpool på kedjan av flera små cykler.


I den här modellen betalar användaren avgifterna endast vid sitt första inträde i en pool, vilket gör att de kan delta i en mängd olika remixer utan ytterligare avgifter. Det är de nya deltagarna som täcker Mining-avgifterna för remixarna.


Med varje ytterligare CoinJoin som ett mynt deltar i, tillsammans med sina tidigare motsvarigheter, kommer anonsets att växa exponentiellt. Målet är därför att dra nytta av dessa gratis remixer som, med varje förekomst, bidrar till att stärka densiteten hos de anonsets som är associerade med varje blandat mynt.


Whirlpool har utformats med hänsyn till två viktiga krav:


- Tillgängligheten för implementering på mobila enheter, med tanke på att Samourai Wallet främst är en smartphone-applikation;
- Hastigheten på omblandningscyklerna för att främja en betydande ökning av anonsets.

Dessa krav vägledde utvecklarna av Samourai Wallet i utformningen av Whirlpool och fick dem att begränsa antalet deltagare per cykel. För få deltagare skulle ha äventyrat CoinJoin:s effektivitet och drastiskt minskat antalet anonset som genereras varje cykel, medan för många deltagare skulle ha medfört problem med hanteringen av mobilapplikationer och skulle ha hindrat cykelflödet.

**I slutändan finns det inget behov av att ha ett högt antal deltagare per CoinJoin på Whirlpool eftersom anonsets uppnås genom ackumulering av flera CoinJoin-cykler.**


[-> Läs mer om Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Poolerna och CoinJoin-avgifter

För att dessa multipla cykler effektivt ska öka de blandade myntens anonset måste ett visst ramverk upprättas för att begränsa de mängder UTXO som används. Whirlpool definierar således olika pooler.


En pool representerar en grupp användare som vill mixa tillsammans och som kommer överens om mängden UTXO som ska användas för att optimera CoinJoin-processen. Varje pool anger ett fast belopp för UTXO, som användaren måste följa för att kunna delta. För att utföra coinjoins med Whirlpool måste du alltså välja en pool. De pooler som för närvarande är tillgängliga är följande:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Genom att gå med i en pool med dina bitcoins kommer de att delas upp till generate UTXO som är helt homogena med de andra deltagarna i poolen. Varje pool har en maxgräns; för belopp som överstiger denna gräns kommer du därför att tvingas antingen att göra två separata poster inom samma pool eller att orientera dig mot en annan pool med ett högre belopp:


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


Innan man går vidare till coinjoins har användaren således ett val mellan två strategier:


- Välj en mindre pool för att minimera serviceavgifterna, i vetskap om att de kommer att få flera små UTXO:er i gengäld;
- Eller föredrar en större pool och går med på att betala högre avgifter för att i slutändan få ett minskat antal UTXO:er med högre värde.


Det avråds i allmänhet från att slå samman flera blandade UTXO efter CoinJoin-cyklerna, eftersom detta kan äventyra den förvärvade sekretessen, särskilt på grund av CIOH (Common-Input-Ownership Heuristic). Därför kan det vara klokt att välja en större pool, även om det innebär att betala mer, för att undvika att få för många UTXO:er med litet värde som resultat. Användaren måste väga dessa kompromisser mot varandra för att välja den pool som han eller hon föredrar.


Förutom serviceavgifterna måste man också ta hänsyn till Mining-avgifterna som ingår i alla Bitcoin-transaktioner. Som Whirlpool-användare kommer du att behöva betala Mining-avgifterna för förberedelsetransaktionen (`Tx0`) samt för den första CoinJoin. Alla efterföljande remixer kommer att vara gratis, tack vare Whirlpool:s modell som bygger på betalning av nya deltagare.


I varje Whirlpool CoinJoin är två användare bland inmatningarna faktiskt nya aktörer. De övriga inmatningarna kommer från remixare. Följaktligen täcks Mining-avgifterna för alla deltagare i transaktionen av dessa två nya deltagare, som sedan också kommer att dra nytta av gratis remixer:

![coinjoin](assets/en/6.webp)

Tack vare detta avgiftssystem skiljer sig Whirlpool verkligen från andra CoinJoin-tjänster eftersom UTXO:ernas anonymitet inte står i proportion till det pris som användaren betalar. Det är således möjligt att uppnå avsevärt höga nivåer av anonymitet genom att endast betala poolens inträdesavgift och Mining:s avgifter för två transaktioner (`Tx0` och den initiala mixen).

Det är viktigt att notera att användaren också måste täcka Mining-avgifterna för att ta ut sina UTXO:er från poolen efter att ha slutfört sina multipla coinjoins, såvida de inte har valt alternativet "mixa till", vilket vi kommer att diskutera i handledningen nedan.


### HD Wallet konton som används av Whirlpool

För att utföra en CoinJoin via Whirlpool måste Wallet generate flera distinkta konton. Ett konto, i samband med en HD (*Hierarkical Deterministic*) Wallet, utgör en sektion som är helt isolerad från de andra, denna separation sker på den tredje djupnivån i Wallet:s hierarki, det vill säga på nivån för "xpub".


En HD Wallet kan teoretiskt härleda upp till `2^(32/2)` olika konton. Det första kontot, som används som standard på alla Bitcoin-plånböcker, motsvarar indexet `0`.


För plånböcker som är anpassade till Whirlpool, t.ex. Samourai eller Sparrow, används 4 konton för att tillgodose behoven i CoinJoin-processen:


- Kontot **deposit**, identifierat med indexet `0`;
- Kontot **bad bank** (eller doxxic change), identifierat genom indexet `2 147 483 644'`;
- Kontot **premix**, identifierat genom indexet "2 147 483 645";
- Kontot **postmix**, identifierat genom indexet "2 147 483 646".


Vart och ett av dessa konton fyller en specifik funktion inom CoinJoin-processen.


Alla dessa konton är länkade till en enda seed, vilket gör det möjligt för användaren att återställa åtkomst till alla sina bitcoins med hjälp av sin återställningsfras och, om tillämpligt, deras passphrase. Det är dock nödvändigt att under denna återställningsoperation ange de olika kontoindex som användes för programvaran.


Låt oss nu titta på de olika stadierna av en Whirlpool CoinJoin inom dessa konton.


### De olika stadierna av coinjoins på Whirlpool

**Steg 1: Tx0**

Startpunkten för alla Whirlpool CoinJoin är **deposit**-kontot. Det här kontot är det som du automatiskt använder när du skapar en ny Bitcoin Wallet. Detta konto måste krediteras med de bitcoins som man vill blanda.

`Tx0` representerar det första steget i Whirlpool-blandningsprocessen. Det syftar till att förbereda och utjämna UTXO för CoinJoin, genom att dela upp dem i enheter som motsvarar mängden av den valda poolen, för att säkerställa blandningens homogenitet. De utjämnade UTXO skickas sedan till **premix**-kontot. När det gäller skillnaden som inte kan komma in i poolen separeras den till ett specifikt konto: **bad bank** (eller "doxxic change").

Denna inledande transaktion `Tx0` tjänar också till att reglera de serviceavgifter som ska betalas till mixkoordinatorn. Till skillnad från följande steg är denna transaktion inte ett samarbete; användaren måste därför ta på sig alla Mining-avgifter:

![coinjoin](assets/en/7.webp)


I detta exempel på en `Tx0`-transaktion delas en inmatning på `372 000 Sats` från vårt **deposit**-konto upp i flera utmatningar UTXO, som fördelas enligt följande:


- Ett belopp på 5 000 Sats` avsett för samordnaren för serviceavgifter, motsvarande inträdet i poolen på 100 000 Sats`;
- Tre UTXO förberedda för mixning, omdirigerade till vårt **premix**-konto och registrerade hos koordinatorn. Dessa UTXO utjämnas till 108 000 Sats` vardera, för att täcka Mining-avgifterna för deras framtida initiala mixning;
- Det överskott som inte kan komma in i poolen, eftersom det är för litet, betraktas som en giftig förändring. Den skickas till sitt specifika konto. Här uppgår denna förändring till "40 000 Sats";
- Slutligen finns det "3 000 Sats" som inte utgör en produktion, utan är de Mining-avgifter som krävs för att bekräfta "Tx0".


Här är till exempel en riktig Whirlpool Tx0 (inte från mig): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Steg 2: Den doxiska förändringen**

Det överskott som inte kunde integreras i poolen, här motsvarande "40 000 Sats", omdirigeras till kontot **bad bank**, även kallat "doxxic change", för att säkerställa en strikt separation från de andra UTXO i Wallet.


Denna UTXO är farlig för användarens integritet, eftersom den inte bara fortfarande är kopplad till sitt förflutna, och därmed möjligen till sin ägares identitet, utan dessutom noteras som tillhörande en användare som har utfört en CoinJoin.

Om denna UTXO slås samman med blandade utdata kommer de att förlora all den sekretess som uppnåtts under CoinJoin-cyklerna, särskilt på grund av Common-Input-Ownership-Heuristic (CIOH). Om det slås samman med andra doxiska förändringar riskerar användaren att förlora sekretessen eftersom detta kommer att länka samman de olika ingångarna i CoinJoin-cyklerna. Därför måste den hanteras med försiktighet. Sättet att hantera denna giftiga UTXO kommer att beskrivas i den sista delen av denna artikel, och framtida handledningar kommer att täcka dessa metoder mer djupgående på PlanB Network.


**Steg 3: Den inledande mixen**

När `Tx0` har slutförts skickas de utjämnade UTXO:erna till **premix**-kontot i vår Wallet, redo att introduceras i sin första CoinJoin-cykel, även kallad "initial mix". Om, som i vårt exempel, `Tx0` genererar flera UTXO:er för blandning, kommer var och en av dem att integreras i en separat initial CoinJoin.


I slutet av dessa första mixar kommer **premix**-kontot att vara tomt, medan våra mynt, som har betalat Mining-avgifterna för denna första CoinJoin, kommer att justeras exakt till det belopp som definieras av den valda poolen. I vårt exempel kommer våra ursprungliga UTXO:er på 108 000 Sats att ha reducerats till exakt 100 000 Sats.

![coinjoin](assets/en/8.webp)

**Steg 4: Remixerna**

Efter den första mixningen överförs UTXO:erna till kontot **postmix**. Detta konto samlar de redan blandade UTXO:erna och de som väntar på omblandning. När Whirlpool-klienten är aktiv är UTXO:erna i **postmix**-kontot automatiskt tillgängliga för omblandning och kommer att slumpmässigt väljas ut för att delta i dessa nya cykler.


Som en påminnelse är remixerna sedan 100% gratis: inga ytterligare serviceavgifter eller Mining-avgifter krävs. Att behålla UTXO:erna på **postmix**-kontot bibehåller således deras värde intakt och förbättrar samtidigt deras anonsets. Det är därför det är viktigt att låta dessa mynt delta i flera CoinJoin-cykler. Det kostar dig absolut ingenting, och det ökar deras anonymitetsnivåer.


När du bestämmer dig för att spendera blandade UTXO:er kan du göra det direkt från detta **postmix**-konto. Det är tillrådligt att behålla de blandade UTXO:erna på detta konto för att dra nytta av gratis remixer och för att undvika att de lämnar Whirlpool-kretsen, vilket kan minska deras konfidentialitet.


Som vi kommer att se i följande handledning finns det också alternativet "mixa till" som ger möjlighet att automatiskt skicka dina mixade mynt till en annan Wallet, till exempel en Cold Wallet, efter ett definierat antal coinjoins.

Efter att ha gått igenom teorin, låt oss dyka in i praktiken med en handledning om hur man använder Whirlpool genom Samourai Wallet Android-appen!


## Självstudier: CoinJoin Whirlpool på Samourai Wallet

Det finns många alternativ för att använda Whirlpool. Det jag vill presentera här är Samourai Wallet-alternativet (utan Dojo), en Bitcoin Wallet-hanteringsapplikation med öppen källkod på Android.


Att mixa på Samourai utan Dojo har fördelen att det är ganska enkelt att hantera, går snabbt att installera och kräver ingen annan enhet än en Android-telefon och en internetanslutning.


Denna metod har dock två betydande nackdelar:


- Coinjoins kommer endast att ske när Samourai körs i bakgrunden och är ansluten. Detta innebär att om du vill mixa och remixa dina bitcoins 24/7 måste du ständigt hålla Samourai påslagen;
- Om du använder Whirlpool med Samourai Wallet utan att se till att ansluta din egen Dojo, måste din applikation ansluta till servern som underhålls av Samourai-teamen, och du kommer att avslöja `xpub` för din Wallet för dem. Dessa anonyma informationsbitar är nödvändiga för att din applikation ska hitta dina transaktioner.


Den idealiska lösningen för att övervinna dessa begränsningar är att driva din egen Dojo associerad med en Whirlpool CLI-instans på din personliga Bitcoin-nod. På så sätt undviker du informationsläckage och uppnår fullständigt oberoende. Även om den handledning som presenteras nedan är användbar för vissa mål eller för nybörjare, rekommenderas att du använder din egen Dojo för att verkligen optimera din CoinJoin-session. En detaljerad guide om hur du ställer in den här konfigurationen kommer snart att finnas tillgänglig på PlanB Network.


### Installation av Samourai Wallet

För att börja behöver du självklart Samourai Wallet-appen. Du kan ladda ner den direkt från den officiella webbplatsen med hjälp av APK, från deras GitLab eller från Google Play Store.


### Skapa en Software Wallet

När du har installerat programvaran måste du fortsätta med att skapa en Bitcoin Wallet på Samourai. Om du redan har en kan du hoppa direkt till nästa steg.


När du öppnar programmet trycker du på den blå `Start`-knappen. Du kommer sedan att bli ombedd att välja en plats i telefonens filer där den krypterade säkerhetskopian av din nya Wallet kommer att lagras.


![samourai](assets/notext/9.webp)

Aktivera Tor genom att klicka på motsvarande skåra. I det här skedet har du också möjlighet att välja en specifik Dojo. Men i den här handledningen kommer vi att fortsätta med standard Dojo; så du kan lämna alternativet inaktiverat. När Tor är anslutet trycker du på knappen "Skapa en ny Wallet".

![samourai](assets/notext/10.webp)


Samourai Wallet uppmanar dig sedan att ställa in ett BIP39 passphrase. Det här extra lösenordet är mycket viktigt eftersom det direkt används för att härleda dina privata nycklar. En potentiell förlust av denna passphrase skulle leda till att du inte kan komma åt dina bitcoins, vilket gör dem oåterkalleligt förlorade. För att återställa din Samourai Wallet är det absolut nödvändigt att ha både din 12-ords återställningsfras och passphrase.


Det är därför viktigt att välja en robust passphrase och att göra en eller flera fysiska kopior, på papper eller på ett metalliskt medium, för att garantera säkerheten för dina bitcoins. När du har slutfört dessa uppgifter markerar du rutan "Jag är medveten om att i händelse av förlust..." och trycker sedan på knappen "NÄSTA".


![samourai](assets/notext/11.webp)


Du måste sedan ange en PIN-kod som består av 5 till 8 siffror. Denna kod kommer att säkra åtkomsten till din Wallet på din telefon. Den kommer att begäras varje gång du vill öppna Samourai-applikationen. Välj en robust PIN-kod och se till att ha en säkerhetskopia. Därefter kan du trycka på knappen `NEXT`.


![samourai](assets/notext/12.webp)


Samourai kommer att be dig att ange din PIN-kod igen för bekräftelse. Ange den och tryck sedan på `FINALIZE`.


![samourai](assets/notext/13.webp)


Du kommer då åt din återställningsfras som består av 12 ord. Med denna fras kan du återställa din Wallet med den tidigare inmatade passphrase. Vi rekommenderar starkt att du gör en eller flera kopior av den här frasen på fysiska medier, t.ex. papper eller ett metalliskt material, för att garantera säkerheten för dina bitcoins i händelse av problem.


När du har gjort dessa säkerhetskopior kommer du att hänvisas till Interface i din nya Samourai Wallet.


![samourai](assets/notext/14.webp)


Du erbjuds att hämta din PayNym Bot. Du kan begära det om du vill, även om det inte är nödvändigt för vår handledning.


![samourai](assets/notext/15.webp)

Innan du fortsätter att ta emot bitcoins på den här nya Wallet rekommenderas det starkt att du kontrollerar giltigheten av dina Wallet-säkerhetskopior (passphrase och återställningsfrasen). För att verifiera passphrase kan du välja ikonen för din PayNym Bot som finns längst upp till vänster på skärmen och sedan följa vägen:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


Ange din passphrase för att utföra verifieringen.


![samourai](assets/notext/16.webp)


Samourai kommer att bekräfta om det är giltigt.


![samourai](assets/notext/17.webp)


För att verifiera din säkerhetskopia av återställningsfrasen, gå till ikonen för din PayNym Bot, som finns längst upp till vänster på skärmen, och följ den här vägen:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai kommer att visa ett fönster med din återställningsfras. Se till att den matchar exakt med din fysiska säkerhetskopia.


För att gå längre och utföra ett fullständigt återställningstest, notera ett vittneselement i din Wallet, till exempel en av "xpubarna", och fortsätt sedan att radera din Wallet (förutsatt att den fortfarande är tom). Målet är att försöka återställa denna tomma Wallet med hjälp av endast dina fysiska säkerhetskopior. Om återställningen lyckas tyder det på att dina säkerhetskopior är giltiga och tillförlitliga.


### Mottagande av bitcoins

När du har skapat din Wallet kommer du att börja med ett enda konto, identifierat med indexet `0`. Detta är **deposit**-kontot som vi pratade om i de tidigare delarna. Det är till detta konto som du måste överföra bitcoins avsedda för coinjoins.


Detta gör du genom att klicka på den blå symbolen `+` längst ned till höger på skärmen.


![samourai](assets/notext/18.webp)


Klicka sedan på knappen Green `Receive`.


![samourai](assets/notext/19.webp)


Samourai kommer automatiskt generate ett nytt tomt Address för att ta emot bitcoins.


![samourai](assets/notext/20.webp)


Du kan skicka bitcoins för att blandas där.


![samourai](assets/notext/21.webp)


### Tillverkning av Tx0

När transaktionen är bekräftad kan vi starta coinjoins-processen. För att göra detta, klicka på den blå `+` knappen längst ner till höger på skärmen.


![samourai](assets/notext/22.webp)


Klicka sedan på `Whirlpool` i blått.


![samourai](assets/notext/23.webp)


Vänta medan Whirlpool initieras och Samourai skapar de konton som behövs.


![samourai](assets/notext/24.webp)


Du kommer då att komma till Whirlpool:s hemsida. Klicka på `Start`.

![samourai](assets/notext/25.webp)

Välj UTXO från **deposit**-kontot som du vill skicka i CoinJoin-cykler och klicka sedan på `Nästa`.


![samourai](assets/notext/26.webp)


I nästa steg måste du välja den avgiftsnivå som ska tilldelas `Tx0` samt till din första mix. Denna inställning kommer att avgöra hastigheten med vilken din `Tx0` och din första CoinJoin (eller första coinjoins) kommer att bekräftas. Tänk på att Mining-avgifterna för `Tx0` och den första mixen är ditt ansvar, men du behöver inte betala Mining-avgifter för de efterföljande remixerna. Du har valet mellan alternativen `Low`, `Normal` eller `High`.


![samourai](assets/notext/27.webp)


I samma fönster har du möjlighet att välja vilken pool du ska gå in i. Med tanke på att jag ursprungligen valde en UTXO på 454 258 Sats, är mitt enda möjliga val poolen på 100 000 Sats. På denna sida presenteras också poolens serviceavgifter, utöver Mining-avgifterna, vilket gör att du kan veta den totala kostnaden för denna CoinJoin-cykel. Om allt passar dig, välj lämplig pool och fortsätt genom att klicka på den blå knappen `VERIFY CYCLE DETAILS`.


![samourai](assets/notext/28.webp)


Du kan sedan se alla detaljer för din CoinJoin-cykel:


- antalet UTXO som kommer att ingå i poolen;
- de olika avgifter som uppkommit;
- mängden doxisk förändring...


Kontrollera informationen och klicka sedan på knappen Green `START CYCLE`.


![samourai](assets/notext/29.webp)


Ett fönster visas där du kan markera den toxiska förändringen som uppstår när du går in i CoinJoin-cykeln som "ej spenderbar". Genom att välja `YES` kommer denna UTXO inte att vara synlig i din Wallet och kan inte väljas för framtida transaktioner. Den kommer dock att förbli tillgänglig i listan över UTXO:er i din Wallet, där du manuellt kan ändra dess status. Vi rekommenderar att du väljer detta alternativ för att undvika eventuella hanteringsfel som kan äventyra din integritet senare. Om du väljer `NO` kommer den toxiska förändringen att förbli tillgänglig för användning i din Wallet. Om du vill lära dig mer om att hantera och använda denna toxiska förändring rekommenderar jag att du läser den sista delen av denna handledning.


![samourai](assets/notext/30.webp)


Samourai kommer sedan att sända din Tx0.


![samourai](assets/notext/31.webp)


### Tillverkning av sammanfogningar

När Tx0 har sänts ut kan du hitta den på fliken `Transaktioner` i Whirlpool-menyn.


![samourai](assets/notext/32.webp)

Dina UTXO:er som är klara att blandas finns i fliken "Blandning pågår...", som motsvarar kontot **Premix**.

![samourai](assets/notext/33.webp)


När "Tx0" har bekräftats kommer dina UTXO:er automatiskt att registreras hos koordinatorn och de första mixningarna kommer att starta successivt på ett automatiskt sätt.


![samourai](assets/notext/34.webp)


Genom att kontrollera fliken `Remixing`, som motsvarar **Postmix**-kontot, kommer du att observera UTXO: erna som härrör från de första mixarna. Dessa mynt kommer att förbli redo för efterföljande remixing, vilket inte medför några extra avgifter. Jag rekommenderar att du läser den här andra artikeln för att lära dig mer om remixprocessen och effektiviteten i en CoinJoin-cykel: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-Whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


Det är möjligt att tillfälligt avbryta remixningen av en UTXO genom att trycka på pausknappen till höger om den. För att göra den tillgänglig för remixning igen klickar du helt enkelt på samma knapp en gång till. Det är viktigt att notera att endast en CoinJoin kan utföras per användare och per pool samtidigt. Om du har 6 UTXO:er med `100 000 Sats` redo för CoinJoin kan alltså bara en av dem blandas. Efter att ha blandat en UTXO fortsätter Samourai Wallet att slumpmässigt välja en ny UTXO från din tillgänglighet, för att diversifiera och balansera remixningen av varje mynt.


![samourai](assets/notext/36.webp)


För att säkerställa kontinuerlig tillgänglighet av dina UTXO:er för remixning är det nödvändigt att hålla Samourai-applikationen aktiv i bakgrunden. Du bör se ett meddelande på din telefon som bekräftar att Whirlpool körs. Om du stänger applikationen eller stänger av telefonen kommer coinjoins att pausas.


### Färdigställande av coinjoins

För att spendera dina blandade bitcoins, gå till **Postmix**-kontot noterat `Remixing` i Whirlpool-menyflikarna.


![samourai](assets/notext/37.webp)


Klicka på den blå Whirlpool-logotypen längst ned till höger.


![samourai](assets/notext/38.webp)


Klicka sedan på `Spend Mixed UTXOs`.


![samourai](assets/notext/39.webp)


Du kan sedan ange mottagarens Address och det belopp som ska skickas, på samma sätt som för alla andra transaktioner som görs med Samourai Wallet. Den blå bakgrunden indikerar att pengarna används från ett Whirlpool-konto och inte från **deposit**-kontot.


![samourai](assets/notext/40.webp)


Genom att klicka på de 3 små prickarna längst upp till höger kan du välja specifika UTXO:er.

![samourai](assets/notext/41.webp)

Genom att klicka på den vita fyrkanten längst upp till höger i fönstret kan du skanna QR-koden för den mottagande Address med din kamera.


![samourai](assets/notext/42.webp)


Ange nödvändig information för din utgiftstransaktion och klicka sedan på den blå knappen "VERIFY TRANSACTION".


![samourai](assets/notext/43.webp)


I nästa steg har du möjlighet att ändra den avgiftssats som är kopplad till din transaktion. Du kan också aktivera Stonewall-alternativet genom att markera motsvarande ruta. Om Stonewall-alternativet inte kan väljas betyder det att ditt **Postmix**-konto inte innehåller en UTXO av tillräcklig storlek för att stödja denna särskilda transaktionsstruktur.


[-> Läs mer om Stonewall-transaktioner] (https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Om allt är till din belåtenhet klickar du på Green `SEND ... BTC`-knappen.


![samourai](assets/notext/44.webp)


Samourai kommer sedan att fortsätta att signera din transaktion innan den sänds ut i nätverket. Du behöver bara vänta tills den läggs till i ett block av en Miner.


![samourai](assets/notext/45.webp)


### Använda en SCODE

Ibland erbjuder Samourai Wallet-lagen "SCODEs". En SCODE är en kampanjkod som ger rabatt på poolens serviceavgifter. Samourai Wallet erbjuder ibland sådana koder till sina användare under speciella evenemang. Jag råder dig [att följa Samourai Wallet](https://twitter.com/SamouraiWallet) på sociala medier för att inte gå miste om framtida SCODES.


För att tillämpa en SCODE på Samourai, innan du startar en ny CoinJoin-cykel, gå till Whirlpool-menyn och välj de tre små prickarna längst upp till höger på skärmen.


![samourai](assets/notext/46.webp)


Klicka på `SCODE (kampanjkod) Whirlpool`.


![samourai](assets/notext/47.webp)


Ange SCODE i fönstret som öppnas och bekräfta sedan genom att klicka på "OK".


![samourai](assets/notext/48.webp)


Whirlpool kommer automatiskt att stängas. Vänta tills Samourai har laddats färdigt och öppna sedan Whirlpool-menyn igen.


![samourai](assets/notext/49.webp)


Kontrollera att din SCODE har registrerats korrekt genom att klicka en gång till på de tre små prickarna och sedan välja `SCODE (kampanjkod) Whirlpool`. Om allt är i sin ordning är du redo att starta en ny Whirlpool-cykel med rabatt på serviceavgifterna. Det är viktigt att notera att dessa SCODEs är tillfälliga: de förblir giltiga i några dagar innan de blir föråldrade.


## Hur vet man kvaliteten på våra CoinJoin-cykler?

För att en CoinJoin verkligen ska vara effektiv är det viktigt att den visar på en god överensstämmelse mellan beloppen för in- och utbetalningar. Denna enhetlighet ökar antalet möjliga tolkningar i en extern observatörs ögon och ökar därmed osäkerheten kring transaktionen. För att kvantifiera denna osäkerhet som genereras av en CoinJoin kan man använda sig av att beräkna transaktionens entropi.


För en djupgående undersökning av dessa indikatorer (Whirlpool-modellen är erkänd som den som ger mest homogenitet till coinjoins) hänvisar jag dig till handledningen: [BOLTZMANN KALKYLATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Därefter utvärderas prestandan hos flera CoinJoin-cykler baserat på omfattningen av de grupper i vilka ett mynt är dolt. Storleken på dessa grupper definierar vad som kallas anonsets. Det finns två typer av anonsets: den första bedömer den integritet som erhållits mot en retrospektiv analys (från nutid till dåtid) och den andra mot en prospektiv analys (från dåtid till nutid). För en detaljerad förklaring av dessa två indikatorer uppmanar jag dig att läsa handledningen: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Hur hanterar man postmix?

Efter att ha utfört CoinJoin-cykler är den bästa strategin att behålla dina UTXO:er på **postmix**-kontot i väntan på framtida användning. Det är till och med tillrådligt att låta dem remixas på obestämd tid tills du behöver spendera dem.


Vissa användare kan överväga att överföra sina blandade bitcoins till en Wallet som säkras av en Hardware Wallet. Detta är möjligt, men det är viktigt att följa rekommendationerna från Samourai Wallet noggrant för att inte äventyra den förvärvade sekretessen.


Sammanslagning av UTXO:er är det vanligaste misstaget. Det är nödvändigt att undvika att kombinera blandade UTXO:er med oblandade UTXO:er i samma transaktion, för att undvika CIOH (*Common-Input-Ownership-Heuristic*). Detta kräver noggrann hantering av dina UTXO:er inom din Wallet, särskilt när det gäller märkning. Utöver CoinJoin är sammanslagning av UTXO:er i allmänhet en dålig praxis som ofta leder till förlust av sekretess om den inte hanteras korrekt.

Du bör också vara vaksam på konsolideringen av blandade UTXO:er med varandra. Måttliga konsolideringar är möjliga om dina blandade UTXO:er har betydande anonsets, men detta kommer oundvikligen att minska dina mynts integritet. Se till att konsolideringarna varken är för stora eller utförs efter ett otillräckligt antal remixer, eftersom detta riskerar att upprätta härledbara länkar mellan dina UTXO:er före och efter CoinJoin-cyklerna. Om du är osäker på dessa operationer är den bästa metoden att inte konsolidera UTXO:er efter blandning, utan att överföra dem en efter en till din Hardware Wallet och generera en ny tom Address varje gång. Kom återigen ihåg att märka varje mottagen UTXO på rätt sätt.


Det rekommenderas också att du inte överför dina UTXO:er efter blandning till en Wallet med ovanliga skript. Om du till exempel går in i Whirlpool från en Multisig Wallet med hjälp av `P2WSH`-skript, är det liten chans att du blandas med andra användare som har samma typ av Wallet ursprungligen. Om du avslutar din postmix till samma Multisig Wallet kommer sekretessnivån för dina blandade bitcoins att minska kraftigt. Utöver skript finns det många andra Wallet-fingeravtryck som kan lura dig.


Som med alla Bitcoin-transaktioner är det också lämpligt att inte återanvända mottagningsadresser. Varje ny transaktion måste tas emot på en ny blank Address.


Den enklaste och säkraste lösningen är att låta dina blandade UTXO:er vila på deras **postmix**-konto, låta dem remixa och bara röra dem för att spendera. Samourai- och Sparrow-plånböckerna har ytterligare skydd mot alla dessa risker relaterade till kedjeanalys. Dessa skydd hjälper dig att undvika att göra misstag.


## Hur hanterar man en doxisk förändring?

Därefter måste du vara försiktig med att hantera doxisk förändring, den förändring som inte kunde komma in i CoinJoin-poolen. Dessa toxiska UTXO:er, som uppstår till följd av användningen av Whirlpool, utgör en risk för din integritet eftersom de etablerar en koppling mellan dig och användningen av CoinJoin. Det är därför absolut nödvändigt att hantera dem med försiktighet och inte kombinera dem med andra UTXO:er, särskilt inte blandade UTXO:er. Här följer olika strategier som du kan överväga för deras användning:


- Blanda dem i mindre pooler:** Om din giftiga UTXO är tillräckligt stor för att komma in i en mindre pool på egen hand, överväg att blanda den. Detta är ofta det bästa alternativet. Det är dock viktigt att inte slå samman flera giftiga UTXO för att komma in i en pool, eftersom detta kan länka dina olika poster.
- Markera dem som "icke spenderbara":** Ett annat tillvägagångssätt är att sluta använda dem, markera dem som "icke spenderbara" på deras dedikerade konto och bara HODL. Detta säkerställer att du inte av misstag spenderar dem. Om värdet på Bitcoin ökar kan nya pooler som är mer lämpade för dina giftiga UTXO: er dyka upp;
- Gör donationer:** Överväg att göra donationer, även blygsamma, till utvecklare som arbetar med Bitcoin och dess tillhörande programvara. Du kan också donera till organisationer som accepterar BTC. Om det verkar för komplicerat att hantera dina giftiga UTXO: er kan du helt enkelt bli av med dem genom att göra en donation;
- Köp presentkort:** Plattformar som [Bitrefill] (https://www.bitrefill.com/) låter dig Exchange bitcoins för presentkort som kan användas hos olika handlare. Detta kan vara ett sätt att bli av med dina giftiga UTXO:er utan att förlora det tillhörande värdet;
- Konsolidera dem på Monero:** Samourai Wallet erbjuder nu en atombytestjänst mellan BTC och XMR. Detta är perfekt för att hantera giftiga UTXO genom att konsolidera dem på Monero, utan att äventyra din integritet via KYC, innan du skickar tillbaka dem till Bitcoin. Detta alternativ kan dock vara kostsamt när det gäller Mining-avgifter och premien på grund av likviditetsbegränsningar;
- Skicka dem till Lightning Network:** Att överföra dessa UTXO:er till Lightning Network för att dra nytta av reducerade transaktionsavgifter är ett alternativ som kan vara intressant. Denna metod kan dock avslöja viss information beroende på din användning av Lightning och bör därför användas med försiktighet.


Detaljerade handledningar om hur man implementerar dessa olika tekniker kommer snart att erbjudas på PlanB Network.


**Ytterligare resurser:**

[Samourai Wallet video tutorial](https://planb.network/tutorials/Wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Dokumentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter-tråd om coinjoins] (https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogginlägg om coinjoins] (https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).