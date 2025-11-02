---
name: Esploratore BLOCKSTREAM
description: Esplorare il Layer principale di Bitcoin e Liquid Network
---

![cover](assets/cover.webp)



Il BLOCKSTREAM Explorer è un progetto che facilita l'esplorazione delle transazioni e del Global State del protocollo Bitcoin, così come del [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid sviluppato dalla società BLOCKSTREAM.



Avviato nel 2014 da BLOCKSTREAM, una società fondata da Adam Back, l'esploratore [BLOCKSTREAM.info](https://BLOCKSTREAM.info) ha l'obiettivo di fornire una solida infrastruttura per Bitcoin, garantendo l'interoperabilità e il tracciamento delle transazioni tra i livelli (On-Chain e Liquid), migliorando al contempo la sicurezza e la privacy degli utenti.



In questa esercitazione presentiamo le caratteristiche che lo rendono diverso, i suoi servizi e il modo in cui offre un monitoraggio continuo delle operazioni e dello stato dei livelli Bitcoin On-Chain e Liquid.



## Come iniziare con il BLOCKSTREAM



### Navigare nel canale principale



Quando si accede all'explorer BLOCKSTREAM.info, su "**Dashboard**", il canale principale del protocollo Bitcoin è selezionato per impostazione predefinita. Da questo Interface, si ha una panoramica di :





- Dimensione della catena principale: Blocchi estratti di recente.



![blocks](assets/fr/01.webp)



Questa sezione fornisce informazioni sui blocchi estratti di recente, sul Timestamp, sul numero di transazioni incluse in ogni BLOCK, sulla dimensione in kilobyte (kB) e sulla misura di ogni BLOCK in unità di peso (**WU** = *Weight Units*). Quest'ultima misura è interessante perché ci permette di valutare l'ottimizzazione del BLOCK, dato che ogni BLOCK della catena principale è limitato a `4.000.000 WU`, o `4.000 kWU`.





- Transazioni recenti.



![transactions](assets/fr/02.webp)



La sezione della transazione fornisce informazioni sull'identificatore univoco della transazione, sul valore Bitcoin coinvolto, sulla dimensione in byte virtuali (vB) - che rappresenta la somma di tutti i dati (input e output) - e sulla tariffa associata. Ad esempio, una transazione con una dimensione di `153 vB` a un tasso di `2 sat/vB` comporterà un addebito di `306 satoshis`.



### Esplorazione dei fluidi



Dal menu "**Blocchi**" è possibile tracciare la storia dell'intera catena principale fino all'ultimo BLOCK estratto.



![blocs](assets/fr/03.webp)



Facendo clic su uno specifico BLOCK, è possibile ottenere maggiori dettagli sulle informazioni e sulle transazioni in esso contenute. Ad esempio, per il BLOCK 919330: si ha il Hash del BLOCK. È anche possibile navigare verso il BLOCK precedente, poiché ogni BLOCK estratto (a parte il Genesis) è collegato al precedente, mantenendo il Hash del suo predecessore.



![metadata](assets/fr/04.webp)



Facendo clic sul pulsante **"Dettagli "**, è possibile ottenere ulteriori informazioni su questo BLOCK, come il suo stato, che conferma che è stato aggiunto alla catena principale conservata e propagata. È inoltre possibile conoscere la difficoltà con cui questo BLOCK viene estratto: questa difficoltà rappresenta la potenza di calcolo richiesta per risolvere il problema crittografico del Mining e viene modificata ogni 2016 blocchi (circa 2 settimane).



![details](assets/fr/05.webp)



Sotto questa sezione di dettagli, troviamo tutte le transazioni incluse in questo BLOCK.



