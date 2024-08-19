---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Art des SigHash-Flags (`0x83`) in Kombination mit dem `SIGHASH_ANYONECANPAY`-Modifikator (`SIGHASH_ACP`), verwendet in Bitcoin-Transaktionssignaturen. Diese Kombination legt fest, dass die Signatur nur für einen spezifischen einzelnen Eingang gilt und nur für den Ausgang, der denselben Index wie dieser Eingang hat. Andere Eingänge und Ausgänge können von anderen Parteien hinzugefügt oder modifiziert werden. Diese Konfiguration ist nützlich für kollaborative Transaktionen, bei denen Teilnehmer ihre eigenen Eingänge hinzufügen können, um einen spezifischen Ausgang zu finanzieren.