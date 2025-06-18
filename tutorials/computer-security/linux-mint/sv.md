---
name: Linux Mint

description: Konfigurera en dator för Bitcoin-transaktioner
---

![image](assets/cover.webp)


## Vad är det för fel om du använder en vanlig dator?


När du gör Bitcoin-transaktioner är det idealiskt om din dator inte har någon skadlig kod. Självklart är det så.


Om du håller din Bitcoin seed-fras (vanligtvis 12 eller 24 ord) borta från datorn med en signeringsenhet (t.ex. en Hardware Wallet - dess huvudsyfte), kanske du tycker att det inte är så viktigt att ha en "ren" dator - det stämmer inte.


En dator infekterad med skadlig kod kan läsa dina Bitcoin-adresser och avslöja ditt saldo för en angripare - de kan inte ta Bitcoin bara genom att känna till Address, men de kan se hur mycket du har och utifrån det beräkna om du är ett värdigt mål. De kan också på något sätt räkna ut var du bor, till exempel, och extrahera fingernaglar eller barn från dig för att få dig att betala en lösensumma.


## Vad är lösningen?


Jag uppmuntrar de flesta Bitcoin-användare att använda en dedikerad dator utan skadlig kod (med internetåtkomst) för att göra Bitcoin-transaktioner. Jag föreslår att folk använder ett operativsystem med öppen källkod som Linux Mint, men använd Windows eller Mac om du måste - det är bättre än att använda en vanlig, välanvänd dator som alltid har skadlig kod gömd i den.


Ett hinder som folk stöter på är att installera ett nytt operativsystem på sådana datorer. Den här guiden är till för att hjälpa till med det.


Det finns många olika varianter av Linux och jag har provat flera. Min rekommendation för Bitcoiners är Linux Mint, eftersom det är enkelt att installera, mycket snabbt (särskilt vid uppstart och avstängning), inte uppblåst (varje extra mjukvara är en risk) och sällan har kraschat på mig eller betett sig konstigt (jämfört med andra versioner som Ubuntu och Debian).


Vissa kan vara mycket motståndskraftiga mot ett nytt operativsystem och föredrar Windows eller Mac OS. Jag förstår, men operativsystemen Windows och Apple har sluten källkod, så vi måste lita på vad de gör; jag tycker inte att det är en bra policy, men det är inte allt eller inget. Jag skulle mycket hellre se att folk använde en dedikerad nyinstallerad Windows- eller Mac OS-dator än en välanvänd dator (med vem vet vilken skadlig kod som har samlats på den). Ett steg bättre är att använda en nyinstallerad Linux-dator, vilket är vad jag kommer att demonstrera.


Om du är nervös för att använda Linux på grund av det okända är det naturligt, men det är också bra att lägga lite tid på att lära sig. Det finns så mycket information tillgänglig på nätet. Här är en utmärkt kort video som introducerar grunderna i kommandoraden som jag varmt rekommenderar.

Välj en dator


Jag börjar med det som jag tycker är det bästa alternativet. Sedan ger jag min åsikt om alternativen.


Perfekt alternativ:


Min rekommendation, om du har råd med det och om storleken på din Bitcoin-stack motiverar det, är att skaffa en helt ny bärbar dator på nybörjarnivå. Den mest grundläggande modellen som byggs idag är tillräckligt bra för att hantera vad den kommer att användas till. Processor- och RAM-specifikationerna är inte relevanta, eftersom de alla kommer att vara tillräckligt bra.


Undvik:



- Alla kombinationer av surfplattor, inklusive Surface Pro
- Chromebooks - ofta är lagringskapaciteten för låg
- Alla datorer med en eMMC-enhet; om den har en SSD-enhet är det perfekt
- Mac-datorer - de är dyra, och hårdvaran fungerar inte bra med Linux-operativsystem enligt min erfarenhet
- Allt som är renoverat eller begagnat (dock inte en absolut deal-breaker)


Leta istället efter en bärbar dator med Windows 11 (Windows 11 är för närvarande den senaste versionen. Vi kommer att bli av med den programvaran, oroa dig inte.). Jag sökte på amazon.com efter "Windows 11 Laptop" och hittade det här bra exemplet:


![image](assets/1.webp)


Priset på den här ovan är bra. Specifikationerna är tillräckligt bra. Den har en inbyggd kamera som vi kan använda för PSBT-transaktioner med QR-kod (annars måste du köpa en USB-kamera för att göra det). Oroa dig inte för att det inte är ett välkänt varumärke (det är billigt). Om du vill ha ett bättre varumärke kommer det att kosta dig, t.ex:


