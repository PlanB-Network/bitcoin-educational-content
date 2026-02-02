---
name: Ashigaru - Stonewall
description: Comprendere e utilizzare le transazioni Stonewall su Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Rompete i presupposti dell'analisi blockchain con il dubbio matematicamente dimostrabile tra mittente e destinatario delle vostre transazioni.*

## Cos'è una transazione Stonewall?



Stonewall è una forma specifica di transazione Bitcoin progettata per aumentare la riservatezza degli utenti quando spendono, imitando una coinjoin tra due persone, senza esserlo realmente. In realtà, questa transazione non è collaborativa. Un utente può costruirla da solo, usando solo gli UTXO che possiede come input. È quindi possibile creare una transazione Stonewall per qualsiasi occasione, senza doversi sincronizzare con un altro utente.



La transazione Stonewall funziona come segue: come input della transazione, l'emittente utilizza 2 UTXO che gli appartengono. In uscita, la transazione produce 4 uscite, 2 delle quali sono esattamente dello stesso importo. Gli altri due saranno valuta estera. Delle due uscite dello stesso importo, solo una andrà effettivamente al beneficiario.



Quindi ci sono solo 2 ruoli in una transazione Stonewall:




- L'emittente, che effettua il pagamento effettivo ;
- Il destinatario, che potrebbe non essere a conoscenza della natura specifica della transazione e si aspetta semplicemente il pagamento da parte del mittente.



Facciamo un esempio per capire questa struttura di transazione. Alice è dal panettiere per comprare la sua baguette, che costa `4.000 sats`. Vuole pagare in bitcoin, mantenendo una forma di riservatezza sul pagamento. Decide quindi di creare una transazione Stonewall per il pagamento.



![image](assets/fr/01.webp)



Analizzando questa transazione, possiamo vedere che il fornaio ha effettivamente ricevuto `4.000 sats` in pagamento per la baguette. Il Alice ha utilizzato 2 UTXO come input: uno di `10.000 sats` e uno di `15.000 sats`. Sul fronte dell'output, ha recuperato 3 UTXO: uno di `4.000 sats`, uno di `6.000 sats` e uno di `11.000 sats`. Alice ha quindi un saldo netto di `- 4.000 sats` su questa transazione, che corrisponde bene al prezzo della baguette.



In questo esempio, ho intenzionalmente trascurato le commissioni di mining per facilitarne la comprensione. In realtà, i costi di transazione sono interamente a carico dell'emittente.



## Qual è la differenza tra Stonewall e Stonewall x2?



La transazione Stonewall funziona in modo identico alla transazione StonewallX2, solo che quest'ultima richiede una collaborazione, a differenza della transazione Stonewall classica, da cui il nome "x2". Questo perché la transazione Stonewall viene eseguita senza bisogno di collaborazione esterna: il mittente può eseguirla senza l'aiuto di un'altra persona. Al contrario, per una transazione Stonewall x2, un ulteriore partecipante, noto come "collaboratore", si unisce al processo. Questi contribuisce con i propri bitcoin alla transazione, accanto a quelli del mittente, e si appropria dell'intero importo alla fine (modulo dei costi mining).



Torniamo all'esempio di Alice alla panetteria. Se avesse voluto effettuare una transazione Stonewall x2, il Alice avrebbe dovuto collaborare con il Bob (una terza parte) per impostare la transazione. Ognuno di loro avrebbe portato un UTXO. Il Bob avrebbe quindi ricevuto indietro il suo intero contributo. Il panettiere avrebbe ricevuto il pagamento della sua baguette come nella transazione Stonewall, mentre il Alice avrebbe recuperato il suo saldo iniziale, meno il costo della baguette.



![image](assets/fr/02.webp)



Da un punto di vista esterno, la transazione sarebbe rimasta esattamente la stessa.



![image](assets/fr/03.webp)



In sintesi, le transazioni Stonewall e Stonewall x2 hanno una struttura identica. La differenza tra le due sta nella loro natura collaborativa o non collaborativa. La transazione Stonewall viene sviluppata individualmente, senza bisogno di collaborazione. La transazione Stonewall x2, invece, si basa sulla cooperazione tra due persone per la sua realizzazione.



