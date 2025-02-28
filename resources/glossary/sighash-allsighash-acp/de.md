---
term: SIGHASH_ALL/SIGHASH_ACP

---
Typ des SigHash-Flags (`0x81`) kombiniert mit dem Modifikator `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`), der in Bitcoin-Transaktionssignaturen verwendet wird. Diese Kombination legt fest, dass die Signatur für alle Ausgaben und nur für eine bestimmte Eingabe der Transaktion gilt. sIGHASH_ALL | SIGHASH_ANYONECANPAY" ermöglicht es anderen Teilnehmern, der Transaktion nach der ersten Signatur weitere Eingaben hinzuzufügen. Dies ist besonders nützlich in kollaborativen Szenarien, wie z. B. Crowdfunding-Transaktionen, bei denen verschiedene Mitwirkende ihre eigenen Eingaben hinzufügen können, während die Integrität der vom Erstunterzeichner zugesagten Ausgaben gewahrt bleibt.