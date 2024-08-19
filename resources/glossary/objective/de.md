---
term: ZIEL
---

In deterministischen und hierarchischen (HD) Wallets wird das Ziel (oder _Zweck_ auf Englisch), definiert durch BIP43, als eine spezifische Ebene der Ableitung dargestellt. Dieser Index, der sich auf der ersten Tiefe des Ableitungsbaums befindet (`m / purpose' /`), identifiziert den vom Wallet angenommenen Ableitungsstandard, um die Kompatibilität zwischen verschiedenen Wallet-Verwaltungssoftwaren zu erleichtern. Zum Beispiel wird im Fall von SegWit-Adressen (BIP84) das Ziel als `/84'/` notiert. Diese Methode ermöglicht eine effiziente Organisation von Schlüsseln unter verschiedenen Arten von Adressen innerhalb desselben HD-Wallets. Die standardmäßig verwendeten Indizes sind:
* Für P2PKH: `44'`;
* Für P2WPKH-nested-in-P2SH: `49'`;
* Für P2WPKH: `84'`;
* Für P2TR: `86'`.

![](../../dictionnaire/assets/20.png)