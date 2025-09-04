---
name: Bidrag - Självstudier med GitHub Desktop (mellanstadium)
description: Komplett guide för att föreslå en handledning på Plan ₿ Network med hjälp av GitHub Desktop
---
![cover](assets/cover.webp)


Innan du följer denna handledning om hur du lägger till en ny handledning måste du ha genomfört några inledande steg. Om du inte har gjort det ännu, ber jag dig att först läsa denna inledande handledning och sedan komma tillbaka hit:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Det har du redan gjort:


- Välj tema för din handledning;
- Kontaktade Plan ₿ Network-teamet via [Telegramgruppen](https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network;
- Välj dina bidragsverktyg.


I den här handledningen kommer vi att se hur du lägger till din handledning på Plan ₿ Network genom att ställa in din lokala miljö med GitHub Desktop. Om du redan är duktig på Git kanske denna mycket detaljerade handledning inte är nödvändig för dig. Jag skulle hellre rekommendera att du läser den här andra handledningen där jag bara presenterar de viktigaste riktlinjerna, utan detaljerad steg-för-steg-vägledning:



- Erfarna användare**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Om du föredrar att inte konfigurera din lokala miljö kan du följa den här andra handledningen som är utformad för nybörjare, där vi gör ändringarna direkt via GitHubs webb Interface:



- Nybörjare (webb Interface)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Förkunskapskrav


Programvara som krävs för att följa denna handledning:



- [GitHub Desktop] (https://desktop.github.com/);
- En redigerare för markdownfiler som [Obsidian] (https://obsidian.md/);
- En kodredigerare ([VSC](https://code.visualstudio.com/) eller [Sublime Text](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


Förutsättningar innan du börjar handledningen:



- Har ett [GitHub-konto] (https://github.com/signup);
- Ha en Fork av [Plan ₿ Network källförvar] (https://github.com/PlanB-Network/Bitcoin-educational-content);
- Har [en professorsprofil på Plan ₿ Network] (https://planb.network/professors) (endast om du föreslår en fullständig handledning).


Om du behöver hjälp med att skaffa dessa förutsättningar kan du få hjälp av mina andra handledningar:



När allt är på plats och din lokala miljö är korrekt inställd med din egen Fork av Plan ₿ Network, kan du börja lägga till handledningen.


## 1 - Skapa en ny filial


Öppna din webbläsare och gå till sidan för din Fork i Plan ₿ Network-förvaret. Detta är den Fork som du har etablerat på GitHub. URL:en till din Fork bör se ut som: `https://github.com/[ditt-användarnamn]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


Se till att du befinner dig på huvudgrenen `dev` och klicka sedan på knappen `Synkronisera Fork`. Om din Fork inte är uppdaterad kommer GitHub att erbjuda dig att uppdatera din gren. Fortsätt med denna uppdatering. Om din gren tvärtom redan är uppdaterad kommer GitHub att informera dig om detta:


![TUTO](assets/fr/04.webp)


Öppna GitHub Desktop-programvaran och se till att din Fork är korrekt vald i det övre vänstra hörnet av fönstret:


![TUTO](assets/fr/05.webp)


Klicka på knappen `Fetch origin`. Om ditt lokala arkiv redan är uppdaterat kommer GitHub Desktop inte att föreslå någon ytterligare åtgärd. Annars kommer alternativet `Pull origin` att visas. Klicka på den här knappen för att uppdatera ditt lokala arkiv:


![TUTO](assets/fr/06.webp)


Kontrollera att du verkligen befinner dig på huvudgrenen `dev`:


![TUTO](assets/fr/07.webp)


Klicka på den här grenen och klicka sedan på knappen "Ny gren":


![TUTO](assets/fr/08.webp)


Se till att den nya grenen är baserad på källarkivet, nämligen `PlanB-Network/Bitcoin-educational-content`.


Namnge din gren på ett sätt som gör att titeln tydligt visar dess syfte, och använd bindestreck för att separera varje ord. Låt oss till exempel säga att vårt mål är att skriva en handledning om hur man använder programvaran Sparrow wallet. I det här fallet kan arbetsgrenen som är avsedd för att skriva denna handledning få namnet: `tuto-Sparrow-Wallet-loic`. När du har angett rätt namn klickar du på `Create branch` för att bekräfta skapandet av grenen:


![TUTO](assets/fr/09.webp)


Klicka nu på knappen `Publish branch` för att spara din nya arbetsgren till din online Fork på GitHub:

![TUTORIAL](assets/fr/10.webp)

Nu, på GitHub Desktop, bör du befinna dig på din nya gren. Detta innebär att alla ändringar som görs lokalt på din dator kommer att sparas uteslutande på denna specifika gren. Så länge den här grenen är vald på GitHub Desktop kommer de filer som är synliga lokalt på din dator att motsvara filerna i den här grenen (`tuto-Sparrow-Wallet-loic`), och inte filerna i huvudgrenen (`dev`).


![TUTORIAL](assets/fr/11.webp)


För varje ny artikel som du vill publicera måste du skapa en ny gren från `dev`. En gren i Git är en parallell version av projektet, vilket gör att du kan göra ändringar utan att påverka huvudgrenen, tills arbetet är redo att slås samman.


## 2 - Lägga till handledningsfilerna


Nu när arbetsgrenen är skapad är det dags att integrera din nya handledning. Du har två alternativ: använd mitt Python-skript, som automatiserar skapandet av de nödvändiga dokumenten, eller skapa varje fil manuellt. Vi kommer att titta på de steg som ska följas för varje alternativ.


### Med mitt Python-skript


Du måste installera på din maskin:


- Python 3.8 eller högre.


För att använda skriptet, navigera till mappen där det är lagrat. Skriptet finns i Plan ₿ Network:s datalager på sökvägen: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


När du är i mappen installerar du beroendena:


```
pip install -r requirements.txt
```


Starta sedan programvaran med kommandot:


```
python3 main.py
```


Ett grafiskt användargränssnitt Interface (GUI) öppnas. Första gången måste du ange all nödvändig information, men vid senare användning kommer skriptet att komma ihåg din personliga information, så att du inte behöver ange den igen.


![DATA-CREATOR-PY](assets/fr/37.webp)


Börja med att ange den lokala sökvägen till mappen `/tutorials` i ditt klonade repository (`.../Bitcoin-educational-content/tutorials/`). Du kan ange den manuellt eller klicka på knappen "Browse" för att navigera med din filutforskare.


![DATA-CREATOR-PY](assets/fr/38.webp)


Välj det språk som du vill skriva din handledning på.


![DATA-CREATOR-PY](assets/fr/39.webp)


I fältet "Contributor's GitHub ID" anger du ditt användarnamn på GitHub.


![DATA-CREATOR-PY](assets/fr/40.webp)


Därefter måste du fylla i din professorsprofil. Det finns flera alternativ tillgängliga för dig:


- Ange de första bokstäverna i ditt namn i fältet "Professor Name". Ditt namn kommer då att visas i rullgardinsmenyn "Prof. Suggestions" nedan. Välj det genom att klicka på det;
- Alternativt kan du klicka direkt på rullgardinsmenyn "Prof. Suggestions" och välja ditt professorsnamn.


Denna åtgärd kommer automatiskt att fylla i din professors UUID i motsvarande fält.



![DATA-CREATOR-PY](assets/fr/41.webp)


Om du inte har en professorsprofil ännu kan du läsa den här handledningen:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Klicka sedan på knappen "Ny handledning".


![DATA-CREATOR-PY](assets/fr/42.webp)


Välj en huvudkategori för din handledning. Välj sedan en relevant underkategori baserat på den valda huvudkategorin.


![DATA-CREATOR-PY](assets/fr/43.webp)


Bestäm svårighetsgraden för handledningen.


![DATA-CREATOR-PY](assets/fr/44.webp)


Välj ett namn för den katalog som skapats specifikt för din handledning. Namnet på den här mappen ska återspegla den programvara som behandlas i handledningen och skilja orden åt med bindestreck. Mappen kan till exempel heta "red-Wallet":


![DATA-CREATOR-PY](assets/fr/45.webp)


`project_id` är UUID för företaget eller organisationen bakom det verktyg som behandlas i handledningen, tillgängligt [i listan över projekt](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Till exempel, för en handledning om Sparrow wallet, kan du hitta dess `project_id` i filen: `Bitcoin-educational-content/resources/projects/Sparrow/project.yml`. Denna information läggs till i din handlednings YAML-fil eftersom Plan ₿ Network upprätthåller en databas över företag och organisationer som är aktiva i Bitcoin eller relaterade projekt. Genom att lägga till det associerade `project_id` länkar du ditt innehåll till den relevanta enheten.


***Uppdatering:*** I den nya versionen av skriptet behöver du inte längre ange `project_id` manuellt. En sökfunktion har lagts till för att hitta projektet efter namn och automatiskt hämta motsvarande `project_id`. Skriv början av projektets namn i fältet "Project Name" för att söka efter det och välj sedan önskat företag i rullgardinsmenyn. "Project_id" fylls automatiskt i i fältet nedan. Du kan också ange det manuellt om det behövs.


![DATA-CREATOR-PY](assets/fr/46.webp)


För taggar väljer du 2 eller 3 relevanta nyckelord som är relaterade till innehållet i din handledning och väljer uteslutande från [Plan ₿ Network tagglista] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Programvaran innehåller också en sökfunktion för nyckelord med en rullgardinslista.


![DATA-CREATOR-PY](assets/fr/47.webp)


När all information har angetts och verifierats klickar du på "Create Tutorial" för att bekräfta skapandet av dina handledningsfiler. Detta kommer att generate din handledningsmapp och alla nödvändiga filer i den valda kategorin lokalt.


![DATA-CREATOR-PY](assets/fr/48.webp)


Du kan nu hoppa över underavsnittet "Utan mitt Python-skript" samt steg 3, "Fyll i YAML-filen", eftersom skriptet redan har utfört dessa åtgärder åt dig. Fortsätt direkt till steg 4 och börja skriva din självstudie.


För mer information om detta Python-skript kan du också läsa [README] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


### Utan mitt Python-skript


Öppna din filhanterare och navigera till mappen `Bitcoin-educational-content`, som representerar den lokala klonen av ditt arkiv. Du hittar den vanligtvis under `Documents\GitHub\Bitcoin-educational-content`.


I den här katalogen måste du hitta den lämpliga undermappen för att placera din handledning. Mapporganisationen återspeglar de olika avsnitten på Plan ₿ Network-webbplatsen. I vårt exempel, eftersom vi vill lägga till en handledning om Sparrow wallet, ska vi navigera till följande sökväg: `Bitcoin-educational-content\tutorials\Wallet`, vilket motsvarar avsnittet `Wallet` på webbplatsen:


![TUTO](assets/fr/12.webp)


I mappen `Wallet` måste du skapa en ny katalog som är särskilt avsedd för din handledning. Namnet på den här mappen ska påminna om den programvara som behandlas i handledningen och se till att koppla samman ord med bindestreck. I mitt exempel kommer mappen att heta `Sparrow-Wallet`:


![TUTO](assets/fr/13.webp)


I den här nya undermappen som är avsedd för din handledning måste flera Elements läggas till:


- Skapa en mapp "Assets" som ska innehålla alla illustrationer som behövs för din handledning;
- I mappen `assets` måste du skapa en undermapp med namnet enligt handledningens ursprungliga språkkod. Om handledningen t.ex. är skriven på engelska måste undermappen heta "en". Placera alla bilder från handledningen där (diagram, bilder, skärmdumpar etc.).
- En fil `tutorial.yml` måste skapas för att registrera de detaljer som är relaterade till din handledning;
- En fil i markdown-format ska skapas för att skriva det faktiska innehållet i din handledning. Filen måste ha en titel som motsvarar språkkoden för det som skrivs. Till exempel, för en handledning skriven på franska måste filen heta `fr.md`.


![TUTO](assets/fr/14.webp)


Sammanfattningsvis är det här hierarkin av filer som ska skapas:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - Fyll i YAML-filen


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



- projekt_id**: UUID för företaget eller organisationen bakom det verktyg som presenteras i handledningen [från projektlistan] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Om du till exempel skapar en handledning om programvaran Green Wallet kan du hitta detta `project_id` i följande fil: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Den här informationen läggs till i din handlednings YAML-fil eftersom Plan ₿ Network upprätthåller en databas över alla företag och organisationer som arbetar med Bitcoin eller relaterade projekt. Genom att lägga till `project_id` för den enhet som är länkad till din handledning skapar du en länk mellan de två Elements;



- taggar**: 2 eller 3 relevanta nyckelord relaterade till handledningens innehåll, uteslutande valda [från Plan ₿ Network:s tagglista] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategori**: Underkategorin som motsvarar innehållet i handledningen, enligt Plan ₿ Network:s webbplatsstruktur (t.ex. för plånböcker: `desktop`, `hardware`, `mobile`, `backup`);



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


När du är klar med att ändra filen `tutorial.yml` sparar du dokumentet genom att klicka på `File > Save`:


![TUTO](assets/fr/16.webp)


Du kan nu stänga din kodredigerare.


## 4 - Fyll i Markdown-filen


Nu kan du öppna din fil som kommer att vara värd för din handledning, namngiven med koden för ditt språk, till exempel `fr.md`. Gå till Obsidian, på vänster sida av fönstret, bläddra igenom mappträdet tills du hittar mappen för din handledning och den fil du letar efter:


![TUTO](assets/fr/18.webp)


Klicka på filen för att öppna den:


![TUTO](assets/fr/19.webp)


Vi börjar med att fylla i avsnittet `Properties` högst upp i dokumentet.


![TUTO](assets/fr/20.webp)


Lägg till och fyll i följande kodblock manuellt:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


Fyll i namnet på din handledning och en kort beskrivning av den:


![TUTO](assets/fr/22.webp)


Lägg sedan till sökvägen för omslagsbilden i början av din handledning. För att göra detta, notera:


```
![cover-sparrow](assets/cover.webp)
```


Denna syntax är användbar när det är nödvändigt att lägga till en bild i din handledning. Utropstecknet anger att det är en bild, med den alternativa texten (alt) angiven mellan parenteserna. Sökvägen till bilden anges mellan parenteserna:


![TUTO](assets/fr/23.webp)


## 5 - Lägg till logotyp och omslag


I mappen `assets` måste du lägga till en fil med namnet `logo.webp`, som kommer att fungera som en miniatyrbild för din artikel. Bilden måste vara i formatet `.webp` och måste ha en kvadratisk dimension för att harmonisera med användarens Interface. Du kan välja logotypen för den programvara som behandlas i handledningen eller någon annan relevant bild, förutsatt att den är fri från rättigheter. Lägg dessutom till en bild med titeln `cover.webp` på samma plats. Den här bilden kommer att visas högst upp i din handledning. Se till att denna bild, precis som logotypen, respekterar användningsrättigheter och är lämplig för sammanhanget i din handledning:

## 6 - Skriva självstudien och lägga till bilder


Fortsätt att skriva din handledning genom att utarbeta ditt innehåll. När du vill integrera en undertitel tillämpar du lämplig markdownformatering genom att prefixera texten med `##`:


![TUTO](assets/fr/24.webp)


Undermappen Language i mappen `assets` används för att lagra diagram och bilder som ska följa med din handledning. Undvik i möjligaste mån att inkludera text i dina bilder för att göra ditt innehåll tillgängligt för en internationell publik. Programvaran som presenteras kommer naturligtvis att innehålla text, men om du lägger till diagram eller ytterligare indikationer på skärmdumpar av programvara, gör det utan text eller, om det visar sig vara nödvändigt, använd engelska.


![TUTO](assets/fr/25.webp)


För att namnge dina bilder använder du helt enkelt nummer som motsvarar den ordning de visas i handledningen, formaterade med två siffror (eller tre siffror om din handledning innehåller fler än 99 bilder). Namnge till exempel din första bild "01.webp", din andra "02.webp" och så vidare.


Dina bilder måste uteslutande vara i `.webp`-format. Om det behövs kan du använda [min programvara för bildkonvertering] (https://github.com/LoicPandul/ImagesConverter).


![TUTO](assets/fr/26.webp)


Om du vill infoga ett diagram i ditt dokument använder du följande Markdown-kommando och ser till att ange lämplig alternativ text samt korrekt sökväg för bilden:


```
![sparrow](assets/fr/01.webp)
```


Utropstecknet i början anger att det är en bild. Den alternativa texten, som hjälper till med tillgänglighet och SEO, placeras mellan parenteserna. Slutligen anges sökvägen till bilden mellan parenteserna.


Om du vill skapa dina egna diagram, se till att följa Plan ₿ Network:s grafiska stadgar för att säkerställa visuell enhetlighet:


- Font**: Använd [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Färger**:
 - Orange: #FF5C00
 - Svart: #000000
 - Vit: #FFFFFF


**Det är absolut nödvändigt att alla bilder som integreras i dina handledningar är fria från rättigheter eller respekterar källfilens licens**. Alla diagram som publiceras på Plan ₿ Network görs också tillgängliga under CC-BY-SA-licensen, på samma sätt som texten.

**-> Tips: ** När du delar filer offentligt, till exempel bilder, är det viktigt att ta bort onödiga metadata. Detta kan innehålla känslig information, som platsdata, skapandedatum eller detaljer om författaren. För att skydda din integritet är det lämpligt att radera dessa metadata. För att förenkla denna process kan du använda specialiserade verktyg som [Exif Cleaner] (https://exifcleaner.com/), som gör det möjligt att rengöra ett dokuments metadata genom en enkel dra-och-släpp-funktion.

## 7 - Spara och skicka in självstudiekursen


När du är klar med att skriva din handledning på det språk du vill, är nästa steg att skicka in en **Pull Request**. Administratören kommer sedan att lägga till alla saknade översättningar av din handledning, tack vare vår automatiserade översättningsmetod med mänsklig granskning.


För att fortsätta med Pull Request öppnar du programvaran GitHub Desktop. Programvaran bör automatiskt upptäcka de ändringar du har gjort lokalt på din gren jämfört med det ursprungliga förvaret. Innan du fortsätter, kontrollera noggrant på vänster sida av Interface att dessa ändringar matchar vad du förväntade dig:


![TUTO](assets/fr/28.webp)


Lägg till en titel för din commit och klicka sedan på den blå knappen `Commit to [your branch]` för att validera ändringarna:


![TUTO](assets/fr/29.webp)


En commit är en lagring av de ändringar som gjorts i grenen, tillsammans med ett beskrivande meddelande, vilket gör det möjligt att följa utvecklingen av ett projekt över tid. Det är en slags mellanliggande kontrollpunkt.


Klicka sedan på knappen `Push origin`. Detta kommer att skicka din commit till din Fork:


![TUTO](assets/fr/30.webp)


Om du inte har avslutat din handledning kan du komma tillbaka till den senare och göra nya ändringar. Om du har slutfört dina ändringar för den här grenen klickar du nu på knappen `Preview Pull Request`:


![TUTO](assets/fr/31.webp)


Du kan kontrollera en sista gång att dina ändringar är korrekta och sedan klicka på knappen `Create pull request`:


![TUTO](assets/fr/32.webp)


En Pull Request är en begäran som görs för att integrera ändringarna från din gren till huvudgrenen i Plan ₿ Network-arkivet, vilket möjliggör granskning och diskussion av ändringarna innan de slås samman.


Du kommer automatiskt att omdirigeras till din webbläsare på GitHub till förberedelsesidan för din Pull Request:


![TUTO](assets/fr/33.webp)

Ange en titel som kort sammanfattar de ändringar som du vill slå samman med källarkivet. Lägg till en kort kommentar som beskriver dessa ändringar (om du har ett problemnummer som är kopplat till skapandet av din handledning, kom ihåg att notera i kommentaren `Closes #{issue number}`), klicka sedan på Green `Create pull request`-knappen för att bekräfta sammanslagningsbegäran:

![TUTO](assets/fr/34.webp)


Din PR kommer sedan att synas på fliken "Pull Request" i Plan ₿ Network:s huvudarkiv. Allt du behöver göra är att vänta tills en administratör kontaktar dig för att bekräfta sammanslagningen av ditt bidrag eller för att begära ytterligare ändringar.


![TUTO](assets/fr/35.webp)


Efter att din PR har slagits samman med huvudgrenen rekommenderas det att du tar bort din arbetsgren (`tuto-Sparrow-Wallet`) för att upprätthålla en ren historik på din Fork. GitHub kommer automatiskt att erbjuda dig detta alternativ på din PR-sida:


![TUTO](assets/fr/36.webp)


På GitHub Desktop-programvaran kan du växla tillbaka till huvudgrenen för din Fork (`dev`).


![TUTO](assets/fr/07.webp)


Om du vill göra ändringar i ditt bidrag efter att du redan har skickat in din PR, beror förfarandet på hur långt du har kommit med din PR:


- Om din PR fortfarande är öppen och ännu inte har sammanfogats, gör ändringarna lokalt medan du stannar kvar på samma gren. När ändringarna har slutförts använder du knappen `Push origin` för att lägga till en ny commit till din fortfarande öppna PR;
- Om din PR redan har sammanfogats med huvudgrenen måste du börja om processen genom att skapa en ny gren och sedan skicka in en ny PR. Se till att ditt lokala arkiv är synkroniserat med Plan ₿ Network:s källarkiv innan du fortsätter.


Om du stöter på tekniska svårigheter när du skickar in din handledning, tveka inte att be om hjälp på [vår särskilda Telegramgrupp för bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tack så mycket!