---
term: P2PKH
---

P2PKH significa *Pay to Public Key Hash* (Pagar al Hash de la Clave Pública). Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. Permite bloquear bitcoins en un hash de una clave pública, es decir, en una dirección de recepción. Este script está asociado con el estándar Legacy y fue introducido en las primeras versiones de Bitcoin por Satoshi Nakamoto.

A diferencia de P2PK, donde la clave pública se incluye explícitamente en el script, P2PKH utiliza una huella digital criptográfica de la clave pública. Este script incluye el hash `RIPEMD160` del `SHA256` de la clave pública y estipula que, para acceder a los fondos, el destinatario debe proporcionar una clave pública que coincida con este hash, así como una firma digital válida generada a partir de la clave privada asociada. Las direcciones P2PKH se codifican utilizando el formato `Base58Check`, lo que les otorga robustez contra errores tipográficos mediante el uso de un checksum. Estas direcciones siempre comienzan con el número `1`.