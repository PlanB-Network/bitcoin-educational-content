---
term: AVG. DURATA DEL GIRO

---
La durata media del round è un indicatore utilizzato per stimare il tempo necessario a un pool di mining per trovare un blocco, in base alla difficoltà della rete e all'hashrate del pool. Si calcola prendendo il numero di azioni previste per trovare un blocco e dividendolo per l'hashrate del pool. Ad esempio, se un pool di mining ha 200 minatori e ognuno genera in media 4 azioni al secondo, la potenza di calcolo totale del pool è di 800 azioni al secondo:

```text
200 * 4 = 800
```

Supponendo che, in media, ci vogliano 1 milione di azioni per trovare un blocco valido, la *durata media del pool* sarebbe di 1.250 secondi o circa 21 minuti. Round Duration* sarebbe di 1.250 secondi, ovvero circa 21 minuti:

```text
1,000,000 / 800 = 1,250
```

In termini pratici, ciò significa che, in media, il pool di mining dovrebbe trovare un blocco ogni 21 minuti circa. Questo indicatore fluttua con le variazioni dell'hashrate del pool: un aumento dell'hashrate riduce l'*Avg. Round Duration*, mentre una diminuzione la estende. Inoltre, fluttua ad ogni adeguamento periodico dell'obiettivo di difficoltà del Bitcoin (ogni 2016 blocchi). Questa misura non tiene conto dei blocchi trovati da altri pool e si concentra esclusivamente sulle prestazioni interne del pool in esame.