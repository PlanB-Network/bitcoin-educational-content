---
term: DESCRIPCIÓN DE SCRIPTS DE SALIDA
---

Los descriptores de scripts de salida, o simplemente descriptores, son expresiones estructuradas que describen completamente un script de salida (`scriptPubKey`) y proporcionan toda la información necesaria para rastrear transacciones hacia o desde un script específico. Estos descriptores facilitan la gestión de llaves en billeteras HD a través de una descripción estándar de la estructura y tipos de direcciones utilizadas.

El principal interés de los descriptores radica en su capacidad para encapsular toda la información esencial para restaurar una billetera en una sola cadena (además de la frase de recuperación). Al guardar un descriptor con las frases mnemotécnicas correspondientes, es posible restaurar no solo las llaves privadas sino también la estructura precisa de la billetera y los parámetros de script asociados. De hecho, recuperar una billetera requiere no solo el conocimiento de la semilla inicial sino también índices específicos para la derivación de pares de llaves secundarias, así como el `xpub` de cada factor en el caso de una billetera multisig. Anteriormente, se asumía que esta información era implícitamente conocida por todos. Sin embargo, con la diversificación de scripts y la aparición de configuraciones más complejas, esta información podría volverse difícil de extrapolar, convirtiendo estos datos en información privada y difícil de forzar bruscamente. El uso de descriptores simplifica enormemente el proceso: es suficiente conocer la(s) frase(s) de recuperación y el descriptor correspondiente para restaurar todo de manera fiable y segura.

Un descriptor consiste en varios elementos:
* Funciones de script como `pk` (Pago-a-PubKey), `pkh` (Pago-a-PubKey-Hash), `wpkh` (Pago-a-Witness-PubKey-Hash), `sh` (Pago-a-Script-Hash), `wsh` (Pago-a-Witness-Script-Hash), `tr` (Pago-a-Taproot), `multi` (Multifirma), y `sortedmulti` (Multifirma con llaves ordenadas);
* Caminos de derivación, por ejemplo, `[d34db33f/44h/0h/0h]` indicando un camino derivado y una huella digital de llave maestra específica;
* Llaves en varios formatos como llaves públicas hexadecimales o llaves públicas extendidas (`xpub`);
* Un checksum, precedido por un hash, para verificar la integridad del descriptor.

Por ejemplo, un descriptor para una billetera P2WPKH podría lucir así:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
En este descriptor, la función de derivación `wpkh` indica un tipo de script Pay-to-Witness-Public-Key-Hash. Le sigue el camino de derivación que contiene:
* `cdeab12f`: la huella digital de la llave maestra;
* `84h`: que significa el uso de un propósito BIP84, destinado para direcciones SegWit v0;
* `0h`: que indica que es una moneda BTC en la red principal;
* `0h`: que se refiere al número de cuenta específico utilizado en la billetera.

El descriptor también incluye la llave pública extendida utilizada en esta billetera:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

A continuación, la notación `/<0;1>/*` especifica que el descriptor puede generar direcciones de la cadena externa (`0`) e interna (`1`), con un comodín (`*`) que permite la derivación secuencial de múltiples direcciones de una manera configurable, similar a la gestión de un "límite de brecha" en el software de billetera tradicional.

Finalmente, `#jy0l7nr4` representa la suma de verificación para verificar la integridad del descriptor.