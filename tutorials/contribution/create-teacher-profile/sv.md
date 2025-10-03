---
name: Professor Plan ₿ Network
description: Hur lägger jag till eller ändrar min lärarprofil på Plan ₿ Network?
---
![cover](assets/cover.webp)


Om du planerar att bidra till Plan ₿ Network genom att skriva en ny handledning eller kurs behöver du en lärarprofil. Denna profil gör det möjligt för dig att få lämpliga krediter för det innehåll du bidrar med till plattformen.


För de av er som redan har varit involverade i att skapa utbildningsinnehåll på Plan ₿ Network har ni förmodligen redan en lärarprofil. Du hittar den i mappen `/professors` [på vårt GitHub-arkiv] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Om din profil redan existerar hittar du din inloggning i filen `professor.yml`.


För att göra ändringar i din profil, gå till avsnittet "Redigera din lärarprofil" i slutet av denna handledning.


## Lägg till en ny lärare med vår programvara


Det enklaste sättet att skapa din lärarprofil på Plan ₿ Network är att använda vårt integrerade Python-verktyg. Så här fungerar det.


### 1 - Konfigurera din lokala miljö


Du måste ha din egen Fork från [Plan ₿ Network repository on GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).


Synkronisera huvudgrenen (`dev`) i din Fork med källkatalogen.


Uppdatera din lokala klon.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Skapa en ny filial


Se till att du är på `dev`-grenen. Skapa en ny gren med ett beskrivande namn (t.ex. `add-professor-loic-morel`).


Publicera denna filial på din Fork online.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Skapa din lärarprofil


Gå till mappen `scripts/tutorial-related/data-creator/` på din lokala klon. Se till att du har installerat alla beroenden som krävs för programvaran, efter att först ha installerat Python:


```bash
pip install -r requirements.txt
```


Starta sedan programvaran med kommandot:


```bash
python3 main.py
```


När du är på startsidan anger du den lokala sökvägen till din repository-klon, det språk du skriver på och ditt GitHub-ID. Om du skapar den här profilen för någon annan och redan har en professorsprofil anger du ditt ID i fältet "*PBN Professor's ID*". Om du skapar din egen profil kommer du inte att ha ett Professor's ID ännu, eftersom du håller på att skapa ett, så lämna det här fältet tomt.


Klicka sedan på knappen "*New Professor*".


![Image](assets/fr/01.webp)


Fyll i den information som krävs (observera att all denna information kommer att vara offentlig på vår plattform samt på GitHub):




- Namnet på din lärarfil (använd ditt för- och efternamn eller en pseudonym, med gemener) ;
- Ditt namn eller smeknamn ;
- Din webbplats och profil X (valfritt) ;
- En Lightning Address för att ta emot donationer från läsare (valfritt) ;
- Välj 2 eller 3 taggar från listan;
- Klicka på "*Select Image*" för att välja en profilbild från dina lokala mappar (vilket namn och format som helst kan användas för bilden, och programmet anpassar den automatiskt. Se bara till att bilden är kvadratisk);
- Skriv en kort beskrivning av din profil.


Slutför skapandet genom att klicka på "*Create Professor*". Detta kommer automatiskt att generate alla de filer som krävs för din profil.


![Image](assets/fr/02.webp)


Spara dina ändringar lokalt genom att skapa en commit med ett förklarande meddelande. Skicka ändringarna till din Fork GitHub.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


När du är klar skapar du en Pull Request (PR) på GitHub för att föreslå integration av dina ändringar. Lägg till en titel och en kort beskrivning i PR:n.


### 4 - Korrekturläsning och sammanslagning


Vänta på validering eller feedback från en administratör. Om det behövs, gör korrigeringar och skicka nya commits.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


När PR:n har sammanfogats kan du ta bort din arbetsgren.


## Ändra din lärarprofil


Om du behärskar användningen av Git kan du ändra din lärarprofil genom att skapa en ny gren och redigera den relevanta filen direkt i din befintliga mapp. Ändringar kan göras antingen i filen `professor.yml` eller i markdown-filen, beroende på vilken information som ska korrigeras. När du har gjort dina ändringar lokalt kan du skicka dem till din Fork och skicka in en PR.


För nybörjare rekommenderar jag att du gör modifieringen direkt via GitHubs Interface-webb. Se till att du har ett GitHub-konto. Om du inte vet hur du skapar ett, följ denna handledning:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Gå till [Plan ₿ Network:s GitHub-arkiv för data] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).


![Image](assets/fr/03.webp)


Klicka på mappen "*professorer*" och gå sedan till din personliga mapp.


![Image](assets/fr/04.webp)


Om du vill ändra metadata för din profil, t.ex. Lightning Address, namn eller länkar, väljer du filen "*professor.yml*". Om du vill ändra din beskrivning klickar du på YAML-filen för ditt språk (t.ex. "*en.yml*" eller "*fr.yml*").


Om du ändrar din beskrivning ska du komma ihåg att ta bort alla föråldrade översättningar. Sedan kan du antingen ta hand om att översätta din beskrivning till de andra språken med hjälp av en LLM, eller bara lämna beskrivningen på ditt modersmål och nämna i din Pull Request att din beskrivning kräver översättning av vårt team.


![Image](assets/fr/05.webp)


Klicka på pennikonen när du befinner dig i den fil du vill ändra.


![Image](assets/fr/06.webp)


Om du inte redan har en Fork från Plan ₿ Network-arkivet kommer GitHub att föreslå att du skapar en. Klicka på "*Fork this repository*".


![Image](assets/fr/07.webp)


Gör de önskade ändringarna i filen. När du är klar klickar du på "*Commit changes*".


![Image](assets/fr/08.webp)


Skriv ett meddelande som beskriver din ändring och välj sedan "*Föreslå ändringar*".


![Image](assets/fr/09.webp)


En sammanfattning av dina ändringar visas. Om du vill göra ytterligare ändringar i din profil kan du gå tillbaka till mapparna och göra ytterligare commits. När du är klar klickar du på "*Create pull request*".


En Pull Request är en begäran som görs för att integrera ändringar från din gren till huvudgrenen i Plan ₿ Network-arkivet, vilket möjliggör granskning och diskussion av ändringar innan de slås samman.


![Image](assets/fr/10.webp)


Se till, i början av Interface, att din arbetsgren slås samman med `dev`-grenen i Plan ₿ Network-arkivet (som är huvudgrenen).


Ange en titel som kort sammanfattar de ändringar som du vill slå samman med källarkivet. Lägg till en kort kommentar som beskriver ändringarna och klicka sedan på Green-knappen "*Create pull request*" för att bekräfta pull request:


![Image](assets/fr/11.webp)


Din PR kommer då att synas på fliken "*Pull Request*" i Plan ₿ Network:s huvudarkiv. Allt du behöver göra nu är att vänta på att en administratör ska sammanfoga din modifiering.


![Image](assets/fr/12.webp)


Om du stöter på några tekniska svårigheter när du skickar in din ändring, tveka inte att be om hjälp på [vår Telegramgrupp för bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tack så mycket!