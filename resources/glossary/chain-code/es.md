---
term: CHAIN CODE
---

En el contexto de la derivación determinista jerárquica (HD) de carteras de Bitcoin, el chain code es un valor de sal criptográfico de 256 bits utilizado para generar claves hijas a partir de una clave padre, de acuerdo con el estándar BIP32. El chain code se utiliza en combinación con la clave padre y el índice del hijo para generar de manera determinista un nuevo par de claves (clave privada y clave pública) sin revelar la clave padre u otras claves hijas derivadas.

Por lo tanto, hay un chain code único para cada par de claves. El chain code se obtiene ya sea hasheando la semilla de la cartera y tomando la mitad derecha de los bits. En este caso, se le denomina como un master chain code, asociado con la clave privada maestra. Alternativamente, se puede obtener hasheando una clave padre con su chain code padre y un índice, luego manteniendo los bits derechos. Esto se denomina entonces como un child chain code.

Es imposible derivar claves sin conocer el chain code asociado con cada par padre. Introduce datos pseudoaleatorios en el proceso de derivación para asegurar que la generación de claves criptográficas permanezca impredecible para los atacantes mientras sea determinista para el poseedor de la cartera.

> ► *En inglés, un "code de chaîne" se llama "chain code", y un "code de chaîne maître" se llama "master chain code".*