---
name: Contribution - Tutorials
description: Come proporre un nuovo tutorial su PlanB Network?
---
![cover](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin, nel maggior numero di lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, il che offre l'opportunità a chiunque di partecipare all'arricchimento della piattaforma. I contributi possono assumere varie forme: correzione e revisione dei testi esistenti, traduzione in altre lingue, aggiornamento delle informazioni o creazione di nuovi tutorial non ancora disponibili sul nostro sito.

In questo tutorial, spiegherò come modificare la sezione "Tutorials" del PlanB Network. Se desideri aggiungere un nuovo tutorial o migliorarne uno esistente, questo articolo fa per te! Esamineremo in dettaglio come contribuire al PlanB Network tramite GitHub, utilizzando Obsidian, uno strumento di scrittura.

## Prerequisiti

Per contribuire al PlanB Network, hai 3 opzioni a seconda del tuo livello di esperienza con GitHub:
1. **Utenti esperti**: Prosegui con i tuoi metodi abituali e consulta questo tutorial per familiarizzare con la struttura del repository di PlanB, i requisiti specifici e il flusso di lavoro.
2. **Principianti pronti ad imparare**: Ti consiglio di configurare il tuo ambiente di lavoro. Segui questo tutorial così come gli altri nostri articoli elencati di seguito per guidarti passo dopo passo.
3. **Principianti per contributi minori**: Per compiti che richiedono meno modifiche, come la correzione di bozze o correzioni, usa direttamente l'interfaccia web di GitHub senza configurare un ambiente locale completo.

**Software necessario per seguire il mio tutorial:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Un editor di codice ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Prerequisiti prima di iniziare il tutorial:**
- Avere un [account GitHub](https://github.com/signup).
- Avere un fork del [repository sorgente di PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content).
- Avere [un profilo professore su PlanB Network](https://planb.network/professors) (solo se stai proponendo un tutorial completo).

**Se hai bisogno di aiuto per ottenere questi prerequisiti, i miei altri tutorial ti guideranno:**
**[Comprendere Git e GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Creare un account GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Configurare il tuo ambiente di lavoro](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Creare un profilo professore](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Che tipo di contenuto scrivere su PlanB Network?
Siamo principalmente alla ricerca di tutorial su strumenti relativi a Bitcoin o al suo ecosistema. Questi contenuti possono essere organizzati attorno a sei categorie principali:
- Wallet;
- Nodo;
- Mining;
- Commerciante;
- Exchange;
- Privacy.
![tutorial](assets/2.webp)
Oltre a questi argomenti specificamente legati a Bitcoin, PlanB è alla ricerca anche di contributi su temi che evidenziano la sovranità individuale, come:
- Strumenti open source;
- Informatica;
- Crittografia;
- Energia;
- Matematica;
- Economia;
- Fai da te;
- LifeHacking...
Ad esempio, attualmente disponiamo di tutorial su Tails, Nostr o GrapheneOS. Questi strumenti non sono direttamente collegati a Bitcoin, ma sono sistemi che possono interessarci in un processo di sovranità nel mondo digitale. Questi contenuti possono essere integrati in una sottocategoria della sezione "Altri".
Hai la possibilità di progettare un tutorial da zero o di prendere un tutorial precedentemente pubblicato sul tuo sito web (a condizione che tu ne detenga i diritti d'autore) per condividerlo anche su PlanB Network, aggiungendo un link all'articolo originale.

Qualunque sia la tua scelta, tieni presente che tutto il contenuto pubblicato su PlanB Network è sotto la licenza libera [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Questa licenza permette a chiunque di copiare e, potenzialmente, di modificare il tuo contenuto, a condizione che la fonte originale sia debitamente accreditata.

## Come proporre un tutorial su PlanB Network?

Una volta che tutto è a posto, e il tuo ambiente locale è ben configurato con il tuo fork di PlanB Network, puoi iniziare ad aggiungere il tutorial.

### Crea un nuovo ramo

- Apri il tuo browser e vai alla pagina del tuo fork del repository PlanB. Questo è il fork che hai stabilito su GitHub. L'URL del tuo fork dovrebbe apparire così: `https://github.com/[il-tuo-username]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Assicurati di essere sul ramo principale `dev` poi clicca sul pulsante `Sync fork`. Se il tuo fork non è aggiornato, GitHub offrirà di aggiornare il tuo ramo. Procedi con questo aggiornamento. Se, al contrario, il tuo ramo è già aggiornato, GitHub ti informerà:
![tutorial](assets/4.webp)
- Apri il software GitHub Desktop e assicurati che il tuo fork sia correttamente selezionato nell'angolo in alto a sinistra della finestra:
![tutorial](assets/5.webp)
- Clicca sul pulsante `Fetch origin`. Se il tuo repository locale è già aggiornato, GitHub Desktop non suggerirà ulteriori azioni. Altrimenti, apparirà l'opzione `Pull origin`. Clicca su questo pulsante per aggiornare il tuo repository locale: ![tutorial](assets/6.webp)
- Assicurati di essere sul ramo principale `dev`:
![tutorial](assets/7.webp)
- Clicca su questo ramo, poi clicca sul pulsante `New Branch`:
![tutorial](assets/8.webp)
- Assicurati che il nuovo ramo sia basato sul repository sorgente, ovvero `PlanB-Network/bitcoin-educational-content`.
- Nominare il tuo ramo in modo che il titolo sia chiaro riguardo al suo scopo, utilizzando trattini per separare ogni parola. Ad esempio, diciamo che il nostro obiettivo è scrivere un tutorial sull'uso del software Sparrow Wallet. In questo caso, il ramo di lavoro dedicato alla scrittura di questo tutorial potrebbe essere nominato: `tuto-sparrow-wallet-loic`. Una volta inserito il nome appropriato, clicca su `Create branch` per confermare la creazione del ramo:
![tutorial](assets/9.webp)
- Ora clicca sul pulsante `Publish branch` per salvare il tuo nuovo ramo di lavoro sul tuo fork online su GitHub:
![tutorial](assets/10.webp)
Ora, su GitHub Desktop, dovresti essere sul tuo nuovo ramo. Questo significa che tutte le modifiche effettuate localmente sul tuo computer verranno registrate esclusivamente su questo ramo specifico. Inoltre, finché questo ramo rimane selezionato su GitHub Desktop, i file localmente visibili sulla tua macchina corrispondono a quelli di questo ramo (`tuto-sparrow-wallet-loic`), e non a quelli del ramo principale (`dev`).
![tutorial](assets/11.webp)
Per ogni nuovo articolo che desideri pubblicare, dovrai creare un nuovo ramo da `dev`. Un ramo in Git è una versione parallela del progetto, che ti permette di apportare modifiche senza influenzare il ramo principale, fino a quando il lavoro non è pronto per essere unito.
### Aggiungere il tutorial

Ora che il ramo di lavoro è stato creato, è il momento di integrare il tuo nuovo tutorial.
- Apri il tuo gestore di file e naviga fino alla cartella `bitcoin-educational-content`, che rappresenta il clone locale del tuo repository. Normalmente dovresti trovarla sotto `Documents\GitHub\bitcoin-educational-content`. All'interno di questa directory, sarà necessario individuare la sottocartella appropriata per posizionare il tuo tutorial. L'organizzazione delle cartelle riflette le diverse sezioni del sito web PlanB Network. Nel nostro esempio, poiché desideriamo aggiungere un tutorial su Sparrow Wallet, è appropriato andare al seguente percorso: `bitcoin-educational-content\tutorials\wallet` che corrisponde alla sezione `WALLET` sul sito web: ![tutorial](assets/12.webp)
- All'interno della cartella `wallet`, devi creare una nuova directory specificamente dedicata al tuo tutorial. Il nome di questa cartella deve evocare il software trattato nel tutorial, assicurandosi di collegare le parole con trattini. Per il mio esempio, la cartella sarà intitolata `sparrow-wallet`:
![tutorial](assets/13.webp)
- In questa nuova sottocartella dedicata al tuo tutorial, devono essere aggiunti diversi elementi:
	- Crea una cartella `assets`, destinata a ricevere tutte le illustrazioni necessarie per il tuo tutorial;
    - All'interno di questa cartella `assets`, devi creare 8 sottocartelle denominate `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` e `pt`, al fine di classificare le immagini secondo le lingue corrispondenti. Devi anche aggiungere una sottocartella `notext` per le immagini che non necessitano di traduzione, come gli screenshot ad esempio;
	- Deve essere creato un file `tutorial.yml` per registrare i dettagli relativi al tuo tutorial;
	- Deve essere creato un file in formato markdown per scrivere il contenuto effettivo del tuo tutorial. Questo file deve essere intitolato secondo il codice della lingua della scrittura. Ad esempio, per un tutorial scritto in francese, il file dovrebbe essere chiamato `fr.md`.
![tutorial](assets/14.webp)
- Per riassumere, ecco la gerarchia dei file da creare:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (da modificare con la categoria giusta)
        └── sparrow-wallet/ (da modificare con il nome del tutorial)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (da modificare secondo il codice lingua appropriato)
```

- Per iniziare, apri il tuo file `tutorial.yml` utilizzando il tuo editor di codice.
- Compila ogni campo con le informazioni specificate di seguito:
- **builder**: Inserisci il nome dell'azienda che produce il software per cui stai creando un tutorial;
- **tags**: Determina una serie di parole chiave strettamente correlate all'argomento del tuo articolo, per facilitarne la ricerca e l'indicizzazione;
- **categoria**: Seleziona una sottocategoria appropriata tra quelle disponibili sul sito PlanB, in base al contenuto del tuo tutorial. Ad esempio, per un tutorial nella sezione `WALLET`, le opzioni disponibili sono `Desktop`, `Hardware` e `Mobile`;
- **livello**: Indica il livello di difficoltà del tuo tutorial scegliendo una delle seguenti quattro categorie:
    - Principiante (`beginner`),
    - Intermedio (`intermediary`),
    - Avanzato (`advanced`),
    - Esperto (`expert`).
- **professore**: Fornisci il tuo ID contributore come appare sul tuo profilo professore. Per maggiori dettagli, fai riferimento a [il tutorial corrispondente](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (opzionale): Nel caso in cui desideri attribuire il merito a un sito web sorgente per il tutorial che stai sviluppando, come il tuo sito personale, qui puoi aggiungere il link in questione.
![tutorial](assets/15.webp)
- Una volta terminata la modifica del tuo file `tutorial.yml`, salva il documento cliccando su `File > Salva`:
![tutorial](assets/16.webp)
- Ora puoi chiudere il tuo editor di codice.
- Nella cartella `assets`, devi aggiungere un file denominato `logo.webp`, che servirà come miniatura per il tuo articolo. Questa immagine deve essere in formato `.webp` e deve rispettare una dimensione quadrata per armonizzarsi con l'interfaccia utente. Hai la libertà di scegliere il logo del software trattato nel tutorial o qualsiasi altra immagine pertinente, purché sia priva di diritti. Inoltre, aggiungi anche un'immagine intitolata `cover.webp` nella stessa posizione. Questa immagine verrà visualizzata in cima al tuo tutorial. Assicurati che questa immagine, come il logo, rispetti i diritti di utilizzo e sia adatta al contesto del tuo tutorial:
![tutorial](assets/17.webp)
- Ora, puoi aprire il tuo file che ospiterà il tuo tutorial, denominato con il codice della tua lingua, come `fr.md`. Vai su Obsidian, sul lato sinistro della finestra, scorri l'albero delle cartelle fino alla cartella del tuo tutorial e al file cercato:
![tutorial](assets/18.webp)
- Clicca sul file per aprirlo:
![tutorial](assets/19.webp)
- Inizieremo compilando la sezione `Properties` in cima al documento. Se questa sezione manca dal tuo file (se il documento è completamente vuoto), puoi riprodurla copiandola da un altro tutorial esistente: ![tutorial](assets/20.webp)
- Puoi anche aggiungerla manualmente in questo modo usando il tuo editor di codice:
```markdown
---
name: [Titolo]
description: [Descrizione]
---
```
![tutorial](assets/21.webp)
- Compila il nome del tuo tutorial e una breve descrizione dello stesso:
![tutorial](assets/22.webp)
- Poi aggiungi la tua immagine di copertina all'inizio del tuo tutorial. Per fare ciò, digita:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Questa sintassi sarà utile ogni volta che sarà necessario aggiungere un'immagine al tuo tutorial. Il punto esclamativo indica che si tratta di un'immagine, con il testo alternativo (alt) specificato tra le parentesi quadre. Il percorso dell'immagine è indicato tra le parentesi:
![tutorial](assets/23.webp)
- Continua a scrivere il tuo tutorial scrivendo il tuo contenuto. Quando vuoi integrare un sottotitolo, applica la formattazione markdown appropriata prefissando il testo con `##`:
![tutorial](assets/24.webp)

### Come aggiungere diagrammi al tutorial?
Le sottocartelle linguistiche nella cartella `assets` sono destinate a organizzare i diagrammi e le immagini che accompagneranno il tuo tutorial. Se le tue immagini includono testo, assicurati di tradurle per ogni lingua interessata per rendere il tuo contenuto accessibile a un pubblico internazionale. Per i diagrammi senza testo da tradurre o screenshot, posizionali direttamente nella sottocartella `notext`. ![tutorial](assets/25.webp)
Per nominare le tue immagini, inserisci semplicemente i numeri nell'ordine di apparizione nel tutorial. Ad esempio, nomina la tua prima immagine `1.webp`, la seconda `2.webp`, e così via.

Se lo stesso diagramma viene tradotto in più lingue, mantieni lo stesso nome del file per le diverse traduzioni nelle sottocartelle linguistiche, come `en/1.webp`, `fr/1.webp`, `pt/1.webp`, ecc.

Hai la possibilità di utilizzare diversi formati di immagine come `jpeg`, `png` o `webp`. Si raccomanda di optare per il formato `webp` affinché le immagini siano meno pesanti. ![tutorial](assets/26.webp)
Per inserire un diagramma nel tuo documento, usa il seguente comando in Markdown, assicurandoti di specificare il testo alternativo appropriato e il percorso corretto dell'immagine:
```markdown
![sparrow](assets/notext/1.webp)
```
Il punto esclamativo all'inizio indica che si tratta di un'immagine. Il testo alternativo, che aiuta nell'accessibilità e nel SEO, è posizionato tra le parentesi quadre. Infine, il percorso dell'immagine è indicato tra le parentesi: ![tutorial](assets/27.webp)
Se desideri creare i tuoi diagrammi, assicurati di aderire alla carta grafica di PlanB Network per garantire la consistenza visiva:
- **Carattere**: Usa [Rubik](https://fonts.google.com/specimen/Rubik);
- **Colori**:
	- Arancione: #FF5C00
	- Nero: #000000
	- Bianco: #FFFFFF

**È imperativo che tutti i visual integrati nei tuoi tutorial siano liberi da diritti o rispettino la licenza del file sorgente**. Inoltre, tutti i diagrammi pubblicati su PlanB Network sono resi disponibili sotto la licenza CC-BY-SA, allo stesso modo del testo.

**-> Suggerimento:** Quando si condividono file pubblicamente, come le immagini, è importante rimuovere qualsiasi metadato superfluo. Questo può contenere informazioni sensibili, come dati sulla posizione, date di creazione o dettagli sull'autore. Per proteggere la tua privacy, è consigliabile rimuovere questi metadati. Per semplificare questa operazione, puoi utilizzare strumenti specializzati come [Exif Cleaner](https://exifcleaner.com/), che offre la possibilità di pulire i metadati di un documento con un semplice trascinamento.

### Come salvare e inviare il tutorial?

Una volta terminato di scrivere il tuo tutorial nella lingua prescelta, il passo successivo è inviare una **Pull Request**. L'amministratore aggiungerà quindi le traduzioni mancanti del tuo tutorial, grazie al nostro metodo di traduzione automatizzato.

- Per procedere con la Pull Request, apri il software GitHub Desktop.
- Il software dovrebbe rilevare automaticamente le modifiche che hai apportato localmente rispetto al repository originale. Prima di continuare, verifica attentamente sul lato sinistro dell'interfaccia che queste modifiche corrispondano esattamente a ciò che ti aspettavi: ![tutorial](assets/28.webp)
- Aggiungi un titolo per il tuo commit, poi clicca sul pulsante blu `Commit to [your branch]` per convalidare queste modifiche: ![tutorial](assets/29.webp)
Un commit è un salvataggio delle modifiche apportate al ramo, accompagnato da un messaggio descrittivo, che consente di seguire l'evoluzione di un progetto nel tempo. È quindi una sorta di punto di controllo intermedio.
- Quindi clicca sul pulsante `Push origin`. Questo invierà il tuo commit al tuo fork: ![tutorial](assets/30.webp) - Se non hai terminato il tuo tutorial, puoi tornarci più tardi e fare nuovi commit.
- Se hai terminato le tue modifiche per questo ramo, ora clicca sul pulsante `Preview Pull Request`: ![tutorial](assets/31.webp)
- Puoi controllare un'ultima volta che le tue modifiche siano corrette, poi clicca sul pulsante `Create Pull Request`:
![tutorial](assets/32.webp)
Una Pull Request è una richiesta fatta per integrare i cambiamenti dal tuo ramo al ramo principale del repository di PlanB Network, che permette la revisione e la discussione dei cambiamenti prima della loro fusione.

- Sarai automaticamente reindirizzato nel tuo browser a GitHub sulla pagina di preparazione della tua Pull Request:
![tutorial](assets/33.webp)
- Fornisci un titolo che riassuma brevemente le modifiche che desideri unire al repository sorgente.
- Aggiungi un breve commento che descriva queste modifiche.
- Clicca sul pulsante verde `Create Pull Request` per confermare la richiesta di fusione:
![tutorial](assets/34.webp)
La tua PR sarà poi visibile nella scheda `Pull Request` del repository principale di PlanB Network. Tutto ciò che devi fare ora è aspettare fino a quando un amministratore ti contatterà per confermare la fusione del tuo contributo o per richiedere eventuali modifiche aggiuntive.
![tutorial](assets/35.webp)
Dopo la fusione della tua PR con il ramo principale, si raccomanda di eliminare il tuo ramo di lavoro (`tuto-sparrow-wallet`) per mantenere una cronologia pulita sul tuo fork. GitHub ti offrirà automaticamente questa opzione sulla pagina della tua PR:
![tutorial](assets/36.webp)
Sul software GitHub Desktop, puoi tornare al ramo principale del tuo fork (`dev`).
![tutorial](assets/7.webp)
Se desideri apportare modifiche al tuo contributo dopo aver già inviato la tua PR, la procedura da seguire dipende dallo stato attuale della tua PR:
- Se la tua PR è ancora aperta e non è ancora stata fusa, esegui le modifiche localmente rimanendo sullo stesso ramo. Una volta finalizzate le modifiche, usa il pulsante `Push origin` per aggiungere un nuovo commit alla tua PR ancora aperta;
- Nel caso in cui la tua PR sia già stata fusa con il ramo principale, dovrai rifare il processo dall'inizio creando un nuovo ramo, poi inviando una nuova PR. Assicurati che il tuo repository locale sia sincronizzato con il repository sorgente di PlanB Network prima di procedere.
