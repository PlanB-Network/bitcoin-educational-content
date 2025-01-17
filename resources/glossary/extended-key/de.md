---
term: EXTENDED KEY

---
Eine Zeichenfolge, die einen (öffentlichen oder privaten) Schlüssel, den zugehörigen Kettencode und eine Reihe von Metadaten kombiniert. Ein erweiterter Schlüssel fasst alle Elemente, die für die Ableitung von Unterschlüsseln erforderlich sind, in einem einzigen Bezeichner zusammen. Sie werden in deterministischen und hierarchischen Wallets verwendet und können zwei Arten haben: einen erweiterten öffentlichen Schlüssel (zur Ableitung von öffentlichen Unterschlüsseln) oder einen erweiterten privaten Schlüssel (zur Ableitung von privaten und öffentlichen Unterschlüsseln). Ein erweiterter Schlüssel enthält also mehrere verschiedene Daten, die in BIP32 in dieser Reihenfolge beschrieben sind:


- Das Präfix: `prv` und `pub` sind HRP (Human Readable Part) und zeigen an, ob es sich um einen erweiterten privaten Schlüssel (`prv`) oder einen erweiterten öffentlichen Schlüssel (`pub`) handelt. Der erste Buchstabe des Präfixes bezeichnet die Version des erweiterten Schlüssels: `x` für Legacy oder SegWit V1 auf Bitcoin, `t` für Legacy oder SegWit V1 auf Bitcoin Testnet, `y` für Nested SegWit auf Bitcoin, `u` für Nested SegWit auf Bitcoin Testnet, `z` für SegWit V0 auf Bitcoin, `v` für SegWit V0 auf Bitcoin Testnet.
- Die Tiefe, die die Anzahl der Ableitungen vom Hauptschlüssel angibt, um den erweiterten Schlüssel zu erreichen;
- Der übergeordnete Fingerabdruck. Dies sind die ersten 4 Bytes des `HASH160` des übergeordneten öffentlichen Schlüssels;
- Der Index. Dies ist die Nummer des Paares unter seinen Geschwistern, von dem der erweiterte Schlüssel abgeleitet wird;
- Der Kettencode;
- Ein Auffüllungsbyte, wenn es sich um einen privaten Schlüssel "0x00" handelt;
- Der private oder öffentliche Schlüssel;
- Eine Prüfsumme. Es handelt sich um die ersten 4 Bytes des `HASH256` des Restes des erweiterten Schlüssels.

In der Praxis wird der erweiterte öffentliche Schlüssel verwendet, um Empfangsadressen zu generieren und die Transaktionen eines Kontos zu beobachten, ohne die zugehörigen privaten Schlüssel offenzulegen. Dies kann beispielsweise die Erstellung einer sogenannten "Watch-only"-Brieftasche ermöglichen. Es ist jedoch zu beachten, dass der erweiterte öffentliche Schlüssel eine sensible Information für die Privatsphäre des Nutzers darstellt, da seine Offenlegung es Dritten ermöglichen kann, Transaktionen nachzuvollziehen und den Kontostand des zugehörigen Kontos einzusehen.