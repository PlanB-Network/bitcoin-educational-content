---
name: Come scrivere tutorial usando GitHub Desktop (intermedio)
description: Guida completa per proporre un tutorial su Plan ₿ Academy utilizzando GitHub Desktop
---
![cover](assets/cover.webp)

Prima di seguire questo tutorial sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passi preliminari. Se non l'hai ancora fatto, ti invito a consultare prima quest'altro tutorial introduttivo e poi a tornare qui:

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

A questo punto, hai già:

- Scelto il tema del tutorial;
- Contattato il team di Plan ₿ Academy tramite [il gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Scelto gli strumenti con i quali fornire il tuo contributo.

In questa guida vedrai come aggiungere il tuo tutorial su Plan ₿ Netwrok configurando il tuo ambiente locale con GitHub Desktop. Se sei già esperto di GitHub, questo tutorial molto dettagliato potrebbe non essere necessario per te. Ti consiglio piuttosto di consultare quest'altro tutorial in cui presento solo le linee guida principali, senza una descrizione dettagliata passo-passo:

- **Utenti esperti**:

https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Se preferisci non configurare il tuo ambiente di lavoro in locale, segui quest'altro tutorial pensato per i principianti, in cui apportiamo le modifiche direttamente tramite l'interfaccia web di GitHub:

- **Principianti (interfaccia web)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Prerequisiti

Software necessari per seguire questo tutorial:


- [GitHub Desktop](https://desktop.github.com/);
- Un editor di file markdown come [Obsidian](https://obsidian.md/);
- Un editor di codice ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Prerequisiti prima di iniziare il tutorial:


- Avere un [account GitHub](https://github.com/signup);
- Aver forkato il [repository di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content);
- Avere [un profilo da professore su Plan ₿ Academy](https://planb.academy/professors) (solo se si propone un tutorial completo).

Se hai bisogno di aiuto per ottenere i prerequisiti sopra elencati, questo tutorial ti aiuterà:

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

Una volta che tutto è a posto e il tuo ambiente di lavoro è correttamente configurato con il fork di Plan ₿ Academy, puoi iniziare ad aggiungere il tutorial.


## 1 - Creare un nuovo branch

Apri il browser e vai alla pagina del tuo fork del repository Plan ₿ Academy. Questo è il fork che hai creato su GitHub. L'URL del tuo fork dovrebbe essere simile a: `https://github.com/[nomeutente]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Assicurati di essere nel branch principale `dev`, quindi clicca sul pulsante `Sync fork`. Se il tuo fork non è aggiornato, GitHub ti proporrà di aggiornare il tuo branch. Procedi con l'aggiornamento. Se, al contrario, il tuo branch è già aggiornato, GitHub ti informerà:

![TUTO](assets/fr/04.webp)

Apri GitHub Desktop e assicurati che il tuo fork sia selezionato correttamente nell'angolo superiore sinistro della schermata:

![TUTO](assets/fr/05.webp)

Clicca sul pulsante "Fetch origin". Se il repository locale è già aggiornato, GitHub Desktop non suggerirà alcuna azione aggiuntiva. In caso contrario, apparirà l'opzione `Pull origin`. Clicca su questo pulsante per aggiornare il repository locale:

![TUTO](assets/fr/06.webp)

Verifica che ti trovi effettivamente nel branch principale `dev`:

![TUTO](assets/fr/07.webp)

Clicca su questo branch, quindi sul pulsante "New branch":

![TUTO](assets/fr/08.webp)

Assicurati che il nuovo branch sia basato sul repository sorgente, cioè `Plan ₿ Academy/bitcoin-educational-content`.

Nomina il tuo branch usando un titolo esplicativo, ricorrendo ai trattini per separare ogni parola. Per esempio, diciamo che il nostro obiettivo è scrivere un tutorial sull'uso di Sparrow. In questo caso, il branch di lavoro dedicato alla scrittura di questo tutorial potrebbe essere chiamato: `tuto-sparrow-wallet-loic`. Una volta inserito un titolo appropriato, clicca su `Create branch` per confermare la creazione del branch:

![TUTO](assets/fr/09.webp)

Ora clicca sul pulsante `Publish branch` per salvare il nuovo branch nel tuo fork online su GitHub:

![TUTORIAL](assets/fr/10.webp)

Ora, su GitHub Desktop si dovrebbe trovare nel nuovo branch. Ciò significa che tutte le modifiche apportate localmente sul computer saranno salvate esclusivamente su questo branch specifico. Inoltre, finché questo branch rimane selezionato su GitHub Desktop, i file visibili localmente sul computer corrisponderanno a quelli di questo branch (`tuto-sparrow-wallet-loic`) e non a quelli del branch principale (`dev`).

![TUTORIAL](assets/fr/11.webp)

Per ogni nuovo articolo che desideri pubblicare, è necessario creare un nuovo branch da `dev`. Un branch in GitHub è una versione parallela del progetto, che consente di apportare modifiche senza influenzare il branch principale, finché il lavoro non è pronto per essere unito.

## 2 - Aggiungere i file del tutorial

Ora che il branch di lavoro è stato creato, è il momento di integrare il nuovo tutorial. Hai due opzioni: usare il mio script Python, che automatizza la creazione dei documenti necessari, oppure creare manualmente ogni file. Vediamo i passi da seguire per ciascuna opzione.

### Con il mio script Python

È necessario installare Python sul proprio computer:

- Python 3.8 o una versione superiore.

Per utilizzare lo script, naviga nella cartella in cui è memorizzato. Lo script si trova nel repository dei dati di Plan ₿ Academy al percorso: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Una volta nella cartella, installa le dipendenze:

```
pip install -r requirements.txt
```

Avvia quindi il software con il comando:

```
python3 main.py
```

Si aprirà un'interfaccia grafica [(GUI)](https://planb.academy/resources/glossary/gui). La prima volta sarà necessario inserire tutte le informazioni necessarie, ma negli utilizzi successivi lo script ricorderà le informazioni personali, per cui non sarà necessario inserirle di nuovo.

![DATA-CREATOR-PY](assets/fr/37.webp)

Inizia inserendo il percorso locale della cartella `/tutorials` nel tuo repository clonato (`.../bitcoin-educational-content/tutorials/`). Puoi inserirlo manualmente o cliccare sul pulsante "Sfoglia" per navigare con il tuo file explorer.

![DATA-CREATOR-PY](assets/fr/38.webp)

Seleziona la lingua in cui scrivere il tutorial.

![DATA-CREATOR-PY](assets/fr/39.webp)

Nel campo "ID GitHub del collaboratore", inserisci il tuo nome utente GitHub.

![DATA-CREATOR-PY](assets/fr/40.webp)

Successivamente, è necessario compilare il tuo profilo professore. Ci sono diverse opzioni disponibili:

- Inserisci le prime lettere del tuo nome nel campo "Professor Name". Il tuo nome apparirà nell'elenco a discesa "Prof. Suggestions" situato sotto. Selezionalo cliccandoci su;
- In alternativa, puoi cliccare direttamente sul menù a discesa "Prof. Suggestions" e scegliere il tuo nome di professore.

Questa azione inserirà automaticamente il tuo UUID di professore nel campo corrispondente.

![DATA-CREATOR-PY](assets/fr/41.webp)

Se non hai ancora un profilo da professore, consulta questa guida:

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Clicca quindi sul pulsante "New tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Scegli una categoria principale per il tutorial. Quindi, seleziona una sottocategoria pertinente in base alla categoria principale scelta.

![DATA-CREATOR-PY](assets/fr/43.webp)

Imposta un livello di difficoltà del tutorial.

![DATA-CREATOR-PY](assets/fr/44.webp)

Scegli un nome per la cartella creata appositamente per il tutorial. Il nome di questa cartella deve riflettere il software trattato nel tutorial, usando i trattini per separare le parole. Ad esempio, la cartella potrebbe chiamarsi `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

Il `project_id` è l'UUID dell'azienda o dell'organizzazione che sta dietro allo strumento trattato nel tutorial, disponibile [nell'elenco dei progetti](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ad esempio, per un tutorial su Sparrow, è possibile trovare il suo `project_id` nel file: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Questa informazione viene aggiunta al file YAML del tutorial perché Plan ₿ Academy mantiene un database di aziende e organizzazioni attive in ambito Bitcoin o in progetti correlati. Aggiungendo il `project_id` associato, si collega il contenuto all'entità pertinente.

**Aggiornamento:** Nella nuova versione dello script, non è più necessario inserire manualmente il `project_id`. È stata aggiunta una funzione di ricerca per trovare il progetto in base al nome e recuperare automaticamente il corrispondente `project_id`. Digita l'inizio del nome del progetto nel campo "Project Name" per cercarlo, quindi selezionare la società dal menu a discesa. Il `project_id` verrà inserito automaticamente nel campo sottostante. Se necessario, è possibile digitarlo manualmente.

![DATA-CREATOR-PY](assets/fr/46.webp)

Per i tag, selezionare 2 o 3 parole chiave pertinenti al contenuto del tutorial, scegliendole esclusivamente dall'[elenco dei tag Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Il software offre anche una funzione di ricerca per parole chiave con un menù a tendina.

![DATA-CREATOR-PY](assets/fr/47.webp)

Una volta inserite e verificate tutte le informazioni, clicca su "Create tutorial" per confermare la creazione dei file del tutorial. La cartella del tutorial e tutti i file necessari della categoria selezionata verranno generati localmente.

![DATA-CREATOR-PY](assets/fr/48.webp)

A questo punto, si può saltare la sezione "Without my Python script" e il passo 3, "Fill in the YAML file", poiché lo script ha già completato queste azioni per te. Passa direttamente al punto 4 e inizia a scrivere il tuo tutorial.

Per ulteriori informazioni su questo script Python, puoi consultare il relativo file [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Senza il mio script Python

Apri il file manager e naviga nella cartella `bitcoin-educational-content`, che rappresenta il clone locale del repository. In genere si trova sotto `Documents\GitHub\bitcoin-educational-content`.

All'interno di questa cartella, è necessario individuare la sottocartella appropriata per inserire il tutorial. L'organizzazione delle cartelle riflette le diverse sezioni del sito web di Plan ₿ Academy. Nel nostro esempio, poiché vogliamo aggiungere un tutorial su Sparrow, dovremo navigare verso seguente percorso: `bitcoin-educational-content\tutorials\wallet`, che corrisponde alla sezione `WALLET` del sito web:

![TUTO](assets/fr/12.webp)

All'interno della cartella `wallet`, è necessario creare una nuova cartella specificamente dedicata al tutorial. Il nome di questa cartella dovrebbe contenere il software trattato nel tutorial, assicurandosi di collegare le parole con dei trattini. Nel mio esempio, la cartella sarà intitolata `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

In questa nuova sottocartella dedicata al tutorial, è necessario aggiungere diversi elementi:

- Creare una cartella `assets`, destinata a ricevere tutte le illustrazioni necessarie per il tutorial;
- All'interno di questa cartella `assets`, è necessario creare una sottocartella denominata in base al codice della lingua originale del tutorial. Ad esempio, se il tutorial è scritto in inglese, questa sottocartella deve essere denominata `en`. Inserisci lì tutte le immagini del tutorial (diagrammi, immagini, screenshot, ecc.).
- È necessario creare un file `tutorial.yml` per registrare i dettagli relativi al tutorial;
- È necessario creare un file in formato markdown per scrivere il contenuto effettivo del tutorial. Questo file deve essere intitolato usando il codice della lingua in cui è scritto. Ad esempio, per un tutorial scritto in francese, il file deve essere chiamato `fr.md`.

![TUTO](assets/fr/14.webp)

In sintesi, ecco la gerarchia dei file da creare:

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (da modificare con la categoria corretta)
└── sparrow-wallet/ (da modificare con la il nome del tutorial)
├── assets/
│   ├── en/ (da modificare con il codice della lingua di riferimento)
├── tutorial.yml
└── en.md (da modificare con il codice della lingua di riferimento)
```

## 3 - Compilare il file YAML

Compila il file `tutorial.yml` copiando il seguente modello:

```
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

professor_id:

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributor_names:
      - 
    reward:
```

Ecco i campi obbligatori:

- **id**: Un UUID (_Identificatore Unico Universale_) che identifica univocamente il tutorial. Puoi generarlo con [uno strumento online](https://www.uuidgenerator.net/version4). L'unico requisito è che questo UUID sia casuale per evitare conflitti con altri UUID presenti sulla piattaforma;

- **project_id**: L'UUID dell'azienda o organizzazione dietro lo strumento presentato nel tutorial [dall'elenco dei progetti](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ad esempio, se stai creando un tutorial su Blockstream App, puoi trovare il `project_id` nel seguente file: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Queste informazioni vengono aggiunte al file YAML del tuo tutorial perché Plan ₿ Academy mantiene un database di tutte le aziende e organizzazioni che operano su Bitcoin o progetti correlati. Aggiungendo il `project_id` dell'entità associata al tuo tutorial, crei un collegamento tra i due elementi;

- **tags**: 2 o 3 parole chiave relative al contenuto del tutorial, scelte esclusivamente [dall'elenco dei tag di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: La sottocategoria corrispondente al contenuto del tutorial, in base alla struttura del sito Plan ₿ Academy (ad esempio per i wallet: `desktop`, `hardware`, `mobile`, `backup`);

- **level**: Il livello di difficoltà del tutorial, selezionabile tra:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id**: Il tuo `professor_id` (UUID) come mostrato nel [tuo profilo professore](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language**: La lingua originale del tutorial (ad esempio `fr`, `en`, ecc.);

- **proofreading**: Informazioni sul proofreading. Compila la prima parte, poiché la revisione del tuo stesso tutorial conta come prima convalida:
    - **language**: Codice lingua della revisione (ad esempio `fr`, `en`, ecc.).
    - **last_contribution_date**: Data di oggi.
    - **urgency**: 1
    - **contributor_names**: Il tuo ID GitHub.
    - **reward**: 0

Per maggiori dettagli sull'ID insegnante, consulta il tutorial corrispondente:

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency: 1
    contributor_names:
      - LoicPandul
    reward: 0
```

Una volta terminata la modifica del file `tutorial.yml`, salva il documento cliccando su `File > Save`:

![TUTO](assets/fr/16.webp)

Ora è possibile chiudere l'editor di codice.

## 4 - Compilare il file Markdown

A questo punto, puoi aprire il file che contiene il tuo tutorial, che viene denominato con il codice della propria lingua. Ad esempio `fr.md`. Vai su Obsidian, sul lato sinistro della finestra, scorri l'albero delle cartelle fino a trovare la cartella del tuo tutorial e il file che stai cercando:

![TUTO](assets/fr/18.webp)

Clicca sul file per aprirlo:

![TUTO](assets/fr/19.webp)

Inizia compilando la sezione `Properties` all'inizio del documento.

![TUTO](assets/fr/20.webp)

Aggiungi manualmente e compila il seguente blocco di codice:

```
---
name: [Titolo]
description: [Descrizione]
---
```

![TUTO](assets/fr/21.webp)

Inserisci il nome del tuo tutorial e una breve descrizione:

![TUTO](assets/fr/22.webp)

Aggiungi quindi il percorso dell'immagine di copertina all'inizio del tutorial, come di seguito:

```
![cover-sparrow](assets/cover.webp)
```

Questa sintassi è utile quando è necessario aggiungere un'immagine al tutorial. Il punto esclamativo indica che si tratta di un'immagine, con il testo alternativo (alt) specificato tra le parentesi quadre. Il percorso dell'immagine è indicato tra le parentesi tonde:

![TUTO](assets/fr/23.webp)

## 5 - Aggiungere il logo e la copertina

Nella cartella `assets` si deve aggiungere un file chiamato `logo.webp`, che servirà come miniatura per l'articolo. Questa immagine deve essere in formato `.webp` e deve rispettare una dimensione quadrata per armonizzarsi con l'interfaccia utente. È possibile scegliere il logo del software trattato nel tutorial o qualsiasi altra immagine pertinente, a condizione che sia libera da diritti. Inoltre, aggiungi anche un'immagine intitolata `cover.webp` nello stesso posto. Questa immagine verrà visualizzata nella parte superiore del tutorial. Assicurati che questa immagine, come il logo, rispetti i diritti d'uso e sia adatta al contesto del tutorial.

## 6 - Scrittura del tutorial e aggiunta di immagini

Continua a scrivere il contenuto del tuo tutorial. Quando desideri integrare un sottotitolo, applica la formattazione markdown appropriata anteponendo al testo il prefisso `##`:

![TUTO](assets/fr/24.webp)

La sottocartella relativa alla lingua nella cartella `assets` è utilizzata per memorizzare i diagrammi e le immagini che accompagneranno il tutorial. Per quanto possibile, evita di inserire testo nelle immagini in modo che queste siano accessibili ad un pubblico internazionale. Naturalmente il software presentato conterrà del testo, ma se aggiungi immagini rappresentanti le schermate del software, fallo senza testo o, se risulta indispensabile, usa l'inglese.

![TUTO](assets/fr/25.webp)

Per nominare le immagini, è sufficiente utilizzare i numeri corrispondenti all'ordine di apparizione nel tutorial, formattati con due cifre (o tre cifre se il tutorial contiene più di 99 immagini). Ad esempio, nomina la prima immagine `01.webp`, la seconda `02.webp` e così via.

Le immagini devono essere esclusivamente in formato `.webp`. Se necessario, puoi utilizzare [il mio software di conversione delle immagini](https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Per inserire un'immagine nel documento, utilizza il seguente comando Markdown, assicurandoti di specificare il testo alternativo appropriato e il percorso corretto dell'immagine:

```
![sparrow](assets/fr/01.webp)
```

Il punto esclamativo all'inizio indica che si tratta di un'immagine. Il testo alternativo, che aiuta l'accessibilità e la SEO, è posto tra le parentesi quadre. Infine, il percorso dell'immagine è indicato tra le parentesi tonde.

Se desideri creare delle immagini personalizzate, assicurati che abbiano lo stesso formato grafico di Plan ₿ Academy per garantire una coerenza visiva:


- Font**: Utilizza [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Colori**:
 - Arancione: #FF5C00
 - Nero: #000000
 - Bianco: #FFFFFF

**È indispensabile che tutte le immagini integrate nei tutorial siano libere da diritti o rispettino la licenza del file sorgente**. Inoltre, tutte le immagini pubblicate su Plan ₿ Academy sono rese disponibili con licenza CC-BY-SA, così come avviene per i testi.

**-> Suggerimento:** Quando si condividono file pubblicamente, come le immagini, è importante rimuovere i metadati non necessari. Questi possono contenere informazioni sensibili, come dati sulla posizione, date di creazione o dettagli sull'autore. Per proteggere la privacy, è consigliabile eliminare questi metadati. Per semplificare questo processo, è possibile utilizzare strumenti specializzati come [Exif Cleaner](https://exifcleaner.com/), che consente di pulire i metadati di un documento con un semplice drag-and-drop.

## 7 - Salvare e inviare il tutorial

Una volta terminata la stesura del tutorial nella lingua desiderata, il passo successivo consiste nell'inviare una **Pull request**. L'admin si occuperà di aggiungere le traduzioni mancanti del tuo tutorial, grazie al nostro metodo di traduzione automatica con revisione umana.

Per procedere con la pull request, apri il software GitHub Desktop. Il software dovrebbe rilevare automaticamente le modifiche apportate localmente al branch rispetto al repository originale. Prima di continuare, verifica attentamente sul lato sinistro dell'interfaccia che le modifiche corrispondano a quanto previsto:

![TUTO](assets/fr/28.webp)

Aggiungi un titolo per il tuo commit, quindi clicca sul pulsante blu `Commit to [your branch]` per convalidare le modifiche:

![TUTO](assets/fr/29.webp)

Un commit è un salvataggio delle modifiche apportate al branch, accompagnato da un messaggio descrittivo, che permette di seguire l'evoluzione di un progetto nel tempo. È una sorta di checkpoint intermedio.

Quindi clicca sul pulsante `Push origin`. Questo invierà il commit al proprio fork:

![TUTO](assets/fr/30.webp)

Se non hai terminato il tutorial, puoi tornare più tardi e fare nuovi commit. Se hai completato le modifiche per questo branch, clicca ora sul pulsante `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Puoi controllare un'ultima volta che le modifiche siano corrette, quindi clicca sul pulsante `Create pull request`:

![TUTO](assets/fr/32.webp)

Una pull request è una richiesta di integrazione delle modifiche dal tuo branch al branch principale del repository di Plan ₿ Academy: la PR consente la revisione e la discussione delle modifiche prima che vengano "mergiate".

Verrai automaticamente reindirizzato nel tuo browser su GitHub alla pagina di preparazione della tua pull request:

![TUTO](assets/fr/33.webp)

Indica un titolo che riassuma brevemente le modifiche che desideri unire al repository sorgente. Aggiungi un breve commento che descriva queste modifiche (se alla creazione del tutorial è associato un numero della issue, ricordati di annotare nel commento `Closes #{numero di issue}`), quindi clicca sul pulsante verde `Create pull request` per confermare la richiesta di "merge":

![TUTO](assets/fr/34.webp)

La tua PR sarà quindi visibile nella scheda "Pull Request" del repository principale di Plan ₿ Academy. Non devi far altro che attendere che un amministratore ti contatti per confermare l'inclusione del tuo contributo al branch principale, o per richiedere ulteriori modifiche.

![TUTO](assets/fr/35.webp)

Dopo che la PR è stata inclusa nel branch principale, ti consiglio di cancellare il branch di lavoro (`tuto-sparrow-wallet`) per mantenere pulito il tuo fork. GitHub offre automaticamente questa opzione nella pagina della PR:

![TUTO](assets/fr/36.webp)

Sul software GitHub Desktop, è possibile tornare al branch principale del tuo fork (`dev`).

![TUTO](assets/fr/07.webp)

Se desideri apportare modifiche al tuo tutorial dopo aver già presentato la PR, la procedura dipende dallo stato attuale della PR:


- Se la PR è ancora aperta e non è ancora stata inclusa, apporta le modifiche localmente rimanendo sullo stesso branch. Una volta finalizzate le modifiche, usa il pulsante `Push origin` per aggiungere un nuovo commit alla PR ancora aperta;
- Se la tua PR è già stata unita al branch principale, devi ricominciare il processo creando un nuovo branch e inviando una nuova PR. Assicurati che il repository locale sia sincronizzato con il repository di Plan ₿ Academy prima di procedere.

Se incontri difficoltà tecniche nell'inviare il tuo tutorial, non esitare a chiedere aiuto sul [nostro gruppo Telegram dedicato a coloro che sostengono il progetto Plan ₿ Academy](https://t.me/PlanBNetwork_ContentBuilder). Grazie!

