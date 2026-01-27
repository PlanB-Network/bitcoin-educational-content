---
name: 1ML
description: Imparare a utilizzare l'esploratore 1ML per comprendere e analizzare la rete Lightning di Bitcoin.
---
![cover](assets/cover.webp)



## Introduzione



Lightning Network è una soluzione di pagamento veloce e a basso costo costruita sulla base di Bitcoin, che consente transazioni istantanee e sicure. L'osservazione di questa rete è essenziale per capire come funziona, la sua topologia e lo stato dei nodi che la compongono. Un Lightning explorer, come 1ML, viene utilizzato per visualizzare i dati pubblici della rete, compresi i nodi attivi, i canali aperti e la capacità disponibile, fornendo una panoramica preziosa per utenti, sviluppatori e operatori dei nodi.



## Accedere a 1ML e comprendere la pagina iniziale



Per accedere all'1ML, basta aprire il browser web e digitare [https://1ml.com](https://1ml.com). Si accede così alla home page, che funge da cruscotto globale del Lightning Network.



![capture](assets/fr/03.webp)



Questa pagina visualizza diverse statistiche importanti nella parte superiore dello schermo, tra cui :





- Il **numero totale di nodi attivi** sulla rete, ovvero i computer coinvolti nell'invio e nella ricezione dei pagamenti Lightning.
- Il **numero di canali aperti**, che corrispondono alle connessioni tra questi nodi che consentono il trasferimento di fondi.
- La **capacità totale della rete**, espressa in bitcoin (BTC), che indica la somma delle capacità di tutti i canali pubblici.



Queste cifre vengono aggiornate regolarmente per riflettere lo stato attuale della rete. Danno un'idea delle sue dimensioni, della sua crescita e della sua solidità.



![capture](assets/fr/04.webp)



Subito sotto, la pagina offre elenchi con classifiche:





- I **nodi più connessi**, che hanno il maggior numero di canali aperti verso altri nodi.
- Le **capacità più elevate** dei nodi, che indicano quali nodi possono trasferire le quantità maggiori.
- I canali più importanti in termini di capacità.



I filtri possono anche essere utilizzati per affinare questi elenchi in base alla posizione geografica o ad altri criteri.



Questa pagina è il punto di partenza ideale per esplorare il Lightning Network e comprenderne la topologia generale.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Esplorazione dei nodi Lightning



Per esplorare un nodo su 1ML, utilizzare la barra di ricerca in cima alla pagina. È possibile inserire il **Node ID**, cioè l'identificatore unico del nodo, o il suo **alias**, che è un nome più facile da ricordare.



Una volta completata la ricerca, fare clic sul nodo corrispondente per accedere alla sua pagina dettagliata.



![capture](assets/fr/07.webp)



In questa pagina vengono visualizzate diverse informazioni importanti:





- ID nodo**: questo identificativo unico è una lunga stringa di caratteri che consente di identificare con precisione il nodo in tutta la rete.



![capture](assets/fr/08.webp)





- Alias**: è il nome scelto dal proprietario del nodo per rappresentarlo pubblicamente.



![capture](assets/fr/09.webp)





- Il **numero di canali** indica quante connessioni il nodo ha aperto con altri nodi, mentre la **capacità totale** rappresenta la somma dei bitcoin disponibili in questi canali. Un nodo con un gran numero di canali e un'elevata capacità è generalmente ben collegato e in grado di trasferire rapidamente grandi quantità di denaro attraverso la rete.



![capture](assets/fr/10.webp)





- L'**uptime**, o disponibilità, misura per quanto tempo un nodo è rimasto attivo e accessibile online, riflettendo la sua affidabilità. L' **età** del nodo, invece, indica da quanto tempo è presente sulla rete, riflettendo la sua stabilità e la sua esperienza all'interno del Lightning Network.



![capture](assets/fr/11.webp)



Questi dati aiutano a capire l'importanza e l'affidabilità di un nodo nella rete Lightning Network. Ad esempio, un nodo con un gran numero di canali, un'alta capacità e un elevato tempo di attività è spesso un attore importante della rete.



## Esplorare i canali dei fulmini



### Che cos'è un canale Lightning?



Un canale Lightning è una connessione diretta tra due nodi della rete. Consente a questi due nodi di scambiare pagamenti istantanei e a basso costo senza passare attraverso la catena principale del Bitcoin per ogni transazione. I canali sono la base che rende il Lightning Network veloce e scalabile.



### Leggere le informazioni sul canale su 1ML



Su 1ML, ogni canale ha una propria pagina o scheda descrittiva contenente una serie di dati importanti:



