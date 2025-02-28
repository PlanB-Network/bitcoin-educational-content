---
term: LUCRO

---
Un indicatore utilizzato nei pool minerari per misurare le prestazioni di un pool rispetto alle sue aspettative teoriche. Come suggerisce il nome, valuta la fortuna del pool nel trovare un blocco. La fortuna viene calcolata confrontando il numero di azioni teoricamente necessarie per trovare un blocco valido, in base alla difficoltà attuale di Bitcoin, con il numero effettivo di azioni prodotte per trovare quel blocco. Un numero di azioni inferiore a quello previsto indica una buona fortuna, mentre un numero superiore indica una cattiva fortuna.

Mettendo in relazione la difficoltà di Bitcoin con il numero di azioni prodotte ogni secondo e la difficoltà di ogni azione, il pool può calcolare il numero di azioni teoricamente necessarie per trovare un blocco valido. Ad esempio, supponiamo che teoricamente un pool abbia bisogno di 100.000 azioni per trovare un blocco. Se il pool ne produce effettivamente 200.000 prima di trovare un blocco, la sua fortuna è del 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Al contrario, se questo pool ha trovato un blocco valido dopo aver prodotto solo 50.000 azioni, la sua fortuna è del 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Luck è un indicatore che può essere aggiornato solo dopo che un blocco viene scoperto dal pool, il che lo rende un indicatore statico che viene aggiornato periodicamente.