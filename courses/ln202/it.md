---
name: Configurazione di un nodo Bitcoin & Lightning
goal: Deploy di un nodo Bitcoin e Lightning tramite Umbrel
objectives:
  - Installare un nodo Bitcoin
  - Gestire un nodo Bitcoin
  - Utilizzare un nodo Lightning Network
---

# Un viaggio nel lato tecnico di Bitcoin

![locandina del corso](Formation\courses\btc101\assets\affiche\BTC101_vignette-presentation-front.png)

Questa formazione è più tecnica e sarà ancora più vantaggiosa se hai una conoscenza di base di Bitcoin, in particolare la comprensione del funzionamento dei portafogli Bitcoin e dei principi di transazione, mining e blockchain. Non è necessario saper programmare, la tua curiosità e la tua volontà di imparare sono le uniche competenze necessarie. Ricorda, ogni esperto era una volta un principiante. Quindi, prendi una grande boccata d'aria e immergiti nell'entusiasmante universo di Bitcoin. Stai per iniziare un viaggio appassionante e gratificante. Buona fortuna!

+++

# Diventare un Bitcoiner sovrano

![Avvio della formazione](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

Per partecipare pienamente alla filosofia di Bitcoin e incarnare il motto "Don't Trust, Verify", miriamo a diventare utenti sovrani dei nodi Bitcoin. In questo processo, ci affideremo all'interfaccia di Umbrel per configurare il nostro nodo personale. Gli strumenti necessari per questo compito includono un Raspberry Pi, un disco rigido esterno, una scheda SD, un ventilatore e una custodia, per un investimento totale stimato di circa 200€.

Adottando Umbrel come base operativa, saremo in grado di integrare Lightning Network, esplorare la mempool e scoprire soluzioni di multisig. Alla fine di questo viaggio, non solo ci saremo affermati come Bitcoiner sovrani, ma avremo anche la soddisfazione di aver contribuito attivamente alla rete Bitcoin.

# Cosa è un nodo Bitcoin?

![Che cos'è un nodo?](https://youtu.be/19YgL9vkHh4)

Un nodo Bitcoin è semplicemente un dispositivo che esegue il software Bitcoin, la pietra angolare dell'esistenza e della comunicazione della rete. Questi nodi costituiscono la base della decentralizzazione di Bitcoin, assumendo forme diverse e svolgendo diverse responsabilità. Tra queste, ci sono la ricezione e la trasmissione delle transazioni, la visualizzazione delle transazioni in uscita e l'instaurazione di connessioni con altri nodi.
Tre ruoli principali sono assegnati a questi nodi: stabilire il consenso di Bitcoin, convalidare le transazioni e interagire con la rete. Grazie a questa decentralizzazione, Bitcoin beneficia di una maggiore resilienza, con una privacy rafforzata dal fatto di non dipendere da un server terzo. Secondo [Bitnodes](https://bitnodes.io/nodes/all/), circa 43.000 nodi in tutto il mondo formano la rete Bitcoin.

Esploriamo ora le funzioni specifiche di questi nodi all'interno della rete Bitcoin. Un nodo non è solo un software; è anche un gateway per il consenso della rete Bitcoin e l'accesso alla cronologia della blockchain. Ad esempio, i commercianti utilizzano il proprio nodo per convalidare le transazioni in entrata e in uscita.

Il vantaggio di gestire il proprio nodo risiede nell'aumento della privacy e nel raggiungimento della sovranità finanziaria. Infatti, eseguire il proprio nodo rafforza il tuo contributo alla rete e ti fa diventare la tua banca. Ciò ti consente di verificare le transazioni in tempo reale, offrendoti una migliore presa di decisione sulle tue finanze.

In conclusione, far funzionare il proprio nodo nella rete Bitcoin offre numerosi vantaggi. Non solo contribuisce alla decentralizzazione della rete, rafforzando così la resilienza del sistema, ma garantisce anche una maggiore privacy e autonomia finanziaria. Eseguendo questa procedura, potrai autenticare le transazioni in tempo reale, prendere decisioni finanziarie informate ed evitare la dipendenza da un server terzo, garantendo così la tua privacy. Oltre a tutto ciò, eseguire il proprio nodo è un modo concreto per contribuire all'ecosistema Bitcoin e incarnare veramente il ruolo della propria banca.

# Tutorial nodo Bitcoin tramite Umbrel

![Tutorial umbrel](https://youtu.be/mr4iTzdTczI)

In questo capitolo, installeremo noi stessi un nodo Bitcoin, apriremo canali lightning e proveremo un portafoglio multi-firma.
Ciò ha un costo materiale non trascurabile per alcune persone. Sappiate che l'intera formazione può essere seguita SENZA il materiale. Non sarete persi se non avete il vostro nodo.
Se volete provare, ecco i prodotti (link di affiliazione):

- Scheda SD da 16 GB - https://amzn.to/3Qi2Opm
- Raspberry Pi 4 - https://amzn.to/3qoSUYl
- SSD da 1 TB - https://amzn.to/3jSvjLC​
- Custodia esterna per disco rigido - https://amzn.to/3x5R02S
- Alimentatore RASPBERRY - https://amzn.to/3D36zvM
- Custodia Raspberry Pi FLIRC - https://amzn.to/3TNllgi
  Se hai seguito i link di affiliazione, grazie per il tuo supporto! Ciò consente a questo progetto di sopravvivere e offrire sempre più formazioni e contenuti educativi.
  Cosa serve per far funzionare il tuo nodo Bitcoin?

- La blockchain è di circa 500 GB, quindi è necessario prevedere spazio
- La connessione internet deve essere costante con circa 5 GB di larghezza di banda al mese
- È necessaria della RAM per far funzionare BTC Core
- È necessaria più RAM se si fa funzionare Umbrel e un nodo LN (minimo 4 GB)

Puoi quindi far funzionare il tuo nodo Bitcoin direttamente sul tuo computer o utilizzare un sistema come quello mostrato nel video con un Raspberry Pi.

Esistono già altre [soluzioni](https://thebitcoinmanual.com/behind-btc/nodes/buy-node/) già pronte!

Segui questi passaggi per creare un nodo completo con un Raspberry Pi e Umbrel. Prima di iniziare, tieni presente che avrai bisogno di circa 200 euro per l'acquisto dell'hardware necessario, anche se il software è gratuito.

1. **Preparazione degli strumenti**: Vai su [Umbrel](https://umbrel.com/), una soluzione open source nota per la sua eccellente interfaccia utente e il suo buon servizio, per scaricare il software necessario. Inoltre, avrai bisogno di Benella Itcher per flashare la scheda SD.
2. **Assemblaggio del Raspberry Pi**: Assembla il tuo Raspberry Pi. Assicurati di installare la ventola e i piccoli componenti di raffreddamento inclusi nel kit.
3. **Flash della scheda SD**: Utilizza il dispositivo fornito nel kit per flashare la scheda SD. Se incontri difficoltà, prova a formattare la scheda o a scollegare/ricollegare il dispositivo.
4. **Connessione dell'hardware**: Una volta che la scheda SD è stata flashata, collega l'SSD al Raspberry Pi tramite una porta 3.0. Quindi, collega il Raspberry Pi al tuo router e a una fonte di alimentazione elettrica.
5. **Configurazione di Umbrel**: Dopo circa 5 minuti, potrai accedere all'interfaccia di Umbrel sul tuo computer. Si consiglia di utilizzare un gestore di password per creare e salvare una password sicura per l'accesso al tuo nodo Umbrel.
6. **Protezione del tuo seed (frase mnemonica)**: Il tuo seed è la chiave privata che ti dà accesso ai tuoi bitcoin. Assicurati quindi di conservarlo in un luogo sicuro. Evita di fare foto o screenshot del tuo seed. Si consiglia inoltre di salvare il link TOR nel tuo gestore di password per un facile accesso in futuro.
7. **Esplorazione del dashboard di Umbrel**: Umbrel ha un dashboard chiaro e un App Store innovativo per scaricare altre applicazioni. Il tutorial di Umbrel è accessibile a tutti, basta acquistare l'hardware e seguire i passaggi.
8. **Prendre conscience de l'importance des nœuds**: I nodi sono essenziali per trasformare il sistema bancario e sostituire le banche centrali. Con il tuo proprio nodo, partecipi alla verifica delle transazioni Bitcoin e al rispetto delle regole del protocollo. Facendo funzionare il tuo proprio nodo, non hai più bisogno di fidarti di un terzo di fiducia e puoi verificare le transazioni da solo. I nodi sono un pilastro essenziale della tua sovranità finanziaria.

Seguendo questi passaggi, puoi contribuire alla decentralizzazione della rete Bitcoin, aumentare la tua privacy e autonomia finanziaria e partecipare attivamente all'evoluzione del sistema bancario tradizionale. Quindi, non esitare a lanciarti e diventare un vero Bitcoiner sovrano.

# Overview di Umbrel

![umbrel overview](https://youtu.be/cwEa61BgemM)

Ci apprestiamo ad esaminare in modo esaustivo questa interfaccia che facilita la gestione del tuo portafoglio Bitcoin e Lightning Network.

Per iniziare, ci identificheremo nell'account utilizzando una password sicura e un gestore di password dedicato. Successivamente, esploreremo in dettaglio l'interfaccia, familiarizzando con le caratteristiche distintive del portafoglio Bitcoin e della Lightning Network.

Il nodo comunicherà con altri nodi sulla rete peer-to-peer di Bitcoin in modo casuale e sotto pseudonimo. Questa caratteristica essenziale consente di scaricare l'intera blockchain (anche chiamata timechain) senza dover dipendere da un'entità centrale. Tuttavia, è necessario considerare che il download iniziale della timechain può richiedere diversi giorni, poiché rappresenta un volume di oltre 500 GB da ricevere.

Successivamente, effettueremo transazioni all'interno del portafoglio Bitcoin, compresa una prova di trasferimento verso un portafoglio multisig. In seguito, ci concentreremo sull'apertura dei canali della Lightning Network e sull'utilizzo delle connessioni attive nel portafoglio della Lightning Network. L'apertura dei canali richiede una certa esplorazione visiva.

Dopo aver effettuato queste operazioni, Bitcoin Core diventa operativo. Sei quindi in grado di connettere alcuni dei tuoi portafogli al tuo nodo per verificare lo stato dei tuoi conti.

È possibile collegare i tuoi portafogli Bitcoin come [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) al tuo nodo Bitcoin tramite un'interfaccia dedicata. Collegando il tuo portafoglio al tuo nodo personale, puoi confermare la ricezione dei fondi senza dover fidarti di un server esterno, il che è particolarmente consigliato per i commercianti.
Umbrel propone anche un App Store che raggruppa Explorer, molti altri servizi legati a Bitcoin, Lightning o all'hosting dei propri dati. Nuove applicazioni vengono regolarmente aggiunte al loro [appstore](https://apps.umbrel.com/).
Per ulteriori informazioni e supporto, non esitate a consultare il loro sito web, la chat Telegram, Discord, Github e Reddit. In sintesi, grazie ad Umbrel, avete la possibilità di riprendere il controllo della vostra sovranità finanziaria grazie a Bitcoin e diventare la vostra banca, contribuendo alla rete. Vi incoraggiamo vivamente ad approfondire e imparare questa tecnologia per integrarla nel vostro negozio, e-commerce, vita personale o semplicemente per curiosità.

# Analisi della MemPool

![mempool](https://youtu.be/0xS859IoMh8)

La MemPool, intrinsecamente, funziona come uno spazio di transito per le transazioni Bitcoin in attesa di essere validate nella blockchain. Per esaminare la MemPool in modo efficace, Umbrel è lo strumento di scelta. L'applicazione [Mempool.space](https://mempool.space/), accessibile tramite l'interfaccia di Umbrel, fornisce una rappresentazione chiara delle transazioni in attesa, dei costi associati e di varie altre funzionalità pertinenti.

La blockchain di Bitcoin è essenzialmente un database che incorpora blocchi di transazioni a intervalli regolari di circa 10 minuti. Dopo ogni serie di 2016 blocchi, la difficoltà di mining si adatta per mantenere questo intervallo medio. Se i minatori decidono di ritirare la loro energia dalla rete Bitcoin, il tempo medio necessario per trovare nuovi blocchi aumenta, portando a una diminuzione della difficoltà di mining e consentendo ad altri minatori di diventare competitivi.

Oltre alla difficoltà di mining, il costo attuale di una transazione Bitcoin è visibile sulla dashboard, così come la blockchain con la sua catena di blocchi. Le commissioni per una transazione Bitcoin sono attualmente di 40 sats/vbyte. Le commissioni di transazione su Bitcoin si basano sulla complessità della transazione, che è considerata proporzionale al peso virtuale (i vbyte) della transazione. I vbyte, o byte virtuali, sono un'unità di misura utilizzata in Bitcoin per valutare la dimensione di una transazione tenendo conto della tecnologia SegWit. Pertanto, l'uso dei vbyte consente una misura più precisa dell'efficienza dello spazio in un blocco.

Ogni utente è libero di determinare le commissioni associate alla propria transazione, che tendono a riflettere l'urgenza della convalida della transazione: più l'utente desidera che la sua transazione venga convalidata rapidamente, più le commissioni aumentano. Pertanto, poiché il volume di un blocco è limitato a 4 MB (anche se la dimensione media dei blocchi è di circa 1,5 MB), quando la domanda aumenta, le commissioni per aumentare la probabilità che la nostra transazione venga inclusa nel prossimo blocco possono aumentare significativamente.
Bitcoin ha diverse strati: il Mainnet (la catena principale), il Testnet e il Signet (catene dedicate all'esperimentazione e alla validazione di nuove funzionalità), il Lightning Network (una rete di pagamento) e Liquid (una sidechain dove i blocchi sono validati ogni minuto). Ogni strato ha la propria utilità e i propri casi d'uso specifici.

I blocchi che contengono le transazioni sono costruiti dai pool di mining e il loro livello di riempimento varia in base alla domanda e al tempo trascorso dal mining dell'ultimo blocco. Strati superiori, come il Lightning Network, consentono transazioni più veloci e meno costose rispetto alla blockchain principale, ma si basano comunque su Bitcoin per il loro modello di sicurezza.

In conclusione, gli esploratori di blocchi consentono di seguire le transazioni in tempo reale o di rintracciarle nel passato. Queste transazioni possono presentare livelli di complessità variabili. Mempool offre una soluzione efficace per visualizzare la blockchain, seguire le transazioni e analizzare le commissioni e la congestione della rete.

# Esploratore di blocchi e analisi statistiche

![esploratore di blocchi e analisi statistiche](https://youtu.be/Qe9VaUhUS0E)

Inizieremo un viaggio di esplorazione attraverso la blockchain di Bitcoin, utilizzando strumenti potenti come gli esploratori di blocchi e l'applicazione BTC Explorer sul nodo Umbrel. Gli esploratori di blocchi ci danno la capacità di analizzare in dettaglio la blockchain di Bitcoin. Con BTC Explorer, un'applicazione su Umbrel, è possibile verificare tutte le informazioni relative alla blockchain di Bitcoin che si trovano sul proprio disco rigido, il che consente di non dipendere più dalla fiducia di terzi.

Ci riferiamo a una transazione specifica, la stessa esaminata nel corso precedente, per dimostrare le funzionalità e l'importanza di questi strumenti. Illustreremo anche gli ultimi blocchi minati e dettaglieremo le informazioni sul loro contenuto. Poi, faremo un confronto approfondito tra due blocchi distinti, analizzando il loro contenuto e il tempo impiegato per il mining.

L'esploratore di blocchi ci consente di visualizzare i dettagli di un blocco minato, come l'hash, il sommario, gli output, le commissioni, il tempo e le transazioni. Per quanto riguarda Bitcoin Explorer, offre strumenti più sofisticati per l'analisi della blockchain. Il primo strumento consente ad esempio di esaminare in dettaglio il proprio nodo (sincronizzazione, indice, dimensione della blockchain, BIP accettati).

Le proposte di miglioramento di Bitcoin (BIP) sono proposte di miglioramento del protocollo Bitcoin. Possiamo osservare l'attivazione di Segwit e il numero di connessioni di rete. Inoltre, i Blockstats forniscono statistiche dettagliate sulle commissioni, le transazioni, gli input e gli output.
L'analisi dei dati di Segwit offre una panoramica sull'evoluzione di Bitcoin nel corso degli anni. Le statistiche sulle transazioni, i volumi, i blocchi, gli UTXO e i timestamp sono disponibili gratuitamente. L'interpretazione di questi dati è cruciale per la ricerca finanziaria e per verificare l'adozione di Bitcoin.

È importante prendere in mano la propria sovranità finanziaria e cercare i dati da soli. L'analisi dei blocchi consente di studiare i dati di un blocco specifico, come il primo blocco estratto da Satoshi nel 2009, in cui ha distrutto volontariamente i suoi primi 50 bitcoin per un lancio onesto.

I dati delle transazioni Bitcoin sono trasparenti e consultabili da tutti, compresi gli analisti e i professionisti del settore. Queste informazioni sono vitali perché forniscono preziose indicazioni sull'attività della rete Bitcoin, la dinamica del mercato e le tendenze in corso, che sono essenziali per una decisione informata e l'implementazione di solide strategie finanziarie. Inoltre, questi dati vengono utilizzati per il monitoraggio delle transazioni, garantendo la tracciabilità e la trasparenza della rete Bitcoin.

Una transazione Bitcoin "pesante", come ad esempio una che contiene 673 input e 1 output, illustra il compromesso tra il numero di UTXO (Unspent Transaction Outputs) e la quantità di Bitcoin in un indirizzo. Gli UTXO rappresentano i fondi non spesi di una transazione precedente, che diventano gli input delle transazioni future. L'aumento del numero di UTXO in una transazione la rende più complessa e costosa. Pertanto, è essenziale raggruppare gli UTXO per minimizzare le commissioni di transazione e ottimizzare l'utilizzo dello spazio in un blocco della blockchain Bitcoin.

Il mining, fulcro centrale del protocollo Bitcoin, svolge un ruolo fondamentale nella sicurezza delle transazioni. Il processo è regolato da un'aggiustamento della difficoltà ogni 2016 blocchi per mantenere un intervallo medio di 10 minuti tra i blocchi. Allo stesso tempo, il tasso di hash, riflesso della potenza di calcolo della rete, è in costante aumento.

All'interno della rete, i minatori si raggruppano in pool di mining. Queste entità non hanno il potere di controllare l'intera rete poiché i minatori hanno il privilegio di poter passare da un pool all'altro a loro discrezione. Tecnologie innovative come Stratum V2 danno più potere ai minatori all'interno dei pool di mining. Inoltre, soluzioni tecniche come MimbleWimble e Dandelion si presentano come promettenti miglioramenti per le transazioni.
Par ailleurs, la ricchezza storica della blockchain risiede nel fatto che archivia tutte le transazioni, dal blocco genesi alle transazioni più recenti. Essa comprende la prima transazione Bitcoin effettuata da Satoshi a Hal Finney al blocco 170 e la famosa transazione di 10.000 bitcoin per due pizze al blocco 57043, evento all'origine della celebrazione annuale del "Pizza Day" il 22 maggio.
Per rafforzare la propria sovranità finanziaria ed evitare la dipendenza da terzi per la ricezione e l'invio dei propri bitcoin, è cruciale connettere i propri portafogli al proprio nodo Bitcoin. Le transazioni vengono prima validate dai nodi della rete durante la loro propagazione, e poi una seconda volta quando vengono incorporate in un blocco.
In conclusione, condividere e iniziare il proprio entourage a Bitcoin è un'azione lodevole. Sfruttando il proprio nodo e contribuendo alla rete, si può diventare la propria banca. L'obiettivo ultimo è diventare completamente autonomi.

# Collegare il proprio portafoglio al proprio nodo

![collegare il proprio portafoglio al proprio nodo](https://youtu.be/HOV3bVcram4)

Nel mondo digitale di oggi, proteggere le proprie criptovalute e la propria privacy è fondamentale. È in questo contesto che vi guiderò nella connessione dei vostri portafogli mobili e desktop al nostro nodo Bitcoin. Questa procedura aumenta significativamente la vostra sicurezza e il vostro controllo sui vostri asset.

Esistono molteplici portafogli disponibili: Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum e molti altri. Ognuno ha le sue specificità, i suoi punti di forza e di debolezza. Per oggi, ci concentreremo su Sparrow, un'alternativa interessante a Ledger Live, nota per la sua facilità di gestione e creazione di portafogli.

In materia di sicurezza e privacy, si può fare un ulteriore passo avanti: l'uso di un server privato invece di un server pubblico. Questa procedura, sebbene più complessa, garantisce un livello superiore di controllo e protezione. Troverete le informazioni necessarie per la connessione a un server privato su Umbrel.

Ricordatevi che mantenere i vostri portafogli aggiornati è un gesto essenziale. Gli aggiornamenti correggono i bug, combattono le vulnerabilità, migliorano il prodotto e talvolta aggiungono nuove funzionalità utili. Umbrel, in particolare, garantisce l'aggiornamento automatico di tutte le sue applicazioni. È quindi saggio mantenere il proprio Umbrel aggiornato.
Per concludere, collegare i vostri portafogli direttamente al nostro nodo Bitcoin è un passo verso l'indipendenza finanziaria. Ciò vi conferisce un livello di privacy e sicurezza superiore, consentendovi di mantenere il controllo totale sui vostri asset digitali. La sovranità finanziaria significa avere la piena proprietà e il controllo del proprio denaro, senza intermediari. Diversificando i vostri portafogli e mantenendoli aggiornati, fate un passo in più verso questa autonomia.

# I portafogli multi-sig tramite Specter

![i portafogli multi-sig](https://youtu.be/mV1KS-Uwjew)

Vi proponiamo di fare un ulteriore passo verso l'autonomia finanziaria. Il nostro obiettivo è la creazione di un portafoglio multi-sig con l'applicazione Specter, integrata in Umbrel. Collegando l'applicazione Desktop al nostro nodo, questo tutorial sarà accessibile a tutti.

Il concetto di multi-sig è semplice: garantire un livello di sicurezza eccezionale per le somme importanti. Per questo, utilizzeremo tre chiavi private per proteggere il nostro nuovo portafoglio Bitcoin. Esistono diversi livelli di sicurezza: portafoglio mobile, portafoglio fisico, passphrase, multi-sig 2 su 3, multi-sig 3 su 5, o anche una combinazione di tutti questi elementi con open dimes. Non è necessario essere esperti di tecnologia per seguire questo tutorial, ma è richiesta una certa familiarità con il sistema di chiavi private e pubbliche.

Preparatevi, perché il tutorial è veloce. Avendo già inizializzato i dispositivi, ci vorranno circa 15 minuti. Per seguire, avrete bisogno di tre dispositivi inizializzati, di un nodo per collegare l'applicazione Specter, una chiave USB e una stampante. Utilizzeremo l'applicazione Specter per la nostra soluzione multi-sig. Potete scaricarla tramite Umbrel o direttamente dal sito web di Specter Solutions. Non dimenticate di verificare la firma prima del download. Potete anche fare il vostro multi-sig con Sparrow o Electrum. Non esitate a fare le vostre ricerche e a prendervi il tempo di familiarizzare con questi strumenti prima di utilizzarli per gestire somme importanti.

Passiamo ora alla pratica. Qui, abbiamo realizzato un 2 su 3 con una ledger e 2 trezor (bianco e nero) e Specter Desktop, che è l'interfaccia del portafoglio che ci consente di interagire con i nostri portafogli e che è collegata a Bitcoin Core tramite Umbrel.
Creeremo prima un portafoglio semplice per interagire con Ledger senza Ledger Live. Ciò ci permetterà di generare nuovi indirizzi e inviare Bitcoin. Aggiungeremo poi altri dispositivi (tesori) per creare il multisig. Iniziamo scegliendo il secondo dispositivo (il Tesoro bianco) che connetteremo tramite USB. Dopo aver usato il PIN per attivarlo, estraiamo le chiavi pubbliche e creiamo un secondo portafoglio. Aggiungeremo poi un terzo dispositivo (il Trezor Nero) e lo useremo per creare un portafoglio multisig. Creeremo un portafoglio multisig scegliendo i tre dispositivi, utilizzando Signet per testare e non perdere fondi in caso di errore (tuttavia la procedura è la stessa per il mainnet).

Creeremo poi il portafoglio combinando le chiavi pubbliche. Il backup di un portafoglio multisig contiene diversi elementi. Infatti, per ricreare il portafoglio avremo bisogno delle tre chiavi pubbliche e di due chiavi private per spendere i soldi. È quindi cruciale conservare le chiavi pubbliche con il backup di ciascuna delle chiavi private in un luogo sicuro.

Si consiglia di scrivere su carta o su metallo le frasi mnemoniche (elenco di 24 parole) delle 3 chiavi private in più copie (almeno 2). Inoltre, si consiglia di scrivere informazioni precise e dettagliate che consentano di recuperare i propri soldi in caso di problemi o per un piano di eredità. Queste istruzioni devono essere conservate anche in un luogo sicuro.

In questo modo, avrai fatto un passo avanti sulla strada della sovranità di Bitcoin. Gestendo la tua sicurezza e utilizzando strumenti come il multisig, rafforzi la tua autonomia finanziaria e proteggi i tuoi asset in modo ottimale. Ricorda, la prudenza e l'apprendimento continuo sono le chiavi del successo nel mondo di Bitcoin.

Se vuoi esercitarti con i bitcoin di Testnet, puoi ottenerli tramite questo [faucet](https://bitcoinfaucet.uo1.net/).

# Apertura dei canali Lightning

![apertura dei canali](https://youtu.be/bAZJn0AH1yU)

Passiamo ora alla parte Lightning del nodo Umbrel. Utilizzeremo ThunderHub, un'applicazione tra molte che fungono da gestore del nodo Lightning, come Lightning Terminal e RideTheLightning (RTL). Queste applicazioni ci danno una visione precisa dello stato dei nostri canali, fungendo da interfaccia tra noi e i nostri canali Lightning Network (LN).
A questo punto, il nostro obiettivo principale è l'apertura di un nuovo canale. Quando si scarica ThunderHub, viene fornita una password predefinita, che è possibile trovare direttamente nell'appstore. È essenziale cambiarla e conservare con cura questa nuova password in un gestore di password dedicato.

Quando si considera l'apertura di un canale con un altro nodo Lightning della rete, sorgono alcune domande. Ad esempio, quale quantità di liquidità si desidera allocare in un canale? Con quali parti si desidera aprire un canale? Le risposte a queste domande sono cruciali per ottimizzare le transazioni e evitare potenziali problemi.

Parliamo delle dimensioni dei canali. Non sarebbe saggio iniziare aprendo canali con un importo basso, come 20k, 50k o 100k sats. Sarebbe insufficiente e le spese di apertura e chiusura del canale non sarebbero coperte. Un canale di importo basso sarebbe più dannoso che utile per te e per il resto della rete. Ad esempio, se avessi un canale di 20k aperto con il mio nodo, coprirebbe appena le spese di apertura e chiusura (+ riserva). Ti resterebbero solo briciole da spendere.

Ecco perché è consigliabile aprire canali di almeno 500k-1M sats. Ciò offrirebbe un routing migliore, benefico per te e per tutti gli altri che instraderebbero le transazioni attraverso il tuo nodo. È importante notare che l'idea di "più è grande, meglio è" non si applica qui. Sarebbe preferibile avere 5-6 canali in uscita, ognuno contenente tra 500k e 1M sats, e, a seconda delle esigenze, 4-5 canali in entrata con una capacità simile.

Ora che sei familiare con le dimensioni dei canali, passiamo alla loro gestione. Per quanto riguarda la liquidità in uscita (dal tuo lato), il tuo nodo LN ti consente di effettuare pagamenti LN, acquistare cose, inviare denaro agli amici, pagare servizi, ecc. Cerca di aprire canali LN con i commercianti con cui prevedi di scambiare. Per quanto riguarda la liquidità in entrata (dal lato dei tuoi peer), trova peer disposti ad aprire canali verso il tuo nodo. Questa liquidità in entrata è necessaria per ricevere pagamenti sulla LN.
La questione di con chi aprire i canali è fondamentale. In primo luogo, con i commercianti con cui intendi effettuare transazioni, potrai beneficiare di un routing diretto ed evitare le commissioni. In secondo luogo, pensa agli amici e agli utenti esperti di LN che conosci e che possono creare un anello di nodi (ring of fire) con una certa quantità di sats per questi canali. Questo è perfetto per bilanciare la liquidità riducendo le commissioni tra i nodi dell'anello. In terzo luogo, il tuo anello di nodi può avere connessioni o canali "esterni" con altri buoni nodi, facilitando e accelerando il routing verso qualsiasi destinatario.

Per stabilire queste connessioni, dovrai recuperare gli indirizzi pubblici delle altre parti. Puoi farlo chiedendo direttamente o tramite siti come [1ML](https://1ml.com/) o [Amboss](https://amboss.space/). L'apertura di un canale comporta commissioni di transazione in catena, quindi approfitta dei momenti in cui la Mempool è vuota per aprire i canali. Una volta aperto un canale, la liquidità è bloccata da un lato del canale. Per spostarla dall'altro lato, è necessario effettuare transazioni per i pagamenti o effettuare ciò che viene chiamato uno "scambio sottomarino" (lo vedremo nella prossima parte). È importante notare che nella Lightning Network ci sono commissioni di routing. Se un canale si svuota troppo velocemente a causa del routing, puoi aumentare queste commissioni.

Prima di concludere, è importante notare che c'è un'altra decisione cruciale da prendere quando si aprono i canali Lightning: scegliere tra un canale pubblico o un canale privato. Ognuno ha i suoi vantaggi e svantaggi, a seconda delle tue esigenze e preferenze.

Un canale pubblico è annunciato a tutta la rete Lightning e può essere utilizzato per il routing dei pagamenti. È un'ottima opzione se desideri partecipare attivamente alla rete e aiutare a facilitare le transazioni degli altri utenti. Ciò può anche generare entrate (molto basse) grazie alle commissioni di routing che puoi percepire. Tuttavia, tieni presente che poiché un canale pubblico è visibile a tutti, non è adatto se stai cercando di mantenere un alto livello di privacy.

D'altra parte, un canale privato non è annunciato alla rete e non verrà utilizzato per il routing dei pagamenti. È una buona opzione se privilegi la privacy e prevedi di utilizzare il canale principalmente per le tue transazioni. È importante notare che anche se un canale privato non offre le stesse opportunità di entrate delle commissioni di routing di un canale pubblico, può offrire una maggiore tranquillità in termini di sicurezza e privacy.
In fin dei conti, la scelta tra un canale pubblico e un canale privato dipende dalla vostra situazione e dalle vostre priorità. Valutate attentamente le vostre esigenze e i vostri obiettivi prima di prendere una decisione.

In conclusione, l'apertura dei canali nella Lightning Network è un passaggio tecnico essenziale per ottimizzare le vostre transazioni. La scelta delle dimensioni dei vostri canali, la scelta tra un canale pubblico o privato e la selezione oculata delle parti con cui aprire i canali sono fattori determinanti per un routing efficiente ed economico. Nella nostra prossima sezione, ci concentreremo sulla gestione efficace di questi canali. Quindi, passate alla prossima sezione per ulteriori dettagli su questo importante aspetto della Lightning Network.

# Gestione dei canali LN

![gestione dei canali LN](https://youtu.be/CgBnGQLar4o)

Ora che abbiamo coperto l'apertura dei canali della Lightning Network, rivolgiamo la nostra attenzione alla loro gestione. Una gestione efficace dei canali può fare una grande differenza nell'ottimizzazione della vostra esperienza nella Lightning Network.

Il primo elemento essenziale della gestione dei canali è il bilanciamento. I canali della Lightning Network hanno ciò che si chiama "liquidità", che è divisa tra le due parti del canale. Il bilanciamento di questa liquidità è cruciale per assicurarsi che le transazioni possano essere instradate efficacemente dal vostro nodo. Troppa liquidità da un lato o dall'altro può rendere il canale meno utile per il routing. Fortunatamente, esistono diverse strategie per bilanciare i canali, tra cui l'utilizzo di servizi come Lightning Loop di Lightning Labs, che consente di spostare la liquidità dentro e fuori dalla rete Bitcoin.

Il secondo elemento da considerare è la monitoraggio dei vostri canali. È importante controllare regolarmente lo stato dei vostri canali e monitorare le prestazioni del vostro nodo. Strumenti come ThunderHub e RTL offrono grandi funzionalità per aiutare a monitorare il vostro nodo e gestire i vostri canali. Forniscono informazioni sullo stato dei vostri canali, inclusa la loro liquidità, le loro commissioni e la loro capacità. Inoltre, offrono funzionalità per chiudere i canali, aprire nuovi canali e riequilibrare la liquidità tra i canali.

In terzo luogo, è necessario considerare la chiusura dei canali. A volte, potreste trovarvi con un canale che non è più utile o performante. In questo caso, vorrete chiudere il canale. Tuttavia, è importante notare che la chiusura di un canale comporta una transazione sulla blockchain di Bitcoin, il che può comportare commissioni. Pertanto, è saggio chiudere i canali durante i periodi di bassa congestione sulla blockchain per minimizzare le commissioni.
In conclusione, la gestione dei canali della Lightning Network è un elemento importante per mantenere un nodo Lightning performante ed economico. Con una buona strategia di bilanciamento, una regolare monitoraggio e una gestione intelligente dell'apertura e della chiusura dei canali, è possibile ottimizzare la propria esperienza con la Lightning Network. Nel prossimo segmento, affronteremo un altro aspetto cruciale della Lightning Network: la sicurezza.

# Rinominare il proprio nodo LN

![rinominare il proprio nodo LN](https://youtu.be/HnK1_TDYXsY)

Personalizzare l'alias del proprio nodo Lightning Network è un'ottima maniera per distinguersi sulla rete. Non solo è pratico, ma è anche un modo per personalizzare la propria esperienza. Per cambiare l'alias del proprio nodo, useremo l'interfaccia della riga di comando. Per coloro che non sono familiari con questa interfaccia, non preoccupatevi, questa guida vi aiuterà passo dopo passo.

Per iniziare, è necessario aprire il terminale del proprio sistema. Il terminale è un'interfaccia di comando che consente di interagire direttamente con il proprio sistema operativo. Una volta aperto il terminale, digitare il comando `ssh -t umbrel@umbrel.local` e premere Invio. Questo comando stabilirà una connessione sicura con il proprio Umbrel.

Successivamente, verrà richiesto di inserire la password del proprio Umbrel. Notare che per motivi di sicurezza, la password non viene visualizzata a schermo durante la digitazione. Dopo aver inserito la propria password, si accederà all'interfaccia del proprio Umbrel.

Una volta connessi, digitare il comando `sudo nano umbrel/lnd/lnd.conf` nel terminale e premere Invio. Ciò porterà ad un editor di testo chiamato Nano, dove è possibile modificare il file di configurazione del proprio nodo Lightning.

Ancora una volta, sarà necessario inserire la propria password. Successivamente, navigare nel file fino alla sezione intitolata "Application Options". In questa sezione, aggiungere la riga `alias=SOMENAME`, sostituendo "SOMENAME" con l'alias desiderato per il proprio nodo. Notare che l'uso del mouse è inutile in questa interfaccia, quindi utilizzare le frecce per navigare.

Per salvare le modifiche, premere `Ctrl-X`, quindi premere `Y` e infine premere Invio. Ciò chiuderà l'editor e salverà le modifiche. Per rendere effettive queste modifiche, è necessario riavviare il proprio Umbrel. Per farlo, accedere al menu delle impostazioni dell'interfaccia Umbrel e scegliere l'opzione di riavvio.

Ecco fatto, si è riusciti a cambiare l'alias del proprio nodo Lightning Network! Ora è possibile rivendicare il proprio nodo su siti come 1ML o Amboss. Nella prossima sezione, discuteremo di altre metodologie per personalizzare e ottimizzare il proprio nodo Lightning Network.

### Sostienici

Questo corso, così come l'intero contenuto presente su questa università, ti è stato offerto gratuitamente dalla nostra comunità. Per supportarci, puoi condividerlo con chi ti sta intorno, diventare membro dell'università e persino contribuire al suo sviluppo tramite GitHub. A nome di tutto il team, grazie!

### Nota sulla formazione

Un sistema di valutazione per la formazione sarà presto integrato in questa nuova piattaforma di E-learning! Nel frattempo, grazie mille per aver seguito il corso e se ti è piaciuto, pensa di condividerlo con chi ti sta intorno.

# Utilizzo divertente di LN

![utilizzo di LN](https://youtu.be/6yekAvH13E0)

Ora che hai configurato il tuo nodo, è il momento di usarlo. Per questo primo utilizzo, ci concentreremo su [Satoshi's Place](https://satoshis.place/), un servizio affascinante che ti consente di spendere satoshi, l'unità più piccola di bitcoin, per fare pixel art su una piazza pubblica online. Ogni pixel cambia colore per un satoshi. Sii libero di dare libero sfogo alla tua creatività, per la mia parte, ho creato una pokeball per 166 satoshi! I pagamenti avvengono tramite "fatture" o "invoices" sulla rete Lightning. Queste fatture possono essere rappresentate sotto forma di codice QR, rendendo il pagamento facile e istantaneo.

Quando una transazione attraversa più nodi, di solito sono coinvolti costi di routing. È quindi cruciale essere ben connessi al centro della rete per ridurre questi costi. Un'alternativa sarebbe quella di aprire un canale direttamente con il commerciante. Ciò presenta diversi vantaggi, tra cui costi di transazione più bassi e una velocità di transazione più rapida.

A titolo di esempio, creeremo un canale con Satoshi's Place per i futuri pagamenti. Dopo la creazione del canale, è necessaria un'attesa di circa 30 minuti affinché il canale diventi operativo. Una volta creato il canale, puoi effettuare pagamenti diretti. Ad esempio, puoi inviare un satoshi gratuitamente tramite la rete Lightning senza intermediari di fiducia.

La rete Lightning presenta diversi vantaggi, tra cui il suo basso costo e la possibilità di effettuare pagamenti regolari. Per iniziare, è consigliabile utilizzare portafogli come Wallet of Satoshi o Alby. Questi portafogli consentono di pagare le fatture utilizzando la rete Lightning. Per saperne di più, puoi leggere questo [articolo](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) di Darthcoin.

In conclusione, la rete Lightning dimostra la capacità di Bitcoin di evolversi. Non solo consente transazioni a basso costo, ma offre anche una soluzione ai problemi di scala che Bitcoin ha avuto in passato.

# Accettare Bitcoin con BTCpay server

![accettare bitcoin nel proprio commercio](https://youtu.be/zpCMlLfiRgg)
Durante questo ultimo capitolo, esploreremo i diversi modi per accettare Bitcoin per la vostra attività commerciale. Esamineremo tre opzioni principali, ovvero BTCPay Server tramite il vostro nodo Umbrel, BTCPay tramite un nodo Luna esterno e infine tramite OpenNode. È essenziale notare che ogni opzione ha le sue sfumature, ed è cruciale scegliere quella che meglio si adatta alle vostre esigenze specifiche.

Immaginiamo che siate proprietari di un ristorante e che abbiate un nodo Umbrel nel vostro locale. In questo caso, potete utilizzare BTCpay direttamente sotto Tor. È una soluzione ideale per le operazioni fisiche in cui i clienti pagano di persona.

Tuttavia, per un e-commerce, l'utilizzo di BTCPay sotto Tor del proprio nodo Umbrel non è realizzabile. In questo caso, l'utilizzo di un nodo esterno in clearnet, come Luna Node, è preferibile. Ciò offre maggiore flessibilità e consente un'integrazione più fluida con la vostra piattaforma di commercio online.

Per coloro che cercano una soluzione tutto-in-uno e facile da gestire, OpenNode è un'ottima opzione. Tuttavia, la sua configurazione e il suo utilizzo possono essere abbastanza complessi. Ecco perché prevediamo di coprire questa soluzione in modo più dettagliato in una formazione dedicata a parte.

Di seguito troverete i link ai diversi servizi menzionati:

- [OpenNode](https://www.opennode.com/)
- [BTCPay Server](https://btcpayserver.org/)
- [Luna Node](https://www.lunanode.com/) e la guida su [BTCPay Server con Luna Node](https://docs.btcpayserver.org/Deployment/LunaNode/)

Inoltre, ho avuto l'opportunità di intervistare Nicolas Dorier, il creatore di BTCPay Server. Se siete interessati, non esitate a guardare la nostra conversazione cliccando [qui](https://www.youtube.com/watch?v=XR6qB76hCL0&pp=ygUoaW50ZXJ2aWV3IG5pY29sYSBkb3JpZXIgZGVjb3V2cmUgYml0Y29pbg%3D%3D). Scoprirete molte informazioni interessanti e preziosi consigli per ottimizzare l'utilizzo di BTCPay Server nella vostra attività commerciale.

In sintesi, l'accettazione di Bitcoin può offrire una moltitudine di vantaggi per la vostra attività commerciale. Che siate un ristorante locale o un e-commerce globale, esiste una soluzione adatta alle vostre esigenze. Prendetevi il tempo di esaminare le diverse opzioni e non esitate a lanciarvi in questa nuova avventura Bitcoin.

# Riassunto della formazione

![conclusion](https://youtu.be/QrKbagtUE1s)
Eccoci giunti alla conclusione della nostra approfondita esplorazione della rete Lightning di Bitcoin. Abbiamo percorso un cammino complesso, popolato di innovazioni tecnologiche e di nuove prospettive su come interagiamo con il nostro denaro digitale. Dall'esplorazione iniziale di Umbrel all'apertura e alla gestione dei canali Lightning, ogni passo è stato un passo verso una migliore comprensione e una maggiore padronanza di questa tecnologia rivoluzionaria.

Abbiamo iniziato con una panoramica di Umbrel, familiarizzando con l'interfaccia e le funzionalità chiave. Successivamente, ci siamo immersi nella Mempool, imparando ad analizzare le transazioni in attesa per una visione più approfondita della rete Bitcoin. Poi, abbiamo esplorato gli esploratori di blocchi e le statistiche di rete, strumenti essenziali per monitorare lo stato della rete.

Abbiamo poi affrontato l'aspetto più personale della rete Bitcoin: il portafoglio. Abbiamo imparato a collegare il nostro portafoglio al nostro nodo, poi abbiamo scoperto l'importanza e la sicurezza dei portafogli multisig grazie a Specter.

Successivamente, ci siamo immersi nell'universo della rete Lightning. Abbiamo esplorato l'apertura dei canali Lightning e la loro gestione, due aspetti cruciali per un funzionamento ottimale del nostro nodo. Abbiamo anche imparato a rinominare il nostro nodo per facilitarne l'identificazione sulla rete.

Abbiamo anche avuto una visione divertente dell'utilizzo della Lightning Network grazie a Satoshi's Place, un esempio concreto di come la LN possa essere utilizzata per micro-transazioni a basso costo.

Infine, abbiamo affrontato l'aspetto commerciale di Bitcoin. Abbiamo esplorato come accettare Bitcoin nel proprio commercio tramite BTCpay server, tenendo conto di diverse configurazioni in base alle esigenze.

Detto questo, padroneggiare la rete Lightning non è un compito che si fa in un giorno. Si tratta di una tecnologia in costante evoluzione, complessa e sfumata. Ci vorrà tempo, pratica e una volontà di imparare per padroneggiare veramente questo strumento. Proprio come Bitcoin stesso, la Lightning Network è un'avventura, un'esplorazione di ciò che è possibile nel campo della finanza digitale. Ma con pazienza, perseveranza e una volontà di apprendere, presto sarete in grado di navigare nella rete Lightning con facilità e fiducia.

In sintesi, il viaggio che abbiamo intrapreso insieme attraverso la rete Lightning è solo l'inizio. La padronanza di questa tecnologia offre molte opportunità e vantaggi. Quindi continuate ad esplorare, imparare e sperimentare con la Lightning Network. Il futuro della finanza è a portata di mano.
Per concludere, è importante sottolineare che questa formazione, così come le altre che proponiamo, è completamente gratuita. Crediamo fermamente nell'importanza di condividere la conoscenza e rendere l'accesso alle informazioni il più libero e aperto possibile. È in questo spirito che abbiamo deciso di condividere con voi tutto ciò che abbiamo imparato sulla rete Lightning.

Tuttavia, se hai trovato valore in questa formazione e desideri sostenerci, ti invitiamo a visitare il nostro sito di e-commerce all'indirizzo seguente: https://thebitcoinrabbithole.myshopify.com/. Effettuando acquisti sul nostro sito, contribuirai non solo a sostenere il nostro lavoro, ma ci aiuterai anche a continuare a fornire formazioni gratuite e di alta qualità.

Grazie per aver dedicato del tempo a seguire questa formazione. Il tuo sostegno e il tuo interesse per il nostro lavoro significano molto per noi.

# Ringraziamenti e continua a scavare la tana del coniglio

Congratulazioni per aver completato questa formazione LN 202! Spero sinceramente che ti sia piaciuta e abbia aperto nuove porte. La tua scoperta del bitcoin è solo all'inizio e ti invito a scoprire tutte le altre formazioni disponibili nell'università.

- ECON 201 affronterà l'economia austriaca
- SECU 101 ti permetterà di aggiornare la tua sicurezza
- MINAGE 201 per saperne di più sull'estrazione
- (e molti altri)

Baci e a presto!
