---
name: Lägg till ett evenemang på PlanB Network
description: Hur föreslår jag att man lägger till ett nytt evenemang på PlanB Network?
---
![event](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och värd på GitHub, vilket ger alla möjlighet att bidra till berikningen av plattformen.


Om du vill lägga till en Bitcoin-konferens på PlanB Network-webbplatsen och öka synligheten för ditt evenemang, men inte vet hur? Den här handledningen är för dig!

![event](assets/01.webp)


- Först måste du ha ett konto på GitHub. Om du inte vet hur du skapar ett konto har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-arkivet för PlanB tillägnad data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) i avsnittet `resurser/konferens/`:

![event](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![event](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, så att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![event](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![event](assets/05.webp)


- Skapa en mapp för din konferens. Detta gör du genom att i rutan `Namn på filen...` skriva namnet på din konferens med gemener och bindestreck i stället för mellanslag. Om din konferens till exempel heter "Paris Bitcoin Conference", skriver du `paris-Bitcoin-conference`. Lägg också till året för konferensen, till exempel: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- För att bekräfta att mappen har skapats skriver du bara ett snedstreck efter ditt namn i samma ruta, till exempel: `paris-Bitcoin-conference-2024/`. Genom att lägga till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![event](assets/07.webp)


- I den här mappen ska du skapa en första YAML-fil med namnet `events.yml`:

![event](assets/08.webp)


- Fyll i denna fil med information om din konferens med hjälp av denna mall:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
builder:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


Din YAML-fil kan till exempel se ut så här:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Om du ännu inte har en "*builder*"-identifierare för din organisation kan du lägga till den genom att följa denna andra handledning.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- När du är klar med ändringarna i den här filen sparar du dem genom att klicka på knappen `Commit changes...`:

![event](assets/10.webp)


- Lägg till en titel för dina ändringar samt en kort beskrivning:

![event](assets/11.webp)


- Klicka på knappen Green "Föreslå ändringar":

![event](assets/12.webp)


- Du kommer då till en sida som sammanfattar alla dina ändringar:

![event](assets/13.webp)


- Klicka på din GitHub-profilbild längst upp till höger och sedan på `Your Repositories`:

![event](assets/14.webp)


- Välj din Fork i PlanB Network-förvaret:

![event](assets/15.webp)


- Du bör se ett meddelande längst upp i fönstret med din nya gren. Den heter förmodligen `patch-1`. Klicka på den:

![event](assets/16.webp)


- Du befinner dig nu på din arbetsfilial:

![event](assets/17.webp)


- Gå tillbaka till mappen `resources/conference/` och välj mappen för din konferens som du just skapade i den föregående överföringen:

![event](assets/18.webp)


- I konferensmappen klickar du på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![event](assets/19.webp)


- Döp den nya mappen till `assets` och bekräfta att den skapats genom att sätta ett snedstreck `/` i slutet:

![event](assets/20.webp)


- I mappen `assets` skapar du en fil med namnet `.gitkeep`:

![event](assets/21.webp)


- Klicka på knappen `Commit changes...`:

![event](assets/22.webp)


- Lämna commit title som standard och se till att rutan `Commit directly to the patch-1 branch` är markerad, klicka sedan på `Commit changes`:

![event](assets/23.webp)


- Gå tillbaka till mappen `assets`:

![event](assets/24.webp)


- Klicka på knappen "Lägg till fil" och sedan på "Ladda upp filer": ![event](assets/25.webp)
- En ny sida kommer att öppnas. Dra och släpp en bild som representerar din konferens och som kommer att visas på PlanB Network-webbplatsen:

![event](assets/26.webp)


- Det kan vara logotypen, en miniatyrbild eller till och med en affisch:

![event](assets/27.webp)


- När bilden har laddats upp kontrollerar du att rutan `Commit directly to the patch-1 branch` är ikryssad och klickar sedan på `Commit changes`:

![event](assets/28.webp)


- Var försiktig, din bild måste heta `thumbnail` och måste vara i `.webp`-format. Det fullständiga filnamnet bör därför vara: `thumbnail.webp`:

![event](assets/29.webp)


- Gå tillbaka till mappen `assets` och klicka på den mellanliggande filen `.gitkeep`:

![event](assets/30.webp)


- När du är i filen klickar du på de 3 små prickarna längst upp till höger och sedan på `Delete file`:

![event](assets/31.webp)


- Kontrollera att du fortfarande befinner dig på samma arbetsgren och klicka sedan på knappen `Commit changes`:

![event](assets/32.webp)


- Lägg till en titel och en beskrivning till din ändring och klicka sedan på `Ändra ändringar`:

![event](assets/33.webp)


- Gå tillbaka till roten av ditt arkiv:

![event](assets/34.webp)


- Du bör se ett meddelande som anger att din gren har genomgått förändringar. Klicka på knappen `Jämför & dra begäran`:

![event](assets/35.webp)


- Lägg till en tydlig titel och en beskrivning till din PR:

![event](assets/36.webp)


- Klicka på knappen `Create pull request`:

![event](assets/37.webp)

Gratulerar till din PR! Din PR har skapats framgångsrikt. En administratör kommer nu att kontrollera den och, om allt är i sin ordning, sammanfoga den till PlanB Networks huvudarkiv. Du bör se ditt evenemang visas på webbplatsen några dagar senare.


Var noga med att följa utvecklingen av din PR. En administratör kan lämna en kommentar där han eller hon ber om ytterligare information. Så länge din PR inte är validerad kan du se den under fliken "Pull requests" på PlanB Network GitHub-arkivet:

![event](assets/38.webp)

Tack så mycket för ditt värdefulla bidrag! :)