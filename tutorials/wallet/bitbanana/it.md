---
name: BitBanana
description: Manager mobile per il vostro nodo Lightning
---

![cover](assets/cover.webp)



In questo tutorial imparerete a installare e configurare BitBanana su Android per controllare il vostro nodo Lightning dal vostro smartphone. Vedremo come collegare l'app alla vostra infrastruttura esistente (Umbrel, RaspiBlitz, myNode o qualsiasi nodo LND/Core Lightning), effettuare pagamenti Lightning, gestire i vostri canali da remoto, visualizzare i vostri ricavi da routing e fare il backup delle vostre configurazioni. Inoltre, imparerete le migliori pratiche di sicurezza per proteggere l'accesso al vostro nodo e come si confronta con Zeus, una popolare alternativa.



## Presentazione di BitBanana



BitBanana è un'applicazione mobile open source per Android che trasforma il vostro smartphone in un cruscotto completo per il controllo remoto del vostro nodo Lightning. A differenza dei portafogli Lightning, che incorporano un nodo locale sul telefono, BitBanana adotta una filosofia di controllo remoto al 100%: l'applicazione non contiene satoshi e si connette solo all'infrastruttura esistente.



Sviluppata da Michael Wünsch sotto licenza MIT, l'applicazione garantisce una trasparenza totale, senza raccolta di dati personali e con build riproducibili e verificate. BitBanana supporta nativamente LND e Core Lightning tramite URI standard (`lndconnect://` e `clngrpc://`), semplificando drasticamente la configurazione iniziale. L'applicazione riconosce anche LndHub e Nostr Wallet Connect per gli utenti che non dispongono di un nodo personale, anche se queste modalità operano in modo custodiale con funzionalità limitate.



L'interfaccia offre un accesso completo a tutte le funzioni critiche del nodo: invio e ricezione di pagamenti (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), gestione dei canali Lightning (apertura, chiusura, adeguamento delle commissioni, ribilanciamento), controllo avanzato delle monete e gestione della watchtower. BitBanana implementa anche diversi livelli di sicurezza: blocco biometrico, modalità stealth, PIN di emergenza e supporto Tor nativo per anonimizzare le connessioni.



## Piattaforme e installazione supportate



### Installazione



BitBanana è disponibile esclusivamente per Android 8.0 o versioni successive. L'applicazione non esiste su iOS e non è prevista alcuna versione. Questa limitazione si spiega con la storia del progetto: BitBanana è il diretto successore di Zap Android, originariamente sviluppato da Michael Wünsch, che ha deciso di continuare il suo lavoro sotto il proprio marchio. Zap era una famiglia di applicazioni separate (Zap Android, Zap iOS, Zap Desktop) sviluppate da diversi collaboratori con basi di codice separate. BitBanana sta portando avanti solo il ramo Android.



Inoltre, l'ecosistema iOS presenta notevoli vincoli normativi e tecnici per le applicazioni Lightning non custodite. Nel 2023, Apple ha rifiutato un aggiornamento di Zeus per "violazioni della licenza" e nel 2024 Phoenix Wallet ha abbandonato l'App Store statunitense a causa delle incertezze normative sui fornitori di servizi Lightning. Questi ostacoli spiegano il motivo per cui molti sviluppatori Lightning preferiscono Android, che offre una politica più aperta per le applicazioni non-custodiali.



Per Android sono disponibili tre metodi di installazione: Google Play Store (oltre 5000 installazioni, aggiornamenti automatici), F-Droid (build riproducibili, verifica del codice sorgente) o APK manuale da GitHub.



![BitBanana](assets/fr/01.webp)



Il sito web ufficiale di bitbanana.app (a sinistra) vanta "100% autosufficiente con ZERO raccolta dati". La schermata centrale mostra le tre opzioni di download: F-Droid (consigliato), Google Play e APK. La schermata a destra mostra l'autorizzazione alle notifiche per gli avvisi di pagamento.



