---
name: Bidrag - Git-opplæring (avansert)
description: Veiledning for avanserte brukere med opplæring i Plan ₿ Nettverk med Git
---
![cover](assets/cover.webp)

Før du følger denne veiledningen om hvordan du legger til en ny opplæring, må du ha fullført noen innledende trinn. Hvis du ikke allerede har gjort det, kan du ta en titt på denne introduksjonsveiledningen først, og deretter komme tilbake hit :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Du har allerede :


- Velg et tema for opplæringen din;
- Kontaktet Plan ₿ Network-teamet via [Telegramgruppe] (https://t.me/PlanBNetwork_ContentBuilder) eller paolo@planb.network ;
- Velg dine bidragsverktøy.

I denne veiledningen for erfarne Git-brukere vil vi kort oppsummere de viktigste trinnene og de viktigste retningslinjene for å tilby en ny Plan ₿ Nettverksveiledning. Hvis du ikke er kjent med Git og GitHub, anbefaler jeg at du i stedet følger en av disse to andre mer detaljerte veiledningene som tar deg steg for steg :


- Mellomnivå (GitHub Desktop)** :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Nybegynnere (webgrensesnitt)** :

https://planb.network/tutorials/contribution/tutorial/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

```
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

```
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

```
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

```
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
```

Her er de obligatoriske feltene:


- id**: En UUID (_Universally Unique Identifier_) for å identifisere opplæringen på en unik måte. Du kan generere den med [et nettbasert verktøy] (https://www.uuidgenerator.net/version4). Den eneste begrensningen er at denne UUID-en må være tilfeldig, slik at den ikke kommer i konflikt med en annen UUID på plattformen;
- project_id** : UUID-en til selskapet eller organisasjonen som står bak verktøyet som presenteres i opplæringen [fra listen over prosjekter] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Hvis du for eksempel lager en veiledning om Green Wallet-programvaren, kan du finne denne `project_id` i følgende fil: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Denne informasjonen er lagt til i YAML-filen i opplæringen din fordi Plan ₿ Network vedlikeholder en database over alle selskaper og organisasjoner som opererer på Bitcoin eller relaterte prosjekter. Ved å legge til `project_id` for den koblede enheten i opplæringen din, oppretter du en kobling mellom de to elementene;
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

### 5 - Skriv innholdet


- Fullfør Markdown-filens egenskaper med :
    - Tittelen (`navn`).
    - En kort beskrivelse (`description`).
- Legg til forsidebildet øverst i veiledningen ved hjelp av Markdown-syntaks (erstatt "grønn" med navnet på verktøyet som vises):

```
![cover-green](assets/cover.webp)
```


- Skriv opplæringsinnholdet i Markdown :
    - Bruk velstrukturerte overskrifter (`##`), lister og avsnitt.
    - Sett inn bilder ved hjelp av Markdown-syntaks :

```
![nom-image](assets/en/001.webp)
```


- Plasser diagrammer og bilder i undermappen for det aktuelle språket, i `/assets`.

### 6 - Lagre og send inn veiledningen


- Lagre endringene lokalt ved å opprette en commit med en beskrivende melding.
- Skyv endringene til GitHub-gaffelen din.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Når du er ferdig, oppretter du en Pull Request (PR) på GitHub for å foreslå integrering av endringene dine.
- Legg til en tittel og en kort beskrivelse av PR-en. Oppgi det tilsvarende problemnummeret i kommentaren.

### 7 - Korrekturlesing og sammenslåing


- Vent på bekreftelse eller tilbakemelding fra en administrator.
- Gjør om nødvendig rettelser og publiser nye commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Når PR-en er slått sammen, kan du slette arbeidsgrenen din.

## Standarder for innholdsproduksjon


- Formatering støttes på plattformen** :
    - Klassisk Markdown: lister, lenker, bilder, anførselstegn, fet skrift, kursiv osv.
    - LaTeX (kun blokk, ikke inline): avgrenset av `$$`.
    - Innebygd kode: Syntaks med en enkelt backtick.
    - Kodeblokker: Syntaks med tre backticks, for eksempel :

```
print("Hello, Bitcoin!")
```


- Illustrasjoner og diagrammer** :
    - Alle bilder må være i WebP-format. Bruk dette gratisverktøyet for å konvertere dem om nødvendig: [ImagesConverter] (https://github.com/LoicPandul/ImagesConverter).
    - Navngi bilder med 2 eller 3 siffer (f.eks. `001.webp`, `002.webp`).
    - Bruk mock-ups for opplæring i mobil- eller maskinvarelommebøker.
    - Bruk kun egenproduserte eller royaltyfrie bilder.
    - Sørg for at de er relevante og av høy kvalitet.
- Grafisk charter** :
    - Skrifttype: [Rubik] (https://fonts.google.com/specimen/Rubik).
    - Farger Plan ₿ Nettverk :
        - Oransje: `#FF5C00`
        - Svart: `#000000`
        - Hvit: `#FFFFFFFF`

Hvis du har tekniske problemer med å sende inn opplæringen din, ikke nøl med å be om hjelp på [vår dedikerte Telegram-gruppe for bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tusen takk skal du ha!