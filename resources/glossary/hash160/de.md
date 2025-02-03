---
term: HASH160

---
Kryptografische Funktion, die in Bitcoin verwendet wird, insbesondere zur Erzeugung von Legacy- und SegWit v0-Empfangsadressen. Sie kombiniert zwei Hash-Funktionen, die nacheinander auf die Eingabe angewendet werden: zuerst SHA256, dann RIPEMD160. Die Ausgabe dieser Funktion besteht also aus 160 Bit.

$$$text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$