[**-> Scopri di più sulle transazioni Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Qual è lo scopo di una transazione Stonewall?



La struttura Stonewall aggiunge un'enorme quantità di entropia alla transazione, confondendo le linee di analisi della catena. Vista dall'esterno, una transazione di questo tipo può essere interpretata come una piccola unione di monete tra due persone. Ma in realtà, come la transazione Stonewall x2, si tratta di un pagamento. Questo metodo genera quindi incertezze nell'analisi della catena, o addirittura porta a false piste.



Prendiamo l'esempio del Alice dal panettiere. La transazione sulla blockchain avrebbe il seguente aspetto:



![image](assets/fr/04.webp)



Un osservatore esterno che si affidi alla comune euristica dell'analisi della catena potrebbe concludere erroneamente che "**due persone hanno realizzato una piccola coinjoin, con un UTXO ciascuno come ingresso e due UTXO ciascuno come uscita**".



![image](assets/fr/05.webp)



Questa interpretazione è imprecisa, perché, come sapete, un UTXO è stato inviato al panettiere, i 2 UTXO in entrata provenivano da Alices, e lei ha recuperato 3 uscite di cambio.



![image](assets/fr/01.webp)



Anche se l'osservatore esterno riuscisse a identificare il paternità della transazione Stonewall, non disporrebbe di tutte le informazioni. Non sarà in grado di determinare quale dei due UTXO di pari importo corrisponde al pagamento. Inoltre, non sarà in grado di stabilire se i due UTXO inseriti sono di due persone diverse o se appartengono a un'unica persona che li ha uniti. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall x2, menzionate in precedenza, seguono esattamente lo stesso schema delle transazioni Stonewall. Se viste dall'esterno e senza ulteriori informazioni contestuali, è impossibile distinguere tra una transazione Stonewall e una transazione Stonewall x2. Le prime non sono transazioni collaborative, mentre le seconde lo sono. Questo aggiunge ancora più dubbi alla spesa.



![image](assets/fr/03.webp)



## Come posso effettuare una transazione Stonewall su Ashigaru?



Originariamente sviluppate dal team Wallet di Samourai, le transazioni di Stonewall sono state rilevate dall'applicazione Ashigaru, un fork del wallet originale creato in seguito all'arresto degli sviluppatori di Samourai. È necessario installare Ashigaru e creare un wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

A differenza delle transazioni Stowaway o Stonewall x2 (*coppie*), le transazioni Stonewall non richiedono l'uso di Paynyms. Possono essere eseguite direttamente, senza preparazione preliminare o collaborazione con un altro utente.



In realtà, non è necessario un tutorial per effettuare le transazioni Stonewall, poiché Ashigaru le genera automaticamente ogni volta che si spende, non appena il wallet contiene abbastanza UTXO.



Fare clic sul pulsante `+` in basso a destra dello schermo, quindi selezionare `Invia`.



![Image](assets/fr/06.webp)



Selezionare il conto dal quale si desidera effettuare la spesa.



![Image](assets/fr/07.webp)



Inserite quindi i dettagli della transazione: l'indirizzo del destinatario e l'importo da inviare, e premete la freccia per confermare.



![Image](assets/fr/08.webp)



Qui è ovviamente possibile regolare le commissioni predefinite per le transazioni in base alle condizioni di mercato. Tuttavia, l'elemento più interessante di questa pagina è il tipo di transazione. Noterete che Ashigaru ha selezionato automaticamente `STONEWALL`. Cliccate sul pulsante `PREVIEW` per saperne di più.



![Image](assets/fr/09.webp)



Si può notare che la transazione è effettivamente del tipo Stonewall: comprende 2 ingressi dello stesso importo, 2 uscite dello stesso importo, oltre alle uscite di scambio e, nel mio caso, un ingresso aggiuntivo per soddisfare la somma di pagamento.



![Image](assets/fr/10.webp)



Se non si desidera effettuare una transazione Stonewall, ma si preferisce un pagamento tradizionale, fare clic sull'icona della matita in alto a destra dello schermo, quindi selezionare `Semplice` invece di `STONEWALL`.



![Image](assets/fr/11.webp)



Una volta controllati tutti i dettagli, trascinate la freccia verde in fondo alla schermata per firmare e rilasciare la transazione.



![Image](assets/fr/12.webp)



Ora sapete come effettuare una transazione Stonewall e, soprattutto, come funziona. Se volete saperne di più, date un'occhiata al mio tutorial sul Terminale Ashigaru, che spiega come effettuare coin join tramite Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
