---
term: DERIVATION PATH
---

En el contexto de las billeteras deterministas jerárquicas (HD), un camino de derivación se refiere a la secuencia de índices utilizados para derivar claves secundarias a partir de una clave maestra. Descrito en BIP32, este camino identifica la estructura de árbol para derivar claves secundarias. Un camino de derivación está representado por una serie de índices separados por barras inclinadas, y siempre comienza con la clave maestra (denotada como `m/`). Por ejemplo, un camino típico podría ser `m/84'/0'/0'/0/0`. Cada nivel de derivación está asociado con una profundidad específica:
* `m /` indica la clave privada maestra. Es única para una billetera y no puede tener hermanos a la misma profundidad. La clave maestra se deriva directamente de la semilla;
* `m / purpose' /` indica el propósito de derivación que ayuda a identificar el estándar seguido. Este campo se describe en BIP43. Por ejemplo, si la billetera se adhiere al estándar BIP84 (SegWit V0), el índice sería entonces `84'`;
* `m / purpose' / coin-type' /` indica el tipo de criptomoneda. Esto permite una clara diferenciación entre las ramas dedicadas a una criptomoneda y aquellas dedicadas a otra en una billetera multi-moneda. El índice dedicado a Bitcoin es `0'`;
* `m / purpose' / coin-type' / account' /` indica el número de cuenta. Esta profundidad facilita la diferenciación y organización de una billetera en diferentes cuentas. Estas cuentas están numeradas comenzando desde `0'`. Las claves extendidas (`xpub`, `xprv`...) se encuentran en este nivel de profundidad;
* `m / purpose' / coin-type' / account' / change /` indica el camino. Cada cuenta definida en la profundidad 3 tiene dos caminos en la profundidad 4: una cadena externa y una cadena interna (también llamada "cambio"). La cadena externa deriva direcciones destinadas a ser compartidas públicamente, es decir, las direcciones que se nos ofrecen cuando hacemos clic en "recibir" en nuestro software de billetera. La cadena interna deriva direcciones no destinadas a ser intercambiadas públicamente, principalmente direcciones de cambio. La cadena externa se identifica con el índice `0` y la cadena interna se identifica con el índice `1`. Notarás que a partir de esta profundidad, ya no realizamos una derivación endurecida, sino una derivación normal (no hay apóstrofo). Es gracias a este mecanismo que somos capaces de derivar todas las claves públicas secundarias a partir de su `xpub`;

* `m / purpose' / coin-type' / account' / change / address-index` simplemente indica el número de la dirección receptora y su par de claves, para diferenciarla de sus hermanos a la misma profundidad en la misma rama. Por ejemplo, la primera dirección derivada tiene el índice `0`, la segunda dirección tiene el índice `1`, y así sucesivamente...

Por ejemplo, si mi dirección receptora tiene el camino de derivación `m / 86' / 0' / 0' / 0 / 5`, podemos deducir la siguiente información:
* `86'` indica que estamos siguiendo el estándar de derivación de BIP86 (Taproot / SegWit V1);
* `0'` indica que es una dirección de Bitcoin;
* `0'` indica que estamos en la primera cuenta de la billetera;
* `0` indica que es una dirección externa;
* `5` indica que es la sexta dirección externa de esta cuenta.

![](../../dictionnaire/assets/18.png)