---
name: Introduktion till Bitcoin Mining
goal: Förstå hur Mining-industrin fungerar genom en praktisk övning av återanvändning av ASIC.
objectives: 

  - Förstå teorin bakom Mining
  - Förstå Mining-branschen
  - Förvandla en S9 till en värmare
  - Min din första Satoshi

---

# Dina första steg i Mining!


I den här utbildningen kommer vi att fördjupa oss i Mining-industrin för att avmystifiera detta komplexa ämne! Utbildningen är tillgänglig för alla och kräver ingen initial investering.


Det första avsnittet kommer att vara teoretiskt, där Ajelex och jag kommer att ha en djupgående diskussion om olika ämnen relaterade till Mining. Detta kommer att hjälpa oss att bättre förstå denna bransch och de ekonomiska och geopolitiska frågor som är förknippade med den.

I det andra avsnittet kommer vi att ta itu med ett praktiskt fall. Vi kommer faktiskt att lära oss hur man förvandlar en begagnad S9 Miner till ett hemvärmesystem! Genom skriftliga guider och videor kommer vi att visa och förklara alla steg för att uppnå detta hemma hos dig :)


Genom den här kursen hoppas vi kunna visa dig att Mining-industrin är mer komplex än den verkar, och att studera den hjälper till att nyansera den ekologiska debatt som är kopplad till den!

Om du behöver hjälp med installationen har en Telegram-grupp skapats för studenter, och alla nödvändiga komponenter finns på vår e-handelsplattform!


+++

# Inledning


<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>


## Kursöversikt


<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>


Välkommen till kursen MIN201: En introduktion till Mining. Ajelex, Jim & Rogzy är glada att få guida dig genom dina första steg i den här branschen. Vi hoppas att du tycker om kursen och påbörjar ditt Mining-äventyr!


Den här utbildningen tar dig till hjärtat av Bitcoin Mining-industrin och ger dig både teoretisk och praktisk kunskap. Oavsett om du är nybörjare eller redan är bekant med ämnet kommer den här kursen att hjälpa dig att förstå de ekonomiska och tekniska aspekterna av Mining, samtidigt som du slutför ett praktiskt projekt för att återanvända en ASIC för uppvärmning av hemmet.


**Avsnitt 2: Allt om Mining**

I detta avsnitt kommer vi att ge en omfattande förståelse för Bitcoin Mining. Vi kommer att täcka den tekniska funktionen av Mining, dess roll i Bitcoin-protokollet och dess ekonomiska och geopolitiska konsekvenser. Du kommer också att utforska det komplexa förhållandet mellan Bitcoin-priset och Hashrate, samt frågor som rör suveränitet och reglering i branschen.


**Avsnitt 3: Mining och återanvändning av värme i hemmet**

Därefter kommer vi att dyka in i praktisk tillämpning med konceptet Attakai, som syftar till att demokratisera Mining för hemmabruk genom att omvandla begagnade S9-gruvbrytare till uppvärmningsanordningar för hemmabruk. Du kommer att lära dig hur man köper och modifierar en begagnad ASIC, samtidigt som du förbereder nödvändig utrustning för hårdvarumodifieringar.


**Avsnitt 4: Attakai - Modifiera programvaran i en Antminer S9**

Här får du lära dig hur du konfigurerar din Antminer S9 för hemmabruk. Vi guidar dig genom att sätta upp en Wi-Fi/Ethernet-brygga, återställa din enhet, installera BraiinsOS+ och optimera den för Mining.


**Avsnitt 5: Attakai - Modifieringar av fläktar**

För att optimera din Antminer S9 för användning som extravärmare, kommer detta avsnitt att lära dig hur du byter ut Supply-fläktarna och huvudfläktarna. Dessa ändringar är viktiga för att minska bullret och förbättra enhetens termiska effektivitet.


**Avsnitt 6: Attakai - Konfiguration**

Slutligen får du lära dig hur du går med i en Mining pool och optimerar prestandan hos din Antminer S9. Du kommer att upptäcka hur du uppnår optimal energieffektivitet och effektivt bryter dina första satoshis.


Är du redo att upptäcka världen i Bitcoin Mining och ta dig an den praktiska utmaningen i Attakai? Låt oss komma igång!



# Allt du behöver veta om Mining


<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>


## Förklaring av Mining


<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>


### Mining förklaras: pusselanalogin


För att förklara konceptet Mining på ett förenklat sätt kan en relevant analogi användas: ett pussel. Precis som ett pussel är Mining en komplex uppgift att utföra men lätt att verifiera när den är klar. I samband med Bitcoin Mining strävar gruvarbetare efter att snabbt lösa ett digitalt pussel. Den första Miner som löser pusslet presenterar sin lösning för hela nätverket, som sedan enkelt kan verifiera dess giltighet. Denna framgångsrika verifiering gör det möjligt för Miner att validera ett nytt block och lägga till det i Bitcoin Timechain. Som ett erkännande av sitt arbete, som innebär betydande kostnader, belönas Miner med ett visst antal bitcoins. Denna belöning fungerar som ett ekonomiskt incitament för miners att fortsätta sitt arbete med att validera transaktioner och säkra Bitcoin-nätverket.


![image](assets/en/01.webp)


Inledningsvis i Bitcoin-nätverket var den tilldelade belöningen 50 bitcoins var tionde minut, parallellt med att gruvarbetarna upptäckte ett block var tionde minut i genomsnitt. Denna belöning genomgår en Halving var 210.000:e block, ungefär vart fjärde år. Denna ersättning fungerar som ett kraftfullt incitament för att uppmuntra miners att delta i Mining-processen trots dess energikostnad. Utan en belöning skulle den elintensiva Mining överges, vilket skulle äventyra säkerheten och stabiliteten i hela Bitcoin-nätverket.

Den nuvarande Mining-belöningen är tvåfaldig. Å ena sidan inkluderar den skapandet av nya bitcoins, vilket har minskat från 50 bitcoins var tionde minut initialt till 6,25 bitcoins idag (2023). Å andra sidan inkluderar det transaktionsavgifter, eller Mining-avgifter, från de transaktioner som Miner väljer att inkludera i sitt block. När en Bitcoin-transaktion görs betalas transaktionsavgifter. Dessa avgifter fungerar som en slags auktion där användarna anger hur mycket de är villiga att betala för att få sin transaktion inkluderad i nästa block. För att maximera sin belöning väljer miners, som agerar i eget intresse, de mest lönsamma transaktionerna att inkludera i sitt block, med tanke på det begränsade tillgängliga utrymmet. Mining:s belöning består således av både generering av nya bitcoins och transaktionsavgifter, vilket ger ett kontinuerligt incitament för miners och säkerställer Bitcoin-nätverkets livslängd och säkerhet.


### Gruvarbetare och deras verktyg: Mining


Mining-processen innebär att man hittar en giltig Hash som är godtagbar för Bitcoin-nätverket. När denna Hash väl har beräknats och hittats är den irreversibel, ungefär som när potatis blir till potatismos. Den verifierar en viss funktion utan möjlighet att gå tillbaka. Miners, i konkurrens, använder maskiner för att beräkna dessa hashes. Även om det är teoretiskt möjligt att hitta denna Hash manuellt, gör komplexiteten i operationen detta alternativ ogenomförbart. Därför används datorer som kan utföra dessa beräkningar snabbt och som förbrukar en betydande mängd el.


I början dominerade CPU-eran, där gruvarbetarna använde sina persondatorer för Bitcoin Mining. Upptäckten av fördelarna med GPU:er (grafikkort) för denna uppgift markerade en vändpunkt, vilket avsevärt ökade Hashrate och minskade energiförbrukningen. Utvecklingen stannade inte där, utan FPGA:er (Field Programmable Gate Arrays) introducerades senare. FPGA:erna fungerade som en plattform för utvecklingen av ASIC:er (applikationsspecifika integrerade kretsar).


![image](assets/en/02.webp)


ASICs är chip som kan jämföras med ett CPU-chip, men de är utvecklade för att utföra endast en specifik typ av beräkning på effektivast möjliga sätt. Med andra ord kan en CPU utföra en mängd olika typer av beräkningar utan att vara särskilt optimerad för den ena eller andra typen av beräkning, medan en ASIC endast kan utföra en typ av beräkning, men mycket effektivt. Bitcoin ASICs är konstruerade för beräkning av SHA256-algoritmen.

Numera använder miners uteslutande ASIC:er som är avsedda för denna operation, optimerade för att testa det maximala antalet kombinationer med minsta möjliga energiförbrukning och så snabbt som möjligt. Dessa datorer, som inte kan utföra andra uppgifter än Bitcoin Mining, är ett påtagligt bevis på den kontinuerliga utvecklingen och den ökande specialiseringen av Bitcoin Mining-industrin. Denna ständiga utveckling återspeglar den inneboende dynamiken i Bitcoin, där en svårighetsjustering säkerställer produktionen av ett block var tionde minut trots den exponentiella ökningen av Mining-kapaciteten.


För att illustrera intensiteten i denna process kan man tänka sig en typisk Miner som kan uppnå 14 TeraHash per sekund, eller 14 biljoner försök varje sekund att hitta rätt Hash. I Bitcoin-nätverkets skala når vi nu cirka 300 HexaHash per sekund, vilket belyser den kollektiva kraften som mobiliserats i Bitcoin Mining.


### Justering av svårighetsgrad


Svårighetsjustering är en avgörande mekanism i driften av Bitcoin-nätverket och säkerställer att block bryts i genomsnitt var 10:e minut. Denna varaktighet är ett genomsnitt eftersom Mining-processen faktiskt är ett sannolikhetsspel, som liknar att kasta tärning i hopp om att få ett nummer som är lägre än det nummer som definieras av svårigheten. Vart 2016:e block justerar nätverket Mining-svårigheten baserat på den genomsnittliga tid som krävs för att bryta de föregående blocken. Om den genomsnittliga tiden är längre än 10 minuter minskas svårighetsgraden och omvänt, om den genomsnittliga tiden är lägre, ökas svårighetsgraden. Denna justeringsmekanism säkerställer att Mining-tiden för nya block förblir konstant över tiden, oavsett antalet miners eller den totala datorkraften i nätverket. Det är därför som Bitcoin Blockchain också kallas för Timechain.


![image](assets/en/03.webp)



- Exempel från Kina:

Fallet Kina illustrerar perfekt denna mekanism för anpassning av svårigheter. Med riklig och billig energi var Kina det viktigaste globala navet för Bitcoin Mining. År 2021 förbjöd landet plötsligt Bitcoin Mining på sitt territorium, vilket resulterade i en massiv minskning av det globala Bitcoin-nätverkets Hashrate, cirka 50 %. Denna snabba minskning av Mining-kraften kunde ha stört Bitcoin-nätverket allvarligt genom att öka den genomsnittliga block Mining-tiden. Mekanismen för justering av svårighetsgraden trädde dock i kraft och minskade svårighetsgraden för Mining för att säkerställa att frekvensen för blockering av Mining ligger kvar på i genomsnitt 10 minuter. Detta fall visar effektiviteten och motståndskraften hos Bitcoin:s mekanism för svårighetsjustering, som säkerställer nätverkets stabilitet och förutsägbarhet, även inför plötsliga och betydande förändringar i det globala Mining-landskapet.


