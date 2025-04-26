---
term: HASH256

---
Kryptografische Funktion, die für verschiedene Anwendungen auf Bitcoin verwendet wird. Dabei wird die SHA256-Funktion zweimal auf die Eingabedaten angewendet. Die Nachricht wird einmal durch SHA256 geleitet, und das Ergebnis dieses Vorgangs wird als Eingabe für einen zweiten Durchlauf durch SHA256 verwendet. Die Ausgabe dieser Funktion beträgt also 256 Bit.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$