---
term: SIGHASH_ALL/SIGHASH_ACP
definition: SigHash-kombination som gör det möjligt att lägga till inputs efter den ursprungliga signaturen.
---

Typ av SigHash-flagga (`0x81`) kombinerad med modifieraren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som används i Bitcoin-transaktionssignaturer. Denna kombination anger att signaturen gäller för alla utgångar och endast för en viss ingång i transaktionen. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` gör det möjligt för andra deltagare att lägga till ytterligare input i transaktionen efter den första signeringen. Det är särskilt användbart i samarbetsscenarier, t.ex. crowdfunding-transaktioner, där olika bidragsgivare kan lägga till sina egna inmatningar samtidigt som integriteten för de utmatningar som den ursprungliga undertecknaren har åtagit sig bevaras.