La primissima transazione nel BLOCK è chiamata **transazione coinbase**. Viene utilizzata per allocare la ricompensa Mining del Miner (tutte le commissioni associate alle transazioni incluse nel BLOCK e nella sovvenzione BLOCK). I bitcoin creati da questa transazione possono essere spesi solo dopo che sono stati minati altri 100 blocchi consecutivi. In altre parole, per poterli utilizzare, il Miner dovrà attendere la produzione del BLOCK **919430**. Questo è noto come [*"periodo di maturità "*](https://planb.network/fr/resources/glossary/maturity-period).



La coinbase è una transazione speciale: è l'unica che non ha alcun input reale, poiché non spende alcun bitcoin da una transazione precedente.




![coinbase](assets/fr/06.webp)



Tutte le altre transazioni sono suddivise in due sezioni: ingressi e uscite.



Affinché i bitcoin possano essere utilizzati come input in una nuova transazione, l'iniziatore della transazione deve dimostrarne il possesso fornendo una firma che corrisponde a uno script specifico. Ogni pezzo di bitcoin (UTXO) contiene uno script che generalmente richiede una firma specifica che solo la chiave privata del titolare può fornire. Questi script sono ***scriptSig*** (in ASM), scritti in Bitcoin Script, e possono essere di vario tipo. In questo esempio, si può notare che gli UTXO utilizzati erano di tipo P2SH per un output di tipo P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



È possibile tracciare la storia di uno specifico UTXO utilizzando l'euristica. Vi invitiamo a scoprire le diverse euristiche del Bitcoin e a capire come rafforzare la riservatezza delle vostre transazioni Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Prendiamo l'esempio delle spese in uscita di questa transazione. Facendo clic sull'identificativo della transazione, si viene reindirizzati alla sezione **Transazioni** della pagina dei dettagli della transazione.



![transaction](assets/fr/08.webp)



Da questa pagina è possibile scoprire in quale BLOCK è stata inclusa la transazione. A seconda del tipo di Address utilizzato, la transazione può ottimizzare i suoi dati (*virtual bytes*) e quindi pagare meno tasse di transazione. Questa transazione, ad esempio, ha risparmiato il 53% di commissioni utilizzando un formato SegWit BECH32 Address nativo che inizia con `bc1q`.



![trx_details](assets/fr/09.webp)



## Rivestimento Liquid



Liquid Network è un [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) e una soluzione open source di livello 2 per il protocollo Bitcoin. In particolare, consente transazioni Bitcoin più veloci e riservate.



Nell'explorer di BLOCKSTREAM.info, fare clic sul pulsante **"Liquid"** per passare a Liquid Network.



![liquid](assets/fr/10.webp)



Facendo clic su una delle transazioni che desideriamo seguire, vediamo che gli importi dei pezzi Bitcoin sono sostituiti dalla dicitura "**Confidenziale**". Su questa rete, le transazioni possono essere riservate, quindi non possiamo vedere gli importi di ciascun UTXO, né in entrata né in uscita dalla transazione.



![liquid_trx](assets/fr/11.webp)



Tuttavia, notiamo che i principi e i meccanismi presenti sul Layer principale del protocollo Bitcoin sono gli stessi: script di blocco Bitcoin e tracciabilità UTXO.



![liquid_details](assets/fr/12.webp)



Il Liquid Network fornisce anche asset digitali non depositati che possono essere utilizzati dalle organizzazioni. Nel menu **"Assets "** si trova un elenco degli asset registrati, il loro totale e il dominio a cui si riferiscono.



![assets](assets/fr/13.webp)



Per ogni asset, è possibile tracciare la storia delle transazioni di emissione e combustione (eliminando il totale in circolazione).



![assets_trxs](assets/fr/14.webp)




## Altre opzioni



L'esploratore BLOCKSTREAM.info include anche visualizzazioni e tracciamento delle transazioni su Testnet, Bitcoin, On-Chain e Liquid Network.



![testnet](assets/fr/15.webp)



Quando si passa alla rete Testnet, non si utilizzano bitcoin reali, ma si hanno a disposizione tutte le caratteristiche descritte sopra.



![liquid_testnet](assets/fr/16.webp)



Questa rete è dotata di una catena di diversa lunghezza, alla quale è possibile collegare e testare il funzionamento dei meccanismi Bitcoin e Liquid.





- La sezione API è dedicata a chi desidera integrare alcune funzioni di Explorer nella propria applicazione. Attraverso questo API è possibile interrogare la catena principale dei diversi livelli (On-Chain e Liquid), tracciare le transazioni e conoscere le commissioni medie delle transazioni in un BLOCK, ad esempio.



![api](assets/fr/17.webp)



Ora siete pronti a sfruttare tutte le potenzialità di BLOCKSTREAM Explorer per interrogare le blockchain sui livelli On-Chain e Liquid. Ci auguriamo che questo tutorial sia stato utile e vi consigliamo il nostro tutorial su Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f