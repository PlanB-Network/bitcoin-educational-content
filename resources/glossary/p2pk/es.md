---
term: P2PK
---

P2PK significa *Pay to Public Key* (Pago a la Clave Pública). Es un modelo de script estándar utilizado en Bitcoin para establecer condiciones de gasto en un UTXO. Permite bloquear bitcoins directamente en una clave pública, en lugar de en una dirección.
Técnicamente, el script P2PK contiene una clave pública y una instrucción que exige una firma digital correspondiente para desbloquear los fondos. Cuando el propietario desea gastar los bitcoins, debe proporcionar una firma producida con la clave privada asociada. Esta firma se verifica utilizando el ECDSA (*Elliptic Curve Digital Signature Algorithm* - Algoritmo de Firma Digital de Curva Elíptica). P2PK se utilizó a menudo en las primeras versiones de Bitcoin, notablemente por Satoshi Nakamoto. Hoy en día, casi no se utiliza.