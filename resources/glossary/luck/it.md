---
term: LUCK
---

Un indicatore utilizzato nelle mining pool per misurare la performance di una pool rispetto alle sue aspettative teoriche. Come suggerisce il nome, valuta la fortuna della pool nel trovare un blocco. La fortuna (Luck) è calcolata confrontando il numero di share teoricamente necessarie per trovare un blocco valido, basandosi sulla difficoltà corrente di Bitcoin, con il numero effettivo di share prodotte per trovare quel blocco. Un numero di share inferiore al previsto indica buona fortuna, mentre un numero superiore indica cattiva fortuna.

Correlando la difficoltà su Bitcoin con il suo numero di share prodotte ogni secondo e la difficoltà di ogni share, la pool può calcolare il numero di share teoricamente necessarie per trovare un blocco valido. Per esempio, supponiamo che teoricamente servano 100.000 share affinché una pool trovi un blocco. Se la pool effettivamente produce 200.000 share prima di trovare un blocco, la sua fortuna è del 50%:

```text
100.000 / 200.000 = 0,5 = 50%
```

Al contrario, se questa pool trovasse un blocco valido dopo aver prodotto solo 50.000 share, allora la sua fortuna è del 200%:

```text
100.000 / 50.000 = 2 = 200%
```

La fortuna è un indicatore che può essere aggiornato solo dopo che un blocco è stato scoperto dalla pool, rendendolo un indicatore statico che viene aggiornato periodicamente.