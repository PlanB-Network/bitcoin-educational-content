---
term: CONTA

---
Nas carteiras HD (Hierarchical Deterministic), uma conta representa uma camada de derivação na profundidade 3 de acordo com o BIP32. Cada conta é numerada sequencialmente a partir de `/0'/` (derivação reforçada, portanto, na realidade `/2^31/` ou `/2 147 483 648/`). É nesta profundidade de derivação que se encontram os conhecidos `xpubs`. Hoje em dia, tipicamente, apenas uma conta é usada numa carteira HD. No entanto, originalmente, elas foram concebidas para separar várias categorias de uso dentro da mesma carteira. Por exemplo, se tomarmos um caminho de derivação padrão para um endereço de receção Taproot externo (P2TR): `m/86'/0'/0'/0/0`, o índice da conta é o segundo `/0'/`.

![](../../dictionnaire/assets/17.webp)