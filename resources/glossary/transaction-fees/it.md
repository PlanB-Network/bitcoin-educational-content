---
term: COMMISSIONI DI TRANSAZIONE
---

Le commissioni di transazione rappresentano una somma che mira a compensare i minatori per la loro partecipazione al meccanismo di proof of work. Queste commissioni incoraggiano i minatori a includere le transazioni nei blocchi che creano. Derivano dalla differenza tra l'importo totale degli input e l'importo totale degli output in una transazione:

```text
commissioni = input - output
```

Sono espresse in `sats/vByte`, il che significa che le commissioni non dipendono dall'importo di bitcoin inviati, ma dal peso della transazione. Sono liberamente scelte dal mittente di una transazione e ne determinano la velocità di inclusione in un blocco attraverso un meccanismo d'asta. Per esempio, diciamo che effettuo una transazione con un input di `100.000 sats`, un output di `40.000 sats` e un altro output di `58.500 sats`. Il totale degli output è `98.500 sats`. Le commissioni allocate a questa transazione sono `1.500 sats`. Il minatore che include la mia transazione può creare `1.500 sats` nella loro transazione coinbase in cambio dei `1.500 sats` che non ho recuperato nei miei output.

Le transazioni con commissioni più elevate, rispetto alla loro dimensione, sono trattate come prioritarie dai minatori, il che può accelerare il processo di conferma. Al contrario, le transazioni con commissioni più basse possono subire ritardi durante periodi di alta congestione. È importante notare che le commissioni di transazione Bitcoin sono distinte dal sussidio di blocco, che è un incentivo aggiuntivo per i minatori. La ricompensa del blocco consiste in nuovi bitcoin creati con ogni blocco estratto (sussidio di blocco), oltre alle commissioni di transazione raccolte. Mentre il sussidio di blocco diminuisce nel tempo a causa del limite dell'offerta totale di bitcoin, le commissioni di transazione continueranno a svolgere un ruolo cruciale nell'incoraggiare i minatori a partecipare.

A livello di protocollo, nulla impedisce agli utenti di includere transazioni senza commissioni in un blocco. Nella realtà, questo tipo di transazione senza commissioni è eccezionale. Per impostazione predefinita, i nodi Bitcoin non inoltrano transazioni con commissioni inferiori a `1 sat/vByte`. Se alcune transazioni senza commissioni sono passate, è perché sono state integrate direttamente dal minatore vincente, senza attraversare la rete di nodi. Per esempio, la seguente transazione non include commissioni:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

In questo esempio specifico, si trattava di una transazione avviata dal direttore del pool di mining F2Pool. Come utente regolare, il limite inferiore attuale è quindi `1 sat/vByte`.
È anche necessario considerare i limiti di purga. Durante periodi di alta congestione, i mempool dei nodi purgano le loro transazioni in sospeso al di sotto di una certa soglia, al fine di rispettare il loro limite di RAM allocata. Questo limite è liberamente scelto dall'utente, ma molti lasciano il valore predefinito di Bitcoin Core a 300 MB. Può essere modificato nel file `bitcoin.conf` con il parametro `maxmempool`.
> ► *In inglese, ci riferiamo ad esse come "transaction fees".*