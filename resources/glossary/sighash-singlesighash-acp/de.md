---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Typ des SigHash-Flags (`0x83`) kombiniert mit dem Modifikator `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`), der in Bitcoin-Transaktionssignaturen verwendet wird. Diese Kombination legt fest, dass die Signatur nur für eine bestimmte einzelne Eingabe und nur für die Ausgabe mit dem gleichen Index wie diese Eingabe gilt. Andere Eingaben und Ausgaben können von anderen Parteien hinzugefügt oder geändert werden. Diese Konfiguration ist nützlich für gemeinschaftliche Transaktionen, bei denen die Teilnehmer ihre eigenen Eingaben hinzufügen können, um eine bestimmte Ausgabe zu finanzieren.