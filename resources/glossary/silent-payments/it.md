---
term: PAGAMENTI SILENZIOSI

---
Metodo per l'utilizzo di indirizzi Bitcoin statici per ricevere pagamenti senza riutilizzo di indirizzi, senza interazione e senza un collegamento visibile sulla catena tra i diversi pagamenti e l'indirizzo statico. Questa tecnica elimina la necessità di generare nuovi indirizzi di ricezione inutilizzati per ogni transazione, evitando così le consuete interazioni in Bitcoin in cui il destinatario deve fornire un nuovo indirizzo al pagatore.

Con Silent Payments, il pagatore utilizza le chiavi pubbliche del destinatario (chiave pubblica di spesa e chiave pubblica di scansione) e la somma delle proprie chiavi private come input per generare un nuovo indirizzo per ogni pagamento. Solo il destinatario, con le proprie chiavi private, può calcolare la chiave privata corrispondente a questo indirizzo di pagamento. L'ECDH (*Elliptic-Curve Diffie-Hellman*), un algoritmo di scambio di chiavi crittografiche, viene utilizzato per stabilire un segreto condiviso che viene poi utilizzato per ricavare l'indirizzo di ricezione e la chiave privata (solo dal lato del destinatario). Per identificare i Silent Payments a loro destinati, i destinatari devono scansionare la blockchain ed esaminare ogni transazione che corrisponde ai criteri del protocollo. A differenza del BIP47, che utilizza una transazione di notifica per stabilire il canale di pagamento, i Silent Payments eliminano questo passaggio, risparmiando una transazione. Tuttavia, il compromesso è che il destinatario deve scansionare tutte le potenziali transazioni per determinare, applicando l'ECDH, se sono indirizzate a lui.

Ad esempio, l'indirizzo statico di Bob $B$ rappresenta la concatenazione della sua chiave pubblica di scansione e della sua chiave pubblica di spesa:

$$ B = B_{{testo{scan}} \´testo{ ‖ } B_{testo{spesa}} $$

Queste chiavi sono semplicemente derivate dal seguente percorso:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Questo indirizzo statico viene pubblicato da Bob. Alice lo recupera per effettuare un pagamento silenzioso a Bob. Calcola l'indirizzo di pagamento di Bob $P_0$ in questo modo:

$$ P_0 = B_{{testo{spesa}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{{text{scan}} \text{ ‖ } 0) \cdot G $$

Dove:

$$ ´testo{inputHash} = ´testo{hash}(´testo{outpoint}_L ´testo{ ‖ } A) $$

Con:


- $B_{\text{scan}}$: chiave pubblica di scansione di Bob (indirizzo statico);
- $B_{{testo{spesa}}$: chiave pubblica di spesa di Bob (indirizzo statico);
- $A$: La somma delle chiavi pubbliche in ingresso (tweak);
- $a$: La chiave privata del tweak, cioè la somma di tutte le coppie di chiavi utilizzate nella `scriptPubKey` degli UTXO consumati come input nella transazione di Alice;
- $testo{outpoint}_L$: L'UTXO più piccolo (in senso lessicografico) utilizzato come ingresso nella transazione di Alice;
- $testo{ ‖ }$: Concatenazione (l'operazione di unione degli operandi da un capo all'altro);
- $G$: Il punto generatore della curva ellittica `secp256k1`;
- $testo{hash}$: La funzione hash SHA256 contrassegnata da `BIP0352/SharedSecret`;
- $P_0$: La prima chiave pubblica/indirizzo unico per il pagamento a Bob;
- $0$: Un numero intero utilizzato per generare più indirizzi di pagamento univoci.

Bob scansiona la blockchain per trovare il suo Silent Payment in questo modo:

$$ P_0 = B_{{testo{spesa}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Con:


- $b_{\text{scan}}$: la chiave di scansione privata di Bob.

Se trova $P_0$ come indirizzo contenente un Silent Payment indirizzato a lui, calcola $p_0$, la chiave privata che gli permette di spendere i fondi inviati da Alice a $P_0$:

$$ p_0 = (b_{{testo{spesa}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Con:


- $b_{\text{spend}}$: la chiave di spesa privata di Bob;
- $n$: l'ordine della curva ellittica `secp256k1`.

Oltre a questa versione di base, le etichette possono essere utilizzate per generare diversi indirizzi statici dallo stesso indirizzo statico di base, con l'obiettivo di separare gli usi multipli senza moltiplicare eccessivamente il lavoro richiesto durante la scansione.