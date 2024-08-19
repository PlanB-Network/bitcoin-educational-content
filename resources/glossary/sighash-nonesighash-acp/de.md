---
term: SIGHASH_NONE/SIGHASH_ACP
---

Art des SigHash-Flags (`0x82`), kombiniert mit dem `SIGHASH_ANYONECANPAY`-Modifier (`SIGHASH_ACP`), verwendet in Bitcoin-Transaktionssignaturen. Diese Kombination zeigt an, dass die Signatur nur für einen spezifischen Input gilt, ohne sich auf irgendeinen Output festzulegen. Dies ermöglicht es anderen Teilnehmern, frei zusätzliche Inputs hinzuzufügen und alle Outputs der Transaktion zu modifizieren.