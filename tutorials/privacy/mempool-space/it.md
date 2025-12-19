---
nome: Mempool
descrizione: Esplorate l'intero ecosistema Bitcoin.
---

![cover](assets/cover.webp)



Il protocollo Bitcoin è una rete pseudonima, decentralizzata e aperta alla consultazione. I membri (nodi), cioè i computer che possiedono un'istanza del software Bitcoin, hanno accesso illimitato a tutti i dati pubblicati su Bitcoin. Tuttavia, nei primi anni di vita di Bitcoin, il protocollo non era così ampiamente accessibile come lo è oggi.


Nei primi tempi di Bitcoin, era necessario far funzionare un nodo Bitcoin per poter accedere agli strumenti appropriati (bitcoin-cli) per interrogare la rete da terminale.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Per qusto, sono stati avviati dei progetti per espandere la comunità Bitcoin, rendendola più accessibile a tutti coloro che non possiedono un nodo e/o non hanno le competenze tecniche necessarie.



In questa esercitazione esamineremo il progetto **Mempool.space**, le sue caratteristiche e l'impatto che ha avuto sull'ecosistema Bitcoin.



## Che cos'è Mempool.space?



**Mempool.space** è un explorer open-source che fornisce informazioni utili sulle transazioni, sulle tariffe delle transazioni, sui blocchi e sui miner delle varie reti del protocollo Bitcoin. Lanciato nel 2020, migliora notevolmente l'esperienza dell'utente grazie ad una grafica rappresentativa, ad animazioni fluide ed interfacce semplici.



Per comprendere il progetto, la Mempool (pool di memoria) è uno spazio virtuale in cui vengono memorizzate tutte le transazioni in attesa di conferma sulla rete Bitcoin. La Mempool è come una "sala d'attesa" dove le transazioni Bitcoin attendono di essere confermate. Ogni computer della rete (nodo) ha la propria sala d'attesa, ciò spiega perché non tutte le transazioni sono visibili a tutti nello stesso momento.



L'impatto principale della piattaforma Mempool.space nell'ecosistema Bitcoin è che consente di accedere alle varie informazioni presenti nelle aree di memoria della maggior parte dei nodi presenti su Bitcoin, senza doverne eseguire uno. Mempool.space è un archivio per la visualizzazione e la ricerca di reti di protocollo Bitcoin.



Essendo open source, Mempool.space ha visto una crescente diffusione nell'ecosistema, facilitando la sua integrazione in un numero sempre maggiore di sistemi di hosting personali. Ora è possibile avere una propria istanza di Mempool.space direttamente sul proprio nodo personale. Guarda il nostro tutorial su come configurare Mempool.space sul tuo nodo Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## I fondamenti di Mempool.space



