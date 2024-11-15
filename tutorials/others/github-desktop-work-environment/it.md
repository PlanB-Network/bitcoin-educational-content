---
name: GitHub Desktop
description: Come configurare il tuo ambiente di lavoro locale?
---
![github](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, il che consente a chiunque di partecipare all'arricchimento della piattaforma. I contributi possono assumere varie forme: correzione e revisione dei testi esistenti, traduzione in altre lingue, aggiornamento delle informazioni o creazione di nuovi tutorial non ancora disponibili sul nostro sito.

Se desideri contribuire alla Rete PlanB, dovrai utilizzare GitHub per proporre modifiche. Per fare ciò, hai due opzioni:
- **Contribuire direttamente tramite l'interfaccia web di GitHub**: Questo è il metodo più semplice. Se sei un principiante o se prevedi di fare solo pochi contributi minori, questa opzione è probabilmente la migliore per te;
- **Contribuire localmente utilizzando Git**: Questo metodo è più adatto se prevedi di fare contributi regolari o significativi alla Rete PlanB. Anche se configurare il tuo ambiente Git locale sul computer può sembrare complesso all'inizio, questo approccio è più efficiente nel lungo termine. Consente una gestione più flessibile delle modifiche. Se sei nuovo in questo, non preoccuparti, **spieghiamo l'intero processo di configurazione del tuo ambiente in questo tutorial** (promesso, non dovrai digitare alcuna riga di comando ^^).

Se non hai idea di cosa sia GitHub, o se vuoi saperne di più sui termini tecnici relativi a Git e GitHub, ti consiglio di leggere il nostro articolo introduttivo per familiarizzare con questi concetti.

https://planb.network/tutorials/others/basics-of-github



- Per iniziare, avrai ovviamente bisogno di un account GitHub. Se ne hai già uno, puoi accedere, altrimenti, puoi usare il nostro tutorial per crearne uno nuovo.

https://planb.network/tutorials/others/create-github-account



## Passo 1: Installa GitHub Desktop

- Vai su https://desktop.github.com/ per scaricare il software GitHub Desktop. Questo software ti consente di interagire facilmente con GitHub, senza dover usare un terminale:
![github-desktop](assets/1.webp)
- Quando avvii il software per la prima volta, ti verrà chiesto di collegare il tuo account GitHub. Per fare ciò, clicca su `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- Una pagina di autenticazione si aprirà nel tuo browser. Inserisci il tuo indirizzo email e la password scelti durante la creazione del tuo account, poi clicca sul pulsante `Sign in`:
![github-desktop](assets/3.webp)
- Clicca su `Authorize desktop` per confermare la connessione tra il tuo account e il software:
![github-desktop](assets/4.webp)
- Sarai automaticamente reindirizzato al software GitHub Desktop. Clicca su `Finish`: ![github-desktop](assets/5.webp)
- Se hai appena creato il tuo account GitHub, verrai reindirizzato a una pagina che indica che non hai ancora creato alcun repository. A questo punto, metti da parte il software GitHub Desktop; ci torneremo più tardi: ![github-desktop](assets/6.webp)

## Passo 2: Installa Obsidian

Passiamo ora all'installazione del software di scrittura. Qui, hai diverse opzioni. Avrai bisogno di un software che supporti la modifica dei file Markdown, poiché la Rete PlanB utilizza questo formato per i file di testo nel suo repository.
Esistono molteplici software specializzati nella modifica di file Markdown, come Typora, progettato specificamente per la scrittura. Anche se non è l'ideale, è possibile anche scegliere un editor di codice, come Visual Studio Code (VSC) o Sublime Text. Tuttavia, come scrittore, preferisco utilizzare il software Obsidian. Vediamo insieme come installarlo e iniziare a usarlo.
- Vai su https://obsidian.md/download e scarica il software: ![github-desktop](assets/7.webp)
- Installa Obsidian, avvia il software, scegli la tua lingua e poi clicca su `Quick Start`: ![github-desktop](assets/8.webp)
- Arriverai al software Obsidian. Per ora, non hai nessun file aperto: ![github-desktop](assets/9.webp)

## Passo 3: Fork del repository della rete PlanB

- Vai al repository dei dati della rete PlanB al seguente indirizzo: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Da questa pagina, clicca sul pulsante `Fork` in alto a destra della finestra: ![github-desktop](assets/11.webp)
- Nel menu di creazione, puoi lasciare le impostazioni predefinite. Assicurati che la casella `Copy the dev branch only` sia selezionata, poi clicca sul pulsante `Create fork`: ![github-desktop](assets/12.webp)
- Arriverai quindi al tuo fork del repository della rete PlanB: ![github-desktop](assets/13.webp)
Questo fork costituisce un repository separato dall'originale, anche se attualmente contiene gli stessi dati. Ora lavorerai su questo nuovo repository.

Abbiamo, in un certo senso, fatto una copia del repository sorgente della rete PlanB. Il tuo fork (la copia) e il repository originale ora evolveranno indipendentemente l'uno dall'altro. Sul repository originale, altri contributori possono aggiungere nuovi dati, mentre tu, sul tuo fork, procederai con le tue modifiche.
Per mantenere la consistenza tra questi due repository, sarà necessario sincronizzarli periodicamente affinché recuperino le stesse informazioni. Per inviare le tue modifiche al repository sorgente, utilizzerai quello che si chiama una **Pull Request**. E per integrare le modifiche dal repository sorgente nel tuo fork, utilizzerai il comando **Sync fork** disponibile sull'interfaccia web di GitHub.
![github-desktop](assets/14.webp)

## Passo 4: Clona il fork

- Ritorna al software GitHub Desktop. Ormai, il tuo fork dovrebbe apparire nella sezione `Your repositories`. Se non lo vedi immediatamente, usa il pulsante a doppia freccia per aggiornare l'elenco. Quando il tuo fork appare, cliccaci sopra per selezionarlo:
![github-desktop](assets/15.webp)
- Poi clicca sul pulsante blu: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Mantieni il percorso predefinito. Per confermare, clicca sul pulsante blu `Clone`:
![github-desktop](assets/17.webp)
- Attendi mentre GitHub Desktop clona localmente il tuo fork:
![github-desktop](assets/18.webp)
- Dopo aver clonato il repository, il software ti offre due opzioni. Devi selezionare la prima: `To contribute to the parent project`. Questa scelta ti permetterà di presentare il tuo futuro lavoro come un contributo al progetto principale (`PlanB-Network/bitcoin-educational-content`), e non esclusivamente come una modifica del tuo fork personale (`[username]/bitcoin-educational-content`). Una volta scelta l'opzione, clicca su `Continue`:
![github-desktop](assets/19.webp)
- Il tuo GitHub Desktop è ora correttamente configurato. Ora, puoi lasciare il software aperto in background per seguire le modifiche che apporteremo.
![github-desktop](assets/20.webp)
Quello che abbiamo raggiunto in questa fase è la creazione di una copia locale del tuo repository, che è ospitato su GitHub. Come promemoria, questo repository è un fork del repository sorgente di PlanB Network. Sarai in grado di apportare modifiche a questa copia locale, come aggiungere tutorial, traduzioni o correzioni. Una volta effettuate queste modifiche, utilizzerai il comando **Push origin** per inviare le tue modifiche locali al tuo fork ospitato su GitHub.

Puoi anche recuperare le modifiche dal fork, ad esempio, durante una sincronizzazione con il repository di PlanB Network. Per questo, utilizzerai il comando **Fetch origin** per scaricare le modifiche sulla tua copia locale (il tuo clone), e poi il comando **Pull origin** per unirle al tuo lavoro. Questo ti permette di rimanere aggiornato sugli ultimi sviluppi del progetto contribuendo in modo efficace.

![github-desktop](assets/21.webp)
## Passo 5: Crea un nuovo caveau in Obsidian

- Apri il software Obsidian e clicca sull'icona del piccolo caveau in basso a sinistra della finestra:
![github-desktop](assets/22.webp)
- Clicca sul pulsante `Open` per aprire una cartella esistente come caveau: ![github-desktop](assets/23.webp)
- Si aprirà il tuo esplora file. Devi localizzare e selezionare la cartella intitolata `GitHub`, che dovrebbe trovarsi nella tua directory `Documenti` tra i tuoi file. Questo percorso corrisponde a quello stabilito durante il passo 4. Dopo aver scelto la cartella, conferma la sua selezione. La creazione del tuo caveau su Obsidian verrà quindi avviata su una nuova pagina del software:

![github-desktop](assets/24.webp)
-> **Attenzione**, è importante non scegliere la cartella `bitcoin-educational-content` quando si crea un nuovo caveau in Obsidian. Invece, seleziona la cartella principale, `GitHub`. Se selezioni la cartella `bitcoin-educational-content`, la cartella di configurazione `.obsidian`, contenente le tue impostazioni locali di Obsidian, verrà automaticamente integrata nel repository. Vogliamo evitare questo, poiché non è necessario trasferire le tue configurazioni di Obsidian al repository di PlanB Network. Un'alternativa è aggiungere la cartella `.obsidian` al file `.gitignore`, ma questo metodo modificherebbe anche il file `.gitignore` del repository sorgente, il che non è desiderabile.

- Sul lato sinistro della finestra, puoi vedere l'albero dei file con i tuoi diversi repository GitHub che sono stati clonati localmente.
- Cliccando sulle frecce accanto ai nomi delle cartelle, puoi espanderle per accedere alle sottocartelle dei repository e ai loro documenti:
![github-desktop](assets/25.webp)
- Non dimenticare di impostare Obsidian in modalità scura: "La luce attira gli insetti" ;)

## Passo 6: Installa un Editor di Codice
La maggior parte delle tue modifiche riguarderà file in formato Markdown (`.md`). Per modificare questi documenti, puoi utilizzare Obsidian, il software di cui abbiamo parlato in precedenza. Tuttavia, PlanB Network utilizza altri formati di file e dovrai modificarne alcuni.

Ad esempio, quando crei un nuovo tutorial, dovrai creare un file YAML (`.yml`) per inserire i tag del tuo tutorial, il suo titolo e il tuo ID insegnante. Obsidian non offre la possibilità di modificare questo tipo di file, quindi avrai bisogno di un editor di codice.

Per questo, hai diverse opzioni a disposizione. Sebbene il blocco note standard del tuo computer possa essere utilizzato per queste modifiche, questa soluzione non è ideale per un lavoro ordinato. Ti consiglio di scegliere un software specificamente progettato per questo scopo, come [VS Code](https://code.visualstudio.com/download) o [Sublime Text](https://www.sublimetext.com/download). Sublime Text, essendo particolarmente leggero, sarà più che sufficiente per le nostre esigenze.
- Installa uno di questi programmi software e tienilo da parte per le tue future modifiche. ![github-desktop](assets/26.webp)
Congratulazioni! Il tuo ambiente di lavoro è ora configurato per contribuire a PlanB Network. Ora puoi esplorare i nostri altri tutorial specifici per ogni tipo di contributo (traduzione, revisione, scrittura.

https://planb.network/tutorials/others

..).
