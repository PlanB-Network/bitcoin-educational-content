---
name: Lägga till en bok i PlanB Network
description: Hur lägger man till en ny bok i PlanB Network?
---
![book](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och värd på GitHub, så att alla kan bidra till att berika plattformen.


**Vill du lägga till en bok relaterad till Bitcoin på PlanB Network-webbplatsen och öka synligheten för ditt arbete, men vet inte hur? Den här handledningen är för dig!**

![book](assets/01.webp)


- Först måste du ha ett GitHub-konto. Om du inte vet hur du skapar ett konto har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-arkivet för PlanB tillägnad data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) i avsnittet `resources/books/`:

![book](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![book](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, så att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![book](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![book](assets/05.webp)


- Skapa en mapp för din bok. Det gör du genom att i rutan `Namn på filen...` skriva bokens namn med små bokstäver och bindestreck i stället för mellanslag. Om din bok till exempel heter "*Min Bitcoin-bok*" ska du skriva `min-Bitcoin-bok`:

![book](assets/06.webp)


- För att bekräfta att mappen har skapats lägger du till ett snedstreck efter boknamnet i samma ruta, till exempel: `my-Bitcoin-book/`. Om du lägger till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![book](assets/07.webp)


- I den här mappen skapar du en första YAML-fil med namnet `book.yml`:

![book](assets/08.webp)


- Fyll i den här filen med information om din bok med hjälp av den här mallen:


```yaml
author:
level:
tags:
-
-
```


Här är de uppgifter som ska fyllas i för varje fält:


- `författare`**: Ange namnet på bokens författare.
- nivå**: Ange den nivå som krävs för att kunna läsa och förstå boken på ett bra sätt. Välj en nivå bland följande:
 - "nybörjare
 - "mellanliggande
- "avancerad" - "expert
- `taggar`**: Lägg till två eller tre taggar som är relaterade till din bok. Till exempel:
    - `Bitcoin`
    - `historia`
    - teknik
    - ekonomi
    - "utbildning"...


Din YAML-fil kan till exempel se ut så här:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- När du är klar med ändringarna i den här filen sparar du dem genom att klicka på knappen `Commit changes...`:

![book](assets/10.webp)


- Lägg till en titel för dina ändringar samt en kort beskrivning:

![book](assets/11.webp)


- Klicka på knappen Green "Föreslå ändringar":

![book](assets/12.webp)


- Du kommer då till en sida som sammanfattar alla dina ändringar:

![book](assets/13.webp)


- Klicka på din GitHub-profilbild längst upp till höger och sedan på `Your Repositories`:

![book](assets/14.webp)


- Välj din Fork i PlanB Network-förvaret:

![book](assets/15.webp)


- Du bör se ett meddelande längst upp i fönstret med din nya gren. Den heter förmodligen `patch-1`. Klicka på den:

![book](assets/16.webp)


- Du befinner dig nu på din arbetsfilial:

![book](assets/17.webp)


- Gå tillbaka till mappen `resources/books/` och välj mappen för din bok som du just skapade i föregående kommando:

![book](assets/18.webp)


- I mappen för din bok klickar du på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![book](assets/19.webp)


- Döp den nya mappen till `assets` och bekräfta att den skapats genom att sätta ett snedstreck `/` i slutet:

![book](assets/20.webp)


- I mappen `assets` skapar du en fil med namnet `.gitkeep`:

![book](assets/21.webp)


- Klicka på knappen `Commit changes...`:

![book](assets/22.webp)


- Lämna commit title som standard och se till att rutan `Commit directly to the patch-1 branch` är markerad, klicka sedan på `Commit changes`:

![book](assets/23.webp)


- Gå tillbaka till mappen `assets`:

![book](assets/24.webp)


- Klicka på knappen "Lägg till fil" och sedan på "Ladda upp filer":

![book](assets/25.webp)


- En ny sida öppnas. Dra och släpp omslagsbilden för din bok i området. Denna bild kommer att visas på PlanB Network-webbplatsen:

![book](assets/26.webp)


- Var försiktig, bilden måste vara i bokformat för att bäst anpassas till vår webbplats, som till exempel:

![book](assets/27.webp)


- När bilden har laddats upp, se till att rutan `Commit directly to the patch-1 branch` är markerad och klicka sedan på `Commit changes`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Gå tillbaka till din `assets`-mapp och klicka på `.gitkeep` mellanfilen:

![book](assets/30.webp)


- När du är i filen klickar du på de 3 små prickarna längst upp till höger och sedan på `Delete file`:

![book](assets/31.webp)


- Se till att du fortfarande befinner dig på samma arbetsgren och klicka sedan på knappen `Commit changes...`:

![book](assets/32.webp)


- Lägg till en titel och en beskrivning till din ändring och klicka sedan på `Ändra ändringar`:

![book](assets/33.webp)


- Gå tillbaka till din boks mapp:

![book](assets/34.webp)


- Klicka på knappen `Add file` och sedan på `Create new file`:

![book](assets/35.webp)


- Skapa en ny YAML-fil genom att namnge den med bokens språkindikator. Den här filen kommer att användas för bokens beskrivning. Om jag t.ex. vill skriva min beskrivning på engelska namnger jag filen `en.yml`:

![book](assets/36.webp)


- Fyll i denna YAML-fil med hjälp av denna mall:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


Här är de uppgifter som ska fyllas i för varje fält:


- `title`**: Ange bokens namn inom citationstecken.
- `publication_year`**: Anger det år boken publicerades.
- `cover`**: Ange namnet på den fil som motsvarar omslagsbilden, i enlighet med språket i den YAML-fil som du för närvarande redigerar. Om du t.ex. redigerar filen `en.yml` och du tidigare har lagt till den engelska omslagsbilden med titeln `cover_en.webp`, anger du bara `cover_en.webp` i det här fältet.
- `Beskrivning`**: Lägg till ett kort stycke som beskriver boken. Beskrivningen måste vara på samma språk som anges i titeln på YAML-filen.
- `bidragsgivare`**: Lägg till ditt bidragsgivar-ID om du har ett.


Din YAML-fil kan till exempel se ut så här:


```yaml