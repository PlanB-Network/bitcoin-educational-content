---
name: Bidrag - GitHub Webbhandledning (nybörjare)
description: Komplett guide till Plan ₿ Network-handledning med GitHub Web
---
![cover](assets/cover.webp)


Innan du följer denna handledning om hur du lägger till en ny handledning måste du ha slutfört några inledande steg. Om du inte redan har gjort det kan du först läsa den här inledande handledningen och sedan komma tillbaka hit:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Du har redan:




- Välj ett tema för din handledning;
- Kontaktade Plan ₿ Network-teamet via [Telegramgrupp](https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network ;
- Välj dina bidragsverktyg.


I den här handledningen tittar vi på hur du lägger till din handledning i Plan ₿ Network med hjälp av webbversionen av GitHub. Om du redan har behärskat Git kanske denna mycket detaljerade handledning inte är nödvändig för dig. Istället rekommenderar jag att du kollar in en av dessa andra 2 tutorials, där jag beskriver de riktlinjer som ska följas och stegen för att göra ändringar från en lokal:




- Erfarna användare**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- Mellanliggande (GitHub Desktop)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Förkunskapskrav


Förutsättningar innan du påbörjar handledningen:




- Har ett [GitHub-konto] (https://github.com/signup);
- Ha en Fork av [Plan ₿ Network-källförvaret] (https://github.com/PlanB-Network/Bitcoin-educational-content);
- Har [en lärarprofil på Plan ₿ Network] (https://planb.network/professors) (endast om du erbjuder en fullständig handledning).


Om du behöver hjälp med att få dessa förutsättningar, kommer mina andra handledningar att hjälpa dig:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

När allt är på plats och du har din Fork av Plan ₿ Network-repository kan du börja lägga till handledningen.


## 1 - Skapa en ny filial


Öppna din webbläsare och navigera till din Fork-sida i Plan ₿ Network-förvaret. Detta är den Fork som du etablerade på GitHub. URL:en till din Fork ska se ut så här: `https://github.com/[ditt-användarnamn]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


Se till att du befinner dig på huvudgrenen `dev` och klicka sedan på knappen "*Sync Fork*". Om din Fork inte är uppdaterad kommer GitHub att be dig att uppdatera din gren. Fortsätt med den här uppdateringen:


![GITHUB](assets/fr/02.webp)


Klicka på grenen `dev` och namnge sedan din arbetsgren så att dess titel tydligt återspeglar dess syfte och använd bindestreck för att separera ord. Om vårt mål till exempel är att skriva en handledning om hur man använder Green Wallet, kan grenen kallas: `tuto-Green-Wallet-loic`. När du har angett ett lämpligt namn klickar du på "*Create branch*" för att bekräfta skapandet av din nya gren baserad på `dev`:


![GITHUB](assets/fr/03.webp)


Du bör nu befinna dig på din nya arbetsplats:


![GITHUB](assets/fr/04.webp)


Det innebär att alla ändringar som du gör bara sparas på den specifika grenen.


För varje ny artikel som du planerar att publicera skapar du en ny gren från `dev`.


En gren i Git representerar en parallell version av projektet, vilket gör att du kan arbeta med ändringar utan att påverka huvudgrenen, tills ditt arbete är klart att integreras.


## 2 - Lägg till handledningsfiler


Nu när arbetsgrenen har skapats är det dags att integrera den nya handledningen.


I dina grenfiler måste du hitta den lämpliga undermappen för placeringen av din handledning. Mapparnas organisation återspeglar de olika avsnitten på Plan ₿ Network-webbplatsen. I vårt exempel, eftersom vi lägger till en handledning om Green Wallet, ska du gå till följande sökväg: `Bitcoin-educational-content\tutorials\Wallet` som motsvarar avsnittet `Wallet` på webbplatsen:


![GITHUB](assets/fr/05.webp)


I mappen `Wallet` skapar du en ny katalog som är särskilt avsedd för din handledning. Namnet på den här mappen ska tydligt ange den programvara som behandlas i handledningen och använda bindestreck för att koppla samman ord. I mitt exempel kommer mappen att heta `Green-Wallet`. Klicka på "*Add File*" och sedan på "*Create new file*":


![GITHUB](assets/fr/06.webp)


Ange mappens namn följt av ett snedstreck `/` för att bekräfta att den skapats som en mapp.


![GITHUB](assets/fr/07.webp)


I den här nya undermappen som är avsedd för din handledning måste du lägga till flera objekt:




- Skapa en mapp med namnet "Assets" där du kan spara alla illustrationer som behövs för din handledning;
- I mappen `assets` skapar du en undermapp med namn enligt handledningens ursprungliga språkkod. Om handledningen t.ex. är skriven på engelska ska undermappen heta "en". Placera alla handledningens visuella element (diagram, bilder, skärmdumpar etc.) i den här mappen.
- En fil `tutorial.yml` måste skapas för att registrera detaljerna i din handledning;
- En markdown-fil måste skapas för att skriva det faktiska innehållet i din handledning. Denna fil måste namnges enligt koden för det språk som den är skriven på. För en handledning som är skriven på franska ska filen till exempel heta `fr.md`.


Sammanfattningsvis är detta filhierarkin (vi fortsätter att skapa dem i nästa avsnitt):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - Fyll i YAML-filen


Låt oss börja med YAML-filen. I rutan för att skapa en ny fil skriver du in `tutorial.yml`:


![GITHUB](assets/fr/08.webp)


Fyll i filen `tutorial.yml` genom att kopiera följande mall:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Här är de obligatoriska fälten:



- id**: En UUID (_Universally Unique Identifier_) som identifierar handledningen på ett unikt sätt. Du kan generate det med hjälp av [ett onlineverktyg] (https://www.uuidgenerator.net/version4). Det enda kravet är att detta UUID är slumpmässigt för att undvika konflikter med ett annat UUID på plattformen;



- projekt_id**: UUID för företaget eller organisationen bakom det verktyg som presenteras i handledningen [från projektlistan] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Om du t.ex. skapar en handledning om programvaran Green Wallet hittar du detta `project_id` i följande fil: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Den här informationen läggs till i din handlednings YAML-fil eftersom Plan ₿ Network upprätthåller en databas över alla företag och organisationer som arbetar med Bitcoin eller relaterade projekt. Genom att lägga till `project_id` för den enhet som är länkad till din handledning skapar du en länk mellan de två Elements;



- taggar**: 2 eller 3 relevanta nyckelord relaterade till handledningens innehåll, uteslutande valda [från Plan ₿ Network:s tagglista] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategori**: Den underkategori som motsvarar innehållet i handledningen, enligt Plan ₿ Network:s webbplatsstruktur (t.ex. för plånböcker: "Desktop", "Hardware", "Mobile", "Backup");



- nivå**: Handledningens svårighetsgrad, vald från:
    - "nybörjare
    - "mellanliggande
    - "Avancerad
    - "expert



- professor_id**: Ditt `professor_id` (UUID) som visas på [din professorsprofil] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- original_language**: Handledningens originalspråk (t.ex. `fr`, `en`, etc.);



- korrekturläsning**: Information om korrekturläsningsprocessen. Slutför den första delen, eftersom korrekturläsning av din egen handledning räknas som en första validering:
    - språk**: Språkkod för korrekturläsningen (t.ex. `fr`, `en`, etc.).
    - last_contribution_date**: Datum för dagen.
    - brådskande**: 1
    - bidragsgivarens_namn**: Ditt GitHub-ID.
    - belöning**: 0


För mer information om ditt lärar-ID, se motsvarande handledning:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


När du är klar med att ändra filen `tutorial.yml` sparar du dokumentet genom att klicka på knappen "*Commit changes...*":


![GITHUB](assets/fr/09.webp)


Lägg till en titel och en beskrivning och se till att överföringen görs till den gren som du skapade i början av denna handledning. Bekräfta sedan genom att klicka på "*Commit changes*".


![GITHUB](assets/fr/10.webp)


## 4 - Skapa undermappar för bilder


Klicka på "*Add File*" igen och sedan på "*Create new file*":


![GITHUB](assets/fr/11.webp)


Ange `assets` följt av ett snedstreck `/` för att skapa mappen:


![GITHUB](assets/fr/12.webp)


Upprepa detta steg i mappen `/assets` för att skapa undermappen för språket, t.ex. `fr` om din handledning är på franska:


![GITHUB](assets/fr/13.webp)


I den här mappen skapar du en dummyfil för att tvinga GitHub att behålla din mapp (som annars skulle vara tom). Namnge den här filen `.gitkeep`. Klicka sedan på "*Commit changes...*".


![GITHUB](assets/fr/14.webp)


Kontrollera igen att du befinner dig på rätt gren och klicka sedan på "*Commit changes*".


![GITHUB](assets/fr/15.webp)


## 5 - Skapa Markdown-filen


Nu ska vi skapa den fil som ska vara värd för din handledning, med namn enligt din språkkod, till exempel `fr.md` om vi skriver på franska. Gå till din handledningsmapp:


![GITHUB](assets/fr/16.webp)


Klicka på "Lägg till fil*" och sedan på "Skapa ny fil*".


![GITHUB](assets/fr/17.webp)


Namnge filen med hjälp av din språkkod. I mitt fall, eftersom handledningen är skriven på franska, namnger jag min fil `fr.md`. Tillägget `.md` indikerar att filen är i Markdown-format.


![GITHUB](assets/fr/18.webp)


Vi börjar med att fylla i avsnittet `Properties` högst upp i dokumentet. Lägg till och fyll i följande kodblock manuellt (nycklarna `name:` och `description:` måste vara på engelska, men deras värden måste skrivas på det språk som används för din handledning):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Fyll i namnet på din handledning och en kort beskrivning:


![GITHUB](assets/fr/20.webp)


Lägg sedan till sökvägen till omslagsbilden i början av din handledning. För att göra detta, notera:


```
![cover-green](assets/cover.webp)
```


Denna syntax kommer väl till pass när du behöver lägga till en bild i din handledning. Utropstecknet anger en bild, vars alternativa text (alt) anges mellan hakparenteserna. Sökvägen till bilden anges mellan parenteserna:


![GITHUB](assets/fr/21.webp)


Klicka på knappen "*Commit changes...*" för att spara filen.


![GITHUB](assets/fr/22.webp)


Kontrollera att du befinner dig på rätt gren och bekräfta sedan överföringen.


![GITHUB](assets/fr/23.webp)


Din tutorial-mapp ska nu se ut så här, beroende på din språkkod:


![GITHUB](assets/fr/24.webp)


## 6 - Lägg till logotyp och omslag


I mappen `assets` måste du lägga till en fil med namnet `logo.webp`, som kommer att fungera som miniatyrbild för din artikel. Bilden måste vara i formatet `.webp` och ha kvadratisk storlek för att matcha användarens Interface.


Du kan fritt välja programvarulogotypen som används i handledningen eller någon annan relevant bild, så länge den är royaltyfri. Lägg dessutom till en bild med titeln `cover.webp` på samma plats. Den kommer att visas högst upp i din handledning. Se till att denna bild, liksom logotypen, respekterar användarrättigheterna och är lämplig för sammanhanget i din handledning.


Om du vill lägga till bilder i mappen `/assets` kan du dra och släppa dem från dina lokala filer. Se till att du befinner dig i mappen `/assets` och på rätt gren, klicka sedan på "*Commit changes*".


![GITHUB](assets/fr/26.webp)


Du bör nu se att bilderna visas i mappen.


![GITHUB](assets/fr/27.webp)


## 7 - Skriva handledning


Fortsätt att skriva din handledning genom att notera ditt innehåll i Markdown-filen med språkkoden (i mitt exempel, på franska, är det filen `fr.md`). Gå till filen och klicka på pennikonen:


![GITHUB](assets/fr/28.webp)


Börja skriva din handledning. När du lägger till en undertitel, använd lämplig Markdown-formatering genom att prefixera texten med `##`:


![GITHUB](assets/fr/29.webp)


Växla mellan vyerna "*Edit*" och "*Preview*" för att få en bättre bild av renderingen.


![GITHUB](assets/fr/30.webp)


För att spara ditt arbete klickar du på "*Commit Changes...*", kontrollerar att du befinner dig på rätt gren och bekräftar sedan genom att klicka på "*Commit Changes*" igen.


![GITHUB](assets/fr/31.webp)


## 8 - Lägg till bilder


Språkundermappen i mappen `/assets` (i mitt exempel: `/assets/en`) används för att lagra de diagram och bilder som ska följa med din handledning. Undvik i möjligaste mån att inkludera text i dina bilder för att göra ditt innehåll tillgängligt för en internationell publik. Naturligtvis kommer programvaran som presenteras att innehålla text, men om du lägger till scheman eller ytterligare indikationer på programvarans skärmdumpar, gör det utan text eller, om det är nödvändigt, använd engelska.


För att namnge dina bilder använder du helt enkelt nummer som motsvarar den ordning de visas i handledningen, formaterade som två siffror (eller tre siffror om din handledning innehåller fler än 99 bilder). Namnge till exempel den första bilden "01.webp", den andra "02.webp" och så vidare.


Dina bilder måste endast vara i formatet `.webp`. Om det behövs kan du använda [min programvara för bildkonvertering] (https://github.com/LoicPandul/ImagesConverter).


![GITHUB](assets/fr/32.webp)


Nu när du har lagt till dina bilder i undermappen kan du ta bort dummyfilen `.gitkeep`. Öppna den här filen, klicka på de tre små prickarna i det övre högra hörnet och sedan på "*Delete file*".


![GITHUB](assets/fr/33.webp)


Spara dina ändringar genom att klicka på "*Commit changes...*".


![GITHUB](assets/fr/34.webp)


För att infoga ett diagram från din undermapp i ditt redaktionella dokument använder du följande Markdown-kommando och ser till att ange lämplig alternativ text och rätt bildsökväg för ditt språk:


```
![green](assets/fr/01.webp)
```


Utropstecknet i början indikerar en bild. Den alternativa texten, som hjälper till med tillgänglighet och referenser, placeras mellan hakparenteserna. Slutligen anges sökvägen till bilden mellan parenteserna.


![GITHUB](assets/fr/35.webp)


Om du vill skapa dina egna scheman, se till att följa Plan ₿ Network:s grafiska riktlinjer för att säkerställa visuell enhetlighet:




- Font**: Använd [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Färger**:
 - Orange: #FF5C00
 - Svart: #000000
 - Vit: #FFFFFF


**Det är absolut nödvändigt att alla bilder som integreras i dina handledningar är fria från upphovsrätt eller respekterar källfilslicensen**. Därför görs alla diagram som publiceras på Plan ₿ Network tillgängliga under en CC-BY-SA-licens, på samma sätt som texten.


**-> Tips: ** När du delar filer offentligt, till exempel bilder, är det viktigt att ta bort överflödiga metadata. Dessa kan innehålla känslig information, t.ex. platsdata, skapandedatum och författardetaljer. För att skydda din integritet är det en bra idé att ta bort dessa metadata. För att förenkla detta kan du använda specialiserade verktyg som [Exif Cleaner] (https://exifcleaner.com/), som gör att du kan rensa upp ett dokuments metadata med en enkel dra-och-släpp-funktion.


## 9 - Föreslå handledning


När du är klar med att skriva din handledning på det språk du vill, är nästa steg att skicka in en **Pull Request**. Administratören kommer sedan att lägga till de saknade översättningarna i din handledning med hjälp av vår automatiserade översättningsmetod med mänsklig korrekturläsning.


För att gå vidare med Pull Request, efter att ha sparat alla dina ändringar, klicka på knappen "*Contribute*" och sedan på "*Open pull request*":


![GITHUB](assets/fr/36.webp)


En Pull Request är en begäran som görs för att integrera ändringar från din gren till huvudgrenen i Plan ₿ Network-arkivet, vilket möjliggör granskning och diskussion av ändringar innan de slås samman.


Innan du fortsätter ska du kontrollera noga längst ned i Interface att ändringarna är de du förväntade dig:


![GITHUB](assets/fr/37.webp)


Se till, högst upp i Interface, att din arbetsgren slås samman med `dev`-grenen i Plan ₿ Network-arkivet (som är huvudgrenen).


Ange en titel som kort sammanfattar de ändringar som du vill slå samman med källarkivet. Lägg till en kort kommentar som beskriver dessa ändringar (om du har ett problemnummer som är kopplat till skapandet av din handledning, kom ihåg att notera `Closes #{problemnummer}` som en kommentar) och klicka sedan på Green "*Create pull request*"-knappen för att bekräfta sammanslagningsbegäran:


![GITHUB](assets/fr/38.webp)


Din PR kommer sedan att synas på fliken "*Pull Request*" i Plan ₿ Network:s huvudarkiv. Allt du behöver göra nu är att vänta tills en administratör kontaktar dig för att bekräfta att ditt bidrag har sammanfogats eller för att begära ytterligare ändringar.


![GITHUB](assets/fr/39.webp)


Efter att ha sammanfogat din PR med huvudgrenen rekommenderar vi att du tar bort din arbetsgren (i mitt exempel: `tuto-Green-Wallet`) för att upprätthålla en ren historik över din Fork. GitHub kommer automatiskt att erbjuda dig detta alternativ på din PR-sida:


![GITHUB](assets/fr/40.webp)


Om du vill göra ändringar i ditt bidrag efter att du redan har skickat in din PR, beror stegen på vilken status din PR har:




- Om din PR fortfarande är öppen och ännu inte har sammanfogats kan du göra ändringarna i samma arbetsgren. Ändringarna kommer att läggas till i din fortfarande öppna PR;
- Om din PR redan har slagits samman med huvudgrenen måste du göra om processen från början genom att skapa en ny gren och sedan skicka in en ny PR. Se till att din Fork är synkroniserad med Plan ₿ Network-källarkivet på `dev`-grenen innan du fortsätter.


Om du har tekniska problem med att skicka in din handledning, tveka inte att be om hjälp på [vår dedikerade Telegramgrupp för bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tack så mycket!