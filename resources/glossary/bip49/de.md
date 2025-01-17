---
term: BIP49

---
BIP49 ist ein informatives BIP, das die Ableitungsmethode vorstellt, die zur Generierung von Nested SegWit-Adressen in einer HD-Wallet verwendet wird. Der vorgeschlagene Ableitungspfad folgt den Standards von BIP43 und BIP44, wobei der Index "49" (gehärtete Ableitung) in der Tiefe des Ziels steht. Zum Beispiel würde die erste Adresse eines P2SH-P2WPKH-Kontos aus dem Pfad abgeleitet werden: `m/49'/0'/0'/0/0`. Verschachtelte SegWit-Skripte wurden bei der Einführung von SegWit erfunden, um seine Einführung zu erleichtern. Sie ermöglichen die Verwendung dieses neuen Standards, auch auf Geldbörsen, die noch nicht nativ mit SegWit kompatibel sind.