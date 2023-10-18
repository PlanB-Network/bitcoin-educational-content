name: Introduzione al Mining di Bitcoin
goal: Comprendere il funzionamento dell'industria del mining attraverso un esercizio pratico di riutilizzo degli ASIC.
objectives:
  - Comprendere la teoria del mining
  - Comprendere l'industria del mining
  - Trasformare un S9 in un riscaldamento
  - Estrarre il primo satoshi

# I tuoi primi passi nel mining!

In questo corso, approfondiremo l'industria del mining per svelare i segreti di questo argomento così complesso! Il corso è accessibile a tutti e non richiede un investimento iniziale.

La prima sezione sarà teorica, in cui avremo una discussione approfondita con Ajelex su vari argomenti legati al mining. Ciò ci permetterà di comprendere meglio questa industria e le sfide economiche e geopolitiche ad essa legate.
Nella seconda sezione, affronteremo un caso pratico. Infatti, impareremo a trasformare un vecchio minatore S9 in un riscaldamento ausiliario per la casa! Attraverso guide scritte e video, vi mostreremo e spiegheremo tutti i passaggi necessari per realizzarlo a casa vostra :)

Speriamo che questo video vi mostri come l'industria del mining sia più complessa di quanto sembri e che lo studio di essa permetta di sfumare il dibattito ecologico ad essa legato!
Se avete bisogno di aiuto per il vostro progetto, è stato creato un gruppo Telegram per gli studenti e tutti i componenti necessari possono essere trovati sul nostro e-commerce!

+++

# Introduzione

## Benvenuti!

Benvenuti in MINING 201: un'introduzione al mining. Ajelex, Jim & Rogzy sono felici di accompagnarvi nei vostri primi passi concreti in questa nuova industria. Speriamo che il corso vi piaccia e che vi uniate all'avventura del mining casalingo!

### Panoramica del corso

In questo corso, la prima sezione sarà dedicata alla teoria del mining con Ajelex. Discuteremo approfonditamente dei vari argomenti legati al mining, il che ci permetterà di comprendere meglio questa industria e le sfide economiche e geopolitiche ad essa legate.

Nella seconda sezione, ci immergeremo in un affascinante caso pratico, imparando a trasformare un vecchio minatore S9 in un riscaldamento ausiliario per la casa. Grazie a guide scritte e video, tutti i passaggi necessari saranno spiegati in dettaglio, garantendo il successo del vostro progetto innovativo.

Questo viaggio di apprendimento vi mostrerà che l'industria del mining è più complessa di quanto sembri, offrendo una prospettiva equilibrata sul dibattito ecologico ad essa legato. Un supporto continuo sarà disponibile tramite un gruppo Telegram dedicato agli studenti e tutti i componenti necessari saranno facilmente accessibili sulla nostra piattaforma di e-commerce.

### Curriculum:

Sezione Teorica:
* Spiegazione del mining.
* L'industria del mining.
* Le sfumature dell'industria del mining.
* Il mining nel protocollo bitcoin.
* Prezzo del bitcoin e hashrate, una correlazione? Sovranità e regolamentazione
* Intervista a un professionista dell'industria del mining

Sezione Pratica: Attakai
* Introduzione ad Attakai.
* Guida all'acquisto.
* Modifica del software di un Antminer S9.
* Sostituzione delle ventole per ridurre il rumore.
* Configurazione di un pool.
* Configurazione di un Antminer S9 con Braiins OS+.

Pronti per iniziare questa avventura affascinante? Tuffiamoci insieme nel mondo affascinante del mining casalingo!

# Conoscere tutto sul mining

## Spiegazione del mining

