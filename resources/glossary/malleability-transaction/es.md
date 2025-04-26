---
term: MALEABILIDAD (TRANSACCIÓN)

---
Se refiere a la capacidad de modificar ligeramente la estructura de una transacción Bitcoin, sin alterar su efecto, pero cambiando el identificador de la transacción (*TXID*). Esta propiedad puede ser explotada maliciosamente para engañar a los interesados sobre el estado de una transacción, causando así problemas como el doble gasto. La maleabilidad era posible gracias a la flexibilidad de la firma digital utilizada. La bifurcación suave SegWit se introdujo especialmente para evitar esta maleabilidad de las transacciones de Bitcoin, complicando la implementación de la Lightning Network. Lo consigue eliminando los datos maleables de la transacción del cálculo del TXID.

> ► *Aunque es poco frecuente, a veces se utiliza el término "mutabilidad" para referirse al mismo concepto.*