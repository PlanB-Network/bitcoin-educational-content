---
termine: DURATA MEDIA ROUND
---

La durata media di un round è un indicatore utilizzato per stimare il tempo necessario a un pool di mining per trovare un blocco, basandosi sulla difficoltà della rete e sul hashrate del pool. Viene calcolato prendendo il numero di share necessarie per trovare un blocco e dividendo tale numero per il hashrate del pool. Ad esempio, se un pool di mining ha 200 minatori, e ognuno genera in media 4 share al secondo, la potenza computazionale totale del pool è di 800 share al secondo:

```text
200 * 4 = 800
```

Assumendo che, in media, siano necessarie 1 milione di share per trovare un blocco valido, la *Durata Media Round* del pool sarebbe di 1.250 secondi, o circa 21 minuti:

```text
1.000.000 / 800 = 1.250
```

In termini pratici, ciò significa che, in media, il pool di mining dovrebbe trovare un blocco ogni 21 minuti circa. Questo indicatore fluttua con i cambiamenti nel hashrate del pool: un aumento del hashrate riduce la *Durata Media Round*, mentre una diminuzione la prolunga. Fluttuerà anche con ogni aggiustamento periodico del target di difficoltà di Bitcoin (ogni 2016 blocchi). Questa misura non tiene conto dei blocchi trovati da altri pool e si concentra esclusivamente sulla performance interna del pool in esame.