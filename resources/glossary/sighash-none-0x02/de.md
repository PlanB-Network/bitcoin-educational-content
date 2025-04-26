---
term: SIGHASH_NONE (0X02)

---
Typ des SigHash-Flags, das in Bitcoin-Transaktionssignaturen verwendet wird, um anzuzeigen, dass die Signatur für alle Eingaben der Transaktion gilt, aber für keine ihrer Ausgaben. Die Verwendung von `SIGHASH_NONE` impliziert, dass der Unterzeichner sich nur auf die Eingaben verpflichtet und die Ausgaben nach der Unterzeichnung unbestimmt oder veränderbar bleiben. Diese Art von Signatur ist nützlich, wenn der Unterzeichner andere Parteien ermächtigen möchte, zu entscheiden, wie die Bitcoins in der Transaktion verteilt werden sollen.