---
term: SIGHASH_SINGLE (0X03)

---
Typ des SigHash-Flags, das in Bitcoin-Transaktionssignaturen verwendet wird, um anzuzeigen, dass die Signatur für alle Eingaben der Transaktion und nur für eine Ausgabe gilt, die dem Index der gleichen signierten Eingabe entspricht. Somit ist jede mit `SIGHASH_SINGLE` signierte Eingabe spezifisch mit einer bestimmten Ausgabe verbunden. Die anderen Ausgaben werden durch die Signatur nicht gebunden und können daher später geändert werden. Diese Art der Signatur ist bei komplexen Transaktionen nützlich, bei denen die Teilnehmer bestimmte Eingaben mit bestimmten Ausgaben verknüpfen wollen, während sie für die anderen Ausgaben der Transaktion Flexibilität zulassen.