Dalla pagina di un nodo è possibile accedere all'elenco dei suoi canali. Facendo clic su un canale, 1ML visualizza una pagina dedicata con diverse informazioni chiave.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



I principali dati visibili sono i seguenti:





- Nodi partner**: ogni canale collega due nodi. 1ML visualizza entrambi gli identificatori e i rispettivi alias.



![capture](assets/fr/14.webp)





- Capacità del canale**: è la quantità totale di bitcoin bloccati in questo canale. Questa capacità rappresenta il limite massimo di pagamenti che possono transitare attraverso questo canale.



![capture](assets/fr/15.webp)





- Età del canale**: indica da quanto tempo il canale è aperto. Un canale vecchio è spesso segno di una relazione stabile tra due nodi.



![capture](assets/fr/16.webp)



### Limiti di visibilità del canale



È importante capire che 1ML mostra solo **parte** del Lightning Network. L'explorer mostra solo i **canali pubblici**, cioè quelli che sono stati annunciati in rete. I canali privati, spesso utilizzati per motivi di riservatezza o di strategia, non sono visibili. Inoltre, 1ML non mostra l'esatta distribuzione dei fondi su ciascun lato di un canale, né i pagamenti effettuati, né la liquidità effettivamente disponibile in un determinato momento. Le informazioni visualizzate possono quindi essere utilizzate per analizzare la **struttura generale della rete**, ma non la sua effettiva attività finanziaria o lo stato dettagliato della liquidità.



## Esplora Lightning Network per località



### Nodi per paese e regione



1ML consente di esplorare Lightning Network secondo una **dispartizione geografica**. Dalla home page o attraverso sezioni dedicate, è possibile visualizzare i nodi per paese o regione. Questa funzione si basa sulle informazioni di localizzazione dichiarate dagli operatori dei nodi.


Nella barra di navigazione è presente il link **Localizzazione**. Nella pagina, i nodi sono raggruppati per continente, paese e città.



![capture](assets/fr/17.webp)



Selezionando un Paese, 1ML visualizza un elenco di nodi associati, insieme a statistiche aggregate come il numero di nodi e la capacità totale visibile per quell'area geografica.



#### Cosa dice questo sull'adozione locale





- Adozione della tecnologia**: Un numero elevato di nodi in una regione indica che gli utenti, le aziende o i servizi Bitcoin stanno adottando attivamente il Lightning Network. Questo dimostra la maturità tecnologica e la volontà di sfruttare i vantaggi (transazioni veloci, costi inferiori) di Lightning. Questo dimostra la maturità tecnologica e la volontà di sfruttare i vantaggi di Lightning (transazioni veloci, costi inferiori).
- Ecosistema economico** : La fitta presenza di nodi può anche segnalare un tessuto economico locale intorno al Bitcoin: commercianti che accettano Lightning, startup che sviluppano strumenti, eventi comunitari, ecc.
- Sicurezza e resilienza**: La distribuzione geografica diversificata aumenta la resilienza della rete di fronte a interruzioni o restrizioni locali. Più i nodi sono dispersi, più la rete è decentralizzata e difficile da censurare.
- Politiche e normative**: Alcuni Paesi possono registrare un'adozione più rapida grazie a un quadro normativo favorevole o a una comunità proattiva. Al contrario, nelle aree in cui le normative sono rigide o ostili, il numero di nodi sarà inferiore.



#### Limiti dei dati geografici



Si tenga presente, tuttavia, che la geolocalizzazione dei nodi Lightning ha dei limiti e dei pregiudizi:





- Posizione IP approssimativa**: 1ML generalmente utilizza l'indirizzo IP pubblico dei nodi per stimare la loro posizione. Tuttavia, questo metodo può essere falsato dall'uso di VPN, server cloud (AWS, Google Cloud) o hosting in Paesi diversi dal domicilio effettivo del proprietario del nodo.
- Nodi virtuali**: Alcuni operatori ospitano i loro nodi su server remoti per motivi di affidabilità e disponibilità, il che può dare una falsa impressione della posizione fisica.
- Mobilità dell'utente**: L'operatore di un nodo può cambiare sede, spostare la propria infrastruttura o aprire diversi nodi in regioni diverse, rendendo più complessa la lettura dei dati.
- Invisibilità dei nodi privati**: Alcuni nodi non pubblicano il proprio indirizzo IP o utilizzano metodi per nascondere la propria posizione, rendendo impossibile la geolocalizzazione.



## casi d'uso concreti dell'1ML



### Comprendere la topologia della rete



