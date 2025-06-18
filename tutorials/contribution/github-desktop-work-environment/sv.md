---
name: GitHub skrivbord
description: Hur ställer man in den lokala arbetsmiljön?
---
![github](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och finns på GitHub, vilket gör att vem som helst kan delta i att berika plattformen. Bidrag kan ta olika former: korrigering och korrekturläsning av befintliga texter, översättning till andra språk, uppdatering av information eller skapande av nya tutorials som ännu inte finns tillgängliga på vår webbplats.


Om du vill bidra till PlanB-nätverket måste du använda GitHub för att föreslå ändringar. För att göra detta har du två alternativ:


- Bidra direkt via GitHubs webb Interface**: Detta är den enklaste metoden. Om du är nybörjare eller om du bara planerar att göra några få mindre bidrag är det här alternativet förmodligen det bästa för dig;
- Bidra lokalt med hjälp av Git**: Den här metoden är mer lämplig om du planerar att göra regelbundna eller betydande bidrag till PlanB Network. Även om det kan verka komplicerat i början att konfigurera din lokala Git-miljö på din dator, är detta tillvägagångssätt effektivare i det långa loppet. Det möjliggör en mer flexibel hantering av ändringar. Om du är ny på detta, oroa dig inte, **vi förklarar hela processen med att ställa in din miljö i denna handledning** (lovar, du behöver inte skriva några kommandorader ^^).


Om du inte har en aning om vad GitHub är, eller om du vill lära dig mer om de tekniska termerna relaterade till Git och GitHub, rekommenderar jag att du läser vår introduktionsartikel för att bekanta dig med dessa begrepp.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- För att börja behöver du naturligtvis ett GitHub-konto. Om du redan har ett kan du logga in, annars kan du använda vår handledning för att skapa ett nytt.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Steg 1: Installera GitHub Desktop



- Gå till https://desktop.github.com/ för att ladda ner programvaran GitHub Desktop. Med den här programvaran kan du enkelt interagera med GitHub utan att behöva använda en terminal:

![github-desktop](assets/1.webp)


- När du först startar programvaran kommer du att bli ombedd att ansluta ditt GitHub-konto. För att göra detta klickar du på "Logga in på GitHub.com":

![github-desktop](assets/2.webp)


- En autentiseringssida öppnas i din webbläsare. Ange ditt e-postmeddelande Address och lösenord som du valde när du skapade ditt konto och klicka sedan på knappen "Logga in":

![github-desktop](assets/3.webp)


- Klicka på `Authorize desktop` för att bekräfta anslutningen mellan ditt konto och programvaran:

![github-desktop](assets/4.webp)


- Du kommer automatiskt att omdirigeras till programvaran GitHub Desktop. Klicka på `Finish`: ![github-desktop](assets/5.webp)
- Om du precis har skapat ditt GitHub-konto kommer du att omdirigeras till en sida som indikerar att du ännu inte har skapat några repositories. Lägg GitHub Desktop-programvaran åt sidan nu, vi återkommer till den senare: ![github-desktop](assets/6.webp)


## Steg 2: Installera Obsidian


Låt oss nu gå vidare till att installera skrivprogrammet. Här har du flera alternativ. Du kommer att behöva programvara som stöder redigering av Markdown-filer, eftersom PlanB Network använder detta format för textfiler i sitt arkiv.


Det finns en mängd program som är specialiserade på att redigera Markdown-filer, till exempel Typora, som är utformad speciellt för att skriva. Även om det inte är idealiskt är det också möjligt att välja en kodredigerare, som Visual Studio Code (VSC) eller Sublime Text. Som skribent föredrar jag dock att använda programvaran Obsidian. Låt oss tillsammans se hur man installerar och kommer igång med den.



- Gå till https://obsidian.md/download och ladda ner programvaran: ![github-desktop](assets/7.webp)
- Installera Obsidian, starta programmet, välj språk och klicka sedan på "Snabbstart": ![github-desktop](assets/8.webp)
- Du kommer att anlända till Obsidian-programvaran. För tillfället har du inga filer öppna: ![github-desktop](assets/9.webp)


## Steg 3: Fork PlanB Network-arkivet



- Gå till datalagret för PlanB Network på följande Address: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content): ![github-desktop](tillgångar/10.webp)
- Från denna sida, klicka på `Fork` knappen längst upp till höger i fönstret: ![github-desktop](assets/11.webp)
- I skapandemenyn kan du lämna standardinställningarna. Se till att rutan `Kopiera endast dev-grenen` är markerad och klicka sedan på knappen `Create Fork`: ![github-desktop](assets/12.webp)
- Du kommer då att komma till din egen Fork i PlanB Network-arkivet: ![github-desktop](assets/13.webp)

Denna Fork utgör ett separat arkiv från det ursprungliga, även om det för närvarande innehåller samma data. Du kommer nu att arbeta med detta nya arkiv.


Vi har på sätt och vis gjort en kopia av PlanB-nätverkets källförvar. Din Fork (kopian) och originalarkivet kommer nu att utvecklas oberoende av varandra. I originalarkivet kan andra bidragsgivare lägga till nya data, medan du, på din Fork, kommer att fortsätta med dina egna ändringar.

För att upprätthålla konsistensen mellan dessa två arkiv kommer det att vara nödvändigt att synkronisera dem regelbundet så att de hämtar samma information. För att skicka dina ändringar till källförvaret använder du det som kallas en **Pull Request**. Och för att integrera ändringar från källförvaret i din Fork använder du kommandot **Sync Fork** som finns tillgängligt på GitHub-webben Interface.

![github-desktop](assets/14.webp)


## Steg 4: Klona Fork



