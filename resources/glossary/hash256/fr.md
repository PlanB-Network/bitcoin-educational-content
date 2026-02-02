---
term: HASH256
definition: Fonction appliquant deux fois SHA256 successivement, utilisée dans diverses applications Bitcoin.
---

Fonction cryptographique utilisée pour diverses applications sur Bitcoin. Elle consiste en l'application double de la fonction SHA256 sur les données en entrée. Le message est passé une première fois dans SHA256, et le résultat de cette opération est utilisé comme entrée pour passer une seconde fois dans SHA256. La sortie de cette fonction est donc de 256 bits.
$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$
