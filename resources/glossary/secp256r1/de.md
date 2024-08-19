---
term: SECP256R1
---

Name, der einer elliptischen Kurve gegeben wurde, die durch den NIST-Standard für öffentliche Schlüsselkryptographie definiert ist. Sie verwendet ein Primzahl-Feld von 256 Bits und eine elliptische Kurvengleichung $y^2 = x^3 + ax + b$ mit den Konstanten:

```text
a = -3
```

und

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Die Kurve `secp256r1` wird in vielen Protokollen verwendet, jedoch nicht in Bitcoin. Tatsächlich entschied sich Satoshi Nakamoto für die Kurve `secp256k1`, die im Jahr 2009 noch wenig bekannt war. Der genaue Grund für diese Wahl ist unbekannt, aber es könnte gewesen sein, um das Risiko von Hintertüren zu minimieren. Die Parameter der $k1$-Kurve sind tatsächlich viel einfacher als die der $r1$-Kurve, insbesondere die Konstante $b$.

> ► *Diese Kurve wird manchmal auch "P-256" genannt.*