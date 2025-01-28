---
term: SIGHASH FLAG

---
Ein Parameter in einer Bitcoin-Transaktion, der festlegt, welche Komponenten einer Transaktion (Eingaben und Ausgaben) durch die zugehörige Signatur abgedeckt sind und dadurch unveränderlich werden. Das SigHash Flag ist ein Byte, das der digitalen Signatur jeder Eingabe hinzugefügt wird. Daher wirkt sich die Wahl des SigHash Flag direkt darauf aus, welche Teile der Transaktion durch die Signatur eingefroren werden und welche nachträglich noch geändert werden können. Dieser Mechanismus stellt sicher, dass Signaturen Transaktionsdaten präzise und sicher entsprechend der Absicht des Unterzeichners festschreiben. Es gibt drei Haupt-SigHash-Flags:


- sIGHASH_ALL" (0x01): Die Signatur gilt für alle Ein- und Ausgänge der Transaktion und sperrt sie somit vollständig;
- sIGHASH_NONE" (0x02): Die Signatur gilt für alle Eingänge, aber nicht für die Ausgänge, so dass die Ausgänge nach der Signatur geändert werden können;
- sIGHASH_SINGLE" (0x03): Die Signatur umfasst alle Eingänge und nur einen Ausgang, der dem Index des signierten Eingangs entspricht.

Zusätzlich zu diesen drei SigHash-Flags kann der Modifikator `SIGHASH_ANYONECANPAY` (`0x80`) mit jedem der vorherigen Typen kombiniert werden. Wenn dieser Modifikator verwendet wird, wird nur ein Teil der Eingaben vorzeichenbehaftet, während die anderen offen für Änderungen bleiben. Hier sind die bestehenden Kombinationen mit dem Modifikator:


- sIGHASH_ALL | SIGHASH_ANYONECANPAY" (0x81"): Die Signatur gilt für eine einzige Eingabe und deckt alle Ausgaben der Transaktion ab;
- sIGHASH_NONE | SIGHASH_ANYONECANPAY" (0x82"): Die Signatur deckt eine einzige Eingabe ab, ohne eine Ausgabe zu bestätigen;
- sIGHASH_SINGLE | SIGHASH_ANYONECANPAY" (0x83"): Die Signatur gilt für eine einzige Eingabe und nur für die Ausgabe mit dem gleichen Index wie diese Eingabe.

> ► *Ein manchmal verwendetes Synonym für "SigHash" ist "Signature Hash Types"