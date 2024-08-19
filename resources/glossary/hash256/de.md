---
term: HASH256
---

Kryptografische Funktion, die für verschiedene Anwendungen bei Bitcoin verwendet wird. Sie beinhaltet die zweimalige Anwendung der SHA256-Funktion auf die Eingabedaten. Die Nachricht wird einmal durch SHA256 geleitet, und das Ergebnis dieser Operation wird als Eingabe für einen zweiten Durchlauf durch SHA256 verwendet. Die Ausgabe dieser Funktion ist daher 256 Bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$