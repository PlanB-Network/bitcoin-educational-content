---
name: Contributo - Tutorial web GitHub (principiante)
description: Guida completa ai tutorial Plan ₿ Academy con GitHub Web
---
![cover](assets/cover.webp)

Prima di seguire questa guida sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passaggi preliminari. Se non l'hai ancora fatto, dai prima un'occhiata a questo tutorial introduttivo e poi torna qui:

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

A questo punto, hai già:


- Scelto un tema per il tuo tutorial;
- Contattato il team di Plan ₿ Academy tramite [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o la mail paolo@planb.network;
- Scelto quali strumenti utilizzare.

In questa guida vedremo come aggiungere il tuo tutorial a Plan ₿ Academy utilizzando la versione web di GitHub. Se sei già esperto di Git, questo tutorial molto dettagliato potrebbe non essere necessario per te. Ti consiglio invece di dare un'occhiata a uno di questi altri due tutorial, in cui sono descritte in dettaglio le linee guida da seguire e i passaggi per apportare modifiche da un file:


**- Utenti esperti**:

https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

**- Intermedio (GitHub Desktop)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Prerequisiti

Prerequisiti da avere prima di iniziare il tutorial:


- Avere un [account GitHub](https://github.com/signup);
- Avere un fork del [repository dei sorgenti di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content);
- Avere [un profilo docente su Plan ₿ Academy](https://planb.academy/professors) (solo se vuoi fare un tutorial completo).

Se hai bisogno di aiuto per ottenere i prerequisiti elencati sopra, questi altri tutorial ti aiuteranno:


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.academy/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Una volta che tutto è a posto e che hai il tuo fork del repository Plan ₿ Academy, puoi iniziare ad aggiungere il tutorial.

## 1 - Creare un nuovo branch

Apri il browser e vai alla pagina del tuo fork (del repository Plan ₿ Academy). Questo è il fork che hai creato su GitHub. L'URL del tuo fork dovrebbe essere simile a questo: `https://github.com/[nomeutente]/bitcoin-educational-content`:

![GITHUB](assets/fr/01.webp)

Assicurati di essere nel branch principale `dev`, quindi clicca sul pulsante "*Sync fork*". Se il tuo fork non è aggiornato, GitHub ti chiederà di aggiornare il tuo branch. Procedi con l'aggiornamento:

![GITHUB](assets/fr/02.webp)

Clicca sul branch `dev`, quindi nomina il tuo branch usando un titolo esplicativo, usando i trattini per separare le parole. Per esempio, se il nostro obiettivo è scrivere un tutorial sull'uso di Green, il branch potrebbe chiamarsi: `tuto-green-wallet-loic`. Dopo aver inserito un nome adeguato, clicca su "*Create branch*" per confermare la creazione del nuovo branch basato su `dev`:

![GITHUB](assets/fr/03.webp)

Ora dovresti trovarti nel tuo nuovo branch di lavoro:

![GITHUB](assets/fr/04.webp)

Ciò significa che tutte le modifiche apportate saranno salvate solo in quel branch specifico.

Per ogni nuovo articolo che intendi pubblicare, crea un nuovo branch da `dev`.

Un branch in Git rappresenta una versione parallela del progetto, che consente di lavorare sulle modifiche senza influenzare il branch principale, finché il lavoro non è pronto per essere integrato.

## 2 - Aggiungere i file del tutorial

Ora che il branch di lavoro è stato creato, è il momento di inserire il nuovo tutorial.

All'interno dei file del tuo branch, devi trovare la sottocartella appropriata per caricare il tutorial. L'organizzazione delle cartelle riflette le diverse sezioni del sito web [planb.network](https://planb.academy/). Nel nostro esempio, dato che stiamo aggiungendo un tutorial su Green, segui questo percorso: `bitcoin-educational-content\tutorials\wallet` che corrisponde alla sezione `WALLET` del sito web:

![GITHUB](assets/fr/05.webp)

Nella cartella `wallet`, crea una nuova cartella specificamente dedicata al tutorial. Il nome di questa cartella deve indicare chiaramente il software trattato nel tutorial, usando i trattini per collegare le parole. Nel mio esempio, la cartella si chiamerà `green-wallet`. Clicca su "*Add file*" e poi su "*Create new file*":

![GITHUB](assets/fr/06.webp)

Inserisci il nome della cartella seguito da una barra `/` per confermare la sua creazione come directory.

![GITHUB](assets/fr/07.webp)

In questa nuova sottocartella dedicata al tutorial, è necessario aggiungere diversi elementi:


- Crea una cartella `assets` per contenere tutte le illustrazioni necessarie per il tutorial;
- All'interno di questa cartella `assets`, crea una sottocartella denominata secondo il codice della lingua originale del tutorial. Ad esempio, se il tutorial è scritto in inglese, questa sottocartella dovrebbe essere denominata `en`. In questa cartella vanno inseriti tutti gli elementi visuali del tutorial (diagrammi, immagini, screenshot, ecc.).
- È necessario creare un file `tutorial.yml` per registrare i dettagli del tutorial;
- È necessario creare un file markdown per scrivere il contenuto effettivo del tutorial. Questo file deve essere chiamato secondo il codice della lingua in cui è scritto. Ad esempio, per un tutorial scritto in francese, il file deve essere chiamato `fr.md`.

Per riassumere, ecco la gerarchia dei file (continueremo a crearli nella prossima sezione):

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (a modificare con la categoria corretta)
└── green-wallet/ (a modificare con il nome del tutorial)
├── assets/
│   ├── fr/ (da modificare con il codice della lingua appropriato)
├── tutorial.yml
└── fr.md (da modificare con il codice della lingua appropriato)
```

## 3 - Compilare il file YAML

Cominciamo con il file YAML. Nella casella per la creazione di un nuovo file, inserisci `tutorial.yml`:

![GITHUB](assets/fr/08.webp)

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

- **project_id**: L'UUID dell'azienda o organizzazione che ha creato lo strumento presentato nel tutorial [dall'elenco dei progetti](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ad esempio, se stai creando un tutorial sul software Green, puoi trovare il `project_id` nel seguente file: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Queste informazioni vengono aggiunte al file YAML del tuo tutorial perché Plan ₿ Academy mantiene un database di tutte le aziende e organizzazioni che lavorano su Bitcoin o progetti correlati. Aggiungendo il `project_id` dell'entità associata al tuo tutorial, si crea quindi un collegamento tra i due elementi;

- **tags**: 2 o 3 parole chiave pertinenti al contenuto del tutorial, scelte esclusivamente [dall'elenco dei tag di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: La sottocategoria corrispondente al contenuto del tutorial, in base alla struttura del sito Plan ₿ Academy (ad esempio per i wallet: `desktop`, `hardware`, `mobile`, `backup`);

- **level**: Il livello di difficoltà del tutorial, selezionabile tra:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id**: Il tuo `professor_id` (UUID) come mostrato nel [tuo profilo professore](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language**: La lingua originale del tutorial (ad esempio `fr`, `en`, ecc.);

- **proofreading**: Informazioni sul processo di revisione. Compila la prima parte, poiché la revisione del tuo stesso tutorial conta come prima convalida:
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

Una volta terminata la modifica del file `tutorial.yml`, salva il documento cliccando sul pulsante "*Commit changes...*":

![GITHUB](assets/fr/09.webp)

Aggiungi un titolo e una descrizione, e assicurati che il commit sia effettuato nel branch creato all'inizio di questa guida. Quindi conferma cliccando su "*Commit changes*".

![GITHUB](assets/fr/10.webp)

## 4 - Creare sottocartelle per le immagini

Clicca nuovamente su "*Add file*" e poi su "*Create new file*":

![GITHUB](assets/fr/11.webp)

Inserisci `assets` seguito da una barra `/` per creare la cartella:

![GITHUB](assets/fr/12.webp)

Ripeti questo passaggio nella cartella `/assets` per creare la sottocartella della lingua, ad esempio `fr` se il tutorial è in francese:

![GITHUB](assets/fr/13.webp)

In questa cartella, crea un file fittizio per forzare GitHub a mantenere la directory (che altrimenti sarebbe vuota). Nomina questo file `.gitkeep`. Quindi clicca su "*Commit changes...*".

![GITHUB](assets/fr/14.webp)

Controlla di nuovo di essere nel branch corretto, quindi clicca su "*Commit changes*".

![GITHUB](assets/fr/15.webp)

## 5 - Creare il file Markdown

Ora creeremo il file del tutorial, con il nome della tua lingua, per esempio `fr.md` se scriviamo in francese. Vai alla cartella `tutorial`:

![GITHUB](assets/fr/16.webp)

Clicca su "Add file*", quindi su "Create new file*".

![GITHUB](assets/fr/17.webp)

Nomina il file usando il codice della tua lingua. Nel mio caso, dato che il tutorial è scritto in francese, ho nominato il mio file `fr.md`. L'estensione `.md` indica che il file è in formato Markdown.

![GITHUB](assets/fr/18.webp)

Si inizia compilando la sezione `Proprietà` all'inizio del documento. Aggiungiamo manualmente e compiliamo il seguente blocco di codice (le chiavi `name:` e `description:` devono essere mantenute in inglese, ma ciò che viene scritto dopo i due punti deve essere nella lingua utilizzata per il tutorial):

```
---
name: [Titolo]
description: [Descrizione]
---
```

![GITHUB](assets/fr/19.webp)

Inserisci il nome del tuo tutorial e una breve descrizione:

![GITHUB](assets/fr/20.webp)

Quindi aggiungi il percorso all'immagine di copertina all'inizio del tutorial. Per fare ciò, nota quanto segue:

```
![cover-green](assets/cover.webp)
```

Questa sintassi ti sarà utile ogni volta che dovrai aggiungere un'immagine al tuo tutorial. Il punto esclamativo indica un'immagine, il cui testo alternativo (alt) è specificato tra le parentesi quadre. Il percorso dell'immagine è indicato tra le parentesi tonde:

![GITHUB](assets/fr/21.webp)

Clicca sul pulsante "*Commit changes...*" per salvare il file.

![GITHUB](assets/fr/22.webp)

Controlla di essere nel branch giusto, quindi conferma il commit.

![GITHUB](assets/fr/23.webp)

La cartella dei tutorial dovrebbe ora avere questo aspetto, in base al codice della lingua:

![GITHUB](assets/fr/24.webp)

## 6 - Aggiungere il logo e la copertina

Nella cartella `assets` è necessario aggiungere un file chiamato `logo.webp`, che servirà come miniatura dell'articolo. Questa immagine deve essere in formato `.webp` e deve essere di dimensioni quadrate per adattarsi all'interfaccia utente.

È possibile scegliere il logo del software utilizzato nel tutorial o qualsiasi altra immagine pertinente, purché sia libera da diritti d'autore. Inoltre, aggiungi un'immagine intitolata `cover.webp`, che verrà visualizzata nella parte iniziale del tutorial. Assicurati che questa immagine, come il logo, rispetti i diritti d'uso e sia appropriata al contesto del tutorial.

Per aggiungere immagini alla cartella `/assets`, è possibile trascinarle dai file locali. Assicurati di essere nella cartella `/assets` e nel branch giusto, quindi clicca su "*Commit changes*".

![GITHUB](assets/fr/26.webp)

A questo punto le immagini dovrebbero apparire nella cartella.

![GITHUB](assets/fr/27.webp)

## 7 - Scrivere il tutorial

Continua a scrivere il tutorial annotando il contenuto nel file Markdown con il codice della lingua (nel mio esempio, in francese, è il file `fr.md`). Vai al file e clicca sull'icona della matita:

![GITHUB](assets/fr/28.webp)

Inizia a scrivere il tutorial. Quando si aggiunge un sottotitolo, utilizza la formattazione Markdown appropriata, facendo precedere il testo da `##`:

![GITHUB](assets/fr/29.webp)

Alterna le viste "*Edit*" e "*Preview*" per visualizzare meglio il rendering.

![GITHUB](assets/fr/30.webp)

Per salvare il lavoro, clicca su "*Commit Changes...*", assicurati di essere nel branch giusto, quindi conferma cliccando nuovamente su "*Commit Changes*".

![GITHUB](assets/fr/31.webp)

## 8 - Aggiungere immagini

La sottocartella della lingua nella cartella `/assets` (nel mio esempio: `/assets/en`) viene utilizzata per archiviare i diagrammi e le immagini che accompagneranno il tutorial. Per quanto possibile, evita di includere testo nelle immagini, per rendere i contenuti accessibili a un pubblico internazionale. Naturalmente il software presentato conterrà del testo, ma se aggiungi schemi o indicazioni aggiuntive alle schermate prese dal software, non aggiungere testo o, se essenziale, usa l'inglese.

Per nominare le immagini, è sufficiente utilizzare i numeri corrispondenti all'ordine di apparizione nel tutorial, formattati a due cifre (o a tre cifre se il tutorial contiene più di 99 immagini). Ad esempio, nomina la prima immagine `01.webp`, la seconda `02.webp` e così via.

Le immagini devono essere solo in formato `.webp`. Se necessario, è possibile utilizzare [il mio software di conversione delle immagini](https://github.com/LoicPandul/ImagesConverter).

![GITHUB](assets/fr/32.webp)

Ora che le immagini sono state aggiunte alla sottocartella, è possibile eliminare il file fittizio `.gitkeep`. Apri questo file, clicca sui tre puntini in alto a destra e poi su "*Delete file*".

![GITHUB](assets/fr/33.webp)

Salvare le modifiche cliccando su "*Commit changes...*".

![GITHUB](assets/fr/34.webp)

Per inserire un'immagine dalla sottocartella nel documento editoriale, utilizza il seguente comando Markdown, avendo cura di specificare il testo alternativo appropriato e il percorso dell'immagine corretto per la propria lingua:

```
![green](assets/fr/01.webp)
```

Il punto esclamativo all'inizio indica un'immagine. Il testo alternativo, che aiuta l'accessibilità e il riferimento, è posto tra le parentesi quadre. Infine, il percorso dell'immagine è indicato tra le parentesi tonde.

![GITHUB](assets/fr/35.webp)

Se desideri creare manualmente delle immagini o degli schemi, assicurati di seguire le linee guida grafiche di Plan ₿ Academy per garantire la coerenza visiva:


- **Font**: Utilizzare [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Pantone**:
 - Arancione: #FF5C00
 - Nero: #000000
 - Bianco: #FFFFFF

**È indispensabile che tutte le immagini inserite nei tutorial siano libere da copyright o rispettino la licenza del file sorgente**. Pertanto, tutti i file pubblicati su Plan ₿ Academy sono resi disponibili con licenza CC-BY-SA, così come avviene per il testo.

**-> Suggerimento:** Quando si condividono file in pubblico, come le immagini, è importante rimuovere i metadati superflui. Questi possono contenere informazioni sensibili, come dati sulla posizione, date sulla creazione del file, e dettagli sull'autore. Per proteggere la propria privacy, è bene rimuoverli. Per semplificare questa operazione, è possibile utilizzare strumenti specializzati come [Exif Cleaner](https://exifcleaner.com/), che consente di ripulire i metadati di un documento trascinandoli semplicemente al di fuori dell'immagine.

## 9 - Proporre il tutorial

Una volta terminata la stesura del tutorial nella lingua desiderata, il passo successivo consiste nell'inviare una **Pull Request**. L'amministratore tradurra il file in altre lingue tramite l'utilizzo di AI.

Per procedere con la pull request, dopo aver salvato tutte le modifiche, clicca sul pulsante "*Contribute*", quindi su "*Open pull request*":

![GITHUB](assets/fr/36.webp)

Una pull request è una richiesta fatta per integrare le modifiche dal proprio branch nel branch principale del repository Plan ₿ Academy, che consente la revisione e la discussione delle modifiche prima che vengano unite.

Prima di continuare, controlla attentamente nella parte inferiore dell'interfaccia che le modifiche apportate corrispondano a quanto previsto:

![GITHUB](assets/fr/37.webp)

Assicurati, all'inizio dell'interfaccia, che il tuo branch di lavoro sia unito al branch `dev' del repository Plan ₿ Academy (che è il branch principale).

Inserisci un titolo che riassuma brevemente le modifiche che desideri effettuare al repository sorgente. Aggiungi un breve commento che descriva queste modifiche (se alla creazione del tutorial è associato un numero di issue, ricordati di annotare `Close #{numero di issue}` come commento), quindi clicca sul pulsante verde "*Create pull request*" per confermare la richiesta di ["merge"](https://planb.academy/resources/glossary/merge):

![GITHUB](assets/fr/38.webp)

La tua PR sarà quindi visibile nella scheda "*Pull Request*" del repository principale di Plan ₿ Academy. A questo punto non resta che attendere che un amministratore ti contatti per confermare che il tuo tutorial sia stato unito al repository principale, o per richiedere ulteriori modifiche.

![GITHUB](assets/fr/39.webp)

Dopo aver inserito la PR al branch principale, si consiglia di cancellare il branch di lavoro (nel mio esempio: `tuto-green-wallet`) per mantenere il fork più ordinato e pulito. GitHub ti consiglierà automaticamente questa opzione nella pagina della tua PR:

![GITHUB](assets/fr/40.webp)

Se desideri apportare modifiche ai tuoi file dopo aver già inviato la Pull Request, i passi da seguire dipendono dallo stato attuale della stessa PR:


- Se la PR è ancora aperta e non è ancora stato fatto il "merge", puoi apportare le modifiche nello stesso branch dove hai lavorato. Le modifiche del commit saranno aggiunte alla PR ancora aperta;
- Nel caso in cui la tua PR sia già stata unita al branch principale, devi rifare il processo dall'inizio, creando un nuovo branch e inviando una nuova PR. Assicurati che il fork sia sincronizzato con il repository sorgente di Plan ₿ Academy sul branch `dev` prima di procedere.

Se hai difficoltà tecniche a inviare il tuo tutorial, non esitare a chiedere aiuto sul [nostro gruppo Telegram dedicato ai contributors](https://t.me/PlanBNetwork_ContentBuilder). Grazie mille!