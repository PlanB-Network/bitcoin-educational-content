---
term: HAUPTSCHLÜSSEL
---

Im Kontext von HD (Hierarchisch Deterministischen) Wallets ist der Hauptschlüssel ein einzigartiger privater Schlüssel, der aus dem Seed der Wallet abgeleitet wird. Um den Hauptschlüssel zu erhalten, wird die Funktion `HMAC-SHA512` auf den Seed angewendet, wobei die Wörter "*Bitcoin seed*" wörtlich als Schlüssel verwendet werden. Das Ergebnis dieser Operation erzeugt eine 512-Bit-Ausgabe, wobei die ersten 256 Bits den Hauptschlüssel bilden und die verbleibenden 256 Bits den Hauptketten-Code formen. Der Hauptschlüssel und der Hauptketten-Code dienen als Ausgangspunkt für die Ableitung aller Kind-privaten und öffentlichen Schlüssel in der Baumstruktur der HD-Wallet. Daher befindet sich der Hauptschlüssel auf der Ableitungstiefe 0.

![](../../dictionnaire/assets/19.png)