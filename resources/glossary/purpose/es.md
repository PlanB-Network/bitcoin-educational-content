---
term: OBJETIVO
---

En las carteras deterministas y jerárquicas (HD), el propósito, definido por la BIP43, representa un nivel de derivación específico. Este índice, situado en la primera profundidad del árbol de derivación (`m / purpose' /`), identifica la norma de derivación adoptada por la cartera, para facilitar la compatibilidad entre distintos programas informáticos de gestión de carteras. Por ejemplo, en el caso de las direcciones SegWit (BIP84), la finalidad se anota como `/84'/`. Este método permite organizar eficazmente las claves entre distintos tipos de Address dentro de una misma cartera de HD. Los índices estándar utilizados son :




- Para P2PKH: `44'` ;
- Para P2WPKH anidado en P2SH: `49'` ;
- Para P2WPKH: `84'` ;
- Para P2TR: `86'`.