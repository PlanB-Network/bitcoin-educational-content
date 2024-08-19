---
termine: DIFFICULTY ADJUSTMENT
---

La regolazione della difficoltà è un processo periodico che ridefinisce l'obiettivo di difficoltà per il meccanismo di proof of work (mining) su Bitcoin. Questo evento si verifica ogni 2016 blocchi (circa ogni due settimane). Serve per aumentare o diminuire il fattore di difficoltà (chiamato anche target di difficoltà), a seconda della rapidità con cui sono stati trovati gli ultimi 2016 blocchi. L'aggiustamento mira a mantenere un tasso di produzione di blocchi stabile e prevedibile, con una frequenza di un blocco ogni 10 minuti, nonostante le variazioni nella potenza computazionale impiegata dai minatori. La variazione della difficoltà durante l'aggiustamento è limitata a un fattore di 4. La formula eseguita dai nodi per calcolare il nuovo target è la seguente:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Dove:
* $N$: Il nuovo target;
* $A$: Il vecchio target degli ultimi 2016 blocchi;
* $T$: Il tempo totale effettivo degli ultimi 2016 blocchi in secondi;
* $1,209,600$: Il tempo target in secondi per produrre 2016 blocchi con un intervallo di 10 minuti tra ciascuno.

> ► *In francese, il termine "reciblage" è talvolta usato anche per riferirsi alla regolazione. In inglese, è denominato "Difficulty Adjustment".*