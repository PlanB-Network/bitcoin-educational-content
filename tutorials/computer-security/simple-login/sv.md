---
name: Enkel inloggning
description: Identitet skyddad med alias
---
![cover](assets/cover.webp)

## Inloggning = e-post = förlust av integritet


I den digitala världen har det blivit standard att ha ett konto för varje plattform som man vill ha tillgång till.

Var och en av dessa tjänster kräver en inloggning, som vanligtvis är kopplad till paret _användarnamn_ och _lösenord_. Ofta är användarnamnet användarens personliga e-postadress.


När man använder sin personliga e-post Address för varje inloggning är det lätt att föreställa sig den första konsekvensen: förlust av sekretess, vilket blir större om Address består av _name.surname@serviceemail.com_.


Utvecklare av verktyg med öppen källkod har skapat en rad programsviter som är skapade just för att användarna ska få tillbaka lite av sin integritet: de kommer fortfarande att logga in, men med ett alias istället för med det verktyg som avslöjar deras privata identitet.


Den enklaste av dem som jag personligen har provat och fortfarande testar är [Simple Login] (https://simplelogin.io/).


## Alias


Ett e-postalias ersätter helt enkelt delen _namn.efternamn_ i din e-post Address med ett fiktivt namn. För användaren förändras ingenting; alias-tjänsten vidarebefordrar e-postmeddelanden till och från den vanliga Address som vanligt. Alla kan fortsätta att använda sin inkorg som vanligt, men istället för att visa sitt riktiga namn kommer det att visa en oigenkännlig användare. Den här tjänsten måste vara effektiv, och hittills har Simple Login visat sig vara just det.


När du besöker Simple Login-webbplatsen för första gången måste du skapa ett konto (här också!) Med hjälp av den "officiella" e-postadressen Address. Här måste du ange e-postmeddelandet, ett lösenord och lösa en captcha.


![image](assets/it/02.webp)


Simple Login skickar ett verifieringsmeddelande till den angivna e-postadressen Address. Istället för att klicka på verifieringsknappen är det lämpligt att kopiera länken och klistra in den i Address-fältet.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Instrumentpanelen för Simple Login öppnas omedelbart med en kort handledning för navigering.


![image](assets/it/05.webp)


Det bör noteras att Simple Login automatiskt aktiverar prenumerationen på nyhetsbrevet, som kan avaktiveras från lämpligt kommando.


![image](assets/it/06.webp)


## Inställningar


Du kan ta en titt på _Settings_ direkt för att upptäcka tjänstens funktioner. Simple Login startar med alla alternativ aktiva, inklusive _Premium_, som är användbara i 10 dagar. När testperioden är över kommer du att ha möjlighet att skapa 10 alias med den här profilen och du kan direkt länka din Proton-e-post, eftersom Simple Login har förvärvats av den schweiziska e-postleverantören.


![image](assets/it/07.webp)


Du kan ställa in en rad parametrar eller kontrollera om din e-post redan har äventyrats när det gäller sekretess.


![image](assets/it/08.webp)


Slutligen kan du exportera en säkerhetskopia av din profil eller importera en från en annan leverantör.


![image](assets/it/09.webp)


### E-post på jobbet


De som använder e-post med en personlig domän som arbetsmejl kan konfigurera sin privata domän.


![image](assets/it/10.webp)


Från huvudpanelen, genom att välja _Mailboxes_, är det till och med möjligt att lägga till andra e-postadresser och även använda de alias som kommer att skapas i enlighet därmed. I den här handledningen bestämde jag mig till exempel för att skapa profilen med en _gmail.com_-brevlåda och sedan associera en _proton.me_ Address.


![image](assets/it/11.webp)


Genom att lägga till en ny Address, särskilt om den tillhör Proton-leverantören, visar den guidade proceduren möjligheten att gå in i _sudo_-läge, superanvändare. Enkel inloggning kommer att be om att få ange lösenordet för den här brevlådan, för att bevisa att Ownership är legitimt.


⚠️ **Jag avråder personligen från att göra detta**. ⚠️


![image](assets/it/12.webp)


** Det är bättre att komma åt e-postrutan -> kopiera länken för verifiering och klistra in den i URL-fältet -> och få verifieringen utan att avslöja lösenordet.**


![image](assets/it/13.webp)


Av de två adresser som anges blir den ena standard och den andra sekundär, men de kan enkelt bytas ut och inställningen är lätt att identifiera i instrumentpanelen.


![image](assets/it/14.webp)


Efter att ha lagt till ett andra e-postmeddelande Address (valfritt), låt oss se vad vi kan göra med Simple Login.


## Skapande av alias


I panelen är det första menyalternativet märkt _Alias_, och det är där du kan skapa dem. Du har möjlighet att generate alias slumpmässigt genom att klicka på Random Alias-knappen, som är Green-knappen som visas på nästa foto. Den här funktionen skapar ett unikt och spännande e-postmeddelande Address.


![image](assets/it/24.webp)


Om du däremot vill differentiera tjänsterna genom att ge dem olika namn måste du välja _New Custom Alias_. På så sätt kan du ge aliaset namnet på den tjänst som du vill ha tillgång till (sociala medier, tjänsteleverantörer, online-evenemang, främlingar som träffats av en slump etc.) Resten sköts av Simple Login.

För skojs skull (men inte riktigt, för att säga sanningen) bestämde jag mig för att skapa ett alias för banken och kallade det `BANK`. Även om det är sant att min bank vet allt om mig, tycker jag att det är roligt att kommunicera med dem med hjälp av ett e-postmeddelande Address som är obegripligt för dem. Simple Login genererar faktiskt ett slumpmässigt namn, som separeras från det vi väljer med ett `.`


Här kan den nya e-postadressen Address bli:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- och så vidare


Man kan välja mer än en domän: publika domäner är tillgängliga med gratisplanen, medan andra, som anges som privata (inklusive _@simplelogin.com_), utökar valet för användare som väljer att prenumerera på en betalplan.


![image](assets/it/15.webp)


När det slumpmässiga suffixet och domänen har valts kan du ställa in om denna nya (och bisarra) Address ska fungera som ett alias för bara en av de personliga e-postlådorna eller för alla. Aliaset blir klart och aktivt efter att du klickat på _Create_


![image](assets/it/16.webp)


Det nya e-postmeddelandet Address skapades och det är nu synligt, redo att skickas (till banken!) genom att helt enkelt kopiera det.


![image](assets/it/18.webp)


Nu kan du fokusera på att skapa ett alias för varje tjänst eller plattform som du vill ha tillgång till och där e-post krävs som en viktig parameter för att skapa ett konto.


![image](assets/it/19.webp)


För integritetsentusiaster finns det också möjlighet att generate ett e-postmeddelande Address baserat på UUID-protokollet (inte på identifierbara namn), vilket skapar en unik 128-bitars identifierare som inte kontrolleras av centraliserade parter. Den här funktionen, som är användbar för känsliga konton, finns i menyn _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Som du kan se är detta ett Address-meddelande som kräver korrekt hantering.


Om du ändrar dig och inte längre vill använda ett alias klickar du bara på kommandot _More_ för varje enskilt alias och väljer _Delete_.


![image](assets/it/23.webp)


## Alias-hantering


Att skapa alias är enkelt, liksom hanteringen av dem, vilket bara kräver lite omsorg och disciplin. All trafik kommer faktiskt fortfarande att passera genom den e-postinkorg som vi i början har definierat som den officiella. Meddelanden och viktig kommunikation från plattformar kommer att fortsätta att anlända till Gmail, Proton eller vilken e-postleverantör du än har.


Resultatet är dock att vi har bevarat den viktigaste Address som vi, från det ögonblick då alias skapas, fritt kan bestämma vem vi ska avslöja den för och vem inte.


Ett alias fungerar både för mottagning och sändning: en annan användare kommer att få svaret från alias.preoccupy789@8shield.net, om detta är den pseudonym som valts för just den mottagaren.


## Proffs


Att använda alias är ett effektivt sätt att skydda din identitet och integritet. E-postadresser samlas ofta in av datamäklare och webbplatser för att spåra användarnas vanor och beteenden. Även om ett alias inte gör dig helt ospårbar är det ett positivt steg mot att skydda din information om du konsekvent använder ett. I vår "globala digitala by", där hacking, dataförsäljning och säkerhetsbrister är alltför vanliga, är det dessutom mycket troligt att den e-postadress du använder för att registrera dig på olika webbplatser redan har äventyrats eller utsatts för angrepp.


En unik pseudonym, som används för varje inloggning, **gör det omedelbart möjligt för oss att förstå vilken plattform som skickar skräppost (eller värre) till vår brevlåda, eftersom e-postmeddelandet identifieras av det alias som är kopplat till det**. Du har ingen aning om hur mycket skräppost och nätfiske som kommer från så kallade tillförlitliga kanaler, eftersom de är institutionella, förrän du börjar använda ett alias för banker, ett för posttjänster eller ett specifikt för vissa obligatoriska myndighetstjänster. När avsändaren av skräpposten (eller ännu värre) har identifierats vet du att den webbplatsen har äventyrats och vidtar alla försiktighetsåtgärder för att skydda alla uppgifter som lämnas (tänk på kreditkort!) till den specifika webbplatsen, som kanske inser intrånget veckor senare.


När det gäller Simple Login har detta verktyg följande funktioner:



- mobilapp (även från F-Droid) och webbläsartillägg, för att hantera alias i alla situationer;
- tvåfaktorsautentisering för varje ny pseudonym, vilket ökar graden av oberoende från själva tjänsten;
- PGP-stöd (för _Premium-användare);
- enkelt skapande av alla typer av alias (anpassade, slumpmässiga och UUID);
- bland de kostnadsfria planerna i sektorn, möjligheten att använda alias med fler "officiella" e-postlådor. Andra konkurrenter begränsar sig till bara en.


## Nackdelar


- 10 alias kanske inte räcker om du planerar att använda Simple Login i stor utsträckning. I det här fallet är den betalda planen, som är ganska överkomlig, användbar för att öka antalet möjliga alias som är tillgängliga.
- Det går inte att skapa ett alias med ett specifikt namn och en specifik domän. Det slumpmässiga suffixet, som läggs till efter ett namn som vi valt, genererar en Address som i bästa fall kan beskrivas som bisarr. Traditionella sociala medier vägrar vanligtvis att bevilja konton som skapats med den här typen av e-postadresser. Nostr fixar detta!
- Om du använder ett alias för att skicka ett meddelande till någon är det lätt hänt att det hamnar i mottagarens skräppostmapp. Som ett första steg är det lämpligt att använda pseudonymen för att ta emot, precis som när du skapar ett konto, prenumererar på en e-postlista etc.