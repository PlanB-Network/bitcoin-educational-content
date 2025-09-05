---
name: Weblate - översättning av statisk Elements
description: Hur kan du delta i översättningen av den statiska Elements på planb.network?
---
![cover](assets/cover.webp)


Plan ₿ Network:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser på Bitcoin och översätta dem till så många språk som möjligt. Mycket av det innehåll som publiceras på webbplatsen är öppen källkod och finns på GitHub, vilket gör att vem som helst kan delta i att berika plattformen. Bidrag kan ta olika former: korrigering och korrekturläsning av befintligt innehåll, uppdatering av information eller skapande av nya handledningar att lägga till på plattformen.


I den här handledningen visar vi dig hur du enkelt kan bidra till översättningen av den statiska Elements på vår webbplats. Uppgifterna på plattformen är indelade i två huvudkategorier:


- frontend-data/statisk Elements (sidor, knappar etc.);
- utbildningsinnehåll (handledning, kurser, resurser ...).


För att översätta det pedagogiska innehållet använder vi [artificiell intelligens] (https://github.com/Asi0Flammeus/LLM-Translator). För att rätta till eventuella fel i dessa filer bjuder vi sedan in korrekturläsare att bidra. Om du vill korrekturläsa en del av innehållet kan du läsa följande handledning:


https://planb.network/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017

Om du däremot är intresserad av att översätta webbplatsens statiska Elements (exklusive utbildningsinnehåll) har du kommit helt rätt! För att effektivt översätta frontend använder vi verktyget Weblate, som är mycket enkelt att använda och underlättar översättningen.


Om du vill lägga till ett helt nytt språk i Plan ₿ Network, se till att kontakta Plan ₿ Network-teamet via vår [Telegramgrupp] (https://t.me/PlanBNetwork_ContentBuilder). Om du inte har telegram kan du skicka ett e-postmeddelande till mari@planb.network. Se till att skriva en liten presentation om vem du är och vilka språk du talar.

Våra medarbetare kommer att ge dig specifika instruktioner och öppna relaterade "issues" på Github för att samordna ditt arbete.


Innan du följer denna specifika handledning för att lägga till ett nytt språk i Weblate.


https://planb.network/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86

När du är redo att börja översätta kan du gå tillbaka till den här handledningen och gå igenom följande punkter.


## Registrera dig på Weblate



- Gå till [den självhostade Weblate för Plan ₿ Network] (https://weblate.planb.network/):

![weblate](assets/01.webp)


- Om du redan har ett Weblate-konto klickar du på "Logga in":

![weblate](assets/02.webp)


- Om du inte har något konto klickar du på "Registrera dig":

![weblate](assets/03.webp)


- Ange din e-postadress Address, samt ett användarnamn och fullständigt namn (du kan använda en pseudonym) och klicka sedan på "Registrera":

![weblate](assets/04.webp)


- I din e-postinkorg bör du ha fått ett bekräftelsemeddelande från Weblate. Klicka på länken för att bekräfta din registrering:

![weblate](assets/05.webp)


- Välj ett starkt lösenord och klicka sedan på "Ändra mitt lösenord":

![weblate](assets/06.webp)


- Du kan nu gå tillbaka till Plan ₿ Network:s instrumentpanel:

![weblate](assets/07.webp)


## Börja översätta



- Klicka på projektet "Webbplats Elements" (inte ordlistan):

![weblate](assets/08.webp)


- Du kommer till en Interface, där du kan se vilka språk som är på gång:

![weblate](assets/09.webp)


- Välj ditt språk. Låt oss till exempel ta franska:

![weblate](assets/10.webp)


- För att börja översätta klickar du bara på knappen `Translate`:

![weblate](assets/11.webp)


- Du kommer att omdirigeras till arbetet Interface:

![weblate](assets/12.webp)


- Weblate kommer sedan automatiskt att föreslå meningar, stycken eller till och med ord att översätta i rutan "språk". I ditt fall kommer du förmodligen att se den engelska huvudsträngen och en annan textruta för ditt språk:

![weblate](assets/13.webp)


- Din uppgift består i att översätta de angivna strängarna. Du måste skriva din text i den ruta som motsvarar det språk du har valt. Om du t.ex. arbetar med den franska versionen, skriver du din översättning i rutan "Franska":

![weblate](assets/14.webp)


- Klicka på fliken "Automatiska förslag":

![weblate](assets/15.webp)


- Här visar Weblate dig en översättning som gjorts med hjälp av artificiell intelligens:

![weblate](assets/16.webp)


- Om den föreslagna översättningen verkar relevant för dig kan du klicka på knappen "Klona till översättning":

![weblate](assets/17.webp)


- Förslaget är nu placerat i din arbetslåda:

![weblate](assets/18.webp)


- Du kan sedan ändra förslaget manuellt:

![weblate](assets/19.webp)


- När du tycker att översättningen verkar tillfredsställande klickar du på knappen "Spara och fortsätt". Se till att avmarkera rutan "Behöver redigeras" när du är säker på din översättning:

![weblate](assets/20.webp)


- Så där ja! Din översättning har sparats framgångsrikt. Weblate kommer automatiskt att omdirigera dig till nästa objekt att översätta. Om du går tillbaka till instrumentpanelen för ditt språk kan du se att alla typer av strängar har olika översättningsstatus. Om du till exempel bara vill fokusera på "oöversatta strängar" kan du klicka på den specifika fliken:

![weblate](assets/21.webp)


- Om du behöver söka efter ett specifikt ord, oavsett om det är på ditt språk eller på originalspråket, klickar du på "sök" och infogar det där:

![weblate](assets/22.webp)


## Riktlinjer för översättning



- När du hittar ord som är infogade inom hakparenteser "{" behöver du inte översätta dem. Till exempel i "Your account has been created, {{userName}}!" översätter du hela meningen, men behåller "användarnamn" på engelska.
- När du hittar "Plan ₿ Network" i en sträng, se till att INTE översätta ordet "nätverk" (betrakta Plan ₿ Network som ett varumärke). Dessutom ska du alltid använda Bitcoin:s ₿!
- Om du bara hittar ordet "network" kan du översätta det i stället.
- Översätt inte "B-CERT", eftersom det är ett annat fast ord.
- Om du hittar strängar som slutar med ett mellanslag kan du låta det vara kvar.
- Vissa strängar kan innehålla ett mellanslag mellan det sista ordet och ett skiljetecken: lämna inte kvar det på målspråket om inte grammatiken kräver det. Till exempel bör "Kontaktuppgifter :" korrigeras till "Kontaktuppgifter:". I så fall ska du översätta det på rätt sätt. Du kan också lägga till en kommentar för att berätta för administratörerna om detta problem i den engelska originalversionen.


## Nya funktioner


- Vi arbetar på att lägga till ett avsnitt med "förklaring" för varje sträng, tillsammans med en skärmdump, för att hjälpa dig att hitta var en viss mening/ett visst ord visas på webbplatsen. Från och med nu, om du har några tvivel om vissa ord och du behöver hitta deras specifika plats på webbplatsen, kan du ställa en fråga i avsnittet "kommentarer" eller fråga översättningssamordnaren i Telegram-gruppen som nämns i början av denna handledning.

![weblate](assets/23.webp)


Tack på förhand för ditt bidrag till översättningen av Plan ₿ Network! Om du har några specifika frågor eller kommentarer till oss är du välkommen att kontakta oss via [Telegramgruppen] (https://t.me/PlanBNetwork_ContentBuilder).