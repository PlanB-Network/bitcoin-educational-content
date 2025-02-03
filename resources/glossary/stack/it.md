---
term: STACCO

---
Nel contesto del linguaggio di scripting utilizzato per applicare le condizioni di spesa sugli UTXO Bitcoin, lo stack è una struttura di dati "LIFO" (*Last In, First Out*) che serve a memorizzare elementi temporanei durante l'esecuzione di uno script. Ogni operazione dello script manipola questi stack, dove gli elementi possono essere aggiunti (*push*) o rimossi (*pop*). Gli script utilizzano gli stack per valutare espressioni, memorizzare variabili temporanee e gestire condizioni.

Durante l'esecuzione di uno script Bitcoin, possono essere utilizzati due stack: lo stack principale e lo stack alt (alternativo). Lo stack principale è utilizzato per la maggior parte delle operazioni di uno script. È su questo stack che le operazioni di script aggiungono, rimuovono o manipolano i dati. Lo stack alternativo, invece, serve a memorizzare temporaneamente i dati durante l'esecuzione dello script. Codici operativi specifici, come `OP_TOALTSTACK` e `OP_FROMALTSTACK`, consentono di trasferire elementi dallo stack principale a quello alternativo e viceversa.

Ad esempio, durante la convalida di una transazione, le firme e le chiavi pubbliche vengono inserite nello stack principale ed elaborate da opcode successivi per verificare che le firme corrispondano alle chiavi e ai dati della transazione.

> *In inglese, la traduzione di "pile" è "stack". Il termine inglese è generalmente usato anche in francese durante le discussioni tecniche