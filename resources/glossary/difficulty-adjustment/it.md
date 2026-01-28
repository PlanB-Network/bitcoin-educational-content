---
term: Aggiustamento della difficoltà

definition: Processo periodico ogni 2016 blocchi che ridefinisce il target di difficoltà per mantenere un tempo medio di 10 minuti per blocco.
---
L'aggiustamento della difficoltà è un processo periodico che ridefinisce l'obiettivo di difficoltà per il meccanismo di proof of work (mining) su Bitcoin. Questo evento si verifica ogni 2016 blocchi (circa ogni due settimane). Serve ad aumentare o diminuire il fattore di difficoltà (chiamato anche obiettivo di difficoltà), a seconda della velocità con cui sono stati trovati gli ultimi blocchi del 2016. L'aggiustamento mira a mantenere un tasso di produzione di blocchi stabile e prevedibile, con una frequenza di un blocco ogni 10 minuti, nonostante le variazioni della potenza di calcolo impiegata dai minatori. La variazione della difficoltà durante l'aggiustamento è limitata a un fattore di 4. La formula eseguita dai nodi per calcolare il nuovo obiettivo è la seguente:

$$N = A \cdot \left(\frac{T}{1.209.600}\right)$$

Dove:


- $N$: Il nuovo obiettivo;
- $A$: Il vecchio obiettivo degli ultimi 2016 blocchi;
- $T$: Il tempo totale effettivo degli ultimi 2016 blocchi in secondi;
- $1,209,600$: Il tempo target in secondi per produrre 2016 blocchi con un intervallo di 10 minuti tra l'uno e l'altro.

