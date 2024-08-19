---
term: KONTO
---

In HD (Hierarchisch Deterministischen) Wallets stellt ein Konto eine Ableitungsebene in der Tiefe 3 gemäß BIP32 dar. Jedes Konto wird sequenziell nummeriert, beginnend mit `/0'/` (gehärtete Ableitung, also in Wirklichkeit `/2^31/` oder `/2 147 483 648/`). Es ist auf dieser Ableitungstiefe, dass die bekannten `xpubs` lokalisiert sind. Heutzutage wird typischerweise nur ein Konto innerhalb eines HD-Wallets verwendet. Ursprünglich wurden sie jedoch konzipiert, um verschiedene Kategorien der Nutzung innerhalb desselben Wallets zu trennen. Zum Beispiel, wenn wir einen Standard-Ableitungspfad für eine externe Taproot (P2TR) Empfangsadresse nehmen: `m/86'/0'/0'/0/0`, ist der Kontenindex das zweite `/0'/`.

![](../../dictionnaire/assets/17.png)