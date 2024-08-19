---
term: BIP118
---

Vorschlag zur Verbesserung von Bitcoin, der darauf abzielt, zwei neue SigHash-Flag-Modifikatoren einzuführen: `SIGHASH_ANYPREVOUT` und `SIGHASH_ANYPREVOUTANYSCRIPT`. Diese Funktionen erweitern die Fähigkeiten von Bitcoin-Transaktionen, insbesondere im Hinblick auf Smart Contracts und Overlay-Lösungen wie das Lightning Network. BIP118 würde insbesondere die Verwendung von Eltoo ermöglichen. Der Hauptvorteil von `SIGHASH_ANYPREVOUT` besteht darin, dass die Wiederverwendung von Signaturen über mehrere Transaktionen hinweg ermöglicht wird, was mehr Flexibilität bietet. Speziell erlauben diese SigHashes eine Signatur, die keine der Eingaben der Transaktion abdeckt.