---
name: Impostazione del primo nodo Bitcoin
goal: Comprensione, installazione, configurazione e utilizzo di un nodo Bitcoin
objectives: 


  - Comprendere il ruolo e lo scopo di un nodo Bitcoin.
  - Identificare le diverse soluzioni hardware e software disponibili.
  - Installare e configurare un full node (Bitcoin Core).
  - Utilizzate l'interfaccia Umbrel e aggiungete applicazioni utili.
  - Collegare un wallet personale al proprio nodo.
  - Esplorate le impostazioni avanzate e le migliori pratiche di sicurezza.


---
# Diventare un bitcoiner sovrano



Probabilmente conosci il detto "Not your keys, not your coins", che incoraggia l'autocustodia dei tuoi bitcoin. Possedere le proprie chiavi è un primo passo essenziale, ma non è sufficiente. Per ottenere la vera sovranità monetaria, è necessario anche installare e utilizzare il proprio nodo Bitcoin. Questo corso è stato progettato per guidarti in un passo fondamentale del tuo viaggio in Bitcoin!



BTC 202 è una formazione accessibile pensata per insegnarti a gestire il tuo nodo Bitcoin, anche se non sei un esperto tecnico. Inizieremo definendo cos’è un nodo Bitcoin, a cosa serve e perché è assolutamente essenziale gestirne uno autonomamente. Ti guiderò poi passo dopo passo nella scelta dell’hardware, nell’installazione dei software necessari, nel collegamento del tuo walleto e nelle prime ottimizzazioni possibili per progredire ulteriormente.



La gestione di un nodo Bitcoin per gli esperti non è solo un'opzione, ma una necessità. È uno strumento di resilienza che ogni utente deve comprendere e implementare. Questo corso è il punto di partenza per diventare un bitcoiner sovrano!




+++




# Introduzione


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Panoramica del corso


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Benvenuto a BTC 202, dove imparerai a installare, configurare e utilizzare un nodo Bitcoin in modo semplice e indipendente. Ma non solo: imparerai anche a conoscere il ruolo e la funzione dei nodi nel sistema Bitcoin. Il corso alterna spiegazioni teoriche a pratiche guidate.



### Parte 1 - Introduzione



In questa prima parte del corso, chiariremo le nozioni di base per poi passare a definizioni più precise. Che cos'è un nodo? Quali sono le differenze tra nodo, wallet e miner? Si parlerà poi del Bitcoin Core e delle implementazioni del protocollo. L'obiettivo è quello di parlare la stessa lingua, evitare confusione e stabilire una solida base teorica.



### Parte 2 - Diventare un bitcoiner sovrano



In questa seconda parte, inizierò spiegando perché è importante gestire il proprio nodo Bitcoin. Esploreremo poi i diversi tipi di nodi esistenti (completo, pruned, SPV...), il loro funzionamento e le loro implicazioni tecniche.



Ti forniremo quindi una panoramica del software disponibile per l'esecuzione di un nodo Bitcoin, con i relativi vantaggi e svantaggi. Infine, concluderemo con alcuni consigli pratici per la scelta dell'hardware adatto alle tue esigenze e al tuo budget.



Questa sezione, quindi, illustra il percorso del bitcoiner sovrano: capire perché è necessario gestire un nodo, scegliere il tipo di nodo, in base a questa scelta, selezionare il software e, in base al software scelto, determinare l'hardware appropriato.



### Parte 3 - Installazione semplice di un nodo Bitcoin



Una volta completata questa preparazione, è il momento di passare alla pratica con la Parte 3 dedicata a Umbrel: il sistema operativo per il cloud domestico che semplifica il self-hosting e l'installazione di un nodo Bitcoin e Lightning.



Dopo una breve introduzione a Umbrel, forniremo un tutorial dettagliato per guidarti attraverso il processo di installazione e configurazione sulla vostra macchina fai-da-te. L'obiettivo di questa parte è chiaro: avere il tuo primo nodo Bitcoin completamente funzionante e sincronizzato.



### Parte 4 - Collegamento del wallet al nodo



Ora che hai configurato un nodo Bitcoin, è il momento di usarlo! In questa sezione imparerai a collegare il tuo software di gestione wallet (come il Sparrow wallet) al vostro address indexer(indicizzatore di indirizzi) (Electrs o Fulcrum) o direttamente a Bitcoin Core, in modo da non dipendere più dai server pubblici.



Esamineremo anche il ruolo degli indexer e i vari metodi di connessione al proprio nodo (LAN, Tor, Tailscale, ecc.). Infine, nell'ultimo capitolo, passeremo in rassegna le applicazioni più utili disponibili su Umbrel per il bitcoiner di tutti i giorni.



### Parte 5 - Concetti avanzati e best practice



In questa parte finale di BTC 202, l'obiettivo è quello di approfondire le tue conoscenze. In primo luogo, esamineremo le migliori pratiche da adottare con il tuo nuovo nodo Bitcoin e come mantenerlo a lungo termine.



In seguito, ci occuperemo di rivedere alcune delle teorie trattate in precedenza nel corso, tra cui la comprensione del processo IBD e la scoperta dei peer in dettaglio, l'esplorazione dell'anatomia di un nodo e, infine, l'apprendimento dell'uso del file `Bitcoin.conf` per mettere a punto le impostazioni.



### Parte 6 - Sezione finale



Come per tutti i corsi Plan ₿ Academy, nella sezione finale troverai un esame finale per verificare le tue conoscenze sui nodi Bitcoin.



Allora, sei pronto ad accendere il tuo primo nodo Bitcoin? Traccia la rotta verso la sovranità!



## Che cos'è un nodo Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Come descritto dal suo creatore, [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi), Bitcoin si presenta come un sistema di denaro elettronico [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p). Questa semplice frase, che è il titolo del [White Paper](https://planb.academy/resources/glossary/white-paper), contiene molti indizi sulla natura di Bitcoin:




- Innanzitutto, il Satoshi descrive Bitcoin come un "sistema", in altre parole un insieme coerente di componenti hardware e software che interagiscono per fornire un servizio specifico o svolgere una funzione specifica;
- Spiega poi che questo sistema consente l'uso di contanti elettronici, cioè di una forma di moneta immateriale;
- Infine, sottolinea che questo sistema non dipende da alcuna entità centrale: è "peer-to-peer", cioè sono gli stessi utenti a gestire il sistema.



Poiché Bitcoin è un sistema, deve necessariamente essere eseguito su computer. E, data la sua natura peer-to-peer, sono gli stessi utenti ad assumersi la responsabilità di far funzionare queste macchine. Quello che chiamiamo "[nodo Bitcoin](https://planb.academy/resources/glossary/node)" è proprio il computer su cui gira il software che implementa il protocollo Bitcoin (come [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core), ma su questo torneremo più avanti). Questo è ciò che consente al Bitcoin di operare senza un'autorità centrale: la convalida viene effettuata in modo [distribuito](https://planb.academy/resources/glossary/distributed), da migliaia di macchine indipendenti appartenenti a migliaia di utenti.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



