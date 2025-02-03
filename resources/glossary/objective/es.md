---
term: OBJETIVO

---
En los monederos deterministas y jerárquicos (HD), el objetivo (o _purpose_ en inglés), definido por BIP43, representa un nivel específico de derivación. Este índice, situado en la primera profundidad del árbol de derivación (`m / purpose' /`), identifica la norma de derivación adoptada por el monedero, con el fin de facilitar la compatibilidad entre los distintos programas de gestión de monederos. Por ejemplo, en el caso de las direcciones SegWit (BIP84), el objetivo se anota como `/84'/`. Este método permite organizar eficazmente las claves entre distintos tipos de direcciones dentro de un mismo monedero HD. Los índices estándar utilizados son:


- Para P2PKH: `44'`;
- Para P2WPKH anidado en P2SH: `49'`;
- Para P2WPKH: `84'`;
- Para P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)