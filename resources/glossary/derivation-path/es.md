---
term: VÍA DE DERIVACIÓN

---
En el contexto de los monederos deterministas jerárquicos (HD), una ruta de derivación se refiere a la secuencia de índices utilizados para derivar claves hijas a partir de una clave maestra. Descrita en BIP32, esta ruta identifica la estructura de árbol para derivar claves hijas. Una ruta de derivación está representada por una serie de índices separados por barras oblicuas, y siempre comienza con la clave maestra (denotada como `m/`). Por ejemplo, una ruta típica podría ser `m/84'/0'/0'/0/0`. Cada nivel de derivación está asociado a una profundidad específica:


- m /` indica la clave privada maestra. Es única para un monedero y no puede tener hermanos en la misma profundidad. La clave maestra se deriva directamente de la semilla;
- m / purpose' /` indica el propósito de la derivación que ayuda a identificar la norma seguida. Este campo se describe en BIP43. Por ejemplo, si la cartera se adhiere al estándar BIP84 (SegWit V0), el índice sería `84'`;
- m / purpose' / coin-type' /` indica el tipo de criptomoneda. Esto permite diferenciar claramente las ramas dedicadas a una criptodivisa de las dedicadas a otra en un monedero multidivisa. El índice dedicado a Bitcoin es `0'`;
- `m / propósito' / tipo de moneda' / cuenta' /` indica el número de cuenta. Esta profundidad facilita la diferenciación y organización de un monedero en diferentes cuentas. Estas cuentas se numeran empezando por `0`. Las claves extendidas (`xpub`, `xprv`...) se encuentran en este nivel de profundidad;
- `m / propósito' / tipo de moneda' / cuenta' / cambio /` indica la ruta. Cada cuenta definida en profundidad 3 tiene dos caminos en profundidad 4: una cadena externa y una cadena interna (también llamada "cambio"). La cadena externa deriva las direcciones destinadas a ser compartidas públicamente, es decir, las direcciones que se nos ofrecen cuando hacemos clic en "recibir" en el software de nuestro monedero. La cadena interna deriva direcciones no destinadas a ser intercambiadas públicamente, principalmente direcciones de cambio. La cadena externa se identifica con el índice `0` y la cadena interna con el índice `1`. Observará que a partir de esta profundidad, ya no realizamos una derivación endurecida, sino una derivación normal (no hay apóstrofe). Gracias a este mecanismo podemos derivar todas las claves públicas hijas a partir de su `xpub`;
- `m / propósito' / tipo de moneda' / cuenta' / cambio / dirección-índice` indica simplemente el número de la dirección receptora y su par de claves, para diferenciarla de sus hermanas de la misma profundidad en la misma rama. Por ejemplo, la primera dirección derivada tiene el índice `0`, la segunda dirección tiene el índice `1`, y así sucesivamente...

Por ejemplo, si mi dirección de recepción tiene la ruta de derivación `m / 86' / 0' / 0' / 0 / 5`, podemos deducir la siguiente información:


- `86'` indica que estamos siguiendo el estándar de derivación de BIP86 (Taproot / SegWit V1);
- `0'` indica que se trata de una dirección Bitcoin;
- `0'` indica que estamos en la primera cuenta del monedero;
- `0` indica que se trata de una dirección externa;
- `5` indica que es la sexta dirección externa de esta cuenta.

![](../../dictionnaire/assets/18.webp)