---
name: Ashigaru - Stonewall x2
description: Comprendere e utilizzare le transazioni Stonewall x2 su Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Rendere ogni spesa un coinjoin

## Cos'è una transazione Stonewall x2?



Stonewall x2 è una forma specifica di transazione Bitcoin progettata per aumentare la riservatezza dell'utente quando spende, collaborando con una terza parte non coinvolta nella spesa. Questo metodo simula una mini-coinjoin tra due partecipanti, mentre effettua un pagamento a una terza parte. Le transazioni Stonewall x2 sono disponibili sull'applicazione Ashigaru, una fork di Samourai Wallet (il team che ha creato questo tipo di transazione).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Il funzionamento è relativamente semplice: si utilizza un UTXO in proprio possesso per effettuare il pagamento e si chiede l'aiuto di una terza persona che contribuisce anch'essa con un UTXO di sua proprietà. La transazione si conclude con quattro uscite: due di uguale importo, una destinata all'indirizzo del beneficiario, l'altra a un indirizzo del collaboratore. Un terzo UTXO viene restituito a un altro indirizzo del collaboratore, permettendogli di recuperare l'importo iniziale (un'azione neutra per lui, oltre ai costi del mining), e un ultimo UTXO ritorna a un indirizzo di nostra proprietà, che costituisce lo scambio di pagamento.



Nelle transazioni Stonewall x2 vengono quindi definiti tre ruoli diversi:




- L'emittente, che effettua il pagamento effettivo ;
- Il collaboratore, che mette a disposizione i bitcoin per migliorare l'anonimato della transazione, recuperando alla fine i suoi fondi (un'azione neutra per lui, oltre ai costi di mining);
- Il destinatario, che potrebbe non essere a conoscenza della natura specifica della transazione e si aspetta semplicemente il pagamento da parte del mittente.



Facciamo un esempio. Alice è dal panettiere per comprare la sua baguette, che costa `4.000 sats`. Vuole pagare in bitcoin, mantenendo una certa riservatezza sul pagamento. Chiede quindi aiuto al suo amico Bob, che la aiuterà a farlo.



![image](assets/fr/01.webp)



Analizzando questa transazione, possiamo vedere che il fornaio ha effettivamente ricevuto `4.000 sats` in pagamento per la baguette. Alice ha utilizzato `10.000 sats` in input e ha recuperato `6.000 sats` in output, ottenendo un saldo netto di `4.000 sats`, che corrisponde al prezzo della baguette. Quanto al Bob, ha fornito `15.000 sats` in input e ha ricevuto due output: uno di `4.000 sats` e l'altro di `11.000 sats`, ottenendo un saldo di `0`.



In questo esempio, ho intenzionalmente trascurato le commissioni mining per rendere più facile la comprensione. In realtà, le commissioni di transazione sono suddivise in parti uguali tra l'emittente del pagamento e il collaboratore.



## Qual è la differenza tra Stonewall e Stonewall x2?



Una transazione StonewallX2 funziona esattamente come una transazione Stonewall, con la differenza che la prima è collaborativa, mentre la seconda no. Come abbiamo visto, una transazione Stonewall x2 prevede la partecipazione di una terza parte, esterna al pagamento, che metterà a disposizione i propri bitcoin per aumentare la riservatezza della transazione. In una transazione Stonewall classica, il ruolo di collaboratore è assunto dal mittente.



Torniamo all'esempio di Alice alla panetteria. Se non fosse stata in grado di trovare qualcuno come Bob che l'accompagnasse nella sua spesa, avrebbe potuto fare una Stonewall da sola. In questo modo, i due UTXO all'entrata sarebbero stati suoi e ne avrebbe raccolti 3 all'uscita.



![image](assets/fr/02.webp)




Da un punto di vista esterno, la transazione sarebbe rimasta invariata.



![image](assets/fr/05.webp)



La logica dovrebbe quindi essere la seguente quando si vuole utilizzare uno strumento di spesa Ashigaru:




- Se l'esercente non supporta Payjoin Stowaway, è possibile effettuare una transazione collaborativa con un'altra persona al di fuori del pagamento grazie a Stonewall x2 ;
- Se non si riesce a trovare nessuno che faccia una transazione Stonewall x2, si può fare una transazione solo Stonewall, che imiterà il comportamento di una transazione Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## A cosa serve una transazione Stonewall x2?



