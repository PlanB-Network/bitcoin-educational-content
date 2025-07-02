---
name: Linee guida da seguire durante il proofreading
description: Quali sono i fattori importanti da tenere a mente per il proofreading su Plan ₿ Network?
---

![github](assets/cover.webp)


Benvenuti in questo tutorial sulle **linee guida da seguire per la revisione dei contenuti su Plan ₿ Network**. Siamo lieti che condividiate la nostra missione di tradurre i materiali del Bitcoin nel maggior numero di lingue possibile, al fine di aiutare le persone a conoscere il suo funzionamento e il suo utilizzo nella vita quotidiana.


Innanzitutto, contribuire a Plan ₿ Network [repository pubblico](https://github.com/PlanB-Network/Bitcoin-educational-content) ti dà la possibilità di scrivere tutorial, correggere i contenuti esistenti o persino proporre l'aggiunta di una nuova lingua alla piattaforma. Per saperne di più, iscrivetevi prima al nostro [Gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) e scrivete una breve presentazione di voi e delle lingue che sapete parlare.


Il presente tutorial è dedicato ai collaboratori che vogliono fare proofreading dei contenuti sul repo. La maggior parte di loro non sa molto di [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) o del [linguaggio Markdown](https://www.markdownguide.org/basic-syntax/) che usiamo all'interno del repository, quindi è importante condividere alcuni approfondimenti sui fattori chiave coinvolti in questo compito.


Qui di seguito ho raccolto i problemi più comuni che i proofreader incontrano. Sentitevi liberi di suggerirne altri, perché possono aiutare gli altri a migliorare.


Prima di addentrarci nello specifico, la prima cosa da fare è leggere questo tutorial sulle azioni pratiche da seguire su Github, effettuando il fork del repository Plan ₿ Network, effettuando il commit delle modifiche e inviando le PR:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## Che cos'è la correzione di bozze?


La correzione di bozze è il processo di revisione finale di un testo scritto, per identificare e correggere gli errori di grammatica, ortografia, punteggiatura e formattazione. Assicura che il testo sia chiaro, coerente e privo di errori prima della pubblicazione o dell'invio.


Quando si esegue questo tipo di compito, è importante seguire il significato della lingua originale (EN o FR), ma assicurarsi che il testo nella lingua finale sia il più fluido possibile per un madrelingua.


Ricordate sempre che la traduzione/correzione è EDUCAZIONE!


Infatti, il nostro obiettivo comune è quello di educare il maggior numero possibile di persone sul Bitcoin, quindi è fondamentale che il materiale che leggono sia scorrevole e chiaro.

In questo senso, tutti i collaboratori del Plan ₿ Network sono educatori!


## I primi passi prima della correzione di bozze su Plan ₿ Network


Prima di iniziare un nuovo compito di correzione, annunciatelo nel [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o informate il vostro coordinatore Plan ₿ Network, che aprirà un [topic] dedicato(https://github.com/orgs/PlanB-Network/projects/3). Quando si riceve il link alla questione, è sufficiente **commentare che si sta iniziando** con il compito di correzione di quel contenuto.


Questo sistema aiuta il coordinatore a tenere traccia dei progressi all'interno del repo e consente di "rivendicare" il contenuto da parte del correttore, evitando che qualcun altro faccia sforzi doppi.

Nel problema stesso, troverete i link che vi reindirizzano al contenuto da controllare. Si può semplicemente fare clic su di essi o, ancora meglio, si può tornare al proprio repo biforcuto e lavorare direttamente da lì. Vediamo come fare!


Prima di tutto, **ricordatevi SEMPRE di sincronizzare il vostro repo, sul ramo "dev "**. In questo modo, il contenuto sarà sempre aggiornato prima di iniziare qualsiasi tipo di attività e non si creeranno conflitti tra il materiale vecchio e quello nuovo. Assicurarsi di fare clic su "Sync Fork" e "Update branch".



![REVIEW](assets/en/1.webp)



Dopo la sincronizzazione, si può accedere direttamente al contenuto di interesse e fare il commit su un nuovo ramo, come mostrato in questo [tutorial](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Altrimenti, si può aprire un nuovo ramo dove lavorare, facendo clic su "Rami", come mostrato di seguito.



![REVIEW](assets/en/2.webp)



All'interno di questa nuova pagina, sotto il titolo "Le tue filiali" si trovano tutte le filiali già aperte. Questa sezione è molto utile perché vi permette di trovare facilmente il punto in cui avete modificato un contenuto. Se si desidera aprire un nuovo ramo, è possibile fare clic su "Nuovo ramo" nell'angolo superiore destro della pagina.



![REVIEW](assets/en/3.webp)



Si aprirà quindi un pop-up in cui si dovrà inserire il nome della nuova filiale. Nel caso seguente, ho scelto di chiamarla "BTC101-FR". In questo modo, ricorderò sempre che questo ramo specifico deve essere usato per la correzione del corso BTC101 in francese e **non lo userò per nessun altro compito**.


Vi suggerisco di fare lo stesso: assicuratevi di aprire un nuovo ramo ogni volta che dovete iniziare una nuova attività.



![REVIEW](assets/en/4.webp)



Dopo aver creato questo nuovo ramo, assicurarsi di fare clic su di esso da "I tuoi rami" nella pagina precedente e iniziare a lavorare sul file *.md* relativo al contenuto specifico (nel mio caso, farò clic su "corsi" -> "BTC101" -> "fr.md"). Tutti i commit relativi a quel file specifico dovranno essere impegnati (salvati) all'interno dello stesso ramo.



## Lingua originale o traduzione?


Quando si effettua la correzione di un contenuto, è importante **controllare sempre la versione originale in inglese (o francese)**. Tenete presente che traduciamo utilizzando strumenti linguistici AI, quindi la resa nella lingua di destinazione potrebbe non essere fluida o ben comprensibile per il lettore finale.


Pertanto, sentitevi liberi di apportare modifiche al testo e di modificare le frasi, se necessario. Il nostro obiettivo è quello di migliorare la fluidità, ma sempre rispettando il significato originale. In caso di dubbi su come trattare una parola specifica, chiedete al coordinatore della traduzione.


Gli strumenti di LLM possono tradurre alcune parole relative al Bitcoin in modo letterale, come il Lightning Network. Ciò accade soprattutto quando si tratta di parole molto tecniche. In casi come questi, è consigliabile mantenere la parola originale inglese nella lingua di destinazione per una maggiore chiarezza, a meno che le regole linguistiche non impongano di tradurre ogni singola parola.


In questo secondo caso, **fate sempre qualche ricerca per vedere se qualcun altro nella vostra comunità Bitcoin ha già tradotto quella parola** ed è ormai ampiamente utilizzata.



- Una soluzione potrebbe essere quella di **controllare su [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** nella lingua di destinazione per vedere se la parola è stata tradotta o meno. Se non lo è, si mantiene la parola in inglese.



- In ogni caso, il mio consiglio è di **inserire la parola EN tuttavia**, aggiungendo il significato corrispondente nella lingua di arrivo all'interno di parentesi tonde, seguendo lo schema EN (LANG), o viceversa. Es. Address (indirizzo), o indirizzo (Address).



- Un'altra buona soluzione è quella di mantenere la parola/frase originale IT, quindi **creare un collegamento ipertestuale** che reindirizzi al [glossario](https://planb.network/en/resources/glossary) su planb.network. Per fare ciò, è necessario inserire la parola/frase all'interno di parentesi quadre e il link all'interno di parentesi tonde, come si può vedere nell'esempio seguente:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Nel risultato finale (immagine sotto) non verrà visualizzato l'intero link e la parola diventerà cliccabile.



![REVIEW](assets/en/5.webp)



Si prega di notare che il link al glossario che prenderete dal sito web contiene il codice della lingua dopo la parola "network" (esempio: ``https://planb.network/en/resources/glossary/UTXO``-> qui potete leggere il codice della lingua "en"). In questo caso, **rimuovete il codice della lingua dal link**, come avete visto nel riquadro qui sopra. In questo modo, il sistema porterà automaticamente il lettore alla lingua designata.


Il contenuto del repository è pieno di collegamenti ipertestuali come questi. Ora che sapete cosa significano, **accertatevi di non cancellare nessun link** inserito dall'autore originale.



- Un'altra cosa legata alla resa delle parole è la seguente. Se nel testo si trova "Plan ₿ Network", **lasciare la parola in questa forma originale**. Non traducete la parola "piano" o la parola "rete". Inoltre, NON utilizzare l'articolo "Il" quando si presenta Plan ₿ Network: **consideratelo come un marchio**.



- Lo stesso vale per "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", che dovrebbero essere conservati nella forma originale.


Un'ultima nota a questo paragrafo: come abbiamo detto sopra, usiamo strumenti di intelligenza artificiale per tradurre i contenuti, e poi chiediamo l'intervento dei collaboratori per assicurarci che tutto sia fluido e ben corretto.


Se si utilizza l'IA per correggere la maggior parte del testo, lo noteremo sicuramente, poiché abbiamo familiarità con le strutture tipiche delle frasi generate dall'IA. Se scopriamo che vi siete affidati esclusivamente all'IA per la correzione delle bozze, senza applicare modifiche significative, la ricompensa finale in Sats potrebbe essere ridotta della metà!



## La struttura delle intestazioni


Nel linguaggio markdown, le intestazioni (e i titoli dei paragrafi) iniziano tutte con il segno Hash ``#``. Il numero di segni Hash corrisponde al livello dell'intestazione. Ad esempio, un'intestazione di livello tre ha tre segni numerici prima del testo (ad esempio, `### La mia intestazione').


Nei corsi, le parti più importanti sono introdotte da un singolo segno Hash, mentre le sottoparti possono avere da due a quattro segni Hash. Nei tutorial, di solito si utilizzano solo intestazioni con due segni Hash.



![REVIEW](assets/en/6.webp)



Assicuratevi di non eliminare MAI i segni Hash** prima di un titolo, altrimenti creerete problemi con la struttura del testo.


Allo stesso tempo, **non cambiare** la parte del chapterID che si può vedere nell'immagine qui sopra, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` o i riferimenti al video come ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Quando inseriamo ``#`` prima di un titolo, questo diventerà automaticamente in grassetto nell'anteprima del corso, quindi **evitare di rendere i titoli in grassetto durante la correzione**.


Come nota a margine, nella versione EN dei corsi, i **titoli introdotti da uno o due ``#`` hanno tutte le parole che iniziano in maiuscolo**, mentre i titoli che iniziano con tre o quattro ``#``, di solito non seguono questa regola. Se possibile, assicuratevi che i titoli nella vostra lingua d'arrivo seguano questa struttura.



## La sezione iniziale dei corsi


All'inizio di ogni contenuto si trovano le seguenti parole statiche in minuscolo: "nome", "descrizione", "obiettivi". Sono utilizzate dal sito web per decodificare il contenuto stesso e sono **sempre lasciate in EN**. Di conseguenza, NON traducetele, altrimenti il contenuto creerà problemi di sincronizzazione. Assicurarsi di correggere solo la parte dopo i due punti, che viene tradotta automaticamente dall'intelligenza artificiale.



![REVIEW](assets/en/7.webp)



In questa stessa sezione iniziale, mantenete il formato attuale. Non aggiungete nulla all'inizio del testo. Ad esempio, evitate di aggiungere "tt" prima dei trattini, come nell'immagine qui sotto!



![REVIEW](assets/en/8.webp)



## Raccomandazioni sul formato


Di seguito sono riportati alcuni esempi di problemi di formato a cui prestare attenzione quando si revisiona un contenuto nella lingua di destinazione.



- Prestare attenzione a punteggiature strane come ``***`, o ``**`` che potrebbero rappresentare una cattiva resa del simbolo del grassetto. Nell'immagine sottostante, si può notare che gli asterischi sono solo a destra della parola, il che appare strano.



![REVIEW](assets/en/9.webp)



Pertanto, è necessario controllare sempre il testo originale in inglese per vedere se un testo in grassetto dovrebbe essere presente. In questo caso, basta aggiungere due asterischi all'inizio della parola, per farla apparire correttamente sul sito web. Infatti, nel linguaggio markdown, **per rendere il grassetto, è necessario inserire due asterischi ``**`` sia prima che dopo la parola/sentenza** (si veda l'esempio seguente).



![REVIEW](assets/en/10.webp)




- Lo stesso problema può verificarsi con simboli come $ e `` ``.

Assicuratevi di controllare il file della lingua originale (spesso EN o FR) per vedere dove dovrebbero essere questi simboli. È sempre possibile chiedere assistenza al coordinatore.



- Se trovate delle citazioni, assicuratevi di fare qualche ricerca online per trovare la giusta traduzione nella vostra lingua. Le virgolette vengono solitamente inserite dopo il simbolo ``>``.



![REVIEW](assets/en/11.webp)



## Correzione dei quiz


Sapevate che potete anche correggere le domande dei quiz di ogni corso? Ad esempio, se volete correggere i quiz del corso BTC101 di informatica, potete aprire una sezione dedicata e seguire questo percorso: "corsi" -> "BTC101" -> "quiz". Lì troverete tutte le cartelle dedicate a ogni domanda, insieme al relativo file di lingua in formato _yml_.


Ancora una volta, assicuratevi di essere in una filiale dedicata, aperta appositamente per questo scopo, e informate sempre il coordinatore.


Dopo aver esaminato la domanda, assicurarsi di modificare lo stato "revisionato" da "falso" a "vero", come mostrato nell'immagine seguente.



![REVIEW](assets/en/12.webp)


## Correzione del glossario


Come per i quiz, potete anche correggere il glossario. Il glossario originale è stato scritto in francese, quindi troverete frasi come: "In francese, questa espressione può essere tradotta in..."


In casi come questo, vi preghiamo di adattare questa frase alla vostra lingua di destinazione o all'inglese.


## Altre migliori pratiche



- Se è necessario cercare parole specifiche all'interno del testo, è possibile fare clic su ``CTRL+F`` e apparirà la sezione Trova-sostituisci. Questa parte è molto utile quando si ha bisogno di saltare a una parte specifica del testo o di sostituire parole o frasi specifiche in gruppo, senza scorrere l'intero contenuto.



![REVIEW](assets/en/13.webp)



Quando si utilizza la funzione "sostituisci tutto", è importante ricontrollare i risultati per assicurarsi che anche i collegamenti non siano stati modificati. Ad esempio, se si vuole cambiare la parola "Bitcoin" in "Bitkoin" (cosa che potrebbe essere necessaria in alcune lingue), la funzione "sostituisci tutto" può aggiornare efficacemente tutte le istanze nel testo. Tuttavia, si tenga presente che questo strumento modificherà anche tutti i link contenenti quella parola, causando potenzialmente problemi di reindirizzamento.


Nell'esempio che segue, il proofreader ha utilizzato la funzione di cui sopra per sostituire "Satoshi" con "Satoshi(Sats)", modificando anche il link a un tutorial contenente la parola stessa. Di conseguenza, il link è diventato non valido.


Controllare sempre due volte tutti i collegamenti ipertestuali nel testo, per assicurarsi che siano corretti.



![REVIEW](assets/en/14.webp)




- Restando in tema, se l'autore inserisce un link che rimanda a un corso o a un tutorial di Plan ₿ Network (**non** tra parentesi), il sito web creerà automaticamente una "scheda" che mostra la relativa miniatura. Di conseguenza, assicuratevi sempre di **avere uno spazio tra il testo e il link stesso**, altrimenti potreste vedere il seguente errore sul sito.



![REVIEW](assets/en/15.webp)





- Infine, un'altra buona pratica da applicare quando si termina il compito di correzione e si invia la PR è tornare al problema originale aperto dal coordinatore e commentare con "Proofreading completato". **Assicuratevi di inserire anche il link della vostra PR**.



## Conclusione


In sintesi, conoscere gli errori più comuni dei proofreader può aiutarvi a migliorare le vostre capacità di controllo dei contenuti. È facile trascurare aspetti come il contesto o la coerenza, e cogliere questi errori può fare una grande differenza.


Tenete sempre presente che un principiante può leggere questi corsi e tutorial, quindi è nostra responsabilità assicurarci che capisca appieno. Come proofreader, siete un educatore!


Grazie per aver letto questo tutorial e buon viaggio nella correzione delle bozze!