### Utveckling av Bitcoin Mining maskiner


När det gäller utvecklingen av Bitcoin Mining-maskiner är det viktigt att notera att sammanhanget är mer inriktat på en traditionell affärsmodell. Miners tjänar sin inkomst från blockvalidering, en uppgift med relativt låg sannolikhet för framgång. Den nuvarande modellen som används, Antminer S9, är visserligen en äldre modell som lanserades runt 2016, men den är fortfarande i omlopp på andrahandsmarknaden och handlas för cirka 100 till 200 euro. Priset på Mining-maskiner varierar dock beroende på värdet på Bitcoin, och en nyare modell, Antminer S19, uppskattas för närvarande till cirka 3000 euro.


Med tanke på de ständiga tekniska framstegen inom Mining-området måste yrkesverksamma strategiskt positionera sig. Mining-industrin är föremål för kontinuerliga innovationer, vilket framgår av den senaste lanseringen av J-versionen av S19 och den förväntade lanseringen av S19 XP, som erbjuder betydligt högre Mining-kapacitet. Dessutom är förbättringarna inte bara relaterade till maskinernas råprestanda. Till exempel använder den nya S19 XP-modellen ett Liquid-kylsystem, en teknisk modifiering som möjliggör en betydande förbättring av energieffektiviteten. Även om innovation förblir en konstant kommer framtida effektivitetsvinster sannolikt att vara mindre jämfört med de som hittills observerats, på grund av att en viss tröskel för teknisk innovation har nåtts.


![image](assets/en/04.webp)


Sammanfattningsvis fortsätter Bitcoin Mining-industrin att anpassa sig och utvecklas, och branschaktörerna måste förutse minskande effektivitetsvinster i framtiden och anpassa sina strategier därefter. Framtida tekniska framsteg, även om de fortfarande är närvarande, kommer sannolikt att ske i mindre skala, vilket återspeglar sektorns växande mognad.


## Mining-industrin


<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>


### Mining-pooler


För närvarande har Bitcoin Mining utvecklats till en seriös och betydande industri, med många aktörer som nu är allmänt kända och ett ökande antal betydande gruvarbetare. Denna utveckling har gjort Mining nästan otillgänglig för små aktörer på grund av de höga kostnaderna för att skaffa nya Mining-maskiner. Detta väcker frågan om fördelningen av Hashrate mellan olika marknadsaktörer. Situationen är komplex eftersom det är viktigt att undersöka både fördelningen av Hashrate mellan olika företag och mellan olika Mining-pooler.


![image](assets/en/05.webp)


En Mining pool är en grupp miners som kombinerar sina dataresurser för att öka sina chanser till Mining. Detta samarbete är nödvändigt eftersom en isolerad liten Mining-maskin konkurrerar mot branschjättar, vilket minskar dess chanser att lyckas till en försumbar nivå. Mining fungerar enligt en lotteriprincip och chansen att vinna ett block (och därmed Bitcoin-belöningen) var tionde minut är extremt låg för en enskild liten Miner. Genom att gå samman i en pool kan miners kombinera sin datorkraft, hitta block oftare och sedan fördela belöningarna proportionellt mot varje Miner:s bidrag till poolen.


Till exempel, om en pool hittar ett block och vinner 6,25 bitcoins, skulle en Miner som bidrar med 1% av poolens totala datorkraft få 1% av de 6,25 bitcoins som tjänats. Det bör dock noteras att Mining-pooler i allmänhet tar en liten provision (vanligtvis cirka 2%) för att täcka kooperativets driftskostnader.


### Programvara som används av branschen


I samband med Bitcoin Mining är mjukvarans roll lika avgörande som hårdvarans. Ett exempel på detta illustreras av Bitmain, en produktiv tillverkare som utvecklade Antminer S9. Förutom Mining-hårdvara är branschen starkt beroende av Mining-pooler som samarbetar, till exempel Brainspool, som kontrollerar cirka 5% av det globala Hashrate i Bitcoin-nätverket.

Aktörerna i denna bransch strävar ständigt efter att öka effektiviteten genom hård- och mjukvara. En populär programvara som används i detta sammanhang är till exempel BrainsOS Plus. Denna mjukvara ersätter det ursprungliga operativsystemet i Mining-maskinen, vilket gör att samma operationer kan utföras mer effektivt. Med en sådan programvara kan en Miner öka effektiviteten i sin maskin med 25%. Det innebär att för en motsvarande mängd elektricitet kan maskinen producera ytterligare 25 % Hashrate, vilket ökar belöningen som Miner får. Denna mjukvaruoptimering är en viktig del av konkurrenskraften i Bitcoin Mining, vilket visar vikten av en integrerad strategi som kombinerar förbättringar av både hårdvara och mjukvara för att maximera effektiviteten och avkastningen.


### Reglering och eltariffer


Som observerats i Kina och på andra håll har regleringar ett betydande inflytande på Mining. Även om det inte finns några betydande gruvföretag i Frankrike, utgör regleringar och höga elpriser i Europa stora hinder. Gruvbolagen söker ständigt efter billig el för att maximera sina vinster. Därför lockar inte de höga elkostnaderna i Europa och Frankrike gruvarbetare till dessa regioner.


Gruvarbetare tenderar att söka sig till regioner med låga elpriser, ofta i tillväxtländer eller länder med energiöverskott. Till exempel ligger en stor del av den globala Hashrate i Texas, USA. Texas har ett oberoende elnät som inte delar sina energiresurser med andra delstater. Denna unika situation leder ofta till att Texas producerar mer el än nödvändigt för att undvika brist, vilket skapar ett överskott. Bitcoin-miners drar nytta av denna överproduktion genom att etablera verksamhet i Texas, där de kan bryta bitcoins till mycket låga elpriser under perioder med energiöverskott. Denna situation visar att regleringar och eltariffer har ett betydande inflytande på Bitcoin Mining, vilket belyser vikten av dessa faktorer i gruvarbetarnas beslutsfattande om var de ska förlägga sin Mining-verksamhet.


### Vart tar gruvarbetarna vägen och energihantering?


Genom att belysa Bitcoin-gruvarbetarnas inverkan på energisektorn är utvecklingen tydlig: dessa aktörer söker ständigt efter källor till billig el, ofta sådana som är bortkastade eller outnyttjade. Detta fenomen är tydligt i regioner med ny elektrisk infrastruktur, till exempel de som är utrustade med nya vattenkraftsdammar.


Låt oss ta ett exempel. I ett land där man håller på att bygga en damm startar elproduktionen ofta innan distributionsledningarna är helt i drift. Denna tidslucka kan leda till betydande kostnader och avskräcka från investeringar i sådana infrastrukturprojekt. Bitcoin miners kan dock fungera som en flexibel efterfrågekälla, redo att konsumera denna "föräldralösa" el och därmed bidra till att kompensera för infrastrukturkostnaderna. Innebörden är att nya installationer kan bli omedelbart lönsamma, vilket främjar skapandet av nya elkällor. Denna princip gäller även i mindre skala. Oavsett om det är en enskild person som använder en vattenkraftsgenerator i en liten flod eller ett hushåll som är utrustat med solpaneler, kan den överskottsel som produceras användas för att driva Bitcoin Mining:s verksamhet.


I Frankrike, till exempel, matas överskottsel från solpaneler tillbaka in i elnätet och producenterna kompenseras med en konsumtionskredit från EDF. På samma sätt kan man föreställa sig en Miner som drivs av denna överskottsel och stängs av när den lokala efterfrågan är lika stor som Supply. Även om detta kan verka själviskt, att prioritera Bitcoin-produktion framför att stödja det lokala elnätet, ger det en annan vinkel: att stabilisera elnätet. Den komplexa hanteringen av överskottsel, ibland även med tillhörande kostnader för bortskaffande, kan förenklas avsevärt. Bitcoin-gruvor kan absorbera dessa överskott och fungera som en flexibel buffert som justerar efterfrågan snarare än Supply. I en värld där elproduktionen från förnybara (icke-kontrollerbara) källor ständigt ökar kan gruvarbetare spela en nyckelroll för att säkerställa balansen i våra elnät, samtidigt som de drar nytta av billig eller överskottsel för att driva sin Mining-verksamhet.


### Mining centralisering


Mining centralisering tas upp som en stor utmaning. Stora aktörer, såsom Foundry, dominerar marknaden, vilket potentiellt kan leda till transaktionscensur. Denna centralisering kan också göra nätverket sårbart för attacker, inklusive 51%-attacken, där en aktör eller grupp kontrollerar mer än 50% av nätverkets hashingkraft, vilket gör att de kan kontrollera och manipulera nätverket.


Regleringsrisk Det betonas att om ett land som USA skulle besluta att reglera eller förbjuda vissa Bitcoin-transaktioner skulle det kunna ha en betydande inverkan på nätverket, särskilt om en stor del av hashkraften är centraliserad i det landet.


![image](assets/en/06.webp)


För att motverka denna centralisering diskuteras olika strategier:



- Hem Mining: Idén med Hem Mining är baserad på decentraliseringen av Mining-aktivitet. Det uppmuntrar individer att delta i Mining från sina hem och därmed distribuera Hashrate mer allmänt.
- Stratum V2: Stratum V2-protokollet erbjuder ett annat tillvägagångssätt. Till skillnad från sin föregångare tillåter Stratum V2 miners att välja vilka transaktioner som ska ingå i de block de minar. Denna möjlighet stärker motståndet mot censur och minskar förmågan hos stora Mining-pooler att dominera nätverket. Genom att ge mer makt till enskilda gruvarbetare kan Stratum V2-protokollet spela en avgörande roll i kampen mot Hashrate-centraliseringen.

Open-Sourcing av Mining-programvara


- Open-sourcing Mining programvara: Detta är en annan potentiellt effektiv strategi. Genom att göra Mining-programvara tillgänglig för alla skulle små gruvbrytare ha samma möjligheter som stora Mining-företag att delta och bidra till Blockchain-nätverket. Detta tillvägagångssätt skulle uppmuntra till en bredare distribution av Hashrate och därmed bidra till decentralisering av nätverket.
- Diversifiering av aktörer och geografi: Att uppmuntra deltagande av olika aktörer från olika geografiska regioner i kryptovalutan Mining kan också visa sig vara effektivt. Genom att diversifiera Hashrate geografiskt blir det svårare för en enskild aktör eller ett land att utöva oproportionerlig kontroll eller inflytande över nätverket. Detta tillvägagångssätt kan bidra till att skydda nätverket mot potentiella attacker och stärka dess decentralisering.


