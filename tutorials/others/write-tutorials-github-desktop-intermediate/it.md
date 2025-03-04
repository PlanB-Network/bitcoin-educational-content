---
name: Contributo - Esercitazione con GitHub Desktop (intermedio)
description: Guida completa per proporre un tutorial su Plan ₿ Network utilizzando GitHub Desktop
---
![cover](assets/cover.webp)

Prima di seguire questo tutorial sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passi preliminari. Se non l'avete ancora fatto, vi invito a consultare prima questo tutorial introduttivo e poi a tornare qui:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
L'avete già fatto:


- Scegliere il tema del tutorial;
- Contattare il team di Plan ₿ Network tramite [il gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Scegliere gli strumenti di contribuzione.

In questa guida vedremo come aggiungere il vostro tutorial alla rete di Plan ₿ impostando il vostro ambiente locale con GitHub Desktop. Se siete già esperti di Git, questo tutorial molto dettagliato potrebbe non essere necessario per voi. Vi consiglio piuttosto di consultare quest'altro tutorial in cui presento solo le linee guida principali, senza una guida dettagliata passo-passo:


- Utenti esperti**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Se preferite non configurare il vostro ambiente locale, seguite quest'altra guida pensata per i principianti, in cui apportiamo le modifiche direttamente tramite l'interfaccia web di GitHub:


- Principianti (interfaccia web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Prerequisiti

Software necessario per seguire questa esercitazione:


- [GitHub Desktop](https://desktop.github.com/);
- Un editor di file markdown come [Obsidian](https://obsidian.md/);
- Un editor di codice ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Prerequisiti prima di iniziare l'esercitazione:


- Avere un [account GitHub](https://github.com/signup);
- Avere un fork del [repository dei sorgenti di Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content);
- Avere [un profilo di professore su Plan ₿ Network](https://planb.network/professors) (solo se si propone un tutorial completo).

Se avete bisogno di aiuto per ottenere questi prerequisiti, le mie altre esercitazioni vi aiuteranno:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Una volta che tutto è a posto e l'ambiente locale è correttamente configurato con il proprio fork della rete Plan ₿, si può iniziare ad aggiungere il tutorial.

## 1 - Creare un nuovo ramo

Aprire il browser e andare alla pagina del proprio fork del repository Plan ₿ Network. Questo è il fork che avete creato su GitHub. L'URL del vostro fork dovrebbe essere simile a: `https://github.com/[nomeutente]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Assicurarsi di essere nel ramo principale `dev`, quindi fare clic sul pulsante `Sync fork`. Se il vostro fork non è aggiornato, GitHub vi proporrà di aggiornare il vostro ramo. Procedere con l'aggiornamento. Se, al contrario, il vostro ramo è già aggiornato, GitHub vi informerà:

![TUTO](assets/fr/04.webp)

Aprite il software GitHub Desktop e assicuratevi che il vostro fork sia selezionato correttamente nell'angolo superiore sinistro della finestra:

![TUTO](assets/fr/05.webp)

Fare clic sul pulsante "Recupera origine". Se il repository locale è già aggiornato, GitHub Desktop non suggerirà alcuna azione aggiuntiva. In caso contrario, apparirà l'opzione `Pull origin`. Fare clic su questo pulsante per aggiornare il repository locale:

![TUTO](assets/fr/06.webp)

Verificare che ci si trovi effettivamente nel ramo principale `dev`:

![TUTO](assets/fr/07.webp)

Fare clic su questo ramo, quindi fare clic sul pulsante "Nuovo ramo":

![TUTO](assets/fr/08.webp)

Assicurarsi che il nuovo ramo sia basato sul repository sorgente, cioè `PlanB-Network/bitcoin-educational-content`.

Nominate il vostro ramo in modo che il titolo sia chiaro sul suo scopo, usando i trattini per separare ogni parola. Per esempio, supponiamo che il nostro obiettivo sia scrivere un tutorial sull'uso del software Sparrow Wallet. In questo caso, il ramo di lavoro dedicato alla scrittura di questo tutorial potrebbe essere chiamato: `tuto-sparrow-wallet-loic`. Una volta inserito il nome appropriato, fare clic su `Crea ramo` per confermare la creazione del ramo:

![TUTO](assets/fr/09.webp)

Ora fate clic sul pulsante `Publish branch` per salvare il nuovo ramo di lavoro nel vostro fork online su GitHub:

![TUTORIAL](assets/fr/10.webp)

Ora, su GitHub Desktop, ci si dovrebbe trovare nel nuovo ramo. Ciò significa che tutte le modifiche apportate localmente sul computer saranno salvate esclusivamente su questo ramo specifico. Inoltre, finché questo ramo rimane selezionato su GitHub Desktop, i file visibili localmente sul computer corrispondono a quelli di questo ramo (`tuto-sparrow-wallet-loic`) e non a quelli del ramo principale (`dev`).

![TUTORIAL](assets/fr/11.webp)

Per ogni nuovo articolo che si desidera pubblicare, è necessario creare un nuovo ramo da `dev`. Un ramo in Git è una versione parallela del progetto, che consente di apportare modifiche senza influenzare il ramo principale, finché il lavoro non è pronto per essere unito.

## 2 - Aggiungere i file del tutorial

Ora che il ramo di lavoro è stato creato, è il momento di integrare il nuovo tutorial. Avete due opzioni: usare il mio script Python, che automatizza la creazione dei documenti necessari, oppure creare manualmente ogni file. Vediamo i passi da seguire per ciascuna opzione.

### Con il mio script Python

È necessario installarlo sul proprio computer:


- Python 3.8 o superiore;
- Le dipendenze necessarie per lo script. Eseguire:

```bash
pip install customtkinter appdirs
```

Per utilizzare lo script, accedere alla cartella in cui è memorizzato. Lo script si trova nel repository dei dati della rete Plan ₿ nel percorso: `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.

Una volta nella cartella, eseguite il comando:

```bash
python new-tutorial-creation.py
```

Si aprirà un'interfaccia grafica (GUI). La prima volta è necessario inserire tutte le informazioni necessarie, ma durante i successivi utilizzi dello script, le informazioni personali verranno ricordate, evitando così di doverle inserire nuovamente.

![TUTORIAL](assets/fr/37.webp)

Iniziate indicando il percorso locale che porta alla cartella `/tutorials` sul vostro clone del repository (`.../bitcoin-educational-content/tutorials/`). È possibile annotarlo manualmente o fare clic sul pulsante "Sfoglia" per navigare attraverso il proprio file explorer.

![TUTORIAL](assets/fr/38.webp)

Selezionare la lingua in cui scrivere il tutorial.

![TUTORIAL](assets/fr/39.webp)

Scegliete una categoria principale per il vostro tutorial.

![TUTORIAL](assets/fr/40.webp)

Quindi, selezionare una sottocategoria appropriata, in base alla categoria principale scelta.

![TUTORIAL](assets/fr/41.webp)

Determinare un livello di difficoltà per l'esercitazione.

![TUTORIAL](assets/fr/42.webp)

Scegliere il nome della cartella creata appositamente per l'esercitazione. Il nome di questa cartella deve riflettere il software trattato nell'esercitazione, usando i trattini per collegare le parole. Ad esempio, la cartella potrebbe chiamarsi `red-wallet`:

![TUTO](assets/fr/43.webp)

Il `project_id` è l'UUID dell'azienda o dell'organizzazione che sta dietro allo strumento presentato nel tutorial, disponibile [nell'elenco dei progetti](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ad esempio, per un tutorial sul software Sparrow Wallet, si può trovare questo `project_id` nel file: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Questa informazione viene aggiunta al file YAML del vostro tutorial perché Plan ₿ Network mantiene un database di aziende e organizzazioni attive in Bitcoin o in progetti correlati. Aggiungendo il `project_id` associato alla propria esercitazione, si crea un collegamento tra il proprio contenuto e l'entità interessata.

***Nella nuova versione dello script, non è più necessario inserire manualmente il `project_id`. È stata aggiunta una funzione di ricerca per trovare il progetto in base al suo nome e recuperare automaticamente il corrispondente `project_id`. Digitare l'inizio del nome del progetto nella casella "Nome progetto" per cercarlo, quindi selezionare la società desiderata dal menu a discesa. Il `project_id` verrà automaticamente inserito nella casella sottostante. Se necessario, è possibile annotarlo manualmente.

![TUTO](assets/fr/44.webp)

Per i tag, selezionare 2 o 3 parole chiave pertinenti al contenuto del tutorial, scegliendole esclusivamente [dall'elenco dei tag del Piano ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).

![TUTO](assets/fr/45.webp)

Nella casella "ID GitHub del collaboratore", inserire il proprio ID GitHub.

![TUTO](assets/fr/46.webp)

Per il riquadro "ID professore PBN", inserire il proprio ID utilizzando le parole dell'elenco BIP39, così come appare sul [profilo del professore](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![TUTO](assets/fr/47.webp)

Per maggiori dettagli sull'ID professore, consultare il seguente tutorial:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Una volta inserite e verificate tutte le informazioni, fare clic su "Crea tutorial" per convalidare la creazione dei file del tutorial. Questo genererà localmente la cartella del tutorial e tutti i file necessari nella cartella della categoria selezionata.

![TUTO](assets/fr/48.webp)

A questo punto si può saltare la sottosezione "Senza il mio script Python" e il passo 3 "Compilazione del file YAML", perché lo script ha già eseguito queste azioni automaticamente per voi. Passate direttamente al passo 4 e iniziate a scrivere il vostro tutorial.

Per ulteriori informazioni su questo script Python, si può anche [consultare il suo README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Senza il mio script Python

Aprire il file manager e navigare nella cartella `bitcoin-educational-content`, che rappresenta il clone locale del repository. Di solito si trova sotto `Documents\GitHub\bitcoin-educational-content`.

All'interno di questa cartella, sarà necessario individuare la sottocartella appropriata per inserire il proprio tutorial. L'organizzazione delle cartelle riflette le diverse sezioni del sito web di Plan ₿ Network. Nel nostro esempio, poiché vogliamo aggiungere un tutorial su Sparrow Wallet, è opportuno andare nel seguente percorso: `bitcoin-educational-content\tutorials\wallet` che corrisponde alla sezione `WALLET` del sito web:

![TUTO](assets/fr/12.webp)

All'interno della cartella `wallet`, è necessario creare una nuova cartella specificamente dedicata all'esercitazione. Il nome di questa cartella dovrebbe evocare il software trattato nel tutorial, assicurandosi di collegare le parole con dei trattini. Nel mio esempio, la cartella sarà intitolata `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

In questa nuova sottocartella dedicata al tutorial, è necessario aggiungere diversi elementi:


- Creare una cartella `assets`, destinata a ricevere tutte le illustrazioni necessarie per l'esercitazione;
- All'interno di questa cartella `assets`, è necessario creare una sottocartella denominata in base al codice della lingua originale del tutorial. Ad esempio, se il tutorial è scritto in inglese, questa sottocartella deve essere denominata `en`. Inserire lì tutte le immagini del tutorial (diagrammi, immagini, screenshot, ecc.).
- È necessario creare un file `tutorial.yml` per registrare i dettagli relativi all'esercitazione;
- È necessario creare un file in formato markdown per scrivere il contenuto effettivo del tutorial. Questo file deve essere intitolato secondo il codice della lingua in cui è scritto. Ad esempio, per un tutorial scritto in francese, il file deve essere chiamato `fr.md`.

![TUTO](assets/fr/14.webp)

In sintesi, ecco la gerarchia dei file da creare:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Compilare il file YAML

Compilare il file `tutorial.yml` copiando il seguente modello:

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

Ecco i dettagli dei campi obbligatori:


- **id**: Un UUID (_Universally Unique Identifier_) per identificare in modo univoco il tutorial. È possibile generarlo con [uno strumento online](https://www.uuidgenerator.net/version4). L'unico requisito è che questo UUID sia casuale per evitare conflitti con un altro UUID della piattaforma;
- **project_id**: L'UUID dell'azienda o dell'organizzazione che sta dietro allo strumento presentato nel tutorial [dall'elenco dei progetti] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ad esempio, se si sta creando un tutorial sul software Sparrow Wallet, si può trovare questo `project_id` nel seguente file: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Questa informazione viene aggiunta al file YAML del vostro tutorial perché Plan ₿ Network mantiene un database di tutte le aziende e organizzazioni che operano su Bitcoin o su progetti correlati. Aggiungendo il `project_id` dell'entità correlata al tutorial, si crea un collegamento tra i due elementi;
- **tasg**: 2 o 3 parole chiave pertinenti al contenuto del tutorial, scelte esclusivamente [dall'elenco dei tag di Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: La sottocategoria corrispondente al contenuto del tutorial, secondo la struttura del sito Plan ₿ Network (ad esempio per i portafogli: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: Il livello di difficoltà dell'esercitazione, tra:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Il tuo `contributor_id` (parole BIP39) come visualizzato nel [tuo profilo di professore](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: La lingua originale del tutorial (ad esempio `fr`, `en`, ecc.);
- **proofreading**: Informazioni sul processo di correzione delle bozze. Compilare la prima parte, poiché la correzione del proprio tutorial conta come prima validazione:
    - **language**: Codice della lingua della correzione (ad esempio `fr`, `en`, ecc.).
    - **last_contribution_date**: Data di oggi.
    - **urgency**: Lasciare in bianco.
    - **contributors_id**: Il vostro ID GitHub.
    - **reward**: Lasciare vuoto.

Per maggiori dettagli sull'identificativo del professore, consultare il relativo tutorial:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Ecco un esempio di file `tutorial.yml` completato per un tutorial sul portafoglio Blockstream Green:

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
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Titolo]
description: [Descrizione]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```