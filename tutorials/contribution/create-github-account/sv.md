---
name: GitHub-konto
description: Hur skapar jag ett eget konto på GitHub?
---

![cover](assets/cover.webp)


Plan ₿s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin, tillgängliga på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och finns på GitHub, vilket ger alla möjlighet att bidra till att berika plattformen. Bidrag kan ta olika former: korrigering och korrekturläsning av befintliga texter, översättningar till andra språk, uppdatering av information eller skapande av nya tutorials som ännu inte finns tillgängliga på vår webbplats.


Om du vill bidra till Plan ₿ Network måste du använda Git och GitHub, så om dessa verktyg inte är bekanta för dig eller om deras funktion verkar obskyr, få inte panik, den här artikeln är för dig! Vi kommer tillsammans att gå igenom grunderna i Git och GitHub, samt den tillhörande tekniska jargongen, så att du kan använda dem effektivt efteråt.


## Vad är Git?


Git är ett versionskontrollsystem som är särskilt utformat för att hantera programvaruprojekt. Git skapades 2005 av Linus Torvalds och har snabbt blivit standard för versionshantering inom mjukvaruutvecklingsbranschen. Men vad innebär det egentligen?

![git](assets/11.webp)

Git gör det möjligt för utvecklare att spåra ändringar som gjorts i ett projekts källkod över tid. Det innebär att Git registrerar en ny version av projektet för varje ändring i koden. Om ett fel uppstår eller om en experimentell funktion inte fungerar som förväntat är det möjligt att återgå till ett tidigare tillstånd av koden, som en slags tidsmaskin, men för filer.


En av de viktigaste funktionerna i Git är grenhantering. En gren är en slags parallell linje där utvecklare kan arbeta oberoende av resten av projektet. Detta underlättar i hög grad tillägg av nya funktioner eller korrigering av buggar utan att störa huvudkoden. När ändringarna har testats och validerats kan de slås samman med huvudgrenen.


En av de speciella egenskaperna hos Git är dess förmåga att fungera på ett distribuerat sätt. Varje utvecklare har en fullständig kopia av projektet på sin egen dators Hard-enhet, vilket gör att de kan arbeta offline och sammanfoga ändringar senare när en internetanslutning är tillgänglig. Detta minskar risken för konflikter och gör det möjligt för flera utvecklare att arbeta samtidigt på samma projekt utan att trampa varandra på tårna.

Ursprungligen var Git främst utformat för mjukvaruutvecklingsprojekt. Men det kan också användas för att hantera projekt för att skriva innehåll. Istället för att samarbeta om kod samarbetar vi om text. Och det är just den här metoden som Plan ₿ Network har använt för att hantera sitt innehåll! Git underlättar samarbetet kring skrivande av kurser och handledningar, eftersom det möjliggör exakt spårning av ändringar, effektiv versionshantering och även möjliggör granskning och förbättring av innehållet av andra bidragsgivare.


## Vad är GitHub?


GitHub är en plattform för källkodshantering och hosting som baseras på versionshanteringssystemet Git som vi just diskuterade. GitHub lanserades 2008 och blev snabbt populärt och har blivit en viktig referens för utvecklare över hela världen. Men hur skiljer sig GitHub från Git, och varför är det så viktigt i vår metod för innehållsproduktion?

![github](assets/12.webp)

Först är det viktigt att förstå att GitHub bygger på Git (som vi diskuterade i föregående avsnitt). Medan Git är verktyget som spårar kodändringar, är GitHub onlinetjänsten som är värd för, delar och hanterar denna kod.


Föreställ dig Git som en slags loggbok som varje utvecklare använder på sin egen dator för att registrera alla ändringar i sitt projekt. GitHub, å andra sidan, är som ett offentligt bibliotek där alla dessa loggböcker kan delas, jämföras och kombineras.


Den grundläggande skillnaden mellan Git och GitHub ligger i deras funktion: Git är det verktyg som används lokalt av varje utvecklare för att hantera sina kodversioner, medan GitHub är den onlineplattform som är värd för dessa versioner och underlättar samarbete.


GitHub är mycket mer än bara en tjänst för kodhosting. Det är en samarbetsplattform som gör det möjligt för utvecklare att arbeta tillsammans på ett effektivt sätt. Och Plan ₿ Network använder faktiskt denna plattform för att vara värd för inte bara all kod som driver webbplatsen utan också, och det är det som intresserar oss, allt innehåll (handledning, utbildning, resurser ...).


## Några tekniska termer


På Git och GitHub kommer du att stöta på kommandon och funktioner vars namn kan verka komplexa. I den här sista delen kommer jag att ge några enkla definitioner för att förstå de tekniska termer som du kan stöta på när du använder Git och GitHub:



- Fetch origin:** Kommando som hämtar ny information och ändringar från ett fjärrarkiv utan att sammanfoga dem med ditt lokala arbete. Det uppdaterar ditt lokala arkiv med nya grenar och commits som finns i fjärrarkivet.



