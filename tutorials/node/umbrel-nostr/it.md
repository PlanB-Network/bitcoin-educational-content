---
name: Umbrel Nostr
description: Configurazione e utilizzo delle applicazioni Nostr su Umbrel
---

![cover](assets/cover.webp)



## Prerequisiti: Installazione di Umbrel



Umbrel è una piattaforma open-source che consente di ospitare facilmente le applicazioni Bitcoin e altri servizi sul proprio server personale. Si tratta di una soluzione all-in-one che semplifica notevolmente l'auto-ospitalità dei nodi Bitcoin e delle applicazioni decentralizzate.



Assicuratevi di aver installato Umbrel seguendo la nostra guida all'installazione:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Introduzione a Nostr



**Nostr** è un protocollo di rete aperto e decentralizzato progettato per il social networking. Il suo nome sta per _"Note e altre cose trasmesse dai relè"_. Consente a chiunque di pubblicare messaggi (note), gestiti come eventi JSON, e di propagarli attraverso i server relay anziché attraverso una piattaforma centralizzata. Ogni utente possiede una coppia di chiavi crittografiche (private/pubbliche) che servono come identificatore: la chiave pubblica (npub) identifica l'utente, mentre la chiave privata (nsec) permette di firmare i messaggi. Grazie a questa architettura distribuita, **Nostr offre resistenza alla censura** e grande flessibilità: è possibile utilizzare diversi client e connettersi a quanti relay si desidera, senza dipendere da un singolo server.



In breve, Nostr è un protocollo di comunicazione decentralizzato in cui i **clienti** (applicazioni utente) inviano e ricevono eventi tramite i **relayers** (server). Questo protocollo è stato particolarmente apprezzato dalla comunità Bitcoin a partire dal 2023, grazie ai suoi valori di decentralizzazione e sovranità dei dati.



