---
name: Attakaï

description: förvandla en S9 till ett uppvärmningssystem för hemmet
---

![cover](assets/cover.webp)


# Attakai - gör Mining i hemmet möjligt och tillgängligt!


Initiativet "Attakaï" utforskar Bitcoin Mining med hjälp av den genererade värmen. Guiden erbjuder lösningar för att göra gruvarbetare lämpliga att använda som radiatorer i hemmen, vilket ger mer komfort och energibesparingar. Bitcoin justerar automatiskt Mining-svårigheten och belönar gruvarbetarna för deras arbete. Koncentrationen av Hashrate kan dock utgöra en risk för nätneutraliteten. "Attakaï" ger en praktisk guide för att eftermontera miners på ett ekonomiskt sätt, så att deltagarna kan minska sina elräkningar och belönas med Sats utan kundkännedom.


## Inledning


"Attakaï", som betyder "idealisk temperatur" på japanska, är namnet på det initiativ som syftar till att upptäcka Bitcoin Mining genom återanvändning av värme som lanserades av @ajelexBTC och @BlobOnChain med Découvre Bitcoin. Denna eftermonteringsguide för ASIC kommer att fungera som en grund för att lära sig mer om Mining, dess drift, senaste historia och den underliggande ekonomin.


### Varför återanvända värmen från en ASIC?


Det är viktigt att förstå sambandet mellan energi och värmeproduktion i ett elsystem.


För en investering på 1 kW elenergi producerar en elradiator 1 kW värme, varken mer eller mindre. Nya radiatorer är inte mer effektiva än traditionella radiatorer. Deras fördel ligger i att de kan fördela värmen kontinuerligt och jämnt i ett rum, vilket ger mer komfort jämfört med traditionella radiatorer som växlar mellan hög värmeeffekt och ingen uppvärmning, vilket ger regelbundna temperaturvariationer och obehag.


En dator, eller mer allmänt ett elektroniskt kort, förbrukar inte energi för att utföra beräkningar; den behöver helt enkelt energi för att flöda genom sina komponenter för att fungera. Energiförbrukningen beror på komponenternas elektriska motstånd, som ger förluster och därmed alstrar värme, den s.k. Joule-effekten.

Vissa företag har kommit på idén att samla behovet av datorkraft och uppvärmningsbehov genom radiator/servrar. Tanken är att distribuera ett företags servrar till små enheter som kan placeras ut i hemmen eller på kontoren. Denna idé stöter dock på flera problem. Behovet av servrar är inte relaterat till behovet av uppvärmning och företagen kan inte använda datorkapaciteten i sina servrar på ett flexibelt sätt. Det finns också gränser för den bandbredd som enskilda personer kan förfoga över. Alla dessa begränsningar hindrar företaget från att göra dessa dyra installationer lönsamma eller att tillhandahålla ett stabilt serverutbud online utan datacenter som kan ta över när uppvärmningen inte behövs.


> Värmen från din dator är inte bortkastad om du behöver värma upp ditt hem. Om du använder elvärme där du bor, är värmen från din dator inte bortkastad. Det kostar samma sak om du generate denna värme med din dator. Om du har ett billigare värmesystem än elvärme är det bara kostnadsskillnaden som är slöseri. Om det är sommar och du använder luftkonditionering är det dubbelt så mycket.
> Bitcoin Mining bör ske där det är billigare. Kanske blir det där klimatet är Cold och där uppvärmningen är elektrisk, som Mining blir gratis.

_Som Satoshi Nakamoto sa den 8 augusti 2010


Bitcoin och dess Proof of Work sticker ut eftersom de automatiskt justerar Mining-svårigheten baserat på mängden databehandling som utförs av hela nätverket, denna mängd kallas Hashrate och uttrycks i hashes per sekund. Idag uppskattas den till 280 Exahashes per sekund, eller 280 miljarder miljarder hashes per sekund. Denna Hashrate representerar arbete och därmed en mängd förbrukad energi. Ju högre Hashrate, desto högre blir svårighetsgraden och vice versa. En Bitcoin Miner kan således aktiveras eller avaktiveras när som helst utan att nätverket påverkas, till skillnad från radiatorer/servrar som måste vara stabila för att kunna erbjuda sina tjänster. Miner belönas för det arbete som utförs i förhållande till andras arbete, oavsett hur litet detta deltagande kan vara.


Sammanfattningsvis producerar en elektrisk radiator och en Bitcoin Miner båda 1 kW värme för 1 kW el som förbrukas. Miner får dock också bitcoins som belöning. Oavsett priset på el, priset på Bitcoin eller konkurrensen från Mining-aktivitet i Bitcoin-nätverket är det ekonomiskt mer fördelaktigt att värma med en Miner snarare än en elektrisk radiator.


