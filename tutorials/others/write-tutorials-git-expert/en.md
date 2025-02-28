---
name: Contribution - Git tutorial (advanced)
description: Guide for advanced users to offer a tutorial on Plan ₿ Network with Git
---
![cover](assets/cover.webp)

Before following this tutorial on adding a new tutorial, you need to have completed a few preliminary steps. If you haven't already done so, please take a look at this introductory tutorial first, then come back here :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
You already have :


- Choose a theme for your tutorial;
- Contacted the Plan ₿ Network team via [Telegram group](https://t.me/PlanBNetwork_ContentBuilder) or paolo@planb.network ;
- Choose your contribution tools.

In this tutorial for experienced Git users, we'll briefly summarize the key steps and essential guidelines for offering a new Plan ₿ Network tutorial. If you're not familiar with Git and GitHub, I recommend you instead follow one of these 2 other, more detailed tutorials that will take you step by step :


- Intermediate (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Beginners (web interface)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Suggested tools

For editing Markdown files :


- Obsidian** (Free, not open-source)
- Mark Text** (Free, open-source)
- Zettlr** (Free, open-source)
- Typora** (Payware, ~€15, not open-source)

For Git :


- Git** (Free, open-source)
- GitHub Desktop** (Free, open-source)
- Sourcetree** (Free, not open-source)

For editing YAML files :


- Visual Studio Code** (Free, open-source)
- Sublime Text** (Free with limitations, not open-source)

To create diagrams and visuals :


- Canva** (Free with paid options, not open-source)
- Inkscape** (Free, open-source)
- Penpot** (Free, open-source)

## Workflows

### 1 - Configure your local environment


- You must have your own fork of the [Plan ₿ Network repository on GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synchronize the main branch (`dev`) of your fork with the source repository.
- Update your local clone.

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

### 2 - Create a new branch


- Make sure you're on the `dev` branch.
- Create a new branch with a descriptive name (e.g. `tuto-green-wallet-loic`).
- Publish this branch on your online fork.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Add the tutorial documents

***Note:*** You can automate steps 3 and 4 using [my Python GUI script](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Run it directly from its folder in your local clone, then fill in the required fields on the GUI. For more information on how to install and use it, see the [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

If you prefer to do it manually, follow these steps :


- Locate the appropriate folder in the local repository (e.g. `tutorials/wallet`).
- Create a directory dedicated to the tutorial with a clear name (e.g. `green-wallet`). This folder name will also determine the URL path of the tutorial. It should be in lower case, with no special characters (except hyphens) and no spaces.
- Add the following items to this directory:
    - A subfolder named `assets` containing :
        - Two `.webp` images:
            - `logo.webp`: The tutorial logo (square format with background). This logo must represent the software or tool presented. If the tutorial is not specific to a tool (e.g.: a general guide to generating a mnemonic phrase), you can choose a suitable visual (e.g.: a generic icon).
            - `cover.webp`: A cover image displayed at the start of the tutorial.
        - A subfolder bearing the code of the tutorial's original language. For example, if the tutorial is written in English, this subfolder should be named `en'. Place all the tutorial's visuals (diagrams, images, screenshots, etc.) in this folder.
    - A `tutorial.yml` file containing metadata (author, tags, category, difficulty level, etc.).
    - A Markdown file containing the tutorial, named according to the language code (e.g. `fr.md`, `en.md`, etc.).

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

### 4 - Fill in the YAML file


- Complete the `tutorial.yml` file as follows:

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

# Create a commit with a descriptive message

git commit -m "Add green-wallet tutorial"

# Push your modifications onto your fork

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Create a commit describing the corrections made

git commit -m "Corrections following review of green-wallet tutorial"

# Push corrections on your fork

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

print("Hello, Bitcoin!")

```