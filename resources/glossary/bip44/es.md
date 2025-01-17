---
term: BIP44

---
Una propuesta de mejora que introduce una estructura de derivación jerárquica estándar para los monederos HD. BIP44 se basa en los principios establecidos por BIP32 para la derivación de claves y en BIP43 para el uso del campo "purpose". Introduce una estructura de derivación de cinco niveles: `m / purpose' / coin_type' / account' / change / address_index`. He aquí los detalles de cada profundidad:


- m /` indica la clave privada maestra. Es única para un monedero y no puede tener hermanos en la misma profundidad. La clave maestra se deriva directamente de la semilla del monedero;
- m / purpose' /` indica el propósito de la derivación que ayuda a identificar la norma seguida. Este campo se describe en BIP43. Por ejemplo, si la cartera sigue el estándar BIP84 (SegWit V0), el índice sería `84'`;
- m / purpose' / coin-type' /` indica el tipo de criptomoneda. Esto permite diferenciar claramente entre las ramas dedicadas a una criptodivisa y las dedicadas a otra criptodivisa en un monedero multidivisa. El índice dedicado a Bitcoin es `0'`;
- `m / propósito' / tipo de moneda' / cuenta' /` indica el número de cuenta. Esta profundidad permite diferenciar y organizar fácilmente un monedero en diferentes cuentas. Estas cuentas se numeran empezando por `0`. Las claves extendidas (`xpub`, `xprv`...) se encuentran en esta profundidad;
- `m / propósito' / tipo de moneda' / cuenta' / cambio /` indica la cadena. Cada cuenta definida en profundidad 3 tiene dos cadenas en profundidad 4: una cadena externa y una cadena interna (también llamada "cambio"). La cadena externa deriva las direcciones destinadas a ser comunicadas públicamente, es decir, las direcciones que se nos ofrecen cuando hacemos clic en "recibir" en el software de nuestro monedero. La cadena interna deriva las direcciones no destinadas a ser intercambiadas públicamente, es decir, principalmente las direcciones de cambio. La cadena externa se identifica con el índice `0` y la cadena interna con el índice `1`. Observará que a partir de esta profundidad, ya no realizamos una derivación endurecida, sino una derivación normal (no hay apóstrofe). Gracias a este mecanismo somos capaces de derivar todas las claves públicas hijas a partir de su `xpub`;
- `m / propósito' / tipo de moneda' / cuenta' / cambio / dirección-índice` indica simplemente el número de la dirección receptora y su par de claves, para diferenciarla de sus hermanas de la misma profundidad en la misma rama. Por ejemplo, la primera dirección derivada tiene el índice `0`, la segunda dirección tiene el índice `1`, y así sucesivamente...

Por ejemplo, si mi dirección de recepción tiene la ruta de derivación `m / 86' / 0' / 0' / 0 / 5`, podemos deducir la siguiente información:


- `86'` indica que estamos siguiendo el estándar de derivación de BIP86 (Taproot o SegWitV1);
- `0'` indica que se trata de una dirección Bitcoin;
- `0'` indica que estamos en la primera cuenta del monedero;
- `0` indica que se trata de una dirección externa;
- `5` indica que es la sexta dirección externa de esta cuenta.

![](../../dictionnaire/assets/18.webp)