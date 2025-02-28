---
term: ETICHETTA (PAGAMENTI SILENZIOSI)

---
Nel protocollo Silent Payments, le etichette sono numeri interi utilizzati per modificare l'indirizzo statico iniziale al fine di creare molti altri indirizzi statici. L'uso di queste etichette consente di segregare i pagamenti inviati tramite Silent Payments, impiegando indirizzi statici diversi per ogni utilizzo, senza aumentare eccessivamente l'onere operativo per la rilevazione di questi pagamenti (scansione). Bob utilizza un indirizzo statico $B$, composto da due chiavi pubbliche: $B_{\text{scan}}$ per la scansione e $B_{\text{spend}}$ per la spesa. L'hash di $b_{\text{scan}}$ e di un intero $m$, moltiplicato scalarmente per il punto generatore $G$, viene aggiunto alla chiave pubblica di spesa $B_{\text{spend}}$ per creare una sorta di nuova chiave pubblica di spesa $B_m$:

$$ B_m = B_{{testo{spesa}} + \text{hash}(b_{text{scan}} \text{ ‖ } m) \cdot G $$

Ad esempio, la prima chiave $B_1$ si ottiene in questo modo:

$$ B_1 = B_{{text{spend}} + \text{hash}(b_{testo{scan}} \text{ ‖ } 1) \cdot G $$

L'indirizzo statico pubblicato da Bob sarà ora composto da $B_{\text{scan}}$ e $B_m$. Ad esempio, il primo indirizzo statico con etichetta $1$ sarà:

$$ B = B_{{testo{scan}} \text{ ‖ } B_1 $$

Si parte solo dall'etichetta $1$, perché l'etichetta $0$ è riservata alle modifiche. Alice, che desidera inviare bitcoin all'indirizzo statico etichettato fornito da Bob, ricaverà l'indirizzo di pagamento univoco $P_0$ utilizzando la nuova $B_1$ invece di $B_{text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{text{scan}} \text{ ‖ } 0) \cdot G$

In realtà, Alice potrebbe anche non sapere che Bob ha un indirizzo etichettato, poiché utilizza semplicemente la seconda parte dell'indirizzo statico fornito, che in questo caso è il valore $B_1$ piuttosto che $B_{\text{spend}}$. Per effettuare la scansione dei pagamenti, Bob utilizzerà sempre il valore del suo indirizzo statico iniziale con $B_{\text{spend}}$ in questo modo:

$$ P_0 = B_{{testo{spesa}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Quindi, sottrarrà semplicemente il valore trovato per $P_0$ da ogni uscita, una per una. Quindi controlla se uno dei risultati di queste sottrazioni corrisponde al valore di una delle etichette utilizzate nel suo portafoglio. Se corrisponde, ad esempio, all'uscita #4 con l'etichetta $1$, significa che questa uscita è un Pagamento silenzioso associato al suo indirizzo statico con l'etichetta $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G$

Questo funziona perché:

$$ B_1 = B_{{text{spend}} + \text{hash}(b_{testo{scan}} \text{ ‖ } 1) \cdot G $$

Grazie a questo metodo, Bob può utilizzare una moltitudine di indirizzi statici (con $B_1$, $B_2$, $B_3$...), tutti derivati dal suo indirizzo statico di base ($B = B_{{text{scan}} \text{ ‖ } B_{{text{spend}}$), al fine di separare correttamente gli usi.

Tuttavia, questa separazione degli indirizzi statici è valida solo dal punto di vista della gestione del portafoglio personale, ma non consente di separare le identità. Poiché tutti hanno lo stesso $B_{{text{scan}}$, è molto facile associare tutti gli indirizzi statici insieme e dedurre che appartengono a un'unica entità.