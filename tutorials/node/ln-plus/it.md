---
name: Lightning Network+
description: Ottenere liquidità in entrata gratuita con aperture di cooperative sul proprio nodo Lightning
---

![cover](assets/cover.webp)



## Introduzione



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) è una piattaforma comunitaria progettata per facilitare la cooperazione tra gli operatori dei nodi Lightning Network. Il suo obiettivo principale è migliorare la connettività e la liquidità della rete Lightning, senza bisogno di intermediari centralizzati. Il suo obiettivo principale è migliorare la connettività, la liquidità e la decentralizzazione della rete Lightning, senza la necessità di intermediari centralizzati.



Questo tutorial si concentrerà sul servizio **"Swaps "**, che è la funzione più utilizzata e strutturante di LN+ oggi. Verranno inoltre presentati gli altri servizi offerti dalla piattaforma.



## Panoramica del LN



### Che cos'è il Lightning Network Plus?



Lightning Network Plus (LN+) è una piattaforma comunitaria per gli operatori di nodi Lightning che desiderano collaborare direttamente e volontariamente. Il suo obiettivo è quello di facilitare la creazione di canali Lightning utili, equilibrati e sostenibili, evitando la necessità di soluzioni centralizzate o di hub imposti.



Il LN+ si basa su un principio fondamentale: la cooperazione tra pari, fondata su trasparenza, reciprocità e reputazione.



### I servizi LN+ in sintesi



LN+ offre diversi servizi progettati per migliorare la topologia e la liquidità della rete Lightning, tra cui :





- Swap**: apertura reciproca di canali tra operatori (servizio principale).
- Anelli**: aperture di canali circolari tra più partecipanti.
- Swap basati sulla fiducia**: varianti che si basano maggiormente sulla fiducia e sulla storia dei partecipanti.
- Caratteristiche sociali**: profili, commenti e sistema di reputazione.



Nel resto di questa guida, ci concentreremo esclusivamente sul servizio **Swaps**, che è il cuore dell'attuale utilizzo di LN+.



## Servizio "swap" LN+



### Definizione di uno swap LN+



Uno **scambio** LN+ è un accordo volontario tra due operatori di nodi Lightning per aprire reciprocamente canali Lightning di capacità equivalente (o preconcordata). A differenza dell'apertura unilaterale di un canale convenzionale, lo swap si basa su una **reciprocità esplicita**.



In pratica :





- Si apre un canale verso il nodo del partner.
- Il vostro partner apre un canale verso il vostro nodo.
- Entrambe le parti stanno vincolando una quantità simile di on-chain bitcoin.



### Qual è lo scopo degli swap per gli operatori dei nodi?



Il servizio Swaps affronta diversi problemi chiave incontrati dagli operatori di Lightning:





- Connettività migliorata**: creazione di canali bidirezionali utili non appena vengono aperti.
- Migliore gestione della liquidità**: ogni parte dispone di capacità in entrata e in uscita.
- Riduzione del rischio di canali inutili**: il partner è incoraggiato a mantenere aperto il canale.
- Maggiore decentramento**: connessioni dirette tra gli operatori, senza hub imposti.



### Per quali profili di nodo è utile lo swap?



Gli swap sono particolarmente utili per :





- Nuovi nodi che desiderano migliorare rapidamente la loro instradabilità.
- Operatori intermediari che cercano di aumentare la densità del loro grafico di canale.
- Nodi orientati all'instradamento che vogliono ottimizzare la loro topologia.



## Collegare il nodo Lightning al LN+



### Requisiti tecnici



Prima di iniziare, è necessario :





- Un nodo Lightning funzionante (LND, Core Lightning o Eclair).
- Accesso all'interfaccia di gestione del nodo.
- Capacità on-chain sufficiente per aprire i canali.



