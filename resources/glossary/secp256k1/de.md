---
term: SECP256K1

---
Bezeichnung für eine bestimmte elliptische Kurve, die im Bitcoin-Protokoll für die Implementierung der digitalen Signaturalgorithmen ECDSA (*Elliptic Curve Digital Signature Algorithm*) und Schnorr verwendet wird. Die Kurve "secp256k1" wurde vom Erfinder von Bitcoin, Satoshi Nakamoto, ausgewählt. Sie hat einige interessante Eigenschaften, vor allem Leistungsvorteile.

Die Verwendung von "secp256k1" in Bitcoin bedeutet, dass jeder private Schlüssel (eine 256-Bit-Zufallszahl) durch Addition und Verdoppelung des Punktes des privaten Schlüssels mit dem Generatorpunkt der "secp256k1"-Kurve auf einen entsprechenden öffentlichen Schlüssel abgebildet wird. Dieser Vorgang ist in eine Richtung leicht durchführbar, aber praktisch nicht umkehrbar, was die Grundlage für die Sicherheit digitaler Signaturen auf Bitcoin bildet.

Die Kurve `secp256k1` ist durch die elliptische Kurvengleichung $y^2 = x^3 + 7$ spezifiziert, d.h. sie hat Koeffizienten $a$ gleich $0$ und $b$ gleich $7$ in der allgemeinen Form einer elliptischen Kurvengleichung $y^2 = x^3 + ax + b$. `secp256k1` ist über einem endlichen Feld definiert, dessen Ordnung eine sehr große Primzahl ist, nämlich $p = 2^{256} - 2^{32} - 977$. Die Kurve hat außerdem eine Gruppenordnung, d. h. die Anzahl der verschiedenen Punkte auf der Kurve, einen vordefinierten Generatorpunkt (oder Punkt $G$), der bei kryptographischen Operationen zur Erzeugung von Schlüsselpaaren verwendet wird, und einen Kofaktor gleich $1$.

> ► *"SEC" steht für "Standards for Efficient Cryptography". "P256" bedeutet, dass die Kurve über einem Feld $\mathbb{Z}_p$ definiert ist, wobei $p$ eine 256-Bit-Primzahl ist. "K" bezieht sich auf den Namen des Erfinders, Neal Koblitz. Schließlich zeigt "1" an, dass dies die erste Version dieser Kurve ist