---
term: FORMBARKEIT (TRANSAKTION)

---
Bezieht sich auf die Möglichkeit, die Struktur einer Bitcoin-Transaktion geringfügig zu verändern, ohne ihre Wirkung zu verändern, aber unter Änderung des Transaktionsidentifikators (*TXID*). Diese Eigenschaft kann böswillig ausgenutzt werden, um die Beteiligten über den Status einer Transaktion in die Irre zu führen und so Probleme wie Doppelausgaben zu verursachen. Die Fälschbarkeit wurde durch die Flexibilität der verwendeten digitalen Signatur ermöglicht. Die SegWit-Soft-Fork wurde vor allem eingeführt, um diese Fälschbarkeit von Bitcoin-Transaktionen zu verhindern, was die Implementierung des Lightning Network kompliziert macht. Dies wird dadurch erreicht, dass die verfälschbaren Daten der Transaktion aus der TXID-Berechnung entfernt werden.

> ► *Obwohl selten, wird der Begriff "Veränderlichkeit" manchmal für dasselbe Konzept verwendet