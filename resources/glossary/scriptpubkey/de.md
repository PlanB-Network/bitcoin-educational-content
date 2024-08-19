---
term: SCRIPTPUBKEY
---

Ein Skript, das sich im Ausgabeteil einer Bitcoin-Transaktion befindet und die Bedingungen definiert, unter denen das zugehörige UTXO ausgegeben werden kann. Dieses Skript sichert also Bitcoins. In seiner häufigsten Form enthält das `scriptPubKey` eine Bedingung, die verlangt, dass die nächste Transaktion den Nachweis des Besitzes des privaten Schlüssels erbringt, der einer bestimmten Bitcoin-Adresse zugeordnet ist. Dies wird oft durch ein Skript erreicht, das eine Unterschrift verlangt, die dem öffentlichen Schlüssel entspricht, der mit der Adresse verbunden ist, die verwendet wurde, um diese Mittel zu sichern. Wenn eine Transaktion versucht, dieses UTXO als Eingabe zu verwenden, muss sie ein `scriptSig` bereitstellen, das, einmal mit dem `scriptPubKey` kombiniert, die festgelegten Bedingungen erfüllt und ein gültiges Skript produziert.

Zum Beispiel, hier ist ein klassisches P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <Adresse> OP_EQUALVERIFY OP_CHECKSIG
```

Das entsprechende `scriptSig` wäre:

```text
<Signatur> <öffentlicher Schlüssel>
```

![](../../dictionnaire/assets/35.png)

> ► *Dieses Skript wird manchmal auch als "Locking Script" auf Englisch bezeichnet.*