---
term: SECP256R1

---
Bezeichnung für eine elliptische Kurve, die durch den NIST-Standard für die Kryptografie öffentlicher Schlüssel definiert ist. Sie verwendet ein Primzahlfeld von 256 Bit und eine elliptische Kurvengleichung $y^2 = x^3 + ax + b$ mit den Konstanten:

```text
a = -3
```

und

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Die Kurve "secp256r1" ist in vielen Protokollen weit verbreitet, wird aber nicht in Bitcoin verwendet. Tatsächlich entschied sich Satoshi Nakamoto für die Kurve "secp256k1", die 2009 noch wenig bekannt war. Der genaue Grund für diese Wahl ist unbekannt, aber es könnte daran gelegen haben, das Risiko von Hintertüren zu minimieren. Die Parameter der $k1$-Kurve sind in der Tat viel einfacher als die der $r1$-Kurve, insbesondere die Konstante $b$.

> ► *Diese Kurve wird manchmal auch "P-256" genannt.*