La struttura Stonewall x2 aggiunge un'enorme quantità di entropia alla transazione, confondendo l'analisi della catena. Vista dall'esterno, una transazione di questo tipo potrebbe essere interpretata come una piccola Coinjoin tra due persone. Ma in realtà si tratta di un pagamento. Questo metodo crea quindi incertezze nell'analisi della catena, o addirittura porta a false piste.



Prendiamo l'esempio di Alice, Bob e Boulanger. La transazione sulla blockchain avrebbe il seguente aspetto:



![image](assets/fr/03.webp)



Un osservatore esterno che si affidi alla comune euristica dell'analisi della catena potrebbe concludere erroneamente che "*Alice e Bob hanno effettuato un piccolo coinjoin, con un UTXO ciascuno in entrata e due UTXO ciascuno in uscita*".



![image](assets/fr/04.webp)



Questa interpretazione non è corretta perché, come sapete, un UTXO è stato inviato al Boulanger, il Alice ha una sola uscita di scambio e il Bob ne ha due.



![image](assets/fr/01.webp)



Anche se l'osservatore esterno riuscisse a identificare il paternità della transazione Stonewall x2, non disporrebbe di tutte le informazioni. Non sarà in grado di determinare quale dei due UTXO di pari importo corrisponda al pagamento. Né sarà in grado di stabilire se il pagamento è stato effettuato da Alice o da Bob. Infine, non sarà in grado di stabilire se i due UTXO inseriti sono di due persone diverse o se appartengono a un'unica persona che li ha uniti. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall classiche, discusse in precedenza, seguono esattamente lo stesso pateracchio delle transazioni Stonewall x2. Viste dall'esterno e senza ulteriori informazioni contestuali, è impossibile differenziare una transazione Stonewall da una transazione Stonewall x2. Le prime non sono transazioni collaborative, mentre le seconde lo sono. Questo aggiunge ancora più dubbi alla spesa.



![image](assets/fr/05.webp)




## Come si stabilisce una connessione tra Paynyms?



Come per altre transazioni collaborative su Ashigaru (*Cahoots*), Stonewall x2 prevede lo scambio di transazioni parzialmente firmate tra il mittente e il collaboratore. Questo scambio può essere effettuato manualmente, se si è fisicamente presenti con il collaboratore, o automaticamente utilizzando il protocollo di comunicazione Soroban.



Se si sceglie la seconda opzione, è necessario stabilire una connessione tra i Paynym prima di poter eseguire uno Stonewall x2. A tal fine, il vostro Paynym deve "*seguire*" il Paynym del vostro collaboratore e viceversa. Per sapere come fare, potete seguire l'inizio di quest'altro tutorial:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Come posso effettuare una transazione Stonewall x2 su Ashigaru?



Per effettuare una transazione Stonewall x2, cliccate sull'immagine del vostro Paynym nell'angolo in alto a sinistra dello schermo, quindi aprite il menu "Collabora". La persona che partecipa alla transazione con voi deve fare lo stesso, a meno che non vi scambiate i codici QR di persona.



![Image](assets/fr/06.webp)



Sono disponibili due opzioni: selezionare `Inizia` se si è il mittente del pagamento, oppure `Partecipa` se si è la persona che collabora alla transazione ma non è né il pagatore né il destinatario effettivo.



![Image](assets/fr/07.webp)



Se si ha il ruolo di collaboratore, la procedura è molto semplice. Per la collaborazione a distanza tramite la rete Soroban, cliccate su `Partecipa`, scegliete il conto che desiderate utilizzare, quindi premete `ATTENDERE LE RICHIESTE DI CAUSE` per attendere la richiesta inviata dal pagatore.



![Image](assets/fr/08.webp)



D'altra parte, per la collaborazione di persona tramite la scansione del codice QR, andare alla pagina iniziale del proprio wallet, premere l'icona del codice QR nella parte superiore dello schermo, quindi scansionare il codice QR fornito dal pagatore che avvia la transazione.



![Image](assets/fr/09.webp)



