---
name: Sparrow Wallet - Stonewall
description: Comprendere e utilizzare le transazioni Stonewall su Sparrow
---

![cover](assets/cover.webp)




> *Rompete i presupposti dell'analisi blockchain con il dubbio matematicamente dimostrabile tra mittente e destinatario delle vostre transazioni.*

## Cos'è una transazione Stonewall?



Stonewall è una forma specifica di transazione Bitcoin progettata per aumentare la riservatezza degli utenti quando spendono, imitando una coinjoin tra due persone, senza esserlo realmente. In realtà, questa transazione non è collaborativa. Un utente può costruirla da solo, utilizzando come input solo gli UTXO che gli appartengono. È quindi possibile creare una transazione Stonewall per qualsiasi occasione, senza doversi sincronizzare con un altro utente.



La transazione Stonewall funziona come segue: come input della transazione, l'emittente utilizza 2 UTXO che gli appartengono. In uscita, la transazione produce 4 uscite, 2 delle quali sono esattamente dello stesso importo. Gli altri due saranno valuta estera. Delle due uscite dello stesso importo, solo una andrà effettivamente al beneficiario.



Quindi ci sono solo 2 ruoli in una transazione Stonewall:




- L'emittente, che effettua il pagamento effettivo ;
- Il destinatario, che potrebbe non essere a conoscenza della natura specifica della transazione e si aspetta semplicemente il pagamento da parte del mittente.



Facciamo un esempio per capire questa struttura di transazione. Alice è dal panettiere per comprare la sua baguette, che costa `4.000 sats`. Vuole pagare in bitcoin, mantenendo una forma di riservatezza sul pagamento. Decide quindi di creare una transazione Stonewall per il pagamento.



![image](assets/fr/01.webp)



Analizzando questa transazione, possiamo vedere che il fornaio ha effettivamente ricevuto `4.000 sats` in pagamento per la baguette. Il Alice ha utilizzato 2 UTXO come input: uno di `10.000 sats` e uno di `15.000 sats`. In uscita, ha recuperato 3 UTXO: uno di `4.000 sats`, uno di `6.000 sats` e uno di `11.000 sats`. Alice ha quindi un saldo netto di `- 4.000 sats` su questa transazione, che corrisponde bene al prezzo della baguette.



In questo esempio, ho intenzionalmente trascurato le commissioni del mining per renderlo più comprensibile. In realtà, i costi di transazione sono interamente a carico dell'emittente.



## Qual è la differenza tra Stonewall e Stonewall x2?



La transazione Stonewall funziona in modo identico alla transazione StonewallX2, solo che quest'ultima richiede una collaborazione, a differenza della transazione Stonewall classica, da cui il nome "x2". Questo perché la transazione Stonewall viene eseguita senza bisogno di collaborazione esterna: il mittente può eseguirla senza l'aiuto di un'altra persona. Al contrario, per una transazione Stonewall x2, un ulteriore partecipante, noto come "collaboratore", si unisce al processo. Questi contribuisce con i propri bitcoin alla transazione, insieme a quelli del mittente, e alla fine si appropria dell'intero importo (meno i costi della mining).



Torniamo all'esempio del Alice alla panetteria. Se avesse voluto effettuare una transazione Stonewall x2, il Alice avrebbe dovuto collaborare con il Bob (una terza parte) per impostare la transazione. Ognuno avrebbe portato un UTXO. Bob avrebbe ricevuto l'intero importo del suo contributo all'uscita. Il panettiere avrebbe ricevuto il pagamento per la sua baguette come nella transazione Stonewall, mentre Alice avrebbe recuperato il suo saldo iniziale, meno il costo della baguette.



![image](assets/fr/02.webp)



Da un punto di vista esterno, la transazione sarebbe rimasta esattamente la stessa.



![image](assets/fr/03.webp)



In sintesi, le transazioni Stonewall e Stonewall x2 hanno una struttura identica. La differenza tra le due sta nella loro natura collaborativa o non collaborativa. La transazione Stonewall viene sviluppata individualmente, senza bisogno di collaborazione. La transazione Stonewall x2, invece, si basa sulla cooperazione tra due persone per la sua realizzazione.



