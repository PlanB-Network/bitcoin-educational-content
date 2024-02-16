---
name: Stonewall
description: Comprensione e utilizzo delle transazioni Stonewall
---
![cover stonewall](assets/cover.jpeg)

> *"Rompi le supposizioni dell'analisi della blockchain con un dubbio matematicamente provabile tra mittente e destinatario delle tue transazioni."*

## Cosa è una transazione Stonewall?
Stonewall è una forma specifica di transazione Bitcoin mirata ad aumentare la privacy dell'utente durante una spesa, imitando un coinjoin tra due persone, senza essere effettivamente tale. Infatti, questa transazione non è collaborativa. Un utente può costruirla da solo, coinvolgendo solo i propri UTXO come input. Pertanto, è possibile creare una transazione Stonewall per qualsiasi occasione senza bisogno di sincronizzarsi con un altro utente.

Il funzionamento di una transazione Stonewall è il seguente: come input della transazione, il mittente utilizza 2 UTXO che gli appartengono. Come output, la transazione produce 4 output, di cui 2 saranno esattamente della stessa quantità. Gli altri 2 saranno resto. Tra i 2 output della stessa quantità, solo uno andrà effettivamente al destinatario del pagamento.

Pertanto, ci sono solo 2 ruoli in una transazione Stonewall:
- Il mittente, che effettua il pagamento effettivo;
- Il destinatario, che può ignorare la natura specifica della transazione e semplicemente aspettarsi un pagamento dal mittente.

Prendiamo un esempio per capire questa struttura di transazione. Alice è in panetteria per comprare la sua baguette, che costa 4.000 sats. Vuole pagare in bitcoin mantenendo un certo livello di privacy per il suo pagamento. Pertanto, decide di costruire una transazione Stonewall per il pagamento.
![transaction stonewall bakery](assets/it/1.png)
Analizzando questa transazione, possiamo vedere che il panettiere ha effettivamente ricevuto 4.000 sats come pagamento per la baguette. Alice ha utilizzato 2 UTXO come input: uno da 10.000 sats e uno da 15.000 sats. Come output, ha ricevuto 3 UTXO: uno da 4.000 sats, uno da 6.000 sats e uno da 11.000 sats. Alice ha quindi un saldo netto di -4.000 sats in questa transazione, che corrisponde al prezzo della baguette.

In questo esempio, ho intenzionalmente trascurato le commissioni di mining per facilitare la comprensione. In realtà, le commissioni di transazione sono interamente coperte dal mittente.

Qual è la differenza tra Stonewall e Stonewall x2?
La transazione Stonewall funziona allo stesso modo della transazione StonewallX2, con l'eccezione che quest'ultima richiede la collaborazione, a differenza della classica transazione Stonewall, da qui la designazione "x2". Infatti, la transazione Stonewall può essere eseguita senza la collaborazione esterna: il mittente può completarla senza l'aiuto di un'altra persona. Tuttavia, per una transazione Stonewall x2, un partecipante aggiuntivo, chiamato "collaboratore", si unisce al processo. Il collaboratore contribuisce con i propri bitcoin come input, insieme a quelli del mittente, e riceve l'intera somma come output (meno le commissioni di mining).

Riprendiamo il nostro esempio con Alice in panetteria. Se avesse voluto effettuare una transazione Stonewall x2, Alice avrebbe dovuto collaborare con Bob (un terzo soggetto) durante la creazione della transazione. Ognuno avrebbe fornito un UTXO come input. Bob avrebbe quindi ricevuto l'intera sua contribuzione come output. Il panettiere avrebbe ricevuto il pagamento per la baguette allo stesso modo della transazione Stonewall, mentre Alice avrebbe ricevuto il suo saldo iniziale, meno il costo della baguette.
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)
Come traduttore professionista esperto, il mio compito principale è tradurre con precisione contenuti tecnici dalla lingua di origine in italiano, la mia lingua madre. Seguirò le seguenti linee guida per garantire una traduzione di alta qualità:

Lingua di origine: Il contenuto è originariamente nella lingua di origine.
Natura del contenuto: Mi troverò di fronte a materiale tecnico, potenzialmente includendo terminologia specifica del settore.
Link e termini tecnici: Non tradurrò gli URL o termini tecnici altamente specifici. Se non sono sicuro, manterrò il termine originale.
Coerenza della formattazione: Manterrò lo stesso layout e la stessa formattazione del testo originale. La coerenza della struttura è fondamentale.
Proprietà YML: Se una riga inizia con una proprietà YML (ad esempio, 'name:', 'goal:', 'objectives:'), manterrò il nome della proprietà in inglese.
Contesto culturale: Per riferimenti culturali o specifici del contesto che potrebbero non tradursi direttamente, parafraserò per preservare il significato inteso o fornirò una breve spiegazione.
L'accento sarà posto nel mantenere l'integrità del contenuto tecnico, garantendo al contempo che la traduzione sia comprensibile e accurata dal punto di vista contestuale in italiano.

Questo è il testo da tradurre:
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Risorse esterne:**
- https://docs.samourai.io/en/spend-tools#stonewall ;
- https://samouraiwallet.com/stonewall.