![image](assets/2.webp)


Vissa av de billigare har bara 64 GB hårddiskutrymme; jag har inte testat bärbara datorer med så små hårddiskar - det är förmodligen OK att ha 64 GB, men det kan vara att ta i.


## Andra alternativ - Svansar


Tails är ett operativsystem som startar från ett USB-minne och tillfälligt tar över hårdvaran i en dator. Det använder endast Tor-anslutningar, så du måste vara bekväm med att använda Tor. Ingen av de data som du skriver till minnet under din session sparas på enheten (den startar på nytt varje gång) om du inte justerar inställningarna och skapar ett permanent lagringsalternativ (på USB-minnet) - som du låser med ett lösenord.


Det är inte ett dåligt alternativ och det är gratis, men det är lite klumpigt för vårt syfte. Att installera ny programvara på den är inte en bris. En bra funktion är att den levereras med Electrum, men nackdelen med detta är att du inte installerade det själv. Se till att USB-minnet du använder är minst 8 GB.


Din flexibilitet minskar om du använder Tails. Du kanske inte kan följa olika guider för att ställa in det du behöver och få det att fungera korrekt. Om du till exempel följer min guide för att installera Bitcoin Core finns det ändringar som behövs för att få det att fungera. Jag tror inte att jag kommer att göra en Tails-specifik guide, så du måste bygga dina färdigheter och göra det ensam.


Jag är inte heller säker på hur väl hårdvaruplånböcker kommer att interagera med detta operativsystem.


Med allt detta sagt är en Tails-dator för Bitcoin-transaktioner ett trevligt extra alternativ och kommer säkert att hjälpa dina övergripande integritetsfärdigheter att lära dig att använda Tails.


## Andra alternativ - Live OS Boot


Detta är mycket likt Tails, förutom att operativsystemet inte är integritetsskyddat. Det grundläggande sättet att använda detta är att flasha en USB-enhet med det Linux-operativsystem du väljer och få datorn att starta från den istället för den interna enheten. Hur man gör detta förklaras senare.


Fördelen är att du är mindre begränsad och att saker och ting fungerar utan avancerade justeringar.


Jag är inte säker på hur väl ett sådant system isolerar skadlig kod på den befintliga datorn från den USB-startdisk som du använder som innehåller det nya operativsystemet. Det gör förmodligen ett bra jobb och är förmodligen inte lika bra som Tails. Eftersom jag inte vet, föredrar jag den dedikerade bärbara datorn.

Andra alternativ - Din egen begagnade bärbara eller stationära dator


Att använda en begagnad dator är inte idealiskt, främst eftersom jag inte är medveten om hur sofistikerad skadlig kod fungerar, och inte heller om det räcker att rensa en hårddisk för att bli av med den. Det är det förmodligen, men jag vill inte underskatta hur smarta hackare kan vara. Du kan bestämma, jag vill inte binda mig.


Om du väljer att använda en gammal stationär dator istället för en gammal bärbar dator går det bra, förutom att den permanent kommer att ta upp plats för dina förmodligen sällsynta Bitcoin-transaktioner; du bör inte använda den till något annat. Med en bärbar dator kan du däremot bara lägga undan den och till och med gömma den för extra säkerhet.


## Installera Linux Mint på valfri dator


Det här är instruktioner för att radera alla operativsystem från din nya bärbara dator och installera Linux Mint, men du kan anpassa det för att installera nästan vilken Linux-version som helst på nästan vilken dator som helst.


Vi kommer att använda vilken dator som helst för att flasha operativsystemet till en minnespinne av något slag. Det spelar ingen roll vilket minne, så länge det är kompatibelt med en USB-port, och jag föreslår minst 16 GB.


Skaffa en av de här sakerna:


![image](assets/3.webp)


Eller så kan du använda något som detta:


![image](assets/4.webp)


Navigera sedan till linuxmint.com


![image](assets/5.webp)


Håll muspekaren över Download-menyn högst upp och klicka sedan på länken "Linux Mint 20.3" eller den version som är den senaste rekommenderade när du gör detta.


![image](assets/6.webp)


Det kommer att finnas några "smaker" att välja mellan. Välj "Cinnamon" för att följa med i den här guiden. Klicka på knappen Ladda ner.


![image](assets/7.webp)


