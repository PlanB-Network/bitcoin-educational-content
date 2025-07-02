---
name: Coinjoin - Dojo
description: Come eseguire un coinjoin con il proprio Dojo
---
![cover](assets/cover.webp)

***ATTENZIONE:** A seguito dell’arresto dei fondatori di Samourai Wallet e del sequestro dei loro server in data 24 aprile 2024, lo strumento Whirlpool ha cessato di funzionare, anche per coloro che utilizzano un nodo personale Dojo o Sparrow Wallet.
Sebbene il servizio sia attualmente inattivo, non si esclude la possibilità che venga ripristinato o rilanciato in una forma diversa nelle prossime settimane.
La parte teorica di questo articolo conserva piena rilevanza per comprendere il funzionamento e gli obiettivi dei CoinJoin in generale, non limitatamente al modello Whirlpool, e analizzare i benefici in termini di privacy offerti da questo approccio.*

_Stiamo monitorando attentamente l'evoluzione di questo caso, così come gli sviluppi riguardanti gli strumenti coinvolti. Il presente tutorial verrà aggiornato non appena saranno disponibili nuove informazioni rilevanti._

_Questo contenuto è fornito esclusivamente a scopo educativo e informativo. Non incoraggiamo né approviamo l'uso di questi strumenti per fini illeciti. Ogni utente è pienamente responsabile del rispetto delle leggi vigenti nella propria giurisdizione._

---

In questo tutorial scoprirai che cos'è un coinjoin e come eseguirne uno utilizzando il software Samourai Wallet e la sua implementazione Whirlpool, attraverso il tuo nodo personale Dojo.
A mio parere, si tratta attualmente del metodo più efficace per migliorare la privacy delle proprie transazioni Bitcoin.

## Cos'è un coinjoin su Bitcoin?
**Il coinjoin è una tecnica che interrompe la tracciabilità dei bitcoin sulla blockchain**. Si basa su una transazione collaborativa con una struttura specifica, chiamata appunto “transazione CoinJoin”.

I coinjoin migliorano la privacy degli utenti Bitcoin rendendo più complessa l’analisi della blockchain da parte di osservatori esterni. La loro struttura consente infatti di unire più input provenienti da diversi utenti in una singola transazione, offuscando i collegamenti tra indirizzi di input e output.

Il principio del coinjoin si fonda sulla collaborazione tra utenti: più persone che desiderano mixare i propri bitcoin forniscono importi identici come input nella stessa transazione. Tali importi vengono poi redistribuiti come output di pari valore.
Alla fine della transazione, diventa impossibile associare con certezza un output a uno degli input originali. In questo modo, viene interrotto il collegamento tra gli utenti e i loro UTXO, così come la cronologia associata a ciascuna moneta.

![coinjoin](assets/notext/1.webp)

Esempio di una transazione coinjoin (non mia): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/it/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Per eseguire un coinjoin in modo che ogni partecipante mantenga sempre il pieno controllo sui propri fondi, il processo inizia con la costruzione della transazione da parte di un coordinatore, che la condivide poi con tutti i partecipanti.
Ogni utente verifica attentamente la transazione e, solo se la ritiene corretta, procede a firmare la propria parte. Una volta raccolte tutte le firme, queste vengono aggregate nella transazione finale.
Nel caso in cui il coordinatore o uno dei partecipanti tenti di alterare la transazione, ad esempio modificando gli output per dirottare fondi, le firme digitali diventeranno invalide. Di conseguenza, la transazione verrà rifiutata dai nodi della rete Bitcoin, impedendo qualsiasi spostamento non autorizzato di fondi.
Esistono diverse implementazioni del protocollo coinjoin, come Whirlpool, JoinMarket e WabiSabi, ognuna con un proprio approccio al coordinamento tra partecipanti e all'efficienza della transazione.
In questo tutorial ci concentreremo su Whirlpool, che ritengo essere oggi la soluzione più efficace per eseguire coinjoin su Bitcoin.
Sebbene Whirlpool sia compatibile con più wallet, ci focalizzeremo esclusivamente sull'utilizzo tramite l'app mobile Samourai Wallet, senza Dojo.

## Perché eseguire coinjoin su Bitcoin?
Uno dei problemi fondamentali nei sistemi di pagamento peer-to-peer è la doppia spesa: come impedire che un individuo malintenzionato spenda gli stessi fondi più di una volta, senza ricorrere a un'autorità centrale che faccia da arbitro?

Satoshi Nakamoto ha risolto questo dilemma introducendo il protocollo Bitcoin, un sistema di pagamento elettronico peer-to-peer che opera in modo completamente decentralizzato. Nel suo white paper, evidenzia che l’unico modo per prevenire la doppia spesa è rendere visibili tutte le transazioni del sistema. In altre parole, per garantire la corretta validazione, tutte le transazioni devono essere pubblicamente diffuse.

Il funzionamento di Bitcoin si basa quindi su un’infrastruttura trasparente e distribuita, in cui chiunque esegua un nodo può verificare autonomamente la catena completa delle firme elettroniche e la storia di ogni moneta, dalla sua creazione da parte di un miner in poi.