![Cos'è il mining di bitcoin?](https://www.youtube.com/watch?v=neEQzEQzmPQ)

### Il Mining Spiegato: L'Analogia del Puzzle

Per spiegare in modo semplificato il concetto di mining, si può utilizzare un'analogia pertinente: quella del puzzle. Come un puzzle, il mining è un compito complesso da completare, ma facile da verificare una volta completato. Nel contesto del mining di Bitcoin, i minatori cercano di risolvere rapidamente un puzzle digitale. Il primo minatore a risolvere il puzzle presenta la sua soluzione all'intera rete, che può quindi verificarne facilmente la validità. Questa verifica di successo consente al minatore di convalidare un nuovo blocco e aggiungerlo alla blockchain di Bitcoin. In riconoscimento del loro lavoro, che comporta costi significativi, il minatore viene ricompensato con un certo numero di bitcoin. Questa ricompensa costituisce un incentivo finanziario per i minatori a continuare il loro lavoro di convalida delle transazioni e di sicurezza della rete Bitcoin.

![immagine](assets/overview/puzzle.png)

Inizialmente nella rete Bitcoin, la ricompensa assegnata era di 50 bitcoin ogni dieci minuti, parallelamente alla scoperta di un blocco ogni dieci minuti in media da parte dei minatori. Questa ricompensa subisce una divisione per due ogni 210.000 blocchi, ovvero approssimativamente ogni quattro anni. Questa remunerazione serve come potente incentivo per incoraggiare i minatori a partecipare al processo di mining nonostante il suo costo energetico. In assenza di ricompensa, il mining, costoso in termini di elettricità, verrebbe abbandonato, compromettendo così la sicurezza e la stabilità dell'intera rete Bitcoin.
La ricompensa attuale per il mining è doppia. Da un lato, include la creazione di nuovi bitcoin, passati da 50 bitcoin ogni dieci minuti inizialmente a 6,25 bitcoin oggi (2023). Dall'altro lato, include le commissioni di transazione, o commissioni di mining, delle transazioni che il minatore sceglie di includere nel suo blocco. Quando viene effettuata una transazione bitcoin, vengono pagate delle commissioni di transazione. Queste commissioni funzionano come una sorta di asta in cui gli utenti indicano quanto sono disposti a pagare affinché la loro transazione venga inclusa nel blocco successivo. Per massimizzare la loro ricompensa, i minatori, agendo nel loro interesse personale, selezionano le transazioni più redditizie da includere nel loro blocco, tenendo conto dello spazio limitato disponibile. Pertanto, la ricompensa per il mining è composta sia dalla generazione di nuovi bitcoin che dalle commissioni di transazione, garantendo un incentivo continuo per i minatori e assicurando la durata e la sicurezza della rete Bitcoin.
### I Minatori e i Loro Strumenti: L'Estrazione

Il processo di mining consiste nel trovare un hash valido accettabile dalla rete Bitcoin. Questo hash, una volta calcolato e trovato, è irreversibile, come le patate trasformate in purè. Verifica una determinata funzione senza possibilità di tornare indietro. I minatori, in competizione, utilizzano macchine per calcolare questi hash. Sebbene teoricamente sia possibile trovare questo hash manualmente, la complessità dell'operazione rende questa opzione impraticabile. Pertanto, vengono utilizzati computer in grado di eseguire rapidamente questi calcoli, anche se consumano una quantità significativa di elettricità.

All'inizio, dominava l'era della CPU, in cui i minatori utilizzavano i loro computer personali per il mining di Bitcoin. La scoperta dei vantaggi delle GPU (schede grafiche) per questo compito ha segnato una svolta, aumentando in modo significativo l'hashrate e riducendo il consumo di energia. Il progresso non si è fermato qui, con l'introduzione successiva degli FPGA (field-programmable gate array / array di porte programmabili in campo). Gli FPGA hanno servito come piattaforma per lo sviluppo degli ASIC (application-specific integrated circuit / circuito integrato specifico per un'applicazione).

![image](assets/overview/chip.png)

Gli ASIC sono chip, simili al chip di una CPU, ma sono sviluppati per eseguire un solo tipo di calcolo specifico nel modo più efficiente possibile. In altre parole, una CPU è in grado di eseguire una moltitudine di tipi di calcoli diversi senza essere particolarmente ottimizzata per un tipo di calcolo o un altro, mentre un ASIC sarà in grado di eseguire un solo tipo di calcolo, ma in modo molto efficiente. Nel caso specifico, gli ASIC Bitcoin sono progettati per il calcolo dell'algoritmo SHA256.
Oggi, i minatori utilizzano esclusivamente ASIC dedicati a questa operazione, ottimizzati per testare il numero massimo di combinazioni con il consumo di energia più basso possibile e nel minor tempo possibile. Questi computer, incapaci di eseguire compiti diversi dal mining di Bitcoin, sono una testimonianza tangibile dell'evoluzione continua e della crescente specializzazione dell'industria del mining di Bitcoin. Questa costante evoluzione riflette la dinamica intrinseca di Bitcoin, in cui un'ajustement de la difficulté garantisce la produzione di un blocco ogni dieci minuti nonostante l'aumento esponenziale della capacità di mining.

Per illustrare l'intensità di questo processo, considera un minatore tipico in grado di eseguire 14 TeraHash al secondo, ovvero 14.000 miliardi di tentativi al secondo per trovare l'hash corretto. A livello della rete Bitcoin, si raggiungono attualmente circa 300 HexaHash al secondo, evidenziando la potenza collettiva impiegata nel mining di Bitcoin.

### Ajustement de la difficulté:

L'ajustement de la difficulté è un meccanismo cruciale nel funzionamento della rete Bitcoin, garantendo che i blocchi vengano minati in media ogni 10 minuti. Questa durata è una media, poiché il processo di mining è in realtà un gioco di probabilità, simile al lancio di dadi nella speranza di ottenere un numero inferiore al numero definito dalla difficoltà. Ogni 2016 blocchi, la rete regola la difficoltà di mining in base al tempo medio necessario per minare i blocchi precedenti. Se il tempo medio è superiore a 10 minuti, la difficoltà viene ridotta, e viceversa se il tempo medio è inferiore, la difficoltà viene aumentata. Questo meccanismo di ajustement assicura che il tempo di mining dei nuovi blocchi rimanga costante nel tempo, indipendentemente dal numero di minatori o dalla potenza di calcolo complessiva della rete. È per questa ragione che la Blockchain di Bitcoin viene anche chiamata Timechain.

![image](assets/overview/chinaban.png)

* Esempio della Cina:
Il caso della Cina illustra perfettamente questo meccanismo di regolazione della difficoltà, ricca di energia abbondante e a basso costo, era il principale hub mondiale per il mining di Bitcoin. Nel 2021, il paese ha improvvisamente vietato il mining di Bitcoin sul suo territorio, causando una massiccia caduta del tasso di hash globale della rete Bitcoin, dell'ordine del 50%. Questa rapida diminuzione della potenza di mining avrebbe potuto gravemente disturbare la rete Bitcoin, aumentando il tempo medio di mining dei blocchi. Tuttavia, è intervenuto il meccanismo di regolazione della difficoltà, riducendo la difficoltà di mining per garantire che la frequenza di mining dei blocchi rimanga in media di 10 minuti. Questo caso dimostra l'efficienza e la resilienza del meccanismo di regolazione della difficoltà di Bitcoin, che assicura la stabilità e la prevedibilità della rete, anche in caso di cambiamenti improvvisi e significativi nel panorama del mining globale.
### Evoluzione delle Macchine per il Mining di Bitcoin

Per quanto riguarda l'evoluzione delle macchine per il mining di Bitcoin, è importante sottolineare che il contesto è più orientato verso un modello di business tradizionale. I minatori guadagnano dalla validazione dei blocchi, un compito con una probabilità di successo relativamente bassa. Il modello di macchina attualmente in uso, l'Antminer S9, anche se è un modello più vecchio lanciato intorno al 2016, rimane in circolazione sul mercato dell'usato, negoziato a circa 100€ - 200€. Tuttavia, il prezzo delle macchine per il mining varia in base al valore di Bitcoin, e un modello più recente, l'Antminer S19, è attualmente stimato intorno ai 3000€.

Di fronte all'evoluzione tecnologica costante nel campo del mining, i professionisti devono posizionarsi strategicamente. L'industria del mining è soggetta a continue innovazioni, come dimostra il recente lancio della versione J del S19, e l'attesa del S19 XP, che offrirà capacità di mining nettamente superiori. Inoltre, i miglioramenti non sono solo legati alle prestazioni grezze delle macchine. Ad esempio, il nuovo modello S19 XP utilizza un sistema di raffreddamento a liquido, una modifica tecnica che consente un miglioramento significativo dell'efficienza energetica. Sebbene l'innovazione rimanga una costante, i futuri guadagni di efficienza saranno probabilmente inferiori rispetto a quelli finora osservati, a causa del raggiungimento di una certa soglia di innovazione tecnologica.

![image](assets/overview/chipevolution.png)
In conclusione, l'industria del mining di Bitcoin continua ad adattarsi e svilupparsi, e gli attori del settore devono anticipare guadagni di efficienza sempre più limitati in futuro e adeguare di conseguenza le loro strategie. Gli sviluppi tecnologici futuri, sebbene ancora presenti, probabilmente avverranno su una scala più ridotta, riflettendo una crescente maturità del settore.
## L'industria del mining

![Il mining di Bitcoin troppo centralizzato? Rischi e soluzioni](https://www.youtube.com/watch?v=xkiY8DgkcLQ)

### I pool di mining

Attualmente, il mining di Bitcoin si è evoluto in un'industria seria e sostanziale, con molti attori ormai pubblici e un numero crescente di minatori significativi. Questa evoluzione ha reso il mining quasi inaccessibile per i piccoli attori a causa del costo elevato associato all'acquisizione di nuove macchine da mining. Pertanto, sorge la questione della distribuzione dell'hashrate tra diversi attori del mercato. La situazione è complessa, poiché è essenziale esaminare sia la distribuzione dell'hashrate tra diverse società che tra diversi pool di mining.

![immagine](assets/overview/pool.png)

Un pool di mining è un gruppo di minatori che uniscono le loro risorse di calcolo per aumentare le loro possibilità di mining. Questa cooperazione è necessaria perché una piccola macchina da mining isolata è in competizione con i giganti dell'industria, riducendo le sue possibilità di successo a un livello trascurabile. Il mining funziona secondo un principio di lotteria, e le possibilità di vincere un blocco (e quindi la ricompensa in Bitcoin) ogni dieci minuti sono estremamente basse per un piccolo minatore individuale. Unendosi in pool, i minatori possono combinare la loro potenza di calcolo, trovare blocchi più frequentemente e poi distribuire le ricompense in modo proporzionale al contributo di ciascun minatore al pool.

Ad esempio, se un pool trova un blocco e vince 6,25 bitcoin, un minatore che contribuisce all'1% della potenza di calcolo totale del pool riceverebbe l'1% dei 6,25 bitcoin vinti. Tuttavia, è importante notare che i pool di mining di solito prendono una piccola commissione (di solito intorno al 2%) per coprire i costi operativi della cooperativa.

### I software utilizzati dall'industria

Nel contesto del mining di Bitcoin, il ruolo del software è altrettanto cruciale quanto l'hardware. Un esempio di ciò è illustrato dal ruolo di Bitmain, un produttore prolifico che ha sviluppato l'Antminer S9. Oltre all'hardware di mining, l'industria si basa fortemente sui pool di mining collaborativi, come Brainspool, che controlla circa il 5% dell'hashrate globale della rete Bitcoin.
Gli attori di questa industria cercano costantemente di aumentare l'efficienza attraverso l'hardware e il software. Ad esempio, un software popolare utilizzato in questo contesto è BrainsOS Plus. Questo software sostituisce il sistema operativo originale della macchina di mining, consentendo di eseguire le stesse operazioni in modo più efficiente. Con un tale software, un minatore può aumentare l'efficienza della sua macchina del 25%. Ciò significa che con la stessa quantità di elettricità, la macchina può produrre un hash rate aggiuntivo del 25%, aumentando così le ricompense ricevute dal minatore. Questa ottimizzazione del software è un elemento essenziale per la competitività nel mining di Bitcoin, dimostrando l'importanza di un approccio integrato che combini miglioramenti hardware e software per massimizzare l'efficienza e i rendimenti.
### La regolamentazione e il costo dell'elettricità

Come osservato in Cina e altrove, la regolamentazione influisce notevolmente sul mining. Sebbene non ci siano importanti minatori in Francia, la regolamentazione e i costi elevati dell'elettricità in Europa costituiscono ostacoli significativi. I minatori sono costantemente alla ricerca di elettricità a basso costo per massimizzare i loro guadagni. Pertanto, il costo elevato dell'elettricità in Europa e in Francia non favorisce l'attrazione dei minatori in queste regioni.

I minatori tendono a dirigere le loro attività verso regioni con tariffe elettriche basse, spesso in paesi emergenti o paesi con surplus energetici. Ad esempio, una grande parte dell'hash rate mondiale si trova in Texas, negli Stati Uniti. Il Texas ha una rete elettrica indipendente che non condivide le sue risorse energetiche con gli altri stati. Questa particolarità obbliga il Texas a produrre spesso più elettricità di quanto necessario per evitare carenze, creando così un surplus. I minatori di Bitcoin approfittano di questa sovrapproduzione stabilendosi in Texas, dove possono estrarre Bitcoin a tariffe elettriche molto basse durante i periodi di surplus energetico. Questa situazione dimostra l'influenza significativa della regolamentazione e dei costi dell'elettricità sul mining di Bitcoin, sottolineando l'importanza di questi fattori nella decisione dei minatori sulla posizione delle loro operazioni di mining.

### Dove vanno i minatori e la gestione dell'energia?

Sottolineando l'impatto dei minatori di Bitcoin nel mondo dell'energia, la tendenza è chiara: questi attori sono costantemente alla ricerca di fonti di elettricità a basso costo, spesso quelle che vengono sprecate o non sfruttate. Questo fenomeno è evidente nelle regioni con nuove infrastrutture elettriche, come quelle dotate di recenti dighe idroelettriche.
Prendiamo un esempio. In un paese in cui è in corso la costruzione di una diga, la produzione di elettricità spesso inizia prima che le linee di distribuzione siano completamente operative. Questo divario può comportare costi considerevoli e scoraggiare gli investimenti in progetti di infrastrutture simili. Tuttavia, i minatori di bitcoin possono agire come una fonte di domanda flessibile, pronti a consumare questa "elettricità orfana", contribuendo così ad ammortizzare i costi delle infrastrutture. L'implicazione qui è che è possibile rendere redditizie immediatamente nuove installazioni, favorendo la creazione di nuove fonti di elettricità. Questo principio si applica anche a scale più piccole. Che si tratti di un individuo che utilizza una centrale idroelettrica su un piccolo fiume o di una casa dotata di pannelli solari, l'eccesso di elettricità prodotta può essere utilizzato per alimentare un'operazione di mining di bitcoin.

In Francia, ad esempio, gli eccessi di elettricità dai pannelli solari vengono reiniettati nella rete e i produttori vengono remunerati con un credito di consumo da parte di EDF. In modo simile, si può immaginare un minatore che opera su questi eccessi di elettricità, spegnendosi quando la domanda locale eguaglia l'offerta. Sebbene possa sembrare egoistico, privilegiare la produzione di bitcoin anziché sostenere la rete elettrica locale, presenta un altro punto di vista: la stabilizzazione della rete elettrica. La complessa gestione degli eccessi di elettricità, talvolta con costi associati alla loro eliminazione, può essere notevolmente semplificata. I minatori di bitcoin possono assorbire questi eccessi, agendo come un cuscinetto flessibile, regolando la domanda anziché l'offerta. In un mondo in cui la produzione di elettricità da fonti rinnovabili (poco pilotabili) è in costante aumento, i minatori possono svolgere un ruolo chiave nel garantire l'equilibrio delle nostre reti elettriche, beneficiando allo stesso tempo dell'elettricità a buon mercato o in eccesso per alimentare le loro operazioni di mining.

### La centralizzazione del mining

La centralizzazione del mining viene affrontata come una sfida significativa. Grandi attori, come Foundry, dominano il mercato, il che potrebbe potenzialmente portare alla censura delle transazioni. Questa centralizzazione può anche rendere la rete vulnerabile ad attacchi, in particolare l'attacco del 51%, in cui un attore o un gruppo controlla più del 50% della potenza di hash della rete, consentendo loro di controllare e manipolare la rete.
Rischio di regolamentazione. Si sottolinea che se un paese come gli Stati Uniti decidesse di regolamentare o vietare alcune transazioni Bitcoin, ciò potrebbe avere un impatto significativo sulla rete, soprattutto se una grande parte della potenza di hash è centralizzata in quel paese.

![image](assets/overview/foundry.png)

Per contrastare questa centralizzazione, vengono affrontate diverse strategie:
Le principe de Attakai est de permettre aux mineurs de crypto-monnaies d'utiliser la chaleur générée par leurs équipements de minage pour chauffer leur domicile. Cela permet de réduire les coûts de chauffage tout en contribuant à la sécurité et à la décentralisation du réseau Bitcoin.

### Les avantages du Home Mining

Le Home Mining présente plusieurs avantages. Tout d'abord, il permet une distribution plus large du hashrate en encourageant les individus à participer à l'activité de minage depuis leur domicile. Cela réduit la concentration du pouvoir entre les mains de grandes pools de minage et renforce la résistance à la censure.

De plus, le Home Mining contribue à la décentralisation du réseau en diversifiant les acteurs et la géographie du minage. En encourageant la participation de mineurs de différentes régions géographiques, il devient plus difficile pour un seul acteur ou pays d'exercer un contrôle ou une influence disproportionnée sur le réseau.

### Le protocole Stratum V2

Le protocole Stratum V2 offre une approche différente pour renforcer la décentralisation du réseau Bitcoin. Contrairement à son prédécesseur, Stratum V2 permet aux mineurs de choisir les transactions à inclure dans les blocs qu'ils minent. Cela donne plus de pouvoir aux mineurs individuels et diminue la capacité des grandes pools de minage à dominer le réseau. Ainsi, Stratum V2 joue un rôle déterminant dans la lutte contre la centralisation du hashrate.

### L'open-sourcing des logiciels de minage

Une autre stratégie pour favoriser la décentralisation est l'open-sourcing des logiciels de minage. En rendant ces logiciels accessibles à tous, les petits mineurs ont les mêmes opportunités que les grandes entreprises de minage pour participer et contribuer au réseau de blockchain. Cela encourage une distribution plus large du hashrate et contribue à la décentralisation du réseau.

### Conclusion

En conclusion, la décentralisation est cruciale pour la sécurité et la résilience du réseau Bitcoin. Des initiatives telles que Attakai, l'adoption du protocole Stratum V2 et l'open-sourcing des logiciels de minage sont des étapes importantes vers la décentralisation et la protection du réseau contre les risques de censure et d'attaques des 51%.
Nel contesto attuale, la pratica del mining di Bitcoin con S9 può sembrare complessa, ma un'analisi più approfondita apre la strada a alternative innovative. Il principio di Attakai si basa su una riflessione sull'uso delle strutture di mining in diversi tipi di edifici, come scuole o ospedali. L'idea principale è quella di posizionare alcune macchine di mining in vari luoghi, consentendo così di riutilizzare il calore emesso da queste macchine per riscaldare gli edifici. Optando per modelli più performanti come gli S19, sarebbe possibile distribuire l'attività di mining, favorendo una migliore performance complessiva e contribuendo utilmente alla società. Questa iniziativa mirerebbe a competere con le grandi strutture di mining centralizzate utilizzando il calore generato dalle macchine di mining in modo produttivo ed efficiente.

L'iniziativa Attakai deriva da un'esperienza personale di mining casalingo, realizzata da due amici desiderosi di partecipare attivamente alla rete Bitcoin. Hanno incontrato ostacoli significativi, come il livello di rumore elevato delle attrezzature di mining, progettate per un uso industriale e non domestico. Per ovviare a questo problema, sono state apportate modifiche hardware alle macchine di mining. Ventole più performanti e silenziose hanno sostituito le attrezzature originali, rendendo il mining casalingo più accessibile e meno disturbante. Inoltre, l'aggiunta di un adattatore Wi-Fi ha eliminato la necessità di una connessione Ethernet via cavo, semplificando ulteriormente il processo di mining casalingo. Durante l'inverno, questi minatori modificati sono stati utilizzati come fonte di riscaldamento, trasformando un fastidio in un beneficio.

Esponendo il loro progetto alla comunità Bitcoin e di fronte all'interesse suscitato, gli inventori di Attakai hanno deciso di pubblicare guide dettagliate sulla piattaforma Découvre Bitcoin, consentendo a chiunque di riprodurre la loro esperienza di mining casalingo. Ora stanno considerando l'espansione di questo concetto al di là del contesto domestico. L'obiettivo è dimostrare come un minatore modificato possa essere trasformato in un riscaldamento ausiliario silenzioso utilizzabile durante l'inverno, offrendo una transizione graduale a una seconda parte di formazione dedicata all'implementazione pratica di queste modifiche, illustrata da video esplicativi. Resta comunque da capire se questa iniziativa può essere estesa su una scala più ampia, offrendo così un'alternativa realistica e sostenibile alle attuali strutture di mining centralizzate.

![image](assets/overview/attakai.png)

### La limite di questa decentralizzazione?
Sebbene l'idea di decentralizzare il mining attraverso l'utilizzo produttivo del calore generato sembri promettente, presenta alcune limitazioni e rimangono delle domande. Le strutture ad alto consumo energetico, come saune e piscine, potrebbero beneficiare di questo concetto utilizzando il calore prodotto dai minatori per riscaldare l'acqua delle loro strutture. Questa pratica è già stata adottata da alcuni membri della comunità Bitcoin, che stanno esplorando diversi metodi per utilizzare in modo efficiente il calore generato dagli apparecchi di mining. Ad esempio, una sala per feste potrebbe teoricamente essere riscaldata da tre o quattro S19, ognuno dei quali consuma 3000 watt e produce una quantità equivalente di calore.

Tuttavia, è importante sottolineare che il consumo di energia e la produzione di calore sono equivalenti, che l'energia venga utilizzata da un radiatore elettrico o da un minatore. Per ogni kilowatt di elettricità utilizzata, la quantità di calore prodotta sarà la stessa in entrambi i casi. La differenza sta nel fatto che il minatore fornirà non solo il calore, ma anche una ricompensa in bitcoin, offrendo così un incentivo economico per utilizzare un minatore anziché un semplice radiatore elettrico. Questa ricompensa aggiuntiva potrebbe contribuire ad attenuare le preoccupazioni legate all'alto consumo energetico dei minatori.

La questione dell'efficienza e della fattibilità a lungo termine dell'utilizzo dei minatori di bitcoin per il riscaldamento rimane aperta. Le continue innovazioni nell'hardware di mining e nelle tecnologie di riscaldamento potrebbero potenzialmente aprire nuove strade per un utilizzo più efficiente del calore generato dal mining, contribuendo così alla sostenibilità di questo approccio in futuro.

### Perché avere ricompense in BTC?

La questione della ricompensa in bitcoin anziché in un'altra valuta è fondamentale nel sistema ideato da Satoshi Nakamoto. La creazione del Bitcoin si caratterizza per un tetto massimo fisso di 21 milioni di unità. L'obiettivo era trovare un modo equo per distribuire queste unità appena create. I minatori, fornendo la loro potenza di calcolo per proteggere la rete, rendendo così sempre più costosa qualsiasi attacco, proteggono efficacemente la rete Bitcoin. In cambio di questo contributo cruciale, vengono ricompensati con i nuovi bitcoin creati, facilitando così la distribuzione delle monete nell'ecosistema.
È un sistema vantaggioso per entrambe le parti. I minatori vengono pagati sia per la sicurezza della rete che per l'approvazione delle transazioni. I nuovi bitcoin creati vengono dati come incentivo per rafforzare la sicurezza, mentre le commissioni di transazione rappresentano un reddito aggiuntivo per l'approvazione delle transazioni. Questi due elementi combinati costituiscono la ricompensa totale per il mining. La questione del futuro del mining sorge a causa della riduzione programmata delle ricompense per il mining, che diminuiscono della metà ogni quattro anni, in un evento noto come "halving". Entro il 2032, la ricompensa per blocco sarà inferiore a un bitcoin e nel 2140 non verranno creati nuovi bitcoin. A quel punto, i minatori dipenderanno esclusivamente dalle commissioni di transazione per il pagamento. La rete Bitcoin dovrà supportare un grande volume di transazioni, con commissioni sufficientemente alte, per garantire la redditività del mining.
L'emergere del Lightning Network, che consente transazioni veloci e a basso costo al di fuori della blockchain principale di Bitcoin, solleva interrogativi sul futuro del mining. Il Lightning Network ha il potenziale per ridurre significativamente le commissioni di transazione, influenzando così il reddito dei minatori. Tuttavia, ciò dipenderà dall'adozione e dall'uso del Lightning Network rispetto alla rete Bitcoin principale. In uno scenario pessimistico, i minatori potrebbero trovare redditizio continuare a minare anche a perdita, se hanno ammortizzato i loro costi e hanno accesso a energia elettrica a basso costo. In uno scenario più ottimistico, le commissioni di transazione sulla rete Bitcoin principale potrebbero rimanere sufficientemente alte da mantenere la redditività del mining.

### Cosa dovrebbe essere incluso in un blocco Bitcoin?

Per quanto riguarda la questione di cosa dovrebbe essere incluso in un blocco Bitcoin, è fondamentale considerare la natura complementare dei diversi strati della rete Bitcoin. Sebbene il Lightning Network possa consentire transazioni più veloci e a costo inferiore, dipende ancora dal livello di base di Bitcoin, spesso chiamato "livello di regolamento", per l'apertura e la chiusura dei canali di pagamento.

Con la prevista crescita del Lightning Network e l'aumento conseguente delle aperture e delle chiusure dei canali, lo spazio nei blocchi Bitcoin diventerà sempre più prezioso. La comunità Bitcoin tende già a valorizzare la preservazione di questo spazio, riconoscendone la limitazione intrinseca. Questa consapevolezza ha portato a discussioni sull'uso legittimo o meno dello spazio dei blocchi, con preoccupazioni riguardanti lo "spam" sulla blockchain tramite transazioni considerate non essenziali.

![image](assets/overview/block.png)
La speculazione circonda l'uso futuro dello spazio dei blocchi, ma è generalmente accettato che sia una risorsa rara che dovrebbe essere utilizzata saggiamente. Anche se c'è il desiderio di riempirlo, è essenziale preservarlo per garantire la sostenibilità a lungo termine della rete Bitcoin, in previsione di un futuro aumento della domanda di spazio nei blocchi. Come in ogni mercato libero, l'offerta e la domanda regoleranno l'uso dello spazio dei blocchi. Con un'offerta limitata, le parti interessate dovranno fare scelte informate sull'uso di questo prezioso spazio per garantire l'efficienza e la sicurezza a lungo termine della rete Bitcoin.

## Il mining nel protocollo Bitcoin

![Chi ha il potere? Bitcoin, energia e produttori](https://www.youtube.com/watch?v=4wywK6BfDw8)

Il ruolo dei minatori nella rete Bitcoin è stato oggetto di intenso dibattito durante la guerra dei blocchi. Sebbene siano essenziali per la sicurezza e la funzionalità della rete, i minatori non detengono necessariamente il potere ultimo nell'ecosistema Bitcoin. L'equilibrio tra i minatori, i nodi e gli utenti finali garantisce l'integrità e la distribuzione della rete.

### La guerra dei blocchi

Durante la guerra dei blocchi, molti minatori erano contrari a alcune evoluzioni della rete, evidenziando la tensione tra i diversi attori dell'ecosistema. La domanda rimane su come bilanciare il potere tra i minatori, i nodi e gli utenti per garantire la sicurezza a lungo termine di Bitcoin.

Sicurezza ed Equilibrio di Potere

![immagine](assets/overview/blocksize-wars--BTC-vs-BCH-.webp)

Il dilemma della sicurezza di Bitcoin si basa su un equilibrio delicato. Sebbene i minatori svolgano un ruolo essenziale nella convalida e nella creazione dei blocchi, i nodi mantengono l'integrità verificando e convalidando le transazioni e i blocchi. Un blocco errato o fraudolento sarà rifiutato dai nodi, censurando così il minatore e preservando la sicurezza della rete. Il potere è anche detenuto dai nodi e dagli utenti della rete Bitcoin. I nodi hanno il potere di verifica e convalida, mentre gli utenti hanno il potere di scegliere quale catena di blocchi utilizzare. Questa distribuzione del potere assicura la distribuzione e l'integrità della rete Bitcoin.

La guerra dei blocchi ha rivelato l'incertezza e la tensione intrinseche nella gestione della rete Bitcoin. Sebbene Bitcoin Core sia attualmente la catena dominante, il dibattito sulla governance e la gestione della rete persiste.
Alla fine, la responsabilità è condivisa tra tutti gli attori della rete Bitcoin. Una diminuzione del numero di utenti, nodi o minatori potrebbe indebolire la rete, aumentando il rischio di centralizzazione e vulnerabilità agli attacchi. Ogni attore contribuisce alla robustezza e alla sicurezza della rete, rafforzando l'importanza di mantenere un equilibrio di potere e responsabilità.
### Il potere dei minatori

L'elegante teoria dei giochi di Satoshi Nakamoto ha stabilito una situazione in cui ogni attore della rete Bitcoin è incentivato ad agire correttamente per proteggere sia i propri interessi che quelli degli altri partecipanti. Ciò crea un equilibrio in cui il comportamento scorretto può essere punito, rafforzando così la sicurezza e la stabilità dell'intero sistema. Nonostante questo equilibrio, gli Stati rimangono una potenziale minaccia. Come indicato nella presentazione a Surfing Bitcoin 2022, gli Stati possono cercare di attaccare l'industria del mining, esponendo la rete Bitcoin a rischi di centralizzazione e attacco. Scenari ipotetici come un attacco militare mirato alle strutture di produzione di hardware per il mining sottolineano l'importanza della diversificazione geografica e industriale per la resilienza della rete Bitcoin.

![image](assets/overview/miner.png)

La centralizzazione della produzione di hardware per il mining in Cina rappresenta un altro rischio. Un rifiuto di esportare macchine per il mining o un accumulo di hashrate per un potenziale attacco del 51% da parte della Cina sottolineano la necessità di una produzione diversificata di hardware per il mining. Di fronte a questi rischi, la comunità Bitcoin sta attivamente esplorando soluzioni. Aziende come Intel stanno considerando la produzione di attrezzature per il mining negli Stati Uniti, contribuendo alla distribuzione della produzione. Altre iniziative, come quella di Block con il suo Mining Development Kit (MDK) open source, mirano a ridurre i monopoli nella progettazione e produzione di hardware per il mining, consentendo una distribuzione più ampia dell'hashrate. Al centro di queste discussioni c'è la missione fondamentale di Bitcoin: essere una rete di scambio di valore resistente alla censura. La comunità Bitcoin si impegna costantemente a rafforzare la distribuzione, la resistenza alla censura e l'antifragilità della rete, respingendo proposte come il passaggio al proof of stake, che non si allineano con questi principi fondamentali.

### Il legame fisico della prova di lavoro vs la prova di scommessa
La corrélation entre le prix du bitcoin et le hashrate est un sujet d'intérêt dans l'industrie de la cryptomonnaie. Le hashrate fait référence à la puissance de calcul totale du réseau Bitcoin, mesurée en termes de nombre de calculs par seconde. Il est généralement considéré comme un indicateur de la sécurité et de la robustesse du réseau.

Il existe une corrélation positive entre le prix du bitcoin et le hashrate. En d'autres termes, lorsque le prix du bitcoin augmente, le hashrate a tendance à augmenter également. Cela peut s'expliquer par le fait que lorsque le prix du bitcoin est élevé, il devient plus rentable pour les mineurs de participer au réseau et de consacrer des ressources à l'extraction de nouvelles pièces.

D'autre part, lorsque le prix du bitcoin baisse, certains mineurs peuvent trouver moins rentable de continuer à extraire, ce qui peut entraîner une diminution du hashrate. Cependant, il est important de noter que cette corrélation n'est pas toujours linéaire et peut être influencée par d'autres facteurs tels que la disponibilité de l'équipement minier et les coûts d'électricité.

En conclusion, la corrélation entre le prix du bitcoin et le hashrate est complexe et peut être influencée par plusieurs facteurs. Cependant, il est généralement admis qu'une augmentation du prix du bitcoin est souvent accompagnée d'une augmentation du hashrate, ce qui renforce la sécurité et la résilience du réseau Bitcoin.
Il mining di Bitcoin può essere svolto con l'obiettivo di ottenere un profitto o di contribuire alla sicurezza e alla decentralizzazione della rete. Molti miner si concentrano sul calcolo dei costi e sulla redditività dell'attività di mining, cercando di massimizzare i guadagni. Tuttavia, è importante considerare anche l'importanza di contribuire al funzionamento del network Bitcoin e alla sua sicurezza. I miner che scelgono di dedicarsi al mining per il bene della rete spesso sono disposti a sopportare costi più elevati e a guadagnare meno, poiché ritengono che la sicurezza e la decentralizzazione del network siano di fondamentale importanza per il successo a lungo termine di Bitcoin.
La question de la souveraineté et de la régulation est également un aspect important du minage de Bitcoin. Certains pays considèrent le minage de Bitcoin comme une activité illégale ou non réglementée, ce qui peut entraîner des conséquences juridiques pour les mineurs. D'autres pays adoptent une approche plus favorable en encourageant le développement de l'industrie du minage de Bitcoin sur leur territoire.

La souveraineté est également un enjeu majeur, car le minage de Bitcoin est un processus décentralisé qui ne dépend pas d'une autorité centrale. Cela signifie que les mineurs peuvent opérer indépendamment des frontières nationales, ce qui peut poser des défis aux gouvernements qui cherchent à réglementer cette activité.

Il est important de trouver un équilibre entre la souveraineté nationale et la régulation pour assurer la sécurité et la viabilité du réseau Bitcoin. Une régulation excessive peut entraîner une centralisation du pouvoir de hachage, tandis qu'une absence de régulation peut entraîner des risques pour les utilisateurs et le réseau lui-même.

La communauté Bitcoin continue de débattre de ces questions et cherche des solutions pour promouvoir une régulation équilibrée qui soutienne la souveraineté individuelle tout en garantissant la sécurité et la stabilité du réseau.
### Sovranità prima del profitto?
Per affrontare la questione cruciale della ricchezza attraverso il mining, è importante considerare diverse prospettive e approcci. Le domande sulla redditività del mining sono comuni, con domande che riguardano l'acquisto di azioni di aziende come Riot o il noleggio di macchine per il mining in paesi a basso costo energetico come l'Islanda o la Russia. Prima di avventurarsi nel mining, una considerazione essenziale sarebbe confrontare la redditività del mining con l'acquisto diretto di Bitcoin. Se il costo di mining di un Bitcoin supera il costo dell'acquisto diretto, di solito è più saggio acquistare direttamente il Bitcoin. Ciò evita le molteplici sfide e i costi associati al processo di mining.

Tuttavia, il mining offre vie uniche per coinvolgersi nell'ecosistema Bitcoin. Ad esempio, il mining di Bitcoin in inverno può essere un modo ingegnoso per riscaldare la propria casa generando reddito in Bitcoin. Un'altra opzione è investire in aziende che vendono hardware per il mining e che conservano e gestiscono le macchine in posizioni a basso costo energetico, offrendo così l'accesso a tariffe elettriche vantaggiose senza i problemi legati alla gestione delle attrezzature.

Nonostante queste opzioni, il mining presenta sfide significative. Il noto adagio del mondo delle criptovalute, "Not your keys, not your Bitcoins" (Non le tue chiavi, non i tuoi Bitcoin), trova una risonanza simile nel mondo del mining: "Not your hashrate, not your reward" (Non il tuo hashrate, non la tua ricompensa). Storie di delusioni e di macchine disconnesse sono comuni, con molti attori che promettono risultati eccezionali ma non li consegnano. Problemi di fornitura di elettricità e guasti alle macchine possono lasciare gli investitori impotenti, con costose attrezzature che non controllano. In questo contesto, la prudenza e una comprensione approfondita del settore del mining sono cruciali prima di avventurarsi. Sebbene ci siano opportunità di guadagno, i rischi sono significativi e un approccio informato e riflessivo è essenziale per navigare in questo campo complesso e spesso imprevedibile. Pertanto, è vitale condurre ricerche approfondite e valutare attentamente i vantaggi e gli svantaggi prima di impegnarsi nel mining di Bitcoin.

![image](assets/overview/self.png)

### Bitcoin vergini
L'interdiction du minage en Europe est un sujet qui suscite des débats et des préoccupations. Bien que certains pays européens aient mis en place des réglementations strictes concernant le minage de cryptomonnaies, il n'y a pas d'interdiction générale du minage en Europe. Les réglementations varient d'un pays à l'autre et peuvent être liées à des questions environnementales, énergétiques ou de conformité fiscale. Il est donc important de se renseigner sur les réglementations spécifiques du pays dans lequel vous vous trouvez avant de vous lancer dans le minage de cryptomonnaies.
Con la questione del potenziale divieto del mining in Europa, le discussioni sulla regolamentazione stanno diventando sempre più rilevanti. Il mutevole panorama normativo potrebbe infatti influenzare notevolmente l'industria del mining di Bitcoin. Il divieto del mining in Europa è uno scenario plausibile, soprattutto considerando i precedenti in Cina. Nonostante il divieto, le operazioni di mining continuano in Cina, ma l'Europa potrebbe seguire una strada simile. Una distribuzione più ampia dell'hashrate in diverse regioni potrebbe contribuire a rafforzare la comunità dei minatori in Europa, consentendo loro di contrastare efficacemente i fraintendimenti e le false idee sul mining, il suo impatto ambientale e la sua impronta sulla rete elettrica.
![image](assets/overview/regulation.jpg)

Di fronte a campagne come quelle di Greenpeace e ai dati spesso ingannevoli di alcuni studi, l'arma migliore rimane l'informazione veritiera. È essenziale informare il pubblico e i decisori sulla realtà del mining, sulla sua complessità e sfumatura, anziché lasciarli fare affidamento su stereotipi e informazioni inesatte. Più persone saranno informate e consapevoli di cosa sia realmente il mining, meglio l'industria potrà difendersi dalle eventuali regolamentazioni restrittive.

In conclusione, nonostante il rischio normativo e la possibilità di un divieto del mining in Europa, l'arma più potente rimane l'educazione e l'informazione. Una comprensione chiara e precisa del mining, del suo funzionamento e del suo impatto può contribuire a demistificare l'industria e combattere la disinformazione, offrendo così una migliore resistenza alle potenziali regolamentazioni dannose. L'iniziativa di formare e informare le persone sul mining, come fa questa discussione, è un passo nella giusta direzione per garantire la sostenibilità e la crescita del mining in Europa e in tutto il mondo. Gli sforzi continui per educare e informare sono essenziali per assicurare un futuro sicuro e prospero per l'industria del mining di Bitcoin.

## Intervista a un professionista dell'industria del mining

### Dietro le quinte del mining industriale - Sebastien Gouspillou

![Dietro le quinte del mining industriale - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Home-mining e riutilizzo del calore

## Attakai - il home-mining reso possibile e accessibile!

![Vi presentiamo Attakaï!](https://www.youtube.com/watch?v=gKoh44UCSnE&t=3s)

Attakai, che significa "la temperatura ideale" in giapponese, è il nome dell'iniziativa volta a scoprire il mining di bitcoin attraverso il riutilizzo del calore, lanciata da @ajelexBTC e @jimzap21 con Découvre Bitcoin.
Questa guida per il retrofitting di un ASIC servirà come base per imparare di più sul mining, il suo funzionamento e l'economia sottostante, dimostrando la possibilità di adattare un minatore di Bitcoin per l'uso come radiatori nelle abitazioni. Ciò offre maggiore comfort ed efficienza energetica, consentendo ai partecipanti di ottenere cash back in BTC non KYC sulla loro bolletta di riscaldamento elettrico.
Bitcoin regola automaticamente la difficoltà del mining e ricompensa i minatori per la loro partecipazione, tuttavia, la concentrazione dell'hashrate può rappresentare un rischio per la neutralità della rete. Utilizzare la potenza di calcolo di Bitcoin per soluzioni di riscaldamento beneficia direttamente la rete stessa, aumentando la distribuzione della potenza di calcolo.

### Perché riutilizzare il calore di un ASIC?

È importante comprendere la relazione tra energia e produzione di calore in un sistema elettrico.

Per un investimento di 1 kW di energia elettrica, un radiatore elettrico produce 1 kW di calore, né più né meno. I nuovi radiatori non sono più efficienti dei radiatori tradizionali. Il loro vantaggio risiede nella loro capacità di diffondere il calore in modo continuo e uniforme in una stanza, offrendo quindi maggiore comfort rispetto ai radiatori tradizionali che alternano tra una potenza di riscaldamento elevata e l'assenza di riscaldamento, generando così variazioni di temperatura regolari e disagio.

Un computer, o più in generale una scheda elettronica, non consuma energia per effettuare calcoli, ha semplicemente bisogno che l'energia circoli nei suoi componenti per funzionare. Il consumo di energia è dovuto alla resistenza elettrica dei componenti che produce perdite, generando così calore, questo è ciò che viene chiamato effetto Joule.

Alcune aziende hanno avuto l'idea di condividere le esigenze di potenza di calcolo e le esigenze di riscaldamento attraverso radiatori/server. L'idea è distribuire i server di un'azienda in piccole unità che potrebbero essere collocate in abitazioni o uffici. Tuttavia, questa idea incontra diversi problemi. Le esigenze dei server non sono legate alle esigenze di riscaldamento e le aziende non possono utilizzare le capacità di calcolo dei loro server in modo flessibile. Esistono anche limiti alla larghezza di banda che i singoli individui possono possedere. Tutti questi vincoli impediscono all'azienda di rendere redditizie queste costose installazioni o di fornire un'offerta stabile di server online senza avere centri dati in grado di prendere il sopravvento quando non è presente la necessità di riscaldamento.
> "Il calore del tuo computer non viene sprecato se devi riscaldare la tua casa. Se usi un riscaldamento elettrico dove vivi, allora il calore del tuo computer non è uno spreco. Costa lo stesso generare quel calore con il tuo computer. Se hai un altro sistema di riscaldamento più economico dell'elettrico, allora lo spreco è solo nella differenza di costo. Se è estate e usi l'aria condizionata, allora è il doppio. Il mining di bitcoin dovrebbe avvenire dove è meno costoso. Forse sarà dove il clima è freddo e dove il riscaldamento è elettrico, dove il mining diventerà gratuito."
> Satoshi Nakamoto - 8 agosto 2010

Il Bitcoin e la sua prova di lavoro si distinguono perché regolano automaticamente la difficoltà del mining in base alla quantità di calcoli effettuati dall'intera rete, questa quantità è chiamata hashrate ed è espressa in hash al secondo. Oggi si stima che sia di 380 Exahash al secondo, ovvero 380 miliardi di miliardi di hash al secondo. Questo hashrate rappresenta lavoro e quindi una quantità di energia spesa. Più alto è l'hashrate, maggiore è la difficoltà e viceversa. Pertanto, è possibile attivare o disattivare un minatore di Bitcoin in qualsiasi momento senza conseguenze per la rete, a differenza dei radiatori/server che devono rimanere stabili per offrire il loro servizio. Il minatore viene ricompensato per la sua partecipazione, anche se è relativamente piccola rispetto agli altri.

In sintesi, un radiatore elettrico e un minatore di Bitcoin producono entrambi 1 kW di calore per 1 kW di energia elettrica consumata. Tuttavia, il minatore riceve anche bitcoin come ricompensa. Indipendentemente dal prezzo dell'elettricità, dal prezzo del bitcoin o dalla concorrenza nell'attività di mining sulla rete Bitcoin, è economicamente più vantaggioso riscaldarsi con un minatore piuttosto che con un radiatore elettrico.

### Il valore aggiunto per Bitcoin

Ciò che è importante capire è come il mining contribuisca alla decentralizzazione di Bitcoin.
Diverse tecnologie già esistenti sono state ingegnosamente combinate per dare vita al consenso di Nakamoto. Questo consenso permette di ricompensare economicamente gli attori onesti per la loro partecipazione al funzionamento della rete Bitcoin, scoraggiando nel contempo gli attori disonesti. Questo è uno dei punti chiave che permette alla rete di esistere in modo sostenibile.
Gli attori onesti, coloro che effettuano il mining secondo le regole, sono tutti in competizione tra loro per ottenere la più grande parte possibile della ricompensa per la produzione di nuovi blocchi. Questo incentivo economico porta naturalmente a una forma di centralizzazione poiché le aziende scelgono di specializzarsi in questa attività redditizia riducendo i loro costi grazie all'economia di scala. Questi attori industriali hanno una posizione vantaggiosa per l'acquisto, la manutenzione delle macchine ma anche per la negoziazione di tariffe elettriche all'ingrosso.

> "All'inizio, la maggior parte degli utenti eseguirebbe nodi di rete, ma man mano che la rete si svilupperebbe oltre un certo punto, sarebbe sempre più lasciata agli specialisti con grandi farm di server hardware specializzati. Una batteria di server avrebbe bisogno solo di un singolo nodo sulla rete e il resto della LAN si connetterebbe a quel nodo."
>
> - Satoshi Nakamoto - 2 novembre 2008

Alcune entità detengono una percentuale considerevole dell'hashrate totale in grandi farm di mining. È possibile osservare l'ultima ondata di freddo negli Stati Uniti, dove una parte significativa dell'hashrate è stata messa offline per consentire all'energia di essere ridirezionata verso le case che avevano bisogno di elettricità in modo eccezionale. Per diversi giorni, i minatori sono stati incentivati economicamente a spegnere le loro farm e quindi si può vedere questo clima eccezionale sulla curva dell'hashrate di Bitcoin.

Questo problema potrebbe diventare problematico e rappresenta un rischio significativo per la neutralità della rete. Un attore che possiede più del 51% dell'hashrate potrebbe più facilmente censurare le transazioni se lo desiderasse. Ecco perché è importante distribuire l'hashrate tra più attori anziché in entità centralizzate che potrebbero essere più facilmente sequestrate da un governo, ad esempio.

**Se i minatori sono distribuiti in migliaia, se non milioni, di case in tutto il mondo, diventa molto complicato per uno Stato prenderne il controllo.**

All'uscita dalla fabbrica, un minatore non è adatto per essere utilizzato come radiatore in una casa, a causa di due problemi principali: un rumore eccessivo e l'assenza di regolazione. Tuttavia, questi problemi possono essere facilmente risolti attraverso modifiche hardware e software, consentendo di ottenere un minatore molto più silenzioso e che può essere programmato e automatizzato come i riscaldamenti elettrici moderni.

**Attakaï è un'iniziativa educativa che ti insegna come effettuare un retrofitting dell'Antminer S9 nel modo più economico possibile.**

È un'ottima opportunità per imparare praticando e allo stesso tempo essere ricompensati per la tua partecipazione con satoshi KYC gratuiti.


## Guida all'acquisto di un ASIC usato

![Introduzione ad Attakaï: riscaldarsi con Bitcoin](https://www.youtube.com/watch?v=U_PLo59lp-g)
In questa sezione vedremo le buone pratiche per l'acquisto di un Bitmain Antminer S9 usato, la macchina su cui si basa questo tutorial di retrofitting in radiatore. Questa guida funziona anche per altri modelli di ASIC in quanto si tratta di una guida generale per l'acquisto di hardware per il mining usato.
L'Antminer S9 è un dispositivo offerto da Bitmain dal maggio 2016. Consuma 1400W di elettricità e produce 13,5 TH/s. Nonostante sia considerato vecchio, rimane un'ottima opzione per iniziare il mining. Dato che è stato prodotto in grande quantità, è facile trovare pezzi di ricambio in abbondanza in molte regioni del mondo. Di solito è possibile acquistarlo direttamente da privati su siti come Ebay o LeBonCoin, poiché i rivenditori per professionisti non lo offrono più a causa della sua minore competitività rispetto a macchine più recenti. È meno efficiente rispetto ad ASIC come l'Antminer S19, offerto dal marzo 2020, ma questo lo rende un hardware usato conveniente e più adatto alle modifiche che effettueremo.

L'Antminer S9 è disponibile in diverse varianti (i,j) che apportano modifiche minori all'hardware di prima generazione. Non riteniamo che questo elemento debba influenzare la vostra decisione di acquisto e questa guida funziona per tutte queste varianti.

Il prezzo degli ASIC varia in base a molti fattori come il prezzo del bitcoin, la difficoltà della rete, l'efficienza della macchina e il costo dell'elettricità. È quindi difficile dare una stima precisa per l'acquisto di una macchina usata. A febbraio 2023, il prezzo atteso in Francia si situa generalmente tra 100€ e 200€ ma questi prezzi sono suscettibili di cambiare molto rapidamente.

![image](assets/guide-achat/1.jpeg)

L'Antminer S9 è composto dalle seguenti parti:

- 3 hashboard che contengono i chip che producono l'hashing

![image](assets/guide-achat/2.jpeg)

- Una scheda di controllo che include uno slot per una scheda SD, una porta Ethernet e connettori per gli hashboard e i ventilatori. È il cervello del vostro ASIC.

![image](assets/guide-achat/3.jpeg)

- 3 cavi di dati che collegano gli hashboard alla scheda di controllo

![image](assets/guide-achat/4.jpeg)

- L'alimentatore che funziona a 220V e può quindi essere collegato come un normale elettrodomestico

![image](assets/guide-achat/5.jpeg)

- 2 ventilatori da 120mm

![image](assets/guide-achat/6.jpeg)

- Un cavo maschio C13

![image](assets/guide-achat/7.jpeg)
Quando acquisti una macchina usata, è importante verificare che tutte le parti siano incluse e funzionanti. Durante lo scambio, dovresti chiedere al venditore di accendere la macchina per verificarne il corretto funzionamento. È importante verificare che l'apparecchio si accenda correttamente, quindi verificare la connettività a Internet collegando un cavo Ethernet e accedendo all'interfaccia di connessione di Bitmain tramite un browser Internet sulla stessa rete locale. Puoi trovare questo indirizzo IP collegandoti all'interfaccia del tuo router Internet e cercando i dispositivi connessi. Questo indirizzo dovrebbe avere il seguente formato: 192.168.x.x
![image](assets/guide-achat/8.gif)

Verifica anche che le credenziali predefinite funzionino (nome utente: root, password: root). Se le credenziali predefinite non funzionano, sarà necessario eseguire un reset della macchina.

![image](assets/guide-achat/9.jpeg)

Una volta connesso, dovresti essere in grado di vedere lo stato di ogni hashboard sulla dashboard. Se il minatore è connesso a un pool, dovresti vedere tutte le hashboard funzionare. È importante notare che i minatori fanno molto rumore, è normale. Assicurati anche che le ventole funzionino correttamente.

Successivamente, puoi rimuovere il pool di mining del vecchio proprietario per configurare il tuo in seguito. Se lo desideri, puoi anche ispezionare le hashboard smontando la macchina. Tuttavia, questa operazione è più complessa e richiede più tempo e alcuni strumenti. Se desideri procedere con lo smontaggio, puoi fare riferimento alla parte successiva di questo tutorial che spiega come farlo. È importante notare che i minatori accumulano molta polvere e richiedono una manutenzione regolare. È questa accumulazione di polvere e la qualità della manutenzione che puoi osservare smontando la macchina.
Dopo aver esaminato tutti questi punti, puoi acquistare la tua macchina con un alto grado di fiducia. In caso di dubbi, rivolgiti alla comunità.

Per sintetizzare questa guida in una frase: **"Non fidarti, verifica"**.

[Puoi anche rivolgerti a professionisti del ricondizionamento di macchine per il mining, come il nostro partner 21energy. Offrono S9 testati, puliti e con il software BraiiinOS+ già installato. Utilizzando il codice di affiliazione "decouvre", otterrai uno sconto del 10% sull'acquisto di un S9, supportando anche il progetto Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guida all'acquisto di parti per modifiche hardware del S9

![Introduzione ad Attakaï: riscaldarsi con Bitcoin](https://www.youtube.com/watch?v=U_PLo59lp-g)
Proprietario di un Antminer S9, probabilmente sai quanto questo dispositivo possa essere rumoroso e ingombrante. Tuttavia, è possibile trasformarlo in un riscaldamento silenzioso e connesso seguendo alcuni semplici passaggi. In questa sezione ti presenteremo l'attrezzatura necessaria per apportare le modifiche.

Se sei un bricoleur esperto e stai cercando di trasformare un minatore in un riscaldamento, questo tutorial è fatto per te. Vogliamo avvertirti che le modifiche apportate a un dispositivo elettronico possono comportare rischi elettrici. Pertanto, è essenziale prendere tutte le precauzioni necessarie per evitare danni o lesioni.

1. Sostituire le ventole

Le ventole originali dell'Antminer S9 sono troppo rumorose per utilizzare il tuo Antminer come riscaldamento. La soluzione è sostituirle con ventole più silenziose. Il nostro team ha testato diversi modelli del marchio Noctua e ha selezionato il Noctua NF-A14 iPPC-2000 PWM come miglior compromesso, assicurandosi di scegliere la versione a 12V delle ventole. Questa ventola da 140 mm può produrre fino a 1200W di calore mantenendo un livello teorico di rumore di 31 dB. Per poter installare queste ventole da 140 mm, sarà necessario utilizzare un adattatore da 140 mm a 120 mm che potrai trovare nel negozio di DécouvreBitcoin. Aggiungeremo anche delle griglie di protezione da 140 mm.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

Anche la ventola dell'alimentatore è abbastanza rumorosa e deve essere sostituita. Consigliamo il Noctua NF-A6x25 PWM. Nota che i connettori delle ventole Noctua non sono gli stessi di quelli originali, quindi avrai bisogno di un adattatore per collegarli, ne bastano 2. Anche qui, assicurati di scegliere la versione a 12V della ventola.

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

2. Aggiungere un bridge WIFI/Ethernet

Invece di utilizzare un cavo Ethernet, puoi connettere il tuo Antminer tramite WIFI aggiungendo un bridge WIFI/Ethernet. Abbiamo selezionato il vonets vap11g-300 perché consente di recuperare facilmente il segnale WIFI del tuo router e trasmetterlo al tuo Antminer tramite Ethernet senza creare una sottorete. Se hai competenze elettriche, puoi alimentarlo direttamente con l'alimentatore dell'Antminer senza dover aggiungere un caricatore USB, per questo avrai bisogno di un jack femmina da 5,5 mm x 2,1 mm.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

3. Opzionale: aggiungere una presa intelligente.
Se desideri accendere/spegnere il tuo Antminer dal tuo smartphone e monitorarne il consumo energetico, puoi aggiungere una presa smart. Abbiamo testato la presa ANTELA in versione 16A compatibile con l'applicazione smartlife. Questa presa smart consente di consultare il consumo giornaliero e mensile e si connette direttamente al tuo router Internet tramite Wi-Fi.
![image](assets/piece/8.jpeg)

Elenco del materiale e link

* 2X adattatori 3D da 140mm a 120mm

* [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

* [2X Griglie per ventilatori da 140mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
  
* [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)

* [Cavo elettrico da 2,5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
* [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Presa intelligente opzionale ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - modifica del software di un Antminer S9

## Configurazione di un bridge WIFI/Ethernet Vonet

![Collegare un Antminer S9 alla rete Wifi](https://www.youtube.com/watch?v=y4oYURBaPqg)

Per collegare il tuo ASIC tramite WIFI, avrai bisogno di un dispositivo chiamato bridge, che consente di ricevere il segnale WIFI dal tuo router e trasmetterlo a un altro dispositivo tramite Ethernet.

Ci sono molti dispositivi che possono fare ciò, consigliamo il VONETS WiFi Bridge/Repeteur per la sua praticità.

Alimenta il bridge collegandolo tramite USB.

Dal tuo computer, connettiti alla rete WIFI VONETS_****** con la password 12345678.

![image](assets/software/vonet1.png)

Nome utente: admin
Password: admin

![image](assets/software/vonet2.png)

Seleziona Wizard

![image](assets/software/vonet3.png)

Seleziona la rete WIFI a cui desideri connettere il tuo minatore e clicca su Avanti.

ATTENZIONE: il bridge Vonet funziona solo a 2,4 GHz, oggi i router di solito offrono due reti WIFI, una a 2,4 GHz e una a 5 GHz.

![image](assets/software/vonet4.png)

Inserisci la password della tua rete WIFI in "Source WIFI hotspot password".
Se non desideri utilizzare il tuo bridge Vonet per estendere la tua rete WIFI, spunta la casella "Disable Hotspot", altrimenti lasciala deselezionata.

Successivamente, puoi fare clic su Applica.

Infine, dovrai fare clic su Riavvia, il bridge si riavvierà in pochi minuti.

Il bridge dovrebbe connettersi al tuo router e apparire con il nome di "[VONETS.COM](http://vonets.com/)".
Potrebbe essere necessario scollegare/ricollegare il bridge se non si connette ancora dopo alcuni minuti.

Una volta che il bridge è connesso, collega il cavo Ethernet del bridge al tuo ASIC e collega l'ASIC all'alimentazione. Potrai quindi accedere all'interfaccia dell'ASIC allo stesso modo in cui lo faresti se fosse collegato direttamente via Ethernet al tuo router.

## Ripristinare un Antminer S9

Prima di installare BraiinOS+, potrebbe essere necessario ripristinare il tuo S9 alle impostazioni di fabbrica.
Questa procedura può essere applicata tra 2 e 10 minuti dopo l'avvio del minatore.
2 minuti dopo aver acceso il minatore, premere il pulsante "Reset" per 5 secondi, quindi rilasciarlo. Il minatore verrà ripristinato alle impostazioni di fabbrica entro 4 minuti e si riavvierà automaticamente (non è necessario spegnerlo).

![immagine](assets/software/1.jpeg)

## Installare BraiinsOS+ su un Antminer S9

![Installare Braiins OS+ sul proprio Antminer S9](https://www.youtube.com/watch?v=luqwlvzGsO4)

Il software originale installato da Antminer sulle loro macchine da mining è limitato in termini di funzionalità. Per questo motivo, in questa guida installeremo un altro software chiamato BraiinsOS+. Si tratta di un software di terze parti sviluppato dal primo pool di mining di Bitcoin che offre più funzionalità e consente, ad esempio, di modificare la potenza della macchina.

Ci sono diversi modi per installare Braiins OS+ su un ASIC. Puoi fare riferimento a questa guida ma anche alla [documentazione ufficiale di Braiins](https://academy.braiins.com/en/braiins-os/about/).

Vedremo qui come installare facilmente Braiins OS+ direttamente sulla memoria del tuo Antminer utilizzando il software BOS toolbox, sostituendo così il sistema operativo originale, attraverso i seguenti passaggi dettagliati.

1. Alimenta il tuo Antminer e collegalo al tuo router internet.
2. Scarica BOS toolbox per Windows / Linux.
3. Decomprimi il file scaricato e apri il file bos-toolbox.bat, seleziona la lingua e dopo qualche istante vedrai questa finestra:

![immagine](assets/software/5.jpeg)

4. BOS toolbox ti permetterà di trovare facilmente l'indirizzo IP del tuo Antminer e installare BraiinsOS+. Se conosci già l'indirizzo IP della tua macchina, puoi passare al passaggio 8. Altrimenti, vai alla scheda "scan".

![immagine](assets/software/6.jpeg)

5. Di solito, nelle reti domestiche, l'intervallo di indirizzi IP si trova tra 192.168.1.1 e 192.168.1.255, quindi inserisci nell'campo "IP range" "192.168.1.0/24". Se la tua rete è diversa, modifica questi indirizzi di conseguenza. Quindi clicca su "Start".

6. Attenzione, se l'Antminer ha una password, la rilevazione non funzionerà. In tal caso, la soluzione più semplice è eseguire un ripristino.

7. Dovresti vedere tutti gli Antminer sulla tua rete, qui l'indirizzo IP è 192.168.1.37.

![immagine](assets/software/7.jpeg)

8. Fai clic su "Back" e poi sulla scheda "install", inserisci l'indirizzo IP trovato in precedenza e clicca su "Start".

> Se l'installazione non funziona, potrebbe essere necessario eseguire un ripristino e riprovare (vedi la sezione precedente).
9. Dopo alcuni istanti, il tuo Antminer si riavvierà e potrai accedere all'interfaccia di Braiins OS+ all'indirizzo IP indicato, qui 192.168.1.37, da inserire direttamente nella barra degli indirizzi del tuo browser, nome utente predefinito "root" senza password predefinita.

## Configurare BraiinsOS+

![Configurare il tuo Antminer S9 con Braiins OS+](https://www.youtube.com/watch?v=dK0t8M8kLYg)

Dovrai connetterti al tuo ASIC utilizzando l'indirizzo IP locale del tuo dispositivo sulla tua rete tramite un browser.

Puoi trovare l'indirizzo IP della tua macchina utilizzando lo strumento BOS toolbox o direttamente sulla pagina web del tuo router.

Le credenziali predefinite sono le stesse del sistema operativo originale.

- nome utente: root
- password: (nessuna)

Verrai quindi accolto dalla Dashboard di Brains OS+

### Dashboard

![image](assets/software/14.jpeg)

In questa prima pagina potrai osservare le prestazioni della tua macchina in tempo reale.

- Tre grafici in tempo reale che mostrano la temperatura, l'hashrate e lo stato complessivo della tua macchina.
- A destra l'hashrate effettivo, la temperatura media dei chip, l'efficienza stimata in W/THs e il consumo di energia.
- Sotto la velocità di rotazione delle ventole in percentuale rispetto alla velocità massima e il numero di rotazioni al minuto.

![image](assets/software/15.jpeg)

- Più in basso troverai una vista dettagliata di ogni hashboard. La temperatura media della board e dei chip che la compongono, la tensione e la frequenza.
- Un dettaglio sui pool di mining attivi in Pools.
- Lo stato dell'autotuning in Tuner Status.
- A destra i dettagli sui dati trasmessi al pool.

### Configurazione

![image](assets/software/16.jpeg)

### Sistema

![image](assets/software/17.jpeg)

### Azioni rapide

![image](assets/software/18.jpeg)

# Attakai - Modifica delle ventole

## Sostituire la ventola dell'alimentatore

![Sostituire le ventole per ridurre il rumore](https://www.youtube.com/watch?v=2CNGKZiveuc)

> ATTENZIONE: È essenziale aver installato in precedenza Braiins OS+ sul tuo minatore, o qualsiasi altro software in grado di ridurre le prestazioni della tua macchina. Questa misura è cruciale perché, al fine di ridurre il rumore, installeremo ventole meno potenti che saranno in grado di dissipare meno calore.

![image](assets/hardware/cover.jpeg)

### Materiali necessari

- 1 ventola Noctua NF-A6x25 PWM
- Filo elettrico da 2,5 mm2

> ATTENZIONE: Prima di iniziare, assicurati di aver scollegato il tuo minatore per evitare qualsiasi rischio di scossa elettrica.

![image](assets/hardware/1.jpeg)
Prima di tutto, rimuovi le 6 viti sul lato del case che lo tengono chiuso. Una volta rimosse le viti, apri delicatamente il case per rimuovere la protezione in plastica che copre i componenti.
![image](assets/hardware/2.jpeg)
![image](assets/hardware/3.jpeg)

Successivamente, è il momento di rimuovere la ventola originale facendo attenzione a non danneggiare gli altri componenti. Per farlo, rimuovi le viti che la tengono in posizione e stacca delicatamente la colla bianca che circonda il connettore. È importante procedere con delicatezza per evitare di danneggiare i fili o i connettori.

![image](assets/hardware/4.jpeg)

Una volta rimossa la ventola originale, noterai che i connettori della nuova ventola Noctua non corrispondono a quelli della ventola originale. Infatti, la nuova ventola ha 3 fili, di cui uno giallo che consente di controllare la velocità. Tuttavia, questo filo non verrà utilizzato in questo caso specifico. Per collegare la nuova ventola, è quindi consigliabile utilizzare un adattatore speciale. È importante notare che questo adattatore può talvolta essere difficile da trovare.

![image](assets/hardware/5.jpeg)

Se non hai questo adattatore, puoi comunque procedere al collegamento della nuova ventola utilizzando un connettore elettrico. Per farlo, dovrai tagliare i cavi della vecchia e della nuova ventola.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

Sulla nuova ventola, usa un cutter e taglia delicatamente i contorni del rivestimento principale a 1 cm senza tagliare i rivestimenti dei cavi sottostanti.

![image](assets/hardware/8.jpeg)

Poi, tirando verso il basso il rivestimento principale, taglia i rivestimenti dei cavi rossi e neri nello stesso modo di prima. E taglia il cavo giallo a filo.

![image](assets/hardware/9.jpeg)

Sulla vecchia ventola è più delicato tagliare il rivestimento principale senza danneggiare i rivestimenti dei cavi rossi e neri. Per farlo, abbiamo usato un ago che abbiamo fatto scorrere tra il rivestimento principale e i cavi rossi e neri.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Una volta liberati i cavi rossi e neri, taglia delicatamente i rivestimenti per non danneggiare i fili elettrici.

![image](assets/hardware/12.jpeg)

Poi collega i cavi con un connettore, il filo nero con il nero e il filo rosso con il rosso. Puoi anche aggiungere del nastro elettrico.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)
Una volta effettuato il collegamento, è ora di installare il nuovo ventilatore Noctua con la griglia e le vecchie viti, le nuove viti presenti nella scatola saranno riutilizzate in seguito. Assicurati di posizionarlo nella giusta orientazione. Noterai una freccia su uno dei lati del ventilatore, che indica la direzione del flusso d'aria. È importante posizionare il ventilatore in modo che questa freccia punti verso l'interno del case. Quindi ricollega il ventilatore.
![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Opzionale: Se hai competenze elettriche, puoi aggiungere direttamente un connettore jack femmina da 5,5 mm all'uscita di alimentazione a 12V, che consentirà di alimentare direttamente il bridge Wi-Fi Vonet. Tuttavia, se non sei sicuro delle tue competenze elettriche, è meglio utilizzare il connettore USB con un caricatore per smartphone per evitare qualsiasi rischio di cortocircuito o danni elettrici.

![image](assets/hardware/17.jpeg)

Una volta effettuati i collegamenti, rimetti la plastica del coperchio sopra la plastica del case e non all'interno.

![image](assets/hardware/18.jpeg)

Infine, rimetti il coperchio del case al suo posto e riavvita le 6 viti sui lati per mantenere tutto in posizione. Ecco fatto, il tuo case di alimentazione è ora dotato di un nuovo ventilatore.

## Sostituire i Ventilatori Principali

![Sostituire i ventilatori per ridurre il rumore](https://www.youtube.com/watch?v=2CNGKZiveuc)

> ATTENZIONE: È essenziale aver precedentemente installato Braiins OS+ sul tuo minatore, o qualsiasi altro software in grado di ridurre le prestazioni della tua macchina. Questa misura è cruciale perché, al fine di ridurre il rumore, installeremo ventilatori meno potenti, che saranno in grado di dissipare meno calore.

![image](assets/hardware/cover.jpeg)


### Materiali necessari

- 2 adattatori 3D da 140mm a 120mm
- 2 ventilatori Noctua NF-A14 iPPC-2000 PWM
- 2 griglie per ventilatori da 140mm

> ATTENZIONE: Prima di iniziare, assicurati di aver scollegato il tuo minatore per evitare qualsiasi rischio di scossa elettrica.

1. Inizialmente, scollega i ventilatori e svítali.

![image](assets/hardware/19.jpeg)

2. I connettori dei nuovi ventilatori Noctua non corrispondono a quelli originali, ma niente paura! Prendi il tuo cutter e taglia delicatamente le piccole linguette di plastica in modo che i connettori si adattino perfettamente al tuo minatore.

![image](assets/hardware/20.jpeg)
![image](assets/hardware/21.jpeg)
3. È ora di installare le parti 3D!
Fissale su entrambi i lati del minatore utilizzando le viti che hai rimosso dai ventilatori. Avvita fino a quando la testa della vite si infila nella parte 3D e questa rimane saldamente in posizione. Attenzione a non stringere troppo, potresti deformare la parte e una delle viti potrebbe toccare un condensatore!

![image](assets/hardware/22.jpeg)

4. Passiamo ora ai ventilatori.
Fissali sulle parti 3D utilizzando le viti fornite nella scatola. Presta attenzione alla direzione del flusso d'aria, le frecce sui lati dei ventilatori ti indicheranno la direzione da seguire. Vai dal lato della porta Ethernet all'altro lato. Vedi foto qui sotto

![image](assets/hardware/23.jpeg)
![image](assets/hardware/24.jpeg)
![image](assets/hardware/25.jpeg)

5. Ultimo passo: collega i ventilatori e fissali con le griglie sopra utilizzando le viti che non sono state utilizzate nella scatola del ventilatore di alimentazione. Ne hai solo 4, ma 2 per griglia negli angoli opposti saranno sufficienti. Se necessario, puoi cercare altre viti simili in un negozio di ferramenta.

![image](assets/hardware/26.jpeg)
![image](assets/hardware/27.jpeg)

Nel frattempo, mentre aspetti di poter offrire un involucro più attraente al tuo nuovo riscaldamento, puoi fissare il case e l'alimentazione con fascette da elettricista.

![image](assets/hardware/28.jpeg)

E per il tocco finale, collega il bridge Vonet alla porta Ethernet con il suo alimentatore.

![image](assets/hardware/29.jpeg)

Ecco fatto, bravo! Hai appena sostituito l'intera parte meccanica del tuo minatore. Ora dovresti sentire molto meno rumore.

# Attakai - Configurazione

## Unisciti a un pool di mining

![Unisciti a un pool di mining con un Antminer S9](https://www.youtube.com/watch?v=wM-dRog6mls&t=166s)
Si vous souhaitez créer un système de chauffage en utilisant une pool de minage, il est important de choisir celle qui convient le mieux à vos besoins. Une pool de minage est un groupe de mineurs qui mettent en commun leur puissance de calcul pour augmenter leurs chances de trouver un bloc et de recevoir une récompense. En rejoignant une pool, vous partagez les frais et les récompenses avec les autres mineurs en fonction de votre contribution au hashrate de la pool.

Il est important de noter que si vous décidez de miner seul, vos chances de trouver un bloc et de recevoir une récompense sont très faibles. En rejoignant une pool, vous augmentez considérablement vos chances de succès. Cependant, il est également possible, bien que très improbable, de réussir en tant que mineur solo.

Dans notre guide, nous nous concentrerons sur la création d'un système de chauffage en utilisant une pool de minage.
Le considerazioni da tenere in considerazione nella scelta di un pool di mining sono il funzionamento delle ricompense del pool, che possono essere diverse, così come l'importo minimo prima di poter prelevare le ricompense su un indirizzo. Ad esempio, Braiins, che offre il software di cui stiamo parlando qui, offre anche un pool. Questo pool ha un sistema di ricompensa chiamato "Score" che incoraggia i minatori a minare per lunghi periodi. La partecipazione include un fattore di tempo di attività che viene espresso con un "scoring hashrate". Nel nostro caso, in cui desideriamo un sistema di riscaldamento che possa essere acceso solo per pochi minuti, questo non è il sistema di ricompensa ideale. Preferiamo invece un sistema di ricompensa che ci dia una ricompensa uguale per ogni partecipazione. Inoltre, l'importo minimo di prelievo per Braiins Pool è di 100.000 sats e On-Chain. Quindi perdiamo alcuni sats in commissioni di transazione e una parte della nostra ricompensa può essere bloccata se non miniamo abbastanza durante l'inverno.
Il modello di ricompensa che ci interessa è il PPS, che significa "pay-per-share". Ciò significa che il minatore riceverà una ricompensa per ogni condivisione valida. Esiste anche una variante di questo sistema, il FPPS (Full Pay Per Share), che divide non solo la ricompensa della coinbase, ma anche le commissioni di transazione incluse nel blocco. I pool di mining che consigliamo per collegare il tuo mining/riscaldamento sono Linecoin Pool (FPPS) e Nicehash (PPS).

- Nicehash: Il vantaggio di Nicehash è che il prelievo può essere effettuato utilizzando Lightning con commissioni minime. Inoltre, l'importo minimo di prelievo è di 2000 sats. Lo svantaggio è che Nicehash utilizza il suo hashrate per la blockchain più redditizia, senza dare realmente il controllo all'utente e quindi potrebbe non partecipare all'hashrate di Bitcoin.

- Lincoin: Il vantaggio di Linecoin è il numero di funzionalità offerte, come un pannello di controllo dettagliato, la possibilità di effettuare prelievi con un Paynym (BIP 47) per una migliore protezione della privacy e l'integrazione di un bot Telegram e automazioni direttamente configurabili nell'applicazione mobile. Questo pool mina solo blocchi Bitcoin, ma l'importo minimo per il prelievo rimane elevato a 100.000 sats. Esamineremo più nel dettaglio l'interfaccia di uno di questi pool in un prossimo articolo.

Per configurare un pool in Braiins 0S+, sarà necessario creare un account in uno dei pool a tua scelta. Qui prenderemo l'esempio di Lincoin:

![image](assets/software/19.jpeg)

Una volta creato il tuo account, fai clic su "Connect To Pool"

Successivamente, copia l'indirizzo Stratum e il tuo nome utente:

![image](assets/software/20.jpeg)

Ora puoi tornare all'interfaccia di Braiins OS+ per inserire queste credenziali. Per la password, puoi lasciare il campo vuoto.

![image](assets/software/21.jpeg)
## Ottimizzare le prestazioni del proprio Antminer S9
![Ottimizzare le prestazioni del proprio Antminer S9 con l'autotuning](https://www.youtube.com/watch?v=yh8U9Ay1i-E&t=277s)

L'overclocking e l'autotuning consistono entrambi nell'aggiustare le frequenze delle schede di hashing per migliorare le prestazioni dell'ASIC. La differenza tra i due risiede nella complessità di questi settaggi di frequenza.

L'overclocking è un semplice aggiustamento che consiste nell'aumentare la frequenza delle schede di hashing per aumentare il tasso di hashing della macchina. L'underclocking, invece, consiste nel diminuire la frequenza di clock di un circuito integrato al di sotto della sua frequenza nominale. Riducendo la frequenza di clock di un ASIC tramite l'underclocking, si riduce anche il calore generato dall'hardware. Ciò consente di ridurre la velocità dei ventilatori necessari per raffreddare l'ASIC, poiché non devono lavorare così duramente per mantenere una temperatura adeguata. Riducendo la velocità dei ventilatori, si riduce anche il rumore generato dall'ASIC. Ciò può essere particolarmente utile per gli utenti che utilizzano ASIC a casa e cercano di ridurre al minimo le interferenze sonore causate dall'hardware di mining.

Braiins OS+ supporta l'overclocking, l'underclocking degli ASIC e l'autotuning. Consente agli utenti di regolare in modo flessibile la frequenza di clock del proprio hardware per massimizzare le prestazioni o risparmiare energia secondo le proprie preferenze.

### Ottimizzare le prestazioni del proprio Antminer S9 con l'autotuning

Prima del 2018, i minatori avevano due modi per ottenere un vantaggio nella loro attività: trovare elettricità a un costo ragionevole e acquistare hardware più efficiente. Tuttavia, nel 2018 è stata scoperta una nuova avanzata nel campo del software e del firmware di mining, chiamata AsicBoost. Questa tecnica consente ai minatori di ridurre i loro costi di circa il 13% modificando il firmware eseguito sui loro dispositivi.
Oggi c'è un nuovo sviluppo nel settore del software e del firmware minerario chiamato autoregolazione (o autotuning) che offre un vantaggio ancora maggiore rispetto ad AsicBoost. Gli ASIC sono composti da numerosi piccoli chip informatici che eseguono l'hashing. Questi chip sono fatti di silicio, lo stesso elemento ampiamente utilizzato nei semiconduttori e in altri componenti microelettronici. La chiave di comprensione qui è che tutti i chip di silicio non sono identici, ognuno può variare leggermente nelle sue proprietà elettriche. I produttori di hardware lo sanno e pubblicano le specifiche di prestazione delle loro macchine minerarie in base al limite inferiore delle loro tolleranze. In altre parole, i produttori conoscono la frequenza che funziona meglio per i chip medi e utilizzano questa frequenza in modo uniforme per tutti i chip della macchina.

Questo pone un limite superiore alla velocità di hashing che una macchina può avere. L'autoregolazione è un processo in cui gli algoritmi valutano le frequenze ottimali per l'hashing chip per chip, invece di trattare l'intera macchina come un'unica unità. Ciò significa che un chip di migliore qualità che può eseguire più hash al secondo otterrà una frequenza più alta, mentre un chip di qualità inferiore che può eseguire relativamente meno otterrà una frequenza più bassa. L'autoregolazione del chip è essenzialmente un modo per ottimizzare le prestazioni di un ASIC tramite il software e il firmware eseguiti su di esso.

Il risultato finale è una velocità di hashing più elevata per watt di elettricità, il che significa margini di profitto più elevati per i minatori. La ragione per cui le macchine non vengono distribuite con questo tipo di software è che la varianza per macchina non è desiderabile, poiché i clienti vogliono sapere esattamente cosa stanno ottenendo ed è quindi una cattiva idea per i produttori vendere un prodotto che non ha prestazioni costanti e prevedibili da una macchina all'altra. Inoltre, l'autoregolazione del chip richiede considerevoli risorse di sviluppo, poiché è complessa da implementare. I produttori già spendono molte risorse per sviluppare i propri firmware. Ci sono soluzioni software che consentono di implementare l'autotuning, come Braiins OS+. Inoltre, migliora le prestazioni dell'ASIC fino al 20%.

## Controllare un Antminer S9 dal proprio smartphone

### Creare scorciatoie su iOS

![Controllare un Antminer S9 con il proprio smartphone](https://www.youtube.com/watch?v=OsKmdB2iw88&t=60s)
