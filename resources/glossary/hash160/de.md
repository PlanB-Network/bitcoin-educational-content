---
term: HASH160
---

Kryptografische Funktion, die in Bitcoin verwendet wird, insbesondere für die Generierung von Legacy- und SegWit v0 Empfangsadressen. Sie kombiniert zwei Hash-Funktionen, die nacheinander auf die Eingabe ausgeführt werden: zuerst SHA256, dann RIPEMD160. Die Ausgabe dieser Funktion ist daher 160 Bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$