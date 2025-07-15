---
name: Lägga till en konferensrepris
description: Hur lägger man till en konferensuppspelning på PlanB Network?
---
![conference](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla förstklassiga utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och värd på GitHub, så att alla kan bidra till plattformens berikning.


Vill du lägga till uppspelningen av din Bitcoin-konferens på PlanB Network-webbplatsen och ge synlighet åt detta evenemang, men vet inte hur? Den här handledningen är för dig!


Men om du vill lägga till en konferens som kommer att äga rum i framtiden rekommenderar jag att du läser den här andra handledningen där vi förklarar hur du lägger till ett nytt evenemang på webbplatsen.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Först måste du ha ett konto på GitHub. Om du inte vet hur du skapar ett konto har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-arkivet för PlanB tillägnad data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) i avsnittet `resurser/konferens/`:

![conference](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![conference](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, vilket gör att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![conference](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![conference](assets/05.webp)


- Skapa en mapp för din konferens. Detta gör du genom att i rutan `Namn på filen...` skriva namnet på din konferens med gemener och bindestreck i stället för mellanslag. Om din konferens till exempel heter "Paris Bitcoin Conference", skriver du `paris-Bitcoin-conference`. Lägg också till året för konferensen, till exempel: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- För att bekräfta att mappen har skapats skriver du bara ett snedstreck efter ditt namn i samma ruta, till exempel: `paris-Bitcoin-conference-2024/`. Genom att lägga till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![conference](assets/07.webp)


- I den här mappen ska du skapa en första YAML-fil med namnet `conference.yml`:

![conference](assets/08.webp)

Fyll i den här filen med information om din konferens med hjälp av den här mallen:

```yaml
year:
name:
builder:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


Din YAML-fil kan till exempel se ut så här:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Om du ännu inte har en "*builder*"-identifierare för din organisation kan du lägga till den genom att följa denna andra handledning.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- När du är klar med ändringarna i den här filen sparar du dem genom att klicka på knappen `Commit changes...`:

![conference](assets/10.webp)


- Lägg till en titel för dina ändringar samt en kort beskrivning:

![conference](assets/11.webp)


- Klicka på knappen Green "Föreslå ändringar":

![conference](assets/12.webp)


- Du kommer då till en sida som sammanfattar alla dina ändringar:

![conference](assets/13.webp)


- Klicka på din GitHub-profilbild längst upp till höger och sedan på `Your Repositories`:

![conference](assets/14.webp)


- Välj din Fork i PlanB Network-förvaret:

![conference](assets/15.webp)


- Du bör se ett meddelande längst upp i fönstret med din nya gren. Den kallas förmodligen `patch-1`. Klicka på den:

![conference](assets/16.webp)


- Du befinner dig nu på din arbetsfilial:

![conference](assets/17.webp)


- Gå tillbaka till mappen `resources/conference/` och välj mappen för din konferens som du skapade i föregående kommando:

![conference](assets/18.webp)


- I konferensmappen klickar du på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![conference](assets/19.webp)


- Döp den nya mappen till `assets` och bekräfta att den skapats genom att sätta ett snedstreck `/` i slutet:

![conference](assets/20.webp)


- I mappen `assets` skapar du en fil med namnet `.gitkeep`:

![conference](assets/21.webp)


- Klicka på knappen `Commit changes...`:

![conference](assets/22.webp)


- Lämna commit title som standard och se till att rutan `Commit directly to the patch-1 branch` är markerad, klicka sedan på `Commit changes`:

![conference](assets/23.webp)


- Gå tillbaka till mappen `assets`:

![conference](assets/24.webp)


- Klicka på knappen "Lägg till fil" och sedan på "Ladda upp filer":

![conference](assets/25.webp)


- En ny sida kommer att öppnas. Dra och släpp en bild som representerar din konferens och som kommer att visas på PlanB Network-webbplatsen: ![konferens](assets/26.webp)
- Det kan vara en logotyp, en miniatyrbild eller till och med en affisch:

![conference](assets/27.webp)


- När bilden har laddats upp kontrollerar du att rutan `Commit directly to the patch-1 branch` är markerad och klickar sedan på `Commit changes`:

![conference](assets/28.webp)


- Var försiktig, din bild måste heta `thumbnail` och måste vara i `.webp`-format. Det fullständiga filnamnet bör därför vara: `thumbnail.webp`:

![conference](assets/29.webp)


- Gå tillbaka till din mapp `assets` och klicka på mellanfilen `.gitkeep`:

![conference](assets/30.webp)


- När du är i filen klickar du på de 3 små prickarna i det övre högra hörnet och sedan på `Delete file`:

![conference](assets/31.webp)


- Kontrollera att du fortfarande befinner dig på samma arbetsgren och klicka sedan på knappen `Commit changes`:

![conference](assets/32.webp)


- Lägg till en titel och en beskrivning till din ändring och klicka sedan på `Ändra ändringar`:

![conference](assets/33.webp)


- Gå tillbaka till din konferensmapp:

![conference](assets/34.webp)


- Klicka på knappen `Add file` och sedan på `Create new file`:

![conference](assets/35.webp)


- Skapa en ny markdown-fil (.md) genom att namnge den med indikatorn för ditt modersmål. Den här filen kommer att användas för repriserna av din konferens. Om jag t.ex. vill skriva beskrivningarna av konferenserna på engelska, namnger jag filen en.md:

![conference](assets/36.webp)


- Fyll i den här markdown-filen med hjälp av den här mallen som du kan anpassa till konfigurationen för din konferens:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- I början av dokumentet, i "front matter", fyller du i fältet "name" med namnet på din konferens och året för repriserna. I fältet `description:` skriver du en kort beskrivning av ditt evenemang på filens språk. För en fil med namnet `en.md` ska beskrivningen till exempel vara på engelska. PlanB Network-teamet kommer att översätta din beskrivning med hjälp av sin modell.
- Titlar på första nivån, markerade med en `#`, används för att organisera konferensen efter scener. Till exempel `# Main Stage` för huvudscenen och `# Workshop Room` för en scen som är avsedd för workshops.



- Titlar på andra nivån, markerade med en dubbel `##`, används för att skilja de olika videofilmerna åt. Om konferenserna filmades kontinuerligt under en halvdag, ange till exempel `## fredag morgon`. Om konferenserna filmades och sändes individuellt, namnge konferensen direkt med en andra gradens titel.



- Under varje titel på andra nivån infogar du en länk till motsvarande reprisvideo. Syntaxen bör vara: `![video](https://youtu.be/XXXXXXXXXXXX)`, där `XXXXXXXXXXXX` ersätts med den faktiska videolänken.



- Om formatet tillåter det (enskilda konferenser) kan du lägga till namnen på talarna. Detta gör du genom att lägga till fältet `Speaker:` följt av namnet eller pseudonymen på talaren under videolänken. Om det finns flera talare separerar du varje namn med ett kommatecken, till exempel så här: `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- När ändringarna i den här filen är klara sparar du dem genom att klicka på knappen `Commit changes...`:

![conference](assets/38.webp)


- Lägg till en titel för dina ändringar samt en kort beskrivning:

![conference](assets/39.webp)


- Klicka på `Kommittera ändringar`:

![conference](assets/40.webp)


- Din konferensmapp bör nu se ut så här:

![conference](assets/41.webp)


- Om allt är till belåtenhet kan du återvända till roten till din Fork:

![conference](assets/42.webp)


- Du bör se ett meddelande som anger att din gren har genomgått ändringar. Klicka på knappen `Jämför & dra begäran`:

![conference](assets/43.webp)


- Lägg till en tydlig titel och beskrivning för din PR:

![conference](assets/44.webp)


- Klicka på knappen `Create pull request`:

![conference](assets/45.webp)

Gratulerar till din PR! Din PR har skapats på ett framgångsrikt sätt. En administratör kommer nu att granska den och, om allt är i sin ordning, sammanfoga den till PlanB Networks huvudarkiv. Du bör se repriserna av din konferens på webbplatsen några dagar senare.


Se till att följa utvecklingen av din PR. Det är möjligt att en administratör kan lämna en kommentar och be om ytterligare information. Så länge din PR inte är validerad kan du se den under fliken `Pull requests` på PlanB-nätverkets GitHub-arkiv:

![conference](assets/46.webp)


Tack så mycket för ditt värdefulla bidrag! :)