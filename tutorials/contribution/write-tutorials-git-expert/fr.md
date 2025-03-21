---
name: Contribution - Tutoriel avec Git (avancé)
description: Guide pour utilisateurs avancés pour proposer un tutoriel sur Plan ₿ Network avec Git
---
![cover](assets/cover.webp)

Avant de suivre ce tutoriel sur l'ajout d'un nouveau tutoriel, vous devez avoir complété quelques étapes préliminaires. Si ce n'est pas encore fait, je vous invite à consulter d'abord ce tutoriel introductif, puis à revenir ici :

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Vous avez déjà :
- Choisi le thème de votre tutoriel ;
- Contacté l'équipe de Plan ₿ Network via [le groupe Telegram](https://t.me/PlanBNetwork_ContentBuilder) ou paolo@planb.network ;
- Choisi vos outils de contribution.

Dans ce tutoriel destiné aux utilisateurs expérimentés de Git, nous allons brièvement résumer les étapes clés et les directives essentielles pour proposer un nouveau tutoriel sur Plan ₿ Network. Si vous n'êtes pas familier avec Git et GitHub, je vous recommande plutôt de suivre un de ces 2 autres tutoriels plus détaillés qui vous accompagneront pas à pas :

- **Intermédiaire (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- **Débutants (interface web)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Outils suggérés

Pour l’édition de fichiers Markdown :
- **Obsidian** (Gratuit, non open-source)
- **Mark Text** (Gratuit, open-source)
- **Zettlr** (Gratuit, open-source)
- **Typora** (Payant, ~15 €, non open-source)

Pour Git :
- **Git** (Gratuit, open-source)
- **GitHub Desktop** (Gratuit, open-source)
- **Sourcetree** (Gratuit, non open-source)

Pour l’édition de fichiers YAML :
- **Visual Studio Code** (Gratuit, open-source)
- **Sublime Text** (Gratuit avec limitations, non open-source)

Pour la création de schémas et visuels :
- **Canva** (Gratuit avec options payantes, non open-source)
- **Inkscape** (Gratuit, open-source)
- **Penpot** (Gratuit, open-source)

## Flux de travail

### 1 - Configurez votre environnement local

- Vous devez avoir votre propre fork du [dépôt Plan ₿ Network sur GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synchronisez la branche principale (`dev`) de votre fork avec le dépôt source.
- Mettez à jour votre clone local.

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

### 2 - Créez une nouvelle branche

- Assurez-vous d’être sur la branche `dev`.
- Créez une nouvelle branche avec un nom descriptif (par exemple : `tuto-green-wallet-loic`).
- Publiez cette branche sur votre fork en ligne.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev

# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic

# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Ajoutez les documents du tutoriel

***Note :*** Vous pouvez automatiser les étapes 3 et 4 en utilisant [mon script GUI Python](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Exécutez-le directement depuis son dossier dans votre clone local, puis remplissez les champs requis sur la GUI. Pour plus d'informations sur son installation et son utilisation, consultez le [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Si vous préférez le faire manuellement, suivez ces étapes :

- Repérez le dossier approprié dans le dépôt local (ex. : `tutorials/wallet`).
- Créez un répertoire dédié au tutoriel avec un nom clair (ex. : `green-wallet`). Ce nom de dossier déterminera également le chemin d’URL du tutoriel. Il doit être en minuscules, sans caractères spéciaux (excepté les tirets) et sans espaces.
- Ajoutez les éléments suivants dans ce répertoire :
    - Un sous-dossier nommé `assets` contenant :
        - Deux images `.webp` :
            - `logo.webp` : Le logo du tutoriel (format carré avec un fond). Ce logo doit représenter le logiciel ou l’outil présenté. Si le tutoriel n’est pas spécifique à un outil (ex. : un guide général sur la génération d’une phrase mnémonique), vous pouvez choisir un visuel adapté (par exemple : une icône générique).
            - `cover.webp` : Une image de couverture affichée au début du tutoriel.
        - Un sous-dossier portant le code de la langue d’origine du tutoriel. Par exemple, si le tutoriel est écrit en anglais, ce sous-dossier doit être nommé `en`. Placez-y tous les visuels du tutoriel (schémas, images, captures d’écran, etc.).
    - Un fichier `tutorial.yml` contenant les métadonnées (auteur, tags, catégorie, niveau de difficulté, etc.).
    - Un fichier Markdown contenant le tutoriel, nommé selon le code de la langue (ex. : `fr.md`, `en.md`, etc.).

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

### 4 - Remplissez le fichier YAML

- Complétez le fichier `tutorial.yml` en suivant ce modèle :

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
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"

# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```

- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.

### 7 - Relecture et fusion

- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"

# Poussez les corrections sur votre fork
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

- **Illustrations et schémas** :
    - Toutes les images doivent être au format WebP. Utilisez cet outil gratuit pour les convertir si besoin : [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nommez les visuels avec 2 ou 3 chiffres (ex. : `001.webp`, `002.webp`).
    - Pour les tutoriels sur mobile ou hardware wallets, utilisez des maquettes.
    - Utilisez uniquement des visuels créés par vous ou libres de droits.
    - Assurez-vous de leur pertinence et qualité.

- **Charte graphique** :
    - Police : [Rubik](https://fonts.google.com/specimen/Rubik).
    - Couleurs Plan ₿ Network :
        - Orange : `#FF5C00`
        - Noir : `#000000`
        - Blanc : `#FFFFFF`

Si vous rencontrez des difficultés techniques pour soumettre votre tutoriel, n'hésitez pas à demander de l'aide sur [notre groupe Telegram dédié aux contributions](https://t.me/PlanBNetwork_ContentBuilder). Merci !