[**-> Scopri di più sulle transazioni Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Qual è lo scopo di una transazione Stonewall?



La struttura Stonewall aggiunge un'enorme quantità di entropia alla transazione, confondendo le linee di analisi della catena. Vista dall'esterno, una transazione di questo tipo può essere interpretata come una piccola unione di monete tra due persone. Ma in realtà, come la transazione Stonewall x2, si tratta di un pagamento. Questo metodo genera quindi incertezze nell'analisi della catena, o addirittura porta a false piste.



Prendiamo l'esempio del Alice dal panettiere. La transazione sulla blockchain avrebbe il seguente aspetto:



![image](assets/fr/04.webp)



Un osservatore esterno che si affidi alla comune euristica dell'analisi della catena potrebbe concludere erroneamente che "*due persone hanno realizzato una piccola coinjoin, con un UTXO ciascuno come ingresso e due UTXO ciascuno come uscita*".



![image](assets/fr/05.webp)



Questa interpretazione è imprecisa, perché, come sapete, un UTXO è stato inviato al panettiere, i 2 UTXO in arrivo provenivano da Alices, che ha recuperato 3 uscite di scambio.



![image](assets/fr/01.webp)



Anche se l'osservatore esterno riuscisse a identificare il paternità della transazione Stonewall, non disporrebbe di tutte le informazioni. Non sarà in grado di stabilire quale dei due UTXO di pari importo corrisponda al pagamento. Inoltre, non sarà in grado di stabilire se le due voci del UTXO provengono da due persone diverse o se appartengono a un'unica persona che le ha unite. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall x2, menzionate in precedenza, seguono esattamente lo stesso schema delle transazioni Stonewall. Se viste dall'esterno e senza ulteriori informazioni contestuali, è impossibile distinguere tra una transazione Stonewall e una transazione Stonewall x2. Le prime non sono transazioni collaborative, mentre le seconde lo sono. Questo aggiunge ancora più dubbi alla spesa.



![image](assets/fr/03.webp)



## Come si effettua una transazione Stonewall su Sparrow?



Originariamente sviluppate dal team Samurai Wallet, le transazioni di Stonewall sono state rilevate dall'applicazione Ashigaru, un fork del portfolio originale creato in seguito all'arresto degli sviluppatori di Samurai, e anche su Sparrow Wallet.



È necessario installare Sparrow e creare un file :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

A differenza delle transazioni Stowaway o Stonewall x2 (*coppie*), le transazioni Stonewall non richiedono l'uso di Paynyms. Possono essere effettuate direttamente, senza alcuna preparazione particolare o collaborazione con un altro utente.



Per eseguire una transazione Stonewall sul Sparrow, la procedura è molto semplice: iniziate creando una transazione come di consueto, tramite il menu `Invio` o dal menu `UTXOs` se desiderate fare il *Controllo Coin*.



![Image](assets/fr/06.webp)



Inserite quindi i dettagli della transazione: l'indirizzo del destinatario, un'etichetta, l'importo da inviare e l'importo o il tasso delle spese, a seconda delle condizioni di mercato.



![Image](assets/fr/07.webp)



Prima di confermare, è possibile selezionare la struttura Stonewall. Nella parte inferiore dell'interfaccia, sostituire `Efficienza` con `Privacy`. Se questa opzione non appare, significa che il vostro portafoglio non ha un numero sufficiente di UTXO per realizzare questo tipo di transazione.



![Image](assets/fr/08.webp)



Dopo aver selezionato l'opzione `Privacy`, noterete che la struttura della transazione è completamente modificata: diventa una transazione Stonewall, che consuma diversi dei vostri UTXO come input e produce due output di importi identici, uno dei quali corrisponde al pagamento effettivo di `100.000 sats`, oltre agli output di scambio.



![Image](assets/fr/09.webp)



Se tutto è corretto, fare clic su "Crea transazione".



È quindi possibile controllare i dettagli della transazione un'ultima volta e fare clic su "Finalizza transazione per la firma".



![Image](assets/fr/10.webp)



Firmate quindi la transazione secondo il metodo specifico per il vostro portafoglio e fate clic su "Trasmissione della transazione" per trasmetterla sulla rete Bitcoin, in attesa di conferma.



![Image](assets/fr/11.webp)



Ora sapete come funziona una transazione Stonewall su Sparrow Wallet e come crearne una. Per approfondire la padronanza di questi strumenti progettati per rafforzare la vostra riservatezza sulla catena, vi invito a seguire la mia formazione BTC 204 su Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c