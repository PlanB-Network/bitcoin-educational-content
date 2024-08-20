---
term: CUENTA
---

En las billeteras HD (Deterministas Jerárquicas), una cuenta representa una capa de derivación en la profundidad 3 según BIP32. Cada cuenta está numerada secuencialmente comenzando desde `/0'/` (derivación endurecida, así que en realidad `/2^31/` o `/2 147 483 648/`). Es en esta profundidad de derivación donde se ubican los conocidos `xpubs`. Hoy en día, típicamente solo se utiliza una cuenta dentro de una billetera HD. Sin embargo, originalmente, fueron concebidas para segregar varias categorías de uso dentro de la misma billetera. Por ejemplo, si tomamos un camino de derivación estándar para una dirección de recepción externa Taproot (P2TR): `m/86'/0'/0'/0/0`, el índice de la cuenta es el segundo `/0'/`.

![](../../dictionnaire/assets/17.png)