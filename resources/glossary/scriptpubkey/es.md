---
term: SCRIPTPUBKEY
---

Un script ubicado en la parte de salida de una transacción de Bitcoin que define las condiciones bajo las cuales el UTXO asociado puede ser gastado. Este script, por lo tanto, asegura los bitcoins. En su forma más común, el `scriptPubKey` contiene una condición que requiere que la próxima transacción proporcione prueba de posesión de la clave privada correspondiente a una dirección de Bitcoin especificada. Esto se logra a menudo mediante un script que exige una firma correspondiente a la clave pública asociada con la dirección utilizada para asegurar estos fondos. Cuando una transacción intenta usar este UTXO como entrada, debe proporcionar un `scriptSig` que, una vez combinado con el `scriptPubKey`, cumple con las condiciones establecidas y produce un script válido.

Por ejemplo, aquí hay un clásico `scriptPubKey` P2PKH:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <dirección> OP_EQUALVERIFY OP_CHECKSIG
```

El `scriptSig` correspondiente sería:

```text
<firma> <clave pública>
```

![](../../dictionnaire/assets/35.png)

> ► *Este script también se conoce a veces como "script de bloqueo" en inglés.*