![Video presentation](https://youtu.be/gKoh44UCSnE)


### Mervärdet för Bitcoin


Vi kommer inte att gå in på detaljerna i Mining:s drift här (resurser finns tillgängliga på akademin om det behövs). Det som är viktigt att förstå är hur Mining bidrar till decentraliseringen av Bitcoin. Flera befintliga tekniker har kombinerats på ett genialt sätt för att ge liv åt Nakamotos konsensus. Detta samförstånd belönar ärliga aktörer ekonomiskt för deras deltagande i driften av Bitcoin-nätverket, samtidigt som det avskräcker oärliga aktörer. Detta är en av de viktigaste punkterna som gör det möjligt för nätverket att existera på ett hållbart sätt.


De hederliga aktörerna, de som bedriver gruvdrift enligt reglerna, konkurrerar alla med varandra om att få största möjliga andel av belöningen för att producera nya block. Detta ekonomiska incitament leder naturligt till en form av centralisering eftersom företag väljer att specialisera sig på denna lukrativa verksamhet genom att minska sina kostnader genom stordriftsfördelar. Dessa industriella aktörer har en fördelaktig position när det gäller inköp och underhåll av maskiner samt förhandlingar om elpriser.


> Till en början skulle de flesta användare köra nätverksnoder, men när nätverket växte över en viss punkt skulle det lämnas mer och mer till specialister med serverhallar med specialiserad hårdvara. En serverfarm behöver bara köra en nod i nätverket och resten av LAN:et ansluts till den noden.

_Som Satoshi Nakamoto sade den 2 november 2008_


Vissa enheter innehar en betydande andel av den totala Hashrate i stora Mining-gårdar. Vi kan observera den senaste Cold-vågen i USA där en betydande del av Hashrate togs offline för att omdirigera energi till hushåll med ett exceptionellt behov av el. Under flera dagar fick gruvarbetare ekonomiska incitament att stänga av sina gårdar, och därför kan vi se detta exceptionella väder på Bitcoin Hashrate-kurvan.


Denna fråga skulle kunna bli problematisk och utgöra en betydande risk för nätverkets neutralitet. En aktör som innehar mer än 51% av Hashrate skulle lättare kunna censurera transaktioner om de så önskade. Det är därför det är viktigt att fördela Hashrate mellan flera aktörer snarare än centraliserade enheter som lättare kan beslagtas av till exempel en regering.


**Om gruvarbetare är spridda över tusentals, eller till och med miljoner, hushåll runt om i världen blir det mycket komplicerat för en stat att ta kontroll över dem.**


"På fabriken är en Miner inte lämplig att använda som radiator i ett hus på grund av två huvudproblem: för högt ljud och brist på justering. Dessa problem kan dock enkelt lösas genom enkla modifieringar av hård- och mjukvaran, vilket ger en mycket tystare Miner som kan konfigureras och automatiseras på samma sätt som moderna elektriska värmare.


**Attakaï är ett utbildningsinitiativ som lär dig hur du kan eftermontera Antminer S9 på ett så kostnadseffektivt sätt som möjligt


Det här är ett utmärkt tillfälle att lära sig genom att praktisera. Förutom att du minskar din elräkning belönas du för ditt deltagande med gratis KYC Sats.


## Kapitel 1: Köpguide för en begagnad ASIC


I det här avsnittet kommer vi att diskutera bästa praxis för att köpa en begagnad Bitmain Antminer S9, den maskin som denna handledning för eftermontering av kylare kommer att baseras på. Denna guide gäller även för andra ASIC-modeller eftersom det är en allmän köpguide för begagnad Mining-hårdvara.


Antminer S9 är en enhet som erbjuds av Bitmain sedan maj 2016. Den förbrukar 1323W el och producerar 13,5 TH/s. Även om den anses vara gammal, är den fortfarande ett utmärkt alternativ för att starta Mining. Eftersom den har producerats i stora mängder är det lätt att hitta reservdelar i överflöd i många regioner i världen. Den kan i allmänhet förvärvas peer-to-peer på webbplatser som Ebay eller LeBonCoin, eftersom professionella återförsäljare inte längre erbjuder den på grund av dess lägre konkurrenskraft jämfört med nyare maskiner. Den är mindre effektiv än ASICs som Antminer S19, som introducerades sedan mars 2020, men detta gör den till en prisvärd begagnad hårdvara och mer lämplig för de modifieringar vi kommer att göra.


Antminer S9 finns i flera varianter (i, j) som innebär mindre modifieringar av den första generationens hårdvara. Vi anser inte att detta ska påverka ditt köpbeslut, och den här guiden fungerar för alla dessa varianter.


Priset på ASICs varierar beroende på många faktorer, t.ex. priset på Bitcoin, nätverkets svårighetsgrad, maskinens effektivitet och elkostnaden. Därför är det svårt att ge en exakt uppskattning för att köpa en begagnad maskin. I februari 2023 ligger det förväntade priset i Frankrike i allmänhet mellan 100 och 200 euro, men dessa priser kan ändras snabbt.


![image](assets/guide-achat/1.webp)


Antminer S9 är uppbyggd av följande delar:



- 3 hashboards där de chip som producerar hashkraften finns


![image](assets/guide-achat/2.webp)'



- Ett kontrollkort som innehåller en plats för ett SD-kort, en Ethernet-port och kontakter för hashkort och fläktar. Detta är hjärnan i din ASIC.

![image](assets/guide-achat/3.webp)



- 3 datakablar som ansluter hashplattorna till styrkortet.


![image](assets/guide-achat/4.webp)



- Strömmen Supply som drivs med 220V och kan anslutas till elnätet som en vanlig hushållsapparat.


![image](assets/guide-achat/5.webp)



- 2 120 mm fläktar.


![image](assets/guide-achat/6.webp)



- En C13-hankabel.


![image](assets/guide-achat/7.webp)


Vid köp av en begagnad maskin är det viktigt att kontrollera att alla delar ingår och fungerar. Under Exchange bör du be säljaren att slå på maskinen för att verifiera att den fungerar korrekt. Det är viktigt att kontrollera att enheten slås på korrekt och sedan kontrollera internetanslutningen genom att ansluta en Ethernet-kabel och komma åt Bitmain-anslutningen Interface via en webbläsare på samma lokala nätverk. Du hittar denna IP Address genom att ansluta till din internetrouter Interface och leta efter anslutna enheter. Denna Address bör ha följande format: 192.168.x.x


![image](assets/guide-achat/8.webp)


Kontrollera också att standardautentiseringsuppgifterna fungerar (användarnamn: root, lösenord: root). Om standardautentiseringsuppgifterna inte fungerar måste du göra en återställning av maskinen.


![image](assets/guide-achat/9.webp)


När du är ansluten bör du kunna se status för varje hashpanel på instrumentpanelen. Om Miner är ansluten till en pool bör du se att alla hashboards fungerar. Det är viktigt att notera att miners låter en hel del, vilket är normalt. Se också till att fläktarna fungerar som de ska.


Du kan sedan ta bort den tidigare ägarens Mining pool för att sätta upp din egen senare. Om du vill kan du också inspektera hashborden genom att demontera maskinen. Detta steg är dock mer komplicerat och kräver mer tid och vissa verktyg. Om du vill gå vidare med denna demontering kan du hänvisa till nästa del av denna handledning som beskriver hur du gör det. Det är viktigt att notera att gruvarbetare samlar in mycket Dust och kräver regelbundet underhåll. Du kan observera denna Dust-ackumulering och kvaliteten på underhållet genom att demontera maskinen.

Efter att ha granskat alla dessa punkter kan du köpa din maskin med en hög grad av förtroende. Om du är osäker, kontakta communityn, och om du behöver utrustning för att slutföra denna handledning, skicka gärna ett meddelande till oss.

För att sammanfatta den här guiden i en mening:


> Lita inte, verifiera.

## Kapitel 2: Köpguide för modifieringsdelar


![image](assets/piece/1.webp)


### Hur förvandlar du din Antminer S9 till en tyst och uppkopplad värmare?


Om du äger en Antminer S9 vet du säkert hur högljudd och skrymmande den kan vara. Det är dock möjligt att förvandla den till en tyst och ansluten värmare genom att följa några enkla steg. I den här artikeln kommer vi att presentera den nödvändiga utrustningen för att göra ändringarna, medan en senare artikel kommer att förklara i detalj de steg som ska följas för att göra dessa ändringar.


### 1. Byt ut fläktarna


Antminer S9:s originalfläktar är för högljudda för att kunna användas som värmare. Lösningen är att ersätta dem med tystare fläktar. Vårt team har testat flera modeller från varumärket Noctua och valt Noctua NF-A14 iPPC-2000 PWM som den bästa kompromissen. Var noga med att välja 12V-versionen av fläktarna. Denna 140mm fläkt kan producera upp till 1300W värme samtidigt som den bibehåller en teoretisk ljudnivå på 31 dB. För att montera dessa 140mm fläktar behöver du en 140mm till 120mm adapter, som du kan hitta i DécouvreBitcoin-butiken. Vi kommer också att lägga till 140mm skyddsgaller.


![image](assets/piece/1.webp)

![image](assets/piece/2.webp)

![image](assets/piece/3.webp)


Den kraftfulla Supply-fläkten är också ganska bullrig och behöver bytas ut. Vi rekommenderar Noctua NF-A6x25 PWM. Observera att kontakterna på Noctua-fläktarna inte är desamma som de ursprungliga, så du behöver en kontaktadapter för att ansluta dem. Två stycken borde räcka. Återigen, se till att välja 12V-versionen av fläkten.


![image](assets/piece/4.webp)

![image](assets/piece/5.webp)


### 2. Lägg till en WIFI/Ethernet-brygga


Istället för att använda en Ethernet-kabel kan du ansluta din Antminer till WIFI genom att lägga till en WIFI/Ethernet-brygga. Vi har valt vonets vap11g-300 eftersom den enkelt låter dig hämta WIFI-signalen från din Internetbox och överföra den till din Antminer via Ethernet utan att skapa ett subnät. Om du har elektriska färdigheter kan du driva den direkt med Antminers ström Supply utan att behöva lägga till en USB-laddare. För detta behöver du ett 5,5 mmx2,1 mm honjack.


![image](assets/piece/6.webp)

![image](assets/piece/7.webp)


### 3. Valfritt: Lägg till en smart kontakt


Om du vill slå på/stänga av din Antminer från din smartphone och övervaka dess strömförbrukning kan du lägga till en smart kontakt. Vi testade ANTELA-kontakten i 16A-versionen, som är kompatibel med smartlife-applikationen. Med den här smarta kontakten kan du kontrollera den dagliga och månatliga strömförbrukningen och ansluta direkt till din internetbox via WIFI.

![image](assets/piece/8.webp)


**Lista över utrustning och länkar:**



- 2X 3D-adapterstycke 140mm till 120mm
- 2X NF-A14 iPPC-2000 PWM [länk](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)
- 2X 140 mm fläktgaller [länk](https://www.amazon.fr/dp/B06XD4FTSQ)
- Noctua NF-A6x25 PWM [länk](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)
- Elektrikersocker 2,5mm2 [länk](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- Vonets vap11g-300 [länk](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)


## Kapitel 3 - TUTORIAL: Hur gör man en Miner till en värmare?


Om du är en skicklig gör-det-självare och vill förvandla en Miner till en värmare är den här handledningen något för dig. Vi vill varna dig för att modifiering av en elektronisk enhet kan medföra elektriska risker och brandrisker. Det är viktigt att vidta alla nödvändiga försiktighetsåtgärder för att undvika skador eller personskador.

En Miner från fabriken är inte riktigt användbar som radiator i ett hem eftersom den är för högljudd och inte justerbar. Det är dock möjligt att göra enkla modifieringar för att lösa dessa problem.


**Anmärkning:** Det är viktigt att du tidigare har installerat Braiins OS+ på din Miner eller någon annan programvara som kan minska maskinens prestanda. Denna åtgärd är avgörande eftersom vi, för att minska bullret, kommer att installera **mindre kraftfulla fläktar som kan avleda mindre värme**.


### Obligatoriska material



- 2 stycken 3D-adapter 140mm till 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM-fläktar
- 2 140 mm fläktgaller
- 1 Noctua NF-A6x25 PWM-fläkt
- 2.5mm² elektriker-socker
- Vonets VAP11G-300
- Valfritt: ANTELA smart kontakt


### Byte av fläktarna


Vi börjar med att byta ut den strömförande Supply-fläkten.


**Notering**: Först och främst, innan du börjar, se till att du har kopplat ur din Miner för att undvika risk för elstötar.


![image](assets/hardware/1.webp)


Vi börjar med att byta ut den strömförande Supply-fläkten.


Ta först bort de 6 skruvarna på sidan av höljet som håller det stängt. När skruvarna har tagits bort öppnar du försiktigt höljet för att ta bort plasthöljet som skyddar komponenterna.


![image](assets/hardware/2.webp)

![image](assets/hardware/3.webp)'

Därefter är det dags att ta bort originalfläkten, var försiktig så att du inte skadar de andra komponenterna. För att göra detta, ta bort skruvarna som håller den på plats och skala försiktigt bort det vita limmet som omger kontakten. Det är viktigt att gå försiktigt fram för att undvika att skada ledningarna eller kontakterna.

![image](assets/hardware/4.webp)


När originalfläkten har tagits bort kommer du att märka att kontakterna på den nya Noctua-fläkten inte matchar originalfläktens. Den nya fläkten har faktiskt 3 ledningar, inklusive en gul ledning som möjliggör hastighetsreglering. Denna ledning kommer dock inte att användas i detta specifika fall. För att ansluta den nya fläkten rekommenderas att du använder en speciell adapter. Det är dock viktigt att notera att denna adapter ibland kan vara svår att hitta.


![image](assets/hardware/5.webp)


Om du inte har den här adaptern kan du ändå ansluta den nya fläkten med hjälp av en kabelmutter. För att göra detta måste du klippa av kablarna till den gamla och den nya fläkten.


![image](assets/hardware/6.webp)

![image](assets/hardware/7.webp)


På den nya fläkten använder du en avbitare och skär försiktigt konturerna av huvudmanteln på 1 cm utan att skära av mantlarna på kablarna nedanför.


![image](assets/hardware/8.webp)


Dra sedan huvudmanteln nedåt och klipp av mantlarna på den röda och svarta kabeln på samma sätt som tidigare. Och klipp av den gula kabeln i jämnhöjd.


![image](assets/hardware/9.webp)


På den gamla fläkten är det mer känsligt att skära av huvudmanteln utan att skada mantlarna på de röda och svarta ledningarna. För detta ändamål använde vi en nål som vi förde in mellan huvudmanteln och de röda och svarta ledningarna.


![image](assets/hardware/10.webp)

![image](assets/hardware/11.webp)


När de röda och svarta ledningarna är frilagda, klipp försiktigt av höljena för att undvika att skada de elektriska ledningarna.


![image](assets/hardware/12.webp)


Anslut sedan kablarna med en mutter, den svarta kabeln med den svarta och den röda kabeln med den röda. Du kan också lägga till eltejp.


![image](assets/hardware/13.webp)

![image](assets/hardware/14.webp)


När anslutningen är klar är det dags att installera den nya Noctua-fläkten med gallret och de gamla skruvarna, de nya skruvarna som finns i lådan kommer att återanvändas senare. Se till att placera den med rätt orientering. Du kommer att märka en pil på ena sidan av fläkten, som indikerar luftflödets riktning. Det är viktigt att placera fläkten så att pilen pekar mot insidan av chassit. Anslut sedan fläkten igen.

![image](assets/hardware/15.webp)

![image](assets/hardware/16.webp)


**Alternativ:** Om du är duktig på elektricitet kan du direkt lägga till en 5,5 mm jackkontakt till 12V-utgången, vilket gör att du kan strömförsörja Vonet Wi-Fi-bryggan direkt. Men om du är osäker på dina elektriska färdigheter är det bäst att använda USB-kontakten med en smarttelefonladdare för att undvika risk för kortslutning eller elektriska skador.


![image](assets/hardware/17.webp)


När anslutningarna är klara ska du se till att plastskyddet placeras över plasthöljet och inte inuti.


![image](assets/hardware/18.webp)


Slutligen sätter du tillbaka höljets lock på plats och skruvar fast de 6 skruvarna på sidorna för att hålla allt säkert på plats. Och så har du det, ditt power Supply-hölje är nu utrustat med en ny fläkt.


### Byte av de 2 huvudfläktarna


1. Koppla först ur fläktarna och skruva loss dem.

![image](assets/hardware/19.webp)


2. Anslutningarna på de nya Noctua-fläktarna matchar inte de ursprungliga, men ingen panik! Ta fram din avbitartång och klipp försiktigt av de små plastflikarna så att kontakterna passar perfekt till din Miner.


![image](assets/hardware/20.webp)

![image](assets/hardware/21.webp)


3. Nu är det dags att installera 3D-delarna!

Fäst dem på båda sidor av Miner med hjälp av skruvarna som du tog bort från fläktarna. Skruva tills skruvhuvudet går in i 3D-delen och den sitter ordentligt på plats. Var försiktig så att du inte drar åt för mycket, eftersom du då kan deformera delen och en av skruvarna kan komma i kontakt med en kondensator! Klipp sedan försiktigt av de små plastflikarna så att kontakterna passar perfekt med din Miner.


![image](assets/hardware/22.webp)


4. Låt oss nu gå vidare till fansen.

Fäst dem på 3D-delarna med hjälp av skruvarna som medföljer i lådan. Var uppmärksam på luftflödets riktning, pilarna på sidorna av fläktarna visar vilken riktning du ska följa. Gå från Ethernet-portsidan till den andra sidan. Se bilden nedan.


![image](assets/hardware/23.webp)

![image](assets/hardware/24.webp)

![image](assets/hardware/25.webp)


5. Sista steget: koppla in fläktarna och fäst gallren ovanpå med de oanvända skruvarna från fläktboxen. Du har bara 4 stycken, men det räcker med 2 per galler i motsatta hörn. Du kan också leta efter andra liknande skruvar i en järnaffär om det behövs.


![image](assets/hardware/26.webp)

![image](assets/hardware/27.webp)


I väntan på att kunna erbjuda ett sexigare hölje för din nya värmare kan du fästa höljet och strömförsörjningen Supply tillsammans med elektrikerns buntband.


![image](assets/hardware/28.webp)


Och som pricken över i:et ansluter du Vonet-bryggan till Ethernet-porten på dess strömförsörjning Supply. Om du inte redan har gjort det kan du följa den här handledningen för att konfigurera din brygga.


![image](assets/hardware/29.webp)


Och där har du det, grattis! Du har just bytt ut hela den mekaniska delen av din Miner. Du bör nu höra mycket mindre ljud.


## Kapitel 4 - Modifiering av programvara - Återställning av Antminer S9


**Artikelserie föreslagen av BlobOnChain & Ajelex - 15/02/2023**


### Återställ via knappen "Återställ"


Denna metod kan tillämpas inom 10 minuter efter start av Miner.


När du har slagit på Miner i 2 minuter, tryck på "Reset"-knappen i 5 sekunder och släpp den sedan. Miner återställs till fabriksinställningarna inom 4 minuter och startar om automatiskt (du behöver inte stänga av den).


![image](assets/software/1.webp)


Återställning via webbsidan


Logga in på användaren Interface i din Miner, klicka på "Upgrade" >> "Perform a reset" och klicka sedan på "OK" i popup-fönstret.


### Ursprungligt operativsystem


För den här delen kommer vi att anta att maskinen fungerar, körs och att dess ursprungliga operativsystem är installerat. Vi kommer kortfattat att se Interface för det ursprungliga operativsystemet som erbjuds av Bitmain.


Anslut först till din maskin via ditt lokala nätverk:


![image](assets/software/2.webp)


När du är på inloggningssidan måste du logga in på ASIC med hjälp av standardautentiseringsuppgifterna:



- användarnamn: root
- lösenord: root


**Hur återställer jag om standardlösenordet inte fungerar?


Huvudoperativsystemet är relativt grundläggande. Med de 4 flikarna: System, Miner-konfiguration, Miner-status, nätverk. På fliken Miner Configuration kan du konfigurera upp till 3 Mining-pooler.


![image](assets/software/3.webp)


På fliken Miner Status kan du se olika information om hur ASIC fungerar i realtid. Hashrate uttryckt i GH/s, mer detaljerad information om poolen, samt detaljer om statusen för varje hashboard och fläkthastigheten i rotationer/minut.


![image](assets/software/4.webp)


### Braiins OS+


Nu ska vi studera programvaran för ASICs Braiins OS+ (https://braiins.com/os/plus). Programvaran är utvecklad av företaget [Braiins] (https://braiins.com/), som är moderbolag till Mining pool Braiins Pool (https://braiins.com/pool). Denna Mining pool har för närvarande 4,39% av den globala Hashrate när dessa rader skrivs. Det Prag-baserade företaget var tidigare känt som Slushpool och är den första Mining pool som startade i november 2010. [Här](https://Mempool.space/Mining/pool/braiinspool) hittar du uppdaterad statistik för Hashrate och pooldominans.


Idag erbjuder företaget, med sina olika verksamheter, verktyg för lönsamhetsstudier för Mining (https://insights.braiins.com/en), lösningar för hantering av Mining-gårdar parallellt med poolverksamheten samt optimeringsprogramvara för ASICs. Företaget erbjuder också Mining med det nya Stratum V2-protokollet (https://braiins.com/Bitcoin-Mining-stack-upgrade).


Vi kommer därför att studera mer i detalj driften av Bitmain-enheter, som för närvarande är de enda kompatibla modellerna:



- S19, S19 Pro, S19j, S19j Pro, T19,



- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]


Programvaran Braiins OS kan enkelt installeras på alla de maskiner som nämns ovan. Den möjliggör mer exakt kontroll av en maskin genom att tillåta överklockning eller underklockning. Det möjliggör också finjustering av frekvensen för varje chip genom en automatisk optimeringsfunktion som kallas autotuning. Eftersom varje hashingchip är något annorlunda på grund av tillverkningsprocessen, testar programvaran den optimala frekvensen för varje chip för att uppnå maximal effektivitet (W/THs). Programvaran hävdar att den kan uppnå prestanda som är 25% högre än originalet. Enligt våra mätningar är det möjligt att uppnå dessa siffror.


## Installation av Braiins OS+


Det finns flera sätt att installera Braiins OS+ på en ASIC. Du kan hänvisa till den här guiden samt den officiella dokumentationen från Braiins och videohandledning.

Installera Braiins OS+ direkt på Antminers minne


Lär dig hur du enkelt installerar Braiins OS+ direkt i minnet på din Antminer med hjälp av BOS toolbox och ersätter det ursprungliga operativsystemet genom de detaljerade stegen nedan. Om du vill behålla det ursprungliga operativsystemet parallellt kan du installera Braiins OS+ på ett SD-kort.


1. Slå på din Antminer och anslut den till din internetbox.

2. Ladda ner BOS verktygslåda Windows / Linux.

3. Packa upp den nedladdade filen och öppna filen bos-toolbox.bat, välj språk och efter ett ögonblick kommer du att se detta fönster:

![image](assets/software/5.webp)

4. Bos verktygslåda gör att du enkelt kan hitta IP Address för din Antminer och installera Braiins OS+. Om du redan vet IP Address för din maskin kan du hoppa till steg 8. Annars går du till fliken Skanna.

![image](assets/software/6.webp)

5. I hemmanätverk är IP Address-intervallet vanligtvis mellan 192.168.1.1 och 192.168.1.255, så ange "192.168.1.0/24" i fältet för IP-intervall. Om ditt nätverk är annorlunda måste du ändra dessa adresser. Klicka sedan på "Start".

6. Observera att om Antminer har ett lösenord kommer detekteringen inte att fungera. Om så är fallet är den enklaste lösningen att utföra en fabriksåterställning.

7. Du bör se alla Antminers i ditt nätverk, här är IP Address 192.168.1.37.

![image](assets/software/7.webp)

8. Klicka på Tillbaka, gå sedan till fliken Installera, ange den tidigare hittade IP Address i fältet Miner(s) och "admin" (eller "root") i fältet Lösenord, vilket är standardlösenordet, och klicka sedan på "Start".

Om installationen inte fungerar med "admin" eller "root" som lösenord kan det vara nödvändigt att göra en fabriksåterställning och försöka igen.

![image](assets/software/8.webp)

9. Efter några ögonblick kommer din Antminer att starta om och du kommer att kunna komma åt Braiins OS+ Interface på IP Address i fråga, här 192.168.1.37, direkt i Address-fältet i din webbläsare. Standardanvändarnamnet är "root" och det finns inget standardlösenord.

![image](assets/software/9.webp)

![image](assets/software/10.webp)


Att installera Braiins OS+ på ett SD-kort är den andra metoden, den använder den ursprungliga Interface i din Antminer. Den här metoden fungerar för maskiner med ett operativsystem från före 2019.


### Antminer Interface


1. Ladda ner det nya operativsystemet som ska installeras.

2. Precis som i föregående avsnitt ansluter du till din maskin via det lokala nätverket.

3. Gå till fliken System och sedan Upgrade.

4. Ladda den fil som du hämtade och flasha avbildningen.


![image](assets/software/11.webp)


### Micro SD-kort


En andra metod gör att du kan använda ett micro SD-kort. Den här metoden fungerar bara med maskiner med ett operativsystem från efter 2019.


1. Ladda ner det nya operativsystemet som ska installeras.

2. Flasha den nedladdade bilden till ett micro SD-kort. För detta kan du använda Etcher. Att bara kopiera filen till micro SD-kortet fungerar inte.

3. Om du äger en Antminer S9 och dess varianter (S9i, S9j) måste du justera byglarna för att tvinga din ASIC att starta från filen på micro SD-kortet istället för NAND. Om du har en annan modell kan du hoppa till del 4. Byglarna sitter på kontrollkortet på den övre delen av ASIC, nära Ethernet-porten. Du måste ta bort den genom att skjuta den bakåt. När bygelpositionen har ändrats enligt bilderna nedan BOOT FROM SD kan du sätta tillbaka kontrollkortet och återansluta S9.

![image](assets/software/12.webp)

![image](assets/software/13.webp)

4. Sätt i micro SD-kortet i ASIC.

5. Starta ASIC. Om den automatiska installationsversionen användes kommer det nya operativsystemet att installeras automatiskt. Installationen är slutförd när båda LED-lamporna tänds samtidigt. Du kan starta om ASIC och ta ut micro SD-kortet. Om en annan version har laddats ner måste du lämna kvar micro SD-kortet i ASIC.


Mer information om installation finns i detta avsnitt på Braiins webbplats.


## Interface


Du måste ansluta till din ASIC på ett liknande sätt. Använd den lokala IP:n Address för din enhet i ditt nätverk via en webbläsare.


Standardautentiseringsuppgifterna är desamma som för det ursprungliga operativsystemet.



- användarnamn: root
- lösenord: root


Du kommer sedan att mötas av Brains OS+ Dashboard.


### Instrumentpanel


![image](assets/software/14.webp)


På den första sidan kan du se hur din maskin presterar i realtid.



- Tre grafer i realtid som visar temperatur, Hashrate och maskinens övergripande status.
- Till höger visas den verkliga Hashrate, genomsnittlig chiptemperatur, uppskattad effektivitet i W/THs och strömförbrukning.
- Nedan visas fläkthastigheten i procent av maxhastigheten och antalet rotationer per minut.


![image](assets/software/15.webp)



- Längre ner hittar du en detaljerad vy över varje hashboard. Kortets medeltemperatur och de chip det innehåller, spänning och frekvens.
- Detaljer om de aktiva Mining-poolerna i Pools.
- Status för autotuning i Tuner Status.
- Till höger, detaljer om de aktier som överförts till poolen.


### Konfiguration


![image](assets/software/16.webp)


### System


![image](assets/software/17.webp)


### Snabba åtgärder


![image](assets/software/18.webp)


Konfigurera en pool


Man kan föreställa sig en Mining pool som ett jordbrukskooperativ. Jordbrukare slår samman sin produktion för att minska variansen mellan Supply och efterfrågan och därmed få en stabilare inkomst för sin verksamhet. En Mining pool fungerar på samma sätt, och råvaran som samlas ihop är hash. Faktum är att upptäckten av en enda giltig Hash gör det möjligt att skapa ett block och därmed vinna coinbase eller belöningen, för närvarande 3,125 BTC plus transaktionsavgifterna som ingår i blocket. Om du minar ensam kommer du bara att belönas när du hittar ett block. Eftersom du konkurrerar med alla andra miners på planeten skulle du ha mycket liten chans att vinna detta stora lotteri och du skulle fortfarande behöva betala avgifterna för att använda din Miner utan någon garanti för framgång. Mining pooler Address detta problem genom att poola datorkraften hos flera (tusentals) miners och dela deras belöningar baserat på procentandelen deltagande i poolens Hashrate när ett block hittas. För att visualisera dina chanser att Mining ett block ensam kan du använda det här verktyget. Genom att ange informationen för en Antminer S9 kan vi se att chansen att hitta en Hash som gör det möjligt att skapa ett block är 1 av 24 777 849 för varje block eller 1 av 172 068 per dag. I genomsnitt (med en konstant Hashrate och svårighetsgrad) skulle det ta 471 år att hitta ett block.


Men eftersom allt i Bitcoin är sannolikhet händer det ibland att solo gruvarbetare belönas för att ta denna risk: Solo Bitcoin Miner löser block med Hash-hastighet på bara 10 TH/s och slår extremt osannolika odds - Decrypt


Om du gillar att spela kan du prova det, men vår guide kommer inte att fokusera i den riktningen. Istället kommer vi att koncentrera oss på den Mining pool som bäst passar våra behov för att skapa ett värmesystem.

De överväganden som ska göras när du väljer en Mining pool är driften av poolens belöningar, som kan vara olika, samt det lägsta beloppet innan du kan ta ut belöningarna till en Address. Till exempel erbjuder Braiins, som erbjuder den programvara vi pratar om här, också en pool. Denna pool har ett belöningssystem som kallas "Score" som uppmuntrar miners att minera under långa tidsperioder. Deltagandet inkluderar en aktivitetstidsfaktor som uttrycks med en "poäng Hashrate". I vårt fall, där vi vill ha ett värmesystem som bara kan slås på i några minuter, är detta inte det perfekta belöningssystemet. Vi föredrar ett belöningssystem som ger oss en lika stor belöning för varje deltagande. Dessutom är det lägsta uttagsbeloppet för Braiins Pool 100 000 Sats och On-Chain. Så vi förlorar några Sats i transaktionsavgifter och en del av vår belöning kan låsas om vi inte bryter tillräckligt under vintern.


Den belöningsmodell som intresserar oss är PPS, som står för "pay-per-share". Detta innebär att Miner kommer att få en belöning för varje giltig aktie. Det finns också en variant av detta system, FPPS (Full Pay Per Share), som inte bara delar coinbase-belöningen utan också de transaktionsavgifter som ingår i blocket. De Mining pooler vi rekommenderar för att ansluta din Mining/heating är Linecoin Pool (FPPS) och Nicehash (PPS).



- Nicehash: Fördelen med Nicehash är att uttag kan göras med Lightning med minimala avgifter. Dessutom är det minsta uttagsbeloppet 2000 Sats. Nackdelen är att Nicehash använder sin Hashrate för den mest lönsamma Blockchain, utan att verkligen ge kontroll till användaren, så det kanske inte nödvändigtvis deltar i Bitcoin Hashrate.



- Linecoin: Fördelen med Linecoin är antalet funktioner som erbjuds, till exempel en detaljerad instrumentpanel, möjligheten att göra uttag med en Paynym (BIP 47) för bättre integritetsskydd och integrationen av en Telegram-bot samt direkt konfigurerbara automatiseringar i mobilapplikationen. Denna pool bryter endast Bitcoin-block, men det lägsta beloppet för att ta ut förblir högt på 100 000 Sats. Vi kommer att undersöka Interface i en av dessa pooler mer detaljerat i en framtida artikel.


För att konfigurera en pool i Braiins 0S+ måste du skapa ett konto i en av de pooler du väljer. Här kommer vi att ta exemplet Linecoin:


![image](assets/software/19.webp)


När ditt konto har skapats klickar du på Connect To Pool


Kopiera sedan Stratum Address samt ditt användarnamn:


![image](assets/software/20.webp)


Du kan nu återvända till Braiins OS+ Interface för att ange dessa uppgifter. För lösenordet kan du lämna fältet tomt.


![image](assets/software/21.webp)


### Överklockning och underklockning


Överklockning och autotuning innebär båda att frekvenser på hashkort justeras för att förbättra ASIC-prestanda. Skillnaden mellan de två ligger i komplexiteten i dessa frekvensinställningar.


**Overklockning** är en enkel justering som innebär att man ökar frekvensen på hashkort för att öka maskinens Hash-frekvens. Underklockning, å andra sidan, innebär att man sänker klockfrekvensen för en integrerad krets under dess nominella frekvens. Genom att minska klockfrekvensen på en ASIC genom underklockning minskas också värmen som genereras av hårdvaran. Detta gör det möjligt att minska hastigheten på de fläktar som behövs för att kyla ASIC, eftersom de inte behöver arbeta lika mycket som Hard för att hålla en lämplig temperatur. Genom att minska fläkthastigheten minskas också det buller som ASIC genererar. Detta kan vara särskilt användbart för användare som använder ASICs hemma och som vill minimera de ljudstörningar som orsakas av Mining-hårdvara.


Det är viktigt att notera att underklockning kan resultera i en minskning av ASIC-prestandan, så det är viktigt att hitta en bra balans mellan prestanda och ljudnivå.


Braiins OS+ stöder överklockning, underklockning av ASICs och autotuning. Det gör det möjligt för användare att justera klockfrekvensen på sin hårdvara flexibelt för att maximera prestanda eller spara energi enligt deras önskemål.


### Autotuning


Före 2018 hade gruvarbetare två sätt att få en fördel i sin verksamhet: att hitta el till en rimlig kostnad och att köpa effektivare hårdvara. Under 2018 upptäcktes dock ett nytt framsteg inom området Mining-programvara och firmware, kallat AsicBoost. Denna teknik gör det möjligt för gruvarbetare att minska sina kostnader med cirka 13% genom att ändra den fasta programvaran som körs på deras enheter.

Idag finns det ett nytt framsteg inom mjukvaru- och firmware Mining-sektorn som kallas autotuning, vilket ger en ännu större fördel än AsicBoost. ASICs består av många små datachips som utför hashing. Dessa chip är tillverkade av kisel, samma element som används i halvledare och andra mikroelektroniska komponenter. Det som är viktigt att förstå här är att alla kiselchip inte är identiska - varje chip kan variera något i sina elektriska egenskaper. Hårdvarutillverkare vet detta och publicerar prestandaspecifikationerna för sina Mining-maskiner baserat på den nedre gränsen för deras toleranser. Med andra ord vet tillverkarna vilken frekvens som fungerar bäst för genomsnittliga chip och de använder denna frekvens enhetligt för alla chip i maskinen.


Detta sätter en övre gräns för den Hash-frekvens som en maskin kan ha. Autotuning är en process där algoritmer utvärderar de optimala frekvenserna för hashning chip för chip, i stället för att behandla hela maskinen som en enda enhet. Det innebär att ett chip av högre kvalitet som kan utföra fler hashningar per sekund får en högre frekvens, och ett chip av lägre kvalitet som kan utföra relativt färre hashningar får en lägre frekvens. Autotuning på chipnivå är i huvudsak ett sätt att optimera prestandan hos en ASIC genom den programvara och fasta programvara som körs på den.


Slutresultatet blir ett högre Hash-pris per watt elektricitet, vilket innebär större vinstmarginaler för gruvbrytarna. Anledningen till att maskiner inte distribueras med denna typ av programvara är att maskinvarians inte är önskvärt, eftersom kunderna vill veta exakt vad de får och det därför är en dålig idé för tillverkare att sälja en produkt som inte har konsekvent och förutsägbar prestanda från en maskin till en annan. Dessutom kräver autotuning på chipnivå avsevärda utvecklingsresurser, eftersom det är komplicerat att implementera. Tillverkarna lägger redan mycket resurser på att utveckla sina egna firmware. Det finns mjukvarulösningar som möjliggör autotuning, t.ex. Braiins OS+. Förutom att förbättra ASIC-prestandan med upp till 20%.


Denna guide har skapats av DecouvreBitcoin, mer information om MIN201 - kredit Jim och Ajelex