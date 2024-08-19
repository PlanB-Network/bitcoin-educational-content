---
termine: DEPTH
---

Nel contesto dei portafogli HD (Hierarchical Deterministic), depth si riferisce al livello specifico di una chiave (pubblica o privata), un codice catena, una chiave estesa o un indirizzo all'interno della struttura di derivazione del portafoglio dal master key. Ogni livello di questa struttura può essere visto come un piano in un albero di chiavi, dove il master key si trova alla radice (depth 0) e i livelli successivi definiscono vari attributi come:
lo scopo (depth 1), il tipo di valuta (depth 2), l'account (depth 3), il tipo di catena (depth 4) e l'indice dell'indirizzo specifico (depth 5).

![](../../dictionnaire/assets/18.png)

Per passare da un livello di profondità al successivo, viene utilizzato un processo di derivazione da una coppia di chiavi genitore a una coppia di chiavi figlio.

> ► *Il termine "piano di derivazione" è talvolta usato al posto di depth.*