Questa trasparenza radicale implica che ogni utente della rete può osservare ed analizzare le transazioni effettuate da altri. Ne consegue che l'anonimato transazionale è, di fatto, impossibile. Tuttavia, Bitcoin garantisce un certo grado di pseudonimato: a differenza del sistema bancario tradizionale, dove i conti sono legati a identità personali, su Bitcoin i fondi sono associati a coppie di chiavi crittografiche, non a nomi o documenti.

La privacy può però essere compromessa nel momento in cui un osservatore riesce ad associare uno specifico UTXO a un'identità. Da lì, è possibile tracciare tutte le attività on-chain di quell'utente e ricostruire la storia dei suoi bitcoin.

Il coinjoin è una tecnica pensata per rompere questa tracciabilità, spezzando i collegamenti diretti tra input e output. In questo modo, offre agli utenti Bitcoin una forma concreta di privacy a livello transazionale.

## Come funziona Whirlpool?
Whirlpool si distingue dagli altri metodi di coinjoin utilizzando transazioni _ZeroLink_, che garantiscono che non ci sia tecnicamente alcun collegamento possibile tra tutti gli input e tutti gli output. Questo perfetto mescolamento è ottenuto attraverso una struttura in cui ogni partecipante contribuisce con un importo identico come input (ad eccezione delle commissioni di mining), generando così output di importi perfettamente uguali.

Questo approccio restrittivo agli input conferisce alle transazioni coinjoin di Whirlpool una caratteristica unica: l'assenza completa di collegamenti deterministici tra gli input e gli output. In altre parole, ogni output ha una probabilità uguale di essere attribuito a qualsiasi partecipante, rispetto a tutti gli altri output nella transazione.

Inizialmente, il numero di partecipanti in ogni coinjoin Whirlpool era limitato a 5, con 2 nuovi ingressi e 3 remixers (spiegheremo questi concetti più avanti). Tuttavia, l’aumento delle commissioni per le transazioni on-chain osservato nel 2023 ha spinto i team di Samourai a ripensare il loro modello per migliorare la privacy riducendo i costi. Pertanto, tenendo conto della situazione relativa al costo delle commissioni e al numero di partecipanti, il coordinatore può ora organizzare coinjoin che includono 6, 7 o 8 partecipanti. Queste sessioni potenziate sono denominate _Cicli di Surge_.

È importante notare che, indipendentemente dalla configurazione, ci sono sempre e solo 2 nuovi entranti (per ogni round di mix) nei coinjoin di Whirlpool.
Pertanto, le transazioni Whirlpool sono caratterizzate da un numero identico di input ed output, che possono essere:

- 5 input e 5 output;
![coinjoin](assets/notext/2.webp)
- 6 input e 6 output;
![coinjoin](assets/notext/3.webp)
- 7 input e 7 output;
![coinjoin](assets/notext/4.webp)
- 8 input e 8 output.
![coinjoin](assets/notext/5.webp)

Il modello proposto da Whirlpool si basa quindi su piccole transazioni coinjoin. A differenza di Wasabi e JoinMarket, dove la robustezza degli anonset dipende dal volume dei partecipanti in un singolo ciclo, Whirlpool punta su una catena di più cicli di dimensioni ridotte.

In questo modello, l’utente paga le commissioni solo al momento del suo ingresso iniziale in un pool, consentendogli di partecipare a numerosi remix senza costi aggiuntivi. Sono infatti i nuovi entranti a coprire le commissioni di mining per i remixers.
Con ogni coinjoin aggiuntivo a cui un UTXO partecipa, insieme ai peer incontrati in precedenza, gli anonset crescono esponenzialmente. L’obiettivo è quindi sfruttare questi remix “gratuiti” che, a ogni mix, contribuiscono ad aumentare la densità degli anonset associati a ciascun UTXO remixato.
Whirlpool è stato progettato tenendo conto di due requisiti fondamentali:
- L’accessibilità su dispositivi mobili, visto che Samourai Wallet è principalmente un’applicazione per smartphone;
- La velocità dei cicli di remixing, indispensabile per favorire un aumento significativo degli anonset.
  
Questi imperativi hanno guidato le scelte degli sviluppatori di Samourai Wallet nella progettazione di Whirlpool, portandoli a limitare il numero di partecipanti per ciclo. Troppi pochi partecipanti avrebbero compromesso l’efficacia del coinjoin, riducendo drasticamente gli anonset generati a ogni ciclo, mentre un numero eccessivo avrebbe creato difficoltà di gestione sulle app mobili e rallentato il flusso delle sessioni.

**In definitiva, non è necessario un elevato numero di partecipanti per ogni coinjoin su Whirlpool, poiché gli anonset si accumulano progressivamente attraverso la partecipazione a più cicli di coinjoin.**

[-> Scopri di più sugli anonset di Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Pool e commissioni nei coinjoin
Affinché questi cicli multipli aumentino efficacemente l'anonset, è necessario stabilire un quadro che limiti le quantità di UTXO utilizzati. Whirlpool definisce quindi diversi pool, o gruppi di utenti.
Una pool rappresenta un insieme di partecipanti che concordano su un importo fisso per gli UTXO da utilizzare, così da ottimizzare il processo di coinjoin. Ogni pool stabilisce un valore specifico a cui gli UTXO devono aderire affinché l’utente possa partecipare.
Per eseguire un coinjoin con Whirlpool, è quindi necessario selezionare una specifica pool tra le seguenti:
- 0,5 bitcoin;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100.000 sats).

