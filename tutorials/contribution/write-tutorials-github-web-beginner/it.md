---
name: Contributo - Tutorial web GitHub (principiante)
description: Guida completa alla pianificazione ₿ Tutorial di rete con GitHub Web
---
![cover](assets/cover.webp)

Prima di seguire questo tutorial sull'aggiunta di un nuovo tutorial, è necessario aver completato alcuni passaggi preliminari. Se non l'avete ancora fatto, date prima un'occhiata a questo tutorial introduttivo e poi tornate qui:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Avete già :


- Scegliete un tema per il vostro tutorial;
- Contattare il team di Plan ₿ Network tramite [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Scegliete gli strumenti di contribuzione.

In questa guida vedremo come aggiungere il vostro tutorial a Plan ₿ Network utilizzando la versione web di GitHub. Se siete già esperti di Git, questo tutorial molto dettagliato potrebbe non essere necessario per voi. Vi consiglio invece di dare un'occhiata a uno di questi altri due tutorial, in cui sono descritte in dettaglio le linee guida da seguire e i passaggi per apportare modifiche da un file :


- Utenti esperti** :

https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Prerequisiti

Prerequisiti prima di iniziare l'esercitazione :


- Avere un [account GitHub](https://github.com/signup);
- Avere un fork del [repository dei sorgenti di Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content);
- Avere [un profilo docente su Plan ₿ Network](https://planb.network/professors) (solo se si offre un tutorial completo).

Se avete bisogno di aiuto per ottenere questi prerequisiti, le mie altre esercitazioni vi aiuteranno:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Una volta che tutto è a posto e che avete il vostro fork del repository Plan ₿ Network, potete iniziare ad aggiungere il tutorial.

## 1 - Creare un nuovo ramo

Aprire il browser e navigare alla pagina del fork nel repository Plan ₿ Network. Questo è il fork che avete creato su GitHub. L'URL del vostro fork dovrebbe essere simile a questo: `https://github.com/[nomeutente]/bitcoin-educational-content`:

![GITHUB](assets/fr/01.webp)

Assicurarsi di essere nel ramo principale `dev`, quindi fare clic sul pulsante "*Sync fork*". Se il vostro fork non è aggiornato, GitHub vi chiederà di aggiornare il vostro ramo. Procedere con l'aggiornamento:

![GITHUB](assets/fr/02.webp)

Cliccate sul ramo `dev`, quindi date un nome al vostro ramo di lavoro in modo che il titolo rifletta chiaramente il suo scopo, usando i trattini per separare le parole. Per esempio, se il nostro obiettivo è scrivere un tutorial sull'uso del Green Wallet, il ramo potrebbe chiamarsi: `tuto-green-wallet-loic`. Dopo aver inserito un nome adeguato, fare clic su "*Crea ramo*" per confermare la creazione del nuovo ramo basato su `dev`:

![GITHUB](assets/fr/03.webp)

Ora dovreste trovarvi nel vostro nuovo ramo di lavoro:

![GITHUB](assets/fr/04.webp)

Ciò significa che tutte le modifiche apportate saranno salvate solo in quel ramo specifico.

Per ogni nuovo articolo che si intende pubblicare, creare un nuovo ramo da `dev`.

Un ramo in Git rappresenta una versione parallela del progetto, che consente di lavorare sulle modifiche senza influenzare il ramo principale, finché il lavoro non è pronto per essere integrato.

## 2 - Aggiungere i file del tutorial

Ora che il ramo di lavoro è stato creato, è il momento di integrare il nuovo tutorial.

All'interno dei file del vostro ramo, dovrete trovare la sottocartella appropriata per il posizionamento del vostro tutorial. L'organizzazione delle cartelle riflette le diverse sezioni del sito web di Plan ₿ Network. Nel nostro esempio, dato che stiamo aggiungendo un tutorial sul Portafoglio verde, andate nel seguente percorso: `bitcoin-educational-content\tutorials\wallet` che corrisponde alla sezione `WALLET` del sito web:

![GITHUB](assets/fr/05.webp)

Nella cartella `wallet`, creare una nuova cartella specificamente dedicata all'esercitazione. Il nome di questa cartella deve indicare chiaramente il software trattato nell'esercitazione, usando i trattini per collegare le parole. Nel mio esempio, la cartella si chiamerà `green-wallet`. Fare clic su "*Aggiungi file*" e poi su "*Crea nuovo file*":

![GITHUB](assets/fr/06.webp)

Inserire il nome della cartella seguito da una barra `/` per confermare la sua creazione come cartella.

![GITHUB](assets/fr/07.webp)

In questa nuova sottocartella dedicata al tutorial, è necessario aggiungere diversi elementi:


- Creare una cartella `assets` per contenere tutte le illustrazioni necessarie per l'esercitazione;
- All'interno di questa cartella `assets`, creare una sottocartella denominata secondo il codice della lingua originale del tutorial. Ad esempio, se il tutorial è scritto in inglese, questa sottocartella dovrebbe essere denominata `en`. In questa cartella vanno inseriti tutti gli elementi visivi del tutorial (diagrammi, immagini, screenshot, ecc.).
- È necessario creare un file `tutorial.yml` per registrare i dettagli dell'esercitazione;
- È necessario creare un file markdown per scrivere il contenuto effettivo del tutorial. Questo file deve essere chiamato secondo il codice della lingua in cui è scritto. Ad esempio, per un tutorial scritto in francese, il file deve essere chiamato `fr.md`.

Per riassumere, ecco la gerarchia dei file (continueremo a crearli nella prossima sezione):

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```

## 3 - Compilare il file YAML

Cominciamo con il file YAML. Nella casella per la creazione di un nuovo file, inserire `tutorial.yml`:

![GITHUB](assets/fr/08.webp)

Compilare il file `tutorial.yml` copiando il seguente modello:

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

Ecco un esempio di file `tutorial.yml` compilato per un tutorial sul portafoglio Blockstream Green:

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

Una volta terminata la modifica del file `tutorial.yml`, salvare il documento facendo clic sul pulsante "*Commit changes...*":

![GITHUB](assets/fr/09.webp)

Aggiungete un titolo e una descrizione e assicuratevi che il commit sia effettuato nel ramo creato all'inizio di questa guida. Quindi confermare facendo clic su "*Commit changes*".

![GITHUB](assets/fr/10.webp)

## 4 - Creare sottocartelle per le immagini

Cliccate nuovamente su "*Aggiungi file*" e poi su "*Crea nuovo file*" :

![GITHUB](assets/fr/11.webp)

Inserire `assets` seguito da una barra `/` per creare la cartella:

![GITHUB](assets/fr/12.webp)

Ripetere questo passaggio nella cartella `/assets` per creare la sottocartella della lingua, ad esempio `fr` se il tutorial è in francese:

![GITHUB](assets/fr/13.webp)

In questa cartella, creare un file fittizio per forzare GitHub a mantenere la cartella (che altrimenti sarebbe vuota). Nominare questo file `.gitkeep`. Quindi fare clic su "*Commit changes...*".

![GITHUB](assets/fr/14.webp)

Controllate di nuovo di essere nel ramo corretto, quindi fate clic su "*Commit changes*".

![GITHUB](assets/fr/15.webp)

## 5 - Creare il file Markdown

Ora creeremo il file che ospiterà il vostro tutorial, con il nome della vostra lingua, per esempio `fr.md` se scriviamo in francese. Andare alla cartella tutorial :

![GITHUB](assets/fr/16.webp)

Fare clic su "Aggiungi file*", quindi su "Crea nuovo file*".

![GITHUB](assets/fr/17.webp)

Nominare il file usando il codice della propria lingua. Nel mio caso, dato che il tutorial è scritto in francese, ho nominato il mio file `fr.md`. L'estensione `.md` indica che il file è in formato Markdown.

![GITHUB](assets/fr/18.webp)

Si inizia compilando la sezione `Proprietà` all'inizio del documento. Aggiungiamo manualmente e compiliamo il seguente blocco di codice (le chiavi `nome:` e `descrizione:` devono essere mantenute in inglese, ma i loro valori devono essere scritti nella lingua utilizzata per il tutorial):

```
---
name: [Titre]
description: [Description]
---
```

![GITHUB](assets/fr/19.webp)

Inserite il nome del vostro tutorial e una breve descrizione:

![GITHUB](assets/fr/20.webp)

Quindi aggiungere il percorso all'immagine di copertina all'inizio del tutorial. Per fare ciò, notare :

```
![cover-green](assets/cover.webp)
```

Questa sintassi vi sarà utile ogni volta che dovrete aggiungere un'immagine al vostro tutorial. Il punto esclamativo indica un'immagine, il cui testo alternativo (alt) è specificato tra le parentesi quadre. Il percorso dell'immagine è indicato tra le parentesi:

![GITHUB](assets/fr/21.webp)

Fare clic sul pulsante "*Commetti le modifiche...*" per salvare il file.

![GITHUB](assets/fr/22.webp)

Controllare di essere nel ramo giusto, quindi confermare il commit.

![GITHUB](assets/fr/23.webp)

La cartella dei tutorial dovrebbe ora avere questo aspetto, in base al codice della lingua:

![GITHUB](assets/fr/24.webp)

## 6 - Aggiungere il logo e la copertina

Nella cartella `assets` è necessario aggiungere un file chiamato `logo.webp`, che servirà come miniatura dell'articolo. Questa immagine deve essere in formato `.webp` e deve essere di dimensioni quadrate per adattarsi all'interfaccia utente.

È possibile scegliere il logo del software utilizzato nel tutorial o qualsiasi altra immagine pertinente, purché sia libera da diritti d'autore. Inoltre, aggiungere un'immagine intitolata `cover.webp` nello stesso posto. Questa verrà visualizzata nella parte superiore del tutorial. Assicurarsi che questa immagine, come il logo, rispetti i diritti d'uso e sia appropriata al contesto del tutorial.

Per aggiungere immagini alla cartella `/assets`, è possibile trascinarle dai file locali. Assicurarsi di essere nella cartella `/assets` e nel ramo giusto, quindi fare clic su "*Commit changes*".

![GITHUB](assets/fr/26.webp)

A questo punto le immagini dovrebbero apparire nella cartella.

![GITHUB](assets/fr/27.webp)

## 7 - Scrivere il tutorial

Continuare a scrivere il tutorial annotando il contenuto nel file Markdown con il codice della lingua (nel mio esempio, in francese, è il file `fr.md`). Andare al file e fare clic sull'icona della matita:

![GITHUB](assets/fr/28.webp)

Iniziare a scrivere il tutorial. Quando si aggiunge un sottotitolo, utilizzare la formattazione Markdown appropriata, facendo precedere il testo da `##`:

![GITHUB](assets/fr/29.webp)

Alternare le viste "*Modifica*" e "*Anteprima*" per visualizzare meglio il rendering.

![GITHUB](assets/fr/30.webp)

Per salvare il lavoro, fare clic su "*Commit Changes...*", assicurarsi di essere nel ramo giusto, quindi confermare facendo nuovamente clic su "*Commit Changes*".

![GITHUB](assets/fr/31.webp)

## 8 - Aggiungere immagini

La sottocartella della lingua nella cartella `/assets` (nel mio esempio: `/assets/en`) viene utilizzata per memorizzare i diagrammi e le immagini che accompagneranno il tutorial. Per quanto possibile, evitate di includere testo nelle immagini per rendere i contenuti accessibili a un pubblico internazionale. Naturalmente il software presentato conterrà del testo, ma se aggiungete schemi o indicazioni aggiuntive alle schermate del software, fatelo senza testo o, se essenziale, usate l'inglese.

Per nominare le immagini, è sufficiente utilizzare i numeri corrispondenti all'ordine di apparizione nel tutorial, formattati a due cifre (o a tre cifre se il tutorial contiene più di 99 immagini). Ad esempio, nominare la prima immagine `01.webp`, la seconda `02.webp` e così via.

Le immagini devono essere solo in formato `.webp`. Se necessario, è possibile utilizzare [il mio software di conversione delle immagini](https://github.com/LoicPandul/ImagesConverter).

![GITHUB](assets/fr/32.webp)

Ora che le immagini sono state aggiunte alla sottocartella, è possibile eliminare il file fittizio `.gitkeep`. Aprite questo file, fate clic sui tre puntini in alto a destra e poi su "*Elimina file*".

![GITHUB](assets/fr/33.webp)

Salvare le modifiche facendo clic su "*Conferma le modifiche...*".

![GITHUB](assets/fr/34.webp)

Per inserire un diagramma dalla sottocartella nel documento editoriale, utilizzare il seguente comando Markdown, avendo cura di specificare il testo alternativo appropriato e il percorso dell'immagine corretto per la propria lingua:

```
![green](assets/fr/01.webp)
```

Il punto esclamativo all'inizio indica un'immagine. Il testo alternativo, che aiuta l'accessibilità e il riferimento, è posto tra le parentesi quadre. Infine, il percorso dell'immagine è indicato tra le parentesi.

![GITHUB](assets/fr/35.webp)

Se desiderate creare i vostri schemi, assicuratevi di seguire le linee guida grafiche di Plan ₿ Network per garantire la coerenza visiva:


- Font**: Utilizzare [Rubik](https://fonts.google.com/specimen/Rubik);
- Colori** :
 - Arancione: #FF5C00
 - Nero : #000000
 - Bianco: #FFFFFF

**È indispensabile che tutte le immagini integrate nelle esercitazioni siano libere da copyright o rispettino la licenza del file sorgente**. Pertanto, tutti i diagrammi pubblicati su Plan ₿ Network sono resi disponibili con licenza CC-BY-SA, allo stesso modo del testo.

**-> Suggerimento:** Quando si condividono file in pubblico, come le immagini, è importante rimuovere i metadati superflui. Questi possono contenere informazioni sensibili, come dati sulla posizione, date di creazione e dettagli sull'autore. Per proteggere la propria privacy, è bene rimuovere questi metadati. Per semplificare questa operazione, è possibile utilizzare strumenti specializzati come [Exif Cleaner](https://exifcleaner.com/), che consente di ripulire i metadati di un documento con un semplice trascinamento.

## 9 - Proporre il tutorial

Una volta terminata la stesura del tutorial nella lingua desiderata, il passo successivo consiste nell'inviare una **Richiesta di estrazione**. L'amministratore aggiungerà le traduzioni mancanti al vostro tutorial, utilizzando il nostro metodo di traduzione automatica con revisione umana.

Per procedere con la richiesta di pull, dopo aver salvato tutte le modifiche, cliccare sul pulsante "*Contribuisci*", quindi su "*Apri richiesta di pull*" :

![GITHUB](assets/fr/36.webp)

Una richiesta di pull è una richiesta fatta per integrare le modifiche dal proprio ramo nel ramo principale del repository Plan ₿ Network, che consente la revisione e la discussione delle modifiche prima che vengano unite.

Prima di continuare, controllate attentamente nella parte inferiore dell'interfaccia che le modifiche apportate corrispondano a quanto previsto:

![GITHUB](assets/fr/37.webp)

Assicuratevi, all'inizio dell'interfaccia, che il vostro ramo di lavoro sia unito al ramo `dev' del repository Plan ₿ Network (che è il ramo principale).

Inserire un titolo che riassuma brevemente le modifiche che si desidera unire al repository sorgente. Aggiungere un breve commento che descriva queste modifiche (se alla creazione del tutorial è associato un numero di problema, ricordarsi di annotare `Chiude #{numero di problema}` come commento), quindi fare clic sul pulsante verde "*Create pull request*" per confermare la richiesta di unione:

![GITHUB](assets/fr/38.webp)

Il vostro PR sarà quindi visibile nella scheda "*Richiesta di estrazione*" del repository principale di Plan ₿ Network. A questo punto non resta che attendere che un amministratore vi contatti per confermare che il vostro contributo è stato unito o per richiedere ulteriori modifiche.

![GITHUB](assets/fr/39.webp)

Dopo aver unito la PR al ramo principale, si consiglia di cancellare il ramo di lavoro (nel mio esempio: `tuto-green-wallet`) per mantenere una storia pulita del fork. GitHub vi offrirà automaticamente questa opzione nella pagina della vostra PR:

![GITHUB](assets/fr/40.webp)

Se desiderate apportare modifiche al vostro contributo dopo aver già presentato la PR, i passi da seguire dipendono dallo stato attuale della PR:


- Se il PR è ancora aperto e non è ancora stato unito, apportare le modifiche nello stesso workbranch. Le modifiche del commit saranno aggiunte al PR ancora aperto;
- Nel caso in cui il vostro PR sia già stato unito al ramo principale, dovrete rifare il processo dall'inizio creando un nuovo ramo e inviando un nuovo PR. Assicurarsi che il fork sia sincronizzato con il repository dei sorgenti di Plan ₿ Network sul ramo `dev` prima di procedere.

Se hai difficoltà tecniche a inviare il tuo tutorial, non esitare a chiedere aiuto su [il nostro gruppo Telegram dedicato ai contributi](https://t.me/PlanBNetwork_ContentBuilder). Grazie mille!
