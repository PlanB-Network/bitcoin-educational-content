# Installation av Linux Mint

## Konfigurera en dator för Bitcoin-transaktioner

![image](assets/cover.jpeg)

# En dator för Bitcoin-transaktioner (Installation av Linux Mint)

## Vad är problemet med att använda en vanlig dator?

När du utför Bitcoin-transaktioner är det idealiskt att din dator inte innehåller någon skadlig programvara. Självklart.

Om du håller din Bitcoin-återställningsfras (vanligtvis bestående av 12 eller 24 ord) utanför datorn med en signaturenhet (till exempel en hårdvaruplånbok - dess huvudsyfte), kan du kanske tro att det inte är så viktigt att ha en "ren" dator - men det är inte sant.

En dator som är infekterad med skadlig programvara kan läsa dina Bitcoin-adresser och därmed exponera din saldo för en angripare - de kan inte ta dina bitcoins bara genom att känna till adressen, men de kan se hur mycket du har och beräkna därifrån om du är ett intressant mål. De kan också ta reda på var du bor och utpressa dig genom att hota att skada dig eller kidnappa dina barn.

## Vad är lösningen?

Jag uppmanar de flesta Bitcoin-användare att använda en dedikerad dator som är fri från skadlig programvara (med internetåtkomst) för att utföra Bitcoin-transaktioner. Jag föreslår att människor använder ett öppen källkods-operativsystem som Linux Mint, men använd Windows eller Mac om du måste - det är bättre än att använda en vanlig begagnad dator som sannolikt innehåller dold skadlig programvara.

En hinder som människor stöter på är installationen av ett nytt operativsystem på sådana datorer. Den här guiden är till för att hjälpa dig.

Det finns många varianter av Linux och jag har provat flera av dem. Mitt rekommendation för Bitcoin-användare är Linux Mint, eftersom det är lätt att installera, mycket snabbt (särskilt vid start och avstängning), tar lite plats (varje extra programvara utgör en risk) och det har sällan kraschat eller uppvisat konstigt beteende (jämfört med andra versioner som Ubuntu och Debian).

Vissa kan vara mycket motvilliga att använda ett nytt operativsystem och föredrar Windows eller Mac OS. Jag förstår det, men Windows- och Apple-operativsystemen är proprietära programvaror, så vi måste lita på vad de gör; jag tycker inte att det är en bra policy, men det är inte allt eller inget. Jag skulle mycket hellre vilja att människor använder en nyligen installerad och dedikerad Windows- eller Mac OS-dator än en begagnad dator (med vem vet vilken skadlig programvara som har samlats på den). Ett steg bättre är att använda en nyligen installerad Linux-dator, vilket jag kommer att visa dig.
Om du är nervös inför att använda Linux på grund av det okända, är det normalt, men det är också normalt att ägna tid åt att lära sig. Det finns så mycket information tillgänglig online. Här är en utmärkt kort video som introducerar grunderna i kommandoraden som jag starkt rekommenderar. Välj en dator.

Jag kommer att börja med vad jag anser vara det bästa alternativet. Sedan kommer jag att ge min åsikt om alternativen.

Idealiskt alternativ:

Mitt rekommendation, om du har råd och om storleken på din Bitcoin-plånbok motiverar det, är att köpa en helt ny instegsnivå bärbar dator. Den mest grundläggande modellen som byggs nuförtiden är tillräckligt kraftfull för det den kommer att användas till. Specifikationerna för processorn och RAM-minnet är inte relevanta, eftersom de alla kommer att vara tillräckligt bra.

Att undvika:

- Alla tablettkombinationer, inklusive Surface Pro.
- Chromebooks - ofta är lagringskapaciteten för låg.
- Alla datorer med eMMC-lagring; om den har en SSD är det perfekt.
- Mac-datorer - de är dyra och hårdvaran fungerar inte bra med Linux-operativsystem enligt min erfarenhet.
- Allt som är renoverat eller begagnat (detta är inte ett absolut kriterium för att avvisa alternativet).

I stället bör du leta efter en bärbar dator med Windows 11 (för närvarande är Windows 11 den senaste versionen. Vi kommer att bli av med den mjukvaran, oroa dig inte.). Jag sökte på amazon.com efter en "bärbar dator med Windows 11" och hittade detta bra exempel:
![image](assets/1.png)