- Återgå till programvaran GitHub Desktop. Vid det här laget bör din Fork visas i avsnittet "Dina arkiv". Om du inte ser det omedelbart, använd dubbelpilen för att uppdatera listan. När din Fork visas klickar du på den för att välja den:

![github-desktop](assets/15.webp)


- Klicka sedan på den blå knappen: `Clone [användarnamn]/Bitcoin-educational-content`:

![github-desktop](assets/16.webp)


- Behåll den förvalda sökvägen. Klicka på den blå knappen "Klona" för att bekräfta:

![github-desktop](assets/17.webp)


- Vänta medan GitHub Desktop klonar din Fork lokalt:

![github-desktop](assets/18.webp)


- Efter kloning av förvaret erbjuder programvaran dig två alternativ. Du måste välja det första: `Att bidra till moderprojektet`. Detta val gör att du kan presentera ditt framtida arbete som ett bidrag till moderprojektet (`PlanB-Network/Bitcoin-educational-content`), och inte enbart som en modifiering av din personliga Fork (`[användarnamn]/Bitcoin-educational-content`). När du har valt alternativet klickar du på "Fortsätt":

![github-desktop](assets/19.webp)


- Ditt GitHub Desktop är nu korrekt konfigurerat. Nu kan du låta programvaran vara öppen i bakgrunden för att följa de ändringar vi kommer att göra.

![github-desktop](assets/20.webp)

Vad vi har uppnått i det här skedet är skapandet av en lokal kopia av ditt arkiv, som finns på GitHub. Som en påminnelse är detta förvar en Fork av källförvaret för PlanB Network. Du kommer att kunna göra ändringar i denna lokala kopia, till exempel lägga till handledning, översättningar eller korrigeringar. När dessa ändringar har gjorts använder du kommandot **Push origin** för att skicka dina lokala ändringar till din Fork som finns på GitHub.


Du kan också hämta ändringar från Fork, t.ex. under en synkronisering med PlanB Network-arkivet. För detta använder du kommandot **Fetch origin** för att hämta ändringarna till din lokala kopia (din klon), och sedan kommandot **Pull origin** för att sammanfoga dem med ditt arbete. Detta gör att du kan hålla dig uppdaterad med den senaste utvecklingen av projektet samtidigt som du bidrar på ett effektivt sätt.


![github-desktop](assets/21.webp)

## Steg 5: Skapa ett nytt Obsidian-valv



- Öppna Obsidian-programmet och klicka på den lilla valv-ikonen längst ned till vänster i fönstret:

![github-desktop](assets/22.webp)


- Klicka på knappen `Open` för att öppna en befintlig mapp som ett valv: ![github-desktop](assets/23.webp)
- Din filutforskare kommer att öppnas. Du måste hitta och välja mappen med titeln `GitHub`, som ska finnas i din `Documents`-katalog bland dina filer. Den här sökvägen motsvarar den som du upprättade i steg 4. När du har valt mappen ska du bekräfta valet. Skapandet av ditt valv på Obsidian kommer sedan att starta på en ny sida av programvaran:


![github-desktop](assets/24.webp)

-> Det är viktigt att du inte väljer mappen `Bitcoin-educational-content` när du skapar ett nytt valv i Obsidian. Välj istället den överordnade mappen, `GitHub`. Om du väljer mappen `Bitcoin-educational-content` kommer konfigurationsmappen `.obsidian`, som innehåller dina lokala Obsidian-inställningar, automatiskt att integreras i förvaret. Vi vill undvika detta, eftersom det inte är nödvändigt att överföra dina Obsidian-konfigurationer till PlanB Network-arkivet. Ett alternativ är att lägga till mappen `.obsidian` i filen `.gitignore`, men den här metoden skulle också ändra filen `.gitignore` i källförvaret, vilket inte är önskvärt.



- På vänster sida av fönstret kan du se filträdet med dina olika GitHub-repositories som har klonats lokalt.
- Genom att klicka på pilarna bredvid mappnamnen kan du expandera dem för att komma åt undermapparna i arkiven och deras dokument:

![github-desktop](assets/25.webp)


- Glöm inte att ställa in Obsidian på mörkt läge: "Ljus drar till sig insekter" ;)


## Steg 6: Installera en kodredigerare


De flesta av dina ändringar kommer att göras i filer i Markdown-format (`.md`). För att redigera dessa dokument kan du använda Obsidian, den programvara som vi diskuterade tidigare. PlanB Network använder dock andra filformat, och du kommer att behöva modifiera några av dem.


När du t.ex. skapar en ny handledning måste du skapa en YAML-fil (`.yml`) för att ange taggarna för din handledning, dess titel och ditt lärar-ID. Obsidian erbjuder inte möjligheten att ändra den här typen av filer, så du behöver en kodredigerare.


För detta finns flera alternativ tillgängliga för dig. Även om datorns standardanteckningsblock kan användas för dessa ändringar, är denna lösning inte idealisk för snyggt arbete. Jag rekommenderar att du väljer programvara som är särskilt utformad för detta ändamål, till exempel [VS Code](https://code.visualstudio.com/download) eller [Sublime Text](https://www.sublimetext.com/download). Sublime Text, som är särskilt lättviktigt, kommer att vara mer än tillräckligt för våra behov.


- Installera ett av dessa program och spara det för framtida ändringar. ![github-desktop](assets/26.webp)

Vi gratulerar dig! Din arbetsmiljö är nu inställd för att bidra till PlanB Network. Du kan nu utforska våra andra specifika handledningar för varje typ av bidrag (översättning, korrekturläsning, skrivning.


https://planb.network/tutorials/others

..).