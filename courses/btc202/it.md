---
name: Impostazione del primo nodo Bitcoin
goal: Comprensione, installazione, configurazione e utilizzo di un nodo Bitcoin
objectives: 


  - Comprendere il ruolo e lo scopo di un nodo Bitcoin.
  - Identificare le diverse soluzioni hardware e software disponibili.
  - Installare e configurare un Full node (Bitcoin core).
  - Utilizzate l'ombrello Interface e aggiungete applicazioni utili.
  - Collegare un Wallet personale al proprio nodo.
  - Esplorate le impostazioni avanzate e le migliori pratiche di sicurezza.


---
# Diventare un bitcoiner sovrano



Probabilmente conoscete l'adagio "Not your keys, not your coins", che incoraggia l'autocustodia dei vostri bitcoin. Possedere le proprie chiavi è un primo passo essenziale, ma non è sufficiente. Per ottenere la vera sovranità monetaria, è necessario anche installare e utilizzare il proprio nodo Bitcoin. Questo corso è stato progettato per guidarvi in questo passo fondamentale del vostro viaggio in Bitcoin!



Il BTC 202 è un corso accessibile progettato per insegnarvi a filare il vostro nodo Bitcoin, anche se non siete esperti di tecnica. Inizieremo definendo che cos'è un nodo Bitcoin, a che cosa serve e perché è assolutamente indispensabile farne uno da soli. Poi vi guiderò passo dopo passo nella scelta dell'hardware, nell'installazione del software necessario, nel collegamento del Wallet e nelle prime ottimizzazioni possibili per andare oltre.



La gestione di un nodo Bitcoin non è solo un'opzione per gli esperti, ma una necessità. È uno strumento di resilienza che ogni utente deve comprendere e implementare. Questo corso è il punto di partenza per diventare un bitcoiner sovrano!




+++




# Introduzione


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Panoramica del corso


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Benvenuti a BTC 202, dove imparerete a installare, configurare e utilizzare un nodo Bitcoin in modo semplice e indipendente. Ma non solo: imparerete anche a conoscere il posto e la funzione dei nodi nel sistema Bitcoin. Il corso alterna spiegazioni teoriche e pratica guidata.



### Parte 1 - Introduzione



In questa prima parte del corso, chiariremo le nozioni di base per poi passare a definizioni più precise. Che cos'è un nodo? Quali sono le differenze tra nodo, Wallet e Miner? Si parlerà poi del Bitcoin core e delle implementazioni del protocollo. L'obiettivo è quello di parlare la stessa lingua, evitare confusione e stabilire una solida base teorica.



### Parte 2 - Diventare un bitcoiner sovrano



In questa seconda parte, inizierò spiegando perché è importante gestire il proprio nodo Bitcoin. Esploreremo poi i diversi tipi di nodi esistenti (completo, pruned, SPV...), il loro funzionamento e le loro implicazioni tecniche.



Vi forniremo quindi una panoramica del software disponibile per l'esecuzione di un nodo Bitcoin, con i relativi vantaggi e svantaggi. Infine, concluderemo con alcuni consigli pratici per la scelta dell'hardware adatto alle vostre esigenze e al vostro budget.



Questa sezione, quindi, illustra il percorso del bitcoiner sovrano: capire perché è necessario gestire un nodo, scegliere il tipo di nodo, in base a questa scelta, selezionare il software e, in base al software scelto, determinare l'hardware appropriato.



### Parte 3 - Installazione semplice di un nodo Bitcoin



Una volta completata questa preparazione, è il momento di passare alla pratica con la Parte 3 dedicata a Umbrel: il sistema operativo per il cloud domestico che semplifica il self-hosting e l'installazione di un nodo Bitcoin e Lightning.



Dopo una breve introduzione a Umbrel, forniremo un tutorial dettagliato per guidarvi attraverso il processo di installazione e configurazione sulla vostra macchina fai-da-te. L'obiettivo di questa parte è chiaro: avere il vostro primo nodo Bitcoin completamente funzionante e sincronizzato.



### Parte 4 - Collegamento del Wallet al nodo



Ora che avete configurato un nodo Bitcoin, è il momento di usarlo! In questa sezione imparerete a collegare il vostro software di gestione Wallet (come il Sparrow wallet) al vostro indicizzatore Address (Electrs o Fulcrum) o direttamente al Bitcoin core, in modo da non dipendere più dai server pubblici.



Esamineremo anche il ruolo degli indicizzatori e i vari metodi di connessione al proprio nodo (LAN, Tor, Tailscale, ecc.). Infine, nell'ultimo capitolo, passeremo in rassegna le applicazioni più utili disponibili su Umbrel per il bitcoiner di tutti i giorni.



### Parte 5 - Concetti avanzati e best practice



In questa parte finale di BTC 202, l'obiettivo è quello di approfondire le vostre conoscenze. In primo luogo, esamineremo le migliori pratiche da adottare con il vostro nuovo nodo Bitcoin e come mantenerlo a lungo termine.



In seguito, ci occuperemo di rivedere alcune delle teorie trattate in precedenza nel corso, tra cui la comprensione del processo IBD e la scoperta dei peer in dettaglio, l'esplorazione dell'anatomia di un nodo e, infine, l'apprendimento dell'uso del file `Bitcoin.conf` per mettere a punto le impostazioni.



### Parte 6 - Sezione finale



Come per tutti i corsi Plan ₿ Network, nella sezione finale troverete un esame finale per verificare le vostre conoscenze sui nodi Bitcoin.



Allora, siete pronti ad accendere il vostro primo nodo Bitcoin? Fate rotta verso la sovranità!



## Che cos'è un nodo Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Come descritto dal suo creatore, Satoshi Nakamoto, Bitcoin si presenta come un sistema di denaro elettronico peer-to-peer. Questa semplice frase, che è il titolo del Libro Bianco, contiene molti indizi sulla natura del Bitcoin:




- Innanzitutto, il Satoshi descrive il Bitcoin come un "sistema", in altre parole un insieme coerente di componenti hardware e software che interagiscono per fornire un servizio specifico o svolgere una funzione specifica;
- Spiega poi che questo sistema consente l'uso di contanti elettronici, cioè di una forma di moneta immateriale;
- Infine, sottolinea che questo sistema non dipende da alcuna entità centrale: è "peer-to-peer", cioè sono gli stessi utenti a gestire il sistema.



Poiché Bitcoin è un sistema, deve necessariamente essere eseguito su computer. E, data la sua natura peer-to-peer, sono gli stessi utenti ad assumersi la responsabilità di far funzionare queste macchine. Quello che chiamiamo "nodo Bitcoin" è proprio il computer su cui gira il software che implementa il protocollo Bitcoin (come il Bitcoin core, ma su questo torneremo più avanti). Questo è ciò che consente al Bitcoin di operare senza un'autorità centrale: la convalida viene effettuata in modo distribuito, da migliaia di macchine indipendenti appartenenti a migliaia di utenti.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



Sono proprio questi utenti a garantire la sicurezza del Bitcoin. Come spiega Eric Voskuil nel suo libro *Cryptoeconomics*, la sicurezza del Bitcoin non si basa né sul Blockchain, né sulla potenza di hashing, né sulla validazione, sulla decentralizzazione, sulla crittografia, sull'open source o sulla teoria dei giochi. La sicurezza del Bitcoin dipende principalmente dagli individui che sono disposti a esporsi al rischio personale. La decentralizzazione permette di distribuire questo rischio su un gran numero di individui, ed è solo la loro capacità di resistere che garantisce la solidità del sistema.



Questo principio è facile da capire: se il Bitcoin dipendesse da un singolo nodo di proprietà di un'unica persona, l'imprigionamento di questa persona sarebbe sufficiente a spegnere la rete, poiché da sola si assumerebbe tutti i rischi. Con decine di migliaia di nodi sparsi in tutto il mondo, il rischio è diffuso: ognuno di questi operatori dovrebbe essere neutralizzato per spegnere il Bitcoin.



![Image](assets/fr/048.webp)



Possiamo quindi distinguere e nominare diversi concetti per chiarire le cose per il resto del corso:




- Valuta Bitcoin: l'unità di conto utilizzata per le transazioni all'interno di questo sistema;
- La rete Bitcoin: l'insieme di tutti i nodi connessi;
- Nodi Bitcoin: macchine che eseguono un'implementazione di Bitcoin;
- Implementazioni Bitcoin: software che traduce il protocollo in istruzioni eseguibili;
- Protocollo Bitcoin: l'insieme delle regole che governano il funzionamento del sistema;
- Il sistema Bitcoin: la combinazione coerente di tutti questi Elements.



### Il ruolo del nodo Bitcoin



L'insieme dei nodi Bitcoin forma la cosiddetta rete Bitcoin. Essi consentono all'intero sistema di operare in modo autonomo, senza ricorrere a un'autorità centrale o a una gerarchia di server.



Fin dall'inizio, il Bitcoin è stato progettato per consentire a ciascun utente di gestire un nodo personale. Questo caso rimane valido con l'attuale software Bitcoin core, che combina i ruoli di Wallet e nodo. Al giorno d'oggi, però, questa funzione è spesso dissociata: molti portafogli Bitcoin moderni sono solo portafogli che si collegano a nodi esterni (di proprietà della stessa persona o meno).



### Mantenere Blockchain



Il primo compito di un nodo è quello di mantenere una copia locale della Blockchain. Per prevenire il Double-spending sul Bitcoin senza coinvolgere un'autorità centrale, ogni utente deve verificare che non esista alcuna transazione nel sistema. L'unico modo per esserne certi è conoscere tutte le transazioni effettuate su Bitcoin. Per questo motivo, tutte le transazioni sono marcate temporalmente e raggruppate in blocchi, e ogni nodo memorizza l'intero Blockchain.



> L'unico modo per confermare l'assenza di una transazione è essere a conoscenza di tutte le transazioni.

Nakamoto, S. (2008). *Bitcoin: un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



Il Blockchain è quindi un registro in evoluzione: ogni volta che un nuovo blocco viene pubblicato da un Miner, il nodo ne verifica la validità prima di aggiungerlo alla propria copia locale della catena. Ad oggi (luglio 2025), l'intero Blockchain supera i 675 GB e questa dimensione continua a crescere, poiché viene aggiunto un nuovo blocco in media ogni 10 minuti.



![Image](assets/fr/049.webp)



Il nodo mantiene anche un registro locale di tutti gli UTXO esistenti in un dato momento, noto come **UTXO set**. Questo database contiene tutti i frammenti Bitcoin non spenti. Questo argomento sarà ripreso in dettaglio nella parte finale del corso.



### Verifica e distribuzione delle transazioni



Il secondo ruolo di un nodo è quello di assicurare la verifica e la propagazione delle transazioni. Quando una nuova transazione raggiunge il nodo (tramite il software Wallet o un altro nodo), esso verifica che sia conforme a un insieme di regole (regole di consenso e regole di propagazione). Ad esempio:




- i bitcoin spesi devono esistere nel suo set UTXO (il database delle uscite non spese);
- la firma deve essere valida e tutte le condizioni di spesa devono essere soddisfatte (script valido);
- l'importo totale delle uscite non deve superare l'importo totale delle entrate, il che significa che i costi non possono essere negativi.



![Image](assets/fr/050.webp)



Dopo la convalida, la transazione viene memorizzata nel Mempool del nodo, uno spazio di memoria temporaneo riservato alle transazioni non confermate, e quindi trasmessa agli altri peer della rete a cui è collegato. Questo meccanismo di distribuzione e convalida continua da nodo a nodo. In questo modo, la transazione si propaga attraverso la rete Bitcoin e ogni nodo la memorizza nel Mempool fino a quando non viene inclusa in un blocco valido da un Miner, che agisce quindi sulla sua prima conferma.



### Controllare e distribuire i blocchi



Il terzo ruolo del nodo riguarda la gestione dei blocchi estratti. Quando un Miner scopre un nuovo blocco con un Proof of Work valido, lo trasmette in rete. I nodi lo ricevono, verificano che sia conforme a tutte le regole del protocollo e lo integrano nella propria copia locale del Blockchain se è valido. Come nel caso delle transazioni, i blocchi appena convalidati vengono trasmessi a tutti i peer connessi al nodo. Questo processo continua fino a quando tutti i nodi della rete Bitcoin sono a conoscenza del nuovo blocco.



![Image](assets/fr/051.webp)



## Qual è la differenza tra un arco e un Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



È essenziale distinguere tra due tipi di software distinti quando si utilizza il Bitcoin: il nodo e il Wallet.



Un nodo Bitcoin, come già detto, è un software che partecipa attivamente alla rete peer-to-peer. Svolge tre compiti principali:




- backup di Blockchain,
- convalida e trasmissione delle transazioni,
- convalida del blocco e relè.



Un Bitcoin Wallet, invece, è un software progettato per memorizzare e gestire le chiavi private. Queste chiavi consentono di spendere i bitcoin soddisfacendo gli script di blocco (in genere attraverso una firma). Un Wallet può connettersi a un nodo (locale o remoto) per consultare lo stato del Blockchain e trasmettere le transazioni che costruisce, ma non è, in quanto tale, un partecipante alla rete.



In alcuni casi, queste due funzioni coesistono all'interno dello stesso software, come nel caso del Bitcoin core, che funge sia da Full node che da Wallet. Tuttavia, molti dei programmi Wallet più diffusi (Sparrow, BlueWallet, ecc.) richiedono una connessione a un nodo esterno (proprio o di terzi) per trasmettere le transazioni e determinare il saldo del Wallet.



![Image](assets/fr/052.webp)



## Qual è la differenza tra un nodo e un Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Le nozioni di nodo e Miner sono spesso confuse. Eppure questi due Elements svolgono funzioni radicalmente diverse all'interno del sistema.



Inizialmente, quando Bitcoin fu lanciato da Satoshi Nakamoto nel 2009, ci si aspettava che ogni utente partecipasse alla rete nel suo complesso. Pertanto, il software originale Bitcoin combinava più funzioni contemporaneamente: fungeva da Wallet, un nodo, e anche da Miner, in grado di generare nuovi blocchi. All'epoca, la difficoltà del Mining era molto bassa. Bastava eseguire il software Bitcoin sul proprio computer per trovare blocchi e ricevere bitcoin come ricompensa.



Tuttavia, con la graduale diffusione del Bitcoin e l'aumento del numero di minatori, il panorama competitivo del Mining ha subito un cambiamento radicale. Oggi il Mining è diventato un'attività estremamente competitiva, dominata da operatori industriali dotati di infrastrutture specializzate. La potenza richiesta per estrarre un nuovo blocco è ora così grande che è praticamente impossibile per un singolo utente raggiungere questo obiettivo utilizzando solo un computer convenzionale. Di conseguenza, il Mining viene ora eseguito principalmente con macchine specializzate chiamate ASIC (*Application-Specific Integrated Circuits*). Questi chip sono ottimizzati esclusivamente per eseguire il doppio SHA-256, l'algoritmo utilizzato per Mining su Bitcoin.



![Image](assets/fr/053.webp)



A fronte di questa evoluzione, i ruoli del nodo Bitcoin e del Miner sono diventati chiaramente distinti. Come mostrato sopra, il ruolo di un nodo Bitcoin è puramente informativo e basato sulla convalida. Il ruolo del Miner è diverso:




- Seleziona le transazioni in sospeso nel Mempool.
- Costruisce un blocco candidato che integra queste transazioni.
- Cerca per tentativi un Proof of Work valido.
- Se trova una prova valida, trasmette il blocco attraverso il proprio nodo agli altri nodi.



Un Miner ha bisogno di un nodo Bitcoin per interagire con la rete.



Anche il ruolo del Miner è talvolta differenziato da quello del trinciatore. Un tritacarne è una macchina il cui compito è quello di Hash modellare i blocchi forniti dal server di un pool, cercando hash che soddisfino l'obiettivo di difficoltà definito per le azioni, e non quello del Bitcoin. Il resto del processo Mining , che comprende la costruzione dei blocchi veri e propri, la selezione delle transazioni o la ricerca Proof-of-Work in base alla difficoltà propria del Bitcoin, nonché la distribuzione, viene eseguito direttamente dai pool.



![Image](assets/fr/054.webp)



Infine, c'è un'importante differenza in termini di incentivo economico tra il Miner e il nodo. La gestione di un nodo Bitcoin non fornisce alcun beneficio monetario diretto. D'altro canto, partecipare al Mining comporta ricompense (sovvenzioni e commissioni di transazione) per ogni blocco trovato.



Nella seconda parte analizzeremo più in dettaglio i vantaggi pratici e personali dell'installazione e dell'utilizzo di un nodo Bitcoin, al di là di quelli puramente finanziari.



## Bitcoin core e implementazioni del protocollo


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Il protocollo Bitcoin non è un software: è un insieme di regole tacite condivise tra gli utenti della rete. Definisce le condizioni di validità delle transazioni, i meccanismi di creazione del denaro, il formato dei blocchi, le condizioni del Proof-of-Work e molte altre specifiche. Per interagire con questo protocollo, gli utenti devono eseguire un software che implementi queste regole: questo è noto come **implementazione** del Bitcoin.



Un'implementazione è quindi un software di nodo: un programma in grado di interfacciarsi con altre macchine della rete Bitcoin, di scaricare, verificare, memorizzare e propagare blocchi e transazioni e di applicare localmente le regole di consenso e di relè. Ogni implementazione è un'interpretazione concreta del protocollo, scritta in un determinato linguaggio di programmazione, con una propria architettura, prestazioni ed ergonomia. Ogni implementazione avrà anche una propria organizzazione di sviluppo, con una propria divisione delle responsabilità.



Tra queste implementazioni, una domina di gran lunga: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Un'implementazione storica che è diventata un punto di riferimento



