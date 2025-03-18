---
name: Contributo - Tutorial Git (avanzato)
description: Guida per utenti avanzati per offrire un tutorial sul Piano ₿ Rete con Git
---
![cover](assets/cover.webp)

Prima di seguire questo tutorial sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passaggi preliminari. Se non l'avete ancora fatto, date prima un'occhiata a questo tutorial introduttivo e poi tornate qui:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Avete già :


- Scegliete un tema per il vostro tutorial;
- Contattare il team di Plan ₿ Network tramite [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Scegliete gli strumenti di contribuzione.

In questo tutorial per utenti esperti di Git, riassumeremo brevemente i passaggi chiave e le linee guida essenziali per offrire un nuovo tutorial di Rete Plan ₿. Se non avete familiarità con Git e GitHub, vi consiglio di seguire uno di questi due tutorial più dettagliati che vi accompagneranno passo dopo passo:


- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Principianti (interfaccia web)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

### 2 - Creare un nuovo ramo


- Assicurarsi di essere nel ramo `dev`.
- Creare un nuovo ramo con un nome descrittivo (ad esempio, `tuto-green-wallet-loic`).
- Pubblicate questo ramo sul vostro fork online.

```
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

### 4 - Compilare il file YAML


- Completare il file `tutorial.yml` come segue:

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

Ecco i campi obbligatori:


- id**: Un UUID (_Universally Unique Identifier_) per identificare in modo univoco il tutorial. È possibile generarlo con [uno strumento online](https://www.uuidgenerator.net/version4). L'unico vincolo è che questo UUID deve essere casuale, in modo da non entrare in conflitto con un altro UUID della piattaforma;
- project_id** : L'UUID dell'azienda o dell'organizzazione che sta dietro allo strumento presentato nell'esercitazione [dall'elenco dei progetti] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Per esempio, se si sta facendo un tutorial sul software Green Wallet, si può trovare questo `project_id` nel seguente file: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Questa informazione viene aggiunta nel file YAML del tutorial perché Plan ₿ Network mantiene un database di tutte le aziende e organizzazioni che operano su Bitcoin o su progetti correlati. Aggiungendo il `project_id` dell'entità collegata al tutorial, si crea un collegamento tra i due elementi;
- tag**: 2 o 3 parole chiave pertinenti al contenuto del tutorial, scelte esclusivamente [dall'elenco dei tag della Rete Plan ₿](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- categoria** : La sottocategoria corrispondente al contenuto del tutorial, secondo la struttura del Piano ₿ Network (ad esempio, per i portafogli: `desktop`, `hardware`, `mobile`, `backup`) ;
- livello** : Livello di difficoltà del tutorial, da :
    - principiante`
    - `intermedio`
    - avanzato
    - esperto
- professore**: Il vostro `contributor_id` (parole BIP39) come visualizzato nel [vostro profilo docente](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- lingua_originale** : La lingua originale del tutorial (es. `fr`, `en`, ecc.) ;
- correzione di bozze**: Informazioni sul processo di correzione. Compilare la prima parte, perché la correzione del proprio tutorial conta come prima validazione:
    - lingua**: Correzione del codice della lingua (ad es. `fr`, `en`, ecc.).
    - data_ultimo_contributo**: Data di oggi.
    - urgenza** : Lasciare in bianco.
    - contributors_id** : Il vostro ID GitHub.
    - ricompensa** : Lasciare vuoto.

Per maggiori dettagli sull'ID insegnante, consultare il tutorial corrispondente:

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

### 5 - Scrivere il contenuto


- Completate le proprietà del file Markdown con :
    - Il titolo (`nome`).
    - Una breve descrizione (`description`).
- Aggiungete l'immagine di copertina all'inizio del tutorial usando la sintassi Markdown (sostituite "verde" con il nome dello strumento mostrato):

```
![cover-green](assets/cover.webp)
```


- Scrivere il contenuto del tutorial in Markdown :
    - Utilizzate titoli (`##`), elenchi e paragrafi ben strutturati.
    - Inserire immagini utilizzando la sintassi Markdown :

```
![nom-image](assets/en/001.webp)
```


- Inserire i diagrammi e le immagini nella sottocartella della lingua corrispondente, in `/assets`.

### 6 - Salvare e inviare il tutorial


- Salvare le modifiche localmente creando un commit con un messaggio descrittivo.
- Spingere le modifiche al proprio fork GitHub.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Una volta terminato, creare una richiesta di pull (PR) su GitHub per proporre l'integrazione delle modifiche.
- Aggiungete un titolo e una breve descrizione alla PR. Indicare il numero del problema corrispondente nel commento.

### 7 - Correzione di bozze e fusione


- Attendere la convalida o il feedback di un amministratore.
- Se necessario, apportate le correzioni e inviate nuovi commit.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Una volta che il PR è stato unito, si può cancellare il ramo di lavoro.

## Standard di creazione dei contenuti


- Formattazione supportata dalla piattaforma** :
    - Markdown classico: elenchi, link, immagini, citazioni, grassetto, corsivo, ecc.
    - LaTeX (solo blocco, non in linea): delimitato da `$$`.
    - Codice in linea: Sintassi con un singolo backtick.
    - Blocchi di codice: Sintassi con tre trattini, ad esempio :

```
print("Hello, Bitcoin!")
```


- Illustrazioni e diagrammi** :
    - Tutte le immagini devono essere in formato WebP. Se necessario, utilizzare questo strumento gratuito per convertirle: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nominare le immagini con 2 o 3 cifre (ad esempio, `001.webp`, `002.webp`).
    - Per le esercitazioni sui portafogli mobili o hardware, utilizzate dei mock-up.
    - Utilizzate solo immagini create da voi o libere da diritti d'autore.
    - Assicuratevi che siano pertinenti e di alta qualità.
- Carta grafica** :
    - Font: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Piano colori ₿ Rete :
        - Arancione: `#FF5C00`
        - Nero: `#000000`
        - Bianco: `#FFFFFF`

Se hai difficoltà tecniche a inviare il tuo tutorial, non esitare a chiedere aiuto su [il nostro gruppo Telegram dedicato ai contributi](https://t.me/PlanBNetwork_ContentBuilder). Grazie mille!