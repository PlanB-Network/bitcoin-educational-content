---
term: CLAVE EXTENDIDA
---

Una secuencia de caracteres que combina una clave (pública o privada), su código de cadena asociado y una serie de metadatos. Una clave extendida compila todos los elementos necesarios para derivar claves secundarias en un solo identificador. Se utilizan en carteras deterministas y jerárquicas y pueden ser de dos tipos: una clave pública extendida (usada para derivar claves públicas secundarias) o una clave privada extendida (usada para derivar tanto claves privadas como públicas secundarias). Una clave extendida incluye, por lo tanto, varios datos diferentes, descritos en BIP32, en el orden:
* El prefijo: `prv` y `pub` son HRP (Parte Legible por Humanos) que indican si es una clave privada extendida (`prv`) o una clave pública extendida (`pub`). La primera letra del prefijo designa la versión de la clave extendida: `x` para Legacy o SegWit V1 en Bitcoin, `t` para Legacy o SegWit V1 en Bitcoin Testnet, `y` para Nested SegWit en Bitcoin, `u` para Nested SegWit en Bitcoin Testnet, `z` para SegWit V0 en Bitcoin, `v` para SegWit V0 en Bitcoin Testnet.
* La profundidad, que indica el número de derivaciones desde la clave maestra para alcanzar la clave extendida;
* La huella digital del padre. Esto representa los primeros 4 bytes del `HASH160` de la clave pública del padre;
* El índice. Este es el número del par entre sus hermanos del cual se deriva la clave extendida;
* El código de cadena;
* Un byte de relleno si es una clave privada `0x00`;
* La clave privada o pública;
* Un checksum. Representa los primeros 4 bytes del `HASH256` del resto de la clave extendida.

En la práctica, la clave pública extendida se utiliza para generar direcciones de recepción y para observar las transacciones de una cuenta sin exponer las claves privadas asociadas. Esto puede permitir, por ejemplo, la creación de una cartera denominada "solo visualización". Sin embargo, es importante notar que la clave pública extendida es información sensible para la privacidad del usuario, ya que su divulgación puede permitir a terceros rastrear transacciones y ver el saldo de la cuenta asociada.