Priset på den ovanstående är bra. Specifikationerna är tillräckliga. Den har en inbyggd kamera som vi kan använda för QR-kodstransaktioner med PSBT (annars måste du köpa en USB-kamera för att göra det). Oroa dig inte över att det inte är ett välkänt varumärke (det är billigt). Om du vill ha ett bättre varumärke kommer det att kosta dig, till exempel:
![image](assets/2.png)

Några av de billigaste har bara 64 GB lagringsutrymme; jag har inte testat bärbara datorer med så små diskar - det är förmodligen möjligt att ha 64 GB, men det kan vara begränsat.

## Andra alternativ - Tails

Tails är ett operativsystem som startar från en USB-enhet och temporärt tar kontroll över hårdvaran på vilken dator som helst. Det använder endast Tor-anslutningar, så du måste vara bekväm med att använda Tor. Ingen av de data du skriver i minnet under din session sparas på disken (den startar om från noll varje gång), om du inte ändrar inställningarna och skapar ett permanent lagringsalternativ (på USB-enheten) - som du låser med ett lösenord.
Det är inte en dålig option och det är gratis, men det är lite tungt för vårt syfte. Installationen av nya program är inte enkel. En bra funktion är att det kommer med Electrum, men nackdelen är att du inte har installerat det själv. Se till att USB-minnet du använder har minst 8 GB.

Din flexibilitet är begränsad om du använder Tails. Du kanske inte kan följa olika guider för att konfigurera det du behöver och få det att fungera korrekt. Till exempel, om du följer min guide för att installera Bitcoin Core, krävs det ändringar för att få det att fungera. Jag planerar inte att göra en specifik guide för Tails, så du måste utveckla dina färdigheter och göra det själv.

Jag är inte heller säker på kompatibiliteten med hårdvaruplånböcker för detta operativsystem.

Med det sagt, en Tails-dator för Bitcoin-transaktioner är ett bra extra alternativ och kommer definitivt att hjälpa dig att förbättra dina sekretesskunskaper genom att lära dig att använda Tails.

## Andra alternativ - Live OS Boot

Detta är mycket likt Tails, förutom att operativsystemet inte är dedikerat till sekretess. Det grundläggande sättet att använda det är att kopiera operativsystemet Linux du väljer till ett USB-minne och starta datorn från det istället för den interna disken. Hur du gör detta förklaras senare.

Fördelen är att du är mindre begränsad och att saker kommer att fungera utan avancerade inställningar.

Jag är inte säker på förmågan hos ett sådant system att isolera skadlig programvara på den befintliga datorn från start-USB-minnet du använder för det nya operativsystemet. Det gör förmodligen ett bra jobb och är förmodligen inte lika bra som Tails. Eftersom jag inte vet, föredrar jag en dedikerad bärbar dator.
Andra alternativ - Din egen bärbara dator eller begagnad stationär dator

Att använda en begagnad dator är inte idealiskt, främst eftersom jag inte vet hur avancerad skadlig programvara fungerar internt, eller om formatering av en disk är tillräckligt för att bli av med den. Det är förmodligen fallet, men jag vill inte underskatta skickligheten hos skadliga hackare. Du kan bestämma, jag vill inte engagera mig.
Om du väljer att använda en gammal stationär dator istället för en gammal bärbar dator fungerar det bra, förutom att det definitivt kommer att ta upp utrymme för dina förmodligen sällsynta Bitcoin-transaktioner; du bör inte använda den till något annat. Med en bärbar dator kan du helt enkelt förvara den och till och med gömma den för extra säkerhet.

## Installation av Linux Mint på valfri dator

Här är instruktionerna för att ta bort vilket operativsystem som helst från din nya bärbara dator och installera Linux Mint, men du kan anpassa dem för att installera nästan vilken version av Linux som helst på nästan vilken dator som helst.
Vi kommer att använda vilken dator som helst för att överföra operativsystemet till en USB-enhet eller annan lagringsenhet. Det spelar ingen roll vilken, så länge den är kompatibel med en USB-port, och jag rekommenderar minst 16 GB.

Få tag på en av dessa enheter:

![image](assets/3.png)

Eller så kan du använda något som detta:

![image](assets/4.png)

Gå sedan till linuxmint.com

![image](assets/5.png)

Hovra över nedladdningsmenyn högst upp och klicka sedan på länken "Linux Mint 20.3" eller vilken som helst senaste rekommenderade version vid tidpunkten för detta.

![image](assets/6.png)

Det kommer att finnas några "smaker" att välja mellan. Välj "Cinnamon" för att följa den här guiden. Klicka på nedladdningsknappen.

![image](assets/7.png)

