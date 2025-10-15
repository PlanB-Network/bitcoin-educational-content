---
name: Amboss
description: Esplorare e analizzare Lightning Network
---

![cover](assets/cover.webp)



Il Lightning Network è un Layer del protocollo Bitcoin, sviluppato principalmente per promuovere l'adozione dei pagamenti Bitcoin su base quotidiana aumentando la velocità di elaborazione di ogni transazione. Basato sul principio della decentralizzazione, il Lightning Network è costituito da nodi (computer che eseguono un'implementazione di Lightning) che comunicano tra loro in modalità peer-to-peer, trasmettendo i dati (pagamenti e verifica dei pagamenti).



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Proprio come nella catena principale, è diventato essenziale consentire agli utenti di conoscere le informazioni e lo stato della rete, al fine di facilitare le connessioni tra i nodi e ridurre al minimo il problema della liquidità che generalmente si verifica nella rete. Infatti, sul Lightning Network, si consigliano micropagamenti di importi relativamente più piccoli rispetto a quelli delle transazioni sulla catena principale Bitcoin.



È importante notare che non tutti i nodi Lightning sono disponibili sulla piattaforma Amboss.



Come [Spazio Mempool](https://Mempool.space), che fornisce informazioni utili sulla catena principale del protocollo Bitcoin, dal 2022 [Amboss](https://amboss.space) fornisce informazioni su :





- Nodi sul Lightning Network
- Canali di pagamento e loro capacità di pagamento
- Evoluzione del Lightning Network nel tempo
- Statistiche sugli addebiti ai nodi di collegamento per i vostri pagamenti.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In questo tutorial vi faremo fare un giro su questa piattaforma, che è una risorsa essenziale per gli utenti di Lightning Network, per chi vuole collegare il proprio nodo per espandere la rete, ecc.




## Trova le coppie



Uno degli obiettivi della piattaforma Amboss è quello di consentire ai vari nodi della rete di connettersi e comunicare informazioni tra loro. Sulla home page della piattaforma, potete cercare direttamente il nome di un nodo che già conoscete o trovare i nodi dei portafogli Lightning più popolari che utilizzate.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Sulla home page, troverete anche i nodi classificati in base a :




- Evoluzione della capacità: la quantità di Bitcoin associata alla chiave pubblica del nodo e il totale disponibile in tutti i suoi canali.
- Evoluzione del canale: il numero di nuove connessioni con altri nodi della rete.
- Popolarità del nodo: la frequenza di utilizzo del nodo.



![nodes](assets/fr/03.webp)



La scelta del nodo giusto a cui collegarsi si riduce quindi alla verifica dei seguenti criteri:





- Assicuratevi che il nodo disponga di una quantità sufficiente di bitcoin; maggiore è la capacità del nodo, maggiore è la quantità di bitcoin che potete pagare.





- Assicurarsi che il nodo abbia un gran numero di connessioni e canali aperti con altri nodi della rete.





- Assicurarsi che il nodo sia attivo e ancora apprezzato dai suoi pari controllando il numero di nuovi canali; più nuovi canali ha aperto questo nodo, più è apprezzato dagli altri nodi della rete.



Una volta trovato il nodo giusto, fare clic sul suo nome per essere reindirizzati alla pagina delle informazioni sul nodo.



Su questo Interface, controllando il Timestamp del canale appena creato, avrete un indizio sull'attività di questo nodo. Troverete anche informazioni sulla capacità dei canali di questo nodo: questa informazione è fondamentale se volete utilizzare attivamente questo nodo per effettuare i vostri pagamenti.




![node_info](assets/fr/04.webp)



Nella sezione di sinistra si trovano ulteriori dettagli sulla posizione di questo nodo. Ad esempio, è possibile visualizzare :




- La chiave pubblica: l'identificatore appena sotto il nome del nodo.
- La posizione geografica di questo nodo.




![channels](assets/fr/05.webp)



Questo Interface indica il Address di connessione per questo nodo: assume la forma `pubkey@ip:port`. Nel nostro esempio, vogliamo connetterci al nodo il cui file :




- la chiave pubblica `pubkey` è: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- La porta: `9735`



![geoinfo](assets/fr/06.webp)



Nella sezione **Canali**, viene visualizzato l'elenco dei canali aperti e le connessioni del nodo con altri nodi della rete. In questa Interface, diverse informazioni sono fondamentali per confermare che questo nodo corrisponde alle nostre esigenze o è affidabile:





- Rapporto in entrata**: L'importo che il nodo addebiterà per ogni milione di Satoshi che riceve, a seconda del canale scelto.
- Il rapporto (parti per milione)** : rappresenta il numero di Satoshi per milione di unità che il nodo addebiterà all'utente quando decide di effettuare un pagamento tramite uno dei suoi canali. Supponiamo che decidiate di effettuare un pagamento di `10_000 Sats` attraverso un canale il cui rapporto ppm è `500 Sats`, dovrete pagare al nodo `10_000 * 500 / 1_000_000` satoshi, equivalenti a `5 Sats`.
- Il [HTLC](https://planb.network/resources/glossary/HTLC) massimo** : L'importo massimo che questo nodo consente di transitare attraverso uno di questi canali.



Consultando la tabella in questo Interface, è possibile trovare tutte queste informazioni anche sul nodo a cui è abbinato.



![channels_info](assets/fr/07.webp)



Nella sezione **Mappe dei canali** è possibile vedere la distribuzione e la capacità dei vari canali su questo nodo. È possibile modificare i criteri di distribuzione visualizzati selezionando una delle opzioni nell'elenco a discesa a destra.



![cha_maps](assets/fr/08.webp)



La sezione **Canali chiusi** raggruppa tutti i canali precedenti del nodo in base al tipo di chiusura:




- Chiusura reciproca**: rappresenta l'accordo di entrambe le parti, che utilizzano la loro chiave privata per firmare la transazione che segna la chiusura del canale e la distribuzione dei saldi al suo interno
- Una **chiusura forzata**: rappresenta la chiusura improvvisa e unilaterale di una parte del canale. Questo tipo di chiusura è sconsigliato, poiché il Lightning Network è un protocollo basato sulla punizione: quando si cerca di frodare l'equilibrio di un canale, si rischia di perdere tutto l'equilibrio disponibile in quel canale.



![closed](assets/fr/09.webp)



Ottenere informazioni sulle commissioni di transito per l'instradamento dei pagamenti attraverso un canale sul nodo in uso



![fees](assets/fr/10.webp)



## Informazioni sulla rete



Amboss si concentra non solo sulle informazioni relative ai membri della rete, ma anche sullo stato della rete stessa.



Nella sezione **Statistiche**, sotto il menu di sinistra "Simulazioni", si trova un grafico che mostra la probabilità di successo di un pagamento in funzione dell'importo del pagamento.



In effetti, noterete che la curva sta diminuendo perché, con l'aumentare dell'importo del pagamento, avete meno possibilità di vederlo passare. Questo riflette il vero problema di liquidità del Lightning Network. Per esempio, il vostro pagamento di `10_000` satoshi ha il `79%` di probabilità di essere effettuato. D'altra parte, per un pagamento di `3_000_000` satoshis avete meno del `13%` di probabilità di successo.



![network](assets/fr/11.webp)



Il menu **Statistiche di rete** consente di visualizzare graficamente le statistiche di :




- Canali di pagamento
- Nodi
- Capacità
- Tasse
- Evoluzione del canale.



![network_stat](assets/fr/12.webp)



Nel menu **Statistiche di mercato**, l'opzione **Dettagli ordine** consente di visualizzare la domanda di liquidità sul Lightning Network. Questo grafico può anche mostrare quali canali sono più richiesti e/o quali hanno una notevole capacità. Questo grafico può anche mostrare quali canali sono più richiesti e/o quali hanno una notevole capacità.



![markets](assets/fr/13.webp)




## Strumenti



Amboss offre una serie di strumenti per aiutarvi a ottimizzare le ricerche e le azioni.



### Decoder Lightning Network



Questo strumento è principalmente responsabile di fornire dettagli sulla struttura di un Lightning Invoice, Lightning Address o Lightning URL.



Nella home page, nella sezione **Strumenti**, presentate il vostro Lightning Address, ad esempio.



![decoder](assets/fr/14.webp)



Da questo decodificatore è possibile ottenere informazioni quali :




- la chiave pubblica del nodo associata al proprio Lightning Address;
- Il tempo di scadenza di un Invoice dal vostro Address;
- Il minimo e il massimo che è possibile inviare;
- Il nodo Nostr associato al Address, se Nostr è abilitato su questo nodo.



![decode](assets/fr/15.webp)



### Magma IA



Scoprite l'ultimo strumento presentato da Amboss per gestire in maniera efficiente le connessioni ai nodi Lightning Network. Magma AI utilizza un'intelligenza artificiale dedicata per concentrarsi su un problema importante: effettuare una buona selezione dei nodi a cui collegarsi.



![magma](assets/fr/16.webp)



### Calcolatrice Satoshi



Scoprite il prezzo attuale di Bitcoin nella vostra valuta locale (EUR / USD). Nella home page, utilizzare il calcolatore di satoshis per trovare il prezzo di mercato attuale.



![calculator](assets/fr/17.webp)




Ora avete fatto un giro completo delle caratteristiche e degli strumenti di analisi della piattaforma. Di seguito trovate il nostro articolo sull'esploratore Bitcoin **Mempool.space**.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f