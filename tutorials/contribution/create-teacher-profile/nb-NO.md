---
name: Professor Plan ₿ Network
description: Hvordan legger jeg til eller endrer lærerprofilen min på Plan ₿ Network?
---
![cover](assets/cover.webp)

Hvis du planlegger å bidra til Plan ₿ Network ved å skrive en ny veiledning eller et nytt kurs, trenger du en lærerprofil. Denne profilen vil gjøre det mulig for deg å motta de riktige krediteringene for innholdet du bidrar med på plattformen.

De av dere som allerede har vært med på å lage pedagogisk innhold på Plan ₿ Network, har sannsynligvis allerede en lærerprofil. Du finner den i mappen `/professors` [på GitHub-depotet vårt] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Hvis profilen din allerede finnes, finner du påloggingen din i filen `professor.yml`.

Hvis du vil gjøre endringer i profilen din, kan du gå til avsnittet "Rediger lærerprofilen din" på slutten av denne veiledningen.

## Legg til en ny lærer med vår programvare

Den enkleste måten å opprette lærerprofilen din på Plan ₿ Network er å bruke vårt integrerte Python-verktøy. Her er hvordan det fungerer.

### 1 - Konfigurer ditt lokale miljø

Du må ha din egen Fork fra [Plan ₿ Network repository on GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).

Synkroniser hovedgrenen (`dev`) i Fork med kildelageret.

Oppdater din lokale klone.

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

### 2 - Opprett en ny filial

Sørg for at du er på `dev`-grenen. Opprett en ny gren med et beskrivende navn (f.eks. `add-professor-loic-morel`).

Publiser denne grenen på Fork på nettet.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Opprett lærerprofilen din

Gå til mappen `scripts/tutorial-related/data-creator/` på din lokale klone. Sørg for at du har installert alle avhengighetene som kreves for programvaren, etter først å ha installert Python :

```bash
pip install -r requirements.txt
```

Start deretter programvaren med kommandoen :

```bash
python3 main.py
```

Når du er på startsiden, skriver du inn den lokale stien til klonen av repositoriet ditt, språket du skriver på og GitHub-ID-en din. Hvis du oppretter denne profilen for noen andre og allerede har en professorprofil, skriver du inn ID-en din i feltet "*PBN Professor's ID*". Hvis du oppretter din egen profil, vil du ikke ha en professor-ID ennå, siden du er i ferd med å opprette en, så la dette feltet stå tomt.

Klikk deretter på knappen "*Ny professor*".

![Image](assets/fr/01.webp)

Fyll ut den nødvendige informasjonen (vær oppmerksom på at all denne informasjonen vil være offentlig både på vår plattform og på GitHub) :


- Navn på lærerfilen (bruk for- og etternavn eller et pseudonym, med små bokstaver) ;
- Ditt navn eller kallenavn ;
- Tilfeldig generering av påloggingen din ;
- Ditt nettsted og din profil X (valgfritt) ;
- En Lightning Address for å motta donasjoner fra leserne (valgfritt) ;
- Velg 2 eller 3 tagger fra listen;
- Klikk på "*Velg bilde*" for å velge et profilbilde fra de lokale mappene dine (du kan bruke hvilket som helst navn og format på bildet, og programvaren tilpasser det automatisk). Bare sørg for at bildet er kvadratisk);
- Skriv en kort beskrivelse av profilen din.

Fullfør opprettelsen ved å klikke på "*Create Professor*". Dette vil automatisk generate alle filene som kreves for profilen din.

![Image](assets/fr/02.webp)

Lagre endringene lokalt ved å opprette en commit med en forklarende melding. Skyv endringene til Fork GitHub.

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

Når du er ferdig, oppretter du en Pull Request (PR) på GitHub for å foreslå integrering av endringene dine. Legg til en tittel og en kort beskrivelse i PR-en.

### 4 - Korrekturlesing og sammenslåing

Vent på validering eller tilbakemelding fra en administrator. Gjør om nødvendig rettelser og publiser nye commits.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

Når PR-en er slått sammen, kan du slette arbeidsgrenen din.

## Endre lærerprofilen din

Hvis du behersker Git, kan du endre lærerprofilen din ved å opprette en ny gren og redigere den relevante filen direkte i den eksisterende mappen. Endringer kan gjøres enten i filen `professor.yml` eller i markdown-filen, avhengig av hvilken informasjon som skal korrigeres. Når du har gjort endringene lokalt, kan du pushe dem til Fork og sende inn en PR.

For nybegynnere anbefaler jeg å gjøre modifikasjonen direkte via GitHubs Interface-web. Sørg for at du har en GitHub-konto. Hvis du ikke vet hvordan du oppretter en, kan du følge denne veiledningen :

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Gå til [Plan ₿ Network GitHub-arkivet dedikert til data] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Klikk på mappen "*professorer*", og gå deretter til din personlige mappe.

![Image](assets/fr/04.webp)

Hvis du vil endre metadata for profilen din, for eksempel Lightning Address, navn eller lenker, velger du filen "*professor.yml*". Hvis du vil endre beskrivelsen din, klikker du på YAML-filen for språket ditt (f.eks. "*en.yml*" eller "*fr.yml*").

Hvis du endrer beskrivelsen din, må du huske å fjerne alle foreldede oversettelser. Deretter kan du enten oversette beskrivelsen til de andre språkene ved hjelp av en LLM, eller bare la beskrivelsen være på morsmålet ditt og nevne i Pull-forespørselen din at beskrivelsen må oversettes av teamet vårt.

![Image](assets/fr/05.webp)

Klikk på blyantikonet når du er inne på filen du ønsker å endre.

![Image](assets/fr/06.webp)

Hvis du ikke allerede har en Fork fra Plan ₿ Network repository, vil GitHub foreslå at du oppretter en. Klikk på "*Fork this repository*".

![Image](assets/fr/07.webp)

Gjør de ønskede endringene i filen. Når du er ferdig, klikker du på "*Commit changes*".

![Image](assets/fr/08.webp)

Skriv inn en melding som beskriver endringen, og velg deretter "*Foreslå endringer*".

![Image](assets/fr/09.webp)

En oppsummering av endringene dine vises. Hvis du ønsker å gjøre ytterligere endringer i profilen din, kan du gå tilbake til mappene og gjøre flere commits. Når du er ferdig, klikker du på "*Create pull request*".

En pull-forespørsel er en forespørsel om å integrere endringer fra din gren i hovedgrenen i Plan ₿ Network-arkivet, slik at du kan gå gjennom og diskutere endringene før de slås sammen.

![Image](assets/fr/10.webp)

Sørg for at arbeidsgrenen din øverst i Interface er slått sammen med `dev`-grenen i Plan ₿ Network-repositoryet (som er hovedgrenen).

Skriv inn en tittel som kort oppsummerer endringene du ønsker å slå sammen med kildelageret. Legg til en kort kommentar som beskriver endringene, og klikk deretter på Green-knappen "*Create pull request*" for å bekrefte pull-forespørselen:

![Image](assets/fr/11.webp)

PR-en din vil da være synlig i "*Pull Request*"-fanen i hovedarkivet til Plan ₿ Network. Alt du trenger å gjøre nå er å vente på at en administrator skal slå sammen modifikasjonen din.

![Image](assets/fr/12.webp)

Hvis du støter på tekniske problemer med å sende inn endringen din, ikke nøl med å be om hjelp på [vår Telegram-gruppe dedikert til bidrag] (https://t.me/PlanBNetwork_ContentBuilder). Tusen takk skal du ha!