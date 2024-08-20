---
term: DIRECCIÓN DE RECEPCIÓN
---

Información utilizada para recibir bitcoins. Una dirección se construye usualmente mediante el hash de una clave pública, usando `SHA256` y `RIMPEMD160`, y añadiendo metadatos a este resumen. Las claves públicas usadas para construir una dirección de recepción son parte de la cartera del usuario y, por lo tanto, se derivan de su semilla. Por ejemplo, las direcciones SegWit están compuestas de la siguiente información:
* Un HRP para designar "bitcoin": `bc`;
* Un separador: `1`;
* La versión de SegWit utilizada: `q` o `p`;
* El payload: el resumen de la clave pública (o directamente la clave pública en el caso de Taproot);
* El checksum: un código BCH.

Sin embargo, una dirección de recepción también puede representar algo diferente dependiendo del modelo de script utilizado. Por ejemplo, las direcciones P2SH se construyen usando el hash del script. Las direcciones Taproot, por otro lado, contienen la clave pública modificada directamente sin hashearla.

Una dirección de recepción puede ser representada en forma de una cadena alfanumérica o como un código QR. Cada dirección puede ser utilizada múltiples veces, pero esta es una práctica altamente desaconsejada. De hecho, para mantener un cierto nivel de privacidad, se aconseja usar cada dirección de Bitcoin solo una vez. Se debe generar una nueva dirección para cada pago entrante a la cartera de uno. Una dirección está codificada en `Bech32` para direcciones SegWit V0, en `Bech32m` para direcciones SegWit V1, y en `Base58check` para direcciones Legacy. Desde un punto de vista técnico, recibir bitcoins se traduce en poseer la clave privada asociada con una clave pública (y por lo tanto una dirección). Cuando alguien recibe bitcoins, el remitente actualiza la restricción existente sobre su gasto de modo que solo el receptor ahora puede tener este poder.

![](../../dictionnaire/assets/23.png)