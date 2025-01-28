---
term: SCRIPTPUBKEY

---
Ein Skript, das sich im Ausgabeteil einer Bitcoin-Transaktion befindet und die Bedingungen festlegt, unter denen der zugehörige UTXO ausgegeben werden kann. Dieses Skript sichert also Bitcoins. In seiner gebräuchlichsten Form enthält das `scriptPubKey` eine Bedingung, die verlangt, dass die nächste Transaktion den Besitz des privaten Schlüssels, der einer bestimmten Bitcoin-Adresse entspricht, nachweist. Dies wird häufig durch ein Skript erreicht, das eine Signatur verlangt, die dem öffentlichen Schlüssel entspricht, der mit der Adresse verbunden ist, die zur Sicherung dieser Gelder verwendet wird. Wenn eine Transaktion versucht, diese UTXO als Eingabe zu verwenden, muss sie eine "scriptSig" bereitstellen, die in Kombination mit dem "scriptPubKey" die festgelegten Bedingungen erfüllt und ein gültiges Skript ergibt.

Hier ist zum Beispiel ein klassischer P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Die entsprechende `scriptSig` wäre:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Diese Schrift wird im Englischen manchmal auch als "locking script" bezeichnet