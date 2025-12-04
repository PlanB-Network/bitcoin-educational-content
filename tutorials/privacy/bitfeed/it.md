---
name: Bitfeed
description: Esplorare la catena di protocollo principale del Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed è una piattaforma per la visualizzazione del livello onchain del protocollo Bitcoin. È stata creata da uno dei collaboratori del progetto Mempool.space e si distingue soprattutto per il suo aspetto minimalista e la sua facilità d'uso.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In questo tutorial daremo un'occhiata a questo strumento, che consente di esplorare tutte le transazioni e i blocchi della rete.



## Come iniziare con Bitfeed



Bitfeed è una piattaforma che si concentra su tre punti principali:





- Consultazione Blockchain**,
- Ricerca di transazioni**,
- Visualizzazione del mempool**.



### Consultare la blockchain



Sulla home page di Bitfeed troverete soprattutto :





- La barra di ricerca: Questa sezione è il punto di ingresso per le ricerche sulla blockchain. Qui è possibile cercare un blocco specifico in base al numero o all'hash. È inoltre possibile cercare transazioni specifiche e indirizzi Bitcoin per verificare determinate informazioni sulle transazioni in rete.



![searchBar](assets/fr/01.webp)



Nell'angolo in alto a sinistra si può vedere il prezzo attuale del bitcoin, stimato in dollari USA (USD).



![price](assets/fr/02.webp)



Nella barra laterale destra si trova il menu della piattaforma. Da questo menu è possibile personalizzare l'interfaccia della piattaforma a proprio piacimento, aggiungere o rimuovere elementi e personalizzare i filtri di visualizzazione. Ad esempio, è possibile visualizzare la dimensione di ciascun blocco in base al valore o al peso in byte virtuali (vByte).



![menu](assets/fr/03.webp)



Al centro della pagina si trova l'ultimo blocco estratto, con una vista di tutte le transazioni incluse in quel blocco. Questa sezione fornisce informazioni sul timestamp, sul numero totale di bitcoin coinvolti nel blocco, sulla dimensione del blocco in byte, sul numero di transazioni e sul rapporto medio del costo della transazione per byte virtuale nel blocco.



![block](assets/fr/04.webp)



È possibile ripercorrere la storia del canale cercando un blocco specifico nella barra di ricerca e visualizzarlo secondo i propri criteri.



Ad esempio, si vogliono visualizzare le transazioni nel blocco `879488`.



![bloc](assets/fr/05.webp)



La prima transazione di questo blocco rappresenta la transazione **coinbase** che consente al minatore di questo blocco di guadagnare la ricompensa mining, spendibile solo dopo che sono stati minati 100 blocchi, composta dalle commissioni di transazione incluse e dal block grant. Questa transazione è quella che consente l'emissione di nuovi bitcoin nel sistema.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Per impostazione predefinita, le transazioni in un blocco sono rappresentate secondo due criteri:




- La dimensione, che può variare tra il valore e il peso (vByte) ;
- Il colore può variare in base all'età e al rapporto tra le commissioni di transazione per byte virtuale.



![options](assets/fr/07.webp)



Possiamo quindi concludere che tutte le transazioni incluse nello stesso blocco hanno lo stesso numero di conferme nella blockchain. I cubi più grandi rappresentano le transazioni che contengono la quantità maggiore di bitcoin.



Questa interpretazione è ulteriormente confermata dall'opzione di menu **"Info "**, che ci informa della traduzione del colore e delle dimensioni delle transazioni del blocco.



![infos](assets/fr/08.webp)



È inoltre possibile visualizzare le transazioni di un blocco in base ai byte virtuali e al rapporto delle commissioni. Questa visualizzazione può differire dalla precedente, poiché il valore in bitcoin incluso in una transazione non ne definisce la dimensione.



![visualisation](assets/fr/09.webp)



### Visualizzazione delle transazioni



È possibile cercare una transazione utilizzando il suo identificativo tramite la barra di ricerca. È inoltre possibile fare clic su un cubo per visualizzare le informazioni relative a quella transazione.



Nel nostro caso, prendiamo la transazione che occupa lo spazio maggiore nel blocco `879488`.



![biggest](assets/fr/10.webp)



Vedrete che questa transazione ha `42.989`, che rappresenta la differenza tra l'ultimo blocco estratto e il blocco scelto. Queste conferme contribuiscono a rafforzare la sicurezza della rete Bitcoin, perché per modificare questa transazione in modo malevolo, gli aggressori dovrebbero possedere una potenza di calcolo equivalente a quella necessaria per riscrivere l'intera catena di blocchi principale.



La dimensione di questa transazione è di `57.088 vByte`, principalmente a causa del gran numero di UTXO utilizzati nella sua costruzione (842 voci). Sorprendentemente, il rapporto di commissione applicato rimane relativamente basso (solo 4 sats/vByte) rispetto alla media complessiva dei blocchi di 5,82 sats/vByte.



La transazione che occupa più spazio non è quindi necessariamente quella con il più alto rapporto di costo della transazione.



![transaction](assets/fr/11.webp)



Se si segue la scala nel menu **Info**, la transazione con il rapporto costo transazione più alto è quella di colore viola. Si tratta della transazione [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) con un rapporto di costo di transazione di `147,49 sats/vByte`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualizzazione Mempool



Il mempool è il luogo virtuale in cui vengono raggruppate le transazioni Bitcoin in attesa di essere incluse in un blocco. Bitfeed permette di consultare il [mempool](https://planb.academy/resources/glossary/mempool) di diversi minatori Bitcoin, offrendo un'ampia gamma di tracciamenti delle transazioni.



![mempool](assets/fr/13.webp)



In questa sezione è possibile tenere traccia di tutte le transazioni valide e non ancora confermate sulla catena principale della rete Bitcoin.



![unconfirmed](assets/fr/14.webp)



Ora avete una guida all'utilizzo della piattaforma Bitfeed per analizzare blocchi e transazioni al fine di visualizzare le informazioni disponibili sulla catena principale della rete Bitcoin, beneficiando di un'interfaccia minimalista e facile da usare. Se questo tutorial vi è piaciuto, vi consigliamo di fare il passo successivo: scoprire il Lightning Network attraverso il progetto Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017