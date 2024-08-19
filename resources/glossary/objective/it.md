termine: OBJECTIVE

Nelle wallet deterministiche e gerarchiche (HD), l'objective (o _purpose_ in inglese), definito dal BIP43, rappresenta un specifico livello di derivazione. Questo indice, situato al primo livello dell'albero di derivazione (`m / purpose' /`), identifica lo standard di derivazione adottato dal portafoglio, al fine di facilitare la compatibilità tra diversi software di gestione del portafoglio. Ad esempio, nel caso degli indirizzi SegWit (BIP84), l'objective è indicato come `/84'/`. Questo metodo consente un'organizzazione efficiente delle chiavi tra diversi tipi di indirizzi all'interno dello stesso portafoglio HD. Gli indici standard utilizzati sono:
* Per P2PKH: `44'`;
* Per P2WPKH-nested-in-P2SH: `49'`;
* Per P2WPKH: `84'`;
* Per P2TR: `86'`.

![](../../dictionnaire/assets/20.png)