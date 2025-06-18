---
term: BATTERIA
---

Nel contesto del linguaggio di scripting utilizzato per apporre condizioni di spesa agli UTXO Bitcoin, lo stack è una struttura di dati LIFO (*Last In, First Out*) utilizzata per memorizzare Elements temporanei durante l'esecuzione dello script. Ogni operazione dello script manipola queste pile, dove il Elements può essere aggiunto (*push*) o rimosso (*pop*). Gli script utilizzano gli stack per valutare le espressioni, memorizzare le variabili temporanee e gestire le condizioni.


Quando si esegue uno script Bitcoin, si possono utilizzare due stack: lo stack principale e lo stack alt (alternativo). Lo stack principale viene utilizzato per la maggior parte delle operazioni di script. È su questo stack che le operazioni di script aggiungono, rimuovono o manipolano i dati. Lo stack alternativo, invece, viene utilizzato per memorizzare temporaneamente i dati durante l'esecuzione dello script. Codici operativi specifici, come `OP_TOALTSTACK` e `OP_FROMALTSTACK`, consentono di trasferire Elements dallo stack principale allo stack alternativo e viceversa.


Ad esempio, quando una transazione viene convalidata, le firme e le chiavi pubbliche vengono inserite nello stack principale ed elaborate da opcode successivi per verificare che le firme corrispondano alle chiavi e ai dati della transazione.