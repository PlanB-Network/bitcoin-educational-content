---
term: ZIEL
---

In deterministischen und hierarchischen (HD) Portfolios stellt der Zweck, definiert durch BIP43, eine spezifische Ableitungsebene dar. Dieser Index, der sich in der ersten Tiefe des Ableitungsbaums befindet (`m / Zweck' /`), identifiziert den vom Portfolio angenommenen Ableitungsstandard, um die Kompatibilität zwischen verschiedenen Portfolioverwaltungsprogrammen zu erleichtern. Im Falle von SegWit-Adressen (BIP84) wird der Zweck beispielsweise als `/84'/` angegeben. Diese Methode ermöglicht eine effiziente Organisation der Schlüssel zwischen verschiedenen Address-Typen innerhalb eines einzigen HD-Portfolios. Die verwendeten Standardindizes sind:




- Für P2PKH: `44'` ;
- Für P2WPKH-nested-in-P2SH: `49'` ;
- Für P2WPKH: `84'` ;
- Für P2TR: `86'`.