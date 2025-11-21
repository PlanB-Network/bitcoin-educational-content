---
name: Zeus Embedded - Avanzato
description: Portafoglio Lightning auto-custodiale multi-nodo
---

![Zeus](assets/cover.webp)


## Introduzione a ZEUS Wallet


ZEUS è un'applicazione mobile per la gestione di Bitcoin Wallet e nodi con tutte le funzionalità di un Bitcoin lightning Wallet che rende semplici i pagamenti Bitcoin, offre agli utenti il controllo completo delle proprie finanze e consente agli utenti più esperti di gestire i propri nodi Lightning dal palmo della mano.


### Per chi è ZEUS?

Attualmente ZEUS è per persone che gestiscono i propri nodi domestici / aziendali [Lightning Network Daemon (LND)](https://lightning.engineering/) o [Core Lightning (CLN)](https://blockstream.com/lightning/) e li amministrano da remoto tramite Zeus.


I commercianti che utilizzano [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) o [Alby](https://getalby.com/) (o qualsiasi altro account LNDhub) possono anche collegarsi, utilizzare e gestire i propri nodi / account da ZEUS.


[A partire dalla versione v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS inizierà a rivolgersi agli utenti medi che desiderano semplicemente un modo facile per effettuare pagamenti bitcoin veloci ed economici dal proprio dispositivo mobile, grazie a un [nodo Lightning mobile integrato](https://docs.zeusln.app/category/embedded-node) con un [Fornitore di Servizi Lightning (LSP)](https://docs.zeusln.app/lsp/intro) incorporato.


### Risorse importanti di Zeus:


- Pagina web ufficiale di Zeus - [https://zeusln.app/](https://zeusln.app/)
- Documentazione Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repository Github di Zeus](https://github.com/ZeusLN/zeus)
- [Gruppo di supporto Telegram di Zeus](https://t.me/ZeusLN)
- [Zeus su NOSTR](https://iris.to/zeus@zeusln.app)
- [Annunci del blog di Zeus](https://blog.zeusln.com)


### Caratteristiche di Zeus

#### Caratteristiche generali:


- Autotutela, solo Bitcoin e Lightning Wallet
- Nessuna commissione di elaborazione, nessun KYC
- Completamente open source (APGLv3)
- Supporto di più nodi/account (è possibile gestire i propri nodi domestici, eseguire nodi LND integrati, connettersi a più account LNDhub)
- Menu attività facile da usare
- Crittografia PIN o passphrase, modalità Privacy - per nascondere i dati sensibili
- Libro dei contatti, multi tema, multi lingua


#### Caratteristiche tecniche


- Connettersi tramite Tor
- Supporto completo LNURL (pagamento, prelievo, autorizzazione, canale), invio a indirizzi Lightning
- Gestione dettagliata dei canali di illuminazione, supporto MPP/AMP, Keysend, gestione delle tariffe di routing
- Supporto Replace-by-fee (RBF) e Child-pays-for-parent (CPFP)
- Pagamenti e richieste NFC, firma e verifica dei messaggi
- Supporto SegWit e Taproot
- Canali semplici Taproot
- Indirizzi fulminei di autocustodia (@zeuspay.com)
- Punto vendita di Square (presto aperto PoS)


### Guide e video tutorial

Per poter utilizzare Zeus e gestire i canali Lightning, la liquidità, le commissioni, ecc. è meglio leggere prima alcune guide importanti su Lightning Network.


#### Guide:


- [LND - Documentazione Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Documentazione di Core Lightning](https://lightning.readthedocs.io/index.html)
- [Guida a Lightning per principianti](https://bitcoiner.guide/lightning/) – di Bitcoin Q&A
- [Gestione del nodo Lightning](https://www.lightningnode.info/) – di openoms
- [Il Lightning Network e l’analogia con l’aeroporto](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Gestione della liquidità del nodo Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Manutenzione del nodo Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video tutorial di BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Una guida dettagliata su come iniziare a utilizzare il nodo incorporato Zeus LN sul proprio dispositivo mobile


![Image](assets/en/01.webp)


Dedico questa guida a tutti i nuovi utenti del Lightning Network (LN) che vogliono iniziare un nuovo viaggio sovrano utilizzando un nodo di autocustodia Wallet sui loro dispositivi mobili.


Consideriamo che si è già passati attraverso tutta quella pletora di portafogli LN custodiali, ma non si è ancora pronti per iniziare a gestire un nodo LN di routing PUBBLICO, si vuole solo impilare più Sats su LN in un modo più auto-custodiale e fare i pagamenti regolari su LN.


Ecco Zeus, a partire dalla [versione v0.8.0 annunciata sul loro blog](https://blog.zeusln.com/new-release-zeus-v0-8-0/), che ora offre un nodo LND integrato nell’app. Fino ad ora Zeus era un’app di gestione di nodi remoti + account LNDhub. Ma ora… il nodo è nel telefono!


![Image](assets/en/02.webp)


### Riepilogo rapido delle caratteristiche principali di Zeus Node:



- **Nodo LND privato** - Significa che questo nodo NON effettua l'instradamento pubblico di altri pagamenti attraverso il proprio nodo. Il nodo e i canali non sono annunciati (privati, non visibili sul grafico pubblico del LN). La ricezione e l'esecuzione dei pagamenti avverrà attraverso i peer LSP collegati. RICORDA: Zeus Embedded Node NON effettua il routing pubblico!
- **Servizio LND persistente** - l'utente può attivare questa funzione e mantenere il servizio LND attivo in modo continuativo come un qualsiasi nodo LN regolare. Non è necessario che l'applicazione sia aperta, il servizio persistente manterrà tutte le comunicazioni online.
-   **Filtri di blocco Neutrino** - la sincronizzazione dei blocchi viene eseguita utilizzando [i filtri di blocco e il protocollo Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (senza fornire alcuna informazione sui fondi on-chain dei nostri utenti). Promemoria: per connessioni Internet ad alta latenza / lente questa sincronizzazione dei blocchi basata su Neutrino può talvolta fallire. Provare a passare a un server Neutrino vicino potrebbe aiutare a ripristinare la sincronizzazione. Senza questa sincronizzazione il tuo nodo LND non può avviarsi!
- **Canali Taproot semplici** - Quando si chiudono questi canali, gli utenti incorrono in minori spese e godono di una maggiore privacy, in quanto appaiono come qualsiasi altra spesa Taproot quando si esamina la loro impronta On-Chain.
- **LSP integrato** - Olympus è il nuovo nodo LSP per Zeus. Gli utenti possono ricevere subito il Sats sul LN, senza dover configurare in precedenza i canali LN. Basta creare un LN Invoice e pagare da qualsiasi altro LN Wallet, con Zeus 0-conf. Sarà sufficiente creare un LN Invoice e pagare da qualsiasi altro LN Wallet, con il servizio di canale Zeus 0-conf. Per saperne di più su Zeus LSP, cliccate qui. L'LSP offre anche una maggiore privacy ai nostri utenti, fornendo loro fatture avvolte che nascondono le chiavi pubbliche dei loro nodi ai pagatori.
- **Rubrica** - è possibile salvare manualmente i contatti o importarli da NOSTR, per inviare facilmente i pagamenti alle destinazioni abituali.
- Pieno supporto per LNURL, LN Address invio e ricezione - ora è possibile impostare il proprio LN Address auto-custodiale con @zeuspay.com. Ricordate: È possibile utilizzare Zeus per l'autenticazione LN anche sui siti in cui è possibile effettuare il login con l'autenticazione LN. È molto utile.
- **Punto vendita** - Ora gli utenti commercianti possono impostare i propri articoli e vendere direttamente da Zeus, con PoS integrato. Per il momento contiene le esigenze di base, ma in futuro conterrà funzionalità più estese.
- **LND logs** - l'utente può leggere in tempo reale i log del servizio LND e utilizzarli per il debug di eventuali problemi (soprattutto per le connessioni non corrette)
- **Backup automatico** - i canali del nodo LN vengono automaticamente salvati sul server Olympus. Questo backup automatico è criptato con il nodo Wallet seed (senza il seed è totalmente inutile). L'utente può anche esportare manualmente un SCB (backup statico dei canali) per un ripristino di emergenza.


### Come salire a bordo di Zeus LN Node (LND embedded)


In questa guida parlerò solo del nodo LND integrato e non degli altri modi di utilizzare questa magnifica app (gestione dei nodi remoti e account LNDhub). Per gli altri tipi di connessioni, fare riferimento alla [pagina della documentazione di Zeus](https://docs.zeusln.app/category/getting-started), che è spiegata molto bene e non necessita di una guida dedicata.


#### FASE 1 - CONFIGURAZIONE INIZIALE


Dato che Zeus è un nodo LND completo, avrò alcune raccomandazioni iniziali:



- Non utilizzate un dispositivo vecchio, che potrebbe compromettere l'utilizzo di questa potente applicazione. Soprattutto nel periodo di sincronizzazione, l'app potrebbe utilizzare intensamente la CPU e la RAM. La mancanza di queste ultime potrebbe addirittura rendere impossibile l'utilizzo dell'app Zeus.
- Utilizzate almeno Android 11 come sistema operativo mobile e aggiornatelo il più possibile. Per iOS lo stesso, cercate di usare una versione molto più alta del sistema operativo.
- È necessario almeno 1 GB di spazio su disco per l'archiviazione dei dati. Nel tempo potrebbe crescere di più, ma esiste una funzionalità per compattare il database a un livello di MB.
- Non è necessario utilizzare Zeus con il servizio Tor o Orbot. Non complicate le cose più del necessario. Tor in questo caso non vi offrirà più privacy ma peggiorerà solo le cose per la sincronizzazione iniziale. Fate anche attenzione alle VPN che utilizzate e verificate la latenza della connessione verso i server di Neutrino. Tenete presente che il filtro di blocco Neutrino non fa trapelare o traccia l'identità del vostro dispositivo, ma si limita a servire i blocchi. Il traffico del LN è anche dietro un LSP con canali privati, quindi le informazioni che escono sono pochissime, non c'è motivo di preoccuparsi della privacy.
-   Abbiate pazienza per la sincronizzazione iniziale, potrebbe richiedere diversi minuti. Cercate di essere collegati a una connessione Internet a banda larga con buona latenza. Se gestite il vostro nodo Bitcoin, [potete attivare il servizio neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) e collegare il vostro Zeus al vostro nodo, anche utilizzando la LAN interna, così avrete la massima velocità.


Una volta impostato il tipo di connessione "Nodo incorporato", l'applicazione inizierà a sincronizzarsi per un po'. Aspettate pazientemente di finire questa parte, poi entrate nella pagina principale delle impostazioni.


![Image](assets/en/03.webp)


Vediamo brevemente le sezioni delle impostazioni per capire alcune delle caratteristiche principali, prima di iniziare a usare Zeus:


**A - IMPOSTAZIONI**


Questa è una sezione con le impostazioni generali per l'intera applicazione


**1 - Lightning Service Provider (LSP)**


Qui vengono presentati due servizi LSP:



- canali just in time_ - quando non avete nessun canale aperto o liquidità in entrata disponibile, se il servizio è attivato aprirà un canale al volo per voi. Questa opzione può essere disattivata se non si desidera aprire altri canali di questo tipo.
- richiedere i canali in anticipo_ - è possibile acquistare i canali inbound dall'LSP Olympus direttamente nell'app con diverse opzioni e importi (per l'inbound e l'outbound).


L’LSP aiuta a connettere gli utenti alla rete Lightning aprendo canali di pagamento verso i loro nodi. [Leggi di più sugli LSP qui](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS ha un nuovo LSP integrato chiamato [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), disponibile per tutti gli utenti che utilizzano il nuovo nodo integrato.


In questa sezione, l'impostazione predefinita è l'LSP Olympus (https://0conf.lnolymp.us), ma presto sarà possibile impostare anche un altro LSP 0conf che supporti questo protocollo.


tenete a mente che..

quando aprite un canale con Olympus LSP utilizzando le fatture LN incartate, ottenete anche una liquidità in entrata di 100k! Si tratta di un'ottima opzione nel caso in cui abbiate bisogno di ricevere subito altre fatture Sats

esempio: si depositano 400k Sats per aprire un canale LSP, poi l'LSP apre un canale con capacità di 500k Sats verso il proprio nodo Zeus e spinge i 400k Sats depositati verso il proprio lato

liquidità in entrata" = più "spazio" nel vostro canale per ricevere


In futuro speriamo di poter avere molti altri LSP che possano essere integrati in Zeus e utilizzare alternativamente ciascuno di essi. È solo questione di tempo prima che i nuovi LSP adottino uno standard aperto per questo tipo di canali 0conf.


Se non si desidera aprire nuovi canali "al volo", si può disattivare questa opzione.


In questa stessa sezione, è possibile scegliere di "richiedere canali Taproot semplici" quando l'LSP aprirà un canale verso il vostro nodo Zeus. Questi canali semplici Taproot offrono una migliore privacy On-Chain e tariffe più basse alla chiusura del canale. Ci sono solo due motivi per non usarli:



- Sono nuovi e potrebbero esserci ancora dei bug in LND quando li si usa.
- La vostra controparte non li supporta. Per il momento, anche i nodi LND devono optare esplicitamente per il loro utilizzo.


**2 - Impostazioni di pagamento**


Questa funzione vi consentirà di impostare le vostre tariffe preferite per i pagamenti, tramite LN o onchain. Offre inoltre la possibilità di aumentare o diminuire il timeout delle fatture.


Se alcuni pagamenti del LN non vanno a buon fine, si può aumentare la tariffa per trovare un percorso migliore. Inoltre, se si tratta di tx onchain, è possibile impostare una tariffa specifica, in modo che il tx non rimanga bloccato nel Mempool per molto tempo, in caso di un periodo di tariffe elevate.


**3 - Impostazioni delle fatture**


In questa sezione sono presenti alcune opzioni per le fatture generate:



- Impostare un memo standard da visualizzare nel Invoice o nel generate
- Tempo di scadenza in secondi, nel caso in cui si desideri un tempo specifico, più o meno lungo, per il pagamento del Invoice
- Includere suggerimenti sul percorso: fornire informazioni per trovare canali non pubblicizzati o privati. Ciò consente di instradare i pagamenti verso nodi che non sono pubblicamente visibili sulla rete. Un suggerimento di percorso fornisce un percorso parziale tra il nodo privato del destinatario e un nodo pubblico. Questo suggerimento di instradamento viene poi incluso nel Invoice generato dal destinatario e fornito al pagatore. Suggerisco di abilitarlo per impostazione predefinita, altrimenti i pagamenti in arrivo potrebbero fallire (nessun percorso trovato).
- AMP Invoice - I pagamenti multipercorso atomici sono un nuovo tipo di pagamenti Lightning implementati da LND che consentono di ricevere Sats senza uno specifico Invoice, utilizzando [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). È praticamente un codice di pagamento statico. [Leggi qui](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Mostra campo preimmagine personalizzato - utilizzare questa opzione solo in casi molto specifici, quando si desidera davvero utilizzare campi personalizzati nella preimmagine. [Per saperne di più](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Un'altra opzione in questa sezione è come impostare il tipo di Address onchain che si desidera utilizzare: SegWit annidato, SegWit, Taproot.


![Image](assets/en/04.webp)


Fare clic sul pulsante a rotella superiore e apparirà una schermata a comparsa per scegliere il tipo di Address desiderato. Una volta impostato, la prossima volta che si preme il pulsante di ricezione per l'onchain, il generate sceglierà il tipo di Address selezionato. È possibile cambiarlo in qualsiasi momento.


**4 - Impostazioni dei canali**


In questa sezione si preimpostano alcune caratteristiche dei canali di apertura, come ad esempio:



- numero di conferme
- Canale di annuncio (per impostazione predefinita è disattivato), ciò significa che saranno canali non annunciati
- Canali semplici Taproot
- Mostra il pulsante di acquisto del canale


**5 - Impostazioni sulla privacy**


Qui troverete alcune impostazioni di base per aumentare la privacy utilizzando l'app Zeus:



- Block explorer per aprire i dettagli di tx (Mempool.space, blockstream.info o uno personale personalizzato)
- Leggi appunti - attiva/disattiva se si desidera che Zeus legga gli appunti del dispositivo
- Modalità Lurker - attiva/disattiva se si desidera nascondere specifiche informazioni sensibili dall'applicazione Zeus. È una buona opzione quando si realizzano demo o screenshot.
- Suggerimento tariffe Mempool - attivare questa opzione se si desidera utilizzare i livelli di tariffe raccomandati da [Mempool.space](https://Mempool.space/)


**6 - Sicurezza**


In questa sezione ci sono solo due opzioni per proteggere l'app all'apertura: impostare una password o un PIN.


Una volta impostato un PIN per aprire l'applicazione, è possibile impostare anche un "PIN di costrizione". Questo PIN aggiuntivo segreto verrà utilizzato SOLO in caso di pericolo, se si è minacciati. Se si inserisce questo PIN, la configurazione sarà completamente cancellata. È quindi meglio tenere aggiornati i backup. I backup automatici sono attivi per impostazione predefinita, ma è bene avere anche i propri backup, al di fuori del dispositivo.


**7 - Valuta**


Abilitare o disabilitare l'opzione di visualizzazione della conversione della valuta fiat nell'utilizzo dell'app Zeus. Attualmente supporta oltre 30 valute fiat mondiali.


**8 - Lingua**


È possibile passare da una lingua di traduzione all'altra, recensita dalla comunità Zeus con madrelingua.


**9 - Display**


In questa sezione è possibile personalizzare il display di Zeus, selezionando vari temi di colore, la schermata predefinita (tastiera o bilancia), mostrando l'alias del nodo, attivando i pulsanti grandi della tastiera, mostrando più cifre decimali.


**10 - Punto vendita**


Si tratta di una funzione speciale per attivare/disattivare un sistema PoS integrato in Zeus. Si può gestire un PoS autonomo o collegato a un sistema PoS di Square. Attualmente supporta le funzionalità di base di un PoS, ma è sufficiente per un buon inizio e potrebbe aiutare i piccoli commercianti (bar/ristoranti, negozi di alimentari) ad iniziare ad accettare BTC in modo nativo.


All'interno di queste impostazioni si trovano varie opzioni per configurare il PoS:



- Tipo di pagamento di conferma: Solo LN, 0-conf, 1-conf
- Abilitazione/disabilitazione delle mance per i dipendenti che operano con il PoS
- Mostra / nascondi la tastiera
- Percentuale di tasse da applicare sul biglietto
- Creare prodotti e categorie di prodotti
- Un semplice elenco di tutte le vendite


Ecco un video dimostrativo dal vivo su come utilizzare Zeus PoS:


**B - Backup Wallet**


Il nodo incorporato in ZEUS è basato su LND e utilizza il [formato aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Questo è diverso dal tipico [formato BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) che si vede nella maggior parte dei portafogli Bitcoin, anche se può sembrare simile. Aezeed include alcuni dati extra, tra cui la data di nascita del Wallet, che consentono di eseguire in modo più efficiente le scansioni durante il recupero.


Il formato della chiave aezeed dovrebbe essere compatibile con i seguenti portafogli mobili: Blixt, BlueWallet e Breez. Si noti che il seed da solo non sarà sufficiente a recuperare tutti i saldi se si hanno canali aperti o in attesa di chiusura!


Per saperne di più sul processo di backup e ripristino, consultare la [pagina Zeus Docs](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


CONSIGLIO DI POTENZA: Quando salvate il vostro seed, salvate anche la pubkey del nodo! A volte è bene averla a portata di mano, insieme al seed e all'SCB (Static Channels Backup), nel caso sia necessario verificare il ripristino.


La SCB è necessaria solo se si hanno canali LN aperti. Se si dispone solo di fondi onchain, non è necessario.


Se vedete che dopo molto tempo non vengono ancora mostrati i vecchi tx della cronologia, andate su Nodo incorporato - Peers e disabilitate l'opzione per utilizzare l'elenco dei peer selezionati (di default è btcd.lnolymp.us). In questo modo si attiverà un riavvio e ci si connetterà al primo nodo neutrino disponibile con una risposta temporale migliore. Oppure utilizzare gli altri peer di neutrino ben noti citati di seguito.


Se volete vedere altre opzioni di recupero per un nodo LND, [leggete la mia guida precedente](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), dove potete trovare i passaggi per importare un seed in Sparrow Wallet o altri metodi.


**C - Nodo incorporato**


In questa sezione sono riportati alcuni strumenti di base per la gestione del nodo integrato:



- _Disaster Recovery_ - Backup automatici e manuali per i canali LN. Per ulteriori informazioni su come utilizzare questa funzione, consultare la pagina Zeus Docs.
- l'applicazione Zeus scaricherà il grafico dei pettegolezzi LN da un server dedicato, per una sincronizzazione più veloce e migliore, offrendo i migliori percorsi di pagamento. È possibile scegliere anche di cancellare i dati del grafico precedente all'avvio.
- _Peers_ - sezione per gestire i peer di neutrino e i peer 0-conf. Se si verificano problemi con la sincronizzazione iniziale, i canali non vengono messi online, è perché il dispositivo ha una latenza elevata con il peer neutrino configurato. Provate a cambiare l'elenco dei peer preferiti o aggiungete un peer specifico che sapete avere una latenza migliore per la sincronizzazione. I server neutrini più noti sono:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - per la regione USA
 - sg.lnolymp.us - per la regione Asia
 - btcd-Mainnet.lightning.computer - per la regione USA
 - uswest.blixtwallet.com (Seattle) - per la regione USA
 - europe.blixtwallet.com (Germania) - per la regione UE
 - asia.blixtwallet.com - per la regione Asia
 - node.eldamar.icu - per la regione USA
 - noad.sathoarder.com - per la regione USA
 - bb1.breez.technology | bb2.breez.technology - per la regione USA
 - neutrino.shock.network - Regione USA



- _LND logs_ - strumento molto utile per eseguire il debug dei problemi del nodo LN e controllare in modo approfondito ciò che sta accadendo a un livello più tecnico.
- impostazioni avanzate: ulteriori strumenti per controllare l'uso del nodo LND:



 - modalità di ricerca del percorso - bimodale o apriori, modi per trovare un percorso migliore per i pagamenti del LN e anche per ripristinare le informazioni di percorso precedenti. Leggete queste ottime guide sul pathfinding: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - da Docs Lightning Engineering e [Pathfinding dei pagamenti LN](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - da Voltage
 - _Persistent LND_ - attivate questa modalità se volete che il servizio LND venga eseguito continuamente in background e mantenga il vostro nodo online 24 ore su 24, 7 giorni su 7. Questa modalità è molto utile se si utilizza Zeus come PoS in un piccolo negozio o se si ricevono molti suggerimenti LN sul LN Address.
 - _Rescan wallet_ - questa opzione attiva al riavvio una scansione completa di tutti i tx onchain del Wallet. Attivatela solo nel caso in cui vi manchino alcuni tx nel vostro Wallet. L'operazione di riscansione richiederà del tempo, alcuni minuti, quindi siate pazienti e controllate sempre i log per avere maggiori dettagli sui progressi.
 - _Compact Database_ - questa opzione è molto utile se l'applicazione Zeus occupa molto spazio sul dispositivo (vedere i dettagli dell'applicazione nelle impostazioni del dispositivo). Se avete molte attività con Zeus, vi consiglio di eseguire questa compattazione più spesso. Quando vedete che avete più di 1-1,5 GB di dati per l'applicazione Zeus, eseguite la compattazione. L'operazione si riavvia e richiede un po' di tempo, quindi siate pazienti.
 - _Elimina i file di neutrino_ - questa opzione per eliminare i file di neutrino (con un riavvio) ridurrà di molto l'utilizzo della memoria dati. La riduzione dell'uso dei dati ha anche un grande impatto sull'uso della batteria, riducendo il consumo della stessa, soprattutto se si usa Zeus in modalità persistente.


**D - Informazioni sul nodo**


In questa sezione troverete maggiori dettagli sullo stato del vostro nodo Zeus:



- Alias - ID breve del nodo
- Chiave pubblica - la chiave pubblica completa del vostro nodo, necessaria agli altri nodi per trovare il percorso verso il vostro nodo. Ricordate che questa chiave pubblica NON è visibile sui normali Explorer LN (Mempool, Amboss, 1ML ecc.). Questa pubkey è raggiungibile SOLO attraverso i peer e i canali LN collegati.
- Versione di implementazione LN
- Versione dell'app Zeus
- Stato sincronizzato con la catena e Stato sincronizzato con il grafico: sono molto importanti e mostrano lo stato corretto del nodo. Se questi due non sono visualizzati come "vero", significa che il nodo è ancora in fase di sincronizzazione o che ha qualche problema. Si suggerisce quindi di esaminare i log di LND o di attendere ancora un po'.
- Altezza blocco e Hash - mostra l'ultimo blocco e Hash che il nodo ha visto e sincronizzato.


**E - Informazioni di rete**


Questa sezione mostra ulteriori dettagli sullo stato generale del Lightning Network, estratti dai dati di sincronizzazione del grafico: numero di canali pubblici disponibili, numero di nodi, numero di canali zombie (offline o morti), diametro del grafico, grado medio e massimo del grafico.


Queste informazioni possono essere utili per il debug o semplicemente utilizzate per le statistiche.


**F - Fulmine Address**


In questa sezione l'utente può impostare la propria autocustodia LN Address @zeuspay.com.


ZEUS PAY sfrutta gli hash preimmaginali generati dall'utente, le fatture HODL e lo schema di attestazione Zaplocker Nostr per consentire agli utenti che potrebbero non essere online 24 ore su 24, 7 giorni su 7, di ricevere pagamenti su un fulmine statico Address. Gli utenti devono solo accedere ai loro portafogli ZEUS entro 24 ore per reclamare i pagamenti, altrimenti questi verranno restituiti al mittente.


Se si attiva la "modalità persistente", tutti i pagamenti al vostro LN Address saranno ricevuti istantaneamente.


Scoprite come funzionano i pagamenti [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) e maggiori informazioni su [ZeusPay Fees here](https://docs.zeusln.app/lightning-Address/fees).


**G - Indirizzi Onchain**


In questa sezione si possono consultare gli indirizzi onchain generati per un migliore controllo delle monete


**H - Contatti**


In Zeus v 0.8.0 è stata introdotta una nuova rubrica di contatti che è possibile utilizzare per inviare rapidamente pagamenti ad amici e familiari, anche con la possibilità di importare i contatti da Nostr.


È sufficiente inserire il vostro Nostr npub o il NIP-05 Address leggibile dall'uomo e ZEUS interrogherà Nostr per trovare tutti i vostri contatti. Da qui è possibile inviare un pagamento rapido a un contatto, oppure importare tutti o alcuni contatti nella rubrica locale./<


Ecco un breve video su come configurare e utilizzare i contatti Zeus:


**I - Strumenti**


Qui ci sono varie sottosezioni con altri strumenti:



- conti_ - qui è possibile importare conti esterni / portafogli, portafogli Cold, portafogli Hot, da controllare o utilizzare come fonte di finanziamento esterna per i canali del nodo Zeus. Questa funzione è ancora sperimentale.
- velocizzare la transazione_ - Questa funzione potrebbe essere utile quando si ha una transazione bloccata nel Mempool e si vuole aumentare la tariffa. Dovrete fornire l'output del tx dai dettagli del tx e selezionare la nuova tariffa desiderata. Deve essere più alta di quella precedente e richiede di avere più fondi disponibili nella propria catena Wallet.


![Image](assets/en/05.webp)


È necessario andare sul proprio tx in sospeso e copiare l'outpoint txid. Quindi, passare a questa sezione e incollarlo, quindi selezionare la nuova tariffa che si desidera utilizzare per il bump. Verrà visualizzata una nuova schermata con le tariffe consigliate in quel momento, oppure è possibile impostarne una personalizzata. Ricordate che DEVE essere superiore a quella precedente.


È sempre meglio tenere un UTXO con un Sats da 100k al massimo nel vostro Zeus onchain Wallet, per poterlo usare per far salire le tasse quando è necessario.



- firma o verifica_ - Questa funzione consente di firmare un messaggio specifico con le chiavi Wallet. Può anche essere utilizzata per verificare un messaggio per provare che proviene da una specifica chiave Wallet.
- convertitore di valuta_ - un semplice strumento per calcolare il tasso di conversione tra BTC e altre valute fiat.


**J - Merchandising e supporto**


Qui troverete ulteriori informazioni e link su Zeus, il negozio online, gli sponsor e i social media.


**K - Aiuto**


In quest'ultima sezione troverete i link alla pagina di documentazione di Zeus, ai problemi di Github (se volete inviare un bug o una richiesta direttamente agli sviluppatori dell'app), al supporto via e-mail.



### PASSO 2 - INIZIARE A UTILIZZARE IL NODO ZEUS



Ricordate che Zeus deve essere utilizzato principalmente come LN Wallet, per pagamenti facili e veloci su LN. Certo, contiene anche un Wallet onchain, ma questo dovrebbe essere usato esclusivamente per aprire/chiudere canali LN e non per i pagamenti regolari di un caffè.


Leggete la mia altra guida su [come diventare la vostra banca personale usando i 3 livelli di Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


In questo momento l'utente ha due modi per iniziare a usare Zeus:



- Direttamente su LN, utilizzando il canale 0-conf da Olympus LSP
- Depositare prima in onchain Wallet e poi aprire un normale canale LN con il peer desiderato.


#### Metodo A - Utilizzo dell'LSP Olympus


Si tratta di un modo molto semplice e diretto per far salire a bordo un nuovo utente LN con Zeus. Potrebbe trattarsi di un nuovo utente Bitcoin che non ha mai usato il Sats, di un amico o di un nuovo commerciante che inizia a pagare il suo primo LN.


Per impostazione predefinita, Zeus utilizzerà il proprio LSP, Olympus. Ma in seguito si potrà passare anche ad altri LSP che supportano questo protocollo 0-conf per aprire i canali.


Creando semplicemente un Invoice sul vostro Zeus (inserite l'importo e cliccate sul pulsante "richiedi"), sarete in grado di ricevere subito questi Sats.


Il Invoice che avete generate sarà [avvolto](https://docs.zeusln.app/lsp/wrapped-invoices) e vi verranno presentate le tariffe associate al servizio, se sono state pagate. Questo Invoice avvolto contiene indicazioni di percorso verso il vostro nodo Zeus, in modo che l'LSP possa trovare il vostro nuovo nodo e aprire un canale con i nuovi fondi che state depositando.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Per ottenere un canale LN dal LSP con i fondi che volete ricevere la prima volta, questo Invoice deve essere pagato da un altro LN Wallet e aspettare qualche istante finché il LSP non apre il canale verso il vostro nodo Zeus, detrae la tassa e spinge l'importo rimanente del pagamento sul vostro lato del canale.


Tutto ciò che dovete fare è pagare il Invoice generato per voi in ZEUS con un altro Wallet fulmineo, e il vostro canale si aprirà immediatamente. [Consultare le tariffe dell'LSP di Zeus](https://docs.zeusln.app/lsp/fees).


Un altro vantaggio del pagamento di un canale è l'instradamento a costo zero. Ciò significa che quando si instradano i pagamenti, il primo passaggio attraverso OLYMPUS by ZEUS non comporta spese di instradamento. Si noti che i passaggi oltre OLYMPUS by ZEUS comportano comunque un addebito.


Una volta che il canale è pronto, fate clic sul pulsante destro in fondo allo schermo, che visualizza i canali Zeus.


![Image](assets/en/08.webp)


Vedrete un canale come questo, che mostra il vostro lato del bilanciamento del canale:


![Image](assets/en/09.webp)


Più spendete da questo canale, più liquidità in entrata avrete. Per più Sats che riceverete in questo canale, avrete meno spazio di liquidità in entrata.


Ecco una semplice dimostrazione visiva (di Rene Pickhardt) sul funzionamento dei canali LN:


In questo momento, considerando la schermata dimostrativa dei canali, fate clic sul nome del canale e vedrete maggiori dettagli su di esso.


Avete un singolo canale con Olympus, con una capacità totale di 490 000 Sats, con un saldo di 378k Sats dalla vostra parte e 88k Sats dalla parte di Olympus. Ciò significa che potreste ricevere un massimo di 88k Sats in più nello stesso canale.


Se avete bisogno di ricevere più di 88k Sats (la liquidità disponibile in entrata in questo caso), diciamo altri 500k Sats, creando semplicemente un nuovo LN Invoice con quella quantità, si attiverà una nuova richiesta di canale all'LSP Olympus. Quindi si otterrà un secondo canale.


Per questo motivo, per evitare di pagare più tasse per l'apertura di più canali, si consiglia di aprire per la prima volta un canale più grande, diciamo 1-2 milioni di Sats. Una volta aperto, è possibile scambiare con onchain una parte di questi Sats, ad esempio il 50%, utilizzando qualsiasi servizio di swap esterno descritto in questa guida.


Una volta che si è effettuato lo swap da quel canale, diciamo al 50%, e si è riportato il Sats nel proprio Zeus onchain Wallet, si è pronti per passare al metodo successivo di apertura di un nuovo canale - dal bilanciamento onchain.


#### Metodo B - Utilizzare il saldo onchain


Con questo metodo è possibile aprire canali verso qualsiasi altro nodo LN, compreso lo stesso LSP Olympus. Ma se si dispone già di un canale con Olympus si raccomanda di averlo anche con un altro nodo, per una maggiore affidabilità e per poter utilizzare anche l'MPP (multi-part payment).


![Image](assets/en/10.webp)


Qui sopra è riportato un esempio di pagamento di un LN Invoice tramite MPP. Come si può notare, nella parte inferiore della schermata è presente la voce "impostazioni", che apre una pagina a discesa con ulteriori dettagli sul pagamento che si sta per effettuare. In questa schermata, se avete almeno 2 canali aperti, la funzione MPP sarà attiva per impostazione predefinita. È inoltre possibile attivare la funzione AMP (atomic multi-path) e impostare le parti specifiche desiderate. Si tratta di una funzione molto potente!


Per un nodo privato come Zeus, raccomanderei di avere 2-3 buoni canali (massimo 4-5), con buoni LSP e buona liquidità per coprire tutte le esigenze di pagare o ricevere Sats su LN. [Vedi altri consigli sulla liquidità dei nodi LN in questa guida](/nodes/managing-lightning-node-liquidity-it.html). Ecco anche un'altra [guida generale sulla liquidità del LN](https://Bitcoin.design/guide/how-it-works/liquidity/) del team di progettazione del Bitcoin.


Scegliere i peer giusti, lo so, non è un compito facile, anche per gli utenti più esperti. [Perciò vi darò alcune opzioni per iniziare](https://github.com/ZeusLN/zeus/discussions/2265), questi sono nodi peer che ho testato io stesso usando Zeus (ho cercato di connettermi solo a nodi LND per evitare problemi di incompatibilità)


Qui c'è anche un elenco di nodi peer garantiti per Zeus. Se ne conoscete di buoni, siete invitati ad aggiungerli all'elenco.


È possibile aprire un canale in Zeus accedendo alla vista Canali facendo clic sull'icona del canale nell'angolo in basso a destra della vista principale e poi premendo l'icona + nell'angolo in alto a destra.


![Image](assets/en/11.webp)


Se si desidera aprire un canale con un nodo specifico, fare clic su (A) nell'angolo superiore per scansionare il QR nodeID del nodo (su Mempool, Amboss, 1ML è possibile ottenere tale QR) e tutti i dettagli del peer saranno popolati.


RICORDA:


- I nodi Zeus embedded non utilizzano il servizio Tor! Quindi, per favore, non cercate di aprire canali con nodi che sono sotto Tor! State facendo più danni a voi stessi che aggiungere più privacy. Tor per LN non offre più privacy ma aggiunge più problemi.
- scegliete saggiamente i vostri peer, meglio che siano buoni LSP, buoni nodi di routing, non nodi plebei a caso che potrebbero chiudere i vostri canali e non potrebbero offrire una buona liquidità. [Qui ho scritto una guida dedicata](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) sulla liquidità e sugli esempi di nodi.


Se si fa clic direttamente sul pulsante "Open Channel to Olympus" (Apri canale con Olympus), verranno compilati i campi necessari per aprire un canale con [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


A differenza dei canali LSP a pagamento, il vostro canale richiederà una conferma On-Chain, utilizzando i vostri fondi onchain (potete selezionarli tra i vostri UTXO nella vista del canale aperto); non si aprirà istantaneamente. Consultate prima le tariffe effettive del Mempool e regolatevi di conseguenza, a seconda della velocità con cui volete aprire il canale.


Prima di premere il pulsante per aprire il canale, scorrere le opzioni avanzate:


![Image](assets/en/12.webp)


Dovrete anche assicurarvi che il canale non sia annunciato (privato). Per impostazione predefinita, l'opzione è disattivata per i canali annunciati. Non è consigliabile attivare questa opzione per il nodo incorporato di Zeus; è utile solo quando si usa Zeus con il nodo remoto, come nodo di instradamento pubblico.


A differenza dei canali LSP a pagamento, con l'apertura di canali con questo metodo non beneficerete del routing a tariffa zero.


Fatto questo, basta cliccare sul pulsante "Aprire il canale" e attendere la conferma del messaggio da parte dei minatori. Una volta aperto il canale, potrete effettuare le transazioni che desiderate con il Sats dai vostri canali.


Tenete presente che questi canali avranno tutto l'equilibrio dalla VOSTRA parte, quindi non avrete liquidità in entrata. Come ho detto prima, scambiate o spendete un po' di Sats per acquistare materiale sul LN per "fare più spazio" per ricevere.


Pensate ai vostri canali LN come a un bicchiere d'acqua. Versate dell'acqua (Sats) in un bicchiere vuoto (il vostro canale) fino a riempirlo. Non potete versare altra acqua finché non ne bevete un po' (spendete/scambiate). Quando il bicchiere è quasi vuoto, si versa altra acqua (Sats) utilizzando uno swap in. [Per saperne di più sui servizi di scambio esterni, cliccare qui](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Esistono anche altri servizi LSP che vendono canali in entrata: LNBig o Bitrefill. Credo che ci siano altri servizi come questi, ma al momento non li ricordo.


Quindi, se avete bisogno di un canale LN praticamente vuoto (il saldo è al 100% sul lato peer fin dall'inizio), per ricevere più pagamenti di quanti ne possiate gestire sui vostri canali già pieni, questa potrebbe essere un'ottima opzione. Pagherete una tariffa specifica per aprire questi canali e otterrete molto spazio in entrata.



## SUGGERIMENTI E TRUCCHI


### Limiti di riserva in entrata


Al momento, a causa di alcune limitazioni del codice LN, non è possibile ricevere esattamente l'importo visualizzato in "Inbound". Tenete sempre presente che dovreste fare le vostre fatture con un importo leggermente inferiore, rispettivamente l'importo della "Riserva locale del canale".


![Image](assets/en/13.webp)


Come si può vedere nell'immagine qui sopra, la voce "in entrata" indica che posso ancora ricevere 5101 Sats, ma in realtà in questo momento è impossibile ricevere di più. E si può osservare che è la stessa quantità della "Riserva locale".


Quindi, quando fate le fatture da ricevere, date anche un'occhiata alla liquidità dei vostri canali e deducete la riserva locale da quell'importo, se volete spingere al massimo l'importo del credito.


### Un consiglio rapido per i nuovi utenti che iniziano a utilizzare il nodo Zeus:



- Sfruttate correttamente i vostri nuovi canali.


Ad esempio, se sapete che tra una settimana riceverete, diciamo, 1 milione di Sats, aprite un canale da 2 milioni di Sats e scambiate con il conto onchain Wallet o con un altro conto (temporaneo) LN il 50-60% della vostra liquidità in uscita. Siate sempre pronti con più liquidità. Quando avrete bisogno di più liquidità nei vostri canali Zeus, potrete spostarla di nuovo dai conti di deposito.


Se sapete che invierete, diciamo, 500k Sats a settimana, aprite un canale da 1M Sats. In questo modo avrete ancora una riserva fino a quando non la riempirete di nuovo.



- Se siete commercianti e ricevete sempre più di quanto spendete regolarmente, acquistate un canale inbound dedicato. È il modo più economico. Si paga una tariffa minima e si ottiene un canale "vuoto".



- Non aprite piccoli canali insignificanti di 50-100-300-500k Sats. Li riempirete in pochi giorni, anche se li usate solo per gli zap. Aprite canali più grandi e diversi, NON un solo canale.


Una volta aperto un canale più grande, è sempre possibile utilizzare gli swap sottomarini esterni per spostare le Sats nei portafogli onchain (compreso il ritorno a Zeus onchain). Mantenere un equilibrio tra liquidità in entrata e in uscita è positivo e inoltre potete "riutilizzare" quei Sats per aprire altri canali, se volete.


### Avvolto Invoice


Se si desidera aggiungere maggiore privacy alla ricezione, è possibile utilizzare il metodo "Invoice avvolto". Ricordiamo che per poterlo fare, è necessario disporre di un canale con Olympus LSP. Le fatture avvolte "nascondono" la destinazione finale (il vostro nodo Zeus) e mostrano il vostro nodo LSP come destinazione al pagatore.


Per ottenere un Invoice avvolto, andare alla schermata principale della tastiera, inserire l'importo e premere richiedi. Verrà visualizzato un normale codice QR per il Invoice. A questo punto, fare clic sul pulsante "X" in alto a destra e si verrà reindirizzati a ulteriori opzioni per il Invoice.


![Image](assets/en/14.webp)


Ora dovrete attivare l'opzione in alto "Abilita LSP" e premere il pulsante "Crea Invoice". Questa opzione creerà il Invoice avvolto e, ricordate, addebiterà un piccolo costo.


### Fatture con suggerimenti sul percorso


Si tratta di una funzione molto utile se si desidera gestire la liquidità di più canali in entrata. In pratica, è possibile indicare a quale canale in entrata si vuole ricevere il Sats da un Invoice.


Questa funzione può essere utilizzata anche per il ribilanciamento circolare, quando si vuole spostare la liquidità da un canale pieno a un altro scarico.


Come creare un Invoice con suggerimenti di percorso?



- Nella schermata principale, far scorrere a destra il cassetto LN e fare clic su "Ricezione"
- Nell'impostazione di Invoice, nella parte inferiore, attivate il pulsante "Inserisci suggerimenti di percorso", quindi selezionate la scheda "Personalizzato". Si aprirà una schermata con tutti i canali disponibili. Selezionare quello che si desidera ricevere.
- Compilare tutti gli altri dettagli del Invoice, l'importo, il promemoria ecc. e fare clic su "Crea Invoice".
- Pagando quel Invoice si porterà il Sats nel canale indicato.


Se volete pagare a voi stessi quel Invoice (ribilanciamento circolare), quando lo pagate dal vostro stesso nodo Zeus, nella schermata di pagamento, selezionate il canale in uscita (quello con più liquidità) che volete sia usato come invio del pagamento.


### Pagare con Keysend


Keysend è una funzione di LN molto sottovalutata e gli utenti dovrebbero usarla più spesso.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) consente agli utenti del Lightning Network di inviare pagamenti ad altri, direttamente alla loro chiave pubblica, purché il loro nodo abbia canali pubblici e sia abilitato a keysend. Keysend non richiede che il beneficiario emetta un Invoice.


Come si può fare con Zeus?


È sufficiente scansionare o copiare l'ID del nodo di destinazione (o utilizzare i contatti di Zeus per salvare i nodi di destinazione regolari come contatti) e poi, dalla schermata principale di Zeus, fare clic sul pulsante "Invia". In questa schermata incollare il nodeID o selezionarlo dai propri contatti.


Inserite l'importo di Sats, un messaggio se necessario (sì, potete usarlo anche come chat segreta su LN) e fate clic sul pulsante "Invia". Fatto!


![Image](assets/en/15.webp)


Se avete un canale diretto con il peer di destinazione, non ci saranno spese.


Se non si dispone di un canale diretto con il peer di destinazione, il pagamento keysend pagherà le tariffe come un normale pagamento LN Invoice, instradato su un percorso regolare come qualsiasi altro pagamento. Solo che, ricordate, non rimarrà traccia di un LN Invoice.


## Conlusione


Vi consiglio di leggere la guida [Uso avanzato di Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) con ulteriori istruzioni e casi d'uso.


E... ecco fatto! D'ora in poi potrete utilizzare Zeus Node come un normale BTC/LN Wallet sul vostro cellulare. L'interfaccia utente è piuttosto semplice e facile da usare, intuitiva per qualsiasi tipo di utente, non credo di dover fornire ulteriori dettagli su come effettuare e ricevere pagamenti.


Per concludere, ecco una tabella comparativa della privacy:


![Image](assets/en/16.webp)
