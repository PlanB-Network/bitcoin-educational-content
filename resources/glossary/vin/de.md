---
term: VIN
---

Ein spezifisches Element einer Bitcoin-Transaktion, das die Herkunft der Mittel angibt, die verwendet werden, um die Ausgaben zu decken. Jeder `vin` bezieht sich auf einen unverbrauchten Ausgang (UTXO) aus einer vorherigen Transaktion. Eine Transaktion kann mehrere Eingaben enthalten, die jeweils durch eine Kombination aus dem `txid` (der Kennung der ursprünglichen Transaktion) und dem `vout` (der Index des Ausgangs in dieser Transaktion) identifiziert werden.

Jeder `vin` enthält die folgenden Informationen:
* `txid`: die Kennung der vorherigen Transaktion, die den hier als Eingabe verwendeten Ausgang enthält;
* `vout`: der Index des Ausgangs in der vorherigen Transaktion;
* `scriptSig` oder `scriptWitness`: ein Entsperrungsskript, das die notwendigen Daten bereitstellt, um die Bedingungen zu erfüllen, die durch das `scriptPubKey` der vorherigen Transaktion gestellt werden, deren Mittel ausgegeben werden, in der Regel durch Bereitstellung einer kryptografischen Signatur;
* `nSequence`: ein spezifisches Feld, das verwendet wird, um anzugeben, wie dieser Eingang zeitlich gesperrt ist, sowie andere Optionen wie RBF.