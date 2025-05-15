---
name: Lägga till pedagogiska verktyg
description: Hur lägger man till nytt utbildningsmaterial på PlanB Network?
---
![event](assets/cover.webp)


PlanB:s uppdrag är att tillhandahålla ledande utbildningsresurser om Bitcoin på så många språk som möjligt. Allt innehåll som publiceras på webbplatsen är öppen källkod och finns på GitHub, vilket gör att vem som helst kan delta i att berika plattformen.


Utöver handledning och utbildning erbjuder PlanB Network också ett stort bibliotek med varierat utbildningsinnehåll på Bitcoin, tillgängligt för alla, [i avsnittet "BET" (_Bitcoin Educational Toolkit_)] (https://planb.network/resources/bet). Denna databas innehåller pedagogiska affischer, memes, humoristiska propagandaaffischer, tekniska diagram, logotyper och andra verktyg för användare. Målet med detta initiativ är att stödja individer och samhällen som undervisar Bitcoin runt om i världen genom att förse dem med nödvändiga visuella resurser.


Vill du vara med och berika den här databasen, men vet inte hur? Den här handledningen är för dig!


*Det är absolut nödvändigt att allt innehåll som integreras på webbplatsen är fritt från rättigheter eller respekterar källfilens licens. Dessutom görs alla bilder som publiceras på PlanB Network tillgängliga under licensen [CC-BY-SA] (https://creativecommons.org/licenses/by-sa/4.0/).*

![event](assets/01.webp)


- Först måste du ha ett konto på GitHub. Om du inte vet hur du skapar ett konto har vi gjort en detaljerad handledning för att vägleda dig.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Gå till [GitHub-förvaret för PlanB tillägnad data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) i avsnittet `resurser/bet/`:

![event](assets/02.webp)


- Klicka längst upp till höger på knappen "Lägg till fil" och sedan på "Skapa ny fil":

![event](assets/03.webp)


- Om du aldrig har bidragit till innehållet i PlanB Network tidigare måste du skapa din Fork av det ursprungliga förvaret. Att forka ett arkiv innebär att du skapar en kopia av det arkivet på ditt eget GitHub-konto, vilket gör att du kan arbeta med projektet utan att påverka det ursprungliga arkivet. Klicka på knappen `Fork this repository`:

![event](assets/04.webp)


- Du kommer då att komma till GitHubs redigeringssida:

![event](assets/05.webp)


- Skapa en mapp för ditt innehåll. Det gör du genom att i rutan `Namn på filen...` skriva namnet på innehållet med gemener och bindestreck i stället för mellanslag. I mitt exempel säger vi att jag vill lägga till en PDF-bild av BIP39-listan med 2048 ord. Då kallar jag min mapp för `bip39-ordlista`: ![event](assets/06.webp)
- Om du vill bekräfta att mappen har skapats lägger du till ett snedstreck efter namnet i samma ruta, till exempel: `bip39-wordlist/`. Om du lägger till ett snedstreck skapas automatiskt en mapp i stället för en fil:

![event](assets/07.webp)


- I den här mappen ska du skapa en första YAML-fil med namnet `bet.yml`:

![event](assets/08.webp)


- Fyll i den här filen med information som rör ditt innehåll med hjälp av den här mallen:


```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


Här är de uppgifter som ska fyllas i för varje fält:



- `byggare`**: Ange din organisations identifierare på PlanB Network. Om du ännu inte har en "builder"-identifierare för ditt företag kan du skapa en genom att följa denna handledning.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Om du inte har någon sådan kan du använda ditt namn, din pseudonym eller ditt företagsnamn utan att skapa en byggprofil.



- `typ`**: Välj vilken typ av innehåll du vill ha bland följande två alternativ:
 - `Utbildningsinnehåll` för utbildningsinnehåll.
 - `Visuellt innehåll` för andra typer av olika innehåll.



- `länkar`**: Tillhandahåller länkar till ditt innehåll. Du har två alternativ:
 - Om du väljer att hosta ditt innehåll direkt på PlanB:s GitHub måste du lägga till länkarna till den här filen under följande steg.
 - Om ditt innehåll finns någon annanstans, t.ex. på din personliga webbplats, anger du motsvarande länkar här:
     - `nedladdning`: En länk för att ladda ner ditt innehåll.
     - `Visa`: En länk för att visa ditt innehåll (kan vara samma som nedladdningslänken). Om ditt innehåll finns tillgängligt på flera språk lägger du till en länk för varje språk.



- `taggar`**: Lägg till två taggar som associeras med ditt innehåll. Exempel på taggar:
 - Bitcoin
 - teknik
 - ekonomi
 - utbildning
 - meme...



- bidragsgivare**: Ange din identifierare för bidragsgivare om du har en.


Din YAML-fil kan till exempel se ut så här:


```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Komplett och numrerad lista över de 2048 engelska ord från BIP39-ordlistan som används för att koda Mnemonic-fraser. Dokumentet kan skrivas ut på en enda sida.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-ordlista/tillgångar/BIP39-ORDLISTA.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```