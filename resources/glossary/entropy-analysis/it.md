---
term: ENTROPIA (ANALISI)

---
Nel contesto specifico dell'analisi delle catene, entropia è anche il nome di un indicatore, derivato dall'entropia di Shannon, inventato da LaurentMT. Questo indicatore permette di misurare la scarsa conoscenza che gli analisti hanno dell'esatta configurazione di una transazione Bitcoin. In altre parole, più alta è l'entropia di una transazione, più difficile diventa per gli analisti identificare i movimenti di bitcoin tra ingressi e uscite.

In pratica, l'entropia rivela se, dal punto di vista di un osservatore esterno, una transazione presenta molteplici interpretazioni possibili, basate esclusivamente sulle quantità di input e output, senza considerare altri modelli ed euristiche esterne o interne. Un'elevata entropia è quindi sinonimo di una migliore riservatezza della transazione.

L'entropia è definita come il logaritmo binario del numero di combinazioni possibili. Ecco la formula utilizzata con $E$ che rappresenta l'entropia della transazione e $C$ il numero di interpretazioni possibili:

$$
E = \log_2(C)
$$

Tenendo conto dei valori degli UTXO coinvolti nella transazione, il numero di interpretazioni $C$ rappresenta il numero di modi in cui gli input possono essere associati agli output. In altre parole, determina il numero di interpretazioni che una transazione può suscitare dal punto di vista di un osservatore esterno che la analizza.