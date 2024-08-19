---
term: SIGHASH_SINGLE (0X03)
---

Art des SigHash-Flags, das bei Bitcoin-Transaktionssignaturen verwendet wird, um anzuzeigen, dass die Signatur für alle Eingaben der Transaktion gilt und nur für einen Ausgang, der dem Index der gleichen signierten Eingabe entspricht. Somit ist jede mit `SIGHASH_SINGLE` signierte Eingabe spezifisch mit einem bestimmten Ausgang verknüpft. Die anderen Ausgänge werden durch die Signatur nicht festgelegt und können daher später geändert werden. Diese Art der Signatur ist nützlich bei komplexen Transaktionen, bei denen die Teilnehmer bestimmte Eingaben mit spezifischen Ausgängen verknüpfen möchten, während sie Flexibilität für die anderen Ausgänge der Transaktion lassen.