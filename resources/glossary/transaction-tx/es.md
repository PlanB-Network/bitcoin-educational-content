---
term: TRANSACTION (TX)
---

En el contexto de Bitcoin, una transacción (abreviada como "TX") es una operación registrada en la blockchain que transfiere la propiedad de bitcoins de una o más entradas a una o más salidas. Cada transacción consume Salidas de Transacción No Gastadas (UTXOs, por sus siglas en inglés) como entradas, las cuales son salidas de transacciones anteriores, y crea nuevas UTXOs como salidas, que pueden ser utilizadas como entradas en transacciones futuras.

Cada entrada incluye una referencia a una salida existente junto con un script de firma (`scriptSig`) que cumple con las condiciones de gasto (`scriptPubKey`) establecidas por la salida a la que hace referencia. Esto es lo que permite que los bitcoins sean desbloqueados. Las salidas definen nuevas condiciones de gasto (`scriptPubKey`) para los bitcoins transferidos, a menudo en forma de una clave pública o una dirección a la cual los bitcoins están ahora asociados.