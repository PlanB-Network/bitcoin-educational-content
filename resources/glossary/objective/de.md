---
term: OBJEKTIV

---
In deterministischen und hierarchischen (HD) Geldbörsen stellt das Ziel (oder _Zweck_ im Englischen), definiert durch BIP43, eine bestimmte Ableitungsebene dar. Dieser Index, der sich in der ersten Tiefe des Ableitungsbaums befindet (`m / purpose' /`), identifiziert den Ableitungsstandard, der von der Wallet verwendet wird, um die Kompatibilität zwischen verschiedenen Wallet-Verwaltungsprogrammen zu erleichtern. Im Falle von SegWit-Adressen (BIP84) wird das Ziel beispielsweise als `/84'/` angegeben. Diese Methode ermöglicht die effiziente Organisation von Schlüsseln zwischen verschiedenen Arten von Adressen innerhalb derselben HD-Wallet. Die verwendeten Standard-Indizes sind:


- Für P2PKH: `44'`;
- Für P2WPKH-nested-in-P2SH: "49";
- Für P2WPKH: `84'`;
- Für P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)