Sono proprio questi utenti a garantire la sicurezza di Bitcoin. Come spiega Eric Voskuil nel suo libro *Cryptoeconomics*, la sicurezza di Bitcoin non si basa né sulla [blockchain](https://planb.academy/resources/glossary/blockchain), né sulla [potenza di hashing](https://planb.academy/resources/glossary/hashrate), né sulla validazione, sulla decentralizzazione, sulla [crittografia](https://planb.academy/resources/glossary/cryptography), sull'[open source](https://planb.academy/resources/glossary/foss) o sulla teoria dei giochi. La sicurezza di Bitcoin dipende principalmente dagli individui che sono disposti a esporsi al rischio personale. La decentralizzazione permette di distribuire questo rischio su un gran numero di individui, ed è solo la loro capacità di resistere che garantisce la solidità del sistema.



Questo principio è facile da capire: se Bitcoin dipendesse da un singolo nodo di proprietà di un'unica persona, l'imprigionamento di questa persona sarebbe sufficiente a spegnere la rete, poiché da sola si assumerebbe tutti i rischi. Con decine di migliaia di nodi sparsi in tutto il mondo, il rischio è diffuso: ognuno di questi operatori dovrebbe essere neutralizzato per spegnere Bitcoin.



![Image](assets/fr/048.webp)



Possiamo quindi distinguere e definire dei concetti, in modo da rendere più chiari gli argomenti per il resto del corso.




- La valuta Bitcoin: l'unità di conto utilizzata per le transazioni all'interno di questo sistema;
- Il network Bitcoin: l'insieme di tutti i nodi connessi;
- I Nodi Bitcoin: macchine che eseguono un'[implementazione di Bitcoin](https://planb.academy/resources/glossary/bitcoin-implementation);
- Le implementazioni di Bitcoin: dei software che traducono il protocollo in istruzioni eseguibili;
- Il protocollo Bitcoin: l'insieme delle regole che governano il funzionamento del sistema;
- Il sistema Bitcoin: la combinazione coerente di tutti questi elementi.



### Il ruolo del nodo Bitcoin



L'insieme dei nodi Bitcoin forma il cosiddetto Bitcoin network. Essi consentono all'intero sistema di operare in modo autonomo, senza ricorrere a un'autorità centrale o a una gerarchia di server.



Fin dall'inizio, Bitcoin è stato progettato per consentire a ciascun utente di gestire un nodo personale. Questo concetto rimane valido con l'attuale software Bitcoin Core, che combina i ruoli di [wallet](https://planb.academy/resources/glossary/wallet) e nodo. Al giorno d'oggi, però, questa funzione è spesso dissociata: molti wallet Bitcoin moderni sono solo wallet che si collegano a nodi esterni (di proprietà della stessa persona o meno).



### Mantenere la Blockchain



Il primo compito di un nodo è quello di mantenere una copia locale della blockchain. Per prevenire il [double-spending](https://planb.academy/resources/glossary/double-spending-attack) su Bitcoin senza coinvolgere un'autorità centrale, ogni utente deve verificare che non esista alcuna [transazione](https://planb.academy/resources/glossary/transaction-tx) nel sistema. L'unico modo per esserne certi è conoscere tutte le transazioni effettuate su Bitcoin. Per questo motivo, tutte le transazioni sono [marcate temporalmente](https://planb.academy/resources/glossary/timestamp) e raggruppate in [blocchi](https://planb.academy/resources/glossary/block), e ogni nodo memorizza l'intera blockchain.



> L'unico modo per confermare l'assenza di una transazione è essere a conoscenza di tutte le transazioni.

Nakamoto, S. (2008). *Bitcoin: un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



La blockchain è quindi un registro in evoluzione: ogni volta che un nuovo blocco viene pubblicato da un [miner](https://planb.academy/resources/glossary/miner), il nodo ne verifica la validità prima di aggiungerlo alla propria copia locale della catena. Ad oggi (luglio 2025), l'intera blockchain supera i 675 GB e questa dimensione continua a crescere, poiché viene aggiunto un nuovo blocco in media ogni 10 minuti.



![Image](assets/fr/049.webp)



Il nodo mantiene anche un registro locale di tutti gli [UTXO](https://planb.academy/resources/glossary/utxo) esistenti in un dato momento, noto come **[UTXO set](https://planb.academy/resources/glossary/utxo-set)**. Questo database contiene tutti i frammenti di bitcoin non spesi. Questo argomento sarà ripreso in dettaglio nella parte finale del corso.



### Verifica e distribuzione delle transazioni



Il secondo ruolo di un nodo è quello di assicurare la verifica e la propagazione delle transazioni. Quando una nuova transazione raggiunge il nodo (tramite il wallet o un altro nodo), esso verifica che sia conforme a un insieme di regole ([regole di consenso](https://planb.academy/resources/glossary/consensus-rules) e [regole di propagazione](https://planb.academy/resources/glossary/relay)). Ad esempio:




- i bitcoin spesi devono esistere nel suo UTXO set (il database degli [output](https://planb.academy/resources/glossary/output) non spesi);
- la [firma](https://planb.academy/resources/glossary/digital-signature) deve essere valida e tutte le condizioni di spesa devono essere soddisfatte ([script](https://planb.academy/resources/glossary/script) valido);
- l'importo totale delle uscite non deve superare l'importo totale delle [entrate](https://planb.academy/resources/glossary/input), il che significa che i [costi](https://planb.academy/resources/glossary/transaction-fees) non possono essere negativi.



![Image](assets/fr/050.webp)



Dopo la convalida, la transazione viene memorizzata nella [Mempool](https://planb.academy/resources/glossary/mempool) del nodo, uno spazio di memoria temporaneo riservato alle transazioni non confermate, e quindi trasmessa agli altri peer della rete a cui è collegato. Questo meccanismo di distribuzione e convalida continua da nodo a nodo. In questo modo, la transazione si propaga attraverso la rete Bitcoin e ogni nodo la memorizza nella Mempool fino a quando non viene inclusa in un blocco valido da un miner, che agisce quindi alla sua prima [conferma](https://planb.academy/resources/glossary/confirmation).



### Controllare e distribuire i blocchi



Il terzo ruolo del nodo riguarda la gestione dei blocchi estratti. Quando un miner scopre un nuovo blocco con una [proof of work](https://planb.academy/resources/glossary/proof-of-work) valida, lo [trasmette](https://planb.academy/resources/glossary/diffusion) in rete. I nodi lo ricevono, verificano che sia conforme a tutte le regole del protocollo e lo integrano nella propria copia locale della blockchain se è valido. Come nel caso delle transazioni, i blocchi appena convalidati vengono trasmessi a tutti i peer connessi al nodo. Questo processo continua fino a quando tutti i nodi del network Bitcoin sono a conoscenza del nuovo blocco.



![Image](assets/fr/051.webp)



## Qual è la differenza tra un nodo e un wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



È essenziale distinguere tra due tipi di software distinti quando si utilizza Bitcoin: il nodo e il wallet.



Un nodo Bitcoin, come già detto, è un software che partecipa attivamente alla rete peer-to-peer. Svolge tre compiti principali:




- backup della blockchain,
- convalida e relay(trasmissione) delle transazioni,
- convalida dei blocchi e relay.



Un Bitcoin wallet, invece, è un software progettato per memorizzare e gestire le chiavi private. Queste chiavi consentono di spendere i bitcoin soddisfacendo gli script di blocco (in genere attraverso una firma). Un wallet può connettersi a un nodo (locale o remoto) per consultare lo stato della blockchain e trasmettere le transazioni che costruisce, ma non è, in quanto tale, un partecipante alla rete.



In alcuni casi, queste due funzioni coesistono all'interno dello stesso software, come nel caso di Bitcoin Core, che funge sia da full node che da wallet. Tuttavia, molti dei programmi wallet più diffusi (Sparrow, BlueWallet, ecc.) richiedono una connessione a un nodo esterno (proprio o di terzi) per trasmettere le transazioni e determinare il saldo del wallet.



![Image](assets/fr/052.webp)



## Qual è la differenza tra un nodo e un miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Le nozioni di nodo e miner sono spesso confuse. Eppure questi due elementi svolgono funzioni radicalmente diverse all'interno del sistema.



Inizialmente, quando Bitcoin fu lanciato da Satoshi Nakamoto nel 2009, ci si aspettava che ogni utente partecipasse alla rete nel suo complesso. Pertanto, il software originale di Bitcoin combinava più funzioni contemporaneamente: fungeva da wallet, un nodo, e anche da miner, in grado di generare nuovi blocchi. All'epoca, la difficoltà del mining era molto bassa. Bastava eseguire il software Bitcoin sul proprio computer per trovare blocchi e ricevere bitcoin come ricompensa.



Tuttavia, con la graduale diffusione di Bitcoin e l'aumento del numero di miner, il panorama competitivo del mining ha subito un cambiamento radicale. Oggi il mining è diventato un'attività estremamente competitiva, dominata da operatori industriali dotati di infrastrutture specializzate. La potenza richiesta per estrarre un nuovo blocco è ora così grande che è praticamente impossibile per un singolo utente raggiungere questo obiettivo utilizzando solo un computer convenzionale. Di conseguenza, il mining viene ora eseguito principalmente con dispositivi specializzati chiamati [ASIC](https://planb.academy/resources/glossary/asic) (*Application-Specific Integrated Circuits*). Questi chip sono ottimizzati esclusivamente per eseguire il double [SHA-256](https://planb.academy/resources/glossary/sha256), l'algoritmo utilizzato per il mining di Bitcoin.



![Image](assets/fr/053.webp)



A fronte di questa evoluzione, i ruoli del nodo Bitcoin e del miner sono diventati chiaramente distinti. Come mostrato sopra, il ruolo di un nodo Bitcoin è puramente informativo e basato sulla convalida. Il ruolo del miner è diverso:




- Seleziona le transazioni in sospeso nella mempool.
- Costruisce un blocco candidato che integra queste transazioni.
- Cerca per tentativi una proof of work valida.
- Se trova una proof of work valida, trasmette il blocco attraverso il proprio nodo agli altri nodi.



Un miner ha bisogno di un nodo Bitcoin per interagire con la rete.



Anche il ruolo del miner è talvolta differenziato da quello del "grind". Un "grind" è una macchina il cui compito è quello di calcolare l'hash dei blocchi modello forniti dal server di una [pool](https://planb.academy/resources/glossary/pool-mining), cercando hash che soddisfino l'obiettivo di difficoltà definito per le "shares", e non quello di Bitcoin. Il resto del processo di mining , che comprende la costruzione dei blocchi veri e propri, la selezione delle transazioni o la ricerca proof-of-work in base alla difficoltà propria di Bitcoin, nonché la distribuzione, viene eseguito direttamente dalle pool.



![Image](assets/fr/054.webp)



Infine, c'è un'importante differenza in termini di incentivo economico tra il miner e il nodo. La gestione di un nodo Bitcoin non fornisce alcun beneficio monetario diretto. D'altro canto, partecipare al mining comporta permette di ottenere delle ricompense (subsidies e transaction fees) per ogni blocco trovato.



Nella seconda parte analizzeremo più in dettaglio i vantaggi pratici e personali dell'installazione e dell'utilizzo di un nodo Bitcoin, al di là di quelli puramente finanziari.



## Bitcoin Core e implementazioni del protocollo


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Il protocollo Bitcoin non è un software: è un insieme di regole tacite condivise tra gli utenti della rete. Definisce le condizioni di validità delle transazioni, i meccanismi di creazione del denaro, il formato dei blocchi, le condizioni del proof-of-work e molte altre specifiche. Per interagire con questo protocollo, gli utenti devono eseguire un software che implementi queste regole: questo è noto come **implementazione** di Bitcoin.



Un'implementazione è quindi un software di nodo: un programma in grado di interfacciarsi con altre macchine del network Bitcoin, di scaricare, verificare, memorizzare e propagare blocchi e transazioni e di applicare localmente le regole di consenso e di relay. Ogni implementazione è un'interpretazione concreta del protocollo, scritta in un determinato linguaggio di programmazione, con una propria architettura, prestazioni ed ergonomia. Ogni implementazione avrà anche una propria organizzazione di sviluppo, con una propria divisione delle responsabilità.



Tra queste implementazioni, una domina di gran lunga: **Bitcoin Core**.



![Image](assets/fr/055.webp)



### Un'implementazione storica che è diventata un punto di riferimento



Bitcoin Core è il software di riferimento per il protocollo Bitcoin. È derivato dal codice originale scritto da Satoshi Nakamoto nel 2008-2009 e ne è la diretta continuazione. Inizialmente conosciuto come "*Bitcoin*", poi "*Bitcoin QT*" (a causa dell'aggiunta di un'interfaccia grafica tramite la libreria Qt), è stato rinominato "*Bitcoin Core*" nel 2014 per differenziare chiaramente il software dal network. Dalla versione 0.5, è stato distribuito con due componenti: `Bitcoin-qt` (l'interfaccia grafica) e `bitcoind` (l'interfaccia a riga di comando).



In teoria, Bitcoin Core non rappresenta il protocollo Bitcoin; piuttosto, è solo un'implementazione tra le tante. Tuttavia, si contraddistingue sugli altri per la sua massiccia adozione, la sua longevità, la robustezza del suo codice e il rigore del suo processo di sviluppo. Di conseguenza, nella pratica, le regole applicate da Bitcoin Core sono di fatto quelle del protocollo Bitcoin: gli utenti, gli sviluppatori, i miner e i servizi dell'ecosistema fanno riferimento quasi esclusivamente ad esso.



### Distribuzione attuale delle implementazioni



Secondo [i dati raccolti nell'agosto 2025 da Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (un noto sviluppatore dell'ecosistema), la distribuzione delle implementazioni tra i nodi pubblici della rete è la seguente:




- **Bitcoin Core**: 87.3% dei nodi
- **Bitcoin Knots**: 12.5
- **Altre implementazioni cumulative**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



In altre parole, circa 9 nodi pubblici su 10 utilizzano Bitcoin Core. Il resto della rete si affida a client più marginali (anche se la quota di Knots è aumentata notevolmente negli ultimi mesi, sopratutto in seguito ai dibattiti sul limite di dimensione del `OP_RETURN`). Queste implementazioni alternative sono spesso gestite da una sola persona o da un piccolo team.



**Nota: ** Queste cifre sono comunque stime, in quanto si basano principalmente sui *nodi in ascolto*, cioè sui nodi che accettano connessioni in entrata (con la porta 8333 aperta). I nodi non in ascolto* sono molto più complessi da contare, poiché è impossibile connettersi direttamente a loro: bisogna aspettare che l'iniziativa arrivi da loro, sotto forma di connessione in uscita. Il sito di Luke Dashjr sostiene di cercare di contare anche questi *nodi non in ascolto*, ma resta impossibile ottenere dati perfettamente precisi su di essi, e l'aggiornamento di queste statistiche è inevitabilmente in ritardo rispetto alla realtà.



### Funzionamento interno del Bitcoin Core



Bitcoin Core è un software scritto in C++. È anche un progetto open source mantenuto da una community di sviluppatori, volontari o retribuiti da varie entità (spesso aziende dell'ecosistema interessate a che lo sviluppo di Core proceda favorevolmente). [Il codice è ospitato su GitHub](https://github.com/bitcoin/bitcoin) e lo sviluppo segue un modello rigoroso:




- I **contributori** presentano proposte sotto forma di _richieste di modifica_ (PR). In linea di principio, chiunque può proporre una modifica, ma quest'ultima deve essere testata, documentata e sottoposta a un processo di revisione paritaria.
- I **maintainer** hanno il diritto di approvare e inglobare le modifiche delle PR nel codice. Sono coloro che garantiscono la coerenza e la stabilità del progetto. Nel luglio 2025, ce n'erano cinque: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao e Ryan Ofsky.
- Dal febbraio 2023 non c'è più un **maintainer principale**. Questo ruolo è stato inizialmente ricoperto da Satoshi Nakamoto quando fu lanciato Bitcoin, poi da Gavin Andresen dopo la partenza di Nakamoto all'inizio del 2011 e infine da Wladimir J. Van Der Laan dal 2014 al 2023.



![Image](assets/fr/057.webp)



Lo sviluppo di Bitcoin Core segue una logica meritocratica: i nuovi collaboratori sono incoraggiati a rivedere e testare il codice prima di proporre modifiche. Le decisioni si basano sul consenso tecnico e le modifiche più importanti (soprattutto nelle aree di consenso) richiedono discussioni a monte su canali pubblici, come le mailing list o i club di revisione delle PR.



### Altre implementazioni di Bitcoin



Anche se marginali in termini di adozione, esistono altri client. Il principale è Bitcoin Knots, sviluppato da Luke Dashjr, un fork di Bitcoin Core che incorpora opzioni aggiuntive e un approccio più conservativo allo sviluppo. Queste includono restrizioni più severe sui formati delle transazioni.



![Image](assets/fr/058.webp)



Possiamo anche citare:




- **Libbitcoin**: una libreria modulare in C++ sviluppata da Amir Taaki e mantenuta da Eric Voskuil;
- **Bcoin**: un'implementazione in JavaScript, non più mantenuta attivamente;
- **BTCD/btcsuite** : un'implementazione in Go.



Questi progetti contribuiscono alla diversità dell'ecosistema, ma la loro adozione rimane molto limitata, rendendo difficile l'evoluzione indipendente di Bitcoin Core.



### Il potere degli sviluppatori Core



Si potrebbe pensare che gli sviluppatori di Bitcoin Core abbiano un controllo diretto su Bitcoin, ma non è così. Non possono imporre una modifica al protocollo. Il loro ruolo è quello di proporre il codice. Spetta a ciascun utente, tramite il proprio nodo, decidere se utilizzare o meno questo codice.



Ciò significa che se una modifica in Bitcoin Core non ottiene il consenso, può essere ignorata dai nodi, non aggiornando Bitcoin Core o semplicemente cambiando l'implementazione. Al contrario, se una funzionalità desiderata dagli utenti viene bloccata nel processo di sviluppo di Core, è sempre possibile passare a un'altra implementazione o fare un fork del progetto.



Come discuteremo più avanti in questo corso, sono i nodi, in base al loro peso nell'economia (cioè i commercianti), a conferire "utilità" a una versione del protocollo (e quindi alla valuta corrispondente), accettando unità che rispettano le sue regole. Il vero potere di governance di Bitcoin, quindi, è mantenuto da questi commercianti, non agli sviluppatori.




# Diventare un bitcoiner sovrano


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Perché gestire il proprio nodo?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



È opinione diffusa che gestire un nodo Bitcoin sia un atto puramente altruistico, senza alcun guadagno personale, al solo servizio della decentralizzazione della rete. Alcuni bitcoiners lo considerano una forma di dovere per sostenere il sistema e mostrare la loro gratitudine a Bitcoin.



Come abbiamo sottolineato nei capitoli precedenti, gestire un nodo non genera un guadagno finanziario diretto. Si potrebbe quindi pensare che non vi sia alcun interesse personale nel farlo. Tuttavia, gestire il proprio nodo offre numerosi vantaggi individuali. Per convincerti, in questo capitolo presenterò tutte le ragioni, sia tecniche che strategiche, che dovrebbero spingerti a installare e utilizzare il tuo nodo Bitcoin personale.



### Diffusione più riservata delle transazioni



Quando il software wallet si collega a un nodo esterno, trasmette le proprie transazioni a un'infrastruttura che non è sotto il tuo controllo. Questo genera ovvi rischi di sorveglianza: l'operatore del nodo remoto può analizzare i dettagli delle tue transazioni, compresi gli importi e le frequenze, e, attraverso un controllo incrociato di alcuni metadati (come indirizzi IP, orari e luoghi), potenzialmente associarli alla tua identità.



Infatti, come sottolineato nel capitolo precedente, i wallet non comunicano con il network Bitcoin per magia; devono connettersi a un nodo per consultare i saldi o trasmettere le transazioni. Se non hai mai creato un tuo nodo, significa che il tuo wallet dipende dall'infrastruttura di una terza parte (di solito l'azienda dietro al software). Questa terza parte, soprattutto se si tratta di un'azienda, può osservare, sfruttare o addirittura divulgare questi dati: per motivi commerciali, per vincoli legali o per pirateria.



![Image](assets/fr/059.webp)



Utilizzando il proprio nodo, si trasmettono le transazioni direttamente al network, evitando gli intermediari. A condizione che il tuo nodo sia protetto in modo adeguato (di cui parleremo più avanti) e che rispetti determinati standard, nessuna informazione viene esposta: né il tuo IP Address né i dettagli delle tue transazioni passano attraverso un'entità che non controllate. Questo è un prerequisito fondamentale per preservare la tua riservatezza su Bitcoin.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Operazioni non censurabili



Per le stesse ragioni menzionate in precedenza, il software wallet basato su un nodo di terze parti è vulnerabile al rischio di censura: l'operatore del nodo remoto può rifiutarsi di trasmettere determinate transazioni per vari motivi. Potrebbe considerarle sospette o contrarie alla propria politica. La transazione può anche essere bloccata se non è conforme alle regole di trasmissione del nodo. Infine, l'operatore potrebbe prendere di mira specificamente il tuo IP Address per bloccare la trasmissione delle vostre transazioni.



Al contrario, utilizzando il proprio nodo, si garantisce la propagazione delle transazioni all'interno della rete peer-to-peer. Ciò significa che si mantiene il controllo totale sulla distribuzione delle transazioni, senza dipendere da un intermediario. Finché la transazione è conforme alle regole di consenso e di relay dei nodi collegati al tuo, sarà trasmessa sulla rete e poi, a condizione che siano incluse quote sufficienti, integrata in un blocco da un miner. Avere un proprio nodo garantisce una conferma delle transazioni neutrale e senza permessi.



### Verifica indipendente dei dati



Senza un nodo personale, si rimane dipendenti da una terza parte per l'accesso alle informazioni come il saldo, lo stato di conferma delle transazioni e la validità dei blocchi. Ciò implica una fiducia implicita nell'accuratezza e nell'integrità del nodo esterno.



![Image](assets/fr/060.webp)



L'utilizzo di un full node consente di verificare personalmente tutte le regole del protocollo, per ogni transazione e per ogni blocco. Di conseguenza, il saldo visualizzato dal tuo wallet non è un dato ricevuto da un server remoto, ma un risultato calcolato localmente da una copia completa della blockchain, convalidato blocco per blocco. Questo approccio dà pieno significato alla massima dei bitcoiners:



> Non fidatevi, verificate.

### Migliore distribuzione della sicurezza del sistema



Ogni nodo che si unisce alla rete rafforza la ridondanza e la resilienza di Bitcoin. Facilita la diffusione delle informazioni e permette a nuovi peer di connettersi tra loro. Senza i nodi, il sistema sarebbe semplicemente inutilizzabile.



Come abbiamo visto, la sicurezza di Bitcoin non si basa sulla decentralizzazione, sul mining o sulla crittografia: come ogni sistema, si basa sugli individui. Più precisamente, dipende dalla capacità degli operatori dei nodi di resistere alla coercizione.



Ciò che distingue i sistemi decentralizzati come Bitcoin è la distribuzione del rischio tra tutti coloro che sono coinvolti nel loro funzionamento. Gestire il proprio nodo Bitcoin significa accettare una parte di questo rischio garantendo la sicurezza della propria istanza; così facendo, si alleggerisce anche il peso del rischio per gli altri operatori del nodo.



Non si tratta quindi di un vantaggio personale diretto: la gestione di un nodo ti rende in parte responsabile della sicurezza del network. È soprattutto un vantaggio collettivo, perché il tuo coinvolgimento contribuisce a diffondere il rischio. A sua volta, aumenta la propria capacità di utilizzare Bitcoin in modo affidabile.



### Approfondire la comprensione del sistema



L'installazione di un full node non è un'operazione banale. Comporta l'installazione del software, la comprensione del funzionamento di base, il monitoraggio della sincronizzazione, l'esame dei log in caso di problemi e l'utilizzo del terminale. Questo ti porterà necessariamente ad approfondire la tua conoscenza del protocollo. Questo è un vantaggio indiretto, ma non trascurabile.



Acquisire questa conoscenza rafforza la fiducia nello strumento e può ridurre il rischio di errori o di esposizione a truffe. Gestire il proprio nodo significa anche imparare.



### Scegliere quali regole applicare



Un aspetto importante, spesso frainteso, è che la gestione di un nodo consente di scegliere le regole da applicare localmente. Esistono due tipi principali di regole:





- **Regole di consenso**:



Queste sono le regole fondamentali del protocollo Bitcoin, che garantiscono l'integrità del sistema e stabiliscono i criteri di convalida delle transazioni e dei blocchi. Qualsiasi transazione non conforme a queste regole di consenso non potrà mai essere inclusa in un blocco valido. Ad esempio, una transazione con una firma non valida su una delle sue voci sarà sistematicamente esclusa.



Cambiare queste regole equivale a cambiare il protocollo, e quindi la moneta ([Hard Fork](https://planb.academy/resources/glossary/hard-fork)). Tuttavia, anche senza cercare di modificarle, il semplice fatto di applicare rigorosamente le regole esistenti conferisce un certo potere: se un blocco viola le regole, il nodo lo rifiuta immediatamente.





- **Regole del Relay**:



Si tratta di regole specifiche per ogni nodo Bitcoin, che vengono aggiunte alle regole di consenso per definire la struttura delle transazioni non confermate accettate nella mempool e trasmesse ai peer. Ogni nodo configura e applica queste regole a livello locale, il che spiega perché possono differire da un nodo all'altro. Esse si applicano solo alle transazioni non confermate: una transazione considerata "non standard" da un nodo sarà accettata solo se compare già in un blocco valido. La modifica di queste regole non esclude il nodo dal sistema Bitcoin.



Ad esempio, una transazione senza commissioni è, secondo le regole del consenso, perfettamente valida, ma sarà rifiutata per impostazione predefinita secondo la politica di relay di Bitcoin Core, perché il parametro `minRelayTxFee` è impostato a `0,00001` (in BTC/kB). Tuttavia, è possibile, sul proprio nodo, abbassare questa soglia per trasmettere transazioni con commissioni inferiori o, al contrario, aumentare il limite, ad esempio, a 2 Sats/vB, per evitare di trasmettere transazioni con commissioni basse.



Far girare il proprio nodo significa affermare che: "Convalido ciò che scelgo di convalidare, secondo le regole che io stesso ho adottato "*. Si diventa così attori della governance del sistema, in grado di rifiutare un'evoluzione che ci sembra inaccettabile o di approvare un aggiornamento secondo i propri criteri.



Possiamo quindi cercare di capire quanto potere avete sulle regole grazie al tuo nodo. L'entità di questo potere dipende dal tipo di regola.



#### Regole del relay



Per quanto riguarda le regole di trasmissione, l'essenziale è semplicemente possedere un nodo, indipendentemente dalla sua attività economica. La posta in gioco è l'accettazione o meno di trasmettere determinati tipi di transazioni.



Se, ad esempio, si ritiene che le transazioni con commissioni inferiori a 1 sat/vB debbano essere accettate su Bitcoin, si può regolare questa regola sul proprio nodo in modo che trasmetta queste transazioni, facilitando così la loro propagazione sulla rete fino a quando un miner non le includa in un blocco valido. In sostanza, quindi, si tratta di una questione di potere sulla diffusione delle transazioni: ogni nodo ha potere decisionale, poiché accettare di trasmettere un tipo di transazione equivale a promuoverne l'accettazione sul network Bitcoin. Di conseguenza, se si gestiscono più nodi, si ha una maggiore influenza sulla politica di rilancio, poiché ogni nodo ha le sue connessioni e le sue aree di impatto sulla rete.



Infatti, avere uno o più nodi configurati con specifiche regole di relay significa determinare quale parte del network accetta di propagare un determinato tipo di transazione. La diffusione di un messaggio in un grafo peer-to-peer, come nel caso delle transazioni Bitcoin, segue la logica della teoria della percolazione. Immaginate ogni nodo come un sito che può essere attivo (`p` = trasmette) o inattivo (`1-p`). Non appena la proporzione `p` supera una soglia critica (`p_c`), emerge una componente gigante: la transazione riesce ad attraversare la rete e ha tutte le possibilità di raggiungere un miner. In un network come Bitcoin, dove ogni nodo mantiene una media di 8 connessioni in uscita, la soglia `p_c` è generalmente fissata a pochi punti percentuali, ancora più bassa se alcuni nodi hanno un numero molto elevato di connessioni.



![Image](assets/fr/061.webp)



Finché `p` rimane al di sotto di `p_c`, una transazione resta confinata in zone isolate e non raggiunge un miner. Non appena questa soglia viene superata, la transazione si diffonde quasi istantaneamente in tutto il network.



In ultima analisi, sono sempre i miner a decidere se includere o meno una transazione in un blocco. Tuttavia, i nodi intervengono a monte influenzando la distribuzione delle transazioni: determinano se i miner saranno o meno a conoscenza di una determinata transazione. Se una transazione non viene trasmessa ai miner, è ovviamente impossibile per loro includerla in un blocco.



L'aggiunta di qualche altro nodo avrà quindi un impatto marginale se la rete è già in fase di percolazione per un determinato tipo di transazione, ma può rivelarsi decisiva quando la soglia di percolazione si avvicina. Possedere o influenzare diversi nodi, soprattutto se ben collegati, può aumentare o ridurre il valore di `p` e, di conseguenza, indirizzare indirettamente le regole di relay che determinano quali transazioni vengono viste e infine accettate dai miner.



#### Per le regole di consenso



Per quanto riguarda l'influenza del tuo nodo sulle regole del consenso, sarà soprattutto il suo peso economico a essere decisivo. Si tratta di un concetto cruciale: il valore di qualsiasi moneta è direttamente correlato alla sua capacità di facilitare lo scambio. Infatti, se un oggetto non è accettato da nessuno per lo scambio di beni o servizi, teoricamente non ha alcuna utilità monetaria. Ad esempio, se nessun commerciante accetta i sassolini come mezzo di pagamento, essi non hanno alcuna utilità come denaro. Naturalmente, l'utilità rimane una nozione soggettiva su scala individuale, ma in un dato territorio, maggiore è il numero di commercanti che accettano un oggetto come mezzo di pagamento nello scambio, più è probabile che questo oggetto abbia un'utilità monetaria per le persone che vivono in questo territorio.



Prendiamo l'esempio di un villaggio in cui molti mercanti accettano oro in cambio delle merci: è probabile che l'oro abbia un'utilità monetaria per gli abitanti del villaggio. Ciò indica che l'utilità di una moneta dipende direttamente dalle decisioni dei mercanti di accettarla o rifiutarla.



Questo concetto è fondamentale per capire le dinamiche di potere in gioco nel sistema Bitcoin. Satoshi lo dice chiaramente: Bitcoin è un sistema di denaro elettronico; in altre parole, fornisce un servizio che offre una forma di valuta, bitcoin (o BTC). Quando le regole del protocollo vengono modificate in modo non retrocompatibile (Hard Fork), ciò equivale a creare un nuovo sistema e quindi una nuova valuta. Il successo o il fallimento di questo fork dipende dalle dimensioni della sua economia, che a sua volta è determinata dal numero di commercianti che accettano questa nuova forma di valuta.



![Image](assets/fr/062.webp)



Facciamo un esempio: supponiamo che Bitcoin subisca un hard fork. Ci sarebbero quindi 2 forme distinte di valuta: BTC-1 (la versione originale, invariata) e BTC-2 (la nuova valuta con regole di consenso diverse). Se tutti i commercianti che accettano BTC-1 continuano a farlo, ma rifiutano BTC-2, quest'ultimo avrà, in teoria, un'utilità monetaria molto limitata. Come utente, non avrei alcun interesse a conservare e utilizzare il BTC-2, sapendo che nessun commerciante lo vorrebbe per lo scambio di beni o servizi. Al contrario, se il 50% dei commercianti sceglie di accettare esclusivamente BTC-2 e il restante 50% accetta solo BTC-1, allora l'utilità di BTC-1 sarà, in teoria, dimezzata. Uso il termine "in teoria" perché l'utilità rimane soggettiva a livello individuale e dipende da una moltitudine di fattori (come il territorio e le abitudini di consumo) difficili da comprendere caso per caso.



In Bitcoin, il ruolo di "commerciante", è inteso come qualsiasi entità con un certo peso economico, comprende ovviamente le imprese (negozi fisici, siti di vendita online, fornitori di servizi, ecc.), ma anche le piattaforme Exchange, poiché accettano Bitcoin in cambio di altre valute, e i miner, poiché accettano Bitcoin tramite commissioni in cambio del servizio di inclusione di una transazione in un blocco.



Per quanto riguarda le regole del consenso, il tuo nodo ti permette di indirizzare la tua attività economica verso una valuta o un'altra. Ad esempio, se avete 10 full node a casa, ma nessuna attività economica significativa, la vostra influenza durante un fork sarà quasi nulla. Al contrario, un singolo nodo utilizzato per gestire una catena di 200 negozi che accettano Bitcoin conferisce un peso economico significativo.



Non è quindi il numero di nodi che conta, ma l'importanza dell'attività economica che essi supportano. Inoltre, se la tua attività economica dipende da un nodo che non controllate, il suo proprietario deciderà quale valuta utilizzare, finché rimarrai connesso a quel nodo. Ecco perché gestire e utilizzare il proprio nodo è particolarmente importante nel contesto della governance del sistema:



> Non è il tuo nodo, non sono le tue regole.


## I diversi tipi di nodi Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Un nodo Bitcoin è, quindi, una macchina che esegue un'implementazione del protocollo Bitcoin. Dietro questa definizione comune di nodi, esistono diverse configurazioni possibili, non tutte in grado di offrire lo stesso livello di autonomia, consumo di risorse e utilità per il network. In questo capitolo cercheremo di capire queste differenze per aiutarvi a scegliere un'architettura di nodi adatta all'uso e ai vincoli hardware.



### Il full node



Un full node è semplicemente un nodo Bitcoin che scarica l'intera blockchain dal blocco genesis, convalida ogni blocco in modo indipendente e memorizza la storia di tutta la blockchain a livello locale. Questa è la forma "normale" di un nodo Bitcoin, come immaginato da Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Il full node non ha bisogno di fidarsi di nessuno perché convalida e conosce tutte le informazioni del sistema. È il tipo di nodo che offre le maggiori garanzie: sa, senza affidarsi a terzi, se un pagamento è valido, se un blocco è valido, se una riorganizzazione è legittima e così via.



In pratica, un full node richiede risorse non banali, tra cui diverse centinaia di gigabyte per i file a blocchi, un processore in grado di convalidare gli script, RAM per la mempool e le cache, e una larghezza di banda stabile. La prima sincronizzazione (*[IBD](https://planb.academy/resources/glossary/initial-block-download-ibd)*) legge e verifica l'intera cronologia: è intensa, ma avviene una sola volta. Un full node partecipa attivamente al network, trasmettendo blocchi e transazioni, e può accettare connessioni in entrata per assistere altri peer.



A seconda delle esigenze, è possibile aggiungere un indicizzatore al full node. Bitcoin Core offre l'indicizzazione delle transazioni come funzione opzionale (disattivata per impostazione predefinita), che può essere utile per scopi specifici. Tuttavia, non include un indicizzatore di indirizzi, che spesso è la funzione più richiesta dai singoli utenti. Per ovviare a questo problema, è possibile installare sul proprio nodo un software dedicato, come Electrs o Fulcrum, per velocizzare le interrogazioni di verifica del saldo dell'indirizzo da parte degli UTXO associati. Torneremo sul ruolo dell'indicizzatore in modo più dettagliato in un capitolo a parte.



### Il nodo pruned



Il pruned node convalida tutto come un full node, dal blocco genesis alla testa della catena con il maggior lavoro, ma **conserva solo la parte più recente del file dei blocchi**. Una volta che i vecchi blocchi sono stati controllati, li cancella gradualmente per rimanere al di sotto di un limite di spazio impostabile. Questa configurazione è ideale se si hanno vincoli di spazio su disco: si mantiene l'indipendenza della convalida dei blocchi, senza memorizzare l'archivio storico completo della blockchain. Questa opzione è particolarmente utile se si desidera semplicemente installare Bitcoin Core sul proprio computer, senza utilizzare un dispositivo dedicato.



![Image](assets/fr/064.webp)



Le implicazioni tecniche di questa opzione sono abbastanza semplici: il pruned node è perfettamente in grado di trasmettere le transazioni, partecipare al relay, verificare blocchi e transazioni e tracciare la catena. D'altra parte, non può servire come fonte di dati storici oltre i suoi limiti per altre applicazioni (ad esempio, esploratori completi, indicizzatori, wallet). Le funzioni che richiedono l'archivio (o un indice globale) non saranno quindi disponibili.



In pratica, è possibile utilizzare un pruned node per collegare un software di gestione del wallet come Sparrow wallet. Tuttavia, non sarà possibile eseguire la scansione delle transazioni sul wallet che sono precedenti al limite del prune. Ad esempio, se si ha una transazione registrata nel blocco 901 458, ma il nodo conserva solo i blocchi da 905 402 in su (perché i più vecchi sono stati cancellati tramite il prune), non sarà possibile eseguire la scansione di questa transazione. D'altra parte, se l'hai già scansionata quando il tuo nodo aveva ancora questa altezza di blocco, il tuo software di gestione wallet memorizzerà le informazioni e visualizzerà correttamente il saldo degli UTXO corrispondenti.



In breve, il tracciamento del wallet funziona senza problemi su un pruned node se si crea un nuovo wallet mentre il software è già collegato a quel nodo. D'altra parte, si possono incontrare difficoltà se si ripristina un vecchio wallet, poiché le transazioni passate che non sono più conservate dal nodo non saranno ovviamente recuperabili.



### Il nodo leggero / SPV



Un nodo [SPV](https://planb.academy/resources/glossary/spv-node-light-node) (*Simplified Payment Verification*), o nodo leggero, conserva solo le intestazioni dei blocchi, non i dettagli delle transazioni, e si affida ad altri full node per ottenere la prova che una transazione si trova in un blocco (tramite [Merkle](https://planb.academy/resources/glossary/merkle-tree) proofs trees) di cui possiede l'intestazione. Il concetto di verifica semplificata dei pagamenti non è nuovo, essendo stato proposto dallo stesso Satoshi Nakamoto nella parte 8 del White Paper.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Un sistema di contanti elettronici Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf



Questo tipo di nodo è ovviamente molto più leggero in termini di memoria e di utilizzo della CPU rispetto a un nodo full node o addirittura a un pruned node. Il nodo SPV è quindi adatto ai dispositivi più piccoli e alle connessioni intermittenti. Infatti, viene spesso integrato direttamente nei wallet, in particolare nei software mobile come l'app Blockstream.



Il compromesso è la fiducia e la riservatezza: un client SPV non controlla autonomamente gli script o le politiche di convalida; presume che la blockchain con il maggior numero di PoW (proof of work) sia valida e dipende da uno o più full node per le risposte. L'utilizzo di questo tipo di nodo è quindi un'opzione migliore rispetto alla connessione a un nodo di terze parti; tuttavia, è ancora meno vantaggioso rispetto a un full o pruned node.



![Image](assets/fr/065.webp)



### Quale nodo per quale esigenza?





- Utente mobile / principiante



Per un utente alle prime armi con un semplice wallet su un'applicazione mobile, l'uso di un nodo SPV è sicuramente il modo migliore per iniziare. L'installazione è rapida, richiede poche risorse e l'esperienza è semplice e fluida. Ciò significa che è possibile verificare da soli alcune informazioni e, quindi, fare meno affidamento sui nodi di terze parti e allo stesso tempo essere più indipendenti quando si tratta di trasmettere le transazioni.





- PC / utente intermedio



Un utente intermedio con un PC può installare un pruned node per beneficiare di quasi tutti i vantaggi di un full node, senza sovraccaricare il proprio computer su base giornaliera: convalida completa, utilizzo moderato del disco e manutenzione semplice. È una soluzione ideale per collegare i wallet desktop e rimanere indipendenti nella distribuzione delle transazioni, senza investire in un dispositivo dedicato o sovraccaricare lo spazio su disco.





- Bitcoiner sovrano / avanzato



Un full node rimane la soluzione migliore se si vuole essere totalmente indipendenti nell'uso di Bitcoin, e in seguito non trovarsi limitati da usi avanzati come un indicizzatore, un nodo [Lightning](https://planb.academy/resources/glossary/lightning-network) o addirittura un block explorer. Questo è esattamente ciò che esploreremo in questo corso!



## Panoramica delle soluzioni software


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Dal punto di vista del software, esistono due modi principali per gestire un nodo Bitcoin:




- installare direttamente un'implementazione del protocollo, come Bitcoin Core (consigliato) o Bitcoin Knots,
- oppure utilizzare una distribuzione "chiavi in mano" (spesso chiamata "_node-in-a-box_") che integri un'implementazione di Bitcoin allo stesso modo, ma che includa anche un sistema con interfaccia da amministratore, un archivio di applicazioni e strumenti pronti all'uso (Lightning, browser, index server, persino applicazioni self-hosting esterne a Bitcoin...).



Entrambi gli approcci portano allo stesso obiettivo: avere un proprio nodo, ma differiscono in termini di installazione e utilizzo di interfaccia, manutenzione, espandibilità e costi. Nel corso di questo capitolo analizzeremo questi aspetti.



### Implementazioni grezze del nodo Bitcoin



Installare un'implementazione grezza significa utilizzare direttamente il software di un'implementazione del protocollo Bitcoin (come Core), senza alcun software Layer aggiuntivo. L'utente gestisce autonomamente la configurazione, gli aggiornamenti e i servizi associati (indicizzazione, API, Lightning, backup, ecc.), in base alle proprie esigenze.



Questo è l'approccio più sovrano e flessibile: si sa esattamente cosa sta funzionando, dove si trovano i dati e come funziona tutto. D'altra parte, diventa più complesso quando si vuole andare oltre il semplice funzionamento di un nodo Bitcoin. Se l'obiettivo è solo quello di avere un nodo, la complessità è paragonabile a quella di un "node in a box", o anche meno, poiché si tratta semplicemente di installare un software.



#### Bitcoin Core (client maggiormente usato)



[Bitcoin Core](https://bitcoincore.org/) è il client maggiormente usato dalla rete. Scarica, convalida e mantiene la blockchain, fornisce API [RPC](https://planb.academy/resources/glossary/rpc-remote-procedure-call)/REST e può integrare un wallet. Se si preferiscono strumenti standard e ci si sente a proprio agio nell'aggiungere servizi (come il server Electrum, explorer e LND), è meglio usare Core così com'è.



**Vantaggi:** Massima stabilità, comportamento prevedibile, esperienza grezza, facile da installare e configurare.



**Svantaggi:** È necessario costruire manualmente il resto dello stack per creare un ambiente applicativo completo, piuttosto che un semplice nodo Bitcoin.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (client alternativo principale)



[Bitcoin Knots è un Fork di Bitcoin core](https://bitcoinknots.org/), mantenuto da Luke Dashjr. È il principale client alternativo a Core per l'implementazione del protocollo Bitcoin. Pienamente compatibile con il resto della rete (non è assolutamente un hard fork come Bitcoin Cash), offre tuttavia caratteristiche aggiuntive, tra cui opzioni di politica di relay assenti in Core o applicate in modo più rigoroso per impostazione predefinita per limitare ciò che alcuni considerano spam.



Ci sono due possibili ragioni per scegliere Knots rispetto a Core:




- **Tecniche**: Opzioni diverse da Core, in particolare in termini di gestione dei relay, determinando quali transazioni vengono accettate e trasmesse dal proprio nodo.
- **Politica**: Alcune persone preferiscono usare client alternativi come Knots per ragioni non tecniche, in particolare per supportare un'alternativa a Core e quindi ridurre il suo monopolio. Se Core fosse mai compromesso, sarebbe utile non solo avere client alternativi solidi e ben mantenuti, ma anche sapere come utilizzarli efficacemente. Altri usano Knots per protesta, perché hanno perso fiducia negli sviluppatori di Core o disapprovano la maggior parte della gestione del client.


https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Personalmente, ti consiglio di scegliere Core, soprattutto per beneficiare più rapidamente delle patch di sicurezza. Infatti, alcune vulnerabilità scoperte in Knots vengono corrette con un certo ritardo. Più in generale, il processo di sviluppo di Core è solidamente strutturato e supportato da un gran numero di collaboratori, mentre Knots è mantenuto da una sola persona e ha una comunità molto più piccola. D'altra parte, le regole di relay tendono a perdere la loro utilità oggi, soprattutto quando sono applicate solo da una piccola frazione del network (come per la teoria della percolazione).



### Distribuzioni Node-in-a-box



Il _node-in-a-box_ combina Bitcoin Core (o Knots) con un sistema operativo preconfigurato, un'interfaccia web e un App Store di servizi di self-hosting (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, ecc.) Con un solo clic è possibile installare, aggiornare e interconnettere questi diversi moduli.



È una soluzione molto più semplice per l'avvio e la gestione di numerose applicazioni accessorie su base giornaliera. Il rovescio della medaglia è che quando si verifica un problema (ad esempio, un conflitto con l'immagine Docker, un aggiornamento errato, un database danneggiato), il debugging può diventare molto complesso, poiché si dipende dall'integrazione della distribuzione stessa. Inoltre, il supporto ufficiale o della community è spesso complicato.



Quindi, un node-in-a-box è estremamente facile da usare finché tutto funziona correttamente, ma in caso di bug bisogna essere pronti a fare lunghe ricerche, ad aspettare aiuto e a sporcarsi le mani.



La maggior parte di queste soluzioni è disponibile in due formati:




- Dispositivo preassemblato: un computer completo con il sistema operativo già installato. Questi dispositivi pay-as-you-go devono semplicemente essere collegati alla rete elettrica e a Internet per essere operativi. Se il tuo budget lo consente, questa opzione ha il vantaggio di essere molto semplice da configurare, di offrire spesso un'assistenza prioritaria e di contribuire al finanziamento dello sviluppo, dato che il modello di business di queste aziende si basa generalmente sulla vendita di hardware.
- Fai da te: installare il sistema operativo della distribuzione sul proprio dispositivo (vecchio PC, NUC, Raspberry Pi, server domestico...). Questa è la soluzione più economica, in quanto si può riciclare un vecchio dispositivo o scegliere un hardware che corrisponda esattamente alle proprie esigenze e al proprio budget. È anche l'opzione più flessibile e più soddisfacente da configurare. È questo l'approccio che esploreremo nella parte pratica del corso.



Ecco una panoramica delle principali soluzioni node-in-a-box disponibili (nel 2025):



### Umbrel (umbrelOS e Umbrel Home)



[Oggi Umbrel è il leader delle soluzioni node-in-a-box (https://umbrel.com/). Il suo successo è dovuto in gran parte alla semplicità di installazione (quando è stato lanciato su un semplice Raspberry Pi), la sua interfaccia elegante e intuitiva, e a un ecosistema di applicazioni che è cresciuto rapidamente ed è ora estremamente esteso.



![Image](assets/fr/067.webp)



Lanciato nel 2020 come semplice nodo Bitcoin accompagnato da alcune applicazioni accessorie, Umbrel si è gradualmente evoluto in un cloud domestico moderno e completo.



Non entrerò nel dettaglio di come funziona e delle sue caratteristiche specifiche, perché le esamineremo in modo più approfondito nel primo capitolo della prossima parte. Infatti, per gli scopi di questo corso BTC 202, ho scelto di utilizzare UmbrelOS, che ritengo sia la migliore soluzione node-in-a-box attuale per gli utenti principianti e intermedi.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 offre StartOS (https://start9.com/), un sistema progettato per il "sovereign computing": l'obiettivo è che ognuno possieda e gestisca il proprio server privato, arricchito da un mercato di applicazioni self-hosted. È possibile acquistare un server Start9 (Server One a 619 dollari, Server Pure a 899 dollari) o assemblarlo in modalità DIY sul proprio dispositivo.



Sul lato Bitcoin, StartOS consente di installare un full node, un nodo Lightning, un server BTCPay, Electrs e molti altri servizi. Tuttavia, il fascino di Start9 va oltre: offre la possibilità di scoprire, configurare ed esporre vari software (file cloud, messaggistica, monitoraggio) in modo unificato, con un controllo completo. Il progetto si rivolge quindi agli utenti che desiderano una solida piattaforma di self-hosting, non solo un semplice nodo Bitcoin. È probabilmente l'ecosistema più completo dopo Umbrel.



![Image](assets/fr/068.webp)



La differenza principale con Umbrel sta nell'interfaccia . Umbrel si basa su un'interfaccia utente molto curata, mentre Start9 offre un'interfaccia più semplice e funzionale. L'ecosistema di applicazioni di Start9 è meno ricco di quello di Umbrel, ma compensa con diversi vantaggi tecnici: l'accesso alle impostazioni avanzate delle applicazioni è semplificato, mentre Umbrel diventa rapidamente restrittivo se l'opzione desiderata non è fornita dall'interfaccia. Start9 eccelle anche nella gestione dei backup: a parte l'efficiente soluzione di Umbrel per il LND, non esiste un meccanismo unificato, a differenza di Start9. Inoltre, offre strumenti di monitoraggio più accessibili e una connessione remota criptata (`https`), mentre l'accesso locale a Umbrel avviene tramite `http`.



In breve, se hai semplicemente bisogno delle applicazioni essenziali per Bitcoin, senza particolare interesse per il ricchissimo ecosistema di Umbrel, e se la user interface(interfaccia utente) non è una priorità, allora Start9 è un'opzione migliore. Altrimenti, Umbrel è la scelta migliore.



https://planb.academy/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode è una distribuzione focalizzata esclusivamente su Bitcoin e Lightning](https://mynodebtc.com/), che offre una web interface, un marketplace di applicazioni e aggiornamenti con un solo clic. È possibile acquistare hardware pronto all'uso (*Modello Due* disponibile a 549 dollari) o installare MyNode gratuitamente sul proprio dispositivo. Il progetto offre anche una versione *premium* del software (94 dollari), che include supporto prioritario e funzioni avanzate.



![Image](assets/fr/069.webp)



In pratica, MyNode riunisce tutti gli elementi di base necessari per il funzionamento di un full node, nonché le applicazioni essenziali per gli utenti di Bitcoin. Pertanto, è una soluzione adatta se non si richiedono applicazioni esterne all'ecosistema Bitcoin, come le applicazioni self-hosted presenti nei sistemi Start9 e Umbrel.



https://planb.academy/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz è un progetto 100% open source](https://docs.raspiblitz.org/) (licenza MIT) per montare un nodo Bitcoin e un nodo Lightning su un Raspberry Pi. È sufficiente scaricare l'immagine di sistema, avviarla e seguire la procedura guidata per avere un nodo funzionante sul proprio Raspberry Pi. I kit preassemblati sono disponibili anche presso terzi, di solito tra i 300 e i 400 dollari, a seconda dell'hardware. RaspiBlitz offre anche una serie di applicazioni aggiuntive, facili da installare.



![Image](assets/fr/070.webp)



Se possiedi un Raspberry Pi, questa è un'opzione eccellente, poiché i sistemi più completi come Umbrel stanno diventando sempre più pesanti per questo tipo di mini-PC.



https://planb.academy/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo è un node-in-a-box incentrato sulla privacy](https://wiki.ronindojo.io/en/home) che automatizza la distribuzione di Samurai Dojo e Whirlpool, con un Interface dedicato e plugin specificamente progettati per l'ecosistema Samurai.



Il principio è semplice: se utilizzi Ashigaru Wallet (il successore fork di Samurai Wallet, in seguito all'arresto dei suoi sviluppatori) o se vuoi beneficiare di strumenti avanzati per la privacy, RoninDojo fa per te.



![Image](assets/fr/071.webp)



In precedenza il progetto offriva un dispositivo preconfigurato chiamato "Tanto", ma attualmente non è disponibile. Potrebbe tornare in un secondo momento. Nel frattempo, è possibile installare facilmente RoninDojo su un Rock5B+ o Rockpro64, o anche indirettamente su un Raspberry Pi.



https://planb.academy/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Un'altra soluzione [node-in-a-box è Nodl](https://www.nodl.eu/). Come per i progetti precedenti, è possibile acquistare l'hardware preconfigurato (tra 599 e 799 euro, a seconda del modello) o installarlo da soli in modalità fai-da-te.



Per quanto riguarda il software, Nodl integra Bitcoin Core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, nonché BTC RPC Explorer, tutti con una catena di aggiornamento integrata e un codice open-source sotto licenza MIT.



![Image](assets/fr/072.webp)



Dopo aver esplorato le varie soluzioni software, è ora il momento di scegliere il dispositivo che ospiterà il nodo!




## Panoramica delle soluzioni hardware


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Dopo aver esplorato tutte le possibilità software, concentriamoci sull'hardware necessario per il nodo. Ti fornirò alcuni consigli concreti sulla scelta dei componenti, insieme a configurazioni adatte a diversi budget. Naturalmente, questa è la mia opinione personale e il mio feedback: ci sono sicuramente altre alternative rilevanti oltre a quelle presentate qui. Inoltre, non intendo rivisitare i dispositivi preassemblati offerti dai progetti node-in-a-box, che abbiamo già trattato nel capitolo precedente. Qui ci concentreremo esclusivamente sulle soluzioni fai-da-te.



### Hai davvero bisogno di una macchina dedicata?



Negli ultimi anni, i bitcoiners sono diventati sempre più consapevoli di un'idea sbagliata comune, in particolare con la diffusione dei node-in-a-box nei primi anni 2020: un nodo Bitcoin deve necessariamente funzionare su un dispositivo dedicato esclusivamente a questo scopo. Ma questo non è vero. Non serve necessariamente un computer dedicato per far funzionare un nodo Bitcoin: Bitcoin Core è perfettamente in grado di funzionare sul PC di tutti i giorni. Se si dispone di spazio su disco sufficiente per la blockchain o si abilita il pruning, è possibile convalidare la catena, collegare il wallet e persino chiudere il programma quando si è finito di usarlo. Il vantaggio di questo approccio è notevole: zero investimenti iniziali e minima complessità.



![Image](assets/fr/074.webp)



Detto questo, l'utilizzo di un dispostivo dedicato è spesso più comodo. Può funzionare ininterrottamente (24 ore su 24, 7 giorni su 7), essere accessibile da remoto in qualsiasi momento, senza monopolizzare le risorse della macchina principale e, soprattutto, isolare gli utilizzi (una buona pratica di sicurezza: se il tuo PC personale ha un problema, il tuo nodo continua a funzionare e viceversa). Quindi la domanda non è "Ho bisogno di un dipositivo apposito?", ma piuttosto "Ho bisogno di un nodo che sia costantemente online, accessibile da altri dispositivi e in grado di evolversi?" (Lightning, indicizzatori, applicazioni aggiuntive...). Se la risposta è sì, optare per un dispositivo separato renderà le cose molto più semplici.



### 3 metodi di acquisizione: riciclaggio, usato e nuovo



#### Riciclare un vecchio PC



È la soluzione più economica. La maggior parte di noi ha un vecchio PC che raccoglie polvere a casa, o presso amici e familiari: questa è l'occasione perfetta per rimetterlo in funzione! Per adattarlo all'uso come nodo Bitcoin, basta aggiungere un SSD da 2 TB e, a seconda delle esigenze, sostituire o aggiungere barre di RAM per aumentare la RAM. Per un dispositivo completamente funzionante è necessario sborsare tra i 100 e i 200 euro.



Prima di acquistare qualsiasi hardware, verificare il numero di slot per dischi disponibili, il tipo di connessione (M.2 o SATA), il formato della RAM (SODIMM o DIMM) e la sua generazione (DDR4, ecc.). Si dovrebbe anche cogliere l'occasione per pulire il dispositivo, in particolare la ventola, per garantire prestazioni ottimali.



Attenzione, però, se si utilizza un computer portatile: la batteria può diventare un problema con il passare del tempo (per saperne di più, vedi il capitolo successivo).



#### Ricondizionato o usato



Il mercato è pieno di mini-PC aziendali ricondizionati come *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* o *Dell OptiPlex Micro*. Questi dispositivi sono solidi, compatti, silenziosi ed efficienti dal punto di vista energetico. Il loro prezzo è ben al di sotto del nuovo ed è facile trovare modelli dotati di processori i5/i7 di 6a-10a generazione e di 8-16 GB di RAM, il tutto a prezzi molto interessanti, generalmente compresi tra 70 e 200 euro, a seconda della configurazione. A mio parere, questa è probabilmente l'opzione migliore se si cerca un dispositivo apposito per il nodo Bitcoin.



![Image](assets/fr/075.webp)



È anche possibile trovare PC e portatili usati di qualche anno fa, con configurazioni interessanti e un ottimo rapporto qualità-prezzo.



**Nota: ** i computer delle flotte aziendali, come il *ThinkCentre Tiny*, sono spesso dotati solo di una porta *DisplayPort* (DP) per lo schermo, senza uscita HDMI. Non dimenticarti quindi di portare con te un adattatore o un cavo da DP a HDMI, se ne hai bisogno.



#### Acquisto del nuovo



Se il tuo budget lo consente, puoi anche optare per un nuovo dispostivo. Si tratta di una buona opzione se si vuole disporre di hardware recente con buone prestazioni, soprattutto se si intende utilizzare Umbrel o Start9 con applicazioni aggiuntive al di fuori dell'ecosistema Bitcoin per il self-hosting.



### Che tipo di dispositivo devo scegliere?



#### Mini-PC "NUC" / barebone



I mini-PC, a mio avviso, offrono il miglior compromesso per ospitare un nodo Bitcoin a casa. Sono poco ingombranti, si adattano facilmente a uno scaffale, consumano poca energia e si prestano a facili modifiche hardware, come l'aggiunta di RAM o la sostituzione dell'SSD.



Personalmente, preferisco i *Lenovo ThinkCentre Tiny*, molto diffusi sul mercato dell'usato (da flotte aziendali); sono particolarmente robusti e facili da modificare. Naturalmente esistono molti equivalenti di altri produttori: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*....



![Image](assets/fr/001.webp)



**Evidenze:** ingombro ridotto, consumo energetico moderato, bassa rumorosità, scalabilità (a seconda del modello) e affidabilità.



**Punti deboli:** leggermente più costoso di un SBC tipo Raspberry Pi, assenza di schermo integrato (accesso remoto o tramite monitor esterno), assenza di batteria (spegnimento improvviso in caso di interruzione di corrente).



#### Computer portatile dedicato



È un'ottima alternativa a basso costo al mini-PC: oggi si possono trovare portatili usati o addirittura nuovi a prezzi bassi, dotati di processori decenti, numerose porte, nonché di schermo e tastiera integrati (molto pratici per la prima installazione). Soprattutto, la batteria funge da UPS(Uninterruptible Power Supply/gruppo di continuità) naturale: in caso di interruzione di corrente, il nodo non si spegne bruscamente e può rimanere operativo anche per diverse ore.



![Image](assets/fr/076.webp)



**Punti forti:** La batteria funge da UPS (nessun blackout), l'installazione è semplificata grazie al display e alla tastiera integrati, alla scheda Wi-Fi integrata e all'ampia scelta di mercati dell'usato e del nuovo (il che significa che spesso è possibile negoziare i prezzi).



**Punti deboli:** consumo di energia leggermente superiore a quello di un mini-PC nudo, usura graduale della batteria in caso di funzionamento 24/7 con perdita di capacità, rischio raro ma reale di rigonfiamento della batteria o di fuga termica con l'età. È soprattutto questo aspetto che mi fa considerare il mini-PC un'opzione migliore del portatile: il graduale degrado della batteria e i rischi associati.



Se scegli questa soluzione, ti consiglio di tenere sotto controllo le condizioni della batteria per evitare qualsiasi pericolo. Osserva il calore eccessivo, gli odori insoliti, l'instabilità o la deformazione dell'involucro. In caso di allarme, spegnere e scollegare immediatamente il computer, quindi smaltire la batteria presso un centro di riciclaggio specializzato.



**Suggerimento:** Se il BIOS/UEFI o lo strumento del produttore lo consentono, impostare un limite di carico (ad esempio, 60% o 80%) per prolungare la durata della batteria.



#### Raspberry Pi e altri SBC: l'idea sbagliata



All'inizio degli anni 2020, con l'ascesa del software node-in-a-box, è emersa anche la mania del Raspberry Pi come mezzo per far funzionare un nodo Bitcoin. L'idea sembrava attraente: economica, compatta e accessibile.



![Image](assets/fr/073.webp)



In pratica, se l'obiettivo è solo quello di eseguire un nodo Bitcoin senza applicazioni aggiuntive, un Raspberry Pi può essere sufficiente. Ma non appena si desidera utilizzare Umbrel, Start9 o un ecosistema più ricco (block explorer, indicizzatore di indirizzi, nodo Lightning, applicazioni self-hosting...), il dispositivo raggiunge rapidamente i suoi limiti.



Il Raspberry Pi presenta una serie di svantaggi:




- processori troppo sottili, con un'architettura ARM che a volte è incompatibile con alcuni software o richiede una maggiore gestione;
- RAM saldata, impossibile da aggiornare, con configurazioni limitate (spesso un massimo di 8 GB);
- box esterni per SSD collegati via cavo, frequenti fonti di bug, che richiedono l'acquisto di una scheda specifica per un SSD stabile;
- tendenza a riscaldarsi rapidamente e difficoltà a garantire il corretto raffreddamento;
- necessità di acquistare hardware aggiuntivo (case, ventola, scheda SSD, ecc.);
- connettività molto limitata.



Storicamente, il grande vantaggio degli SBC come il Raspberry Pi era il loro prezzo: per poche decine di euro si poteva avere un dispositivo dedicato. Tuttavia, oggi i prezzi sono aumentati notevolmente e, una volta aggiunto tutto l'hardware aggiuntivo essenziale, il costo si avvicina a quello dei primi mini-PC x86 usati o ricondizionati che, a mio parere, offrono molti più vantaggi. Per questo motivo, non consiglio di optare per un SBC.



### Selezione dei componenti



#### Archiviazione su disco: SSD obbligatorio, minimo 2 TB



Tecnicamente, è possibile far funzionare un nodo Bitcoin su un HDD. Il problema è che tutto rallenterà notevolmente, soprattutto l'IBD, che diventerà estremamente lungo a causa dell'uso intensivo del disco come cache da parte di Bitcoin Core (soprattutto per l'UTXO set). Per questo motivo sconsiglio vivamente l'uso di un HDD: crea un vero e proprio collo di bottiglia, limita fortemente l'evoluzione futura (ad esempio, per un nodo Lightning) e può persino portare a un disallineamento della sincronizzazione con la blockchain. Inoltre, lo stress costante sul disco meccanico aumenta il rischio di usura prematura.



Le unità SSD cambiano radicalmente l'esperienza dell'utente: tutto diventa più veloce e fluido, con un'affidabilità di gran lunga superiore. L'uso di un'unità SSD è quindi (quasi) obbligatorio per il vostro nodo e non te ne pentirai, soprattutto perché i modelli ad alta capacità sono ora relativamente accessibili.



![Image](assets/fr/077.webp)



In termini di capacità, 2 TB si stanno gradualmente affermando come il nuovo minimo ragionevole. Nell'estate del 2025, la blockchain si sta già avvicinando ai 700 GB e se si aggiungono Umbrel, un indicizzatore di indirizzi e alcune applicazioni, un'unità SSD da 1 TB si saturerà rapidamente. Con 2 TB si ha un margine confortevole per gli anni a venire (in una stima di massima, tra i 5 e i 15 anni). Si può anche optare per 4 TB se si prevede di utilizzare molte applicazioni su Umbrel, di archiviare file di grandi dimensioni in self-hosting o se si desidera anticipare le esigenze di spazio su disco in larga misura.



![Image](assets/fr/078.webp)



Per quanto riguarda il formato, dipende dalle porte disponibili sulla vostra macchina; tuttavia, se possibile, vi consiglio di utilizzare un'unità SSD M.2 NVMe.



#### Memoria (RAM): da 8 a 16 GB



Per il solo Bitcoin Core (senza sovrapposizione di Umbrel), le raccomandazioni degli sviluppatori indicano un minimo di 256 MB di RAM con le impostazioni regolate al minimo, 512 MB con le impostazioni predefinite e 1 GB per l'uso normale.



D'altra parte, se si utilizza un sistema node-in-a-box come Umbrel o Start9, i requisiti di RAM sono significativamente più elevati. Gli sviluppatori di Umbrel raccomandano un minimo di 4 GB di RAM. Questo potrebbe essere sufficiente per eseguire solo Core, ma sarai presto limitato. Pertanto raccomandano 8 GB, che considero il minimo per una configurazione di base intorno a Bitcoin (Core, LND, indexer e alcune applicazioni). Secondo la mia esperienza, con Umbrel e alcuni servizi aggiuntivi, 8 GB sono ancora un po' pochi. Per essere davvero tranquillo e avere un po' di margine, consiglierei 16 GB di RAM.



#### Processore (CPU)



Per un nodo Umbrel, il requisito minimo è un processore dual-core a 64 bit di Intel o AMD. Se si desidera utilizzare alcune applicazioni oltre a Bitcoin Core, un quad-core (o superiore) farà la differenza in termini di fluidità. Ad esempio, i processori i5/i7 dalla sesta alla decima generazione sono ottime opzioni sul mercato dell'usato.



### Esempi di configurazioni concrete



Di seguito, propongo tre configurazioni concrete, adatte a diversi budget ed esigenze, con modelli precisi a supporto. Queste scelte sono fornite come esempi per illustrare le informazioni contenute in questo capitolo; non siete obbligati a scegliere esattamente questi modelli. Poiché ritengo che il mini-PC sia l'opzione migliore a lungo termine, mi affiderò a questo formato per le tre configurazioni proposte.



*I prezzi indicati di seguito sono puramente indicativi e possono variare a seconda della regione, del fornitore e del periodo*



Innanzitutto, è necessario un SSD abbastanza grande da ospitare la blockchain, pur lasciando spazio di manovra. Le unità SSD hanno una durata limitata in termini di cicli di scrittura e volume totale di dati scritti. Tuttavia, un nodo Bitcoin impone un carico significativo sul disco durante la scrittura. Per questo motivo non consiglio i modelli entry-level; suggerisco invece un'unità SSD NVMe, che offre prestazioni nettamente superiori.



A titolo di esempio, per gli scopi di questo corso, ho scelto il seguente modello: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, disponibile a circa 120 euro su Amazon. Puoi anche optare per altri marchi noti come Crucial, Western Digital o Kingston.



![Image](assets/fr/046.webp)



#### Configurazione a basso budget



Ovviamente, se il tuo budget è molto limitato (sotto i 200 euro), ti consiglio di non investire in un dispositivo dedicato, ma di installare Bitcoin Core direttamente sul tuo PC di tutti i giorni (in modalità pruned se avete poco spazio su disco).



Altrimenti, per un budget entry-level, consiglio il modello *HP EliteDesk 800 G2 Mini*. Ho trovato un modello ricondizionato a 96 euro su Amazon, dotato di un processore Intel Core i5 di sesta generazione e 8 GB di RAM. Si tratta di un'opzione particolarmente interessante per i principianti: questo processore e questa quantità di memoria sono più che sufficienti per eseguire Core su Umbrel, così come diverse applicazioni contemporaneamente, come un indicizzatore Electrs, un nodo Lightning e un'istanza mempool, a patto di non allocare troppa cache a Core. Inoltre, questo tipo di mini-PC consente di aumentare facilmente la RAM a 16 GB, ad esempio, in caso di necessità (aspettati di pagare circa 30-40 euro in più per una o due chiavette di memoria di qualità).



![Image](assets/fr/045.webp)



Poi basta aggiungere l'SSD al budget. Partendo dal Samsung da 2 TB a 120 euro, otteniamo un costo totale di 216 euro per un dispositivo completo e funzionale.



#### Configurazione a medio budget



Se hai un budget medio di circa 300 euro per il dispositivo che ospiterà il vostro nodo, ti consiglio un *Lenovo ThinkCentre Tiny*, ad esempio, dotato di un processore ad alte prestazioni e di sufficiente RAM. Ho trovato un modello ricondizionato su Amazon a 180 euro, con un processore Intel Core i7 di sesta generazione e 16 GB di RAM. Con l'aggiunta dell'unità SSD da 2 TB a 120 euro, il costo totale è di 300 euro.



![Image](assets/fr/044.webp)



Con questo dispositivo, hai una configurazione confortevole: un IBD veloce e la possibilità di eseguire numerose applicazioni su Umbrel o Start9 senza difficoltà. È proprio questa la configurazione che sto utilizzando per il corso BTC 202.



#### Configurazione di fascia alta



Con un budget più elevato, le possibilità diventano molto più ampie. Si può scegliere una configurazione fai-da-te, oppure optare per un dispositivo preassemblato offerto direttamente da un progetto node-in-a-box.



Ad esempio, l'*ASUS NUC 14 Pro* è disponibile nuovo su Amazon a 540 euro. A questo prezzo si ottiene un processore Intel Core Ultra 5 (recente e particolarmente performante), accompagnato da 16 GB di RAM DDR5. Con una tale configurazione, sarai in grado di completare un IBD in tempi record e di installare applicazioni impegnative senza difficoltà.



Si tratta di una configurazione estremamente comoda, persino eccessiva se l'obiettivo iniziale è semplicemente quello di far funzionare un nodo Bitcoin. D'altra parte, se vuoi sfruttare appieno tutte le applicazioni self-hosting disponibili su Umbrel e Start9, questo livello di potenza è la scelta giusta.



![Image](assets/fr/043.webp)



A seconda dell'uso che si intende fare, si può optare per un'unità SSD da 2 TB, come nelle altre configurazioni, oppure direttamente per un'unità SSD da 4 TB a 260 euro se si desidera archiviare anche file personali e ampliare l'uso del self-hosting. Con un'unità SSD da 2 TB, il costo totale della configurazione è di 660 euro, mentre con un'unità SSD da 4 TB raggiunge gli 800 euro.



### Qualche altro consiglio





- Se vuoi acquistare attrezzature di seconda mano e pagare in bitcoin, vieni a un meetup vicino a te! Chiacchierando con gli altri partecipanti, troverai sicuramente l'attrezzatura adatta a un buon prezzo, contribuendo al contempo a mantenere viva l'economia circolare intorno a Bitcoin. È anche un'opportunità per beneficiare dei consigli della community.





- Per la connessione a Internet è ovviamente necessario un cavo Ethernet RJ45, almeno per l'installazione del sistema.





- Alcuni ambienti, come Umbrel, consentono di utilizzare il Wi-Fi, ma le prestazioni saranno generalmente inferiori (soprattutto se si desidera utilizzare il nodo Lightning da remoto, in quanto ciò può avere un impatto). Se si sceglie il Wi-Fi, assicurarsi che il dispositivo abbia una scheda integrata o aggiungere una chiavetta USB compatibile.





- Utilizzare sempre l'alimentatore originale del produttore per il dispositivo. Questo è fondamentale per evitare danni all'apparecchiatura e per prevenire il rischio di incendi.





- Se la macchina non dispone di una batteria integrata, è bene investire in un inverter per evitare spegnimenti improvvisi.





- A seconda del valore delle apparecchiature e della posizione geografica, può essere opportuno installare un sistema di protezione contro i fulmini, direttamente sul quadro elettrico o sulla ciabatta utilizzata.





- Infine, ricordate di ottimizzare il raffreddamento della macchina: pulitela regolarmente e installatela in un luogo fresco, ben ventilato e non ingombro per evitare il surriscaldamento, che potrebbe portare al throttling (limitazione volontaria della velocità del processore).



# Installazione semplice di un nodo Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: molto più di un nodo Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel è un sistema operativo per server personali progettato per rendere accessibile il self-hosting: si installa Umbrel, si apre un browser su `umbrel.local` e si gestisce tutto tramite una semplice interfaccia remota.



Il progetto ha dapprima reso popolare l'idea di un nodo Bitcoin e Lightning con un solo clic, per poi espandersi in una vera e propria "nuvola domestica": archiviazione di file e foto, streaming multimediale, strumenti di rete, automazione domestica, intelligenza artificiale locale e centinaia di app installabili da un App Store integrato.



In Umbrel, ogni applicazione viene eseguita in un contenitore Docker (isolamento, aggiornamenti atomici, avvio/arresto indipendente). L'interfaccia centralizza l'accesso a tutte queste applicazioni, offrendo single sign-on (con 2FA opzionale), aggiornamenti one-click per il sistema operativo e le applicazioni, monitoraggio in tempo reale della macchina (CPU, RAM, temperatura, storage), gestione dei permessi tra le applicazioni e una panoramica del loro consumo.



L'obiettivo di Umbrel è quindi quello di restituire all'utente il controllo e la riservatezza dei propri dati, senza affidarsi a servizi cloud, al di là della semplice gestione di un nodo Bitcoin.



### Umbrel Home vs umbrelOS



Umbrel offre due approcci distinti:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): è un mini-server pronto all'uso, appositamente progettato e ottimizzato per umbrelOS. Compatto, silenzioso, collegato a Ethernet, è dotato di un SSD NVMe (fino a 4TB opzionali), 16GB di RAM e una CPU quad-core. Lo si ordina, lo si collega e si va su `umbrel.local`. È possibile avere un Umbrel operativo e funzionante in pochi minuti. Questa è l'opzione plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): è il sistema operativo che puoi installare tu stesso sul tuo hardware (mini-PC, NUC, tower, laptop dedicato...). Si dispone della stessa interfaccia e dello stesso App Store di Umbrel Home.



![Image](assets/fr/080.webp)



In entrambi i casi, l'esperienza dell'utente è identica dal punto di vista del software: amministrazione basata su browser, aggiornamenti con un solo clic, installazione di applicazioni su richiesta... La soluzione fai da te è spesso più economica dell'acquisto di Umbrel Home (a seconda della macchina utilizzata). Tuttavia, non consiglierei necessariamente di optare sempre per l'opzione fai-da-te, poiché **l'acquisto di Umbrel Home contribuisce direttamente a finanziare lo sviluppo del progetto**, dato che il suo modello commerciale si basa sulla vendita di hardware. E francamente, a 389 euro per 2 TB di spazio di archiviazione, il prezzo rimane molto ragionevole vista la qualità del dispositivo offerto.



![Image](assets/fr/079.webp)



Nel prossimo capitolo vedremo come installare umbrelOS DIY sul proprio dispositivo. Tuttavia, puoi seguire questo corso BTC 202 allo stesso modo se hai optato per una Umbrel Home.



### Caso d'uso: dal nodo Bitcoin al cloud domestico



Umbrel può rimanere molto minimalista e focalizzato esclusivamente su Bitcoin, oppure evolversi in un vero e proprio server personale multifunzionale, a seconda delle tue esigenze. Ecco i principali utilizzi di Umbrel:





- **Semplice nodo Bitcoin**: questo è l'uso principale su cui Umbrel ha fatto affidamento fin dall'inizio. È possibile eseguire Bitcoin Core (o Knots), collegare i wallet direttamente al nodo, esporre un server Electrum, ospitare il Mempool Block Explorer per visualizzare la blockchain e stimare le spese... È su questi usi che ci concentreremo in questo corso.



![Image](assets/fr/082.webp)





- **Lightning Network**: Umbrel consente inoltre di implementare LND o Core Lightning, due implementazioni di Lightning Network, per gestire il proprio nodo Lightning. Potrai aprire canali, gestire la liquidità, effettuare pagamenti, automatizzare il bilanciamento, offrire servizi, collegare un wallet remoto o sfruttare la gestione avanzata dell'interfaccia grazie alle numerose applicazioni disponibili. Analizzeremo questo caso specifico nel prossimo corso LNP 202.



![Image](assets/fr/083.webp)





- **Self-hosting generale**: con Nextcloud, Immich, Jellyfin/Plex, blocco degli annunci a livello di DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), domotica (Home Assistant), backup, gestione delle note, strumenti per l'ufficio, AI locale (Ollama + Open WebUI)... Umbrel può diventare il tuo server personale, permettendoti di riprendere il controllo dei tuoi dati. Ospita tu stesso i servizi che utilizzi quotidianamente, con un'esperienza utente raffinata che ricorda le soluzioni esterne, mantenendo il controllo totale sui tuoi dati e della tua privacy.



Distribuendo le applicazioni in containers, puoi modellare Umbrel come vuoi: inizia con un semplice nodo Bitcoin e alcune applicazioni legate al suo ecosistema, poi installa un nodo Lightning accanto al nodo Bitcoin e arricchisci gradualmente la tua istanza con le applicazioni self-hosting di cui hai bisogno.



### Community e aiuto reciproco



Uno dei vantaggi principali di Umbrel rispetto ai suoi concorrenti è la sua vasta e attivissima community di utenti. È possibile raggiungerli principalmente tramite [il loro Discord](https://discord.gg/efNtFzqtdx) e [il loro forum online](https://community.umbrel.com/). Qui troverai non solo consigli pratici, ma soprattutto soluzioni per risolvere i problemi o risolvere i bug. È un ottimo punto di partenza, per progredire e, infine, per aiutare gli altri utenti, in modo da non essere lasciato solo con il proprio nodo Bitcoin.



![Image](assets/fr/084.webp)



### Licenza UmbrelOS



Il codice di Umbrel è pubblicamente disponibile (è possibile visualizzarlo, Fork e modificarlo), ma non è sotto una vera licenza open-source. Infatti, umbrelOS è distribuito sotto la licenza [*PolyForm Noncommercial 1.0*](https://polyformproject.org/licenses/noncommercial/1.0.0/), sebbene alcuni strumenti di sviluppo associati siano disponibili sotto la licenza MIT.



In pratica, puoi fare praticamente tutto quello che vuoi con umbrelOS, purché sia per uso personale e non commerciale: modifiche, ridistribuzione per scopi non di lucro, creazione di derivati per te stesso o per organizzazioni non di lucro, purché rispetti le note legali.



Tuttavia, è vietato vendere Umbrel o i suoi derivati (ad esempio, una macchina preassemblata con umbrelOS preinstallato), offrire servizi legati a Umbrel a scopo commerciale o integrare il suo codice in un prodotto a scopo di lucro.



Tecnicamente, questa licenza non limita l'installazione, la verifica o l'adattamento di Umbrel per uso personale. Dal punto di vista legale, protegge il progetto dalla rivendita non autorizzata o dall'hosting commerciale, in particolare da parte dei fornitori di cloud. Umbrel non è quindi open source, anche se il suo codice rimane pubblicamente accessibile.



Tuttavia, ogni applicazione dello store mantiene la propria licenza, spesso open source.




## Installazione di un full node con Umbrel


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Ora che abbiamo tutte le informazioni necessarie, è il momento di entrare nei dettagli. In questa guida ti mostreremo come installare un nodo Bitcoin completo utilizzando UmbrelOS.



### Materiali necessari



In questo caso, utilizzeremo l'immagine UmbrelOS x86 (più precisamente, la versione x86_64). Potrai seguire questa guida su qualsiasi dispositivo scegli, purché non sia dotata di un processore con architettura ARM (niente Apple Silicon, Raspberry Pi, ecc.). Ciò significa che qualsiasi computer con processore Intel o AMD a 64 bit sarà sufficiente, purché soddisfi i requisiti minimi, a seconda di come intendi utilizzare Umbrel (si consiglia almeno un processore dual-core).



Se si è optato per un Raspberry Pi 5 (opzione che non consiglio, come indicato nella sezione precedente), l'installazione è leggermente diversa. Potrai quindi seguire questo tutorial dedicato e tornare al mio corso una volta raggiunta l'interfaccia web al sito `http://umbrel.local`:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Come accennato nella sezione precedente, ho scelto di eseguire questa esercitazione su un piccolo PC ricondizionato che ho trovato a un buon prezzo: un *Lenovo ThinkCentre M900 Tiny* dotato di un processore Intel Core i7 e 16 GB di RAM. È una configurazione molto comoda per l'esecuzione di Umbrel, soprattutto per un nodo Bitcoin. Tuttavia, ho scelto questa configurazione perché voglio installare un nodo Lightning e altre applicazioni più impegnative in seguito. Ho anche aggiunto un SSD da 2 TB al mio ThinkCentre per mantenere l'intera blockchain e avere ancora un margine confortevole. Con questa configurazione, il costo totale è di 270 euro, comprensivo di tutte le spese.



![Image](assets/fr/001.webp)



Sono particolarmente appassionato della gamma ThinkCentre Tiny di Lenovo, in quanto si tratta di dispositivi compatti, silenziosi e molto robusti. Questi computer sono molto popolari tra le aziende e quindi abbondano sul mercato dell'usato, dove si possono trovare configurazioni interessanti tra i 70 e i 200 euro.



Se, come me, hai scelto un PC senza monitor, **dovrai collegare un monitor e una tastiera** solo per la durata dell'installazione. In seguito, potrai accedervi in remoto da un altro computer della stessa rete (o con altri metodi che tratteremo nei capitoli successivi). È inoltre necessario un cavo Ethernet RJ45 per collegare il dispositivo alla rete locale e una chiave USB di almeno 4 GB per memorizzare l'immagine di installazione.



Per ricapitolare, ecco i requisiti dell'attrezzatura:




- Computer con processore x86_64 (minimo Dual-core, consigliato Quad-core);
- Memoria RAM (4 GB minimo, 8 GB consigliati o più per un uso prolungato);
- SSD (consigliato + 2 TB);
- Chiave USB (+ 4 GB) per l'installazione dell'immagine di UmbrelOS;
- Monitor e tastiera (utile solo per l'installazione iniziale se il PC non ne è dotato);
- Cavo Ethernet RJ45.



### Fase 1 - Montaggio del computer



A seconda dell'hardware scelto, il primo passo consiste nell'assemblare i vari componenti del computer. Ad esempio, nel mio caso, l'unità SSD originale aveva una capacità di soli 256 GB, quindi la riciclerò per un altro uso e la sostituirò con un'unità SSD da 2 TB. Se vuoi sostituire anche i moduli RAM, è il momento di farlo.



### Fase 2: preparazione di una chiave USB avviabile



Prima di installare UmbrelOS sul vostro dispositivo, dovrai creare una chiave USB avviabile contenente il sistema operativo. Tutti i passaggi del punto 2 devono essere eseguiti sul tuo computer personale (e non direttamente sul computer destinato a diventare il tuo nodo).





- Iniziare scaricando l'ultima versione di UmbrelOS in formato USB:



Vai sul [sito ufficiale di Umbrel per scaricare l'immagine ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) per l'installazione tramite chiave USB. Assicurarsi di selezionare la versione compatibile con l'architettura x86_64 (file denominato `umbrelos-amd64-usb-installer.iso`). Il download può richiedere un po' di tempo, poiché l'immagine è piuttosto grande.



![Image](assets/fr/002.webp)





- Installare Balena Etcher:



Per creare la chiavetta USB avviabile, utilizzerai un semplice strumento multipiattaforma chiamato [Balena Etcher](https://www.balena.io/etcher/). Scaricalo e installalo sul tuo computer.



![Image](assets/fr/003.webp)





- Inserire una chiave USB vuota di almeno 4 GB:



Inserisci una chiavetta USB nel computer (quella su cui hai appena scaricato l'immagine di UmbrelOS e Balena Etcher). **Attenzione: tutti i dati contenuti nella chiavetta saranno cancellati**. Assicurati che non contenga file importanti.





- Masterizzare l'immagine ISO sulla chiavetta USB con Balena Etcher:



Avviare Balena Etcher e selezionare il file ISO `umbrelos-amd64-usb-installer.iso` appena scaricato facendo clic sul pulsante "*Flash da file*". Quindi, selezionare la chiave USB come dispositivo di destinazione e fare clic su "*Flash!*" per iniziare la scrittura.



![Image](assets/fr/004.webp)



Una volta completata l'operazione, avrai una chiavetta USB avviabile contenente UmbrelOS, pronta per l'avvio e l'installazione di Umbrel sul tuo computer.



![Image](assets/fr/005.webp)



### Fase 3: avvio del computer dalla chiave USB



Ora che la chiavetta USB avviabile contenente UmbrelOS è pronta, puoi avviare il computer da USB per iniziare l'installazione del sistema. Scollegare la chiavetta USB dal computer principale e inserirla nel dispositivo su cui si desidera installare Umbrel e il nodo Bitcoin.



Come spiegato all'inizio di questo capitolo, per completare l'installazione sono necessari un dispositivo di visualizzazione e un dispositivo di input. Collega uno schermo tramite HDMI (o un'altra porta, a seconda del vostro PC) e una tastiera tramite USB al vostro dispositivo. Questi dispositivi sono necessari solo per l'installazione; in seguito non saranno più necessari, poiché Umbrel sarà accessibile in remoto da un altro computer. Collegare questi due dispositivi al PC.



**Suggerimento:** Se non si dispone di uno schermo periferico a casa, è possibile utilizzare il televisore. Grazie all'ingresso HDMI (o di altro tipo), può essere utilizzato come schermo temporaneo mentre si installa il sistema operativo.



Umbrel richiede ovviamente una connessione a Internet. Collega il cavo Ethernet RJ45 tra il dispositivo e il router.



![Image](assets/fr/006.webp)



Accendi il computer. Nella maggior parte dei casi, dovrebbe rilevare automaticamente la chiave USB e avviarla. Verrà quindi visualizzata la schermata di installazione di UmbrelOS Interface.



Se il dispositivo si avvia su un altro sistema o visualizza un messaggio di errore, probabilmente significa che non si sta avviando automaticamente dalla chiave USB. In questo caso, riavviare e accedere alle impostazioni del BIOS/UEFI (di solito si accede premendo `DEL`, `F2`, `F12` o `ESC`, a seconda del produttore del computer). Quindi, modificare l'ordine di avvio per dare priorità alla chiave USB. Quindi riavviare il dispositivo per avviare UmbrelOS.



### Passo 4: Installare UmbrelOS sul computer



Una volta avviato il dispositivo dalla chiavetta USB, verrai accolto dall'interfaccia di installazione di UmbrelOS. Questo passaggio prevede l'installazione del sistema direttamente all'interno dell'hard disk.



La schermata visualizzata elenca tutti i dispositivi di archiviazione interna rilevati dal computer. Ogni disco è accompagnato da un numero, un nome e una capacità di memoria. Individuare il disco su cui si desidera installare Umbrel. **Attenzione: tutti i file presenti su questo disco verranno eliminati in modo permanente.**



![Image](assets/fr/007.webp)



Una volta individuato il disco corretto (di solito quello con la capacità maggiore, per ospitare la blockchain), prendere nota del numero assegnatogli. Ad esempio, se il disco scelto appare sotto il numero `2`, è sufficiente immettere `2`, quindi premere il tasto `Enter` sulla tastiera.



![Image](assets/fr/008.webp)



Il programma formatta il disco selezionato, installa UmbrelOS e configura automaticamente il sistema. Questa operazione potrebbe richiedere alcuni minuti. Lascia che il processo si svolga senza interruzioni.



![Image](assets/fr/009.webp)



Al termine dell'installazione, verrà richiesto di spegnere il dispositivo. Premi un tasto qualsiasi per spegnere il computer.



![Image](assets/fr/010.webp)



Ora è possibile rimuovere la chiave USB, la tastiera e lo schermo, che non sono più necessari per Umbrel. Tutto ciò che rimane del nodo è la fonte di alimentazione e il cavo Ethernet RJ45.



![Image](assets/fr/011.webp)



Prima di riavviare il dispositivo, verifica i due punti seguenti:





- **La chiave USB è scollegata**: se rimane collegata, il sistema potrebbe riavviarsi su di essa anziché sul disco interno;
- **Il cavo Ethernet è collegato**: per funzionare, il dispositivo deve essere collegato al router.



Premi il pulsante di accensione. Il sistema si avvia automaticamente dal disco interno in cui è stato installato UmbrelOS. Il primo avvio può richiedere circa **5 minuti**. Durante questo periodo, Umbrel inizializza l'interfaccia e i suoi servizi.



Da un altro computer (il PC di tutti i giorni) collegato alla **stessa rete locale**, apri un web browser (Firefox, Chrome...) e vai su:



```
http://umbrel.local
```



Questo indirizzo viene utilizzato per accedere all'interfaccia grafica di Umbrel da remoto e iniziare la configurazione.



Se il sito Address `http://umbrel.local` non funziona sul tuo browser dopo aver atteso almeno 5 minuti, prova semplicemente:



```
http://umbrel
```



Se ancora non funziona, inserisci l'indirizzo IP locale di Umbrel direttamente nel browser. Ad esempio (sostituisci `42` con il numero del dispositivo che ospita Umbrel sulla rete locale):



```
http://192.168.1.42
```



Per identificare l'indirizzo IP di Umbrel, esistono diversi metodi, dai più semplici ai più avanzati:





- Accedere all'interfaccia di amministrazione del router e trova l'indirizzo IP del dispositivo Umbrel sulla rete locale.





- Utilizzare un software di scansione di rete come Angry IP Scanner per rilevare i dispositivi collegati e individuare l'indirizzo IP di Umbrel.



![Image](assets/fr/012.webp)



https://planb.academy/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Come ultima risorsa, ricollega un monitor e una tastiera al dispositivo, effettua il login (login predefinito: `umbrel`, password: `umbrel`), quindi digita il seguente comando:



```
hostname -I
```



Ora sei pronto a usare Umbrel!



### Passo 5: Iniziare con Umbrel



Per iniziare a configurare Umbrel, fai clic sul pulsante "*Avvio*".



![Image](assets/fr/013.webp)



#### Creare un account



Scegli uno pseudonimo o inserisci il vostro nome, quindi imposta una password forte. Attenzione: questa password è l'unica barriera che protegge l'accesso al tuo Umbrel dalla tua rete (e quindi, potenzialmente, ai tuoi bitcoin se gestisci un nodo Lightning su Umbrel). Protegge anche l'accesso remoto tramite [Tor](https://planb.academy/resources/glossary/tor) o VPN, se questi servizi sono abilitati.



Scegli una password forte e assicurati di conservarne almeno una di backup (si consiglia un gestore di password).



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.academy/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Una volta inserita la password, fai clic sul pulsante "*Crea*".



![Image](assets/fr/014.webp)



La configurazione di Umbrel è ora completa.



![Image](assets/fr/015.webp)



#### Scoperta dell'interfaccia



L'interfaccia di Umbrel è piuttosto intuitiva:





- Nella pagina iniziale è possibile visualizzare le applicazioni e i widget installati.



![Image](assets/fr/016.webp)





- L'"*App Store*" consente di installare nuove applicazioni,



![Image](assets/fr/017.webp)





- Il menu "*Files*" centralizza tutti i documenti memorizzati su Umbrel.



![Image](assets/fr/018.webp)





- Il menu "*Impostazioni*" consente di modificare le impostazioni di Umbrel e di accedere alle sue informazioni, tra cui:
    - Aggiornare, riavviare o arrestare il computer;
    - Consultare lo spazio di memoria disponibile, l'utilizzo della RAM e la temperatura del processore;
    - Cambiare lo sfondo;
    - Gestione dell'accesso remoto tramite Tor, attivazione del Wi-Fi o 2FA.



![Image](assets/fr/019.webp)



#### Impostazioni di sicurezza e di connessione



Innanzitutto, consiglio vivamente di attivare l'autenticazione a due fattori (2FA). Questo aggiunge un ulteriore Layer di sicurezza alla vostra password. È quasi indispensabile se si intende utilizzare Umbrel per archiviare file personali, eseguire un nodo Lightning o svolgere qualsiasi altra attività sensibile.



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

A tal fine, fai clic sulla casella corrispondente nelle impostazioni.



![Image](assets/fr/020.webp)



Esegui la scansione del codice QR visualizzato utilizzando la tua applicazione di autenticazione. Immetti quindi il codice dinamico a 6 cifre nell'apposito campo dell'Umbrel.



D'ora in poi, ogni nuova connessione al tuo Umbrel richiederà sia la password che il codice a 6 cifre generato dalla tua applicazione di autenticazione a due fattori (2FA).



![Image](assets/fr/021.webp)



Per quanto riguarda l'accesso remoto via Tor, se non ne hai bisogno, ti consiglio di lasciare questa opzione disattivata per limitare la superficie di attacco di Umbrel. Per impostazione predefinita, è possibile accedere al nodo solo da un dispositivo connessa alla stessa rete locale. L'abilitazione dell'accesso via Tor ti permetterà comunque di gestire il tuo Umbrel da remoto.



Se si attiva questa funzione, in teoria è possibile per qualsiasi dispositivo al mondo tentare una connessione al vostro nodo, a condizione che conosca l'indirizzo Tor. Tuttavia, la password e la 2FA continueranno a proteggerti.



Se si attiva questa opzione, assicurati di aver attivato l'autenticazione a due fattori (2FA), di avere una password forte e di non rivelare mai il tuo indirizzo connessione Tor.



È sufficiente inserire questo indirizzo Tor nel browser Tor per accedere all'interfaccia di Umbrel da qualsiasi rete.



![Image](assets/fr/026.webp)



Infine, in questa pagina di impostazioni è possibile attivare la connessione Wi-Fi. Se il dispositivo che ospita Umbrel dispone di una scheda di rete Wi-Fi o di una chiavetta Wi-Fi, ciò consente di accedere a Internet senza utilizzare il cavo RJ45. Tuttavia, a seconda della configurazione, questa soluzione può rallentare la connessione, il che può influire sulla sincronizzazione iniziale (IBD) e sull'uso futuro del nodo (ad esempio, per le transazioni Lightning). Personalmente, non consiglio questa opzione, in quanto un nodo non è destinato all'uso mobile: si accede sempre da remoto, quindi tanto vale lasciarlo collegato.



### Passo 6: Installazione di un nodo Bitcoin su Umbrel



Ora che UmbrelOS è correttamente installato e configurato sul dispositivo, si può procedere all'installazione del nodo Bitcoin. Niente di più semplice: andate sull'App Store, aprite la categoria "*Bitcoin*", quindi selezionate l'applicazione "*Bitcoin Node*" (in realtà è Bitcoin Core).



![Image](assets/fr/022.webp)



Quindi fare clic sul pulsante "*Installa*".



![Image](assets/fr/023.webp)



Una volta completata l'installazione, il nodo Bitcoin avvierà il suo IBD (*Initial Block Download*): scaricherà e convaliderà tutte le transazioni e i blocchi dalla creazione di Bitcoin nel 2009.



![Image](assets/fr/024.webp)



Questa fase è particolarmente lunga, poiché la sua durata dipende da diversi fattori, tra cui la quantità di RAM allocata nella cache del nodo, la velocità del disco, la velocità della connessione a Internet e la potenza del processore. Con un PC ad alte prestazioni (SSD NVMe, +32 GB di RAM, processore potente e buona connessione a Internet), l'IBD può essere completato in circa dieci ore. D'altra parte, un processore vecchio, poca RAM o, peggio ancora, un hard disk meccanico (fortemente sconsigliato) possono prolungare questa operazione fino a diverse settimane.



Con un PC di configurazione standard (un processore decente, da 8 a 16 GB di RAM e un'unità SSD), è possibile completare l'IBD tra i 2 e i 7 giorni.



Per accelerare leggermente l'IBD, è possibile aumentare la RAM allocata alla cache del nodo (utilizzata principalmente per l'UTXO set, che verrà rivisto più avanti nel corso) tramite il parametro `dbcache`. Su Umbrel, questa modifica si effettua nei parametri del nodo, nella scheda "*Optimization*".



![Image](assets/fr/025.webp)



Per impostazione predefinita, il valore del parametro `dbcache` in Bitcoin Core è impostato su 450 MiB, ovvero circa 472 MB. Aumentando questo valore, si può accelerare leggermente IBD. Tuttavia, non raccomanderei necessariamente di spingere questo parametro troppo in alto: anche impostandolo a 4 GiB la sincronizzazione sarà più veloce solo del 10% circa e potrebbe far perdere tempo in caso di interruzione durante l'IBD.



Fai attenzione a non allocare un valore troppo grande per il tuo dispositivo. Se la RAM disponibile per UmbrelOS si esaurisce, il nodo potrebbe arrestarsi bruscamente, interrompendo l'IBD e richiedendo di riavviarlo manualmente, con una notevole perdita di tempo.



Per saperne di più sull'impatto del parametro `dbcache` sulla sincronizzazione iniziale, consiglio questa analisi di Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Una volta completato l'IBD del nodo (sincronizzazione al 100%), si dispone di un nodo Bitcoin pienamente operativo. Congratulazioni, ora sei parte integrante del network Bitcoin!



![Image](assets/fr/027.webp)



Nella prossima parte, esploreremo l'uso pratico del tuo nuovo nodo: come collegare il tuo wallet ad esso e quali applicazioni dovresti installare per diventare un Bitcoiner sovrano.





# Collegamento del wallet al nodo


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indicizzatori: ruolo, funzionamento e soluzioni


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Se hai già esplorato i nodi Bitcoin prima di seguire questo corso, potresti aver incontrato il termine "indicizzatore"(indexer). Si tratta di strumenti come Electrs o Fulcrum, che possono essere aggiunti a un nodo Bitcoin Core. Ma qual è esattamente il loro ruolo? Come funzionano in pratica? E dovresti installarne uno sul tuo nuovo nodo Bitcoin? In questo capitolo esamineremo l’argomento.


### Che cos'è un indicizzatore?



In generale, un indicizzatore è un programma che analizza un insieme di dati grezzi, estrae le chiavi rilevanti (come parole, identificatori e indirizzi) e costruisce un file ausiliario, chiamato "indice"(index), in cui ogni chiave si riferisce alla posizione esatta dei dati nel corpus. Questa fase di pre-elaborazione utilizza il tempo della CPU e richiede spazio su disco, ma elimina la necessità di elaborare l'intero corpus ogni volta che si interroga il database; semplicemente interrogando l'indice si ottiene una risposta quasi immediata.



In parole povere, è lo stesso principio dell'indice di un libro: se si cerca un'informazione specifica, invece di rileggere l'intero libro, si consulta l'indice per trovare direttamente la pagina in cui compare l'informazione cercata.



In un nodo Bitcoin, come Bitcoin Core, i dati della blockchain sono memorizzati nella loro forma grezza e cronologica. Ogni blocco contiene transazioni, che a loro volta contengono input e output, senza alcuna classificazione particolare per indirizzi, identificatore o wallet. Questa organizzazione lineare è ottimizzata per la convalida dei blocchi, ma inadatta per le ricerche mirate. Ad esempio, se si volessero trovare tutte le transazioni collegate a uno specifico indirizzo in un nodo non indicizzato, si dovrebbe esaminare manualmente l'intera blockchain, blocco per blocco e transazione per transazione. È proprio qui che entra in gioco l'indicizzatore del nodo Bitcoin.



![Image](assets/fr/085.webp)



Un indicizzatore è un software specializzato che analizza questa massa di dati grezzi (Blockchain, Mempool, UTXO) ed estrae le chiavi, come gli identificatori delle transazioni, gli indirizzi e le altezze dei blocchi. Da queste chiavi, costruisce il suo indice, associando ogni chiave alla posizione esatta delle informazioni nella memoria del nodo.



![Image](assets/fr/086.webp)



L'indicizzazione consente di cercare informazioni sul nodo in modo rapido, preciso ed efficiente. Ad esempio, quando si collega un wallet come Sparrow al proprio nodo, questo può visualizzare il bilancio di un indirizzo quasi istantaneamente. In concreto, interroga l'indicizzatore con una richiesta del tipo: "_Quali UTXO sono associati a questo script-Hash?_" L'indicizzatore risponde quasi immediatamente, senza dover rileggere l'intera blockchain, poiché questi dati sono già elencati nel suo database.



### Bitcoin Core dispone di un indicizzatore?



Senza un software aggiuntivo, Bitcoin Core non offre, in senso stretto, un indicizzatore di indirizzi completo, paragonabile a quelli presenti in software come Electrs o Fulcrum. Tuttavia, incorpora diversi meccanismi di indicizzazione interna, nonché opzioni per estendere le sue capacità di interrogazione. Per comprendere appieno la situazione, dobbiamo fare una digressione nella storia del progetto.



Fino alla versione 0.8.0 di Bitcoin Core, la convalida delle transazioni si basava su un indice globale delle transazioni, noto come `txindex`. Questo indice faceva riferimento a tutte le transazioni su blockchain e ai loro output. Quando un nodo riceveva una nuova transazione, consultava questo indice per verificare che gli output consumati (in input) esistessero davvero e non fossero già stati spesi. Il `txindex` era quindi indispensabile per la validazione delle transazioni all'epoca.



Tuttavia, questo approccio aveva i suoi limiti: era lento, costoso in termini di archiviazione e ridondante in termini di informazioni. Per ovviare a ciò, la versione 0.8.0 introduce una revisione del modello di convalida chiamata ***Ultraprune***. Invece di memorizzare tutto sotto forma di indici di transazioni, Bitcoin Core mantiene un semplice database dedicato esclusivamente agli UTXO, chiamato `chainstate` (nel linguaggio comune, questo è noto come "UTXO set"), e ne aggiorna l'elenco man mano che gli output vengono consumati e creati.



Questo metodo è molto più veloce e memorizza solo lo stato corrente del registro, rendendo superfluo l'indicizzatore `txindex`. Tuttavia, invece di eliminare il codice `txindex`, gli sviluppatori hanno scelto di mantenere questa funzionalità dietro un semplice parametro (`txindex=1`). Abilitando questa opzione sul proprio nodo, è possibile interrogare qualsiasi transazione dal suo `txid`.



Contrariamente a quanto si pensa, Bitcoin Core non offre l'indicizzazione basata su indirizzi come Electrs o Fulcrum. Le ragioni di questa scelta sono molteplici:





- Il ruolo di Bitcoin Core non è quello di diventare un block explorer completo, né di fornire un'API su misura per ogni utilizzo. L'integrazione di un indice basato su indirizzi implicherebbe un'impegno di manutenzione a lungo termine che va oltre lo scopo iniziale del software.





- La maggior parte dei casi d'uso può essere già coperta in altri modi. Ad esempio, per stimare l'equilibrio di un indirizzo, si può usare il comando `scantxoutset`, che interroga direttamente l'insieme UTXO senza richiedere un indice completo.





- Ogni programma software ha requisiti specifici per quanto riguarda il formato o il tipo di dati da indicizzare (Address, script Hash, tag proprietario, ecc.). È più flessibile e logico lasciare che questi programmi costruiscano i propri indici personalizzati piuttosto che fissare una soluzione generica in Bitcoin Core.



Bitcoin Core ha un indicizzatore di transazioni opzionale (`txindex`), un retaggio del suo funzionamento storico, ma non fornisce un indice basato su indirizzi, né un'interfaccia diretta per ricerche complesse. In alcuni casi, quindi, può essere utile aggiungere un indicizzatore esterno.



### È necessario aggiungere un indicizzatore di indirizzi al nodo?



L'aggiunta di un indicizzatore di indirizzi, come Electrs o Fulcrum, non è obbligatoria; dipende dalle tue esigenze specifiche.



Se si desidera semplicemente collegare un wallet, come Sparrow, al proprio nodo per visualizzare i saldi e trasmettere le transazioni, questo è possibile direttamente tramite l'interfaccia RPC di Bitcoin Core, sia localmente che in remoto tramite Tor.



D'altra parte, per utilizzare software più avanzati, come l'esecuzione di mempool.space in locale, l'installazione di un indicizzatore di indirizzi diventa indispensabile per lo space block explorer.



L'indicizzatore richiede un certo tempo di sincronizzazione (inferiore a quello dell'IBD) e occuperà ulteriore spazio su disco. Se l'SSD ha ancora spazio libero sufficiente dopo aver scaricato la blockchain, è possibile aggiungere facilmente un indicizzatore.



### Quale indicizzatore scegliere?



Per costruire questo tipo di indice di indirizzi e renderlo accessibile si utilizzano comunemente due software: **Electrs** e **Fulcrum**. Questi strumenti indicizzano la blockchain in base agli script-hash (indirizzi) e propongono poi un'interfaccia standardizzata (il protocollo Electrum), al quale si collegano numerosi wallet, come Electrum Wallet, Sparrow o Phoenix.



![Image](assets/fr/087.webp)



In poche parole, Electrs è piuttosto compatto: indicizza la blockchain più velocemente e occupa meno spazio su disco, ma ha prestazioni leggermente inferiori a Fulcrum nelle interrogazioni. Fulcrum, invece, consuma più spazio su disco e richiede più tempo per l'indicizzazione, ma offre prestazioni superiori nelle query.



Per l'uso individuale, consiglio Electrs: consuma meno spazio, è ben mantenuto e, sebbene sia leggermente più lento su alcune richieste rispetto a Fulcrum, è comunque più che sufficiente per l'uso quotidiano. Se hai tempo e spazio su disco, puoi provare anche Fulcrum, che avrà prestazioni nettamente superiori, soprattutto su wallet con numerosi indirizzi da verificare.



In concreto, nell'agosto 2025 Electrs richiederà circa 56 GB di spazio di archiviazione, contro i circa 178 GB di Fulcrum. La scelta dell'indicizzatore, quindi, dipende anche dalla capacità di archiviazione:




- Se lo spazio su disco è molto limitato, dovrai accontentarti di Bitcoin Core senza un indicizzatore di indirizzi esterno.
- Se desideri utilizzare un indicizzatore, ma sei ancora limitato dalla capacità, opta per Electrs.
- Se hai una buona quantità di spazio su disco, Fulcrum potrebbe fare al caso tuo.



Per il resto di questo corso BTC 202, utilizzerò Electrum, ma puoi tranquillamente proseguire con Fulcrum: la procedura di installazione è identica, così come la connessione dell'interfaccia al wallet, poiché entrambi espongono un server Electrum.



### Come si installa un indicizzatore su Umbrel?



Per installare Electrs (o Fulcrum) sul tuo Umbrel, la procedura è semplice: vai sull'App Store, cerca l'applicazione in questione (che si trova nella scheda Bitcoin), quindi fai clic sul pulsante "*Install*".



![Image](assets/fr/028.webp)



Una volta completata l'installazione, Electrs procederà alla fase di sincronizzazione (indicizzazione), che può richiedere diverse ore.



![Image](assets/fr/029.webp)



Una volta completata la sincronizzazione, è possibile collegare il software wallet al server Electrum, ospitato su Umbrel.



## Come si collega il wallet al nodo Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Ora che hai un nodo Bitcoin completo, è il momento di farne buon uso! Nel prossimo capitolo esploreremo altri potenziali usi della tua istanza Umbrel. Tuttavia, iniziamo con le basi: collegare il software wallet per utilizzare le informazioni della propria blockchain e distribuire le transazioni attraverso il proprio nodo.



Come già detto, esistono due interfacce di connessione principali:




- Connessione diretta a Bitcoin Core tramite il RPC;
- Oppure collegarsi a un server Electrum (Electrs o Fulcrum).



In questa guida ci concentreremo sulla connessione al nodo tramite Tor, poiché si tratta di una soluzione semplice e sicura per i principianti. Sconsiglio vivamente di esporre la porta RPC del nodo in chiaro, poiché una configurazione errata rappresenta un rischio significativo per la sicurezza e la riservatezza dei dati. Il principale svantaggio delle comunicazioni via Tor è la sua lentezza. Nel prossimo capitolo esploreremo un'alternativa veloce e sicura a Tor per l'accesso remoto al nodo: LA VPN.



In questo capitolo utilizzeremo Sparrow come esempio, ma la procedura è la stessa per tutti gli altri software di gestione wallet che accettano connessioni ai server Electrum. È sufficiente individuare l'impostazione corrispondente nei parametri dell'applicazione (di solito in "*Server*", "*Rete*", "*Nodo*"...).



Su Sparrow, apri la scheda "*File*" e accedi al menu "Impostazioni".



![Image](assets/fr/030.webp)



Clicca quindi su "*Server*" per accedere ai parametri di connessione.



![Image](assets/fr/031.webp)



Si scopriranno quindi tre opzioni per collegare il software a un nodo Bitcoin:




- Server pubblico* (giallo): per impostazione predefinita, se non possiedi un nodo Bitcoin, questa opzione vi connette a un nodo pubblico che non possiedi (di solito quello di un'azienda). Questa opzione non è rilevante in questo caso, poiché avrai il tuo nodo su Umbrel.
- Bitcoin core* (verde): questa opzione corrisponde al collegamento tramite Interface RPC, cioè direttamente a Bitcoin Core.
- Electrum privato* (blu): questa opzione consente di collegarsi tramite il server Electrum Interface dell'indicizzatore (Electrs o Fulcrum).



### Collegamento a Bitcoin Core RPC



Se il nodo Umbrel non dispone di un indicizzatore, questa è l'opzione da selezionare. Su Sparrow, fai clic su "*Bitcoin Core*".



![Image](assets/fr/032.webp)



Sarà quindi necessario inserire diverse informazioni per stabilire la connessione al nodo. Tutti questi dati sono accessibili dall'applicazione "*Nodo Bitcoin*" su Umbrel facendo clic sul pulsante "*Connetti*" nell'angolo in alto a destra dell'interfaccia.



![Image](assets/fr/033.webp)



La scheda "*Dettagli RPC*" visualizza tutte le informazioni necessarie per la connessione. Scegli la connessione tramite Tor Address (in `.onion`).



![Image](assets/fr/034.webp)



Inseriscu questi dati nei campi corrispondenti del wallet Sparrow, quindi fai clic sul pulsante "*Test Connection*".



![Image](assets/fr/035.webp)



Se la connessione va a buon fine, apparirà una spunta verde e un messaggio di conferma.



![Image](assets/fr/036.webp)



Il segno di spunta in basso a destra dell'interfaccia Sparrow wallet, sarà ora verde (a indicare una connessione diretta con Bitcoin Core).



**Nota:** Affinché la connessione vada a buon fine, il nodo deve essere sincronizzato al 100%. In caso contrario, attendi la fine dell'IBD.



### Collegarsi a Electrs



Se il nodo dispone di un indicizzatore, è meglio collegarsi ad esso piuttosto che utilizzare direttamente Bitcoin Core, in quanto le query saranno elaborate più rapidamente.



Su Sparrow, vai alla scheda "*Private Electrum*".



![Image](assets/fr/037.webp)



Dovrai quindi inserire diverse informazioni per stabilire la connessione con il tuo indicizzatore. Questi dati si trovano nell'applicazione "*Electrs*" (o, se del caso, "*Fulcrum*") su Umbrel.



Selezionare la scheda "*Tor*" per ottenere la connessione all'indirizzo `.onion`. Se si desidera collegare un software mobile wallet, è anche possibile scansionare direttamente il codice QR.



![Image](assets/fr/038.webp)



È sufficiente inserire l'indirizzo Tor del proprio server Electrum nel campo "*URL*", quindi fare clic sul pulsante "*Test Connection*".



![Image](assets/fr/039.webp)



Se la connessione è riuscita, vengono visualizzati una spunta e un messaggio di conferma.



![Image](assets/fr/040.webp)



La spunta nell'angolo inferiore destro dell'interfaccia Sparrow wallet diventerà blu (il colore associato alla connessione a un server Electrum).



**Nota:** Affinché la connessione funzioni, l'indicizzatore deve essere sincronizzato al 100%. In caso contrario, attendere il completamento del processo di indicizzazione.



Ora sai come collegare il wallet al tuo nodo Bitcoin! Nel prossimo capitolo, ti presenterò diverse applicazioni aggiuntive disponibili su Umbrel a cui sono particolarmente affezionato e che vi permetteranno di migliorare l'uso quotidiano di Bitcoin attraverso il vostro nodo.




## Panoramica delle applicazioni disponibili


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel offre un vasto archivio di applicazioni. Come vedrai, ci sono molti strumenti legati a Bitcoin, ma anche un'ampia varietà di applicazioni in campi molto diversi: soluzioni di self-hosting per servizi e file, applicazioni di produttività, strumenti finanziari più generali, gestione dei media, sicurezza e amministrazione della rete, sviluppo, intelligenza artificiale, social network e persino domotica.



In questo corso BTC 202 ci concentreremo esclusivamente sulle applicazioni legate a Bitcoin. Tuttavia, sentiti libero di esplorare il resto del catalogo per trovare gli strumenti che potrebbero esserti utili.



Naturalmente, sarebbe impossibile elencare qui tutte le applicazioni Bitcoin. In questo capitolo, vorrei presentarti gli strumenti essenziali che faciliteranno e arricchiranno il tuo uso quotidiano di Bitcoin.



### Mempool.space



Nell'uso quotidiano di Bitcoin, se c'è uno strumento veramente indispensabile è il Block Explorer. Accessibile online o installato localmente, trasforma i dati grezzi della blockchain in un formato strutturato, chiaro e di facile lettura. È inoltre dotato di un motore di ricerca che consente agli utenti di individuare rapidamente un blocco, una transazione o un indirizzo specifico.



In concreto, l'explorer consente di stimare le commissioni necessarie per l'inclusione di una transazione in un blocco, quindi di seguirne l'andamento: scoprire se è probabile che venga inclusa nel prossimo futuro, a seconda del mercato delle commissioni, e infine confermare che è stata effettivamente inclusa in un blocco. Offre inoltre la possibilità di analizzare le transazioni passate e di consultarne lo storico. In breve, è il coltellino svizzero del bitcoiner.



Come accennato in precedenza, un explorer può essere ospitato online su un sito web o eseguito localmente sul tuo computer. Uno dei principali svantaggi dei servizi online è che possono compromettere la privacy. Senza VPN o Tor, il server che ospita l'explorer può collegare il tuo IP Address alle transazioni che stai visualizzando, il che può fornire un punto di ingresso ideale per l'analisi della catena.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Inoltre, il tuo Internet Service Provider (ISP) potrebbe sapere che state visualizzando una determinata transazione tramite il sito block explorer. Ciò solleva anche una questione di fiducia: dovrai fare affidamento sul servizio online per ottenere informazioni accurate sulle tue transazioni, senza poterne verificare personalmente la veridicità.



Ecco perché è sempre meglio utilizzare il proprio block explorer locale. In questo modo, nessun dato relativo alla tua attività di ricerca trapela, poiché tutte le query vengono elaborate direttamente su un dispositivo che controllate, senza passare da Internet. Inoltre, un explorer locale si basa sui dati del tuo nodo Bitcoin, che hai convalidato tu stesso, secondo le tue regole, e di cui ti puoi fidare.



Umbrel offre diversi esploratori di blocchi:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Sono particolarmente appassionato di Mempool.Space, che ho installato sul mio nodo. Attenzione: per utilizzare la maggior parte dei block explorer su Umbrel, è necessario un indicizzatore di indirizzi. È quindi necessaria l'applicazione Bitcoin Node (o Bitcoin Knots), che ha una blockchain sincronizzata al 100%, e un indicizzatore come Electrs o Fulcrum, anch'esso sincronizzato al 100%.



Una volta installata l'applicazione, è sufficiente aprirla per accedere al proprio explorer.



![Image](assets/fr/041.webp)



Per saperne di più sull'uso dell'explorer Mempool.Space, ti consiglio di consultare questa guida completa:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Lightning Node



Ora che hai il tuo nodo Bitcoin, puoi creare anche il tuo nodo Lightning per effettuare transazioni off-chain, senza affidarti a un'infrastruttura di terzi.



Umbrel offre una serie di applicazioni per aiutarti a rendere operativo il tuo nodo Lightning. È già possibile scegliere tra due implementazioni principali:




- LND, tramite l'applicazione *Lightning Node*;
- Core Lightning.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

È quindi possibile amministrare il nodo dall'interfaccia principale oppure, per ottenere funzionalità ancora maggiori e opzioni avanzate, installa *Ride The Lightning* o *ThunderHub*. Questi strumenti ti forniranno un sistema di gestione dell'interfaccia basato sul web molto più completo per il vostro nodo.



https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Infine, ti consiglio l'applicazione *Lightning Network+*, che ti permette di trovare dei pari con cui aprire dei canali, consentendovi di effettuare transazioni in contanti sia in uscita che in entrata.



![Image](assets/fr/089.webp)



Grazie a Umbrel, la gestione di un nodo Lightning personale è semplificata, ma rimane comunque relativamente complessa. Per questo motivo vi consiglio di seguire il corso LNP 202, che rappresenta il naturale proseguimento del corso BTC 202 e nel quale vi accompagno passo dopo passo nell’installazione e nella gestione del vostro nodo Lightning su Umbrel.



### Tailscale



Un'altra applicazione che mi piace particolarmente su Umbrel è Tailscale. È un'applicazione VPN progettata per semplificare la creazione di reti sicure tra più dispositivi, ovunque essi si trovino nel mondo. A differenza delle VPN tradizionali, che si basano su server centralizzati, Tailscale utilizza il protocollo WireGuard per stabilire connessioni crittografate end-to-end tra i vari computer. Ciò significa che è possibile implementare una VPN funzionante in pochi minuti, senza dover ricorrere a complicate configurazioni di rete.



Su Umbrel, l'installazione di Tailscale collega il nodo Bitcoin al proprio network privato virtuale. Una volta configurato, il nodo ottiene un indirizzo IP Tailscale privato, accessibile solo da altri dispositivi connessi alla stessa rete Tailscale (come computer, smartphone e tablet). Questa connessione è crittografata end-to-end e non passa attraverso una rete pubblica non protetta, migliorando notevolmente la sicurezza rispetto a una connessione non crittografata.



![Image](assets/fr/090.webp)



In concreto, Tailscale offre diversi vantaggi nell'utilizzo di Umbrel:





- Potete amministrare l'interfaccia Umbrel o accedere alle applicazioni collegate al vostro nodo (come Mempool, Ride The Lightning, ThunderHub...) da qualsiasi luogo, come se foste sulla stessa rete locale, senza esporre le porte su Internet e senza passare per Tor, che è molto lento;





- È possibile collegarsi al proprio server Electrum (Electrs o Fulcrum) o direttamente a Bitcoin Core tramite la propria VPN, aggirando Tor. In questo modo si ottiene una connessione sicura, paragonabile all'utilizzo di Tor, ma con una velocità molto più elevata e una latenza ridotta. In breve, si mantengono i vantaggi di Tor in termini di privacy e sicurezza, pur godendo della velocità di una connessione Clearnet. Per un wallet on-chain, questo guadagno può sembrare marginale, ma se avete intenzione di creare un vostro nodo Lightning in un secondo momento, la differenza è notevole. Infatti, effettuare pagamenti tramite il proprio nodo in movimento su Tor è estremamente lento a causa dei numerosi scambi necessari, mentre con Tailscale funziona perfettamente.





- Non è necessario configurare regole NAT, aprire porte o configurare un server VPN convenzionale. Una volta installata l'applicazione su Umbrel e sui vostri dispositivi, la rete viene stabilita automaticamente.



Tailscale su Umbrel è quindi una soluzione molto interessante se si vuole accedere al proprio nodo da qualsiasi parte del mondo in modo sicuro, performante e facile da configurare, senza sacrificare la privacy o la sicurezza.



Per installare e configurare Tailscale su Umbrel, consultare questo tutorial, sezione 4: "*Using Tailscale on Umbrel*":



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, acronimo di "*Notes and Other Stuff Transmitted by Relays*", è un protocollo aperto e decentralizzato progettato per consentire la pubblicazione e lo scambio di messaggi su Internet senza dipendere da una piattaforma centralizzata. Ogni utente possiede una coppia di chiavi crittografiche: la chiave pubblica (`npub`), che serve come identificatore, e la chiave privata (`nsec`), utilizzata per firmare i messaggi e garantirne l'autenticità.



I messaggi vengono trasmessi attraverso un network di relay indipendenti. Questa architettura distribuita rende Nostr resistente alla censura: nessun singolo server controlla l'accesso o la distribuzione e un utente può connettersi a tutti i relay che desidera.



Questo protocollo è molto popolare all'interno della community Bitcoin perché, come Bitcoin, Nostr affronta questioni di sovranità digitale e controllo dei dati. Il suo creatore, Fiatjaf, è uno sviluppatore già riconosciuto nell'ecosistema per i suoi numerosi contributi.



Con il tuo Umbrel, puoi ottimizzare l'uso di Nostr. Installando l'applicazione ***Nostr Relay***, puoi ospitare il vostro relay privato direttamente sul vostro computer, assicurandoti che tutti i tuoi post e le tue interazioni su Nostr siano salvati localmente e non vadano persi a causa della cancellazione da parte dei relay pubblici.



I client Nostr ***noStrudel*** o ***Snort*** sono disponibili anche su Umbrel. Grazie a queste applicazioni, è possibile pubblicare, leggere, cercare profili e interagire con l'ecosistema Nostr direttamente dall'interfaccia web sul proprio Umbrel.



Infine, c'è l'applicazione ***Nostr Wallet Connect*** su Umbrel, che consente di effettuare pagamenti Lightning nativi all'interno di Nostr. In pratica, puoi collegare il tuo futuro nodo Lightning ai tuoi client Nostr per inviare micropagamenti, chiamati "*zaps*", per premiare un contenuto o interagire economicamente, senza passare per un servizio di terze parti. Questi pagamenti partono direttamente dal tuo nodo personale tramite i tuoi canali.



Per scoprire come utilizzare tutte queste applicazioni, ti consiglio di dare un'occhiata a questo tutorial completo:



https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Server BTCPay



[BTCPay Server](https://planb.academy/resources/glossary/btcpay-server) è un processore di pagamento gratuito e open-source che consente di accettare pagamenti tramite Bitcoin e Lightning Network senza intermediari, mantenendo la custodia dei fondi.



L'architettura di BTCPay Server è basata su un nodo Bitcoin e, per Lightning, su un'implementazione compatibile (LND, Core Lightning...), il che lo rende una delle uniche soluzioni PoS totalmente non custodiale. È anche il software più completo per la tracciabilità e la contabilità.



![Image](assets/fr/091.webp)



Se siete titolari di un'attività commerciale e desiderate accettare pagamenti Bitcoin direttamente tramite il vostro nodo Umbrel, l'applicazione BTCPay Server è l'ideale per voi. Per saperne di più su questo argomento, vi consiglio di consultare le seguenti risorse:





- Il corso BIZ 101 sull'utilizzo i Bitcoin nella vostra azienda:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Il corso POS 305 sull'utilizzo del server BTCPay:



https://planb.academy/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Il tutorial sul server BTCPay:



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Concetti avanzati e best practice


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Mantenere il proprio nodo Umbrel


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Per dare il via a questa sezione finale e prima di passare alla teoria più avanzata, in questo breve capitolo vorrei esaminare le migliori pratiche e le azioni concrete che puoi intraprendere una volta che il tuo nodo Umbrel è installato, sincronizzato e configurato correttamente. Come mantenerlo quotidianamente?



### Mantenere in salute le attrezzature



Un nodo affidabile inizia con un hardware stabile. Assicurati che il dispositivo che ospita il nodo sia adeguatamente ventilato, privo di polvere e installato in un ambiente asciutto, lontano da fonti di calore e umidità. Evita di stipare il dispositivo in uno spazio ristretto e opta per una posizione ben ventilata.



Su Raspberry Pi e mini-PC, la polvere finisce per intasare i dissipatori di calore, aumentando la temperatura e portando al throttling (limitazione volontaria dell'uso delle risorse), che a sua volta si traduce in un calo dell'efficienza del nodo. Per questo motivo consiglio di pulire periodicamente la presa d'aria e la ventola, idealmente ogni pochi mesi.



Assicurarsi di utilizzare un alimentatore di alta qualità, in quanto una tensione instabile può causare la corruzione del sistema e persino un rischio di incendio. L'ideale sarebbe utilizzare l'alimentatore originale fornito dal produttore del dispositivo. Attenzione anche al surriscaldamento dovuto all'effetto Joule delle ciabatte: rispetta sempre la potenza massima consentita e non collegare mai più ciabatte in cascata.



Consiglio anche di investire in un UPS. Questo protegge il nodo da arresti improvvisi, permette a Umbrel di spegnersi in modo pulito in caso di interruzione e garantisce la continuità del funzionamento durante le microinterruzioni o i guasti di breve durata.



Per quanto riguarda l'archiviazione, tenere d'occhio i progressi: se il disco si sta avvicinando alla saturazione, considerare la possibilità di liberare spazio (disinstallare le applicazioni inutilizzate, regolare le impostazioni dell'indicizzatore) o migrare a un SSD più grande. Lo svantaggio di un nodo Bitcoin completo è che i suoi requisiti di archiviazione aumentano continuamente, poiché ogni 10 minuti viene generato un nuovo blocco e i vecchi blocchi non possono essere cancellati (a meno che il nodo non sia pruned). Vi consiglio quindi di prevedere una capacità sufficientemente ampia al momento dell'acquisto dell'hardware (minimo 2 TB).



### Aggiornamento



Gli aggiornamenti dei nodi sono importanti per tre motivi principali: in primo luogo, la sicurezza (patch di vulnerabilità, indurimento del network e protezione DoS); in secondo luogo, la compatibilità (modifiche alla politica dei relay, cambiamenti di formato e aggiornamenti di protocollo); in terzo luogo, l'affidabilità e le prestazioni (correzioni di bug, consumo di risorse e altri miglioramenti). Controlla quindi periodicamente che UmbrelOS e le tue applicazioni siano aggiornate:





- Per aggiornare il sistema: Apri il menu delle impostazioni, quindi fai clic sul pulsante "*Verifica aggiornamento*" accanto al parametro "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Per aggiornare le applicazioni: Accedi all'App Store. Se una delle applicazioni richiede un aggiornamento, nell'angolo in alto a destra dell'interfaccia apparirà un pulsante con una bolla rossa. È sufficiente fare clic su di esso, quindi aggiornare ogni applicazione.



Esegui questa operazione regolarmente per mantenere aggiornati il sistema operativo e le applicazioni.



### Backup



Se si utilizza il proprio nodo Bitcoin solo per convalidare e distribuire le transazioni, ma i wallet sono gestiti al di fuori di Umbrel (ad esempio, con un hardware wallet e un Sparrow wallet), non c'è nulla di cui eseguire il backup direttamente su Umbrel. In questo caso, il backup essenziale rimane quello della frase di recupero e del Descriptor del vostro wallet esterno, e questo vale sia che usi il tuo nodo sia che non lo usi. Quindi non cambia nulla rispetto alla configurazione precedente.



D'altra parte, a seconda delle applicazioni aggiuntive utilizzate su Umbrel, potrebbero essere necessari ulteriori backup. Ciò è particolarmente vero se si utilizza un nodo Lightning su Umbrel. In questo caso, è assolutamente necessario eseguire il backup del seed fornito al momento dell'installazione del nodo Lightning. Oltre al seed, è necessario un ***Static Channel Backup (SCB)*** aggiornato per poter ripristinare il nodo Lightning in caso di problemi. L'SCB consente di recuperare i fondi chiudendo forzatamente i canali. Se manca il seed o l'SCB, è impossibile ripristinare un nodo Lightning.



Umbrel offre anche la possibilità di eseguire il backup automatico e dinamico di questo SCB sui propri server, tramite Tor, per garantire che sia sempre disponibile un file aggiornato. In questo caso, per ripristinare il nodo è necessario solo il seed.



Rivedremo questi aspetti in dettaglio nel prossimo corso LNP202.



### Sicurezza operativa quotidiana



In termini di sicurezza, utilizza una password lunga, unica e casuale per l'interfaccia Umbrel e ricorda di attivare l'autenticazione a due fattori (2FA). Per le applicazioni che offrono protezione sia con password che con 2FA, attivale sempre entrambe e modifica le password predefinite.



Non esporre mai la dashboard a Internet senza utilizzare un gateway sicuro (come una VPN, Tor o un accesso solo locale). Limita il numero di applicazioni installate e cancella regolarmente quelle non più necessarie per ridurre la superficie di attacco.



Per approfondire le tue conoscenze sulla sicurezza informatica in generale, ti consiglio di dare un'occhiata a quest'altro corso gratuito:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnosi e auto-aiuto



In caso di bug su Umbrel, innanzitutto genera un bundle di diagnostica tramite la sezione di risoluzione dei problemi di UmbrelOS o dell'applicazione interessata, quindi riavvia l'applicazione in modo pulito. Se necessario, tenta anche un riavvio completo del sistema.



Se il problema persiste, ti consiglio di [unirti alla comunità di utenti Umbrel su Discord](https://discord.gg/efNtFzqtdx). Inizia a cercare se qualcuno ha già incontrato la stessa difficoltà e ha trovato una soluzione. In caso contrario, è possibile inviare un messaggio nel canale `general-support`. Si può anche utilizzare [il forum di Umbrel](https://community.umbrel.com/).



Questi siti vi permetteranno non solo di seguire gli annunci e gli aggiornamenti sulla sicurezza, ma anche di porre domande e, in ultima analisi, di aiutare altri utenti. È spesso in questi scambi che si scoprono le migliori pratiche.



Con queste semplici abitudini, il vostro tuo Umbrel rimarrà stabile, sicuro e utile, sia per te che per il network Bitcoin.




## Comprendere l'IBD e il processo di scoperta tra pari


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Il nodo Bitcoin si avvia senza alcuna conoscenza preliminare della cronologia delle transazioni. Inizialmente, è solo un computer che esegue un software (Bitcoin Core o simile). Per diventare un nodo Bitcoin completamente sincronizzato e operativo, deve ricostruire localmente lo stato del registro controllando tutti i blocchi pubblicati dal [blocco genesis](https://planb.academy/resources/glossary/genesis-block) (blocco 0, pubblicato da Satoshi Nakamoto il 3 gennaio 2009). Questa fase è chiamata **IBD (_Initial Block Download_)**.



L'IBD consiste nello scaricare e verificare ogni blocco e transazione individualmente, applicando le regole del consenso, per costruire la propria versione della blockchain. L'obiettivo non è semplicemente recuperare una copia di dati non verificati, ma arrivare alla stessa conclusione in modo completamente indipendente, come la maggioranza onesta del network.



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
- [Nonce](https://planb.academy/resources/glossary/nonce)



![Image](assets/fr/094.webp)



Le transazioni vengono impegnate in un Merkle Tree. Si tratta di una struttura che riassume un grande insieme di dati (in questo caso, tutte le transazioni del blocco) aggregando i loro hash progressivamente a due a due fino a un'unica "radice", dimostrando così l'appartenenza di un elemento all'insieme (e rilevando eventuali modifiche). In questo modo, qualsiasi modifica a una transazione modifica anche la radice del Merkle Tree e quindi l'impronta digitale dell'intestazione del blocco. [SegWit](https://planb.academy/resources/glossary/segwit) ha introdotto un ulteriore commitment separato per i witness data(firme), collocate nel coinbase.



![Image](assets/fr/095.webp)



Questo passaggio _**headers-first**_ permette al nodo di identificare il ramo con più lavoro (indipendentemente dal numero di blocchi), che è il ramo su cui i nodi Bitcoin si sincronizzano. Una volta identificato questo ramo, il nodo scarica il contenuto dei blocchi in parallelo da diverse connessioni, quindi convalida ogni transazione: formato, validità degli script (tranne `assumevalid=1`), importi, e assenza di doppia spesa. A ogni verifica andata a buon fine, lo stato attuale delle monete non spese (UTXO set) viene aggiornato nel database `chainstate/`: gli output spesi vengono rimossi, mentre vengono aggiunti nuovi output validi.



La Mempool, invece, entra in gioco solo quando ci si avvicina alla punta della catena: finché il nodo rimane in ritardo, non ha transazioni in sospeso da memorizzare.



Una volta completato l'IBD, il nodo entra nella sua fase normale: convalida i nuovi blocchi man mano che vengono pubblicati, mantiene la sua Mempool con le transazioni in sospeso in base alle sue regole di relay, trasmette transazioni e blocchi e gestisce eventuali riorganizzazioni della catena.



### AssumeValid



Bitcoin Core incorpora un meccanismo progettato per ridurre il tempo necessario prima che un nodo sia completamente operativo, pur mantenendo l'essenza del principio di verifica autonoma: [AssumeValid](https://planb.academy/resources/glossary/assume-valid).



Il parametro `assumevalid` si basa su un blocco di riferimento passato, il cui hash è integrato in ogni versione del software. Durante l'IBD, se il nodo scopre che questo blocco si trova effettivamente sul ramo con più lavoro, può ignorare la verifica dello script per tutte le transazioni precedenti a questo punto.



Tutte le altre regole (struttura dei blocchi, Proof of Work, limiti di dimensione, importi delle transazioni, UTXO, ecc.) continuano ad essere verificate integralmente. Solo il calcolo delle scritture precedenti a questo blocco di riferimento viene ignorato. L'aumento delle prestazioni è significativo sull'IBD, poiché la verifica delle firme rappresenta una parte importante del carico della CPU. Dopo questo blocco di riferimento, la verifica ritorna allo stato normale.



È possibile forzare la convalida completa di tutti gli script disabilitando questo meccanismo, al costo di un IBD molto più lungo, utilizzando il parametro `assumevalid=0` nel file `Bitcoin.conf`.



### AssumereUTXO



`assumeutxo` è un altro parametro esistente, ma a differenza di `assumevalid`, non è attivato di default. Questo meccanismo consente al software di caricare un'istantanea dell'insieme UTXO, insieme ai suoi metadati, e di considerarlo provvisoriamente come uno stato di riferimento, dopo aver verificato che le intestazioni portino effettivamente alla blockchain con il maggior numero di lavori.



Il nodo diventa così rapidamente operativo per gli usi comuni (RPC, connessione di wallet, ecc.), avviando contemporaneamente la ricostruzione completa e verificata del proprio UTXO set in background. Una volta completata questa fase, lo snapshot iniziale viene sostituito dallo stato ricostruito localmente. Questo approccio separa la fornitura rapida di nodi dalla verifica completa, senza compromettere quest'ultima.



### Individuazione dei peer: Come fa il nodo a trovare il network Bitcoin?



Quando un nodo si avvia per la prima volta, non conosce ancora alcun peer. Tuttavia, deve trovare altri nodi Bitcoin su Internet per richiedere headers, quindi blocchi, al fine di completare il suo IBD. Per avviare queste connessioni, Bitcoin Core segue una logica di priorità.



![Image](assets/fr/096.webp)



Quando il nodo si riavvia dopo essere stato utilizzato, Core tenta innanzitutto di riconnettersi ai peer in uscita registrati prima dello spegnimento, informazioni memorizzate nel file `anchors.dat`. Quindi, consulta il suo libro di indirizzi IP **`peers.dat`**, che memorizza l'elenco dei peer incontrati in precedenza, per riconnettersi ad essi. Si tratta semplicemente di un file locale, aggiornato e conservato da Core. D'altra parte, per un nuovo nodo appena lanciato, questi due file sono vuoti, poiché non ha mai comunicato con altri nodi Bitcoin .



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



Nella stragrande maggioranza dei casi, la fase di *DNS seed* è sufficiente per stabilire le prime connessioni con altri nodi. Se, eccezionalmente, questi server non rispondono entro 60 secondi, il nodo passa a un altro metodo: [un elenco statico di oltre 1.000 indirizzi](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) di _nodi seed_ è integrato nel codice di Bitcoin Core e viene aggiornato regolarmente. Se i primi due metodi per ottenere indirizzi IP falliscono, quest'ultima soluzione stabilisce una connessione iniziale, dalla quale il nodo può poi richiedere nuovi indirizzi IP.



![Image](assets/fr/097.webp)



Come ultima risorsa, è possibile forzare manualmente gli indirizzi IP forniti tramite il file `peers.dat` per forzare connessioni specifiche.



Una volta avviato, il gestore di indirizzi interno diversifica le fonti (reti autonome separate, Clearnet e Tor, oltre a varie aree geografiche) per ridurre il rischio di isolamento topologico. Il nodo stabilisce le connessioni in uscita (connessioni che seleziona da solo e che sono quindi più sicure).



Se il nodo è in ascolto su una porta aperta (per impostazione predefinita, 8333), accetta le connessioni in entrata. Queste rafforzano la resilienza complessiva del network fornendo un punto di contatto per i nuovi nodi, senza apportare alcun beneficio particolare al proprio IBD. Se il nodo funziona su Tor, la logica rimane la stessa, ma gli indirizzi utilizzati sono servizi `.onion`.




## Anatomia del tuo nodo Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Quando il nodo ha completato la sincronizzazione iniziale, memorizza localmente diversi set di dati complementari, che gli consentono di convalidare blocchi e transazioni, servire i peer della rete e riavviarsi rapidamente mantenendo il proprio stato. 3 colonne portanti sono essenziali in un nodo:




- i **blocchi** della blockchain memorizzati su disco,
- l'insieme **UTXO** mantenuto in un database chiave-valore,
- e la **Mempool** viene memorizzato nella RAM e serializzata periodicamente.



Inoltre, diversi file ausiliari (pari, preventivi, liste di esclusione, wallet, ecc.) completano il quadro. Scopriamo il ruolo di tutti questi file.



### Dove si trovano effettivamente i dati del nodo?



Per impostazione predefinita, Bitcoin Core salva i propri dati in una specifica directory di lavoro. Sotto GNU/Linux, questa si trova solitamente in `~/.Bitcoin/`, sotto Windows in `%APPDATA%\Bitcoin/` e sotto macOS in `~/Library/Application Support/Bitcoin/`. Se si utilizza una soluzione preconfezionata (ad esempio, all'interno di una distribuzione di nodi), questa directory può essere montata altrove, ma la sua struttura rimane la stessa. Le sottocartelle e i file importanti descritti di seguito si trovano ancora qui.



![Image](assets/fr/098.webp)



### I blocchi



LA blockchain è quindi un insieme di blocchi. Un full node memorizza questi blocchi come ["flat file"](https://it.wikipedia.org/wiki/Flat_file) sequenziali e mantiene un indice parallelo per un rapido recupero. Quando è necessario (nel caso di riorganizzazione, wallet rescan, peer service), questi dati vengono riletti così come sono.



**Nota:** Una riorganizzazione, o risincronizzazione, è un fenomeno in cui la blockchain subisce una modifica della sua struttura a causa dell'esistenza di blocchi concorrenti alla stessa altezza. Ciò accade quando una porzione della blockchain viene sostituita da un'altra catena con una maggiore quantità di lavoro accumulato. Queste risincronizzazioni sono una parte naturale del funzionamento di Bitcoin, dove diversi miner possono trovare nuovi blocchi quasi contemporaneamente, dividendo così il network di Bitcoin in due. In questi casi, il network può temporaneamente dividersi in catene concorrenti. Alla fine, quando una di queste catene accumula più lavoro, le altre catene vengono abbandonate dai nodi e i loro blocchi diventano noti come "blocchi obsoleti" o "blocchi orfani" Questo processo di sostituzione di una catena con un'altra è chiamato risincronizzazione.



#### File Blk*.dat (dati grezzi dei blocchi)



I blocchi ricevuti e convalidati vengono scritti in contenitori sequenziali denominati `blkNNNN.dat`, memorizzati nella cartella `blocks/`. Ogni file viene riempito in sequenza fino a raggiungere la dimensione massima di 128 MiB, a quel punto Core apre il file successivo. All'interno, ogni blocco è serializzato in formato di network, preceduto da un "magic identifier" (una sequenza di byte fissa che segnala l’inizio del blocco e il tipo di rete), e una lunghezza. Questa organizzazione consente una scrittura veloce su disco e facilita il servizio di blocco per la sincronizzazione dei peer.



![Image](assets/fr/099.webp)



In modalità pruned, il nodo conserva solo una finestra recente di questi file per limitare l'ingombro su disco. Elimina i contenitori `blk*.dat` più vecchi non appena viene raggiunto l'obiettivo di spazio configurato, pur conservando una cronologia sufficiente per rimanere coerente con la catena più conosciuta. L'indice e l'UTXO set rimangono normali, consentendo la convalida delle transazioni e dei blocchi successivi.



#### File Rev*.dat (dati di cancellazione)



Per poter tornare indietro nel tempo durante una riorganizzazione, Core salva, parallelamente a ogni file `blk`, un file `revNNNN.dat` in `blocks/`. Questo file contiene le informazioni necessarie per annullare l'effetto di un blocco sul set di UTXO: per ogni uscita consumata dal blocco, viene memorizzato lo stato precedente dell'UTXO corrispondente (quantità, script, altezza...). In caso di interruzione del blocco, il nodo può ricostituire rapidamente lo stato precedente senza dover riesaminare l'intera catena.



![Image](assets/fr/100.webp)



#### Indice dei blocchi (blocchi/indice)



La ricerca di un blocco direttamente nei flat file richiederebbe troppo tempo. Core mantiene quindi un database [LevelDB](https://planb.academy/resources/glossary/leveldb) in `blocks/index/` che elenca, per ogni blocco noto, metadati quali hash, altezza, stato di validazione, file `blk` e offset in cui si trova. Quando un peer richiede un blocco, o quando un componente interno deve accedere a un blocco specifico, questo indice fornisce un accesso rapido. Senza questo indice, sarebbero necessarie troppe operazioni.



![Image](assets/fr/101.webp)



#### Indici opzionali (indici/)



Alcuni indici sono opzionali e disabilitati per impostazione predefinita, in quanto aumentano l'ingombro su disco:




- `indexes/txindex/`, di cui abbiamo già parlato, fornisce una tabella di mappatura della →località delle transazioni, rendendo possibile recuperare qualsiasi transazione confermata senza conoscere il blocco che la contiene. Questo è utile per le interrogazioni fuori dal wallet di tipo `getrawtransaction`, ma è piuttosto costoso.
- `indexes/blockfilter/` che può contenere filtri a blocchi compatti (BIP157/158) per i thin client. Queste strutture accelerano la verifica dal lato client a scapito della memorizzazione aggiuntiva sull'indexer node(nodo indicizzatore).



### UTXO set (chainstate)



Il modello UTXO (*Unspent Transaction Output*) è la rappresentazione contabile di Bitcoin: ogni output non speso è un "coin" disponibile che può essere utilizzato come input per una transazione futura.



![Image](assets/fr/102.webp)



L'insieme di tutte queste parti in un dato momento T costituisce l'insieme UTXO: un grande elenco di tutte le parti ora disponibili. È questo stato che il nodo consulta per decidere se una transazione spende unità legittime non già utilizzate in una transazione precedente (per evitare il double-spending).



![Image](assets/fr/103.webp)



L'insieme UTXO è memorizzato nella cartella `chainstate/` come database LevelDB compatto. Ogni parte associa una chiave derivata dall'hash della transazione e l'indice di uscita con un valore contenente: l'importo, il blocco `scriptPubKey`, l'altezza del blocco di creazione e un indicatore [coinbase](https://planb.academy/resources/glossary/coinbase-transaction).



![Image](assets/fr/104.webp)



Il nodo mantiene una cache di memoria sopra LevelDB per assorbire le operazioni frequenti di lettura e scrittura. Il parametro `dbcache` può essere usato per modificare la dimensione di questa cache: più è grande, più accessi alla memoria beneficiano l'IBD e la convalida corrente, al costo di un maggiore consumo di RAM. Quando un nuovo blocco viene trovato da un miner, il nodo cancella dall'insieme UTXO gli output spesi (o consumati) dalle transazioni incluse nel blocco e aggiunge le uscite appena create.



Teoricamente, si potrebbe convalidare una transazione ricontrollando la cronologia dei blocchi per verificare che un'uscita non sia mai stata spesa. In pratica, tuttavia, ciò richiederebbe troppo tempo, poiché l'intera blockchain dovrebbe essere scansionata per ogni nuova transazione. l'UTXO set, pertanto, fornisce la visualizzazione minima necessaria per dimostrare localmente e in tempi ragionevoli l'assenza del double-spending.



Si noti che l'UTXO set è spesso al centro delle preoccupazioni sulla decentralizzazione di Bitcoin, poiché le sue dimensioni aumentano naturalmente in modo rapido. Ciò è dovuto in parte all'aumento del prezzo di Bitcoin, che incoraggia la frammentazione delle parti, e in parte alla crescente adozione del sistema: più utenti ci sono, maggiore è la richiesta di UTXO.



![Image](assets/fr/105.webp)



La crescita dell'insieme UTXO deriva anche dalla struttura delle semplici transazioni di pagamento su Bitcoin. Infatti, quando si effettua un pagamento, si consuma un singolo UTXO come input e si creano due nuovi UTXO come output (uno per il pagamento e l'altro come resto). Infine, un'euristica di analisi della catena, chiamata [CIOH](https://planb.academy/resources/glossary/cioh) (*Common Input Ownership Heuristic*), fornisce un ulteriore incentivo a evitare il consolidamento della moneta.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Poiché una parte di esso deve essere mantenuta nella RAM per verificare le transazioni in un tempo ragionevole, l'insieme UTXO può gradualmente rendere troppo costoso il funzionamento di un full node. Per risolvere questo problema, esistono già alcune proposte, in particolare Utreexo.



### La Mempool



La Mempool è l'insieme locale delle transazioni valide che sono state ricevute ma non ancora confermate. Come promemoria, una "transazione confermata" è una transazione che è stata inclusa in un blocco valido. Ogni nodo mantiene la propria Mempool, che può differire da quello degli altri nodi della rete a seconda di:




- la dimensione allocata alla Mempool tramite il parametro `maxmempool`: un nodo con una Mempool più grande sarà in grado di contenere più transazioni di un nodo con una Mempool più piccola (a meno che quest'ultimo non diventi vuoto);
- le regole della Mempool: costituiscono un sottoinsieme delle regole di inoltro del nodo e definiscono le caratteristiche che una transazione non confermata deve rispettare per essere accettata nella Mempool;
- percolazione delle transazioni: a causa di vari fattori, una determinata transazione può essere stata distribuita in una parte del network, ma non ancora raggiunta da un'altra.



È importante notare che le Mempool dei nodi non hanno valore in termini di consenso. Bitcoin funziona perfettamente anche se ogni nodo ha una Mempool diversa. In definitiva, i blocchi autorevoli sono sempre quelli aggiunti alla blockchain. Ad esempio, anche se un nodo inizialmente rifiuta una determinata transazione nella sua Mempool (valida secondo le regole del consenso), sarà obbligato ad accettarla se alla fine viene inclusa in un blocco con una Proof of Work valida. Se non lo facesse e rifiutasse questo blocco, pur essendo conforme alle regole di consenso, innescherebbe un hard fork, cioè la creazione di un nuovo Bitcoin separato in cui sarebbe solo.



#### Policy e gestione della memoria



Quando riceve una transazione, Core applica una serie di controlli rispetto alle regole del consenso (sintassi, script validi, assenza di doppie spese, ecc.) e alle regole Mempool, che rappresentano una politica locale ([RBF](https://planb.academy/resources/glossary/rbf-replacebyfee), soglie minime di addebito, limite di dati nel `OP_RETURN`, ecc.) Se la transazione rispetta queste regole, viene memorizzata.



La dimensione della Mempool è limitata dal parametro `maxmempool` nel file `Bitcoin.conf` (maggiori informazioni nel prossimo capitolo). Per impostazione predefinita, il limite è di 300 MB. Quando è piena, il nodo aumenta dinamicamente la soglia di carica minima ed espelle per prime le transazioni meno redditizie (cioè, conserva le transazioni che dovrebbero essere estratte per prime). Le transazioni troppo vecchie possono anche scadere dopo un ritardo configurato.



#### Persistenza su disco della Mempool



Per accelerare i riavvii, Core serializza periodicamente lo stato della Mempool nel file `Mempool.dat` quando il nodo viene spento. Oltre alla Mempool vera e propria, che rimane in memoria, Core memorizza questo file `Mempool.dat` su disco. Al successivo avvio del nodo, ricarica questo snapshot e cancella tutto ciò che non è più valido per la blockchain corrente.



### File ausiliari e database



Diversi altri file allo stesso livello di `blocks/`, `chainstate/` e `indexes/` partecipano al corretto funzionamento del sistema:




- `peers.dat` mantiene un elenco di indirizzi IP di potenziali peer, alimentato dalla scoperta iniziale del DNS, dagli scambi di rete e dalle aggiunte manuali. Quando il nodo si avvia, può attingere a questo file per stabilire le connessioni in uscita.
- Quando il nodo viene spento, `anchors.dat` salva gli indirizzi dei peer uscenti, in modo da poter provare a ricontattarli rapidamente al successivo avvio.
- `banlist.json` contiene i divieti locali decisi dall'operatore o dal nodo (comportamenti ripetuti non validi), al fine di impedire al nodo di riconnettersi o accettare connessioni da questi specifici peer.
- `fee_estimates.dat` memorizza le statistiche sull'orizzonte temporale delle conferme osservate, utilizzate dallo stimatore delle tariffe per proporre tariffe coerenti con gli obiettivi di ritardo scelti durante la creazione di una transazione.
- `bitcoin.conf` contiene i parametri di configurazione del tuo nodo. È in questo file che si possono regolare le regole di inoltro. Ne parlerò più in dettaglio nel prossimo capitolo;
- `settings.json` contiene parametri aggiuntivi a `Bitcoin.conf`.
- `debug.log' è il registro di testo diagnostico, che può essere usato per capire l'attività del nodo in caso di bug.
- `bitcoind.pid` registra l’identificatore del processo durante l’esecuzione, consentendo ad altre applicazioni o script di identificare facilmente Bitcoind (*Bitcoin Daemon*) e di interagire con esso, se necessario. Viene creato all’avvio del nodo e rimosso all’arresto;
- `ip_asn.map` è una tabella di mappatura IP → ASN (sistema autonomo) utilizzata per il bucketing e la diversificazione dei peer (opzione `-asmap`).
- `onion_v3_private_key` memorizza la chiave privata del servizio Tor v3 quando l'opzione `-listenonion` è abilitata, per mantenere stabile l'indirizzo onion tra i riavvii.
- `i2p_private_key` memorizza la chiave privata di I2P quando si usa `-i2psam=`, per effettuare connessioni in uscita ed eventualmente in entrata su I2P.
- `.cookie` contiene un RPC effimero di autenticazione (creato all'avvio e cancellato allo spegnimento) quando si utilizza l'autenticazione tramite cookie. Questo può essere utilizzato, ad esempio, per connettere il software wallet.
- `.lock` è il blocco della directory dei dati, che impedisce a più istanze di scrivere contemporaneamente sulla stessa directory dei dati.
- `guisettings.ini.bak` è il salvataggio automatico delle impostazioni della GUI (*Bitcoin Qt*) quando si usa l'opzione `resetguisettings`.



Come abbiamo visto nelle prime parti di questo corso, Bitcoin Core è sia il software del nodo Bitcoin che wallet. Tuttavia, non è necessariamente la soluzione che consiglierei per la gestione dei wallet, poiché la sua interfaccia rimane basica e le sue funzionalità sono limitate rispetto a software moderni come Sparrow o Liana. Core include anche i file per la gestione dei wallet:





- `wallets/` è la directory predefinita che ospita uno o più wallet;
- `wallets/<nome>/Wallet.dat` è il database SQLite del wallet (chiavi, descrittori, metadati delle transazioni, ecc.);
- `wallets/<name>/wallet.dat-journal` è il registro di rollback di SQLite.



Per riassumere, ecco la struttura del file Bitcoin Core:



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



Alla ricezione di un nuovo blocco, il nodo controlla la Proof of Work e, più in generale, il rispetto delle regole di consenso. Se tutto è a posto, applica le modifiche transazione per transazione al suo set dell'UTXO: controlla che ogni voce spenda le dell'UTXO esistenti con uno script valido, cancella queste UTXO e aggiunge le nuove uscite. Se tutto è valido, le modifiche vengono impegnate in `chainstate/`.



In parallelo, i dati di annullamento vengono scritti in `rev*.dat` e i metadati nell'indice `blocks/index/`. Il blocco viene quindi serializzato nel file `blk*.dat` corretto. In caso di riorganizzazione, il nodo legge `rev*.dat` al contrario per scollegare in modo pulito i blocchi abbandonati, ripristinare l'UTXO set e quindi collegare i blocchi della nuova catena migliore.





## Comprendere il file Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Il file `Bitcoin.conf` è il principale file di configurazione di interfaccia per Bitcoin Core. Permette di regolare il comportamento e i parametri del nodo senza dover ricompilare il codice sorgente o apportare modifiche alla riga di comando. In concreto, si tratta di un file di testo strutturato in coppie chiave-valore, il che significa che ogni riga del file fa riferimento a un parametro specifico (la chiave) e al suo valore associato, che può essere modificato per regolare quel parametro.



I parametri relativi alla rete, al relay delle transazioni, alle prestazioni, all'indicizzazione, al logging e all'accesso al RPC possono essere definiti nel file `Bitcoin.conf`. Tuttavia, questo file di configurazione non modifica mai le regole di consenso del protocollo: imposta solo la politica locale del nodo (regole di relaying), il modo in cui si connette, indicizza ed espone i servizi.



### Posizione e priorità



Per impostazione predefinita, `Bitcoin.conf` risiede nella directory dei dati di Bitcoin Core. Si tratta della famosa directory di cui abbiamo parlato nel capitolo precedente. Tuttavia, questo file non viene creato automaticamente da Bitcoin Core, tranne in alcuni ambienti, come Umbrel. Se non esiste già, dovrete crearlo voi stessi creando un file chiamato `Bitcoin.conf` e aprendolo con un editor di testo per apportare le vostre modifiche.



I parametri definiti nel file `Bitcoin.conf` possono essere sovrascritti da 2 livelli:




- `settings.json` (scritto dinamicamente dall'interfaccia grafica o da qualche RPC),
- e le opzioni modificate tramite linee di comando.



Si noti che qualsiasi modifica a `Bitcoin.conf` richiede il riavvio del nodo per avere effetto.



### Formato e struttura



Il formato del file `Bitcoin.conf` è quindi molto semplice: una riga per opzione, nella forma `opzione=valore`. Gli spazi inutili e le righe vuote vengono ignorati e i commenti al codice iniziano con `#`.



Quasi tutte le opzioni booleane possono essere disabilitate con il prefisso `no`. Ad esempio, `listen=0` e `nolisten=1` sono equivalenti a seconda della versione.



Per segmentare la configurazione per rete, si possono usare le sezioni: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. In alternativa, è possibile anteporre al nome dell'opzione il prefisso `regtest.maxmempool=100`.



### Cosa può e non può fare Bitcoin.conf



Come spiegato sopra, le regole di consenso non sono ovviamente configurabili in `Bitcoin.conf`, in quanto ciò potrebbe creare un hard fork. D'altra parte, molti altri aspetti sono configurabili. Ci sono 3 classi utili da tenere a mente:




- Parametri puramente locali. Hanno effetto solo sul proprio nodo: dimensione della cache (`dbcache`), modalità pruned (`prune`), indici opzionali... Influenzano le prestazioni della propria macchina, ma non il network.
- Politiche di relay e Mempool. Queste decidono ciò che il nodo accetta, conserva e rilancia prima della conferma: soglia minima della tassa (`minrelaytxfee`), dimensione e tempo di conservazione della Mempool (`maxmempool`, `mempoolexpiry`), sostituzione delle transazioni (RBF)... Queste regole non fanno parte del consenso, quindi due nodi diversi possono avere politiche diverse ed essere comunque pienamente compatibili. D'altra parte, questi parametri avranno un'influenza sul network Bitcoin (come spiegato nella prima parte, in particolare con la teoria della percolazione).
- Connettività di rete. Queste opzioni determinano il modo in cui il nodo trova i peer, ascolta, attraversa un NAT, usa Tor o un proxy o limita la sua larghezza di banda. Danno forma alla topologia, ma non alterano il trasferimento delle transazioni.



La comprensione di questa separazione è fondamentale: se una transazione non è conforme alle regole del consenso, il nodo la rifiuterà in ogni caso. Ma una politica locale più rigida può rifiutarsi di trasmettere una transazione valida ai fini del consenso.



### Rete e topologia



Innanzitutto, è importante distinguere chiaramente tra i due tipi di connessione che un nodo Bitcoin può avere:




- Connessioni in uscita, avviate dal nostro nodo verso un altro nodo;



![Image](assets/fr/106.webp)





- Connessioni in entrata, avviate da un altro nodo verso il nostro.



![Image](assets/fr/107.webp)



Questi due tipi di connessione sono perfettamente in grado di scambiare gli stessi dati in entrambe le direzioni; non si tratta di limitare la direzione del flusso, ma solo di una differenza nell'iniziatore della connessione. Dal punto di vista del nostro nodo, le connessioni in uscita sono generalmente considerate più sicure, poiché siamo noi ad avviarle e a scegliere con precisione il nodo a cui connetterci, rendendo improbabile che la connessione sia malevola. Per impostazione predefinita, Bitcoin Core mantiene 10 connessioni in uscita (8 "*full-relay*" + 2 "*block-relay-only*").



Un full node aggiunge ulteriore valore alla rete accettando le connessioni in entrata. Il parametro `listen=1` abilita l'ascolto sulla porta predefinita 8333 della rete in questione, consentendo di ricevere queste connessioni in entrata sulla rete. Per funzionare, questa porta deve essere aperta anche sul router. In caso contrario, il nodo continuerà a funzionare solo con le connessioni in uscita, senza alcun impatto sull'uso personale di Bitcoin. La scelta di consentire o meno le connessioni in entrata è vostra; non esiste una "scelta migliore"



Se si preferisce non aprire una porta sul router, ma accettare comunque le connessioni in entrata, si può attivare il parametro `listenonion=1`. In questo modo si otterrà lo stesso risultato, ma solo attraverso il network Tor anziché attraverso clearnet.



A livello di rete, abbiamo anche:




- `addnode`: aggiunge un peer amico da contattare in aggiunta alla solita scoperta (può essere specificato più volte).
- `connect`: limita rigorosamente le connessioni all’indirizzo fornito (può essere specificato più volte). Core non si connetterà ad alcun altro nodo;
- `seednode`: è usato solo per compilare il book-address quando ci si connette a un nodo e poi ci si disconnette.
- `maxconnections`: definisce il limite massimo globale per le connessioni in entrata e in uscita. Per impostazione predefinita, questo parametro è impostato a 125, il che significa che il nodo non accetterà mai più di 125 connessioni.
- `maxuploadtarget` : limita l'upload per contenere la larghezza di banda su una finestra mobile di 24 ore. Questo limite non compromette la propagazione degli elementi recenti essenziali;
- `onlynet`: limita le connessioni in uscita solo ai network selezionati (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Ad esempio, se si vuole che il nodo si connetta al network Bitcoin solo tramite Tor, si può abilitare il parametro `onlynet=onion` e disabilitare le connessioni in entrata (o consentire anche le connessioni tramite Tor).
- `dnsseed`: consente o meno ai _DNS seed_ di richiedere peer quando la pool address locale è bassa (default: `1`, a meno che `-connect` o `-maxconnections=0`).
- `forcednsseed`: forza la richiesta di semi _DNS_ all'avvio, anche se gli indirizzi sono già disponibili (default: `0`).
- `fixedseeds`: Consente l'uso di *nodi seed* (elenco indirizzi codificato) se _DNS seeds_ fallisce o è disabilitato (predefinito: `1`).
- `dns`: Autorizza le risoluzioni DNS in generale (ad esempio, per `-addnode`/`-seednode`/`-connect`).



Per impostazione predefinita, il nodo comunica su clearnet, Tor e I2P. Ciò significa che i peer con cui si connette su clearnet possono vedere il tuo indirizzo IP pubblico e il tuo ISP sarà probabilmente in grado di rilevare che state gestendo un nodo Bitcoin (sebbene il [P2P Transport V2](https://planb.academy/resources/glossary/p2p-transport-v2) renda più difficile per un ISP origliare). Questo non è necessariamente un problema, ma se si vuole evitare qualsiasi perdita di queste informazioni, si può collegare il nodo esclusivamente tramite Tor.



Per essere completamente abilitati a Tor, è necessario forzare il Bitcoin Core a usare solo questa rete e a creare un servizio nascosto per le connessioni in entrata (se si desidera abilitarle). Nel file `Bitcoin.conf`, è necessario aggiungere questa configurazione:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Tutte le connessioni P2P passano attraverso Tor. Il tuo nodo riceve un indirizzo `.onion' per le connessioni in entrata, quindi non è necessario aprire alcuna porta sul router. Il tuo ISP vede solo il traffico Tor e i tuoi peer non sono a conoscenza del tuo indirizzo IP pubblico.



Per evitare la risoluzione DNS in chiaro, è possibile aggiungere `dnsseed=0` e `dns=0` alla configurazione. Sarà poi necessario fornire manualmente i peer `.onion` tramite `seednode=` o `addnode=`, poiché altrimenti la scoperta di nuovi nodi sarà difficile.



Ovviamente, se sei un principiante, ti consiglio di lasciar perdere tutte queste impostazioni di rete per il momento. La configurazione predefinita è spesso sufficiente.



### Mempool e politica dei relay



#### Parametri di base



Ecco i parametri di base che potete modificare nel vostro `Bitcoin.conf` per quanto riguarda la gestione della vostra Mempool e la trasmissione di transazioni non confermate:





- `maxmempool=<n>`: Limita la dimensione massima della Mempool locale a `<n>` megabyte (default: `300`). Quando il limite viene raggiunto, il nodo aumenta dinamicamente la soglia della tariffa effettiva e dà priorità alle transazioni meno redditizie (in base alla tariffa, non al valore assoluto) per rimanere al di sotto del limite. È possibile lasciare questa impostazione come predefinita. Aumentarla può essere utile se si lavora da soli o se si vuole avere una visione più precisa della congestione della Mempool e migliorare la stima delle tariffe. Al contrario, riducendola si risparmia RAM e, in misura minore, altre risorse di sistema.





- `mempoolexpiry=<n>`: Tempo massimo di conservazione delle transazioni non confermate in Mempool (in ore, valore predefinito: `336`). Dopo questo tempo, le transazioni vengono rimosse anche se rimane spazio disponibile.





- `persistmempool=1`: Salva uno snapshot della Mempool a riposo e la ricarica al riavvio (valore predefinito: `1`). Questo accelera il ripristino dopo il riavvio, evitando la necessità di riapprendere lo stato tramite la rete.





- `maxorphantx=<n>`: Numero massimo di transazioni orfane mantenute (input dipendenti da UTXO non ancora visti nell'UTXO set, default: `100`). Oltre questa soglia, le transazioni più vecchie vengono eliminate per evitare una crescita incontrollata della cache.





- `blocksonly=1` : Disattiva l'accettazione e la ritrasmissione delle transazioni non confermate ricevute dai peer (tranne permessi speciali). Il nodo scarica e annuncia solo i blocchi. Le transazioni create localmente possono comunque essere trasmesse (per utilizzare il nodo con il wallet). Questo riduce notevolmente la larghezza di banda e il consumo di RAM, a scapito dell'utilità per il relay e della totale mancanza di conoscenza della Mempool.





- `minrelaytxfee=<n>`: Tariffa minima (in BTC/kvB) al di sotto della quale le transazioni non vengono accettate nella Mempool del nodo e non vengono trasmesse ai peer (valore predefinito: `0,00001` = 1 sat/vB). Più alto è questo valore, più il nodo filtra in modo aggressivo le transazioni a basso costo.





- `mempoolfullrbf=1`: Accetta le transazioni RBF anche senza un'esplicita segnalazione RBF nella transazione sostituita. Con questa politica "*full-RBF*", una transazione che offre una tariffa più alta può sostituirne un'altra in Mempool se sono soddisfatte le altre condizioni di sostituzione.



Come promemoria, RBF è un meccanismo transazionale che consente al mittente di sostituire una transazione con una con commissioni più elevate per accelerare la conferma. Se una transazione con una commissione troppo bassa rimane bloccata, il mittente può utilizzare *Replace-by-fee* per aumentare la commissione e dare priorità alla transazione sostitutiva nelle Mempool e presso i miner.



#### Impostazioni avanzate e specifiche



Ecco le impostazioni avanzate per la Mempool e la politica dei relay. Se si è alle prime armi, non dovrebbe essere necessario modificare queste impostazioni:





- `datacarrier=1` : Consente il relay e (se il mining avviene tramite il nodo) l’inclusione di transazioni contenenti dati non finanziari tramite un output `OP_RETURN` (predefinito: `1`). Disattivare questo parametro riduce leggermente la superficie di spam dei dati non finanziari a scapito di una minore compatibilità con alcuni usi. In ogni caso, dovrai accettare gli `OP_RETURN` minati.





- `datacarriersize=<n>`: Dimensione massima (in byte) del `OP_RETURN` che il nodo trasmette (valore predefinito: `83`). L'abbassamento di questo valore limita i payload trasportati tramite `OP_RETURN`. Si noti che questo limite sarà rimosso per impostazione predefinita in una versione futura di Bitcoin Core.





- `bytespersigop=<n>`: Parametro che converte le transazioni di firma in byte equivalenti per la valutazione del limite del relay (default: `20`). Questo influenzerà l'accettazione delle transazioni ricche di `sigops` secondo le regole locali.





- `permitbaremultisig=1`: Consente la trasmissione di transazioni P2MS *bare-Multisig* (default: `1`). Questo è il modello di script più vecchio per stabilire condizioni di firma multipla su un UTXO (inventato nel 2011 da Gavin Andresen).





- `whitelistrelay=1`: Concede automaticamente l'autorizzazione al relay ai peer in entrata inseriti nella whitelist (default: `1`). Questi peer hanno le loro transazioni accettate dal relay anche se il nodo non è in modalità relay generale.





- `whitelistforcerelay=1`: Assegna il permesso "*forcerelay*" ai peer in whitelist con permessi predefiniti (default: `0`). Il nodo quindi inoltra le loro transazioni anche se sono già presenti nella Mempool, aggirando così i meccanismi anti-ridondanza.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Consente di associare un’interfaccia o un intervallo di indirizzi e di assegnare permessi dettagliati ai peer corrispondenti: `relay`, `forzelay`, `Mempool` (richiesta di contenuti Mempool), `noban`, `download`, `addr`, `bloomfilter`. Questo può essere utile per concedere un trattamento privilegiato a peer fidati (come gateway, LAN e servizi interni).





- `peerbloomfilters=1` : Attiva il supporto ai [filtri Bloom](https://planb.academy/resources/glossary/bloom-filter) (BIP37) per servire blocchi/transazioni filtrati ai client leggeri (predefinito: `0`). Attenzione, questo aumenta il carico sulle tue risorse.





- `peerblockfilters=1` : Fornisce filtri compatti BIP157 (*Neutrino*) ai peer (predefinito: `0`).





- `blockreconstructionextratxn=<n>`: Numero aggiuntivo di transazioni mantenute in memoria per ricostruire i blocchi compatti (predefinito: `100`). Migliora il successo delle ricostruzioni durante le sincronizzazioni compatte, al costo di un po' di memoria.



Come promemoria, tutte queste regole di relay non hanno alcun impatto sulla validità delle transazioni incluse in un blocco valido. Servono a regolare il vostro contributo al relay, a proteggere le vostre risorse e a rendere il vostro nodo prevedibile in ambienti limitati, ma non vi permettono mai di rifiutare i blocchi che rispettano le regole del consenso.



### Wallets



È inoltre possibile regolare il modo in cui vengono gestiti i wallet nel file `Bitcoin.conf`. Se non si utilizza wallet direttamente in Core, ma piuttosto un software di gestione esterno come Sparrow o Liana, questi parametri saranno di scarsa importanza:





- `addresstype=<legacy|p2sh-segwit|bech32|bech32m>` : Definisce il formato degli indirizzi generati dal wallet per la ricezione.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Forza il formato dell'indirizzo di resto (resto di un input su un singolo pagamento).





- `Wallet=<percorso>`: Carica un wallet esistente all'avvio (può essere ripetuto per caricare più wallet).





- `walletdir=<dir>`: Directory contenente i wallet (predefinita: `<datadir>/wallets` se esiste, altrimenti `<datadir>`). Questo può essere utile se si desidera memorizzare i wallet su un volume dedicato o criptato.





- `walletbroadcast=1`: Trasmette automaticamente le transazioni create dai wallet caricati (default: `1`). Impostare `0` se si desidera gestire la trasmissione tramite un altro canale.





- `walletrbf=1`: Abilita l'RBF opt-in per segnalare l'RBF su tutte le transazioni (default: `1`). Consente di aumentare le tariffe in un secondo momento in caso di transazione bloccata.





- `txconfirmtarget=<n>`: Obiettivo di conferma per la transazione (in numero di blocchi, default: `6`). Il wallet imposterà automaticamente la tariffa per la transazione da confermare entro questo numero di blocchi.





- `paytxfee=<amt>`: Tariffa fissa (BTC/kvB) applicata alle transazioni. Generalmente sconsigliato: è preferibile utilizzare la stima flessibile tramite `txconfirmtarget`.





- `fallbackfee=<amt>` : Tariffa di riserva (BTC/kvB) utilizzata se il sistema di stima non dispone di dati sufficienti (predefinito: `0.00`). Impostarla su 0 disattiva completamente la funzione di riserva.





- `mintxfee=<amt>`: Soglia minima (BTC/kvB) per la creazione di transazioni da parte di wallet (valore predefinito: `0,00001`). Il wallet rifiuterà di creare una transazione al di sotto di questa soglia.





- `maxtxfee=<amt>`: Limite assoluto alle commissioni totali per una transazione wallet (default: `0,10` BTC). Protegge da commissioni troppo alte che distruggerebbero inutilmente i bitcoin.





- `avoidpartialspends=1`: Seleziona gli UTXO per cluster(gruppo o insieme) di indirizzi per evitare spese parziali.





- `spendzeroconfchange=1`: Consente di riutilizzare un UTXO di resto non confermato come voce in una nuova transazione (default: `1`).





- `consolidatefeerate=<amt>`: Tasso massimo (BTC/kvB) oltre il quale il wallet evita di aggiungere più input del necessario per consolidare. Ciò consente di consolidare a prezzi bassi dei piccoli UTXO in uno più grande, e riduce i costi quando sono alti.


- `maxapsfee=<n>`: Budget per le spese aggiuntive (BTC, valore assoluto) che il wallet accetta di pagare per attivare l'opzione "*evita spese parziali*".





- `discardfee=<amt>`: Tasso (BTC/kvB) che indica la tolleranza a buttare via il resto aggiungendolo alle fee. Gli output che costerebbero più di un terzo del loro valore a questo tasso vengono eliminati.





- `keypool=<n>`: Dimensione della pool di indirizzi pre-generata (predefinito: `1000`). Valori troppo piccoli aumentano il rischio di ripristini incompleti.





- `disablewallet=1`: Avvia Bitcoin Core senza il sottosistema wallet e disabilita le RPC associate. Riduce la superficie di attacco e l'impronta se il nodo viene usato solo per la convalida/rilascio.



### Archiviazione, indicizzazione e prestazioni



Il file di configurazione consente anche di regolare i parametri relativi alla macchina. Questo può essere particolarmente importante se si dispone di risorse limitate o, al contrario, di una grande quantità di capacità disponibile:





- `datadir=<dir>`: Imposta la directory principale dei dati di Bitcoin Core.





- `blocksdir=<dir>`: Disaccoppia la posizione dei file dei blocchi (`blocks/blk*.dat` e `blocks/rev*.dat`) dalla `datadir`. Questo può essere utile per collocare l'archivio dei blocchi su un volume diverso, mantenendo la "state base" (`chainstate/`) su un supporto più veloce, ad esempio.





- `dbcache=<n>`: Imposta `<n>` in MiB alla cache del database (*LevelDB*) utilizzata dall'indice dei blocchi e dal `chainstate` (valore predefinito: `450`). Più alto è il valore, più veloce è l'IBD e la validazione corrente, al costo di un maggiore consumo di RAM.





- `prune=<n>`: Abilita il pruning dei file a blocchi e imposta un obiettivo di spazio su disco in MiB (predefinito: `0` = disabilitato; `1` = pruning manuale tramite RPC; `>=550` = pruning automatico al di sotto dell'obiettivo). Incompatibile con `txindex=1`. Il nodo rimane un nodo pienamente validante, ma non può più fornire la vecchia cronologia. Questa opzione è particolarmente utile se lo spazio su disco è limitato, ad esempio quando si installa un nodo sul computer di casa.





- `txindex=1` : Costruisce e mantiene un indice globale delle transazioni confermate. Indispensabile per alcune richieste (`getrawtransaction` fuori dal walleto) e per scopi di esplorazione, ma aumenta notevolmente l'utilizzo del disco. Incompatibile con la modalità ridotta.





- `assumevalid=<hex>`: Indica un blocco che si presume valido, consentendo di saltare i controlli di script per i suoi antenati (impostare `0` per controllare tutto). Si veda il capitolo precedente per ulteriori informazioni.





- `reindex=1`: Ricostruisce gli indici dei blocchi e lo stato (`chainstate`) dai file `blk*.dat` su disco. Ricostruisce anche gli indici attivi opzionali. È un'operazione che richiede molto tempo per riparare un database danneggiato o per attivare/disattivare in modo pulito indici pesanti.





- `reindex-chainstate=1`: Ricostruisce solo il `chainstate` dall'indice di blocco corrente. Preferibile quando i file di blocco sono sani.





- `blockfilterindex=<tipo>`: Mantiene gli indici dei filtri di blocco compatti (ad esempio, `basic`) usati dai thin client (BIP157/158) e da alcune RPC. Disabilitato per impostazione predefinita (`0`). Consuma ulteriore spazio su disco e tempo di indicizzazione.





- `coinstatsindex=1`: Mantiene un indice delle statistiche degli UTXO set gestito dalla chiamata `gettxoutsetinfo`. Utile per le verifiche e le metriche, eliminando la necessità di un costoso ricalcolo. Disattivato per impostazione predefinita.





- `carica blocco=<file>`: Importa i blocchi all'avvio da un file esterno `blk*.dat`. Si usa per precaricare la cronologia da una fonte offline (copia locale, supporto esterno) per accelerare l'inizializzazione.





- `par=<n>`: Imposta il numero di thread di verifica dello script (da `-10` a `15`, `0` = auto, `<0` = lascia libero questo numero di core). Permette di regolare il parallelismo della CPU durante la validazione. La modalità automatica è adatta nella maggior parte dei casi.





- `debuglogfile=<file>`: Specifica la posizione del registro `debug.log`.





- `shrinkdebugfile=1`: Riduce la dimensione di `debug.log` all'avvio (valore predefinito: `1` quando `debug` non è attivo).





- `settings=<file>`: Percorso del file delle impostazioni dinamiche `settings.json`.



### RPC accesso e sicurezza operativa



Infine, il file `Bitcoin.conf` consente di configurare i parametri di accesso al nodo. Sii cauto con queste impostazioni, soprattutto se sei agli inizi: evita di modificarle senza averne compreso a fondo le implicazioni, perché potrebbero introdurre delle vulnerabilità.





- `server=1`: Attiva il server JSON-RPC. Essenziale se si utilizza `bitcoind` tramite `bitcoin-cli` o un'applicazione di terze parti. Disattivare (`0`) su un nodo di pura convalida che non espone alcuna API o che utilizza già un server Electrum.





- `rpcbind=<addr>[:port]`: Server RPC in ascolto address/port. Per impostazione predefinita, l'ascolto avviene solo localmente (`127.0.0.1` e `::1`). Questo parametro viene ignorato se non viene definito anche `rpcallowip`. Usalo per limitare esplicitamente Interface.





- `rpcport=<port>`: Porta RPC (predefinita: `8332` su Mainnet, `18332` su Testnet, `38332` su bookmark, `18443` su regtest).





- `rpcallowip=<ip|cidr>`: Consente i client RPC da un determinato IP o subnet (può essere ripetuto). Da usare insieme a `rpcbind` per esporre l'API solo a un segmento fidato (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Metodo di autenticazione RPC consigliato (password con hash). Consente più inserimenti ed evita di memorizzare un segreto in chiaro.





- `rpccookiefile=<path>`: Percorso del cookie di autenticazione (predefinito: file `.cookie` sotto `datadir/`). Viene utilizzato per l'accesso locale da parte dello stesso utente senza gestire password persistenti. Ad esempio, si può usare per collegare il wallet Liana a Bitcoin Core sullo stesso dispostivo.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Autenticazione classica RPC con password in chiaro. Evitare di usarlo a favore di `rpcauth` o di un cookie.





- `rpcthreads=<n>`: Numero di thread per servire le chiamate RPC (valore predefinito: `4`). Aumentalo se si hanno picchi di chiamate elevati sul lato del monitoraggio o strumenti esterni.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist di API autorizzate. Riduce la superficie di attacco limitando i metodi accessibili.





- `rpcwhitelistdefault=1|0`: Comportamento predefinito della whitelist: se abilitato e viene utilizzata una whitelist, le chiamate non elencate vengono rifiutate. Questo può anche forzare un insieme vuoto predefinito (nessuna chiamata consentita), purché non ci sia nulla di esplicitamente elencato.





- `rest=1`: Abilita l'API REST pubblica (disabilitata per impostazione predefinita). Da esporre solo su una rete fidata (stessa cautela di JSON-RPC).





- `conf=<file>`: Specifica, solo sulla riga di comando, un file di configurazione di sola lettura. Utile per congelare un profilo di esecuzione (immutabile) sul lato operativo.





- `includeconf=<file>`: Carica un file di configurazione aggiuntivo (percorso relativo a `datadir/`). Permette la separazione dei ruoli: base comune + sovraccarico locale sensibile.





- `daemon=1` / `daemonwait=1`: Avvia `bitcoind` in background e, con `daemonwait`, attendi che l'inizializzazione finisca prima di consegnarla. Ciò facilita l'integrazione con i supervisori (systemd, runit).





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



Abbiamo finito di elencare la maggior parte dei parametri di configurazione. Questo file `Bitcoin.conf' costituisce quindi la vera dashboard del nodo: definisce la configurazione del network, la gestione della Mempool, l'uso del disco e della memoria, l'indicizzazione e l'amministrazione generale. Se vuoi saperne di più su questo file e crearne uno su misura per le tue esigenze, ti consiglio di usare [Jameson Lopp's generator](https://jlopp.github.io/Bitcoin-core-config-generator/).



Siamo giunti alla conclusione del corso BTC 202, che ti avrà permesso non solo di comprendere le basi del funzionamento dei nodi e della loro interazione all'interno del sistema, ma anche di crearne uno tuo. Ora sei un Bitcoiner sovrano, con il tuo wallet autocustodito, che trasmette le tue transazioni tramite il tuo nodo. Congratulazioni!



Ora potrai passare alla parte finale del corso, dove potrai valutare il corso BTC 202 e poi prendere il diploma per verificare che hai acquisito tutti i concetti trattati.



Ora hai diverse opzioni a disposizione. Il passo logico successivo è quello di creare un proprio nodo Lightning, che ti permetta di essere completamente indipendenti per le tue transazioni off-chain. Questo sarà l'argomento di un prossimo corso, che sarà pubblicato nell'autunno del 2025 sul Plan ₿ Academy.


https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

Nel frattempo, ti invito a scoprire il corso BTC 204, che ti consentirà di comprendere e padroneggiare i principi di protezione della privacy nell'utilizzo di Bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c


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
