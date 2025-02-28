---
term: BIP44

---
Una proposta di miglioramento che introduce una struttura di derivazione gerarchica standard per i portafogli HD. Il BIP44 si basa sui principi stabiliti dal BIP32 per la derivazione delle chiavi e sul BIP43 per l'uso del campo "purpose". Introduce una struttura di derivazione a cinque livelli: `m / purpose' / coin_type' / account' / change / address_index'. Ecco i dettagli di ogni livello:


- `m /` indica la chiave privata principale. È unica per un portafoglio e non può avere fratelli alla stessa profondità. La chiave master deriva direttamente dal seme del portafoglio;
- `m / purpose' /` indica lo scopo della derivazione che aiuta a identificare lo standard seguito. Questo campo è descritto in BIP43. Ad esempio, se il portafoglio segue lo standard BIP84 (SegWit V0), l'indice sarà `84'`;
- `m / purpose' / coin-type' /` indica il tipo di criptovaluta. Ciò consente di differenziare chiaramente i rami dedicati a una criptovaluta da quelli dedicati a un'altra criptovaluta in un portafoglio multi-moneta. L'indice dedicato a Bitcoin è `0'`;
- `m / purpose' / coin-type' / account' /` indica il numero di conto. Questa profondità consente di differenziare e organizzare facilmente un portafoglio in diversi conti. Questi conti sono numerati a partire da `0'`. Le chiavi estese (`xpub`, `xprv`...) si trovano a questa profondità;
- `m / purpose' / coin-type' / account' / change /` indica la catena. Ogni conto, come definito alla profondità 3, ha due catene alla profondità 4: una catena esterna e una catena interna (chiamata anche "cambio"). La catena esterna deriva gli indirizzi destinati a essere comunicati pubblicamente, cioè gli indirizzi che ci vengono offerti quando clicchiamo su "ricevi" nel nostro software di portafoglio. La catena interna deriva gli indirizzi non destinati a essere scambiati pubblicamente, cioè principalmente gli indirizzi di cambio. La catena esterna è identificata con l'indice `0` e quella interna con l'indice `1`. Si noterà che a partire da questa profondità non si esegue più una derivazione protetta, ma una derivazione normale (non c'è l'apostrofo). È grazie a questo meccanismo che siamo in grado di derivare tutte le chiavi pubbliche figlie dalla loro `xpub`;
- `m / purpose' / coin-type' / account' / change / address-index' indica semplicemente il numero dell'indirizzo ricevente e la sua coppia di chiavi, per differenziarlo dai suoi fratelli alla stessa profondità sullo stesso ramo. Ad esempio, il primo indirizzo derivato ha l'indice `0`, il secondo indirizzo ha l'indice `1`, e così via...

Per esempio, se il mio indirizzo di ricezione ha il percorso di derivazione `m / 86' / 0' / 0' / 0 / 5', possiamo dedurre le seguenti informazioni:


- `86'` indica che stiamo seguendo lo standard di derivazione di BIP86 (Taproot o SegWitV1);
- `0'` indica che si tratta di un indirizzo Bitcoin;
- `0'` indica che siamo al primo conto del portafoglio;
- `0` indica che si tratta di un indirizzo esterno;
- `5` indica che si tratta del sesto indirizzo esterno di questo conto.

![](../../dictionnaire/assets/18.webp)