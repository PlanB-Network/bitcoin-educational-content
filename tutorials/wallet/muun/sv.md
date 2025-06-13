---
name: Muun

description: Konfigurera din Muun Wallet
---

![cover](assets/cover.webp)


Muun (https://muun.com/) är en självförvarare Wallet för Bitcoin och blixtar.


## videohandledning


![video tutorial](https://youtu.be/t1rxp8InZW8)


## Muun Wallet - Komplett användarhandbok


Komplett användarhandbok (med skärmdumpar) för Muun-applikationen; en användarvänlig mobil Bitcoin Wallet som gör att du kan göra transaktioner på Lightning Network.


![image](assets/0.5.webp)


### Ladda ner Muun och skapa din Wallet


Först måste du ladda ner mobilapplikationen, som finns för både iOS och Android. Se alltid till att ladda ner rätt version. Det finns ibland bedrägliga repliker på marknaden. Jag rekommenderar att du hittar den officiella Muun Wallet-webbplatsen, som är https://muun.com/, och använder länken för ditt valda system (iOS/Android), därifrån kan du vara säker på att du använder den officiella applikationen.


![image](assets/1.webp)


När du öppnar programmet får du möjlighet att skapa en ny Wallet eller återställa en befintlig. Låt oss börja med att skapa en ny Wallet. Jag kommer att demonstrera stegen för Wallet-återställning efteråt. Tryck på "Skapa en ny Wallet".


![image](assets/2.webp)


Muun Wallet ber dig sedan att skapa ett fyrsiffrigt personligt identifikationsnummer (PIN). Med en PIN-kod ökar du säkerheten för din Wallet om till exempel en illvillig aktör skulle stjäla din telefon och därmed dina bitcoins.


![image](assets/3.webp)


Där går du, applikationen har genererat en helt ny Wallet som nu kommer att bli hemsidan. Nu måste du säkra relevant Wallet-återställningsinformation innan du skickar några pengar till den, eftersom det skulle vara en riskabel praxis.


![image](assets/4.webp)


### Säkerhetskopiering av nyckel


Tryck på rutan "Säkerhetskopiera din Wallet", så kommer du att omdirigeras till fliken "Säkerhet". Muuns säkerhetskopieringsprocess är bekvämt indelad i tre steg. Det är inte obligatoriskt att genomföra alla tre stegen, men kombinationen av dem ger maximal försiktighet.


![image](assets/5.webp)


Det första alternativet gör att du kan ansluta din Wallet till en e-post Address, och dessutom skydda den med ett lösenord. Detta alternativ är valfritt och kan hoppas över utan problem. Om du vill använda det, tryck på "1: Säkerhetskopiera din Wallet" och sedan på "Start" på nästa skärm och ange en e-post Address. På nästa skärm kommer du att få veta att du måste validera e-postmeddelandet genom att gå till din brevlåda och klicka på länken i Muun-meddelandet.


![image](assets/6.webp)


När e-postmeddelandet har verifierats kommer du att uppmanas att skapa ett lösenord. Sedan måste du kryssa i två rutor som anger att du förstår att Wallet-återställning, om det behövs, kommer att kräva användning av den e-post och det lösenord du just valde. Detta står i kontrast till traditionella program som gör att du kan återställa ditt lösenord vid förlust eller glömska, så se till att du har noterat allt.


![image](assets/7.webp)

![image](assets/8.webp)


Fliken "Säkerhet" visar nu att du har en grundläggande säkerhetskopia. Du kan nu återgå till fliken "Wallet" och använda programmet för att slutföra transaktioner (dessa funktioner beskrivs senare i den här guiden), eftersom du vet att Wallet nu kan återställas. Jag rekommenderar dock att du använder säkerhetsalternativ 2 för att generate en ytterligare säkerhetskopieringskod, om lösenordet som anges i alternativ 1 äventyras eller om du föredrar att inte använda alternativet för återställning av e-post.


![image](assets/9.webp)


Muuns alternativ "alternativ säkerhetskopiering" liknar Mnemonic-frasen som används av flera Wallet-applikationer som många Bitcoin-användare känner till. Tryck på "Start" för att visa din återställningskod och skriv ner den på ett papper (programmet censurerar skärmdumpen på den sida som visar koden). När du har noterat den ska du jämföra den med koden som visas på skärmen eftersom du måste skriva in den på nytt i programmet för att bekräfta att den är giltig.


Återigen ber Muun dig att bekräfta att du har förstått problemet, vilket är att du kommer att behöva denna 32-teckens kod om du förlorar ditt tidigare fastställda lösenord.


Wallet-backupen är nu betydligt säkrare enligt moderna standarder som vi känner till. Muun-applikationen har dock ett tredje säkerhetsalternativ som heter "Emergency Kit". Genom att skapa Emergency Kit kan du återställa din Wallet utan att behöva gå igenom Muun. Med andra ord, genom att använda en annan Bitcoin Wallet-programvara än Muun.


![image](assets/10.webp)


När du har tryckt på "Create an Emergency Kit" kommer du att få förklaringen att detta kit kommer i form av ett PDF-dokument som innehåller information och instruktioner om oberoende överföring av dina medel. Kitet kan lagras i molnet utan oro eftersom det kräver att din "Recovery Code" används, vilket inte ingår i dokumentet. Svep över skärmen för att komma till sidan där du skapar ett kit.


![image](assets/11.webp)


Du kan välja mellan tre alternativ:



- Spara i molnet på ditt Google-konto.
- Skicka ett e-postmeddelande till din egen Address för att säkerhetskopiera ditt kit och få tillgång till det.
- Manuell säkerhetskopiering med en lokal applikation på din enhet.


![image](assets/12.webp)


Se till att du kan komma åt ditt kit när du har skickat det till din valda backup-destination eftersom Muun då kommer att be dig, för valideringsändamål, att ange en sexsiffrig kod som finns i kitet.


![image](assets/13.webp)


När detta sista steg har slutförts är konfigurationen av säkerhet och återställning av Wallet klar. Vi kommer nu att utforska de olika sätten att återställa din Wallet med hjälp av de nyligen skapade säkerhetskopiorna.

Wallet Återvinning


![image](assets/14.webp)


Det finns många scenarier där en användare tillfälligt kan förlora åtkomsten till sin Wallet och sina pengar; förlust av enhet, avinstallerad/ saknad applikation, glömt personligt identifikationsnummer, Wallet frånkoppling, etc. Det är därför absolut nödvändigt att veta hur man återfår denna åtkomst. När du återställer via Muun-applikationen, tryck på alternativet "Jag har redan en Wallet" på öppningsskärmen.


![image](assets/15.webp)


### Återställning med e-post Address


Om du använde Muuns backup-alternativ #1, ange den e-post Address som valdes vid det tillfället. Eftersom detta alternativ är valfritt kan du också välja att fortsätta istället med återställningskoden, vilket råkar vara alternativ # 2 som erbjuds av Muun. Låt oss först gå igenom e-postalternativet.


![image](assets/15.webp)


När din e-postadress Address har angetts kommer Muun att informera dig om att ett e-postmeddelande har skickats till dig och att du måste komma åt det för att auktorisera Wallet-återhämtningen. Kontrollera din brevlåda (inklusive skräppostavdelningen) och använd länken i Muuns e-postmeddelande. Du kommer att omdirigeras till applikationen där skärmen nu kommer att be dig att ange ditt lösenord som är kopplat till det registrerade e-postmeddelandet Address.


![image](assets/16.webp)


Det sista steget är att skapa ett personligt identifikationsnummer, och sedan kommer du tillbaka till bekant territorium på Wallet: s hemsida och anger det saldo som är kopplat till det.


![image](assets/17.webp)


### Användning av "återvinningskoden"


När du återställer åtkomst till en befintlig Wallet kan du välja att använda den återställningskod ("Recovery Code" som Muun anger) som du tidigare noterade om du valde backupalternativ #2.


Den här processen liknar den som beskrivs i föregående avsnitt; återställning via e-post. Välj helt enkelt att använda alternativet "Återställ med återställningskod" och ange den i lämpliga fält som visas på skärmen. Om din Wallet också säkerhetskopieras av ett e-postmeddelande utöver återställningskoden, kommer Muun att be dig att kontrollera din brevlåda för att godkänna återställningsprocessen, som du kan slutföra när du återvänder till applikationen efter att ha klickat på den medföljande länken. Återigen måste du skapa ett personligt identifikationsnummer. Där går du, du kommer att ha tillgång till din Wallet igen.


### Återhämtning med hjälp av nödutrustningen


För att återställa din Wallet utan att använda Muun Wallet-applikationen behöver du ditt nödkit, det tredje återställningsalternativet som erbjuds av Muun. Detta alternativ gör att du kan skicka de medel som finns i din Muun Wallet till någon annan Bitcoin Address. Så se till att du har en alternativ Wallet som kan generate en Address som du kommer att skicka pengarna till.


Öppna det PDF-dokument som du sparade när du skapade satsen. Detta dokument innehåller de instruktioner som krävs för att återställa din Wallet. Observera att den här funktionen kräver användning av en stationär eller bärbar dator eftersom du måste ladda ner ett skript som skapats av Muuns utvecklingsteam. Länken finns med i e-postmeddelandet, men jag delar den här ändå: https://github.com/muun/recovery


Nödsatsen är utrustad med en verifieringskod, som du redan har använt för att bekräfta skapandet av satsen, samt två nycklar. Nycklarna kommer att vara nödvändiga när du aktiverar Muun-återställningsskriptet. Så se till att du har dem till hands under operationen.


![image](assets/19.webp)


Här är en översättning av instruktionerna:


Denna nödrutin hjälper dig att få tillbaka dina pengar om du inte kan använda Muun på din enhet.


1. Hitta din återställningskod


Du skrev den här koden på ett papper innan du skapade din nödutrustning. Du kommer att behöva den senare.


2. Ladda ner återställningsverktyget


Gå till sidan https://github.com/muun/recovery och ladda ner verktyget till din dator.


3. Få tillbaka dina pengar


Kör återställningsverktyget och följ stegen. Verktyget kommer att överföra dina pengar till en Bitcoin Address som du väljer.


![image](assets/20.webp)


En gång i skriptet är allt du behöver göra att ange den begärda informationen på skärmen. Skriptet kommer att ta hand om överföringsprocessen för pengar åt dig. På "github"-sidan som anges ovan finns en animerad video av processen, som visar exakt vad du kan förvänta dig när du startar återställningsskriptet.


![image](assets/21.webp)


## Mottagning av transaktioner


### Bitcoin Tab


Vi kommer nu att gå igenom "Receive"-delen av Muun Wallet och dess olika funktioner. Startsidan för din applikation är fliken "Wallet". Ditt saldo visas i mitten och du kan trycka på det för att växla mellan att dölja beloppet och visa det. Vi kommer att gå igenom alla programinställningar senare i den här artikeln. För tillfället trycker vi på "Receive" för att utforska den här funktionen.


![image](assets/22.webp)


På den här sidan kan du välja att ta emot en transaktion i både Bitcoin- och Lightning-nätverken. En ny Address (och den tillhörande QR-koden) som motsvarar det önskade nätverket kommer att visas. Som standard visas en Bitcoin Address när du kommer till skärmen "Receive". Genom att trycka på QR-koden kopieras Address till din enhets urklipp. Du kan enkelt dela Address direkt till andra applikationer med knappen "Share", och du kan också kopiera Address med knappen "Copy". Om du trycker på ögonikonen i slutet av Address visas den fullständiga Address, så att du kan jämföra den med den som kopierats till urklippet under delningen.


![image](assets/23.webp)


Denna information innehåller allt du behöver för att ta emot transaktioner i Bitcoin-nätverket. Dessutom erbjuder Muun dig några anpassningsalternativ under menyn "Address-inställningar". För det första kan du lägga till ett belopp i Address-beskrivningen. För det andra kan du välja att använda en SegWit Address (standardalternativet) eller en traditionell Address (legacy).


![image](assets/24.webp)


Genom att trycka på "Add +" kan du lägga till ett visst belopp till Address, vilket gör det enklare för den sändande parten. Detta alternativ är valfritt. Observera att när ett belopp har angetts kommer knappen "Kopiera" på föregående sida att lägga till information i den kopierade Address ("Bitcoin:" som prefix, följt av beloppet som suffix). För att undvika att behöva justera detta spontant kan du trycka på QR-koden direkt för att kopiera Address. Beloppsinformationen kommer att förbli förankrad med den. Dessutom låter applikationen dig välja att ange beloppet i den valuta du väljer, vilket förenklar omvandlingsprocessen till BTC.


![image](assets/25.webp)


När det gäller valet av Address-typ, SegWit eller Legacy, rekommenderar jag att SegWit behålls. Denna typ av Address (som börjar med "bc1") minskar storleken på transaktionsdata och minskar därmed de tillhörande transaktionsavgifterna. Det är dock möjligt att du kan behöva använda "Legacy"-systemet (Address som börjar med "3") om en Wallet eller programvara inte är kompatibel med SegWit-adresser. Det är därför viktigt att veta hur man skiljer mellan de två typerna.


![image](assets/26.webp)


## Blixtfliken


För att ta emot transaktioner via Lightning Network måste du trycka på fliken med samma namn högst upp på skärmen. En QR-kod som innehåller en Lightning Address visas nu, som du kan kopiera och dela på samma sätt som Bitcoin-adresserna som nämndes tidigare i den här guiden. Jag påminner dig om att Lightning Network ger dig nästan omedelbar transaktionshastighet och dessutom transaktionsavgifter som är en bråkdel av avgifterna för Bitcoin-kedjan.


![image](assets/27.webp)


Anpassningsalternativen finns under menyn "Invoice-inställningar". Här kan du ändra beloppet som är kopplat till Address genom att trycka på "Lägg till +". Baserat på min erfarenhet med Lightning Network tror jag att det är bättre att ange ett belopp när du skapar transaktionen eftersom flera plånböcker inte svarar bra på tomma fakturor. Du kommer också att märka att det finns en utgångstimer i den här menyn. I den här applikationen är timern inställd på 60 minuter, varefter Address kommer att vara ogiltig. Notera att Muun genererar en ny Lightning Address varje gång du gör en ändring av beloppet eller när du lämnar och återvänder till sidan.


![image](assets/28.webp)


## Använda LNURL-funktionen


Muun Wallet erbjuder möjligheten att använda LNURL för att ta emot transaktioner. Denna funktion, som aktiveras genom att trycka på den fyrkantiga skanningssymbolen längst upp till höger på sidan, har flera fördelar, bland annat behöver du inte dela en Invoice för att ta emot en transaktion. Istället behöver du skanna en QR-kod för att ta emot betalningsinformationen, som du sedan kan validera för att bekräfta transaktionsprocessen.


![image](assets/29.webp)


Muun kommer först att visa dig en förklarande sida (se skärmdump ovan) och sedan be dig att aktivera kamerainmatningen på din enhet, ett nödvändigt steg för att använda applikationen. Observera att LNURL-adresser för närvarande inte stöds av alla Lightning-plånböcker. De som stöder det erbjuder i allmänhet bara möjligheten att använda LNURL för att ta emot transaktioner och inte för att skicka dem.


![image](assets/30.webp)


## Skicka transaktioner


### Via Bitcoin-nätverket


Nu när vi har sett hur man tar emot bitcoins med Muun, låt oss utforska hur man skickar dem. Tillbaka på hemsidan under fliken "Wallet" måste du trycka på "Skicka". En enkel sida kommer nu att visas där du har möjlighet att kopiera en Bitcoin eller Lightning Address till det angivna fältet eller trycka på QR-kodikonen till höger om detta fält för att aktivera kameran och skanna en Address i QR-kodform.


![image](assets/31.webp)

![image](assets/32.webp)


När du kommer till sidan "Skicka", om du redan har en Address kopierad på din enhet, kommer Muun att känna igen Address-formatet (Bitcoin eller Lightning) och föreslå att du använder det för att sända en transaktion genom ett inramat meddelande.


![image](assets/33.webp)

![image](assets/34.webp)


När du förbereder en Bitcoin-transaktion måste du ange det belopp som ska skickas. Se till att destinationen Address som visas högst upp på skärmen matchar den tidigare kopierade Address. Under beloppet som ska skickas visar Muun saldot på din Wallet och ger dig möjlighet att använda alla dina medel, en mycket användbar funktion om du vill tömma din Wallet helt och undvika att lämna kvar "Dust" (några satoshis).


![image](assets/35.webp)


Efter att ha bekräftat beloppet som ska skickas ber Muun dig på nästa sida att skriva en anteckning. Detta fungerar som en ytterligare validering och du kan skriva vad du vill, relevant eller inte.


![image](assets/36.webp)


En slutlig genomgång av transaktionsdetaljerna är nödvändig innan den slutligen sänds. Validera den inmatade Address och beloppet, anpassa sedan transaktionsavgifterna om det behövs genom att trycka på den blå pennikonen till höger om "Nätverksavgift". Att förstå grunderna i hur Bitcoin-transaktionspoolen (Mempool) fungerar är en bra pedagogisk erfarenhet som kan spara dig många satoshis över tid!


![image](assets/37.webp)


Muuns programvara implementerar som standard en algoritm som beräknar de nödvändiga transaktionsavgifterna för en bekräftelse på 30 minuter eller mindre. Detta är vad som kommer att visas när du försöker ändra transaktionsavgifterna. Med knappen "Ange avgift manuellt" kan du själv anpassa denna detalj, en funktion som kan vara mycket användbar om du behöver en snabbare bekräftelse eller omvänt om du har en bred manövermarginal.


![image](assets/38.webp)

Om du väljer att ange beloppet för transaktionsavgiften själv kommer du till en ny sida som anger beloppet som ska anges i sat/vbyte (satoshis per virtuell byte). Muun visar även en uppskattning av bekräftelsetiden som är kopplad till det valda beloppet, samt kostnaden i BTC och fiatvaluta som du väljer.

![image](assets/39.webp)


Gå tillbaka till översiktssidan för transaktionsdetaljer och tryck på "Skicka". Voilà, din transaktion sänds ut i Bitcoin-nätverket! Du kommer att omdirigeras till Wallet:s startsida där du ser avdraget från ditt saldo. Längst ner på skärmen finns en pil som du kan trycka på för att granska din transaktionshistorik. Den transaktion du just gjorde kommer att läggas till i det första ögonblicket av dess utfärdande.


![image](assets/40.webp)


Tryck på en post för att visa detaljerna för en specifik transaktion. Din transaktion kommer att bekräftas när en Miner lägger till ett nytt block som innehåller den till kedjan. Muun delar transaction ID längst ner på skärmen, så att du kan kontrollera statusen för din transaktion på en Block explorer.


![image](assets/41.webp)


## Via Lightning Network


Låt oss nu använda en Bolt 11 Invoice (traditionell/standard Lightning Invoice) för att göra en transaktion. Kopiera eller skanna en Lightning Address på sidan "Skicka". Du kommer att omdirigeras till en ny sida som visar detaljerna för den aktuella Invoice. Transaktionsbeloppen visas (inklusive nätverksavgifter), tillsammans med anteckningen eller beskrivningen som skrivits på Invoice och utgångstimern längst ned. Observera att transaktionsavgifterna inte kan ändras för Lightning-transaktioner. De bestäms av den eller de kanaler som måste användas för att nå mottagaren.


![image](assets/42.webp)


(Här är varningen som visas på skärmen när du använder en tom Invoice, vilket innebär att den inte har något förifyllt belopp. Vissa plånböcker stöder den här typen av Invoice och låter dig anpassa beloppet själv. Detta är inte fallet för Muun)


![image](assets/43.webp)


Om du trycker på ögonikonen visas detaljerna för den Lightning-nod som du har att göra med i den här transaktionen. Du har även möjlighet att visa en webbutforskare för mer information. Detta är ett bra exempel på den tekniska abstraktion som Muun åstadkommer.


![image](assets/44.webp)


När du trycker på "Skicka" kommer din transaktion att startas och normalt slutföras på en bråkdel av en sekund. Det betalda beloppet dras av från ditt saldo, som syns på applikationens startsida. Gå tillbaka till din transaktionshistorik för att se den omedelbara bekräftelsen av betalningen.


![image](assets/45.webp)


Observera att Lightning- och Bitcoin-transaktioner i historiken särskiljs med en annan symbol. Om du vill se detaljerna för Lightning-transaktionen trycker du på den på historikskärmen.


![image](assets/46.webp)


## Applikationsinställningar


Den tredje fliken på startsidan, "Inställningar", är där du kan hitta applikationsinställningarna. Den här sidan är förvånansvärt kort, särskilt jämfört med andra populära mobila plånböcker. Enligt min mening är detta inte en nackdel; tvärtom ser jag det som en fördel när det gäller enkelhet.


![image](assets/47.webp)


I den allmänna kategorin kan du välja önskad konto- och valutaenhet samt applikationens utseendemässiga tema (mörkt eller ljust), som initialt kommer att bestämmas utifrån din enhets system.


För applikationens kontoenhet väljer du mellan Bitcoin (BTC) eller Satoshi (SAT). Bara för din information, en Satoshi är den minsta bråkdelen av en Bitcoin, vilket är den åttonde decimalen (1 SAT = 0,00000001 BTC). Att denominera Wallet i Satoshis är ofta att föredra när man främst använder Lightning Network med små belopp.


Muun erbjuder ett brett urval av valutor, vilket gör det lättare för dig att hitta den nödvändiga BTC-konverteringen för dina transaktions- och/eller personliga behov.


Om du anser att du behöver ändra ditt lösenord för återställning av Wallet kan du göra det på inställningssidan. Se till att du har ditt nuvarande lösenord eller återställningskod och tillgång till din e-post.


![image](assets/48.webp)


Ange ditt nuvarande lösenord eller välj att ange din återställningskod för att påbörja återställningen. Muun kommer att skicka ett e-postmeddelande till den tidigare registrerade Address.


![image](assets/49.webp)

![image](assets/50.webp)


Avsnittet avancerade inställningar innehåller två poster: Bitcoin-nätverk och Lightning Network. I Bitcoin Network får vi välja att aktivera Taproot-mottagningsadresser (bc1p, den nyaste Address-typen) som standard.


![image](assets/51.webp)


Inuti Lightning Network hittar du:



- Mottagande protokoll: Välj ditt standardmottagningsnätverk som visas på skärmen Receive (Mottagning). En experimentell funktion, Unified, finns också tillgänglig. Detta är en QR-kod som förenar både Bitcoin- och Lightning-adresser. För närvarande finns det dock få Bitcoin-program som stöder denna funktion.

-


- Turbo-kanaler: Med det här alternativet kan du aktivera eller inaktivera funktionen Turbo-kanaler. Som standard är den aktiverad.


![image](assets/52.webp)


För att förstå vad som kallas Turbo-kanaler måste vi först veta att Lightning-transaktioner utförs genom kanaler från en användare till en annan, och att dessa kanaler initialt måste finansieras genom en transaktion på Bitcoin Blockchain.


Turbo-kanaler gör att du kan börja göra transaktioner på Lightning Network även innan någon On-Chain-transaktion har bekräftats. Om du inaktiverar denna funktion kommer du att behöva vänta betydligt längre för att göra transaktioner på Lightning Network, i Exchange för ökad säkerhet för dina medel, eftersom du annars måste lita på att Muun inte kommer att agera illvilligt (en mycket offentlig dubbelspend) medan du väntar på att din transaktion ska bekräftas på Blockchain.


Längst ner på inställningssidan finns alternativet "Logga ut". Du kan använda den här funktionen om du vill att programmet ska koppla bort den Wallet som för närvarande känns igen. Detta gör att du kan skapa en ny Wallet eller importera/återskapa en befintlig.


![image](assets/53.webp)