Unendoti a una pool con i tuoi bitcoin, questi verranno suddivisi in UTXO perfettamente omogenei a quelli degli altri partecipanti. Ogni pool prevede un limite massimo di partecipazione; pertanto, se il tuo importo supera tale limite, dovrai effettuare due ingressi separati all’interno della stessa pool oppure scegliere una pool diversa con un importo maggiore:

| Pool (bitcoin) | Importo massimo per ingresso (bitcoin) |
|-------------------|----------------------------------------|
| 0,5               | 35                                     |
| 0,05              | 3,5                                    |
| 0,01              | 0,7                                    |
| 0,001             | 0,025                                  |

Come accennato in precedenza, un UTXO è considerato appartenente a una pool quando è pronto per essere incluso in un coinjoin. Tuttavia, ciò non implica che l’utente perda il controllo su di esso. **Attraverso i diversi cicli di mix, mantieni il pieno controllo delle tue chiavi e, di conseguenza, dei tuoi bitcoin.** Questo è ciò che differenzia la tecnica del coinjoin da altre tecniche di mixing centralizzate.

Per entrare in una pool di coinjoin, è necessario pagare sia le commissioni di servizio sia le commissioni di mining.
Le commissioni di servizio sono fisse per ogni pool e servono a compensare i team responsabili dello sviluppo e della manutenzione di Whirlpool.
Queste commissioni devono essere pagate una sola volta, al momento dell’ingresso nella pool e, dopo questo passaggio, potrai partecipare a un numero illimitato di remix senza costi aggiuntivi.
Di seguito, le commissioni fisse attualmente applicate per ciascuna pool:

| Pool (bitcoin) | Commissione di ingresso (bitcoin) |
| -------------- | --------------------------------- |
| 0,5            | 0,0175                            |
| 0,05           | 0,00175                           |
| 0,01           | 0,0005 (50 000 sats)              |
| 0,001          | 0,00005 (5 000 sats)              |


Queste commissioni funzionano sostanzialmente come un biglietto d’ingresso per la pool scelta, indipendentemente dall’importo che decidi di utilizzare nel coinjoin.
In altre parole, sia che tu entri nella pool da 0,01 BTC con esattamente 0,01 BTC, sia che tu vi acceda con 0,5 BTC, la commissione resterà invariata in termini assoluti.

Prima di procedere ai coinjoin, puoi scegliere tra due strategie:

- Optare per una pool più piccola, così da ridurre le commissioni di servizio, sapendo però che riceverai in cambio più UTXO di importo minore;
- Scegliere una pool più grande, accettando commissioni più alte, ma ottenendo meno UTXO, ciascuno di valore maggiore.

Generalmente, è sconsigliato unire diversi UTXO mixati dopo i cicli di coinjoin, poiché ciò potrebbe compromettere la privacy acquisita, riducendo anche la riservatezza degli altri partecipanti al coinjoin, a causa dell’Euristica di Proprietà Comune dell’Input (CIOH).
Per questo motivo, può essere più prudente scegliere fin da subito una pool più grande, anche a costo di commissioni più elevate, per evitare di generare troppi UTXO di piccolo valore in uscita.
Valuta attentamente questi compromessi per selezionare la pool più adatta alle tue esigenze.

Oltre alle commissioni di servizio, devi considerare anche le commissioni di mining inerenti a qualsiasi transazione Bitcoin. Come utente di Whirlpool, dovrai pagare le commissioni di mining per la transazione di preparazione (`Tx0`) così come quelle per il primo coinjoin. Tutti i remix successivi saranno gratuiti, grazie al modello di Whirlpool basato sulle spese dei nuovi partecipanti.

Infatti, in ogni coinjoin eseguito tramite Whirlpool, due utenti tra tutti gli input sono nuovi partecipanti, mentre gli altri input provengono da remixer, ovvero utenti che hanno già preso parte a un mix precedente.
Le commissioni di mining dell’intera transazione sono quindi interamente sostenute dai due nuovi entranti, che in cambio ottengono l’accesso a remix successivi senza dover pagare ulteriori commissioni.

![coinjoin](assets/it/6.webp)

Grazie a questo sistema di commissioni, Whirlpool si distingue davvero da altri servizi di coinjoin, poiché il livello di anonimato raggiunto (anonset) non è proporzionale al costo sostenuto dall’utente.
È quindi possibile ottenere un’elevata privacy pagando soltanto la commissione d’ingresso nella pool, oltre alle commissioni di mining per due transazioni: la `Tx0` e il primo mix.
Va sottolineato che, al termine dei cicli di coinjoin, l’utente dovrà comunque coprire le commissioni di mining necessarie per prelevare i propri UTXO dalla pool, a meno che non abbia attivato l’opzione `mix to`, che verrà spiegata più avanti in questo tutorial.

### Gli account del portafoglio HD utilizzati da Whirlpool
Per eseguire un coinjoin tramite Whirlpool, il portafoglio deve generare diversi account distinti. Un account, nel contesto di un portafoglio HD (*Hierarchical Deterministic*), costituisce una sezione completamente isolata dalle altre, questa scissione avviene al terzo livello di profondità della gerarchia del portafoglio, ovvero a livello dell'`xpub`.

