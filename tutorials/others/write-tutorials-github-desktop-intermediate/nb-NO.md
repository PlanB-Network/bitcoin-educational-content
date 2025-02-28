---
name: Bidrag - Opplæring med GitHub Desktop (middels nivå)
description: Komplett guide til Plan ₿ Nettverksopplæring med GitHub Desktop
---
![cover](assets/cover.webp)

Før du følger denne veiledningen om hvordan du legger til en ny opplæring, må du ha fullført noen innledende trinn. Hvis du ikke allerede har gjort det, kan du ta en titt på denne introduksjonsveiledningen først, og deretter komme tilbake hit :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Du har allerede :


- Velg et tema for opplæringen din;
- Kontaktet Plan ₿ Network-teamet via [Telegramgruppe] (https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network ;
- Velg dine bidragsverktøy.

I denne veiledningen skal vi se på hvordan du legger til opplæringen din i Plan ₿ Network ved å konfigurere det lokale miljøet ditt med GitHub Desktop. Hvis du allerede behersker Git, er det ikke sikkert at denne svært detaljerte opplæringen er nødvendig for deg. I stedet anbefaler jeg at du tar en titt på denne andre veiledningen, der jeg kun presenterer de generelle retningslinjene, uten detaljert trinn-for-trinn-veiledning:


- Erfarne brukere** :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Hvis du foretrekker å ikke konfigurere ditt lokale miljø, kan du følge denne andre opplæringen designet for nybegynnere, der vi gjør endringene direkte via GitHubs webgrensesnitt :


- Nybegynnere (webgrensesnitt)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Forutsetninger

Programvare som kreves for å følge denne opplæringen :


- [GitHub Desktop] (https://desktop.github.com/);
- En markdown-filredigerer som [Obsidian] (https://obsidian.md/);
- En kodeditor ([VSC](https://code.visualstudio.com/) eller [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Forutsetninger før du starter opplæringen :


- Har en [GitHub-konto] (https://github.com/signup);
- Ha en gaffel av [Plan ₿ Network source repository] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Ha [en lærerprofil på Plan ₿ Network] (https://planb.network/professors) (bare hvis du tilbyr en fullstendig veiledning).

Hvis du trenger hjelp med å skaffe deg disse forutsetningene, kan du finne hjelp i de andre veiledningene mine:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Når alt er på plass og det lokale miljøet ditt er satt opp med din egen Plan ₿ Network-gaffel, kan du begynne å legge til opplæringen.

## 1 - Opprett en ny filial

Åpne nettleseren din og naviger til gaffelsiden din i Plan ₿ Network repository. Dette er gaffelen du har opprettet på GitHub. URL-adressen til gaffelen din skal se slik ut: `https://github.com/[ditt-brukernavn]/bitcoin-educational-content` :

![TUTO](assets/fr/03.webp)

Sørg for at du er på hovedgrenen `dev`, og klikk deretter på knappen `Sync fork`. Hvis gaffelen din ikke er oppdatert, vil GitHub be deg om å oppdatere grenen din. Fortsett med denne oppdateringen. Hvis grenen din derimot allerede er oppdatert, vil GitHub informere deg om dette:

![TUTO](assets/fr/04.webp)

Åpne GitHub Desktop og sørg for at gaffelen din er riktig valgt øverst i venstre hjørne av vinduet:

![TUTO](assets/fr/05.webp)

Klikk på knappen `Fetch origin`. Hvis det lokale depotet ditt allerede er oppdatert, vil GitHub Desktop ikke foreslå ytterligere tiltak. I motsatt fall vises alternativet `Pull origin`. Klikk på denne knappen for å oppdatere det lokale depotet:

![TUTO](assets/fr/06.webp)

Sjekk at du er på hovedgrenen `dev`:

![TUTO](assets/fr/07.webp)

Klikk på denne grenen, og klikk deretter på knappen Ny gren:

![TUTO](assets/fr/08.webp)

Sørg for at den nye grenen er basert på kildelageret, dvs. `PlanB-Network/bitcoin-educational-content`.

Navngi grenen slik at tittelen er tydelig når det gjelder formålet, og bruk bindestreker for å skille ordene fra hverandre. La oss for eksempel si at målet vårt er å skrive en veiledning om hvordan du bruker Sparrow Wallet. I dette tilfellet kan arbeidsgrenen som er dedikert til å skrive denne veiledningen få navnet: `tuto-sparrow-wallet-loic`. Når du har angitt det riktige navnet, klikker du på `Opprett gren` for å bekrefte opprettelsen av grenen:

![TUTO](assets/fr/09.webp)

Klikk nå på knappen `Publish branch` for å lagre den nye arbeidsgrenen på din online fork på GitHub :

![TUTO](assets/fr/10.webp)

Nå, på GitHub Desktop, bør du være på den nye grenen din. Dette betyr at alle endringer du gjør lokalt på datamaskinen din, vil bli lagret utelukkende på denne spesifikke grenen. Så lenge denne grenen er valgt på GitHub Desktop, vil filene som er synlige lokalt på maskinen din, være filene til denne grenen (`tuto-sparrow-wallet-loic`), og ikke filene til hovedgrenen (`dev`).

![TUTO](assets/fr/11.webp)

For hver nye artikkel du vil publisere, må du opprette en ny gren fra `dev`. En gren i Git er en parallell versjon av prosjektet, slik at du kan gjøre endringer uten at det påvirker hovedgrenen, helt til arbeidet er klart til å slås sammen.

## 2 - Legg til opplæringsfiler

Nå som arbeidsgrenen er opprettet, er det på tide å integrere den nye opplæringen. Du har to alternativer: Bruk Python-skriptet mitt, som automatiserer opprettelsen av de nødvendige dokumentene, eller opprett hver fil manuelt. La oss ta en titt på trinnene du må følge for hvert alternativ.

### Med Python-skriptet mitt

Du må installere :


- Python 3.8 eller nyere ;
- Avhengigheter som kreves for skriptet. Kjør :

```bash
pip install customtkinter appdirs
````
Pour utiliser le script, rendez-vous dans le dossier où il est stocké. Le script se trouve dans le dépôt de data de Plan ₿ Network sous le chemin : `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.
Une fois dans le dossier, exécutez la commande :
```

python new-tutorial-creation.py

```
Une interface graphique (GUI) va s'ouvrir. La première fois, vous devrez entrer toutes les informations nécessaires, mais lors des utilisations ultérieures du script, vos informations personnelles seront mémorisées, ce qui vous évite de devoir les saisir de nouveau.
![TUTO](assets/fr/37.webp)
Commencez par indiquer le chemin local menant au dossier `/tutorials` sur votre clone du dépôt (`.../bitcoin-educational-content/tutorials/`). Vous pouvez le noter manuellement ou cliquer sur le bouton "Browse" pour naviguer via votre explorateur de fichiers.
![TUTO](assets/fr/38.webp)
Sélectionnez la langue dans laquelle vous rédigerez votre tutoriel.
![TUTO](assets/fr/39.webp)
Choisissez une catégorie principale pour votre tutoriel.
![TUTO](assets/fr/40.webp)
Ensuite, sélectionnez une sous-catégorie appropriée, en fonction de la catégorie principale que vous avez choisie.
![TUTO](assets/fr/41.webp)
Déterminez un niveau de difficulté pour le tutoriel.
![TUTO](assets/fr/42.webp)
Choisissez le nom du répertoire spécialement créé pour votre tutoriel. Le nom de ce dossier devrait refléter le logiciel abordé dans le tutoriel, en utilisant des tirets pour relier les mots. Par exemple, le dossier pourrait s'appeler `red-wallet` :
![TUTO](assets/fr/43.webp)
Le `project_id` est l'UUID de l'entreprise ou de l'organisation derrière l'outil présenté dans le tutoriel, disponible [dans la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, pour un tutoriel sur le logiciel Sparrow Wallet, vous trouverez ce `project_id` dans le fichier : `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Cette information est ajoutée au fichier YAML de votre tutoriel car Plan ₿ Network maintient une base de données des entreprises et organisations actives sur Bitcoin ou des projets connexes. En ajoutant le `project_id` associé à votre tutoriel, vous créez un lien entre votre contenu et l'entité concernée.
***Mise à jour :*** Dans la nouvelle version du script, vous n'avez plus besoin de saisir manuellement le `project_id`. Une fonction de recherche a été ajoutée pour trouver le projet par son nom et récupérer automatiquement le `project_id` correspondant. Tapez le début du nom du projet dans la case "Project name" pour le rechercher, puis sélectionnez l'entreprise souhaitée dans le menu déroulant. Le `project_id` sera automatiquement renseigné dans la case en dessous. Vous avez également la possibilité de le noter manuellement si nécessaire.
![TUTO](assets/fr/44.webp)
Pour les tags, sélectionnez 2 ou 3 mots-clés pertinents en relation avec le contenu de votre tutoriel, en les choisissant exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).
![TUTO](assets/fr/45.webp)
Dans la case "Contributor's GitHub ID", inscrivez votre identifiant GitHub.
![TUTO](assets/fr/46.webp)
Pour la case "PBN professor's ID", saisissez votre identifiant en utilisant les mots de la liste BIP39, tel qu'il apparaît sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).
![TUTO](assets/fr/47.webp)
Pour plus de détails sur votre identifiant de professeur, veuillez consulter le tutoriel suivant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Une fois toutes les informations saisies et vérifiées, cliquez sur "Create Tutorial" pour valider la création des fichiers de votre tutoriel. Cela générera en local le dossier de votre tutoriel et tous les fichiers nécessaires dans le dossier de la catégorie sélectionnée.
![TUTO](assets/fr/48.webp)
Vous pouvez maintenant passer outre la sous-partie "Sans mon script Python", ainsi que l'étape 3 "Remplir le fichier YAML", car le script a déjà effectué ces actions automatiquement pour vous. Passez directement à l'étape 4 et à la rédaction de votre tutoriel.
Pour plus d'informations sur ce script Python, vous pouvez également [consulter son README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).
### Sans mon script Python
Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`.
Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web Plan ₿ Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![TUTO](assets/fr/12.webp)
Au sein du dossier `wallet`, il faut créer un nouveau répertoire spécifiquement dédié à votre tutoriel. Le nom de ce dossier doit évoquer le logiciel traité dans le tutoriel, en veillant à relier les mots par des tirets. Pour mon exemple, le dossier sera intitulé `sparrow-wallet` :
![TUTO](assets/fr/13.webp)
Dans ce nouveau sous-dossier dédié à votre tutoriel, il faut ajouter plusieurs éléments :
- Créez un dossier `assets`, destiné à recevoir toutes les illustrations nécessaires à votre tutoriel ;
- Au sein de ce dossier `assets`, il faut créer un sous-dossier nommé selon le code de langue originale du tutoriel. Par exemple, si le tutoriel est rédigé en anglais, ce sous-dossier doit être nommé `en`. Placez-y tous les visuels du tutoriel (schémas, images, captures d’écran, etc.).
- Un fichier `tutorial.yml` doit être créé pour y consigner les détails relatifs à votre tutoriel ;
- Un fichier en format markdown est à créer pour y rédiger le contenu effectif de votre tutoriel. Ce fichier doit être intitulé selon le code de la langue de rédaction. Par exemple, pour un tutoriel rédigé en français, le fichier devra s'appeler `fr.md`.
![TUTO](assets/fr/14.webp)
Pour résumer, voici la hiérarchie des fichiers à créer :
```

bitcoin-pedagogisk-innhold/

└── tutorials/

└── lommebok/ (bytt til riktig kategori)

└── sparrow-wallet/ (modifiser med tuto-navn)

├── eiendeler/

│ ├── en/ (bytt til riktig språkkode)

├── tutorial.yml

└── fr.md (skal modifiseres i henhold til den aktuelle språkkoden)

```
## 3 - Remplir le fichier YAML
Remplissez le fichier `tutorial.yml` en copiant le modèle suivant :
```

id:

prosjekt_id:

tags:

-

-

-

kategori:

nivå:

kreditter:

professor:

# Korrekturlesing av metadata

original_language:

korrekturlesing:


  - språk:

siste_bidrag_dato:

det haster:

bidragsytere_id:

-

belønning:

````

Her er de obligatoriske feltene:


- id**: En UUID (_Universally Unique Identifier_) for å identifisere opplæringen på en unik måte. Du kan generere den med [et nettbasert verktøy] (https://www.uuidgenerator.net/version4). Den eneste begrensningen er at denne UUID-en må være tilfeldig, slik at den ikke kommer i konflikt med en annen UUID på plattformen;
- project_id** : UUID-en til selskapet eller organisasjonen som står bak verktøyet som presenteres i opplæringen [fra listen over prosjekter] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Hvis du for eksempel lager en veiledning om programvaren Sparrow Wallet, kan du finne denne `project_id` i følgende fil: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Denne informasjonen er lagt til i YAML-filen i opplæringen din fordi Plan ₿ Network vedlikeholder en database over alle selskaper og organisasjoner som opererer på Bitcoin eller relaterte prosjekter. Ved å legge til `project_id` for den koblede enheten i opplæringen din, oppretter du en kobling mellom de to elementene;
- tagger**: 2 eller 3 relevante nøkkelord relatert til opplæringsinnholdet, valgt utelukkende [fra Plan ₿ Network-tagglisten] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- kategori** : Underkategorien som tilsvarer innholdet i opplæringen, i henhold til Plan ₿ Nettverksstruktur (f.eks. for lommebøker: `desktop`, `hardware`, `mobile`, `backup`) ;
- nivå** : Opplæringens vanskelighetsgrad, fra :
    - nybegynner``
    - "mellomliggende
    - `avansert`
    - `ekspert`
- professor**: Ditt `contributor_id` (BIP39-ord) slik det vises på [lærerprofilen din] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language** : Originalspråket for opplæringen (f.eks. `fr`, `en`, osv.) ;
- korrekturlesing**: Informasjon om korrekturlesingsprosessen. Fyll ut den første delen, fordi korrekturlesing av din egen veiledning teller som en første validering:
    - språk**: Korrekturlesing av språkkode (f.eks. `fr`, `en` osv.).
    - siste_bidrag_dato**: Dagens dato.
    - haster** : La stå tomt.
    - contributors_id** : Din GitHub-ID.
    - belønning** : La stå tomt.

For mer informasjon om lærer-ID-en din, se den tilhørende veiledningen :

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Her er et eksempel på en `tutorial.yml`-fil som er fylt ut for en opplæring om Blockstream Green-lommeboken:

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
```

Når du er ferdig med å redigere filen `tutorial.yml`, lagrer du dokumentet ved å klikke på `File > Save` :

![TUTO](assets/fr/16.webp)

Du kan nå lukke kodeditoren.

## 4 - Fyll ut Markdown-filen

Nå kan du åpne opplæringsfilen din, navngitt med språkkoden din, f.eks. Gå til Obsidian, på venstre side av vinduet, og bla nedover mappetreet til opplæringsmappen og den ønskede filen :

![TUTO](assets/fr/18.webp)

Klikk på filen for å åpne den:

![TUTO](assets/fr/19.webp)

Vi begynner med å fylle ut `Properties`-delen helt øverst i dokumentet.

![TUTO](assets/fr/20.webp)

Legg til og fyll inn følgende kodeblokk manuelt:

```markdown
---
name: [Titre]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Skriv inn navnet på opplæringen og en kort beskrivelse:

![TUTO](assets/fr/22.webp)

Legg deretter til banen til forsidebildet i begynnelsen av opplæringen. Dette gjør du ved å notere :

```markdown
![cover-sparrow](assets/cover.webp)
```

Denne syntaksen er nyttig når du trenger å legge til et bilde i opplæringen din. Utropstegnet indikerer et bilde, hvis alternative tekst (alt) er spesifisert mellom de firkantede parentesene. Stien til bildet er angitt mellom parentesene:

![TUTO](assets/fr/23.webp)

## 5 - Legg til logo og omslag

I mappen `assets` må du legge til en fil med navnet `logo.webp`, som skal fungere som miniatyrbilde for artikkelen din. Dette bildet må være i `.webp`-format og kvadratisk i størrelse for å matche brukergrensesnittet. Du kan velge logoen til programvaren som omtales i veiledningen, eller et hvilket som helst annet relevant bilde, så lenge det er royaltyfritt. I tillegg legger du til et bilde med tittelen `cover.webp` på samme sted. Dette vil vises øverst i opplæringen. Sørg for at dette bildet, i likhet med logoen, respekterer bruksrettighetene og passer inn i konteksten til opplæringen:

![TUTO](assets/fr/17.webp)

## 6 - Skrive veiledningen og legge til bilder

Fortsett å skrive innholdet i opplæringen. Når du vil inkludere en undertittel, bruker du riktig markdown-formatering ved å sette `##` foran teksten:

![TUTO](assets/fr/24.webp)

Undermappen for språk i mappen `assets` brukes til å lagre diagrammer og bilder som skal følge med opplæringen. Unngå så langt det er mulig å inkludere tekst i bildene for å gjøre innholdet tilgjengelig for et internasjonalt publikum. Programvaren som presenteres, vil selvfølgelig inneholde tekst, men hvis du legger til skjemaer eller ytterligere indikasjoner på skjermbildene av programvaren, bør du gjøre det uten tekst eller, hvis det er viktig, bruke engelsk.

![TUTO](assets/fr/25.webp)

Når du skal navngi bildene dine, bruker du ganske enkelt numre som tilsvarer rekkefølgen de vises i i opplæringen, formatert som to sifre (eller tre sifre hvis opplæringen inneholder mer enn 99 bilder). Gi for eksempel det første bildet navnet `01.webp`, det andre `02.webp`, og så videre.

Bildene dine må kun være i `.webp`-format. Om nødvendig kan du bruke [my image conversion software] (https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

For å sette inn et diagram i dokumentet bruker du følgende kommando i Markdown, og er nøye med å angi riktig alternativ tekst og riktig bildebane:

```markdown
![sparrow](assets/fr/01.webp)
```

Utropstegnet i begynnelsen indikerer et bilde. Den alternative teksten, som bidrar til tilgjengelighet og referanser, er plassert mellom hakeparentesene. Til slutt er stien til bildet angitt mellom parentesene.

Hvis du ønsker å lage dine egne skjemaer, må du følge Plan ₿ Network grafiske retningslinjer for å sikre visuell konsistens:


- Skrifttype**: Bruk [Rubik] (https://fonts.google.com/specimen/Rubik);
- Farger** :
 - Oransje: #FF5C00
 - Svart : #000000
 - Hvit: #FFFFFFFF

**Det er viktig at alle bilder som integreres i opplæringsvideoene dine er fri for opphavsrett eller respekterer kildefilens lisens**. Derfor er alle diagrammer som publiseres på Plan ₿ Network gjort tilgjengelig under en CC-BY-SA-lisens, på samme måte som teksten.

**-> Tips:** Når du deler filer offentlig, for eksempel bilder, er det viktig å fjerne overflødige metadata. Disse kan inneholde sensitiv informasjon, for eksempel stedsdata, dato for opprettelse og forfatterdetaljer. For å beskytte personvernet ditt er det lurt å fjerne disse metadataene. For å forenkle denne operasjonen kan du bruke spesialiserte verktøy som [Exif Cleaner] (https://exifcleaner.com/), som gjør det mulig å rydde opp i et dokuments metadata ved hjelp av enkel dra-og-slipp-funksjon.

## 7 - Lagre og foreslå veiledningen

Når du er ferdig med å skrive opplæringen på det språket du ønsker, er neste trinn å sende inn en **Pull Request**. Administratoren vil deretter legge til de manglende oversettelsene i opplæringen din, ved hjelp av vår automatiserte oversettelsesmetode med menneskelig korrekturlesing.

For å utføre en Pull Request åpner du GitHub Desktop. Programvaren bør automatisk oppdage eventuelle endringer du har gjort lokalt på grenen din i det opprinnelige repositoriet. Før du fortsetter, bør du sjekke nøye på venstre side av grensesnittet at disse endringene samsvarer med det du forventet:

![TUTO](assets/fr/28.webp)

Legg til en tittel for overføringen, og klikk deretter på den blå knappen `Commit to [your branch]` for å validere endringene:

![TUTO](assets/fr/29.webp)

En commit er en registrering av endringer som er gjort i en gren, ledsaget av en beskrivende melding, slik at du kan følge utviklingen av et prosjekt over tid. Det er et slags mellomliggende sjekkpunkt.

Klikk deretter på `Push origin`-knappen. Dette vil sende din commit til din fork:

![TUTO](assets/fr/30.webp)

Hvis du ikke er ferdig med opplæringen, kan du komme tilbake til den senere og gjøre nye overføringer. Hvis du er ferdig med å redigere denne grenen, klikker du på knappen `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Du kan sjekke en siste gang at endringene dine er korrekte, og deretter klikke på knappen `Create pull request`:

![TUTO](assets/fr/32.webp)

En Pull Request er en forespørsel om å integrere endringer fra din gren i hovedgrenen i Plan ₿ Network-arkivet, noe som gjør det mulig å gjennomgå og diskutere endringer før de slås sammen.

Du vil automatisk bli omdirigert i nettleseren din til GitHub på forberedelsessiden for Pull Request :

![TUTO](assets/fr/33.webp)

Skriv inn en tittel som kort oppsummerer endringene du ønsker å slå sammen med kildelageret. Legg til en kort kommentar som beskriver endringene (hvis du har et problemnummer knyttet til opprettelsen av opplæringen, må du huske å skrive `Lukker #{problemnummer}` som en kommentar), og klikk deretter på den grønne knappen `Opprett pull-forespørsel` for å bekrefte fletteforespørselen:

![TUTO](assets/fr/34.webp)

PR-en din vil da være synlig i fanen `Pull Request` i Plan ₿ Network-repository. Alt du trenger å gjøre nå, er å vente til en administrator kontakter deg for å bekrefte at bidraget ditt har blitt slått sammen, eller for å be om ytterligere endringer.

![TUTO](assets/fr/35.webp)

Etter at du har slått sammen PR-en din med hovedgrenen, anbefaler vi at du sletter arbeidsgrenen din (`tuto-sparrow-wallet`) for å opprettholde en ren historikk på gaffelen din. GitHub vil tilby deg dette alternativet automatisk på PR-siden din:

![TUTO](assets/fr/36.webp)

På GitHub Desktop kan du flytte tilbake til hovedgrenen til gaffelen din (`dev`).

![TUTO](assets/fr/07.webp)

Hvis du ønsker å gjøre endringer i bidraget ditt etter at du allerede har sendt inn PR-en din, avhenger stegene du må følge av PR-ens nåværende status:


- Hvis PR-en din fortsatt er åpen og ennå ikke har blitt slått sammen, kan du gjøre endringene lokalt, på samme gren. Når endringene er ferdigstilt, bruker du `Push origin`-knappen for å legge til en ny forpliktelse til den fortsatt åpne PR-en;
- Hvis PR-en din allerede er slått sammen med hovedgrenen, må du gjøre prosessen på nytt fra begynnelsen ved å opprette en ny gren og deretter sende inn en ny PR. Sørg for at det lokale depotet ditt er synkronisert med Plan ₿ Network-kilderegisteret før du fortsetter.

Hvis du har tekniske problemer med å sende inn opplæringen din, ikke nøl med å be om hjelp på [vår dedikerte Telegram-gruppe for bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tusen takk skal du ha!