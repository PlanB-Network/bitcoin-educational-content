---
name: Ombrello LND
description: Esercitazione avanzata sull'installazione e la configurazione di Lightning Network Daemon (LND) su Umbrel
---
![cover](assets/cover.webp)




## Introduzione



Questo tutorial avanzato vi porta passo dopo passo all'installazione, alla configurazione e all'utilizzo dell'applicazione Lightning Node (LND) sul vostro nodo Umbrel. Imparerete ad aprire canali, a gestire la liquidità e a sincronizzare il vostro nodo con un'applicazione mobile.



## 1. Prerequisito: nodo funzionale Bitcoin Umbrel



Prima di distribuire Lightning, è necessario avere un nodo Bitcoin pienamente operativo su Umbrel. Ciò comporta l'installazione di Umbrel (su Raspberry Pi, NAS o altra macchina) e la sincronizzazione completa del Blockchain Bitcoin.



Per installare Umbrel e configurare il nodo Bitcoin, si consiglia di seguire il nostro tutorial dedicato:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Assicurarsi che il nodo Bitcoin sia aggiornato e funzioni correttamente, in quanto il Lightning Network si basa su di esso per tutte le transazioni off-chain.



## 2. Introduzione al Lightning Network



Il Lightning Network è un protocollo di secondo Layer progettato per accelerare e ridurre il costo delle transazioni Bitcoin eseguendole al di fuori del Blockchain principale.



In concreto, Lightning utilizza una rete di canali di pagamento tra nodi: due utenti aprono un canale bloccando On-Chain BTC (transazione iniziale), quindi possono effettuare istantaneamente pagamenti Exchange all'interno di questo canale. Queste transazioni off-chain non vengono registrate sul Blockchain, da qui la loro velocità e il costo praticamente nullo.



I pagamenti possono essere instradati attraverso più canali (grazie ai nodi intermediari) per raggiungere qualsiasi destinatario della rete, consentendo una scala quasi illimitata di transazioni istantanee. Lightning offre quindi transazioni molto veloci e a basso costo, ideali per i pagamenti di tutti i giorni o per le micro-transazioni, alleggerendo al contempo il carico del Blockchain Bitcoin.



Per funzionare, un nodo Lightning deve essere permanentemente collegato alla rete e interagire con altri nodi Lightning. Esistono diverse implementazioni software (LND, Core Lightning, Eclair, ecc.), tutte compatibili tra loro. Umbrel utilizza LND (Lightning Network Daemon) come parte della sua applicazione ufficiale Lightning Node. Questo tutorial si concentra su LND.



Per un'introduzione teorica completa al Lightning Network, vi consigliamo di seguire il nostro corso dedicato:



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Questo corso vi fornirà una base approfondita dei concetti fondamentali del Lightning Network, prima di passare alla pratica con il nodo LND.



## 3. Perché auto-ospitare LND?



Gestire il proprio nodo Lightning (LND) su Umbrel vi dà la totale sovranità sui vostri fondi e canali, rispetto alle soluzioni di custodia o semi-deposito.



### Confronto tra le soluzioni Lightning :



**Soluzioni custodiali (es.: Wallet di Satoshi)** :




- I vostri bitcoin Lightning sono gestiti da una terza parte fidata
- Facile da usare, nessuna complessità tecnica
- L'operatore detiene i vostri fondi e può tracciare le vostre transazioni
- Si sacrificano il controllo e la riservatezza



**Portafogli di consumo non di materie prime (ad es. Phoenix, Breez)** :




- Gli utenti conservano le loro chiavi private e quindi il Ownership dei loro BTC
- Nessuna gestione completa dei nodi - l'applicazione gestisce i canali in background
- Compromesso tra semplicità e sovranità
- Dipendenza dall'infrastruttura dei fornitori per la liquidità
- Limitazioni tecniche (uno smartphone non può instradare i pagamenti per gli altri)



**Nodo LND auto-ospitato (Umbrel)** :




- Massima sovranità: i vostri BTC On-Chain e off-chain sono interamente sotto il vostro controllo
- Non ci sono terze parti coinvolte nell'apertura dei canali o nella gestione dei vostri pagamenti
- Maggiore riservatezza (i vostri canali e le vostre transazioni sono noti solo a voi e ai vostri diretti interlocutori)
- Libertà di utilizzo: connessione ai propri servizi e portafogli
- Possibilità di instradare le transazioni per conto di altri (microcompensazione)
- Maggiori responsabilità tecniche (manutenzione, gestione della liquidità, backup)



In breve, il self-hosting di LND offre il massimo controllo, ma richiede maggiori competenze tecniche. È un compromesso tra convenienza e sovranità.



## 4. Tutorial passo dopo passo



### 4.1 Installazione e configurazione dell'applicazione Lightning Node su Umbrel