**Nota: ** Per utilizzare Nostr, è necessaria la chiave privata (generata da un client Nostr o tramite un'estensione dedicata). **Non condividete mai la vostra chiave privata**, perché permetterebbe a chiunque di impersonarvi. Conservatela in un luogo sicuro e utilizzate strumenti sicuri per la gestione delle chiavi (vedi Suggerimento sotto).



## Applicazioni per ombrelli per Nostr



Umbrel offre un ecosistema di applicazioni integrate per sfruttare appieno Nostr sul proprio nodo personale. In questa sede illustreremo in dettaglio l'uso delle principali applicazioni legate a Nostr: **Nostr Relay**, **noStrudel**, **Snort** e **Nostr Wallet Connect**. Ognuna di esse risponde a un'esigenza specifica: _Nostr Relay_ è un **server privato**, _noStrudel_ e _Snort_ sono **client Nostr** (interfacce per la lettura/pubblicazione di note), mentre _Nostr Wallet Connect_ è uno strumento per collegare il vostro **portafoglio Lightning** a Nostr.



### Relè Nostr - Il vostro relè privato su Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** è l'applicazione ufficiale di Umbrel per gestire il proprio **relè Nostr** sul proprio nodo. L'obiettivo principale è quello di avere un relè **privato** e affidabile per il **backup di tutte le attività Nostr** in tempo reale. In altre parole, utilizzando questo relè personale in aggiunta ai relè pubblici, vi assicurate che tutte le vostre note, messaggi e reazioni siano copiate a casa, al sicuro dalla censura o dalla perdita di dati.



**Installazione:** Dall'App Store di Umbrel (categoria _Social_), installare _Nostr Relay_. Una volta lanciata, l'applicazione viene eseguita in background (servizio docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Il web Interface viene visualizzato tramite Umbrel: fornisce informazioni di base e, soprattutto, l'URL del vostro relè (in alto a destra), che dovrete copiare per utilizzarlo ulteriormente. È disponibile anche un pulsante di sincronizzazione (icona del globo).



**Per sfruttare il vostro relè Umbrel:**



**Aggiungere il relè al proprio client Nostr:** Nell'applicazione client (ad esempio Damus su iOS, Amethyst su Android, Snort o noStrudel su Umbrel, ecc.), aggiungere l'URL del relè privato copiato in precedenza. Per impostazione predefinita, il relay Umbrel ascolta sulla porta **4848**. Se si accede dalla rete locale, si ottiene un URL come: `ws://umbrel.local:4848` (oppure utilizzare l'IP locale di Umbrel).



Se si usa Tailscale (vedi sotto), si può anche usare l'alias DNS di MagicDNS (di solito `umbrel` o un nome generato automaticamente) per accedervi da qualsiasi luogo, sempre sulla porta 4848.



Se si preferisce Tor, ottenere il .onion Address di Umbrel e utilizzarlo con la porta 4848 tramite un browser o un client compatibile con Tor (vedere la sezione Tor)



Una volta aggiunto l'URL alla configurazione del relè del client Nostr, collegarsi a questo relè. Nel client si dovrebbe vedere che il relè Umbrel è connesso (di solito indicato da un punto Green o simile).



**Sincronizzare la cronologia (opzionale)**: Nella pagina web Interface di _Nostr Relay_ su Umbrel, fare clic sull'icona **globo** 🌐 (nella parte superiore della pagina). Questa azione costringerà il vostro relè Umbrel a connettersi agli altri relè (quelli configurati nel vostro client) per **importare le vostre vecchie attività pubbliche**. Ciò significa che le note passate che avete pubblicato o letto tramite i relè pubblici saranno scaricate e memorizzate anche sul vostro relè privato. Attendere la sincronizzazione.



**D'ora in poi, ogni nuova attività (note pubblicate, reazioni, messaggi privati criptati, ecc.) svolta su Nostr sarà inoltrata come di consueto ai relay pubblici** e in parallelo al vostro relay Umbrel. Se il vostro client Nostr è configurato correttamente, invierà ogni evento a tutti i relè (compreso il vostro). Il vostro relè privato fungerà da backup in tempo reale. Anche in caso di disconnessione temporanea, i vostri clienti potranno risincronizzare i dati mancanti in un secondo momento grazie a questo relè. questo vi dà il controllo completo sui vostri dati Nostr



Sullo sfondo, il _Nostr Relay_ di Umbrel è basato sul progetto open-source **nostr-rs-relay** (implementazione del protocollo Rust). Supporta l'intero protocollo Nostr e numerosi NIP standard (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, ecc.), garantendo la massima compatibilità con i clienti.



### noStrudel - client Nostr per gli esploratori



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** è un client web Nostr orientato all'utente, ideale per comprendere ed esplorare la rete Nostr in dettaglio. È una sorta di sandbox per ispezionare eventi e relè e per sperimentare le caratteristiche avanzate del protocollo. Interface è in inglese ed è relativamente tecnico, quindi ideale per gli utenti esperti che desiderano conoscere il funzionamento interno di Nostr.



**Installazione: ** Installare _noStrudel_ dall'App Store di Umbrel (categoria _Social_). Una volta lanciata, è possibile accedervi tramite il browser al Address di Umbrel (ad esempio `http://umbrel.local` o tramite il suo .onion/Tailscale, vedere la sezione Accesso esterno).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Configurazione dei relè: ** Quando si apre noStrudel, nell'angolo in alto a destra si trova il pulsante "Setup Relays". Fare clic su di esso per configurare i relè.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



In questa pagina, incollare l'URL del relè Umbrel copiato in precedenza. È possibile aggiungere anche altri relè proposti di default dall'applicazione. Una volta configurati i relè, fare clic su "Accedi" in basso a sinistra per continuare.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Connessione:** noStrudel offre diverse opzioni di connessione. Nel nostro caso, sceglieremo "Chiave privata" e incolleremo la chiave privata Nostr precedentemente generata. Se non avete ancora una chiave, potete installare l'estensione [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) per creare e/o salvare le vostre chiavi Nostr e comunicare così in modo più sicuro con le varie applicazioni Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Una volta connessi, è possibile utilizzare noStrudel per condividere le note tramite Nostr. Interface vi dà accesso a :





- Cruscotto Nostr completo con cronologia delle note, notifiche, messaggistica, ricerca dei profili
- Gestione dei relè e stato delle connessioni
- Strumenti avanzati per l'esame degli eventi e del loro contenuto JSON
- Opzioni di configurazione per i filtri e i PIN della linea temporale



**Suggerimento:** Su _noStrudel_, è possibile impostare _filtri temporali_ o testare diverse _NIP (Nostr Implementation Possibilities)_. Ad esempio, verificare il supporto del NIP-05 (identificatori decentralizzati) o di caratteristiche più recenti. Questo rende _noStrudel_ uno strumento eccellente per sperimentare in un ambiente controllato.



### Snort - Cliente moderno di Nostr su Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** è un altro client web di Nostr disponibile su Umbrel, che offre un **Interface** moderno, veloce e ordinato per interagire con il social network decentralizzato. A differenza di noStrudel, che si rivolge ai power user, _Snort_ punta alla semplicità d'uso senza sacrificare le funzionalità. È costruito in React e offre un'interfaccia utente ordinata che ricorda i classici social network, rendendolo adatto all'uso quotidiano.



**Installazione:** Installate _Snort_ dall'App Store di Umbrel (categoria _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Quando si apre Snort, nell'angolo in basso a sinistra si trova il pulsante "Registrati".



![Options de connexion dans Snort](assets/fr/10.webp)



Si può scegliere di registrarsi o di collegarsi a un account esistente (che è quello che faremo per questa esercitazione).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort offre diversi metodi di connessione. È possibile utilizzare l'estensione Nostr Connect precedentemente installata o altri metodi disponibili. Una volta connessi, sarete in grado di utilizzare appieno l'applicazione.



Il Interface di _Snort_ offre :





- Un display **Posts/Conversations/Global** per navigare tra le note, le discussioni o il feed globale
- Schede per **Notifiche**, **Messaggi** (DM), **Ricerca**, **Profilo**, ecc.
- Un pulsante **+** o _Scrivi_ per pubblicare una nuova nota
- Gestione di **abbonamenti (following)** e **liste**
- Menu di gestione dei relè per aggiungere/rimuovere i relè e monitorare la loro disponibilità



**Per aggiungere il proprio relè Umbrel, andare in Impostazioni - Relè. Inserire l'URL del proprio relè (`ws://umbrel:4848` o un altro URL a seconda della configurazione) nell'elenco dei relè di Snort. In questo modo, Snort pubblicherà le note sul proprio relè privato, oltre a quelle pubbliche.**



### Nostr Wallet Connect - Collegamento del Lightning Wallet a Nostr



**Nostr Wallet Connect (NWC)** è un'applicazione che **collega il vostro nodo Umbrel (Lightning)** alle applicazioni Nostr compatibili per effettuare pagamenti Lightning (ad esempio, l'invio di _zaps_, quei micro-pagamenti per il "gradimento" dei contenuti). In questo tutorial, vedremo come collegare noStrudel al vostro nodo Lightning per effettuare pagamenti direttamente dal Interface.



**Installazione e configurazione:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installare _Nostr Wallet Connect_ dal negozio Alby su Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



In noStrudel, fare clic sul proprio profilo nell'angolo in alto a destra, quindi sul pulsante "Gestisci".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Fare clic su "Fulmine" e poi su "Connetti Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Tra le opzioni di connessione disponibili, scegliere "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Fare clic su "Connect" per essere automaticamente reindirizzati alla propria sessione Umbrel Nostr Wallet Connect.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Nella pagina Nostr Wallet Connect è possibile :




   - Definite il vostro budget massimo
   - Convalidare le autorizzazioni
   - Impostare un tempo di scadenza per la connessione


Fare clic su "Connetti" per finalizzare.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Si viene reindirizzati a noStrudel con un messaggio di conferma: ora si può fare zapping in tutto il mondo dal proprio nodo Wallet/LND!



Grazie a NWC, i vostri **pagamenti Lightning tramite Nostr** (zap ai post di ricompensa, pagamenti _Value for Value_, ecc.) partono dal **vostro nodo**. Non è più necessario instradare le transazioni attraverso servizi esterni o scansionare ogni volta un QR dal telefono. L'esperienza dell'utente è notevolmente migliorata, pur rimanendo _non custodiale_ e rispettosa della privacy.



Se volete sapere come configurare il vostro nodo Lightning su Umbrel, vi consiglio di consultare quest'altra guida completa:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Configurazione e sicurezza avanzate



L'uso congiunto di Umbrel e Nostr a livello avanzato richiede un'attenzione particolare alla **sicurezza** e alla **connettività**. Ecco alcuni consigli su come proteggere la configurazione e accedervi in modo ottimale, ovunque vi troviate.



### Accesso esterno sicuro: Tor e Tailscale



Per motivi di sicurezza, il vostro Umbrel è accessibile di default solo sulla vostra rete locale (e tramite Tor). Per interagire con Nostr fuori casa, avete due soluzioni preferite: **Tor** (accesso anonimo tramite rete a cipolla) e **Tailscale** (rete VPN privata).





- **Accesso via Tor:** Umbrel configura automaticamente un **servizio Tor (.onion)** per il suo Interface web e le sue applicazioni. Ciò significa che è possibile accedere a Interface Umbrel (compresi *noStrudel* o *Snort*) da qualsiasi luogo, utilizzando il browser Tor, senza esporre il proprio IP pubblico. tor viene utilizzato per accedere ai servizi Umbrel dall'esterno della rete locale, senza esporre il dispositivo a Internet ([Configurazione di Tor sul sistema - Guide - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%2F%2Fwww)). Per utilizzare questa opzione, accedere alle impostazioni di Umbrel e recuperare l'URL .onion di Umbrel (o scansionare il codice QR fornito). Con un browser Tor, accedere a questo .onion Address: si otterrà lo stesso Interface che si trova in locale. È quindi possibile utilizzare le applicazioni Nostr come a casa.


**Se volete che il vostro relay Nostr sia raggiungibile via Tor dai vostri clienti (o amici autorizzati), è possibile. Umbrel non fornisce direttamente il .onion Address del relè, ma poiché funziona sulla porta 4848, è possibile utilizzare il:**





    - Utilizzare il .onion Address di UI Umbrel e configurare il client in modo che si connetta tramite questo Interface (poco pratico per WebSocket),





- Oppure esporre la porta 4848 come servizio onion separato. Questo richiede di armeggiare con la configurazione di Tor su Umbrel (riservato agli utenti avanzati che hanno dimestichezza con SSH). In alternativa, si può considerare un **tunnel Tor** su un altro server che reindirizzi a Umbrel: tuttavia, per uso personale, è più facile usare Tailscale.





- Accesso tramite Tailscale: [Tailscale](https://tailscale.com/) è una soluzione VPN mesh che crea una rete privata virtuale tra i vostri dispositivi e Umbrel. Il vantaggio: funziona come se foste in una LAN, ma su Internet, in modo criptato e senza complesse configurazioni. **Tailscale assegna a Umbrel un IP fisso e un nome di dominio privato, indipendentemente dalla sua posizione in rete** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). In pratica, una volta installato Tailscale su Umbrel (dall'App Store di Umbrel, categoria *Networking*) **e** sui vostri dispositivi (cellulari, PC...), potrete raggiungere Umbrel tramite un Address come `100.x.y.z` (IP di Tailscale) o un nome come `umbrel.tailnet123.ts.net`.


per Nostr_, Tailscale è estremamente utile: il vostro cellulare, se ha Tailscale attivo, sarà in grado di connettersi a `ws://umbrel:4848` (grazie a MagicDNS) o direttamente all'IP di Tailscale e alla porta 4848 per utilizzare il relay. Client come Damus o Amethyst vedranno il vostro Umbrel come se fosse sulla stessa rete locale. **Suggerimento:** Abilitare l'opzione **MagicDNS** in Tailscale per utilizzare il nome host `umbrel` invece di memorizzare l'IP. Questo assicura una connessione fluida al vostro relè anche quando siete in viaggio ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Inoltre, Tailscale consente di accedere a Interface Umbrel (e quindi ai client web _noStrudel/Snort_) tramite un semplice browser, utilizzando l'IP privato o il nome di dominio assegnato. Non è necessario un browser Tor e la velocità di trasferimento dei dati è generalmente migliore rispetto alla rete Tor.




**Nota: Tor e Tailscale non si escludono a vicenda. È possibile mantenere Tor attivo per l'accesso anonimo o per servizi specifici e utilizzare Tailscale su base quotidiana per la sua semplicità. In entrambi i casi, non è necessario aprire una porta sul router, il che rafforza la sicurezza.**



### Protezione del relè Nostr (pratiche consigliate)



Se ospitate un relè Nostr su Umbrel, soprattutto in un contesto avanzato, assicuratevi di applicare alcune buone pratiche:





- **Relè privato o limitato:** Per impostazione predefinita, il vostro relè Umbrel è privato (non annunciato pubblicamente) e, se vi accedete solo tramite Tailscale o la vostra LAN, rimarrà inaccessibile agli estranei. **Mantenete il link riservato** - Non diffondetelo su reti pubbliche Nostr a meno che non vogliate ospitare volontariamente altri utenti, il che è tutto un altro problema (moderazione, larghezza di banda, ecc.). Per l'uso personale, si consiglia di limitare l'accesso a se stessi e, se necessario, a pochi amici e familiari fidati.





- **Whitelist / Auth**: L'implementazione di nostr-rs-relay supporta un meccanismo di autenticazione **NIP-42** e una *whitelist* di chiavi pubbliche. Abilitando queste opzioni, si può limitare il proprio relay in modo che **accetti solo eventi firmati da certe chiavi (le proprie)**, o che i client debbano autenticarsi per pubblicare. Per impostare questo richiede la modifica del file di configurazione `config.toml` del relay in Umbrel (tramite SSH nel contenitore Docker). *È una manipolazione avanzata, ma per esempio si possono elencare gli annunci consentiti* (`pubkey_whitelist`). In questo modo, anche se qualcuno scopre il vostro relay, non sarà in grado di pubblicarvi nulla se non è presente nell'elenco.





- **Aggiornamenti e manutenzione:** Mantenete il vostro Umbrel e l'applicazione *Nostr Relay* aggiornati. Gli aggiornamenti possono includere miglioramenti delle prestazioni (ad esempio, una migliore gestione dello spam) e correzioni di sicurezza. Su Umbrel, controllare regolarmente l'App Store per gli aggiornamenti di *Nostr Relay* e applicarli se necessario.





- **Monitoraggio e limiti:** Tenete d'occhio l'utilizzo del vostro relè. Se lo si apre ad altri, è bene tenere d'occhio il carico (CPU/RAM) del proprio Umbrel, poiché un relay può accumulare rapidamente molti dati. nostr-rs-relay offre dei **limiti di velocità e di memoria** configurabili (`limiti' nella configurazione, ad esempio numero di eventi al secondo, dimensione massima dell'evento, eliminazione dei vecchi eventi...). Per l'uso privato, probabilmente non sarà necessario toccarli, ma è bene sapere che questi parametri esistono se ne avete bisogno ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Proteggere le chiavi Nostr:** Questo punto è già stato menzionato, ma è fondamentale: non inserite mai le vostre chiavi private Nostr in un Interface di cui non vi fidate pienamente. Utilizzate invece estensioni del browser o dispositivi esterni (come gli _signer_ Nostr su telefoni separati) per firmare le azioni sensibili. Su Umbrel, i vostri client web come _Snort_ e _noStrudel_ possono funzionare senza conoscere la vostra chiave segreta, tramite il NIP-07. Approfittate di questa opportunità per combinare comodità e sicurezza.




Seguendo questi suggerimenti, l'integrazione di un nodo Umbrel con Nostr sarà potente **e** sicura. Avrete un ambiente completo: un nodo Bitcoin per i pagamenti Lightning, un relay Nostr privato per la sovranità dei dati e client web Nostr ad alte prestazioni per navigare in questo nuovo social network decentralizzato. Divertitevi a esplorare Nostr con Umbrel!