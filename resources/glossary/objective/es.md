---
term: OBJETIVO
---

En las carteras deterministas y jerárquicas (HD), el objetivo (o _propósito_ en inglés), definido por BIP43, representa un nivel específico de derivación. Este índice, ubicado en la primera profundidad del árbol de derivación (`m / purpose' /`), identifica el estándar de derivación adoptado por la cartera, con el fin de facilitar la compatibilidad entre diferentes software de gestión de carteras. Por ejemplo, en el caso de las direcciones SegWit (BIP84), el objetivo se nota como `/84'/`. Este método permite la organización eficiente de llaves entre diferentes tipos de direcciones dentro de la misma cartera HD. Los índices estándar utilizados son:
* Para P2PKH: `44'`;
* Para P2WPKH anidado en P2SH: `49'`;
* Para P2WPKH: `84'`;
* Para P2TR: `86'`.

![](../../dictionnaire/assets/20.png)