Accedere al sito web di [Lightning Network](https://lightningnetwork.plus/) Plus e fare clic sul pulsante `Login` in alto a destra dell'interfaccia.



![capture](assets/fr/03.webp)



### Autenticazione tramite firma del messaggio



Per autenticarsi, è necessario firmare il messaggio fornito utilizzando la chiave privata del proprio nodo Lightning. Con ThunderHub, questa operazione è molto semplice.



Iniziare copiando il messaggio visualizzato dal LN+.



![capture](assets/fr/04.webp)



In ThunderHub, andare alla scheda `Strumenti`, quindi fare clic sul pulsante `Firma` nella sezione `Messaggi`.



![capture](assets/fr/05.webp)



Incollare il messaggio di autenticazione fornito da LN+, quindi fare clic su "Firma".



![capture](assets/fr/06.webp)



Il ThunderHub firma il messaggio usando la chiave privata del nodo. Copiare la firma generata.



![capture](assets/fr/07.webp)



Incollare questa firma nel campo corrispondente del sito LN+, quindi fare clic su "Accedi".



![capture](assets/fr/08.webp)



Ora siete connessi a LN+ con il vostro nodo Lightning. Questo processo consente a LN+ di verificare che siate i legittimi proprietari del nodo che dichiarate sulla loro piattaforma.



![capture](assets/fr/09.webp)



Se lo desiderate, potete personalizzare il vostro profilo LN+, ad esempio aggiungendo una breve biografia.



## Partecipare a uno swap esistente



### Accesso alle offerte di scambio



Per partecipare all'apertura del vostro primo canale, accedete al menu `Swaps` nella parte superiore dell'interfaccia. Qui troverete tutti gli swap attualmente disponibili, a seconda delle caratteristiche del vostro nodo.



![capture](assets/fr/10.webp)



### Condizioni di ammissibilità



Per aderire a un'offerta di scambio esistente, è sufficiente selezionare l'annuncio corrispondente e registrarsi. Tuttavia, LN+ consente al creatore dello swap di definire alcune **condizioni di ammissibilità**, quali :





- un numero minimo di canali già aperti ;
- capacità totale minima del nodo ;
- alcuni tipi di connessione accettati.



### Nodi recenti



Di conseguenza, soprattutto nelle prime fasi di utilizzo, è possibile che **poche o nessuna offerta sia disponibile** per il vostro nodo. Questa è una situazione comune per i nuovi nodi o per quelli non ancora connessi.



Nel mio caso, nonostante l'esistenza di alcuni canali aperti, nessuna delle offerte soddisfaceva i criteri richiesti.



## Create la vostra offerta di scambio



### Quando è opportuno creare il proprio swap?



Quando non è disponibile un'offerta esistente, la creazione di un proprio swap è spesso la soluzione migliore. Inoltre, vi permette di mantenere il controllo sui parametri dello swap.



### Configurazione di scambio



Fare clic su **Avvia Liquidity Swap**, quindi configurare i parametri dell'offerta:





- selezionare il numero totale di partecipanti (3, 4 o 5);
- indicano la capacità dei canali da aprire;
- definire il periodo di impegno durante il quale i partecipanti si impegnano a non chiudere i propri canali;
- specificare eventuali restrizioni applicabili ai partecipanti (numero minimo di canali, capacità totale minima, tipo di connessione accettata).



![capture](assets/fr/11.webp)



### Pubblicazione e aspettative dei partecipanti



Una volta inseriti tutti i parametri, cliccate su **Avvia Liquidity Swap** per pubblicare la vostra offerta. Ora non resta che aspettare che altri operatori si iscrivano.



![capture](assets/fr/12.webp)



## Finalizzazione di uno scambio



### Apertura effettiva del canale



Ora che tutte le posizioni di scambio sono state prese, ogni partecipante può vedere, dalla sua interfaccia LN+, quale nodo deve aprire un canale Lightning.



![capture](assets/fr/13.webp)



Da parte vostra, aprite il canale utilizzando l'ID del nodo fornito da LN+ e rispettando la quantità indicata. Questa operazione può essere effettuata tramite ThunderHub, un altro gestore di nodi Lightning o direttamente tramite l'interfaccia di base del nodo.



![capture](assets/fr/14.webp)



Una volta aperto, il canale appare nella sezione dei canali in attesa.



![capture](assets/fr/15.webp)



### Conferma in LN+



Tornare quindi al LN+ per confermare l'apertura del canale, facendo clic sul pulsante "Apertura del canale avviata".



![capture](assets/fr/16.webp)



### Fine dello scambio



Quando tutti i partecipanti hanno aperto i canali per i quali si sono impegnati, lo swap è considerato completo.



## Reputazione e buone pratiche di comunicazione



### Il sistema di reputazione LN+



LN+ incorpora un sistema di reputazione basato sulle opinioni lasciate dai partecipanti al termine degli swap. Queste opinioni sono pubbliche e influenzano direttamente la capacità di un operatore di partecipare o creare futuri swap.



![capture](assets/fr/17.webp)



### Migliori pratiche consigliate



Al fine di preservare una buona reputazione e garantire il regolare svolgimento degli swap, si raccomanda di :





- rispettare le scadenze di apertura dei canali ;
- comunicare rapidamente in caso di problemi o ritardi;
- utilizzare la sezione commenti per scambiare opinioni con gli altri partecipanti;
- non chiudere un canale prima della fine del periodo di impegno.




![capture](assets/fr/18.webp)



### Perché la reputazione è fondamentale per LN+



LN+ si basa su un modello di cooperazione volontaria, senza forti vincoli tecnici. La reputazione è quindi il principale incentivo per garantire l'affidabilità e la serietà dei partecipanti.



## Altri servizi LN+



Oltre agli swap, LN+ offre altri servizi progettati per migliorare la connettività e il coordinamento tra gli operatori dei nodi Lightning. Gli anelli** consentono a più partecipanti di creare un anello di aperture di canali, rafforzando così la ridondanza dei percorsi di instradamento e la densità del grafo Lightning. Gli swap** basati sulla fiducia si basano su principi simili a quelli degli swap classici, ma offrono una maggiore flessibilità ai partecipanti che hanno già una reputazione consolidata sulla piattaforma.



LN+ integra anche funzioni sociali come i profili pubblici dei nodi, i commenti di scambio e un sistema di reputazione. Questi strumenti non sono servizi tecnici in sé, ma svolgono un ruolo centrale nel buon funzionamento della piattaforma, facilitando la comunicazione, il coordinamento e la fiducia tra gli operatori.



## Conclusione



Il servizio Swaps di LN+ è uno strumento efficace per migliorare la connettività, la liquidità e la decentralizzazione della rete Lightning. Promuovendo l'apertura reciproca e coordinata dei canali, LN+ consente agli operatori dei nodi di rafforzare la propria topologia, promuovendo al contempo una cooperazione responsabile e decentralizzata.