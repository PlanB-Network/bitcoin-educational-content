---
term: WÄHRUNGSTYP
---

Im Kontext von deterministischen und hierarchischen (HD) Wallets ist der Währungstyp (*coin type* auf Englisch) eine Ebene der Ableitung, die es ermöglicht, die Zweige des Wallets basierend auf den verschiedenen verwendeten Kryptowährungen zu unterscheiden. Diese Ableitungsebene, definiert durch BIP 44, befindet sich auf der Tiefe 2 der Ableitungsstruktur, folgend auf den Master-Schlüssel und den Zweck. Zum Beispiel ist für Bitcoin der zugewiesene Index `0x80000000`, notiert als `/0'/` im Ableitungspfad. Das bedeutet, dass alle Adressen und Konten, die von diesem Pfad abgeleitet werden, mit Bitcoin assoziiert sind. Diese Ebene der Ableitung ermöglicht eine klare Trennung verschiedener Vermögenswerte in einem Multi-Währungs-Wallet. Hier sind die Indizes, die für verschiedene Kryptowährungen verwendet werden:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)