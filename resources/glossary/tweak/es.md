---
term: TWEAK
---

En criptografía, "retocar" una clave pública es modificarla utilizando un valor aditivo llamado "retoque", de modo que siga siendo utilizable con el conocimiento tanto de la clave privada original como del retoque. Técnicamente, un "tweak" es un valor escalar que se añade a la clave pública original. Si $P$ es la clave pública y $t$ es la modificación, la clave pública modificada se convierte en :


$$
P' = P + tG
$$


Donde $G$ es el generador de la curva elíptica utilizada. Esta operación produce una nueva clave pública derivada de la original, conservando ciertas propiedades criptográficas que permiten su uso. Por ejemplo, este método se utiliza para las direcciones Taproot (P2TR), para permitir el gasto bien presentando una firma Schnorr de la forma tradicional, bien cumpliendo una de las condiciones establecidas en una Merkle Tree, también conocida como "MAST".