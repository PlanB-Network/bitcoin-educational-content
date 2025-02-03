---
term: VOUT

---
Ein spezifisches Element einer Bitcoin-Transaktion, das das Ziel der gesendeten Gelder bestimmt. Eine Transaktion kann mehrere Ausgaben enthalten, die jeweils eindeutig durch die Kombination aus dem Transaktionsbezeichner (txid) und einem Index namens "vout" identifiziert werden. Dieser Index, der bei "0" beginnt, kennzeichnet die Position der Ausgabe in der Reihenfolge der Transaktionsausgaben. So wird die erste Ausgabe mit "vout" bezeichnet: 0", die zweite mit "vout": 1`, und so weiter.

Jedes "vout" kapselt in erster Linie zwei Informationen:


- der in Bitcoins ausgedrückte Wert, der den gesendeten Betrag darstellt;
- ein Sperrskript (`scriptPubKey`), das die Bedingungen festlegt, unter denen die Mittel in einer zukünftigen Transaktion wieder ausgegeben werden können.

Die Kombination aus dem "txid" und dem "vout" eines bestimmten Stücks bildet z. B. ein so genanntes UTXO:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```