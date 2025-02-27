---
name: Contribution - Git-opastus (edistyneet)
description: Opas edistyneille käyttäjille, joka tarjoaa opastuksen Plan ₿ Network with Git -ohjelmasta
---
![cover](assets/cover.webp)

Ennen kuin seuraat tätä ohjeistusta uuden ohjeen lisäämisestä, sinun on suoritettava muutama alustava vaihe. Jos et ole vielä tehnyt sitä, tutustu ensin tähän johdantooppaaseen ja palaa sitten tänne :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Sinulla on jo :


- Valitse opetusohjelmasi teema;
- Ota yhteyttä Plan ₿ Network -tiimiin [Telegram-ryhmässä] (https://t.me/PlanBNetwork_ContentBuilder) tai paolo@planb.network ;
- Valitse osallistumisvälineesi.

Tässä kokeneille Git-käyttäjille suunnatussa opetusohjelmassa kerromme lyhyesti keskeiset vaiheet ja olennaiset ohjeet uuden Plan ₿ Network -oppaan tarjoamiseksi. Jos Git ja GitHub eivät ole sinulle tuttuja, suosittelen sen sijaan seuraamaan yhtä näistä kahdesta muusta, yksityiskohtaisemmasta opetusohjelmasta, jotka vievät sinut askel askeleelta :


- Keskitason (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Aloittelijoille (verkkokäyttöliittymä)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Ehdotetut työkalut

Markdown-tiedostojen muokkaamiseen :


- Obsidian** (ilmainen, ei avointa lähdekoodia)
- Mark Text** (ilmainen, avoin lähdekoodi)
- Zettlr** (ilmainen, avoin lähdekoodi)
- Typora** (maksullinen, ~15 €, ei avointa lähdekoodia)

Gitille :


- Git** (ilmainen, avoin lähdekoodi)
- GitHub Desktop** (ilmainen, avoin lähdekoodi)
- Sourcetree** (ilmainen, ei avoin lähdekoodi)

YAML-tiedostojen muokkaamiseen :


- Visual Studio Code** (ilmainen, avoin lähdekoodi)
- Sublime Text** (ilmainen rajoituksin, ei avointa lähdekoodia)

Kaavioiden ja visuaalisten esitysten luominen :


- Canva** (ilmainen ja maksullisia vaihtoehtoja, ei avointa lähdekoodia)
- Inkscape** (ilmainen, avoin lähdekoodi)
- Penpot** (ilmainen, avoin lähdekoodi)

## Työnkulut

### 1 - Määritä paikallinen ympäristö


- Sinulla on oltava oma haarasi [Plan ₿ Network -tietovarastosta GitHubissa](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synkronoi haarasi päähaara (`dev`) lähdekoodivaraston kanssa.
- Päivitä paikallinen kloonisi.

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

### 2 - Luo uusi haara


- Varmista, että olet `dev`-haarassa.
- Luo uusi haara kuvaavalla nimellä (esim. `tuto-green-wallet-loic`).
- Julkaise tämä haara verkkohaarassasi.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Lisää opetusdokumentit

***Huomautus:*** Voit automatisoida vaiheet 3 ja 4 käyttämällä [Python GUI -skriptiäni](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Suorita se suoraan sen kansiosta paikallisessa kloonissasi ja täytä sitten vaaditut kentät graafisessa käyttöliittymässä. Lisätietoja sen asentamisesta ja käyttämisestä on [README]-julkaisussa(https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Jos haluat tehdä sen manuaalisesti, noudata seuraavia ohjeita :


- Etsi sopiva kansio paikallisesta arkistosta (esim. `tutorials/wallet`).
- Luo opetusohjelmalle oma hakemisto, jolla on selkeä nimi (esim. `green-wallet`). Tämä kansion nimi määrittää myös opetusohjelman URL-polun. Sen tulisi olla pienaakkosin, ilman erikoismerkkejä (paitsi väliviivoja) ja ilman välilyöntejä.
- Lisää tähän hakemistoon seuraavat kohteet:
    - Alikansio nimeltä `assets`, joka sisältää :
        - Kaksi .webp-kuvaa:
            - `logo.webp`: (neliön muotoinen ja taustalla). Logon on edustettava esiteltyä ohjelmistoa tai työkalua. Jos opetusohjelma ei koske tiettyä työkalua (esim. yleinen opas muistisanojen luomiseen), voit valita sopivan visuaalisen ilmeen (esim. yleisen kuvakkeen).
            - `cover.webp`: Kannen kuva, joka näytetään opetusohjelman alussa.
        - Alikansio, jossa on opetusohjelman alkuperäisen kielen koodi. Jos opetusohjelma on esimerkiksi kirjoitettu englanniksi, tämän alikansion nimi on `en'. Sijoita kaikki opetusohjelman visuaalinen materiaali (kaaviot, kuvat, kuvakaappaukset jne.) tähän kansioon.
    - `tutorial.yml`-tiedosto, joka sisältää metatietoja (tekijä, tunnisteet, kategoria, vaikeustaso jne.).
    - Markdown-tiedosto, joka sisältää opetusohjelman ja joka on nimetty kielikoodin mukaan (esim. `fr.md`, `en.md`, jne.).

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

### 4 - Täytä YAML-tiedosto


- Täydennä `tutorial.yml`-tiedosto seuraavasti:

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

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tunnisteet:


  - lompakot
  - ohjelmisto
  - avaimet

kategoria: mobiili

taso: aloittelija

krediittejä:

professori: pretty-private

# Metatietojen oikolukeminen

original_language: fr

oikoluku:


  - kieli: fr

last_contribution_date: 2024-11-20

kiireellisyys:

avustajat_id:


      - LoicPandul

palkinto:

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

# Luo commit, jolla on kuvaava viesti

git commit -m "Lisää vihreän lompakon opetusohjelma"

# Työnnä muutokset haarukkaan

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Luo tehtyjä korjauksia kuvaava sitoumus

git commit -m "Korjaukset green-wallet-oppaaseen tehdyn tarkistuksen jälkeen"

# Työnnä korjauksia haarukkaan

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hei, Bitcoin!")

```