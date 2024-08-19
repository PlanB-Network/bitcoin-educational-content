---
term: SIGHASH FLAG
---

Ein Parameter in einer Bitcoin-Transaktion, der bestimmt, welche Komponenten einer Transaktion (Eingaben und Ausgaben) von der zugehörigen Signatur abgedeckt und somit unveränderlich gemacht werden. Der SigHash Flag ist ein Byte, das der digitalen Signatur jeder Eingabe hinzugefügt wird. Daher beeinflusst die Wahl des SigHash Flag direkt, welche Teile der Transaktion durch die Signatur eingefroren werden und welche nachträglich noch modifiziert werden können. Dieser Mechanismus stellt sicher, dass Signaturen Transaktionsdaten präzise und sicher gemäß der Absicht des Unterzeichners festlegen. Es gibt drei Haupt-SigHash Flags:

- `SIGHASH_ALL` (`0x01`): Die Signatur gilt für alle Eingaben und Ausgaben der Transaktion und sperrt diese somit vollständig;

- `SIGHASH_NONE` (`0x02`): Die Signatur gilt für alle Eingaben, aber keine der Ausgaben, was es ermöglicht, die Ausgaben nach der Signatur zu modifizieren;

- `SIGHASH_SINGLE` (`0x03`): Die Signatur deckt alle Eingaben und nur eine Ausgabe ab, die dem Index der signierten Eingabe entspricht.

Zusätzlich zu diesen drei SigHash Flags kann der Modifikator `SIGHASH_ANYONECANPAY` (`0x80`) mit jedem der vorherigen Typen kombiniert werden. Wenn dieser Modifikator verwendet wird, wird nur ein Teil der Eingaben signiert, wodurch die anderen für Modifikationen offen bleiben. Hier sind die existierenden Kombinationen mit dem Modifikator:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Die Signatur gilt für eine einzelne Eingabe und deckt alle Ausgaben der Transaktion ab;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Die Signatur deckt eine einzelne Eingabe ab, ohne sich auf eine Ausgabe festzulegen;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Die Signatur gilt für eine einzelne Eingabe und nur für die Ausgabe, die denselben Index wie diese Eingabe hat.

> ► *Ein Synonym, das manchmal für "SigHash" verwendet wird, ist "Signature Hash Types".*