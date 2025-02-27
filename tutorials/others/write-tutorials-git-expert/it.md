---
name: Contributo - Tutorial Git (avanzato)
description: Guida per utenti avanzati per offrire un tutorial sul Piano ₿ Rete con Git
---
![cover](assets/cover.webp)

Prima di seguire questo tutorial sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passaggi preliminari. Se non l'avete ancora fatto, date prima un'occhiata a questo tutorial introduttivo e poi tornate qui:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Avete già :


- Scegliete un tema per il vostro tutorial;
- Contattare il team di Plan ₿ Network tramite [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Scegliete gli strumenti di contribuzione.

In questo tutorial per utenti esperti di Git, riassumeremo brevemente i passaggi chiave e le linee guida essenziali per offrire un nuovo tutorial di Rete Plan ₿. Se non avete familiarità con Git e GitHub, vi consiglio di seguire uno di questi due tutorial più dettagliati che vi accompagneranno passo dopo passo:


- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Principianti (interfaccia web)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Strumenti suggeriti

Per modificare i file Markdown :


- Obsidian** (gratuito, non open-source)
- Mark Text** (gratuito, open-source)
- Zettlr** (gratuito, open-source)
- Typora** (Payware, ~€15, non open-source)

Per Git :


- Git** (gratuito, open-source)
- GitHub Desktop** (gratuito, open-source)
- Sourcetree** (gratuito, non open-source)

Per la modifica dei file YAML :


- Visual Studio Code** (gratuito, open-source)
- Sublime Text** (gratuito con limitazioni, non open-source)

Per creare diagrammi e immagini :


- Canva** (gratuito con opzioni a pagamento, non open-source)
- Inkscape** (gratuito, open-source)
- Penpot** (gratuito, open-source)

## Flussi di lavoro

### 1 - Configurare l'ambiente locale


- È necessario disporre di un proprio fork del [repository di Plan ₿ Network su GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sincronizzare il ramo principale (`dev`) del fork con il repository dei sorgenti.
- Aggiornare il clone locale.

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

### 2 - Creare un nuovo ramo


- Assicurarsi di essere nel ramo `dev`.
- Creare un nuovo ramo con un nome descrittivo (ad esempio, `tuto-green-wallet-loic`).
- Pubblicate questo ramo sul vostro fork online.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Aggiungere i documenti del tutorial

***Nota: *** È possibile automatizzare i passaggi 3 e 4 utilizzando [il mio script Python GUI](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Eseguirlo direttamente dalla sua cartella nel clone locale, quindi compilare i campi richiesti dalla GUI. Per ulteriori informazioni su come installarlo e usarlo, vedere il [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Se preferite farlo manualmente, seguite questi passaggi:


- Individuare la cartella appropriata nel repository locale (ad esempio, `tutorials/wallet`).
- Creare una cartella dedicata al tutorial con un nome chiaro (ad esempio `green-wallet`). Il nome di questa cartella determinerà anche il percorso URL del tutorial. Deve essere scritto in minuscolo, senza caratteri speciali (tranne i trattini) e senza spazi.
- Aggiungete i seguenti elementi a questa directory:
    - Una sottocartella denominata `assets` contenente :
        - Due immagini `.webp`:
            - `logo.webp`: Il logo del tutorial (formato quadrato con sfondo). Questo logo deve rappresentare il software o lo strumento presentato. Se il tutorial non è specifico per uno strumento (ad esempio, una guida generale alla generazione di una frase mnemonica), si può scegliere un'immagine adatta (ad esempio, un'icona generica).
            - `cover.webp`: Immagine di copertina visualizzata all'inizio dell'esercitazione.
        - Una sottocartella con il codice della lingua originale del tutorial. Ad esempio, se il tutorial è scritto in inglese, questa sottocartella dovrebbe essere denominata `en'. In questa cartella vanno inseriti tutti gli elementi visivi del tutorial (diagrammi, immagini, screenshot, ecc.).
    - Un file `tutorial.yml` contenente metadati (autore, tag, categoria, livello di difficoltà, ecc.).
    - Un file Markdown contenente il tutorial, denominato in base al codice della lingua (ad esempio, `fr.md`, `en.md`, ecc.).

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

### 4 - Compilare il file YAML


- Completare il file `tutorial.yml` come segue:

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

progetto_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tag:


  - portafogli
  - software
  - chiavi

categoria: mobile

livello: principiante

crediti:

professore: pretty-private

# Correzione dei metadati

lingua_originale: fr

correzione di bozze:


  - lingua: fr

last_contribution_date: 2024-11-20

urgenza:

collaboratori_id:


      - LoicPandul

ricompensa:

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

# Creare un commit con un messaggio descrittivo

git commit -m "Aggiungere tutorial sul portafoglio verde"

# Spingere le modifiche sulla forchetta

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Creare un commit che descriva le correzioni apportate

git commit -m "Correzioni in seguito alla revisione del tutorial sul portafoglio verde"

# Spingere le correzioni sulla forcella

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

print("Ciao, Bitcoin!")

```