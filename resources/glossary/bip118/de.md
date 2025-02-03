---
term: BIP118

---
Vorschlag zur Verbesserung von Bitcoin mit dem Ziel, zwei neue SigHash-Flag-Modifikatoren einzuführen: `SIGHASH_ANYPREVOUT` und `SIGHASH_ANYPREVOUTANYSCRIPT`. Diese Funktionen erweitern die Möglichkeiten von Bitcoin-Transaktionen, insbesondere im Hinblick auf intelligente Verträge und Overlay-Lösungen wie das Lightning Network. BIP118 würde vor allem die Verwendung von Eltoo ermöglichen. Der Hauptvorteil von `SIGHASH_ANYPREVOUT` besteht darin, dass die Wiederverwendung von Signaturen über mehrere Transaktionen hinweg ermöglicht wird, was mehr Flexibilität bietet. Insbesondere ermöglichen diese SigHashes eine Signatur, die keine der Eingaben der Transaktion abdeckt.