Come già accennato, [Mempool.space](https://Mempool.space) è un explorer di protocolli Bitcoin che consente di monitorare, da un'interfaccia grafica, le transazioni e la loro propagazione sulla rete Bitcoin in tempo reale.



Mempool.space supporta molte reti del protocollo Bitcoin.


Nella barra dei menù si trovano le seguenti reti:




- **Mainnet**: la rete Bitcoin principale dove avvengono le transazioni Bitcoin reali;
- **Signet**: una rete di prova che utilizza le firme digitali per convalidare i blocchi senza richiedere le risorse necessarie alla rete principale;
- **Testnet 3**: una rete di test e sviluppo priva di rischi sul protocollo Bitcoin;
- **Testnet 4**: la nuova versione di Testnet 3, apporta maggiore stabilità e nuove regole di consenso all'ambiente di test.



![reseaux](assets/fr/01.webp)



Sulla home page, a sinistra in verde, vedrai i possibili futuri blocchi (gruppi di transazioni) pronti per essere convalidati e integrati (minati) nella rete Bitcoin. In media, un blocco viene minato ogni dieci minuti: conservate questa informazione, perché vi tornerà utile più avanti.


In viola, sul lato destro, troverete i recenti blocchi minati su Bitcoin, con il numero dell'ultimo blocco minato che rappresenta l'altezza attuale della rete.



![blocs](assets/fr/02.webp)



La sezione **Transaction Fees** è una stima delle commissioni di transazione. Più alte sono le commissioni assegnate alla transazione, più è probabile che la transazione venga aggiunta al blocco successivo pronto per essere minato.


Le commissioni di transazione rappresentano il costo che un miner richiede all'utente per inserire la sua transazione in un blocco candidato per il mining. La commissione è definita da un rapporto sat/vB (Satoshi/Virtual Bytes) che rappresenta il numero di satoshi pagati per lo spazio che la transazione occuperà nel blocco candidato.



⚠️ IMPORTANTE: in caso di saturazione della Mempool, i miner danno priorità alle transazioni che offrono il miglior rapporto Satoshi/vByte. Più pesante (grande) è la transazione, più satoshi saranno necessari per essere inclusi rapidamente.



![fees-visualizer](assets/fr/03.webp)



La sezione **Mempool Goggles** consente di visualizzare lo spazio occupato da una transazione.



![mempool](assets/fr/04.webp)



Un blocco viene minato ogni dieci minuti circa a causa della difficoltà della Proof Of Work che i miner devono fornire per aggiungere il loro blocco candidato alla catena di blocchi minati. Questa difficoltà varia ogni **2016 blocchi**, equivalente a circa **2 settimane**. È possibile vedere l'evoluzione di questa difficoltà qui.



![difficulty](assets/fr/05.webp)



L'aggiunta di un nuovo blocco alla catena principale dà diritto al miner del blocco convalidato a una ricompensa composta da una parte fissa (dimezzata ogni 210.000 blocchi, **equivalente a circa 4 anni** ) e dalle commissioni delle transazioni.



![halving](assets/fr/06.webp)



## Accedi ai dettagli delle tue transazioni



Nella barra di ricerca di Mempool.space, è possibile inserire il proprio indirizzo Bitcoin o il proprio ID della transazione per ottenere ulteriori informazioni sulla tua cronologia.


![search](assets/fr/07.webp)



Nella pagina dei dettagli della transazione si trovano informazioni generali sulla transazione:




- **stato**: confermato quando viene aggiunto a un blocco, non confermato quando è in attesa nella Mempool;
- **spese di transazione**;
- **Estimated Time of Arrival, ETA (tempo stimato di arrivo)**: il tempo approssimativo necessario affinché la transazione venga aggiunta ad un blocco. Il calcolo si basa sulla proporzione tra queste commissioni.



![general-txinfo](assets/fr/08.webp)



La sezione **Flow** mostra un grafico dei componenti della transazione.



Gli input (UTXO precedenti) utilizzati nella tua transazione, insieme agli output, conferiscono ai destinatari il diritto di utilizzare i bitcoin contenuti in ciascun output, presentando la firma necessaria per poterli spendere.



![flow](assets/fr/09.webp)



Per maggiori dettagli sugli indirizzi utilizzati, consultare la sezione **Inputs & Outputs**.



![address](assets/fr/10.webp)



Scoprite i diversi schemi di transazione Bitcoin per migliorare la vostra riservatezza.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Velocizzare le transazioni



Nell'ecosistema Bitcoin, l'aspetto della convalida delle transazioni da parte dei miner è strettamente legato alle commissioni associate. I miner  tendono a prioritizzare le transazioni con un rapporto di commissioni più elevato (satoshis/vByte), il che può influire sulla validità della transazione se non si pagano commissioni ragionevoli accettate da loro. La transazione potrebbe rimaner bloccata nella Mempool in attesa di un blocco che accetti il suo rapporto di commissioni.



Fortunatamente, sulla rete Bitcoin sono disponibili due metodi per accelerare la conferma della transazione.





- **RBF** - Replacement By Fee: un metodo che consente di spendere gli stessi elementi della transazione con basse commissioni, ma questa volta aumentando la tariffa della transazione per accelerare la convalida. La nuova transazione verrà convalidata più rapidamente ed inserita in un blocco, invalidando la transazione iniziale con commissioni più basse.



È possibile effettuare Replace By Fee (RBF) con i wallet che integrano questo meccanismo. Ad esempio, leggi il nostro articolo Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child Pay For Parent: un approccio ispirato a RBF, ma applicato dal punto di vista del destinatario. Quando una transazione che ci coinvolge viene bloccata nella Mempool, abbiamo l'opportunità di utilizzare gli output (UTXO) di questa transazione, anche se non è ancora stata confermata. Per farlo, si crea una nuova transazione con commissioni più elevate, affinchè la media delle commissioni risulti superiore per entrambe le transazioni, incentivando i miner ad includere le due transazioni in un blocco.



⚠️ La prima transazione deve essere inclusa in un blocco per consentire la conferma della seconda transazione.



Se tutti questi termini vi sembrano un po' troppo tecnici, vi consiglio di [consultare il nostro glossario](https://planb.academy/resources/glossary), che contiene le definizioni di tutti i termini tecnici relativi a Bitcoin ed al suo ecosistema.



Oltre a questi metodi, Mempool.space, grazie alle sue connessioni con oltre l'80% dei miner presenti sulla rete Bitcoin, consente di accelerare qualsiasi transazione **non confermata**, anche quelle che non attivano RBF, pagando un corrispettivo ai miner in cambio puoi avere la tua transazione minata nel blocco successivo.


Nella pagina dei dettagli della transazione, fare clic sul pulsante **Accelera**, quindi procedere al pagamento della controparte ai miner.



![accelerate-section](assets/fr/11.webp)


## Miner


Per miner ci riferiamo ad una persona che gestisce computer impegnati nel processo di mining; un processo che implica la partecipazione alla Proof-Of-Work. Il miner, raggruppa le transazioni in sospeso nella sua Mempool per formare un blocco candidato. Cerca un Hash (funzione matematica che prende un input di dimensione variabile e produce un output di dimensione fissa) valido, inferiore o uguale all'obiettivo, per l'intestazione di questo blocco modificando il nonce (valore modificabile dal miner per trovare un hash crittografico che sia inferiore o uguale al target di difficoltà). Se trova un Hash valido, trasmette il blocco alla rete Bitcoin e riceve la ricompensa pecuniaria associata, composta dalla sovvenzione del blocco (creazione di nuovi bitcoin) e dalla commissione di transazione.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

I miner sono come "validatori" che verificano e raggruppano le transazioni in blocchi. Per aggiungere un nuovo blocco alla rete Bitcoin, devono risolvere un complesso puzzle matematico (la Proof-Of-Work). Il primo miner che risolve il puzzle vince una ricompensa Bitcoin (sovvenzione del blocco + commissioni per le transazioni incluse nel blocco).



La difficoltà della Proof Of Work viene monitorata, consentendo di visualizzare l'evoluzione della potenza di calcolo richiesta ai miner. Nelle sezioni seguenti troverete:





- una stima delle ricompense totali raccolte dai miner durante l'ultimo aggiustamento della difficoltà, insieme ad una stima della data del prossimo Halving, che si verifica ogni 210.000 blocchi (circa 4 anni).



![rewards](assets/fr/12.webp)



Questa difficoltà viene modificata ogni 2016 blocchi (circa due settimane). È inversamente proporzionale al tempo medio impiegato dai miner per minare ogni 2016 blocchi.


Quando il tempo medio impiegato dai miner è inferiore a 10 minuti, la difficoltà aumenta, al contrario, quando il tempo medio impiegato è superiore a 10 minuti, la difficoltà diminuisce.



![mining-pool](assets/fr/13.webp)





- Gruppi di miner: data la difficoltà, gruppi di miner collaborano per aiutare a risolvere la Proof Of Work, questi gruppi si chiamano **pool**. Quando un blocco viene minato dal gruppo, la ricompensa ottenuta viene distribuita in base alla percentuale di successo nella ricerca della soluzione parziale di ciascun miner, ovvero al contributo in termini di potenza di calcolo nella ricerca della Proof-Of-Work, oppure in base al metodo di remunerazione concordato dalla collaborazione.





![mining](assets/fr/14.webp)



## Infrastruttura Lightning Network



Mempool.space non si limita a fornire informazioni sull'infrastruttura di rete di Bitcoin (main chain), integra anche strumenti di visualizzazione ed esplorazione per la rete Lightning di Bitcoin.



Nella sezione **Lightning** è possibile visualizzare tutte le connessioni esistenti tra i nodi Lightning.



![network-stats](assets/fr/15.webp)



Questa interfaccia fornisce informazioni su:





- statistiche Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **IMPORTANTE**: la capacità di un canale di pagamento indica l'importo massimo che un nodo può inviare ad un altro nodo durante una transazione Lightning.





- I nodi Lightning sono configurati in base al provider di servizi Internet (servizio di hosting) e, facoltativamente, in base alla capacità del canale di pagamento.



![distribution](assets/fr/17.webp)





- La storia della capacità complessiva del Lightning Network.


Troverete anche una classifica di questi nodi in base alla capacità dei loro canali di pagamento.



![ranking](assets/fr/18.webp)



## Diversi grafici



Mempool.space è la piattaforma ideale per esplorare le interazioni del protocollo Bitcoin. I grafici forniscono dati visivi che aiutano a decidere quando effettuare le transazioni ed anche parametri precisi che consentono di visualizzare, in tempo reale, la robustezza e la salute della rete Bitcoin e delle infrastrutture Lightning associate.



Nella sezione **Graphics** si possono visualizzare i dati essenziali della rete Bitcoin:




- evoluzione delle dimensioni della Mempool: è possibile osservare la fluttuazione delle dimensioni della Mempool, che indica periodi di alta o bassa attività sulla rete;



![graphs](assets/fr/19.webp)






- l'evoluzione delle transazioni e delle commissioni di transazione sulla rete selezionata: tracciando le variazioni delle transazioni al secondo, è possibile anticipare i periodi di congestione o di scarsa attività e ottimizzare le commissioni per la tua transazione. Questo grafico ti fornisce una prospettiva sulla capacità della rete di gestire il volume delle transazioni.



![graphs](assets/fr/20.webp)



Ora che siete arrivati alla fine del vostro viaggio su Mempool.space, diventate il vostro esploratore personale e seguite le vostre transazioni in tempo reale. Di seguito trovi il nostro articolo sul **Public Pool** explorer di Bitcoin.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1
