---
term: SIGHASH_NONE/SIGHASH_ACP
definition: SigHash-kombination som signerar en specifik input utan att binda sig till någon output.
---

Typ av SigHash-flagga (`0x82`) kombinerad med modifieraren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som används i Bitcoin-transaktionssignaturer. Denna kombination anger att signaturen endast gäller för en specifik inmatning, utan att binda sig till någon utmatning. Detta gör det möjligt för andra deltagare att fritt lägga till ytterligare inmatningar och modifiera alla transaktionens utmatningar.