1ML permette di visualizzare la **struttura generale di Lightning Network**. Osservando le connessioni tra i nodi, il numero di canali e la capacità complessiva, è possibile capire come è organizzata la rete, quali nodi hanno un ruolo centrale e come possono circolare teoricamente i flussi di pagamento.



Questa comprensione è essenziale per capire come funziona il Lightning Network, e non solo per l'uso del portafoglio.



### Identificare i nodi importanti



Grazie alle classifiche offerte da 1ML (nodi più connessi, maggiore capacità, età), è possibile identificare i nodi che occupano un posto importante nella rete. Questi nodi sono spesso i principali gateway per i pagamenti Lightning.



![capture](assets/fr/18.webp)



### Controllare la visibilità pubblica di un nodo



Per un operatore di nodo, l'1ML consente di verificare se il proprio nodo è **pubblicato** su Lightning Network. Se un nodo appare su 1ML, significa che è visibile e accessibile ad altri nodi per l'apertura di canali pubblici.


Questo può essere utile per diagnosticare problemi di visibilità o di connettività.



### Osservare l'evoluzione del Lightning Network nel tempo



Confrontando le statistiche globali in diversi periodi, 1ML ci permette di osservare l'evoluzione del Lightning Network: aumento o diminuzione del numero di nodi, variazioni della capacità totale o cambiamenti nella distribuzione geografica.


Queste osservazioni offrono un'interessante prospettiva sulla crescita, la maturità e le tendenze del Lightning Network.



## migliori pratiche e limiti dell'1ML



### Dati pubblici ≠ realtà completa



1ML si basa esclusivamente sui dati **pubblicati** su Lightning Network. Ciò significa che lo strumento mostra solo una parte della realtà. Molti canali potrebbero essere privati, alcuni nodi potrebbero non essere pubblicizzati e la liquidità effettiva disponibile nei canali non è visibile. È quindi essenziale utilizzare 1ML come strumento di analisi globale, non come rappresentazione esaustiva della rete.



### Privacy e fulmini



Lightning Network è stato progettato con una forte attenzione alla **privacy dei pagamenti**. Le singole transazioni non sono visibili su 1ML e i saldi esatti dei canali non sono pubblici. Questa limitazione non è una colpa dell'esploratore, ma una caratteristica fondamentale di Lightning Network, progettata per proteggere la privacy degli utenti.



### Non saltare alle conclusioni



Un nodo con una capacità elevata o con molti canali non è necessariamente più "affidabile" o "efficiente" in tutti i casi. Allo stesso modo, un calo temporaneo della capacità complessiva della rete non implica necessariamente un problema strutturale. I dati vanno sempre interpretati con il senno di poi e contestualizzati.



### Complementarietà con altri strumenti



l'1ML è un ottimo punto di partenza per l'esplorazione del Lightning Network, ma è meglio utilizzarlo insieme ad altri strumenti come i portafogli Lightning, le interfacce di gestione dei nodi e altri esploratori. Questo approccio fornisce una visione più completa e sfumata della rete.



## opzione di connessione 1ML (funzionalità avanzata)



1ML offre un'opzione di **log-in/creazione di un account**, visibile sul sito, ma questo non è **necessario** per visualizzare i dati del Lightning Network. Tutte le funzioni discusse finora in questo tutorial sono disponibili **senza account**.



La connessione è rivolta principalmente agli operatori di **nodi luminosi**. In particolare, consente di associare un nodo a un account 1ML per gestire alcune informazioni pubbliche, come la presentazione del nodo, i link di contatto e altri metadati. Questa funzione è pensata per migliorare la visibilità e l'identificazione di un nodo all'interno dell'explorer.



È importante notare che 1ML non è **un servizio di custodia**. La creazione di un conto non dà accesso a fondi, canali o pagamenti di un nodo. Serve solo a interagire con l'esploratore da un punto di vista dichiarativo e informativo.



Nel contesto dell'apprendimento o della scoperta del Lightning Network, questa opzione può quindi essere considerata **opzionale** e riservata a un uso più avanzato.



## Conclusione



1ML è uno strumento prezioso per osservare e comprendere la Lightning Network a partire dai suoi dati pubblici. Permette di esplorare la struttura della rete, di analizzare nodi e canali e di seguire l'evoluzione complessiva dell'adozione del Lightning Network nel tempo. Senza bisogno di un account o di gestire fondi, 1ML offre un accesso accessibile a chiunque voglia approfondire la comprensione del funzionamento di Lightning.


Se volete approfondire il tema del Lightning Network, vi consiglio di seguire il corso completo Introduzione al Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb