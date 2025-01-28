---
term: TIPO DI VALUTA

---
Nel contesto dei portafogli deterministici e gerarchici (HD), il tipo di valuta (*coin type* in inglese) è un livello di derivazione che consente di differenziare i rami del portafoglio in base alle varie criptovalute utilizzate. Questo livello di derivazione, definito dal BIP 44, si trova alla profondità 2 della struttura di derivazione, dopo la chiave master e lo scopo. Ad esempio, per il Bitcoin, l'indice assegnato è `0x80000000`, indicato come `/0'/` nel percorso di derivazione. Ciò significa che tutti gli indirizzi e i conti derivati da questo percorso sono associati a Bitcoin. Questo livello di derivazione consente una chiara separazione delle diverse attività in un portafoglio multivaluta. Ecco gli indici utilizzati per le varie criptovalute:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)