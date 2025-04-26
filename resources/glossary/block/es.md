---
term: BLOQUE

---
Estructura de datos en el sistema Bitcoin. Un bloque contiene un conjunto de transacciones válidas y metadatos contenidos en su cabecera. Cada bloque está vinculado al siguiente por el hash de su cabecera, formando así la cadena de bloques. El blockchain actúa como un servidor de sellado de tiempo que permite a cada usuario conocer todas las transacciones pasadas, con el fin de verificar la no existencia de una transacción y evitar el doble gasto. Las transacciones se organizan en un árbol de Merkle. Este acumulador criptográfico permite obtener un compendio de todas las transacciones de un bloque, llamado "raíz de Merkle" La cabecera de un bloque contiene 6 elementos:


- La versión del bloque;
- La huella del bloque anterior;
- La raíz del árbol de Merkle de las transacciones;
- La marca de tiempo del bloque;
- El objetivo de dificultad;
- El nonce.

Para que un bloque sea válido, debe tener una cabecera que, una vez hasheada con `SHA256d`, produzca un compendio menor o igual que el objetivo de dificultad.