Un portafoglio HD può teoricamente derivare fino a `2^(32/2)` account diversi. L'account iniziale, utilizzato di default su tutti i portafogli Bitcoin, corrisponde all'indice `0'`.

Per i portafogli idonei a Whirlpool, come Samourai o Sparrow, vengono utilizzati 4 account per soddisfare le esigenze del processo di coinjoin:
- L'account **deposito**, identificato dall'indice `0'`;
- L'account **bad bank** (o cambio tossico), identificato dall'indice `2 147 483 644`;
- L'account **premix**, identificato dall'indice `2 147 483 645`;
- L'account **postmix**, identificato dall'indice `2 147 483 646`.

Ognuno di questi account svolge una funzione specifica all'interno del coinjoin.

Tutti questi account sono collegati a un unico seed, il quale permette all’utente di recuperare l’accesso a tutti i propri bitcoin utilizzando la frase di recupero e, se impostata, la passphrase.
Tuttavia, durante il processo di ripristino, è necessario indicare al software gli indici degli account effettivamente utilizzati, affinché possa derivare correttamente tutti gli address e UTXO associati.

Ora esaminiamo le diverse fasi di un coinjoin Whirlpool all'interno di questi account.

### Le diverse fasi dei coinjoin su Whirlpool
**Fase 1: La `Tx0`**
Il punto di partenza di qualsiasi coinjoin Whirlpool è l’account **deposito**. È l’account utilizzato automaticamente alla creazione di un nuovo wallet Bitcoin e deve essere finanziato con i bitcoin che si desidera mixare.
La `Tx0` rappresenta il primo passaggio del processo di mixing con Whirlpool. Serve a preparare e omogeneizzare gli UTXO per il coinjoin, suddividendoli in unità corrispondenti all’importo della pool selezionata. Questo passaggio garantisce l’uniformità necessaria per il mixing. Gli UTXO così omogeneizzati vengono poi inviati all’account **premix**.
L’eventuale eccedenza non compatibile con la pool viene invece separata e inviata a un account dedicato chiamato **bad bank** (o “cambio tossico”).
Questa transazione iniziale `Tx0` include anche il pagamento della commissione di servizio destinata al coordinatore del mix. A differenza delle fasi successive, si tratta di una transazione non collaborativa, e l’utente deve farsi carico per intero delle relative commissioni di mining.

![coinjoin](assets/it/7.webp)

In questo esempio di transazione Tx0, un input di `372.000 sats` proveniente dal nostro account deposito viene suddiviso in diversi UTXO di output, così distribuiti:

- `5.000 sats` sono destinati al coordinatore come commissione di servizio, corrispondenti all’ingresso nella pool da `100.000 sats`;
- Tre UTXO omogeneizzati da `108.000 sats` ciascuno, preparati per il mixing e inviati al nostro account **premix**, con la relativa registrazione presso il coordinatore. Questi importi coprono anche le future commissioni di mining del mix iniziale;
- Un eccedenza troppo piccola per entrare nella pool, definita “cambio tossico”, pari a `40.000 sats`, che viene inviata al relativo account dedicato;
- Infine, `3.000 sats` rappresentano le commissioni di mining necessarie per confermare la `Tx0`.

Ad esempio, ecco un vero Whirlpool `Tx0` (non mio): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/it/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Fase 2: Il cambio tossico**
L’eccedenza che non può essere integrata nel pool, in questo caso pari a `40.000 sats`, viene indirizzata all’account **bad bank**, noto anche come “cambio tossico”, per garantire una netta separazione dagli altri UTXO nel portafoglio. Questo UTXO rappresenta un rischio per la privacy dell’utente, perché non solo è ancora collegato al suo storico, e quindi potenzialmente all’identità del proprietario, ma risulta anche evidente a un osservatore esterno come appartenente a un utente che ha effettuato un coinjoin.
Se questo UTXO viene combinato con output mixati, gli output perderanno tutta la riservatezza acquisita nei cicli di coinjoin, soprattutto a causa della Common-Input-Ownership Heuristic (CIOH). Se invece viene unito ad altri "cambi tossici", l’utente rischia di compromettere la privacy collegando tra loro diversi input di coinjoin. Per questo motivo, deve essere gestito con estrema attenzione.
La gestione di questo UTXO “tossico” sarà approfondita nella parte finale di questo articolo; inoltre, futuri tutorial su Plan ₿ Network tratteranno questi metodi in modo più dettagliato.

**Passo 3: Il Mix Iniziale**
Una volta completata la Tx0, gli UTXO equalizzati vengono trasferiti al conto **premix** del wallet, pronti per essere utilizzati nel loro primo ciclo di coinjoin, chiamato anche “mix iniziale”. Nel caso del nostro esempio, se la `Tx0` genera più UTXO destinati al mixing, ciascuno verrà inserito in un coinjoin iniziale separato.

Al termine di questi primi mix, il conto **premix** risulterà vuoto, mentre gli UTXO, avendo coperto le commissioni di mining di questo primo coinjoin, saranno esattamente dell’importo previsto dalla pool scelta. Nel nostro esempio, gli UTXO iniziali da `108.000 sats` saranno quindi stati ridotti a `100.000 sats` ciascuno.

![coinjoin](assets/it/8.webp)

