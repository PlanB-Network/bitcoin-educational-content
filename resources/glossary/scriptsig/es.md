---
term: SCRIPTSIG

---
Elemento de una transacción Bitcoin situado en las entradas. El `scriptSig` proporciona los datos necesarios para satisfacer las condiciones establecidas por el `scriptPubKey` de la transacción anterior de la que se están gastando fondos. Por tanto, desempeña un papel complementario al de la `scriptPubKey`. Normalmente, el `scriptSig` contiene una firma digital y una clave pública. La firma la genera el propietario de los bitcoins utilizando su clave privada y demuestra que tiene autorización para gastar los UTXO. En este caso, el `scriptSig` demuestra que el titular de la entrada posee la clave privada correspondiente a la clave pública asociada a la dirección especificada en el `scriptPubKey` de la transacción saliente anterior.

Cuando se verifica la transacción, los datos del `scriptSig` se ejecutan en el `scriptPubKey` correspondiente. Si el resultado es válido, significa que se han cumplido las condiciones para gastar los fondos. Si todas las entradas de la transacción proporcionan un `scriptSig` que valida su `scriptPubKey`, la transacción es válida y puede añadirse a un bloque para su ejecución.

Por ejemplo, he aquí un `scriptSig` clásico de P2PKH:

```text
<signature> <public key>
```

La `scriptPubKey` correspondiente sería:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *El `scriptSig` también se llama a veces `script de desbloqueo` en inglés