Una volta sincronizzato il nodo Umbrel (Bitcoin), procedere come segue:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installare l'applicazione Lightning Node dalla sezione "App Store" di Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) verrà distribuito sul vostro Umbrel come applicazione. Quando la aprirete per la prima volta, vedrete un messaggio di avvertimento che vi informerà che Lightning è una tecnologia sperimentale.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



È possibile scegliere tra la creazione di un nuovo nodo o il ripristino di uno da un backup/seed. Per la prima installazione, scegliere di creare un nuovo nodo. L'applicazione Lightning Node vi generate una frase di 24 parole Mnemonic (il vostro seed Lightning): scrivetela con molta attenzione (idealmente offline, su carta), poiché verrà utilizzata per ripristinare i fondi Lightning, se necessario.



**Nota: nelle versioni recenti di Umbrel, l'installazione dell'applicazione Lightning fornisce questo seed di 24 parole (il nodo Bitcoin di Umbrel non lo fornisce).



![Interface principale de Lightning Node](assets/fr/04.webp)



Dopo l'inizializzazione, si accede alla Interface principale di Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



Nelle impostazioni dell'applicazione sono presenti diverse opzioni importanti:




   - Consultare l'ID del nodo (l'identificativo univoco del nodo)
   - Collegamento di un Wallet esterno (Collegare Wallet)
   - Visualizza le parole segrete
   - Accesso alle impostazioni avanzate
   - Recuperare i canali
   - Scarica il file di backup del canale
   - Abilita i backup automatici
   - Configurare il backup via Tor (Backup over Tor)



Queste opzioni sono essenziali per la sicurezza e la gestione del nodo Lightning. Assicuratevi di attivare i backup automatici e di tenere al sicuro le vostre parole segrete.



**Risorse utili:**




