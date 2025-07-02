---
name: Linee guida per la correzione delle bozze
description: Quali sono i fattori importanti da tenere a mente durante la correzione di bozze su Plan ₿ Network?
---
![github](assets/cover.webp)


Benvenuti a questo tutorial sulle linee guida da seguire per la correzione dei contenuti del Plan ₿ Network. Siamo lieti che condividiate la nostra missione di tradurre i materiali del Bitcoin nel maggior numero di lingue possibile, per aiutare le persone a conoscere il suo funzionamento e il suo utilizzo nella vita quotidiana.


Innanzitutto, contribuire a Plan ₿ Network [repository pubblico](https://github.com/PlanB-Network/Bitcoin-educational-content) ti dà la possibilità di scrivere tutorial, correggere i contenuti esistenti o persino proporre l'aggiunta di una nuova lingua alla piattaforma. Per saperne di più, iscrivetevi prima al nostro [Gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) e scrivete una breve presentazione di voi e delle lingue che sapete parlare.


Il presente tutorial è dedicato ai collaboratori che vogliono correggere i contenuti. La maggior parte di loro non sa molto di [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) o del [linguaggio Markdown](https://www.markdownguide.org/basic-syntax/) che usiamo sul repository, quindi è importante condividere alcuni spunti su ciò a cui devono prestare attenzione quando eseguono questo compito.


L'ho creato dopo aver raccolto i problemi più comuni che i correttori di bozze incontrano quando completano i loro compiti. Sentitevi liberi di suggerirne altri, perché possono aiutare gli altri a migliorare.


Prima di addentrarci nello specifico, la prima cosa da fare è leggere questo tutorial sulle azioni pratiche da applicare su Github, effettuando il fork del repository Plan ₿ Network, effettuando il commit delle modifiche e inviando le PR:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

## Che cos'è la correzione di bozze?


La correzione di bozze è il processo di revisione finale di un testo scritto, per identificare e correggere gli errori di grammatica, ortografia, punteggiatura e formattazione. Assicura che il testo sia chiaro, coerente e privo di errori prima della pubblicazione o dell'invio.


Quando si affronta questo tipo di compito, è importante seguire il significato della lingua originale (EN o FR), ma assicurarsi che il testo nella lingua finale sia il più fluido possibile per un madrelingua.


## I primi passi prima della correzione di bozze su Plan ₿ Network


Prima di iniziare un nuovo compito di correzione, annunciatelo nel [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder) o informate il vostro coordinatore Plan ₿ Network, che aprirà un [topic] dedicato(https://github.com/orgs/PlanB-Network/projects/3). Quando si riceve il link alla questione, è sufficiente commentare che si sta iniziando con il compito di correzione di quel contenuto.

Questo sistema consente al coordinatore di tenere traccia dei progressi all'interno del repo e permette di "rivendicare" il contenuto da parte del correttore, evitando che qualcun altro faccia un doppio lavoro.

Sul problema stesso, si trovano i link che portano direttamente al contenuto da controllare. Si può cliccare direttamente su di essi o, ancora meglio, si può tornare al proprio repo biforcuto e lavorare direttamente da lì.


Prima di tutto, ricordatevi SEMPRE di sincronizzare il vostro repo, sul ramo "dev". In questo modo, il contenuto sarà sempre aggiornato prima di iniziare qualsiasi tipo di attività e non si creeranno conflitti tra il materiale vecchio e quello nuovo. Assicurarsi di fare clic su "Sync Fork" e "Update branch".



![REVIEW](assets/en/1.webp)



Dopo la sincronizzazione, si può accedere direttamente al contenuto di interesse e fare il commit su un nuovo ramo, come mostrato in questo [tutorial](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Altrimenti, si può aprire un nuovo ramo dove lavorare, facendo clic su "Rami", come mostrato di seguito.



![REVIEW](assets/en/2.webp)



All'interno di questa nuova pagina, troverete tutti i rami già aperti sotto il titolo "I tuoi rami". Questa sezione è molto utile perché permette di trovare facilmente il luogo in cui si è modificato un contenuto. Se si desidera aprire un nuovo ramo, è possibile fare clic su "Nuovo ramo" nell'angolo superiore destro della pagina.


![REVIEW](assets/en/3.webp)



Si aprirà quindi un pop-up in cui si dovrà inserire il nome della nuova filiale. Nel caso seguente, ho scelto di chiamarla "BTC101-FR". In questo modo, ricorderò sempre che questo ramo specifico deve essere usato per la correzione del corso BTC101 in francese e **non lo userò per nessun altro compito**.


Vi suggerisco di fare lo stesso: assicuratevi di aprire un nuovo ramo ogni volta che dovete iniziare una nuova attività.



![REVIEW](assets/en/4.webp)



Dopo aver creato questo nuovo ramo, assicurarsi di fare clic su di esso da "I vostri rami" nella pagina precedente e iniziare a lavorare sul file *.md* relativo al contenuto specifico (nel mio caso, farò clic sulla cartella "corsi" e sulla sottocartella BTC101, per cercare fr.md). Tutti i commit relativi a quel file specifico dovranno essere impegnati (salvati) all'interno dello stesso ramo.


## Lingua originale o traduzione?


Quando si effettua la correzione di un contenuto, è importante controllare sempre la versione originale in inglese (o francese). Tenete presente che traduciamo utilizzando strumenti linguistici AI, quindi la resa nella lingua di destinazione potrebbe non essere fluida o ben comprensibile per il lettore finale.


Pertanto, sentitevi liberi di apportare modifiche al testo e di modificare le frasi, se necessario. Il nostro obiettivo è quello di migliorare la fluidità, ma sempre rispettando il significato originale. In caso di dubbi su come trattare una parola specifica, chiedete al coordinatore della traduzione.


Gli strumenti LLM possono tradurre letteralmente alcune parole relative al Bitcoin, come Lightning Network, che in italiano diventerebbe "Rete Fulmine", ad esempio.


Questo vale soprattutto quando si tratta di parole molto tecniche. In casi come questi, è consigliabile mantenere la parola originale inglese nella lingua di destinazione per una maggiore chiarezza, a meno che le regole linguistiche non impongano di tradurre ogni singola parola. In questo secondo caso, fate sempre qualche ricerca per vedere se qualcun altro nella vostra comunità Bitcoin ha già tradotto quella parola ed è ormai ampiamente utilizzata.



- Una soluzione potrebbe essere quella di controllare su [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page) nella lingua di destinazione per vedere se la parola è stata tradotta o meno. Se non lo è, si mantiene la parola in inglese.



- In ogni caso, il mio consiglio è di inserire comunque la parola EN e poi il significato corrispondente nella lingua di arrivo all'interno di parentesi tonde, seguendo lo schema EN (LANG), o viceversa. Es. Address (indirizzo) o indirizzo (Address).



- Un'altra buona soluzione è quella di mantenere la parola/frase originale IT, quindi creare un collegamento ipertestuale che reindirizzi al [glossario](https://planb.network/en/resources/glossary) su planb.network. Per fare ciò, è necessario inserire la parola/frase all'interno di parentesi quadre e il link all'interno di parentesi tonde, come si può vedere nell'esempio seguente:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Nel risultato finale (immagine sotto) non verrà visualizzato l'intero link e la parola diventerà cliccabile.


![REVIEW](assets/en/5.webp)



Tenete presente che il link al glossario che prenderete dal sito contiene il codice della lingua dopo la parola "network" (esempio: ``https://planb.network/en/resources/glossary/UTXO``-> qui potete leggere il codice della lingua "en"). In questo caso, rimuovete il codice della lingua dal link, come avete visto nel riquadro qui sopra. In questo modo, il sistema porterà automaticamente il lettore alla lingua designata.


Il contenuto del repo è pieno di collegamenti ipertestuali come questi. Ora che sapete cosa significano, assicuratevi di non cancellare nessun collegamento inserito dall'autore.


Un'altra cosa legata alla resa delle parole è la seguente. Se nel testo trovate "Plan ₿ Network", lasciatelo in questa forma originale. Non traducete la parola "piano" o la parola "rete". Inoltre, NON usate l'articolo "Il" quando presentate Plan ₿ Network e **consideratelo come un marchio**.


Lo stesso vale per "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", che dovrebbero essere conservati nella forma originale.


Un'ultima nota a questo paragrafo: come abbiamo detto sopra, usiamo strumenti di intelligenza artificiale per tradurre i contenuti, e poi chiediamo l'intervento "umano" per assicurarci che tutto sia fluido e ben corretto.


Se la correzione delle bozze viene effettuata utilizzando l'IA per la maggior parte del testo, lo noteremo sicuramente, poiché conosciamo le strutture tipiche delle frasi generate dall'IA. Se scopriamo che vi siete affidati esclusivamente all'IA per la correzione, senza apportare modifiche significative, la ricompensa finale in Sats potrebbe essere dimezzata!


## La struttura delle intestazioni


Nel linguaggio markdown, le intestazioni (e i titoli dei paragrafi) iniziano tutte con il segno Hash ``#``. Il numero di segni Hash corrisponde al livello dell'intestazione. Ad esempio, un'intestazione di livello tre ha tre segni numerici prima del testo (ad esempio, `### La mia intestazione').


Nei corsi, le parti più importanti sono introdotte da un singolo segno Hash, mentre le sottoparti possono avere da due a quattro segni Hash. Nei tutorial, di solito si usano solo intestazioni con due segni Hash.



![REVIEW](assets/en/6.webp)


Assicuratevi di non eliminare MAI i segni Hash prima di un titolo, altrimenti creerete problemi con la struttura del testo.


Allo stesso tempo, **non** cambiare la parte del chapterID che si può vedere nell'immagine qui sopra, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` o i riferimenti al video come ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Quando inseriamo ``#`` prima di un titolo, questo diventerà automaticamente in grassetto nell'anteprima del corso, quindi evitate di rendere i titoli in grassetto durante la correzione.


Inoltre, nella versione EN dei corsi, i titoli che hanno uno o due ``#`` hanno tutte le parole che iniziano in maiuscolo, mentre i titoli che iniziano con tre o quattro non seguono questa regola. Se possibile, assicuratevi che i titoli nella vostra lingua d'arrivo seguano questa struttura.


## La sezione iniziale dei corsi


All'inizio di ogni contenuto si trovano le seguenti parole statiche in minuscolo: "nome", "descrizione", "obiettivi". Sono utilizzate dal sito web per decodificare il contenuto stesso e sono **sempre lasciate in EN**. Di conseguenza, NON traducetele, altrimenti il contenuto creerà problemi di sincronizzazione. Assicurarsi di correggere solo la parte dopo i due punti, che viene tradotta automaticamente dall'intelligenza artificiale.



![REVIEW](assets/en/7.webp)



In questa stessa sezione iniziale, mantenete il formato attuale. Non aggiungete nulla all'inizio del testo. Ad esempio, evitate di aggiungere "tt" prima dei trattini, come nell'immagine qui sotto!



![REVIEW](assets/en/8.webp)


## Raccomandazioni sul formato


Di seguito sono riportati alcuni esempi di problemi di formato a cui prestare attenzione quando si revisiona un contenuto nella lingua di destinazione.



- Prestare attenzione a punteggiature strane come ``***`, o ``**`` che potrebbero rappresentare una cattiva resa del simbolo del grassetto. Nell'immagine sottostante, si può notare che gli asterischi sono solo a destra della parola, il che appare strano.


![REVIEW](assets/en/9.webp)



Controllare sempre il testo originale in inglese per vedere se un testo in grassetto dovrebbe essere presente. In questo caso, è sufficiente aggiungere due asterischi all'inizio della parola, per farla apparire correttamente sul sito web. Infatti, nel linguaggio markdown, per rendere il grassetto è necessario inserire due asterischi ``**`` sia prima che dopo la parola/sentenza (si veda l'esempio seguente).



![REVIEW](assets/en/10.webp)




- Lo stesso problema può verificarsi con simboli come $ e `` ``.

Assicuratevi di controllare il file della lingua originale (spesso EN o FR) per vedere dove dovrebbero essere questi simboli. È sempre possibile chiedere assistenza al coordinatore.



- Se trovate delle citazioni, assicuratevi di fare qualche ricerca online per trovare la giusta traduzione nella vostra lingua. Le virgolette vengono solitamente inserite dopo il simbolo ``>``.



![REVIEW](assets/en/11.webp)


## Correzione dei quiz


Sapevate che potete anche correggere le domande dei quiz di ogni corso? Ad esempio, se volete correggere i quiz del corso BTC101 di informatica, potete aprire una sezione dedicata e seguire questo percorso: "corsi" -> "BTC101" -> "quiz" Lì troverete tutte le cartelle dedicate a ogni domanda, insieme al relativo file di lingua in formato _yml_.


Ancora una volta, assicuratevi di essere in una filiale dedicata, aperta appositamente per questo scopo, e informate sempre il coordinatore.


Dopo aver esaminato la domanda, assicurarsi di modificare lo stato "revisionato" da "falso" a "vero", come mostrato nell'immagine seguente.


![REVIEW](assets/en/12.webp)


## Altre migliori pratiche


Se è necessario cercare parole specifiche all'interno del testo, è possibile fare clic su ``CTRL+F`` e apparirà la sezione Trova-sostituisci. Questa parte è molto utile quando si ha bisogno di saltare a una parte specifica del testo o di sostituire parole o frasi specifiche in gruppo, senza scorrere l'intero contenuto.



![REVIEW](assets/en/13.webp)



Quando si utilizza la funzione "sostituisci tutto", è importante ricontrollare i risultati per assicurarsi che anche i collegamenti non siano stati modificati. Ad esempio, se si vuole cambiare la parola "Bitcoin" in "Bitkoin" (cosa che potrebbe essere necessaria in alcune lingue), la funzione "sostituisci tutto" può aggiornare efficacemente tutte le istanze nel testo. Tuttavia, occorre tenere presente che questo strumento modificherà anche tutti i link contenenti la parola, causando potenzialmente problemi di reindirizzamento.


Nell'esempio che segue, il correttore di bozze ha utilizzato la funzione di cui sopra per sostituire "Satoshi" con "Satoshi(Sats)", modificando anche il link a un tutorial contenente la parola stessa. Di conseguenza, il link è diventato non valido.


![REVIEW](assets/en/14.webp)


Restando in tema di link, se l'autore inserisce un link che rimanda a un corso o a un tutorial di Plan ₿ Network, il sito creerà automaticamente una "scheda" che mostrerà la relativa miniatura. Di conseguenza, assicuratevi sempre di avere uno spazio tra il testo e il link stesso, altrimenti potreste vedere il seguente errore sul sito.


![REVIEW](assets/en/15.webp)




Infine, un'altra buona pratica da applicare quando si termina il compito di correzione e si invia la RP è tornare al problema originale aperto dal coordinatore e commentare con "Correzione di bozze effettuata". Assicuratevi di inserire anche il link della vostra RP.


## Conclusione


In sintesi, conoscere gli errori più comuni dei correttori di bozze può aiutarvi a migliorare le vostre capacità di controllo dei contenuti. È facile trascurare aspetti come il contesto o la coerenza, quindi cogliere questi errori può fare una grande differenza. Tenete sempre presente che un principiante potrebbe leggere questi corsi e tutorial, quindi è nostra responsabilità assicurarci che capisca appieno.


Grazie per aver letto questo tutorial e buon viaggio nella correzione delle bozze!