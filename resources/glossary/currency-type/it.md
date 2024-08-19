---
term: TIPO DI VALUTA
---

Nel contesto dei portafogli deterministici e gerarchici (HD), il tipo di valuta (*coin type* in inglese) rappresenta un livello di derivazione che permette di differenziare i rami del portafoglio basandosi sulle varie criptovalute utilizzate. Questo strato di derivazione, definito dal BIP 44, si trova al livello 2 della struttura di derivazione, seguendo la chiave principale e lo scopo. Ad esempio, per Bitcoin, l'indice assegnato è `0x80000000`, indicato come `/0'/` nel percorso di derivazione. Ciò significa che tutti gli indirizzi e i conti derivati da questo percorso sono associati a Bitcoin. Questo strato di derivazione consente una chiara separazione dei diversi asset in un portafoglio multi-valuta. Ecco gli indici utilizzati per varie criptovalute:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)