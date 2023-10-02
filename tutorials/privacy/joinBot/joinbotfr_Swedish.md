namn: JoinBot
beskrivning: Förstå och använda JoinBot

![DALL·E - samurajrobot i en röd skog, 3D-rendering](assets/cover.jpeg)

# Om du inte har några vänner, använd JoinBot!

JoinBot är ett nytt verktyg som läggs till i Samourai Wallet-sviten med den senaste uppdateringen 0.99.98f av den populära Bitcoin-plånboksprogramvaran. Det gör det enkelt för dig att genomföra en samarbetsbaserad transaktion för att optimera din integritet utan att behöva hitta en partner.

** Tack till den fantastiska Fanis Michalakis för idén att använda DALL-E för miniatyren! **

## Vad är en samarbetsbaserad transaktion på Bitcoin?

Bitcoin bygger på ett distribuerat och transparent kontoregister. Alla kan spåra användarnas transaktioner i detta elektroniska kontantsystem. För att säkerställa viss integritet kan Bitcoin-användaren genomföra transaktioner med en specifik struktur för att lägga till möjligheten till förnekbarhet vid tolkningen av dessa transaktioner.

Målet är inte att direkt dölja informationen, utan att förvirra den bland annan information. Detta mål används särskilt i Coinjoins, transaktioner som bryter myntets historia på Bitcoin och gör det svårt att spåra det. För att uppnå detta måste flera inputs och outputs av samma belopp skapas i transaktionen.

Inputs är ingångar i en Bitcoin-transaktion och outputs är utgångar. Transaktionen konsumerar sina inputs för att skapa nya outputs genom att ändra villkoren för att spendera ett mynt. Detta är mekanismen som gör det möjligt att flytta bitcoins mellan användare.
Jag pratar mer detaljerat om detta i den här artikeln: Mekanismen för en Bitcoin-transaktion: UTXO, inputs och outputs.

Ett sätt att förvirra spåren i en Bitcoin-transaktion är att genomföra en samarbetsbaserad transaktion. Som namnet antyder innebär det att flera användare kommer överens om att var och en sätter in en summa bitcoins som input i en och samma transaktion och sedan tar ut en summa som output.

Som tidigare nämnts är den mest kända strukturen för en samarbetsbaserad transaktion Coinjoin. Till exempel, på Coinjoin Whirlpool-protokollet, involverar transaktionerna 5 deltagare som input och output, var och en med samma summa bitcoins.

![Diagram över en Coinjoin-transaktion på Whirlpool](assets/1.jpeg)

En extern observatör av denna transaktion kommer inte att kunna veta vilken output som tillhör vilken användare som input. Om vi tar exemplet med användare nr 4 (violett) kan vi identifiera hans/hennes UTXO som input, men vi kommer inte att veta vilken av de 5 outputs som verkligen tillhör honom/henne. Den ursprungliga informationen är inte dold, utan förvirrad i en grupp.
Användaren kan förneka ägandet av en viss UTXO vid utgången. Detta fenomen kallas "plausibel förnekbarhet" och det ger konfidentialitet i en transparent Bitcoin-transaktion.

För att lära dig mer om Coinjoin förklarar jag ALLT i den här långa artikeln: Förstå och använda CoinJoin på Bitcoin.

Även om Coinjoin är mycket effektivt för att bryta spårningen av en UTXO, är det inte lämpligt för direkt utgift. Dess struktur innebär att man måste använda inputs av fördefinierat belopp och outputs av samma värde (minus gruvavgifter). Men utgiftstransaktionen på Bitcoin är en kritisk tidpunkt för konfidentialitet eftersom den ofta skapar en fysisk koppling mellan användaren och dess aktivitet på kedjan. Det verkar därför vara viktigt att använda konfidentialitetsverktyg för utgifter. Det finns också andra strukturer för samarbetsbaserade transaktioner som är speciellt utformade för effektiva betalningstransaktioner.

## StonewallX2-transaktionen

Bland de många utgiftsverktyg som erbjuds av Samourai Wallet finns den samarbetsbaserade transaktionen StonewallX2. Det är en mini Coinjoin mellan två användare som är avsedd för betalningar. Utifrån kan denna transaktion leda till flera möjliga tolkningar. Det finns då möjlighet till plausibel förnekbarhet och därmed konfidentialitet för användaren.

Denna samarbetsbaserade StonewallX2-transaktion är tillgänglig på Samourai Wallet och Sparrow Wallet. Detta verktyg är interoperabelt mellan de två programmen.

Dess mekanism är ganska enkel att förstå. Här är hur det fungerar i praktiken:

> - En användare vill göra en betalning i bitcoins (till exempel till en handlare).
> - Användaren hämtar mottagarens faktiska betalningsadress (handlaren).
> - Användaren bygger en specifik transaktion med flera inputs: minst en som tillhör användaren och en som tillhör en extern medarbetare.
> - Transaktionen kommer att ha 4 outputs, varav 2 av samma belopp: en till handlarens adress för att betala, en växel som går tillbaka till användaren, en output med samma värde som betalningen som går till medarbetaren och en annan output som också går till medarbetaren.

Till exempel, här är en vanlig StonewallX2-transaktion där jag gjorde en betalning på 50 125 sats. Den första inputen på 102 588 sats kommer från min Samourai-plånbok. Den andra inputen på 104 255 sats kommer från min medarbetares plånbok:

![Schemat för en StonewallX2-transaktion](assets/2.jpeg)

Vi kan se 4 outputs, varav 2 av samma belopp för att förvirra spåren:

> - 50 125 sats som går till den faktiska mottagaren av min betalning.
> - 52 306 sats som representerar min växel och som därför går tillbaka till en adress i min plånbok.
> - 50 125 sats som går tillbaka till min medarbetare.
- 53 973 sats som återgår till min medarbetare.
Vid slutet av operationen återfår medarbetaren hela sitt ursprungliga saldo (minus gruvavgifter), och användaren har betalat handlaren. Detta gör det möjligt att lägga till mycket entropi i transaktionen och bryta de tydliga länkarna mellan avsändaren och mottagaren av betalningen.

Styrkan i StonewallX2-transaktionen är att den helt motverkar en av de empiriska reglerna som används av kedjeanalytiker: gemensam ägande av insatser i en transaktion med flera insatser. Med andra ord, i de flesta fall, om vi observerar en Bitcoin-transaktion som har flera insatser, kan vi anta att alla dessa insatser tillhör samma person. Satoshi Nakamoto hade redan identifierat detta problem med användarens integritet i sin White Paper:

> "Som en extra brandvägg kan ett nytt nyckelpar användas för varje transaktion för att hålla dem obundna till en gemensam ägare. Men bindningen är oundviklig med flera insatstransaktioner, vilket nödvändigtvis avslöjar att deras insatser ägdes av samma ägare."

Detta är en av de många empiriska reglerna som används i kedjeanalys för att bygga adresskluster. Om du vill veta mer om dessa heuristiker rekommenderar jag att du läser denna serie av 4 artiklar från Samourai som introducerar ämnet på ett fantastiskt sätt.

Styrkan i StonewallX2-transaktionen ligger i att en extern observatör kommer att tro att de olika insatserna i transaktionen tillhör en gemensam ägare. I själva verket är det två olika användare som samarbetar. Betalningsanalysen leder därför till en vilseledning, och användarnas integritet bevaras.

Utifrån kan en StonewallX2-transaktion inte skiljas från en Stonewall-transaktion. Den faktiska skillnaden mellan dem ligger helt enkelt i det faktum att Stonewall inte är samarbetsvillig. Den använder endast UTXO från en enda användare. Men i deras strukturer på kontoregistret är Stonewall och StonewallX2 helt identiska. Detta gör det möjligt att lägga till ännu fler möjliga tolkningar av denna transaktionsstruktur eftersom en extern observatör inte kommer att kunna veta om insatserna kommer från samma person eller från två samarbetspartners.

Därefter är fördelen med StonewallX2 jämfört med en PayJoin av typen Stowaway att den kan användas i alla situationer. Den faktiska mottagaren av betalningen lägger inte in några insatser i transaktionen. Således kan vi använda en StonewallX2 för att betala hos vilken som helst handlare som accepterar Bitcoin, även om den inte använder Samourai eller Sparrow.
Däremot är den främsta nackdelen med denna transaktionsstruktur att den kräver en medarbetare som är villig att använda sina bitcoins för att delta i din betalning. Om du har bitcoinvänner som är redo att hjälpa dig när som helst är det inte ett problem. Men om du inte känner till några andra användare av Samourai Wallet, eller om ingen är tillgänglig för att samarbeta, då är du fast.

Det finns dock en Telegram-grupp där du kan hitta andra Samourai-användare som är villiga att samarbeta med dig. Du kan hitta den genom att klicka här.

För att lösa detta problem har Samourai-teamen nyligen lagt till en ny funktion i sin app: JoinBot.

# Vad är JoinBot?

Principen för JoinBot är enkel. Om du inte hittar någon att samarbeta med för en StonewallX2-transaktion kan du samarbeta med JoinBot istället. Konkret kommer du att genomföra en samarbetsbaserad transaktion direkt med Samourai Wallet.

