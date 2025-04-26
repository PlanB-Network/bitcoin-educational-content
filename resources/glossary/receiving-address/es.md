---
term: DIRECCIÓN DE RECEPCIÓN

---
Información utilizada para recibir bitcoins. Una dirección se construye normalmente haciendo un hash de una clave pública, utilizando `SHA256` y `RIMPEMD160`, y añadiendo metadatos a este digesto. Las claves públicas utilizadas para construir una dirección receptora forman parte del monedero del usuario y, por tanto, derivan de su semilla. Por ejemplo, las direcciones SegWit se componen de la siguiente información:


- Un HRP para designar "bitcoin": `bc`;
- Un separador: `1`;
- La versión de SegWit utilizada: `q` o `p`;
- La carga útil: el resumen de la clave pública (o directamente la clave pública en el caso de Taproot);
- La suma de comprobación: un código BCH.

Sin embargo, una dirección de recepción también puede representar otra cosa dependiendo del modelo de script utilizado. Por ejemplo, las direcciones P2SH se construyen utilizando el hash del script. Las direcciones Taproot, por otro lado, contienen la clave pública ajustada directamente sin hash.

Una dirección de recepción puede representarse en forma de cadena alfanumérica o de código QR. Cada dirección puede utilizarse varias veces, pero es una práctica muy desaconsejada. De hecho, para mantener un cierto nivel de privacidad, se aconseja utilizar cada dirección Bitcoin una sola vez. Debe generarse una nueva dirección para cada pago recibido en el monedero. Una dirección se codifica en `Bech32` para direcciones SegWit V0, en `Bech32m` para direcciones SegWit V1, y en `Base58check` para direcciones Legacy. Desde un punto de vista técnico, recibir bitcoins se traduce en poseer la clave privada asociada a una clave pública (y, por tanto, una dirección). Cuando alguien recibe bitcoins, el remitente actualiza la restricción existente sobre su gasto, de modo que ahora sólo el destinatario puede tener este poder.

![](../../dictionnaire/assets/23.webp)