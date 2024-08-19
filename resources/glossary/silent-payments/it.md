---
termine: PAGAMENTI SILENZIOSI
---

Metodo per utilizzare indirizzi Bitcoin statici per ricevere pagamenti senza riutilizzo dell'indirizzo, senza interazione e senza un collegamento visibile sulla blockchain tra i diversi pagamenti e l'indirizzo statico. Questa tecnica elimina la necessità di generare nuovi indirizzi di ricezione inutilizzati per ogni transazione, evitando così le usuali interazioni in Bitcoin dove il destinatario deve fornire un nuovo indirizzo al pagatore.

Con i Pagamenti Silenziosi, il pagatore utilizza le chiavi pubbliche del destinatario (chiave pubblica di spesa e chiave pubblica di scansione) e la somma delle proprie chiavi private come input per generare un nuovo indirizzo per ogni pagamento. Solo il destinatario, con le proprie chiavi private, può calcolare la chiave privata corrispondente a questo indirizzo di pagamento. ECDH (*Elliptic-Curve Diffie-Hellman*), un algoritmo di scambio di chiavi crittografiche, viene utilizzato per stabilire un segreto condiviso che viene poi utilizzato per derivare l'indirizzo di ricezione e la chiave privata (solo dal lato del destinatario). Per identificare i Pagamenti Silenziosi destinati a loro, i destinatari devono scandagliare la blockchain ed esaminare ogni transazione che corrisponde ai criteri del protocollo. A differenza di BIP47, che utilizza una transazione di notifica per stabilire il canale di pagamento, i Pagamenti Silenziosi eliminano questo passaggio, risparmiando una transazione. Tuttavia, il compromesso è che il destinatario deve scandagliare tutte le transazioni potenziali per determinare, applicando ECDH, se sono indirizzate a loro.

Per esempio, l'indirizzo statico di Bob $B$ rappresenta la concatenazione della sua chiave pubblica di scansione e della sua chiave pubblica di spesa:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Queste chiavi sono semplicemente derivate dal seguente percorso:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Questo indirizzo statico è pubblicato da Bob. Alice lo recupera per effettuare un Pagamento Silenzioso a Bob. Lei calcola l'indirizzo di pagamento di Bob $P_0$ in questo modo:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Dove:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Con:
* $B_{\text{scan}}$: La chiave pubblica di scansione di Bob (indirizzo statico);
* $B_{\text{spend}}$: La chiave pubblica di spesa di Bob (indirizzo statico);
* $A$: La somma delle chiavi pubbliche in input (tweak);
* $a$: La chiave privata del tweak, cioè la somma di tutte le coppie di chiavi utilizzate nel `scriptPubKey` degli UTXO consumati come input nella transazione di Alice;
* $\text{outpoint}_L$: L'UTXO più piccolo (lessicograficamente) utilizzato come input nella transazione di Alice;
* $\text{ ‖ }$: Concatenazione (l'operazione di unione degli operandi da capo a fine);
* $G$: Il punto generatore della curva ellittica `secp256k1`;
* $\text{hash}$: La funzione di hash SHA256 etichettata con `BIP0352/SharedSecret`;
* $P_0$: La prima chiave pubblica / indirizzo unico per il pagamento a Bob;
* $0$: Un intero utilizzato per generare più indirizzi di pagamento unici.

Bob scandaglia la blockchain per trovare il suo Pagamento Silenzioso in questo modo:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Con:
* $b_{\text{scan}}$: chiave privata di scansione di Bob.

Se trova $P_0$ come un indirizzo contenente un Pagamento Silenzioso indirizzato a lui, calcola $p_0$, la chiave privata che gli permette di spendere i fondi inviati da Alice a $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Con:
* $b_{\text{spend}}$: chiave privata di spesa di Bob;
* $n$: l'ordine della curva ellittica `secp256k1`.

Oltre a questa versione base, le etichette possono anche essere utilizzate per generare diversi indirizzi statici differenti a partire dallo stesso indirizzo statico base, con l'obiettivo di separare usi multipli senza moltiplicare in modo irragionevole il lavoro richiesto durante la scansione.