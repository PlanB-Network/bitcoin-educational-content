---
term: ACCOUNT

---
In HD-Geldbörsen (Hierarchical Deterministic) stellt ein Konto eine Ableitungsebene der Tiefe 3 gemäß BIP32 dar. Jedes Konto ist fortlaufend nummeriert, beginnend mit `/0'/` (gehärtete Ableitung, also in Wirklichkeit `/2^31/` oder `/2 147 483 648/`). Auf dieser Ableitungstiefe befinden sich die bekannten `xpubs`. Heutzutage wird in der Regel nur ein Konto innerhalb einer HD-Geldbörse verwendet. Ursprünglich waren sie jedoch dazu gedacht, verschiedene Nutzungskategorien innerhalb derselben Brieftasche zu trennen. Nehmen wir zum Beispiel einen Standard-Ableitungspfad für eine externe Taproot (P2TR) Empfangsadresse: `m/86'/0'/0'/0/0`, ist der Kontoindex das zweite `/0'/`.

![](../../dictionnaire/assets/17.webp)