---
name: Linee guida da seguire durante il proofreading
description: Quali sono i fattori importanti da tenere a mente per il proofreading su Plan ₿ Network?
---

![github](assets/cover.webp)

Benvenuto in questo tutorial sulle **linee guida da seguire per la revisione dei contenuti su Plan ₿ Network**. Siamo felici che tu condivida la nostra missione di tradurre risorse su Bitcoin nel maggior numero possibile di lingue, al fine di aiutare le persone a conoscere il suo funzionamento e il suo utilizzo nella vita quotidiana.

Innanzitutto, contribuire al [repository pubblico](https://github.com/PlanB-Network/Bitcoin-educational-content) di Plan ₿ Network ti dà la possibilità di scrivere tutorial, correggere i contenuti esistenti o persino proporre l'aggiunta di una nuova lingua alla piattaforma. Per saperne di più, iscriviti prima al nostro [Gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) e manda una breve presentazione su di te e sulle lingue che conosci.

Questo gruppo è dedicato ai collaboratori che vogliono fare proofreading dei contenuti sul repo. La maggior parte di loro non sa molto di [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) o del [linguaggio Markdown](https://www.markdownguide.org/basic-syntax/) che usiamo all'interno del repository, quindi è importante condividere alcuni approfondimenti sui fattori chiave che il proofreading comporta.

Qui di seguito ho raccolto i problemi più comuni incontrati dai proofreader. Sentititi libero di suggerirne altri, perché possono aiutare gli altri a migliorare.

Prima di addentrarci nello specifico, la prima cosa da fare è leggere questo tutorial sulle azioni pratiche da seguire su Github, ad esempio come procedere al fork del repository di Plan ₿ Network, salvare le modifiche (commit) e inviare le Pull Request (PR):

https://planb.network/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017

## Che cos'è il proofreading?

Il proofreading (o correzione di bozze) è il processo di revisione finale di un testo scritto, che serve per individuare e correggere gli errori di grammatica, ortografia, punteggiatura e formattazione. È la fase del lavoro che assicura che il testo sia chiaro, coerente e privo di errori prima della pubblicazione o dell'invio.

Quando si svolge questo tipo di compito, è importante seguire il significato espresso nella lingua originale (EN o FR), assicurandosi che il testo nella lingua finale sia il più fluido possibile per un madrelingua.

Ricordati sempre che traduzione/proofreading è EDUCAZIONE!

Il nostro obiettivo comune è infatti quello di educare il maggior numero possibile di persone su Bitcoin, quindi è fondamentale che le risorse che leggono siano scorrevoli e chiare. In questo senso, tutti i collaboratori di Plan ₿ Network sono educatori!

## I primi passi prima del proofreading su Plan ₿ Network

Prima di iniziare un nuovo proofreading, comunicalo nel [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o informa il tuo coordinatore di Plan ₿ Network, che aprirà appositamente una [issue](https://github.com/orgs/PlanB-Network/projects/3). Quando ricevi il link alla issue è sufficiente che **commenti comunicando che stai iniziando** il proofreading di quel contenuto.

Questo sistema aiuta il coordinatore a tenere traccia dei progressi all'interno del repo e consente al proofreader di "rivendicare" il contenuto, evitando che qualcun altro lo faccia. Nella issue stessa troverai i link che ti reindirizzeranno al contenuto da correggere. Puoi semplicemente fare clic su di essi o, ancora meglio, tornare al fork del tuo repo e lavorare direttamente da lì. Vediamo come fare!

Prima di tutto, **ricordati SEMPRE di sincronizzare il tuo repo, sul branch "dev"**. In questo modo il contenuto sarà sempre aggiornato prima di iniziare qualsiasi tipo di attività e non si creeranno conflitti tra la versione vecchia e quello nuova. Assicurati di fare clic su "Sync Fork" e "Update branch".

![REVIEW](assets/en/1.webp)

Dopo la sincronizzazione, puoi accedere direttamente al testo che vuoi correggere e salvare i commit su un nuovo branch, come mostrato in questo [tutorial](https://planb.network/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Altrimenti puoi creare un nuovo branch dove lavorare, facendo clic su "Branches", come mostrato di seguito.

![REVIEW](assets/en/2.webp)

All'interno di questa nuova pagina, sotto il titolo "Your Branches" si trovano tutti branch aperti e in lavorazione. Questa sezione è molto utile perché ti permette di trovare facilmente dove hai modificato un contenuto. Se desideri aprire un nuovo branch, puoi cliccare su "New Branch" nell'angolo superiore destro della pagina.

![REVIEW](assets/en/3.webp)

Si aprirà quindi un pop-up in cui dovrai inserire il nome del nuovo branch. Nell'esempio che segue, ho scelto di chiamarlo "BTC101-FR". In questo modo ricorderò sempre che questo specifico branch deve essere usato per la correzione del corso BTC101 in francese e **non lo userò per nessun'altra revisione**.

Ti suggerisco di fare lo stesso: assicurati di aprire un nuovo branch ogni volta che inizi un nuovo proofreading.

![REVIEW](assets/en/4.webp)

Dopo aver creato questo nuovo branch, assicurati di selezionarlo dal menu "Your Branches" nella pagina precedente e iniziare a lavorare sul file _.md_ relativo al contenuto specifico (nel mio caso, farò clic su "corsi" -> "BTC101" -> "fr.md"). Tutti i commit relativi a quel file specifico dovranno essere salvati (Commit Changes) all'interno dello stesso branch.

## Lingua originale o traduzione?

Quando si affronta il proofreading, è importante **controllare sempre la relativa versione originale in inglese (o francese)**. Tieni presente che traduciamo utilizzando LLM AI, quindi la resa finale nella tua lingua potrebbe non essere fluida o ben comprensibile per il lettore.

Pertanto, sentiti libero di apportare modifiche al testo e di modificare le frasi, se necessario. Il nostro obiettivo è quello di migliorare la fluidità, ma sempre rispettando il significato originale. In caso di dubbi su come trattare una parola specifica, chiedi al coordinatore della traduzione.

Gli strumenti di LLM possono tradurre alcune parole relative a Bitcoin in modo letterale, come Rete Fulmine (Lightning Network). Ciò accade soprattutto quando si tratta di parole molto tecniche. In casi come questi è consigliabile, per una maggiore chiarezza, mantenere la parola originale inglese anche nella tua lingua, a meno che le regole linguistiche non impongano di tradurre ogni singolo vocabolo.

In questo secondo caso, **fai sempre qualche ricerca per vedere se qualche altro membro nella tua comunità Bitcoin ha già tradotto quella parola** ed è ormai ampiamente utilizzata.

- Una soluzione potrebbe essere quella di **controllare la pagina di [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** nella tua lingua, per vedere se il termine è stata tradotta o meno. Se non lo è, si mantiene l'originale in inglese.

- In ogni caso il mio consiglio è di **inserire comunque il termine inglese**, aggiungendo il significato corrispondente nella tua lingua, magari tra parentesi, seguendo lo schema EN (ITA), o viceversa. Es. Address (indirizzo), o indirizzo (Address).

- Un'altra buona soluzione è quella di mantenere la parola/frase originale inglese, quindi **creare un collegamento ipertestuale** che reindirizzi al [glossario](https://planb.network/en/resources/glossary) su planb.network. Per far questo è necessario inserire la parola/frase all'interno di parentesi quadre e il link all'interno di parentesi tonde, come vedi nell'esempio seguente:

```
[UTXO](https://planb.network/resources/glossary/utxo)
```
Nel risultato finale (immagine sotto) il link non è visualizzato e la parola diventa cliccabile.

![REVIEW](assets/en/5.webp)

Ti chiedo di tenere presente che il link al glossario che prenderai dal sito web, contiene il codice della lingua dopo la parola "network" (esempio: `https://planb.network/en/resources/glossary/utxo`-> qui puoi leggere il codice della lingua "en"). In questo caso **rimuovi il codice della lingua dal link**, come hai visto nel riquadro qui sopra. In questo modo il sistema porterà automaticamente il lettore alla lingua che ha già scelto.

I contenuti del repository sono pieni di link come questi. Ora che sai cosa significano, **accertati di non cancellarne nessuno** inserito dall'autore originale, durante il tuo proofreading.

- Un'altra cosa legata alla visualizzazione delle parole questa: se nel testo trovi "Plan ₿ Network", **lascialo nella forma originale**. Non tradurre la parola "plan" o la parola "network". Inoltre, NON utilizzare l'articolo "Il" quando si presenta Plan ₿ Network: **consideralo come un marchio**.

- Lo stesso vale per "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", che dovrebbero essere conservati nella forma originale.

Un'ultima nota a questo proposito: come abbiamo detto sopra, usiamo strumenti di intelligenza artificiale per tradurre i contenuti e poi chiediamo l'intervento dei collaboratori per assicurarci che tutto sia fluido e ben corretto.

Se utilizzerai l'IA per correggere la maggior parte del testo lo noteremo sicuramente, poiché abbiamo familiarità con le strutture tipiche delle frasi generate da questi strumenti. Se scopriamo che ti sei affidato esclusivamente all'IA per il proofreading, senza apportare modifiche significative, la ricompensa finale in Sats potrebbe essere ridotta della metà!

## La struttura degli headers

Nel linguaggio markdown, gli header (intestazioni e titoli dei paragrafi) iniziano tutti con il segno Hashtag `#`. La quantità di hashtag corrisponde al livello dell'header. Un header di livello tre ha tre hashtag prima del testo (ad esempio, `### My Header').

Nei corsi le parti più importanti sono introdotte da un singolo Hashtag, mentre i sotto-capitoli possono avere da due a quattro hashtag. Nei tutorial di solito si utilizzano solo header con due Hash.

![REVIEW](assets/en/6.webp)

Assicurati di **non eliminare MAI gli Hashtag** prima di un titolo, altrimenti ci saranno problemi con la struttura del testo.

Allo stesso tempo, **non cambiare** la parte del chapterID che puoi vedere nell'immagine sopra, `<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>` o i riferimenti al video come `:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::`.

Quando inseriamo `#` prima di un titolo, questo diventerà automaticamente in grassetto nell'anteprima del corso, quindi **evita di formattare i titoli in grassetto durante la correzione**.

Come nota a margine, nella versione inglese dei corsi, i **titoli preceduti da uno o due `#` hanno tutte le parole che iniziano in maiuscolo**, mentre i titoli preceduti da tre o quattro `#`, di solito non sono sottoposti questa regola. Se possibile, assicurati che i titoli nella tua lingua seguano questa struttura.

## La sezione iniziale dei corsi

All'inizio di ogni contenuto troverai delle parole fisse in minuscolo: "name", "description", "objectives". Sono utilizzate dal sito web per decodificare il contenuto stesso e devono essere **sempre lasciate in inglese**. Di conseguenza, NON tradurle, altrimenti il contenuto creerà problemi di sincronizzazione. Assicurati di correggere solo la parte dopo i due punti, che viene tradotta automaticamente dall'intelligenza artificiale.

![REVIEW](assets/en/7.webp)

In questa stessa sezione iniziale, mantieni il formato attuale. Non aggiungere nulla all'inizio del testo. Ad esempio, evita di aggiungere "tt" prima dei trattini, come nell'immagine qui sotto!

![REVIEW](assets/en/8.webp)

## Raccomandazioni sul formato

Di seguito sono riportati alcuni esempi di problemi di formato a cui prestare attenzione quando revisionerai un contenuto nella tua lingua.

- Fai attenzione a punteggiature strane come `\*\*\`, o `**` che potrebbero rappresentare una pessima visualizzazione del grassetto. Nell'immagine sottostante, puoi notare che gli asterischi sono solo a destra della parola, il che appare strano.

![REVIEW](assets/en/9.webp)

È quindi necessario controllare sempre il testo originale in inglese, per vedere se è previsto il testo in grassetto. In questo caso, basta che tu aggiunga due asterischi all'inizio della parola, per farla apparire correttamente sul sito web. Infatti, nel linguaggio markdown, **per formattare in grassetto, è necessario inserire due asterischi `**` sia prima che dopo la parola/frase** (guarda l'esempio seguente).

![REVIEW](assets/en/10.webp)

- Lo stesso problema può verificarsi con simboli come $ e ```. Assicurati di controllare il file nella lingua originale (spesso EN o FR) per vedere dove dovrebbero essere questi simboli. In ogni caso, ti sarà sempre possibile chiedere l'assistenza del coordinatore.

- Se trovi delle citazioni, assicurati di fare qualche ricerca online per trovare la giusta traduzione nella tua lingua. Le virgolette vengono solitamente inserite dopo il simbolo `>`.

![REVIEW](assets/en/11.webp)

## Correzione dei quiz

Sapevi che puoi correggere anche le domande dei quiz di ogni corso? Ad esempio, se vuoi correggere i quiz del corso BTC101 di italiano, puoi aprire un branch dedicato e seguire questo percorso: "corsi" -> "BTC101" -> "quiz". Lì troverai tutte le cartelle dedicate a ogni domanda, insieme al relativo file nella specifica lingua, in _formato yml_.

Anche qui, assicurati di essere in un branch dedicato, aperto appositamente per questo scopo, e informa sempre il coordinatore.

Dopo aver revisionato la domanda, assicurati di modificare lo stato "reviewed" da "false" a "true", come mostrato nell'immagine seguente.

![REVIEW](assets/en/12.webp)

## Proofreading del glossario

Come per i quiz, puoi revisionare anche il glossario. Il glossario originale è stato scritto in francese, quindi troverai frasi come: "In francese, questa espressione può essere tradotta in..."

In casi come questo, ti chiediamo di adattare questa frase alla tua lingua o all'inglese.

## Altre buone pratiche

- Se hai bisogno di cercare parole specifiche all'interno del testo, puoi far clic su ``CTRL+F`` e ti apparirà la sezione Trova-sostituisci (Find-Replace)- Questa funzione è molto utile quando hai bisogno di saltare a una parte specifica del testo o di sostituire parole o frasi specifiche in gruppo, senza scorrere il testo intero.

![REVIEW](assets/en/13.webp)

Quando si utilizza la funzione "replace all", è importante ricontrollare i risultati per assicurarsi che non siano stati alterati anche i link ipertestuali. Ad esempio, se devi cambiare la parola "Bitcoin" in "Bitkoin" (cosa che potrebbe essere necessaria in alcune lingue), la funzione "sostituisci tutto" può aggiornare efficacemente tutte le istanze nel testo. Tuttavia, tieni presente che questo strumento modificherà anche tutti i link contenenti quella parola, causando potenzialmente problemi di indirizzamento.

Nell'esempio che segue, il proofreader ha utilizzato la funzione di cui sopra per sostituire "Satoshi" con "Satoshi(Sats)", modificando anche il link a un tutorial contenente la parola stessa. Di conseguenza, il link è diventato non valido.

Controlla sempre due volte tutti i link presenti nel testo, per assicurarti che siano corretti.

![REVIEW](assets/en/14.webp)

- Restando in tema, se l'autore inserisce un link che rimanda a un corso o a un tutorial di Plan ₿ Network (**non** tra parentesi), il sito web creerà automaticamente una "scheda" che mostra la relativa anteprima. Di conseguenza, assicurati sempre di **avere uno spazio tra il testo e il link stesso**, altrimenti potresti vedere sul sito un errore come questo.

![REVIEW](assets/en/15.webp)

- Infine, un'altra cosa buona che puoi fare quando hai finito il proofreading e stai per inviare la PR, è tornare alla issue originale aperta dal coordinatore e commentare con "Proofreading completato". **Assicurati di inserire anche il link della tua PR**.

## Conclusione

Per riassumere: conoscere gli errori più comuni dei proofreader può aiutarti a migliorare le tue capacità di revisione dei contenuti. È facile trascurare aspetti come il contesto o la coerenza. Cogliere questi errori può fare una grande differenza.

Tieni sempre presente che un principiante può leggere questi corsi e tutorial, quindi è nostra responsabilità assicurarci che capisca al 100%. Come proofreader, sei un educatore!

Grazie per aver letto questo tutorial e buon viaggio nel proofreading!
