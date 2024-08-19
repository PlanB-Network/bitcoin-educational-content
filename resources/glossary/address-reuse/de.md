---
term: ADDRESS REUSE
---

Die Wiederverwendung von Adressen bezieht sich auf die Praxis, dieselbe Empfangsadresse zu verwenden, um mehrere UTXOs zu blockieren, manchmal innerhalb verschiedener Transaktionen. Bitcoins werden typischerweise mit einem kryptografischen Schlüsselpaar gesperrt, das einer einzigartigen Adresse entspricht. Da die Blockchain öffentlich ist, lässt sich leicht erkennen, welche Adressen mit wie vielen Bitcoins verbunden sind. Im Falle der Wiederverwendung derselben Adresse für mehrere Zahlungen ist es vernünftig anzunehmen, dass alle zugehörigen UTXOs derselben Entität gehören. Daher stellt die Wiederverwendung von Adressen ein Problem für die Privatsphäre des Benutzers dar. Sie ermöglicht deterministische Verbindungen zwischen mehreren Transaktionen und UTXOs sowie die fortlaufende Verfolgung von Mitteln in der Blockchain. Satoshi Nakamoto erwähnte dieses Problem bereits in seinem White Paper:

> "*Als zusätzliche Schutzmaßnahme könnte für jede Transaktion ein neues Schlüsselpaar verwendet werden, um sie nicht mit einem gemeinsamen Eigentümer in Verbindung bringen zu können.*" - Nakamoto, S. (2008). "Bitcoin: Ein Peer-to-Peer Electronic Cash System". Konsultiert unter https://bitcoin.org/bitcoin.pdf.

Um die Privatsphäre mindestens zu wahren, wird dringend empfohlen, jede Empfangsadresse nur einmal zu verwenden. Für jede neue Zahlung ist es angebracht, eine neue Adresse zu generieren. Auch für Wechselgeldausgaben sollte eine frische Adresse verwendet werden. Glücklicherweise ist es dank deterministischer und hierarchischer Wallets sehr einfach geworden, eine Vielzahl von Adressen zu verwenden. Alle mit einer Wallet verbundenen Schlüsselpaare können leicht aus dem Seed regeneriert werden. Dies ist auch der Grund, warum Wallet-Software immer eine neue, unterschiedliche Adresse generiert, wenn Sie auf den „Empfangen“-Button klicken.

> ► *Auf Englisch wird es "Address Reuse" genannt.*