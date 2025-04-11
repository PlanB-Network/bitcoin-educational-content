---
term: VIN

---
Ein spezifisches Element einer Bitcoin-Transaktion, das die Quelle der Mittel angibt, die zur Befriedigung der Ausgaben verwendet werden. Jedes "Vin" bezieht sich auf einen nicht verbrauchten Output (UTXO) aus einer vorherigen Transaktion. Eine Transaktion kann mehrere Inputs enthalten, die jeweils durch eine Kombination aus "txid" (der Kennung der ursprünglichen Transaktion) und "vout" (dem Index des Outputs in dieser Transaktion) identifiziert werden.

Jedes "Vin" enthält die folgenden Informationen:


- txid": die Kennung der vorherigen Transaktion, die die hier als Eingabe verwendete Ausgabe enthält;
- vout": der Index der Ausgabe in der vorherigen Transaktion;
- `scriptSig` oder `scriptWitness`: ein Entsperrungsskript, das die notwendigen Daten liefert, um die Bedingungen zu erfüllen, die durch den `scriptPubKey` der vorangegangenen Transaktion, für die Gelder ausgegeben werden, gestellt werden, in der Regel durch Bereitstellung einer kryptografischen Signatur;
- nSequence": ein spezielles Feld, das angibt, wie diese Eingabe zeitlich gebunden ist, sowie andere Optionen wie RBF.