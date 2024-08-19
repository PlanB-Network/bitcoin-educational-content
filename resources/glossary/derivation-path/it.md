---
termine: DERIVATION PATH
---

Nel contesto dei portafogli gerarchici deterministici (HD), un "derivation path" si riferisce alla sequenza di indici utilizzati per derivare chiavi figlie da una chiave madre. Descritto nel BIP32, questo percorso identifica la struttura ad albero per la derivazione delle chiavi figlie. Un "derivation path" è rappresentato da una serie di indici separati da barre e inizia sempre con la chiave madre (indicata come `m/`). Ad esempio, un percorso tipico potrebbe essere `m/84'/0'/0'/0/0`. Ogni livello di derivazione è associato a una specifica profondità:
* `m /` indica la chiave privata madre. È unica per un portafoglio e non può avere fratelli alla stessa profondità. La chiave madre è derivata direttamente dal seed;
* `m / purpose' /` indica lo scopo della derivazione che aiuta a identificare lo standard seguito. Questo campo è descritto nel BIP43. Ad esempio, se il portafoglio aderisce allo standard BIP84 (SegWit V0), l'indice sarebbe quindi `84'`;
* `m / purpose' / coin-type' /` indica il tipo di criptovaluta. Questo permette una chiara differenziazione tra i rami dedicati a una criptovaluta e quelli dedicati a un'altra in un portafoglio multi-coin. L'indice dedicato a Bitcoin è `0'`;
* `m / purpose' / coin-type' / account' /` indica il numero dell'account. Questa profondità facilita la differenziazione e l'organizzazione di un portafoglio in diversi account. Questi account sono numerati a partire da `0'`. Le chiavi estese (`xpub`, `xprv`...) si trovano a questo livello di profondità;
* `m / purpose' / coin-type' / account' / change /` indica il percorso. Ogni account definito alla profondità 3 ha due percorsi alla profondità 4: una catena esterna e una catena interna (chiamata anche "change"). La catena esterna deriva indirizzi destinati ad essere condivisi pubblicamente, ovvero gli indirizzi che ci vengono offerti quando clicchiamo su "ricevi" nel nostro software di portafoglio. La catena interna deriva indirizzi non destinati allo scambio pubblico, principalmente indirizzi di resto. La catena esterna è identificata con l'indice `0` e la catena interna è identificata con l'indice `1`. Si noterà che da questa profondità, non si esegue più una derivazione rinforzata, ma una derivazione normale (non c'è apostrofo). È grazie a questo meccanismo che siamo in grado di derivare tutte le chiavi pubbliche figlie dal loro `xpub`;

* `m / purpose' / coin-type' / account' / change / address-index` indica semplicemente il numero dell'indirizzo ricevente e la sua coppia di chiavi, per differenziarlo dai suoi fratelli alla stessa profondità sullo stesso ramo. Ad esempio, il primo indirizzo derivato ha l'indice `0`, il secondo indirizzo ha l'indice `1`, e così via...

Ad esempio, se il mio indirizzo ricevente ha il percorso di derivazione `m / 86' / 0' / 0' / 0 / 5`, possiamo dedurre le seguenti informazioni:
* `86'` indica che stiamo seguendo lo standard di derivazione del BIP86 (Taproot / SegWit V1);
* `0'` indica che si tratta di un indirizzo Bitcoin;
* `0'` indica che ci troviamo sul primo account del portafoglio;
* `0` indica che si tratta di un indirizzo esterno;
* `5` indica che è il sesto indirizzo esterno di questo account.