L'applicazione richiede le autorizzazioni: rete (connessione al nodo), fotocamera (codici QR), NFC (LNURL), servizi in background (notifiche), biometria (sicurezza) e WireGuard VPN. Nessun tracker, nessuna raccolta di dati. Abilitate la password o il blocco biometrico per proteggere l'accesso.



## Configurazione iniziale



### Collegamento a un nodo LND



Per connettere BitBanana al vostro nodo LND (Umbrel, RaspiBlitz, myNode), ottenete un URI `lndconnect` o un codice QR contenente l'indirizzo, il certificato TLS e il macaron di autenticazione.



Per questa esercitazione, utilizzeremo un nodo LND tramite umbrel. Per maggiori dettagli, consultare il nostro tutorial dedicato:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Nell'applicazione Lightning Node, accedere al menu in alto a destra e selezionare "Connect wallet".



![BitBanana](assets/fr/04.webp)



Selezionare **gRPC (Tor)** per connettersi tramite Tor (consigliato). Vengono visualizzati il codice QR e i dettagli (Host .onion, Porta 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



In BitBanana, premere "CONNECT NODE", scansionare il codice QR o incollare l'URI. Autorizzare l'accesso alla telecamera, quindi controllare l'indirizzo .onion visualizzato prima di confermare.



**Connessione *Core Lightning



Se si utilizza Core Lightning (CLN) invece di LND, il processo rimane identico, con l'URI `clngrpc://` contenente i certificati TLS reciproci. Core Lightning supporta in modo nativo BOLT12 (offerte), consentendo di riutilizzare le fatture e i pagamenti ricorrenti, non disponibili su LND.



**Connessione senza nodo personale (LNbits/hosted)**



Se non si dispone di un nodo Lightning, BitBanana può connettersi ai servizi ospitati tramite LndHub (il protocollo utilizzato da BlueWallet e LNbits) o Nostr Wallet Connect (NWC). Attenzione: queste modalità operano in modalità di custodia (il servizio ospita i vostri fondi) con funzionalità limitate. Non sarà possibile gestire i canali o configurare le commissioni di routing e si potranno solo inviare e ricevere pagamenti Lightning.



Per maggiori dettagli su LNbits o Nostr Wallet Connect, consultare i nostri vari tutorial:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Uso quotidiano



### Interface principale



La schermata iniziale visualizza il saldo di Lightning, mentre il menu in alto a sinistra consente di accedere alle seguenti sezioni: Canali, Routing, Firma/Verifica, Nodi, Contatti, Impostazioni, Backup. L'icona dell'orologio (in alto a destra) apre la cronologia delle transazioni. I pulsanti "Invia" e "Ricevi" in basso consentono di inviare e ricevere i satoshi.



![BitBanana](assets/fr/05.webp)



### Pagamenti per fulmini e on-chain



![BitBanana](assets/fr/10.webp)



**Inviare un pagamento:** Premere il pulsante "Invia" dalla schermata iniziale. La schermata di pagamento (a sinistra) offre la possibilità di incollare un indirizzo o i dati di pagamento nel campo "Address o dati di pagamento", con uno scanner QR in alto a destra per la scansione dei codici. È anche possibile selezionare un contatto salvato nella sezione Contatti per evitare di dover effettuare la scansione ogni volta.



BitBanana riconosce in modo intelligente tutti i formati di pagamento: fatture Lightning classiche (stringhe di caratteri che iniziano con `lnbc`), Lightning Address (formato e-mail come `utilisateur@domaine.com`), codici LNURL-pay per pagamenti dinamici, LNURL-withdraw per il prelievo di fondi e persino pagamenti Keysend direttamente su una chiave pubblica Lightning senza una fattura precedente. L'applicazione esegue automaticamente le risoluzioni LNURL necessarie in background.



Una volta caricata la fattura, BitBanana visualizza tutti i dettagli: importo esatto, spese di instradamento stimate, descrizione del pagamento (se fornita dal destinatario) e data di scadenza della fattura. Dopo la conferma, il pagamento viene instradato attraverso i canali Lightning. Nei dettagli della transazione è possibile visualizzare il percorso effettuato, passaggio dopo passaggio, e le spese effettivamente pagate.



**Ricevere il pagamento:** Premere il pulsante "Ricevi". Un selettore (schermata di destra) permette di scegliere tra Lightning (pagamento istantaneo tramite i propri canali) e On-Chain. Per una ricevuta Lightning, inserire l'importo desiderato in satoshi (o lasciare a 0 per creare una fattura senza importo fisso da compilare per il pagatore) e aggiungere una descrizione opzionale da inserire nella fattura. BitBanana genera immediatamente una fattura Lightning con codice QR da scansionare. È anche possibile copiare la fattura come testo e inviarla via e-mail. Non appena il pagamento viene ricevuto, una notifica push avvisa l'utente e la transazione appare immediatamente nella cronologia con tutti i suoi dettagli.



### Canali e routing



![BitBanana](assets/fr/06.webp)



La sezione "Canali" mostra le capacità di invio/ricezione ed elenca i canali con avatar unici. Ogni canale mostra la sua liquidità suddivisa tra saldo locale e remoto. Toccare un canale per ottenere tutti i dettagli e le azioni (chiusura, modifica delle commissioni di instradamento). I tre punti in alto a destra danno accesso all'opzione "Riequilibrio" per riequilibrare la liquidità dei canali. Il pulsante "+" apre un nuovo canale.



La sezione Routing (schermata centrale) visualizza i ricavi da inoltro per periodo (1D, 1W, 1M, 3M, 6M, 1Y) con uno storico dettagliato degli inoltri per ottimizzare la strategia.



Firma/Verifica (schermata di destra) consente di firmare/verificare crittograficamente i messaggi per dimostrare il controllo del nodo.



### Nodi multipli e parametri



![BitBanana](assets/fr/07.webp)



**Gestione dei nodi**: elenca i nodi, con pulsanti per aggiungere manualmente, scansionare QR o passare da un nodo all'altro. In particolare, è possibile impostare diversi tipi di connessione allo stesso nodo: LAN, VPN o Tor.



**Gestione dei contatti**: memorizza i contatti Lightning per i pagamenti rapidi.



**Impostazioni**: personalizzazione di valuta, lingua, avatar. Sezione Sicurezza e privacy: App Lock (PIN/biometria), Hide balance (modalità stealth), Tor (anonimizzazione IP). Configurazione di oracoli di prezzi, esploratori di blocchi, stimatori di tariffe personalizzati.



## Vantaggi e limiti



**Salute: **




- Mobilità totale: controllo del nodo Lightning da qualsiasi luogo
- Funzionalità complete: pagamenti (LNURL, Lightning Address, BOLT 12), gestione dei canali, controllo delle monete, torri di guardia, multi-nodi
- Sicurezza: PIN/biometria, modalità stealth, PIN di emergenza, Tor nativo, blocco degli screenshot
- Gratuito, open source (MIT), zero commissioni, zero raccolta dati



**Limitazioni:**




- Richiede un nodo Lightning attivo (o LNbits in modalità custode)
- Non è prevista una versione iOS
- La protezione dell'accesso al telefono è fondamentale (macaroon admin = accesso totale al nodo)



## Le migliori pratiche



**Sicurezza:**




- Attivazione del blocco PIN/biometrico (impedisce l'accesso non autorizzato al nodo)
- Impostare un PIN di emergenza (cancella i dati sensibili in caso di necessità)
- Non condividete mai l'URI o l'amaretto di accesso
- Modalità stealth in ambienti ostili



**Login:**




- VPN mesh (Tailscale, ZeroTier): miglior compromesso tra velocità e sicurezza
- Tor: massima riservatezza, maggiore latenza
- Clearnet: evitare se non necessario (esposizione IP, porte aperte)



### Backup e ripristino



Infine, c'è il menu "Backup", che consente di salvare le configurazioni per la migrazione o la reinstallazione del telefono.



![BitBanana](assets/fr/08.webp)



**Importante: ** Il backup NON contiene i backup di seed o del canale (da eseguire sul nodo). Contiene: configurazioni del nodo (indirizzi, certificati, macaron), etichette, contatti, parametri. Il pulsante Ripristina consente di importare un backup esistente. È richiesta la conferma prima del salvataggio.



![BitBanana](assets/fr/09.webp)



Inserire una password di crittografia (schermata di destra). Il sistema apre il selettore di file (schermata sinistra) per salvare `BitBananaBackup_2025-XX-XX.dat`. Conferma "Backup creato".



**Sicurezza: ** Archiviare il backup in modo criptato (cloud personale, USB, NAS). Non condividere mai i file o le password. Testare regolarmente il ripristino. Il backup recupera le connessioni, non i fondi.



## BitBanana vs Zeus: Qual è la differenza?



Se state esplorando le applicazioni mobili per la gestione di un nodo Lightning, è probabile che vi imbattiate in Zeus, una popolare alternativa a BitBanana. A differenza di BitBanana, che si concentra esclusivamente sul controllo remoto di un nodo esistente, Zeus adotta un approccio più completo, offrendo due modalità di funzionamento: un nodo Lightning incorporato direttamente nell'applicazione (modalità embedded con LND integrato) e la connessione remota a un nodo esterno, proprio come BitBanana.



Questa doppia funzionalità rende Zeus particolarmente interessante per i principianti che desiderano sperimentare Lightning senza alcuna infrastruttura precedente. La modalità embedded consente l'avvio immediato con un nodo mobile completo, mentre gli utenti avanzati possono passare alla connessione remota una volta configurato il proprio nodo personale. Zeus supporta anche LND e Core Lightning per la connessione remota, come BitBanana.



Un altro grande vantaggio di Zeus è la sua disponibilità multipiattaforma (iOS e Android), mentre BitBanana rimane esclusivamente basato su Android. Zeus incorpora anche l'infrastruttura Olympus LSP per facilitare la ricezione di pagamenti Lightning attraverso canali just-in-time, un sistema Point of Sale per gli esercenti e una funzionalità di swap integrata per gestire la liquidità.



Tuttavia, BitBanana mantiene i suoi punti di forza specifici: un'interfaccia più semplice e snella, una migliore esperienza utente (UX) grazie all'attenzione esclusiva al controllo remoto e un approccio educativo con spiegazioni contestuali. Zeus offre maggiori funzionalità, ma al costo di un'interfaccia più complessa. L'applicazione rimane particolarmente adatta agli utenti che desiderano controllare un nodo esclusivamente a distanza, senza funzioni di custodia.



Per saperne di più su Zeus, date un'occhiata alle seguenti esercitazioni:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusione



BitBanana trasforma il vostro smartphone Android in un cruscotto Lightning completo, offrendo una mobilità senza precedenti agli operatori dei nodi. L'applicazione copre tutte le funzionalità: pagamenti (tutti i formati), gestione dei canali, controllo delle monete, torri di guardia, multi-nodo, con sicurezza potenziata (PIN/biometria, Tor, PIN di emergenza).



Interamente sovrano, BitBanana non raccoglie dati e non compromette né la riservatezza né il controllo dei vostri fondi. Il codice sorgente aperto (MIT) garantisce la trasparenza.



## Risorse



### Documentazione ufficiale




- [Sito web di BitBanana](https://bitbanana.app)
- [Documentazione completa](https://docs.bitbanana.app)
- [Codice sorgente GitHub](https://github.com/michaelWuensch/BitBanana)



### Installazione




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)