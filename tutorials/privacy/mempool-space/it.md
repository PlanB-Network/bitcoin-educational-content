---
name: Mempool
description: Esplorate l'intero ecosistema Bitcoin.
---

![cover](assets/cover.webp)



Il protocollo Bitcoin è una rete pseudonima, decentralizzata e aperta alla consultazione. I membri (nodi), cioè i computer che possiedono un'istanza del software Bitcoin, hanno accesso illimitato a tutti i dati pubblicati su Bitcoin. Tuttavia, nei primi anni di vita di Bitcoin, il protocollo non era così ampiamente accessibile come lo è oggi.


Nei primi tempi di Bitcoin, era necessario far funzionare un nodo Bitcoin per poter accedere agli strumenti appropriati (bitcoin-cli) per interrogare la rete da linee di comando.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Sono stati quindi lanciati dei progetti per espandere la comunità Bitcoin, rendendola più accessibile a tutti coloro che non possiedono un nodo e/o non hanno le competenze tecniche necessarie.



In questa esercitazione esamineremo il progetto **Mempool.space**, le sue caratteristiche e l'impatto che ha avuto sull'ecosistema Bitcoin.



## Che cos'è il Mempool.space?



**Mempool.space** è un explorer open-source che fornisce informazioni utili sulle transazioni, sulle tariffe delle transazioni, sui blocchi e sui minatori delle varie reti del protocollo Bitcoin. Lanciato nel 2020, migliora notevolmente l'esperienza dell'utente grazie a una grafica rappresentativa, ad animazioni fluide e a interfacce non complesse.



Per comprendere il progetto, un Mempool (pool di memoria) è uno spazio virtuale in cui vengono memorizzate tutte le transazioni in attesa di conferma sulla rete Bitcoin. Un Mempool è come una "sala d'attesa" dove le transazioni Bitcoin attendono di essere confermate. Ogni computer della rete (nodo) ha la propria sala d'attesa, il che spiega perché non tutte le transazioni sono visibili a tutti nello stesso momento.



L'impatto principale della piattaforma nell'ecosistema Bitcoin è che consente di accedere alle varie informazioni presenti nelle aree di memoria della maggior parte dei nodi presenti su Bitcoin senza doverne eseguire uno. Mempool.space è un repository per la visualizzazione e la ricerca di reti di protocollo Bitcoin.



L'uso sempre più diffuso nell'ecosistema e il fatto che Mempool.space sia open source hanno permesso di integrarlo in un numero sempre maggiore di sistemi di hosting personali. Ora è possibile avere una propria istanza di Mempool.space direttamente sul proprio nodo personale. Vedere il nostro tutorial sulla configurazione di Mempool.space sul vostro nodo Umbrel.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Le basi dello spazio Mempool



