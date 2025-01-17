---
term: PIF

---
Acronimo di "Bitcoin Improvement Proposal" Una Bitcoin Improvement Proposal (BIP) è un processo formale per proporre e documentare miglioramenti e modifiche al protocollo Bitcoin e ai suoi standard. Poiché Bitcoin non ha un'entità centrale che decide sugli aggiornamenti, le BIP consentono alla comunità di suggerire, discutere e implementare miglioramenti in modo strutturato e trasparente. Ogni BIP descrive in dettaglio gli obiettivi del miglioramento proposto, le motivazioni, i potenziali impatti sulla compatibilità, nonché i vantaggi e gli svantaggi. I BIP possono essere scritti da qualsiasi membro della comunità, ma devono essere approvati da altri sviluppatori e dai redattori che gestiscono il database GitHub di Bitcoin Core: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun e Ruben Somsen. Tuttavia, è importante capire che il ruolo di queste persone nella modifica dei PIF non significa che controllino Bitcoin. Se qualcuno propone un miglioramento che non viene accettato all'interno del quadro formale del BIP, può comunque presentarlo direttamente alla comunità Bitcoin o addirittura creare un fork che includa la sua modifica. Il vantaggio del processo BIP risiede nella sua formalità e centralizzazione, che facilita il dibattito per evitare di dividere gli utenti di Bitcoin, cercando di implementare gli aggiornamenti in modo consensuale. Alla fine, è il principio della maggioranza economica a determinare le dinamiche di potere all'interno del protocollo.

I PIF sono classificati in tre categorie principali:


- Standard Track BIP*: Riguardano modifiche che influiscono direttamente sulle implementazioni di Bitcoin, come le regole di convalida delle transazioni e dei blocchi;
- PIF informativi*: Forniscono informazioni o raccomandazioni senza proporre modifiche dirette al protocollo;
- Processo BIP*: Descrivere i cambiamenti nelle procedure relative a Bitcoin, come i processi di governance.

I PIF di tipo Standards Track e Informational sono classificati anche per "Layer":


- Livello di consenso*: Le PIF di questo livello riguardano le regole di consenso di Bitcoin, come le modifiche alle regole di convalida dei blocchi o delle transazioni. Queste proposte possono essere soft fork (modifiche compatibili con il passato) o hard fork (modifiche non compatibili con il passato). Ad esempio, i BIP per SegWit e Taproot appartengono a questa categoria;
- Servizi Peer*: Questo livello riguarda il funzionamento della rete di nodi Bitcoin, cioè il modo in cui i nodi si trovano e comunicano tra loro su Internet.
- API/RPC*: I BIP di questo livello riguardano le Application Programming Interfaces (API) e le Remote Procedure Calls (RPC) che permettono al software Bitcoin di interagire con i nodi;
- Livello applicazioni*: Questo livello riguarda le applicazioni costruite sopra Bitcoin. I PIF di questa categoria si occupano tipicamente di modifiche a livello di standard dei portafogli Bitcoin.

Il processo di presentazione di un PIF inizia con la concettualizzazione e la discussione dell'idea sulla mailing list *Bitcoin-dev*. Se l'idea è promettente, l'autore redige una PIF seguendo un formato specifico e la invia tramite una richiesta di pull sul repository GitHub del Core. I redattori esaminano la proposta per verificare che soddisfi tutti i criteri. La PIF deve essere tecnicamente fattibile, vantaggiosa per il protocollo, conforme alla formattazione richiesta e in linea con la filosofia di Bitcoin. Se il PIF soddisfa queste condizioni, viene ufficialmente integrato nel repository GitHub dei PIF. Gli viene quindi assegnato un numero. Questo numero è generalmente deciso dall'editore, spesso Luke Dashjr, ed è assegnato in modo logico: I PIF che trattano argomenti simili ricevono spesso numeri consecutivi.

I BIP passano quindi attraverso diversi stati nel corso del loro ciclo di vita. Lo stato attuale è specificato nell'intestazione di ogni PIF:


- Bozza: La proposta è ancora in fase di elaborazione e di discussione;
- Proposta: Il PIF è considerato completo e pronto per essere esaminato dalla comunità;
- Rinviata: Il BIP viene messo in attesa per un secondo momento dal campione o da un editore;
- Rifiutato: Un PIF è classificato come rifiutato se non ha mostrato alcuna attività per 3 anni. Il suo autore può decidere di riprenderlo in seguito, il che gli permetterebbe di tornare allo stato di bozza;
- Ritirato: Il PIF è stato ritirato dal suo autore;
- Finale: Il PIF è accettato e ampiamente implementato su Bitcoin;
- Attivo: Solo per i PIF di processo, questo stato viene assegnato una volta raggiunto un certo consenso;
- Sostituito / Obsoleto: Il PIF non è più applicabile o è stato sostituito da una proposta più recente che lo rende superfluo.

![](../../dictionnaire/assets/25.webp)

> *BIP è l'acronimo di "Bitcoin Improvement Proposal". In francese può essere tradotto come "Proposition d'amélioration de Bitcoin". Tuttavia, la maggior parte dei testi francesi utilizza direttamente l'acronimo "BIP" come sostantivo comune, a volte al femminile, altre al maschile.*