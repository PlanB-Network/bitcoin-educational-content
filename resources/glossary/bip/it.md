termine: BIP

Acronimo di "Bitcoin Improvement Proposal" (Proposta di Miglioramento di Bitcoin). Un Bitcoin Improvement Proposal (BIP) è un processo formale per proporre e documentare miglioramenti e cambiamenti al protocollo Bitcoin e ai suoi standard. Poiché Bitcoin non ha un'entità centrale che decide gli aggiornamenti, i BIP permettono alla comunità di suggerire, discutere e implementare miglioramenti in modo strutturato e trasparente. Ogni BIP dettaglia gli obiettivi del miglioramento proposto, le giustificazioni, gli impatti potenziali sulla compatibilità, così come i vantaggi e gli svantaggi. I BIP possono essere scritti da qualsiasi membro della comunità, ma devono essere approvati da altri sviluppatori e dagli editori che mantengono il database GitHub di Bitcoin Core: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun e Ruben Somsen. Tuttavia, è importante comprendere che il ruolo di queste persone nell'editing dei BIP non significa che controllino Bitcoin. Se qualcuno propone un miglioramento che non viene accettato all'interno del framework formale dei BIP, può comunque presentarlo direttamente alla comunità Bitcoin o anche creare un fork includendo la propria modifica. Il vantaggio del processo BIP risiede nella sua formalità e centralizzazione, che facilitano il dibattito per evitare divisioni tra gli utenti di Bitcoin, cercando di implementare aggiornamenti in modo consensuale. Alla fine, è il principio della maggioranza economica a determinare le dinamiche di potere all'interno del protocollo.

I BIP sono classificati in tre categorie principali:
* *BIP di Standards Track*: Riguardano modifiche che influenzano direttamente le implementazioni di Bitcoin, come le regole di validazione delle transazioni e dei blocchi;
* *BIP Informativi*: Forniscono informazioni o raccomandazioni senza proporre cambiamenti diretti al protocollo;
* *BIP di Processo*: Descrivono cambiamenti nelle procedure che circondano Bitcoin, come i processi di governance.

I BIP di Standards Track e Informativi sono anche classificati per "Layer":
* *Layer di Consenso*: I BIP in questo layer riguardano le regole di consenso di Bitcoin, come le modifiche alle regole di validazione dei blocchi o delle transazioni. Queste proposte possono essere soft forks (modifiche compatibili con le versioni precedenti) o hard forks (modifiche non compatibili con le versioni precedenti). Ad esempio, i BIP per SegWit e Taproot appartengono a questa categoria;
* *Servizi Peer*: Questo layer riguarda il funzionamento della rete dei nodi Bitcoin, ovvero come i nodi trovano e comunicano tra loro su Internet.
* *API/RPC*: I BIP di questo layer riguardano le Application Programming Interfaces (API) e le Remote Procedure Calls (RPC) che permettono al software Bitcoin di interagire con i nodi;
* *Layer delle Applicazioni*: Questo layer riguarda le applicazioni costruite sopra Bitcoin. I BIP in questa categoria trattano tipicamente di modifiche a livello degli standard dei portafogli Bitcoin.

Il processo di sottomissione di un BIP inizia con la concettualizzazione e la discussione dell'idea sulla mailing list *Bitcoin-dev*. Se l'idea è promettente, l'autore redige un BIP seguendo un formato specifico e lo sottomette tramite una Pull Request sul repository GitHub Core. Gli editori esaminano questa proposta per verificare che soddisfi tutti i criteri. Il BIP deve essere tecnicamente fattibile, vantaggioso per il protocollo, conforme al formato richiesto e in accordo con la filosofia di Bitcoin. Se il BIP soddisfa queste condizioni, viene ufficialmente integrato nel repository GitHub dei BIP. Viene poi assegnato un numero. Questo numero è generalmente deciso dall'editore, spesso Luke Dashjr, ed è assegnato in modo logico: i BIP che trattano argomenti simili ricevono spesso numeri consecutivi.

I BIP poi attraversano diversi stati nel corso della loro vita. Lo stato attuale è specificato nell'intestazione di ogni BIP:
* Bozza: La proposta è ancora nella fase di stesura e dibattito;
* Proposto: Il BIP è considerato completo e pronto per la revisione da parte della comunità;
* Rinviato: Il BIP è messo in attesa per il futuro dal promotore o da un redattore;
* Rifiutato: Un BIP è classificato come rifiutato se non mostra attività per 3 anni. Il suo autore può scegliere di riprenderlo in seguito, il che consentirebbe di ritornare allo stato di bozza;
* Ritirato: Il BIP è stato ritirato dal suo autore;
* Finale: Il BIP è accettato e ampiamente implementato su Bitcoin;
* Attivo: Solo per i BIP di processo, questo stato viene assegnato una volta raggiunto un certo consenso;
* Sostituito / Obsoleto: Il BIP non è più applicabile o è stato sostituito da una proposta più recente che lo rende non necessario.

![](../../dictionnaire/assets/25.png)

> ► *BIP è l'acronimo di "Bitcoin Improvement Proposal". In francese, può essere tradotto come "Proposition d'amélioration de Bitcoin". Tuttavia, la maggior parte dei testi in francese utilizza direttamente l'acronimo "BIP" come sostantivo comune, a volte femminile, a volte maschile.*