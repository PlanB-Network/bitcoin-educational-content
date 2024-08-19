---
term: FORMBARKEIT (TRANSAKTION)
---

Bezieht sich auf die Fähigkeit, die Struktur einer Bitcoin-Transaktion leicht zu modifizieren, ohne deren Wirkung zu verändern, aber dabei den Transaktionsidentifikator (*TXID*) zu ändern. Diese Eigenschaft kann böswillig ausgenutzt werden, um Stakeholder über den Status einer Transaktion irrezuführen, was Probleme wie doppelte Ausgaben verursachen kann. Die Formbarkeit wurde durch die Flexibilität der verwendeten digitalen Signatur ermöglicht. Der SegWit-Soft-Fork wurde insbesondere eingeführt, um diese Formbarkeit von Bitcoin-Transaktionen zu verhindern, was die Implementierung des Lightning-Netzwerks kompliziert machte. Dies wird erreicht, indem die formbaren Daten aus der Transaktion aus der TXID-Berechnung entfernt werden.

> ► *Obwohl selten, wird der Begriff "Mutabilität" manchmal verwendet, um dasselbe Konzept zu bezeichnen.*