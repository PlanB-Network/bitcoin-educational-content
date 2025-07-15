---
name: Lägga till en podcast i PlanB Network
description: Hur lägger jag till en ny podcast i PlanB Network?
---
![podcast](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och värd på GitHub, så att alla kan delta i att berika plattformen.


Vill du lägga till en Bitcoin-podcast på PlanB Network-webbplatsen och öka synligheten för ditt program, men vet inte hur? Denna handledning är för dig!

![podcast](assets/01.webp)


- Först måste du ha ett GitHub-konto. Om du inte vet hur du skapar ett sådant har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-förvaret för PlanB tillägnad data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) i avsnittet `resurser/podcasts/`:

![podcast](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![podcast](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, så att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![podcast](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![podcast](assets/05.webp)


- Skapa en mapp för din podcast. För att göra detta, i rutan `Namn på din fil...`, skriv namnet på din podcast i gemener med bindestreck istället för mellanslag. Om din show till exempel heter "Super Podcast Bitcoin" ska du skriva `super-podcast-Bitcoin`:

![podcast](assets/06.webp)


- Om du vill bekräfta att mappen har skapats lägger du till ett snedstreck efter podcastnamnet i samma ruta, till exempel: `super-podcast-Bitcoin/`. Om du lägger till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![podcast](assets/07.webp)


- I den här mappen skapar du en första YAML-fil med namnet `podcast.yml`:

![podcast](assets/08.webp)


- Fyll i den här filen med information om din podcast med hjälp av den här mallen:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


Här är de uppgifter som ska fyllas i för varje fält:



- `namn`**: Ange namnet på din podcast.
- `host`**: Lista namnen eller pseudonymerna på podcastens talare eller värd. Varje namn ska separeras med ett kommatecken.
- `språk`**: Ange språkkoden för det språk som talas i din podcast. Till exempel, för engelska, notera `en`, för italienska `it`...



- `länkar`**: Tillhandahåller länkar till ditt innehåll. Du har två alternativ:
 - `podcast`: länken till din podcast,
 - `twitter`: länken till Twitter-profilen för podcasten eller den organisation som producerar den,
 - `webbplats`: länken till webbplatsen för podcasten eller den organisation som producerar den.



- `Beskrivning`**: Lägg till ett kort stycke som beskriver din podcast. Beskrivningen måste vara på samma språk som anges i fältet `language:`.



- `taggar`**: Lägg till två taggar som är kopplade till din podcast. Exempel:
    - `Bitcoin`
    - teknik
    - ekonomi
    - "utbildning"...



- bidragsgivare**: Ange ditt bidragsgivar-ID om du har ett sådant.


Din YAML-fil kan till exempel se ut så här:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- När du är klar med ändringarna i den här filen sparar du dem genom att klicka på knappen `Commit changes...`:

![podcast](assets/10.webp)


- Lägg till en titel för dina ändringar samt en kort beskrivning:

![podcast](assets/11.webp)


- Klicka på knappen Green "Föreslå ändringar":

![podcast](assets/12.webp)


- Du kommer då till en sida som sammanfattar alla dina ändringar:

![podcast](assets/13.webp)


- Klicka på din GitHub-profilbild längst upp till höger och sedan på `Your Repositories`:

![podcast](assets/14.webp)


- Välj din Fork i PlanB Network-förvaret:

![podcast](assets/15.webp)


- Du bör se ett meddelande längst upp i fönstret med din nya gren. Den heter förmodligen `patch-1`. Klicka på den:

![podcast](assets/16.webp)


- Du befinner dig nu på din arbetsfilial:

![podcast](assets/17.webp)


- Gå tillbaka till mappen `resources/podcast/` och välj den podcast-mapp som du just skapade i föregående commit: ![podcast](assets/18.webp)
- I din podcastmapp klickar du på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![podcast](assets/19.webp)


- Döp den nya mappen till `assets` och bekräfta att den skapats genom att lägga till ett snedstreck `/` i slutet:

![podcast](assets/20.webp)


- I mappen `assets` skapar du en fil med namnet `.gitkeep`:

![podcast](assets/21.webp)


- Klicka på knappen `Commit changes...`:

![podcast](assets/22.webp)


- Lämna commit title som standard och se till att rutan `Commit directly to the patch-1 branch` är markerad, klicka sedan på `Commit changes`:

![podcast](assets/23.webp)


- Gå tillbaka till mappen `assets`:

![podcast](assets/24.webp)


- Klicka på knappen "Lägg till fil" och sedan på "Ladda upp filer":

![podcast](assets/25.webp)


- En ny sida kommer att öppnas. Dra och släpp din podcastlogotyp i området. Den här bilden kommer att visas på PlanB Networks webbplats:

![podcast](assets/26.webp)


- Var försiktig, bilden måste vara kvadratisk för att passa bäst på vår webbplats:

![podcast](assets/27.webp)


- När bilden har laddats upp kontrollerar du att rutan `Commit directly to the patch-1 branch` är markerad och klickar sedan på `Commit changes`:

![podcast](assets/28.webp)


- Var försiktig, din bild måste heta `logo` och måste vara i `.webp`-format. Det fullständiga filnamnet bör därför vara: `logo.webp`:

![podcast](assets/29.webp)


- Gå tillbaka till mappen `assets` och klicka på den mellanliggande filen `.gitkeep`:

![podcast](assets/30.webp)


- När du är i filen klickar du på de tre små prickarna längst upp till höger och sedan på `Delete file`:

![podcast](assets/31.webp)


- Kontrollera att du fortfarande befinner dig på samma arbetsgren och klicka sedan på knappen `Commit changes`:

![podcast](assets/32.webp)


- Lägg till en titel och en beskrivning till din ändring och klicka sedan på `Ändra ändringar`:

![podcast](assets/33.webp)


- Gå tillbaka till roten av ditt arkiv:

![podcast](assets/34.webp)


- Du bör se ett meddelande som anger att din gren har genomgått förändringar. Klicka på knappen `Jämför & dra begäran`:

![podcast](assets/35.webp)


- Lägg till en tydlig titel och beskrivning till din PR:

![podcast](assets/36.webp)


- Klicka på knappen `Create pull request`:

![podcast](assets/37.webp)

Gratulerar till din PR! Din PR har skapats på ett framgångsrikt sätt. En administratör kommer nu att granska den och, om allt är i sin ordning, sammanfoga den till PlanB Networks huvudarkiv. Du bör se din podcast visas på webbplatsen några dagar senare.


Se till att följa utvecklingen av din PR-ansökan. En administratör kan lämna en kommentar där han eller hon ber om ytterligare information. Så länge din PR inte är validerad kan du se den under fliken "Pull requests" på PlanB Network GitHub-arkivet:

![podcast](assets/38.webp)

Tack så mycket för ditt värdefulla bidrag! :)