Den allmänna slutsatsen är att decentralisering är avgörande för säkerheten och motståndskraften i Bitcoin-nätverket. Även om centralisering kan erbjuda effektivitetsfördelar utsätter det nätverket för betydande risker, inklusive censur och 51%-attacker. Initiativ som Takai och antagandet av nya protokoll som Stratum V2 är viktiga steg mot decentralisering och skydd av Bitcoin-nätverket mot dessa hot.


## Nyanser av Mining-industrin


<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>


### Principen om Attakai


I det nuvarande sammanhanget kan Bitcoin Mining med S9-modellen verka komplicerad, men en djupare analys öppnar dörren till innovativa alternativ. Attakai-principen bygger på att man överväger att använda Mining-installationer i olika typer av byggnader, t.ex. skolor eller sjukhus. Huvudidén är att placera några Mining-maskiner på olika platser och på så sätt återanvända den värme som avges från dessa maskiner för att värma upp anläggningarna. Genom att välja mer effektiva modeller som S19 skulle det vara möjligt att distribuera Mining-aktivitet och därigenom förbättra den övergripande prestandan samtidigt som man bidrar till samhället på ett användbart sätt. Detta initiativ syftar till att konkurrera med stora centraliserade Mining-verksamheter genom att använda värmen som genereras av Mining-maskiner på ett produktivt och effektivt sätt.


Attakai-initiativet har sitt ursprung i ett personligt Mining-experiment i hemmet som genomfördes av två vänner som var angelägna om att aktivt delta i Bitcoin-nätverket. De stötte på stora hinder, bland annat de höga ljudnivåerna i Mining-utrustningen, som är utformad för industriellt bruk snarare än för hemmabruk. För att Address lösa detta problem gjordes hårdvarumodifieringar på Mining-maskinerna. Effektivare och tystare fläktar ersatte originalutrustningen, vilket gjorde Mining mer tillgänglig och mindre störande i hemmet. Dessutom eliminerade en Wi-Fi-adapter behovet av en trådbunden Ethernet-anslutning, vilket ytterligare förenklade hem-Mining-processen. På vintern användes dessa modifierade gruvarbetare som värmekälla, vilket gjorde att en olägenhet förvandlades till en fördel.


Efter att ha presenterat sitt projekt för Bitcoin-communityn och sett det intresse det genererade, beslutade uppfinnarna av Attakai att publicera detaljerade guider på Découvre Bitcoin-plattformen, så att vem som helst kan replikera sin hem-Mining-upplevelse. De planerar nu att utvidga detta koncept bortom den inhemska miljön. Målet är att visa hur en modifierad Miner kan omvandlas till en tyst extravärmare som kan användas under vintern, vilket ger en smidig övergång till en andra del av utbildningen, som fokuserar på det praktiska genomförandet av dessa modifieringar, illustrerat med förklarande videor. Frågan kvarstår dock om detta initiativ kan utvidgas i större skala och erbjuda ett realistiskt och hållbart alternativ till nuvarande centraliserade Mining-strukturer.


![image](assets/en/07.webp)


### Gränsen för denna decentralisering?


Även om idén att decentralisera Mining genom produktiv användning av genererad värme verkar lovande, har den vissa begränsningar och frågor kvarstår. Energiintensiva anläggningar som bastur och pooler kan dra nytta av detta koncept genom att använda den värme som produceras av gruvarbetare för att värma upp vattnet i sina anläggningar. Denna praxis implementeras redan av vissa medlemmar i Bitcoin-communityn, som utforskar olika metoder för att effektivt utnyttja den värme som genereras av Mining-utrustning. Till exempel skulle en bankettsal teoretiskt kunna värmas upp av tre eller fyra S19-gruvarbetare, som var och en förbrukar 3000 watt och producerar en motsvarande mängd värme.


Det bör dock noteras att energiförbrukning och värmeproduktion är likvärdiga, oavsett om energin används av en elvärmare eller en Miner. För varje kilowatt el som används kommer mängden värme som produceras att vara densamma i båda fallen. Skillnaden ligger i det faktum att Miner inte bara ger värme utan också en Bitcoin-belöning, vilket ger ett ekonomiskt incitament att använda en Miner istället för en enkel elvärmare. Denna extra belöning kan bidra till att minska oron för gruvarbetarnas höga energiförbrukning.


Frågan om den långsiktiga effektiviteten och genomförbarheten av att använda Bitcoin-mineraler för uppvärmning är fortfarande öppen. Pågående innovationer inom Mining-hårdvara och uppvärmningsteknik kan potentiellt öppna nya vägar för effektivare användning av den värme som genereras av Mining, och därmed bidra till att denna metod blir genomförbar i framtiden.


### Varför har BTC-belöningar?


Frågan om att belöna i Bitcoin snarare än en annan valuta är väsentlig i det system som Satoshi Nakamoto föreställer sig. Skapandet av Bitcoin kännetecknas av ett fast tak på 21 miljoner enheter. Målet var att hitta ett rättvist sätt att fördela dessa nyskapade enheter. Genom att tillhandahålla sin datorkraft för att säkra nätverket och göra varje attack alltmer kostsam skyddar miners effektivt Bitcoin-nätverket. I gengäld för detta viktiga bidrag belönas de med nyskapade bitcoins, vilket underlättar distributionen av mynt inom ekosystemet.


Det är ett vinn-vinn-system. Miners belönas både för att säkra nätverket och för att godkänna transaktioner. De nyskapade bitcoins ges som ett incitament för att stärka säkerheten, och transaktionsavgifter är en extra inkomst för att godkänna transaktioner. Dessa två Elements utgör tillsammans den totala belöningen för Mining. Frågan om framtiden för Mining uppstår på grund av den programmerade minskningen av Mining-belöningar, Halving vart fjärde år, en händelse som kallas "Halving". År 2032 kommer Block reward att vara mindre än en Bitcoin, och år 2140 kommer inga nya bitcoins att skapas. Vid denna tidpunkt kommer miners att förlita sig enbart på transaktionsavgifter för kompensation. Bitcoin-nätverket kommer att behöva stödja ett stort antal transaktioner, med tillräckligt höga avgifter, för att säkerställa Mining-lönsamhet.


Ökningen av Lightning Network, som möjliggör snabba och billiga transaktioner utanför den huvudsakliga Bitcoin-kedjan, väcker frågor om framtiden för Mining. Lightning Network har potential att avsevärt minska transaktionsavgifterna och därmed påverka miners inkomster. Detta kommer dock att bero på antagandet och användningen av Lightning Network jämfört med det huvudsakliga Bitcoin-nätverket. I ett pessimistiskt scenario kan gruvarbetare finna det lönsamt att bedriva gruvdrift även med förlust om de har amorterat sina kostnader och har tillgång till billig el. I ett mer optimistiskt scenario kan transaktionsavgifterna i huvudnätverket Bitcoin förbli tillräckligt höga för att upprätthålla lönsamheten i Mining.


### Vad ska ingå i ett Bitcoin-block?


När det gäller frågan om vad som bör ingå i ett Bitcoin-block är det viktigt att beakta den kompletterande karaktären hos de olika lagren i Bitcoin-nätverket. Även om Lightning Network kan möjliggöra snabbare och billigare transaktioner är den fortfarande beroende av Bitcoin:s bas Layer, ofta kallad "avvecklings-Layer", för att öppna och stänga betalningskanaler.


Med den förväntade tillväxten av Lightning Network och den därmed följande ökningen av kanalöppningar och -stängningar kommer utrymme i Bitcoin-block att bli alltmer värdefullt. Bitcoin-communityn tenderar redan att värdesätta bevarandet av detta utrymme och erkänner dess inneboende begränsning. Denna medvetenhet har lett till diskussioner om den legitima användningen av blockutrymme, med oro för "spam" på Blockchain från transaktioner som anses vara icke-essentiella.


![image](assets/en/08.webp)


Spekulationer omger den framtida användningen av blockutrymme, men det är allmänt accepterat att det är en knapp resurs som bör användas klokt. Även om det finns en önskan att fylla det, är det viktigt att bevara det för att säkerställa den långsiktiga livskraften i Bitcoin-nätverket och förutse en framtida ökning av efterfrågan på blockutrymme. Som på alla fria marknader kommer Supply och efterfrågan att reglera användningen av blockutrymme. Med begränsad Supply kommer intressenterna att behöva göra välgrundade val om användningen av detta värdefulla utrymme för att säkerställa den långsiktiga effektiviteten och säkerheten i Bitcoin-nätverket.


## Bitcoin Mining i Bitcoin-protokollet


<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>


Miners roll i Bitcoin-nätverket har varit föremål för intensiv debatt under blockstorlekskriget. Även om de är viktiga för nätverkets säkerhet och funktionalitet har miners inte nödvändigtvis den yttersta makten i Bitcoin:s ekosystem. Balansen mellan miners, noder och slutanvändare säkerställer nätverkets integritet och distribution.


### Kriget om blockstorleken


Under blockstorlekskrigen var många miners emot vissa utvecklingar i nätverket, vilket belyser spänningen mellan olika aktörer i ekosystemet. Frågan kvarstår om hur man ska balansera makten mellan miners, noder och användare för att säkerställa den långsiktiga säkerheten för Bitcoin.


![image](assets/en/09.webp)


Bitcoin:s säkerhetsdilemma vilar på en känslig balans. Medan miners spelar en avgörande roll för att validera och skapa block, upprätthåller noderna integriteten genom att verifiera och validera transaktioner och block. Ett felaktigt eller bedrägligt block kommer att avvisas av noderna, vilket censurerar Miner och bevarar nätverkets säkerhet. Makt innehas också av noderna och användarna av Bitcoin-nätverket. Noderna har makten att verifiera och validera, medan användarna har makten att välja vilken Blockchain som ska användas. Denna maktfördelning säkerställer distributionen och integriteten i Bitcoin-nätverket.


Blockstorlekskrigen avslöjade den osäkerhet och spänning som finns i hanteringen av Bitcoin-nätverket. Även om Bitcoin Core för närvarande är den dominerande kedjan fortsätter debatten om styrning och nätverkshantering.


I slutändan delas ansvaret mellan alla aktörer i Bitcoin-nätverket. En minskning av antalet användare, noder eller miners kan försvaga nätverket, vilket ökar risken för centralisering och sårbarheten för attacker. Varje aktör bidrar till nätverkets robusthet och säkerhet, vilket förstärker vikten av att upprätthålla en balans mellan makt och ansvar.


### Gruvarbetarnas makt


Satoshi Nakamotos eleganta spelteori skapade en situation där varje aktör i Bitcoin-nätverket har incitament att agera korrekt för att skydda både sina egna och andra deltagares intressen. Detta skapar en balans där dåligt beteende kan bestraffas, vilket ökar säkerheten och stabiliteten i hela systemet. Trots denna balans utgör stater fortfarande ett potentiellt hot. Som framgår av presentationen på Surfing Bitcoin 2022 kan stater försöka attackera Mining-industrin, vilket utsätter Bitcoin-nätverket för risker för centralisering och attack. Hypotetiska scenarier som en militär attack riktad mot produktionsanläggningar för Mining-hårdvara belyser vikten av geografisk och industriell diversifiering för Bitcoin-nätverkets motståndskraft.


![image](assets/en/10.webp)


Centraliseringen av produktionen av Mining-hårdvara i Kina utgör en annan risk. En vägran att exportera Mining-maskiner eller en ackumulering av Hashrate för en potentiell 51%-attack från Kina understryker behovet av diversifierad Mining-hårdvaruproduktion. Som svar på dessa risker utforskar Bitcoin-communityn aktivt lösningar. Företag som Intel överväger att producera Mining-utrustning i USA, vilket bidrar till att fördela produktionen. Andra initiativ, som Blocks Mining Development Kit (MDK) med öppen källkod, syftar till att minska monopolet på design och produktion av Mining-hårdvara, vilket möjliggör en bredare distribution av Hashrate. I hjärtat av dessa diskussioner ligger Bitcoin:s grundläggande uppdrag: att vara ett censurresistent värde Exchange-nätverk. Bitcoin-communityn strävar ständigt efter att stärka distributionen, motståndet mot censur och nätverkets antifragilitet, och avvisar förslag som övergången till proof of stake, som inte överensstämmer med dessa grundläggande principer.


### Den fysiska länken till Proof of Work vs Proof of Stake


Proof of Work (PoW) är väsentlig eftersom den utgör den fysiska länken mellan den verkliga världen och Bitcoin. Även om bitcoins är immateriella kräver deras produktion konkret energi, vilket skapar en direkt koppling till den fysiska och verkliga världen. Denna koppling säkerställer att produktionen och valideringen av bitcoins och block har en verklig energikostnad, vilket därmed förankrar Bitcoin-nätverket i den fysiska verkligheten och förhindrar att det helt domineras av mäktiga enheter. PoW fungerar som ett bålverk mot centralisering och säkerställer att deltagande i nätverket och validering av transaktioner kräver en investering i materiella resurser. Detta förhindrar monopolisering av nätverket av enheter som annars skulle kunna ta kontroll utan någon betydande inträdesbarriär, vilket säkerställer en mer rättvis fördelning av makt och inflytande inom Bitcoin-nätverket.


![image](assets/en/11.webp)


### Begränsningarna av Proof of Stake


Å andra sidan garanterar inte Proof of Stake (PoS), även om det möjliggör småskaligt deltagande, ett likvärdigt skydd mot centralisering. I ett PoS-nätverk har de som redan innehar en stor del av valutan oproportionerligt stor makt, vilket återspeglar den befintliga maktojämlikheten i samhället i stort. Denna dynamik skulle potentiellt kunna föreviga centralisering och maktkoncentration i händerna på ett fåtal, i strid med de grundläggande distributionsmålen för Bitcoin-nätverket. Argumentet att alla kan delta i PoS, även i liten skala, genom att gå med i pooler, är inte nödvändigtvis robust. I ett PoW-nätverk kan även en liten bidragsgivare, med blygsam utrustning, aktivt delta och bidra till nätverkets säkerhet och distribution.


### Sammanfattning


Sammanfattningsvis stärker gruvarbetare Bitcoin-nätverket mot censur genom att använda elektricitet för att beräkna Bitcoin:s Proof of Work, och belönas med nya bitcoins och transaktionsavgifter. I takt med att branschen professionaliseras dyker det upp olika aktörer som spelar olika roller, från chipskapande till hantering av Mining-farmer. Dessutom spelar finans också en roll och utövar kontroll genom att bestämma vem som överlever under olika marknadsfaser. Frågan om centralisering kvarstår, med de rikaste enheterna som potentiellt kan dominera marknaden. Alternativ håller dock på att utvecklas både på hårdvaru- och mjukvarunivå. Det är upp till varje individ att agera och bidra till distributionen av nätverket. Bitcoin utgör en extraordinär möjlighet, inte bara när det gäller frihet utan även energioberoende. Trots kontroverser kring dess elförbrukning erbjuder Bitcoin ett ekonomiskt incitament för en övergång till en mer rationell och riklig användning av energi, vilket förverkligar det som tidigare var ett ekologiskt ideal.


## Bitcoin Pris och Hashrate, en korrelation?


<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>


### Hashrate, pris och lönsamhet


Den nuvarande Hash-kursen, trots att Bitcoin:s pris ligger på 30 000 USD jämfört med den tidigare toppen på 69 000 USD, belyser den konkreta kopplingen mellan Mining och den verkliga världen. Tjurmarknadsperioder leder till en hög efterfrågan på Bitcoin Mining och en ökning av maskinorder från tillverkare som Avalon och Bitmain. Produktion och leverans är dock inte omedelbara, vilket skapar en obalans mellan ökad efterfrågan och senare tillgänglighet. Detta kan leda till att maskiner som beställs under en uppåtgående marknad levereras under en nedåtgående marknad, vilket belyser en anmärkningsvärd asymmetri mellan ett lågt pris och en hög Hash-frekvens.


Denna situation illustrerar också motståndskraften hos Bitcoin, som ofta bedöms baserat på dess pris. En djupare analys av Bitcoin:s hälsa kräver dock att man undersöker dess Hash-hastighet, som mäter beräkningarna per sekund i Bitcoin-nätverket. Medan priset på Bitcoin fluktuerar är dess kostnad, kopplad till den elektricitet som krävs för att driva Mining-maskiner, fortfarande avgörande för att förstå marknadsdynamiken. Genom att fokusera på kostnaden snarare än priset får man ett mer konsekvent perspektiv på Bitcoin:s stabilitet och långsiktiga lönsamhet. Generellt sett är kostnaden för Bitcoin proportionell mot priset, vilket ger en bättre förståelse för prisfluktuationer och framtida utsikter.


![image](assets/en/12.webp)


### Hash ränta och belöning


Mining kan utgöra ett golvpris för Bitcoin, under vilket gruvarbetarna skulle sälja med förlust. Kostnaden för Mining påverkar priset avsevärt, vilket illustreras av förbudet mot Mining i Kina, där Hash-raten och priset sjönk avsevärt men snabbt återhämtade sig. Att enbart fokusera på priset kan vara missvisande. Att studera kostnaden, via lönsamhetskalkylatorer, ger ett mer balanserat perspektiv. Marknaden kan dock bete sig irrationellt och gruvarbetare kan tvingas sälja med förlust, vilket kan sänka priset till under Mining-kostnaden. För att bedöma Bitcoin:s hälsa och dess decentralisering skulle en ekvation som innehåller olika faktorer, såsom antalet noder och priset, kunna utvecklas. Detta tillvägagångssätt skulle kunna ge en mer nyanserad analys av Bitcoin jämfört med diskussioner som enbart baseras på pris.


### Mining för vinst eller för nätverket?


Frågan är djupgående och omfattar flera dimensioner av Bitcoin Mining. Balansen mellan att söka vinst och att bidra till säkerheten och distributionen av Bitcoin-nätverket är ett ständigt dilemma för miners. Debatten fortsätter i Bitcoin-communityn, med starka argument på varje sida.



- Mining för vinst:



- För: Gruvarbetare attraheras naturligtvis av de potentiella intäkterna från Bitcoin Mining. Att investera i dyr Mining-utrustning kan kompenseras av Mining-belöningar och transaktionsavgifter, särskilt när priset på Bitcoin är högt.
- Mot: Strävan efter vinst kan leda till en centralisering av hashkraften om endast ett fåtal stora företag har råd att investera i avancerad Mining-utrustning. Dessutom kan Mining i vinstsyfte ha en betydande miljöpåverkan.



- Mining för nätverket:



- För: Mining att bidra till säkerheten och decentraliseringen av Bitcoin-nätverket är ett ädelt initiativ. Det hjälper till att stärka nätverkets motståndskraft och motstå censur och attacker.
- Mot: Utan tillräckliga ekonomiska incitament kan det vara svårt för gruvarbetare att fortsätta stödja nätverket, särskilt om de går med förlust.


Attakai-initiativet belyser vikten av att bidra till nätverket samtidigt som det erbjuder lösningar för att göra Mining mer tillgängligt och mindre skadligt. Möjligheten att göra Mining hemma, med mer prisvärd utrustning och lösningar för att minska buller, kan bidra till att demokratisera Bitcoin Mining. Det uppmuntrar de som är intresserade av Bitcoin att inte bara investera och inneha bitcoins utan också att aktivt delta i att säkra nätverket. Genom att tillhandahålla testad utrustning och guider för montering och installation gör Attakai det lättare att komma in i Bitcoin Mining-världen. Det uppmuntrar också innovation och kontinuerliga förbättringar, och bjuder in samhället att bidra och dela med sig av sina idéer och erfarenheter för att förbättra hemmets Mining. Attakai-modellen är ett svar på frågan om Mining för vinst eller för nätverket. Det handlar inte bara om att göra vinst, utan också om att stärka distributionen och säkerheten i Bitcoin-nätverket, samtidigt som fler människor kan delta i Mining, lära sig och förstå denna viktiga bransch. Utmaningen med ett potentiellt Mining-förbud i Europa är fortfarande en öppen fråga. Detta väcker oro för framtiden för Bitcoin Mining i regionen och behovet av en balanserad reglering som erkänner vikten av Mining för säkerheten och livskraften i Bitcoin-nätverket samtidigt som miljöfrågor hanteras. Attakai och andra liknande initiativ kan spela en avgörande roll i denna debatt och visa att det är möjligt att bedriva gruvdrift på ett mer hållbart och ansvarsfullt sätt, samtidigt som man bidrar positivt till Bitcoin-nätverket.


## Suveränitet och reglering


<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>


### Suveränitet före vinst?


För att Address den viktiga frågan om rikedom genom Mining är det viktigt att beakta olika perspektiv och tillvägagångssätt. Frågor om lönsamheten för Mining är vanliga, med förfrågningar kring köp av aktier i företag som Riot eller leasing av Mining-maskiner i länder med låga energikostnader som Island eller Ryssland. Innan man ger sig in i Mining är det viktigt att jämföra lönsamheten för Mining med ett direkt köp av Bitcoin. Om kostnaden för Mining för en Bitcoin överstiger kostnaden för att köpa den direkt, är det i allmänhet klokare att köpa Bitcoin direkt. På så sätt undviker man de många utmaningar och kostnader som är förknippade med Mining-processen.


Mining erbjuder dock unika möjligheter att engagera sig i Bitcoin-ekosystemet. Till exempel kan Mining Bitcoin på vintern vara ett smart sätt att värma upp ditt hem samtidigt som du genererar Bitcoin-intäkter. Ett annat alternativ är att investera i företag som säljer Mining-utrustning och lagrar och hanterar maskinerna på platser med låga energikostnader, vilket ger tillgång till gynnsamma elpriser utan besväret med att hantera utrustningen.


