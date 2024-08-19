termine: ACCOUNT

Nelle wallet HD (Hierarchical Deterministic), un account rappresenta un livello di derivazione alla profondità 3 secondo BIP32. Ogni account è numerato sequenzialmente a partire da `/0'/` (derivazione rinforzata, quindi in realtà `/2^31/` o `/2 147 483 648/`). È a questa profondità di derivazione che si trovano i ben noti `xpubs`. Oggi, tipicamente viene utilizzato un solo account all'interno di una wallet HD. Tuttavia, in origine, erano concepiti per segregare varie categorie di utilizzo all'interno dello stesso portafoglio. Ad esempio, se prendiamo un percorso di derivazione standard per un indirizzo di ricezione esterno Taproot (P2TR): `m/86'/0'/0'/0/0`, l'indice dell'account è il secondo `/0'/`.

![](../../dictionnaire/assets/17.png)