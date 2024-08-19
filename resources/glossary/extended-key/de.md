---
term: ERWEITERTER SCHLÜSSEL
---

Eine Zeichenfolge, die einen Schlüssel (öffentlich oder privat), den zugehörigen Chain-Code und eine Reihe von Metadaten kombiniert. Ein erweiterter Schlüssel fasst alle Elemente, die für die Ableitung von Kinderschlüsseln notwendig sind, in einem einzigen Identifikator zusammen. Sie werden in deterministischen und hierarchischen Wallets verwendet und können zwei Typen haben: einen erweiterten öffentlichen Schlüssel (zur Ableitung von Kind-öffentlichen Schlüsseln verwendet) oder einen erweiterten privaten Schlüssel (zur Ableitung von Kind-privaten und -öffentlichen Schlüsseln verwendet). Ein erweiterter Schlüssel umfasst also mehrere verschiedene Datenstücke, beschrieben in BIP32, in der Reihenfolge:
* Das Präfix: `prv` und `pub` sind HRP (Human Readable Part), die angeben, ob es sich um einen erweiterten privaten Schlüssel (`prv`) oder einen erweiterten öffentlichen Schlüssel (`pub`) handelt. Der erste Buchstabe des Präfixes bezeichnet die Version des erweiterten Schlüssels: `x` für Legacy oder SegWit V1 auf Bitcoin, `t` für Legacy oder SegWit V1 auf Bitcoin Testnet, `y` für Nested SegWit auf Bitcoin, `u` für Nested SegWit auf Bitcoin Testnet, `z` für SegWit V0 auf Bitcoin, `v` für SegWit V0 auf Bitcoin Testnet.
* Die Tiefe, die die Anzahl der Ableitungen vom Master-Schlüssel bis zum erweiterten Schlüssel angibt;
* Der Eltern-Fingerabdruck. Dies repräsentiert die ersten 4 Bytes des `HASH160` des Eltern-öffentlichen Schlüssels;
* Der Index. Dies ist die Nummer des Paares unter seinen Geschwistern, von dem der erweiterte Schlüssel abgeleitet ist;
* Der Chain-Code;
* Ein Padding-Byte, falls es sich um einen privaten Schlüssel handelt `0x00`;
* Der private oder öffentliche Schlüssel;
* Eine Prüfsumme. Sie repräsentiert die ersten 4 Bytes des `HASH256` des Rests des erweiterten Schlüssels.

In der Praxis wird der erweiterte öffentliche Schlüssel verwendet, um Empfangsadressen zu generieren und die Transaktionen eines Kontos zu beobachten, ohne die zugehörigen privaten Schlüssel preiszugeben. Dies kann beispielsweise die Erstellung einer sogenannten "Watch-Only"-Wallet ermöglichen. Es ist jedoch wichtig zu beachten, dass der erweiterte öffentliche Schlüssel sensible Informationen für die Privatsphäre des Benutzers darstellt, da seine Offenlegung Dritten das Nachverfolgen von Transaktionen und das Sehen des Guthabens des zugehörigen Kontos ermöglichen kann.