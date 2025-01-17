---
term: SCRIPTSIG

---
Ein Element in einer Bitcoin-Transaktion, das sich in den Eingängen befindet. Die `scriptSig` liefert die notwendigen Daten, um die Bedingungen zu erfüllen, die durch den `scriptPubKey` der vorhergehenden Transaktion festgelegt wurden, aus der Gelder ausgegeben werden. Es spielt somit eine ergänzende Rolle zum `scriptPubKey`. Typischerweise enthält das `scriptSig` eine digitale Signatur und einen öffentlichen Schlüssel. Die Signatur wird vom Eigentümer der Bitcoins mit seinem privaten Schlüssel erzeugt und beweist, dass er berechtigt ist, die UTXO auszugeben. In diesem Fall beweist das `scriptSig`, dass der Inhaber der Eingabe den privaten Schlüssel besitzt, der dem öffentlichen Schlüssel entspricht, der mit der in `scriptPubKey` angegebenen Adresse der vorherigen ausgehenden Transaktion verbunden ist.

Wenn die Transaktion überprüft wird, werden die Daten aus dem `scriptSig` in dem entsprechenden `scriptPubKey` ausgeführt. Wenn das Ergebnis gültig ist, bedeutet dies, dass die Bedingungen für die Ausgabe der Mittel erfüllt wurden. Wenn alle Eingänge der Transaktion ein `scriptSig` liefern, das ihren `scriptPubKey` validiert, ist die Transaktion gültig und kann einem Block zur Ausführung hinzugefügt werden.

Hier ist zum Beispiel ein klassisches P2PKH `scriptSig`:

```text
<signature> <public key>
```

Der entsprechende "ScriptPubKey" würde lauten:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *Das `scriptSig` wird im Englischen manchmal auch als "unlocking script" bezeichnet