**Passo 4: I Remix**
Dopo il mix iniziale, gli UTXO vengono trasferiti al conto **postmix**. Questo conto raccoglie gli UTXO già mescolati e quelli in attesa di remix. Quando il client Whirlpool è attivo, gli UTXO in **postmix** sono automaticamente disponibili per il remix e vengono selezionati casualmente per partecipare a nuovi cicli di coinjoin.
Ricorda che i remix sono completamente gratuiti: non sono richieste commissioni di servizio aggiuntive né commissioni di mining. Mantenere gli UTXO nel conto postmix preserva quindi il loro valore e aumenta contemporaneamente il loro anonset. Per questo motivo, è importante lasciare che questi UTXO partecipino a più cicli di coinjoin. Non ti costa nulla e migliora la loro privacy.

Quando decidi di spendere UTXO mescolati, puoi farlo direttamente dal conto **postmix**. Si consiglia di mantenere gli UTXO mescolati in questo conto per beneficiare dei remix gratuiti e per evitare che escano dal circuito Whirlpool, riducendo così la loro privacy.
Come vedremo nel tutorial seguente, esiste anche l’opzione `mix to`, che consente di inviare automaticamente le monete mescolate a un altro wallet, come un cold wallet, dopo un numero definito di coinjoin.

Dopo aver esaminato la teoria, passiamo alla pratica con un tutorial sull’uso di Whirlpool tramite l’app Android Samourai Wallet, sincronizzata con Whirlpool CLI e GUI sul tuo Dojo personale!

## Tutorial: Coinjoin Whirlpool con il Tuo Dojo
Ci sono molte opzioni per utilizzare Whirlpool. In questo tutorial presenterò l’opzione Samourai Wallet, un’applicazione open-source per la gestione di portafogli Bitcoin su Android, utilizzata insieme al proprio Dojo.

Eseguire coinjoin tramite Samourai Wallet collegato al proprio Dojo è, a mio avviso, la strategia più efficace per fare coinjoin su Bitcoin ad oggi. Questo approccio richiede un investimento iniziale di tempo in termini di configurazione, ma una volta impostato, consente di mixare e remixare i propri bitcoin in modo continuo, 24/7, non dovendo avere l’app Samourai sempre attiva. Infatti, grazie a Whirlpool CLI che gira su un nodo Bitcoin, sei sempre pronto a partecipare ai coinjoin. L’app Samourai permette invece di spendere i fondi mixati in qualsiasi momento e ovunque, direttamente dal tuo smartphone. Inoltre, con questo metodo non ti connetti a server gestiti da terzi, preservando così la `xpub` da qualsiasi esposizione esterna.

Questa tecnica è ideale per chi cerca la massima privacy e cicli di coinjoin più efficaci, ma richiede di avere un nodo Bitcoin e una configurazione non banale; per questo motivo è più adatta a utenti intermedi o avanzati. Per i principianti, invece, consiglio prima di familiarizzare con i coinjoin attraverso questi altri due tutorial che mostrano come farlo usando Sparrow Wallet o Samourai Wallet (senza Dojo):

