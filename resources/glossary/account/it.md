---
term: CONTO

---
Nei portafogli HD (Hierarchical Deterministic), un conto rappresenta un livello di derivazione a profondità 3 secondo BIP32. Ogni conto è numerato in modo sequenziale, a partire da `/0'/` (derivazione indurita, quindi in realtà `/2^31/` o `/2 147 483 648/`). È a questa profondità di derivazione che si trovano i noti `xpub'. Al giorno d'oggi, in genere viene utilizzato un solo conto all'interno di un portafoglio HD. Tuttavia, in origine erano stati concepiti per segregare diverse categorie di utilizzo all'interno dello stesso portafoglio. Ad esempio, se prendiamo un percorso di derivazione standard per un indirizzo di ricezione Taproot esterno (P2TR): `m/86'/0'/0'/0/0`, l'indice del conto è il secondo `/0'/`.

![](../../dictionnaire/assets/17.webp)