Se si ricopre il ruolo di pagatore, cioè di colui che avvia la transazione, andare al menu `Collaborare` e selezionare `Inizia`.



![Image](assets/fr/10.webp)



Per il tipo di transazione, dato che desideriamo eseguire una Stonewall x2, scegliere questa opzione.



![Image](assets/fr/11.webp)



È possibile scegliere tra la collaborazione online (*Cahoots* tramite *Soroban*) e la collaborazione faccia a faccia, con scambio di codici QR.



![Image](assets/fr/12.webp)



### Cahoots online



Se avete scelto l'opzione `Online`, selezionate il vostro collaboratore tra i Paynyms che state seguendo.



![Image](assets/fr/13.webp)



Cliccare su "Imposta transazione", quindi scegliere il conto dal quale si desidera effettuare la spesa.



![Image](assets/fr/14.webp)



Nella pagina successiva, inserite i dettagli della transazione: l'indirizzo del destinatario effettivo del pagamento, l'importo da inviare e il tasso di addebito. Cliccare quindi su "Rivedi l'impostazione della transazione".



![Image](assets/fr/15.webp)



Controllate attentamente le informazioni, assicuratevi che il vostro collaboratore ascolti le richieste di *Cahoots*, quindi cliccate sul pulsante verde `BEGIN TRANSACTION` per avviare lo scambio di PSBT tramite Soroban.



![Image](assets/fr/16.webp)



Attendere che entrambi i partecipanti abbiano firmato la transazione, quindi diffonderla sulla rete Bitcoin.



![Image](assets/fr/17.webp)



### Discussioni faccia a faccia



Se si desidera effettuare il cambio di persona, selezionare il tipo di transazione `STONEWALL X2`, quindi scegliere l'opzione `Di persona/manuale`.



![Image](assets/fr/18.webp)



Cliccare su "Imposta transazione", quindi scegliere il conto dal quale si desidera effettuare la spesa.



![Image](assets/fr/19.webp)



Nella pagina successiva, inserite i dettagli della transazione: l'indirizzo del destinatario effettivo del pagamento, l'importo da inviare e il tasso di addebito. Cliccare quindi su "Rivedi l'impostazione della transazione".



![Image](assets/fr/20.webp)



Controllare i dettagli, quindi premere il pulsante verde "INIZIA LA TRANSAZIONE" per avviare lo scambio di PSBT tramite la scansione del codice QR.



![Image](assets/fr/21.webp)



Lo scambio avviene alternando la scansione con il collaboratore: fate clic su "MOSTRA CODICE QR" per mostrare il vostro codice QR al collaboratore, che lo scansionerà. Egli farà quindi clic su "MOSTRA CODICE QR" per visualizzare il suo, e voi lo scansionerete con "LANCIA QR Scanner". Ripetete questa procedura fino a completare tutte e cinque le fasi dello scambio.



![Image](assets/fr/22.webp)



Una volta completati tutti gli scambi, controllare i dettagli della transazione, quindi rilasciarla trascinando la freccia verde nella parte inferiore dello schermo.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). La sua struttura è la seguente:



![Image](assets/fr/24.webp)



*Credito: [mempool.space](https://mempool.space/)*



Possiamo osservare due ingressi dal mio portafoglio, rispettivamente `91.869 sats` e `64.823 sats`, mentre gli altri due ingressi provengono dal wallet del mio collaboratore. In uscita, un UTXO di `100.000 sats` viene inviato al beneficiario effettivo e due UTXO di `100.000 sats` e `159.578 sats` ritornano nel portafoglio del mio collaboratore. Per lui l'operazione è neutra, in quanto recupera l'intero ammontare dei fondi che aveva investito nell'input (esclusi i costi del mining a cui ha contribuito). Infine, ricevo uno scambio UTXO di `56.270 sats`, corrispondente alla differenza tra i miei input totali e il pagamento di `100.000 sats` inviato al destinatario.



Ovviamente, posso descrivere questa struttura perché ho costruito io stesso la transazione. Ma per un osservatore esterno è generalmente impossibile determinare quali UTXO appartengono a quale partecipante, sia in ingresso che in uscita.



Per approfondire la conoscenza della gestione della privacy onchain su Bitcoin, vi consiglio di seguire il mio corso BTC 204 su Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c