- **[Tutorial coinjoin di Sparrow Wallet](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- **[Tutorial coinjoin di Samourai Wallet (senza Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.

### Comprendere la Configurazione
Per iniziare, avrai bisogno di un Dojo! Il Dojo è un'implementazione di un nodo Bitcoin basata su Bitcoin Core, sviluppata dai team di Samourai.

Per eseguire il proprio Dojo, hai l'opzione di installare autonomamente un nodo Dojo, o di sfruttare Dojo su un'altra soluzione di nodo Bitcoin "node-in-box". Attualmente, le opzioni disponibili sono:
- [RoninDojo](https://ronindojo.io/), che è un Dojo arricchito con strumenti aggiuntivi, inclusi un assistente di installazione e un assistente di amministrazione. Dettaglio la procedura per configurare e utilizzare RoninDojo in questo altro tutorial: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) con l'applicazione "Samourai Server";
- [MyNode](https://mynodebtc.com/) con l'applicazione "Dojo";
- [Nodl](https://www.nodl.eu/) con l'applicazione "Dojo";
- [Citadel](https://runcitadel.space/) con l'applicazione "Samourai".
![coinjoin](assets/notext/9.webp)
Nella nostra configurazione, interagiremo con tre interfacce distinte:
- **Samourai Wallet**, che ospiterà il nostro portafoglio Bitcoin dedicato ai coinjoin. Disponibile gratuitamente su Android, questa applicazione FOSS ti consente di controllare il tuo portafoglio di mixing, specialmente per spendere i tuoi postmix UTXO dal tuo smartphone;
- **Whirlpool CLI** (_Interfaccia a Linea di Comando_), che opererà sul nodo che ospita il Dojo. Questo software avrà accesso alle chiavi del tuo portafoglio Samourai. È responsabile della comunicazione con il coordinatore e della gestione continua dei coinjoin. Agisce come una copia del tuo portafoglio Samourai sul tuo nodo, pronto a partecipare ai coinjoin in qualsiasi momento;
- **Whirlpool GUI** (_Interfaccia Grafica Utente_), l'interfaccia grafica che useremo per monitorare l'attività di Whirlpool CLI e avviare il mixing da remoto. Whirlpool GUI fornisce una rappresentazione visiva delle operazioni condotte da Whirlpool CLI. Questo software deve essere installato su un computer separato dal Dojo. Per gli utenti di Umbrel, MyNode, Nodl e Citadel, Whirlpool GUI è obbligatorio. Tuttavia, con RoninDojo, l'interfaccia Whirlpool GUI è già integrata nell'interfaccia web del tuo nodo tramite l'applicazione `Whirlpool`. Pertanto, non sarà necessario installarla su un PC separato.

A mio parere, utilizzare RoninDojo rappresenta la soluzione migliore per eseguire coinjoin con un Dojo. Poiché questo software nodo-in-box è in partnership diretta con i team di Samourai, RoninDojo è molto più ottimizzato per fare ciò. Inoltre, l'integrazione di Whirlpool GUI nell'interfaccia web semplifica notevolmente il processo di configurazione. In questo tutorial, spiegherò comunque come farlo con le altre soluzioni che integrano Dojo (Umbrel, Nodl, MyNode e Citadel).

### Preparare il Tuo Dojo
Per iniziare, dovrai installare Dojo ed ottenere il codice QR o il link che ti permetterà di connetterti ad esso da remoto. Questo link è un indirizzo Tor che termina in `.onion`. Se stai utilizzando RoninDojo, semplicemente naviga nel menu `Pairing` per accedere a queste informazioni.
![coinjoin](assets/notext/10.webp)
Sotto `Samourai Dojo`, clicca sul pulsante `Pair now`.
![coinjoin](assets/notext/11.webp)
Il tuo codice QR di connessione e il link corrispondente verranno visualizzati.
![coinjoin](assets/notext/12.webp)
Se sei su Umbrel, vai all'App Store e cerca l'applicazione `Samourai Server`. Si trova nella scheda `Bitcoin`.
![coinjoin](assets/notext/13.webp)
Installa l'applicazione.
![coinjoin](assets/notext/14.webp)
All'apertura dell'applicazione, avrai quindi accesso al codice QR per connetterti al tuo Dojo.
![coinjoin](assets/notext/15.webp)
Se stai utilizzando un altro software nodo-in-box come MyNode, Citadel o Nodl, il processo è simile a quello di Umbrel. Devi installare l'applicazione Samourai o Dojo per ottenere le informazioni necessarie per connetterti al tuo Dojo.
![coinjoin](assets/notext/16.webp)
### Preparare il Tuo Portafoglio Samourai
Dopo aver recuperato le informazioni di connessione al tuo Dojo, è ora il momento di configurare il tuo portafoglio per i coinjoin. Ci sono due scenari: se non hai ancora un Portafoglio Samourai sul tuo smartphone, il processo è semplice, basta crearne uno nuovo.
D'altra parte, se possiedi già un Samourai Wallet, dovrai reinstallare l'applicazione per associarla ad un nuovo Dojo. Questo passaggio è necessario perché la connessione a un Dojo può essere stabilita solo al primo avvio dell'applicazione. Tuttavia, grazie al file di backup crittografato generato automaticamente da Samourai sul tuo telefono, questa procedura è semplice e veloce.
*Se non hai mai usato Samourai, puoi saltare questi passaggi preliminari e procedere direttamente all'installazione dell'applicazione.*

Prima di tutto, assicurati che la tua applicazione Samourai Wallet sia aggiornata. Per fare ciò, controlla il Google Play Store o confronta la versione della tua applicazione in `Impostazioni > Altro` con quella disponibile sul sito web di Samourai.

![coinjoin](assets/notext/17.webp)

Assicurati di avere la tua frase di recupero del portafoglio Samourai e che sia leggibile. Quindi, esegui un test della tua passphrase BIP39 navigando in `Impostazioni > Risoluzione dei problemi > Test passphrase/backup` per confermarne l'accuratezza.

![coinjoin](assets/notext/18.webp)
Inserisci la tua passphrase, poi verifica che Samourai ne confermi la validità.
![coinjoin](assets/notext/19.webp)

Se la tua passphrase è invalida, o se non hai la tua frase di recupero, è imperativo interrompere immediatamente la procedura! **Rischi di perdere i tuoi bitcoin durante questa operazione.** In questo caso, si consiglia di trasferire i tuoi fondi in un altro portafoglio e iniziare con un nuovo Samourai wallet vuoto. I passaggi seguenti dovrebbero essere seguiti solo se sei certo di avere tutte le informazioni di backup necessarie e che la tua passphrase sia valida.

Procedi quindi con la creazione di un backup crittografato del tuo portafoglio e copialo negli appunti. Per eseguire questa operazione, clicca sui tre piccoli punti situati in alto a destra dello schermo, poi seleziona `Esporta backup del portafoglio`.

![coinjoin](assets/notext/20.webp)

**Da questo passaggio in poi, non copiare altro negli appunti!** È assolutamente essenziale che tu mantenga il tuo backup copiato.

Se hai eseguito correttamente i passaggi precedenti, ora sei in grado di eliminare in sicurezza il tuo Samourai wallet. Per fare ciò, vai su: `Impostazioni > Portafoglio > Cancellazione sicura del portafoglio`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Se non hai mai usato Samourai e stai installando l'applicazione da zero, puoi riprendere il tutorial da questo passaggio.*

La tua applicazione Samourai è ora resettata. Apri l'applicazione e procedi con i passaggi di configurazione come se la stessi usando per la prima volta.

![coinjoin](assets/notext/23.webp)

Nel passaggio successivo, accederai alla pagina dedicata alla configurazione del tuo Dojo. Seleziona l'opzione `Dojo`, poi inserisci le informazioni di accesso del tuo Dojo. Per fare ciò, hai l'opzione di scansionare le informazioni premendo `Scansiona QR`.

![coinjoin](assets/notext/24.webp)

*Per i nuovi utenti di Samourai, sarà quindi necessario creare un portafoglio da zero. Se hai bisogno di assistenza, puoi consultare le istruzioni per configurare un nuovo portafoglio Samourai [in questo tutorial, specificamente nella sezione "Creazione di un portafoglio software"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*

Se stai procedendo con il ripristino di un portafoglio Samourai già esistente, seleziona `Ripristina portafoglio esistente`, poi scegli `Ho un file di backup di Samourai`.
Normalmente, dovresti sempre avere il tuo file di recupero negli appunti. Quindi clicca su `PASTE` per inserire il tuo file nella posizione designata. Per decifrarlo, sarà inoltre necessario inserire la passphrase BIP39 del tuo portafoglio nel campo corrispondente, situato appena sotto. Per finire, clicca su `FINISH`. ![coinjoin](assets/notext/26.webp)

Verrai quindi reindirizzato al tuo Samourai Wallet che, questa volta, sarà connesso al tuo Dojo personale.

![coinjoin](assets/notext/27.webp)

### Installazione di Whirlpool GUI
È ora il momento di installare Whirlpool GUI, l'interfaccia grafica che ti permetterà di gestire i tuoi cicli di coinjoin dal tuo PC abituale. Per gli utenti di RoninDojo, questo passaggio non è necessario poiché la gestione dei coinjoin può essere effettuata direttamente tramite l'interfaccia web in `Apps > Whirlpool`. Tuttavia, se stai utilizzando un'altra soluzione "node-in-box" per Bitcoin, è imperativo procedere con questa installazione.
![coinjoin](assets/notext/28.webp)
Vai sul tuo computer personale e scarica il software Whirlpool dal sito ufficiale di Samourai Wallet, selezionando la versione che corrisponde al tuo sistema operativo.

![coinjoin](assets/notext/29.webp)

Prima di avviare Whirlpool GUI, è necessario installare JAVA 8 o una versione superiore sulla tua macchina. Per questo, [puoi installare OpenJDK](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
È inoltre necessario avere Tor Daemon o Tor Browser operativo in background sul tuo computer. Assicurati di avviare Tor prima di ogni sessione di utilizzo di Whirlpool GUI. Se Tor non è ancora installato sulla tua macchina, [puoi scaricarlo e installarlo dal sito ufficiale del progetto](https://www.torproject.org/download/), poi assicurati di avviarlo in background.

![coinjoin](assets/notext/31.webp)

Una volta che JDK è installato sul tuo sistema e Tor è avviato in background, puoi avviare Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

Da Whirlpool GUI, clicca su `Advanced: Remote CLI` per connettere il tuo Whirlpool CLI che si trova sul tuo Dojo. Avrai bisogno dell'indirizzo Tor del tuo Whirlpool CLI.

![coinjoin](assets/notext/33.webp)

Per localizzare il tuo indirizzo Tor su Umbrel e altre soluzioni "node-in-box", basta avviare l'applicazione Samourai Server o Dojo (il nome può variare a seconda del software utilizzato). L'indirizzo Tor sarà direttamente visibile sulla pagina dell'applicazione.
![coinjoin](assets/notext/34.webp)
In Whirlpool GUI, inserisci l'indirizzo Tor che hai ottenuto in precedenza nel campo `CLI address`. Mantieni il prefisso `http://`, ma non aggiungere la porta `:8899` alla fine. Incolla solo l'indirizzo così come ti è stato fornito.
![coinjoin](assets/notext/35.webp)

Nel campo Tor Proxy, inserisci `socks5://127.0.0.1:9050` se stai utilizzando Tor Daemon, o `socks5://127.0.0.1:9150` se si tratta di Tor Browser (in questo caso ricordati di avviare Tor Browser). Quando ti connetti per la prima volta a Whirlpool CLI tramite Whirlpool GUI, è possibile lasciare vuoto il campo della chiave API. Se questa non è la tua prima connessione, inserisci la tua chiave API nello spazio dedicato. Questa chiave può essere localizzata sulla stessa pagina del tuo indirizzo Tor.
Una volta compilato tutto, clicca sul pulsante `Connect`. Si prega di attendere, la connessione potrebbe richiedere alcuni minuti.

### Associare il tuo Samourai Wallet con Whirlpool GUI
*Per gli utenti RoninDojo, potete riprendere il tutorial da qui.*

Ora assoceremo il portafoglio Samourai che abbiamo configurato in precedenza con il software Whirlpool GUI, o direttamente con RoninDojo per coloro che utilizzano questo software. Che tu stia usando Whirlpool GUI o RoninDojo, ti verrà chiesto di incollare o scansionare le informazioni di associazione del tuo portafoglio Samourai.

Per trovare queste informazioni, vai nelle impostazioni del tuo portafoglio.

Clicca su `Transazioni`, poi su `Associa a Whirlpool GUI`.

Samourai ti fornirà quindi le informazioni necessarie per stabilire la connessione. Attenzione, questi dati sono sensibili! Puoi trasferirli al tuo PC copiandoli direttamente o scansionando il codice QR visualizzato, utilizzando la webcam del tuo computer dopo aver cliccato sull'icona del codice QR.

Dopo aver eseguito questa operazione, in Whirlpool GUI, seleziona `Inizializza GUI`. Si prega di attendere, poiché questo passaggio potrebbe richiedere un momento.

Che tu stia usando Whirlpool GUI o RoninDojo, ti verrà chiesto di inserire la passphrase del tuo portafoglio Samourai. Inseriscila nel campo dedicato, poi premi il pulsante `Login` per continuare.

Arriverai quindi alla homepage di Whirlpool CLI

### Avviare coinjoin da Whirlpool GUI
*Per gli utenti RoninDojo, il processo da seguire è identico. L'interfaccia dell'app Whirlpool integrata in RoninDojo offre le stesse opzioni e funzionalità del software Whirlpool GUI su desktop. Pertanto, puoi seguire queste istruzioni allo stesso modo.*
Ora che tutto è configurato, sei pronto per iniziare a mixare i tuoi bitcoin. Per fare ciò, trasferisci i bitcoin che desideri mixare nel conto **Deposito** del tuo Samourai Wallet. Questa operazione può essere effettuata direttamente tramite l'app Samourai Wallet o su Whirlpool GUI. Dalla pagina principale, clicca sul pulsante `+ Deposito` situato in alto a sinistra.

Whirlpool GUI genererà un indirizzo di ricezione. Mostrerà anche l'importo minimo necessario per partecipare a ciascuna pool di coinjoin. Questo importo varia a seconda del mercato delle commissioni. È consigliabile depositare un importo leggermente superiore al minimo richiesto, poiché se le commissioni di mining non diminuiscono, il tuo UTXO potrebbe non essere accettato nella pool desiderata. Pertanto, invia i tuoi bitcoin all'indirizzo fornito. Per ottenere un nuovo indirizzo, basta cliccare sul pulsante `Rinnova indirizzo`.

Una volta confermato il deposito, potrai vederlo apparire nel conto **Deposito** su Whirlpool GUI.
Per avviare i cicli di coinjoin, seleziona gli UTXO che desideri mixare e premi il pulsante `Premix`. Fai attenzione: se selezioni diversi UTXO contemporaneamente, verranno combinati durante la transazione di preparazione `TX0`. Questa fusione può portare a una diminuzione della privacy, specialmente se gli UTXO provengono da fonti diverse, a causa dell'Euristica di Proprietà Comune dell'Input (CIOH).
![coinjoin](assets/notext/48.webp)

Si apre la pagina di configurazione di Whirlpool. Puoi scegliere la pool in cui desideri entrare. Seleziona anche le commissioni di mining dedicate al `TX0` e ai primi coinjoin. In fondo a questa pagina, un riassunto ti presenterà l'importo del resto tossico così come l'importo e il numero di UTXO che verranno equalizzati ed inclusi nei cicli di coinjoin. Se sei soddisfatto di questa configurazione, premi il pulsante `Premix` per avviare i cicli di coinjoin.
![coinjoin](assets/notext/49.webp)

Una volta creato il `TX0`, potrai vedere i tuoi UTXO equalizzati nell'account **Premix**, in attesa di conferma. Per permettere ai tuoi coin di essere remixati automaticamente 24 ore su 24, 7 giorni su 7, ti consiglio di attivare l'opzione `Automatically mix premix & postmix`. Troverai questa funzionalità nella scheda `Configuration`, situata a sinistra della tua finestra GUI di Whirlpool.
![coinjoin](assets/notext/50.webp)
Dopo aver avviato i coinjoin, puoi uscire da Whirlpool GUI così come da Samourai Wallet. Solo il tuo nodo deve rimanere connesso per poter partecipare ai coinjoin continui. Tuttavia, è consigliabile controllare periodicamente il progresso dei tuoi cicli di coinjoin. Se noti che i tuoi UTXO non vengono più selezionati per un coinjoin da un po' di tempo, ciò potrebbe indicare un bug. In questo caso, vai su Whirlpool CLI e seleziona `Start` per riavviare la tua disponibilità per i coinjoin.

![coinjoin](assets/notext/51.webp)

I tuoi UTXO mixati sono visibili dall'account **Postmix** su Whirlpool GUI. Inoltre, hai l'opzione di visualizzarli e spenderli direttamente tramite l'interfaccia Whirlpool sul tuo Samourai Wallet. Per accedere a questo menu, clicca sul `+` blu in fondo al tuo schermo, poi seleziona `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Gli account Whirlpool sono facilmente identificabili su Samourai Wallet dal loro colore blu. Questo ti permette di spendere i tuoi UTXO mixati da qualsiasi luogo e in qualsiasi momento, direttamente dal tuo smartphone.

![coinjoin](assets/notext/53.webp)

Per tenere traccia dei tuoi coinjoin automatici, ti consiglio anche di configurare un portafoglio solo visualizzazione tramite l'app Sentinel. Aggiungi lo ZPUB del tuo account **Postmix** e monitora il progresso dei tuoi cicli di coinjoin in tempo reale. Se vuoi capire come usare Sentinel, ti consiglio di consultare questo altro tutorial su PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)




