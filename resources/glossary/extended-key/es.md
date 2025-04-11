---
term: CLAVE AMPLIADA

---
Secuencia de caracteres que combina una clave (pública o privada), su código de cadena asociado y una serie de metadatos. Una clave extendida compila todos los elementos necesarios para derivar claves hijas en un único identificador. Se utilizan en los monederos deterministas y jerárquicos y pueden ser de dos tipos: una clave pública extendida (utilizada para derivar claves públicas hijas) o una clave privada extendida (utilizada para derivar tanto claves privadas como públicas hijas). Una clave extendida incluye, por tanto, varios datos diferentes, descritos en BIP32, en el orden:


- El prefijo: `prv` y `pub` son HRP (Human Readable Part) que indican si se trata de una clave privada extendida (`prv`) o una clave pública extendida (`pub`). La primera letra del prefijo designa la versión de la clave extendida: `x` para Legacy o SegWit V1 en Bitcoin, `t` para Legacy o SegWit V1 en Bitcoin Testnet, `y` para Nested SegWit en Bitcoin, `u` para Nested SegWit en Bitcoin Testnet, `z` para SegWit V0 en Bitcoin, `v` para SegWit V0 en Bitcoin Testnet.
- La profundidad, que indica el número de derivaciones a partir de la clave maestra para llegar a la clave extendida;
- La huella digital del padre. Representa los 4 primeros bytes del `HASH160` de la clave pública padre;
- El índice. Es el número del par entre sus hermanos del que se deriva la clave extendida;
- El código de la cadena;
- Un byte de relleno si se trata de una clave privada `0x00`;
- La clave privada o pública;
- Una suma de comprobación. Representa los 4 primeros bytes del `HASH256` del resto de la clave extendida.

En la práctica, la clave pública ampliada se utiliza para generar direcciones de recepción y observar las transacciones de una cuenta sin exponer las claves privadas asociadas. Esto puede permitir, por ejemplo, la creación de un monedero denominado "sólo de vigilancia". Sin embargo, es importante señalar que la clave pública extendida es información sensible para la privacidad del usuario, ya que su divulgación puede permitir a terceros rastrear transacciones y ver el saldo de la cuenta asociada.