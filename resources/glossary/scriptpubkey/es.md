---
term: SCRIPTPUBKEY

---
Un script ubicado en la parte de salida de una transacción Bitcoin que define las condiciones bajo las cuales el UTXO asociado puede ser gastado. Este script asegura así los bitcoins. En su forma más común, el `scriptPubKey` contiene una condición que requiere que la siguiente transacción proporcione una prueba de posesión de la clave privada correspondiente a una dirección Bitcoin especificada. Esto se consigue a menudo mediante un script que exige una firma correspondiente a la clave pública asociada a la dirección utilizada para asegurar estos fondos. Cuando una transacción intenta utilizar este UTXO como entrada, debe proporcionar un `scriptSig` que, una vez combinado con el `scriptPubKey`, cumpla las condiciones establecidas y produzca un script válido.

Por ejemplo, he aquí un clásico P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

El `scriptSig` correspondiente sería:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Este script también se denomina a veces en inglés "locking script "*