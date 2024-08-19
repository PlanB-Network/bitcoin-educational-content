---
term: SCRIPTSIG
---

Ein Element in einer Bitcoin-Transaktion, das sich bei den Eingaben befindet. Das `scriptSig` liefert die notwendigen Daten, um die Bedingungen zu erfüllen, die durch das `scriptPubKey` der vorherigen Transaktion gesetzt wurden, von der Gelder ausgegeben werden. Es spielt somit eine ergänzende Rolle zum `scriptPubKey`. Typischerweise enthält das `scriptSig` eine digitale Signatur und einen öffentlichen Schlüssel. Die Signatur wird vom Besitzer der Bitcoins mit ihrem privaten Schlüssel erzeugt und beweist, dass sie die Autorisierung haben, das UTXO auszugeben. In diesem Fall demonstriert das `scriptSig`, dass der Inhaber der Eingabe den privaten Schlüssel besitzt, der dem öffentlichen Schlüssel zugeordnet ist, der mit der Adresse im `scriptPubKey` der vorherigen ausgehenden Transaktion angegeben ist.

Wenn die Transaktion verifiziert wird, werden die Daten aus dem `scriptSig` im entsprechenden `scriptPubKey` ausgeführt. Wenn das Ergebnis gültig ist, bedeutet dies, dass die Bedingungen für die Ausgabe der Mittel erfüllt wurden. Wenn alle Eingaben der Transaktion ein `scriptSig` bereitstellen, das ihr `scriptPubKey` validiert, ist die Transaktion gültig und kann einem Block zur Ausführung hinzugefügt werden.

Zum Beispiel, hier ist ein klassisches P2PKH `scriptSig`:

```text
<Signatur> <öffentlicher Schlüssel>
```

Das entsprechende `scriptPubKey` wäre:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <Adresse> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *Das `scriptSig` wird manchmal auch auf Englisch als "unlocking script" bezeichnet.*