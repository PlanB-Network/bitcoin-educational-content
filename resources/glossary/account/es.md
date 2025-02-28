---
term: CUENTA

---
En los monederos HD (Hierarchical Deterministic), una cuenta representa una capa de derivación a profundidad 3 según BIP32. Cada cuenta está numerada secuencialmente empezando por `/0'/` (derivación endurecida, así que en realidad `/2^31/` o `/2 147 483 648/`). Es en esta profundidad de derivación donde se encuentran los conocidos `xpubs`. Hoy en día, normalmente sólo se utiliza una cuenta dentro de un monedero HD. Sin embargo, originalmente se concibieron para segregar varias categorías de uso dentro del mismo monedero. Por ejemplo, si tomamos una ruta de derivación estándar para una dirección de recepción externa Taproot (P2TR): `m/86'/0'/0'/0/0`, el índice de la cuenta es el segundo `/0'/`.

![](../../dictionnaire/assets/17.webp)