---
term: BIP44
---

Una propuesta de mejora que introduce una estructura de derivación jerárquica estándar para las carteras HD. BIP44 se basa en los principios establecidos por BIP32 para la derivación de claves y en BIP43 para el uso del campo “purpose” (propósito). Introduce una estructura de derivación de cinco niveles: `m / purpose' / coin_type' / account' / change / address_index`. Aquí están los detalles de cada profundidad:
* `m /` indica la clave privada maestra. Es única para una cartera y no puede tener hermanos en la misma profundidad. La clave maestra se deriva directamente de la semilla de la cartera;
* `m / purpose' /` indica el propósito de derivación que ayuda a identificar el estándar seguido. Este campo se describe en BIP43. Por ejemplo, si la cartera sigue el estándar BIP84 (SegWit V0), el índice sería entonces `84'`;
* `m / purpose' / coin-type' /` indica el tipo de criptomoneda. Esto permite una clara diferenciación entre las ramas dedicadas a una criptomoneda y aquellas dedicadas a otra criptomoneda en una cartera multi-moneda. El índice dedicado a Bitcoin es `0'`;
* `m / purpose' / coin-type' / account' /` indica el número de cuenta. Esta profundidad permite una fácil diferenciación y organización de una cartera en diferentes cuentas. Estas cuentas están numeradas comenzando desde `0'`. Las claves extendidas (`xpub`, `xprv`...) se encuentran en esta profundidad;
* `m / purpose' / coin-type' / account' / change /` indica la cadena. Cada cuenta definida en la profundidad 3 tiene dos cadenas en la profundidad 4: una cadena externa y una cadena interna (también llamada “change”). La cadena externa deriva direcciones destinadas a ser comunicadas públicamente, es decir, las direcciones que se nos ofrecen cuando hacemos clic en “recibir” en nuestro software de cartera. La cadena interna deriva direcciones no destinadas a ser intercambiadas públicamente, es decir, principalmente direcciones de cambio. La cadena externa se identifica con el índice `0` y la cadena interna se identifica con el índice `1`. Notarás que a partir de esta profundidad, ya no realizamos una derivación endurecida, sino una derivación normal (no hay apóstrofo). Es gracias a este mecanismo que somos capaces de derivar todas las claves públicas hijas de su `xpub`;
* `m / purpose' / coin-type' / account' / change / address-index` simplemente indica el número de la dirección receptora y su par de claves, para diferenciarla de sus hermanos en la misma profundidad en la misma rama. Por ejemplo, la primera dirección derivada tiene el índice `0`, la segunda dirección tiene el índice `1`, y así sucesivamente...
Por ejemplo, si mi dirección receptora tiene la ruta de derivación `m / 86' / 0' / 0' / 0 / 5`, podemos deducir la siguiente información:
* `86'` indica que estamos siguiendo el estándar de derivación de BIP86 (Taproot o SegWitV1);
* `0'` indica que es una dirección de Bitcoin;
* `0'` indica que estamos en la primera cuenta de la cartera;
* `0` indica que es una dirección externa;
* `5` indica que es la sexta dirección externa de esta cuenta.

![](../../dictionnaire/assets/18.png)