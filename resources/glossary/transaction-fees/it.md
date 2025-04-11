---
term: COMMISSIONI DI TRANSAZIONE

---
Le commissioni di transazione rappresentano una somma che mira a compensare i minatori per la loro partecipazione al meccanismo di proof of work. Queste commissioni incoraggiano i minatori a includere le transazioni nei blocchi che creano. Esse derivano dalla differenza tra il totale degli input e il totale degli output di una transazione:

```text
fees = inputs - outputs
```

Sono espresse in `sats/vBytes`, il che significa che le commissioni non dipendono dalla quantità di bitcoin inviati, ma dal peso della transazione. Sono scelte liberamente dal mittente di una transazione e determinano la sua velocità di inclusione in un blocco attraverso un meccanismo di asta. Ad esempio, supponiamo che io effettui una transazione con un input di `100.000 sats`, un output di `40.000 sats` e un altro output di `58.500 sats`. Il totale delle uscite è di `98.500 sats`. Le tariffe assegnate a questa transazione sono di `1.500 sats`. Il minatore che include la mia transazione può creare `1.500 sats` nella sua transazione su coinbase in cambio dei `1.500 sats` che non ho recuperato nelle mie uscite.

Le transazioni con tariffe più elevate, in relazione alle loro dimensioni, sono trattate come prioritarie dai minatori, il che può accelerare il processo di conferma. Al contrario, le transazioni con commissioni più basse possono essere ritardate durante i periodi di alta congestione. Vale la pena notare che le commissioni delle transazioni Bitcoin sono distinte dalla sovvenzione di blocco, che è un ulteriore incentivo per i minatori. La ricompensa del blocco consiste in nuovi bitcoin creati con ogni blocco minato (block subsidy), oltre alle commissioni di transazione raccolte. Mentre la sovvenzione di blocco diminuisce nel tempo a causa del limite di fornitura totale di bitcoin, le commissioni di transazione continueranno a svolgere un ruolo cruciale nell'incoraggiare i minatori a partecipare.

A livello di protocollo, nulla impedisce agli utenti di includere in un blocco transazioni senza commissioni. In realtà, questo tipo di transazione senza commissioni è eccezionale. Per impostazione predefinita, i nodi Bitcoin non trasmettono transazioni con commissioni inferiori a `1 sat/vByte`. Se alcune transazioni senza commissioni sono passate, è perché sono state integrate direttamente dal miner vincente, senza attraversare la rete di nodi. Ad esempio, la seguente transazione non prevede commissioni:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

In questo esempio specifico, si trattava di una transazione avviata dal direttore del pool minerario F2Pool. Come utente regolare, il limite inferiore attuale è quindi di `1 sat/vByte`.

È inoltre necessario considerare i limiti del purging. Durante i periodi di alta congestione, i mempool dei nodi eliminano le transazioni in sospeso al di sotto di una certa soglia, al fine di rispettare il limite di RAM assegnato. Questo limite è liberamente scelto dall'utente, ma molti lasciano il valore predefinito di Bitcoin Core a 300 MB. Può essere modificato nel file `bitcoin.conf` con il parametro `maxmempool`.

> *In inglese, ci si riferisce ad esso come "transaction fees"