---
term: VOUT
---

Ein spezifisches Element einer Bitcoin-Transaktion, das das Ziel der gesendeten Mittel bestimmt. Eine Transaktion kann mehrere Ausgänge umfassen, die jeweils eindeutig durch die Kombination des Transaktionsidentifikators (`txid`) und eines Index namens `vout` identifiziert werden. Dieser Index, beginnend bei `0`, markiert die Position des Ausgangs in der Sequenz der Transaktionsausgänge. Somit wird der erste Ausgang durch `"vout": 0`, der zweite durch `"vout": 1` und so weiter bezeichnet.

Jeder `vout` umfasst hauptsächlich zwei Informationen:
* den Wert, ausgedrückt in Bitcoins, der den gesendeten Betrag darstellt;
* ein Sperrskript (`scriptPubKey`), das die Bedingungen festlegt, die erfüllt sein müssen, damit die Mittel in einer zukünftigen Transaktion erneut ausgegeben werden können.

Die Kombination aus dem `txid` und dem `vout` eines spezifischen Teils bildet das, was als UTXO bezeichnet wird, zum Beispiel:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```