Denna tjänst är mycket praktisk, särskilt för nybörjare, eftersom den är tillgänglig 24/7. Om du behöver göra en brådskande betalning och vill göra en StonewallX2 behöver du inte längre kontakta en vän eller leta efter en samarbetspartner online. JoinBot kommer att hjälpa dig.

En annan fördel med JoinBot är att de UTXO (unspent transaction outputs) som den tillhandahåller som input endast kommer från postmix Whirlpool, vilket förbättrar sekretessen för din betalning. Dessutom, eftersom JoinBot är online hela tiden, bör du samarbeta med UTXO som har stora framtida Anonset.

Självklart har JoinBot vissa kompromisser som bör nämnas:

> Precis som för en vanlig StonewallX2 är din samarbetspartner medveten om de använda UTXO:erna och deras destination. I fallet med JoinBot känner Samourai till detaljerna i denna transaktion. Det är inte nödvändigtvis dåligt, men det är viktigt att komma ihåg det.
> För att undvika spam tar Samourai ut en serviceavgift på 3,5% av den faktiska transaktionsbeloppet, med en maximal gräns på 0,01 BTC. Till exempel, om jag skickar en faktisk betalning på 100 kilosatser med JoinBot, kommer serviceavgiften att vara 3 500 satser.
> För att använda JoinBot måste du ha minst två orelaterade och tillgängliga UTXO i din plånbok.
> På en vanlig StonewallX2 delas gruvavgifterna rättvist mellan de två samarbetspartnerna. Med JoinBot måste du själv betala hela gruvavgiften.
För att en JoinBot-transaktion ska vara exakt likadan som en vanlig StonewallX2- eller Stonewall-transaktion görs betalningen av serviceavgifterna i en helt separat transaktion. Återbetalningen av hälften av de ursprungligen betalda gruvavgifterna av Samourai kommer att göras i denna andra transaktion. För att optimera din integritet till fullo görs betalningen av avgifterna med hjälp av en Stowaway-strukturerad transaktion (PayJoin).

## Hur man använder JoinBot?

För att genomföra en JoinBot-transaktion måste du ha en Samourai Wallet-plånbok. Du kan ladda ner den härifrån eller från Google Play Store.

Till skillnad från de flesta verktyg utvecklade av Samourai har Sparrow Wallet ännu inte meddelat att de kommer att implementera JoinBot. Detta verktyg är därför endast tillgängligt på Samourai.

Upptäck steg för steg hur du genomför en StonewallX2-transaktion med JoinBot i den här videon:

![Hur man använder Joinbot](https://youtu.be/80MoMz2Ne5g)

Här är transaktionsschemat som vi just genomförde i videon:

![Schemat för min StonewallX2-transaktion med JoinBot.](assets/3.jpeg)

Där kan man se 5 inputs:

> - 3 inputs på 100 kilosatser som kommer från Samourai (JoinBot).
> - 2 inputs som kommer från min personliga plånbok, på 3 524 satser och 1,8 megasatser.

De 4 outputs av transaktionen är följande:

> - 1 på 212 452 satser till den faktiska mottagaren av min betalning.
> - 1 annan med samma belopp som går till en Samourai-adress.
> - 1 växel som också går tillbaka till Samourai för 87 302 satser. Detta representerar skillnaden mellan deras totala inputs (300 000 satser) och förskjutningsoutputen (212 452 satser) minus gruvavgifterna.
> - 1 växel som går tillbaka till en annan adress i min plånbok. Den representerar skillnaden mellan mina totala inputs och den faktiska betalningen, minus gruvavgifterna.

För att påminna, gruvavgifterna representerar inte en output av transaktionerna. De representerar helt enkelt skillnaden mellan totala inputs och totala outputs.

## Slutsats

JoinBot är ett extra verktyg som ger användare av Samourai fler valmöjligheter och frihet. Det gör det möjligt att genomföra en samarbetsinriktad StonewallX2-transaktion direkt med Samourai som medarbetare. Denna typ av transaktion hjälper till att förbättra användarnas integritet.

Om du kan genomföra en vanlig StonewallX2 med en vän rekommenderar jag ändå att föredra den användningen av verktyget. Å andra sidan, om du är blockerad och inte hittar någon medarbetare för att göra en betalning, vet du att JoinBot kommer att vara tillgänglig 24/7 för att samarbeta med dig.

> Externa resurser:
>
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://youtu.be/vhUREWiY570
- https://docs.samourai.io/wallet/privacy-enhanced-transactions
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin