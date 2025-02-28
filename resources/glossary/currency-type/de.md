---
term: WÄHRUNGSTYP

---
Im Zusammenhang mit deterministischen und hierarchischen (HD) Wallets ist der Währungstyp (*coin type* auf Englisch) eine Ableitungsebene, die es ermöglicht, die Zweige der Wallet auf der Grundlage der verschiedenen verwendeten Kryptowährungen zu unterscheiden. Diese Ableitungsebene, die durch BIP 44 definiert ist, befindet sich in der Tiefe 2 der Ableitungsstruktur, nach dem Hauptschlüssel und dem Zweck. Für Bitcoin ist der zugewiesene Index beispielsweise `0x80000000`, was im Ableitungspfad als `/0'/` vermerkt ist. Dies bedeutet, dass alle Adressen und Konten, die von diesem Pfad abgeleitet werden, mit Bitcoin verbunden sind. Diese Ableitungsebene ermöglicht eine klare Trennung zwischen verschiedenen Vermögenswerten in einer Mehrwährungs-Brieftasche. Hier sind die für verschiedene Kryptowährungen verwendeten Indizes:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: "0x80000001";
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)