---
term: SCRIPTSIG
---

Un elemento en una transacción de Bitcoin ubicado en las entradas. El `scriptSig` proporciona los datos necesarios para satisfacer las condiciones establecidas por el `scriptPubKey` de la transacción anterior de la cual se están gastando los fondos. Por lo tanto, juega un papel complementario al `scriptPubKey`. Típicamente, el `scriptSig` contiene una firma digital y una clave pública. La firma es generada por el propietario de los bitcoins usando su clave privada y demuestra que tienen la autorización para gastar el UTXO. En este caso, el `scriptSig` demuestra que el poseedor de la entrada posee la clave privada correspondiente a la clave pública asociada con la dirección especificada en el `scriptPubKey` de la transacción saliente anterior.

Cuando la transacción es verificada, los datos del `scriptSig` se ejecutan en el correspondiente `scriptPubKey`. Si el resultado es válido, significa que se han cumplido las condiciones para gastar los fondos. Si todas las entradas de la transacción proporcionan un `scriptSig` que valida su `scriptPubKey`, la transacción es válida y puede ser añadida a un bloque para su ejecución.

Por ejemplo, aquí hay un clásico `scriptSig` P2PKH:

```text
<signature> <public key>
```

El `scriptPubKey` correspondiente sería:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *El `scriptSig` también es llamado a veces "script de desbloqueo" en inglés.*