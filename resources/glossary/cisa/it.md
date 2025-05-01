---
term: CISA
---

Acronimo di "Cross-Input Signature Aggregation". Si tratta di una proposta tecnica volta a ottimizzare le dimensioni delle transazioni Bitcoin riducendo il numero di firme necessarie per convalidarle.


Attualmente, sul Bitcoin, ogni input di una transazione deve avere una firma individuale prima di poter essere consumato. Questo dimostra che il proprietario del UTXO in questione ha autorizzato la transazione. Con CISA, l'obiettivo è quello di combinare le firme di tutti gli input di una singola transazione in un'unica firma che copra tutti gli input. Ciò consentirebbe di ridurre le dimensioni delle transazioni con molti input e quindi anche i loro costi. Ciò sarebbe particolarmente utile per chi effettua coinjoin o consolidamenti, consentendo al contempo di confermare un maggior numero di transazioni su Bitcoin senza alterare le dimensioni dei blocchi o gli intervalli. Il CISA si basa sul protocollo Schnorr, che consente l'aggregazione lineare delle firme. Ciò significa che una singola firma può dimostrare il possesso di diverse chiavi indipendenti.


Tuttavia, l'implementazione di CISA su Bitcoin è molto complessa, poiché richiede profondi cambiamenti nel funzionamento degli script. Attualmente, la verifica degli script su Bitcoin avviene ingresso per ingresso. Passare a un modello in cui un'intera transazione viene verificata in una sola volta, come proposto da CISA, è un cambiamento tutt'altro che banale.