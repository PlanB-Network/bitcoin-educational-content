---
termine: STACK
---

Nel contesto del linguaggio di scripting utilizzato per applicare condizioni di spesa sui Bitcoin UTXOs, lo stack è una struttura dati "LIFO" (*Last In, First Out*, Ultimo Entrato, Primo Uscito) che serve a memorizzare elementi temporanei durante l'esecuzione di uno script. Ogni operazione nello script manipola questi stack, dove gli elementi possono essere aggiunti (*push*) o rimossi (*pop*). Gli script utilizzano gli stack per valutare espressioni, memorizzare variabili temporanee e gestire condizioni.

Durante l'esecuzione di uno script Bitcoin, possono essere utilizzati 2 stack: lo stack principale e lo stack alternativo (alt). Lo stack principale è utilizzato per la maggior parte delle operazioni di uno script. È su questo stack che le operazioni dello script aggiungono, rimuovono o manipolano i dati. Lo stack alternativo, d'altra parte, serve a memorizzare temporaneamente i dati durante l'esecuzione dello script. Specifici opcode, come `OP_TOALTSTACK` e `OP_FROMALTSTACK`, permettono il trasferimento di elementi dallo stack principale allo stack alternativo e viceversa.

Ad esempio, durante la validazione di una transazione, le firme e le chiavi pubbliche vengono inserite nello stack principale e processate da successivi opcode per verificare che le firme corrispondano alle chiavi e ai dati della transazione.

> ► *In inglese, la traduzione di « pile » è « stack ». Il termine inglese è generalmente utilizzato anche in francese durante le discussioni tecniche.*