- Pull origin:** Kommando som hämtar uppdateringar från ett fjärrförvar och omedelbart integrerar dem i din lokala gren för att synkronisera den. Detta kombinerar stegen för fetch och merge i ett enda kommando.
- Sync Fork:** En funktion på GitHub som gör att du kan uppdatera din Fork av ett projekt med de senaste ändringarna från källarkivet. Detta säkerställer att din kopia av projektet håller sig uppdaterad med den huvudsakliga utvecklingen.
- Push origin:** Kommando som används för att skicka dina lokala ändringar till ett fjärrarkiv.



- Pull Request:** En begäran som skickas av en bidragsgivare för att ange att de har skickat ändringar till en gren i ett fjärrförvar och vill att dessa ändringar ska granskas och eventuellt slås samman till huvudgrenen i förvaret.



- Commit:** Spara dina ändringar. En commit är som en ögonblicksbild av ditt arbete vid ett givet tillfälle, vilket gör det möjligt att hålla en historik över ändringar. Varje commit innehåller ett beskrivande meddelande som förklarar vad som har ändrats.



- Gren:** En parallell version av arkivet som gör det möjligt att arbeta med ändringar utan att påverka huvudgrenen (ofta kallad "main" eller "master"). Filialer underlättar utvecklingen av nya funktioner och korrigering av buggar utan att riskera att störa stabil kod.



- Sammanfoga:** Sammanfogning består i att integrera ändringar från en gren till en annan. Det används t.ex. för att lägga till ändringar från en arbetsgren till huvudgrenen, vilket gör det möjligt att lägga till de olika bidragen.



- Fork:** Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, vilket gör att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Fork kan antingen gå sin egen väg och bli ett annat projekt än det ursprungliga, eller så kan det regelbundet synkronisera med det ursprungliga projektet för att bidra till det.



- Klona:** Att klona ett repository innebär att du gör en lokal kopia på din dator, vilket ger dig tillgång till alla filer och historiken. Detta gör att du kan arbeta med projektet direkt lokalt.



- Repository:** Lagringsutrymme för ett projekt på GitHub. Ett repository innehåller alla projektfiler samt historiken för alla ändringar som har gjorts i dem. Det är grunden för lagring och samarbete på GitHub.



- Issue:** Ett verktyg för att spåra uppgifter och buggar på GitHub. Frågor gör det möjligt att rapportera problem, föreslå förbättringar eller diskutera nya funktioner. Varje fråga kan tilldelas, märkas och kommenteras.


Den här listan är naturligtvis inte uttömmande. Det finns många andra tekniska termer som är specifika för Git och GitHub. De som nämns här är dock de viktigaste som du ofta kommer att stöta på.


Efter att ha läst den här artikeln är det möjligt att vissa aspekter av Git och GitHub fortfarande är oklara för dig, så jag uppmuntrar dig att börja använda dessa verktyg själv. Övning är ofta det bästa sättet att förstå hur maskinen fungerar! Och för att komma igång kan du upptäcka dessa 2 andra tutorials:


## Så här skapar du ett GitHub-konto


Om du vill bidra till PlanB-nätverket behöver du ett GitHub-konto. I den här handledningen kommer vi att vägleda dig steg för steg om hur du skapar ditt eget konto, konfigurerar det och säkrar det på rätt sätt.



- Gå till [https://github.com/signup](https://github.com/signup).
- Ange din e-postadress Address och klicka sedan på Green "Fortsätt"-knappen:

![github](assets/1.webp)


- Välj ett starkt lösenord och klicka sedan på Green:s "Fortsätt"-knapp:

![github](assets/12.webp)


- Därefter väljer du ditt användarnamn. Du kan avslöja din riktiga identitet eller använda en pseudonym. Klicka sedan på Green:s "Fortsätt"-knapp:

![github](assets/3.webp)


- Fyll i Captcha:

![github](assets/4.webp)


- Ett e-postmeddelande med en bekräftelsekod skickas till dig; du måste ange den för att slutföra skapandet av ditt konto:

![github](assets/5.webp)


- Fyll i frågorna om du vill att GitHub ska vägleda dig till vissa verktyg, eller klicka på "Skip personalization" för att hoppa över:

![github](assets/6.webp)


- Välj den kostnadsfria planen genom att klicka på knappen "Fortsätt kostnadsfritt":

![github](assets/7.webp)


- Du kommer då att omdirigeras till din instrumentpanel.
- Om du vill kan du anpassa ditt konto genom att klicka på din profilbild längst upp till höger på skärmen och sedan gå till menyn "Inställningar":

![github](assets/8.webp)


- I det här avsnittet har du möjlighet att lägga till en ny profilbild, välja ett namn, anpassa din biografi eller lägga till en länk till din personliga webbplats:

![github](assets/9.webp)


- Jag rekommenderar också att du besöker menyn "Lösenord och autentisering" för att ställa in åtminstone tvåfaktorsautentisering:

![github](assets/10.webp)