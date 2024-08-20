---
term: TWEAK (CLAVE PÚBLICA)
---

En el campo de la criptografía, "modificar" una clave pública implica modificar esta clave utilizando un valor aditivo llamado "tweak" para que siga siendo utilizable con el conocimiento de la clave privada original y el tweak. Técnicamente, un tweak es un valor escalar que se suma a la clave pública inicial. Si $P$ es la clave pública y $t$ es el tweak, la clave pública modificada se convierte en:

$$
P' = P + tG
$$

Donde $G$ es el generador de la curva elíptica utilizada. Esta operación permite obtener una nueva clave pública derivada de la clave original mientras se retienen ciertas propiedades criptográficas que la hacen utilizable. Por ejemplo, este método se utiliza para direcciones Taproot (P2TR) para permitir el gasto ya sea presentando una firma Schnorr de la manera tradicional o cumpliendo una de las condiciones establecidas en un árbol de Merkle, también llamado "MAST".

![](../../dictionnaire/assets/26.png)