Trots dessa alternativ presenterar Mining betydande utmaningar. Det välkända ordspråket i kryptovalutornas värld, "Inte dina nycklar, inte dina Bitcoins", finner en liknande resonans i Mining:s värld: "Inte din Hashrate, inte din belöning." Berättelser om besvikelser och frånkopplade maskiner är vanliga, och många spelare lovar exceptionella resultat men misslyckas med att leverera. Problem med el Supply och maskinhaverier kan göra investerare maktlösa, med dyr utrustning som de inte kontrollerar. I detta sammanhang är försiktighet och en djup förståelse för Mining-sektorn avgörande innan man ger sig in i den. Även om det finns möjligheter till vinster är riskerna betydande, och ett informerat och genomtänkt tillvägagångssätt är avgörande för att navigera i detta komplexa och ofta oförutsägbara område. Det är därför viktigt att genomföra grundlig forskning och noggrant väga för- och nackdelar innan man engagerar sig i Bitcoin Mining.


![image](assets/en/13.webp)


### Virgin Bitcoins


Ambitionen att äga sin egen Hashrate framstår som en lovande väg i Mining:s värld. Att navigera i detta komplexa ekosystem kräver dock ett försiktigt tillvägagångssätt. Området för moln Mining präglas av ett stort antal bedrägerier, som drivs av en brist på förståelse för Mining från många investerare. Attraktiva erbjudanden, paketerade på olika sätt, kan lätt vilseleda dem som inte är tillräckligt informerade. Å andra sidan erbjuder det betydande fördelar att äga din egen Mining-utrustning. Förutom den personliga tillfredsställelsen av att aktivt bidra till säkerheten i Bitcoin-nätverket och se belöningar falla in i din Wallet, finns det den tilltalande aspekten av "jungfruliga bitcoins" Dessa är nyligen utvunna bitcoins, som aldrig har spenderats och inte har någon historia kopplad till dem. Dessa bitcoins anses ofta vara mer värdefulla eftersom de aldrig har "fläckats", vilket ger en viss garanti mot avslag från tillsynsmyndigheter eller större Exchange-plattformar.


Möjligheten att Mining virgin bitcoins samtidigt som man undviker Know Your Customer (KYC) -förfaranden är ett annat mervärde. Många Mining-pooler kräver inte gruvarbetarnas identitet, vilket gör det möjligt att förvärva bitcoins utan att genomgå tråkiga identitetskontroller. Virgin bitcoins uppfattas som "rena" och har ingen tidigare historia eller koppling. De är särskilt eftertraktade av stora institutionella aktörer som kan garantera legitimiteten för sina digitala tillgångar inför tillsynsmyndigheter. Trots dessa fördelar är det dock viktigt att inse att Mining-industrin fortfarande är extremt konkurrenskraftig och volatil, och oförutsedda incidenter kan störa Mining-verksamheten.


I detta sammanhang verkar det klokt att välja ett autonomt och utbildat tillvägagångssätt för Mining. Att förvärva sin egen Hashrate och investera i personlig Mining-utrustning, samtidigt som man är medveten om riskerna och utmaningarna, kan potentiellt erbjuda en säkrare och mer tillfredsställande väg till att förvärva jungfruliga bitcoins, vilket förbättrar individens ekonomiska suveränitet samtidigt som det stöder Bitcoin-ekosystemet som helhet.


### Är Mining förbjudet i Europa?


I och med frågan om ett eventuellt förbud mot Mining i Europa blir diskussioner om regleringar alltmer relevanta. Det fluktuerande regleringslandskapet kan verkligen påverka Bitcoin Mining-industrin avsevärt. Förbudet mot Mining i Europa är ett tänkbart scenario, särskilt med tanke på tidigare exempel i Kina. Även om Mining-verksamheten fortsätter i Kina trots förbudet, skulle Europa kunna följa en liknande väg. En bredare distribution av Hashrate över olika regioner skulle kunna bidra till att stärka Mining-samhället i Europa, så att de effektivt kan motverka missförstånd och missuppfattningar om Mining, dess miljöpåverkan och dess fotavtryck på elnätet.


![image](assets/en/14.webp)


Inför kampanjer som Greenpeaces och de ofta missvisande siffrorna från vissa studier är sanningsenlig information fortfarande det bästa vapnet. Det är viktigt att informera allmänheten och beslutsfattarna om verkligheten bakom Mining, dess komplexitet och nyanser, i stället för att låta dem förlita sig på stereotyper och felaktig information. Ju fler människor som är informerade och medvetna om vad Mining verkligen är, desto bättre kan branschen försvara sig mot potentiella restriktiva regleringar.


Sammanfattningsvis, trots den regulatoriska risken och möjligheten till ett förbud mot Mining i Europa, är det mest kraftfulla vapnet fortfarande utbildning och information. En tydlig och exakt förståelse av Mining, hur det fungerar och dess påverkan kan bidra till att avmystifiera branschen och bekämpa felaktig information, och därmed ge bättre motståndskraft mot potentiellt skadliga regleringar. Initiativet att utbilda och informera människor om Mining, som den här diskussionen gör, är ett steg i rätt riktning för att säkerställa hållbarheten och tillväxten för Mining i Europa och runt om i världen. Kontinuerliga insatser för att utbilda och informera är avgörande för att säkerställa en säker och välmående framtid för Bitcoin Mining-industrin.


# Hem Mining och återanvändning av värme


<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>


## Attakai - Gör hem Mining möjligt och tillgängligt!


<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>


Attakai, som betyder "den idealiska temperaturen" på japanska, är namnet på initiativet som syftar till att upptäcka Bitcoin Mining genom värmeåteranvändning som lanserades av @ajelexBTC och @jimzap21 med Découvre Bitcoin.

Denna eftermonteringsguide för ASIC kommer att fungera som en grund för att lära sig mer om Mining, dess drift och den underliggande ekonomin genom att visa möjligheten att anpassa en Bitcoin Miner för användning som radiatorer i hem. Detta ger mer komfort och besparingar, vilket gör att deltagarna kan få tillbaka icke-KYC BTC-kontanter på sin elvärmeräkning.


Bitcoin justerar automatiskt Mining-svårigheten och belönar miners för deras deltagande. Koncentrationen av Hashrate kan dock utgöra en risk för nätverkets neutralitet. Att använda Bitcoin:s datorkraft för uppvärmningslösningar gynnar direkt själva nätverket genom att öka fördelningen av datorkraft.


### Varför återanvända värmen från en ASIC?


Det är viktigt att förstå sambandet mellan energi och värmeproduktion i ett elsystem.


För en investering på 1 kW elenergi producerar en elradiator 1 kW värme, varken mer eller mindre. Nya radiatorer är inte mer effektiva än traditionella radiatorer. Deras fördel ligger i deras förmåga att kontinuerligt och jämnt fördela värmen i ett rum, vilket ger mer komfort jämfört med traditionella radiatorer som växlar mellan hög värmeeffekt och ingen värme, vilket genererar regelbundna temperaturvariationer och obehag.


En dator, eller mer allmänt ett elektroniskt kort, förbrukar inte energi för att utföra beräkningar, den behöver helt enkelt energi för att flöda genom sina komponenter för att fungera. Energiförbrukningen beror på komponenternas elektriska motstånd, som ger upphov till förluster och genererar värme, den så kallade Joules effekt.


Vissa företag har kommit på idén att kombinera behovet av datorkraft med behovet av värme genom radiatorer/servrar. Tanken är att distribuera ett företags servrar till små enheter som kan placeras ut i hemmen eller på kontoren. Denna idé står dock inför flera problem. Behovet av servrar är inte relaterat till behovet av uppvärmning och företagen kan inte använda datorkapaciteten i sina servrar på ett flexibelt sätt. Det finns också gränser för den bandbredd som enskilda personer kan ha. Alla dessa begränsningar hindrar företaget från att göra dessa dyra installationer lönsamma eller tillhandahålla ett stabilt serverutbud online utan datacenter som kan ta över när uppvärmningen inte behövs.


> Värmen som genereras av din dator är inte bortkastad om du behöver värma upp ditt hem. Om du använder elvärme där du bor, så är värmen från din dator inte bortkastad. Det kostar lika mycket att generate denna värme med din dator. Om du har ett billigare värmesystem än elvärme är det bara kostnadsskillnaden som är slöseri. Om det är sommar och du använder luftkonditionering, då är det dubbelt så mycket slöseri. Bitcoin Mining bör äga rum där det är billigare. Kanske blir det där klimatet är Cold och där uppvärmningen är elektrisk, där Mining blir gratis.
>

> Satoshi Nakamoto - 8 augusti 2010

Bitcoin och dess Proof of Work sticker ut eftersom de automatiskt justerar Mining-svårigheten baserat på mängden beräkningar som utförs av hela nätverket. Denna mängd kallas Hashrate och uttrycks i hashes per sekund. Idag uppskattas den till 380 exahashes per sekund, vilket är 380 miljarder miljarder hashes per sekund. Denna Hashrate representerar arbete och därmed en mängd förbrukad energi. Ju högre Hashrate, desto högre svårighetsgrad och vice versa. En Bitcoin Miner kan således aktiveras eller avaktiveras när som helst utan att nätverket påverkas, till skillnad från radiatorer/servrar som måste vara stabila för att kunna tillhandahålla sin tjänst. Miner belönas för sitt deltagande, i förhållande till andra, oavsett hur litet det kan vara.


Sammanfattningsvis producerar en elektrisk radiator och en Bitcoin Miner båda 1 kW värme för 1 kW el som förbrukas. Miner får dock även bitcoins som belöning. Oavsett elpriset, priset på Bitcoin eller konkurrensen inom Bitcoin Mining-aktivitet i nätverket är det ekonomiskt mer fördelaktigt att värma med en Miner än med en elradiator.


### Mervärdet för Bitcoin


Det som är viktigt att förstå är hur Mining bidrar till decentraliseringen av Bitcoin.

Flera befintliga tekniker har kombinerats på ett genialt sätt för att ge liv åt Nakamotos konsensus. Detta samförstånd belönar ärliga deltagare ekonomiskt för deras bidrag till driften av Bitcoin-nätverket, samtidigt som det avskräcker oärliga deltagare. Detta är en av de viktigaste punkterna som gör att nätverket kan existera på ett hållbart sätt.

De hederliga aktörerna, de som bedriver gruvdrift enligt reglerna, konkurrerar alla med varandra om att få största möjliga andel av belöningen för att producera nya block. Detta ekonomiska incitament leder naturligt till en form av centralisering eftersom företag väljer att specialisera sig på denna lukrativa verksamhet genom att minska sina kostnader genom stordriftsfördelar. Dessa industriella aktörer har en fördelaktig position när det gäller inköp och underhåll av maskiner samt förhandlingar om elpriser på grossistnivå.


