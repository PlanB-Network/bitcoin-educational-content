---
term: SIGHASH_ALL/SIGHASH_ACP
---

Art des SigHash-Flags (`0x81`), kombiniert mit dem `SIGHASH_ANYONECANPAY`-Modifikator (`SIGHASH_ACP`), der in Bitcoin-Transaktionssignaturen verwendet wird. Diese Kombination legt fest, dass die Signatur für alle Ausgaben und nur für einen spezifischen Eingang der Transaktion gilt. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` ermöglicht es anderen Teilnehmern, nach der ursprünglichen Signatur zusätzliche Eingaben zur Transaktion hinzuzufügen. Dies ist besonders nützlich in kollaborativen Szenarien, wie bei Crowdfunding-Transaktionen, wo verschiedene Beitragszahler ihre eigenen Eingaben hinzufügen können, während die Integrität der von dem ursprünglichen Unterzeichner festgelegten Ausgaben bewahrt bleibt.