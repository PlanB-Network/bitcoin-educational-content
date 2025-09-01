---
name: Bidrag - Git-handledning (avancerad)
description: Guide för avancerade användare som erbjuder en handledning i Plan ₿ Network med Git
---
![cover](assets/cover.webp)


Innan du följer denna handledning om hur du lägger till en ny handledning måste du ha slutfört några inledande steg. Om du inte redan har gjort det kan du först läsa den här inledande handledningen och sedan komma tillbaka hit:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Du har redan:



- Välj ett tema för din handledning;
- Kontaktade Plan ₿ Network-teamet via [Telegramgrupp](https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network ;
- Välj dina bidragsverktyg.


I denna handledning för erfarna Git-användare sammanfattar vi kort de viktigaste stegen och de viktigaste riktlinjerna för att erbjuda en ny Plan ₿ Network-handledning. Om du inte är bekant med Git och GitHub rekommenderar jag att du istället följer en av dessa andra 2 mer detaljerade handledningar som tar dig steg för steg:



- Mellanliggande (GitHub Desktop):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Nybörjare (webb Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Förslag på verktyg


För redigering av Markdown-filer:



- Obsidian (gratis, ej öppen källkod)
- Mark Text (gratis, öppen källkod)
- Zettlr (gratis, öppen källkod)
- Typora (betalprogram, ~€15, ej öppen källkod)


För Git:



- Git (gratis, öppen källkod)
- GitHub Desktop (gratis, öppen källkod)
- Sourcetree (gratis, inte öppen källkod)


För redigering av YAML-filer:



- Visual Studio Code (gratis, öppen källkod)
- Sublime Text (gratis med begränsningar, inte öppen källkod)


För att skapa diagram och visuella bilder:



- Canva (gratis med betalda alternativ, inte öppen källkod)
- Inkscape (gratis, öppen källkod)
- Penpot (gratis, öppen källkod)


## Arbetsflöden


### 1 - Konfigurera din lokala miljö



- Du måste ha din egen Fork av [Plan ₿ Network repository on GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).
- Synkronisera huvudgrenen (`dev`) i din Fork med källkatalogen.
- Uppdatera din lokala klon.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Skapa en ny filial



- Se till att du är på `dev`-grenen.
- Skapa en ny gren med ett beskrivande namn (t.ex. `tuto-Green-Wallet-loic`).
- Publicera denna filial på din online Fork.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Lägg till handledningsdokumenten


***Anmärkning:*** Du kan automatisera steg 3 och 4 med hjälp av [mitt Python GUI-skript] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Kör det direkt från dess mapp i din lokala klon och fyll sedan i de obligatoriska fälten i GUI. För mer information om hur du installerar och använder det, se [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Om du föredrar att göra det manuellt följer du dessa steg:



- Leta reda på lämplig mapp i det lokala arkivet (t.ex. `tutorials/Wallet`).
- Skapa en katalog som är avsedd för handledningen med ett tydligt namn (t.ex. `Green-Wallet`). Detta mappnamn kommer också att bestämma URL-sökvägen för handledningen. Namnet ska vara skrivet med gemener, utan specialtecken (utom bindestreck) och utan mellanslag.
- Lägg till följande objekt i den här katalogen:
    - En undermapp med namnet `assets` som innehåller:
        - Två `.webp`-bilder:
            - `logo.webp`: Handledningens logotyp (fyrkantigt format med bakgrund). Denna logotyp måste representera den programvara eller det verktyg som presenteras. Om handledningen inte är specifik för ett verktyg (t.ex. en allmän guide för att generera en Mnemonic-fras) kan du välja en lämplig bild (t.ex. en generisk ikon).
            - `omslag.webp`: En omslagsbild som visas i början av handledningen.
        - En undermapp med koden för handledningens originalspråk. Om handledningen t.ex. är skriven på engelska ska denna undermapp heta "en". Placera alla handledningens visuella element (diagram, bilder, skärmdumpar etc.) i denna mapp.
    - En `tutorial.yml`-fil som innehåller metadata (författare, taggar, kategori, svårighetsgrad etc.).
    - En Markdown-fil som innehåller handledningen, namngiven enligt språkkoden (t.ex. `fr.md`, `en.md`, etc.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Fyll i YAML-filen



- Fyll i filen `tutorial.yml` enligt följande:


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



- kategori**: Den underkategori som motsvarar innehållet i handledningen, enligt Plan ₿ Network:s webbplatsstruktur (t.ex. för plånböcker: `dator`, `hårdvara`, `mobil`, `backup`);



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


### 5 - Skriv innehållet



- Fyll i filegenskaperna för Markdown med:
    - Titeln (`namn`).
    - En kort beskrivning (`description`).
- Lägg till omslagsbilden högst upp i handledningen med hjälp av Markdown-syntax (ersätt "Green" med namnet på det verktyg som visas):


```
![cover-green](assets/cover.webp)
```



- Skriv innehållet i handledningen i Markdown:
    - Använd välstrukturerade rubriker (`##`), listor och stycken.
    - Infoga bilder med hjälp av Markdown-syntax:


```
![nom-image](assets/en/001.webp)
```




- Placera diagram och bilder i undermappen för respektive språk i `/assets`.


### 6 - Spara och skicka in handledningen



- Spara dina ändringar lokalt genom att skapa en commit med ett beskrivande meddelande.
- Skicka ändringarna till din GitHub Fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- När du är klar skapar du en Pull Request (PR) på GitHub för att föreslå integration av dina ändringar.
- Lägg till en titel och en kort beskrivning av PR-meddelandet. Ange motsvarande utgåvenummer i kommentaren.


### 7 - Korrekturläsning och sammanslagning



- Invänta bekräftelse eller feedback från en administratör.
- Om det behövs, gör korrigeringar och skicka nya commits.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- När PR:n har sammanfogats kan du ta bort din arbetsgren.


## Standarder för skapande av innehåll



- Formatering stöds på plattformen**:
    - Klassisk Markdown: listor, länkar, bilder, citat, fetstil, kursiv stil etc.
    - LaTeX (endast block, inte inline): avgränsas av `$$`.
    - Inline-kod: Syntax med en enda backtick.
    - Kodblock: Syntax med tre bakåtstreck, till exempel:


```
print("Hello, Bitcoin!")
```



- Illustrationer och diagram**:
    - Alla bilder måste vara i WebP-format. Använd det här gratisverktyget för att konvertera dem om det behövs: [ImagesConverter] (https://github.com/LoicPandul/ImagesConverter).
    - Namnge bilderna med 2 eller 3 siffror (t.ex. `001.webp`, `002.webp`).
    - Använd mock-ups för handledning om mobiler eller Hardware Wallet.
    - Använd endast egenhändigt skapade eller royaltyfria bilder.
    - Se till att de är relevanta och av hög kvalitet.
- Grafisk charter**:
    - Font: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Färger Plan ₿ Network:
        - Orange: `#FF5C00`
        - Svart: `#000000`
        - Vit: `#FFFFFFFF`


Om du har tekniska problem med att skicka in din handledning, tveka inte att be om hjälp på [vår dedikerade Telegramgrupp för bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tack så mycket!