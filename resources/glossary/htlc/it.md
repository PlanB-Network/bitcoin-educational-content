---
term: HTLC
---

Sta per "*Hashed Timelock Contract*". È un meccanismo Smart contract utilizzato principalmente su Lightning. A volte si trova anche negli scambi atomici. In pratica, il HTLC condiziona un trasferimento di denaro alla rivelazione di un segreto e include anche una condizione temporale per proteggere il denaro del mittente in caso di transazione fallita.


Su Lightning, HTLC permette di inviare bitcoin a un nodo con cui non si ha un canale diretto, passando attraverso diversi canali, senza bisogno di fiducia lungo il percorso. Il pagamento tra ciascun nodo è subordinato alla fornitura di una pre-immagine (il segreto che, sottoposto a hash, corrisponde a un valore concordato). Se il destinatario finale fornisce questa pre-immagine, può rivendicare i fondi, e necessariamente permette a ogni nodo intermedio di rivendicare i fondi a cascata.


Ad esempio, se Alice vuole inviare 1 BTC a David, ma non ha un canale diretto con lui, deve passare attraverso Bob e Carol, che hanno canali di pagamento reciproci. Ecco come funziona la transazione:




- David presenta ad Alice un Invoice Lightning. Questo contiene il Hash $h$ di un $s$ segreto (la pre-immagine) che solo David conosce. Quindi abbiamo: $h = \text{Hash}(s)$ ;
- Alice crea un HTLC con Bob, che si offre di inviarle 1 BTC a condizione che Bob le fornisca un segreto $s$ (la pre-immagine) che corrisponde al Hash $h$ ;
- Bob crea un HTLC con Carol, che si offre di inviargli 1 BTC a condizione di fornire lo stesso segreto $s$ ;
- Carol crea un HTLC con David, che offre un altro 1 BTC se rivela la preimmagine $s$;
- David rivela $s$ (che solo lui conosceva) a Carol per ricevere 1 BTC. Carol può ora usare $s$ per ottenere i BTC da Bob. E Bob, che ora conosce $s$, fa lo stesso con Alice.


Infine, Alice ha inviato 1 BTC a David tramite Bob e Carol (un'azione neutrale per quest'ultima), senza che nessuno debba fidarsi l'uno dell'altro, poiché tutto è garantito a cascata dalle condizioni degli HTLC.


Le HTLC consentono quindi i cosiddetti scambi "atomici": o il trasferimento va completamente a buon fine, o fallisce, e i fondi vengono restituiti. Questo garantisce la sicurezza delle transazioni, anche tra più partecipanti senza bisogno di fiducia.