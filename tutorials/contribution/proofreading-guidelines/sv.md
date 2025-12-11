---
name: Riktlinjer för korrekturläsning
description: Vilka är de viktigaste faktorerna att tänka på när man korrekturläser på Plan ₿ Academy?
---

![github](assets/cover.webp)


Välkommen till denna handledning om **riktlinjer att följa när du korrekturläser innehåll på Plan ₿ Academy**. Vi är glada att du delar vårt uppdrag att översätta Bitcoin-material till så många språk som möjligt, för att hjälpa människor att bli medvetna om hur det fungerar och hur det kan användas i deras dagliga liv.


Genom att bidra till Plan ₿ Academy [public repository](https://github.com/PlanB-Network/bitcoin-educational-content) får du först och främst chansen att skriva handledning, korrekturläsa befintligt innehåll eller till och med föreslå att ett nytt språk läggs till på plattformen. Om du vill veta mer kan du först gå med i vår [Telegram Group](https://t.me/PlanBNetwork_ContentBuilder) och skriva en kort presentation om dig och de språk du kan tala.


Den här handledningen är avsedd för bidragsgivare som vill korrekturläsa innehåll. De flesta av dem vet inte mycket om [Github] (https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) eller [Markdown-språket] (https://www.markdownguide.org/basic-syntax/) som vi använder i arkivet, så det är viktigt att dela med sig av några insikter om de nyckelfaktorer som är inblandade i denna uppgift.


Här nedan har jag samlat de vanligaste problemen som korrekturläsare stöter på. Kom gärna med fler förslag, eftersom det kan hjälpa andra att förbättra sig.


Innan du dyker in i detaljerna är det första du ska göra att läsa den här handledningen om de praktiska åtgärder som ska följas på Github, genom att gaffla Plan ₿ Academy-arkivet, göra ändringar och skicka PR:


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Vad är korrekturläsning?


Korrekturläsning är den slutliga granskningsprocessen av en skriven text, för att identifiera och korrigera fel i grammatik, stavning, interpunktion och formatering. Det säkerställer att texten är tydlig, sammanhängande och fri från misstag innan den publiceras eller lämnas in.


När du gör den här typen av uppgifter är det viktigt att följa betydelsen på originalspråket (EN eller FR), men se till att texten på det slutliga språket är så flytande som möjligt för en modersmålstalare.


Kom alltid ihåg att översättning/korrekturläsning är EDUCATION!


Faktum är att vårt gemensamma mål är att utbilda så många människor som möjligt om Bitcoin, så det är grundläggande att det material de läser är smidigt och tydligt.

I denna mening är alla bidragsgivare på Plan ₿ Academy pedagoger!


## De första stegen innan korrekturläsning på Plan ₿ Academy


Innan du påbörjar en ny korrekturläsningsuppgift ska du meddela det i [Telegramgruppen](https://t.me/PlanBNetwork_ContentBuilder) eller informera din Plan ₿ Academy-samordnare, som kommer att öppna en särskild [fråga](https://github.com/orgs/PlanB-Network/projects/3). När du får länken till frågan ska du bara **kommentera att du börjar** med korrekturläsningen av det innehållet.


Det här systemet hjälper koordinatorn att hålla koll på framstegen i repot och gör det möjligt för korrekturläsaren att "göra anspråk" på innehållet, vilket förhindrar att någon annan gör samma sak.

På själva problemet hittar du länkarna som omdirigerar dig till innehållet som ska kontrolleras. Du kan helt enkelt klicka på dem, eller ännu bättre, du kan gå tillbaka till din egen forked repo och arbeta direkt därifrån. Låt oss se hur du kan göra det!


Först och främst ska du ** ALLTID komma ihåg att synkronisera ditt repo på "dev"-grenen**. På så sätt kommer innehållet alltid att vara uppdaterat innan du påbörjar någon typ av uppgift, och du kommer inte att skapa några konflikter mellan gammalt och nytt material. Se till att klicka på "Sync fork" och "Update branch".



![REVIEW](assets/en/1.webp)



När du har synkroniserat kan du direkt komma åt det innehåll du är intresserad av och skapa en ny filial, som visas i denna [handledning] (https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Annars kan du öppna en ny filial där du ska arbeta genom att klicka på "Branches", som visas nedan.



![REVIEW](assets/en/2.webp)



På den här nya sidan hittar du alla filialer som du redan har öppnat under rubriken "Dina filialer". Det här avsnittet är mycket användbart eftersom det gör att du enkelt kan hitta var du har ändrat något innehåll. Om du vill öppna en ny filial kan du klicka på "Ny filial" i det övre högra hörnet på sidan.



![REVIEW](assets/en/3.webp)



Sedan kommer du att få ett popup-fönster där du måste ange namnet på den nya filialen. I fallet nedan valde jag att kalla den "BTC101-FR". På så sätt kommer jag alltid att komma ihåg att den här specifika filialen måste användas för korrekturläsning av kursen BTC101 på franska, och **jag kommer inte att använda den för någon annan uppgift**.


Jag föreslår att du gör likadant: se till att öppna en ny filial när du behöver påbörja en ny uppgift.



![REVIEW](assets/en/4.webp)



När du har skapat den här nya grenen, se till att klicka på den från "Dina grenar" på föregående sida och börja arbeta med *.md*-filen relaterad till det specifika innehållet (i mitt fall kommer jag att klicka på "kurser" -> "BTC101" -> "fr.md"). Alla commits som är relaterade till den specifika filen måste göras (sparas) i samma gren.



## Originalspråk eller översättning?


När du korrekturläser innehåll är det viktigt att **alltid kontrollera den engelska (eller franska)** originalversionen av det. Tänk på att vi översätter med hjälp av AI-språkverktyg, så återgivningen på målspråket kanske inte är flytande eller välförståelig för den slutliga läsaren.


Du får alltså gärna göra justeringar i texten och ändra meningar om det behövs. Vårt mål är att göra texten mer flytande, men alltid i enlighet med den ursprungliga betydelsen. Om du är osäker på hur du ska behandla ett visst ord kan du fråga översättningssamordnaren.


LLM-verktyg kan översätta vissa ord som är relaterade till Bitcoin bokstavligt, som Lightning Network. Det är särskilt fallet när det handlar om mycket tekniska ord. I sådana fall är det lämpligt att behålla det engelska originalordet på målspråket för att göra det tydligare, såvida inte dina språkregler tvingar dig att översätta varje enskilt ord.


I det andra fallet ska du **alltid göra lite efterforskningar för att se om någon annan i din Bitcoin-grupp redan har översatt ordet** och om det nu används allmänt.



- En lösning skulle kunna vara att **kolla på [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** på ditt målspråk för att se om ordet översattes eller inte. Om det inte är det behåller du ordet på engelska.



- I vilket fall som helst skulle mitt råd vara att **införa EN-ordet ändå** och lägga till motsvarande betydelse på målspråket inom rund parentes, enligt schemat EN (LANG), eller vice versa. Ex. Address (indirizzo), eller indirizzo (adress).



- En annan bra lösning är att behålla det ursprungliga ordet/frasen och sedan **skapa en hyperlänk** som omdirigerar till [ordlistan](https://planb.academy/en/resources/glossary) på planb.network. För att göra detta måste du infoga ordet/frasen inom hakparenteser och länken inom runda parenteser, som du kan se i exemplet nedan:


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


I slutresultatet (bilden nedan) kommer du inte att visualisera hela länken, och ordet blir klickbart.



![REVIEW](assets/en/5.webp)



Observera att den länk till ordlistan som du kommer att få från webbplatsen innehåller språkkoden efter ordet "nätverk" (exempel: ``https://planb.academy/en/resources/glossary/utxo``-> här kan du läsa språkkoden "en"). I så fall **tar du bort språkkoden från länken**, som du såg i rutan ovan. På så sätt kommer systemet automatiskt att ta läsaren till det språk som han eller hon har valt.


Innehållet i förvaret är fullt av hyperlänkar som dessa ovan. Nu när du vet vad de betyder, **se till att inte ta bort någon länk** som infogats av den ursprungliga författaren.



- En annan sak som är relaterad till ordåtergivning är följande. Om du hittar "Plan ₿ Academy" i texten ska du **lämna det i denna ursprungliga form**. Översätt inte ordet "plan" eller ordet "network". Dessutom ska du INTE använda artikeln "The" när du introducerar Plan ₿ Academy: **betrakta det som ett varumärke**.



- Detsamma gäller för "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", som också bör behållas i originalform.


En sista kommentar till det här stycket: som vi sa ovan använder vi AI-verktyg för att översätta innehåll, och sedan ber vi om medarbetarnas hjälp för att se till att allt flyter på och är väl korrekturläst.


Om du använder AI för att korrekturläsa större delen av texten kommer vi säkert att märka det, eftersom vi är bekanta med de typiska meningsstrukturer som AI genererar. Om vi upptäcker att du enbart har förlitat dig på AI för korrekturläsning, utan att göra några betydande ändringar, kan den slutliga belöningen i sats komma att halveras!



## Strukturen i rubrikerna


I språket markdown börjar alla rubriker (och styckebeteckningar) med hashtecknet ``#``. Antalet hash-symboler motsvarar rubrikens nivå. Till exempel har en rubrik på nivå tre tre siffertecken före texten (t.ex. `### Min rubrik`).


I kurser inleds de viktigaste delarna med ett enda hash-tecken, medan underdelarna kan ha mellan två och fyra hash-tecken. I självstudier använder vi normalt bara rubriker med två hash-symboler.



![REVIEW](assets/en/6.webp)



Se till att **ALDRIG ta bort hash-symboler** före en titel, annars skapar du problem med strukturen i texten.


Samtidigt ska du **inte ändra** chapterID-delen som du kan se i bilden ovan, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` eller videoreferenserna som ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


När vi infogar ``#`` före en titel blir den automatiskt fet i förhandsgranskningen av kursen, så **undvik att göra titlarna feta under korrigeringen**.


I EN-versionen av kurserna har **titlar som inleds med en eller två ``#`` alla ord som börjar med versaler**, medan titlar som inleds med tre eller fyra ``#`` vanligtvis inte följer denna regel. Om möjligt bör du se till att titlarna på ditt målspråk följer denna struktur.



## Den första delen av kurserna


I början av varje innehåll hittar du följande statiska ord med små bokstäver: "namn", "beskrivning", "mål". De används av webbplatsen för att avkoda själva innehållet och är **alltid kvar i EN**. Därför ska du INTE översätta dem, eftersom innehållet annars kommer att skapa synkroniseringsproblem. Se till att endast korrekturläsa delen efter kolon, som översätts automatiskt av AI.



![REVIEW](assets/en/7.webp)



I samma inledande avsnitt behåller du formatet som det är. Lägg inte till något i början av texten. Undvik t.ex. att lägga till "tt" före bindestrecken, som i bilden nedan!



![REVIEW](assets/en/8.webp)


## Hur man hanterar kursbilder


På vår webbplats finns nu översatta bilder för nästan alla kurser!


När du korrekturläser ska du alltid kontrollera att alla bilder finns med och visas korrekt. Om du i kodvyn hittar den här typen av rad `![IMAGE](assets/en/001.webp)` betyder det att en bild kommer att visas där.


Se till att du alltid lägger till en ny rad mellan bildkoden och texten. Ett exempel nedan:


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```



Kom dessutom ihåg att läsa innehållet i varje bild. Om du upptäcker några problem med översättningen av texten i bilderna, informera din samordnare så får du chansen att korrekturläsa dem också!


Du kan visualisera bilden i avsnittet `Preview` i Github (eller på vår webbplats, öppna i en annan flik). Gå sedan tillbaka till avsnittet "kod" bredvid för korrekturläsning.


![REVIEW](assets/en/9.webp)


## Formatrekommendationer


Här nedan hittar du några exempel på formatfrågor som du bör vara uppmärksam på när du korrekturläser innehåll på ditt målspråk.



- Var uppmärksam på konstiga skiljetecken som "*" eller "**", som kan vara en dålig återgivning av den feta symbolen. I bilden nedan kan du se att asteriskerna bara finns till höger om ordet, vilket ser konstigt ut.



![REVIEW](assets/en/10.webp)



Kontrollera därför alltid den engelska originaltexten för att se om det är meningen att en fet text ska finnas där. I så fall är det bara att lägga till två asterisker i början av ordet, så att det visas korrekt på webbplatsen. Faktum är att i markdown-språket, **för att återge den feta texten, måste du infoga två asterisker ``**`` både före och efter ordet/meningen** (se exempel nedan).



![REVIEW](assets/en/11.webp)




- Samma problem kan uppstå med symboler som $ och `` ` ``.

Se till att kontrollera originalspråksfilen (ofta EN eller FR) för att se var dessa symboler ska vara. Du kan alltid be koordinatorn om hjälp i denna fråga.



- Om du hittar citat, se till att göra lite efterforskningar på nätet för att hitta rätt översättning till ditt språk. Citat infogas vanligtvis efter symbolen ``>``.



![REVIEW](assets/en/12.webp)




## Korrekturläsning av handledning


Om du bestämmer dig för att korrekturläsa självstudier kommer samordnaren att öppna en särskild fråga för **hela avsnittet om självstudier**. När du är klar med din uppgift kan du dokumentera dina framsteg genom att kommentera frågan med en lista över de granskade handledningarna: på så sätt skapar du ett tydligt spårningssystem för framtida referens, vilket är viktigt eftersom nytt innehåll läggs till varje månad. Du kan se ett exempel på detta tillvägagångssätt [här](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).


![REVIEW](assets/en/13.webp)


Eftersom nya handledningar läggs till varje månad kan din filial bli inaktuell under korrekturläsningsprocessen. Vissa korrekturläsare har löst detta problem genom att synkronisera exakt den filial där de arbetar: **Var vänlig och gör det ALDRIG! Om du gör det riskerar du att förlora alla framsteg du har gjort fram till det ögonblicket!**


Istället bör du först avsluta korrekturläsningen av handledningarna i din nuvarande fork. Sedan **synkar du `dev`** och skapar en ny gren där du fokuserar på att korrekturläsa de nyligen tillagda handledningarna (endast de som saknas från din tidigare gren).


I handledningar finns det en risk att **bilderna inte är översatta**. Eftersom de flesta handledningarna är ** ursprungligen skrivna på franska eller engelska**, kommer du förmodligen att hitta bilder som innehåller kommandon eller instruktioner på originalspråket. Låt oss ta ett exempel från handledningen om Sparrow på nederländska, genom att rapportera både texten och den relaterade bilden.


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```


![REVIEW](assets/en/14.webp)


Som du kan se pekar bilden tydligt på `Public Server`, på engelska, medan texten nämner uttrycket `_Publieke server_`. I det här fallet finns det ett koherensproblem, eftersom läsaren hittar motstridig information när han konfronterar bilden med texten.


För att lösa detta problem kan du infoga kommandot som det visas på bilden (engelska eller franska), följt av översättningen till ditt språk inom parentes , enligt nedan:


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```



## Korrekturläsning av frågesporter


Visste du att du även kan korrekturläsa quizfrågorna i varje kurs? Om du till exempel vill korrekturläsa frågesporterna för BTC101 i IT kan du öppna en särskild filial och följa den här vägen: "kurser" -> "BTC101" -> "frågesport". Där hittar du alla mappar som är avsedda för varje fråga, tillsammans med den relaterade språkfilen i _yml_-format.


Återigen, se till att du är i en särskild filial som du öppnar specifikt för detta ändamål, och informera alltid samordnaren.


En viktig sak att tänka på när man korrekturläser den här typen av _yml_-filer är att undvika att lägga till kolon ``:`` eller citationstecken inuti texten . Faktum är att kolon **endast** används för att separera nyckelvärdepar som "wrong_answers" från resten. Du kan se ett exempel på bilden nedan:


![REVIEW](assets/en/15.webp)


När du har granskat frågan ska du se till att ändra statusen "granskad" från "falsk" till "sann", enligt bilden nedan. Se till att **hålla dessa statusord på engelska**, oavsett vilket språk du arbetar med!



![REVIEW](assets/en/16.webp)


Om statusraden "reviewed:true" saknas, se till att **lägga till den i slutet av frågesporten**.


## Korrekturläsning av ordlista


Precis som med frågesporterna kan du också korrekturläsa ordlistan. Den ursprungliga ordlistan skrevs på franska, så du hittar meningar som: "På franska kan det här uttrycket översättas till..."


I sådana här fall ska du anpassa meningen till målspråket eller till engelska. Du kan t.ex. skriva "På engelska används uttrycket...".

Om rubriken är på engelska kan du anpassa meningen till ditt språk: "På swahili är det här uttrycket..."


Se också till att skriva titlar med STORA BOKSTÄVER.


![REVIEW](assets/en/17.webp)



## Titel och beskrivning av din PR


När du skickar din PR skulle det vara fantastiskt om du namngav den i det här formatet: [KORREKTURLÄSNING] INNEHÅLLETS NAMN - SPRÅK:


```
[PROOFREADING] BTC101 - ENGLISH
```


Dessutom kan du i **kommentaravsnittet i PR** skriva "stängs" + numret på den utgåva som samordnaren skickade till dig när du påbörjade korrekturläsningsuppgiften, föregånget av ``#``.

Om du till exempel just skickat en PR med korrekturläsning av cyp201 + frågesporter kan du skriva "stänger [#2934] (https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".


På så sätt kopplas PR-meddelandet och frågan samman, och den som läser det offentliga Github-arkivet kan enkelt hitta information.



## Andra bästa metoder



- Om du behöver söka efter specifika ord i texten kan du klicka på ``CTRL+F`` så visas avsnittet hitta-ersätt. Denna del är mycket användbar när du behöver hoppa till en viss del av texten, eller om du behöver ersätta specifika ord / meningar i batch utan att bläddra i hela innehållet.



![REVIEW](assets/en/18.webp)



När du använder funktionen "ersätt alla" är det viktigt att dubbelkolla resultatet för att se till att inte även länkar har ändrats. Om du till exempel vill ändra ordet "Bitcoin" till "Bitkoin" (vilket kan vara nödvändigt på vissa språk) kan du använda funktionen "ersätt alla" för att effektivt uppdatera alla förekomster i texten. Tänk dock på att det här verktyget också ändrar alla länkar som innehåller det ordet, vilket kan leda till omdirigeringsproblem.


I exemplet nedan har korrekturläsaren använt ovanstående funktion för att ersätta "satoshi" med "satoshi(sats)" och även ändrat länken till en handledning som innehåller själva ordet. Som en följd av detta blev länken ogiltig.


Dubbelkolla alltid alla hyperlänkar i texten för att se till att de är korrekta.



![REVIEW](assets/en/19.webp)




- Om författaren lägger in en länk som hänvisar till en kurs eller handledning i Plan ₿ Academy (**inte** inom parentes), kommer webbplatsen automatiskt att skapa ett "kort" som visar den relaterade miniatyrbilden. Se därför till att du alltid **lägger till en ny rad mellan texten och själva länken**, annars kan du få följande felmeddelande på webbplatsen.



![REVIEW](assets/en/20.webp)



## Slutsats


Sammanfattningsvis kan du verkligen förbättra dina färdigheter när du kontrollerar innehåll genom att vara medveten om de vanligaste korrekturläsarnas misstag. Det är lätt att förbise saker som sammanhang eller konsekvens, och att upptäcka dessa fel kan göra stor skillnad.


Tänk alltid på att en nybörjare kan läsa dessa kurser och handledningar, så det är vårt ansvar att se till att de förstår fullt ut. **Som korrekturläsare är du en utbildare!


Nu är du redo att börja korrekturläsa kurser, självstudier, frågesporter och ordlistor. Håll ögonen öppna för att börja kontrollera videotranskriptioner också!


Tack för att du läste igenom den här handledningen och trevlig resa med korrekturläsning!