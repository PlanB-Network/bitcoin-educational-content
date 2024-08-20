---
term: BLOCK
---

Estructura de datos en el sistema de Bitcoin. Un bloque contiene un conjunto de transacciones válidas y metadatos contenidos en su encabezado. Cada bloque está vinculado al siguiente por el hash de su encabezado, formando así la cadena de bloques. La cadena de bloques actúa como un servidor de sellado de tiempo que permite a cada usuario conocer todas las transacciones pasadas, con el fin de verificar la no existencia de una transacción y prevenir el doble gasto. Las transacciones están organizadas en un árbol de Merkle. Este acumulador criptográfico permite la producción de un resumen de todas las transacciones en un bloque, llamado "raíz de Merkle". El encabezado de un bloque contiene 6 elementos:
* La versión del bloque;
* La huella del bloque anterior;
* La raíz del árbol de Merkle de transacciones;
* La marca de tiempo del bloque;
* El objetivo de dificultad;
* El nonce.

Para que un bloque sea válido, debe tener un encabezado que, una vez hasheado con `SHA256d`, produzca un resumen que sea menor o igual al objetivo de dificultad.