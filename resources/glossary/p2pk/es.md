---
term: P2PK

---
P2PK significa *Pago a Clave Pública*. Es un modelo de escritura estándar utilizado en Bitcoin para establecer condiciones de gasto en un UTXO. Permite bloquear bitcoins directamente en una clave pública, en lugar de una dirección.

Técnicamente, el script P2PK contiene una clave pública y una instrucción que exige la correspondiente firma digital para desbloquear los fondos. Cuando el propietario desea gastar los bitcoins, debe proporcionar una firma producida con la clave privada asociada. Esta firma se verifica mediante el algoritmo ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK se utilizó a menudo en las primeras versiones de Bitcoin, especialmente por Satoshi Nakamoto. Hoy en día ya casi no se utiliza.