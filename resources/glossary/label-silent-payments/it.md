---
termine: LABEL (PAGAMENTI SILENZIOSI)
---

Nel protocollo dei Pagamenti Silenziosi, i label sono interi utilizzati per modificare l'indirizzo statico iniziale al fine di creare molti altri indirizzi statici. L'uso di questi label permette la segregazione dei pagamenti inviati tramite Pagamenti Silenziosi, impiegando diversi indirizzi statici per ogni uso, senza aumentare eccessivamente l'onere operativo per rilevare questi pagamenti (scanning). Bob utilizza un indirizzo statico $B$, composto da due chiavi pubbliche: $B_{\text{scan}}$ per lo scanning e $B_{\text{spend}}$ per spendere. L'hash di $b_{\text{scan}}$ e un intero $m$, moltiplicato scalarmente per il punto generatore $G$, è aggiunto alla chiave pubblica di spesa $B_{\text{spend}}$ per creare una sorta di nuova chiave pubblica di spesa $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Per esempio, la prima chiave $B_1$ è ottenuta in questo modo:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

L'indirizzo statico pubblicato da Bob sarà ora composto da $B_{\text{scan}}$ e $B_m$. Per esempio, il primo indirizzo statico con il label $1$ sarà:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Si parte solo dal label $1$, perché il label $0$ è riservato per il resto. Alice, che desidera inviare bitcoin all'indirizzo statico etichettato fornito da Bob, deriverà l'indirizzo di pagamento unico $P_0$ utilizzando il nuovo $B_1$ invece di $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

In realtà, Alice potrebbe non sapere nemmeno che Bob ha un indirizzo etichettato, poiché semplicemente utilizza la seconda parte dell'indirizzo statico che lui ha fornito, che in questo caso è il valore $B_1$ piuttosto che $B_{\text{spend}}$. Per scansionare i pagamenti, Bob utilizzerà sempre il valore del suo indirizzo statico iniziale con $B_{\text{spend}}$ in questo modo:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Poi, semplicemente sottrarrà il valore che trova per $P_0$ da ogni output uno per uno. Poi controlla se uno dei risultati di queste sottrazioni corrisponde al valore di uno dei label che usa nel suo portafoglio. Se corrisponde, per esempio, per l'output #4 con il label $1$, ciò significa che questo output è un Pagamento Silenzioso associato al suo indirizzo statico etichettato $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Questo funziona perché:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Grazie a questo metodo, Bob può utilizzare una moltitudine di indirizzi statici (con $B_1$, $B_2$, $B_3$...), tutti derivati dal suo indirizzo statico base ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), al fine di separare correttamente gli usi.

Tuttavia, questa separazione degli indirizzi statici è valida solo da una prospettiva di gestione personale del portafoglio, ma non consente la separazione delle identità. Poiché tutti hanno lo stesso $B_{\text{scan}}$, è molto facile associare tutti gli indirizzi statici insieme e dedurre che appartengono a un'unica entità.