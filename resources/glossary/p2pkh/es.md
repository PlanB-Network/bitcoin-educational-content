---
term: P2PKH

---
P2PKH son las siglas de *Pay to Public Key Hash*. Es un modelo de escritura estándar utilizado para establecer condiciones de gasto en un UTXO. Permite bloquear bitcoins en un hash de una clave pública, es decir, en una dirección receptora. Este script está asociado al estándar Legacy y fue introducido en las primeras versiones de Bitcoin por Satoshi Nakamoto.

A diferencia del P2PK, en el que la clave pública se incluye explícitamente en el script, el P2PKH utiliza una huella criptográfica de la clave pública. Este script incluye el hash `RIPEMD160` del `SHA256` de la clave pública y estipula que, para acceder a los fondos, el destinatario debe proporcionar una clave pública que coincida con este hash, así como una firma digital válida generada a partir de la clave privada asociada. Las direcciones P2PKH se codifican utilizando el formato `Base58Check`, que les confiere robustez frente a errores tipográficos mediante el uso de una suma de comprobación. Estas direcciones empiezan siempre por el número "1".