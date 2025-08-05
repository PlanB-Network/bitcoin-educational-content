---
name: Lägga till en byggare
description: Hur föreslår jag att en ny byggare läggs till i PlanB Network?
---
![project](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser på Bitcoin, på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och finns på GitHub, vilket gör att vem som helst kan delta i att berika plattformen.


Vill du lägga till en ny Bitcoin-"byggare" på PlanB Network-webbplatsen och synliggöra ditt företag eller din programvara, men vet inte hur? Den här handledningen är för dig!

![project](assets/01.webp)


- Först måste du ha ett GitHub-konto. Om du inte vet hur du skapar ett konto har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-arkivet för PlanB som är dedikerat till data] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) i avsnittet `resources/project/`:

![project](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![project](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, vilket gör att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![project](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![project](assets/05.webp)


- Skapa en mapp för ditt företag. Det gör du genom att i rutan `Namn på filen...` skriva namnet på ditt företag med gemener och bindestreck i stället för mellanslag. Om ditt företag till exempel heter "Bitcoin Baguette" ska du skriva `Bitcoin-baguette`:

![project](assets/06.webp)


- För att bekräfta att mappen har skapats lägger du till ett snedstreck efter ditt namn i samma ruta, till exempel: `Bitcoin-baguette/`. Om du lägger till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![project](assets/07.webp)


- I den här mappen ska du skapa en första YAML-fil med namnet `project.yml`:

![project](assets/08.webp)


- Fyll i denna fil med information om ditt företag med hjälp av denna mall:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


Här är vad du ska fylla i för varje nyckel:


- `namn`: Namnet på ditt företag (obligatoriskt);
- `Address` : Plats där ditt företag är beläget (valfritt);
- `language` : De länder som ditt företag är verksamt i eller de språk som stöds (valfritt);
- `links` : De olika officiella länkarna till ditt företag (valfritt);
- `tags` : 2 termer som kvalificerar ditt företag (obligatoriskt);
- `category` : Den kategori som bäst beskriver det område inom vilket ditt företag är verksamt bland följande alternativ:
 - `Wallet`,
 - "infrastruktur",
 - `Exchange`,
 - "utbildning",
 - `tjänst`,
 - `samhällen`,
 - `konferens`,
 - "integritet",
 - "investering",
 - `node`,
 - `Mining`,
 - "Nyheter",
 - `tillverkare`.


Din YAML-fil kan till exempel se ut så här:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![project](assets/09.webp)


- När du är klar med ändringarna i den här filen sparar du dem genom att klicka på knappen `Commit changes...`:

![project](assets/10.webp)


- Lägg till en titel för dina ändringar, tillsammans med en kort beskrivning:

![project](assets/11.webp)


- Klicka på knappen Green "Föreslå ändringar":

![project](assets/12.webp)


- Du kommer då till en sida som sammanfattar alla dina ändringar:

![project](assets/13.webp)


- Klicka på din GitHub-profilbild längst upp till höger och sedan på `Your Repositories`:

![project](assets/14.webp)


- Välj din Fork i PlanB Network-förvaret:

![project](assets/15.webp)


- Du bör se ett meddelande längst upp i fönstret med din nya gren. Den heter förmodligen `patch-1`. Klicka på den:

![project](assets/16.webp)


- Du befinner dig nu på din arbetsgren (**se till att du befinner dig på samma gren som dina tidigare ändringar, detta är viktigt!**):

![project](assets/17.webp)


- Gå tillbaka till mappen `resources/projects/` och välj mappen för ditt företag som du just skapade i den föregående överföringen:

![project](assets/18.webp)


- I mappen för ditt företag klickar du på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![project](assets/19.webp)


- Döp den nya mappen till `assets` och bekräfta att den skapats genom att sätta ett snedstreck `/` i slutet:

![project](assets/20.webp)


- I mappen `assets` skapar du en fil med namnet `.gitkeep`:

![project](assets/21.webp)


- Klicka på knappen `Commit changes...`:

![project](assets/22.webp)


- Lämna commit title som standard och se till att rutan `Commit directly to the patch-1 branch` är markerad, klicka sedan på `Commit changes`: ![project](assets/23.webp)
- Gå tillbaka till mappen `assets`:

![project](assets/24.webp)


- Klicka på knappen "Lägg till fil" och sedan på "Ladda upp filer":

![project](assets/25.webp)


- En ny sida kommer att öppnas. Dra och släpp en bild av ditt företag eller din programvara i området. Denna bild kommer att visas på PlanB Network-webbplatsen:

![project](assets/26.webp)


- Det kan vara en logotyp eller en ikon:

![project](assets/27.webp)


- När bilden har laddats upp kontrollerar du att rutan `Commit directly to the patch-1 branch` är markerad och klickar sedan på `Commit changes`:

![project](assets/28.webp)


- Var försiktig, din bild måste vara kvadratisk, måste heta `logo` och måste vara i `.webp`-format. Det fullständiga filnamnet bör därför vara: `logo.webp`:

![project](assets/29.webp)


- Gå tillbaka till din `assets`-mapp och klicka på `.gitkeep` mellanfilen:

![project](assets/30.webp)


- När du är i filen klickar du på de tre små prickarna längst upp till höger och sedan på `Delete file`:

![project](assets/31.webp)


- Kontrollera att du fortfarande befinner dig på samma arbetsgren och klicka sedan på knappen `Commit changes`:

![project](assets/32.webp)


- Lägg till en titel och en beskrivning till din ändring och klicka sedan på `Ändra ändringar`:

![project](assets/33.webp)


- Gå tillbaka till ditt företags mapp:

![project](assets/34.webp)


- Klicka på knappen `Add file` och sedan på `Create new file`:

![project](assets/35.webp)


- Skapa en ny YAML-fil genom att namnge den med indikatorn för ditt modersmål. Den här filen kommer att användas för beskrivningen av byggaren. Om jag t.ex. vill skriva min beskrivning på engelska namnger jag filen `en.yml`:

![project](assets/36.webp)


- Fyll i denna YAML-fil med hjälp av denna mall:

```yaml
description: |

contributors:
-
```



- För nyckeln `contributors` kan du lägga till din identifierare för bidragsgivare till PlanB Network om du har en. Om du inte har det, lämna detta fält tomt.
- För nyckeln `description` behöver du helt enkelt lägga till ett kort stycke som beskriver ditt företag eller din programvara. Beskrivningen måste vara på samma språk som filnamnet. Du behöver inte översätta den här beskrivningen till alla språk som stöds på webbplatsen, eftersom PlanB-teamen kommer att göra det med hjälp av sin modell. Så här kan din fil till exempel se ut:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- Klicka på knappen `Commit changes`:

![project](assets/38.webp)


- Se till att rutan `Commit directly to the patch-1 branch` är markerad, lägg till en titel och klicka sedan på `Commit changes`:

![project](assets/39.webp)


- Din företagsmapp bör nu se ut så här:

![project](assets/40.webp)


- Om allt är till belåtenhet kan du återvända till roten av din Fork:

![project](assets/41.webp)


- Du bör se ett meddelande som anger att din gren har genomgått förändringar. Klicka på knappen `Jämför & dra begäran`:

![project](assets/42.webp)


- Lägg till en tydlig titel och beskrivning till din PR:

![project](assets/43.webp)


- Klicka på knappen `Create pull request`:

![project](assets/44.webp)

Gratulerar till din PR! Din PR har framgångsrikt skapats. En administratör kommer nu att granska den och, om allt är i sin ordning, integrera den i huvudarkivet för PlanB Network. Du bör se din byggarprofil visas på webbplatsen några dagar senare.


Var noga med att följa utvecklingen av din PR. En administratör kan lämna en kommentar där han eller hon ber om ytterligare information. Så länge din PR inte är validerad kan du se den under fliken "Pull requests" på PlanB Network GitHub-arkivet:

![project](assets/45.webp)

Tack så mycket för ditt värdefulla bidrag! :)
