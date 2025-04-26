---
term: PERCORSO DI DERIVAZIONE

---
Nel contesto dei portafogli deterministici gerarchici (HD), un percorso di derivazione si riferisce alla sequenza di indici utilizzati per derivare le chiavi figlio da una chiave master. Descritto nel BIP32, questo percorso identifica la struttura ad albero per la derivazione delle chiavi figlio. Un percorso di derivazione è rappresentato da una serie di indici separati da barre e inizia sempre con la chiave master (indicata come `m/`). Ad esempio, un percorso tipico potrebbe essere `m/84'/0'/0'/0/0`. Ogni livello di derivazione è associato a una profondità specifica:


- `m /` indica la chiave privata principale. È unica per un portafoglio e non può avere fratelli alla stessa profondità. La chiave master è derivata direttamente dal seme;
- `m / purpose' /` indica lo scopo della derivazione che aiuta a identificare lo standard seguito. Questo campo è descritto nel BIP43. Ad esempio, se il portafoglio aderisce allo standard BIP84 (SegWit V0), l'indice sarebbe `84'`;
- `m / purpose' / coin-type' /` indica il tipo di criptovaluta. Questo permette di differenziare chiaramente i rami dedicati a una criptovaluta da quelli dedicati a un'altra in un portafoglio multi-moneta. L'indice dedicato a Bitcoin è `0'`;
- `m / purpose' / coin-type' / account' /` indica il numero di conto. Questa profondità consente di differenziare e organizzare facilmente un portafoglio in diversi conti. Questi conti sono numerati a partire da `0'`. Le chiavi estese (`xpub`, `xprv`...) si trovano a questo livello di profondità;
- `m / purpose' / coin-type' / account' / change /` indica il percorso. Ogni conto definito alla profondità 3 ha due percorsi alla profondità 4: una catena esterna e una catena interna (chiamata anche "cambio"). La catena esterna deriva gli indirizzi destinati a essere condivisi pubblicamente, cioè gli indirizzi che ci vengono offerti quando clicchiamo su "ricevi" nel nostro software di portafoglio. La catena interna deriva gli indirizzi non destinati a essere scambiati pubblicamente, principalmente gli indirizzi di cambio. La catena esterna è identificata con l'indice `0` e quella interna con l'indice `1`. Si noterà che a partire da questa profondità non si esegue più una derivazione protetta, ma una derivazione normale (non c'è l'apostrofo). È grazie a questo meccanismo che siamo in grado di derivare tutte le chiavi pubbliche figlie dalla loro `xpub`;
- `m / purpose' / coin-type' / account' / change / address-index' indica semplicemente il numero dell'indirizzo ricevente e la sua coppia di chiavi, per differenziarlo dai suoi fratelli alla stessa profondità sullo stesso ramo. Ad esempio, il primo indirizzo derivato ha l'indice `0`, il secondo indirizzo ha l'indice `1`, e così via...

Ad esempio, se il mio indirizzo di ricezione ha il percorso di derivazione `m / 86' / 0' / 0' / 0 / 5', possiamo dedurre le seguenti informazioni:


- `86'` indica che stiamo seguendo lo standard di derivazione di BIP86 (Taproot / SegWit V1);
- `0'` indica che si tratta di un indirizzo Bitcoin;
- `0'` indica che siamo al primo conto del portafoglio;
- `0` indica che si tratta di un indirizzo esterno;
- `5` indica che si tratta del sesto indirizzo esterno di questo conto.

![](../../dictionnaire/assets/18.webp)