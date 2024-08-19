---
term: SECP256K1
---

Name, der einer spezifischen elliptischen Kurve gegeben wurde, die im Bitcoin-Protokoll für die Implementierung des ECDSA (*Elliptic Curve Digital Signature Algorithm*) und der Schnorr-Digitalsignaturalgorithmen verwendet wird. Die `secp256k1` Kurve wurde vom Erfinder von Bitcoin, Satoshi Nakamoto, ausgewählt. Sie besitzt einige interessante Eigenschaften, insbesondere Leistungsvorteile.

Die Verwendung von `secp256k1` in Bitcoin bedeutet, dass jeder private Schlüssel (eine zufällige 256-Bit-Zahl) durch Addition und Verdopplung des Punktes des privaten Schlüssels durch den Generatorpunkt der `secp256k1` Kurve einem entsprechenden öffentlichen Schlüssel zugeordnet wird. Diese Operation ist in eine Richtung leicht durchzuführen, aber praktisch unmöglich umzukehren, was die Grundlage der Sicherheit von digitalen Signaturen auf Bitcoin bildet.

Die `secp256k1` Kurve wird durch die elliptische Kurvengleichung $y^2 = x^3 + 7$ spezifiziert, was bedeutet, dass sie Koeffizienten $a$ gleich $0$ und $b$ gleich $7$ in der allgemeinen Form einer elliptischen Kurvengleichung $y^2 = x^3 + ax + b$ hat. `secp256k1` ist über einem endlichen Feld definiert, dessen Ordnung eine sehr große Primzahl ist, speziell $p = 2^{256} - 2^{32} - 977$. Die Kurve hat auch eine Gruppenordnung, die die Anzahl der unterschiedlichen Punkte auf der Kurve ist, einen vordefinierten Generatorpunkt (oder Punkt $G$), der in kryptografischen Operationen zur Erzeugung von Schlüsselpaaren verwendet wird, und einen Kofaktor gleich $1$.

> ► *“SEC” steht für “Standards for Efficient Cryptography”. “P256” zeigt an, dass die Kurve über einem Feld $\mathbb{Z}_p$ definiert ist, wobei $p$ eine 256-Bit-Primzahl ist. “K” bezieht sich auf den Namen seines Erfinders, Neal Koblitz. Schließlich deutet “1” darauf hin, dass dies die erste Version dieser Kurve ist.*