---
term: TRANSACCIÓN (TX)

---
En el contexto de Bitcoin, una transacción (abreviada como "TX") es una operación registrada en la cadena de bloques que transfiere la propiedad de bitcoins de una o más entradas a una o más salidas. Cada transacción consume Unspent Transaction Outputs (UTXOs) como entradas, que son salidas de transacciones anteriores, y crea nuevos UTXOs como salidas, que pueden utilizarse como entradas en transacciones futuras.

Cada entrada incluye una referencia a una salida existente junto con un script de firma (`scriptSig`) que cumple las condiciones de gasto (`scriptPubKey`) establecidas por la salida a la que hace referencia. Esto es lo que permite desbloquear bitcoins. Las salidas definen nuevas condiciones de gasto (`scriptPubKey`) para los bitcoins transferidos, a menudo en forma de una clave pública o una dirección a la que los bitcoins están ahora asociados.