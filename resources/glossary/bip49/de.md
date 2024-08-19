---
term: BIP49
---

BIP49 ist ein informatives BIP, das die Ableitungsmethode einführt, die verwendet wird, um Nested SegWit-Adressen in einem HD-Wallet zu generieren. Der vorgeschlagene Ableitungspfad folgt den Standards von BIP43 und BIP44, mit dem Index `49'` (verstärkte Ableitung) auf der Tiefe des Ziels. Zum Beispiel würde die erste Adresse eines P2SH-P2WPKH-Kontos vom Pfad abgeleitet werden: `m/49'/0'/0'/0/0`. Nested SegWit-Skripte wurden bei der Einführung von SegWit erfunden, um dessen Annahme zu erleichtern. Sie ermöglichen die Nutzung dieses neuen Standards, selbst in Wallets, die noch nicht nativ mit SegWit kompatibel sind.