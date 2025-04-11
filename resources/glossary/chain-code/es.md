---
term: CÓDIGO CADENA

---
En el contexto de la derivación jerárquica determinista (HD) de los monederos Bitcoin, el código de cadena es un valor de sal criptográfica de 256 bits utilizado para generar claves hijas a partir de una clave padre, según el estándar BIP32. El código de cadena se utiliza en combinación con la clave padre y el índice del hijo para generar de forma determinista un nuevo par de claves (clave privada y clave pública) sin revelar la clave padre u otras claves hijo derivadas.

Por lo tanto, existe un código de cadena único para cada par de claves. El código de cadena se obtiene haciendo un hash de la semilla del monedero y tomando la mitad derecha de los bits. En este caso, se denomina código de cadena maestro, asociado a la clave privada maestra. También puede obtenerse haciendo un hash de una clave padre con su código de cadena padre y un índice, y quedándose con los bits de la derecha. En este caso, se denomina código de cadena hijo.

Es imposible derivar claves sin conocer el código de cadena asociado a cada par parental. Introduce datos pseudoaleatorios en el proceso de derivación para garantizar que la generación de claves criptográficas siga siendo impredecible para los atacantes a la vez que determinista para el titular del monedero.

> ► *En inglés, un "code de chaîne" se denomina "chain code", y un "code de chaîne maître", "master chain code "*