- [Umbrel Community](https://community.umbrel.com) - Forum di discussione per gli utenti per condividere problemi e soluzioni riguardanti Umbrel e il suo ecosistema


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Descrizione delle funzionalità dell'app Lightning Node su Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Documentazione ufficiale LND

### 4.2 Apertura di un canale Lightning



Una volta che LND è attivo e funzionante, è possibile aprire il primo canale Lightning. Per trovare nodi di qualità a cui collegarsi:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) è un esploratore per trovare nodi affidabili per aprire canali.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Ad esempio, il [nodo ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) è un nodo riconosciuto con eccellenti statistiche di disponibilità e liquidità.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Per questa esercitazione, apriremo un canale con [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Le informazioni necessarie per la connessione (pubkey@ip:port) sono riportate sulla loro pagina Amboss.



Per aprire il canale :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Nella pagina iniziale di Lightning Node, fate clic sul pulsante "+ APRI CANALE"



![Configuration du canal](assets/fr/10.webp)



Nella pagina di configurazione del canale :




   - Incollare l'ID del nodo copiato da Amboss (formato: pubkey@ip:port)
   - Definire la quantità di capacità del canale (alcuni nodi, come ACINQ, hanno dei minimi, ad esempio 400k Sats)
   - Adattare le commissioni di apertura delle transazioni, se necessario



![Canal en cours d'ouverture](assets/fr/11.webp)



Una volta inviata la transazione, il canale apparirà come "in apertura" sulla home page. Attendere la conferma della transazione On-Chain.



![Détails du canal](assets/fr/12.webp)



Fare clic sul canale per visualizzarne i dettagli:




   - Stato attuale
   - Capacità totale
   - Ripartizione della liquidità (in entrata e in uscita)
   - Chiave pubblica del nodo remoto
   - E altre informazioni tecniche



### Utilizzo del Lightning Network+ per ottenere liquidità in entrata



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ è disponibile nell'App Store di Umbrel per facilitare l'ottenimento di denaro in entrata.



![Interface principale de LN+](assets/fr/14.webp)



Il Interface principale offre tre importanti opzioni:




- "Swap di liquidità: esplorate le offerte di swap disponibili"
- "Open For Me": filtrare gli swap per i quali si è eleggibili
- "To Docs": accesso alla documentazione



![Message d'erreur LN+](assets/fr/15.webp)



Nota: se non avete ancora un canale aperto, vedrete questo messaggio di errore quando cliccate su "Apri per me".



![Liste des swaps disponibles](assets/fr/16.webp)



La pagina "Liquidity Swaps" mostra tutte le offerte di swap disponibili sulla rete.



![Swaps éligibles](assets/fr/17.webp)



l'opzione "Apri per me" filtra solo gli scambi per i quali il nodo soddisfa le condizioni richieste.



![Détails d'un swap](assets/fr/18.webp)



Esempio di dettagli di swap :




- Configurazione del pentagono (5 partecipanti)
- Capacità di 300k Sats per canale
- Prerequisito: almeno 10 canali aperti con capacità totale di 1M Sats
- Posti disponibili: 4/5



### 4.3 Sincronizzazione con un'applicazione mobile (Zeus)



Per controllare il nodo Lightning da remoto (smartphone), è possibile utilizzare Zeus (applicazione open-source disponibile su iOS/Android).



**Configurazione di Zeus con Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Assicuratevi che il vostro nodo Umbrel sia accessibile (per impostazione predefinita tramite Tor).


Nell'Umbrel Interface, aprire l'applicazione Lightning Node, quindi fare clic sul pulsante "Connect Wallet" (Connetti Wallet), come indicato dalla freccia.



![Page de connexion avec QR code](assets/fr/20.webp)



Viene visualizzato un codice QR contenente i dati di accesso al LND in formato lndconnect. Questo codice QR è particolarmente denso di informazioni, quindi non esitate a ingrandirlo per facilitare la lettura.



![Configuration initiale de Zeus](assets/fr/21.webp)



Sul telefono :




   - Aprire Zeus
   - Nella pagina iniziale, fare clic su "Configurazione avanzata" per collegare il proprio nodo Lightning
   - Nei parametri, selezionare "Creare o collegare un Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



In Zeus:




   - Scegliere "LND (REST)" come tipo di connessione
   - È possibile scansionare il codice QR (metodo consigliato) o inserire le informazioni manualmente. (Non esitate a ingrandire il codice QR dell'Ombrello, perché è molto denso)
   - Importante: attivare l'opzione "Usa Tor" se il vostro Umbrel è accessibile solo tramite Tor (l'opzione predefinita)
   - Salvare la configurazione



Il vostro Zeus è ora collegato al vostro nodo Umbrel e vi permette di effettuare pagamenti Lightning, di visualizzare i vostri canali, i saldi, ecc.



**Opzioni di connessione avanzate



Per impostazione predefinita, la connessione di Zeus ↔ Umbrel avviene tramite Tor. Per una connessione più veloce, esistono due alternative:



**Lightning Node Connect (LNC)** :




   - Meccanismo di connessione criptata di Lightning Labs
   - Installare l'applicazione Lightning Terminal su Umbrel (include l'accesso a LNC)
   - generate un codice QR di connessione in Lightning Terminal (Connect → Connect Zeus via LNC)
   - Eseguire la scansione in Zeus (scegliere "LNC" come tipo di connessione)



**VPN Tailscale**:




   - VPN mesh facile da configurare
   - Installare Tailscale su Umbrel (App Store) e sul cellulare
   - Connettere Zeus tramite l'IP privato di Tailscale invece di Tor Address



Queste opzioni non sono obbligatorie e la soluzione Tor + Zeus funziona bene nella maggior parte dei casi.



> **Risorse utili:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Guida ufficiale alla connessione di Zeus a Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Progetto open source Zeus
> - [Umbrel Community - Connettere Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guida alla connessione di Zeus a Umbrel utilizzando Tailscale

## 5. Sicurezza e buone pratiche



La gestione di un nodo Lightning self-hosted richiede una particolare attenzione alla sicurezza.



### Backup e sicurezza per il vostro nodo



**Tipi essenziali di backup**



Il nodo Lightning Umbrel richiede due tipi di backup:



**La frase seed (24 parole)**




- Recupera i fondi On-Chain
- Necessario per ricreare il fulmine Wallet
- Per un'archiviazione ultra-sicura (offline, su carta)



*file *Canale statico di backup (SCB)**




- Contiene informazioni sul canale Lightning
- Consente la chiusura forzata del canale in caso di arresto anomalo
- Importante: ** Non salvare mai il file `channel.db` manualmente (rischio di sanzioni)



**Procedura di backup manuale



Per salvare i canali manualmente :


1. Accedere al menu del nodo Lightning (tre puntini "⋮" accanto a "+ Aprire canale")


2. Scaricare il file di backup del canale


3. Esportazione di un nuovo SCB dopo ogni modifica del canale


4. Conservare l'SCB in modo sicuro (supporti criptati, copia fuori sede)



*sistema di backup automatico *Umbrel**



Umbrel è dotato di un sofisticato sistema di backup automatico che assicura :



*Protezione dei dati:*




- Crittografia lato client prima della trasmissione
- Invio tramite la rete Tor
- Dati integrati da riempimento casuale
- Chiave di crittografia unica per il dispositivo



*Sicurezza migliorata:*




- Backup istantaneo in caso di cambiamenti di stato
- Backup "esca" a intervalli casuali
- Nascondere le modifiche alle dimensioni del backup
- Protezione dall'analisi del tempo



*Processo di restauro:*




- Identificatore e chiave derivati dal vostro ombrello seed
- Il restauro completo è possibile solo con la frase Mnemonic
- Ripristino automatico degli ultimi backup
- Ripristino delle impostazioni e dei dati del canale



### Ripristino degli incidenti



Se il nodo viene perso (guasto hardware, scheda SD danneggiata) :




- Reinstallare l'ombrello
- Inserite il vostro seed di 24 parole nell'applicazione Lightning
- Importare il file SCB durante il ripristino



LND contatterà ogni partner dei vostri vecchi canali per chiuderli e recuperare la vostra quota di fondi On-Chain. I canali saranno chiusi in modo permanente (per essere riaperti se necessario).



### Disponibilità e protezione dalle frodi



L'ideale sarebbe lasciare il proprio nodo online il più spesso possibile. In caso di assenza prolungata:




- Un peer malintenzionato potrebbe tentare di trasmettere uno stato del canale vecchio
- Il fulmine prevede un "periodo di protesta" (circa 2 settimane per il LND)
- Se vi assentate per un lungo periodo, installate un Watchtower



**Configurazione Watchtower:**




- Nelle impostazioni avanzate del LND, aggiungere l'URL di un server Watchtower affidabile
- È possibile utilizzare un servizio pubblico o installare il proprio Watchtower




Per saperne di più sulla configurazione e sull'uso delle torri di guardia, vi consigliamo di consultare il nostro tutorial dedicato:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Altre migliori pratiche





- Aggiornamenti software:** Mantenere Umbrel e LND aggiornati (correzioni di sicurezza)
- Protezione hardware:** Utilizzare un sistema stabile (Raspberry Pi con SSD, mini-PC) e un gruppo di continuità
- Sicurezza di rete:** Mantenere la configurazione predefinita di Tor, cambiare la password di amministrazione di Umbrel (predefinita: "moneyprintergobrrr")
- Crittografia:** Abilitare la crittografia del disco, se possibile



## 6. Strumenti aggiuntivi



L'applicazione Lightning Node di Umbrel fornisce gli elementi essenziali per la gestione dei canali, ma gli strumenti di terze parti offrono funzionalità avanzate.



### ThunderHub



Interface moderno sistema di gestione dei nodi Lightning basato sul web, installabile tramite l'App Store di Umbrel.



**Caratteristiche:**




- Visualizzazione in tempo reale dei canali (capacità, bilanci)
- Strumenti di ribilanciamento integrati
- Supporto per la fatturazione multipercorso (MPP)
- Generazione del codice QR LNURL
- Gestione delle transazioni On-Chain



ThunderHub è ideale per monitorare un nodo di routing attivo ed eseguire un semplice ribilanciamento.



### Cavalcare il fulmine (RTL)



Interface è compatibile con diverse implementazioni di Lightning (LND, Core Lightning, Eclair).



**Salute: **




- Gestione multi-nodo
- Cruscotti sensibili al contesto
- Supporto per lo scambio di sottomarini (Lightning Loop)
- autenticazione a 2 fattori
- Backup dei canali di esportazione/importazione



RTL è un "coltellino svizzero" completo per amministrare un nodo Lightning con un approccio più orientato agli esperti.



### Altri strumenti utili





- Lightning Shell** : Linea di comando (lncli) via browser
- BTC RPC Explorer e Mempool** : Monitoraggio Blockchain
- LNmetrics e Torq**: Analisi delle prestazioni di routing
- Amboss & 1ML**: gestione "sociale" del proprio nodo (alias, contatti, analisi della rete)



Questi strumenti possono essere installati in pochi clic tramite l'App Store di Umbrel, senza alcuna configurazione complessa.



**Risorse aggiuntive per gli strumenti:**




- [ThunderHub.io - Caratteristiche](https://thunderhub.io) - Panoramica delle caratteristiche di ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - Documentazione RTL
- [David Kaspar - Riequilibrio via ThunderHub](https://blog.davidkaspar.com) - Una guida pratica al riequilibrio
- [Guida "Gestione dei nodi Lightning"](https://github.com/openoms/lightning-node-management) - Documentazione avanzata per i power-user



## Conclusione



Gestire il proprio nodo LND su Umbrel è un passo importante verso la sovranità finanziaria. Sebbene richieda un maggiore coinvolgimento tecnico rispetto a una soluzione di custodia, i vantaggi in termini di controllo, riservatezza e partecipazione attiva al Lightning Network sono notevoli.



Seguendo questa guida, dovreste essere in grado di installare LND, aprire canali, gestire la liquidità e accedere al vostro nodo da remoto. Sentitevi liberi di esplorare gradualmente le funzioni avanzate e gli strumenti aggiuntivi man mano che acquisite familiarità con l'ecosistema.



Ricordate che la sicurezza dei vostri fondi dipende dalle vostre misure di sicurezza e dalle vostre pratiche. Prendetevi il tempo necessario per comprendere ogni aspetto prima di impegnare somme ingenti.