Come già accennato, [Mempool.space](https://Mempool.space) è un esploratore di protocolli Bitcoin che consente di monitorare le transazioni e la loro propagazione sulla rete Bitcoin scelta in tempo reale, da un Interface grafico.



Lo spazio Mempool.supporta molte reti di protocollo Bitcoin.


Nella barra dei menu si trovano le seguenti reti:




- **Mainnet**: La rete Bitcoin principale dove avvengono le transazioni Bitcoin reali.
- **Signet**: Una rete di prova che utilizza le firme digitali per convalidare i blocchi senza richiedere le risorse necessarie alla rete principale.
- **Testnet 3**: Una rete di test e sviluppo priva di rischi sul protocollo Bitcoin.
- **Testnet 4**: La nuova versione di Testnet 3 apporta maggiore stabilità e nuove regole di consenso all'ambiente di test.



![reseaux](assets/fr/01.webp)



Sulla home page, a sinistra in Green, vedrete i possibili blocchi futuri (gruppi di transazioni) pronti per essere convalidati e integrati (minati) nella rete Bitcoin. In media, un blocco viene estratto ogni dieci minuti: conservate questa informazione, perché vi tornerà utile più avanti nel nostro sviluppo.


In viola, sul lato destro, troverete i blocchi recenti estratti su Bitcoin, con il numero dell'ultimo blocco estratto che rappresenta l'altezza attuale della rete.



![blocs](assets/fr/02.webp)



La sezione **Transaction Fees** è una stima delle commissioni di transazione. Più alte sono le commissioni assegnate alla transazione, più è probabile che la transazione venga aggiunta al blocco successivo pronto per essere estratto.


Le commissioni di transazione rappresentano il costo che un Miner richiede all'utente per inserire la sua transazione in un blocco candidato per il Mining. È definita da un rapporto sat/vB (Satoshi/Virtual Bytes) che rappresenta il numero di satoshis pagati per lo spazio che la transazione occuperà nel blocco candidato.



⚠️ IMPORTANTE: in caso di saturazione del Mempool, i minatori danno priorità alle transazioni che offrono il miglior rapporto Satoshi/vByte. Più pesante (grande) è la transazione, più satoshi saranno necessari per essere inclusi rapidamente.



![fees-visualizer](assets/fr/03.webp)



La sezione **Mempool Goggles** consente di visualizzare lo spazio occupato da una transazione.



![mempool](assets/fr/04.webp)



Un blocco viene estratto ogni dieci minuti circa a causa della difficoltà del Proof of Work che i minatori devono fornire per aggiungere il loro blocco candidato alla catena di blocchi estratti. Questa difficoltà varia ogni **2016 blocchi**, equivalente a circa **2 settimane**. È possibile vedere l'evoluzione di questa difficoltà qui.



![difficulty](assets/fr/05.webp)



L'aggiunta di un nuovo blocco alla catena principale dà diritto al Miner del blocco convalidato a una ricompensa composta da una parte fissa (dimezzata ogni 210.000 blocchi**, equivalente a circa 4 anni** di dimezzamento) e dalle commissioni di transazione.



![halving](assets/fr/06.webp)



## Accedere ai dettagli della transazione



Nella barra di ricerca di Mempool.space, è possibile inserire il proprio Bitcoin Address o il proprio transaction ID per saperne di più sulla propria storia.



![search](assets/fr/07.webp)



Nella pagina dei dettagli della transazione si trovano informazioni generali sulla transazione:




- **Stato**: Confermato quando viene aggiunto a un blocco, non confermato quando è in attesa in un Mempool.
- **Spese di transazione**.
- **Tempo stimato di arrivo (ETA)**: Il tempo approssimativo necessario affinché la transazione venga aggiunta a un blocco. Viene calcolato in base al rapporto che costituisce le commissioni associate a questa transazione.



![general-txinfo](assets/fr/08.webp)



La sezione **Flusso** mostra un grafico dei componenti della transazione.



Gli input (UTXO precedenti), utilizzati per la transazione, e gli output che danno ai destinatari il diritto di utilizzare i bitcoin di ciascun output presentando la firma richiesta per la loro spesa.



![flow](assets/fr/09.webp)



Per maggiori dettagli sugli indirizzi utilizzati, consultare la sezione **Ingressi e uscite**.



![address](assets/fr/10.webp)



Scoprite i diversi schemi di transazione Bitcoin per migliorare la vostra riservatezza.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Velocizzare le transazioni



Nell'ecosistema Bitcoin, l'aspetto della convalida delle transazioni da parte dei minatori è intrinsecamente legato alle commissioni associate alla transazione. I minatori danno priorità alle transazioni con un rapporto di commissioni più elevato (satoshis/vByte), il che potrebbe influire sulla validità della transazione se non si pagano commissioni ragionevoli accettate dai minatori. La transazione rimarrebbe bloccata in Mempool in attesa di un blocco che accetti il suo rapporto di commissioni.



Fortunatamente, sulla rete Bitcoin sono disponibili due metodi per accelerare la conferma della transazione.





- **RBF** - Sostituzione per tassa: Un metodo che consente di spendere le stesse voci della transazione a tariffa ridotta, ma questa volta aumentando la tariffa della transazione per accelerare la convalida. La nuova transazione verrà convalidata più rapidamente e inserita in un blocco, invalidando la transazione a tariffa ridotta.



È possibile effettuare un'azione di sostituzione delle commissioni con i portafogli che accettano questo meccanismo. Ad esempio, si veda il nostro articolo sul portafoglio Blue Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Un approccio ispirato al RBF, ma dal lato del destinatario. Quando la transazione di cui si è destinatari viene bloccata in un Mempool, si ha la possibilità di spendere gli output (UTXO) di questa transazione, nonostante non sia ancora stata confermata, assegnando più commissioni a questa nuova transazione in modo che le commissioni medie - della transazione di cui si è destinatari e della transazione avviata - incoraggino i minatori a includere entrambe le transazioni in un blocco.



⚠️ La prima transazione deve essere inclusa in un blocco per consentire la conferma della seconda transazione.



Se tutti questi termini vi sembrano un po' troppo tecnici, vi consiglio di [consultare il nostro glossario](https://planb.network/resources/glossary), che contiene le definizioni di tutti i termini tecnici relativi al Bitcoin e al suo ecosistema.



Oltre a questi metodi, Mempool.space, grazie alle sue connessioni con oltre l'80% dei minatori presenti sulla rete Bitcoin, consente anche di accelerare qualsiasi transazione **non confermata**, anche quelle che non attivano il RBF, pagando un corrispettivo ai minatori del Exchange per inserire la transazione a basso costo nel blocco successivo pronto per essere estratto.



Nella pagina dei dettagli della transazione, fare clic sul pulsante **Accelera**, quindi procedere al pagamento della controparte ai minatori.



![accelerate-section](assets/fr/11.webp)


## Minori



Un Miner si riferisce a una persona che gestisce una miniera, ossia un computer impegnato nel processo Mining, che consiste nel partecipare al Proof-of-Work. Il Miner raggruppa le transazioni in sospeso nel suo Mempool per formare un blocco candidato. Cerca quindi un Hash valido, inferiore o uguale all'obiettivo, per l'intestazione di questo blocco modificando i vari nonces. Se trova un Hash valido, trasmette il blocco alla rete Bitcoin e intasca la ricompensa pecuniaria associata, composta dalla sovvenzione del blocco (creazione di nuovi bitcoin ex-nihilo) e dalla commissione di transazione.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

i minatori sono come "validatori" che verificano e raggruppano le transazioni in blocchi. Per aggiungere un nuovo blocco alla rete Bitcoin, devono risolvere un complesso puzzle matematico (il Proof-of-Work). Il primo Miner che risolve il puzzle vince una ricompensa Bitcoin (sovvenzione del blocco + commissioni per le transazioni incluse nel blocco).



La difficoltà di questo Proof of Work viene monitorata, consentendo di visualizzare l'evoluzione della potenza di calcolo richiesta ai minatori. Nelle sezioni seguenti troverete :





- Una stima delle ricompense totali raccolte dai minatori durante l'ultimo aggiustamento della difficoltà, nonché una stima del prossimo Halving della concessione dei blocchi, che si verifica ogni 210.000 blocchi (circa 04 anni).



![rewards](assets/fr/12.webp)



Questa difficoltà viene modificata ogni 2016 blocchi (circa due settimane). È inversamente proporzionale al tempo medio impiegato dai minatori per Miner ogni 2016 blocchi.


Quando il tempo medio impiegato dai minatori è inferiore a 10 minuti, la difficoltà aumenta, dimostrando che per i minatori era più facile convalidare i blocchi Miner. Al contrario, quando il tempo medio impiegato è superiore a 10 minuti, la difficoltà diminuisce.



![mining-pool](assets/fr/13.webp)





- Gruppi di minatori: Data la difficoltà, un gruppo di minatori collabora per aiutare a trovare il Proof of Work sul Bitcoin, in quello che chiamiamo un **pool**. Quando un blocco viene estratto dal gruppo, la ricompensa ottenuta viene distribuita in base alla percentuale di successo nella ricerca della soluzione parziale di ciascun Miner, ovvero al contributo in termini di potenza di calcolo nella ricerca del Proof-of-Work, oppure in base al metodo di remunerazione concordato dalla collaborazione.





![mining](assets/fr/14.webp)



## Infrastruttura Lightning Network



Mempool non si limita a fornire informazioni sull'infrastruttura di rete di Bitcoin (catena principale). Integra anche strumenti di visualizzazione ed esplorazione per l'overlay Lightning di Bitcoin.



Nella sezione **Lightning** è possibile visualizzare tutte le connessioni esistenti tra i nodi Lightning.



![network-stats](assets/fr/15.webp)



Questo Interface fornisce informazioni su :





- Statistiche Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **IMPORTANTE**: La capacità di un canale di pagamento indica l'importo massimo che un nodo può inviare a un altro nodo durante una transazione Lightning.





- I nodi lightning sono assegnati in base al provider di servizi Internet (servizio di hosting) e, facoltativamente, in base alla capacità del canale di pagamento.



![distribution](assets/fr/17.webp)





- La storia della capacità complessiva del Lightning Network.


Troverete anche una classifica di questi nodi in base alla capacità dei loro canali di pagamento.



![ranking](assets/fr/18.webp)



## Più grafica



Mempool.space è la piattaforma ideale per godere dell'interazione con le reti del protocollo Bitcoin. I grafici non solo forniscono dati visivi che aiutano a decidere quando effettuare le transazioni, ma anche parametri precisi che consentono di visualizzare, in tempo reale, la forza e la salute della rete Bitcoin e delle infrastrutture Lightning associate.



Nella sezione **Grafica** si possono visualizzare i dati essenziali della rete Bitcoin:




- Evoluzione delle dimensioni del Mempool: È possibile osservare la fluttuazione delle dimensioni del Mempool, che può indicare periodi di alta o bassa attività sulla rete.



![graphs](assets/fr/19.webp)






- L'evoluzione delle transazioni e delle commissioni di transazione sulla rete scelta: Tracciando le variazioni delle transazioni al secondo, è possibile anticipare i periodi di congestione o di scarsa attività e ottimizzare le commissioni di transazione. Questo grafico fornisce una prospettiva sulla capacità della rete di gestire il volume delle transazioni.



![graphs](assets/fr/20.webp)



Ora che siete arrivati alla fine del vostro viaggio su Mempool.space, diventate il vostro esploratore personale e seguite le vostre transazioni in tempo reale. Di seguito trovate il nostro articolo sull'esploratore della **Piscina pubblica** di Bitcoin.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1