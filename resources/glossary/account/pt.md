---
termo: CONTA
---

Em carteiras HD (Hierárquicas Determinísticas), uma conta representa uma camada de derivação no nível 3 de acordo com o BIP32. Cada conta é numerada sequencialmente a partir de `/0'/` (derivação endurecida, então na realidade `/2^31/` ou `/2 147 483 648/`). É nesta profundidade de derivação que os conhecidos `xpubs` estão localizados. Atualmente, tipicamente apenas uma conta é usada dentro de uma carteira HD. No entanto, originalmente, elas foram concebidas para segregar várias categorias de uso dentro da mesma carteira. Por exemplo, se tomarmos um caminho de derivação padrão para um endereço de recepção Taproot externo (P2TR): `m/86'/0'/0'/0/0`, o índice da conta é o segundo `/0'/`.

![](../../dictionnaire/assets/17.png)