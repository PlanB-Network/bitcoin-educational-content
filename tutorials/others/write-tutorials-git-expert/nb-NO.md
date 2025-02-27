---
name: Bidrag - Git-opplæring (avansert)
description: Veiledning for avanserte brukere med opplæring i Plan ₿ Nettverk med Git
---
![cover](assets/cover.webp)

Før du følger denne veiledningen om hvordan du legger til en ny opplæring, må du ha fullført noen innledende trinn. Hvis du ikke allerede har gjort det, kan du ta en titt på denne introduksjonsveiledningen først, og deretter komme tilbake hit :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Du har allerede :


- Velg et tema for opplæringen din;
- Kontaktet Plan ₿ Network-teamet via [Telegramgruppe] (https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network ;
- Velg dine bidragsverktøy.

I denne veiledningen for erfarne Git-brukere vil vi kort oppsummere de viktigste trinnene og de viktigste retningslinjene for å tilby en ny Plan ₿ Nettverksveiledning. Hvis du ikke er kjent med Git og GitHub, anbefaler jeg at du i stedet følger en av disse to andre, mer detaljerte veiledningene som tar deg steg for steg :


- Mellomnivå (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Nybegynnere (webgrensesnitt)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Foreslåtte verktøy

For redigering av Markdown-filer :


- Obsidian** (gratis, ikke åpen kildekode)
- Mark Text** (gratis, åpen kildekode)
- Zettlr** (gratis, åpen kildekode)
- Typora** (betalingsprogramvare, ~€15, ikke åpen kildekode)

For Git :


- Git** (gratis, åpen kildekode)
- GitHub Desktop** (gratis, åpen kildekode)
- Sourcetree** (gratis, ikke åpen kildekode)

For redigering av YAML-filer :


- Visual Studio Code** (gratis, åpen kildekode)
- Sublime Text** (gratis med begrensninger, ikke åpen kildekode)

For å lage diagrammer og visualiseringer :


- Canva** (gratis med betalte alternativer, ikke åpen kildekode)
- Inkscape** (gratis, åpen kildekode)
- Penpot** (gratis, åpen kildekode)

## Arbeidsflyt

### 1 - Konfigurer ditt lokale miljø


- Du må ha din egen gaffel av [Plan ₿ Network repository på GitHub] (https://github.com/PlanB-Network/bitcoin-educational-content).
- Synkroniser hovedgrenen (`dev`) i gaffelen din med kildelageret.
- Oppdater din lokale klone.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
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

### 2 - Opprett en ny filial


- Sørg for at du er på `dev`-grenen.
- Opprett en ny gren med et beskrivende navn (f.eks. `tuto-green-wallet-loic`).
- Publiser denne grenen på din online fork.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Legg til opplæringsdokumentene

***Merk: *** Du kan automatisere trinn 3 og 4 ved hjelp av [mitt Python GUI-skript] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Kjør det direkte fra mappen i din lokale klone, og fyll deretter ut de nødvendige feltene i GUI-en. For mer informasjon om hvordan du installerer og bruker det, se [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Hvis du foretrekker å gjøre det manuelt, følger du disse trinnene :


- Finn den aktuelle mappen i det lokale depotet (f.eks. `tututorials/wallet`).
- Opprett en mappe dedikert til opplæringen med et tydelig navn (f.eks. `green-wallet`). Dette mappenavnet vil også bestemme URL-banen til opplæringen. Det bør skrives med små bokstaver, uten spesialtegn (bortsett fra bindestreker) og uten mellomrom.
- Legg til følgende elementer i denne katalogen:
    - En undermappe med navnet `assets` som inneholder :
        - To `.webp`-bilder:
            - `logo.webp`: Logoen for opplæringen (kvadratisk format med bakgrunn). Denne logoen må representere programvaren eller verktøyet som presenteres. Hvis opplæringen ikke er spesifikk for et verktøy (f.eks. en generell veiledning for å generere en mnemoteknisk frase), kan du velge et passende visuelt element (f.eks. et generisk ikon).
            - `cover.webp`: Et forsidebilde som vises i starten av opplæringen.
        - En undermappe med koden til opplæringens originalspråk. Hvis opplæringen for eksempel er skrevet på engelsk, bør denne undermappen hete `en'. Plasser alt det visuelle materialet (diagrammer, bilder, skjermbilder osv.) i denne mappen.
    - En `tutorial.yml`-fil som inneholder metadata (forfatter, tagger, kategori, vanskelighetsgrad osv.).
    - En Markdown-fil som inneholder veiledningen, navngitt i henhold til språkkoden (f.eks. `fr.md`, `en.md` osv.).

```bash
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Fyll inn YAML-filen


- Fullfør filen `tutorial.yml` på følgende måte:

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
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

prosjekt_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:


  - lommebøker
  - programvare
  - nøkler

kategori: mobil

nivå: nybegynner

kreditter:

professor: pretty-private

# Korrekturlesing av metadata

original_language: fr

korrekturlesing:


  - språk: fr

last_contribution_date: 2024-11-20

det haster:

bidragsytere_id:


      - LoicPandul

belønning:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Opprett en forpliktelse med en beskrivende melding

git commit -m "Legg til green-wallet tutorial"

# Skyv modifikasjonene opp på gaffelen

git push origin tuto-grønn-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Opprett en commit som beskriver korrigeringene som er gjort

git commit -m "Rettelser etter gjennomgang av green-wallet-opplæringen"

# Trykk på korreksjoner på gaffelen din

git push origin tuto-grønn-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hallo, Bitcoin!")

```