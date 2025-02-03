---
term: DESCRIPTORES DE SCRIPT DE SALIDA

---
Los descriptores de scripts de salida, o simplemente descriptores, son expresiones estructuradas que describen completamente un script de salida (`scriptPubKey`) y proporcionan toda la información necesaria para rastrear transacciones hacia o desde un script específico. Estos descriptores facilitan la gestión de claves en los monederos HD mediante una descripción estándar de la estructura y los tipos de direcciones utilizados.

El principal interés de los descriptores reside en su capacidad para encapsular toda la información esencial para restaurar un monedero en una sola cadena (además de la frase de recuperación). Al guardar un descriptor con las frases mnemotécnicas correspondientes, es posible restaurar no sólo las claves privadas, sino también la estructura precisa del monedero y los parámetros de script asociados. De hecho, recuperar un monedero requiere no sólo conocer la semilla inicial, sino también índices específicos para la derivación de pares de claves hijos, así como el `xpub` de cada factor en el caso de un monedero multisig. Anteriormente, se asumía que esta información era conocida implícitamente por todos. Sin embargo, con la diversificación de los scripts y la aparición de configuraciones más complejas, esta información podía llegar a ser difícil de extrapolar, convirtiendo así estos datos en información privada y difícil de descifrar. El uso de descriptores simplifica enormemente el proceso: basta con conocer la frase o frases de recuperación y el descriptor correspondiente para restaurar todo de forma fiable y segura.

Un descriptor consta de varios elementos:


- Funciones de script como `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multifirma) y `sortedmulti` (Multifirma con claves ordenadas);
- Rutas de derivación, por ejemplo, `[d34db33f/44h/0h/0h]` que indica una ruta derivada y una huella digital de clave maestra específica;
- Claves en varios formatos, como claves públicas hexadecimales o claves públicas extendidas (`xpub`);
- Una suma de comprobación, precedida de un hash, para verificar la integridad del descriptor.

Por ejemplo, un descriptor para un monedero P2WPKH podría tener el siguiente aspecto:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

En este descriptor, la función de derivación `wpkh` indica un tipo de script Pay-to-Witness-Public-Key-Hash. Le sigue la ruta de derivación que contiene:


- `cdeab12f`: la huella digital de la llave maestra;
- `84h`: que significa el uso de un propósito BIP84, destinado a direcciones SegWit v0;
- `0h`: que indica que es una moneda BTC en la mainnet;
- `0h`: que se refiere al número de cuenta específico utilizado en el monedero.

El descriptor también incluye la clave pública extendida utilizada en esta cartera:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

A continuación, la notación `/<0;1>/*` especifica que el descriptor puede generar direcciones de la cadena externa (`0`) e interna (`1`), con un comodín (`*`) que permite la derivación secuencial de múltiples direcciones de forma configurable, similar a la gestión de un "límite de huecos" en el software de monedero tradicional.

Por último, `#jy0l7nr4` representa la suma de comprobación para verificar la integridad del descriptor.