> Till en början skulle de flesta användare köra nätverksnoder, men när nätverket växer över en viss punkt skulle det lämnas mer och mer till specialister med serverhallar med specialiserad hårdvara. En serverfarm behöver bara ha en nod i nätverket och resten av det lokala nätverket ansluts till den noden.
>

> Satoshi Nakamoto - 2 november 2008

Vissa enheter innehar en betydande andel av den totala Hashrate i stora Mining-farmer. Vi kan observera den senaste Cold-vågen i USA där en betydande del av Hashrate togs offline för att omdirigera energi till hushåll med ett exceptionellt behov av elektricitet. Under flera dagar fick gruvarbetare ekonomiska incitament att stänga ned sina gårdar, och detta exceptionella väder kan ses på Bitcoin Hashrate-kurvan.


Denna fråga kan bli problematisk och utgör en betydande risk för nätverkets neutralitet. En aktör med mer än 51% av Hashrate skulle lättare kunna censurera transaktioner om de så önskade. Det är därför det är viktigt att fördela Hashrate mellan flera aktörer snarare än centraliserade enheter som lättare kan beslagtas av till exempel en regering.


**Om miners är fördelade på tusentals, eller till och med miljontals, hushåll runt om i världen blir det mycket svårt för en stat att ta kontroll över dem


När den kommer ut från fabriken är en Miner inte lämplig att använda som värmare i ett hem, på grund av två huvudproblem: överdrivet buller och brist på justering. Dessa problem kan dock enkelt lösas genom modifieringar av hård- och mjukvara, vilket ger en mycket tystare Miner som kan konfigureras och automatiseras på samma sätt som moderna elektriska värmare.


**Attakaï är ett utbildningsinitiativ som lär dig hur du kan eftermontera Antminer S9 på det mest kostnadseffektiva sättet


Detta är ett utmärkt tillfälle att lära sig genom att öva samtidigt som du belönas för ditt deltagande med KYC-fria satoshis.


## Köpguide för en begagnad ASIC


<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>


I det här avsnittet kommer vi att diskutera bästa praxis för att köpa en begagnad Bitmain Antminer S9, den maskin som denna handledning för eftermontering av kylare kommer att baseras på. Denna guide gäller även för andra modeller av ASIC eftersom det är en allmän köpguide för begagnad Mining-hårdvara.


Antminer S9 är en enhet som erbjuds av Bitmain sedan maj 2016. Den förbrukar 1400W el och producerar 13,5 TH/s. Även om den anses vara gammal är den fortfarande ett utmärkt alternativ för att starta Mining. Eftersom den har producerats i stora mängder är det lätt att hitta reservdelar i överflöd i många regioner i världen. Den kan i allmänhet förvärvas peer-to-peer på webbplatser som eBay eller LeBonCoin, eftersom professionella återförsäljare inte längre erbjuder den på grund av dess lägre konkurrenskraft jämfört med nyare maskiner. Den är mindre effektiv än ASICs som Antminer S19, som erbjuds sedan mars 2020, men detta gör den till en prisvärd begagnad hårdvara och mer lämplig för de modifieringar vi kommer att göra.


Antminer S9 finns i flera varianter (i, j) som gör mindre ändringar i den första generationens hårdvara. Vi anser inte att detta ska påverka ditt köpbeslut, och den här guiden fungerar för alla dessa varianter.


Priset på ASICs varierar beroende på många faktorer, t.ex. priset på Bitcoin, nätverkets svårighetsgrad, maskinens effektivitet och elkostnaden. Därför är det svårt att ge en exakt uppskattning för inköp av en begagnad maskin. I februari 2023 ligger det förväntade priset i Frankrike i allmänhet mellan 100 och 200 euro, men dessa priser kan ändras snabbt.


![image](assets/en/15.webp)


Antminer S9 är uppbyggd av följande delar:



- 3 hashboards som innehåller de chips som producerar hashkraften.


![image](assets/en/16.webp)



- Ett kontrollkort som innehåller en plats för ett SD-kort, en Ethernet-port och anslutningar för hashkort och fläktar. Detta är hjärnan i din ASIC.


![image](assets/en/17.webp)



- 3 datakablar som ansluter hashplattorna till styrkortet.


![image](assets/en/18.webp)



- Strömförsörjningen Supply, som drivs med 220V och kan anslutas som en vanlig hushållsapparat.


![image](assets/en/19.webp)



- 2 120 mm fläktar.


![image](assets/en/20.webp)



- En C13-hankabel.


![image](assets/en/21.webp)


När du köper en begagnad maskin är det viktigt att kontrollera att alla delar ingår och fungerar. Under Exchange bör du be säljaren att slå på maskinen för att kontrollera att den fungerar korrekt. Det är viktigt att verifiera att enheten slås på korrekt och sedan kontrollera internetanslutningen genom att ansluta en Ethernet-kabel och komma åt Bitmain-inloggningen Interface via en webbläsare på samma lokala nätverk. Du kan hitta denna IP Address genom att ansluta till din internetrouter Interface och leta efter anslutna enheter. Denna Address bör ha följande format: 192.168.x.x


![image](assets/en/22.webp)


Kontrollera också att standardautentiseringsuppgifterna fungerar (användarnamn: root, lösenord: root). Om standardautentiseringsuppgifterna inte fungerar måste du återställa maskinen.


![image](assets/en/23.webp)


När du är ansluten bör du kunna se status för varje hashboard på instrumentpanelen. Om Miner är ansluten till en pool bör du se att alla hashboards fungerar. Det är viktigt att notera att miners gör mycket ljud, vilket är normalt. Se också till att fläktarna fungerar som de ska.


Du kan sedan ta bort den tidigare ägarens Mining pool för att sätta upp din egen senare. Om du vill kan du också inspektera hashborden genom att demontera maskinen. Detta steg är dock mer komplicerat och kräver mer tid och vissa verktyg. Om du vill fortsätta med denna demontering kan du hänvisa till nästa del av denna handledning som beskriver hur du gör det. Det är viktigt att notera att gruvarbetare samlar in mycket Dust och kräver regelbundet underhåll. Du kan observera denna Dust-ackumulering och kvaliteten på underhållet genom att ta isär maskinen.

När du har gått igenom alla dessa punkter kan du köpa din maskin med en hög grad av självförtroende. Om du är osäker, rådgör med samhället.


För att sammanfatta den här guiden i en mening: **"Lita inte på, verifiera."**


[Du kan också vända dig till proffs inom rekonditionering av Mining-maskiner, till exempel vår partner 21energy. De erbjuder testade S9-maskiner, rengjorda och med BraiiinOS+-programvaran redan installerad. Med affiliatekoden "decouvre" får du 10% rabatt på köpet av en S9 samtidigt som du stödjer Attakai-projektet](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)


## Guide för inköp av hårdvarumodifieringar för S9


<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>


Om du äger en Antminer S9 vet du säkert hur högljudd och skrymmande den här utrustningen kan vara. Det är dock möjligt att förvandla den till en tyst och ansluten värmare genom att följa några enkla steg. I detta avsnitt kommer vi att presentera den nödvändiga utrustningen för att göra ändringarna.


Om du är en skicklig hantverkare och vill förvandla en Miner till en värmare är den här handledningen något för dig. Vi vill varna dig för att ändringar som görs på en elektronisk enhet kan medföra elektriska risker. Det är därför viktigt att du vidtar alla nödvändiga försiktighetsåtgärder för att undvika skador eller personskador.


1. Byt ut fläktarna


Originalfläktarna på Antminer S9 är för högljudda för att Antminer ska kunna användas som värmare. Lösningen är att ersätta dem med tystare fläktar. Vårt team har testat flera modeller från varumärket Noctua och har valt Noctua NF-A14 iPPC-2000 PWM som den bästa kompromissen. Var noga med att välja 12V-versionen av fläktarna. Denna 140mm fläkt kan producera upp till 1200W värme samtidigt som den bibehåller en teoretisk ljudnivå på 31 dB. För att installera dessa 140mm-fläktar måste du använda en 140mm till 120mm-adapter, som du hittar i DécouvreBitcoin-butiken. Vi kommer också att lägga till 140 mm skyddsgaller.


![image](assets/en/24.webp)

![image](assets/en/25.webp)

![image](assets/en/26.webp)


Den kraftfulla Supply-fläkten är också ganska bullrig och måste bytas ut. Vi rekommenderar Noctua NF-A6x25 PWM. Observera att kontakterna på Noctua-fläktarna inte är desamma som de ursprungliga, så du behöver en kontaktadapter för att ansluta dem. Två stycken kommer att räcka. Återigen, se till att välja 12V-versionen av fläkten.


![image](assets/en/27.webp)

![image](assets/en/28.webp)


2. Lägg till en WIFI/Ethernet-brygga


Istället för att använda en Ethernet-kabel kan du ansluta din Antminer via WIFI genom att lägga till en WIFI/Ethernet-brygga. Vi har valt vonets vap11g-300 eftersom den enkelt låter dig hämta WIFI-signalen från din Internetbox och överföra den till din Antminer via Ethernet utan att skapa ett subnät. Om du har elektriska färdigheter kan du driva den direkt med Antminers ström Supply utan att behöva lägga till en USB-laddare. För detta behöver du ett 5,5 mmx2,1 mm honjack.


![image](assets/en/29.webp)

![image](assets/en/30.webp)


3. Valfritt: lägg till en smart kontakt


Om du vill slå på/stänga av din Antminer från din smartphone och övervaka dess strömförbrukning kan du lägga till en smart kontakt. Vi testade ANTELA-kontakten i 16A-versionen, som är kompatibel med smartlife-appen. Med den här smarta kontakten kan du se strömförbrukningen per dag och månad och den ansluts direkt till din internetrouter via WiFi.


![image](assets/en/31.webp)


Lista över utrustning och länkar



- 2X 3D-adapterstycke 140mm till 120mm



- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)



