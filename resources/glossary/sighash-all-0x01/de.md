---
term: SIGHASH_ALL (0X01)
---

Art des SigHash-Flags, das bei Bitcoin-Transaktionssignaturen verwendet wird, um anzuzeigen, dass die Signatur für alle Komponenten der Transaktion gilt. Durch die Verwendung von `SIGHASH_ALL` deckt der Unterzeichner alle Eingaben und alle Ausgaben ab. Das bedeutet, dass weder die Eingaben noch die Ausgaben nach der Signatur ohne deren Ungültigkeitserklärung geändert werden können. Diese Art von SigHash-Flag ist die häufigste bei Bitcoin-Transaktionen, da sie die vollständige Endgültigkeit und Integrität der Transaktion gewährleistet.