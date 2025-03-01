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

In this tutorial for experienced Git users, we'll briefly summarize the key steps and essential guidelines for offering a new Plan ₿ Network tutorial. If you're unfamiliar with Git and GitHub, I recommend you instead follow one of these other 2 more detailed tutorials that will take you step by step :


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

### 2 - Create a new branch


- Make sure you're on the `dev` branch.
- Create a new branch with a descriptive name (e.g. `tuto-green-wallet-loic`).
- Publish this branch on your online fork.

```
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

### 4 - Fill in the YAML file


- Complete the `tutorial.yml` file as follows:

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

Here are the required fields:


- id**: A UUID (_Universally Unique Identifier_) to uniquely identify the tutorial. You can generate it with [an online tool](https://www.uuidgenerator.net/version4). The only constraint is that this UUID must be random, so as not to conflict with another UUID on the platform;
- project_id** : The UUID of the company or organization behind the tool presented in the tutorial [from the list of projects](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). For example, if you're doing a tutorial on the Green Wallet software, you can find this `project_id` in the following file: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. This information is added in the YAML file of your tutorial because Plan ₿ Network maintains a database of all companies and organizations operating on Bitcoin or related projects. By adding the `project_id` of the linked entity to your tutorial, you create a link between the two elements;
- tags**: 2 or 3 relevant keywords related to the tutorial content, chosen exclusively [from the Plan ₿ Network tag list](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- category** : The subcategory corresponding to the tutorial content, according to the Plan ₿ Network structure (e.g. for wallets: `desktop`, `hardware`, `mobile`, `backup`) ;
- level** : Tutorial difficulty level, from :
    - beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- professor**: Your `contributor_id` (BIP39 words) as displayed on [your teacher profile](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language** : The original language of the tutorial (e.g. `fr`, `en`, etc.) ;
- proofreading**: Information about the proofreading process. Fill in the first part, because proofreading your own tutorial counts as a first validation:
    - language**: Proofreading language code (e.g. `fr`, `en`, etc.).
    - last_contribution_date**: Today's date.
    - urgency** : Leave blank.
    - contributors_id** : Your GitHub ID.
    - reward** : Leave blank.

For more details on your teacher ID, please refer to the corresponding tutorial :

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

### 5 - Write the content


- Complete the Markdown file properties with :
    - The title (`name`).
    - A short description (`description`).
- Add the cover image at the top of the tutorial using Markdown syntax (replace "green" with the name of the tool shown):

```
![cover-green](assets/cover.webp)
```


- Write the tutorial content in Markdown :
    - Use well-structured headings (`##`), lists and paragraphs.
    - Insert visuals using Markdown syntax :

```
![nom-image](assets/en/001.webp)
```


- Place diagrams and images in the corresponding language subfolder, in `/assets`.

### 6 - Save and submit the tutorial


- Save your changes locally by creating a commit with a descriptive message.
- Push the changes to your GitHub fork.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Once finished, create a Pull Request (PR) on GitHub to propose the integration of your modifications.
- Add a title and a brief description to the PR. Mention the corresponding issue number in the comment.

### 7 - Proofreading and merging


- Wait for validation or feedback from an administrator.
- If necessary, make corrections and push new commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Once the PR has been merged, you can delete your working branch.

## Content creation standards


- Formatting supported on the platform** :
    - Classic Markdown: lists, links, images, quotes, bold, italics, etc.
    - LaTeX (block only, not inline): delimited by `$$`.
    - Inline code: Syntax with a single backtick.
    - Code blocks: Syntax with three backticks, for example :

```
print("Hello, Bitcoin!")
```


- Illustrations and diagrams** :
    - All images must be in WebP format. Use this free tool to convert them if required: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Name visuals with 2 or 3 digits (e.g. `001.webp`, `002.webp`).
    - For mobile or hardware wallet tutorials, use mock-ups.
    - Use only self-created or royalty-free visuals.
    - Make sure they are relevant and of high quality.
- Graphic charter** :
    - Font: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Colors Plan ₿ Network :
        - Orange: `#FF5C00`
        - Black: `#000000`
        - White: `#FFFFFF`

If you're having technical difficulties submitting your tutorial, please don't hesitate to ask for help on [our dedicated Telegram group for contributions](https://t.me/PlanBNetwork_ContentBuilder). Thank you very much!