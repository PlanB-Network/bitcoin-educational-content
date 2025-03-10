---
name: Bidrag - Opplæring med GitHub Desktop (mellomnivå)
description: Komplett veiledning for å foreslå en opplæring på Plan ₿ Network ved hjelp av GitHub Desktop
---
![cover](assets/cover.webp)

Før du følger denne veiledningen om hvordan du legger til en ny opplæring, må du ha gjennomført noen innledende trinn. Hvis du ikke har gjort det ennå, anbefaler jeg at du først leser denne introduksjonsveiledningen, og deretter kommer tilbake hit:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Det har du allerede gjort:


- Velg tema for veiledningen din;
- Kontaktet Plan ₿ Network-teamet via [Telegramgruppen] (https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network;
- Velg dine bidragsverktøy.

I denne veiledningen vil vi se hvordan du legger til opplæringen din på Plan ₿ Network ved å sette opp ditt lokale miljø med GitHub Desktop. Hvis du allerede er dyktig med Git, er denne veldig detaljerte opplæringen kanskje ikke nødvendig for deg. Jeg vil heller anbefale å lese denne andre veiledningen, der jeg bare presenterer de viktigste retningslinjene, uten detaljert trinnvis veiledning:


- Erfarne brukere**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Hvis du foretrekker å ikke sette opp ditt lokale miljø, kan du følge denne andre veiledningen for nybegynnere, der vi gjør endringene direkte via GitHubs webgrensesnitt:


- Nybegynnere (nettgrensesnitt)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Forutsetninger

Programvare som kreves for å følge denne opplæringen:


- [GitHub Desktop] (https://desktop.github.com/);
- En markdown-filredigerer som [Obsidian] (https://obsidian.md/);
- En kodeditor ([VSC](https://code.visualstudio.com/) eller [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Forutsetninger før du starter opplæringen:


- Har en [GitHub-konto] (https://github.com/signup);
- Ha en gaffel av [Plan ₿ Network source repository] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Har [en professorprofil på Plan ₿ Network] (https://planb.network/professors) (bare hvis du foreslår en fullstendig veiledning).

Hvis du trenger hjelp med å skaffe deg disse forutsetningene, kan du få hjelp i de andre veiledningene mine:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb

Når alt er på plass og det lokale miljøet ditt er riktig konfigurert med din egen gaffel av Plan ₿ Network, kan du begynne å legge til opplæringen.

## 1 - Opprett en ny filial

Åpne nettleseren din og gå til siden for din gaffel av Plan ₿ Network repository. Dette er gaffelen du har etablert på GitHub. URL-adressen til gaffelen din skal se slik ut: `https://github.com/[ditt-brukernavn]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Sørg for at du er på hovedgrenen `dev`, og klikk deretter på `Sync fork`-knappen. Hvis gaffelen din ikke er oppdatert, vil GitHub tilby å oppdatere grenen din. Fortsett med denne oppdateringen. Hvis grenen din derimot allerede er oppdatert, vil GitHub informere deg om dette:

![TUTO](assets/fr/04.webp)

Åpne GitHub Desktop-programvaren og sørg for at gaffelen din er riktig valgt i øvre venstre hjørne av vinduet:

![TUTO](assets/fr/05.webp)

Klikk på knappen `Fetch origin`. Hvis det lokale depotet ditt allerede er oppdatert, vil GitHub Desktop ikke foreslå noen ytterligere tiltak. I motsatt fall vises alternativet `Pull origin`. Klikk på denne knappen for å oppdatere det lokale depotet:

![TUTO](assets/fr/06.webp)

Kontroller at du faktisk er på hovedgrenen `dev`:

![TUTO](assets/fr/07.webp)

Klikk på denne grenen, og klikk deretter på knappen Ny gren:

![TUTO](assets/fr/08.webp)

Sørg for at den nye grenen er basert på kildearkivet, nemlig `PlanB-Network/bitcoin-educational-content`.

Gi grenen et navn som tydeliggjør formålet med tittelen, og bruk bindestreker for å skille ordene fra hverandre. La oss for eksempel si at målet vårt er å skrive en veiledning om hvordan du bruker programvaren Sparrow Wallet. I dette tilfellet kan arbeidsgrenen som er dedikert til å skrive denne opplæringen få navnet: `tuto-sparrow-wallet-loic`. Når du har angitt et passende navn, klikker du på `Opprett gren` for å bekrefte opprettelsen av grenen:

![TUTO](assets/fr/09.webp)

Klikk nå på knappen `Publish branch` for å lagre den nye arbeidsgrenen i din online fork på GitHub:

![TUTORIAL](assets/fr/10.webp)

Nå, på GitHub Desktop, bør du befinne deg på den nye grenen din. Dette betyr at alle endringer som gjøres lokalt på datamaskinen din, utelukkende vil bli lagret på denne spesifikke grenen. Så lenge denne grenen er valgt på GitHub Desktop, vil filene som er synlige lokalt på maskinen din også være filene til denne grenen (`tuto-sparrow-wallet-loic`), og ikke filene til hovedgrenen (`dev`).

![TUTORIAL](assets/fr/11.webp)

For hver nye artikkel du ønsker å publisere, må du opprette en ny gren fra `dev`. En gren i Git er en parallell versjon av prosjektet, som gjør at du kan gjøre endringer uten at det påvirker hovedgrenen, inntil arbeidet er klart til å slås sammen.

## 2 - Legge til opplæringsfilene

Nå som arbeidsgrenen er opprettet, er det på tide å integrere den nye opplæringen. Du har to alternativer: Bruk Python-skriptet mitt, som automatiserer opprettelsen av de nødvendige dokumentene, eller opprett hver fil manuelt. Vi skal se på trinnene du må følge for hvert alternativ.

### Med Python-skriptet mitt

Du må installere på maskinen din:
- Python 3.8 eller nyere.

For å bruke skriptet, naviger til mappen der det er lagret. Skriptet ligger i Plan ₿ Network sitt datalager under banen: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Når du er i mappen, installer avhengighetene:

```bash
pip install -r requirements.txt
```

Deretter starter du programvaren med følgende kommando:

```bash
python3 main.py
```

Et grafisk brukergrensesnitt (GUI) vil åpnes. Første gang må du fylle inn all nødvendig informasjon, men ved senere bruk vil skriptet huske dine personlige opplysninger, slik at du slipper å skrive dem inn på nytt.

![DATA-CREATOR-PY](assets/fr/37.webp)

Start med å angi den lokale banen til `/tutorials`-mappen i din klon av repositoriet (`.../bitcoin-educational-content/tutorials/`). Du kan skrive den inn manuelt eller klikke på "Browse"-knappen for å navigere via filutforskeren.

![DATA-CREATOR-PY](assets/fr/38.webp)

Velg språket du skal skrive opplæringen din på.

![DATA-CREATOR-PY](assets/fr/39.webp)

I feltet "Contributor's GitHub ID", skriv inn ditt GitHub-brukernavn.

![DATA-CREATOR-PY](assets/fr/40.webp)

I feltet "PBN professor's ID", skriv inn din identifikator ved hjelp av ordene fra BIP39-listen, slik det vises på [din professorprofil](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![DATA-CREATOR-PY](assets/fr/41.webp)

Hvis du ikke har en professorprofil ennå, sjekk ut denne opplæringen:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Klikk deretter på knappen "New Tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Velg en hovedkategori for opplæringen din. Deretter velger du en passende underkategori basert på hovedkategorien du valgte.

![DATA-CREATOR-PY](assets/fr/43.webp)

Bestem vanskelighetsgraden for opplæringen.

![DATA-CREATOR-PY](assets/fr/44.webp)

Velg navnet på katalogen som er opprettet spesielt for opplæringen din. Navnet på denne mappen bør reflektere programvaren som dekkes i opplæringen og bruke bindestreker for å skille ordene. For eksempel kan mappen hete `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` er UUID-en til selskapet eller organisasjonen bak verktøyet som dekkes i opplæringen, tilgjengelig [i listen over prosjekter](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). For eksempel, for en opplæring om Sparrow Wallet, finner du `project_id` i filen: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Denne informasjonen legges til i YAML-filen for opplæringen din, fordi Plan ₿ Network opprettholder en database over selskaper og organisasjoner som er aktive innen Bitcoin eller relaterte prosjekter. Ved å legge til `project_id` kobler du innholdet ditt til den relevante enheten.

***Oppdatering:*** I den nye versjonen av skriptet trenger du ikke lenger å skrive inn `project_id` manuelt. En søkefunksjon er lagt til for å finne prosjektet etter navn og automatisk hente den tilsvarende `project_id`. Skriv inn begynnelsen av prosjektnavnet i feltet "Project Name" for å søke etter det, og velg deretter ønsket selskap fra rullegardinmenyen. `project_id` vil automatisk fylles ut i feltet under. Du kan også skrive det inn manuelt om nødvendig.

![DATA-CREATOR-PY](assets/fr/46.webp)

For tagger, velg 2 eller 3 relevante nøkkelord relatert til innholdet i opplæringen din, og velg dem utelukkende fra [Plan ₿ Networks tagliste](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Programvaren har også en søkefunksjon med en rullegardinliste.

![DATA-CREATOR-PY](assets/fr/47.webp)

Når all informasjon er fylt inn og verifisert, klikk på "Create Tutorial" for å bekrefte opprettelsen av filene til opplæringen din. Dette vil lokalt generere opplæringsmappen din og alle nødvendige filer innenfor den valgte kategorien.

![DATA-CREATOR-PY](assets/fr/48.webp)

Du kan nå hoppe over underseksjonen "Uten Python-skriptet mitt", samt trinn 3 "Fylle ut YAML-filen", siden skriptet allerede har fullført disse handlingene automatisk for deg. Gå direkte til trinn 4 og begynn å skrive opplæringen din.

For mer informasjon om dette Python-skriptet, kan du også lese [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Uten Python-skriptet mitt

Åpne filbehandleren din og naviger til mappen `bitcoin-educational-content`, som representerer den lokale klonen av ditt repository. Du finner den vanligvis under `Documents\GitHub\bitcoin-educational-content`.

Inne i denne katalogen må du finne riktig undermappe for å plassere opplæringen din. Mappestrukturen gjenspeiler de forskjellige seksjonene på Plan ₿ Network-nettstedet. I vårt eksempel, siden vi ønsker å legge til en opplæring om Sparrow Wallet, skal vi navigere til følgende bane: `bitcoin-educational-content\tutorials\wallet`, som tilsvarer `WALLET`-seksjonen på nettstedet:

![TUTO](assets/fr/12.webp)

I mappen `wallet` må du opprette en ny mappe som er spesielt dedikert til opplæringen din. Navnet på denne mappen skal minne om programvaren som dekkes i opplæringen, og du må sørge for å koble sammen ord med bindestreker. I mitt eksempel vil mappen hete `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

I denne nye undermappen som er dedikert til opplæringen din, må du legge til flere elementer:


- Opprett en mappe med `assets`, som skal inneholde alle illustrasjonene som er nødvendige for opplæringen;
- I denne `assets`-mappen må du opprette en undermappe som er navngitt i henhold til originalspråket for opplæringen. Hvis opplæringen for eksempel er skrevet på engelsk, må denne undermappen hete `en`. Plasser alt det visuelle materialet i opplæringen der (diagrammer, bilder, skjermbilder osv.).
- En `tutorial.yml`-fil må opprettes for å registrere detaljene knyttet til opplæringen;
- Det skal opprettes en fil i markdown-format for å skrive det faktiske innholdet i opplæringen. Denne filen må ha en tittel som samsvarer med språkkoden for det som skrives. For eksempel må filen hete `fr.md` for en veiledning som er skrevet på fransk.

![TUTO](assets/fr/14.webp)

For å oppsummere, her er hierarkiet av filer som skal opprettes:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Fyll inn YAML-filen

Fyll ut filen `tutorial.yml` ved å kopiere følgende mal:

```yaml
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
````

Her er detaljene for de obligatoriske feltene:


- **id**: En UUID (_Universally Unique Identifier_) for å identifisere opplæringen på en unik måte. Du kan generere den med [et nettbasert verktøy] (https://www.uuidgenerator.net/version4). Det eneste kravet er at denne UUID-en skal være tilfeldig for å unngå konflikt med en annen UUID på plattformen;
- **project_id**: UUID-en til selskapet eller organisasjonen som står bak verktøyet som presenteres i opplæringen [fra listen over prosjekter] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Hvis du for eksempel lager en veiledning om programvaren Sparrow Wallet, kan du finne denne `project_id` i følgende fil: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Denne informasjonen er lagt til i YAML-filen i opplæringen din fordi Plan ₿ Network vedlikeholder en database over alle selskaper og organisasjoner som opererer på Bitcoin eller relaterte prosjekter. Ved å legge til `project_id` for enheten som er relatert til opplæringen din, oppretter du en kobling mellom de to elementene;
- **tags**: 2 eller 3 relevante nøkkelord relatert til innholdet i opplæringen, valgt utelukkende [fra listen over tagger i Plan ₿ Network] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Underkategorien som tilsvarer innholdet i opplæringen, i henhold til strukturen på Plan ₿ Network-nettstedet (for eksempel for lommebøker: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: Vanskelighetsgraden for opplæringen, blant annet:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Ditt `contributor_id` (BIP39-ord) slik det vises på [din professorprofil] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: Originalspråket for opplæringen (for eksempel `fr`, `en` osv.);
- **proofreading**: Informasjon om korrekturlesingsprosessen. Fyll ut den første delen, ettersom korrekturlesing av din egen veiledning teller som en første validering:
    - **language**: Språkkode for korrekturlesingen (for eksempel `fr`, `en`, osv.).
    - **last_contribution_date**: Dagens dato.
    - **urgency**: La stå tomt.
    - **contributors_id**: GitHub-ID-en din.
    - **reward**: La stå tomt.

Hvis du vil ha mer informasjon om professoridentifikatoren, kan du se den tilhørende veiledningen:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Her er et eksempel på en ferdig `tutorial.yml`-fil for en opplæring om Blockstream Green-lommeboken:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Tittel]
description: [Beskrivelse]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```