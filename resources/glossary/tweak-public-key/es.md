---
term: TWEAK (CLAVE PÚBLICA)

---
En el campo de la criptografía, "retocar" una clave pública consiste en modificar esta clave utilizando un valor aditivo denominado "retoque", de modo que siga siendo utilizable con el conocimiento de la clave privada original y del retoque. Técnicamente, un "tweak" es un valor escalar que se añade a la clave pública inicial. Si $P$ es la clave pública y $t$ es el ajuste, la clave pública ajustada será:

$$
P' = P + tG
$$

Donde $G$ es el generador de la curva elíptica utilizada. Esta operación permite obtener una nueva clave pública derivada de la clave original conservando ciertas propiedades criptográficas que la hacen utilizable. Por ejemplo, este método se utiliza en las direcciones Taproot (P2TR) para permitir el gasto, ya sea presentando una firma Schnorr de la forma tradicional o cumpliendo una de las condiciones establecidas en un árbol de Merkle, también llamado "MAST".

![](../../dictionnaire/assets/26.webp)