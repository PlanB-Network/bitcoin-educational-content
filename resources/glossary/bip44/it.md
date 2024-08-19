---
term: BIP44
---

Una proposta di miglioramento che introduce una struttura di derivazione gerarchica standard per i portafogli HD. BIP44 si basa sui principi stabiliti da BIP32 per la derivazione delle chiavi e su BIP43 per l'uso del campo "purpose" (scopo). Introduce una struttura di derivazione a cinque livelli: `m / purpose' / coin_type' / account' / change / address_index`. Ecco i dettagli di ogni livello:
* `m /` indica la chiave privata master. È unica per un portafoglio e non può avere "fratelli" allo stesso livello. La chiave master è derivata direttamente dal seed del portafoglio;
* `m / purpose' /` indica lo scopo della derivazione che aiuta a identificare lo standard seguito. Questo campo è descritto in BIP43. Ad esempio, se il portafoglio segue lo standard BIP84 (SegWit V0), l'indice sarebbe quindi `84'`;
* `m / purpose' / coin-type' /` indica il tipo di criptovaluta. Questo permette una chiara differenziazione tra i rami dedicati a una criptovaluta e quelli dedicati a un'altra criptovaluta in un portafoglio multi-coin. L'indice dedicato a Bitcoin è `0'`;
* `m / purpose' / coin-type' / account' /` indica il numero dell'account. Questo livello permette una facile differenziazione e organizzazione di un portafoglio in diversi account. Questi account sono numerati a partire da `0'`. Le chiavi estese (`xpub`, `xprv`...) si trovano a questo livello;
* `m / purpose' / coin-type' / account' / change /` indica la catena. Ogni account definito nel livello 3 ha due catene al livello 4: una catena esterna e una catena interna (chiamata anche “change”). La catena esterna deriva indirizzi destinati a essere comunicati pubblicamente, ovvero gli indirizzi che ci vengono offerti quando clicchiamo su “ricevi” nel nostro software di portafoglio. La catena interna deriva indirizzi non destinati allo scambio pubblico, ovvero principalmente indirizzi di resto. La catena esterna è identificata con l'indice `0` e la catena interna è identificata con l'indice `1`. Noterai che da questo livello, non eseguiamo più una derivazione rinforzata, ma una derivazione normale (non c'è apostrofo). È grazie a questo meccanismo che siamo capaci di derivare tutte le chiavi pubbliche figlie dal loro `xpub`;
* `m / purpose' / coin-type' / account' / change / address-index` indica semplicemente il numero dell'indirizzo ricevente e la sua coppia di chiavi, per differenziarlo dai suoi "fratelli" allo stesso livello sullo stesso ramo. Ad esempio, il primo indirizzo derivato ha l'indice `0`, il secondo indirizzo ha l'indice `1`, e così via...
Per esempio, se il mio indirizzo ricevente ha il percorso di derivazione `m / 86' / 0' / 0' / 0 / 5`, possiamo dedurre le seguenti informazioni:
* `86'` indica che stiamo seguendo lo standard di derivazione di BIP86 (Taproot o SegWitV1);
* `0'` indica che si tratta di un indirizzo Bitcoin;
* `0'` indica che ci troviamo sul primo account del portafoglio;
* `0` indica che si tratta di un indirizzo esterno;
* `5` indica che è il sesto indirizzo esterno di questo account.