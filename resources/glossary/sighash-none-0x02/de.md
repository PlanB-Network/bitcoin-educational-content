---
term: SIGHASH_NONE (0X02)
---

Art des SigHash-Flags, das bei Bitcoin-Transaktionssignaturen verwendet wird, um anzuzeigen, dass die Signatur auf alle Eingaben der Transaktion, aber auf keine ihrer Ausgaben angewendet wird. Die Verwendung von `SIGHASH_NONE` impliziert, dass sich der Unterzeichner nur auf die Eingaben festlegt und zulässt, dass die Ausgaben nach der Signierung unbestimmt oder modifizierbar bleiben. Diese Art der Signatur ist nützlich in Fällen, in denen der Unterzeichner anderen Parteien die Entscheidung überlassen möchte, wie die Bitcoins in der Transaktion verteilt werden sollen.