Bitcoin core è il software di riferimento per il protocollo Bitcoin. È derivato dal codice originale scritto da Satoshi Nakamoto nel 2008-2009 e ne è la diretta continuazione. Inizialmente conosciuto come "*Bitcoin*", poi "*Bitcoin QT*" (a causa dell'aggiunta di un Interface grafico tramite la libreria Qt), è stato rinominato "*Bitcoin core*" nel 2014 per differenziare chiaramente il software dalla rete. Dalla versione 0.5, è stato distribuito con due componenti: `Bitcoin-qt` (il Interface grafico) e `bitcoind` (il Interface a riga di comando).



In teoria, Bitcoin core non rappresenta il protocollo Bitcoin; piuttosto, è solo un'implementazione tra le tante. Tuttavia, si distingue per la sua massiccia adozione, la sua età, la robustezza del suo codice e il rigore del suo processo di sviluppo. Di conseguenza, nella pratica, le regole applicate dal Bitcoin core sono di fatto quelle del protocollo Bitcoin: gli utenti, gli sviluppatori, i minatori e i servizi ecosistemici fanno riferimento quasi esclusivamente ad esso.



### Distribuzione attuale delle implementazioni



Secondo [i dati raccolti nell'agosto 2025 da Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (un noto sviluppatore dell'ecosistema), la distribuzione delle implementazioni tra i nodi pubblici della rete è la seguente:




- Bitcoin core**: 87.3% dei nodi
- Bitcoin Knots**: 12.5
- Altre implementazioni cumulative**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



In altre parole, circa 9 nodi pubblici su 10 utilizzano Bitcoin core. Il resto della rete si affida a client più marginali (anche se la quota di Knots è aumentata notevolmente negli ultimi mesi, non da ultimo in seguito ai dibattiti sul limite di dimensione del `OP_RETURN`). Queste implementazioni alternative sono spesso gestite da una sola persona o da un piccolo team.



**Nota: ** Queste cifre sono comunque stime, in quanto si basano principalmente sui *nodi in ascolto*, cioè sui nodi che accettano connessioni in entrata (con la porta 8333 aperta). I nodi non in ascolto* sono molto più complessi da contare, poiché è impossibile connettersi direttamente a loro: bisogna aspettare che l'iniziativa arrivi da loro, sotto forma di connessione in uscita. Il sito di Luke Dashjr sostiene di cercare di contare anche questi *nodi non in ascolto*, ma resta impossibile ottenere dati perfettamente precisi su di essi, e l'aggiornamento di queste statistiche è inevitabilmente in ritardo rispetto alla realtà.



### Funzionamento interno del Bitcoin core



Bitcoin core è scritto in C++. È anche un progetto open source che viene mantenuto da una comunità di sviluppatori volontari o pagati da varie entità (spesso da aziende dell'ecosistema che hanno un interesse personale nello sviluppo di Core). [Il codice è ospitato su GitHub](https://github.com/Bitcoin/Bitcoin) e lo sviluppo segue una procedura rigorosa:




- I contributori** presentano proposte sotto forma di _richieste di modifica_ (PR). In linea di principio, chiunque può proporre una modifica, ma questa deve essere testata, documentata e sottoposta a un processo di revisione paritaria.
- I **manutentori** hanno il diritto di approvare e unire le PR. Sono coloro che garantiscono la coerenza e la stabilità del progetto. Nel luglio 2025, ce ne sono cinque: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao e Ryan Ofsky.
- Dal febbraio 2023 non c'è più un **principal maintainer**. Questo ruolo è stato inizialmente ricoperto da Satoshi Nakamoto al momento del lancio di Bitcoin, poi da Gavin Andresen dopo la partenza di Nakamoto all'inizio del 2011 e infine da Wladimir J. Van Der Laan dal 2014 al 2023.



![Image](assets/fr/057.webp)



Lo sviluppo di Bitcoin core segue una logica meritocratica: i nuovi collaboratori sono incoraggiati a rivedere e testare il codice prima di proporre modifiche. Le decisioni si basano sul consenso tecnico e le modifiche più importanti (soprattutto nelle aree di consenso) richiedono discussioni a monte su canali pubblici, come le mailing list o i club di revisione delle PR.



### Altre implementazioni Bitcoin



Anche se marginali in termini di adozione, esistono altri client. Il principale è Bitcoin Knots, sviluppato da Luke Dashjr, un Fork di Bitcoin core che incorpora opzioni aggiuntive e un approccio più conservativo allo sviluppo. Queste includono restrizioni più severe sui formati delle transazioni.



![Image](assets/fr/058.webp)



Possiamo anche citare:




- Libbitcoin**: una libreria modulare in C++ sviluppata da Amir Taaki e mantenuta da Eric Voskuil;
- Bcoin**: un'implementazione in JavaScript, non più mantenuta attivamente;
- BTCD/btcsuit**e: un'implementazione in Go.



Questi progetti contribuiscono alla diversità dell'ecosistema, ma la loro adozione rimane molto limitata, rendendo difficile l'evoluzione indipendente del Bitcoin core.



### Il potere degli sviluppatori Core



Si potrebbe pensare che gli sviluppatori di Bitcoin core abbiano un controllo diretto su Bitcoin, ma non è così. Non possono imporre una modifica al protocollo. Il loro ruolo è quello di proporre il codice. Spetta a ciascun utente, tramite il proprio nodo, decidere se utilizzare o meno questo codice.



Ciò significa che se una modifica in Bitcoin core non incontra il consenso, può essere ignorata dai nodi, non aggiornando Bitcoin core o semplicemente cambiando l'implementazione. Al contrario, se una funzionalità desiderata dagli utenti viene bloccata nel processo di sviluppo del Core, è sempre possibile passare a un'altra implementazione o Fork al progetto.



Come discuteremo più avanti in questo corso, sono i nodi, in base al loro peso economico (cioè i commercianti), a conferire utilità a una versione del protocollo (e quindi alla valuta corrispondente), accettando unità che rispettano le sue regole. Il vero potere di governance del Bitcoin, quindi, spetta a questi commercianti, non agli sviluppatori.




# Diventare un bitcoiner sovrano


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Perché fare il proprio nodo?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



È opinione diffusa che gestire un nodo Bitcoin sia un atto puramente altruistico, senza alcun guadagno personale, al solo servizio della decentralizzazione della rete. Alcuni lo considerano una forma di dovere per i bitcoiners di sostenere il sistema e mostrare la loro gratitudine a Bitcoin.



Infatti, come abbiamo sottolineato nei capitoli precedenti, non c'è alcun guadagno economico diretto nel filare un nodo. Si potrebbe quindi pensare che non ci sia alcun interesse personale nel farlo. Eppure, gestire il proprio nodo porta molti vantaggi individuali. Per convincervi di ciò, in questo capitolo vi presenterò tutte le ragioni, sia tecniche che strategiche, per cui dovreste installare e utilizzare il vostro nodo Bitcoin.



### Diffusione più riservata delle transazioni



Quando il software Wallet si collega a un nodo esterno, trasmette le proprie transazioni a un'infrastruttura che non è sotto il vostro controllo. Questo genera ovvi rischi di sorveglianza: l'operatore del nodo remoto può analizzare i dettagli delle vostre transazioni, compresi gli importi e le frequenze, e, attraverso un controllo incrociato di alcuni metadati (come indirizzi IP, orari e luoghi), potenzialmente associarli alla vostra identità.



Infatti, come sottolineato nel capitolo precedente, i portafogli non comunicano con la rete Bitcoin per magia; devono connettersi a un nodo per consultare i saldi o trasmettere le transazioni. Se non avete mai creato un vostro nodo, ciò significa che il vostro Wallet dipende dall'infrastruttura di una terza parte (di solito l'azienda dietro al software). Questa terza parte, soprattutto se si tratta di un'azienda, può osservare, sfruttare o addirittura divulgare questi dati: per motivi commerciali, per vincoli legali o per pirateria.



![Image](assets/fr/059.webp)



Utilizzando il proprio nodo, si trasmettono le transazioni direttamente alla rete, evitando gli intermediari. A condizione che il vostro nodo sia protetto in modo adeguato (di cui parleremo più avanti) o che rispettiate determinati standard, nessuna informazione viene esposta: né il vostro IP Address né i dettagli delle vostre transazioni passano attraverso un'entità che non controllate. Questo è un prerequisito fondamentale per preservare la vostra riservatezza sul Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Operazioni non censurabili



Per le stesse ragioni menzionate in precedenza, il software Wallet basato su un nodo di terze parti è vulnerabile al rischio di censura: l'operatore del nodo remoto può rifiutarsi di trasmettere determinate transazioni per vari motivi. Potrebbe considerarle sospette o contrarie alla propria politica. La transazione può anche essere bloccata se non è conforme alle regole di trasmissione del nodo. Infine, l'operatore potrebbe prendere di mira specificamente il vostro IP Address per bloccare la trasmissione delle vostre transazioni.



Al contrario, utilizzando il proprio nodo, si garantisce la propagazione delle transazioni all'interno della rete peer-to-peer. Ciò significa che si mantiene il controllo totale sulla distribuzione delle transazioni, senza dipendere da un intermediario. Finché la transazione è conforme alle regole di consenso e di relè dei nodi collegati al vostro, sarà trasmessa sulla rete e poi, a condizione che siano incluse quote sufficienti, integrata in un blocco da un Miner. Avere un proprio nodo garantisce una conferma neutrale e senza permessi delle transazioni.



### Verifica indipendente dei dati



Senza un nodo personale, si rimane dipendenti da una terza parte per l'accesso alle informazioni, come il saldo Address, lo stato di conferma delle transazioni e la validità dei blocchi. Ciò implica una fiducia implicita nell'accuratezza e nell'integrità del nodo esterno.



![Image](assets/fr/060.webp)



L'utilizzo di un Full node consente di verificare personalmente tutte le regole del protocollo, per ogni transazione e per ogni blocco. Di conseguenza, il saldo visualizzato dal vostro Wallet non è un dato ricevuto da un server remoto, ma un risultato calcolato localmente da una copia completa del Blockchain, convalidato blocco per blocco. Questo approccio dà pieno significato alla massima dei bitcoiners:



> Non fidatevi, verificate.

### Migliore distribuzione della sicurezza del sistema



Ogni nodo che si unisce alla rete rafforza la ridondanza e la resilienza del Bitcoin. Facilita la diffusione delle informazioni e permette a nuovi peer di connettersi tra loro. Senza i nodi, il sistema sarebbe semplicemente inutilizzabile.



Come abbiamo visto, la sicurezza del Bitcoin non si basa sulla decentralizzazione, sul Mining o sulla crittografia: come ogni sistema, si basa sugli individui. Più precisamente, dipende dalla capacità degli operatori dei nodi di resistere alla coercizione.



Ciò che distingue i sistemi decentralizzati come Bitcoin è la distribuzione del rischio tra tutti coloro che sono coinvolti nel loro funzionamento. Gestire il proprio nodo Bitcoin significa accettare una parte di questo rischio garantendo la sicurezza della propria istanza; così facendo, si alleggerisce anche il peso del rischio per gli altri operatori del nodo.



Non si tratta quindi di un vantaggio personale diretto: la gestione di un nodo vi rende in parte responsabili della sicurezza della rete. È soprattutto un vantaggio collettivo, perché il vostro coinvolgimento contribuisce a diffondere il rischio. A sua volta, aumenta la propria capacità di utilizzare Bitcoin in modo affidabile.



### Approfondire la comprensione del sistema



L'installazione di un Full node non è un'operazione banale. Comporta l'installazione del software, la comprensione del funzionamento di base, il monitoraggio della sincronizzazione, l'esame dei log in caso di problemi e l'utilizzo del terminale. Questo vi porterà necessariamente ad approfondire la vostra conoscenza del protocollo. Questo è un vantaggio indiretto, ma non trascurabile.



L'acquisizione di queste conoscenze rafforza la fiducia nello strumento e può ridurre il rischio di errori o di esposizione a truffe. Anche fare il proprio nodo è una forma di apprendimento.



### Scegliere quali regole applicare



Un aspetto importante, spesso frainteso, è che la gestione di un nodo consente di scegliere le regole da applicare localmente. Esistono due tipi principali di regole:





- Regole di consenso**:



Queste sono le regole fondamentali del protocollo Bitcoin, che garantiscono l'integrità del sistema e stabiliscono i criteri di convalida delle transazioni e dei blocchi. Qualsiasi transazione non conforme a queste regole di consenso non potrà mai essere inclusa in un blocco valido. Ad esempio, una transazione con una firma non valida su una delle sue voci sarà sistematicamente esclusa.



Cambiare queste regole equivale a cambiare il protocollo, e quindi la moneta (Hard Fork). Tuttavia, anche senza cercare di modificarle, il semplice fatto di applicare rigorosamente le regole esistenti conferisce un certo potere: se un blocco viola le regole, il nodo lo rifiuta immediatamente.





- Regole della staffetta**:



Si tratta di regole specifiche per ogni nodo Bitcoin, che vengono aggiunte alle regole di consenso per definire la struttura delle transazioni non confermate accettate nel Mempool e trasmesse ai peer. Ogni nodo configura e applica queste regole a livello locale, il che spiega perché possono differire da un nodo all'altro. Esse si applicano solo alle transazioni non confermate: una transazione considerata "non standard" da un nodo sarà accettata solo se compare già in un blocco valido. La modifica di queste regole non esclude il nodo dal sistema Bitcoin.



Ad esempio, una transazione senza commissioni è, secondo le regole del consenso, perfettamente valida, ma sarà rifiutata per impostazione predefinita secondo la politica di relay Bitcoin core, perché il parametro `minRelayTxFee` è impostato a `0,00001` (in BTC/kB). Tuttavia, è possibile, sul proprio nodo, abbassare questa soglia per trasmettere transazioni con commissioni inferiori o, al contrario, aumentare il limite, ad esempio, a 2 Sats/vB, per evitare di trasmettere transazioni con commissioni basse.



Far girare il proprio nodo significa affermare che: "Convalido ciò che scelgo di convalidare, secondo le regole che io stesso ho adottato "*. Si diventa così attori della governance del sistema, in grado di rifiutare un'evoluzione che ci sembra inaccettabile o di approvare un aggiornamento secondo i propri criteri.



Possiamo quindi cercare di capire quanto potere avete sulle regole grazie al vostro nodo. L'entità di questo potere dipende dal tipo di regola.



#### Per le regole della staffetta



Per quanto riguarda le regole di trasmissione, l'essenziale è semplicemente possedere un nodo, indipendentemente dalla sua attività economica. La posta in gioco è l'accettazione o meno di trasmettere determinati tipi di transazioni.



Se, ad esempio, si ritiene che le transazioni con commissioni inferiori a 1 sat/vB debbano essere accettate sul Bitcoin, si può regolare questa regola sul proprio nodo in modo che trasmetta queste transazioni, facilitando così la loro propagazione sulla rete fino a quando un Miner non le includa in un blocco valido. In sostanza, quindi, si tratta di una questione di potere sulla diffusione delle transazioni: ogni nodo ha potere decisionale, poiché accettare di trasmettere un tipo di transazione equivale a promuoverne l'accettazione sulla rete Bitcoin. Di conseguenza, se si gestiscono più nodi, si ha una maggiore influenza sulla politica di rilancio, poiché ogni nodo ha le sue connessioni e le sue aree di impatto sulla rete.



Infatti, avere uno o più nodi configurati con specifiche regole di relay significa determinare quale parte della rete accetta di propagare un determinato tipo di transazione. La diffusione di un messaggio in un grafo peer-to-peer, come nel caso delle transazioni Bitcoin, segue la logica della teoria della percolazione. Immaginate ogni nodo come un sito che può essere attivo (`p` = trasmette) o inattivo (`1-p`). Non appena la proporzione `p` supera una soglia critica (`p_c`), emerge una componente gigante: la transazione riesce ad attraversare la rete e ha tutte le possibilità di raggiungere un Miner. In una rete come la Bitcoin, dove ogni nodo mantiene una media di 8 connessioni in uscita, la soglia `p_c` è generalmente fissata a pochi punti percentuali, ancora più bassa se alcuni nodi hanno un numero molto elevato di connessioni.



![Image](assets/fr/061.webp)



Finché `p` rimane al di sotto di `p_c`, una transazione resta confinata in sacche isolate e non raggiunge un Miner. Non appena questa soglia viene superata, la transazione si diffonde quasi istantaneamente in tutta la rete.



In ultima analisi, sono sempre i minatori a decidere se includere o meno una transazione in un blocco. Tuttavia, i nodi intervengono a monte influenzando la distribuzione delle transazioni: determinano se i minatori saranno o meno a conoscenza di una determinata transazione. Se una transazione non viene trasmessa ai minatori, è ovviamente impossibile per loro includerla in un blocco.



L'aggiunta di qualche altro nodo avrà quindi un impatto marginale se la rete è già in fase di percolazione per un determinato tipo di transazione, ma può rivelarsi decisiva quando la soglia di percolazione si avvicina. Possedere o influenzare diversi nodi, soprattutto se ben collegati, può aumentare o ridurre il valore di `p` e, di conseguenza, indirizzare indirettamente le regole di relay che determinano quali transazioni vengono viste e infine accettate dai minatori.



#### Per le regole di consenso



Per quanto riguarda l'influenza del vostro nodo sulle regole del consenso, sarà soprattutto il suo peso economico a essere decisivo. Si tratta di un concetto cruciale: il valore di qualsiasi moneta è direttamente correlato alla sua capacità di facilitare il Exchange. Infatti, se un oggetto non è accettato da nessuno nel Exchange per beni o servizi, non può essere accettato da nessuno. Infatti, se un oggetto non viene accettato da nessuno nel Exchange per beni o servizi, teoricamente non ha alcuna utilità monetaria. Ad esempio, se nessun commerciante accetta i sassolini come mezzo di pagamento, essi non hanno alcuna utilità come denaro. Naturalmente, l'utilità rimane una nozione soggettiva su scala individuale, ma in un dato territorio, maggiore è il numero di mercanti che accettano un oggetto come mezzo di pagamento nel Exchange, più è probabile che questo oggetto abbia un'utilità monetaria per le persone che vivono in questo territorio.



Prendiamo l'esempio di un villaggio in cui molti mercanti accettano oro in Exchange per le merci: è probabile che l'oro abbia un'utilità monetaria per gli abitanti del villaggio. Ciò indica che l'utilità di una moneta dipende direttamente dalle decisioni dei mercanti di accettarla o rifiutarla.



Questo concetto è fondamentale per capire le dinamiche di potere in gioco nel sistema Bitcoin. Il Satoshi lo dice chiaramente: il Bitcoin è un sistema di denaro elettronico; in altre parole, fornisce un servizio che offre una forma di valuta, il Bitcoin (o BTC). Quando le regole del protocollo vengono modificate in modo non retrocompatibile (Hard Fork), ciò equivale a creare un nuovo sistema e quindi una nuova valuta. Il successo o il fallimento di questo Fork dipende dalle dimensioni della sua economia, che a sua volta è determinata dal numero di commercianti che accettano questa nuova forma di valuta.



![Image](assets/fr/062.webp)



Facciamo un esempio: supponiamo che il Bitcoin subisca un Hard Fork. Ci sarebbero quindi 2 forme distinte di valuta: BTC-1 (la versione originale, invariata) e BTC-2 (la nuova valuta con regole di consenso diverse). Se tutti i commercianti che accettano BTC-1 continuano a farlo, ma rifiutano BTC-2, quest'ultimo avrà, in teoria, un'utilità monetaria molto limitata. Come utente, non avrei alcun interesse a conservare e utilizzare il BTC-2, sapendo che nessun commerciante lo vorrebbe nel Exchange per beni o servizi. Al contrario, se il 50% dei commercianti sceglie di accettare esclusivamente BTC-2 e il restante 50% accetta solo BTC-1, allora l'utilità di BTC-1 sarà, in teoria, dimezzata. Uso il termine "in teoria" perché l'utilità rimane soggettiva a livello individuale e dipende da una moltitudine di fattori (come il territorio e le abitudini di consumo) difficili da comprendere caso per caso.



Sul Bitcoin, il ruolo di "commerciante", inteso come qualsiasi entità con un certo peso economico, comprende ovviamente le imprese (negozi fisici, siti di vendita online, fornitori di servizi, ecc.), ma anche le piattaforme Exchange, poiché accettano il Bitcoin in Exchange per altre valute, e i minatori, poiché accettano il Bitcoin tramite commissioni in Exchange per il servizio di inclusione di una transazione in un blocco.



Per quanto riguarda le regole del consenso, il vostro nodo vi permette di indirizzare la vostra attività economica verso una valuta o un'altra. Ad esempio, se avete 10 nodi pieni a casa, ma nessuna attività economica significativa, la vostra influenza durante un Fork sarà quasi nulla. Al contrario, un singolo nodo utilizzato per gestire una catena di 200 negozi che accettano il Bitcoin conferisce un peso economico significativo.



Non è quindi il numero di nodi che conta, ma l'importanza dell'attività economica che essi supportano. Inoltre, se la vostra attività economica dipende da un nodo che non controllate, il suo proprietario deciderà quale valuta utilizzare, finché rimarrete connessi a quel nodo. Ecco perché gestire e utilizzare il proprio nodo è particolarmente importante nel contesto della governance del sistema:



> Non il vostro nodo, non le vostre regole.


## I diversi tipi di nodi Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Un nodo Bitcoin è, quindi, una macchina che esegue un'implementazione del protocollo Bitcoin. Dietro questa definizione comune di nodi, esistono diverse configurazioni possibili, non tutte in grado di offrire lo stesso livello di autonomia, consumo di risorse e utilità per la rete. In questo capitolo cercheremo di capire queste differenze per aiutarvi a scegliere un'architettura di nodi adatta all'uso e ai vincoli hardware.



### Il nodo completo



Un Full node è semplicemente un nodo Bitcoin che scarica l'intero Blockchain dal blocco Genesis, convalida ogni blocco in modo indipendente e memorizza la storia di tutto il Blockchain a livello locale. Questa è la forma "normale" di un nodo Bitcoin, come immaginato da Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Il Full node non ha bisogno di fidarsi di nessuno perché convalida e conosce tutte le informazioni del sistema. È il tipo di nodo che offre le maggiori garanzie: sa, senza affidarsi a terzi, se un pagamento è valido, se un blocco è valido, se una riorganizzazione è legittima e così via.



In pratica, un Full node richiede risorse non banali, tra cui diverse centinaia di gigabyte per i file a blocchi, un processore in grado di convalidare gli script, la RAM per il Mempool e le cache e una larghezza di banda stabile. La prima sincronizzazione (*IBD*) legge e verifica l'intera cronologia: è intensa, ma avviene una sola volta. Un Full node partecipa attivamente alla rete, trasmettendo blocchi e transazioni, e può accettare connessioni in entrata per assistere altri peer.



A seconda delle esigenze, è possibile aggiungere un indicizzatore al Full node. Il Bitcoin core offre l'indicizzazione delle transazioni come funzione opzionale (disattivata per impostazione predefinita), che può essere utile per scopi specifici. Tuttavia, non include un indicizzatore Address, che spesso è la funzione più richiesta dai singoli utenti. Per ovviare a questo problema, è possibile installare sul proprio nodo un software dedicato, come Electrs o Fulcrum, per velocizzare le interrogazioni di verifica del saldo Address da parte degli UTXO associati. Torneremo sul ruolo dell'indicizzatore in modo più dettagliato in un capitolo a parte.



### Il nodo pruned



Il nodo pruned convalida tutto come un Full node, dal blocco Genesis alla testa della catena con il maggior lavoro, ma **conserva solo la parte più recente dei file dei blocchi**. Una volta che i vecchi blocchi sono stati controllati, li cancella gradualmente per rimanere al di sotto di un limite di spazio impostabile. Questa configurazione è ideale se si hanno vincoli di spazio su disco: si mantiene l'indipendenza della convalida dei blocchi, senza memorizzare l'archivio storico completo di Blockchain. Questa opzione è particolarmente utile se si desidera semplicemente installare Bitcoin core sul proprio computer, senza utilizzare una macchina dedicata.



![Image](assets/fr/064.webp)



Le implicazioni tecniche di questa opzione sono abbastanza semplici: il nodo pruned è perfettamente in grado di trasmettere le transazioni, partecipare al relay, verificare blocchi e transazioni e tracciare la catena. D'altra parte, non può servire come fonte di dati storici oltre i suoi limiti per altre applicazioni (ad esempio, esploratori completi, indicizzatori, portafogli). Le funzioni che richiedono l'archivio (o un indice globale) non saranno quindi disponibili.



In pratica, è possibile utilizzare un nodo pruned per collegare un software di gestione Wallet come il Sparrow wallet. Tuttavia, non sarà possibile eseguire la scansione delle transazioni sul Wallet che sono precedenti al limite di potatura. Ad esempio, se si ha una transazione registrata nel blocco 901 458, ma il nodo conserva solo i blocchi da 905 402 in su (perché i più vecchi sono stati pruned), non sarà possibile eseguire la scansione di questa transazione. D'altra parte, se l'avete già scansionata quando il vostro nodo aveva ancora questa altezza di blocco, il vostro software di gestione Wallet memorizzerà le informazioni e visualizzerà correttamente il saldo degli UTXO corrispondenti.



In breve, il tracciamento Wallet funziona senza problemi su un nodo pruned se si crea un nuovo Wallet mentre il software è già collegato a quel nodo. D'altra parte, si possono incontrare difficoltà se si ripristina un vecchio Wallet, poiché le transazioni passate che non sono più conservate dal nodo non saranno ovviamente recuperabili.



### Il nodo luce / SPV



Un nodo SPV (*Simplified Payment Verification*), o nodo leggero, conserva solo le intestazioni dei blocchi, non i dettagli delle transazioni, e si affida ad altri nodi completi per ottenere la prova che una transazione si trova in un blocco (Merkle proofs via trees) di cui possiede l'intestazione. Il concetto di verifica semplificata dei pagamenti non è nuovo, essendo stato proposto dallo stesso Satoshi Nakamoto nella parte 8 del Libro Bianco.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



Questo tipo di nodo è ovviamente molto più leggero in termini di memoria e di utilizzo della CPU rispetto a un nodo Full node o addirittura a un nodo pruned. Il nodo SPV è quindi adatto ai dispositivi più piccoli e alle connessioni intermittenti. Infatti, viene spesso integrato direttamente nel Wallet, in particolare nel software mobile come l'App Blockstream.



Il compromesso è la fiducia e la riservatezza: un client SPV non controlla autonomamente gli script o le politiche di convalida; presume che la catena con il maggior numero di lavori sia valida e dipende da uno o più nodi completi per le risposte. L'utilizzo di questo tipo di nodo è quindi un'opzione migliore rispetto alla connessione a un nodo di terze parti; tuttavia, è ancora meno vantaggioso rispetto a un nodo Full node o addirittura pruned.



![Image](assets/fr/065.webp)



### Quale nodo per quale esigenza?





- Utente mobile / principiante



Per un utente alle prime armi con un semplice Wallet su un'applicazione mobile, l'uso di un nodo SPV è sicuramente il modo migliore per iniziare. L'installazione è rapida, richiede poche risorse e l'esperienza è semplice e fluida. Ciò significa che è possibile verificare da soli alcune informazioni e, quindi, fare meno affidamento sui nodi di terze parti e allo stesso tempo essere più indipendenti quando si tratta di trasmettere le transazioni.





- PC / utente intermedio



Un utente intermedio con un PC può installare un nodo pruned per beneficiare di quasi tutti i vantaggi di un Full node, senza sovraccaricare la propria macchina su base giornaliera: convalida completa, utilizzo moderato del disco e manutenzione semplice. È una soluzione ideale per collegare i portafogli desktop e rimanere indipendenti nella distribuzione delle transazioni, senza investire in una macchina dedicata o sovraccaricare lo spazio su disco.





- Bitcoiner sovrano / avanzato



Un Full node rimane la soluzione migliore se si vuole essere totalmente indipendenti nell'uso del Bitcoin e non limitarsi in seguito ad usi avanzati come un indicizzatore, un nodo Lightning o addirittura un Block explorer. Questo è esattamente ciò che esploreremo in questo corso!



## Panoramica delle soluzioni software


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Dal punto di vista del software, esistono due modi principali per gestire un nodo Bitcoin:




- installare direttamente un'implementazione del protocollo, come Bitcoin core (consigliato) o Bitcoin Knots,
- oppure utilizzare una distribuzione "chiavi in mano" (spesso chiamata "_node-in-a-box_") che integri un'implementazione di Bitcoin allo stesso modo, ma che includa anche un sistema di amministrazione di Interface, un archivio di applicazioni e strumenti pronti all'uso (Lightning, browser, index server, persino applicazioni self-hosting esterne a Bitcoin...).



Entrambi gli approcci portano allo stesso obiettivo: avere un proprio nodo, ma differiscono in termini di installazione e utilizzo di Interface, manutenzione, espandibilità e costi. Questo è l'aspetto che analizzeremo in questo capitolo.



### Implementazioni grezze del nodo Bitcoin



Installare un'implementazione grezza significa utilizzare direttamente il software di un'implementazione del protocollo Bitcoin (come Core), senza alcun software Layer aggiuntivo. L'utente gestisce autonomamente la configurazione, gli aggiornamenti e i servizi associati (indicizzazione, API, Lightning, backup, ecc.), in base alle proprie esigenze.



Questo è l'approccio più sovrano e flessibile: si sa esattamente cosa sta funzionando, dove si trovano i dati e come funziona tutto. D'altra parte, diventa più complesso quando si vuole andare oltre il semplice funzionamento di un nodo Bitcoin. Se l'obiettivo è solo quello di avere un nodo, la complessità è paragonabile a quella di un nodo in scatola, o anche meno, poiché si tratta semplicemente di installare un software.



#### Bitcoin core (cliente a maggioranza assoluta)



[Bitcoin core è il client ultra-maggioritario della rete](https://bitcoincore.org/). Scarica, convalida e mantiene il Blockchain, fornisce API RPC/REST e può integrare un Wallet. Se si preferiscono strumenti standard e ci si sente a proprio agio nell'aggiungere servizi (come il server Electrum, explorer e LND), è meglio usare Core così com'è.



**Vantaggi:** Massima stabilità, comportamento prevedibile, esperienza grezza, facile da installare e configurare.



**Svantaggi:** È necessario costruire manualmente il resto dello stack per creare un ambiente applicativo completo, piuttosto che un semplice nodo Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (cliente alternativo principale)



[Bitcoin Knots è un Fork di Bitcoin core](https://bitcoinknots.org/), mantenuto da Luke Dashjr. È il principale client alternativo a Core per l'implementazione del protocollo Bitcoin. Pienamente compatibile con il resto della rete (non è assolutamente un Hard Fork come Bitcoin Cash), offre tuttavia caratteristiche aggiuntive, tra cui opzioni di politica di relay assenti in Core o applicate in modo più rigoroso per impostazione predefinita per limitare ciò che alcuni considerano spam.



Ci sono due possibili ragioni per scegliere i nodi rispetto al nucleo:




- Tecniche**: Opzioni diverse da Core, in particolare in termini di gestione dei relè, determinando quali transazioni vengono accettate e trasmesse dal proprio nodo.
- Politica**: Alcune persone preferiscono usare client alternativi come Knots per ragioni non tecniche, in particolare per supportare un'alternativa a Core e quindi ridurre il suo monopolio. Se Core fosse mai compromesso, sarebbe utile non solo avere client alternativi solidi e ben mantenuti, ma anche sapere come utilizzarli efficacemente. Altri usano Knots per protesta, perché hanno perso fiducia negli sviluppatori di Core o disapprovano la maggior parte della gestione del client.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Personalmente, vi consiglio di scegliere Core, soprattutto per beneficiare più rapidamente delle patch di sicurezza. Infatti, alcune vulnerabilità scoperte in Knots vengono corrette con un certo ritardo. Più in generale, il processo di sviluppo di Core è solidamente strutturato e supportato da un gran numero di collaboratori, mentre Knots è mantenuto da una sola persona e ha una comunità molto più piccola. D'altra parte, le regole di relè tendono a perdere la loro utilità oggi, soprattutto quando sono applicate solo da una piccola frazione della rete (come per la teoria della percolazione).



### Distribuzioni Node-in-a-box



Il _node-in-a-box_ combina Bitcoin core (o Knots) con un sistema operativo preconfigurato, un Interface Web e un App Store di servizi di self-hosting (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, ecc.) Con un solo clic è possibile installare, aggiornare e interconnettere questi diversi moduli.



È una soluzione molto più semplice per l'avvio e la gestione di numerose applicazioni accessorie su base giornaliera. Il rovescio della medaglia è che quando si verifica un problema (ad esempio, un conflitto con l'immagine Docker, un aggiornamento errato, un database danneggiato), il debugging può diventare molto complesso, poiché si dipende dall'integrazione della distribuzione stessa. Inoltre, il supporto della comunità o ufficiale è spesso complicato.



Quindi, un node-in-a-box è estremamente facile da usare finché tutto funziona correttamente, ma in caso di bug bisogna essere pronti a fare lunghe ricerche, ad aspettare l'aiuto e a sporcarsi le mani.



La maggior parte di queste soluzioni è disponibile in due formati:




- Macchina preassemblata: un computer completo con il sistema operativo già installato. Queste macchine a pagamento devono semplicemente essere collegate alla rete elettrica e a Internet per essere operative. Se il vostro budget lo consente, questa opzione ha il vantaggio di essere molto semplice da configurare, di offrire spesso un'assistenza prioritaria e di contribuire al finanziamento dello sviluppo, dato che il modello di business di queste aziende si basa generalmente sulla vendita di hardware.
- Fai da te: installare il sistema operativo della distribuzione sulla propria macchina (vecchio PC, NUC, Raspberry Pi, server domestico...). Questa è la soluzione più economica, in quanto si può riciclare una vecchia macchina o scegliere un hardware che corrisponda esattamente alle proprie esigenze e al proprio budget. È anche l'opzione più flessibile e più soddisfacente da configurare. È questo l'approccio che esploreremo nella parte pratica del corso.



Ecco una panoramica delle principali soluzioni node-in-a-box disponibili (nel 2025):



### Umbrel (umbrelOS e Umbrel Home)



[Oggi Umbrel è il leader delle soluzioni node-in-a-box (https://umbrel.com/). Il suo successo è dovuto in gran parte alla semplicità di installazione (quando è stato lanciato su un semplice Raspberry Pi), al suo Interface elegante e intuitivo e a un ecosistema di applicazioni che è cresciuto rapidamente ed è ora estremamente esteso.



![Image](assets/fr/067.webp)



Lanciato nel 2020 come semplice nodo Bitcoin accompagnato da alcune applicazioni accessorie, Umbrel si è gradualmente evoluto in un cloud domestico moderno e completo.



Non entrerò nel dettaglio di come funziona e delle sue caratteristiche specifiche, perché le esamineremo in modo più approfondito nel primo capitolo della prossima parte. Infatti, per gli scopi di questo corso BTC 202, ho scelto di utilizzare UmbrelOS, che ritengo sia la migliore soluzione node-in-a-box attuale per gli utenti principianti e intermedi.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 offre StartOS (https://start9.com/), un sistema progettato per il "sovereign computing": l'obiettivo è che ognuno possieda e gestisca il proprio server privato, arricchito da un mercato di applicazioni self-hosted. È possibile acquistare un server Start9 (Server One a 619 dollari, Server Pure a 899 dollari) o assemblarlo in modalità DIY sulla propria macchina.



Sul lato Bitcoin, StartOS consente di installare un Full node, un nodo Lightning, un server BTCPay, Electrs e molti altri servizi. Tuttavia, il fascino di Start9 va oltre: offre la possibilità di scoprire, configurare ed esporre vari software (file cloud, messaggistica, monitoraggio) in modo unificato, con un controllo completo. Il progetto si rivolge quindi agli utenti che desiderano una solida piattaforma di self-hosting, non solo un semplice nodo Bitcoin. È probabilmente l'ecosistema più completo dopo Umbrel.



![Image](assets/fr/068.webp)



La differenza principale con Umbrel sta nel Interface. Umbrel si basa su un'interfaccia utente molto curata, mentre Start9 offre un Interface più semplice e funzionale. L'ecosistema di applicazioni di Start9 è meno ricco di quello di Umbrel, ma compensa con diversi vantaggi tecnici: l'accesso alle impostazioni avanzate delle applicazioni è semplificato, mentre Umbrel diventa rapidamente restrittivo se l'opzione desiderata non è fornita dal Interface. Start9 eccelle anche nella gestione dei backup: a parte l'efficiente soluzione di Umbrel per il LND, non esiste un meccanismo unificato, a differenza di Start9. Inoltre, offre strumenti di monitoraggio più accessibili e una connessione remota criptata (`https`), mentre l'accesso locale a Umbrel avviene tramite `http`.



In breve, se avete semplicemente bisogno delle applicazioni essenziali per Bitcoin, senza particolare interesse per il ricchissimo ecosistema di Umbrel, e se l'utente di Interface non è una priorità, allora Start9 è un'opzione migliore. Altrimenti, Umbrel è la scelta migliore.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MioNodo



[MyNode è una distribuzione focalizzata esclusivamente su Bitcoin e Lightning](https://mynodebtc.com/), che offre un Interface web, un marketplace di applicazioni e aggiornamenti con un solo clic. È possibile acquistare hardware pronto all'uso (*Modello Due* disponibile a 549 dollari) o installare MyNode gratuitamente sulla propria macchina. Il progetto offre anche una versione *premium* del software (94 dollari), che include supporto prioritario e funzioni avanzate.



![Image](assets/fr/069.webp)



In pratica, MyNode riunisce tutti gli elementi di base necessari per il funzionamento di un Full node, nonché le applicazioni essenziali per gli utenti del Bitcoin. Pertanto, è una soluzione adatta se non si richiedono applicazioni esterne all'ecosistema Bitcoin, come le applicazioni self-hosted presenti nei sistemi Start9 e Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz è un progetto 100% open source](https://docs.raspiblitz.org/) (licenza MIT) per montare un nodo Bitcoin e un nodo Lightning su un Raspberry Pi. È sufficiente scaricare l'immagine, avviarla e seguire la procedura guidata per avere un nodo funzionante sul proprio Raspberry Pi. I kit preassemblati sono disponibili anche presso terzi, di solito tra i 300 e i 400 dollari, a seconda dell'hardware. RaspiBlitz offre anche una serie di applicazioni aggiuntive, facili da installare.



![Image](assets/fr/070.webp)



Se possedete un Raspberry Pi, questa è un'opzione eccellente, poiché i sistemi più completi come Umbrel stanno diventando sempre più pesanti per questo tipo di mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo è un node-in-a-box incentrato sulla privacy](https://wiki.ronindojo.io/en/home) che automatizza la distribuzione di Samurai Dojo e Whirlpool, con un Interface dedicato e plugin specificamente progettati per l'ecosistema Samurai.



Il principio è semplice: se utilizzate Ashigaru Wallet (il successore Fork di Samurai Wallet, in seguito all'arresto dei suoi sviluppatori) o se volete beneficiare di strumenti avanzati per la privacy, RoninDojo fa per voi.



![Image](assets/fr/071.webp)



In precedenza il progetto offriva una macchina preconfigurata chiamata Tanto, ma attualmente non è disponibile. Potrebbe tornare in un secondo momento. Nel frattempo, è possibile installare facilmente RoninDojo su un Rock5B+ o Rockpro64, o anche indirettamente su un Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Un'altra soluzione [node-in-a-box è Nodl](https://www.nodl.eu/). Come per i progetti precedenti, è possibile acquistare l'hardware preconfigurato (tra 599 e 799 euro, a seconda del modello) o installarlo da soli in modalità fai-da-te.



Per quanto riguarda il software, Nodl integra Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, nonché BTC RPC Explorer, tutti con una catena di aggiornamento integrata e un codice open-source sotto licenza MIT.



![Image](assets/fr/072.webp)



Dopo aver esplorato le varie soluzioni software, è ora il momento di scegliere la macchina che ospiterà il nodo!




## Panoramica delle soluzioni hardware


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Dopo aver esplorato tutte le possibilità software, concentriamoci sull'hardware necessario per il nodo. Vi fornirò alcuni consigli concreti sulla scelta dei componenti, insieme a configurazioni adatte a diversi budget. Naturalmente, questa è la mia opinione personale e il mio feedback: ci sono sicuramente altre alternative rilevanti oltre a quelle presentate qui. Inoltre, non intendo rivisitare le macchine preassemblate offerte dai progetti node-in-a-box, che abbiamo già trattato nel capitolo precedente. Qui ci concentreremo esclusivamente sulle soluzioni fai-da-te.



### Avete davvero bisogno di una macchina dedicata?



Negli ultimi anni, i bitcoiners sono diventati sempre più consapevoli di un'idea sbagliata comune, in particolare con la diffusione dei nodi in scatola nei primi anni 2020: un nodo Bitcoin deve necessariamente funzionare su una macchina dedicata esclusivamente a questo scopo. Ma questo non è vero. Non serve necessariamente un computer dedicato per far funzionare un nodo Bitcoin: Bitcoin core è perfettamente in grado di funzionare sul PC di tutti i giorni. Se si dispone di spazio su disco sufficiente per Blockchain o si abilita il pruning, è possibile convalidare la catena, collegare il Wallet e persino chiudere il programma quando si è finito di usarlo. Il vantaggio di questo approccio è notevole: zero investimenti iniziali e minima complessità.



![Image](assets/fr/074.webp)



Detto questo, l'utilizzo di una macchina dedicata è spesso più comodo. Può funzionare ininterrottamente (24 ore su 24, 7 giorni su 7), essere accessibile da remoto in qualsiasi momento, non monopolizzare le risorse della macchina principale e, soprattutto, isolare gli utilizzi (una buona pratica di sicurezza: se il vostro PC personale ha un problema, il vostro nodo continua a funzionare e viceversa). Quindi la domanda non è "Ho bisogno di dedicare una macchina?", ma piuttosto "Ho bisogno di un nodo che sia costantemente online, accessibile da altri dispositivi e in grado di evolversi?" (Lightning, indicizzatori, applicazioni aggiuntive...). Se la risposta è sì, optare per una macchina separata renderà le cose molto più semplici.



### 3 metodi di acquisizione: riciclaggio, usato e nuovo



#### Riciclare un vecchio PC



È la soluzione più economica. La maggior parte di noi ha un vecchio PC che raccoglie Dust a casa, o presso amici e familiari: questa è l'occasione perfetta per rimetterlo in funzione! Per adattarlo all'uso come nodo Bitcoin, basta aggiungere un SSD da 2 TB e, a seconda delle esigenze, sostituire o aggiungere barre di RAM per aumentare la RAM. Per una macchina completamente funzionante è necessario sborsare tra i 100 e i 200 euro.



Prima di acquistare qualsiasi hardware, verificare il numero di slot per dischi disponibili, il tipo di connessione (M.2 o SATA), il formato della RAM (SODIMM o DIMM) e la sua generazione (DDR4, ecc.). Si dovrebbe anche cogliere l'occasione per pulire la macchina, in particolare la ventola, per garantire prestazioni ottimali.



Attenzione, però, se si utilizza un computer portatile: la batteria può diventare un problema con il passare del tempo (per saperne di più, si veda il capitolo successivo).



#### Ricondizionato o usato



Il mercato è pieno di mini-PC aziendali ricondizionati come *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* o *Dell OptiPlex Micro*. Queste macchine sono solide, compatte, silenziose ed efficienti dal punto di vista energetico. Il loro prezzo è ben al di sotto del nuovo ed è facile trovare modelli dotati di processori i5/i7 di 6a-10a generazione e di 8-16 GB di RAM, il tutto a prezzi molto interessanti, generalmente compresi tra 70 e 200 euro, a seconda della configurazione. A mio parere, questa è probabilmente l'opzione migliore se si cerca una macchina dedicata per il nodo Bitcoin.



![Image](assets/fr/075.webp)



È anche possibile trovare PC e portatili usati di qualche anno fa, con configurazioni interessanti e un ottimo rapporto qualità-prezzo.



**Nota: ** i computer delle flotte aziendali, come il *ThinkCentre Tiny*, sono spesso dotati solo di una porta *DisplayPort* (DP) per lo schermo, senza uscita HDMI. Non dimenticate quindi di portare con voi un adattatore o un cavo da DP a HDMI, se ne avete bisogno.



#### Acquisto del nuovo



Se il vostro budget lo consente, potete anche optare per una nuova macchina. Si tratta di una buona opzione se si vuole disporre di hardware recente con buone prestazioni, soprattutto se si intende utilizzare Umbrel o Start9 con applicazioni aggiuntive al di fuori dell'ecosistema Bitcoin per il self-hosting.



### Che tipo di macchina devo scegliere?



#### Mini-PC "NUC" / barebone



I mini-PC, a mio avviso, offrono il miglior compromesso per ospitare un nodo Bitcoin a casa. Sono poco ingombranti, si adattano facilmente a uno scaffale, consumano poca energia e si prestano a facili modifiche hardware, come l'aggiunta di RAM o la sostituzione dell'SSD.



Personalmente, preferisco i *Lenovo ThinkCentre Tiny*, molto diffusi sul mercato dell'usato (da flotte aziendali); sono particolarmente robusti e facili da modificare. Naturalmente esistono molti equivalenti di altri produttori: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*....



![Image](assets/fr/001.webp)



**Evidenze: ** ingombro ridotto, consumo energetico moderato, bassa rumorosità, scalabilità (a seconda del modello) e affidabilità.



**Punti deboli:** leggermente più costoso di un SBC tipo Raspberry Pi, assenza di schermo integrato (accesso remoto o tramite monitor esterno), assenza di batteria (spegnimento improvviso in caso di interruzione di corrente).



#### Computer portatile dedicato



È un'ottima alternativa a basso costo al mini-PC: oggi si possono trovare portatili usati o addirittura nuovi a prezzi bassi, dotati di processori decenti, numerose porte, nonché di schermo e tastiera integrati (molto pratici per la prima installazione). Soprattutto, la batteria funge da UPS naturale: in caso di interruzione di corrente, il nodo non si spegne bruscamente e può rimanere operativo anche per diverse ore.



![Image](assets/fr/076.webp)



**La batteria funge da UPS (nessun blackout), l'installazione è semplificata grazie al display e alla tastiera integrati, alla scheda Wi-Fi integrata e all'ampia scelta di mercati dell'usato e del nuovo (il che significa che spesso è possibile negoziare i prezzi).



**Punti deboli:** consumo di energia leggermente superiore a quello di un Mini-PC nudo, usura graduale della batteria in caso di funzionamento 24/7 con perdita di capacità, rischio raro ma reale di rigonfiamento della batteria o di fuga termica con l'età. È soprattutto questo aspetto che mi fa considerare il mini-PC un'opzione migliore del portatile: il graduale degrado della batteria e i rischi associati.



Se scegliete questa soluzione, vi consiglio di tenere sotto controllo le condizioni della batteria per evitare qualsiasi pericolo. Osservate il calore eccessivo, gli odori insoliti, l'instabilità o la deformazione dell'involucro. In caso di allarme, spegnere e scollegare immediatamente il computer, quindi smaltire la batteria presso un centro di riciclaggio specializzato.



**Suggerimento:** Se il BIOS/UEFI o lo strumento del produttore lo consentono, impostare un limite di carico (ad esempio, 60% o 80%) per prolungare la durata della batteria.



#### Raspberry Pi e altri SBC: un'idea sbagliata



All'inizio degli anni 2020, con l'ascesa del software node-in-a-box, è emersa anche la mania del Raspberry Pi come mezzo per far funzionare un nodo Bitcoin. L'idea sembrava attraente: economica, compatta e accessibile.



![Image](assets/fr/073.webp)



In pratica, se l'obiettivo è solo quello di eseguire un nodo Bitcoin senza applicazioni aggiuntive, un Raspberry Pi può essere sufficiente. Ma non appena si desidera utilizzare Umbrel, Start9 o un ecosistema più ricco (Block explorer, indicizzatore Address, nodo Lightning, applicazioni self-hosting...), la macchina raggiunge rapidamente i suoi limiti.



Il Raspberry Pi presenta una serie di svantaggi:




- processori troppo sottili, con un'architettura ARM che a volte è incompatibile con alcuni software o richiede una maggiore gestione;
- RAM saldata, impossibile da aggiornare, con configurazioni limitate (spesso un massimo di 8 GB);
- box esterni per SSD collegati via cavo, frequenti fonti di bug, che richiedono l'acquisto di una scheda specifica per un SSD stabile;
- tendenza a riscaldarsi rapidamente e difficoltà a garantire il corretto raffreddamento;
- necessità di acquistare hardware aggiuntivo (case, ventola, scheda SSD, ecc.);
- connettività molto limitata.



Storicamente, il grande vantaggio degli SBC come il Raspberry Pi era il loro prezzo: per poche decine di euro si poteva avere una macchina dedicata. Tuttavia, oggi i prezzi sono aumentati notevolmente e, una volta aggiunto tutto l'hardware aggiuntivo essenziale, il costo si avvicina a quello dei primi mini-PC x86 usati o ricondizionati che, a mio parere, offrono molti più vantaggi. Per questo motivo, non consiglio di optare per un SBC.



### Selezione dei componenti



#### Archiviazione su disco: SSD obbligatorio, minimo 2 TB



Tecnicamente, è possibile far funzionare un nodo Bitcoin su un HDD. Il problema è che tutto rallenterà notevolmente, soprattutto l'IBD, che diventerà estremamente lungo a causa dell'uso intensivo del disco come cache da parte di Bitcoin core (soprattutto per il set UTXO). Per questo motivo sconsiglio vivamente l'uso di un HDD: crea un vero e proprio collo di bottiglia, limita fortemente l'evoluzione futura (ad esempio, per un nodo Lightning) e può persino portare a un disallineamento della sincronizzazione con la testa Blockchain. Inoltre, lo stress costante sul disco meccanico aumenta il rischio di usura prematura.



Le unità SSD cambiano radicalmente l'esperienza dell'utente: tutto diventa più veloce e fluido, con un'affidabilità di gran lunga superiore. L'uso di un'unità SSD è quindi (quasi) obbligatorio per il vostro nodo e non ve ne pentirete, soprattutto perché i modelli ad alta capacità sono ora relativamente accessibili.



![Image](assets/fr/077.webp)



In termini di capacità, 2 TB si stanno gradualmente affermando come il nuovo minimo ragionevole. Nell'estate del 2025, Blockchain si sta già avvicinando ai 700 GB e se si aggiungono Umbrel, un indicizzatore Address e alcune applicazioni, un'unità SSD da 1 TB si saturerà rapidamente. Con 2 TB si ha un margine confortevole per gli anni a venire (in una stima di massima, tra i 5 e i 15 anni). Si può anche optare per 4 TB se si prevede di utilizzare molte applicazioni su Umbrel, di archiviare file di grandi dimensioni in self-hosting o se si desidera anticipare le esigenze di spazio su disco in larga misura.



![Image](assets/fr/078.webp)



Per quanto riguarda il formato, dipende dalle porte disponibili sulla vostra macchina; tuttavia, se possibile, vi consiglio di utilizzare un'unità SSD M.2 NVMe.



#### Memoria (RAM): da 8 a 16 GB



Per il solo Bitcoin core (senza sovrapposizione di Umbrel), le raccomandazioni degli sviluppatori indicano un minimo di 256 MB di RAM con le impostazioni regolate al minimo, 512 MB con le impostazioni predefinite e 1 GB per l'uso normale.



D'altra parte, se si utilizza un sistema node-in-a-box come Umbrel o Start9, i requisiti di RAM sono significativamente più elevati. Gli sviluppatori di Umbrel raccomandano un minimo di 4 GB di RAM. Questo potrebbe essere sufficiente per eseguire solo Core, ma presto sarete limitati. Pertanto raccomandano 8 GB, che considero il minimo per una configurazione di base intorno a Bitcoin (Core, LND, indexer e alcune applicazioni). Secondo la mia esperienza, con Umbrel e alcuni servizi aggiuntivi, 8 GB sono ancora un po' pochi. Per essere davvero tranquilli e avere un po' di margine, consiglierei 16 GB di RAM.



#### Processore (CPU)



Per un nodo Umbrel, il requisito minimo è un processore dual-core a 64 bit di Intel o AMD. Se si desidera utilizzare alcune applicazioni oltre a Bitcoin core, un quad-core (o superiore) farà la differenza in termini di fluidità. Ad esempio, i processori i5/i7 dalla sesta alla decima generazione sono ottime opzioni sul mercato dell'usato.



### Esempi di configurazioni concrete



Di seguito, propongo tre configurazioni concrete, adatte a diversi budget ed esigenze, con modelli precisi a supporto. Queste scelte sono fornite come esempi per illustrare le informazioni contenute in questo capitolo; non siete obbligati a scegliere esattamente questi modelli. Poiché ritengo che il Mini-PC sia l'opzione migliore a lungo termine, mi affiderò a questo formato per le tre configurazioni proposte.



*I prezzi indicati di seguito sono puramente indicativi e possono variare a seconda della regione, del fornitore e del periodo*



Innanzitutto, è necessario un SSD abbastanza grande da ospitare il Blockchain, pur lasciando spazio di manovra. Le unità SSD hanno una durata limitata in termini di cicli di scrittura e volume totale di dati scritti. Tuttavia, un nodo Bitcoin impone un carico significativo sul disco durante la scrittura. Per questo motivo non consiglio i modelli entry-level; suggerisco invece un'unità SSD NVMe, che offre prestazioni nettamente superiori.



A titolo di esempio, per gli scopi di questo corso, ho scelto il seguente modello: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, disponibile a circa 120 euro su Amazon. Potete anche optare per altri marchi noti come Crucial, Western Digital o Kingston.



![Image](assets/fr/046.webp)



#### Configurazione a basso budget



Ovviamente, se il vostro budget è molto limitato (sotto i 200 euro), vi consiglio di non investire in una macchina dedicata, ma di installare Bitcoin core direttamente sul vostro PC di tutti i giorni (in modalità pruned se avete poco spazio su disco).



Altrimenti, per un budget entry-level, consiglio il modello *HP EliteDesk 800 G2 Mini*. Ho trovato un modello ricondizionato a 96 euro su Amazon, dotato di un processore Intel Core i5 di sesta generazione e 8 GB di RAM. Si tratta di un'opzione particolarmente interessante per i principianti: questo processore e questa quantità di memoria sono più che sufficienti per eseguire Core su Umbrel, così come diverse applicazioni contemporaneamente, come un indicizzatore Electrs, un nodo Lightning e un'istanza Mempool, a patto di non allocare troppa cache a Core. Inoltre, questo tipo di mini-PC consente di aumentare facilmente la RAM a 16 GB, ad esempio, in caso di necessità (aspettatevi di pagare circa 30-40 euro in più per una o due chiavette di memoria di qualità).



![Image](assets/fr/045.webp)



Poi basta aggiungere l'SSD al budget. Partendo dal Samsung da 2 TB a 120 euro, otteniamo un costo totale di 216 euro per una macchina completa e funzionale.



#### Configurazione a medio budget



Se avete un budget medio di circa 300 euro per la macchina che ospiterà il vostro nodo, vi consiglio un *Lenovo ThinkCentre Tiny*, ad esempio, dotato di un processore ad alte prestazioni e di sufficiente RAM. Ho trovato un modello ricondizionato su Amazon a 180 euro, con un processore Intel Core i7 di sesta generazione e 16 GB di RAM. Con l'aggiunta dell'unità SSD da 2 TB a 120 euro, il costo totale è di 300 euro.



![Image](assets/fr/044.webp)



Con questa macchina, avete una configurazione confortevole: un IBD veloce e la possibilità di eseguire numerose applicazioni su Umbrel o Start9 senza difficoltà. È proprio questa la configurazione che sto utilizzando per il corso BTC 202.



#### Configurazione di fascia alta



Con un budget più elevato, le possibilità diventano molto più ampie. Si può scegliere una configurazione fai-da-te, oppure optare per una macchina preassemblata offerta direttamente da un progetto node-in-a-box.



Ad esempio, l'*ASUS NUC 14 Pro* è disponibile nuovo su Amazon a 540 euro. A questo prezzo si ottiene un processore Intel Core Ultra 5 (recente e particolarmente performante), accompagnato da 16 GB di RAM DDR5. Con una tale configurazione, sarete in grado di completare un IBD in tempi record e di installare applicazioni impegnative senza difficoltà.



Si tratta di una configurazione estremamente comoda, persino eccessiva se l'obiettivo iniziale è semplicemente quello di far funzionare un nodo Bitcoin. D'altra parte, se volete sfruttare appieno tutte le applicazioni self-hosting disponibili su Umbrel e Start9, questo livello di potenza fa al caso vostro.



![Image](assets/fr/043.webp)



A seconda dell'uso che si intende fare, si può optare per un'unità SSD da 2 TB, come nelle altre configurazioni, oppure direttamente per un'unità SSD da 4 TB a 260 euro se si desidera archiviare anche file personali e ampliare l'uso del self-hosting. Con un'unità SSD da 2 TB, il costo totale della configurazione è di 660 euro, mentre con un'unità SSD da 4 TB raggiunge gli 800 euro.



### Qualche altro consiglio





- Se vuoi acquistare attrezzature di seconda mano e pagare in bitcoin, vieni a un meetup vicino a te! Chiacchierando con gli altri partecipanti, troverete sicuramente l'attrezzatura adatta a un buon prezzo, contribuendo al contempo a mantenere viva l'economia circolare intorno al Bitcoin. È anche un'opportunità per beneficiare dei consigli della comunità.





- Per la connessione a Internet è ovviamente necessario un cavo Ethernet RJ45, almeno per l'installazione del sistema.





- Alcuni ambienti, come Umbrel, consentono di utilizzare il Wi-Fi, ma le prestazioni saranno generalmente inferiori (soprattutto se si desidera utilizzare il nodo Lightning da remoto, in quanto ciò può avere un impatto). Se si sceglie il Wi-Fi, assicurarsi che la macchina abbia una scheda integrata o aggiungere un dongle compatibile.





- Utilizzare sempre l'alimentatore Supply originale del produttore per la macchina. Questo è fondamentale per evitare danni all'apparecchiatura e per prevenire il rischio di incendi.





- Se la macchina non dispone di una batteria integrata, è bene investire in un inverter per evitare spegnimenti improvvisi.





- A seconda del valore delle apparecchiature e della posizione geografica, può essere opportuno installare un sistema di protezione contro i fulmini, direttamente sul quadro elettrico o sulla ciabatta utilizzata.





- Infine, ricordate di ottimizzare il raffreddamento della macchina: pulitela regolarmente e installatela in un luogo fresco, ben ventilato e non ingombro per evitare il surriscaldamento, che potrebbe portare al throttling (limitazione volontaria della velocità del processore).



# Installazione semplice di un nodo Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: molto più di un nodo Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel è un sistema operativo per server personali progettato per rendere accessibile il self-hosting: si installa Umbrel, si apre un browser su `umbrel.local` e si gestisce tutto tramite un semplice Interface remoto.



Il progetto ha dapprima reso popolare l'idea di un nodo Bitcoin e Lightning con un solo clic, per poi espandersi in una vera e propria "nuvola domestica": archiviazione di file e foto, streaming multimediale, strumenti di rete, automazione domestica, intelligenza artificiale locale e centinaia di app installabili da un App Store integrato.



In Umbrel, ogni applicazione viene eseguita in un contenitore Docker (isolamento, aggiornamenti atomici, avvio/arresto indipendente). Il Interface centralizza l'accesso a tutte queste applicazioni, offrendo single sign-on (con 2FA opzionale), aggiornamenti one-click per il sistema operativo e le applicazioni, monitoraggio in tempo reale della macchina (CPU, RAM, temperatura, storage), gestione dei permessi tra le applicazioni e una panoramica del loro consumo.



L'obiettivo di Umbrel è quindi quello di restituire all'utente il controllo e la riservatezza dei propri dati, senza affidarsi a servizi cloud, al di là della semplice gestione di un nodo Bitcoin.



### Umbrel Home vs umbrelOS



Umbrel offre due approcci distinti:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): è un mini-server pronto all'uso, appositamente progettato e ottimizzato per umbrelOS. Compatto, silenzioso, collegato a Ethernet, è dotato di un SSD NVMe (fino a 4TB opzionali), 16GB di RAM e una CPU quad-core. Lo si ordina, lo si collega e si va su `umbrel.local`. È possibile avere un Umbrel operativo e funzionante in pochi minuti. Questa è l'opzione plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): è il sistema operativo che potete installare voi stessi sul vostro hardware (mini-PC, NUC, tower, laptop dedicato...). Si dispone dello stesso Interface e dello stesso App Store di Umbrel Home.



![Image](assets/fr/080.webp)



In entrambi i casi, l'esperienza dell'utente è identica dal punto di vista del software: amministrazione basata su browser, aggiornamenti con un solo clic, installazione di applicazioni su richiesta... La soluzione fai da te è spesso più economica dell'acquisto di Umbrel Home (a seconda della macchina utilizzata). Tuttavia, non consiglierei necessariamente di optare sempre per l'opzione fai-da-te, poiché **l'acquisto di Umbrel Home contribuisce direttamente a finanziare lo sviluppo del progetto**, dato che il suo modello commerciale si basa sulla vendita di hardware. E francamente, a 389 euro per 2 TB di spazio di archiviazione, il prezzo rimane molto ragionevole vista la qualità della macchina offerta.



![Image](assets/fr/079.webp)



Nel prossimo capitolo vedremo come installare umbrelOS DIY sulla propria macchina. Tuttavia, potete seguire questo corso BTC 202 allo stesso modo se avete optato per una Umbrel Home.



### Caso d'uso: dal nodo Bitcoin al cloud domestico



Umbrel può rimanere molto minimalista e focalizzato esclusivamente sul Bitcoin, oppure evolversi in un vero e proprio server personale multifunzionale, a seconda delle vostre esigenze. Ecco i principali utilizzi di Umbrel:





- Semplice nodo Bitcoin**: questo è l'uso principale su cui Umbrel ha fatto affidamento fin dall'inizio. È possibile eseguire Bitcoin core (o Knots), collegare i portafogli direttamente al nodo, esporre un server Electrum, ospitare il Mempool Block explorer per visualizzare il Blockchain e stimare le spese... È su questi usi che ci concentreremo in questo corso.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel consente inoltre di implementare LND o Core Lightning, due implementazioni di Lightning Network, per gestire il proprio nodo Lightning. Potrete aprire canali, gestire la liquidità, effettuare pagamenti, automatizzare il bilanciamento, offrire servizi, collegare un Wallet remoto o sfruttare la gestione avanzata del Interface grazie alle numerose applicazioni disponibili. Analizzeremo questo caso specifico nel prossimo corso LNP 202.



![Image](assets/fr/083.webp)





- Self-hosting generale**: con Nextcloud, Immich, Jellyfin/Plex, blocco degli annunci a livello di DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), domotica (Home Assistant), backup, gestione delle note, strumenti per l'ufficio, AI locale (Ollama + Open WebUI)... Umbrel può diventare il vostro server personale, permettendovi di riprendere il controllo dei vostri dati. Ospitate voi stessi i servizi che utilizzate quotidianamente, con un'esperienza utente raffinata che ricorda da vicino le soluzioni esterne, mantenendo il controllo totale sui vostri dati e sulla vostra privacy.



Distribuendo le applicazioni in contenitori, potete modellare Umbrel come volete: iniziate con un semplice nodo Bitcoin e alcune applicazioni legate al suo ecosistema, poi installate un nodo Lightning accanto al nodo Bitcoin e arricchite gradualmente la vostra istanza con le applicazioni self-hosting di cui avete bisogno.



### Comunità e aiuto reciproco



Uno dei vantaggi principali di Umbrel rispetto ai suoi concorrenti è la sua vasta e attivissima comunità di utenti. È possibile raggiungerli principalmente tramite [il loro Discord](https://discord.gg/efNtFzqtdx) e [il loro forum online](https://community.umbrel.com/). Qui troverete non solo consigli pratici, ma soprattutto soluzioni per risolvere i problemi o risolvere i bug. È un ottimo punto di partenza, per progredire e, infine, per aiutare gli altri utenti, in modo da non essere lasciati soli con il vostro Coin.



![Image](assets/fr/084.webp)



### Licenza UmbrelOS



Il codice di Umbrel è pubblicamente disponibile (è possibile visualizzarlo, Fork e modificarlo), ma non è sotto una vera licenza open-source. Infatti, umbrelOS è distribuito sotto la licenza [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), sebbene alcuni strumenti di sviluppo associati siano disponibili sotto la licenza MIT.



In pratica, potete fare praticamente tutto quello che volete con umbrelOS, purché sia per uso personale e non commerciale: modifiche, ridistribuzione per scopi non di lucro, creazione di derivati per voi stessi o per organizzazioni non di lucro, purché rispettiate le note legali.



Tuttavia, è vietato vendere Umbrel o i suoi derivati (ad esempio, una macchina preassemblata con umbrelOS preinstallato), offrire servizi legati a Umbrel a scopo commerciale o integrare il suo codice in un prodotto a scopo di lucro.



Tecnicamente, questa licenza non limita l'installazione, la verifica o l'adattamento di Umbrel per uso personale. Dal punto di vista legale, protegge il progetto dalla rivendita non autorizzata o dall'hosting commerciale, in particolare da parte dei fornitori di cloud. Umbrel non è quindi open source, anche se il suo codice rimane pubblicamente accessibile.



Tuttavia, ogni applicazione dello Store mantiene la propria licenza, spesso open source.




## Installazione di un Full node con ombrello


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Ora che abbiamo tutte le informazioni necessarie, è il momento di entrare nei dettagli. In questa guida vi mostreremo come installare un nodo Bitcoin completo utilizzando UmbrelOS.



### Materiali necessari



In questo caso, utilizzeremo l'immagine UmbrelOS x86 (più precisamente, la versione x86_64). Potrete seguire questa guida su qualsiasi macchina scegliate, purché non sia dotata di un processore con architettura ARM (niente Apple Silicon, Raspberry Pi, ecc.). Ciò significa che qualsiasi computer con processore Intel o AMD a 64 bit sarà sufficiente, purché soddisfi i requisiti minimi, a seconda di come intendete utilizzare Umbrel (si consiglia almeno un processore dual-core).



Se si è optato per un Raspberry Pi 5 (opzione che non consiglio, come indicato nella sezione precedente), l'installazione è leggermente diversa. Potete quindi seguire questo tutorial dedicato e tornare al mio corso una volta sul sito web Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Come accennato nella sezione precedente, ho scelto di eseguire questa esercitazione su un piccolo PC ricondizionato che ho trovato a un buon prezzo: un *Lenovo ThinkCentre M900 Tiny* dotato di un processore Intel Core i7 e 16 GB di RAM. È una configurazione molto comoda per l'esecuzione di Umbrel, soprattutto per un nodo Bitcoin. Tuttavia, ho scelto questa configurazione perché voglio installare un nodo Lightning e altre applicazioni più impegnative in seguito. Ho anche aggiunto un SSD da 2 TB al mio ThinkCentre per mantenere l'intero Blockchain e avere ancora un margine confortevole. Con questa configurazione, il costo totale è di 270 euro, comprensivo di tutte le spese.



![Image](assets/fr/001.webp)



Sono particolarmente appassionato della gamma ThinkCentre Tiny di Lenovo, in quanto si tratta di macchine compatte, silenziose e molto robuste. Questi computer sono molto popolari tra le aziende e quindi abbondano sul mercato dell'usato, dove si possono trovare configurazioni interessanti tra i 70 e i 200 euro.



Se, come me, avete scelto un PC senza monitor, **dovrete collegare un monitor e una tastiera** solo per la durata dell'installazione. In seguito, potrete accedervi in remoto da un altro computer della stessa rete (o con altri metodi che tratteremo nei capitoli successivi). È inoltre necessario un cavo Ethernet RJ45 per collegare la macchina alla rete locale e una chiave USB di almeno 4 GB per memorizzare l'immagine di installazione.



Per ricapitolare, ecco i requisiti dell'attrezzatura:




- Computer con processore x86_64 (minimo Dual-core, consigliato Quad-core);
- Memoria RAM (4 GB minimo, 8 GB consigliati o più per un uso prolungato);
- SSD (consigliato + 2 TB);
- Chiave USB (+ 4 GB) per l'installazione dell'immagine di UmbrelOS;
- Monitor e tastiera (utile solo per l'installazione iniziale se il PC non ne è dotato);
- Cavo Ethernet RJ45.



### Fase 1 - Montaggio del computer



A seconda dell'hardware scelto, il primo passo consiste nell'assemblare i vari componenti del computer. Ad esempio, nel mio caso, l'unità SSD originale aveva una capacità di soli 256 GB, quindi la riciclerò per un altro uso e la sostituirò con un'unità SSD da 2 TB. Se volete sostituire anche i moduli RAM, è il momento di farlo.



### Fase 2: preparazione di una chiave USB avviabile



Prima di installare UmbrelOS sulla vostra macchina, dovrete creare una chiave USB avviabile contenente il sistema operativo. Tutti i passaggi del punto 2 devono essere eseguiti sul vostro computer personale (e non direttamente sul computer destinato a diventare il vostro nodo).





- Iniziare scaricando l'ultima versione di UmbrelOS in formato USB:



Andate su [il sito ufficiale di Umbrel per scaricare l'immagine ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) per l'installazione tramite chiave USB. Assicurarsi di selezionare la versione compatibile con l'architettura x86_64 (file denominato `umbrelos-amd64-usb-installer.iso`). Il download può richiedere un po' di tempo, poiché l'immagine è piuttosto grande.



![Image](assets/fr/002.webp)





- Installare l'Etcher Balena:



Per creare la chiavetta USB avviabile, utilizzerete un semplice strumento multipiattaforma chiamato [Balena Etcher](https://www.balena.io/etcher/). Scaricatelo e installatelo sul vostro computer.



![Image](assets/fr/003.webp)





- Inserire una chiave USB vuota di almeno 4 GB:



Inserite una chiavetta USB nel computer (quella su cui avete appena scaricato l'immagine di UmbrelOS e Balena Etcher). **Attenzione: tutti i dati contenuti nella chiavetta saranno cancellati**. Assicuratevi che non contenga file importanti.





- Masterizzare l'immagine ISO sulla chiavetta USB con Balena Etcher:



Avviare Balena Etcher e selezionare il file ISO `umbrelos-amd64-usb-installer.iso` appena scaricato facendo clic sul pulsante "*Flash da file*". Quindi, selezionare la chiave USB come dispositivo di destinazione e fare clic su "*Flash!*" per iniziare la scrittura.



![Image](assets/fr/004.webp)



Una volta completata l'operazione, avrete una chiavetta USB avviabile contenente UmbrelOS, pronta per l'avvio e l'installazione di Umbrel sulla vostra macchina.



![Image](assets/fr/005.webp)



### Fase 3: avvio del computer dalla chiave USB



Ora che la chiavetta USB avviabile contenente UmbrelOS è pronta, è possibile avviare il computer su di essa per iniziare l'installazione del sistema. Scollegare la chiavetta USB dal computer principale e inserirla nel dispositivo su cui si desidera installare Umbrel e il nodo Bitcoin.



Come spiegato all'inizio di questo capitolo, per completare l'installazione sono necessari un dispositivo di visualizzazione e un dispositivo di input. Collegate uno schermo tramite HDMI (o un'altra porta, a seconda del vostro PC) e una tastiera tramite USB alla vostra macchina. Questi dispositivi sono necessari solo per l'installazione; in seguito non saranno più necessari, poiché Umbrel sarà accessibile in remoto da un altro computer. Collegare questi due dispositivi al PC.



**Suggerimento:** Se non si dispone di uno schermo periferico a casa, è possibile utilizzare il televisore. Grazie all'ingresso HDMI (o di altro tipo), può essere utilizzato come schermo temporaneo mentre si installa il sistema operativo.



Umbrel richiede ovviamente una connessione a Internet. Collegare il cavo Ethernet RJ45 tra il dispositivo e il router.



![Image](assets/fr/006.webp)



Accendere il computer. Nella maggior parte dei casi, dovrebbe rilevare automaticamente la chiave USB e avviarla. Verrà quindi visualizzata la schermata di installazione di UmbrelOS Interface.



Se il dispositivo si avvia su un altro sistema o visualizza un messaggio di errore, probabilmente significa che non si sta avviando automaticamente dalla chiave USB. In questo caso, riavviare e accedere alle impostazioni del BIOS/UEFI (di solito si accede premendo `DEL`, `F2`, `F12` o `ESC`, a seconda del produttore del computer). Quindi, modificare l'ordine di avvio per dare priorità alla chiave USB. Quindi riavviare il dispositivo per avviare UmbrelOS.



### Passo 4: Installare UmbrelOS sul computer



Una volta avviato il dispositivo dalla chiavetta USB, si aprirà l'installazione di Interface UmbrelOS. Questo passaggio prevede l'installazione del sistema direttamente sul disco interno del Hard.



La schermata visualizzata elenca tutti i dispositivi di archiviazione interna rilevati dal computer. Ogni disco è accompagnato da un numero, un nome e una capacità di memoria. Individuare il disco su cui si desidera installare Umbrel. **Attenzione: tutti i file presenti su questo disco verranno eliminati in modo permanente



![Image](assets/fr/007.webp)



Una volta individuato il disco corretto (di solito quello con la capacità maggiore, per ospitare il Blockchain), prendere nota del numero assegnatogli. Ad esempio, se il disco scelto appare sotto il numero `2`, è sufficiente immettere `2`, quindi premere il tasto `Enter` sulla tastiera.



![Image](assets/fr/008.webp)



Il programma formatta il disco selezionato, installa UmbrelOS e configura automaticamente il sistema. Questa operazione potrebbe richiedere alcuni minuti. Lasciare che il processo si svolga senza interruzioni.



![Image](assets/fr/009.webp)



Al termine dell'installazione, verrà richiesto di spegnere il dispositivo. Premere un tasto qualsiasi per spegnere il computer.



![Image](assets/fr/010.webp)



Ora è possibile rimuovere la chiave USB, la tastiera e lo schermo, che non sono più necessari per Umbrel. Tutto ciò che rimane del nodo è il Supply di alimentazione e il cavo Ethernet RJ45.



![Image](assets/fr/011.webp)



Prima di riavviare il dispositivo, verificare i due punti seguenti:





- La chiave USB è scollegata**: se rimane collegata, il sistema potrebbe riavviarsi su di essa anziché sul disco interno;
- Il cavo Ethernet è collegato**: per funzionare, il dispositivo deve essere collegato al router.



Premere il pulsante di accensione. Il sistema si avvia automaticamente dal disco interno in cui è stato installato UmbrelOS. Il primo avvio può richiedere circa **5 minuti**. Durante questo periodo, Umbrel inizializza i suoi servizi e il Interface.



Da un altro computer (il PC di tutti i giorni) collegato alla **stessa rete locale**, aprire un browser web (Firefox, Chrome...) e andare su:



```
http://umbrel.local
```



Questo Address viene utilizzato per accedere all'utente grafico Interface Umbrel da remoto e iniziare la configurazione.



Se il sito Address `http://umbrel.local` non funziona sul vostro browser dopo aver atteso almeno 5 minuti, provate semplicemente:



```
http://umbrel
```



Se ancora non funziona, inserire l'IP locale di Umbrel Address direttamente nel browser. Ad esempio (sostituire `42` con il numero della macchina che ospita Umbrel sulla rete locale):



```
http://192.168.1.42
```



Per identificare l'IP Address di Umbrel, esistono diversi metodi, dai più semplici ai più avanzati:





- Accedere all'amministrazione del router Interface e trovare l'IP Address del dispositivo Umbrel sulla rete locale.





- Utilizzare un software di scansione di rete come Angry IP Scanner per rilevare i dispositivi collegati e individuare l'IP Address di Umbrel.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Come ultima risorsa, ricollegare un monitor e una tastiera al dispositivo, effettuare il login (login predefinito: `umbrel`, password: `umbrel`), quindi digitare il seguente comando:



```
hostname -I
```



Ora siete pronti a usare Umbrel!



### Passo 5: Iniziare con Umbrel



Per iniziare a configurare Umbrel, fare clic sul pulsante "*Avvio*".



![Image](assets/fr/013.webp)



#### Creare un account



Scegliete uno pseudonimo o inserite il vostro nome, quindi impostate una password forte. Attenzione: questa password è l'unica barriera che protegge l'accesso al vostro Umbrel dalla vostra rete (e quindi, potenzialmente, ai vostri bitcoin se gestite un nodo Lightning su Umbrel). Protegge anche l'accesso remoto tramite Tor o VPN, se questi servizi sono abilitati.



Scegliete una password forte e assicuratevi di conservarne almeno una di backup (si consiglia un gestore di password).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Una volta inserita la password, fare clic sul pulsante "*Crea*".



![Image](assets/fr/014.webp)



La configurazione di Umbrel è ora completa.



![Image](assets/fr/015.webp)



#### Scoperta del Interface



Il Interface di Umbrel è piuttosto intuitivo:





- Nella pagina iniziale è possibile visualizzare le applicazioni e i widget installati.



![Image](assets/fr/016.webp)





- L'"*App Store*" consente di installare nuove applicazioni,



![Image](assets/fr/017.webp)





- Il menu "*Files*" centralizza tutti i documenti memorizzati su Umbrel.



![Image](assets/fr/018.webp)





- Il menu "*Impostazioni*" consente di modificare le impostazioni dell'Umbrel e di accedere alle sue informazioni, tra cui:
    - Aggiornare, riavviare o arrestare il computer;
    - Consultare lo spazio di memoria disponibile, l'utilizzo della RAM e la temperatura del processore;
    - Cambiare lo sfondo;
    - Gestione dell'accesso remoto tramite Tor, attivazione del Wi-Fi o 2FA.



![Image](assets/fr/019.webp)



#### Impostazioni di sicurezza e di connessione



Innanzitutto, consiglio vivamente di attivare l'autenticazione a due fattori (2FA). Questo aggiunge un ulteriore Layer di sicurezza alla vostra password. È quasi indispensabile se si intende utilizzare Umbrel per archiviare file personali, eseguire un nodo Lightning o svolgere qualsiasi altra attività sensibile.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

A tal fine, fare clic sulla casella corrispondente nelle impostazioni.



![Image](assets/fr/020.webp)



Eseguire la scansione del codice QR visualizzato utilizzando la propria applicazione di autenticazione. Immettere quindi il codice dinamico a 6 cifre nell'apposito campo dell'Umbrel.



D'ora in poi, ogni nuova connessione al vostro Umbrel richiederà sia la password che il codice a 6 cifre generato dalla vostra applicazione di autenticazione a due fattori (2FA).



![Image](assets/fr/021.webp)



Per quanto riguarda l'accesso remoto via Tor, se non ne avete bisogno, vi consiglio di lasciare questa opzione disattivata per limitare la superficie di attacco di Umbrel. Per impostazione predefinita, è possibile accedere al nodo solo da una macchina connessa alla stessa rete locale. L'abilitazione dell'accesso via Tor vi permetterà comunque di gestire il vostro Umbrel in mobilità.



Se si attiva questa funzione, in teoria è possibile per qualsiasi macchina al mondo tentare una connessione al vostro nodo, a condizione che conosca il Tor Address. Tuttavia, la password e la 2FA continueranno a proteggervi.



Se si attiva questa opzione, assicurarsi di aver attivato l'autenticazione a due fattori (2FA), di avere una password forte e di non rivelare mai la propria connessione Tor Address.



È sufficiente inserire questo Tor Address nel browser Tor per accedere al Interface di Umbrel da qualsiasi rete.



![Image](assets/fr/026.webp)



Infine, in questa pagina di impostazioni è possibile attivare la connessione Wi-Fi. Se la macchina che ospita Umbrel dispone di una scheda di rete Wi-Fi o di un dongle Wi-Fi, ciò consente di accedere a Internet senza utilizzare il cavo RJ45. Tuttavia, a seconda della configurazione, questa soluzione può rallentare la connessione, il che può influire sulla sincronizzazione iniziale (IBD) e sull'uso futuro del nodo (ad esempio, per le transazioni Lightning). Personalmente, non consiglio questa opzione, in quanto un nodo non è destinato all'uso mobile: si accede sempre da remoto, quindi tanto vale lasciarlo collegato.



### Passo 6: Installazione di un nodo Bitcoin su Umbrel



Ora che UmbrelOS è correttamente installato e configurato sulla macchina, si può procedere all'installazione del nodo Bitcoin. Niente di più semplice: andate sull'App Store, aprite la categoria "*Bitcoin*", quindi selezionate l'applicazione "*Bitcoin Node*" (in realtà è Bitcoin core).



![Image](assets/fr/022.webp)



Quindi fare clic sul pulsante "*Installa*".



![Image](assets/fr/023.webp)



Una volta completata l'installazione, il nodo Bitcoin avvierà il suo IBD (*Initial Block Download*): scaricherà e convaliderà tutte le transazioni e i blocchi dalla creazione del Bitcoin nel 2009.



![Image](assets/fr/024.webp)



Questa fase è particolarmente lunga, poiché la sua durata dipende da diversi fattori, tra cui la quantità di RAM allocata nella cache del nodo, la velocità del disco, la velocità della connessione a Internet e la potenza del processore. La gamma di durate è quindi molto ampia, a seconda della configurazione. Con un PC ad alte prestazioni (SSD NVMe, +32 GB di RAM, processore potente e buona connessione a Internet), IBD può essere completato in circa dieci ore. D'altra parte, un processore vecchio, poca RAM o, peggio ancora, un disco meccanico Hard (fortemente sconsigliato) possono prolungare questa operazione fino a diverse settimane.



Con un PC di configurazione normale (un processore decente, da 8 a 16 GB di RAM e un'unità SSD), è possibile trascorrere da 2 a 7 giorni.



Per accelerare leggermente IBD, è possibile aumentare la RAM allocata alla cache del nodo (utilizzata principalmente per il set UTXO, che verrà rivisto più avanti nel corso) tramite il parametro `dbcache`. Su Umbrel, questa modifica si effettua nei parametri del nodo, nella scheda "*Optimization*".



![Image](assets/fr/025.webp)



Per impostazione predefinita, il valore del parametro `dbcache` in Bitcoin core è impostato su 450 MiB, ovvero circa 472 MB. Aumentando questo valore, si può accelerare leggermente IBD. Tuttavia, non raccomanderei necessariamente di spingere questo parametro troppo in alto: anche impostandolo a 4 GiB la sincronizzazione sarà più veloce solo del 10% circa e potrebbe far perdere tempo in caso di interruzione durante l'IBD.



Fate attenzione a non allocare un valore troppo grande per la vostra macchina. Se la RAM disponibile per UmbrelOS si esaurisce, il nodo potrebbe arrestarsi bruscamente, interrompendo l'IBD e richiedendo di riavviarlo manualmente, con una notevole perdita di tempo.



Per saperne di più sull'impatto del parametro `dbcache` sulla sincronizzazione iniziale, consiglio questa analisi di Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Una volta completato l'IBD del nodo (sincronizzazione al 100%), si dispone di un nodo Bitcoin pienamente operativo. Congratulazioni, ora siete parte integrante della rete Bitcoin!



![Image](assets/fr/027.webp)



Nella prossima parte, esploreremo l'uso pratico del vostro nuovo nodo: come collegare il vostro Wallet ad esso e quali applicazioni dovreste installare per diventare un Bitcoiner sovrano.





# Collegamento del Wallet al nodo


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indicizzatori: ruolo, funzionamento e soluzioni


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Se avete già esplorato i nodi Bitcoin prima di seguire questo corso, potreste aver incontrato il termine "indicizzatore". Si tratta di strumenti come Electrs o Fulcrum, che possono essere aggiunti a un nodo Bitcoin core. Ma qual è esattamente il loro ruolo? Come funzionano in pratica? E dovreste installarne uno sul vostro nuovo nodo Bitcoin? Questo è ciò che analizzeremo in questo capitolo.



### Che cos'è un indicizzatore?



In generale, un indicizzatore è un programma che analizza un insieme di dati grezzi, estrae le chiavi rilevanti (come parole, identificatori e indirizzi) e costruisce un file ausiliario, chiamato "indice", in cui ogni chiave si riferisce alla posizione esatta dei dati nel corpus. Questa fase di pre-elaborazione utilizza il tempo della CPU e richiede un po' di spazio su disco, ma elimina la necessità di elaborare l'intero corpus ogni volta che si interroga il database; semplicemente interrogando l'indice si ottiene una risposta quasi immediata.



In parole povere, è lo stesso principio dell'indice di un libro: se si cerca un'informazione specifica, invece di rileggere l'intero libro, si consulta l'indice per trovare direttamente la pagina in cui compare l'informazione cercata.



In un nodo Bitcoin, come il Bitcoin core, i dati Blockchain sono memorizzati nella loro forma grezza e cronologica. Ogni blocco contiene transazioni, che a loro volta contengono input e output, senza alcuna classificazione particolare per Address, identificatore o Wallet . Questa organizzazione lineare è ottimizzata per la convalida dei blocchi, ma inadatta per le ricerche mirate. Ad esempio, se si volessero trovare tutte le transazioni collegate a uno specifico Address in un nodo non indicizzato, si dovrebbe esaminare manualmente l'intero Blockchain, blocco per blocco e transazione per transazione. È proprio qui che entra in gioco l'indicizzatore del nodo Bitcoin.



![Image](assets/fr/085.webp)



Un indicizzatore è un programma software specializzato che analizza questa massa di dati grezzi (set Blockchain, Mempool, UTXO) ed estrae le chiavi, come gli identificatori delle transazioni, gli indirizzi e le altezze dei blocchi. Da queste chiavi, costruisce il suo indice, associando ogni chiave alla posizione esatta delle informazioni nella memoria del nodo.



![Image](assets/fr/086.webp)



L'indicizzazione consente di cercare informazioni sul nodo in modo rapido, preciso ed efficiente. Ad esempio, quando si collega un Wallet come Sparrow al proprio nodo, questo può visualizzare il bilancio di un Address quasi istantaneamente. In concreto, interroga l'indicizzatore con una richiesta del tipo: "_Quali UTXO sono associati a questo script-Hash?_" L'indicizzatore risponde quasi immediatamente, senza dover rileggere l'intero Blockchain, poiché questi dati sono già elencati nel suo database.



### Il Bitcoin core dispone di un indicizzatore?



Senza la necessità di un software aggiuntivo, Bitcoin core non offre, in senso stretto, un indicizzatore Address completo, paragonabile a quelli presenti in software come Electrs o Fulcrum. Tuttavia, incorpora diversi meccanismi di indicizzazione interna, nonché opzioni opzionali per estendere le sue capacità di interrogazione. Per comprendere appieno la situazione, dobbiamo fare una deviazione nella storia del progetto.



Fino alla versione 0.8.0 di Bitcoin core, la convalida delle transazioni si basava su un indice globale delle transazioni, noto come `txindex`. Questo indice faceva riferimento a tutte le transazioni Blockchain e ai loro output. Quando un nodo riceveva una nuova transazione, consultava questo indice per verificare che gli output consumati (in input) esistessero davvero e non fossero già stati spesi. il `txindex` era quindi indispensabile per la validazione delle transazioni all'epoca.



Tuttavia, questo approccio aveva i suoi limiti: era lento, costoso in termini di archiviazione e ridondante in termini di informazioni. Per ovviare a ciò, la versione 0.8.0 introduce una revisione del modello di convalida chiamata ***Ultraprune***. Invece di memorizzare tutto sotto forma di indici di transazioni, Bitcoin core mantiene un semplice database dedicato esclusivamente agli UTXO, chiamato `chainstate` (nel linguaggio comune, questo è noto come "set UTXO"), e ne aggiorna l'elenco man mano che gli output vengono consumati e creati.



Questo metodo è molto più veloce e memorizza solo lo stato corrente del registro, rendendo superfluo l'indicizzatore `txindex`. Tuttavia, invece di eliminare il codice `txindex`, gli sviluppatori hanno scelto di mantenere questa funzionalità dietro un semplice parametro (`txindex=1`). Abilitando questa opzione sul proprio nodo, è possibile interrogare qualsiasi transazione dal suo `txid`.



Contrariamente a quanto si pensa, Bitcoin core non offre l'indicizzazione basata su Address come Electrs o Fulcrum. Le ragioni di questa scelta sono molteplici:





- Il ruolo del Bitcoin core non è quello di diventare un Block explorer completo, né di fornire un'API su misura per ogni utilizzo. L'integrazione di un indice basato su Address implicherebbe una manutenzione a lungo termine Commitment che va oltre lo scopo iniziale del software.





- La maggior parte dei casi d'uso può essere già coperta in altri modi. Ad esempio, per stimare l'equilibrio di un Address, si può usare il comando `scantxoutset`, che interroga direttamente l'insieme UTXO senza richiedere un indice completo.





- Ogni programma software ha requisiti specifici per quanto riguarda il formato o il tipo di dati da indicizzare (Address, script Hash, tag proprietario, ecc.). È più flessibile e logico lasciare che questi programmi costruiscano i propri indici personalizzati piuttosto che fissare una soluzione generica in Bitcoin core.



Bitcoin core ha un indicizzatore di transazioni opzionale (`txindex`), un retaggio del suo funzionamento storico, ma non fornisce un indice Address, né un Interface diretto per ricerche complesse. In alcuni casi, quindi, può essere utile aggiungere un indicizzatore esterno.



### È necessario aggiungere un indicizzatore Address al nodo?



L'aggiunta di un indicizzatore Address, come Electrs o Fulcrum, non è obbligatoria; dipende dalle vostre esigenze specifiche.



Se si desidera semplicemente collegare un Wallet, come il Sparrow, al proprio nodo per visualizzare i saldi e trasmettere le transazioni, questo è possibile direttamente tramite il Interface RPC del Bitcoin core, sia localmente che in remoto tramite Tor.



D'altra parte, per utilizzare software più avanzati, come l'esecuzione di un Mempool.Localmente, l'installazione di un indicizzatore Address diventa indispensabile per lo spazio Block explorer.



L'indicizzatore richiede un certo tempo di sincronizzazione (inferiore a quello dell'IBD) e occuperà ulteriore spazio su disco. Se l'SSD ha ancora spazio libero sufficiente dopo aver scaricato Blockchain, è possibile aggiungere facilmente un indicizzatore.



### Quale indicizzatore scegliere?



Per costruire questo tipo di indice Address e renderlo accessibile si utilizzano comunemente due software: **Electrs** e **Fulcrum**. Questi strumenti indicizzano il Blockchain in base agli script-Hash (indirizzi) e propongono poi un Interface standardizzato (il protocollo Electrum), al quale si collegano numerosi portafogli, come Electrum Wallet, Sparrow o Phoenix.



![Image](assets/fr/087.webp)



In poche parole, Electrs è piuttosto compatto: indicizza Blockchain più velocemente e occupa meno spazio su disco, ma ha prestazioni leggermente inferiori a Fulcrum nelle interrogazioni. Fulcrum, invece, consuma più spazio su disco e richiede più tempo per l'indicizzazione, ma offre prestazioni superiori nelle query.



Per l'uso individuale, consiglio Electrs: consuma meno spazio, è ben mantenuto e, sebbene sia leggermente più lento su alcune richieste rispetto a Fulcrum, è comunque più che sufficiente per l'uso quotidiano. Se avete tempo e spazio su disco, potete anche provare Fulcrum, che avrà prestazioni nettamente superiori, soprattutto su portafogli con numerosi indirizzi da verificare.



In concreto, nell'agosto 2025 Electrs richiederà circa 56 GB di spazio di archiviazione, contro i circa 178 GB di Fulcrum. La scelta dell'indicizzatore, quindi, dipende anche dalla capacità di archiviazione:




- Se lo spazio su disco è molto limitato, dovrete accontentarvi di Bitcoin core senza un indicizzatore Address esterno.
- Se desiderate utilizzare un indicizzatore, ma siete ancora limitati dalla capacità, optate per Electrs.
- Se avete una buona quantità di spazio su disco, Fulcrum potrebbe fare al caso vostro.



Per il resto di questo corso BTC 202, utilizzerò Electrum, ma potete tranquillamente seguire Fulcrum: la procedura di installazione è identica, così come la connessione del Interface al Wallet, poiché entrambi espongono un server Electrum.



### Come si installa un indicizzatore su Umbrel?



Per installare Electrs (o Fulcrum) sul vostro Umbrel, la procedura è semplice: andate sull'App Store, cercate l'applicazione in questione (che si trova nella scheda Bitcoin), quindi fate clic sul pulsante "*Install*".



![Image](assets/fr/028.webp)



Una volta completata l'installazione, Electrs procederà alla fase di sincronizzazione (indicizzazione), che può richiedere diverse ore.



![Image](assets/fr/029.webp)



Una volta completata la sincronizzazione, è possibile collegare il software Wallet al server Electrum, ospitato su Umbrel.



## Come si collega il Wallet al nodo Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Ora che avete un nodo Bitcoin completo, è il momento di farne buon uso! Nel prossimo capitolo esploreremo altri potenziali usi della vostra istanza Umbrel. Tuttavia, iniziamo con le basi: collegare il software Wallet per utilizzare le informazioni del proprio Blockchain e distribuire le transazioni attraverso il proprio nodo.



Come già detto, esistono due interfacce di connessione principali:




- Connessione diretta al Bitcoin core tramite il RPC;
- Oppure collegarsi a un server Electrum (Electrs o Fulcrum).



In questa guida ci concentreremo sulla connessione al nodo tramite Tor, poiché si tratta di una soluzione semplice e sicura per i principianti. Sconsiglio vivamente di esporre la porta RPC del nodo in chiaro, poiché una configurazione errata rappresenta un rischio significativo per la sicurezza e la riservatezza dei dati. Il principale svantaggio delle comunicazioni via Tor è la sua lentezza. Nel prossimo capitolo esploreremo un'alternativa veloce e sicura a Tor per l'accesso remoto al nodo: LA VPN.



In questo capitolo utilizzeremo il Sparrow come esempio, ma la procedura è la stessa per tutti gli altri software di gestione Wallet che accettano connessioni ai server Electrum. È sufficiente individuare l'impostazione corrispondente nei parametri dell'applicazione (di solito in "*Server*", "*Rete*", "*Nodo*"...).



Sul Sparrow, aprire la scheda "*File*" e accedere al menu "Impostazioni".



![Image](assets/fr/030.webp)



Cliccare quindi su "*Server*" per accedere ai parametri di connessione.



![Image](assets/fr/031.webp)



Si scopriranno quindi tre opzioni per collegare il software a un nodo Bitcoin:




- Server pubblico* (giallo): per impostazione predefinita, se non possedete un nodo Bitcoin, questa opzione vi connette a un nodo pubblico che non possedete (di solito quello di un'azienda). Questa opzione non è rilevante in questo caso, poiché avete il vostro nodo su Umbrel.
- Bitcoin core* (Green): questa opzione corrisponde al collegamento tramite Interface RPC, cioè direttamente al Bitcoin core.
- Electrum privato* (blu): questa opzione consente di collegarsi tramite il server Electrum Interface dell'indicizzatore (Electrs o Fulcrum).



### Collegamento a Bitcoin core RPC



Se il nodo Umbrel non dispone di un indicizzatore, questa è l'opzione da selezionare. Su Sparrow, fare clic su "*Bitcoin core*".



![Image](assets/fr/032.webp)



Sarà quindi necessario inserire diverse informazioni per stabilire la connessione al nodo. Tutti questi dati sono accessibili dall'applicazione "*Nodo Bitcoin*" su Umbrel facendo clic sul pulsante "*Connetti*" nell'angolo in alto a destra del Interface.



![Image](assets/fr/033.webp)



La scheda "*Dettagli RPC*" visualizza tutte le informazioni necessarie per la connessione. Scegliere la connessione tramite Tor Address (in `.onion`).



![Image](assets/fr/034.webp)



Inserire questi dati nei campi corrispondenti del Sparrow wallet, quindi fare clic sul pulsante "*Test Connection*".



![Image](assets/fr/035.webp)



Se la connessione va a buon fine, apparirà un segno di spunta del Green e un messaggio di conferma.



![Image](assets/fr/036.webp)



Il segno di spunta in basso a destra del Interface Sparrow wallet sarà ora Green (a indicare una connessione diretta con il Bitcoin core).



**Nota: ** Affinché la connessione vada a buon fine, il nodo deve essere sincronizzato al 100%. In caso contrario, attendere la fine dell'IBD.



### Collegarsi agli elettrotecnici



Se il nodo dispone di un indicizzatore, è meglio collegarsi ad esso piuttosto che utilizzare direttamente Bitcoin core, in quanto le query saranno elaborate più rapidamente.



Sul Sparrow, andare alla scheda "*Elettro privato*".



![Image](assets/fr/037.webp)



Dovrete quindi inserire diverse informazioni per stabilire la connessione con il vostro indicizzatore. Questi dati si trovano nell'applicazione "*Electrs*" (o, se del caso, "*Fulcrum*") su Umbrel.



Selezionare la scheda "*Tor*" per ottenere la connessione `.onion` Address. Se si desidera collegare un software mobile Wallet, è anche possibile scansionare direttamente il codice QR.



![Image](assets/fr/038.webp)



È sufficiente inserire il codice Tor Address del proprio server Electrum nel campo "*URL*", quindi fare clic sul pulsante "*Test Connection*".



![Image](assets/fr/039.webp)



Se la connessione è riuscita, vengono visualizzati un segno di spunta e un messaggio di conferma.



![Image](assets/fr/040.webp)



Il segno di spunta nell'angolo inferiore destro del Interface Sparrow wallet diventerà blu (il colore associato alla connessione a un server Electrum).



**Nota: ** Affinché la connessione funzioni, l'indicizzatore deve essere sincronizzato al 100%. In caso contrario, attendere il completamento del processo di indicizzazione.



Ora sapete come collegare il Wallet al vostro nodo Bitcoin! Nel prossimo capitolo, vi presenterò diverse applicazioni aggiuntive disponibili su Umbrel a cui sono particolarmente affezionato e che vi permetteranno di migliorare l'uso quotidiano del Bitcoin attraverso il vostro nodo.




## Panoramica delle applicazioni disponibili


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel offre un vasto archivio di applicazioni. Come vedrete, ci sono molti strumenti legati a Bitcoin, ma anche un'ampia varietà di applicazioni in campi molto diversi: soluzioni di self-hosting per servizi e file, applicazioni di produttività, strumenti finanziari più generali, gestione dei media, sicurezza e amministrazione della rete, sviluppo, intelligenza artificiale, social network e persino domotica.



In questo corso BTC 202 ci concentreremo esclusivamente sulle applicazioni legate al Bitcoin. Tuttavia, sentitevi liberi di esplorare il resto del catalogo per trovare gli strumenti che potrebbero esservi utili.



Naturalmente, sarebbe impossibile elencare qui tutte le applicazioni del Bitcoin. In questo capitolo, vorrei presentarvi gli strumenti essenziali che faciliteranno e arricchiranno il vostro uso quotidiano di Bitcoin.



### Mempool.space



Nell'uso quotidiano del Bitcoin, se c'è uno strumento veramente indispensabile è il Block explorer. Accessibile online o installato localmente, trasforma i dati grezzi del Blockchain in un formato strutturato, chiaro e di facile lettura. È inoltre dotato di un motore di ricerca che consente agli utenti di individuare rapidamente un blocco, una transazione o un Address specifico.



In concreto, l'explorer consente di stimare le commissioni necessarie per l'inclusione di una transazione in un blocco, quindi di seguirne l'andamento: scoprire se è probabile che venga inclusa nel prossimo futuro, a seconda del mercato delle commissioni, e infine confermare che è stata effettivamente inclusa in un blocco. Offre inoltre la possibilità di analizzare le transazioni passate e di consultarne lo storico. In breve, è il coltellino svizzero del bitcoiner.



Come accennato in precedenza, un explorer può essere ospitato online su un sito web o eseguito localmente sul vostro computer. Uno dei principali svantaggi dei servizi online è che possono compromettere la privacy. Senza VPN o Tor, il server che ospita l'explorer può collegare il vostro IP Address alle transazioni che state visualizzando, il che può fornire un punto di ingresso ideale per l'analisi della catena.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Inoltre, il vostro Internet Service Provider (ISP) potrebbe sapere che state visualizzando una determinata transazione tramite il sito Block explorer. Ciò solleva anche una questione di fiducia: dovete fare affidamento sul servizio online per ottenere informazioni accurate sulle vostre transazioni, senza poterne verificare personalmente la veridicità.



Ecco perché è sempre meglio utilizzare il proprio Block explorer locale. In questo modo, nessun dato relativo alla vostra attività di ricerca trapela, poiché tutte le query vengono elaborate direttamente su una macchina che controllate, senza passare da Internet. Inoltre, un explorer locale si basa sui dati del vostro nodo Bitcoin, che avete convalidato voi stessi, secondo le vostre regole, e di cui vi potete fidare.



Umbrel offre diversi esploratori di blocchi:




- Mempool.Space
- Bitfeed
- Esploratore BTC RPC



Sono particolarmente appassionato di Mempool.Space, che ho installato sul mio nodo. Attenzione: per utilizzare la maggior parte degli esploratori di blocchi su Umbrel, è necessario un indicizzatore Address . È quindi necessaria l'applicazione Bitcoin Node (o Bitcoin Knots), che ha un Blockchain sincronizzato al 100%, e un indicizzatore come Electrs o Fulcrum, anch'esso sincronizzato al 100%.



Una volta installata l'applicazione, è sufficiente aprirla per accedere al proprio explorer.



![Image](assets/fr/041.webp)



Per saperne di più sull'uso dell'explorer Mempool.Space, vi consiglio di consultare questa guida completa:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Nodo fulmineo



Ora che avete il vostro nodo Bitcoin, potete anche creare il vostro nodo Lightning per effettuare transazioni off-chain, senza affidarvi a un'infrastruttura di terzi.



Umbrel offre una serie di applicazioni per aiutarvi a rendere operativo il vostro nodo Lightning. È già possibile scegliere tra due implementazioni principali:




- LND, tramite l'applicazione *Lightning Node*;
- Fulmine di base.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

È quindi possibile amministrare il nodo dal Interface principale oppure, per ottenere funzionalità ancora maggiori e opzioni avanzate, installare *Ride The Lightning* o *ThunderHub*. Questi strumenti vi forniranno un sistema di gestione del Interface basato sul web molto più completo per il vostro nodo.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Infine, vi consiglio l'applicazione *Lightning Network+*, che vi permette di trovare dei pari con cui aprire dei canali, consentendovi di effettuare transazioni in contanti sia in uscita che in entrata.



![Image](assets/fr/089.webp)



Grazie a Umbrel, la gestione di un nodo Lightning personale è stata notevolmente semplificata, ma è ancora relativamente complessa. Per questo motivo, approfondiremo l'argomento in un prossimo corso interamente dedicato a questo utilizzo.



### Scala della coda



Un'altra applicazione che mi piace particolarmente su Umbrel è Tailscale. È un'applicazione VPN progettata per semplificare la creazione di reti sicure tra più dispositivi, ovunque essi si trovino nel mondo. A differenza delle VPN tradizionali, che si basano su server centralizzati, Tailscale utilizza il protocollo WireGuard per stabilire connessioni crittografate end-to-end tra i vari computer. Ciò significa che è possibile implementare una VPN funzionante in pochi minuti, senza dover ricorrere a complicate configurazioni di rete.



Su Umbrel, l'installazione di Tailscale collega il nodo Bitcoin alla propria rete privata virtuale. Una volta configurato, il nodo ottiene un IP Tailscale Address privato, accessibile solo da altri dispositivi connessi alla stessa rete Tailscale (come computer, smartphone e tablet). Questa connessione è crittografata end-to-end e non passa attraverso una rete pubblica non protetta, migliorando notevolmente la sicurezza rispetto a una connessione non crittografata.



![Image](assets/fr/090.webp)



In concreto, Tailscale offre diversi vantaggi nell'utilizzo dell'Umbrel:





- Potete amministrare il Interface Umbrel o accedere alle applicazioni collegate al vostro nodo (come Mempool, Ride The Lightning, ThunderHub...) da qualsiasi luogo, come se foste sulla stessa rete locale, senza esporre le porte su Internet e senza passare per Tor, che è molto lento;





- È possibile collegarsi al proprio server Electrum (Electrs o Fulcrum) o direttamente a Bitcoin core tramite la propria VPN, aggirando Tor. In questo modo si ottiene una connessione sicura, paragonabile all'utilizzo di Tor, ma con una velocità molto più elevata e una latenza ridotta. In breve, si mantengono i vantaggi di Tor in termini di privacy e sicurezza, pur godendo della velocità di una connessione Clearnet. Per un On-Chain Wallet, questo guadagno può sembrare marginale, ma se avete intenzione di creare un vostro nodo Lightning in un secondo momento, la differenza è notevole. Infatti, effettuare pagamenti tramite il proprio nodo in movimento su Tor è estremamente lento a causa dei numerosi scambi necessari, mentre con Tailscale funziona perfettamente.





- Non è necessario configurare regole NAT, aprire porte o configurare un server VPN convenzionale. Una volta installata l'applicazione su Umbrel e sui vostri dispositivi, la rete viene stabilita automaticamente.



Tailscale su Umbrel è quindi una soluzione molto interessante se si vuole accedere al proprio nodo da qualsiasi parte del mondo in modo sicuro, performante e facile da configurare, senza sacrificare la privacy o la sicurezza.



Per installare e configurare Tailscale su Umbrel, consultare questo tutorial, sezione 4: "*Using Tailscale on Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, acronimo di "*Notes and Other Stuff Transmitted by Relays*", è un protocollo aperto e decentralizzato progettato per consentire la pubblicazione e lo scambio di messaggi su Internet senza dipendere da una piattaforma centralizzata. Ogni utente possiede una coppia di chiavi crittografiche: la chiave pubblica (`npub`), che serve come identificatore, e la chiave privata (`nsec`), utilizzata per firmare i messaggi e garantirne l'autenticità.



I messaggi vengono trasmessi attraverso una rete di relè indipendenti. Questa architettura distribuita rende Nostr resistente alla censura: nessun singolo server controlla l'accesso o la distribuzione e un utente può connettersi a tutti i relay che desidera.



Questo protocollo è molto popolare all'interno della comunità Bitcoin perché, come Bitcoin, Nostr affronta questioni di sovranità digitale e controllo dei dati. Il suo creatore, Fiatjaf, è uno sviluppatore già riconosciuto nell'ecosistema per i suoi numerosi contributi.



Con il vostro Umbrel, potete ottimizzare l'uso di Nostr. Installando l'applicazione ***Nostr Relay***, potete ospitare il vostro relay privato direttamente sul vostro computer, assicurandovi che tutti i vostri post e le vostre interazioni su Nostr siano salvati localmente e non vadano persi a causa della cancellazione da parte dei relay pubblici.



I client Nostr ***noStrudel*** o ***Snort*** sono disponibili anche su Umbrel. Grazie a queste applicazioni, è possibile pubblicare, leggere, cercare profili e interagire con l'ecosistema Nostr direttamente dal web Interface sul proprio Umbrel.



Infine, c'è l'app ***Nostr Wallet Connect*** su Umbrel, che abilita i pagamenti Lightning nativi in Nostr. In concreto, potete collegare il vostro futuro nodo Lightning ai vostri clienti Nostr per inviare micropagamenti, chiamati "*zaps*", per premiare contenuti o interagire in modo monetizzato, senza dover passare attraverso un servizio di terze parti. Questi pagamenti vengono inviati direttamente dal vostro nodo personale attraverso i vostri canali.



Per scoprire come utilizzare tutte queste applicazioni, vi consiglio di dare un'occhiata a questo tutorial completo:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Server BTCPay



BTCPay Server è un processore di pagamento gratuito e open-source che consente di accettare pagamenti tramite Bitcoin e Lightning Network senza intermediari, mantenendo la custodia dei fondi.



L'architettura di BTCPay Server è basata su un nodo Bitcoin e, per Lightning, su un'implementazione compatibile (LND, Core Lightning...), il che lo rende una delle uniche soluzioni PoS totalmente non custodiale. È anche il software più completo per la tracciabilità e la contabilità.



![Image](assets/fr/091.webp)



Se siete titolari di un'attività commerciale e desiderate accettare pagamenti Bitcoin direttamente tramite il vostro nodo Umbrel, l'applicazione BTCPay Server è l'ideale per voi. Per saperne di più su questo argomento, vi consiglio di consultare le seguenti risorse:





- Il corso BIZ 101 sull'utilizzo del Bitcoin nella vostra azienda:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Il corso POS 305 sull'utilizzo del server BTCPay:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Il tutorial sul server BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Concetti avanzati e best practice


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Manutenzione del nodo a ombrello


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Per dare il via a questa sezione finale e prima di passare alla teoria più avanzata, in questo breve capitolo vorrei esaminare le migliori pratiche e le azioni concrete che potete intraprendere una volta che il vostro nodo Umbrel è installato, sincronizzato e configurato correttamente. Come lo mantenete quotidianamente?



### Mantenere in salute le attrezzature



Un nodo affidabile inizia con un hardware stabile. Assicuratevi che la macchina che ospita il nodo sia adeguatamente ventilata, priva di Dust e installata in un ambiente asciutto, lontano da fonti di calore e umidità. Evitate di stipare la macchina in uno spazio ristretto e optate per una posizione ben ventilata.



Su Raspberry Pi e mini-PC, il Dust finisce per intasare i dissipatori di calore, aumentando la temperatura e portando al throttling (limitazione volontaria dell'uso delle risorse), che a sua volta si traduce in un calo dell'efficienza del nodo. Per questo motivo consiglio di pulire periodicamente la presa d'aria e la ventola, idealmente ogni pochi mesi.



Assicurarsi di utilizzare un alimentatore Supply di alta qualità, in quanto una tensione instabile può causare la corruzione del sistema e persino un rischio di incendio. L'ideale sarebbe utilizzare l'alimentatore originale Supply fornito dal produttore della macchina. Attenzione anche al surriscaldamento dovuto all'effetto Joule delle ciabatte: rispettare sempre la potenza massima consentita e non collegare mai più ciabatte in cascata.



Consiglio anche di investire in un UPS. Questo protegge il nodo da arresti improvvisi, permette a Umbrel di spegnersi in modo pulito in caso di interruzione e garantisce la continuità del funzionamento durante le microinterruzioni o i guasti di breve durata.



Per quanto riguarda l'archiviazione, tenere d'occhio i progressi: se il disco si sta avvicinando alla saturazione, considerare la possibilità di liberare spazio (disinstallare le applicazioni inutilizzate, regolare le impostazioni dell'indicizzatore) o migrare a un SSD più grande. Lo svantaggio di un nodo Bitcoin completo è che i suoi requisiti di archiviazione aumentano continuamente, poiché ogni 10 minuti viene generato un nuovo blocco e i vecchi blocchi non possono essere cancellati (a meno che il nodo non sia pruned). Vi consiglio quindi di prevedere una capacità sufficientemente ampia al momento dell'acquisto dell'hardware (minimo 2 TB).



### Aggiornamento



Gli aggiornamenti dei nodi sono importanti per tre motivi principali: in primo luogo, la sicurezza (patch di vulnerabilità, indurimento della rete e protezione DoS); in secondo luogo, la compatibilità (modifiche alla politica dei relè, cambiamenti di formato e aggiornamenti di protocollo); in terzo luogo, l'affidabilità e le prestazioni (correzioni di bug, consumo di risorse e altri miglioramenti). Controllate quindi periodicamente che UmbrelOS e le vostre applicazioni siano aggiornate:





- Per aggiornare il sistema: Aprire il menu delle impostazioni, quindi fare clic sul pulsante "*Verifica aggiornamento*" accanto al parametro "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Per aggiornare le applicazioni: Accedere all'App Store. Se una delle applicazioni richiede un aggiornamento, nell'angolo in alto a destra del Interface apparirà un pulsante con una bolla rossa. È sufficiente fare clic su di esso, quindi aggiornare ogni applicazione.



Eseguite questa operazione regolarmente per mantenere aggiornati il sistema operativo e le applicazioni.



### Backup



Se si utilizza il proprio nodo Bitcoin solo per convalidare e distribuire le transazioni, ma i portafogli sono gestiti al di fuori di Umbrel (ad esempio, con un Hardware Wallet e un Sparrow wallet), non c'è nulla di cui eseguire il backup direttamente su Umbrel. In questo caso, il backup essenziale rimane quello della frase di recupero e del Descriptor del vostro Wallet esterno, e questo vale sia che usiate il vostro nodo sia che non lo usiate. Quindi non cambia nulla rispetto alla configurazione precedente.



D'altra parte, a seconda delle applicazioni aggiuntive utilizzate su Umbrel, potrebbero essere necessari ulteriori backup. Ciò è particolarmente vero se si utilizza un nodo Lightning su Umbrel. In questo caso, è assolutamente necessario eseguire il backup del seed fornito al momento dell'installazione del nodo Lightning. Oltre al seed, è necessario un ***Static Channel Backup (SCB)*** aggiornato per poter ripristinare il nodo Lightning in caso di problemi. L'SCB consente di recuperare i fondi chiudendo forzatamente i canali. Se manca il seed o l'SCB, è impossibile ripristinare un nodo Lightning.



Umbrel offre anche la possibilità di eseguire il backup automatico e dinamico di questo SCB sui propri server, tramite Tor, per garantire che sia sempre disponibile un file aggiornato. In questo caso, per ripristinare il nodo è necessario solo il seed.



Rivedremo questi aspetti in dettaglio nel prossimo corso LNP202.



### Sicurezza operativa quotidiana



In termini di sicurezza, utilizzare una password lunga, unica e casuale per Interface Umbrel e ricordarsi di attivare l'autenticazione a due fattori (2FA). Per le applicazioni che offrono protezione sia con password che con 2FA, attivatele sempre entrambe e modificate le password predefinite.



Non esporre mai la dashboard a Internet senza utilizzare un gateway sicuro (come una VPN, Tor o un accesso solo locale). Limitare il numero di applicazioni installate e cancellare regolarmente quelle non più necessarie per ridurre la superficie di attacco.



Per approfondire le vostre conoscenze sulla sicurezza informatica in generale, vi consiglio di dare un'occhiata a quest'altro corso gratuito:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnosi e auto-aiuto



In caso di bug su Umbrel, innanzitutto generate un bundle di diagnostica tramite la sezione di risoluzione dei problemi di UmbrelOS o dell'applicazione interessata, quindi riavviare l'applicazione in modo pulito. Se necessario, tentare anche un riavvio completo del sistema.



Se il problema persiste, vi consiglio di [unirvi alla comunità di utenti Umbrel su Discord](https://discord.gg/efNtFzqtdx). Iniziare a cercare se qualcuno ha già incontrato la stessa difficoltà e ha trovato una soluzione. In caso contrario, è possibile inviare un messaggio nel canale `general-support`. Si può anche utilizzare [il forum di Umbrel](https://community.umbrel.com/).



Queste aree vi permetteranno non solo di seguire gli annunci e gli aggiornamenti sulla sicurezza, ma anche di porre domande e, in ultima analisi, di aiutare altri utenti. È spesso in questi scambi che si scoprono le migliori pratiche.



Con queste semplici abitudini, il vostro nodo Umbrel rimarrà stabile, sicuro e utile, sia per voi che per la rete Bitcoin.




## Comprendere l'IBD e il processo di scoperta tra pari


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Il nodo Bitcoin si avvia senza alcuna conoscenza preliminare della cronologia delle transazioni. Inizialmente, è solo un computer che esegue un software (Bitcoin core o simile). Per diventare un nodo Bitcoin completamente sincronizzato e operativo, deve ricostruire localmente lo stato del Ledger controllando tutti i blocchi pubblicati dal blocco Genesis (blocco 0, pubblicato da Satoshi Nakamoto il 3 gennaio 2009). Questa fase è chiamata **IBD (_Initial Block Download_)**.



L'IBD consiste nello scaricare e verificare ogni blocco e transazione individualmente, applicando le regole del consenso, per costruire la propria versione del Blockchain. L'obiettivo non è semplicemente recuperare una copia di dati non verificati, ma arrivare alla stessa conclusione in modo completamente indipendente, come la maggioranza onesta della rete.



![Image](assets/fr/092.webp)



### Pietre miliari dell'IBD



La sincronizzazione inizia con la fase _**headers-first**_. Il nodo richiede la sequenza di intestazioni di blocco a diversi peer e, per ciascuna di esse, verifica le regole Proof of Work, la regolazione della difficoltà, la sintassi, nonché le regole Timestamp e il numero di versione. In breve, si assicura che ogni intestazione ricevuta sia conforme alle regole di consenso.



![Image](assets/fr/093.webp)



Come promemoria, un blocco Bitcoin consiste in un'intestazione di 80 byte e in un elenco di transazioni. L'impronta digitale del blocco si ottiene applicando un doppio SHA-256 Hash a questa intestazione, che contiene 6 campi:




- versione
- Hash del blocco precedente
- Merkle Root di transazioni
- Timestamp (maggiore del tempo mediano degli 11 blocchi precedenti)
- obiettivo di difficoltà
- Nonce



![Image](assets/fr/094.webp)



Le transazioni vengono impegnate in un Merkle Tree. Si tratta di una struttura che riassume un grande insieme di dati (in questo caso, tutte le transazioni del blocco) aggregando i loro hash progressivamente a due a due fino a un'unica "radice", dimostrando così l'appartenenza di un elemento all'insieme (e rilevando eventuali modifiche). In questo modo, qualsiasi modifica a una transazione modifica anche la radice del Merkle Tree e quindi l'impronta digitale dell'intestazione del blocco. Il SegWit ha introdotto un ulteriore Commitment separato per i cookie (firme), collocato nel coinbase.



![Image](assets/fr/095.webp)



Questo passaggio _**headers-first**_ permette al nodo di identificare il ramo con più lavoro (indipendentemente dal numero di blocchi), che è il ramo su cui i nodi Bitcoin si sincronizzano. Una volta identificato questo ramo, il nodo scarica il contenuto dei blocchi in parallelo da diverse connessioni, quindi convalida ogni transazione: formato, validità degli script (tranne `assumevalid=1`), importi e assenza di doppia spesa. A ogni verifica andata a buon fine, lo stato attuale delle monete non spese (set UTXO) viene aggiornato nel database `chainstate/`: gli output spesi vengono rimossi, mentre vengono aggiunti nuovi output validi.



Il Mempool, invece, entra in gioco solo quando ci si avvicina alla punta della catena: finché il nodo rimane in ritardo, non ha transazioni in sospeso da memorizzare.



Una volta completato l'IBD, il nodo entra nella sua fase normale: convalida i nuovi blocchi man mano che vengono pubblicati, mantiene il suo Mempool con le transazioni in sospeso in base alle sue regole di relè, trasmette transazioni e blocchi e gestisce eventuali riorganizzazioni della catena.



### AssumiValido



Bitcoin core incorpora un meccanismo progettato per ridurre il tempo necessario prima che un nodo sia completamente operativo, pur mantenendo l'essenza del principio di verifica autonoma: AssumeValid.



Il parametro `assumevalid` si basa su un blocco di riferimento passato, il cui Hash è integrato in ogni versione del software. Durante l'IBD, se il nodo scopre che questo blocco si trova effettivamente sul ramo con più lavoro, può ignorare la verifica dello script per tutte le transazioni precedenti a questo punto.



Tutte le altre regole (struttura dei blocchi, Proof of Work, limiti di dimensione, importi delle transazioni, UTXO, ecc. Solo il calcolo delle scritture precedenti a questo blocco di riferimento viene ignorato. L'aumento delle prestazioni è significativo sull'IBD, poiché la verifica delle firme rappresenta una parte importante del carico della CPU. Dopo questo blocco di riferimento, la verifica ritorna allo stato normale.



È possibile forzare la convalida completa di tutti gli script disabilitando questo meccanismo, al costo di un IBD molto più lungo, utilizzando il parametro `assumevalid=0` nel file `Bitcoin.conf`.



### AssumereUTXO



`assumeutxo` è un altro parametro esistente, ma a differenza di `assumevalid`, non è attivato per default. Questo meccanismo consente al software di caricare un'istantanea dell'insieme UTXO, insieme ai suoi metadati, e di considerarlo provvisoriamente come uno stato di riferimento, dopo aver verificato che le intestazioni portino effettivamente al Blockchain con il maggior numero di lavori.



Il nodo diventa così rapidamente operativo per gli usi comuni (RPC, connessione di portafogli, ecc.), avviando contemporaneamente la ricostruzione completa e verificata del proprio set UTXO in background. Una volta completata questa fase, l'istantanea iniziale viene sostituita dallo stato ricostruito localmente. Questo approccio separa la fornitura rapida di nodi dalla verifica completa, senza compromettere quest'ultima.



### Individuazione dei peer: Come fa il nodo a trovare la rete Bitcoin?



Quando un nodo si avvia per la prima volta, non conosce ancora alcun peer. Tuttavia, deve trovare altri nodi Bitcoin su Internet per richiedere intestazioni, quindi blocchi, al fine di completare il suo IBD. Per avviare queste connessioni, Bitcoin core segue una logica di priorità.



![Image](assets/fr/096.webp)



Quando il nodo si riavvia dopo essere stato utilizzato, Core tenta innanzitutto di riconnettersi ai peer in uscita registrati prima dello spegnimento, informazioni memorizzate nel file `anchors.dat`. Quindi, consulta il suo libro IP Address **`peers.dat`**, che memorizza l'elenco dei peer incontrati in precedenza, per riconnettersi ad essi. Si tratta semplicemente di un file locale, aggiornato e conservato da Core. D'altra parte, per un nuovo nodo appena lanciato, questi due file sono vuoti, poiché non ha mai comunicato con altri nodi Bitcoin .



In questo caso, il software interroga i _**DNS seed**_. Si tratta di [server gestiti da sviluppatori riconosciuti dell'ecosistema](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), che restituiscono un elenco di indirizzi IP di nodi presumibilmente attivi. Questi indirizzi consentono al nuovo nodo di avviare le prime connessioni e di richiedere i dati necessari all'IBD. Ecco l'elenco dei semi *DNS* attivi ad oggi (agosto 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: gW-568.Mainnet.achownodes.xyz



Nella stragrande maggioranza dei casi, la fase di *semina DNS* è sufficiente per stabilire le prime connessioni con altri nodi. Se, eccezionalmente, questi server non rispondono entro 60 secondi, il nodo passa a un altro metodo: [un elenco statico di oltre 1.000 indirizzi](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) di _nodi seed_ è integrato nel codice di Bitcoin core e viene aggiornato regolarmente. Se i primi due metodi per ottenere indirizzi IP falliscono, quest'ultima soluzione stabilisce una connessione iniziale, dalla quale il nodo può poi richiedere nuovi indirizzi IP.



![Image](assets/fr/097.webp)



Come ultima risorsa, è possibile forzare manualmente gli indirizzi IP Supply tramite il file `peers.dat` per forzare connessioni specifiche.



Una volta avviato, il gestore interno di Address diversifica le fonti (reti autonome separate, Clearnet e Tor, oltre a varie aree geografiche) per ridurre il rischio di isolamento topologico. Il nodo stabilisce le connessioni in uscita (connessioni che seleziona da solo e che sono quindi più sicure).



Se il nodo è in ascolto su una porta aperta (per impostazione predefinita, 8333), accetta le connessioni in entrata. Queste rafforzano la resilienza complessiva della rete fornendo un punto di contatto per i nuovi nodi, senza apportare alcun beneficio particolare al proprio IBD. Se il nodo funziona su Tor, la logica rimane la stessa, ma gli indirizzi utilizzati sono servizi `.onion`.




## Anatomia del nodo Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Quando il nodo ha completato la sincronizzazione iniziale, memorizza localmente diversi set di dati complementari, che gli consentono di convalidare blocchi e transazioni, servire i peer della rete e riavviarsi rapidamente mantenendo il proprio stato. 3 mattoni principali sono essenziali su un nodo:




- gW-402 **blocchi** memorizzati su disco,
- l'insieme **UTXO** mantenuto in un database chiave-valore,
- e il **Mempool** viene memorizzato nella RAM e serializzato periodicamente.



Inoltre, diversi file ausiliari (pari, preventivi, liste di esclusione, portafogli, ecc.) completano il quadro. Scopriamo il ruolo di tutti questi file.



### Dove si trovano effettivamente i dati del nodo?



Per impostazione predefinita, Bitcoin core salva i propri dati in una specifica directory di lavoro. Sotto GNU/Linux, questa si trova solitamente in `~/.Bitcoin/`, sotto Windows in `%APPDATA%\Bitcoin/` e sotto macOS in `~/Library/Application Support/Bitcoin/`. Se si utilizza una soluzione pacchettizzata (ad esempio, all'interno di una distribuzione di nodi), questa directory può essere montata altrove, ma la sua struttura rimane la stessa. Le sottocartelle e i file importanti descritti di seguito si trovano ancora qui.



![Image](assets/fr/098.webp)



### I blocchi



Il Blockchain è quindi un insieme di blocchi. Un Full node memorizza questi blocchi come file piatti sequenziali e mantiene un indice parallelo per un rapido recupero. Quando è necessario (riorganizzazione, Wallet rescan, servizio peer), questi dati vengono riletti così come sono.



**Nota: ** Una riorganizzazione, o risincronizzazione, è un fenomeno in cui il Blockchain subisce una modifica della sua struttura a causa dell'esistenza di blocchi concorrenti alla stessa altezza. Ciò accade quando una porzione del Blockchain viene sostituita da un'altra catena con una maggiore quantità di lavoro accumulato. Queste risincronizzazioni sono una parte naturale del funzionamento del Bitcoin, dove diversi minatori possono trovare nuovi blocchi quasi contemporaneamente, dividendo così la rete Bitcoin in due. In questi casi, la rete può temporaneamente dividersi in catene concorrenti. Alla fine, quando una di queste catene accumula più lavoro, le altre catene vengono abbandonate dai nodi e i loro blocchi diventano noti come "blocchi obsoleti" o "blocchi orfani" Questo processo di sostituzione di una catena con un'altra è chiamato risincronizzazione.



#### File Blk*.dat (dati grezzi dei blocchi)



I blocchi ricevuti e convalidati vengono scritti in contenitori sequenziali denominati `blkNNNN.dat`, memorizzati nella cartella `blocks/`. Ogni file viene riempito in sequenza fino a raggiungere la dimensione massima di 128 MiB, a quel punto Core apre il file successivo. All'interno, ogni blocco è serializzato in formato di rete, preceduto da un identificatore magico e da una lunghezza. Questa organizzazione consente una scrittura veloce su disco e facilita il servizio di blocco per la sincronizzazione dei peer.



![Image](assets/fr/099.webp)



In modalità pruned, il nodo conserva solo una finestra recente di questi file per limitare l'ingombro su disco. Elimina i contenitori `blk*.dat` più vecchi non appena viene raggiunto l'obiettivo di spazio configurato, pur conservando una cronologia sufficiente per rimanere coerente con la catena più conosciuta. L'indice e il set UTXO rimangono normali, consentendo la convalida delle transazioni e dei blocchi successivi.



#### File Rev*.dat (dati di cancellazione)



Per poter tornare indietro nel tempo durante una riorganizzazione, Core salva, parallelamente a ogni file `blk`, un file `revNNNN.dat` in `blocks/`. Questo file contiene le informazioni necessarie per annullare l'effetto di un blocco sul set di UTXO: per ogni uscita consumata dal blocco, viene memorizzato lo stato precedente del UTXO corrispondente (quantità, script, altezza...). In caso di interruzione del blocco, il nodo può ricostituire rapidamente lo stato precedente senza dover riesaminare l'intera catena.



![Image](assets/fr/100.webp)



#### Indice dei blocchi (blocchi/indice)



La ricerca di un blocco direttamente nei file piatti richiederebbe troppo tempo. Core mantiene quindi un database LevelDB in `blocks/index/` che elenca, per ogni blocco noto, metadati quali Hash, altezza, stato di validazione, file `blk` e offset in cui si trova. Quando un peer richiede un blocco, o quando un componente interno deve accedere a un blocco specifico, questo indice fornisce un accesso rapido. Senza questo indice, sarebbero necessarie troppe operazioni.



![Image](assets/fr/101.webp)



#### Indici opzionali (indici/)



Alcuni indici sono opzionali e disabilitati per impostazione predefinita, in quanto aumentano l'ingombro su disco:




- `indexes/txindex/`, di cui abbiamo già parlato, fornisce una tabella di mappatura della →località delle transazioni, rendendo possibile recuperare qualsiasi transazione confermata senza conoscere il blocco che la contiene. Questo è utile per le interrogazioni fuori dal Wallet di tipo `getrawtransaction`, ma è piuttosto costoso.
- indexes/blockfilter/` che può contenere filtri a blocchi compatti (BIP157/158) per i thin client. Queste strutture accelerano la verifica lato client a scapito della memorizzazione aggiuntiva sul nodo indicizzatore.



### Set UTXO (stato a catena)



Il modello UTXO (*Unspent Transaction Output*) è la rappresentazione contabile di Bitcoin: ogni output non speso è un "Coin" disponibile che può essere utilizzato come input per una transazione futura.



![Image](assets/fr/102.webp)



L'insieme di tutte queste parti in un dato momento T costituisce l'insieme UTXO: un grande elenco di tutte le parti ora disponibili. È questo stato che il nodo consulta per decidere se una transazione spende unità legittime non già utilizzate in una transazione precedente (per evitare il Double-spending).



![Image](assets/fr/103.webp)



L'insieme UTXO è memorizzato nella cartella `chainstate/` come database LevelDB compatto. Ogni parte associa una chiave derivata dal Hash della transazione e l'indice di uscita con un valore contenente: l'importo, il blocco `scriptPubKey`, l'altezza del blocco di creazione e un indicatore coinbase.



![Image](assets/fr/104.webp)



Il nodo mantiene una cache di memoria sopra LevelDB per assorbire le operazioni frequenti di lettura e scrittura. Il parametro `dbcache` può essere usato per modificare la dimensione di questa cache: più è grande, più accessi alla memoria beneficiano l'IBD e la convalida corrente, al costo di un maggiore consumo di RAM. Quando un nuovo blocco viene trovato da un Miner, il nodo cancella dall'insieme UTXO le uscite spese (o consumate) dalle transazioni incluse nel blocco e aggiunge le uscite appena create.



Teoricamente, si potrebbe convalidare una transazione ricontrollando la cronologia dei blocchi per verificare che un'uscita non sia mai stata spesa. In pratica, tuttavia, ciò richiederebbe troppo tempo, poiché l'intero Blockchain dovrebbe essere scansionato per ogni nuova transazione. Il set UTXO, pertanto, fornisce la visualizzazione minima necessaria per dimostrare localmente e in tempi ragionevoli l'assenza del Double-spending.



Si noti che il set UTXO è spesso al centro delle preoccupazioni sulla decentralizzazione del Bitcoin, poiché le sue dimensioni aumentano naturalmente in modo rapido. Ciò è dovuto in parte all'aumento del prezzo del Bitcoin, che incoraggia la frammentazione delle parti, e in parte alla crescente adozione del sistema: più utenti ci sono, maggiore è la richiesta di UTXO.



![Image](assets/fr/105.webp)



La crescita dell'insieme UTXO deriva anche dalla struttura delle semplici transazioni di pagamento su Bitcoin. Infatti, quando si effettua un pagamento, si consuma un singolo UTXO come input e si creano 2 nuovi UTXO come output (uno per il pagamento e l'altro per il Exchange). Infine, un'euristica di analisi della catena, chiamata CIOH (*Common Input Ownership Heuristic*), fornisce un ulteriore incentivo a evitare il consolidamento del Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Poiché una parte di esso deve essere mantenuta nella RAM per verificare le transazioni in un tempo ragionevole, l'insieme UTXO può gradualmente rendere troppo costoso il funzionamento di un Full node. Per risolvere questo problema, esistono già alcune proposte, in particolare [Utreexo](https://planb.network/resources/glossary/utreexo).



### Il Mempool



Il Mempool è l'insieme locale delle transazioni valide che sono state ricevute ma non ancora confermate. Come promemoria, una "transazione confermata" è una transazione che è stata inclusa in un blocco valido. Ogni nodo mantiene il proprio Mempool, che può differire da quello degli altri nodi della rete a seconda di:




- la dimensione allocata al Mempool tramite il parametro `maxmempool`: un nodo con un Mempool più grande sarà in grado di contenere più transazioni di un nodo con un Mempool più piccolo (a meno che quest'ultimo non diventi vuoto);
- regole gW-433: sono un sottoinsieme delle regole di trasmissione del nodo e definiscono le caratteristiche che una transazione non confermata deve soddisfare per essere accettata nel Mempool;
- percolazione delle transazioni: a causa di vari fattori, una determinata transazione può essere stata distribuita in una parte della rete, ma non ancora raggiunta da un'altra.



È importante notare che i mempool dei nodi non hanno valore di consenso. Il Bitcoin funziona perfettamente anche se ogni nodo ha un Mempool diverso. In definitiva, i blocchi autorevoli sono sempre quelli aggiunti alla Blockchain. Ad esempio, anche se un nodo inizialmente rifiuta una determinata transazione nel suo Mempool (valido secondo le regole del consenso), sarà obbligato ad accettarla se alla fine viene inclusa in un blocco con un Proof of Work valido. Se non lo facesse e rifiutasse questo blocco, pur essendo conforme alle regole di consenso, innescherebbe un Hard Fork, cioè la creazione di un nuovo Bitcoin separato su cui sarebbe solo.



#### Politica e gestione della memoria



Quando riceve una transazione, Core applica una serie di controlli rispetto alle regole del consenso (sintassi, script validi, assenza di doppie spese, ecc.) e alle regole Mempool, che rappresentano una politica locale (RBF, soglie minime di addebito, limite di dati nel `OP_RETURN`, ecc.) Se la transazione rispetta queste regole, viene memorizzata.



La dimensione del Mempool è limitata dal parametro `maxmempool` nel file `Bitcoin.conf` (maggiori informazioni nel prossimo capitolo). Per impostazione predefinita, il limite è di 300 MB. Quando è pieno, il nodo aumenta dinamicamente la soglia di carica minima ed espelle per prime le transazioni meno redditizie (cioè, conserva le transazioni che dovrebbero essere estratte per prime). Le transazioni troppo vecchie possono anche scadere dopo un ritardo configurato.



#### Mempool persistenza su disco



Per accelerare i riavvii, Core serializza periodicamente lo stato del Mempool nel file `Mempool.dat` quando il nodo viene spento. Oltre al Mempool vero e proprio, che rimane in memoria, Core memorizza questo file `Mempool.dat` su disco. Al successivo avvio del nodo, ricarica questa istantanea e cancella tutto ciò che non è più valido per il Blockchain corrente.



### File ausiliari e database



Diversi altri file allo stesso livello di `blocks/`, `chainstate/` e `indexes/` partecipano al corretto funzionamento del sistema:




- `peers.dat` mantiene un elenco IP Address di potenziali peer, alimentato dalla scoperta iniziale del DNS, dagli scambi di rete e dalle aggiunte manuali. Quando il nodo si avvia, può attingere a questo file per stabilire le connessioni in uscita.
- Quando il nodo viene spento, `anchors.dat` salva gli indirizzi dei peer uscenti, in modo da poter provare a ricontattarli rapidamente al successivo avvio.
- `banlist.json` contiene i divieti locali decisi dall'operatore o dal nodo (comportamenti ripetuti non validi), al fine di impedire al nodo di riconnettersi o accettare connessioni da questi specifici peer.
- `fee_estimates.dat` memorizza le statistiche sull'orizzonte temporale delle conferme osservate, utilizzate dallo stimatore delle tariffe per proporre tariffe coerenti con gli obiettivi di ritardo scelti durante la creazione di una transazione.
- gW-446.conf` contiene i parametri di configurazione del nodo. È qui che si possono regolare le regole del relè. Se ne parlerà nel prossimo capitolo.
- `settings.json` contiene parametri aggiuntivi a `Bitcoin.conf`.
- `debug.log' è il registro di testo diagnostico, che può essere usato per capire l'attività del nodo in caso di bug.
- gW-448.pid` memorizza l'identificatore del processo in fase di esecuzione, consentendo ad altre applicazioni o script di identificare facilmente bitcoind (*Bitcoin daemon*) e di interagire con esso se necessario. Viene creato all'avvio del nodo e cancellato allo spegnimento.
- `ip_asn.map` è una tabella di mappatura IP → ASN (sistema autonomo) utilizzata per il bucketing e la diversificazione dei peer (opzione `-asmap`).
- `onion_v3_private_key` memorizza la chiave privata del servizio Tor v3 quando l'opzione `-listenonion` è abilitata, per mantenere stabile la cipolla Address tra i riavvii.
- `i2p_private_key` memorizza la chiave privata di I2P quando si usa `-i2psam=`, per effettuare connessioni in uscita ed eventualmente in entrata su I2P.
- `.cookie` contiene un RPC effimero di autenticazione (creato all'avvio e cancellato allo spegnimento) quando si utilizza l'autenticazione tramite cookie. Questo può essere utilizzato, ad esempio, per connettere il software Wallet.
- `.lock` è il blocco della directory dei dati, che impedisce a più istanze di scrivere contemporaneamente sulla stessa directory dei dati.
- `guisettings.ini.bak` è il salvataggio automatico delle impostazioni della GUI (*Bitcoin Qt*) quando si usa l'opzione `resetguisettings`.



Come abbiamo visto nelle prime parti di questo corso BTC 202, Bitcoin core è sia il software del nodo Bitcoin che Wallet. Tuttavia, non è necessariamente la soluzione che consiglierei per la gestione dei portafogli, poiché il suo Interface rimane di base e le sue funzionalità sono limitate rispetto a software moderni come Sparrow o Liana. Core include anche i file per la gestione dei portafogli:





- `wallets/` è la directory predefinita che ospita uno o più;
- `wallets/<nome>/Wallet.dat` è il database SQLite del Wallet (chiavi, descrittori, metadati delle transazioni, ecc.);
- wallets/<nome>/Wallet.dat-journal` è il registro dei rollback di SQLite.



Per riassumere, ecco la struttura del file Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Il percorso di validazione di un nuovo blocco



Alla ricezione di un nuovo blocco, il nodo controlla il Proof of Work e, più in generale, il rispetto delle regole di consenso. Se tutto è a posto, applica le modifiche transazione per transazione al suo set UTXO: controlla che ogni voce spenda gli UTXO esistenti con uno script valido, cancella questi UTXO e aggiunge le nuove uscite. Se tutto è valido, le modifiche vengono impegnate in `chainstate/`.



In parallelo, i dati di annullamento vengono scritti in `rev*.dat` e i metadati nell'indice `blocks/index/`. Il blocco viene quindi serializzato nel file `blk*.dat` corretto. In caso di riorganizzazione, il nodo legge `rev*.dat` al contrario per scollegare in modo pulito i blocchi abbandonati, ripristinare il set UTXO e quindi collegare i blocchi della nuova catena migliore.





## Comprendere il file Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Il file `Bitcoin.conf` è il principale file di configurazione di Interface per Bitcoin core. Permette di regolare il comportamento e i parametri del nodo senza dover ricompilare il codice sorgente o apportare modifiche alla riga di comando. In concreto, si tratta di un file di testo strutturato in coppie chiave-valore, il che significa che ogni riga del file fa riferimento a un parametro specifico (la chiave) e al suo valore associato, che può essere modificato per regolare quel parametro.



I parametri relativi alla rete, al relay delle transazioni, alle prestazioni, all'indicizzazione, al logging e all'accesso al RPC possono essere definiti nel file `Bitcoin.conf`. Tuttavia, questo file di configurazione non modifica mai le regole di consenso del protocollo: imposta solo la politica locale del nodo (regole di relaying), il modo in cui si connette, indicizza ed espone i servizi.



### Posizione e priorità



Per impostazione predefinita, `Bitcoin.conf` risiede nella directory dei dati del Bitcoin core. Si tratta della famosa directory di cui abbiamo parlato nel capitolo precedente. Tuttavia, questo file non viene creato automaticamente da Bitcoin core, tranne in alcuni ambienti, come Umbrel. Se non esiste già, dovrete crearlo voi stessi creando un file chiamato `Bitcoin.conf` e aprendolo con un editor di testo per apportare le vostre modifiche.



I parametri definiti nel file `Bitcoin.conf` possono essere sovrascritti da 2 livelli:




- `settings.json` (scritto dinamicamente dalla grafica Interface o da qualche RPC),
- e le opzioni modificate tramite linee di comando.



Si noti che qualsiasi modifica a `Bitcoin.conf` richiede il riavvio del nodo per avere effetto.



### Formato e struttura



Il formato del file `Bitcoin.conf` è quindi molto semplice: una riga per opzione, nella forma `opzione=valore`. Gli spazi inutili e le righe vuote vengono ignorati e i commenti al codice iniziano con `#`.



Quasi tutte le opzioni booleane possono essere disabilitate con il prefisso `no`. Ad esempio, `listen=0` e `nolisten=1` sono equivalenti a seconda della versione.



Per segmentare la configurazione per rete, si possono usare le sezioni: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. In alternativa, è possibile anteporre al nome dell'opzione il prefisso `regtest.maxmempool=100`.



### Cosa può e non può fare Bitcoin.conf



Come spiegato sopra, le regole di consenso non sono ovviamente configurabili in `Bitcoin.conf`, in quanto ciò potrebbe creare un Hard Fork. D'altra parte, molti altri aspetti sono configurabili. Ci sono 3 classi utili da tenere a mente:




- Parametri puramente locali. Hanno effetto solo sul proprio nodo: dimensione della cache (`dbcache`), modalità pruned (`prune`), indici opzionali... Influenzano le prestazioni della propria macchina, ma non la rete.
- Politiche di relay e Mempool. Queste decidono ciò che il nodo accetta, conserva e rilancia prima della conferma: soglia minima della tassa (`minrelaytxfee`), dimensione e tempo di conservazione del Mempool (`maxmempool`, `mempoolexpiry`), sostituzione delle transazioni (RBF)... Queste regole non fanno parte del consenso, quindi due nodi diversi possono avere politiche diverse ed essere comunque pienamente compatibili. D'altra parte, questi parametri avranno un'influenza sulla rete Bitcoin (come spiegato nella prima parte, in particolare con la teoria della percolazione).
- Connettività di rete. Queste opzioni determinano il modo in cui il nodo trova i peer, ascolta, attraversa un NAT, usa Tor o un proxy o limita la sua larghezza di banda. Danno forma alla topologia, ma non alterano il trasferimento delle transazioni.



La comprensione di questa separazione è fondamentale: se una transazione non è conforme alle regole del consenso, il nodo la rifiuterà in ogni caso. Ma una politica locale più rigida può rifiutarsi di trasmettere una transazione valida ai fini del consenso.



### Rete e topologia



Innanzitutto, è importante distinguere chiaramente tra i due tipi di connessione che un nodo Bitcoin può avere:




- Connessioni in uscita, avviate dal nostro nodo verso un altro nodo;



![Image](assets/fr/106.webp)





- Connessioni in entrata, avviate da un altro nodo verso il nostro.



![Image](assets/fr/107.webp)



Questi due tipi di connessione sono perfettamente in grado di scambiare gli stessi dati in entrambe le direzioni; non si tratta di limitare la direzione del flusso, ma solo di una differenza nell'iniziatore della connessione. Dal punto di vista del nostro nodo, le connessioni in uscita sono generalmente considerate più sicure, poiché siamo noi ad avviarle e a scegliere con precisione il nodo a cui connetterci, rendendo improbabile che la connessione sia malevola. Per impostazione predefinita, Bitcoin core mantiene 10 connessioni in uscita (8 "*full-relay*" + 2 "*block-relay-only*").



Un Full node aggiunge ulteriore valore alla rete accettando le connessioni in entrata. Il parametro `listen=1` abilita l'ascolto sulla porta predefinita 8333 della rete in questione, consentendo di ricevere queste connessioni in entrata sulla rete. Per funzionare, questa porta deve essere aperta anche sul router. In caso contrario, il nodo continuerà a funzionare solo con le connessioni in uscita, senza alcun impatto sull'uso personale del Bitcoin. La scelta di consentire o meno le connessioni in entrata è vostra; non esiste una "scelta migliore"



Se si preferisce non aprire una porta sul router, ma accettare comunque le connessioni in entrata, si può attivare il parametro `listenonion=1`. In questo modo si otterrà lo stesso risultato, ma solo attraverso la rete Tor anziché attraverso clearnet.



A livello di rete, abbiamo anche:




- `addnode`: aggiunge un peer amico da contattare in aggiunta alla solita scoperta (può essere specificato più volte).
- connect`: limita strettamente le connessioni al Address fornito (può essere specificato più volte). Il nucleo non si connetterà a nessun altro nodo.
- `seednode`: è usato solo per compilare il book-Address quando ci si connette a un nodo e poi ci si disconnette.
- `maxconnessioni`: definisce il limite massimo globale per le connessioni in entrata e in uscita. Per impostazione predefinita, questo parametro è impostato a 125, il che significa che il nodo non accetterà mai più di 125 connessioni.
- maxuploadtarget`: limita gli upload per limitare la larghezza di banda in una finestra scorrevole di 24 ore. Questo limite non sacrifica la propagazione di Elements recenti ed essenziali.
- `onlynet`: limita le connessioni in uscita solo alle reti selezionate (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Ad esempio, se si vuole che il nodo si connetta alla rete Bitcoin solo tramite Tor, si può abilitare il parametro `onlynet=onion` e disabilitare le connessioni in entrata (o consentire anche le connessioni tramite Tor).
- `dnsseed`: consente o meno ai _DNS seed_ di richiedere peer quando il pool Address locale è basso (default: `1`, a meno che `-connect` o `-maxconnections=0`).
- `forcednsseed`: forza la richiesta di semi _DNS_ all'avvio, anche se gli indirizzi sono già disponibili (default: `0`).
- `fixedseeds`: Consente l'uso di *nodi seed* (elenco Address codificato) se _DNS seeds_ fallisce o è disabilitato (predefinito: `1`).
- `dns`: Autorizza le risoluzioni DNS in generale (ad esempio, per `-addnode`/`-seednode`/`-connect`).



Per impostazione predefinita, il nodo comunica su clearnet, Tor e I2P. Ciò significa che i peer con cui si connette su clearnet possono vedere il vostro IP pubblico Address e il vostro ISP sarà probabilmente in grado di rilevare che state gestendo un nodo Bitcoin (sebbene il P2P Transport V2 renda più difficile per un ISP origliare). Questo non è necessariamente un problema, ma se si vuole evitare qualsiasi perdita di queste informazioni, si può collegare il nodo esclusivamente tramite la rete Tor.



Per essere completamente abilitati a Tor, è necessario forzare il Bitcoin core a usare solo questa rete e a creare un servizio nascosto per le connessioni in entrata (se si desidera abilitarle). Nel file `Bitcoin.conf`, è necessario aggiungere questa configurazione:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Tutte le connessioni P2P passano attraverso Tor. Il vostro nodo riceve un `.onion' Address per le connessioni in entrata, quindi non è necessario aprire alcuna porta sul router. Il vostro ISP vede solo il traffico Tor e i vostri peer non sono a conoscenza del vostro IP pubblico Address.



Per evitare la risoluzione DNS in chiaro, è possibile aggiungere `dnsseed=0` e `dns=0` alla configurazione. Sarà poi necessario fornire manualmente i peer `.onion` tramite `seednode=` o `addnode=`, poiché altrimenti la scoperta di nuovi nodi sarà difficile.



Ovviamente, se siete principianti, vi consiglio di lasciar perdere tutte queste impostazioni di rete per il momento. La configurazione predefinita è spesso sufficiente.



### Mempool e politica dei relè



#### Parametri di base



Ecco i parametri di base che potete modificare nel vostro `Bitcoin.conf` per quanto riguarda la gestione del vostro Mempool e la trasmissione di transazioni non confermate:





- `maxmempool=<n>`: Limita la dimensione massima del Mempool locale a `<n>` megabyte (default: `300`). Quando il limite viene raggiunto, il nodo aumenta dinamicamente la soglia della tariffa effettiva e dà priorità alle transazioni meno redditizie (in base alla tariffa, non al valore assoluto) per rimanere al di sotto del limite. È possibile lasciare questa impostazione come predefinita. Aumentarla può essere utile se si lavora da soli o se si vuole avere una visione più precisa della congestione del Mempool e migliorare la stima delle tariffe. Al contrario, riducendola si risparmia RAM e, in misura minore, altre risorse di sistema.





- `mempoolexpiry=<n>`: Tempo massimo di conservazione delle transazioni non confermate in Mempool (in ore, valore predefinito: `336`). Dopo questo tempo, le transazioni vengono rimosse anche se rimane spazio disponibile.





- `persistmempool=1`: Salva un'istantanea del Mempool a riposo e la ricarica al riavvio (valore predefinito: `1`). Questo accelera il ripristino dopo il riavvio, evitando la necessità di riapprendere lo stato tramite la rete.





- `maxorphantx=<n>`: Numero massimo di transazioni orfane mantenute (input dipendenti da UTXO non ancora visti nel set UTXO, default: `100`). Oltre questa soglia, le transazioni più vecchie vengono eliminate per evitare una crescita incontrollata della cache.





- blocksonly=1`: Disabilita l'accettazione e la ritrasmissione di transazioni non confermate ricevute dai peer (a meno che non vengano concessi permessi speciali). Il nodo ora carica e pubblicizza solo i blocchi. Le transazioni create localmente possono ancora essere trasmesse (per utilizzare il nodo con il software Wallet). Questo riduce notevolmente la larghezza di banda e i requisiti di RAM, anche se al costo di una minore utilità per il relay e di una totale mancanza di familiarità con il Mempool.





- `minrelaytxfee=<n>`: Tariffa minima (in BTC/kvB) al di sotto della quale le transazioni non vengono accettate nel Mempool del nodo e non vengono trasmesse ai peer (valore predefinito: `0,00001` = 1 sat/vB). Più alto è questo valore, più il nodo filtra in modo aggressivo le transazioni a basso costo.





- `mempoolfullrbf=1`: Accetta le transazioni RBF anche senza un'esplicita segnalazione RBF nella transazione sostituita. Con questa politica "*full-RBF*", una transazione che offre una tariffa più alta può sostituirne un'altra in Mempool se sono soddisfatte le altre condizioni di sostituzione.



Come promemoria, RBF è un meccanismo transazionale che consente al mittente di sostituire una transazione con una con commissioni più elevate per accelerare la conferma. Se una transazione con una commissione troppo bassa rimane bloccata, il mittente può utilizzare *Replace-by-fee* per aumentare la commissione e dare priorità alla transazione sostitutiva nelle mempool e presso i minatori.



#### Impostazioni avanzate e specifiche



Ecco le impostazioni avanzate per il Mempool e la politica dei relè. Se si è alle prime armi, non dovrebbe essere necessario modificare queste impostazioni:





- datacarrier=1`: Consente la trasmissione e (se Mining via nodo) l'inclusione di transazioni che trasportano dati non finanziari attraverso un'uscita `OP_RETURN` (default: `1`). La disattivazione di questo parametro riduce leggermente la superficie per lo spam di dati non finanziari, al costo di una minore compatibilità con alcuni usi. In ogni caso, è necessario accettare `OP_RETURN` minati.





- `datacarriersize=<n>`: Dimensione massima (in byte) del `OP_RETURN` che il nodo trasmette (valore predefinito: `83`). L'abbassamento di questo valore limita i payload trasportati tramite `OP_RETURN`. Si noti che questo limite sarà rimosso per impostazione predefinita in una versione futura di Bitcoin core.





- `bytespersigop=<n>`: Parametro che converte le transazioni di firma in byte equivalenti per la valutazione del limite del relè (default: `20`). Questo influenzerà l'accettazione delle transazioni ricche di `sigops` secondo le regole locali.





- `permitbaremultisig=1`: Consente la trasmissione di transazioni P2MS *bare-Multisig* (default: `1`). Questo è il modello di script più vecchio per stabilire condizioni di firma multipla su un UTXO (inventato nel 2011 da Gavin Andresen).





- `whitelistrelay=1`: Concede automaticamente l'autorizzazione al relay ai peer in entrata inseriti nella whitelist (default: `1`). Questi peer hanno le loro transazioni accettate dal relay anche se il nodo non è in modalità relay generale.





- `whitelistforcerelay=1`: Assegna il permesso "*forcerelay*" ai peer in whitelist con permessi predefiniti (default: `0`). Il nodo quindi inoltra le loro transazioni anche se sono già presenti nel Mempool, aggirando così i meccanismi anti-ridondanza.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Lega un intervallo Interface o Address e assegna permessi a grana fine ai peer corrispondenti: `relay`, `forzelay`, `Mempool` (richiesta di contenuti Mempool), `noban`, `download`, `addr`, `bloomfilter`. Questo può essere utile per concedere un trattamento privilegiato a peer fidati (come gateway, LAN e servizi interni).





- peerbloomfilters=1`: Abilita il supporto per i filtri Bloom (BIP37) per servire blocchi/transazioni filtrate ai thin client (default: `0`). Attenzione: questo aumenta il carico sulle risorse.





- peerblockfilters=1`: Serve i filtri compatti BIP157 (*Neutrino*) ai peer (default: `0`).





- `blockreconstructionextratxn=<n>`: Numero aggiuntivo di transazioni mantenute in memoria per ricostruire i blocchi compatti (predefinito: `100`). Migliora il successo delle ricostruzioni durante le sincronizzazioni compatte, al costo di un po' di memoria.



Come promemoria, tutte queste regole di relè non hanno alcun impatto sulla validità delle transazioni incluse in un blocco valido. Servono a regolare il vostro contributo al relè, a proteggere le vostre risorse e a rendere il vostro nodo prevedibile in ambienti limitati, ma non vi permettono mai di rifiutare i blocchi che rispettano le regole del consenso.



### Portafogli



È inoltre possibile regolare il modo in cui vengono gestiti i portafogli nel file `Bitcoin.conf`. Se non si utilizza Wallet direttamente in Core, ma piuttosto un software di gestione esterno come Sparrow o Liana, questi parametri saranno di scarsa importanza:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Definisce il formato degli indirizzi generati dal Wallet per la ricezione.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Forza il formato Exchange Address (resto di un input su un singolo pagamento).





- `Wallet=<percorso>`: Carica un Wallet esistente all'avvio (può essere ripetuto per caricare più portafogli).





- `walletdir=<dir>`: Directory contenente i portafogli (predefinita: `<datadir>/wallets` se esiste, altrimenti `<datadir>`). Questo può essere utile se si desidera memorizzare i portafogli su un volume dedicato o criptato.





- `walletbroadcast=1`: Trasmette automaticamente le transazioni create dai portafogli caricati (default: `1`). Impostare `0` se si desidera gestire la trasmissione tramite un altro canale.





- `walletrbf=1`: Abilita il RBF opt-in per segnalare il RBF su tutte le transazioni (default: `1`). Consente di aumentare le tariffe in un secondo momento in caso di transazione bloccata.





- `txconfirmtarget=<n>`: Obiettivo di conferma per la transazione (in numero di blocchi, default: `6`). Il Wallet imposterà automaticamente la tariffa per la transazione da confermare entro questo numero di blocchi.





- `paytxfee=<amt>`: Tariffa fissa (BTC/kvB) applicata alle transazioni Wallet. Evitare in generale: utilizzare la stima adattiva tramite `txconfirmtarget`.





- fallbackfee=<amt>`: Tasso di ripiego (BTC/kvB) utilizzato se lo stimatore esaurisce i dati (default: `0,00`). L'impostazione a 0 disabilita completamente il fallback.





- `mintxfee=<amt>`: Soglia minima (BTC/kvB) per la creazione di transazioni da parte di Wallet (valore predefinito: `0,00001`). Wallet rifiuterà di creare una transazione al di sotto di questa soglia.





- `maxtxfee=<amt>`: Limite assoluto alle commissioni totali per una transazione Wallet (default: `0,10` BTC). Protegge da commissioni anormalmente alte che distruggerebbero inutilmente i bitcoin.





- `avoidpartialspends=1`: Seleziona gli UTXO per cluster Address per evitare spese parziali.





- `spendzeroconfchange=1`: Consente di riutilizzare un UTXO Exchange non confermato come voce in una nuova transazione (default: `1`).





- `consolidatefeerate=<amt>`: Tasso massimo (BTC/kvB) oltre il quale Wallet evita di aggiungere più input del necessario per consolidare. Ciò consente consolidamenti opportunistici a prezzi bassi e riduce i costi quando i costi sono elevati.





- `maxapsfee=<n>`: Budget per le spese aggiuntive (BTC, valore assoluto) che il Wallet accetta di pagare per attivare l'opzione "*evita spese parziali*".





- `discardfee=<amt>`: Tasso (BTC/kvB) che indica la tolleranza a buttare via il Exchange aggiungendolo alla tariffa. Le uscite che costerebbero più di un terzo del loro valore a questo tasso vengono eliminate.





- `keypool=<n>`: Dimensione del pool Address pre-generato (predefinito: `1000`). Valori troppo piccoli aumentano il rischio di ripristini incompleti.





- `disablewallet=1`: Avvia Bitcoin core senza il sottosistema Wallet e disabilita le RPC associate. Riduce la superficie di attacco e l'impronta se il nodo viene usato solo per la convalida/rilascio.



### Archiviazione, indicizzazione e prestazioni



Il file di configurazione consente anche di regolare i parametri relativi alla macchina. Questo può essere particolarmente importante se si dispone di risorse limitate o, al contrario, di una grande quantità di capacità disponibile:





- `datadir=<dir>`: Imposta la directory principale dei dati di Bitcoin core.





- `blocksdir=<dir>`: Disaccoppia la posizione dei file dei blocchi (`blocks/blk*.dat` e `blocks/rev*.dat`) dalla `datadir`. Questo può essere utile per collocare l'archivio dei blocchi su un volume diverso, mantenendo la base di stato (`chainstate/`) su un supporto più veloce, ad esempio.





- `dbcache=<n>`: Alloca `<n>` MiB alla cache del database (*LevelDB*) utilizzata dall'indice dei blocchi e dal `chainstate` (valore predefinito: `450`). Più alto è il valore, più veloce è l'IBD e la validazione corrente, al costo di un maggiore consumo di RAM.





- `prune=<n>`: Abilita il pruning dei file a blocchi e imposta un obiettivo di spazio su disco in MiB (predefinito: `0` = disabilitato; `1` = pruning manuale tramite RPC; `>=550` = pruning automatico al di sotto dell'obiettivo). Incompatibile con `txindex=1`. Il nodo rimane un nodo pienamente validante, ma non può più fornire la vecchia cronologia. Questa opzione è particolarmente utile se lo spazio su disco è limitato, ad esempio quando si installa un nodo sul computer di casa.





- txindex=1`: Costruisce e mantiene un indice globale delle transazioni confermate. È essenziale per alcune query (`getrawtransaction` non-Wallet) e per scopi di esplorazione, ma aumenta significativamente l'ingombro su disco. Incompatibile con la modalità pruned.





- `assumevalid=<hex>`: Indica un blocco che si presume valido, consentendo di saltare i controlli di script per i suoi antenati (impostare `0` per controllare tutto). Si veda il capitolo precedente per ulteriori informazioni.





- `reindex=1`: Ricostruisce gli indici dei blocchi e lo stato (`chainstate`) dai file `blk*.dat` su disco. Ricostruisce anche gli indici attivi opzionali. È un'operazione che richiede molto tempo per riparare un database danneggiato o per attivare/disattivare in modo pulito indici pesanti.





- `reindex-chainstate=1`: Ricostruisce solo il `chainstate` dall'indice di blocco corrente. Preferibile quando i file di blocco sono sani.





- `blockfilterindex=<tipo>`: Mantiene gli indici dei filtri di blocco compatti (ad esempio, `basic`) usati dai thin client (BIP157/158) e da alcune RPC. Disabilitato per impostazione predefinita (`0`). Consuma ulteriore spazio su disco e tempo di indicizzazione.





- `coinstatsindex=1`: Mantiene un indice delle statistiche dei set UTXO gestito dalla chiamata `gettxoutsetinfo`. Utile per le verifiche e le metriche, eliminando la necessità di un costoso ricalcolo. Disattivato per impostazione predefinita.





- `carica blocco=<file>`: Importa i blocchi all'avvio da un file esterno `blk*.dat`. Si usa per precaricare la cronologia da una fonte offline (copia locale, supporto esterno) per accelerare l'inizializzazione.





- `par=<n>`: Imposta il numero di thread di verifica dello script (da `-10` a `15`, `0` = auto, `<0` = lascia libero questo numero di core). Permette di regolare il parallelismo della CPU durante la validazione. La modalità automatica è adatta nella maggior parte dei casi.





- `debuglogfile=<file>`: Specifica la posizione del registro `debug.log`.





- `shrinkdebugfile=1`: Riduce la dimensione di `debug.log` all'avvio (valore predefinito: `1` quando `debug` non è attivo).





- `settings=<file>`: Percorso del file delle impostazioni dinamiche `settings.json`.



### RPC accesso e sicurezza operativa



Infine, il file `Bitcoin.conf` consente di configurare i parametri di accesso al nodo. Siate cauti con queste impostazioni, soprattutto se siete agli inizi: evitate di modificarle senza averne compreso a fondo le implicazioni, perché potrebbero introdurre delle vulnerabilità.





- `server=1`: Attiva il server JSON-RPC. Essenziale se si utilizza `bitcoind` tramite `bitcoin-cli` o un'applicazione di terze parti. Disattivare (`0`) su un nodo di pura convalida che non espone alcuna API o che utilizza già un server Electrum.





- `rpcbind=<addr>[:port]`: Server RPC in ascolto Address/port. Per impostazione predefinita, l'ascolto avviene solo localmente (`127.0.0.1` e `::1`). Questo parametro viene ignorato se non viene definito anche `rpcallowip`. Usarlo per limitare esplicitamente Interface.





- `rpcport=<port>`: Porta RPC (predefinita: `8332` su Mainnet, `18332` su Testnet, `38332` su bookmark, `18443` su regtest).





- `rpcallowip=<ip|cidr>`: Consente i client RPC da un determinato IP o subnet (può essere ripetuto). Da usare insieme a `rpcbind` per esporre l'API solo a un segmento fidato (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Metodo di autenticazione RPC consigliato (password con hash). Consente più inserimenti ed evita di memorizzare un segreto in chiaro.





- `rpccookiefile=<path>`: Percorso del cookie di autenticazione (predefinito: file `.cookie` sotto `datadir/`). Viene utilizzato per l'accesso locale da parte dello stesso utente senza gestire password persistenti. Ad esempio, si può usare per collegare il Liana Wallet al Bitcoin core sulla stessa macchina.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Autenticazione classica RPC con password in chiaro. Evitare di usarlo a favore di `rpcauth` o di un cookie.





- `rpcthreads=<n>`: Numero di thread per servire le chiamate RPC (valore predefinito: `4`). Aumentarlo se si hanno picchi di chiamate elevati sul lato del monitoraggio/strumento esterno.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist di API autorizzate. Riduce la superficie di attacco limitando i metodi accessibili.





- `rpcwhitelistdefault=1|0`: Comportamento predefinito della whitelist: se abilitato e viene utilizzata una whitelist, le chiamate non elencate vengono rifiutate. Questo può anche forzare un insieme vuoto predefinito (nessuna chiamata consentita), purché non ci sia nulla di esplicitamente elencato.





- `rest=1`: Abilita l'API REST pubblica (disabilitata per impostazione predefinita). Da esporre solo su una rete fidata (stessa cautela di JSON-RPC).





- `conf=<file>`: Specifica, solo sulla riga di comando, un file di configurazione di sola lettura. Utile per congelare un profilo di esecuzione (immutabile) sul lato operativo.





- `includeconf=<file>`: Carica un file di configurazione aggiuntivo (percorso relativo a `datadir/`). Permette la separazione dei ruoli: base comune + sovraccarico locale sensibile.





- `daemon=1` / `daemonwait=1`: Avvia `bitcoind` in background e, con `daemonwait`, attende che l'inizializzazione finisca prima di consegnarlo. Questo facilita l'integrazione con i supervisori (systemd, runit).





- `pid=<file>`: Posizione del file PID.





- `sandbox=<log-e-abort|abort>`: Abilita il sandboxing sperimentale delle syscalls: sono consentite solo le syscalls previste.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Esegue un comando all'avvio o allo spegnimento.





- `alertnotify=<cmd>`: Attiva un comando al ricevimento di un avviso.





- `blocknotify=<cmd>`: Esegue un comando per ogni nuovo blocco.





- `debug=<categoria>|1` / `debugexclude=<categoria>`: Abilita/disabilita categorie di log dettagliate (ad esempio `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Registra gli indirizzi IP.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Aggiunge rispettivamente le posizioni delle fonti, i nomi dei thread e i timestamp precisi ai registri.





- `printtoconsole=1`: Invia tracce/debug alla console (*stdout*).





- `help-debug=1`: Visualizza l'aiuto dell'opzione di debug e si chiude.





- `uacomment=<cmt>`: Aggiunge un commento a User-Agent P2P.



Abbiamo finito di elencare la maggior parte dei parametri di configurazione. Questo file `Bitcoin.conf' costituisce quindi il vero cruscotto del nodo: definisce la configurazione della rete, la gestione del Mempool , l'uso del disco e della memoria, l'indicizzazione e l'amministrazione generale. Se volete saperne di più su questo file e crearne uno su misura per le vostre esigenze, vi consiglio di usare [Jameson Lopp's generator](https://jlopp.github.io/Bitcoin-core-config-generator/).



Siamo giunti alla conclusione di questo corso BTC 202, che vi avrà permesso non solo di comprendere le basi del funzionamento dei nodi e della loro interazione all'interno del sistema, ma anche di crearne uno vostro. Ora siete un Bitcoiner sovrano, con la vostra autocustodia Wallet, che trasmette le vostre transazioni tramite il vostro nodo. Congratulazioni!



Ora potete passare alla parte finale del corso, dove potrete valutare il BTC 202 e poi prendere il diploma per verificare che abbiate acquisito tutti i concetti trattati.



Ora avete diverse opzioni a disposizione. Il passo logico successivo è quello di creare un proprio nodo Lightning, che vi permetta di essere completamente indipendenti per le vostre transazioni off-chain. Questo sarà l'argomento di un prossimo corso, che sarà pubblicato nell'autunno del 2025 sul Plan ₿ Network.



Nel frattempo, vi invito a scoprire la formazione BTC 204, che vi consentirà di comprendere e padroneggiare i principi di protezione della privacy nell'utilizzo di Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Parte finale


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Recensioni e valutazioni


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Esame finale


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Conclusione


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>