På nästa sida kan du rulla ner för att se speglarna (speglar är olika servrar som har en kopia av den fil vi vill ha). Du kan verifiera nedladdningen med hjälp av SHA256 och gpg (rekommenderas), men jag ska hoppa över att förklara det här eftersom jag redan har skrivit guider om detta.


![image](assets/8.webp)


Välj en spegel som ligger närmast dig och klicka på dess länk (texten Green i spegelkolumnen). Filen kommer att börja laddas ner - den version jag laddar ner är 2,1 gigabyte.


När den har laddats ner kan du flasha filen till en bärbar minnesenhet och göra den startbar. För att göra detta är det enklaste sättet att använda Balena Etcher. Ladda ner och installera det om du inte har det.


Kör det sedan:


![image](assets/9.webp)


Klicka på Flash från fil och välj den LinuxMint-fil som du hämtade.


Klicka sedan på Select target. Se till att minnesenheten är ansluten och att du väljer rätt enhet, annars kan du förstöra innehållet i fel enhet!


Därefter väljer du Flash! Du kan behöva ange ditt lösenord. När det är klart kommer enheten sannolikt inte att kunna läsas av din Windows- eller Mac-dator eftersom den har förvandlats till en Linux-enhet. Det är bara att dra ut den.

Förbereda måldatorn


Slå på den nya bärbara datorn och håll BIOS-tangenten nedtryckt medan den startar. Detta är vanligtvis F2, men det kan vara F1, F8, F10, F11, F12 eller Delete. Prova alla tills du hittar rätt, eller sök på internet efter din datormodell och ställ rätt fråga.


T.ex. "BIOS-nyckel Dell bärbara datorer".


Varje dator har en BIOS-meny som skiljer sig åt. Utforska och hitta den meny där du kan konfigurera startordningen. För våra syften vill vi att datorn ska försöka starta från en USB-ansluten enhet (om det finns en sådan ansluten), innan den försöker starta från den interna Hard-enheten (annars laddas Windows). När du har ställt in detta kan du behöva spara innan du avslutar eller så kan det sparas automatiskt.


Starta om datorn och den bör laddas från USB-minnet. Vi kan inte installera Linux på den interna hårddisken och Windows kommer att tas bort för gott.


När du kommer till följande skärm väljer du "OEM-installation (för tillverkare)". Om du istället väljer "Starta Linux Mint" får du en Linux Mint-session laddad från minnesenheten, men när du stänger av datorn sparas ingen av dina uppgifter - det är i princip en tillfällig session så att du kan prova den.


![image](assets/10.webp)


Du kommer att ledas genom en grafisk guide som ställer ett antal frågor som bör vara enkla att besvara. En fråga gäller språkinställningar och en annan gäller anslutning till och lösenord för ditt hemnätverk. Om du uppmanas att installera ytterligare programvara, avvisa den. När du kommer till frågan om installationstyp kanske en del tvekar - du måste välja "Radera disken och installera Linux Mint". Kryptera inte heller enheten och välj inte LVM.


Så småningom kommer du till skrivbordet. Vid den här tidpunkten är du inte riktigt klar. Du agerar faktiskt som tillverkaren (dvs. någon som bygger en dator och installerar Linux åt kunden). Du måste dubbelklicka på skrivbordsikonen, "Installera Linux Mint", för att slutföra det.


![image](assets/11.webp)


Kom ihåg att ta bort minnesstickan och starta sedan om. Efter omstarten kommer du att använda operativsystemet för första gången som ny användare. Gratulerar till den här gången.


En av de första sakerna att göra (och att göra regelbundet) är att hålla systemet uppdaterat.


Öppna programmet Terminal och skriv följande:


```bash
sudo apt-get update
```


tryck <enter>, bekräfta ditt val och sedan detta kommando:


```bash
sudo apt-get upgrade
```


tryck <enter> och bekräfta ditt val.


Låt den göra sitt, det kan ta flera minuter.


Därefter vill jag installera Tor (skiftlägeskänsligt):


```bash
sudo apt-get install tor
```


**Pro Tips:** Du kan också köra Linux Mint-start från "OEM-installation" (Se till att du är ansluten till internet, annars kan du få fel). Om du gör detta måste du senare klicka på ikonen "ship to end user" som ska finnas på skrivbordet. Därefter startar du om och startar operativsystemet som om du öppnade datorn för första gången.


Den här guiden förklarade varför du kan behöva en dedikerad dator för Bitcoin-transaktioner och hur du installerar ett nytt Linux Mint-operativsystem på den.