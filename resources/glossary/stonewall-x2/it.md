---
term: MURO DI PIETRA X2

---
Una forma specifica di transazione Bitcoin volta ad aumentare la privacy dell'utente durante una spesa, collaborando con una terza parte non coinvolta nella spesa. Questo metodo simula una mini-coinjoin tra due partecipanti, mentre effettua un pagamento a una terza parte. Le transazioni Stonewall x2 sono disponibili sia sull'applicazione Samourai Wallet che sul software Sparrow Wallet (entrambi sono interoperabili).

Il suo funzionamento è relativamente semplice: utilizza un UTXO in nostro possesso per effettuare il pagamento e chiede l'aiuto di una terza persona che contribuisce anch'essa con un UTXO di sua proprietà. La transazione si conclude con quattro uscite: due di uguale importo, una destinata all'indirizzo del destinatario del pagamento, l'altra a un indirizzo del collaboratore. Un terzo UTXO viene rispedito a un altro indirizzo del collaboratore, consentendogli di recuperare l'importo iniziale (un'azione neutra per loro, meno le commissioni di estrazione), e un ultimo UTXO ritorna a un indirizzo di nostra proprietà, che costituisce la variazione del pagamento. Pertanto, nelle transazioni Stonewall x2 sono definiti tre ruoli diversi:


- Il mittente, che effettua il pagamento effettivo;
- Il collaboratore, che fornisce bitcoin per migliorare l'anonimato generale della transazione, recuperando completamente i propri fondi alla fine;
- Il destinatario, che potrebbe non essere a conoscenza della natura specifica della transazione e attende semplicemente il pagamento da parte del mittente.

![](../../dictionnaire/assets/3.webp)

La struttura Stonewall x2 aggiunge molta entropia alla transazione e confonde le tracce dell'analisi della catena. Dall'esterno, una transazione di questo tipo può essere interpretata come una piccola unione di monete tra due persone. Ma in realtà si tratta di un pagamento. Questo metodo genera quindi incertezze nell'analisi della catena, o addirittura porta a false piste. Anche se un osservatore esterno riuscisse a identificare lo schema della transazione Stonewall x2, non disporrebbe di tutte le informazioni. Non sarà in grado di determinare quale dei due UTXO di pari importo corrisponde al pagamento. Inoltre, non saranno in grado di sapere chi ha effettuato il pagamento. Infine, non potranno stabilire se i due UTXO in ingresso provengono da due persone diverse o se appartengono a un'unica persona che li ha uniti. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall classiche seguono esattamente lo stesso schema delle transazioni Stonewall x2. Dall'esterno e senza ulteriori informazioni sul contesto, è impossibile distinguere una transazione Stonewall da una transazione Stonewall x2. Tuttavia, le prime non sono transazioni collaborative, mentre le seconde lo sono. Questo aggiunge ulteriori dubbi sulla spesa.