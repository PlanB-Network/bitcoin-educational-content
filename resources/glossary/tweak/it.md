---
term: TWEAK
---

In crittografia, "tweakare" una chiave pubblica significa modificarla utilizzando un valore additivo chiamato "tweak", in modo che rimanga utilizzabile con la conoscenza sia della chiave privata originale sia del tweak. Tecnicamente, un tweak è un valore scalare che viene aggiunto alla chiave pubblica originale. Se $P$ è la chiave pubblica e $t$ è il tweak, la chiave pubblica modificata diventa :


$$
P' = P + tG
$$


Dove $G$ è il generatore della curva ellittica utilizzata. Questa operazione produce una nuova chiave pubblica derivata dall'originale, pur mantenendo alcune proprietà crittografiche che ne consentono l'utilizzo. Ad esempio, questo metodo viene utilizzato per gli indirizzi Taproot (P2TR), per consentire la spendibilità sia presentando una firma Schnorr nel modo tradizionale, sia soddisfacendo una delle condizioni stabilite in un Merkle Tree, noto anche come "MAST".