- [2X 140 mm fläktgaller](https://www.amazon.fr/dp/B06XD4FTSQ)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)



- [Elektrikerns socker 2,5 mm²](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)
- [ANTELA smart plug (tillval)] (https://www.amazon.fr/dp/B09YYMVXJZ)


# Attakai - Modifiering av programvaran i en Antminer S9


<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>


## Konfigurera en Vonet WIFI/Ethernet-brygga


<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>


För att ansluta din ASIC via WIFI behöver du en enhet som kallas brygga. Med den här enheten kan du hämta WIFI-signalen från din router och överföra den till en annan enhet via Ethernet.


Många enheter kan utföra den här funktionen, men vi rekommenderar VONETS WiFi Bridge/Repeater för dess bekvämlighet.


Strömförsörj bryggan genom att ansluta den via USB.


Från datorn ansluter du till VONETS\_**\*\*** WIFI-nätverk med lösenordet 12345678.


![image](assets/en/32.webp)


Logga in med användarnamnet "admin" och lösenordet "admin".


![image](assets/en/33.webp)


Välj Wizard.


![image](assets/en/34.webp)


Välj det WIFI-nätverk som du vill ansluta din Miner till och klicka sedan på Nästa.


OBS: Vonet-bryggan fungerar endast på 2,4 GHz-frekvensen. Numera erbjuder routrar vanligtvis två WIFI-nätverk, ett på 2,4 GHz och ett på 5 GHz.


![image](assets/en/35.webp)


Ange lösenordet för ditt WIFI-nätverk i fältet "Source WIFI hotspot password". Om du inte vill använda din Vonet-brygga för att utöka ditt WIFI-nätverk markerar du rutan "Disable Hotspot". Annars lämnar du den omarkerad.


Du kan sedan klicka på Apply.


Klicka slutligen på reboot för att starta om bryggan. Det kommer att ta några minuter att starta om.


Bryggan ska ansluta till din router och visas under namnet "[VONETS.COM](http://vonets.com/)". Om den fortfarande inte ansluter efter några minuter kan du behöva koppla ur/till bryggan.


När bryggan är ansluten ansluter du Ethernet-kabeln från bryggan till din ASIC och ansluter sedan ASIC till eluttaget. Du kan sedan komma åt ASIC Interface på samma sätt som om den vore direktansluten till din router via Ethernet.


## Återställning av en Antminer S9


<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>


Innan du installerar BraiinOS+ kan det vara nödvändigt att återställa din S9 till fabriksinställningarna.

Denna metod kan tillämpas mellan 2 minuter och 10 minuter efter att Miner har startats.

2 minuter efter att du har slagit på Miner, tryck på "Reset"-knappen i 5 sekunder och släpp den sedan. Miner återställs till fabriksinställningarna inom 4 minuter och startar om automatiskt (du behöver inte stänga av den).


![image](assets/en/36.webp)


## Installera BraiinsOS+ på en Antminer S9


<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>


Den ursprungliga programvaran som installerades av Antminer på deras Mining-maskiner är begränsad i funktionalitet. Därför kommer vi i den här guiden att installera en annan programvara som heter BraiinsOS+. Det är en tredjepartsprogramvara som utvecklats av den allra första Bitcoin Mining pool som har fler funktioner och gör det till exempel möjligt att ändra maskinens effekt.


Det finns flera sätt att installera Braiins OS+ på en ASIC. Du kan hänvisa till den här guiden samt [den officiella Braiins-dokumentationen] (https://academy.braiins.com/en/braiins-os/about/).


Här kommer vi att se hur du enkelt installerar Braiins OS+ direkt på minnet i din Antminer med hjälp av BOS toolbox-programvaran, som ersätter det ursprungliga operativsystemet, genom de detaljerade stegen nedan.


1. Slå på din Antminer och anslut den till din internetbox.

2. Ladda ner BOS toolbox för Windows / Linux.

3. Packa upp den nedladdade filen och öppna filen bos-toolbox.bat. Välj språk och efter en stund kommer du att se det här fönstret:


![image](assets/en/37.webp)


4. Bos verktygslåda gör att du enkelt kan hitta IP Address för din Antminer och installera BraiinsOS+. Om du redan vet IP Address för din maskin kan du hoppa till steg 8. Annars går du till fliken Skanna.


![image](assets/en/38.webp)


5. I hemmanätverk är IP Address vanligtvis mellan 192.168.1.1 och 192.168.1.255, så ange "192.168.1.0/24" i fältet för IP-intervall. Om ditt nätverk är annorlunda, ändra dessa adresser i enlighet med detta. Klicka sedan på "Start".


6. Observera att om Antminer har ett lösenord kommer detekteringen inte att fungera. Om så är fallet är den enklaste lösningen att utföra en återställning.


7. Du bör se att alla Antminers i ditt nätverk visas här, och IP Address är 192.168.1.37.


![image](assets/en/39.webp)


8. Klicka på "Tillbaka" och sedan på fliken "Installera", ange den tidigare hittade IP Address och klicka på "Start".


> Om installationen inte fungerar kan det vara nödvändigt att göra en återställning och försöka igen (se föregående avsnitt).

![image](assets/en/40.webp)


9. Efter några ögonblick startar din Antminer om och du kommer att kunna komma åt Braiins OS+ Interface på den angivna IP Address, här 192.168.1.37, direkt i Address-fältet i din webbläsare. Standardanvändarnamnet är "root" och det finns inget standardlösenord.


## Konfigurera BraiinsOS+


<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>


Du måste ansluta till din ASIC med hjälp av den lokala IP Address för din enhet i ditt nätverk via en webbläsare.


Du kan hitta IP Address för din maskin med hjälp av BOS toolbox-verktyget eller direkt på routerns webbsida.


Standardautentiseringsuppgifterna är desamma som för det ursprungliga operativsystemet.



- användarnamn: root
- lösenord: (inget)


Du kommer sedan att mötas av Brains OS+ Dashboard.


### Instrumentpanel


![image](assets/en/41.webp)


På den första sidan kan du se hur din maskin presterar i realtid.



- Tre grafer i realtid som visar temperatur, Hashrate och maskinens övergripande status.
- Till höger, den verkliga Hashrate, genomsnittlig chiptemperatur, uppskattad effektivitet i W/THs och strömförbrukning.
- Nedan visas fläkthastigheten i procent av maxhastigheten och antalet rotationer per minut.


![image](assets/en/42.webp)



- Längre ner hittar du en detaljerad bild av varje hashboard. Kortets medeltemperatur och de chips som det innehåller, samt spänning och frekvens.
- Detaljer om de aktiva Mining-poolerna i Pooler.
- Status för autotuning i Tuner Status.
- Till höger, detaljer om de data som överförs till poolen.


### Konfiguration


![image](assets/en/43.webp)


### System


![image](assets/en/44.webp)


### Snabba åtgärder


![image](assets/en/45.webp)


# Attakai - Modifiering av fläkt


<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>


## Byt ut strömförsörjningen Supply Fläkt


<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>


> VARNING: Det är viktigt att du tidigare har installerat Braiins OS+ på din Miner, eller någon annan programvara som kan minska maskinens prestanda. Denna åtgärd är avgörande eftersom vi för att minska bullret kommer att installera mindre kraftfulla fläktar som kan avleda mindre värme.

![image](assets/en/46.webp)


### Nödvändiga material



- 1 Noctua NF-A6x25 PWM-fläkt
- 2.5mm2 elektrikersocker


> VARNING: Innan du börjar ska du först kontrollera att du har dragit ur kontakten till din Miner för att undvika risk för elstötar.

![image](assets/en/47.webp)


Ta först bort de 6 skruvarna på sidan av chassit som håller det stängt. När skruvarna har lossats öppnar du försiktigt höljet för att ta bort plastskyddet som täcker komponenterna.


![image](assets/en/48.webp)

![image](assets/en/49.webp)


Därefter är det dags att ta bort originalfläkten, var försiktig så att du inte skadar de andra komponenterna. För att göra detta, ta bort skruvarna som håller den på plats och skala försiktigt bort det vita limmet som omger kontakten. Det är viktigt att gå försiktigt fram för att undvika att skada ledningarna eller kontakterna.


![image](assets/en/50.webp)


När originalfläkten har tagits bort kommer du att märka att kontakterna på den nya Noctua-fläkten inte matchar originalfläktens. Den nya fläkten har faktiskt 3 ledningar, inklusive en gul ledning som möjliggör hastighetsreglering. Denna ledning kommer dock inte att användas i detta specifika fall. För att ansluta den nya fläkten rekommenderas därför att man använder en speciell adapter. Det är dock viktigt att notera att denna adapter ibland kan vara svår att hitta.


![image](assets/en/51.webp)


Om du inte har denna adapter kan du ändå fortsätta att ansluta den nya fläkten med hjälp av en elektrikers socker. För att göra detta måste du klippa kablarna till den gamla och den nya fläkten.


![image](assets/en/52.webp)

![image](assets/en/53.webp)


På den nya fläkten använder du en avbitartång och skär försiktigt av huvudmantelns konturer på 1 cm utan att skära av kablarnas mantlar undertill.


![image](assets/en/54.webp)


Dra sedan huvudmanteln nedåt och klipp av mantlarna på den röda och svarta kabeln på samma sätt som tidigare. Och klipp av den gula kabeln i jämnhöjd.


![image](assets/en/55.webp)


På den gamla fläkten är det mer känsligt att skära av huvudmanteln utan att skada mantlarna på de röda och svarta ledningarna. För detta ändamål använde vi en nål som vi förde in mellan huvudmanteln och de röda och svarta ledningarna.


![image](assets/en/56.webp)

![image](assets/en/57.webp)


När de röda och svarta ledningarna är frilagda, klipp försiktigt av höljena för att undvika att skada de elektriska ledningarna.


![image](assets/en/58.webp)


Anslut sedan kablarna med ett socker, den svarta ledningen med den svarta och den röda ledningen med den röda. Du kan också lägga till eltejp.


![image](assets/en/59.webp)

![image](assets/en/60.webp)


När anslutningen är klar är det dags att montera den nya Noctua-fläkten med gallret och de gamla skruvarna. De nya skruvarna i lådan kommer att återanvändas senare. Se till att placera den i rätt riktning. Du kommer att märka en pil på ena sidan av fläkten, som anger luftflödets riktning. Det är viktigt att fläkten placeras så att pilen pekar mot insidan av chassit. Anslut sedan fläkten igen.


![image](assets/en/61.webp)

![image](assets/en/62.webp)


> Valfritt: Om du är kunnig inom elektricitet kan du direkt lägga till en 5,5 mm jackkontakt till 12V-utgången, som direkt driver Vonet Wi-Fi-bryggan. Om du är osäker på dina elektriska färdigheter är det dock bäst att använda USB-kontakten med en laddare av smartphonetyp för att undvika risk för kortslutning eller elektriska skador.

![image](assets/en/63.webp)


När anslutningarna är klara ska plastskyddet placeras över höljets plast och inte inuti.


![image](assets/en/64.webp)


Slutligen sätter du tillbaka chassilocket på plats och skruvar fast de 6 skruvarna på sidorna för att hålla allt på plats. Och så har du det, ditt power Supply-chassi är nu utrustat med en ny fläkt.


## Byte av huvudfläktarna


<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>


> VARNING: Det är viktigt att du tidigare har installerat Braiins OS+ på din Miner, eller någon annan programvara som kan minska maskinens prestanda. Denna åtgärd är avgörande eftersom vi för att minska bullret kommer att installera mindre kraftfulla fläktar, som kommer att avleda mindre värme.

![image](assets/en/46.webp)


### Obligatoriska material



- 2 stycken 3D-adapter 140mm till 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM-fläktar
- 2 140 mm fläktgaller


> VARNING: Först av allt, innan du börjar, se till att koppla bort din Miner för att undvika risk för elstöt.

1. Koppla först bort fläktarna och skruva loss dem.


![image](assets/en/65.webp)


2. Anslutningarna på de nya Noctua-fläktarna matchar inte de ursprungliga, men oroa dig inte! Ta fram din avbitartång och klipp försiktigt av de små plastflikarna så att kontakterna passar perfekt på din Miner.


![image](assets/en/66.webp)

![image](assets/en/67.webp)


3. Nu är det dags att installera 3D-delarna!

Fäst dem på båda sidor av Miner med hjälp av skruvarna som du tog bort från fläktarna. Skruva fast dem tills skruvhuvudet är i jämnhöjd med 3D-delen och den sitter ordentligt på plats. Var försiktig så att du inte drar åt för mycket, eftersom du då kan deformera delen och en av skruvarna kan komma i kontakt med en kondensator!


![image](assets/en/68.webp)


4. Låt oss nu gå vidare till fansen.


Fäst dem på 3D-delarna med hjälp av skruvarna som medföljer i lådan. Var uppmärksam på luftflödets riktning, pilarna på sidorna av fläktarna visar vilken riktning du ska följa. Gå från Ethernet-portsidan till den andra sidan. Se bilden nedan.


![image](assets/en/69.webp)

![image](assets/en/70.webp)

![image](assets/en/71.webp)


5. Sista steget: anslut fläktarna och fäst gallren ovanpå med skruvarna som inte användes i Power Supply fläktbox. Du har bara 4 stycken, men det räcker med 2 per galler i motsatta hörn. Du kan också leta efter liknande skruvar i en järnaffär om det behövs.


![image](assets/en/72.webp)

![image](assets/en/73.webp)


I väntan på att kunna erbjuda ett snyggare hölje för din nya värmare kan du fästa höljet och strömmen Supply med elektrikerns buntband.


![image](assets/en/74.webp)


Och som pricken över i:et ansluter du Vonet-bryggan till Ethernet-porten och dess strömförsörjning Supply.


![image](assets/en/75.webp)


Och där har du det, grattis! Du har just bytt ut hela den mekaniska delen av din Miner. Du bör nu höra mycket mindre ljud.


# Attakai - Konfiguration


<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>


## Ansluta till en Mining pool


<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>


Man kan föreställa sig en Mining pool som ett jordbrukskooperativ. Lantbrukare slår samman sin produktion för att minska variansen i Supply och efterfrågan och därmed få en stabilare inkomst för sin verksamhet. En Mining pool fungerar på samma sätt, där den delade resursen är hashes. Upptäckten av en enda giltig Hash gör det möjligt att skapa ett block och vinna coinbase eller belöningen, för närvarande 6,25 BTC plus de transaktionsavgifter som ingår i blocket.


Om du minar ensam kommer du bara att bli belönad när du hittar ett block. Eftersom du konkurrerar med alla andra miners på planeten skulle du ha mycket liten chans att vinna detta lotteri och du skulle fortfarande behöva betala de avgifter som är förknippade med att använda din Miner utan någon garanti för framgång. Mining pooler Address detta problem genom att samla datorkraften hos flera (tusentals) miners och dela deras belöningar baserat på procentandelen av deltagande i poolens Hashrate när ett block hittas. För att visualisera dina chanser att Mining ett block ensam kan du använda det här verktyget. Genom att ange informationen för en Antminer S9 kan vi se att chansen att hitta en Hash som gör det möjligt att skapa ett block är 1 på 24 777 849 för varje block eller 1 på 172 068 per dag. I genomsnitt (med en konstant Hashrate och svårighetsgrad) skulle det ta minst 471 år att hitta ett block (eftersom svårighetsgraden ökar).


Men eftersom allt i Bitcoin är baserat på sannolikhet händer det ibland att solo-gruvarbetare belönas för att de tar denna risk: Solo Bitcoin Miner löser block med Hash-hastighet på bara 10 TH/s och slår extremt osannolika odds - Decrypt


Om du gillar att spela kan du prova det, men vår guide kommer inte att fokusera i den riktningen. Istället kommer vi att koncentrera oss på Mining pool som bäst passar våra behov för att skapa ett värmesystem.


Överväganden att ha när man väljer en Mining pool är driften av poolens belöningar, som kan variera, samt det lägsta beloppet innan man kan ta ut belöningar till en Address. Till exempel erbjuder Braiins, som erbjuder den programvara vi diskuterar här, också en pool. Denna pool har ett belöningssystem som kallas "Score" som uppmuntrar gruvarbetare att bryta under långa perioder. Deltagandet inkluderar en upptidsfaktor uttryckt som en "scoring Hashrate". I vårt fall, där vi vill ha ett värmesystem som bara kan slås på under några minuter, är detta inte det perfekta belöningssystemet. Vi föredrar ett belöningssystem som ger oss en lika stor belöning för varje deltagande. Dessutom är det lägsta uttagsbeloppet för Braiins Pool 100 000 Sats och On-Chain. Så vi förlorar lite Sats i transaktionsavgifter och en del av vår belöning kan låsas om vi inte bryter tillräckligt under vintern.


Den belöningsmodell som intresserar oss är PPS, som står för "pay-per-share". Detta innebär att Miner kommer att få en belöning för varje giltig aktie. Det finns också en variant av detta system, FPPS (Full Pay Per Share), som inte bara delar coinbase-belöningen utan också de transaktionsavgifter som ingår i blocket. De Mining-pooler som vi rekommenderar för att ansluta din Mining/heating är Linecoin Pool (FPPS) och Nicehash (PPS).



- Nicehash: Fördelen med Nicehash är att uttag kan göras med Lightning med minimala avgifter. Dessutom är det minsta uttagsbeloppet 2000 Sats. Nackdelen är att Nicehash använder sin Hashrate för den mest lönsamma Blockchain, utan att verkligen ge kontroll till användaren, så det kanske inte nödvändigtvis bidrar till Bitcoin Hashrate.



- Linecoin: Fördelen med Linecoin är antalet funktioner som erbjuds, till exempel en detaljerad instrumentpanel, möjligheten att göra uttag med en Paynym (BIP 47) för bättre integritetsskydd och integrationen av en Telegram-bot samt direkt konfigurerbara automatiseringar i mobilapplikationen. Denna pool bryter endast Bitcoin-block, men det lägsta beloppet för att ta ut förblir högt på 100 000 Sats. Vi kommer att undersöka Interface i en av dessa pooler mer detaljerat i en framtida artikel.


För att konfigurera en pool i Braiins OS+ måste du skapa ett konto i en av de pooler du väljer. Här kommer vi att ta exemplet Linecoin:


![image](assets/en/76.webp)


När ditt konto har skapats klickar du på Connect To Pool


Kopiera sedan Stratum Address och ditt användarnamn:


![image](assets/en/77.webp)


Du kan nu gå tillbaka till Braiins OS+ Interface för att ange dessa inloggningsuppgifter. För lösenordet kan du lämna fältet tomt.


![image](assets/en/78.webp)


## Optimera prestandan för din Antminer S9


<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>


Både överklockning och autotuning innebär att man justerar frekvenserna på hashingkorten för att förbättra prestandan hos ASIC. Skillnaden mellan de två ligger i komplexiteten i dessa frekvensinställningar.


Överklockning är en enkel justering som innebär att man ökar frekvensen på hashingkorten för att öka maskinens Hash-frekvens. Underklockning, å andra sidan, innebär att man minskar klockfrekvensen för en integrerad krets under dess nominella frekvens. Genom att minska klockfrekvensen på en ASIC genom underklockning minskas också värmen som genereras av hårdvaran. Detta gör det möjligt att minska hastigheten på de fläktar som krävs för att kyla ASIC, eftersom de inte behöver arbeta lika mycket som Hard för att hålla en lämplig temperatur. Genom att minska fläkthastigheten minskas också det buller som ASIC genererar. Detta kan vara särskilt användbart för användare som använder ASICs hemma och vill minimera de bullerstörningar som orsakas av Mining-utrustning.


Braiins OS+ stöder överklockning, underklockning av ASICs och autotuning. Det gör det möjligt för användare att justera klockfrekvensen på sin hårdvara flexibelt för att maximera prestanda eller spara energi enligt deras önskemål.


### Optimera prestandan hos din Antminer S9 med auto-tuning


Före 2018 hade gruvarbetare två sätt att få en fördel i sin verksamhet: att hitta el till en rimlig kostnad och att köpa effektivare hårdvara. Under 2018 upptäcktes dock ett nytt framsteg inom området Mining-programvara och firmware, kallat AsicBoost. Denna teknik gör det möjligt för gruvarbetare att minska sina kostnader med cirka 13% genom att ändra den inbyggda programvaran som körs på deras enheter.


Idag finns det ett nytt framsteg inom mjukvaru- och firmware Mining-sektorn som kallas autotuning, vilket ger en ännu större fördel än AsicBoost. ASICs består av många små datorchips som utför hashing. Dessa chip är tillverkade av kisel, samma element som används i halvledare och andra mikroelektroniska komponenter. Det som är viktigt att förstå här är att alla kiselchip inte är identiska, utan kan variera något i sina elektriska egenskaper. Hårdvarutillverkare är medvetna om detta och publicerar prestandaspecifikationerna för sina Mining-maskiner baserat på den nedre gränsen för deras toleranser. Med andra ord vet tillverkarna vilken frekvens som fungerar bäst för genomsnittliga chip och de använder denna frekvens enhetligt för alla chip i maskinen.


Detta sätter en övre gräns för hur hög Hash-frekvens en maskin kan ha. Autotuning är en process där algoritmer utvärderar de optimala frekvenserna för hashning chip för chip, istället för att behandla hela maskinen som en enda enhet. Det innebär att ett chip av högre kvalitet som kan utföra fler hashningar per sekund får en högre frekvens, och ett chip av lägre kvalitet som kan utföra relativt färre hashningar får en lägre frekvens. Autotuning på chipnivå är i huvudsak ett sätt att optimera prestandan hos en ASIC genom den programvara och fasta programvara som körs på den.


Slutresultatet är en högre Hash-frekvens per watt elektricitet, vilket innebär större vinstmarginaler för gruvbrytarna. Anledningen till att maskiner inte distribueras med denna typ av programvara är att maskinvarians inte är önskvärt, eftersom kunderna vill veta exakt vad de får, så det är en dålig idé för tillverkare att sälja en produkt som inte har konsekvent och förutsägbar prestanda från en maskin till en annan. Dessutom kräver autotuning på chipnivå avsevärda utvecklingsresurser, eftersom det är komplicerat att implementera. Tillverkarna lägger redan mycket resurser på att utveckla sina egna firmware. Det finns mjukvarulösningar som möjliggör autotuning, t.ex. Braiins OS+. Förutom att förbättra ASIC-prestandan med upp till 20%.


# Sista avsnittet


<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>


## Recensioner & betyg


<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>

<isCourseReview>true</isCourseReview>

## Slutlig tentamen


<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>

<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>

<isCourseConclusion>true</isCourseConclusion>