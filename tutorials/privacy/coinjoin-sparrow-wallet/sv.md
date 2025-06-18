---
name: CoinJoin - Sparv Wallet
description: Hur utför man en CoinJoin på Sparrow Wallet?
---
![cover](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Whirlpool-verktyget inte längre, inte ens för personer som har sin egen Dojo eller använder Sparrow Wallet. Det är dock fortfarande möjligt att detta verktyg kan återinföras under de kommande veckorna eller återlanseras på ett annat sätt. Dessutom är den teoretiska delen av denna artikel fortfarande relevant för att förstå principerna och målen för coinjoins i allmänhet (inte bara Whirlpool), samt för att förstå effektiviteten i Whirlpool-modellen.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

I denna handledning får du lära dig vad en CoinJoin är och hur du utför en CoinJoin med hjälp av Sparrow Wallet-programvaran och Whirlpool-implementeringen.


## Vad är en CoinJoin på Bitcoin?

**En CoinJoin är en teknik som bryter spårbarheten för bitcoins på Blockchain**. Den förlitar sig på en samarbetstransaktion med en specifik struktur med samma namn: CoinJoin-transaktionen.


Coinjoins förbättrar Bitcoin-användarnas integritet genom att komplicera kedjeanalysen för externa observatörer. Deras struktur gör det möjligt att slå samman flera mynt från olika användare till en enda transaktion, vilket suddar ut spåren och gör det svårt att fastställa länkarna mellan in- och utdataadresser.


Principen för CoinJoin bygger på ett samarbetsbaserat tillvägagångssätt: flera användare som vill blanda sina bitcoins sätter in identiska belopp som input i samma transaktion. Dessa belopp omfördelas sedan som outputs av lika värde till varje användare. I slutet av transaktionen blir det omöjligt att associera en specifik utgång med en känd användare vid ingången. Det finns ingen direkt länk mellan inputs och outputs, vilket bryter kopplingen mellan användarna och deras UTXO, liksom varje mynts historia.

![coinjoin](assets/notext/1.webp)


Exempel på en CoinJoin-transaktion (inte från mig): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


För att genomföra en CoinJoin och samtidigt säkerställa att varje användare hela tiden har kontroll över sina medel börjar processen med att en koordinator skapar transaktionen, som sedan överförs till varje deltagare. Varje användare signerar sedan transaktionen efter att ha verifierat att den passar dem. Alla insamlade signaturer integreras slutligen i transaktionen. Om en användare eller koordinatorn försöker avleda medel genom att ändra CoinJoin-transaktionens utdata kommer signaturerna att visa sig vara ogiltiga, vilket leder till att noderna avvisar transaktionen.


Det finns flera implementeringar av CoinJoin, till exempel Whirlpool, JoinMarket eller Wabisabi, som alla syftar till att hantera samordning mellan deltagare och öka effektiviteten i CoinJoin-transaktioner.


I den här handledningen fokuserar vi på implementeringen **Whirlpool**, som jag anser vara den mest effektiva lösningen för att utföra coinjoins på Bitcoin. Även om den finns tillgänglig på flera plånböcker, utforskar denna handledning uteslutande dess användning med Sparrow Wallet Desktop-programvaran.

## Varför utföra CoinJoins på Bitcoin?


Ett av de första problemen med alla peer-to-peer-betalningssystem är Double-spending: hur kan man förhindra att illvilliga individer spenderar samma monetära enheter flera gånger utan att vända sig till en central myndighet för skiljedom?


Satoshi Nakamoto gav en lösning på detta dilemma genom Bitcoin-protokollet, ett elektroniskt peer-to-peer-betalningssystem som fungerar oberoende av någon central myndighet. I sin vitbok understryker han att det enda sättet att certifiera frånvaron av Double-spending är att säkerställa att alla transaktioner inom betalningssystemet är synliga.


För att säkerställa att varje deltagare är medveten om transaktionerna måste de offentliggöras. Bitcoin:s verksamhet är således beroende av en transparent och distribuerad infrastruktur som gör det möjligt för alla nodoperatörer att verifiera hela kedjan av elektroniska signaturer och varje mynts historia, från det att det skapades av en Miner.


Den transparenta och distribuerade karaktären hos Bitcoin:s Blockchain innebär att alla nätverksanvändare kan följa och analysera alla andra deltagares transaktioner. Följaktligen är anonymitet på transaktionsnivå omöjlig. Anonymiteten bevaras dock på nivån för individuell identifiering. Till skillnad från det traditionella banksystemet där varje konto är kopplat till en personlig identitet, är medel i Bitcoin kopplade till par av kryptografiska nycklar, vilket ger användarna en form av pseudonymitet bakom kryptografiska identifierare.


Därför äventyras sekretessen för Bitcoin när externa observatörer lyckas associera specifika UTXO:er med identifierade användare. När denna koppling väl är etablerad blir det möjligt att spåra deras transaktioner och analysera historiken för deras bitcoins. CoinJoin är just en teknik som utvecklats för att bryta spårbarheten hos UTXO:er och därmed erbjuda en viss Layer av konfidentialitet till Bitcoin-användare på transaktionsnivå.


## Hur fungerar Whirlpool?


Whirlpool skiljer sig från andra CoinJoin-metoder genom att använda "_ZeroLink_"-transaktioner, som säkerställer att det inte finns någon teknisk koppling mellan alla inmatningar och alla utmatningar. Denna perfekta blandning uppnås genom en struktur där varje deltagare bidrar med ett identiskt belopp i input (med undantag för Mining-avgifter), vilket genererar outputs av perfekt lika stora belopp.


Detta restriktiva synsätt på insatsvaror ger Whirlpool CoinJoin-transaktioner en unik egenskap: den totala avsaknaden av deterministiska kopplingar mellan insatsvaror och utdata. Med andra ord är det lika stor sannolikhet att varje output tillskrivs någon deltagare jämfört med alla andra outputs i transaktionen.

Inledningsvis var antalet deltagare i varje Whirlpool CoinJoin begränsat till 5, med 2 nya deltagare och 3 remixare (vi kommer att förklara dessa begrepp längre fram). Ökningen av transaktionsavgifterna i On-Chain som observerades 2023 fick dock Samourai-teamen att ompröva sin modell för att förbättra integriteten och samtidigt minska kostnaderna. Med hänsyn till marknadssituationen för avgifter och antalet deltagare kan samordnaren nu organisera coinjoins med 6, 7 eller 8 deltagare. Dessa förbättrade sessioner kallas "_Surge Cycles_". Det är viktigt att notera att det, oavsett upplägg, alltid bara finns 2 nya deltagare i Whirlpool coinjoins.


Därför kännetecknas Whirlpool-transaktioner av ett identiskt antal in- och utgångar, som kan vara:


- 5 ingångar och 5 utgångar;

![coinjoin](assets/notext/2.webp)


- 6 ingångar och 6 utgångar;

![coinjoin](assets/notext/3.webp)


- 7 ingångar och 7 utgångar;

![coinjoin](assets/notext/4.webp)


- 8 ingångar och 8 utgångar.

![coinjoin](assets/notext/5.webp)

Den modell som föreslås av Whirlpool baseras således på små CoinJoin-transaktioner. Till skillnad från Wasabi och JoinMarket, där anonsets robusthet är beroende av volymen deltagare i en enda cykel, satsar Whirlpool på kedjan av flera små cykler.


I den här modellen betalar användaren endast avgifter vid sitt första inträde i en pool, vilket gör att de kan delta i en mängd olika remixer utan ytterligare avgifter. Det är de nya deltagarna som står för Mining-avgifterna för remixarna.


Med varje ytterligare CoinJoin som ett mynt deltar i, tillsammans med dess tidigare påträffade kamrater, kommer anonsets att växa exponentiellt. Målet är således att dra nytta av dessa gratis remixer som, med varje förekomst, bidrar till att stärka tätheten av de anonsets som är associerade med varje blandat mynt.


Whirlpool har utformats med hänsyn till två viktiga krav:


- Tillgängligheten för implementering på mobila enheter, med tanke på att Samourai Wallet främst är en smartphone-applikation;
- Hastigheten på omblandningscyklerna för att främja en betydande ökning av anonsets.


Dessa krav styrde de val som utvecklarna av Samourai Wallet gjorde vid utformningen av Whirlpool, och ledde dem till att begränsa antalet deltagare per cykel. För få deltagare skulle ha äventyrat CoinJoin:s effektivitet och drastiskt minskat de anonsets som genereras med varje cykel, medan för många deltagare skulle ha medfört hanteringsproblem i mobilapplikationer och skulle ha hindrat cykelflödet.


**I slutändan finns det inget behov av att ha ett högt antal deltagare per CoinJoin på Whirlpool eftersom anonsets görs under ackumuleringen av flera CoinJoin-cykler

[-> Läs mer om Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin pooler och avgifter

För att säkerställa att multipla cykler effektivt ökar anonsets för blandade mynt måste ett visst ramverk fastställas för att begränsa de mängder UTXO som används. Whirlpool definierar olika pooler för detta ändamål.


En pool representerar en grupp användare som vill mixa tillsammans och som kommer överens om mängden UTXO:er som ska användas för att optimera CoinJoin-processen. Varje pool specificerar ett fast belopp för UTXO, vilket användaren måste följa för att kunna delta. För att utföra coinjoins med Whirlpool måste du alltså välja en pool. De för närvarande tillgängliga poolerna är följande:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Genom att gå med i en pool med dina bitcoins kommer de att delas till generate UTXO som är helt homogena med de andra deltagarna i poolen. Varje pool har en maxgräns; för belopp som överskrider denna gräns kommer du därför att tvingas antingen göra två separata poster inom samma pool eller flytta till en annan pool med ett högre belopp:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Som tidigare nämnts anses en UTXO tillhöra en pool när den är redo att integreras i en CoinJoin. Detta innebär dock inte att användaren förlorar äganderätten till den. **Genom de olika blandningscyklerna behåller du full kontroll över dina nycklar och följaktligen dina bitcoins.** Det är detta som skiljer CoinJoin-tekniken från andra centraliserade blandningstekniker.


För att delta i en CoinJoin-pool måste serviceavgifter samt Mining-avgifter betalas. Serviceavgifterna är fasta för varje pool och är avsedda att kompensera de team som ansvarar för utveckling och underhåll av Whirlpool. För Sparrow Wallet-användare vidarebefordras dessa avgifter av Samourai-teamen till utvecklarna av Sparrow.


Serviceavgifterna för att använda Whirlpool ska betalas en gång när du går in i poolen. När detta steg är slutfört har du möjlighet att delta i ett obegränsat antal remixer utan ytterligare avgifter. Här är de aktuella fasta avgifterna för varje pool:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Dessa avgifter fungerar i huvudsak som en inträdesbiljett till den valda poolen, oavsett hur mycket du sätter in CoinJoin. Så oavsett om du går med i 0,01-poolen med exakt 0,01 BTC eller om du går in med 0,5 BTC, kommer avgifterna att förbli desamma i absolut värde.


Innan användaren går vidare med coinjoins kan han eller hon därför välja mellan två strategier:


- Välj en mindre pool för att minimera serviceavgifterna, i vetskap om att de kommer att få flera små UTXO:er i gengäld;
- Eller föredrar en större pool och går med på att betala högre avgifter för att i slutändan få ett minskat antal UTXO:er med högre värde.


Det avråds generellt från att slå samman flera blandade UTXO efter CoinJoin-cyklerna, eftersom detta kan äventyra den förvärvade sekretessen, särskilt på grund av Common-Input-Ownership Heuristic (CIOH). Därför kan det vara klokt att välja en större pool, även om det innebär att betala mer, för att undvika att få för många UTXO:er med litet värde som resultat. Användaren måste väga in dessa avvägningar för att välja den pool som han eller hon föredrar.


Förutom serviceavgifterna måste även Mining-avgifterna som är inneboende i alla Bitcoin-transaktioner beaktas. Som Whirlpool-användare kommer du att behöva betala Mining-avgifterna för förberedelsetransaktionen (`Tx0`) samt för den första CoinJoin. Alla efterföljande remixer kommer att vara gratis, tack vare Whirlpool:s modell som bygger på betalning av nya deltagare.


I varje Whirlpool CoinJoin är två användare bland inmatningarna faktiskt nya aktörer. De övriga inmatningarna kommer från remixare. Följaktligen täcks Mining-avgifterna för alla deltagare i transaktionen av dessa två nya deltagare, som sedan också kommer att dra nytta av gratis remixer:

![coinjoin](assets/en/6.webp)

Tack vare detta avgiftssystem skiljer sig Whirlpool verkligen från andra CoinJoin-tjänster eftersom UTXO:ernas anonymitet inte står i proportion till det pris som användaren betalar. Det är således möjligt att uppnå avsevärt höga anonymitetsnivåer genom att endast betala poolens inträdesavgifter och Mining:s avgifter för två transaktioner (`Tx0` och den initiala mixen).


Det är viktigt att notera att användaren också måste täcka Mining-avgifterna för att ta ut sina UTXO:er från poolen efter att ha slutfört sina multipla coinjoins, såvida de inte har valt alternativet "mixa till", vilket vi kommer att diskutera i handledningen nedan.


### HD Wallet konton som används av Whirlpool

För att utföra en CoinJoin via Whirlpool måste Wallet generate flera distinkta konton. Ett konto, i samband med en HD (Hierarchical Deterministic) Wallet, utgör en sektion som är helt isolerad från de andra, denna separation sker på den tredje djupnivån i Wallet:s hierarki, det vill säga på nivån för `xpub`.

En HD Wallet kan teoretiskt härleda upp till `2^(32/2)` olika konton. Det första kontot, som används som standard på alla Bitcoin-plånböcker, motsvarar indexet `0`.


För plånböcker som är anpassade till Whirlpool, t.ex. Samourai eller Sparrow, används 4 konton för att tillgodose behoven i CoinJoin-processen:


- Kontot **deposit**, identifierat med indexet `0`;
- Kontot **bad bank** (eller doxxic change), identifierat genom indexet `2 147 483 644'`;
- Kontot **premix**, identifierat genom indexet "2 147 483 645";
- Kontot **postmix**, identifierat genom indexet "2 147 483 646".


Vart och ett av dessa konton fyller en specifik funktion inom CoinJoin.


Alla dessa konton är länkade till en enda seed, vilket gör det möjligt för användaren att återställa åtkomst till alla sina bitcoins genom att använda sin återställningsfras och, om tillämpligt, sin passphrase. Det är dock nödvändigt att under denna återställningsoperation ange de olika kontoindex som användes för programvaran.


Låt oss nu titta på de olika stadierna av en Whirlpool CoinJoin inom dessa konton.


### De olika stadierna av coinjoins på Whirlpool

**Steg 1: Tx0**

Startpunkten för alla Whirlpool CoinJoin är **deposit**-kontot. Det här kontot är det som du automatiskt använder när du skapar en ny Bitcoin Wallet. Detta konto måste krediteras med de bitcoins som du vill mixa.


`Tx0` representerar det första steget i Whirlpool blandningsprocessen. Det syftar till att förbereda och utjämna UTXO:erna för CoinJoin genom att dela upp dem i enheter som motsvarar mängden av den valda poolen, för att säkerställa homogeniteten i blandningen. De utjämnade UTXO:erna skickas sedan till **premix**-kontot. När det gäller skillnaden som inte kan komma in i poolen separeras den till ett specifikt konto: **bad bank** (eller "doxxic change").


Denna inledande transaktion `Tx0` tjänar också till att reglera de serviceavgifter som ska betalas till mixkoordinatorn. Till skillnad från de följande stegen är denna transaktion inte kollaborativ; användaren måste därför ta på sig hela Mining-avgiften:

![coinjoin](assets/en/7.webp)

I detta exempel på en transaktion `Tx0` delas en inmatning på `372 000 Sats` från vårt **deposit**-konto upp i flera utgående UTXO, som fördelas enligt följande:


- Ett belopp på 5 000 Sats` avsett för samordnaren för serviceavgifter, motsvarande inträdet i poolen på 100 000 Sats`;
- Tre UTXO:er förberedda för mixning, omdirigerade till vårt **premix**-konto och registrerade hos koordinatorn. Dessa UTXO:er utjämnas till 108 000 Sats vardera för att täcka Mining-avgifterna för deras framtida initiala mixning;
- Överskottet, som inte kan komma in i poolen eftersom det är för litet, betraktas som giftig förändring. Den skickas till sitt specifika konto. Här uppgår denna förändring till 40 000 Sats;
- Slutligen finns det "3 000 Sats" som inte utgör en output, utan är de Mining-avgifter som krävs för att bekräfta "Tx0".


Här är till exempel en riktig Tx0 Whirlpool (som inte kommer från mig): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Steg 2: Den giftiga förändringen**

Överskottet, som inte har kunnat integreras i poolen, här motsvarande `40.000 Sats`, omdirigeras till **bad bank**-kontot, även kallat "toxic change", för att säkerställa en strikt separation från de andra UTXO:erna i Wallet.


Denna UTXO är farlig för användarens integritet eftersom den inte bara alltid är kopplad till sitt förflutna, och därför möjligen till sin ägares identitet, utan dessutom noteras som tillhörande en användare som har utfört en CoinJoin.


Om denna UTXO slås samman med blandade utgångar kommer den senare att förlora all den integritet som uppnåtts under CoinJoin-cyklerna, särskilt på grund av CIOH (*Common-Input-Ownership-Heuristic*). Om den slås samman med andra giftiga förändringar riskerar användaren att förlora sin integritet eftersom detta kommer att länka samman de olika posterna i CoinJoin-cyklerna. Den måste därför behandlas med försiktighet. Sättet att hantera denna giftiga UTXO kommer att beskrivas i den sista delen av denna artikel, och framtida handledningar kommer att gå djupare in på dessa metoder i PlanB Network.


**Steg 3: Den inledande mixen**

Efter slutförandet av `Tx0` skickas de utjämnade UTXO:erna till **premix**-kontot i vår Wallet, redo att introduceras i sin första cykel av CoinJoin, även kallad "initial mix". Om, som i vårt exempel, `Tx0` genererar flera UTXO:er avsedda för blandning, kommer var och en av dem att integreras i en separat initial CoinJoin.

I slutet av dessa inledande mixar kommer **premix**-kontot att vara tomt, medan våra mynt, som har betalat Mining-avgifterna för denna första CoinJoin, kommer att justeras exakt till det belopp som definieras av den valda poolen. I vårt exempel kommer våra ursprungliga UTXO:er på 108 000 Sats att ha reducerats till exakt 100 000 Sats.

![coinjoin](assets/en/8.webp)

**Steg 4: Remixerna**

Efter den första mixningen överförs UTXO:erna till kontot **postmix**. Detta konto samlar de redan mixade UTXO:erna och de som väntar på remixning. När Whirlpool-klienten är aktiv är de UTXO:er som finns på kontot **postmix** automatiskt tillgängliga för omblandning och kommer slumpmässigt att väljas ut för att delta i dessa nya cykler.


Som en påminnelse är remixer då 100% gratis: inga ytterligare serviceavgifter eller Mining-avgifter krävs. Att behålla UTXO:erna på **postmix**-kontot bibehåller således deras värde intakt och förbättrar samtidigt deras anonsets. Det är därför det är viktigt att låta dessa mynt delta i flera CoinJoin-cykler. Det kostar dig absolut ingenting, och det ökar deras anonymitetsnivåer.


När du bestämmer dig för att spendera blandade UTXO:er kan du göra det direkt från detta **postmix**-konto. Det är tillrådligt att behålla de blandade UTXO:erna på detta konto för att dra nytta av gratis remixer och för att förhindra att de lämnar Whirlpool-kretsen, vilket kan minska deras integritet.


Som vi kommer att se i följande handledning finns det också alternativet "mixa till" som ger möjlighet att automatiskt skicka dina blandade mynt till en annan Wallet, till exempel en Cold Wallet, efter ett definierat antal coinjoins.


Efter att ha diskuterat teorin, låt oss dyka in i praktiken med en handledning om hur man använder Whirlpool via Sparrow Wallet skrivbordsprogramvara!


## Självstudier: CoinJoin Whirlpool på Sparrow Wallet

Det finns många alternativ för att använda Whirlpool. Det första jag vill presentera för dig är Sparrow Wallet-alternativet, en öppen källkod Bitcoin Wallet-hanteringsprogramvara för PC.

Att använda Sparrow har fördelen att det är ganska enkelt att komma igång med, går snabbt att installera och kräver ingen annan utrustning än en dator och en internetanslutning. Det finns dock en anmärkningsvärd nackdel: coinjoins kommer endast att ske när Sparrow är lanserad och ansluten. Detta innebär att om du vill mixa och remixa dina bitcoins 24/7 måste du ständigt hålla din dator påslagen.


### Installera Sparrow Wallet

För att börja behöver du naturligtvis programvaran Sparrow Wallet. Du kan ladda ner den direkt från [den officiella webbplatsen] (https://sparrowwallet.com/download/) eller på [deras GitHub] (https://github.com/sparrowwallet/sparrow/releases).


Innan du installerar programvaran är det viktigt att verifiera signaturen och integriteten för den körbara filen som du just har laddat ner. Om du vill ha mer information om installationsprocessen och verifiering av Sparrow-programvara rekommenderar jag att du läser den här andra handledningen: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Skapa en Software Wallet

När du har installerat programvaran måste du fortsätta med att skapa en Bitcoin Wallet. Det är viktigt att notera att för att delta i coinjoins är det nödvändigt att använda en Software Wallet (även kallad en "Hot Wallet"). Därför kommer **det inte att vara möjligt att utföra coinjoins med en Wallet som säkras av en Hardware Wallet**.


Även om det inte är absolut nödvändigt, rekommenderas det starkt att välja att använda en stark BIP39 passphrase för denna Wallet om du planerar att blanda betydande mängder.


För att skapa en ny Wallet, öppna Sparrow, klicka sedan på fliken `File` och `New Wallet`.


![sparrow](assets/notext/9.webp)


Välj ett namn för denna Wallet, t.ex: "CoinJoin Wallet". Klicka på knappen `Create Wallet`.


![sparrow](assets/notext/10.webp)


Lämna standardinställningarna och klicka sedan på knappen `Ny eller importerad Software Wallet`.


![sparrow](assets/notext/11.webp)


När du öppnar fönstret för skapande av Wallet rekommenderar jag att du väljer en sekvens på 12 ord, eftersom det är fullt tillräckligt. Välj `generate New` för att generate en ny återställningsfras, och klicka på `Use passphrase` om du vill lägga till en BIP39 passphrase. Det är viktigt att göra en fysisk säkerhetskopia av din återställningsinformation, antingen på papper eller på ett metallstöd, för att säkerställa säkerheten för dina bitcoins.


![sparrow](assets/notext/12.webp)

Säkerställ att din säkerhetskopia av återställningsfrasen är giltig innan du klickar på `Bekräfta säkerhetskopia...`. Sparrow kommer då att be dig att ange din fras igen för att verifiera att du har noterat den. När detta steg har slutförts fortsätter du genom att klicka på "Skapa nyckellager".

![sparrow](assets/notext/13.webp)


Lämna den föreslagna avledningssökvägen som standard och tryck på `Importera Keystore`. I mitt exempel skiljer sig härledningsvägen något eftersom jag använder Testnet för den här handledningen. Den härledningsväg som bör visas för dig är följande:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


Därefter kommer Sparrow att visa avledningsdetaljerna för din nya Wallet. Om du har ställt in en passphrase rekommenderas det starkt att du noterar ditt "masterfingeravtryck". Även om detta fingeravtryck för huvudnyckeln inte är känslig data, kommer det att vara användbart för dig att senare verifiera att du verkligen har tillgång till rätt Wallet och för att bekräfta att det inte finns några fel när du anger din passphrase.


Klicka på knappen `Apply`.


![sparrow](assets/notext/15.webp)


Sparrow uppmanar dig att skapa ett lösenord för din Wallet. Detta lösenord kommer att krävas för att komma åt den via Sparrow Wallet-programvaran. Välj ett starkt lösenord, gör en säkerhetskopia av det och klicka sedan på "Ange lösenord".


![sparrow](assets/notext/16.webp)


### Mottagande av bitcoins

När du har skapat din Wallet kommer du initialt att ha ett enda konto med indexet "0". Detta är **deposit**-kontot som vi pratade om i de tidigare delarna. Det här är det konto som du måste skicka bitcoins till för att blanda.


För att göra detta, välj fliken `Receive` på vänster sida av fönstret. Sparrow kommer automatiskt generate ett nytt tomt Address för att ta emot bitcoins.


![sparrow](assets/notext/17.webp)


Du kan ange en etikett för denna Address och sedan skicka de bitcoins som ska blandas till den.


![sparrow](assets/notext/18.webp)


### Tillverkning av Tx0

När transaktionen är bekräftad kan du gå till fliken "Utgångar".


![sparrow](assets/notext/19.webp)


Välj sedan den eller de UTXO som du vill skicka till CoinJoin-cyklerna. Om du vill välja flera UTXO:er samtidigt håller du ned "Ctrl"-tangenten medan du klickar på de UTXO:er du vill välja.


![sparrow](assets/notext/20.webp)


Klicka sedan på knappen `Mix Selected` längst ned i fönstret. Om den här knappen inte visas på din Interface beror det på att du befinner dig på en Wallet som är säkrad med en Hardware Wallet. Du måste använda en Software Wallet för att utföra coinjoins med Sparrow.

![sparrow](assets/notext/21.webp)

Ett fönster öppnas för att förklara hur Whirlpool fungerar. Detta är en förenkling av vad jag förklarade i de tidigare delarna. Klicka på `Nästa` för att gå vidare.


![sparrow](assets/notext/22.webp)


På nästa sida kan du ange en "SCODE" om du har en sådan. En SCODE är en kampanjkod som erbjuder rabatt på poolens serviceavgifter. Samourai Wallet tillhandahåller ibland sådana koder till sina användare under speciella evenemang. Jag råder dig att [följa Samourai Wallet](https://twitter.com/SamouraiWallet) på sociala medier så att du inte går miste om framtida SCODES.


På samma sida måste du också ställa in avgiftssatsen för `Tx0` och din första mix. Detta val kommer att påverka bekräftelsehastigheten för din förberedande transaktion och din första CoinJoin. Kom ihåg att du är ansvarig för Mining-avgifterna för `Tx0` och den första mixen, men du kommer inte att vara skyldig Mining-avgifter för efterföljande remixer. Justera skjutreglaget `Premix Priority` enligt dina önskemål och klicka sedan på `Next`.


![sparrow](assets/notext/23.webp)


I det nya fönstret har du möjlighet att välja den pool som du vill ange med hjälp av rullgardinsmenyn. I mitt fall, efter att ursprungligen ha valt en UTXO på 456 214 Sats, är mitt enda möjliga val poolen på 100 000 Sats. Denna Interface informerar dig också om de serviceavgifter som ska betalas samt antalet UTXO:er som kommer att integreras i poolen. Om villkoren verkar tillfredsställande för dig, fortsätt genom att klicka på `Preview Premix`.


![sparrow](assets/notext/24.webp)


Efter detta steg kommer Sparrow att be dig ange lösenordet för din Wallet, det lösenord som du angav när du skapade den i programmet. När lösenordet har angetts kommer du att få tillgång till förhandsgranskningen av din `Tx0`. På vänster sida av fönstret ser du att Sparrow har skapat de olika konton som krävs för att använda Whirlpool (`Deposit`, `Premix`, `Postmix` och `Badbank`). Du kommer också att ha möjlighet att se strukturen på din `Tx0`, med de olika utgångarna:


- Serviceavgifterna;
- De utjämnade UTXO:erna avsåg att ingå i poolen;
- Den toxiska förändringen (Doxxic Change).


![sparrow](assets/notext/25.webp)


Om transaktionen är till din belåtenhet klickar du på `Broadcast Transaction` för att sända din `Tx0`. Annars har du möjlighet att justera parametrarna för denna `Tx0` genom att välja `Clear` för att radera de inmatade uppgifterna och starta skapandeprocessen från början.


### Utförande av sammanfogningar

När Tx0 har sänts ut hittar du dina UTXO:er redo att blandas i `Premix`-kontot.

![sparrow](assets/notext/26.webp)


När "Tx0" har bekräftats registreras dina UTXO:er hos koordinatorn och de första mixningarna startar automatiskt i tur och ordning.


![sparrow](assets/notext/27.webp)


Genom att kontrollera `Postmix`-kontot kommer du att observera UTXO: erna som härrör från de första mixarna. Dessa mynt kommer att förbli redo för efterföljande remixning, vilket inte kommer att medföra några extra avgifter.


![sparrow](assets/notext/28.webp)


I kolumnen "Mixes" kan man se antalet coinjoins som utförts av vart och ett av dina mynt. Som vi kommer att se i följande avsnitt är det som verkligen betyder något inte så mycket antalet remixer i sig, utan snarare de associerade anonsets, även om dessa två indikatorer delvis är relaterade.


![sparrow](assets/notext/29.webp)


För att tillfälligt stoppa coinjoins, klicka bara på `Stop Mixing`. Du kan när som helst återuppta arbetet genom att välja `Start Mixing`.


![sparrow](assets/notext/30.webp)


För att säkerställa kontinuerlig tillgänglighet av dina UTXO:er för remixning är det nödvändigt att hålla Sparrow-programvaran aktiv. Om du stänger programvaran eller stänger av datorn kommer coinjoins att pausas. En lösning för att kringgå detta problem är att inaktivera sömnfunktioner via operativsystemets inställningar. Dessutom erbjuder Sparrow ett alternativ för att förhindra att datorn automatiskt går i viloläge, som du hittar under fliken "Verktyg" med rubriken "Förhindra att datorn går i viloläge".


![sparrow](assets/notext/31.webp)


### Färdigställande av coinjoins

För att spendera dina blandade bitcoins har du flera alternativ. Den mest direkta metoden är att gå in på `Postmix`-kontot och välja fliken `Sänd`.


![sparrow](assets/notext/32.webp)


I det här avsnittet har du möjlighet att ange destinationen Address, beloppet som ska skickas och transaktionsavgifterna, på samma sätt som för alla andra transaktioner som görs med Sparrow Wallet. Om du vill kan du också dra nytta av avancerade sekretessfunktioner som Stonewall genom att klicka på knappen `Privacy`.


![sparrow](assets/notext/33.webp)


[-> Läs mer om Stonewall-transaktioner] (https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Om du vill göra ett mer exakt urval av dina mynt att spendera, gå till fliken `UTXOs`. Välj de UTXO:er som du specifikt vill konsumera och tryck sedan på knappen `Send Selected` för att initiera transaktionen.


![sparrow](assets/notext/34.webp)

Slutligen, alternativet `Mix to...` som finns tillgängligt på Sparrow gör det möjligt att automatiskt ta bort en utvald UTXO från CoinJoin-cykler, utan att ådra sig ytterligare avgifter. Denna funktion gör det möjligt att bestämma ett antal remixer varefter UTXO inte kommer att återintegreras i ditt `Postmix`-konto, utan istället kommer att överföras direkt till en annan Wallet. Detta alternativ används ofta för att automatiskt skicka blandade bitcoins till en Cold Wallet.

För att använda detta alternativ börjar du med att öppna den mottagande Wallet tillsammans med din CoinJoin Wallet i Sparrow-programvaran.


![sparrow](assets/notext/35.webp)


Gå sedan till fliken `UTXOs` och klicka sedan på knappen `Mix to...` längst ner i fönstret.


![sparrow](assets/notext/36.webp)


Ett fönster öppnas, börja med att välja destination Wallet från rullgardinsmenyn.


![sparrow](assets/notext/37.webp)


Välj CoinJoin-tröskeln bortom vilken uttaget kommer att göras automatiskt. Jag kan inte ge dig ett exakt antal remixer att utföra, eftersom detta varierar beroende på din personliga situation och dina integritetsmål, men undvik att välja en tröskel som är för låg. Jag rekommenderar att du läser den här andra artikeln för att lära dig mer om remixningsprocessen: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


Du kan låta alternativet `Indexintervall` vara kvar på standardvärdet `Full`. Denna funktion gör det möjligt att mixa samtidigt från olika klienter, men det är inte vad vi vill göra i denna handledning. För att slutföra och aktivera alternativet `Mix to...`, tryck på `Restart Whirlpool`.


![sparrow](assets/notext/38.webp)


Var dock försiktig när du använder alternativet `Mix to`, eftersom borttagning av blandade mynt från ditt `Postmix`-konto kan öka risken för att din integritet äventyras avsevärt. Anledningarna till denna risk beskrivs närmare i följande avsnitt.


## Hur vet man kvaliteten på våra CoinJoin-cykler?

För att en CoinJoin verkligen ska vara effektiv är det viktigt att den uppvisar en god homogenitet mellan beloppen för in- och utdata. Denna enhetlighet förstärker antalet möjliga tolkningar i en extern observatörs ögon och ökar därmed osäkerheten kring transaktionen. För att kvantifiera denna osäkerhet som genereras av en CoinJoin kan man beräkna transaktionens entropi. För en djupgående undersökning av dessa indikatorer hänvisar jag till handledningen: [BOLTZMANN CALCULATOR] (https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Whirlpool-modellen är erkänd som den som ger mest homogenitet i coinjoins.

Därefter utvärderas prestandan hos flera CoinJoin-cykler baserat på storleken på de grupper i vilka ett mynt är dolt. Storleken på dessa grupper definierar vad som kallas anonsets. Det finns två typer av anonsets: den första bedömer den integritet som uppnåtts mot retrospektiv analys (från nutid till dåtid) och den andra mot prospektiv analys (från dåtid till nutid). För en detaljerad förklaring av dessa två indikatorer ber jag dig att läsa handledningen: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Hur hanterar man postmix?

Efter att ha utfört CoinJoin-cykler är den bästa strategin att behålla dina UTXO:er på **postmix**-kontot i väntan på framtida användning. Det är till och med tillrådligt att låta dem remixas på obestämd tid tills du behöver spendera dem.


Vissa användare kan överväga att överföra sina blandade bitcoins till en Wallet som säkras av en Hardware Wallet. Detta är möjligt, men det är viktigt att följa rekommendationerna från Samourai Wallet noggrant för att inte äventyra den förvärvade sekretessen.


Att slå samman UTXO:er är det vanligaste misstaget. Det är nödvändigt att undvika att kombinera blandade UTXO:er med oblandade UTXO:er i samma transaktion, för att undvika CIOH (*Common-Input-Ownership-Heuristic*). Detta kräver noggrann hantering av dina UTXO:er inom din Wallet, särskilt när det gäller märkning. Utöver CoinJoin är sammanslagning av UTXO:er i allmänhet en dålig praxis som ofta leder till förlust av integritet när den inte hanteras korrekt.


Det är också viktigt att vara försiktig med att konsolidera blandade UTXO:er med varandra. Måttliga konsolideringar är tänkbara om dina blandade UTXO:er har betydande anonsets, men detta kommer oundvikligen att minska dina mynts konfidentialitet. Se till att konsolideringar varken är för stora eller utförs efter ett otillräckligt antal remixer, eftersom detta riskerar att etablera härledbara länkar mellan dina UTXO:er före och efter CoinJoin-cyklerna. Om du är osäker på dessa manipulationer är den bästa metoden att inte konsolidera UTXO:erna efter mixningen, utan att överföra dem en efter en till din Hardware Wallet och generera en ny tom Address varje gång. Kom ihåg att märka varje mottagen UTXO på rätt sätt.

Det rekommenderas också att du inte överför dina UTXO:er efter blandning till en Wallet med ovanliga skript. Om du till exempel går in i Whirlpool från en Multisig Wallet med hjälp av `P2WSH`-skript är det liten chans att du blandas med andra användare som har samma typ av Wallet ursprungligen. Om du drar tillbaka din postmix till samma Multisig Wallet kommer sekretessnivån för dina blandade bitcoins att minska kraftigt. Utöver skript finns det många andra Wallet-fingeravtryck som kan lura dig.

Som med alla Bitcoin-transaktioner är det också viktigt att inte återanvända mottagningsadresser. Varje ny transaktion ska tas emot på en ny, blank Address.


Den enklaste och säkraste lösningen är att låta dina blandade UTXO:er vila på deras **postmix**-konto, låta dem remixa och bara röra vid dem för att spendera. Samourai- och Sparrow-plånböckerna har ytterligare skydd mot alla dessa kedjeanalysrelaterade risker. Dessa skydd hjälper dig att undvika att göra misstag.


## Hur hanterar man en doxisk förändring?

Därefter måste du vara försiktig med att hantera doxisk förändring, den förändring som inte kunde komma in i CoinJoin-poolen. Dessa toxiska UTXO:er, som härrör från användningen av Whirlpool, utgör en risk för din integritet eftersom de skapar en koppling mellan dig och användningen av CoinJoin. Därför är det absolut nödvändigt att hantera dem med försiktighet och inte kombinera dem med andra UTXO:er, särskilt inte blandade UTXO:er. Här är olika strategier som du kan överväga för att använda dem:


- Blanda dem i mindre pooler:** Om din giftiga UTXO är tillräckligt betydande för att komma in i en mindre pool ensam, överväg att blanda den. Detta är ofta det bästa alternativet. Det är dock viktigt att inte slå samman flera giftiga UTXO:er för att få tillgång till en pool, eftersom detta kan länka dina olika poster;
- Markera dem som "icke spenderbara":** En annan metod är att inte längre använda dem, att markera dem som "icke spenderbara" på deras dedikerade konto och att bara HODL. Detta säkerställer att du inte av misstag spenderar dem. Om värdet på Bitcoin ökar kan nya pooler som är mer lämpade för dina giftiga UTXO:er dyka upp;
- Gör donationer:** Överväg att göra donationer, även blygsamma, till utvecklare som arbetar med Bitcoin och dess tillhörande programvara. Du kan också donera till organisationer som accepterar BTC. Om det verkar för komplicerat att hantera dina giftiga UTXO: er kan du helt enkelt bli av med dem genom att göra en donation;
- Köp presentkort:** Plattformar som [Bitrefill] (https://www.bitrefill.com/) gör att du kan Exchange bitcoins för presentkort som kan användas hos olika handlare. Detta kan vara ett sätt att göra sig av med dina giftiga UTXO:er utan att förlora det tillhörande värdet.
- Konsolidera dem på Monero:** Samourai Wallet erbjuder nu en atomic swap-tjänst mellan BTC och XMR. Detta är perfekt för att hantera giftiga UTXO: er genom att konsolidera dem på Monero, utan att äventyra din integritet via CIOH, innan du skickar tillbaka dem till Bitcoin. Detta alternativ kan dock vara kostsamt när det gäller Mining-avgifter och premien på grund av likviditetsbegränsningar.
- Skicka dem till Lightning Network:** Att överföra dessa UTXO till Lightning Network för att dra nytta av reducerade transaktionsavgifter är ett alternativ som kan vara intressant. Denna metod kan dock avslöja viss information beroende på din användning av Lightning och bör därför användas med försiktighet.


Detaljerade handledningar om hur man implementerar dessa olika tekniker kommer snart att erbjudas på PlanB Network.


**Ytterligare resurser:**

[Sparrow Wallet Video Tutorial] (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Dokumentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter-tråd om CoinJoins] (https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogginlägg om CoinJoins] (https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).