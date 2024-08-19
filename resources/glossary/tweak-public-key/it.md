---
termine: TWEAK (CHIAVE PUBBLICA)
---

Nel campo della crittografia, "tweaking" una chiave pubblica implica la modifica di questa chiave utilizzando un valore additivo chiamato "tweak" in modo che rimanga utilizzabile con la conoscenza della chiave privata originale e del tweak. Tecnicamente, un tweak è un valore scalare che viene aggiunto alla chiave pubblica iniziale. Se $P$ è la chiave pubblica e $t$ è il tweak, la chiave pubblica modificata diventa:

$$
P' = P + tG
$$

Dove $G$ è il generatore della curva ellittica utilizzata. Questa operazione permette di ottenere una nuova chiave pubblica derivata dalla chiave originale mantenendo certe proprietà crittografiche che la rendono utilizzabile. Ad esempio, questo metodo è utilizzato per gli indirizzi Taproot (P2TR) per consentire la spesa sia presentando una firma Schnorr nel modo tradizionale sia soddisfacendo una delle condizioni enunciate in un albero di Merkle, chiamato anche "MAST".