På nästa sida kan du bläddra ner för att se speglarna (spegelserver är olika servrar som innehåller en kopia av filen vi vill ha). Du kan kontrollera nedladdningen med hjälp av SHA256 och gpg (rekommenderas), men jag kommer att hoppa över att förklara det här eftersom jag redan har skrivit guider om det.

![image](assets/8.png)

Välj en spegel som är närmast dig och klicka på dess länk (grön text i spegelkolumnen). Filen börjar laddas ner - den version jag laddar ner är 2,1 gigabyte.

När nedladdningen är klar kan du överföra filen till en bärbar lagringsenhet och göra den bootbar. Det enklaste sättet att göra detta är att använda Balena Etcher. Ladda ner och installera det om du inte redan har det.

Kör det sedan:

![image](assets/9.png)

Klicka på "Flash from file" och välj LinuxMint-filen du laddade ner.

Klicka sedan på "Select target". Se till att lagringsenheten är ansluten och se till att välja rätt enhet, annars riskerar du att radera innehållet på fel enhet!

Efter det, välj "Flash!" Du kanske måste ange ditt lösenord. När det är klart kommer enheten förmodligen inte att vara läsbar av din Windows- eller Mac-dator eftersom den har omvandlats till en Linux-enhet. Ta bara bort den.
Förberedelse av måldatorn
Starta den nya bärbara datorn och håll BIOS-knappen nedtryckt medan den startar. Det är vanligtvis F2, men det kan vara F1, F8, F10, F11, F12 eller Delete. Prova var och en av dem tills du får rätt, eller sök på internet efter modellen på din dator och ställ rätt fråga.
Till exempel, "BIOS-knapp för Dell-bärbara datorer".

Varje dator kommer att ha en annan BIOS-meny. Utforska och hitta menyn som låter dig konfigurera startordningen. I vårt fall vill vi att datorn ska försöka starta från en ansluten USB-enhet (om det finns en ansluten) innan den försöker starta från den interna hårddisken (annars kommer Windows att laddas). När du har ställt in detta måste du kanske spara innan du avslutar eller så sparas det automatiskt.

Starta om datorn och den ska starta från USB-lagringsenheten. Nu kan vi installera Linux på den interna disken och Windows kommer att tas bort permanent.
När du kommer till nästa skärm, välj "OEM-installation (för tillverkare)". Om du istället väljer "Starta Linux Mint" får du en Linux Mint-session som laddas från minnesenheten, men när du stänger av datorn sparas ingen av dina uppgifter - det är i princip en tillfällig session för att du ska kunna prova den.
![image](assets/10.png)

Du kommer att guidas genom en grafisk guide som kommer att ställa flera enkla frågor. En av dem kommer att vara språkinställningar, en annan kommer att vara din hemanslutning till internet och ditt lösenord. Om du blir ombedd att installera ytterligare programvara, avböj. När du kommer till frågan om installationsalternativ kan vissa vara osäkra - du måste välja "Radera disken och installera Linux Mint". Dessutom, kryptera inte disken och välj inte LVM.

Du kommer till slut att komma till skrivbordet. Vid det här laget är du inte helt klar. Du agerar faktiskt som en tillverkare (det vill säga någon som monterar en dator och konfigurerar Linux för kunden). Du måste dubbelklicka på skrivbordsikonen "Installera Linux Mint" för att slutföra installationen.

![image](assets/11.png)

Glöm inte att ta bort USB-enheten och starta om. Efter omstarten kommer du att använda operativsystemet för första gången som en ny användare. Grattis.

En av de första sakerna att göra (och göra regelbundet) är att hålla systemet uppdaterat.

Öppna Terminal-applikationen och skriv följande:

```
    sudo apt-get update
```

tryck på <enter>, bekräfta ditt val, och sedan detta kommando:

````
sudo apt-get upgrade```

Tryck på <enter> och bekräfta ditt val.

Låt det göra sitt jobb, det kan ta flera minuter.

Sedan gillar jag att installera Tor (skiftlägeskänsligt):

````

    sudo apt-get install tor

```

> _TILLÄGG: Du kan också köra Linux Mint-start från "OEM-installation" (Se till att du är ansluten till internet, annars kan du stöta på fel). Om du gör det måste du sedan klicka på ikonen "skicka till slutanvändaren" som bör finnas på skrivbordet. Du startar sedan om och startar operativsystemet som om du öppnar datorn för första gången._

Denna guide förklarar varför du kan behöva en dator dedikerad till Bitcoin-transaktioner och hur du installerar ett fräscht Linux Mint-operativsystem på den.
```
