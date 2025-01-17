---
term: TWEAK (CHIAVE PUBBLICA)

---
Nel campo della crittografia, il "tweaking" di una chiave pubblica consiste nel modificare questa chiave utilizzando un valore additivo chiamato "tweak" in modo che rimanga utilizzabile con la conoscenza della chiave privata originale e del tweak. Tecnicamente, un tweak è un valore scalare che viene aggiunto alla chiave pubblica iniziale. Se $P$ è la chiave pubblica e $t$ è il tweak, la chiave pubblica modificata diventa:

$$
P' = P + tG
$$

Dove $G$ è il generatore della curva ellittica utilizzata. Questa operazione consente di ottenere una nuova chiave pubblica derivata dalla chiave originale, mantenendo alcune proprietà crittografiche che la rendono utilizzabile. Ad esempio, questo metodo viene utilizzato per gli indirizzi Taproot (P2TR) per consentire la spesa sia presentando una firma Schnorr in modo tradizionale, sia soddisfacendo una delle condizioni indicate in un albero di Merkle, detto anche "MAST".

![](../../dictionnaire/assets/26.webp)