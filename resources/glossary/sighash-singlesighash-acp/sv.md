---
term: SIGHASH_SINGLE/SIGHASH_ACP
definition: Kombination som signerar endast en input och endast outputen med samma index.
---

Typ av SigHash-flagga (`0x83`) kombinerad med modifieraren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som används i Bitcoin-transaktionssignaturer. Denna kombination anger att signaturen endast gäller för en specifik enskild inmatning och endast för den utmatning som har samma index som denna inmatning. Andra inmatningar och utmatningar kan läggas till eller ändras av andra parter. Denna konfiguration är användbar för samarbetstransaktioner där deltagarna kan lägga till sina egna inmatningar för att finansiera en viss utmatning.