---
term: MALLEABILIDAD (TRANSACCIÓN)
---

Se refiere a la capacidad de modificar ligeramente la estructura de una transacción de Bitcoin, sin alterar su efecto, pero cambiando el identificador de la transacción (*TXID*). Esta propiedad puede ser explotada maliciosamente para engañar a los interesados sobre el estado de una transacción, causando así problemas como el doble gasto. La malleabilidad fue posible debido a la flexibilidad de la firma digital utilizada. El soft fork SegWit fue introducido notablemente para prevenir esta malleabilidad de las transacciones de Bitcoin, complicando la implementación de la Lightning Network. Lo logra eliminando los datos maleables de la transacción del cálculo del TXID.

> ► *Aunque es raro, el término "mutabilidad" a veces se usa para referirse al mismo concepto.*